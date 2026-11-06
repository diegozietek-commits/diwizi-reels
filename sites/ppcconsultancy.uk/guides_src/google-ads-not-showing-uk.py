# Guide: Google Ads not showing (UK). British English. Single dict P, no imports.

P = {
"slug": "google-ads-not-showing-uk",
"short": "Ads not showing",
"blurb": "What each campaign and ad status means, why searching for your own ad proves nothing, and when more budget is the wrong fix.",
"title": "Google Ads Not Showing? What Each Status Really Means",
"meta": "Google ads not showing: what Limited by budget, Eligible (limited), Learning and Under review mean for a UK business, and when more budget is the wrong fix.",
"kicker": "Ads not showing",
"h1": "Google ads not showing: read the status column before you touch the budget",
"lead": "In most accounts I open, the ad is showing and the owner simply cannot see it, because searching for your own ad is not a reliable test. When ads genuinely are not running, the status column in Google Ads already names the reason: Limited by budget, Eligible (limited), Not eligible, Pending or Under review. Each of those has a different fix, and only one of them is more money.",
"body": """
<section><div class="wrap">
<h2>First, prove the ad is actually not showing</h2>
<p>An owner types their own service into Google on a Tuesday evening, sees a competitor and not themselves, and concludes the campaign is broken. It usually is not. Your ad may be outside its schedule, the daily budget may have been spent by lunchtime, Google may be rotating ads, or your own repeated searches without clicks may have taught the system that you are not a buyer. Google's <a href="https://support.google.com/google-ads/answer/148778?hl=en-GB" rel="noopener" target="_blank">Ad Preview and Diagnosis tool</a> exists for exactly this. It shows a preview of the results page for a search term, location and device, and Google says it "avoids accumulating ad impressions and impacting your performance statistics", which a manual search does not. It also warns that your ad may stop appearing in the preview once the campaign has reached its average daily budget, which is the most common honest answer to "why can't I see my ad at 6pm".</p>
<p>The tool sits under Tools and then Troubleshooting. If it says the ad is not showing and gives "Reason unknown", Google lists two common causes: the campaign is in a learning period after a bidding change, or the keyword has low search volume and will not trigger a preview. Before diagnosing anything else, the same page says to check the account itself, because ads do not serve while an account is in billing verification or temporarily suspended for security reasons.</p>
<p>So the order is: run the preview tool for your real location, read the status column, then decide. The rest of this guide is the status column.</p>
</div></section>

<section><div class="wrap">
<h2>The campaign statuses, in Google's words</h2>
<p>Google defines campaign statuses on its <a href="https://support.google.com/google-ads/answer/2549115?hl=en-GB" rel="noopener" target="_blank">campaign status</a> page and its <a href="https://support.google.com/google-ads/answer/1722131?hl=en-GB" rel="noopener" target="_blank">about campaign statuses</a> page. The ones that matter when nothing seems to be running are below, with what each means for the business rather than for the person operating the account.</p>
<table>
<tr><th>Status shown</th><th>Google's definition</th><th>What it means for you</th><th>Right fix</th></tr>
<tr><td>Eligible</td><td>"Your campaign is active and can show ads."</td><td>Nothing is wrong at campaign level. If you cannot see the ad, the problem is schedule, location, budget pacing or your test method.</td><td>Use Ad Preview and Diagnosis, not a Google search.</td></tr>
<tr><td>Eligible (limited)</td><td>"only showing ads occasionally due to budget constraints or a limited bid strategy."</td><td>Ads run, but Google is rationing them. Impressions arrive in bursts and then stop.</td><td>Read the bid strategy status before adding budget. Often the target is too tight, not the budget too small.</td></tr>
<tr><td>Limited by budget</td><td>"The campaign is active and can show ads, but not as often as it could due to budget constraints."</td><td>There is more demand than money. You are missing searches you could have won.</td><td>Decide whether those extra searches are worth having. More budget is only right if the existing clicks convert.</td></tr>
<tr><td>Not eligible</td><td>"there are no ad groups, all ad groups are paused or deleted" (or all ads or keywords are paused or deleted).</td><td>The campaign is a shell. Something inside it was paused or removed, often during a clean-up.</td><td>Open the campaign and look at ad groups, ads and keywords for the paused or removed items.</td></tr>
<tr><td>Pending</td><td>"scheduled to begin at a future date."</td><td>Someone set a start date. Nothing will run until it arrives.</td><td>Change the start date if that was a mistake.</td></tr>
<tr><td>Ended</td><td>"it's past its scheduled end date."</td><td>An end date from a previous promotion or a test is still on the campaign.</td><td>Remove or move the end date.</td></tr>
<tr><td>Paused</td><td>"Your campaign is inactive because you paused it."</td><td>Someone with access paused it. Check the change history to see who.</td><td>Resume it, and find out why it was paused first.</td></tr>
</table>
<p>Two more strings appear at ad level rather than campaign level and are covered by Google's <a href="https://support.google.com/google-ads/answer/1722120?hl=en-GB" rel="noopener" target="_blank">ad status page</a>. "Under review" means the ad is being checked against policy, and Google says most ads are reviewed within one working day, to check the status if it takes more than two full working days, and to contact support if it takes more than a week. "Disapproved" means the review found a policy violation and the ad cannot show anywhere. A disapproved ad will not run until it is fixed and reviewed again, and Google's <a href="https://support.google.com/google-ads/answer/1704381?hl=en-GB" rel="noopener" target="_blank">disapproved ad page</a> limits each ad to three appeals with at least 24 hours between appeals on the same ads.</p>
</div></section>

<section><div class="wrap">
<h2>Learning, Limited and Misconfigured: the bid strategy column</h2>
<p>People search for "learning limited" because they see two words in two columns at once: a campaign status of "Eligible (limited)" and a bid strategy status of "Learning". Google documents the bid strategy statuses on its <a href="https://support.google.com/google-ads/answer/6263057?hl=en-GB" rel="noopener" target="_blank">bid strategy statuses</a> page.</p>
<div class="cols">
<div class="card"><h3>Learning</h3><p>Google says there may be minor performance fluctuations as it optimises bids after a new strategy or after campaigns and keywords are added or removed. Its dedicated <a href="https://support.google.com/google-ads/answer/13020501?hl=en-GB" rel="noopener" target="_blank">Smart Bidding learning page</a> says the status "never lasts more than seven days", is triggered only by a new strategy, a composition change or a significant goal change, and is never triggered by budget, target, creative or targeting changes. Judge results over two conversion cycles or two weeks, whichever is longer.</p></div>
<div class="card"><h3>Limited</h3><p>Google lists four causes. Inventory, meaning available search volume. Bid limits that stop bids being fully optimised. Budget constrained, where many of the keywords are Limited by budget. And the bidding strategy itself, where a target CPA is too low or a target ROAS is too high for what the market will give.</p></div>
<div class="card"><h3>Misconfigured</h3><p>Conversion-based strategies do not have the right conversion actions set up, or a Maximise strategy is sharing a budget with a different strategy. Google's campaign statuses page adds a note that "Eligible (misconfigured)" usually means no biddable conversions were recorded in the last 28 days.</p></div>
</div>
<p>This matters for the owner because the fix for each is different and none of them is "spend more". A Learning status means wait and stop changing things. A Limited status caused by a bid limit or a tight target means loosen the target, not the wallet. A Misconfigured status means the tracking is broken, which is a <a href="/ppc-audit/">PPC audit</a> finding rather than a bidding problem, and raising budget on a campaign that cannot see its own conversions only buys more untracked clicks.</p>
</div></section>

<section><div class="wrap">
<h2>Why "Limited by budget" is a decision, not an error</h2>
<p>Google's <a href="https://support.google.com/google-ads/answer/2616012?hl=en-GB" rel="noopener" target="_blank">page on fixing Limited by budget</a> says the status appears when your average daily budget is lower than the recommended amount, and offers a budget simulator to show how much exposure a different budget might buy. It lists two responses: a higher budget to increase clicks, or lower bid adjustments to get more clicks within the same budget. Notice what it does not say. It does not say the campaign is broken. The campaign is working and the market has more searches than you chose to pay for.</p>
<p>Whether to buy them depends on one question: are the clicks you already buy turning into enquiries at a cost you would pay again? If the answer is yes, Limited by budget is the best status in the account because it tells you growth is available. If the answer is no, or you do not know because tracking is unreliable, more budget scales the waste. In audits for UK small businesses this is the single most common place money is lost. The campaign shows the red "Limited by budget" bubble, someone raises the budget, and the extra spend goes to the same broad match terms that were not converting at the lower budget either. The <a href="/google-ads-small-business/">Google Ads for small business</a> page explains how I size a budget from conversion data rather than from Google's recommendation.</p>
<p>There is a second reason to pause before paying. The same Google page says that from 17 August 2026 Google is updating how its bidding systems optimise budget-limited campaigns running Target CPA, Target ROAS, and Target CPC for Demand Gen, and that this may cause temporary performance and traffic fluctuations. A bid target adjustment tool became available on 6 July 2026, and Google says it will not change your budgets or targets for you. If a campaign that was fine in spring started behaving oddly in late summer, that change is a more likely cause than anything you did.</p>
<h3>How the daily budget really spends</h3>
<p>Owners also misread normal pacing as "not spending" or "overspending". Google's <a href="https://support.google.com/google-ads/answer/1704443?hl=en-GB" rel="noopener" target="_blank">overdelivery page</a> says that on a given day a campaign might spend up to twice your average daily budget, and that at the end of the month you will have spent no more than 30.4 times the average daily budget. A £50 daily budget can take £100 on a busy Monday and £15 on a quiet Sunday. If you check only on the quiet day, the ad looks absent. If you check only the busy day, you think you are being overcharged. Neither is true.</p>
</div></section>

<section><div class="wrap">
<h2>Location and schedule mistakes common in UK accounts</h2>
<p>When the status column says Eligible and the preview tool still shows nothing for you, the campaign settings are usually to blame. Three patterns repeat in UK accounts.</p>
<h3>The location setting reaches the wrong people, or excludes you</h3>
<p>Google's <a href="https://support.google.com/google-ads/answer/1722043?hl=en-GB" rel="noopener" target="_blank">location targeting page</a> describes two target options. "Presence or Interest" reaches people in your targeted locations and people who have shown interest in them, and Google recommends it as a best practice on Search. "Presence" reaches only people physically in the location. For a Manchester accountant, Presence or Interest means a person in Lisbon researching UK accountants can see and click the ad, while Presence means a Mancunian searching from a hotel in Lisbon cannot. Neither is wrong, but owners rarely know which one is set, and a sudden fall in impressions after an "optimisation" is often someone switching the setting. Radius targeting has a minimum of 1 km, so a tight radius around a shop in a dense town can be far smaller than the trade area it serves.</p>
<h3>The ad schedule runs on the account time zone, which may not be London</h3>
<p>Google's <a href="https://support.google.com/google-ads/answer/6372656?hl=en-GB" rel="noopener" target="_blank">ad schedule setup page</a> states that "Ad schedules are set based on your account's time zone", with a maximum of six ad schedules per day for each campaign, and a schedule that runs past midnight has to be split across two days. The account time zone is the trap. Google's <a href="https://support.google.com/google-ads/answer/17006726?hl=en-GB" rel="noopener" target="_blank">time zone setting page</a> says it is set when the account is created and that time zone changes are no longer supported in standard serving accounts. Accounts opened by a founder while living abroad, or set up by a supplier overseas, keep that time zone forever. A 9 to 5 schedule on an account that thinks it is in New York runs from 2pm to 10pm in the UK, and the owner who searches at 10am sees nothing.</p>
<h3>Spending limits that used to be campaign budgets</h3>
<p>Monthly spending limits set at account level, campaign end dates left over from a Christmas push, and ad groups paused during a seasonal clean-up all produce a campaign that looks live and serves nothing. The change history in Google Ads shows who did what and when, and I read it before I change anything.</p>
</div></section>

<section><div class="wrap">
<h2>What to do today, in order</h2>
<ol class="steps">
<li><div><strong>Check the account before the campaign.</strong> Billing verification, a payment that failed, or a security hold stops every ad. The Ad Preview page itself says to check account status first.</div></li>
<li><div><strong>Run Ad Preview and Diagnosis</strong> for your real keyword, your real town and mobile. Stop searching for yourself on Google.</div></li>
<li><div><strong>Read the campaign status and the bid strategy status together.</strong> Eligible plus Learning means wait. Eligible (limited) plus Limited means loosen targets or accept the limit. Not eligible means something inside was paused or removed.</div></li>
<li><div><strong>Open the ad statuses.</strong> Under review older than two working days gets a status check. Disapproved gets fixed and resubmitted, with at most three appeals per ad.</div></li>
<li><div><strong>Check location option, schedule and the account time zone</strong> before concluding that demand is missing.</div></li>
<li><div><strong>Only then look at budget</strong>, and only if the clicks you already buy are converting.</div></li>
</ol>
<p>What not to do: do not create a duplicate campaign to "restart" it, which resets learning and splits your data, and do not change the budget, the target and the keywords in the same afternoon, because you will never know which change worked. If several of these are true at once, the account has drifted and a structured review is cheaper than another month of guessing. That is what the <a href="/ppc-audit/">audit</a> is for, and the <a href="/google-ads-management/">Google Ads management</a> page describes how the weekly checks stop the drift coming back.</p>
</div></section>

<section><div class="wrap">
<h2>Keeping ads visible without babysitting them</h2>
<ul>
<li>Check the status column once a week, not the search results page. The preview tool is for spot checks.</li>
<li>Leave Smart Bidding alone while it shows Learning, which Google says never lasts more than seven days, and make one change at a time.</li>
<li>Write down the account time zone and the location option on the first page of your campaign notes so the next person does not guess.</li>
<li>Remove end dates and seasonal schedules when the season ends, not when you notice the silence.</li>
<li>Treat "Limited by budget" as a quarterly decision backed by cost per enquiry, not as an alert to act on the same day.</li>
</ul>
</div></section>
""",
"faq": [
("Why is my Google ad not showing when I search for it?", "Because a Google search is not a test. Your budget may have been spent for the day, the campaign may be outside its schedule, your location setting may not include where you are standing, or Google may simply not have entered that auction for you. Use the Ad Preview and Diagnosis tool inside Google Ads, which Google says avoids adding impressions and skewing your statistics."),
("What does Limited by budget mean in Google Ads?", "Google's definition is that the campaign is active and can show ads but not as often as it could because of budget constraints. There is more demand than you have chosen to pay for. It is a signal of available growth, not a fault, and whether to act on it depends on whether the clicks you already buy are converting at a price you would pay again."),
("How long does Learning last in Google Ads?", "Google's Smart Bidding learning page says the Learning status never lasts more than seven days and is triggered by a new strategy, a change to what is inside the strategy or a significant change to the conversion goals. Budget and target changes do not trigger it. Google then advises judging results over two conversion cycles or a two-week window, whichever is longer."),
("Why does my campaign say Eligible but get no impressions?", "Eligible only means nothing is blocking the campaign itself. Look at the ad statuses for Under review or Disapproved, the bid strategy status for Limited or Misconfigured, the location option, the ad schedule and the account time zone. In UK accounts the time zone and the location option explain most of these cases."),
("Should I raise my budget to get my ads showing?", "Only if the status is Limited by budget and the existing clicks convert at an acceptable cost. If the status is Learning, Not eligible, Pending, Under review or Disapproved, more money changes nothing. If the bid strategy is Limited by its targets, loosening the target is the fix, and if it is Misconfigured the problem is tracking rather than spend."),
],
"messages": [
"Eligible",
"Eligible (limited)",
"Limited by budget",
"Not eligible",
"Pending",
"Ended",
"Paused",
"Under review",
"Disapproved",
"Learning",
"Limited",
"Misconfigured",
"Eligible (misconfigured)",
"Reason unknown",
],
"sources": [
"https://support.google.com/google-ads/answer/148778?hl=en-GB",
"https://support.google.com/google-ads/answer/2549115?hl=en-GB",
"https://support.google.com/google-ads/answer/1722131?hl=en-GB",
"https://support.google.com/google-ads/answer/1722120?hl=en-GB",
"https://support.google.com/google-ads/answer/1704381?hl=en-GB",
"https://support.google.com/google-ads/answer/6263057?hl=en-GB",
"https://support.google.com/google-ads/answer/2616012?hl=en-GB",
"https://support.google.com/google-ads/answer/1704443?hl=en-GB",
"https://support.google.com/google-ads/answer/1722043?hl=en-GB",
"https://support.google.com/google-ads/answer/6372656?hl=en-GB",
"https://support.google.com/google-ads/answer/17006726?hl=en-GB",
"https://support.google.com/google-ads/answer/1722022?hl=en-GB",
"https://support.google.com/google-ads/answer/13020501?hl=en-GB",
"https://support.google.com/google-ads/answer/13459939?hl=en-GB",
],
"related": ["/ppc-audit/", "/google-ads-management/", "/google-ads-small-business/"],
}
