# Agent Guardrails

## The context contract

An agent needs five things:

1. **Outcome** — what the user can do when this is done.
2. **Constraints** — what must not change, what must be used, what must be avoided.
3. **Examples** — one good and one bad reference.
4. **Acceptance criteria** — how the output will be judged.
5. **Verification** — the commands and checks that prove it.

If any of these is missing, the agent will guess. Guessing is the source of most AI slop.

## Rules to give every design agent

```text
You are working inside an existing product and design system.

Use:
- Existing components before creating new ones.
- Semantic tokens for color, type, spacing, radius, shadow, and motion.
- The existing API, naming, and file structure.
- Accessible primitives for dialogs, menus, tabs, and popovers.
- Real content or clearly labeled placeholders.

Do not:
- Hardcode colors, spacing, or type.
- Introduce a new dependency without approval.
- Invent metrics, testimonials, or product claims.
- Add animation without a purpose and a reduced-motion path.
- Use generic AI aesthetics (cream + serif + terracotta, near-black + acid green,
  identical rounded cards, all-caps eyebrows, gradient blobs).
- Ship code you have not read.

Before finishing:
- List files changed.
- List design gaps you filled.
- Run the verification commands.
- Report what passed and what failed.
```

## The design review prompt

```text
Review this UI as a senior design engineer.

Separate evidence from taste. Check:
1. Hierarchy: what does the eye see first, second, third?
2. Clarity: what is this, who is it for, what do I do next?
3. States: empty, loading, error, success, disabled, focus, hover, active.
4. Responsive: 320px, 768px, 1440px, 200% zoom.
5. Accessibility: keyboard, focus, labels, contrast, target size, reduced motion.
6. Performance: LCP, INP, CLS, bundle, images, fonts.
7. System: tokens, components, naming, consistency.
8. Content: truth, specificity, voice.
9. Originality: what is generic or templated?

Rank findings by severity. Do not praise by default. Propose the smallest fix.
```

## Common agent failure modes

| Failure | Signal | Correction |
| --- | --- | --- |
| Generic hero | Big headline, gradient, floating dashboard, no specific claim | Demand subject-specific content and a concrete first screen |
| Token drift | Hex values, arbitrary spacing | Provide token manifest; reject raw values |
| Component duplication | New Button next to existing Button | Provide inventory; require reuse |
| Accessibility regression | Div buttons, no labels, no focus | Make a11y part of acceptance |
| Motion overload | Every section fades and slides | Require a motion spec and one signature moment |
| Hallucinated content | Fake logos, metrics, testimonials | Require real content or labeled placeholders |
| Brittle code | Works in demo, fails on empty/error | Require states and tests |
| Over-abstraction | Premature generic system | Build the concrete case first |
| Dependency creep | New library for a small need | Require approval and justify |
| False completion | “Done” without evidence | Run verification yourself |

## Verification commands

Adapt to the repo:

```bash
npm run format
npm run lint
npm run typecheck
npm run test
npm run build
npm run test:e2e
npx playwright test
npx axe
npx lighthouse http://localhost:3000 --view
```

If a command does not exist, say so. Do not invent a passing result.

## Human review checklist

- [ ] I can explain the layout and hierarchy.
- [ ] I can explain the type and color choices.
- [ ] I know which components and tokens were used.
- [ ] I have read the diff.
- [ ] I have tested the happy path and the edge cases.
- [ ] I have checked keyboard and screen reader.
- [ ] I have measured performance.
- [ ] I have removed anything I cannot justify.
