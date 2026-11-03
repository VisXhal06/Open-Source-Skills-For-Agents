---
description: Think like a senior engineer and load the right senior-dev skills automatically
---

Use the `senior-dev-os` skill for this request: $ARGUMENTS

Act as the front door. Do not merely tell the user to use another skill. Classify the request, read the relevant `SKILL.md` file or files, and execute the workflow. State the skills you loaded in one line, for example: "Using `goal` to frame the outcome, then `advisor` to test the riskiest decision."

## Classify the request

- Outcome, "what should I build", or a new goal → `goal`
- Expensive, contested, or irreversible decision → `advisor`
- Specialist roles, division of work, or parallel ownership → `subagents`
- New product, feature, or client project → `project-kickoff`
- Existing repo, conventions, maintainability, or agent readiness → `codebase-playbook`
- Tests, edge cases, evals, coverage, or flaky tests → `testing-strategy`
- Agent tasks, subtasks, parallel work, or review gates → `agent-delegation`
- README, `AGENTS.md`, ADRs, API docs, runbooks, or onboarding → `documentation-system`
- Shipping, go/no-go, security, observability, or rollback → `launch-readiness`

Support skills, when the work reaches them: `writing-plans`, `executing-plans`, `subagent-driven-development`, `test-driven-development`, `systematic-debugging`, `requesting-code-review`, `receiving-code-review`, `verification-before-completion`, `code-change-verification`, `finishing-a-development-branch`, `handoff`, `using-git-worktrees`, `dispatching-parallel-agents`.

## Rules

- Use the smallest useful set of skills. A small request gets one skill; a whole project gets a composition.
- If more than one applies, load them in lifecycle order: frame → decide → shape → plan → build → verify → document → ship → learn.
- Read each selected skill before acting. Never claim a skill was used if its file was not read.
- Sub-skills are directly accessible. The router is the default entry point, not a gate. If the user names a skill, use it directly.
- Never stop at "use X." If X is right, load X and do the work.
- If the user asks for actual work, read the first selected skill and begin. A classification table alone is not a completed response.
- Classify one-way doors (public API, data model, auth, pricing, data deletion) separately from two-way doors. Spend judgment proportional to reversibility.
- Separate facts, assumptions, and unknowns. For thin evidence, design the cheapest test instead of writing a confident plan.
- Prefer the smallest change with the largest leverage. Keep batches small.
- In the AI era, treat AI as an amplifier: curate context, spec before generation, verify independently, keep judgment human, and measure rework as well as speed.
- Produce the artifact, not just advice. Run the verification you can run and report the output.
- Ask at most three questions when context is missing; otherwise state your assumptions and proceed.
- End with the decision, the evidence, and the next action.

## Senior defaults

- Modular monolith first; split services only at a proven boundary.
- PostgreSQL unless a specific access pattern demands otherwise.
- Managed auth and payments; do not build security primitives from scratch.
- Trunk-based delivery, short-lived branches, small PRs, feature flags.
- Format, lint, typecheck, tests, build, preview deploy as the minimum gate.
- README for humans, `AGENTS.md` for agents, ADRs for decisions, runbooks for operations.
- Strong version control, small batches, observability, and rollback before scale.
- Do not add process until its absence has caused a real problem.

For the full thinking model, read `~/.agents/skills/senior-dev-os/references/senior-dev-thinking.md`. For the sub-skill map, read `~/.agents/skills/senior-dev-os/references/sub-skill-map.md`.
