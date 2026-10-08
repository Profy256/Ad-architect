# Implementation standards

Read before writing or reviewing any ad code. Good placement can be ruined by poor implementation.

## Contents
0. Network capability check
1. Universal rules
2. Layout stability and slot reservation
3. Loading and performance
4. Native in-feed ads (with corrected example)
5. Muted video banners
6. Sticky, floating and overlay units
7. Rewarded and interstitial flow rules
8. Accessibility
9. Mobile and desktop specifics
10. Failure handling and kill switches
11. Instrumentation

## 0. Network capability check (do this before designing a component)

Pick the route that actually supports what the developer wants. A common mistake is designing a custom "native" component around a network that does not allow it.

| Route | Where it works | Native / custom styling | Notes |
|---|---|---|---|
| Google AdSense | Websites (AdSense is a website product; apps use AdMob; not re-verified this session) | In-feed and in-article units are styled through the AdSense layout tools; you cannot take the ad's content and render it in your own component | Auto ads and manual units; policy applies to placement, labeling and content |
| Google AdMob | Android, iOS and cross-platform apps | Native ads: the SDK returns assets and you render them in your own layout, inside the SDK's native ad view, with required attribution and registered asset views | Rewarded, interstitial, banner, app-open and native formats; child/teen age-treatment settings and consent tooling |
| Google Ad Manager | Web and apps | Native styles/templates let you render a matching layout | More control and complexity; suited to direct-sold plus programmatic |
| Other networks (AppLovin, Unity, ironSource, Meta Audience Network, Taboola/Outbrain and similar) | Mostly apps or content sites | Each has its own native rules | Check certification for children's apps (Families self-certified list) |
| Direct-sold, self-rendered sponsor cards | Anywhere | Full control: you render your own sponsor data, labeled, with first-party tracking | Best for marketplaces, desktop apps, small audiences; you own vetting, labeling and reporting |

Consequences for common requests:
- "An in-feed component that copies my card styling using AdSense in a React Native app": AdSense does not serve apps, so the route is AdMob native (or direct-sold cards). On web, AdSense in-feed units are styled in the console rather than rendered from your own component; for full component control on web use Ad Manager native styles or direct-sold cards.
- "Make the ad look exactly like organic content": matching layout rhythm is fine, indistinguishable is not, and modifying network-supplied content or attribution is prohibited.
- Always tell the developer which route you chose and why, and confirm the network's current native-ad policy before shipping.

## 1. Universal rules

- Every unit has: a label ("Ad", "Sponsored" or "Promoted"), a fixed or reserved size, a dismiss/report path where the format warrants it, and a frequency rule from the strategy.
- Ads never sit on protected screens (see SKILL.md step 3). Enforce this in code with an allowlist of screens/routes that may render ad slots, not a denylist: a new screen then defaults to no ads.
- Build one ad-slot abstraction (component/service) with a single place for frequency caps, suppression rules, consent state, labeling and kill switch. Do not scatter ad calls through screens.
- Never place a tappable ad adjacent to a primary control. Keep clear spacing so mis-taps are unlikely (check the network's current minimum spacing rules).

## 2. Layout stability and slot reservation

- Reserve the slot's width and height before the ad loads (explicit dimensions or aspect ratio) to avoid Cumulative Layout Shift. Unreserved ads that push content down are one of the worst reading and tapping experiences.
- For responsive units, reserve the smallest likely size and avoid resizing after load; never insert a slot *above* content the user is already reading or tapping.
- If no ad fills: below the fold, collapse the slot; above the fold or inside a feed, collapse in a way that does not move content under the user's finger (collapse only when the slot is off-screen, or keep a quiet reserved placeholder).
- Respect safe areas (notches, home indicators), bottom navigation and on-screen keyboards. Hide or reposition anchored units when the keyboard opens.

## 3. Loading and performance

- Load the ad SDK/script after the app is interactive (idle or after first meaningful content), never in the critical path of first paint or app start.
- Lazy-load slots with IntersectionObserver (web) or on-near-viewport (mobile lists); preload one screen ahead for feeds so the slot is ready when it appears.
- Budget: set explicit limits for ad JS weight, number of requests, video bytes, and main-thread time on the lowest-end target device; measure with and without ads. If ads break the budget, reduce format weight or drop the placement.
- Respect data-saver/low-data settings (e.g. the Save-Data client hint, OS data saver): serve image/text units and do not autoplay video.
- Cap refresh: do not auto-refresh banners aggressively; check the network's allowed refresh policy.
- Do not block rendering or navigation on ad responses; apply timeouts.

## 4. Native in-feed ads

Goal: an ad unit that shares the host feed's structure and rhythm (media, avatar/brand, title, description, action) so it does not jar the user, while staying **clearly distinguishable as an ad**.

Critical compliance notes (these correct a common oversimplification that "a Sponsored badge is all that's required"):
- Matching the feed's layout is fine. Making the ad *indistinguishable* from organic content is deceptive and violates network policy and advertising-disclosure norms. The label must be visible, legible and consistent.
- With network native ads (e.g. AdMob native, AdSense in-feed), you must follow the network's rules for assets and attribution. Typically: use the supplied assets as delivered, include the required ad attribution, register the asset views with the SDK's native ad view so impressions and clicks are counted correctly, don't alter or hide required elements, don't overlay your own controls on the ad, and don't make the whole card look like a plain organic item. Check the network's current native ad policy before shipping; policies change.
- AdChoices / "Why this ad" icons are supplied by the SDK where applicable; don't remove or obscure them.

Insertion logic belongs in one place and should encode the frequency strategy, not hard-code a modulo:

```tsx
// Generic pattern: decide ad positions once, outside render.
export function withAdSlots<T>(items: T[], opts = {
  firstAfter: 5,     // no ad before 5 organic items
  every: 8,          // then roughly every 8 organic items
  maxPerPage: 3,     // density cap
}) {
  const out: Array<{ type: 'item'; data: T } | { type: 'ad'; slotKey: string }> = [];
  let sinceAd = 0, ads = 0;
  items.forEach((data, i) => {
    out.push({ type: 'item', data });
    sinceAd++;
    const threshold = ads === 0 ? opts.firstAfter : opts.every;
    if (sinceAd >= threshold && ads < opts.maxPerPage && i < items.length - 1) {
      out.push({ type: 'ad', slotKey: `slot-${ads}` });
      sinceAd = 0; ads++;
    }
  });
  return out;
}
```

Notes:
- A bare `index % 5 === 4` places an ad after item 5 and every 5th thereafter with no cap and no grace period, and can put an ad as the last item. Prefer an explicit first position, spacing, density cap, and a rule that never places two ads adjacent.
- Use stable keys for slots so virtualized lists do not remount and re-request ads while scrolling.
- Render ads with the same card component structure (e.g. the host `VideoCard` layout via a template/props) but keep the label and ad-network elements intact. If the network's SDK renders the content, wrap it in a container that matches spacing/radius rather than restyling the ad's internals.
- Never pass the ad into an "organic" analytics event (opens, likes); track it separately.

If building a reusable adapter/library: it takes ad data (network or custom JSON), a card template, a label component, and a slot policy (first/every/max/suppress). It must refuse to render without a label and must not expose options that remove the label.

## 5. Muted video banners

Autoplay rules in modern browsers and iOS require muted, inline playback.

```html
<div class="ad-slot" style="width:300px;height:250px;position:relative">
  <span class="ad-label">Ad</span>
  <video muted playsinline loop preload="none" poster="poster.jpg" data-src="ad.mp4"></video>
  <button class="ad-mute" aria-label="Unmute ad">🔇</button>
  <button class="ad-close" aria-label="Close ad">✕</button>
</div>
<script>
  const v = document.querySelector('.ad-slot video');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const saveData = navigator.connection && navigator.connection.saveData;
  new IntersectionObserver(([e]) => {
    if (e.isIntersecting && !reduce && !saveData) {
      if (!v.src) v.src = v.dataset.src;
      v.play().catch(() => {});
    } else v.pause();
  }, { threshold: 0.5 }).observe(v);
</script>
```

- Muted by default; sound only by explicit tap on the unmute control. Never start audio automatically.
- Load the video only when near the viewport; pause when off-screen; use a poster image for the initial frame; honor reduced-motion and data-saver preferences (show the poster instead).
- Provide visible close and mute controls with adequate touch size and accessible names.
- Keep loops short and files small; avoid multiple simultaneous video ads on one screen.

## 6. Sticky, floating and overlay units

- Only in moderate-to-low attention contexts; never over inputs, primary actions, captions or video controls.
- Small by default; the unit plus other fixed UI must not consume a large share of the viewport. Check mobile ad-density guidance from the current Better Ads Standards or your network.
- Always dismissible with a clear, reasonably sized close target; remember dismissal for the session.
- Hide when the keyboard is open, during form entry, and on protected screens.
- Corner/docked video: muted, small, stays clear of navigation menus and content controls.

## 7. Rewarded and interstitial flow rules

- **Rewarded:** always user-initiated, with the reward stated before the ad starts ("Watch a 20 s ad for +10 credits"). Grant the reward only on completion; handle failures gracefully (no ad available → say so, don't punish the user). Provide an alternative path (wait, subscribe, skip) where the feature matters. Do not reward clicks on ads.
- **Interstitial:** show only at a natural break after the user's action has completed and its result is visible; preload ahead so it does not add waiting time; never trigger from a tap on a core control; provide a visible, accessible close after any network-allowed minimum; do not show two in a row; do not show on app start unless it follows the app-open rules in the strategy.
- **Skippable/closing:** the close control must be present, legible and where users expect it; never shrink or hide it, and never fake one.

## 8. Accessibility

- Label every ad region (e.g. a labeled landmark or group such as "Advertisement") so screen-reader users can recognize and skip it; keep it out of the primary reading order's critical path.
- Full keyboard operability for any interactive unit; visible focus; logical tab order; focus moves into a dialog-style interstitial and returns to the triggering element when it closes; Escape closes where applicable.
- Sufficient contrast for the label and controls; text resizes without breaking the slot; touch targets large enough.
- No flashing content; honor `prefers-reduced-motion`; no autoplay with sound; offer pause for motion longer than a few seconds.
- Make dismissal obvious and operable by assistive tech wherever dismissal is intended.

## 9. Mobile and desktop specifics

- **Mobile:** thumb reach, bottom navigation conflicts, safe areas, keyboard overlap, accidental-tap risk, small banner heights, data cost, battery. Test on a low-end device.
- **Desktop/web:** use sidebars and gutters; sticky sidebar units only when they do not cover content; collapse sidebars below a width breakpoint instead of shrinking the ad; header/footer units must not push primary navigation or content down.
- **Desktop apps (Tauri/Electron):** prefer self-rendered sponsor cards over third-party ad scripts; fetch sponsor content from your own endpoint with caching; never block the main thread; respect offline mode by showing nothing (or a cached sponsor line) rather than an error.

## 10. Failure handling and kill switches

- Ad failures must never break the host screen: wrap in error boundaries, apply timeouts, and fall back to nothing.
- Provide remote-config kill switches per placement and per format, plus a global switch, so a problematic ad or advertiser can be removed without an app release.
- Provide an advertiser/creative block path (report ad, category blocklist) and review creatives for sensitive categories.

## 11. Instrumentation

Log impressions with viewability, clicks, dismissals, mute/unmute, rewarded starts/completions, ad load time, no-fill, errors, layout shift attributable to slots, and the surrounding user outcomes (retention, session length, conversion). Compare exposed and holdout groups. Without this data, scores in the audit stay unvalidated judgment.
