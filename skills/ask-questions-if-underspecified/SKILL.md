---
name: ask-questions-if-underspecified
description: Clarify requirements before implementing. Use when a request has multiple plausible interpretations or critical details (objective, scope, constraints, environment, safety) are missing, and guessing would risk doing the wrong work.
metadata:
  source: https://github.com/trailofbits/skills/tree/main/plugins/ask-questions-if-underspecified
  author: Kevin Valerio (Trail of Bits)
  license: CC BY-SA 4.0
---

# Ask Questions If Underspecified

Ask the minimum set of clarifying questions needed to avoid wrong work. Do not start implementing until the must-have questions are answered, or the user explicitly approves proceeding on stated assumptions.

## When to use

Use when a request has multiple plausible interpretations, or when any of these are unclear and would change the implementation:

- **Objective**: what should change versus stay the same
- **Done**: acceptance criteria, examples, edge cases
- **Scope**: files, components, users, or systems in and out
- **Constraints**: compatibility, performance, style, dependencies, deadline
- **Environment**: language and runtime versions, OS, build and test runner
- **Safety**: data migration, rollout, rollback, reversibility, blast radius

## When not to use

Do not use when the request is already clear, or when a quick, low-risk discovery read (config, README, existing patterns) answers the missing detail. Do not interrogate the user about things you can inspect yourself.

## Workflow

### 1. Decide whether it is underspecified

Explore how you would perform the work. If more than one plausible interpretation survives that exploration, treat it as underspecified. If the only gaps are cheap to discover from the repo, discover them instead of asking.

### 2. Ask 1-5 must-have questions

Prefer questions that eliminate whole branches of work. Keep the first pass small.

Make questions easy to answer:

- Number them, and letter the options.
- Offer multiple choice rather than open-ended prose.
- Mark a recommended default.
- Support a fast path such as `defaults`.
- Include "not sure - use default" where honest.
- Separate "need to know" from "nice to know".
- Let the user answer compactly, e.g. `1b 2a 3c`.

If the harness provides a structured question tool, use it for each question. Otherwise use this shape:

```text
1) Scope?
a) Minimal change (recommended)
b) Refactor while touching the area
c) Not sure - use default

2) Compatibility target?
a) Current project defaults (recommended)
b) Also support older versions: <specify>
c) Not sure - use default

Reply with: defaults (or 1a 2a)
```

### 3. Pause before acting

Until the must-have answers arrive:

- Do not run commands, edit files, or produce a detailed plan that depends on unknowns.
- A clearly labeled, low-risk discovery step is fine if it does not commit you to a direction.

If the user says to proceed without answers:

1. State your assumptions as a short numbered list.
2. Ask for confirmation.
3. Proceed only after they confirm or correct the list.

### 4. Confirm interpretation, then proceed

Restate the requirements in one to three sentences, including key constraints and what success looks like. Then start work.

## Anti-patterns

- Asking what a quick config read would answer.
- Asking ten questions when two would eliminate the ambiguity.
- Open-ended questions where a tight multiple choice would do.
- Silently picking an interpretation and building the wrong thing.
- Blocking on questions the user already answered earlier in the session.

## Attribution

Adapted from the Trail of Bits `ask-questions-if-underspecified` skill (CC BY-SA 4.0), with harness-neutral question handling.
