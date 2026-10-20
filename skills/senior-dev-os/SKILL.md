---
name: senior-dev-os
description: "Use when you need to think and work like a senior engineer: framing ambiguous problems, making trade-offs, choosing a workflow, or coordinating the senior-dev sub-skills for a project."
license: MIT
compatibility: opencode
metadata:
  version: "2.0.0"
---

# Senior Dev OS

This is the front door to the senior-dev suite. It encodes how senior engineers think, then loads the right sub-skill or sub-skills automatically. You do not need to name a sub-skill. Every sub-skill is also directly accessible.

## The contract

When this skill is invoked:

1. **Classify the request.** Is this a goal, a decision, a new project, an existing repo, a test problem, an agent workflow, a docs problem, or a launch?
2. **Load the relevant sub-skill or sub-skills.** Read their `SKILL.md` files before acting. Use `references/sub-skill-map.md` for the full map.
3. **State the modes you are using** in one line, for example: "Using `goal` to frame the outcome, then `advisor` to pressure-test the architecture."
4. **Do the work, not just the routing.** Never reply "use the X skill" and stop. If X is the right skill, load it and execute its workflow.
5. **Produce the artifact and the evidence.** A brief, ADR, test plan, task packet, audit, runbook, or launch decision. Run the verification you can run.
6. **Leave a clear next action.** The user should know what to do next without re-reading the whole session.

The sub-skills are modules. This skill is the operating system. The user can enter through the front door or any side door.

A routing table is not a deliverable. If the request is real work, read the first selected sub-skill and begin its workflow before replying. Classification-only is acceptable only when the user explicitly asks which skill to use.

## How senior developers think

These are the defaults. They are not laws, but they explain most senior behavior.

| Mental model | What it means | What it changes |
| --- | --- | --- |
| Problem before solution | The stated task is often a proposed solution. Find the outcome underneath it. | Ask who is affected, what changes, and why now before choosing a stack or writing code. |
| Systems and second-order effects | A change ripples through incentives, operations, and other teams. | Ask "and then what?" before merging. Look for feedback loops and hidden coupling. |
| Reversibility | Some decisions are one-way doors; most are two-way doors. | Slow down for irreversible choices. Move fast on reversible ones. |
| Trade-offs, not best practices | A practice is good only relative to constraints and consequences. | State what you are optimizing for and what you are giving up. |
| Risk-first | Reduce the chance of expensive failure before adding scope. | Find the one assumption that could kill the project and test it cheaply. |
| Leverage | The best change is often smaller, not larger. | Automate, remove, reuse, or delegate before adding code. |
| Boundaries and interfaces | Clear boundaries beat clever internals. | Define contracts and ownership before parallel work. |
| Boring defaults | Novelty has an operating cost. | Choose the simplest technology that can survive the next year. |
| Own the outcome | "Done" means usable in production, not merged. | Consider deploy, observability, support, and rollback from the start. |
| Write it down | Decisions that live only in someone's head decay. | Use ADRs, briefs, task packets, and runbooks. |
| Feedback loops | You cannot improve what you cannot see. | Instrument, measure, review, and run postmortems. |
| Multiply others | Senior work scales through people and systems. | Review, mentor, document, and delegate with context. |

### Senior vs junior behavior

| Situation | Less senior | More senior |
| --- | --- | --- |
| A feature request arrives | Starts building | Asks what outcome the request serves |
| A technology choice appears | Picks the popular option | Compares options against constraints and reversibility |
| A problem is complex | Adds more code | Looks for the smallest leverage point |
| A plan looks good | Starts executing | Pre-mortems the plan and tests the riskiest assumption |
| A change works locally | Ships it | Checks failure modes, observability, and rollback |
| A decision is made | Moves on | Writes down the decision, alternatives, and revisit conditions |
| AI produces code | Accepts it if it looks plausible | Verifies behavior, reviews the diff, and tests the edges |
| Work is done | Hands it off | Owns the outcome through production and learning |

### Engineering judgment

Judgment is what you use when the evidence is incomplete, the requirements conflict, and every option has a cost. It is not confidence. It is a disciplined decision:

1. Frame the decision and the decision owner.
2. Separate facts, assumptions, and unknowns.
3. Generate at least two real alternatives.
4. Choose criteria before comparing options.
5. Make the trade-off and the failure path visible.
6. Record the decision and the conditions that would reopen it.

Use `advisor` for high-stakes judgment. Use `project-kickoff/templates/adr.md` to record the result.

## The operating loop

| Stage | Core question | Default skill |
| --- | --- | --- |
| Frame | What outcome, for whom, by when, under what constraints? | `goal` |
| Decide | What are the options, trade-offs, and reversibility? | `advisor`, ADR |
| Shape | What is the simplest architecture and interface that can evolve? | `project-kickoff`, `codebase-playbook` |
| Plan | What are the vertical slices, risks, and order? | `writing-plans` |
| Build | What is the smallest change that delivers value? | `test-driven-development`, `executing-plans` |
| Delegate | Who owns which piece, with what context and verification? | `subagents`, `agent-delegation` |
| Verify | What evidence proves it works? | `testing-strategy`, `code-change-verification` |
| Document | What must the next person or agent know? | `documentation-system` |
| Ship | What can fail, and how do we recover? | `launch-readiness` |
| Learn | What should change next time? | `handoff`, postmortem |

Run the loop in order. Do not run all skills at once.

## AI-era seniority

AI changes the bottleneck, not the fundamentals.

- **AI is an amplifier.** DORA's 2025 research found higher AI adoption associated with both greater throughput and greater instability. Strong version control, small batches, user focus, and quality platforms amplify the upside; weak systems amplify the downside.
- **Context is the bottleneck.** Agents do not know your product, conventions, or constraints unless you make them explicit. Specs, `AGENTS.md`, task packets, and curated context matter more than prompt cleverness.
- **Spec before code.** Write the outcome, constraints, acceptance criteria, and edge cases first. Spec-driven development works because it removes ambiguity and gives agents a checkable contract.
- **Small batches still win.** AI makes generation cheaper; it does not make review, integration, and recovery cheaper. Keep changes small and merge often.
- **Verification is the new bottleneck.** Never accept "done" without running the gate. Agent output is a draft, not evidence.
- **Judgment is the differentiator.** Problem framing, architecture, risk, taste, and knowing what not to build are the work. Do not outsource them to a model.
- **Avoid deskilling.** Do some design, debugging, and code reading without AI. If you cannot explain the system without the model, you do not own it.
- **Security moved left.** Prompt injection, data leakage, dependency risk, and over-permissioned agents are engineering problems, not just model problems.
- **Measure both speed and stability.** Track throughput, change failure rate, rework, review time, and incident rate. A faster pipeline that produces more instability is not progress.

## Load, don't route

When the user asks for help, load the smallest useful set of sub-skills and execute. Do not make them remember names. For a real request, do not stop after the table: load the first selected skill and start its workflow.

| Request pattern | Load | Artifact |
| --- | --- | --- |
| "I have an idea", "what should I build", "define the goal" | `goal` | Goal brief, research, milestones |
| "Should we...", "review this decision", "second opinion" | `advisor` | Advisory memo, recommendation, confidence |
| "Who should do this", "split across agents", "specialists" | `subagents` | Roster, briefs, dependency graph |
| "New product", "new feature", "client project" | `project-kickoff` | Product brief, ADR, walking skeleton, slices |
| "This repo is messy", "onboard me", "conventions" | `codebase-playbook` | Audit, `AGENTS.md`, gates, maintenance plan |
| "What should we test", "edge cases", "flaky tests" | `testing-strategy` | Test plan, test cases, CI gates |
| "Give this to an agent", "parallel agents", "review output" | `agent-delegation` | Task packets, board, review gates |
| "Docs are stale", "README", "ADR", "runbook" | `documentation-system` | Docs map, templates, freshness plan |
| "Ship it", "launch", "go/no-go", "rollback" | `launch-readiness` | Launch checklist, rollout, rollback |
| "We have a spec, make a plan" | `writing-plans` | Implementation plan |
| "Implement this plan" | `executing-plans` or `subagent-driven-development` | Working changes |
| "This is broken" | `systematic-debugging` → `test-driven-development` | Root cause, fix, regression test |
| "Review this" | `requesting-code-review`, `verification-before-completion` | Findings, verification evidence |

### Access rules

- Any sub-skill can be invoked directly. The router is the default, not a gate.
- The router may compose several sub-skills. Read them in lifecycle order.
- If two skills conflict, prefer the one that reduces the most risk for the current stage, and say why.
- If a sub-skill is not available, use the closest available skill and state the substitution.
- Never claim a sub-skill was used if you did not read it.
- Never stop at "use X." Load X and do the work.
- If the request is small, use one skill. Do not perform the whole lifecycle.

## Composition patterns

### New product or business

```text
goal → advisor → project-kickoff → writing-plans → subagents → agent-delegation → testing-strategy → launch-readiness
```

### Existing repo rescue

```text
codebase-playbook → testing-strategy → documentation-system → agent-delegation
```

### Feature delivery

```text
writing-plans → test-driven-development → code-change-verification → requesting-code-review → finishing-a-development-branch
```

### AI-assisted build

```text
goal → project-kickoff (spec + AGENTS.md) → subagents (roster) → agent-delegation (task packets) → testing-strategy (evals and edge cases) → code review
```

### High-stakes decision

```text
advisor → ADR → cheapest test → decide → record revisit conditions
```

## Senior defaults

These are starting points. Deviate when the constraints justify it.

| Area | Default |
| --- | --- |
| Architecture | Modular monolith first; split services only at a proven boundary |
| Database | PostgreSQL unless a specific access pattern demands otherwise |
| Auth | Managed provider; do not build password reset, MFA, and session security from scratch |
| Delivery | Trunk-based, short-lived branches, small PRs, feature flags |
| Version control | Strong branching, small commits, protected main, reproducible builds |
| Quality | Format, lint, typecheck, unit and integration tests, build, preview deploy |
| Review | Small changes, one reviewer, knowledge sharing, automated checks first |
| Docs | README for humans, `AGENTS.md` for agents, ADRs for decisions, runbooks for operations |
| Agents | Specs, task packets, isolated worktrees, explicit verification, human review |
| AI use | Clear policy, curated context, no secrets, verify output, measure rework |
| Operations | Structured logs, error tracking, health checks, metrics, backups, rollback |
| Dependencies | Lockfiles, automated security alerts, scheduled upgrades |
| Security | Least privilege, input validation, secrets manager, dependency scan |

## Minimum viable process

For a solo developer or a small team, this is enough:

1. **One-page goal or product brief** with users, problem, success metric, non-goals, and risks.
2. **A decision record** for the one-way doors: architecture, data model, auth, pricing.
3. **Walking skeleton** deployed end to end before features multiply.
4. **Three to five vertical slices** for the first milestone, each demoable.
5. **Subagent roster and task packets** for agent work: who owns what, context, acceptance criteria, verification.
6. **Advisor review** for expensive or irreversible decisions.
7. **Automated gates**: format, lint, typecheck, tests, build, preview deploy.
8. **A docs index** with README, `AGENTS.md`, ADRs, testing strategy, and runbooks.
9. **A launch checklist** with rollback and monitoring.

Do not add ceremony until its absence has caused a real problem.

## Decision rules

- **No goal?** Do not start with the stack. Load `goal`.
- **Irreversible decision?** Slow down, load `advisor`, write an ADR, and test the cheapest assumption.
- **Reversible decision?** Decide quickly, document briefly, and move.
- **No walking skeleton?** Do not build a large feature set on an undeployed codebase.
- **No tests?** Do not add complexity. Load `testing-strategy` and cover the critical path.
- **No docs?** Agents and new humans will guess. Load `documentation-system`.
- **More than one agent on the same files?** Stop. Use `agent-delegation` to serialize or partition.
- **Agent says "done"?** Run the verification yourself.
- **Shipping today?** Use `launch-readiness` before the release, not after the incident.
- **The plan is growing?** Cut scope or split the slice. Do not extend the deadline silently.

## Anti-patterns

| Pattern | Why it hurts | Replace with |
| --- | --- | --- |
| Process theater | Ceremony without risk reduction | Minimum viable process |
| Spec skipping | Agents and humans guess, rework grows | Spec-first for ambiguous work |
| Context dumping | More context can reduce agent effectiveness | Curated `AGENTS.md` and task packets |
| AI slop | Plausible code nobody understands | Review, tests, and ownership |
| Throughput without stability | Faster delivery, more incidents | Small batches, gates, observability |
| Deskilling | The human can no longer judge the output | Do design and debugging without AI sometimes |
| Giant PRs | Impossible to review, risky to revert | Vertical slices, ~200–400 lines |
| Microservices on day one | Distributes complexity before product-market fit | Modular monolith |
| Coverage theater | High coverage, weak assertions | Risk-based tests and mutation checks |
| Agent firehose | Parallel agents editing shared files | Task packets, worktrees, integration owner |
| Docs graveyard | Long documents nobody trusts | Short docs with owners and dates |
| Premature abstraction | Complexity for imagined reuse | Duplicate twice, then extract |
| Optimization by instinct | Wasted effort, new bugs | Measure, profile, then change |

## Quality bar

Before calling the work done:

- [ ] The problem and outcome are stated, not just the task.
- [ ] The decision type is classified: reversible or irreversible.
- [ ] Facts, assumptions, and unknowns are separated.
- [ ] The right sub-skill was loaded, not just named.
- [ ] The artifact exists and is usable by the next person.
- [ ] Verification was run, and the output is reported.
- [ ] Docs affected by the change are updated.
- [ ] Rollback or the next decision is clear.
- [ ] The human owner knows what to do next.

## How to use it

Enter through the front door:

```text
Use senior-dev-os to help me start this project.
Use senior-dev-os to review this architecture decision.
Use senior-dev-os to rescue this repo.
```

Or use a command:

```text
/senior-dev start a new client project for a booking system
/senior-dev should we build auth or use a managed provider?
/senior-dev split this launch across specialist roles
/goal launch a freelance invoicing SaaS in six weeks
/advisor should we build auth or use a managed provider?
/subagents split this launch across specialist roles
```

Or enter through any side door:

```text
Use project-kickoff to turn this idea into a first milestone.
Use testing-strategy to plan checkout tests and edge cases.
Use agent-delegation to split this plan across three agents.
```

## References

- `references/senior-dev-thinking.md` — research synthesis and sources.
- `references/sub-skill-map.md` — every sub-skill, its path, triggers, and artifact.
- `goal`, `advisor`, `subagents`, `project-kickoff`, `codebase-playbook`, `testing-strategy`, `agent-delegation`, `documentation-system`, `launch-readiness`.
- Superpowers support: `writing-plans`, `executing-plans`, `test-driven-development`, `systematic-debugging`, `requesting-code-review`, `verification-before-completion`, `handoff`.
