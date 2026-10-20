---
name: design-critique
description: "Use when reviewing a UI, page, component, design system, or animation for quality, usability, accessibility, visual hierarchy, responsiveness, performance, design-system consistency, or generic AI aesthetics."
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
---

# Design Critique

Review design with evidence, not vibes. This skill covers heuristic review, visual hierarchy, usability, accessibility, responsiveness, motion, performance, content, and design-system consistency.

## Suite integration

Part of the design-engineering suite. `design-engineering` can load this skill automatically when the user asks for a review or says something feels off. Direct invocation works too. Load `web-design-guidelines` for rule-based UI checks and `web-perf` for deep performance work.

## The stance

A critique is not a list of opinions. It is:

1. **Describe** what is there.
2. **Assess** against a standard or the brief.
3. **Recommend** the smallest fix.
4. **Prioritize** by user impact.

Separate **taste** (“I would use a serif”) from **evidence** (“body text is 3.1:1 against the background”). Both can matter, but they are not the same kind of finding.

## Step 1: Get context

Before reviewing, ask:

- Who is this for?
- What is the primary job?
- What is the design trying to feel like?
- What are the constraints?
- What is the success metric?
- What stage is this: concept, prototype, or production?

Without context, you can only review craft, not fit.

## Step 2: First impression

Look for three seconds, then answer:

- What is this?
- Who is it for?
- What is the one thing I should do?
- What do I trust or distrust?
- What feels generic or specific?

Write the first impression before analyzing. It is data.

## Step 3: Walk the primary task

Complete the main job as a user would:

1. Land on the page.
2. Understand the promise.
3. Find the next action.
4. Complete it.
5. Recover from a mistake.
6. Return later.

Note friction, ambiguity, and missing feedback. Do not review screens in isolation; review the flow.

## Step 4: Heuristic review

| Heuristic | Questions |
| --- | --- |
| Visibility of system status | Does the UI show what is happening? |
| Match with the real world | Does it use the user's language and mental model? |
| User control and freedom | Can the user undo, cancel, go back? |
| Consistency and standards | Does it follow platform and product conventions? |
| Error prevention | Does it prevent mistakes before they happen? |
| Recognition over recall | Can the user see options instead of remembering them? |
| Flexibility and efficiency | Are there shortcuts for experts and clarity for novices? |
| Aesthetic and minimalist design | Is every element earning its place? |
| Error recovery | Are errors explained and fixable? |
| Help and documentation | Is help available where it is needed? |

Source: [NN/g — 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)

## Step 5: Visual hierarchy

- Is there one primary focus per screen?
- Is the reading order obvious?
- Is type hierarchy clear at a glance?
- Is spacing doing the grouping?
- Is color used semantically, not decoratively?
- Is there one memorable moment, or five competing ones?
- Does the direction fit the subject, or could it be any SaaS?
- What can be removed?

### Anti-generic audit

A generic default is a finding even when it is polished. Check:

- **Type:** Inter, Roboto, Arial, Helvetica, a `system-ui` stack, or the Poppins / Montserrat / Open Sans / Lato stack, with no stated reason.
- **Color:** violet, indigo, or purple on white; a blue-to-purple "AI" gradient; gradient text; a pastel mesh; glass cards on a gradient.
- **Layout:** the centered badge-headline-two-buttons hero; three identical feature cards; a logo cloud; a testimonial trio; a pricing trio with a highlighted middle card; identical bento tiles; a floating dashboard mockup.
- **Components:** a pill badge above every heading; one radius and shadow everywhere; an icon in a rounded square for every feature; gradient-border cards; hover-lift on every card.
- **Motion:** fade-and-slide-up on every section; stagger on every list; a looping ambient gradient.
- **Copy:** "Build faster, ship smarter", "AI-powered", "supercharge", "seamless", "unlock" without a specific claim.

Name the pattern and the replacement. "It looks AI-generated" is not a finding. "The hero uses the centered badge-headline-two-buttons pattern and a violet-on-white gradient, so the product's only distinctive claim sits below the fold" is.

Severity: if the default defines the first impression or the brand, **Blocker**. If it is localized, **Major**. It is never a Nit.

## Step 6: States and edge cases

Check:

- Empty
- Loading
- Error
- Success
- Partial
- Disabled
- Focus
- Hover
- Active
- Long content
- No permission
- Offline
- Slow network
- Small screen
- 200% zoom

Most perceived quality lives here.

## Step 7: Responsive

- 320px: no horizontal scroll; readable; touch targets.
- 375px: common mobile.
- 768px: tablet composition.
- 1024px: small desktop.
- 1440px: desktop.
- 1920px: large screen; max width.
- Landscape mobile.
- 200% zoom.
- Large text.

Check composition, not just stacking. A mobile layout should have its own hierarchy.

## Step 8: Accessibility

- Keyboard: reachable, operable, logical order.
- Focus: visible, trapped where appropriate, restored after dialogs.
- Labels: every field has one.
- Contrast: 4.5:1 body, 3:1 large text and UI.
- Target size: 24×24 minimum, 44×44 recommended.
- Motion: reduced-motion path; no flashing; no scroll-jacking.
- Screen reader: landmarks, headings, names, live regions.
- Zoom: 200%.
- Color: not the only signal.
- Errors: announced and associated.

Sources: [WCAG 2.2](https://www.w3.org/TR/WCAG2/), [web.dev — Learn Accessibility](https://web.dev/learn/accessibility/)

## Step 9: Motion

- Does every animation have a purpose?
- Are timing and easing specified?
- Is the entrance and exit both designed?
- Is interruption handled?
- Is reduced motion implemented?
- Does it run at 60fps on a mid-range device?
- Does it block input or navigation?
- Does it cause layout shift?
- Is it scroll-jacking?

Load `interaction-motion` for depth.

## Step 10: Performance

- LCP ≤ 2.5 s.
- INP ≤ 200 ms.
- CLS ≤ 0.1.
- Hero image optimized.
- Fonts subset and preloaded.
- JS code-split; client components minimal.
- Third parties deferred.
- Animations transform/opacity only.
- Long lists virtualized.

Load `web-perf` for diagnosis.

## Step 11: System consistency

- Are tokens used, or raw values?
- Are existing components reused?
- Are variants and states consistent?
- Do Figma and code match?
- Is the naming consistent?
- Are there duplicate patterns?
- Is accessibility consistent across components?

Load `design-systems` for depth.

## Step 12: Content

- Is it true?
- Is it specific?
- Is it in the product's voice?
- Does the CTA say what happens?
- Do errors explain what happened and how to fix it?
- Are empty states useful?
- Is there filler or generic SaaS language?
- Are there placeholder links or lorem ipsum?

## Severity

| Severity | Meaning | Action |
| --- | --- | --- |
| **Blocker** | Prevents the task, breaks accessibility, or ships a serious bug | Fix before release |
| **Major** | Significant friction, confusion, or visual break | Fix in this cycle |
| **Minor** | Noticeable but not blocking | Fix when possible |
| **Nit** | Taste or polish | Optional |

Do not inflate nits into blockers. Do not bury blockers in a long list.

## Output format

Use `templates/critique-report.md`:

```text
## Summary
One paragraph: what works, what does not, and the main risk.

## Findings
| Severity | Finding | Evidence | Fix |
| --- | --- | --- | --- |
| Blocker | ... | ... | ... |

## What works
- ...

## Questions
- ...

## Next action
- ...
```

Each finding needs:

- What is wrong.
- Where it is (screen, component, file:line if possible).
- Why it matters (user impact or standard).
- The smallest fix.

## Common false positives

- “I don’t like the color” without a contrast or brand argument.
- “It should be bigger” without a hierarchy or accessibility reason.
- “Add more whitespace” without saying what should be grouped or separated.
- “Make it pop” — not a finding.
- “Users will be confused” without a task or evidence.
- “Best practice” without naming the practice or the context.
- “It looks AI-generated” without naming the banned pattern, its location, and the replacement. With those, it is a valid finding, not a false positive.

## Quality bar

- [ ] Context and primary task are known.
- [ ] First impression is recorded.
- [ ] The primary task was walked.
- [ ] Heuristics were checked.
- [ ] Visual hierarchy was assessed.
- [ ] Anti-generic audit completed; every finding names the pattern and the replacement.
- [ ] All states were checked.
- [ ] Responsive breakpoints were checked.
- [ ] Keyboard and screen reader were checked.
- [ ] Motion and performance were checked.
- [ ] System consistency was checked.
- [ ] Content was checked.
- [ ] Findings are prioritized and actionable.

## Related skills

- `design-engineering` for the full workflow.
- `visual-ui-design` for visual fixes.
- `interaction-motion` for motion fixes.
- `design-systems` for system fixes.
- `frontend-craft` for implementation fixes.
- `web-design-guidelines` for rule-based review.
- `web-perf` for performance.
- `apple-hig` for iOS-specific review.

## References

- `templates/critique-report.md` — report format.
- `references/critique-heuristics.md` — expanded checklist.
