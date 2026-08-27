# Gate C C8 — RULED: CONTINUE

**Date:** 2026-08-27 ~17:5xZ, Will in-session (RED's S36 sitting).
**Ruling:** Will, on RED's C8 review recommendation (`AGENTS/RED/reports/2026-08-27_KERNEL_GATE_C_C8_REVIEW.md`): **"I approve CONTINUE — go ahead with the six conditions."** Verbatim, in-session.
**Scope of the word:** approves the CONTINUE recommendation for Gate C after pilot `LIVE-2026-0001`, and directs RED to execute the review's six conditions (§5 of the review) — including the root `CLAUDE.md` custody-enumeration reconcile, which is Will-gated and is hereby worded.
**Executor:** RED (reviewer-implements; PROME as custodian should re-read the runbook and test edits at its next boot — flagged via RED OUTBOX-026).
**Recorded by:** RED, same sitting, per review finding N6 (mid-process rulings get a durable record at ruling time, not only inside a later packet).

## The six conditions (review §5, restated for the record)

1. Runbook step 6 re-worded — events byte-identical + zero event writes; views differ only in `render_as_of`, verified mechanically; view-integrity weight on step 8. Doc-only.
2. Runbook steps 1/7/9 drop the hold-local push assumption — no step may depend on a commit remaining local. Doc-only.
3. Runbook step 9 becomes an affirmative close (`revoked_at` set + committed) + stop-condition discipline (no live applies post-stop until ruled; preserve before diagnosing; rulings appended to the ruling record at ruling time). Doc-only.
4. Durable transcript of every sitting, committed with the closeout packet. Doc/process-only.
5. `test_prepare_pilot` fixture fixed (mirror from the pinned source commit); suite re-run to green. Test-code only.
6. Housekeeping: READINESS_PLAN checkpoint rows advanced; root `CLAUDE.md` custody enumeration reconciled to cover activation documents, ruling records, and closeout packets.

**Execution record:** conditions applied in the commits immediately following this file; suite state after condition 5 recorded in the commit message that carries it.
