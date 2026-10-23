# Evidence Standard

The gate does not need a perfect eval suite. It needs enough evidence to make a defensible release decision and to name what is missing.

## Minimum Evidence

| Level | What it means |
| --- | --- |
| **Directional** | Fewer than 20 paired tasks, or a convenience sample. Useful for a low-tier internal change; never enough for a high-tier release. |
| **Usable** | 20–39 paired tasks, a frozen regression set, and at least one hard slice. Enough for a low- or medium-tier decision if the delta is clear. |
| **Strong** | 40+ paired tasks, multiple slices, confidence interval, and judge-human agreement. Enough for a medium-tier release and a high-tier discussion. |

The preferred starting point is 20–50 real tasks drawn from actual failures, not synthetic examples. Report the sample size and the comparison method.

## Pass Rate and Delta

- Report baseline and candidate pass rates.
- Report the delta in percentage points, not only the ratio.
- Use a bootstrap confidence interval for the delta. If the interval crosses zero, do not claim an improvement; label it directional.
- Do not compare different task sets. Use the same frozen set, or state the set changed and treat the result as a new baseline.
- If tasks are paired by ID, compare paired outcomes. If not, say so.

## Hard Slices

At least one known-hard slice must be reported separately:

- long-tail intents
- policy edge cases
- multilingual or accessibility cases
- empty or conflicting retrieval
- tool failure or partial success
- adversarial or injected input
- high-value or high-risk user segment

An overall pass-rate gain can hide a regression on the slice that matters. A gate that does not name a hard slice is incomplete.

## Judge-Human Agreement

If an LLM judge is used:

- label a sample by hand
- report agreement between judge and human
- target at least 0.80 agreement for a usable judge
- below 0.80, treat judge-only results as directional and add human review for the release decision
- report disagreement examples, not just the aggregate

## Cost and Latency

Report before and after:

- tokens per request, p50 and p95
- cost per request and cost per successful task
- latency p50 and p95
- retry rate
- context utilization
- cache hit rate, if caching is used

A quality gain that doubles cost or latency is a product decision, not an automatic ship. Compare against the stated budget, not against a vague “it feels fine.”

## Evidence Table

Use one row per required evidence item:

| ID | Status | Artifact | Owner | Note |
| --- | --- | --- | --- | --- |
| `regression_delta` | present | `evals/run-2026-10-23.json` | eval-owner | n=40, delta +3.2pp, CI [0.4, 5.8] |
| `hard_slice` | missing | — | retrieval-owner | no policy-edge slice yet |
| `cost_delta` | present | `reports/cost.json` | platform | +8% per successful task |

`present` means the artifact exists and was reviewed. It does not mean the result is favorable.

## Underpowered Results

When the sample is small:

- say “directional”
- do not use the word “significant”
- do not make a high-tier ship decision from it
- name the smallest test that would make the result usable

## Redaction

The gate reads local artifacts. Redact:

- customer names and identifiers
- secrets and API keys
- raw prompts containing PII
- production database rows
- private URLs and internal hostnames

If redaction makes the evidence unreadable, summarize the metric and keep the raw artifact out of the report.
