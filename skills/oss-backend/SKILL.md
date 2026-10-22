---
name: oss-backend
description: "Use when contributing backend code to an open-source project or large codebase: HTTP APIs, services, auth, authorization, background jobs, queues, integrations, concurrency, retries, error handling, performance, or observability. Use this whenever the task touches a server-side request path, service boundary, API contract, job, or backend bug in code the user does not own."
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
  suite: "oss-contributor"
---

# OSS Backend

Backend contribution is contract work. The request path, status codes, event payloads, retry semantics, and authorization rules are promises to clients and operators. A small backend change can break a mobile app, a partner integration, a background worker, or an on-call runbook.

Use this skill for server-side changes in open source or a large company codebase. Pair it with `large-codebase-navigator` for the request path, `oss-database` for data changes, and `oss-devops-server` for deployment and runtime.

## Workflow

### 1. Map the request path

Trace one concrete call:

```text
client -> gateway/proxy -> route -> middleware -> handler/controller
       -> service/use case -> repository/client -> database/external service
       -> response/event
```

At each hop, capture:

- input validation
- authentication and authorization
- transaction boundary
- error mapping
- timeout and retry
- idempotency
- logging, metrics, and traces
- tests and fixtures

If the path crosses services, record the contract and deploy order.

### 2. Reproduce the behavior

Capture:

- request or job input
- environment and version
- expected vs actual response/status
- logs and trace IDs
- database or queue state
- concurrency or load conditions
- whether the issue is reproducible locally

For flaky or production-only issues, state what you cannot reproduce and what evidence you have.

### 3. Find the root cause

Check in this order:

1. Input validation and serialization
2. Authn/authz and tenant scope
3. Business logic and state transitions
4. Transaction and consistency boundaries
5. External dependency behavior
6. Timeouts, retries, and idempotency
7. Configuration and feature flags
8. Resource limits and concurrency
9. Deployment/version skew

Use `systematic-debugging`. Do not add a retry or a null check until you know why the failure happens.

### 4. Design the smallest safe change

State:

```text
Contract affected:
Behavior change:
Compatibility:
Failure modes:
Idempotency:
Rollout:
Rollback:
Tests:
```

Prefer:

- preserving existing status codes and error shapes
- additive fields over renamed fields
- explicit validation over silent coercion
- bounded retries with jitter and a deadline
- idempotency keys for mutating operations
- feature flags for behavior changes
- backward-compatible defaults

### 5. Handle the failure path

Every backend change needs an answer for:

- dependency timeout or outage
- partial failure and retry
- duplicate delivery
- concurrent updates
- rate limiting and backpressure
- invalid or malicious input
- authorization failure
- resource exhaustion
- version skew during rollout

If the operation mutates data, define whether it is idempotent and how a retry is deduplicated.

### 6. Test

Use the project's test layers:

- unit tests for pure logic
- integration tests for the handler/service/database path
- contract tests for API or event schemas
- failure-injection tests for timeouts and errors
- concurrency tests where races are possible
- migration tests for data changes

Test the real boundary when possible. A test that mocks the database cannot prove a transaction or query is correct.

### 7. Roll out and observe

- Add logs with stable fields, not prose.
- Add metrics for success, failure, latency, and saturation where relevant.
- Add traces across service boundaries.
- Use a feature flag or canary for risky behavior.
- Define the rollback trigger and procedure.
- Check dashboards and alerts after release.

## API change checklist

```markdown
## Contract
- Endpoint / event / job:
- Request schema:
- Response schema:
- Status codes:
- Error model:
- Auth and tenancy:
- Idempotency:
- Rate limits:

## Compatibility
- Existing clients:
- Versioning:
- Deprecation:
- Migration:

## Evidence
- Tests:
- Load/performance:
- Logs/traces:
- Rollback:
```

## OSS-specific rules

- Public APIs, webhooks, and event schemas are contracts. Treat them like published libraries.
- Support the documented versions; do not silently drop old clients.
- Do not add a new infrastructure dependency for a small feature.
- Keep plugin and extension APIs versioned.
- Respect the project's security and disclosure process.
- Make local development possible without proprietary services.
- Do not commit secrets, tokens, or production data.

## Composition

- `large-codebase-navigator` — map the request path.
- `systematic-debugging` — root cause.
- `oss-database` — schema, query, migration.
- `oss-devops-server` — deploy, runtime, observability.
- `oss-security` — authz, injection, secrets, supply chain.
- `testing-strategy` — test layers and edge cases.
- `launch-readiness` — rollout and rollback.

## Output format

End with:

```markdown
### Backend contribution
- Contract affected:
- Root cause:
- Change:
- Failure handling:
- Tests and evidence:
- Compatibility:
- Rollout/rollback:
- Next action:
```

A backend change is done when it is correct, observable, and reversible.
