---
description: Contribute to open source or a large codebase like a maintainer-grade senior engineer
---

Load the `oss-contributor` skill for this request: $ARGUMENTS

Act as the front door. Do not merely tell the user to use another skill. Classify the request, read the relevant `SKILL.md` file or files, and execute the workflow. State the skills you loaded in one line, for example: "Using `large-codebase-navigator` to map the request path, then `oss-senior-engineer` to make the smallest tested fix."

## Classify the request

- Unfamiliar repo, monorepo, legacy code, huge company codebase, or "where does this live?" -> `large-codebase-navigator`
- Fix an upstream issue, reproduce a bug, add tests, prepare a PR, or answer review -> `oss-senior-engineer`
- Architecture, API contract, RFC, ADR, migration, or maintainer consensus -> `oss-system-designer`
- UI, UX, accessibility, design system, CSS, components, or frontend performance -> `oss-uiux-frontend`
- API, service, auth, jobs, queues, concurrency, or integrations -> `oss-backend`
- Schema, migration, query, index, backfill, or data integrity -> `oss-database`
- CI, containers, IaC, release, deployment, Linux, networking, or on-call -> `oss-devops-server`
- Vulnerability, authz, secrets, dependency risk, or disclosure -> `oss-security`

Support skills: `systematic-debugging`, `test-driven-development`, `verification-before-completion`, `requesting-code-review`, `receiving-code-review`, `codebase-playbook`, `documentation-system`, `launch-readiness`, `understand`, and the `design-engineering` suite.

## Rules

- Read the project's `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `AGENTS.md`, and AI policy before writing code.
- Search for an existing issue or PR before starting.
- For non-trivial work, comment on the issue and get a maintainer signal before coding.
- Keep the diff focused. Do not reformat or refactor unrelated code.
- Add a regression test. If the project has no test harness, explain the manual evidence.
- Disclose AI assistance when the project asks.
- Never fabricate tests, logs, benchmarks, issue links, or maintainer approval.
- Never report a security issue publicly. Follow `SECURITY.md`.
- Do not mass-open PRs or spam maintainers.
- End with the contribution status, evidence, what was not verified, and the next action.

For the suite map, read `~/.agents/skills/oss-contributor/SKILL.md`. For large-codebase reconnaissance, read `~/.agents/skills/large-codebase-navigator/SKILL.md`.
