---
name: freelance-client-delivery
description: "Use when delivering a freelance or client engagement: kickoff, onboarding, weekly status, scope and change control, QA, stakeholder communication, handoff, documentation, case studies, or turning a project into a retainer or referral. Use this whenever the user mentions client delivery, onboarding, status updates, handoff, project management, or keeping a client happy."
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
  suite: "freelance-operator"
---

# Freelance Client Delivery

Winning the work is only half the business. Delivery is where reputation is made: the client experiences your communication, judgment, and reliability long before they can judge the code or design.

Use this skill to run an engagement so the client always knows what is happening, scope changes are explicit, quality is evidenced, and the project ends with proof you can reuse.

## The delivery contract

- The client knows the goal, scope, roles, cadence, and definition of done.
- Every week has a written update: progress, decisions, risks, next actions.
- Scope changes are priced and approved, not absorbed.
- Quality is verified against acceptance criteria, not vibes.
- The handoff is usable without you.
- The closeout produces a case study and a next step.

## Workflow

### 1. Kickoff

Before work starts, collect:

```markdown
## Engagement
- Client and sponsor:
- Goal and success metric:
- Scope and deliverables:
- Non-goals:
- Acceptance criteria:
- Timeline and milestones:
- Roles and decision rights:
- Communication channel and cadence:
- Access and credentials:
- Data handling:
- Risks:
- Change-control process:
```

Do not start with missing access, an unnamed decision-maker, or an undefined success metric. Those are the three most expensive ambiguities.

### 2. Onboarding

- Send a welcome note with the plan, contacts, and next meeting.
- Collect access through a secure channel, not email attachments.
- Confirm the tool stack and where work will live.
- Set up a shared status document and decision log.
- Agree on response times and meeting cadence.
- Confirm the first milestone and what the client must provide.

### 3. Plan the delivery

Break the work into vertical slices that produce something demonstrable:

```text
Slice 1: smallest end-to-end path
Slice 2: highest-risk integration or workflow
Slice 3: quality, edge cases, and operations
Slice 4: handoff, documentation, and training
```

For each slice: outcome, acceptance criteria, owner, evidence, and demo date.

### 4. Weekly cadence

Send a short update every week:

```markdown
## Status — week of <date>

**Done**
- ...

**In progress**
- ...

**Decisions**
- ...

**Risks / blockers**
- ...

**Next week**
- ...

**Need from you**
- ...
```

Keep it skimmable. Bad news early is a service; bad news late is a betrayal.

### 5. Change control

When a request is outside the agreed scope:

1. Acknowledge the need.
2. State the impact on scope, time, or price.
3. Offer options: add it, trade it, or defer it.
4. Get written approval before doing the work.

Template:

```text
This is outside the agreed scope. Adding it will take <time> and <price>,
or we can trade it for <existing item>. Which option do you prefer?
```

Do not silently absorb changes to keep the client happy. That teaches them that scope is negotiable and makes the eventual boundary feel like a breach.

### 6. Quality assurance

Before each demo or handoff:

- acceptance criteria met
- tests/checks run and recorded
- edge cases and error states handled
- accessibility and responsive behavior checked where relevant
- data and permissions verified
- documentation updated
- no secrets or debug artifacts left behind
- known limitations written down

Use `code-change-verification`, `testing-strategy`, `web-design-guidelines`, and `launch-readiness` as appropriate.

### 7. Stakeholder communication

- Give the sponsor outcomes and risks, not a task list.
- Give the working team specifics and decisions.
- Give end users a clear picture of what changes and when.
- Escalate early when a decision, access, or dependency is blocking progress.
- Never surprise the sponsor with a missed deadline in a public meeting.

### 8. Handoff

A handoff is complete when the client can operate and extend the work without you.

Include:

- architecture and code map
- setup and deploy instructions
- environment variables and secrets ownership
- test and QA commands
- runbook for common failures
- known limitations and backlog
- a recorded walkthrough
- training session or office hours
- support window and escalation path

### 9. Closeout

- Confirm acceptance in writing.
- Deliver the final invoice.
- Return or destroy access and data per the contract.
- Ask for a testimonial and a referral if the work went well.
- Write a case study with the before/after and a real number.
- Propose the next logical engagement or retainer.
- Archive the project in a reusable template.

### 10. Case study

```markdown
# <Client / project>

## Context
## Problem
## Constraint
## What we did
## Evidence
- before:
- after:
- method:
## What did not work
## Client outcome
## What I would do differently
```

A case study with a negative finding is more credible than a perfect story. The research on freelancing repeatedly shows that measurable proof outperforms generic claims.

## Delivery scorecard

| Dimension | Question |
| --- | --- |
| Scope | Is the boundary written and respected? |
| Communication | Does the client know status and risk weekly? |
| Quality | Is acceptance evidence recorded? |
| Margin | Is the work still profitable? |
| Handoff | Can the client operate without me? |
| Proof | Do I have a reusable case study? |
| Relationship | Is there a next step or referral? |

## Red flags

- the client adds scope every call and you absorb it
- the decision-maker is never in the room
- access or data is delayed and the deadline does not move
- the client judges progress by activity, not outcomes
- you are the only person who can deploy or explain the system
- the project has no acceptance criteria
- the client asks you to hide a risk from their boss
- the relationship is disrespectful or unsafe

## Composition

- `freelance-operator` — business context.
- `freelance-product-lead` — scope and product decisions.
- `freelance-business-development` — change orders and commercial terms.
- `documentation-system` — handoff docs and runbooks.
- `launch-readiness` — production readiness.
- `code-change-verification` — quality gate.
- `handoff` — session or project handoff.

## Output format

End with:

```markdown
### Delivery status
- Milestone:
- Done:
- In progress:
- Decisions:
- Risks:
- Client action needed:
- Next action:
```

Delivery succeeds when the client trusts you with the next problem.
