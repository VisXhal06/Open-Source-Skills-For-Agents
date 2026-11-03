---
title: Build Ship Team
aliases:
  - Build and Ship Team
  - Fast Build Team
  - Ship Team
type: reference
created: 2026-11-03
updated: 2026-11-03
tags:
  - opencode
  - claude-code
  - agents
  - skills
  - workflow
  - shipping
---

# Build Ship Team

A named team of seven specialist agents that takes a change from "we should build this" to "it is verified and shipped" — without the two usual failure modes of agent work: confident code nobody checked, and process so heavy it ships nothing.

The team is one skill plus seven agent definitions, installed globally for both OpenCode and Claude Code.

- Skill: `~/.agents/skills/build-ship-team/`
- OpenCode agents: `~/.config/opencode/agents/`
- Claude Code agents: `~/.claude/agents/`
- Commands: `/ship-team` and `/build-fast`

## The roster

| Role | Mission | Writes code | When to use |
| --- | --- | --- | --- |
| `ship-lead` | Frame the outcome, pick the lane, route work, hold the ledger, make the ship call | No, except trivial glue | Always |
| `scout` | Read the repo and return a context brief | No | Unknown repo, or > 4 files |
| `architect` | Shape the smallest design and slice order | Plan only | One-way door, or > 3 files |
| `builder` | Implement one vertical slice with tests and a report | Yes | Always |
| `verifier` | Run the real gates and report evidence | No | Always |
| `reviewer` | Independent review for correctness, security, regressions, UI | No | Risky diff, or before release |
| `shipper` | Changelog, PR, deploy steps, rollback, post-deploy checks | Release files only | Deploying or opening a PR |

The full contracts are in `references/team-contracts.md` inside the skill. Each role has one job and a hard stop; a role doing another role's job is a defect because it hides that role's gate.

## Three lanes

Do not run seven agents on a one-line fix. Pick the smallest lane that can still prove the change works.

| Lane | Use when | Team | Time box |
| --- | --- | --- | --- |
| **Fast** | One file, obvious, reversible, no data or auth | `ship-lead` + `verifier` (lead implements) | 15–30 min |
| **Standard** | Feature slice, 2–6 files, existing patterns | `ship-lead` + `builder` + `verifier` | 1–3 hours |
| **Full** | Auth, money, migrations, public API, production, UI redesign | All seven, `reviewer` mandatory | Half day to multi-day |

Escalate the lane, never silently. If a "fast" change turns out to touch a shared interface, a migration, or an auth path, stop and move to the full lane.

## The gates

```text
G0 Frame ──▶ G1 Recon ──▶ G2 Plan ──▶ G3 Build ──▶ G4 Verify ──▶ G5 Ship
```

| Gate | Question | Artifact |
| --- | --- | --- |
| G0 Frame | Do we know what outcome we are buying, and what we are not? | `.ship/brief.md` |
| G1 Recon | What is actually here, and what will this break? | `.ship/context-brief.md` |
| G2 Plan | Is this the smallest shape, and can two people build it without colliding? | `.ship/plan.md` |
| G3 Build | Does the slice work, and is the diff reviewable? | `.ship/reports/slice-N-build.md` |
| G4 Verify | Can someone other than the author reproduce the result? | `.ship/reports/slice-N-verify.md` |
| G5 Review + Ship | What did the tests miss, and can a human approve and undo it? | `.ship/reports/slice-N-review.md`, `.ship/ship.md` |

A gate passes only with evidence: a command and output, a screenshot, or a test name. "Looks good" is not evidence. A gate that does not exist is `NOT RUN`, never passed.

## Artifacts

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

Add `.ship/` to `.gitignore` unless you want the audit trail committed. The ledger is the recovery map: after compaction, trust the ledger and `git log` over memory.

## How to use it

### OpenCode

Switch to the `ship-lead` agent, or run:

```text
/ship-team add passkey login to the existing auth flow
```

For one small slice:

```text
/build-fast fix the empty state on the orders table
```

The lead dispatches `scout`, `architect`, `builder`, `verifier`, `reviewer`, and `shipper` through the `subagent` tool. The workers are also callable directly:

```text
Use the scout subagent to map this repo.
Use the verifier subagent to run the gates on the current diff.
```

### Claude Code

The main conversation is the lead. Ask for a worker by name:

```text
Use the scout agent to map this repo and write .ship/context-brief.md.
Use the builder agent to implement slice 1 from .ship/plan.md.
Use the verifier agent to run the gates on the current diff.
```

`ship-lead` also exists as a subagent for a full frame-and-dispatch plan. Claude Code's depth limit may prevent it from spawning workers from inside a subagent; in that case it returns the dispatch board and the main thread launches them.

Claude Code subagents count against the same usage limits as the main conversation. The team is fast because it is small and evidence-driven, not because subagents are free.

## The anti-generic gate

Any UI work still passes `frontend-design/references/anti-generic-aesthetics.md`. The builder writes `.ship/design-record.md` before styling:

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

The reviewer rejects a UI diff with no design record, or one that is a list of trends rather than reasons.

## Operating rules

- One outcome per session.
- Smallest diff that works. No speculative abstraction, no drive-by refactors.
- Vertical slices, not layers.
- Evidence over claims.
- Independent verification: the author does not certify the work.
- One writer per file.
- Small commits, conventional messages.
- Rulings, not stalls: for reversible ambiguity, decide, record the cost, continue.
- Stop only for an irreversible action, a security decision, a side effect outside the worktree, or a plan that leaves every path a guess.
- No merge to `main`, force-push, or production deploy without explicit human approval.

## Claude Code free use: what is actually legitimate

There is no legitimate unlimited free Claude Code. Claude Code is not included in the Claude Free plan. The paid entry point is Claude Pro at $20/month, or $17/month with the annual discount. Max is $100/month, Ultra $200/month.

Anything that claims unlimited free Claude Code is account sharing, credential abuse, a modified client, or a resold account. Those violate Anthropic's terms and risk a ban. This note does not cover them.

Legitimate zero-cost or low-cost paths:

| Option | What you get | Limit |
| --- | --- | --- |
| **OpenCode + free model** | A Claude Code-like agent with skills, subagents, and commands; the current session runs a free model | Free model availability and rate limits vary |
| **Google Antigravity CLI** | $0 individual plan with agent models, subagents, MCP, skills, slash commands | Basic weekly rate limits |
| **Qwen Code** | Open-source terminal agent; connect a free provider or a local model | Model access and limits depend on the provider |
| **GitHub Copilot Free** | Limited completions and chat, auto model selection | 2,000 completions/month and a limited AI-credit allowance |
| **Local models** | Ollama, LM Studio, vLLM with OpenCode, Aider, or Continue | Hardware-bound; weaker on large repos |
| **Claude Pro** | Real Claude Code with plan usage | $20/month, $17 annual; not free |
| **Student / startup / cloud credits** | Copilot Student, Anthropic or cloud startup credits, Bedrock/Vertex trial credits | Eligibility required; not unlimited |

The practical setup: use the free team in OpenCode for most work, keep a Claude Pro subscription only if Claude Code's model quality is worth $17–20/month, and reserve it for the hard tasks. That is cheaper and more honest than chasing an unlimited free account that does not exist.

## Verification status

| Check | Result |
| --- | --- |
| Skill installed | `~/.agents/skills/build-ship-team` with 4 references and 7 templates |
| OpenCode agents load | 7 of 7 visible in `opencode debug agents` |
| Live routing smoke test | `scout` ran end-to-end on a throwaway repo: found 3 of 8 commands, marked the rest `not found`, wrote `.ship/context-brief.md`, returned the status contract |
| OpenCode commands | `/ship-team` and `/build-fast` present |
| Claude Code agents | 7 of 7 pass `claude plugin validate ~/.claude/agents` |
| Anti-generic gate | Linked from the skill, the builder, the reviewer, and both commands |
| Global skill count | 94 |

*Last verified: 2026-11-03. Live smoke test: `scout` on a throwaway repo.*
