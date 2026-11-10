# BOND pre-auction read, 2026-11-10: CPI and Waller on the curve

**Written 2026-11-10 11:4x ET** (desktop, Claude Code, `claude-opus-5-5`; launched by PROME prome-07 on Will's 11:38 ET word). $0. No score, band, gate, threshold or card moved.

## Answer

**A front-led bear flattener in two steps, then the long end caught up after the cash open.** Governor Waller's London speech (04:00 ET) hit the 2-year hardest; the CPI print (08:30 ET, core +0.3%, unrounded +0.296%, HENRY HEN-57) hit every tenor about equally; and since 08:40 ET the long bond and ultra have taken more than half their day's move with no new data. The 10-year auction (13:00 ET) prices into a curve about 13bp cheaper on the day and back at its 10/28 level.

## Levels (vendor intraday, NOT closes; CBOE yield indices, not Treasury par)

| Tenor | 11/9 vendor close | 11/10 ~11:25 ET | Day | Basis |
|---|---:|---:|---:|---|
| 2Y | Treasury par 4.56 [11/9] | not observed as a yield | ZT −0.35% in price, about +19bp at an ASSUMED 1.9 duration | [EST] |
| 5Y (^FVX) | 4.659 | 4.828 | +16.9bp | [EST vendor] |
| 10Y (^TNX) | 4.864 | 4.998 | +13.4bp | [EST vendor] |
| 30Y (^TYX) | 5.256 | 5.359 | +10.3bp | [EST vendor] |
| 5s30s | 59.7bp | 53.1bp | −6.6bp | [EST subtraction, same basis] |

Treasury par 11/9 for reference: 2Y 4.56, 10Y 4.88, 30Y 5.26 [CONF PRIMARY]. CBOE closes sit 1–2bp under par (on-the-run vs fitted par); compare within a basis only. On the H.15 basis the last close at or above 4.99 on the 10Y and 5.36 on the 30Y was **10/28 (FOMC day)**; 2026 highs 10Y 5.31 [10/5], 30Y 5.67 [10/7]. Real yields are not observed intraday.

## Timing: share of each futures contract's price move, prior close to 11:10 ET (vendor 5-minute bars, last trade, not settlement)

| Window | ZT 2Y | ZF 5Y | ZN 10Y | ZB bond | UB ultra |
|---|---:|---:|---:|---:|---:|
| Prior close → 03:45 ET | 0% | −3% | −5% | −4% | −4% |
| **03:45 → 04:05 (Waller, 04:00 ET)** | **29%** | 24% | 20% | 9% | 8% |
| 04:05 → 08:25 | 8% | 12% | 15% | 11% | 10% |
| **08:25 → 08:40 (CPI, 08:30 ET)** | 30% | 33% | 32% | 30% | 27% |
| **08:40 → 11:10 (no scheduled data)** | 33% | 35% | 38% | **55%** | **60%** |
| Total price change | −0.363 (−0.35%) | −0.695 (−0.66%) | −0.938 (−0.88%) | −1.469 (−1.35%) | −1.625 (−1.48%) |

Duration-free: each cell is a share of that contract's own move, so no duration assumption enters. Negative pre-03:45 cells = a small overnight rally.

## What it means for BOND

1. **Waller was a front-end policy shock; CPI was a level shock; the afternoon long-end sale is unexplained.** Waller's text named a December 25bp hike and a 50bp case if core ran about 0.3 (federalreserve.gov `waller20261110a.htm`, read by HENRY at the primary). Core printed +0.3. December is now fully priced plus about 13% of a further 25bp [HENRY 11:10 ET, `f3279ab9ac`, vendor last, not settlement]; boot_recompute at 11:40 ET reads the same +28.2bp in-month. **Beyond December:** strip peak 4.640 (Sep-2027) = +76bp vs EFFR 3.88, against +46.5bp on 11/6 — about +48bp priced past December vs +27.5 on 11/6. HENRY owns the Fed path.
2. **The long end is moving after the data, not on it.** 55–60% of the bond and ultra move came after 08:40. Candidates, none tested: pre-auction concession into today's $42B 10Y and Thursday's $25B 30Y; positioning unwind after a third straight 0.3 core; duration supply hedging. **Cause not established.** The 10Y auction is the first test of whether that concession was enough.
3. **11/6 read revisited.** On 11/6 BOND recorded that hikes leaving the 2027 path did not lower real long rates. Today hikes came back and nominal long rates rose, but less than the front: 5s30s −6.6bp. Real 10Y for 11/10 publishes tonight; no real-yield claim until then.
4. **Auction set-up (frozen 11/2, `registry/auction_bars/2026-11-10_91282CRX1.json`):** 10Y `91282CRX1` $42B new issue. I′ indirect < 65.05 (strict); OLD indirect < 63.95 AND dealer > 13.38; cover marker BTC < 2.39. Trailing-12 indirect median 72.34, mean 72.59, min 63.95; dealer median 9.14, max 13.38; BTC median 2.54. The 3Y on 11/9 fired I′ (55.48 vs 57.44) with dealers at 9.48: the shortfall went to directs. BND-33 is already TRUE, so this grade moves the clean-nominal counter (now 0) and the record only.

## Sources

CBOE ^FVX/^TNX/^TYX and CBOT ZT/ZF/ZN/ZB/UB via yfinance, pulled 11:41 ET 11/10 (vendor, intraday, not settlement); FRED DGS10/DGS30/DGS5 through 11/6; Treasury par 11/9 (KB-BND-563); `monitors/boot_recompute.py` 11:40 ET (fed funds strip, vendor bars); HENRY `research/2026-11-10_cpi-grade/CPI_GRADE.md` and `OVERNIGHT_HIKE_REPRICING.md` (commit f3279ab9ac).

## Grade, 13:04 ET (added after the print; the read above was written before it and is unchanged)

Registered grade on the 11/2 frozen bars, full output `grade_91282CRX1.txt`:

| Leg | Print | Bar | Margin | Result |
|---|---:|---:|---:|---|
| I′ indirect (P15) | 61.23% | 65.05 | −3.82pp | **FIRE** (🟠 marker) |
| Indirect vs 12-auction min | 61.23% | 63.95 | −2.72pp | below |
| Dealer vs 12-auction max | 9.77% | 13.38 | −3.61pp | not above (OLD not met) |
| BTC vs 12-auction min | 2.46 | 2.39 | +0.07 | no cover marker |

Direct 29.00%; high yield 5.020%; % of competitive accepted $41.757B. Lowest 10Y nominal indirect in BOND's corpus since 2023-10-11 (60.3, a reopening). **Second refunding I′ fire in two sessions, both with the shortfall taken by direct bidders, not dealers: a warning light, not a break.** Counter stays 0; auction health held 3; BND-33 already TRUE. KB-BND-566.
