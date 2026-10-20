---
name: launch-readiness
description: Use when preparing to ship a feature or project to production and you need to check security, data, reliability, observability, rollback, performance, accessibility, and support readiness.
license: MIT
compatibility: opencode
metadata:
  version: "1.1.0"
---

# Launch Readiness

Shipping is a risk decision, not a calendar event. The question is not "Is it done?" It is "What can fail, how bad is it, and can we recover?"

## Suite integration

Part of the senior-dev suite. `senior-dev-os` can load this skill automatically before a release or go/no-go decision; direct invocation works too. If the router loaded it, produce the launch type, readiness evidence, rollout, and rollback, not a reassurance.

## Decide the launch type

| Type | When | Requirements |
| --- | --- | --- |
| Silent launch | Internal or low-risk change | Tests, monitoring, rollback |
| Feature flag | User-visible, reversible | Flag, metrics, kill switch |
| Canary | Higher traffic or risk | Small percentage, dashboards, rollback trigger |
| Full launch | Low-risk or already proven | All checks below |
| Delayed | Any red item with no mitigation | Owner and date |

If the change is irreversible (data deletion, public API contract, pricing), treat it as high risk regardless of size.

## Readiness dimensions

### Product and scope

- [ ] Acceptance criteria are met and demoed.
- [ ] Non-goals are respected; no surprise scope.
- [ ] Success metric and instrumentation are defined.
- [ ] Support and sales know what changed.
- [ ] Rollback or kill switch is available.

### Security and privacy

- [ ] Authentication and authorization are enforced server-side.
- [ ] Every new endpoint checks the right role and tenant.
- [ ] Inputs are validated and outputs encoded.
- [ ] No secrets in code, logs, or client bundles.
- [ ] Dependencies are scanned; no known critical vulnerabilities.
- [ ] Rate limits and abuse controls exist for public endpoints.
- [ ] PII is minimized, encrypted, and covered by retention policy.
- [ ] File uploads check type, size, and content.
- [ ] Error messages do not leak internals.

### Data and migrations

- [ ] Migration runs on a copy of production data.
- [ ] Migration is backward compatible during deploy.
- [ ] A rollback or forward-fix plan exists.
- [ ] Backups are current and restore has been tested.
- [ ] New indexes are created safely on large tables.
- [ ] Data deletion and retention are handled.
- [ ] Idempotency prevents duplicate writes.

### Reliability and observability

- [ ] Health check and readiness check exist.
- [ ] Structured logs include request ID and relevant context.
- [ ] Errors are captured with stack traces and release version.
- [ ] Metrics cover traffic, errors, latency, and saturation.
- [ ] Alerts have owners and runbooks.
- [ ] Timeouts, retries, and circuit breakers are configured.
- [ ] Graceful shutdown and job draining work.
- [ ] Load test covers expected launch traffic.

### Performance

- [ ] Critical pages meet the Core Web Vitals budget.
- [ ] API p95 latency is within budget.
- [ ] Database queries are indexed and explained.
- [ ] Caching is correct and invalidates safely.
- [ ] Large payloads and images are optimized.
- [ ] The system degrades gracefully under load.

### Accessibility and UX

- [ ] Keyboard-only navigation works.
- [ ] Screen reader labels and landmarks are present.
- [ ] Color contrast meets WCAG AA.
- [ ] Loading, empty, error, and disabled states exist.
- [ ] Mobile viewport and slow network are tested.
- [ ] Error messages say what to do next.

### Operations and support

- [ ] Runbook covers deploy, rollback, and incidents.
- [ ] On-call or escalation path is known.
- [ ] Status page or user communication plan exists.
- [ ] Support macros and FAQs are updated.
- [ ] Access and permissions for the new system are documented.
- [ ] Cost estimate and budget alert are in place.

### Release and rollback

- [ ] Version and changelog are updated.
- [ ] Deploy is automated and repeatable.
- [ ] Rollback command is known and tested.
- [ ] Feature flag defaults are safe.
- [ ] Database rollback is possible or a forward fix is ready.
- [ ] Post-deploy verification steps are written.

### AI-specific launch risks

If the product uses AI, add these checks:

- [ ] Prompt injection and untrusted input are treated as security boundaries.
- [ ] User data, secrets, and system prompts are not leaked in outputs or logs.
- [ ] Model, prompt, tool, and retrieval versions are pinned or recorded.
- [ ] An eval gate blocks release when quality drops below the threshold.
- [ ] Cost, latency, and rate limits are measured and budgeted.
- [ ] High-stakes output has human review or a safe fallback.
- [ ] Abuse, spam, and unsafe-output paths have an owner and a response.
- [ ] A rollback plan covers model or prompt changes, not just code.

## Go / no-go

Hold a short review with the people who own product, engineering, and operations.

For each open risk:

| Risk | Likelihood | Impact | Mitigation | Owner | Decision |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

Rules:

- Any unmitigated critical security or data-loss risk is a no-go.
- Any red item without an owner is a no-go.
- Yellow items can ship with a monitor and a rollback plan.
- If the team cannot describe how to roll back, do not ship.

## Rollout

1. Deploy to staging or a preview environment.
2. Run the smoke test and critical E2E suite.
3. Enable for internal users or a small cohort.
4. Watch errors, latency, and business metrics for a defined window.
5. Expand gradually.
6. Keep the kill switch ready until the monitoring window closes.

Define rollback triggers in advance, for example:

- Error rate above 2% for 5 minutes
- p95 latency above 1 second for 10 minutes
- Payment failure rate above baseline by 50%
- Any data corruption or authorization bypass

## Post-launch

- Monitor for 24–48 hours, longer for high-risk changes.
- Compare metrics to the baseline.
- Collect user feedback and support tickets.
- Record what surprised you.
- Write a short postmortem for incidents and near misses.
- Turn follow-ups into tasks with owners.

## Founder lens

Ask three questions:

1. **What can kill the company if this goes wrong?** Security, data loss, payments, legal, trust. Do not ship with an unmitigated risk here.
2. **What is reversible?** Ship reversible things quickly; slow down for irreversible ones.
3. **What can wait?** Polish, extra dashboards, and non-critical refactors can follow. Do not delay learning for them.

## Common mistakes

| Mistake | Consequence | Fix |
| --- | --- | --- |
| Launch date drives the decision | Known risks ship | Go/no-go with explicit risks |
| No rollback | A bad deploy becomes an outage | Test rollback before launch |
| No monitoring window | Problems found by users | Watch metrics after deploy |
| Migration tested only on empty DB | Fails on real data | Test on a production copy |
| Auth checked only in the UI | Data exposed via API | Enforce server-side |
| No owner for alerts | Nobody responds | Assign owners and runbooks |
| Launching everything at once | Maximum blast radius | Flag or canary |
| No support prep | Users hit unexplained changes | Update docs and macros |

## Related skills

- `project-kickoff` for the initial quality baseline
- `testing-strategy` for critical-path tests
- `documentation-system` for runbooks and changelog
- `codebase-playbook` for release and rollback process
- `verification-before-completion` before the final go
