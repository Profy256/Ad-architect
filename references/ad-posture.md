# Ad posture: non-interruptive first, interruptive only by opt-in

The developer decides how much interruption their users should face. The skill must know that decision (or make a safe, stated assumption) before recommending any format.

**Default rule: non-interruptive ads have the highest priority. Interruptive ads are never recommended as the primary plan unless the developer explicitly asks for them.** Without a stated preference, the posture is Passive-first.

## Contents
1. The three postures
2. How to determine the posture
3. What to ask when it is unspecified
4. Recommended posture by product situation
5. The escalation ladder (exhaust passive before interruptive)
6. Rules for each posture
7. Handling ambiguous developer wording
8. What to report

## 1. The three postures

| Posture | Meaning | Interruptive formats |
|---|---|---|
| **A. Passive-first (DEFAULT)** | Only non-interruptive, relevant, labeled placements: sponsored/featured listings, native cards, contextual recommendations, in-content/sidebar display, sponsorships, affiliate, empty-state sponsors, small muted video banners | Not recommended. Listed as "held in reserve" with the conditions that would justify them, for the developer to approve or ignore |
| **B. Balanced** | Passive placements first, plus a few user-controlled or natural-break formats if passive revenue falls short | Rewarded (opt-in), expandable, post-roll, completion-point interstitial, all capped and tested; nothing forced |
| **C. Revenue-max (explicit opt-in only)** | Developer accepts more interruption for more revenue | Interstitials at natural breaks, skippable pre-roll, carefully chosen mid-roll, capped app-open; still bounded by the hard lines and by network, store and regulator policy |

Rewarded ads are interruptive by mechanics but user-chosen. Treat them as the first interruptive step (Balanced), not as part of Passive-first, unless the developer asks for them.

## 2. How to determine the posture

Check, in order:
1. **Developer's words** in the conversation, brief, PRD or code comments (see section 7 for phrase mapping).
2. **Existing implementation**: are interstitials/app-open/rewarded already in the code? Existing choices show intent but not necessarily preference; confirm.
3. **Product situation** (section 4): audience, vertical, stage, session pattern.
4. If still unknown: **assume Passive-first**, say so in the report ("Assumed posture: Passive-first, because you did not specify"), and ask the developer the one question in section 3.

Never silently assume a more interruptive posture than the developer stated. Never silently apply a less interruptive posture when the developer clearly asked for more; instead follow the request and show the cost.

## 3. What to ask when it is unspecified

Ask once, briefly, and continue working with the Passive-first default while waiting. Offer plain choices:

> How much interruption are you willing to accept to earn more?
> 1. **Non-interruptive only** (listings, native cards, sponsorships; users are never interrupted). Recommended default.
> 2. **Mostly non-interruptive, plus user-chosen extras** (for example rewarded ads, a post-completion ad).
> 3. **Maximum revenue** (interstitials and video breaks at natural moments, with caps), accepting some retention risk.

If the environment offers a tappable-choice tool, use it; otherwise ask in prose. Do not stall the work waiting for the answer.

## 4. Recommended posture by product situation

Use these to recommend, not to override a stated preference.

| Situation | Recommended posture | Why |
|---|---|---|
| Early-stage product, small audience, retention unproven | A | Retention is worth more than early ad income; interruptions at low traffic earn little |
| Marketplace, jobs, property, classifieds | A | Sponsored/featured listings are high value and low friction |
| Fintech, payments, health, education, kids, community, AI assistants | A | Trust is the product; interruptions are costly or restricted |
| Professional tools, desktop apps, dev tools | A | Interruptions signal low quality |
| Content/news/blog with decent traffic | A, possibly B | In-content native is strong; post-article units are acceptable |
| Video/streaming with a free tier | B | Pre/post-roll and rewarded are normal expectations; mid-roll only at breaks |
| Casual/hyper-casual games | B or C | Users expect rewarded and level-break ads; never during play |
| Utility app with a clear free/paid split | B | Rewarded unlock pairs with a paid tier |
| Betting operators and regulated gambling | A for third-party ads; first-party promotions under responsible-gambling rules | Interruptive promotions raise harm and regulatory risk (see vertical playbook) |
| Minor or mixed-age audiences | A | Restricted formats and categories |

## 5. The escalation ladder (exhaust passive before interruptive)

Never jump to a higher tier because a lower one is "not enough" without first checking that the lower tiers are well used and that the real problem is not something else (placement, targeting, traffic, fill, pricing, wrong model).

1. **Tier 1: Sponsored/featured listings, sponsorships, affiliate, native cards.** Highest value per user, lowest friction. Done first.
2. **Tier 2: Contextual in-content and sidebar/companion display, empty-state and loading-state sponsors, sponsored features and sections, small muted video banners.**
3. **Tier 3: User-chosen extras** (rewarded video, expandable ads, optional sponsored challenges). Only in Posture B or C, or when the developer asks.
4. **Tier 4: Natural-break interruptions** (completion-point interstitial, post-roll, skippable pre-roll, capped app-open). Only in Posture C, or when the developer explicitly asks.
5. **Tier 5: Aggressive formats** (mid-roll, unskippable video, content/download gates). Hard to justify; only if the developer insists, always HIGH RISK, staged test with rollback.
6. **Never:** deceptive, policy-violating or protected-screen placements, in any posture.

Before recommending any step up, state what Tiers 1 and 2 are expected to earn, the gap to the revenue target, the diagnosis of why the gap exists, and the UX cost of the step up. Present the step up as a proposal for the developer to approve.

## 6. Rules for each posture

### Posture A: Passive-first
- Build the whole architecture from Tiers 1 and 2.
- Output section **E (Interruptive opportunities)** contains only "held in reserve" items: format, natural break, expected revenue lift (qualitative), UX risk, caps that would apply, and the trigger ("consider only if retention is stable and Tier 1 to 2 revenue is below target after N weeks"). Label them 🟠 HIGH RISK or 🟡 CONDITIONAL as appropriate, marked "not part of the recommended plan".
- No interstitials, app-open, pre/mid-roll, content gates, popups or forced formats in the recommended plan.
- Even passive units follow the rules: relevance, labeling, no covering controls, reserved space, frequency limits.

### Posture B: Balanced
- Everything in A is built first.
- Add only user-controlled or post-completion units, at identified natural breaks, with caps and a grace period for new users.
- Every added unit has a guardrail metric and a rollback.
- No forced formats.

### Posture C: Revenue-max
- Build A first, then add interruptive units at the best natural breaks by revenue-per-annoyance, with strict caps and suppression rules (new users, errors, failed payments, recent dismissals).
- Show a tradeoff block for each interruptive unit.
- Hard lines and platform/regulator policy still apply: no deceptive patterns, no protected screens, no children's or regulated-vertical violations, no stacking.
- Stage the rollout with holdouts and stop conditions.

## 7. Handling ambiguous developer wording

| Developer says | Treat as |
|---|---|
| "Don't annoy users", "good UX is the priority", "non-intrusive", "no popups" | Posture A (explicit) |
| "We need more revenue", "make more money", "more ads" | Not a posture. Stay in A; diagnose the cause (placement, targeting, traffic, fill, pricing, model); propose a step up as an option; ask the section 3 question |
| "Add rewarded ads", "let users watch ads for credits" | Posture B for that feature (explicit opt-in); the rest stays A unless stated |
| "Add an interstitial/app-open/video ad" | Explicit opt-in for that format. Implement it correctly (natural break, caps, closeable) and report the risk; do not refuse because the default is A |
| "Maximize revenue, I don't care about annoyance" | Posture C, but still bounded by hard lines and policy; explain the retention and policy risks once; do not lecture repeatedly |
| "Everything is allowed" or no restriction mentioned | Not an opt-in. Assume A and ask |
| "Put a banner here" | Specific request, not a posture. Evaluate the placement, explain if harmful, then follow the developer's decision if it is not deceptive or a policy violation |

An explicit request from the developer changes the posture only for what they asked for, unless they say it applies generally.

**Frequency wording:** if the developer asks for an unbounded trigger ("an interstitial after each save", "every time the user opens a recipe"), implement the format but apply a cap by default (for example once per N completed actions or per time window, a grace period for new users, and no ad after errors) and explain why in one or two sentences. Make the cap configurable so the developer can raise it, but never exceed what the network, store or regulator allows, and never let it become consecutive or unbounded by default.

## 8. What to report

In section A of the output include:

```
AD POSTURE: Passive-first | Balanced | Revenue-max
SOURCE: stated by developer | inferred from <signal> | assumed default (not specified)
IMPLICATIONS: what is in the plan, what is held in reserve, what is excluded
OPEN QUESTION: the section 3 question, if the posture was not stated
```

Sections E and F follow the posture: under A, F is the plan and E is the reserve list; under B and C, E contains the approved interruptive units with caps, natural breaks and guardrails.
