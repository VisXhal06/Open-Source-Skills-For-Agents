---
description: Design, build, or critique a UI by loading the right design-engineering skills
---

Use the `design-engineering` skill for this request: $ARGUMENTS

Act as the front door. Do not merely tell the user to use another skill. Classify the request, read the relevant `SKILL.md` file or files, and execute the workflow. State the skills you loaded in one line, for example: "Using `design-research` to find a direction, then `visual-ui-design` to define the system."

## Classify the request

- Direction, references, moodboard, competitor audit, or user research → `design-research`
- Visual design, layout, typography, color, hierarchy, style, dark mode → `visual-ui-design`
- Interaction, states, microinteractions, animation, page transitions, scroll → `interaction-motion`
- Tokens, components, themes, Figma-to-code, AI-readable system → `design-systems`
- Production implementation, responsive, accessibility, performance, React/Next.js → `frontend-craft`
- AI tools, Figma MCP, v0/Lovable/Framer, design-to-code → `ai-design-workflow`
- Review, critique, audit, "why does this feel off" → `design-critique`

## Rules

- Use the smallest useful set of skills. A small request gets one skill; a full page gets a composition.
- If more than one applies, load them in workflow order: brief → research → direction → interaction → system → build → critique.
- Read each selected skill before acting. Never claim a skill was used if its file was not read.
- Sub-skills are directly accessible. The router is the default entry point, not a gate.
- Never stop at "use X." If X is right, load X and do the work.
- If the user asks for actual work, read the first selected skill and begin. A routing table alone is not a completed response.
- Start with the brief: audience, job, feeling, constraints, non-goals. If it is missing, propose assumptions and label them.
- Create two or three genuinely different directions before polishing one. The anti-generic gate is binding: reject Inter, Roboto, Arial, Helvetica, and `system-ui` stacks; violet/indigo/purple gradients on white and blue-to-purple "AI" gradients; the centered badge-headline-two-buttons hero; three identical feature cards; the cream + serif + terracotta and near-black + acid-green defaults; identical rounded cards; one radius and shadow everywhere; all-caps eyebrows; gradient blobs; floating dashboard heroes; fade-and-slide-up on every section. A banned choice ships only when the brief, brand, or existing system requires it, and the exception is recorded.
- Before building, write the six-line design record: direction, type rationale, palette source, layout logic, signature element, rejected defaults. A banned default that defines the first impression is a blocker; a localized one is a major finding. Recoloring is not a replacement.
- Use real content. Design all states: empty, loading, error, success, disabled, focus, hover, active.
- Check 320px, 768px, 1440px, dark mode, 200% zoom, keyboard, screen reader, and reduced motion.
- Motion must have a purpose, a timing/easing spec, and a reduced-motion path. Respect WCAG 2.2 and Core Web Vitals.
- Build in code early. A vertical slice beats a pile of static screens.
- Use existing design tokens and components before creating new ones.
- End with the artifact, the evidence, and the next action.

For the source map, read `~/.agents/skills/design-engineering/references/landscape.md`. For primary sources, read `~/.agents/skills/design-engineering/references/sources.md`.
