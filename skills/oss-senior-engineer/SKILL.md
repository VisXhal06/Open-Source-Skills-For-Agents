---
name: oss-senior-engineer
description: "Use when the user wants to fix an open-source issue, make a maintainer-grade pull request, reproduce a bug, add a regression test, review a patch, or respond to code review in a project they do not own. Use this whenever the task involves an upstream issue, PR, patch, maintainer feedback, or contributing a fix, even if the user only says 'help me fix this' or 'make a PR.'"
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
  suite: "oss-contributor"
---

# OSS Senior Engineer

A merged PR is not the goal. The goal is a change a maintainer can trust: the problem is real, the cause is understood, the diff is small, the tests prove the behavior, and the contributor is easy to work with.

This skill is the issue-to-PR operating loop for open source. Use it after `large-codebase-navigator` has mapped an unfamiliar codebase, or directly when the area is already known.

## The senior standard

| Junior move | Senior move |
| --- | --- |
| Starts from the proposed solution | Starts from the user-visible problem and reproduction |
| Changes many files while exploring | Explores in a scratch branch, then produces one focused diff |
| Adds a test that mirrors the implementation | Adds a test that fails for the real bug and passes for the right reason |
| Fixes the symptom | Finds the root cause and checks adjacent paths |
| Ignores compatibility | Lists public behavior, versions, and migration impact |
| Says "works on my machine" | Provides commands, environment, output, and known gaps |
| Treats review as criticism | Treats review as shared debugging |
| Opens five PRs at once | Finishes one, learns the project, then repeats |

## Workflow

### 1. Pick an issue worth doing

Score the issue:

| Signal | Good | Bad |
| --- | --- | --- |
| Status | Open, unassigned, recently discussed | Assigned, stale, closed, locked |
| Reproduction | Clear steps or a failing test | "It doesn't work" with no detail |
| Scope | One behavior, one module | Cross-cutting redesign |
| Maintainer signal | "PRs welcome" or a triage label | "Needs design" with no decision |
| Your fit | You can run and test the area | You cannot build the project |
| Evidence | You can prove the change | Only a guess |

Before committing time, search for duplicates and competing PRs. Read the issue comments, linked discussions, and roadmap. If the issue is ambiguous, ask one precise question with what you have already checked.

### 2. Pre-flight the repository

- Read `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `AGENTS.md`, and the AI policy.
- Find the test, lint, typecheck, format, and build commands.
- Check the supported versions and platforms.
- Check the branch and release model.
- Identify the code owner or most recent author of the area.
- Read the nearest tests and docs before the implementation.

If the project requires an issue-first proposal, write the proposal before coding. If it requires a design doc for non-trivial changes, use `oss-system-designer`.

### 3. Reproduce with the smallest case

Write a reproduction that a maintainer can run:

```markdown
**Environment:** OS, runtime version, package version, commit
**Steps:**
1. ...
**Expected:**
**Actual:**
**Minimal input:**
**Logs / traceback:**
**Regression:** first known bad version, if found
```

Use the smallest input that still fails. Remove secrets, tokens, customer data, and unrelated configuration. If the bug depends on timing, concurrency, data volume, or a platform, say so.

If you cannot reproduce it, do not invent a cause. Ask for the missing detail or write a diagnostic test that narrows the condition.

### 4. Find the root cause

Use `systematic-debugging`:

1. Read the actual error, not just the last line of the stack.
2. Find the first point where the value diverges from the expected value.
3. Check inputs, configuration, dependency versions, and environment.
4. Use `git bisect` when the regression version is unknown and the history is bisectable.
5. Check whether tests encode the old behavior.
6. Write down the cause in one sentence before editing.

A root cause that sounds like "the null check was missing" may still be incomplete. Ask why the value was null, and whether the same path can produce another invalid value.

### 5. Design the smallest fix

Before coding, state:

```text
Cause:
Change:
Not changing:
Compatibility:
Failure modes:
Tests:
Rollback:
```

Prefer:

- a local fix over a framework change
- an existing utility over a new dependency
- a backward-compatible default over a breaking change
- a feature flag over a risky big-bang rollout
- a clear error over silent fallback

If the fix needs an API change, schema migration, or cross-service coordination, stop and use `oss-system-designer`, `oss-database`, or `oss-backend`.

### 6. Test first

Add a failing test that captures the bug. Run it and confirm it fails for the expected reason, not because of a typo or missing fixture.

Then implement until it passes. Add adjacent tests only where the same cause can recur:

- boundary values
- empty/null input
- error path
- concurrency or retry
- backward compatibility
- platform-specific behavior

Avoid tests that:

- assert only that a mock was called
- duplicate the implementation line by line
- depend on sleep instead of a condition
- pass even when the fix is removed

If the project has no tests for the area, add the smallest existing-style test and explain the manual verification.

### 7. Implement in coherent commits

- Keep one logical change per commit.
- Match the project's style, not your personal style.
- Do not reformat unrelated files.
- Do not upgrade dependencies unless the issue requires it.
- Do not edit generated files by hand.
- Update docs, examples, changelog, and types when the project expects it.
- Remove debug prints and temporary files.

### 8. Verify like CI

Run the repository's full gate:

```bash
# use the project's actual commands
<install>
<format check>
<lint>
<typecheck>
<unit tests>
<integration tests>
<build>
```

Also run the specific test and the reproduction. For UI changes, capture before/after screenshots at relevant viewports and themes. For performance changes, include a before/after benchmark with methodology. For migrations, test up and down.

If a check cannot run, say why and what you ran instead. Do not report a check as passing if you only read the code.

### 9. Write the PR

Use this structure:

```markdown
## Problem
What is broken and who is affected?

## Reproduction
Minimal steps, environment, expected vs actual.

## Root cause
The specific cause, with file/symbol references.

## Approach
What changed and why this is the smallest safe fix.

## Tests
Commands run and results. Include the new test and why it would fail without the fix.

## Compatibility
Public API, schema, config, platform, or version impact.

## Screenshots / recordings
For UI changes.

## AI assistance
Disclose per project policy. State what was generated, what you reviewed, and what you verified.

## Checklist
- [ ] Tests added/updated
- [ ] Docs/changelog updated
- [ ] Lint/typecheck/build pass
- [ ] No unrelated changes
- [ ] No secrets or customer data
```

Link the issue with the project's preferred syntax. Keep the description factual. Do not overstate confidence.

### 10. Respond to review

- Reply to every substantive comment.
- Ask for clarification when a comment is ambiguous.
- Make requested changes in small commits unless the project prefers amend/force-push.
- Do not argue about taste; explain trade-offs with evidence.
- If you disagree, state the constraint and propose an alternative.
- If the maintainer declines, thank them, close cleanly, and leave the branch usable.
- If review stalls, wait a reasonable period and ping once with a concise status.

### 11. After merge

- Confirm the release or changelog includes the change if relevant.
- Update your notes and the issue.
- Thank the reviewer.
- If the fix should be backported, follow the project's backport process.
- Turn the experience into a reusable contribution note for the next issue.

## Reviewing someone else's PR

Use `requesting-code-review` and `receiving-code-review` for the full review loop, plus this OSS lens:

- Does the PR solve the linked problem?
- Is the diff scoped and reversible?
- Is there a meaningful test?
- Are public contracts preserved?
- Are error paths and compatibility handled?
- Is the contributor responsive and honest about gaps?
- Is the change maintainable by the project, not just by the author?

Lead with the highest-risk finding. Be specific and kind. Distinguish blockers from suggestions.

## Anti-patterns

- **Drive-by rewrite:** fixing a bug by restructuring the module.
- **Test theater:** a test that passes before and after the fix.
- **Dependency bloat:** adding a package for a tiny utility.
- **Silent break:** changing a default, error message, or schema without documentation.
- **AI slop:** plausible code with no reproduction, no tests, and no understanding.
- **PR spam:** many low-quality PRs to many repos.
- **Maintainer capture:** arguing until the maintainer gives up.
- **Unverified claim:** "all tests pass" without running them.

## Output format

End with:

```markdown
### Contribution report
- Issue:
- Root cause:
- Change:
- Tests and evidence:
- Compatibility:
- Not verified:
- Next action:
```

The best compliment is not "good code." It is "this was easy to review and I trust it."
