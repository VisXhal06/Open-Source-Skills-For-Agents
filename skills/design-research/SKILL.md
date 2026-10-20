---
name: design-research
description: "Use when you need to find a design direction, audit competitors, build a moodboard or reference board, choose a visual style, or understand user needs before designing a UI, brand, or product experience."
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
---

# Design Research

Find the right problem and the right direction before polishing pixels. This skill covers user research, competitive audits, reference mining, moodboards, style tiles, and direction selection.

## Suite integration

Part of the design-engineering suite. `design-engineering` can load this skill automatically when the user asks what something should look like or needs a direction. Direct invocation works too. If the router loaded it, read the existing brief or product context first.

## What this produces

| Artifact | Purpose |
| --- | --- |
| Design brief | Audience, job, feeling, constraints, non-goals |
| Research plan | Questions, methods, evidence, participants |
| Competitive audit | Conventions, gaps, opportunities |
| Reference board | Tagged references across structure, type, color, motion |
| Three directions | Contrasting style tiles or moodboards |
| Direction decision | Chosen direction, principles, risks, next step |

## Step 1: Write the brief

Ask at most five questions:

1. Who is this for, and what do they already know?
2. What job are they trying to do?
3. What should it feel like, in three adjectives?
4. What constraints are real: brand, accessibility, performance, platform, content, timeline?
5. What should it explicitly not be?

If the user cannot answer, propose a default and label it as an assumption. Do not stall.

## Step 2: Choose the research mode

Not every project needs the same research. Match the method to the uncertainty.

| Uncertainty | Method | Output |
| --- | --- | --- |
| We do not understand users | Interviews, observation, diary study | Needs, language, workarounds |
| We do not know if it is usable | Usability test, task-based test | Friction points, severity |
| We do not know the market | Competitive audit, adjacent category scan | Conventions, gaps, differentiation |
| We do not know the visual direction | Reference mining, style tiles | Two or three directions |
| We do not know the content | Content audit, card sort, tree test | Structure, labels, priorities |
| We do not know if it works | Prototype test, analytics, A/B test | Evidence, decision |

### Research plan

Write:

- Decision this research will inform.
- Questions.
- Methods.
- Participants or sources.
- What counts as evidence.
- What would change your mind.
- Timeline and owner.

Do not run research without a decision attached. "Learn more" is not a decision.

## Step 3: Competitive audit

Audit three groups:

1. **Direct competitors** — same job, same audience.
2. **Adjacent categories** — different product, similar interaction or emotion.
3. **Aspirational references** — best-in-class craft, not necessarily same market.

For each, capture:

| Dimension | Questions |
| --- | --- |
| Positioning | What promise is on the first screen? |
| Structure | How is the page or flow organized? |
| Navigation | How do users find things? |
| Content | What is said, in what order, in what voice? |
| Visual | Type, color, spacing, imagery, density |
| Interaction | States, feedback, motion, keyboard |
| Trust | Proof, pricing, security, social evidence |
| Gaps | What is missing, confusing, or generic? |

The output is not a feature list. It is a map of **conventions to respect** and **gaps to exploit**.

## Step 4: Mine references

Collect 20–30 references, not 3. Tag each one across four axes:

| Axis | What to extract |
| --- | --- |
| Structure | Layout, hierarchy, density, flow, navigation |
| Typography | Scale, pairing, rhythm, voice, texture |
| Color | Palette, contrast, semantic use, dark mode |
| Motion | Feedback, transitions, scroll, choreography |

For every reference, write **why**:

- What specifically works?
- Why does it fit this brief?
- What should we not copy?
- What principle can we reuse?

"Looks good" is not a finding. "The dense table works because the only saturated color is reserved for the primary action" is a finding.

### Reference pools

- **Patterns and flows:** [Mobbin](https://mobbin.com/), [Page Flows](https://pageflows.com/), [UX Archive](https://uxarchive.com/)
- **Craft and portfolios:** [Godly](https://godly.website/), [Awwwards](https://www.awwwards.com/websites/portfolio/)
- **Visual exploration:** [Behance](https://www.behance.net/), [Dribbble](https://dribbble.com/)
- **Landing pages:** [Land-book](https://land-book.com/), [SiteInspire](https://www.siteinspire.com/), [Httpster](https://httpster.net/)
- **Systems:** [Material 3](https://m3.material.io/), [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [Carbon](https://carbondesignsystem.com/), [Polaris](https://polaris.shopify.com/), [Primer](https://primer.style/), [Radix](https://www.radix-ui.com/), [shadcn/ui](https://ui.shadcn.com/)

### Avoid copying

- Change the content, audience, and constraints; if the reference only works with its original content, it is not a direction.
- Extract the principle, not the pixels: "reserve saturated color for one action," not "use this hex and this layout."
- Check whether the reference is production-quality or a concept shot. Dribbble is for exploration, not proof.
- Name what you are deliberately rejecting. A direction is defined by its exclusions.

### Anti-generic gate: banned defaults are not references

Some references are so common that collecting them produces a template. Tag these as **reject**, not inspiration:

- Inter, Roboto, Arial, Helvetica, or a system stack used without a subject-specific reason.
- Violet, indigo, or purple on white; blue-to-purple "AI" gradients; gradient text; pastel mesh.
- The centered badge-headline-two-buttons hero; three identical feature cards; a logo cloud; a testimonial trio; a pricing trio with a highlighted middle card; identical bento tiles; a floating dashboard mockup.
- One radius and shadow everywhere; a pill badge above every heading; an icon in a rounded square for every feature.

When a competitor uses a default, say what it costs them: "this reads as every other AI tool, so the product's difference is invisible." Do not extract it as a principle.

## Step 5: Synthesize

Turn raw references into a point of view:

- **Insights:** what did we learn that we did not know?
- **Tensions:** what competing needs must be balanced? (dense vs. calm, premium vs. approachable, fast vs. thorough)
- **Principles:** three to five rules that will guide decisions.
- **Opportunity:** where can this product be meaningfully different?
- **Anti-principles:** what we will not do.

A good principle is testable: "Every screen has one primary action" is better than "make it clean."

## Step 6: Create two or three directions

Each direction must be genuinely different. Do not create three shades of the same idea.

For each direction:

| Element | What to define |
| --- | --- |
| Concept | One sentence that captures the idea |
| Audience fit | Why this fits the people and the job |
| Palette | 4–6 named values, with contrast notes |
| Typography | Typefaces, roles, scale, voice |
| Layout | Grid, density, alignment, hierarchy |
| Imagery | Photography, illustration, 3D, texture, none |
| Motion | One signature moment and its purpose |
| Risk | What could fail, and how to test it |
| Anti-pattern | What this direction deliberately avoids |
| Rejected defaults | The specific generic defaults this direction refuses |

Present them as style tiles or moodboards, not full screens. The goal is to choose a direction cheaply.

## Step 7: Test and choose

Choose against criteria, not loudest opinion:

- Fits the brief and audience.
- Distinctive without being confusing.
- Works with real content.
- Survives mobile, dark mode, and accessibility.
- Can be implemented within the constraints.
- Has a clear motion and interaction idea.
- The team can explain it in one sentence.

Test with five people if possible. Ask:

- What do you think this product is?
- Who is it for?
- What would you do first?
- What feels untrustworthy or confusing?
- Which direction feels most like the promise?

Then decide. Record the choice, the reasons, and what would reopen it.

## Step 8: Hand off

Give the next skill:

- The brief.
- The chosen direction and principles.
- The reference board with "why" notes.
- The anti-goals.
- The open questions.
- The constraints and success criteria.

Then load `visual-ui-design` to turn the direction into a visual system, or `interaction-motion` if behavior is the main uncertainty.

## Working with AI

Use AI to widen the search, not to make the decision.

| Task | Prompt pattern | Human check |
| --- | --- | --- |
| Cluster research | "Group these notes by need, tension, and workaround; quote the evidence." | Verify quotes and sample bias |
| Competitive scan | "Compare these three competitors on positioning, structure, trust, and visual voice." | Open the actual pages |
| Reference board | "Generate 20 references across editorial, technical, warm, and brutalist directions; explain the principle in each." | Check that references exist and fit |
| Style tiles | "Create three contrasting directions for this brief; include palette, type, layout, motion, and risk." | Choose and edit; do not ship the first output |
| Copy | "Write five headline directions in this voice; no generic SaaS claims." | Edit for truth and specificity |
| Critique | "What is generic here? What would a senior designer cut?" | Judge with taste |

AI does not replace user evidence. A model's guess about users is not research.

## Common mistakes

| Mistake | Consequence | Fix |
| --- | --- | --- |
| Starting with references | The direction is a collage, not a solution | Write the brief first |
| Three identical directions | No real choice | Force contrasting concepts |
| Copying a competitor | Undifferentiated, possibly wrong for your users | Extract principles and change the content |
| Dribbble as proof | Concept work that fails in production | Check real products and code |
| No anti-goals | Scope and style drift | Write what you will not do |
| Research without a decision | Endless discovery | Tie every method to a decision |
| Choosing by loudest voice | Politics over fit | Define criteria before review |
| Skipping the test | Expensive direction error | Test a small slice |
| A direction that is a banned default | Looks generated; no point of view | Rework type, palette, and layout from the subject |
| Recoloring a template | Same template, new paint | Change the concept, not the hue |
| Collecting defaults as references | The board becomes a mood of the industry | Tag defaults as reject and name the cost |

## Quality bar

- [ ] The brief is one page and specific.
- [ ] The research method matches the uncertainty.
- [ ] The competitive audit covers direct, adjacent, and aspirational references.
- [ ] References are tagged with why, not just collected.
- [ ] Two or three genuinely different directions exist.
- [ ] The chosen direction names the generic defaults it rejects.
- [ ] The type, palette, and layout are traceable to the subject, not to a trend.
- [ ] The chosen direction has principles and anti-principles.
- [ ] The direction works with real content.
- [ ] The next skill has what it needs.

## Related skills

- `design-engineering` for the full workflow.
- `visual-ui-design` to turn the direction into a visual system.
- `interaction-motion` when behavior is the main uncertainty.
- `design-critique` to review the direction.
- `frontend-design` for distinctive aesthetic risk.
- `research` for deeper, cited research when the question is broader than design.

## References

- `references/reference-pools.md` — curated sources and what to use each for.
- `templates/research-plan.md` — research plan.
- `templates/reference-board.md` — tagged reference board.
- `templates/direction-review.md` — direction comparison and decision.
