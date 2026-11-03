---
description: Ship one thin vertical slice fast, with independent verification
---

Use the `build-ship-team` skill in **fast** or **standard** lane for: $ARGUMENTS

The goal is one shipped, verified slice, not a plan for the whole product.

## Do this

1. **Write the brief in five lines.** Outcome, user, success test, non-goal, constraints. Put it in `.ship/brief.md`. Do not ask more than three questions; assume and record the cost.
2. **Pick the smallest slice.** One end-to-end behavior a user can see. If the request is a layer ("build the models"), restate it as the thinnest path through the stack.
3. **Recon only what the slice touches.** Use `grep`/`glob` and the nearest existing example. If the repo is genuinely unknown, dispatch `scout` with a thirty-five step cap. Otherwise skip it.
4. **Plan in five lines.** Files, interface, test, rollback. Skip `architect` unless the change crosses three files, touches a public interface, data, or auth.
5. **Build.** Do it yourself in the fast lane, or dispatch one `builder`. Smallest diff. Test the behavior. No drive-by refactors.
6. **Verify independently.** Dispatch `verifier` or, if unavailable, re-read the diff in a fresh pass and run the real gates: format, lint, typecheck, unit, integration, build, and the acceptance test. Record the command and output.
7. **Stop at the gate.** Do not start the next slice until this one is verified. Report what is shipped, what is not, and the next slice.

## Fast-lane rules

- Time box: 15–30 minutes for fast, 1–3 hours for standard.
- One slice, one writer, one verification pass.
- No new dependency without a stated reason.
- No merge to `main`, force-push, or production deploy without explicit approval.
- If the change turns out to touch auth, money, data, a migration, or a public API, stop and switch to the full lane.
- UI work still needs `.ship/design-record.md` and the anti-generic gate.

End with:

```text
Shipped: <what is verified>
Evidence: <command and result>
Not shipped: <the next slice>
Next: <one action>
```
