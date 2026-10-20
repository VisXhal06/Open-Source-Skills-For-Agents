---
name: research
description: Run structured deep research on any topic and produce a cited report. Uses built-in web search by default, with Firecrawl for crawling and Perplexity as an optional accelerator when its API is connected. Use for market analysis, competitive intelligence, literature reviews, technology comparisons, current events, or any request that needs sources rather than a from-memory answer.
license: MIT
compatibility: opencode
metadata:
  version: "1.1.0"
---

# Research

Turn a research question into a decision-ready, cited report. The default path is built-in web search plus reading the underlying pages. Firecrawl adds bulk crawling. Perplexity is optional and only used when its API is connected.

## Connection policy

Perplexity is not required. Never block research on it.

- **Default:** built-in web search, then open the most authoritative pages.
- **Firecrawl:** use `firecrawl-search`, `firecrawl-scrape`, or `firecrawl-crawl` only if the CLI is authenticated.
- **Perplexity:** use `perplexity_search`, `perplexity_ask`, `perplexity_research`, or `perplexity_reason` only if those tools are present and working.
- If a Perplexity call returns an auth error, stop calling it for the rest of the session. Do not retry in a loop and do not ask the user to complete OAuth mid-research. Continue with built-in search and note the limitation in the report.
- Never ask for, print, log, or store an API key.

> [!note] Why a Perplexity Pro login is not enough
> Perplexity's API and MCP server require an **API organization with pay-as-you-go billing**. A consumer Pro/Max subscription does not authorize API calls. The old monthly API credit for Pro subscribers was discontinued in February 2026. Do not suggest OAuth as a free fix.

## Preflight

1. Identify which tools are actually available: built-in web search, Firecrawl, Perplexity.
2. Default to built-in web search unless the user explicitly asks for Perplexity.
3. If no web access is available at all, answer from model knowledge and label it clearly as unverified. Do not fabricate citations.

## Choose the depth

| Need | Default path | Optional Perplexity path |
| --- | --- | --- |
| Quick fact, definition, sanity check | 1–2 searches, read the top source | `perplexity_ask` |
| Current landscape, comparison, news | 4–6 searches, open 3–5 pages | `perplexity_search` + `perplexity_ask` |
| Deep report, market analysis, literature review | 8–12 searches, open 8–12 primary pages | `perplexity_research` |
| Complex trade-off or architecture decision | Search plus an evidence table | `perplexity_reason` |

Tell the user a deep report can take 5–15 minutes and needs 8–12 sources. Do not cancel early.

## Workflow

### 1. Frame the brief

If the request is underspecified, ask up to three questions:

- What decision will this research support?
- What timeframe, geography, or market matters?
- What depth and output do you want?

If the user asks for speed, state your assumptions in one short block and proceed. Use `ask-questions-if-underspecified` when the ambiguity is expensive.

Write the brief as one sentence plus 3–6 subquestions. Example:

> Question: Should a small SaaS team migrate from REST to tRPC in 2026?
> Subquestions: migration cost, performance impact, ecosystem maturity, hiring pool, lock-in risk.

### 2. Plan the sources

Decide before searching:

- **Primary sources first:** official docs, changelogs, filings, papers, standards, pricing pages.
- **Recency window:** news and pricing need the last 3–12 months; foundational concepts do not.
- **Geography and currency:** state them explicitly for market or pricing work.
- **Exclusions:** vendor marketing, SEO listicles, undated posts, AI-generated summaries.
- **Source count:** at least 5 independent sources for a standard report; 10+ for deep research.

### 3. Gather

Run independent searches in parallel when the harness allows it. Open the most authoritative results; do not rely on search snippets for important claims.

Good query patterns:

- Landscape: `state of <topic> 2026`, `<A> vs <B> 2026`, `best <category> for <use case>`
- Evidence: `site:arxiv.org <topic>`, `site:docs.<vendor>.com <feature>`, `<topic> benchmark 2026`
- Market: `<market> size 2025 2026`, `<vendor> pricing`, `<vendor> competitors`
- Risk: `<topic> limitations`, `<topic> failure cases`, `<topic> security issues`
- Recency: add a month or year when freshness matters.
- Domains: restrict to primary sources with `site:` queries.

For deep mode:

1. Break the brief into 4–6 subquestions.
2. Run 2–3 searches per subquestion, in parallel where possible.
3. Open 8–12 primary pages and extract the evidence, dates, and caveats.
4. If Perplexity is connected, optionally call `perplexity_research` once with the full brief, then use its citations to find gaps. Verify its claims against the underlying pages.
5. Use `perplexity_reason` only for explicit trade-off analysis, not as a substitute for sources.

### 4. Verify before synthesizing

- Every key claim needs a source. Two independent sources for anything surprising or consequential.
- Open the underlying page for important claims; do not rely on a search snippet alone.
- Record publication or last-updated dates. A 2023 benchmark may be useless in 2026.
- Separate fact, estimate, and opinion.
- If sources disagree, present both positions and explain why they differ.
- Flag paywalls, inaccessible pages, and vendor bias.

### 5. Synthesize

Lead with the answer. Use this order:

1. **Bottom line:** 2–4 sentences.
2. **Key findings:** 3–7 bullets, each with a citation.
3. **Evidence table:** claim, evidence, source, date.
4. **Disagreements and uncertainty:** what experts or sources dispute.
5. **Confidence:** high, medium, or low, with the reason.
6. **What would change this answer:** the evidence to watch.
7. **Next steps:** what to verify, test, or decide.

### 6. Cite

Use numbered inline citations like `[1]` and a full source list:

```markdown
1. [Title](https://example.com) — Publisher, published 2026-03-14. Accessed 2026-10-20.
```

Cite the page you actually read. Do not invent titles, dates, or URLs. If a source is a PDF, link the PDF.

### 7. Save the report

Unless the user gives a path, save to:

```text
research/<slug>-<YYYY-MM-DD>.md
```

in the current project. If the working directory is the user's home folder, ask before creating a folder there. Create parent directories as needed.

Use this template:

```markdown
---
title: <report title>
date: <YYYY-MM-DD>
question: <one-sentence brief>
depth: quick | standard | deep
confidence: high | medium | low
sources: <count>
tags:
  - research
---

# <report title>

## Bottom line

## Key findings

## Evidence

| Claim | Evidence | Source | Date |
| --- | --- | --- | --- |

## Disagreements and uncertainty

## Confidence

## What would change this answer

## Next steps

## Sources
```

Report back with the file path and a 5-bullet executive summary. Do not paste the whole report into chat unless asked.

## Manual Perplexity path

If the user has a consumer Perplexity account but no API organization:

1. Ask them to run the deep-research prompt in the Perplexity app themselves.
2. Have them paste the report or export it.
3. Treat it as one source, verify its key claims against the cited pages, and keep the citations.
4. Never claim the agent called Perplexity when the user ran it manually.

## Project-aware research

When working inside a repository:

1. Read the README, manifests, and the code around the question first.
2. Include the real stack and versions in queries, for example `Next.js 16`, `React 19`, `Python 3.13`.
3. Compare options against the project's actual constraints, not a generic checklist.
4. Never send secrets, customer data, or proprietary source code to an external search tool. Summarize or redact first.
5. Link the saved report from the issue or PR when asked.

## Fallback order

1. **Built-in web search + page reading** — always available, always the default.
2. **Firecrawl** — if the CLI is authenticated; use `firecrawl-search` for discovery and `firecrawl-scrape` for pages.
3. **Perplexity** — only if its MCP tools are present and working.

State which path was used in the report's confidence section. Never claim a Perplexity tool was used when it was not.

## Failure handling

- **Perplexity auth error:** switch to built-in search for the rest of the session. Explain once that Perplexity needs an API organization with billing. Do not retry or loop.
- **Firecrawl not authenticated:** use built-in search. Do not run `firecrawl login` without asking.
- **Rate limit:** reduce scope, wait once, retry once, then fall back.
- **Timeout on deep research:** narrow the brief and retry, or split it into subquestions.
- **Thin results:** say the evidence is thin. Do not fill gaps with plausible-sounding claims.
- **Conflicting sources:** preserve the conflict; do not average it away.

## Quality bar

- No source, no claim.
- Primary over secondary; recent over stale.
- Specific over generic.
- Uncertainty stated, not hidden.
- The report should let someone make a decision without rereading every source.
