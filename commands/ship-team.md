---
description: Run the full build-ship team from recon to release
---

Use the `build-ship-team` skill for this request: $ARGUMENTS

Read `~/.agents/skills/build-ship-team/SKILL.md` and `references/gates.md` before acting.

Run the team in this order, skipping only what the lane does not need:

1. **Frame.** Write `.ship/brief.md`: outcome, user, success criteria, non-goals, constraints, lane. Ask at most three blocking questions; otherwise record assumptions and proceed.
2. **Recon.** Dispatch the `scout` subagent for `.ship/context-brief.md`. Skip only if this session already mapped the repo.
3. **Plan.** Dispatch the `architect` subagent for `.ship/plan.md` when the change crosses three files, changes a public interface, touches data, or has more than one plausible shape. Otherwise write a five-line plan.
4. **Build.** Dispatch one `builder` per vertical slice, serial by default. Give each builder the slice number, `.ship/brief.md`, `.ship/plan.md`, the owned files, the verification commands, and its report path.
5. **Verify.** Dispatch the `verifier` subagent after every slice. Do not accept the builder's own test claim. A gate that does not exist is `NOT RUN`, never passed.
6. **Review.** Dispatch the `reviewer` subagent before release, and always for auth, money, data, public API, migrations, or UI.
7. **Ship.** Dispatch the `shipper` subagent only when verification passes and review is not `REQUEST CHANGES`.

Rules:

- Pick the smallest lane that can still prove the change works. Fast = lead + verifier. Standard = lead + builder + verifier. Full = all seven.
- One writer per file. Serialize shared files.
- No merge to `main`, force-push, or production deploy without explicit human approval.
- Evidence over claims: every gate needs a command and output.
- If the work is UI, require `.ship/design-record.md` and the anti-generic gate at `~/.agents/skills/frontend-design/references/anti-generic-aesthetics.md`.

End with:

```text
Gate:
Lane:
Verified:
Open:
Next:
```
