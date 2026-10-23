# LLM Failure Modes

Review this catalogue during phase 5. Not every row applies to every change. For each applicable row, record severity, mitigation, owner, and the evidence that the mitigation works.

## Output and Reasoning

| Failure | Symptom | Test | Mitigation |
| --- | --- | --- | --- |
| Invalid structured output | JSON parse error, missing field, wrong enum | Validate against a schema on every response | Schema validation, repair pass, typed tool output |
| Instruction drift | Model ignores a system constraint after a long context | Replay adversarial and long-context cases | Shorter instructions, pinned policy block, post-check |
| Reasoning-action mismatch | Explanation says one thing; tool call does another | Compare rationale with tool arguments | Tool-call validation, allowlists, human approval |
| Step repetition | Agent repeats the same tool call or plan step | Trace loop detection | Step budget, loop breaker, explicit completion check |
| Failure to stop | Agent continues after the task is complete | Completion criteria test | Stop condition, budget, verifier |
| Overconfident wrong answer | Fluent answer with no supporting evidence | Groundedness check and human sample | Retrieval citations, refusal rule, confidence threshold |

## Context and Retrieval

| Failure | Symptom | Test | Mitigation |
| --- | --- | --- | --- |
| Empty retrieval | No documents returned; model invents an answer | Empty-index and no-match cases | Refuse or ask, fallback to search, explicit empty state |
| Stale index | Answer reflects an old document | Compare index version to source version | Index pinning, freshness check, reindex job |
| Context overflow | Truncated instructions or missing evidence | Long-context boundary tests | Compression, ranking, section budgets, summarization |
| Conflicting context | Two documents disagree | Conflict fixtures | Source priority, citation, abstain |
| Retrieval drift | Recall changes after chunking or embedding | Recall@k on frozen queries | Freeze index, compare recall, rollback |
| Prompt injection in retrieved text | Document tells the model to ignore instructions | Adversarial corpus | Treat retrieved text as data, isolate instructions, output checks |

## Tools and Agents

| Failure | Symptom | Test | Mitigation |
| --- | --- | --- | --- |
| Tool error | Exception or timeout from a tool | Fault injection | Retry with backoff, typed error, fallback |
| Partial success | Side effect happened; response says failure | Idempotency test | Idempotency key, reconciliation, explicit status |
| Tool poisoning | Tool description or output redirects behavior | Malicious tool fixture | Tool allowlist, schema pinning, review tool metadata |
| Injection through tool output | Tool returns “ignore previous instructions” | Adversarial tool output | Treat output as data, sanitize, no instruction following |
| Unauthorized action | Agent calls a tool outside its scope | Permission matrix test | Least privilege, human approval, deny-by-default |
| Runaway loop | Cost and latency spike | Step and token budget test | Hard budget, loop detector, kill switch |
| Non-idempotent retry | Duplicate email, charge, or ticket | Retry after simulated timeout | Idempotency key, dedupe store, dry run |

## Operations

| Failure | Symptom | Test | Mitigation |
| --- | --- | --- | --- |
| Rate limit | 429s, retries, degraded answers | Load and burst test | Backoff, queue, quota, fallback model |
| Timeout | p95 latency breach | Latency test at p95 | Timeout budget, streaming, smaller model fallback |
| Cost regression | Cost per successful task rises | Cost delta | Prompt compression, caching, routing, budget alert |
| Model deprecation | Provider removes or changes a model | Pinned model and fallback test | Version pin, fallback, migration plan |
| Silent degradation | Pass rate looks fine; a slice regressed | Slice-level eval | Hard slices, online evals, alerts |
| Canary failure | Small rollout hurts users | Canary abort test | Abort criteria, kill switch, traffic rollback |

## Security and Privacy

| Failure | Symptom | Test | Mitigation |
| --- | --- | --- | --- |
| Prompt injection | User or document changes system behavior | Injection corpus | Instruction hierarchy, isolation, output policy |
| Data exfiltration | Model sends private data to a tool or URL | Egress test | Network deny, allowlist, redaction, human approval |
| Secret leakage | Key appears in output or logs | Secret scanner on traces | Secret management, redaction, no secrets in prompts |
| PII exposure | Customer data appears in logs or eval artifacts | Redaction check | Minimize, mask, retention policy |
| Tool supply chain | Third-party tool changes behavior | Pin and diff | Pin versions, review updates, sandbox |
| Over-broad permission | Agent can read or write too much | Permission matrix | Least privilege, scoped tokens, approval |

## Release Evidence

For each applicable failure, the gate needs one of:

- a test that covers it
- a monitoring signal that detects it
- a named accepted risk with an owner
- a blocker

“We will watch it” is not a mitigation unless there is an alert, a threshold, and an owner.
