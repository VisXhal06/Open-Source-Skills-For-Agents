---
title: OpenCode Skills
aliases:
  - Skills Guide
  - Agent Skills
type: reference
created: 2026-10-20
updated: 2026-11-03
tags:
  - opencode
  - skills
  - ai-workflow
  - reference
---

# OpenCode Skills

> [!info] What this is
> A complete reference for the **94 agent skills** installed globally in `~/.agents/skills`. Every project on this machine can use them. This note explains what each skill does, when to reach for it, and what to say.

> [!tip] The one rule
> Skills load automatically when your request matches their description. To be certain, name the skill: **"Use the `<skill-name>` skill to …"**

## How skills work

A skill is a folder containing a `SKILL.md` file. The file has YAML frontmatter with a `name` and `description`, followed by instructions. Some skills also ship scripts, references, or assets.

OpenCode reads every skill's **name and description** at the start of a session. The full instructions load only when the skill is selected. That keeps the context small until a skill is needed.

Skills are instructions, not separate programs. Once loaded, they use the agent's normal tools: read files, run commands, edit code, search the web.

### Three ways to invoke a skill

| Method | Example | Reliability |
| --- | --- | --- |
| Name it | "Use the `systematic-debugging` skill on this failure." | Highest |
| Describe the task | "This test fails intermittently. Find the root cause." | Automatic routing |
| Trigger phrase | "grill me", "caveman mode", "handoff", "stop slop" | Skill-specific |

### See what is installed

```powershell
npx skills ls -g -a opencode
```

Or ask the agent: *"List your available skills."*

## Category index

- [[#Planning and development]] — 15 skills
- [[#Senior-dev guardrails]] - 3 skills
- [[#Build and ship]] - 1 skill
- [[#Frontend and design]] - 5 skills
- [[#Design engineering]] — 8 skills
- [[#Cloudflare]] — 6 skills
- [[#Research and web]] — 8 skills
- [[#Codebase understanding]] — 5 skills
- [[#Open source contribution]] — 11 skills
- [[#AI engineering]] — 1 skill
- [[#Reverse engineering]] — 2 skills
- [[#Writing and sessions]] — 4 skills
- [[#Skill building and testing]] — 4 skills
- [[#Knowledge and notes]] — 1 skill
- [[#Integrations]] — 5 skills
- [[#Engineering leadership]] — 7 skills
- [[#Freelancing and client work]] — 5 skills
- [[#Goals, advice, and orchestration]] — 3 skills

---

## Planning and development

The Superpowers set. Use these as a chain, not as isolated tricks.

### using-superpowers

**What:** Session bootstrap. Checks whether any skill applies before answering, even on a slim chance, and routes into the right workflow.
**Use when:** Starting a session, or when you are unsure which skill fits.
**Try:** `"Use using-superpowers to pick the right workflow for this task."`

### brainstorming

**What:** A structured interview that turns a vague idea into a real specification. One question at a time, resolving each branch of the design tree.
**Use when:** Before any creative work: a feature, component, product, talk, business, or renovation.
**Try:** `"Use brainstorming to design a subscription billing system."`

### writing-plans

**What:** Converts a spec into a phased implementation plan with files, tests, checkpoints, and 2–5 minute tasks.
**Use when:** You have requirements for a multi-step task and have not touched code yet.
**Try:** `"Turn this spec into an implementation plan."`

### executing-plans

**What:** Executes a plan inline, step by step, verifying each checkpoint instead of racing to the end.
**Use when:** A plan exists and you are the implementer in this session.
**Try:** `"Execute docs/plan.md and stop at each checkpoint."`

### subagent-driven-development

**What:** Splits independent plan tasks across subagents, then runs two-stage review on their work.
**Use when:** The plan has independent tasks and the harness supports subagents.
**Try:** `"Run this plan with subagent-driven development."`

### test-driven-development

**What:** Enforces red → green → refactor. Write a failing test first, make it pass, then clean up.
**Use when:** Implementing any feature or bug fix, before writing implementation code.
**Try:** `"Implement this endpoint using TDD."`

### systematic-debugging

**What:** Root cause before fixes. Reproduce, isolate, form a hypothesis, test it, then patch.
**Use when:** Any bug, failing test, or unexpected behavior, before proposing a fix.
**Try:** `"This test fails intermittently. Debug it systematically."`

### verification-before-completion

**What:** No success claim without fresh evidence. Runs the verification commands and shows the output.
**Use when:** About to say work is complete, fixed, or passing; before commit or PR.
**Try:** `"Verify everything before you say it's done."`

### requesting-code-review

**What:** Reviews your own diff against the requirements before merge, looking for gaps and regressions.
**Use when:** Finishing a task, a major feature, or preparing to merge.
**Try:** `"Request a code review of this branch before I merge."`

### receiving-code-review

**What:** Evaluates review feedback with technical rigor instead of blind agreement. Verifies each claim.
**Use when:** You receive review comments, especially unclear or questionable ones.
**Try:** Paste the feedback, then: `"Evaluate this review before applying it."`

### dispatching-parallel-agents

**What:** Splits independent work across parallel agents without shared state or ordering problems.
**Use when:** Two or more tasks can run independently.
**Try:** `"Split these three independent fixes across parallel agents."`

### using-git-worktrees

**What:** Creates an isolated workspace via native tools or a Git worktree fallback.
**Use when:** Starting feature work that should not disturb the current workspace, or before executing a plan.
**Try:** `"Create an isolated worktree for this feature."`

### finishing-a-development-branch

**What:** Decides how to integrate finished work: merge, rebase, PR, or clean up.
**Use when:** Implementation is complete and tests pass.
**Try:** `"Finish this development branch and tell me the integration options."`

### writing-skills

**What:** Creates, edits, and verifies skills, including how to test that a skill actually triggers.
**Use when:** Turning a repeated workflow into a reusable skill.
**Try:** `"Turn this release checklist into a skill."`

### diagnosing-superpowers

**What:** Diagnoses a Superpowers session that went wrong: repeated work, ignored plans, a skill that did not fire, slow or expensive runs.
**Use when:** The workflow misbehaved and you want the cause, not a guess.
**Try:** `"Diagnose why this session ignored the plan."`

---

## Senior-dev guardrails

Three skills that prevent expensive mistakes before and after coding.

### ask-questions-if-underspecified

**What:** Asks 1–5 must-have questions when a request has multiple plausible readings, offers defaults, and pauses before acting.
**Use when:** Objective, scope, constraints, environment, or safety are unclear and guessing would risk wrong work.
**Try:** `"Ask me what you need before starting."`

### implementation-strategy

**What:** Defines the supported behavior and compatibility boundary before editing runtime code, public APIs, schemas, protocols, or migrations. Includes a complexity-reset procedure when review feedback keeps widening the patch.
**Use when:** A change may affect released behavior, durable formats, serialized state, or which inputs are supported.
**Try:** `"We're changing a public API. Set the compatibility boundary first."`

### code-change-verification

**What:** Discovers the repository's real verification stack from `AGENTS.md`, CI config, `Makefile`, `package.json`, `pyproject.toml`, and runs format → lint → typecheck → build → tests. Reports exact commands and results.
**Use when:** Before claiming work is complete, committing, or opening a PR, and whenever runtime code or build config changes.
**Try:** `"Run the full verification stack and show me the output."`

---

## Frontend and design

### frontend-design

**What:** Forces an explicit aesthetic direction before writing UI and enforces the anti-generic gate: no default type stacks, purple-on-white gradients, template heroes, identical cards, or cookie-cutter component kits. Type, palette, layout, and motion each need a subject-specific rationale.
**Use when:** Building or reshaping a UI and the default output looks generic.
**Try:** `"Redesign this onboarding page with a deliberate visual direction."`

### vercel-react-best-practices

**What:** Vercel Engineering's React and Next.js performance rules, prioritized by impact: waterfalls, bundle size, RSC boundaries, memoization, re-renders.
**Use when:** Writing, reviewing, or refactoring React or Next.js code.
**Try:** `"Review this Next.js page for performance."`

### vercel-composition-patterns

**What:** React composition patterns that scale: compound components, context interfaces, children over render props, avoiding boolean prop sprawl. Includes React 19 changes.
**Use when:** Designing reusable component APIs or refactoring a component library.
**Try:** `"Refactor this component API to remove boolean props."`

### web-design-guidelines

**What:** Audits UI code against the Web Interface Guidelines and an anti-generic gate: accessibility, interaction, layout, type, color, and UX best practices.
**Use when:** Asked to review a UI, check accessibility, or audit a design.
**Try:** `"Audit this UI for accessibility and UX."`

### web-perf

**What:** Audits and diagnoses loading and interaction performance: Core Web Vitals, Lighthouse, and the changes that actually move the numbers.
**Use when:** A site feels slow or a performance score needs improving.
**Try:** `"Why is my LCP bad? Audit this page."`

---

## Design engineering

The design-engineering suite. `design-engineering` is the front door: it loads the smallest useful set of sub-skills automatically, and every sub-skill is also directly accessible. It covers product design, UI/UX, visual design, interaction and motion, design systems, frontend craft, AI-assisted design, and critique. The full role map, suite workflow, and source list are in [[Design Engineering Skills]]. You can also use the `/design` command.

> [!warning] Anti-generic gate
> All 11 frontend and design skills reject generic AI defaults: Inter, Roboto, Arial,
> Helvetica, system stacks, violet-on-white gradients, template heroes, identical cards,
> one-radius-everywhere kits, and decorative motion on every section. A banned choice
> ships only when the brief, brand, or existing system requires it, with the exception
> recorded. The canonical checklist is
> `C:\Users\Vishal\.agents\skills\frontend-design\references\anti-generic-aesthetics.md`.

### design-engineering

**What:** The front door and operating model. Maps the roles (product designer, UI/UX, interaction, design systems, design engineer, frontend engineer), encodes the design loop, and loads the right specialist skill automatically.
**Use when:** Designing or building any UI, frontend, product interface, design system, or motion experience; when the user asks for a modern, stylish, accessible interface, a design critique, or wants to work like a product designer, UI/UX designer, design engineer, or frontend engineer.
**Try:** `Use design-engineering to design a landing page for a developer tool.`
**Loads:** `design-research`, `visual-ui-design`, `interaction-motion`, `design-systems`, `frontend-craft`, `ai-design-workflow`, `design-critique`. Direct access to any of them still works.

### design-research

**What:** Finds the right problem and direction before pixels: brief, research plan, competitive audit, reference mining, moodboards, style tiles, three contrasting directions, and a direction decision.
**Use when:** You need a design direction, competitor audit, reference board, moodboard, or to understand users before designing.
**Try:** `Use design-research to find a direction for this brief.`

### visual-ui-design

**What:** Builds the visual system: hierarchy, layout, typography, color, spacing, responsive behavior, dark mode, states, and a deliberate style direction (editorial, Swiss, warm, technical, brutalist, glass, bento, maximalist, retrofuturist, organic). Enforces the anti-generic gate on type, palette, and layout.
**Use when:** Designing the visual layer or making an interface feel modern, distinctive, and polished.
**Try:** `Use visual-ui-design to define the type, color, and layout system for this page.`

### interaction-motion

**What:** Designs behavior and motion: interaction model, states, timing, easing, choreography, microinteractions, page transitions, scroll effects, reduced motion, and performance.
**Use when:** Designing or implementing interactions, animation, transitions, or motion systems; when animation feels janky, excessive, generic, or inaccessible.
**Try:** `Use interaction-motion to spec the page transitions and the hero reveal.`

### design-systems

**What:** Builds the system that makes good design the default: token architecture, component APIs, variants, states, documentation, governance, Figma/code parity, and AI-readable `DESIGN.md`/manifests.
**Use when:** Building or maintaining a design system, tokens, component library, theme, or Figma-to-code workflow.
**Try:** `Use design-systems to structure the tokens and component contracts.`

### frontend-craft

**What:** Turns a design into production UI: semantic HTML, CSS architecture, responsive behavior, React/Next.js, Tailwind/shadcn, accessibility, Core Web Vitals, testing, and visual QA. Stops to fix a generic direction before implementing it faithfully.
**Use when:** Implementing a design, improving fidelity, fixing responsiveness, accessibility, performance, or cross-browser quality.
**Try:** `Use frontend-craft to implement this screen in Next.js and Tailwind.`

### ai-design-workflow

**What:** Uses AI agents for design and frontend work with context packs, Figma MCP, v0/Lovable/Framer AI, design-to-code, guardrails, and verification. Rejects the generic AI look at generation time.
**Use when:** Using AI to design or build UI, or when generated UI needs guardrails and review.
**Try:** `Use ai-design-workflow to brief the coding agent and verify the output.`

### design-critique

**What:** Reviews UI with evidence: hierarchy, usability heuristics, states, responsive behavior, accessibility, motion, performance, system consistency, content, and the anti-generic audit. Produces prioritized findings and a fix plan.
**Use when:** Reviewing a UI, page, component, design system, or animation; when something feels off.
**Try:** `Use design-critique to review this checkout flow.`

---

## Cloudflare

### cloudflare

**What:** A product map for Cloudflare: Workers, Pages, D1, R2, KV, Durable Objects, Vectorize, Workers AI, networking, and security. Routes a need to the right product.
**Use when:** Choosing an architecture or product, even if you do not name Cloudflare first.
**Try:** `"Choose the right Cloudflare products for this app."`

### workers-best-practices

**What:** Production guidance for Cloudflare Workers: configuration, bindings, limits, error handling, and deployment shape.
**Use when:** Writing, reviewing, or configuring a Worker.
**Try:** `"Review this Worker for production issues."`

### wrangler

**What:** Runs and troubleshoots Wrangler CLI commands in projects that already have a Wrangler config: local dev, previews, deploy, resources.
**Use when:** The repo has `wrangler.jsonc`, `wrangler.json`, or `wrangler.toml`.
**Try:** `"Set up local dev and deploy this Worker."`

### durable-objects

**What:** Designs and debugs Durable Objects for persistent state, coordination, and single-writer logic.
**Use when:** You need stateful coordination, rate limiting, rooms, or consistent counters on Workers.
**Try:** `"Add a rate limiter with a Durable Object."`

### agents-sdk

**What:** Builds, debugs, and reviews agents with Cloudflare's `agents` package: state, tools, scheduling, and real-time connections.
**Use when:** Building an agent that runs on Cloudflare.
**Try:** `"Build a chat agent with the Cloudflare Agents SDK."`

### nextjs-on-cloudflare

**What:** Migrates and deploys Next.js apps to Workers with vinext or OpenNext, including the trade-offs between them.
**Use when:** Starting a Next.js project on Cloudflare or moving an existing app.
**Try:** `"Deploy this Next.js app to Workers."`

---

## Research and web

Three research paths: **built-in web search** for the default cited report, **Firecrawl** for crawling and extraction, and **Perplexity** as an optional accelerator when its API is connected. Local files route to `firecrawl-parse`.

### research

**What:** A global deep-research workflow. Frames the question, chooses a depth, gathers evidence with built-in web search by default, cross-checks key claims, and saves a cited report under `research/`. Uses Firecrawl for crawling when authenticated and Perplexity only when its API is connected.
**Use when:** Any project needs market analysis, competitive intelligence, a literature review, a technology comparison, or a sourced report.
**Try:** `/research Should we migrate this Next.js app from Pages Router to App Router in 2026?`

> [!warning] Perplexity is optional
> A consumer Pro/Max account cannot authorize Perplexity's API. It requires an API organization with pay-as-you-go billing, and the old Pro API credit was discontinued in February 2026. The skill uses built-in web search instead. If you later create an API org, re-enable the MCP server and run `opencode mcp auth perplexity`.

### firecrawl

**What:** The router for live-web work: search, read, extract, gather sources, discover URLs, bulk extraction, downloads, and change monitoring.
**Use when:** Any task needs current web content rather than model memory.
**Try:** `"Research the current state of WebGPU and cite sources."`

### firecrawl-search

**What:** Web search with query-relevant excerpts, optional full-page content, and discovery of data APIs and indexes.
**Use when:** Finding sources, records, listings, transcripts, or datasets.
**Try:** `"Find recent articles about React 20."`

### firecrawl-scrape

**What:** Reads a known URL and extracts its content or a structured result.
**Use when:** You already have the page URL.
**Try:** `"Scrape this pricing page and extract the tiers."`

### firecrawl-crawl

**What:** Bulk-extracts many pages from one site or section.
**Use when:** The answer spans linked pages under `/docs` or a similar section.
**Try:** `"Crawl the /docs section and summarize it."`

### firecrawl-map

**What:** Lists a site's URLs with search filtering, without fetching every page.
**Use when:** You know the site but not the exact page, or want its structure.
**Try:** `"Map the URLs on this site."`

### firecrawl-parse

**What:** Converts a local file (PDF, DOCX, XLSX, HTML) to markdown, or answers questions about its content.
**Use when:** The input is a file path, not a URL.
**Try:** `"Parse this PDF into markdown."`

### firecrawl-developer-index

**What:** Searches current documentation, release notes, API references, and public issues for libraries, SDKs, and CLIs.
**Use when:** A version, API, error, or migration may have changed after the model's training cutoff.
**Try:** `"Check whether this bug is fixed in the latest release."`

---

## Codebase understanding

The Understand-Anything set. Builds a knowledge graph, then answers from it.

### understand

**What:** Analyzes a codebase into an interactive knowledge graph of architecture, components, and relationships.
**Use when:** Entering an unfamiliar repo or needing a structural map.
**Try:** `"Map this codebase into a knowledge graph."`

### understand-chat

**What:** Answers questions about a codebase using the generated knowledge graph.
**Use when:** You want architecture-level answers rather than a file-by-file read.
**Try:** `"Using the graph, how does authentication work?"`

### understand-diff

**What:** Analyzes a Git diff or pull request for changed components, blast radius, and risks.
**Use when:** Reviewing a PR or checking what a change actually touches.
**Try:** `"Analyze this PR diff and list the risks."`

### understand-explain

**What:** Deep-dives a specific file, function, or module.
**Use when:** You need one piece explained in context.
**Try:** `"Explain src/auth/session.ts in depth."`

### understand-onboard

**What:** Generates an onboarding guide for new team members: setup, structure, key flows, and where to start.
**Use when:** Joining a project or handing it to someone else.
**Try:** `"Generate an onboarding guide for this repo."`

---

## Open source contribution

The maintainer-grade OSS suite: 11 skills for finding issues, mapping unfamiliar code, making the fix, and planning GSoC. `oss-contributor` is the front door: it classifies the request, loads the right specialist skill, and enforces the contribution contract. `oss-issue-scout` finds and scores the work; `gsoc-strategist` turns contribution proof into a campaign. The suite map and usage guide is [[OSS and Freelance Skills]].

### oss-contributor

**What:** Front door for open source and large-codebase contribution: issue selection, maintainer lens, repo policies, AI disclosure, small-diff discipline, quality gates, security reporting, and routing to the specialist roles.
**Use when:** Contributing to any project you do not own, fixing an upstream issue, preparing a PR, or working inside a large company codebase.
**Try:** `/oss I want to contribute a fix to this repo but I have never seen the codebase`

### large-codebase-navigator

**What:** Maps a large, legacy, monolithic, or unfamiliar codebase by tracing one real path through routes, services, data stores, and external boundaries; extracts invariants, ownership, blast radius, and the smallest safe change point.
**Use when:** You are lost in a repo, joining a huge company codebase, or need to change code without breaking hidden dependencies.
**Try:** `"Map this monorepo and trace how a payment refund actually works before I touch it."`

### oss-senior-engineer

**What:** The issue-to-PR operating loop: choose the right issue, reproduce, root-cause, design the smallest fix, test first, run the full gate, write a reviewable PR, and respond to review like a senior contributor.
**Use when:** Fixing an upstream bug, adding a feature, preparing a patch, or reviewing someone else's PR.
**Try:** `"Use oss-senior-engineer to fix this issue and prepare the PR."`

### oss-system-designer

**What:** Architecture and design for shared code: RFC/ADR, alternatives, trade-offs, public contracts, compatibility, migration, rollout, and maintainer consensus.
**Use when:** A change touches an API, service boundary, plugin contract, schema, or other shared design.
**Try:** `"Use oss-system-designer to write an RFC for adding plugin hooks without breaking existing plugins."`

### oss-uiux-frontend

**What:** UI/UX, accessibility, design-system, CSS, component, and frontend contribution in a project with its own design language; covers states, responsive behavior, dark mode, keyboard and screen-reader testing, and visual evidence.
**Use when:** Fixing a UI bug, contributing a component, improving accessibility, or reviewing a frontend PR.
**Try:** `"Use oss-uiux-frontend to fix this keyboard trap without restyling the whole app."`

### oss-backend

**What:** Backend contribution: request paths, APIs, auth, jobs, queues, integrations, concurrency, retries, error handling, observability, compatibility, and rollout.
**Use when:** The change touches a server-side request, service boundary, API contract, or background job.
**Try:** `"Use oss-backend to fix this idempotency bug in the webhook handler."`

### oss-database

**What:** Database contribution: schema design, safe migrations, indexes, query plans, backfills, data integrity, multi-engine compatibility, and rollback.
**Use when:** The change touches SQL, a migration, a slow query, data corruption, or a schema contract.
**Try:** `"Use oss-database to plan a zero-downtime migration for this column rename."`

### oss-devops-server

**What:** DevOps, SRE, and server contribution: CI/CD, containers, IaC, release engineering, Linux, networking, reverse proxies, resource limits, observability, and on-call safety.
**Use when:** A pipeline, deployment, container, infrastructure, server, or runtime change is involved.
**Try:** `"Use oss-devops-server to fix this GitHub Actions failure without exposing secrets to forks."`

### oss-security

**What:** Security review and coordinated disclosure: threat modeling, authz, injection, secrets, dependency and supply-chain risk, safe reproduction, private reporting, and a minimal fix.
**Use when:** The task involves a vulnerability, security review, CVE, advisory, secret leak, or permission boundary.
**Try:** `"Use oss-security to review this authorization path and report the finding privately."`

### oss-issue-scout

**What:** Finds, scores, and tracks open-source issues: GitHub label queries, stale/assigned filtering, a 100-point fit score, human-lead and mentor discovery, issue briefs, and a contribution pipeline.
**Use when:** You do not know what to work on, need to scan repos for good first issues, want to find the area maintainer or GSoC mentor, or need to keep a contribution pipeline.
**Try:** `/issues scan kubernetes/kubernetes and rust-lang/rust for unassigned bugs I can fix`

### gsoc-strategist

**What:** Plans a Google Summer of Code campaign: organization shortlisting, ideas-list analysis, contribution proof, mentor outreach, proposal structure, timeline, risks, community bonding, and coding cadence.
**Use when:** You are targeting GSoC, choosing an org, writing a proposal, contacting a mentor, or planning the months before applications.
**Try:** `/gsoc Build my Oct-to-May plan for a GSoC project in the Kubernetes ecosystem`

> [!warning] Contribution guardrails
> Read the project's `CONTRIBUTING.md`, `SECURITY.md`, and AI policy first. Never
> fabricate tests or maintainer approval, never report a vulnerability publicly,
> and never mass-open AI-generated PRs.

---

## Build and ship

The build-ship team. One skill and seven named agents that take a change from frame to release, with independent verification and a hard anti-generic UI gate.

### build-ship-team

**What:** Runs a small named team — `ship-lead`, `scout`, `architect`, `builder`, `verifier`, `reviewer`, `shipper` — through six gates: frame, recon, plan, build, verify, ship. Picks the smallest lane that can still prove the change works, keeps evidence in `.ship/`, and refuses to ship on a missing gate.
**Use when:** You want to build and ship fast without shipping unverified code, or you need a repeatable release path for a feature, fix, or client project.
**Try:** `/ship-team add passkey login to the existing auth flow` or `/build-fast fix the empty states on the orders table`
**Agents:** 7 OpenCode agents in `~/.config/opencode/agents` and 7 Claude Code agents in `~/.claude/agents`.
**Docs:** [[Build Ship Team]]

---

## AI engineering

The production-side skill. It is deliberately narrow: it gates one LLM change and refuses to ship on missing evidence.

### llm-release-gate

**What:** Reviews a prompt, model, retrieval, tool, or agent change against local evidence and returns `SHIP`, `SHIP WITH CONDITIONS`, or `BLOCK`, with an evidence table, budget table, risk register, rollback plan, and durable record.
**Use when:** You are preparing a canary or rollout, a model or prompt change regressed quality, or you need to decide whether an AI feature is safe to ship.
**Try:** `/release-gate Review this prompt change. The regression set is in run-manifest.json.`
**Report:** [[Agent skills AI engineers use]] — the research and full specification behind the skill.

---

## Reverse engineering

The REA pair. The first is the OpenCode front door; the second is the full
upstream workflow it loads.

### rea

**What:** OpenCode front door for REA. Loads the full `reverse-engineer-anything` workflow and adds the Code Mode tool namespace, `/rea` and `@rea` entry points, recovery steps, and safety rules.
**Use when:** You want to reverse engineer an app, binary, package, firmware image, .NET assembly, JavaScript/Electron app, browser/runtime behavior, or capture file.
**Try:** `@rea explain how offline search works in C:\Apps\Example`

### reverse-engineer-anything

**What:** The managed upstream REA skill. Owns target routing, provider selection, Evidence workflows, runtime discipline, and the investigation checklist across 207 MCP tools.
**Use when:** You want the full upstream instructions directly, without the OpenCode wrapper.
**Try:** `"Use reverse-engineer-anything to compare these two app versions and cite the Evidence."`

> [!note] REA setup
> REA is also registered as the MCP server `rea`. Its guided prompts appear as
> `/rea:investigate_feature`, `/rea:compare_application_versions`,
> `/rea:trace_crash`, and other `/rea:*` commands when the current session
> exposes them. See [[REA Skill Setup Plan]] for the full installation map.

---

## Writing and sessions

### stop-slop

**What:** Removes predictable AI writing tells from prose: filler, formulaic contrasts, dramatic fragmentation, passive throat-clearing.
**Use when:** Drafting or editing docs, READMEs, release notes, or any text that should sound human.
**Try:** `"Clean the AI tone out of this README."`

### handoff

**What:** Produces a complete handoff document so another model or session can continue exactly where this one stopped.
**Use when:** The context is nearly full, the session is ending, or you want to switch tools.
**Try:** `"Write a handoff for this session."`

### grill-me

**What:** Interviews you relentlessly about a plan or design, resolving each branch of the decision tree until you share the same understanding.
**Use when:** You want to stress-test an idea before committing to it.
**Try:** `"Grill me on this architecture."`

### caveman

**What:** Switches to terse caveman speech: answer first, no fluff, every technical fact kept.
**Use when:** You want brevity or fewer tokens.
**Try:** `"Caveman mode."` Stop with `"stop caveman"` or `"normal mode"`.

---

## Skill building and testing

### skill-creator

**What:** Creates, edits, benchmarks, and improves skills, including trigger-description optimization and eval runs.
**Use when:** Turning a repeated workflow into a skill or fixing one that does not trigger.
**Try:** `"Use skill-creator to turn our release workflow into a skill."`

### mcp-builder

**What:** Guides the full lifecycle of an MCP server: protocol, SDK choice, tool schemas, evals, and Inspector testing.
**Use when:** Building an MCP server in Python (FastMCP) or TypeScript.
**Try:** `"Build an MCP server for our internal API."`

### webapp-testing

**What:** A Playwright toolkit for local web apps: start servers, inspect the rendered page, act on discovered selectors, capture screenshots and console logs.
**Use when:** Verifying frontend behavior or debugging a UI in a real browser.
**Try:** `"Test the checkout flow at localhost:5173."`

### find-skills

**What:** Discovers and installs new skills when you ask "is there a skill for X?"
**Use when:** You need capability that is not installed yet.
**Try:** `"Find a skill for database migrations."`

---

## Knowledge and notes

### vault-daydream

**What:** Mines this Obsidian vault for non-obvious connections. Samples recency-weighted note pairs, synthesizes an insight, scores novelty/coherence/usefulness with a skeptical critic, and keeps only insights averaging 7.0 or higher. Writes notes to `Daydreams/`, a digest, a daily-note section, and a history log.
**Use when:** You want serendipitous cross-note ideas rather than search.
**Try:** `"Daydream my vault."`

**One-time setup:**

```powershell
python "$env:USERPROFILE\.agents\skills\vault-daydream\scripts\daydream.py" resolve --set "C:\Users\Vishal\OneDrive\Documents\Obsidian Vault"
```

---

## Integrations

### composio

**What:** Routes Composio work across two products: Composio For You (your own apps) and Composio Platform (apps your users connect). Covers MCP setup, CLI use, SDK sessions, auth, and debugging.
**Use when:** You want the agent to act in Gmail, Slack, GitHub, Notion, Calendar, Linear, or similar.
**Try:** `"Connect my Gmail and summarize unread mail."`

> [!warning] Setup required
> The Composio MCP server is configured globally, but OAuth must be completed once:
> `opencode mcp auth composio` → approve in the browser → `opencode mcp list`.

### insforge

**What:** App-code guidance for InsForge and `@insforge/sdk`: database CRUD, auth, storage and RLS, functions, OpenRouter AI, realtime, email, and payments.
**Use when:** Writing application code that uses InsForge.
**Try:** `"Add auth and a database to this app with InsForge."`

### insforge-cli

**What:** InsForge infrastructure through the CLI: projects, SQL, migrations, RLS policies, functions, storage, backups, deploys, secrets, logs, and diagnostics.
**Use when:** Setting up or operating the backend, not writing app code.
**Try:** `"Create an InsForge project and run the migrations."`

### insforge-debug

**What:** Diagnoses InsForge failures: SDK errors, 4xx/5xx, gateway timeouts, auth and RLS denials, realtime issues, slow queries, and deploy failures. Also runs security, performance, and launch-readiness audits.
**Use when:** Something is broken and you need the failing boundary.
**Try:** `"Diagnose this 500 error in my InsForge project."`

### insforge-integrations

**What:** Wires external auth providers (Clerk, Auth0, WorkOS, Kinde, Stytch, Better Auth) into InsForge for JWT-based RLS, and adds OKX x402 pay-per-use billing.
**Use when:** Connecting an identity provider or onchain payments.
**Try:** `"Wire Clerk auth into InsForge with RLS."`

---

## Engineering leadership

The senior-dev suite. `senior-dev-os` is the front door: it loads the smallest useful set of skills automatically, and every skill is also directly accessible. The reasoning model is in [[Senior Developer Thinking]]; the full playbook in [[Senior Developer Operating System]].

### senior-dev-os

**What:** The front door and reasoning model. Encodes how senior engineers think (systems, reversibility, trade-offs, risk-first, leverage, ownership), then loads the smallest useful set of sub-skills automatically. Also defines senior defaults for architecture, delivery, quality, docs, agents, and operations.
**Use when:** Starting, rescuing, or standardizing a project, thinking through an ambiguous engineering problem, or deciding which process skill applies.
**Try:** `/senior-dev start a new client project for a booking system`
**Loads:** `goal`, `advisor`, `subagents`, `project-kickoff`, `codebase-playbook`, `testing-strategy`, `agent-delegation`, `documentation-system`, `launch-readiness`, plus Superpowers support skills. Direct access to any of them still works.

### project-kickoff

**What:** Turns an idea into a buildable first milestone: one-page product brief, constraints and non-goals, architecture ADR, walking skeleton, three to five vertical slices, docs baseline, and quality gates.
**Use when:** Starting a new product, feature, or client project, before writing feature code.
**Try:** `"Use project-kickoff to turn this invoicing idea into a six-week MVP."`

### codebase-playbook

**What:** Audits and standardizes an existing repo: structure, `AGENTS.md`, README, architecture map, ADR policy, dependency policy, quality gates, review rules, release process, and maintenance cadence.
**Use when:** A codebase feels messy, onboarding is slow, or agents keep changing the wrong things.
**Try:** `"Use codebase-playbook to audit this repo and write AGENTS.md."`

### testing-strategy

**What:** Builds a risk-based test plan: test levels, test cases, edge-case catalog, test data, CI gates, coverage policy, and flaky-test rules.
**Use when:** Planning tests, deciding what to test at which level, or fixing low-confidence or flaky suites.
**Try:** `"Use testing-strategy to plan tests for checkout, including edge cases."`

### agent-delegation

**What:** Turns work into context-complete task packets, splits it into independent subtasks, assigns parallel agents safely, and defines review and integration gates.
**Use when:** Giving work to AI agents, splitting a plan, running agents in parallel, or reviewing agent output.
**Try:** `"Use agent-delegation to split this plan across three agents."`

### documentation-system

**What:** Designs documentation that stays current: README, AGENTS.md, ADRs, API docs, runbooks, changelog, onboarding, ownership, and freshness checks.
**Use when:** Docs are missing, stale, or scattered, or a new project needs a docs baseline.
**Try:** `"Use documentation-system to set up this repo's docs and runbooks."`

### launch-readiness

**What:** A go/no-go review for shipping: security, data and migrations, reliability, observability, performance, accessibility, support, rollout, and rollback.
**Use when:** Preparing to ship a feature or project to production.
**Try:** `"Use launch-readiness to review this release before we deploy."`

---

## Freelancing and client work

The freelance business suite. `freelance-operator` is the front door: it treats freelancing as a pipeline and a delivery system, not a collection of tactics. The suite map and usage guide is [[OSS and Freelance Skills]].

### freelance-operator

**What:** Front door for the freelance business: positioning, lead generation, qualification, pricing, proposals, product leadership, delivery, proof, and retention. Anchors the work on measurable outcomes and the market reality of commodity versus specialist work.
**Use when:** Winning, scoping, pricing, or delivering freelance work, especially AI, software, product, or design services.
**Try:** `/freelance Help me turn my AI evaluation work into a paid offer`

### freelance-lead-gen

**What:** Builds a repeatable lead engine: ICP, offer, channel choice, qualified list, personalized outreach, follow-up cadence, discovery, pipeline stages, and metrics.
**Use when:** You need more clients, better leads, a narrower niche, or a consistent prospecting system.
**Try:** `"Use freelance-lead-gen to define my ICP and build a 50-lead list for an AI document-review offer."`

### freelance-business-development

**What:** Positions and prices the work: commercial models, rate and margin math, proposals, SOWs, negotiation, contracts, change control, and retainers.
**Use when:** Turning a discovery into a proposal, setting a price, negotiating terms, or structuring ongoing work.
**Try:** `"Use freelance-business-development to price a six-week AI product discovery and write the proposal."`

### freelance-product-lead

**What:** Acts as lead product manager for a client engagement: discovery, problem framing, MVP, PRD, prioritization, roadmap by outcome, stakeholder alignment, and measurement.
**Use when:** Scoping a product, defining an MVP, writing a PRD, or keeping a client's scope and stakeholders aligned.
**Try:** `"Use freelance-product-lead to turn this vague client request into a testable MVP and PRD."`

### freelance-client-delivery

**What:** Runs the engagement: kickoff, onboarding, weekly status, change control, QA, stakeholder communication, handoff, case study, referral, and retainer.
**Use when:** Delivering a project, managing a client relationship, handing off work, or turning a result into proof.
**Try:** `"Use freelance-client-delivery to build the kickoff plan and weekly update cadence for this engagement."`

> [!note] Market reality
> The research report [[Freelancing and open source AI skills]] found that the open
> marketplace is price-compressed (median posted AI rate around $27.50/hour, most
> postings under $50) while specialist and direct work pays far more. The suite is
> built to move the work toward measurable, specialist outcomes rather than
> competing on volume.

---

## Goals, advice, and orchestration

The front of the funnel: define the outcome, get specialist counsel, then split the work across the right experts. Documented in detail in [[Goal to Execution]].

### goal

**What:** Turns an ambition into a researched, measurable goal: one-sentence outcome, success levels, constraints, non-goals, resource inventory, domain research, three to five milestones, pre-mortem, kill criteria, and review cadence.
**Use when:** Defining a new goal, deciding what to build, or turning an outcome into a plan backed by evidence.
**Try:** `/goal I want to launch a freelance invoicing SaaS in six weeks and get 10 paying users.`

### advisor

**What:** Gives specialist advice rather than generic encouragement: frames the decision, chooses two to four expert lenses, gets independent views, surfaces disagreement, recommends with confidence, and names the cheapest test.
**Use when:** You need a second opinion, a red-team review, a pre-mortem, or a panel of specialist perspectives on a goal, plan, design, or decision.
**Try:** `/advisor Should we build auth ourselves or use a managed provider?`

### subagents

**What:** Chooses specialist subagent roles and orchestrates them: roster, mission, subagent briefs, dependency graph, file ownership, parallel vs serial phases, review gates, and integration.
**Use when:** A goal splits into research, product, architecture, build, test, security, docs, or review work that different specialists should own.
**Try:** `/subagents Split the launch of this SaaS across specialist roles.`

---

## Workflow recipes

### From a goal to execution

```text
/goal <outcome>
  → goal (research, success metrics, milestones, kill criteria)
  → advisor (specialist counsel and red-team review)
  → subagents (roster, briefs, dependency graph)
  → agent-delegation (task packets, worktrees, review gates)
  → senior-dev-os (loads project-kickoff, testing-strategy, launch-readiness as needed)
```

Use `advisor` before committing to an expensive option. Use `subagents` only when the work has distinct specialist roles and clean ownership. `senior-dev-os` can also start the flow: it loads the right sub-skills instead of making you name them.

### Ship a feature

```text
brainstorming
  → writing-plans
  → executing-plans (or subagent-driven-development)
  → code-change-verification
  → requesting-code-review
  → finishing-a-development-branch
```

### Fix a bug

```text
systematic-debugging
  → test-driven-development
  → verification-before-completion
```

### Start from a vague request

```text
ask-questions-if-underspecified
  → implementation-strategy (if a boundary is involved)
  → writing-plans
```

### Risky change to a public API or schema

```text
implementation-strategy
  → writing-plans
  → test-driven-development
  → code-change-verification
```

### Research a topic

```text
/research <question>
  → research skill (built-in web search; Perplexity optional)
  → cited report in research/<slug>-<date>.md
```

Fallback when Perplexity is unavailable: `firecrawl-search` → `firecrawl-scrape`.

### Check a library or a breaking change

```text
firecrawl-developer-index
  → firecrawl-scrape (read the canonical page)
```

### Reverse engineer a shipped app or binary

```text
/rea <target and question>
  → rea skill
  → reverse-engineer-anything
  → target summary or inventory
  → focused Evidence follow-ups
  → observations, inferences, unknowns
```

Use `@rea` instead when composing a longer prompt. Use `rea doctor --client
opencode --json` only when tools are missing or a provider is blocked.

### Compare two shipped versions

```text
/rea:compare_application_versions "<old path>" "<new path>"
```

If the guided prompt is not exposed, ask `/rea` to compare the two artifacts and
require Evidence IDs for every claimed difference.

### Understand a new repository

```text
understand
  → understand-chat
  → understand-explain
```

### Contribute to open source

```text
/oss <issue or repo and goal>
  → oss-contributor (choose the work and read the policies)
  → large-codebase-navigator (map the path and blast radius)
  → oss-senior-engineer (reproduce, fix, test, PR)
  → specialist skill as needed
  → verification-before-completion
```

For a role-specific contribution, go straight to `oss-uiux-frontend`,
`oss-backend`, `oss-database`, `oss-devops-server`, or `oss-security`.

### Work inside a very large company codebase

```text
/oss I need to change <behavior> in this large codebase
  → large-codebase-navigator (surface map, runtime topology, traced path)
  → extract invariants and ownership
  → oss-system-designer (if the change crosses a boundary)
  → oss-senior-engineer (smallest safe change)
  → code-change-verification
```

### Win and deliver freelance work

```text
/freelance <stage or goal>
  → freelance-operator (classify the stage)
  → freelance-lead-gen (ICP, offer, pipeline)
  → freelance-business-development (price, proposal, contract)
  → freelance-product-lead (scope, PRD, roadmap)
  → freelance-client-delivery (deliver, handoff, case study)
```

### Find a high-leverage open-source issue

```text
/issues scan <org/repo> for good first issues and help-wanted bugs
  → score impact, reproducibility, scope, maintainer signal, fit
  → find the human lead: assignee, CODEOWNERS, recent authors, reviewers
  → verify open, unassigned, not already fixed
  → comment with a reproduction plan
  → /oss make the fix
```

### Plan a GSoC campaign

```text
/gsoc I want to target <org> for the next GSoC
  → choose 3 orgs and score fit
  → read the ideas list and identify mentors
  → use /issues to build 3–5 contributions in the target area
  → draft the proposal and timeline
  → ask the mentor one specific question
  → submit early and keep contributing
```

### Gate an LLM change before release

```text
/release-gate <prompt, model, RAG, tool, or agent change>
  → classify the change and blast radius
  → require a falsifiable claim
  → inventory required evidence
  → run scripts/gate_report.py on run-manifest.json
  → review budgets, failure modes, observability, and rollback
  → return SHIP, SHIP WITH CONDITIONS, or BLOCK
```

### End of session

```text
handoff
```

---

## Current setup status

| Item | Status |
| --- | --- |
| Global skills | 94 installed in `C:\Users\Vishal\.agents\skills` |
| OpenCode registration | All 94 discoverable; reload OpenCode for the new commands |
| Firecrawl CLI | v1.26.15 installed; not authenticated |
| Perplexity MCP | Disabled — requires paid API org |
| Research command | `/research` available globally |
| Senior-dev command | `/senior-dev` available globally |
| Senior-dev access | `senior-dev-os` loads sub-skills automatically; direct invocation also works |
| Senior-dev research | `senior-dev-os/references/senior-dev-thinking.md` and `sub-skill-map.md` |
| Build-ship command | `/ship-team` and `/build-fast` available globally |
| Build-ship agents | 7 OpenCode agents and 7 Claude Code agents, all verified |
| Build-ship skill | `build-ship-team` with 4 references and 7 templates |
| Goal command | `/goal` available globally |
| Advisor command | `/advisor` available globally |
| Subagents command | `/subagents` available globally |
| OSS command | `/oss` available globally; `@oss-contributor` loads the front-door skill |
| OSS suite | 11 skills: issue scouting, repo mapping, senior contribution, system design, UI/UX frontend, backend, database, DevOps/server, security, GSoC strategy |
| Issue command | `/issues` available globally; `@oss-issue-scout` finds and scores issues |
| GSoC command | `/gsoc` available globally; `@gsoc-strategist` plans the campaign and proposal |
| Release gate command | `/release-gate` available globally; `@llm-release-gate` returns SHIP, SHIP WITH CONDITIONS, or BLOCK |
| Freelance command | `/freelance` available globally; `@freelance-operator` loads the front-door skill |
| Freelance suite | 5 skills: lead generation, business development, product lead, client delivery |
| REA command | `/rea` available globally; `@rea` loads the front-door skill |
| REA MCP | `rea` connected; 207 tools, 6 guided prompts |
| REA CLI | `rea-agents@6.7.0` installed globally |
| REA native engines | Ghidra, IDA, JADX, and Kuna not installed; Hopper is unsupported on Windows; static JS/.NET/artifact work is ready |
| Composio MCP | Configured; OAuth pending |
| Vault Daydream | Installed; vault path not yet saved |

> [!note] Vault Daydream vault
> The skill auto-detects `.obsidian`, but saving the path once avoids prompts:
> `resolve --set "C:\Users\Vishal\OneDrive\Documents\Obsidian Vault"`.

---

## Maintenance

### List

```powershell
npx skills ls -g -a opencode
```

### Add a skill

```powershell
npx skills add <owner>/<repo> --skill <skill-name> -g -a opencode --copy -y
```

`--copy` avoids Windows symlink problems.

### Update all global skills

```powershell
npx skills update -g
```

### Remove a skill

```powershell
npx skills remove --global <skill-name>
```

### Where skills live

| Scope | Path |
| --- | --- |
| Global (this machine) | `C:\Users\Vishal\.agents\skills` |
| Project | `.agents/skills`, `.opencode/skills`, `.claude/skills` |
| OpenCode native global | `C:\Users\Vishal\.config\opencode\skills` |

OpenCode discovers all of them. This setup uses the shared `.agents/skills` directory so other agents can use the same files.

---

## Related notes

- [[Senior Developer Thinking]] — how senior engineers reason, with research and sources.
- [[Senior Developer Operating System]] — the operational playbook and lifecycle.
- [[Goal to Execution]] — goal, advisor, and subagent workflow.
- [[Design Engineering Skills]] — design, UI/UX, motion, systems, frontend craft, AI workflow, critique.
- [[OSS and Freelance Skills]] — the 16-skill suite for open-source contribution and freelance client work, with `/oss`, `/issues`, `/gsoc`, and `/freelance`.
- [[GSoC Strategy 2027]] — month-by-month campaign plan, contribution proof, and proposal checklist.
- [[Agent skills AI engineers use]] — research report and full specification behind `llm-release-gate`.
- [[Freelancing and open source AI skills]] — the research report behind the OSS and freelance suite.
- [[REA Skill Setup Plan]] — reverse-engineering setup, `/rea`, `@rea`, MCP registration, Evidence workflow, and maintenance.

---

## Sources

- [10 Best OpenCode Skills That Are Actually Useful in 2026](https://composio.dev/content/10-best-opencode-skills-that-are-actually-useful-in-2026) — Composio
- [12 OpenCode Skills Every Dev Team Should Steal](https://hackernoon.com/twelve-opencode-skills-every-dev-team-should-steal) — HackerNoon
- [obra/superpowers](https://github.com/obra/superpowers)
- [anthropics/skills](https://github.com/anthropics/skills)
- [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)
- [cloudflare/skills](https://github.com/cloudflare/skills)
- [firecrawl/skills](https://github.com/firecrawl/skills)
- [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)
- [trailofbits/skills](https://github.com/trailofbits/skills)
- [openai/openai-agents-python](https://github.com/openai/openai-agents-python)
- [glebis/claude-skills](https://github.com/glebis/claude-skills)
- [ComposioHQ/composio](https://github.com/ComposioHQ/composio)
- [Perplexity MCP Server](https://docs.perplexity.ai/docs/getting-started/integrations/mcp-server)
- [morluto/rea](https://github.com/morluto/rea)
- [rea-agents on npm](https://www.npmjs.com/package/rea-agents)

---

*Last verified: 2026-11-03. Skill count: 94.*
