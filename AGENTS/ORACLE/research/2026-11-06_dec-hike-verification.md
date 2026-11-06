# December FOMC hike odds: verification after October payrolls

**Written:** 2026-11-06 15:3x ET, ORACLE, desktop `DESKTOP-BC6EF81`, Kalshi signed lane. **Task:** PROME assignment, Will's word 2026-11-06 15:24 ET. No trade implied. KB-ORC-125, KB-ORC-126. All data free and public.

## Answer

| Source | Figure | Time | Depth |
|---|---|---|---|
| Polymarket "increase 25 bps after December meeting" | **77.5** (book 77/78) | 2026-11-06T20:26Z, 15:26 ET | vol $5.0M, liq $312.4K |
| Polymarket, same market, gate read | 77.5 | 15:15Z, 10:15 ET | liq $322.7K, QUALIFIED |
| Kalshi `KXFED-26DEC-T4.00` | **78.0** last (book 77/78) | 20:26Z | OI 92.5K, vol 253.6K |
| Kalshi two or more (`T4.25`) | 3.0 last (book 1/2) | 20:26Z | OI 73.9K |
| CME FedWatch via CNBC | 76.8 | article 08:31 ET, later updated; figure time unknown | secondary |

**"78 from 70" holds as a level on my sources.** Polymarket was 69.5 at 08:25 ET and 77.5 at 08:35 ET. Kalshi was 72/73 at 08:27 ET and 78/79 at 08:33 ET. ⚠️ **The Reuters sentence itself is not verified.** The Reuters story relayed at cp24.com (published 09:24 ET, updated 11:53 ET) has no hike-odds sentence, and I found no other copy. WALTER card SIG-W-20261106-017 prints it; HENRY's note calls it FedWatch. I did not confirm that basis.

## Same units (KB-ORC-100 rule: expected bp at a matched time)

| Market | Time | Inputs | Expected move |
|---|---|---|---|
| Polymarket | 20:26Z | −50+ 0.45, −25 0.65, hold 20.5, +25 77.5, +50+ 0.55; sum 99.65 | **+19.3bp** normalised |
| Kalshi | 20:26Z | book mids `T4.00` 77.5, `T4.25` 1.5, `T3.75` 98.5, `T3.50` 98.5 | **+19.0bp**; tails are at the tick floor |
| ZQZ26 | 15:18 ET last | 95.985, 22 of 31 December days after the meeting | **+19.0bp** = 76 |
| ZQF27 | 15:18 ET last | 95.925 | **+19.5bp** = 78 |

EFFR 3.88 [11/05, NY Fed API]. ⚠️ Futures are Yahoo last trades, not settlement. One tick (0.005) is 2 to 3 points of probability. The percent assumes hold or +25 only. ZQF27 carries any January meeting days; that date is unchecked. HENRY owns this method (`AGENTS/HENRY/research/2026-09-24_fedwatch-method-october-odds.md`); I ran it only to match units.

**So what:** no dislocation. Three separately traded markets price about the same 19bp. Nothing goes to TERRY on this read.

## The 11/05 fall: what "17 points" means

| Basis | From | To | Change |
|---|---|---|---|
| Polymarket, 11/04 read to 11/05 evening | 80.5 (brief spike) | 63.5 (23:11Z) | −17.0 |
| Polymarket, level held before the move | 77.5 (11/04 17Z to 11/05 09:30 ET) | 63.5 | **−14.0** |
| Kalshi, hour closes | 82.0 (to 09:00 ET) | 65.0 (to 11:00 ET, 44.7K contracts) | −17.0 |
| Futures ZQZ26, same units | +20.4bp, 82 (08:30 ET) | +16.2bp, 65 (15:55 ET) | −17 |

Polymarket path, 10-minute CLOB, ET: 77.5 (09:30), 76.5 (09:40), 73.5 (10:20), 71.5 (10:40), **64.5 (10:50)**, 70.5 (11:30), 66.0 (11:50), 63.5 (17:00).

Sharpest ten minutes, 10:40 to 10:50 ET (Yahoo 5-minute last trades):

| Series | 10:40 | 10:50 |
|---|---|---|
| Polymarket hike | 71.5 | 64.5 |
| SPY | 744.96 | 739.38 |
| QQQ | 657.30 | 650.99 |
| ZQF27 | 95.935 | 95.960 |
| 2-year futures | 102.348 | 102.418 |

**Cause remains NOT established.** What changed: this was not a venue artifact, because five markets moved together. Stocks fell from the 09:30 open; the odds started down by 09:40. Ten-minute data cannot say which led. Two named candidates fail on direction or evidence: the Hammack headline (15:41Z, 10:41 ET, "restrictive rates needed") sits inside the sharpest stretch but reads hawkish, and the Barkin headline (14:29Z, 09:29 ET) also reads hawkish. Both bodies are unread (SIG-W-20261105-022). Three web searches found no report of the day's driver. A risk-off move fits the timing. Timing is not cause.

## The 11/06 rebound: about 6 of 14 points came before the print

| Time ET | Polymarket | Kalshi book | ZQZ26 implied |
|---|---|---|---|
| 11/05 17:00 | 63.5 | 65/66 (19:00) | 65 (15:55) |
| 11/06 05:00 | 69.5 | 65/66 (07:00) | 68 (07:15) |
| 08:25 | 69.5 | 72/73 | 73 (08:15 bar) |
| 08:35 | 77.5 | 77/78 | 76 (08:45 bar) |
| 09:00 | 78.5 | 79/80 | 76 |
| 15:26 | 77.5 | 77/78 | 76 (15:18) |

Polymarket: 63.5 to 69.5 before the print (+6.0), 69.5 to 77.5 after it (+8.0). The print was +165,000 against about +65,000 consensus, unemployment 4.1% (SIG-W-20261106-001, -017). Why the odds rose overnight is not established.

## Sources

Polymarket Gamma and CLOB `prices-history` (fidelity 5, 10, 60); Kalshi market, event and candlesticks (signed; `end_period_ts` is period end); Yahoo chart API; NY Fed `markets.newyorkfed.org`; CNBC https://www.cnbc.com/2026/11/06/jobs-report-october-2026.html and Reuters via https://www.cp24.com/news/money/2026/11/06/nasdaq-eyes-higher-open-as-chips-pare-losses-rate-hike-fears-linger/ (both read by a web-fetch helper). cmegroup.com not touched. FRED CSV returned empty, so NY Fed supplied EFFR.
