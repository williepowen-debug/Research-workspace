---
name: finding_reconcile_mismatch_does_not_say_which_side_is_wrong
description: "A count-vs-contents reconcile flags that two sides DISAGREE, never which is wrong — 'adjust the count to match' destroys the evidence. And errors that cancel hide each other, so flagged discrepancies UNDERSTATE defects."
metadata: 
  node_type: memory
  type: finding
  originSessionId: cf5575f0-f79f-44e8-92eb-0be9e98e0a50
  modified: 2026-08-10T19:23:43.378Z
---

A reconciliation check that compares a declared **count** against actual **contents** (index header vs rows, ToC vs sections, ledger total vs entries, manifest vs files) reports one fact: **the two sides disagree.** It does **not** report which side is wrong — and the cheap fix is always to move the count, because the count is one character and the contents are many.

**That fix is frequently the wrong one, and it destroys the evidence that would have found the real defect.**

**The case (WALTER, 2026-08-10).** `board_reconcile` flagged two sections of a 687-signal index: `FED_FRAMEWORK` ToC=45 / actual=44, and `HYDROCARBON_INFRA` ToC=36 / actual=37. The obvious reading — "the counts drifted, correct them" — was wrong in **both** directions. The counts were **right**. Three rows written in a prior session had each been appended to the end of the section **immediately PRECEDING** the correct one (inserted just before the target's `##` header rather than at the end of its rows). Correcting the counts would have:
- silently corrupted **two sections that were entirely correct**,
- left **all three rows still misfiled**, and
- **destroyed the only signal** that a misfile existed, since the check would then read green.

**⚠️ The second half is the one that generalises hardest: ERRORS THAT CANCEL HIDE EACH OTHER.** There were **three** misplaced rows and only **two** flagged sections. A row leaving section A and a different row arriving into section A **net to zero** and the check reads clean. So:

> **The number of flagged discrepancies is a LOWER BOUND on the number of defects, never a count of them.** A reconcile that flags N problems may have 2N. And a **grand total** that reconciles (here: 687 = files = rows = ToC) proves only that the errors were **conservative**, not that they were few — a pure permutation reconciles perfectly at the top level.

**How to apply:**
- On any count-vs-contents mismatch, **find the specific missing or extra item before touching the number.** If you cannot name it, you have not diagnosed it.
- **Diagnose by joining on identity, not by arithmetic** — check each row against its own declared home (here: each signal file's `cluster:` header vs the section its row sits in). The arithmetic tells you something is wrong; only the join tells you what.
- **Never adjust a declared count to silence a check.** If the count turns out to be wrong, fix it *after* naming the item, and say which side moved.
- **When you find one misfile, sweep the WHOLE structure, not the flagged sections.** Cancelling siblings are invisible by construction and sit in sections the check called clean.
- **Prefer checks that report the offending ITEM over checks that report a DELTA.** A delta-only check is satisfiable by editing the delta.

Sits with [[finding_verify_counts_before_propagating]] (verify a count before carrying it) and [[finding_silent_blank_evades_review]] (an absence that reads as clean). Inverse of the usual worry: here the ledger was honest and the **contents** had drifted — the direction people rarely check, because contents feel like ground truth.
