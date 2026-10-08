# Market context and monetization readiness

Use this when traffic is small, the product is early, users are data-sensitive or on low-end devices, or ad fill/CPM is low. It matters most for products serving emerging markets (e.g. East Africa), but the readiness check applies to any early-stage product.

## Contents
1. Monetization readiness check
2. Low-traffic reality
3. Emerging-market constraints
4. Revenue models ranked by fit
5. Advertiser side (who pays and how)

## 1. Monetization readiness check

Run before recommending any programmatic ad:

| Question | If the answer is "no/unknown" |
|---|---|
| Is there evidence users return (retention) without ads? | Keep ads minimal or zero; early retention is more valuable than early ad revenue |
| Is there enough traffic for ad revenue to matter? | Estimate: monthly ad-eligible sessions × pages/units per session × realistic RPM ÷ 1000. If the result is trivial, programmatic ads cost more UX than they earn |
| Is there supply and demand density (for marketplaces)? | Sponsored listings need enough listings and searches to be valuable and trustworthy |
| Are there direct advertisers or sellers who would pay now? | Sell sponsorships/featured listings directly before integrating a network |
| Can the product absorb the performance cost (data, CPU, load) of ad SDKs? | Favor lightweight self-rendered sponsor cards |

Use `scripts/revenue_estimator.py` for the range (it requires your own eCPM, fill and price assumptions, so nothing is invented). State the answers, or say they are unknown, in the Product Understanding section. Do not fabricate revenue figures. If you estimate, show the formula and mark inputs as assumptions.

## 2. Low-traffic reality

- With small audiences, a banner's earnings can be negligible while its UX cost (layout shift, load time, accidental taps) is immediate. Prefer fewer, higher-value placements.
- A handful of direct partners paying for a sponsored section, featured listings or a sponsored tool often beats network banners per user.
- Statistical A/B tests may not reach significance; use staged rollouts, qualitative feedback, and direct comparison of retention before/after.
- Do not let monetization work delay the work that creates the audience.

## 3. Emerging-market constraints (verify for the actual user base)

- **Data cost and connectivity:** many users pay per megabyte, on unstable networks. Video ads, heavy rich media and multiple ad SDK calls can cost users real money and drain trust. Prefer image/text native units, lazy loading, compressed assets, and respect data-saver settings. Auto-playing video ads are the most expensive in data terms.
- **Device range:** low-RAM Android devices are common. Ad SDKs add memory, CPU, battery and app size. Measure startup time and memory with ads on and off on a low-end device.
- **Typical economics:** programmatic CPMs in many emerging markets are usually much lower than in North America or Western Europe, and fill can be inconsistent. Rely on direct deals, local sponsors and listing/featured-placement revenue where possible. Check current network rates rather than assuming.
- **Local relevance:** local-language and locally relevant offers (telecom bundles, mobile-money promotions, education, housing, jobs, agriculture, local retail) tend to feel useful; irrelevant global ads feel like noise.
- **Channels:** SMS, WhatsApp and mobile-money notifications are heavily used. They are also easy to over-use and are covered by consent and data-protection rules; treat them as opt-in, low-frequency channels.
- **Payments for advertisers:** card-based self-serve ad purchase excludes many local advertisers. Mobile-money payment, invoicing, or manual onboarding often unlocks local demand. Keep the buying flow simple and the pricing transparent (e.g. a flat weekly price for a featured slot).
- **Trust and fraud:** scam, predatory-loan, betting and fake-listing ads are common risks. Vet advertisers and block sensitive categories.
- **Data protection:** several countries have data-protection laws (for example Uganda's Data Protection and Privacy Act 2019, Kenya's Data Protection Act 2019, and GDPR for EU users). Prefer contextual targeting, minimize personal data, obtain consent where required, and confirm current legal requirements with a qualified advisor.

## 4. Revenue models ranked by fit for early or emerging-market products (typical, not universal)

1. Featured/promoted listings (marketplaces, jobs, services)
2. Direct sponsorships (sections, features, tools, challenges, events, newsletters)
3. Affiliate and referral (education, finance products with vetting, software, telecom)
4. Native sponsored cards sold directly
5. Rewarded ads where the product has a natural reward economy
6. Network native/in-feed units
7. Network banners
8. Interruptive formats (only at natural breaks, with caps)

This is a heuristic order. Reorder it when the product's own data says otherwise.

## 5. Advertiser side

- Who pays: local businesses, sellers/agents/employers on the platform, education providers, telecom and financial brands, event organizers.
- What they buy: visibility to a defined audience at a decision moment (a person searching for exactly their product).
- What they need: simple packages, clear metrics (impressions, clicks, contacts), proof of audience, labels that make the sponsorship credible.
- Report honestly. Overselling reach damages the advertiser relationship and the platform's credibility.
