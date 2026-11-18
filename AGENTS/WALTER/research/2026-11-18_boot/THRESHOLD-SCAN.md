# November 18 desktop boot threshold scan (walter-89)

Runtime Claude Code, Opus 5.5 (claude-opus-5-5), desktop DESKTOP-BC6EF81. FRED pulls 2026-11-18T15:13:2xZ (latest observation as posted, not an ALFRED first-published pull); vendor pulls 15:13:33Z intraday (not closes, not settles; futures quotes about 10 minutes behind). Registries read this boot: RED scan view (banner sha256 9da587b5, matches canon, unchanged since 7bcfd11889), REGINALD (06f187503c), CREED (4ed90daf56), HANS (8dfe804142) THRESHOLDS.tsv; all unchanged since the 11/18 01:22Z scan. WALTER graded nothing.

| IDs | Observation / result |
|---|---|
| RED-FT-02 (fired, exit <300 s=3), RED-FT-01, RED-FT-12, REG-T-03 (fired) | FRED HY 334 [Nov 16]; Nov 17 not yet posted at 15:13Z (LIQUID grades the Nov 17 cell after about 10:50 ET). No fire or exit. |
| REG-T-04 (>350 s=3) | 334 [Nov 16], 16 bp under: near-trigger watch unchanged. |
| RED-FT-07 | CCC 1,310 [Nov 16]. No change. |
| RED-FT-06 (fired-banked, exit >=18 s=5) | VIXCLS now posted for Nov 17: 25.46. Closes at or above 18 on WALTER's read: 18.70 [Nov 12], 19.30 [Nov 13], 22.91 [Nov 16], 25.46 [Nov 17] = 4 of 5 (17.49 [Nov 11] broke the prior run). A Nov 18 VIXCLS close at or above 18 would meet the exit on WALTER's read; vendor ^VIX 24.59 intraday at 15:13Z. NEAR-EXIT WATCH; RED grades on VIXCLS. |
| Safety net VIX >30 or +5 | 24.59 intraday vs 25.46: -0.87. Clear. |
| RED-FT-09 | T5YIFR 2.16 [Nov 17]. Not near. |
| REG-T-08 | SOFR 3.92 [Nov 17] less IORB 3.90 = +2 bp. Not near. |
| RED-FT-05, REG-T-05 | ICSA 200,000 [w/e Nov 7]. Next Thu 11/19. |
| REG-T-01/02 | KRE 70.79, WAL 70.97 [Nov 18 intraday]; WAL vendor closes 74.79 [11/13], 73.46 [11/16], 71.47 [11/17]: under 78 inside the existing cycle; KRE about 18% above 60. ZION 63.99 (-0.20%): no gap-down; KRE -0.09%: no >3% drop. |
| RED-FT-03/04, boundaries 1/2/8 | BZF27 92.07 intraday (contract identity UNKNOWN on the vendor path), CLF27 83.26 (Jan 2027). Not settles, not gradeable. |
| Boundary 3 | Cushing 27.356M [w/e Nov 6] carried; WPSR due 10:30 ET today (after this scan). |
| HANS-T-07 L3 exit (5 consecutive named-front closes under 90) | TTFZ26.NYM vendor closes: 90.95 [11/13] reset, 84.75 [11/16], 85.40 [11/17] = 2 of 5 on WALTER's read; 82.07 intraday 11/18. Earlier run 11/06 to 11/11 reached 4 (85.59, 82.50, 84.73, 86.65) before 92.26 [11/12]. Vendor bars, not ICE Endex settles; HANS grades (dark since 11/11). |
| HANS-T-11 | EURUSD 1.10 intraday: far from 1.05. |
| HANS-T-17 | UK core CPI October 2.8% (ONS, released 11/18): watch 3.0 not met. |
| Other HANS daily rows (T-05, T-06, T-08, T-09, T-10, T-13) | Not pulled (no WALTER instrument for Bund, gilt, OAT or storage at this boot). |
| CREED rows | Monthly and quarterly; no new print in window. |

No new registered fire or exit. Not a clean board: FRED HY for Nov 17 unposted at the pull; Cushing pending; HANS bond and storage rows not pulled; Brent identity unresolved. Written 2026-11-18T15:25Z.
