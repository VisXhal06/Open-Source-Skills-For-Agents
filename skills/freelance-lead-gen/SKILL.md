---
name: freelance-lead-gen
description: "Use when the user needs more freelance clients or a repeatable lead engine: defining an ideal client profile, choosing a niche, building an offer, finding leads, writing outreach, qualifying prospects, booking discovery calls, or tracking a pipeline. Use this whenever the user mentions lead generation, prospecting, cold email, Upwork proposals, referrals, inbound, booking calls, or getting their first client."
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
  suite: "freelance-operator"
---

# Freelance Lead Generation

Lead generation is not "send more messages." It is a system that connects a specific buyer with a specific outcome and produces a qualified conversation.

The best lead engine for a solo freelancer is usually not the widest channel. It is the narrowest promise with the strongest proof, distributed through channels where the buyer already looks.

## Workflow

### 1. Define the ideal client profile

Write one page:

```markdown
## ICP
- Industry / niche:
- Company size:
- Role / decision maker:
- Trigger event:
- Current workaround:
- Cost of the problem:
- Desired outcome:
- Budget range:
- Where they gather:
- Who else is involved:
- Disqualifiers:
```

A good ICP is narrow enough to name 50 real companies or people. "Startups" is not an ICP. "B2B SaaS companies with 20–100 employees, a support team of 5+, and a documentation backlog after a funding round" is.

### 2. Build the offer

The offer is the bridge between the ICP and a first conversation.

```markdown
## Offer
- Who it is for:
- Outcome:
- Deliverable:
- Time to first value:
- Proof:
- Price band:
- Risk reversal:
- What is excluded:
- Next step:
```

Prefer a **paid diagnostic** or a small fixed-scope entry offer over a large custom proposal. It lowers buyer risk, lets you inspect the real problem, and creates a natural path to the bigger engagement.

### 3. Choose channels

| Channel | Best for | Constraint |
| --- | --- | --- |
| Warm network | First clients, trust | Limited reach |
| Referrals | High-fit buyers | Requires proof and asking |
| Marketplaces | Fast conversations, price pressure | Commodity competition |
| Outbound email | Narrow ICP, direct problem | Deliverability and relevance |
| LinkedIn / communities | Credibility and conversation | Time and consistency |
| Content / case studies | Inbound, authority | Slow compounding |
| Partnerships | Access to trusted buyers | Alignment and margin |

Do not run five channels badly. Pick one primary channel and one support channel for 30 days.

### 4. Build a qualified list

For each lead, capture:

```text
Name, role, company, website, source, trigger, observed problem,
fit score, contact, last touch, next action, disqualifier
```

Use public information only. Verify the person and role. Do not scrape private data or violate platform terms. Keep the list small enough to personalize; 50 well-researched leads beat 5,000 scraped addresses.

### 5. Write outreach that earns a reply

A useful message has:

1. **Specific observation** — proof you looked at their context.
2. **Problem hypothesis** — a cost they recognize.
3. **Relevant proof** — a result, case study, or diagnostic.
4. **Low-friction next step** — a question or a short call, not a pitch deck.

Template:

```text
Subject: <specific observation>

Hi <name>,

I noticed <specific thing> at <company>. That usually means <problem hypothesis>,
which can <cost>.

I recently <proof / result>. I have an idea for <specific improvement> that
would take <small scope>.

Worth a 15-minute conversation to see if it is relevant?

<name>
```

Avoid:

- "I hope this email finds you well"
- a paragraph about your background before the buyer's problem
- fake familiarity
- attachments on the first touch
- five follow-ups in three days
- claims you cannot prove

### 6. Follow up with a cadence

A simple sequence:

| Day | Action |
| --- | --- |
| 0 | Personalized first touch |
| 3 | Short follow-up with one new piece of value |
| 7 | Relevant case study or diagnostic offer |
| 14 | Polite close-the-loop message |
| 30 | Keep-in-touch only if relevant |

Stop when asked. Respect opt-outs and platform rules. The goal is a conversation, not the last word.

### 7. Qualify before the call

Use a short score:

| Dimension | Question | 1–5 |
| --- | --- | --- |
| Problem | Is the pain real and costly? | |
| Urgency | Why now? | |
| Budget | Is there money and authority? | |
| Fit | Can I deliver the outcome? | |
| Access | Can I get data, systems, and decisions? | |
| Respect | Is the buyer responsive and honest? | |

Book the call only when the score is strong enough to justify the time. Send a short agenda and ask for the context you need.

### 8. Run discovery

Ask in this order:

1. What is happening now?
2. What have you tried?
3. What does it cost you?
4. Why now?
5. What does success look like?
6. Who decides and who is affected?
7. What budget and timeline are realistic?
8. What would make this a bad fit?

Do not pitch during discovery. Take notes, reflect the problem back, and propose a next step.

### 9. Track the pipeline

Minimum stages:

```text
New -> Researched -> Contacted -> Replied -> Discovery booked
    -> Discovery held -> Proposal -> Won / Lost / Nurture
```

Track:

- qualified leads added per week
- reply rate
- discovery rate
- proposal rate
- close rate
- average contract value
- time to first response
- source of each win

Review weekly. Kill the channel that produces no qualified conversations after a fair test; double down on the one that does.

## Lead-gen audit

```markdown
## Funnel
- ICP:
- Offer:
- Primary channel:
- Leads/week:
- Reply rate:
- Discovery rate:
- Close rate:
- Average value:

## Bottleneck
- Biggest drop-off:
- Hypothesis:
- Experiment:
- Success threshold:
```

## Compliance and ethics

- Follow platform rules for proposals and messaging.
- Follow privacy and anti-spam law in the buyer's jurisdiction.
- Do not buy or scrape personal data without a lawful basis.
- Do not misrepresent results, clients, or availability.
- Do not mass-send identical messages.
- Honor opt-outs immediately.

## Composition

- `freelance-operator` — overall business context.
- `freelance-business-development` — proposal and pricing after discovery.
- `freelance-product-lead` — scope the problem.
- `research` and `firecrawl-search` — market and buyer research.
- `stop-slop` — remove generic AI outreach language.

## Output format

End with:

```markdown
### Lead engine
- ICP:
- Offer:
- Channel:
- List size:
- Outreach cadence:
- Metric to watch:
- Next action:
```

A lead engine is working when the right buyer replies, not when the send count is high.
