# Motion Patterns

Code patterns for common interactions. Adapt the values to the product's motion grammar.

## Tokens

```css
:root {
  --motion-fast: 120ms;
  --motion-base: 200ms;
  --motion-slow: 320ms;
  --ease-out: cubic-bezier(0.22, 1, 0.36, 1);
  --ease-in: cubic-bezier(0.64, 0, 0.78, 0);
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
}
```

## Reduced motion baseline

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

Use the blanket rule as a safety net, then provide intentional reduced-motion states for important transitions.

## Button feedback

```css
.button {
  transition:
    background-color var(--motion-fast) var(--ease-out),
    transform var(--motion-fast) var(--ease-out);
}

.button:hover {
  background-color: var(--button-hover);
}

.button:active {
  transform: scale(0.98);
}

.button:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
```

## Dialog

```css
.dialog {
  opacity: 0;
  transform: translateY(8px) scale(0.96);
  transition:
    opacity var(--motion-base) var(--ease-out),
    transform var(--motion-base) var(--ease-out);
}

.dialog[open] {
  opacity: 1;
  transform: translateY(0) scale(1);
}

.dialog::backdrop {
  opacity: 0;
  transition: opacity 160ms var(--ease-out);
}

.dialog[open]::backdrop {
  opacity: 1;
}

@media (prefers-reduced-motion: reduce) {
  .dialog {
    transform: none;
    transition: opacity 1ms;
  }
}
```

## Drawer

```css
.drawer {
  transform: translateX(100%);
  transition: transform var(--motion-slow) var(--ease-out);
}

.drawer[data-open="true"] {
  transform: translateX(0);
}

.drawer[data-dragging="true"] {
  transition: none;
}
```

For drag-to-dismiss, track velocity and settle with a spring or a short ease-out.

## Accordion with grid rows

```css
.accordion-content {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows var(--motion-base) var(--ease-out);
}

.accordion-content > div {
  overflow: hidden;
}

.accordion[data-open="true"] .accordion-content {
  grid-template-rows: 1fr;
}
```

## Toast

```css
.toast {
  opacity: 0;
  transform: translateY(8px);
  animation: toast-in var(--motion-base) var(--ease-out) forwards;
}

@keyframes toast-in {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

## Staggered list

```jsx
import { motion } from "motion/react";

<motion.ul
  initial="hidden"
  animate="show"
  variants={{
    hidden: {},
    show: { transition: { staggerChildren: 0.04 } }
  }}
>
  {items.map((item) => (
    <motion.li
      key={item.id}
      variants={{
        hidden: { opacity: 0, y: 8 },
        show: { opacity: 1, y: 0 }
      }}
      transition={{ duration: 0.24, ease: [0.22, 1, 0.36, 1] }}
    />
  ))}
</motion.ul>
```

## Shared layout

```jsx
import { motion, LayoutGroup } from "motion/react";

<LayoutGroup>
  {items.map((item) => (
    <motion.div layoutId={`card-${item.id}`} key={item.id} />
  ))}
</LayoutGroup>
```

Use shared layout for tabs, cards to detail, and reordering. Keep the layout stable and avoid animating too many elements at once.

## View transition

```css
@view-transition {
  navigation: auto;
}

.card-image {
  view-transition-name: card-image;
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(*) {
    animation-duration: 0.01ms;
  }
}
```

## Scroll reveal with IntersectionObserver

```js
const observer = new IntersectionObserver(
  (entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        entry.target.dataset.revealed = "true";
        observer.unobserve(entry.target);
      }
    }
  },
  { threshold: 0.15 }
);

document.querySelectorAll("[data-reveal]").forEach((el) => observer.observe(el));
```

```css
[data-reveal] {
  opacity: 0;
  transform: translateY(16px);
  transition:
    opacity 500ms var(--ease-out),
    transform 500ms var(--ease-out);
}

[data-reveal="true"] {
  opacity: 1;
  transform: none;
}

@media (prefers-reduced-motion: reduce) {
  [data-reveal] {
    opacity: 1;
    transform: none;
    transition: none;
  }
}
```

## Scroll-driven CSS

```css
@supports (animation-timeline: view()) {
  .reveal {
    animation: reveal linear both;
    animation-timeline: view();
    animation-range: entry 15% cover 35%;
  }

  @keyframes reveal {
    from { opacity: 0; transform: translateY(16px); }
    to { opacity: 1; transform: none; }
  }
}
```

## GSAP timeline

```js
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

const tl = gsap.timeline({
  scrollTrigger: {
    trigger: ".section",
    start: "top 80%",
    once: true
  }
});

tl.from(".section-title", { y: 24, opacity: 0, duration: 0.6 })
  .from(".section-copy", { y: 12, opacity: 0, duration: 0.4 }, "-=0.3")
  .from(".section-cta", { y: 8, opacity: 0, duration: 0.3 }, "-=0.2");
```

## Counter

```jsx
import { animate, useMotionValue, useTransform, motion } from "motion/react";
import { useEffect } from "react";

function Counter({ value }) {
  const count = useMotionValue(0);
  const rounded = useTransform(count, (v) => Math.round(v).toLocaleString());

  useEffect(() => {
    const controls = animate(count, value, { duration: 0.6, ease: "easeOut" });
    return controls.stop;
  }, [value]);

  return <motion.span>{rounded}</motion.span>;
}
```

## Text reveal

```css
.line {
  display: block;
  overflow: hidden;
}

.line > span {
  display: block;
  transform: translateY(100%);
  transition: transform 600ms var(--ease-out);
}

.is-visible .line > span {
  transform: translateY(0);
}
```

Stagger lines with `transition-delay`. Keep the text in the DOM for search and accessibility.

## Performance checklist

- [ ] Only `transform` and `opacity` animate.
- [ ] No layout thrash.
- [ ] `will-change` is temporary.
- [ ] Offscreen animation is paused.
- [ ] The tab-hidden state is handled.
- [ ] The animation is tested on a mid-range Android.
- [ ] INP stays under 200 ms.
- [ ] CLS stays under 0.1.
- [ ] Reduced motion is respected.
