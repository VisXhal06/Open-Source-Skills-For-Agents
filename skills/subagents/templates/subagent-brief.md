# Subagent brief: <role> — <task>

- **Task ID:**
- **Parent goal:**
- **Owner:**
- **Status:** ready | in progress | review | done
- **Depends on:**
- **Blocks:**

## Role

You are the **<specialist role>**. Your lens is <what you optimize for>. You are not responsible for the whole project.

## Mission

<One sentence. The outcome this subagent must produce.>

## Why

<The goal or decision this serves. Link the goal brief.>

## Context

Read first:

- `AGENTS.md`
- `<file>`
- `<doc>`
- `<prior decision or research>`

## Inputs

- 
- 

## Deliverable

<Memo, diff, test plan, review, runbook, or integration report. Be specific.>

## Scope

In:

- 
- 

Out:

- 
- 

## Allowed paths

```text
<paths this subagent may change>
```

Read-only:

```text
<paths it may read but not change>
```

## Acceptance criteria

- [ ] 
- [ ] 

## Verification

```bash
<commands>
```

Evidence required:

- 

## Constraints

- Follow `<path>` conventions.
- No new dependencies without approval.
- No secrets or real customer data.
- Do not change public contracts unless listed in scope.
- Do not merge to main.

## Stop conditions

Stop and ask if:

- You need to change a file outside the allowed paths.
- The contract is ambiguous.
- A required test cannot run.
- The work requires a product or security decision.

## Reporting format

```text
Role:
Task:
Status: done | blocked | needs review
Changed:
Verified:
Not done:
Risks:
Recommendation:
Next:
```
