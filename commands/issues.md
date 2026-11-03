---
description: Find, score, and track open-source issues and the maintainers behind them
---

Load the `oss-issue-scout` skill for this request: $ARGUMENTS

Act as the front door. Do not merely list issues. Classify the request, read the relevant skill files, and execute the workflow.

## Classify the request

- "Find issues", "what should I work on", or "scan this repo" -> issue radar and scoring
- "Who owns this issue", "who is the maintainer", or "who is the GSoC mentor" -> human-lead discovery
- "Is this issue worth it" -> 100-point score and red flags
- "Build my pipeline" -> tracker and weekly review
- "I want GSoC proof" -> link the issue to an organization's ideas list and `gsoc-strategist`

## Rules

- Use the authenticated `gh` CLI. Verify the issue is open, unassigned, and not already fixed.
- Do not automate comments, claims, or PRs. Draft only; the human sends.
- Score with impact, reproducibility, scope, maintainer signal, and fit. Threshold 70/100.
- Identify the human lead: assignee, area maintainer, recent authors, reviewers, or GSoC mentor.
- Prefer 3–5 meaningful contributions in one area over many scattered issues.
- End with the top issues, recommended issue, human lead, first action, and risks.

For the full workflow, read `~/.agents/skills/oss-issue-scout/SKILL.md`. For the tracker, use `~/.agents/skills/oss-issue-scout/templates/oss-pipeline.md`.
