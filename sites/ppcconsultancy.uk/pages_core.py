# Core pages for ppcconsultancy.uk. British English throughout. {{email}} and {{brands}} are filled by build.py.

NOT_FOR = """
<section id="fit"><div class="wrap">
<h2>Who this is for, and who it is not</h2>
<div class="cols">
<div class="card"><h3>A good fit</h3><ul>
<li>B2B and SaaS, professional services, healthcare, home and trade services, and online retail.</li>
<li>Spending roughly £2,000 to £60,000 a month across Google, Microsoft or Meta.</li>
<li>An owner or marketing manager who wants one senior person accountable for the result, not an account manager relaying messages.</li>
<li>Accounts where tracking is doubtful and the landing page has never been touched by whoever runs the ads.</li>
</ul></div>
<div class="card"><h3>Not a fit</h3><ul>
<li>Online stores with tens of thousands of products and daily feed operations, where the feed alone is a full-time job. I will say so rather than run it half well.</li>
<li>Accounts that need a creative production line for paid social. I run the media; volume creative comes from your designer or a studio.</li>
<li>Anyone looking for the cheapest possible pair of hands. There are marketplaces for that, and they are the right answer for some accounts.</li>
</ul></div>
</div>
</div></section>
"""

FAQ_GROUPS = [
("ppc", "PPC and Google Ads", [
("choosing", "Choosing who runs your PPC", [
("freelancer-specialist-consultant", "PPC freelancer, specialist or consultancy: which one am I actually hiring?",
"""Through this site you hire one independent consultant, which in practice covers all three labels. Specialist signals depth on the platforms, consultant means reviews and advice are available without a retainer, and freelancer means no agency sits between us. Here they all describe the same person, who audits, builds and runs your accounts. A consultancy usually implies a firm; this one has a single consultant. More on <a href="/ppc-specialist/">PPC specialist</a>."""),
("agency-or-consultant-uk", "Should a UK business hire a PPC agency or an independent consultant?",
"""It depends on scale and complexity. One company spending from a few thousand to around £60,000 a month, mostly on lead generation, usually suits a consultant, while several countries, languages or a heavy creative pipeline suit an agency. Before choosing, ask who touches the account each week, how the fee is calculated, whether landing pages and tracking are in scope, and what happens if you leave. The full comparison, bias declared, is on <a href="/agency-vs-consultant/">agency vs consultant</a>."""),
("point-me-to-an-agency", "When would you tell me to go to an agency instead?",
"""When the account needs more than one pair of hands. That includes spend well above £60,000 a month across several platforms, multi-country campaigns needing native-language copy, paid social where creative production is the bottleneck, procurement that demands a team, insurance levels and SLAs, and shops with tens of thousands of products and daily feed work. I would rather say so on the first call than run the account half well. See <a href="/agency-vs-consultant/">agency vs consultant</a>."""),
("cheaper-than-agency", "Is an independent consultant cheaper than a PPC agency?",
"""Usually, for the same account, because no account manager, office or margin layer sits between you and the work. Experienced consultants overlap with small agencies at the upper end, so the gap is not always large. The cheapest route is a marketplace freelancer, which is a different product: whoever wins the bid, typically paid by the hour or per task, with tracking and landing pages outside the brief. See <a href="/ppc-freelancer/">PPC freelancer</a>."""),
("anyone-else-on-account", "Does anyone besides you ever work on my account?",
"""No. I run every account personally, and nothing is handed to subcontractors or juniors after the first call. If a project needs design or development beyond what I build myself, for example original illustration or a change only your developer can make, you are told beforehand and the specialist is named. Search terms, bids, tracking, pages and reports remain with me throughout. See <a href="/about/">About</a>."""),
("vetting-checklist", "What should I ask a PPC freelancer before signing anything?",
"""Six questions separate an operator from a profile. Who will actually be in the account? Whose accounts will the campaigns live in, and who holds admin access? How are phone calls, spam and duplicated conversions measured? What happens in the first month? How do you charge, and for how long? Can I see a sample of your reporting? Good answers start with tracking and wasted spend, and keep everything in your name. See <a href="/ppc-freelancer/">PPC freelancer</a>."""),
("with-our-team", "Can you work next to our marketing manager, or alongside the agency that makes our creative?",
"""Yes, both arrangements are common. You can hand over the whole account, or keep your own marketer on the daily work and bring me in for an audit, a second opinion or a regular review. Where a separate agency already makes your Meta creative, it can carry on doing so while I handle the media and measurement against a test plan we all share. Advisory-only support suits teams that prefer to run their own accounts. See <a href="/ppc-management/">PPC management</a>."""),
]),
("fees", "Fees, model and quotes", [
("how-you-price", "How do you price PPC management?",
"""With a flat monthly fee set by the scope of the work, never a share of your media. Scope means the platforms, campaigns and markets involved, plus the landing pages and tracking the account needs. Audits, set-ups and tracking rebuilds are fixed project fees. Every quote is in pounds, ex VAT, and arrives by email within one working day of the form; a firm figure needs read-only access or a short call. See <a href="/pricing/">pricing</a>."""),
("packages", "Do you sell fixed PPC packages?",
"""No. There is no rate card or bundle to choose from, because two accounts with the same spend can need very different amounts of work. The fee is built for your account from its platforms, markets, campaigns and the landing page and tracking work involved. What is fixed in advance is the model: a flat monthly fee for management and a single fixed fee for each defined project. See <a href="/pricing/">pricing</a>."""),
("minimum-spend", "Is there a minimum monthly ad spend?",
"""Not a hard one, but below about £2,000 a month a retainer rarely pays for itself. At that level, a fixed-price set-up you then run yourself, or an audit your own team implements, is usually the honest recommendation. Above it, lean monthly management with tracking and landing page fixes included becomes worthwhile. The options by budget are laid out on <a href="/google-ads-small-business/">Google Ads for small business</a>."""),
("onboarding-fee", "Do I pay anything up front before monthly management begins?",
"""Only the fixed fee for the first piece of work, and that is credited if management follows. There is no onboarding fee. Existing accounts start with an audit and new ones with a set-up; whichever applies is priced in pounds, ex VAT, and deducted from the first month of management. After that, you pay a flat monthly fee, one month at a time. See <a href="/pricing/">pricing</a>."""),
("quote-turnaround", "How quickly will I get a quote, and do I need a call for it?",
"""Within one working day, often the same day, and no call is needed for a range. The form asks for your spend band, platforms and what is going wrong, and the written reply comes by email from me, not from a sales team. A firm figure needs read-only access or a short call. There is no chaser sequence: if you do not reply, I take it that the timing is wrong. See <a href="/contact/">contact</a>."""),
]),
("audit", "The PPC audit", [
("audit-deliverables", "What do I receive at the end of a PPC audit?",
"""A plain-English report that ranks each finding by what it is costing, puts a monthly pound figure on it where possible, and says what the fix is, who should carry it out and how to check it worked. Alongside it come a 30, 60 and 90-day action plan, a walkthrough call lasting up to an hour, and a month of email questions while the changes go in. Expect it five to seven working days after access. See <a href="/ppc-audit/">PPC audit</a>."""),
("audit-price-credit", "How is the audit priced, and is the fee credited if I carry on?",
"""With a single fixed fee worked out from your monthly spend, campaign count and the platforms involved, and yes, all of it is credited against your first month of management if you continue. You receive the figure in pounds, ex VAT, by email within one working day of sending the form, and no call is required. It stays the same whether or not you hire me afterwards. See <a href="/ppc-audit/">PPC audit</a>."""),
("free-audit", "Why pay for an audit when agencies offer free ones?",
"""Because a free audit is written to win a retainer, and a paid one is written to tell you where the money goes. Agency audits are often produced by a sales team from an automated script and rarely conclude that the account is fine. An independent paid audit can say your current set-up is sound and list the few remaining gains, and you can hand it to your own team or agency to implement. See <a href="/ppc-audit/">PPC audit</a>."""),
("judge-my-agency", "Can you give me an honest view of my current agency's work?",
"""Yes, in writing, with no retainer of my own to win by criticising them. A fair review that finds the agency competent is still useful: it lists the remaining gains and gives you specific questions for your next meeting with them. If the work falls short, the report shows where and what it is costing, so the conversation rests on evidence rather than impressions. See <a href="/google-ads-consultant/">Google Ads consultant</a>."""),
]),
("running", "Running the account", [
("first-month", "What do you do in the first four weeks on my account?",
"""Week one is read-only: every conversion action checked against what your business counts as a lead, plus the last 90 days of search terms. Weeks two and three fix the tracking first and then cut the waste, with every change written down so it can be undone. Week four brings a written report on what changed, what it should do and what comes next, whether structure, landing pages or testing. See <a href="/ppc-freelancer/">PPC freelancer</a>."""),
("who-keeps-what", "If we part ways, who keeps the accounts, the data and the history?",
"""You do, all of it. Google Ads, Microsoft, Meta, GA4 and Tag Manager sit in your accounts with admin rights staying with you, and I am added as a user. When we stop, you remove my access and keep the campaigns, conversion actions, tags, pages and their full history. Nothing has to be migrated, and 30 days' written notice from either side ends the arrangement. See <a href="/ppc-management/">PPC management</a>."""),
("monthly-report-uk", "What will I see in the monthly report, and in which currency?",
"""Cost per enquiry, cost per qualified enquiry, revenue where it can be measured, and what changed and why, all in pounds. The report is written in plain English for whoever pays the bills, with a shared dashboard for the figures between reports. Platform numbers are shown next to your CRM or order data rather than on their own, and the month closes with a call to agree the next tests. See <a href="/ppc-management/">PPC management</a>."""),
("results-timing", "How soon should I expect results?",
"""The first month tends to bring the quickest gains, since it is spent repairing tracking and removing wasted spend. Structural changes, new landing pages and tests take longer to show up in the numbers. I will not quote a figure before reading the account; instead you get a fixed sequence, measurement first and testing last, and a written note after each stage explaining what changed and what it did. See <a href="/results/">results</a>."""),
("start-uk", "How quickly can you take the account on?",
"""An audit can usually begin within a week of your go-ahead. Monthly management depends on capacity, since the client list is kept deliberately short; if I cannot take your account on within a month, I will tell you up front rather than accept it and let it wait. New accounts start with a set-up instead of an audit, priced as a fixed fee. See <a href="/ppc-management/">PPC management</a>."""),
("platforms-uk", "Do you run Microsoft Ads and Meta as well as Google?",
"""Yes, alongside Google Ads, which remains the core. Microsoft Advertising is usually added once Google works, as a modest increase to the fee; in the accounts I have run, the same conversion has often cost less there, with an older, more professional UK audience. Meta covers Facebook and Instagram for businesses whose offer can be understood in a feed, with creative from your designer or a studio. See <a href="/microsoft-ads-management/">Microsoft Ads</a>."""),
("ecommerce-uk", "Do you take on online shops and Google Shopping?",
"""Yes. UK and Irish shops on Shopify, WooCommerce, Magento or BigCommerce are welcome. The work starts with Merchant Centre and the feed, runs Shopping and Performance Max by margin band with the brand excluded, and reports new-customer orders and contribution after ad cost, reconciled monthly against your own order export. Catalogues of tens of thousands of products with daily feed operations suit an agency better, and Amazon Ads are not offered. See <a href="/ecommerce-ppc/">e-commerce PPC</a>."""),
("pages-and-tracking", "Are landing pages and conversion tracking part of the monthly fee?",
"""Yes. Building and testing landing pages and keeping tracking healthy are part of running the account, not extra change requests. That covers one page per search intent on your CMS or a subdomain you control, plus GA4, Tag Manager, Consent Mode v2, enhanced conversions and offline import kept in step with your CRM. If you only want one of them, each is also available as a standalone fixed-fee project. See <a href="/landing-pages/">landing pages</a>."""),
]),
]),
("uk", "Hiring from the UK", [
("vat-billing", "VAT, Google's surcharge and billing", [
("vat-on-your-invoice", "Will your invoices include UK VAT?",
"""No. My quotes and invoices carry no UK VAT, because the supply comes from outside the UK and the reverse charge normally applies. In practice your business records the VAT itself on its own return, and the invoice spells out that treatment so your accountant can see it at a glance. The media you buy is invoiced separately by Google, Microsoft or Meta and never shows up on my invoice. See <a href="/pricing/">pricing</a>."""),
("two-percent-surcharge", "What is the 2% Digital Services Tax charge on UK Google Ads invoices?",
"""It is 2% that Google adds on top of the cost of ads served to UK audiences, shown as its own line on the invoice and tied to the UK Digital Services Tax. So a month with £10,000 of media is billed at £10,200 before VAT. Because it applies no matter who manages the account, I include it in the budget plan from the outset, and the first invoice holds no surprise. See <a href="/pricing/">pricing</a>."""),
("surcharge-and-fee", "Does Google's 2% surcharge come out of your fee or my budget?",
"""Your media budget, and it does not change my fee. Google charges the surcharge on the advertising itself, not on management, and it would be the same with any agency or in-house team. Because it is predictable, I build it into the budget plan so that the Google invoice matches the forecast. My own fee stays a flat amount agreed in advance. See <a href="/pricing/">pricing</a>."""),
("pounds", "Are quotes and invoices in pounds?",
"""Yes for UK businesses: every quote is given in pounds, ex VAT, and invoices are issued in pounds as well, even though I work from Brazil. Irish businesses are quoted and invoiced in euros. Your media is a separate bill from Google, Microsoft or Meta, charged to your own billing profile. Monthly reports use the same currency as the invoice, so cost per enquiry is read in the currency you budget in. See <a href="/about/">About</a>."""),
("media-through-you", "Does my ad spend pass through you, or go straight to Google?",
"""Straight to the platforms. Google, Microsoft and Meta bill you directly from your own billing profile, and the money never passes through me or forms part of my fee. That keeps the accounts, the payment history and the invoices in your name, and it means my fee has no reason to grow with your budget. Extra paid software is seldom needed, and you approve it before anything is bought. See <a href="/pricing/">pricing</a>."""),
]),
("contracts", "Contracts and suppliers", [
("ltd-or-sole-trader", "Can a sole trader or a limited company hire you?",
"""Yes, both. The engagement uses the same short services agreement either way, with the monthly fee in pounds, 30 days' notice from either side, confidentiality, and everything built belonging to you. Smaller businesses often start with a fixed-price set-up they run themselves or an audit; larger ones usually move to monthly management after the audit. See <a href="/google-ads-small-business/">Google Ads for small business</a>."""),
("agreement-and-notice", "What does the agreement cover, and how much notice ends it?",
"""Scope, the monthly fee in pounds, confidentiality and ownership, and 30 days' written notice from either side ends it. There is no minimum term and no twelve-month contract: management runs one month at a time. Because the campaigns, tags and pages already sit in your accounts, ending the arrangement involves no migration, only removing my access. See <a href="/pricing/">pricing</a>."""),
("procurement", "Can you meet our supplier onboarding, insurance and SLA requirements?",
"""Not if your procurement needs a company with a team, specific insurance levels and SLAs, because a one-person consultancy cannot sign those, and an agency is the better fit. What I offer instead is a short services agreement covering scope, fee, notice and confidentiality, direct access to the person doing the work, and accounts that stay in your name. If your requirements are lighter, send them with the form and I will say plainly whether they can be met."""),
]),
("consent-data", "Cookies, consent and data", [
("consent-mode-v2", "Do UK advertisers need Google Consent Mode v2?",
"""Yes. For UK and EU traffic it is required, and UK advertisers need it to keep remarketing and audience features working. Consent Mode v2 works with your cookie banner so that consented visitors are measured fully and the rest are modelled rather than lost. I set it up through Tag Manager alongside your existing banner, with the same conversion definitions used across Google, Microsoft and Meta. See <a href="/conversion-tracking/">conversion tracking</a>."""),
("rejected-cookies", "What happens to my conversion data when visitors reject cookies?",
"""With Consent Mode v2 in place, those visitors are modelled rather than lost; without it, they vanish from measurement entirely. A banner installed on its own simply switches tracking off for everyone who declines, so bids end up set on a fraction of the real data. Pairing the banner with Consent Mode keeps consented visitors measured in full and lets Google estimate the rest, so Smart Bidding works from realistic numbers."""),
("cookie-banner-setup", "How do you set up the cookie banner on a site that runs Google Ads?",
"""With a banner that genuinely holds marketing tags back until the visitor agrees, connected to Consent Mode v2 through Tag Manager. If you already use a consent platform, I configure it rather than replace it. The aim is measurement that respects each visitor's choice under UK GDPR and PECR while keeping remarketing and audience features available for people who accept. This site works the same way: nothing is stored on your device until you choose."""),
("which-cmp", "Which consent banner works with Google Ads?",
"""Any consent management platform certified by Google can feed Consent Mode v2. In the UK, Cookiebot, CookieYes and Iubenda turn up most often, though the set-up matters more than the brand. An existing platform is kept and configured rather than swapped out, and the tags in Tag Manager are told to follow its signals, so visitors who accept and visitors who decline are each treated correctly. See <a href="/conversion-tracking/">conversion tracking</a>."""),
("personal-data-to-google", "Does your tracking send personal or health data to Google?",
"""No health data, and personal data only in hashed form where enhanced conversions are used. Conversions are sent as outcomes, such as an enquiry booked or an appointment attended, never as diagnoses or case details. Everything runs under Consent Mode v2, and the set-up is documented so your data protection lead can review exactly what is sent and when. See <a href="/healthcare-ppc/">healthcare PPC</a> for how this works in sensitive sectors."""),
]),
("uk-costs", "UK click prices and budgets", [
("uk-click-prices", "What does a Google Ads click cost in UK cities?",
"""It varies widely by sector and city, so a national average misleads. Google Ads keyword data for October 2026 put an employment lawyer search at £18.60 a click in London against £9.99 in Leeds, and IT support at £37.70 in London against £11.49 in Birmingham, while web design cost more in Birmingham than in London. An audit prices your own auction before any budget is set. The full tables are on the city pages, such as <a href="/ppc-consultant-manchester/">Manchester</a>."""),
("london-premium", "Why do London clicks cost more than the rest of the UK?",
"""More firms bid on the same searches in London, and a London client is often worth more, so bids climb. The gap depends heavily on the sector: legal and IT searches cost from around 40% more to over three times as much as in other large cities, while financial advice costs about the same in Birmingham. That is why a London account needs tight location targeting by borough and hour rather than one pin on the whole city. See <a href="/ppc-consultant-london/">PPC consultant, London</a>."""),
("small-business-budget-uk", "How much should a UK small business budget for Google Ads?",
"""For many UK trades and local services, around £1,000 to £2,000 a month in media buys a meaningful number of clicks at local prices. Solicitors, IT support and other expensive sectors in large cities need more, because each click costs more. Below about £2,000 a month, a fixed-price set-up you run yourself is usually better value than paying a monthly management fee on top. See <a href="/google-ads-small-business/">Google Ads for small business</a>."""),
("market-rates-uk", "What do UK PPC agencies and freelancers usually charge?",
"""Most use one of three models: a share of monthly media, commonly 10% to 20% and often with a floor; a flat monthly retainer; or a day rate, typical of senior freelancers. Percentage fees grow with your budget whether or not results do, and day rates make every question feel billable. Whatever the model, check who owns the accounts. My own fee is a flat monthly amount set by scope and quoted individually; see <a href="/pricing/">pricing</a>."""),
]),
("uk-rules", "UK advertising rules", [
("regulated-sectors-uk", "Can you advertise solicitors, financial services or private clinics within UK rules?",
"""Yes, with copy written inside the rules and signed off by your compliance or clinical lead. For law firms that means the SRA Transparency Rules and the ASA, including the qualifications 'no win no fee' needs. For private healthcare, the CAP Code, MHRA rules on medicines and Google's certification for some treatments, handled with you. For many financial products, Google requires FCA authorisation and verification before adverts can run, so that must be in place first. See <a href="/ppc-for-law-firms/">PPC for law firms</a>."""),
("competitor-names-uk", "Can I bid on a rival firm's name in the UK?",
"""Yes, it is legal in the UK, but whether it pays depends on your sector. Software companies usually do well with a separate competitor campaign, its own comparison page that is honest about the rival's strengths, and a lower target. For law firms the clicks are expensive, conversion is low and the ASA governs how comparative adverts are worded, so it rarely earns its budget. Either way, it is reviewed against the numbers rather than switched on by default. See <a href="/saas-ppc/">SaaS PPC</a>."""),
]),
("remote", "Working with a consultant abroad", [
("in-person", "Will you come to our office in London or elsewhere in the UK?",
"""No, the work is remote as standard, with calls booked ahead on UK time and updates in writing. I am based in Curitiba, Brazil, and there is no London office behind the fee. What you get instead is written replies within one working day, a written monthly report, a note whenever something important changes, and access to the accounts and reporting at any time. If regular face-to-face meetings matter, a local agency will suit you better."""),
("uk-cities", "Do you work with businesses outside London, such as in Manchester, Birmingham, Leeds or Bristol?",
"""Yes, across the UK and Ireland, on the same service and terms everywhere. There are pages for Manchester, Birmingham, Leeds and Bristol because businesses there search locally, and each sets out local click prices and sectors. Location targeting is matched to how you actually serve your area, with the radius around your office bid separately from the wider region. See <a href="/ppc-consultant-manchester/">Manchester</a>, <a href="/ppc-consultant-birmingham/">Birmingham</a>, <a href="/ppc-consultant-leeds/">Leeds</a> and <a href="/ppc-consultant-bristol/">Bristol</a>."""),
("uk-case-study", "Why is there no UK case study yet?",
"""Because no UK engagement can yet be written up with its dates and limits, and an unverifiable story would prove nothing. The four engagements on the results page, including a Houston home services account where cost per acquisition fell 44%, each close with what transfers to a UK business, such as a boiler firm where emergency repairs and new installations fight over one budget. The first UK engagement that can be documented properly will join them. See <a href="/results/">results</a>."""),
("why-uk-site", "Why does a UK consultancy site point to diwizi.com and a US site?",
"""Because one consultant serves several markets, and this is the door for the UK. Diwizi is the name I trade under: diwizi.com covers industries in depth and publishes research, while googleadsfreelancer.com is written for businesses in the US, Canada and Europe. This site gives UK and Irish firms pounds, a clear account of VAT and planning around UK working hours. Whichever door you use, the same person runs your account. See <a href="/about/">About</a>."""),
("outside-uk-ireland", "Can a business outside the UK and Ireland work with you?",
"""Yes. Companies in any country can hire me, provided we can work in English. This site concentrates on the UK and Ireland, quoting in pounds for UK firms and in euros for Irish ones, and explaining VAT for UK firms. If you are based in the US, Canada or elsewhere in Europe, <a href="https://googleadsfreelancer.com/" rel="noopener">googleadsfreelancer.com</a> describes the same service, with the same person behind it, for those markets."""),
]),
]),
]

PAGES = [
{
"slug": 'index',
"short": 'Home',
"blurb": 'Independent PPC consultancy for UK and Irish businesses.',
"title": 'PPC Consultancy UK | Independent PPC Consultant, No Agency Layer',
"meta": 'Independent PPC consultancy for UK businesses: Google, Microsoft and Meta Ads run by one senior consultant, landing pages and tracking included.',
"kicker": 'PPC consultancy',
"h1": 'PPC consultancy without the agency layer. The consultant who audits your account is the one who runs it.',
"lead": 'I am Diego Zietek, an independent PPC consultant with 14+ years on the account. Google, Microsoft and Meta Ads for UK and Irish businesses, with the landing pages and conversion tracking done by the same person. Flat monthly fee, month to month, your accounts stay yours.',
"service_name": 'PPC consultancy and management',
"body": """
<section><div class="wrap">
<h2>One published result, and what it means for a UK account</h2>
<div class="cols">
<div class="card"><h3>Home services, Houston, Texas</h3><p><strong>Google Ads Search · May 2025 to February 2026 · around US$20,000 a month.</strong> Cost per acquisition cut by 44% and qualified leads up 60%, in a local auction where the main searches cost US$45 to US$80 a click.</p><p>The work: campaigns split by type of job, measurement that told a booked job apart from a phone call, a weekly pass through the search terms, and steady tests of adverts and landing pages. The UK equivalent is a boiler and heating business, where emergency repairs and new installations fight over the same budget.</p><p>Three more engagements, each with its limits, are on the <a href="/results/">results page →</a></p></div>
<div class="card"><h3>What the monthly fee includes</h3><ul><li>Hands-on work in the accounts every week: search terms, bids, budgets, adverts and exclusions</li><li>Tracking set up and kept honest: GA4, Tag Manager, Consent Mode v2 and offline import from your CRM</li><li>Landing pages written and built by me on your site or page builder; work that needs your developer is specified for them</li><li>A written report each month on cost per qualified enquiry and what changed</li><li>Your questions answered by the person doing the work</li></ul></div>
</div>
</div></section>

{{brands}}

<section id="services"><div class="wrap">
<h2>What the consultancy covers</h2>
<div class="cols">
<div class="card"><h3><a href="/ppc-management/">PPC management</a></h3><p>Google, Microsoft and Meta Ads run as one programme with one set of numbers, landing pages and tracking included.</p><p class="price"><b>Flat monthly fee</b> · sized to the work, never to your spend · month to month</p></div>
<div class="card"><h3><a href="/ppc-audit/">PPC audit</a></h3><p>An independent, paid review of your accounts, with every fix put in order of what it is costing you. The report is yours to keep and act on, with or without me.</p><p class="price"><b>One fixed fee</b> · agreed before work starts · deducted from month one if you continue</p></div>
<div class="card"><h3><a href="/landing-pages/">Landing pages</a></h3><p>A page for each search intent, written to match the advert that sends the visitor, with tracking tested before launch.</p><p class="price"><b>Included</b> in management · <b>fixed fee</b> as a one-off project</p></div>
<div class="card"><h3><a href="/conversion-tracking/">Conversion tracking</a></h3><p>GA4, Tag Manager, Consent Mode v2 and offline conversion import, so the platforms learn from enquiries that became customers.</p><p class="price"><b>Fixed fee</b> · depends on platforms and CRM</p></div>
</div>
<p>Quotes come in pounds, ex VAT, or in euros for Irish businesses, from three details on the <a href="/contact/#form">form</a>: roughly what you spend, on which platforms, and what is going wrong. Your media is paid straight to Google, Microsoft or Meta and never forms part of my fee. The <a href="/pricing/">pricing page</a> sets out every model.</p>
</div></section>

""" + NOT_FOR + """

<section><div class="wrap">
<h2>Industries where the pattern recognition is already built</h2>
<div class="cols">
<div class="card"><h3><a href="/saas-ppc/">B2B and SaaS</a></h3><p>Trial-to-paid and demo funnels, search on Google and Microsoft, CRM stages fed back to the platforms so they optimise towards pipeline rather than form fills. <a href="/b2b-ppc/">B2B PPC →</a></p></div>
<div class="card"><h3><a href="/ppc-for-law-firms/">Professional and financial services</a></h3><p>Law firms, accountants, advisers and consultancies: expensive clicks, long consideration, and a compliance layer on what an ad can say. Enquiry quality is the whole game.</p></div>
<div class="card"><h3><a href="/healthcare-ppc/">Healthcare and regulated categories</a></h3><p>Past roles include senior in-house paid media work in healthcare and a freelance role with a US pharmaceutical agency. Policy restrictions, certification and sensitive-category rules are familiar ground.</p></div>
<div class="card"><h3>Home and trade services</h3><p>Emergency versus planned work, call tracking that separates a booked job from a ring, and bidding by postcode and hour. The Houston case above is this pattern.</p></div>
<div class="card"><h3><a href="/ecommerce-ppc/">Online retail</a></h3><p>Shopping and Performance Max measured on margin and new customers, with platform-reported revenue reconciled against the store's own orders.</p></div>
</div>
<p>Industry pages with more detail are on <a href="https://diwizi.com/" rel="noopener">diwizi.com</a>, the same practice organised by sector.</p>
</div></section>

<section><div class="wrap">
<h2>How we would start</h2>
<ol class="steps">
<li><div><strong>You send the form.</strong> What you spend, your site and what has already been tried. I reply personally, saying whether I can help, what I would look at first and a price range. A call follows only if it is useful.</div></li>
<li><div><strong>A fixed-fee audit.</strong> Read-only access is all it needs. You get written findings in order of impact, starting with tracking, then wasted spend, then structure, then testing, and they are yours to act on however you choose.</div></li>
<li><div><strong>Management, one month at a time.</strong> If the audit shows there is enough to gain, I take on the accounts for a flat fee, with the audit fee deducted from the first month. Thirty days' notice, no fixed term.</div></li>
</ol>
</div></section>

<section><div class="wrap">
<h2>Consultant, agency or in-house hire: which suits your account</h2>
<table>
<tr><th></th><th>Independent consultant</th><th>PPC agency</th><th>Hiring in-house</th></tr>
<tr><td>Who works on the account</td><td>The person you first spoke to</td><td>An account executive, once the pitch team has moved on</td><td>One employee, often junior</td></tr>
<tr><td>How it is paid for</td><td>Flat fee, no fixed term</td><td>Retainer or a share of spend, usually a 6 to 12 month contract</td><td>Salary, tools and management time</td></tr>
<tr><td>Landing pages and tracking</td><td>Included, by the same person</td><td>Often another team, or outside the scope</td><td>Depends entirely on who you hire</td></tr>
<tr><td>Suits</td><td>£2,000 to £60,000 a month, one business</td><td>Many markets, languages or heavy creative output</td><td>Budgets big enough to support a team</td></tr>
</table>
<p>The longer comparison, including when I would point you to an agency instead, is on <a href="/agency-vs-consultant/">PPC agency vs PPC consultant</a>.</p>
</div></section>
""",
"faq": [
('Are you a freelancer or an agency?', 'Neither, in the usual sense. I am an independent consultant: one senior person who audits, builds and runs the accounts. No account manager and no juniors: the ads, tracking and reports are never handed on. If a project needs design or development beyond what I build myself, you are told first and the specialist is named.'),
('Can you work with a UK business from Brazil?', 'Yes. I am based in Curitiba (GMT-3), three to four hours behind London. Most of the work is done in writing, calls are booked ahead, usually in the UK afternoon, and everything is in English.'),
('How much does PPC consultancy cost?', "A flat monthly fee for management, sized to the work rather than to your spend, quoted in pounds ex VAT. The audit is one fixed fee, deducted from the first month if you carry on. There is no twelve-month contract, and the <a href='/pricing/'>pricing page</a> sets out each model."),
('Do you do e-commerce PPC?', 'Yes. Google Shopping, Merchant Centre feeds, Performance Max and Meta for online stores, measured on margin and new customers rather than on the platform\'s own ROAS. Very large catalogues with daily feed operations are agency work, and I will say so.'),
('Which platforms?', 'Google Ads (Search, Shopping, Performance Max, YouTube, Demand Gen), Microsoft Advertising and Meta Ads, plus GA4, Tag Manager and the landing pages that sit under all of them.'),
('Can you take over an account an agency set up?', 'Yes, and that is where most engagements begin. The usual findings are conversion actions counted twice, broad match left to Smart Bidding with no exclusions, and campaigns arranged around how they were built rather than how the business makes money. Nothing gets changed until the tracking can be trusted.'),
],
"related": ['ppc-management', 'ppc-audit', 'b2b-ppc', 'pricing'],
"cta_title": 'Get a quote in pounds',
"cta_text": 'Roughly what you spend, your site and what is going wrong. You will get a straight answer on whether I can help, where I would start and a price range, without a proposal deck or a chaser email.',
},

{
"slug": "ppc-consultant-london", "short": "PPC consultant, London", "blurb": "For London businesses, delivered remotely on UK hours.",
"title": 'PPC Consultant London | PPC Management Without an Agency',
"meta": 'Independent PPC consultant for London businesses: Google, Microsoft and Meta Ads run by one senior consultant on UK hours. Flat monthly fee.',
"kicker": "PPC consultant London",
"h1": "PPC consultant for London businesses, working remotely on your hours",
"lead": "Independent PPC consultant for London firms: 14+ years running Google, Microsoft and Meta Ads, calls on UK time, everything in writing, and a fee that does not carry a London office inside it.",
"service_name": "PPC consultancy for London businesses",
"body": """
<section><div class="wrap">
<h2>What London accounts usually need</h2>
<p>London is the most crowded paid search market in the UK. More firms bid on the same searches, the client each click might bring is often worth more, and the result is that waste costs more here than almost anywhere else in the country. The work is the same everywhere; the tolerance for getting it wrong is lower.</p>
<ul>
<li><strong>Location targeting that matches how you actually serve.</strong> "London" is thirty-two boroughs, the City and a commuter belt. Bids by borough and by hour, with the radius around your office kept separate from the wider catchment, instead of one pin on Charing Cross.</li>
<li><strong>Enquiry quality over enquiry count.</strong> Call tracking tied to the keyword, form fields that qualify, and CRM stages fed back to Google and Microsoft so bidding learns from clients, not from clicks.</li>
<li><strong>A landing page per intent.</strong> Not the homepage, and not one generic contact page for twelve services.</li>
<li><strong>Brand and competitor terms handled deliberately.</strong> Whether to bid on your own name in a crowded market is a calculation, not a reflex, and the answer changes with who else is bidding.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>What a click costs in London compared with other UK cities</h2>
<p>Average cost per click for the same search with the city name attached, from Google Ads keyword data for the UK, October 2026. These are market averages, not a forecast for your account.</p>
<table>
<tr><th>Search</th><th>London</th><th>Manchester</th><th>Birmingham</th><th>Leeds</th></tr>
<tr><td>solicitors [city]</td><td>£13.49</td><td>£9.46</td><td>£9.31</td><td>£7.09</td></tr>
<tr><td>employment lawyer [city]</td><td>£18.60</td><td>£10.95</td><td>£10.92</td><td>£9.99</td></tr>
<tr><td>accountants [city]</td><td>£12.55</td><td>£12.21</td><td>£10.53</td><td>£8.80</td></tr>
<tr><td>IT support [city]</td><td>£37.70</td><td>£16.03</td><td>£11.49</td><td>£26.67</td></tr>
<tr><td>financial advisor [city]</td><td>£20.43</td><td>£15.93</td><td>£20.38</td><td>£19.07</td></tr>
<tr><td>web design [city]</td><td>£12.05</td><td>£13.97</td><td>£20.01</td><td>£9.15</td></tr>
</table>
<p>Two things stand out. Legal and IT searches cost far more per click in London, from around 40% more than the other cities to over three times as much. And London is not the most expensive city for everything: financial advice costs about the same in Birmingham, and web design costs more there. The lesson is to price your own auction rather than assume. It is one of the first things an <a href="/ppc-audit/">audit</a> looks at.</p>
</div></section>

<section><div class="wrap">
<h2>London sectors where this work is already familiar</h2>
<div class="cols">
<div class="card"><h3>Professional services</h3><p>Law firms, accountants and consultancies: expensive clicks, long consideration and a compliance layer on what an advert can say. The job is to pay for enquiries that turn into instructions, not for people comparing fees. Pages built around one practice area convert better than a firm-wide page.</p></div>
<div class="card"><h3>Financial services</h3><p>Advisers, lenders and fintech. Google requires advertisers of many financial products in the UK to be FCA authorised and verified before ads can run, and every claim must stand up. Budgets are wasted less by bids than by disapproved adverts and research traffic.</p></div>
<div class="card"><h3>B2B and SaaS</h3><p>London's technology and B2B services firms buy through committees. Google and Microsoft Search capture the buyers already looking, judged on pipeline from the CRM rather than form fills. <a href="/b2b-ppc/">B2B PPC →</a></p></div>
</div>
</div></section>

<section><div class="wrap">
<h2>What a published result looks like in London terms</h2>
<p>There is no London case study on this site yet, and none will be invented. What can be shown is how a published engagement would translate. The <a href="/results/">Houston home services account</a> cut cost per acquisition by 44% and lifted qualified leads by 60% in an auction where clicks cost US$45 to US$80. What moved it was not a bidding trick:</p>
<ul>
<li>Campaigns split by type of job, so urgent, cheaper work stopped absorbing the budget meant for higher-value jobs.</li>
<li>Tracking rebuilt so a booked job and a phone call were different events.</li>
<li>A weekly pass through the search terms and steady tests of adverts and landing pages.</li>
</ul>
<p>For a London law firm, the same three moves mean separating practice areas that share one campaign, counting a signed instruction rather than a call, and cutting the research searches ("how much does a divorce cost", "free legal advice") that eat budget at well over £10 a click. The auction is different; the order of work is not.</p>
</div></section>

<section><div class="wrap">
<h2>Consultant or London agency</h2>
<table>
<tr><th></th><th>Independent consultant</th><th>London PPC agency</th></tr>
<tr><td>Who does the work</td><td>The person you spoke to first</td><td>An account team, often led by someone junior once the pitch is over</td></tr>
<tr><td>How it is charged</td><td>Flat monthly fee, never a share of spend</td><td>Retainer or a percentage of spend</td></tr>
<tr><td>Minimum term</td><td>None; 30 days' notice</td><td>Commonly 6 to 12 months</td></tr>
<tr><td>Landing pages and tracking</td><td>Included, by the same person</td><td>Often another team or an extra</td></tr>
<tr><td>Meetings</td><td>Remote, calls on UK time, written updates</td><td>In person if you want them</td></tr>
<tr><td>Better when</td><td>One business, one senior person accountable</td><td>Many markets, heavy creative or regular face-to-face</td></tr>
</table>
<p>The full comparison is on <a href="/agency-vs-consultant/">PPC agency vs PPC consultant</a>.</p>
</div></section>

<section><div class="wrap">
<h2>Remote, and honest about it</h2>
<p>I do not have a London office and this page will not pretend otherwise. I am based in Curitiba, Brazil, three to four hours behind London. What you get instead: calls booked in advance, usually in the UK afternoon, written replies within one working day, a written monthly report and a note in writing whenever something important changes, access to the accounts and reporting at any time, and a fee without London overheads inside it. If you need someone in the room every month, a London agency is the better choice, and I will say so on the first call.</p>
</div></section>

<section><div class="wrap">
<h2>Same services, same terms</h2>
<div class="cols">
<div class="card"><h3><a href="/ppc-audit/">Audit first</a></h3><p>Fixed price, read-only access, written findings ranked by impact. Credited against the first month if we continue.</p></div>
<div class="card"><h3><a href="/ppc-management/">Management</a></h3><p>Flat monthly fee, month to month, landing pages and tracking in scope. Never a percentage of spend.</p></div>
<div class="card"><h3><a href="/b2b-ppc/">B2B PPC</a></h3><p>For London B2B and SaaS firms: pipeline reported, not leads.</p></div>
</div>
</div></section>
""",
"faq": [
('Do you meet clients in London?', 'The engagement is remote as standard: calls on UK time and written updates. If regular face-to-face meetings matter to you, an agency with a London office will suit you better, and I would rather say so at the start.'),
('Do you work with businesses outside London?', 'Yes, across the UK and Ireland. This page exists because London businesses search for a London consultant; the service and the terms are the same everywhere.'),
('What do London PPC consultants charge?', 'Senior UK freelancers commonly quote a few hundred pounds a day or a flat monthly retainer; agencies usually start higher and add a minimum term. I quote a flat monthly fee set by scope, in pounds ex VAT, without a minimum term. The <a href="/pricing/">pricing page</a> has the models.'),
('Why are clicks so expensive in London?', 'More firms compete for the same searches and a London client is often worth more, so bids rise. It varies a lot by sector: legal and IT searches cost far more in London than in other cities, while some others cost about the same. The table on this page shows real averages.'),
('Should I target all of London?', 'Rarely. Most firms win clients from a few boroughs, the City or a commuter corridor, and bidding on the whole of Greater London pays for clicks from people who will never travel to you. Location and schedule settings are reviewed in the first month.'),
('Do you have a London case study?', 'Not one that can be published yet with dates and limits. The results page shows engagements that can be described properly, and this page shows how they translate to a London account. The first London engagement that can be written up the same way will be added.'),
('How soon will I see a difference?', 'Nobody honest can promise a number before seeing the account. The first month usually goes on tracking and wasted spend, which is where the quickest gains tend to be. Each step is reported in writing so you can see what moved and why.'),
],
"related": ["ppc-management", "ppc-audit", "agency-vs-consultant", "contact"],
},

{
"slug": "agency-vs-consultant", "short": "Agency vs consultant", "blurb": "When a PPC agency is the right answer, and when it is not.",
"title": "PPC Agency vs PPC Consultant: Which Should a UK Business Hire?",
"meta": 'PPC agency or independent consultant? Who does the work, how each charges, what is in scope, and when an agency is the better choice for a UK business.',
"kicker": "Choosing",
"h1": "PPC agency or PPC consultant? When each one is the right call",
"lead": "Written by a consultant, so read it with that in mind. It still names the cases where I would tell you to hire an agency, because sending the wrong client to the wrong model helps nobody.",
"body": """
<section><div class="wrap">
<h2>The five questions that decide it</h2>
<ol class="steps">
<li><div><strong>Who will touch the account each week?</strong> At an agency, ask for the name and the years of experience of the person doing the weekly work, not the person on the pitch. With a consultant the answer is trivially the person you are talking to.</div></li>
<li><div><strong>How many markets, languages and creative formats?</strong> Five countries, three languages and a weekly video pipeline is agency work. One company, one or two markets, mostly search and lead forms is consultant work.</div></li>
<li><div><strong>How is the fee calculated?</strong> A percentage of spend pays the vendor to grow spend. A flat fee pays them to grow results. Ask what happens to the invoice if the right advice is to cut budget by a third.</div></li>
<li><div><strong>Are landing pages and tracking in scope?</strong> Most agency retainers cover the ad accounts and stop at the click. Most of the waste is after the click.</div></li>
<li><div><strong>What happens if you leave?</strong> If the campaigns, conversion actions and tags live in the vendor's accounts, the real price of the contract is that you cannot go.</div></li>
</ol>
</div></section>

<section><div class="wrap">
<h2>Where an agency is the better choice</h2>
<ul>
<li>Spend above roughly £60,000 a month across several platforms, where the work genuinely needs more than one pair of hands.</li>
<li>Multi-country accounts needing native-language copy and local compliance.</li>
<li>Paid social at scale, where creative production is the bottleneck and the agency has a studio.</li>
<li>Procurement that requires a company with a team, insurance levels and SLAs a one-person consultancy cannot sign.</li>
<li>E-commerce with tens of thousands of products and daily feed operations, where the feed alone is a full-time job.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>Where an independent consultant is the better choice</h2>
<ul>
<li>One company spending between a few thousand and sixty thousand pounds a month, mostly on lead generation.</li>
<li>An account that has been through two agencies and nobody can explain what is actually being done.</li>
<li>An in-house team that needs a senior second opinion, a structured audit, or someone to build the measurement layer once, properly.</li>
<li>Owners who want to speak to the person doing the work, and want the fee to reflect that there is no office and no margin stack.</li>
</ul>
<p>If you are in the second group, the <a href="/ppc-audit/">audit</a> is the low-risk way to find out. If you are in the first, the <a href="https://www.leverdigital.co.uk/guides/best-ppc-consultants-uk" rel="noopener">Lever Digital guide to UK PPC consultants and agencies</a> is a fair place to start looking.</p>
</div></section>
""",
"faq": [
("Is a consultant cheaper than an agency?", "Usually, for the same account, because there is no account manager, office or margin between you and the work. Senior consultants overlap with small agencies at the top of the range. The cheaper option is a marketplace freelancer, which is a different product."),
("Can a consultant handle Google, Microsoft and Meta at once?", "For one company, yes, and it is better that way: one measurement layer and one person deciding where the next pound goes. What a consultant cannot do is produce creative at agency volume."),
("Will you tell me if my current agency is doing a good job?", "Yes, in writing. A fair audit that confirms the agency is competent is still useful: it tells you where the remaining gains are and gives you specific questions for the next review."),
],
"related": ["ppc-audit", "ppc-management", "pricing", "about"],
},

{
"slug": 'pricing',
"short": 'Pricing',
"blurb": 'How UK PPC work is charged, what it typically costs, and my fees.',
"title": 'PPC Management Pricing UK | What PPC Management Costs, and My Fees',
"meta": "PPC management pricing in the UK: how fees are charged, typical costs by spend band, Google's 2% UK surcharge, and how I price. In pounds, ex VAT.",
"kicker": 'Pricing',
"h1": 'PPC management pricing in the UK: what it costs and how I charge',
"lead": 'Before any number, the model matters more than the rate: it decides whose interests the advice serves. This page sets out how UK consultancies and agencies charge, what management tends to cost at each spend level, the costs that sit on top of any fee, and exactly how I price.',
"service_name": 'PPC consultancy pricing',
"proof": [('£', 'flat fees, ex VAT'), ('0%', 'of your ad spend'), ('Fixed', 'price audits'), ('No', 'minimum term')],
"body": """
<section><div class="wrap">
<h2>Three ways UK consultancies and agencies charge</h2>
<div class="cols">
<div class="card"><h3>A share of your spend</h3><p>Commonly 10% to 20% of monthly media, often with a floor. Simple to budget for, but the fee climbs every time the budget does, which is an uncomfortable position for anyone who ought to be telling you to spend less.</p></div>
<div class="card"><h3>A flat monthly retainer</h3><p>One fee each month, whatever the spend. The incentives are cleaner. The thing to check is what sits outside it: when landing pages and tracking are extras, the fixes that matter most have a habit of staying on the to-do list.</p></div>
<div class="card"><h3>Days or hours</h3><p>Senior UK freelancers commonly quote a few hundred pounds a day. Sensible for an audit, training or a second opinion. Awkward for running an account week to week, because every question starts to feel billable, and that is when accounts drift.</p></div>
</div>
<p class="note">Whatever the model, ask who owns the accounts. If the campaigns, conversion actions and tags sit in the supplier's accounts rather than yours, leaving costs you the history, and that is the most expensive line in any contract.</p>
</div></section>

<section><div class="wrap">
<h2>What UK PPC management tends to cost</h2>
<p>Indicative ranges for context, not a quote. Independent consultants usually come in under agency fees at the same spend because there is no account team, office or margin layered on top; experienced independents sit at the upper end and overlap with small agencies.</p>
<table>
<tr><th>Monthly media spend</th><th>Independent consultant</th><th>Small agency</th><th>What to watch</th></tr>
<tr><td>Below £2,000</td><td>A one-off setup or audit</td><td>Often under the minimum</td><td>A monthly retainer rarely pays for itself</td></tr>
<tr><td>£2,000 to £10,000</td><td>Flat monthly retainer, set by scope</td><td>A minimum fee or 15% to 20%</td><td>The band where one senior person makes most difference</td></tr>
<tr><td>£10,000 to £40,000</td><td>Flat retainer sized to the scope</td><td>Around 10% to 15%</td><td>Percentage fees begin to outgrow the work</td></tr>
<tr><td>Above £40,000</td><td>Flat retainer, part-time head of paid media</td><td>Bespoke, often 8% to 12%</td><td>Structure and measurement outweigh bid tweaks</td></tr>
</table>
</div></section>

<section><div class="wrap">
<h2>Costs that sit on top of any fee</h2>
<ul>
<li><strong>Media.</strong> Billed to you directly by Google, Microsoft or Meta from your own billing profile. It never passes through me.</li>
<li><strong>Google's 2% UK surcharge.</strong> Google adds a 2% charge to invoices for ads shown in the UK, listed as a separate line and linked to the UK Digital Services Tax. A £10,000 month is therefore invoiced as £10,200 before VAT. It applies whoever runs the account, so I build it into the budget plan rather than let it surprise you.</li>
<li><strong>Creative at volume.</strong> For Meta-heavy accounts, regular creative production comes from your designer or a studio and is billed by them.</li>
<li><strong>Paid tools.</strong> Rarely needed beyond what the platforms provide, and always agreed with you first.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>How I price</h2>
<p>Every engagement is quoted in pounds, ex VAT, or in euros for Irish businesses, after the form tells me the spend band, the platforms, and whether landing pages or tracking need rebuilding. The model below is fixed before any quote.</p>
<p>The fee is set for your account, not from a rate card: platforms, markets, campaigns and how much landing page and tracking work is included. A range comes by email from the form; a firm figure needs a look at the accounts.</p>
<table>
<tr><th>Engagement</th><th>How it is charged</th><th>What you get</th></tr>
<tr><td><a href="/ppc-audit/">PPC audit</a></td><td>One fixed fee for your account, set from monthly spend, number of campaigns and platforms in scope</td><td>A written report with fixes in order of impact and a walkthrough call. The figure comes by email from the form within one working day and is deducted in full from the first month if management follows.</td></tr>
<tr><td><a href="/ppc-management/">Management, media up to around £10,000 a month</a></td><td>Flat monthly fee</td><td>Weekly work in the accounts, tracking kept healthy, landing page fixes and a written monthly report. Month to month.</td></tr>
<tr><td>Management, £10,000 to £40,000 a month</td><td>Flat monthly fee sized to the scope</td><td>The same service across more campaigns, platforms or markets.</td></tr>
<tr><td>Management, above £40,000 a month</td><td>Flat monthly fee quoted per account</td><td>Several platforms, a weekly call, and the role of a part-time head of paid media rather than an operator.</td></tr>
<tr><td><a href="/landing-pages/">Landing pages</a></td><td>Included in management, or a fixed project fee</td><td>A page per search intent: copy, build, tracking and a test plan.</td></tr>
<tr><td><a href="/conversion-tracking/">Conversion tracking</a></td><td>Fixed project fee</td><td>GA4, Tag Manager, Consent Mode v2, enhanced and offline conversions, and a reconciliation against your CRM.</td></tr>
<tr><td>Account setup</td><td>Fixed project fee</td><td>Built in your own account, tracking included, with a handover document to run it yourself.</td></tr>
<tr><td>Advice for in-house teams</td><td>Day rate, or a fixed fee per piece of work</td><td>Strategy, second opinions and regular review sessions.</td></tr>
</table>
<p>No line on this page is a percentage of your media, so telling you to cut budget costs me nothing. Adding Microsoft Advertising to a Google account is a small increase; adding Meta with ongoing creative testing is a bigger one, agreed before it starts. Send the <a href="/contact/#form">form</a> and a range comes back within one working day, often the same day; a firm figure needs a look at the accounts.</p>
</div></section>
""",
"faq": [
('Do you charge VAT?', 'Quotes are always ex VAT. I supply services to UK businesses from outside the UK, so the reverse charge normally applies: you account for the VAT in your own return, and your accountant will recognise the treatment on the invoice.'),
('Is there a setup fee or a minimum term?', 'Starting management has no onboarding fee. Existing accounts start with an audit and new accounts with a setup; either one is a fixed price in pounds, ex VAT, and is credited against the first month of management. Management runs month to month, with 30 days\' notice either way.'),
("Can either side end it?", "Either side can end management with 30 days' written notice. Everything stays in your accounts, so nothing has to be migrated when it ends."),
('Why not charge a percentage of spend like most agencies?', 'Because it pays the supplier for spending more rather than for results. With a flat fee, the advice to cut a campaign or pause a platform costs me nothing, so you get it when you need it.'),
("Does Google's 2% UK surcharge change your fee?", 'No. Google charges it on the media, not me, and it is the same whoever runs the account. I include it in the budget plan so the invoice matches the forecast.'),
('Can I get a price without a call?', 'Yes. The form asks for spend band, platforms and what needs fixing, and a range comes back by email. A firm number needs read-only access or a short call.'),
],
"related": ['ppc-audit', 'ppc-management', 'agency-vs-consultant', 'contact'],
},

{
"slug": 'results',
"short": 'Results',
"blurb": 'Published results, their limits, and what carries over to a UK account.',
"title": 'PPC Results and Case Studies | What Transfers to a UK Account',
"meta": 'Four published PPC engagements, including 44% lower CPA for a home services firm and 600% sales growth for a startup, and what carries over to UK accounts.',
"kicker": 'Results',
"h1": 'Published results, their limits, and what they mean for a UK account',
"lead": 'Four engagements are described here. None of them is British yet, so each one ends with the part that carries over to a UK business, and each says plainly what a reader can and cannot verify.',
"proof": [('44%', 'lower CPA, home services'), ('60%', 'more qualified leads, same account'), ('600%', 'sales growth in 8 months, software'), ('3 months', 'early on a 5,000-student target')],
"body": """
<section><div class="wrap">
<h2>Home services: an HVAC and plumbing business in Houston, Texas</h2>
<p><strong>Google Ads Search · May 2025 to February 2026 · around US$20,000 a month · working directly with the owner.</strong></p>
<h3>Starting point</h3>
<p>Local home services in one of the priciest auctions in the United States, with core searches costing US$45 to US$80 a click and demand rising and falling with the weather. Emergency call-outs and full system replacements shared a single campaign, so the cheaper, urgent jobs soaked up budget meant for installations. Every phone call counted as a conversion, whether or not it turned into work, so the account was optimising for the phone ringing rather than for booked jobs.</p>
<h3>What changed</h3>
<ul>
<li>Campaigns split by type of job, so emergency repairs, replacements and maintenance each had their own budget, bids and landing page.</li>
<li>Measurement rebuilt so that a booked job and a phone call were separate events, with each call traced back to the search behind it.</li>
<li>A weekly pass through the search terms, adding exclusions the account had gone months without.</li>
<li>Steady testing of adverts and landing pages, one challenger against one control at a time.</li>
<li>Location and audience settings brought into line with the area the engineers actually covered.</li>
</ul>
<h3>Outcome</h3>
<p>Cost per acquisition came down <strong>44%</strong> and qualified leads went up <strong>60%</strong> across the engagement, on roughly US$20,000 of monthly spend.</p>
<h3>How much of this can be checked</h3>
<p class="note">The figures come from the Google Ads account and the reports delivered during the engagement. Nobody independent has audited them, the client has not published a testimonial, and the comparison window and conversion definition are not given here. The engagement and its dates can be matched against the fuller write-up on <a href="https://diwizi.com/case-houston-hvac-plumbing.html" rel="noopener">diwizi.com</a>. Account structure, keyword lists, lead volumes and revenue stay confidential. A reference is available for serious enquiries if the client agrees.</p>
<h3>The UK version of this account</h3>
<p>Swap air conditioning for boilers and it looks very familiar: emergency boiler repair and new boiler installation fighting over one budget, calls counted whether or not an engineer is booked, and postcodes mattering more than keywords. UK clicks are cheaper, which makes the same waste easier to overlook rather than smaller.</p>
</div></section>

<section><div class="wrap">
<h2>Software: Pontomais, time-tracking and HR software in Brazil</h2>
<p><strong>Paid media, mainly Google Ads · startup stage · eight months.</strong></p>
<p>Pontomais sold time-tracking and HR software to Brazilian businesses and was up against larger, better-funded rivals on the same searches. The brief was to make paid search the main source of new customers without matching their budgets: keywords confined to buying intent, landing pages designed around the trial and demo request, and tracking that followed each lead through to a signed contract.</p>
<p>Sales rose <strong>600% in eight months</strong>, with most of the new business coming from Google.</p>
<p class="note">Taken from the company's own sales reporting at the time and not audited independently. Budgets, cost per acquisition and contract values are not published.</p>
<p><strong>For a UK software business:</strong> the order of work is the same. Measure trials and demos through to paying accounts, bid on the searches buyers make rather than those made by students and job-seekers, and build each landing page around the trial or the demo.</p>
</div></section>

<section><div class="wrap">
<h2>Education: one of the largest private school groups in Brazil</h2>
<p><strong>Enrolment campaigns · client not named.</strong></p>
<p>The target was <strong>5,000 new students</strong>. It was met <strong>three months ahead of the deadline</strong>, with paid media carrying families from the first search through to an enrolment enquiry.</p>
<p class="note">Budgets, cost per enrolment and results by campus are confidential.</p>
<p><strong>For UK schools, colleges and training providers:</strong> enrolment runs to a hard deadline, so demand has to be built before the intake rather than during it, and the campaign calendar is set by the admissions timetable, not by the media plan.</p>
</div></section>

<section><div class="wrap">
<h2>Regulated categories: Underscore Marketing, a US pharmaceutical agency</h2>
<p>From September 2023 to March 2024 I worked as a freelance paid media operator for Underscore Marketing, on Google Ads and paid social accounts run under the agency's name, across oncology, rare disease and gene therapy brands. Product names, budgets and results stay confidential under the agency's NDA.</p>
<p><strong>For UK healthcare advertisers:</strong> the rules are different here, since prescription medicines cannot be advertised to the public at all and health advertising sits under the CAP Code and Google's own healthcare policies. The discipline carries over unchanged: every advert and landing page is written to be approved first time, with claims that can be substantiated.</p>
</div></section>

<section><div class="wrap">
<h2>Published research</h2>
<p>Two pieces of first-party research are public on the consultancy's main site: the <a href="https://diwizi.com/paid-media-cost-index.html" rel="noopener">Paid Media Cost Index</a>, a median Google Ads cost-per-click benchmark across six US industries with its method and date, and a series of <a href="https://diwizi.com/case-study-hubspot-paid-search.html" rel="noopener">ad spend teardowns</a> built from public advertiser data.</p>
</div></section>
""",
"faq": [
('Why is there no UK case study?', 'Because none can be published yet with dates and limits attached. Rather than write a vague one, this page shows engagements that can be described properly and what each means for a UK account. The first UK engagement that can be written up the same way will be added here.'),
('Why are some clients not named?', 'Much paid media work sits under NDAs or compliance rules. Where a client cannot be named, the sector, the scale and the result are given and nothing more. A few engagements with their limits spelled out are worth more than a long list with the limits hidden.'),
('Can I speak to a previous client?', 'For serious enquiries, yes, provided the client agrees. Mention it in the form or on the call.'),
('What will you promise before seeing my account?', 'No figure. Anyone who quotes a result before looking at the account is guessing. What I commit to is the order of work: tracking first, then wasted spend, then structure, then testing, with each step reported in writing so you can see what moved.'),
],
"related": ['ppc-management', 'ppc-audit', 'about', 'b2b-ppc'],
},

{
"slug": 'about',
"short": 'About Diego',
"blurb": 'The consultant behind this site, and how a UK engagement works.',
"title": 'About Diego Zietek | PPC Consultant Working With UK Businesses',
"meta": 'Diego Zietek, the consultant behind PPC Consultancy UK: 14+ years running Google, Microsoft and Meta Ads for UK and Irish businesses.',
"kicker": 'About',
"h1": 'Who runs your account, and how a UK engagement works',
"lead": 'I am Diego Zietek. I have run paid media for more than 14 years across Google Ads, Microsoft Advertising and Meta, and every account taken on through this site is run by me personally, from the first audit to the monthly report.',
"proof": [('14+', 'years running paid media'), ('1', 'person on your account'), ('£ / €', 'pounds for the UK, euros for Ireland'), ('No', 'minimum term')],
"body": """
<section><div class="wrap">
<h2>In short</h2>
<table>
<tr><th>Who</th><td>Diego Zietek, independent PPC consultant and founder of Diwizi, a consultancy of one. No account managers, no juniors, no hand-offs.</td></tr>
<tr><th>Track record</th><td>More than 14 years hands-on, across in-house roles, freelance engagements and agency work.</td></tr>
<tr><th>Channels</th><td>Google Ads (Search, Performance Max, Demand Gen, YouTube), Microsoft Advertising, Meta (Facebook and Instagram).</td></tr>
<tr><th>Measurement</th><td>GA4 and Tag Manager, Consent Mode v2 set up for UK GDPR and PECR, enhanced conversions, and offline conversion import from HubSpot or Salesforce.</td></tr>
<tr><th>Sectors</th><td>B2B and SaaS, professional and financial services, healthcare, home and trade services, and online retail.</td></tr>
<tr><th>Working pattern</th><td>Remote, in English and mostly in writing. Based in Curitiba, Brazil (GMT-3), three to four hours behind London, with calls booked in advance and usually held in the UK afternoon.</td></tr>
<tr><th>Contracting</th><td>Quoted and invoiced in pounds, or in euros for Irish businesses. For UK businesses, the services are supplied from outside the UK, so the reverse charge normally applies and you account for the VAT yourself.</td></tr>
<tr><th>Contact</th><td>The <a href="/contact/#form">form</a> or {{email}}. Both reach me directly.</td></tr>
</table>
</div></section>

{{brands}}

<section><div class="wrap">
<h2>What a UK client can expect</h2>
<ul>
<li><strong>The same person throughout.</strong> Whoever you speak to on the first call is the person working in your account every week.</li>
<li><strong>A flat fee in pounds.</strong> Never a slice of your media, so advising a lower budget costs me nothing.</li>
<li><strong>Everything built in your accounts.</strong> Google Ads, GA4, Tag Manager and Meta stay in your name. Stop whenever you like and keep all of it.</li>
<li><strong>Landing pages and tracking in scope.</strong> In lead generation, that is usually where the waste is, not in the bids.</li>
<li><strong>Consent done properly.</strong> Consent Mode v2 and a banner that genuinely holds marketing tags back until a visitor agrees, which UK advertisers need for remarketing and audience features.</li>
<li><strong>Reports written for the person paying.</strong> Cost per qualified enquiry, what changed and why, rather than a page of click counts.</li>
<li><strong>A short client list.</strong> Kept deliberately small so each account gets proper attention.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>Why a separate site for the UK</h2>
<p>This site is the UK entrance to one practice. <a href="https://diwizi.com/" rel="noopener">Diwizi.com</a> goes deep by industry and publishes the research; <a href="https://googleadsfreelancer.com/" rel="noopener">googleadsfreelancer.com</a> serves businesses in the US, Canada and Europe looking for a freelance Google Ads specialist. This one is for UK and Irish businesses that want prices in pounds or euros, the VAT position set out plainly and a consultant who plans around UK hours. Whichever site you arrive through, the account is run by the same person.</p>
</div></section>

<section><div class="wrap">
<h2>What is published, and what is not</h2>
<p>Four engagements are written up on the <a href="/results/">results page</a>, each with its limits: a Houston HVAC and plumbing business, Pontomais (a Brazilian HR software startup), one of the largest private school groups in Brazil, and a freelance role with Underscore Marketing, a US pharmaceutical agency. A past role, several years of senior in-house paid media work in healthcare, is part of the experience and is deliberately left out: no employer name, budget or result from that work appears on this site.</p>
</div></section>
""",
"faq": [
('Can you work with a UK limited company or a sole trader?', 'Yes. The engagement is a short services agreement covering scope, the monthly fee in pounds, 30 days\' notice and confidentiality. There is no minimum term.'),
('How is VAT handled?', 'Quotes are ex VAT. Because I supply services from outside the UK, the reverse charge normally applies and you account for the VAT in your own return. The invoice states the treatment clearly.'),
('What about UK GDPR and cookie consent?', 'Tracking is set up with Consent Mode v2 and a consent banner that really does block marketing tags until the visitor agrees. If you already use a consent platform, I work with it rather than replace it.'),
('Are you an agency?', 'No. Diwizi is a consultancy with one consultant. When a project needs a designer or a developer, I bring in a named person for that piece of work and tell you who it is.'),
('Does the time difference get in the way?', 'Rarely. Most of the work is done in writing and does not need a meeting. Calls are booked ahead, usually in the UK afternoon, and written replies come within one working day.'),
],
"related": ['results', 'ppc-management', 'ppc-consultant-london', 'contact'],
},
{
    "slug": "faq", "short": "FAQ",
    "blurb": "Answers for UK and Irish businesses: fees, VAT, Google's 2% surcharge, consent, contracts and how the work runs.",
    "title": "PPC Consultancy FAQ | Fees, VAT, Consent and Contracts",
    "meta": "48 answers for UK and Irish businesses hiring an independent PPC consultant: how fees work, VAT and Google's 2% surcharge, Consent Mode v2, contracts and notice.",
    "kicker": "About",
    "h1": "Questions UK businesses ask before hiring a PPC consultant",
    "lead": "Two sets of answers: how PPC and Google Ads work here, from fees to the first month, and what changes when you hire from the UK, from VAT and Google's surcharge to consent and contracts.",
    "proof": [],
    "body": "",
    "related": ["about", "pricing", "ppc-audit", "contact"],
    "faq_groups": FAQ_GROUPS,
},

{
"slug": 'contact',
"short": 'Contact',
"blurb": 'Book a call, send the form or write an email. All three reach the same person.',
"title": 'Contact | PPC Consultancy UK, Quotes in Pounds Within One Working Day',
"meta": 'Send your spend, site and what is going wrong. Diego Zietek replies personally within one working day, often the same day, with a range in pounds, ex VAT.',
"kicker": 'Contact',
"h1": 'Get a quote. The reply comes from the consultant, not a sales team.',
"lead": 'A few details are enough for me to say whether I can help, where I would start and roughly what it would cost. If someone else would suit you better, I will say so and suggest who.',
"proof": [],
"body": """
<section><div class="wrap">
<div class="cols">
<div class="card"><h3>Use the form</h3><p>Your spend, name, email, site and what is going wrong. You will find it <a href="#form">at the foot of this page</a> and on every other page. One reply, written by me, within one working day, often the same day.</p></div>
<div class="card"><h3>Or email</h3><p>If you would rather write, send the same details to {{email}}. If you already know you want an audit, read-only access to Google Ads and GA4 speeds things up.</p></div>
</div>
<h2 style="margin-top:36px">What helps me reply properly</h2>
<ul>
<li>Your approximate monthly spend, and the platforms it goes on.</li>
<li>What the accounts are meant to produce: enquiries, booked calls, demos or pipeline.</li>
<li>Who runs them at the moment: you, a colleague, an agency, or nobody in particular.</li>
<li>What made you look: costs creeping up, enquiries getting worse, a launch coming, or reports you no longer trust.</li>
</ul>
<p>You do not need to give access to get a range. Read-only access only comes into it if we agree on an audit.</p>
</div></section>
""",
"faq": [
('Will you add me to a sales sequence?', 'No. You get one reply, from me. If you do not answer it, I take it that the timing is wrong and leave it there.'),
('Can we talk outside UK office hours?', 'Within reason, yes. Tell me in the form which times suit you and I will suggest a slot.'),
('Should I send access to the account with my enquiry?', 'Only if you want to. Read-only access makes my reply more specific, but a range does not need it.'),
],
"related": ['ppc-audit', 'ppc-management', 'pricing', 'about'],
"cta_title": 'Get a quote in pounds',
"cta_text": 'Your spend, your site and what is going wrong. One reply, with a straight answer and a range.',
},
]
