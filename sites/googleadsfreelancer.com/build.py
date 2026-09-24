#!/usr/bin/env python3
"""Static site generator for googleadsfreelancer.com.

Usage:  python3 build.py            -> writes ./dist
Pages content lives in pages_core.py and pages_services.py.
"""
import html
import json
import os
import re
import shutil
from datetime import date

from pages_core import PAGES as CORE
from pages_services import PAGES as SERVICES

SITE = "https://googleadsfreelancer.com"
NAME = "Diego Zietek"
BRAND = "Google Ads Freelancer"
CAL = "https://cal.com/diwizi"
MAIL = "hello@diwizi.com"
LINKEDIN = "https://www.linkedin.com/in/diegozietek/"
PARENT = "https://diwizi.com/"
TODAY = date.today().isoformat()

PAGES = CORE + SERVICES
BY_SLUG = {p["slug"]: p for p in PAGES}

NAV = [
    ("google-ads-management", "Management"),
    ("google-ads-consultant", "Consulting"),
    ("google-ads-audit", "Audit"),
    ("pricing", "Pricing"),
    ("results", "Results"),
    ("about", "About"),
]

FOOTER_GROUPS = [
    ("Google Ads", ["google-ads-management", "google-ads-consultant", "google-ads-audit",
                    "google-ads-setup", "conversion-tracking-setup", "ecommerce-ppc-management",
                    "small-business-ppc-management"]),
    ("Other platforms", ["ppc-management", "meta-ads-management", "microsoft-ads-management",
                         "linkedin-ads-management", "white-label-ppc"]),
    ("Working with me", ["freelance-ppc-consultant", "pricing", "results", "about", "contact"]),
]

CSS = r"""
:root{--bg:#ffffff;--fg:#151a21;--muted:#5b6672;--line:#e4e8ec;--soft:#f4f6f8;--accent:#1a56db;--accent-fg:#ffffff;--ok:#0f766e;--max:1040px}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#0f1318;--fg:#e8ecf0;--muted:#9aa5b1;--line:#252c35;--soft:#161c23;--accent:#5b8def;--accent-fg:#0b1220}}
:root[data-theme=dark]{--bg:#0f1318;--fg:#e8ecf0;--muted:#9aa5b1;--line:#252c35;--soft:#161c23;--accent:#5b8def;--accent-fg:#0b1220}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
a{color:var(--accent)}a:hover{text-decoration-thickness:2px}
.wrap{max-width:var(--max);margin:0 auto;padding:0 16px}
header.top{border-bottom:1px solid var(--line);position:sticky;top:0;background:var(--bg);z-index:5}
header.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:60px}
.logo{font-weight:700;text-decoration:none;color:var(--fg);letter-spacing:-.01em;white-space:nowrap}
.logo span{color:var(--accent)}
nav.main{display:flex;gap:18px;align-items:center;overflow-x:auto;scrollbar-width:none}nav.main::-webkit-scrollbar{display:none}
nav.main a{color:var(--fg);text-decoration:none;font-size:15px;white-space:nowrap;padding:6px 0;border-bottom:2px solid transparent}
nav.main a[aria-current]{border-color:var(--accent)}
.btn{display:inline-block;background:var(--accent);color:var(--accent-fg);text-decoration:none;font-weight:600;padding:12px 20px;border-radius:8px;white-space:nowrap}
.btn:hover{filter:brightness(1.08);text-decoration:none}
.btn.ghost{background:transparent;color:var(--fg);border:1px solid var(--line)}
.hero{padding:56px 0 32px}
.hero .kicker{color:var(--accent);font-weight:600;font-size:14px;letter-spacing:.06em;text-transform:uppercase;margin:0 0 10px}
h1{font-size:clamp(30px,4.6vw,46px);line-height:1.12;letter-spacing:-.02em;margin:0 0 16px;max-width:22ch}
.hero p.lead{font-size:20px;color:var(--muted);max-width:60ch;margin:0 0 26px}
.cta-row{display:flex;gap:12px;flex-wrap:wrap;align-items:center}
.proof{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:32px 0 8px}
.proof div{background:var(--soft);border:1px solid var(--line);border-radius:10px;padding:14px 16px}
.proof b{display:block;font-size:26px;letter-spacing:-.02em}
.proof small{color:var(--muted)}
main section{padding:34px 0;border-top:1px solid var(--line)}
main section:first-of-type{border-top:0}
h2{font-size:clamp(24px,3vw,32px);line-height:1.2;letter-spacing:-.015em;margin:0 0 14px;max-width:30ch}
h3{font-size:20px;margin:26px 0 8px}
p,li{max-width:70ch}
ul{padding-left:22px}
.cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px}
.card{background:var(--soft);border:1px solid var(--line);border-radius:12px;padding:20px}
.card h3{margin-top:0}
.steps{counter-reset:s;list-style:none;padding:0;display:grid;gap:14px}
.steps li{counter-increment:s;display:grid;grid-template-columns:40px 1fr;gap:12px;align-items:start}
.steps li::before{content:counter(s);width:32px;height:32px;border-radius:50%;background:var(--accent);color:var(--accent-fg);display:grid;place-items:center;font-weight:700}
table{border-collapse:collapse;width:100%;font-size:15.5px;margin:12px 0}
th,td{text-align:left;padding:10px 10px;border-bottom:1px solid var(--line);vertical-align:top}
th{color:var(--muted);font-weight:600;font-size:14px}
.note{border-left:3px solid var(--accent);padding:10px 16px;background:var(--soft);border-radius:0 10px 10px 0;color:var(--muted);font-size:15.5px}
details{border:1px solid var(--line);border-radius:10px;padding:0 16px;margin:10px 0;background:var(--bg)}
summary{cursor:pointer;font-weight:600;padding:14px 0;list-style:none}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";float:right;color:var(--muted)}
details[open] summary::after{content:"–"}
details p{margin-top:0}
.ctabox{background:var(--soft);border:1px solid var(--line);border-radius:14px;padding:28px;margin:40px 0 0}
.ctabox h2{margin-bottom:8px}
.related{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px}
.related a{display:block;padding:14px 16px;border:1px solid var(--line);border-radius:10px;text-decoration:none;color:var(--fg);background:var(--bg)}
.related a b{display:block;color:var(--accent)}
.related a small{color:var(--muted)}
footer{border-top:1px solid var(--line);margin-top:56px;padding:36px 0 40px;font-size:15px;color:var(--muted)}
footer .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:24px}
footer h4{margin:0 0 8px;color:var(--fg);font-size:14px;text-transform:uppercase;letter-spacing:.06em}
footer ul{list-style:none;padding:0;margin:0}footer li{margin:4px 0}
footer a{color:var(--muted)}
.fine{margin-top:26px;padding-top:18px;border-top:1px solid var(--line);font-size:13.5px}
.updated{color:var(--muted);font-size:14px}
@media (max-width:640px){.hero{padding:36px 0 24px}.hero p.lead{font-size:18px}main section{padding:28px 0}.ctabox{padding:22px}}
"""


def esc(s):
    return html.escape(s, quote=True)


def url_for(slug):
    return "/" if slug == "index" else f"/{slug}/"


def out_path(slug):
    return "index.html" if slug == "index" else f"{slug}/index.html"


def nav_html(active):
    items = []
    for slug, label in NAV:
        cur = ' aria-current="page"' if slug == active else ""
        items.append(f'<a href="{url_for(slug)}"{cur}>{label}</a>')
    return "\n".join(items)


def footer_html():
    groups = []
    for title, slugs in FOOTER_GROUPS:
        lis = "".join(f'<li><a href="{url_for(s)}">{esc(BY_SLUG[s]["short"])}</a></li>' for s in slugs)
        groups.append(f"<div><h4>{title}</h4><ul>{lis}</ul></div>")
    groups.append(
        f'<div><h4>Contact</h4><ul><li><a href="{CAL}" rel="noopener">Book a call</a></li>'
        f'<li><a href="mailto:{MAIL}">{MAIL}</a></li>'
        f'<li><a href="{LINKEDIN}" rel="noopener">LinkedIn</a></li>'
        f'<li><a href="{PARENT}" rel="noopener">Diwizi (industry pages)</a></li></ul></div>'
    )
    return (
        '<footer><div class="wrap"><div class="grid">' + "".join(groups) + "</div>"
        f'<div class="fine">{BRAND} is the personal practice of {NAME}, independent paid media consultant '
        f'operating as Diwizi. Remote, in English, for clients in the United States, Canada, the United Kingdom '
        f'and Ireland. Google Ads, Meta Ads, LinkedIn Ads and Microsoft Advertising are trademarks of their '
        f'respective owners; this site is not affiliated with or endorsed by Google, Meta, Microsoft or LinkedIn. '
        f'&copy; {date.today().year} {NAME}. <a href="/privacy/">Privacy</a></div></div></footer>'
    )


def faq_html(faq):
    if not faq:
        return ""
    items = "".join(f"<details><summary>{esc(q)}</summary><p>{a}</p></details>" for q, a in faq)
    return f'<section id="faq"><div class="wrap"><h2>Questions people ask before hiring</h2>{items}</div></section>'


def related_html(slug):
    rel = BY_SLUG[slug].get("related", [])
    if not rel:
        return ""
    cards = "".join(
        f'<a href="{url_for(s)}"><b>{esc(BY_SLUG[s]["short"])}</b><small>{esc(BY_SLUG[s]["blurb"])}</small></a>'
        for s in rel
    )
    return f'<section><div class="wrap"><h2>Related services</h2><div class="related">{cards}</div></div></section>'


def cta_html(p):
    return (
        '<div class="wrap"><div class="ctabox"><h2>' + esc(p.get("cta_title", "Talk to the person who would run the account")) +
        "</h2><p>" + p.get("cta_text", "A 20-minute call. You describe the account and what is not working; I tell you "
        "whether I can help, what I would do first, and what it costs. No proposal deck, no sales follow-up sequence.") +
        f'</p><div class="cta-row"><a class="btn" href="{CAL}" rel="noopener">Book a call</a>'
        f'<a class="btn ghost" href="mailto:{MAIL}">Email {MAIL}</a></div></div></div>'
    )


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def schema_for(p):
    url = SITE + url_for(p["slug"])
    person = {
        "@type": "Person", "@id": SITE + "/about/#person", "name": NAME,
        "jobTitle": "Independent paid media consultant", "url": SITE + "/about/",
        "sameAs": [LINKEDIN, PARENT, PARENT + "diego-zietek.html"],
        "worksFor": {"@type": "Organization", "name": "Diwizi", "url": PARENT},
        "knowsAbout": ["Google Ads", "Meta Ads", "LinkedIn Ads", "Microsoft Advertising", "Conversion tracking", "GA4"],
    }
    service = {
        "@type": "ProfessionalService", "@id": SITE + "/#service", "name": BRAND + " — " + NAME,
        "url": SITE + "/", "founder": {"@id": SITE + "/about/#person"}, "email": MAIL,
        "areaServed": [{"@type": "Country", "name": c} for c in ["United States", "Canada", "United Kingdom", "Ireland"]],
        "priceRange": "$$", "serviceType": "Google Ads management and consulting",
    }
    graph = [person, service, {
        "@type": "WebPage", "@id": url, "url": url, "name": p["title"], "description": p["meta"],
        "dateModified": TODAY, "isPartOf": {"@type": "WebSite", "url": SITE + "/", "name": BRAND},
        "about": {"@id": SITE + "/#service"},
    }]
    if p.get("faq"):
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
            for q, a in p["faq"]]})
    if p.get("service_name"):
        graph.append({"@type": "Service", "name": p["service_name"], "serviceType": p["service_name"],
                      "provider": {"@id": SITE + "/#service"}, "url": url,
                      "areaServed": ["US", "CA", "GB", "IE"]})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)


def render(p):
    slug = p["slug"]
    url = SITE + url_for(slug)
    proof = p.get("proof", [("14+", "years running paid media"), ("1", "person on your account"),
                            ("44%", "lower CPA, published case"), ("0", "long-term contracts")])
    proof_html = "".join(f"<div><b>{esc(b)}</b><small>{esc(s)}</small></div>" for b, s in proof)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(p['title'])}</title>
<meta name="description" content="{esc(p['meta'])}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:title" content="{esc(p['title'])}">
<meta property="og:description" content="{esc(p['meta'])}"><meta property="og:url" content="{url}">
<meta property="og:site_name" content="{BRAND}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="sitemap" type="application/xml" href="/sitemap.xml">
<style>{CSS}</style>
<script type="application/ld+json">{schema_for(p)}</script>
</head>
<body>
<header class="top"><div class="wrap">
<a class="logo" href="/">google<span>ads</span>freelancer</a>
<nav class="main" aria-label="Main">{nav_html(slug)}</nav>
<a class="btn" href="{CAL}" rel="noopener">Book a call</a>
</div></header>
<main>
<section class="hero"><div class="wrap">
<p class="kicker">{esc(p.get('kicker', BRAND))}</p>
<h1>{p['h1']}</h1>
<p class="lead">{p['lead']}</p>
<div class="cta-row"><a class="btn" href="{CAL}" rel="noopener">Book a 20-minute call</a><a class="btn ghost" href="#faq">Read the FAQ</a></div>
<div class="proof">{proof_html}</div>
<p class="updated">Written by <a href="/about/">{NAME}</a>. Last updated {TODAY}.</p>
</div></section>
{p['body']}
{faq_html(p.get('faq'))}
{related_html(slug)}
{cta_html(p)}
</main>
{footer_html()}
</body>
</html>
"""


def privacy_page():
    body = f"""<section><div class="wrap">
<h2>What this site collects</h2>
<p>This site is a set of static pages. It sets no cookies of its own. If analytics or advertising tags are added, they are listed here with the vendor and purpose.</p>
<ul><li><b>Booking.</b> Calls are scheduled through Cal.com. Data you enter there is handled under <a href="https://cal.com/privacy" rel="noopener">Cal.com's privacy policy</a>.</li>
<li><b>Email.</b> Messages to {MAIL} go to {NAME} directly and are kept for the purpose of replying and, if you become a client, running the engagement.</li>
<li><b>Hosting.</b> Pages are served by Cloudflare, which processes IP addresses and request logs to deliver the site and protect it from abuse.</li></ul>
<h2>Your rights</h2>
<p>You can ask what personal data I hold about you, ask for it to be corrected or deleted, or object to its use, by emailing {MAIL}. Requests are answered by the same person who received your original message.</p>
<h2>Controller</h2>
<p>{NAME}, operating as Diwizi, Curitiba, Brazil. Contact: {MAIL}.</p>
</div></section>"""
    return {"slug": "privacy", "short": "Privacy", "blurb": "", "title": "Privacy policy | Google Ads Freelancer",
            "meta": "What googleadsfreelancer.com collects, why, and how to reach the person responsible for it.",
            "h1": "Privacy policy", "lead": "Short, because there is little to say: static pages, a booking link and an email address.",
            "body": body, "kicker": "Legal", "proof": [], "noindex": False}


def build():
    dist = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")
    if os.path.isdir(dist):
        shutil.rmtree(dist)
    os.makedirs(dist)
    all_pages = PAGES + [privacy_page()]
    urls = []
    for p in all_pages:
        path = os.path.join(dist, out_path(p["slug"]))
        os.makedirs(os.path.dirname(path) or dist, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(render(p))
        urls.append((SITE + url_for(p["slug"]), "1.0" if p["slug"] == "index" else ("0.5" if p["slug"] == "privacy" else "0.8")))
    with open(os.path.join(dist, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for u, pr in urls:
            f.write(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>\n")
        f.write("</urlset>\n")
    with open(os.path.join(dist, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    with open(os.path.join(dist, "favicon.svg"), "w") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#1a56db"/>'
                '<text x="32" y="43" font-family="Arial,Helvetica,sans-serif" font-size="30" font-weight="700" fill="#fff" text-anchor="middle">GA</text></svg>')
    with open(os.path.join(dist, "_headers"), "w") as f:
        f.write("/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n"
                "  X-Frame-Options: SAMEORIGIN\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n"
                "/favicon.svg\n  Cache-Control: public, max-age=604800\n")
    with open(os.path.join(dist, "_redirects"), "w") as f:
        f.write(f"https://www.googleadsfreelancer.com/* {SITE}/:splat 301\n")
    with open(os.path.join(dist, "404.html"), "w", encoding="utf-8") as f:
        f.write(render({"slug": "404", "title": "Page not found | " + BRAND, "meta": "That page does not exist.",
                        "h1": "That page is not here", "lead": "The address may have changed. Everything on this site is one click from the footer.",
                        "body": "", "kicker": "404", "proof": []}).replace('<link rel="canonical" href="' + SITE + '/404/">', '<meta name="robots" content="noindex">'))
    # report
    words = {}
    for p in all_pages:
        words[p["slug"]] = len(strip_tags(p["body"] + " ".join(a for _, a in p.get("faq", []))).split())
    return dist, words


if __name__ == "__main__":
    dist, words = build()
    print(f"built {len(words)} pages -> {dist}")
    for k, v in sorted(words.items(), key=lambda x: -x[1]):
        print(f"  {v:5d} words  /{k}")
