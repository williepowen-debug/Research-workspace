# November 23 return threshold scan (walter-7f, laptop)

Written 2026-11-23T17:25:21Z (date command). RED scan banner sha 7358ccf1 matches canon. FRED pulled 17:22Z; vendor intraday reads 17:15Z to 17:22Z are not closes.

| IDs | Result |
|---|---|
| Safety net VIX | 11/20 both legs fired (001 of 11/20 and 11/21). 11/23 vendor 27.93, under 30 intraday; a later up-cross is a re-cross |
| HY safety net | +24 bp [11/20], over 25 NOT met |
| REG-T-04 | 376 [11/20], 2 of 3; day 3 is the 11/23 observation |
| RED-FT-02, REG-T-03, RED-FT-07 | fired states unchanged; HY 376, CCC 1,402 |
| RED-FT-06 | un-fired, not re-armed; VIXCLS 35.89 |
| RED-FT-09 | T5YIFR 2.12 [11/20]: not near |
| RED-FT-10 exit (<140 x4) | SKEW 138.84 [11/20], 1 of 4; vendor mirror, VIOLET level agrees; RED grades |
| REG-T-08 | SOFR 3.92 less IORB 3.90 = +2 bp [11/20] |
| RED-FT-05, REG-T-05 | ICSA 203,000 [w/e 11/14]; next 11/25 |
| REG-T-01, KRE -3% | KRE 69.37 (+1.54%) intraday: not near |
| REG-T-02 | WAL 69.86 intraday, existing cycle |
| HANS-T-07 L3 exit | 5 of 5 at 11/20 on TTFZ26 vendor closes: SIG-W-20261123-005, HANS grades |
| HANS-T-11 | EURUSD 1.0892 intraday: not near 1.05 |
| RED-FT-03, -04 | BZF27 89.93 vendor intraday, provisional: neither line near; no settlement read |
| NOT READ, not cleared | HANS-T-05, 06, 08, 09, 10, 13; RED-FT-11; monthly and qualitative CREED rows; Cushing (no new WPSR) |

## Continuation, 2026-11-23T20:43:27Z (date command), after the connectivity gap

Resumption refresh 15:40 ET: VIX 26.76 (high since about 14:30 ET 27.61), S&P 7,256.94 (low 7,223.37), vendor 5-minute bars, not closes. No upward crossing.

| IDs | Result |
|---|---|
| HANS-T-05 | Bund 3.27 [TE page dated 11/23, close or intraday not labelled]; ECB-basis not read; WATCH over 3.00 stays open, orange 3.75 is 48 bp away |
| HANS-T-06, T-13 | Gilt 10Y 5.20, 30Y 5.66 [TE 11/23]: not met (30 bp and 34 bp under) |
| HANS-T-09 | BTP 4.35, spread about 107 bp [TE 11/23]: not met, both legs |
| HANS-T-10 | ideal-investisseur rows 11/20 4.87 / 155.4 bp, 11/23 4.83 / 153.1 bp: both fire legs met, stays OPEN, exit 0 of 5 (read via the .fr host; HANS named the .com path, whose certificate mismatched) |
| HANS-T-08 | HANS's own 11/23 row, gap -17.66 pp [11/21], FIRED-OPEN: not re-read by WALTER |
| RED-FT-11 | FRED DGS30 ends 11/19 at this read: 5-session change -3 bp, no precondition. Treasury par 11/20: 30Y 5.31 from 5.47 [11/13] = -16 bp, at the -10.2 line if FRED posts the same. Provisional legs on Treasury par: 30Y-5Y +11 bp, 2Y -25 bp, T10YIE -9 bp [FRED, 2.24 to 2.15]: FUNDAMENTAL by RED's letter, no weight. Await FRED |
| CREED-T-08a | price-only 63-session VNQ less SPY +0.33 pp [11/23 intraday]; the row is total return; fired state stands, no exit registered |
| CREED monthly rows | CREED STATUS 11/16: October graded; next Trepp November about 12/1 to 12/3; FDIC Q3 QBP about 11/25 |
| Boot-context reads (FILTER_SPEC) | FORGE header and first rows, RED CATALYSTS through 12/2, trailing 48 h kill and route logs read; other STATUS heads not read |
