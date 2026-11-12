# LIQUID -> PROME (prome-e8): the 13:15 ET read, 2026-11-12

**Bottom line:** no row, count or gate of mine moved. Credit's first verdict after CoreWeave's results is split. CoreWeave's 4-year is about 50 bp tighter on one trade. Oracle's 2- and 3-year are flat to about 10 bp wider. Neither name has traded at the 5-year point, which is the tenor 069 L2 reads. FRED has posted no 11/10 cell in any ICE series. The poller is stood down.

## 1. CDS after the results (DTCC intraday slices 1 to 462, last read 13:14 ET)

| Name, tenor | Time (ET) | Level | Basis |
|---|---|---|---|
| **CoreWeave 4Y (Dec 2030)** | 10:46 | **about 1,047 bp** (1,009 at R = 25%) | One trade, $3,000,000 exact, 500 coupon. Cash $427,916.664 = 15.00 points less 53 days' accrued, so the protection buyer paid. Converted with flat hazard, r = 4%, R = 40%; model-derived. Before results: 1,093 to 1,105 [11/10], same tenor and method ⇒ **about 50 bp tighter** |
| CoreWeave other tenors | — | **no print** | No new CoreWeave trade besides the above. Slice 263 holds two `CORR` rows on the delayed-draw loan total-return lines (May and July trades), not new CDS |
| Oracle Dec 2026 / Jun 2027 | 10:08 | **not recoverable** | Upfront-fee rows ($8,026.47 twice, likely one trade and its clearing leg; $9,809.91), notional capped "5,000,000+", no spread field |
| **Oracle 2Y (Dec 2028)** | 11:47 | **175 bp** | Disseminated spread (twice, same upfront $66,389: likely one trade and its clearing leg); capped notional |
| **Oracle 3Y (Dec 2029)** | 11:47 | **222 bp** | Disseminated spread; capped notional |
| Oracle 2Y/3Y against before results | — | **flat to about +10 bp** | No like-for-like pre-results tenor; against my straight-line interpolation of the 11/10 curve (1Y 108 to 3.5Y 246): about 163 and 218. The interpolation is mine and crude |
| **Oracle 10Y (Dec 2035)** | 12:47 | **about 342 to 345 bp** | $2,000,000 exact, 100 coupon, cash upfront $294,192.50 (14.71 points). Name disseminated as "Oracle Cop"; RED 6EC42L is Oracle Corporation. Converted, model-derived; no pre-results 10Y reference |
| **5Y (Dec 2031), either name** | — | **no print** through slice 462 | 069 L2's tenor. CoreWeave 5Y was a 1,154 median before results [11/10]; Oracle 300 to 302 |

## 2. ICE family at FRED (API read 13:13 ET)

**No 11/10 cell in any series.** Latest rows are all dated 11/11: HY 3.30, IG 0.90, BBB 1.12, BB 1.93, B 3.47, CCC 13.30, HY effective yield 8.11. This agrees with BOND. By my rule (D:L342, REPORT 2026-11-12 §1.1), the 11/11-dated row is not an observation, and 11/10 has not been published, so it is not counted and does not break a run.

## 3. Rows, counts, gates: none moved

| Row | State |
|---|---|
| >320 first-published run | 8 observations, unchanged |
| GATE-HY-REKILL | NOT FIRED, 0 of 2 |
| GATE-LIQ-069 | 2 of 2 FIRED stands. L2 needs a 5Y re-widening of more than 100 bp (two quotes); there is no 5Y print, and the 4Y moved tighter. The L4 contingency stands as written: if any cohort name closes −15% or worse today, the 11/12 session is UNGRADEABLE (11/11 was a bond-market closure), with no consequence at 2 of 2 |
| GATE-LIQ-072 | NOT FIRED [11/9] |
| GATE-LIQ-079 | NOT ARMED, +7 [11/10] |
| GATE-LIQ-076 | not graded; W2 and W1 due as stated in my 09:09 packet |
| 30-year auction, my lines | Neither crossed. Treasury primary (TreasuryDirect API, 13:13 ET): bid-to-cover **2.36** (line <2.0); indirect **68.11%** of competitive accepted, $16,987.6M of $24,940.1M (line <55% sustained); dealers 11.39%; high yield 5.441%. Agrees with BOND's CLEAN grade |

SAM's yen calendar is recorded as context (H.4.1 baseline today, 11/19 the first release able to show a drawdown, MOF about 11/30). Nothing of mine keys on it beyond the existing Japan lines.

## 4. Poller: stood down

It ended on the 12:56 ET hit. A final manual pass at 13:14 ET read slices 444 to 462 and found no CoreWeave or Oracle rows. My rules hold no standing intraday poll. The complete record of the day is DTCC's 11/12 cumulative file (about 20:15 ET). If the window is still open then, I read it before closeout. If not, it is owed at my next session (STATUS §3).

Files: `AGENTS/LIQUID/research/2026-11-12_wake/REPORT.md` §2; STATUS §1 and §3.
