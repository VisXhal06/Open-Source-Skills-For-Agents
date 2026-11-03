# Handoff Protocol

A handoff is a file, not a speech. The next agent reads the file, not the previous agent's transcript.

## Why

Agent sessions compact, crash, and expire. A handoff that lives only in conversation is lost. A handoff on disk survives a new session, a new model, and a new tool.

## The handoff file

Write `.ship/handoff.md` at the end of a session, or when passing work to another agent.

```text
# Handoff — <outcome>

## State
Lane: fast | standard | full
Gate: G0 | G1 | G2 | G3 | G4 | G5
Slice: <n> of <total>

## What was the goal
<one sentence, user terms>

## What changed
<files and commits>

## What was verified
<commands and results, or NOT RUN>

## What is still open
<findings, gaps, decisions waiting on a human>

## What the next agent should read first
<paths, in order>

## What not to touch
<files, interfaces, decisions already settled>

## Rulings
<decision — why — cost if wrong>

## Next action
<the single next step>
```

## The status contract

Every worker returns this, and writes the long form to its report file:

```text
Task: <slice or gate>
Status: done | done_with_concerns | needs_context | blocked
Changed: <files>
Verified: <commands and results>
Not done: <anything incomplete>
Risks: <what could break>
Next: <the next action or decision>
```

| Status | Meaning | Lead's move |
| --- | --- | --- |
| `done` | Acceptance criteria met, tests run. | Verify. |
| `done_with_concerns` | Work is complete, but the worker flagged a risk. | Read the concern; resolve it before review if it is about correctness or scope. |
| `needs_context` | The worker is missing information. | Provide it and re-dispatch the same task. |
| `blocked` | The worker cannot proceed. | Diagnose: context, capability, task size, or plan defect. Change something before retrying. |

Never accept `done` without the verification line. `done` with an empty `Verified` is `done_with_concerns` at best.

## Handoff rules

- **Hand over files, not history.** The next agent gets paths and a summary, not a pasted transcript.
- **Name the authority.** The brief is the authority; the plan is its argument. Say which one wins when they conflict.
- **Record rulings.** A decision made without a record dies with the session.
- **Say what not to touch.** The fastest way to lose work is a fresh agent "cleaning up" a settled interface.
- **One next action.** A handoff with five next steps is a backlog, not a handoff.
- **Include the diff range.** `git diff <base>..<head>` is the review surface.
- **Mark evidence versus claim.** If it was not run, say `NOT RUN`.

## After compaction

Trust the files and `git log` over memory:

1. Read `.ship/ledger.md`.
2. Read `.ship/handoff.md`.
3. Run `git log --oneline -20` and `git status`.
4. Read the current gate's artifact.
5. Resume at the first gate that is not passed.

Do not re-dispatch a slice that the ledger says is complete unless the code is missing from `git log`.
