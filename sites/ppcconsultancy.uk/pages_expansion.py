# Pages added in October 2026 from the page expansion study (research/estudo-paginas-2026-10-06.md):
# services the US site already had, sector pages and city pages. UK spelling throughout. No prices, no claims
# beyond the published cases on /results/.

CITY_CPC = {  # Google Ads keyword data, UK, October 2026: average CPC in pounds for the search with the city attached
    "London":     {"solicitors": 13.49, "employment lawyer": 18.60, "accountants": 12.55, "IT support": 37.70, "financial advisor": 20.43, "web design": 12.05},
    "Manchester": {"solicitors": 9.46,  "employment lawyer": 10.95, "accountants": 12.21, "IT support": 16.03, "financial advisor": 15.93, "web design": 13.97},
    "Birmingham": {"solicitors": 9.31,  "employment lawyer": 10.92, "accountants": 10.53, "IT support": 11.49, "financial advisor": 20.38, "web design": 20.01},
    "Leeds":      {"solicitors": 7.09,  "employment lawyer": 9.99,  "accountants": 8.80,  "IT support": 26.67, "financial advisor": 19.07, "web design": 9.15},
    "Bristol":    {"solicitors": 7.97,  "employment lawyer": 11.72, "accountants": 14.11, "IT support": 20.85, "financial advisor": 23.98, "web design": 9.08},
}


def cpc_table(city):
    others = [c for c in ("London", "Manchester", "Birmingham", "Leeds", "Bristol") if c != city][:3]
    cols = [city] + others
    head = "".join(f"<th>{c}</th>" for c in cols)
    rows = ""
    for search in CITY_CPC[city]:
        cells = "".join(f"<td>£{CITY_CPC[c][search]:.2f}</td>" for c in cols)
        rows += f"<tr><td>{search} [city]</td>{cells}</tr>\n"
    return f"<table>\n<tr><th>Search</th>{head}</tr>\n{rows}</table>"


def city_page(slug, city, kicker_city, intro, sectors, cpc_comment, faq_extra, local_note):
    return {
        "slug": slug, "short": f"PPC consultant, {city}", "blurb": f"For {city} businesses, delivered remotely on UK hours.",
        "title": f"PPC Consultant {city} | Independent PPC Management, No Agency Layer",
        "meta": f"Independent PPC consultant for {city} businesses: Google, Microsoft, Meta and LinkedIn Ads run by one senior consultant on UK hours. Flat monthly fee, no agency layer.",
        "kicker": f"PPC consultant {kicker_city}",
        "h1": f"PPC consultant for {city} businesses, working remotely on your hours",
        "lead": f"Independent PPC consultant for {city} firms: 14+ years running Google, Microsoft, Meta and LinkedIn Ads, calls on UK time, everything in writing, and a fee that does not carry an office inside it.",
        "service_name": f"PPC consultancy for {city} businesses",
        "body": f"""
<section><div class="wrap">
<h2>What {city} accounts usually need</h2>
{intro}
<ul>
<li><strong>Location targeting that matches how you actually serve.</strong> A radius around the office for the work that needs a visit, the wider region for the work that does not, and the two bid separately instead of one pin on the city centre.</li>
<li><strong>Enquiry quality over enquiry count.</strong> Call tracking tied to the keyword, form fields that qualify, and CRM stages fed back to Google and LinkedIn so bidding learns from clients, not from clicks.</li>
<li><strong>A landing page per intent.</strong> Not the homepage, and not one generic contact page for twelve services.</li>
<li><strong>Brand and competitor terms handled deliberately.</strong> Whether to bid on your own name depends on who else is bidding on it in {city} this month, and the answer changes.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>What a click costs in {city} compared with other UK cities</h2>
<p>Average cost per click for the same search with the city name attached, from Google Ads keyword data for the UK, October 2026. Market averages, not a forecast for your account.</p>
{cpc_table(city)}
{cpc_comment}
</div></section>

<section><div class="wrap">
<h2>{city} sectors where this work is already familiar</h2>
<div class="cols">
{sectors}
</div>
</div></section>

<section><div class="wrap">
<h2>What a published result looks like in {city} terms</h2>
<p>There is no {city} case study on this site yet, and none will be invented. What can be shown is how a published engagement would translate. The <a href="/results/">Houston home services account</a> cut cost per acquisition by 44% and lifted qualified leads by 60% in an auction where clicks cost US$45 to US$80. What moved it was not a bidding trick:</p>
<ul>
<li>Campaigns split by type of job, so urgent, cheaper work stopped absorbing the budget meant for higher-value jobs.</li>
<li>Tracking rebuilt so a booked job and a phone call were different events.</li>
<li>A weekly pass through the search terms and steady tests of adverts and landing pages.</li>
</ul>
{local_note}
</div></section>

<section><div class="wrap">
<h2>Consultant or {city} agency</h2>
<table>
<tr><th></th><th>Independent consultant</th><th>{city} PPC agency</th></tr>
<tr><td>Who does the work</td><td>The person you spoke to first</td><td>An account team, often led by someone junior once the pitch is over</td></tr>
<tr><td>How it is charged</td><td>Flat monthly fee, never a share of spend</td><td>Retainer or a percentage of spend</td></tr>
<tr><td>Minimum term</td><td>None; 30 days' notice</td><td>Commonly 6 to 12 months</td></tr>
<tr><td>Landing pages and tracking</td><td>Included, by the same person</td><td>Often another team or an extra</td></tr>
<tr><td>Meetings</td><td>Remote, calls on UK time, written updates</td><td>In person if you want them</td></tr>
<tr><td>Better when</td><td>One business, one senior person accountable</td><td>Many markets, heavy creative or regular face-to-face</td></tr>
</table>
<p>The full comparison is on <a href="/agency-vs-consultant/">PPC agency vs PPC consultant</a>. Engagements start with a fixed-price <a href="/ppc-audit/">PPC audit</a> or, for a new account, a setup; either is credited against the first month of <a href="/ppc-management/">management</a>.</p>
</div></section>
""",
        "faq": [
            (f"Do you meet clients in {city}?", "The engagement is remote as standard: calls on UK time and written updates. If regular face-to-face meetings matter to you, an agency with a local office will suit you better, and I would rather say so at the start."),
            (f"Do you work with businesses outside {city}?", f"Yes, across the UK and Ireland. This page exists because {city} businesses search for a {city} consultant; the service and the terms are the same everywhere."),
            (f"What do {city} PPC agencies and consultants charge?", "Senior UK freelancers commonly quote a few hundred pounds a day or a flat monthly retainer; agencies commonly charge a percentage of spend with a monthly minimum. My fee is flat, set from the scope of the account, and quoted in pounds, ex VAT, from the form. See <a href=\"/pricing/\">pricing</a>."),
        ] + faq_extra,
        "related": ["ppc-management", "ppc-audit", "agency-vs-consultant", "ppc-consultant-london"],
    }


PAGES = [

# ---------------------------------------------------------------- Google Ads consultant
{
"slug": "google-ads-consultant", "short": "Google Ads consultant", "blurb": "Strategy, a second opinion or a full review of the account, from the person who would run it.",
"title": "Google Ads Consultant UK | Independent, 14+ Years on the Account",
"meta": "Independent Google Ads consultant for UK businesses: account reviews, strategy and hands-on fixes from one senior specialist, not an agency team. Quoted in pounds.",
"kicker": "Google Ads consultant",
"h1": "A Google Ads consultant who has run accounts for 14+ years, hired directly instead of through an agency",
"lead": "Consulting for UK businesses that want a senior person to look at the Google Ads account, say what is wrong in writing and fix it, or to stay on as the person running it. One consultant, no handover to a junior.",
"service_name": "Google Ads consulting",
"body": """
<section><div class="wrap">
<h2>Three reasons UK businesses hire a Google Ads consultant</h2>
<div class="cols">
<div class="card"><h3>The account is not converting and nobody can say why</h3><p>Spend is steady, the agency report is green, and the sales team says the enquiries are poor. A consultant reads the account from the search terms up and puts the cause in writing, with a figure next to each item.</p></div>
<div class="card"><h3>A decision needs a second opinion</h3><p>Whether to move to Performance Max, whether to bid on the brand, whether the agency's proposed budget increase is justified. An independent view from someone who has no retainer to win by agreeing.</p></div>
<div class="card"><h3>The in-house marketer needs a senior pair of hands</h3><p>A marketing manager who runs Google Ads among ten other things, and wants a specialist to set the structure, fix the tracking and check the work monthly.</p></div>
</div>
</div></section>

<section><div class="wrap">
<h2>How the consulting works</h2>
<ol class="steps">
<li><div><strong>Read-only access first.</strong> Google Ads, GA4 and Tag Manager. Nothing is changed until you have the findings and have agreed what to do.</div></li>
<li><div><strong>A written review.</strong> Findings ranked by financial impact: measurement, search terms, structure, automation, adverts and landing pages. Each with the fix, who should do it and how to confirm it worked. This is the <a href="/ppc-audit/">PPC audit</a>, priced fixed and in advance.</div></li>
<li><div><strong>Then one of three paths.</strong> Your team or agency implements the report; I implement the fixes as a fixed-price project; or I take the account on month to month as the person running it. Many clients choose the first and come back for the third.</div></li>
<li><div><strong>Ongoing advisory where it fits.</strong> A monthly review of the work your team does, with a written note and a call. For in-house teams that want supervision rather than outsourcing. For a single question or decision, a one-off <a href="/ppc-consultation/">PPC consultation</a> is the smaller option.</div></li>
</ol>
</div></section>

<section><div class="wrap">
<h2>What the review looks at, in order</h2>
<ul>
<li><strong>Measurement.</strong> Conversion actions, GA4 events, Consent Mode v2, the CRM. If an enquiry and a phone click are counted the same, every decision downstream is wrong.</li>
<li><strong>Search terms.</strong> Twelve months read against the negatives that exist. In most UK lead generation accounts this is where the largest number sits.</li>
<li><strong>Structure.</strong> Whether campaigns follow margin, service line and intent, or follow whoever built them.</li>
<li><strong>Automation.</strong> What Smart Bidding and Performance Max are actually doing, and whether the reported results survive excluding the brand.</li>
<li><strong>Adverts and pages.</strong> Message match, the form, the phone number, the speed on a mobile connection.</li>
</ul>
<p>The method is the same one applied in <a href="/google-ads-management/">Google Ads management</a>, which is why the review is credited against the first month if management follows.</p>
</div></section>

<section><div class="wrap">
<h2>Consultant, agency or freelancer</h2>
<p>The words overlap and UK businesses search for all three. The useful distinction is who touches the account. An agency puts a team between you and the work; a consultant or <a href="/ppc-freelancer/">freelancer</a> is the person doing it. Within that, "consultant" usually means advice and reviews are available on their own, without a retainer, which is the case here. The comparison with agencies is on <a href="/agency-vs-consultant/">PPC agency vs PPC consultant</a>.</p>
</div></section>
""",
"faq": [
("What does a Google Ads consultant cost in the UK?", "Reviews are a fixed price set from monthly spend, number of campaigns and platforms in scope, quoted in pounds ex VAT by email from the form. Ongoing management is a flat monthly fee set by scope, never a percentage of spend. See <a href=\"/pricing/\">pricing</a>."),
("Can you consult without taking over the account?", "Yes. The written review and the implementation plan stand on their own, and many are carried out by the client's team or existing agency. There is no obligation to hire me afterwards."),
("Do you work with our existing agency?", "Yes, and in writing. A fair review that says the agency is competent and lists the three remaining gains is still useful. I have no retainer to win by criticising them."),
("Which platforms do you cover?", "Google Ads (Search, Shopping, Performance Max, YouTube, Demand Gen), Microsoft Advertising, Meta Ads and LinkedIn Ads, plus GA4, Tag Manager and the landing pages that sit under all of them."),
("Do you take calls on UK hours?", "Yes. I work remotely from Curitiba, Brazil, three to four hours behind the UK, so calls fit a UK afternoon. Everything agreed is confirmed in writing."),
("Are you Google Partner certified?", "Certifications are not the point of hiring a consultant and the badge is earned by spend thresholds as much as by skill. What you can check is the written review, the <a href=\"/results/\">published cases</a> and the way the first call goes."),
],
"related": ["ppc-audit", "google-ads-management", "ppc-freelancer", "agency-vs-consultant"],
},

# ---------------------------------------------------------------- E-commerce PPC
{
"slug": "ecommerce-ppc", "short": "E-commerce PPC", "blurb": "Shopping, Performance Max and Meta for online stores, measured on margin and new customers.",
"title": "Ecommerce PPC Agency Alternative UK | Shopping & Performance Max by One Consultant",
"meta": "E-commerce PPC for UK online stores: Google Shopping, Merchant Centre feeds, Performance Max and Meta run by one senior consultant, judged on margin rather than platform ROAS.",
"kicker": "E-commerce PPC",
"h1": "E-commerce PPC that reports margin and new customers, not the ROAS the platform awards itself",
"lead": "Google Shopping, Performance Max, Search and Meta for UK online stores, run by one consultant who reconciles platform-reported revenue against the store's own orders every month. Flat fee, no percentage of spend.",
"service_name": "E-commerce PPC management",
"body": """
<section><div class="wrap">
<h2>Why e-commerce PPC reports look better than the bank account</h2>
<ul>
<li><strong>ROAS counts the brand.</strong> Performance Max and Shopping take credit for people who searched the store's name and would have bought anyway. Exclude the brand and the number often halves.</li>
<li><strong>Returning customers are counted as wins.</strong> A repeat buyer who clicked an advert is revenue the store already had. New-customer and returning-customer revenue are separated here, and the bid strategy is set on the first.</li>
<li><strong>Revenue is not margin.</strong> A 600% ROAS on a product with 20% margin loses money after the click cost. Campaigns are grouped by margin band, and the targets differ by band.</li>
<li><strong>The feed is left to the platform.</strong> Titles written for the warehouse, missing GTINs, no custom labels for margin or stock. The feed decides which auctions you enter; it is the first thing fixed.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>What management includes</h2>
<ol class="steps">
<li><div><strong>Feed first.</strong> Merchant Centre diagnostics cleared, titles rewritten around how people search, GTINs and product types completed, custom labels for margin, stock and seasonality. Supplemental feeds where the platform cannot do it.</div></li>
<li><div><strong>Shopping and Performance Max by margin band.</strong> Standard Shopping where control matters, Performance Max where volume does, brand excluded in both so the reported return is real. Asset groups built per category, not one for the whole store.</div></li>
<li><div><strong>Search for the intent Shopping misses.</strong> Category and problem searches, with negatives maintained weekly and brand kept in its own campaign with its own budget.</div></li>
<li><div><strong>Meta for new customers.</strong> Catalogue and prospecting campaigns with the Conversions API, judged on new-customer orders from the store's own data, not on the platform's view-through revenue.</div></li>
<li><div><strong>Measurement reconciled monthly.</strong> GA4, Google Ads and Meta compared with the order export. The report shows platform revenue, store revenue, new versus returning customers and contribution after ad cost. See <a href="/conversion-tracking/">conversion tracking</a>.</div></li>
</ol>
</div></section>

<section><div class="wrap">
<h2>Who this fits</h2>
<p>UK and Irish stores spending roughly £3,000 to £60,000 a month on a catalogue of a few hundred to a few thousand products, on Shopify, WooCommerce, Magento or BigCommerce. Owners and e-commerce managers who want one accountable person and a report they can reconcile themselves.</p>
<p>Stores with tens of thousands of products and daily feed operations are agency work: the feed alone is a full-time job, and I will say so at the first call rather than run it half well. Marketplaces (Amazon Ads) are not offered.</p>
</div></section>

<section><div class="wrap">
<h2>How an e-commerce engagement starts</h2>
<p>With a fixed-price <a href="/ppc-audit/">audit</a> of the account and the feed, which puts a pound figure on brand inflation, returning-customer spend and feed gaps before anything is changed. The audit fee is credited against the first month of <a href="/ppc-management/">management</a>. Quoted in pounds, ex VAT, from the form.</p>
</div></section>
""",
"faq": [
("Do you do Google Shopping and Performance Max?", "Yes. Standard Shopping, Performance Max and Search, with Merchant Centre and the feed managed as part of the work, measured on margin and new customers rather than on the platform's own ROAS."),
("Can you work with our Shopify or WooCommerce store?", "Yes. The feed comes from the platform's channel or from a feed tool, GA4 and the Conversions API are set up through Tag Manager, and the order export is what the monthly numbers are reconciled against."),
("What ROAS should we expect?", "No honest number exists before the audit. What I can promise is that the figure reported will be the one the store's own orders support, with brand and returning customers shown separately, so you can set the target from margin."),
("Do you run Amazon Ads?", "No. Marketplaces are a separate discipline and a different account structure. Google, Microsoft and Meta for your own store are what this covers."),
("How much does e-commerce PPC management cost?", "A flat monthly fee set by scope: number of platforms, size of the catalogue and how much feed and landing page work is included. Never a percentage of spend or of revenue. Quoted in pounds, ex VAT. See <a href=\"/pricing/\">pricing</a>."),
],
"related": ["ppc-management", "ppc-audit", "conversion-tracking", "facebook-ads-management"],
},

# ---------------------------------------------------------------- LinkedIn Ads
{
"slug": "linkedin-ads-management", "short": "LinkedIn Ads management", "blurb": "B2B campaigns judged on pipeline, not on clicks at £10 each.",
"title": "LinkedIn Ads Management UK | B2B Campaigns Measured in Pipeline",
"meta": "LinkedIn Ads management by an independent B2B consultant in the UK: account targeting, offer-led creative and CRM-connected measurement, for a flat monthly fee.",
"kicker": "LinkedIn Ads",
"h1": "LinkedIn Ads management for UK companies that need pipeline, not impressions among the right job titles",
"lead": "LinkedIn is the only platform where a buying committee can be named by title, seniority, company size and industry. It is also the most expensive click in paid media, which means the offer, the measurement and the follow-up matter more than anywhere else.",
"service_name": "LinkedIn Ads management",
"body": """
<section><div class="wrap">
<h2>Where LinkedIn Ads budgets go wrong</h2>
<p>The targeting is so precise that it hides the real problem: a £10 click on a decision-maker who downloads a whitepaper and never speaks to sales is still £10 spent on nothing. Most LinkedIn accounts I review report hundreds of leads and a sales team that cannot find one worth calling. Three causes recur.</p>
<ul>
<li><strong>The offer is a PDF.</strong> Gated content generates form fills from people doing research, not people buying. The offer has to be something a buyer with a problem would want this quarter.</li>
<li><strong>Measurement stops at the form.</strong> Without lead stages flowing back from the CRM, LinkedIn optimises towards the cheapest form fill, which is the least qualified one.</li>
<li><strong>Audiences too broad or too narrow.</strong> Broad enough to spend, narrow enough to matter: usually a named account list or a tight firmographic definition, layered with title or function, with exclusions for current customers, competitors and your own staff.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>What management includes</h2>
<ol class="steps">
<li><div><strong>Audience architecture.</strong> Account lists from your CRM and intent data where you have it, firmographic and title definitions for the rest, exclusions maintained, matched audiences refreshed monthly.</div></li>
<li><div><strong>Offer and creative.</strong> Offers built for a buyer with a problem: assessments, benchmarks, working sessions, product-led demos. Document ads, single image, video and conversation ads tested against each other with a proper control.</div></li>
<li><div><strong>Measurement to pipeline.</strong> Insight Tag and Conversions API, lead gen forms or landing pages pushed into HubSpot, Salesforce or Pipedrive with campaign data attached, offline conversions uploaded so LinkedIn optimises towards qualified opportunities. See <a href="/conversion-tracking/">conversion tracking</a>.</div></li>
<li><div><strong>Bidding and frequency.</strong> Manual bidding where the account is small, cost-cap where there is volume, frequency watched so the same 400 people are not shown the same advert nine times a week.</div></li>
<li><div><strong>Reporting in pipeline.</strong> Cost per qualified opportunity and pipeline created, alongside Google and Microsoft in the same report, so the expensive click is judged on what it produced.</div></li>
</ol>
</div></section>

<section><div class="wrap">
<h2>LinkedIn next to Google and Microsoft</h2>
<p>For UK B2B accounts LinkedIn creates the demand, Google and <a href="/microsoft-ads-management/">Microsoft</a> capture it when the buyer searches, and LinkedIn remarketing keeps the account warm through a long cycle. Run by one person, the attribution argument disappears and budget follows measured pipeline. That is the case for <a href="/b2b-ppc/">B2B PPC</a> as one engagement rather than three vendors.</p>
</div></section>

<section><div class="wrap">
<h2>Who this fits</h2>
<p>UK and Irish B2B companies with a deal size that justifies a click costing several pounds: SaaS, professional and financial services, industrial and technical suppliers, consultancies. Usually £3,000 a month or more on LinkedIn alone, with Google alongside. Below that, LinkedIn remarketing on a Google account is often the better first step, and I will say so.</p>
</div></section>
""",
"faq": [
("How much does LinkedIn Ads management cost?", "A flat monthly fee set by scope, not by spend; typically similar to a Google Ads retainer of the same complexity. A fixed-price audit comes first for existing accounts. Quoted in pounds, ex VAT. See <a href=\"/pricing/\">pricing</a>."),
("What is a realistic cost per lead on LinkedIn in the UK?", "For gated content, tens of pounds and mostly unqualified. For a demo or assessment request from a named account, a few hundred pounds is common and often worth it. The number that matters is cost per qualified opportunity, and it only exists once the CRM is connected."),
("Can you run LinkedIn without Google Ads?", "Yes, though for most B2B accounts the two work better together: LinkedIn builds the audience and Google catches it when it searches. Both are covered in the same report either way."),
("Do you write the adverts and make the creative?", "I write the copy and brief the creative; a designer on your side or a studio produces the volume. Document ads and conversation ads are usually built by me directly."),
("Which CRMs can you connect?", "HubSpot, Salesforce, Pipedrive and most others with an API or a native LinkedIn integration. Where there is no integration, a scheduled offline conversion upload does the same job."),
],
"related": ["b2b-ppc", "ppc-management", "conversion-tracking", "microsoft-ads-management"],
},

# ---------------------------------------------------------------- Facebook / Meta Ads
{
"slug": "facebook-ads-management", "short": "Facebook Ads management", "blurb": "Facebook and Instagram ads run by one specialist, measured against the CRM or the store's orders.",
"title": "Facebook Ads Management UK | Meta Ads by an Independent Specialist",
"meta": "Facebook and Instagram ads for UK businesses run by one independent specialist: Conversions API, structured creative tests and results measured in the CRM or the store's orders. Flat fee.",
"kicker": "Facebook and Instagram Ads",
"h1": "Facebook Ads management by a specialist who also runs your Google Ads, so the two are judged on the same numbers",
"lead": "Meta campaigns for UK businesses that sell through enquiries and for online stores: Pixel plus Conversions API, deduplicated; creative tests on a schedule with one control; and lead quality or new-customer orders as the number reported, not the platform's own attribution.",
"service_name": "Facebook and Instagram Ads management",
"body": """
<section><div class="wrap">
<h2>Why Meta accounts disappoint in the UK</h2>
<ul>
<li><strong>Measurement broke in 2021 and was never repaired.</strong> Without the Conversions API, Meta sees a fraction of the outcomes and optimises towards the people it can still see. The first week of any engagement is tracking.</li>
<li><strong>Lead forms that produce leads nobody can reach.</strong> Instant forms with every field pre-filled generate volume at a low cost per lead and a sales team that stops answering them. Qualifying questions and a CRM connection fix most of it.</li>
<li><strong>Creative treated as a one-off.</strong> Three adverts launched in January and still running in June. Meta rewards fresh creative, and the only way to produce winners on purpose is a test schedule with a control.</li>
<li><strong>Attribution taken at face value.</strong> Seven-day click plus one-day view flatters every campaign. The report here uses the CRM or the order export, and the platform number is shown next to it for comparison.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>What management includes</h2>
<ol class="steps">
<li><div><strong>Tracking.</strong> Pixel and Conversions API through Tag Manager (server-side where the volume justifies it), events deduplicated, Consent Mode v2 for UK visitors, and the CRM or the store feeding outcomes back. See <a href="/conversion-tracking/">conversion tracking</a>.</div></li>
<li><div><strong>Structure.</strong> Few campaigns with enough budget to learn, broad or Advantage+ audiences where the signal is clean, interest and lookalike audiences where it is not yet, remarketing kept separate so it does not take the credit for everything.</div></li>
<li><div><strong>Creative programme.</strong> A monthly brief with hooks, formats and angles to test, produced by your designer or a studio, launched against one control, with winners scaled and losers retired on a schedule.</div></li>
<li><div><strong>Lead quality or orders.</strong> For lead generation, qualifying questions on the form and CRM stages fed back so Meta optimises towards sales-accepted leads. For stores, catalogue campaigns judged on new-customer orders from the store's data.</div></li>
<li><div><strong>One report with Google.</strong> Meta, Google and Microsoft in the same document, in pounds, with the same definition of a conversion across all three.</div></li>
</ol>
</div></section>

<section><div class="wrap">
<h2>Lead generation and e-commerce, handled differently</h2>
<div class="cols">
<div class="card"><h3>Lead generation</h3><p>Home and trade services, private healthcare, education, financial and professional services where the offer can be understood in a feed. The cost per qualified lead from the CRM is the number, and the creative is built around the problem the customer has today. <a href="/ppc-management/">PPC management →</a></p></div>
<div class="card"><h3>Online stores</h3><p>Catalogue and prospecting campaigns for new customers, remarketing for the rest, with platform-reported revenue reconciled against the store's own orders every month. <a href="/ecommerce-ppc/">E-commerce PPC →</a></p></div>
</div>
</div></section>
""",
"faq": [
("How much does Facebook Ads management cost in the UK?", "A flat monthly fee set by scope, never a percentage of spend. Most Meta accounts are run alongside a Google account under one fee. Quoted in pounds, ex VAT. See <a href=\"/pricing/\">pricing</a>."),
("Do you produce the creative?", "I write the copy, brief the angles and formats, and run the tests. Image and video production comes from your designer or a studio; I can recommend one."),
("Can you run Meta without Google Ads?", "Yes, though for most UK businesses the two are better run together: Meta creates demand and Google catches the search it produces, and one person judging both removes the attribution argument."),
("What budget does Meta need to work?", "Enough for the campaigns to leave the learning phase: in practice a few thousand pounds a month for lead generation, more for stores with a large catalogue. Below that, the money usually works harder on Search."),
("Do you handle Consent Mode and the Conversions API?", "Yes. Both are part of the setup, through Tag Manager, with the same definitions used for Google and LinkedIn."),
],
"related": ["ppc-management", "ecommerce-ppc", "conversion-tracking", "google-ads-management"],
},

# ---------------------------------------------------------------- Microsoft Ads
{
"slug": "microsoft-ads-management", "short": "Microsoft Ads management", "blurb": "Bing Ads managed natively, not left as a stale import of the Google account.",
"title": "Microsoft Advertising Management UK | Bing Ads Managed Properly",
"meta": "Microsoft Advertising (Bing Ads) management for UK businesses by an independent consultant: imported from Google, then run natively with its own negatives, bids and tracking.",
"kicker": "Microsoft Advertising",
"h1": "Microsoft Advertising management: the cheaper click most UK accounts import once and forget",
"lead": "Bing, Yahoo, DuckDuckGo, Copilot and the Microsoft partner network reach a UK audience that skews older, professional and on a work laptop. In the accounts I have run, the same conversion has often cost noticeably less there than on Google. The catch is that it has to be managed, not just imported.",
"service_name": "Microsoft Advertising management",
"body": """
<section><div class="wrap">
<h2>What goes wrong with imported accounts</h2>
<ul>
<li><strong>The import runs on a schedule and nobody looks.</strong> Google changes are copied across, including the ones that only make sense on Google. Microsoft's auction, audience and search partners are different enough to need their own negatives and bids.</li>
<li><strong>Search partners left on by default.</strong> Syndicated traffic that converts poorly and absorbs budget. One of the first settings reviewed.</li>
<li><strong>UET tag missing or counting the wrong thing.</strong> Conversions imported from Google Ads or GA4 arrive late and incomplete. The UET tag through Tag Manager, with the same conversion definitions as Google, is the fix.</li>
<li><strong>Performance Max and Shopping copied without review.</strong> Microsoft's equivalents behave differently and often deserve a different budget share.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>What management includes</h2>
<ol class="steps">
<li><div><strong>Import, then diverge.</strong> The Google structure as a starting point, then Microsoft-specific negatives, bids, schedules and audience adjustments maintained natively, with the automatic import limited to what should stay in sync.</div></li>
<li><div><strong>Tracking.</strong> UET via Tag Manager, enhanced conversions, offline conversion import where the CRM allows it, so Microsoft optimises on the same outcomes as Google. See <a href="/conversion-tracking/">conversion tracking</a>.</div></li>
<li><div><strong>LinkedIn profile targeting.</strong> Microsoft's search campaigns can adjust bids by company, industry and job function from LinkedIn data. For B2B accounts this is often the strongest reason to be there. See <a href="/b2b-ppc/">B2B PPC</a>.</div></li>
<li><div><strong>Weekly search term review</strong> and monthly reporting alongside Google, in pounds, with the cost per conversion of each platform side by side so the budget split follows the numbers.</div></li>
</ol>
</div></section>

<section><div class="wrap">
<h2>Who this fits</h2>
<p>UK businesses already spending on Google Search with conversion tracking that works. Microsoft is usually an add-on to a <a href="/google-ads-management/">Google Ads retainer</a> rather than a standalone engagement, because the volume is a fraction of Google's and the economics are better when one person runs both. B2B, professional services and higher-value home services tend to see the largest gap in cost per conversion.</p>
</div></section>
""",
"faq": [
("Is Bing Ads worth it in the UK?", "For most accounts with working Google Search campaigns, yes, as an add-on: the volume is smaller but the cost per conversion is often lower, and the audience skews towards professionals on work devices. It is rarely worth running on its own."),
("How much does Microsoft Advertising management cost?", "As an add-on to a Google retainer, a modest increase to the flat monthly fee, set by the extra scope. Quoted in pounds, ex VAT. See <a href=\"/pricing/\">pricing</a>."),
("Can you just import our Google account?", "The import is the starting point, not the service. The value is in what is changed afterwards: negatives, search partners, bids, tracking and the LinkedIn profile adjustments Google cannot offer."),
("Do Microsoft Ads show on ChatGPT or Copilot?", "Copilot and Bing's AI answers carry Microsoft Advertising placements; other assistants have their own programmes. Placements change often, and the monthly report shows what each one produced."),
],
"related": ["google-ads-management", "ppc-management", "b2b-ppc", "conversion-tracking"],
},

# ---------------------------------------------------------------- Small business
{
"slug": "google-ads-small-business", "short": "Google Ads for small business", "blurb": "Right-sized Google Ads for small UK companies: a setup you run yourself, an audit, or lean management.",
"title": "Google Ads for Small Business UK | PPC Sized to the Budget",
"meta": "Google Ads for small businesses in the UK: a fixed-price setup you run yourself, an honest audit, or lean flat-fee management by one senior consultant. No percentage of spend.",
"kicker": "Small business PPC",
"h1": "Google Ads for small businesses, sized to the budget instead of to an agency minimum",
"lead": "Most UK agencies will not take an account under a few thousand pounds a month, and the ones that do assign it to the newest hire. This is the alternative: a senior consultant, a service matched to the spend, and a fee that is a flat number rather than a share of your budget.",
"service_name": "Google Ads for small business",
"body": """
<section><div class="wrap">
<h2>Why small business Google Ads accounts underperform</h2>
<ul>
<li><strong>Built from the Google wizard.</strong> Smart campaigns, broad match and location targeting set to the whole country produce clicks from people who will never be customers. The account spends; the phone does not ring.</li>
<li><strong>No conversion tracking, or the wrong kind.</strong> A phone click counted as a lead, a form thank-you page nobody set up, and Google optimising towards whatever it can measure, which is nothing useful.</li>
<li><strong>Nobody reads the search terms.</strong> In a small account, a few bad searches can take half the month's budget. A weekly ten-minute pass through the search terms report is the highest-return task in Google Ads, and it is the one skipped first.</li>
<li><strong>The agency fee eats the budget.</strong> A percentage of spend with a monthly minimum means a £1,500 budget can carry a £500 fee for a junior's attention.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>Three ways to buy this, by budget</h2>
<table>
<tr><th>Monthly ad spend</th><th>What usually makes sense</th><th>What you get</th></tr>
<tr><td>Under £2,000</td><td>A fixed-price setup you run yourself</td><td>Structure, conversion tracking, negatives and a landing page check built in your own account, with a written handover and a short call on what to look at each week.</td></tr>
<tr><td>£1,000 to £3,000 with an existing account</td><td>A fixed-price <a href="/ppc-audit/">audit</a></td><td>What is wasting money, with a pound figure, and the fixes in order. Implemented by you, or by me as a project.</td></tr>
<tr><td>Over £2,000</td><td>Lean monthly management</td><td>Weekly work in the account, a written monthly report, a call when you want one, landing page and tracking fixes included. Month to month, 30 days' notice either way.</td></tr>
</table>
<p>Every option is a fixed or flat price in pounds, ex VAT, quoted by email from the form. Never a percentage of spend. <a href="/pricing/">How I price →</a></p>
</div></section>

<section><div class="wrap">
<h2>What local PPC management focuses on</h2>
<div class="cols">
<div class="card"><h3>Service area, not the whole country</h3><p>Radius and postcode targeting matched to where you actually go, with bids by area and hour, and the searches from outside it excluded.</p></div>
<div class="card"><h3>Calls that are counted properly</h3><p>Call tracking that separates a booked job from a wrong number, so Google learns from real customers. The Google Business Profile linked, with location assets and local service ads reviewed where they apply.</p></div>
<div class="card"><h3>One page per service</h3><p>A landing page for the service someone searched for, with the phone number at the top and a form that works on a mobile. Not the homepage.</p></div>
<div class="card"><h3>Microsoft as a cheap second channel</h3><p>Once Google works, the same structure on <a href="/microsoft-ads-management/">Microsoft Advertising</a> often brings the same enquiry for less.</p></div>
</div>
</div></section>

<section><div class="wrap">
<h2>The proof, at small-business scale</h2>
<p>The published <a href="/results/">Houston home services case</a> ran on a larger budget, but what moved it applies at any size: campaigns split by job type, tracking that separates a booked job from a call, and a weekly pass through the search terms. A small account has the same levers and less room for the fee.</p>
</div></section>
""",
"faq": [
("What is the minimum budget for Google Ads to work for a small business?", "Enough to buy a meaningful number of clicks at your local cost per click. For many UK trades and local services that is £1,000 to £2,000 a month; for solicitors or IT support in a large city it is more, because the clicks cost more. The setup call includes this arithmetic for your market."),
("Do you take small accounts?", "Yes, with the service matched to the spend: a setup you run yourself, an audit, or lean management. What I will not do is take a small account and give it a junior's attention."),
("How much does Google Ads management cost for a small business?", "A flat monthly fee set from the scope, not from spend, quoted in pounds ex VAT from the form. For the smallest accounts a one-off setup is usually the better buy than a retainer. See <a href=\"/pricing/\">pricing</a>."),
("Can you set it up and then let me run it?", "Yes. That is the setup option: built in your own account, handed over in writing, with a short call on what to check each week. If you later want management, the setup fee is credited against the first month."),
("Do you work with sole traders and limited companies?", "Both. The engagement is a short services agreement in pounds, 30 days' notice either way, and everything built belongs to you."),
],
"related": ["ppc-audit", "google-ads-management", "landing-pages", "pricing"],
},

# ---------------------------------------------------------------- PPC specialist / expert
{
"slug": "ppc-specialist", "short": "PPC specialist", "blurb": "A senior specialist on the account, not an agency team: what that means in practice and how to check it.",
"title": "PPC Specialist UK | Senior Google Ads Expert, Hired Directly",
"meta": "Hire a senior PPC specialist in the UK: 14+ years on Google, Microsoft, Meta and LinkedIn Ads, working directly with you instead of through an agency. Flat fee, quoted in pounds.",
"kicker": "PPC specialist",
"h1": "A PPC specialist with 14+ years on the account, hired directly instead of through an agency",
"lead": "Specialist and expert are words every agency uses in its pitch. This page sets out what a senior PPC specialist actually does differently, how to check it before you hire one, and how the engagement works when the specialist is the person you deal with.",
"service_name": "PPC specialist services",
"body": """
<section><div class="wrap">
<h2>What a senior specialist does that a generalist or a junior does not</h2>
<ul>
<li><strong>Reads the search terms before touching the bids.</strong> Most waste in UK lead generation accounts is in what gets counted and in the queries matched, not in the bidding. A specialist starts there.</li>
<li><strong>Treats the automation as a tool with settings, not as a strategy.</strong> Smart Bidding and Performance Max are switched on when the conversion data deserves them and reviewed with the brand excluded, so the reported result is real.</li>
<li><strong>Owns the measurement.</strong> GA4, Tag Manager, Consent Mode v2 and the CRM are part of the job, because a specialist cannot optimise towards a number that is wrong.</li>
<li><strong>Builds the page after the click.</strong> The landing page is usually the largest lever in the account and the one nobody who runs the ads has touched. Here it is included.</li>
<li><strong>Says no.</strong> To budget increases the data does not support, to platforms that do not fit the business, to accounts that need an agency rather than one person.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>How to check a PPC specialist before hiring one</h2>
<ol class="steps">
<li><div><strong>Ask who will be in the account weekly.</strong> If the answer is a team, ask for the name and the years of experience of the person doing the work. Here the answer is one name, and it is the person you spoke to.</div></li>
<li><div><strong>Ask for a written review before any retainer.</strong> A specialist can read your account read-only and tell you in writing what is wrong and what it costs each month. That is the <a href="/ppc-audit/">PPC audit</a>, and it stands on its own.</div></li>
<li><div><strong>Ask how results are reported.</strong> Platform numbers alone are a warning sign. The report should reconcile to your CRM or your orders, in pounds, with brand and non-brand shown separately.</div></li>
<li><div><strong>Ask what they will not do.</strong> A specialist has a scope. Mine is Google, Microsoft, Meta and LinkedIn Ads for businesses spending roughly £2,000 to £60,000 a month, with the exceptions listed on the <a href="/">home page</a>.</div></li>
<li><div><strong>Check the published work.</strong> Named cases where the client allowed it, anonymised where they did not, with the figures and their source stated. <a href="/results/">Results →</a></div></li>
</ol>
</div></section>

<section><div class="wrap">
<h2>Specialist, consultant, freelancer: which word applies</h2>
<p>UK businesses search for all three and the work is the same person. "Specialist" and "expert" describe depth on the platforms; "<a href="/google-ads-consultant/">consultant</a>" describes advice and reviews available without a retainer; "<a href="/ppc-freelancer/">freelancer</a>" describes the independence from an agency. All three are true here, and none of them is the point. The point is that the senior person is the one in the account.</p>
</div></section>

<section><div class="wrap">
<h2>How an engagement with a specialist starts</h2>
<p>Read-only access, a fixed-price written review, then your choice: implement it yourselves, hire me for the fixes, or have me run the account month to month with 30 days' notice either way. Fees are flat, set from the scope, never a percentage of spend, and quoted in pounds, ex VAT, by email from the form.</p>
</div></section>
""",
"faq": [
("How much does a PPC specialist cost in the UK?", "Senior freelance specialists commonly quote a few hundred pounds a day or a flat monthly retainer; agencies commonly charge a percentage of spend with a minimum. My fee is flat, set from the scope of the account, and quoted in pounds, ex VAT, from the form. See <a href=\"/pricing/\">pricing</a>."),
("What is the difference between a PPC specialist and a PPC agency?", "Who does the work. An agency puts an account team between you and the account, usually led by someone junior once the pitch is over. A specialist is the person doing the work, and you speak to them directly. The full comparison is on <a href=\"/agency-vs-consultant/\">PPC agency vs PPC consultant</a>."),
("Which platforms are you a specialist in?", "Google Ads first, including Shopping, Performance Max, YouTube and Demand Gen; then Microsoft Advertising, Meta Ads and LinkedIn Ads, with GA4, Tag Manager and landing pages as part of every engagement."),
("Can you work alongside our in-house marketer?", "Yes. A common arrangement is a monthly review of the work your team does, with a written note and a call, or a setup that your team then runs. The scope is agreed in writing at the start."),
("Are you certified?", "Platform certifications are easy to obtain and say little about judgement. What you can check is the written review, the published cases and how the first call goes."),
],
"related": ["google-ads-consultant", "ppc-freelancer", "ppc-audit", "agency-vs-consultant"],
},

# ---------------------------------------------------------------- Law firms
{
"slug": "ppc-for-law-firms", "short": "PPC for law firms", "blurb": "Google Ads for solicitors: paying for instructions, not for people comparing fees.",
"title": "PPC for Law Firms UK | Google Ads for Solicitors, Run by One Consultant",
"meta": "PPC for UK law firms and solicitors: Google Ads built around practice areas, enquiries counted as instructions, research searches excluded, SRA rules respected. Flat fee, no percentage of spend.",
"kicker": "PPC for law firms",
"h1": "PPC for law firms: paying for instructions, not for people comparing fees at £15 a click",
"lead": "Legal is one of the most expensive auctions in the UK. Employment, conveyancing, family and personal injury searches cost from several pounds to well over £15 a click in the large cities. At that price, the difference between a firm that profits from Google Ads and one that does not is almost never the bid. It is what gets counted, what gets excluded and the page after the click.",
"service_name": "PPC for law firms",
"body": """
<section><div class="wrap">
<h2>Where law firm accounts waste money</h2>
<ul>
<li><strong>Research searches billed as leads.</strong> "How much does a divorce cost", "can I be sacked for", "free legal advice". These searches match broad and phrase keywords, cost as much as a client search, and almost never instruct. Twelve months of search terms read line by line is the first task.</li>
<li><strong>One campaign for the whole firm.</strong> Family, employment and conveyancing share a budget, and the cheapest enquiries take it. Each practice area gets its own campaign, budget and landing page.</li>
<li><strong>A call counted as a client.</strong> Phone clicks and form fills are not instructions. Call tracking tied to the keyword, a qualifying form and the case management system feeding back which enquiries became matters are what let Google optimise towards clients.</li>
<li><strong>The firm's homepage as the landing page.</strong> Someone who searched for an employment solicitor should land on a page about employment law, with the solicitor's name, the first-step explained and the phone number at the top.</li>
<li><strong>Adverts that would not pass compliance.</strong> Claims about outcomes, "no win no fee" without the qualifications, comparative claims about other firms. The SRA Transparency Rules and the ASA set what can be said, and the adverts are written inside that.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>What a click costs by practice area and city</h2>
<p>Average cost per click from Google Ads keyword data for the UK, October 2026, for the search with the city attached. Market averages, not a forecast.</p>
<table>
<tr><th>Search</th><th>London</th><th>Manchester</th><th>Birmingham</th><th>Leeds</th><th>Bristol</th></tr>
<tr><td>solicitors [city]</td><td>£13.49</td><td>£9.46</td><td>£9.31</td><td>£7.09</td><td>£7.97</td></tr>
<tr><td>employment lawyer [city]</td><td>£18.60</td><td>£10.95</td><td>£10.92</td><td>£9.99</td><td>£11.72</td></tr>
</table>
<p>At these prices, 100 clicks on an employment search in London cost close to £1,900. If one in ten calls and one in four callers instructs, that is £760 per instruction before the fee. If a third of those clicks were research searches that should have been excluded, the real figure was closer to £500. That is the arithmetic the account is run on.</p>
</div></section>

<section><div class="wrap">
<h2>What management includes for a law firm</h2>
<ol class="steps">
<li><div><strong>A campaign per practice area</strong>, with exact and phrase match, a negatives programme built from the research vocabulary of each area, and location targeting matched to where the firm takes clients.</div></li>
<li><div><strong>Measurement to the matter.</strong> Call tracking, a form that asks the qualifying question, and the case management system (Clio, LEAP, Proclaim or a spreadsheet) feeding back which enquiries opened a file, imported to Google Ads as offline conversions. See <a href="/conversion-tracking/">conversion tracking</a>.</div></li>
<li><div><strong>A page per practice area</strong>, built by me, with the solicitor, the process, the fee basis as the Transparency Rules require, and a phone number and form that work on a mobile at lunchtime. See <a href="/landing-pages/">landing pages</a>.</div></li>
<li><div><strong>Brand and competitor terms decided, not defaulted.</strong> Whether to bid on the firm's own name depends on who else is bidding on it; competitor bidding is legal in the UK and usually poor value. Both reviewed monthly.</div></li>
<li><div><strong>Microsoft Advertising</strong> once Google works: a professional audience on work devices, often at a lower cost per enquiry for legal searches. <a href="/microsoft-ads-management/">Microsoft Ads →</a></div></li>
<li><div><strong>A monthly report in instructions and cost per instruction</strong>, by practice area, alongside the platform numbers so the two can be compared.</div></li>
</ol>
</div></section>

<section><div class="wrap">
<h2>Who this fits</h2>
<p>UK firms from a few fee earners to mid-size regional practices, spending roughly £2,000 to £40,000 a month, in practice areas where a client is worth several hundred pounds or more: employment, family, private client, conveyancing, commercial, immigration, personal injury where the firm handles its own intake. Claims management companies and lead resellers are not a fit. There is no law firm case on this site yet and none will be invented; the <a href="/results/">published cases</a> show the method on other expensive auctions.</p>
</div></section>
""",
"faq": [
("How much should a law firm spend on Google Ads?", "Enough to buy a meaningful number of clicks in your practice area and city, which the table above lets you estimate: at £10 to £19 a click, a few thousand pounds a month is the floor for a single practice area in a large city. The first call includes this arithmetic for your firm."),
("Can you work within SRA and ASA rules?", "Yes. Adverts avoid outcome claims and comparative claims, 'no win no fee' carries its qualifications, and the landing pages carry the price and service information the SRA Transparency Rules require for the relevant areas. Your compliance partner signs off the copy before it runs."),
("Do you bid on competitor firm names?", "Only if the numbers support it, and they usually do not: the clicks are expensive, the conversion rate is low and the ASA has rules on how the advert may be worded. It is reviewed, not assumed."),
("Can you connect Google Ads to our case management system?", "Yes, through an offline conversion import: Clio, LEAP, Proclaim and most systems can export the enquiries that became matters, and a scheduled upload teaches Google which clicks produced clients."),
("How much does PPC management for a law firm cost?", "A flat monthly fee set from the scope: practice areas, platforms and how much landing page and tracking work is included. Never a percentage of spend. Quoted in pounds, ex VAT, by email from the form. See <a href=\"/pricing/\">pricing</a>."),
],
"related": ["ppc-audit", "google-ads-management", "landing-pages", "ppc-consultant-london"],
},

# ---------------------------------------------------------------- Healthcare
{
"slug": "healthcare-ppc", "short": "Healthcare PPC", "blurb": "Private clinics, dental and healthcare brands: enquiries that become appointments, within Google's health policies.",
"title": "Healthcare PPC UK | Google Ads for Private Clinics and Health Brands",
"meta": "Healthcare PPC for UK private clinics, dental practices and health brands: Google and Meta Ads measured in booked appointments, run within platform health policies by one senior consultant.",
"kicker": "Healthcare PPC",
"h1": "Healthcare PPC measured in booked appointments, run inside the rules the platforms apply to health advertisers",
"lead": "Private healthcare is a crowded UK auction with its own constraints: restricted remarketing, certification for some categories, claims the ASA and the CAP Code do not allow, and patients who research for weeks before booking. The accounts that work are the ones where the measurement reaches the appointment book and the campaigns respect the research journey instead of paying for it twice.",
"service_name": "Healthcare PPC",
"body": """
<section><div class="wrap">
<h2>What is different about healthcare accounts</h2>
<ul>
<li><strong>Policy limits the tools.</strong> Google restricts personalised advertising for health conditions, so remarketing lists built on condition pages are not available; some categories (prescription medicines, certain treatments) require certification before adverts run; Meta has its own health and wellness data restrictions. The structure has to work without the tools other sectors lean on.</li>
<li><strong>Claims are regulated.</strong> Outcome claims, before-and-after imagery for some procedures, and anything that implies a guarantee fall under the CAP Code and, for medicines and devices, the MHRA. Copy is written inside those rules and your clinical lead signs it off.</li>
<li><strong>Research searches dominate.</strong> "Symptoms of", "is it normal", "NHS waiting time for" are expensive, well-meaning and do not book. They are excluded, and the budget goes to the searches that name a treatment, a clinic or a location.</li>
<li><strong>The conversion is an appointment, not a form.</strong> Reception answers the phone; the booking system knows who attended. Until those feed back, Google optimises towards whoever fills in a form, including the people who never show up.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>What management includes</h2>
<ol class="steps">
<li><div><strong>Structure by treatment and location.</strong> A campaign per service line (implants, cosmetic, physiotherapy, fertility, diagnostics) with location targeting matched to how far patients travel for that treatment, and the research vocabulary excluded.</div></li>
<li><div><strong>Measurement to the appointment.</strong> Call tracking with reception outcomes, booking system or practice management software (Dentally, Cliniko, Semble and others) feeding attended appointments back as offline conversions, Consent Mode v2 and a privacy setup that keeps health data out of the ad platforms. See <a href="/conversion-tracking/">conversion tracking</a>.</div></li>
<li><div><strong>Pages built for a worried person.</strong> One page per treatment with the clinician, the process, the price basis, the next available appointment and a phone number at the top, loading fast on a mobile. See <a href="/landing-pages/">landing pages</a>.</div></li>
<li><div><strong>Meta where it fits.</strong> Awareness and remarketing for elective treatments, within Meta's health restrictions, judged on booked consultations rather than on form fills. <a href="/facebook-ads-management/">Facebook Ads →</a></div></li>
<li><div><strong>Reporting in appointments.</strong> Cost per booked and attended appointment by treatment, alongside the platform numbers, in pounds.</div></li>
</ol>
</div></section>

<section><div class="wrap">
<h2>Who this fits</h2>
<p>UK private clinics and groups, dental practices, physiotherapy and diagnostics providers, aesthetics clinics working within the rules, and health brands selling direct. Typically £2,000 to £40,000 a month across Google and Meta. Fourteen years that include senior in-house healthcare work and a freelance role with a US pharmaceutical agency; no patient-facing UK case is published on this site, and none will be invented.</p>
</div></section>
""",
"faq": [
("Can you run Google Ads for a private clinic given the health policies?", "Yes. The restrictions remove some tools (condition-based remarketing, some audience features) and require certification for certain categories. The account is built to work within that, and the certification process is handled with you where it applies."),
("Can you connect Google Ads to our booking system?", "Usually, through an offline conversion import: Dentally, Cliniko, Semble and most practice systems can export which enquiries booked and attended, without sending any clinical data to Google. Where there is no export, reception outcomes from call tracking do most of the job."),
("What about GDPR and patient data?", "No health data goes to the ad platforms. Conversions are sent as outcomes (booked, attended) with hashed contact data where enhanced conversions are used, under Consent Mode v2, and the setup is documented for your data protection lead."),
("Do you work with dental practices?", "Yes. Dental is one of the more competitive local health auctions in the UK, and the structure by treatment (implants, Invisalign, emergency, general) with the practice management system feeding back attended appointments is the pattern that works."),
("How much does healthcare PPC management cost?", "A flat monthly fee set from the scope: treatments, locations, platforms and how much landing page and tracking work is included. Never a percentage of spend. Quoted in pounds, ex VAT, by email from the form. See <a href=\"/pricing/\">pricing</a>."),
],
"related": ["ppc-audit", "google-ads-management", "conversion-tracking", "landing-pages"],
},

# ---------------------------------------------------------------- SaaS
{
"slug": "saas-ppc", "short": "SaaS PPC", "blurb": "Google and LinkedIn Ads for software companies, measured in qualified pipeline and payback, not sign-ups.",
"title": "SaaS PPC Consultant UK | Google & LinkedIn Ads Measured in Pipeline",
"meta": "SaaS PPC for UK and Irish software companies: Google Search for buyers already looking, LinkedIn for the ones who are not, CRM-connected measurement and reporting in pipeline and CAC payback.",
"kicker": "SaaS PPC",
"h1": "SaaS PPC measured in qualified pipeline and payback, by one consultant across Google and LinkedIn",
"lead": "Software companies have the cleanest data in paid media and often the worst use of it. The CRM knows which trials became customers and what they pay; the ad platforms are optimising towards sign-ups. Connecting the two is most of the job, and it is where a SaaS account starts here.",
"service_name": "SaaS PPC management",
"body": """
<section><div class="wrap">
<h2>Where SaaS accounts leak</h2>
<ul>
<li><strong>Optimising towards the top of the funnel.</strong> Free trials, demo requests and content downloads are easy to count and cheap to buy. Without product-qualified or sales-accepted stages flowing back, the platforms buy the cheapest sign-ups, which churn.</li>
<li><strong>Competitor and category terms treated the same.</strong> "[Competitor] alternative" and "best [category] software" bring different buyers at different stages and should sit in separate campaigns with separate pages and expectations.</li>
<li><strong>Brand taking the credit.</strong> Performance Max and broad match drift onto the brand name and the reported CAC looks wonderful. Brand is isolated, and the non-brand number is the one managed.</li>
<li><strong>LinkedIn judged on form fills.</strong> A £10 click on a Head of Operations who downloads a benchmark is not pipeline. LinkedIn is judged on qualified opportunities from the CRM or not at all.</li>
<li><strong>Payback ignored.</strong> A customer acquired at £900 on a £40 monthly plan is a 22-month payback before gross margin. The targets by plan and segment come from that arithmetic, not from a blended CAC.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>What management includes</h2>
<ol class="steps">
<li><div><strong>Measurement to the CRM.</strong> GA4 and Tag Manager with a user ID, HubSpot or Salesforce stages (MQL, SQL, opportunity, closed won, with amount) imported to Google Ads and LinkedIn as offline conversions, so the platforms optimise towards revenue. See <a href="/conversion-tracking/">conversion tracking</a>.</div></li>
<li><div><strong>Google Search by intent.</strong> Category, problem, integration and competitor campaigns, each with its own page and its own target, brand kept separate, Performance Max only with brand excluded and only once the conversion data deserves it.</div></li>
<li><div><strong>LinkedIn for the accounts that are not searching.</strong> Named account lists from the CRM, firmographic and title targeting, offers built for a buyer with a problem this quarter, conversation and document ads tested against a control. <a href="/linkedin-ads-management/">LinkedIn Ads →</a></div></li>
<li><div><strong>Microsoft Advertising</strong> for the professional audience on work devices, with LinkedIn profile bid adjustments Google cannot offer. <a href="/microsoft-ads-management/">Microsoft Ads →</a></div></li>
<li><div><strong>Pages per intent</strong>, built by me: comparison pages, integration pages, use-case pages, with the trial or demo form that asks the one qualifying question. See <a href="/landing-pages/">landing pages</a>.</div></li>
<li><div><strong>Reporting in pipeline and payback.</strong> Qualified pipeline, closed-won revenue and CAC payback by channel and segment, alongside the platform numbers.</div></li>
</ol>
</div></section>

<section><div class="wrap">
<h2>A published SaaS result</h2>
<p>Pontomais, a time-tracking and HR software startup, grew sales by 600% in eight months with paid media, most of it Google, run by me. The figures come from the company's own sales reporting at the time; the full note is on <a href="/results/">results</a>. The market was Brazil and the currency was different, but the method was the one above: the CRM connected first, campaigns split by intent, brand isolated, and budget following measured pipeline.</p>
</div></section>

<section><div class="wrap">
<h2>Who this fits</h2>
<p>UK and Irish B2B software companies from seed to Series B, or established vertical SaaS, spending roughly £3,000 to £60,000 a month across Google and LinkedIn, with a CRM in use and a sales or product-led motion that can report stages. Consumer apps measured on installs are not a fit.</p>
</div></section>
""",
"faq": [
("What CAC should a SaaS company expect from Google Ads?", "No honest number exists before the account and the CRM are read together. What is measurable from the first month is CAC by channel and segment against your plan prices, which gives payback, and that is the figure the targets are set from."),
("Can you connect Google Ads and LinkedIn to HubSpot or Salesforce?", "Yes. Offline conversion import from CRM stages with amounts, enhanced conversions for leads, and a user ID in GA4 so the journey from click to closed won is visible. The setup is documented so your RevOps team owns it."),
("Should we bid on competitor names?", "Usually yes, in a separate campaign with its own page and a target that reflects the lower conversion rate. Comparison pages that are honest about where the competitor is better convert well and stay within the advertising rules."),
("Do you run product-led growth accounts?", "Yes, provided product-qualified signals (activation, team invites, usage thresholds) can be fed back. Without them the platforms optimise towards sign-ups that never activate, and the budget is better spent elsewhere."),
("How much does SaaS PPC management cost?", "A flat monthly fee set from the scope: platforms, markets, campaigns and how much landing page and tracking work is included. Never a percentage of spend. Quoted in pounds, ex VAT, by email from the form. See <a href=\"/pricing/\">pricing</a>."),
],
"related": ["b2b-ppc", "linkedin-ads-management", "conversion-tracking", "landing-pages"],
},

# ---------------------------------------------------------------- Cities
city_page(
    "ppc-consultant-manchester", "Manchester", "Manchester",
    "<p>Manchester is the second paid search market in the UK by most measures, with a professional services, technology and property base that competes on the same searches as London at a lower price per click. The margin for error is wider than in London; the habits that waste budget are the same.</p>",
    """<div class="card"><h3>Professional services</h3><p>Solicitors and accountants across Spinningfields and the city centre: clicks cost less than in London but the research searches are the same, and a page per practice area still beats a firm-wide page. <a href="/ppc-for-law-firms/">PPC for law firms →</a></p></div>
<div class="card"><h3>Technology and SaaS</h3><p>Manchester's software and digital firms sell to the whole country and often abroad. Google captures the buyers already searching; LinkedIn reaches the ones who are not. Judged on pipeline from the CRM. <a href="/saas-ppc/">SaaS PPC →</a></p></div>
<div class="card"><h3>Home and trade services</h3><p>Greater Manchester is ten boroughs and a commuter belt. Emergency and planned work bid separately, by postcode and hour, with call tracking that tells a booked job from a ring.</p></div>""",
    "<p>Manchester clicks cost less than London's across the board, by about 30% for solicitors and more than half for IT support. Web design is the exception: at £13.97 the Manchester auction is more expensive than London's. The lesson is to price your own auction rather than assume, which is one of the first things an <a href=\"/ppc-audit/\">audit</a> does.</p>",
    [("Do you cover the rest of Greater Manchester?", "Yes: Salford, Stockport, Trafford, Bolton, Bury, Oldham, Rochdale, Tameside and Wigan, with location targeting set to how your business actually serves them rather than one pin on the city centre.")],
    "<p>For a Manchester solicitor, the same three moves mean separating practice areas that share one campaign, counting an instruction rather than a call, and cutting the research searches that eat budget at around £10 a click.</p>",
),
city_page(
    "ppc-consultant-birmingham", "Birmingham", "Birmingham",
    "<p>Birmingham and the West Midlands carry the largest search volumes outside London for professional services, with the highest number of solicitor searches of any regional city, and a manufacturing and industrial base that buys through long B2B cycles. The auction is cheaper than London for most searches and more expensive for a few.</p>",
    """<div class="card"><h3>Professional services</h3><p>Birmingham has more "solicitors" searches a month than any UK city outside London. More searches means more research traffic to exclude, and a practice-area structure matters more, not less. <a href="/ppc-for-law-firms/">PPC for law firms →</a></p></div>
<div class="card"><h3>Manufacturing and industrial B2B</h3><p>The West Midlands' engineering and industrial suppliers sell to procurement teams on long cycles. Google Search for the specification searches, LinkedIn for the account list, both judged on quoted pipeline from the CRM. <a href="/b2b-ppc/">B2B PPC →</a></p></div>
<div class="card"><h3>Home and trade services</h3><p>Birmingham, Solihull, Wolverhampton, Coventry and the Black Country are different service areas with different competition. Bids by area and hour, and call tracking that separates a booked job from a ring.</p></div>""",
    "<p>Birmingham is the cheapest of the large cities for IT support, at under a third of the London price, and close to Manchester for legal and accountancy searches. It is the most expensive city in the table for web design and nearly level with London for financial advice. Pricing your own auction before setting a budget is one of the first things an <a href=\"/ppc-audit/\">audit</a> does.</p>",
    [("Do you cover the wider West Midlands?", "Yes: Solihull, Wolverhampton, Coventry, Walsall, Dudley and Sandwell, with location targeting and bids set to how your business actually serves each area.")],
    "<p>For a Birmingham industrial supplier, the same three moves mean splitting specification searches from generic ones, counting a quote request rather than a page view, and feeding the CRM's won quotes back to Google so it learns which clicks became orders.</p>",
),
city_page(
    "ppc-consultant-leeds", "Leeds", "Leeds",
    "<p>Leeds is the financial and legal centre of the North, with a cluster of law firms, accountancy practices, banks and fintechs that buy paid search seriously, and a cost per click that is the lowest of the large English cities for most professional searches. Cheaper clicks make the same mistakes cheaper, not free.</p>",
    """<div class="card"><h3>Legal and professional services</h3><p>Leeds has the lowest solicitor and accountancy click prices of the large cities, which makes a properly structured account very efficient and a badly structured one merely cheap. <a href="/ppc-for-law-firms/">PPC for law firms →</a></p></div>
<div class="card"><h3>Financial services and fintech</h3><p>Advisers, lenders and the fintech cluster. Google requires FCA verification for many financial products in the UK before adverts run, and every claim must stand up. Budgets are wasted less by bids than by disapproved adverts and research traffic.</p></div>
<div class="card"><h3>B2B and technology</h3><p>Leeds' digital and B2B services firms sell nationally. Google for the buyers already searching, LinkedIn for the named accounts, both reported in pipeline. <a href="/b2b-ppc/">B2B PPC →</a></p></div>""",
    "<p>Leeds has the lowest click prices in the table for solicitors, employment law, accountancy and web design, between a third and a half below London. IT support is the exception: at £26.67 Leeds is the second most expensive city for that search, ahead of Manchester and Birmingham. Each sector has its own auction, and an <a href=\"/ppc-audit/\">audit</a> prices yours before anything is changed.</p>",
    [("Do you cover West Yorkshire beyond Leeds?", "Yes: Bradford, Wakefield, Huddersfield, Halifax and Harrogate, with location targeting and bids set to how your business actually serves each area.")],
    "<p>For a Leeds financial adviser, the same three moves mean separating the advice searches from the product searches, counting a booked first meeting rather than a form, and excluding the research traffic that an FCA-verified advert attracts at £19 a click.</p>",
),
city_page(
    "ppc-consultant-bristol", "Bristol", "Bristol",
    "<p>Bristol is the largest market in the South West, with an engineering, aerospace, creative and technology base, a strong professional services sector and a catchment that reaches Bath, Gloucester and across the bridge into South Wales. Click prices sit between Leeds and London for most searches, with financial advice the most expensive in the table.</p>",
    """<div class="card"><h3>Technology, engineering and B2B</h3><p>Bristol's technology, aerospace supply chain and creative agencies sell to procurement teams across the UK. Google for the specification searches, LinkedIn for the named accounts, both judged on pipeline from the CRM. <a href="/b2b-ppc/">B2B PPC →</a></p></div>
<div class="card"><h3>Professional and financial services</h3><p>Solicitors, accountants and advisers serving Bristol, Bath and the surrounding counties. Financial advice is the most expensive search in the table here, so excluding research traffic matters more than anywhere else in the region. <a href="/ppc-for-law-firms/">PPC for law firms →</a></p></div>
<div class="card"><h3>Home and trade services</h3><p>Bristol, Bath, North Somerset and South Gloucestershire are different service areas. Emergency and planned work bid separately, by postcode and hour, with call tracking that tells a booked job from a ring.</p></div>""",
    "<p>Bristol is the most expensive city in the table for financial advice, at £23.98, ahead of London. For solicitors and web design it is among the cheapest, close to Leeds. Accountancy sits above Manchester and Birmingham. The spread shows why a budget set from a national average goes wrong, and why an <a href=\"/ppc-audit/\">audit</a> starts by pricing your own auction.</p>",
    [("Do you cover Bath and the wider South West?", "Yes: Bath, Weston-super-Mare, Gloucester, Cheltenham, Swindon and across to Cardiff and Newport, with location targeting and bids set to how your business actually serves each area.")],
    "<p>For a Bristol engineering supplier, the same three moves mean splitting specification searches from generic ones, counting a quote request rather than a visit, and feeding won quotes back from the CRM so Google learns which clicks became orders.</p>",
),
# ---------------------------------------------------------------- PPC consultation (one-off session)
{
"slug": "ppc-consultation", "short": "PPC consultation", "blurb": "A one-off working session on your account, with written notes, before or instead of a retainer.",
"title": "PPC Consultation UK | One-Off Google Ads Session With Written Notes",
"meta": "Book a PPC consultation: a one-off working session on your Google, Microsoft, Meta or LinkedIn account with a senior UK-facing consultant, with written notes afterwards. Fixed price in pounds.",
"kicker": "PPC consultation",
"h1": "A PPC consultation: one working session on your account, with written notes, before or instead of a retainer",
"lead": "Not every account needs an audit or a retainer. Sometimes a business needs a senior person to look at the account for an hour, answer the three questions that have been going round for months, and write down what to do next. That is the consultation, and it is the smallest way to work with me.",
"service_name": "PPC consultation",
"body": """
<section><div class="wrap">
<h2>When a consultation is the right size</h2>
<ul>
<li><strong>A decision is pending.</strong> Whether to move to Performance Max, whether to take the agency's proposal, whether the budget increase is justified, whether to bid on the brand. A second opinion from someone with no retainer to win.</li>
<li><strong>An in-house marketer wants a senior check.</strong> You run the account yourself and want an experienced pair of eyes on the structure, the tracking and the search terms before the next quarter.</li>
<li><strong>Something broke.</strong> Conversions stopped recording, the account was suspended, spend doubled overnight, and you need the cause and the fix without a six-week engagement.</li>
<li><strong>You are choosing a supplier.</strong> You have two agency proposals and want them read by someone who runs accounts, with the questions to ask each one.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>How the consultation works</h2>
<ol class="steps">
<li><div><strong>Before the call.</strong> You send the form with the spend band, the platforms and the questions. If the account is live, read-only access to Google Ads and GA4 so the hour is spent on answers rather than on screen-sharing.</div></li>
<li><div><strong>The session.</strong> A video call of about an hour, on UK time, working through the account and your questions in order of money at stake. Recorded if you want it.</div></li>
<li><div><strong>Written notes within two working days.</strong> What was found, what to do, in what order, and what to measure to know it worked. Written so your team or your agency can act on it.</div></li>
<li><div><strong>Credited if it grows.</strong> If the consultation becomes a <a href="/ppc-audit/">full audit</a> or <a href="/ppc-management/">management</a> within 60 days, the consultation fee is credited against it.</div></li>
</ol>
</div></section>

<section><div class="wrap">
<h2>Consultation, audit or management</h2>
<table>
<tr><th></th><th>Consultation</th><th>Audit</th><th>Management</th></tr>
<tr><td>What it is</td><td>One working session plus notes</td><td>A full written review of every platform in scope</td><td>Running the account month to month</td></tr>
<tr><td>Time</td><td>About an hour, notes within two working days</td><td>5 to 7 working days</td><td>Ongoing, 30 days' notice either way</td></tr>
<tr><td>Best for</td><td>A decision, a second opinion, a broken thing, an in-house check</td><td>Knowing everything that is wrong and what it costs</td><td>Having the senior person do the work</td></tr>
<tr><td>Price</td><td>Fixed, in pounds, quoted from the form</td><td>Fixed, set from spend, campaigns and platforms</td><td>Flat monthly fee, set from scope</td></tr>
<tr><td>Credited against</td><td>An audit or management within 60 days</td><td>The first month of management</td><td></td></tr>
</table>
<p>How each is priced, with market ranges, is on <a href="/pricing/">pricing</a>.</p>
</div></section>

<section><div class="wrap">
<h2>What a consultation is not</h2>
<p>It is not a sales call dressed as advice: the fee is the same whether or not you go on to work with me, and most consultations end with the notes. It is not a free audit; those are on the <a href="/ppc-audit/">audit page</a>, with the reasons they are a poor idea. And it is not training in Google Ads from the ground up; it assumes someone on your side runs or oversees the account already.</p>
</div></section>
""",
"faq": [
("How much does a PPC consultation cost?", "A fixed fee in pounds, ex VAT, quoted by email from the form within one working day. It is credited against an audit or the first month of management if either follows within 60 days. See <a href=\"/pricing/\">pricing</a> for how everything is priced."),
("Can we book more than one session?", "Yes. Some in-house teams book a session each month or each quarter as a standing review; that is agreed in writing after the first one, with the same notes each time."),
("Do you need access to our account for a consultation?", "It helps: read-only access to Google Ads and GA4 beforehand means the hour goes on answers. Without access, the session works from your screen share and your questions, and the notes say what to check."),
("Which platforms can the consultation cover?", "Google Ads (Search, Shopping, Performance Max, YouTube, Demand Gen), Microsoft Advertising, Meta Ads and LinkedIn Ads, plus GA4, Tag Manager and landing pages."),
("Is the consultation available to businesses outside the UK?", "Yes. UK and Irish businesses are quoted in pounds here; US and Canadian businesses have the same session on <a href=\"https://googleadsfreelancer.com/google-ads-consultation/\" rel=\"noopener\">googleadsfreelancer.com</a>, quoted in dollars."),
],
"related": ["ppc-audit", "google-ads-consultant", "ppc-management", "pricing"],
},
]
