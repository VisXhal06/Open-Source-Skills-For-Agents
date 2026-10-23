# How AI Engineers Actually Work End-to-End (2026)

**Scope note.** This covers LLM/agent application engineering, ML/MLOps engineering, and AI platform/infrastructure. Evidence is dated where possible; survey dates are distinguished from page-publish dates because several 2026 pages report surveys fielded in late 2025. Evidence grades are marked inline: **[Peer-reviewed]**, **[Primary vendor]**, **[Survey]**, **[Practitioner opinion]**, **[Low confidence]**.

---

## What does "AI engineer" mean across companies? What archetypes and responsibilities exist?

### Takeaway
"AI engineer" is now a cluster of at least seven distinct roles unified by one thing: owning a system built on foundation models in production, not just a model in a notebook. The dominant archetype is a backend-leaning product engineer who owns retrieval, agents, evals, latency, and cost; classic ML engineering and MLOps/platform roles persist and are often conflated with it in job titles, which is a major source of mis-hires.

### Cited Findings
- A coding study of 1,000+ AI engineer job descriptions found 95.6% of roles are production-focused; roughly 50% are backend-heavy and about 20% full-stack. The author's working definition: "an AI engineer is an engineer who owns the design, evaluation, and production operation of systems built on foundation models." — [Alexey On Data, 4 Mar 2026](https://alexeyondata.substack.com/p/what-1000-job-descriptions-reveal)
- The same study groups work into three layers: core (end-to-end LLM apps, RAG, agents, APIs, deployment, monitoring, evals, guardrails), common (proprietary retrieval, data pipelines, internal AI platforms, agent workflows, product collaboration), and secondary (frontend, performance optimization, fine-tuning/self-hosting, customer implementations, security/compliance). — [Alexey On Data, 4 Mar 2026](https://alexeyondata.substack.com/p/what-1000-job-descriptions-reveal)
- A manual coding of 60 public JDs across the US, China, and Tokyo ranked requirements: Python 57/60 (95%), agents/tool calling/orchestration 53/60 (88%), RAG 50/60 (83%), backend/APIs 41/60 (68%), LangChain 37/60 (62%), vector DBs/embeddings 37/60 (62%), evaluation/observability/LLMOps 36/60 (60%), LangGraph 31/60 (52%), cloud 30/60 (50%), prompt/context engineering 28/60 (47%). TypeScript appeared in only 11/60 (18%); PyTorch/TensorFlow/HuggingFace in 12/60 (20%); fine-tuning/inference optimization in 15/60 (25%). — [SiBlog JD study, 28 Jul 2026](https://sinimite.work/en/posts/ai-engineer-job-market-2026/)
- OpenAI's Applied AI Engineer posting describes the role as taking "ambitious ideas from use-case selection and architecture through prototyping, evaluation, production launch, and scale," with explicit ownership of "model behavior, reliability, latency, cost, safety, security, governance, and operational readiness." Success is measured by "production systems, sustained adoption, and meaningful customer impact—not simply activity or successful demonstrations." — [OpenAI careers, 20 Oct 2026](https://openai.com/careers/applied-ai-engineer-digital-natives-paris-france/)
- Cornell's AI Engineer posting requires 3–5+ years of professional software engineering, agentic AI delivery, cloud-native experience, enterprise identity (OAuth 2.0, OIDC, SAML, JWT, LDAP), and Python/Node; preferred: vector DBs, orchestration frameworks, MLOps, containers, responsible AI and model governance. — [Cornell University job posting, 13 Oct 2026](https://jobs.hr.cornell.edu/us/en/job/CUICUGUSWDR00061808EXTERNALENUS/AI-Engineer)
- A 2026 hiring guide explicitly separates the role from data science: the AI engineer "both builds AI systems and uses AI to build those systems faster," and is expected to know RAG, agent orchestration, fine-tuning trade-offs, MLOps monitoring, and coding assistants. — [Rework job-description guide, 23 Oct 2026](https://resources.rework.com/libraries/job-description-templates/ai-engineer)
- Role distinctions are consistently drawn as: data scientist owns evidence/insight; ML engineer owns the model as a production system (pipelines, versioning, serving, retraining, drift); AI engineer owns AI product behavior (retrieval, tools, prompts/context, evals, guardrails, latency/cost, fallbacks). — [Dataxy, 1 Sep 2026](https://www.dataaxy.com/blog/ai-engineer-vs-machine-learning-engineer-vs-data-scientist); [Re:Sourced, 8 Jul 2026](https://www.resourced.com.au/articles/what-is-an-ai-engineer)
- A team-design guide argues the seat hired too late is "almost always MLOps or LLMOps," and that eval/prompt work is increasingly folded into the AI engineer rather than being a standalone hire. — [Resourcifi, 15 Jun 2026](https://www.resourcifi.com/insights/ai-engineering-team-structure/)
- Forward Deployed Engineer (FDE) is a distinct, growing archetype: embedded with customers, owning discovery through production, and feeding learnings back into product. OpenAI describes its FDE team as closing "the deployment gap" — "the distance between what models appear capable of and what people can reliably use to do their work." — [OpenAI, "What FDE means at OpenAI," 22 Oct 2026](https://openai.com/index/forward-deployed-engineering-means)
- FDE team topology is described as five responsibility nodes, not five mandatory hires: deployment lead, solution/build, platform/control, adoption/outcome, product learning. Artifacts (deployment brief, eval set, authority-and-control map, adoption plan, disposition record) are treated as the real interfaces between roles. — [Scott Felten, 27 Aug 2026](https://scottfelten.com/blog/design-fde-team-topology/)
- A caution on market-size claims: one vendor resource asserts AI-fluent demand is "up roughly 144% year over year" and commands a "56–80% wage premium," but provides no methodology. Treat as marketing, not measured labor economics. — [Rework, 23 Oct 2026](https://resources.rework.com/libraries/job-description-templates/ai-engineer) **[Low confidence]**

### Archetypes (synthesis of the above)

| Archetype | What they own | Typical org | Core skills | Evidence |
|---|---|---|---|---|
| **LLM product/application engineer** | Chat/assistant features, RAG, structured output, streaming, fallbacks, latency/cost | Product teams, startups, enterprise apps | Python, provider SDKs, FastAPI, retrieval, evals, tracing | [Alexey On Data](https://alexeyondata.substack.com/p/what-1000-job-descriptions-reveal); [SiBlog](https://sinimite.work/en/posts/ai-engineer-job-market-2026/) |
| **Agent engineer** | Tool calling, state machines, multi-step workflows, HITL, permissions | Product/platform, automation teams | LangGraph-style orchestration, tool schemas, MCP, context engineering | [LangChain](https://www.langchain.com/state-of-agent-engineering); [Saturn Cloud](https://saturncloud.io/blog/ai-engineering-tool-landscape-2026/) |
| **Applied / forward-deployed AI engineer** | Customer discovery, architecture, evals, production launch, adoption | Vendor field orgs, consultancies, regulated enterprises | Full-stack + domain learning + stakeholder management | [OpenAI FDE](https://openai.com/index/forward-deployed-engineering-means); [OpenAI Applied AI JD](https://openai.com/careers/applied-ai-engineer-digital-natives-paris-france/) |
| **ML engineer** | Training/fine-tuning, feature pipelines, serving, retraining, drift | ML-mature companies, ranking/recs/forecasting | PyTorch, Spark, feature stores, MLflow/W&B, Kubernetes | [Dataxy](https://www.dataaxy.com/blog/ai-engineer-vs-machine-learning-engineer-vs-data-scientist); [Sculley et al.](https://papers.neurips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf) |
| **MLOps / LLMOps / platform engineer** | CI/CD for models and prompts, registries, gateways, tracing, cost controls, rollback | Platform orgs, AI CoE | K8s, Terraform, OTel, eval infra, identity, quotas | [DORA 2025](https://dora.dev/research/2025/dora-report/); [Resourcifi](https://www.resourcifi.com/insights/ai-engineering-team-structure/) |
| **Eval / quality engineer** | Eval datasets, graders, red teaming, regression gates, transcript review | Larger AI product orgs | Statistics, LLM-as-judge calibration, CI, domain analysis | [Anthropic evals, 9 Jan 2026](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) |
| **AI infrastructure / serving engineer** | Inference, GPU capacity, routing, caching, gateways, reliability | Hyperscalers, model providers, large platforms | Distributed systems, serving, quantization, networking | [LangChain](https://www.langchain.com/state-of-agent-engineering); [Notion/Amplify/Vercel survey](https://www.notion.com/lp/ai-engineering-survey) |

### Inferences
- The title "AI engineer" is company-dependent enough that the only reliable way to scope a role is to ask which artifact the person owns: an eval suite and product behavior (AI engineer), a training/serving pipeline (ML engineer), or shared rails and guardrails (platform).
- The FDE archetype is the strongest evidence that "AI engineering" is partly a discovery and change-management discipline, not only a coding one. This matters for skills design: FDEs need reusable playbooks more than reusable code.
- Because only ~20–25% of JDs mention PyTorch or fine-tuning, the median "AI engineer" in 2026 is not doing model training. Classic ML engineering remains a real but narrower market.
- TypeScript is secondary in JDs but likely undercounted because "AI engineer" JDs skew backend; product-surface work (streaming UI, feedback capture, HITL) still requires frontend skills.

### Gaps
- No representative, methodology-transparent global sample of AI engineer titles exists. The 1,000-JD and 60-JD studies are self-published convenience samples with unclear geography weighting.
- LinkedIn "Jobs on the Rise 2026" is cited secondhand for AI engineer being the fastest-growing US job; I did not access the primary LinkedIn dataset, and growth-rate denominators are undefined.
- No reliable 2026 data on the split between AI application engineers, ML engineers, MLOps, and infra engineers by headcount.

---

## What is the end-to-end lifecycle?

### Takeaway
The lifecycle is a loop, not a pipeline: framing → data/context → architecture → prototype → eval harness → iterate → productionize → gate → launch → operate → cost/latency/model migration → simplify. The two stages teams most often skip — eval construction and production context governance — are also the two most consistently named as the reason projects stall.

### Lifecycle map

| # | Stage | Core work | Key artifacts | Exit gate | Common tools | Failure if skipped |
|---|---|---|---|---|---|---|
| 0 | **Problem framing & value case** | Define user, workflow, baseline, acceptable error, cost ceiling; decide whether a model is needed at all | Problem brief with baseline metric and accountable owner | A measurable outcome and an explicit "do nothing" option | Product analytics, interviews | Building an expensive AI layer for a logic problem ([Underdog, 8 Apr 2026](https://underdog.io/blog/ai-engineer-99c0c)) |
| 1 | **Feasibility & decomposition** | Split task into deterministic code vs model calls; decide single call vs workflow vs agent; buy vs build | Architecture sketch, risk list | Clear answer to "why an agent?" | Provider SDKs, notebooks | Agentic overkill; runaway loops ([Anthropic, building effective agents, 19 Dec 2024](https://www.anthropic.com/research/building-effective-agents)) |
| 2 | **Data & context foundation** | Corpus curation, permissions, freshness, chunking, semantic model, memory scoping | Context spec, access-control map, indexing pipeline | Can prove context is fresh and authorized | Ingestion pipelines, vector DB, semantic layer | Confident wrong answers from stale/partial context ([Redis, 2026](https://redis.io/resources/state-of-context-engineering-2026/)) |
| 3 | **Model & architecture selection** | Multi-model routing, open vs closed weights, RAG vs fine-tune vs long context, self-host vs API | Decision record with cost/latency/quality trade-offs | Reversible choice with a benchmark | OpenAI/Anthropic/Gemini APIs, HF, gateways | Lock-in or premature fine-tuning ([LangChain](https://www.langchain.com/state-of-agent-engineering)) |
| 4 | **Prototype / thin slice** | One end-to-end path, ugly but real; instrument from day one | Working demo + trace logs | Demo passes a small manual set | FastAPI, provider SDK, LangGraph/LlamaIndex | Demo that cannot survive real input shapes ([DORA](https://dora.dev/research/2025/dora-report/)) |
| 5 | **Eval harness** | 20–50 real tasks, reference solutions, deterministic graders first, calibrated LLM judges | Eval dataset, grader code, baseline scores | Two experts agree on pass/fail per task | pytest, promptfoo, DeepEval, Ragas, LangSmith/Braintrust | "Vibe-based evals"; no way to know if a change helped ([Anthropic, 9 Jan 2026](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)) |
| 6 | **Iterate** | Error analysis on transcripts; fix retrieval, context, tools, prompts in that order; add capability evals | Failure taxonomy, changelog | Capability curve improving; no regression drop | Trace viewers, notebooks | Tuning prompts when retrieval is the bottleneck ([Barnett et al.](https://arxiv.org/abs/2401.05856)) |
| 7 | **Productionize** | Streaming, caching, timeouts, retries with jitter, idempotency, rate limits, HITL, fallback paths | Service SLOs, runbook | Load test + failure injection pass | FastAPI, queues, Redis, gateways, K8s | Duplicate side effects, thundering-herd retries ([production stack notes](https://harut8.github.io/system-design/ai-rag/appendix-j-production-ai-stack/)) |
| 8 | **Pre-launch gates** | Safety/red team, cost model per task, latency budget, data-boundary review, rollback plan | Sign-off record | Named owner signs safety and failure modes | promptfoo red team, tracing, load tests | Security review fails late; unbounded spend ([LangChain](https://www.langchain.com/state-of-agent-engineering)) |
| 9 | **Launch** | Shadow mode → canary → A/B; capture feedback and transcripts | Experiment readout | Guardrail metrics within bounds | Feature flags, A/B infra | Big-bang launch with no baseline |
| 10 | **Operate & monitor** | Traces, online evals, drift, incident response, on-call, alert fatigue control | Dashboards, incident reviews | Error budget respected | OTel GenAI, LangSmith/Langfuse/Phoenix, Sentry | Silent quality decay ([LangChain](https://www.langchain.com/state-of-agent-engineering)) |
| 11 | **Cost/latency tuning & model migration** | Prompt caching, smaller models for subtasks, batching, routing, re-running evals on new models | Cost per successful task, p95 latency | New model passes regression suite | Gateways, eval suites | Freezing on an old model out of fear ([LangChain](https://www.langchain.com/state-of-agent-engineering)) |
| 12 | **Simplify / deprecate** | Replace custom glue with platform primitives; delete dead scaffolding; re-scope | Migration record | Less code, same outcome | Platform SDK, skills/plugins | Permanent bespoke maintenance ([OpenAI FDE](https://openai.com/index/forward-deployed-engineering-means)) |

### Cited Findings
- Anthropic recommends starting evals with **20–50 simple tasks drawn from real failures**, not hundreds, because early changes have large effect sizes; evals get harder to build the longer you wait. — [Anthropic, 9 Jan 2026](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- Anthropic distinguishes **capability evals** (low pass rate, "what can it do?") from **regression evals** (near-100%, "does it still work?"), and notes capability evals can "graduate" into regression suites after launch. — [Anthropic, 9 Jan 2026](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- Anthropic recommends grading **what the agent produced, not the path it took**, because agents find valid approaches designers did not anticipate; and building partial credit for multi-component tasks. — [Anthropic, 9 Jan 2026](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- The same post documents eval bugs materially distorting results: Opus 4.5 initially scored 42% on CORE-Bench due to rigid grading, ambiguous specs, and stochastic tasks; after fixes and a less constrained scaffold it reached 95%. — [Anthropic, 9 Jan 2026](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- Anthropic reports SWE-Bench Verified moved from ~30% to >80% within a year, illustrating **eval saturation**: at 100%, an eval tracks regressions but gives no improvement signal. — [Anthropic, 9 Jan 2026](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- Anthropic's operating model pairs **dedicated evals teams** owning infrastructure with **domain/product teams** contributing tasks and running evals. — [Anthropic, 9 Jan 2026](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- 89% of organizations have agent observability and 62% have detailed tracing, but only 52.4% run offline evals and 37.3% run online evals; 29.5% do not evaluate at all (22.8% among production teams). — [LangChain State of Agent Engineering, fielded 18 Nov–2 Dec 2025](https://www.langchain.com/state-of-agent-engineering)
- Among teams that do evaluate, 59.8% use human review and 53.3% use LLM-as-judge; traditional metrics like ROUGE/BLEU see limited adoption for open-ended agent work. — [LangChain](https://www.langchain.com/state-of-agent-engineering)
- RAG systems have seven empirically observed failure points: missing content, missed top-ranked documents, not-in-context, not-extracted, wrong format, incorrect specificity, incomplete. The authors conclude validation is "only feasible during operation" and robustness "evolves rather than [is] designed in at the start." — [Barnett et al., arXiv:2401.05856](https://arxiv.org/abs/2401.05856) **[Peer-reviewed]**
- A 2026 taxonomy extends this to **33 failure modes across 7 pipeline stages** (ingestion, representation, retrieval, generation, evaluation, deployment, agentic orchestration), finding 12 modes have no dedicated peer-reviewed evidence — all 8 agentic-orchestration modes among them. — [ACL Anthology, TrustNLP 2026](https://aclanthology.org/2026.trustnlp-main.27/) **[Peer-reviewed]**
- MLOps field study of 18 ML engineers identifies four stages — data preparation, experimentation, evaluation and deployment, monitoring and response — and finds deployment/maintenance is "highly iterative, manually-intensive, and team-oriented," with on-call rotations, manual guardrails, and multi-stage rollout with human authorization at each stage. — [NSF/par.nsf.gov, "We Have No Idea How Models will Behave in Production until Production"](https://par.nsf.gov/servlets/purl/10531529) **[Peer-reviewed]**
- A 2026 study of 13 ML practitioners identifies 23 engineering changes in notebook-to-production transitions and names **"oversight debt"**: notebooks externalize human oversight, and operationalization is the repayment — automated data assertions, snapshots, guardrails, structured logging. The authors argue this debt is structurally unavoidable, not a sign of poor practice. — [arXiv:2609.22903, 2026](https://arxiv.org/pdf/2609.22903) **[Peer-reviewed preprint]**
- Sculley et al.'s canonical ML technical-debt paper identifies boundary erosion, entanglement, hidden feedback loops, undeclared consumers, data dependencies, configuration issues, and external-world change as ML-specific maintenance risks. — [NeurIPS 2015](https://papers.neurips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf) **[Peer-reviewed]**
- Real deployments show stage 12 (simplify) is not theoretical: OpenAI reports removing ~90% of custom code per project by rebuilding on Codex primitives, turning a two-month initial deployment into a one-day extension to a second team. — [OpenAI, 22 Oct 2026](https://openai.com/index/forward-deployed-engineering-means)
- The same engagement reports evals moving from ~60% to 80% then 90%+ over six months as model capability improved, with the customer's evals as the shared definition of "production ready." — [OpenAI, 22 Oct 2026](https://openai.com/index/forward-deployed-engineering-means)

### Inferences
- The lifecycle's center of gravity has shifted from **model selection** to **context and evaluation**. Model choice is increasingly a routing decision; context assembly and grading are where engineering weeks are spent.
- Stage 5 (eval harness) should precede serious prompt work, not follow it. Teams that prototype first and eval later end up reverse-engineering success criteria from a live system, which Anthropic explicitly warns against.
- MLOps and LLMOps lifecycles are converging on the same shape (version, deploy, monitor, roll back), but LLMOps adds prompt/context versioning and token-cost attribution, while MLOps adds data/feature versioning and retraining cadence.
- The "oversight debt" finding explains a common AI engineering surprise: moving a working notebook or prototype into a service is not refactoring, it is rebuilding the human judgment that the interactive environment provided.
- A mature team should expect to delete a large fraction of its custom scaffolding within 12–18 months as platform primitives absorb it. Planning for that reduces sunk-cost resistance.

### Gaps
- No public, quantitative stage-by-stage time allocation for AI engineers in 2026. Claims like "80% of time on data" are folklore without a current time-diary study.
- Little evidence on how often teams actually perform stage 8 gates versus treating them as paperwork; most sources describe recommended practice, not observed compliance.
- Cost-per-successful-task benchmarks are not publicly standardized, so cross-company comparison is unreliable.

---

## How do AI engineers use coding agents and skills in daily work? What is delegated vs human-owned?

### Takeaway
Coding agents are the most-used AI tool in practitioners' daily workflows, but delegation is bounded: agents get code generation, test writing, documentation, investigation, and first-pass triage; humans retain architecture, eval design and interpretation, safety sign-off, and stakeholder judgment. Skills are emerging as the mechanism for packaging the *procedural* half of that work — and the strongest reported wins are consistency and reuse, not autonomy.

### Cited Findings
- Coding agents "dominate daily workflows": respondents named Claude Code, Cursor, GitHub Copilot, Amazon Q, Windsurf, and Antigravity for code generation, debugging, test creation, and navigating large codebases. Research/deep-research agents were second, and custom LangChain/LangGraph agents third. — [LangChain](https://www.langchain.com/state-of-agent-engineering)
- 84% of developers use or plan to use AI tools (up from 76%); 51% of professional developers use them daily; 31% currently use AI agents, 17% plan to, 38% have no plans. — [Stack Overflow 2025](https://survey.stackoverflow.co/2025/ai)
- Only 14.1% use agents daily at work; another 9% weekly and 7.8% monthly/infrequently. — [Stack Overflow 2025](https://survey.stackoverflow.co/2025/ai)
- 69% of developers who have used agents at work report a productivity increase. — [Stack Overflow press release, 29 Jul 2025](https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/)
- Developers resist delegating high-responsibility systemic work: 76% do not plan to use AI for deployment and monitoring, and 69% do not plan to use it for project planning. — [Stack Overflow 2025](https://survey.stackoverflow.co/2025/ai)
- 66% cite "AI solutions that are almost right, but not quite" as their top frustration; 45% say debugging AI-generated code is more time-consuming. (Note: Stack Overflow's blog post states these two numbers in the reverse order — 45% for "almost right," 66% for extra debugging time. The survey page and the 29 Jul press release support the 66%/45% pairing used here.) — [Stack Overflow 2025](https://survey.stackoverflow.co/2025/ai); [Stack Overflow blog, 29 Dec 2025](https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/)
- More developers distrust AI output accuracy (46%) than trust it (33%); only 3% "highly trust" it, and experienced developers are the most cautious. — [Stack Overflow 2025](https://survey.stackoverflow.co/2025/ai)
- DORA finds 90% use AI at work and >80% believe it improved productivity, but 30% report little or no trust in AI-generated code. — [DORA 2025](https://dora.dev/research/2025/dora-report/); [Google Cloud announcement, 23 Sep 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)
- DORA's central finding: AI is an **amplifier** — positively associated with throughput but still negatively associated with delivery stability; gains depend on testing, version control, fast feedback, and loosely coupled architecture. — [Google Cloud, 23 Sep 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)
- Notion/Amplify/Vercel's 2026 survey (1,053 responses, 16 May–15 Jun 2026) finds agents' write permissions rose from 52% to 90% year over year, but most still require human-in-the-loop; guardrails remain primitive (HITL approvals and permission gating are the top two). 61% say hallucinations are where agents fail most. — [Notion AI Engineering Survey](https://www.notion.com/lp/ai-engineering-survey)
- The same survey finds 48% say AI has most impacted **planning and spec writing**, and 28% say backend/API work — evidence that agents are used upstream and downstream of code, not only for code. — [Notion](https://www.notion.com/lp/ai-engineering-survey)
- A hiring guide's delegation split is explicit: agents handle code generation, test writing, documentation from codebase analysis, monitoring alerts/first-pass triage, scheduled pipeline execution, and draft PR/release notes. Humans own architecture and autonomy boundaries, safety/alignment review, stakeholder communication, escalation design, and the decision of when HITL is required. — [Rework, 23 Oct 2026](https://resources.rework.com/libraries/job-description-templates/ai-engineer) **[Practitioner opinion]**
- Anthropic's "safest" observed pattern for skills is **progressive disclosure**: only name + description load at startup (~50 tokens), full `SKILL.md` (~500 tokens) loads on match, and referenced files (~2,000+ tokens) load only when needed. — [Anthropic, 22 Jan 2026](https://claude.com/resources/articles/building-agents-with-skills-equipping-agents-for-specialized-work)
- Agent Skills launched 16 Oct 2025, became an open standard on 18 Dec 2025, and were donated to the Linux Foundation's Agentic AI Foundation on 22 Oct 2026. Anthropic reports 70+ agent platforms have integrated the standard, with ~1 million skills published and ~280 million installs. — [Anthropic, 22 Oct 2026](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation); [Anthropic engineering, 16 Oct 2025](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- OpenAI's FDE team reports replacing custom applications with **plugins and skills built on common Codex primitives**, retiring bespoke terminal UIs and CLIs; this is the mechanism behind the ~90% code reduction. Skills also covered eval creation ("building fresh evals (which we also had a skill for)"). — [OpenAI, 22 Oct 2026](https://openai.com/index/forward-deployed-engineering-means)
- Counter-evidence: LlamaIndex tested combining a documentation MCP with skills and found "skills were rarely invoked, and often did not yield substantially better" results; the docs MCP alone was sufficient, and skills needed constant updating in a fast-moving API surface. — [LlamaIndex, 3 Feb 2026](https://www.llamaindex.ai/blog/skills-vs-mcp-tools-for-agents-when-to-use-what)
- Skills fail **silently**: no error, no stack trace. Documented causes include wrong path, permissions, session restart needed, double-nested archive, description/relevance mismatch, truncation when many skill descriptions exceed an internal character budget, formatter damage to YAML frontmatter, and staleness. — [Aerospike, 31 Mar 2026](https://aerospike.com/blog/agent-skills-guide/)
- Skills have no native auth/credential model; a skill needing OAuth or secrets must pair with an MCP server or tool that owns auth. Network access also varies by host, so the same `SKILL.md` behaves differently across platforms. — [Aerospike, 31 Mar 2026](https://aerospike.com/blog/agent-skills-guide/); [Dockup, 15 Jan 2026](https://dockup.ai/blog/agent-skills-vs-mcp)
- Skills are natural-language instructions, so the agent decides *which, when, and how*; MCP tools are deterministic once selected. This is the core reliability trade-off. — [LlamaIndex, 3 Feb 2026](https://www.llamaindex.ai/blog/skills-vs-mcp-tools-for-agents-when-to-use-what)
- MCP context cost is the mirror-image problem: a standard multi-server setup can consume a large share of a 200K-token window before work begins (one analysis cites ~72% with GitHub + Playwright + IDE), and tool-selection accuracy reportedly falls from 43% to below 14% as tool count rises. — [Milvus, 1 Apr 2026](https://milvus.io/blog/is-mcp-dead-cli-and-skills-for-ai-agents.md) **[Practitioner analysis; numbers not independently verified]**

### Delegation boundary (synthesis)

| Work | Typically delegated to agent | Typically human-owned | Why |
|---|---|---|---|
| Code scaffolding, refactors, tests | Yes, with review | Final review and merge accountability | "Almost right" output is the top frustration ([Stack Overflow](https://survey.stackoverflow.co/2025/ai)) |
| Debugging / reproduction | First pass, log correlation | Hypothesis selection, production changes | Agents can widen search; humans own risk |
| Documentation, PR notes | Yes | Accuracy sign-off | Low blast radius |
| Eval task generation | Draft tasks, synthetic cases | Defining "good," calibrating judges, reading transcripts | Evals encode product intent ([Anthropic](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)) |
| Prompt/context iteration | Variant generation | Deciding what context is authoritative | Context is a governance decision |
| Architecture / autonomy boundaries | Option generation | Decision and accountability | Irreversible, cross-team |
| Safety, permissions, data boundaries | Checklist support | Sign-off | Security review is an owned gate ([LangChain](https://www.langchain.com/state-of-agent-engineering)) |
| Deployment & monitoring | Draft pipeline/config | Approval, rollback authority | 76% won't delegate this ([Stack Overflow](https://survey.stackoverflow.co/2025/ai)) |
| Incident triage | Alert summarization, first pass | Command decisions, comms | Accountability and context |
| Stakeholder communication | Drafts | Delivery and negotiation | Trust and judgment |

### Inferences
- The realistic 2026 pattern is **human-directed, agent-executed**: agents compress the inner loop (write, test, debug), while humans expand the outer loop (what to build, what "correct" means, what may act autonomously).
- Skills are best understood as **onboarding docs for agents**, not as tools. They raise consistency on procedures that are stable and repetitive; they do not guarantee execution.
- The strongest skill ROI evidence comes from platform-like environments (OpenAI FDE) where many similar deployments share procedures. The weakest evidence is fast-moving API surfaces, where a stale skill is worse than no skill.
- Because skills fail silently, teams need skill-level observability (did it load? did it trigger?) that most agent platforms do not yet provide. This is a genuine tooling gap.
- The MCP-vs-skills debate is mostly a false dichotomy: skills carry procedure, MCP/tools carry live data and authenticated action. Mature stacks use both.

### Gaps
- No controlled study measures skill-induced quality or speed gains for AI engineering tasks. Evidence is vendor case studies and practitioner anecdotes.
- No public data on what fraction of published skills are actively used, stale, or broken. The 1M/280M figures measure supply and installs, not efficacy.
- Unclear how skill invocation is traced in most observability platforms; I found no vendor documentation confirming first-class skill spans.

---

## What are the common failure modes and best practices?

### Takeaway
Failures cluster in three places: **specification** (ambiguous task/role design), **coordination** (agents misreading each other or the state), and **verification** (superficial checks, premature termination). The most expensive failures are not wrong answers but *confident, silent* wrong answers that reach a customer or a report. Best practice is layered verification plus error analysis on real transcripts.

### Cited Findings
- MAST (Multi-Agent System Failure Taxonomy), built from 1,600+ annotated traces across 7 frameworks, identifies **14 failure modes in 3 categories**: system design/specification, inter-agent misalignment, and task verification. Inter-annotator agreement κ = 0.88. — [arXiv:2503.13657](https://arxiv.org/abs/2503.13657) **[Peer-reviewed]**
- Failure distribution is balanced: FC1 specification 41.77%, FC2 inter-agent misalignment 36.94%, FC3 verification 21.30% — no single dominant cause. — [MAST project site](https://multi-agent-systems-failure-taxonomy.github.io/MAST/) **[Peer-reviewed]**
- Specific high-frequency modes: step repetition (15.7%), reasoning-action mismatch (13.2%), not recognizing task completion (12.4%), disobeying task specs (11.8%), incorrect verification (9.1%), no/incomplete verification (8.2%), task derailment (7.4%), premature termination (6.2%). — [arXiv:2503.13657](https://arxiv.org/abs/2503.13657)
- Interventions matter more than model swaps: improving agent role specifications alone yielded **+9.4%** success for ChatDev with the same model and prompt; adding a high-level objective verification step yielded **+15.6%** on ProgramDev. — [arXiv:2503.13657](https://arxiv.org/abs/2503.13657)
- Verifiers are often superficial: a generated chess program passed compilation checks but had runtime bugs because it was never validated against game rules. — [arXiv:2503.13657](https://arxiv.org/abs/2503.13657)
- Top production barrier is **quality** (32%), covering accuracy, relevance, consistency, tone, and policy adherence; **latency** is second (20%); cost has declined as a concern. For enterprises ≥2,000 employees, **security** is second (24.9%). — [LangChain](https://www.langchain.com/state-of-agent-engineering)
- For 10k+ employee orgs, write-in responses name hallucinations and output consistency as the biggest quality challenge, plus "context engineering and managing context at scale." — [LangChain](https://www.langchain.com/state-of-agent-engineering)
- 69% of enterprises running AI agents traced at least one confident-but-wrong answer to bad business context in the past six months; 41% traced more than one; 39% had a "high-impact failure" where the wrong answer reached a customer, partner, supplier, official report, or forced a reversed decision. — [VentureBeat VB Pulse, Sep 2026](https://venturebeat.com/vb-pulse-agentic-context-layers-report) **[Survey; vendor-sponsored]**
- 69% of enterprises consider an agent that cannot navigate across systems *more dangerous* than one that hallucinates. — [Redis State of Context Engineering 2026](https://redis.io/resources/state-of-context-engineering-2026/) **[Vendor survey]**
- Context failure modes are named as pollution (too much), starvation (too little), retrieval failure (wrong information), and structural incoherence (poorly organized); irrelevant documents can degrade performance below no retrieval at all. — [Replyant, 6 Apr 2026](https://replyant.com/lab/context-engineering/) **[Practitioner opinion]**
- Biggest obstacles to scaling agents: security/privacy 51%, tool integration complexity 43%, data fragmentation 41%, evaluation/observability gaps 37%, governance/compliance 34%, context-window limits 31%, talent 31%, latency/cost 29%. — [DataHub/TrendCandy, 250 leaders, Mar 2026](https://datahub.com/wp-content/uploads/2026/03/Report-State-of-Context-Management.pdf) **[Survey; vendor-sponsored, ±4% MoE]**
- 88% claim fully operational context platforms, yet 61% frequently delay AI initiatives for lack of trusted data and 87% cite data readiness as the biggest impediment — a self-assessment gap. — [DataHub/TrendCandy, Mar 2026](https://datahub.com/wp-content/uploads/2026/03/Report-State-of-Context-Management.pdf)
- MLOps failures include alert fatigue and "pipeline jungles" — accreted filters, checks, and transformations added over time. — [MLOps interview study](https://par.nsf.gov/servlets/purl/10531529) **[Peer-reviewed]**
- RAG failure points include retrieval ranking misses and consolidation dropping the answer before generation — i.e., the model is often blamed for an upstream data/retrieval defect. — [Barnett et al.](https://arxiv.org/abs/2401.05856)
- Only about one-third of organizations have begun scaling AI; 62% are at least experimenting with agents but just 23% are scaling an agentic system anywhere, and no more than 10% per business function. 39% attribute any EBIT impact to AI; ~6% qualify as high performers. — [McKinsey State of AI, 5 Nov 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025) **[Survey, 1,993 respondents]**
- McKinsey's strongest differentiator for high performers is **workflow redesign**, plus defined processes for when model outputs need human validation. — [McKinsey, 5 Nov 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025)

### Best practices (evidence-backed where possible)

1. **Define success before building.** Write eval tasks with reference solutions; if two domain experts would not agree on pass/fail, the task is underspecified. — [Anthropic](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
2. **Grade outcomes, not trajectories.** Path-checking produces brittle tests that punish valid solutions. — [Anthropic](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
3. **Layer verification.** Deterministic checks first, calibrated LLM judges second, human review for calibration and high-stakes cases. — [Anthropic](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents); [OpenAI eval guidance](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
4. **Read transcripts.** Scores without transcript review hide grader bugs and unfair tasks. — [Anthropic](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
5. **Diagnose at the failing layer.** Fix retrieval before prompting; fix context assembly before model choice. — [Barnett et al.](https://arxiv.org/abs/2401.05856)
6. **Instrument before launch, with PII policy.** Traces are a data store; set redaction, retention, and region before the first production trace. — [production AI stack notes](https://harut8.github.io/system-design/ai-rag/appendix-j-production-ai-stack/)
7. **Treat context as governed infrastructure.** Freshness, permissions, semantic definitions, and memory scoping are product requirements, not prompt details. — [Redis](https://redis.io/resources/state-of-context-engineering-2026/); [BARC/DataHub, 3 Sep 2026](https://datahub.com/news/barc-2026-study-context-engineering-agentic-ai/)
8. **Keep a human authorization boundary for actions with side effects.** Most teams still require HITL even as write permissions rise to 90%. — [Notion](https://www.notion.com/lp/ai-engineering-survey)
9. **Design for retries and idempotency.** Duplicate tool execution, partial graph completion, and checkpoint migration are named production failure classes. — [production AI stack notes](https://harut8.github.io/system-design/ai-rag/appendix-j-production-ai-stack/)
10. **Budget for oversight debt.** Moving from notebook to production requires automated substitutes for human inspection, not just code cleanup. — [arXiv:2609.22903](https://arxiv.org/pdf/2609.22903)

### Inferences
- Many "model quality" problems are actually **product specification problems**. MAST's +9.4% from role clarification and +15.6% from objective verification are larger than most prompt tweaks.
- The most under-invested failure mode is verification, despite being only ~21% of observed failures — because verification failures are the ones that reach users.
- Context failures are more dangerous than hallucinations in agentic settings because they produce *plausible actions*, not just plausible text.
- Security rising to #2 for large enterprises is a leading indicator that agents are moving from read-only assistants to actors with credentials and side effects.
- Organizations consistently overrate their context maturity; self-reported "AI-ready" numbers should not be used as evidence of actual readiness.

### Gaps
- MAST covers multi-agent systems; there is no equally rigorous taxonomy for single-agent RAG-plus-tools systems, though the ACL 2026 taxonomy begins to fill this.
- No public incident database quantifies how often agent failures cause financial or safety harm. The VentureBeat figure is survey-reported, not audited.
- Evidence on whether HITL actually improves outcomes (vs. creating rubber-stamp approvals) is largely absent.

---

## What metrics and quality gates matter?

### Takeaway
Teams need a small, layered scorecard: task success on a representative set, regression pass rate, groundedness/faithfulness, p50/p95 latency, cost per successful task, safety/refusal correctness, and operational reliability. The gate that matters most is not a single number but a **release contract**: which evals must pass, which require human sign-off, and what triggers rollback.

### Cited Findings
- Anthropic's eval stack maps methods to stages: automated evals pre-launch and in CI/CD; production monitoring post-launch for distribution drift; A/B testing once traffic suffices; user feedback and transcript review ongoing; human studies reserved for calibrating judges and subjective outputs. — [Anthropic, 9 Jan 2026](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- Anthropic explicitly invokes the **Swiss Cheese Model**: no single evaluation layer catches every issue. — [Anthropic, 9 Jan 2026](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- OpenAI's eval guidance lists five components (objective, dataset, metrics, run/compare, continuous evaluation) and anti-patterns: generic academic metrics, biased datasets, "vibe-based evals," and ignoring human feedback. — [OpenAI, evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- OpenAI recommends logging from the start so logs can be mined for eval cases, and maintaining agreement between automated scoring and human judgment. — [OpenAI](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- LLM-as-judge should be calibrated against human labels, given a way to say "Unknown," and ideally decomposed into per-dimension judges rather than one judge scoring everything. — [Anthropic, 9 Jan 2026](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- Eval saturation is a real gate risk: once a suite hits 100%, it detects regressions but no longer measures capability. — [Anthropic, 9 Jan 2026](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- Observability is near-universal (89%) but eval coverage is not (52% offline, 37% online), which is the clearest quality-gate gap in the data. — [LangChain](https://www.langchain.com/state-of-agent-engineering)
- Latency is now a first-class constraint (20% cite it as top barrier), driven by customer-facing agents and the quality/speed trade-off of multi-step reasoning. — [LangChain](https://www.langchain.com/state-of-agent-engineering)
- Cost remains real operationally even as it dropped as a *barrier*: three-quarters of 2026 survey respondents adjust AI usage based on cost, and 40% say cost regularly shapes how ambitiously they use AI. — [Notion/Amplify/Vercel](https://www.notion.com/lp/ai-engineering-survey)
- DORA's delivery metrics remain the right operational baseline: lead time for changes, deployment frequency, change fail rate, failed deployment recovery time, rework rate. AI adoption correlates with higher throughput and **higher instability**, so these gates become more important, not less. — [DORA 2025](https://dora.dev/research/2025/dora-report/)
- 90% of organizations have adopted at least one platform and 76% have dedicated platform teams; platform quality correlates with AI value capture. — [DORA 2025 / Google Cloud](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report)
- Context-specific quality metrics proposed in practice: tool-selection accuracy (first-attempt), response relevance, and token efficiency, tracked per request and aggregated weekly. — [Replyant, 6 Apr 2026](https://replyant.com/lab/context-engineering/) **[Practitioner heuristic, thresholds not validated]**

### Metrics scorecard (synthesis)

| Layer | Metric | What it catches | Gate style | Evidence/caveat |
|---|---|---|---|---|
| Task quality | Task success rate on representative set | Core capability | Capability eval; climb over time | [Anthropic](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) |
| Regression | Pass rate on frozen suite | Backsliding after prompt/model change | Near-100%; block release on drop | [Anthropic](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) |
| Retrieval | Recall@k, top-ranked inclusion, groundedness/faithfulness | Retrieval and attribution defects | Threshold per use case | [Barnett et al.](https://arxiv.org/abs/2401.05856); [Ragas-style metrics](https://harut8.github.io/system-design/ai-rag/appendix-j-production-ai-stack/) |
| Agent behavior | Tool-call correctness, loop/step count, termination correctness | Step repetition, derailment, premature stop | Budget caps + failure taxonomy review | [MAST](https://arxiv.org/abs/2503.13657) |
| Safety | Refusal correctness, prompt-injection resistance, data-boundary violations | Harmful or unauthorized action | Red-team suite + human sign-off | [LangChain security barrier](https://www.langchain.com/state-of-agent-engineering); [Anthropic course outline](https://anthropic-partners.skilljar.com/production-engineering-evals-security) |
| Latency | p50/p95 end-to-end, per-step attribution | UX degradation, slow retrieval/tools | SLO per request class | [LangChain](https://www.langchain.com/state-of-agent-engineering) |
| Cost | Cost per successful task, tokens/request, cache hit rate | Waste, runaway loops, model overkill | Budget per feature; alert on drift | [Notion](https://www.notion.com/lp/ai-engineering-survey); [Milvus on KV-cache economics](https://milvus.io/blog/is-mcp-dead-cli-and-skills-for-ai-agents.md) |
| Reliability | Error rate, timeout rate, duplicate side effects, recovery time | Production fragility | Error budget; rollback trigger | [DORA](https://dora.dev/research/2025/dora-report/); [production notes](https://harut8.github.io/system-design/ai-rag/appendix-j-production-ai-stack/) |
| Drift | Input distribution shift, freshness lag, quality trend | Silent decay | Weekly review; re-index/retrain trigger | [Anthropic](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents); [MLOps study](https://par.nsf.gov/servlets/purl/10531529) |
| Adoption | Task completion, escalation rate, time saved, retention | Whether anyone uses it | Post-launch outcome review | [OpenAI FDE](https://openai.com/index/forward-deployed-engineering-means); [McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025) |

### Inferences
- A release gate should combine a **hard regression floor** (near-100% on frozen tasks), a **capability trend** (is the hard set improving?), and **operational guardrails** (latency, cost, error budget). Any one alone is gameable.
- Cost per *successful* task is a better metric than cost per token because it captures retries and failures, which are where agent spend actually goes.
- Most teams can instrument traces faster than they can define quality. That asymmetry explains the 89%/52% observability-eval gap and is the single highest-leverage place to invest.
- DORA's instability finding implies AI feature releases need stricter change-failure tracking than traditional features, because the failure surface is probabilistic and often invisible in logs.

### Gaps
- No industry-standard benchmark for "AI engineer productivity" or "agent reliability" that is comparable across companies.
- Public data on real p95 latency and cost-per-task distributions by use case is scarce; most published numbers are vendor case studies with favorable selection.
- Safety metrics lack shared definitions (e.g., what counts as a "prompt injection success"), making cross-team gates hard to calibrate.

---

## How do AI engineers collaborate with product, data, platform, and security teams?

### Takeaway
Collaboration runs through **artifacts, not meetings**: a problem brief with a baseline, an eval set that encodes product intent, an authority/control map for agent actions, and a deployment record. The recurring organizational failure is unclear ownership at the production boundary — especially security, data access, and who may authorize an agent to act.

### Cited Findings
- FDE topology treats artifacts as the interfaces between roles: deployment brief (customer context → build), eval set (desired behavior → evidence), authority-and-control map (capability → permitted action), adoption plan (release → use), disposition record (field learning → product decision). Each needs one accountable party and an acceptance point. — [Scott Felten, 27 Aug 2026](https://scottfelten.com/blog/design-fde-team-topology/)
- A working FDE pod is described as one or two embedded engineers, a domain lead owning adoption and definition of done, a back-line product team that generalizes patterns, and engineering supervision tethered to the technical org to avoid "shadow IT." — [Monterail, 31 Aug 2026](https://www.monterail.com/blog/scaling-fde-teams-in-enterprise)
- IBM's guidance (cited by Monterail) puts effective pod size at two to five engineers with end-to-end responsibility, sized to "reduce the number of places where work pauses because ownership is fragmented." — [Monterail, 31 Aug 2026](https://www.monterail.com/blog/scaling-fde-teams-in-enterprise)
- FDEs should report to product or engineering with a dotted line to sales, "never the reverse," or the productization loop dies. — [Perspective AI, 12 Jun 2026](https://getperspective.ai/blog/the-forward-deployed-engineer-playbook-how-to-structure-run-and-scale-an-fde-function-in-2026) **[Practitioner opinion]**
- A modern AI team is sequenced, not fully staffed on day one: AI engineer, backend/data engineer, product owner at pilot; add MLOps/LLMOps, governed data, and a security seat as the pilot heads to production. — [Resourcifi, 15 Jun 2026](https://www.resourcifi.com/insights/ai-engineering-team-structure/)
- Security/governance responsibilities rise sharply near production: data access controls, prompt-injection defense, model risk, and audit readiness. — [Resourcifi, 15 Jun 2026](https://www.resourcifi.com/insights/ai-engineering-team-structure/)
- Agent authorization is an unsolved collaboration boundary: tracing can show an agent called an API, but not whether that delegation was authorized. The LangChain report is read by one commentator as documenting a missing authorization layer for multi-agent chains. — [Amla Labs analysis, 18 Dec 2025](https://amlalabs.com/blog/langchain-state-of-agents-2025/) **[Opinion/analysis]**
- Security is the #2 barrier for enterprises ≥2,000 employees (24.9%), ahead of latency. — [LangChain](https://www.langchain.com/state-of-agent-engineering)
- Security/privacy is the top obstacle to scaling agents (51%) in a 250-leader survey. — [DataHub/TrendCandy, Mar 2026](https://datahub.com/wp-content/uploads/2026/03/Report-State-of-Context-Management.pdf)
- Product's leverage point is evaluation: defining eval tasks is described as "one of the best ways to stress-test whether the product requirements are concrete enough to start building." — [Anthropic, 9 Jan 2026](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- Data teams own the semantic layer and freshness; BARC finds 42% of respondents are "context leaders," and those organizations are ~4x more likely to also be AI leaders (49% vs 12%). — [BARC/DataHub, 3 Sep 2026](https://datahub.com/news/barc-2026-study-context-engineering-agentic-ai/) **[Vendor-commissioned study]**
- Platform teams are the scaling mechanism: 90% platform adoption and 76% with dedicated platform teams, with platform quality correlating to AI value. — [DORA 2025 / Google Cloud](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report)
- McKinsey finds only ~6% of organizations are AI high performers, and workflow redesign is among the strongest differentiators — implying product/operations collaboration matters more than tool choice. — [McKinsey, 5 Nov 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025)

### Collaboration map (synthesis)

| Partner | What they own | What the AI engineer needs from them | Typical friction |
|---|---|---|---|
| **Product** | Outcome, acceptable error, prioritization | Concrete success criteria convertible to evals; decision on HITL vs autonomy | "Make it smarter" requests without a failure definition |
| **Domain experts** | Ground truth, edge cases, adoption | Labeled examples, reference solutions, transcript review | Availability; tacit knowledge not written down |
| **Data engineering** | Pipelines, warehouse, semantic layer, permissions | Fresh, governed, documented context; entity resolution | Data quality blamed on the model; access latency |
| **Platform / infra** | Gateway, identity, deploy, observability, quotas | Standard tracing, secrets, rollout, rollback | Bespoke glue; gateway limits; no eval env |
| **Security / compliance** | Threat model, data boundaries, audit | Injection tests, scoped credentials, action allowlists | Late review; binary approve/deny; no agent-specific policy |
| **Legal / privacy** | Retention, residency, PII | Redaction rules, trace retention, DPA constraints | Trace data conflicts with observability needs |
| **Support / ops** | Real failures, escalation | Failure transcripts, escalation paths | Feedback loop not instrumented |
| **FDE / customer team** | Workflow access, change management | Staging environment, discovery cadence, named decision-maker | Shadow IT; no owner after handoff |

### Inferences
- The highest-leverage cross-functional artifact is the **eval set**. It forces product to be concrete, gives data a target, gives security a test surface, and gives platform a regression gate.
- Security should be engaged at architecture time, not launch time, because agent authorization is an architecture property (scoped credentials, action allowlists), not a checklist.
- Platform teams convert individual AI productivity into organizational capability; without them, every team rebuilds retrieval, tracing, and guardrails.
- FDE-style roles Only work if there is a back-line product team to absorb generalizations; otherwise the org is running a consultancy, not building a platform.
- The "production boundary" is where ownership most often breaks: who is on call, who can roll back, who authorizes an agent action. Naming these explicitly is more valuable than another status meeting.

### Gaps
- No public study quantifies collaboration overhead (meetings, handoffs) for AI teams specifically.
- Evidence on security team maturity with agentic systems is anecdotal; no benchmark for "agent authorization readiness."
- Little data on how often product managers actually author or review evals versus delegating to engineers.

---

## Workflow pain points

### Takeaway
The pains are consistent across surveys and are mostly *systemic*, not model-capability problems: eval debt, context governance, silent failures, cost/latency pressure, and organizational pilot purgatory. The most-cited pain — "almost right" output — is a verification and specification problem more than a model problem.

### Cited Findings / pain inventory

| Pain | Evidence | Why it persists | Workaround observed |
|---|---|---|---|
| **Eval debt / observability-eval gap** | 89% observability vs 52% offline evals; 29.5% not evaluating — [LangChain](https://www.langchain.com/state-of-agent-engineering) | Defining "correct" is hard and cross-functional; traces are easier to buy than graders | Start with 20–50 real failures; dedicated evals team — [Anthropic](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) |
| **"Almost right" output** | 66% top frustration; 45% say debugging takes longer — [Stack Overflow](https://survey.stackoverflow.co/2025/ai) | Plausible-but-wrong is harder to detect than obviously wrong | Read transcripts; deterministic checks first |
| **Silent failure** | Skills/agents fail with no error or stack trace — [Aerospike](https://aerospike.com/blog/agent-skills-guide/) | Success is inferred from transport-level ACKs; no semantic check | Explicit terminal-state semantics; structured errors — [Dockup](https://dockup.ai/blog/agent-skills-vs-mcp) |
| **Context staleness & fragmentation** | 69% still feed critical decisions with stale data; 55% lack a reliable semantic model — [Redis](https://redis.io/resources/state-of-context-engineering-2026/); 41% cite data fragmentation — [DataHub](https://datahub.com/wp-content/uploads/2026/03/Report-State-of-Context-Management.pdf) | Context spans systems with different owners and refresh rates | Semantic layer, event-driven sync, freshness SLAs |
| **Context bloat** | MCP tool definitions can consume most of a large context window; tool-selection accuracy degrades as tools increase — [Milvus](https://milvus.io/blog/is-mcp-dead-cli-and-skills-for-ai-agents.md) **[unverified numbers]** | More tools/context feels safer; it degrades attention | Progressive disclosure, code execution over tool sprawl, retrieval-first |
| **Latency vs quality** | Latency #2 barrier (20%) — [LangChain](https://www.langchain.com/state-of-agent-engineering) | Multi-step reasoning improves quality but adds time | Smaller models for subtasks, caching, streaming, parallel calls |
| **Cost pressure** | 75% adjust usage on cost; 40% say cost shapes ambition — [Notion](https://www.notion.com/lp/ai-engineering-survey) | Retries, long contexts, and agent loops multiply spend | Cost per successful task; cache hit rate; model routing |
| **Non-determinism / debuggability** | MAST inter-agent failures 36.9%; reasoning-action mismatch 13.2% — [MAST](https://arxiv.org/abs/2503.13657) | Same input can take different paths; logs are huge | Trace trees, replay, step budgets, failure taxonomy |
| **Security & authorization** | Security #2 enterprise barrier; 51% cite security/privacy as top scaling obstacle — [LangChain](https://www.langchain.com/state-of-agent-engineering); [DataHub](https://datahub.com/wp-content/uploads/2026/03/Report-State-of-Context-Management.pdf) | Agents now take actions with credentials | Scoped tokens, action allowlists, HITL approvals |
| **Model churn / deprecation** | Multi-model is norm (75%+); 57% not fine-tuning — [LangChain](https://www.langchain.com/state-of-agent-engineering) | Providers change models, prices, and behavior | Regression suite run on every model change |
| **Prototype-to-production gap** | "Oversight debt" requires rebuilding human checks — [arXiv:2609.22903](https://arxiv.org/pdf/2609.22903); only ~1/3 of orgs scaling AI — [McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025) | Interactive oversight disappears in batch/service contexts | Automated assertions, snapshots, guardrails, structured logging |
| **Pilot purgatory / unclear ROI** | 39% report any EBIT impact; ~6% high performers — [McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025) | Use cases chosen for demo value, not workflow value | Workflow redesign; baseline metrics; named owner |
| **Alert fatigue / on-call for probabilistic systems** | MLOps interviews cite alert fatigue and pipeline jungles — [MLOps study](https://par.nsf.gov/servlets/purl/10531529) | Thresholds are noisy; failures are semantic | Sample traces not evals; keep all errors, sample successes |
| **Framework/tool churn** | Stack in flux; LangChain/LangGraph reached 1.0, observability consolidating — [Neural Dispatch, 2 Oct 2026](https://www.apollotechnologiesus.com/neural-dispatch/posts/top-10-ai-engineering-topics-2026) | Fast-moving ecosystem, breaking changes | Prefer protocols (OTel, MCP, Agent Skills) over frameworks |
| **Skill staleness / non-triggering** | Skills can fail to load, fail to trigger, truncate, or go stale — [Aerospike](https://aerospike.com/blog/agent-skills-guide/) | Markdown doesn't update itself; relevance scoring is opaque | Version skills with the code; test triggering; avoid for fast-moving APIs — [LlamaIndex](https://www.llamaindex.ai/blog/skills-vs-mcp-tools-for-agents-when-to-use-what) |
| **Hiring/title ambiguity** | AI engineer, ML engineer, MLOps conflated in JDs — [Dataxy](https://www.dataaxy.com/blog/ai-engineer-vs-machine-learning-engineer-vs-data-scientist) | Titles outran org design | Scope by artifact ownership, not title |

### Inferences
- The pain distribution suggests AI engineering is bottlenecked by **verification and governance**, not generation. Tools that only accelerate code generation address the least-constrained part of the loop.
- "Almost right" is expensive because it consumes senior attention; junior engineers are most exposed, which is why experienced developers report the highest distrust.
- Context pain is fundamentally an *organizational* problem (ownership, freshness, permissions) that no prompt or model upgrade fixes.
- Cost is not a top *barrier* but is a top *operational* constraint — a distinction many reports blur.
- Silent failure is the through-line between agent failures, skill failures, and context failures: the system does something plausible and gives no signal that it diverged.

### Gaps
- No reliable estimate of how much engineer time is lost to each pain; rankings are self-reported and susceptible to recency bias.
- Cost-per-task benchmarks by industry are absent.
- Evidence on whether eval investment actually reduces incidents (vs. just improving scores) is thin.

---

## Where agent skills genuinely help — and where they fail

### Takeaway
Skills help most when the **procedure is stable, repeated, org-specific, and expensive to re-explain** — eval authoring, RAG tuning, incident triage, provider migration, security review, deployment runbooks, and house conventions. They fail when the task needs guaranteed execution, live authenticated data, fast-moving APIs, or provable triggering — and they fail silently, which makes them dangerous in production-critical paths.

### Where skills genuinely help

| Use case | Why skills fit | Evidence |
|---|---|---|
| **Eval authoring & maintenance** | Procedure is stable and org-specific; output is inspectable; huge leverage per use | OpenAI FDE built "fresh evals (which we also had a skill for)" — [OpenAI](https://openai.com/index/forward-deployed-engineering-means); Anthropic ships an eval-building skill — [anthropics/skills](https://github.com/anthropics/skills/blob/main/skills/claude-api/shared/evals/build-eval.md) |
| **RAG/retrieval tuning playbooks** | Diagnostic order (corpus → retrieval → context → generation) is repeatable and easy to get wrong | Seven failure points provide a natural decision tree — [Barnett et al.](https://arxiv.org/abs/2401.05856) |
| **House conventions / architecture rules** | Prevents agents defaulting to training-data patterns (e.g., barrel imports) | Documented example of agents importing 1,583 modules without guidance — [Mintlify, 26 Jan 2026](https://www.mintlify.com/blog/why-do-we-need-mcp-if-skills-exist) |
| **Deployment/incident runbooks** | Multi-step, order-sensitive, needs checkpoints and escalation | Recommended as procedural knowledge, not tool calls — [Aerospike](https://aerospike.com/blog/agent-skills-guide/) |
| **Security review checklists** | Codifies threat model, injection tests, data boundaries | Security is a top barrier; review is procedural — [LangChain](https://www.langchain.com/state-of-agent-engineering) |
| **Onboarding & knowledge transfer** | Skills are "an onboarding guide for a new hire"; cheap to author, portable | [Anthropic, 16 Oct 2025](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) |
| **Cross-platform standardization** | Same skill works across Claude, Codex, Cursor, Copilot, VS Code (70+ platforms) | [Anthropic, 22 Oct 2026](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation) |
| **Non-engineer contribution** | PMs, analysts, domain experts can author Markdown procedures | [Anthropic, 22 Jan 2026](https://claude.com/resources/articles/building-agents-with-skills-equipping-agents-for-specialized-work) |
| **Replacing bespoke glue** | Skills/plugins on common primitives cut custom code and speed replication | ~90% code removed; 2 months → 1 day — [OpenAI](https://openai.com/index/forward-deployed-engineering-means) |

### Where skills fail

| Failure mode | Mechanism | Mitigation | Evidence |
|---|---|---|---|
| **Never loads** | Wrong path, permissions, nested folder, session restart needed | Validate install; `skill status`-style check | [Aerospike](https://aerospike.com/blog/agent-skills-guide/) |
| **Loads but doesn't trigger** | Description/relevance mismatch; broad or vague description | Write description as both *what* and *when* | [Aerospike](https://aerospike.com/blog/agent-skills-guide/); [Claude docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) |
| **Silent truncation** | Many skill descriptions exceed internal character budget | Raise budget; keep descriptions one line | [Aerospike](https://aerospike.com/blog/agent-skills-guide/) |
| **Staleness** | Markdown doesn't track API changes; wrong instructions are worse than none | Version skill with code; prefer MCP for fast-moving docs | [LlamaIndex](https://www.llamaindex.ai/blog/skills-vs-mcp-tools-for-agents-when-to-use-what) |
| **No auth** | Skills have no OAuth/credential model | Pair with MCP server that owns auth | [Aerospike](https://aerospike.com/blog/agent-skills-guide/) |
| **Non-determinism** | Natural language is interpreted, not executed | Use a tool when it must run the same way every time | [LlamaIndex](https://www.llamaindex.ai/blog/skills-vs-mcp-tools-for-agents-when-to-use-what) |
| **Host-dependent behavior** | Network access and secrets differ by platform | Test on target host; don't assume parity | [Aerospike](https://aerospike.com/blog/agent-skills-guide/) |
| **Skill sprawl / selection overload** | Many skills compete for relevance; agent picks wrong or none | Curate; scope tightly; measure trigger rate | [Milvus](https://milvus.io/blog/is-mcp-dead-cli-and-skills-for-ai-agents.md) |
| **Security risk** | Malicious skill can exfiltrate data or direct unsafe actions | Install only from trusted sources; audit bundled scripts | [Anthropic, 16 Oct 2025](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) |
| **Low marginal value** | Docs MCP already sufficient; skill adds little | Measure; don't add skills by default | [LlamaIndex](https://www.llamaindex.ai/blog/skills-vs-mcp-tools-for-agents-when-to-use-what) |
| **No native observability** | No standard span for "skill loaded/triggered/applied" | Log skill invocation in harness; test triggering in CI | **Inference** from absence in vendor docs — flag as gap |

### Decision rule (synthesis)

```
Does the task require live data or a credentialed action?
  YES → tool / MCP server (skill may wrap the procedure around it)
  NO  → Does it need to run identically every time?
          YES → deterministic script/tool, not a skill
          NO  → Is the procedure stable and repeated?
                  YES → skill
                  NO  → prompt or one-off instructions
```

This matches the most-cited practitioner guideline: "use a tool when the data changes between invocations, and a skill when the procedure stays the same" — [Aerospike](https://aerospike.com/blog/agent-skills-guide/); also [Dockup](https://dockup.ai/blog/agent-skills-vs-mcp), [Red Hat](https://developers.redhat.com/articles/2026/05/25/mcp-servers-vs-skills-choosing-right-context-your-ai).

### Inferences
- The best skill candidates are **diagnostic procedures**, not capabilities. "How to decide which RAG layer is failing" is a better skill than "search the docs."
- Skills have an unusually good cost/benefit for *organizational* knowledge because they are plain files that can be reviewed like code and authored by non-engineers.
- The biggest risk is not a skill doing something wrong; it is a skill **not running** and the team assuming it did. Skill observability is therefore a prerequisite for production use, not a nice-to-have.
- OpenAI's FDE result is the strongest existence proof for skills at scale, but it depends on a platform (Codex) with stable primitives and a team whose job is replication. Generalizing it to a single product team is not supported by evidence.
- For AI engineers specifically, skills are most valuable in the *meta* work — building evals, reviewing traces, migrating models, hardening security — because that work is procedural, repeated, and under-automated.

### Gaps
- No controlled measurement of skill efficacy, trigger rates, or maintenance cost. The 1M/280M figures are supply/install counts, not outcome data.
- No standard for skill versioning, testing, or signing; security guidance is still being drafted per Anthropic's AAIF roadmap.
- Unclear whether skills improve or degrade performance when many are installed; truncation anecdotes suggest a ceiling but no published benchmark.

---

## Tools and platforms that dominate (with caveats)

### Takeaway
The stack has consolidated around a few layers: Python + FastAPI for services, provider SDKs plus LangGraph-style orchestration for agents, pgvector or a dedicated vector DB for retrieval, OpenTelemetry-based tracing, and eval frameworks that fit into CI. Most teams buy inference and build prompt/context management. Framework choice matters far less than instrumentation and eval discipline.

### Cited Findings
- Inference/serving is the most commonly **bought** layer (45% bought, 37% happy; only 23% built) while **prompt management** is the most commonly built and least commonly bought. — [Notion/Amplify/Vercel, 2026](https://www.notion.com/lp/ai-engineering-survey)
- 81% use multiple models, but >50% report at least some standardization onto fewer AI tools. — [Notion](https://www.notion.com/lp/ai-engineering-survey)
- OpenAI models are used by more than two-thirds of organizations; 75%+ use multiple models in production or development; ~1/3 invest in self-hosting open models; 57% do no fine-tuning. — [LangChain](https://www.langchain.com/state-of-agent-engineering)
- OpenAI GPT models were used by 81% of Stack Overflow respondents; Claude Sonnet 43%; Gemini Flash 35%. — [Stack Overflow 2025](https://survey.stackoverflow.co/2025/technology)
- Agent frameworks in 2026 are categorized as: LangGraph (explicit state graph, persistence, HITL, rollback), CrewAI (role/task crews), AutoGen (conversational multi-agent), LlamaIndex (RAG-first), and vendor SDKs (Claude Agent SDK, OpenAI Agents SDK). — [Saturn Cloud, 3 Jun 2026](https://saturncloud.io/blog/ai-engineering-tool-landscape-2026/)
- Vector DB shortlist: Pinecone (managed), Qdrant (price/performance, filtered search), Weaviate (hybrid, multi-tenancy), Chroma (developer-first, <~1M vectors), pgvector (stay in Postgres). Filtered-search latency is described as a better differentiator than raw recall. — [Saturn Cloud, 3 Jun 2026](https://saturncloud.io/blog/ai-engineering-tool-landscape-2026/)
- pgvector is consolidating the category at ~1M vectors; dedicated engines still win at tens of millions, strict latency, or heavy filtered search. — [Neural Dispatch, 2 Oct 2026](https://www.apollotechnologiesus.com/neural-dispatch/posts/top-10-ai-engineering-topics-2026) **[Practitioner analysis]**
- Observability platforms: LangSmith (deep LangChain/LangGraph, SaaS by default), Langfuse (open source, self-hostable, MIT), Arize Phoenix (OTel/OpenInference, retrieval views), Braintrust (experiment-first), Helicone (proxy), plus libraries Ragas, DeepEval, promptfoo. — [Saturn Cloud](https://saturncloud.io/blog/ai-engineering-tool-landscape-2026/); [production AI stack notes](https://harut8.github.io/system-design/ai-rag/appendix-j-production-ai-stack/)
- OpenTelemetry GenAI semantic conventions and OpenInference are converging as the vendor-neutral trace format, so a LangGraph span and a raw API span look the same across backends. — [Neural Dispatch, 2 Oct 2026](https://www.apollotechnologiesus.com/neural-dispatch/posts/top-10-ai-engineering-topics-2026)
- Market consolidation: ClickHouse acquired Langfuse (MIT license retained) alongside a $400M Series D; Dynatrace agreed to acquire Arize for $915M. — [Neural Dispatch, 2 Oct 2026](https://www.apollotechnologiesus.com/neural-dispatch/posts/top-10-ai-engineering-topics-2026) **[Secondary reporting; deal terms not independently verified]**
- LangChain and LangGraph both reached 1.0 and split jobs: LangChain for high-level building blocks, LangGraph for stateful graph workflows with checkpoints, HITL interrupts, and streaming. — [Neural Dispatch, 2 Oct 2026](https://www.apollotechnologiesus.com/neural-dispatch/posts/top-10-ai-engineering-topics-2026)
- LangChain adds roughly 40–80ms overhead per chain step versus calling the API directly — material for p99-sensitive user-facing features, irrelevant for background pipelines. — [Akava, 21 Apr 2026](https://akava.io/blog/building-with-llms-the-new-full-stack-engineers-toolbox) **[Practitioner benchmark, single source]**
- Python usage rose 7 percentage points in Stack Overflow 2025, alongside Rust and Go (+2), all used in AI development and infrastructure. — [Stack Overflow blog, 29 Dec 2025](https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/)
- TypeScript appears in only 18% of AI engineer JDs, versus Python at 95%. — [SiBlog, 28 Jul 2026](https://sinimite.work/en/posts/ai-engineer-job-market-2026/)
- Stack Overflow's new AI-agent data storage question found Redis (43%) and GitHub MCP server (43%) as top choices, with Sentry (32%) and New Relic (13%) adapted for agent observability. — [Stack Overflow blog, 29 Dec 2025](https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/)

### Stack map (synthesis)

| Layer | Default choice | Alternatives | Decision driver |
|---|---|---|---|
| Language | Python | TypeScript (product surface), Go/Java (platform) | JD frequency; ecosystem |
| Service | FastAPI + Pydantic | Node/TS, existing backend framework | Team's existing stack |
| Model access | Provider SDKs | Gateway/proxy, multi-model router | Cost, latency, failover, residency |
| Orchestration | LangGraph for stateful; SDK for simple loops | CrewAI, AutoGen, LlamaIndex, vendor SDK | Need for explicit control flow and checkpoints |
| Retrieval | pgvector if Postgres exists | Pinecone, Qdrant, Weaviate, Chroma, Milvus | Scale, filtered-search latency, ops appetite |
| Context/data | Warehouse + semantic layer | Knowledge graph, feature store | Freshness, governance, entity resolution |
| Tracing | OpenTelemetry GenAI → backend | LangSmith, Langfuse, Phoenix, Braintrust, Helicone | Lock-in, self-host, data residency |
| Evals | pytest/CI + promptfoo/DeepEval/Ragas | LangSmith evals, Braintrust | CI fit, judge calibration effort |
| Serving | Bought (API) | Self-hosted (vLLM-class), managed endpoints | Volume, residency, cost |
| Guardrails | HITL approvals + permission gating | Policy engines, classifier filters | Risk tolerance, regulatory context |
| Agent packaging | Skills + MCP | Custom plugins, CLI | Stability of procedure vs live data need |

### Inferences
- The "framework wars" are less consequential than they appear: the durable decisions are trace format (OTel), eval ownership, and context governance. Frameworks are replaceable; instrumentation and eval datasets are not.
- pgvector's rise means retrieval is becoming a database feature rather than a product category, which lowers the barrier for small teams and increases pressure on dedicated vendors to differentiate on filtered-search latency and scale.
- Buying inference and building prompt/context management is a rational division: inference is commoditizing, while org-specific context is the actual moat.
- Python dominance is structural (ML ecosystem, data tooling) and unlikely to shift; TypeScript's role is product surfaces and edge runtimes, not the core AI service.
- Observability consolidation (ClickHouse/Langfuse, Dynatrace/Arize) suggests tracing is becoming a feature of data platforms, which may reduce vendor lock-in but also reduce standalone tool choice.

### Gaps
- No public market-share data for agent frameworks in production; survey percentages are unavailable or vendor-reported.
- Self-hosted serving stack specifics (vLLM, TGI, TensorRT-LLM) are not well covered by the 2026 surveys I found; LangChain only reports that ~1/3 self-host models.
- Pricing and total cost of ownership comparisons between vector DBs are vendor-supplied and not normalized by workload.

---

## Cross-cutting synthesis: what the evidence supports

1. **The job is production ownership, not model building.** Across JDs, surveys, and role definitions, the center of gravity is reliable behavior in production. Training is a minority activity. — [Alexey On Data](https://alexeyondata.substack.com/p/what-1000-job-descriptions-reveal); [SiBlog](https://sinimite.work/en/posts/ai-engineer-job-market-2026/)
2. **Quality is the binding constraint, and verification is the weakest link.** Quality is the #1 barrier; evals lag observability badly; MAST shows verification failures are a distinct, costly category. — [LangChain](https://www.langchain.com/state-of-agent-engineering); [MAST](https://arxiv.org/abs/2503.13657)
3. **Context is infrastructure.** Stale/fragmented context causes confident wrong answers that reach customers; governance is named the biggest barrier to maturity. — [VentureBeat](https://venturebeat.com/vb-pulse-agentic-context-layers-report); [Redis](https://redis.io/resources/state-of-context-engineering-2026/)
4. **Agents amplify existing organizational strength or dysfunction.** DORA's amplifier finding is the best-supported organizational claim in the corpus. — [DORA 2025](https://dora.dev/research/2025/dora-report/)
5. **Most organizations are still pre-scale.** McKinsey: ~1/3 scaling, 39% any EBIT impact, ~6% high performers. LangChain's 57% "in production" is a narrower, self-selected population and should not be read as enterprise-wide maturity. — [McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025); [LangChain](https://www.langchain.com/state-of-agent-engineering)
6. **Skills are a real but narrow lever.** Strong evidence for procedural consistency and replication in platform-like settings; weak evidence for general quality gains; clear failure modes around triggering, staleness, and auth. — [OpenAI](https://openai.com/index/forward-deployed-engineering-means); [LlamaIndex](https://www.llamaindex.ai/blog/skills-vs-mcp-tools-for-agents-when-to-use-what); [Aerospike](https://aerospike.com/blog/agent-skills-guide/)
7. **Human accountability is not being delegated.** Deployment/monitoring and planning remain human-owned by large margins; HITL is still the top guardrail. — [Stack Overflow](https://survey.stackoverflow.co/2025/ai); [Notion](https://www.notion.com/lp/ai-engineering-survey)

## Source-quality notes and open gaps

- **Survey self-selection.** LangChain (1,340), Stack Overflow (~49,000), DORA (~5,000), McKinsey (1,993), Notion/Amplify/Vercel (1,053), DataHub (250), and Redis all use self-selected or panel samples. Technology-industry overrepresentation is explicit in LangChain's methodology (63% technology).
- **Vendor sponsorship.** Redis, DataHub/BARC, VentureBeat Pulse, and various observability vendors sponsor the research whose conclusions favor their categories. Numbers are reported here but flagged.
- **Date ambiguity.** The LangChain report page is dated 12 Jun 2026 but the survey was fielded 18 Nov–2 Dec 2025 and first published in Dec 2025. Cite the fielding window when precision matters.
- **Stack Overflow internal inconsistency.** The 2025 survey page and the Dec 2025 blog swap the 66%/45% figures for "almost right" and "debugging takes longer." The Jul 2025 press release supports 66% for "almost right." This should be noted in any downstream report.
- **Missing 2026 Stack Overflow data.** Our World in Data references a 2026 Stack Overflow question wording change, but I did not retrieve the 2026 survey results. Treat 2025 as the latest verified Stack Overflow data here.
- **Thin ML/MLOps survey coverage.** Most 2026 surveys are agent-centric. Classic ML engineering evidence comes from older peer-reviewed fieldwork (2015–2025) and a 2026 notebook-operationalization study; there is no equivalent 2026 "state of MLOps" with a large sample in this corpus.
- **No time-allocation study.** I found no time-diary or observational study of AI engineers' daily work in 2026. Any "X% of time on data/prompting/evals" claim should be treated as anecdote.
- **Skills ROI is not measured.** The strongest positive evidence is a single vendor case study (OpenAI FDE); the strongest negative evidence is a single vendor experiment (LlamaIndex). Neither is a controlled trial.
