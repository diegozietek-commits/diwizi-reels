# Guide: US state privacy laws (CCPA), cookie banners and Google Ads. American English. Single dict P, no imports.

P = {
"slug": "google-ads-us-privacy-laws",
"short": "US privacy laws and Google Ads",
"blurb": "When the CCPA applies, why it is an opt-out law rather than a cookie banner law, the Do Not Sell or Share link, Global Privacy Control and Google's restricted data processing.",
"title": "Do US Websites Need a Cookie Banner for Google Ads? CCPA Explained",
"meta": "US privacy laws and Google Ads: when the CCPA applies to a business, the Do Not Sell or Share link, Global Privacy Control and Google's restricted data processing.",
"kicker": "US privacy laws",
"h1": "Do you need a cookie banner for Google Ads in the US? What the CCPA actually asks of an advertiser",
"lead": "Owners who see European cookie banners everywhere often assume a US site needs one too before Google Ads or GA4 can run. California's privacy law works differently: it is mostly an opt-out law, and it only applies to businesses above certain thresholds. This guide sets out who the CCPA covers, what it asks of a business that advertises, and what Google offers to help, quoting the official pages. It is not legal advice: if you are near the thresholds, ask a lawyer.",
"body": """
<section><div class="wrap">
<h2>Does the CCPA apply to your business?</h2>
<p>The California Privacy Protection Agency's <a href="https://cppa.ca.gov/faq.html" rel="noopener" target="_blank">FAQ</a> says the CCPA applies to for-profit businesses that do business in California and meet any of these thresholds:</p>
<ul>
<li>"Have a gross annual revenue of $26.625 million or more (effective January 1, 2025) for the preceding calendar year"</li>
<li>"Buy, sell, or share the personal information of 100,000 or more California residents or households"</li>
<li>"Derive 50% or more of their annual revenue from selling or sharing California residents' personal information"</li>
</ul>
<p>The California Attorney General's <a href="https://oag.ca.gov/privacy/ccpa" rel="noopener" target="_blank">CCPA page</a> still shows the original $25 million figure. The agency's FAQ has the adjusted one. The Attorney General's page also says the CCPA "generally does not apply to nonprofit organizations or government agencies".</p>
<p>For most small businesses running Google Ads, none of the three applies. If you are close to one of them, the rest of this guide is the part to read with your lawyer.</p>
</div></section>

<section><div class="wrap">
<h2>Why advertising counts: "sale" and "sharing"</h2>
<p>The Attorney General's page explains that "sharing refers specifically to sharing for cross-context behavioral advertising, which is the targeting of advertising to a consumer based on the consumer's personal information obtained from the consumer's online activity across numerous websites."</p>
<p>In Google Ads terms, that is remarketing and audience lists built from what people did on your site and elsewhere. Showing a Search ad to someone who typed a query is a different thing. So the question for a business covered by the CCPA is not whether it uses Google Ads, but whether it uses data from your site to target people across other sites.</p>
</div></section>

<section><div class="wrap">
<h2>Opt-out, not a cookie banner</h2>
<p>The CCPA gives California residents a "right to opt-out of sale or sharing", including "via a user-enabled global privacy control". It does not require opt-in consent before cookies are set. The opt-in requirement on the Attorney General's page is for minors: businesses "can only sell the personal information of a child that they know to be under the age of 16 if they get affirmative authorization ('opt-in')".</p>
<p>A covered business that sells or shares personal information must offer:</p>
<ul>
<li><strong>A "Do Not Sell or Share My Personal Information" link.</strong> The Attorney General describes "a clear and conspicuous" link on the website, and says businesses "cannot require you to create an account" to use it. The same link must appear in the privacy policy.</li>
<li><strong>Respect for Global Privacy Control.</strong> Consumers "can also submit an opt-out request via a user-enabled global privacy control, like the GPC". A browser with GPC switched on is an opt-out.</li>
<li><strong>A 12-month wait before asking again.</strong> "Businesses must wait at least 12 months before asking you to opt back in to the sale or sharing of your personal information."</li>
</ul>
<p>This is enforced. In August 2022 the Attorney General announced a <a href="https://oag.ca.gov/news/press-releases/attorney-general-bonta-announces-settlement-sephora-part-ongoing-enforcement" rel="noopener" target="_blank">$1.2 million settlement with Sephora</a>, which had allowed third-party tracking on its site and, according to the Attorney General, failed to process opt-out requests "via user-enabled global privacy controls".</p>
</div></section>

<section><div class="wrap">
<h2>What Google offers: restricted data processing</h2>
<p>Google's <a href="https://support.google.com/google-ads/answer/9614122?hl=en" rel="noopener" target="_blank">restricted data processing page</a> describes a mode in which "Google restricts the way it uses certain unique identifiers", acting as your service provider under its US state privacy terms. What changes for the advertiser:</p>
<ul>
<li><strong>Remarketing stops for those users.</strong> "Certain features will be unavailable, including adding users to remarketing lists."</li>
<li><strong>Measurement keeps working.</strong> "Even when restricted data processing is enabled, features, such as conversion tracking and campaign measurement, will continue to function as normal."</li>
<li><strong>Two ways to switch it on in Google Ads.</strong> A "restricted_data_processing" parameter in the Google tag for particular users, such as people who clicked your opt-out link, or a checkbox in the remarketing tag settings for all users in applicable US states.</li>
<li><strong>GPC is handled for you in some states.</strong> Google says it "will turn off ads targeting and activate restrictive data processing (RDP) if we receive a GPC in these U.S. States."</li>
<li><strong>A California exception.</strong> "As of July 1, 2023, restricted data processing is not available in California where the advertiser engages in cross-context behavioral advertising, including Customer Match."</li>
</ul>
<p>Google's <a href="https://business.safety.google/usaprivacy/" rel="noopener" target="_blank">US state privacy page</a> adds that "Advertisers should work with their legal advisors to determine whether and how they should comply with applicable US state privacy laws."</p>
<p>Consent mode is a separate tool. Google's <a href="https://support.google.com/google-ads/answer/10000067?hl=en" rel="noopener" target="_blank">consent mode page</a> says it "lets you communicate your users' cookie or app identifier consent status to Google" and "doesn't provide a consent banner or widget". In advanced mode Google defaults to a consented state unless a choice is made, "though there may be regional behavioral differences for specific areas like the EEA, Switzerland, and the UK". If your ads also reach Europe or the UK, those visitors need a consent banner, and the UK rules are covered on <a href="https://ppcconsultancy.uk/guides/google-ads-conversions-not-tracking-uk/" rel="noopener">ppcconsultancy.uk</a>.</p>
</div></section>

<section><div class="wrap">
<h2>What to do today</h2>
<ol class="steps">
<li><div><strong>Check the three thresholds.</strong> Revenue, the number of California residents or households whose data you buy, sell or share, and the share of revenue from selling or sharing. If none applies, the CCPA does not apply, and you do not need a California opt-out link for it.</div></li>
<li><div><strong>List what your tags do.</strong> Conversion tracking and Search ads are one thing. Remarketing, Customer Match and audience lists are the "sharing" the law is about.</div></li>
<li><div><strong>If you are covered:</strong> add the "Do Not Sell or Share My Personal Information" link to the site and the privacy policy, make it work without an account, and make sure your consent tool honors GPC.</div></li>
<li><div><strong>Connect the opt-out to Google.</strong> Set the restricted_data_processing parameter for users who opt out, or enable it for all users in applicable states. Conversion tracking keeps working either way.</div></li>
<li><div><strong>If you advertise to Europe or the UK,</strong> run a consent banner for those visitors, separately from the US setup.</div></li>
<li><div><strong>Have the setup checked once.</strong> A <a href="/conversion-tracking-setup/">conversion tracking setup</a> covers the tags, consent signals and restricted data processing together.</div></li>
</ol>
<p>A wider look at how privacy changes affect paid media in 2026 is on <a href="https://diwizi.com/blog/privacy-changes-impact-on-ppc-2026.html" rel="noopener">diwizi.com</a>.</p>
</div></section>
""",
"faq": [
("Do US websites need a cookie banner for Google Ads?", "Not under the CCPA in the way European sites do. The CCPA is an opt-out law: businesses it covers must offer a Do Not Sell or Share My Personal Information link and honor Global Privacy Control. Opt-in is required for selling the data of minors under 16. Other states have their own laws, so check with a lawyer if you are close to the thresholds."),
("Does the CCPA apply to small businesses?", "Only if they meet one of three thresholds: gross annual revenue of $26.625 million or more (as adjusted from January 1, 2025), buying, selling or sharing the personal information of 100,000 or more California residents or households, or deriving 50% or more of revenue from selling or sharing it."),
("Is Google Ads remarketing a sale or sharing of data?", "Under the CCPA, sharing means sharing for cross-context behavioral advertising, which targets ads based on activity across websites. Remarketing and audience lists built from site visitors fall into that description. Search ads shown to people who typed a query do not depend on it."),
("Does conversion tracking stop if I enable restricted data processing?", "No. Google says conversion tracking and campaign measurement continue to function as normal. What stops is adding those users to remarketing lists."),
("What is Global Privacy Control?", "A browser setting that signals the user's choice to opt out. The California Attorney General treats it as a valid opt-out request, and in 2022 settled with Sephora for $1.2 million partly for not processing it."),
],
"messages": [
"Do Not Sell or Share My Personal Information",
"Global Privacy Control",
"Restricted data processing",
"restricted_data_processing",
"Consent mode",
],
"sources": [
"https://cppa.ca.gov/faq.html",
"https://oag.ca.gov/privacy/ccpa",
"https://oag.ca.gov/news/press-releases/attorney-general-bonta-announces-settlement-sephora-part-ongoing-enforcement",
"https://support.google.com/google-ads/answer/9614122?hl=en",
"https://business.safety.google/usaprivacy/",
"https://support.google.com/google-ads/answer/10000067?hl=en",
],
"related": ["/conversion-tracking-setup/", "/google-ads-audit/", "/google-ads-management/"],
}
