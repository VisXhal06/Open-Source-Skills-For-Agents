---
name: documentation-system
description: Use when setting up or repairing project documentation such as README, AGENTS.md, ADRs, API docs, runbooks, changelog, onboarding, or docs that keep going stale.
license: MIT
compatibility: opencode
metadata:
  version: "1.1.0"
---

# Documentation System

Documentation is part of the product. Its job is to let someone make a correct decision or change without asking the author. If a document does not do that, it is either incomplete or unnecessary.

## Suite integration

Part of the senior-dev suite. `senior-dev-os` can load this skill automatically when knowledge is missing, stale, or scattered; direct invocation works too. If the router loaded it, start with the audience and produce the docs map, owners, and freshness checks.

## Start with the audience

| Audience | Needs | Lives in |
| --- | --- | --- |
| New developer | Setup, architecture, first task | `README.md`, `docs/onboarding.md` |
| AI agent | Commands, boundaries, conventions | `AGENTS.md` |
| Maintainer | Decisions and trade-offs | `docs/adr/` |
| API consumer | Auth, endpoints, errors, examples | `docs/api/` or generated reference |
| On-call engineer | Symptoms, diagnosis, rollback | `docs/runbooks/` |
| Product stakeholder | Problem, scope, metrics | `docs/product-brief.md` |
| User | What changed and how to use it | `CHANGELOG.md`, help center |

If a document has no audience, delete it.

## Docs map

```text
README.md                     # what, quickstart, architecture, deploy
AGENTS.md                     # operating manual for agents
CHANGELOG.md                  # user-facing changes
docs/
  product-brief.md            # problem, users, scope, metrics
  roadmap.md                  # milestones and vertical slices
  testing-strategy.md         # risks, levels, edge cases, gates
  onboarding.md               # first day, first week, first task
  adr/
    0001-<decision>.md
  api/
    overview.md
    errors.md
  runbooks/
    deploy.md
    rollback.md
    incident.md
```

Keep this map in the README or `docs/README.md` so people can find things.

## Rules

- Docs live with the code and are reviewed in the same pull request.
- Every document has an owner and a last-verified date.
- One source of truth. Link instead of copying.
- Write for the reader's task, not the author's history.
- Prefer short documents with clear headings over long prose.
- Commands must be copy-pasteable.
- Delete or archive stale docs; do not leave contradictory versions.
- Generated API docs come from the schema, not from manual duplication.
- Use `stop-slop` to remove filler and AI-writing tells.

## Documentation as context engineering

Docs are the context interface for both people and agents. Curate them; do not dump everything into one file.

- `AGENTS.md` is a contract: commands, boundaries, conventions, and verification. Keep it short and current.
- Specs and ADRs preserve the "why" that code cannot.
- Link to sources instead of copying them; copies drift.
- Too much context reduces agent effectiveness. Put the common path in `AGENTS.md` and link to deeper docs.
- Write for retrieval: clear headings, short sections, searchable terms, and copy-pasteable commands.
- Every doc has an owner and a last-verified date.

## README

Use `templates/README.md`. The README must answer:

1. What is this?
2. Who is it for?
3. How do I run it locally?
4. What environment variables are required?
5. How do I test it?
6. How do I deploy it?
7. Where are the deeper docs?
8. Who owns it?

Keep the quickstart under ten minutes. If setup takes longer, provide a script or a container.

## AGENTS.md

Use `codebase-playbook/templates/AGENTS.md`. Do not duplicate the README. The agent manual needs:

- Exact commands
- Architecture map
- Conventions
- Boundaries and generated files
- Verification requirements
- Links to docs
- Known gotchas

Keep it current. An agent following stale instructions is worse than an agent with no instructions.

## ADRs

Write an ADR for decisions that are expensive to reverse, cross-cutting, or surprising.

Use `templates/adr.md`. Keep it short:

- Context
- Decision
- Alternatives
- Consequences
- Revisit conditions

Do not rewrite history. Supersede an old ADR with a new one and link both.

## Runbooks

A runbook is for a person under pressure. It must be concrete.

Use `templates/runbook.md`. Include:

- What this runbook covers
- Symptoms and alerts
- Prerequisites and access
- Step-by-step diagnosis
- Remediation
- Rollback
- Escalation
- Post-incident actions

Test the runbook during a calm period. A runbook that has never been executed is a hypothesis.

## API documentation

Generate from the schema where possible: OpenAPI, GraphQL schema, or typed route definitions.

Document:

- Authentication and scopes
- Base URL and versioning
- Every endpoint: method, path, params, body, response
- Error codes and shapes
- Pagination, filtering, sorting
- Rate limits
- Idempotency
- Webhooks and retries
- One request and response example per endpoint

Keep examples executable. A curl example that does not run is worse than no example.

## Onboarding

Use `templates/onboarding.md`. Structure:

- Day 1: access, setup, run the app
- Week 1: architecture tour, first small task, testing workflow
- First month: own a feature, review a PR, ship to production
- Who to ask for what
- Glossary of domain terms

An onboarding doc is also a test of the README. If onboarding needs undocumented steps, fix the README.

## Changelog

Write for users, not for git history.

```markdown
## [1.4.0] - 2026-10-20

### Added
- Bulk export for invoices.

### Changed
- Search now supports filters by date.

### Fixed
- Duplicate charge when retrying a failed payment.

### Breaking
- `GET /v1/orders` now returns `items` instead of `lines`.
```

Link the migration guide for breaking changes.

## Freshness

Documentation debt compounds. Put it on a schedule:

| Cadence | Check |
| --- | --- |
| Every PR | Update docs affected by the change |
| Monthly | Link check, stale commands, last-verified dates |
| Quarterly | README and onboarding walkthrough by someone new |
| Before launch | Runbooks and rollback tested |

Add a `docs:check` script if possible:

- Markdown link checker
- Spell check
- Code block command validation
- Stale date report

## Writing style

- Answer first. Put the conclusion in the first paragraph.
- Use short sections and descriptive headings.
- Prefer tables for options, commands, and status.
- Use active voice.
- Define domain terms once.
- Remove filler: "simply", "just", "obviously", "in order to".
- Do not use a screenshot where text or a command works.
- Keep line length reasonable for diffs.

## Common mistakes

| Mistake | Consequence | Fix |
| --- | --- | --- |
| Docs in a separate wiki | Drift from the code | Keep docs in the repo |
| README is a marketing page | Developers cannot run it | Add quickstart and architecture |
| AGENTS.md duplicates everything | Becomes stale | Keep only operating rules |
| No owner | Nobody updates it | Assign an owner and date |
| Huge design docs | Nobody reads them | One page plus ADRs |
| Manual API reference | Diverges from the schema | Generate it |
| Runbook never tested | Fails during an incident | Execute it quarterly |
| No changelog | Users surprised by changes | Write user-facing entries |

## Related skills

- `project-kickoff` for the initial docs baseline
- `codebase-playbook` for AGENTS.md and repo conventions
- `testing-strategy` for the testing doc
- `launch-readiness` for runbooks
- `stop-slop` for prose quality
