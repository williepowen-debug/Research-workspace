# 11/11 pre-open: why futures are up — HENRY read (PROME prome-2b ask 09:06 ET)

Runtime: Claude Code, Opus 5.5 (`claude-opus-5-5`), launched from AGENTS/HENRY. Clock from `date`. Every quote is a vendor or Cboe delayed quote, not a settle.

## 1. Gamma map, pre-open (gamma_flip.py --both --publish, 09:06–09:09 ET; Cboe chain asof 11/11, open interest = end of 11/10 trading)

| Chain | Spot used | Flip 14d / 35d | Net GEX per 1% 14d / 35d | Put wall | Call wall | Spot vs flip |
|---|---:|---:|---:|---|---|---|
| SPX | ~7,593 implied (ESZ26 7,617 at ~08:57 ET less the 11/10 close basis of ~24 pts: ES prior 7,617/1.0096 = 7,544.6 vs SPX close 7,520.93) | ~7,622 / ~7,625 | −$11.0B / −$14.6B (−$43.8B at the 11/10 close spot) | **7,500** clean both (+16% / +15%) | **7,700** clean both (+30%) | ~30 pts (0.4%) UNDER → NEGATIVE |
| QQQ | 687.31 Cboe premarket | ~690 / ~691 | −$0.5B / −$0.6B | **680** (35d clean +18%; 14d near-tie band 680–685) | **700** clean both | ~3 pts UNDER → NEGATIVE |
| NDX | ~28,270 implied (NQZ26 +1.91% on the 11/10 close 27,740.79) | ~27,887 / ~28,026 | +$0.8B / +$0.6B | **28,000** clean both (now UNDER spot) | **29,675** clean both | ~240–380 pts ABOVE → POSITIVE |

**What it means.** The S&P opens in negative gamma, but only just: the dealer short-gamma book at the implied open is about a quarter of Tuesday's close reading, and the flip sits 0.4% overhead. Under ~7,625 dealer hedging adds to the move in whichever direction it goes, so the gap can carry toward the flip. Above it hedging starts to damp the move, and 7,700 is the next concentration. A fade back under 7,500 returns the index to the deeper negative zone it closed in Tuesday. Nasdaq is split: NDX is above its flip (damped) and QQQ is just under (amplified). The two chains straddle the same boundary, so read Nasdaq as AT the flip, not on either side of it.

**Limits.** Free-tier proxy: sign and flip are robust, dollar sizes depend on assumptions and walls are the fragile part. Open interest is end of 11/10, so today's 0DTE and opening flows are not in it. Implied spot carries basis error of a few points. Cboe IV reads zero for about 15 minutes after 09:30 ET, so the opening re-run waits until after ~09:47.

## 2. Drivers, own sources (Cboe delayed premarket quotes ~09:08 ET; vendor futures ~08:57 ET)

| Group | Move |
|---|---|
| Index futures | ES +0.96%, NQ +1.91%, YM +0.30%, RTY +0.92% |
| Cap vs equal weight | SPY +0.96% vs RSP +0.43% (cap weight leads by about 0.5pp); DIA +0.28%; IWM +0.90% |
| Chips / AI infrastructure | SMH +4.52%, MU +6.88%, AMD +5.19%, ORCL +4.82%, TSM +4.28%, AVGO +3.97%, NVDA +3.42% (from 168.89, which was −5.47% on 11/10), CRWV +14.78% |
| Other mega caps | META +1.58%, TSLA +1.40%, GOOGL +1.14%, AMZN +0.75%, MSFT +0.63%, AAPL −0.32% |
| Sectors | XLI +1.02%, XLE +1.21% (Brent ~92.5, +1.2%), XLF −0.21%, XLU −0.09%, XLV −0.77%; KRE +0.22%, HYG +0.28% |
| Vol | VIX 18.33 (−5.8%), VIX9D 18.54, VIX3M 20.64 (prior), VVIX 96.6 |

**Read:** chip- and AI-infrastructure-led, with a real but much smaller broad bid (cyclicals and small caps up about 1%) and defensives down. The press attribution (CoreWeave's results, a Nvidia rebound) fits the cross-section: CRWV leads and the AI-infrastructure complex (ORCL, MU, AMD, TSM) moves more than NVDA itself. CoreWeave Q3 beat on the headline (EPS −$1.27 vs −$1.55, revenue $3.66B vs $3.54B, WALTER 011, relay, release not read here) and held its 2026 capex guide at $37–39B with the low end raised (VULCAN via WALTER 013). The TrendForce "Nvidia may slow chip orders" report (WALTER 20261111-003, unquantified) is not being priced this morning (TSM +4.3%).

**Rates did not help.** Cash Treasuries are closed (Veterans Day; no Treasury par print for 11/11). Futures, vendor last ~08:58 ET against the vendor 11/10 daily bar (not CME settlement): ZT 101.957 vs 102.023 (about +3bp in 2Y yield), ZN 106.125 vs 106.250 (about +2bp), ZB 107.063 vs 107.219 (about +1bp). Small bear flattening continues. **December hike pricing edged UP:** ZQZ26 95.915 (08:51 ET) vs 95.920 at the 16:01 ET 11/10 last trade = about +28.9bp priced (Dec average 4.085%, days 1–9 at EFFR 3.88, post-meeting ≈4.169%), +0.7bp. ZQF27 95.820 (4.18%), ZQH27 95.600 (4.40%, +2bp). USD/JPY 159.56 (+0.54%, SAM's velocity line not fired). So this is an earnings/AI-sentiment rebound into a slightly MORE hawkish rate path, not a relief rally on rates.

## 3. Rows touched (graded on their letters)

| Row | Letter | State 11/11 pre-open |
|---|---|---|
| HEN-57 | Oct core CPI 0.4+ = FIRED | RESOLVED 11/10 (NOT FIRED, core +0.3). Untouched |
| HEN-60 (0.50) | an official SPX close below its 200-session average, 11/9–11/30 | OPEN, NOT FIRED. Closes only; 200-day 7,331.08 (11/10 basis); implied open ~3.6% above |
| HEN-61 (0.28) | an official close above 7,818.93 by 12/31 | OPEN, NOT FIRED. Implied open ~2.9% under |
| HEN-63 (0.70) | December FOMC upper bound above 4.00% | OPEN. Not re-marked (no re-mark clause). Market ~+28.9bp = a 25bp hike fully priced plus ~16% of a second, so the gap above my 0.70 widened slightly |
| HEN-58 | PPI 11/13 | OPEN, untouched |
| CYPHER ESCALATION_WATCH row 9, collapse leg (WQ-635 A; my price read, CYPHER's row) | PANW ≤ $289.24 AND ≥10.0 points behind HACK, 2 consecutive adjusted closes, graded at the 11/18 close | NOT BREACHED on the 11/10 close: PANW 326.36 (−4.09% from 340.28), HACK 115.29 (−2.61% from 118.38), PANW 1.48 points behind (yfinance adjusted). Bank leg unsized |
| RED-FT-06 / RED-29 (RED's rows, not mine) | VIXCLS ≥ 18 | VIX 18.33 pre-open; RED grades 11/12 |
