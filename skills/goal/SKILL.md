---
name: goal
description: Use when defining a new goal, deciding what to build, or turning an outcome into a researched, measurable plan with success criteria, resources, milestones, and first actions.
license: MIT
compatibility: opencode
metadata:
  version: "1.1.0"
---

# Goal

Turn an ambition into a goal that can be researched, planned, executed, and reviewed. A goal is not a task list. It is a measurable outcome plus the constraints and evidence that tell you whether you are on track.

## Suite integration

Part of the senior-dev suite. `senior-dev-os` can load this skill automatically when the request is an outcome rather than a task; direct invocation works too. If the router loaded it, confirm the outcome, constraints, and decision owner, then produce the goal brief and research summary below.

## What a good goal contains

- **Outcome:** what changes, for whom
- **Measure:** how you will know
- **Time:** by when
- **Constraints:** time, money, skills, access, risk
- **Non-goals:** what you are not doing
- **Owner:** who decides and who does the work
- **Evidence:** what you will observe to adjust course

If any of these are missing, the goal is still a wish.

## Step 1: Capture the goal

Write one sentence:

> I want **[outcome]** by **[date]** so that **[reason]**.

Examples:

- I want a freelance invoicing SaaS with 10 paying users by March 31 so the business has recurring revenue.
- I want to be employable as a backend engineer by December so I can change roles.
- I want a landing page that converts 5% of visitors by Friday so the launch has a funnel.

If the sentence cannot be written, the goal is not clear enough yet. Use `brainstorming` to explore before continuing.

## Step 2: Clarify with at most five questions

1. What decision or action does this goal unlock?
2. What does "done" look like in observable terms?
3. What is the deadline, and what happens if it slips?
4. What constraints are fixed: budget, team, skills, access, compliance?
5. What would make this goal a failure even if it technically ships?

If the user cannot answer, propose a default, label it as an assumption, and continue. Do not stall.

## Step 3: Define success

Use three levels:

| Level | Meaning |
| --- | --- |
| Minimum | The smallest result that is still worth doing |
| Target | The expected outcome |
| Stretch | The result that would change the next decision |

Define:

- **Lagging metric:** the result you ultimately want (revenue, users, job offers, weight, completed project).
- **Leading metrics:** the behaviors that predict it (conversations, demos, practice sessions, published slices).
- **Evidence:** what you will inspect, not what you will feel.
- **Review date:** when you will decide to continue, pivot, or stop.

## Step 4: Constraints and non-goals

Write down:

- Deadline and budget
- Available hours per week
- Skills and gaps
- Tools and access
- Dependencies on other people
- Regulatory, privacy, or safety constraints

Write non-goals explicitly. A non-goal is a decision, not a maybe.

## Step 5: Research the domain

Before planning, search for what already works. Use the `research` skill for a deep pass, `firecrawl` for sources, and `advisor` for specialist interpretation.

Answer these questions:

1. What are the accepted methods or approaches?
2. What tools, platforms, and resources do practitioners actually use?
3. What are the prerequisites and their order?
4. What does it cost in time and money?
5. What are the common failure modes?
6. Who is already good at this, and what can be copied?
7. What benchmarks or examples show what "good" looks like?
8. What is the smallest test of demand or progress?
9. What can be bought, borrowed, or automated instead of built?
10. What would make this goal unnecessary or obsolete?

### Evidence standard

For each important claim, record the source, date, and confidence. Separate facts, assumptions, and unknowns. Prefer primary sources and current documentation over summaries. If the evidence is thin, say so and design the cheapest test instead of writing a confident plan.

### Search map by goal type

| Goal type | Search for |
| --- | --- |
| Build a product | Similar products, pricing, user complaints, market size, distribution channels, build vs buy, regulations |
| Learn a skill | Curricula, prerequisites, practice methods, projects, benchmarks, common plateaus |
| Start a business | Customer interviews, competitors, unit economics, licensing, acquisition channels, failure postmortems |
| Career | Role requirements, portfolios, referrals, salary bands, hiring processes, skill gaps |
| Creative work | Reference works, techniques, tools, distribution, audience, rights |
| Health or habit | Evidence-based protocols, contraindications, adherence research, measurement |
| Operations or process | Current baselines, bottlenecks, standards, automation options, change management |

### Resource inventory

| Resource | Have | Need | Get how | Cost |
| --- | --- | --- | --- | --- |
| Time |  |  |  |  |
| Money |  |  |  |  |
| Skills |  |  |  |  |
| People |  |  |  |  |
| Tools |  |  |  |  |
| Data |  |  |  |  |
| Distribution |  |  |  |  |

Do not plan as if missing resources exist. Name them and decide whether to acquire, borrow, or cut scope.

## Step 6: Map the path

Create three to five milestones. Each milestone has:

- An outcome
- A measurable completion signal
- A deadline
- Dependencies
- The first action

Then write the first three actions. They should be doable this week and should produce evidence, not just activity.

## Step 7: Pre-mortem and kill criteria

Ask: "It is six months from now and the goal failed. Why?"

List the top five reasons. For each, add a prevention or early-detection signal.

Define kill criteria in advance:

- A date by which a signal must appear
- A budget or time cap
- A quality or safety red line
- A condition under which the goal is no longer worth pursuing

Kill criteria prevent sunk-cost thinking. They are not pessimism; they are decision hygiene.

## Step 8: Choose the operating model

| Model | Use when |
| --- | --- |
| Solo | The goal is small, sequential, or highly personal |
| Advisor panel | The decision is high-stakes or you need specialist lenses |
| Subagents | The work splits into research, building, review, or documentation roles |
| Full project OS | The goal is a product or business with multiple workstreams |

Use `advisor` for counsel and `subagents` for decomposition. Use `project-kickoff` when the goal becomes a software project.

## Step 9: Write the goal brief

Save to `goals/<slug>-<YYYY-MM-DD>.md`, or `docs/goals/` inside a software repo. Use `templates/goal-brief.md`.

The brief must fit on one or two pages. If it is longer, the goal is probably several goals. Split it.

## Step 10: Review cadence

| Cadence | Review |
| --- | --- |
| Weekly | Leading metrics, first actions, blockers |
| Monthly | Milestone progress, resource burn, evidence |
| At each milestone | Continue, adjust, or kill |
| At the deadline | Outcome, lessons, next goal |

Review the evidence, not the effort. "I worked hard" is not progress.

## Output format

```markdown
# Goal: <outcome>

## Statement
I want <outcome> by <date> so that <reason>.

## Success
- Minimum:
- Target:
- Stretch:
- Leading metrics:
- Evidence:
- Review date:

## Constraints and non-goals
...

## Research summary
...

## Resource inventory
...

## Milestones
| # | Outcome | Signal | Date | Depends on |
| --- | --- | --- | --- | --- |

## First three actions
1.
2.
3.

## Risks and kill criteria
...

## Operating model
...
```

## Common mistakes

| Mistake | Consequence | Fix |
| --- | --- | --- |
| Goal is an activity ("learn React") | No finish line | Define an outcome and evidence |
| No leading metric | You only learn at the end | Track weekly behavior |
| No non-goals | Scope expands | Write the fence |
| Research skipped | You repeat known mistakes | Search methods, costs, failures |
| Plan assumes missing resources | Stalled halfway | Resource inventory |
| No kill criteria | Sunk-cost escalation | Decide the stop conditions now |
| Too many milestones | Nothing completes | Three to five |
| No review date | Goal drifts | Put it on the calendar |

## Related skills

- `brainstorming` when the idea is still fuzzy
- `research` for the evidence pass
- `advisor` for specialist counsel
- `subagents` for parallel workstreams
- `project-kickoff` when the goal becomes a software project
- `writing-plans` for the implementation plan
