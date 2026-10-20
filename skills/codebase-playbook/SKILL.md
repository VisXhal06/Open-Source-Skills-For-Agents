---
name: codebase-playbook
description: Use when a repository needs conventions, structure, ownership, dependency policy, quality gates, or an audit of how maintainable and agent-ready it is.
license: MIT
compatibility: opencode
metadata:
  version: "1.1.0"
---

# Codebase Playbook

Make the codebase legible, changeable, and safe. A good playbook lets a new human or agent make a correct change without asking where things live or what "done" means.

## Suite integration

Part of the senior-dev suite. `senior-dev-os` can load this skill automatically when a repo is hard to change, slow to onboard, or not agent-ready; direct invocation works too. If the router loaded it, run the audit before writing rules, then produce the artifacts.

## Start with an audit

Do not write rules before you know what is broken. Score each dimension 0–2.

Use `templates/audit-scorecard.md` or write the table into `docs/codebase-audit.md`.

| Dimension | 0 | 2 |
| --- | --- | --- |
| Local setup | Cannot run | One documented command |
| Structure | No clear boundaries | Modules with owners and entry points |
| Tests | None or flaky | Fast, risk-based, trustworthy |
| CI | Manual | Required gates and preview deploy |
| Docs | Missing | README, AGENTS.md, ADRs, runbooks |
| Observability | None | Logs, errors, metrics, alerts |
| Security | Unknown | Least privilege, secrets managed, scans |
| Dependencies | Stale | Policy and scheduled upgrades |
| Release | Manual and scary | Repeatable with rollback |
| Agent readiness | No context | AGENTS.md and task packets |

A score below 12 means fix foundations before adding features. A score below 6 means stop feature work and stabilize.

## AI-ready repository

DORA's 2025 research associates AI adoption with both higher throughput and higher instability. The repository determines which effect dominates. Check:

- **Strong version control:** small commits, protected main, reproducible builds.
- **Small batches:** short-lived branches, small PRs, feature flags.
- **AI-accessible internal data:** docs, schemas, and decisions live in the repo, not in private chats.
- **Clear AI stance:** the team knows what may be delegated and what must stay human-owned.
- **Quality internal platform:** fast CI, preview environments, reliable local setup.
- **User-centric focus:** AI work is measured by user outcomes, not generated lines.
- **Healthy data ecosystems:** test data, logs, and analytics are usable without leaking secrets or PII.

If these are weak, fix them before scaling agent usage. More agents on a weak platform produce more rework.

## Write AGENTS.md

`AGENTS.md` is the operating manual for agents. Keep it under about 150 lines. It is not a second README; it tells an agent how to work here.

Use `templates/AGENTS.md`. Required sections:

1. **Purpose** — one paragraph.
2. **Stack** — language, framework, database, hosting, package manager.
3. **Commands** — install, dev, format, lint, typecheck, test, build, deploy.
4. **Architecture map** — the five to ten directories that matter and what lives there.
5. **Conventions** — naming, error handling, state, styling, commits.
6. **Boundaries** — what not to touch without approval; generated files; migrations.
7. **Verification** — the exact commands that must pass before a task is done.
8. **Docs** — links to the brief, ADRs, testing strategy, and runbooks.
9. **Gotchas** — local quirks, flaky tests, environment traps.

If `AGENTS.md` disagrees with the code, fix one of them. Stale instructions are worse than none.

## Make the README useful

The README answers:

- What is this?
- Who is it for?
- How do I run it locally in under 10 minutes?
- What environment variables are required?
- How do I test it?
- How do I deploy it?
- Where do I go for deeper docs?
- Who owns it?

Add a small architecture diagram in Mermaid if the system has more than three moving parts.

## Define the architecture map

Write down the modules, their responsibilities, and their allowed dependencies. Keep it short.

```text
src/
  app/          routes and pages
  features/     vertical feature modules
  server/       API handlers, services, jobs
  db/           schema, migrations, queries
  lib/          shared utilities with no domain knowledge
  components/   shared UI primitives
```

Rules that prevent decay:

- A feature owns its UI, server logic, and tests.
- Shared code moves to `lib/` only after a second real use.
- The database schema is changed only through migrations.
- Cross-module imports go through a public entry point, not deep file paths.
- Generated files are never edited by hand.

## Record decisions with ADRs

Write an ADR when a decision is:

- Expensive to reverse
- Cross-cutting
- Surprising to a new engineer
- A deliberate departure from the default

Do not write an ADR for every library choice. Use `project-kickoff/templates/adr.md` or `documentation-system/templates/adr.md`.

## Dependency policy

- Commit the lockfile.
- Pin runtime versions in one place.
- Enable automated security alerts.
- Review updates on a schedule, not only when something breaks.
- Group patch and minor updates; handle majors one at a time.
- Check licenses before adding a dependency.
- Remove unused dependencies quarterly.
- Prefer the platform and standard library over a new package for small needs.

## Quality gates

| Gate | When | Must pass |
| --- | --- | --- |
| Pre-commit | Before commit | Format, lint staged files |
| Pull request | Every PR | Lint, typecheck, unit tests, build |
| Integration | PRs touching boundaries | Contract or integration tests |
| Preview | Every PR | Deploy succeeds, smoke test |
| Main | Merge | Full suite, deploy |
| Nightly | Scheduled | E2E, dependency audit, mutation tests if used |
| Release | Before production | Launch checklist |

Branch protection should require the gates. A documented gate that can be bypassed is a suggestion.

## Review rules

- One logical change per PR.
- Aim for roughly 200 changed lines; split anything over 400 unless it is a mechanical change.
- Review is knowledge sharing and risk reduction, not gatekeeping.
- The description states the problem, the approach, and the verification.
- Tests are reviewed with the code.
- Screenshots or recordings for UI changes.
- Migrations include a rollback or a forward-fix plan.
- No secrets, debug logs, or commented-out code.
- The author runs the verification commands, not just CI.

Use `requesting-code-review` and `verification-before-completion`.

## Release process

- Version with semantic versioning or date-based releases.
- Keep a changelog written for users, not commits.
- Ship behind a feature flag when the change is risky.
- Use a canary or staged rollout for production.
- Know the rollback command before deploying.
- Announce breaking changes before they ship.

## Maintenance cadence

| Cadence | Activity |
| --- | --- |
| Weekly | Triage bugs, flaky tests, dependency alerts |
| Monthly | Dependency updates, dead code removal, docs freshness check |
| Quarterly | Architecture review, access review, backup restore test |
| Yearly | Disaster recovery drill, major upgrade plan, cost review |

## Common mistakes

| Mistake | Consequence | Fix |
| --- | --- | --- |
| AGENTS.md is a copy of the README | Agents miss the operating rules | Write commands, boundaries, and verification |
| Rules live only in a wiki | They drift from the code | Keep docs in the repo |
| Every module imports every module | Changes ripple everywhere | Define allowed dependencies |
| Coverage target without risk analysis | Tests that assert nothing | Use `testing-strategy` |
| Dependency upgrades deferred | Painful, risky big-bang upgrade | Scheduled small updates |
| No rollback plan | A bad deploy becomes an outage | Document and test rollback |

## Related skills

- `senior-dev-os` for routing
- `project-kickoff` for a new repo
- `testing-strategy` for the test plan
- `documentation-system` for the docs map
- `agent-delegation` for task packets
- `launch-readiness` for production
