---
name: oss-system-designer
description: "Use when designing a feature, API, service boundary, plugin contract, data flow, or migration in an open-source project or large codebase; when writing an RFC or ADR; or when a change needs maintainer consensus, backward compatibility, or a rollout plan. Use this whenever the user asks for system design, architecture, an RFC, an API contract, or a non-trivial design decision in a project they do not own."
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
  suite: "oss-contributor"
---

# OSS System Designer

Open-source system design has a constraint that product design often hides: **you are changing a shared contract you do not own alone.** The maintainer, downstream users, plugin authors, and future contributors all pay for the decision. Good design makes the trade-off visible and keeps the project reversible.

Use this skill for RFCs, ADRs, API changes, service boundaries, plugin interfaces, data models, migrations, and any change that cannot be reviewed as a single local patch.

## Design posture

- Start from the problem and the constraints, not the architecture diagram.
- Prefer the smallest design that satisfies the next two years, not the next two weeks.
- Treat public APIs, schemas, CLI flags, config keys, event names, and error codes as contracts.
- Optimize for reversibility. Most decisions are two-way doors; say which ones are not.
- Make the failure path as explicit as the happy path.
- Write down what you are deliberately not doing.
- Design for the maintainer's review capacity. A smaller RFC with a clear recommendation beats a survey of ten options.

## Workflow

### 1. Frame the decision

Write:

```text
Decision:
Why now:
Who is affected:
Constraints:
Quality attributes (ranked):
Non-goals:
Decision owner:
Revisit conditions:
```

Quality attributes to rank explicitly: correctness, compatibility, security, reliability, latency, throughput, cost, operability, accessibility, maintainability, developer experience. You cannot maximize all of them.

### 2. Map the current system

Use `large-codebase-navigator`. Capture:

- current boundaries and ownership
- data ownership and flow
- public contracts and consumers
- deployment and release model
- invariants that must survive
- known pain points and incident history
- what is generated, vendored, or deprecated

If the current system is not understood, stop designing the replacement.

### 3. Generate real alternatives

Produce at least three:

1. **Minimal/local** — smallest change inside the current design.
2. **Evolutionary** — extend the current design with a new boundary or adapter.
3. **Replacement** — a new design, with a migration path.

For each, state:

- how it works
- what it optimizes
- what it costs
- compatibility impact
- failure modes
- migration effort
- reversibility
- who has to maintain it

Do not present one option plus two straw men. If the minimal option is genuinely best, say so and explain why the others lose.

### 4. Choose with criteria

Use a decision matrix with weights agreed before scoring:

| Criterion | Weight | Option A | Option B | Option C |
| --- | --- | --- | --- | --- |
| Correctness | 5 | | | |
| Compatibility | 5 | | | |
| Security | 5 | | | |
| Operability | 4 | | | |
| Maintenance | 4 | | | |
| Delivery cost | 3 | | | |

A score is not a decision. Use it to expose disagreement, then record the rationale and the conditions that would change the answer.

### 5. Define the contract

For an API, event, plugin, or data model, specify:

- names and types
- required vs optional fields
- defaults and null semantics
- error model and status codes
- versioning and deprecation policy
- idempotency and retry behavior
- authorization and tenancy
- pagination, limits, and rate limits
- ordering and consistency guarantees
- observability: logs, metrics, traces
- compatibility matrix

Write examples for the normal case, the edge case, and the failure case.

### 6. Design the rollout

Every non-trivial design needs a path from old to new:

1. Add the new path without removing the old.
2. Dual-write or dual-read if data is involved.
3. Backfill and verify.
4. Switch traffic behind a flag.
5. Observe.
6. Remove the old path after the compatibility window.
7. Document the migration and rollback.

For a breaking change, include a deprecation timeline, migration guide, codemod if possible, and a support window.

### 7. Write the RFC or ADR

Use the project's template if one exists. Otherwise:

```markdown
# RFC: <title>

## Summary
## Motivation
## Goals and non-goals
## Current system
## Proposed design
## Alternatives considered
## Compatibility and migration
## Security and privacy
## Performance and cost
## Observability
## Rollout and rollback
## Open questions
## Decision
```

An ADR is shorter:

```markdown
# ADR: <decision>

## Context
## Decision
## Consequences
## Alternatives
## Revisit when
```

### 8. Socialize before implementing

- Open a discussion or draft RFC before a large PR.
- Ask the maintainer what would make the design acceptable.
- Separate "must have" from "nice to have."
- Record objections and how they were resolved.
- If consensus is not reached, prefer the reversible experiment over a permanent decision.

Do not surprise maintainers with a 4,000-line PR that implements an undiscussed architecture.

## OSS-specific constraints

| Constraint | Design implication |
| --- | --- |
| Public API stability | Add, deprecate, then remove. Never silently break. |
| Multiple versions | Support the documented matrix or state the drop clearly. |
| Plugin ecosystem | Treat plugin interfaces as public contracts with versioning. |
| Downstream forks | Avoid hidden coupling to a hosted service or private config. |
| Maintainer capacity | Prefer fewer concepts and less custom infrastructure. |
| Security disclosure | Design private reporting and coordinated fixes. |
| License compatibility | Check dependencies and copied code before proposing them. |
| Contributor experience | Make the change testable locally with one command. |

## Review questions

Ask before approving a design:

- What is the one assumption that could make this fail?
- What happens when the dependency is slow, down, or returns bad data?
- Can the old and new versions run at the same time?
- Who owns the migration and the cleanup?
- What is the rollback?
- How will we know it is working in production?
- What does a downstream user have to change?
- Is this design smaller than the problem requires?

## Composition

- Use `senior-dev-os` for judgment and trade-off framing.
- Use `project-kickoff` for a new product or feature brief.
- Use `writing-plans` to turn the design into vertical slices.
- Use `implementation-strategy` before changing released behavior or durable formats.
- Use `launch-readiness` for rollout, observability, and rollback.
- Use `oss-backend`, `oss-database`, or `oss-devops-server` for domain-specific design.

## Output format

End with:

```markdown
### Design decision
- Recommendation:
- Why:
- What we give up:
- Compatibility impact:
- Rollout:
- Revisit when:
- Next action:
```

The design is good when a maintainer can say "I understand the trade-off, I can review this, and I can reverse it."
