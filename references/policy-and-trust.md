# Policy, trust and transparency

Policies change. Treat everything below as principles and common patterns, and tell the user to confirm against the **current** policy of their ad network, app store and local law before shipping. If web search is available, check the live policy pages for the network in question.

## Contents
0. Verified policy snapshot
1. Labeling and disclosure
2. Deceptive and dark patterns (never)
3. Common network and store policy themes
4. Children and sensitive audiences
5. Consent, privacy and targeting
6. Advertiser and creative quality
7. Sponsored content and affiliate disclosure
8. If the owner insists on a risky placement

## 0. Verified policy snapshot (checked October 2026)

Checked during skill creation against official Google help pages unless noted. Re-check before shipping; wording and numbers change.

- **Google publisher content rules:** Publisher Policies list content that cannot be monetized (illegal content, sexually explicit content, dangerous or derogatory content, misrepresentative content, intellectual-property abuse, malware or unwanted software, enabling dishonest behavior, and others). Publisher Restrictions list content that may be monetized but will receive reduced or no Google Ads demand: sexual content, shocking content, guns and gun parts, explosives, other weapons, tobacco, recreational drugs, alcohol sales and misuse, online gambling, prescription drugs, unapproved pharmaceuticals and supplements.
- **Google video inventory:** publishers must declare video placements accurately, including audibility (audible by default or muted) and placement type (in-stream versus accompanying content).
- **Teen protections:** Google limits categories such as adult content, gambling and casino, complex speculative financial products and dangerous products from serving to teens.
- **Google Play Disruptive Ads policy:** unexpected full-screen interstitials are not allowed; interstitials at the start of gameplay levels or content segments are not allowed; full-screen video interstitials before the app's loading screen are not allowed; full-screen interstitials must be closeable after 15 seconds (opt-in formats excepted); ads must be easy to dismiss and must not force clicks; interstitials may display only inside the app serving them. Opt-in and non-interrupting placements (for example after a score screen) are allowed.
- **Google Play gambling:** real-money gambling apps and related ads are allowed only in eligible countries and only with a valid licence for each country, under-age prevention, geo-restriction to licensed regions and visible responsible-gambling information; an app first published under a lower age rating cannot be repurposed into a real-money gambling app.
- **Better Ads Standards (Coalition for Better Ads):** mobile web experiences beneath the standard include pop-ups, prestitials, ad density above 30%, flashing animation, autoplay video with sound, poststitials with countdown, full-screen scrollover ads and large sticky ads; desktop includes pop-ups, autoplay with sound, prestitials with countdown and large sticky ads. One secondary source reports a January 2026 revision adding more experiences and app interstitial variants; confirm the current text at betterads.org.
- **Uganda gaming regulation:** the National Lotteries and Gaming Regulatory Board licenses and supervises betting and lotteries under the Lotteries and Gaming Act; Responsible Gaming Directives, 2025 were issued, reportedly requiring responsible-gaming messages, a self-exclusion register, stronger age verification and restrictions on credit and inducements; gaming advertising is regulated under Gaming (Advertisement) Directives and the board has removed non-compliant billboards. Based on news and industry reporting; obtain the primary texts before advising a licensed operator.
- **Not verified here:** Apple App Store and ATT current wording, AdSense native/in-feed asset rules, extension store ad-injection rules, other countries' gambling advertising law. Treat statements about them as principles and verify.

## 1. Labeling and disclosure

- Every ad, sponsored listing, sponsored recommendation or affiliate item is labeled clearly: "Ad", "Advertisement", "Sponsored", "Promoted", or "Partner", chosen to fit the context.
- The label is visible without interaction, legible (contrast and size), consistently positioned, and not removable by the advertiser or by styling.
- Sponsored items in sorted/ranked lists are visibly distinct from organic ones even when they share a card layout.
- Disclose affiliate relationships near the recommendation, not only in a footer.

## 2. Deceptive and dark patterns (never design or implement)

- Ads that look like system notifications, platform controls, error messages, login prompts, or download/play/close buttons.
- Fake close buttons, hidden or tiny close targets, close buttons that open the ad, moving close targets.
- Layouts that invite accidental clicks (ad directly beside a primary control; ad shifting under the finger at load).
- Ads presented as user content or independent reviews without disclosure.
- Forced-dwell countdown walls over core content; ad loops that never let the user proceed.
- Back-button/exit hijacking; ads that reopen after being dismissed.
- Unexpected audio; ads that start sound automatically.
- Rewarding or pressuring clicks on ads ("tap the ad to continue", incentivized clicks).
- Hiding the fact that something is an ad.
- Notifications or SMS promos disguised as transactional messages.

If asked for any of these, decline that part, explain why it harms users and often violates network policy, and propose a compliant alternative that serves the same business goal (e.g. rewarded opt-in instead of forced gate; labeled native card instead of disguised content).

## 3. Common network and store policy themes (verify current text)

- **Non-content screens:** ad networks commonly prohibit ads on screens with no publisher content (login, error, navigation, thank-you, loading-only or alert screens). This supports keeping protected screens ad-free.
- **Placement integrity:** ads must not be placed so they are mistaken for content or navigation, or placed to cause accidental clicks; limits on ad density and on ads crowding above-the-fold content.
- **Pop-ups/pop-unders and app-launch/exit tricks:** commonly disallowed or restricted; many browsers block pop-unders. Unexpected full-screen ads triggered by ordinary taps or by leaving the app are commonly disallowed on mobile stores.
- **Native ads:** must keep required attribution and supplied assets; no obscuring or modifying them; ads must be distinguishable.
- **Rewarded ads:** must be opt-in with the reward described; no rewarding clicks.
- **Invalid activity:** never click your own ads, ask others to, or incentivize clicks; test with the network's test ad units during development.
- **Interstitials:** must appear at natural transition points, not on top of the user's current task; avoid frequent or stacked interstitials.
- **Better Ads–type standards:** experiences widely flagged on mobile include pop-ups, prestitials, ad density above roughly 30% of the viewport, flashing animations, autoplay video with sound, full-screen scroll-over ads, and large sticky ads. Confirm the current list.
- **Prohibited categories and restricted content:** adult, gambling, alcohol, financial services, health claims and others carry network and local-law restrictions that vary by country.

## 4. Children and sensitive audiences

- If the product may be used by children (apps for students, games, family content), apply child-directed rules **before** choosing formats: restricted ad formats and networks, no behavioral/personalized advertising, strict content filtering, and legal requirements such as COPPA (US) and equivalents elsewhere. When age is uncertain, treat the audience conservatively and say so.
- Avoid ads that exploit age, vulnerability, grief, illness, financial stress, or emergencies.
- Do not target or personalize using sensitive attributes (health, religion, ethnicity, sexuality, political belief, financial distress). Prefer contextual targeting.
- Emergency/safety screens and health-critical flows stay ad-free.

## 5. Consent, privacy and targeting

- Prefer contextual placement (based on the content or query) over personal profiling; it is more relevant to the moment, lighter on data and easier to defend.
- Where personal data, device identifiers or cross-app tracking are used, obtain required consent (GDPR/ePrivacy-style consent, platform prompts such as App Tracking Transparency on iOS, local laws) and respect opt-outs. Provide a privacy explanation reachable from the ad ("Why this ad").
- Email, SMS and push promotion require opt-in, an easy unsubscribe and honest sender identity; keep transactional and promotional messages separate.
- Minimize data sent to ad partners; document what each SDK collects, and make sure the privacy policy matches.
- Confirm country-specific requirements (for example Uganda's Data Protection and Privacy Act 2019, Kenya's Data Protection Act 2019, GDPR) with a qualified advisor. This skill gives product guidance, not legal advice.

## 6. Advertiser and creative quality

Bad creatives destroy trust in the host platform, even when the platform did not make them.

- Set advertiser approval rules for direct deals; require a real business identity.
- Block or tightly vet: scams, get-rich-quick, predatory loans, fake products/jobs/listings, misleading health claims, adult content, aggressive betting, malware/"your device is infected" creatives, and competitors that harm the user's goal.
- For network ads, use category and advertiser blocklists, enable creative review where offered, and give users a "report this ad" path.
- Review the ads actually served on key screens periodically.

## 7. Sponsored content and affiliate disclosure

- Sponsored articles, reviews, tutorials and comparisons must be labeled and keep editorial integrity: sponsorship buys visibility, not a rewritten conclusion.
- Comparison tables with sponsored rows mark the sponsored row clearly and keep sort criteria honest.
- Sponsored comments/answers in communities: avoid unless there is strong labeling and moderation.
- Follow local advertising-disclosure rules and any platform requirements for sponsored content.

## 8. If the owner insists on a risky placement

1. State plainly what harm is likely and to whom, in a sentence or two.
2. Offer the best alternative that serves the same goal.
3. If they still want it and it is not deceptive or a policy violation, label it 🟠 HIGH RISK, specify mitigations (cap, delay, dismissibility, size, suppression for new users) and a rollback metric, and propose a staged test.
4. If it is deceptive or likely to violate policy, do not implement it.
