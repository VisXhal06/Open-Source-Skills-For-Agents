# Worked Examples

These are illustrative manifests, not real production results.

## Example 1 — Prompt Change, Medium Tier, SHIP

```json
{
  "change": {
    "class": "prompt",
    "summary": "Add refund-policy edge cases to the support prompt"
  },
  "claim": "This change improves refund-answer accuracy on policy-edge cases without regressing billing questions",
  "tier": "medium",
  "baseline": {"n": 40, "passed": 31, "tasks": []},
  "candidate": {"n": 40, "passed": 35, "tasks": []},
  "budgets": {
    "pass_rate_min": 0.80,
    "cost_per_task_max": 0.02,
    "latency_p95_ms_max": 2500
  },
  "evidence": [
    {"id": "regression_delta", "status": "present"},
    {"id": "hard_slice", "status": "present"},
    {"id": "cost_delta", "status": "present"}
  ],
  "risks": [],
  "rollback": {
    "steps": ["restore prompt v3 from prompt registry"],
    "owner": "ai-platform",
    "tested": true
  },
  "observability": {
    "trace_fields": ["prompt_version", "model", "retrieval_ids"],
    "alerts": ["p95 latency", "refund-policy eval delta"]
  }
}
```

Result: `SHIP`. Overall pass rate rises from 77.5% to 87.5%, the policy-edge slice rises from 70% to 78%, cost rises 6% but remains inside budget, and rollback is tested.

Why it ships: the claim names a slice and a guardrail, the required rows are present, the hard slice improved, and the rollback is executable.

## Example 2 — Model Upgrade, Medium Tier, BLOCK

```json
{
  "change": {
    "class": "model",
    "summary": "Upgrade the support assistant from model A to model B"
  },
  "claim": "Model B improves answer quality without regressing latency or policy compliance",
  "tier": "medium",
  "baseline": {"n": 40, "passed": 34, "tasks": []},
  "candidate": {"n": 40, "passed": 33, "tasks": []},
  "budgets": {
    "pass_rate_min": 0.85,
    "cost_per_task_max": 0.025,
    "latency_p95_ms_max": 2500
  },
  "evidence": [
    {"id": "regression_delta", "status": "present"},
    {"id": "hard_slice", "status": "missing", "owner": "eval-owner"},
    {"id": "cost_delta", "status": "present"},
    {"id": "capability_delta", "status": "present"},
    {"id": "judge_human_agreement", "status": "present"},
    {"id": "latency_cost", "status": "present"},
    {"id": "fallback", "status": "missing", "owner": "platform"}
  ],
  "risks": [
    {
      "severity": "high",
      "status": "open",
      "name": "No tested fallback if model B is rate-limited",
      "mitigation": "Add model A fallback and rerun",
      "owner": "platform"
    }
  ],
  "rollback": {
    "steps": ["switch model alias back to model A"],
    "owner": "platform",
    "tested": false
  }
}
```

Result: `BLOCK`.

Blockers:

- hard slice missing
- fallback missing
- open high-severity risk
- rollback not tested
- candidate pass rate is below baseline, and the confidence interval includes a meaningful regression

Smallest unblocking action: add 12 policy-edge tasks and a tested model-A fallback, rerun the gate, then review the latency delta.

## Example 3 — Retrieval Change, Medium Tier, BLOCK

```json
{
  "change": {
    "class": "retrieval",
    "summary": "Switch chunking from 800 to 400 tokens and add a reranker"
  },
  "claim": "The new chunking improves groundedness on long policy documents without increasing cost per task",
  "tier": "medium",
  "baseline": {"n": 40, "passed": 32, "tasks": []},
  "candidate": {"n": 40, "passed": 35, "tasks": []},
  "budgets": {
    "pass_rate_min": 0.85,
    "cost_per_task_max": 0.02
  },
  "evidence": [
    {"id": "regression_delta", "status": "present"},
    {"id": "hard_slice", "status": "present"},
    {"id": "cost_delta", "status": "present"},
    {"id": "recall_at_k", "status": "present"},
    {"id": "groundedness", "status": "present"},
    {"id": "index_rollback", "status": "missing", "owner": "search-platform"}
  ],
  "risks": [
    {
      "severity": "medium",
      "status": "open",
      "name": "Cost per successful task is up 40%",
      "mitigation": "Route long documents to the cheaper retriever",
      "owner": "ai-platform"
    }
  ],
  "rollback": {
    "steps": ["restore the previous index alias"],
    "owner": "search-platform",
    "tested": false
  }
}
```

Result: `BLOCK`.

Why: groundedness and recall improved, but the index rollback row is missing and rollback is untested. The cost regression is large enough that it would need a condition even after the rollback exists. The smallest unblocking action is to pin the previous index and prove a restore in staging, then rerun the gate with the cost budget.

## Pattern Summary

| Situation | Verdict |
| --- | --- |
| Clear gain, hard slice holds, rollback tested, budget met | SHIP |
| Good gain, one non-critical row missing, owner and expiry named | SHIP WITH CONDITIONS |
| Missing hard slice or rollback on a customer-facing change | BLOCK |
| High-severity risk with no mitigation | BLOCK |
| Underpowered sample on a high-tier change | BLOCK |
