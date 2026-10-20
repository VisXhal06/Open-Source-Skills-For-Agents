---
name: subagents
description: Use when a goal or project can be split across specialized subagents, or when you need to choose which expert roles should research, build, review, or document the work.
license: MIT
compatibility: opencode
metadata:
  version: "1.1.0"
---

# Subagents

Use subagents to put the right kind of expertise on each part of the work, not to split a task into arbitrary chunks. A specialist with a clear brief and a narrow ownership boundary produces better work than four generalists with the same prompt.

## Suite integration

Part of the senior-dev suite. `senior-dev-os` can load this skill automatically when work needs specialist roles or parallel ownership; direct invocation works too. If the router loaded it, produce the roster, briefs, dependency graph, and review gates, not just a list of agent names.

## How this fits the other skills

| Skill | Answers |
| --- | --- |
| `goal` | What outcome are we pursuing? |
| `advisor` | What do the experts think about the decision? |
| `subagents` | Which specialist roles should do the work, and in what order? |
| `agent-delegation` | What exactly goes in each task packet, and how is it reviewed? |
| `dispatching-parallel-agents` | How do we run independent tasks in parallel? |
| `subagent-driven-development` | How do we execute an implementation plan with subagents? |

Do not use `subagents` as a synonym for "spawn many agents." The point is specialization and clean ownership.

## When to use subagents

Use them when:

- The work has genuinely different kinds of expertise.
- Several independent research questions can run in parallel.
- A build has separable modules with stable interfaces.
- You want independent review from a different perspective.
- A large goal needs research, product, architecture, implementation, testing, security, and docs.

Do not use them when:

- The task is small and sequential.
- The decision is ambiguous and needs one owner.
- The work has no stable interface to split against.
- Agents would edit the same files.
- You cannot verify the output.
- The task requires credentials or production access you are not prepared to grant.

## In OpenCode

Use the `subagent` tool. Each call starts a fresh context, so put the full brief in the prompt.

- `explore` for fast codebase reconnaissance and file discovery.
- `general` for multi-step research, implementation, review, or documentation.
- Launch multiple subagent calls in parallel only when their outputs are independent.
- Give each subagent a disjoint file scope or a read-only review scope.
- Pass the `sessionID` when you need to continue the same subagent conversation.
- Do not let subagents make product, security, or irreversible decisions. They prepare evidence and options; the human decides.

## The roster

| Role | Mission | Inputs | Output | Gate |
| --- | --- | --- | --- | --- |
| Goal lead | Keep the outcome and scope coherent | Goal brief, constraints | Clarified goal, decisions | Human approval |
| Domain researcher | Find evidence, methods, costs, and failure modes | Questions, sources | Research memo with citations | Source quality |
| Product strategist | Define users, wedge, scope, and success metrics | Research, constraints | Product brief, non-goals | Human approval |
| Architect | Define boundaries, interfaces, and technical shape | Brief, constraints | ADR, interface contracts | Review by implementers |
| Implementer | Build one module or vertical slice | Task packet, contracts | Diff, tests, report | Code review and verification |
| Test engineer | Design tests and find edge cases | Acceptance criteria, risks | Test plan, automated tests | Coverage of critical risks |
| Security reviewer | Find auth, data, and abuse risks | Design, diff, threat model | Findings by severity | No unresolved criticals |
| Data analyst | Define and check metrics | Questions, instrumentation | Metric definitions, queries | Reproducible numbers |
| UX designer | Simplify flows and check accessibility | Users, journeys | Flow, states, copy | Usability and accessibility review |
| SRE or DevOps | Make deploy, observe, and rollback safe | Architecture, release plan | Runbook, dashboards, rollout | Rollback tested |
| Docs writer | Make the work usable by the next person | Decisions, APIs, runbooks | README, ADR, guide | Docs match behavior |
| Red team | Attack the plan or implementation | Plan, diff, assumptions | Failure modes, test cases | Findings triaged |
| Integrator | Own the seams and the final verification | All outputs, contracts | Merged result, verification report | Full gate passes |

A person or agent can hold more than one role on a small task. On a large task, separate the builder from the reviewer.

## Step 1: Decompose by specialization

Ask: **what kind of expertise does this part need?**

Bad split by file count:

```text
Agent 1: files 1–5
Agent 2: files 6–10
```

Better split by specialization and outcome:

```text
Researcher: what do freelancers hate about current invoicing tools?
Architect: define the invoice and payment boundaries.
Implementer A: invoice creation and PDF generation.
Implementer B: payment link and webhook handling.
Test engineer: edge cases for totals, tax, retries, and partial payment.
Security reviewer: authorization and webhook verification.
Integrator: wire the slices and run the full gate.
```

## Step 2: Choose the minimum number

| Situation | Agents |
| --- | --- |
| Small, sequential, ambiguous | 1 |
| Independent research questions | 2–3 researchers |
| Build with stable interfaces | 2–3 implementers plus an integrator |
| High-stakes decision | 2–4 advisor lenses |
| Implementation plus independent review | 1 builder, 1 reviewer |
| Large multi-workstream goal | Serial phases of 2–4 agents, not all at once |

More agents increase coordination cost, merge risk, and token spend. Add an agent only when it has a distinct mission and a clean ownership boundary.

## Step 3: Write the subagent brief

Every subagent gets a brief. Use `templates/subagent-brief.md`.

| Field | Content |
| --- | --- |
| Role | The specialist identity and lens |
| Mission | One sentence, outcome not activity |
| Why | The goal or decision this serves |
| Context | Files, docs, research, prior decisions |
| Inputs | What it receives and can rely on |
| Deliverable | Memo, diff, test plan, review, runbook |
| Constraints | Scope, style, tools, time, security |
| Acceptance criteria | Testable statements |
| Verification | Exact commands or evidence |
| Stop conditions | When to ask instead of guessing |
| Reporting | The format and where to write it |

A good brief sounds like:

> You are the security reviewer for the invoice payment flow. Read `AGENTS.md`, the payment ADR, and the diff in `src/payments/`. Your job is to find authorization gaps, webhook forgery, replay, and data exposure. Do not change code. Return findings by severity with file and line references, and a clear ship / do-not-ship recommendation.

A bad brief sounds like:

> Review the code and make it secure.

### Context budget

Give each subagent only the context it needs for its mission:

- The goal, the decision, and the acceptance criteria.
- The files and interfaces it owns.
- The conventions and commands that apply.
- The prior decisions that constrain it.
- The verification it must run.

Do not paste the entire repository, every meeting note, or all prior agent outputs. Excess context increases cost and can reduce the quality of the result. Link to deeper documents instead of copying them.

## Step 4: Draw the dependency graph

```text
research → product decision → architecture → contracts
                                      ↓
                          implementation A ─┐
                          implementation B ─┼→ integration → verification → docs
                          tests ────────────┘
```

Rules:

- Research precedes decisions.
- Contracts precede parallel implementation.
- Shared files are serialized.
- Integration follows parallel work.
- Documentation follows verified behavior.
- A reviewer is independent from the builder.

## Step 5: Orchestrate

### Research fan-out

Spawn independent researchers with the same question frame but different lenses:

- Market and competitors
- User pain and willingness to pay
- Technical feasibility
- Cost and operations

Then synthesize. Do not concatenate four memos and call it research.

### Build pipeline

Use a pipeline when each stage changes the artifact:

```text
architect → implementer → test engineer → security reviewer → integrator
```

### Parallel implementation

Use parallel implementation only when:

- Interfaces are fixed.
- File ownership is disjoint.
- Each agent has its own worktree or branch.
- An integrator owns the merge and full verification.

### Review panel

Give the same artifact to independent reviewers with different lenses. Ask for findings first, not a summary. Synthesize disagreements.

### Red team

Ask one agent to assume the plan fails and explain why. Ask another to find the cheapest evidence that would disprove the plan.

## Step 6: Own the files

- One owner per file at a time.
- Shared files are serialized: schema, migrations, routers, types, config, lockfiles, global styles.
- Each agent works in its own worktree or branch.
- No agent merges to main.
- The integrator resolves conflicts and reruns the gate.

If two briefs list the same file in their allowed paths, stop and fix the plan.

## Step 7: Aggregate

Synthesize; do not average.

For research:

- What is consistent across sources?
- Where do sources disagree?
- What is the quality of the evidence?
- What decision does the evidence support?

For implementation:

- Does the integrated result meet the acceptance criteria?
- Do the interfaces match?
- Are there duplicate or conflicting changes?
- Does the full gate pass?

For review:

- Which findings are critical, high, medium, low?
- Which are in scope?
- What is the recommended action?

## Step 8: Review and verify

Review in this order:

1. **Mission fit:** did the subagent do the assigned job?
2. **Scope:** did it stay inside the allowed paths?
3. **Correctness:** does the evidence or diff hold up?
4. **Quality:** does it follow the repo conventions?
5. **Verification:** run the commands yourself.

An agent's claim of "done" is a status update, not evidence. Use `verification-before-completion`.

## Example roster: freelance invoicing SaaS

| Phase | Agents | Output |
| --- | --- | --- |
| Discover | Domain researcher, product strategist | Pain points, competitors, pricing, wedge |
| Decide | Architect, security advisor, finance advisor | ADR, auth and payment boundaries, unit economics |
| Build | Implementer A (invoices), Implementer B (payments), test engineer | Two slices and tests |
| Review | Security reviewer, red team | Findings and test cases |
| Integrate | Integrator | Merged result, full gate |
| Launch | SRE, docs writer | Runbook, rollback, changelog |

Do not run all phases at once. Run them in order, with two to four agents active at a time.

## Common mistakes

| Mistake | Consequence | Fix |
| --- | --- | --- |
| Generalist agents for specialist work | Generic output | Assign explicit roles and lenses |
| Splitting by file count | No coherent outcome | Split by specialization and deliverable |
| Too many agents | Coordination cost, conflicts | Minimum viable roster |
| No integrator | Pieces do not compose | Assign an integration owner |
| Overlapping file ownership | Merge conflicts and lost work | One owner per file |
| Parallel work without contracts | Interfaces drift | Fix interfaces first |
| Concatenating reports | Noise, no decision | Synthesize and resolve |
| Trusting "done" | Broken merge | Verify independently |

## Related skills

- `goal` for the outcome
- `advisor` for specialist counsel
- `agent-delegation` for task packets and review gates
- `dispatching-parallel-agents` for parallel execution
- `subagent-driven-development` for plan execution
- `handoff` for context transfer
