---
title: Senior Developer Thinking
aliases:
  - How Senior Developers Think
  - Senior Engineering Judgment
type: reference
created: 2026-10-20
updated: 2026-10-20
tags:
  - engineering
  - senior-dev
  - decision-making
  - agents
  - reference
---

# Senior Developer Thinking

> [!info] What this is
> The reasoning model behind the senior-dev skills. It explains how senior and staff engineers frame problems, make trade-offs, reduce risk, and use AI without surrendering judgment. The operational playbook is [[Senior Developer Operating System]]; the skill reference is [[OpenCode Skills]].

> [!tip] The short version
> Seniority is not writing more code faster. It is framing the real problem, choosing what not to build, making trade-offs with incomplete information, and owning the outcome through production.

## The shift: from maker to decision-maker

Less senior work is often judged by output: tickets closed, code shipped, features delivered. Senior work is judged by outcomes and judgment:

- Can you handle ambiguity and find the real problem?
- Can you choose what not to build?
- Can you make a defensible trade-off with incomplete information?
- Can you predict second-order effects?
- Can you reduce risk before adding scope?
- Can you own the system through production?
- Can you multiply other people through review, docs, and delegation?

A useful test: a senior engineer can explain not only what they chose, but what they did not choose and why.

## The mental models

| Model | What it means in practice |
| --- | --- |
| Problem before solution | The request is often a proposed solution. Find the outcome underneath it before choosing a stack or writing code. |
| Systems thinking | The code is one part of a system that includes people, incentives, operations, and feedback loops. Optimizing one part can worsen the whole. |
| Second-order thinking | Ask "and then what?" Caching improves latency, then creates invalidation bugs. A process change saves time, then creates a review bottleneck. |
| First principles | Break the problem down to invariants and rebuild from what is true, instead of copying a template that does not fit. |
| Inversion | Define failure first. "What would make this fail?" surfaces risks that a success-first plan hides. |
| Reversibility | Separate one-way doors from two-way doors. Spend judgment proportional to how expensive the decision is to undo. |
| Circle of competence | Know what you know and what you do not. Bring in a specialist or gather evidence when the decision is outside your competence. |
| Leverage | Prefer the smallest change with outsized effect: remove a requirement, automate a step, reuse a service, or delegate with context. |
| Feedback loops | Instrument, measure, review, and retrospect. A system without feedback cannot improve. |
| Trade-offs | There is no best practice in a vacuum. Name what you optimize for and what you give up. |
| Boundaries and interfaces | Clear contracts and ownership beat clever internals. Design what changes together and what must stay independent. |
| Risk and uncertainty | Buy information cheaply. Test the assumption that could kill the project before building the parts that cannot. |
| Communication | Writing is part of engineering. Decisions, assumptions, and revisit conditions must survive the meeting. |

## Senior vs junior behavior

| Situation | Less senior | More senior |
| --- | --- | --- |
| A feature request arrives | Starts building | Asks what outcome the request serves |
| A technology choice appears | Picks the popular option | Compares options against constraints and reversibility |
| A problem is complex | Adds more code | Looks for the smallest leverage point |
| A plan looks good | Starts executing | Pre-mortems the plan and tests the riskiest assumption |
| A change works locally | Ships it | Checks failure modes, observability, and rollback |
| A decision is made | Moves on | Writes down the decision, alternatives, and revisit conditions |
| AI produces code | Accepts it if it looks plausible | Verifies behavior, reviews the diff, and tests the edges |
| Work is done | Hands it off | Owns the outcome through production and learning |

## Staff engineer archetypes

Will Larson's research describes four common Staff-plus patterns. They show that "senior" is contextual, not one ladder.

| Archetype | What they optimize | Typical work |
| --- | --- | --- |
| Tech Lead | Team execution and technical direction | Scoping, unblocking, cross-team relationships, delegating, alignment |
| Architect | Direction and quality of a critical domain | Constraints, interfaces, technical debt, long-term evolution |
| Solver | Resolving knotty, high-risk problems | Deep diagnosis, containment, handoff to the owning team |
| Right Hand | Executive leverage | Cross-functional problems at the intersection of business, technology, people, and process |

The lesson for the suite: match the mode to the problem. A solver needs `systematic-debugging`; a tech lead needs `subagents` and `agent-delegation`; an architect needs `advisor` and ADRs; a right hand needs `goal` and stakeholder framing.

## Engineering judgment under uncertainty

Judgment is a closed-loop decision process, not a personality trait:

1. **Frame** the decision, the owner, the stakes, and the deadline.
2. **Separate** facts, assumptions, unknowns, and opinions.
3. **Generate** at least two real alternatives, including "do nothing" or "buy instead of build."
4. **Choose criteria** before comparing options: cost, reversibility, risk, time, maintainability, user impact.
5. **Test** the weakest assumption with the cheapest experiment.
6. **Decide** and record the trade-off, the failure path, and the conditions that would reopen it.
7. **Monitor** the leading signals and update.

This is the same shape as `advisor` (lenses and recommendation), `project-kickoff` (ADR), and `launch-readiness` (go/no-go and rollback).

## What the AI-era evidence says

### DORA 2025

The 2025 DORA report, *State of AI-assisted Software Development*, found:

- AI adoption is nearly universal: about 90% of technology professionals use AI at work.
- Most users report individual productivity gains.
- Higher AI adoption is associated with **both** greater software delivery throughput and greater instability.
- A large minority lack trust in AI-generated code; one summary puts "little or no trust" at around 30%.
- The returns depend on the surrounding system: clear AI stance, healthy data ecosystems, AI-accessible internal data, strong version control, working in small batches, user-centric focus, and quality internal platforms.

Implication: AI is an amplifier. It magnifies good engineering systems and bad ones. The senior response is not "use more AI." It is "fix the system, keep batches small, and verify."

### Context engineering

Birgitta Böckeler's 2026 primer describes context engineering as "curating what the model sees so that you get a better result." Key points:

- Context includes instructions, guidance, tools, MCP servers, skills, files, and conversation history.
- Skills are lazy-loaded context; the model or human decides when to load them.
- Subagents run in their own context window and can be parallelized, which helps with focused reviews and orchestrations.
- Too much context reduces effectiveness and increases cost.
- Build context iteratively; do not dump copied instructions into every session.

Implication: `AGENTS.md`, specs, task packets, and a small set of well-scoped skills are more valuable than a giant prompt.

### Spec-driven development

The 2026 spec-driven development literature distinguishes three levels of rigor:

- **Spec-first:** write the spec before implementation, then let it guide the work.
- **Spec-anchored:** keep the spec as a reference and validation artifact.
- **Spec-as-source:** the spec is the primary artifact and code is generated or verified from it.

The common workflow is Specify → Plan → Tasks → Implement → Validate. The evidence also shows that structured workflows can still be "context blind" if intermediate artifacts are not grounded in the repository.

Implication: a spec is not paperwork. It is a contract that makes agent output checkable.

### Code review and small changes

Google's engineering practice research found that small changes are reviewed faster and are easier to understand, test, and roll back. *Software Engineering at Google* recommends changes around 200 lines and describes review as knowledge sharing and team building, not just bug detection.

Implication: AI-generated code does not change the review economics. It makes small batches and clear ownership more important, because generation is cheap and review is not.

## The senior operating principles

1. Frame the problem before choosing the solution.
2. Think in systems and second-order effects.
3. Classify decisions by reversibility.
4. Make trade-offs explicit.
5. Reduce uncertainty before adding scope.
6. Seek leverage, not volume.
7. Design boundaries and interfaces.
8. Prefer boring defaults and clarity.
9. Own the outcome through production.
10. Write decisions down.
11. Build feedback loops and measure stability, not just speed.
12. Multiply others through review, docs, and delegation.
13. In the AI era, keep judgment and verification human-owned.

## How this maps to the skills

| Principle | Skill |
| --- | --- |
| Frame the outcome | `goal` |
| Pressure-test a decision | `advisor` |
| Match specialists to work | `subagents` |
| Turn an idea into a first milestone | `project-kickoff` |
| Make a repo legible and maintainable | `codebase-playbook` |
| Manage risk with tests | `testing-strategy` |
| Delegate with context and ownership | `agent-delegation` |
| Make knowledge durable | `documentation-system` |
| Ship with recovery | `launch-readiness` |
| Plan and execute | `writing-plans`, `executing-plans`, `test-driven-development` |
| Verify before claiming done | `verification-before-completion`, `code-change-verification` |

## Practical checklist

Before a consequential decision:

- [ ] What is the real problem, and who owns the outcome?
- [ ] Is this a one-way or two-way door?
- [ ] What are the alternatives, including doing nothing?
- [ ] What are the facts, assumptions, and unknowns?
- [ ] What is the cheapest test of the riskiest assumption?
- [ ] What would make us reverse this decision?
- [ ] What is the failure path and the rollback?
- [ ] Who needs to know, and where is it written down?

Before shipping AI-assisted work:

- [ ] Is the spec or task packet unambiguous?
- [ ] Is the context curated rather than dumped?
- [ ] Is the change small enough to review?
- [ ] Did a human verify the behavior, not just the claim?
- [ ] Are security, data, and permission boundaries explicit?
- [ ] Is there a fallback for model or prompt failure?
- [ ] Are we measuring rework and stability, not only speed?

## Sources

- DORA, *State of AI-assisted Software Development 2025*: https://dora.dev/research/2025/dora-report
- DORA AI Capabilities Model: https://dora.dev/ai/capabilities-model/report/
- Google Cloud, "Introducing DORA's inaugural AI Capabilities Model" (2025): https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model
- Will Larson, *Staff Engineer* archetypes: https://staffeng.com/guides/staff-archetypes
- Titus Winters, Tom Manshreck, Hyrum Wright, *Software Engineering at Google*: https://abseil.io/resources/swe-book
- Google, "Modern Code Review: A Case Study at Google": https://dl.acm.org/doi/pdf/10.1145/3183519.3183525
- Birgitta Böckeler, "Context Engineering for Coding Agents" (Martin Fowler, Feb 2026): https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html
- Deepak Babu Piskala, "Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants" (arXiv 2602.00180, 2026): https://arxiv.org/abs/2602.00180
- "Spec Kit Agents: Context-Grounded Agentic Workflows" (arXiv 2604.05278, 2026): https://arxiv.org/abs/2604.05278
- CIO, "Decision-making under uncertainty: A practical playbook for engineering leaders" (Feb 2026): https://www.cio.com/article/4125879/decision-making-under-uncertainty-a-practical-playbook-for-engineering-leaders.html

## Related notes

- [[Senior Developer Operating System]] — the operational playbook.
- [[OpenCode Skills]] — the full skill reference.
- [[Goal to Execution]] — goal, advisor, and subagent workflow.

*Last verified: 2026-10-20.*
