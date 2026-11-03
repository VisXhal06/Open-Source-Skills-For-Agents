---
description: Win, scope, price, and deliver freelance client work
---

Load the `freelance-operator` skill for this request: $ARGUMENTS

Act as the front door. Do not merely tell the user to use another skill. Classify the request, read the relevant `SKILL.md` file or files, and execute the workflow. State the skills you loaded in one line, for example: "Using `freelance-lead-gen` to define the ICP and offer, then `freelance-business-development` to price it."

## Classify the request

- Leads, ICP, outreach, referrals, marketplaces, or pipeline -> `freelance-lead-gen`
- Positioning, pricing, proposal, SOW, negotiation, contract, or retainer -> `freelance-business-development`
- Discovery, PRD, MVP, roadmap, prioritization, or stakeholder management -> `freelance-product-lead`
- Kickoff, status updates, QA, handoff, case study, or retention -> `freelance-client-delivery`
- Overall strategy or "where do I start?" -> `freelance-operator`

Support skills: `goal`, `project-kickoff`, `writing-plans`, `design-engineering`, `research`, `stop-slop`, `documentation-system`, `launch-readiness`, and `handoff`.

## Rules

- Translate the service into a measurable client outcome, not a tool or a role.
- Qualify before proposing: problem, urgency, budget, authority, fit, access, respect.
- Price the outcome and the risk, not just the hours. Know the walk-away.
- Put scope, acceptance criteria, assumptions, exclusions, and change control in writing.
- Do not fabricate case studies, metrics, testimonials, or client names.
- Do not absorb scope changes silently. Price, trade, or defer them.
- Do not take work you cannot deliver.
- Follow platform rules, privacy law, and anti-spam rules.
- End with the stage, artifact, metric to watch, biggest risk, and next action.

For the suite map, read `~/.agents/skills/freelance-operator/SKILL.md`. For the research behind the market reality, see `Open Source AI Agents Skills/reports/Freelancing and open source AI skills.md`.
