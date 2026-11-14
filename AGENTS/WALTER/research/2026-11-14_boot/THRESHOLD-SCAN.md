# November 14 boot threshold scan (walter-72, Saturday)

Runtime Claude Code, Opus 5.5 (claude-opus-5-5). Vendor pull 2026-11-14T16:08:14Z (Saturday; rows are Friday Nov 13 closes per vendor as-of, flagged stale by the tool because markets are closed; not settlements). FRED pull 16:08:23Z to 16:08:27Z via fetch.py API (5-minute cache TTL, so these are fresh reads). Registries: RED scan view banner sha256 17b9a52b... matches canon FALSIFICATION_TRIGGERS.tsv (last RED registry commit ebe839ffe0, 11/12); REGINALD, CREED, HANS rows read; WALTER fired logs unchanged. WALTER graded nothing. File written 2026-11-14T16:21:31Z.

| IDs | Observation / result |
|---|---|
| RED-FT-02 (fired, exit <300 s=3), RED-FT-01 (<280), RED-FT-12 (<260), REG-T-03 (fired, exit <=300 x5), REG-T-04 (>350) | FRED HY OAS 320 [Nov 12] latest; Nov 13 bar not yet published at pull. No fire or exit. REG-T-04 8.6% away (not within 5%). |
| RED-FT-07 (firing-banked) | CCC 1,314 [Nov 12]. No change. |
| RED-FT-06 (fired-banked, exit >=18 s=5) | VIXCLS 18.70 [Nov 12]; Nov 13 not yet published. Vendor ^VIX Friday close 19.30 (+3.21%), a second witness only. RED owns the exit count. |
| RED-FT-05, REG-T-05 | ICSA 200,000 [w/e Nov 7]. Not near. |
| REG-T-08 | SOFR 3.90 [Nov 12] less IORB 3.90 = 0 bp. Not near 15. |
| RED-FT-09 | T5YIFR 2.18 [Nov 13] vs >2.55. Not near. |
| REG-T-01/02 | Vendor Friday close KRE 72.74 (+0.30%), WAL 74.79 (+0.54%): WAL under 78 inside the existing fired cycle; exit (>=81.90 x3) not near. |
| RED-FT-03/04, boundaries 1/2/8 | BZF27 95.84 (+0.02%, identity UNKNOWN on name cut), CLF27 87.29 (−0.46%, Jan 2027): vendor, not settlements, not gradeable. |
| Boundary 3 | Cushing 27.356M [w/e Nov 6] (card 20261112-006); next WPSR Wed Nov 18 (BRENT, modeled). |
| HANS-T-07 | Vendor TTFZ26 90.95 (−1.42%), identity UNKNOWN; HANS grades closes. EURUSD 1.11. Other HANS rows not re-pulled. |
| CREED | Monthly/quarterly; no new print since the 11/05 to 11/06 states. |

Safety net: VIX under 30, no +5 move; HY 320 flat, no 25 bp widening. S&P 500 Friday close 7,561.67 (−0.40%), matching HENRY's close read. No new registered fire or exit established. Not a clean board: Nov 13 FRED bars unposted; HANS daily rows not re-pulled.
