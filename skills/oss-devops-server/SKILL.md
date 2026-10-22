---
name: oss-devops-server
description: "Use when contributing CI/CD, infrastructure-as-code, containers, release engineering, deployment, Linux server, networking, reverse proxy, observability, or production-runtime changes to an open-source project or large codebase. Use this whenever the task involves a failing pipeline, Dockerfile, Kubernetes manifest, Terraform, GitHub Actions, deployment, server performance, logs, metrics, or on-call behavior."
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
  suite: "oss-contributor"
---

# OSS DevOps + Server

DevOps changes are shared infrastructure. A pipeline change affects every contributor; a runtime change affects every user; a secret mistake can compromise the project. The standard is not "it deployed on my machine." The standard is reproducible, least-privilege, observable, and reversible.

Use this skill for CI/CD, infrastructure, containers, release engineering, server/runtime work, and production operations in open source or a large company codebase.

## Workflow

### 1. Map the delivery system

Capture:

- repository and branch model
- CI provider and workflow files
- build, test, and release steps
- artifact and registry
- environments and promotion path
- deployment mechanism
- infrastructure-as-code and state
- secrets and identity
- runtime platform and resource limits
- observability and alerting
- rollback and incident process

If the project has a `Makefile`, `Taskfile`, `justfile`, or `scripts/` directory, read it before adding a new command.

### 2. Reproduce the failure

For CI:

- the exact workflow and job
- runner OS and version
- dependency cache state
- environment variables and secrets presence
- logs around the first error
- whether it fails on `main`, only on PRs, or only on forks
- whether it is flaky or deterministic

For runtime:

- process, container, or host
- CPU, memory, disk, file descriptors
- network path and DNS
- logs, traces, and metrics
- recent deploy or config change
- version and image digest

### 3. Design the smallest safe change

State:

```text
System affected:
Change:
Blast radius:
Least privilege:
Reproducibility:
Rollback:
Verification:
```

Prefer:

- pinned action and image versions
- least-privilege tokens and permissions
- reproducible builds
- cached dependencies with a correct key
- small, composable workflows
- infrastructure as code over console changes
- feature flags and canaries over big-bang releases
- explicit health checks and resource limits

### 4. CI/CD quality

- Keep workflows fast enough that contributors run them.
- Fail with a clear error near the cause.
- Do not expose secrets to forked PRs.
- Pin third-party actions to a commit SHA when the project requires it.
- Cache only what is safe to cache.
- Make the test matrix intentional; do not multiply jobs without value.
- Upload artifacts and test reports on failure.
- Keep release notes and changelog generation reproducible.
- Separate build, test, and deploy permissions.

### 5. Container and runtime quality

- Use a minimal, supported base image.
- Pin the image version or digest.
- Run as a non-root user where possible.
- Do not bake secrets into the image.
- Set CPU and memory requests/limits.
- Handle `SIGTERM` and graceful shutdown.
- Add liveness and readiness checks that reflect real dependencies.
- Keep the filesystem read-only where possible.
- Log to stdout/stderr with structured fields.
- Expose metrics and traces at a stable endpoint.

### 6. Server and networking

For Linux/server issues, check:

- process state and exit code
- file descriptors and ulimits
- disk, inode, and memory pressure
- DNS resolution and TLS
- reverse proxy timeouts and headers
- connection pooling and keep-alive
- firewall and security groups
- clock skew
- kernel or runtime version
- systemd unit or supervisor behavior

Do not restart a production service to "see if it helps" without a hypothesis and a rollback.

### 7. Observability and rollback

Every change needs:

- a success signal
- a failure signal
- a latency/saturation signal where relevant
- a dashboard or query to check it
- an alert threshold
- a rollback command or procedure
- a post-deploy verification step

Logs should answer who/what/when/where/result without leaking secrets or PII.

### 8. Verify

Run:

```bash
<lint IaC>
<validate manifests>
<build image>
<run tests>
<smoke test>
<security scan>
```

Then verify in a staging or preview environment. For pipeline changes, open a test PR and confirm both success and failure paths. For runtime changes, check startup, health, traffic, and shutdown.

## Review checklist

```markdown
## Change
- Pipeline / infra / runtime:
- Blast radius:
- Permissions:
- Secrets:

## Reproducibility
- Pinned versions:
- Lockfiles:
- Cache:
- Build artifacts:

## Safety
- Health checks:
- Resource limits:
- Rollback:
- Monitoring:

## Evidence
- CI run:
- Staging run:
- Logs/metrics:
```

## OSS-specific rules

- Do not require paid infrastructure for contributors to run tests.
- Keep the local development path working without cloud credentials.
- Do not expose maintainer secrets to pull requests from forks.
- Keep CI cost and runtime reasonable; maintainers pay for it.
- Pin actions and images when the project's security policy expects it.
- Document environment variables and required permissions.
- Make release steps reproducible by someone other than the original author.
- Do not add a new platform dependency without maintainer agreement.

## Composition

- `launch-readiness` — production readiness, rollout, rollback.
- `code-change-verification` — run the project's full gate.
- `systematic-debugging` — CI and runtime failures.
- `oss-backend` — service behavior and observability.
- `oss-database` — backups, migrations, replication.
- `wrangler`, `workers-best-practices`, `durable-objects`, `cloudflare` — Cloudflare-specific work.
- `oss-security` — secrets, supply chain, permissions.

## Output format

End with:

```markdown
### DevOps/server contribution
- System affected:
- Root cause:
- Change:
- Permissions/secrets:
- Verification:
- Rollback:
- Monitoring:
- Next action:
```

A DevOps change is done when another maintainer can reproduce it, observe it, and reverse it.
