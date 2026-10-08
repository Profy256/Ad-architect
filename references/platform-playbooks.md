# Platform and surface playbooks

The right ad depends on WHERE the product lives, not only what it does. Identify every surface the product ships on (a product can be web + Android + iOS + email at once) and analyze each separately.

Policy statements marked **[verified Oct 2026]** were checked against official help pages during skill creation; everything else is a durable principle. Re-check live policy before committing (see `policy-and-trust.md`).

## Contents
1. Quick selector
2. Mobile web / responsive website
3. Desktop web
4. PWA
5. Native Android
6. Native iOS
7. Cross-platform apps (Flutter, React Native, Expo)
8. Desktop apps (Tauri, Electron)
9. Browser extensions
10. Email newsletters
11. Messaging surfaces (WhatsApp, Telegram, SMS, USSD)
12. Video / streaming / audio surfaces
13. Games
14. Developer tools, APIs, docs
15. Multi-surface rule

## 1. Quick selector

| Surface | Best-fit ad families | Biggest risk | Network route |
|---|---|---|---|
| Mobile web | Native in-content, sponsored listings, responsive display, sponsor cards | Layout shift, ad density, accidental taps, data cost | AdSense / Ad Manager / direct |
| Desktop web | Sidebar, in-content, native, companion, sponsorship | Sticky overload, slow pages | AdSense / Ad Manager / direct |
| PWA | Same as web, with install and offline in mind | Treated as web by networks; offline ad gaps | Web ad tags / direct |
| Android app | Native, rewarded, banner on non-core screens, capped interstitials | Store disruptive-ads rules, APK size, low-end devices | AdMob / mediation / direct |
| iOS app | Native, rewarded, capped interstitials | ATT and privacy labels, review rejection | AdMob / mediation / direct |
| Desktop app | Self-rendered sponsor cards, sponsored features | Third-party ad scripts hurt trust and performance | Direct / affiliate |
| Browser extension | Sponsor lines inside own UI only | Store policies on injected ads | Direct / affiliate |
| Email | Sponsored section, native text/image block | Spam complaints, deliverability | Direct / newsletter networks |
| Messaging (WhatsApp/SMS/USSD) | Opt-in promos only | Consent law, spam flags, number bans | Direct, consent-based |
| Video/audio | Sponsored cards, companion, pre/post-roll, host-read | Mid-roll abuse, unexpected sound | Ad server / direct |
| Games | Rewarded, level-break interstitials | Ads during play, child audiences | Mediation |
| Dev tools/docs | Single sponsor card, sponsored resources | Trust loss from banners | Dev-focused networks / direct |

## 2. Mobile web / responsive website
- Biggest levers: reserve slot sizes (layout shift), keep ad density modest, avoid sticky overload, lazy-load.
- The Coalition for Better Ads lists these mobile-web experiences as below the acceptability threshold: pop-ups, prestitials, ad density above 30%, flashing animation, autoplay video with sound, poststitials with countdown, full-screen scrollover ads, large sticky ads. **[verified Oct 2026 via multiple secondary sources; one source reports a 2026 revision adding more experiences, so confirm the current list at betterads.org]**
- Chrome and other browsers block pop-ups/pop-unders and may filter abusive experiences. Do not build on them.
- Thumb zone: anchored bottom banners fight with browser UI and in-page nav. Prefer in-content placement.
- Consent banner (where required) must not stack on top of ad overlays; sequence them.
- Data cost: skip autoplay video on slow or data-saver connections.

## 3. Desktop web
- Use gutters and sidebars; collapse them below a width breakpoint instead of shrinking ads.
- Sticky sidebar units should stop before the footer and never overlap content.
- Desktop standards flag: pop-ups, autoplay with sound, prestitials with countdown, large sticky ads. **[verified Oct 2026, same caveat]**
- Ad-blocker usage is higher on desktop: sponsorships and first-party sponsor cards (served from your own domain, static, labeled) survive blockers better and are lighter.

## 4. PWA
- Ad networks see a PWA as a website. Use web ad tags and web policies.
- Offline mode: show nothing or a cached first-party sponsor line; never an empty bordered box.
- Installed PWAs feel like apps; users expect app-level polish, so keep ads off launch and navigation.
- Service-worker caching must not cache personalized ad responses or break consent state.

## 5. Native Android
Google Play's Disruptive Ads policy **[verified Oct 2026 via Play Console Help]**:
- Full-screen interstitials in any format that appear unexpectedly, typically when the user chose to do something else, are not allowed.
- Interstitials shown at the start of a level or at the start of a content segment are not allowed; interstitials that do not interrupt user actions (for example after a score screen) are allowed, as are opt-in ones.
- Full-screen video interstitials that appear before an app's loading screen (splash) are not allowed.
- Full-screen interstitials that cannot be closed after 15 seconds are not allowed (opt-in/rewarded excepted).
- Ads must be easy to dismiss without penalty, must not force clicks to proceed, and interstitials may only display inside the app serving them (not as out-of-app ads on the home screen or other apps).
Design consequences: no app-open interstitial that blocks first content unless it follows the policy and network rules; interstitials only at completion points; rewarded must be opt-in.
- Low-end devices dominate many markets: test memory, startup and ANR with the ad SDK on and off. Prefer lighter formats; consider mediation only if fill needs it, because each added SDK costs size and startup.
- Family/children apps (and apps for everyone that include children) must serve ads through a Google Play Families self-certified ads SDK or mediation configured to Families-certified sources, plus child-directed or age-treatment settings (see `vertical-playbooks.md` section 9). **[verified Oct 2026]**
- Back button: never intercept to show an ad.
- Gambling apps: Play allows real-money gambling apps and related ads only where requirements are met, including a valid licence for each distribution country, age gating, geo-blocking and visible responsible-gambling info. **[verified Oct 2026]** See `vertical-playbooks.md`.

## 6. Native iOS
- App Tracking Transparency: showing the ATT prompt is required before tracking across other companies' apps/sites; without consent, serve contextual or non-personalized ads. Do not nag users to change their choice. Check current Apple guidance.
- Privacy "nutrition labels" must declare ad SDK data collection accurately.
- App Review rejects misleading, hidden-close or forced-click ads, and apps whose main purpose is ads. Keep ads secondary to content.
- Safe areas and Dynamic Island/home indicator: do not anchor ads where they collide; keep close buttons clear of system gestures.

## 7. Cross-platform (Flutter, React Native, Expo)
- Both stores' rules apply to one codebase; build one slot abstraction that reads per-platform config.
- Official wrappers (for example Google Mobile Ads packages) lag native SDK features; verify native ad support and consent flows.
- List virtualization: key ad slots stably so they do not reload during scroll; preload one item ahead.
- Test on a low-end Android device and an older iPhone.

## 8. Desktop apps (Tauri, Electron)
- Avoid embedding third-party ad scripts in the main webview: they hurt performance, security (script injection) and trust.
- Prefer first-party sponsor cards fetched from your own endpoint, cached, labeled, and rendered natively.
- Best spots: dashboard/home, empty states, loading and completion screens, "recommended tools" panel. Never inside editors, file operations, settings, license/update dialogs.
- Auto-update and license flows are protected screens.
- Offline-first: ads must degrade to nothing.
- Telemetry for sponsor impressions needs a privacy disclosure and opt-out where required.

## 9. Browser extensions
- Ads that inject into pages the user visits are widely restricted by extension stores and are deceptive; do not design them. Verify the current store policy.
- Allowed approach: a clearly labeled sponsor line or featured offer inside the extension's own popup/options UI, with disclosure of any data use.
- Affiliate link rewriting must be disclosed and follow the store's affiliate rules.

## 10. Email newsletters
- Ad block types: a sponsored section, a native text-plus-image unit, a sponsor line in the header or footer. One to two units per issue.
- Label as "Sponsored" or "Partner"; keep editorial separate.
- Honor unsubscribe; complaint rate and deliverability are your constraint. Separate transactional mail (no ads, or only unobtrusive notices where allowed) from promotional mail.
- Measure with unique clicks or tracked links; apply privacy rules to tracking pixels.

## 11. Messaging surfaces (WhatsApp, Telegram, SMS, USSD)
- Opt-in only, with clear identity and easy opt-out. Business messaging platforms enforce template and consent rules and can ban numbers for spam.
- Keep promotions separate from transactional/security messages. Never use OTP or payment confirmation messages to carry ads.
- USSD and SMS are low-bandwidth: a single sponsor line in a menu footer is the most you should add; never interrupt a payment sequence.
- Frequency: very low. A burst of promos is the fastest route to uninstalls, blocks and complaints.

## 12. Video, streaming and audio surfaces
- Distinguish in-stream (pre/mid/post-roll, overlays) from out-stream (in-feed, in-article, floating).
- Declare video placement type and audibility accurately to the ad server; accurate signals are a network requirement for video inventory. **[verified Oct 2026 via Google Publisher Restrictions page: audibility and in-stream versus accompanying-content placement must be declared accurately]**
- Muted autoplay only; never start sound. Mid-roll only at breaks.
- Connected TV: remote-control navigation means every ad needs a focusable skip/close and must not trap focus.
- Audio: host-read sponsorship beats inserted commercials; do not interrupt mid-sentence.

## 13. Games
- Rewarded and level-break formats only; nothing during active play; first-session grace period.
- Keep ads away from gameplay controls. Test for accidental taps with the control layout.
- If minors may play, treat as a child audience for formats, data and ad categories.

## 14. Developer tools, APIs, documentation
- Developers punish banner clutter. One tasteful sponsor card, sponsored resources or tools, sponsored challenges and newsletter slots work; interstitials and autoplay do not.
- Never put ads inside code blocks, API reference tables, error messages or CLI output.
- Prefer sponsorship, affiliate and paid tiers over programmatic ads.

## 15. Multi-surface rule
When a product spans surfaces, set one global ad policy (protected screens, labeling, frequency philosophy, advertiser rules) and a per-surface implementation. Do not copy web banners into the app or app interstitials into the website. Deduplicate frequency across surfaces where a single user identity exists, so a person who sees five sponsor cards on web is not served five more in the app in the same hour.
