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
SISTER = "https://ppcconsultancy.uk"  # UK site; hreflang pairs below (US page -> UK page)
SISTER_PAGES = {
    "index": "/", "ppc-management": "/ppc-management/", "google-ads-management": "/google-ads-management/",
    "google-ads-audit": "/ppc-audit/", "linkedin-ads-management": "/b2b-ppc/",
    "conversion-tracking-setup": "/conversion-tracking/", "pricing": "/pricing/", "results": "/results/",
    "about": "/about/", "contact": "/contact/", "privacy": "/privacy/",
}


def hreflang_html(slug):
    other = SISTER_PAGES.get(slug)
    if not other:
        return ""
    here = SITE + url_for(slug)
    return (f'<link rel="alternate" hreflang="en-US" href="{here}">'
            f'<link rel="alternate" hreflang="en-GB" href="{SISTER}{other}">'
            f'<link rel="alternate" hreflang="x-default" href="{here}">')
NAME = "Diego Zietek"
BRAND = "Google Ads Freelancer"
CAL_EVENT_SLUG = "google-ads-call"  # create this event type on Cal.com under the diwizi account
CAL = f"https://cal.com/diwizi/{CAL_EVENT_SLUG}"  # kept for reference; no longer linked from the site
FORM_URL = "/contact/#form"  # every CTA points at the lead form
# Web3Forms access key (account: the hello@ inbox below). Public by design: it only allows sending to that inbox.
WEB3FORMS_KEY = "a8247bcb-2a34-4f73-a97e-877bfef2b8cb"
FORM_ENDPOINT = "https://api.web3forms.com/submit"
BUDGET_BANDS = [("under_3k", "Under $3K / month"), ("3k_20k", "$3K – $20K"), ("20k_50k", "$20K – $50K"), ("50k_plus", "$50K+")]
MAIL = "hello@diwizi.com"
MAIL_USER, MAIL_DOMAIN = MAIL.split("@")
BRAND_SPRITE = "marcas-en-v3.webp"  # 6410x104 transparent sprite, 20 logos, trailing gap for a seamless loop
PARENT = "https://diwizi.com/"
TODAY = date.today().isoformat()

PRICES = {  # edit here; every page reads from this dict
    "audit_usd": 1800, "audit_gbp": 1400,
    "retainer_usd": 2000, "retainer_gbp": 1600,
    "retainer_mid_usd": 3000, "retainer_mid_gbp": 2400,
    "retainer_top_usd": 4500, "retainer_top_gbp": 3600,
    "consulting_hour_usd": 250, "consulting_hour_gbp": 200,
    "setup_usd": 1800, "setup_gbp": 1400,
    "tracking_usd": 1500, "tracking_gbp": 1200,
    "whitelabel_usd": 1200, "whitelabel_gbp": 950,
}
PHOTO = os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "diego.jpg"))

PROOF_DEFAULT = [("14+", "years in paid media"), ("1", "person on your account"), ("Flat fee", "never a % of ad spend"), ("Yours", "accounts, tags and pages stay with you")]
PROOF_GOOGLE = [("14+", "years in paid media"), ("44%", "lower CPA, Google Ads client case"), ("60%", "more qualified leads, same case"), ("Flat fee", "never a % of ad spend")]
PROOF_BY_SLUG = {
    "index": PROOF_GOOGLE, "google-ads-management": PROOF_GOOGLE, "freelance-ppc-consultant": PROOF_GOOGLE,
    "small-business-ppc-management": PROOF_GOOGLE, "results": None, "google-ads-consultant": [("14+", "years in paid media"), ("Read-only", "access is all a review needs"), ("Written", "findings, ranked by impact"), ("Hourly or fixed", "never a % of ad spend")],
    "ppc-management": [("4", "platforms, one operator"), ("1", "measurement layer across all"), ("1", "report, in your currency"), ("Flat fee", "never a % of ad spend")],
    "meta-ads-management": [("Pixel + CAPI", "deduplicated events"), ("CRM", "lead quality, not form fills"), ("Scheduled", "creative tests, one control"), ("Flat fee", "never a % of ad spend")],
    "microsoft-ads-management": [("20–40%", "lower CPC vs Google, typical"), ("Native", "negatives, bids and schedules"), ("UET", "via Tag Manager, same definitions"), ("Small", "add-on to a Google retainer")],
    "linkedin-ads-management": [("Named", "account lists and titles"), ("CRM", "stages fed back to LinkedIn"), ("Pipeline", "is the number reported"), ("Flat fee", "never a % of ad spend")],
    "ecommerce-ppc-management": [("Margin", "not platform ROAS"), ("Feed first", "titles, GTINs, labels"), ("PMax", "with brand excluded"), ("New vs returning", "customers separated")],
}
GTM_ID = "GTM-TB2NHZCH"
GTM_HEAD = ("<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});"
            "var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;"
            "j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);"
            "})(window,document,'script','dataLayer','" + GTM_ID + "');</script>")
GTM_BODY = ('<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=' + GTM_ID +
            '" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>')
# Cal.com appends email, attendeeName, phone, guestEmails (and can glue on a 2nd "?") to the
# redirect URL. Runs before GTM: keep the uid in window.__tyUid, then clear the bar to the
# bare path so nothing PII-shaped sits in the URL, browser history or referrer headers.
TY_LIMPA_JS = ("<script id=\"ty-limpa\">"
    "(function(){try{"
    "var q=new URLSearchParams(location.search.replace(/^\\?/,'').replace(/\\?/g,'&'));"
    "window.__tyUid=q.get('uid')||q.get('bookingUid')||q.get('bookingId')||'';"
    "var n=location.pathname+location.hash;"
    "if(n!==location.pathname+location.search+location.hash)history.replaceState(null,'',n);"
    "}catch(e){}})();"
    "</script>")
# Pushes clean dataLayer events for GTM: book_call_click, email_click (with link_url, cta_location).
CLICK_JS = ("<script>document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a');if(!a)return;"
            "var h=a.getAttribute('href')||'',ev=null;if(h.indexOf('cal.com')>-1)ev='book_call_click';else if(h.indexOf('#form')>-1)ev='quote_click';else if(h.indexOf('mailto:')===0)ev='email_click';"
            "if(!ev)return;var sec=a.closest('header')?'header':a.closest('footer')?'footer':a.closest('.mmenu')?'mobile_menu':"
            "(a.closest('.hero')?'hero':(a.closest('.ctabox')?'bottom_cta':'body'));"
            "window.dataLayer=window.dataLayer||[];window.dataLayer.push({event:ev,link_url:a.href,cta_location:sec});},true);</script>")
# The address is never written out in the HTML: links carry user and domain in data attributes and
# this script assembles them. Without JS the visitor sees "hello [at] diwizi.com".
EMAIL_JS = ("<script>(function(){var l=document.querySelectorAll('a.em');for(var i=0;i<l.length;i++){var a=l[i],"
            "m=a.getAttribute('data-u')+'@'+a.getAttribute('data-d');a.href='mailto:'+m;"
            "a.textContent=(a.getAttribute('data-pre')||'')+m;}})();</script>")
# Lead form: posts to Web3Forms via fetch. On success pushes generate_lead (budget_band, cta_location) and goes to
# /thanks/?src=form once GTM has handled the event (or after 1.5 s if GTM is blocked). No mailto fallback.
FORM_JS = ("<script>(function(){var f=document.getElementById('form');if(!f)return;"
           "var st=f.querySelector('.form-status'),btn=f.querySelector('button'),w=f.querySelector('input[name=website]');"
           "function band(){var r=f.querySelector('input[name=budget]:checked');return r?r.value:''}"
           "if(w)w.addEventListener('input',function(){var v=w.value.replace(/^\\s*https?:\\/\\//i,'');if(v!==w.value)w.value=v;});"
           "function fail(){btn.disabled=false;var m='" + MAIL_USER + "'+'@'+'" + MAIL_DOMAIN + "';"
           "st.innerHTML='Could not send just now. Please try again in a moment, or write to <a href=\"mailto:'+m+'\">'+m+'</a>.';}"
           "f.addEventListener('submit',function(e){e.preventDefault();"
           "if(!f.checkValidity()){f.reportValidity();return}"
           "if(f.botcheck.checked)return;"
           "var fd=new FormData(f);var v=(w&&w.value||'').trim().replace(/^https?:\\/\\//i,'');fd.set('website',v?'https://'+v:'');"
           "btn.disabled=true;st.textContent='Sending\\u2026';"
           "fetch(f.action,{method:'POST',body:fd,headers:{'Accept':'application/json'}}).then(function(r){return r.json()}).then(function(j){"
           "if(!(j&&j.success))throw new Error((j&&j.message)||'error');"
           "var done=false;function go(){if(done)return;done=true;location.href='/thanks/?src=form'}"
           "window.dataLayer=window.dataLayer||[];"
           "window.dataLayer.push({event:'generate_lead',budget_band:band(),cta_location:location.pathname,eventCallback:go,eventTimeout:1500});"
           "setTimeout(go,1500);"
           "}).catch(fail);"
           "});})();</script>")
PAGES = CORE + SERVICES
BY_SLUG = {p["slug"]: p for p in PAGES}

NAV = [
    ("google-ads-management", "Management"),
    ("ppc-management", "Platforms"),
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
form.lead{margin-top:18px;display:grid;gap:14px}form.lead fieldset{border:0;padding:0;margin:0}form.lead legend{font-weight:600;margin-bottom:8px}
.pills{display:flex;gap:8px;flex-wrap:wrap}.pill input{position:absolute;opacity:0;pointer-events:none}.pill span{display:inline-block;padding:9px 14px;border:1px solid var(--line);border-radius:999px;background:var(--bg);cursor:pointer;font-size:15px}
.pill input:checked+span{background:var(--accent);color:var(--accent-fg);border-color:var(--accent)}.pill input:focus-visible+span{outline:2px solid var(--accent);outline-offset:2px}
form.lead label{display:flex;flex-direction:column;gap:6px;font-weight:600;font-size:15px}form.lead label small{font-weight:400;color:var(--muted)}
form.lead input[type=text],form.lead input[type=email],form.lead input[type=url],form.lead input[type=tel],form.lead textarea{font:inherit;font-weight:400;padding:11px 12px;border:1px solid var(--line);border-radius:8px;background:var(--bg);color:var(--fg);width:100%}
form.lead textarea{resize:vertical}.row2{display:grid;grid-template-columns:1fr 1fr;gap:12px}@media (max-width:640px){.row2{grid-template-columns:1fr}}
.pfx{display:flex;align-items:center;border:1px solid var(--line);border-radius:8px;background:var(--bg)}.pfx:focus-within{outline:2px solid var(--accent);outline-offset:1px}
.pfx>span{padding-left:12px;color:var(--muted);font-weight:400;user-select:none}form.lead .pfx input{border:0;background:transparent;padding-left:1px;outline:none;min-width:0}
.brands .eyebrow{color:var(--accent);font-weight:600;font-size:14px;letter-spacing:.06em;text-transform:uppercase;margin:0 0 6px}
.brand-strip{overflow:hidden;margin:22px 0;-webkit-mask-image:linear-gradient(90deg,transparent,#000 7%,#000 93%,transparent);mask-image:linear-gradient(90deg,transparent,#000 7%,#000 93%,transparent)}
.brand-track{display:flex;width:max-content;animation:brandscroll 90s linear infinite}.brand-strip:hover .brand-track{animation-play-state:paused}
.brand-track img{display:block;flex:none;height:52px;width:auto;max-width:none;opacity:.8}
@keyframes brandscroll{from{transform:translateX(0)}to{transform:translateX(-50%)}}
@media (max-width:640px){.brand-track img{height:38px}}@media (prefers-reduced-motion:reduce){.brand-track{animation:none}}
.tags{display:flex;flex-wrap:wrap;gap:8px;list-style:none;padding:0;margin:14px 0}.tags li{border:1px solid var(--line);border-radius:999px;padding:5px 12px;font-size:14px;color:var(--muted);background:var(--bg)}
.fineprint{font-size:13px;color:var(--muted);margin:6px 0 0}
.hp{position:absolute;left:-9999px;opacity:0}.form-note{color:var(--muted);font-size:14px}.form-status{margin:0;font-size:14px;color:var(--muted)}form.lead .btn{border:0;cursor:pointer;font:inherit;font-weight:600}
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
.mmenu{display:none;position:relative}
.mmenu summary{list-style:none;cursor:pointer;font-weight:600;padding:8px 12px;border:1px solid var(--line);border-radius:8px}
.mmenu summary::-webkit-details-marker{display:none}.mmenu summary::after{content:none}
.mmenu-panel{position:absolute;right:0;top:44px;width:min(92vw,360px);background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:16px;box-shadow:0 12px 30px rgba(0,0,0,.12);z-index:10;display:grid;gap:12px}
.mmenu-panel h4{margin:0 0 4px;font-size:12px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
.mmenu-panel ul{list-style:none;padding:0;margin:0}.mmenu-panel li{margin:2px 0}.mmenu-panel a{text-decoration:none;color:var(--fg)}
.hero-grid{display:grid;grid-template-columns:1.4fr 1fr;gap:28px;align-items:center}
.hero-grid img{width:100%;max-width:340px;border-radius:16px;justify-self:end;aspect-ratio:4/5;object-fit:cover}
.hero-grid:not(:has(img)){grid-template-columns:1fr}.hero-grid:not(:has(img))>div{max-width:860px}
.byline{color:var(--muted);font-size:13.5px;margin:28px 0 0}
.price{font-size:15px;color:var(--muted)}.price b{color:var(--fg);font-size:18px}
@media (max-width:720px){nav.main,.top-cta{display:none}.mmenu{display:block}header.top .wrap{min-height:56px}.logo{font-size:15px}.hero-grid{grid-template-columns:1fr}.hero-grid img{justify-self:start;max-width:220px}}
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


def mobile_menu_html():
    groups = []
    for title, slugs in FOOTER_GROUPS:
        lis = "".join(f'<li><a href="{url_for(s)}">{esc(BY_SLUG[s]["short"])}</a></li>' for s in slugs)
        groups.append(f"<div><h4>{title}</h4><ul>{lis}</ul></div>")
    return ('<details class="mmenu"><summary aria-label="Menu">Menu</summary><div class="mmenu-panel">'
            + "".join(groups) + f'<p><a class="btn" href="{FORM_URL}">Get a quote</a></p></div></details>')


def email_link(pre="", cls=""):
    klass = "em" + (" " + cls if cls else "")
    extra = f' data-pre="{pre}"' if pre else ""
    return f'<a class="{klass}" data-u="{MAIL_USER}" data-d="{MAIL_DOMAIN}"{extra}>{pre}{MAIL_USER} [at] {MAIL_DOMAIN}</a>'


BRANDS_ALT = ("Brands Diego Zietek has worked on: Shell, Timberland, Intuit QuickBooks, Mission AC &amp; Plumbing, Amazon Prime, "
              "Skillshare, Regus, TIM, Pontomais, Bluecore, TradingWorks, Underscore Marketing, PUCPR, Grupo Marista, "
              "Clinipam (Grupo NotreDame Intermédica), Forza JMalucelli, PneusAqui, Joias VIP, Éclairé and Trutek")
BRAND_TAGS = ["SaaS &amp; subscription", "Consumer brands", "Home services", "Telecom", "Education",
              "Healthcare &amp; pharma", "E-commerce", "B2B &amp; industrial"]


def brands_html():
    img = f'src="/{BRAND_SPRITE}" width="3205" height="52" loading="lazy" decoding="async"'
    tags = "".join(f"<li>{t}</li>" for t in BRAND_TAGS)
    return f"""<section class="brands" id="brands"><div class="wrap">
<p class="eyebrow">Experience</p>
<h2>Brands I've worked on</h2>
<p>Fourteen-plus years across agency, in-house and freelance roles put me on accounts with very different economics: SaaS and subscription products such as Intuit QuickBooks, Skillshare and Pontomais, global consumer brands such as Shell, Timberland and Amazon Prime, home services companies such as an HVAC and plumbing business in Houston, and companies in telecom, education, healthcare and e-commerce. Through Underscore Marketing, a US agency, I also worked on oncology, rare disease and gene therapy brands.</p>
<div class="brand-strip"><div class="brand-track"><img {img} alt="{BRANDS_ALT}"><img {img} alt="" aria-hidden="true"></div></div>
<p>What carries over to your account is pattern recognition: how a trial-to-paid funnel differs from a lead form, which conversions each business can actually measure, and where spend usually leaks.</p>
<ul class="tags">{tags}</ul>
<p class="fineprint">Logos belong to their owners and identify past work, not endorsements.</p>
</div></section>"""


def footer_html():
    groups = []
    for title, slugs in FOOTER_GROUPS:
        lis = "".join(f'<li><a href="{url_for(s)}">{esc(BY_SLUG[s]["short"])}</a></li>' for s in slugs)
        groups.append(f"<div><h4>{title}</h4><ul>{lis}</ul></div>")
    groups.append(
        f'<div><h4>Contact</h4><ul><li><a href="{FORM_URL}">Get a quote</a></li>'
        f'<li>{email_link()}</li>'
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
    rel = BY_SLUG.get(slug, {}).get("related", [])
    if not rel:
        return ""
    cards = "".join(
        f'<a href="{url_for(s)}"><b>{esc(BY_SLUG[s]["short"])}</b><small>{esc(BY_SLUG[s]["blurb"])}</small></a>'
        for s in rel
    )
    return f'<section><div class="wrap"><h2>Related services</h2><div class="related">{cards}</div></div></section>'


def form_html(slug):
    bands = "".join(
        f'<label class="pill"><input type="radio" name="budget" value="{v}" required><span>{esc(t)}</span></label>'
        for v, t in BUDGET_BANDS
    )
    return f"""<form id="form" class="lead" method="post" action="{FORM_ENDPOINT}" novalidate>
<input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
<input type="hidden" name="subject" value="New enquiry from {BRAND}">
<input type="hidden" name="from_name" value="{BRAND}">
<input type="hidden" name="page" value="{SITE}{url_for(slug)}">
<input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
<fieldset><legend>Monthly ad spend, roughly</legend><div class="pills">{bands}</div></fieldset>
<div class="row2">
<label>Name<input type="text" name="name" autocomplete="name" required></label>
<label>Work email<input type="email" name="email" autocomplete="email" required></label>
</div>
<div class="row2">
<label>Website<span class="pfx"><span aria-hidden="true">https://</span><input type="text" name="website" inputmode="url" autocomplete="url" autocapitalize="off" spellcheck="false" placeholder="yourcompany.com"></span></label>
<label><span>Phone <small>(optional)</small></span><input type="tel" name="phone" autocomplete="tel"></label>
</div>
<label>What is not working, or what you need<textarea name="message" rows="3" placeholder="Platforms, who runs the account today, and what prompted the search."></textarea></label>
<div class="cta-row"><button class="btn" type="submit">Send</button><span class="form-note">One reply, from me, usually within a working day. No sequence.</span></div>
<p class="form-status" role="status" aria-live="polite"></p>
</form>"""


def cta_html(p):
    slug = p["slug"]
    return (
        '<div class="wrap"><div class="ctabox"><h2>' + esc(p.get("cta_title", "Tell me about the account")) +
        "</h2><p>" + p.get("cta_text", "Spend band, site and what is not working. You get a straight answer on whether I can help, "
        "what I would do first and a price range. No proposal deck, no sales follow-up sequence.") +
        "</p>" + (f'<div class="cta-row">{email_link("Email ", "btn ghost")}</div>' if p.get("no_form") else form_html(slug)) + "</div></div>"
    )


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def schema_for(p):
    url = SITE + url_for(p["slug"])
    person = {
        "@type": "Person", "@id": SITE + "/about/#person", "name": NAME,
        "jobTitle": "Independent paid media consultant", "url": SITE + "/about/",
        "sameAs": [PARENT, PARENT + "diego-zietek.html"],
        "worksFor": {"@type": "Organization", "name": "Diwizi", "url": PARENT},
        "knowsAbout": ["Google Ads", "Meta Ads", "LinkedIn Ads", "Microsoft Advertising", "Conversion tracking", "GA4"],
    }
    service = {
        "@type": "ProfessionalService", "@id": SITE + "/#service", "name": BRAND + " — " + NAME,
        "url": SITE + "/", "founder": {"@id": SITE + "/about/#person"},
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


def fill_prices(html_text):
    for k, v in PRICES.items():
        html_text = html_text.replace("{{" + k + "}}", f"{v:,}")
    html_text = html_text.replace("{{cal_url}}", CAL)
    html_text = html_text.replace("{{email}}", email_link())
    html_text = html_text.replace("{{brands}}", brands_html())
    return html_text


def render(p):
    p = dict(p)
    p["body"] = fill_prices(p.get("body", ""))
    p["lead"] = fill_prices(p.get("lead", ""))
    if p.get("faq"):
        p["faq"] = [(q, fill_prices(a)) for q, a in p["faq"]]
    if p.get("proof"):
        p["proof"] = [(fill_prices(b), fill_prices(t)) for b, t in p["proof"]]
    slug = p["slug"]
    url = SITE + url_for(slug)
    proof = p.get("proof")
    if proof is None and slug in PROOF_BY_SLUG:
        proof = PROOF_BY_SLUG[slug]
    if proof is None:
        proof = PROOF_DEFAULT if slug not in ("results", "contact", "privacy", "404") else []
    proof_html = "".join(f"<div><b>{esc(b)}</b><small>{esc(s)}</small></div>" for b, s in proof)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
{p.get('pre_gtm_head', '')}
{GTM_HEAD}
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(p['title'])}</title>
<meta name="description" content="{esc(p['meta'])}">
<link rel="canonical" href="{url}">
{hreflang_html(slug)}
<meta property="og:type" content="website"><meta property="og:title" content="{esc(p['title'])}">
<meta property="og:description" content="{esc(p['meta'])}"><meta property="og:url" content="{url}">
<meta property="og:site_name" content="{BRAND}">
<meta name="robots" content="{'noindex,follow' if p.get('noindex') else 'index,follow,max-snippet:-1,max-image-preview:large'}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="sitemap" type="application/xml" href="/sitemap.xml">
<style>{CSS}</style>
<script type="application/ld+json">{schema_for(p)}</script>
</head>
<body>
{GTM_BODY}
<header class="top"><div class="wrap">
<a class="logo" href="/">google<span>ads</span>freelancer</a>
<nav class="main" aria-label="Main">{nav_html(slug)}</nav>
<a class="btn top-cta" href="{FORM_URL}">Get a quote</a>
{mobile_menu_html()}
</div></header>
<main>
<section class="hero"><div class="wrap">
<p class="kicker">{esc(p.get('kicker', BRAND))}</p>
<div class="hero-grid"><div>
<h1>{p['h1']}</h1>
<p class="lead">{p['lead']}</p>
<div class="cta-row"><a class="btn" href="{"#form" if slug == "contact" else FORM_URL}">Get a quote</a><a class="btn ghost" href="{'#services' if slug == 'index' else ('/#services' if slug == 'pricing' else '/pricing/')}">View services &amp; pricing</a></div>
</div>{('<img src="/diego.jpg" alt="' + NAME + ', independent Google Ads consultant" width="340" height="425" loading="eager">') if (PHOTO and slug == 'about') else ''}</div>
{('<div class="proof">' + proof_html + '</div>') if proof_html else ''}
</div></section>
{p['body']}
{faq_html(p.get('faq'))}
{related_html(slug)}
{cta_html(p)}
</main>
{footer_html()}
{EMAIL_JS}{CLICK_JS}{FORM_JS}{p.get('extra_js', '')}
</body>
</html>
"""


def privacy_page():
    body = f"""<section><div class="wrap">
<h2>What this site collects</h2>
<p>This site is a set of static pages. It uses the following third-party tags, loaded through Google Tag Manager:</p>
<ul><li><b>Google Analytics 4.</b> Measures visits, pages viewed, clicks on the quote and email links and form submissions, to understand which pages are useful. Sets first-party cookies (<code>_ga</code>, <code>_ga_*</code>). Data is processed by Google under <a href="https://policies.google.com/privacy" rel="noopener">Google's privacy policy</a>.</li>
<li><b>Google Ads conversion measurement.</b> When you arrive from a Google ad and send the form, the enquiry is reported back to Google Ads as a conversion so ad spend can be judged on real outcomes.</li></ul>
<p>You can block these with your browser's tracking protection or an extension such as Google's <a href="https://tools.google.com/dlpage/gaoptout" rel="noopener">Analytics opt-out</a>; the site works the same without them.</p>
<ul><li><b>Contact form.</b> What you type in the form is relayed to my inbox by <a href="https://web3forms.com/privacy" rel="noopener">Web3Forms</a> and is not stored on this site. I use it only to reply.</li>
<li><b>Email.</b> Messages to {email_link()} go to {NAME} directly and are kept for the purpose of replying and, if you become a client, running the engagement.</li>
<li><b>Hosting.</b> Pages are served by Cloudflare, which processes IP addresses and request logs to deliver the site and protect it from abuse.</li></ul>
<h2>Your rights</h2>
<p>You can ask what personal data I hold about you, ask for it to be corrected or deleted, or object to its use, by emailing {email_link()}. Requests are answered by the same person who received your original message.</p>
<h2>Controller</h2>
<p>{NAME}, operating as Diwizi, Curitiba, Brazil. Contact: {email_link()}.</p>
</div></section>"""
    return {"slug": "privacy", "short": "Privacy", "blurb": "", "title": "Privacy policy | Google Ads Freelancer",
            "meta": "What googleadsfreelancer.com collects, why, and how to reach the person responsible for it.",
            "h1": "Privacy policy", "lead": "Short, because there is little to say: static pages, analytics, a contact form and an email address.",
            "body": body, "kicker": "Legal", "proof": [], "noindex": False}


def thanks_page():
    body = f"""<section><div class="wrap">
<h2>What happens next</h2>
<ol class="steps">
<li><div><strong>I read it myself.</strong> Usually the same working day; within one working day at most.</div></li>
<li><div><strong>You get one reply</strong> from {email_link()}: whether I can help, what I would look at first, a price range, and two or three times for a short call if it makes sense to talk.</div></li>
<li><div><strong>Nothing else.</strong> No sequence, no newsletter. If you do not answer, I assume the timing was wrong.</div></li>
</ol>
<p>Want to add anything? Write to {email_link()}, and include read-only access to Google Ads and GA4 if you already know you want an audit.</p>
</div></section>"""
    # Fires only when Cal.com actually sent back a booking uid, and only once per uid
    # (sessionStorage + localStorage, so a refresh or a second tab doesn't double-count).
    js = ("<script>(function(){try{"
          "var id=window.__tyUid||'';if(!id)return;"
          "var k='gaf_call_'+id,ja=false;"
          "try{ja=!!(sessionStorage.getItem(k)||localStorage.getItem(k))}catch(e){}"
          "if(ja)return;"
          "window.dataLayer=window.dataLayer||[];"
          "window.dataLayer.push({event:'booking_confirmed',booking_source:'cal.com',booking_uid:id});"
          "try{sessionStorage.setItem(k,'1');localStorage.setItem(k,'1')}catch(e){}"
          "}catch(e){}})();</script>"
          # Booking copy when the visitor came from a Cal.com booking rather than the form.
          "<script>(function(){try{if(!window.__tyUid)return;var h=document.querySelector('h1'),l=document.querySelector('p.lead');"
          "if(h)h.textContent='Your call is booked';if(l)l.textContent='Thanks. Cal.com sends the confirmation and calendar invite; if it is not there in a few minutes, look in spam.';}catch(e){}})();</script>")
    return {"slug": "thanks", "short": "Thanks", "blurb": "", "title": "Message received | Google Ads Freelancer",
            "meta": "Your message to Diego Zietek has been received.", "h1": "Got it. You will hear from me, not from a sequence.",
            "lead": "Thanks for the detail. Here is exactly what happens next.",
            "body": body, "kicker": "Received", "proof": [], "noindex": True,
            "pre_gtm_head": TY_LIMPA_JS, "extra_js": js,
            "cta_title": "Forgot something?",
            "cta_text": "Send it here and I will fold it into the same reply.", "no_form": True}


def build():
    dist = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")
    if os.path.isdir(dist):
        shutil.rmtree(dist)
    os.makedirs(dist)
    all_pages = PAGES + [privacy_page(), thanks_page()]
    urls = []
    for p in all_pages:
        path = os.path.join(dist, out_path(p["slug"]))
        os.makedirs(os.path.dirname(path) or dist, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(render(p))
        if p.get("noindex"):
            continue
        urls.append((SITE + url_for(p["slug"]), "1.0" if p["slug"] == "index" else ("0.5" if p["slug"] == "privacy" else "0.8")))
    with open(os.path.join(dist, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for u, pr in urls:
            f.write(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>\n")
        f.write("</urlset>\n")
    if PHOTO:
        shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "diego.jpg"), os.path.join(dist, "diego.jpg"))
    shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", BRAND_SPRITE), os.path.join(dist, BRAND_SPRITE))
    with open(os.path.join(dist, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /thanks/\n\nSitemap: {SITE}/sitemap.xml\n")
    with open(os.path.join(dist, "favicon.svg"), "w") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#1a56db"/>'
                '<text x="32" y="43" font-family="Arial,Helvetica,sans-serif" font-size="30" font-weight="700" fill="#fff" text-anchor="middle">GA</text></svg>')
    with open(os.path.join(dist, "_headers"), "w") as f:
        f.write("/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n"
                "  X-Frame-Options: SAMEORIGIN\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n"
                "/favicon.svg\n  Cache-Control: public, max-age=604800\n")
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
