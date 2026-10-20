---
name: testing-strategy
description: Use when planning tests for a feature or codebase, deciding what to test at which level, enumerating edge cases, or fixing coverage, flaky-test, and test-data problems.
license: MIT
compatibility: opencode
metadata:
  version: "1.1.0"
---

# Testing Strategy

Tests are a risk-management system, not a coverage score. The goal is fast, trustworthy evidence that the behaviors that matter still work.

## Suite integration

Part of the senior-dev suite. `senior-dev-os` can load this skill automatically when the question is what evidence proves a change; direct invocation works too. If the router loaded it, start from the risks and critical journeys, then produce the test plan and gates.

## Core principles

- Test behavior, not implementation details.
- Choose the cheapest test level that can catch the risk.
- One reason to fail per test.
- A test that can pass while the feature is broken is worse than no test.
- Fast tests run often; slow tests run where they can still block a bad merge.
- Flaky tests are defects. Quarantine, own, and fix them.
- Coverage is a signal, not a target.

## Test levels

| Level | What it proves | Speed | Use for |
| --- | --- | --- | --- |
| Unit | A function or module behaves correctly in isolation | Fast | Pure logic, validation, formatting, calculations |
| Integration | Modules work together with real boundaries | Medium | Database queries, API handlers, queues, auth |
| Contract | Producer and consumer agree on a shape | Medium | Public APIs, events, third-party integrations |
| End-to-end | A critical user journey works in a real browser | Slow | Login, checkout, signup, core workflow |
| Property-based | Invariants hold across many inputs | Medium | Parsers, money, permissions, state machines |
| Mutation | Tests detect injected faults | Slow | Critical modules, quarterly or targeted |
| Performance | The system meets a latency or throughput budget | Slow | Hot paths, launch readiness |
| Security | Common attacks and authorization rules fail closed | Medium | Auth, input handling, file upload, payments |
| Accessibility | The UI works with keyboard and assistive tech | Medium | Primary journeys |

## Build the test plan

### 1. Identify critical journeys

List what a user must be able to do for the product to be useful. Rank by impact if broken.

### 2. Map failure modes

For each journey, ask: what could fail, how likely is it, and how bad is the outcome? Risk = likelihood × impact.

### 3. Pick the level

Use the lowest level that catches the risk:

- Pure logic → unit.
- Database or API boundary → integration.
- Cross-service shape → contract.
- User-visible journey → one E2E, not five.
- Unknown input space → property-based.
- Critical algorithm → targeted mutation testing.

### 4. Write test cases

Use `templates/test-plan.md` and `templates/test-case.md`.

| ID | Scenario | Given | When | Then | Level | Data |
| --- | --- | --- | --- | --- | --- | --- |
| T-01 |  |  |  |  |  |  |

Each case needs one observable outcome. Avoid "and" in the Then column; split it.

### 5. Define test data

- Use factories or builders for valid defaults.
- Override only the fields relevant to the test.
- Keep tests independent; no shared mutable fixtures.
- Use a dedicated test database or schema.
- Never use production data without anonymization.
- Seed deterministic data; freeze time where time matters.
- Clean up in reverse order, or use transactions.

### 6. Set CI gates

| Stage | Run |
| --- | --- |
| Pre-commit | Format, lint staged files |
| Pull request | Unit, integration, typecheck, build |
| Main | Full suite, preview deploy, smoke test |
| Nightly | E2E, dependency audit, performance budget |
| Release | Critical E2E, migration test, launch checklist |

A failing gate blocks merge. Do not rely on reviewers to remember.

## Edge case catalog

Walk this list for every feature. Not every item applies; mark the ones that do.

### Input

- Empty, null, undefined, whitespace
- Minimum, maximum, just below, just above
- Negative, zero, overflow, precision
- Unicode, emoji, right-to-left text, long strings
- Invalid types, malformed JSON, unexpected fields
- Duplicate values, duplicate submissions

### State and concurrency

- First use, repeated use, idempotency
- Partial failure and retry
- Two users acting at once
- Stale cache or stale read
- Out-of-order events
- Concurrent updates to the same record

### Time

- Time zones and daylight saving
- Leap year and month boundaries
- Expired and not-yet-valid tokens
- Clock skew between services
- Scheduled jobs running twice

### Auth and permissions

- Anonymous user
- Expired, revoked, or malformed token
- Wrong role
- Cross-tenant access
- Deactivated account
- Rate limit exceeded

### Data

- Missing record
- Deleted record
- Pagination boundaries
- Sorting and filtering combinations
- Very large result sets
- SQL injection and XSS payloads
- File type, size, encoding, and path traversal

### Network and integrations

- Timeout
- Offline
- Slow response
- 4xx and 5xx
- 429 rate limit
- Partial response
- Webhook retry and duplicate delivery

### Money

- Rounding and currency
- Tax and discount order
- Negative amounts and refunds
- Double charge and race conditions
- Currency mismatch

### UI

- Loading, empty, error, and disabled states
- Keyboard-only navigation
- Screen reader labels
- Mobile viewport and slow network
- Long content and overflow
- Double click and back button

### Operations

- Migration on existing data
- Rollback
- Backup restore
- Missing environment variable
- Secret rotation
- Read-only database or disk full

## Coverage policy

- Require coverage for critical paths and changed lines, not a global percentage.
- Use diff coverage on pull requests.
- Do not write tests for generated code, trivial getters, or framework wiring.
- Use mutation testing on one or two critical modules rather than everywhere.
- Track escaped defects; they tell you more than coverage.

## AI-generated code and AI features

These are different problems and need different evidence.

### AI-generated code

Treat generated code as an untrusted draft:

- Review the diff for scope, security, and conventions.
- Require tests for the behavior and the edge cases the generator likely missed.
- Run the full gate; never accept "the model says it works."
- Check that the code is the simplest change, not merely a plausible one.

### AI-powered features

When the product behavior is probabilistic, example-based tests are not enough. Add an eval set:

- Representative inputs, including adversarial and ambiguous cases.
- A grader: exact match, rubric, model judge, or human review.
- A threshold that blocks release.
- Regression runs when the model, prompt, tools, or retrieval change.
- Cost, latency, and failure-mode checks.
- A fallback or human escalation for high-stakes output.

Keep evals small and owned. An eval set nobody reviews is coverage theater.

## Flaky tests

1. Quarantine the test so it stops blocking unrelated work.
2. Assign an owner and a fix deadline.
3. Capture the failure output, seed, and environment.
4. Fix the root cause: time, order, shared state, network, or randomness.
5. Do not add retries to hide flakiness. Retries are for known external instability, not your own race conditions.

## Anti-patterns

| Pattern | Problem | Fix |
| --- | --- | --- |
| Ice cream cone | Many slow E2E tests, few unit tests | Invert the pyramid |
| Mock everything | Tests pass while integration breaks | Use real boundaries where cheap |
| Snapshot abuse | Large snapshots nobody reviews | Assert the behavior that matters |
| Coverage theater | High number, weak assertions | Risk-based and mutation checks |
| Shared mutable fixtures | Tests depend on order | Isolated data per test |
| Sleep-based waits | Slow and flaky | Wait for a condition |
| Testing implementation | Refactors break tests | Test public behavior |
| No error-path tests | Happy path only | Add failure and permission cases |

## Definition of done for tests

- [ ] Critical path covered at the right level.
- [ ] Named edge cases covered.
- [ ] Error and permission paths covered.
- [ ] Tests are deterministic and independent.
- [ ] Test data is isolated and realistic.
- [ ] CI runs the suite and blocks merge.
- [ ] No new flaky tests.
- [ ] Verification output recorded.

## Related skills

- `test-driven-development` for the red-green-refactor loop
- `systematic-debugging` when a test fails unexpectedly
- `code-change-verification` for the full gate
- `launch-readiness` for production checks
- `agent-delegation` for assigning test work
