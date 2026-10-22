---
name: freelance-operator
description: "Use when the user wants to win, scope, price, or deliver freelance work, especially AI, software, product, or design services: finding leads, positioning an offer, writing proposals, qualifying clients, setting scope and price, running discovery, managing delivery, or turning a project into a case study and retainer. Use this whenever the user mentions freelancing, clients, Upwork, Fiverr, proposals, retainers, lead generation, business development, or product leadership for client work."
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
  suite: "freelance-operator"
---

# Freelance Operator

This is the front door to the freelance business suite. It treats freelancing as a pipeline and a delivery system, not a collection of tactics.

The research is blunt: the open marketplace is crowded and price-compressed, while specialist and direct work pays far more. The median posted AI rate is around **$27.50/hour**, with most hourly postings under $50; the high end is a different market built on proof, specialization, and accountability. The way out of the commodity layer is not a better profile. It is a narrower promise, measurable evidence, and a delivery process a client can trust.

## The contract

When this skill is invoked:

1. **Classify the request.** Is this lead generation, positioning, product/scope, pricing/proposal, delivery, or retention?
2. **Load the smallest useful sub-skill.** Read its `SKILL.md` before acting.
3. **State the mode in one line.** Example: "Using `freelance-lead-gen` to define the ICP and offer, then `freelance-business-development` to price it."
4. **Produce a business artifact.** ICP brief, offer one-pager, outreach sequence, discovery script, proposal, SOW, product brief, delivery plan, case study, or retainer plan.
5. **Tie it to a number.** Leads, reply rate, discovery rate, close rate, average contract value, gross margin, utilization, or retention.
6. **Leave one clear next action.**

A list of tips is not a deliverable. If the request is real work, load the first skill and produce the artifact.

## The freelance reality

| Layer | Typical shape | What wins |
| --- | --- | --- |
| Commodity marketplace | Low posted rates, high competition, price-sensitive buyers | Speed, clarity, a narrow offer, proof |
| Specialist / direct | Higher rates, fewer buyers, trust-based | A specific outcome, case studies, referral network |
| Retainer / embedded | Monthly capacity, ongoing ownership | Reliability, communication, measurable impact |

The barbell is real: you can compete on price at the bottom, or you can compete on **verified uncertainty reduction** at the top. The middle is the worst place to be — more expensive than commodity, less proven than a specialist.

## What clients actually buy

Clients do not buy "AI agents," "full-stack development," or "product management" in the abstract. They buy:

- a risky decision made safer
- a costly workflow made faster
- a broken system made reliable
- a vague idea turned into a testable scope
- a launch that does not embarrass them
- someone who will own the outcome when it gets messy

Translate every service into one of those outcomes. Then prove it with a number, a demo, a case study, or a low-risk paid diagnostic.

## The pipeline

```text
ICP -> offer -> lead sources -> qualification -> discovery
    -> proposal -> close -> onboarding -> delivery
    -> proof -> case study -> referral/retainer
```

Each stage has an owner, an artifact, and a metric. If a stage has no artifact, it is a vibe.

| Stage | Artifact | Metric |
| --- | --- | --- |
| ICP | One-page ideal client profile | Qualified leads per week |
| Offer | One-page outcome + scope + proof | Reply and discovery rate |
| Lead sources | Channel list and weekly cadence | Cost per qualified conversation |
| Qualification | Fit score and disqualifiers | Discovery show rate |
| Discovery | Notes, current state, impact, urgency | Proposal rate |
| Proposal | Situation, scope, price, acceptance | Close rate |
| Onboarding | Access, roles, cadence, success criteria | Time to first value |
| Delivery | Plan, updates, QA, change control | On-time, rework, margin |
| Proof | Case study with before/after | Referrals and inbound |
| Retention | Review, retainer, roadmap | Renewal and expansion |

## Positioning

Strong positioning has four parts:

1. **Who** — a specific buyer with a specific context.
2. **Outcome** — the measurable change they want.
3. **Mechanism** — why your approach works, in one sentence.
4. **Proof** — evidence that you have done it or can de-risk it.

Weak: "I build AI agents and full-stack apps."

Strong: "I help insurance operations teams cut document-review time with a measured RAG pipeline, and I publish the evaluation harness that proves the accuracy."

The second is narrower, easier to refer, and easier to price.

## Qualification

Ask:

- Is there a real budget and a decision-maker?
- Is the pain urgent enough to act now?
- Can I deliver the outcome with the access and time available?
- Is the scope clear enough to estimate?
- Is the client respectful and responsive?
- Is this a fit for my proof and capacity?

Disqualify quickly when:

- the buyer wants a free spec or "just a quick call" with no budget
- the scope is "make us an AI strategy" with no owner
- the deadline is impossible and the client will not move it
- payment terms are unsafe
- the work requires a license or access you do not have
- the client has fired multiple contractors for the same reason

## Pricing

Use value and risk, not hours alone:

- **Fixed fee** for a defined outcome with clear acceptance criteria.
- **Retainer** for ongoing capacity and ownership.
- **Hourly** only as a fallback or for exploratory work.
- **Paid diagnostic** for ambiguous, high-risk problems.

Price the outcome, the risk you absorb, and the speed you provide. State assumptions, exclusions, revision limits, and change-control rules. A lower price with vague scope is not cheaper; it is a future dispute.

## Delivery

Every engagement needs:

- a kickoff with goals, roles, cadence, and access
- a written scope and acceptance criteria
- a weekly update with progress, decisions, risks, and next actions
- a decision log and change-request process
- QA and handoff standards
- a closeout with documentation, training, and a case study

The client should never wonder what is happening. Silence is interpreted as risk.

## Ethics

- Do not fabricate case studies, metrics, testimonials, or client names.
- Do not use outreach lists that violate platform rules or privacy law.
- Do not take work you cannot deliver.
- Do not hide AI use when the client or contract requires disclosure.
- Do not hold client data, credentials, or code hostage.
- Do not optimize for utilization at the expense of the client's outcome.

## Role routing

| Request | Load | Artifact |
| --- | --- | --- |
| "Find clients", "leads", "outreach", "ICP" | `freelance-lead-gen` | ICP, offer, list, sequences, pipeline |
| "Price this", "proposal", "contract", "retainer" | `freelance-business-development` | Proposal, SOW, pricing model |
| "Scope this", "product manager", "roadmap", "PRD" | `freelance-product-lead` | Product brief, PRD, roadmap |
| "Deliver this", "client updates", "handoff", "case study" | `freelance-client-delivery` | Delivery plan, status report, handoff pack |

## Output format

End with:

```markdown
### Freelance operating status
- Stage:
- Artifact produced:
- Metric to watch:
- Biggest risk:
- Next action:
```

The business improves when the next action is specific and the metric is measurable.
