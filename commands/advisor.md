---
description: Get specialist advice, a second opinion, or a red-team review
---

Use the `advisor` skill to advise on: $ARGUMENTS

Do this:

1. Frame the decision: question, context, options, stakes, reversibility, deadline, owner, and evidence.
2. Choose two to four relevant specialist lenses. Pick from product, market, architecture, security, data, UX, QA, SRE, finance, legal, marketing, operations, domain expert, or learning/career.
3. Separate facts, assumptions, opinions, and unknowns. Do not invent sources or benchmarks.
4. Get independent views first. If subagents are available, use the `subagents` skill so one advisor does not anchor another.
5. Surface disagreements instead of averaging them.
6. Give a primary recommendation, the conditions under which it holds, confidence, the strongest counterargument, and what would change your mind.
7. Propose the cheapest test before a large commitment.

If the decision requires a lawyer, doctor, accountant, or other licensed professional, give general criteria and say so. Do not make the decision for the human owner.

If I ask for a record, save an advisory memo to `advisory/<slug>-<date>.md` using `templates/advisory-memo.md` from the `advisor` skill.
