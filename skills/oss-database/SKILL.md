---
name: oss-database
description: "Use when contributing database or data-layer changes to an open-source project or large codebase: schema design, migrations, indexes, query performance, data integrity, backfills, transactions, ORM behavior, or multi-database compatibility. Use this whenever the task involves SQL, a migration, a slow query, data corruption, or a schema change in code the user does not own."
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
  suite: "oss-contributor"
---

# OSS Database

Database changes are the least reversible part of most systems. A schema migration can outlive the code that introduced it, and a bad backfill can corrupt data before anyone notices. The senior move is to make the change observable, backward-compatible, and recoverable.

Use this skill for any data-layer contribution. Pair it with `oss-backend` for the request path and `oss-devops-server` for deployment and operational safety.

## Workflow

### 1. Understand the data model

Before changing anything, capture:

- engine and version (Postgres, MySQL, SQLite, SQL Server, etc.)
- schema ownership and migration tool
- tables, relationships, constraints, and indexes
- access patterns and query frequency
- expected data volume and growth
- transaction and isolation assumptions
- replication, backup, and retention policy
- ORM/query builder behavior
- supported database matrix for OSS projects

Read the migrations, not just the ORM models. The model may not reflect the real constraints.

### 2. Reproduce the problem

For a correctness bug:

- the exact query or operation
- the data that triggers it
- expected vs actual result
- transaction and concurrency conditions
- engine/version details

For a performance problem:

- the query and bind values
- `EXPLAIN` / `EXPLAIN ANALYZE` output
- table and index sizes
- row estimates vs actual rows
- lock waits and concurrent load
- before/after timing with methodology

Do not optimize a query without a plan and a baseline.

### 3. Design the change

State:

```text
Data affected:
Schema change:
Migration strategy:
Backfill:
Compatibility window:
Lock/load risk:
Rollback:
Verification:
```

Prefer:

- additive changes before destructive ones
- nullable columns or defaults with a backfill plan
- new indexes created concurrently where supported
- expand/contract migrations over in-place rewrites
- idempotent backfills
- application-level dual-write/dual-read during transition
- small batches with checkpoints

### 4. Migration safety

A production-safe migration answers:

- Does it lock the table? For how long?
- Does it rewrite the table?
- Can it run online while old code is still serving?
- Can old and new code run simultaneously?
- What happens if it fails halfway?
- Can it be rolled back without data loss?
- How is the backfill resumed?
- How is completion verified?

Use the expand/contract pattern:

1. **Expand:** add the new column/table/index without removing the old.
2. **Dual-write:** write both old and new.
3. **Backfill:** copy existing data in batches.
4. **Verify:** compare counts and checksums.
5. **Switch reads:** move traffic to the new path.
6. **Contract:** remove the old path after the compatibility window.

### 5. Query and index discipline

- Add an index for a real query pattern, not speculatively.
- Check column order and selectivity.
- Avoid functions on indexed columns in predicates.
- Watch for N+1 queries and unbounded result sets.
- Use keyset pagination for large offsets.
- Keep transactions short; do not hold locks across network calls.
- Use `EXPLAIN` before and after.
- Measure with realistic data volume.

### 6. Test

Add:

- migration up and down tests
- constraint and integrity tests
- backfill idempotency tests
- concurrent update tests where relevant
- query correctness tests with edge data
- performance regression evidence for hot paths

If the project supports multiple engines, run the relevant matrix or state which engine you tested.

### 7. Roll out and monitor

- Back up before destructive changes.
- Run in staging with production-like volume.
- Monitor locks, replication lag, error rate, and query latency.
- Keep the old path until the new path is proven.
- Document the rollback trigger and steps.
- Verify data after the rollout, not just application health.

## Migration review checklist

```markdown
## Change
- Tables/columns/indexes:
- Estimated rows:
- Lock risk:
- Rewrite risk:

## Compatibility
- Old code can run with new schema:
- New code can run with old schema:
- Backfill plan:
- Cleanup plan:

## Safety
- Backup:
- Rollback:
- Monitoring:
- Verification query:
```

## OSS-specific rules

- Support the documented database versions and engines.
- Do not use engine-specific SQL without a fallback or a documented requirement.
- Keep migrations runnable by contributors with a local database.
- Do not require a hosted service for tests.
- Avoid destructive migrations in a minor release.
- Include a migration guide for users who upgrade.
- Respect user data: no silent deletion, no lossy type changes.

## Composition

- `oss-backend` — request path and transaction boundaries.
- `oss-devops-server` — deployment, backups, monitoring.
- `systematic-debugging` — data corruption and slow queries.
- `testing-strategy` — migration and edge-case coverage.
- `launch-readiness` — rollout and rollback.

## Output format

End with:

```markdown
### Database contribution
- Data model:
- Change:
- Migration strategy:
- Lock/load risk:
- Verification:
- Rollback:
- Evidence:
- Next action:
```

A database change is safe when the old system and the new system can coexist until the data proves the migration worked.
