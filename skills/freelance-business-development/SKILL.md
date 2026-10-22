---
name: freelance-business-development
description: "Use when the user needs to position, price, propose, negotiate, or contract freelance work: choosing a business model, setting rates, writing a proposal or statement of work, handling scope changes, negotiating terms, or structuring a retainer. Use this whenever the user mentions pricing, proposals, SOWs, contracts, retainers, discounts, negotiations, or making freelance work profitable."
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
  suite: "freelance-operator"
---

# Freelance Business Development

Business development is where the work becomes a business. The goal is not to win every deal. It is to win the right deals at a price that covers delivery, risk, and the cost of running the business.

Use this skill after discovery, when you know the buyer's problem and need to shape the commercial offer.

## Workflow

### 1. Position the offer

Write one sentence:

```text
I help <specific buyer> achieve <measurable outcome> through <mechanism>,
proven by <evidence>.
```

Then list:

- the buyer's current alternative
- why it fails or costs too much
- what you do differently
- the proof
- the risk you remove
- the next step

If the sentence could describe a hundred freelancers, it is not positioning.

### 2. Choose the commercial model

| Model | Use when | Watch |
| --- | --- | --- |
| Fixed fee | Outcome is clear and scope can be bounded | Scope creep, hidden discovery |
| Retainer | Ongoing capacity or ownership | Utilization, response expectations |
| Hourly | Exploratory or unpredictable work | Penalizes efficiency, caps upside |
| Paid diagnostic | Problem is ambiguous or high-risk | Must produce a concrete artifact |
| Value-based | Impact is measurable and trust is high | Attribution and baseline disputes |
| Equity / hybrid | Long-term alignment, early-stage client | Illiquidity, governance, opportunity cost |

Most solo freelancers should anchor on fixed-fee projects and retainers, with hourly only as a fallback. Fixed fees reward outcomes; retainers reward reliability.

### 3. Price the work

Build the number from three layers:

1. **Delivery cost** — your time, subcontractors, tools, data, travel, payment fees.
2. **Risk cost** — ambiguity, dependencies, revisions, payment delay, opportunity cost.
3. **Value capture** — a share of the outcome you create.

Formula:

```text
Floor   = delivery cost + taxes + fees + a living margin
Target  = floor + risk premium + value share
Walk-away = the price below which the work is not worth doing
```

Do not quote a single number until you know:

- scope and acceptance criteria
- assumptions and exclusions
- client dependencies
- revision limit
- payment schedule
- who owns the output
- what happens if the client delays

### 4. Write the proposal

Use a decision document, not a brochure.

```markdown
# Proposal: <outcome> for <client>

## Situation
What is happening, and what it costs.

## Objective
The measurable outcome and success criteria.

## Approach
Phases, activities, and why this approach fits.

## Deliverables
What the client receives, in concrete terms.

## Timeline
Milestones and dependencies.

## Acceptance
How we agree the work is done.

## Assumptions and exclusions
What is included and what is not.

## Investment
Price, payment schedule, and validity.

## Why me
Relevant proof, not a life story.

## Next step
One action to proceed.
```

Keep it short enough to read. Put the price near the end, after value is clear.

### 5. Protect the scope

Every proposal needs:

- a clear definition of done
- a revision limit
- a change-request process
- client responsibilities and response times
- assumptions about access, data, and approvals
- a delay clause
- a termination clause

When scope changes, do not absorb it silently. Say:

```text
That is a new requirement outside the agreed scope. I can add it for <price>
and <time>, or trade it against <existing item>. Which works better?
```

### 6. Negotiate on the whole deal

Do not negotiate only price. Trade across:

- scope
- timeline
- payment schedule
- risk
- case-study rights
- referral commitment
- retainer length

If the buyer asks for a discount, ask what they will remove or commit to. A discount with no trade teaches the buyer that your price is fictional.

Know your walk-away. Be willing to say no politely.

### 7. Contract basics

A statement of work should cover:

- parties and effective date
- scope and deliverables
- timeline and milestones
- fees, expenses, taxes, and payment terms
- late payment and suspension rights
- intellectual property ownership and license
- confidentiality and data handling
- warranties and disclaimers
- limitation of liability
- change control
- termination and wind-down
- governing law and dispute process

This is not legal advice. For material contracts, have a lawyer review the template in your jurisdiction.

### 8. Structure the retainer

A retainer is not "hours on call." Define:

- monthly capacity or outcome
- response-time expectations
- included work and exclusions
- reporting cadence
- rollover policy
- renewal and price review
- termination notice

Price for availability and priority, not just hours. If the client consumes more than the capacity, the overage rate should make the constraint real.

### 9. Invoice and collect

- Invoice on the agreed schedule, not when you remember.
- Use a written payment policy and late fee.
- Stop work on overdue invoices according to the contract.
- Keep records of deliverables and approvals.
- Separate business and personal finances.
- Reserve for taxes and slow months.

## Proposal review checklist

```markdown
## Fit
- Buyer and problem:
- Outcome and success metric:
- Why us:

## Scope
- Deliverables:
- Assumptions:
- Exclusions:
- Acceptance:
- Change control:

## Commercials
- Price and margin:
- Payment schedule:
- Risk:
- Walk-away:

## Next step
- Decision date:
- Owner:
```

## Common failure modes

- **Custom proposal before discovery** — you price a guess.
- **Hourly pricing for a fixed outcome** — you absorb the risk.
- **Unlimited revisions** — the project never ends.
- **No acceptance criteria** — "done" becomes an argument.
- **Discount without a trade** — margin disappears and scope grows.
- **No deposit** — the client has no commitment.
- **Vague IP terms** — the client assumes everything, including reusable tools.
- **Retainer without capacity limits** — you become an employee at a contractor's price.

## Composition

- `freelance-operator` — business context.
- `freelance-lead-gen` — discovery and qualification.
- `freelance-product-lead` — scope and product definition.
- `freelance-client-delivery` — delivery and change control.
- `stop-slop` — clear, non-generic writing.

## Output format

End with:

```markdown
### Commercial recommendation
- Offer:
- Model:
- Price:
- Margin:
- Key assumptions:
- Walk-away:
- Next action:
```

A good deal is profitable, deliverable, and reversible. If it is only one of those, it is not a good deal.
