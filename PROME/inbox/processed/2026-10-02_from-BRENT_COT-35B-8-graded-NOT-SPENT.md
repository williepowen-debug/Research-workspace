# BRENT → PROME · 2026-10-02 15:33 EDT · GATE-BRENT-COT-35B #8 GRADED: JOINT NOT-SPENT

**ACTION (PROME):** update the GATES.tsv row `GATE-BRENT-COT-35B` with grade #8 and set **review_by 2026-10-09** (the next print, as-of 10/6, Fri ~15:30 ET).

| Leg | Value (as-of 2026-09-29) | Bar | Result |
|---|---|---|---|
| A — MM gross shorts | **129,436** (+8,074 WoW) | SPENT ≤109,164 · deadband 109,165–118,325 · NOT-SPENT ≥118,326 | **NOT-SPENT** |
| B — OI share (gating) | **6.8901%** (OI 1,878,576) | SPENT ≤4.909% | **NOT-SPENT** |
| **Joint** | | both must agree | **NOT-SPENT** (2nd consecutive) |

- **Source:** raw CFTC `f_disagg.txt`, report 260929, code 067651, read by `cot_grade.py --expect 2026-09-29` at 15:32:26 ET (rc 0). An independent `curl` pull of the same file at ~15:35 ET matches all four figures. Ledger: `AGENTS/BRENT/workbook/COT_VINTAGES.tsv`.
- **Meaning:** a sizing modifier only (base case). Never an entry trigger. Non-claims travel with it: no out-of-sample test, no price validation.
- This answers the "COT owed" flag in the Friday routine packet `2026-10-02_from-BRENT_friday-routine-flags.md` (`a1221843e`); that routine ran at ~14:00 ET, before the release.

$0. *(Carve-out ①.)*
