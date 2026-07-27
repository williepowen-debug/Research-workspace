---
name: finding-date-gate-beats-weekday-name
description: "Schedule instructions on a LITERAL DATE, never a weekday name. A wrong day-name ('Mon 8/4' when 8/4 is a Tuesday) survives every reader and propagates; gating on 2026-08-03 makes the ambiguity un-actionable. The fix pattern for the n=4 weekday-error class — and it also decides whether a date defect is blocking or bookkeeping."
metadata:
  node_type: memory
  type: finding
---

**A weekday name attached to a date is a second, unchecked assertion.** `date +%A` is never run, the two halves can disagree, and the wrong half propagates at full confidence. Fleet count reached **n=4 within one week** across four agents.

**The fix is not more vigilance — it is removing the redundant field from anything operative.**

**The case (PROME, 2026-07-27).** A Batch-3 orchestration packet scheduled *"Kickoff **Mon 8/4**."* **2026-08-04 is a Tuesday; Monday is 8/3.** It propagated to a delivered inbox packet (×2), `ACTIVE_DECISIONS`, HANDOFF and a daily memory — and **the recipient acked the packet without catching it**, which is the point: a wrong weekday is invisible to readers because both halves look like data.

When six owner packets were then written from that origin doc, they were gated **`"begin at your first boot on or after Mon 2026-08-03"`** — a literal ISO date, day-name present only as decoration. Consequences:

- **The ambiguity never reached the six agents doing the work.** Whichever way the origin was resolved, the instruction was already unambiguous.
- **It reclassified the defect from blocking to bookkeeping.** A multi-day research leg does not care about a one-day start offset, so the open question could wait for the operator instead of stalling the dispatch.
- **When the operator ruled (8/3, "the day name was right, the number wrong"), zero owner packets needed editing.** Only the origin-record surfaces were swept.

**How to apply:**
- **Operative instructions carry an ISO date** (`2026-08-03`), optionally with the weekday as *decoration* — never the weekday as the identifier.
- **Prefer "on or after \<date\>" to "on \<date\>"** for work with multi-day duration. It absorbs a one-day error by construction and states the real constraint (don't start before X) rather than a false one (start exactly on X).
- **Ask whether a date defect is blocking or bookkeeping** before escalating. If every reading lands inside the intended window, fix the record and keep moving; don't stall the work on a resolution that changes nothing.
- **`scripts/claim_check.py` catches this mechanically** (`weekday` check). It caught this instance on its first live run, ~18 minutes after being built. Note its documented limits: it cannot tell **mention from use**, so quoting a wrong weekday *in order to correct it* still flags.
- **When sweeping the fix,** grep the OLD PREMISE PHRASES too, not just the date (`DOCKET.tsv` re-date rule). In this case most `"Aug 4-11"` hits repo-wide were a **different item** — the NY Fed HHDC window, already correctly re-dated off *its own* weekday error — and a find-replace would have corrupted a correctly-handled correction.

Related: [[finding_weekday_assumed_never_evaluated]] (the error class, n=3 → this made n=4) · [[finding_premise_residue_survives_date_fix]] (a clean date check is necessary, never sufficient) · [[feedback_date_specificity_weakest_link]] · [[finding_redated_falsifier_inherits_premise]].
