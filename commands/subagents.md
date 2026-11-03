---
description: Split work across specialist subagents
---

Use the `subagents` skill to split this work across specialist subagents: $ARGUMENTS

Produce:

1. The goal and the decision this work serves.
2. A role roster: the minimum set of specialists needed, with a mission and deliverable for each.
3. A dependency graph showing what must happen before what.
4. A parallel plan: which agents can work at the same time, which must be serial, and why.
5. File or area ownership: one owner per file, with shared files serialized.
6. A subagent brief for each role, using `templates/subagent-brief.md`.
7. Review gates: mission fit, scope, correctness, security, and independent verification.
8. An integration owner for the seams and the final gate.

Use the `agent-delegation` skill for task packets, worktrees, status reporting, and review discipline. Do not run more than two to four agents at once unless the interfaces and ownership are proven. Do not let agents merge to main. Do not delegate product or security decisions.

If the work is small or sequential, say so and recommend one agent instead of forcing a roster.
