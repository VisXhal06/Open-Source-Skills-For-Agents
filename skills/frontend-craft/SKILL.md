---
name: frontend-craft
description: "Use when implementing a design in production frontend code, improving design fidelity, responsiveness, accessibility, performance, or cross-browser quality; for React, Next.js, Tailwind, shadcn/ui, and framework-agnostic UI work; and when generated UI looks generic, templated, or built from default AI aesthetics."
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
---

# Frontend Craft

Turn a design into production UI that is faithful, fast, accessible, and maintainable. This skill covers semantic HTML, CSS architecture, responsive behavior, state, React/Next.js patterns, Tailwind/shadcn, accessibility, performance, and visual QA.

## Suite integration

Part of the design-engineering suite. `design-engineering` can load this skill automatically when the user asks to build or fix a UI. Direct invocation works too. Read the visual and motion specs first if they exist.

## Principles

1. **Semantic HTML first.** A button is a `<button>`. A link is an `<a>`. A dialog is a `<dialog>` or an accessible primitive.
2. **Progressive enhancement.** The page works without JavaScript for content and navigation where possible.
3. **CSS owns layout.** Use flexbox, grid, container queries, and fluid type before JavaScript.
4. **Components have boundaries.** Separate primitives, patterns, and page-specific UI.
5. **State is explicit.** Loading, empty, error, success, and partial states are part of the component.
6. **Accessibility is structural.** Keyboard, focus, labels, and semantics are not a final pass.
7. **Performance is a feature.** LCP, INP, and CLS are part of the design.
8. **Design fidelity includes behavior.** Spacing and color are not enough; motion, focus, and states matter.
9. **Aesthetics are part of fidelity.** A generic template implemented perfectly is still a failed design. Apply the anti-generic gate before writing UI.

## Anti-generic gate

Fidelity to a generic template is not success. Before building, confirm the design record names the direction, the typeface and why it fits, the palette source, the layout logic, one signature element, and the defaults rejected.

Banned as defaults: Inter, Roboto, Arial, Helvetica, and `system-ui` / `-apple-system` / `Segoe UI` stacks; the Poppins / Montserrat / Open Sans stack; violet, indigo, or purple gradients on white; blue-to-purple "AI" gradients; gradient text; the centered eyebrow-headline-two-buttons hero; three identical feature cards; a pricing trio with a highlighted middle card; identical bento tiles; a floating dashboard mockup; one radius and shadow on every surface; a pill badge above every heading; hover-lift on every card; fade-and-slide-up on every section.

If the design is a banned default, stop and fix the direction. Do not implement it faithfully. If the brief or the existing system mandates a banned choice, record the exception and implement it exactly. Load `frontend-design` for the full gate and replacement method.

## Step 1: Read the design as a system

Before coding, extract:

- Layout and breakpoints.
- Type scale and spacing tokens.
- Color roles and themes.
- Components and variants.
- States for each interactive element.
- Motion spec.
- Content and edge cases.
- Accessibility requirements.
- Performance constraints.

If the design is incomplete, do not invent silently. List the gaps and propose defaults.

## Step 2: Inventory before building

Check:

- Which components already exist?
- Which tokens exist?
- Which primitives (Radix, React Aria, Headless UI) are available?
- Which patterns are already in the codebase?
- Which dependencies are allowed?

Build with what exists. Do not create a new button because the design looks slightly different. Extend the system deliberately.

## Step 3: Build a vertical slice

Start with one real screen or flow end to end:

1. Semantic structure.
2. Layout and responsive composition.
3. Type, color, and spacing from tokens.
4. Interactive states.
5. Keyboard and focus.
6. Motion.
7. Loading, empty, error, and success.
8. Performance check.

A vertical slice exposes integration problems early. Do not build ten static screens first.

## Step 4: Semantic HTML

| Need | Use | Avoid |
| --- | --- | --- |
| Action | `<button>` | `<div onClick>` |
| Navigation | `<a href>` | `<span onClick>` |
| Page structure | `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>` | Div soup |
| Heading hierarchy | `<h1>`–`<h6>` in order | Styled divs |
| Form field | `<label>` + `<input>` | Placeholder-only labels |
| Group | `<fieldset>` + `<legend>` | Visual grouping only |
| Dialog | `<dialog>` or accessible primitive | Custom div without focus trap |
| List | `<ul>`, `<ol>`, `<dl>` | Divs with bullets |
| Table | `<table>` with `<th>` | Grid of divs for tabular data |
| Progress | `<progress>` or `role="progressbar"` | Spinner with no label |

Semantic HTML gives you keyboard behavior, screen reader semantics, and browser defaults for free.

## Step 5: CSS architecture

### Layout

```css
.page {
  display: grid;
  grid-template-columns:
    minmax(1rem, 1fr)
    minmax(0, 72rem)
    minmax(1rem, 1fr);
}

.page > * {
  grid-column: 2;
}

.page > .full-bleed {
  grid-column: 1 / -1;
}
```

### Fluid type

```css
h1 {
  font-size: clamp(2rem, 1.2rem + 4vw, 4.5rem);
  line-height: 1.05;
  letter-spacing: -0.03em;
}
```

### Container queries

```css
.card-list {
  container-type: inline-size;
}

@container (min-width: 40rem) {
  .card-list {
    grid-template-columns: repeat(2, 1fr);
  }
}
```

### Focus

```css
:where(a, button, input, select, textarea, [tabindex]):focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 2px;
}
```

Never remove focus without a replacement.

### Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

### Dark mode

```css
:root {
  color-scheme: light;
  --color-bg: #faf9f6;
  --color-text: #1a1a1a;
}

[data-theme="dark"] {
  color-scheme: dark;
  --color-bg: #121212;
  --color-text: #f2f2f2;
}

@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    color-scheme: dark;
    --color-bg: #121212;
    --color-text: #f2f2f2;
  }
}
```

### CSS discipline

- Use a small number of layers: reset, tokens, base, layout, components, utilities.
- Avoid deep selector chains.
- Avoid `!important` except for accessibility safety nets.
- Prefer logical properties: `margin-inline`, `padding-block`, `inset-inline`.
- Use `:where()` to keep specificity low.
- Use `clamp()` for fluid spacing and type.
- Test at 320px and with 200% zoom.

## Step 6: React and Next.js

### Server/client boundaries

- Keep data fetching and static content in server components.
- Use client components only for interactivity, state, effects, and browser APIs.
- Do not make the whole page a client component because one button is interactive.
- Pass serializable props across the boundary.

### Hydration

- Do not render different markup on server and client.
- Guard browser-only values with `useEffect` or a mounted flag.
- Avoid `Date.now()` and `Math.random()` in initial render.
- Use `suppressHydrationWarning` only for intentional, narrow cases.

### Images and fonts

```tsx
import Image from "next/image";

<Image
  src="/hero.webp"
  alt="Descriptive alt text"
  width={1200}
  height={800}
  priority
  sizes="(max-width: 768px) 100vw, 50vw"
/>
```

- Use `next/font` or self-hosted fonts with `font-display: swap`.
- Preload the hero image only.
- Set width and height to prevent CLS.
- Use modern formats: AVIF, WebP.

### Suspense and errors

```tsx
<Suspense fallback={<Skeleton />}>
  <AsyncSection />
</Suspense>
```

- Use `error.tsx` and `not-found.tsx` in Next.js App Router.
- Do not let a failed widget take down the page.
- Show a useful fallback, not a blank screen.

### Forms

- Use native validation where possible.
- Label every field.
- Show errors next to the field.
- Announce errors with `aria-live`.
- Preserve user input on failure.
- Disable submit only when necessary; explain why.

### Tailwind and shadcn/ui

- Use semantic tokens in the Tailwind theme.
- Prefer `className` composition with `cn()`.
- Do not hardcode colors in components.
- Customize shadcn components through variants and tokens, not one-off overrides.
- Keep accessible primitives (Radix) underneath.
- Use `data-*` attributes for states where useful.

```tsx
<Button variant="default" size="lg" className="w-full sm:w-auto">
  Start free
</Button>
```

## Step 7: State

Every data-driven view needs:

| State | What the user sees |
| --- | --- |
| Loading | Skeleton or progress with context |
| Empty | Explanation and next action |
| Error | What happened, how to fix, retry |
| Success | Confirmation and next step |
| Partial | What is available, what is missing |
| Unauthorized | Why, and how to get access |
| Offline | What still works |

Do not render `null` for a failed fetch. Do not show a spinner forever. Do not show a success state before the server confirms.

## Step 8: Accessibility

- Keyboard: every interactive element is reachable and operable.
- Focus: visible, logical order, restored after dialogs.
- Labels: every input has a programmatic label.
- Contrast: 4.5:1 body text, 3:1 large text and UI components.
- Target size: at least 24×24 CSS px; 44×44 recommended.
- Motion: respect `prefers-reduced-motion`.
- Screen reader: test the main flow with VoiceOver, NVDA, or TalkBack.
- Zoom: usable at 200%.
- Errors: announced and associated with fields.
- Language: set `<html lang>`.
- Skip link: provide one for long navigation.

Sources: [WCAG 2.2](https://www.w3.org/TR/WCAG2/), [web.dev — Learn Accessibility](https://web.dev/learn/accessibility/)

## Step 9: Performance

### Core Web Vitals

| Metric | Good | What to do |
| --- | --- | --- |
| LCP | ≤ 2.5 s | Optimize hero image, fonts, server response, render-blocking resources |
| INP | ≤ 200 ms | Break up long tasks, reduce JS, avoid heavy event handlers |
| CLS | ≤ 0.1 | Reserve space, set dimensions, avoid inserting content above |

### Checklist

- [ ] Hero image is optimized and prioritized.
- [ ] Fonts are subset, preloaded, and `font-display: swap`.
- [ ] No layout shift from images, ads, or embeds.
- [ ] JavaScript is code-split; client components are minimal.
- [ ] Third-party scripts are deferred or removed.
- [ ] Animations use transform/opacity.
- [ ] Long lists are virtualized if needed.
- [ ] Bundle size is reviewed.
- [ ] Lighthouse and real-device tests are run.
- [ ] INP is tested with CPU throttling.

## Step 10: Testing and visual QA

- **Unit:** logic, formatting, state transitions.
- **Integration:** forms, data fetching, error states.
- **Visual regression:** Playwright screenshots or Chromatic.
- **Accessibility:** axe, keyboard walkthrough, screen reader.
- **Performance:** Lighthouse, WebPageTest, real device.
- **Cross-browser:** Chrome, Safari, Firefox, Edge; iOS Safari and Android Chrome.
- **Responsive:** 320, 375, 768, 1024, 1440, 1920.

### Visual QA

Compare against the design at the same viewport. Check:

- Spacing and alignment.
- Type scale and line breaks.
- Color and contrast.
- Border radius and shadows.
- Icon alignment.
- Hover, focus, active, disabled.
- Loading, empty, error.
- Dark mode.
- Long content.
- Zoom.

## Common mistakes

| Mistake | Consequence | Fix |
| --- | --- | --- |
| Div buttons | Inaccessible, no keyboard | Use `<button>` |
| Placeholder labels | Screen reader and usability failure | Visible `<label>` |
| Removing focus | Keyboard users lost | `:focus-visible` ring |
| Hardcoded colors | Theme drift | Semantic tokens |
| Client component everywhere | Large JS bundle | Server-first |
| No image dimensions | CLS | Width/height or aspect ratio |
| Spinner forever | User stuck | Timeout, error, retry |
| Hover-only menus | Touch and keyboard failure | Click/focus alternatives |
| Animation on layout properties | Jank | Transform/opacity |
| Testing only on desktop | Mobile bugs | Real devices and throttling |
| Implementing a generic template faithfully | Looks generated; the build amplifies a weak direction | Fix the direction before coding |
| Swapping purple for blue | Same template, new paint | Change the concept, not the hue |
| Adding one radius and one shadow everywhere | No hierarchy between control, card, and overlay | Radius and elevation by role |

## Quality bar

- [ ] Anti-generic gate passed: direction, type, palette, and layout are specific to the subject.
- [ ] No banned default ships without a recorded exception.
- [ ] Semantic HTML.
- [ ] Keyboard path works.
- [ ] Focus is visible and logical.
- [ ] Screen reader flow works.
- [ ] Contrast passes.
- [ ] Responsive at 320px and 200% zoom.
- [ ] All states implemented.
- [ ] Dark mode works.
- [ ] Reduced motion works.
- [ ] LCP, INP, and CLS are within budget.
- [ ] Visual QA matches the design.
- [ ] Tests cover the critical path.

## Related skills

- `design-engineering` for the full workflow.
- `visual-ui-design` for the visual spec.
- `interaction-motion` for motion.
- `design-systems` for tokens and components.
- `ai-design-workflow` for agent-assisted implementation.
- `design-critique` for review.
- `web-perf` for deep performance work.
- `vercel-react-best-practices` for React/Next.js performance.
- `vercel-composition-patterns` for component composition.

## References

- `references/frontend-checklist.md` — implementation and QA checklist.
- `templates/frontend-qa.md` — QA report.
