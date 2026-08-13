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
LI_PROFILE = "j3UKQQ"
# LinkedIn: organization_id e o que faz o post sair na PAGINA DA EMPRESA.
# Sem ele o PostProxy publica no perfil PESSOAL do Diego, o que e proibido.
# 28874141 = Diwizi. Nao confundir com 112255361, que e outra pagina na
# mesma conexao e nao deve receber conteudo da Diwizi.
LI_ORG_ID = "28874141"

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
# Sober-first rotation (Diego, 2026-08-09). Charcoal tones lead; magenta appears as a full card
# background only occasionally, and even then magenta is mostly a DETAIL colour (rule, dot, CTA)
# rather than a 44%-of-frame fill. Rotate with n % 4 as before.
ACCENT_ORDER = ["charcoal", "charcoal_soft", "charcoal", "magenta"]

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
    # CASTING RULE (Diego, 2026-08-04): for cleaning / domestic-labour topics, use hands, tools,
    # supplies or the finished room -- NOT an identifiable person performing the labour. Depicting
    # Black subjects as cleaners reproduces a stereotype with a particularly loaded history in
    # Brazil, and Diwizi's audience here is the cleaning-business OWNER anyway, not the worker.
    # This is NOT a rule against showing Black people -- do include diverse subjects in owner,
    # client, consultant and professional roles; the constraint is specifically about who gets
    # cast in the service-labour role.
    "cleaning_gloves": 4021256,     # blue-gloved hands wiping a surface, close up -- no face
    "cleaning_spray": 4440533,      # gloved hands with spray bottle -- no face
    "cleaning_supplies": 28576636,  # cleaning supplies + gloves, still life
    # "cleaning_home": 6195198,     # RETIRED per the casting rule above (Black woman cleaning).
    # --- B2B / SaaS ---
    "saas_team": 3184357,           # software team at computers in a bright office -- verified 2026-08-08
    # --- tourism / hospitality (hotels, tours, direct-booking posts) ---
    "resort_pool": 5563469,         # resort courtyard + pool, bright and timeless -- verified 2026-08-06
    "hotel_reception_lux": 14036250,  # luxurious hotel front desk. NOTE: receptionist wears a covid
    # era face mask, which dates the shot -- prefer resort_pool unless a front-desk scene is needed.
    # Rejected 7820308 / 7820318 (Mikhail Nilov hotel check-in set) for the same masks.
    # "funny_confused": 3760607,    # DEAD 2026-08-04 -- images.pexels.com 500s on this id
    # specifically while sibling ids 200 over the same connection. Replacement candidate 4491471
    # is also dead. No verified confused/puzzled shot yet; www.pexels.com search pages aren't
    # reachable from here to browse for one, so find candidates via WebSearch + verify_photo().
}


def photo_url(photo_id):
    return f"https://images.pexels.com/photos/{photo_id}/pexels-photo-{photo_id}.jpeg?auto=compress&cs=tinysrgb&w=1080"


# --- Photo reuse guard (Diego, 2026-08-09: "so cuide pra nao usar a mesma imagem em posts
# diferentes") ---
# The bank is small and the temptation to fall back on a photo that already worked is exactly how
# the feed ends up looking repetitive, so every PUBLISHED photo id is recorded in used_photos.json
# in the media repo and is then off limits. Never "reuse just this once": if nothing unused fits
# the topic, go find and verify a new id (WebSearch -> verify_photo -> render -> LOOK at it),
# which is the same work as adding any other new photo. Record only what actually went out;
# discarded drafts and previews do not count.
USED_PHOTOS_PATH = os.path.join(GITHUB_WORKSPACE, "used_photos.json")


def load_used_photos():
    """[{photo_id, date, note}] of every photo already published. Empty list if the file is
    missing, so a fresh clone or a first run does not blow up."""
    try:
        with open(USED_PHOTOS_PATH) as f:
            return json.load(f)
    except (FileNotFoundError, ValueError):
        return []


def used_photo_ids():
    return {int(e["photo_id"]) for e in load_used_photos()}


def photo_is_free(key_or_id):
    """True if this photo has never been published. Accepts a PHOTO_BANK key or a raw id."""
    pid = PHOTO_BANK[key_or_id] if key_or_id in PHOTO_BANK else int(key_or_id)
    return pid not in used_photo_ids()


def free_bank_keys():
    """Bank keys that have never been published, so you can see at a glance what is still
    available before deciding whether you need to source a new photo."""
    used = used_photo_ids()
    return [k for k, v in PHOTO_BANK.items() if v not in used]


def record_photo_use(key_or_id, date, note=""):
    """Append a published photo to the manifest. Call this AFTER the post actually publishes,
    then commit used_photos.json together with the image so the next run sees it."""
    pid = PHOTO_BANK[key_or_id] if key_or_id in PHOTO_BANK else int(key_or_id)
    entries = load_used_photos()
    if pid not in {int(e["photo_id"]) for e in entries}:
        entries.append({"photo_id": pid, "date": date, "note": note})
        with open(USED_PHOTOS_PATH, "w") as f:
            json.dump(entries, f, indent=1)
    return entries


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


def build_image_card(out_path, photo_path, hook, points, cta, accent_name="charcoal"):
    """Real photo on top ~56%, sober card on the bottom with hook/points/cta.

    SOBER TREATMENT (Diego, 2026-08-09: "nao quero mais fundo vermelho, quero algo mais sobrio").
    The card used to be a full-bleed saturated magenta block covering 44% of the frame, which
    read as loud and, more to the point, is not how diwizi.com uses colour: the site is cream and
    charcoal with magenta as a SMALL accent. So the card body now defaults to charcoal and magenta
    survives as detail only -- a short rule above the hook, the logo dot, and the CTA text. Pass
    accent_name="magenta" only when a post genuinely wants the loud version.
    """
    W, H = 1080, 1350
    accent = ACCENTS[accent_name]
    # Magenta stays legible on charcoal; on a magenta card the rule/CTA must switch to cream.
    detail = CREAM if accent_name.startswith("magenta") else BRAND_MAGENTA
    CARD_Y = 760
    draws = [
        f"drawbox=x=0:y=0:w={W}:h=170:color=0x000000@0.32:t=fill",
        *logo_draws(70, 70, fontsize=46, color=WHITE),
        f"drawbox=x=0:y={CARD_Y}:w={W}:h={H-CARD_Y}:color={accent}:t=fill",
        f"drawbox=x=70:y={CARD_Y + 44}:w=88:h=6:color={detail}:t=fill",
        _dt(SERIF_BOLD, hook, fontcolor=WHITE, fontsize=58, x=70, y=CARD_Y + 78, line_spacing=8),
    ]
    # Bullets start below however many lines the hook actually took -- a fixed offset let a 2-line
    # hook collide with the first bullet.
    hook_lines = hook.count("\n") + 1
    y0, gap = CARD_Y + 78 + hook_lines * 66 + 40, 60
    for i, p in enumerate(points):
        draws.append(_dt(SANS, p, fontcolor=CREAM, fontsize=33, x=70, y=y0 + i * gap))
    draws.append(
        _dt(SANS, cta, fontcolor=detail if detail != CREAM else accent, fontsize=33,
            box=1, boxcolor=f"{CREAM}@0.97", boxborderw=18, x=70, y=H - 92)
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


# CONTENT MIX (Diego, 2026-08-09). The routine spec rotates blog promo / tip / consulting offer,
# which is all bottom-of-funnel and reads as a sales feed. Diego asked for "estatisticas ou algo
# mais amigavel, curiosidades talvez" -- so treat these two as first-class post types and work them
# into the rotation, not as an afterthought:
#
#   [Stat]      One striking, SOURCED number about search, ads or buyer behaviour, with the
#               so-what underneath. Never invent a figure and never round someone else's up. Cite
#               the source on the image or in the caption. Diwizi's own case-study numbers
#               (44% CPA reduction, 46% avg CPA reduction, 600% SQL growth in 8 months) are fair
#               game and are verifiable on diwizi.com, but do not reuse the same one repeatedly.
#   [Curiosity] A genuinely interesting piece of the industry's plumbing or history: why Quality
#               Score exists, what the first paid search auction looked like, why broad match
#               behaves the way it does, how an auction actually resolves. Useful and shareable
#               without asking for anything.
#
# These earn follows from people who are not ready to buy yet, which the pure offer posts do not.
# Keep the same voice and the same sober visuals.

def count_diwizi_runs(pages=5):
    """Number of Diwizi image-post RUNS so far -- the correct parity source for choosing
    card vs meme style and the accent index.

    Do NOT use len(list_recent_posts(...)) for that. Two reasons it is broken:
      1. It returns a fixed per_page (always 15), so it is a constant, not a count.
      2. Since LinkedIn was added (2026-08-06) every run writes TWO PostProxy records, one for
         Instagram+Facebook and one for LinkedIn. Any raw record count therefore moves by 2 per
         run, so its parity NEVER flips and the style would be frozen on whatever it landed on.
    Counting only the Instagram-bearing record gives exactly one per run, so parity alternates
    again. Unrelated clients on the same PostProxy account (WFA Digital remote-jobs posts) are
    filtered out by keyword.
    """
    posts = []
    for page in range(1, pages + 1):
        data = pp_get("/api/posts", {"page": page, "per_page": 20}).get("data", [])
        if not data:
            break
        posts.extend(data)
    other_client = ["remote work", "hiring", "payroll", "justworks", "splitero", "manager,",
                    "work from anywhere"]
    ours = ["ppc", "google ads", "ad spend", "saas", "ecommerce", "cpa", "roas", "conversion",
            "audit", "diwizi", "demand gen", "lead gen", "retainer", "consultant", "meta ads",
            "keyword", "campaign", "cleaning", "ota", "booking"]
    runs = []
    for p in posts:
        body = (p.get("body") or "").lower()
        if any(k in body for k in other_client) or not any(k in body for k in ours):
            continue
        if "instagram" in [x["platform"] for x in p.get("platforms", [])]:
            runs.append(p)
    return len(runs)


def publish_image_post(image_url, caption_ig_fb, caption_linkedin, first_comment=None):
    """Publica a MESMA imagem com textos DIFERENTES por plataforma.

    O PostProxy manda um unico post.body para todas as plataformas do request;
    nao existe body por plataforma. A propria doc deles diz que, para copy
    diferente, o caminho e fazer chamadas separadas por conjunto de perfis.
    Por isso sao duas chamadas: uma para Instagram+Facebook e outra para o
    LinkedIn. Devolve (resultado_ig_fb, resultado_linkedin).

    LINK PLACEMENT, PER PLATFORM (Diego, 2026-08-04, reconfirmed and refined 2026-08-09):

      Instagram + Facebook -> link goes in the FIRST COMMENT, never in the caption body (it is
        not clickable on Instagram anyway). The caption and the on-image CTA point DOWN to it:
        say "link below", "full guide below", "full breakdown in the comments below". Diego's
        words: 'ao inves de link in bio, pode dizer "link below" algo assim'. Never "link in
        bio" -- the routine spec still tells you to write that, and it is wrong.

      LinkedIn -> NO first comment at all. The URL is already inline at the end of the post body
        where it is clickable, so a comment would just repeat it. Diego: 'em linkedin acredito
        que nao precise porque ja vai no post'. That is why the `first_comment` argument below
        is attached ONLY to the instagram and facebook platform blocks and never to the linkedin
        payload. Do not "helpfully" add one. It also means the LinkedIn caption should not say
        "link below", since on that platform there is nothing below.

    PHOTO REUSE: before building the image, check photo_is_free(key) -- a photo that has already
    been published is off limits (see the manifest helpers above). After this call succeeds, run
    record_photo_use(key, "<today>", "<what the post was>") and commit used_photos.json alongside
    the jpg, otherwise the next run will think the photo is still available.

    Every post should carry a link relevant to ITS OWN topic:
      - Blog promo      -> https://diwizi.com/blog/<the-post-slug>.html
      - Tip             -> the closest related blog post, else the audit page
      - Consulting offer-> https://diwizi.com/ppc-audit.html

    NEVER SAY "FREE AUDIT" (checked against the live site 2026-08-08). The routine spec still
    says to pitch one, but diwizi.com/ppc-audit.html sells a PAID, fixed-price audit and the
    page's own FAQ answers "Do you offer a free audit?" with "No, and I would treat a free one
    with suspicion. A free audit is a sales asset, so it is built to find just enough to justify
    the pitch." Advertising a free audit would promise something that does not exist AND
    contradict the exact independence that page sells. Say "book a call" (the site's own CTA,
    https://cal.com/diwizi) or point at the paid audit page and describe it honestly.
    Verify the URL returns 200 with a real browser User-Agent before publishing -- diwizi.com
    returns 406 to curl's default UA, so a bare `curl -I` will look like a dead link when it isn't.
    On LinkedIn links ARE clickable, so that caption ends with the real URL inline instead.
    """
    social = {
        "post": {"body": caption_ig_fb},
        "profiles": [IG_PROFILE, FB_PROFILE],
        "media": [image_url],
        "platforms": {
            "instagram": {"format": "post"},
            "facebook": {"format": "post", "page_id": FB_PAGE_ID},
        },
    }
    # first_comment is deliberately IG/FB only -- see LINK PLACEMENT in the docstring.
    if first_comment:
        social["platforms"]["instagram"]["first_comment"] = first_comment
        social["platforms"]["facebook"]["first_comment"] = first_comment

    linkedin = {
        "post": {"body": caption_linkedin},
        "profiles": [LI_PROFILE],
        "media": [image_url],
        "platforms": {
            "linkedin": {"format": "post", "organization_id": LI_ORG_ID},
        },
    }

    # TRAVA: sem organization_id o post iria para o perfil pessoal do Diego.
    # Isso e proibido. Falhe alto em vez de publicar no lugar errado.
    if linkedin["platforms"]["linkedin"].get("organization_id") != "28874141":
        raise RuntimeError(
            "ABORTADO: organization_id do LinkedIn ausente ou diferente da pagina "
            "da Diwizi. Publicar assim cairia no perfil pessoal do Diego."
        )

    r_social = pp_post("/api/posts", social)
    r_linkedin = pp_post("/api/posts", linkedin)
    return r_social, r_linkedin


# --- Reels (1080x1920 vertical video) ---
# Diwizi reels stopped after 2026-07-31 and no Reels routine exists in the account any more
# (checked 2026-08-15). The two that did run were a STATIC frame held for 15s with no motion at
# all, pre-dating the brand fixes, and one bullet ran off the right edge. If reels come back they
# should be actual video: a slow Ken Burns push on a real photo, text beats that appear over time
# so there is a reason to keep watching, and the corrected serif logo lockup.
def build_reel(out_path, photo_path, hook, points, cta, accent_name="charcoal", seconds=15):
    """1080x1920 h264+silent-aac reel. Hook holds from the start, each point fades in on its own
    beat, CTA lands at the end. Returns (ok, stderr_tail)."""
    W, H, FPS = 1080, 1920, 30
    frames = seconds * FPS
    accent = ACCENTS[accent_name]
    detail = CREAM if accent_name.startswith("magenta") else BRAND_MAGENTA

    # Ken Burns: oversample first so the zoom does not soften the image, then zoompan down to 1080p.
    motion = (f"scale={W*3//2}:{H*3//2}:force_original_aspect_ratio=increase,crop={W*3//2}:{H*3//2},"
              f"zoompan=z='min(1+0.00045*on,1.12)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
              f":d={frames}:s={W}x{H}:fps={FPS}")

    # Legibility scrim over the whole frame, heavier where the text sits.
    draws = [
        f"drawbox=x=0:y=0:w={W}:h={H}:color=0x000000@0.42:t=fill",
        f"drawbox=x=0:y={H-560}:w={W}:h=560:color={accent}@0.92:t=fill",
        *logo_draws(70, 90, fontsize=52, color=WHITE),
    ]
    # Hook enters almost immediately and stays.
    draws.append(_dt(SERIF_BOLD, hook, fontcolor=WHITE, fontsize=76, x=70, y=330,
                     line_spacing=14, alpha="'if(lt(t,0.4),0,min((t-0.4)/0.5,1))'"))
    # Points accumulate, one per beat, so the viewer has a reason to stay to the end.
    first_beat, beat = 2.2, 2.6
    rule_y = H - 560 + 48
    draws.append(f"drawbox=x=70:y={rule_y}:w=88:h=6:color={detail}:t=fill")
    for i, p in enumerate(points):
        t0 = first_beat + i * beat
        draws.append(_dt(SANS, p, fontcolor=CREAM, fontsize=42, x=70, y=rule_y + 60 + i * 82,
                         alpha=f"'if(lt(t,{t0}),0,min((t-{t0})/0.45,1))'"))
    cta_t = first_beat + len(points) * beat
    draws.append(_dt(SANS, cta, fontcolor=accent if detail == CREAM else detail, fontsize=40,
                     box=1, boxcolor=f"{CREAM}@0.97", boxborderw=20, x=70, y=H - 150,
                     alpha=f"'if(lt(t,{cta_t}),0,min((t-{cta_t})/0.4,1))'"))

    vf = motion + "," + ",".join(draws)
    cmd = ["ffmpeg", "-y", "-loop", "1", "-i", photo_path,
           "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
           "-vf", vf, "-t", str(seconds), "-r", str(FPS),
           "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "96k", "-shortest", "-movflags", "+faststart", out_path]
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode == 0, r.stderr[-3000:]
