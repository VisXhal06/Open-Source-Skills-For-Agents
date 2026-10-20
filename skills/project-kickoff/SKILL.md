---
name: project-kickoff
description: Use when starting a new product, feature, or client project and you need to turn the idea into a buildable first milestone with clear scope, architecture, documentation, and quality gates.
license: MIT
compatibility: opencode
metadata:
  version: "1.1.0"
---

# Project Kickoff

Turn an idea into a first milestone that can be built, demoed, and handed to another person. The goal is not a perfect plan. The goal is to remove the expensive ambiguities before code starts.

## Suite integration

Part of the senior-dev suite. `senior-dev-os` can load this skill automatically for a new product, feature, or client project; direct invocation works too. If the router loaded it, read the existing goal or brief and `AGENTS.md` first, then produce the artifacts below. Do not stop at a recommendation.

## What this produces

| Artifact | Purpose |
| --- | --- |
| `docs/product-brief.md` | Users, problem, outcome, scope, non-goals, risks |
| `docs/adr/0001-<decision>.md` | The architecture decision and its trade-offs |
| `docs/roadmap.md` | First milestone as vertical slices |
| `AGENTS.md` | How agents should work in this repo |
| `README.md` | How a human runs and understands the project |
| CI + quality gates | The definition of a safe change |
| Task packets | The first assignable units of work |

## Step 1: One-page product brief

Ask at most five questions:

1. Who has the problem, and what do they do today?
2. What outcome changes for them?
3. How will you know it worked?
4. What is explicitly out of scope for the first milestone?
5. What constraint could kill the project: time, budget, compliance, team skill, or distribution?

If the user cannot answer, propose a default and label it as your assumption. Do not stall on a perfect answer.

Write the brief with `templates/product-brief.md`. Keep it to one page. If it needs more than a page, the scope is probably too large.

## Step 2: Constraints and non-goals

List the real constraints:

- Deadline and budget
- Team size and skills
- Existing stack and integrations
- Expected traffic and data volume
- Regulatory, privacy, or security requirements
- Platforms and browsers
- Operational support available after launch

Write **non-goals** explicitly. A non-goal is not a maybe; it is something the team has agreed not to build in this milestone.

### Classify the decision

Not every choice deserves the same rigor. Separate one-way doors from two-way doors:

| Door | Examples | Rigor |
| --- | --- | --- |
| One-way | Public API, data model, auth, pricing, deployment region, data deletion | Advisor review, ADR, cheapest test, rollback plan |
| Two-way | Internal naming, UI copy, library choice, folder structure | Decide quickly, record one line, move |

Spend judgment proportional to reversibility. A reversible decision that is slow to make is still a cost.

## Step 3: Architecture decision

Choose the simplest architecture that can survive the next 12 months. Write an ADR with `templates/adr.md`.

Defaults to challenge before deviating:

- **Monolith first.** Modular boundaries inside one deployable.
- **Managed services** for auth, payments, email, file storage, and error tracking.
- **PostgreSQL** unless the access pattern clearly needs something else.
- **One repository** unless independent deployability is a proven requirement.
- **Server-rendered or simple SPA** over a complex distributed frontend.
- **Background jobs** only where work is slow, retryable, or scheduled.

Avoid on day one: microservices, Kubernetes, custom auth, event sourcing, a design system, a plugin architecture, and abstractions for imagined reuse.

Record the decision, the alternatives considered, and the conditions that would make you revisit it.

## Step 4: Walking skeleton

A walking skeleton is the thinnest end-to-end system that can be deployed. Build it before feature work.

Minimum:

- Repository with a clear structure
- `README.md` and `AGENTS.md`
- `.env.example` and secret handling
- Format, lint, typecheck, test, and build commands
- CI running those commands on every PR
- A preview or staging deploy
- Health check endpoint
- Structured logs and error tracking
- Database connection and one migration
- One vertical slice: UI → API → database → response
- Seed data and a reset command
- Backup and restore path for persistent data

If the skeleton cannot deploy, do not add features. Fix the deployment path first.

## Step 5: First milestone as vertical slices

Define three to five slices. Each slice must be demoable by itself.

For every slice, write:

- **Outcome:** what a user can do after it ships
- **Acceptance criteria:** testable statements
- **Touch points:** UI, API, data, jobs, integrations
- **Risks:** what is uncertain or expensive
- **Verification:** commands and manual checks
- **Dependencies:** what must ship first

Prefer slices that cross the stack over layers that touch every file. A thin end-to-end slice exposes integration risk early.

### Spec-first for AI-assisted work

If agents will implement any part of a slice, write the slice as a contract before delegating:

- Outcome and user journey
- Acceptance criteria
- Allowed paths and interfaces
- Edge cases and error behavior
- Verification commands
- Explicit non-goals

A spec that an agent can interpret two ways is not ready. Add the contract to the task packet and keep it with the code.

Use `templates/first-milestone.md`.

## Step 6: Documentation baseline

Create the minimum docs now, not after launch:

```text
README.md
AGENTS.md
docs/
  product-brief.md
  roadmap.md
  testing-strategy.md
  adr/0001-<decision>.md
  runbooks/
```

Use `documentation-system` for the full map. For kickoff, the README and AGENTS.md are mandatory.

## Step 7: Quality gates

Define what must pass before merge:

- Formatting
- Linting
- Type checking
- Unit tests
- Integration tests for changed boundaries
- Build
- Preview deploy
- Security scan for dependencies and secrets

Write the exact commands in `AGENTS.md` and CI. A gate that only exists in someone's memory is not a gate.

## Step 8: Kickoff review

Before the first feature task, confirm:

- [ ] The product brief fits on one page.
- [ ] Non-goals are explicit.
- [ ] The architecture decision is recorded.
- [ ] The walking skeleton deploys end to end.
- [ ] CI runs the quality gates.
- [ ] The first milestone has three to five vertical slices.
- [ ] Each slice has acceptance criteria and verification.
- [ ] README and AGENTS.md exist.
- [ ] The first task packet is ready.

## Common mistakes

| Mistake | Consequence | Fix |
| --- | --- | --- |
| Choosing the stack before the problem | Sophisticated solution to the wrong problem | Write the brief first |
| Building auth, billing, and admin before the core loop | Months of work before learning | Managed services, manual admin |
| Horizontal layers instead of slices | Integration risk discovered late | Vertical slices |
| No non-goals | Scope creep by default | Write them down |
| No walking skeleton | "Works on my machine" until launch | Deploy on day one |
| Docs postponed | Nobody can onboard or delegate | Create the baseline now |
| Ten slices in milestone one | Nothing finishes | Cut to three to five |

## Related skills

- `senior-dev-os` for routing
- `writing-plans` after the brief is approved
- `codebase-playbook` for the repo operating manual
- `testing-strategy` for the test plan
- `documentation-system` for the docs map
- `agent-delegation` for the first task packets
- `launch-readiness` before the first production release
