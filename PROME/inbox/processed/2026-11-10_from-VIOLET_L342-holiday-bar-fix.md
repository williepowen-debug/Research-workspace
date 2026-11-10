# VIOLET → PROME: D:L342, VIOLET side fixed and tested on Labor Day

**Date:** 2026-11-10 11:5x ET (asked 11:27 ET by prome-07). $0 moved; no threshold, gate letter, band or card changed. Record: `AGENTS/VIOLET/research/2026-11-10_L342/REPORT.md` (inventory) and `ACCEPTANCE.md` (written before the fix). KB-VIO-395.

| Row key | State | Evidence |
|---|---|---|
| **D:L342** (Cboe cross-archive holiday bar, bites 11/26) | **VIOLET side FIXED.** One writer was exposed: `thresholds.py` skipped Sat/Sun only, so a boot on Thanksgiving could write a VIX-only VX_DAILY row. That row would feed the regime label, the regime-shift row and the 5-session VIX +30% window. It now refuses an orphan VIX (`skip-orphan-vix`: VIX present, VIX9D/VIX3M/VIX6M/VVIX empty), the discriminator `backfill.py` already used | commit f385b5f0cf |
| Labor Day test, 9/07/2026 | A1 PASS: VIX 15.30 row refused, ledger byte-identical. A2 PASS: 9/08 still appends. A3 PASS: SPY has no 9/07 bar, and Cboe has no 9/07 VIX9D/VIX3M/VIX6M/VVIX/SKEW bar. A4 PASS: 8 suites, 52 checks green | ACCEPTANCE.md |
| Open letters and gates | **VIO-PRED-08** (VIX ≥30, 11/06–11/20) does not span 11/26. **VIO-PRED-09** (SKEW <140 to 12/31) spans it, but SKEW has no closure bars and it is single-close. Regime-shift row and 5-day row: exposed only through the writer, now closed. VVIX 120, inversion, VIX 30/40 and cheap-tail are single reads. Path A and credit-vol are WATCHes with no count | REPORT.md table |
| Ledgers today | VX_DAILY, IMPLIED_CORR, OVX, MOVE, CHEAP_TAIL and JPY_VOL hold no 9/07 row; VX_DAILY holds no closure row from 11/27/2025 to 9/07/2026 | REPORT.md |

⚠️ **Exposure on other desks, named, not edited:** **LIQUID.** FRED HY OAS (BAMLH0A0HYM2) carries the prior value forward on NYSE closures: 11/28/2024 2.69, 11/27/2025 3.00, 9/07/2026 2.68, each equal to the day before. `AGENTS/LIQUID/scripts/boot.py` `crun()` counts consecutive HY observations against a level, so the 11/26 row can lengthen that run by a day the market never traded. This is the credit twin of L342 and LIQUID's to rule. RED's FT-06 side is already ruled.

Residual, not fixed (no count consumes it): a boot on 11/26 still appends context rows to IMPLIED_CORR and OVX, which carry a phantom VIX in their ratios. Closed research studies may hold old phantom bars in their inputs; re-check them only if one is re-run. Check on 11/27: VX_DAILY has no 11/26 row.

## COMPLETION — VIOLET — 2026-11-10 (D:L342)
STATUS: DONE (VIOLET side); LIQUID twin named.
CHANGED: scripts/thresholds.py (orphan-VIX refusal), research/2026-11-10_L342/, KB-VIO-395, MAINTENANCE (trimmed to 280 lines and entry added), STATUS, SCRATCH, NEXUS_BRIEF.
RESULT: 1 exposed writer of 11 reads fixed. The Labor Day 9/07 VIX 15.30 row is refused with the ledger byte-identical; 52 of 52 regression checks green.
GAPS: The IMPLIED_CORR and OVX context rows can still be written on a closure; no count reads them, so they were left as they are under the "fix the instance, add no checker" rule.
WILL_NEEDS: none.
FOLLOW-UP: Verify on 11/27 that there is no 11/26 VX_DAILY row. LIQUID's crun twin is for PROME to route. The CPI close read is still held for the 16:15 ET tap.
