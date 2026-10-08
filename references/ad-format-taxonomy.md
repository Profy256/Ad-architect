# Ad format taxonomy

## Contents
1. The three axes
2. Format families (A to H) with default ratings
3. Interruption ladder
4. Format-specific notes that change the decision
5. Default dispositions (reject / conditional / safe)
6. Standard display sizes
7. Moment-to-format selector
8. Classification pitfalls

## 1. The three axes

Never reduce an ad to "interruptive = bad, non-interruptive = good". Rate every candidate on:

| Axis | Scale (low → high concern) |
|---|---|
| Intrusiveness | passive → noticeable → interactive → interruptive |
| User control | user chooses → optional interaction → no action required → forced |
| Context | directly useful → contextual → somewhat relevant → irrelevant |

(Control and context are listed from best to worst so that moving right is always worse on every axis.)

Then add Timing, Frequency and Reward. The decision is the combination: Context × User intent × Format × Timing × Frequency × Relevance × User control.

Examples of why it matters:
- Rewarded 20 s video: medium intrusiveness, user chooses, high context → potentially a good experience.
- Tiny irrelevant banner: low intrusiveness, but irrelevant → possibly a poor experience.
- Small banner covering the "Pay" button: low intrusiveness on paper, terrible in context.

## 2. Format families

Default ratings are starting points. Adjust for the actual screen. Intr = intrusiveness, Ctl = user control, Ctx = typical context fit.

### A. Display
| Format | Intr | Ctl | Notes |
|---|---|---|---|
| Static/responsive banner (header, footer, in-content, sidebar) | passive | none needed | Low value per impression; safe only if it never touches controls |
| Anchored/sticky bottom banner | noticeable | none needed | Eats thumb zone; collides with bottom navigation; check safe areas |
| Sidebar / skyscraper / half-page (desktop) | passive | none needed | Best use of desktop whitespace; hide or collapse on narrow widths |
| Video banner (muted autoplay, click-to-play, in-banner video) | noticeable | optional | Muted by default; lazy-load; mute/close control |
| Floating card/corner unit | noticeable | optional | Becomes intrusive with size, sound or motion; must be dismissible and clear of controls |
| Companion ad | passive | none needed | Sits beside a player/content; content continues |
| Expandable (user-triggered) | interactive | chosen | Acceptable when expansion is user-initiated; auto-expand is not |

### B. Native
| Format | Intr | Notes |
|---|---|---|
| In-feed native card | passive | Matches feed rhythm; must be clearly labeled |
| Recommendation widget / "you may also like" | passive | Strong when contextual; avoid low-quality "around the web" clickbait grids |
| Sponsored post/article/discussion/question | passive | Needs strong disclosure and moderation |
| Sponsored search suggestion / result | passive | High intent, high relevance |
| Sponsored notification-center item | passive | Only inside the in-app notification list, never as a surprise popup |

### C. Marketplace / listing
Featured, promoted, boosted, premium listing; sponsored seller/business/agent; sponsored map pin; sponsored filter or category. Usually the highest-value, lowest-friction inventory for marketplaces because the user is already looking at listings. Guard against paid placement degrading result quality (see playbooks).

### D. Content
Sponsored article/tutorial/video/podcast segment, creator sponsorship, product placement, case study. The content itself must be useful. Disclose clearly.

### E. Promotional
Deal/coupon/discount card, offer card, affiliate recommendation, comparison table with a sponsored row. Good when the user is already evaluating options; disclose affiliate relationships and sponsored rows.

### F. Interactive
Rewarded video/interaction, watch-to-unlock, playable ads, quiz/poll ads, sponsored challenges and contests, sponsored surveys. Fine when optional and genuinely engaging.

### G. Sponsorship (brand-level)
Sponsored section/category/page/event/community/series/leaderboard/feature/tool ("Free CV Builder, sponsored by X"), branded UI element, branded experience, empty-state or loading-screen sponsor line. Often the best option when traffic is small: a few premium partners instead of programmatic inventory.

### H. Contextual
Ads chosen from the content/search/location/task rather than from personal identity: search-intent, article-context, category, map/location, user-task-related recommendations. Prefer contextual targeting where consent or data-protection rules are a concern.

### I. Off-platform / outbound channels
Email newsletter ads, promotional email, push notification ads, SMS. These leave the app and are the easiest way to cause unsubscribes, uninstalls and complaints. Require opt-in, per-channel frequency limits, easy opt-out and relevance. SMS needs especially strong consent.

### J. Interruptive formats
Interstitial (image/video/rich/playable), full-screen video, pre-roll, mid-roll, post-roll, bumper, forced/unskippable video, app-open, splash, transition/page-break ads, download-gate/content-gate, popups/overlays, takeovers, exit-intent, timed and frequency-triggered ads, audio interruptions, forced-action ads.

## 3. Interruption ladder (least → most disruptive)

```
Expandable (user-triggered)
 → Overlay / lower-third (small, dismissible, content keeps playing)
 → Floating video (small, muted)
 → Post-roll / content-complete ad
 → Interstitial at natural break
 → Pre-roll (skippable)
 → Pre-roll (non-skippable) / app-open
 → Mid-roll at natural break
 → Mid-roll at arbitrary time
 → Full-screen video / takeover
 → Content gate / download gate
 → Unskippable pods, double pre-roll, forced action
 → Aggressive popups, pop-unders, back-button intercepts
```

This ladder ranks technical interruption, **not** quality of experience. A user-chosen rewarded ad sits mid-ladder yet can be better received than a low-ladder irrelevant overlay. Use the ladder to find the least interruptive option, then check control and context.

Video-specific grouping: Low = small/muted video banner, companion, sponsored video card. Medium = skippable pre-roll, post-roll, small overlay. High = mid-roll, full-screen, unskippable.

## 4. Format notes that change decisions

- **Pre-roll** interrupts before consumption begins, so it is the most defensible in-stream break. **Post-roll** is least annoying: the task is done. **Mid-roll** only at chapter/scene/section ends; a timer firing mid-sentence is a rejection.
- **Bumper ads** (≤6 s, non-skippable) are still forced; use sparingly.
- **Lower-third overlay** is low-interruption only if small, dismissible, clear of captions/controls, and time-limited.
- **SqueezeBack / picture-by-picture** suits live sports-style breaks; rarely appropriate for an ordinary app.
- **Splash/app-open**: only fill an existing launch/load period. If the ad *creates* waiting time, it is an interruption. Never on every launch; never during cold-start after install.
- **Loading/transition ads**: borderline. Acceptable only if the ad does not lengthen the wait.
- **Download-gate / content-gate**: a repeated gate quickly becomes the reason people leave. Prefer a rewarded, user-chosen version with a clear alternative (e.g. subscription or wait).
- **Exit-intent / back-button**: reject by default (see policy file).
- **Push/SMS**: out-of-app; treat as the most intrusive channel regardless of format.
- **Sound**: unexpected audio turns an acceptable ad into an intrusive one. Muted by default, always.
- **Sponsored comments/answers**: high deception risk in community products; need strict labeling and moderation, or avoid.

## 5. Default dispositions

| Disposition | Formats |
|---|---|
| 🔴 Reject by default | Pop-unders; back-button/exit intercepts; unmuted autoplay; lock-screen ads; countdown "wait to load" walls over core content; unskippable mid-roll pods; double pre-roll; page takeovers with autoplay media; fake close/download buttons; ads on protected screens |
| 🟠 High risk, test carefully | Mid-roll (even at breaks), full-screen video, app-open, interstitial during navigation, sticky banners near bottom navigation, floating video, forced download/content gates, push/SMS ads |
| 🟡 Conditional | Interstitial at true natural breaks, skippable pre-roll, post-roll, rewarded (opt-in), expandable, playable, sponsored survey, exit offers that are not blocking |
| 🟢 Usually safe when placed well | Native in-feed, sponsored/featured listings, contextual recommendations, sponsored sections/features, in-content/sidebar display, empty-state sponsor lines, affiliate and comparison cards, sponsored content that is useful |

"Safe" still requires relevance, labeling, performance discipline and frequency control.

## 6. Standard display sizes (CSS px, IAB-style)

Mobile banner 320×50 · Large mobile banner 320×100 · Medium rectangle 300×250 · Leaderboard 728×90 · Large leaderboard/billboard 970×90 / 970×250 · Half-page 300×600 · Wide skyscraper 160×600. Responsive/adaptive units are usually better than fixed sizes on mobile; always reserve the slot size to prevent layout shift. Confirm sizes against the chosen network's current specs.

## 7. Moment-to-format selector (fast lookup)

Match the user's current moment to the least intrusive formats that fit. "Avoid" lists what tends to fail at that moment. This is posture-aware: items marked (opt-in) are only used when the developer allows interruption.

| User's moment | Best fit | Avoid |
|---|---|---|
| Browsing a feed or list | Native in-feed card, sponsored listing, carousel | Interstitials on scroll, autoplay with sound |
| Searching | Sponsored result matching the query, sponsored suggestion, featured listing | Banners above filters, takeovers |
| Reading | In-content native between sections, sidebar (desktop), end-of-article recommendations | Mid-paragraph ads, sticky bars over text, layout shift |
| Watching or listening | Sponsored video card, companion banner, small muted overlay, post-roll, host-read sponsor; skippable pre-roll (opt-in) | Timer mid-roll, unskippable pods, sound-on autoplay |
| Learning or concentrating | Sponsored resource after the lesson, post-lesson recommendation | Anything during lessons, quizzes, exams, code or text input |
| Comparing options | Labeled sponsored row, comparison card, deal/coupon card | Unlabeled paid ranking |
| Waiting (loading, processing) | Quiet sponsor line that adds no wait | Ads that lengthen the wait |
| Task just completed | Post-completion recommendation, sponsored next step; interstitial (opt-in, capped) | Ads before the confirmation is seen |
| Empty state (nothing saved yet) | Sponsor line or recommendations | Pushy full-width banners |
| Returning to the app | Nothing for the first moments; later native units | App-open ads on every return (opt-in only, rarely) |
| Needs a feature or credits | Rewarded ad the user chooses (opt-in) | Forced gates |
| Paying, signing in, verifying, uploading ID, editing important work | **Nothing (⚪ NO AD)** | Everything |
| Leaving | Nothing, or a quiet saved-for-later offer | Exit popups, back-button intercepts |

## 8. Classification pitfalls

- Pre-roll, mid-roll, post-roll, bumper, interstitial, rewarded, playable, pop-up and pop-under are **not** "non-interruptive", even though casual lists sometimes group them with display formats.
- Pop-up/pop-under are interruptive and widely prohibited by networks and browsers; never treat them as display banners.
- Some formats appear in both lists depending on behavior (overlay, floating video, expandable). Classify by *behavior as implemented*: size, sound, timing, dismissibility, control.
- Rewarded ads are interruptive but user-controlled; do not equate them with forced ads.
- "Sticky" and "floating" are placement behaviors, not quality judgments.
