# Vertical (industry) playbooks and ad-eligibility gate

The product's industry changes what ads are ALLOWED, what is SAFE and what is PROFITABLE. Run the eligibility gate in section 1 before choosing any format. A betting site, a kids' learning app and a property marketplace need different answers even with the same screens.

Facts marked **[verified Oct 2026]** were checked against official help pages or regulator-related reporting at skill creation; re-check live sources before committing. Law and policy vary by country: this is product guidance, not legal advice.

## Contents
1. Eligibility gate (do this first)
2. Betting, gambling and casino
3. Adult content
4. Crypto, trading, forex
5. Lending, loans, fintech, mobile money
6. Health, pharma, supplements, mental health
7. Alcohol, tobacco, vaping, recreational drugs
8. Weapons, shocking, dangerous content
9. Children, teens, students
10. News, politics, elections
11. Dating
12. Real estate, jobs, classifieds
13. E-commerce and deals
14. File-sharing, downloads, streaming of unlicensed media
15. VPN, utilities, cleaners, "boosters"
16. Religion, community, NGOs
17. Travel, food, local services, telecom
18. AI tools and assistants

## 1. Eligibility gate

Answer in order and put the result in the report (section A):

1. **Can the product show ads from the intended network at all?** Google splits content into Publisher Policies (violating content cannot be monetized: for example illegal content, sexually explicit content, dangerous or derogatory content, misrepresentative content, malware, enabling dishonest behavior) and Publisher Restrictions (allowed, but Google Ads does not serve, so demand is low or absent: sexual content, shocking content, guns and gun parts, explosives, other weapons, tobacco, recreational drugs, alcohol sales and misuse, online gambling, prescription drugs, unapproved pharmaceuticals and supplements). **[verified Oct 2026]** Consequence: restricted verticals cannot rely on Google display revenue; plan direct sponsorship, affiliate and in-house promotion instead.
2. **Which ads may the product show for this vertical?** Many categories are restricted or banned for certain audiences, countries and surfaces (see sections below).
3. **Is the audience protected?** Minors, vulnerable users, self-excluded or at-risk users change the answer. Google restricts certain categories (including gambling and casino ads, complex speculative financial products) from serving to teens. **[verified Oct 2026]**
4. **Which regulator and laws apply** in each country served (gambling, financial services, health, alcohol, data protection, consumer protection, election rules)?
5. **What do users of THIS vertical consider acceptable?** In high-trust verticals (finance, health, education, marketplaces with safety stakes) a single bad ad can destroy the brand.
6. **Is the main revenue really ads?** In many verticals the product earns from its core transaction (bets, listings, subscriptions, commissions), and "ads" are mostly first-party promotions, sponsorships or affiliate placements.

If any answer is "no/unknown" for a regulated vertical, say so, give the safe default, and ask the owner for the licence/regulatory details before recommending anything beyond it. If web search is available, check the current policy and regulator rules before finalizing.

## 2. Betting, gambling and casino

Two different situations. Identify which one applies:

### 2A. The product IS a licensed betting/casino operator (sportsbook, casino, lottery, betting app)
Its "advertising" is mostly **first-party promotion** (bonuses, odds boosts, free bets, jackpot banners, cross-sell between sportsbook and casino) plus partner/affiliate marketing. Third-party programmatic ads are usually neither lucrative nor appropriate.
- **Protected, no promotions:** age verification and registration/KYC; deposit, withdrawal and payment confirmation screens; bet slip confirmation; limit-setting, self-exclusion and cool-off screens; responsible-gambling pages; account-closure; support and complaints; error recovery.
- **Allowed with care:** promotion cards on the home/lobby, event pages (an odds boost for the match the user is viewing), a "promotions" tab, post-settlement screens (not right after a loss, see below), personalized offers only within consent and responsible-gambling rules.
- **Responsible-gambling design rules (treat as ad design constraints):**
  - Show required responsible-gambling messages and warnings with any promotion; regulators in markets like Uganda require responsible gaming messages in gaming advertisements. **[verified Oct 2026 via regulator reporting]**
  - Do not use promotions that pressure loss-chasing: no "bet again" or "double up" prompts right after a loss, no countdown-urgency pop-ups on the bet slip, no promo that interrupts withdrawal.
  - Exclude self-excluded, cooling-off and flagged at-risk users from all promotion, including push, SMS and email. Respect registries of self-excluded players where the regulator operates one.
  - No credit, loans or inducements that encourage unsafe wagering; Uganda's 2025 directives are reported to prohibit credit and inducements and to introduce a self-exclusion register, stricter age verification and responsible advertising rules. **[verified via secondary reporting; get the directive text]**
  - Age: no promotion to under-18 or under the local legal age; no use of youth-appealing creative, athletes or influencers in ways the regulator prohibits.
  - Frequency: lower caps than ordinary apps; cap bonus pushes per week; quiet hours (no late-night pushes); easy opt-out of marketing separate from account notices.
  - Bonus terms must be accessible and honest: wagering requirements and expiry visible near the offer, not buried.
- **Channel rules:** push/SMS/email promotions are the highest-risk channel for this vertical; consent and responsible-gambling controls apply.
- **Regulation checkpoints (verify per country):** gaming licence for each country served; advertising directives; geo-blocking where unlicensed; payment-provider rules; app-store rules. Google Play allows real-money gambling apps and gambling ads only in eligible countries with a valid licence per country, under-age prevention, geo-restriction and visible responsible-gambling information; apps once published under a lower age rating cannot be repurposed for real-money gambling. **[verified Oct 2026]** In Uganda the National Lotteries and Gaming Regulatory Board licenses operators and regulates gaming advertising, and has removed non-compliant gaming billboards. **[verified Oct 2026]** Confirm Uganda's Gaming (Advertisement) Directives text and equivalents elsewhere.
- **Revenue note:** for operators, the best "ad" is a relevant, compliant promotion at a natural moment (pre-match), not an interruption.

### 2B. The product is a tipster, odds-comparison, sports-stats or affiliate site (does not take bets itself)
- Revenue: affiliate/CPA/revenue share with **licensed operators only**, sponsorships, premium subscriptions. AdSense/AdMob demand is limited because online gambling is a Google publisher restriction; do not plan on Google display as the main revenue. **[verified Oct 2026]**
- Show operators relevant to the visitor's country only; hide or replace offers for unlicensed jurisdictions.
- Every operator placement carries a visible "Ad"/"Sponsored" label, 18+ (or local age) notice, responsible-gambling message and a link to help resources.
- Comparison tables: mark sponsored rows, keep ranking criteria honest, disclose affiliate relationships near the link.
- Never promise guaranteed wins or profit; do not design "sure tip" claims as ads.
- Do not run interstitials or popups with bonuses over content; keep to in-content cards and comparison blocks.

### 2C. A non-gambling product being asked to show betting ads (for example a sports news app, a student app)
- Treat betting ads as a high-risk category: platform and regulator restrictions apply, minors may be present, and trust cost can be high.
- Prefer excluding the category (use the network's category blocking) unless the audience is verified adult and the advertiser is licensed in that country.
- Never show to students or mixed-age audiences without age signals.

## 3. Adult content
- Google Publisher Policies prohibit monetizing sexually explicit content with its products. **[verified Oct 2026]** Use adult-specialist networks or direct deals, with strict age verification.
- Ad controls: ads must not appear to or target minors; no deceptive "close" or fake-download buttons (a notorious pattern in this vertical); no auto-playing audio; no ads posing as system messages.
- Many ad creatives in this space are malicious or deceptive; apply strict creative review and category blocks.
- Payment and app-store rules are stricter than for most verticals.

## 4. Crypto, trading, forex
- High-fraud category. Many networks require advertiser certification and limit formats or countries; "complex speculative financial products" are restricted from serving to teens. **[verified Oct 2026]**
- For a product in this vertical: no ads in trade, deposit, withdrawal, key-management or wallet-connect screens; no ads that look like wallet prompts or security warnings (a major phishing pattern); strong labeling; no guaranteed-return claims.
- Prefer partner placements from vetted exchanges/tools, educational sponsorships, and affiliate with disclosure. Risk warnings should accompany promotions where regulation requires.

## 5. Lending, loans, fintech, mobile money
- Highest trust stakes. Predatory-loan and scam ads cause real harm and brand damage.
- Protected: KYC, transfers, payments, PIN/OTP, balance, statements, dispute flows.
- Safe pattern: vetted partner offers shown after a user opts into "offers", clearly labeled, with transparent rates and terms; no deceptive "pre-approved" claims; no urgency pressure.
- Regulator and consumer-protection rules often require disclosure of cost and licensing; verify per country.
- Never place ads next to money-moving buttons or payment confirmation.

## 6. Health, pharma, supplements, mental health
- Prescription drugs and unapproved pharmaceuticals/supplements are Google publisher restrictions; many networks bar or limit health ads. **[verified Oct 2026]**
- Never target on health conditions or sensitive inferences. Contextual only, and keep sensitive or crisis contexts (mental health, abuse, emergencies, symptoms checkers) ad-free.
- No ads that exploit fear, miracle claims or body-shaming. Disclose sponsorship on health content; keep editorial independence.
- Telehealth and pharmacy promotions require regulatory checks.

## 7. Alcohol, tobacco, vaping, recreational drugs
- Google restricts publisher content that promotes tobacco sales or recreational drugs and alcohol sales/misuse; these categories have heavy country-specific and age-based limits. **[verified Oct 2026]**
- Needs age gating, local-law checks and exclusion from youth/mixed audiences. Default: block the category unless the audience is verified adult and legal in-country.

## 8. Weapons, shocking, dangerous content
- Guns, gun parts, explosives, other weapons and shocking content are Google publisher restrictions; dangerous or derogatory content cannot be monetized. **[verified Oct 2026]**
- Default: no programmatic ads; consider direct, lawful sponsorships with strict review, or no ads.

## 9. Children, teens, students
- If minors may use the product, decide the audience classification first; it overrides format choices.
- Children's products: use only certified/child-safe ad networks and child-directed settings, no personalized ads, no behavioral tracking, no gambling/adult/dating/finance categories, no deceptive or incentivized-click mechanics, no interstitials that trap input, and no ad that looks like game content. Check laws (for example COPPA in the US, GDPR child rules in the EU, and local equivalents) and store family policies.
- Teen audiences: platforms restrict categories (adult content, gambling and casino, speculative finance, dangerous content) from serving to teens. **[verified Oct 2026]**
- Education platforms: ads never during lessons, quizzes or exams; prefer sponsored learning resources, scholarships, clearly educational partners.
- When age is unknown, assume a mixed audience and exclude sensitive categories.
- **Age-split rule:** if the audience spans children and teens (for example 10 to 17), treat the under-13 segment as child-directed. Unless the product reliably age-gates and routes under-13 users to a different, ad-free or child-directed configuration, apply the strictest rules to the whole app. **[verified Oct 2026: COPPA covers services directed to under-13s and general-audience services with users known to be under 13; Google's child-directed tagging disables interest-based and remarketing ads for tagged requests]**
- **Google tooling:** AdMob offers child-directed treatment and an under-age-of-consent tag for EEA users (now being folded into an "age treatment" setting with child, teen and unspecified values); child-directed takes precedence if both are set. On Google Play, apps for children and apps for everyone including children must use a Google Play Families self-certified ads SDK or mediation set to Families-certified sources when serving ads to children or users of unknown age. **[verified Oct 2026 via AdMob help]**
- **Money without risky ads:** for minors, revenue usually comes from parent- or school-paid models: subscriptions bought by parents, school/institution licensing, scholarships and sponsored programs from vetted education partners (sponsorship of a feature, not behavioral ads), and in-app purchases with parental controls. Present these first; if ads remain, they are Tier-1 style sponsored learning resources outside lessons, via certified sources.

## 10. News, politics, elections
- Political and issue ads carry disclosure rules (who paid) and election-period regulation in many countries; some networks require advertiser verification.
- Keep clear separation between editorial and ads; "sponsored content" labeled; no ads mimicking news headlines (clickbait recommendation widgets erode credibility).
- Avoid placing ads next to breaking tragedies or sensitive coverage (brand safety and user trust).
- Do not microtarget political ads with sensitive data.

## 11. Dating
- Trust and safety dominate: scams, catfishing and adult ads are common. Strict advertiser vetting; no ads inside conversations; no ads disguised as profiles (a classic deception).
- Some networks restrict dating ads by country. Sensitive-attribute targeting is prohibited in many jurisdictions.
- Premium subscription is usually the main monetization; ads, if any, are light and outside chat and profile-viewing.

## 12. Real estate, jobs, classifieds
- Best vertical for intent-matched ads: featured/promoted listings, sponsored agents/employers, sponsored map pins.
- Guard against fake listings and scam jobs; verify sponsors; label every paid placement; keep paid ranking from hiding better organic matches.
- Fair-housing/discrimination rules and employment-advertising rules restrict targeting in some countries; target by content/location, not protected characteristics.
- Protected: contact forms, applications, deposit/booking payment, document upload, identity verification.

## 13. E-commerce and deals
- Sponsored products in search and category pages, deal and coupon cards, affiliate, post-purchase recommendations.
- Keep sponsored items relevant and labeled; protect cart, checkout and payment.
- Beware "fake discount" or fake scarcity creatives; they damage trust and may violate consumer law.

## 14. File-sharing, downloads, streaming of unlicensed media
- High-risk: copyright-infringement content is a Google publisher policy violation (intellectual property abuse) and cannot be monetized with Google. Download-gate sites attract malicious ads and deceptive fake download buttons. Recommend moving to licensed or user-generated original content before any serious monetization; otherwise expect account bans and security incidents.
- For legitimate file-hosting: no fake download buttons, clear distinction between ad and download control, sandboxed ad iframes, strict malware scanning of creatives.

## 15. VPN, utilities, cleaners, "boosters"
- Frequent scare-ware ad abuse ("your phone is infected"). Block these creative categories.
- Utility apps tolerate fewer ads: users want one task done. Rewarded unlock and a single native card, not interstitial-heavy flows.
- Privacy-sensitive audiences (VPN) object to tracking; prefer contextual sponsorship.

## 16. Religion, community, NGOs
- Highly trusting audience; ads should be restrained and respectful. Avoid ads that conflict with community values (alcohol, gambling, adult) by category blocking.
- Prefer community sponsors, donor/partner recognition and local business sponsorship.
- Sponsored content in a faith or charity context must be clearly separate from devotional or appeal content.

## 17. Travel, food, local services, telecom
- Strong contextual fit: sponsored hotels, restaurants, bundles, airtime and data offers (in telecom markets), event tickets.
- Local relevance beats global programmatic. Mobile-money and telecom partners can be strong direct sponsors.
- Keep booking and payment steps clean.

## 18. AI tools and assistants
- Ads must never alter or appear inside the answer; sponsored suggestions are visually separate and labeled; no ads in sensitive conversations (health, legal, finance distress, mental health).
- Disclose when a recommendation is sponsored. Any perceived steering of answers by advertisers destroys trust.
- Prefer sponsorships of the product surface (sidebar, empty states, templates) and subscriptions.
