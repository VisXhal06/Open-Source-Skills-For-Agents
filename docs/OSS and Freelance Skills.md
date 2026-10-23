---
title: OSS and Freelance Skills
tags: [skills, open-source, freelancing, opencode, engineering, product]
created: 2026-10-22
updated: 2026-10-22
status: active
---

# OSS and Freelance Skills

This note documents the 16-skill suite added from the research report [[Freelancing and open source AI skills]]. The suite turns the research into two operating systems:

- **`oss-contributor`** — contribute to open source or a large company codebase like a maintainer-grade senior engineer.
- **`freelance-operator`** — find, qualify, scope, price, and deliver client work like a business owner.

Both are front doors. They load specialist skills automatically and can be invoked directly.

## Quick start

| Entry point | What it does |
| --- | --- |
| `/oss <request>` | Loads `oss-contributor` and applies it to the request. |
| `@oss-contributor` | Loads the OSS front door as a skill mention. |
| `/issues <request>` | Loads `oss-issue-scout` to find, score, and track issues. |
| `@oss-issue-scout` | Finds issue leads and human leads. |
| `/gsoc <request>` | Loads `gsoc-strategist` to plan the GSoC campaign. |
| `@gsoc-strategist` | Plans orgs, contributions, mentor outreach, and proposals. |
| `/freelance <request>` | Loads `freelance-operator` and applies it to the request. |
| `@freelance-operator` | Loads the freelance front door as a skill mention. |

Examples:

```text
/oss I want to fix a bug in a large Rust monorepo I have never seen
/issues scan kubernetes/kubernetes and rust-lang/rust for unassigned bugs I can fix
/gsoc Build my Oct-to-May plan for a GSoC project in the Kubernetes ecosystem
/freelance Help me turn my RAG evaluation work into a paid diagnostic offer
/oss Review this upstream PR like a maintainer and list the blockers
/freelance Price a 6-week AI product discovery engagement
```

## The OSS suite

| Skill | Role | Use when |
| --- | --- | --- |
| `oss-contributor` | Front door, maintainer lens, contribution strategy | Any open-source or large-codebase contribution |
| `large-codebase-navigator` | Codebase archaeologist and mapping lead | The repo is huge, legacy, unfamiliar, or owned by another team |
| `oss-senior-engineer` | Senior open-source developer | Issue selection, reproduction, fix, tests, PR, review |
| `oss-system-designer` | System designer and architect | API, service boundary, RFC, ADR, migration, compatibility |
| `oss-uiux-frontend` | UI/UX designer and frontend engineer | Design systems, accessibility, responsive UI, frontend bugs |
| `oss-backend` | Backend engineer | APIs, services, auth, jobs, queues, concurrency |
| `oss-database` | Database engineer | Schema, migrations, indexes, queries, backfills |
| `oss-devops-server` | DevOps, SRE, and server engineer | CI/CD, containers, IaC, Linux, networking, observability |
| `oss-security` | Security engineer | Threat modeling, authz, secrets, supply chain, disclosure |
| `oss-issue-scout` | Issue scout and maintainer mapper | Finding, scoring, and tracking issues; identifying owners and mentors |
| `gsoc-strategist` | GSoC campaign lead | Org selection, ideas list, contribution proof, proposal, timeline |

### The OSS operating loop

```text
/oss
  → oss-contributor (choose the work)
  → large-codebase-navigator (map the system)
  → oss-senior-engineer (reproduce, fix, test, PR)
  → specialist skill as needed
  → verification-before-completion
  → receiving-code-review
```

For a large company codebase:

```text
large-codebase-navigator
  → trace one path
  → extract invariants
  → identify the smallest change point
  → oss-senior-engineer
  → oss-backend / oss-database / oss-devops-server / oss-uiux-frontend
```

For an architecture change:

```text
large-codebase-navigator
  → oss-system-designer (RFC/ADR)
  → oss-senior-engineer (slices)
  → launch-readiness
```

## The freelance suite

| Skill | Role | Use when |
| --- | --- | --- |
| `freelance-operator` | Front door and business operator | Strategy, routing, pipeline, offer design |
| `freelance-lead-gen` | Lead generator and growth operator | ICP, offer, lists, outreach, discovery, pipeline |
| `freelance-business-development` | Business developer | Positioning, pricing, proposals, contracts, retainers |
| `freelance-product-lead` | Lead product manager | Discovery, PRD, MVP, roadmap, stakeholders |
| `freelance-client-delivery` | Delivery lead and account manager | Kickoff, status, QA, handoff, case study, retention |

### The freelance operating loop

```text
/freelance
  → freelance-operator (stage and strategy)
  → freelance-lead-gen (ICP, offer, pipeline)
  → freelance-business-development (proposal, price, close)
  → freelance-product-lead (scope and product)
  → freelance-client-delivery (deliver, prove, retain)
```

For a first client:

```text
freelance-lead-gen
  → define ICP and paid diagnostic
  → build 50-lead list
  → outreach + discovery
  → freelance-business-development
  → proposal and close
```

For an existing engagement:

```text
freelance-client-delivery
  → weekly status and change control
  → freelance-product-lead (scope decisions)
  → handoff and case study
  → retainer proposal
```

## What changed in the skill library

The global library was 76 skills. This suite adds 16; with the later AI engineering add-on, `llm-release-gate`, the global total is **93**.

New skills:

```text
oss-contributor
large-codebase-navigator
oss-senior-engineer
oss-system-designer
oss-uiux-frontend
oss-backend
oss-database
oss-devops-server
oss-security
oss-issue-scout
gsoc-strategist
freelance-operator
freelance-lead-gen
freelance-business-development
freelance-product-lead
freelance-client-delivery
```

New commands:

```text
/oss
/issues
/gsoc
/freelance
```

AI engineering add-on:

```text
/release-gate   -> llm-release-gate
```

## Design principles

### OSS

- **Uncertainty reduction beats code volume.** A reproduction and a regression test are worth more than a large speculative patch.
- **Read the project before changing it.** Policies, ownership, conventions, and invariants come first.
- **Keep the diff small.** One logical change, one reviewable PR, one clear rollback.
- **Respect maintainers.** Ask before large work, disclose AI use, respond well to review, do not spam.
- **Make the map usable.** A codebase brief should let another engineer change the system without rediscovering it.
- **Verify like CI.** Tests, lint, typecheck, build, and manual evidence are the contribution.

### Freelancing

- **Sell an outcome, not a tool.** "AI agent developer" is a commodity; a measured outcome is a business.
- **Qualify before proposing.** Problem, urgency, budget, authority, fit, access, respect.
- **Price the risk and the value.** Know the floor, target, and walk-away.
- **Scope in writing.** Acceptance criteria, assumptions, exclusions, and change control.
- **Deliver with evidence.** Weekly updates, QA, handoff, case study, referral.
- **Do not fabricate proof.** A negative finding is more credible than a perfect story.

## Relationship to existing skills

The new suite does not replace the existing library. It composes it.

| Need | Existing skill |
| --- | --- |
| Senior engineering judgment | `senior-dev-os` |
| Repo conventions and agent readiness | `codebase-playbook` |
| Codebase knowledge graph | `understand`, `understand-chat`, `understand-diff`, `understand-explain`, `understand-onboard` |
| Debugging | `systematic-debugging` |
| Test-first development | `test-driven-development` |
| Test strategy | `testing-strategy` |
| Verification | `verification-before-completion`, `code-change-verification` |
| Code review | `requesting-code-review`, `receiving-code-review` |
| Design and frontend craft | `design-engineering` and its sub-skills |
| Documentation and handoff | `documentation-system`, `handoff` |
| Launch and rollback | `launch-readiness` |
| Research | `research`, `firecrawl-*` |
| Writing quality | `stop-slop` |

## Quality gates

### Before an OSS PR

- [ ] Project policies read
- [ ] Existing issue/PR searched
- [ ] Maintainer signal received for non-trivial work
- [ ] Reproduction is minimal and real
- [ ] Root cause is understood
- [ ] Regression test fails without the fix
- [ ] Full project gate passes
- [ ] Diff is focused
- [ ] Compatibility documented
- [ ] AI disclosure done if required
- [ ] PR tells the reviewer how to verify

### Before a freelance proposal

- [ ] ICP and buyer are specific
- [ ] Discovery covered problem, urgency, budget, authority, fit
- [ ] Outcome and success metric are measurable
- [ ] Scope, assumptions, exclusions, and acceptance criteria are written
- [ ] Price covers delivery, risk, fees, and margin
- [ ] Walk-away is known
- [ ] Payment and change-control terms are clear
- [ ] Proof is real and relevant
- [ ] Next step is one action

## Maintenance

```powershell
# List global skills
npx skills ls -g -a opencode

# Verify the new suite
Get-ChildItem "$HOME\.agents\skills" -Directory |
  Where-Object { $_.Name -match '^(oss-|large-codebase-|gsoc-|freelance-)' } |
  Select-Object -ExpandProperty Name
```

Skill files live at:

```text
C:\Users\Vishal\.agents\skills\<skill-name>\SKILL.md
```

Commands live at:

```text
C:\Users\Vishal\.config\opencode\commands\oss.md
C:\Users\Vishal\.config\opencode\commands\issues.md
C:\Users\Vishal\.config\opencode\commands\gsoc.md
C:\Users\Vishal\.config\opencode\commands\freelance.md
```

If `/oss`, `/issues`, `/gsoc`, or `/freelance` is not visible, restart OpenCode or run `opencode reload`.

## Related notes

- [[Freelancing and open source AI skills]] — the research report behind this suite.
- [[GSoC Strategy 2027]] — month-by-month campaign plan and proposal checklist.
- [[Agent skills AI engineers use]] — research report and full specification behind the `llm-release-gate` AI engineering add-on.
- [[OpenCode Skills]] — the full global skill index.
- [[Senior Developer Operating System]] — senior engineering lifecycle.
- [[Design Engineering Skills]] — UI/UX, design systems, frontend craft.
- [[REA Skill Setup Plan]] — reverse engineering for shipped artifacts.
- [[Freelancing Machine - Full Context and Playbook]] — the existing freelance operating context.

---

*Last verified: 2026-10-23. Global skill count: 93.*
