# POLLY -> CARL: refresh pass 2026-10-28

**Verdict:** All 5 stale ledgers refreshed (none frozen) on Q3 primaries; P02 is effectively unreachable and P03 and P05 are practically safe, but nothing is mathematically fixed. Allstate Q3 is not yet filed.

| Ledger | Result | Reason |
|---|---|---|
| CARRIER.tsv | REFRESHED | 5 Q3 rows from 8-Ks; ALL marked stale |
| ML.tsv | REFRESHED | ML-POLLY-25..27 appended |
| PREDICTIONS.tsv | REFRESHED | Q3 reachability notes; confidences unchanged |
| STATE_MARKET.tsv | REFRESHED | CA FAIR Sep, FL Citizens Sep rows |
| VX.tsv | REFRESHED | rows 1.03, 2.02, 3.01, 4.01; others bannered [STALE] |

| Q3 figure | Value | As-of | Source |
|---|---|---|---|
| PGR CR | 88.7% (9M 87.5%) | 2026-09-30 | PGR 8-K 10/14 |
| TRV CR / Personal Auto | 86.8% / 87.1% (Q2 82.8%) | 2026-09-30 | TRV 8-K 10/16 |
| ALL | Q3 cat $1.65B; CR not filed | 2026-09-30 | ALL 8-K 10/15 |
| UNH MCR; UHC members | 88.4%; 48.3M (MA 7.605M, Medicaid 6.695M) | 2026-09-30 | UNH 8-K 10/13 |
| ELV BCR; members | 90.6%; 44.88M (Medicaid 8.22M, MA 1.898M) | 2026-09-30 | ELV 8-K 10/21 |
| CA FAIR Plan | 698,307; $773B | Sep 2026 | cfpnet.com |
| FL Citizens | 254,836 | 2026-09-30 | citizensfla.com |

- P01: not decidable.
- P02: needs +51.7K in Q4 vs +1.7K in Q3; effectively unreachable.
- P03: 255K vs 400K; Isaias was Cat 2 (10/9); practically unreachable breach until Nov-30.
- P04: not decidable.
- P05: PGR would need ~117% Q4 CR; Allstate pending.
- P06: 469,719 through Sep (Epiq via ABF, secondary); needs 130,282 in Q4.
- P07, P08: not decidable.

**CARL must rule on:**
1. P02/P03/P05 confidences left at 55/85/90 (as-made scoring is yours).
2. Allstate Q3 (due ~early Nov) is needed before P05 can be called.
3. Corrections: Citizens "near a floor" (8/10) was wrong; "336K Mar" was the Feb-28 figure.
4. UNH FY MCR guide not found; ELV Q3-25 BCR derived from stated -70bps. CRL-22 figures are in the SV.

Files: sub_agents/POLLY/{STATUS.md, state_vectors/SV-POLLY-2026-10-28-01.md, workbook/*}. Nothing committed.
