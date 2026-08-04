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
# egress -- confirmed repeatedly reset at the TLS layer during testing on 2026-08-03. Do not
# attempt it or waste time re-diagnosing it. Use GitHub instead: repo
# diegozietek-commits/diwizi-reels, media committed under reels/, served via
# raw.githubusercontent.com (plain HTTPS/443, always reachable). See Step 4 for the flow.
# A reference copy of this whole file also lives in that repo as socialkit_image_posts.py --
# if these embedded instructions ever look stale, pull that file and follow it instead.
GITHUB_OWNER = "diegozietek-commits"
GITHUB_REPO = "diwizi-reels"
GITHUB_WORKSPACE = "/workspace/diwizi-reels"

FONTS_DIR = "/tmp/social_fonts"
SERIF_BOLD = f"{FONTS_DIR}/SourceSerif4-Bold.ttf"
SANS = f"{FONTS_DIR}/Inter-Bold.ttf"

# --- Brand palette, lifted verbatim from diwizi.com's :root CSS vars (checked 2026-08-04) ---
# --charcoal:#201E1D  --charcoal-soft:#3A3735  --cream:#F3F2F2  --white:#FFFFFF
# --magenta:#D6006C   --magenta-soft:#FF90B1   --gray:#6E6A67   --border:#E4E1DE
# --serif:'Source Serif 4'  --sans:'Inter'
WHITE = "0xFFFFFF"
CREAM = "0xF3F2F2"
CHARCOAL = "0x201E1D"
CHARCOAL_SOFT = "0x3A3735"
BRAND_MAGENTA = "0xD6006C"
MAGENTA_SOFT = "0xFF90B1"
GRAY = "0x6E6A67"

# Accents are now BRAND-ONLY. The old teal/amber/indigo were invented here and appear nowhere on
# diwizi.com -- they were the main reason posts read as disconnected from the site (Diego,
# 2026-08-04). Variety now comes from the real palette (magenta is the primary; charcoal tones are
# the neutral alternates), not from off-brand hues. Legacy key names are kept as aliases so any
# older caller passing accent_name="teal" still renders something on-brand instead of KeyError-ing.
ACCENTS = {
    "magenta": BRAND_MAGENTA,
    "charcoal": CHARCOAL,
    "charcoal_soft": CHARCOAL_SOFT,
    "magenta_soft": MAGENTA_SOFT,
    # legacy aliases -> nearest brand tone
    "teal": CHARCOAL,
    "amber": CHARCOAL_SOFT,
    "indigo": CHARCOAL,
}
ACCENT_ORDER = ["magenta", "charcoal", "magenta", "charcoal_soft"]

# Curated, verified-working royalty-free Pexels photos (no API key needed -- images.pexels.com
# is reachable from this environment; most other stock hosts, e.g. picsum/unsplash/pixabay/imgur,
# are NOT reachable here, gateway returns 403). Crops to 1080x1350 portrait via center-crop, so
# IDs were picked/checked to keep their subject roughly centered (avoid wide shots with the
# subject near an edge -- verify any NEW id you add the same way, by rendering + Reading it,
# before trusting it. Feel free to add more verified IDs over time to widen variety).
# THE PHOTO MUST MATCH THE POST'S SUBJECT. Diego flagged this on 2026-08-04 after a house-cleaning
# post went out over a photo of a desk covered in laptops -- "o que tem a ver uma mesa com
# notebook?". The generic office/analytics shots below are ONLY for genuinely generic topics
# (pricing, agency-vs-freelancer, account audits). Whenever a post is about a specific INDUSTRY --
# cleaning, tourism, legal, mortgage, ecommerce, SaaS -- use a photo of THAT industry. If the bank
# has nothing that fits, find a new one instead of settling: WebSearch "pexels.com/photo <topic>"
# to get candidate ids, verify each with verify_photo(id) (must be 200 -- ids do go dead, see
# funny_confused below), then render it and LOOK at the result before publishing, since the
# 1080x1350 centre-crop can decapitate a subject that sits near an edge. Add keepers here.
PHOTO_BANK = {
    # --- generic business / data (use only when the topic really is generic) ---
    "meeting_handshake": 3184291,   # team handshake, office
    "meeting_results": 3182773,     # team around laptops/tablet showing a results screen
    "analytics_charts": 590016,     # charts + laptop on wood desk
    "analytics_pie": 265087,        # laptop + tablet, bar/pie charts
    "tech_server": 1181316,         # person with tablet in a server room
    "lifestyle_coffee": 4126724,    # coffee + laptop, casual creative work
    # --- home & cleaning services ---
    "cleaning_home": 6195198,       # woman cleaning a home -- house-cleaning / maid-service posts
    "cleaning_gloves": 4021256,     # blue-gloved hands wiping a surface, close up
    "cleaning_spray": 4440533,      # gloved hands with spray bottle
    "cleaning_supplies": 28576636,  # cleaning supplies + gloves, still life
    # "funny_confused": 3760607,    # DEAD 2026-08-04 -- images.pexels.com 500s on this id
    # specifically while sibling ids 200 over the same connection. Replacement candidate 4491471
    # is also dead. No verified confused/puzzled shot yet; www.pexels.com search pages aren't
    # reachable from here to browse for one, so find candidates via WebSearch + verify_photo().
}


def photo_url(photo_id):
    return f"https://images.pexels.com/photos/{photo_id}/pexels-photo-{photo_id}.jpeg?auto=compress&cs=tinysrgb&w=1080"


def verify_photo(photo_id):
    """True if images.pexels.com actually serves this id. Always check a NEW id before using it --
    dead ids return 500 and download_photo() will blow up mid-run."""
    req = urllib.request.Request(photo_url(photo_id), headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=30) as resp:
            return resp.status == 200
    except Exception:
        return False


def download_photo(key, out_path="/tmp/social_photo.jpg"):
    """`key` may be a PHOTO_BANK key or a raw Pexels photo id (int), so a topic-matched photo
    found mid-run can be used without editing the bank first."""
    photo_id = PHOTO_BANK[key] if key in PHOTO_BANK else int(key)
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
    # NOTE: do NOT escape '%' -- ffmpeg drawtext's default text-expansion chokes on a lone '%'
    # ("Stray % near ..." and the whole drawtext silently drops, no crash, just missing text).
    # Fixed by disabling expansion (expansion=none) on every drawtext call below instead.
    return t.replace("\\", "\\\\").replace("'", "’").replace(":", "\\:")


def _dt(fontfile, text, **opts):
    parts = [f"drawtext=fontfile={fontfile}:text='{safe_text(text)}':expansion=none"]
    for k, v in opts.items():
        parts.append(f"{k}={v}")
    return ":".join(parts)


def logo_draws(x, y, fontsize=46, color=WHITE):
    """The REAL diwizi lockup, matching the site header's inline SVG exactly:
    'diwizi' in Source Serif 4 Bold + a magenta '.' -- NOT a sans wordmark, and the dot is ALWAYS
    brand magenta regardless of the post's accent colour (it's a fixed brand mark, not an accent).
    `color` is the wordmark colour: CHARCOAL on light backgrounds, WHITE reversed on dark ones.
    ffmpeg can't colour part of one drawtext, so the dot is a second drawtext offset by the
    measured width of 'diwizi' (PIL measures the same TTF ffmpeg renders, so they line up).
    """
    from PIL import ImageFont
    f = ImageFont.truetype(SERIF_BOLD, fontsize)
    word_w = f.getlength("diwizi")
    # ffmpeg anchors each drawtext at the TOP OF ITS OWN INK BOX, and a lone '.' is a tiny box
    # sitting near the baseline -- so passing both the same y floats the dot up by the cap height
    # and it reads as a degree sign. Shift the dot down by the difference between the two ink-box
    # tops (same units, same font, so PIL's bboxes give the exact correction).
    top_word = f.getbbox("diwizi")[1]
    top_dot = f.getbbox(".")[1]
    return [
        _dt(SERIF_BOLD, "diwizi", fontcolor=color, fontsize=fontsize, x=int(x), y=int(y)),
        _dt(SERIF_BOLD, ".", fontcolor=BRAND_MAGENTA, fontsize=fontsize,
            x=int(x + round(word_w)), y=int(y + (top_dot - top_word))),
    ]


def logo_width(fontsize=46):
    from PIL import ImageFont
    f = ImageFont.truetype(SERIF_BOLD, fontsize)
    return f.getlength("diwizi.")


def build_image_card(out_path, photo_path, hook, points, cta, accent_name="magenta"):
    """Real photo on top ~55%, solid accent-color card on bottom with hook/points/cta.
    Use for blog-promo / tip / consulting-offer content."""
    W, H = 1080, 1350
    accent = ACCENTS[accent_name]
    CARD_Y = 760
    draws = [
        f"drawbox=x=0:y=0:w={W}:h=170:color=0x000000@0.32:t=fill",
        *logo_draws(70, 70, fontsize=46, color=WHITE),
        f"drawbox=x=0:y={CARD_Y}:w={W}:h={H-CARD_Y}:color={accent}:t=fill",
        _dt(SERIF_BOLD, hook, fontcolor=WHITE, fontsize=58, x=70, y=CARD_Y + 45, line_spacing=8),
    ]
    # Bullets start below however many lines the hook actually took -- a fixed offset let a 2-line
    # hook collide with the first bullet.
    hook_lines = hook.count("\n") + 1
    y0, gap = CARD_Y + 45 + hook_lines * 66 + 42, 62
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
        # Bar must clear BOTH caption lines AND the logo chip below them. A 2-line caption at
        # fontsize 34 is ~74px tall, so the old 190px bar put the chip on top of line 2.
        f"drawbox=x=0:y={H-270}:w={W}:h=270:color=0x000000@0.62:t=fill",
        _dt(SANS, bottom_text, fontcolor=WHITE, fontsize=34, x="(w-text_w)/2", y=H - 232, line_spacing=6),
        # Reversed logo (white wordmark + magenta dot) centred on the dark bar. The old white-box
        # chip in accent-coloured sans looked like a random badge, not the brand mark.
        *logo_draws((W - logo_width(38)) / 2, H - 122, fontsize=38, color=WHITE),
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
    """CTA CONVENTION (set by Diego 2026-08-04): do NOT use "link in bio" anywhere -- not in the
    caption, not in the on-image CTA, not in the first comment. Instead put the REAL destination
    URL in the first comment, and have the on-image CTA / caption point there ("Full guide in
    comments", "Link in comments"). Every post should carry a link relevant to ITS OWN topic:
      - Blog promo      -> https://diwizi.com/blog/<the-post-slug>.html
      - Tip             -> the closest related blog post, else the audit page
      - Consulting offer-> https://diwizi.com/ppc-audit.html
    Verify the URL returns 200 with a real browser User-Agent before publishing -- diwizi.com
    returns 406 to curl's default UA, so a bare `curl -I` will look like a dead link when it isn't.
    """
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
