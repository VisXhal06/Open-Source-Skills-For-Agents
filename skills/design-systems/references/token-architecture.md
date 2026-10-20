# Token Architecture

## Three tiers

```text
Primitive → Semantic → Component
```

### Primitive tokens

Raw values. Never use directly in UI.

```css
:root {
  --blue-50: oklch(97% 0.02 255);
  --blue-500: oklch(62% 0.18 255);
  --blue-900: oklch(28% 0.12 255);
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-4: 1rem;
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
}
```

### Semantic tokens

Meaningful roles. This is the main API.

```css
:root {
  --color-bg: var(--blue-50);
  --color-surface: white;
  --color-text: var(--blue-900);
  --color-text-muted: oklch(48% 0.03 255);
  --color-action: var(--blue-500);
  --color-action-hover: oklch(56% 0.18 255);
  --color-border: oklch(88% 0.02 255);
  --color-focus: oklch(58% 0.2 255);
}
```

### Component tokens

Optional aliases for a specific component.

```css
:root {
  --button-primary-bg: var(--color-action);
  --button-primary-fg: white;
  --button-primary-bg-hover: var(--color-action-hover);
  --button-radius: var(--radius-md);
  --button-height: 2.75rem;
}
```

Use component tokens when a component needs to diverge from the semantic default. Do not create a component token for every property.

## Naming

Pattern:

```text
category.role.variant.state
```

Examples:

```text
color.text.primary
color.text.muted
color.surface.raised
color.action.primary
color.action.primary.hover
color.feedback.danger
space.inset.sm
space.stack.md
radius.control
shadow.overlay
motion.duration.fast
motion.ease.out
```

Rules:

- Use semantic names, not appearance names: `text.muted`, not `gray-500`.
- Use the same names in design and code.
- Keep the vocabulary small.
- Avoid abbreviations that only one person understands.
- Use consistent pluralization and casing.

## Themes

```css
:root {
  color-scheme: light;
  --color-bg: oklch(98% 0.01 90);
  --color-surface: oklch(100% 0 0);
  --color-text: oklch(20% 0.02 90);
  --color-text-muted: oklch(46% 0.02 90);
  --color-action: oklch(55% 0.18 255);
  --color-border: oklch(88% 0.01 90);
  --color-focus: oklch(58% 0.2 255);
}

[data-theme="dark"] {
  color-scheme: dark;
  --color-bg: oklch(16% 0.02 90);
  --color-surface: oklch(21% 0.02 90);
  --color-text: oklch(94% 0.01 90);
  --color-text-muted: oklch(72% 0.02 90);
  --color-action: oklch(70% 0.14 255);
  --color-border: oklch(30% 0.02 90);
  --color-focus: oklch(76% 0.14 255);
}
```

## Typography tokens

```css
:root {
  --font-sans: "Inter", system-ui, sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, monospace;

  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 1.875rem;
  --text-4xl: 2.25rem;

  --leading-tight: 1.15;
  --leading-normal: 1.5;
  --leading-relaxed: 1.7;

  --tracking-tight: -0.02em;
  --tracking-normal: 0;
  --tracking-wide: 0.04em;
}
```

## Spacing tokens

```css
:root {
  --space-0: 0;
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-12: 3rem;
  --space-16: 4rem;
  --space-24: 6rem;
}
```

Use `space-1` to `space-4` inside components; larger steps between sections.

## Motion tokens

```css
:root {
  --motion-fast: 120ms;
  --motion-base: 200ms;
  --motion-slow: 320ms;
  --ease-out: cubic-bezier(0.22, 1, 0.36, 1);
  --ease-in: cubic-bezier(0.64, 0, 0.78, 0);
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

## Token pipeline

1. Define primitives.
2. Define semantic roles for light and dark themes.
3. Define component aliases only where needed.
4. Export to CSS variables, Tailwind theme, and TypeScript types.
5. Generate docs from the same source.
6. Audit for raw values outside the token layer.

## Token review questions

- Is this a decision or a value?
- Does it have a semantic name?
- Does it work in both themes?
- Is it used in at least two places?
- Can it be derived from an existing token?
- Does it need a component alias?
- Is it documented?
- Will it survive a rebrand?
