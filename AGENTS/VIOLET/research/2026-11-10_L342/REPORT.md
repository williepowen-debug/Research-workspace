# D:L342: VIOLET's exposure to Cboe holiday bars, and the one fix (2026-11-10)

**Stamp:** 2026-11-10 11:27–11:31 ET (from `date`; corrected from a hand-typed 11:5x). Commissioned by PROME prome-07, time-boxed at about 30 minutes. Acceptance condition written first: [ACCEPTANCE.md](ACCEPTANCE.md). $0 moved; no threshold, gate letter, band or card changed.

## Inventory: VIOLET reads that take VIX from Cboe History, FRED or yfinance

| Read | Count type | Spans 11/26? | Could a closed-day bar advance it? |
|---|---|---|---|
| VX_DAILY ledger writer `thresholds.py` (every boot) | the base every row-count reads | yes | **YES, before the fix.** It skipped Sat/Sun only. A boot on 11/26 would have written a VIX-only row. **Fixed:** `skip-orphan-vix` |
| VX_DAILY ledger writer `backfill.py` | base | yes | No. It already refuses to create an orphan-VIX row; `vx_daily_gapcheck.py` uses the same discriminator |
| VIO-PRED-08, VIX ≥30 on any close, 11/06–11/20 | single close | no | No: the window ends 11/20 |
| VIO-PRED-09, SKEW <140 on any close, to 12/31 | single close, SKEW | yes | No. SKEW History has no 9/07 bar (Cboe omits closures), and the live writer nulls a SKEW quote stamped before today |
| Regime label and regime-shift outbound row | single close | yes | **Was exposed through the ledger writer** (a phantom row carries a regime label). Closed by the same fix |
| VIX +30% in 5 days, HY 5-session ≤ +25bp | 5-session window over VX_DAILY | yes | **Was exposed** (a phantom row shortens the window by one real session). Closed by the same fix. The HY leg is read on the VIX session dates, so a FRED HY holiday row does not enter |
| VVIX 120, VIX3M/VIX inversion, VIX 30/40 | single close | yes | No count. Inversion needs VIX3M, which has no closure bar |
| Cheap-tail alert (live) and its backtest | single read; the backtest groups fire days | yes | No. The backtest joins VIX, VVIX and SKEW per date, so a VIX-only bar drops out |
| `convexity_read.py` implied-realized spread | percentile on a date-keyed join with SPX | yes | No. It is already date-joined, not positional |
| Path A WATCH, credit-vol WATCH (ends 11/17) | no count | n/a | No |
| Boot context ledgers: IMPLIED_CORR, OVX, MOVE, JPY_VOL | daily context, no sustain count (COR1M first-tell and MOVE pause/resume are retired) | yes | No count to advance. ⚠️ A boot on 11/26 can still append a context row whose OVX/VIX or corr inputs use a phantom VIX. Not fixed (no count consumes it); read with care |
| Closed research studies (`sustain_run_query.py`, `two_anchor_ladder.py`, `diet_coiled_spring.py`, `skew_trajectory.py`, `regime_termination.py`, analog pulls) | historical runs and episodes | n/a | Inputs may contain past phantom bars. These are not live letters; re-check if any is re-run |

**Ledgers clean today:** VX_DAILY, IMPLIED_CORR, OVX, MOVE, CHEAP_TAIL and JPY_VOL hold no row on 9/07/2026. VX_DAILY holds none on any NYSE closure from 11/27/2025 to 9/07/2026, and git history shows no 9/07 VIX 15.30 row ever written.

## The fix

`scripts/thresholds.py` `append_daily_log()`: refuse a row when VIX is present and VIX9D, VIX3M, VIX6M and VVIX are all empty. A refusal is recoverable, because backfill.py creates any real session's row from History. A written phantom row is removed by nothing.

**Test, Labor Day:** Cboe History 9/07/2026 shows VIX 15.30, with no bar in VIX9D, VIX3M, VIX6M, VVIX or SKEW. SPY (yfinance daily) has bars on 9/03, 9/04, 9/08 and 9/09, and none on 9/07. A1 PASS: the 9/07 row was refused and the ledger copy is byte-identical. A2 PASS: the 9/08 row was appended. A3 PASS: the companion rule and the SPY rule agree. A4 PASS: `run_tests.py`, 8 suites, 52 checks green; the closeout guard is green. The live VX_DAILY is unchanged.

**Why the companion form, not an SPY-bar lookup:** it is the discriminator the ledger's other writer already uses (13/13 exact at source, MEMORY). It needs no second fetch. An SPY daily bar for today is no more available pre-open than the companions are.

## Exposure outside VIOLET (named, not edited)

- **FRED HY OAS (BAMLH0A0HYM2) carries rows on NYSE closures, carried forward from the prior day:** 11/28/2024 2.69 (= 11/27), 11/27/2025 3.00 (= 11/26), 1/20/2025 2.64 (= 1/17), 9/07/2026 2.68 (= 9/04). **LIQUID's `scripts/boot.py` `crun()` counts consecutive HY observations against a level**, so a Thanksgiving carry-forward row can lengthen that run by one day the market never traded. This is the credit twin of D:L342. LIQUID owns it.
- RED's FT-06 counts VIXCLS ×5; RED has ruled its own side (D:L342).
