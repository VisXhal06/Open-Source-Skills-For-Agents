# Open Source Skills for Agents

**93 agent skills in the portable `SKILL.md` format, plus the notes, reports, and research behind them — in one repository.**

Agent skills are instruction packs that teach a coding agent how to do a specific kind of work well. This collection covers the whole lifecycle of software work: deciding what to build, planning it, implementing and verifying it, designing the interface, shipping it, researching problems, contributing to open source, and running client work.

## Why this repository exists

Most agent sessions start from zero. You re-explain how you want plans written, how code should be verified, how a UI should be designed, or what a maintainer-grade pull request looks like. The result is inconsistent work and a lot of repeated prompting.

This repository packages those expectations as reusable skills so that any compatible agent can load them on demand:

- **Consistent quality** — the same planning, review, testing, and verification workflows every time.
- **Less prompting** — state the outcome instead of rebuilding the process.
- **Guardrails, not just suggestions** — skills such as `verification-before-completion` require fresh evidence before work is called done.
- **Portable** — the open `SKILL.md` format works across OpenCode, Claude Code, and other compatible harnesses.
- **Transparent** — the `docs/` folder explains what each skill does, when to use it, and how it was researched.

## What is an agent skill?

A skill is a folder containing a `SKILL.md` file. The file starts with YAML frontmatter:

```yaml
---
name: systematic-debugging
description: Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes.
---
```

The agent reads only the name and description at session start. When a request matches, it loads the full instructions. Some skills also ship scripts, references, templates, or assets.

Skills are not separate programs. They guide the agent's normal tools: reading files, running commands, editing code, and searching the web.

## What is inside

| Area | Skills | What it covers |
| --- | ---: | --- |
| Planning and development | 15 | Session bootstrap, brainstorming, plans, execution, TDD, debugging, review, worktrees, parallel agents |
| Senior-dev guardrails | 3 | Clarifying underspecified work, compatibility decisions, verification before completion |
| Frontend and design | 5 | Frontend design, React performance, composition patterns, web interface guidelines, web performance |
| Design engineering | 8 | Design research, visual UI, motion, design systems, frontend craft, AI-assisted design, critique |
| Cloudflare | 6 | Workers, Durable Objects, Wrangler, Agents SDK, Next.js on Workers, performance |
| Research and web | 8 | Deep research, Firecrawl search, scrape, crawl, map, parse, and developer docs |
| Codebase understanding | 5 | Architecture graphs, code chat, diffs, deep dives, onboarding guides |
| Open source contribution | 11 | Issue scouting, maintainer-grade fixes, backend, database, security, DevOps, UI/UX, system design, GSoC |
| AI engineering | 1 | LLM release gate for prompts, models, RAG, and agent changes |
| Reverse engineering | 2 | REA workflows and shipped-artifact reconstruction |
| Writing and sessions | 4 | Removing AI prose tells, handoffs, design grilling, terse mode |
| Skill building and testing | 4 | Skill creation, MCP servers, web app testing, discovering new skills |
| Knowledge and notes | 1 | Mining an Obsidian vault for non-obvious connections |
| Integrations | 5 | Composio, InsForge app work, CLI, debugging, integrations |
| Engineering leadership | 7 | Senior-dev operating system, project kickoff, codebase playbooks, testing, delegation, docs, launch readiness |
| Freelancing and client work | 5 | Lead generation, proposals and pricing, product leadership, delivery, operations |
| Goals, advice, and orchestration | 3 | Goal definition, expert advice, subagent orchestration |
| **Total** | **93** | Plus 8 reference notes, 2 reports, and 9 research notes in `docs/` |

## How skills load

1. At session start, the agent indexes every skill's **name** and **description**.
2. When your request matches a description, the agent loads that skill's instructions.
3. For reliable routing, name the skill explicitly: *"Use the `systematic-debugging` skill on this failure."*

This keeps context small: you get a catalogue at startup and pay for the full instructions only when a skill is used.

## Quick start

### 1. Clone the repository

Windows (PowerShell):

```powershell
git clone https://github.com/VisXhal06/Open-Source-Skills-For-Agents.git "$env:USERPROFILE\Open-Source-Skills-For-Agents"
```

macOS / Linux:

```bash
git clone https://github.com/VisXhal06/Open-Source-Skills-For-Agents.git ~/Open-Source-Skills-For-Agents
```

### 2. Pick the skills directory

| Harness | Global (all projects) | Project-local |
| --- | --- | --- |
| OpenCode | `~/.agents/skills` (shared) or `~/.config/opencode/skills` | `.agents/skills`, `.opencode/skills`, or `.claude/skills` |
| Claude Code | `~/.claude/skills` | `.claude/skills` |
| Other `SKILL.md` harnesses | Use the documented global skills directory | Use the documented project skills directory |

OpenCode discovers the shared `~/.agents/skills` directory as well as its native global directory, so the same files can be used by multiple agents.

### 3. Copy the skills

Windows (PowerShell):

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.agents\skills" | Out-Null
Copy-Item -Recurse -Force "$env:USERPROFILE\Open-Source-Skills-For-Agents\skills\*" "$env:USERPROFILE\.agents\skills\"
```

macOS / Linux:

```bash
mkdir -p ~/.agents/skills
cp -R ~/Open-Source-Skills-For-Agents/skills/. ~/.agents/skills/
```

For Claude Code, replace the destination with `$env:USERPROFILE\.claude\skills` (Windows) or `~/.claude/skills` (macOS/Linux).

### 4. Verify and restart

```powershell
$dest = "$env:USERPROFILE\.agents\skills"
(Get-ChildItem $dest -Directory).Count
Get-ChildItem $dest -Directory | Where-Object { -not (Test-Path (Join-Path $_.FullName 'SKILL.md')) }
```

```bash
find ~/.agents/skills -mindepth 1 -maxdepth 1 -type d | wc -l
for d in ~/.agents/skills/*/; do [ -f "$d/SKILL.md" ] || echo "missing: $d"; done
```

Expect **93** skill folders (or more if you already had skills), and no output from the second command. Then restart the agent session so it re-indexes the skills.

## Let your agent install everything itself

Paste this prompt into a fresh agent session. The agent will detect its own skills directory, clone the repo, install all 93 skills, verify them, clean up, and report back.

```text
Install the Open-Source-Skills-For-Agents collection on this machine.

Repository: https://github.com/VisXhal06/Open-Source-Skills-For-Agents
Goal: make all 93 skills available to you in future sessions.

Rules:
1. Detect the global skills directory your harness loads:
   - OpenCode: ~/.agents/skills (shared) or ~/.config/opencode/skills
   - Claude Code: ~/.claude/skills
   - Another SKILL.md-compatible harness: use its documented global skills directory.
   If you cannot determine the directory, stop and ask me instead of guessing.
2. Clone the repository into a temporary directory.
3. Copy every folder inside skills/ into the global skills directory. Do not copy docs/ or README.md.
4. Never delete unrelated skills. If a skill name already exists, compare both versions, keep the newer content, and report the conflict.
5. Verify that each of the 93 copied folders contains a SKILL.md with name and description frontmatter.
6. Remove the temporary clone.
7. Report the destination path, how many skills were installed, any conflicts, and remind me to restart the session so you re-index the skills.
```

The agent should finish with a report like: destination path, 93 installed, 0 conflicts, and a reminder to restart. If it cannot find its skills directory, it should ask rather than install somewhere arbitrary.

For a project-local install, change rule 1 to the project path (`.agents/skills` for OpenCode, `.claude/skills` for Claude Code) and install there instead.

## Updating

```bash
git -C ~/Open-Source-Skills-For-Agents pull --ff-only
mkdir -p ~/.agents/skills
cp -R ~/Open-Source-Skills-For-Agents/skills/. ~/.agents/skills/
```

On Windows, use `git -C "$env:USERPROFILE\Open-Source-Skills-For-Agents" pull --ff-only` and the `Copy-Item` command from the quick start.

Re-copying overwrites skills with the same name. Back up any local edits first. Then restart the session so the updated descriptions are re-indexed.

## What to use it for

| Goal | Start with |
| --- | --- |
| Turn a vague idea into a plan | `brainstorming` → `writing-plans` → `executing-plans` |
| Fix a hard bug | `systematic-debugging` → `test-driven-development` → `verification-before-completion` |
| Design or polish a UI | `design-engineering`, `design-critique`, `frontend-craft` |
| Ship on Cloudflare | `cloudflare`, `workers-best-practices`, `wrangler` |
| Contribute to open source | `oss-contributor`, `oss-issue-scout` |
| Run a freelance project | `freelance-operator`, `freelance-client-delivery` |
| Research a topic | `research`, `firecrawl` |
| Understand a new codebase | `understand`, `understand-onboard` |
| Reverse engineer a shipped app | `reverse-engineer-anything`, `rea` |
| Prepare a branch for review | `requesting-code-review`, `verification-before-completion` |
| End a long session cleanly | `handoff` |

## Requirements and limitations

- **Git** and an agent that supports `SKILL.md` skills.
- Skills are **instructions**, not a sandbox. They use the agent's normal tools and permissions. Review what you install before using it in a sensitive environment.
- Some skills expect optional tools or accounts: Firecrawl CLI, Composio MCP, InsForge CLI, REA MCP, Cloudflare/Wrangler. The planning, design, engineering, research, and open-source skills work without extra setup.
- Skills are installed copies of publicly available agent skill packs. Licenses and attribution requirements may vary by skill; check the upstream project before redistributing.

## Repository layout

```text
skills/                 93 skill packages, one folder per skill
  <skill-name>/
    SKILL.md            name, description, and instructions
    ...                 optional scripts, references, templates, assets
docs/                   reference notes, reports, and research
  reports/
  research_notes/
README.md               this file
```

## Skill index

<details>
<summary>All 93 skills (alphabetical)</summary>

- [advisor](skills/advisor/SKILL.md)
- [agent-delegation](skills/agent-delegation/SKILL.md)
- [agents-sdk](skills/agents-sdk/SKILL.md)
- [ai-design-workflow](skills/ai-design-workflow/SKILL.md)
- [ask-questions-if-underspecified](skills/ask-questions-if-underspecified/SKILL.md)
- [brainstorming](skills/brainstorming/SKILL.md)
- [caveman](skills/caveman/SKILL.md)
- [cloudflare](skills/cloudflare/SKILL.md)
- [codebase-playbook](skills/codebase-playbook/SKILL.md)
- [code-change-verification](skills/code-change-verification/SKILL.md)
- [composio](skills/composio/SKILL.md)
- [design-critique](skills/design-critique/SKILL.md)
- [design-engineering](skills/design-engineering/SKILL.md)
- [design-research](skills/design-research/SKILL.md)
- [design-systems](skills/design-systems/SKILL.md)
- [diagnosing-superpowers](skills/diagnosing-superpowers/SKILL.md)
- [dispatching-parallel-agents](skills/dispatching-parallel-agents/SKILL.md)
- [documentation-system](skills/documentation-system/SKILL.md)
- [durable-objects](skills/durable-objects/SKILL.md)
- [executing-plans](skills/executing-plans/SKILL.md)
- [find-skills](skills/find-skills/SKILL.md)
- [finishing-a-development-branch](skills/finishing-a-development-branch/SKILL.md)
- [firecrawl](skills/firecrawl/SKILL.md)
- [firecrawl-crawl](skills/firecrawl-crawl/SKILL.md)
- [firecrawl-developer-index](skills/firecrawl-developer-index/SKILL.md)
- [firecrawl-map](skills/firecrawl-map/SKILL.md)
- [firecrawl-parse](skills/firecrawl-parse/SKILL.md)
- [firecrawl-scrape](skills/firecrawl-scrape/SKILL.md)
- [firecrawl-search](skills/firecrawl-search/SKILL.md)
- [freelance-business-development](skills/freelance-business-development/SKILL.md)
- [freelance-client-delivery](skills/freelance-client-delivery/SKILL.md)
- [freelance-lead-gen](skills/freelance-lead-gen/SKILL.md)
- [freelance-operator](skills/freelance-operator/SKILL.md)
- [freelance-product-lead](skills/freelance-product-lead/SKILL.md)
- [frontend-craft](skills/frontend-craft/SKILL.md)
- [frontend-design](skills/frontend-design/SKILL.md)
- [goal](skills/goal/SKILL.md)
- [grill-me](skills/grill-me/SKILL.md)
- [gsoc-strategist](skills/gsoc-strategist/SKILL.md)
- [handoff](skills/handoff/SKILL.md)
- [implementation-strategy](skills/implementation-strategy/SKILL.md)
- [insforge](skills/insforge/SKILL.md)
- [insforge-cli](skills/insforge-cli/SKILL.md)
- [insforge-debug](skills/insforge-debug/SKILL.md)
- [insforge-integrations](skills/insforge-integrations/SKILL.md)
- [interaction-motion](skills/interaction-motion/SKILL.md)
- [large-codebase-navigator](skills/large-codebase-navigator/SKILL.md)
- [launch-readiness](skills/launch-readiness/SKILL.md)
- [llm-release-gate](skills/llm-release-gate/SKILL.md)
- [mcp-builder](skills/mcp-builder/SKILL.md)
- [nextjs-on-cloudflare](skills/nextjs-on-cloudflare/SKILL.md)
- [oss-backend](skills/oss-backend/SKILL.md)
- [oss-contributor](skills/oss-contributor/SKILL.md)
- [oss-database](skills/oss-database/SKILL.md)
- [oss-devops-server](skills/oss-devops-server/SKILL.md)
- [oss-issue-scout](skills/oss-issue-scout/SKILL.md)
- [oss-security](skills/oss-security/SKILL.md)
- [oss-senior-engineer](skills/oss-senior-engineer/SKILL.md)
- [oss-system-designer](skills/oss-system-designer/SKILL.md)
- [oss-uiux-frontend](skills/oss-uiux-frontend/SKILL.md)
- [project-kickoff](skills/project-kickoff/SKILL.md)
- [rea](skills/rea/SKILL.md)
- [receiving-code-review](skills/receiving-code-review/SKILL.md)
- [requesting-code-review](skills/requesting-code-review/SKILL.md)
- [research](skills/research/SKILL.md)
- [reverse-engineer-anything](skills/reverse-engineer-anything/SKILL.md)
- [senior-dev-os](skills/senior-dev-os/SKILL.md)
- [skill-creator](skills/skill-creator/SKILL.md)
- [stop-slop](skills/stop-slop/SKILL.md)
- [subagent-driven-development](skills/subagent-driven-development/SKILL.md)
- [subagents](skills/subagents/SKILL.md)
- [systematic-debugging](skills/systematic-debugging/SKILL.md)
- [test-driven-development](skills/test-driven-development/SKILL.md)
- [testing-strategy](skills/testing-strategy/SKILL.md)
- [understand](skills/understand/SKILL.md)
- [understand-chat](skills/understand-chat/SKILL.md)
- [understand-diff](skills/understand-diff/SKILL.md)
- [understand-explain](skills/understand-explain/SKILL.md)
- [understand-onboard](skills/understand-onboard/SKILL.md)
- [using-git-worktrees](skills/using-git-worktrees/SKILL.md)
- [using-superpowers](skills/using-superpowers/SKILL.md)
- [vault-daydream](skills/vault-daydream/SKILL.md)
- [vercel-composition-patterns](skills/vercel-composition-patterns/SKILL.md)
- [vercel-react-best-practices](skills/vercel-react-best-practices/SKILL.md)
- [verification-before-completion](skills/verification-before-completion/SKILL.md)
- [visual-ui-design](skills/visual-ui-design/SKILL.md)
- [webapp-testing](skills/webapp-testing/SKILL.md)
- [web-design-guidelines](skills/web-design-guidelines/SKILL.md)
- [web-perf](skills/web-perf/SKILL.md)
- [workers-best-practices](skills/workers-best-practices/SKILL.md)
- [wrangler](skills/wrangler/SKILL.md)
- [writing-plans](skills/writing-plans/SKILL.md)
- [writing-skills](skills/writing-skills/SKILL.md)

</details>

## Documentation

- [OpenCode Skills](docs/OpenCode%20Skills.md) — complete reference for all 93 skills, including invocation examples and workflow recipes
- [Design Engineering Skills](docs/Design%20Engineering%20Skills.md)
- [Goal to Execution](docs/Goal%20to%20Execution.md)
- [GSoC Strategy 2027](docs/GSoC%20Strategy%202027.md)
- [OSS and Freelance Skills](docs/OSS%20and%20Freelance%20Skills.md)
- [REA Skill Setup Plan](docs/REA%20Skill%20Setup%20Plan.md)
- [Senior Developer Operating System](docs/Senior%20Developer%20Operating%20System.md)
- [Senior Developer Thinking](docs/Senior%20Developer%20Thinking.md)

Reports and research notes live in [docs/reports](docs/reports) and [docs/research_notes](docs/research_notes).

## Attribution

These are installed copies of publicly available agent skills. Each skill may carry its own license or attribution requirements; review the individual skill and its upstream project before redistributing it.
