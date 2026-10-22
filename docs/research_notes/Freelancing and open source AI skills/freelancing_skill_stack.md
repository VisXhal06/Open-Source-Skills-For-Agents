# Installable Agent Skills and Workflows for Freelancers (October 2026)

> Scope: installable skills (`SKILL.md` packages), MCP servers, plugins, and CLI tool stacks used by independent professionals to deliver client work. Snapshot date: 22 October 2026. "Older evidence" means anything dated before roughly July 2026 and is marked inline.
>
> Method note: skills.sh install counts are anonymous, deduplicated CLI telemetry. A repo install can count once per skill it contains, so counts measure bundle weight, not unique users or quality. GitHub stars measure attention. Neither is a capability or security review. Several third-party "leaderboard" sites (SkillSignal, Edge, aiagents.org.uk, topaiskills, OpenAgentSkill) publish numbers that cannot be independently verified and sometimes conflict; they are treated as secondary signals only.

## Which installable agent skills are most adopted and most powerful for freelance delivery?

### Takeaway
Adoption is concentrated in a small number of publisher families, and the head of the market is dominated by *engineering process* skills (Matt Pocock's pack, Superpowers) plus *discovery and browser* utilities. For actual freelance deliverables, the highest-adoption non-coding skills are Anthropic's document skills (`pptx`, `pdf`, `docx`, `xlsx`) and `frontend-design`. Business operations (CRM, invoicing, proposals) is the least served category by pure skills and is mostly handled by vendor MCP servers.

### Cited Findings
- The public skills.sh all-time snapshot of 18 Oct 2026 had 100 leaderboard entries, 96 unique skill IDs, and 77.6M recorded installs; 80 of the 100 sit between 500K and 1M installs, median 654,433, and the top 10 hold 18.1% of installs — [SkillSignal analysis of skills.sh](https://skill-signal.org/reports/top-100-agent-skills) (2026-10-18)
- Top of that snapshot: `find-skills` (vercel-labs/skills) 3,905,457; `grill-me` (mattpocock/skills) 1,379,134; `grill-with-docs` 1,181,124; `agent-browser` (vercel-labs/agent-browser) 1,159,197; `tdd` 1,102,991; `hyperframes-cli` 1,085,544; `setup-matt-pocock-skills` 1,018,273; `handoff` 1,001,711 — [SkillSignal](https://skill-signal.org/reports/top-100-agent-skills) (2026-10-18)
- Live skills.sh leaderboard on 22 Oct 2026 shows `find-skills` at 4.0M, `grill-me` 1.4M, `agent-browser` 1.2M, `grill-with-docs` 1.2M, `improve-codebase-architecture` 1.2M, `tdd` 1.1M, `frontend-design` 1.0M — [skills.sh](https://www.skills.sh/)
- By job category, the top 100 are: 30 workspace-app connectors, 22 cloud/vendor platforms, 20 dev workflow (review, testing, planning), 12 image/video/audio generation, 9 agent/browser tooling, 5 UI design, and only 2 marketing/sales; "business-facing" is 32 of 100, and 30 of those 32 are workspace connectors — [Pro Skill Packs study](https://proskillpacks.github.io/study/top-skills/) (2026-10-04)
- The publisher base is concentrated: 14 publishers total; the top 3 hold 68 skills and 67.9% of installs, top 5 hold 83 skills and 84.1%, top 10 hold 96.8% — [Pro Skill Packs](https://proskillpacks.github.io/study/top-skills/) (2026-10-04)
- `mattpocock/skills` reports 55 skills and 29.5M total installs; the repo is 298,822 stars, MIT, created 2026-02-03 — [skills.sh/mattpocock](https://www.skills.sh/mattpocock/skills); [GitHub](https://github.com/mattpocock/skills)
- `obra/superpowers` reports 303,172 stars, 27,019 forks, MIT, 15 `SKILL.md` files, and ~269K skills.sh installs (~2M total installs by one tracker) — [GitHub](https://github.com/obra/superpowers/); [Open Skills](https://openskills.app/skills/superpowers)
- Anthropic's official pack (`anthropics/skills`, 182,875 stars) has install counts: `frontend-design` 1.0M, `skill-creator` 412.6K, `pptx` 240.5K, `pdf` 215.1K, `docx` 205.4K, `xlsx` 186.3K, `webapp-testing` 184.8K, `mcp-builder` 130.1K — [skills.sh/anthropics](https://www.skills.sh/anthropics/skills)
- Two of the week's most-cited design skills are proprietary-adjacent but freely installable: `frontend-design` (Anthropic) and `design-taste-frontend` from Leonxlnx/taste-skill, which ranked #2 on OpenAgentSkill's 14–20 Oct activity table with 99,450 — [OpenAgentSkill](https://www.openagentskill.com/trending) (2026-10-21)
- Weekly install volume is being driven heavily by media generation: four `magentosh/superpowers` media skills and six `heygen-com/hyperframes` video skills occupied most of the 7-day top 10, with `hyperframes-cli` at 146,752 weekly installs — [SkillSignal weekly](https://skill-signal.org/reports/trending-agent-skills-this-week) (2026-10-18)
- `find-skills` alone at ~3.9–4.0M installs is the strongest single demand signal: the top job freelancers and developers appear to need is finding and evaluating the right skill — [SkillSignal](https://skill-signal.org/reports/top-100-agent-skills); [skills.sh](https://www.skills.sh/)
- Freelancer-specific MCP coverage is real but vendor-driven: official/hosted servers now exist for Notion, Stripe, QuickBooks, Xero, HubSpot, Calendly, Slack, GitHub, and Upwork — [MyMCPTools](https://www.mymcptools.com/blog/best-mcp-servers-for-freelancers) (2026-05-05); [ChatForest](https://chatforest.com/guides/mcp-freelancers-solopreneurs-small-business/) (2026-03-30)
- Upwork publishes an official hosted MCP server at `https://mcp.upwork.com/mcp`, scored 95/100 on MartechDB's Agent Readiness Index and 1st of 6 in recruiting/freelance talent, checked 22 Oct 2026 — [MartechDB](https://martechdb.com/vendors/upwork) (2026-10-22)
- Anthropic's official plugin directory (`anthropics/claude-plugins-official`) has 43,544 stars, Apache-2.0, and lists partner plugins including GitHub, Playwright, Figma, Vercel, Supabase, Slack, Atlassian, Context7, Serena — [GitHub](https://github.com/anthropics/claude-plugins-official/); [Claude Marketplace](https://claude.com/marketplace/plugins)

### Inferences
- The "most powerful" skills for a freelancer are not the most-installed ones. Install leadership is skewed by developer process packs and viral media-generation bundles; the skills that map to billable deliverables (documents, design, research, QA) sit in the 100K–1M band.
- Because business-facing skills are only 2% of the top 100, a freelancer's back office will be assembled from MCP servers, not skills. That is a structural gap, not a temporary one.
- `find-skills` leading by ~3× the #2 entry implies the ecosystem's bottleneck is selection, not supply — consistent with independent findings that retrieval precision collapses as skill pools grow.

### Gaps
- No public data isolates freelancer/sole-trader adoption from developer adoption. All headline numbers are ecosystem-wide.
- No vendor publishes revenue, delivery hours saved, or client acceptance rates attributable to a specific skill.
- Some trackers report materially different star counts for the same repo on the same day (e.g., `anthropics/skills` at 182,875 on GitHub vs 128.1K on agskills.dev), so all star figures should be treated as ±30% approximations.

## What concrete work does each skill enable, and what is the evidence of quality?

### Takeaway
The strongest quality evidence is *process enforcement plus deterministic verification*, not popularity. Superpowers and Matt Pocock's pack encode gated workflows (spec → plan → TDD → review → handoff). Anthropic's document skills encode library choices and mandatory QA passes. Taste Skill and agent-browser ship executable checkers. The weakest evidence is for "taste" and research skills, where quality is judged by output review.

### Cited Findings
**Engineering process**
- Superpowers' mandatory loop is: `brainstorming` → `using-git-worktrees` → `writing-plans` (2–5 minute tasks with exact file paths and verification steps) → `subagent-driven-development` or `executing-plans` → `test-driven-development` (RED-GREEN-REFACTOR, deletes code written before tests) → `requesting-code-review` (critical issues block progress) → `finishing-a-development-branch` — [GitHub](https://github.com/obra/superpowers/)
- Superpowers has 37–38 contributors and shipped v7.0.1 on 21 Oct 2026, indicating active maintenance — [selan.ai](https://selan.ai/top/claude-code-skills/obra-superpowers) (2026-10-22)
- Matt Pocock's pack separates *user-invoked* orchestration skills from *model-invoked* discipline skills so the agent can auto-apply the latter; `grill-with-docs` builds a domain model/glossary and ADRs while interrogating the request; `implement-spec` builds a task graph and runs subagents across the "frontier"; `wayfinder` plans work too large for one session; `handoff` produces a transfer document — [GitHub](https://github.com/mattpocock/skills); [aihero.dev](https://www.aihero.dev/skills)
- The pack is deliberately small and composable and claims to work with any model; it is distributed as a self-updating Claude Code plugin or editable files via `npx skills add` — [GitHub](https://github.com/mattpocock/skills)
- A practitioner workflow for client projects uses the same shape: spec + acceptance tests → `CLAUDE.md`/`AGENTS.md` rules → plan per task → one branch/worktree per task → hooks run formatter/tests → reviewer subagent + second model for risky diffs → human reads every diff → staging acceptance checklist → handover of rules files — [shahidmalla.com](https://shahidmalla.com/blog/claude-code-workflow-for-client-projects) (2026-10-15)
- A consulting variant commits four files before feature work: `CLAUDE.md`, a locked `plan/*.md`, `scratch/` for load-bearing facts that survive compaction, and `.claude/settings.json` with permissions/hooks — [c0nsl.com](https://c0nsl.com/t/claude-code-consulting-workflow) (2026-05-01)

**Design**
- `frontend-design` is Anthropic-verified in the Claude Marketplace and is described as producing "production-grade frontends with distinctive design" that avoid generic AI aesthetics — [Claude Marketplace](https://claude.com/marketplace/plugins)
- Anthropic's own guidance frames skills as on-demand context loaders for design standards — [Anthropic blog](https://claude.com/blog/improving-frontend-design-through-skills) (2025-11-12, older evidence)
- Taste Skill v2 is derived from a study of 247 curated gallery sites, deals 3 of 20 researched directions via `scripts/draw.mjs`, and enforces rules with `scripts/lint.mjs` and a real-browser `scripts/inspect.mjs` that measures headline line counts, type sizes, loaded fonts, contrast, overflow at 1440/768/390 px, and saves screenshots; the agent must fix every FAIL and re-run — [tasteskill.dev](https://www.tasteskill.dev/); [SKILL.md](https://github.com/leonxlnx/taste-skill/blob/HEAD/skills/taste-skill/SKILL.md)
- Taste Skill explicitly bans LLM tells: eyebrows, monospace outside code, 01/02/03 numbering, hairline rules, gradients, glass/blur, icon-topped feature cards, three-equal-card rows, AI-purple/mesh gradients, em-dashes — [tasteskill.dev](https://www.tasteskill.dev/)
- A build is reported at roughly 30–45 minutes and a few hundred thousand tokens, requiring Node 22+ and a local Chrome/Edge/Chromium — [GitHub](https://github.com/leonxlnx/taste-skill) (2026-10-21)

**Documents and spreadsheets**
- Anthropic's document suite: DOCX uses `docx-js` to create, XML unpack/repack to edit, supports tracked changes and comments and page renders for visual check; PDF uses `pypdf`, `pdfplumber`, `reportlab` for merge/split/rotate/extract/forms/OCR; PPTX uses `pptxgenjs` plus XML editing with design guidance and a required QA pass; XLSX uses `openpyxl`/`pandas` and recalculates via headless LibreOffice so cached values are correct — [Anthropic docs](https://anthropics-skills.mintlify.app/skills/document-skills); [vibecodes.net](https://vibecodes.net/skills/document-skills)
- XLSX rules are explicit: always use Excel formulas rather than hardcoded values, zero formula errors (`#REF!`, `#DIV/0!`), blue for inputs/black for formulas, document assumptions — [Anthropic docs](https://anthropics-skills.mintlify.app/skills/document-skills)
- Observed generation times: Excel ~2 minutes with charts/formatting, PowerPoint 1–2 minutes for a simple 2-slide deck, PDF 40–60 seconds — [Claude Cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction) (2025-10-14, older evidence)
- The four document skills were substantially revised in Feb 2026 (+28,509/−9,427 across 202 files), indicating production maintenance rather than a demo — [commit 4e6907a](https://github.com/anthropics/skills/commit/4e6907a33c3c0c9ce7c1836980546aaba78a34b5) (2026-02-04)

**Browser, QA, and reverse-engineering**
- `agent-browser` is a native Rust CLI with 50+ commands, accessibility-tree snapshots with stable `@eN` refs, network control, video recording, visual diffing, sessions/profiles/auth state, and cross-platform binaries — [GitHub](https://github.com/vercel-labs/agent-browser/); [agent-browser.dev](https://agent-browser.dev/)
- It ships task-specific skills: `dogfood` (exploratory testing producing a structured report with screenshots and repro videos), `derive-client` (records HAR with response bodies, identifies real endpoints, generates a standalone client that skips the browser), `electron`, `slack`, `vercel-sandbox`, `agentcore` — [agent-browser.dev/skills](https://agent-browser.dev/skills)
- It solves skill/version drift by keeping the installed `SKILL.md` as a thin stub and serving full instructions from the installed CLI (`agent-browser skills get core`) — [agent-browser.dev/skills](https://agent-browser.dev/skills)
- Playwright MCP by Microsoft is the mainstream alternative, with 25 tools and ~6,510 tokens of tool definitions in v0.0.83 — [Voyager measurement](https://voyager.so/blog/mcp-vs-skills) (2026-10-20)

**Design handoff**
- Figma's MCP `get_design_context` returns React + Tailwind by default (framework overridable), and Code Connect injects real component imports, snippets, and team instructions into context; write-to-canvas can create frames, components, variants, variables, and auto layout — [Figma developer docs](https://developers.figma.com/docs/figma-mcp-server/); [tools reference](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/)
- Figma's own docs recommend installing Figma's skills alongside the MCP server because they make write tools more reliable — [Figma docs](https://developers.figma.com/docs/figma-mcp-server/)

**Research**
- A widely copied deep-research skill pattern decomposes a question into 3–5 sub-questions, runs 2–3 keyword variants each, targets 15–30 unique sources, deep-reads 3–5 in full, and requires a citation per claim — [ECC deep-research skill](https://github.com/affaan-m/ECC/blob/main/skills/deep-research/SKILL.md)
- Exa reports its highlights use up to 17× fewer tokens than full-page text; Firecrawl reports 7,456 median task tokens vs Exa's 22,344 on OpenBenchmarks' search-only board, and ships an opt-in `checkPromptInjection` flag — [Exa blog](https://exa.ai/blog/open-source-deep-research-agents) (2026-10-01); [Firecrawl comparison](https://www.firecrawl.dev/alternatives/firecrawl-vs-exa.md)
- Firecrawl's MCP surface covers search, scrape, map, crawl, parse (PDF/DOCX/XLSX/HTML), autonomous `firecrawl_agent`, live-page interaction, research index (PubMed/bioRxiv/medRxiv/arXiv), developer index (70M+ READMEs/issues/PRs), government index, and change monitoring — [Firecrawl docs](https://docs.firecrawl.dev/mcp-server/tools)
- Exa's Agent API prices runs from $0.012 (minimal) to $1.00 (xhigh) with a $5 default cap, giving predictable research cost — [Exa blog](https://exa.ai/blog/open-source-deep-research-agents) (2026-10-01)
- A parallel-subagent research workflow reports a 5-question session dropping from ~15 minutes sequential to ~4 minutes — [CryptoFlex](https://www.cryptoflexllc.com/blog/from-websearch-to-deep-research-adding-exa-and-firecrawl-to-claude-code) (2026-04-07)

**Client acquisition (proprietary)**
- Upwork's MCP can summarize proposals/offers/messages/contracts, search jobs and freelancers, draft a proposal grounded in profile and past work, prepare offers, manage milestones, pull timesheets, and message clients; binding actions are confirmed on upwork.com so the contract only activates after user confirmation — [MartechDB](https://martechdb.com/vendors/upwork) (2026-10-22)

### Inferences
- Deterministic verifiers are the dividing line between "prompt pack" and "tool". Skills that ship a checker (Taste Skill's inspector, XLSX's LibreOffice recalc, agent-browser's snapshots/video) are more defensible than skills that only ship prose.
- The Superpowers/Pocock approach is best understood as *process scaffolding for solo operators*: it substitutes for the missing tech lead and reviewer on a freelance engagement.
- The document skills are the single clearest freelance ROI because they convert an LLM into a file-producing tool with format-correct output, which is what clients actually accept.

### Gaps
- No independent, vendor-neutral benchmark exists for Superpowers, Matt Pocock's pack, Taste Skill, or the document skills specifically. SkillsBench evaluates curated tasks, not these named packs.
- Install counts cannot distinguish one user installing once from CI or repeated installs.
- Real client acceptance rates for AI-produced decks, docs, and sites are not published anywhere I could find.

## Which are open-source versus proprietary?

### Takeaway
The process/design layer is overwhelmingly permissive open source (MIT/Apache-2.0). The *document* layer is the big exception: source-available but proprietary, and legally unsafe to redistribute inside client repos. The tool/access layer (Figma, Exa, Upwork, HubSpot, Slack) is proprietary SaaS with free tiers, and several "free" features are explicitly beta-then-paid.

### Cited Findings
- `obra/superpowers`: MIT — [GitHub](https://github.com/obra/superpowers/)
- `mattpocock/skills`: MIT — [GitHub](https://github.com/mattpocock/skills)
- `anthropics/skills`: many skills Apache-2.0; the repo is public — [GitHub](https://github.com/anthropics/skills)
- `anthropics/claude-plugins-official`: Apache-2.0 — [GitHub](https://github.com/anthropics/claude-plugins-official/)
- `leonxlnx/taste-skill`: MIT — [DecimalAI listing](https://app.decimal.ai/skills/design-taste-frontend)
- `punkpeye/awesome-mcp-servers`: MIT — [GitHub](https://github.com/punkpeye/awesome-mcp-servers/)
- Anthropic's `docx`, `pdf`, `pptx`, `xlsx` are **source-available, not open source**: "These are source-available, not open source"; the licence restricts copying outside Anthropic's services and forbids derivative works/redistribution — [GitHub](https://github.com/anthropics/skills); [vibecodes.net](https://vibecodes.net/skills/document-skills)
- The `skills` CLI and skills.sh registry are open source at `vercel-labs/skills` — [skills.sh/docs](https://www.skills.sh/docs)
- The Agent Skills format is an open standard, originally developed by Anthropic and published at agentskills.io — [agentskills.io](https://agentskills.io/home)
- The MCP Skills extension (SEP-2640) reached Final status and was merged 13 Sep 2026; the extension and registry are permissively licensed/open — [MCP docs](https://modelcontextprotocol.io/extensions/skills/overview); [SEP-2640](https://modelcontextprotocol.io/seps/2640-skills-extension)
- Figma MCP: remote server is free during beta and "will eventually become a usage-based paid feature"; writing outside drafts requires a Full seat — [Figma docs](https://developers.figma.com/docs/figma-mcp-server/)
- Exa is a proprietary platform with no self-hosting option; Firecrawl is open source and self-hostable, with a paid cloud API — [Firecrawl comparison](https://www.firecrawl.dev/alternatives/firecrawl-vs-exa.md)
- Upwork's MCP is official but hosted and account-gated — [MartechDB](https://martechdb.com/vendors/upwork)
- MCP servers vary: GitHub, Playwright, Supabase, Notion, Atlassian, Linear, Asana, Slack, Sentry and Figma all publish official servers; Serena and Postgres MCP Pro are "community standard" — [MCP.so](https://mcp.so/blog/best-mcp-servers) (2026-10-15)

### Inferences
- A freelancer can build an entirely open-source delivery stack from Superpowers/Pocock + Taste Skill + agent-browser + Firecrawl self-hosted + Playwright MCP. The one thing they cannot legally vendor is the document layer, which is also the highest-ROI layer for non-coding work.
- The document licence means agencies cannot ship a "documents capability" to a client repo or bundle it into a paid template. They must depend on Anthropic's runtime or rebuild equivalents.
- "Free during beta" on Figma write-to-canvas is a pricing risk to flag in fixed-price quotes.

### Gaps
- Licence text for individual third-party skills is inconsistent; many list no licence in the repo at all (Pro Skill Packs found only 69% of MCP entries had licence info in one dataset).
- No source confirms whether Anthropic intends to open the document skills.
- Unclear whether MCP-hosted skills inherit the server's licence or the skill author's.

## Which GitHub repositories, marketplaces, and registries are most important?

### Takeaway
Four layers matter: (1) skills.sh as the de facto install registry; (2) a handful of GitHub repos that are the actual source of truth; (3) Anthropic's Claude Code marketplaces plus the web directory; (4) the official MCP Registry and agentskills.io as the standards layer. Everything else is discovery/SEO noise.

### Cited Findings
**Registries and marketplaces**
- **skills.sh** (Vercel Labs) is the dominant skills registry: browse leaderboard, install with `npx skills add owner/repo`, packs, badges, anonymous telemetry, routine security audits but explicitly "we cannot guarantee the quality or security of every skill listed" — [skills.sh/docs](https://www.skills.sh/docs)
- **Claude Code marketplaces**: official `claude-plugins-official` (auto-added on first interactive session), community `claude-community` (repo `anthropics/claude-plugins-community`), demo `claude-code-plugins` (repo `anthropics/claude-code`); install with `/plugin install name@marketplace`. Most official-marketplace listings come from partners, not Anthropic — [Claude Code docs](https://code.claude.com/docs/en/plugins/anthropic-marketplaces)
- **Claude Marketplace** (web) is the browsable catalog with install counts and "Anthropic verified" badges; it is separate from the plugin marketplaces and syncs to Claude Code via account — [claude.com/marketplace/plugins](https://claude.com/marketplace/plugins); [publish docs](https://code.claude.com/docs/en/plugins/publish)
- Anthropic also publishes topic marketplaces including `anthropics/skills` and `anthropics/knowledge-work-plugins`, added with `/plugin marketplace add owner/repo` — [Claude Code docs](https://code.claude.com/docs/en/plugins/anthropic-marketplaces)
- **Official MCP Registry** at `registry.modelcontextprotocol.io` launched in preview on 8 Sep 2025 as the single upstream source of truth, open source, with public and private sub-registries and community denylisting — [MCP blog](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/) (older: 2025-09-08)
- **agentskills.io** hosts the open Agent Skills spec, client showcase, and progressive-disclosure model; Cloudflare proposed `.well-known/skills` URL-based discovery, which Vercel implemented in `npx skills` — [agentskills.io](https://agentskills.io/home); [Vercel case study](https://claude.com/customers/vercel-qa)
- MCP Skills extension (`io.modelcontextprotocol/skills`) is Final, with `skills/list`, `skills/get`, and `resources/read`; SDK/host support is still rolling out — [MCP docs](https://modelcontextprotocol.io/extensions/skills/overview)

**Repositories (GitHub, 22 Oct 2026 unless noted)**
| Repo | Stars | Licence | Why it matters |
|---|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers/) | 303,172 | MIT | Most-starred skills framework; full SDLC method |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 298,822 | MIT | Most-used engineering skill pack; 55 skills |
| [anthropics/skills](https://github.com/anthropics/skills) | 182,875 | Apache-2.0 + proprietary docs | Canonical reference implementations |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/) | ~1.2M installs | — | Browser CLI + task skills |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official/) | 43,544 | Apache-2.0 | Official plugin catalog |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers/) | 96,747 | MIT | Largest MCP discovery list (1,631 servers in one derived dataset) |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | ~89,611 (Aug 2026) | — | Reference servers: Filesystem, Memory, Sequential Thinking, Fetch, Git, Time |
| [openai/skills](https://www.skills.sh/openai/skills) | ~13.3K installs (pdf) | — | Codex-side official skills: pdf, playwright, figma, deploy, security |
| [leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill) | — | MIT | Anti-slop design skill with browser verification |
| [heygen-com/hyperframes](https://www.skills.sh/) | — | — | HTML→MP4 video; dominant weekly install growth |

**Secondary discovery/analytics layer** (useful for signal, not authority)
- SkillSignal, Edge, OpenAgentSkill, agskills.dev, gitcodar, gitnova, Open Skills, DecimalAI, aiagents.org.uk, topaiskills, distilledbrew. Several mix real telemetry with unverifiable editorial claims; treat as a shortlist generator only — [SkillSignal](https://skill-signal.org/reports/top-100-agent-skills); [Edge](https://getedge.cc/trending/); [OpenAgentSkill](https://www.openagentskill.com/trending)
- Vendor docs are the most reliable source for install commands and current tool surfaces: [Claude Code plugins](https://code.claude.com/docs/en/plugins/install), [Vercel agent resources](https://vercel.com/docs/agent-resources/skills), [Figma](https://developers.figma.com/docs/figma-mcp-server/), [Firecrawl](https://docs.firecrawl.dev/mcp-server/tools), [Exa](https://exa.ai/blog/open-source-deep-research-agents)

### Inferences
- For a freelancer, the practical hierarchy is: skills.sh to discover → GitHub to audit → vendor docs to install → `/context` to verify what actually loaded. Marketplaces are convenience, not trust.
- Anthropic's official marketplace is now the highest-signal curated channel because partner listings are vendor-maintained and Anthropic marks some as verified; skills.sh is the highest-volume channel but explicitly disclaims security.
- The standards layer (agentskills.io + SEP-2640 + MCP Registry) matters strategically: skills are becoming portable across Claude Code, Codex, Cursor, Copilot, Gemini CLI, and OpenCode, which reduces lock-in.

### Gaps
- No public ranking of registries by install volume other than skills.sh's own telemetry.
- Star counts conflict across aggregators and over time (see Q1 gap); the table above mixes direct GitHub reads with older readings and should be treated as directional.
- MCP Registry GA status and total server count as of Oct 2026 were not confirmed; the preview post is from Sep 2025.
- ClawHub/OpenClaw is repeatedly named in security research as a major marketplace, but I did not verify its current size or whether it is still active in Oct 2026.

## Which skills combine well into a reliable freelance stack?

### Takeaway
The reliable pattern is one process pack + one document pack + one browser/verifier + a small number of scoped MCP servers. Do not stack two process packs or two browser stacks. Add business MCPs read-only first. The strongest published freelancer stacks converge on Notion + Stripe as the admin core, GitHub/Playwright/Context7 as the dev core, and Slack + a search server for communication and research.

### Cited Findings
**Published starter stacks**
- Freelancer MCP starter stack, in priority order: Notion + Stripe first; then GitHub (technical) or HubSpot (business development); then Calendly + Resend for outreach/scheduling; then QuickBooks or Xero at volume — [MyMCPTools](https://www.mymcptools.com/blog/best-mcp-servers-for-freelancers) (2026-05-05)
- Solo-freelancer MCP trio: accounting (QuickBooks/Xero official), time tracking (Toggl/Clockify), scheduling (Calendly official hosted) — [ChatForest](https://chatforest.com/guides/mcp-freelancers-solopreneurs-small-business/) (2026-03-30)
- Solo-developer stack: GitHub + Context7 + Playwright + one database in restricted mode; add Linear/Atlassian, Sentry, Figma for product teams; Exa/Firecrawl + Notion + DeepWiki for research/content — [MCP.so](https://mcp.so/blog/best-mcp-servers) (2026-10-15)
- Keep three to six servers, because every server adds tool descriptions to context and every write-capable server widens prompt-injection reach — [MCP.so](https://mcp.so/blog/best-mcp-servers)
- Practitioner four-stage delivery: spec → worktree per task → subagent with one task per context window → two-stage review (spec compliance, then quality/YAGNI), with a second model (e.g., Copilot) as reviewer — [valpere.github.io](https://valpere.github.io/blog/2026/04/01/claude-code-freelance-workflow/) (2026-04-01)
- Freelance onboarding automation: three inputs (client name, industry, project type) produce proposal, contract prefill, project brief, and Notion workspace in ~10 minutes vs 2–3 hours; monthly reporting and invoicing drop to under 20 minutes — [alejandroarce.com](https://alejandroarce.com/blog/claude-code-freelancer-workflow/) (2026-06-05)
- A public freelancer workspace template structures `.claude/commands/` (`/proposal-draft`, `/scope-of-work`, `/invoice-chase`, `/status-report`, `/client-onboard`, `/new-business`, `/weekly-wrap`) over per-client folders containing brief, contract, SOW, onboarding checklist, status log, comms log, deliverables, invoices — [Claudient freelancer-workspace](https://github.com/Claudient/Claudient/blob/main/structures/freelancer-workspace.md)
- A companion `freelance-studio` structure adds `/scope-of-work` and `/feedback-request` per milestone — [Claudient freelance-studio](https://github.com/Claudient/Claudient/blob/main/structures/freelance-studio.md)

**Recommended combination logic**
- Skill = procedure; MCP = access; CLI = lightest access when a good CLI exists; subagent = isolation. Default to trying a skill first and a subagent last — [agentic-ai-system-course](https://github.com/bryanyzhu/agentic-ai-system-course/blob/main/course/14-skills-mcp-subagents.md)
- Skills fail like "a vague brief handed to a new hire"; MCP fails like a compiler — loud and specific. Use MCP for stateful/external actions, skills for judgment — [decodo.com](https://decodo.com/blog/claude-skills-vs-mcp)

**Concrete freelance stack (synthesis, not a single source)**
1. **Meta**: `find-skills` (discovery) + `skill-creator` (turn your own repeatable process into a skill).
2. **Process (pick one)**: `obra/superpowers` (fullest SDLC, heavier) *or* `mattpocock/skills` (lighter, composable, 55 skills). Never both — duplicate triggers and double context.
3. **Deliverables**: `docx`, `pdf`, `pptx`, `xlsx` for reports, proposals, decks, models; `frontend-design` for web work.
4. **Design polish**: `design-taste-frontend` (Taste Skill) for art direction + pre-flight gate; Figma MCP when the client supplies designs.
5. **Verify**: `agent-browser` (dogfood/derive-client) or Playwright MCP + `webapp-testing`; add Chrome DevTools MCP only when debugging.
6. **Research**: Exa MCP (semantic, cheap highlights) + Firecrawl MCP (JS pages, PDFs, crawling) behind a `deep-research` skill with citation rules.
7. **Ops/access (read-only first)**: Notion, GitHub, Slack, Stripe; then HubSpot/Calendly/Resend; QuickBooks/Xero at volume.
8. **Pipeline (later)**: Upwork MCP for job search and proposal drafts.
9. **Deploy**: Vercel/Netlify/Cloudflare deploy skills (available in `openai/skills` and partner plugins) — [skills.sh/openai](https://www.skills.sh/openai/skills)

### Inferences
- The highest-reliability stack is deliberately small: two or three skills per job, one process pack, 3–6 MCP servers. Every additional overlapping skill raises trigger ambiguity and the "regression tax".
- For non-coding freelancers, the center of gravity shifts: document skills + research MCP + browser verification + Notion/Stripe, with no process pack at all.
- For coding freelancers, Superpowers or Pocock + GitHub + Playwright + Sentry is the closest thing to a professional delivery system that substitutes for a team.

### Gaps
- No controlled comparison of "Superpowers vs Pocock vs no pack" on freelance delivery outcomes.
- The Claudient templates are community artifacts with no adoption data; they illustrate structure, not proven results.
- No source quantifies how often stacking multiple packs causes trigger collisions in practice.

## What are the limitations, security risks, and failure modes?

### Takeaway
The ecosystem has a measured, severe supply-chain problem: roughly a quarter of skills contain at least one vulnerability, malicious skills are confirmed in the wild, and popularity is not a safety signal. Separately, skills often simply fail to fire, and when they do fire they can regress tasks they were not meant to touch. Treat skills as executable third-party code with prompt-injection surface, not as documentation.

### Cited Findings
**Supply chain and malicious skills**
- Large-scale study of 42,447 skills (31,132 analyzed with SkillScan): 26.1% contain at least one vulnerability across 14 patterns in four categories (prompt injection, data exfiltration, privilege escalation, supply chain); data exfiltration 13.3%, privilege escalation 11.8%, 5.2% high-severity strongly suggesting malicious intent; skills bundling executable scripts are 2.12× more likely to be vulnerable (OR=2.12, p<0.001) — [arXiv 2601.10338](https://arxiv.org/abs/2601.10338)
- Snyk analyzed 3,984 skills from ClawHub and skills.sh: 76 confirmed malicious payloads (credential theft, backdoor installation, data exfiltration), 13.4% (534) with at least one Critical issue, 36.82% (1,467) with at least one issue of any severity; at least 8 confirmed malicious skills remained installable at publication — [Snyk research](https://research.snyk.io/blog/agent-skills-threat-landscape/) (2026-02-05)
- 100% of confirmed malicious skills contained malicious code patterns and 91% also used prompt injection; 17.7% of ClawHub skills and 9% of the skills.sh top 100 fetch untrusted third-party content; 2.9% of ClawHub skills use unverifiable remote dependencies (21% of malicious samples) — [Snyk](https://research.snyk.io/blog/agent-skills-threat-landscape/)
- A separate study of 98,380 skills found 157 confirmed malicious skills with 632 vulnerabilities across 13 attack techniques, averaging 4.03 vulnerabilities per malicious skill; over half came from one threat actor using templated brand impersonation; all 157 were removed after disclosure — [arXiv 2602.06547](https://arxiv.org/html/2602.06547v3)
- The ClawHavoc campaign (Jan–Feb 2026) published hundreds of malicious skills to the OpenClaw marketplace, distributing the AMOS credential stealer; Koi Security counted 341 malicious of 2,857 listed, then 824 as the marketplace passed 10,700; Antiy CERT counted 1,184 malicious packages historically — [arXiv 2603.00195](https://arxiv.org/html/2603.00195v2); [CSA research note](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-skill-supply-chain-attacks-20260624-csa/) (2026-06-24)
- CVE-2026-25253 was a one-click RCE in OpenClaw reached through auth-token exfiltration — one of the first CVEs assigned to an agentic AI system — [arXiv 2603.00195](https://arxiv.org/html/2603.00195v2)
- Payload-less attacks work: "Semantic Compliance Hijacking" encodes malicious behavior as natural-language compliance rules and reports up to 77.67% exfiltration and 67.33% RCE at 0.00% scanner detection; metadata-only attacks manipulate discovery at an 86% pairwise win rate, bias agent selection 77.6% of the time, and evade governance classifiers in 36.5–100% of cases — [CSA research note](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-skill-supply-chain-attacks-20260624-csa/) (2026-06-24)
- MCP tool poisoning (CVE-2025-54136) shows attacker-controlled tool descriptions load verbatim into context and function as instructions regardless of code-level controls — [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-skill-supply-chain-attacks-20260624-csa/)
- Anthropic and GitHub both warn that community skills are unverified and may contain malicious scripts or hidden instructions; GitHub specifically warns against pre-approving shell access without reviewing the skill and its referenced files — [Jason Doyle whitepaper](https://jasondoyle.ie/whitepapers/when-you-need-an-mcp-server/) (2026-08-27)
- Marketplaces disclaim responsibility: skills.sh says it audits but "cannot guarantee the quality or security of every skill"; Anthropic's plugin directory says it "does not control what MCP servers, files, or other software are included in plugins" — [skills.sh/docs](https://www.skills.sh/docs); [claude-plugins-official](https://github.com/anthropics/claude-plugins-official/)

**Efficacy and reliability**
- SkillsBench: curated skills raise average pass rate from 33.9% to 50.5% (+16.6 pp, 25.5% normalized gain) across 18 model–harness configurations, range +4.1 to +25.7 pp; focused skills with ≤3 modules outperform larger/exhaustive bundles; smaller models with skills can match larger models without — [arXiv 2602.12670](https://arxiv.org/abs/2602.12670)
- A different SkillsBench revision (86 tasks, 7 configs, 7,308 trajectories) found +16.2 pp average, +4.5 pp for software engineering vs +51.9 pp for healthcare, 16 of 84 tasks with negative deltas, and self-generated skills providing **no** average benefit (−1.3 pp) — [SkillsBench PDF](https://yubol-bobo.github.io/assets/pdf/SkillsBench.pdf)
- In realistic conditions with 34K skills to retrieve from, "the benefits of skills are fragile" and pass rates approach no-skill baselines; two bottlenecks are choosing which skill to load and noisy/insufficient skill content; query-specific refinement recovers much of the loss (Claude 40.1%→48.2%) and lifts Terminal-Bench 2.0 from 57.7% to 65.5% — [arXiv 2604.04323](https://arxiv.org/html/2604.04323v1)
- Retrieval precision collapses as the pool grows: actual-use precision falls from 29.6% at 5 candidates to 3.3% at 100; procedural anchoring accounts for 65.7% of skill benefit vs 4.5% for explicit knowledge injection — [arXiv 2608.14036](https://arxiv.org/html/2608.14036) (2026-08-14)
- The "regression tax": across 5,832 runs, 553 gain transitions were offset by 324 regressions (59% of gross gains cancelled); no library condition had zero regressions; causes include skill-description osmosis (a skill changes behavior just by being present), grounding displacement, and verification displacement — [arXiv 2607.22520](https://arxiv.org/abs/2607.22520)
- Vercel's Next.js 16 evals: a documentation skill was never invoked in 56% of cases and scored the same 53% as no documentation; explicit instructions to use it raised this to 79%; a compressed 8 KB documentation index in `AGENTS.md` scored 100%. Vercel's conclusion: skills suit specific user-triggered workflows, while always-needed knowledge belongs in the instructions file — [Voyager](https://voyager.so/blog/mcp-vs-skills) (2026-10-20, reporting Vercel's Jan 2026 eval)

**Cost and context**
- GitHub MCP v2.0.2 with all toolsets: 91 tools, 40,117 tokens of definitions (1,227 deferred); default toolsets 46 tools/19,150 tokens. Notion's older self-hosted server: 24 tools/33,274 tokens (~1,386 tokens per tool). Playwright MCP: 25 tools/6,510. Context7: 2 tools/1,711. Chrome DevTools MCP: 32 tools/10,685, or 325 with `--slim` — [Voyager](https://voyager.so/blog/mcp-vs-skills) (2026-10-20)
- Skills are cheap when idle, expensive when used: median skill listing is ~100 tokens, median full `SKILL.md` ~3,226 tokens; Playwright CLI skill is 29 tokens idle / 5,896 activated; all 19 Anthropic skills together cost 3,215 tokens of listings — [Voyager](https://voyager.so/blog/mcp-vs-skills)
- Clients cap skill listings: Codex limits the startup list to 2% of the context window; Claude Code budgets 1% and drops descriptions of least-used skills when the listing overflows; after compaction Claude Code keeps only the first 5,000 tokens of each recent skill within a 25,000-token total — [Voyager](https://voyager.so/blog/mcp-vs-skills)
- Deferred MCP tool loading became Claude Code's default on 12 March 2026; Cursor's A/B test cut total agent tokens 46.9%; Codex always defers when `tool_search` is available — [Voyager](https://voyager.so/blog/mcp-vs-skills)
- Skills fail quietly — skipped steps, misapplied rules, plausible-but-wrong output — whereas MCP fails loudly with schema errors — [decodo.com](https://decodo.com/blog/claude-skills-vs-mcp)

**Freelance-specific risk**
- Client data obligations: running client financial data through AI agents may require consent depending on jurisdiction and contract; use restricted read-only keys and separate sessions per client — [ChatForest](https://chatforest.com/guides/mcp-freelancers-solopreneurs-small-business/) (2026-03-30)
- Secrets and production access: deny rules for `.env`, least-privilege allow lists, no production credentials in the agent, dependency and licence checks before merge, anonymized data only — [shahidmalla.com](https://shahidmalla.com/blog/claude-code-workflow-for-client-projects) (2026-10-15)
- The document skills' proprietary licence restricts redistribution, which matters when handing a repo to a client — [vibecodes.net](https://vibecodes.net/skills/document-skills)

### Inferences
- For a freelancer, the practical threat model is not "nation-state malware" but (a) a typo-squatted or impersonating skill stealing API keys/credentials, (b) a legitimately useful skill that fetches untrusted content and gets indirectly injected, and (c) a skill silently steering output in a way that embarrasses you in front of a client.
- Because regression tax is real, adding skills is not monotonically good. A freelancer should measure per-client/per-project lift, not accumulate packs.
- The 56% non-invocation finding is the single most under-appreciated failure: your expensive skill may simply never load. Explicit slash invocation and a small always-on `AGENTS.md`/`CLAUDE.md` are the mitigations.
- Context cost is now a configuration problem more than a protocol problem, but the freelancer still pays in latency and in degraded attention when 40K tokens of GitHub tool definitions sit in the window.

### Gaps
- Security studies use different corpora and dates (42,447 vs 98,380 vs 3,984 skills), so percentages are not directly comparable.
- No study isolates freelance/client-data scenarios specifically.
- No public incident data on client confidentiality breaches caused by agent skills.
- Whether Claude Code/Codex/Cursor enforce per-skill permission manifests in Oct 2026 is unclear; the research recommends capability-based permissions, implying they are not standard.
- Vercel's eval is reported secondhand; I did not read the primary Vercel post.

## What should a freelancer learn or install first versus later?

### Takeaway
Install the *minimum viable delivery loop* first: discovery + your own process + document output + a browser verifier + one or two scoped MCP servers. Add design, research, and business ops only after the loop is reliable. The human skills — scoping, acceptance criteria, diff review, client communication — matter more than any additional skill and cannot be installed.

### Cited Findings
**Sequencing evidence**
- SkillsBench finds focused skills with ≤3 modules outperform larger bundles, and self-generated skills provide no average benefit — so curation and restraint beat volume — [arXiv 2602.12670](https://arxiv.org/abs/2602.12670); [SkillsBench PDF](https://yubol-bobo.github.io/assets/pdf/SkillsBench.pdf)
- Realistic-retrieval research finds agents struggle to choose which skill to load and that content is often too noisy; explicit, narrow descriptions and query-specific refinement help — [arXiv 2604.04323](https://arxiv.org/html/2604.04323v1)
- Vercel's eval implies a split: user-triggered workflows → skills; knowledge needed on every task → `AGENTS.md`/`CLAUDE.md` — [Voyager](https://voyager.so/blog/mcp-vs-skills)
- MCP guidance: prefer official servers, start read-only, keep to 3–6 servers, disable unused ones, and review before connecting anything with write access — [MCP.so](https://mcp.so/blog/best-mcp-servers); [ChatForest](https://chatforest.com/guides/mcp-freelancers-solopreneurs-small-business/)
- Upwork-specific advice: use the agent to scope the job before bidding, build in small reviewable tasks, run/test the result yourself, and price fixed-fee rather than hourly so speed becomes income rather than a discount — [Upwork Income Club](https://www.upworkincomeclub.com/blog/claude-code-for-upwork-freelancers) (2026-08-07)
- Practitioner consensus on what stays human: discovery calls, strategic decisions, final QC, relationship management — [alejandroarce.com](https://alejandroarce.com/blog/claude-code-freelancer-workflow/) (2026-06-05)
- Handoff is routinely underinvested; generating README, architecture overview, maintenance tasks, and "how to add a feature" instructions reduces post-project support and drives referrals — [phosailabs.com](https://phosailabs.com/blog/claude-code-freelance-developer-workflow) (2026-04-21)

**Recommended sequence (synthesis)**
- **First 2 hours — the delivery loop**
  1. `find-skills` — learn to search before installing.
  2. `skill-creator` — capture one repeated process of your own (e.g., "client status report").
  3. Document pack: `docx`, `pdf`, `pptx`, `xlsx` — immediate client-facing output.
  4. One browser skill: `agent-browser` (or Playwright MCP) — verify what you ship.
  5. One scoped MCP: GitHub if you code, Notion if you don't. Read-only where possible.
  6. Learn the mechanics: project vs global install scope, reading `SKILL.md` before install, pinning versions, `/context` to see what loaded, explicit `/skill-name` invocation.
- **First month — quality and range**
  7. One process pack: `obra/superpowers` (thorough) or `mattpocock/skills` (lighter). Not both.
  8. Design: `frontend-design`, then `design-taste-frontend`; add Figma MCP only when a client supplies Figma files.
  9. Research: Exa MCP + Firecrawl MCP behind a `deep-research` skill that requires a citation per claim.
  10. Comms/ops: Slack, Calendly, Resend; Stripe read-only.
  11. Deployment: Vercel/Netlify/Cloudflare deploy skill; Sentry if you maintain client apps.
- **Later — leverage and scale**
  12. Upwork MCP for pipeline and proposal drafting (review every draft; platform rules apply).
  13. HubSpot/CRM and accounting (QuickBooks/Xero) once volume justifies it.
  14. Custom client-specific skills and a private marketplace/monorepo of `SKILL.md` files.
  15. Subagent orchestration (`subagent-driven-development`, `dispatching-parallel-agents`) and worktree isolation.
  16. Memory/knowledge-graph tooling and multi-model review (e.g., second-model diff review).

**What to learn (human, not installable)**
- Scoping and fixed-price estimation from a real look at client files, not from the job post.
- Writing acceptance criteria and a locked SOW with explicit out-of-scope.
- Reading diffs and explaining generated code to a client.
- Security review of skills: read `SKILL.md`, list bundled scripts, check network calls, check dependencies, check licence, check maintainer and release cadence.
- Prompt/context engineering: writing descriptions as triggers, keeping always-needed rules in `AGENTS.md`.
- Basic eval design: run the same task with and without the skill, count tool calls/tokens, and record regressions.

### Inferences
- The correct first purchase is not a bundle; it is literacy. A freelancer who can read a `SKILL.md`, audit a script, and measure a regression will outperform one who installs the top 50.
- Document skills should come before coding process packs for the majority of freelancers (designers, marketers, consultants, ops), because those clients buy files, not commits.
- Upwork MCP is genuinely high-leverage but should come later, because automating proposals before you have a repeatable delivery loop just scales bad proposals.
- The 3–6 MCP ceiling and the "focused skills win" finding point to the same discipline: curate per engagement, not per career.

### Gaps
- No published learning curve or time-to-competence data for agent skills.
- No evidence on whether Upwork MCP use affects proposal win rates or violates platform automation rules; I found no official Upwork policy statement.
- No data on which freelancer verticals (design vs dev vs writing vs consulting) adopt which skills at what rate.
- Unclear how durable these specific packs will be; star growth is steep but several 2026 leaders appeared within months, and "fast risers fade fast" was already observed week-over-week.
