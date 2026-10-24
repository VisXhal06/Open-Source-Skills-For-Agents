---
title: Design Engineering Skills
aliases:
  - Design Suite
  - UI UX Skills
  - Frontend Design Skills
type: reference
created: 2026-10-21
updated: 2026-10-24
tags:
  - design
  - frontend
  - ui
  - ux
  - motion
  - design-systems
  - ai-workflow
  - reference
---

# Design Engineering Skills

> [!info] What this is
> A global skill suite for product design, UI/UX, visual design, interaction and motion, design systems, frontend craft, AI-assisted design, and critique. The front door is `design-engineering`; every sub-skill is directly accessible.

## The role map

| Role | Known for | Core tasks | Typical artifacts |
| --- | --- | --- | --- |
| UX researcher | Evidence over assumption | Interviews, usability tests, synthesis | Research plan, insights, journey maps |
| UX designer | Framing the problem and flow | IA, flows, wireframes, prototypes, tests | Flows, wireframes, prototypes |
| UI designer | Surface craft and clarity | Layout, type, color, spacing, states | High-fidelity screens, UI kits |
| Interaction designer | Behavior and feedback | States, transitions, gestures, microinteractions | Interaction specs, prototypes |
| Visual / brand designer | Identity and art direction | Type, color, imagery, grids, brand systems | Brand guidelines, style tiles |
| Product designer | End-to-end product thinking | Research through ship, trade-offs, metrics | Product specs, prototypes, decisions |
| Design systems designer/engineer | Scale and consistency | Tokens, components, variants, docs, governance | Design system, tokens, docs |
| Design engineer | Designing in code | Prototype, production UI, motion, performance, a11y | Shipped UI, components, prototypes |
| Frontend engineer | Reliable implementation | Architecture, state, responsive, testing | Production code, tests, budgets |
| Product engineer | Owning outcomes across the stack | Discovery, full-stack build, instrumentation | Shipped features, metrics |
| Creative developer / motion designer | Experiential craft | WebGL, shaders, 3D, scroll narratives | Immersive sites, motion systems |

The overlaps matter: product design = research + interaction + visual; design engineering = design + production code + performance + accessibility.

## The suite

| Skill | What it does |
| --- | --- |
| `design-engineering` | Front door: role map, design loop, workflow selection, orchestration |
| `design-research` | Brief, research plan, competitive audit, reference board, directions |
| `visual-ui-design` | Layout, type, color, spacing, hierarchy, responsive, dark mode, style |
| `interaction-motion` | States, microinteractions, transitions, scroll, motion systems, a11y |
| `design-systems` | Tokens, components, docs, governance, Figma/code parity, AI context |
| `frontend-craft` | Production UI, React/Next.js, Tailwind/shadcn, a11y, performance |
| `ai-design-workflow` | Context packs, Figma MCP, AI tools, guardrails, verification |
| `design-critique` | Heuristics, hierarchy, states, responsive, a11y, motion, performance |

## The workflow

**Brief → research → direction → prototype → test → build → critique → ship → measure**

The Double Diamond underneath:

| Phase | Question | Output |
| --- | --- | --- |
| Discover | What is really going on? | User evidence, constraints, competitive map |
| Define | Which problem are we solving? | Problem statement, principles, non-goals |
| Develop | What are the possible answers? | Two or three real directions |
| Deliver | What works in the world? | Tested, accessible, performant, shipped |

Source: [Design Council — The Double Diamond](https://www.designcouncil.org.uk/our-resources/the-double-diamond)

## How designers find a direction

1. Write a one-page brief: audience, job, feeling, constraints, anti-goals.
2. Audit three direct competitors and three adjacent categories.
3. Mine 20–30 references across structure, typography, color, and motion.
4. Tag every reference with **why** it works.
5. Build two or three genuinely different style tiles or moodboards.
6. Test the direction with users or stakeholders.
7. Extract principles and tokens, then build a vertical slice.

Reference pools: [Mobbin](https://mobbin.com/), [Godly](https://godly.website/), [Awwwards](https://www.awwwards.com/websites/portfolio/), [Behance](https://www.behance.net/), [Dribbble](https://dribbble.com/), [SiteInspire](https://www.siteinspire.com/), [Land-book](https://land-book.com/), [Httpster](https://httpster.net/).

The rule: **reference is not copy.** Extract the principle, not the pixels.

## How designers work with AI

AI is for divergence, speed, and coverage. Humans own taste, framing, and accountability.

| Stage | AI can do | Human owns |
| --- | --- | --- |
| Discover | Summarize, cluster, hypothesize | Research validity |
| Define | Draft frames, JTBD, personas | Choosing the problem |
| Explore | Moodboards, variants, copy | Taste and brand fit |
| Prototype | v0, Lovable, Framer AI, Figma AI | Hierarchy and interaction logic |
| Implement | Figma MCP, code agents, tokens | Architecture, a11y, performance |
| Verify | Visual diff, a11y scans, traces | Ship/no-ship judgment |

Guardrails: use existing components and tokens; no hardcoded values; no animation without reduced motion; no AI-generated UI without accessibility, responsive, and performance checks; no generic AI aesthetic; never ship code you have not read.

Source: [Figma — Design Systems and AI](https://www.figma.com/blog/design-systems-ai-mcp), [Figma AI Design System Agent](https://www.figma.com/solutions/ai-design-system-agent)

## Modern UI and motion

### Visual

- Typography carries the brand; hierarchy first.
- Color is semantic; contrast is checked.
- Layout is intentional; mobile is a composition, not a squeeze.
- Depth, texture, and glass are back, with performance discipline.
- Dark mode is a first-class theme.
- Accessibility is a design constraint.
- One memorable moment beats five competing effects.

### Motion

- Purpose: feedback, orientation, continuity, hierarchy, delight.
- Timing: most UI animation is 100–500 ms; simple feedback ≈ 100 ms; modals ≈ 200–300 ms.
- Easing: ease-out for entrances, ease-in for exits.
- Choreography: stagger 20–50 ms; lead, follow, settle.
- Properties: transform and opacity; avoid layout animation.
- Accessibility: `prefers-reduced-motion`, no scroll-jacking, no flashing.
- Performance: LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1.

Sources: [NN/g — Executing UX Animations](https://www.nngroup.com/articles/animation-duration/), [WCAG 2.2](https://www.w3.org/TR/WCAG2/), [web.dev — Web Vitals](https://web.dev/articles/vitals)

## Anti-generic aesthetics gate

A hard rule across all 11 frontend and design skills. Generic AI aesthetics are rejected as defaults, not reviewed as a matter of taste. Any banned choice must be justified by the brief, the brand, or an existing design system, and the exception is recorded.

**Banned as defaults:**

- **Type:** Inter, Roboto, Arial, Helvetica, `system-ui` / `-apple-system` / `Segoe UI` stacks; the Poppins / Montserrat / Open Sans / Lato template stack.
- **Color:** violet, indigo, or purple gradients on white; blue-to-purple "AI" gradients; gradient text; pastel mesh; glass cards on a gradient; cream + serif + terracotta; near-black + acid green.
- **Layout:** centered eyebrow-headline-two-buttons hero with a gradient blob; three identical feature cards; logo cloud; testimonial trio; pricing trio with a highlighted middle card; identical bento tiles; floating dashboard mockup; every section in a rounded card.
- **Components:** a pill badge above every heading; one radius and shadow on every surface; icon-in-rounded-square for every feature; gradient-border cards; hover-lift on every card.
- **Motion:** fade-and-slide-up on every section; stagger on every list; hover scale everywhere; looping ambient gradient.
- **Copy:** "Build faster, ship smarter", "AI-powered", "supercharge", "seamless", "unlock" without a specific claim.

**Required before implementation:**

```text
Direction: <name> — <why it belongs to this subject>
Type: <face> — <what its construction or history contributes>
Palette: <source> — <4–6 core values>
Layout: <what the structure encodes> — <what it deliberately breaks>
Signature: <the one element that could not move to another product>
Rejected: <the specific defaults this brief refuses>
```

**Enforcement:** a banned default that defines the first impression is a blocker; a localized one is a major finding. It is never a nit. Replace the idea, not the hue.

**Applied in:** `frontend-design`, `frontend-craft`, `visual-ui-design`, `design-engineering`, `design-critique`, `design-systems`, `design-research`, `ai-design-workflow`, `oss-uiux-frontend`, `web-design-guidelines`, `interaction-motion`.

**Canonical checklist:** `C:\Users\Vishal\.agents\skills\frontend-design\references\anti-generic-aesthetics.md`

## How to use it

```text
Use design-engineering to design a landing page for a developer tool.
Use design-research to find a direction for this brief.
Use visual-ui-design to define the type and color system.
Use interaction-motion to spec the page transitions.
Use design-systems to structure the tokens.
Use frontend-craft to implement this screen.
Use ai-design-workflow to brief the coding agent.
Use design-critique to review the checkout flow.
```

Or use the command:

```text
/design design a landing page for a developer tool
/design review this dashboard
/design build the token system for this app
```

## Sources

### Roles and process
- [Design Engineering at Vercel](https://vercel.com/blog/design-engineering-at-vercel)
- [The Double Diamond — Design Council](https://www.designcouncil.org.uk/our-resources/the-double-diamond)
- [UX Design Processes — IxDF](https://www.interaction-design.org/literature/topics/design-processes)
- [UX vs. UI — NN/g](https://www.nngroup.com/videos/ux-vs-ui/)
- [Atomic Design — Brad Frost](https://atomicdesign.bradfrost.com/)

### Visual
- [Refactoring UI](https://www.refactoringui.com/)
- [Laws of UX](https://lawsofux.com/)
- [Material 3](https://m3.material.io/)
- [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/)
- [Carbon](https://carbondesignsystem.com/)
- [Polaris](https://polaris.shopify.com/)
- [Primer](https://primer.style/)
- [Radix](https://www.radix-ui.com/)
- [shadcn/ui](https://ui.shadcn.com/)
- [Inclusive Components](https://inclusive-components.design/)

### Motion
- [NN/g — Executing UX Animations](https://www.nngroup.com/articles/animation-duration/)
- [NN/g — The Role of Animation and Motion in UX](https://www.nngroup.com/articles/animation-purpose-ux/)
- [Motion](https://motion.dev/docs)
- [GSAP](https://gsap.com/docs/v3/)
- [Rive](https://rive.app/)
- [Three.js](https://threejs.org/)
- [View Transitions API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)
- [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll-driven_animations)

### Accessibility and performance
- [WCAG 2.2](https://www.w3.org/TR/WCAG2/)
- [WAI — Animation from Interactions](https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions.html)
- [web.dev — Web Vitals](https://web.dev/articles/vitals)
- [web.dev — Learn Accessibility](https://web.dev/learn/accessibility/)
- [web.dev — Learn Performance](https://web.dev/learn/performance/)

### AI and systems
- [Figma — Design Systems and AI](https://www.figma.com/blog/design-systems-ai-mcp)
- [Figma AI Design System Agent](https://www.figma.com/solutions/ai-design-system-agent)
- [Figma MCP Catalog](https://www.figma.com/mcp-catalog)
- [Motion AI Kit](https://motion.dev/docs/ai-kit)

### Reference pools
- [Mobbin](https://mobbin.com/)
- [Godly](https://godly.website/)
- [Awwwards](https://www.awwwards.com/websites/portfolio/)
- [Behance](https://www.behance.net/)
- [Dribbble](https://dribbble.com/)
- [SiteInspire](https://www.siteinspire.com/)
- [Land-book](https://land-book.com/)
- [Httpster](https://httpster.net/)

## Related notes

- [[OpenCode Skills]]
- [[Senior Developer Thinking]]
- [[Senior Developer Operating System]]
- [[Goal to Execution]]
