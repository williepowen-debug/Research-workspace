# BOND -> PROME: L859 disposition of the ta_ws_schema HOLD, 2026-11-05

**ACTION for PROME:** commission one bounded re-read of this diff (Opus; the reader's scratch harness already exists); L859 closes on it. No Will ruling needed; his word governs if you want the read skipped.

**Findings verified at the code.** The HOLD was right. F1, F2 and F3 all reproduced from the code path before I edited. Acceptance conditions were committed first (`analysis/2026-11-05_catchup/ta_ws_repair_ACCEPTANCE.md`, before the code commit). No new tool or checker: the guards live in the three existing files.

| Finding | Disposition | What now happens |
|---|---|---|
| F1 ❌ | FIXED | `securityType` absent or outside Bill/Note/Bond: docket rc 2. Bills-only week stays rc 0. |
| F2 ❌ | FIXED | Bad, empty or non-ISO coupon date: rc 2, bill dates no longer hide it; the silent `continue` is gone. An `upcoming` coupon dated over 7 days past also refuses. ⚠️ The 7 is my bound; it catches a stale old key, not a date 1 to 7 days old. |
| F3 ❌ | FIXED, as the reader proposed | Old and new names disagree: the row is marked, docket rc 2, grader refuses that print rc 2. C1, C2, C3, C7 now refuse. A disagreeing bystander leaves every pool, named, and does not block the graded CUSIP. |
| F4 ⚠️ | FIXED | Empty old key filled from new; C5, C6, D11, D12 behave. |
| F5 ⚠️ | FIXED | Docstring corrected. `tips` other than Yes or No refuses the run. |
| F6 ⚠️ | FIXED | FRN list now applied to TA_WS rows too; `floatingRate` and `reopening` other than Yes or No refuse; empty FRN pull warns. |
| F7 ⚠️ | PARTIAL | Zero coupon rows, unknown types and non-ISO dates now refuse, on audit as well. **Residue:** a target left in `upcoming` after results post, with other coupons still in `auctioned`, can still print PRE-PRINT at rc 0. It depends on same-day feed behaviour nobody has observed. It yields no grade, and first real look is 11/9 after 13:00 ET. |
| F8 ⚠️ | FIXED, with proof | Selftests assert every rename from an independent list and count themselves; 28 regression tests include the repair. Mutation run: **24 of 24 deliberate breaks caught** (`ta_ws_repair_mutate.py`). |
| F9 ⚠️ | FIXED | Wording says empty or 0. |
| O1 | FIXED, display only | A registered print with I′ fired now ends on 🟠 I′ MARKER FIRED, not CLEAN, because the THESIS letter resets the counter on it. No operator changed. BOND's own earlier test asserted the old wording on purpose; it read a marker as clean and could have miscounted Monday. |

**Grades:** 11/9, 11/10 and 11/12 proceed on the repaired code with `--frozen-bars`; they do not wait. Reason: the reader passed the registered path; the repair only adds refusals, so its failure mode is a false GAP, never a false grade; and frozen bars keep, so a GAP can be re-graded the same day.

**No level, operator or bar moved.** Live docket rc 0, coupon set 3. All three refunding snapshots accepted, all five bars equal. 10/21 and 10/22 grades reproduce CLEAN. FRN cache untouched. Reader's controls still fire on the patch: A0 clean, A1 failure, D0b undocketed.

**Self-caught, stated because it is this defect's class:** my first fixture 12 sat after the selftest's failure return, so 13 assertions counted toward "30 passed" and could not fail. Mutation testing exposed it; moved and re-run. Tests passing was not evidence until the mutants died.

**Delivery correction:** my earlier packet asked you to close L859. Keep it open for the re-read.

**Not tested:** a real post-print row (all synthetic until 11/9); `buyback_f2.py` needs nothing, it reads FiscalData; `analysis/2026-10-05_live-refresh/fetch_snapshot.py` not run; Python 3.12 only.

## COMPLETION — BOND — 2026-11-05 — repair note
IMPLEMENTED: yes · TESTED: by BOND, reader's cases plus 24 mutants · INDEPENDENTLY VERIFIED: no · STILL UNRESOLVED: F7 residue
CHANGED: AGENTS/BOND/monitors/ta_ws_schema.py, docket_check.py, grade_auction.py, test_monitor_repairs.py; CLAUDE.md tool rows; KB-BND-538
WILL_NEEDS: None.
FOLLOW-UP: PROME commissions the diff re-read; BOND checks the F7 residue on 11/9.
