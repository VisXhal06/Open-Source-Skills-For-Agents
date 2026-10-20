---
name: ai-design-workflow
description: "Use when using AI agents or AI tools for design, UI generation, design-to-code, Figma MCP, v0, Lovable, Framer AI, or when AI-generated UI needs guardrails, context, and verification."
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
---

# AI Design Workflow

Use AI to explore faster and cover more ground without surrendering taste, judgment, or accountability. This skill covers context packs, prompt patterns, design-to-code, Figma MCP, guardrails, and verification.

## Suite integration

Part of the design-engineering suite. `design-engineering` can load this skill automatically when the user wants to use AI for design or frontend work. Direct invocation works too. Load `design-systems` first if the project has tokens or components; load `design-critique` after generation.

## The principle

AI is an amplifier, not an authority.

| AI is good at | Humans must own |
| --- | --- |
| Generating options | Choosing the direction |
| Summarizing research | Validating the evidence |
| Producing boilerplate | Architecture and boundaries |
| Applying known patterns | Knowing when to break them |
| Auditing consistency | Judging what matters |
| Writing first drafts | Editing for truth and taste |
| Converting designs to code | Accessibility, performance, correctness |

The bottleneck is no longer generation. It is **context, taste, and verification**.

## Step 1: Build the context pack

An agent cannot infer your product, conventions, or constraints. Give it a compact, explicit pack:

```text
design/
  brief.md
  principles.md
  tokens.json
  components.json
  patterns.md
  anti-patterns.md
  examples/
    good/
    bad/
```

### Brief

- Audience.
- Job to be done.
- Feeling.
- Constraints.
- Non-goals.
- Success criteria.

### Principles

Three to five testable rules, plus anti-principles.

### Tokens

Color, type, spacing, radius, shadow, motion — with semantic names.

### Components

Component inventory, variants, states, accessibility contracts, and file paths.

### Examples

One good example and one bad example for the agent to imitate or avoid. Show, don't just tell.

### Acceptance criteria

What “done” means, including responsive, accessibility, performance, and visual checks.

## Step 2: Choose the tool for the job

| Job | Tool | What to verify |
| --- | --- | --- |
| Explore visual directions | Figma AI, Framer AI, image models | Originality, brand fit, real content |
| Generate a UI scaffold | v0, Lovable, Framer AI | Tokens, accessibility, responsive behavior |
| Convert Figma to code | Figma MCP, Code Connect | Component reuse, token fidelity, behavior |
| Build inside an existing repo | Code agent (OpenCode, Claude Code, Codex, Cursor) | Architecture, tests, edge cases |
| Generate motion | Motion AI Kit, code agent | Timing, reduced motion, performance |
| Audit a design system | Figma AI, code agent | False positives, real usage |
| Review a UI | Screenshot + critique prompt | Human taste, evidence |

Tools change. The workflow does not.

## Step 3: Prompt patterns

### Art direction

```text
You are a senior visual designer. Use the attached brief, principles, and tokens.
Propose three genuinely different directions. For each: concept, palette, type,
layout, motion idea, risk, and what it deliberately avoids. Do not use generic
SaaS hero patterns. Do not use the default AI aesthetic (cream + serif +
terracotta, near-black + acid green, identical rounded cards). Ask for missing
information before generating.
```

### Component generation

```text
Build a [component] for [product]. Use only the existing tokens and primitives
in the attached manifest. Match the existing API and naming. Include variants,
sizes, states, keyboard behavior, focus management, and a reduced-motion path.
Do not introduce a new dependency. Show the diff and the tests.
```

### Design-to-code

```text
Use the Figma MCP context for this frame. Reuse existing components and tokens.
Do not hardcode colors, spacing, or type. Preserve the hierarchy and responsive
behavior. List any design gaps you had to fill. Add a visual check and an
accessibility check.
```

### Critique

```text
Review this screen as a senior design engineer. Separate evidence from taste.
Check hierarchy, states, responsive behavior, keyboard, contrast, motion,
performance, and design-system consistency. Rank findings by severity. Do not
praise by default. Propose the smallest fix for each.
```

### Motion

```text
Spec the motion for this interaction. Define trigger, elements, properties,
from/to, duration, delay, easing, interruption, reduced-motion fallback, and
performance notes. Use transform/opacity only. No scroll-jacking. No animation
without a purpose.
```

### Copy

```text
Write interface copy in the product's voice. Name things by what users
understand, not how the system is built. Use active voice. Make CTAs specific.
Do not use generic SaaS claims, exclamation marks, or filler. Give five options
and explain the trade-off in each.
```

## Step 4: Figma MCP and design-to-code

Figma’s MCP server brings design context into the IDE. It can provide components, styles, and variables to an AI agent, and can generate a structured rules file covering token definitions, component libraries, style hierarchies, and naming conventions. Figma’s design-system agent uses real tokens, variables, and styles rather than placeholders, and can generate components and audit consistency.

Sources: [Figma — Design Systems and AI](https://www.figma.com/blog/design-systems-ai-mcp), [Figma AI Design System Agent](https://www.figma.com/solutions/ai-design-system-agent)

A practical loop:

1. Select the frame or component in Figma.
2. Give the agent the MCP context and the `DESIGN.md` / token manifest.
3. Ask it to reuse existing components first.
4. Generate the smallest vertical slice.
5. Review the diff, not just the screenshot.
6. Run visual, accessibility, and performance checks.
7. Feed the gaps back into the system, not into a one-off override.

## Step 5: Guardrails

### Non-negotiables

- Use existing components before creating new ones.
- Use semantic tokens, never raw hex or arbitrary pixel values.
- Match the existing API and naming.
- Preserve keyboard and screen reader behavior.
- Add a reduced-motion path for every animation.
- Do not introduce a dependency without approval.
- Do not invent content, metrics, or testimonials.
- Do not ship code you have not read.
- Do not accept a design you cannot explain.
- Do not ship a banned generic default as a default. If the brief or system requires one, record the exception.

### Anti-slop rules

Reject or revise:

- **Type:** Inter, Roboto, Arial, Helvetica, and `system-ui` stacks; the Poppins / Montserrat / Open Sans / Lato stack.
- **Color:** violet, indigo, or purple gradients on white; blue-to-purple "AI" gradients; gradient text; pastel mesh; glass cards on a gradient; the cream + serif + terracotta default; near-black + acid green.
- **Layout:** the centered badge-headline-two-buttons hero; three identical feature cards; a logo cloud; a testimonial trio; a pricing trio with a highlighted middle card; identical bento tiles; a floating dashboard mockup; every section in a rounded card.
- **Components:** a pill badge above every heading; one radius and shadow everywhere; an icon in a rounded square for every feature; gradient-border cards; hover-lift everywhere.
- **Motion:** fade-and-slide-up on every section; stagger on every list; hover scale everywhere; a looping ambient gradient.
- **Copy and imagery:** "Build faster, ship smarter", "AI-powered", "supercharge", "seamless", "unlock" without a claim; generic 3D blobs; stock team photography; AI imagery with no art direction.

These are defaults to avoid, not forever bans. A banned default may be used only when the brief or the existing system explicitly requires it; record the exception. Recoloring is not a revision.

Before generating, require the six-line design record: direction, type rationale, palette source, layout logic, signature element, rejected defaults.

## Step 6: Verify

AI output is a draft, not evidence.

### Visual

- Screenshot at 320, 768, 1440.
- Compare against the design at the same viewport.
- Check spacing, type, color, radius, shadows, icons.
- Check dark mode.
- Check long content.
- Check all states.
- Run the anti-generic audit: name the direction, the type rationale, the palette source, the signature element, and the banned defaults rejected. If any first-impression element is a banned default, stop and fix the direction.

### Accessibility

- Keyboard walkthrough.
- Focus visible and logical.
- Screen reader flow.
- Contrast.
- Target size.
- Reduced motion.
- Zoom 200%.

### Performance

- LCP ≤ 2.5 s.
- INP ≤ 200 ms.
- CLS ≤ 0.1.
- Bundle size.
- Client/server boundaries.
- Image and font optimization.

### Code

- Read the diff.
- Check architecture and boundaries.
- Check error handling.
- Check tests.
- Check dependency changes.
- Check for secrets and unsafe input.

### Content

- Is it true?
- Is it specific?
- Is it in the product's voice?
- Does it explain what happens next?

## Step 7: Handoff

When handing work to another agent or human, include:

- Outcome and scope.
- Context pack paths.
- Files to touch and files to avoid.
- Acceptance criteria.
- Verification commands.
- Known gaps.
- What not to change.

Use `templates/design-agent-task.md`.

## Common failure modes

| Failure | Why it happens | Fix |
| --- | --- | --- |
| Generic layout | No brief or subject context | Give the brief and anti-goals |
| Token drift | No token manifest | Provide tokens and forbid raw values |
| Component duplication | No inventory | Provide component manifest and reuse rule |
| Inaccessible UI | No a11y constraints | Make a11y part of acceptance |
| Janky motion | No motion spec | Require timing, easing, reduced motion |
| Brittle code | Agent optimized for demo | Require tests, error states, review |
| Hallucinated content | Model fills gaps | Require real content or placeholders labeled |
| False confidence | Agent says “done” | Run verification yourself |

## Quality bar

- [ ] The context pack exists and is current.
- [ ] The agent knows the brief, principles, tokens, and components.
- [ ] The output reuses the system.
- [ ] The diff was read.
- [ ] The anti-generic gate passed; no banned default defines the first impression.
- [ ] Type, palette, and layout have a stated rationale tied to the subject.
- [ ] Visual QA was run.
- [ ] Accessibility was checked.
- [ ] Performance was measured.
- [ ] Content is true and specific.
- [ ] The human can explain every decision.
- [ ] The next action is clear.

## Related skills

- `design-engineering` for the full workflow.
- `design-research` for the brief.
- `design-systems` for tokens and manifests.
- `frontend-craft` for implementation.
- `design-critique` for review.
- `agent-delegation` and `subagents` for multi-agent work.
- `verification-before-completion` for evidence.

## References

- `references/agent-guardrails.md` — rules and failure modes.
- `templates/ai-design-brief.md` — context pack.
- `templates/design-agent-task.md` — task packet.
