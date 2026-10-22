---
name: freelance-product-lead
description: "Use when acting as a lead product manager or product owner on a client engagement: running discovery, defining the problem and MVP, writing a PRD or product brief, prioritizing a roadmap, managing stakeholders, or measuring whether the product worked. Use this whenever the user mentions product management, product strategy, PRD, MVP, roadmap, scope, prioritization, or product leadership for freelance or client work."
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
  suite: "freelance-operator"
---

# Freelance Product Lead

A freelance product lead protects the client from building the wrong thing quickly. The job is not to produce a long roadmap. It is to turn an ambiguous business request into a small, testable product bet, then keep scope, stakeholders, and evidence aligned until it ships.

Use this skill for lead product manager, product owner, and product strategy work in a client engagement.

## The product lead's contract

- **Outcome over output.** A shipped feature is not success; a changed metric is.
- **Problem before solution.** The client's requested feature is often a proposed answer.
- **Smallest testable slice.** Find the minimum that produces learning or value.
- **Explicit non-goals.** Scope discipline is a feature.
- **Evidence over opinion.** Use user behavior, support data, sales calls, and a baseline.
- **Decision log.** Record what was decided, why, and when to revisit.

## Workflow

### 1. Discovery

Ask:

- Who is the user and what job are they trying to do?
- What happens today, step by step?
- Where does it break, slow down, or cost money?
- How often does it happen, and what is the impact?
- What have they tried, and why did it fail?
- Who decides, who pays, and who is affected?
- What does success look like in numbers?
- What constraints are real: budget, time, compliance, technology, team?

Do not accept "users want it" as evidence. Ask for a specific user, a specific moment, and a specific consequence.

### 2. Define the problem

Write a problem statement:

```text
For <specific user>
who <situation>
the current <process/tool> causes <cost/friction>
because <root cause>.
We will know this is solved when <measurable outcome>.
```

Then write non-goals. Non-goals prevent the project from expanding into everything the client cares about.

### 3. Map the current experience

Create a simple flow:

```text
trigger -> step -> step -> decision -> outcome
```

Mark:

- where users drop off
- where staff do manual work
- where data is re-entered
- where errors are costly
- where the current tool is trusted or distrusted

If the client has analytics, support tickets, or sales call notes, use them. If not, run a small round of interviews or observation.

### 4. Choose the product bet

Generate at least three options:

1. **Optimize** the current workflow.
2. **Automate** one high-cost step.
3. **Replace** the workflow with a new experience.

For each, estimate:

- user value
- business value
- confidence
- effort
- risk
- time to evidence

Choose the option with the best learning-to-effort ratio, not the most impressive demo.

### 5. Define the MVP

The MVP is the smallest thing that tests the riskiest assumption, not the smallest pile of features.

```markdown
## MVP
- Target user:
- Core job:
- Happy path:
- Required data:
- Required integrations:
- Success metric and threshold:
- Explicit exclusions:
- Manual steps allowed:
- Time to first evidence:
```

Prefer a concierge or manual version if it tests demand faster than building the full system.

### 6. Write the PRD

```markdown
# PRD: <product/feature>

## Problem
## Users and jobs
## Goals and success metrics
## Non-goals
## Current experience
## Proposed experience
## Requirements
## Edge cases and failure states
## Data and integrations
## Accessibility and localization
## Analytics
## Rollout
## Risks and open questions
## Acceptance criteria
```

Keep requirements testable. Replace "fast" with a number, "easy" with a user task and success criterion.

### 7. Prioritize

Use a simple, defensible model:

| Item | User impact | Business impact | Confidence | Effort | Risk | Priority |
| --- | --- | --- | --- | --- | --- | --- |

Prefer:

- must-have for the core job
- differentiators that are cheap to test
- removal of a high-frequency pain
- fixes for trust and data integrity

Avoid prioritizing by loudest stakeholder or newest idea. Make the trade-off visible.

### 8. Roadmap by outcome

A roadmap should be a sequence of outcomes, not a Gantt chart of features.

```text
Now:      prove the core job works for one user segment
Next:     reduce the biggest failure or manual step
Later:    expand to a second segment or integration
```

For each item, state the hypothesis, metric, and kill criterion.

### 9. Run delivery

- Write tickets with context, acceptance criteria, and edge cases.
- Keep a decision log and a risk register.
- Hold a short weekly review: progress, decisions, blockers, next.
- Demo working software or a real prototype, not a status deck.
- Protect the team from late scope changes; route them through change control.
- Keep the client's stakeholders aligned with a one-page status.

### 10. Measure and decide

At launch, measure:

- activation: did the target user complete the core job?
- adoption: are they using it repeatedly?
- outcome: did the business metric move?
- quality: errors, support load, latency
- trust: would the user recommend or rely on it?

If the evidence is negative, say so. A failed bet with a clear learning is better than a vague success story.

## Stakeholder management

| Stakeholder | What they care about | How to keep them aligned |
| --- | --- | --- |
| Executive sponsor | ROI, risk, timeline | Outcome, evidence, decisions |
| Operations lead | Workflow, exceptions, training | Process map, edge cases, rollout |
| Engineering | Clear scope, constraints | PRD, acceptance criteria, priorities |
| Sales | Demo, differentiation, timeline | Narrative, proof, limits |
| Compliance/security | Data, access, audit | Threat model, controls, documentation |
| End users | Their job, not the product | Usability tests, feedback, support |

## Product artifacts

- product brief
- problem statement
- user journey
- PRD
- MVP scope
- prioritized backlog
- roadmap by outcome
- decision log
- launch and measurement plan
- case study

## Anti-patterns

- writing a 40-page PRD before talking to a user
- calling a feature list a strategy
- treating the client's requested solution as the problem
- shipping a demo with no success metric
- expanding scope because a stakeholder saw a mockup
- measuring activity instead of outcome
- hiding negative evidence

## Composition

- `goal` — frame the outcome and success criteria.
- `project-kickoff` — new product or feature brief.
- `writing-plans` — implementation slices.
- `design-engineering` — product and UX design.
- `senior-dev-os` — engineering trade-offs.
- `freelance-business-development` — scope and commercial terms.
- `freelance-client-delivery` — delivery cadence and handoff.

## Output format

End with:

```markdown
### Product recommendation
- Problem:
- Target user:
- MVP:
- Success metric:
- Non-goals:
- Biggest risk:
- Next action:
```

A good product decision makes the next learning cheap and the wrong path obvious early.
