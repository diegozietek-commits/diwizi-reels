# Guide: Google Ads targeting rules for housing, employment and credit ads (US and Canada). American English. Single dict P, no imports.

P = {
"slug": "google-ads-housing-employment-credit",
"short": "Housing, jobs and credit ads",
"blurb": "The five targeting options Google bans for home, job and credit ads in the US and Canada, what still works, and how to fix an affected campaign.",
"title": "Google Ads for Housing, Jobs or Credit: What You Can't Target in the US",
"meta": "Google Ads rules for housing, employment and credit ads in the US and Canada: which targeting is off limits, what still works, and how to fix an affected campaign.",
"kicker": "Housing, jobs and credit ads",
"h1": "Running Google Ads for homes, jobs or loans? Five targeting options are off limits in the US and Canada",
"lead": "If you sell or rent homes, recruit, or offer loans or credit cards, Google applies a separate set of targeting rules to your ads in the United States and Canada. The rules date from October 2020, but they still catch real estate agents, mortgage brokers, staffing firms and lenders who copy a campaign from another business or let an agency apply a standard audience setup. This guide sets out what Google restricts, what you can still use, and what to change today.",
"body": """
<section><div class="wrap">
<h2>Who the rules apply to</h2>
<p>Google groups these businesses under "Access to opportunities categories (US and Canada only)" in its <a href="https://support.google.com/adspolicy/answer/143465?hl=en" rel="noopener" target="_blank">personalized advertising policy</a>. Enforcement follows where the ads are shown, not where you are based. Google's <a href="https://support.google.com/adspolicy/answer/9997418?hl=en" rel="noopener" target="_blank">FAQ on the policy</a> says: "The focus of the enforcement will be on ad target geo location and not based on advertiser's billing or physical location."</p>
<table>
<tr><th>Category</th><th>Google's description</th><th>Restricted examples</th><th>Not restricted, per Google's FAQ</th></tr>
<tr><td>Housing</td><td>"homes for sale or rental ... as well as products or services enabling the sale or rental of homes" (<a href="https://support.google.com/adspolicy/answer/16701755" rel="noopener" target="_blank">housing page</a>)</td><td>Listing sites, a single home for sale, real estate agents or brokers</td><td>Hotels and vacation rentals, office space, property management services</td></tr>
<tr><td>Employment</td><td>"employment opportunities or hiring a person for a job" (<a href="https://support.google.com/adspolicy/answer/16700442" rel="noopener" target="_blank">employment page</a>)</td><td>Job ads, recruitment and job listing sites, freelance or gig job listings</td><td>Career advice, employment training, networking services</td></tr>
<tr><td>Consumer finance (credit)</td><td>"offers relating to credit, banking products and services, or certain financial planning and management services" (<a href="https://support.google.com/adspolicy/answer/16700846" rel="noopener" target="_blank">consumer finance page</a>)</td><td>Credit cards and loans, including home and car loans</td><td>Financial guidance, gift cards</td></tr>
</table>
<p>One detail has moved since 2020. The original FAQ listed checking accounts as not restricted, while Google's current consumer finance page lists "Banking and checking accounts" as an example in scope. Treat banking products as in scope.</p>
<p>You do not declare the category yourself. Google's FAQ says it reviews "both the ad text and landing page", and for Display and YouTube ads the visual elements too.</p>
</div></section>

<section><div class="wrap">
<h2>The five targeting options you can't use</h2>
<p>Google's policy pages for all three categories list the same five for the United States and Canada: gender, age, parental status, marital status and ZIP codes. In practice, per Google's FAQ:</p>
<ul>
<li><strong>Age, gender and parental status</strong> must target everyone, and bid adjustments on them must be "reverted to 0% or removed".</li>
<li><strong>Detailed demographics</strong> for marital status and parental status must be removed.</li>
<li><strong>The life event "Marriage"</strong>, including getting married soon and recently married, must be removed.</li>
<li><strong>ZIP code targeting</strong> must be removed. In Canada the full postal code is out, but Google says the first three characters (the FSA) are acceptable.</li>
<li><strong>Customer Match and remarketing lists</strong> are only affected "if they use demographics, Marriage/Marital Status, Parental status, or ZIP Code signals to build users lists."</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>What still works</h2>
<p>From Google's policy pages: "Targeting geographic locations using radius, as well as city and country-based targeting is allowed. Radius targeting requires setting at least 1 km around any given location."</p>
<p>Google's FAQ lists as not restricted: household income, homeownership status, education, in-market and affinity segments, custom segments, life events other than marriage, and city, county, DMA and radius targeting.</p>
<p>Keywords are not part of these rules. A Search campaign built on what people type, such as "homes for sale in Plano", "CDL driver jobs Dallas" or "refinance rates", remains the cleanest way to reach buyers in these categories.</p>
</div></section>

<section><div class="wrap">
<h2>Why this matters for the business, not only for compliance</h2>
<ul>
<li><strong>A ZIP code list is the most common casualty.</strong> Agents and lenders often target the ten ZIP codes they know best. Rebuild the same map with a radius around each neighborhood, or with city and county targeting.</li>
<li><strong>Age targeting is the second.</strong> A senior living community or a first-time buyer program cannot narrow by age in Google Ads. The precision has to come from keywords and from landing pages written for that buyer.</li>
<li><strong>Ads stop, and so do new campaigns.</strong> Google's FAQ says ads using the restricted targeting "will stop serving", and that an account cannot create new campaigns until the policy has been accepted.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>What to do today</h2>
<ol class="steps">
<li><div><strong>Open Policy Manager in Google Ads.</strong> Google's FAQ says "Impacted ads will be included in the Policy Manager page of your Google Ads account."</div></li>
<li><div><strong>Fix the audiences.</strong> In each campaign that advertises homes, jobs or credit, set age, gender and parental status to all, and remove marital and parental detailed demographics and the Marriage life event.</div></li>
<li><div><strong>Fix the locations.</strong> Replace ZIP codes with a radius of at least 1 km, cities or counties.</div></li>
<li><div><strong>Check your lists.</strong> If a Customer Match or remarketing list was built from age, gender, marital status or ZIP code, stop using it in these campaigns.</div></li>
<li><div><strong>Let the ad be reviewed again.</strong> Google: "Your ad will be automatically reviewed again." Check the status in "Ads &amp; assets".</div></li>
<li><div><strong>Move the precision into keywords and pages.</strong> That is where it now lives. A <a href="/google-ads-audit/">Google Ads audit</a> covers this in one pass if several campaigns are affected.</div></li>
</ol>
<p>A longer guide to real estate campaigns, including this policy, is on <a href="https://diwizi.com/blog/real-estate-lead-generation-google-ads.html" rel="noopener">diwizi.com</a>.</p>
</div></section>
""",
"faq": [
("Do these rules apply if my business is based outside the US?", "Yes, if the ads target people in the United States or Canada. Google's FAQ says enforcement is based on where the ad is targeted, not on the advertiser's billing or physical location."),
("Can I still target my city with housing or loan ads?", "Yes. Google allows city, county and DMA targeting and a radius of at least 1 km. ZIP code targeting is not allowed for these ads in the US, and full postal codes are not allowed in Canada."),
("Is a property management company affected?", "Google's FAQ lists property management services as not restricted and promoting homes for sale or rental as restricted. If your ads promote specific rentals, assume the rules apply."),
("Are keywords restricted for housing, job or credit ads?", "No. The restrictions cover demographics, the Marriage life event, lists built from those signals and ZIP codes. Keyword targeting is not part of them, which makes Search campaigns the most precise option left."),
("Does Meta have the same rule?", "Meta has its own Special Ad Categories for housing, employment and credit, with similar limits. This guide covers Google only."),
],
"messages": [
"Housing in personalized advertising",
"Employment in personalized advertising",
"Consumer finance in personalized advertising",
"Restricted targeting",
"Policy Manager",
],
"sources": [
"https://support.google.com/adspolicy/answer/143465?hl=en",
"https://support.google.com/adspolicy/answer/16701755",
"https://support.google.com/adspolicy/answer/16700442",
"https://support.google.com/adspolicy/answer/16700846",
"https://support.google.com/adspolicy/answer/9917652?hl=en",
"https://support.google.com/adspolicy/answer/9997418?hl=en",
],
"related": ["/google-ads-audit/", "/small-business-ppc-management/", "/google-ads-consultation/"],
}
