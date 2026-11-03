# Verification Report — Slice <n>

## Scope

- Change range: `<base>..<head>`
- Brief: `.ship/brief.md`
- Build report: `.ship/reports/slice-<n>-build.md`

## Gates

| # | Gate | Command | Result | Evidence |
| --- | --- | --- | --- | --- |
| 1 | Install / restore | `<cmd>` | PASS / FAIL / NOT RUN | <key output> |
| 2 | Format check | `<cmd>` | | |
| 3 | Lint | `<cmd>` | | |
| 4 | Typecheck | `<cmd>` | | |
| 5 | Unit tests | `<cmd>` | | |
| 6 | Integration tests | `<cmd>` | | |
| 7 | Build | `<cmd>` | | |
| 8 | E2E / smoke | `<cmd>` | | |

## Acceptance criteria

| Criterion | Check | Result |
| --- | --- | --- |
| <criterion> | <command or manual step> | PASS / FAIL |
| <criterion> | <command or manual step> | PASS / FAIL |

## Reproduction

<For a bug fix: the original failure, the command that reproduced it, and the result after the fix.>

## Flaky or environment notes

- <test name, failure rate, evidence, suspected cause>

## Risks

| Risk | Impact | Likelihood | Notes |
| --- | --- | --- | --- |
| <risk> | low/med/high | low/med/high | |

## Verdict

`PASS` | `PASS WITH RISKS` | `FAIL`

## Next

<Ship, fix the named gate, or escalate.>
