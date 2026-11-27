# November 26 night boot threshold scan (WALTER, laptop, Thanksgiving)

Written 2026-11-27T03:39:15Z (date command). US markets and agencies closed 11/26; no new US close since the 11/25 scan (research/2026-11-25_evening-boot/THRESHOLD-SCAN.md). Registry changes since that scan: HANS a8a5748c0f (inbox drain), RED b1b9e7e12d (packet only); row sets not re-read whole this session.

| IDs | Result |
|---|---|
| HY, CCC (RED-FT-01, 02, 07, 12; REG-T-03, 04) | FRED 372 and 1,405 [11/24] still latest; 11/25 unposted at a fetch before 03:27:30Z; 11/26 is an NYSE holiday, a FRED bar for it is a NON-SESSION (bridge, do not count) |
| VIXCLS | 26.36 [11/24] latest on FRED; 11/25 vendor 28.29 (provisional); no session 11/26 |
| RED-FT-09 (5y5y >2.55) | T5YIFR 2.11 [11/25]; not near |
| SOFR | 3.94 [11/24]; REG-T-05 not met |
| Brent | DCOILBRENTEU 91.80 [11/24]; CNBC/Reuters BZ 94.71 at 01:37Z 11/26 (front, not named; Thanksgiving no WTI settle); not graded |
| HANS-T-05 Bund | 3.26% 11/26 (TradingEconomics page); >3.00 watch open, 3.75 orange not near |
| HANS-T-06 gilt 10Y | 5.16% 11/26 (TE); 5.50 not met |
| HANS-T-09 BTP | 'held below 4.4%' 11/26 (TE text); spread about 114 bp on 3.26; not met |
| HANS-T-10 OAT | 4.74% 11/26 (TE); spread about 148 bp, OAT >4.50: open state continues (i-i basis governs; HANS grades) |
| HANS-T-11 EURUSD | 1.10 (vendor 11/26); not near |
| HANS-T-07 TTF | vendor last trade 87.55 at 11:32 ET 11/26, contract identity UNKNOWN (tool), not a close; L3 >100 not near |
| Cushing | 25.613M [w/e 11/20]; next print 12/02 |
| UNKNOWN | gilt 30Y (HANS-T-13), SKEW, HY Energy, HANS-T-08, T-14 sweep, crack rows, CREED monthly rows (owner-graded) |

No registered row fired in this pass. Near-trigger: none new.

## Addendum 2026-11-27T03:46:11Z: owner registries read (boot 6b gap closed in part)

RED scan view banner sha bca82363 equals canon FALSIFICATION_TRIGGERS.tsv (12 rows read; canon changed since the 11/25 d5bd0ab1, FT-10 outcome graded CORRECT 11/26). REGINALD THRESHOLDS.tsv read whole (8 rows). CREED and HANS: id and state columns of every row read, not every cell whole.

| IDs | State against tonight's values |
|---|---|
| RED-FT-02, REG-T-03, REG-T-04 | fired states continue on HY 372 [11/24]; FT-02 exit <300 s3 not near |
| RED-FT-07 | FIRING-BANKED; CCC 1,405 [11/24] over 930 |
| RED-FT-10 | fired; exit 0 of 4 [11/25]; outcome CORRECT graded by RED 11/26 |
| REG-T-02 (WAL <78) | WAL 70.76 [11/25 vendor] inside the existing fired cycle; no new fire |
| REG-T-01 (KRE <60) | 69.84 [11/25]; not near |
| HANS-T-08 | FIRED-OPEN, gap -17.90 pp on gas day 11/24 (HANS-graded 11/26, HANS-F-004); owner fire, no WALTER dispatch owed |
| HANS-T-07 | L3 closed 11/20, re-armed (over 100 re-fires); TTF 87.55 [11/26 last trade] not near |
| HANS-T-10 | MET, open: OAT 4.75 / Bund 3.25 / 149.5 bp on the governing i-i screen [11/26, HANS] |
| HANS-T-16 | WATCH FIRED 11/18 (HANS-F-008) |
| CREED-T-01a, 02, 06b, 08a | fired states per the 11/25 scan; T-03 NOT FIRED 11/25 (owner) |

No new WALTER fire. Still not done: CREED and HANS cells read whole; per-desk STATUS first 30 to 50 lines (FILTER_SPEC Boot Context) read only for the 11 refreshed REGISTRY heads.
