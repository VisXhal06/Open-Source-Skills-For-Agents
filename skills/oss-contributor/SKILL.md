---
name: oss-contributor
description: "Use when contributing to open source or working inside a large, unfamiliar company codebase: choosing an issue, understanding repo architecture, reproducing a bug, making a maintainer-grade fix, writing tests, preparing a PR, responding to review, or contributing across frontend, backend, database, DevOps, server, security, or system design. Use this whenever the user mentions open source, OSS, upstream, a PR, an issue, a monorepo, a legacy codebase, maintainers, or contributing to a project they did not write, even if they do not name a specific role."
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
  suite: "oss-contributor"
---

# OSS Contributor

This is the front door to maintainer-grade open-source contribution. It turns a vague "help me contribute" request into a small, evidence-backed change that a maintainer can review without babysitting it.

The suite is built around one principle from the research: **open source rewards verified uncertainty reduction, not code volume.** Maintainers do not need more plausible patches. They need reproduction steps, root cause, a focused diff, tests that fail before the fix and pass after it, and a contributor who responds well to review.

## The contract

When this skill is invoked:

1. **Classify the work.** Is this repo reconnaissance, issue selection, bug reproduction, implementation, review, documentation, infrastructure, security, or release work?
2. **Load the smallest useful sub-skill.** Read its `SKILL.md` before acting. Do not stop at routing.
3. **State the mode in one line.** Example: "Using `large-codebase-navigator` to map the request path, then `oss-senior-engineer` to make the smallest tested fix."
4. **Produce an artifact.** A contribution brief, issue comment, reproduction, failing test, patch, PR description, review response, or runbook.
5. **Leave evidence.** Commands run, tests passed, screenshots, logs, benchmarks, and known unknowns.
6. **Leave one clear next action.** The user should know exactly what to do next.

A routing table is not a deliverable. If the request is real work, load the first skill and begin its workflow.

## Non-negotiables

- Read `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `GOVERNANCE.md`, `AGENTS.md`, and any AI-contribution policy before writing code.
- Search for an existing issue, PR, discussion, or duplicate before opening a new one.
- Comment on the issue and get a signal from a maintainer before doing large work. Small typo fixes usually do not need this; architecture changes always do.
- Keep the diff focused. Do not reformat, rename, or refactor unrelated code in the same PR.
- Preserve public behavior unless the issue explicitly asks to change it. Treat public APIs, schemas, CLI flags, config keys, and error messages as contracts.
- Add a regression test when fixing a bug. If the repository has no test harness, explain what you ran manually and why.
- Disclose AI assistance when the project asks, and never claim you manually verified something you did not.
- Do not fabricate logs, test output, benchmarks, issue links, maintainer quotes, or reproduction steps.
- Never send a security report publicly. Follow `SECURITY.md` and private disclosure.
- Do not spam maintainers, mass-open PRs, or submit generated changes to many repositories at once.

## The maintainer lens

Read the project the way a maintainer reads it.

| Maintainers value | Maintainers reject |
| --- | --- |
| A clear problem and a minimal reproduction | "AI fixed it" with no evidence |
| A small diff with one logical change | A drive-by rewrite or mass formatting change |
| A test that would have caught the bug | A test that only asserts the mock was called |
| Respect for existing conventions | A new dependency for a five-line problem |
| Compatibility and migration notes | A silent breaking change |
| Responsive, humble review replies | Argument, force-pushes during review, or entitlement |
| Documentation and changelog updates | "Tests are obvious" with no tests |

The best contribution is often not code. High-leverage contributions include reproducing a hard bug, triaging duplicates, improving error messages, adding a missing test, fixing docs, making CI faster, and reviewing someone else's PR.

## Choose the right contribution

Score candidate issues on five dimensions, 1–5:

| Dimension | Question |
| --- | --- |
| Impact | Does this unblock users, fix a real bug, or reduce maintainer burden? |
| Evidence | Can I reproduce it and prove the fix? |
| Scope | Can I finish it in one focused PR? |
| Signal | Is a maintainer receptive, or is it stale, assigned, or controversial? |
| Fit | Do I understand the area and can I maintain the change? |

Prefer an issue with a score of 18+ and a clear owner. Avoid "good first issue" labels that are years old, issues with an unmerged competing PR, and issues that require a design decision you are not prepared to defend.

## Contribution workflow

### 0. Pre-flight

- Read the policies and the README.
- Check the default branch, release process, test commands, and supported versions.
- Search issues, PRs, and discussions for the exact symptom.
- Identify the maintainer or area owner. Do not guess.

### 1. Understand before changing

Use `large-codebase-navigator` for any repository you did not write, especially a monorepo, a legacy service, or a large company codebase. Produce a short map before touching code:

- entry points and runtime boundaries
- the path the bug travels
- data stores and external services
- invariants and conventions
- the smallest safe change point
- the verification path

### 2. Reproduce

Write a minimal reproduction with environment, version, steps, expected behavior, actual behavior, logs, and a traceback. Remove secrets and customer data. If you cannot reproduce, say so and ask for the missing detail instead of guessing.

### 3. Find the root cause

Use `systematic-debugging`. Distinguish the symptom from the cause. Check whether the bug is in the code, configuration, dependency, documentation, or deployment. Read the tests around the area; they encode invariants.

### 4. Design the smallest fix

State:

- what changes
- what does not change
- compatibility impact
- failure modes
- rollback path
- how you will prove it

If the fix needs a public API change, migration, or cross-team decision, use `oss-system-designer` and write an RFC/ADR before coding.

### 5. Implement with evidence

Use `oss-senior-engineer`. Prefer test-first. Keep commits coherent. Run the repository's formatter, linter, typecheck, unit tests, integration tests, and build, not just the one test you added.

### 6. Prepare the PR

Include:

- linked issue
- problem
- approach
- tests and evidence
- screenshots or recordings for UI changes
- performance numbers for hot paths
- breaking changes and migration notes
- AI disclosure if required
- known limitations

### 7. Respond to review

Treat review as collaborative debugging, not a verdict on your identity. Answer each comment, ask when unclear, keep changes scoped, and avoid force-pushing unless the project asks for it. If a maintainer declines the change, thank them and leave the branch in a clean state.

## Role routing

| Request | Load | Artifact |
| --- | --- | --- |
| "I don't understand this repo", monorepo, legacy code, huge codebase | `large-codebase-navigator` | Codebase brief and change map |
| "Fix this issue", "make a PR", "review my patch" | `oss-senior-engineer` | Reproduction, failing test, patch, PR |
| "Design this feature", API change, architecture, RFC | `oss-system-designer` | RFC/ADR, interface design, rollout plan |
| UI, UX, accessibility, design system, frontend | `oss-uiux-frontend` | UI change, states, a11y and visual evidence |
| API, service, auth, concurrency, integrations | `oss-backend` | Service change, contract tests, failure plan |
| Schema, migration, query, index, data integrity | `oss-database` | Migration plan, query evidence, rollback |
| CI, containers, IaC, release, runtime, server, on-call | `oss-devops-server` | Pipeline or runtime change, runbook |
| Vulnerability, authz, secrets, dependency risk | `oss-security` | Threat model, private report, fix/advisory |
| "What should I work on?", find issues, identify owners or mentors | `oss-issue-scout` | Scored issue list, issue brief, contribution pipeline |
| "I want GSoC", org selection, proposal, mentor outreach | `gsoc-strategist` | Org scorecard, contribution proof plan, proposal |

Also compose existing skills when they fit better: `test-driven-development`, `systematic-debugging`, `verification-before-completion`, `requesting-code-review`, `receiving-code-review`, `documentation-system`, `launch-readiness`, `codebase-playbook`, `understand`, and the `design-engineering` suite.

## Contribution brief

Before a non-trivial patch, write this into the issue or a local note:

```markdown
## Contribution brief

**Issue:**
**Project and version:**
**Problem:**
**Reproduction:**
**Expected vs actual:**
**Root cause:**
**Smallest change:**
**Invariants to preserve:**
**Compatibility / migration:**
**Tests and evidence:**
**Risks and unknowns:**
**AI assistance:**
**Next action:**
```

## Quality gates

Do not call the work done until these are true:

- The reproduction fails on the current code and passes after the fix.
- The new test is meaningful and would fail without the change.
- Existing tests, lint, typecheck, and build pass.
- The diff contains no unrelated changes.
- Public behavior and error messages are preserved or intentionally documented.
- Docs, changelog, and examples are updated when the project expects it.
- No secrets, customer data, or private URLs are in the patch.
- The PR description tells a reviewer how to verify the change.

## Stop conditions

Stop and ask, rather than guessing, when:

- the issue is assigned, closed, or has an active competing PR
- the project has no clear AI policy and the change is substantial
- the fix requires a security disclosure
- the license is incompatible with the proposed dependency or copied code
- the change requires a public API break or data migration without an owner
- you cannot reproduce the problem or run the tests
- the maintainer has explicitly declined the direction

## Output format

End with:

```markdown
### Contribution status
- Mode:
- What I changed:
- Evidence:
- What I did not verify:
- Next action:
```

Keep the summary short. The patch and the evidence are the real deliverable.
