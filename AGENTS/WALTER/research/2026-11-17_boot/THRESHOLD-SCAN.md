# November 17 boot threshold scan (Tuesday)

Runtime Claude Code, Opus 5.5 (claude-opus-5-5), desktop. Vendor pull 2026-11-17T16:45:45Z (11:45 ET, intraday, not closes or settlements); FRED first-published pull and yfinance daily bars 2026-11-17T16:46:25Z. Registries: RED scan view banner sha256 9da587b5... matches canon FALSIFICATION_TRIGGERS.tsv (RED commit 7bcfd11889, 11/17 08:46 ET: FT-06 exit 2 of 5 on [11/13]); REGINALD THRESHOLDS.tsv (236a091d45, 10/11) read whole; CREED THRESHOLDS.tsv diff read since the 11/16 scan's 39bc4f7c8e (4ed90daf56: CREED-T-01b state 11/16, Oct office SS 16.60, NOT FIRED); HANS THRESHOLDS.tsv unchanged since 8dfe804142 (read whole at the 11/16 scan, not re-read whole today); WALTER, CREED and HANS fired logs unchanged since 11/05-11/06. WALTER graded nothing.

| IDs | Observation / result |
|---|---|
| RED-FT-02 (fired, exit <300 s=3), RED-FT-01 (<280), RED-FT-12 (<260), REG-T-03 (fired, exit <=300 x5) | FRED HY OAS 334 [Nov 16] (323 [Nov 13], 320 [Nov 12]). +11 bp, under the 25 bp safety-net widening. No fire or exit. |
| REG-T-04 (>350 s=3) | HY 334 [Nov 16] is 16 bp (4.6%) under 350: NEAR-TRIGGER WATCH (within 5%), not a fire. REGINALD and LIQUID own. |
| RED-FT-07 (firing-banked) | CCC 1,310 [Nov 16]. No change. |
| RED-FT-06 (fired-banked, exit >=18 s=5) | VIXCLS 18.70 [Nov 12], 19.30 [Nov 13], 22.91 [Nov 16]: three consecutive closes at or above 18 on WALTER's read (RED's registry says 2 of 5 at [11/13] and 'Cboe 22.91 [11/16] indicates 3'). RED owns the count. |
| Safety net VIX >30 or +5 intraday | ^VIX daily bar 11/17: open 23.11, high 27.22, low 22.36, last 26.18 vs VIXCLS 22.91 [Nov 16]: high is +4.31, last +3.27. Under +5 and under 30: NEAR WATCH (+5 line = 27.91; the high came within 0.69). |
| RED-FT-05, REG-T-05 | ICSA 200,000 [w/e Nov 7]. Not near. Next print Thu 11/19. |
| REG-T-08 | SOFR 3.93 [Nov 16] less IORB 3.90 = +3 bp. Not near 15. |
| RED-FT-09 | T5YIFR 2.15 [Nov 16] vs >2.55. Not near. |
| REG-T-01/02 | Vendor KRE 70.96 (-1.70%), WAL 71.48 (-2.70%) intraday: WAL under 78 inside the existing fired cycle; exit (>=81.90 x3) not near. KRE not near 60. ZION open 65.39 vs 65.72 close (-0.5%): no gap-down over 5%. KRE not -3%. |
| REG-T-06 | Owner-graded REVIEW 11/16 (card 20261116-004). No new print. |
| RED-FT-03/04, boundaries 1/2/8 | BZF27 93.17 (+0.79%), CLF27 85.16 (+0.82%) vendor intraday, identity not probed; not settlements, not gradeable. |
| Boundary 3 | Cushing 27.356M [w/e Nov 6] carried; next WPSR Wed 11/18. |
| HANS-T-07 and other HANS rows | Vendor TTFZ26 84.44 (-0.36%), identity not probed; HANS grades closes. EURUSD 1.10, USD/JPY 159.23. HANS dailies not re-pulled. |
| CREED | Monthly/quarterly; CREED-T-01b NOT FIRED at 16.60 (CREED 11/16). CREED-T-03 next QBP late November. |
| DGS10 / DGS30 | 5.15 / 5.47 [Nov 13] (FRED, first-published 11/16). |

Market context (not a registered trigger): S&P 500 7,311.80 intraday (-1.41%), low 7,288.34, second session under HENRY's 7,500 put wall (card 20261116-011). NVDA 153.35 (-1.79%) ahead of results after today's close. No new registered fire or exit established. Not a clean board: closes not yet in; HANS daily rows not re-pulled; Brent and TTF contract identity not probed.
