---
name: oss-issue-scout
description: "Use when finding, scoring, and tracking open-source issues to work on: scanning GitHub for good first issues or help-wanted bugs, filtering out stale or assigned work, identifying the area maintainer or GSoC mentor, building a contribution pipeline, or deciding which issue is worth a PR. Use this whenever the user asks how to find issues, which repo to contribute to, how to get started in open source, or how to find the right maintainer for an issue."
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
  suite: "oss-contributor"
---

# OSS Issue Scout

Finding an issue is not the hard part. Finding an issue that is **real, unclaimed, reproducible, in scope, and owned by a responsive maintainer** is the hard part. This skill turns GitHub into a ranked, tracked pipeline instead of a pile of open tabs.

Use it before `oss-contributor` when the question is "what should I work on?" and before `gsoc-strategist` when the question is "which org and issue should I build proof in?"

## The two leads

| Lead | Meaning | Where to find it |
| --- | --- | --- |
| **Issue lead** | A high-potential issue worth your time | GitHub search, labels, scoring |
| **Human lead** | The person who owns the area or mentors the project | Assignee, author, comments, `CODEOWNERS`, git history, recent PR reviewers, GSoC ideas list |

The issue reporter is usually not the owner. The person who says "PR welcome" is a stronger signal than the person who opened the issue.

## Non-negotiables

- Do not automate comments, claims, or PRs. The agent drafts; the human sends.
- Do not mass-comment on issues or ask "Can I work on this?" without a plan.
- Check whether the issue is assigned, closed, has a linked PR, or is already fixed on `main`.
- Read `CONTRIBUTING.md`, `CODEOWNERS`, and the project's AI policy before writing code.
- Never fabricate reproduction steps, logs, or maintainer approval.
- If a maintainer does not respond, wait a reasonable period and move on. Do not ping repeatedly.
- Prefer one finished contribution over ten claimed issues.

## 1. Define the target

Before scanning, write:

```text
Stack:
Organizations (3 max):
Repositories (2 per org max):
GSoC interest: yes/no
Area of interest:
Time available per week:
Constraints:
```

Choose organizations that are active, have a public ideas list if you are targeting GSoC, and have maintainers who respond. A famous org with a dead issue tracker is a worse target than a smaller active project.

## 2. Build the issue radar

Labels vary. Scan for variants:

```text
good first issue
good-first-issue
beginner
easy
help wanted
mentor
gsoc
bug
confirmed
needs-repro
docs
tests
area/<your-area>
```

GitHub search strings:

```text
is:issue is:open no:assignee label:"good first issue" sort:updated-desc
is:issue is:open no:assignee label:"help wanted" sort:updated-desc
is:issue is:open label:"bug" label:"confirmed"
is:issue is:open label:"docs"
is:issue is:open label:"tests"
```

With `gh`:

```powershell
gh issue list --repo org/repo --state open --label "good first issue" --limit 50 --json number,title,url,labels,assignees,comments,createdAt,updatedAt,author
```

```powershell
gh issue view 123 --repo org/repo --comments
```

```powershell
gh api repos/org/repo/issues/123/timeline --paginate
```

```powershell
gh search issues --owner org --label "help wanted" --state open --limit 50
```

Use `scripts/scan-issues.ps1` to scan several repos and export a CSV:

```powershell
.\scripts\scan-issues.ps1 -Repos "org/repo-one","org/repo-two" -Labels "good first issue","help wanted" -OutFile "oss-issues.csv"
```

Scan a maximum of six repositories. More than that produces noise, not a pipeline.

## 3. Score the issue

Use 100 points:

| Dimension | Weight | 5 means | 1 means |
| --- | ---: | --- | --- |
| Impact | 25 | Fixes a real user or maintainer pain | Cosmetic or unclear |
| Reproducibility | 20 | Clear minimal repro, you can run it | Cannot reproduce or verify |
| Scope | 20 | One focused PR | Cross-cutting redesign |
| Maintainer signal | 20 | Recent activity, "PR welcome," unassigned | Stale, blocked, assigned, contested |
| Fit | 15 | You can build and test the area | You cannot run the project |

**Threshold: 70+.** Below 70, skip unless you are deliberately learning.

Red flags:

- assigned to someone
- linked open PR or duplicate issue
- `needs design`, `needs discussion`, `blocked`, `wontfix`
- stale for a year with no maintainer response
- 30+ comments with disagreement
- no reproduction and no way to get one
- requires hardware, paid cloud, or private data
- "good first issue" that actually requires deep domain knowledge
- CLA/DCO or security process you cannot satisfy

Green flags:

- maintainer says "PRs welcome" or asks for a reproduction
- small, confirmed bug with a clear expected result
- test, docs, error-message, or CI improvement
- recent activity in the area
- a maintainer or mentor has already described the expected behavior

## 4. Find the human lead

For a promising issue:

```powershell
gh issue view 123 --repo org/repo --comments
```

Look for:

- assignee
- issue author
- maintainers replying
- area labels such as `area/api`, `sig/network`
- linked PRs and reviewers

Find code ownership:

```powershell
gh api repos/org/repo/contents/.github/CODEOWNERS -H "Accept: application/vnd.github.raw"
```

Find recent authors in the area:

```powershell
git log --format="%an" -- path/to/area | Sort-Object -Unique
```

Find recent merged PRs and reviewers:

```powershell
gh pr list --repo org/repo --state merged --limit 30 --json number,title,author,reviews,files
```

For GSoC, the mentor is usually listed on the organization's ideas page, not necessarily in the issue. Use the official channel; do not cold-DM.

## 5. Qualify before commenting

Verify:

- the issue is still open and unassigned
- no linked PR already fixes it
- the behavior still reproduces on the current `main`
- the project's tests/build run locally
- the expected behavior is stated or can be inferred from docs/tests
- the fix is within your time budget
- you know the area owner or mentor

If any of these fail, write the gap down and either ask one precise question or move on.

## 6. Comment with a plan

Do not ask for permission with no work. Show that you have already done the first step.

```text
I reproduced this on <version/commit> with <minimal case>.
The failing path appears to be <area/function>.
I plan to <small fix> and add a regression test for <case>.
Is that the right direction, or is there a constraint I should know about?
```

If the issue is ambiguous:

```text
I can reproduce <part>, but I cannot reproduce <part> because <reason>.
Could you confirm <specific detail>? I will then write the failing test and PR.
```

If you are targeting GSoC, add a link to your prior contribution in the same area. Do not mention GSoC in every issue comment; let the work speak.

## 7. Run the pipeline

Track each issue:

```text
Org | Repo | Issue | Score | Human lead | Status | Next action | PR | Updated
```

Stages:

```text
New -> Scored -> Owner found -> Reproduced -> Commented
    -> In progress -> PR open -> In review -> Merged / Closed
```

Weekly review:

- add 10–20 candidates
- score the top 5
- inspect 1–2 deeply
- comment on 1
- finish 1 PR before starting another
- remove stale or assigned issues

## 8. Link to GSoC

For a GSoC target:

- scan the organization's **ideas list** first
- prefer issues in the same area as the idea
- identify the mentor for the idea
- build 3–5 merged contributions in that area
- keep a public contribution log with links
- use `gsoc-strategist` to turn the proof into a proposal

The goal is not "many issues." The goal is "a maintainer in the target area knows my work."

## 9. Anti-patterns

- claiming five issues and finishing none
- commenting "I can do this" with no reproduction
- picking an issue because the label says beginner without reading it
- ignoring an existing PR
- using an agent to generate a comment and posting it unedited
- chasing a famous org with no responsive maintainers
- treating a typo fix as proof you can deliver a GSoC project
- asking a mentor to explain the whole codebase before doing any work

## 10. Output format

End with:

```markdown
### Issue scout result
- Target:
- Candidates scanned:
- Top issues:
| Score | Repo | Issue | Human lead | Why it fits |
- Recommended issue:
- First action:
- Risks:
```

Use `templates/issue-brief.md` for the chosen issue and `templates/oss-pipeline.md` for the tracker.

## Composition

- `oss-contributor` — contribution contract and maintainer lens.
- `large-codebase-navigator` — map the code path after choosing an issue.
- `oss-senior-engineer` — reproduce, fix, test, PR.
- `gsoc-strategist` — org and proposal strategy.
- `research` / `firecrawl-search` — org and project background.
- `stop-slop` — clean up comments and outreach.
