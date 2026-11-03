# Tool Mapping

The team is the same in OpenCode and Claude Code. Only the mechanics differ.

## OpenCode V2

### Agents

Global agents live in `~/.config/opencode/agents/<name>.md`.

```yaml
---
description: Implements one slice with tests
mode: subagent
steps: 60
color: "#4ade80"
permissions:
  - action: subagent
    resource: "*"
    effect: deny
  - action: edit
    resource: "*"
    effect: allow
  - action: shell
    resource: "*"
    effect: allow
  - action: shell
    resource: "git push*"
    effect: deny
---
```

Key fields:

| Field | Use |
| --- | --- |
| `description` | Shown to the model choosing a subagent. Make it a trigger, not a title. |
| `mode` | `primary` for `ship-lead`, `subagent` for everyone else. |
| `model` | `provider/model#variant`. Omit to inherit the parent session. |
| `permissions` | Ordered rules; the last match wins. Put broad rules first. |
| `steps` | Hard cap on model steps. Keeps a worker from touring the repo. |
| `color` | Six-digit hex. UI only. |

### Launching

Ask the primary agent to use a named subagent:

```text
Use the scout subagent to map this repo and write .ship/context-brief.md.
```

Or dispatch explicitly with the `subagent` tool. The parent's `subagent` permissions decide which agents it may launch.

### Commands

`~/.config/opencode/commands/ship-team.md` and `build-fast.md` are available as `/ship-team` and `/build-fast`.

### Worktrees

Use the `using-git-worktrees` skill. One worker per worktree. The lead merges in dependency order.

## Claude Code

### Agents

Global subagents live in `~/.claude/agents/<name>.md`.

```yaml
---
name: builder
description: Implements one slice with tests. Use for a bounded coding task with a clear plan and file set.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
color: green
---

You implement one slice...
```

Key fields:

| Field | Use |
| --- | --- |
| `name` | Required. Must be unique. No `:`. |
| `description` | Required. When Claude should delegate. Keep it short; all descriptions share context. |
| `tools` | Allowlist. Omit `Edit`/`Write` for read-only roles. |
| `disallowedTools` | Denylist. Applied before `tools`. |
| `model` | `sonnet`, `opus`, `haiku`, `fable`, `inherit`, or a full ID. |
| `permissionMode` | `default`, `acceptEdits`, `plan`, etc. Use `plan` for read-only roles if desired. |
| `maxTurns` | Hard cap. |
| `isolation` | `worktree` for an isolated copy. |
| `color` | `red`, `blue`, `green`, `yellow`, `purple`, `orange`, `pink`, `cyan`. |
| `skills` | Preload a skill into the subagent's context. |

### Launching

```text
Use the scout agent to map this repo and write .ship/context-brief.md.
Use the verifier agent to run the gates on the current diff.
```

The main conversation is the lead. `ship-lead` exists as a subagent when you want a second pass on the plan or a full dispatch board, but the main thread owns the final call and the human approval.

### Isolation

Set `isolation: worktree` on a builder when it will run in parallel with another builder. The worktree is branched from the default branch by default, so tell the builder to rebase or merge the parent's HEAD if the slice depends on it.

## Role-to-model defaults

Use the least capable model that can do the role, and specify it per dispatch when the harness allows.

| Role | Default tier | Escalate when |
| --- | --- | --- |
| `scout` | Fast | The repo is huge or the stack is unfamiliar |
| `architect` | Strongest available | Always, if the change is a one-way door |
| `builder` | Mid | Multi-file integration, unclear pattern, or a failed fix round |
| `verifier` | Fast to mid | The gate output is ambiguous or the environment is broken |
| `reviewer` | Strongest available | Auth, money, data, or public API |
| `shipper` | Mid | The deploy is irreversible or the rollback is untested |

In OpenCode, omit `model` to inherit, or set `provider/model#variant`. In Claude Code, use `model: inherit`, `sonnet`, `opus`, or `haiku`.

## When the tool has no subagents

Run the roles inline in order:

1. Write the brief.
2. Do the recon yourself, with a step budget.
3. Write the plan.
4. Build one slice.
5. Verify in a fresh pass: re-read the diff, run the gates, do not trust your memory of writing it.
6. Review against the brief.
7. Write the ship note.

The independence is weaker, so compensate with a fresh context, a diff file, and the exact commands. Never skip the verification gate because you are alone.

## Artifact paths

All paths are relative to the repo root, not the home directory.

```text
.ship/
  ledger.md
  brief.md
  context-brief.md
  plan.md
  design-record.md
  reports/
  ship.md
```

Add `.ship/` to `.gitignore` unless the user wants the audit trail in the repo. If it is committed, exclude `ledger.md` when it contains internal rulings you do not want in history.
