---
name: finding_guard_correctness_and_wiring_are_independent
description: "A guard's CORRECTNESS and its WIRING are independent properties — we verify the first and assume the second. n=4 in one day across 3 agents: the check ran, the check was right, and nothing downstream was gated on its result."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 38654ed8-2008-4dea-b6c0-f64a4c624254
  modified: 2026-08-18T19:59:28.725Z
---

**A guard's correctness and its wiring are independent properties.** Verifying that a check is *correct* tells you **nothing** about whether anything *acts on its result*. The failure is never in the check — it is downstream, in the connection between the check and the action it was supposed to prevent.

**Why:** this is the failure mode that arrives **after** you fix [[finding_mechanize_the_cap_not_the_ritual]]. That finding says a remembered ritual is performed as often as someone remembers, so mechanize it. Do that, and the next defect is subtler and worse: **the mechanism exists, it runs, it is right, and its verdict is connected to nothing.** A ritual that isn't performed leaves you with *no* confidence. A correct guard nothing is gated on leaves you with *false* confidence — the check's green output reads as coverage. **Every instance below was authored by someone who had just been thinking carefully about exactly this class of problem.**

**How to apply:** for each guard you write or rely on, **name the specific action it must prevent, then trace the mechanical path by which a failing guard prevents it.** If you cannot name the path in one sentence, the guard is decorative. Concretely — the four shapes seen 2026-08-18, VIOLET n=2 · TERRY n=2:

- **Separated by a newline instead of `&&`.** TERRY's python assertion guarded a `git commit --amend`; the assertion **failed correctly** and the amend ran anyway, rewriting another agent's already-public commit. In shell, a failing guard does not stop the next line — only `&&`, `set -e`, or an explicit exit does.
- **A result nothing reads.** VIOLET's edit script asserted on a mismatched string and, being all-or-nothing, **wrote nothing — correctly.** The `git commit` was a *separate invocation* in the same call, so it committed a message describing changes that were not in the diff. **A commit message is a claim about a diff and inherits no truth from the script meant to produce it.**
- **A success report not scoped to the goal.** VIOLET's `backfill.py` printed `touched 36 rows` while leaving the one date-hole it exists to fill. The report was *true* and did not answer *did the gap close?* **Verify the fill, not the exit code.**
- **The documenting tool suffering the documented defect.** TERRY's `python3 -c "…"` written to *document* a backtick defect was itself backtick-substituted.

**The generalisation worth carrying:** we habitually audit whether a check is *right* and almost never audit whether it is *load-bearing*. Ask of any guard: **"if this fires, what stops?"** — and if the honest answer is "I would notice," it is not a guard, it is a log line. Related: [[finding_concurrent_commit_index_race]] (TERRY's half — three values race: the hash, the owner, and whether it is public), and [[finding_record_of_an_action_is_not_the_action]], which is this same gap seen from the artifact side.
