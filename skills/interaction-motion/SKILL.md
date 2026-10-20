---
name: interaction-motion
description: "Use when designing or implementing interactions, microinteractions, transitions, page animations, scroll effects, or motion systems; when an animation feels janky, excessive, generic, or inaccessible."
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
---

# Interaction and Motion

Design behavior before decoration. This skill covers interaction models, states, feedback, microinteractions, transitions, page animation, scroll effects, motion systems, accessibility, and performance.

## Suite integration

Part of the design-engineering suite. `design-engineering` can load this skill automatically when the user asks for animation, interaction, or “make it feel alive.” Direct invocation works too. Read the visual direction first if one exists.

## The stance

Motion is not a layer you add at the end. It is part of the interaction model. Every animation should do at least one of these:

- **Feedback:** confirm an action.
- **Orientation:** show where something came from or went.
- **Continuity:** preserve context across a change.
- **Hierarchy:** direct attention in sequence.
- **Delight:** create a moment of personality.

If it does none of these, cut it. A page with one deliberate motion feels more premium than a page with ten decorative ones.

### Anti-generic gate: generic motion defaults

These are the motion equivalents of template design. Reject them as defaults:

- Fade-and-slide-up on every section.
- Staggered reveal on every list, whether or not sequence matters.
- Hover scale or lift on every card, including non-interactive ones.
- A looping ambient gradient, blob, or particle field.
- A cursor-following blob or magnetic effect on every control.
- 3D tilt on every card.
- Scroll-jacking with parallax on body text.

One signature motion is enough. The rest should be functional feedback. If the brief or the existing system mandates a pattern, record the exception.

## Step 1: Model the interaction

Before timing or easing, define:

| Element | Question |
| --- | --- |
| Trigger | What starts the interaction? Click, hover, focus, scroll, drag, load, data change? |
| Actor | Who initiates it: user, system, or both? |
| State | What state changes? |
| Feedback | How does the user know it happened? |
| Reversibility | Can it be undone? How? |
| Interruption | What happens if the user acts mid-animation? |
| Completion | What signals “done”? |
| Failure | What happens when it fails? |

### States

Every interactive element needs:

- Default
- Hover (pointer devices)
- Focus-visible (keyboard)
- Active/pressed
- Disabled
- Loading
- Error
- Success
- Selected/current
- Dragging (if applicable)

### Affordances

- A control should look interactive before hover.
- Cursor, underline, elevation, and color can signal affordance, but do not rely on color alone.
- Do not animate a control into a different shape on hover in a way that breaks its hit area.
- Keep hit areas stable during animation.

## Step 2: Choose the motion grammar

| Feeling | Grammar |
| --- | --- |
| Calm, premium | Slow ease-out, small distances, low amplitude, long holds |
| Snappy, efficient | Short durations, crisp ease-out, minimal overshoot |
| Playful | Springs, overshoot, squash and stretch, staggered entrances |
| Technical | Linear or near-linear for data, precise fades, no bounce |
| Cinematic | Longer sequences, parallax, depth, orchestrated reveals |
| Tactile | Direct manipulation, spring follow, drag inertia |

The grammar must match the product, not the designer’s mood.

## Step 3: Timing and easing

### Duration

| Interaction | Duration | Notes |
| --- | --- | --- |
| Hover/focus color | 100–150 ms | Fast enough to feel immediate |
| Button press | 80–120 ms | Feedback, not a show |
| Toggle/checkbox | 100–150 ms | Physical manipulation feel |
| Tooltip | 100–200 ms | Delay before show, fast fade |
| Dropdown/menu | 120–200 ms | Short distance |
| Modal/dialog | 200–300 ms | Longer for larger distance |
| Drawer/sheet | 250–350 ms | Respect gesture velocity |
| Page transition | 200–400 ms | Keep perceived speed |
| Large scene change | 300–500 ms | Rare; 500 ms feels slow |
| Scroll reveal | 300–600 ms | Once, not on every scroll |

Most UI animation is **100–500 ms**. Simple feedback around 100 ms; substantial screen changes around 200–300 ms. Entrance often needs slightly longer than exit. Source: [NN/g](https://www.nngroup.com/articles/animation-duration/).

### Easing

| Use | Easing | Why |
| --- | --- | --- |
| Entrance | Ease-out | Fast start, gentle stop; feels responsive |
| Exit | Ease-in | Accelerates away; feels intentional |
| Move A→B | Ease-in-out | Natural acceleration and deceleration |
| Direct manipulation | Spring | Follows the finger; settles naturally |
| Data/progress | Linear | Predictable, honest |
| Playful | Spring with overshoot | Energy, but use sparingly |

Use cubic-bezier curves deliberately. A good default:

```css
--ease-out: cubic-bezier(0.22, 1, 0.36, 1);
--ease-in: cubic-bezier(0.64, 0, 0.78, 0);
--ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
```

### Distance and scale

- Small elements move small distances. A 4px shift can be enough.
- Large elements can move farther but should not cross the whole screen.
- Scale entrances should start close to 1 (0.96–0.98), not 0.
- Avoid animating width/height when transform can achieve the effect.

## Step 4: Choreograph

### Sequencing

- **Lead:** the element that carries the meaning moves first.
- **Follow:** supporting elements follow with a small stagger.
- **Settle:** the final state is stable and readable.
- **Stagger:** 20–50 ms between related items; more for a deliberate cascade.
- **Overlap:** start the next phase before the previous ends to avoid dead time.

### Shared elements

When a card becomes a detail view, preserve the visual connection:

- Keep the same image or title.
- Animate position and size, not a crossfade.
- Use a container transform or View Transition.
- Return to the same place on close.

### Interruption

- If the user reverses mid-animation, start from the current visual state, not the original.
- If the user navigates away, cancel or complete quickly; do not block.
- If data arrives late, do not replay the entire entrance.

## Step 5: Pattern library

### Hover and press

- Hover: small color, border, or elevation change; 100–150 ms.
- Press: scale to ~0.98 or translate 1px; 80–120 ms.
- Do not move the hit area.
- Do not rely on hover for touch.

### Focus

- Always visible for keyboard users.
- Use `:focus-visible`, not `:focus`, to avoid mouse-ring noise.
- Animate the ring only if it remains continuously visible.
- Never remove the outline without a replacement.

### Loading

- **< 100 ms:** no spinner; it will flash.
- **100–300 ms:** subtle inline indicator.
- **> 300 ms:** skeleton or progress with context.
- **> 1 s:** explain what is happening.
- **> 10 s:** allow cancel or background continue.

Skeletons should match the final layout to prevent CLS. Shimmer is optional; a calm pulse is often better.

### Toasts

- Enter from the edge, 150–250 ms.
- Stay long enough to read: 4–6 s for short messages.
- Pause on hover/focus.
- Do not stack more than three.
- Announce with `role="status"` or `aria-live="polite"`.

### Modals and dialogs

- Backdrop fade 150–200 ms; panel 200–300 ms.
- Scale from 0.96 and fade, or slide from the trigger.
- Trap focus; restore focus on close.
- Close on Escape and backdrop click when appropriate.
- Respect reduced motion: fade only.

### Drawers and sheets

- Slide with ease-out; 250–350 ms.
- Allow drag-to-dismiss with velocity.
- Keep the handle and close affordance visible.
- Do not cover the whole screen on desktop unless it is a true modal.

### Accordions

- Animate height with `grid-template-rows: 0fr → 1fr` or a measured height.
- Rotate the chevron 180°.
- Keep the trigger’s hit area stable.
- Do not animate content that is `display: none`.

### Tabs

- Animate the indicator with a shared layout animation or transform.
- Crossfade content 150–200 ms.
- Keep focus on the active tab.
- Do not animate content height unless necessary.

### Tooltips and popovers

- Show after a short delay (300–500 ms) on hover; immediately on focus.
- Fade and shift 4–8 px.
- Keep them out of the pointer path.
- Dismiss on Escape.

### Drag and drop

- Lift the item slightly (scale 1.02, shadow).
- Follow the pointer with a spring.
- Show a clear drop target.
- Animate the settle into place.
- Provide keyboard alternatives.

### Scroll reveal

- Use once, not on every scroll direction.
- Start with opacity 0 and translate 8–24 px, not 100 px.
- Trigger when ~15–20% of the element is visible.
- Respect reduced motion: show immediately.
- Do not hide content that is critical for SEO or no-JS.

### Parallax and scroll-linked

- Keep movement subtle; large parallax causes nausea.
- Do not hijack scroll.
- Use `scroll-timeline` / `view-timeline` where supported, with a JS fallback if needed.
- Test on low-end mobile.

### Page transitions

- Use the View Transitions API where supported.
- Keep transitions short (200–400 ms).
- Preserve shared elements.
- Provide a reduced-motion path that removes the transition.
- Do not block navigation on the animation.

### Text reveal

- One headline, not every heading.
- Reveal by line or word, not by character for long copy.
- Keep the final state readable immediately after.
- Respect reduced motion.

### Counters and numbers

- Animate only when the number changes and the change matters.
- Use a short duration (400–800 ms) with ease-out.
- Preserve the final value exactly.
- Do not animate on every render.

### Cursor and magnetic effects

- Optional, pointer-only, and subtle.
- Never required to understand or operate the UI.
- Disable on touch and reduced motion.
- Keep performance in mind; do not run a RAF loop for a decorative cursor.

### WebGL and 3D

- Use when the experience genuinely benefits.
- Provide a static or lightweight fallback.
- Lazy-load the scene.
- Pause when offscreen or when the tab is hidden.
- Test on low-end devices and with reduced motion.

## Step 6: Implement

### CSS first

Use CSS transitions and keyframes for simple state changes. They are cheap, declarative, and work without JavaScript.

```css
.button {
  transition:
    background-color 120ms var(--ease-out),
    transform 120ms var(--ease-out);
}

.button:active {
  transform: scale(0.98);
}

@media (prefers-reduced-motion: reduce) {
  .button {
    transition: none;
  }
}
```

### Web Animations API

Use WAAPI when you need programmatic control without a library.

```js
element.animate(
  [
    { opacity: 0, transform: "translateY(8px)" },
    { opacity: 1, transform: "translateY(0)" }
  ],
  { duration: 240, easing: "cubic-bezier(0.22, 1, 0.36, 1)", fill: "both" }
);
```

### Motion

Use [Motion](https://motion.dev/) for React layout animations, presence, gestures, and springs.

```jsx
import { motion, AnimatePresence } from "motion/react";

<AnimatePresence>
  {open && (
    <motion.div
      initial={{ opacity: 0, y: 8 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: 4 }}
      transition={{ duration: 0.24, ease: [0.22, 1, 0.36, 1] }}
    />
  )}
</AnimatePresence>
```

### GSAP

Use [GSAP](https://gsap.com/) for complex timelines, scroll-driven sequences, SVG, and precise choreography.

```js
const tl = gsap.timeline({ defaults: { ease: "power3.out" } });
tl.from(".hero-title", { y: 24, opacity: 0, duration: 0.6 })
  .from(".hero-cta", { y: 12, opacity: 0, duration: 0.4 }, "-=0.3");
```

### View Transitions

```css
@view-transition {
  navigation: auto;
}

.card {
  view-transition-name: card;
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(*) {
    animation-duration: 0.01ms;
  }
}
```

### Scroll-driven

```css
@supports (animation-timeline: view()) {
  .reveal {
    animation: reveal linear both;
    animation-timeline: view();
    animation-range: entry 15% cover 35%;
  }
}
```

Always provide a non-animated fallback and respect reduced motion.

## Step 7: Performance

- Prefer `transform` and `opacity`. They can be composited.
- Avoid animating `width`, `height`, `top`, `left`, `margin`, and `box-shadow` on large elements.
- Use `will-change` sparingly and remove it after the animation.
- Avoid layout thrash: read and write separately.
- Use `requestAnimationFrame` for JS-driven motion.
- Pause offscreen animations with `IntersectionObserver`.
- Pause when the tab is hidden.
- Test on a mid-range Android device, not just a desktop.
- Keep INP ≤ 200 ms; animation should not block input.
- Keep LCP ≤ 2.5 s; do not let a hero animation delay the main content.
- Keep CLS ≤ 0.1; reserve space for animated content.

## Step 8: Accessibility

- Honor `prefers-reduced-motion: reduce`. Remove or reduce non-essential motion.
- Do not use flashing more than three times per second.
- Do not hijack scroll.
- Avoid large parallax and zoom effects.
- Provide pause/stop/hide for auto-playing motion.
- Never rely on motion alone to communicate state.
- Keep focus visible during and after animation.
- Do not move focus unexpectedly.
- Ensure animated content remains readable at 200% zoom.
- Test with a screen reader and keyboard only.

Sources: [WCAG 2.2](https://www.w3.org/TR/WCAG2/), [WAI — Animation from Interactions](https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions.html), [MDN — prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)

## Motion spec

For every non-trivial animation, write:

| Field | Example |
| --- | --- |
| Name | Dialog enter |
| Trigger | Open button click |
| Element | Dialog panel, backdrop |
| Property | opacity, transform |
| From | opacity 0, scale 0.96, y 8px |
| To | opacity 1, scale 1, y 0 |
| Duration | 240 ms |
| Delay | 0 ms |
| Easing | cubic-bezier(0.22, 1, 0.36, 1) |
| Exit | 160 ms, ease-in, opacity 0, y 4px |
| Reduced motion | opacity only, 1 ms |
| Performance | transform/opacity only |
| Interruption | reverse from current state |

Use `templates/motion-spec.md`.

## Common mistakes

| Mistake | Consequence | Fix |
| --- | --- | --- |
| Animating everything | Noise, slow, inaccessible | One signature moment |
| Too long | Feels laggy | 100–500 ms |
| Linear motion | Mechanical | Ease-out/ease-in |
| Animating layout properties | Jank | Transform/opacity |
| No reduced-motion path | Accessibility failure | Media query |
| Scroll-jacking | Nausea, lost control | Native scroll |
| Hover-only interactions | Touch users excluded | Tap/focus alternatives |
| Spinner for <100 ms | Flash | Delay before showing |
| Replaying entrance on data change | Distracting | Animate the change only |
| Decorative WebGL on low-end | Battery drain, jank | Lazy-load, fallback, pause |
| Fade-slide-up on every section | The generated-page default | One orchestrated moment, or event-driven motion |
| Stagger on every list | Sequence implied where none exists | Stagger only when order matters |
| Hover-lift on every card | Decoration on non-actions | Feedback only on interactive elements |
| Looping ambient gradient | Motion with no message | Cut it, or give it a job |

## Quality bar

- [ ] Every animation has a purpose.
- [ ] No generic motion default ships without a recorded exception.
- [ ] One signature moment at most; the rest is functional feedback.
- [ ] Timing and easing are specified.
- [ ] Enter and exit are both designed.
- [ ] Interruption is handled.
- [ ] Reduced motion is implemented.
- [ ] Keyboard and focus behavior is correct.
- [ ] It runs at 60fps on a mid-range device.
- [ ] It does not block input or navigation.
- [ ] It does not cause layout shift.
- [ ] It is tested with real content.

## Related skills

- `design-engineering` for the full workflow.
- `visual-ui-design` for the visual direction.
- `frontend-craft` for production implementation.
- `design-critique` for review.
- `web-perf` for performance diagnosis.

## References

- `references/motion-patterns.md` — code patterns for common interactions.
- `templates/motion-spec.md` — animation specification.
