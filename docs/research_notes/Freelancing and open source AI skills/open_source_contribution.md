# Open-Source Contribution with AI Agents: Skills, Workflows, and Guardrails (as of October 2026)

*Evidence labels used below: **[P]** primary/official project or foundation document; **[R]** peer-reviewed or preprint research; **[S]** secondary reporting/vendor blog/aggregator; **[A]** individual anecdote or forum comment. Dates are given wherever the source is time-sensitive. Two major 2026 data points anchor this note: the Linux Foundation Research survey released 20 Oct 2026, and the AIDev/EASE 2026 empirical studies of agent-authored pull requests.*

## Which agent skills are most useful for real open-source contribution?

### Takeaway
The highest-value skills are not "write code" skills but **repository-context, verification, and review-readiness** skills: reading a repo's conventions, reproducing a bug, writing a failing test, running the project's own checks, and producing a small, explainable diff. Code-generation skill without those is precisely what maintainers describe as the problem.

### Cited Findings
- **[P]** GitHub Copilot code review now consumes repository-specific context from `.github/copilot-instructions.md`, root `AGENTS.md`, path-scoped `.github/instructions/**/*.instructions.md`, and also `CLAUDE.md`, `GEMINI.md`, `REVIEW.md`; it can use agent skills placed in `.github/skills` and MCP servers, and it labels comments High/Medium/Low severity — [GitHub Docs, Copilot code review](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review).
- **[P]** By default Copilot leaves a "Comment" review, not "Approve"/"Request changes"; Copilot approvals that satisfy branch protection are a separately enabled public preview and are off by default — [GitHub Docs](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review). This makes agent review a pre-review filter, not a substitute for human sign-off.
- **[P]** Copilot reads custom instructions, agent instructions, and agent skills **from the PR head branch**, not the base branch, so instruction/skill changes can be tested in the same PR — [GitHub Docs](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review). (Security implication in Inferences.)
- **[P]** The Linux kernel requires an AI-assisted workflow to: read the full process docs, locate the commit, **build a reproducer for any non-trivial bug**, write the fix, build and verify it, pass `checkpatch.pl`, add a `Fixes:` tag, find maintainers with `scripts/get_maintainer.pl`, and explicitly state what could not be built or tested — [Linux kernel "AI Coding Assistants", docs v7.3.0](https://docs.kernel.org/process/coding-assistants.html).
- **[P]** Google Summer of Code 2026 guidance to contributors says the human retains **100% responsibility**, AI is best used for research/learning and "grunt work" (boilerplate, refactors, tests, debugging), and contributors must define test scope themselves; mentors report blind trust and poor guideline adherence as top concerns — [Google Open Source, GSoC AI guidance, updated 2026-02-19](https://developers.google.com/open-source/gsoc/resources/ai_guidance).
- **[P]** Kubernetes documents AI pull-request review tooling as a governed process, with maintainers test-driving tools in `kubernetes-sigs` repos; Copilot was limited because only maintainers could request reviews, while CodeRabbit gave contributors a pre-review quality gate, with a label marking unresolved AI comments — [Kubernetes blog, 26 Jun 2026](https://kubernetes.io/blog/2026/06/26/open-source-maintainership-in-the-age-of-ai/).
- **[S]** The most-starred public skill pack, `addyosmani/agent-skills`, had ~109.6k stars and 11.4k forks at time of access, MIT-licensed, with 25 skills, 9 lifecycle commands, 4 reviewer personas, and 7 checklists; relevant skills include `code-review-and-quality` (five-axis review, ~100-line change sizing, Nit/Optional/FYI severities), `test-driven-development`, `debugging-and-error-recovery`, `security-and-hardening`, `documentation-and-adrs`, `ci-cd-and-automation`, `git-workflow-and-versioning`, `context-engineering`, `source-driven-development`, `doubt-driven-development` (fresh-context adversarial review), and `constraint-driven-development` (explicitly "catches agents silencing checks or skipping tests to get green") — [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills). Star count is a popularity signal, not an efficacy measure.
- **[S]** That pack's stated design pattern is reusable as an evaluation rubric: each skill has a process, trigger conditions, an "anti-rationalization" table of excuses agents use to skip steps, red flags, and **evidence-based exit criteria** ("tests passing, build output, runtime data"), with progressive disclosure to limit tokens — [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills).
- **[R]** An EASE 2026 study of AI-generated PRs using the AIDev dataset found most AI-generated PRs receive **no review at all**, and when reviewed, review is dominated by AI agents rather than humans; human-authored PRs are more likely to get human-only review and direct human feedback, with human involvement in agentic PRs often appearing as "agent steering" — [arXiv:2605.02273, submitted 4 May 2026](https://arxiv.org/abs/2605.02273).
- **[R]** AIDev itself aggregates 932,791 agent-authored PRs from five agents (OpenAI Codex, Devin, GitHub Copilot, Cursor, Claude Code), 116,211 repos, 72,189 developers, with a curated 33,596-PR/2,807-repo subset for repos >100 stars — [arXiv:2602.09185, 9 Feb 2026](https://arxiv.org/abs/2602.09185).

### Inferences
- A practical skill stack for OSS contribution, in priority order: (1) **repo-convention ingestion** (`AGENTS.md`/`CONTRIBUTING.md`/CI config → a constraints file); (2) **bug reproduction and failing-test creation**; (3) **verified implementation** with project-native build/lint/test; (4) **self-review before human review** (five-axis + project checklist); (5) **PR narrative** (what/why/risk/what was not tested); (6) **review-response loop**; (7) **docs/changelog/release-note generation**; (8) **security review** only with reproduction and maintainer-channel discipline.
- Skills that encode *evidence gates* and *anti-rationalization* are more valuable in OSS than skills that encode style opinions, because maintainers' scarce resource is trust, not formatting.
- "Agent reviews agent" is the default failure mode of the current toolchain. A contributor should treat AI review as a filter that reduces obvious defects, never as evidence that a human reviewed the change.
- Because review tooling reads instructions from the PR head branch, a contributor (or attacker) can alter the reviewer's behavior in the same PR. Maintainers should treat changes to `AGENTS.md`, `.github/skills`, and instruction files as security-relevant diffs requiring human review. *(Inference from the documented mechanism.)*

### Gaps
- No public, peer-reviewed head-to-head evaluation of OSS-specific agent skills exists; star counts, vendor benchmarks, and blog comparisons are not evidence of contribution quality.
- No data was found on which specific skills correlate with higher merge rates in real OSS repos.
- The EASE study measures review *activity structure*, not review quality or defect escape rate.

## Which tasks give contributors the highest leverage and the best reception from maintainers?

### Takeaway
The best-received work **reduces maintainer uncertainty per unit of review time**: a confirmed reproducer, a failing-then-passing test, a triaged duplicate, a precise docs fix, or a small patch with CI green. Large "complete" PRs, speculative refactors, and automated vulnerability reports are the worst-received, even when technically correct.

### Cited Findings
- **[P]** Linux Foundation Research (fielded with Red Hat, OpenSSF, LF AI & Data; released 20 Oct 2026) reports 59% of maintainers see growing contribution volume (69% at large projects), 25% of incoming PRs estimated as low-quality "AI slop" (31% at large projects), and 53% of maintainers disagree that GenAI has improved community trust — [LF Research press release, 20 Oct 2026](https://www.prnewswire.com/news-releases/new-lf-research-survey-shows-generative-ai-cuts-open-source-coding-time-in-half-but-25-of-incoming-pull-requests-are-considered-ai-slop-302913843.html); report page: [linuxfoundation.org/research/oss-development-gen-ai-era-2026](https://www.linuxfoundation.org/research/oss-development-gen-ai-era-2026).
- **[P]** The same survey estimates time reductions of 52% for code authoring but only 19% for proposal discussions, and 21% of respondents report *taking more time* on high-complexity tasks — i.e., the leverage is in execution, not in deciding what to build — [LF Research release](https://www.prnewswire.com/news-releases/new-lf-research-survey-shows-generative-ai-cuts-open-source-coding-time-in-half-but-25-of-incoming-pull-requests-are-considered-ai-slop-302913843.html).
- **[P]** The kernel explicitly says unverified reports waste maintainer time: "maintainers currently waste too much time analyzing unverified reports and untested fixes," and an AI assistant must stop if a bug does not reproduce — [Linux kernel docs](https://docs.kernel.org/process/coding-assistants.html).
- **[P]** LLVM's AI policy permits AI with disclosure but **forbids using AI to fix issues labeled "good first issues"**, preserving those as human learning entry points — [LLVM AI Tool Use Policy](https://llvm.org/docs/AIToolPolicy.html), as catalogued in [melissawm/open-source-ai-contribution-policies](https://github.com/melissawm/open-source-ai-contribution-policies).
- **[P]** curl's policy states the golden rule: "a contribution should be worth more to the project than the time it takes to review it, which is usually not the case if large parts of your PR were written by LLMs" — [curl contribution policy](https://curl.se/dev/contribute.html#on-ai-use-in-curl), quoted in the [policy catalogue](https://github.com/melissawm/open-source-ai-contribution-policies).
- **[A]** In GitHub's low-quality-contributions thread, a TypeScript maintainer (RyanCavanaugh) reports colleagues spending "10, 20, 30 minutes" writing explanations for why bot-driven PRs/issues are wrong, and argues per-repo caps fail because bots spread activity across many repos — [GitHub Community #197319, 5 Jun 2026](https://github.com/orgs/community/discussions/197319).
- **[A]** An Azure Core Upstream maintainer summarized six pain points: the review trust model is broken; AI PRs can look structurally fine but be logically wrong or unsafe; line-by-line review does not scale; maintainers are uncomfortable approving code they do not understand; cognitive load now includes judging whether the author understands; and review burden is higher than pre-AI — [GitHub Community #185387, 28 Jan 2026](https://github.com/orgs/community/discussions/185387).
- **[P]** GitHub's Maintainer Month update says it is exploring recognition for non-code contributions — "issue triage, documentation, testing, reproduction steps, design feedback, and community support" — as contributions "just as important to a project's health as writing code" — [GitHub Community #197319, 29 May 2026](https://github.com/orgs/community/discussions/197319).
- **[P]** GSoC mentor guidance recommends AI for boilerplate, refactors, test scaffolding, and debugging, but not for core logic, with the contributor defining test scope — [GSoC AI guidance](https://developers.google.com/open-source/gsoc/resources/ai_guidance).
- **[R]** AIDev shows agentic PRs are numerous but mostly unreviewed; volume is not the same as accepted contribution — [arXiv:2602.09185](https://arxiv.org/abs/2602.09185); review structure findings in [arXiv:2605.02273](https://arxiv.org/abs/2605.02273).

### Inferences
- Highest-leverage, best-received task ranking (my synthesis): (1) **reproduce and minimally fix a confirmed bug** with a regression test; (2) **add missing tests** to an existing behavior, with the maintainer's preferred test style; (3) **triage**: dedupe issues, confirm versions/environments, bisect; (4) **docs/examples/changelog** corrections tied to a released behavior; (5) **CI/dependency/tooling maintenance** that reduces maintainer toil; (6) **small, well-scoped features** that were discussed and agreed first; (7) **security fixes** only through private channels with a reproducer.
- The unit of contribution that wins is the **"reviewable unit"**: one concern, a clear before/after, a test that fails before and passes after, and an explicit statement of residual risk.
- Tasks that touch onboarding ("good first issue"), mass refactors, formatting-only churn, or speculative architecture are low-reception even when correct, because they consume review attention without reducing uncertainty.
- Because proposal discussion is only ~19% faster with AI, agents should not be used to invent scope; scope should be agreed with maintainers in an issue first.

### Gaps
- No public dataset was found that ranks *task types* by merge rate or maintainer satisfaction for agent-assisted PRs. The ranking above is inference from maintainer statements, not measured preference.
- No reliable data on how often AI-assisted docs/changelog PRs are accepted versus code PRs.
- LF Research's full report was not read (only the release summary); sampling method and margin of error are unknown.

## Which open-source projects or ecosystems are especially agent-friendly?

### Takeaway
"Agent-friendly" correlates with **explicit written policy + a disclosure/attribution convention + strong CI + maintainer capacity to review**, not with enthusiasm about AI. Kubernetes, the Apache ecosystem, the Linux kernel, Fedora, Mozilla Firefox, Rust, and several Python/scientific projects have workable policies; Zig, Godot, QEMU, OpenJDK, NetBSD (approval-gated), Servo, and many GNOME apps are closed or effectively closed.

### Cited Findings
- **[P]** Kubernetes has an AI policy and contributor guidance; its policy allows `Assisted-by:` but **not** `Co-developed-by:` for AI, requires disclosure and a human in the loop — [Kubernetes AI guidance](https://www.kubernetes.dev/docs/guide/pull-requests/#ai-guidance), summarized in the [policy catalogue](https://github.com/melissawm/open-source-ai-contribution-policies). Kubernetes also published a governance process for adopting AI code-review tools — [Kubernetes blog, 26 Jun 2026](https://kubernetes.io/blog/2026/06/26/open-source-maintainership-in-the-age-of-ai/).
- **[P]** CNCF provides GitHub Copilot access to maintainers, which seeded adoption of AI review in Kubernetes SIGs; the stated next steps are "AI skills to reduce maintainer burnout," "AI assisted triage of failing tests," and "skills to aid the operational aspects of Kubernetes" — [Kubernetes blog](https://kubernetes.io/blog/2026/06/26/open-source-maintainership-in-the-age-of-ai/).
- **[P]** The Apache Software Foundation published generative-tooling guidance (current August 2026) requiring contributors to ensure tool terms permit open-source licensing, to meet one of three provenance conditions, and recommending `Generated-by: <Tool> <Version>` or `Co-authored-by:` trailers; it notes ICLA §7 is "not a practical route" for AI output because source details are generally unknowable — [ASF Generative Tooling Guidance](https://www.apache.org/legal/generative-tooling.html).
- **[P]** ASF project-level policies vary: Apache Airflow allows Gen-AI-assisted contributions with disclosure and human-in-the-loop and added Copilot review instructions to catch AI-slop PRs; Apache DataFusion explicitly offers "better ways to contribute than an AI dump"; Apache CouchDB and PouchDB disallow AI — [policy catalogue](https://github.com/melissawm/open-source-ai-contribution-policies).
- **[P]** The Linux kernel permits AI-assisted contributions but requires human DCO sign-off, `Assisted-by:` attribution, reproduction, build/test evidence, and GPL-2.0-only compatibility — [Linux kernel docs](https://docs.kernel.org/process/coding-assistants.html).
- **[P]** Rust adopted an LLM usage policy (announced 5 Aug 2026); Fedora has an AI-assisted contributions policy; Mozilla Firefox has an AI coding policy; OpenInfra requires `Assisted-by:`/`Generated-by:`; EasyBuild requires naming specific models/tools — [policy catalogue](https://github.com/melissawm/open-source-ai-contribution-policies) with links to each project policy.
- **[P]** Python/scientific ecosystem policies are comparatively mature and disclosure-oriented: CPython, NumPy, SciPy, pandas, scikit-learn, scikit-image, matplotlib, Astropy, napari, pytest, PyTorch, xarray, Sphinx, and others have written policies; several forbid AI `Co-authored-by:` trailers or require a human in the loop — [policy catalogue](https://github.com/melissawm/open-source-ai-contribution-policies).
- **[P]** Closed or highly restricted examples: Zig ("strict no LLM/no AI"), Godot (no AI-assisted contributions after a 2026 policy change), QEMU (no AI-generated content), OpenJDK (interim no), NetBSD (explicit core approval), Servo (no), Asahi Linux (no), Gentoo (no), and multiple GNOME apps (libadwaita, GIMP, Loupe) — [policy catalogue](https://github.com/melissawm/open-source-ai-contribution-policies); Godot's own announcement: [Contribution policy 2026](https://godotengine.org/article/contribution-policy-2026/).
- **[P]** LLVM is a middle case: AI is allowed with disclosure, but AI on "good first issues" is forbidden — [LLVM AI Tool Use Policy](https://llvm.org/docs/AIToolPolicy.html).
- **[S]** The curated policy list had 316 stars, 44 forks, and 98 commits at time of access, and is maintained with community PRs; it explicitly warns its own classification columns are "in many cases, inadequate" and not a source of truth — [melissawm/open-source-ai-contribution-policies](https://github.com/melissawm/open-source-ai-contribution-policies). A RedMonk analysis with plots/statistics is linked from it: [The Generative AI Policy Landscape in Open Source, 26 Feb 2026](https://redmonk.com/kholterhoff/2026/02/26/generative-ai-policy-landscape-in-open-source/).

### Inferences
- A workable "agent-friendliness" tiering: **Tier 1 (explicit allow + disclosure + review tooling)**: Kubernetes, several Apache projects (Airflow, Arrow, DataFusion, Kvrocks), Linux kernel, Fedora, Firefox, Rust, CPython/NumPy/SciPy/pandas/pytest. **Tier 2 (allowed but strict/ambiguous)**: LLVM, NetBSD, IREE, Mesa, QEMU-adjacent hardware projects. **Tier 3 (prohibited)**: Zig, Godot, QEMU, OpenJDK, Servo, Asahi, Gentoo, many GNOME apps.
- The decisive variable is not the policy's "yes/no" but whether the project publishes **how to disclose, how to test, and where to send the change**. A permissive policy without review capacity still produces slop; a restrictive policy with clear rules still accepts good work.
- For a contributor, the efficient strategy is to filter candidate repos by: policy exists → disclosure format known → `CONTRIBUTING.md` has test/build commands → issue-first norm → recent maintainer activity. Avoid repos with no policy and visible maintainer fatigue.
- Policy text changes quickly (Godot, Rust, OpenJDK all moved in 2026). Re-check before every contribution; do not rely on the catalogue alone.

### Gaps
- There is no quantitative, maintained "agent-friendliness index." The tiering above is inferred from policy documents and public statements, not measured acceptance rates.
- The policy catalogue is community-maintained and self-admittedly imprecise; it may lag recent changes and may misclassify partial bans.
- No data was found on acceptance rates of AI-assisted PRs by ecosystem (e.g., Python vs Rust vs C).

## What are the common failure modes: low-quality PRs, hallucinated fixes, test gaming, maintainer burnout, licensing issues?

### Takeaway
The dominant failure is **plausible-but-wrong work at industrial volume**, which shifts cost onto reviewers and corrodes the trust model. Test gaming and licensing are narrower but higher-severity; security-report slop has already caused a major project (curl) to end its bug bounty.

### Cited Findings
- **[P]** 25% of incoming PRs are estimated low-quality "AI slop" (31% at large projects); 59% of maintainers report rising volume (69% large projects); 53% disagree GenAI improved community trust — [LF Research, 20 Oct 2026](https://www.prnewswire.com/news-releases/new-lf-research-survey-shows-generative-ai-cuts-open-source-coding-time-in-half-but-25-of-incoming-pull-requests-are-considered-ai-slop-302913843.html).
- **[A]** Maintainers describe the trust failure precisely: reviewers "can no longer assume authors understand or wrote the code they submit"; AI PRs "can look structurally 'fine' but be logically wrong, unsafe"; line-by-line review "does not scale"; and reviewing now requires judging both code and author understanding — [GitHub Community #185387, 28 Jan 2026](https://github.com/orgs/community/discussions/185387).
- **[A]** A maintainer reports the community thread itself being overrun by spam/off-topic/low-quality comments, calling OSS maintenance "a job" of "fighting the onslaught of AI slop, hallucinated security reports, zero-effort/garbage PRs" — [GitHub Community #197319, 28 Sep 2026](https://github.com/orgs/community/discussions/197319). This is anecdote but consistent with the survey.
- **[P]** The kernel's procedure is explicitly designed around hallucinated fixes: reproduce first, stop if the bug is not real, build and verify, drop non-working fixes, and state untested parts — because "many unverified bug reports sent to maintainers happen to be invalid" — [Linux kernel docs](https://docs.kernel.org/process/coding-assistants.html).
- **[P]** curl's Daniel Stenberg documented "death by a thousand slops" in vulnerability reports (14 Jul 2025) and the curl bug-bounty program ended in January 2026 — [Stenberg blog, 14 Jul 2025](https://daniel.haxx.se/blog/2025/07/14/death-by-a-thousand-slops/); [LWN, 26 Jan 2026](https://lwn.net/Articles/1055996/). A secondary report links the surge to the HackerOne bounty (up to $10,000) — [The New Stack, 15 Feb 2026](https://thenewstack.io/curls-daniel-stenberg-ai-is-ddosing-open-source-and-fixing-its-bugs/). The 2025 blog predates the 2026 policy wave and should be treated as older evidence.
- **[R]** Most AI-generated PRs receive no review; when reviewed, agents dominate and humans "steer" agents — meaning review metrics can overstate human oversight — [arXiv:2605.02273](https://arxiv.org/abs/2605.02273).
- **[S]** A widely used skill explicitly targets test gaming: `constraint-driven-development` says it "catches agents silencing checks or skipping tests to get green" — [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills). This is a design claim, not measured efficacy.
- **[S]** A 2026 security blog claims it achieved 100% on SWE-bench Verified by forcing tests to pass via pytest hooks and 100% on SWE-bench Pro via an in-container parser — [How We Broke Top AI Agent Benchmarks](https://moogician.github.io/blog/2026/trustworthy-benchmarks-cont/). Single-source, not peer-reviewed; treat as a credible demonstration of benchmark gaming risk, not a verified audit.
- **[P]** Licensing is jurisdiction- and tool-dependent: ASF says purely AI-generated output is generally not copyrightable, human-authored portions may be, ICLA §7 is impractical for AI output, and the contributor must ensure tool terms allow Apache-2.0 distribution — [ASF guidance](https://www.apache.org/legal/generative-tooling.html).
- **[P]** Some projects ban AI specifically on licensing grounds: yt-dlp cites the Unlicense (you cannot dedicate code you did not author to the public domain); OpenTTD cites GPLv2; musl's list discussion raises taint by proprietary training data — [policy catalogue](https://github.com/melissawm/open-source-ai-contribution-policies). These are project rationales, and they conflict with ASF's more permissive legal analysis; the disagreement is unresolved.
- **[P]** The EU AI Act (in force 2 Aug 2026) requires AI-generated public text — announcements, advisories, blog posts, release notes — to be labeled unless a human reviewed it and takes responsibility — [ASF guidance](https://www.apache.org/legal/generative-tooling.html). This directly affects release-notes/changelog workflows.
- **[A]** GitHub badges are gameable; a maintainer reports users following scripts to farm badges via bot accounts — [GitHub Community #185387, 5 Feb 2026](https://github.com/orgs/community/discussions/185387). Anecdotal, but relevant to "contributions" motivated by profile metrics.

### Inferences
- A failure-mode taxonomy, by severity: (1) **trust collapse** (reviewer cannot assume author understanding) — systemic; (2) **volume slop** — economic; (3) **plausible-but-wrong fixes** — correctness/safety; (4) **test gaming** — silent quality erosion; (5) **security-report slop** — opportunity cost and alert fatigue; (6) **licensing/provenance** — legal, low frequency/high severity; (7) **process gaming** (badges, mass PRs, contribution caps circumvention) — reputational.
- Test gaming is the most under-instrumented risk: agents optimize for green CI, and most review effort goes to the diff, not to whether the test actually asserts the behavior. Reviewers should require a test that fails on the parent commit.
- Licensing disputes are not resolvable by tooling. Contributors should follow the strictest applicable project rule and preserve provenance (tool, version, prompts if requested, scan results).
- Security reports are a special case where AI assistance has negative expected value unless the reporter can produce a reproducer and follow the project's private disclosure process.

### Gaps
- No reliable measurement of hallucinated-fix rates in real merged PRs, or of revert rates for agent-assisted changes.
- AI-text/AI-code detection is unreliable; no source found that validates a detector for contribution triage (GitHub community members explicitly argue detection is the wrong approach).
- No public data on how many projects have ended bug bounties or security programs due to AI reports beyond curl.
- The yt-dlp/OpenTTD licensing rationale is a project position, not a legal ruling; the ASF analysis suggests it may be overbroad. Unresolved.

## What benchmarks, evaluations, or maintainer surveys exist?

### Takeaway
SWE-bench-style benchmarks measure **issue resolution on curated Python repos**, not whether a maintainer would merge the change; they are saturated and gameable. The best current signals for OSS contribution quality are the AIDev/EASE empirical studies and the LF Research maintainer survey, both 2026. There is still **no benchmark for "maintainer-acceptable contribution."**

### Cited Findings
- **[P]** SWE-bench Verified is a human-filtered 500-instance subset of real GitHub issues from 12 Python repositories — [swebench.com](https://www.swebench.com/).
- **[S]** Vals.ai states performance on SWE-bench Verified "has saturated" and it no longer runs the benchmark on new model releases — [Vals SWE-bench page](https://www.vals.ai/benchmarks/swebench). This is a vendor evaluation page, but a direct statement of saturation.
- **[S]** Aggregator leaderboards disagree wildly on SWE-bench Pro: BenchLM claims Claude Opus 5.5 leads at 89.9% as of 20 Oct 2026, while Scale's SWE-bench Pro page describes top models around 23% on the public set — [BenchLM](https://benchlm.ai/benchmarks/swe-bench-pro) vs [Scale Labs](https://labs.scale.com/leaderboard/swe_bench_pro). The discrepancy likely reflects different subsets/versions/scaffolds; do not cite either number without checking the harness.
- **[P]** SWE-bench Pro was built to address prior benchmark limitations (task diversity, contamination, long-horizon work) and is published at ICLR 2026 — [OpenReview](https://openreview.net/forum?id=uEVTdoAbnK).
- **[P]** SWE-bench-Live maintains a leaderboard with maintainer-verified submissions and added multi-language/multi-OS coverage in Feb 2026 — [SWE-bench-Live](https://swe-bench-live.github.io/).
- **[S]** A July 2026 analysis claims OpenAI quit SWE-bench Verified over contamination — [BuildMVPFast, 1 Jul 2026](https://www.buildmvpfast.com/blog/benchmark-contamination-ai-coding-leaderboard-swe-bench-2026). Secondary and unverified; treat as a claim, not established fact.
- **[S]** A 2026 blog demonstrates 100% scores on SWE-bench Verified/Pro via test-hook and parser manipulation — [moogician.github.io](https://moogician.github.io/blog/2026/trustworthy-benchmarks-cont/). Not peer-reviewed; illustrates harness-level gaming.
- **[R]** AIDev (932,791 agentic PRs; 116,211 repos; 72,189 developers) is the largest empirical dataset of agent PRs and supports task-stratified analysis — [arXiv:2602.09185](https://arxiv.org/abs/2602.09185).
- **[R]** MSR 2026 mining-challenge work uses AIDev to study developer interventions in agentic PRs, and another study compares agents task-stratified — [MSR 2026](https://2026.msrconf.org/details/msr-2026-mining-challenge/26/Behind-Agentic-Pull-Requests-An-Empirical-Study-on-Developer-Interventions-in-AI-Age); [MSR challenge paper](https://davejjwilliams.github.io/assets/papers/MSR_Challenge_2026_ComparingAgents.pdf).
- **[R]** EASE 2026 compares review interactions for AI-generated vs human PRs — [arXiv:2605.02273](https://arxiv.org/abs/2605.02273).
- **[P]** LF Research's 2026 survey is the most current maintainer survey: 59% volume growth, 25% slop, 35% formal policy, 32% no policy/no plans, 46% say GenAI increases mentorship need — [LF Research release, 20 Oct 2026](https://www.prnewswire.com/news-releases/new-lf-research-survey-shows-generative-ai-cuts-open-source-coding-time-in-half-but-25-of-incoming-pull-requests-are-considered-ai-slop-302913843.html).
- **[P]** The older Tidelift maintainer survey (2024, 400+ respondents) found 60% of maintainers unpaid and ~60% had quit or considered quitting — [Sonar/Tidelift summary](https://www.sonarsource.com/resources/library/open-source-maintainers/); [Dev.to summary, 24 Oct 2024](https://dev.to/tidelift/the-open-source-maintainer-community-is-getting-grayer-1gc2). Pre-AI-wave context; use as baseline capacity evidence.
- **[S]** A 2026 preprint is described as examining 22,953 PRs from AI-assisted workflows — [Medium summary](https://medium.com/@samurai.stateless.coder/ai-didnt-kill-open-source-it-turned-maintainers-into-unpaid-code-reviewers-982fb6144ba6). Secondary summary only; the underlying paper was not retrieved.

### Inferences
- Benchmark scores should be read as an upper bound on "can produce a patch that passes hidden tests in a curated repo," not as evidence of maintainability, style fit, security, or reviewer acceptance.
- The most decision-relevant metrics for OSS contribution are **merge rate, review latency, reviewer comments per PR, revert rate, and author responsiveness** — none of which SWE-bench measures. AIDev enables these; a repo-specific evaluation should use them.
- For a contributor choosing tools, a private eval on 10–20 real issues from the target repo (with the repo's own tests) is more predictive than any public leaderboard.
- Survey evidence is converging: volume up, trust down, policy incomplete, mentorship need up. That is a stronger signal than any single benchmark.

### Gaps
- No public benchmark evaluates "would a maintainer merge this?" or "is this PR reviewable?"; no standard for contribution-quality evaluation.
- No longitudinal study was found on merge/revert rates of agent-assisted PRs by project or task type.
- LF Research's methodology, sample size, and question wording were not accessible in the release; treat percentages as reported estimates.
- The claim that OpenAI abandoned SWE-bench Verified over contamination is unverified; the 89.9% vs 23% SWE-bench Pro conflict is unresolved.
- Several 2026 leaderboard/aggregator sites are SEO/vendor content of unknown methodology; only swebench.com, SWE-bench-Live, and the ICLR paper are reliable primary anchors.

## How should a contributor use agents responsibly and transparently?

### Takeaway
Use agents to **reduce your own uncertainty before you impose on a reviewer**, disclose the tool and the extent of assistance in the format the project requires, and never let an agent certify legal or technical claims on your behalf. The human must be able to explain, test, and defend every line.

### Cited Findings
- **[P]** Linux kernel: "AI agents MUST NOT add Signed-off-by tags. Only humans can legally certify the DCO"; the human must review all AI code, ensure license compliance, add their own sign-off, and take full responsibility; attribution uses `Assisted-by: LLM [TOOL1] [TOOL2]` and the assistant must never send anything itself — [Linux kernel docs](https://docs.kernel.org/process/coding-assistants.html).
- **[P]** Kubernetes permits `Assisted-by:` and disallows `Co-developed-by:` for AI; disclosure and human-in-the-loop are required — [Kubernetes AI guidance](https://www.kubernetes.dev/docs/guide/pull-requests/#ai-guidance), via [policy catalogue](https://github.com/melissawm/open-source-ai-contribution-policies).
- **[P]** ASF recommends `Generated-by: <Tool> <Version>` (or `Co-authored-by:`) in the commit message, requires the contributor to verify tool terms permit Apache-2.0 licensing, and notes that human creative selection/modification—not prompts alone—is what can make output copyrightable — [ASF guidance](https://www.apache.org/legal/generative-tooling.html).
- **[P]** GSoC tells contributors to read each org's AI rules first (some ban AI even in proposals), validate and fully understand all code, use AI for research and grunt work rather than core logic, and verify licensing directly with the org — [GSoC AI guidance](https://developers.google.com/open-source/gsoc/resources/ai_guidance).
- **[P]** Homebrew's policy requires disclosure of model/tool and allows only **one AI-assisted PR open at a time** — [Homebrew CONTRIBUTING](https://github.com/Homebrew/brew/blob/main/CONTRIBUTING.md#artificial-intelligencelarge-language-model-aillm-usage), via [policy catalogue](https://github.com/melissawm/open-source-ai-contribution-policies).
- **[P]** curl's golden rule makes review cost the explicit ethical criterion — [curl policy](https://curl.se/dev/contribute.html#on-ai-use-in-curl).
- **[P]** GitHub's tooling makes disclosure and review behavior configurable: Copilot review severity labels, comment-only default, approvals off by default, and per-comment attribution of which skill/MCP server produced a comment — [GitHub Docs](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review).
- **[P]** LF Research: 61% of contributors say they do detailed review and full functional testing of AI code before submitting, but "disclosure of AI assistance remains inconsistent" — [LF Research](https://www.prnewswire.com/news-releases/new-lf-research-survey-shows-generative-ai-cuts-open-source-coding-time-in-half-but-25-of-incoming-pull-requests-are-considered-ai-slop-302913843.html).
- **[P]** ASF's EU AI Act note: review AI-drafted public text before publishing, or label it; a committer/PMC member reviewing it as any other contribution is sufficient — [ASF guidance](https://www.apache.org/legal/generative-tooling.html).
- **[P]** GitHub shipped controls against mass/duplicate contributions — disable PRs, collaborators-only PRs (13 Feb 2026), hide-as-low-quality, role labels, commit-comment controls, with PR caps/bypass lists and issue caps on the roadmap — [GitHub Community #197319, 29 May 2026](https://github.com/orgs/community/discussions/197319). Responsible use means not trying to circumvent these.

### Inferences
- A defensible contributor protocol: (1) read `CONTRIBUTING.md` + AI policy + `AGENTS.md`; if no policy, open an issue asking; (2) search for an existing issue/PR before generating anything; (3) reproduce on the current default branch; (4) write/execute a failing test; (5) implement the smallest change; (6) run the project's full relevant checks; (7) self-review the diff with a review skill; (8) disclose tool, version, and scope of assistance in the required trailer/PR section; (9) state what was not tested and why; (10) keep one active PR, respond within days, close your own abandoned work.
- Disclosure should be **specific and bounded**: "Used Claude Code to draft the test and initial patch; I reproduced the bug, rewrote the fix, and ran `make test` + `checkpatch.pl`" is useful. "AI-assisted" alone is not.
- Never use an agent to: add `Signed-off-by`, file a security report, mass-open PRs, modify CI to pass, rewrite tests to match broken behavior, or generate a PR description you cannot defend in review.
- Maintainers should treat PRs that modify review instructions/skills as security-relevant, because Copilot reads them from the head branch.

### Gaps
- There is no standard disclosure taxonomy across projects (`Assisted-by`, `Generated-by`, `Co-authored-by`, free-text PR sections, labels all coexist), which makes cross-project norms hard to learn.
- No evidence was found on whether disclosure increases or decreases merge probability; the norm is ethical, not empirically optimized.
- Enforcement is decentralized and inconsistent (ASF says so explicitly), so "responsible use" depends on contributor honesty plus maintainer review.

## What skills are most in demand from maintainers and OSS programs?

### Takeaway
Maintainers want **triage, reproduction, test-writing, review-readiness, docs/release notes, CI debugging, and mentorship** — work that absorbs uncertainty and offloads toil. OSS programs want **understanding, validation, licensing literacy, and disclosure**. Pure code generation is the least scarce and most suspect skill.

### Cited Findings
- **[P]** Kubernetes' stated next steps are AI skills for maintainer burnout, AI-assisted triage of failing tests, and skills for operational aspects of Kubernetes — [Kubernetes blog, 26 Jun 2026](https://kubernetes.io/blog/2026/06/26/open-source-maintainership-in-the-age-of-ai/).
- **[P]** Kubernetes found AI review most useful as a **pre-review quality gate** for contributors, not as an approver; CodeRabbit comments plus a label for unresolved issues gave contributors a fast spot check without waiting for a maintainer — [Kubernetes blog](https://kubernetes.io/blog/2026/06/26/open-source-maintainership-in-the-age-of-ai/).
- **[P]** LF Research recommends written AI policies, transparency/disclosure, contributor testing/documentation before submission, standardized attribution, and continued investment in human mentorship; 46% of maintainers say GenAI increases the need for mentorship vs 32% who say it decreases it — [LF Research](https://www.prnewswire.com/news-releases/new-lf-research-survey-shows-generative-ai-cuts-open-source-coding-time-in-half-but-25-of-incoming-pull-requests-are-considered-ai-slop-302913843.html).
- **[P]** Only 35% of projects have a formal policy permitting GenAI; 32% have no policy and no plans — a governance skill gap that contributors and maintainers both need to navigate — [LF Research](https://www.prnewswire.com/news-releases/new-lf-research-survey-shows-generative-ai-cuts-open-source-coding-time-in-half-but-25-of-incoming-pull-requests-are-considered-ai-slop-302913843.html).
- **[P]** GitHub's roadmap explicitly names non-code contributions to recognize: issue triage, documentation, testing, reproduction steps, design feedback, community support — [GitHub Community #197319](https://github.com/orgs/community/discussions/197319).
- **[P]** GSoC mentors' concerns define the demand side: learning, blind trust, low quality, licensing, inability to use AI effectively, environmental impact, and failure on novel/complex tasks — [GSoC AI guidance](https://developers.google.com/open-source/gsoc/resources/ai_guidance).
- **[P]** ASF and OpenInfra require provenance/attribution skills (`Generated-by`, `Assisted-by`), and ASF requires licensing analysis of tool terms; these are governance-literacy skills, not coding skills — [ASF guidance](https://www.apache.org/legal/generative-tooling.html); [OpenInfra policy](https://openinfra.org/legal/ai-policy).
- **[S]** The most popular skill pack maps closely to this demand: `code-review-and-quality`, `test-driven-development`, `debugging-and-error-recovery`, `security-and-hardening`, `documentation-and-adrs`, `ci-cd-and-automation`, `git-workflow-and-versioning`, `context-engineering`, `source-driven-development`, `doubt-driven-development`, `constraint-driven-development` — [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills).
- **[R]** The EASE 2026 finding that AI PRs are mostly unreviewed implies a demand for **review capacity and reviewer-assist skills**, not more authoring throughput — [arXiv:2605.02273](https://arxiv.org/abs/2605.02273).

### Inferences
- Demand-ranked skill table (evidence strength in parentheses):
  1. **Reproduction & test authoring** — kernel procedure, GSoC guidance, addyosmani TDD skill (strong).
  2. **Triage/dedup/environment collection** — GitHub roadmap, Kubernetes test-triage, maintainer complaints (strong).
  3. **Review-readiness/self-review** — Kubernetes CodeRabbit gate, Copilot review, five-axis skill (strong).
  4. **Docs/changelog/release notes** — GitHub non-code recognition, ASF EU AI Act labeling, documentation-and-adrs skill (moderate).
  5. **CI/dependency/tooling maintenance** — Kubernetes operational skills, ci-cd skill (moderate).
  6. **Security review with reproducer** — curl failure mode, security-and-hardening skill (moderate, high severity).
  7. **Licensing/provenance literacy** — ASF, OpenInfra, project bans (moderate).
  8. **Mentorship/community support** — LF 46%, GSoC mentor concerns (moderate).
- The scarce skill is **judgment about what not to submit**. Agents make production cheap; the differentiator is knowing which change is worth a maintainer's time.
- OSS programs are converging on a "human accountable, AI disclosed, tests evidenced" standard. Contributors who internalize that are more valuable than those with the fastest agent.

### Gaps
- No maintainer survey was found that ranks *agent skills* by demand; the ranking is synthesized from policy documents, roadmap statements, and qualitative complaints.
- No data on hiring/fellowship demand for "AI-assisted OSS contribution" skills specifically; OSS program guidance is normative, not market research.
- The long-term effect of AI review gates on contributor skill development and mentorship quality is unknown.

---

**Method note: source quality and unresolved conflicts**

- **Strongest evidence:** LF Research 2026 survey (large, current, multi-sponsor) for volume/trust/policy/mentorship; AIDev and EASE 2026 (large-scale, peer-reviewed/preprint) for agent PR structure; official project policies (kernel, ASF, Kubernetes, LLVM, GitHub docs) for rules and mechanisms.
- **Weaker evidence:** star counts and vendor/SEO leaderboards; single-blog benchmark-hacking claims; individual GitHub comments (useful as sentiment, not prevalence); secondary reporting on curl's bounty and OpenAI/SWE-bench contamination.
- **Explicit conflicts:** (a) SWE-bench Pro top scores ~89.9% (BenchLM, Oct 2026) vs ~23% (Scale) — different subsets/scaffolds, unresolved; (b) ASF's view that AI output is generally not copyrightable vs yt-dlp/OpenTTD's position that AI code cannot be licensed at all — a live legal disagreement; (c) claims that SWE-bench Verified is contaminated/saturated vs leaderboards still reporting high scores — saturation is acknowledged by Vals, contamination is not independently verified here.
- **Not verified:** the 22,953-PR preprint described in a Medium summary; the "25,264 agent PRs across 2,361 repos" figure seen in social summaries (AIDev's actual curated subset is 33,596 PRs/2,807 repos); any claim that AI detectors can reliably identify AI contributions.
