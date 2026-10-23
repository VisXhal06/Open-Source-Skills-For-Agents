# Verdict Rules

Return exactly one verdict:

- `SHIP`
- `SHIP WITH CONDITIONS`
- `BLOCK`

## Decision Table

| Condition | Low tier | Medium tier | High tier |
| --- | --- | --- | --- |
| All required evidence present; no regression; no high risk; rollback tested; budget met | SHIP | SHIP | SHIP with named human sign-off |
| Non-critical evidence missing | SHIP WITH CONDITIONS | SHIP WITH CONDITIONS | BLOCK |
| Critical evidence missing | SHIP WITH CONDITIONS | BLOCK | BLOCK |
| Regression below floor | SHIP WITH CONDITIONS | BLOCK | BLOCK |
| Delta negative but CI crosses zero | SHIP WITH CONDITIONS, monitor | SHIP WITH CONDITIONS, monitor | BLOCK |
| Sample under 20 paired tasks | SHIP WITH CONDITIONS | BLOCK | BLOCK |
| Open high-severity risk | BLOCK | BLOCK | BLOCK |
| Rollback steps or owner missing | BLOCK | BLOCK | BLOCK |
| Rollback not tested | SHIP WITH CONDITIONS | SHIP WITH CONDITIONS | BLOCK |
| Cost or latency budget breached | SHIP WITH CONDITIONS | SHIP WITH CONDITIONS | BLOCK |
| Claim is not falsifiable | SHIP WITH CONDITIONS | BLOCK | BLOCK |
| Judge-human agreement below 0.80 | SHIP WITH CONDITIONS; add human review | SHIP WITH CONDITIONS; add human review | BLOCK |

## SHIP

All of these must be true:

- the claim names a target slice and a guardrail
- every required row for the change class is present
- the regression delta is at or above the floor
- the confidence interval does not show a clear regression
- no open high-severity risk
- rollback has steps, an owner, and a test
- budget is within limits
- for high tier, a named human has signed off

## SHIP WITH CONDITIONS

Every condition needs:

- a name
- an owner
- an expiry or review date
- a monitoring signal
- a concrete next action

Examples:

```text
Condition: policy-edge slice is missing.
Owner: retrieval-owner.
Expiry: 2026-10-30.
Signal: weekly eval delta on policy-edge set.
Next action: add 12 policy-edge cases and rerun the gate.
```

`SHIP WITH CONDITIONS` is not available for high-tier changes. A high-tier change either ships clean or blocks.

## BLOCK

BLOCK is mandatory when any of these is true:

- required measurement is missing on a medium or high-tier change
- the regression floor is breached
- a high-severity risk is unresolved
- rollback is undefined or untested on a high-tier change
- the claim cannot be falsified
- the evidence is underpowered for the tier
- the change class is unknown

When blocking, say:

1. the smallest action that unblocks
2. who owns it
3. how the next review will verify it

## Edge Cases

### Quality up, cost up sharply

Do not silently ship. Compare against the budget and the product value. If the budget is exceeded, use `SHIP WITH CONDITIONS` only at low or medium tier, with a named cost owner and a rollback trigger.

### Quality flat, cost down

A cost win can ship if the regression floor is met and the hard slice did not regress. Record the lack of quality gain explicitly; do not claim an improvement.

### Quality up overall, hard slice regressed

Treat it as a regression unless the hard slice is irrelevant to the release. Name the slice and the mitigation.

### Model upgrade with missing fallback

At medium tier, `BLOCK` if the fallback is critical for the change class. At low tier, `SHIP WITH CONDITIONS` with a tested fallback deadline.

### Retrieval change with no index rollback

`BLOCK` at medium or high tier. A retrieval change without a rollback path is an unowned production risk.

### Tool change with no injection test

`BLOCK` at medium or high tier. Tool output is an instruction-injection surface.

### Conflicting evidence

List both results, state which one is more trustworthy and why, and ask `advisor` for a red-team review if the verdict is contested.

### Missing claim

If the user cannot state what should improve and what must not regress, the change is not ready for a gate. Route to `brainstorming` or `writing-plans`.
