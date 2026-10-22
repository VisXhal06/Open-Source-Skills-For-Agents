---
name: large-codebase-navigator
description: "Use when a codebase is large, unfamiliar, legacy, monolithic, or owned by another team: mapping a monorepo, tracing a request through services, finding where behavior lives, understanding architecture before a change, or fixing something in a very large company codebase without breaking hidden dependencies. Use this whenever the user says they are lost in a repo, need to understand a large codebase, or must change code they did not write, even if they do not ask for a 'map.'"
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
  suite: "oss-contributor"
---

# Large Codebase Navigator

Large codebases are not read linearly. They are navigated by following a question through boundaries: a route, a job, an event, a CLI command, a database query, or a failing test. The goal is not to understand everything. The goal is to understand **the smallest system that can explain the behavior** and the **blast radius** of changing it.

Use this skill before making a change in a repository you did not write, especially a monorepo, a legacy service, a platform owned by another team, or an open-source project with years of history.

## The rule

Do not start with a global search and start editing. Start with a question and a path.

Bad: "Where is auth handled? Let me grep for `auth`."

Better: "A user with a valid token gets a 403 on `POST /projects`. Trace that request from the route to the authorization check, then identify the smallest change point."

## Workflow

### 0. Define the question and the blast radius

Write one sentence:

```text
I need to know how <behavior> happens so I can <change> without breaking <invariants>.
```

Then classify the change:

| Change type | Blast radius |
| --- | --- |
| Copy, docs, comment | Tiny |
| Local bug fix | One function or module |
| Shared utility change | Every caller |
| API/schema/config change | Every consumer, including external |
| Dependency upgrade | Build, runtime, security, license |
| Cross-service change | Deploy order, compatibility, rollback |
| Data migration | Existing rows, backups, dual-write, rollback |

The bigger the blast radius, the more time goes into mapping and verification, not typing.

### 1. Map the surface

Read, in this order:

1. `README`, `CONTRIBUTING`, `AGENTS.md`, `CODEOWNERS`, `SECURITY.md`, and any `docs/` index.
2. Build and package manifests: `package.json`, `pnpm-workspace.yaml`, `Cargo.toml`, `go.mod`, `pyproject.toml`, `pom.xml`, `build.gradle`, `*.csproj`, `Makefile`, `BUILD.bazel`, `docker-compose.yml`, `Dockerfile`.
3. Top-level directories and the five to ten that carry the domain.
4. CI workflows, deployment config, and environment templates.
5. ADRs, RFCs, runbooks, and migration folders.
6. Test layout and test commands.

Produce a one-page map:

```text
apps/        deployable entry points
services/    independently deployed services
packages/    shared libraries and contracts
infra/       IaC, environments, deploy config
db/          schema, migrations, seeds
docs/        ADRs, runbooks, API docs
```

Do not assume directory names reflect ownership. Check `CODEOWNERS`, git history, and docs.

### 2. Identify the runtime topology

Answer:

- What starts the process? (HTTP server, worker, cron, CLI, queue consumer, browser app)
- What are the external boundaries? (database, cache, queue, object storage, third-party API, auth provider)
- What is deployed together and what is deployed separately?
- Where does configuration come from? (env, config service, feature flags, secrets manager)
- What is the data ownership boundary?
- What is generated, vendored, or copied from another repo?

Draw a small Mermaid diagram if there are more than three moving parts. A diagram is a debugging tool, not decoration.

### 3. Trace one path end to end

Pick a concrete request, event, or command and follow it. Record each hop with file and symbol.

Example path:

```text
HTTP POST /projects
  -> router (apps/api/src/routes/projects.ts)
  -> auth middleware (packages/auth/src/require-user.ts)
  -> project service (apps/api/src/projects/create.ts)
  -> repository (packages/db/src/projects.ts)
  -> Postgres insert + outbox event
  -> worker consumes ProjectCreated
  -> notification service
```

For each hop, capture:

- input and output contract
- error behavior
- authorization check
- transaction boundary
- retry/idempotency behavior
- logs, metrics, and traces
- tests that cover it

If the path is dynamic (dependency injection, reflection, event bus, plugin registry, generated code), say so explicitly. Do not pretend a static search found the whole path.

### 4. Read the tests and the history

Tests are executable documentation of invariants. Read the nearest tests before changing behavior.

Use history to answer "why is it like this?":

```bash
git log --oneline -- path/to/file
git log -S "symbol_or_string" -- path/
git blame -L 40,80 path/to/file
git log --follow -- path/to/renamed_file
git show <commit>
```

Look for reverted changes, incident fixes, compatibility shims, and TODOs with issue links. A weird line often has a reason. Do not delete the reason without understanding it.

### 5. Extract invariants and conventions

Write down what must remain true:

- public API shape, status codes, error messages
- database constraints, indexes, transaction boundaries
- event names and payload schemas
- auth and tenancy rules
- ordering, idempotency, and retry semantics
- performance budgets
- accessibility and browser support
- supported versions and platforms
- generated files and formatting rules

Also capture conventions: naming, error wrapping, logging fields, state management, CSS approach, test style, commit format.

### 6. Choose the smallest change point

Prefer a change that:

- fixes the behavior at the cause, not the symptom
- stays inside one ownership boundary when possible
- preserves public contracts
- is easy to revert
- can be verified with an existing test or a small new one

If the smallest change crosses a boundary, write the boundary contract first. If it requires a shared library change, list every caller and how you checked them.

### 7. Plan verification before editing

Define the evidence now:

- failing test or reproduction
- unit/integration/e2e tests to run
- typecheck, lint, format, build
- manual steps and expected result
- performance or load check
- migration up/down and data check
- feature flag and rollback plan
- reviewer-specific evidence

If you cannot run the full suite, say which parts you ran and which you did not.

### 8. Write the codebase brief

Use this template. Keep it under two pages.

```markdown
# Codebase brief: <question>

## Question
## Scope and non-goals
## Surface map
## Runtime topology
## Traced path
1. ...
## Invariants to preserve
## Conventions
## Smallest change point
## Blast radius
## Verification plan
## Unknowns and assumptions
## Recommended next action
```

## Navigation techniques

| Need | Technique |
| --- | --- |
| Find a file by name | `rg --files`, `fd`, IDE search |
| Find a symbol | IDE go-to-definition, `rg "symbol"`, language server |
| Find call sites | `rg "functionName\\("`, IDE find references |
| Find config usage | `rg "ENV_NAME|configKey"` |
| Find route to handler | Search route string, then middleware chain |
| Find database access | Search table name, ORM model, repository layer |
| Find event flow | Search event name, producer, consumer, schema |
| Find why code exists | `git log -S`, `git blame`, linked issues |
| Find ownership | `CODEOWNERS`, `git shortlog`, team docs |
| Find dead code | No references, no tests, no runtime path; confirm before deleting |
| Find generated code | Header comments, `.gitattributes`, build scripts, `generated/` |
| Find feature flags | Flag SDK calls, config, experiments, rollout docs |

Useful commands:

```bash
rg --files | head -200
rg -n "route|handler|controller" src
rg -n "CREATE TABLE|ALTER TABLE|migration" .
git log --oneline -20
git log -S "oldBehavior" --all -- .
```

## Large-company specifics

In a company codebase, the hardest part is often not the code. It is ownership, process, and hidden coupling.

Check:

- **Ownership:** who approves changes, who is on call, who owns the data?
- **Change management:** RFC, design review, security review, privacy review, release window.
- **Internal platforms:** shared auth, logging, deployment, feature flags, service catalog.
- **Generated code:** API clients, protobuf, GraphQL types, ORM models. Change the source, not the output.
- **Vendored code:** do not patch vendored directories without an upstream plan.
- **Data contracts:** schemas, events, warehouse tables, analytics, downstream consumers.
- **Compliance:** PII, retention, audit logs, access control, regional data rules.
- **Rollout:** canary, feature flag, dark launch, dual-write, backfill, rollback.
- **Incident history:** postmortems explain strange guards and retries.

Do not assume the repo is the whole system. The behavior may live in configuration, a gateway, a feature flag, a cron job, a database trigger, or another service.

## Legacy and archaeology

Legacy code is a record of decisions made under constraints you no longer see. Treat it as evidence.

- Find the oldest and newest commits around the area.
- Look for renamed concepts; search old names.
- Check whether the code is still reachable. Dead code in a monorepo may still be deployed from another entry point.
- Distinguish accidental complexity from compatibility shims.
- Prefer a strangled change (new path behind a flag, old path retained) over a big-bang rewrite.
- If you must rewrite, define behavior parity tests first.

## Red flags

Stop and investigate when:

- the same behavior exists in three places
- a config value changes behavior but is not in the repo
- a "small" change touches a shared package with many callers
- tests are skipped, flaky, or mock the exact thing you need to verify
- the code is generated but has no source
- ownership is unclear
- the change requires a data migration with no rollback
- the issue description and the code disagree

## Composition

- Use `understand` when you need a knowledge graph or onboarding map.
- Use `systematic-debugging` when the question is "why is this broken?"
- Use `codebase-playbook` when the repo needs conventions, `AGENTS.md`, or an audit.
- Use `oss-senior-engineer` after the map to make the change.
- Use `oss-system-designer` if the map reveals an architectural decision.
- Use `oss-database` or `oss-devops-server` when the path crosses data or deployment boundaries.

## Output format

End with:

```markdown
### Navigation result
- Question answered:
- Path traced:
- Invariants found:
- Smallest safe change:
- Evidence still missing:
- Recommended next action:
```

The map is successful when another engineer can make the change without rediscovering the system.
