# Review Report — Slice <n>

## Scope

- Diff: `<base>..<head>`
- Brief: `.ship/brief.md`
- Build report: `.ship/reports/slice-<n>-build.md`
- Verification: `.ship/reports/slice-<n>-verify.md`

## Spec compliance

| Requirement | Met? | Evidence |
| --- | --- | --- |
| <criterion> | yes / no / partial | `file:line` |

Out of scope:

- <anything the diff does that the brief did not ask for>

## Findings

### Critical

| # | Location | Finding | Fix |
| --- | --- | --- | --- |
| C1 | `file:line` | <what is wrong and why it matters> | <smallest fix> |

### Important

| # | Location | Finding | Fix |
| --- | --- | --- | --- |
| I1 | `file:line` | | |

### Minor

| # | Location | Finding | Fix |
| --- | --- | --- | --- |
| M1 | `file:line` | | |

## Checks performed

- [ ] Correctness and error paths
- [ ] Boundary and empty states
- [ ] Concurrency / idempotency
- [ ] Authorization and input validation
- [ ] Secrets and logging
- [ ] Injection / SSRF / unsafe deserialization
- [ ] Migration safety and backward compatibility
- [ ] Performance: N+1, unbounded work, indexes
- [ ] Tests would fail if the behavior broke
- [ ] UI: anti-generic gate and design record
- [ ] UI: accessibility, responsive, dark mode
- [ ] Simplicity / YAGNI

## UI gate

- Design record present: yes / no
- Banned defaults found: <list, or none>
- Exception recorded: <if any>
- Verdict: pass / fail

## Verdict

`APPROVE` | `APPROVE WITH NITS` | `REQUEST CHANGES`

## Next

<Ship, fix the blocking findings, or escalate.>
