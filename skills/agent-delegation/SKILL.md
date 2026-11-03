---
name: agent-delegation
description: Use when giving work to AI agents, splitting a project into subtasks, running agents in parallel, or reviewing and integrating agent output.
license: MIT
compatibility: opencode
metadata:
  version: "1.1.0"
---

# Agent Delegation

Agent output quality is roughly:

```text
task clarity × context quality × verification strength
```

A vague task produces plausible code that is hard to verify. A precise task with the wrong context produces confident code in the wrong place. A precise task with no verification produces "done" claims you cannot trust.

## Suite integration

Part of the senior-dev suite. `senior-dev-os` can load this skill automatically when work is handed to AI agents; direct invocation works too. If the router loaded it, produce context-complete task packets and review gates, not just a partition of the work.

## When to delegate

Delegate when the work is:

- Bounded and independently verifiable
- Mostly implementation against a known pattern
- Parallelizable without shared files
- Repetitive but judgment-light
- Easy to review as a diff

Do not delegate when the work is:

- A product decision or an ambiguous trade-off
- A security-sensitive change without a clear design
- A cross-cutting refactor with no stable interface
- A debugging task where the cause is unknown and the search space is wide
- A change that requires credentials, production access, or customer data

Use `brainstorming` and `writing-plans` before delegating the first task. An agent should not be the first place a decision is made.

## When the team already exists

If the work is build-and-ship rather than a one-off delegation, use `build-ship-team` instead of inventing the roster. It ships a named team with fixed contracts, lanes, and gates:

```text
ship-lead → scout → architect → builder → verifier → reviewer → shipper
```

Use this skill for the packet design, ownership rules, and review discipline inside a slice. Use `build-ship-team` for the whole change, the lane choice, and the release decision.

## AI-era guardrails

AI is an amplifier: it increases throughput and, without strong controls, instability. DORA's 2025 research found both effects. Keep the guardrails explicit:

- **Spec before generation.** The task packet is the contract.
- **Curate context.** Give the agent the files, conventions, and examples it needs; do not dump the repo.
- **Small batches.** One bounded change per task; review is still the bottleneck.
- **Verify independently.** The agent's "done" is a status update, not evidence.
- **Keep judgment human.** Architecture, security trade-offs, product scope, and irreversible decisions stay with the owner.
- **Measure rework.** Track how often agent output is rejected, reopened, or rolled back. Speed without stability is not progress.
- **Protect secrets and production.** No credentials, customer data, or unrestricted deploy access in the agent's context.

## The task packet

Every delegated task gets a packet. Use `templates/task-packet.md`.

| Field | Purpose |
| --- | --- |
| ID and title | Stable reference for the board and handoff |
| Goal | One sentence, outcome not activity |
| Why | The user or business reason |
| Context | Files to read, docs, prior decisions, related tasks |
| Scope | What is in and explicitly out |
| Allowed paths | Files or directories the agent may change |
| Acceptance criteria | Testable statements, not adjectives |
| Verification | Exact commands and manual checks |
| Constraints | Style, performance, security, dependencies |
| Deliverable | Diff, commit, report, or artifact |
| Stop conditions | When to stop and ask instead of guessing |
| Handoff | What to report back and where |

### Good vs bad task

| Bad | Why | Better |
| --- | --- | --- |
| "Build the dashboard" | No scope, no acceptance, no boundaries | "Add a `/dashboard` route that shows the last 10 orders for the signed-in user; use the existing `OrderTable`; tests for empty, loading, and error states; do not change the API" |
| "Fix the tests" | No failure, no root cause | "Test `checkout.spec.ts:42` fails with `timeout waiting for #pay`; reproduce it, find the root cause, fix it without changing the test's intent, run the checkout suite" |
| "Refactor auth" | Cross-cutting, high risk | "Extract `getSession()` from `auth.ts` into `session.ts`; keep the public exports unchanged; all auth tests must pass" |
| "Make it faster" | No metric | "Reduce `/api/search` p95 from 800 ms to under 300 ms on the seeded dataset; do not change the response shape; include before/after measurements" |

## Decompose the work

### 1. Start from vertical slices

A slice delivers a user-visible outcome across the stack. A layer task ("build all models") creates integration risk and long feedback loops.

### 2. Build a dependency graph

List tasks and edges:

```text
schema → repository → API → UI → E2E
                 ↘ email job
```

Anything with an arrow must be serialized unless the interface is fixed first.

### 3. Size each task

A good agent task is usually:

- One module or one vertical slice
- One to three files
- 30–90 minutes of agent work
- Reviewable in under 15 minutes

If it is larger, split by behavior or boundary, not by file count.

### 4. Partition by file ownership

Two agents must not edit the same file at the same time. Shared files include:

- Database schema and migrations
- Routers and route tables
- Shared types and interfaces
- Configuration and environment files
- Package manifests and lockfiles
- Design tokens and global styles

Serialize these. Give one agent ownership of the shared file and have others depend on it.

### 5. Fix interfaces before parallel work

For parallel tasks, define the contract first:

- Function signatures
- API request and response shapes
- Event names and payloads
- Database schema
- Error codes

Then agents can implement against the contract independently.

### 6. Add an integration task

Parallel work needs an owner for the seams:

- Wire modules together
- Run the full suite
- Resolve conflicts
- Verify the acceptance criteria end to end
- Update docs

Without an integration task, parallel agents produce pieces that do not compose.

## Parallel execution

Use isolated worktrees or branches:

```text
git worktree add ../project-task-01 -b task/01-schema
git worktree add ../project-task-02 -b task/02-api
```

Rules:

- One agent per worktree.
- One owner per file.
- No agent merges to main.
- The coordinator reviews and merges in dependency order.
- Each agent reports the commit or diff, commands run, and blockers.
- The coordinator runs the verification again after integration.

If the harness supports subagents, use `dispatching-parallel-agents` for independent work and `subagent-driven-development` for plan execution.

## Review gates

Review in this order:

### 1. Spec compliance

- Does the diff do what the packet asked?
- Is anything out of scope?
- Are the acceptance criteria met?
- Were the allowed paths respected?

### 2. Correctness

- Are error paths handled?
- Are permissions enforced?
- Are inputs validated?
- Are edge cases covered by tests?
- Is the change idempotent where needed?

### 3. Quality

- Does it follow the repository conventions?
- Is it the simplest change that works?
- Are names clear?
- Is dead code removed?
- Are logs useful and free of secrets?

### 4. Verification

Run the commands yourself. Do not accept "all tests pass" without output.

Use `requesting-code-review`, `receiving-code-review`, and `verification-before-completion`.

## Status protocol

Each agent reports:

```text
Task: <ID>
Status: done | blocked | needs review
Changed: <files>
Verified: <commands and results>
Not done: <anything incomplete>
Risks: <what could break>
Next: <the next task or decision>
```

Keep a board in `docs/tasks/board.md` or `TASKS.md`. Use `templates/board.md`.

Board columns:

- Backlog
- Ready
- In progress
- Review
- Blocked
- Done

A task is not "done" because an agent says so. It is done when the acceptance criteria and verification pass.

## Handoff between agents

When a task spans sessions or agents, write a handoff:

- What was the goal
- What changed
- What was verified
- What is still open
- What the next agent should read first
- What not to touch

Use the `handoff` skill for the full format.

## Anti-patterns

| Pattern | Consequence | Fix |
| --- | --- | --- |
| "Build the whole app" | Unreviewable, unrecoverable | Vertical slices and task packets |
| Parallel agents on shared files | Merge conflicts and lost work | Partition or serialize |
| No acceptance criteria | "Done" is subjective | Testable statements |
| No verification commands | Agent claims are unverified | Exact commands in the packet |
| Context dump | Agent misses the relevant files | Curated context with links |
| No stop conditions | Agent invents requirements | Stop and ask when ambiguous |
| Trusting the diff without running it | Broken code merges | Coordinator runs the gates |
| No integration task | Pieces do not compose | Assign an integration owner |

## Red flags

- The task touches more than one module and has no interface defined.
- Two tasks list the same file in allowed paths.
- The acceptance criteria use words like "better", "clean", or "modern".
- The agent is asked to make a product or security decision.
- The task has no verification command.
- The task is estimated in hours but has no demo.
- The agent reports "done" with no diff or command output.

## Related skills

- `writing-plans` to produce the plan before decomposition
- `dispatching-parallel-agents` for independent tasks
- `subagent-driven-development` for plan execution
- `requesting-code-review` and `receiving-code-review`
- `verification-before-completion`
- `handoff`
