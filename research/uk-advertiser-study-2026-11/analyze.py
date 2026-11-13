"""Read each advertiser's home page (and its Tag Manager containers) and record what it measures.
Pages are fetched by DataForSEO's On-Page API; nothing here runs the sites' JavaScript."""
import json, os, re, sys, time, concurrent.futures as cf
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dfs
HERE = os.path.dirname(os.path.abspath(__file__))
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
CACHE = os.path.join(HERE, "pages"); os.makedirs(CACHE, exist_ok=True)

def fetch(url, hops=3):
    """Return (status, body). Follows up to `hops` redirects."""
    for _ in range(hops):
        d = dfs.call("/v3/on_page/instant_pages", [{"url": url, "store_raw_html": True, "custom_user_agent": UA}])
        t = d["tasks"][0]
        res = (t.get("result") or [{}])[0]
        items = res.get("items") or []
        if not items:
            return (res.get("crawl_status") or t.get("status_message") or "no item"), ""
        it = items[0]
        st = it.get("status_code")
        if st in (301, 302, 303, 307, 308) and it.get("location"):
            loc = it["location"]
            url = loc if loc.startswith("http") else re.match(r"https?://[^/]+", url).group(0) + (loc if loc.startswith("/") else "/" + loc)
            continue
        if st != 200:
            return st, ""
        r = dfs.call("/v3/on_page/raw_html", [{"id": t["id"], "url": url}])
        body = ((r["tasks"][0].get("result") or [{}])[0].get("items") or {}).get("html") or ""
        return 200, body
    return "redirect loop", ""

RX_GTM = re.compile(r"\bGTM-[A-Z0-9]{5,9}\b")
RX_AW = re.compile(r"\bAW-\d{8,12}\b")
RX_GA4 = re.compile(r"\bG-[A-Z0-9]{8,12}\b")
CONSENT = {"Cookiebot": r"cookiebot", "OneTrust": r"onetrust|optanon", "CookieYes": r"cookieyes|cky-consent|cookie-law-info", "Complianz": r"complianz|cmplz",
           "Iubenda": r"iubenda", "Termly": r"termly", "Usercentrics": r"usercentrics", "Civic Cookie Control": r"civicuk|cookiecontrol|cookie-control", "Cookie Script": r"cookie-script",
           "CookieFirst": r"cookiefirst", "Borlabs": r"borlabs", "Didomi": r"didomi", "TrustArc": r"trustarc|consent\.truste|truste\.com", "Osano": r"osano", "Quantcast": r"quantcast|quantserve",
           "Moove GDPR": r"moove_gdpr|gdpr-cookie-compliance", "Wix consent": r"consentPolicyManager", "Shopify consent": r"customerPrivacy", "Cookie Notice": r"cookie-notice|cookie_notice",
           "Real Cookie Banner": r"real-cookie-banner", "HubSpot banner": r"hs-banner|hs-eu-cookie", "Squarespace banner": r"sqs-cookie-banner", "Other banner": r"cookieconsent|cookie-consent|cookie_consent|cc-window|cookie-banner|cookiebanner"}
CALLTRACK = {"CallRail": r"callrail|calltrk", "Infinity": r"infinitycloud|infinity-tracking|ictnumbers", "ResponseTap": r"responsetap|adinsight", "Ruler Analytics": r"ruleranalytics|ruler\.nyltx",
             "WhatConverts": r"whatconverts", "Mediahawk": r"mediahawk", "Calltracks": r"calltracks", "CallTrackingMetrics": r"calltrackingmetrics|tctm\.co", "Nimbata": r"nimbata",
             "Invoca": r"invoca", "Iovox": r"iovox", "AVANSER": r"avanser", "Delacon": r"delacon", "Freespee": r"freespee", "Call Tracker (generic DNI)": r"dynamic[-_ ]number|number[-_ ]insertion"}

SECTOR_RX = {
    "Solicitors": r"solicitor|conveyanc|law firm|lawyer|legal",
    "Accountants": r"accountan|bookkeep|tax return|payroll",
    "Dentists": r"dent|orthodont|invisalign",
    "Private healthcare and physiotherapy": r"physio|clinic|osteopath|chiropract|podiatr|private gp|doctor",
    "Plumbing and heating": r"plumb|boiler|heating|gas safe",
    "Electricians": r"electric|rewir|ev charg|niceic",
    "Roofing": r"roof|gutter",
    "Estate and letting agents": r"estate agen|letting|landlord|valuation|property for sale",
    "Mortgage and financial advice": r"mortgage|financial advi|financial plann|pension|wealth",
    "IT support": r"it support|managed it|managed service|cyber|computer repair|helpdesk|microsoft 365|it services",
    "Removals": r"removal|man and van|man & van|moving house|storage",
    "Home improvement": r"loft|kitchen|bathroom|builder|driveway|extension",
    "Cleaning": r"clean",
    "Pest control": r"pest|wasp|rodent|vermin",
    "Locksmiths and drainage": r"locksmith|drain|\block",
}
RX_UK = re.compile(r"\+44|\b0[1-9]\d{2,3}[ -]?\d{3}[ -]?\d{3,4}\b|\b[A-Z]{1,2}\d[A-Z\d]? ?\d[A-Z]{2}\b|united kingdom|england|scotland|wales|\blondon\b|vat (reg|no)|company (reg|no)|registered in", re.I)

def analyse(domain, sector=None):
    out = {"domain": domain, "sector": sector}
    path = os.path.join(CACHE, domain + ".html")
    if os.path.exists(path):
        st, html = 200, open(path, encoding="utf-8", errors="replace").read()
    else:
        st, html = fetch("https://" + domain + "/")
        if st != 200 and not domain.startswith("www."):
            st, html = fetch("https://www." + domain + "/")
        if st == 200 and html:
            open(path, "w", encoding="utf-8").write(html)
    out["status"] = st
    if st != 200 or len(html) < 500:
        out["readable"] = False
        return out
    out["readable"] = True
    mt = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
    out["title"] = re.sub(r"\s+", " ", mt.group(1)).strip()[:120] if mt else ""
    text = re.sub(r"(?s)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", html)
    text = re.sub(r"<[^>]+>", " ", text); text = re.sub(r"\s+", " ", text)
    out["text_len"] = len(text)
    out["uk_signal"] = bool(domain.endswith(".uk") or RX_UK.search(text[:80000]))
    out["sector_match"] = bool(sector and re.search(SECTOR_RX.get(sector, "."), (out["title"] + " " + text[:60000]), re.I))
    out["parked"] = bool(re.search(r"domain (is )?for sale|buy this domain|parked free|coming soon|under construction|sedoparking|godaddy\.com/forsale", text[:5000], re.I) or len(text) < 400)
    extra = ""
    m1, m2 = re.search(r'"metaSiteId":"([a-f0-9-]{36})"', html), re.search(r'"siteId":"([a-f0-9-]{36})"', html)
    out["platform"] = ("Wix" if "parastorage.com" in html else "Shopify" if "cdn.shopify.com" in html else "Squarespace" if "squarespace" in html.lower()
                       else "WordPress" if "wp-content" in html else "Webflow" if "webflow" in html.lower() else "other")
    if out["platform"] == "Wix" and m1 and m2:
        u = (f"https://{domain}/_api/tag-manager/api/v1/tags/sites/{m1.group(1)}?wixSite=false&htmlsiteId={m2.group(1)}"
             "&language=en&categories=essential%2Cfunctional%2Canalytics%2Cadvertising")
        wp = os.path.join(CACHE, domain + ".wixtags.json")
        try:
            if os.path.exists(wp): s2, b2 = 200, open(wp, encoding="utf-8", errors="replace").read()
            else:
                s2, b2 = fetch(u)
                if s2 == 200: open(wp, "w", encoding="utf-8").write(b2)
            if s2 == 200: extra += "\n" + b2.replace("\\n", "\n").replace('\\"', '"').replace("\\/", "/")
        except Exception: pass
    page = html + extra
    gtm_ids = sorted(set(RX_GTM.findall(page)) - {"GTM-XXXXXX", "GTM-XXXXXXX", "GTM-XXXX"})[:4]
    gt_ids = sorted(set(re.findall(r"\bGT-[A-Z0-9]{6,12}\b", page)))[:2]
    direct = (gt_ids + sorted(set(RX_GA4.findall(page)))[:1] + sorted(set(RX_AW.findall(page)))[:1])[:3]
    out["google_tag_ids"] = direct
    containers = ""
    for g in gtm_ids + direct:
        p = os.path.join(CACHE, g + ".js")
        if os.path.exists(p):
            c = open(p, encoding="utf-8", errors="replace").read()
        else:
            try:
                s3, c = fetch("https://www.googletagmanager.com/" + ("gtm.js?id=" if g.startswith("GTM-") else "gtag/js?id=") + g)
            except Exception:
                s3, c = "err", ""
            if s3 == 200: open(p, "w", encoding="utf-8").write(c)
        containers += "\n// Copyright 2012 Google Inc." + (c or "")
    out["gtm"] = bool(gtm_ids); out["gtm_ids"] = gtm_ids; out["gtm_container_read"] = bool(containers.strip())
    # A gtm.js file is the container's own configuration ("var data = {...}", up to "runtime") followed by Google's shared
    # library. Tag types and IDs are read from the configuration only; the library mentions every feature for every site.
    conf, vendor_text = "", ""
    for c in containers.split("\n// Copyright 2012 Google Inc.") if containers else []:
        i = c.find("var data = {")
        if i < 0: continue
        j = c.find('"runtime":', i)
        conf += c[i:j if j > 0 else i + 200000] + "\n"
        k = c.find("\n};\n", i)
        vendor_text += c[i:k if k > 0 else i + 400000] + "\n"   # configuration plus custom template code, without the library
    containers = conf
    fn = set(re.findall(r'"function":"(__[a-z_0-9]+)"', conf))
    low_page, low_all = page.lower(), (page + vendor_text).lower()
    aw_page, aw_cont = set(RX_AW.findall(page)), set(RX_AW.findall(conf))
    out["ads_tag"] = bool(aw_page or aw_cont or "__awct" in fn or "__sp" in fn or "__awcc" in fn or "__awec" in fn or "googleadservices.com/pagead/conversion" in low_all)
    conv_page = bool(re.search(r"send_to['\"]?\s*:\s*['\"]AW-\d+/[A-Za-z0-9_-]+", page) or re.search(r"google_conversion_label", page)
                     or re.search(r"gtag\(\s*['\"]event['\"]\s*,\s*['\"]conversion['\"]", page) or re.search(r"AW-\d{8,12}/[A-Za-z0-9_-]{8,}", page))
    conv_cont = bool("__awct" in fn or "__awcc" in fn or re.search(r"AW-\d{8,12}/[A-Za-z0-9_-]{8,}", containers))
    out["ads_conversion"] = conv_page or conv_cont
    out["ads_call_conversion"] = bool("__awcc" in fn or "phone_conversion_number" in low_page or "_googwcmget" in low_page or "google_wcc" in low_page)
    out["ads_remarketing"] = bool("__sp" in fn or (out["ads_tag"] and not out["ads_conversion"]))
    out["conversion_linker"] = "__gclidw" in fn
    out["ga4"] = bool(RX_GA4.findall(page) or RX_GA4.findall(conf) or "__gaawe" in fn or "__gaawc" in fn or "__get" in fn and gt_ids)
    out["google_tag_gt"] = bool(gt_ids)
    out["tel_click_tag"] = bool("tel:" in conf.lower() and ("__awct" in fn or "__gaawe" in fn or "__awcc" in fn))
    out["ua_legacy_only"] = bool(re.search(r"\bUA-\d{4,10}-\d{1,3}\b", page + conf)) and not out["ga4"]
    out["meta_pixel"] = bool("fbevents.js" in low_all or re.search(r"fbq\(\s*['\"]init", page + vendor_text) or "connect.facebook.net" in low_all and "fbq" in low_all)
    out["microsoft_uet"] = bool("bat.bing.com" in low_all or "__bzi" in fn or "__baut" in fn)
    out["enhanced_conversions"] = bool("__awec" in fn or "user_data" in conf and "__awct" in fn)
    out["clarity_or_hotjar"] = bool("clarity.ms" in low_all or "hotjar" in low_all or "__hjtc" in fn)
    out["consent_vendor"] = next((k for k, rx in CONSENT.items() if re.search(rx, page, re.I)), "")
    out["consent_banner"] = bool(out["consent_vendor"])
    out["consent_mode"] = bool(re.search(r"['\"]consent['\"]\s*,\s*['\"]default['\"]", page) or "ad_user_data" in low_page)
    out["call_tracking_vendor"] = next((k for k, rx in CALLTRACK.items() if re.search(rx, page + vendor_text, re.I)), "")
    out["tel_link"] = bool(re.search(r"href\s*=\s*['\"]?tel:", page, re.I))
    out["form"] = bool(re.search(r"<form\b", page, re.I) and re.search(r"type\s*=\s*['\"]?(email|tel)|<textarea|wpcf7|gform|wpforms|elementor-form|hs-form|name=['\"](phone|message|your-)", page, re.I))
    out["any_measurement"] = bool(out["gtm"] or out["ga4"] or out["ads_tag"] or out["google_tag_gt"] or out["meta_pixel"] or out["microsoft_uet"] or out["ua_legacy_only"] or out["clarity_or_hotjar"])
    # Signs that a tag exists but its ID is not in the page source (loaded by a script bundle, a site builder or a consent tool).
    out["hidden_tag_signal"] = bool(not out["any_measurement"] and re.search(
        r"(dns-prefetch|preconnect)[^>]{0,80}(googletagmanager|google-analytics|connect\.facebook)|function gtag\(|window\.gtag\s*=|gtag\(\s*['\"]consent|dataLayer\.push|wsimg\.com/signals|plausible\.io|matomo|cloudflareinsights|statcounter|hs-scripts\.com|usefathom", page, re.I))
    out["call_measured"] = bool(out["ads_call_conversion"] or out["call_tracking_vendor"] or out["tel_click_tag"])
    return out

if __name__ == "__main__":
    doms = json.load(open(os.path.join(HERE, sys.argv[1])))   # {domain: sector} or [domain, ...]
    if isinstance(doms, list): doms = {d: None for d in doms}
    res_path = os.path.join(HERE, "sites.json")
    done = {r["domain"]: r for r in (json.load(open(res_path)) if os.path.exists(res_path) else [])}
    todo = [d for d in doms if d not in done]
    print("to read", len(todo), "already", len(done), flush=True)
    def safe(d):
        try: return analyse(d, doms[d])
        except Exception as e: return {"domain": d, "sector": doms[d], "status": "error " + type(e).__name__, "readable": False}
    with cf.ThreadPoolExecutor(8) as ex:
        for i, r in enumerate(ex.map(safe, todo), 1):
            done[r["domain"]] = r
            if i % 25 == 0:
                json.dump(list(done.values()), open(res_path, "w")); print(i, "read, spent", round(dfs.SPENT, 4), flush=True)
    json.dump(list(done.values()), open(res_path, "w"))
    rd = [r for r in done.values() if r.get("readable")]
    print("FINISHED total", len(done), "readable", len(rd), "spent", round(dfs.SPENT, 4))
