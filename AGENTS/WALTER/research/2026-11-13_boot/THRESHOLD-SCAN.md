# November 13 desktop boot threshold scan (walter-d4)

Runtime Claude Code, Opus 5.5 (claude-opus-5-5), host DESKTOP-BC6EF81. Vendor pull 2026-11-13T15:16:46Z (10:16 ET, intraday, not closes or settlements); FRED pull 15:16:54Z to 15:17:03Z. Registries: RED scan view banner sha256 17b9a52b… matches canon FALSIFICATION_TRIGGERS.tsv (last RED commit ebe839ffe0, 11/12 09:53 ET); REGINALD (10/11), CREED (11/06), HANS (11/11) unchanged since the 11/12 scans; WALTER fired logs unchanged (11/05, 11/06). State cells read truncated (IDs complete). WALTER graded nothing.

| IDs | Observation / result |
|---|---|
| RED-FT-02 (fired, exit <300 s=3), RED-FT-01 (<280), RED-FT-12 (<260), REG-T-03 (fired, exit <=300 x5), REG-T-04 (>350) | FRED HY OAS 320 [Nov 12] (first read this pull), 330 [Nov 11, non-session per RED nonsession.py], 334 [Nov 9]. Tightening; 320 is not above the FT-02 320 entry line and not under either exit. No fire or exit. |
| RED-FT-07 (firing-banked) | CCC 1,314 [Nov 12]. No change of state. |
| RED-FT-06 (fired-banked, exit >=18 s=5), RED-29 | VIXCLS 18.70 [Nov 12], 17.49 [Nov 11]: on WALTER's read the exit run restarts at 1 of 5 from Nov 12; RED owns the count. Vendor ^VIX 19.43 (+3.90%) intraday. No fire. |
| RED-FT-05, REG-T-05 | ICSA 200,000 [w/e Nov 7]; not near 250,000 / 300,000. |
| REG-T-08 | SOFR 3.90 less IORB 3.90 = 0 bp [Nov 12]. Not near 15. |
| RED-FT-09 | T5YIFR 2.17 [Nov 12] vs >2.55. Not near. |
| REG-T-01/02 | Vendor KRE 72.11 (−0.56%), WAL 74.24 (−0.20%) intraday; WAL under 78 inside the existing fired cycle; exit (>=81.90 x3) not near. |
| RED-FT-03/04, boundaries 1/2/8 | BZF27 96.93 (+1.16%, contract identity UNKNOWN on name cut), CLF27 88.30 (+0.70%, Jan 2027): intraday, not settlements, not gradeable. |
| Boundary 3 | Cushing 27.356M [w/e Nov 6] (card 20261112-006); no new WPSR since. |
| HANS-T-07 (L3 exit: 5 closes under €90) | Vendor TTFZ26 90.70 (−1.69%) intraday, identity UNKNOWN on name cut; HANS grades closes. HANS-T-11 EURUSD 1.11 vendor. Other HANS rows not re-pulled (owner values dated 11/10 to 11/11). |
| CREED | Monthly/quarterly rows; no new print since 11/06 state. |

Safety net: VIX under 30, no +5 intraday; HY 320 vs 330 prior, tightening, no 25 bp widening. No new registered fire or exit established. Not a clean board: HANS daily rows not re-pulled; vendor rows intraday.
