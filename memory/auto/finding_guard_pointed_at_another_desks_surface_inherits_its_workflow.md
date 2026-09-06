---
name: finding_guard_pointed_at_another_desks_surface_inherits_its_workflow
description: "A guard re-pointed at ANOTHER desk's directory inherits that desk's workflow as a hidden dependency — VIOLET's two blocking closeout guards globbed PROME/inbox/ and went red the minute PROME consumed the memo to processed/; newest-by-filename then graded the wrong same-day memo while reporting green."
symptoms: "closeout guard reports the delivery memo MISSING right after a successful delivery; a guard that goes red precisely when the recipient is prompt; an always-red check that everyone learns to ignore; newest file chosen by name and an addendum loses to the morning memo; a re-pointed contract that was green in testing and red in production"
metadata:
  node_type: memory
  type: finding
---

**When you point a guard at a surface another desk owns, you are not pointing at a file — you are pointing at that desk's workflow, and every step of it becomes an unstated precondition of your check.**

**The instance (VIOLET, 2026-09-06, KB-VIO-250 + its addendum):** PROME's 9/5 flag asked VIOLET to re-key the retired `LAST_COMPLETION.md` overwrite to dated delivery memos. VIOLET's sweep found the flag named two lines while **five live consumers** existed, two of them **BLOCKING closeout guards** (`writeback_order_check.py`, `surface_agreement.py`) that tracked the file — so freezing it per the flag alone would have **inverted a control** (a frozen file never catches up to STATUS; the ordering check goes red at every closeout; an always-red guard gets silenced, taking its real coverage with it). VIOLET re-pointed both guards to `PROME/inbox/*_from-VIOLET_*.md` — **and shipped the same inversion from the other side:** PROME `git mv`s a consumed memo to `PROME/inbox/processed/` within minutes of delivery (it did so to VIOLET's memo inside one minute), so both guards reported the memo **MISSING** for a delivery that had succeeded. Red precisely when the recipient is prompt. A second defect in the same code: **newest-by-filename** — an ISO date prefix orders days, not the packets inside one, so the 10:4x `_addendum-` memo lost to the 10:2x `_ft10-` memo because `a` < `f`, and the check graded the older delivery while reporting green.

**Why it recurs:** the re-point is tested against the surface as it looks at the moment of writing. The other desk's workflow (consume → move → rotate → archive) runs on its own clock and is documented, if at all, on that desk's surfaces — nothing in your directory names it. The check passes in testing, fails in production, and the failure reads as the other desk's fault.

**How to apply:**
- **Before re-pointing a guard at another desk's directory, read what that desk DOES to the surface after the event you care about** (its consume step, its processed/ move, its rotation cadence) and encode it: glob both `inbox/` and `inbox/processed/`; treat *delivered-and-filed* as delivered.
- **Order candidates by COMMIT TIME, never filename or mtime** (a date prefix orders days; git sync restamps mtime — [[finding_mtime_is_corrupted_by_git_sync]]); when several same-day artifacts exist, read them together — an addendum contradicting its memo IS a cross-surface disagreement.
- **A flag that says "re-point X" is half the lesson; grep for every consumer of X first** — the census names the lines it found, not the controls that depend on them ([[finding_scan_keyed_on_naming_reads_local_form_as_absence]]).
- **Fix the shape, not the desk:** the rule now lives in `PROME/COMPLETION_SPEC.md` method 1 (the surface the next re-keying desk reads), and any guard-inversion candidate is a desk-hardening pattern for DAEDALUS. Related: [[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]], [[finding_a_check_that_only_advises_is_overridden_the_control_is_downstream]].
