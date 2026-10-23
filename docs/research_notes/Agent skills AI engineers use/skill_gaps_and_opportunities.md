---
title: Agent Skills Landscape for AI Engineers — Gaps and Opportunities
type: research-notes
created: 2026-10-23
status: complete
confidence: mixed (labelled per claim)
---

# Agent Skills Landscape for AI Engineers — Gaps and Opportunities

**Scope.** Agent Skills (SKILL.md-style packs and marketplaces) as of **23 October 2026**, assessed for relevance to engineers building LLM applications, ML/MLOps systems, and AI platform/infrastructure. Excludes generic AI tools, MCP servers as a category, and prompt libraries that are not packaged as skills.

**Method.** GitHub REST API queries for repository metadata (23 Oct 2026); skills.sh leaderboard and topic pages; primary vendor docs (Anthropic, OpenAI Codex, OpenCode); two 2026 practitioner surveys; one 2026 job-market study; one security audit; Hacker News and practitioner blogs. Install and star counts are platform-reported, not independently audited.

**Confidence key.** [High] = primary source or direct API/doc observation. [Medium] = single credible secondary source or platform-reported metric. [Low] = marketing claim, single anecdote, or inference from incomplete data.

---

## 1. Which skill packs are most used, and why?

### Takeaway
Adoption is concentrated in **process/meta-workflow packs** (superpowers, mattpocock/skills), **official platform packs** (Anthropic, Vercel, OpenAI, Cloudflare), and **visual/design taste packs**. The winners are small, composable, and opinionated about *how to work*; none of the top packs is about building, evaluating, or operating LLM systems.

### Comparison table

| Pack | Scope | Reported reach (23 Oct 2026) | What it does well | Weakness / complaint | AI-engineering coverage |
|---|---|---|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers) | Full dev methodology: brainstorm → spec → plan → TDD → review → finish | 303,996 GitHub stars; 27,074 forks. Top skill installs: brainstorming 403.0K, systematic-debugging 304.9K, TDD 258.3K, verification-before-completion 250.3K ([skills.sh](https://skills.sh/), 23 Oct 2026) [Medium] | Enforces discipline; adversarial self-review; strong verification norm | Heavy ceremony; giant plan docs; "same Claude, not a silver bullet"; skills decay in long sessions | None. Assumes deterministic code |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Small, composable engineering habits (grill-me, tdd, triage, domain modeling, handoff) | 301,421 stars; grill-me 1.4M installs, tdd 1.1M ([skills.sh](https://skills.sh/)) [Medium] | Deliberately small and editable; "not vibe coding"; works across models; strong trigger names | Author-framed opposition to process frameworks; still code-centric | None |
| [anthropics/skills](https://github.com/anthropics/skills) | Official reference skills: docx/pdf/pptx/xlsx, frontend-design, skill-creator, mcp-builder, claude-api, webapp-testing | 183,181 stars; frontend-design 1.0M installs, skill-creator 413.4K ([skills.sh](https://skills.sh/)) [Medium] | Highest production quality; good progressive disclosure; canonical authoring guidance | Narrow, artifact- and API-focused; `claude-api` is reference docs, not an engineering workflow | Very low: one API-reference skill |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | React/Next.js performance, composition, web design, find-skills | 32,868 stars; find-skills 4.0M installs (the #1 skill on skills.sh) [Medium] | Distribution advantage via skills.sh; high-quality frontend rules | Frontend/Vercel-shaped; little model or eval content | Low |
| [openai/skills](https://github.com/openai/skills) | Codex skills catalog, incl. `skill-creator` and `$skill-creator` workflow | 28,266 stars ([GitHub API](https://api.github.com/repos/openai/skills)) [High] | Tight integration with Codex; eval-driven skill testing guidance | Codex-centric; thin public catalog | Low |
| [cloudflare/skills](https://github.com/cloudflare/skills) | Workers, Durable Objects, Agents SDK, Wrangler, Next.js on Workers | 3,150 stars ([GitHub API](https://api.github.com/repos/cloudflare/skills)) [High] | Accurate, product-scoped, immediately actionable | Platform-locked; infra primitives only, no model quality | None (platform only) |
| Eval-specific packs: [latitude-dev/eval-skills](https://github.com/latitude-dev/eval-skills), [Calibre-Labs/reforge-ai-evals](https://github.com/Calibre-Labs/reforge-ai-evals), QASkills catalog | Eval rubrics, trace annotation, judges, golden datasets, regression runs | 22 and 85 GitHub stars; QASkills lists 450+ skills with 500–2,000 installs each ([QASkills](https://qaskills.sh/skills-for/ai-llm-evals)) [High for stars; Medium for installs] | The *right* workflow shape: rubric → annotate → cluster failures → judge → align → golden set | Tiny distribution; single-discipline; tool-wrapper variants (Ragas/Promptfoo/DeepEval) dominate listings | **High but invisible** |
| Mega-packs: [affaan-m/ECC](https://github.com/affaan-m/ECC), [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills), alirezarezvani/claude-skills | 300–1,000+ skills across every domain | ECC 286,946 stars; VoltAgent 36,204 stars; alirezarezvani 28,583 stars ([GitHub search](https://api.github.com/search/repositories?q=agent+skills)) [Medium] | Breadth; one install covers many domains | Quality variance; context/metadata load; hard to audit | Scattered, mostly shallow |

### Cited findings
- The all-time skills.sh leaderboard is dominated by `find-skills` (4.0M), `grill-me` (1.4M), `agent-browser` (1.2M), `hyperframes` (1.2M), `tdd` (1.1M), and `frontend-design` (1.0M). **No eval, RAG, prompt-ops, or LLM-release skill appears in the top ~280 entries** — [skills.sh leaderboard](https://skills.sh/), accessed 23 Oct 2026. [High for the observation; Medium for install accuracy]
- superpowers' README describes itself as "a complete software development methodology for your coding agents" built from composable skills — [obra/superpowers](https://github.com/obra/superpowers). [High]
- mattpocock/skills explicitly positions against GSD, BMAD, and Spec-Kit: those "own the process… take away your control and make bugs in the process hard to resolve"; his skills are "small, easy to adapt, and composable" — [README](https://github.com/mattpocock/skills). [High, but vendor framing]
- Anthropic's official skills repo contains 19 skills; only `claude-api` and `mcp-builder` touch AI engineering, and both are reference/how-to rather than lifecycle workflows — [repo contents](https://api.github.com/repos/anthropics/skills/contents/skills), 23 Oct 2026. [High]
- Official platform packs are real but small in reach: Cloudflare 3,150 stars, Vercel 32,868, OpenAI 28,266 — [GitHub API](https://api.github.com/repos/cloudflare/skills), 23 Oct 2026. [High]
- The highest-signal eval packs are recent and small: latitude-dev/eval-skills (22 stars, 9 skills, explicit ordering from annotation → issue discovery → judge → alignment → golden dataset → regression runner) and Calibre-Labs/reforge-ai-evals (85 stars, 8-step loop with two human steps) — [README](https://github.com/latitude-dev/eval-skills), [README](https://github.com/Calibre-Labs/reforge-ai-evals). [High]
- Star counts above are unusually large in absolute terms (superpowers at ~304k would rank among the most-starred repos on GitHub). Treat **rank order** as meaningful and **absolute magnitude** as platform-reported and possibly inflated. [Low confidence on magnitude]

### Inferences
- Adoption follows **distribution plus a named pain**, not completeness: `find-skills` wins because it is the installer; `grill-me` wins because it names an interaction; TDD wins because it maps to an existing engineering habit.
- The "skills for real engineers" framing is winning because it promises **control and small surface area**, which is a direct reaction to heavyweight methodology packs.
- AI-engineering skills are not losing on quality — several are well designed — they are losing on **discoverability, naming, and scope packaging**.

### Gaps
- No public, audited install data by category; skills.sh does not expose a topic-level install total. Category-level demand is therefore inferred from leaderboard absence plus survey data, not measured directly.
- Cloudflare/Vercel/OpenAI do not publish adoption numbers for their official packs beyond star counts.

---

## 2. What is crowded, and what is missing, shallow, or generic?

### Takeaway
Crowded: design/taste, video/image generation, planning-and-TDD meta-workflows, enterprise connectors, database vendor docs, marketing, and skill-authoring itself. Missing: **LLM release engineering** — the evidence gate between "the eval passed" and "we shipped it" — plus RAG diagnosis, agent tool contracts, cost/latency SLOs, and quality-incident response.

### Category map

| Category | Status | Representative evidence |
|---|---|---|
| Design / visual taste / anti-slop | **Saturated** | `frontend-design` 1.0M installs; `design-taste-frontend` 663.6K; `high-end-visual-design` 458.8K; `impeccable` 354.8K — [skills.sh](https://skills.sh/) |
| Video / image / avatar generation | **Saturated** | heygen hyperframes family, runcomfy, ai-video-generation repeats across several republishers at 350K–1.2M installs — [skills.sh](https://skills.sh/) |
| Planning / TDD / review meta-workflows | **Saturated** | superpowers + mattpocock + GSD/BMAD/Spec-Kit clones |
| Enterprise connectors (Lark, Azure) | **Saturated by vendors** | open.feishu.cn 17.6M combined; microsoft/azure-skills 8.5M combined — [skills.sh](https://skills.sh/) |
| Database / ORM docs | **Crowded** | prisma skills ~370K each; supabase, neon — [skills.sh](https://skills.sh/) |
| Marketing / SEO / copy | **Crowded** | coreyhaines31/marketingskills, 56,160 stars — [GitHub](https://github.com/coreyhaines31/marketingskills) |
| Skill authoring / skill testing | **Crowded and good** | `skill-creator` 413.4K; OpenAI's eval-skills guide; this library already has `skill-creator` and `writing-skills` |
| Evals (tool wrappers) | **Crowded, shallow** | Ragas/Promptfoo/DeepEval/Langfuse wrappers, each 500–2,000 installs, one publisher — [QASkills](https://qaskills.sh/skills-for/ai-llm-evals) |
| Evals (workflow) | **Sparse but excellent** | latitude-dev (22★), Calibre (85★) |
| RAG design/diagnosis | **Shallow** | Vendor-shaped: Qdrant, Supabase, Neon skills teach their product, not retrieval diagnosis — [Qdrant skills release](https://qdrant.tech/blog/qdrant-skills-release/) |
| Prompt engineering | **Generic** | Mostly "write clearer prompts"; job ads weight it 29.1%, but a model already knows generic advice |
| Agent tool/schema contracts | **Missing** | No top pack covers idempotency, error surfaces, permission scopes, or mock-tool testing |
| LLM cost/latency budgets | **Missing** | `web-perf` covers frontend; nothing covers tokens/request, p95, routing, caching |
| Model/prompt change management | **Missing** | No diff-review, version pinning, or rollback workflow |
| Quality incident response | **Missing** | `systematic-debugging` is for deterministic bugs; no triage for "quality dropped 8% after model upgrade" |
| ML/MLOps gates (drift, retraining, serving) | **Missing** | No prominent skill; MLOps content lives in courses, not skills |
| AI security review | **Adjacent only** | `oss-security` covers code; no skill covers prompt injection, tool poisoning, data exfiltration in LLM apps |

### Cited findings
- Anthropic's own repo and the top community packs contain **no skill for LLM evaluation, release gating, or production quality operations**; the closest are `claude-api` (API reference) and `mcp-builder` (server construction) — [anthropics/skills contents](https://api.github.com/repos/anthropics/skills/contents/skills). [High]
- GitHub search for eval/RAG/AI-engineering skill repos returns a long tail under 100 stars, while general-purpose packs exceed 100,000 stars: `Calibre-Labs/reforge-ai-evals` 85, `ContextJet-ai/awesome-llm-observability` 42, `latitude-dev/eval-skills` 22 — [GitHub search](https://api.github.com/search/repositories?q=llm+evals+skill), 23 Oct 2026. [High]
- QASkills markets 450+ skills but its top eval skills are all by one publisher (`thetestingacademy`) and framed as tool integrations ("Ragas RAG Evaluation", "Promptfoo LLM Red Teaming") rather than decisions about what to measure — [QASkills](https://qaskills.sh/skills-for/ai-llm-evals). [High]
- vendor skills are documentation-shaped: Qdrant's release explains that "the standard RAG tutorial teaches a simple pattern" and its skills correct that pattern — useful, but product-anchored — [Qdrant](https://qdrant.tech/blog/qdrant-skills-release/). [Medium]
- The most common AI-engineer tasks in job ads are RAG (35.9%), prompt engineering (29.1%), LLM integration (25.4%), and agents (14.4%); evaluation appears in only 4.5% of ads — [AI Shipping Labs, 4 Mar 2026](https://aishippinglabs.com/blog/what-is-an-ai-engineer-based-on-job-descriptions). [Medium: 889 roles, one job board, Jan 2026]

### Inferences
- The market has solved **"how do I work with a coding agent"** and **"how do I make it look good"**, but not **"how do I know this LLM change is safe to ship"**.
- Job ads under-index evals relative to practitioner surveys, which suggests the pain is felt in production rather than written into hiring specs. That is exactly where a skill can create leverage: it encodes the work nobody puts in the JD.
- A new eval skill would duplicate existing work. A new **release-gate** skill composes with it and fills a real hole.

### Gaps
- No public taxonomy or install-weighted category data for AI-engineering skills; saturation judgments are based on leaderboard composition and repo counts.
- MLOps-specific skill usage (drift, retraining, feature stores) was not measurable — no prominent packs surfaced in search, but absence of evidence is not proof of zero use.

---

## 3. What do practitioners complain about?

### Takeaway
Six recurring complaints, each with a design implication: unreliable triggers, context bloat, generic/ceremonial advice, no verification loop, unsafe supply chain, and poor tool/environment assumptions.

### Cited findings

**3.1 Trigger reliability**
- Skill activation is LLM semantic matching, not deterministic routing: "you can't force-invoke… you can't prevent invocation… no visibility into decisions" — [paddo.dev, 4 Nov 2025, updated 10 Jan 2026](https://paddo.dev/blog/claude-skills-controllability-problem/). [Medium]
- OpenAI's own guidance: name and description "are the primary signals Codex uses to decide whether to invoke the skill at all"; "if these are vague or overloaded, the skill won't trigger reliably" — [OpenAI, Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills). [High]
- A 650-trial experiment claims skill activation has two distinct reliability problems and tests a fix — [Medium, 2026](https://medium.com/@marc.bara.iniesta/claude-skills-have-two-reliability-problems-not-one-299401842ca8). [Low: single author, method not independently replicated]
- Anthropic requires descriptions to state **what the skill does and when to use it**, in third person, because the description is injected into the system prompt and "inconsistent point-of-view can cause discovery problems" — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices). [High]

**3.2 Context bloat**
- Anthropic: "the context window is a public good"; keep `SKILL.md` under 500 lines; only metadata is preloaded — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices). [High]
- Metadata is not free: ~50 tokens per skill, so 10 skills = ~500 tokens before anything loads; an auto-invoked skill "might consume 10k tokens of context for instructions you didn't need" — [paddo.dev](https://paddo.dev/blog/claude-skills-controllability-problem/). [Medium]
- Cursor users report the agent auto-loading local skills at conversation start and consuming >50% of tokens — [Cursor forum thread](https://forum.cursor.com/t/excessive-token-usage-cursor-auto-loads-too-many-skills-from-claude-skills-at-conversation-start/160677). [Low: single bug report, vendor-specific]
- Practitioners describe "too many skills" as overwhelming and hard to prune — [r/ClaudeCode discussion](https://www.reddit.com/r/ClaudeCode/comments/1s0k1vj/too_many_skills/). [Low: thread content inaccessible (403); title and search snippet only]

**3.3 Generic / ceremonial advice**
- HN commenters on superpowers: plan mode produces "a giant plan document" that is "hard to review"; feedback regenerates the whole document; "Superpowers isn't the ideal solution because it too lacks flexibility" — [HN 47623101](https://news.ycombinator.com/item?id=47623101). [Medium: practitioner opinion]
- "I think Claude makes more mistakes when using superpowers than when not… It's still the same Claude" — same thread. [Low: single anecdote]
- Skills can decay in long sessions; users re-run `/using-superpowers` to re-activate — [Medium review](https://medium.com/@anilmathewm/i-gave-claude-code-a-brain-its-called-superpowers-and-it-has-150-000-github-stars-for-a-reason-16c4074a9209). [Low]

**3.4 No verification**
- "When you're iterating on a skill… it's hard to tell whether you're actually improving it or just changing its behavior… a regression slips in: the skill doesn't trigger, it skips a required step, or it leaves extra files behind" — [OpenAI](https://developers.openai.com/blog/eval-skills). [High]
- Anthropic: "Create evaluations BEFORE writing extensive documentation… This ensures your Skill solves real problems rather than documenting imagined ones" — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices). [High]
- The absence of evals is "the clearest anti-pattern" in production AI: 35% of AI teams do none, and teams with evals plus fast diagnosis are the most confident cohort (p<0.01) — [Inngest AI in Production 2026, 5 May 2026](https://www.inngest.com/blog/ai-in-production-report-2026). [Medium: n=130]
- A separate survey of 1,340 professionals found only 52.4% run offline evals, 37.3% online, and 29.5% do not evaluate at all — [LangChain State of Agent Engineering, 12 Jun 2026](https://www.langchain.com/state-of-agent-engineering). [Medium: self-selected sample]

**3.5 Security and supply chain**
- Snyk scanned 3,984 skills from ClawHub and skills.sh (as of 5 Feb 2026): **13.4% (534) had at least one critical issue; 36.82% (1,467) had any security flaw; 76 confirmed malicious payloads; 8 still live at publication** — [Snyk ToxicSkills, 5 Feb 2026](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/). [High for the audit; Medium for generalization beyond the corpus]
- Skills inherit full agent permissions: shell, filesystem, credentials, messaging, persistent memory. Publishing requires "a `SKILL.md` Markdown file and a GitHub account that's one week old. No code signing. No security review. No sandbox by default." — same source. [High]
- 91% of confirmed malicious skills combined prompt injection with malicious code; 10.9% of all ClawHub skills contained hardcoded secrets — same source. [High]
- Daily submissions rose from <50 in mid-January 2026 to >500 by early February — same source. [Medium]

**3.6 Tool and environment assumptions**
- Skills assume an empty directory, `npm` over other package managers, or that dependencies are installed; OpenAI recommends explicitly testing these assumptions — [OpenAI](https://developers.openai.com/blog/eval-skills). [High]
- Anthropic: do not assume packages are installed; use fully qualified MCP tool names (`ServerName:tool_name`) or the agent may fail to locate tools — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices). [High]
- Install-by-instruction (`curl | bash`-style) draws suspicion: "it's like curl|bash but with added LLM agents" — [HN 47623101](https://news.ycombinator.com/item?id=47623101). [Medium]

### Inferences
- The binding constraint on a new skill is **not content volume** — it is trigger precision, token economy, and a verifiable definition of done.
- A skill that outputs a **structured verdict with evidence** directly addresses complaints 3.3 and 3.4, and is testable in a way that "write better prompts" never is.
- Security posture should be part of the skill's design: no bundled binaries, no network fetches at runtime, no credential handling, no remote instruction loading.

### Gaps
- No large-N, vendor-neutral study of trigger precision across models. The strongest public evidence remains vendor guidance plus small experiments.
- Reddit and some practitioner forums blocked automated access; complaint evidence skews toward HN, vendor blogs, and one forum bug report. Treat frequency claims as directional.

---

## 4. What evidence supports the gap?

### Takeaway
Four independent signals converge: (a) AI-engineering skills are absent from adoption leaders; (b) the work is real and frequent; (c) quality is the top production barrier and evals are immature; (d) the existing eval skills are good but invisible.

### Cited findings

**Adoption signal**
- Zero AI-engineering/eval skills in the skills.sh top ~280; the category leaders are meta-workflow and design — [skills.sh](https://skills.sh/), 23 Oct 2026. [High]
- AI-engineering skill repos sit two to four orders of magnitude below general packs in stars: 22–85 vs 100,000–300,000 — [GitHub search](https://api.github.com/search/repositories?q=llm+evals+skill), 23 Oct 2026. [High]

**Demand signal (job tasks)**
- 889 unique AI Engineer roles, Jan 2026, five hubs: ~70% AI-first, 28.5% AI-support/platform, <2% traditional ML; 95.6% production-focused — [AI Shipping Labs](https://aishippinglabs.com/blog/what-is-an-ai-engineer-based-on-job-descriptions). [Medium]
- Skill frequencies: RAG 35.9%, prompt engineering 29.1%, LLM integration 25.4%, agents 14.4%, fine-tuning 8.5%, evaluation 4.5%; Python 82.5%, AWS 40.1%, Docker 31.0%, CI/CD 29.3%, Kubernetes 29.1%, vector DBs 10.8% — same source. [Medium]
- Core responsibilities explicitly include "make system behavior measurable with evaluation and monitoring" and "turn prototypes into reliable, observable services" — same source. [Medium]

**Pain signal (production)**
- 74% of AI teams had at least one customer-visible incident in the past 90 days vs 62% of non-AI teams; 20% of AI teams spend 26–50% of engineering capacity on reliability, twice the non-AI rate — [Inngest](https://www.inngest.com/blog/ai-in-production-report-2026). [Medium: n=130]
- 47% cite at least one eval-integration failure: results in a separate system (20%), no way to act on a failed eval (13%), offline evals disconnected from production (10%) — same source. [Medium]
- Quality is the #1 barrier to production (32%), ahead of latency (20%); cost has fallen as a concern — [LangChain](https://www.langchain.com/state-of-agent-engineering). [Medium: n=1,340]
- 69% of AI teams call LLM APIs directly or build their own abstraction rather than using an agent framework, and 26% say framework abstractions make failures harder to trace — [Inngest](https://www.inngest.com/blog/ai-in-production-report-2026). [Medium]

**Quality-tooling signal**
- Only 52.4% run offline evals; 37.3% online; 29.5% none. Among those evaluating, human review (59.8%) still outranks LLM-as-judge (53.3%) — [LangChain](https://www.langchain.com/state-of-agent-engineering). [Medium]
- Evals are the strongest statistical predictor of confidence alongside fast diagnosis; "not one unconfident team has both" — [Inngest](https://www.inngest.com/blog/ai-in-production-report-2026). [Medium]

**Supply signal**
- Good workflow-shaped eval skills exist but are new and small: latitude-dev 22★, Calibre 85★ — [GitHub](https://github.com/latitude-dev/eval-skills), [GitHub](https://github.com/Calibre-Labs/reforge-ai-evals). [High]
- The official Anthropic catalog has no eval skill; the closest is `claude-api` — [GitHub contents](https://api.github.com/repos/anthropics/skills/contents/skills). [High]

### Inferences
- The gap is **distribution plus lifecycle scope**, not absence of ideas. A new entrant should not compete with latitude/Calibre on "how to build evals"; it should own the decision that follows.
- The strongest wedge is the **release moment**: it is frequent (every prompt/model/retrieval change), high-stakes (customer-visible incidents), evidence-based (fits the verification culture already in the library), and currently unskilled.
- Job-ad under-weighting of evals (4.5%) is a lagging indicator; practitioner surveys and incident rates are leading indicators. Trust the latter for product decisions.

### Gaps
- No public data on how many teams have a formal LLM release process (canary, eval gate, rollback). The claim that this is rare is an inference from eval-adoption rates, not a direct measurement.
- No reliable install counts for AI-engineering skills by category; skills.sh does not publish a category rollup.
- Star counts in this ecosystem are unusually high and unverified; do not use them as a market-size estimate.

---

## 5. Candidate skill concepts (3–5) and recommendation

### Takeaway
Recommend **`llm-release-gate`**: a pre-ship evidence review for any LLM feature change. It is the only candidate that is (a) high-frequency, (b) not already well served, (c) verifiable, and (d) composable with both the existing 92-skill library and the emerging eval packs.

### Candidates

| # | Concept | Scope | Why it could win | Overlap / risk | Verdict |
|---|---|---|---|---|---|
| 1 | **`llm-release-gate`** | Evidence review before shipping a prompt, model, retrieval, or agent-tool change: eval delta, slice coverage, cost/latency budget, failure modes, observability, rollback; outputs ship / conditions / block | Every change passes through it; matches verification culture; testable output; no strong incumbent | Must not become a generic checklist; must delegate eval construction | **Recommended** |
| 2 | `llm-eval-foundations` | Build rubric, annotate traces, cluster failures, create/align judges, golden set, regression runner | Real pain; strong existing exemplars to learn from | Directly duplicates latitude-dev and Calibre; crowded tool-wrapper listings | Reject: late and duplicative |
| 3 | `rag-quality-diagnosis` | Diagnose retrieval failures: recall vs precision, chunking, hybrid search, rerank, metadata filters, query rewriting; measure before/after | RAG is the #1 job task (35.9%); vendor skills are product-shaped | Needs corpus access and a running system; hard to make deterministic; overlaps eval skills | Strong second choice |
| 4 | `agent-tool-contracts` | Design and verify tool schemas: idempotency, typed errors, retries, timeouts, permission scopes, mock-tool tests, injection resistance | Agents are 14.4% of jobs and rising; almost no coverage; complements `mcp-builder` and `agents-sdk` | Narrower audience; harder to trigger from natural language | Good third choice / future add-on |
| 5 | `llm-cost-latency-budget` | Model cost model, token budgets, caching, routing, streaming, p50/p95 targets, cost regression checks in CI | Cost/latency is a named production concern; complements `web-perf` | Could be a section of #1 rather than a standalone skill; smaller surface | Fold into #1 as a phase |

### Why #1 wins
- **Frequency:** every prompt edit, model upgrade, retriever change, and tool-schema change is a release event. That is weekly or daily for AI teams.
- **Evidence:** quality is the top barrier (32%) and incidents are common (74%); the missing layer is not measurement but the *decision* that measurement informs — [LangChain](https://www.langchain.com/state-of-agent-engineering), [Inngest](https://www.inngest.com/blog/ai-in-production-report-2026).
- **Fit:** the library already teaches "no completion claim without evidence" (`verification-before-completion`) and "run the checks" (`code-change-verification`). An LLM-specific evidence gate is the natural extension, not a new philosophy.
- **Differentiation:** latitude and Calibre answer "how do I build evals?"; this answers "given these evals, may I ship?" — a distinct job to be done.
- **Testability:** the output is a structured verdict with required evidence fields, so it can be evaluated with deterministic checks (does the verdict exist? are all required evidence rows present? did it block when eval delta was missing?).

### Inferences
- If the skill succeeds, the natural follow-ons are `rag-quality-diagnosis` and `agent-tool-contracts`, each invoked from a phase of the gate.
- A release gate also creates demand for the eval packs it depends on, which makes it complementary rather than competitive in the ecosystem.

### Gaps
- No direct survey evidence on how many teams would adopt a release-gate skill; the case rests on inferred frequency and observed eval immaturity.
- Competitive risk: a platform vendor (LangSmith, Vercel, OpenAI) could ship an equivalent gate as a product feature rather than a skill.

---

## 6. Fit with the existing 92-skill global library

### Takeaway
The library is deep in **how to engineer software** and **how to design interfaces**, and thin in **how to operate non-deterministic systems**. `llm-release-gate` fills the one missing layer without re-teaching anything already installed.

### What the library already covers (relevant neighbours)
From `~/.agents/skills` (92 skills, 23 Oct 2026):

| Existing skill | What it owns | Relationship to the new skill |
|---|---|---|
| `verification-before-completion` | No success claim without fresh evidence | **Parent principle.** New skill supplies the LLM-specific evidence types |
| `code-change-verification` | Run format/lint/type-check/build/test after changes | **Sibling.** New skill adds eval/cost/latency commands to the gate; should call it, not replace it |
| `testing-strategy` | Test levels, edge cases, flaky tests, test data | **Upstream.** Deterministic tests; new skill handles statistical/non-deterministic checks |
| `launch-readiness` | Security, data, reliability, observability, rollback, a11y | **Parent checklist.** New skill is the LLM annex; must not restate auth, backups, or on-call basics |
| `systematic-debugging` | Reproduce → isolate → hypothesise → test | **Downstream.** Used when the gate finds a quality regression |
| `implementation-strategy` | Scope and compatibility boundaries before runtime changes | **Upstream.** Decides whether a model/prompt change is a breaking change |
| `brainstorming` / `writing-plans` | Spec and plan | **Upstream.** Produces the success criteria the gate checks against |
| `web-perf` | Frontend Core Web Vitals and loading performance | **Adjacent.** Latency budgets overlap; new skill owns token and inference latency, not browser metrics |
| `agents-sdk`, `mcp-builder`, `durable-objects`, `workers-best-practices` | Agent and platform construction | **Complement.** New skill gates their output; should not teach Workers or MCP |
| `oss-security` | Threat modeling, authn/authz, injection, secrets | **Complement.** New skill adds LLM-specific threats: prompt injection, tool poisoning, data exfiltration via retrieved content |
| `advisor` | Second opinion / red-team review | **Escalation path** for a contested block verdict |
| `handoff` | Session continuity | **Persistence** for eval state and open risks |
| `documentation-system` | README, ADRs, runbooks, changelog | **Downstream.** Model/prompt changelog and release note |
| `skill-creator`, `writing-skills` | Authoring and testing skills | **Meta.** Use to build and eval the new skill itself |

### Composition points (explicit)
1. **Entry:** if no spec or success criteria exist → route to `brainstorming` / `writing-plans`.
2. **Evidence:** if no eval set exists → route to an eval pack (external) or mark the gate **blocked: no measurement**; do not fabricate a quality claim.
3. **Checks:** run `code-change-verification` for deterministic checks; add eval, cost, and latency commands.
4. **Production readiness:** defer general items to `launch-readiness`; only add LLM-specific rows.
5. **Regression:** on failure, hand off to `systematic-debugging` with the failing slice and trace IDs.
6. **Contest:** if the verdict is disputed, invoke `advisor` for a red-team pass.
7. **Record:** write the verdict + evidence into the release note via `documentation-system`; optionally `handoff` if the release spans sessions.

### Anti-duplication rules
- Do **not** teach TDD, planning, code review, or general debugging — the library has them.
- Do **not** re-implement Ragas/Promptfoo/DeepEval/Langfuse wrappers. Reference them as evidence sources, not procedures.
- Do **not** restate `launch-readiness` security/rollback lists. Link to them.
- Do **not** include generic prompt-engineering tips ("be specific", "use examples"). Models already know; it wastes context and dilutes triggers.
- Do **not** claim statistical validity from tiny samples. Require n and confidence intervals, or explicitly label results as directional.

### Inferences
- A gate skill raises the value of the library's existing verification skills by giving them a domain where evidence is hard to produce.
- Cross-links should be one level deep and few; Anthropic warns that nested references cause partial reads.

### Gaps
- No existing skill in the library covers model/prompt versioning or eval data management; the new skill must define minimal conventions (e.g., `evals/` layout, run manifest) without becoming a platform.

---

## 7. Proposed skill: name, trigger description, and core workflow

### Name
**`llm-release-gate`** (alternative: `shipping-llm-features`; prefer the noun-ish gate name for trigger precision).

Naming follows OpenCode rules: lowercase alphanumeric with single hyphens, 1–64 chars, matching the directory name — [OpenCode Agent Skills docs](https://opencode.ai/docs/skills), 23 Oct 2026.

### Trigger description (frontmatter, ≤1,024 chars, third person)
> Reviews an LLM feature or change — prompt, model, retrieval pipeline, tool schema, or agent loop — against evidence before it ships, and returns a ship / ship-with-conditions / block verdict. Use when asked whether an LLM feature, prompt, model upgrade, RAG pipeline, or agent change is ready for production; when preparing a release, canary, or rollout for an AI feature; when quality regressed after a prompt or model change; or when a team needs eval coverage, cost and latency budgets, failure modes, observability, and rollback verified in one pass. Produces an evidence table and a risk register; does not build the eval suite from scratch.

Why this shape:
- States **what** and **when**, in third person, with concrete trigger nouns and verbs — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).
- Includes negative scope in the last clause to reduce false positives, a documented failure mode — [OpenAI](https://developers.openai.com/blog/eval-skills).
- Fits the 1,024-character OpenCode/Agent Skills limit — [OpenCode docs](https://opencode.ai/docs/skills).

### Core workflow (SKILL.md body, target 180–260 lines)

**Phase 0 — Classify the change.**
Prompt text, model/version, retrieval (corpus, chunking, embedding, rerank), tool schema, agent loop, or infrastructure. Record the diff and the blast radius. If the change is not user-visible, say so and scale the gate down.

**Phase 1 — Establish the claim.**
Write the release claim in one sentence: "This change improves X on slice Y without regressing Z." If the team cannot state it, stop and route to `brainstorming`/`writing-plans`.

**Phase 2 — Inventory evidence.**
Required rows: eval set version and size; offline delta with n and CI; slice coverage (must include at least one known-hard slice); judge-human agreement if an LLM judge is used; adversarial/red-team result; production shadow or canary result if available. Missing rows are findings, not blanks.

**Phase 3 — Check budgets.**
Tokens per request (p50/p95), cost per successful task (not per call), latency p50/p95, retry and fallback rates, context utilisation, cache hit rate. Compare to the pre-change baseline on the same traffic mix.

**Phase 4 — Failure-mode review.**
Structured-output validation, timeouts, rate limits, context overflow, tool errors, empty retrieval, conflicting retrieved instructions (injection), partial tool success, and graceful degradation. Each gets a mitigation or an accepted-risk entry.

**Phase 5 — Observability and rollback.**
Trace fields sufficient to reconstruct a bad answer (prompt version, model version, retrieved doc IDs, tool calls, token counts); alert thresholds tied to eval metrics; prompt/model pinning; canary percentage and abort criteria; kill switch; data rollback if indexes changed.

**Phase 6 — Verdict.**
Exactly one of:
- **SHIP** — all required evidence present, no unresolved high-severity risk.
- **SHIP WITH CONDITIONS** — named conditions, owner, expiry, and monitoring.
- **BLOCK** — missing measurement or unresolved high-severity risk; state the smallest action that unblocks.

**Phase 7 — Record.**
Write `release-gate.md`: claim, change surface, evidence table, budget table, risk register, verdict, conditions, rollback steps. Link it from the PR or release note.

### Output template (required fields)
```
## Release gate: <feature / change>
Verdict: SHIP | SHIP WITH CONDITIONS | BLOCK
Claim: ...
Change surface: ...
Evidence: | Check | Result | n | Confidence | Source |
Budgets: | Metric | Before | After | Budget | Status |
Risks: | Risk | Severity | Mitigation | Owner |
Rollback: ...
Conditions (if any): ...
```

### Acceptance tests for the skill itself
Per OpenAI/Anthropic guidance, build evals before polishing prose:
- **Positive triggers (5–8):** "is this prompt ready to ship?", "we upgraded to the new model, can we deploy?", "did the RAG change regress anything?", "prepare a canary for the support agent".
- **Negative triggers (3–5):** "write an eval suite for this feature" (→ eval skill), "review this Python PR" (→ code review), "why is this unit test flaky?" (→ `systematic-debugging`).
- **Deterministic checks:** verdict field present; evidence table has ≥4 rows; a BLOCK verdict appears when eval delta is absent; no SHIP with an unresolved high-severity risk; output under ~700 tokens.
- **Quality checks:** budget table includes p95, not just averages; at least one hard slice named; rollback steps are executable, not "roll back if needed".
- **Token budget:** body under 500 lines; references one level deep; no time-sensitive model names in the main path — [Anthropic](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).

### Supporting files (progressive disclosure)
```
llm-release-gate/
  SKILL.md
  references/evidence-checklist.md     # what counts as acceptable evidence, by change type
  references/failure-modes.md          # LLM-specific failure catalogue + mitigations
  references/verdict-template.md       # release-gate.md template
  references/examples.md               # 3 worked examples: prompt change, model upgrade, RAG change
```
No scripts that fetch remote content; no credentials; no bundled binaries.

### Inferences
- The gate's value comes from **refusing to accept vibes**: a missing eval row produces BLOCK, which is more useful than a confident-sounding checklist.
- Naming the verdict states makes the skill legible to both engineers and non-technical stakeholders, which matches the "explain trade-offs to non-specialists" responsibility in AI-engineer job descriptions.

### Gaps
- No validated threshold for "enough" eval coverage; the skill should require *stated* coverage and slice rationale, not a universal number.
- Judge-human agreement thresholds vary by task; the skill should require reporting the metric and the decision rule, not impose one.

---

## 8. What the skill should explicitly not do

- **Not build the eval suite.** No rubric design, annotation workflow, judge creation, or golden-dataset curation. Route to an eval pack (latitude-dev, Calibre, or the team's own). This avoids duplicating the strongest existing work.
- **Not benchmark models or recommend a model.** Model choice depends on private cost, latency, and data constraints; the skill reviews the evidence for a chosen change.
- **Not write product code or prompts.** It reviews; implementation stays with the engineer and normal coding skills.
- **Not replace human judgement for high-stakes domains.** Medical, legal, financial, and safety-critical releases need domain review; the skill should force a named human sign-off.
- **Not promise statistical significance from small samples.** It must require n, the comparison method, and a confidence statement, and label underpowered results as directional.
- **Not restate general production readiness.** Auth, backups, on-call, accessibility, and infrastructure security belong to `launch-readiness`; duplication wastes context and creates drift.
- **Not teach generic prompt-engineering advice.** "Be specific", "use examples", "set a role" are already known and dilute the trigger.
- **Not touch secrets, credentials, or production data.** It reads eval artefacts and traces; it must not request keys, print environment variables, or fetch remote instructions.
- **Not run unbounded or destructive actions.** No automatic deploys, index migrations, or traffic shifts; it produces a verdict and a plan for a human to execute.
- **Not claim certainty about causes.** Attribute regressions to a change only when the evidence supports it; otherwise list competing hypotheses and the next diagnostic step.
- **Not auto-invoke on every LLM-related question.** Trigger on release/regression/readiness intent, not on "explain how RAG works".

---

## 9. Residual risks and open questions

1. **Market timing.** If LangSmith, Vercel, or OpenAI ship a native "release gate" product, a skill version loses differentiation. Counter-positioning: vendor-neutral, evidence-format-first, works with any eval stack.
2. **Adoption path.** The library is personal/global (92 skills). At 93, metadata cost rises slightly; the description must be tight and the skill should be prunable if unused.
3. **Evidence quality.** Two key surveys are self-selected (n=130 and n=1,340) and one job study covers a single board and five hubs. Directional, not representative.
4. **Star inflation.** Absolute GitHub star counts in this ecosystem look anomalous; do not cite them as market size. Use rank and category absence instead.
5. **Security posture.** A gate skill that reads traces could be pointed at sensitive data. It should default to redaction and local artefacts.
6. **Unanswered:** how often teams actually run a formal LLM release review; whether eval-gate skills improve outcomes (no published controlled study found); whether platform vendors will absorb this workflow.

---

## Source list (all accessed 23 Oct 2026 unless dated)

- https://github.com/obra/superpowers
- https://github.com/mattpocock/skills
- https://github.com/anthropics/skills
- https://github.com/vercel-labs/agent-skills
- https://github.com/openai/skills
- https://github.com/cloudflare/skills
- https://github.com/latitude-dev/eval-skills
- https://github.com/Calibre-Labs/reforge-ai-evals
- https://skills.sh/
- https://skills.sh/topic/agent-workflows
- https://qaskills.sh/skills-for/ai-llm-evals
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- https://opencode.ai/docs/skills
- https://developers.openai.com/blog/eval-skills
- https://www.inngest.com/blog/ai-in-production-report-2026 (5 May 2026)
- https://www.langchain.com/state-of-agent-engineering (12 Jun 2026)
- https://aishippinglabs.com/blog/what-is-an-ai-engineer-based-on-job-descriptions (4 Mar 2026)
- https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/ (5 Feb 2026)
- https://paddo.dev/blog/claude-skills-controllability-problem/ (4 Nov 2025, upd. 10 Jan 2026)
- https://news.ycombinator.com/item?id=47623101
- https://qdrant.tech/blog/qdrant-skills-release/
- https://forum.cursor.com/t/excessive-token-usage-cursor-auto-loads-too-many-skills-from-claude-skills-at-conversation-start/160677
- https://www.reddit.com/r/ClaudeCode/comments/1s0k1vj/too_many_skills/
- https://medium.com/@marc.bara.iniesta/claude-skills-have-two-reliability-problems-not-one-299401842ca8
