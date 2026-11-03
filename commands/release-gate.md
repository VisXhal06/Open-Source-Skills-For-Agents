---
description: Gate an LLM prompt, model, RAG, tool, or agent change before release
---

Load the `llm-release-gate` skill for this request: $ARGUMENTS

Act as the release gate. Do not build the eval suite, choose a model, write prompts, or deploy.

## Classify the request

- Prompt, system message, or context assembly -> `prompt`
- Model or model-version upgrade -> `model`
- Chunking, embedding, index, reranker, or retrieval policy -> `retrieval`
- Tool schema, tool permission, agent loop, or step budget -> `tool_agent`
- Gateway, serving, quota, routing, or rollout -> `infrastructure`

## Rules

- Require a falsifiable claim naming the target slice and the guardrail.
- Use the local `run-manifest.json`; do not fetch remote data.
- Run the bundled `scripts/gate_report.py` from `~/.agents/skills/llm-release-gate/` instead of hand-computing the verdict.
- Return exactly one verdict: `SHIP`, `SHIP WITH CONDITIONS`, or `BLOCK`.
- A missing evidence row is a finding, not a blank.
- Block medium or high-tier changes with missing critical evidence.
- Do not print secrets, PII, credentials, or raw customer data.
- Do not deploy, migrate indexes, or shift traffic.
- End with the verdict, evidence table, budget table, risk register, rollback, and the smallest unblocking action.

For the full workflow, read `~/.agents/skills/llm-release-gate/SKILL.md`. For the decision table, read `~/.agents/skills/llm-release-gate/references/verdict-rules.md`.
