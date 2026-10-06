# Pages added in October 2026 from the page expansion study (research/estudo-paginas-2026-10-06.md):
# services the UK site already had, sector pages and a Houston page. US spelling throughout. No prices, no claims
# beyond the published cases on /results/.

CITY_CPC = {  # Google Ads keyword data, US, October 2026: average CPC in dollars for the search with the city attached
    "Houston": {"plumber": 35.53, "HVAC repair": 29.18, "roofing company": 14.44, "dentist": 16.76, "personal injury lawyer": 126.93, "IT support": 88.94},
    "Dallas":  {"plumber": 35.66, "HVAC repair": 43.67, "roofing company": 10.66, "dentist": 12.60, "personal injury lawyer": 139.57, "IT support": 42.06},
    "Phoenix": {"plumber": 54.16, "HVAC repair": 17.70, "roofing company": 16.74, "dentist": 21.82, "personal injury lawyer": 126.26, "IT support": 17.86},
}

PAGES = [

# ---------------------------------------------------------------- B2B PPC
{
"slug": "b2b-ppc", "short": "B2B PPC", "blurb": "Search for the buyers already looking, LinkedIn for the ones who are not, both judged on pipeline.",
"title": "B2B PPC Consultant | Google and LinkedIn Ads for Pipeline, Not Leads",
"meta": "B2B PPC by an independent consultant: Google Search for buyers already looking, LinkedIn for the rest, CRM-connected and reported in pipeline. Flat fee.",
"kicker": "B2B PPC",
"h1": "B2B PPC measured in qualified pipeline, by one consultant across Google, Microsoft and LinkedIn",
"lead": "B2B accounts fail in a specific way: the platforms are optimizing toward form fills, the sales team is ignoring them, and nobody can say which campaign produced the last closed deal. Connecting the CRM to the ad platforms is most of the job, and it is where a B2B engagement starts here.",
"service_name": "B2B PPC management",
"body": """
<section><div class="wrap">
<h2>Where B2B accounts leak</h2>
<ul>
<li><strong>Leads counted, pipeline not.</strong> A whitepaper download and a demo request from a named account are both "a lead" to the platform. Until MQL, SQL and opportunity stages flow back from HubSpot or Salesforce, Google and LinkedIn buy the cheapest form fill, which is the least qualified one.</li>
<li><strong>Brand taking the credit.</strong> Broad match and Performance Max drift onto the company name and the reported cost per lead looks excellent. Brand is isolated, and the non-brand number is the one managed.</li>
<li><strong>Research and job-seeker traffic.</strong> "What is", "salary", "jobs", "free template": expensive clicks from people who will never buy. Twelve months of search terms read line by line, then a negatives program maintained weekly.</li>
<li><strong>LinkedIn judged like Google.</strong> A $12 click on a VP who downloads a benchmark is not pipeline. LinkedIn is judged on qualified opportunities from the CRM or not at all.</li>
<li><strong>One page for every intent.</strong> A category search, a competitor comparison and an integration search deserve different pages with different asks.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>What management includes</h2>
<ol class="steps">
<li><div><strong>Measurement to the CRM.</strong> GA4 and Tag Manager with campaign data attached to every lead, HubSpot, Salesforce or Pipedrive stages imported to Google Ads and LinkedIn as offline conversions with amounts, enhanced conversions for leads. See <a href="/conversion-tracking-setup/">conversion tracking</a>.</div></li>
<li><div><strong>Google Search by intent.</strong> Category, problem, integration and competitor campaigns, each with its own page and target, brand kept separate, Performance Max only with brand excluded and only once the conversion data deserves it.</div></li>
<li><div><strong>LinkedIn for the accounts that are not searching.</strong> Named account lists, firmographic and title targeting, offers built for a buyer with a problem this quarter, tested against a control. <a href="/linkedin-ads-management/">LinkedIn Ads →</a></div></li>
<li><div><strong>Microsoft Advertising</strong> for the professional audience on work devices, with LinkedIn profile bid adjustments Google cannot offer. <a href="/microsoft-ads-management/">Microsoft Ads →</a></div></li>
<li><div><strong>Pages per intent</strong>, built by me: comparison pages, integration pages, use-case pages, with a form that asks the one qualifying question. See <a href="/landing-pages/">landing pages</a>.</div></li>
<li><div><strong>Reporting in pipeline.</strong> Qualified pipeline, closed-won revenue and cost per opportunity by channel and segment, alongside the platform numbers, in your currency.</div></li>
</ol>
</div></section>

<section><div class="wrap">
<h2>Published B2B results</h2>
<p>Two of the four cases on <a href="/results/">results</a> were sold to organizations rather than consumers: a SaaS startup that grew sales by 600% in eight months with paid media, most of it Google, and a private school group that reached a 5,000-student enrollment target three months early. The figures come from the companies' own reporting and are labeled as such. The method was the one above.</p>
</div></section>

<section><div class="wrap">
<h2>Who this fits</h2>
<p>US and Canadian B2B companies, and companies from any country that work in English: SaaS, professional and technical services, industrial suppliers, consultancies, spending roughly $5,000 to $80,000 a month across Google and LinkedIn, with a CRM in use. Below that, Google Search alone with the CRM connected is usually the right first step, and I will say so. For software companies specifically, see <a href="/saas-ppc/">SaaS PPC</a>.</p>
</div></section>
""",
"faq": [
("What is a good cost per lead for B2B PPC?", "The wrong question, politely. Cost per qualified opportunity and cost per closed deal are the numbers, and they only exist once the CRM is connected. From that point the targets come from your deal size and sales cycle, not from an industry benchmark."),
("Can you connect Google Ads and LinkedIn to our CRM?", "Yes: HubSpot, Salesforce, Pipedrive and most others with an API or native integration. Offline conversion import with stage and amount, enhanced conversions for leads, and campaign data stored on every record so sales can see where a deal came from."),
("Should we bid on competitor names?", "Usually yes, in a separate campaign with its own comparison page and a target that reflects the lower conversion rate. Honest comparison pages convert well and stay within the advertising rules."),
("Do you run LinkedIn without Google?", "Yes, though for most B2B accounts the two work together: LinkedIn builds the audience and Google catches it when it searches. Both appear in one report either way."),
("How much does B2B PPC management cost?", "A flat monthly fee set from the scope: platforms, markets, campaigns and how much landing page and tracking work is included. Never a percentage of spend. Quoted in US dollars, pounds or euros by email from the form. See <a href=\"/pricing/\">pricing</a>."),
],
"related": ["linkedin-ads-management", "saas-ppc", "conversion-tracking-setup", "landing-pages"],
},

# ---------------------------------------------------------------- Landing pages / CRO
{
"slug": "landing-pages", "short": "Landing pages", "blurb": "Pages built by the person running the ads, tested before they go live, and improved from the account data.",
"title": "PPC Landing Pages | CRO by the Consultant Who Runs the Ads",
"meta": "Landing pages and conversion rate optimization for paid traffic, built and tested by the consultant who runs the campaigns. Included in management.",
"kicker": "Landing pages and CRO",
"h1": "Landing pages built by the person running the ads, because the page after the click is the largest lever in the account",
"lead": "Most paid accounts are optimized up to the click and abandoned after it. The ad agency does not own the website; the web agency does not read the ad account. Here the same person does both, so the page is built from the search terms, measured from the first visit and changed from the data.",
"service_name": "PPC landing pages and conversion rate optimization",
"body": """
<section><div class="wrap">
<h2>Why the page is usually the problem</h2>
<ul>
<li><strong>The homepage as the landing page.</strong> Someone who searched for emergency AC repair lands on a page about the company's history, twelve services and a careers link. The page has to answer the search in the first screen.</li>
<li><strong>A form built for the company, not the visitor.</strong> Nine fields, a captcha, no phone number on mobile. Every field removed is measured in inquiries.</li>
<li><strong>No message match.</strong> The ad promises a fixed price; the page says "contact us for a quote". The visitor leaves and the click is paid for either way.</li>
<li><strong>Slow on a phone.</strong> Most paid clicks for services are on mobile; a page that takes six seconds on a cellular connection loses a third of them before it loads.</li>
<li><strong>Nothing is tested.</strong> One page since launch, no record of what was tried. Conversion rate optimization is a program, not a redesign.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>What the work includes</h2>
<ol class="steps">
<li><div><strong>One page per intent, from the account.</strong> The search terms, the ads and the call recordings decide what each page says. Services get one page each; B2B gets comparison, integration and use-case pages.</div></li>
<li><div><strong>Built by me, on your stack.</strong> Webflow, WordPress, Unbounce, HubSpot, Shopify, or static pages hosted on your domain. No agency queue, no three-week change request.</div></li>
<li><div><strong>Tracked before it goes live.</strong> GA4, Tag Manager, call tracking and the form connected and tested, so the first visit is measured. See <a href="/conversion-tracking-setup/">conversion tracking</a>.</div></li>
<li><div><strong>Fast and compliant.</strong> Core Web Vitals checked on a real mobile connection, consent handled, accessibility basics in place.</div></li>
<li><div><strong>A test program.</strong> One change at a time, with enough traffic to read the result, recorded so the next person knows what was tried. Headline, offer, form length, proof, phone placement, in that order of likely impact.</div></li>
</ol>
</div></section>

<section><div class="wrap">
<h2>Included or standalone</h2>
<p>Included in <a href="/google-ads-management/">management retainers</a>: building and testing pages is part of running the account, not a change request. As a standalone project, a fixed price per page or per set of pages, quoted from the form, for companies that run their own ads or use another agency. Either way the pages belong to you and live on your domain.</p>
</div></section>

<section><div class="wrap">
<h2>What moved in a published case</h2>
<p>The <a href="/results/">Houston home services account</a> cut cost per acquisition by 44% and lifted qualified leads by 60%. Part of that was the account; part was the pages: one per service instead of one for the company, the phone number and the booking form in the first screen, and the promise in the ad repeated on the page.</p>
</div></section>
""",
"faq": [
("Do you design the pages or just the copy?", "Both, within a system: your brand's fonts and colors, a layout built for the intent, copy from the search terms and the sales calls. For heavy custom design a designer on your side or a studio produces the visuals and I build and test the page."),
("Which platforms can you build on?", "Webflow, WordPress, Unbounce, HubSpot, Shopify, Framer and static HTML on your own hosting. If your site is on something else, say so in the form."),
("How much does a landing page cost?", "Included in management retainers. As a standalone project, a fixed price per page or per set of pages, set from the scope and quoted by email from the form. See <a href=\"/pricing/\">pricing</a>."),
("Can you improve our existing pages instead of building new ones?", "Yes. A conversion review of the current pages against the account data comes first, and often the fixes are to the form, the first screen and the speed rather than a rebuild."),
("How long until a test shows a result?", "It depends on traffic: a page with 1,000 paid visits a month can read a meaningful change in two to four weeks; a page with 100 cannot, and the program is adjusted to test bigger changes less often."),
],
"related": ["conversion-tracking-setup", "google-ads-management", "google-ads-audit", "b2b-ppc"],
},

# ---------------------------------------------------------------- YouTube Ads
{
"slug": "youtube-ads-management", "short": "YouTube Ads management", "blurb": "Video campaigns inside Google Ads, run for measured demand rather than for views.",
"title": "YouTube Ads Management | Video Campaigns Measured in Leads and Sales",
"meta": "YouTube Ads management by an independent Google Ads specialist: in-stream, Shorts and Demand Gen measured in leads and sales, not views.",
"kicker": "YouTube Ads",
"h1": "YouTube Ads management for companies that want leads and sales from video, not a report full of views",
"lead": "YouTube is the cheapest reach in Google Ads and the easiest place to spend without result. Run as part of the Search account, with the same conversion tracking and the same person judging both, video can create the demand Search then captures. Run on its own and measured in views, it rarely pays.",
"service_name": "YouTube Ads management",
"body": """
<section><div class="wrap">
<h2>Why YouTube budgets disappear</h2>
<ul>
<li><strong>Measured in views and view rate.</strong> A view is counted at 30 seconds or a click; neither is a customer. The campaign is judged on conversions and on the lift in branded search and Search conversions during the flight.</li>
<li><strong>Audiences left to the default.</strong> Without custom segments built from your own search terms, competitor channels and in-market signals, the campaign reaches whoever is cheapest.</li>
<li><strong>One creative, run until it dies.</strong> Video wears out faster than text. A program of hooks and cuts, tested against each other, is the difference between a campaign that keeps working and one that spikes and fades.</li>
<li><strong>Demand Gen switched on as a bet.</strong> Demand Gen reaches YouTube, Discover and Gmail with the same creative and Google's audience modeling. It can work for considered purchases and lead generation; it needs conversion data to learn from and brand excluded from the credit.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>What management includes</h2>
<ol class="steps">
<li><div><strong>Objective and measurement first.</strong> Conversion actions shared with Search, view-through windows set deliberately and reported separately, brand search lift tracked during flights. See <a href="/conversion-tracking-setup/">conversion tracking</a>.</div></li>
<li><div><strong>Audience architecture.</strong> Custom segments from your search terms and competitors' names, in-market and life-event segments where they fit, remarketing from site visitors and the CRM, exclusions for existing customers.</div></li>
<li><div><strong>Format by job.</strong> Skippable in-stream for consideration, Shorts and bumpers for frequency, Demand Gen for lead generation and considered purchases, video action campaigns where the conversion data supports them.</div></li>
<li><div><strong>Creative program.</strong> Briefs for hooks in the first five seconds, cuts at 6, 15 and 30 seconds, vertical versions for Shorts, produced by your team or a studio, tested against a control and retired on a schedule.</div></li>
<li><div><strong>One report with Search.</strong> YouTube and Demand Gen next to Search, Shopping and Performance Max, with the conversions each produced and the effect on branded search, so the budget split follows the numbers.</div></li>
</ol>
</div></section>

<section><div class="wrap">
<h2>Who this fits</h2>
<p>Companies already running Search with conversion tracking that works, and with a product or service that benefits from being explained or shown: SaaS, considered consumer purchases, education, healthcare, higher-value home services. Usually $3,000 a month or more on video alongside Search. Brands that want views and reach as the objective are better served by a media agency, and I will say so. YouTube is managed as part of <a href="/google-ads-management/">Google Ads management</a> rather than as a separate retainer.</p>
</div></section>
""",
"faq": [
("How much does YouTube advertising cost?", "Cost per view is commonly a few cents; what matters is cost per lead or sale, which only exists once the campaign shares the Search account's conversion tracking. Management is part of a Google Ads retainer, a flat fee set from the scope. See <a href=\"/pricing/\">pricing</a>."),
("Do you produce the video?", "I write the briefs, the hooks and the cuts to test; your team or a studio produces the footage. Many successful campaigns run on edits of existing video, phone-shot founder pieces and product demos."),
("Is Demand Gen worth it?", "For lead generation and considered purchases with enough conversion data, often yes, with brand excluded so the reported result is real. For low-value transactions, usually not. It is tested against a budget and a target, not switched on as a bet."),
("Can you run YouTube without Google Search?", "Yes, but it is rarely the right order. Search captures the demand video creates, and without it the result of the video is hard to see and harder to keep."),
],
"related": ["google-ads-management", "conversion-tracking-setup", "meta-ads-management", "ppc-management"],
},

# ---------------------------------------------------------------- Google Ads expert / specialist
{
"slug": "google-ads-expert", "short": "Google Ads expert", "blurb": "What a senior specialist does differently, how to check it before hiring, and how the engagement works.",
"title": "Google Ads Expert | Senior PPC Specialist, Hired Directly",
"meta": "Hire a Google Ads expert directly: a senior PPC specialist with 14+ years on the account, working with you instead of through an agency. Flat fee.",
"kicker": "Google Ads expert",
"h1": "A Google Ads expert with 14+ years on the account, hired directly instead of through an agency",
"lead": "Expert and specialist are words every agency uses in its pitch. This page sets out what a senior Google Ads specialist actually does differently, how to check it before you hire one, and how the engagement works when the expert is the person you deal with.",
"service_name": "Google Ads expert services",
"body": """
<section><div class="wrap">
<h2>What a senior specialist does that a generalist or a junior does not</h2>
<ul>
<li><strong>Reads the search terms before touching the bids.</strong> Most waste in lead generation accounts is in what gets counted and in the queries matched, not in the bidding. A specialist starts there.</li>
<li><strong>Treats the automation as a tool with settings, not as a strategy.</strong> Smart Bidding and Performance Max are switched on when the conversion data deserves them and reviewed with brand excluded, so the reported result is real.</li>
<li><strong>Owns the measurement.</strong> GA4, Tag Manager, consent and the CRM are part of the job, because an expert cannot optimize toward a number that is wrong.</li>
<li><strong>Builds the page after the click.</strong> The landing page is usually the largest lever in the account and the one nobody who runs the ads has touched. Here it is included.</li>
<li><strong>Says no.</strong> To budget increases the data does not support, to platforms that do not fit the business, to accounts that need an agency rather than one person.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>How to check a Google Ads expert before hiring one</h2>
<ol class="steps">
<li><div><strong>Ask who will be in the account weekly.</strong> If the answer is a team, ask for the name and the years of experience of the person doing the work. Here the answer is one name, and it is the person you spoke to.</div></li>
<li><div><strong>Ask for a written review before any retainer.</strong> An expert can read your account read-only and tell you in writing what is wrong and what it costs each month. That is the <a href="/google-ads-audit/">Google Ads audit</a>, and it stands on its own.</div></li>
<li><div><strong>Ask how results are reported.</strong> Platform numbers alone are a warning sign. The report should reconcile to your CRM or your orders, with brand and non-brand shown separately.</div></li>
<li><div><strong>Ask what they will not do.</strong> An expert has a scope. Mine is Google, Microsoft, Meta and LinkedIn Ads for businesses spending roughly $3,000 to $80,000 a month, with the exceptions listed on the <a href="/">home page</a>.</div></li>
<li><div><strong>Check the published work.</strong> Named cases where the client allowed it, anonymized where they did not, with the figures and their source stated. <a href="/results/">Results →</a></div></li>
</ol>
</div></section>

<section><div class="wrap">
<h2>Expert, consultant, freelancer: which word applies</h2>
<p>People search for all three and the work is the same person. "Expert" and "specialist" describe depth on the platform; "<a href="/google-ads-consultant/">consultant</a>" describes advice and reviews available without a retainer; "<a href="/freelance-ppc-consultant/">freelancer</a>" describes the independence from an agency. All three are true here, and none of them is the point. The point is that the senior person is the one in the account.</p>
</div></section>

<section><div class="wrap">
<h2>How an engagement with an expert starts</h2>
<p>Read-only access, a fixed-price written review, then your choice: implement it yourselves, hire me for the fixes, or have me run the account month to month with 30 days' notice either way. Fees are flat, set from the scope, never a percentage of spend, and quoted in US dollars, pounds or euros by email from the form.</p>
</div></section>
""",
"faq": [
("How much does a Google Ads expert cost?", "Senior US freelancers commonly quote by the hour or a flat monthly retainer; agencies commonly charge a percentage of spend with a minimum. My fee is flat, set from the scope of the account, and quoted by email from the form. See <a href=\"/pricing/\">pricing</a>."),
("What is the difference between a Google Ads expert and an agency?", "Who does the work. An agency puts an account team between you and the account, usually led by someone junior once the pitch is over. An expert is the person doing the work, and you speak to them directly."),
("Are you Google Partner certified?", "Certifications are earned by spend thresholds as much as by skill and say little about judgment. What you can check is the written review, the published cases and how the first call goes."),
("Can you work alongside our in-house marketer?", "Yes. A common arrangement is a monthly review of the work your team does, with a written note and a call, or a setup that your team then runs. The scope is agreed in writing at the start."),
("Which platforms are you an expert in?", "Google Ads first, including Shopping, Performance Max, YouTube and Demand Gen; then Microsoft Advertising, Meta Ads and LinkedIn Ads, with GA4, Tag Manager and landing pages as part of every engagement."),
],
"related": ["google-ads-consultant", "freelance-ppc-consultant", "google-ads-audit", "google-ads-management"],
},

# ---------------------------------------------------------------- Law firms
{
"slug": "ppc-for-law-firms", "short": "PPC for law firms", "blurb": "Google Ads for attorneys: paying for signed clients, not for people comparing fees at $100 a click.",
"title": "PPC for Law Firms | Google Ads for Attorneys, Run by One Consultant",
"meta": "PPC for law firms: Google Ads by practice area, intake tracked to signed clients, research searches excluded, bar rules respected. Flat fee.",
"kicker": "PPC for law firms",
"h1": "PPC for law firms: paying for signed clients, not for people comparing fees at $100 a click",
"lead": "Legal is the most expensive auction in Google Ads. Personal injury searches in Houston, Dallas or Phoenix average well over $100 a click, and family, immigration and employment searches run from $20 to $80 in most metros. At that price the difference between a firm that profits from Google Ads and one that does not is almost never the bid. It is what gets counted, what gets excluded and the page after the click.",
"service_name": "PPC for law firms",
"body": """
<section><div class="wrap">
<h2>Where law firm accounts waste money</h2>
<ul>
<li><strong>Research searches billed as leads.</strong> "How much does a divorce cost", "can I sue for", "free legal advice", "statute of limitations". These match broad and phrase keywords, cost as much as a client search and almost never sign. Twelve months of search terms read line by line is the first task.</li>
<li><strong>One campaign for the whole firm.</strong> Family, immigration and personal injury share a budget, and the cheapest inquiries take it. Each practice area gets its own campaign, budget and landing page.</li>
<li><strong>A call counted as a client.</strong> Phone clicks and form fills are not signed clients. Call tracking tied to the keyword, intake software recording the outcome, and the case management system feeding back which inquiries became matters are what let Google optimize toward clients.</li>
<li><strong>The firm's homepage as the landing page.</strong> Someone who searched for an immigration attorney should land on a page about immigration law, with the attorney's name, the first step explained and the phone number at the top.</li>
<li><strong>Ads that would not pass the bar.</strong> Outcome claims, "specialist" where the state bar restricts the word, missing disclaimers. State bar advertising rules set what can be said, and the ads are written inside them.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>What a click costs by practice area and metro</h2>
<p>Average cost per click from Google Ads keyword data for the US, October 2026, for the search with the city attached. Market averages, not a forecast.</p>
<table>
<tr><th>Search</th><th>Houston</th><th>Dallas</th><th>Phoenix</th></tr>
<tr><td>personal injury lawyer [city]</td><td>$126.93</td><td>$139.57</td><td>$126.26</td></tr>
</table>
<p>At these prices, 100 clicks cost close to $13,000. If one in eight calls and one in three callers signs, that is about $3,100 per signed case before the fee. If a third of those clicks were research searches that should have been excluded, the real figure was closer to $2,100. That is the arithmetic the account is run on, and it is why the negatives program and the intake tracking come before any bidding change.</p>
</div></section>

<section><div class="wrap">
<h2>What management includes for a law firm</h2>
<ol class="steps">
<li><div><strong>A campaign per practice area</strong>, with exact and phrase match, a negatives program built from the research vocabulary of each area, and location targeting matched to where the firm takes clients and is licensed.</div></li>
<li><div><strong>Measurement to the signed client.</strong> Call tracking, intake outcomes, and the case management system (Clio, MyCase, Filevine, Lawmatics or a spreadsheet) feeding back which inquiries opened a matter, imported to Google Ads as offline conversions. See <a href="/conversion-tracking-setup/">conversion tracking</a>.</div></li>
<li><div><strong>A page per practice area</strong>, built by me, with the attorney, the process, the fee basis, and a phone number and form that work on a phone at lunchtime. See <a href="/landing-pages/">landing pages</a>.</div></li>
<li><div><strong>Local Services Ads alongside Search</strong> where the practice area qualifies, with the Google Screened process handled and the two channels compared on cost per signed client.</div></li>
<li><div><strong>Brand and competitor terms decided, not defaulted.</strong> Whether to bid on the firm's own name depends on who else is bidding on it; competitor bidding is permitted but usually poor value and in some states restricted. Both reviewed monthly.</div></li>
<li><div><strong>Microsoft Advertising</strong> once Google works: a professional audience on work devices, often at a lower cost per inquiry for legal searches. <a href="/microsoft-ads-management/">Microsoft Ads →</a></div></li>
<li><div><strong>A monthly report in signed clients and cost per signed client</strong>, by practice area, alongside the platform numbers so the two can be compared.</div></li>
</ol>
</div></section>

<section><div class="wrap">
<h2>Who this fits</h2>
<p>US and Canadian firms from a few attorneys to mid-size regional practices, spending roughly $5,000 to $80,000 a month, in practice areas where a client is worth several thousand dollars or more: personal injury where the firm handles its own intake, family, immigration, employment, criminal defense, estate planning, business law. Lead resellers and mass-tort aggregators are not a fit. There is no law firm case on this site yet and none will be invented; the <a href="/results/">published cases</a> show the method on other expensive auctions.</p>
</div></section>
""",
"faq": [
("How much should a law firm spend on Google Ads?", "Enough to buy a meaningful number of clicks in your practice area and metro. At $30 to $140 a click, several thousand dollars a month is the floor for a single practice area in a large city, and personal injury needs more. The first call includes this arithmetic for your firm."),
("Can you work within state bar advertising rules?", "Yes. Ads avoid outcome claims and restricted terms, carry the disclaimers your state requires, and your compliance partner signs off the copy before it runs. Where a state requires ad filing or review, that is built into the timeline."),
("Do you handle Local Services Ads?", "Yes, where the practice area qualifies: the Google Screened process, the profile, the budget and the lead disputes, with LSA and Search compared on cost per signed client in the same report."),
("Can you connect Google Ads to our case management system?", "Yes, through an offline conversion import: Clio, MyCase, Filevine, Lawmatics and most systems can export the inquiries that became matters, and a scheduled upload teaches Google which clicks produced clients."),
("How much does PPC management for a law firm cost?", "A flat monthly fee set from the scope: practice areas, platforms and how much landing page and tracking work is included. Never a percentage of spend. Quoted in US dollars by email from the form. See <a href=\"/pricing/\">pricing</a>."),
],
"related": ["google-ads-audit", "google-ads-management", "landing-pages", "conversion-tracking-setup"],
},

# ---------------------------------------------------------------- Home services
{
"slug": "home-services-ppc", "short": "Home services PPC", "blurb": "HVAC, plumbing, roofing, electrical: Google Ads built around booked jobs, with a published case.",
"title": "Home Services PPC | Google Ads for HVAC, Plumbing & Contractors",
"meta": "Home services PPC: Google Ads and Local Services Ads for HVAC, plumbing, roofing and electrical, measured in booked jobs. Houston case: 44% lower CPA.",
"kicker": "Home services PPC",
"h1": "Home services PPC measured in booked jobs, with a published HVAC and plumbing case to show the method",
"lead": "Contractors buy the most expensive local clicks outside legal: $30 to $55 for a plumber or AC repair search in the large Sun Belt metros. The published Houston case on this site cut cost per acquisition by 44% and lifted qualified leads by 60% in that auction. What moved it is on this page.",
"service_name": "Home services PPC",
"body": """
<section><div class="wrap">
<h2>Where contractor accounts waste money</h2>
<ul>
<li><strong>Emergency and planned work in one campaign.</strong> "AC not cooling" at 9 pm in July and "new HVAC system cost" are different customers with different values. Sharing a budget, the cheap emergency clicks take it and the installs never get seen.</li>
<li><strong>A phone call counted as a job.</strong> Wrong numbers, suppliers, job seekers and existing customers all ring the tracked line. Until the office marks which calls were booked, Google optimizes toward whoever calls, not whoever buys.</li>
<li><strong>Service area set to the metro.</strong> A plumber in Katy paying for clicks from Baytown. Radius and ZIP targeting matched to the trucks' actual routes, with bids by area and hour.</li>
<li><strong>Local Services Ads ignored or left to run.</strong> Google Guaranteed leads are often cheaper than Search for emergency work and the two should be compared on cost per booked job, not run by different people.</li>
<li><strong>The homepage as the landing page.</strong> Someone with water on the floor needs the phone number, the response time and the service area in the first screen, not the company history.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>What a click costs by trade and metro</h2>
<p>Average cost per click from Google Ads keyword data for the US, October 2026, for the search with the city attached. Market averages, not a forecast.</p>
<table>
<tr><th>Search</th><th>Houston</th><th>Dallas</th><th>Phoenix</th></tr>
<tr><td>plumber [city]</td><td>$35.53</td><td>$35.66</td><td>$54.16</td></tr>
<tr><td>HVAC repair [city]</td><td>$29.18</td><td>$43.67</td><td>$17.70</td></tr>
<tr><td>roofing company [city]</td><td>$14.44</td><td>$10.66</td><td>$16.74</td></tr>
</table>
<p>The same trade costs very different amounts in neighboring markets: HVAC repair in Dallas costs two and a half times what it does in Phoenix, and a Phoenix plumber pays half as much again as a Houston one. Budgets set from a national average go wrong in both directions. An <a href="/google-ads-audit/">audit</a> prices your own auction before anything is changed.</p>
</div></section>

<section><div class="wrap">
<h2>What moved the Houston account</h2>
<p>An HVAC and plumbing company in Houston, running Google Ads from May 2025 to February 2026, with clicks costing $45 to $80. Cost per acquisition fell 44% and qualified leads rose 60%. The full note, with the source of the figures, is on <a href="/results/">results</a>. The work:</p>
<ol class="steps">
<li><div><strong>Campaigns split by type of job</strong>, so urgent, cheaper work stopped absorbing the budget meant for installs and higher-value repairs.</div></li>
<li><div><strong>Tracking rebuilt</strong> so a booked job and a phone call were different events, with the office marking call outcomes and the booked jobs fed back to Google.</div></li>
<li><div><strong>A weekly pass through the search terms</strong>, with a negatives program that grew every week, and steady tests of ads and landing pages.</div></li>
<li><div><strong>Bids by area and hour</strong>, matched to the trucks' routes and to when emergency calls actually come in.</div></li>
</ol>
</div></section>

<section><div class="wrap">
<h2>What management includes for a contractor</h2>
<ul>
<li><strong>Google Search by service and urgency</strong>, Local Services Ads where the trade qualifies, and <a href="/microsoft-ads-management/">Microsoft Advertising</a> once Google works, compared on cost per booked job.</li>
<li><strong>Call tracking with outcomes</strong>, the booking software (ServiceTitan, Housecall Pro, Jobber and others) feeding booked and completed jobs back as offline conversions. See <a href="/conversion-tracking-setup/">conversion tracking</a>.</li>
<li><strong>One page per service</strong>, built by me, with the phone number, the response time and the service area at the top, loading fast on a phone. See <a href="/landing-pages/">landing pages</a>.</li>
<li><strong>Seasonal budgets</strong> planned in advance: cooling in May, heating in October, storm response when it happens.</li>
<li><strong>A monthly report in booked jobs and cost per booked job</strong>, by service line, alongside the platform numbers.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>Who this fits</h2>
<p>HVAC, plumbing, electrical, roofing, garage door, pest control, restoration and similar contractors in the US and Canada, from a few trucks to regional multi-location companies, spending roughly $3,000 to $60,000 a month. Lead-generation networks that resell contractor leads are not a fit. For smaller budgets, see <a href="/small-business-ppc-management/">Google Ads for small business</a>.</p>
</div></section>
""",
"faq": [
("How much should an HVAC or plumbing company spend on Google Ads?", "Enough to buy a meaningful number of clicks at your metro's price: at $30 to $55 a click, a few thousand dollars a month is the floor for one trade in a large metro, and more during the season. The first call includes this arithmetic for your market."),
("Do you manage Local Services Ads too?", "Yes: the Google Guaranteed process, the profile, the budget, the lead disputes, and the comparison with Search on cost per booked job in the same report."),
("Can you connect Google Ads to ServiceTitan or Housecall Pro?", "Yes, through an offline conversion import: booked and completed jobs with their value exported from the booking software and uploaded on a schedule, so Google learns which clicks became jobs."),
("Do you work with multi-location contractors?", "Yes. Each location gets its own service area, budget and pages, with the shared structure maintained once, and the report broken down by location."),
("How much does home services PPC management cost?", "A flat monthly fee set from the scope: service lines, locations, platforms and how much landing page and tracking work is included. Never a percentage of spend. Quoted in US dollars by email from the form. See <a href=\"/pricing/\">pricing</a>."),
],
"related": ["small-business-ppc-management", "google-ads-audit", "ppc-consultant-houston", "conversion-tracking-setup"],
},

# ---------------------------------------------------------------- Dentists
{
"slug": "google-ads-for-dentists", "short": "Google Ads for dentists", "blurb": "Dental practices: new patients by treatment, tracked to the appointment book, inside Google's health rules.",
"title": "Google Ads for Dentists | New Patients, Tracked to the Chair",
"meta": "Google Ads for dental practices by an independent consultant: campaigns by treatment, tracked to attended appointments, health rules respected.",
"kicker": "Google Ads for dentists",
"h1": "Google Ads for dentists measured in new patients in the chair, not in phone clicks",
"lead": "Dental is one of the most competitive local auctions in healthcare: $12 to $22 a click for a dentist search in the large metros, more for implants and orthodontics. The practices that profit are the ones where the front desk's outcomes reach Google, the campaigns follow the treatments that pay, and the research searches are excluded.",
"service_name": "Google Ads for dentists",
"body": """
<section><div class="wrap">
<h2>Where dental accounts waste money</h2>
<ul>
<li><strong>One campaign for the practice.</strong> Emergency, general, implants, Invisalign and whitening are different patients with different lifetime values. Sharing a budget, the cheap emergency clicks take it and the implant inquiries never get seen.</li>
<li><strong>A call counted as a patient.</strong> Insurance questions, existing patients and wrong numbers ring the tracked line. Until the front desk marks booked and attended, Google optimizes toward whoever calls.</li>
<li><strong>Research searches paid for.</strong> "Does a root canal hurt", "how much do implants cost", "dentist near me open now" from outside the catchment. Excluded, and the budget goes to the searches that name a treatment and a place.</li>
<li><strong>Insurance and financing left off the page.</strong> The two questions every new patient has, answered on the landing page before the form, raise conversion more than any bid change.</li>
<li><strong>Health policy ignored.</strong> Google restricts personalized advertising on health conditions, so remarketing built on treatment pages is not available. The account has to work without it.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>What a click costs by metro</h2>
<p>Average cost per click from Google Ads keyword data for the US, October 2026, for "dentist [city]". Market averages, not a forecast; treatment searches such as implants and orthodontics cost more.</p>
<table>
<tr><th>Search</th><th>Houston</th><th>Dallas</th><th>Phoenix</th></tr>
<tr><td>dentist [city]</td><td>$16.76</td><td>$12.60</td><td>$21.82</td></tr>
</table>
</div></section>

<section><div class="wrap">
<h2>What management includes for a practice</h2>
<ol class="steps">
<li><div><strong>A campaign per treatment line</strong>, with location targeting matched to how far patients travel for each one (a few miles for general, much further for implants), and the research vocabulary excluded.</div></li>
<li><div><strong>Measurement to the chair.</strong> Call tracking with front-desk outcomes, online booking tracked, and the practice management system (Dentrix, Eaglesoft, Open Dental, Curve) feeding attended new-patient appointments back as offline conversions, without sending any health data to Google. See <a href="/conversion-tracking-setup/">conversion tracking</a>.</div></li>
<li><div><strong>A page per treatment</strong>, built by me, with the dentist, the process, insurance and financing answered, the next available appointment and a phone number at the top. See <a href="/landing-pages/">landing pages</a>.</div></li>
<li><div><strong>Local Services Ads and the Business Profile</strong> alongside Search, compared on cost per new patient.</div></li>
<li><div><strong>Meta where it fits</strong>: cosmetic and orthodontic treatments, within Meta's health restrictions, judged on booked consultations. <a href="/meta-ads-management/">Meta Ads →</a></div></li>
<li><div><strong>A monthly report in new patients and cost per new patient</strong>, by treatment, alongside the platform numbers.</div></li>
</ol>
</div></section>

<section><div class="wrap">
<h2>Who this fits</h2>
<p>Single and multi-location dental practices in the US and Canada, general and specialist, and DSOs that want one senior person rather than a vendor's account team, spending roughly $3,000 to $40,000 a month. Healthcare is among the sectors I have worked in over 14 years; there is no dental case published on this site and none will be invented. The method is the one that moved the <a href="/results/">Houston home services account</a>, applied to a practice: split by service, track the real outcome, read the search terms every week.</p>
</div></section>
""",
"faq": [
("How much should a dental practice spend on Google Ads?", "Enough to buy a meaningful number of clicks in your metro and treatment: at $12 to $22 for a general search and more for implants, a few thousand dollars a month is the floor in a large city. The first call includes this arithmetic for your practice."),
("Can you connect Google Ads to our practice management software?", "Usually, through an offline conversion import: Dentrix, Eaglesoft, Open Dental and Curve can export which new inquiries booked and attended, without any clinical data leaving the practice. Where there is no export, front-desk outcomes from call tracking do most of the job."),
("What about HIPAA?", "No protected health information goes to Google or Meta. Conversions are sent as outcomes (booked, attended) with hashed contact data only where enhanced conversions are used, and the setup is documented for your compliance officer. Your business associate agreements with your software vendors are unaffected."),
("Do you work with DSOs and multi-location groups?", "Yes. Each location gets its own catchment, budget and pages, the structure is maintained once, and the report is broken down by location and treatment."),
("How much does Google Ads management for a dentist cost?", "A flat monthly fee set from the scope: treatments, locations, platforms and how much landing page and tracking work is included. Never a percentage of spend. Quoted in US dollars by email from the form. See <a href=\"/pricing/\">pricing</a>."),
],
"related": ["healthcare-ppc", "google-ads-audit", "landing-pages", "conversion-tracking-setup"],
},

# ---------------------------------------------------------------- Healthcare
{
"slug": "healthcare-ppc", "short": "Healthcare PPC", "blurb": "Clinics, practices and health brands: inquiries that become appointments, within Google's health policies.",
"title": "Healthcare PPC | Google Ads for Clinics, Practices and Health Brands",
"meta": "Healthcare PPC by an independent consultant: Google and Meta Ads for clinics and health brands, measured in booked appointments, within health policies.",
"kicker": "Healthcare PPC",
"h1": "Healthcare PPC measured in booked appointments, run inside the rules the platforms apply to health advertisers",
"lead": "Healthcare is a crowded auction with its own constraints: restricted remarketing, certification for some categories, claims the FTC and the platforms do not allow, HIPAA, and patients who research for weeks before booking. The accounts that work are the ones where the measurement reaches the appointment book and the campaigns respect the research journey instead of paying for it twice.",
"service_name": "Healthcare PPC",
"body": """
<section><div class="wrap">
<h2>What is different about healthcare accounts</h2>
<ul>
<li><strong>Policy limits the tools.</strong> Google restricts personalized advertising for health conditions, so remarketing lists built on condition pages are not available; some categories (prescription drugs, addiction treatment, certain procedures) require certification before ads run; Meta has its own health and wellness data restrictions. The structure has to work without the tools other sectors lean on.</li>
<li><strong>Claims are regulated.</strong> Outcome claims, before-and-after imagery for some procedures, and anything that implies a guarantee fall under the FTC and, for drugs and devices, the FDA. Copy is written inside those rules and your clinical or compliance lead signs it off.</li>
<li><strong>Research searches dominate.</strong> "Symptoms of", "is it normal", "does insurance cover" are expensive, well-meaning and do not book. They are excluded, and the budget goes to the searches that name a treatment, a provider type or a location.</li>
<li><strong>The conversion is an appointment, not a form.</strong> The front desk answers the phone; the scheduling system knows who attended. Until those feed back, Google optimizes toward whoever fills in a form, including the people who never show up.</li>
<li><strong>HIPAA shapes the measurement.</strong> No protected health information goes to the ad platforms. Conversions are outcomes, not diagnoses, and the setup is documented.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>What management includes</h2>
<ol class="steps">
<li><div><strong>Structure by service line and location.</strong> A campaign per service (orthopedics, fertility, dermatology, behavioral health, diagnostics, urgent care) with location targeting matched to how far patients travel for each, and the research vocabulary excluded.</div></li>
<li><div><strong>Measurement to the appointment.</strong> Call tracking with front-desk outcomes, the scheduling or practice management system feeding booked and attended appointments back as offline conversions, consent handled, and a privacy setup that keeps health data out of the ad platforms. See <a href="/conversion-tracking-setup/">conversion tracking</a>.</div></li>
<li><div><strong>Pages built for a worried person.</strong> One page per service with the provider, the process, insurance and cost answered, the next available appointment and a phone number at the top, loading fast on a phone. See <a href="/landing-pages/">landing pages</a>.</div></li>
<li><div><strong>Meta where it fits.</strong> Awareness and remarketing for elective services, within Meta's health restrictions, judged on booked consultations rather than on form fills. <a href="/meta-ads-management/">Meta Ads →</a></div></li>
<li><div><strong>Reporting in appointments.</strong> Cost per booked and attended appointment by service line, alongside the platform numbers.</div></li>
</ol>
</div></section>

<section><div class="wrap">
<h2>Who this fits</h2>
<p>US and Canadian clinics and practice groups, specialty practices, diagnostics and imaging, behavioral health providers working within the certification rules, med spas and aesthetics within the claims rules, and health brands selling direct. Typically $3,000 to $60,000 a month across Google and Meta. Healthcare and pharma are among the sectors I have worked in over 14 years; no patient-facing case is published on this site, and none will be invented. For dental practices specifically, see <a href="/google-ads-for-dentists/">Google Ads for dentists</a>.</p>
</div></section>
""",
"faq": [
("Can you run Google Ads for a clinic given the health policies?", "Yes. The restrictions remove some tools (condition-based remarketing, some audience features) and require certification for certain categories, including addiction treatment and prescription drugs. The account is built to work within that, and the certification process is handled with you where it applies."),
("How do you handle HIPAA?", "No protected health information goes to Google or Meta. Conversions are sent as outcomes (booked, attended) with hashed contact data only where enhanced conversions are used; tags on pages that could reveal a condition are reviewed; and the setup is documented for your compliance officer. Where your counsel prefers server-side tagging with filtering, that is how it is built."),
("Can you connect Google Ads to our scheduling system?", "Usually, through an offline conversion import from the scheduling or practice management system, exporting which inquiries booked and attended without clinical data. Where there is no export, front-desk outcomes from call tracking do most of the job."),
("Do you work with med spas and aesthetics?", "Yes, within the claims rules: no outcome guarantees, before-and-after imagery only where the platform allows it, and copy signed off by your clinical lead."),
("How much does healthcare PPC management cost?", "A flat monthly fee set from the scope: service lines, locations, platforms and how much landing page and tracking work is included. Never a percentage of spend. Quoted in US dollars by email from the form. See <a href=\"/pricing/\">pricing</a>."),
],
"related": ["google-ads-for-dentists", "google-ads-audit", "conversion-tracking-setup", "landing-pages"],
},

# ---------------------------------------------------------------- SaaS
{
"slug": "saas-ppc", "short": "SaaS PPC", "blurb": "Google and LinkedIn Ads for software companies, measured in qualified pipeline and CAC payback, with a published case.",
"title": "SaaS PPC Consultant | Google & LinkedIn Ads Measured in Pipeline",
"meta": "SaaS PPC by an independent consultant: Google and LinkedIn Ads connected to the CRM and reported in pipeline and CAC payback. Published case: 600% growth.",
"kicker": "SaaS PPC",
"h1": "SaaS PPC measured in qualified pipeline and CAC payback, by one consultant across Google and LinkedIn",
"lead": "Software companies have the cleanest data in paid media and often the worst use of it. The CRM knows which trials became customers and what they pay; the ad platforms are optimizing toward sign-ups. Connecting the two is most of the job, and it is where a SaaS account starts here.",
"service_name": "SaaS PPC management",
"body": """
<section><div class="wrap">
<h2>Where SaaS accounts leak</h2>
<ul>
<li><strong>Optimizing toward the top of the funnel.</strong> Free trials, demo requests and content downloads are easy to count and cheap to buy. Without product-qualified or sales-accepted stages flowing back, the platforms buy the cheapest sign-ups, which churn.</li>
<li><strong>Competitor and category terms treated the same.</strong> "[Competitor] alternative" and "best [category] software" bring different buyers at different stages and should sit in separate campaigns with separate pages and expectations.</li>
<li><strong>Brand taking the credit.</strong> Performance Max and broad match drift onto the brand name and the reported CAC looks wonderful. Brand is isolated, and the non-brand number is the one managed.</li>
<li><strong>LinkedIn judged on form fills.</strong> A $12 click on a Head of Operations who downloads a benchmark is not pipeline. LinkedIn is judged on qualified opportunities from the CRM or not at all.</li>
<li><strong>Payback ignored.</strong> A customer acquired at $1,200 on a $49 monthly plan is a two-year payback before gross margin. The targets by plan and segment come from that arithmetic, not from a blended CAC.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>What management includes</h2>
<ol class="steps">
<li><div><strong>Measurement to the CRM.</strong> GA4 and Tag Manager with a user ID, HubSpot or Salesforce stages (MQL, SQL, opportunity, closed won, with amount) imported to Google Ads and LinkedIn as offline conversions, so the platforms optimize toward revenue. See <a href="/conversion-tracking-setup/">conversion tracking</a>.</div></li>
<li><div><strong>Google Search by intent.</strong> Category, problem, integration and competitor campaigns, each with its own page and its own target, brand kept separate, Performance Max only with brand excluded and only once the conversion data deserves it.</div></li>
<li><div><strong>LinkedIn for the accounts that are not searching.</strong> Named account lists from the CRM, firmographic and title targeting, offers built for a buyer with a problem this quarter, conversation and document ads tested against a control. <a href="/linkedin-ads-management/">LinkedIn Ads →</a></div></li>
<li><div><strong>YouTube and Demand Gen</strong> for product demos and founder pieces, judged on the lift in branded search and on conversions, not on views. <a href="/youtube-ads-management/">YouTube Ads →</a></div></li>
<li><div><strong>Pages per intent</strong>, built by me: comparison pages, integration pages, use-case pages, with the trial or demo form that asks the one qualifying question. See <a href="/landing-pages/">landing pages</a>.</div></li>
<li><div><strong>Reporting in pipeline and payback.</strong> Qualified pipeline, closed-won revenue and CAC payback by channel and segment, alongside the platform numbers.</div></li>
</ol>
</div></section>

<section><div class="wrap">
<h2>A published SaaS result</h2>
<p>Pontomais, a time-tracking and HR software startup, grew sales by 600% in eight months with paid media, most of it Google, run by me. The figures come from the company's own sales reporting at the time; the full note is on <a href="/results/">results</a>. The market was Brazil and the currency was different, but the method was the one above: the CRM connected first, campaigns split by intent, brand isolated, and budget following measured pipeline. Intuit QuickBooks and Skillshare are among the subscription brands I have worked on in agency and in-house roles.</p>
</div></section>

<section><div class="wrap">
<h2>Who this fits</h2>
<p>B2B software companies in the US, Canada and anywhere that works in English, from seed to Series B or established vertical SaaS, spending roughly $5,000 to $80,000 a month across Google and LinkedIn, with a CRM in use and a sales or product-led motion that can report stages. Consumer apps measured on installs are not a fit. For the wider B2B picture, see <a href="/b2b-ppc/">B2B PPC</a>.</p>
</div></section>
""",
"faq": [
("What CAC should a SaaS company expect from Google Ads?", "No honest number exists before the account and the CRM are read together. What is measurable from the first month is CAC by channel and segment against your plan prices, which gives payback, and that is the figure the targets are set from."),
("Can you connect Google Ads and LinkedIn to HubSpot or Salesforce?", "Yes. Offline conversion import from CRM stages with amounts, enhanced conversions for leads, and a user ID in GA4 so the journey from click to closed won is visible. The setup is documented so your RevOps team owns it."),
("Should we bid on competitor names?", "Usually yes, in a separate campaign with its own page and a target that reflects the lower conversion rate. Comparison pages that are honest about where the competitor is better convert well and stay within the advertising rules."),
("Do you run product-led growth accounts?", "Yes, provided product-qualified signals (activation, team invites, usage thresholds) can be fed back. Without them the platforms optimize toward sign-ups that never activate, and the budget is better spent elsewhere."),
("How much does SaaS PPC management cost?", "A flat monthly fee set from the scope: platforms, markets, campaigns and how much landing page and tracking work is included. Never a percentage of spend. Quoted in US dollars, pounds or euros by email from the form. See <a href=\"/pricing/\">pricing</a>."),
],
"related": ["b2b-ppc", "linkedin-ads-management", "conversion-tracking-setup", "landing-pages"],
},

# ---------------------------------------------------------------- Houston
{
"slug": "ppc-consultant-houston", "short": "PPC consultant, Houston", "blurb": "For Houston businesses, with a published Houston case, delivered remotely on Central time.",
"title": "PPC Consultant Houston | Google Ads With a Published Houston Case",
"meta": "Independent PPC consultant for Houston businesses: Google, Microsoft, Meta and LinkedIn Ads on Central time, with a published Houston case. Flat fee.",
"kicker": "PPC consultant Houston",
"h1": "PPC consultant for Houston businesses, with a published Houston case and calls on Central time",
"lead": "Independent PPC consultant for Houston companies: 14+ years running Google, Microsoft, Meta and LinkedIn Ads, a published Houston HVAC and plumbing case with a 44% lower cost per acquisition, calls on Central time, and a fee that does not carry a Galleria office inside it.",
"service_name": "PPC consultancy for Houston businesses",
"body": """
<section><div class="wrap">
<h2>What Houston accounts usually need</h2>
<p>Houston is the fourth-largest metro in the country and one of the most spread out: a service business in Katy, Sugar Land, The Woodlands and Pearland is running four different auctions, not one. Energy, healthcare, legal and the trades all buy paid search seriously, and the summer makes home services one of the most expensive local markets in the United States.</p>
<ul>
<li><strong>Location targeting that matches the map.</strong> The metro is eight counties and a 60-mile drive across. ZIP and radius targeting matched to where you actually serve, with bids by area and hour, instead of one pin downtown.</li>
<li><strong>Inquiry quality over inquiry count.</strong> Call tracking tied to the keyword, forms that qualify, and the CRM or booking software feeding back which inquiries became customers, so bidding learns from revenue.</li>
<li><strong>A landing page per service.</strong> Not the homepage, and not one contact page for twelve services.</li>
<li><strong>Season planned in advance.</strong> Cooling budgets in May, storm response when it happens, and the quieter months used for installs and planned work.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>What a click costs in Houston compared with other metros</h2>
<p>Average cost per click for the same search with the city name attached, from Google Ads keyword data for the US, October 2026. Market averages, not a forecast for your account.</p>
<table>
<tr><th>Search</th><th>Houston</th><th>Dallas</th><th>Phoenix</th></tr>
<tr><td>plumber [city]</td><td>$35.53</td><td>$35.66</td><td>$54.16</td></tr>
<tr><td>HVAC repair [city]</td><td>$29.18</td><td>$43.67</td><td>$17.70</td></tr>
<tr><td>roofing company [city]</td><td>$14.44</td><td>$10.66</td><td>$16.74</td></tr>
<tr><td>dentist [city]</td><td>$16.76</td><td>$12.60</td><td>$21.82</td></tr>
<tr><td>personal injury lawyer [city]</td><td>$126.93</td><td>$139.57</td><td>$126.26</td></tr>
<tr><td>IT support [city]</td><td>$88.94</td><td>$42.06</td><td>$17.86</td></tr>
</table>
<p>Houston is not the most expensive metro for everything: HVAC repair costs a third less than in Dallas, and a plumber click costs far less than in Phoenix. IT support is the outlier, at more than twice the Dallas price. The lesson is to price your own auction rather than assume, which is one of the first things an <a href="/google-ads-audit/">audit</a> does.</p>
</div></section>

<section><div class="wrap">
<h2>The published Houston case</h2>
<p>An HVAC and plumbing company in Houston, Google Ads from May 2025 to February 2026, clicks costing $45 to $80. Cost per acquisition fell 44% and qualified leads rose 60%. The figures come from the Google Ads account and the reports delivered during the engagement; nobody independent has audited them, and the full note is on <a href="/results/">results</a>. What moved it:</p>
<ul>
<li>Campaigns split by type of job, so urgent, cheaper work stopped absorbing the budget meant for installs and higher-value repairs.</li>
<li>Tracking rebuilt so a booked job and a phone call were different events, with the office marking outcomes.</li>
<li>A weekly pass through the search terms and steady tests of ads and landing pages.</li>
</ul>
<p>For a Houston law firm or clinic the same three moves apply: separate the practice areas or service lines sharing one campaign, count a signed client or an attended appointment rather than a call, and cut the research searches that eat budget at the prices in the table. <a href="/home-services-ppc/">Home services PPC →</a></p>
</div></section>

<section><div class="wrap">
<h2>Houston sectors where this work is already familiar</h2>
<div class="cols">
<div class="card"><h3>Home services</h3><p>HVAC, plumbing, roofing, electrical, pest control and restoration across the metro. Emergency versus planned work, call tracking that separates a booked job from a ring, bids by ZIP and hour, and Local Services Ads compared with Search. The published case is this pattern.</p></div>
<div class="card"><h3>Healthcare</h3><p>The Texas Medical Center anchors the largest medical cluster in the world, and the private practices around it compete hard for the same searches. Campaigns by service line, measurement to the attended appointment, HIPAA-safe tracking. <a href="/healthcare-ppc/">Healthcare PPC →</a></p></div>
<div class="card"><h3>Legal and professional services</h3><p>Personal injury at $127 a click, immigration, family and energy-sector business law. A campaign per practice area, intake tracked to the signed client, and the research searches excluded. <a href="/ppc-for-law-firms/">PPC for law firms →</a></p></div>
</div>
</div></section>

<section><div class="wrap">
<h2>Consultant or Houston agency</h2>
<table>
<tr><th></th><th>Independent consultant</th><th>Houston PPC agency</th></tr>
<tr><td>Who does the work</td><td>The person you spoke to first</td><td>An account team, often led by someone junior once the pitch is over</td></tr>
<tr><td>How it is charged</td><td>Flat monthly fee, never a share of spend</td><td>Retainer or a percentage of spend</td></tr>
<tr><td>Minimum term</td><td>None; 30 days' notice</td><td>Commonly 6 to 12 months</td></tr>
<tr><td>Landing pages and tracking</td><td>Included, by the same person</td><td>Often another team or an extra</td></tr>
<tr><td>Meetings</td><td>Remote, calls on Central time, written updates</td><td>In person if you want them</td></tr>
<tr><td>Better when</td><td>One business, one senior person accountable</td><td>Many markets, heavy creative or regular face-to-face</td></tr>
</table>
<p>Engagements start with a fixed-price <a href="/google-ads-audit/">audit</a> or, for a new account, a <a href="/google-ads-setup/">setup</a>; either is credited against the first month of <a href="/google-ads-management/">management</a>.</p>
</div></section>
""",
"faq": [
("Do you meet clients in Houston?", "The engagement is remote as standard: calls on Central time and written updates. I work from Curitiba, Brazil, two hours ahead of Houston for most of the year. If regular face-to-face meetings matter to you, an agency with a Houston office will suit you better, and I would rather say so at the start."),
("Do you work with businesses outside Houston?", "Yes, across the US and Canada, and with companies from any country that work in English. This page exists because Houston businesses search for a Houston consultant and because the published case is a Houston account; the service and the terms are the same everywhere."),
("Do you cover the suburbs?", "Yes: Katy, Sugar Land, The Woodlands, Pearland, Cypress, Spring, Pasadena, League City and the rest of the metro, with location targeting and bids set to how your business actually serves each area."),
("What do Houston PPC agencies and consultants charge?", "Agencies commonly charge a percentage of spend with a monthly minimum; senior freelancers quote by the hour or a flat retainer. My fee is flat, set from the scope of the account, and quoted in US dollars by email from the form. See <a href=\"/pricing/\">pricing</a>."),
],
"related": ["home-services-ppc", "google-ads-audit", "google-ads-management", "results"],
},
# ---------------------------------------------------------------- Google Ads consultation (one-off session)
{
"slug": "google-ads-consultation", "short": "Google Ads consultation", "blurb": "A one-off working session on your account, with written notes, before or instead of a retainer.",
"title": "Google Ads Consultation | One-Off PPC Session With Written Notes",
"meta": "Book a Google Ads consultation: one working session on your account with a senior independent consultant, written notes afterwards. Fixed price.",
"kicker": "Google Ads consultation",
"h1": "A Google Ads consultation: one working session on your account, with written notes, before or instead of a retainer",
"lead": "Not every account needs an audit or a retainer. Sometimes a business needs a senior person to look at the account for an hour, answer the three questions that have been going around for months, and write down what to do next. That is the consultation, and it is the smallest way to work with me.",
"service_name": "Google Ads consultation",
"body": """
<section><div class="wrap">
<h2>When a consultation is the right size</h2>
<ul>
<li><strong>A decision is pending.</strong> Whether to move to Performance Max, whether to take the agency's proposal, whether the budget increase is justified, whether to bid on the brand. A second opinion from someone with no retainer to win.</li>
<li><strong>An in-house marketer wants a senior check.</strong> You run the account yourself and want an experienced pair of eyes on the structure, the tracking and the search terms before the next quarter.</li>
<li><strong>Something broke.</strong> Conversions stopped recording, the account was suspended, spend doubled overnight, and you need the cause and the fix without a six-week engagement.</li>
<li><strong>You are choosing a vendor.</strong> You have two agency proposals and want them read by someone who runs accounts, with the questions to ask each one.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>How the consultation works</h2>
<ol class="steps">
<li><div><strong>Before the call.</strong> You send the form with the spend band, the platforms and the questions. If the account is live, read-only access to Google Ads and GA4 so the hour is spent on answers rather than on screen-sharing.</div></li>
<li><div><strong>The session.</strong> A video call of about an hour, in a US morning or early afternoon, working through the account and your questions in order of money at stake. Recorded if you want it.</div></li>
<li><div><strong>Written notes within two working days.</strong> What was found, what to do, in what order, and what to measure to know it worked. Written so your team or your agency can act on it.</div></li>
<li><div><strong>Credited if it grows.</strong> If the consultation becomes a <a href="/google-ads-audit/">full audit</a> or <a href="/google-ads-management/">management</a> within 60 days, the consultation fee is credited against it.</div></li>
</ol>
</div></section>

<section><div class="wrap">
<h2>Consultation, audit or management</h2>
<table>
<tr><th></th><th>Consultation</th><th>Audit</th><th>Management</th></tr>
<tr><td>What it is</td><td>One working session plus notes</td><td>A full written review of every platform in scope</td><td>Running the account month to month</td></tr>
<tr><td>Time</td><td>About an hour, notes within two working days</td><td>5 to 7 working days</td><td>Ongoing, 30 days' notice either way</td></tr>
<tr><td>Best for</td><td>A decision, a second opinion, a broken thing, an in-house check</td><td>Knowing everything that is wrong and what it costs</td><td>Having the senior person do the work</td></tr>
<tr><td>Price</td><td>Fixed, quoted from the form</td><td>Fixed, set from spend, campaigns and platforms</td><td>Flat monthly fee, set from scope</td></tr>
<tr><td>Credited against</td><td>An audit or management within 60 days</td><td>The first month of management</td><td></td></tr>
</table>
<p>How each is priced, with market ranges, is on <a href="/pricing/">pricing</a>.</p>
</div></section>

<section><div class="wrap">
<h2>What a consultation is not</h2>
<p>It is not a sales call dressed as advice: the fee is the same whether or not you go on to work with me, and most consultations end with the notes. It is not a free audit; those are discussed on the <a href="/google-ads-audit/">audit page</a>, with the reasons they are a poor idea. And it is not Google Ads training from the ground up; it assumes someone on your side runs or oversees the account already.</p>
</div></section>
""",
"faq": [
("How much does a Google Ads consultation cost?", "A fixed fee quoted by email from the form within one working day, in US dollars, pounds or euros. It is credited against an audit or the first month of management if either follows within 60 days. See <a href=\"/pricing/\">pricing</a> for how everything is priced."),
("Can we book more than one session?", "Yes. Some in-house teams book a session each month or each quarter as a standing review; that is agreed in writing after the first one, with the same notes each time."),
("Do you need access to our account for a consultation?", "It helps: read-only access to Google Ads and GA4 beforehand means the hour goes on answers. Without access, the session works from your screen share and your questions, and the notes say what to check."),
("Which platforms can the consultation cover?", "Google Ads (Search, Shopping, Performance Max, YouTube, Demand Gen), Microsoft Advertising, Meta Ads and LinkedIn Ads, plus GA4, Tag Manager and landing pages."),
("What time zones work for the call?", "I work from Curitiba, Brazil, one to four hours ahead of US time zones, so a US morning or early afternoon works for both of us. UK and Irish businesses have the same session on <a href=\"https://ppcconsultancy.uk/ppc-consultation/\" rel=\"noopener\">ppcconsultancy.uk</a>, quoted in pounds."),
],
"related": ["google-ads-audit", "google-ads-consultant", "google-ads-management", "pricing"],
},
]
