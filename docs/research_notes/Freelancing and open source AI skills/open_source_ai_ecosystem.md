# Open-Source AI Agent Ecosystem and Reusable Skill Packages (as of 22 October 2026)

> Scope note: all GitHub star/fork/issue counts below were pulled from the GitHub REST API on 2026-10-22 (UTC) unless another date is stated. Download counts are PyPI (`pypistats.org`, trailing 30 days) and npm (`api.npmjs.org`, last month), also read 2026-10-22. Both are volatile and include CI/mirror traffic. The ecosystem moved sharply in 2025–2026: skills repositories now out-star most agent frameworks, two well-known coding agents were archived or acquired, and several benchmark boards disagree by 20+ points on the same model.

## Which open-source agent projects are most popular and powerful by stars, downloads, contributors, release activity, and benchmarks?

### Takeaway
By raw attention, the winners are no longer the classic frameworks: OpenClaw (392.8k stars), the Superpowers skills framework (303.6k), Nous Research's Hermes Agent (256.2k) and OpenCode (220.1k) lead, while LangChain (148.3k) remains the most-downloaded framework by a wide margin (170M PyPI downloads/month). "Power" is better judged by maintenance velocity, contributor depth, and benchmark evidence than by stars; by those measures LangChain/LangGraph, OpenHands, Cline, OpenCode, Goose and the Microsoft Agent Framework are the strongest maintained projects, while Aider, Roo Code, Continue, AutoGen and SWE-agent are dormant, archived, acquired, or superseded.

### Cited Findings

**Tier 1 — attention leaders (stars, 22 Oct 2026)**

| Project | Category | Stars | Forks | Notes |
|---|---|---:|---:|---|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Personal assistant / agent gateway | 392,764 | 82,555 | MIT, TypeScript, created 2025-11-24 |
| [obra/superpowers](https://github.com/obra/superpowers) | Skills framework / methodology | 303,598 | 27,053 | MIT, created 2025-10-09; only ~38 contributors |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Self-hosted general agent | 256,178 | 55,933 | Python, created 2025-07-22 |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | Coding agent (TUI/desktop/IDE) | 220,087 | 29,413 | MIT, created 2025-04-30 |
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | Workflow automation + AI | 208,340 | 61,217 | Fair-code, not an agent SDK |
| [langgenius/dify](https://github.com/langgenius/dify) | Low-code agent/RAG platform | 159,266 | 25,160 | |
| [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | Visual agent builder | 155,921 | 10,238 | |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Coding agent (public repo) | 152,884 | 26,763 | 15,434 open issues; repo is the public issue/docs surface (see Gaps) |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Agent framework | 148,277 | 24,884 | MIT |
| [openai/codex](https://github.com/openai/codex) | Coding agent (Rust CLI) | 130,460 | 20,568 | Apache-2.0 |
| [earendil-works/pi](https://github.com/earendil-works/pi) | Agent toolkit / coding CLI | 117,170 | 14,965 | TypeScript |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Coding agent | 107,519 | 14,756 | Apache-2.0 |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Cross-agent memory plugin | 102,292 | 9,013 | 293 contributors |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | MCP directory | 96,750 | 18,256 | List, not software |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | Coding agent + SDK | 91,579 | 12,157 | MIT |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Reference MCP servers | 91,484 | 11,837 | |
| [cline/cline](https://github.com/cline/cline) | IDE/CLI/desktop coding agent | 70,731 | 7,725 | Apache-2.0 |
| [microsoft/autogen](https://github.com/microsoft/autogen) | Multi-agent framework | 61,529 | 9,307 | Maintenance-only since Oct 2025 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Role-based multi-agent framework | 59,988 | 8,836 | MIT |
| [aaif-goose/goose](https://github.com/aaif-goose/goose) | General-purpose local agent | 55,532 | 6,423 | Apache-2.0, Rust |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Skills/agent directory | 56,253 | 4,850 | List |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | RAG/data framework | 52,618 | 8,410 | |
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | Terminal pair programmer | 49,693 | 5,099 | Last push 2026-05-22 |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Durable agent runtime | 43,720 | 7,495 | MIT |
| [agno-agi/agno](https://github.com/agno-agi/agno) | Agent platform | 42,863 | 6,175 | |
| [wshobson/agents](https://github.com/wshobson/agents) | Multi-harness plugin marketplace | 41,552 | 4,406 | Claude Code, Codex, Cursor, OpenCode, Copilot, Antigravity |
| [continuedev/continue](https://github.com/continuedev/continue) | Coding agent | 36,290 | 5,507 | Read-only; acquired by Cursor June 2026 |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | Agent SDK | 30,229 | 4,925 | MIT |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | Code-writing agents | 29,989 | 3,128 | |
| [mastra-ai/mastra](https://github.com/mastra-ai/mastra) | TypeScript agent framework | 29,011 | 3,033 | |
| [google/adk-python](https://github.com/google/adk-python) | Agent Development Kit | 21,964 | 4,217 | Apache-2.0 |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | Typed Python agent framework | 20,792 | 2,994 | MIT |
| [SWE-agent/SWE-agent](https://github.com/SWE-agent/SWE-agent) | Research SWE agent | 20,614 | 2,259 | Superseded by mini-SWE-agent |
| [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | Enterprise agent SDK | 14,273 | 2,499 | v1.0 April 2026 |
| [ag2ai/ag2](https://github.com/ag2ai/ag2) | AutoGen community fork | 5,011 | 754 | Apache-2.0 |

Sources for the table: GitHub REST API `repos/{owner}/{repo}` read 2026-10-22 (e.g. [OpenClaw API record](https://api.github.com/repos/openclaw/openclaw), [LangChain API record](https://api.github.com/repos/langchain-ai/langchain)); category labels from each repo description.

**Download and usage signals (last 30 days, 22 Oct 2026)**

- PyPI: `langchain` 170.5M downloads/month; `langgraph` 44.8M; `strands-agents` 37.1M; `openai-agents` 12.4M; `google-adk` 10.1M; `pydantic-ai` 5.4M; `crewai` 2.44M; `llama-index` 2.94M; `openhands-ai` 461k; `smolagents` 426k; `autogen-agentchat` 380k; `aider-chat` 260.5k; `agent-framework` 190k; `ag2` 165k — [pypistats.org](https://pypistats.org/api/packages/langchain/recent) (same endpoint queried for each package).
- npm: `@modelcontextprotocol/sdk` 256.8M/month; `ai` (Vercel AI SDK) 118.6M; `@openai/codex` 91.5M; `@anthropic-ai/claude-code` 49.1M; `opencode-ai` 11.6M; `@mastra/core` 8.0M; `@google/gemini-cli` 1.6M; `cline` 302k; `@qwen-code/qwen-code` 314k; `@charmland/crush` 36k; `@continuedev/cli` 19.8k — [npm downloads API](https://api.npmjs.org/downloads/point/last-month/@modelcontextprotocol/sdk).
- Registry/package counts are inflated by CI, mirrors and transitive installs; they are upper bounds on human use, not user counts — [Major Labs MCP data notes](https://majorlabs.co/data).

**Survey-level adoption (the best independent demand data)**

- Stack Overflow 2026 (n=17,464): 83% use at least one AI tool; 65.9% use coding assistants/agents; 26.2% use "AI agents or automated workflows"; 73% of coding-agent users use them daily — [Stack Overflow 2026 AI data](https://survey.stackoverflow.co/2026/ai/data).
- Coding agents used in the past year among respondents: Claude Code 65.5%, GitHub Copilot 58.7%, OpenAI Codex 29.5%, Cursor 25.5%, Google Antigravity 16.0%, Gemini Code Assist 14.6%, OpenCode 13.6%, JetBrains AI 12.8%, Cline 4.5%, Pi 4.4%, Continue 3.8%, Kilo Code 3.2%, Aider 2.1% — [Stack Overflow coding-agent table](https://survey.stackoverflow.co/2026/ai/data/ai-code-agent).
- Orchestration/automation usage: LangChain 30%, OpenAI Agents SDK 24%, Make 39%, n8n 33% — [Stack Overflow 2026 AI overview](https://survey.stackoverflow.co/2026/ai).
- JetBrains Developer Ecosystem Survey 2026 (15,000+ professional developers, May–July 2026): 90% use an AI coding agent at work at least weekly, 68% daily; Claude Code 39% at work (47% in the US), Codex 16% (up from 3% in Jan 2026), Copilot 21% (down from 29% a year earlier), Cursor 12%, OpenCode 7%, Antigravity 6% — [JetBrains research](https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/).
- JetBrains also reports ~47% of code written last month was fully agent-generated, 38% AI-assisted, 27% manual (self-reported, bucketed averages) — [JetBrains](https://blog.jetbrains.com/research/2026/08/how-much-code-do-developers-really-let-agents-write/).

**Benchmarks (and why they conflict)**

- Official SWE-bench Verified (any scaffold, 500 human-validated issues), as of 22 Oct 2026: Claude Opus 4.5 (high) 76.8% with mini-SWE-agent; Gemini 3 Flash (high) 75.8%; MiniMax M2.5 (high) 75.8%; Claude Opus 4.6 75.6%; GPT-5.2-Codex 72.8% — [BenchLeader SWE-bench Verified](https://www.benchleader.com/benchmarks/swe_bench_verified_any).
- Cost per resolved task on the same runs ranged from $0.097 (MiniMax M2.5) to $0.982 (Opus 4.5), a ~10x spread at similar scores — [Vibe Code Textbook task-level analysis](https://vibecodetextbook.com/posts/swe-bench-verified-task-by-task.html).
- Conflicting boards: Vals AI reports Claude Opus 5 at 97.0% and DeepSeek V4 Pro at 96.4% on SWE-bench Verified (76 models), while Epoch AI reports Claude Opus 4.7 at 83.5% and the official board tops out at 76.8% — [Vals AI board via llmbenchmark.ai](https://llmbenchmark.ai/benchmarks/vals-swe-bench); [Epoch AI via AI.info](https://ai.info/tracker/benchmarks/swe-bench-verified); [SWE-bench official](https://www.swebench.com/verified.html). The spread reflects different harnesses, prompts, retries/scaffolds, and possible benchmark saturation/contamination; scores are not comparable across boards.
- Terminal-Bench 2.0 (89 hard containerized tasks; 142 published submissions): top entries NexAU-AHE/GPT-5.5 84.7% ±2.1, LemonHarness 84.5%, Capy 83.1%, Codex CLI/GPT-5.5 82.2%; the top 10 sit within ~7 points and confidence intervals overlap — [Snorkel Terminal-Bench 2.0 leaderboard](https://snorkel.ai/leaderboard/terminal-bench-2-0/); benchmark paper: [arXiv 2601.11868](http://arxiv.org/abs/2601.11868). Terminal-Bench has already moved to a 4.0 edition, so 2.0 numbers are a snapshot — [tbench.ai](https://www.tbench.ai/).
- OpenHands Software Agent SDK V1: 72.8% SWE-bench Verified with Claude Sonnet 4.5, 67.9% GAIA, and later 76.6% SWE-bench Verified with Opus 4.5 in the MLSys 2026 paper; published SOTA at the time was 79.2% — [OpenHands SDK paper](https://arxiv.org/html/2511.03690v1).
- SWE-agent's README still claims "state of the art among open-source projects", but now carries a warning that most development moved to `mini-swe-agent`, which "has superseded SWE-agent" and matches its performance with a simpler loop — [SWE-agent README](https://github.com/SWE-agent/SWE-agent).

**Release/activity evidence for "power"**

- LangChain 1.0 and LangGraph 1.0 shipped 2025-10-17/20 with LTS-style policies; by Oct 2026 LangChain was on 1.4.7 with near-weekly patches and added `langchain.mcp` in 1.4.0 (Sept 2026) — [LangChain 1.0 announcement](https://www.langchain.com/blog/langchain-langgraph-1dot0); [changelog](https://docs.langchain.com/oss/python/releases/changelog); [release policy](https://docs.langchain.com/oss/python/release-policy).
- Microsoft Agent Framework reached 1.0 (Python and .NET) on 2026-04-03, explicitly as the successor to AutoGen and Semantic Kernel, with graph workflows, middleware, MCP/A2A and migration assistants — [Microsoft DevBlog](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/); [AutoGen maintenance notice](https://github.com/microsoft/autogen/discussions/7066).
- OpenCode moved from `sst/opencode` to `anomalyco/opencode`, passed 120k stars in March 2026 and 172k by June 2026, with 900+ contributors and a company-claimed 7.5M monthly developers — [aqua-registry PR documenting the transfer](https://github.com/aquaproj/aqua-registry/pull/46521); [Ry Walker research](https://rywalker.com/research/opencode); [The Agent Times](https://theagenttimes.com/articles/opencode-crosses-120k-github-stars-as-open-source-coding-age-3e4b556f).
- OpenClaw grew from a November 2025 launch to 247k stars by 2 March 2026 and 392.8k by 22 Oct 2026, with a 21% fork-to-star ratio — [Wikipedia](https://en.wikipedia.org/wiki/OpenClaw); [findarepo](https://findarepo.com/repo/openclaw/openclaw/).
- Hermes Agent shipped v0.22.0 on 13 Oct 2026, claiming ~24,200 commits, ~6,080 merged PRs and ~2,520 contributors in that cycle — [Hermes v0.22.0 release](https://github.com/NousResearch/hermes-agent/releases). Treat the contributor figure as unverified/implausible for a single cycle; it is likely cumulative or counting co-authored/automated accounts.

### Inferences
- Stars have decoupled from engineering adoption: skills/methodology repos and consumer-style personal agents can out-star every framework while having far fewer contributors and no benchmark presence. A 300k-star skills repo with ~38 contributors is a media phenomenon, not necessarily a large engineering community.
- Download counts confirm LangChain/LangGraph as the default Python production substrate and MCP SDKs as the real "plumbing" layer; framework stars understate MCP's importance.
- The coding-agent market consolidated around Claude Code and Codex at the top, with OpenCode as the leading independent open-source challenger and Cline/Kilo/Goose as smaller but healthy alternatives. Aider, Roo Code and Continue are no longer safe default recommendations for new work in Oct 2026.
- Model choice now dominates benchmark outcomes more than scaffold choice, but scaffold still matters at the margin (Terminal-Bench top-10 spread, harness-dependent SWE-bench results).

### Gaps
- GitHub contributor counts for the largest repos could not be read (API rate limit, HTTP 403 on 2026-10-22); only a few counts were captured (Superpowers 38, claude-mem 293, ponytail 130, caveman 94, ruflo 78, Kilo 1,268). Contributor depth for LangChain, OpenHands, Cline and OpenCode is therefore inferred from issue volume/release notes, not measured.
- No primary source confirmed whether `anthropics/claude-code` contains the agent's source or only issues/docs; its stars may measure attention, not open-source adoption. Its license field is absent/NOASSERTION in the API and it should not be grouped with Apache/MIT agents without qualification.
- No reliable public data on paid usage, enterprise seats, or retention for any of these projects; vendor claims (OpenCode 5–7.5M monthly developers, Hermes contributor counts) are self-reported.
- Benchmark scores for agent *scaffolds* (as opposed to models) are sparse, vendor-run, and not independently replicated.

## What are the dominant architectures and design patterns?

### Takeaway
Six patterns dominate: (1) graph/state-machine orchestration with durable checkpoints (LangGraph, Microsoft Agent Framework); (2) role-based crews plus event-driven flows (CrewAI); (3) minimal tool-loop SDKs with handoffs and guardrails (OpenAI Agents SDK, Claude Agent SDK); (4) event-sourced, sandboxed software-engineering agents (OpenHands V1); (5) client/server coding harnesses with human approval and provider abstraction (OpenCode, Cline, Goose); and (6) skills-as-markdown procedural memory layered on top of any harness (Agent Skills/Superpowers). MCP has become the common tool bus, and A2A the emerging agent-to-agent bus.

### Cited Findings
- LangChain 1.0 centers on `create_agent` (model → tools → response loop) built on the LangGraph runtime, with middleware for dynamic prompts, summarization, tool access, state and guardrails; LangGraph adds durable state, persistence, human-in-the-loop interrupts and time travel — [LangChain 1.0](https://www.langchain.com/blog/langchain-langgraph-1dot0); [LangChain v1 docs](https://docs.langchain.com/oss/python/releases/langchain-v1).
- LangGraph 1.1/1.2 added per-node timeouts, node-level error handlers, graceful drain/shutdown and a `DeltaChannel` for long-running threads — [LangChain changelog](https://docs.langchain.com/oss/python/releases/changelog).
- Microsoft Agent Framework combines AutoGen's agent abstractions with Semantic Kernel's enterprise features; its stable 1.0 surface includes graph-based workflows, sequential/concurrent/handoff/group-chat/Magentic orchestration, checkpointing, YAML-declarative agents, middleware, MCP and A2A — [Microsoft Agent Framework 1.0](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/); [overview](https://learn.microsoft.com/en-us/agent-framework/overview/).
- OpenAI Agents SDK's core concepts are agents, sandbox agents (containerized long-horizon work), realtime/voice agents, agents-as-tools/handoffs, tools (functions, MCP, hosted), guardrails, human-in-the-loop and tracing — [OpenAI Agents SDK README](https://github.com/openai/openai-agents-python).
- OpenHands V1 is an event-sourced architecture: immutable agent configuration, typed tools with MCP integration, a workspace abstraction that moves the same agent from local to sandboxed remote execution, a built-in REST/WebSocket server, and an LLM-based security analyzer for actions — [OpenHands SDK paper](https://arxiv.org/html/2511.03690v1). Event-sourcing overhead is negligible (0.2 ms median persist, 4.1 ms full replay) — same source.
- Cline ships as IDE extension, CLI and desktop app, with human-in-the-loop approval, Plan/Act-style operation, MCP servers and plugins — [Cline README](https://github.com/cline/cline).
- OpenCode is a provider-agnostic client/server harness with build (full access) and plan (read-only) agents, a `general` subagent, LSP, and 75+ providers via Models.dev — [OpenCode README](https://github.com/anomalyco/opencode); [Ry Walker](https://rywalker.com/research/opencode).
- Goose is a Rust general-purpose local agent with desktop, CLI and embeddable API, 15+ providers and extension/MCP-based tools — [Goose README](https://github.com/aaif-goose/goose).
- AutoGen pioneered event-driven GroupChat/team orchestration but is now maintenance-only; its successor maps those patterns onto typed graph workflows — [AutoGen update](https://github.com/microsoft/autogen/discussions/7066); [migration guide](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/).
- MCP is now embedded in major frameworks: LangChain 1.4 ships `langchain.mcp` built on FastMCP with OAuth 2.1 and interrupt-driven elicitation; Microsoft Agent Framework and OpenAI Agents SDK both treat MCP as a first-class tool source — [LangChain changelog](https://docs.langchain.com/oss/python/releases/changelog); [Microsoft](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/); [OpenAI Agents SDK](https://github.com/openai/openai-agents-python).
- MCP adoption is large and still growing: official registry ~48,180 servers (65% remote endpoints), 38,503 public `mcp-server` repos, TypeScript SDK 76.7M npm downloads/week, Python `mcp` 67.9M PyPI downloads/week — [MCP adoption statistics](https://gravity.fast/data/mcp-adoption-statistics/). Counts differ by methodology: 46,303 in one deep-scan and 139,477 deduplicated across five registries — [Major Labs](https://majorlabs.co/data); [MCP Toplist](https://mcptoplist.com/reports/mcp-ecosystem/2026-10).
- Skills architecture is standardizing on folders with a `SKILL.md` (YAML `name` + `description`), optional scripts/resources, and progressive disclosure (metadata loaded first, body/references only when needed) — [anthropics/skills README](https://github.com/anthropics/skills); [Agent Skills spec](https://agentskills.io); [addyosmani/agent-skills README](https://github.com/addyosmani/agent-skills).
- Methodology skills add process control rather than tools: Superpowers enforces brainstorm → spec → plan → worktrees → TDD → review → finish, with subagent-driven execution — [Superpowers README](https://github.com/obra/superpowers).
- Multi-harness packaging is emerging: Vercel's `skills` CLI installs into 70+ agents, and wshobson/agents targets Claude Code, Codex, Cursor, OpenCode, Copilot and Antigravity from one repo — [skills.sh docs](https://www.skills.sh/docs); [wshobson/agents](https://github.com/wshobson/agents); [addyosmani README](https://github.com/addyosmani/agent-skills).

### Inferences
- The durable-execution graph (LangGraph, Microsoft Workflows) is the mature answer for long-running, resumable, human-approved work; the minimal tool-loop SDK is the better answer for single-purpose agents and is easier to embed.
- Event-sourced sandboxing (OpenHands) is the strongest architectural fit for autonomous software engineering because it gives replay, auditability and safe remote execution; it is heavier than a CLI harness.
- Skills are becoming the portable "application layer," while MCP is the portable "tool layer." Frameworks compete below that; harnesses compete on UX, provider access and permissions.
- Convergence on MCP + A2A + AGENTS.md/SKILL.md reduces lock-in at the protocol level, but vendor SDKs still differentiate on hosted tools, tracing and sandbox services.

### Gaps
- No public, independent architectural comparison of token efficiency, latency or failure modes across harnesses; vendor papers (OpenHands) are the main deep architectural evidence.
- CrewAI's current internal architecture (Crews vs Flows) was not verified from a primary doc in this pass; only its role-based positioning is confirmed by the repo.
- A2A adoption remains much smaller than MCP (6.9M weekly SDK downloads vs 144.7M for MCP), and no killer open-source A2A product was identified — [MCP adoption statistics](https://gravity.fast/data/mcp-adoption-statistics/).

## Which skill packages are reusable across agents and which are ecosystem-specific?

### Takeaway
The reusable layer is plain `SKILL.md` packs plus MCP servers: Superpowers (methodology), addyosmani/agent-skills (25 lifecycle skills), anthropics/skills (reference/example skills), mattpocock/skills (workflow skills) and wshobson/agents (multi-harness plugin marketplace) install across Claude Code, Codex, Cursor, Gemini CLI, OpenCode, Copilot and others via the `skills` CLI. Ecosystem-specific layers are Claude Code plugins/marketplaces, OpenAI Codex plugins, Cline plugins, and OpenClaw's ClawHub; they are convenient but do not port. Most "skills" are prompt/procedure files, not sandboxed code, so portability is high but enforcement and security are weak.

### Cited Findings
- `anthropics/skills` reached 182,984 stars and 21,670 forks by 22 Oct 2026; it hosts creative, technical and enterprise skill examples, the Agent Skills spec and a template; the docx/pdf/pptx/xlsx skills are source-available, not open source — [repo](https://github.com/anthropics/skills); star count from [GitHub API](https://api.github.com/repos/anthropics/skills).
- Install counts on skills.sh's leaderboard (8-week activity window): `find-skills` (vercel-labs) 4.0M, `grill-me` (mattpocock) 1.4M, `agent-browser` 1.2M, `improve-codebase-architecture` 1.2M, `tdd` 1.1M, `handoff` 1.0M, `frontend-design` (anthropics) 1.0M — [skills.sh leaderboard](https://www.skills.sh/). Ranking is based on anonymous installer telemetry, not quality — [skills.sh docs](https://www.skills.sh/docs).
- skills.sh launched 20 Jan 2026; by 5 June 2026 it claimed 600,000 open-source skills via its API, with Snyk scanning installs — [Vercel changelog](https://vercel.com/changelog/introducing-skills-the-open-agent-skills-ecosystem); [Snyk](https://snyk.io/blog/snyk-vercel-securing-agent-skill-ecosystem/); 600k figure from [Totalum comparison](https://www.totalum.app/blog/agent-skills-marketplaces-2026) (secondary).
- Registry scale (22 Oct 2026): 60,909 agent skills and 45,833 plugins across 20 sources; 22,734 skills.sh entries, 2,728 Claude Code marketplaces, 7,400 ClawHub entries, 183 Copilot plugins, 65 Codex plugins — [Small Print stats](https://smallprint.dev/stats).
- Ecosystem-specific: ClawHub is OpenClaw's skill/plugin registry (9,524 stars) — [OpenClaw org](https://github.com/orgs/openclaw/repositories); ClawHub is listed with 7,400 entries — [Small Print](https://smallprint.dev/stats). OpenAI Codex plugins and Cline plugins are host-bound by design — [Totalum](https://www.totalum.app/blog/agent-skills-marketplaces-2026).
- Reusable packs: Superpowers has ~15 skills, v7.0.0 (10 Oct 2026) rebuilt brainstorming, and is listed in Anthropic's plugin marketplace — [README](https://github.com/obra/superpowers); [Kunal Ganglani analysis](https://www.kunalganglani.com/blog/superpowers-agentic-skills-framework). addyosmani/agent-skills ships 25 skills + 9 slash commands + 4 personas + 7 checklists, with native adapters for Claude Code, Codex, Cursor, Gemini CLI, OpenCode, Copilot CLI, Kiro and Antigravity, and warns that per-skill installs omit shared `references/` (issue #361) — [README](https://github.com/addyosmani/agent-skills).
- wshobson/agents (41.5k stars) explicitly packages one plugin marketplace for Claude Code, Codex, Cursor, OpenCode, GitHub Copilot and Google Antigravity — [repo](https://github.com/wshobson/agents).
- Aggregators have no gatekeeping: SkillsMP indexes hundreds of thousands of `SKILL.md` files, LobeHub ~169k, and neither reviews content — [AgentVolt comparison](https://www.agentvolt.ai/blog/best-agent-skills-marketplaces); [Totalum](https://www.totalum.app/blog/agent-skills-marketplaces-2026).
- Security is the weak point: Snyk scans skills at install time, but the registry itself says it "cannot guarantee the quality or security of every skill" — [skills.sh docs](https://www.skills.sh/docs); [Snyk](https://snyk.io/blog/snyk-vercel-securing-agent-skill-ecosystem/). One secondary survey reports flaws in more than a third of skills on one open registry — [AgentVolt](https://www.agentvolt.ai/blog/best-agent-skills-marketplaces). Small Print records 5,728 security advisories, 1,214 naming an MCP server/skill/plugin — [Small Print](https://smallprint.dev/stats).

### Inferences
- The most reusable assets are process/methodology skills (TDD, spec, review, debugging) and single-purpose utilities (browser, docs, search), because they depend only on a shell/file system and generic agent capabilities.
- Tool-wrapper skills (Jira, Stripe, Notion, browser automation) are increasingly shipped as MCP servers instead, because MCP gives typed tools, auth and a runtime rather than prompt instructions.
- Host-specific plugin formats are a distribution moat, not a technical necessity; multi-harness repos are the pragmatic hedge.
- A skill pack's star count is a poor quality signal. Contributor count, eval coverage, release cadence and security review are better; Superpowers' 303k stars vs ~38 contributors is the extreme example.

### Gaps
- No comprehensive, independent quality/security audit of the top 100 skills was found; most security claims are vendor or secondary.
- Actual install-to-retention data is private; leaderboard installs may include repeated/CI installs.
- The Agent Skills spec's governance (who controls changes, compatibility guarantees) was not verified beyond the spec site and Anthropic's repo.

## What are the trade-offs between frameworks, coding agents, and skill libraries?

### Takeaway
Frameworks buy control, durability and integrations at the cost of abstraction and lock-in; coding agents buy immediate productivity and UX at the cost of opacity, permission risk and vendor direction; skill libraries buy cheap, portable process enforcement at the cost of being advisory, unversioned in practice, and a supply-chain risk. The right default in Oct 2026 is a thin stack: one harness + MCP for tools + a small curated skill pack + a framework only where durable orchestration is genuinely needed.

### Cited Findings
- Framework abstraction trade-off is explicit in LangChain's own guidance: use LangChain for standard loops and speed, LangGraph for deterministic+agentic mixes, long-running workflows, human oversight and cost/latency control — [LangChain 1.0](https://www.langchain.com/blog/langchain-langgraph-1dot0).
- Microsoft positions Agent Framework for enterprise .NET/Python with telemetry, approvals, durability and A2A/MCP, but it is a successor product: AutoGen receives only critical fixes, and Semantic Kernel is supported for at least a year after AF GA — [Microsoft](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/); [SK/AF position](https://devblogs.microsoft.com/agent-framework/semantic-kernel-and-microsoft-agent-framework/).
- Open-source coding agents differ mainly on openness and execution model: OpenCode (MIT, 75+ providers, local-first), Cline (Apache-2.0, IDE+CLI+desktop, approvals), Goose (Apache-2.0, Rust, local general agent), Codex (Apache-2.0) and Gemini CLI (Apache-2.0) versus Claude Code's public repo with unclear source licensing — [OpenCode](https://github.com/anomalyco/opencode); [Cline](https://github.com/cline/cline); [Goose](https://github.com/aaif-goose/goose); [Codex](https://github.com/openai/codex); [Gemini CLI](https://github.com/google-gemini/gemini-cli).
- Consolidation risk is real: Roo Code (24.1k stars, 3M+ VS Code installs) was archived 15 May 2026 and the team pivoted to Roomote; Continue (34k stars) was acquired by Cursor in June 2026 and its repo is read-only; Aider has had no commit since 22 May 2026 and 531 open PRs; Flowise's last push was Aug 2026 and the repo is now archived — [Roo Code notice](https://github.com/RooCodeInc/Roo-Code); [Kilo shutdown analysis](https://kilo.ai/compare/roo-code-shutdown-roomote); [The New Stack on Continue](https://thenewstack.io/cursor-acquires-continue-coding/); [Aider status analysis](https://aicoderscope.com/blog/aider-2026-stalled-what-happened-alternatives/); [Flowise API record](https://api.github.com/repos/FlowiseAI/Flowise).
- Skills are advisory, not enforced: they are markdown instructions loaded into context; addyosmani's pack compensates with anti-rationalization tables and verification gates, but nothing prevents an agent from ignoring them — [addyosmani README](https://github.com/addyosmani/agent-skills); [Superpowers README](https://github.com/obra/superpowers).
- Security risk is structural: installing a skill or MCP server grants an agent new capabilities. MCP has 188,872 servers on record, 59.2% of remote servers return a tool list without sign-in, and 1,214 advisories name an MCP/skill/plugin — [Small Print](https://smallprint.dev/stats).
- Benchmark-based selection is unreliable: SWE-bench Verified scores range from 76.8% (official) to 97.0% (Vals AI) for top models, and Terminal-Bench top-10 confidence intervals overlap — [BenchLeader](https://www.benchleader.com/benchmarks/swe_bench_verified_any); [llmbenchmark.ai](https://llmbenchmark.ai/benchmarks/vals-swe-bench); [Snorkel](https://snorkel.ai/leaderboard/terminal-bench-2-0/).
- Cost matters more than a few benchmark points: on one controlled SWE-bench run, cost per resolved task varied ~10x ($0.097–$0.982) among near-top systems — [Vibe Code Textbook](https://vibecodetextbook.com/posts/swe-bench-verified-task-by-task.html).

### Inferences
- For client work, avoid betting a product on a single-maintainer or VC-pivoting harness; wrap the agent behind your own interface and keep prompts/skills/MCP config in your repo so you can switch.
- Frameworks are most justified when you need durable state, approvals, multi-tenant serving or observability; otherwise a 200-line tool loop plus MCP is cheaper to own.
- Skill libraries are highest ROI for standardizing *how* work is done (spec, TDD, review) and lowest ROI for proprietary integrations, which belong in MCP.
- The "open source" label needs checking per project: some are fully open, some are open-core, some are public issue trackers, and some are source-available.

### Gaps
- No independent total-cost-of-ownership study comparing frameworks/harnesses on the same real tasks; vendor and blog benchmarks dominate.
- Licensing details for several coding agents (especially Claude Code) were not verified from LICENSE files.
- Long-term maintenance commitments are unclear for community forks (AG2, ZooCode/cecli, OpenClaw after its creator joined OpenAI).

## What should a freelancer or open-source contributor learn first?

### Takeaway
Learn the portable substrate first — MCP, `SKILL.md`/Agent Skills, `AGENTS.md`, git-native workflows and evaluation — then one harness deeply and one framework only as needed. The fastest monetizable skills for a freelancer in late 2026 are building private MCP connectors and curated skill packs, auditing agent security/permissions, and running evals; the fastest route to OSS relevance is contributing MCP servers, benchmark tasks, docs and harness integrations rather than another wrapper framework.

### Cited Findings
- Demand is mainstream but shallow: 83% of developers use AI tools, 66% use coding agents, yet only 26% use agents/automated workflows — [Stack Overflow 2026](https://survey.stackoverflow.co/2026/ai/data). This gap is where integration work lives.
- Claude Code (65.5%) and Copilot (58.7%) dominate mindshare, with Codex (29.5%) rising fast; OpenCode is the leading independent OSS tool at 13.6% (SO) / 7% at work (JetBrains) — [Stack Overflow](https://survey.stackoverflow.co/2026/ai/data/ai-code-agent); [JetBrains](https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/).
- The skills installer is a single command and supports 70+ agents: `npx skills add <owner>/<repo>` — [skills.sh docs](https://www.skills.sh/docs). Authoring needs only `name` and `description` frontmatter plus markdown — [anthropics/skills](https://github.com/anthropics/skills).
- Multi-harness skill packs are already a documented pattern, including per-host adapters and install instructions for Claude Code, Codex, Cursor, Gemini CLI, OpenCode, Copilot, Kiro and Antigravity — [addyosmani README](https://github.com/addyosmani/agent-skills); [wshobson/agents](https://github.com/wshobson/agents).
- MCP is the largest tool surface: ~48k registry servers, 38.5k tagged repos, and SDK downloads in the tens of millions per week — [gravity.fast](https://gravity.fast/data/mcp-adoption-statistics/). Registry listings vastly exceed maintained/evaluable servers (~1,200 genuinely evaluable in one deep scan), so quality/integration work is scarce — [Major Labs](https://majorlabs.co/data).
- The benchmark/eval skill is in demand because results are contested and harness-dependent; OpenHands open-sourced its benchmark harness and Index, and SWE-bench maintains a bash-only mini-SWE-agent track — [OpenHands benchmarks](https://github.com/OpenHands/benchmarks); [SWE-bench](https://www.swebench.com/verified.html).
- Security is an explicit, unsolved gap: skills.sh relies on Snyk scanning but disclaims guarantees; registries are largely unreviewed; MCP has thousands of advisories — [skills.sh docs](https://www.skills.sh/docs); [Snyk](https://snyk.io/blog/snyk-vercel-securing-agent-skill-ecosystem/); [Small Print](https://smallprint.dev/stats).
- Working examples of high-leverage OSS contributions exist: Superpowers adds skills + a methodology; addyosmani adds skills + evals + host adapters; Kilo rebuilt on the OpenCode server and invites Roo contributors — [Superpowers](https://github.com/obra/superpowers); [addyosmani](https://github.com/addyosmani/agent-skills); [Kilo](https://blog.kilo.ai/p/thank-you-roo).

### Inferences
- A freelancer's credible offer is not "I build agents" but "I connect your systems to agents safely and prove it works": private MCP server + permission model + eval suite + a small skill pack for the team's workflow.
- Learning one harness deeply (Claude Code or Codex, plus OpenCode for model freedom) transfers better than learning five frameworks superficially, because skills/MCP/AGENTS.md are portable.
- Open-source contribution leverage is highest in unglamorous gaps: docs, setup adapters, benchmark tasks, security review, and MCP server maintenance. Star-heavy skill repos have tiny contributor cores, so maintainers are receptive.
- Avoid building a business on a single-maintainer tool or a repo whose stars are disconnected from contributors; prefer foundation/governed projects or ones with corporate backing and a public roadmap.

### Gaps
- No public data on freelance rates, demand volume, or earnings for agent/MCP/skill work; the monetization advice is inference from adoption gaps, not measured market data.
- It is unclear which credentials or portfolios clients actually value; no survey evidence found.
- The skills job market may be crowded by low-quality packs; no data on differentiation or pricing.

## Which projects have healthy communities and clear contribution paths?

### Takeaway
The healthiest communities by observable signals are LangChain/LangGraph (weekly releases, LTS policy, large issue/PR throughput), OpenHands (peer-reviewed architecture, open benchmark harness, SDK + CLI + cloud), Cline and Kilo (large contributor bases, active plugins), Goose (foundation-hosted with a Linux Foundation health badge), and OpenCode (900+ contributors, very high release velocity). The weakest are Aider (single maintainer, dormant), Roo Code (archived), Continue (read-only), AutoGen (maintenance-only), and star-heavy skill repos with tiny contributor cores. Contribution paths are clearest where the project ships a spec/harness (MCP servers, SKILL.md, benchmark tasks), because those accept small, self-contained PRs.

### Cited Findings
- LangChain/LangGraph: 1.0 LTS policy, minor releases every 1–2 months, patches up to several times a week, and public migration guides — [release policy](https://docs.langchain.com/oss/python/release-policy). LangChain had 666 open issues and LangGraph 508 on 22 Oct 2026, with same-day pushes — [GitHub API](https://api.github.com/repos/langchain-ai/langchain).
- OpenHands: MIT, 91.6k stars, 12.2k forks, 1,093 open issues; SDK paper accepted at MLSys 2026, benchmarks repo, and a separate `software-agent-sdk` repo (1,293 stars) for modular contributions — [OpenHands](https://github.com/OpenHands/OpenHands); [SDK paper](https://arxiv.org/html/2511.03690v1); [benchmarks](https://github.com/OpenHands/benchmarks).
- Cline: Apache-2.0, 70.7k stars, 7.7k forks, 1,699 open issues, active CLI/desktop/IDE releases; plugins/skills bundled since CLI 3.0.16 — [Cline](https://github.com/cline/cline); [Totalum](https://www.totalum.app/blog/agent-skills-marketplaces-2026).
- Kilo: 27.7k stars, 1,268 contributors (the largest contributor count captured in this pass), rebuilt on the OpenCode server and openly recruiting Roo contributors — [Kilo](https://github.com/Kilo-Org/kilocode); [Kilo blog](https://blog.kilo.ai/p/thank-you-roo).
- Goose: Apache-2.0, 55.5k stars, foundation-hosted under `aaif-goose`, with a Linux Foundation health-score badge in its README — [Goose](https://github.com/aaif-goose/goose). (The `aaif` org move and foundation stewardship are visible in the repo/org name; the precise governance terms were not read.)
- OpenCode: MIT, 220k stars, 3,730 open issues, 900+ contributors and 13,000+ commits as of June 2026; very high release cadence (v1.17.3 on 10 June 2026, desktop multi-server, session APIs) — [Ry Walker](https://rywalker.com/research/opencode); [repo](https://github.com/anomalyco/opencode).
- Superpowers: 303.6k stars but only ~38 contributors and 343 open issues; maintenance score 92/100 in one independent audit, but bus factor is concentrated — [topairepos](https://topairepos.com/repos/obra/superpowers); [Kunal Ganglani](https://www.kunalganglani.com/blog/superpowers-agentic-skills-framework).
- Autogen: maintenance-only, no significant new features; users are directed to Microsoft Agent Framework — [AutoGen update](https://github.com/microsoft/autogen/discussions/7066).
- Aider: no commit since 22 May 2026, 531 open PRs, 1.4k open issues, no archive notice; maintainer said he is "busy with other projects" — [Aider status](https://aicoderscope.com/blog/aider-2026-stalled-what-happened-alternatives/); [maintainer comment](https://github.com/Aider-AI/aider/issues/4648).
- Roo Code: archived 15 May 2026 with 492 open PRs and 550 unresolved issues; community fork ZooCode and Cline/Kilo are suggested alternatives — [Roo Code](https://github.com/RooCodeInc/Roo-Code); [founder post](https://www.linkedin.com/feed/update/urn:li:activity:7461246465261240320).
- Continue: read-only after Cursor acquisition; final 2.0.0 release removed telemetry and auth as a deliberate community handoff — [Continue](https://github.com/continuedev/continue); [The New Stack](https://thenewstack.io/cursor-acquires-continue-coding/).
- MCP/skills contribution surfaces are more open than framework cores: the official registry accepts publisher-owned namespaces; skills are plain markdown; `awesome-mcp-servers` has 96.7k stars and 18.2k forks — [MCP registry](https://github.com/modelcontextprotocol/registry); [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers); [anthropics/skills](https://github.com/anthropics/skills).
- Star-based health is unreliable: an ICSE 2026 study found ~6M suspected fake stars and 18,617 repos with fake-star campaigns, with AI/LLM repos the second-largest category (16.6%); fake stars gave only a short-term boost and became a long-term liability — [ICSE paper](https://dl.acm.org/doi/10.1145/3744916.3764531); [CMU summary](https://www.cs.cmu.edu/news/2025/fake-github-stars).

### Inferences
- Prefer projects where the contribution unit is small and testable (MCP server, skill, benchmark task, adapter) over ones where the core is a large proprietary-ish runtime.
- A 300k-star repo with 38 contributors is a content/distribution success, not a community; expect fast merges but limited review depth and high key-person risk.
- Foundation or multi-vendor governance (Goose/AAIF, MCP under the Linux Foundation-adjacent registry, LangChain's LTS policy) is a better long-term bet than a single founder's repo, but even foundation projects can stagnate.
- Consolidation is a feature of the market now: contributing to a doomed fork (Roo, Continue) wastes effort; contributing upstream to OpenCode/Kilo/OpenHands/Cline has clearer absorption paths.

### Gaps
- No systematic measurement of PR review latency, first-response time, or new-contributor retention for these repos; issue counts and release cadence are proxies.
- Governance details for several projects (OpenClaw Foundation, AAIF/Goose, OpenCode/Anomaly) were not verified from primary governance documents.
- Contributor counts for most major repos could not be pulled due to API rate limits, so cross-project community comparisons are incomplete.
- The fake-star study covers 2019–2024, before the 2025–2026 agent boom; its prevalence estimate may understate current inflation in AI repos.

### Cross-cutting caveats for the report writer

- **Date discipline:** star/download/issue figures are 2026-10-22 snapshots and move daily; JetBrains data is May–July 2026; Stack Overflow data is 2026; benchmark boards are Oct 2026 snapshots but use different harnesses.
- **Definitions:** "agent framework" (LangChain, LangGraph, CrewAI, AutoGen/AF, OpenAI Agents SDK, Google ADK, Pydantic AI, Agno, Mastra) ≠ "coding agent/harness" (Claude Code, Codex, OpenCode, Cline, Goose, Kilo, Aider) ≠ "skill library" (Superpowers, addyosmani/agent-skills, anthropics/skills, mattpocock/skills) ≠ "tool protocol/registry" (MCP, Smithery, skills.sh, ClawHub) ≠ "low-code platform" (Dify, Langflow, n8n).
- **Openness:** MIT/Apache projects (OpenCode, Cline, Goose, Codex, Gemini CLI, OpenHands, LangChain) are genuinely open source; Claude Code's public repo and several "skills" repos are not fully open (source-available components, host-bound plugins).
- **Quantitative limits:** stars are gameable (ICSE 2026); downloads include CI/mirrors; registry counts overlap and include experiments; survey self-reports are noisy; benchmarks are harness- and prompt-sensitive and often vendor-run.
- **Strongest evidence:** official release notes/blogs (LangChain, Microsoft, OpenHands paper, Anthropic/Vercel/Snyk), independent surveys (Stack Overflow, JetBrains), and primary GitHub/registry APIs. **Weakest:** SEO comparison sites, star-count aggregators, and vendor claims about monthly developers.
