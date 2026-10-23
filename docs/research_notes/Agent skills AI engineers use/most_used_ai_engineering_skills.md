# Agent Skills Workflows Used by AI Engineers

*Scope: Agent Skills (SKILL.md-style packages) used by engineers building LLM applications, ML/MLOps systems, and AI platform/infrastructure. Current as of 2026-10-23. Star/install figures are point-in-time snapshots and are labeled with confidence. Generic "AI industry trend" data is used only where it directly measures delegated engineering work.*

*Method note: All GitHub star counts below were cross-checked against the GitHub REST API on 2026-10-23 where possible. Install counts come from skills.sh telemetry as aggregated by Linkly AI (updated 2026-10-23). Two structural caveats run through this document: (1) stars measure attention, not use; (2) skills.sh installs are counted from `npx skills add` telemetry, a channel Vercel operates and promotes, so Vercel-published skills are structurally over-represented.*

---

## 1. What tasks do AI engineers delegate to coding agents and skills most often?

### Takeaway
Delegation is concentrated in the *inner loop* of software work — generate code in familiar territory, debug/refactor, write tests, explain an unfamiliar codebase, and draft documentation. Production operations, security remediation, and data/metrics analysis are delegated far less, even though they are where engineers report the most pain. Skills usage mirrors this: the most-installed skills are planning/interrogation, codebase understanding, TDD, debugging, and review — not deployment or evals.

### Cited Findings
- **69.3%** of developers currently use AI/agents to generate code in a familiar area; **63.8%** for debugging/troubleshooting/refactoring; **58.1%** for writing tests; **59.4%** for straightforward technical questions; **51.1%** for documentation; **49.7%** for onboarding to a new codebase; **49.7%** for internal knowledge search — [Stack Overflow Developer Survey 2026, AI data](https://survey.stackoverflow.co/2026/ai/data) (published 2026-10-06; n=17,464 overall, n=12,547 for this question).
- Much lower: **41.9%** for analyzing data/logs/metrics; **40.5%** for code/PR/design review; **34.6%** for finding or fixing security issues; **28.1%** for creating/configuring dev and test environments; **19.9%** for deploying/operating/troubleshooting production systems — [Stack Overflow 2026](https://survey.stackoverflow.co/2026/ai/data).
- Perceived usefulness is highest for implementation (**75%** useful/very useful), debugging/refactoring (**73%**), documentation (**66%**), and review (**64%**); communication is the outlier at **35%** useful — [Stack Overflow 2026](https://survey.stackoverflow.co/2026/ai/data).
- Trust is conditional: **48%** trust AI output only "when I can easily verify it"; just **7%** trust it for important work decisions; **76.5%** run generated code locally before using it and **53%** inspect tests/security implications — [Stack Overflow 2026](https://survey.stackoverflow.co/2026/ai/data). This is a direct argument for skills that produce *verifiable artifacts* (tests, diffs, traces) rather than prose.
- **66%** use AI coding assistants/agents and **26.2%** use AI agents or automated workflows; **73%** of coding-assistant users use them daily — [Stack Overflow 2026](https://survey.stackoverflow.co/2026/ai/data). Claude Code (65.5%), GitHub Copilot (58.7%), OpenAI Codex (29.5%), Cursor (25.5%) lead the agent tools — [same](https://survey.stackoverflow.co/2026/ai/data).
- In LangChain's survey, the write-in answer to "what agents do you use most day-to-day" was dominated by coding assistants (Claude Code, Cursor, Copilot, Amazon Q, Windsurf, Antigravity) "for code generation, debugging, test creation, or navigating large codebases"; research/deep-research agents were second — [LangChain, State of Agent Engineering](https://www.langchain.com/state-of-agent-engineering) (published 2026-06-12; fielded 2025-11-18 to 2025-12-02; n=1,340).
- Where AI has most impact on the pipeline: dev/IDE **57%**, planning/spec writing **48%**, app UI **40%**, CI/CD **32%**, backend/API **28%**, infra **18%** — [Notion × Amplify × Vercel 2026 AI Engineering Survey](https://www.notion.com/lp/ai-engineering-survey) (n=1,053; fielded 2026-05-16 to 2026-06-15).
- Technique mix for changing model behavior: prompting **80%**, tool-use tuning **59%**, RAG/retrieval **49%**, fine-tuning **26%**, RL **22%** — [Notion/Amplify/Vercel 2026](https://www.notion.com/lp/ai-engineering-survey). Fine-tuning remains niche, consistent with LangChain's finding that **57%** are not fine-tuning and rely on prompting + RAG — [LangChain 2026](https://www.langchain.com/state-of-agent-engineering).

### Inferences
- The "delegation frontier" sits exactly where output can be checked cheaply: a diff, a failing test, a stack trace, a doc. Tasks whose output is expensive to verify (prod change, security fix, data interpretation) lag by 20–40 percentage points.
- Because 73% of coding-agent users are daily users, skill value is dominated by *repeat frequency*, not task prestige. A skill used 5×/day on small edits beats a skill used once a quarter on architecture.
- Skills that shorten the verification loop (generate tests first, emit a trace, produce a reviewable plan) should outperform skills that only add instructions.

### Gaps
- No public survey isolates "tasks delegated *specifically through Agent Skills*" from "tasks delegated to coding agents generally." All percentages above are agent-level, not skill-level.
- No vendor publishes per-skill invocation counts (only install counts), so actual usage of installed skills is unmeasured.

---

## 2. Which skill categories appear most frequently in popular repositories and marketplaces?

### Takeaway
The catalogs are overwhelmingly about *general software engineering and content production*. Development/coding is the largest curated category; design/frontend, documents, and business automation follow. AI-engineering-specific categories (RAG, evals, agent orchestration, model serving, LLMOps) are a thin slice of both repository counts and install charts.

### Cited Findings
- The most-starred skill repositories are workflow/methodology packs, not domain tools (GitHub API, 2026-10-23): `obra/superpowers` **303,996 stars / 27,074 forks** (created 2025-10-09) — [GitHub API](https://api.github.com/repos/obra/superpowers); `mattpocock/skills` **300,891**; `multica-ai/andrej-karpathy-skills` **222,535**; `anthropics/skills` **183,034**; `DietrichGebert/ponytail` **173,455**; `nextlevelbuilder/ui-ux-pro-max-skill` **139,015**; `addyosmani/agent-skills` **109,656**; `ComposioHQ/awesome-claude-skills` **77,695** — [Linkly AI, Top Agent Skill Repositories](https://linkly.ai/skills/top-repos) (updated 2026-10-23), cross-checked against the GitHub API.
- Comparative scale, as reported by reviewers: superpowers at ~304k stars is ahead of Vue and "way ahead of Next.js," and a community single-file behavioral skill (`andrej-karpathy-skills`) reached ~222k stars with **1** skill in the repo — [Linkly top-repos](https://linkly.ai/skills/top-repos); [Firecrawl, "Best Trending GitHub Repositories… 2026"](https://www.firecrawl.dev/blog/best-github-repos) (published 2026-05-26); [dev.to/AWS](https://dev.to/aws/the-most-popular-ai-coding-skills-right-now-4183) (2026-06-15).
- Curated category composition in one 100-skill guide: Development & Coding **15**, Content & Writing **9**, Business & Marketing **9**, Productivity **9**, Design & Frontend **8**, Data & Analytics **8**, Security & Compliance **8**, Communication **8**, DevOps & Infrastructure **8**, Creative & Media **8**, Document Processing **7**, Enterprise-specific **3** — [AGNT, "100 Best AI Agent Skills in 2026"](https://agnt.gg/articles/agents/100-best-ai-agent-skills) (2026-04-16). It describes Development & Coding as "the largest and most mature category."
- Anthropic's own reference repo is organized as Creative & Design, Development & Technical, Enterprise & Communication, and Document Skills, with production document skills (docx/pdf/pptx/xlsx) shipped as source-available references — [anthropics/skills README](https://github.com/anthropics/skills).
- Catalog scale is enormous and fragmented: SkillsMP **700k+**, SkillNet **300k+**, Skills.sh **90k+**, SkillHub **80k+**, ClawHub **40k+** skills — [arXiv 2605.07358, "A Comprehensive Survey on Agent Skills"](https://arxiv.org/html/2605.07358v1) (2026-05-08). A separate marketplace claims "3M+" indexed skills — [SkillsMP](https://skillsmp.com/). These numbers are counts of scraped packages, not distinct maintained skills, and should not be read as adoption.
- Of the 100 most-installed skills.sh entries, **14** are from a single author's composable set (`mattpocock/skills`: grill-me, grill-with-docs, improve-codebase-architecture, tdd, setup, handoff, triage, prototype, grilling, domain-modeling, teach, codebase-design, diagnosing-bugs, code-review) — counted from [Linkly, Most Installed](https://linkly.ai/skills/most-installed) (2026-10-23). Another **5** are one video-generation vendor suite (heygen/hyperframes) and **~20** are a single SaaS connector suite (Lark/Feishu). This is vendor-bundle concentration, not a broad long tail of engineering capability.
- skills.sh's own ranking is derived from anonymous telemetry of `npx skills add <owner/repo>`, and Vercel's skills ranked at the top partly because the CLI launched alongside `react-best-practices` — [Hacker News thread, "Show HN: Agent Skills Leaderboard"](https://news.ycombinator.com/item?id=46697908) (c. January 2026). Commenters called the ranking "opaque" and noted the Vercel affiliation is only visible in the corner.

### Inferences
- Star counts are a *media* signal: one-file behavioral manifestos and viral personal workflows out-star maintained multi-skill libraries by 2–3×. Do not use stars to infer engineering adoption.
- Install charts are dominated by four things: a discovery meta-skill, one prolific author's composable workflow set, vendor connector suites, and media generation. Depth-oriented AI-engineering skills are almost absent from the visible top 100.
- Category counts in marketplaces are inflated by scraping and duplication; the *curated* view (AGNT, Anthropic, Composio) is a better proxy for what people actually browse.

### Gaps
- No marketplace publishes a category histogram over installs (only over listings). The "AI-engineering share of installs" cannot be computed from public data.
- SkillHub CN counts (top entries 4.9M–7.6M) are an order of magnitude larger than skills.sh and are not comparable; cross-registry normalization does not exist.

---

## 3. Which concrete workflows recur?

### Takeaway
Nine workflow clusters recur across repositories, install charts, and practitioner writeups. Six are well represented (onboarding, implementation, TDD, debugging, review, refactoring). Three are repeatedly named as needs but thinly represented as skills (RAG/retrieval, evaluation, deployment/observability/incident).

### Cited Findings

| Workflow | Evidence it recurs | Representative skills / artifacts |
|---|---|---|
| **Codebase onboarding & architecture understanding** | 49.7% of developers use AI for onboarding; `improve-codebase-architecture` 1.16M installs; `Understand-Anything` 87.7k stars; `domain-modeling` 869k; `codebase-design` 844k — [SO 2026](https://survey.stackoverflow.co/2026/ai/data); [Linkly Most Installed](https://linkly.ai/skills/most-installed) | `improve-codebase-architecture`, `codebase-design`, `domain-modeling`, `/understand`-style graph skills |
| **Spec / planning / requirements interrogation** | `grill-me` 1.42M, `grill-with-docs` 1.21M, `grilling` 972k, `prototype` 981k installs; Superpowers opens with a brainstorming/spec phase — [Linkly](https://linkly.ai/skills/most-installed); [dev.to/AWS](https://dev.to/aws/the-most-popular-ai-coding-skills-right-now-4183) (2026-06-15) | `grill-me`, `brainstorming`, `writing-plans`, `/spec`+`/plan` |
| **Implementation / TDD** | 69.3% generate code, 58.1% write tests; `tdd` 1.13M installs; Superpowers and Addy Osmani both enforce red-green-refactor — [SO 2026](https://survey.stackoverflow.co/2026/ai/data); [Linkly](https://linkly.ai/skills/most-installed); [Firecrawl](https://www.firecrawl.dev/blog/best-github-repos) | `tdd`, `test-driven-development`, `/build`, `/test` |
| **Debugging / root cause** | 63.8% debug/refactor; 73% call AI useful here; `diagnosing-bugs` 829k, `triage` 984k installs; systematic-debugging is a top-10 skill in AGNT's guide — [SO 2026](https://survey.stackoverflow.co/2026/ai/data); [Linkly](https://linkly.ai/skills/most-installed); [AGNT](https://agnt.gg/articles/agents/100-best-ai-agent-skills) | `diagnosing-bugs`, `systematic-debugging`, `root-cause-tracing`, `/triage` |
| **Code review & simplification** | 40.5% use AI for review, 64% find it useful; `code-review` 783k installs; `/simplify` described as "the most widely installed code quality tool" — [SO 2026](https://survey.stackoverflow.co/2026/ai/data); [Linkly](https://linkly.ai/skills/most-installed); [AGNT](https://agnt.gg/articles/agents/100-best-ai-agent-skills) | `code-review`, `simplify`, five-axis review, `/review` |
| **Refactoring / tech-debt rescue** | Collapsed into the debugging/refactoring 63.8% bucket; `improve-codebase-architecture` is a top-12 install — [SO 2026](https://survey.stackoverflow.co/2026/ai/data); [Linkly](https://linkly.ai/skills/most-installed) | architecture-improvement and code-simplification skills |
| **Documentation & artifacts** | 51.1% use AI for docs, 66% useful; document skills (docx/pdf/pptx/xlsx) are the most-downloaded Anthropic skills (22k–35k each per AGNT) — [SO 2026](https://survey.stackoverflow.co/2026/ai/data); [AGNT](https://agnt.gg/articles/agents/100-best-ai-agent-skills) | `docx`, `pdf`, `pptx`, `xlsx`, changelog, brand-guidelines |
| **RAG / retrieval** | 49% use RAG to adapt behavior; only scattered RAG skills (e.g. a "rag-observability-evals" skill graded A on a directory) — [Notion/Amplify/Vercel](https://www.notion.com/lp/ai-engineering-survey); [SkillsDirectory](https://www.skillsdirectory.com/skills/sickn33-rag-observability-evals-f52c4e1a) | retrieval-quality, chunking, groundedness eval skills — few and low-install |
| **Evaluation / observability** | 52.4% run offline evals, 37.3% online; 89% have observability; "evaluation" is the #1 stack challenge (20%) — [LangChain 2026](https://www.langchain.com/state-of-agent-engineering); [Notion et al.](https://www.notion.com/lp/ai-engineering-survey). Tooling exists (LangSmith 17.3%, MLflow 15.2%, Langfuse 15.2% usage) but *skill* coverage is thin — [SO 2026](https://survey.stackoverflow.co/2026/ai/data) | LangSmith trace-fetch/debug skill; MLflow/Langfuse skill-eval writeups — [MLflow](https://mlflow.org/blog/evaluating-improving-agent-skills/); [Langfuse](https://langfuse.com/blog/2026-02-26-evaluate-ai-agent-skills) |
| **Agent orchestration** | LangChain 30.2%, OpenAI Agents SDK 23.8%, terminal 18.9%, LangGraph 18.8%; framework adoption doubled 9%→18% of orgs; but 59% of agentic requests are single-service-call monoliths — [SO 2026](https://survey.stackoverflow.co/2026/ai/data); [Datadog](https://www.datadoghq.com/state-of-ai-engineering/) | `mcp-builder`, subagent-driven-development, multi-agent workflow skills |
| **Deployment / infra / incidents** | Only 19.9% use AI for production deploy/operate, and 36% say they don't plan to; infra is the least AI-impacted pipeline stage (18%) — [SO 2026](https://survey.stackoverflow.co/2026/ai/data); [Notion et al.](https://www.notion.com/lp/ai-engineering-survey). Vendor skills exist (AWS Agent Toolkit for deployment/serverless/database, launched May 2026; Cloudflare `security-audit-skill` 39.5k stars) — [dev.to/AWS](https://dev.to/aws/the-most-popular-ai-coding-skills-right-now-4183); [Linkly](https://linkly.ai/skills/top-repos) | AWS toolkit skills, Cloudflare security audit, Terraform/K8s skills |
| **Security** | 34.6% use AI for security work, 38% expect to do more; Trail of Bits ships security skills (7.7k stars) — [SO 2026](https://survey.stackoverflow.co/2026/ai/data); [Linkly](https://linkly.ai/skills/top-repos) | static analysis, threat modeling, pentest, secrets detection |
| **Data pipelines / SQL** | 41.9% analyze data/logs/metrics; skills are mostly consumer-grade NL-to-SQL and CSV summarizers — [SO 2026](https://survey.stackoverflow.co/2026/ai/data); [AGNT](https://agnt.gg/articles/agents/100-best-ai-agent-skills) | `agent-sql`, CSV summarizer, Postgres read-only connectors |

- Practitioner confirmation of the SDLC shape: Superpowers, GStack, GSD Core, Addy Osmani's pack and Matt Pocock's set all map to the same phases (brainstorm → spec → plan → build → test → review → ship), differing only in whether they organize by *phase* or by *role* — [dev.to/AWS, 2026-06-15](https://dev.to/aws/the-most-popular-ai-coding-skills-right-now-4183).
- A commenter on that article describes the emerging best practice as "workflow contracts": explicit inputs, expected artifacts, and a verification step, with discovery/implementation/review skills separated and escalation by scope — [dev.to/AWS comments, 2026-08-23](https://dev.to/aws/the-most-popular-ai-coding-skills-right-now-4183).

### Inferences
- The recurring unit is not "a prompt for X" but a **phase gate with an artifact**: a spec doc, a task list, a failing test, a diff, a review checklist. Skills that produce a durable artifact survive; instruction-only "persona" skills do not.
- Review and debugging are the highest-leverage categories by frequency × usefulness, yet receive less install volume than planning. Planning skills may be over-indexed relative to measured usefulness.
- The RAG/eval/deploy cluster is where task frequency (49%, 52%, 20%) exceeds skill supply by the widest margin.

### Gaps
- No public dataset maps skill invocations to workflow phase. The table's "representative skills" are the visible top of each category, not a complete census.
- Incident response and SLO/on-call skills are essentially absent from ranked catalogs; I found no install data for them, only vendor blog posts.

---

## 4. Which categories are well served, and which are underserved or shallow?

### Takeaway
Greenfield coding, TDD, review, refactoring, codebase explanation, frontend/design, and document generation are mature and competitive. Underserved: evaluation (especially *skill-level* evaluation), retrieval/RAG quality, deployment/rollback, incident response, cost/latency engineering, context/caching optimization, data pipelines, and security *of* skills. Many "skills" in the long tail are shallow — a renamed slash command or a restated API doc.

### Cited Findings
- **Well served:** Development & Coding is described as "the largest and most mature category," with multiple competing full-lifecycle packs (Superpowers, GStack, GSD Core, Addy Osmani, Matt Pocock) — [AGNT](https://agnt.gg/articles/agents/100-best-ai-agent-skills); [dev.to/AWS](https://dev.to/aws/the-most-popular-ai-coding-skills-right-now-4183).
- **Well served:** Design/frontend is the clearest example of a skill beating the model's default. Anthropic's `frontend-design` has ~1.02M skills.sh installs and is described as breaking "distributional convergence" (Inter font, purple gradient) — [Linkly](https://linkly.ai/skills/most-installed); [AGNT](https://agnt.gg/articles/agents/100-best-ai-agent-skills). `ui-ux-pro-max-skill` has 139k stars — [Linkly](https://linkly.ai/skills/top-repos).
- **Well served:** Framework/vendor knowledge is moving into the package itself — Vue, Vite, Nuxt, TanStack Intent, `skilld` generating version-aware skills from installed npm deps, and AWS's Agent Toolkit (May 2026) — [dev.to/AWS](https://dev.to/aws/the-most-popular-ai-coding-skills-right-now-4183). This is a durable pattern because it solves the training-cutoff problem.
- **Shallow:** A top HN comment: "Basically skills are /commands that can have attached scripts, that's about it. If your 'skill' doesn't come with scripts/executables, it's just a fancy slash command." The same commenter reports success only with skills that ship real analysis scripts (PEP723 Python + tree-sitter AST) — [HN, c. Jan 2026](https://news.ycombinator.com/item?id=46697908).
- **Shallow / duplicate-heavy:** 700k–3M indexed "skills" across registries, versus 5,200 community skills cited by one curated guide three months earlier — [arXiv 2605.07358](https://arxiv.org/html/2605.07358v1); [SkillsMP](https://skillsmp.com/); [AGNT](https://agnt.gg/articles/agents/100-best-ai-agent-skills). The gap indicates scraping/duplication, not 100× capability growth.
- **Underserved — evaluation:** LangChain finds 52.4% offline / 37.3% online evals, and Notion/Amplify/Vercel rank "evaluation" as the single biggest stack challenge at **20%**, ahead of orchestration (18%), inference cost (16%), and security (15%) — [LangChain](https://www.langchain.com/state-of-agent-engineering); [Notion et al.](https://www.notion.com/lp/ai-engineering-survey). Yet no eval skill appears in the top 100 installs; eval practice is being built as vendor tooling (MLflow, Langfuse) rather than packaged as skills — [MLflow](https://mlflow.org/blog/evaluating-improving-agent-skills/); [Langfuse](https://langfuse.com/blog/2026-02-26-evaluate-ai-agent-skills).
- **Underserved — retrieval:** 49% use RAG, but RAG appears in install charts only as isolated directory entries, not ranked skills — [Notion et al.](https://www.notion.com/lp/ai-engineering-survey); [Linkly](https://linkly.ai/skills/most-installed).
- **Underserved — production operations:** only 19.9% delegate deploy/operate, and **36%** explicitly do not plan to; infra is the least-affected pipeline stage (18%) — [SO 2026](https://survey.stackoverflow.co/2026/ai/data); [Notion et al.](https://www.notion.com/lp/ai-engineering-survey).
- **Underserved — cost/latency/context engineering:** 69% of input tokens are system prompts and only **28%** of LLM call spans show cached-read tokens; rate-limit errors were **60%** of LLM errors in Feb 2026 and about **one-third** in Mar 2026 (~8.4M errors) — [Datadog, State of AI Engineering 2026](https://www.datadoghq.com/state-of-ai-engineering/). These are concrete, skill-shaped problems with no visible skill category.
- **Underserved — security of the skill supply chain:** Snyk's ToxicSkills research reports **36%** of agent skills contain security flaws and **1,467** vulnerable skills (the public summary does not state the scanned denominator) — [Snyk](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/). By 2026-02-03 researchers counted **341** malicious skills on ClawHub — [prplbx](https://www.prplbx.com/blog/agent-skills-supply-chain) (2026-02-07); another count cites **230+** — [Authmind](https://www.authmind.com/blogs/openclaw-malicious-skills-agentic-ai-supply-chain). Counts conflict; the direction does not. OWASP now maintains an **Agentic Skills Top 10** with case studies including the January 2026 "ClawHavoc" campaign — [OWASP](https://owasp.org/www-project-agentic-skills-top-10/case-studies); peer-reviewed detection work exists — [arXiv 2602.06547](https://arxiv.org/abs/2602.06547).
- **Shallow — auto-invocation:** multiple practitioners report the model ignores installed skills; workarounds are explicit `/skill` invocation, shorter/more opinionated skills, or a `UserPromptSubmit` hook that regex-matches and injects a suggestion. One user cut a 1,900-line CLAUDE.md to 150 lines and moved the content into skills + a steering hook — [HN](https://news.ycombinator.com/item?id=46697908). AWS's own advocate notes "I still need to manually tell my agent to run the skills by using the `/` command" — [dev.to/AWS](https://dev.to/aws/the-most-popular-ai-coding-skills-right-now-4183).

### Inferences
- The mature categories are those where correctness is locally checkable (tests pass, diff compiles, page renders, PDF opens). The underserved categories are those requiring *cross-system state*: eval baselines, retrieval corpora, deploy targets, traces, cost budgets.
- "Well served" does not mean "solved": review and debugging skills still mostly encode checklists, not executable analysis. The differentiated ones ship scripts and parse ASTs/traces.
- Security is simultaneously the fastest-growing *category* and the least trustworthy *channel* — a skill that vets other skills (“skill-vetter”, 279k ClawHub installs) is itself in the top 40, which is a telling market signal — [Linkly](https://linkly.ai/skills/most-installed).

### Gaps
- No independent quality audit of top-installed skills exists; Snyk's 36% figure covers scanned skills broadly, not the top 100.
- No data on how often installed skills are actually invoked vs. left dormant. Anecdotes suggest high dormancy but there is no measurement.

---

## 5. What evidence exists, and how good is it?

### Takeaway
There is strong survey evidence for *what engineers delegate to agents* and strong telemetry for *what gets installed*, but almost no evidence connecting the two. Stars are the weakest signal; installs are better but channel-biased; surveys are the most reliable but measure agents, not skills.

### Cited Findings
- **Surveys (high confidence, agent-level):** Stack Overflow 2026, n=17,464, published 2026-10-06 — [survey](https://survey.stackoverflow.co/2026/ai/data); [announcement](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/). LangChain State of Agent Engineering, n=1,340, published 2026-06-12 — [report](https://www.langchain.com/state-of-agent-engineering). Notion/Amplify/Vercel, n=1,053, fielded May–June 2026 — [report](https://www.notion.com/lp/ai-engineering-survey).
- **Production telemetry (high confidence for behavior, biased sample):** Datadog analyzed LLM telemetry from 1,000+ customers; explicitly caveated as infrastructure-serious, cloud-skewed — [Datadog](https://www.datadoghq.com/state-of-ai-engineering/). Datadog reports agent-framework adoption at ~18% of orgs, so most AI applications still do not use an orchestration framework — [same](https://www.datadoghq.com/state-of-ai-engineering/).
- **Install telemetry (medium confidence):** skills.sh counts anonymous `npx skills add` runs; aggregated to a top-100 by Linkly, updated daily — [Linkly](https://linkly.ai/skills/most-installed); [Linkly dataset](https://github.com/LinklyAI/best-skills). HN criticism: the metric is "their own tools download count," and the operator's own skills benefit — [HN](https://news.ycombinator.com/item?id=46697908).
- **Stars/forks (low confidence for usage, high for attention):** GitHub API snapshots are exact but measure interest; e.g. superpowers 303,996 stars / 27,074 forks / 352 open issues on 2026-10-23 — [GitHub API](https://api.github.com/repos/obra/superpowers).
- **Job posts (medium confidence, ML/MLOps only):** 1,959 US MLOps postings since January 2026 (~70/week); median $185k; Python, cloud platforms and MLOps tooling each appear in **more than two-thirds** of postings, with observability and CI/CD close behind; 69% mid/senior IC; 34% at 10,000+ employee companies — [Axial Search, MLOps job market 2026](https://axialsearch.com/insights/mlops-jobs) (updated 2026-09-22).
- **Practitioner writeups (medium confidence, qualitative):** AWS developer advocate tour of the top skill packs — [dev.to/AWS, 2026-06-15](https://dev.to/aws/the-most-popular-ai-coding-skills-right-now-4183); Firecrawl's repo review with explicit "honest take"/"cons" sections — [Firecrawl, 2026-05-26](https://www.firecrawl.dev/blog/best-github-repos); HN thread with 44 comments of unvarnished failure reports — [HN](https://news.ycombinator.com/item?id=46697908).
- **Security research (medium-high confidence):** Snyk ToxicSkills — [Snyk](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/); Palo Alto Unit 42 on evasive malicious skills bypassing scanners — [Unit 42](https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/); OWASP case studies — [OWASP](https://owasp.org/www-project-agentic-skills-top-10/case-studies).
- **Academic (medium confidence, taxonomy not adoption):** the May 2026 survey organizes the field by representation, acquisition, retrieval, evolution, and names quality control, interoperability, safe updating and long-term capability management as open challenges — [arXiv 2605.07358](https://arxiv.org/html/2605.07358v1). It cites registry scales but no usage data.
- **DORA:** the 2025 report found 90% of technology professionals use AI at work — [DORA](https://dora.dev/insights/balancing-ai-tensions/). DORA reportedly paused its annual survey and will not publish a 2026 State of AI-assisted Software Development report — [Waydev](https://waydev.co/dora-pauses-the-annual-survey/) (secondary source; low confidence).

### Inferences
- Triangulation works best as *rank correlation*, not absolute numbers: the same 6–8 workflow categories appear at the top of surveys, install charts, and curated guides. That convergence is the strongest finding in this research.
- Any claim of the form "X% of AI engineers use skill Y" is unsupported by public data. The defensible claim is "skill Y is in the top-N installs and addresses a task that N% of developers delegate to agents."

### Gaps
- **No survey asks about Agent Skills specifically.** Every percentage in this document is about AI tools/agents generally.
- **No role-segmented skill data.** Neither Stack Overflow nor LangChain nor Notion breaks skill/task usage down by "LLM application engineer" vs "ML/MLOps" vs "platform/infra."
- **No vendor reports from Anthropic/OpenAI/Google on skill usage.** Their public material is announcement/education, not measurement.
- **DORA 2026 absence** removes the usual annual baseline for AI-assisted delivery performance.
- Install counts are not de-duplicated by user or machine and can be inflated by CI and tutorials.

---

## 6. How does usage differ between LLM application engineers, ML/MLOps engineers, and platform/infra engineers?

### Takeaway
The three segments delegate different *objects*: LLM app engineers delegate prompts, retrieval, evals and agent logic; ML/MLOps engineers delegate pipelines, deployment and monitoring but mostly through conventional infra tooling; platform/infra engineers delegate configuration, security and incident work least of all. The skill ecosystem serves the first segment's *coding* needs well and its *runtime* needs poorly, and serves the other two mostly through generic coding skills plus vendor toolkits.

### Cited Findings
- **LLM application engineers** report evaluation as the #1 stack challenge (20%), ahead of orchestration (18%), inference cost (16%), security/guardrails (15%), model quality (10%), context/retrieval (9%), observability (8%) — [Notion/Amplify/Vercel 2026](https://www.notion.com/lp/ai-engineering-survey). 49% use RAG, 80% still adapt behavior by prompting, 59% by tool-use tuning — [same](https://www.notion.com/lp/ai-engineering-survey).
- **LLM application engineers** are the group most likely to have observability: 89% overall, 94% among those in production, 71.5% with full tracing; but only 52.4% run offline evals and 37.3% online — [LangChain 2026](https://www.langchain.com/state-of-agent-engineering). The observability/eval gap is the segment's defining asymmetry.
- **LLM application engineers** work in multi-model fleets: 81% use multiple models, 44% route by task, 26% compare outputs — [Notion et al.](https://www.notion.com/lp/ai-engineering-survey); 70%+ of Datadog orgs use 3+ models — [Datadog](https://www.datadoghq.com/state-of-ai-engineering/). Skills for model routing, fallback and cost-tiering are correspondingly valuable and largely absent from install charts.
- **Agent builders** are still mostly monolithic: 59% of agentic requests make a single service call, only 18% make 3+ — [Datadog](https://www.datadoghq.com/state-of-ai-engineering/). This undercuts the market for elaborate multi-agent orchestration skills relative to their visibility.
- **ML/MLOps engineers** are hired for deployment and monitoring, not model invention: Python, cloud platforms and MLOps tooling each appear in >2/3 of postings; observability and CI/CD follow; 69% of roles are mid/senior IC; median $185k; ~70 US postings/week — [Axial Search](https://axialsearch.com/insights/mlops-jobs) (2026-09-22).
- **ML/MLOps engineers** mostly do not fine-tune: 57% of organizations are not fine-tuning, relying on base models + prompting + RAG — [LangChain 2026](https://www.langchain.com/state-of-agent-engineering). Fine-tuning skills are therefore a niche, not a core category.
- **ML tooling shows up as observability, not as skills:** MLflow (15.2%) and Weights & Biases (10.7%) are used for agent observability/eval, behind Sentry (26%) and LangSmith (17.3%) — [SO 2026](https://survey.stackoverflow.co/2026/ai/data). MLflow and Langfuse have published *how to evaluate a skill*, but not packaged eval skills that rank — [MLflow](https://mlflow.org/blog/evaluating-improving-agent-skills/); [Langfuse](https://langfuse.com/blog/2026-02-26-evaluate-ai-agent-skills).
- **Platform/infra engineers** are the least likely to delegate production work: 19.9% use AI for deploy/operate/troubleshoot, 36% do not plan to, and 22% say it is not part of their workflow; infra is the least AI-impacted pipeline stage (18%) — [SO 2026](https://survey.stackoverflow.co/2026/ai/data); [Notion et al.](https://www.notion.com/lp/ai-engineering-survey).
- **Platform/infra** demand is met by vendor-distributed skills rather than community packs: AWS Agent Toolkit for AWS (deployment, serverless, database; announced May 2026) — [dev.to/AWS](https://dev.to/aws/the-most-popular-ai-coding-skills-right-now-4183); Cloudflare `security-audit-skill` at 39.5k stars, one of the fastest-rising repos in the top 100 (+3,098 in a day) — [Linkly](https://linkly.ai/skills/top-repos).
- **Platform/infra** failures are capacity failures: rate-limit errors were 60% of LLM call errors in Feb 2026 and about one-third in Mar 2026 (~8.4M errors); 69% of input tokens are system prompts; only 28% of calls use prompt caching — [Datadog](https://www.datadoghq.com/state-of-ai-engineering/). These are platform-team problems with no mature skill category.
- **Role composition of the AI engineering population:** in one 1,053-person survey, 23% founders/CTOs, 19% AI engineers, 12% full-stack, 9% eng managers/tech leads, 9% PMs; 51% of respondents with 10+ years of software experience have ≤3 years of AI experience — [Notion et al.](https://www.notion.com/lp/ai-engineering-survey). The audience is senior in software, junior in AI — which favors skills that encode *engineering discipline* over skills that explain ML theory.

### Inferences
- The segment with the most skill supply (LLM app engineers doing code) is not the segment with the most unmet need (LLM app engineers doing evals/runtime; MLOps doing monitoring; platform doing capacity).
- MLOps and platform engineers are unlikely to adopt community skill packs wholesale; they adopt vendor-maintained, versioned skills that ship with the tool they already run (AWS, Cloudflare, Terraform, K8s). Trust and provenance dominate.
- Because 59% of agents are monolithic and only 18% of orgs use agent frameworks, "multi-agent orchestration" skills are ahead of the actual architecture base.

### Gaps
- No dataset segments skill installs by job title. The segment analysis above is inferred by mapping each segment's measured task mix onto the skill catalog's composition; it is not directly observed.
- AI platform/infrastructure as a distinct job family has no equivalent of the Axial MLOps posting analysis in the sources found.

---

## 7. What is overhyped or low-value despite being popular?

### Takeaway
Four things are over-indexed: single-file behavioral manifestos, all-in-one SDLC frameworks, raw skill counts, and design/media skills that dominate charts without being AI-engineering work. The common failure is mistaking *distribution* for *effect*, and *instructions* for *capability*.

### Cited Findings
- **Single-file behavioral skills.** `andrej-karpathy-skills` reached ~222k stars with one file and its last push was 2026-04-20 — [Linkly](https://linkly.ai/skills/top-repos). The AWS advocate's verdict: "I'm not sure if this is worth it in my own testing" — [dev.to/AWS](https://dev.to/aws/the-most-popular-ai-coding-skills-right-now-4183). Firecrawl calls the star count "virality as much as adoption" — [Firecrawl](https://www.firecrawl.dev/blog/best-github-repos).
- **All-in-one SDLC frameworks.** Superpowers "can eat up a lot of tokens"; GSD Core "burned through tokens fast" and "takes over your whole workflow"; Matt Pocock's opposing view is that owning the entire process "takes away your control and makes bugs in that process hard to fix" — [dev.to/AWS](https://dev.to/aws/the-most-popular-ai-coding-skills-right-now-4183).
- **Skill-count inflation.** Registries advertise 700k–3M skills while a curated guide counted 5,200 community skills in April 2026 — [arXiv 2605.07358](https://arxiv.org/html/2605.07358v1); [SkillsMP](https://skillsmp.com/); [AGNT](https://agnt.gg/articles/agents/100-best-ai-agent-skills). HN: "Skills certainly got a wildwest pre-VCS copy-paste feeling" — [HN](https://news.ycombinator.com/item?id=46697908).
- **Auto-discovery that doesn't fire.** "I'm having issues with the LLMs ignoring the skills content"; "my skills are never called"; "the most reliable way is to inject them into the user prompt at a fresh session" — [HN](https://news.ycombinator.com/item?id=46697908). Overlapping skill descriptions are suspected to confuse selection — [same](https://news.ycombinator.com/item?id=46697908).
- **Install-chart composition is not AI engineering.** Top-100 installs include video generation (hyperframes, 5 entries), Reddit/Twitter automation, digital-avatar video, Chinese legal/ parenting/anti-fraud skills, and ~20 Lark connector skills — [Linkly](https://linkly.ai/skills/most-installed). The single most-installed skill is `find-skills` at **3,996,428** installs — a skill whose job is to find other skills — [Linkly](https://linkly.ai/skills/most-installed).
- **"Skills replace RAG/MCP" framing.** HN commenters note that many skills just restate `tool --help`, and ask why not let the agent run `--help` — [HN](https://news.ycombinator.com/item?id=46697908). The arXiv survey's framing is more accurate: skills solve a *procedural* gap, MCP solves an *interoperability* gap; they are complementary — [arXiv 2605.07358](https://arxiv.org/html/2605.07358v1).
- **Marketplace rankings as quality signal.** skills.sh ranks by install telemetry from a CLI operated by one of the ranked publishers; HN users called this out as bias and "opaque" — [HN](https://news.ycombinator.com/item?id=46697908). Stars have the same problem at larger scale.

### Inferences
- The lowest-value-per-byte category is the "persona/principle" skill: high stars, no executable artifact, unverifiable effect, and it competes for context with everything else.
- The highest-value-per-byte category is a small skill with a script and a verification step (AST analysis, trace fetch, test runner, schema diff). HN's one concrete success story is exactly this — [HN](https://news.ycombinator.com/item?id=46697908).
- "Popular" in this ecosystem is a mixture of genuine utility, launch-channel advantage, and meme dynamics. Any ranking used for decisions should be recomputed after excluding vendor self-published and media-generation skills.

### Gaps
- No A/B or benchmark evidence that any top-installed behavioral skill improves outcomes. The only quantitative skill-evaluation work found is academic/prototype (task generation for skill utility) — [arXiv 2606.17819](https://arxiv.org/html/2606.17819v1) — not applied to popular packs.
- No churn/abandonment data for installed skills.

---

## 8. Ranked shortlist

Ranking logic: (a) install or star signal after removing vendor/media noise, (b) measured task frequency among developers, (c) recurrence across independent catalogs, (d) whether the skill produces a verifiable artifact. Confidence reflects agreement across sources, not the size of any single number.

| # | Category | Why it ranks here | Key evidence | Confidence |
|---|---|---|---|---|
| 1 | **Planning / spec / requirements interrogation** | Highest install volume of any genuine workflow cluster; precedes every major SDLC pack | grill-me 1.42M, grill-with-docs 1.21M, grilling 972k, prototype 981k installs; Superpowers opens with brainstorming/spec — [Linkly](https://linkly.ai/skills/most-installed); [dev.to/AWS](https://dev.to/aws/the-most-popular-ai-coding-skills-right-now-4183) | High |
| 2 | **Codebase onboarding & architecture understanding** | Matches the 49.7% onboarding task; multiple 800k+ skills; clear artifact (map/domain model) | improve-codebase-architecture 1.16M, domain-modeling 870k, codebase-design 844k; Understand-Anything 87.7k stars — [Linkly](https://linkly.ai/skills/most-installed); [SO 2026](https://survey.stackoverflow.co/2026/ai/data) | High |
| 3 | **TDD / test generation** | Second-highest task frequency (58%) and the canonical red-green-refactor gate | tdd 1.13M installs; 58.1% write tests with AI; `/test` in Addy Osmani pack — [Linkly](https://linkly.ai/skills/most-installed); [SO 2026](https://survey.stackoverflow.co/2026/ai/data); [Firecrawl](https://www.firecrawl.dev/blog/best-github-repos) | High |
| 4 | **Debugging / root cause / triage** | Highest usefulness rating after implementation; strong install signals | 63.8% debug/refactor, 73% useful; diagnosing-bugs 829k, triage 984k — [SO 2026](https://survey.stackoverflow.co/2026/ai/data); [Linkly](https://linkly.ai/skills/most-installed) | High |
| 5 | **Code review & simplification** | 40.5% use AI for review; review burden is a named negative effect of AI coding (28%) | code-review 783k installs; 64% useful; review burden 28% — [Linkly](https://linkly.ai/skills/most-installed); [SO 2026](https://survey.stackoverflow.co/2026/ai/data); [Notion et al.](https://www.notion.com/lp/ai-engineering-survey) | High |
| 6 | **Full-lifecycle SDLC orchestration** | Enormous attention (304k stars) but heavy token cost and contested control trade-off | superpowers 303,996 stars / 27,074 forks; GStack ~110k; GSD Core; "can eat up a lot of tokens" — [GitHub API](https://api.github.com/repos/obra/superpowers); [dev.to/AWS](https://dev.to/aws/the-most-popular-ai-coding-skills-right-now-4183) | Medium-high (attention) / Low (efficacy) |
| 7 | **Frontend & visual design** | The clearest case of a skill beating model defaults; 1M+ installs | frontend-design 1,020,556 installs; ui-ux-pro-max 139k stars; "breaks distributional convergence" — [Linkly](https://linkly.ai/skills/most-installed); [AGNT](https://agnt.gg/articles/agents/100-best-ai-agent-skills) | High |
| 8 | **Framework / vendor API knowledge** | Solves training cutoff; distribution is shifting into packages themselves | vercel-react-best-practices 830k installs; AWS Agent Toolkit (May 2026); TanStack Intent, `skilld` — [Linkly](https://linkly.ai/skills/most-installed); [dev.to/AWS](https://dev.to/aws/the-most-popular-ai-coding-skills-right-now-4183) | High |
| 9 | **Document & artifact production** | High task frequency (51% docs) and very high per-skill downloads; enterprise-relevant | docx/pdf/pptx/xlsx 22k–35k downloads each; 66% find AI useful for docs — [AGNT](https://agnt.gg/articles/agents/100-best-ai-agent-skills); [SO 2026](https://survey.stackoverflow.co/2026/ai/data) | High |
| 10 | **Agent/Skill meta-tooling (mcp-builder, skill-creator, find-skills)** | Necessary plumbing; find-skills is literally #1 by installs | find-skills 3,996,428; mcp-builder 25k+ installs; skill-creator 370k SkillHub — [Linkly](https://linkly.ai/skills/most-installed); [AGNT](https://agnt.gg/articles/agents/100-best-ai-agent-skills) | High volume / Medium value |
| 11 | **Evals & observability** | Biggest measured pain (20% evaluation; 52% evals) with almost no ranked skills | evaluation #1 challenge; 52.4% offline evals; LangSmith 17.3%, MLflow 15.2% — [Notion et al.](https://www.notion.com/lp/ai-engineering-survey); [LangChain](https://www.langchain.com/state-of-agent-engineering); [SO 2026](https://survey.stackoverflow.co/2026/ai/data) | High need / Low supply |
| 12 | **RAG & retrieval quality** | 49% use RAG; skills are scattered and low-install | 49% RAG adoption; no RAG skill in top 100 installs — [Notion et al.](https://www.notion.com/lp/ai-engineering-survey); [Linkly](https://linkly.ai/skills/most-installed) | Medium |
| 13 | **Deployment, infra, incident response** | Real need but low delegation (19.9%) and low trust; vendor-led | 19.9% deploy/operate, 36% no plans; AWS toolkit; Cloudflare audit 39.5k stars — [SO 2026](https://survey.stackoverflow.co/2026/ai/data); [Linkly](https://linkly.ai/skills/top-repos) | Medium |
| 14 | **Security engineering** | Growing fast from a low base; supply-chain risk is now the category's own problem | 34.6% use AI for security; Trail of Bits 7.7k stars; 36% of skills flawed — [SO 2026](https://survey.stackoverflow.co/2026/ai/data); [Snyk](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/) | Medium-high |
| 15 | **Data pipelines / analytics engineering** | Steady demand (41.9% analyze data) but skills are consumer-grade | 41.9% data/logs/metrics; NL-to-SQL and CSV skills dominate — [SO 2026](https://survey.stackoverflow.co/2026/ai/data); [AGNT](https://agnt.gg/articles/agents/100-best-ai-agent-skills) | Medium-low |

**Reading the ranking:** #1–5 and #7–9 are *proven demand with proven supply*. #6 and #10 are *proven attention, unproven value*. #11–15 are *proven demand with unproven or missing supply* — the actual opportunity.

---

## 9. What this means for a new skill

### Takeaway
Build into the gap between measured pain and installed supply: evals, retrieval quality, cost/latency/context engineering, and production operations — and package them as *executable, verifiable* skills scoped to one phase, not as another all-in-one methodology.

### Cited Findings (basis for the recommendations)
- Evaluation is the top stack challenge (**20%**) while evals adoption is only **52.4%** offline / **37.3%** online — [Notion et al.](https://www.notion.com/lp/ai-engineering-survey); [LangChain](https://www.langchain.com/state-of-agent-engineering).
- **49%** use RAG but RAG skills do not rank — [Notion et al.](https://www.notion.com/lp/ai-engineering-survey); [Linkly](https://linkly.ai/skills/most-installed).
- Production failure is dominated by capacity and context economics: rate limits ~1/3 of errors, 69% of input tokens are system prompts, only **28%** of calls cache — [Datadog](https://www.datadoghq.com/state-of-ai-engineering/).
- Only **19.9%** delegate production operations and **36%** refuse to — a trust gap, not a demand gap — [SO 2026](https://survey.stackoverflow.co/2026/ai/data).
- Skills that ship scripts outperform instruction-only skills; auto-invocation is unreliable, so trigger quality and explicit invocation matter — [HN](https://news.ycombinator.com/item?id=46697908); [dev.to/AWS](https://dev.to/aws/the-most-popular-ai-coding-skills-right-now-4183).
- **36%** of skills have security flaws and **341** malicious skills were counted on one registry — provenance and review are part of the product — [Snyk](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/); [prplbx](https://www.prplbx.com/blog/agent-skills-supply-chain).
- Composable, single-purpose skills are winning share against monoliths: one author's set holds **14 of the top 100** installs — [Linkly](https://linkly.ai/skills/most-installed).

### Inferences / Recommendations
1. **Pick a phase, not a lifecycle.** The market is saturated with end-to-end frameworks and thin on single gates. A skill that does one gate (e.g. "build the eval set for this change") has less context cost and a clearer trigger.
2. **Ship an artifact and a verification step.** The recurring successful pattern is input → artifact → check: failing test → pass, diff → review, trace → diagnosis. Skills without an artifact decay into slash-command prose.
3. **Target the eval gap first.** Highest measured pain, lowest ranked supply, and a natural artifact (dataset + rubric + run). MLflow/Langfuse show the technique but not a packaged, installable skill — [MLflow](https://mlflow.org/blog/evaluating-improving-agent-skills/); [Langfuse](https://langfuse.com/blog/2026-02-26-evaluate-ai-agent-skills).
4. **Then retrieval quality and context economics.** Chunking/reranking/groundedness checks, prompt-cache layout, system-prompt budgeting, and rate-limit/backoff patterns are all measurable and all absent from top installs — [Datadog](https://www.datadoghq.com/state-of-ai-engineering/).
5. **Treat MLOps/platform as a separate product.** They buy versioned, vendor-maintained, permission-scoped skills (AWS, Cloudflare pattern), not community prompt packs — [dev.to/AWS](https://dev.to/aws/the-most-popular-ai-coding-skills-right-now-4183); [Linkly](https://linkly.ai/skills/top-repos).
6. **Make the trigger boring and explicit.** Because auto-selection is unreliable, invest in a precise description, a `/command`, and a hook fallback; document when *not* to use it — [HN](https://news.ycombinator.com/item?id=46697908).
7. **Design for review, not virality.** Stars are dominated by one-file manifestos; installs by vendor bundles. Neither predicts retention. Optimize for repeat use in a phase that happens daily (73% daily coding-agent use) — [SO 2026](https://survey.stackoverflow.co/2026/ai/data).
8. **Ship provenance.** Signed releases, pinned versions, a readable SKILL.md, no network calls by default. The "skill-vetter" skill at 279k installs is evidence users are already paying attention to this — [Linkly](https://linkly.ai/skills/most-installed).

### Gaps
- These recommendations are inferred from demand/supply mismatches, not from a controlled test. There is no public evidence that a well-built eval or RAG skill would achieve adoption; the install chart's bias toward coding and media is strong enough that a technically better skill could still lose on distribution.
- No pricing/willingness-to-pay data exists for skills; the entire market is free and install-count-driven, so "value" here means usage, not revenue.
