# B2B sector pages added on 16 Nov 2026: manufacturing, construction, fintech and accountants.
# Written for the UK from scratch (the diwizi.com sector pages were a model of structure only, never of text).
# Rules for this file: paid media only, Sales Qualified Leads as the qualification term, British English, no em dash,
# no semicolons, no prices or values in pounds or dollars, no new client figures, no claims about how fees are or are not
# charged. Sentences that quote the UK B2B study are wrapped in <!--if-page:...--> so they appear only once the study
# page itself is published (see build.py).

STUDY = "guides/b2b-google-ads-measurement-uk"
STUDY_URL = "/" + STUDY + "/"


def study(html):
    """Wrap text that quotes or links the UK B2B study, so it is published together with the study."""
    return f"<!--if-page:{STUDY}-->{html}<!--/if-page-->"


PROOF = [("SQL", "the conversion bidding learns from"), ("CRM", "stages sent back to Google Ads"),
         ("1", "senior consultant on the account"), ("14+", "years in paid media")]

CTA = ("What you sell, who buys it and what the account does today. You get a straight answer on whether I can help "
       "and what I would look at first.")


def cases(sector):
    return f"""
<section id="cases"><div class="wrap">
<h2>What has been run before</h2>
<div class="cols">
<div class="card"><h3>Trutek, truck suspension parts, Brazil</h3><p>Brand, website and Google Ads Search since 2020, for a specialist supplier with few searches and valuable enquiries. The account's history shows 5,707 clicks and about 260 attributed contact conversions. A conversion here is a contact action recorded by Google Ads, not a sale.</p></div>
<div class="card"><h3>Pontomais, HR software, Brazil</h3><p>Google Ads rebuilt from scratch while I worked there as an employee, from August 2017, with daily alignment with the sales team. Contact requests from Google Ads went from roughly five a month to the hundreds over eight months. These are approximate volumes from my own experience on the project.</p></div>
</div>
<p>No case from {sector} has been published here. The cases above come from other sectors and show how the work is done when the sale is slow and decided outside the ad account. Each one, with its limits, is on the <a href="/results/">results page</a>.</p>
</div></section>
"""


def searches(rows):
    body = "".join(f"<tr><td>{s}</td><td>{w}</td><td>{d}</td></tr>" for s, w, d in rows)
    return f"<table><thead><tr><th>Search</th><th>Who usually types it</th><th>What to do with it</th></tr></thead><tbody>{body}</tbody></table>"


def leaks(items):
    return '<div class="cols">' + "".join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in items) + "</div>"


def includes(items):
    return '<ol class="steps">' + "".join(f"<li><div><strong>{h}</strong> {p}</div></li>" for h, p in items) + "</ol>"


PAGES = [

# ---------------------------------------------------------------- Manufacturing
{
"slug": "manufacturing-marketing", "short": "Manufacturing marketing", "blurb": "Google Ads for UK manufacturers and engineering firms, judged on the enquiries sales accepts.",
"title": "Manufacturing Marketing UK | Google Ads for Manufacturers",
"meta": "Manufacturing marketing through paid search for UK manufacturers and engineering firms. Google Ads judged on Sales Qualified Leads, not on form fills.",
"kicker": "Manufacturing marketing",
"h1": "Manufacturing marketing through Google Ads, judged on the enquiries your sales team accepts",
"lead": "On this site, manufacturing marketing means paid media, with Google Ads first and Microsoft Advertising beside it. It is for UK manufacturers and engineering firms that sell to other businesses, such as a contract manufacturer, a component supplier, a fabricator or a machine builder. The buyer is an engineer or a buyer working to a specification, the order is large and the sale closes weeks later, so the account is built around the Sales Qualified Lead rather than the form.",
"proof": PROOF, "cta_text": CTA, "service_name": "Manufacturing marketing through paid search",
"body": """
<section><div class="wrap">
<h2>What is manufacturing marketing through paid search?</h2>
<p>It is buying the searches engineers and buyers make when they need a supplier, a process or a part, and sending each one to a page that answers the specification. Google Ads covers the searches that name the process, the material or the standard. Microsoft Advertising reaches the same buyers on work computers. LinkedIn Ads can support the account when search volume is too small to fill the pipeline, aimed at named companies and job titles, but it is not where the work starts.</p>
</div></section>

<section><div class="wrap">
<h2>Where manufacturing ad budgets leak</h2>
""" + leaks([
    ("Students and apprentices", "Searches such as what is injection moulding, CNC machining course or welding apprenticeship share the words of the services you sell. Without a negative list from the first day, part of every month's budget pays for coursework."),
    ("Job seekers", "CNC machinist jobs near me and engineering vacancies in your town look like your keywords to broad match. They keep arriving every week until they are excluded by name."),
    ("One-off and hobby buyers", "Someone who wants a single bracket cut for a car restoration fills in the same form as a buyer with an annual schedule. The click costs the same and the value does not."),
    ("Suppliers selling to you", "Toolmakers, software vendors and material suppliers search the same terms to find manufacturers to sell to, and many of them use your enquiry form. A form that asks for the part, the quantity and the drawing filters most of them out."),
]) + """
</div></section>

<section><div class="wrap">
<h2>Which manufacturing searches are worth buying</h2>
""" + searches([
    ("contract manufacturing uk", "A buyer looking to outsource production", "Buy, with a page that states capacity, certifications and lead times"),
    ("precision cnc machining services", "An engineer with a drawing to place", "Buy, with a form that accepts the drawing"),
    ("iso 9001 sheet metal fabrication", "A buyer working to a quality requirement", "Buy, and name the certification in the advert"),
    ("cnc machinist jobs", "A job seeker", "Exclude as a negative keyword"),
    ("cnc machining course", "A student or an apprentice", "Exclude"),
    ("laser cutting near me", "A hobby or one-off buyer", "Exclude, or send it to a page that states the minimum order"),
]) + """
<p>Real search terms vary by process and by region, so the list is rebuilt from your own search terms report in the first weeks.</p>
</div></section>

<section><div class="wrap">
<h2>What manufacturing marketing here includes</h2>
""" + includes([
    ("Campaigns by process and by industry served.", "Machining, fabrication, moulding or assembly, each with its own budget, so a strong line does not hide a weak one."),
    ("Negative keywords from the first day.", "Jobs, courses, definitions and hobby terms are excluded before launch and the list is reviewed every week."),
    ("A form that qualifies.", "It asks for the company, the part or process, the quantity and a drawing, so sales can tell a real enquiry within a minute."),
    ("Sales Qualified Leads sent back to Google Ads.", 'The enquiries sales accepts, and the quotes that follow, go back to the account as conversions. See <a href="/conversion-tracking/">conversion tracking</a>.'),
    ("A page per process.", 'With the tolerances, materials, certifications and lead times a buyer checks first. See <a href="/landing-pages/">landing pages</a>.'),
    ("A monthly report your sales lead can check.", "Cost per Sales Qualified Lead and per quote, by process, next to the platform numbers."),
]) + """
</div></section>
""" + study("""
<section><div class="wrap">
<h2>What UK manufacturers measure today</h2>
<p>Manufacturers measure better than most B2B sectors, and still rarely close the loop to sales. In our <a href="/guides/b2b-google-ads-measurement-uk/">study of 66 UK B2B companies running Google Ads</a>, 52% of the 23 manufacturing and engineering sites carried a Google Ads tag, and 9% showed a CRM or automation script next to it. Bidding cannot learn from a quote it never hears about.</p>
</div></section>
""") + cases("manufacturing") + """
<section><div class="wrap">
<h2>Who this fits</h2>
<p>UK manufacturers and engineering firms that sell to other businesses, with a sales team or an owner who follows up enquiries, and a product or capacity that buyers search for by name. It is not for consumer products sold online, which is the work described on <a href="/ecommerce-ppc/">e-commerce PPC</a>, and it is not for recruiting staff, which is a separate job.</p>
</div></section>
""",
"faq": [
("Does Google Ads work for manufacturers?", "Yes, when buyers search for the process, the material or the standard you work to. The volume is small, so the account has to cover every relevant search, exclude the rest and count the enquiries sales accepts rather than every form."),
("Our products are made to order. What do buyers search for?", "The process, the material, the tolerance and the certification, often with a location or the word supplier. Those searches are fewer than consumer searches, and the people behind them usually have a drawing ready."),
("How do you stop job seekers clicking our ads?", "With negative keywords for jobs, vacancies, apprenticeships and salaries from the first day, adverts that state who the service is for, and a weekly read of the search terms report to catch the new variations."),
("Should we use Performance Max?", "Not at the start. Performance Max needs a conversion that reflects the quality of an enquiry, otherwise it drifts towards cheap placements. Search comes first, and Performance Max is tested once Sales Qualified Leads flow back from the CRM."),
("Can you connect Google Ads to our CRM?", "Usually, through enhanced conversions for leads or an offline import from the CRM. Where enquiries live only in email or an ERP, a simple shared sheet of accepted enquiries does most of the job at first."),
("How much does manufacturing marketing cost?", 'The fee is set from the scope: the platforms, the number of process lines, the landing pages and whether CRM work is included. The <a href="/pricing/">pricing page</a> explains how it is worked out, and the quote comes in writing after a look at the account. Your ad spend is paid straight to Google.'),
],
"related": ["b2b-ppc", "conversion-tracking", "landing-pages", "ppc-audit"],
},

# ---------------------------------------------------------------- Construction
{
"slug": "construction-marketing", "short": "Construction marketing", "blurb": "Google Ads for UK contractors that win work from businesses and clients who commission projects.",
"title": "Construction Marketing UK | Google Ads for Contractors",
"meta": "Construction marketing through paid search for UK contractors that sell work to businesses. Google Ads judged on site visits and tenders, not on calls.",
"kicker": "Construction marketing",
"h1": "Construction marketing through Google Ads, for contractors who sell work to businesses",
"lead": "On this site, construction marketing means paid media, with Google Ads first. It is for UK contractors that win work from businesses and from clients who commission projects, such as commercial fit-out, groundworks, steel frame, mechanical and electrical, refurbishment and specialist trades working for main contractors, developers, facilities managers and building owners. Homeowners looking for a builder and people looking for site work are a different audience, and keeping them out is half of the job.",
"proof": PROOF, "cta_text": CTA, "service_name": "Construction marketing through paid search",
"body": """
<section><div class="wrap">
<h2>What is construction marketing through paid search?</h2>
<p>It is buying the searches a client makes when a project needs a contractor, and making sure the enquiry that arrives is one you would price. Google Ads covers the searches that name the trade, the type of building and the area. Microsoft Advertising adds the same buyers on work computers. The goal is an enquiry that becomes a site visit or a tender, counted as a Sales Qualified Lead, and not a call about a garden wall.</p>
</div></section>

<section><div class="wrap">
<h2>Where construction ad budgets leak</h2>
""" + leaks([
    ("Job seekers and site workers", "Searches for a CSCS card, labouring jobs, site manager vacancies or construction salaries share words with your services. They are excluded by name, and the list grows every week from the search terms report."),
    ("Homeowners and do it yourself", "How to build an extension, cheap builders near me and DIY plastering come from people planning their own home project. A commercial contractor pays for those clicks unless the adverts and the negatives say who the work is for."),
    ("Projects outside your range", "A small domestic job and a multi-site fit-out arrive through the same form. Without questions about the type of project, the location and the start date, the estimator spends the week on enquiries the firm would never price."),
    ("Subcontractors and suppliers", "Plant hire firms, merchants and subcontractors looking for main contractors to work with search the same terms and fill in the same enquiry form."),
]) + """
</div></section>

<section><div class="wrap">
<h2>Which construction searches are worth buying</h2>
""" + searches([
    ("commercial fit out contractors", "A facilities or property manager planning a refurbishment", "Buy, with a page that shows sectors, project types and accreditations"),
    ("groundworks contractors manchester", "A developer or main contractor looking for a subcontractor", "Buy, only in the areas you cover"),
    ("design and build contractor", "A business owner commissioning a building", "Buy, with a page for each building type you deliver"),
    ("cscs card test", "Someone starting work on site", "Exclude as a negative keyword"),
    ("construction jobs near me", "A job seeker", "Exclude"),
    ("diy extension plans", "A homeowner doing the work themselves", "Exclude"),
]) + """
<p>The exact terms depend on the trade and the region, so the list is rebuilt from your own search terms report in the first weeks.</p>
</div></section>

<section><div class="wrap">
<h2>What construction marketing here includes</h2>
""" + includes([
    ("Campaigns by trade, building type and area.", "So the budget follows the work you want, in the places your teams can reach."),
    ("Negative keywords from the first day.", "Jobs, training, cards, salaries and do it yourself terms are excluded before launch and reviewed every week."),
    ("An enquiry form that sorts projects.", "It asks for the type of project, the location, the approximate size and the start date, so the estimator can answer the right enquiries first."),
    ("Site visits and tenders sent back to Google Ads.", 'The enquiries that reached a site visit or a tender go back to the account as conversions, so bidding learns from real projects. See <a href="/conversion-tracking/">conversion tracking</a>.'),
    ("A page per service and per building type.", 'With the accreditations you hold, such as CHAS, SafeContractor or Constructionline, and photographs of comparable work. See <a href="/landing-pages/">landing pages</a>.'),
    ("A monthly report in site visits and tenders.", "Cost per Sales Qualified Lead and per tender, by trade and area, next to the platform numbers."),
]) + """
</div></section>
""" + study("""
<section><div class="wrap">
<h2>What UK B2B advertisers measure today</h2>
<p>Our <a href="/guides/b2b-google-ads-measurement-uk/">study of 66 UK B2B companies running Google Ads</a> did not have a construction group. The closest, manufacturing and engineering, showed 52% of sites with a Google Ads tag and 9% with a CRM or automation script beside it. Across all 66 sites, 26% showed no measurement at all.</p>
</div></section>
""") + cases("construction") + """
<section><div class="wrap">
<h2>Who this fits</h2>
<p>UK contractors that sell work to businesses, developers, main contractors and building owners, with someone who visits sites and prices work promptly. It is not for builders who work mainly for homeowners, and it does not cover public sector frameworks, which are won through procurement and not through adverts.</p>
</div></section>
""",
"faq": [
("Does Google Ads work for commercial contractors?", "Yes, for private and commercial clients who search when a project comes up. The searches are fewer than for domestic trades, so every relevant one is covered, the rest is excluded and success is counted in site visits and tenders."),
("How do you keep job seekers and CSCS searches out?", "With negative keywords for jobs, vacancies, salaries, cards, tests and courses from the first day, and a weekly read of the search terms report. Adverts that name the client type help as well."),
("Our work comes through tenders and frameworks. Can paid search help?", "For private and commercial work, yes, because those clients search when they need a contractor. Public sector frameworks are won through procurement portals, and no advert changes that, so the account is aimed at the clients who search."),
("How soon can we see whether it works?", "Clicks and enquiries arrive within days of launch. Judging cost per site visit or tender takes longer, because it depends on how quickly enquiries are followed up and priced, so the first review uses enquiries sales accepted."),
("Should we advertise across the whole of the UK?", "Only where your teams can work profitably. Location targeting by region or radius keeps the budget on projects you can staff, and areas are added once the first ones are proven."),
("How much does construction marketing cost?", 'The fee is set from the scope: the platforms, the number of trades and areas, the landing pages and whether CRM work is included. The <a href="/pricing/">pricing page</a> explains how it is worked out, and the quote comes in writing after a look at the account. Your ad spend is paid straight to Google.'),
],
"related": ["b2b-ppc", "conversion-tracking", "landing-pages", "ppc-audit"],
},

# ---------------------------------------------------------------- Fintech
{
"slug": "fintech-marketing", "short": "Fintech marketing", "blurb": "Google Ads for UK fintech and financial services firms, with verification and promotion rules first.",
"title": "Fintech Marketing UK | Google Ads for Regulated Financial Firms",
"meta": "Fintech marketing through paid search for UK firms. Google verification and the financial promotion rules first, then Google Ads judged on accounts opened.",
"kicker": "Fintech marketing",
"h1": "Fintech marketing through Google Ads, with verification and the promotion rules settled first",
"lead": "On this site, fintech marketing means paid media, with Google Ads first. It is for UK fintech and financial services firms selling payments, lending, accounts, wealth or finance software with a regulated side. In this sector the campaign is the second step. Google's verification and the rules on financial promotions come first, and an account that skips them is paused before it learns anything.",
"proof": [("FCA", "authorisation checked before launch"), ("SQL", "or account opened, as the conversion"), ("CRM", "stages sent back to Google Ads"), ("14+", "years in paid media")],
"cta_text": CTA, "service_name": "Fintech marketing through paid search",
"body": """
<section><div class="wrap">
<h2>What is fintech marketing through paid search?</h2>
<p>It is buying the searches of people and businesses looking for the financial product you offer, inside two sets of rules. Google will not show financial services ads to people in the UK until the advertiser shows FCA authorisation or an exemption and completes Google's own advertiser verification. UK law restricts financial promotions to those made or approved by an authorised person, unless an exemption applies. Both are set out step by step in the guide to <a href="/guides/google-ads-financial-services-verification-uk/">Google Ads financial services verification in the UK</a>.</p>
</div></section>

<section><div class="wrap">
<h2>Where fintech ad budgets leak</h2>
""" + leaks([
    ("Spend before verification", "An account that starts before financial services verification is approved collects disapproved adverts and lost weeks. The usual causes are a company name that does not match the FCA register and a payments profile in another name."),
    ("Copy that fails the promotion rules", "Rates, returns or speed claims written by the ad team and never cleared by compliance. Every advert and landing page is a financial promotion, and the approval trail has to exist before it goes live."),
    ("Existing customers counted as new", "People searching for your brand with login, app or contact click the brand adverts and are reported as acquisition. They belong in their own campaign and their own line of the report."),
    ("Job seekers, students and researchers", "Fintech jobs in London, what is open banking and fintech courses share the words of the category, and none of them opens an account."),
]) + """
</div></section>

<section><div class="wrap">
<h2>Which fintech searches are worth buying</h2>
""" + searches([
    ("invoice finance for small business", "An owner with cash tied up in unpaid invoices", "Buy, with a page that explains eligibility before the form"),
    ("payment gateway for uk business", "A finance or product lead choosing a provider", "Buy, with a comparison you can stand behind"),
    ("open banking api provider", "A product team at a business", "Buy, with a demo request as the conversion"),
    ("fintech jobs london", "A job seeker", "Exclude as a negative keyword"),
    ("what is fintech", "A student or researcher", "Exclude"),
    ("yourbrand login", "An existing customer", "Exclude from acquisition campaigns and leave to the brand campaign"),
]) + """
<p>The examples are generic. The real list depends on the product, the customer and what your permissions allow you to promote.</p>
</div></section>

<section><div class="wrap">
<h2>What fintech marketing here includes</h2>
""" + includes([
    ("Verification before the first click.", 'Financial services verification and advertiser verification completed in the right legal name. See the <a href="/guides/google-ads-financial-services-verification-uk/">verification guide</a>.'),
    ("Copy and pages through your compliance sign-off.", "Adverts and landing pages go to whoever approves your financial promotions, and the approval trail is kept."),
    ("Campaigns by product and by customer type.", "Business and consumer products apart, so each one has its own budget and its own conversion."),
    ("Conversions that mean something.", 'An application completed, an account opened or a demo held, sent from your CRM or onboarding system back to Google Ads. See <a href="/conversion-tracking/">conversion tracking</a>.'),
    ("Landing pages that answer eligibility.", 'Who the product is for, what is needed to apply and the risk wording your approver requires. See <a href="/landing-pages/">landing pages</a>.'),
    ("Brand and new customers reported apart.", "So the cost of a new customer is not flattered by people who already have an account."),
]) + """
</div></section>
""" + study("""
<section><div class="wrap">
<h2>What UK B2B advertisers measure today</h2>
<p>Our <a href="/guides/b2b-google-ads-measurement-uk/">study of 66 UK B2B companies running Google Ads</a> did not have a financial services group. Across all 66 sites, 47% carried a Google Ads tag and only 5% showed a CRM or automation script next to it. For a product where the value lies in the account opened, not in the form, that gap matters more than in most sectors.</p>
</div></section>
""") + cases("fintech or financial services") + """
<section><div class="wrap">
<h2>Who this fits</h2>
<p>UK fintech and financial services firms that are authorised, or work under an authorised firm that approves their promotions, and that have someone who can sign off adverts. It is not for firms that cannot show authorisation or an exemption, because Google will not show the adverts, and it is not for anything Google's financial products policy does not allow.</p>
</div></section>
""",
"faq": [
("Can a fintech advertise on Google in the UK before FCA authorisation?", 'Not for regulated financial services. Google asks for FCA authorisation or an exemption before financial services ads can show to UK users. Where an authorised firm approves your promotions, Google has a request type for that firm to have a third party verified. The <a href="/guides/google-ads-financial-services-verification-uk/">verification guide</a> sets out each route.'),
("How long does verification take?", "It depends on how clean the application is. A company name that matches the FCA register, an account managed from inside the firm and a payments profile in the right name are what keep it to weeks rather than months."),
("Who signs off the adverts?", "Your compliance function, or the authorised person who approves your financial promotions. I write the adverts and the pages, and nothing goes live without that approval."),
("Does Google Ads work for B2B fintech?", "Yes, when businesses search for the product, such as payments, invoice finance or banking software. The volume is small, so the account covers every relevant search and counts demos and accounts opened rather than form fills."),
("What should Google Ads optimise for?", "The deepest step that still happens often, usually an application completed or an account opened. A funded account or a first transaction is imported as a secondary conversion and reported, until there are enough of them for bidding to learn from."),
("How much does fintech marketing cost?", 'The fee is set from the scope: the platforms, the number of products, the landing pages, the compliance rounds and whether CRM work is included. The <a href="/pricing/">pricing page</a> explains how it is worked out, and the quote comes in writing after a look at the account. Your ad spend is paid straight to Google.'),
],
"related": ["guides/google-ads-financial-services-verification-uk", "b2b-ppc", "conversion-tracking", "ppc-audit"],
},

# ---------------------------------------------------------------- Accountants
{
"slug": "marketing-for-accountants", "short": "Marketing for accountants", "blurb": "Google Ads for UK accountancy and bookkeeping practices that want business clients who fit.",
"title": "Marketing for Accountants UK | Google Ads for Accountancy Firms",
"meta": "Marketing for accountants through paid search. Google Ads for UK accountancy and bookkeeping practices, judged on clients who fit, not one-off returns.",
"kicker": "Marketing for accountants",
"h1": "Marketing for accountants through Google Ads, aimed at the clients who fit your practice",
"lead": "On this site, marketing for accountants means paid media, with Google Ads first. It is for UK accountancy and bookkeeping practices that want new business clients from search, such as limited companies, sole traders moving to a firm, contractors and landlords with a portfolio. The aim is a client who fits the practice, counted as a Sales Qualified Lead, and not a rush of one-off tax return enquiries in January.",
"proof": PROOF, "cta_text": CTA, "service_name": "Marketing for accountants through paid search",
"body": """
<section><div class="wrap">
<h2>What is marketing for accountants through paid search?</h2>
<p>It is buying the searches of business owners looking for an accountant, and leaving out the much larger number of people looking for a free answer. Google Ads covers the searches that name the client type, the service and the town. Microsoft Advertising adds the same owners on work computers. The goal is an enquiry that becomes an engagement letter, not a quote for a single return.</p>
</div></section>

<section><div class="wrap">
<h2>Where accountancy ad budgets leak</h2>
""" + leaks([
    ("The January rush", "Self assessment season brings a flood of searches for a single return, often from people comparing on price. They can be served, but only if that is a service you want, with its own campaign and its own budget."),
    ("People who file themselves", "HMRC login, how to file my own tax return and free accounting software come from people who want to do it alone. They are excluded from the first day."),
    ("Students and job seekers", "ACCA course, trainee accountant and accountant jobs share every word of your category, and none of them is a client."),
    ("Work the practice does not take", "Specialisms you do not cover and towns you do not serve arrive through the same form. A few questions on the form and tight location settings keep the diary for the clients you want."),
]) + """
</div></section>

<section><div class="wrap">
<h2>Which accountancy searches are worth buying</h2>
""" + searches([
    ("accountant for limited company", "A director looking for annual accounts and tax", "Buy, with a page that sets out what the service covers"),
    ("accountants for contractors", "A contractor working through their own company", "Buy, if the practice takes contractors"),
    ("switch accountant", "An owner unhappy with the current firm", "Buy, with a page that explains how the handover works"),
    ("hmrc login", "A taxpayer filing on their own", "Exclude as a negative keyword"),
    ("acca course", "A student", "Exclude"),
    ("accountant jobs", "A job seeker", "Exclude"),
]) + """
<p>The right list depends on the client types you want and the towns you serve, so it is rebuilt from your own search terms report in the first weeks.</p>
</div></section>

<section><div class="wrap">
<h2>What marketing for accountants here includes</h2>
""" + includes([
    ("Campaigns by client type and service.", "Limited companies, contractors, landlords and sole traders apart, so the budget follows the clients you want most."),
    ("Budgets that follow the year.", "The self assessment season, year ends and the quieter months planned in advance rather than discovered in the report."),
    ("A form that qualifies.", "It asks for the type of business, the number of employees and the service needed, so the partner can answer the right enquiries first."),
    ("New clients sent back to Google Ads.", 'Calls and forms tracked, and the enquiries that became engagement letters returned to the account as conversions. See <a href="/conversion-tracking/">conversion tracking</a>.'),
    ("A page per client type.", 'Each one says who the service is for, what is included and how switching works. See <a href="/landing-pages/">landing pages</a>.'),
    ("A monthly report in clients won.", "Cost per Sales Qualified Lead and per new client, by client type, next to the platform numbers."),
]) + """
</div></section>
""" + study("""
<section><div class="wrap">
<h2>What UK B2B advertisers measure today</h2>
<p>Our <a href="/guides/b2b-google-ads-measurement-uk/">study of 66 UK B2B companies running Google Ads</a> did not have an accountancy group. The closest, recruitment, calibration and consultancy firms, showed 38% of sites with a Google Ads tag and none with a CRM or automation script beside it.</p>
</div></section>
""") + cases("accountancy") + """
<section><div class="wrap">
<h2>Who this fits</h2>
<p>UK accountancy and bookkeeping practices that want business clients and have a partner or manager who answers enquiries the same day. It is not for practices that only want seasonal tax return work at the lowest price, and it is not for recruiting staff or trainees.</p>
</div></section>
""",
"faq": [
("Does Google Ads work for accountancy practices?", "Yes, when the campaigns are aimed at business clients rather than one-off returns. Owners search for an accountant by client type, service and town, and those searches can be covered completely while the free-answer searches are excluded."),
("How do we avoid a flood of one-off self assessment enquiries?", "By excluding single-return and price-led searches, or giving them a separate campaign with a small budget if you want some of that work. The form and the adverts then say which clients the practice takes."),
("Should a small practice advertise beyond its own town?", "Usually not at first. Most owners want an accountant they can meet, so the account starts with the towns you serve and widens only for services you deliver remotely, such as contractor accounts."),
("Can Google Ads tell us which enquiries became clients?", "Yes, if the enquiries that became engagement letters are sent back to the account. A practice management system or a simple shared sheet of signed clients is enough to start."),
("How soon will new clients arrive?", "Enquiries arrive within days of launch. New clients take longer, because of the time from first call to engagement letter, so the first reviews use enquiries the practice accepted."),
("How much does marketing for accountants cost?", 'The fee is set from the scope: the platforms, the number of client types and towns, the landing pages and whether CRM work is included. The <a href="/pricing/">pricing page</a> explains how it is worked out, and the quote comes in writing after a look at the account. Your ad spend is paid straight to Google.'),
],
"related": ["b2b-ppc", "conversion-tracking", "landing-pages", "ppc-audit"],
},

]
