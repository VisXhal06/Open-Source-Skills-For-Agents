# Ship Checklist — <release>

## Evidence

- [ ] Verification report exists and is `PASS` or `PASS WITH RISKS`
- [ ] Review verdict is `APPROVE` or `APPROVE WITH NITS`
- [ ] Every open finding is fixed or has a recorded ruling
- [ ] Diff range: `<base>..<head>`
- [ ] Commits are clean and named

If any box is unchecked, stop. Do not ship.

## Change

- What changed:
- Why:
- User impact:
- Internal impact:

## Changelog

```text
<user-facing entry>
```

## PR

- Title: `<type>(<scope>): <summary>`
- Body:
  - What:
  - Why:
  - How tested:
  - Risk:
  - Rollback:

## Deploy

| Step | Command or action | Owner |
| --- | --- | --- |
| 1 | <build / migrate / deploy> | |
| 2 | | |

Environment changes:

- [ ] No new variables
- [ ] New variables listed: `<name>` — set in `<env>`

Migrations:

- [ ] None
- [ ] Forward-only, backward-compatible
- [ ] Requires a maintenance window

Feature flags:

- [ ] None
- [ ] `<flag>` — default off, owner `<name>`

## Rollback

1. <revert commit / disable flag / roll back deploy>
2. <restore data if needed>
3. <verify>

Time to roll back: <minutes>

## Post-deploy checks

- [ ] Health endpoint
- [ ] Critical user path
- [ ] Error rate normal for 15 minutes
- [ ] Logs clean
- [ ] Metric or dashboard

## Approval

- Merge to `main`: <human name> — required
- Production deploy: <human name> — required
- Force-push: forbidden without explicit approval

## Notes

<Known risks, follow-ups, and anything the on-call needs.>
