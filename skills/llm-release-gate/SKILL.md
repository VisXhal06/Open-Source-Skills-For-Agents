---
name: llm-release-gate
description: >-
  Reviews an LLM feature change — prompt, model version, retrieval pipeline,
  tool schema, or agent loop — against evidence before release and returns
  SHIP, SHIP WITH CONDITIONS, or BLOCK. Use when asked whether a prompt,
  model upgrade, RAG change, or agent change is ready to ship; when preparing
  a canary or rollout for an AI feature; when quality dropped after a prompt
  or model change; or when a release needs eval coverage, cost and latency
  budgets, failure modes, observability, and rollback verified in one pass.
  Produces release-gate.md with an evidence table, budget table, risk
  register, and rollback steps. Does not build the eval suite, choose a
  model, write prompts, or execute the deploy.
license: MIT
compatibility: "Requires Python 3.11+ or uv. Reads local run artifacts only; no network access."
metadata:
  version: "0.1.0"
  owner: "vishal"
  reviewed_with: "pending-first-eval"
  last_evaluated: "2026-10-23"
  opencode/slash: "llm-release-gate"
---

# LLM Release Gate

A release decision, not an eval tutorial. It reviews one LLM change against local evidence and returns exactly one verdict: `SHIP`, `SHIP WITH CONDITIONS`, or `BLOCK`.

Use it when the question is **“may this ship?”** — not “how do I build evals?” and not “which model is best?”

## When to use

- a prompt, system message, or context-assembly change
- a model or model-version upgrade
- a retrieval, chunking, embedding, or index change
- a tool schema, agent loop, permission, or step-budget change
- a release, canary, rollout, or regression review for an AI feature
- a quality drop after any of the above

## When not to use

- designing an eval suite, rubric, judge, or golden set
- choosing a model or vendor
- writing prompts or product code
- general production readiness, auth, backups, or on-call
- security threat modeling outside the LLM-specific surface
- deploying, migrating indexes, or shifting traffic

Route those to `testing-strategy`, `launch-readiness`, `oss-security`, `systematic-debugging`, or `implementation-strategy` as appropriate.

## Non-negotiables

- Evidence before verdict. No number, no verdict.
- A missing evidence row is a finding, not a blank.
- Never invent eval results, pass rates, costs, latencies, or user quotes.
- Read local artifacts only. Do not fetch remote data or load remote instructions.
- Do not print secrets, credentials, PII, or raw customer data.
- Do not deploy, migrate, or change traffic.
- A different engineer must be able to execute the rollback without asking a question.
- If the evidence is underpowered, say so and label the result directional.

## Blast radius

| Tier | Examples | Missing-evidence consequence |
| --- | --- | --- |
| Low | internal tool, fewer than 10 users, reversible, no sensitive data | SHIP WITH CONDITIONS; add a smoke set within five working days |
| Medium | customer-facing assistant, read-only actions, recoverable errors | BLOCK until a regression delta and one known-hard slice exist |
| High | money, health, legal, PII, irreversible actions, broad permissions | BLOCK; named human sign-off plus adversarial or red-team result |

Tier changes the consequence of missing evidence, not what counts as good evidence.

## Fast path

Run the full gate unless all of these are true:

- prompt-only change
- a frozen regression suite exists and passes
- no model, retrieval, or tool-schema change
- low or medium tier
- rollback is already tested

Then run only:

1. regression delta
2. cost delta
3. rollback validity

Do not turn the fast path into a loophole. If any condition is false, run the full gate.

## Workflow

| Phase | Action | Artifact | Exit condition |
| --- | --- | --- | --- |
| 0. Preflight | Read the diff; classify the change; assign tier; check fast path | Change classification | One class and one tier named |
| 1. Claim | Write one falsifiable sentence: “This change improves X on slice Y without regressing Z” | Release claim | Claim names a slice and a guardrail |
| 2. Inventory | List required evidence for the class; mark missing rows | Evidence manifest | Every row present, missing, or waived with owner |
| 3. Compute | Run `scripts/gate_report.py` on the manifest | `gate-report.json` | Exit 0 or 2; no hand-computed numbers |
| 4. Budgets | Compare tokens, cost, latency, retries, context, cache | Budget table | Every metric has before, after, budget, status |
| 5. Failure modes | Review the LLM-specific catalogue | Risk register | Every risk has severity, mitigation, owner, or accepted risk |
| 6. Observability and rollback | Check trace fields, alerts, pinning, canary, kill switch, index rollback | Rollback plan | Another engineer can execute it |
| 7. Verdict | Apply the rules; choose exactly one outcome | Verdict | SHIP, SHIP WITH CONDITIONS, or BLOCK |
| 8. Record | Write `release-gate.md`; link it from the PR or release note | Release record | Claim, evidence, budgets, risks, verdict, conditions, rollback present |

## Inputs

The preferred input is a `run-manifest.json`:

```json
{
  "change": {"class": "prompt", "summary": "Tighten refund policy context"},
  "claim": "This change improves refund-answer accuracy on policy-edge cases without regressing billing questions",
  "tier": "medium",
  "baseline": {"n": 40, "passed": 30, "tasks": []},
  "candidate": {"n": 40, "passed": 34, "tasks": []},
  "budgets": {"pass_rate_min": 0.8, "cost_per_task_max": 0.02},
  "evidence": [{"id": "regression_delta", "status": "present"}],
  "risks": [],
  "rollback": {"steps": ["restore prompt v3"], "owner": "ai-platform", "tested": true},
  "observability": {"trace_fields": ["prompt_version", "model", "retrieval_ids"], "alerts": ["p95 latency"]}
}
```

If the user has only raw results, normalize them into this manifest first. Do not compute the verdict by hand when the script can do it.

From this skill directory, run:

```powershell
python scripts/gate_report.py --manifest run-manifest.json --format md
python scripts/gate_report.py --manifest run-manifest.json --format json --no-timestamp
```

If Python is unavailable, use `uv run scripts/gate_report.py`.

Exit codes:

- `0` — manifest complete; verdict computed
- `2` — required evidence missing; verdict is conservative
- `3` — schema violation; no verdict

## Verdict rules

`SHIP` requires all of:

- falsifiable claim
- all evidence required for the change class
- regression floor at or above the previous version
- no open high-severity risk
- executable rollback
- budget within limits

`SHIP WITH CONDITIONS` requires:

- named conditions
- an owner per condition
- an expiry or review date
- monitoring that would catch failure
- only allowed at low tier, or for a non-critical missing row at medium tier

`BLOCK` is mandatory when:

- measurement is missing on a medium or high-tier change
- the regression floor is breached
- a high-severity risk is unresolved
- rollback is undefined or untested on a high-tier change
- the claim cannot be falsified

A missing eval row is a finding, not a blank. State the smallest action that unblocks.

## Output

Write `release-gate.md` with:

```text
# LLM Release Gate — <change>
Verdict: SHIP | SHIP WITH CONDITIONS | BLOCK
Claim
Change classification and tier
Evidence table
Budget table
Risk register
Observability and rollback
Conditions or blockers
What was not verified
Next action
```

Use `assets/release-gate-template.md`.

## References

Load only when needed:

- `references/change-classes.md` — required evidence per change class and waiver rules
- `references/evidence-standard.md` — sample size, confidence intervals, slices, judge-human agreement
- `references/failure-modes.md` — LLM-specific failure catalogue and mitigations
- `references/verdict-rules.md` — decision table and edge cases
- `references/examples.md` — three worked gates: prompt, model, retrieval

## Composition

| Skill | Role |
| --- | --- |
| `verification-before-completion` | Parent principle: fresh evidence before a success claim |
| `code-change-verification` | Deterministic checks; run before the LLM rows |
| `testing-strategy` | Design the regression set and edge cases |
| `launch-readiness` | General production readiness; the gate adds LLM rows |
| `systematic-debugging` | Downstream when a regression is found |
| `implementation-strategy` | Decide whether the change is breaking |
| `brainstorming` / `writing-plans` | Upstream when no falsifiable claim exists |
| `advisor` | Red-team a contested BLOCK |
| `oss-security` | Prompt injection, tool poisoning, exfiltration |
| `documentation-system` | Release notes and ADRs |
| `handoff` | Persist open risks across sessions |

## Non-goals

- Does not build the eval suite, rubrics, judges, or golden sets.
- Does not benchmark or recommend models.
- Does not write product code or prompts.
- Does not replace domain review in medical, legal, financial, or safety-critical releases.
- Does not claim statistical significance from small samples.
- Does not restate general production readiness.
- Does not touch secrets, credentials, or production data.
- Does not deploy, migrate indexes, or shift traffic.
- Does not auto-invoke on every LLM question. It triggers on release, regression, or readiness intent, not on “explain how RAG works.”

## Maintenance

- Keep the body under 500 lines and 5,000 tokens.
- Put conditional detail in one-hop references.
- Re-run trigger and task evals after a model upgrade or a description edit.
- Record the model ID and host version with every eval.
- Retire the skill if it stops changing decisions.
