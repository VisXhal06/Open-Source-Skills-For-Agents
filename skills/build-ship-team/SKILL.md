---
name: build-ship-team
description: "Use when you need to build and ship a change fast with a coordinated team of specialist agents: recon, architecture, implementation, independent verification, review, and release. Works in OpenCode and Claude Code."
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
---

# Build-Ship Team

A small, named team that takes a change from "we should build this" to "it is verified and shipped" without the two failure modes of agent work: confident code nobody checked, and process so heavy it ships nothing.

The team is deliberately seven roles. Most work uses three. The full team exists for changes that can hurt you: auth, money, data, public APIs, migrations, and production deploys.

## The team

| Role | Mission | Writes code | Default lane |
| --- | --- | --- | --- |
| `ship-lead` | Frame the outcome, pick the lane, route work, hold the ledger, make the ship call | No, except trivial glue | Always |
| `scout` | Read the repo and return a context brief: stack, patterns, commands, blast radius, unknowns | No | Unknown repo, or > 4 files |
| `architect` | Shape the smallest design: interfaces, slice order, file ownership, test strategy | Plan only | One-way door, or > 3 files |
| `builder` | Implement one vertical slice with tests and a report | Yes | Always |
| `verifier` | Run the real gates and report evidence, pass/fail per gate | No | Always |
| `reviewer` | Independent review for correctness, security, regressions, and UI quality | No | Risky diff, or before release |
| `shipper` | Turn a verified diff into a release: changelog, PR, deploy steps, rollback | Release files only | Deploying, or opening a PR |

Role contracts live in `references/team-contracts.md`. Gates live in `references/gates.md`. Tool mapping lives in `references/tool-mapping.md`.

## Pick the lane before you pick the team

Do not run seven agents on a one-line fix. Pick the smallest lane that can still prove the change works.

| Lane | Use when | Team | Time box |
| --- | --- | --- | --- |
| **Fast** | One file, obvious change, reversible, no data or auth | `ship-lead` + `verifier` (lead implements) | 15–30 min |
| **Standard** | Feature slice, 2–6 files, existing patterns | `ship-lead` + `builder` + `verifier` | 1–3 hours |
| **Full** | Auth, money, migrations, public API, production, UI redesign | All seven, with `reviewer` mandatory | Half day to multi-day |

Escalate the lane, never silently. If a "fast" change turns out to touch a shared interface, a migration, or an auth path, stop and move to the full lane.

## The loop

Five gates. Each gate produces an artifact in `.ship/`. A gate is passed only when the artifact exists and contains evidence, not a claim.

```text
G0 Frame ──▶ G1 Recon ──▶ G2 Plan ──▶ G3 Build ──▶ G4 Verify ──▶ G5 Ship
                │            │            │            │
                └─ skip if    └─ skip if   └─ repeat    └─ reviewer
                   repo known   trivial       per slice     when risky
```

### G0 — Frame

The lead writes `.ship/brief.md`:

- The outcome in one sentence, in user terms.
- Who it is for and what changes for them.
- Success criteria, testable.
- Non-goals. This is the scope fence.
- Constraints: stack, deadline, compatibility, dependencies, design language.
- The lane and why.
- Open questions. Ask at most three; otherwise state assumptions and proceed.

Stop if the outcome is a product decision nobody has made. Do not let a builder invent the product.

### G1 — Recon

Dispatch `scout` unless the repo is already mapped in this session. The scout returns `.ship/context-brief.md`:

- Stack, package manager, runtime, scripts.
- The exact commands for format, lint, typecheck, test, build.
- Existing patterns to copy, with `file:line`.
- The files the change will touch and the hidden coupling around them.
- Risks, unknowns, and the smallest safe slice.
- For UI work: the existing design language, fonts, tokens, components, and whether the anti-generic gate applies.

The scout is read-only. It does not propose a redesign and does not edit.

### G2 — Plan

Run `architect` when the change crosses more than three files, changes a public interface, touches data, or has more than one plausible shape. It returns `.ship/plan.md`:

- The decision and the reason, in three sentences.
- One-way doors versus two-way doors.
- Exact interfaces: signatures, request/response shapes, schema, events, error codes.
- Ordered vertical slices. Each slice is demoable and independently verifiable.
- One owner per file. Shared files are serialized.
- Test strategy per slice.
- Rollback.
- **Not building.** The list that keeps the diff small.

If the change is obvious, skip the architect and write a five-line plan yourself. Do not skip the file.

### G3 — Build

Dispatch one `builder` per slice. Default to serial. Two builders may run in parallel only when their file sets are disjoint and their interfaces are already fixed.

Every builder dispatch carries:

1. The slice goal and why it matters.
2. Paths to `.ship/brief.md` and `.ship/plan.md`, plus the exact slice number.
3. Files it owns. Nothing outside that set without asking.
4. The verification commands it must run.
5. The report path and the status contract.
6. The stop conditions.

The builder works in small commits, tests the behavior it changed, runs the covering tests, and writes `.ship/reports/slice-N-build.md`. It does not push, merge, deploy, or spawn other agents.

### G4 — Verify

Dispatch `verifier` after every slice. The builder's "tests pass" is a status update, not evidence.

The verifier runs the project's real gates in this order and records the exact command and the key output for each:

1. Install or restore, if dependencies changed.
2. Format check.
3. Lint.
4. Typecheck.
5. Unit tests.
6. Integration tests.
7. Build.
8. End-to-end or smoke test, if the project has one.
9. The acceptance criteria from the brief, checked one by one.

Verdict: `PASS`, `PASS WITH RISKS`, or `FAIL`. A gate that does not exist is reported as `NOT RUN`, never as passed.

### G5 — Review and ship

Dispatch `reviewer` before release when the change touches auth, money, data, a public API, a migration, or UI. The reviewer returns findings by severity with `file:line`, a reason, and a fix. Verdict: `APPROVE`, `APPROVE WITH NITS`, or `REQUEST CHANGES`.

Dispatch `shipper` only when G4 passes and G5 review is not `REQUEST CHANGES`. The shipper produces `.ship/ship.md`:

- What changed and why.
- Evidence: the verification report and review verdict.
- Changelog entry.
- PR title and body.
- Deploy steps, environment changes, and migrations.
- Rollback.
- Post-deploy checks.

The shipper may open a PR. It may not merge to `main`, force-push, or deploy to production without explicit human approval. That is a hard stop, not a permission setting.

## Operating rules

- **One outcome per session.** A session that ships one verified slice beats a session that starts four.
- **Smallest diff that works.** No speculative abstraction, no drive-by refactors, no new dependency without a stated reason.
- **Vertical slices.** Ship across the stack, not one layer at a time.
- **Evidence over claims.** Every "done" carries a command and output, a screenshot, or a test name.
- **Independent verification.** The agent that wrote the code does not certify it.
- **One writer per file.** Parallel agents on shared files is how work disappears.
- **Small commits.** One logical change each. Conventional messages.
- **Stop conditions.** Stop and ask on: an irreversible or destructive operation; a security-sensitive decision; a side effect outside the worktree (merge, push to a shared branch, publish, deploy); or a plan so broken every path is a guess.
- **Rulings, not stalls.** For reversible ambiguity, decide, record the ruling in the ledger with what it costs if wrong, and keep going.
- **No product decisions in the build lane.** If the brief is missing the decision, escalate to the human.
- **Cost discipline.** Use the least capable model that can do the role. Do not run a reviewer on a typo.
- **Do not paste the repo into prompts.** Hand over file paths and the brief.

## Artifacts

Create `.ship/` at the repo root and add it to `.gitignore` unless the user wants an audit trail committed.

```text
.ship/
  ledger.md                  # decisions, rulings, gate status, commits
  brief.md                   # G0
  context-brief.md           # G1
  plan.md                    # G2
  design-record.md           # UI work only
  reports/
    slice-1-build.md
    slice-1-verify.md
    slice-1-review.md
  ship.md                    # G5
```

Templates:

- `templates/brief.md`
- `templates/context-brief.md`
- `templates/slice-plan.md`
- `templates/build-report.md`
- `templates/verification-report.md`
- `templates/review-report.md`
- `templates/ship-checklist.md`

The ledger is the recovery map. After compaction, trust the ledger and `git log` over memory. Append one line per event:

```text
G0 frame: lane=standard — reversible feature slice, no data or auth
G1 recon: 6 files, commands found — see context-brief.md
G2 plan: 3 slices, slice 1 is the walking skeleton
G3 slice 1: built (commits a1b2c3d..d4e5f6a)
G4 slice 1: PASS — 42 unit, 6 integration, typecheck clean
G4 slice 1: ruling — kept existing date lib; cost if wrong: one small swap
G5 review: APPROVE WITH NITS — 2 minors deferred
G5 ship: PR #123 opened; merge waits on human
```

## Fast defaults

These are the defaults that make the team fast rather than ceremonial:

- **Walking skeleton first.** One thin end-to-end path beats three perfect layers.
- **Time box recon.** Ten minutes or thirty steps. Stop when the brief answers the questions.
- **Plan in one page.** If the plan is longer than the diff, it is not a plan, it is a proposal.
- **Batch same-shape work.** Ten identical one-line edits are one builder task, not ten.
- **Verify the slice, not the universe.** Run the covering tests every time; run the full suite at the gate.
- **Review the diff, not the repo.** Point the reviewer at the change range and the brief.
- **Ship behind a flag** when the change is user-visible and the rollback is not obvious.
- **One fix wave.** If review finds issues, send one fix batch, then one scoped re-review. Do not loop forever.

## UI work: the anti-generic gate

Any UI, page, component, or design change must pass the gate in `~/.agents/skills/frontend-design/references/anti-generic-aesthetics.md`.

The short version:

- No Inter, Roboto, Arial, Helvetica, `system-ui`, Poppins, Montserrat, Open Sans, or Lato as the default face.
- No violet, indigo, or purple gradients on white; no blue-to-purple "AI" gradients; no gradient text; no blurred blob heroes; no glass cards on a gradient.
- No centered hero with a pill badge, two-line headline, grey subhead, two buttons, and a gradient blob.
- No three identical feature cards, three-tier pricing with the middle card highlighted, logo clouds, or bento grids as the default structure.
- No pill badge above every heading, one radius for everything, one soft shadow for everything, or hover-lift on every card.
- No fade-and-slide-up on every section, staggered reveals on every list, or cursor-following blobs.
- No "supercharge", "seamless", "unlock", "AI-powered", or "the future of work" as unexamined copy.

The builder writes `.ship/design-record.md` before styling:

```text
Subject:
Audience and job:
Direction (one sentence):
Type: <face> because <reason>
Palette: <4–6 named values> from <source>
Layout logic:
Motion:
Banned defaults avoided:
Exception (only if the brief or brand requires one):
```

The reviewer rejects a UI diff that has no design record, or whose record is a list of trends rather than reasons.

## Tool mapping

The team works in both tools. The names are the same; the mechanics differ.

| Need | OpenCode V2 | Claude Code |
| --- | --- | --- |
| Orchestrator | `ship-lead` primary agent, or the main session | The main session; `ship-lead` subagent for a full plan |
| Launch a worker | `subagent` tool with the agent name | `Agent` tool with `subagent_type` |
| Agent files | `~/.config/opencode/agents/<name>.md` | `~/.claude/agents/<name>.md` |
| Read-only worker | `permissions` with `edit: deny` | `tools` without `Edit`/`Write` |
| Isolated work | git worktree via `using-git-worktrees` | `isolation: worktree` |
| Commands | `~/.config/opencode/commands/ship-team.md` | ask for the agent by name, or a project skill |

Full mapping and invocation examples: `references/tool-mapping.md`.

If a tool has no subagent support, run the roles inline in order. The gates still apply. A solo session that verifies independently is better than a team that does not.

## Handoff contract

Every worker returns this and writes the full version to its report file:

```text
Task: <slice or gate>
Status: done | done_with_concerns | needs_context | blocked
Changed: <files>
Verified: <commands and results>
Not done: <anything incomplete>
Risks: <what could break>
Next: <the next action or decision>
```

The lead reads the report file, not the whole transcript. It records the gate result in the ledger and dispatches the next role.

## Definition of done

A change is done when all of these are true:

- The acceptance criteria in `.ship/brief.md` are met, one by one.
- The build report names the tests that cover the change.
- The verifier ran the real gates and recorded output.
- The reviewer approved, or every open finding has a recorded ruling.
- The diff is within the agreed file set, or the expansion is explained.
- The changelog or release note is written.
- Rollback is known.
- The ledger says who did what, with commits.
- UI work has a design record that survives the anti-generic gate.

If any line is missing, the change is not done. It is in progress with a known gap. Say which.

## Related skills

Load these when the work reaches them, not before:

- `brainstorming` and `goal` to frame an unclear outcome.
- `writing-plans` and `executing-plans` for a larger plan.
- `subagent-driven-development` for a strict per-task review loop.
- `agent-delegation` for task packets, ownership, and parallel work.
- `dispatching-parallel-agents` for independent parallel slices.
- `test-driven-development` and `systematic-debugging` inside the build.
- `verification-before-completion` and `code-change-verification` at G4.
- `requesting-code-review` and `receiving-code-review` at G5.
- `launch-readiness` and `llm-release-gate` for production and LLM changes.
- `finishing-a-development-branch` and `handoff` when the session ends.
