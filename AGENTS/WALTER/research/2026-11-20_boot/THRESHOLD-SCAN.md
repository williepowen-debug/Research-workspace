# November 20 boot threshold scan (walter-7f, laptop; charter 6b/6c)

Registries loaded at 6b: RED FALSIFICATION_TRIGGERS_SCAN.tsv (banner sha 7358ccf1ef5e matches canon FALSIFICATION_TRIGGERS.tsv), REGINALD THRESHOLDS.tsv (REG-T-01 to 08), CREED THRESHOLDS.tsv (last real data refresh 2026-11-06; monthly and qualitative rows; T-08a FIRED effective 9/24 stands, no exit registered), HANS THRESHOLDS.tsv (17 rows; T-12 UNINSTRUMENTED, no clean-board credit). FRED values first-published, pulled 2026-11-20T16:24:36Z to 16:24:39Z; vendor intraday pulls 16:24:04Z and 16:28:34Z (not closes).

| IDs | Observation / result |
|---|---|
| Safety net VIX > 30 or +5 intraday | **MET (VIX > 30 leg):** vendor ^VIX 30.19 at 16:24:04Z; PROME 31.09 at 11:19 ET; 29.58 at 16:28:34Z; 30.07 at 16:35:48Z (watcher). +5 leg not met (VIXCLS 28.44 [Nov 19]). FLASH card SIG-W-20261120-001. Re-crossings do not re-fire. |
| REG-T-04 (HY > 350 x3) | HY 352 [Nov 19] first-published (334, 343, 347, 352 for Nov 16 to 19): day 1 of 3. Near-trigger watch (card 001). Fires on publication of a third consecutive close over 350. |
| RED-FT-02, REG-T-03 (> 320 x3) | Fired states unchanged; exit legs (< 300 x3; <= 300 x5) not near. |
| HY safety net +25 bp single session | +5 bp [Nov 19]: not met. |
| RED-FT-07 (CCC > 930) | CCC 1,361 [Nov 19]: FIRING-BANKED, RED owns. |
| RED-FT-06 | UN-FIRED (exited 11/18, executed 11/19); not re-armed. VIXCLS 28.44 [Nov 19]. |
| RED-FT-09 (5y5y > 2.55 x5) | T5YIFR 2.10 [Nov 19]: not near. |
| REG-T-08 (SOFR-IORB > 15) | SOFR 3.91 [Nov 19] less IORB 3.90 = +1 bp: clear. |
| RED-FT-05 / REG-T-05 (claims) | ICSA 203,000 [w/e Nov 14]: not near; next print Wed 11/25 (holiday week). |
| REG-T-01 / REG-T-02 | KRE 69.42 (+0.23%), WAL 69.19 intraday: REG-T-01 not near; WAL under 78 inside the existing cycle, no new fire. |
| FLASH pre-gate KRE -3% | Not met (KRE up). Watcher running. |
| CREED-T-08a | FIRED effective 9/24 stands (owner). Not re-graded here. |
| HANS-T-07 L3 exit | TTF named front not read this boot: not gradeable (earliest exit at the 11/20 close, HANS grades). |
| HANS-T-05/06/09/10/11/13 | Not read this boot (no owner request); not cleared. |
| RED-FT-03/04, boundaries 1/2/8 | No settle read this boot; not gradeable. BRENT's 14:28-14:30 window today is BRENT's. |
| Boundary 3 | Cushing 26.147M [w/e Nov 13]; next WPSR in the holiday week. Not met. |
| HENRY HEN-64 (S&P close < 7,100 by 11/25, 40%) | S&P 7,069.61 intraday at 16:28:34Z; a close grades it (HENRY). |

New registered fire this boot: the safety-net VIX > 30 crossing (card 001). No owner-registry fire or exit. Written 2026-11-20T16:39:12Z (date command).
