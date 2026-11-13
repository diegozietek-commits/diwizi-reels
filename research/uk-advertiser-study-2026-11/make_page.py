"""Write the study page (guides_src file), the public sector CSV and the Dataset JSON-LD from summary.json."""
import json, os, re, csv, sys
HERE = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = sys.argv[1]
S = json.load(open(os.path.join(HERE, "summary.json"))); K = json.load(open(os.path.join(HERE, "kept.json")))
o, sec, fu = S["overall"], S["sectors"], S["funnel"]
N = o["n"]
slug = lambda s: re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
def bars(key, rows, base_note=""):
    h = '<div class="bars">'
    for name, b in rows:
        v = b[key]
        h += f'<div class="bar"><span>{name}</span><div class="trk"><i style="width:{max(v, 1)}%"></i></div><em>{v}%</em></div>'
    return h + "</div>"
by_conv = sorted(sec.items(), key=lambda x: (-x[1]["conv"], x[0]))
by_none = sorted(sec.items(), key=lambda x: (-x[1]["nothing"], x[0]))
top, bottom = by_conv[0], by_conv[-1]
small = [s for s, b in sec.items() if b["n"] < 10]
table_rows = "".join(
    f'<tr><td><a href="#{slug(s)}">{s}</a>{" *" if b["n"] < 10 else ""}</td><td>{b["n"]}</td><td>{b["conv"]}%</td><td>{b["ads_tag_no_conv"]}%</td><td>{b["ga_only"]}%</td>'
    f'<td>{b["nothing"]}%</td><td>{b["banner"]}%</td><td>{b["tel"]}%</td><td>{b["call_measured_of_tel"]}%</td></tr>' for s, b in by_conv)
cards = ""
for s, b in sorted(sec.items()):
    note = " Fewer than ten sites were read here, so treat this as a first picture." if b["n"] < 10 else ""
    cards += (f'<div class="card" id="{slug(s)}"><h3>{s}</h3><p><strong>{b["n"]} sites read.</strong> {b["conv"]}% show a Google Ads conversion tag, '
              f'{b["ga_only"]}% count visits with Google Analytics and show no Google Ads tag, and {b["nothing"]}% show no measurement at all. '
              f'{b["tel"]}% publish a clickable phone number, and of those {b["call_not_measured_of_tel"]}% have nothing we could find to count the call.{note}</p></div>')
# one well-measured site per sector: conversion tag, call measurement, analytics and a consent banner all found
best, seen = [], set()
for r in sorted([r for r in K if r["grp"] == "A" and r["call_measured"] and (r["ga4"] or r["google_tag_gt"]) and r.get("banner")],
                key=lambda r: (-(r["enhanced_conversions"] + r["conversion_linker"] + r["meta_pixel"] + bool(r["call_tracking_vendor"])), r["domain"])):
    if r["sector"] not in seen:
        seen.add(r["sector"]); best.append(r)
best_li = "".join(f'<li><strong>{r["domain"]}</strong>, {r["sector"].lower()}</li>' for r in sorted(best, key=lambda r: r["sector"]))

body = f"""
<section id="headline"><div class="wrap">
<h2>The short version</h2>
<div class="stat-row">
<div class="stat"><b>{o["conv"]}%</b><span>show a Google Ads conversion tag on the home page or inside the tag container</span></div>
<div class="stat"><b>{o["ga_only"]}%</b><span>count visits with Google Analytics and show no Google Ads tag at all</span></div>
<div class="stat"><b>{o["nothing"]}%</b><span>show no measurement of any kind</span></div>
<div class="stat"><b>{o["call_not_measured_of_tel"]}%</b><span>of the sites with a clickable phone number have nothing we could find to count the call</span></div>
</div>
<p>All {N} businesses had a Google ad shown in the United Kingdom between {S["last_shown_min"][8:10]} October and {S["last_shown_max"][8:10]} November 2026, according to Google's own Ads Transparency Center, and all of them are marked there as verified advertisers. They are paying for clicks now. Fewer than half show Google which click became a customer.</p>
<p>The figures are free to quote with a link to this page. The table by sector can be downloaded as a <a href="/data/uk-google-ads-measurement-2026-11.csv">CSV file</a>.</p>
</div></section>

<section id="groups"><div class="wrap">
<h2>Six groups, adding up to 100%</h2>
<p>Every site falls into exactly one group, read from the outside, with no access to anyone's account.</p>
<table><thead><tr><th>Group</th><th>Share of the {N} sites</th><th>What it means for the owner</th></tr></thead><tbody>
<tr><td>A Google Ads conversion tag is visible</td><td>{o["conv"]}%</td><td>Google Ads is being told about at least one kind of result. Whether it is the right result is a separate question.</td></tr>
<tr><td>A Google Ads tag, but no conversion action visible from the home page</td><td>{o["ads_tag_no_conv"]}%</td><td>The tag is installed. The conversion may fire on a thank-you page we did not read, or may not exist.</td></tr>
<tr><td>Google Analytics or a Google tag, and no Google Ads tag</td><td>{o["ga_only"]}%</td><td>Visits are counted. Unless results are imported from Analytics into Google Ads, which cannot be seen from outside, the bidding learns nothing from enquiries.</td></tr>
<tr><td>Other tags only</td><td>{o["other_only"]}%</td><td>An empty Tag Manager container, a retired Universal Analytics tag, a Meta Pixel or a heatmap tool, with nothing for Google Ads.</td></tr>
<tr><td>Signs of a tag we could not read</td><td>{o["hidden"]}%</td><td>The page prepares for a Google tag but the ID is loaded by a script. Counted apart so the next row is not overstated.</td></tr>
<tr><td>No measurement of any kind</td><td>{o["nothing"]}%</td><td>No Tag Manager, no Google tag, no Analytics, no Meta Pixel. The adverts run and nothing on the site records what they bring.</td></tr>
</tbody></table>
</div></section>

<section id="chart"><div class="wrap">
<h2>Google Ads conversion tag, by sector</h2>
<p>Share of sites in each sector where a Google Ads conversion tag was found. The spread runs from {top[1]["conv"]}% in {top[0].lower()} to {bottom[1]["conv"]}% in {bottom[0].lower()}.</p>
{bars("conv", by_conv)}
<h3>No measurement of any kind, by sector</h3>
{bars("nothing", by_none)}
</div></section>

<section id="sectors"><div class="wrap">
<h2>The full table by sector</h2>
<table><thead><tr><th>Sector</th><th>Sites read</th><th>Google Ads conversion tag</th><th>Google Ads tag, no conversion seen</th><th>Analytics only</th><th>No measurement</th><th>Consent banner found</th><th>Clickable phone number</th><th>Calls measured, of sites with a number</th></tr></thead><tbody>
{table_rows}
<tr><td><strong>All sectors</strong></td><td><strong>{N}</strong></td><td><strong>{o["conv"]}%</strong></td><td><strong>{o["ads_tag_no_conv"]}%</strong></td><td><strong>{o["ga_only"]}%</strong></td><td><strong>{o["nothing"]}%</strong></td><td><strong>{o["banner"]}%</strong></td><td><strong>{o["tel"]}%</strong></td><td><strong>{o["call_measured_of_tel"]}%</strong></td></tr>
</tbody></table>
<p>{"* Fewer than ten sites read. " if small else ""}Groups of ten to twenty sites move by several points with a single site, so read the table as a picture of each sector and not as a league table.</p>
<div class="cols">{cards}</div>
</div></section>

<section id="calls"><div class="wrap">
<h2>The phone call is the lead, and half the time nothing counts it</h2>
<p>{o["tel"]}% of the sites publish a phone number a visitor can tap. For most of these businesses the call is the enquiry they want. Among the {o["n_tel"]} sites with a clickable number:</p>
<ul>
<li><strong>{o["ads_call_conv_of_tel"]}%</strong> carry Google's own website call conversion, which swaps the number on the page for a Google forwarding number.</li>
<li><strong>{o["call_vendor_of_tel"]}%</strong> carry a call tracking service from another supplier.</li>
<li><strong>{o["tel_click_of_tel"]}%</strong> have a tag that fires when the number is clicked, which counts taps and not conversations.</li>
<li><strong>{o["call_not_measured_of_tel"]}%</strong> have none of the three.</li>
</ul>
<p>One caveat matters here. Google's help page on <a class="inline-link" href="https://support.google.com/google-ads/answer/1722022?hl=en-GB" rel="noopener" target="_blank">conversion measurement</a> says "Some kinds of conversion measurement don't require a tag", and gives the example of calls from call assets, where "you use a Google forwarding number to track when the call came from one of your ads". A business can therefore count calls made straight from the advert with nothing on its site. What it cannot count that way is the visitor who clicks the advert, reads the page and then rings the number on it.</p>
</div></section>

<section id="carry"><div class="wrap">
<h2>What the {N} sites carry</h2>
<table><thead><tr><th>What we looked for</th><th>Share of the {N} sites</th><th>Why it matters to the owner</th></tr></thead><tbody>
<tr><td>Any Google Ads tag</td><td>{o["ads_tag"]}%</td><td>The starting point for conversions and for remarketing</td></tr>
<tr><td>Google Ads conversion tag</td><td>{o["conv"]}%</td><td>Without it the account bids on clicks, not on enquiries</td></tr>
<tr><td>Google Analytics 4 or a Google tag</td><td>{o["ga4"]}%</td><td>Visits are counted. Visits are not leads</td></tr>
<tr><td>Google Tag Manager container</td><td>{o["gtm"]}%</td><td>The usual place the conversion tag lives</td></tr>
<tr><td>Meta Pixel</td><td>{o["meta"]}%</td><td>Facebook and Instagram adverts without it run blind</td></tr>
<tr><td>Microsoft Advertising tag</td><td>{o["uet"]}%</td><td>Few of these advertisers measure Bing at all</td></tr>
<tr><td>Consent banner from a recognisable tool</td><td>{o["banner"]}%</td><td>UK rules ask for a choice before marketing cookies are set</td></tr>
<tr><td>Clickable phone number</td><td>{o["tel"]}%</td><td>The enquiry most of these businesses actually want</td></tr>
<tr><td>Enquiry form on the home page</td><td>{o["form"]}%</td><td>The other enquiry, and the easier one to count</td></tr>
</tbody></table>
</div></section>

<section id="best"><div class="wrap">
<h2>One well-measured site in each sector</h2>
<p>These sites carry the full set on their home page: a Google Ads conversion tag, some form of call measurement, Google Analytics and a consent banner. They are listed because they do it properly, and for no other reason.</p>
<ul>{best_li}</ul>
</div></section>

<section id="owner"><div class="wrap">
<h2>What this means if you are paying for Google Ads</h2>
<ul>
<li><strong>Ask one question of whoever runs your account.</strong> Which conversion action is the primary one, and when did it last record a conversion. If the answer takes more than a minute, read <a class="inline-link" href="/guides/google-ads-conversions-not-tracking-uk/">what to check when conversions are not tracking</a>.</li>
<li><strong>A phone number on the page is not a measured phone call.</strong> {o["tel"]}% of these sites show a number and {o["call_not_measured_of_tel"]}% of those have nothing to count the call that follows the click.</li>
<li><strong>Analytics is not conversion tracking.</strong> Google Analytics tells you people came. Only a conversion sent to Google Ads, or imported into it, tells the bidding which clicks were worth paying for.</li>
<li><strong>Consent handling is part of measurement.</strong> A banner that blocks tags with no consent mode behind it removes a share of your conversions from the reports. Google explains how <a class="inline-link" href="https://support.google.com/google-ads/answer/10000067?hl=en-GB" rel="noopener" target="_blank">consent mode</a> recovers part of them.</li>
<li><strong>If your site is in the last group,</strong> the first job is not a new campaign. It is a tag, a conversion action and a test. That is what a <a href="/conversion-tracking/">conversion tracking setup</a> covers, and a <a href="/ppc-audit/">PPC audit</a> will tell you which group your own site is in.</li>
</ul>
</div></section>

<section id="method"><div class="wrap">
<h2>How this was measured</h2>
<ol class="steps">
<li><div><strong>Finding the advertisers.</strong> On 13 November 2026 we searched Google's <a class="inline-link" href="https://adstransparency.google.com/?region=GB" rel="noopener" target="_blank">Ads Transparency Center</a>, with the region set to the United Kingdom, for the words a business in each of 15 service sectors is likely to have in its web address, such as plumbers, solicitors, dental or removals, alone and combined with London, Manchester, Birmingham, Leeds and Bristol. The Transparency Center returns advertiser websites that match.</div></li>
<li><div><strong>Keeping only live advertisers.</strong> We checked {fu["domains_checked"]} of those websites in the Transparency Center and kept the {fu["active_30d"]} with an advert last shown in the UK on or after 14 October 2026.</div></li>
<li><div><strong>Reading the sites.</strong> We read the source of each home page, every Google Tag Manager container and Google tag file it refers to, and, for sites built on Wix, the list of tags the platform loads. {fu["readable"]} home pages could be read. The rest refused the request or did not answer.</div></li>
<li><div><strong>Removing what did not belong.</strong> We removed sites that were not UK businesses, were not in the sector they were found under, or were parked pages. {N} sites remain.</div></li>
<li><div><strong>Counting.</strong> Each share on this page is a count over those {N} sites, or over the sites of one sector. Nothing was estimated or weighted.</div></li>
</ol>
<h3>What this study cannot see</h3>
<ul>
<li><strong>Tags on other pages.</strong> Only the home page was read. A conversion tag placed only on a thank-you page is missed, which is why sites with a Google Ads tag and no visible conversion are reported as their own group.</li>
<li><strong>Imports from Analytics.</strong> A business can import results from Google Analytics into Google Ads with no Google Ads tag on the site. That is invisible from outside, so the analytics-only group is not described as untracked.</li>
<li><strong>Calls counted inside the advert.</strong> Calls made straight from a call asset need no tag on the site.</li>
<li><strong>Tags loaded by a script.</strong> The pages were read without running their scripts and without accepting cookies. Where a page showed signs of a tag whose ID we could not read, it was counted in a separate group.</li>
<li><strong>The sample is not random.</strong> Looking for trade words in web addresses favours smaller local firms whose address names what they do. Large national brands are mostly absent.</li>
<li><strong>Small groups.</strong> Sectors hold between {min(b["n"] for b in sec.values())} and {max(b["n"] for b in sec.values())} sites, and the reading was taken on a single day.</li>
</ul>
<p>An earlier edition of this page, published on 6 November 2026, covered 34 sites. This edition replaces it. The larger sample and the reading of Google tag files and Wix tag lists explain the differences between the two.</p>
</div></section>
"""
faq = [
 ("How many UK businesses advertising on Google have conversion tracking?", f"Of the {N} UK advertisers read for this study, {o['conv']}% show a Google Ads conversion tag on the home page or inside their tag container. A further {o['ads_tag_no_conv']}% carry a Google Ads tag with no conversion action visible from the home page, and {o['nothing']}% show no measurement of any kind."),
 ("Does a Google Analytics tag count as Google Ads conversion tracking?", f"No. Google Analytics counts visits and events. Google Ads only learns which click became an enquiry when a conversion action is set up in Google Ads or imported from Analytics. In this study {o['ga_only']}% of sites had Analytics or a Google tag and no Google Ads tag at all."),
 ("Which UK sectors measure their Google Ads best?", f"Among the 15 sectors read, {top[0].lower()} had the highest share of sites with a Google Ads conversion tag, at {top[1]['conv']}%, and {bottom[0].lower()} the lowest, at {bottom[1]['conv']}%. The groups are small, so the order should be read as a picture and not as a ranking."),
 ("How did you find the advertisers?", f"Through Google's Ads Transparency Center, with the region set to the United Kingdom. We searched for trade words that appear in web addresses, kept the websites with an advert last shown in the UK in the previous 30 days, and removed those that were not UK businesses in the sector. All {N} are marked as verified advertisers."),
 ("Can a business count phone calls with no tag on its site?", "Partly. Google's help page says some conversion measurement does not require a tag, and gives calls from call assets as the example. That counts calls made straight from the advert. It does not count the visitor who clicks through, reads the page and rings the number on it, which needs a call conversion or a call tracking service on the site."),
 ("What should I do if my site has no tag?", "Ask whoever runs the account to show you the Conversions page in Google Ads and the status of each action. If there is no action, or it is inactive, the tag needs to be installed and tested before any bidding strategy can work."),
]
dataset = {"@context": "https://schema.org", "@type": "Dataset", "name": f"What {N} UK businesses paying for Google Ads measure on their sites, by sector (November 2026)",
           "description": f"Share of {N} UK advertisers in 15 service sectors whose home page carries a Google Ads conversion tag, Google Analytics, a consent banner and call measurement. Advertisers were taken from Google's Ads Transparency Center and their sites read on 13 November 2026.",
           "url": "https://ppcconsultancy.uk/guides/google-ads-advertisers-measurement-uk/", "creator": {"@type": "Person", "name": "Diego Willian Zietek", "url": "https://ppcconsultancy.uk/about/"},
           "datePublished": "2026-11-13", "temporalCoverage": f'{S["last_shown_min"]}/{S["last_shown_max"]}', "spatialCoverage": {"@type": "Place", "name": "United Kingdom"},
           "isAccessibleForFree": True, "variableMeasured": ["Google Ads conversion tag", "Google Ads tag", "Google Analytics 4", "Google Tag Manager", "Meta Pixel", "Consent banner", "Clickable phone number", "Call measurement"],
           "distribution": [{"@type": "DataDownload", "encodingFormat": "text/csv", "contentUrl": "https://ppcconsultancy.uk/data/uk-google-ads-measurement-2026-11.csv"}]}
P = {
 "slug": "google-ads-advertisers-measurement-uk",
 "short": "Study: what UK advertisers measure",
 "blurb": f"We read the sites of {N} UK businesses with live Google Ads in 15 sectors. {o['conv']}% show a conversion tag. {o['nothing']}% measure nothing.",
 "title": f"What {N} UK Businesses Paying for Google Ads Measure, by Sector",
 "meta": f"We read the sites of {N} UK businesses with live Google Ads in 15 service sectors. {o['conv']}% show a Google Ads conversion tag. {o['nothing']}% show no measurement at all.",
 "kicker": "Study",
 "h1": f"What {N} UK businesses paying for Google Ads actually measure, sector by sector",
 "lead": (f"Of {N} UK businesses with live Google Ads in 15 service sectors, {o['conv']}% show a Google Ads conversion tag on their site, {o['ga_only']}% count visits with Google Analytics and show no Google Ads tag at all, "
          f"and {o['nothing']}% show no measurement of any kind. Four in five publish a clickable phone number, and just over half of those have nothing in place to count the call. These companies are paying for clicks today. A large share cannot tell which click became a customer."),
 "body": body, "faq": faq, "messages": [],
 "sources": ["https://adstransparency.google.com/?region=GB", "https://support.google.com/google-ads/answer/1722022?hl=en-GB", "https://support.google.com/google-ads/answer/10000067?hl=en-GB"],
 "related": ["conversion-tracking", "ppc-audit", "google-ads-management"],
 "jsonld_extra": '<script type="application/ld+json">' + json.dumps(dataset) + "</script>",
}
assert o["tel"] in (79, 80, 81) and 50 < o["call_not_measured_of_tel"] < 56, "lead wording (four in five / just over half) no longer matches the data"
out = ("# Study page generated by research/uk-advertiser-study-2026-11/make_page.py on 2026-11-13 from summary.json.\n"
       "# British English. Every figure is a count over the sites read. Do not edit the numbers by hand: rerun the generator.\nP = " + json.dumps(P, indent=1, ensure_ascii=False) + "\n")
open(os.path.join(SITE_DIR, "guides_src", "google-ads-advertisers-measurement-uk.py"), "w", encoding="utf-8").write(out)
os.makedirs(os.path.join(SITE_DIR, "assets", "data"), exist_ok=True)
with open(os.path.join(SITE_DIR, "assets", "data", "uk-google-ads-measurement-2026-11.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    cols = [("n", "sites_read"), ("conv", "google_ads_conversion_tag_pct"), ("ads_tag_no_conv", "google_ads_tag_no_conversion_seen_pct"), ("ga_only", "analytics_only_pct"),
            ("other_only", "other_tags_only_pct"), ("hidden", "tag_signs_not_readable_pct"), ("nothing", "no_measurement_pct"), ("ads_tag", "any_google_ads_tag_pct"), ("ga4", "google_analytics_or_google_tag_pct"),
            ("gtm", "tag_manager_pct"), ("meta", "meta_pixel_pct"), ("uet", "microsoft_advertising_tag_pct"), ("banner", "consent_banner_pct"), ("tel", "clickable_phone_pct"),
            ("n_tel", "sites_with_clickable_phone"), ("call_measured_of_tel", "calls_measured_pct_of_sites_with_phone"), ("form", "enquiry_form_pct")]
    w.writerow(["sector"] + [c[1] for c in cols])
    for s, b in sorted(sec.items()): w.writerow([s] + [b[c[0]] for c in cols])
    w.writerow(["All sectors"] + [o[c[0]] for c in cols])
    w.writerow([]); w.writerow(["Source: ppcconsultancy.uk/guides/google-ads-advertisers-measurement-uk/ . Sites read on 13 November 2026. Free to quote with a link."])
print("written", N, "sites;", len(best), "best-measured;", "title", len(P["title"]), "meta", len(P["meta"]))
