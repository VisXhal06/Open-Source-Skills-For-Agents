---
name: code-change-verification
description: Run the project's formatting, lint, type-check, build, and test stack after code changes. Use before claiming work is complete, committing, or opening a PR, and whenever a change touches runtime code, tests, build config, or generated artifacts.
metadata:
  source: https://github.com/openai/openai-agents-python/tree/main/.agents/skills/code-change-verification
  author: OpenAI
---

# Code Change Verification

A change is not done because the code looks right. It is done when the project's own verification stack passes on the current diff, and you can show the output.

## When to use

Use when a change touches:

- runtime or library code
- tests or test infrastructure
- build, bundling, or packaging config
- generated code, schemas, or migrations
- public types or API surface

Skip the full stack for docs-only, comment-only, or repository-metadata changes, unless the user asks for it or the project's policy requires it.

## Step 1: Find the project's definition of "verified"

Do not assume. Read, in this order, and stop when you find a definitive answer:

1. `AGENTS.md`, `CLAUDE.md`, or `.agents/` instructions
2. `CONTRIBUTING.md` and the README's development section
3. CI workflows (`.github/workflows/*.yml`, `.gitlab-ci.yml`, etc.)
4. Task runner: `Makefile`, `justfile`, `Taskfile.yml`, `package.json` scripts
5. Ecosystem defaults: `pyproject.toml`, `Cargo.toml`, `go.mod`, `build.gradle`, `pom.xml`, `*.csproj`

Extract the exact commands and their required order. If the project defines a single `check`, `verify`, or `ci` script, prefer it; do not reconstruct a worse version by hand.

If no commands exist, say so and ask before inventing a stack. For a fresh project, propose the ecosystem defaults and get agreement.

## Step 2: Prepare the environment

- Use the project's pinned runtime and package manager (`.nvmrc`, `.python-version`, `rust-toolchain`, `go.mod`, lockfiles).
- Install dependencies only when they are missing or dependency files changed.
- Do not upgrade dependencies as part of verification.
- Do not request elevated permissions, disable sandboxes, or bypass hooks to make checks pass.

## Step 3: Run the stack in order

A typical order, adjusted to the project:

1. **Format**: apply the project formatter, then confirm the tree is clean.
2. **Lint**: run the configured linter with warnings treated as the project treats them.
3. **Type check**: run the type checker if the project has one.
4. **Build or package**: run it when the change affects shipped output.
5. **Tests**: run the relevant suite, then the full suite before handoff.

Rules:

- Run from the repository root unless the project says otherwise.
- Stop at the first failure. Read the actual error, fix the cause, then restart the stack from the failing step or from the beginning if the fix could affect earlier steps.
- Do not skip a failing step because "it was already broken". Determine whether the diff caused it. If it is pre-existing, say so with evidence and do not claim a clean run.
- Do not weaken tests, delete assertions, add blanket ignores, or widen tolerances to get green.
- Do not run repository-wide checks in parallel with another heavy run on the same machine; it produces false failures and noisy timing.
- Use focused tests during iteration; use the full suite before declaring completion.

## Step 4: Verify the evidence

Before reporting success, confirm:

- Every command ran on the current working tree, after the last edit.
- The exit codes were zero, or the only failures are proven pre-existing and disclosed.
- Formatting did not leave uncommitted reformat noise outside the intended change.
- No generated artifact is stale relative to its source.
- The diff contains no debug prints, skipped tests, or temporary bypasses.

If you cannot run a step, say which step and why. "Tests not run" is honest; "should pass" is not evidence.

## Step 5: Report

Use a compact block:

```text
Verification
- format:  <command> - pass
- lint:    <command> - pass
- types:   <command> - pass
- build:   <command> - pass
- tests:   <command> - pass (412 passed, 0 failed)

Skipped: <step> - <reason>
Pre-existing failures: <test> - <evidence it predates this diff>
```

Include the exact commands, not just "tests pass". If a command failed and was fixed, mention the failure and the fix in one line.

## Failure handling

| Situation | Action |
| --- | --- |
| Missing dependency or tool | Install per project instructions, or report the exact missing tool. |
| Version mismatch | Switch to the pinned runtime; do not patch around it. |
| Flaky test | Rerun once in isolation, capture evidence, and disclose it. Do not silently retry until green. |
| Pre-existing failure | Verify against the base commit or an untouched branch, then disclose. |
| Check takes too long | Run the relevant subset, report what was skipped, and run the full stack before handoff if possible. |
| No verification defined | Ask the user; propose ecosystem defaults if they want one. |

## Rules

- Never claim a check passed without fresh output from the current tree.
- Never present partial verification as full verification.
- Never commit or open a PR while a required check is failing.
- Keep verification separate from unrelated refactors.
- CI is the final authority; local green does not override a red pipeline.

## Attribution

Adapted from OpenAI's `code-change-verification` skill in `openai/openai-agents-python`, generalized to discover each repository's own verification stack.
