# Designing, Reviewing, and Evaluating Agent Skills for AI Engineers

Scope note: "skill" here means a `SKILL.md`-style package (Agent Skills open standard) used to encode AI-engineering workflows — eval harnesses, incident triage, migrations, model/prompt changes, data pipelines — not generic prompt-writing advice. Sources are labelled **[Standard/Docs]** (normative or vendor documentation), **[Research]** (arXiv preprints and benchmarks; several are not peer-reviewed), and **[Practitioner]** (opinion/blog). All URLs accessed 2026-10-23 unless a publication date is given.

Canonical primary sources used throughout:
- Agent Skills specification — https://agentskills.io/specification (standard published 2025-12-18 per https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- Anthropic skill authoring best practices — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Anthropic engineering post, 2025-10-16 — https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- agentskills.io creation guides (best-practices, optimizing-descriptions, evaluating-skills, using-scripts) — https://agentskills.io/skill-creation/best-practices.md etc.
- Claude Code skills docs — https://code.claude.com/docs/en/skills
- OpenCode skills docs (last updated 2026-10-23) — https://opencode.ai/docs/skills/
- OpenAI Codex "Build skills" — https://developers.openai.com/codex/build-skills
- Anthropic `skill-creator` skill (local copy read from `~/.claude/skills/.../skill-creator/SKILL.md`; upstream https://github.com/anthropics/skills/tree/main/skills/skill-creator)

---

## 1. What makes a skill trigger reliably, and how should `name` and `description` be written?

### Takeaway
Triggering is a retrieval problem solved almost entirely by the `description` string, so it should be written as a pushy, imperative "use this when…" statement that names user intents and near-miss boundaries — then validated with a labelled query set, not intuition. Trigger quality degrades with library size faster than context cost does, so precision matters more than coverage as a library grows.

### Cited Findings
- Only `name` + `description` are preloaded into the system prompt at startup; the body loads only after the agent decides the skill is relevant — this metadata is "the first level of progressive disclosure." — [Anthropic engineering, 2025-10-16](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- `name`: max 64 chars, lowercase letters/numbers/hyphens only, no leading/trailing hyphen, no consecutive hyphens, must match parent directory, no XML tags, no reserved words "anthropic"/"claude". `description`: non-empty, max 1,024 chars, no XML tags. — [Agent Skills spec](https://agentskills.io/specification); [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Anthropic recommends third-person voice for `description` ("Processes Excel files…", not "I can help you…") because the field is injected into the system prompt and inconsistent point of view causes discovery problems. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Anthropic recommends gerund-form names (`processing-pdfs`, `analyzing-spreadsheets`) and explicitly lists vague names (`helper`, `utils`, `tools`, `documents`, `data`) as anti-patterns. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Anthropic's own guidance contradicts itself slightly on voice: best-practices says third person, while agentskills.io says "use imperative phrasing… 'Use this skill when…' rather than 'This skill does…'". The reconcilable rule: third-person subject, imperative trigger clause (`description: Extracts X. Use when the user…`). — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices); [agentskills.io optimizing descriptions](https://agentskills.io/skill-creation/optimizing-descriptions.md)
- Triggering has a floor: agents only consult skills for tasks needing knowledge beyond their baseline, so "read this PDF" may never trigger a PDF skill even with a perfect description; eval queries must be substantive. — [agentskills.io optimizing descriptions](https://agentskills.io/skill-creation/optimizing-descriptions.md); [skill-creator SKILL.md](https://github.com/anthropics/skills/tree/main/skills/skill-creator)
- Anthropic instructs skill authors to deliberately make descriptions "a little bit pushy" because Claude "has a tendency to undertrigger skills," e.g. "…even if they don't explicitly ask for a 'dashboard.'" — [skill-creator SKILL.md](https://github.com/anthropics/skills/tree/main/skills/skill-creator)
- Recommended trigger-eval design: ~20 realistic queries (8–10 should-trigger, 8–10 should-not), 3 runs each, pass if trigger rate >0.5; negatives should be *near misses* sharing keywords, not obviously irrelevant prompts; 60/40 train/validation split; ~5 optimization iterations; select by validation score. — [agentskills.io optimizing descriptions](https://agentskills.io/skill-creation/optimizing-descriptions.md)
- Codex front-loads trigger words because it shortens descriptions first when many skills are installed; its initial skill list is capped at 2% of the context window or 8,000 characters, configurable to 10,000 tokens, and skills may be omitted entirely with a warning. — [OpenAI Codex Build skills](https://developers.openai.com/codex/build-skills)
- Claude Code concatenates `description` + optional `when_to_use` and truncates the listing at 1,536 characters, so the key use case must come first. — [Claude Code skills docs](https://code.claude.com/docs/en/skills)
- OpenCode lists skills inside the `skill` tool description and lets a skill opt out of model-facing selection with `metadata["opencode/autoinvoke"]="false"`, while remaining callable by exact name. — [OpenCode skills docs](https://opencode.ai/docs/skills/)
- **Scale effect:** growing a library from a small helpful set to 202 skills degraded pass rate by up to 21%, and the dominant cause was *skill shadowing* (wrong-skill selection), not context overhead (whose effect was statistically indistinguishable from zero). — [More Skills, Worse Agents? (arXiv 2605.24050)](https://arxiv.org/html/2605.24050)
- **Routing collapse:** with 1,000 irrelevant skills installed, loaded-skill recall fell from 73.6% to 27.4% and the zero-load rate rose from 9.3% to 51.6%; masking the irrelevant descriptions largely restored loading, and explicit preselection retained 73.9% recall. — [Lost in Implicit Routing (arXiv 2610.18522, 2026-10-13)](https://arxiv.org/html/2610.18522)
- Practitioners report the same failure from a different angle: descriptions that look plausible but adjacent ("skills for every tool in the monorepo") dilute selection, and a "router skill" whose sub-skills also sit at top level doubles the discovery cost instead of hiding it. — [Xavier Chanthavong, "Context Should Be Lazy," 2026-05-14](https://xavierchanth.com/posts/context-should-be-lazy) [Practitioner]

### Inferences
- Write the description as a *classifier specification*: (a) capability in one clause, (b) "Use when…" with 3–6 concrete user-intent phrases including non-jargon paraphrases, (c) an explicit boundary ("Do not use for X; use Y"), (d) front-load the highest-signal terms for hosts that truncate.
- Precision beats breadth past ~30–50 skills. The research implies a hard curation budget: each additional skill taxes every other skill's selection probability, so a library should be periodically consolidated (one skill with `references/` branches) rather than one-skill-per-tool.
- Because trigger evals are cheap relative to task evals, treat them as a required CI gate for any shared skill library; a description change is a behavioural change and should be diffed like code.
- `name` is a human interface (slash command / `$`-mention / `@` pick) as much as a model interface; gerund names read better in a `/` menu but verb-first names (`fix-ci`) are more scannable. Consistency across a collection matters more than which convention you pick.

### Gaps
- No vendor documents a numeric target for "how many skills is too many"; the 202/1,000-skill thresholds come from preprints using specific benchmarks (SkillsBench-derived), so they are directional, not universal.
- No public data on how trigger accuracy differs between explicit invocation hosts (Claude Code `/name`, Codex `$name`) and pure implicit selection at equal library size.

---

## 2. When should content live in `SKILL.md` versus `references/`, `scripts/`, or `assets/`? What is the right level of progressive disclosure?

### Takeaway
`SKILL.md` is an always-loaded routing document: keep it to the decisions, gotchas, and workflow spine that apply on *every* invocation, and push anything conditional into one-hop `references/`, deterministic computation into `scripts/`, and output-shaped material into `assets/`. The failure mode is not "too little documentation" but mandatory text that is paid for on every run.

### Cited Findings
- Three-level model: metadata ~100 tokens always loaded; `SKILL.md` body recommended **<5,000 tokens / <500 lines**; bundled resources loaded only when needed, effectively unbounded because code can execute without being read into context. — [Agent Skills spec](https://agentskills.io/specification); [Anthropic engineering](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- Microsoft's implementation describes a four-stage variant (advertise → load → read resource → run script) and advertises `read_skill_resource` / `run_skill_script` only when at least one skill actually has them. — [Microsoft Learn, 2026-10-15](https://learn.microsoft.com/en-us/agent-framework/agents/skills)
- Canonical directory convention: `scripts/` (executable), `references/` (docs, e.g. `REFERENCE.md`, domain files), `assets/` (templates, images, data). — [Agent Skills spec](https://agentskills.io/specification)
- Anthropic's four structural patterns: (1) high-level guide + reference files, (2) domain-organized references (`reference/finance.md`, `sales.md`), (3) conditional details (`REDLINING.md`, `OOXML.md`), (4) deep-nesting avoidance. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- **One hop only:** references nested inside references cause partial reads (`head -100`) and incomplete information; every reference file should be linked directly from `SKILL.md`. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Reference files >100 lines should start with a table of contents so an agent previewing the head still sees scope. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Load triggers must be *conditional and specific*: "Read `references/api-errors.md` if the API returns a non-200 status code" beats "see references/ for details." — [agentskills.io best practices](https://agentskills.io/skill-creation/best-practices.md)
- Name reference files for content (`form_validation_rules.md`), not ordinals (`doc2.md`); organize by domain, not by file number. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Claude Code notes that a loaded skill body **stays in context across turns**, making every line a recurring token cost, and distinguishes "reference content" (knowledge applied inline) from "task content" (step-by-step action, often better as an explicit `/skill` with `disable-model-invocation: true`). — [Claude Code skills docs](https://code.claude.com/docs/en/skills)
- **Empirical cost evidence:** of 182 skill-induced efficiency regressions, "Excessive Procedure" dominated with 114 cases (62.6%) — chiefly excessive verification (67) and heavy implementation pipelines (30); where context overhead was the cause, 43 of 46 cases came from mandatory `SKILL.md` body text, not optional references. — [An Empirical Study of Skill-Induced Failures (arXiv 2608.11888, 2026-08-12)](https://arxiv.org/html/2608.11888v1)
- The same study recommends "shorten mandatory skill bodies and lazy-load optional references only when the task actually requires it." — [arXiv 2608.11888](https://arxiv.org/html/2608.11888v1)
- Comunity synthesis of early skill research: tasks with 2–3 skills showed the largest gains, 4+ skills much smaller gains, and "comprehensive" skill documentation sometimes underperformed no skills at all. — [SpecOps summary, 2026-02-24](https://spec-ops.ai/blog/posts/skills-research/) [Practitioner summarising research]

### Inferences
- A workable split rule: if content is needed on ≥80% of invocations, it belongs in `SKILL.md`; if it is needed for a recognizable branch, it belongs in a named reference with the branch condition stated inline; if it is a computation or a format, it belongs in a script or asset and should never be pasted into the body.
- `SKILL.md` should read like an index plus the non-obvious judgments — Anthropic's "gotchas" section is the highest-value body content precisely because it cannot be lazily loaded (an agent won't know to look it up).
- The 500-line/5k-token limit is a proxy for "how much can be mandatory before it degrades execution." Treat it as a ceiling, not a target; the research suggests the real budget is closer to a few hundred lines of decisions.
- Assets are underused in AI-engineering skills: golden output files, schemas, and eval fixtures belong in `assets/` where they are diffable and reusable, not embedded as fenced code.

### Gaps
- No source quantifies the marginal quality loss per 1,000 tokens of mandatory body text; the 43/46 finding is about *whether* overhead caused regressions, not a dose-response curve.
- No documented guidance on how hosts handle very large `assets/` (e.g., 100 MB fixtures) or whether asset reads count against tool-output truncation limits.

---

## 3. When should a skill use deterministic scripts versus instructions? How should errors, idempotency, and cross-platform behaviour be handled?

### Takeaway
Use prose for judgment and scripts for anything with a correct answer that must be reproduced identically — and design scripts as non-interactive CLIs with typed flags, teaching error messages, structured stdout, idempotent semantics, and dry-run/confirm gates. "Solve, don't defer": a script that surfaces a raw exception has moved work back onto the model.

### Cited Findings
- "Many applications require the deterministic reliability that only code can provide"; a bundled script can run **without being loaded into context**, so only its output costs tokens. — [Anthropic engineering](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- Degrees-of-freedom model: high freedom (prose) when multiple approaches are valid; medium (parameterised pseudocode/templates) when a preferred pattern exists; low freedom (exact command, "do not modify the command or add flags") when operations are fragile or order-critical. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices); [agentskills.io best practices](https://agentskills.io/skill-creation/best-practices.md)
- "Solve, don't defer": handle `FileNotFoundError`/`PermissionError` inside the script with a fallback or an actionable message instead of letting the agent improvise. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Avoid "voodoo constants": every timeout/retry value must carry a comment explaining why (Ousterhout's law cited by name). — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Execution intent must be unambiguous: "Run `analyze_form.py`" vs "See `analyze_form.py` for the algorithm" — otherwise agents read scripts they should execute, or execute scripts they should read. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Interactive prompts are a **hard blocker**: agents run non-interactive shells, so a TTY prompt hangs indefinitely; all input must come via flags, env vars, or stdin, with a clear "required flag + options + usage" error when missing. — [agentskills.io using scripts](https://agentskills.io/skill-creation/using-scripts.md)
- `--help` is "the primary way an agent learns your script's interface"; keep it concise because it enters the context window. — [agentskills.io using scripts](https://agentskills.io/skill-creation/using-scripts.md)
- Error messages shape the next attempt: state what was wrong, what was expected, and what to try ("`--format` must be one of: json, csv, table. Received: "xml""). — [agentskills.io using scripts](https://agentskills.io/skill-creation/using-scripts.md)
- Structured output on stdout, diagnostics on stderr; JSON/CSV/TSV so both agent and `jq`/`cut` can consume it. — [agentskills.io using scripts](https://agentskills.io/skill-creation/using-scripts.md)
- Explicit agentic-design checklist: idempotency ("create if not exists"), reject ambiguous input, `--dry-run` for stateful/destructive ops, meaningful distinct exit codes documented in `--help`, safe defaults requiring `--confirm`/`--force`, and **predictable output size** because harnesses truncate around 10–30K characters. — [agentskills.io using scripts](https://agentskills.io/skill-creation/using-scripts.md)
- Pin versions in one-off commands (`npx eslint@9.0.0`, `uvx ruff@0.8.0`) and declare prerequisites in `compatibility` (max 500 chars) rather than assuming the environment. — [agentskills.io using scripts](https://agentskills.io/skill-creation/using-scripts.md); [spec](https://agentskills.io/specification)
- Self-contained dependency declarations: PEP 723 inline metadata for Python (`uv run script.py`), `npm:`/`jsr:` specifiers for Deno, auto-install for Bun, `bundler/inline` for Ruby; `uv lock --script` for reproducibility. — [agentskills.io using scripts](https://agentskills.io/skill-creation/using-scripts.md)
- Platform asymmetry is real: claude.ai can install from npm/PyPI/GitHub, while the Claude API "has no network access and no runtime package installation" — dependency-bearing skills must state and check this. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Cross-platform path rule: always forward slashes (`scripts/helper.py`), never `scripts\helper.py`, even on Windows. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Plan-validate-execute: write an intermediate `changes.json`, validate it against a source of truth with a script, then execute; validation errors should enumerate valid options so the agent self-corrects. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices); [agentskills.io best practices](https://agentskills.io/skill-creation/best-practices.md)
- Host-level execution controls: Claude Code supports `` !`command` `` dynamic context injection, a `shell: bash|powershell` selector, `allowed-tools`/`disallowed-tools` (grant clears at the next user message), and `context: fork` to run the skill in a subagent. — [Claude Code skills docs](https://code.claude.com/docs/en/skills)
- MCP tools referenced from skills should use fully qualified `ServerName:tool_name` to avoid "tool not found." — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

### Inferences
- The decision rule that generalises: **script** when the operation is (a) repeated across invocations, (b) mechanically checkable, (c) slow or token-expensive to re-derive, or (d) safety-critical; **prose** when the value is judgment, prioritisation, or adapting to context. Mixed skills should mark each step's mode explicitly.
- Idempotency is not just a retry concern — it is what makes an agent's explore/retry loop safe. Any step that mutates external state should be resumable and should report what it did (`created`/`skipped`/`updated`).
- Cross-platform reality for AI-engineering skills means three things beyond slashes: avoid assuming `bash`, avoid GNU-only flags, and avoid absolute paths. Python (via `uv run`) is the most portable default; PowerShell-awareness matters for Windows-first teams.
- Because tool output can be truncated, scripts that emit unbounded logs (test runners, `git log`, model eval dumps) should default to summarized output plus `--offset`/`--output` escape hatches. This is a frequent silent failure in CI-style skills.
- `compatibility` + a preflight check in step 0 ("verify `uv`, `docker`, and `gh` are on PATH; stop and report if not") is more robust than hoping the agent infers missing tooling from a stack trace.

### Gaps
- No vendor guidance on script *testing* (unit tests for bundled scripts); skill-creator's eval loop tests outputs, not script internals.
- No documented standard for sandboxing scripts or restricting network egress from a skill's scripts (host-dependent).
- Sparse evidence on Windows-specific skill failures; Anthropic's only explicit statement is the forward-slash rule.

---

## 4. How should a skill be tested — trigger evals, task-success evals, regression tests, human review, A/B comparisons?

### Takeaway
Treat a skill as a change to model behaviour and test it like one: baseline against no-skill (or previous version), run in clean contexts, grade with objective assertions plus human review, and report deltas in pass rate *and* cost. Add trigger evals as a separate, cheaper gate, and never rely on task success alone — it hides routing failure.

### Cited Findings
- Eval-driven development order: (1) run representative tasks without the skill and record failures, (2) write **three** scenarios, (3) establish baseline, (4) write minimal instructions to pass them, (5) iterate. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Anthropic explicitly states there is "not currently a built-in way to run these evaluations" (docs page, accessed 2026-10-23) and that "evaluations are your source of truth." — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Test across the model tiers you deploy: Haiku may need more guidance, Opus may be over-explained to; "what works perfectly for Opus might need more detail for Haiku." — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Two-instance authoring loop: Claude A drafts/refines the skill, Claude B (fresh context) executes real tasks; the human feeds B's failures back to A. Observed failure modes to watch: unexpected exploration paths, missed references, overreliance on one section, ignored bundled files. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Eval case schema: `prompt`, `expected_output`, optional `files`, plus `assertions`; store in `evals/evals.json`. Recommended start is 2–3 cases with varied phrasing, at least one boundary case. — [agentskills.io evaluating skills](https://agentskills.io/skill-creation/evaluating-skills.md)
- Run each case twice — `with_skill/` and `without_skill/` (or `old_skill/` from a pre-edit snapshot) — in **clean contexts** (subagent per run) so only `SKILL.md` shapes behaviour; record `timing.json` (`total_tokens`, `duration_ms`) because the notification is the only place that data appears. — [agentskills.io evaluating skills](https://agentskills.io/skill-creation/evaluating-skills.md); [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)
- Assertion quality bar: objectively verifiable, specific, countable ("output file is valid JSON", "chart has labeled axes", "at least 3 recommendations"); avoid vague ("output is good") and brittle exact-phrase checks. Mechanical checks should be scripts, not LLM judgment. — [agentskills.io evaluating skills](https://agentskills.io/skill-creation/evaluating-skills.md)
- Grading discipline: a PASS requires concrete evidence quoted from the output; a section titled "Summary" containing one vague sentence is a FAIL. Review the assertions themselves for always-pass / always-fail / unverifiable. — [agentskills.io evaluating skills](https://agentskills.io/skill-creation/evaluating-skills.md)
- Blind A/B comparison: give two outputs to an independent judge without revealing which version produced them, scored on a holistic rubric — complements assertion grading when both pass all assertions but differ in polish. — [agentskills.io evaluating skills](https://agentskills.io/skill-creation/evaluating-skills.md); [skill-creator `agents/comparator.md`](https://github.com/anthropics/skills/tree/main/skills/skill-creator)
- Benchmark aggregation includes `delta` for pass rate, seconds, and tokens, with the explicit trade-off framing: "+13 s for +50 pp is probably worth it; 2× tokens for +2 pp might not be." — [agentskills.io evaluating skills](https://agentskills.io/skill-creation/evaluating-skills.md)
- Diagnostic heuristics: assertions that always pass in both configurations are non-discriminating and should be removed/replaced; always-fail assertions indicate a broken assertion, an over-hard case, or a wrong check; high `stddev` across runs signals flakiness or ambiguous instructions. — [agentskills.io evaluating skills](https://agentskills.io/skill-creation/evaluating-skills.md)
- Human review remains necessary for qualities that don't decompose into pass/fail (style, design, "misses the point"); record item-level feedback ("chart is missing axis labels"), where empty feedback means acceptable. — [agentskills.io evaluating skills](https://agentskills.io/skill-creation/evaluating-skills.md)
- skill-creator operationalises all of this: per-case folders with `prompt.md`, `case.yaml`, `graders/`, `files/`; iterations in `<skill>-workspace/iteration-N/`; `with_skill/run-k/` directories; `benchmark.json`/`benchmark.md` via `python -m scripts.aggregate_benchmark`; HTML review viewer; the layout is what `claude plugin eval` reads so the same tests can run in CI. — [skill-creator SKILL.md](https://github.com/anthropics/skills/tree/main/skills/skill-creator)
- Claude Code ships `/doctor prompt-audit` to flag instructions "written for older models" across prompts, skills, and tool descriptions and propose a diff. — [Claude Code skills docs](https://code.claude.com/docs/en/skills)
- **Benchmark reality check:** SWE-Skills-Bench tested 49 public software-engineering skills — 39 had no measurable impact, 3 made performance worse, 7 improved it; the worst offender increased token use by 451%. — [Every, "The Case Against Skills"](https://every.to/context-window/the-case-against-skills) [Practitioner reporting benchmark results]
- **Metric gap:** end-to-end Pass@3 fell only 51.6% → 38.6% under routing collapse while loaded-skill recall halved, so "task success alone can therefore make a failing skill system look healthy"; the authors recommend reporting loaded-skill recall and zero-load rate alongside task success. — [arXiv 2610.18522](https://arxiv.org/html/2610.18522)
- Failure attribution matters more than aggregate pass rate: 125 functional failures in the study were mostly *topically relevant* skills that caused wrong or omitted implementation (Task-Implementation Fault, 68.8%), not obviously irrelevant skills. — [arXiv 2608.11888](https://arxiv.org/html/2608.11888v1)

### Inferences
- Minimum credible test suite for an AI-engineering skill: (1) ~20 labelled trigger queries × 3 runs, (2) 3–5 task cases with assertions, (3) with/without baseline in clean contexts, (4) token+time delta, (5) one human review pass, (6) one adversarial case (malformed input, missing dependency, permission denial). Anything less is a demo, not a test.
- Regression testing requires versioned fixtures and a pinned model. Because model updates change skill value (see §8), record the model ID and host version in `timing.json`/`benchmark.json` alongside results, or the numbers are not comparable over time.
- The most informative assertion class is "passes with skill, fails without" — those isolate what the skill actually contributes. Publish that subset as the skill's reason to exist; retire the skill when it empties.
- Blind A/B is the right tool for *reviewing* a skill change; assertion deltas are the right tool for *debugging* one. Use both, in that order.
- Because hosts differ in truncation, permission prompts, and skill listing, an eval run is only valid for the host it ran on; cross-host claims need cross-host runs.

### Gaps
- No published, widely adopted conformance suite for Agent Skills (the spec ships `skills-ref validate` for frontmatter only).
- No vendor guidance on statistical power: how many runs per case are needed to distinguish a real improvement from noise. The 3-run convention is presented as pragmatic, not derived.
- No public benchmark specifically for *AI-engineering* skills (eval-writing, incident triage, migration); SWE-Skills-Bench and SkillsBench are the closest proxies.
- Whether LLM-judge grading correlates with expert human grading for skill outputs is unquantified in the sources reviewed.

---

## 5. What are the security risks, and what controls actually help?

### Takeaway
A skill is simultaneously executable code and authoritative instruction, so it sits outside both dependency scanning and prompt-injection defence — and current models remain highly susceptible even when warned. Treat every third-party skill as untrusted code plus untrusted instructions: least-privilege tools, no ambient credentials, reviewable diffs, pinned versions, and human approval for side effects.

### Cited Findings
- Anthropic's own warning: "malicious skills may introduce vulnerabilities… or direct Claude to exfiltrate data and take unintended actions"; install only from trusted sources, audit bundled files, dependencies, and any instruction to contact external network sources. — [Anthropic engineering, 2025-10-16](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- `allowed-tools` is in the spec but flagged **experimental**, and support varies by host — it is not a portable security boundary. — [Agent Skills spec](https://agentskills.io/specification)
- Claude Code: an `allowed-tools` grant still goes through the normal permission flow and clears at the next user message; `disallowed-tools` removes tools while the skill is active; synced (claude.ai) skills get display-text sanitisation and angle-bracket escaping, and in non-cloud sessions their `` ! `` commands and `@` references are **not** executed. — [Claude Code skills docs](https://code.claude.com/docs/en/skills)
- Claude Code `/doctor` audits "unused skills, MCP servers, and plugins compared with their context cost," and `prompt-audit` checks configured instructions for outdated or conflicting content. — [Claude Code skills docs](https://code.claude.com/docs/en/skills)
- OpenCode implements pattern-based skill permissions with `allow` / `deny` / `ask` (`internal-*: deny`, `experimental-*: ask`), per-agent overrides, and `tools.skill: false` to remove the capability entirely. — [OpenCode skills docs](https://opencode.ai/docs/skills/)
- Codex supports `policy.allow_implicit_invocation: false` to require explicit `$skill` invocation, and `[[skills.config]] enabled = false` to disable a skill without deleting it. — [OpenAI Codex Build skills](https://developers.openai.com/codex/build-skills)
- **Skill-Inject** (202 pairs; body-injection threat model) found up to 80% attack success with frontier models, including data exfiltration, destructive actions, and ransomware-like behaviour; contextual injections succeeded 41–79% across models (Claude 41–52%, several Codex models >65%). Authors conclude this is not solvable by scale or input filtering and requires context-aware authorization. — [arXiv 2602.20156](https://arxiv.org/abs/2602.20156)
- The core difficulty is **dual-use instructions**: "share a summary with the team via the collaboration API" is benign for internal docs and exfiltration for credentials; instruction/data separation defences don't apply because skill files are *entirely* instructions. — [arXiv 2602.20156](https://arxiv.org/abs/2602.20156)
- **Early demonstration (2025-10-24):** malicious instructions hidden in long skill files and referenced scripts exfiltrated internal files and passwords, and a benign "Don't ask again" approval carried over to closely related harmful actions, bypassing system-level guardrails. — [arXiv 2510.26328](https://arxiv.org/html/2510.26328)
- **SkillJect** automates poisoning with two channels: payload hidden in an auxiliary helper script, plus a rewritten `SKILL.md` that front-loads the injection and frames the helper as a "mandatory prerequisite or required first step" with a copy-pasteable command. — [arXiv 2602.14211](https://arxiv.org/html/2602.14211v3)
- **DyMalSkill** shows skills that are benign at distribution but are *modified at runtime* by instructions in `SKILL.md`, defeating static analysis; kernel-enforced read-only mounts reduced ASR to zero, while prompt-based and detection defences failed. — [arXiv 2606.16287](https://arxiv.org/html/2606.16287v2)
- **MalSkillBench** (3,944 malicious skills, 703 in-the-wild, 4,000 benign): code injection verifies at 94.5% vs prompt injection at 75.8%; the strongest skill-specific detector reached 98.4% recall on code injection but "collapses on prompt-injection and agent-control attacks"; supply-chain scanners and prompt-injection defences each see only half the artifact. — [arXiv 2606.07131](https://arxiv.org/html/2606.07131)
- **Ecosystem prevalence:** SkillSecurer found latent prompt-injection vulnerabilities in **>17% of popular skills.sh skills** it examined, and triggered real incidents by running some of them. — [arXiv 2609.14079](https://arxiv.org/html/2609.14079)
- **Registry scale:** MalSkills analysed **150,108 skills across 7 public registries**, flagged 620 as potentially malicious, and manually confirmed 400 (responsibly reported). — [MalSkills, ACM](https://dl.acm.org/doi/pdf/10.1145/3832783.3834375)
- **Supply-chain mechanics in practice:** the `skills` CLI installs from arbitrary git URLs, GitHub/GitLab/Azure, or direct archive URLs (10 MiB download / 25 MiB extract / 1,000 file caps), supports pinning to a commit SHA, and collects install telemetry by default (`DISABLE_TELEMETRY=1` to opt out). — [skills.sh CLI docs](https://www.skills.sh/docs/cli); [vercel-labs/skills](https://github.com/vercel-labs/skills/)
- skill-creator encodes a "principle of lack of surprise": skills "must not contain malware, exploit code, or any content that could compromise system security," and contents should not surprise the user given the description. — [skill-creator SKILL.md](https://github.com/anthropics/skills/tree/main/skills/skill-creator)

### Inferences
- The defensible control set, in order of leverage: (1) **provenance + pinning** (commit SHA, reviewed diff, internal mirror); (2) **capability least privilege** (per-skill tool allow/deny, no broad shell, no ambient cloud creds); (3) **egress control** (network deny by default for scripts); (4) **human approval on side effects**, especially anything that writes outside the workspace or sends data; (5) **read-only skill directories at runtime** (DyMalSkill's only effective defence); (6) review of the *pair* (instructions + scripts), since no scanner covers both.
- "Don't ask again" / blanket approval is a genuine vulnerability amplifier, not a convenience: it converts one legitimate approval into standing authority for adjacent actions. Skills should be the last place to grant broad standing permissions.
- Sanitising descriptions protects against formatting impersonation but not against dual-use intent. The residual risk is semantic, so it must be handled by authorization scope rather than text filtering.
- A practical review heuristic for third-party skills: read every `scripts/*` file, grep for network calls (`curl`, `requests`, `fetch`, `http`), env/secret access (`os.environ`, `process.env`, `~/.ssh`, `~/.aws`), writes outside the skill/workspace, `subprocess`/`eval`/`exec`, and any instruction that says "first run…", "always…", or "do not tell the user". SkillJect's front-loaded "prerequisite" framing is the specific pattern to look for.
- For AI-engineering skills that touch model APIs, the skill itself is a place secrets can leak into context (e.g., an example with a real key, or a script that echoes env). Treat skill bodies as publishable artifacts: no tokens, no internal hostnames, no customer data in examples.

### Gaps
- No signed-skill / attestation standard (Sigstore-style) documented for Agent Skills as of Oct 2026; provenance relies on git and registry trust.
- No host-documented sandbox specification for skill scripts (filesystem/network isolation guarantees differ per product and are mostly unspecified).
- Quantitative comparison of defences (allowlists vs egress deny vs read-only mounts vs LLM screening) is scattered across preprints with different threat models; no consensus ranking.
- Little public data on enterprise-scale skill review workflows (who approves, what the review checklist is).

---

## 6. What are the most common anti-patterns?

### Takeaway
The dominant anti-patterns are not formatting mistakes but *economic* ones: mandatory text that doesn't change behaviour, procedures that force unnecessary work, and descriptions that compete with their neighbours. Most bad skills are over-documented, over-prescriptive, and untested.

### Cited Findings
- **Giant skill / over-documentation:** "overly comprehensive skills can hurt more than they help — the agent struggles to extract what's relevant and may pursue unproductive paths triggered by instructions that don't apply"; concise stepwise guidance with a working example outperforms exhaustive docs. — [agentskills.io best practices](https://agentskills.io/skill-creation/best-practices.md)
- **Vague description:** `description: Helps with documents` / `Processes data` / `Does stuff with files` are called out explicitly; the description must let the agent choose among "100+ available Skills." — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- **Vague names:** `helper`, `utils`, `tools`, `documents`, `data`, `files`; reserved words; inconsistent patterns across a collection. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- **Menu of options:** listing pypdf/pdfplumber/PyMuPDF/pdf2image as equal choices is labelled a bad example; provide a default plus an escape hatch. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices); [agentskills.io best practices](https://agentskills.io/skill-creation/best-practices.md)
- **Deep nesting:** references inside references cause partial reads and incomplete information. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- **Time-sensitive content:** "If you're doing this before August 2025…" rots; move to an "Old patterns" `<details>` block. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- **Duplicated / drifting docs:** Claude Code's `/doctor` explicitly detects "local `CLAUDE.md` files that duplicate checked-in ones" and offers to migrate always-loaded guidance into on-demand skills — evidence that duplication is a recognised failure mode. — [Claude Code skills docs](https://code.claude.com/docs/en/skills)
- **Brittle scripts:** assuming packages are installed ("Use the pdf library" is a bad example), unpinned one-off commands, interactive prompts that hang, raw exceptions, magic constants. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices); [agentskills.io using scripts](https://agentskills.io/skill-creation/using-scripts.md)
- **Over-automation / excessive procedure:** 114 of 182 efficiency regressions came from "Excessive Procedure," with excessive verification (67) and heavy implementation pipelines (30) as the largest sources — "skills often turn validation checklists and construction recipes into mandatory work." — [arXiv 2608.11888](https://arxiv.org/html/2608.11888v1)
- **Context bloat:** 43 of 46 context-overhead regressions traced to mandatory body text, not optional references. — [arXiv 2608.11888](https://arxiv.org/html/2608.11888v1)
- **Too many skills:** skill shadowing degrades selection as libraries grow (up to 21% drop at 202-skill scale); routing collapse at 1,000 distractors. — [arXiv 2605.24050](https://arxiv.org/html/2605.24050); [arXiv 2610.18522](https://arxiv.org/html/2610.18522)
- **LLM-generated skills without domain grounding:** asking a model to write a skill from general training knowledge yields "vague, generic procedures ('handle errors appropriately')" rather than specific API patterns and conventions. — [agentskills.io best practices](https://agentskills.io/skill-creation/best-practices.md)
- **Self-generated skills underperform:** models asked to generate their own skills saw performance drop 1.3%; 4+ skills reduced gains to 5.9 pp vs ~18 pp with 2–3 skills. — [AI with Mike, 2026-04-14](https://aiwithmike.substack.com/p/anthropics-revolution-on-trial-do) [Practitioner summarising research]
- **Rigid MUST/ALWAYS style:** "If you find yourself writing ALWAYS or NEVER in all caps, or using super rigid structures, that's a yellow flag" — reframe with the reasoning instead. — [skill-creator SKILL.md](https://github.com/anthropics/skills/tree/main/skills/skill-creator)
- **Router-skill anti-pattern:** a router skill whose sub-skills are also top-level skills pays the discovery cost twice (sub-skill descriptions can exceed the router's own), defeating the router's purpose. — [Xavier Chanthavong, 2026-05-14](https://xavierchanth.com/posts/context-should-be-lazy) [Practitioner]
- **Skills as status symbols:** "sprawling custom skill libraries are treated as status symbols"; the recommendation is that "every skill should earn its place in your library with proof it improves outcomes." — [Every, "The Case Against Skills"](https://every.to/context-window/the-case-against-skills) [Practitioner]

### Inferences
- Ranked by expected damage: (1) no eval / no baseline, (2) over-broad or vague description at library scale, (3) giant mandatory body, (4) mandatory verification theatre, (5) brittle scripts and unpinned deps, (6) duplicated sources of truth, (7) stale model-era instructions.
- Most anti-patterns are the same mistake in different clothes: encoding *everything the author knows* instead of *the delta the agent needs*. The test "would the agent get this wrong without this instruction?" filters most of them.
- A useful smell test for over-automation: if a step exists mainly to produce evidence that the step was done, cut it or make it conditional.
- Duplication is a maintenance anti-pattern that becomes a correctness anti-pattern: two copies of a procedure diverge, and whichever the agent reads first wins.

### Gaps
- No quantitative ranking of anti-patterns by frequency in the wild (the MalSkills/MalSkillBench datasets measure maliciousness, not quality).
- No published rubric for "acceptable skill length" by task class; the 500-line guidance is uniform across very different skills.

---

## 7. What do excellent skills do that mediocre skills do not?

### Takeaway
Excellent skills encode *non-public, hard-won specifics* — gotchas, defaults, validation gates, and the exact command that works — and prove they help. Mediocre skills restate general best practice, prescribe ceremony, and are never measured.

### Cited Findings
- "The highest-value content in many skills is a list of gotchas — environment-specific facts that defy reasonable assumptions," e.g. soft-deleted rows, `user_id`/`uid`/`accountId` divergence, `/health` vs `/ready`. Gotchas should stay in `SKILL.md` because the agent may not recognise the trigger to load a reference. — [agentskills.io best practices](https://agentskills.io/skill-creation/best-practices.md)
- "Add what the agent lacks, omit what it knows": project conventions, domain procedures, non-obvious edge cases, particular tools/APIs — not what a PDF or HTTP is. — [agentskills.io best practices](https://agentskills.io/skill-creation/best-practices.md); [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- "Favor procedures over declarations": teach how to approach a class of problems ("read schema → join on `_id` → apply filters → aggregate → format") rather than one instance's answer. — [agentskills.io best practices](https://agentskills.io/skill-creation/best-practices.md)
- Grounding beats generation: skills extracted from a real hands-on task (steps that worked, corrections made, I/O formats, context supplied) or synthesised from real artifacts (runbooks, incident reports, API specs, code-review comments, git history) outperform generic best-practice articles. — [agentskills.io best practices](https://agentskills.io/skill-creation/best-practices.md)
- Explain the why: reasoning-based instructions ("Do X because Y tends to cause Z") outperform rigid directives, and models follow instructions more reliably when they understand purpose. — [agentskills.io evaluating skills](https://agentskills.io/skill-creation/evaluating-skills.md); [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)
- Build in a feedback loop (validate → fix → revalidate → only then proceed) and, for batch/destructive work, plan-validate-execute with a machine-checkable intermediate artifact. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices); [agentskills.io best practices](https://agentskills.io/skill-creation/best-practices.md)
- Bundle repeated work: if transcripts show the agent independently rebuilding the same helper (chart builder, parser, validator) across runs, that is the signal to ship a tested script. — [agentskills.io best practices](https://agentskills.io/skill-creation/best-practices.md); [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)
- Read execution traces, not just outputs: wasted steps usually mean vague instructions, inapplicable instructions the agent follows anyway, or too many options without a default. — [agentskills.io best practices](https://agentskills.io/skill-creation/best-practices.md)
- The seven SWE skills that improved outcomes in SWE-Skills-Bench all "provided specialized guidance the model couldn't otherwise supply, like financial-risk formulas or traffic-management instructions." — [Every](https://every.to/context-window/the-case-against-skills) [Practitioner reporting benchmark]
- Precision of load triggers is an excellence marker: naming the exact condition ("if the API returns a non-200") rather than gesturing at a folder. — [agentskills.io best practices](https://agentskills.io/skill-creation/best-practices.md)
- Defaults over menus, with a named escape hatch for the exception. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- One skill = one coherent unit of work that composes; too narrow forces multi-load, too broad can't activate precisely. — [agentskills.io best practices](https://agentskills.io/skill-creation/best-practices.md)

### Inferences
- The excellence test: **delete the skill — what breaks?** If nothing breaks, the skill is decoration. If something breaks, the failing step is the skill's true content and should be the first thing in the body.
- Excellent skills read like a senior engineer's handover note: "here's the trap, here's the command that works, here's how you'll know you're done." Mediocre skills read like a conference talk abstract.
- Preference for private context explains the benchmark results: skills that encode public knowledge are exactly the ones a newer model no longer needs (§8), so durable value concentrates in org-specific facts, exact commands, and verified thresholds.
- Excellent skills are *short but specific*: specificity is expensive in tokens, so it must be spent on the few facts that change behaviour, not on coverage.

### Gaps
- No controlled study isolating which content types (gotchas vs examples vs checklists) contribute most to success; the "gotchas" claim is practitioner consensus plus one vendor guide.
- No data on whether "explain the why" outperforms prescriptive instructions for *skill* bodies specifically (the claim is general prompting guidance).

---

## 8. How should a skill be maintained and versioned as models and platforms change?

### Takeaway
Skills have a shelf life tied to the model generation that needed them, so treat them as versioned, evaluated artifacts with an owner, a pin, and a retirement path. Semantic versioning is not in the spec — the de facto controls are git pins, lockfiles, `metadata.version`, and a recurring re-eval.

### Cited Findings
- The spec has **no `version` field**: optional fields are `license`, `compatibility`, `metadata` (string→string map), and experimental `allowed-tools`; the spec's own example puts `version: "1.0"` under `metadata`, i.e. conventionally, not normatively. — [Agent Skills spec](https://agentskills.io/specification)
- Guidance against time-sensitivity: avoid "before August 2025" style content; preserve history in an "Old patterns" collapsed section so the main body stays current. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Portability is a maintenance constraint: only the six spec fields survive claude.ai upload / Skills API / `package_skill.py`; any Claude Code-only field causes a **hard packaging error** ("Unexpected key(s) in SKILL.md frontmatter"). — [Claude Code skills docs](https://code.claude.com/docs/en/skills)
- Host-specific behaviour must live in `metadata`, not new top-level fields: OpenCode reads `opencode/slash` and `opencode/autoinvoke`; unknown top-level fields are ignored for forward compatibility, and duplicate/miscased recognised fields prevent loading. — [OpenCode skills docs](https://opencode.ai/docs/skills/); [Microsoft Learn](https://learn.microsoft.com/en-us/agent-framework/agents/skills)
- Claude Code reloads changed `SKILL.md` live during a session, but requires `/reload-skills` for a newly created top-level skills directory and `/reload-plugins` for hooks/agents changes. — [Claude Code skills docs](https://code.claude.com/docs/en/skills)
- Synced claude.ai skills are **download-only**: edits under `~/.claude/skills/synced/` are not saved back, and the next sync can overwrite them; changes must be made on claude.ai. — [Claude Code skills docs](https://code.claude.com/docs/en/skills)
- Claude Code `/doctor` audits unused skills against their context cost and offers to migrate always-loaded guidance into on-demand skills; `prompt-audit` flags instructions written for older models and proposes a diff. — [Claude Code skills docs](https://code.claude.com/docs/en/skills)
- Codex enforces a discovery budget: if many skills are installed it shortens descriptions first, may omit skills with a warning, and exposes `skills.max_context_tokens` (up to 10,000) — a platform-level pressure to prune. — [OpenAI Codex Build skills](https://developers.openai.com/codex/build-skills)
- Codex supports disabling without deleting via `[[skills.config]] path=… enabled=false`, and detects skill changes automatically. — [OpenAI Codex Build skills](https://developers.openai.com/codex/build-skills)
- Registry tooling: `npx skills update` updates installed skills; installs can be pinned to a commit SHA; symlink installs (recommended) keep "a single source of truth, easy updates" versus copies. — [skills.sh CLI docs](https://www.skills.sh/docs/cli); [vercel-labs/skills releases](https://github.com/vercel-labs/skills/releases)
- **Shelf-life evidence:** "some of the skills Opus 4.8 needed to avoid mistakes actually harmed the newer model's performance," compared to the GPT-3→GPT-4 transition where prompt hacks became unnecessary; the recommended action is a periodic skills audit — keep private-context skills, retest weakness-compensating skills, retire skills with no demonstrated gain. — [Every, "The Case Against Skills"](https://every.to/context-window/the-case-against-skills) [Practitioner]
- **Test across model tiers on every model upgrade**; Haiku/Sonnet/Opus need different levels of guidance. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Version drift is measurable: skill-induced failures include "environment mismatches" (13 cases) and "wrong artifact locations" (24), i.e. skills that were correct for an older repo/runtime layout. — [arXiv 2608.11888](https://arxiv.org/html/2608.11888v1)
- Library-level maintenance: routing accuracy degrades with library size, and explicit preselection restores it — implying periodic consolidation and pre-filtering are maintenance obligations, not just UI choices. — [arXiv 2610.18522](https://arxiv.org/html/2610.18522); [arXiv 2605.24050](https://arxiv.org/html/2605.24050)

### Inferences
- Practical versioning scheme that works today with the spec as-is: put `version`, `owner`, `reviewed_with` (model IDs), and `last_evaluated` in `metadata`; tag releases in git; pin consumers by commit SHA; keep a `CHANGELOG.md` inside the skill folder for behaviour changes (not just wording).
- Semver semantics can be mapped usefully: MAJOR = when the skill triggers or what it guarantees changes; MINOR = new branch/reference added; PATCH = wording, typo, error-message clarity.
- "Reviewed with model X" is the key metadata: it tells a reviewer whether the skill has been validated against the current frontier model or is legacy compensation.
- Re-eval triggers should be explicit: model version change, host version change, dependency major bump, repo layout change, and any incident where the skill was implicated.
- Consolidation beats proliferation: prefer one skill with `references/<variant>.md` over N sibling skills, because siblings all pay discovery cost and compete for selection.
- Retirement is a feature: a skill that no longer produces a positive delta should be archived (kept in git, removed from the installed set), not silently left to shadow better options.

### Gaps
- No normative versioning/deprecation semantics in the Agent Skills spec; no `deprecated`, `supersedes`, or `min_host_version` field.
- No vendor-published deprecation policy for skills, and no registry-level quality or security signal beyond install counts (skills.sh leaderboard) — which the CLI's own find-skills guidance treats as a proxy, not a guarantee.
- No standard for recording eval provenance (model, host version, date) inside the skill package; this is currently an author convention.
- Unknown how hosts handle a skill whose declared `compatibility` no longer matches (whether they warn, skip, or load anyway) — not documented in the sources reviewed.

---

## Practical checklist (synthesised from the above)

**Definition**
- [ ] The skill encodes knowledge the agent lacks: org conventions, exact commands, verified thresholds, failure modes — not a general tutorial.
- [ ] Scope is one coherent unit of work; you can name what breaks if the skill is deleted.
- [ ] A near-duplicate skill does not already exist (check before creating; merging beats adding).

**Frontmatter**
- [ ] `name` is specific, gerund or verb-first, matches the directory, ≤64 chars, `^[a-z0-9]+(-[a-z0-9]+)*$`.
- [ ] `description` ≤1,024 chars, front-loads the key use case, states *what* + *when*, includes non-jargon paraphrases, and names a boundary ("not for X").
- [ ] Only spec fields at top level (`name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`); host flags go in `metadata`.
- [ ] `compatibility` states runtimes/CLIs/network needs if non-trivial.
- [ ] `metadata` carries `version`, `owner`, `reviewed_with`, `last_evaluated`.

**Body**
- [ ] Under ~500 lines / 5k tokens; ideally a few hundred lines of decisions.
- [ ] Opens with the workflow spine (numbered steps or a copyable checklist), then gotchas, then output contract.
- [ ] Every instruction passes "would the agent get this wrong without it?"
- [ ] One default per decision, with a named escape hatch — no menus.
- [ ] Explains *why* for non-obvious rules; no ALL-CAPS MUST walls.
- [ ] No time-sensitive statements; legacy material in an "Old patterns" block.
- [ ] Consistent terminology; forward slashes only; relative paths from skill root.

**Progressive disclosure**
- [ ] All references are one hop from `SKILL.md`, each with an explicit load condition.
- [ ] Reference files are named for content, domain-split, and have a TOC if >100 lines.
- [ ] Anything conditional, long, or example-shaped is *not* in the mandatory body.
- [ ] `scripts/` are listed with run-vs-read intent stated.

**Scripts**
- [ ] Non-interactive; all input via flags/env/stdin; missing flag produces usage + options.
- [ ] `--help` is accurate, concise, and includes exit codes.
- [ ] Errors say what was wrong, what was expected, what to try.
- [ ] Structured data on stdout; diagnostics on stderr; bounded output with `--offset`/`--output`.
- [ ] Idempotent mutations; `--dry-run` for destructive/stateful ops; `--confirm`/`--force` gates.
- [ ] Dependencies pinned and declared (PEP 723 / `npm:` / etc.) or listed with an install step; no assumption that packages exist.
- [ ] Constants documented; no magic numbers.
- [ ] Works on Windows (no bash-isms, no GNU-only flags, no absolute paths).

**Evaluation**
- [ ] ≥3 task cases (`prompt`, `expected_output`, optional `files`) including one boundary case.
- [ ] With-skill vs without-skill (or previous-version) runs in clean contexts.
- [ ] Objective assertions only; mechanical checks verified by script, not judgment.
- [ ] Pass rate **and** token/time delta recorded, with model + host version.
- [ ] ~20 trigger queries (half near-miss negatives) × 3 runs; train/validation split.
- [ ] One human review pass with item-level feedback; blind A/B for version comparisons.
- [ ] Assertions that always pass in both arms removed as non-discriminating.

**Security**
- [ ] No secrets, internal hostnames, or customer data in body, examples, or scripts.
- [ ] Every network call, env-var read, and write outside the workspace is intentional, documented, and minimal.
- [ ] Tool needs are declared and scoped (`allowed-tools`/`disallowed-tools` or host equivalent); no broad shell where a specific command suffices.
- [ ] Third-party skills: source reviewed file-by-file, pinned to a commit, installed via symlink/mirror, and re-reviewed on update.
- [ ] Skill directories read-only at runtime where the host supports it.
- [ ] No instruction that asks the agent to hide actions from the user or to treat the skill as a "mandatory prerequisite" before unrelated work.

**Maintenance**
- [ ] Owner and re-eval triggers recorded (model bump, host bump, dep major, layout change).
- [ ] Changelog tracks behaviour changes, not just wording.
- [ ] Skill still shows a positive delta on its own evals; otherwise archived.
- [ ] Library audited periodically: duplicates merged, unused skills removed, descriptions de-conflicted.

---

## Short review rubric (1–5 per dimension; ≤2 = request changes)

| Dimension | 1 (failing) | 3 (acceptable) | 5 (excellent) |
|---|---|---|---|
| **Trigger precision** | Vague name/description; would fire on neighbours or never | Clear what + when; untested | Eval-backed trigger rate on 20 labelled queries incl. near misses; explicit boundary |
| **Scope** | Grab-bag of unrelated tasks, or so narrow it needs three siblings | One recognizable job | One coherent unit that composes; deletion has a nameable cost |
| **Context economy** | >500 lines of mandatory prose; duplicated reference material | Under limits, some redundancy | Every mandatory line changes behaviour; conditional material one hop away with load triggers |
| **Instruction quality** | Generic best practice ("handle errors appropriately"); MUST walls | Specific steps, some over-prescription | Gotchas, defaults not menus, reasons given, procedures not one-off answers |
| **Determinism** | Prose for mechanical work; brittle unpinned commands | Some scripts, happy-path only | Scripts for fragile/repeated work; non-interactive, idempotent, dry-run, teaching errors, bounded output |
| **Verifiability** | No success criterion | Assertions exist, not run | Assertions + baseline + delta, plus a validation loop the agent can execute itself |
| **Evidence** | Never evaluated; no baseline | Tried manually a few times | Trigger + task evals, clean-context runs, token/time delta, human review, model IDs recorded |
| **Security** | Unreviewed scripts, broad tools, secrets, unexplained network calls | Trusted source, no secrets | Least-privilege tools, pinned provenance, egress minimized, read-only at runtime, no hidden instructions |
| **Maintainability** | No owner/version; stale API or model references | Version in `metadata`, ad-hoc updates | Owner, changelog, `reviewed_with`, explicit re-eval triggers, retirement criteria, cross-host packaging validated |

Scoring guidance: weight **Trigger precision**, **Evidence**, and **Security** as gates (any 1 blocks adoption regardless of total). A skill scoring 5 on prose quality but 1 on Evidence is a well-written liability — consistent with SWE-Skills-Bench, where most public skills had no measurable effect and some actively harmed performance ([Every](https://every.to/context-window/the-case-against-skills)).
