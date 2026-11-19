# November 19 boot threshold scan (walter-fc, laptop; charter 6b/6c)

Registries loaded at 6b: RED FALSIFICATION_TRIGGERS_SCAN.tsv (banner sha f4fbc650d115 matches canon), REGINALD THRESHOLDS.tsv (REG-T-01 to 08), CREED THRESHOLDS.tsv (last real data refresh 2026-11-06; monthly and qualitative rows, nothing gradable today), HANS THRESHOLDS.tsv (17 rows; T-12 unfed, no clean-board credit). FRED pulled 2026-11-19T14:23:22Z (first-published values as posted); vendor pulled 14:23:29Z, before the cash open: equity rows are 11/18 closes marked stale by the tool; ^VIX 22.54 is an early-session index print, not a close. WALTER graded nothing.

| IDs | Observation / result |
|---|---|
| RED-FT-06 (fired-banked, exit >=18 s=5) | VIXCLS [11/18] NOT YET POSTED at 14:23Z (latest 25.46 [11/17]). On WALTER's read the exit is 4 of 5 on VIXCLS plus vendor close 24.56 [11/18] (card 20261118-015). RED grades when VIXCLS posts. |
| RED-FT-02, REG-T-03 (>320 x3) | HY OAS 343 [11/17], latest posted; 11/18 not yet posted. Fired states unchanged (LIQUID >320 x3 MET, card 20261118-010). |
| REG-T-04 (>350 x3) | 343 [11/17], 7 bp under: near-trigger watch. |
| RED-FT-07 (CCC >930) | CCC 1,329 [11/17]: FIRING-BANKED state, RED owns. |
| RED-FT-05 (claims >250K) / REG-T-05 (>300K) | ICSA 203,000 [w/e Nov 14] (card 001): not near. |
| RED-FT-09 (5y5y >2.55 s=5) | T5YIFR 2.15 [11/18]: not near. |
| REG-T-08 (SOFR-IORB >15) | SOFR 3.90 [11/18] less IORB 3.90 = 0 bp. Clear. |
| REG-T-01/02 | KRE 70.52, WAL 70.83 (under 78, existing cycle), ZION 63.69 [11/18 closes]. |
| Safety net VIX >30 or +5 | ^VIX 22.54 early 11/19 vs 24.56 close: clear. |
| HANS-T-07 L3 exit | TTFZ26 vendor 84.45, last trade 54 minutes old at fetch (vendor flags frozen feed), identity UNKNOWN: not gradeable today. |
| RED-FT-03/04, boundaries 1/2/8 | No settle read this boot; not gradeable. |
| Boundary 3 | Cushing 26.147M [w/e Nov 13] (card 20261118-008); next WPSR Wed 11/25. Not met. |

No new registered fire or exit at boot. Written 2026-11-19T14:30:44Z (date command).
