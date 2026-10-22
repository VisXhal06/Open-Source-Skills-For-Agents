---
name: oss-security
description: "Use when reviewing or fixing security issues in an open-source project or large codebase: threat modeling, authentication, authorization, injection, secrets, dependency and supply-chain risk, unsafe deserialization, SSRF, path traversal, or coordinated vulnerability disclosure. Use this whenever the task involves a vulnerability, security review, CVE, advisory, secret leak, or permission boundary."
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
  suite: "oss-contributor"
---

# OSS Security

Security work has a different failure mode from normal contribution: a mistake can expose users, and a public report can turn a bug into an incident. Act with authorization, minimize data, and follow the project's disclosure process.

Use this skill for security review, vulnerability fixes, and supply-chain work. Do not use it to attack systems you do not own or have explicit permission to test.

## Non-negotiables

- Read `SECURITY.md` before doing anything.
- Never test a third-party service, account, or user without explicit authorization.
- Never publish exploit details, proof-of-concept code, or affected user data before coordinated disclosure.
- Use synthetic data and the smallest reproduction.
- Do not access, copy, or retain data beyond what is necessary to demonstrate the issue.
- If you accidentally access sensitive data, stop and report it privately.
- Do not use a security issue to justify a broad rewrite.

## Workflow

### 1. Define scope and authorization

Write:

```text
Target:
Owner:
Authorization:
In scope:
Out of scope:
Data handling:
Disclosure contact:
```

If authorization is unclear, stop and ask. A public repository is not permission to attack its hosted service or users.

### 2. Threat model

Map:

- assets: data, credentials, sessions, payments, admin actions
- actors: anonymous, authenticated user, tenant admin, service, insider
- trust boundaries: browser/server, service/service, tenant/tenant, admin/user
- entry points: API, webhook, file upload, URL fetch, template, deserialization, CLI
- controls: authentication, authorization, validation, encoding, rate limiting, isolation
- failure impact: confidentiality, integrity, availability

Prioritize the boundary most likely to fail, not the longest checklist.

### 3. Review the common failure classes

- broken object-level authorization (IDOR)
- missing tenant scoping
- authentication bypass and session fixation
- privilege escalation
- SQL/NoSQL/command/template injection
- cross-site scripting and unsafe HTML
- CSRF and state-changing GETs
- SSRF and open redirects
- path traversal and unsafe file handling
- insecure deserialization
- secrets in code, logs, images, or build artifacts
- dependency and supply-chain compromise
- unsafe defaults and permissive CORS
- race conditions and TOCTOU
- denial of service through unbounded input or expensive operations

For each finding, record the exact file, symbol, input, and impact.

### 4. Reproduce safely

- Use a local instance or an authorized test environment.
- Use synthetic accounts and data.
- Minimize requests and avoid destructive actions.
- Capture only the evidence needed to prove the issue.
- Do not exfiltrate data, pivot, or persistence-test.
- Stop if the issue affects real users or production data.

### 5. Report privately

Follow the project's `SECURITY.md`. If none exists, contact the maintainers privately through the repository's stated channel. Include:

```markdown
## Summary
## Affected versions / commit
## Impact
## Preconditions
## Reproduction (minimal, safe)
## Evidence
## Suggested fix
## Disclosure timeline
## Credit preference
```

Do not open a public issue. Do not post details in a public chat. Do not submit a PR that reveals the vulnerability before the maintainer agrees.

### 6. Fix the root cause

- Validate at the trust boundary, not only at the UI.
- Enforce authorization on the object and tenant, not just the route.
- Use parameterized queries and safe APIs.
- Encode output for the correct context.
- Use allowlists over denylists.
- Apply least privilege to tokens, services, and CI.
- Add a regression test that would fail before the fix.
- Check adjacent code paths with the same pattern.
- Backport to supported versions if the project requires it.

### 7. Coordinate disclosure

- Agree on the fix, release, and advisory timing with the maintainer.
- Request a CVE if the project uses them.
- Write a clear advisory with affected versions, fixed versions, workarounds, and credit.
- Publish only after the fix is available and users have had a reasonable window.
- Thank the maintainers and reviewers.

## Security review checklist

```markdown
## Scope
- Target and version:
- Authorization:
- Trust boundaries:

## Findings
| Severity | Finding | Evidence | Affected path | Fix |
| --- | --- | --- | --- | --- |

## Verification
- Regression test:
- Adjacent paths checked:
- Supported versions/backports:
- Advisory/CVE:
```

## OSS-specific rules

- Public repos often have private security advisories enabled; use them.
- Do not assume the hosted service is in scope because the code is open.
- Respect embargoes and maintainer timelines.
- Do not name affected users or customers.
- Check dependency licenses and provenance before recommending a replacement.
- Keep the fix minimal; a security patch is not the time for a refactor.
- If the maintainer is unresponsive, follow the project's governance or a recognized coordinator; do not escalate by public disclosure without careful judgment.

## Composition

- `launch-readiness` — security and operational readiness.
- `oss-backend` — authz, injection, request handling.
- `oss-devops-server` — secrets, CI permissions, supply chain.
- `oss-database` — data exposure and integrity.
- `systematic-debugging` — root cause.
- `requesting-code-review` — review the fix.

## Output format

End with:

```markdown
### Security status
- Scope and authorization:
- Finding:
- Impact:
- Evidence:
- Fix:
- Disclosure state:
- Next action:
```

Security work succeeds when the user is protected, not when the bug is dramatic.
