# BOJ October 29–30 decision — VIOLET carry-to-vol grade

**Graded:** 2026-10-30 12:5x ET (VIOLET, PROME prome-c5 WQ-184 due-row wake, Claude Code, Opus 5.5). **Ledger row:** `workbook/CATALYSTS.tsv` 2026-10-30 BOJ (moved to `catalysts-fired.tsv` here). **KB:** KB-VIO-360.
**Scope:** VIOLET owns only the carry-to-vol transmission read. SAM owns BOJ policy substance; nothing below is policy analysis.

## 1. Fact of the decision (BOJ primary)

| Item | Value | Source |
|---|---|---|
| Policy rate guideline | **Held at around 1.25%** (uncollateralized overnight call rate) | BOJ "Statement on Monetary Policy", 2026-10-30, `https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k261030a.pdf` (HTTP 200, own fetch 10/30 12:53 ET, sha256 `f62859324bd87cc4…`) |
| Vote | **8–1**; TAKATA Hajime against, proposing a faster move toward neutral | same, [Note] |
| ETF sales pace | ~JPY 330B/yr → **~JPY 860B/yr** (book value; ~0.1% of trading value), effective January 2027; unanimous | same, item 2 |
| Announcement timing | Tokyo 10/30 = evening of 10/29 ET; exact hour not stated in the PDF (SAM's calendar: ~noon JST ≈ 23:00 ET) | SAM STATUS line 68 (SAM's estimate) |

SAM's pre-meeting market pricing (Totan, 10/29): October hike 2%. A hold was the priced outcome. SAM grades SAM-42 on this PDF.

## 2. Carry-to-vol read (VIOLET canary)

| Leg | Before (10/29) | After (10/30) | Band / rule | Read |
|---|---:|---:|---|---|
| USDJPY | 157.96 (jpy_vol.py pull 14:52 ET 10/29) | **157.42** (jpy_vol.py 12:53 ET 10/30, INTRADAY); fetch.py 157.47 at 12:55 ET | — | −0.34%, toward yen strength |
| USDJPY range, 10/29 20:00 → 10/30 04:00 ET (decision window, hourly JPY=X) | — | high 157.898 / low 157.110 = **0.79 yen** | — | small, toward yen strength |
| USDJPY range, 10/29 16:00 → 10/30 12:59 ET | — | high 157.983 / low 156.957 = **1.03 yen** | — | SAM owns the fast-move bar |
| RV10 / RV20 | 6.93% / 5.13%, p33.8 | **7.02% / 5.16%, p34.5** | WATCH p90 **14.15%** / FIRE p95 **15.21%** (3y, re-derived this run) | **CALM** |
| FXY near-ATM call IV (Dec 18, OI ≥100) | 11.5% | **11.3%** (RTH chain, usable) | — | flat |
| IV/RV10 | 1.66 | **1.61** | >2× event priced · →1× risk passed · RV>IV unwind underway | No event premium was priced into the decision, and none released. Not the unwind signature (RV < IV). |

**Grade: CALM — no carry-to-vol transmission from the BOJ decision.** RV10 sits 7.13 points under the WATCH line. The yen moved 0.34% stronger, within normal range, and FX option implied vol did not reprice. The JPY carry vector stays at 1 (⚪).

## 3. What this grade does NOT cover

- **Equity vol rose sharply today, intraday, and it is not carry-led on this instrument.** At 12:52–12:55 ET 10/30 (TICK, not a close): VIX 19.96–20.00 (+16.05% vs the 17.20 official 10/29 close), VVIX 111.81, VIX3M/VIX 1.049, COR1M 14.40, SPX −1.58%, QQQ −3.52% (fetch.py; HENRY owns equity). Yen carry did not move with it. The surface is graded on the official 10/30 close by the next session, not here.
- BOJ policy content, the ETF-sales change and any rate path: SAM.
- MOF intervention data (due ~10/30): SAM.

## 4. Sources / receipts

- BOJ statement: URL above; text extracted with pdfminer, sections 1, 2 and the [Note] read.
- `workbook/JPY_VOL.tsv` rows 2026-10-29 and 2026-10-30 (10/30 row annotated INTRADAY).
- Hourly JPY=X bars: yfinance `history(period="5d", interval="60m")`, pulled 12:54 ET 10/30.
- No threshold, score, gate letter or trade moved. $0.
