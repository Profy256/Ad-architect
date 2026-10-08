# Worked examples (match this quality and shape)

Two models of output: a full audit (Example 1) and a quick decision (Example 2). They show tone, depth, labeling and honesty. Do not copy numbers or products; copy the structure and the reasoning discipline.

## Contents
1. Example 1: full audit (student property marketplace, small audience)
2. Example 2: quick decision (mid-roll question)
3. What makes these good

---

## 1. Example 1: full audit

**Request:** "Student property marketplace app in Kampala: search, listing details, saved homes, contact landlord, mobile-money booking deposit. About 3k monthly users. Where do I put ads? I was thinking a full-screen ad on app open and a banner on every screen."

**A. Product understanding**
- **Ad posture:** Passive-first. *Source: assumed default, you did not specify.* Plan contains only non-interruptive placements; interruptive ideas are in section E as a reserve list.
- **Classification:** Android-first mobile app (confirm iOS/web), vertical = marketplace/classifieds, audience = students (check ages; mostly adult, treat under-18 as possible), country = Uganda.
- **Eligibility gate:** property listings are an eligible category on Google networks; no restricted vertical. Third-party ad demand in this market is typically low (assumption; check your network's real eCPMs), so direct sponsors and paid listing boosts matter more.
- **Readiness check:** about 3k monthly users means programmatic banners will earn very little (formula and assumptions in section H). Retention and supply density matter more than ad impressions right now.
- **Revenue engine:** the paying customers are landlords/agents who want visibility, so **paid featured listings** are the primary "ad".
- **Your two ideas:** (1) *App-open full-screen ad:* rejected. It hits the most fragile moment, adds waiting, and Google Play restricts unexpected full-screen interstitials and ads before the loading screen. (2) *Banner on every screen:* rejected as a blanket rule. Banners near Contact and Pay buttons cause accidental taps and cheapen a trust-heavy product, and at this traffic they earn little.

**B. Screen inventory** (from code scan; ✱ = assumed): Onboarding, Login/Register, Home, Search, Results, Listing detail, Saved homes, Contact landlord, Booking deposit (mobile money), Profile/settings, Notifications ✱.

**C. Ad placement map**
```
HOME
├── "Featured homes" carousel (paid, labeled "Featured")      🟢
└── Sponsored partner card (student services, labeled)         🟡 once a direct sponsor exists

SEARCH RESULTS
├── Featured listing at position 3, then max 1 per 8 results  🟢 same card layout, "Featured" tag, must match the user's filters
└── Banner above filters                                       🔴 low value, pushes filters down

LISTING DETAIL
├── "Similar homes" with 1 sponsored item below the fold       🟢
└── Sticky banner near Contact/Call                            🔴

SAVED HOMES (empty state)
└── Sponsor line "Find your next home with X"                  🟡

CONTACT LANDLORD · BOOKING DEPOSIT · LOGIN/REGISTER · SETTINGS  ⚪ NO AD
```

**D. Protected screens (⚪ NO AD):** Contact landlord (accidental taps, privacy), booking deposit and any mobile-money step (money moves), login/register (non-content screens), settings/profile edits, verification and any listing upload form.

**E. Interruptive opportunities (reserve list, NOT in the plan):**
| Format | Natural break | Benefit | Risk | Caps if enabled | Trigger to consider |
|---|---|---|---|---|---|
| Rewarded "unlock extra saved-home alerts" | User chooses | Medium | Low | User-initiated | If featured-listing revenue stalls and you want a free-tier extra |
| Interstitial after a completed booking, after confirmation is seen | After success | Low-medium | Medium | 1 per user per week | Only if retention is stable for 8+ weeks |

**F. Non-interruptive plan (core):** featured listings (highest value/lowest friction), contextual "similar homes", partner cards, empty-state sponsor line. Sold directly to landlords/agents.

**G. Frequency strategy** (starting hypotheses to test): no sponsored unit in the first session until the user views a listing; 1 featured slot per results page plus 1 per 8 organic results; max 1 sponsor card per Home view; no unit adjacent to a primary button; never two paid units adjacent.

**H. Revenue strategy:** run `scripts/revenue_estimator.py` with your real traffic and eCPM assumptions: at 3k users a handful of banners yields small amounts, whereas 10 to 20 landlords paying a flat weekly boost (priced from landlords' willingness to pay, which you must test) is the real lever. Accept mobile-money payment from advertisers. Build first: featured listing + a simple "boost this listing" flow.

**I. UX risk report:** paid listings can degrade trust if irrelevant or fake. Mitigate: relevance to filters, label, verified landlords, cap per page, report button. Watch: contact rate on featured vs organic, search-to-contact conversion, D7 retention.

**J. Final architecture and rollout:** Phase 1 featured listings and "similar homes" → Phase 2 partner sponsor cards → Phase 3 (only if wanted) reserve items. Flags per placement, holdout group, guardrails on retention and contact conversion.

**Open question (one):** How much interruption are you willing to accept to earn more? (non-interruptive only / plus user-chosen extras / maximum revenue). I assumed non-interruptive only.

**Verified vs unverified:** Play Console disruptive-ads rules verified; eCPMs and landlord willingness to pay are assumptions you must replace with real data.

---

## 2. Example 2: quick decision

**Request:** "Video learning app, lessons 10 to 25 minutes with chapters. Should we use mid-roll ads every 5 minutes?"

**Verdict: 🔴 No to timer-based mid-roll. At most 🟠 chapter-boundary breaks, held in reserve.** *(Posture assumed: Passive-first.)*

- **Why not:** a timer fires mid-explanation. For learners that breaks concentration and comprehension, the exact moment they are most invested. Churn risk is high and the revenue per annoyed user is low.
- **Better:**
  1. Sponsored resource card beside/below the player (🟢).
  2. Post-lesson recommendation with one sponsored course (🟢).
  3. Skippable pre-roll once per session only if you want video ads (🟡, opt-in).
  4. Rewarded unlock for optional extras (🟡, opt-in).
- **If you still want mid-roll:** only at chapter ends, never during quizzes or practice, max 1 per lesson and 1 per 20 minutes, never stacked, grace period for new users; roll out to 10% with a retention guardrail.
- **Tradeoff:**
```
OPTION A  Timer mid-roll   Revenue 7/10  UX impact 2/10  Retention risk High
OPTION B  Sponsored card + post-lesson recommendation   Revenue 5/10  UX impact 9/10  Retention risk Low
RECOMMENDATION: B. A gives up learner focus for a modest revenue gain; B keeps lessons intact.
```
- **Question:** are you open to user-chosen extras like rewarded unlocks, or non-interruptive only?

---

## 3. What makes these good

- States the **posture** and whether it was stated, inferred or assumed.
- **Challenges** the owner's assumptions instead of just placing ads.
- Classifies surface, vertical, audience and eligibility **before** formats.
- Every placement has a **label**; protected screens are explicit with reasons.
- Interruptive ideas appear only as a **reserve** unless the developer opted in.
- Numbers are **flagged as hypotheses or assumptions**; verified facts are named as verified.
- One open question, not an interrogation.
- Short where the question is short (Example 2), full where the request is a whole audit (Example 1).
