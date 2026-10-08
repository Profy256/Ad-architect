# Audit templates, scoring and frequency

## Contents
1. Per-screen audit block
2. Scoring method and label thresholds
3. Worked scoring example
4. Placement map format
5. Frequency strategy: structure and starting hypotheses
6. Tradeoff block
7. UX risk report
8. Measurement and rollout plan

## 1. Per-screen audit block

```
SCREEN: <name / route>
Purpose:
USER INTENT:
USER ATTENTION: low | moderate | high | critical
INTERRUPTION TOLERANCE: very low | low | moderate | high
AD RECOMMENDATION: Yes | No | Conditional      LABEL: 🟢/🟡/🟠/🔴/⚪
RECOMMENDED AD TYPE:
PLACEMENT:
SIZE:
BEHAVIOR:           (autoplay? sound? dismissible? sticky?)
TIMING:             (when it may appear; natural break used)
FREQUENCY:
WHY THIS WORKS:
UX RISKS:
RESTRICTIONS:       (what must not happen: covering controls, sound, etc.)
ALTERNATIVE:        (less intrusive or higher-value alternative)
```

Do not force an ad onto a screen where none belongs. For ⚪ NO AD screens, fill Purpose, Intent, Attention, Tolerance and "WHY NO AD" only.

## 2. Scoring method and label thresholds

Score each candidate placement 0 to 10 per factor.

**Value factors (higher is better)**
- Relevance to the user's current intent
- User benefit (does it help the user, e.g. a deal or a useful listing?)
- Context suitability (fits the screen, content and moment)
- Revenue potential

**Risk factors (higher is worse)**
- Intrusiveness
- Interruption risk
- UX damage risk
- Retention risk
- Trust risk
- Performance impact

Derived values:
- **Fit** = mean(relevance, user benefit, context suitability)
- **Peak risk** = max(UX damage, retention risk, trust risk, performance impact)
- **Friction** = mean(intrusiveness, interruption risk)

Why this shape: intrusiveness, interruption and UX damage are strongly correlated, so averaging all risks would double-count and let one severe risk hide behind benign ones. Taking the *peak* risk makes any single serious problem decisive. Revenue is deliberately excluded from Fit and from the gates so that high revenue cannot offset high UX damage; it only ranks options that already pass.

**Evaluate labels in this order (first match wins):**

1. ⚪ **NO AD**: protected screen or state (see SKILL.md step 3).
2. 🔴 **REJECTED** if any: deceptive or policy-violating pattern; trust risk ≥ 8; peak risk ≥ 8; Fit < 4.
3. 🟠 **HIGH RISK** if any: peak risk 6 or 7; friction ≥ 7 with no user control.
4. 🟢 **APPROVED**: Fit ≥ 7 and peak risk ≤ 3 and (friction ≤ 4 or the user chooses it).
5. 🟡 **CONDITIONAL**: everything else that remains (Fit ≥ 4 and peak risk ≤ 5). List the exact conditions: frequency, timing, size, target, test gate.

Among placements that share a label, rank by revenue potential, then by lower friction.

**Posture overlay (from `ad-posture.md`):** the labels above describe a placement's quality. Whether it enters the plan also depends on the developer's posture. Under the default Passive-first posture, interruptive placements never enter the recommended plan even if they score 🟡 CONDITIONAL; they are listed as "held in reserve". Under Balanced, only user-chosen and post-completion units may enter. Under Revenue-max, interruptive units may enter if they are not 🔴 REJECTED, with caps and guardrails. A developer's explicit request for a specific format opts that format in.

These numbers are structured judgment, not measurements. Show the factor scores and a one-line rationale for the decisive ones. Never present them as empirical. Back them with the measurement plan in section 8.

## 3. Worked example

Screen: Search results on a property marketplace; user searching "apartments Kampala".

| Candidate | Rel | Ben | Ctx | Rev | Intr | Intp | UX | Ret | Trust | Perf | Fit | Peak | Friction | Label |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sponsored listing at result #3 (same card layout, "Sponsored" tag, matches query) | 9 | 8 | 9 | 7 | 2 | 1 | 2 | 2 | 3 | 1 | 8.7 | 3 | 1.5 | 🟢 |
| Full-screen interstitial when tapping Search | 3 | 1 | 2 | 8 | 8 | 8 | 7 | 7 | 4 | 4 | 2.0 | 7 | 8 | 🔴 (Fit < 4) |
| 320×100 banner above filters | 3 | 2 | 4 | 3 | 4 | 3 | 5 | 4 | 3 | 3 | 3.0 | 5 | 3.5 | 🔴 (Fit < 4); better to drop it |

Recommendation: sponsored listing; reject the other two. Reasoning: highest relevance and benefit, lowest risk, and the revenue is competitive with the intrusive options.

## 4. Placement map format

Use a tree per screen; one label per placement.

```
HOME
├── Native sponsored card between sections        🟢
├── Bottom banner                                  🟡 only if bottom nav is not obstructed
└── Full-screen interstitial                       🔴

SEARCH RESULTS
├── Sponsored result (position 3, then every 8)   🟢
├── Featured listing slot (top, max 1)            🟢
└── Full-screen ad                                 🟠

DETAIL PAGE
├── Contextual recommendation below fold          🟢
└── Sticky banner over Contact button              🔴

CHECKOUT / PAYMENT / LOGIN / KYC                   ⚪ NO AD

CONTENT COMPLETE
└── Post-roll / sponsored recommendation           🟢
```

For each leaf the written map (output section C) must also give: format, size, timing, frequency, interruption level, reason.

## 5. Frequency strategy

### Structure to produce
- Session rules: grace period before first ad; max ads per session by class (passive / interactive / interruptive)
- Time rules: minimum spacing between interruptive ads; app-open rule
- Screen rules: max passive units per viewport and per screen
- Feed rules: first ad position, spacing, density
- Journey rules: no ads inside protected journeys; no ad at the end of a critical task before the confirmation is seen
- Hard rule: **no consecutive ads and no ad-on-ad stacking**; a session that hit a cap shows passive units only
- Rewarded rules: always user-initiated; cap daily offers only if the reward economy can be abused
- Suppression rules: paying/premium users, brand-new users in their first session, users who just hit an error or a failed payment, users who just dismissed an interruptive ad

### Starting hypotheses (not facts; adjust by product, session length, intent, format, revenue needs, and test)

| Item | Starting range to test | Rationale |
|---|---|---|
| Grace period | No ad until first value moment, or roughly the first 1 to 2 minutes of the first session | Users judge the product before the ads |
| Interstitial spacing | 3 to 5 minutes minimum between, in content/utility apps; consider fewer (e.g. 1 per several completed tasks) | Natural breaks are scarcer than timers suggest |
| Interstitial per session | 1 to 3 in utility/content apps; more tolerance in games with short levels | Match to natural-break count |
| App-open | At most once per several hours; skip on first launch and cold start after install | Launch is the most fragile moment |
| Native in-feed | First ad after ~4 to 6 organic items; then every ~6 to 10 | Keeps the feed organic |
| Banner | At most one persistent unit per viewport; total ad area well under a third of mobile viewport height | Large-ad-density is a commonly flagged poor experience (Coalition for Better Ads); verify the current standard |
| Sponsored listings in results | 1 to 2 per results page, clearly separated and labeled; never all top slots | Preserves result trust |
| Rewarded | User-initiated; if capped, a few per day | Opt-in changes the tolerance |
| Push/SMS | Opt-in only; low single digits per week at most; easy opt-out | Highest uninstall/complaint risk |

Pick values using the product's session length and number of natural breaks; state the assumption. If the product has no analytics yet, start at the conservative end and loosen only with retention data.

## 6. Tradeoff block

```
OPTION A  <format>   Revenue x/10   UX impact x/10   Retention risk Low|Med|High
OPTION B  <format>   Revenue x/10   UX impact x/10   Retention risk Low|Med|High
RECOMMENDATION: <option>. Why: <the decisive factor, e.g. same advertiser value at much lower risk>
```

## 7. UX risk report

List each placement or pattern that could harm: retention, engagement, trust, conversion, performance, accessibility. For each: the risk, who it hits, how likely, the signal you would watch (e.g. D1/D7 retention, session length, bounce on affected screens, rage taps, uninstall rate, complaints, Core Web Vitals / app start time), and the mitigation (smaller format, lower frequency, move to a natural break, make it user-chosen, remove).

## 8. Measurement and rollout plan

- Phase ads in lowest-risk first: sponsored/featured listings and native cards → contextual/in-content units → rewarded options → carefully capped interruptive formats last (if at all).
- Roll out by flag, to a slice of users, with a holdout group that sees fewer or no ads.
- Primary metrics: revenue per active user, ad-attributed churn, D1/D7/D30 retention, sessions per user, session length, key conversion (listing contact, purchase, lesson completion), ad viewability and fill, ad-slot CLS and load time, complaints/reviews mentioning ads.
- **Guardrails** (stop or roll back if breached): retention or conversion drop beyond a pre-agreed threshold in the exposed group versus holdout, crash/ANR increase, CLS or startup regression, rating decline.
- Review after enough exposure for the metric to be meaningful; low-traffic products should favor qualitative feedback and direct advertiser conversations over statistical A/B tests that cannot reach significance.
