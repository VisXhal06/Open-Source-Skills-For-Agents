---
name: oss-uiux-frontend
description: "Use when contributing UI, UX, accessibility, design-system, CSS, component, or frontend changes to an open-source project or large codebase. Use this for visual bugs, responsive layout, dark mode, keyboard and screen-reader issues, design consistency, component APIs, frontend performance, or reviewing a UI pull request, especially when the project already has its own design language and conventions."
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
  suite: "oss-contributor"
---

# OSS UI/UX + Frontend

Frontend contribution in someone else's project is not a greenfield design exercise. Your job is to make the smallest change that fits the existing design system, passes accessibility and browser expectations, and does not impose your taste on maintainers or users.

Use this skill for UI/UX and frontend work in open source or a large company codebase. For deep visual direction, load the `design-engineering` suite; this skill supplies the OSS contribution lens.

## First: read the project's design language

Before changing a pixel, identify:

- design tokens: color, spacing, type, radius, shadow, motion
- component primitives and their variants
- layout system and breakpoints
- theming: light, dark, high contrast, brand overrides
- iconography and asset pipeline
- CSS approach: modules, Tailwind, CSS-in-JS, utility classes, plain CSS
- state patterns: loading, empty, error, disabled, optimistic, offline
- accessibility baseline: focus, keyboard, labels, live regions, reduced motion
- i18n and RTL support
- browser and device support matrix
- visual regression and e2e test setup

If the project has a design system, use it. If it does not, infer the conventions from nearby components and keep the change local.

## The anti-generic rule in someone else's project

The project's design language wins. If it already uses Inter, a purple accent, or identical cards, do not "fix" that in an unrelated contribution. Match the system and keep the diff local.

The rule applies when you add a new surface, a new direction, or when the maintainer asks for design work. Then do not import the generic defaults:

- **Type:** Inter, Roboto, Arial, Helvetica, or a system stack as an unexamined choice.
- **Color:** violet, indigo, or purple on white; blue-to-purple "AI" gradients; gradient text.
- **Layout:** the centered badge-headline-two-buttons hero; three identical feature cards; a pricing trio with a highlighted middle card; identical bento tiles; a floating dashboard mockup.
- **Components:** one radius and shadow everywhere; a pill above every heading; an icon in a rounded square for every feature; hover-lift everywhere.
- **Motion:** fade-and-slide-up everywhere; stagger everywhere; a looping ambient gradient.
- **Copy:** "Build faster, ship smarter", "AI-powered", "supercharge", "seamless", "unlock" without a claim.

Before coding a new surface, write the six-line design record: direction, type rationale, palette source, layout logic, signature element, rejected defaults. For a local change, at least name the direction and the defaults you rejected. In the PR, say why the choice fits this project rather than your portfolio.

If the maintainer asks for one of these looks, that is the brief. Record it and follow it.

## Workflow

### 1. Reproduce the UI issue

Capture:

- URL, route, or component
- viewport and device
- browser and version
- theme and locale
- user role and permissions
- data state: empty, loading, error, long content
- keyboard and screen-reader behavior
- screenshot or recording
- expected vs actual

UI bugs are often state bugs. Check all states, not only the happy path.

### 2. Find the owning component

Use `large-codebase-navigator` to trace:

```text
route -> page/layout -> feature component -> shared primitive -> token/style
```

Identify:

- the component that owns the behavior
- the shared primitive that should own the fix
- tests and stories that encode expected behavior
- whether the issue is in the app, the design system, or a dependency

Do not patch a shared primitive to fix one page unless the primitive is genuinely wrong. Do not fork a shared component to avoid changing it.

### 3. Design the smallest consistent change

Before coding, state:

```text
User problem:
Current behavior:
Desired behavior:
Affected states:
Components to change:
Tokens or primitives to reuse:
Accessibility impact:
Browser impact:
Test plan:
```

Prefer:

- existing tokens over new hex values
- existing primitives over new one-off components
- CSS that composes over CSS that overrides deeply
- semantic HTML over ARIA patches
- progressive enhancement over a new dependency
- a local fix over a global redesign

### 4. Implement all states

A UI change is incomplete if it only covers the default state. Check:

- loading, empty, error, success
- disabled and read-only
- hover, focus-visible, active, selected
- long labels, truncation, wrapping
- small and large viewports
- light, dark, high contrast
- reduced motion
- keyboard-only and screen reader
- RTL and localized strings
- slow network and offline where relevant

### 5. Accessibility

Treat this as a correctness requirement, not a polish pass.

- Use semantic elements first.
- Every interactive element must be keyboard reachable and operable.
- Visible focus must not be removed without an equivalent.
- Inputs need programmatic labels and error associations.
- Images need appropriate alternative text; decorative images need empty alt.
- Dynamic updates need live regions when users must hear them.
- Color must not be the only signal.
- Contrast must meet the project's target (usually WCAG 2.2 AA).
- Motion must respect `prefers-reduced-motion`.
- Modals and menus need focus management and escape behavior.
- Test with a screen reader when the change affects complex interaction.

### 6. Frontend quality

- Keep bundle impact small. Check whether a utility already exists before adding a package.
- Avoid layout shift; reserve space for async content.
- Avoid unnecessary client-side JavaScript.
- Use the framework's data and state patterns instead of inventing a parallel store.
- Keep component APIs small and composable.
- Preserve server-side rendering and hydration behavior.
- Check cross-browser behavior for the features you use.
- Measure performance when the change affects rendering or data fetching.

### 7. Verify

Run the project's checks:

```bash
<format>
<lint>
<typecheck>
<unit tests>
<component tests>
<e2e or visual tests>
<build>
```

Then verify manually:

- keyboard path
- screen reader announcement
- responsive breakpoints
- dark mode
- reduced motion
- error and empty states
- before/after screenshots

For visual changes, include a before/after image in the PR. For accessibility changes, state exactly what you tested and with which tool.

## UI PR checklist

```markdown
## Problem
## Design rationale (direction, type, palette, rejected defaults)
## Before / after
## States covered
## Accessibility
## Responsive behavior
## Dark mode / themes
## Browser matrix
## Tests run
## Bundle or performance impact
## Screenshots / recordings
## Known limitations
```

## OSS-specific rules

- Do not restyle the whole app because you prefer another aesthetic.
- Do not replace the project's visual identity with a generic template, or use a contribution to impose a personal aesthetic.
- Do not introduce a new UI library for one component.
- Do not rename design tokens or public component props without a deprecation path.
- Do not change default behavior for existing users without maintainer agreement.
- Respect the project's browser support, even if your browser supports a newer feature.
- Keep i18n strings in the project's translation system.
- If the project has no design system, propose one only when the maintainer asks; otherwise make the local change.

## Composition

- `design-engineering` — front door to the design suite.
- `design-systems` — tokens, component APIs, governance.
- `visual-ui-design` — hierarchy, type, color, layout.
- `interaction-motion` — states, transitions, motion.
- `frontend-craft` — production implementation and QA.
- `design-critique` — review and prioritized findings.
- `web-design-guidelines` — accessibility and interface compliance.
- `web-perf` — Core Web Vitals and loading performance.
- `vercel-react-best-practices` and `vercel-composition-patterns` — React-specific patterns.
- `webapp-testing` — browser verification with Playwright.

## Output format

End with:

```markdown
### UI contribution
- Problem:
- Change:
- Design rationale:
- States covered:
- Accessibility evidence:
- Responsive/theming evidence:
- Checks run:
- Not verified:
- Next action:
```

The change is successful when it looks like it was always part of the project.
