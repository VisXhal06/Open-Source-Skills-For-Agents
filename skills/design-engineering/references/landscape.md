# Design and Frontend Landscape

A practical map of the disciplines, reference pools, and working methods behind the design-engineering suite. Use it to choose a direction, not to copy one.

## 1. The disciplines

| Discipline | Core question | What it owns | What it does not own |
| --- | --- | --- | --- |
| UX research | What do people actually need? | Evidence, behavior, needs, context | Visual style, final UI |
| UX design | How should the experience flow? | Information architecture, flows, structure | Brand expression, production code |
| UI design | How should the surface look and read? | Layout, type, color, spacing, states | Research validity, system architecture |
| Interaction design | How should it behave? | States, feedback, gestures, transitions | Visual identity, backend |
| Visual / brand design | What should it feel like? | Art direction, type, color, imagery | Product flow, implementation |
| Product design | What should we build and why? | End-to-end product decisions | Deep infrastructure |
| Design systems | How does it scale consistently? | Tokens, components, docs, governance | Every one-off campaign page |
| Design engineering | How do we make it real and good? | Prototypes, production UI, motion, performance, a11y | Product strategy alone |
| Frontend engineering | How do we make it reliable? | Architecture, state, testing, performance | Visual direction alone |
| Product engineering | How do we own the outcome? | Full-stack delivery, instrumentation, iteration | Specialist depth everywhere |
| Creative development | How do we make it memorable? | WebGL, shaders, 3D, scroll narratives | Everyday product UI |

The overlaps matter. Product design = research + interaction + visual. Design engineering = design + production code + performance + accessibility. A strong team does not need every title; it needs every responsibility covered.

## 2. How the work flows

### Double Diamond

| Phase | Divergent or convergent | Activities |
| --- | --- | --- |
| Discover | Divergent | Interviews, observation, competitor audit, data review |
| Define | Convergent | Problem statement, principles, non-goals, success metrics |
| Develop | Divergent | Sketches, prototypes, style tiles, tests |
| Deliver | Convergent | Build, QA, launch, measure |

The loop repeats. Delivery often reveals that the problem was framed wrong.

### The design-engineering loop

1. Brief.
2. Research and reference mining.
3. Two or three directions.
4. Interaction and state model.
5. Tokens and components.
6. Vertical slice in code.
7. Critique and verification.
8. Ship and measure.

## 3. How designers find a direction

### The brief

Before references, write:

- Audience: who is this for, and what do they already know?
- Job: what are they trying to accomplish?
- Feeling: what should the interface feel like, in three adjectives?
- Constraints: brand, accessibility, performance, platform, content, timeline.
- Anti-goals: what should this explicitly not be?
- Success: what observable change means it worked?

### Reference mining

Collect references across four axes, not one:

| Axis | What to look for | Useful sources |
| --- | --- | --- |
| Structure | Navigation, page hierarchy, density, flow | Mobbin, product teardowns, competitor audits |
| Typography | Scale, pairing, rhythm, voice | Typewolf, Google Fonts, foundry sites, editorial design |
| Color | Palette, contrast, semantic use, dark mode | Brand guidelines, accessible palette tools |
| Motion | Feedback, transitions, scroll, choreography | Motion galleries, Awwwards, Godly, studio sites |

Tag every reference with **why**. "I like this" is not a direction. "This works because the dense data table is balanced by a single oversized number and generous whitespace" is a direction.

### The three-direction method

Create two or three genuinely different directions, not three shades of the same idea:

1. **Safe/clear** — conventional, low-risk, highly usable.
2. **Brand-forward** — distinctive, expressive, memorable.
3. **Experimental** — tests a new interaction or visual idea.

For each direction, define:

- Concept in one sentence.
- Palette (4–6 named values).
- Typefaces and roles.
- Layout concept.
- Motion idea.
- Why it fits the brief.
- What it risks.

Test the direction before building the whole product. A small vertical slice beats a beautiful static mockup.

## 4. Reference pools

### Patterns and flows

- [Mobbin](https://mobbin.com/) — real product screens and flows.
- [Page Flows](https://pageflows.com/) — recorded user flows.
- [UX Archive](https://uxarchive.com/) — mobile flow references.

### Craft and portfolios

- [Godly](https://godly.website/) — daily curation of exceptional web design.
- [Awwwards](https://www.awwwards.com/) — portfolio and site awards.
- [Behance](https://www.behance.net/) — visual and brand exploration.
- [Dribbble](https://dribbble.com/) — visual exploration, not production truth.
- [SiteInspire](https://www.siteinspire.com/) — web design inspiration.
- [Land-book](https://land-book.com/) — landing page references.
- [Httpster](https://httpster.net/) — modern web design.

### Products worth studying

Linear, Vercel, Stripe, Figma, Framer, Raycast, Arc, Notion, Superhuman, Ramp, Mercury, Apple, Airbnb, Spotify, Shopify, GitHub, Duolingo.

Study them for specific decisions: onboarding, density, navigation, empty states, pricing, docs, keyboard flows, motion. Do not copy the surface.

### Studios and creative development

Active Theory, Lusion, Resn, Locomotive, Ustwo, Instrument, Pentagram, Collins, DesignStudio, Bureau Borsche, Hello Monday, Jam3, Fantasy, Basic/Dept, Work & Co, Metalab, Clay, Ramotion.

### Systems

- [Material 3](https://m3.material.io/)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Carbon](https://carbondesignsystem.com/)
- [Polaris](https://polaris.shopify.com/)
- [Primer](https://primer.style/)
- [Radix](https://www.radix-ui.com/)
- [shadcn/ui](https://ui.shadcn.com/)

### Reasoning and craft

- [Nielsen Norman Group](https://www.nngroup.com/articles/)
- [Smashing Magazine](https://www.smashingmagazine.com/)
- [A List Apart](https://alistapart.com/)
- [web.dev](https://web.dev/)
- [Josh Comeau](https://www.joshwcomeau.com/)
- [Refactoring UI](https://www.refactoringui.com/)
- [Laws of UX](https://lawsofux.com/)
- [Inclusive Components](https://inclusive-components.design/)
- [Atomic Design](https://atomicdesign.bradfrost.com/)

## 5. How designers use AI

### Good uses

- Summarize and cluster research.
- Generate reference boards and moodboards.
- Explore copy and layout variants.
- Generate component scaffolds from tokens.
- Convert Figma context to code with MCP.
- Audit consistency, contrast, and missing states.
- Generate visual regression tests.
- Draft accessibility and performance checks.

### Bad uses

- Asking AI to choose the brand direction without a brief.
- Accepting generic layouts because they look polished.
- Letting AI invent components outside the design system.
- Shipping AI code without reading it.
- Adding motion because the tool can.
- Replacing user research with model guesses.

### The context pack

Give the agent:

- The brief and audience.
- Design principles and anti-goals.
- Tokens: color, type, spacing, radius, shadow, motion.
- Component inventory and usage rules.
- Existing screens and code patterns.
- Accessibility and performance constraints.
- Examples of good and bad output.
- Acceptance criteria and verification commands.

## 6. Modern visual and motion signals

Treat these as signals, not defaults:

- Expressive, variable typography.
- Saturated or warm palettes with accessible contrast.
- Editorial and asymmetric layouts.
- Bento grids and modular content.
- Tactile realism: subtle gradients, texture, glass, depth.
- Motion as hierarchy and storytelling.
- Dark mode as a first-class theme.
- Accessibility as a creative constraint.
- AI-readable structure: tokens, schema, alt text, semantic HTML.
- Performance as part of the aesthetic.

Trends age. The brief, the audience, and the content do not.

## 7. Quality bar

- The design is specific to the subject.
- The hierarchy is obvious in three seconds.
- The content is real, not lorem ipsum.
- All states exist.
- Mobile is designed, not squeezed.
- Keyboard and screen reader paths work.
- Contrast and target sizes pass.
- Motion is purposeful and reduced-motion safe.
- LCP, INP, and CLS are within budget.
- The design system is used, not bypassed.
- The next action is clear.

## 8. Sources

See `sources.md` for the full list.
