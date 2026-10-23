---
name: gsoc-strategist
description: "Use when planning or applying to Google Summer of Code: choosing organizations, reading ideas lists, building contribution proof, contacting mentors, writing a proposal, planning the timeline, or preparing for community bonding and coding. Use this whenever the user mentions GSoC, Summer of Code, a GSoC proposal, an accepted organization, a mentor, or a summer open-source project."
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
  suite: "oss-contributor"
---

# GSoC Strategist

GSoC is not a bug-fixing contest. It is a **project proposal plus proof that you can work in the community**. The organizations that select you are asking: can this person understand our code, communicate with mentors, and deliver a 12-week project without constant supervision?

Bug fixes are how you answer that question before the proposal.

## The timeline reality

Use the official GSoC timeline for the current cycle. The 2026 cycle is a useful planning model:

| Month | What happens |
| --- | --- |
| January | Mentoring organizations apply to Google |
| February | Accepted organizations announced; contributors discuss ideas |
| March | Contributor application period; proposals due at the end of March |
| April | Mentors review and rank proposals; accepted projects announced at the end of April |
| May | Community bonding; coding begins in late May |
| June–August | Coding, midterm evaluation, final work product |
| August–November | Final evaluations; extended timelines finish by early November |

Source: [Google Summer of Code timeline](https://developers.google.com/open-source/gsoc/timeline). Dates can shift each year. Verify the current cycle before relying on a date.

For the next cycle, the practical start month is **now**, not March. The contributors who get selected usually have months of contribution history before proposals open.

## The GSoC equation

```text
Selection ≈ fit with an ideas-list project
          + evidence you can do the work
          + mentor trust
          + a credible, scoped proposal
```

Missing any one of these weakens the application. A brilliant proposal with no contributions is a guess. Ten random typo PRs with no project fit is noise. A mentor conversation with no proposal is incomplete.

## 1. Choose organizations

Pick **3 organizations**, not 30. Score each 1–5:

| Criterion | Question |
| --- | --- |
| Stack fit | Can I build and test this project comfortably? |
| Ideas list | Is there a project I genuinely want to do? |
| Mentor responsiveness | Do maintainers reply in public channels? |
| Contribution surface | Are there issues I can fix in the target area? |
| Codebase health | Recent commits, merged PRs, clear contributing docs |
| GSoC history | Has the org mentored successfully before? |
| Communication | Is the channel usable for a newcomer? |
| Time fit | Can I commit the required weeks? |

Prefer an organization where you can name **two people** who have reviewed or discussed work in your target area. A famous org with no responsive mentor is a bad bet.

## 2. Read the ideas list like a project brief

For each idea, extract:

- problem and expected outcome
- required skills
- mentor and communication channel
- size and difficulty
- dependencies and risks
- existing code or prototypes
- tests and acceptance criteria
- what a successful final demo looks like

Then ask:

- Can I build a small proof of concept before proposals open?
- Which part is ambiguous, and what would I ask the mentor?
- Which existing issues are in the same area?
- What can I contribute in the next 30 days that proves fit?

If the idea is vague, do not write a proposal around your guess. Ask one specific question after doing background work.

## 3. Build contribution proof

Aim for **3–5 meaningful merged contributions** in the target area, not 20 scattered typo fixes.

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

Use `oss-issue-scout` to find the issues and `oss-contributor` / `oss-senior-engineer` to land them.

## 4. Contact mentors correctly

Do not start with "How can I get selected?" Start with evidence.

```text
Subject: <specific idea> — contribution and one question

Hi <mentor>,

I am preparing for <idea/project> and have been contributing in <area>.
Recent work:
- <PR/issue link>
- <PR/issue link>

I read the idea and the relevant code. My understanding is <one-paragraph summary>.
One thing I cannot determine is <specific question>.

Would <specific approach> fit the project's direction, or is there a constraint
I should account for?

Thanks,
<name>
```

Rules:

- Use the organization's public channel unless told otherwise.
- Ask one specific question, not five broad ones.
- Link to work you actually did.
- Do not ask for a solution or a guaranteed slot.
- Do not mention GSoC in every issue comment.
- Follow up once after a reasonable period, then move on.

## 5. Write the proposal

Use the organization's template if it has one. Otherwise:

```markdown
# <Project title>

## Synopsis
One paragraph: what, for whom, and why it matters.

## Motivation
The problem, current limitations, and why this project is the right next step.

## Deliverables
Concrete outputs, including tests, docs, and a demo.

## Technical approach
Architecture, interfaces, data flow, dependencies, and alternatives considered.

## Timeline
Week-by-week or milestone-by-milestone plan, including buffer.

## Testing and validation
Unit, integration, performance, compatibility, and acceptance criteria.

## Risks and mitigations
What could go wrong and how you will reduce it.

## Communication
Where you will post updates, how often, and how you will ask for help.

## About me
Relevant background and prior contributions, with links.

## References
Issues, PRs, docs, and discussions that shaped the plan.
```

A strong proposal is **specific, scoped, testable, and honest about uncertainty**. A weak proposal is a feature list with no acceptance criteria and no risk plan.

## 6. Run the month-by-month campaign

### October–November

- choose 3 orgs and 2 repos each
- build the issue radar
- make 2–3 low-risk contributions
- learn one codebase deeply
- start a contribution log

### December–January

- land 3–5 contributions in the target area
- read the org's ideas list and past proposals
- identify the mentor and the project
- write a one-page concept note
- ask one specific mentor question

### February

- accepted organizations are announced
- confirm the org and idea
- deepen contributions in that area
- draft the proposal outline
- get feedback on scope and deliverables

### March

- write the full proposal
- share a draft with the mentor or community
- revise based on feedback
- submit before the deadline, not on the last day

### April

- mentors rank proposals
- continue contributing; do not disappear
- prepare for interviews or clarification if asked
- accepted projects are announced at the end of April

### May

- community bonding
- confirm milestones, communication cadence, and access
- set up the development environment
- write the first small PR or prototype before coding officially starts

### June–August

- code in small, reviewable increments
- post weekly updates
- raise blockers early
- pass midterm with a working demo and tests
- finish the final work product, docs, and demo

## 7. Weekly operating cadence

| Day | Action |
| --- | --- |
| Monday | Pick one issue or proposal task; write the next action |
| Tuesday–Thursday | Reproduce, code, test, review |
| Friday | Run the full gate; update the PR and contribution log |
| Weekend | Read one area of the codebase; send one mentor update if appropriate |

Keep one PR in review at a time. Finish before starting the next.

## 8. Proposal scorecard

| Dimension | Question | Score 1–5 |
| --- | --- | --- |
| Fit | Does it match the org's idea and stack? | |
| Specificity | Are deliverables and interfaces concrete? | |
| Feasibility | Can it be done in the available weeks? | |
| Evidence | Do prior contributions prove capability? | |
| Testing | Is validation defined? | |
| Risk | Are risks and mitigations realistic? | |
| Communication | Is the update plan clear? | |

Below 28/35, revise before submitting.

## 9. Common mistakes

- starting in March with no contribution history
- choosing an org for prestige, not mentor fit
- writing a proposal for an idea you have not discussed
- claiming you will "improve performance" without a metric
- proposing a rewrite instead of a scoped change
- ignoring the org's template or deadline
- mass-emailing mentors
- disappearing after submitting
- treating GSoC as a solo coding task instead of a community project
- using AI to write a proposal you cannot defend

## 10. Output format

End with:

```markdown
### GSoC campaign
- Target orgs:
- Target idea:
- Current proof:
- Mentor contact:
- Proposal state:
- Biggest risk:
- Next action this week:
```

Use `templates/org-scorecard.md`, `templates/proposal-outline.md`, and `templates/mentor-outreach.md`.

## Composition

- `oss-issue-scout` — find issues and human leads.
- `oss-contributor` — contribution contract and maintainer lens.
- `oss-senior-engineer` — fix, test, PR.
- `large-codebase-navigator` — understand the target area.
- `goal` — define the outcome and milestones.
- `writing-plans` — turn the proposal into a week-by-week plan.
- `stop-slop` — remove generic proposal and outreach language.
