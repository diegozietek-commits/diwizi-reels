# Comparison lists added in November 2026: UK PPC agencies, UK performance marketing agencies, UK lead generation
# companies and a directory of independent UK PPC consultants. Same rules as the lists on diwizi.com:
# the page says it is not independent, this practice is listed first with reasons that link to public pages, every other
# company is in alphabetical order with no score, and each line about another company is a fact read on its own website
# on the date shown. Nobody paid or was contacted. UK spelling. No prices, no fee form, no contract length.

READ_ON = "13 November 2026"


def _entry(name, url, text, facts=""):
    """Other companies are named only: no link and no web address on the page (owner, 13 Nov 2026).
    The URL stays in this file as the record of which site each fact was read on. Internal URLs are linked."""
    f = f'<p class="price">{facts}</p>' if facts else ""
    head = f'<a href="{url}">{name}</a>' if url.startswith("/") else name
    return f'<div class="card"><h3>{head}</h3><p>{text}</p>{f}</div>'


FIVE_CHECKS = """
<ul>
<li><strong>A named senior person runs the account.</strong> Not a team described in general terms.</li>
<li><strong>The ad account stays in the client's name.</strong> Stated in writing, before any agreement.</li>
<li><strong>There is at least one case with real account numbers.</strong> With the period and what each number means.</li>
<li><strong>There is original data, with source, date and method.</strong> Published work shows how a provider reads a market.</li>
<li><strong>How the fee is set is explained in writing.</strong> Before any work starts.</li>
</ul>
"""

OWN_ENTRY = """
<div class="card"><h3>1. PPC Consultancy</h3>
<p><strong>Best for</strong> UK and Irish businesses that want one senior specialist running Google, Microsoft and Meta Ads personally, with conversion tracking that can be trusted before the budget goes up.</p>
<p>PPC Consultancy is the independent practice of Diego Willian Zietek, a PPC consultant with 14+ years of hands-on work. This is what it shows on each of the five checks, with a page where you can verify it.</p>
<ul>
<li><strong>Who runs the account.</strong> Diego Willian Zietek, personally, with no account manager and no junior team. See <a href="/about/">who runs your account</a>.</li>
<li><strong>Who owns the account.</strong> Google Ads, GA4, Tag Manager and Meta stay in your company's name. If the work stops, access is removed and everything stays with you.</li>
<li><strong>Cases with real numbers.</strong> Trutek, Google Ads managed since 2020: 5,707 clicks and about 260 contact conversions. A health plan reseller: 651 quote requests in October 2019. Neither is British, and each is set out with its limits on the <a href="/results/">results page</a>.</li>
<li><strong>Original data.</strong> A study of <a href="/guides/google-ads-advertisers-measurement-uk/">what 230 UK businesses paying for Google Ads measure</a>, by sector, and <a href="/guides/google-ads-cost-uk/">top of page bids for 42 UK searches</a>, each with source, date and method.</li>
<li><strong>How the fee is set.</strong> Explained on the <a href="/pricing/">pricing page</a>, and agreed in writing before anything starts.</li>
<li><strong>Where it works.</strong> Based in Curitiba, Brazil, working remotely on UK hours, in English. A business that wants meetings in person should choose a company with a UK office.</li>
</ul>
</div>
"""

AGENCIES = [
    ("Brainlabs", "https://www.brainlabsdigital.com/", "Describes itself as a full-service media agency.", "Founded in 2012, according to its site"),
    ("Circus PPC", "https://circusppc.com/", "A PPC and paid media specialist and a Google Premier Partner agency, in its own words.", "Founded in 2009"),
    ("Clean Digital", "https://cleandigital.co.uk/", "A UK PPC agency whose employee-owned team manages paid search, paid social and programmatic.", "Based in Edinburgh · operating since 2012"),
    ("Digital Gearbox", "https://digitalgearbox.co.uk/", "A PPC agency managing Google Ads, Meta Ads and LinkedIn for UK businesses.", "Operating since 2013"),
    ("Genie Goals", "https://www.geniegoals.co.uk/", "Works with e-commerce brands. Its site names PPC, paid social and affiliate marketing as the core services.", "A team of 30 based in Cambridge"),
    ("Loud Mouth Media", "https://www.loudmouth-media.com/", "A digital marketing agency covering PPC, SEO, social and performance creative.", "Offices in Belfast, Glasgow, Dublin and London"),
    ("PPC Geeks", "https://ppcgeeks.co.uk/", "A Google Ads agency and Google Premier Partner.", "Offices in London, Knutsford, Manchester, Liverpool and the Lake District · founded in 2017"),
    ("Prime Digital", "https://primedigital.co/", "A PPC agency offering strategy-led paid advertising for service businesses.", "Based in Glasgow · in business since 2012"),
    ("Vervaunt", "https://vervaunt.com/", "An e-commerce and paid media consultancy working with retail businesses.", "Offices in London and New York · founded in 2013"),
]

PERFORMANCE = [
    ("Bidmark", "https://bidmark.co.uk/", "A performance marketing agency for small and medium-sized businesses and young brands.", "Based in Leeds"),
    ("DemandMore", "https://clicteq.com/", "A performance marketing agency specialising in paid search, paid social and programmatic advertising.", "Based in London"),
    ("Growthcurve", "https://growthcurve.co/", "Describes itself as a growth marketing agency working as a full-funnel marketing team.", ""),
    ("House of Performance", "https://houseofperformance.co.uk/", "Performance marketing for brands that want to get more from their paid media.", "London"),
    ("Impression", "https://www.impressiondigital.com/", "A performance marketing agency.", "Offices in Nottingham, London, Manchester and New York · founded in 2012"),
    ("Launch", "https://www.launchonline.co.uk/", "A performance marketing agency and Google Premier Partner offering paid media, conversion rate optimisation and data insights.", ""),
    ("Mabo", "https://www.mabo.co.uk/", "Describes itself as a performance marketing agency at its core.", "Founded in 2013"),
    ("Renowned", "https://renowned.co.uk/", "A performance marketing agency.", "London"),
    ("Space &amp; Time", "https://www.spaceandtime.co.uk/", "A growth marketing agency.", "Offices in London, Manchester, Edinburgh, Reigate and Bournemouth"),
]

LEADGEN = [   # (name, url, what its site says it sells, model)
    ("Achieve UK", "https://www.achieveuk.com/", "B2B telemarketing and appointment setting for small businesses. Established in 1998.", "Telephone"),
    ("B2B Sales Leads", "https://b2bsalesleads.co.uk/", "B2B lead generation and appointment setting, prospect data and outsourced sales development.", "Telephone and data"),
    ("Beach Marketing", "https://beachmarketing.co.uk/", "B2B marketing for industrial brands with long buying cycles. Operating since 2008.", "Agency"),
    ("Beanstalk Marketing", "https://www.beanstalkmarketing.co.uk/", "B2B telemarketing and lead generation campaigns. Operating since 2009.", "Telephone"),
    ("Catalyst Marketing Agency", "https://wearecatalyst.co.uk/", "Digital marketing and lead generation for small and medium-sized businesses. Offices in Birmingham and London.", "Agency"),
    ("Choose Leads", "https://chooseleads.co.uk/", "B2C and B2B marketing data for telemarketing, email, postal and SMS campaigns.", "Data"),
    ("Leadly", "https://leadly.co.uk/", "Lead generation, SEO, PPC, CRM, creative and out of home. Based in Manchester.", "Agency"),
    ("Smartlead Marketing", "https://smartleadmarketing.co.uk/", "B2B telemarketing and lead generation.", "Telephone"),
    ("The Lead Generation Agency", "https://theleadgenerationagency.uk/", "B2B lead generation through outreach, SEO and paid search. Based in London, operating since 2016.", "Outreach and paid search"),
    ("Toucan Telemarketing", "https://www.toucantelemarketing.co.uk/", "Telemarketing and B2B appointment setting. Based in Cheshire, near Manchester.", "Telephone"),
]

CONSULTANTS = [   # the publisher first (and the page says so), then alphabetical by the name each one trades under
    ("Diego Willian Zietek, PPC Consultancy", "/", "The publisher of this page. Google, Microsoft and Meta Ads, landing pages and conversion tracking, with 14+ years of experience.", "Based in Curitiba, Brazil, working on UK hours"),
    ("Dan Brown", "https://danbrownppc.co.uk/", "Freelance PPC consultant managing Google Ads and Meta Ads, with 15+ years of experience.", "Bournemouth"),
    ("Elevate PPC", "https://www.elevate-ppc.co.uk/", "Freelance PPC and Google Ads consultant offering management, audits and consultancy. Founded by Becky Carr.", "Leamington Spa, Warwickshire"),
    ("George Stevens", "https://georgestevens.co.uk/", "PPC consultant working mainly in Google Ads, with 15 years of experience.", "Near Leeds"),
    ("Mike Ncube", "https://www.mikencube.co.uk/", "Google Ads specialist and PPC consultant, working in digital marketing since 2008.", ""),
    ("PPC Help", "https://ppchelp.co.uk/", "Freelance PPC contractor for agencies and businesses, with over 18 years on Google Ads and Microsoft Ads.", ""),
    ("Results First", "https://results-first.com/", "PPC and SEO consultancy, training and Google Ads reviews for UK businesses and agencies.", "Andover, Hampshire"),
    ("Rob Owlett", "https://robowlett.com/", "Freelance e-commerce and marketing consultant covering PPC, SEO and conversion rate optimisation.", "Keighley, West Yorkshire"),
    ("SGP Digital", "https://www.sgpdigital.co.uk/", "Digital marketing consultant focused on lead generation for service businesses.", "Liverpool"),
    ("Stevie Morris", "https://steviemorris.com/", "Freelance PPC consultant with 14 years in Google Ads, working with e-commerce and home services businesses.", "UK-wide"),
    ("The PPC Machine", "https://www.theppcmachine.co.uk/", "David Miles teaches UK mortgage brokers and financial advisers to run their own Google Ads.", ""),
]

DISCLOSURE = ('<p class="note"><strong>Disclosure.</strong> PPC Consultancy publishes this page and is on it. {first} '
              f'Every other company is in alphabetical order, described with facts read on its own website on {READ_ON}. None of them paid to be here or was contacted. '
              'If something has changed, a correction can be requested through the <a href="/contact/#form">form</a>.</p>')

PERFORMANCE_SECTION = (
    '<section id="agencies"><div class="wrap">\n<h2>Performance marketing agencies in the UK: nine to compare</h2>\n'
    + DISCLOSURE.format(first="It is not one of the nine below, because it is a consultancy of one and not an agency.")
    + "\n<p>If an agency is what you need, these nine describe themselves as performance or growth marketing agencies and state on their own websites what they do. The order is alphabetical and is not a ranking.</p>\n"
    + '<div class="cols">' + "".join(_entry(*e) for e in PERFORMANCE) + "</div>\n"
    + '<p>Whichever you speak to, ask who will work in your account every week, who owns the ad accounts, and whether the report shows your own numbers or only the platform\'s. A list of PPC specialists is on <a href="/best-ppc-agencies-uk/">PPC agencies in the UK</a>.</p>\n</div></section>\n')

LEADGEN_SECTION = (
    '<section id="companies"><div class="wrap">\n<h2>Lead generation companies in the UK, by what they sell</h2>\n'
    + DISCLOSURE.format(first="It is not in the table, because it sells one thing only: enquiries from your own paid campaigns.")
    + "\n<p>The words lead generation cover very different services. The table sorts ten UK companies by what their own websites say they sell, so you can tell which kind you are talking to. The order is alphabetical and is not a ranking.</p>\n"
    + "<table><thead><tr><th>Company</th><th>What its website says it sells</th><th>Kind</th></tr></thead><tbody>"
    + "".join(f'<tr><td>{n}</td><td>{t}</td><td>{k}</td></tr>' for n, u, t, k in LEADGEN)
    + "</tbody></table>\n"
    + "<p><strong>Telephone</strong> means people calling prospects on your behalf to book appointments. <strong>Data</strong> means contact lists you then use yourself. <strong>Agency</strong> means marketing campaigns that bring enquiries to you. Before you sign with any of them, ask where each lead comes from, whether it is sold to anyone else, and how the people on a list agreed to be contacted.</p>\n</div></section>\n")

PAGES = [

# ---------------------------------------------------------------- Best PPC agencies UK
{
"slug": "best-ppc-agencies-uk", "short": "PPC agencies in the UK", "blurb": "Nine UK PPC agencies and one consultancy, with what to check before you sign with any of them.",
"title": "Best PPC Agencies in the UK (2026): Agencies and Consultants Compared",
"meta": "Best PPC agencies in the UK for 2026: nine agencies and one independent consultancy, with facts from their own websites and five checks to run before you sign.",
"kicker": "2026 comparison",
"h1": "Best PPC agencies and consultants in the UK",
"lead": "The best PPC agency for a national retailer is rarely the best one for a service business with a tight budget. This page lists nine UK PPC agencies and one independent consultancy, says plainly who publishes it, and sets out what to check before you sign with any of them.",
"proof": [],
"body": """
<section><div class="wrap">
""" + DISCLOSURE.format(first="It is listed first for the reasons given under the criteria, each one linked to a page you can check.") + """
<h2>The short answer</h2>
<p>For a business that wants a PPC specialist running the account personally, the first pick on this list is PPC Consultancy, the independent practice of Diego Willian Zietek: 14+ years of hands-on work, the ad account kept in the client's name, published cases with real account numbers and its own data on UK advertisers. PPC Consultancy publishes this list. For large retail accounts, several markets or heavy creative production, a larger agency from the list brings more structure. Before you sign with any of them, ask who will work in your account every week.</p>
</div></section>

<section id="criteria"><div class="wrap">
<h2>How this list was built</h2>
<p>To be included, a company had to meet four conditions.</p>
<ul>
<li>PPC or paid media is named as a core service on the company's own website.</li>
<li>It is based in the UK or has a UK office.</li>
<li>There are public facts that can be checked on its own website, read on """ + READ_ON + """.</li>
<li>Freelancer marketplaces, course sellers and directories were left out.</li>
</ul>
<h3>What decided the first position</h3>
<p>Client results, fees and service quality cannot be checked from outside a company. So this list does not rank the companies against each other, and none gets a score. What any buyer can check, on any provider's public pages, is five things.</p>
""" + FIVE_CHECKS + """
<p>PPC Consultancy is first because it is the company on this list for which the proof behind all five can be shown first hand, and each proof is a public page linked in its entry below. For the others this list can only report what their websites state, so they follow in alphabetical order. Run the same five checks on any of them before you sign.</p>
</div></section>

<section id="list"><div class="wrap">
<h2>The companies, one by one</h2>
<p>Position one is explained under the criteria above. From position two onward the order is alphabetical, and position is not a score.</p>
""" + OWN_ENTRY + """
<div class="cols" style="margin-top:18px">""" + "".join(
    _entry(f"{i}. {n}", u, t, f) for i, (n, u, t, f) in enumerate(AGENCIES, 2)) + """</div>
</div></section>

<section><div class="wrap">
<h2>How to choose between them</h2>
<ol class="steps">
<li><div><strong>Who works in the account.</strong> Ask for the name of the person who will open your account every week and how many other accounts they handle.</div></li>
<li><div><strong>Who owns the account.</strong> Google Ads, GA4 and Tag Manager stay in your company's name, with you as administrator.</div></li>
<li><div><strong>How the fee is agreed.</strong> In writing, including what happens if the budget falls or doubles.</div></li>
<li><div><strong>What the report shows.</strong> Cost per qualified enquiry and per customer, not only clicks and impressions.</div></li>
<li><div><strong>Whether the tracking can be trusted.</strong> In a study of 230 UK advertisers, fewer than half showed a Google Ads conversion tag. Ask to see yours working. <a href="/guides/google-ads-advertisers-measurement-uk/">The study →</a></div></li>
</ol>
<p>If you are not sure the current account is being run well, a written <a href="/ppc-audit/">PPC audit</a> answers that before you change provider. The longer comparison between the two models is on <a href="/agency-vs-consultant/">PPC agency vs PPC consultant</a>, and consultants who work alone are listed in the <a href="/independent-ppc-consultants-uk/">directory of independent UK PPC consultants</a>.</p>
</div></section>

<section><div class="wrap">
<h2>Sources and method</h2>
<p>Each description comes from the company's own home or about page, read on """ + READ_ON + """. Where a site did not state a location or a founding year, none is given. The companies whose websites were read: """ + ", ".join(
    n for n, _, _, _ in AGENCIES) + """.</p>
</div></section>
""",
"faq": [
("What is the best PPC agency in the UK?", "It depends on the account. A national retailer with several markets needs the structure of a large agency. A service business that wants one senior person in the account is better served by a specialist or an independent consultant. This page lists nine agencies and one consultancy, with five checks to run on any of them."),
("Why is PPC Consultancy listed first?", "Because it publishes this list, and it is the company here whose proof on five checks can be shown first hand: a named senior person runs the account, the ad account stays in the client's name, there are cases with real account numbers, there is original data with source and date, and how the fee is set is explained in writing. The other companies are in alphabetical order, without scores. The position is not a rating of them."),
("Is this list independent, and did anyone pay to be on it?", "It is not independent. PPC Consultancy publishes the page and is on it. That is why every claim about it links to a page where it can be checked, and the other companies are described only with facts from their own websites. None of them paid or was contacted."),
("Should I hire a PPC agency or an independent consultant?", "An agency suits accounts with several markets or languages, heavy creative output or channels such as affiliates and programmatic. A consultant suits one business that wants the senior person doing the work and answering the questions. The comparison is on <a href=\"/agency-vs-consultant/\">PPC agency vs PPC consultant</a>."),
("What should I ask before signing with any of them?", "Who will work in the account every week, who owns the ad accounts, how the fee is agreed, what the report shows, and how you can see that conversion tracking works."),
("How much does a PPC agency cost in the UK?", "Agencies commonly charge a percentage of ad spend with a minimum, or a monthly retainer, and the figures vary widely with the size of the account. The <a href=\"/pricing/\">pricing page</a> explains the models and how to compare quotes."),
],
"related": ["agency-vs-consultant", "ppc-audit", "performance-marketing", "ppc-management"],
},

# ---------------------------------------------------------------- Directory of independent UK PPC consultants
{
"slug": "independent-ppc-consultants-uk", "short": "Independent PPC consultants", "blurb": "A directory of PPC consultants who work alone for UK businesses, with what each one's own website says.",
"title": "Independent PPC Consultants in the UK: A Directory (2026)",
"meta": "A directory of independent PPC consultants and Google Ads freelancers working with UK businesses, with facts from their own websites and how to choose one.",
"kicker": "Directory",
"h1": "Independent PPC consultants in the UK: a directory",
"lead": "Independent PPC consultants are hard to find in a search full of agencies and job boards. This is a short directory of people who run paid search accounts themselves for UK businesses, with what each one's own website says. It is kept by one of them, who is listed first. The others follow in alphabetical order.",
"proof": [],
"body": """
<section><div class="wrap">
<p class="note"><strong>Disclosure.</strong> This directory is published by PPC Consultancy, the practice of Diego Willian Zietek, who is listed first for that reason alone. Everyone else is in alphabetical order, and nobody is ranked or scored. Each line is a fact read on the consultant's own website on """ + READ_ON + """. Nobody paid to be here or was contacted first. If you are listed and something is wrong, or you would like to be removed, use the <a href="/contact/#form">form</a>.</p>
<h2>The directory</h2>
<div class="cols">""" + "".join(_entry(n, u, t, f) for n, u, t, f in CONSULTANTS) + """</div>
</div></section>

<section><div class="wrap">
<h2>Who was included</h2>
<ul>
<li>One person, or a practice built around one named person, who does the account work personally.</li>
<li>PPC or Google Ads is the main service on their own website.</li>
<li>They work with UK businesses.</li>
<li>Their website appeared on Google UK for searches such as freelance PPC consultant UK or Google Ads freelancer UK on """ + READ_ON + """.</li>
</ul>
<p>Agencies, job boards and freelancer marketplaces were left out. The list is not complete, and being absent says nothing about anyone's work. Independent UK consultants who would like to be added can ask through the form.</p>
</div></section>

<section><div class="wrap">
<h2>How to choose an independent consultant</h2>
<ol class="steps">
<li><div><strong>Ask for a written review first.</strong> A consultant can read your account with read-only access and tell you in writing what is wrong before any ongoing work is agreed.</div></li>
<li><div><strong>Check the fit by sector.</strong> Several people on this list say on their own sites which kinds of business they work with. Believe them.</div></li>
<li><div><strong>Ask what happens when they are away.</strong> One person means one diary. A good answer is specific.</div></li>
<li><div><strong>Keep the accounts in your name.</strong> Whoever you choose, Google Ads, GA4 and Tag Manager belong to your business.</div></li>
</ol>
<p>If your account needs several markets, heavy creative production or a team in the room, an agency is the better choice. Nine are listed on <a href="/best-ppc-agencies-uk/">PPC agencies in the UK</a>, and the difference between the two models is on <a href="/agency-vs-consultant/">PPC agency vs PPC consultant</a>.</p>
</div></section>
""",
"faq": [
("What is an independent PPC consultant?", "A specialist who runs paid search accounts personally, without an agency team around them. You speak to the person who does the work."),
("Is this directory a ranking?", "No. The publisher is listed first, which is said at the top of the page, and everyone else is in alphabetical order. Nobody is scored."),
("How were the consultants found?", "Their websites appeared on Google UK for searches such as freelance PPC consultant UK and Google Ads freelancer UK on " + READ_ON + ", and each site shows one named person doing the account work with PPC as the main service."),
("Can I be added or removed?", "Yes. Use the form on this site. Additions need a website that shows who does the work and that PPC is the main service."),
("Should I choose a consultant near me?", "It rarely matters for the work itself, which is done in the accounts and in writing. It matters if you want meetings in person, and in that case choose someone within reach."),
],
"related": ["ppc-freelancer", "agency-vs-consultant", "ppc-consultation", "ppc-audit"],
},

]
