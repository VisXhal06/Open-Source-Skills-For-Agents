# Task packet: <ID> <title>

- **Owner:** <agent or human>
- **Status:** backlog | ready | in progress | review | blocked | done
- **Depends on:** <task IDs>
- **Blocks:** <task IDs>

## Goal

<One sentence. The outcome, not the activity.>

## Why

<The user or business reason. Link the product brief or issue.>

## Context

Read first:

- `AGENTS.md`
- `<file>`
- `<doc>`
- <prior task or decision>

## Scope

In:

- 
- 

Out:

- 
- 

## Allowed paths

```text
<paths this task may change>
```

Do not touch:

```text
<paths that are off limits>
```

## Acceptance criteria

- [ ] 
- [ ] 
- [ ] 

Each criterion must be observable and testable.

## Verification

```bash
<format>
<lint>
<typecheck>
<test>
<build>
```

Manual checks:

- 
- 

## Constraints

- Follow the existing patterns in `<path>`.
- No new dependencies without approval.
- No changes to the public API unless listed in scope.
- No secrets or real customer data.

## Deliverable

- Diff or commit:
- Report:
- Artifacts:

## Stop conditions

Stop and ask if:

- The task requires changing a file outside the allowed paths.
- A product or security decision is ambiguous.
- A required test or build cannot run.
- The change would break a public contract.

## Handoff

Report:

```text
Task:
Status:
Changed:
Verified:
Not done:
Risks:
Next:
```
