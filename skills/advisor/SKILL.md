---
name: advisor
description: Use when you want expert advice, a second opinion, a red-team review, or a panel of specialist perspectives on a goal, decision, plan, design, or problem.
license: MIT
compatibility: opencode
metadata:
  version: "1.1.0"
---

# Advisor

Advice is a recommendation under uncertainty. It is not agreement, encouragement, or a list of generic best practices. Good advice names the trade-off, states what it assumes, and tells the decision-maker what would change the recommendation.

## Suite integration

Part of the senior-dev suite. `senior-dev-os` can load this skill automatically for an expensive, contested, or irreversible decision; direct invocation works too. If the router loaded it, frame the decision first, then produce the advisory memo and the cheapest test.

## When to use it

Use the advisor when:

- A decision is expensive to reverse.
- You have a plan but cannot see its weak points.
- Several specialists would disagree.
- You need a second opinion before committing.
- You want a red-team review or a pre-mortem.
- You are entering an unfamiliar domain.

Do not use it to:

- Avoid gathering evidence.
- Replace a qualified lawyer, doctor, accountant, or other licensed professional.
- Make a decision that belongs to the human owner.
- Produce a confident answer where the evidence is thin.

## Frame the decision

Before giving advice, write:

- **Question:** the exact decision
- **Context:** the project, goal, and constraints
- **Options:** at least two real alternatives
- **Stakes:** what happens if this is wrong
- **Reversibility:** how expensive it is to undo
- **Deadline:** when the decision must be made
- **Owner:** who decides
- **Evidence:** what is known, assumed, and unknown

If the question is vague, narrow it. "Should we use microservices?" is not a decision. "Should this six-week MVP use one deployable or split billing into a service?" is.

## Choose the lenses

Pick two to four lenses. More than four produces noise, not wisdom.

| Lens | Optimizes for | Asks | Red flags |
| --- | --- | --- | --- |
| Product strategist | User value and focus | Who pays, why now, what is the wedge, what is out | Feature list without a user, no distribution |
| Market researcher | Evidence about demand | Who competes, what do users hate, what will they pay, how do they find it | TAM hand-waving, no primary evidence |
| Software architect | Boundaries and reversibility | What changes together, what is the failure domain, what is the cheapest evolvable shape | Premature distribution, hidden coupling |
| Security and privacy | Loss prevention | What is the threat model, who can access what, where does data live, what is logged | Auth only in the UI, secrets in code, unbounded retention |
| Data and analytics | Measurement quality | What exactly is measured, how, what would make the number lie | Vanity metrics, no baseline, no instrumentation |
| UX and design | User comprehension | What is the user trying to do, what is the simplest flow, what happens on error | Happy-path-only designs, inaccessible controls |
| QA and testing | Release confidence | What can break, what is the cheapest test, what edge cases matter | Coverage theater, no failure-path tests |
| SRE and operations | Reliability and recovery | How does it deploy, how does it fail, how do we know, how do we roll back | No observability, no rollback, manual deploy |
| Finance | Cash and return | What does it cost, what is the margin, what is the payback, what is the downside | No unit economics, optimistic revenue |
| Legal and compliance | Avoidable liability | What is regulated, what is contracted, what is the data lifecycle | Copying policies, ignoring jurisdiction |
| Marketing and distribution | Reach and conversion | Who is the audience, what channel, what message, what proof | Building without a distribution plan |
| Operations | Repeatability | Who does it, what is the capacity, what is the failure path | Hero-dependent processes |
| Domain expert | Field norms | What is accepted practice, what is regulated, what do beginners get wrong | Generic advice that ignores the field |
| Learning or career coach | Skill and market fit | What is the gap, what is the practice, what evidence proves progress | Activity without a portfolio or feedback |

For a topic not in the table, name the specialist lens explicitly and state what it optimizes for.

## Modes

| Mode | Use when | Output |
| --- | --- | --- |
| Single advisor | One clear lens is enough | Concise recommendation and risks |
| Panel | The decision spans several domains | Independent views, then synthesis |
| Red team | The plan looks convincing | Attack surface, failure modes, weakest assumptions |
| Pre-mortem | Before committing | "It failed; why?" list with mitigations |
| Decision review | Choosing between options | Criteria matrix, trade-offs, recommendation |
| Second opinion | You already have a recommendation | Agreement, disagreement, and what would change it |

## In OpenCode

Use the `subagent` tool with the `general` agent for independent advisor views. Run two to four in parallel with the same decision frame and a different lens in each prompt. Do not include another advisor's conclusion in the prompt; anchoring removes the value of independence. Then synthesize in the main session.

If the decision needs implementation or research, use `subagents` for the roster and `research` for the evidence pass.

## Process

### 1. State the decision and the evidence

Separate:

- **Facts:** verified, sourced, reproducible
- **Assumptions:** plausible but unverified
- **Opinions:** judgment calls
- **Unknowns:** what you would need to know

Do not let an assumption masquerade as a fact.

### 2. Get independent views first

If subagents are available, use `subagents` to give each advisor the same brief and ask for an independent answer. Do not show one advisor another's conclusion before they answer; anchoring destroys the value of a panel.

If subagents are not available, answer each lens separately before synthesizing.

### 3. Surface disagreement

Do not average conflicting views. Explain:

- Where the advisors agree
- Where they disagree
- Why the disagreement exists (different assumptions, time horizons, risk tolerance)
- What evidence would resolve it

The disagreement is often the most useful part.

### 4. Recommend

Give:

- A primary recommendation
- The conditions under which it holds
- The strongest counterargument
- Confidence: high, medium, or low
- The dissent, if any
- What would change your mind

### 5. Design the cheapest test

Before a large commitment, propose the smallest experiment that produces evidence:

- A customer interview
- A landing page
- A spike
- A prototype
- A load test
- A manual concierge version

State the cost, the time, and the signal that would justify continuing.

### 6. Check the base rate and the downside

Before forecasting, ask what usually happens to projects like this. Use base rates, reference classes, and historical data where they exist. Then ask what the downside is if the recommendation is wrong and whether it is survivable. A high expected value with a fatal downside is not a good decision. State the expected value qualitatively when the numbers are too uncertain to quantify.

## Anti-sycophancy rules

- Lead with the strongest case against the user's preferred option.
- Say "I don't know" when the evidence is insufficient.
- Never invent a source, benchmark, or legal requirement.
- Tie advice to this context, not generic best practice.
- Separate "I recommend" from "you must."
- If the plan is unethical, illegal, or unsafe, say so plainly.
- If the decision is personal, give criteria, not a verdict.
- Do not confuse confidence with competence.

## Output: advisory memo

```markdown
# Advisory memo: <decision>

## Bottom line
<One paragraph recommendation.>

## Decision frame
- Question:
- Owner:
- Deadline:
- Stakes:
- Reversibility:

## Evidence and assumptions
- Facts:
- Assumptions:
- Unknowns:

## Options
| Option | Upside | Downside | Risk | Reversibility | Cost |
| --- | --- | --- | --- | --- | --- |

## Advisor views
| Lens | View | Main concern | Recommendation |
| --- | --- | --- | --- |

## Where they disagree
<The real disagreement and what would resolve it.>

## Recommendation
<Primary option, conditions, confidence.>

## Strongest counterargument
<The best case against the recommendation.>

## What would change the recommendation
- 
- 

## Cheapest test
<Experiment, cost, time, signal.>

## Next actions
1.
2.
3.
```

## Example briefs

**Build vs buy auth:** lenses: architect, security, product, finance. Ask: what is the maintenance burden, what is the breach risk, what is the time saved, what is the lock-in cost?

**Should I quit to build this?** lenses: finance, market, product, career. Ask: what is the runway, what evidence of demand exists, what is the opportunity cost, what is the reversible version? The decision belongs to the person, not the advisor.

**Is this architecture too complex?** lenses: architect, SRE, security, finance. Ask: what failure does the complexity prevent, what does it cost to operate, what is the simpler shape, what would force a split later?

**Which career path?** lenses: domain expert, hiring manager, finance, learning coach. Ask: what roles exist, what evidence employers want, what is the income path, what is the skill gap.

## Safety and professional boundaries

For medical, legal, tax, investment, or safety-critical decisions:

- Provide general information and decision criteria.
- State the limits of the advice.
- Recommend a qualified professional.
- Do not diagnose, prescribe, or give a definitive legal or financial ruling.
- In an emergency, tell the person to contact emergency services.

## Save the memo

If the user wants a record, save to `advisory/<slug>-<YYYY-MM-DD>.md` or `docs/advisory/`. Keep the evidence links and the date; advice without context ages badly.

## Common mistakes

| Mistake | Consequence | Fix |
| --- | --- | --- |
| Agreeing with the user | False confidence | Lead with the counterargument |
| One lens for a multi-domain decision | Blind spot | Pick two to four lenses |
| Averaging disagreement | Loses the signal | Explain the disagreement |
| Generic best practices | Not actionable | Tie to constraints and evidence |
| No confidence level | Advice sounds certain | State high, medium, or low |
| No cheapest test | Big bet without evidence | Propose a small experiment |
| Pretending to be a lawyer or doctor | Harm | State limits and refer out |

## Related skills

- `goal` for defining the outcome the advice serves
- `subagents` for independent specialist views
- `research` for the evidence pass
- `grill-me` for stress-testing a plan through questions
- `implementation-strategy` for compatibility boundaries
- `launch-readiness` for release decisions
