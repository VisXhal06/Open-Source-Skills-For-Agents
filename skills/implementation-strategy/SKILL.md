---
name: implementation-strategy
description: Decide scope and compatibility boundaries before changing runtime code, public APIs, schemas, protocols, or migrations. Use when a change may affect released behavior, durable formats, serialized state, or which inputs are supported, and when review feedback keeps widening the patch.
metadata:
  source: https://github.com/openai/openai-agents-python/tree/main/.agents/skills/implementation-strategy
  author: OpenAI
---

# Implementation Strategy

Decide what is supported before deciding how to build it. This skill prevents two common failures: breaking a boundary the project promised to keep, and letting an ever-growing patch chase every nearby edge case.

## When to use

- Runtime, public API, SDK, CLI, config, environment, or wire-protocol changes
- Persisted schemas, migrations, serialized state, or data formats
- A change where "support this input" versus "reject it" is a real decision
- Review feedback that keeps adding cases to the same abstraction
- Any patch where the required scenario is small but the diff keeps growing

Skip it for docs-only edits, isolated typo fixes, and purely internal refactors with no reachable behavior change.

## Step 1: Name the surface

Identify what you are changing:

- released public API
- unreleased branch-local API
- internal helper
- persisted schema or durable format
- wire protocol or event contract
- CLI, config, or environment surface
- docs and examples only

Only the first, fourth, fifth, and sixth usually carry compatibility obligations. Branch-local code is disposable unless it already defines a durable boundary.

## Step 2: Find the source of truth

Locate the nearest existing pipeline and the functions, types, or modules that own each affected concern: schema, validation, naming, identity, configuration, invocation, error handling.

Prefer adapting the required input into that pipeline over creating a parallel one. A second schema, validator, or execution path is a permanent cost; add it only for a stated requirement.

## Step 3: Record the scope contract

Write these four items in the plan or working notes. A small fix can use one paragraph. Mark unaffected dimensions as not applicable instead of inventing cases.

1. **Required behavior**: the smallest user-visible scenario that must work.
2. **Compatibility requirements**: released behavior or durable boundaries that must remain usable.
3. **Intentionally unsupported cases**: nearby inputs to reject, including when and how rejection happens.
4. **Supported alternative**: an existing wrapper, adapter, config, or lower-level API; write `none` when absent.

If the unsupported cases cannot be stated clearly, do not start by building a general resolver. Define a narrower contract first.

A reproducer proves reachability, not support. Treat a shape as supported only when public docs, examples, tests, typing, a durable boundary, or explicit maintainer intent says so. Otherwise record the risk and reject early with a supported alternative.

## Step 4: Choose the smallest coherent change

- Preserve released public APIs, documented behavior, and durable formats, or provide an explicit migration path.
- Rewrite branch-local interfaces and same-branch tests directly. Do not shim disposable code.
- Prefer one source of truth for schema, docs, validation, identity, and invocation.
- Treat an interface as everything a caller must know: ordering, errors, lifecycle, configuration, and performance constraints, not just the signature.
- Apply the deletion test before keeping an abstraction: keep it when removing it would scatter required complexity across callers; delete it when the complexity would disappear with it.
- Add a boundary only for demonstrated variation, ownership, or testability. One hypothetical adapter is not enough.
- Add branches, state, dependencies, or config only for a stated requirement or verified risk.
- Prefer an actionable construction- or validation-time error plus an existing alternative over partial protocol emulation.
- Keep unrelated refactors and pre-existing failures out of the patch.
- Append new optional fields or parameters to public constructors and dataclasses; do not insert them before existing positional fields without a compatibility layer and regression coverage.
- Define `None` and empty-value semantics deliberately when they affect behavior.

## Step 5: Review-feedback gate

Use this checkpoint only when feedback changes the scope contract or implementation shape. Reuse evidence you already gathered.

```text
Review checkpoint:
- Root cause and required behavior:
- Compatibility evidence and unsupported cases:
- Source of truth:
- Behavior-space change: narrows / unchanged / widens
- Action: focused patch / complexity reset / reject as unsupported
```

Classify each finding as:

- a required-behavior defect
- a supported compatibility requirement
- another combination of the same implementation dimensions
- an unrelated issue

Widening the behavior space needs new contract evidence, not reviewer confidence.

## Step 6: Complexity reset

Stop extending the current design when:

- Related findings keep combining the same dimensions: wrappers, descriptors, generics, binding, context injection, sync/async, provider variants.
- The patch starts interpreting a host-language or third-party protocol, or infers representations that can drift.
- A narrow requirement needs recursive resolution, cached modes, new state, or unrelated subsystem changes.
- Tests enumerate mechanics while the required scenario stays small.
- The diff keeps growing and every new case is "locally fixable".

When a trigger fires:

1. Stop editing. Freeze the current revision for analysis instead of addressing comments one at a time.
2. Group findings by root cause. Re-read the original requirement, scope contract, and supported boundaries.
3. Write a finding-derived reset spec from those inputs. Do not treat accumulated review explanations or branch-local machinery as requirements.
4. Audit the spec against every affected entry point and the nearest existing supported paths. Freeze it before resuming edits.
5. Map every abstraction, branch, and test in the diff to `retain`, `replace`, or `delete`.
6. Delete unmapped machinery, narrow the contract, and reject unsupported cases before side effects.
7. Rebuild tests around required behavior, supported compatibility, cross-entry-point consistency, and representative unsupported categories.
8. Evaluate later findings against the frozen spec. New contract evidence is required to change it.

```text
Finding-derived reset spec:
- Original required outcome:
- Supported release or durable boundaries:
- Grouped findings and common root cause:
- Invariants across affected entry points:
- Allowed states and behavior:
- Rejected states, failure timing, and side-effect boundary:
- Trusted and untrusted boundaries:
- Single sources of truth:
- Persistence, resume, cleanup, or lifecycle semantics:
- Non-goals and supported alternatives:
- Representative test categories:
- Diff reset: retain / replace / delete:
```

The spec is a falsifiable hypothesis, not a description of the current patch. Do not wait for the reviewer to request a reset when the signals are already present.

## Step 7: Effectiveness check

Before declaring the design complete, answer with evidence:

- Can the required behavior be described without naming internal helper types or reflection mechanics?
- Does the implementation reuse the nearest existing pipeline rather than a parallel interpretation?
- Does every new abstraction and branch map to the scope contract or a verified risk?
- Would deleting each new abstraction only scatter required complexity across callers?
- Are unsupported neighbors rejected before side effects, with a supported alternative identified?
- Do tests exercise the highest stable caller boundary, with expectations independent of the implementation?
- Does the latest revision shrink or preserve the behavior space rather than widen it without evidence?
- After a reset, does every retained piece map to the frozen spec?

## Step 8: State the decision

When this skill materially affects the approach, say so in one line:

```text
Compatibility boundary: latest release tag v2.4.1; branch-local interface rewrite, no shim needed.
Implementation scope contract: support X; preserve Y; reject Z before side effects; alternative W.
Complexity reset: repeated edge cases show the approach is too broad; redesign from the original requirement.
```

## When to stop and confirm

Ask before proceeding when:

- The change would alter behavior shipped in the latest release, or there is concrete evidence of reliance on incidentally accepted behavior.
- The change would modify durable data, protocol formats, or serialized state.
- The correct solution materially expands beyond the requested outcome or needs unrelated architectural work.
- A reset would change a released contract rather than branch-local code.
- The user explicitly asked for backward compatibility, deprecation, or migration support.

Ordinary remediation inside an approved scope contract does not need another confirmation.

## Attribution

Adapted from OpenAI's `implementation-strategy` skill in `openai/openai-agents-python`, generalized beyond the Agents SDK.
