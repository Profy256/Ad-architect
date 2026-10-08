# Ad Experience Architect

**A senior product-monetization, UX and ads architect — packaged as an Agent Skill.**

Audit a whole app, website or platform and decide *where* ads belong (and where they must never appear), *which* format fits, *how often*, and *how to build it* — without damaging retention, trust, accessibility or performance.

![Skill format](https://img.shields.io/badge/format-Agent%20Skill-2dd4bf)
![Python](https://img.shields.io/badge/python-3%2B-3776ab?logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen)
![Evals](https://img.shields.io/badge/evals-8%20scenarios-yellow)
![Interruption default](https://img.shields.io/badge/default-passive--first-8b5cf6)

---

## Why this exists

Generic ad advice is the failure mode this skill exists to prevent. Most "where should I put ads" answers are a format catalogue with no opinion: a banner here, an interstitial there, "because there is space."

This skill is a **decision-maker, not a catalogue**. Its north star:

> Maximize **sustainable ad revenue per active user**, not the number of ads.

A placement that earns today and drives users away is a bad decision. **"No ad here" is a first-class answer**, given as confidently as a placement.

**What makes it different:**

- **Protect first, monetize second.** Login, checkout, KYC, bet slips, PIN/OTP, lessons and quizzes, editors and error recovery are marked ad-free *before* any placement is considered.
- **Least intrusive format that can meet the revenue need** — chosen on three axes (intrusiveness, user control, context), not on "big vs small".
- **Non-interruptive by default.** Interruptive formats (interstitials, pre/mid-roll, app-open, popups) are held in *reserve* unless the developer explicitly opts in.
- **Eligibility before design.** A vertical gate (gambling, kids, fintech, health, adult, alcohol) and a per-surface playbook decide what is *allowed* before anything is *recommended*.
- **Honest numbers.** Revenue figures come from `scripts/revenue_estimator.py` with your own eCPM/price assumptions. No invented defaults, ever.

---

## What you get

A full audit output with a fixed structure (A–J), scaled to the size of the question:

| | Section | Contents |
|---|---|---|
| **A** | Product understanding | Ad posture, classification (surface, vertical, audience, countries), eligibility-gate result, assumptions |
| **B** | Screen inventory | Every relevant screen; inferred ones marked |
| **C** | Ad placement map | Per screen: ad, format, size, timing, frequency, reason, label |
| **D** | Protected screens | Explicit ⚪ NO AD list with reasons |
| **E** | Interruptive opportunities | Reserve list (default posture) or approved capped units |
| **F** | Non-interruptive opportunities | The core plan, ordered by revenue-per-annoyance |
| **G** | Frequency strategy | Caps and spacing, flagged as hypotheses to test |
| **H** | Revenue strategy | Highest-value opportunities, model comparison, build order |
| **I** | UX risk report | Retention, trust, conversion, performance, accessibility — with mitigations |
| **J** | Final architecture | One coherent picture, rollout order, measurement plan |

Every placement carries exactly one label:

`🟢 APPROVED` · `🟡 CONDITIONAL` · `🟠 HIGH RISK` · `🔴 REJECTED` · `⚪ NO AD`

For a single question ("Should I use mid-roll?", "Is a sticky banner OK?") it returns a **verdict first** in roughly one screen instead of the full A–J report.

---

## Installation

The repository is a standard [Agent Skill](https://agentskills.io) — a `SKILL.md` plus `references/` and `scripts/`.

**Claude Code / Claude Desktop**

```bash
git clone <this-repo> ~/.claude/skills/ad-experience-architect
```

**opencode**

```bash
git clone <this-repo> ~/.config/opencode/skills/ad-experience-architect
```

**Project-local (shared with your team)**

```bash
git clone <this-repo> .claude/skills/ad-experience-architect   # or .opencode/skills/
```

Then just ask, naturally:

> *"I run a property marketplace app for students. Where should I put ads?"*
> *"Should I use mid-roll every 5 minutes in my video learning app?"*
> *"Build me a native in-feed ad component that matches my VideoCard."*
> *"We need more revenue — put a banner here."*

No invocation command is needed; the skill description triggers it on any ad-placement, monetization or ad-review request — even without the words "ad audit".

---

## How it works

```
 1. Understand the product   → inventory scan, surface/vertical/audience classification,
                                eligibility gate, monetization readiness check
 1b. Set the ad posture      → Passive-first (default) | Balanced | Revenue-max (opt-in)
 2. Map journeys             → intent, attention, interruption tolerance, natural breaks
 3. Protect critical flows   → NO AD list before any placement is considered
 4. Choose the format        → least intrusive that works; 3-axis classification
 5. Score and label          → value vs risk factors, hard gates, one label each
 6. Frequency strategy       → caps, spacing, no consecutive ads (system, not spots)
 7. Revenue strategy         → tradeoff blocks, revenue per active user
 8. Desktop vs mobile        → analyzed separately
 9. Deliver A–J, then build  → to the implementation standards
```

---

## Repository layout

```
ad-experience-architect/
├── SKILL.md                        # Core instructions, workflow, output contract
├── references/                     # On-demand expert knowledge (read when needed)
│   ├── example-report.md           # Target quality: full audit + quick decision
│   ├── ad-posture.md               # Passive-first default, escalation ladder, opt-in rules
│   ├── ad-format-taxonomy.md       # 3-axis format classification, sizes, dispositions
│   ├── audit-templates.md          # Scoring, labels, placement map, frequency, risk report
│   ├── platform-playbooks.md       # 14 surfaces: web, PWA, Android, iOS, desktop, email…
│   ├── vertical-playbooks.md       # 17 industries + the ad-eligibility gate
│   ├── product-playbooks.md        # Marketplace, video, learning, games, fintech, AI…
│   ├── market-context.md           # Low-traffic readiness check, emerging-market context
│   ├── policy-and-trust.md         # Labeling, dark patterns, network/store policy snapshot
│   └── implementation-standards.md # Ad code: layout shift, loading, a11y, native in-feed
├── scripts/
│   ├── inventory.py                # Heuristic screen/route/SDK map of a codebase
│   └── revenue_estimator.py        # Revenue ranges from YOUR assumptions only
└── evals/
    ├── evals.json                  # 8 behavioral test scenarios
    └── check_coverage.py           # Deterministic regression check for the guidance
```

Total reference depth: ~1,250 lines, loaded only when the workflow calls for them.

---

## Scripts

Both scripts are **standard library only** — no `pip install`.

### Project inventory

Maps a codebase before the audit: candidate screens/routes, protected-flow flags (auth, payment, KYC, forms, settings), existing ad SDKs, plus surface and vertical hints.

```bash
python3 scripts/inventory.py /path/to/your/project
python3 scripts/inventory.py /path/to/your/project --json
```

Detects routes from React Router, Next.js/Expo file-based routing, Vue Router, React Navigation, Go handlers and Express; flags AdSense, AdMob, GPT, AppLovin, Unity, ironSource, Meta AN, Taboola/Outbrain and more. Output is **heuristic by design** — it is a starting map to confirm by reading files, not a result.

### Revenue estimator

Back-of-envelope revenue ranges for the monetization-readiness check. It **never supplies eCPMs or prices**: every number is traceable to an assumption you state.

```bash
# Programmatic units: name : impressions/session : eCPM low : eCPM high : fill
python3 scripts/revenue_estimator.py --mau 3000 --sessions 10 \
  --unit "native feed:3:0.6:2.0:0.8" \
  --unit "banner:2:0.2:0.8:0.7"

# Direct-sold slots: name : slots : price/slot/month : sell-through low : high
python3 scripts/revenue_estimator.py --mau 3000 --sessions 10 \
  --direct "featured listing:6:20:0.3:0.7"
```

Output includes totals, revenue per active user, and a reading guide: compare the total against the UX cost before recommending anything.

---

## Evaluation

Eight scenarios in `evals/evals.json` cover the hard cases — small-traffic marketplaces, timer-based mid-roll, "just add a Sponsored badge", licensed betting, minors, desktop apps, and both directions of the posture question (defaulting to passive vs. explicit interruptive opt-in).

`check_coverage.py` is a deterministic regression check: it verifies that the skill's *text* still contains the guidance each eval needs. It cannot judge model output — it catches **missing guidance** before you ship a change.

```bash
python3 evals/check_coverage.py
# eval 1 | PASS | default non-interruptive
# ...
# 0 gap(s)
```

Exit code is non-zero on any gap, so it can run in CI.

---

## Safety and hard lines

The skill refuses to design or implement:

- Ads disguised as platform controls, system notifications, user content, or fake download/close buttons
- Ads that hide that they are ads, or layouts that induce accidental clicks
- Rewards for *clicking* ads (rewards for *watching* are fine where the network allows)
- Forced-dwell countdown walls over core content, back-button/exit hijacking, unmuted autoplay audio
- Anything targeting children outside the certified, age-appropriate restrictions

Performance and accessibility are part of the decision: an ad that shifts layout, drains data, or cannot be dismissed with a screen reader is a **rejected** ad. Policy statements in `references/policy-and-trust.md` carry a `[verified Oct 2026]` snapshot with explicit "not verified here" markers — live policy is always re-checked before shipping.

> This is product guidance, not legal advice. Confirm current network, store and regulator rules before shipping.

---

## Contributing

Contributions are welcome. Before opening a PR:

1. Run `python3 evals/check_coverage.py` — it must report `0 gap(s)`.
2. If you add guidance the skill needs, add or extend an eval in `evals/evals.json` that depends on it.
3. Keep `references/` load-on-demand: the workflow in `SKILL.md` should only read a file when it needs it.
4. Mark policy facts with a verification date, and mark anything unverified as such. Never add default eCPMs, prices or revenue figures.
5. Preserve the defaults: passive-first posture, protected screens first, one label per placement.

---

## License

No license has been applied yet. Add one (MIT and Apache-2.0 are common choices for skills) before accepting external contributions.
