---
name: finding_freshness_check_cannot_catch_a_fresh_lie
description: Staleness checks compare mtime and so pass a file that is brand new and affirmatively false; the missing test is agreement with an external source of truth, not age
metadata:
  node_type: memory
  type: feedback
---

**A staleness check measures AGE, not AGREEMENT.** A file can be two minutes old and assert the exact opposite of the truth, and every mtime-based guard will pass it forever.

Found n=3 in one VIOLET session (2026-07-28), each from a different direction, all in the same blind spot:

- **`TRADE.md` read `ACTIVE POSITIONS: None.`** for 17 hours while a live position carried $287.70 into FOMC with a mandatory review 2 days out. `ledger_staleness.py --trade` returned **`ok +2d`** — it compares the file's mtime to `STATUS.md`'s. Nothing anywhere compared its *content* to STATUS's position state.
- **A dashboard cell carried `IV/RV 3.24`** — a value that appears nowhere in the series it cited. It was the **OVX ratio from the adjacent row**: two unrelated dimensionless fields both called "ratio", both ≈3. Broadcast to the domain owner twice before their event. Not stale — *current, accurate, and about something else.*
- **A ledger row labelled `basis=TICK`** where only 1 of 5 columns was a tick; the other 4 were the prior settle, and a ratio was computed across them. A row-level label cannot describe a row whose columns have different as-of dates.

**Why this class survives every guard we build:** freshness checks catch values that look *old*, and review catches values that look *wrong*. This class is neither — the value is plausible, current, and internally consistent. It fails only against an **external** referent that nothing is checking.

**How to apply:** for any surface that restates truth owned elsewhere, add a **positive** check, not a staleness check — *"if STATUS shows a LIVE position, TRADE.md must name the same identifier, else fail loud."* Both files are usually already read at boot, so it costs ~20 lines and no new data pull. For ledger-derived dashboard values, **cite the ledger COLUMN rather than the script** (`[JPY_VOL.iv_rv10, 7/27]`, not `[CONF] jpy_vol.py`) — a column citation is mechanically checkable against the file; a script citation is not.

**Two aggravating patterns seen alongside it:**
- A surface that has failed in **both** directions (a dead position shown as OPEN for 3 weeks, then a live one shown as None) is not drifting — it is **unmaintained by construction**. Check whether it appears in the numbered write-back steps or only in a "update when X changes" table row. A condition to remember is not a step to execute.
- A file can declare its own auditable contract and breach it for weeks. `CANARY_MAP.md` defined a DARK threshold and was violating it on 5 rows by up to 21 days, because its enforcement line — *"extend `ledger_staleness.py` to this file's pull dates = a future small ask"* — was never built. See [[finding_mechanize_the_cap_not_the_ritual]] and [[finding_banner_is_a_warning_not_a_fix]].

**Extension n+1 (2026-08-16, PROME spine-audit #9 process review — the SEQUEL failure): the agreement check's truth source becomes SELF-SEALING.** Once you build the positive check this memory prescribes, every disagreement resolves FOR the referent by construction — so an error *inside the referent* is not merely undetected, it is actively **enforced**: the checker rewrites correct surfaces to match the wrong canon. Live shape: the weekly spine audit reconciles 14 boot-read docs against `PROME/DOCKET.tsv` as canon; a wrong DOCKET date would have been propagated into every calendar view as a "fix," and the only DOCKET verifier (`firetime_check`) covered rows ≤7d out — the 170-row far tail had no audit at all. **How to apply:** when you promote a file to truth-source status for an agreement check, that promotion creates a NEW obligation — the referent needs its own independent audit *at its own sources* (sampled is fine; deterministic monotone-counter seeding, since calendar-field seeds degenerate at boundary arithmetic — a day-of-month seed froze on one sample slice at STEP=7 and at 31-day month boundaries). And read the anchor audit's CLEAN honestly: it certifies no *divergence* found, never that the referent is externally true — a row and its artifact sharing a wrong origin pass clean.

Related: [[finding_plausible_stale_value_evades_review]] (this is its sharper sibling — wrong-series beats merely-stale), [[finding_mtime_is_corrupted_by_git_sync]] (the *other* reason mtime lies), [[finding_reconcile_match_on_key_not_substring]], [[finding_record_of_an_action_is_not_the_action]], [[finding_verification_zero_is_ambiguous]] (the CLEAN-reading discipline), [[finding_automation_reads_its_own_error_back_as_canon]] (the intra-tool version of the same loop).
