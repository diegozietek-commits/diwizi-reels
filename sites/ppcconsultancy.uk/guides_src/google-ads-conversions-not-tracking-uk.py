# Guide: Google Ads conversions not tracking (UK). British English. Single dict P, no imports.

P = {
"slug": "google-ads-conversions-not-tracking-uk",
"short": "Conversions not tracking",
"blurb": "What Unverified, Tag inactive and No recent conversions mean, how to tell a dead tag from a quiet week, and why bidding goes wrong when the tag dies.",
"title": "Google Ads Conversions Not Tracking: 6 Checks That Find the Fault",
"meta": "Google Ads conversions not tracking? What Unverified, Tag inactive and No recent conversions mean, six checks an owner can ask for, and why bidding breaks.",
"kicker": "Conversions not tracking",
"h1": "Google Ads conversions not tracking: how to tell a dead tag from a quiet week, and why bidding breaks when it dies",
"lead": "Google Ads shows one of a handful of status strings on the Conversions page, and each one separates two very different problems: nothing happened, or nothing was measured. A dead tag, a consent banner that blocks it, a thank-you page that moved, or a GA4 key event that was never imported all produce the same empty column. The checks below can be asked for without logging in, and the last section explains why a campaign on Smart Bidding gets worse, not just blind, when its conversions stop arriving.",
"body": """
<section><div class="wrap">
<h2>The status strings on the Conversions page, in Google's words</h2>
<p>Google has used two generations of labels on the conversion actions table, and both are still documented on its help pages, so you may meet either depending on how your account is laid out. The older per-action tracking statuses are defined on Google's <a href="https://support.google.com/sa360/answer/9780742?hl=en-GB" rel="noopener" target="_blank">conversion tracking status page</a>. The newer overview statuses are defined in Google's <a href="https://support.google.com/google-ads/troubleshooter/13455130?hl=en-GB" rel="noopener" target="_blank">conversion tracking troubleshooter</a>.</p>
<table>
<tr><th>Status</th><th>Google's definition</th><th>Happened or measured?</th><th>What to ask for</th></tr>
<tr><td>Unverified</td><td>"We haven't verified that your tag has been put on your website yet."</td><td>Nothing measured yet. Normal for a few hours after set-up.</td><td>A Tag Assistant test of the thank-you page. Google's <a href="https://support.google.com/google-ads/answer/11198131?hl=en-GB" rel="noopener" target="_blank">troubleshooting page</a> treats Unverified lasting more than 24 hours as a problem.</td></tr>
<tr><td>No recent conversions</td><td>"We've seen your conversion tracking tag, but haven't recorded any conversions over the last seven days."</td><td>Tag is alive. Possibly nothing happened, possibly the trigger never fires.</td><td>Your own count of enquiries for the same seven days. If you had some, the trigger is wrong.</td></tr>
<tr><td>Recording conversions</td><td>"We've seen your conversion tag and recorded conversions over the last seven days."</td><td>Measured. Check the count against your inbox anyway.</td><td>The conversion count by action, to reconcile.</td></tr>
<tr><td>Tag inactive</td><td>"We can no longer see your tag, and haven't recorded any conversions over the last seven days."</td><td>Not measured. The tag was there and has gone.</td><td>The date the tag was last seen (hover on the status) and what changed on the website that day.</td></tr>
<tr><td>Inactive</td><td>Google's <a href="https://support.google.com/google-ads/answer/1722022?hl=en-GB" rel="noopener" target="_blank">conversion measurement page</a> says a new tag may show "Unverified" or "Inactive" and becomes "Active" after the first recorded conversion or a successful test event.</td><td>Not measured yet.</td><td>A successful test event through Tag Assistant.</td></tr>
<tr><td>Active</td><td>"indicates that everything is working as intended."</td><td>Measured.</td><td>Nothing, beyond the monthly reconciliation.</td></tr>
<tr><td>Needs attention</td><td>"action items to address but that haven't stopped recording conversions entirely."</td><td>Partly measured.</td><td>The list of alerts behind the status.</td></tr>
<tr><td>Misconfigured</td><td>"Conversions have stopped recording entirely due to a setup error or a broken tag."</td><td>Not measured.</td><td>The steps shown when hovering the status, and who will do them by when.</td></tr>
<tr><td>Awaiting conversions</td><td>"No conversions have been recorded in the last seven days."</td><td>Unclear. Google says this typically means the action is under 48 hours old, campaigns are paused or traffic is too low.</td><td>The age of the action and whether campaigns are live.</td></tr>
</table>
<p>The column that matters to an owner is the third one. "Nothing happened" is a marketing problem. "Nothing measured" is a plumbing problem, and no change to keywords, ads or budget will fix plumbing.</p>
</div></section>

<section><div class="wrap">
<h2>"No conversions happened" versus "nothing was measured"</h2>
<p>The quickest separation is a reconciliation that needs no access to Google Ads at all. Count the enquiries your business received from the website in the last seven days, from your inbox, phone system or CRM. Then compare with the conversion count in the account for the same seven days, remembering that Google's <a href="https://support.google.com/google-ads/answer/6270625?hl=en-GB" rel="noopener" target="_blank">conversion data page</a> says reporting lags can take 24 to 48 hours and that the main columns are dated by the click, not by the day the enquiry arrived.</p>
<ul>
<li><strong>Inbox has enquiries, Google Ads has zero.</strong> Nothing was measured. The tag is dead, blocked or on the wrong page.</li>
<li><strong>Inbox has enquiries, Google Ads has far more.</strong> The wrong things are being counted, usually page views, button clicks or a GA4 event that fires on every visit.</li>
<li><strong>Both have zero.</strong> Nothing happened. Check that campaigns are live and that the ads are showing before blaming the tag.</li>
<li><strong>Roughly the same, within the lag.</strong> Measured. Google's page says a discrepancy of up to 20 percent against third-party tools is expected when comparing by conversion time.</li>
</ul>
<p>Most "conversions not tracking" tickets I see are the first case, and most of those trace to a website change nobody told the account manager about.</p>
</div></section>

<section><div class="wrap">
<h2>Six checks an owner can ask for</h2>
<p>You do not need to run these yourself. You need to ask for them by name and expect a screenshot or a sentence back for each.</p>
<ol class="steps">
<li><div><strong>Tag Assistant on the thank-you page.</strong> Google's <a href="https://support.google.com/tagassistant/answer/10039345?hl=en-GB" rel="noopener" target="_blank">Tag Assistant</a> connects to your site and shows the hits sent and any errors while you click through, and Google's <a href="https://support.google.com/google-ads/answer/10989978?hl=en-GB" rel="noopener" target="_blank">troubleshooting guide</a> for Unverified, Tag inactive and Needs attention actions walks through it: connect, trigger the conversion on the site, close the tool, and the status updates in roughly 30 minutes.</div></li>
<li><div><strong>Tag Manager preview.</strong> If the tag lives in Google Tag Manager, <a href="https://support.google.com/tagmanager/answer/6107056?hl=en-GB" rel="noopener" target="_blank">preview mode</a> lists the tags that fired on the page and the tags present that did not fire for each event. A conversion tag sitting in the second list on the thank-you page is the fault, found.</div></li>
<li><div><strong>The thank-you page itself.</strong> Open it. Website redesigns rename /thank-you to /thanks, forms switch to an on-page success message with no new URL, or a booking tool opens in a frame on another domain. The trigger was written for the old behaviour and never fires again.</div></li>
<li><div><strong>The cookie banner.</strong> UK sites need consent before setting non-essential cookies under PECR and UK GDPR, and most consent banners block Google tags until the visitor accepts. If the Google Ads conversion tag is blocked by the banner and nothing else is configured, every visitor who ignores or declines the banner converts invisibly. The next section covers how consent mode changes this.</div></li>
<li><div><strong>GA4 key events versus Google Ads conversions.</strong> Many UK accounts measure in GA4 and assume Google Ads sees the same thing. It does not, unless the key event has been created as a Google Ads conversion. Google's <a href="https://support.google.com/analytics/answer/13965727?hl=en-GB" rel="noopener" target="_blank">conversions versus key events</a> page describes the chain as Event, then Key Event, then Conversion, with a linked Google Ads account required. Its <a href="https://support.google.com/analytics/answer/10632359?hl=en-GB" rel="noopener" target="_blank">import page</a> lists the prerequisites: the accounts linked, auto-tagging on, and editor rights on the property.</div></li>
<li><div><strong>Offline conversion import.</strong> If enquiries are qualified in a CRM and uploaded back, Google's <a href="https://support.google.com/google-ads/answer/2998031?hl=en-GB" rel="noopener" target="_blank">offline conversion import</a> page explains that each click carries a GCLID that must be stored with the lead and sent back when it converts. The conversion measurement page adds that uploads take 24 to 48 hours to process and that the GCLID must be within 90 days of the click. A CRM that stopped storing the GCLID looks exactly like a campaign that stopped converting.</div></li>
</ol>
<p>Each of these is a yes or no. A supplier who cannot give you six quick answers is telling you the measurement has not been looked at, which is also the first thing a <a href="/ppc-audit/">PPC audit</a> checks before any opinion is offered on the campaigns.</p>
</div></section>

<section><div class="wrap">
<h2>Cookie consent, PECR and consent mode on UK sites</h2>
<p>This is the UK-specific failure. A compliant cookie banner is not optional for a UK business, and the Information Commissioner's Office enforces the rules under PECR alongside UK GDPR. The side effect for measurement is that a banner which simply blocks all Google tags until acceptance makes a share of your real enquiries disappear from Google Ads, and the share is whatever proportion of visitors never click accept.</p>
<p>Google's answer is consent mode, documented on its <a href="https://support.google.com/google-ads/answer/10000067?hl=en-GB" rel="noopener" target="_blank">consent mode page</a>. In basic consent mode, Google tags are blocked until the visitor interacts with the banner and nothing at all is sent when they decline. In advanced consent mode, tags load when the page opens, send cookieless pings while consent is denied, and send full data once consent is granted. Google uses the pings to model conversions it cannot observe, and the page says impact figures appear after consent mode has been live for at least seven full days. Google Tag Manager's <a href="https://support.google.com/tagmanager/answer/10718549?hl=en-GB" rel="noopener" target="_blank">consent mode support page</a> lists the consent types and notes that ad_user_data is required for enhanced conversions and tag-based conversion tracking. A banner that grants ad_storage but never sets ad_user_data is a common reason conversions vanish after a consent platform update.</p>
<p>For an owner, the questions are: does our banner integrate with consent mode, basic or advanced, and did anyone test a conversion after declining the banner? If the answer to the second is no, nobody knows what the declined share looks like in your reports. This work sits inside the <a href="/conversion-tracking/">conversion tracking</a> build rather than being left to whoever installed the banner.</p>
</div></section>

<section><div class="wrap">
<h2>Why bidding goes wrong when the tag dies</h2>
<p>A dead tag is not only a reporting problem. If the campaign uses Smart Bidding, the tag is the steering wheel. Google's <a href="https://support.google.com/google-ads/answer/7065882?hl=en-GB" rel="noopener" target="_blank">Smart Bidding page</a> says Target CPA, Target ROAS, Maximise conversions and Maximise conversion value optimise for conversions in every auction and that conversion tracking must be enabled before you create one. Google recommends judging them over periods with at least 30 conversions, and around 50 for Target ROAS.</p>
<p>Take away the conversions and three things follow. First, the strategy keeps bidding on its last good data, which ages by the day, so it buys clicks that resembled converters in a different month. Second, Google's <a href="https://support.google.com/google-ads/answer/1722131?hl=en-GB" rel="noopener" target="_blank">campaign statuses page</a> notes that "Eligible (misconfigured)" usually means no biddable conversions were recorded in the last 28 days, and its <a href="https://support.google.com/google-ads/answer/6263057?hl=en-GB" rel="noopener" target="_blank">bid strategy statuses page</a> describes "Misconfigured" as a conversion-based strategy without the right conversion actions set up. Third, when the tag is fixed, Google's <a href="https://support.google.com/google-ads/answer/13020501?hl=en-GB" rel="noopener" target="_blank">Smart Bidding learning page</a> says a significant change to the conversion goals being optimised puts the strategy into Learning, which never lasts more than seven days, and performance should then be judged over two conversion cycles or two weeks, whichever is longer.</p>
<p>The reverse failure is worse. If the tag counts page views or every form field click as a conversion, Smart Bidding will dutifully find the visitors most likely to view pages, and the account will report a wonderful cost per conversion while the phone stays silent. That is why I treat "which actions are primary" as the first question in every account, and why the <a href="/landing-pages/">landing pages</a> I build carry a single, deliberate conversion event rather than whatever the website builder emits.</p>
</div></section>

<section><div class="wrap">
<h2>What to do today, and what not to do</h2>
<ol class="steps">
<li><div><strong>Reconcile.</strong> Seven days of inbox enquiries against seven days of conversions. Decide whether this is "nothing happened" or "nothing measured".</div></li>
<li><div><strong>Read the status</strong> and the date the tag was last seen. Match that date against website changes, plugin updates and consent banner changes.</div></li>
<li><div><strong>Test one conversion</strong> through Tag Assistant or Tag Manager preview, once with the banner accepted and once declined.</div></li>
<li><div><strong>Check the primary actions.</strong> Anything that is not an enquiry becomes secondary so bidding stops chasing it.</div></li>
<li><div><strong>Protect the bidding</strong> while you fix the tag. Do not raise budgets or change targets on a strategy that cannot see conversions, and expect up to seven days of Learning after the goal is corrected.</div></li>
<li><div><strong>Do not delete and recreate the conversion action.</strong> Google's <a href="https://support.google.com/google-ads/answer/11198131?hl=en-GB" rel="noopener" target="_blank">troubleshooting page</a> says actions with no recorded data for 13 months are removed anyway, and recreating one loses the history that the bidding and your reports depend on.</div></li>
</ol>
</div></section>

<section><div class="wrap">
<h2>Keeping the measurement honest</h2>
<ul>
<li>Reconcile conversions against the inbox or CRM monthly, and keep the two numbers in the same report.</li>
<li>Tell whoever runs the account before any website, form, booking tool or consent banner change, and test one conversion the same day it goes live.</li>
<li>Keep one primary conversion per real business outcome and demote everything else to secondary.</li>
<li>Store the GCLID in the CRM from the first day you run ads, even if you do not import offline conversions yet.</li>
<li>Check the Conversions page status weekly. "Tag inactive" noticed on day two costs a fortnight less than "Tag inactive" noticed at month end.</li>
</ul>
</div></section>
""",
"faq": [
("Why are my Google Ads conversions not showing?", "Either nothing happened or nothing was measured. Compare the enquiries in your inbox for the last seven days with the conversions in the account, allowing for Google's stated 24 to 48 hour reporting lag. If the inbox has enquiries and the account has none, the tag is dead, blocked by the cookie banner or firing on a page that no longer exists."),
("What does Tag inactive mean in Google Ads?", "Google's definition is that it can no longer see your tag and has not recorded any conversions over the last seven days. The tag was there and has gone, usually after a website redesign, a plugin update or a consent banner change. Hover over the status to see the date it was last seen and match that against what changed."),
("How long does Google Ads take to verify a conversion tag?", "Google says the Unverified check takes a few hours and treats an Unverified status lasting more than 24 hours as a problem to troubleshoot. After a Tag Assistant test, Google says the status updates in roughly 30 minutes. Awaiting conversions on a brand new action typically means it is under 48 hours old."),
("Do GA4 key events count as Google Ads conversions?", "Not automatically. Google describes the chain as Event, then Key Event, then Conversion, and the key event only becomes a Google Ads conversion once the accounts are linked, auto-tagging is on and the key event has been created as a conversion. An account that only measures in GA4 can show conversions there and nothing in Google Ads."),
("Why did performance get worse after the conversion tag broke?", "Smart Bidding strategies optimise towards the conversions they can see. With none arriving, the strategy keeps bidding on stale data, the campaign can show Misconfigured, and when the goal is corrected the strategy re-enters Learning, which Google says never lasts more than seven days. Fix the tag before touching budgets or targets."),
],
"messages": [
"Unverified",
"No recent conversions",
"Recording conversions",
"Tag inactive",
"Inactive",
"Active",
"Needs attention",
"Misconfigured",
"Awaiting conversions",
"Removed",
"Eligible (misconfigured)",
"Your website is missing a Google tag",
],
"sources": [
"https://support.google.com/sa360/answer/9780742?hl=en-GB",
"https://support.google.com/google-ads/troubleshooter/13455130?hl=en-GB",
"https://support.google.com/google-ads/answer/11198131?hl=en-GB",
"https://support.google.com/google-ads/answer/10989978?hl=en-GB",
"https://support.google.com/google-ads/answer/1722022?hl=en-GB",
"https://support.google.com/google-ads/answer/6270625?hl=en-GB",
"https://support.google.com/tagassistant/answer/10039345?hl=en-GB",
"https://support.google.com/tagmanager/answer/6107056?hl=en-GB",
"https://support.google.com/analytics/answer/13965727?hl=en-GB",
"https://support.google.com/analytics/answer/10632359?hl=en-GB",
"https://support.google.com/google-ads/answer/2998031?hl=en-GB",
"https://support.google.com/google-ads/answer/10000067?hl=en-GB",
"https://support.google.com/tagmanager/answer/10718549?hl=en-GB",
"https://support.google.com/google-ads/answer/7065882?hl=en-GB",
"https://support.google.com/google-ads/answer/1722131?hl=en-GB",
"https://support.google.com/google-ads/answer/6263057?hl=en-GB",
"https://support.google.com/google-ads/answer/13020501?hl=en-GB",
],
"related": ["/conversion-tracking/", "/ppc-audit/", "/landing-pages/"],
}
