# Slice Plan — <outcome>

## Decision

<Three sentences: what we are building, the shape, and why this shape.>

## Doors

| Door | Type | Reversible how |
| --- | --- | --- |
| <interface / schema / auth / pricing> | one-way / two-way | <how to undo> |

## Interfaces

<Exact contracts. Fix these before parallel work.>

```text
<function signature, request/response, schema, event, error code>
```

## Slices

| # | Slice | Demo | Files owned | Depends on |
| --- | --- | --- | --- | --- |
| 1 | <walking skeleton> | <what you can show> | `src/...` | — |
| 2 | <next behavior> | <what you can show> | `src/...` | 1 |
| 3 | <polish / edge cases> | <what you can show> | `src/...` | 1, 2 |

## File ownership

| File | Owner | Notes |
| --- | --- | --- |
| `src/...` | builder 1 | |
| `src/shared/...` | serialized | <who goes first> |

## Test strategy

| Slice | Test level | What it proves |
| --- | --- | --- |
| 1 | unit + integration | <behavior> |
| 2 | integration | <behavior> |
| 3 | e2e | <behavior> |

## Rollback

<How to undo in one step. Flag, revert, migration down, or restore.>

## Not building

- <The tempting adjacent thing we are not doing>
- <The abstraction we are not adding yet>

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| <risk> | <impact> | <action> |
