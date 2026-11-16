# November 16 boot threshold scan (walter-5a, Monday)

Runtime Claude Code, Opus 5.5 (claude-opus-5-5), desktop. FRED pull 2026-11-16T18:27:56Z via fetch.py fred_fetch_vintage (first-published basis). Vendor pull 18:28:15Z (13:28 ET, intraday, not closes or settlements); day high/low from yfinance daily bars at 18:2xZ. Registries: RED scan view banner sha256 17b9a52b... matches canon FALSIFICATION_TRIGGERS.tsv (last RED registry commit ebe839ffe0, 11/12); REGINALD THRESHOLDS.tsv (236a091d45, 10/11), CREED THRESHOLDS.tsv (39bc4f7c8e, 11/06), HANS THRESHOLDS.tsv (8dfe804142, 11/11) read whole; WALTER fired logs unchanged; CREED and HANS fired logs read at their tails (unchanged since 11/05 and 11/06). WALTER graded nothing.

| IDs | Observation / result |
|---|---|
| RED-FT-02 (fired, exit <300 s=3), RED-FT-01 (<280), RED-FT-12 (<260), REG-T-03 (fired, exit <=300 x5), REG-T-04 (>350) | FRED HY OAS 323 [Nov 13] (320 [Nov 12]). No fire or exit. REG-T-04 is 27 bp (7.7%) away, not within 5%. |
| RED-FT-07 (firing-banked) | CCC 1,316 [Nov 13]. No change. |
| RED-FT-06 (fired-banked, exit >=18 s=5) | VIXCLS 17.49 [Nov 11], 18.70 [Nov 12], 19.30 [Nov 13]: two consecutive closes at or above 18 on WALTER's read (2 of 5); RED owns the count. Vendor ^VIX 22.25 intraday Nov 16, a second witness only. |
| RED-FT-05, REG-T-05 | ICSA 200,000 [w/e Nov 7]. Not near. |
| REG-T-08 | SOFR 3.90 [Nov 13] less IORB 3.90 = 0 bp. Not near 15. |
| RED-FT-09 | T5YIFR 2.18 [Nov 13] vs >2.55. Not near. |
| REG-T-01/02 | Vendor KRE 72.02 (-0.99%), WAL 73.32 (-1.96%) intraday: WAL under 78 inside the existing fired cycle; exit (>=81.90 x3) not near. KRE not near 60. |
| REG-T-06 | Owner-graded REVIEW on Nov 16 (REGINALD; FHLB Q3 CFR $798.4B, third quarter above $700B). Routed SIG-W-20261116-004. |
| RED-FT-03/04, boundaries 1/2/8 | BZF27 92.79 (-3.18%, identity UNKNOWN on name cut); CLF27 84.67 (vendor change withheld, Jan 2027). Vendor intraday, not settlements, not gradeable. |
| Boundary 3 | Cushing 27.356M [w/e Nov 6]; next WPSR Wed Nov 18. |
| HANS-T-07 | Vendor TTFZ26 84.04 (-7.59%), last trade 98 minutes old at fetch (feed may be frozen), identity UNKNOWN; under the L3 exit line; HANS grades closes. EURUSD 1.10. Other HANS rows not re-pulled. |
| CREED | Monthly/quarterly; no new print since the 11/05 to 11/06 states. CREED-T-03 next QBP late November. |

Safety net: VIX 22.25 intraday (high 22.32) vs Friday close 19.30 = +3.0, under +5 and under 30; HY 323, +3 bp, no 25 bp widening; KRE -0.99%, not -3%; no WAL/ZION gap-down over 5%. S&P 500 7,425.43 (-1.80%) intraday, under HENRY's published 7,500 put wall [11/12] and under Friday's 7,499.40 low: routed on SIG-W-20261116-002, not a registered trigger. No new registered fire or exit established. Not a clean board: closes not yet in; HANS daily rows not re-pulled; TTF vendor bar stale.
