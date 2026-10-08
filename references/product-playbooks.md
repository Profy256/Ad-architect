# Product-type playbooks

Starting points per product type. They inform, never replace, the screen-by-screen analysis of the real product. Each lists best-fit formats, usual natural breaks, things to avoid and special cautions.

## Contents
Marketplace / listings · Video and audio · Learning / education · Content / articles · Social / community feed · Tools, SaaS and desktop apps · Games · Commerce, fintech, payments · AI assistants and chat tools · Job / career platforms · Maps / local discovery · Recipes and cooking · Fitness and wellness · Sports scores and news · Weather and quick-lookup utilities · Ride, delivery and logistics · Invoicing, accounting and business admin

## Marketplace / listings (property, products, vehicles, services)
- **Best fit:** featured/promoted/boosted listings in results; sponsored map pins; sponsored seller/agent/business profiles; sponsored category or filter; contextual recommendations on detail pages ("similar, sponsored"); empty-state recommendations (no saved items yet).
- **Natural breaks:** results loaded; after viewing several details; after saving or contacting.
- **Avoid:** interstitials between search and results; banners near Contact/Call/Pay buttons; ads inside the contact or booking form; unlabelled paid placement.
- **Cautions:** paid placement must not degrade result quality: cap sponsored slots per page, require minimum relevance to the query/filters (a sponsored listing outside the user's price or location filter is a bad ad), keep organic ranking trustworthy, and label every paid listing. Sellers/agents are your advertisers: self-serve boosting with transparent pricing can outperform programmatic ads. Verify listings (fake listings destroy trust faster than any ad).

## Video and audio
- **Best fit:** sponsored video cards in recommendations; companion banners beside the player; small muted overlay; pre-roll (skippable) before a session; post-roll then recommendations; sponsor segment (host-read audio).
- **Natural breaks:** before play, chapter/episode end, between playlist items.
- **Avoid:** mid-roll mid-sentence or mid-scene; unskippable pods; double pre-roll; ads that start with sound; ads covering captions or controls; interrupting a live event at a random time.
- **Cautions:** mid-roll belongs only at detected or authored breakpoints. If no breakpoints exist, prefer pre/post-roll and sponsored cards. Cap ads per hour of viewing and never stack.

## Learning / education
- **Best fit:** sponsored courses/resources/tools in recommendation slots; sponsored challenges or hackathons; sponsored section or learning path; rewarded unlock for optional extras (extra practice, a certificate preview); post-lesson recommendation.
- **Natural breaks:** lesson complete, quiz submitted, streak earned.
- **Avoid:** any ad during a lesson, exam, quiz, or while the learner types code or answers; ads on assessment screens; ads that interrupt concentration; promoting competing training in the middle of a course.
- **Cautions:** learners are in a focused, high-trust context; keep sponsorship educational and relevant. Check age rules if students may be minors.

## Content / articles / blogs
- **Best fit:** in-content native units between sections; sidebar units on desktop; end-of-article recommendation widget; sponsored articles clearly labeled; sticky sidebar companion.
- **Natural breaks:** section end, article end.
- **Avoid:** ads mid-sentence or mid-paragraph; layout shift while reading; sticky bars covering text; autoplay video with sound; content-gate walls on first visit.
- **Cautions:** keep density modest; reserve slot sizes to prevent shifting text.

## Social / community feed
- **Best fit:** native in-feed sponsored posts with consistent card structure and label; sponsored community/event; creator sponsorships with disclosure.
- **Natural breaks:** feed scroll gaps between items.
- **Avoid:** interstitials on navigation; ads in direct messages or conversation threads; sponsored comments/answers without strong labels and moderation; ads that imitate user posts without clear labeling.
- **Cautions:** feed ad cadence is the main control (first position, spacing, density). Moderate advertisers, because users judge the platform by the ads they see.

## Tools, SaaS and desktop apps (Tauri/Electron/web apps)
- **Best fit:** sponsored feature/tool inside an existing page ("Free X, sponsored by Y"); empty-state and loading-state sponsor lines; sponsored templates/resources; footer or sidebar partner unit on non-working screens; affiliate recommendations in a "recommended tools" area.
- **Natural breaks:** after export/save, after a task completes, on dashboard idle.
- **Avoid:** ads in editors/creation canvases, near save/submit/export controls, on settings or account pages, during file operations, or anything that steals focus from a text field.
- **Cautions:** for professional tools, ads tend to signal "cheap", so prefer sponsorships, partner integrations and an ad-free paid tier. Desktop apps cannot rely on browser-style ad SDKs; direct-sold sponsor cards you render yourself are simpler, lighter and easier to control.

## Games
- **Best fit:** rewarded video (extra life, revive, bonus) the player chooses; interstitial at level completion with a frequency cap; small banner on menu/non-play screens.
- **Natural breaks:** level complete, game over, between sessions.
- **Avoid:** any ad during active play; interstitial on the first sessions; forced ad right after a failed purchase; accidental-tap placements near gameplay controls; ads for age-inappropriate products.
- **Cautions:** if the game targets children, restrict formats and data use (see policy file).

## Commerce, fintech, payments
- **Best fit:** sponsored products/offers in browse and search; deal and coupon cards; affiliate recommendations; post-purchase recommendations (after the confirmation is clearly seen).
- **Avoid:** anything in cart, checkout, payment, KYC, transfer, balance and security screens; ads that resemble payment buttons or bank notices; lending/high-risk financial ads without strict vetting.
- **Cautions:** trust is the product. In regulated or financial contexts, a bad advertiser (scam, predatory loans) does more harm than the revenue is worth. Use category blocklists and approval for sensitive advertisers.

## AI assistants and chat tools
- **Best fit:** clearly separated sponsored suggestions outside the response body; sponsor placement in sidebars, empty states, or follow-up suggestion areas.
- **Avoid:** inserting ads inside generated answers; ads that look like advice; ads in sensitive conversations (health, legal, mental health, finance); ads that influence the answer without disclosure.
- **Cautions:** the answer's integrity is the product. Any perception that answers are being steered by advertisers destroys trust.

## Job / career platforms
- **Best fit:** promoted jobs and featured employers in search results; sponsored career resources/courses; sponsored events.
- **Avoid:** ads in application forms and CV uploads; promoting jobs unrelated to the search; scam-risk advertisers.
- **Cautions:** fake or low-quality jobs are the trust risk. Verify employers.

## Maps / local discovery
- **Best fit:** sponsored pins and result cards matched to the query and location; sponsored categories.
- **Avoid:** blocking the map interaction area; covering navigation controls; distracting during active navigation (safety).
- **Cautions:** sponsored pins must be visibly distinct and relevant to the search.

## Recipes and cooking
- **Best fit:** native sponsored recipe or ingredient cards in browse/search; grocery or kitchenware affiliate on the recipe list and detail page below the method; sponsored collections ("Ramadan menus", "student budget meals"); contextual units between sections on desktop web.
- **Natural breaks:** after saving, after finishing a recipe, on browse screens.
- **Protected:** **cook mode / step-by-step mode** (hands are busy, the screen stays on, timers run), ingredient lists and method steps (no ads inside or between steps), timers, and shopping-list checkout.
- **Avoid:** layout shift on recipe pages (the classic long-scroll recipe-site problem); video ads that cover the method; interstitials when opening a recipe.
- **Cautions:** keep ads out of the reading flow between ingredients and steps; reserve slot space so the text does not jump while someone is cooking.

## Fitness and wellness
- **Best fit:** sponsored programs, gear and nutrition content outside workouts; rewarded unlocks of extra plans.
- **Protected:** active workout and timer screens, health data entry and sensitive metrics, medical advice screens.
- **Cautions:** health claims and body-image ads are high risk; never target on health data; see the health vertical.

## Sports scores and news
- **Best fit:** native in-feed cards, sponsored match pages or sections, companion units on match pages, sponsored stats widgets.
- **Avoid:** takeover or interstitial on live-score refresh; ads that shift scores while updating.
- **Cautions:** this is the audience betting advertisers want. Treat betting ads as a restricted category: licensed advertisers only, verified-adult audience, local regulator rules, responsible-gambling messaging; otherwise block the category.

## Weather and quick-lookup utilities
- **Best fit:** a single labeled sponsor card or modest banner below the primary answer; contextual offers (umbrella, travel).
- **Avoid:** anything between the user and the answer; interstitials on open (users want a glance, in seconds).

## Ride, delivery and logistics
- **Best fit:** sponsored merchants and offers in browse; post-trip or post-delivery recommendations.
- **Protected:** live tracking, pickup/drop-off, payment, safety/SOS, driver-contact screens, anything used while moving.

## Invoicing, accounting and business admin
- **Best fit:** partner offers in a "recommended tools/services" panel (payments, banking, insurance, tax tools) on the dashboard; sponsored templates and resources; sponsored feature ("Powered by X payments") with disclosure.
- **Protected:** the invoice/quote editor, line items, tax and legal text, payment links and reconciliation, export/send, billing and subscription screens, settings and licence/update dialogs.
- **Cautions:** professionals read ads as cheapness; prefer sponsorship, referral and a paid tier. Financial-product referrals need disclosure and vetting.
