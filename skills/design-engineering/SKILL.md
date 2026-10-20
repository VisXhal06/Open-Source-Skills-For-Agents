---
name: design-engineering
description: "Use when designing or building any UI, frontend, product interface, design system, or motion experience; when the user asks for a modern, stylish, accessible interface, a design critique, or wants to work like a product designer, UI/UX designer, design engineer, or frontend engineer."
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
---

# Design Engineering

This is the front door to the design-engineering suite. It encodes how product designers, UI/UX designers, design engineers, and frontend engineers actually work, then loads the right sub-skill or sub-skills automatically. You do not need to name a sub-skill. Every sub-skill is also directly accessible.

## The contract

When this skill is invoked:

1. **Classify the request.** Is this discovery, visual direction, interaction/motion, a design system, production frontend, AI-assisted design, or critique?
2. **Load the relevant sub-skill or sub-skills.** Read their `SKILL.md` files before acting. Use `references/landscape.md` for the role and reference map.
3. **State the modes you are using** in one line, for example: "Using `design-research` to find a direction, then `visual-ui-design` to define the system."
4. **Do the work, not just the routing.** Never reply "use the X skill" and stop. If X is the right skill, load it and execute its workflow.
5. **Produce the artifact and the evidence.** A brief, reference board, style tile, UI spec, motion spec, component spec, implementation, or critique. Show what you checked.
6. **Leave a clear next action.** The user should know what to do next without re-reading the whole session.

A routing table is not a deliverable. If the request is real work, read the first selected sub-skill and begin its workflow before replying. Classification-only is acceptable only when the user explicitly asks which skill to use.

## How design work actually happens

Design is not a straight line from brief to beautiful screen. It is a loop:

**Brief → research → direction → prototype → test → build → critique → ship → measure → refine**

The common backbone is the Double Diamond:

| Phase | Question | What good looks like |
| --- | --- | --- |
| Discover | What is really going on? | User evidence, business constraints, competitive map |
| Define | Which problem are we solving? | A sharp problem statement and non-goals |
| Develop | What are the possible answers? | Several real directions, not one safe default |
| Deliver | What works in the world? | Tested, accessible, performant, shipped |

Source: [Design Council — The Double Diamond](https://www.designcouncil.org.uk/our-resources/the-double-diamond)

The senior move is to spend disproportionate time on **problem framing** and **taste calibration** before high-fidelity UI. Design engineers collapse the design/build boundary: the prototype is often production code, or close to it. Vercel describes design engineers as people who blend aesthetic sensibility with technical skills and can design in Figma, design in code, write production code, debug performance, and care about page speed, cross-browser support, inclusive input modes, user preferences, and assistive technology.

Source: [Design Engineering at Vercel](https://vercel.com/blog/design-engineering-at-vercel)

## The role map

| Role | Known for | Core tasks | Typical artifacts |
| --- | --- | --- | --- |
| UX researcher | Evidence over assumption | Interviews, usability tests, synthesis | Research plan, insights, journey maps |
| UX designer | Framing the problem and flow | IA, flows, wireframes, prototypes, tests | Flows, wireframes, prototypes |
| UI designer | Surface craft and clarity | Layout, type, color, spacing, states | High-fidelity screens, UI kits |
| Interaction designer | Behavior and feedback | States, transitions, gestures, microinteractions | Interaction specs, prototypes |
| Visual / brand designer | Identity and art direction | Type, color, imagery, grids, brand systems | Brand guidelines, style tiles |
| Product designer | End-to-end product thinking | Research through ship, trade-offs, metrics | Product specs, prototypes, decision records |
| Design systems designer/engineer | Scale and consistency | Tokens, components, variants, docs, governance | Design system, tokens, docs |
| Design engineer | Designing in code | Prototype, build production UI, motion, performance, a11y | Shipped UI, components, interactive prototypes |
| Frontend engineer | Reliable implementation | Architecture, state, responsive, testing, cross-browser | Production code, tests, performance budgets |
| Product engineer | Owning outcomes across the stack | Discovery, full-stack build, instrumentation | Shipped features, metrics |
| Creative developer / motion designer | Experiential craft | WebGL, shaders, 3D, scroll narratives, motion systems | Immersive sites, motion systems |

## Load, don't route

When the user asks for help, load the smallest useful set of sub-skills and execute. Do not make them remember names.

| Request pattern | Load | Artifact |
| --- | --- | --- |
| "Find the design direction", "what should this look like", "moodboard", "competitor audit" | `design-research` | Brief, reference board, 2–3 directions |
| "Design the UI", "make it modern", "layout", "typography", "color", "style" | `visual-ui-design` | Visual direction, UI spec, token draft |
| "Make it feel alive", "animation", "microinteraction", "page transition", "scroll" | `interaction-motion` | Interaction spec, motion tokens, timeline |
| "Build a design system", "tokens", "component library", "Figma to code" | `design-systems` | Token architecture, component spec, docs |
| "Build this UI", "make it responsive", "fix the frontend", "performance", "accessibility" | `frontend-craft` | Production UI, QA report |
| "Use AI to design/build this", "Figma MCP", "v0", "Lovable", "Framer AI" | `ai-design-workflow` | Context pack, agent brief, verification |
| "Review my UI", "critique", "why does this feel off", "audit" | `design-critique` | Prioritized findings, fix plan |
| "I have an idea", "new product", "new feature" | `design-engineering` + `design-research` | Brief, direction, first slice |

### Access rules

- Any sub-skill can be invoked directly. The router is the default, not a gate.
- The router may compose several sub-skills. Read them in workflow order.
- If two skills conflict, prefer the one that reduces the most user or delivery risk for the current stage, and say why.
- If a sub-skill is not available, use the closest available skill and state the substitution.
- Never claim a sub-skill was used if you did not read it.
- Never stop at "use X." Load X and do the work.
- If the request is small, use one skill. Do not perform the whole lifecycle.

## Default workflow for a new interface

1. **Brief.** Audience, job, feeling, constraints, anti-goals. Use `templates/design-brief.md`.
2. **Research.** Audit competitors, mine references, write down why. Load `design-research`.
3. **Direction.** Create two or three contrasting style tiles or moodboards. Choose one and name the principles.
4. **Interaction.** Define the states, feedback, and motion before polishing pixels. Load `interaction-motion`.
5. **System.** Turn the direction into tokens and components. Load `design-systems`.
6. **Build.** Implement a vertical slice in code, not a pile of static screens. Load `frontend-craft`.
7. **Critique.** Review hierarchy, accessibility, responsiveness, performance, and motion. Load `design-critique`.
8. **Ship and measure.** Check real devices, real content, real network conditions.

## How designers find a direction

The disciplined process is not "browse Dribbble until inspired." It is:

1. Write a one-page brief.
2. Audit three direct competitors and three adjacent categories.
3. Mine references across four axes: structure, typography, color, motion.
4. Tag every reference with **why** it is relevant.
5. Build two or three contrasting directions.
6. Test the direction with users or stakeholders.
7. Extract principles and tokens, then build a vertical slice.

Reference pools:

- **Patterns and flows:** [Mobbin](https://mobbin.com/)
- **Craft and portfolios:** [Godly](https://godly.website/), [Awwwards](https://www.awwwards.com/websites/portfolio/)
- **Visual exploration:** [Behance](https://www.behance.net/), [Dribbble](https://dribbble.com/)
- **System constraints:** [Material 3](https://m3.material.io/), [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [Carbon](https://carbondesignsystem.com/), [Polaris](https://polaris.shopify.com/), [Primer](https://primer.style/), [Radix](https://www.radix-ui.com/), [shadcn/ui](https://ui.shadcn.com/)
- **Reasoning and craft:** [NN/g](https://www.nngroup.com/articles/), [Smashing Magazine](https://www.smashingmagazine.com/), [A List Apart](https://alistapart.com/), [web.dev](https://web.dev/), [Josh Comeau](https://www.joshwcomeau.com/), [Refactoring UI](https://www.refactoringui.com/), [Laws of UX](https://lawsofux.com/), [Inclusive Components](https://inclusive-components.design/)

The rule: **reference is not copy.** Extract the principle, not the pixels, and check whether it fits the brief.

## Modern UI and motion: the quality bar

### Visual

- Typography carries the brand. Use expressive type with a clear hierarchy and accessible sizing.
- No generic AI aesthetic. Inter, Roboto, Arial, Helvetica, and system stacks are not a type direction; violet-on-white and blue-to-purple gradients are not a palette; the centered badge-headline-two-buttons hero, three identical feature cards, a pricing trio with a highlighted middle card, identical bento tiles, and one-radius-and-shadow-everywhere are not a layout. Name the direction, the type rationale, the palette source, and one signature element before building. Full gate: load `frontend-design` and read `references/anti-generic-aesthetics.md`.
- Color is semantic, not decorative. Tokens first; contrast checked.
- Layout is intentional. Bento, editorial grids, asymmetry, and whitespace are valid if they survive mobile and CLS.
- Depth is back: subtle gradients, glass, texture, tactile realism — with performance and contrast discipline.
- Dark mode uses semantic tokens so one switch flips everything.
- Accessibility is a design constraint, not a QA afterthought.

### Motion

- **Purpose first.** Feedback, orientation, continuity, hierarchy, delight. If it does none of these, cut it.
- **Timing.** Most UI animation is 100–500 ms. Simple feedback ≈ 100 ms; modals and entrances ≈ 200–300 ms; 500 ms starts to feel slow. Entrance often needs slightly longer than exit.
- **Easing.** Ease-out for entrances, ease-in for exits. Linear motion usually feels mechanical.
- **Choreography.** Stagger, overlap, and sequence. Animate one thing at a time when possible.
- **Properties.** Prefer `transform` and `opacity`; avoid layout-triggering properties.
- **Accessibility.** Honor `prefers-reduced-motion`; avoid scroll-jacking, parallax nausea, and flashing.
- **Performance.** Motion must not destroy Core Web Vitals. Targets: LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 at the 75th percentile.

Sources: [NN/g — Executing UX Animations](https://www.nngroup.com/articles/animation-duration/), [WCAG 2.2](https://www.w3.org/TR/WCAG2/), [web.dev — Web Vitals](https://web.dev/articles/vitals)

## Working with AI agents

AI is for divergence, speed, and coverage. Humans own taste, framing, and accountability.

| Stage | AI can do | Human still owns |
| --- | --- | --- |
| Discover | Summarize interviews, cluster themes, generate hypotheses | Research validity and what matters |
| Define | Draft problem frames, JTBD, personas | Choosing the real problem |
| Explore | Moodboards, variants, copy, layout directions | Taste, distinctiveness, brand fit |
| Prototype | v0, Lovable, Framer AI, Figma AI, code agents | Hierarchy, interaction logic, edge cases |
| Implement | Figma MCP → code, token application, component generation | Architecture, accessibility, performance, correctness |
| Verify | Visual diff, a11y scans, performance traces, test generation | Ship/no-ship judgment |

The guardrails that matter: no hardcoded tokens when tokens exist; no new component when a primitive fits; no animation without a reduced-motion path; no AI-generated UI without accessibility, responsive, and performance checks; no generic AI aesthetic. Load `ai-design-workflow` for the full workflow.

## Decision rules

- **No brief?** Do not start with high-fidelity UI. Load `design-research` and write the brief.
- **No direction?** Do not polish one option. Create two or three real alternatives.
- **No states?** The design is not done. Define empty, loading, error, success, disabled, focus, hover, and active.
- **No mobile?** The design is not done. Check the smallest viewport and real content.
- **No keyboard path?** The design is not accessible. Fix it before visual polish.
- **No motion purpose?** Cut the motion.
- **No performance budget?** Do not add heavy media, WebGL, or scroll effects without one.
- **AI says "done"?** Run the verification yourself.
- **The design feels generic?** Go back to the brief and the subject matter, not to another trend.
- **It is a banned default?** Replace the idea, not the hue. Recoloring a template is still the same template.

## Anti-patterns

| Pattern | Why it hurts | Replace with |
| --- | --- | --- |
| Trend collage | Looks current for a month, communicates nothing | Subject-driven direction |
| High-fidelity too early | Polishes the wrong problem | Brief, references, low-fidelity options |
| Design by committee | Averages away the point of view | One owner, explicit principles |
| Handoff wall | Details lost between design and code | Design in code or pair closely |
| Decoration without purpose | Noise, cognitive load | Space, hierarchy, one memorable moment |
| Motion everywhere | Distracting, inaccessible, slow | Purposeful motion with a reduced-motion path |
| AI slop | Generic layouts, hardcoded tokens, inaccessible UI | Context, constraints, review, verification |
| Generic defaults treated as taste | Inter, purple-on-white, template hero, identical cards | Named direction, type rationale, palette source, signature element |
| Accessibility at the end | Expensive rework | Constraints from the first sketch |
| Desktop-only | Broken mobile experience | Responsive from the first wireframe |
| No real content | Layout collapses with real copy | Design with real content early |

## Quality bar

Before calling the work done:

- [ ] The brief states audience, job, feeling, constraints, and non-goals.
- [ ] The direction is specific to the subject, not a generic default.
- [ ] Anti-generic gate passed: no banned type stack, palette, layout, or component kit.
- [ ] Type, palette, and layout rationales are written, not implied.
- [ ] At least two real directions were considered.
- [ ] All states are designed: empty, loading, error, success, disabled, focus, hover, active.
- [ ] Mobile, tablet, and desktop were checked with real content.
- [ ] Keyboard, screen reader, contrast, and reduced motion were checked.
- [ ] LCP, INP, and CLS were measured or budgeted.
- [ ] The design system or tokens were used, not bypassed.
- [ ] Motion has a purpose, a spec, and a reduced-motion fallback.
- [ ] The next action is clear.

## Suite integration

This skill is the router for the design-engineering suite. It can load:

- `design-research` — discovery, competitive audit, references, direction.
- `visual-ui-design` — layout, typography, color, hierarchy, style.
- `interaction-motion` — states, microinteractions, animation, motion systems.
- `design-systems` — tokens, components, docs, Figma/code parity.
- `frontend-craft` — production implementation, responsive, accessibility, performance.
- `ai-design-workflow` — AI agents, Figma MCP, design-to-code, guardrails.
- `design-critique` — review, findings, fix plan.

It also composes with existing global skills:

- `frontend-design` for distinctive aesthetic risk and anti-templated choices.
- `web-design-guidelines` for rule-based UI review.
- `vercel-react-best-practices` and `vercel-composition-patterns` for React/Next.js.
- `web-perf` for performance diagnosis.
- `apple-hig` for iOS/iPadOS.
- `agent-delegation` and `subagents` for delegating design/build work.
- `senior-dev-os` for project-level judgment.

## How to use it

Front door:

```text
Use design-engineering to design a landing page for a developer tool.
Use design-engineering to review this dashboard.
Use design-engineering to build a design system for this app.
```

Direct access:

```text
Use design-research to find a visual direction for this brief.
Use visual-ui-design to define the type and color system.
Use interaction-motion to spec the page transitions.
Use design-systems to structure the tokens.
Use frontend-craft to implement this screen.
Use ai-design-workflow to brief the coding agent.
Use design-critique to review the checkout flow.
```

## References

- `references/landscape.md` — role map, reference pools, exemplars, and how designers work.
- `references/sources.md` — primary sources and further reading.
- `templates/design-brief.md` — one-page brief.
