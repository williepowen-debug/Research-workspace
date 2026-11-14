# CRU-11 grade (DOCKET L606) and WQ-670 re-read — 2026-11-14

**Session:** CRUISE, Claude Code (Opus 5.5), desktop, spawned by PROME prome-fe. Retrieval 2026-11-14 11:12:50 ET (`date -Iseconds` inside `pull.py`). Raw data: `evidence.json` in this folder.

## 1. CRU-11 — FAILED on the letter

Frozen resolver (PREDICTIONS.tsv line 12, approved WQ-242): NCLH_TR_cum − RCL_TR_cum at the window close ≤ −5pp = CONFIRMED; > −5pp = FAILED; both pinned sources unreadable = NO-VERDICT. 2026-11-14 is a Saturday, so the window close is the nearest preceding session, Friday 2026-11-13.

| Leg | Base close 2026-10-02 | Window close 2026-11-13 | Cumulative TR |
|---|---|---|---|
| NCLH (adj close) | $15.14 | $17.96 | **+18.6262pp** |
| RCL (adj close) | $277.74 | $323.27 | **+16.3930pp** |
| **Spread NCLH − RCL** | | | **+2.2331pp** (threshold ≤ −5pp) |

| Check | Result |
|---|---|
| Pinned source | yfinance `download(auto_adjust=False)["Adj Close"]`, repository `.venv`, retrieved 2026-11-14 11:12 ET |
| Cross-check (letter's second source) | `FORGE/tools/market-data/fetch.py price --history 40`: identical closes at both endpoints, spread **+2.2331pp**. ⚠️ Same vendor (Yahoo), so agreement shows the two code paths read the same tape, not independent confirmation |
| Dividends in window | None for NCLH or RCL (RCL last ex-date 2026-09-17), so adjusted = raw closes across the window; no basis gap |
| Session count | 30 in-window sessions after the base, matching the letter |
| Readable? | Both legs readable from both sources at both endpoints, so NO-VERDICT does not apply |

**Verdict: FAILED.** NCLH did not underperform RCL; it outperformed by 2.23pp. Path context, not graded: no in-window close reached −5pp; NCLH's widest underperformance was −2.52pp (10/27); its widest outperformance was +8.53pp (10/29, the day NCLH beat and raised Q3, +13.45%). The K-shape dispersion this row tested did not hold on the tape after the 10/2 base. This agrees with exit rule 1 having fired 10/29 (NCLH raised); it does not test the narrower NCLH leverage and deposit read on `VX-CRU-05`.

## 2. WQ-670 A encoded — `VX-CRU-01` re-read at live closes

Ruling (Will 2026-11-11 10:25 ET): GREEN = a fall of less than 10% from the fixed raw 2026-02-06 close $33.99, i.e. any close above $30.591; one close is enough. Lower cells unchanged.

| Close (raw, yfinance auto_adjust=False; fetch.py agrees) | vs $33.99 | Reading |
|---|---|---|
| 11/9 $30.81 | −9.36% | GREEN(1) |
| 11/10 $30.74 | −9.56% | GREEN(1) |
| 11/11 $30.68 | −9.74% | GREEN(1) |
| 11/12 $29.34 | −13.68% | YELLOW(2) — all three cruise names fell about 4% (CCL −4.37%, NCLH −4.04%, RCL −3.94%) on an S&P ETF day of −0.35%; cause not checked |
| **11/13 $29.23** | **−14.00%** | **YELLOW(2) — state at the latest close** |

Net: the row read GREEN on 11/9–11/11 under the ruling and is back at YELLOW(2) at the 11/13 close, so the desk total stays **9/20**. CCL went ex-dividend $0.15 on 11/06; the band uses raw closes, so that does not move the reading.

## 3. D:L715 — not gradeable today

The test is the state on 2026-11-17 (exchangeables outstanding AND Free Liquidity < $800M). EDGAR submissions for NCLH (CIK 0001513761, retrieved 2026-11-14 11:12 ET): latest filing is the 2026-10-30 8-K (acc 0001104659-26-120680, SACE facilities, already KB-CRU-216); nothing filed since that retires the $216.2M exchangeables. So nothing settles it early; grade on/after 11/17.
