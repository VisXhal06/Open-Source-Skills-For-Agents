# Gates

A gate is a decision with evidence. If the evidence is missing, the gate is not passed. "Looks good" is not evidence.

## G0 — Frame

**Question.** Do we know what outcome we are buying, and what we are not buying?

**Pass when.**
- One sentence names the outcome in user terms.
- Success criteria are testable.
- Non-goals are written.
- Constraints are written: stack, deadline, compatibility, dependencies, design language.
- The lane is chosen and justified.
- Every open question is either answered or recorded as an assumption with a cost.

**Artifact.** `.ship/brief.md`

**Fail signs.** The outcome is an activity ("build a dashboard") not a result; success is an adjective ("better", "modern"); no non-goals; the lane is "full" because nobody decided.

## G1 — Recon

**Question.** What is actually here, and what will this change break?

**Pass when.**
- Stack and commands are exact, not guessed.
- The patterns to copy are named with `file:line`.
- The blast radius is mapped.
- The unknowns are named.
- For UI, the existing design language is captured.

**Artifact.** `.ship/context-brief.md`

**Fail signs.** "Standard Next.js setup" with no commands; no test command; no mention of the shared file the change will touch; a redesign proposed during recon.

## G2 — Plan

**Question.** Is this the smallest shape that can ship, and can two people build it without colliding?

**Pass when.**
- The decision and reason fit in three sentences.
- One-way doors are marked.
- Interfaces are exact.
- Slices are vertical and demoable.
- Every file has one owner.
- Test strategy and rollback exist.
- The **not building** list exists.

**Artifact.** `.ship/plan.md`

**Fail signs.** A layer plan ("all models, then all APIs"); two slices own the same file; no interface for parallel work; a plan longer than the diff; no rollback.

## G3 — Build

**Question.** Does the slice work, and is the diff reviewable?

**Pass when.**
- The slice meets its acceptance criteria.
- The covering tests exist and pass.
- The diff stays inside the owned file set, or the expansion is explained.
- Commits are small and named.
- The report contains commands and output.

**Artifact.** `.ship/reports/slice-N-build.md`

**Fail signs.** "Done" with no commands; unrelated refactors; a new dependency with no reason; tests that assert nothing; a UI diff with no design record.

## G4 — Verify

**Question.** Can someone other than the author reproduce the result?

**Pass when.**
- Every available gate has a result: install, format, lint, typecheck, unit, integration, build, e2e.
- Missing gates are marked `NOT RUN`, not passed.
- Acceptance criteria are checked one by one.
- The verdict is `PASS`, `PASS WITH RISKS`, or `FAIL`.
- Risks are named with impact and likelihood.

**Artifact.** `.ship/reports/slice-N-verify.md`

**Fail signs.** "All tests pass" with no output; a skipped gate reported as green; the author verifying their own code; a flaky test ignored; a manual check with no steps or result.

## G5 — Review

**Question.** What did the tests miss, and is it safe to put in front of users?

**Pass when.**
- Spec compliance is checked.
- Correctness, security, data, performance, and test quality are checked.
- UI passes the anti-generic gate and the accessibility basics.
- Findings have severity, `file:line`, reason, and fix.
- The verdict is `APPROVE`, `APPROVE WITH NITS`, or `REQUEST CHANGES`.

**Artifact.** `.ship/reports/slice-N-review.md`

**Fail signs.** Only style nits; no security check on an auth diff; "LGTM" with no evidence; a critical finding marked minor; a UI review with no design record.

## G6 — Ship

**Question.** Can a human approve this release in one read, and can we undo it?

**Pass when.**
- Verification passed.
- Review is not `REQUEST CHANGES`.
- The changelog is written.
- The PR body has what, why, how tested, risk, and rollback.
- Deploy steps, migrations, env changes, and flags are listed.
- Post-deploy checks are listed.
- Rollback is executable.
- Human approval is recorded for merge, force-push, and production deploy.

**Artifact.** `.ship/ship.md`

**Fail signs.** Shipping on a red gate; no rollback; a migration with no backward-compatible step; a production deploy without approval; a risk hidden in the PR body.

## Verdict semantics

| Verdict | Meaning | Next |
| --- | --- | --- |
| `PASS` | Every required gate ran and passed. | Ship, or continue. |
| `PASS WITH RISKS` | Gates passed; named risks remain. | Ship with the risks in the PR, or fix first if a risk is unacceptable. |
| `FAIL` | At least one required gate failed. | Fix, then re-run the failed gate and the gates downstream of it. |
| `NOT RUN` | The gate does not exist or was skipped. | Never count as passed. Say why. |
| `APPROVE` | No blocking findings. | Ship. |
| `APPROVE WITH NITS` | Only minor findings. | Ship, or fix nits if cheap. |
| `REQUEST CHANGES` | At least one critical or important finding. | One fix batch, one scoped re-review. |
| `BLOCK` | A security, data, or release risk the team cannot accept. | Human decision. |

## Evidence rules

- A command result is evidence only with the command and the output.
- A screenshot is evidence only with the state that produced it.
- A test is evidence only if it would fail when the behavior breaks.
- A manual check is evidence only with steps, expected result, and actual result.
- A review is evidence only with a diff range and a verdict.
- A claim without one of the above is a status update. Label it as one.
