# VIOLET — session handoff

**As of:** November 25, 2026 (Wednesday), 16:41 ET (from `date`).
- **Task:** D:L1280, the 11/25 close read (PROME prome-77), in the session Will opened 15:34 ET for a status report.
- **Limits:** $0; no score, band, threshold or letter change.
- **Canonical numbers:** [STATUS](STATUS.md); record `research/2026-11-25_close-read/GRADE.md`; KB-VIO-409.

## CHANGES SINCE (11/25 10:19 → 16:35 ET)

- VIX 34.95 at 09:45 → **28.29** on the close print; S&P 6,970 → 7,182.78. HY 11/24 = 372 first-published.

## WHAT I DID

- Boot; five WALTER cards (013, 018, 022, 024, 034); COR-20261125-22 NO-OP; KB-VIO-408 opens `combo:VIOLET/systematic-selling`.
- Close read on the print, PROVISIONAL: 7th inverted close (0.9293), prediction 2' ARMED, day-7 VIX under 31; nothing else fired.
- Artifacts republished: cheat-sheet version 17, Operating Picture version 19.
- PREDICTIONS.tsv: Confidence filled from letters, UNSCORED where the letter states none, `Date_Made` added.
- D:L342 note to RED and REGINALD; TERRY packet; WALTER question 4 answered in the record.
- **20:04 ET, Will's ask (options 1 and 3):** sticky-credit study and VIX options read, `research/2026-11-25_sticky-credit/FINDINGS.md`, KB-VIO-410. My unscored 2' fail view moved 88% → about 75%. Artifacts and NEXUS_BRIEF corrected. VIX_OPTIONS 11/25 rows: OI restored by hand after an after-hours run zeroed it (STATUS queue item 7).

## NEXT SESSION

1. **11/27 boot (short session, closes 13:00):** confirm 11/25 on History for every print cell; `backfill.py --spot-only` (SKEW for 11/25 left blank on purpose: the vendor filled 139.16 forward); **no 11/26 VX_DAILY row** (D:L342); re-score convergence; mark thesis row 2' ARMED on History with CHANGELOG; HY 11/25 cell.
2. Prediction 2' window: 10 closes 11/27, 11/30, 12/01, 02, 03, 04, 07, 08, 09, 10. First close at 25.00 or under = fails.
3. If the 11/25 archive differs from the print, correct both Artifacts.
4. Fix `vix_options.py` / `_daily_log.py`: an OI of 0 must not overwrite good OI (STATUS queue 7).
5. About 12/04 Nvidia 10-Q (VULCAN); 12/16 SOQ vs Z6 25.0258 [11/25], PRED-11 resolves, L441. CFTC 11/24 report due by 12/01.

## CARRY-FORWARD

- **Owners:** RED (FT-06, FT-10, RED-29) · LIQUID (HY) · HENRY (gamma, SPX) · BOND (rates) · VULCAN (Nvidia) · ORACLE (priced odds) · SAM (BOJ, JPY, SoftBank) · REGINALD (REG-T-04).
- **Cboe History high/low cells carry bad prints**; closes only.
- **Vendor index prints keep moving to about 16:31 ET** (15-minute delay): read the close print after 16:32, twice. One pull at 16:20 to 16:22 ET failed on all ten symbols and recovered unaided.
- **yfinance 1-minute bars:** filter on today's date (cross-date hazard pre-open).

## OPEN HYPOTHESES

**Day-7 level split (exploratory, n = 13, overlapping).** 5 of 7 at 31 or more, 0 of 6 under. Live case: 28.29.
