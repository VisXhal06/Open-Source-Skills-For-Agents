# Change Classes and Required Evidence

Use the change class to decide what evidence is required. A row is `present`, `missing`, or `waived` with an owner. Waiving a critical row is never allowed on a high-tier change.

## Evidence IDs

| ID | What it proves |
| --- | --- |
| `regression_delta` | Candidate pass rate minus baseline pass rate on a frozen regression set |
| `hard_slice` | A known-hard slice was measured and reported separately |
| `cost_delta` | Cost per successful task or per request, before and after |
| `capability_delta` | Target capability improved, not just overall pass rate |
| `judge_human_agreement` | Automated judge agrees with human labels often enough to trust it |
| `latency_cost` | p50/p95 latency and cost were measured for the model change |
| `fallback` | A tested fallback exists for model failure, timeout, or regression |
| `recall_at_k` | Retrieval recall at the chosen k, before and after |
| `groundedness` | Answers are supported by retrieved context, not just fluent |
| `index_rollback` | The previous index can be restored and is pinned |
| `tool_call_correctness` | Tool selection, arguments, and refusal behavior are correct |
| `injection_test` | Tool output and retrieved text cannot redirect the agent |
| `idempotency_retry` | Retries and partial tool success do not duplicate side effects |
| `step_budget` | Loop and step budgets are bounded and tested |
| `load_test` | Throughput, saturation, and error budget were measured |
| `error_budget` | Error budget status and alert thresholds are known |
| `canary_abort` | Canary percentage and abort criteria are explicit |
| `capacity_headroom` | Capacity headroom exists for the expected rollout |

## Required Evidence by Class

| Change class | Required evidence |
| --- | --- |
| `prompt` | `regression_delta`, `hard_slice`, `cost_delta` |
| `model` | `regression_delta`, `hard_slice`, `cost_delta`, `capability_delta`, `judge_human_agreement`, `latency_cost`, `fallback` |
| `retrieval` | `regression_delta`, `hard_slice`, `cost_delta`, `recall_at_k`, `groundedness`, `index_rollback` |
| `tool_agent` | `regression_delta`, `hard_slice`, `cost_delta`, `tool_call_correctness`, `injection_test`, `idempotency_retry`, `step_budget` |
| `infrastructure` | `regression_delta`, `hard_slice`, `cost_delta`, `load_test`, `error_budget`, `canary_abort`, `capacity_headroom` |

## Critical Rows

These rows are never waivable on medium or high tier:

| Class | Critical rows |
| --- | --- |
| `prompt` | `regression_delta`, `hard_slice` |
| `model` | `regression_delta`, `hard_slice`, `fallback` |
| `retrieval` | `regression_delta`, `hard_slice`, `index_rollback` |
| `tool_agent` | `regression_delta`, `hard_slice`, `injection_test` |
| `infrastructure` | `regression_delta`, `hard_slice`, `canary_abort` |

## Waiver Rules

- **Low tier:** a non-critical row may be waived with an owner and a five-day expiry. Missing critical rows still produce `SHIP WITH CONDITIONS`.
- **Medium tier:** only a non-critical row may be waived, with an owner and a review date. Missing critical rows produce `BLOCK`.
- **High tier:** no waivers. Every required row must be present, plus named human sign-off and an adversarial or red-team result where the domain requires it.
- A waiver is not evidence. It is an accepted gap with an owner.
- A missing required row without a waiver is a blocker, not a blank.

## Choosing the Class

Choose the class with the largest blast radius:

- prompt text or context assembly only → `prompt`
- model identifier, version, provider, or decoding settings → `model`
- chunking, embedding, index, reranker, or retrieval policy → `retrieval`
- tool schema, tool permissions, agent loop, or step budget → `tool_agent`
- gateway, serving, quota, routing, or rollout infrastructure → `infrastructure`

If a change spans classes, use the strictest class and add the additional rows.
