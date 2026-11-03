# Senior-dev sub-skill map

The router `senior-dev-os` is the front door. Every skill below is also directly accessible. The router loads what it needs; it does not gatekeep.

## Core suite

| Skill | Path | Load when | Produces |
| --- | --- | --- | --- |
| `senior-dev-os` | `~/.agents/skills/senior-dev-os/SKILL.md` | Any whole-project request, ambiguous engineering request, or request to think like a senior engineer | Chosen workflow, composed sub-skills, quality bar |
| `goal` | `~/.agents/skills/goal/SKILL.md` | Defining an outcome, deciding what to build, researching what a goal requires | Goal brief, research summary, milestones, kill criteria |
| `advisor` | `~/.agents/skills/advisor/SKILL.md` | A high-stakes decision, second opinion, red-team review, or specialist panel | Advisory memo, recommendation, confidence, cheapest test |
| `subagents` | `~/.agents/skills/subagents/SKILL.md` | Splitting work by specialization, choosing agent roles, orchestrating parallel work | Roster, briefs, dependency graph, review gates |
| `project-kickoff` | `~/.agents/skills/project-kickoff/SKILL.md` | Starting a product, feature, or client project | Product brief, ADR, walking skeleton, vertical slices, first milestone |
| `codebase-playbook` | `~/.agents/skills/codebase-playbook/SKILL.md` | A repo needs conventions, structure, ownership, dependency policy, gates, or an audit | Audit scorecard, `AGENTS.md`, gates, maintenance plan |
| `testing-strategy` | `~/.agents/skills/testing-strategy/SKILL.md` | Deciding what to test at which level, edge cases, coverage, flaky tests, test data | Test plan, test cases, CI gates, flaky-test policy |
| `agent-delegation` | `~/.agents/skills/agent-delegation/SKILL.md` | Giving work to agents, task packets, parallel execution, review and integration | Task packets, board, worktree rules, review gates |
| `documentation-system` | `~/.agents/skills/documentation-system/SKILL.md` | README, `AGENTS.md`, ADRs, API docs, runbooks, changelog, onboarding, stale docs | Docs map, templates, ownership and freshness plan |
| `launch-readiness` | `~/.agents/skills/launch-readiness/SKILL.md` | Preparing to ship, go/no-go, security, observability, rollback, support | Launch checklist, rollout plan, rollback, post-launch checks |

## Support skills

| Skill | Path | Load when | Produces |
| --- | --- | --- | --- |
| `writing-plans` | `~/.agents/skills/writing-plans/SKILL.md` | An approved spec needs a multi-step implementation plan | Implementation plan |
| `executing-plans` | `~/.agents/skills/executing-plans/SKILL.md` | Executing a plan inline | Working changes |
| `subagent-driven-development` | `~/.agents/skills/subagent-driven-development/SKILL.md` | Executing a plan with independent tasks and subagents | Delegated execution |
| `test-driven-development` | `~/.agents/skills/test-driven-development/SKILL.md` | Implementing a feature or fix | Failing test, minimal implementation, refactor |
| `systematic-debugging` | `~/.agents/skills/systematic-debugging/SKILL.md` | A bug, test failure, or unexpected behavior | Root cause, fix, regression test |
| `requesting-code-review` | `~/.agents/skills/requesting-code-review/SKILL.md` | Completing a task or preparing to merge | Review request and evidence |
| `receiving-code-review` | `~/.agents/skills/receiving-code-review/SKILL.md` | Responding to review feedback | Verified changes or reasoned disagreement |
| `verification-before-completion` | `~/.agents/skills/verification-before-completion/SKILL.md` | About to claim work is done or passing | Verification output |
| `code-change-verification` | `~/.agents/skills/code-change-verification/SKILL.md` | After runtime, test, build, or generated-code changes | Full project gate output |
| `finishing-a-development-branch` | `~/.agents/skills/finishing-a-development-branch/SKILL.md` | Implementation is complete and tests pass | Merge, PR, or cleanup decision |
| `handoff` | `~/.agents/skills/handoff/SKILL.md` | Session ending, context limit, or passing work to another agent | Handoff document |
| `using-git-worktrees` | `~/.agents/skills/using-git-worktrees/SKILL.md` | Isolated feature work or parallel agents | Worktree or branch |
| `dispatching-parallel-agents` | `~/.agents/skills/dispatching-parallel-agents/SKILL.md` | Two or more independent tasks | Parallel execution plan |
| `build-ship-team` | `~/.agents/skills/build-ship-team/SKILL.md` | Building and shipping fast with a named team and evidence gates | Frame, lane, dispatch order, verified release |

### When to use the team instead of a single skill

`build-ship-team` is the packaged team: `ship-lead`, `scout`, `architect`, `builder`, `verifier`, `reviewer`, `shipper`. Use it when the request spans more than one role and must end in a verified, shippable change.

| Request shape | Use |
| --- | --- |
| One narrow idea or unclear outcome | `goal` |
| A plan with independent tasks | `writing-plans` + `subagents` |
| A change that must be built, verified, and shipped | `build-ship-team` |
| A production or LLM release decision | `launch-readiness` / `llm-release-gate` |

## Access rules

1. **Direct access is supported.** The user can name any skill. The router is the default, not a requirement.
2. **The router loads, it does not point.** If `project-kickoff` is needed, read its `SKILL.md` and execute it. Do not reply "use project-kickoff."
3. **Compose in order.** Read skills in lifecycle order, not all at once.
4. **Use the smallest set.** A small request gets one skill. A whole project gets a composition.
5. **State what was loaded.** One line: "Using `goal` then `advisor`."
6. **Respect the risk.** For irreversible decisions, load `advisor` and write an ADR. For reversible decisions, move faster.
7. **Verify.** Loading a skill is not evidence. Run the checks the skill requires.
8. **No phantom usage.** Never claim a skill was used if its file was not read.

## Dependency order

```text
goal
  → advisor
  → project-kickoff
  → writing-plans
  → subagents
  → agent-delegation
  → test-driven-development / executing-plans
  → testing-strategy / code-change-verification
  → requesting-code-review / verification-before-completion
  → documentation-system
  → launch-readiness
  → handoff
```

`codebase-playbook` can be loaded at any point to fix the repo foundations. `systematic-debugging` inserts before implementation when something is broken.

## Artifact map

| Artifact | Owner skill | Typical path |
| --- | --- | --- |
| Goal brief | `goal` | `goals/<slug>-<date>.md` |
| Advisory memo | `advisor` | `advisory/<slug>-<date>.md` |
| Subagent roster | `subagents` | `docs/agents/roster.md` |
| Product brief | `project-kickoff` | `docs/product-brief.md` |
| Architecture decision | `project-kickoff` | `docs/adr/0001-<decision>.md` |
| Roadmap | `project-kickoff` | `docs/roadmap.md` |
| Repo audit | `codebase-playbook` | `docs/codebase-audit.md` |
| Agent instructions | `codebase-playbook` | `AGENTS.md` |
| Test plan | `testing-strategy` | `docs/testing-strategy.md` |
| Task packets | `agent-delegation` | `docs/tasks/<id>.md` |
| Task board | `agent-delegation` | `docs/tasks/board.md` |
| Docs index | `documentation-system` | `docs/README.md` |
| Runbook | `documentation-system` | `docs/runbooks/<operation>.md` |
| Launch checklist | `launch-readiness` | `docs/launch/<release>.md` |

## Loading pattern

```text
1. Read the router (this skill) when the request is broad.
2. Classify the request with the table in SKILL.md.
3. Read the selected skill file(s).
4. Read the project's `AGENTS.md`, goal brief, and relevant docs.
5. Execute, produce the artifact, and verify.
6. Report which skills were used and what evidence exists.
```
