import json, re, subprocess, ssl, urllib.request, urllib.parse, os

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

# --- PostProxy ---
PP_AUTH = "Bearer 4dfbb65f8ef8a54297ec64919aeb375e93d27cf6ca9ab732"
PP_BASE = "https://api.postproxy.dev"
IG_PROFILE = "AnUeOa"
FB_PROFILE = "v2Uk1v"
FB_PAGE_ID = "105951367482831"

# --- Media hosting: public GitHub repo (raw.githubusercontent.com), NOT cPanel/FTP ---
# cPanel (trutek.com.br, ports 21/22/2083/2087) is firewalled off from this environment's
# egress -- confirmed repeatedly reset at the TLS layer. Do not attempt it. Use GitHub instead:
# repo diegozietek-commits/diwizi-reels, media committed under reels/, served via
# raw.githubusercontent.com (plain HTTPS/443, always reachable). See Step 4 below for the flow.
GITHUB_OWNER = "diegozietek-commits"
GITHUB_REPO = "diwizi-reels"
GITHUB_WORKSPACE = "/workspace/diwizi-reels"

FONTS_DIR = "/tmp/social_fonts"
SERIF_BOLD = f"{FONTS_DIR}/SourceSerif4-Bold.ttf"
SANS = f"{FONTS_DIR}/Inter-Bold.ttf"

WHITE = "0xFFFFFF"
CREAM = "0xF3F2F2"
ACCENTS = {
    "magenta": "0xD6006C",
    "teal": "0x0B7A75",
    "amber": "0xC26B00",
    "indigo": "0x3A3AA0",
}
ACCENT_ORDER = ["magenta", "teal", "amber", "indigo"]

# Curated, verified-working royalty-free Pexels photos (no API key needed -- images.pexels.com
# is reachable from this environment; most other stock hosts, e.g. picsum/unsplash/pixabay/imgur,
# are NOT reachable here, gateway returns 403). Crops to 1080x1350 portrait via center-crop, so
# IDs were picked/checked to keep their subject roughly centered (avoid wide shots with the
# subject near an edge -- verify any NEW id you add the same way before trusting it).
PHOTO_BANK = {
    "meeting_handshake": 3184291,   # team handshake, office
    "meeting_results": 3182773,     # team around laptops/tablet showing a results screen
    "analytics_charts": 590016,     # charts + laptop on wood desk
    "analytics_pie": 265087,        # laptop + tablet, bar/pie charts
    "tech_server": 1181316,         # person with tablet in a server room
    "lifestyle_coffee": 4126724,    # coffee + laptop, casual creative work
    # "funny_confused": 3760607,    # DEAD as of 2026-08-04 (confirmed via curl -- images.pexels.com
    # returns 500 for this id specifically, not a proxy/network issue -- other ids in this bank
    # return 200 fine over the same connection). Also tried replacement id 4491471 (Pexels search
    # hit for "confused face"), also 500. Have not found a working "puzzled/confused" replacement
    # yet -- Pexels' own search pages (www.pexels.com) are not reachable from this environment to
    # browse for one. Until a verified id is added here, meme-style posts fall back to
    # "meeting_results" (works fine for a "staring at the results, confused" angle) or whichever
    # bank photo's expression best fits. If you find and verify a working confused/puzzled id,
    # uncomment a line like it above with the new id.
}


def photo_url(photo_id):
    return f"https://images.pexels.com/photos/{photo_id}/pexels-photo-{photo_id}.jpeg?auto=compress&cs=tinysrgb&w=1080"


def download_photo(key, out_path="/tmp/social_photo.jpg"):
    photo_id = PHOTO_BANK[key]
    req = urllib.request.Request(photo_url(photo_id), headers={"User-Agent": UA})
    with urllib.request.urlopen(req, context=CTX, timeout=30) as resp, open(out_path, "wb") as f:
        f.write(resp.read())
    return out_path


def setup_assets():
    os.makedirs(FONTS_DIR, exist_ok=True)
    if not os.path.exists(SERIF_BOLD):
        urllib.request.urlretrieve(
            "https://raw.githubusercontent.com/adobe-fonts/source-serif/release/TTF/SourceSerif4-Bold.ttf",
            SERIF_BOLD,
        )
    if not os.path.exists(SANS):
        urllib.request.urlretrieve(
            "https://raw.githubusercontent.com/google/fonts/main/ofl/inter/Inter%5Bopsz%2Cwght%5D.ttf",
            SANS,
        )


def safe_text(t):
    # NOTE: do NOT escape '%' -- ffmpeg drawtext's default text-expansion chokes on lone '%'
    # ("Stray % near ..." and the whole drawtext silently drops). Fixed here by disabling
    # expansion (expansion=none) on every drawtext call instead of escaping percent signs.
    return t.replace("\\", "\\\\").replace("'", "’").replace(":", "\\:")


def _dt(fontfile, text, **opts):
    parts = [f"drawtext=fontfile={fontfile}:text='{safe_text(text)}':expansion=none"]
    for k, v in opts.items():
        parts.append(f"{k}={v}")
    return ":".join(parts)


def build_image_card(out_path, photo_path, hook, points, cta, accent_name="magenta"):
    """Real photo on top ~55%, solid accent-color card on bottom with hook/points/cta.
    Use for blog-promo / tip / consulting-offer content."""
    W, H = 1080, 1350
    accent = ACCENTS[accent_name]
    CARD_Y = 760
    draws = [
        f"drawbox=x=0:y=0:w={W}:h=170:color=0x000000@0.32:t=fill",
        _dt(SANS, "diwizi.", fontcolor=WHITE, fontsize=46, x=70, y=70),
        f"drawbox=x=0:y={CARD_Y}:w={W}:h={H-CARD_Y}:color={accent}:t=fill",
        _dt(SERIF_BOLD, hook, fontcolor=WHITE, fontsize=58, x=70, y=CARD_Y + 45, line_spacing=8),
    ]
    y0, gap = CARD_Y + 200, 62
    for i, p in enumerate(points):
        draws.append(_dt(SANS, p, fontcolor=CREAM, fontsize=34, x=70, y=y0 + i * gap))
    draws.append(
        _dt(SANS, cta, fontcolor=accent, fontsize=34, box=1, boxcolor=f"{WHITE}@0.95", boxborderw=20, x=70, y=H - 95)
    )
    vf = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}," + ",".join(draws)
    cmd = ["ffmpeg", "-y", "-i", photo_path, "-vf", vf, "-frames:v", "1", out_path]
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode == 0, r.stderr[-3000:]


def build_image_meme(out_path, photo_path, top_text, bottom_text, accent_name="magenta"):
    """Full-bleed photo, bold top caption bar + bottom caption (classic meme format).
    Use for humor/relatable-industry-pain posts. Keep top_text <= 2 short lines,
    bottom_text <= 2 short lines (use '\\n' to force a line break -- ffmpeg drawtext does
    not auto-wrap, long single lines will run off both edges)."""
    W, H = 1080, 1350
    accent = ACCENTS[accent_name]
    draws = [
        f"drawbox=x=0:y=0:w={W}:h=280:color=0x000000@0.55:t=fill",
        _dt(SERIF_BOLD, top_text, fontcolor=WHITE, fontsize=62, x="(w-text_w)/2", y=70, line_spacing=10),
        f"drawbox=x=0:y={H-190}:w={W}:h=190:color=0x000000@0.62:t=fill",
        _dt(SANS, bottom_text, fontcolor=WHITE, fontsize=34, x="(w-text_w)/2", y=H - 145, line_spacing=6),
        _dt(SANS, "diwizi.", fontcolor=accent, fontsize=34, box=1, boxcolor=f"{WHITE}@0.9", boxborderw=14,
            x="(w-text_w)/2", y=H - 60),
    ]
    vf = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}," + ",".join(draws)
    cmd = ["ffmpeg", "-y", "-i", photo_path, "-vf", vf, "-frames:v", "1", out_path]
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode == 0, r.stderr[-3000:]


# --- Blog cards (for "promote a blog post" content type) ---
def fetch_index_html():
    req = urllib.request.Request("https://diwizi.com/blog/index.html", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, context=CTX, timeout=30) as resp:
        return resp.read().decode("utf-8")


def parse_cards(html):
    card_re = re.compile(
        r'<article class="article-card" data-category="(?P<category>[^"]*)">\s*'
        r'<a href="(?P<href>[^"]*)" class="card-link">\s*'
        r'<div class="article-image">\s*'
        r'<img src="(?P<img>[^"]*)" alt="(?P<alt>[^"]*)"[^>]*>\s*'
        r'</div>\s*'
        r'<div class="card-body">\s*'
        r'<div class="card-meta">\s*'
        r'<span class="category-tag">(?P<category_tag>[^<]*)</span>\s*'
        r'<span class="difficulty (?P<diff_class>[^"]*)">(?P<difficulty>[^<]*)</span>\s*'
        r'</div>\s*'
        r'<h2 class="card-title">(?P<title>.*?)</h2>\s*'
        r'<p class="card-description">(?P<description>.*?)</p>\s*'
        r'<div class="card-footer">\s*'
        r'<span class="read-time">[^<]*?(?P<read_time>\d+) min read</span>',
        re.DOTALL,
    )
    def unesc(s):
        return (s.replace("&amp;", "&").replace("&#39;", "'").replace("&quot;", '"')
                 .replace("&lt;", "<").replace("&gt;", ">").strip())
    cards = []
    for m in card_re.finditer(html):
        d = m.groupdict()
        cards.append({
            "category": unesc(d["category"]), "href": d["href"],
            "title": unesc(d["title"]), "description": unesc(d["description"]),
        })
    return cards


# --- PostProxy API ---
def pp_get(path, params=None):
    qs = ("?" + urllib.parse.urlencode(params)) if params else ""
    req = urllib.request.Request(PP_BASE + path + qs, headers={"Authorization": PP_AUTH})
    with urllib.request.urlopen(req, context=CTX, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def pp_post(path, payload):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        PP_BASE + path, data=data,
        headers={"Authorization": PP_AUTH, "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=30) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode("utf-8"))


def list_recent_posts(per_page=20):
    d = pp_get("/api/posts", {"page": 1, "per_page": per_page})
    return d.get("data", [])


def publish_image_post(image_url, caption, first_comment=None):
    payload = {
        "post": {"body": caption},
        "profiles": [IG_PROFILE, FB_PROFILE],
        "media": [image_url],
        "platforms": {
            "instagram": {"format": "post"},
            "facebook": {"format": "post", "page_id": FB_PAGE_ID},
        },
    }
    if first_comment:
        payload["platforms"]["instagram"]["first_comment"] = first_comment
        payload["platforms"]["facebook"]["first_comment"] = first_comment
    return pp_post("/api/posts", payload)
