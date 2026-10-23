# GSoC Strategy 2027

> Planning model based on the official 2026 GSoC timeline. The 2027 dates are not published yet; verify them at [developers.google.com/open-source/gsoc/timeline](https://developers.google.com/open-source/gsoc/timeline) before relying on a specific day.

## Goal

```text
3 target organizations
2 repositories per organization
1 primary project idea
3–5 meaningful merged contributions in the target area
1 credible proposal submitted early
```

GSoC is not a bug-fixing contest. It is a project proposal plus proof that you can work in the community.

## Timeline

| When | What happens | What you do |
| --- | --- | --- |
| Oct–Nov 2026 | Preparation | Choose 3 orgs, set up 2 repos, make 1–2 small contributions, start a log |
| Dec 2026–Jan 2027 | Proof building | Land 3–5 contributions in one area; read ideas lists and past proposals |
| Jan 2027 | Mentoring orgs apply to Google | Refine your shortlist; do not wait for accepted orgs to start contributing |
| Feb 2027 | Accepted orgs announced | Confirm primary + backup; identify mentors; ask one specific question |
| Mar 2027 | Contributor applications | Draft early, get feedback, submit before the deadline |
| Apr 2027 | Mentor review and ranking | Keep contributing; accepted projects announced at the end of April |
| May 2027 | Community bonding | Confirm milestones, communication, access; coding starts late May |
| Jun–Aug 2027 | Coding | Weekly updates, midterm, final work product, docs, demo |
| Sep–Nov 2027 | Final evaluation / extended timeline | Finish, present, and leave the project maintainable |

The 2026 model: org applications in January, accepted orgs in February, proposals due at the end of March, accepted projects at the end of April, coding from late May.

## 30-day starter plan

### Week 1 — choose the target

- [ ] Write your stack, weekly time budget, and constraints
- [ ] Pick 3 organizations with active maintainers
- [ ] Pick 2 repositories per organization
- [ ] Read `CONTRIBUTING.md`, `CODEOWNERS`, `SECURITY.md`, and the AI policy
- [ ] Get one repository building and its tests running

### Week 2 — build the radar

- [ ] Scan for `good first issue`, `help wanted`, `bug`, `docs`, and `tests`
- [ ] Collect 10–20 candidates
- [ ] Score the top 5 on impact, reproducibility, scope, maintainer signal, and fit
- [ ] Identify the human lead for the top 3
- [ ] Reject assigned, stale, duplicate, or already-fixed issues

### Week 3 — reproduce and comment

- [ ] Pick one issue scoring 70+
- [ ] Reproduce it on the current `main`
- [ ] Find the failing path
- [ ] Write a minimal plan and one precise question
- [ ] Comment with evidence, not "Can I work on this?"

### Week 4 — land the first PR

- [ ] Write the failing test first
- [ ] Make the smallest safe change
- [ ] Run the project's full gate
- [ ] Open a focused PR with a clear description
- [ ] Respond to review and update the contribution log

## Weekly cadence

| Day | Action |
| --- | --- |
| Monday | Choose one issue or proposal task; write the next action |
| Tuesday–Thursday | Reproduce, code, test, review |
| Friday | Run the full gate; update the PR and contribution log |
| Weekend | Read one area of the codebase; send one mentor update if appropriate |

Keep one PR in review at a time. Finish before starting the next.

## Contribution proof

Good proof:

- a bug fix with a regression test
- a test-only PR that makes a flaky area trustworthy
- a docs PR that explains a confusing workflow
- a small feature or refactor with maintainer agreement
- a review or triage contribution that shows judgment
- a proof of concept or benchmark for the proposed idea

Weak proof:

- typo fixes in unrelated files
- AI-generated PRs you cannot explain
- drive-by refactors
- comments asking for assignment
- many open PRs and no merges

## Proposal checklist

- [ ] Organization template followed
- [ ] Problem and users are specific
- [ ] Deliverables are concrete
- [ ] Technical approach names interfaces and dependencies
- [ ] Timeline has milestones and buffer
- [ ] Testing and acceptance criteria are defined
- [ ] Risks and mitigations are honest
- [ ] Communication plan is clear
- [ ] Prior contributions are linked
- [ ] Submitted before the deadline

## Risks

| Risk | Mitigation |
| --- | --- |
| Choosing a prestigious org with no responsive mentor | Score mentor responsiveness and contribution surface |
| Starting in March with no history | Start now; build proof before proposals open |
| Too many shallow contributions | Go deep in one area |
| Proposal is a feature list | Add scope, interfaces, tests, and risks |
| Mentor does not reply | Use the public channel; follow up once; keep contributing |
| AI-generated work you cannot defend | Disclose AI use; understand and test every line |
| Missing the deadline | Submit early; do not rely on the last day |

## Do not do

- Do not mass-comment on issues or ask for assignment without a plan.
- Do not contact every mentor with the same message.
- Do not propose a rewrite when a scoped change is possible.
- Do not treat GSoC as a solo coding task.
- Do not disappear after submitting.

## Skills and commands

```text
/issues   find, score, and track issues; identify the human lead
/gsoc     plan organizations, contributions, mentor outreach, and proposal
/oss      make the contribution maintainer-grade
```

Skills:

```text
C:\Users\Vishal\.agents\skills\oss-issue-scout\SKILL.md
C:\Users\Vishal\.agents\skills\gsoc-strategist\SKILL.md
C:\Users\Vishal\.agents\skills\oss-contributor\SKILL.md
```

Templates:

```text
C:\Users\Vishal\.agents\skills\oss-issue-scout\templates\issue-brief.md
C:\Users\Vishal\.agents\skills\oss-issue-scout\templates\oss-pipeline.md
C:\Users\Vishal\.agents\skills\gsoc-strategist\templates\org-scorecard.md
C:\Users\Vishal\.agents\skills\gsoc-strategist\templates\proposal-outline.md
C:\Users\Vishal\.agents\skills\gsoc-strategist\templates\mentor-outreach.md
```

## Related

- [[OSS and Freelance Skills]]
- [[OpenCode Skills]]
- [[Freelancing and open source AI skills]]
