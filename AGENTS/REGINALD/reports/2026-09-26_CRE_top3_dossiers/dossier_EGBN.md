# EGBN CRE-Vulnerability Dossier — Eagle Bancorp (EagleBank; cert 34742; RSSD 2652092; CIK 1050441)
*Built 2026-09-26 (Sat), read-only. $ in millions unless noted. Source keys → list at end. "DERIVED" = my arithmetic, shown. Nothing here is estimated silently.*

---

## 1. EXPOSURE MAP (as of 6/30/2026)

**Mix — total loans HFI $6,622.4 [S1 loan-mix table; S2]**
| Bucket | $ | % loans | Source |
|---|---:|---:|---|
| IPCRE: multifamily | 692.8 | 10.5% (DERIVED ÷6,622.4) | S2 IPCRE-by-collateral table (principal) |
| IPCRE: office | 533.9 | 8.1% | S2 (MD&A: $533.2M amortized-cost basis) |
| IPCRE: hotel/motel | 373.0 | 5.6% | S2 |
| IPCRE: retail | 236.8 | 3.6% | S2 |
| IPCRE: mixed use | 178.2 | 2.7% | S2 |
| IPCRE: industrial | 123.5 | 1.9% | S2 |
| IPCRE: 1-4 fam / res condo | 74.6 | 1.1% | S2 |
| IPCRE: other (land, storage, healthcare) | 520.9 | 7.9% | S2 |
| **IPCRE total** | **2,729.4** | **41%** | S1 |
| Construction – comm. & resi (ADC) | 523.1 | 8% | S1 |
| **Owner-occupied CRE** (separate) | 1,660.7 | 25% | S1 (OO office $133.5 per S3) |
| Construction – C&I owner-occ. | 88.5 | 1% | S1 |
| Commercial (C&I) | 1,540.8 | 23% | S1 |
| CRE conc. ratio (company) / ADC | 267.6% / 66.2% | — | S1 (Q1: 295.1% / 75.7%; Q4-25: 336.6% / 92.1% per S4) |
| SR 07-1 computed (REGINALD) | 258.2% | — | `BANK_EXPOSURE_MATRIX.md:31,47` |

**Geography — IPCRE principal $2,733.6 [S2]:** DC $951.4 (35%) · MD suburbs $672.8 (25%) · other MD $184.3 (7%) · N. Virginia $634.2 (23%) · other VA $197.6 (7%) · other $93.3 (3%).
**Office by geography [S2 table; S3 slide]:** DC $119.1 (22.3%; deck: CBD 11.19% / non-CBD 11.14%) · MD $172.1 (32.2%) · VA $242.7 (45.45%). Deck: "No exposure to Class B CBD office"; Class A $304.8 (13 loans, $36.9 criticized) / B $219.1 (30 loans, $40.2 criticized) / C $9.3.
**Multifamily geography [S3]:** DC $297 (43%) · VA $201 (29%) · MD $150 (21.7%) · other $44 (6.3%); 34 loans, median $9.5M.

**Maturity wall [S2 chart g5 / S3 slide 20-21, quarterly contractual]**
| | 26Q3 | 26Q4 | 27Q1 | 27Q2 | 27Q3 | 27Q4 | 2028 | 2029+ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Office | 89.8 | 46.6 | 32.0 | 26.4 | 46.9 | 39.6 | 160.7 | 91.3 |
| …of which appraised after 6/30/25 | 46 | 11 | 0 | 0 | 0 | 0 | 0 | 2 |
| Multifamily | 141.3 | 263.3 | 71.5 | 126.5 | 26.4 | 0.6 | 2.3 | 59.9 |

- Office through 2028: $441.9 = 82.9% (S3). **Only ~$59 of $533 office (11%) carries an appraisal dated after 6/30/2025** (DERIVED 46+11+2).
- **Multifamily: $404.6 (58%) matures in 2026H2** (DERIVED 141.3+263.3).
- Whole book: $2,531.7 (38%) matures ≤1yr; IPCRE $1,586.3 of $2,729.4 (58%) ≤1yr; construction $440.2 (84%) ≤1yr [S2 maturity table].
- **Interest-only share: NOT DISCLOSED** (10-Q, release, deck searched).

---

## 2. CREDIT TRAJECTORY (5 quarters; HFI unless noted)

| | Q2-25 | Q3-25 | Q4-25 | Q1-26 | Q2-26 | Source |
|---|---:|---:|---:|---:|---:|---|
| Nonaccrual (NPL) | 226.4 | ~118.6 (DERIVED 156.2÷1.3167) | 106.9 | 128.8 | 111.1 | S1; S5 |
| NPL inflows / outflows | 222.8 / 182.8 | 211.8 / 319.6 | 26.1 / 50.5 | 61.6 / 39.8 | 36.0 / 53.7 | S9,S8,S7 (img p2),S6,S1 |
| Special mention | 173.3 | 423.7 | 268.9 | 290.8 | 274.2 | S10,S8q,S5,S6q,S2 |
| Substandard | 702.1 | 534.8 | 514.5 | 447.6 | 459.8 | same |
| C&C incl HFS (deck) | 913 | 1,096 | 874 | 794 | 760 | S3 slide 17 |
| HFS balance (all nonaccrual/C&C) | 37.6 | 136.5 | 90.7 | 55.7 | 49.7 | S1; S5 |
| Gross charge-offs | 84.4 | 141.1 | 12.5 | 26.1 | 49.1 | Note 4; ledger `RUNWAY_COHORT.tsv:59-63` ties |
| NCO / annualized | 83.9 / 4.22% | 140.8 / 7.36% | 12.3 / 0.67% | 26.0 / 1.46% | 47.9 / 2.78% | S1 trend table |
| Provision (loans) | 138.2 | 113.2 | 15.5 | 13.4 | 21.4 | S1 trend table |
| ACL | 183.8 | 156.2 | 159.6 | 147.2 | 121.1 | S2 Note 4 |
| ACL / NPL | 81.2% | 131.7% | 149.3% | 114.3% | 109.0% | S1 |
| Specific ACL / indiv.-assessed loans | 28.5 / 227.0 | 24.7 / 119.1 | 19.6 / 106.9 | 38.4 / 128.8 | 18.5 / 111.1 | S10,S8q,S5,S6q,S2 |
| Office principal | 821.2 | 602.4 | 577.1 | 574.3 | 533.9 | same |
| Office criticized/classified | 270.3 | 113.1 | 107.9 | 94.8 | 77.1 | same |
| Multifamily criticized/classified | NOT PARSED | 184.9 | 175.6 | 175.1 | **284.2** | S8q,S6q,S2 |
| Perf. office ACL coverage | 11.54% | 11.36% | 12.89% | 7.39% | 7.22% | releases |

**Charge-offs by segment (gross)** [S2/S6q/S8q/S5 Note 4; Q1-25/Q4-25/Q1-26 DERIVED by differencing YTD]: IPCRE 68.0 / 123.4 / 8.1 / 11.6 / 38.0 · Construction 10.7 / 7.1 / 0.9 / 0 / 8.7 · OOCRE 4.9 / 10.0 / 2.4 / 2.9 / 0 · **C&I 0.7 / 0.5 / 0.9 / 11.5 / 2.4** (Q2-25→Q2-26).

**ACL on CRE (6/30/26 vs 12/31/25) [S2 allocation tables]:** IPCRE $68.8 (was $98.7) of which **office $39.0 (was $71.4)**, **multifamily $6.7 (was $7.5)**, hotel $5.6, retail $5.9; construction $4.4 (was $11.2); OOCRE $17.2.

**HFS transfers & sales (the disposition channel)**
| Period | Transfer FV | CO on transfer | FV ÷ pre-transfer cost (DERIVED) | Sold | Sale result |
|---|---:|---:|---:|---|---|
| FY-2025 | 201.4 | 132.3 (net) | 60.4% = 201.4/(201.4+132.3) | 7 loans | loss $4.7M; +$6.3M disposition costs, $8.4M HFS valuation adj. [S5] |
| Q1-26 | 111.8 | 11.6 | 90.6% | 8 loans, carrying $143.8 (deck) | gain $3.6M; $2.9M valuation adj. [S6q,S4d] |
| Q2-26 (DERIVED H1 − Q1) | 126.7 | 25.1 | 83.5% | 10 loans, carrying $161.5 (deck) | gain $2.2M (release: $2.3M loan-sale gain) [S2,S3] |
- H1-26 cash proceeds from loan sales $293.8 [S2 cash-flow]. Gains ÷ HFS carrying sold ≈ 2.5% (Q1) / 1.4% (Q2) (DERIVED) ⇒ **sales cleared at ~101-103% of the post-mark carrying value** — the marks held. **Sale price as % of original par/UPB: NOT DISCLOSED** (prior partial charge-offs before transfer are not broken out).
- 100% of $49.7 HFS at 6/30/26 "has executed contracts" [S3 slide 16].

---

## 3. THE RUNWAY LIMITATION RE-AUDIT

**Disposition-linked charge-offs are disclosed (as the grid's excluded "gross charge-offs associated with loans reclassified to HFS or sold")**: 9M-25 $170.3 (of which $124.1 on HFS still held; Q3 transfers alone $109.5) · FY-25 $176.5 · Q1-26 $11.6 · H1-26 $36.7 [S8q; S5; S6q; S2].

| Quarter | Gross CO | (a) Disposition (HFS/sold) | (b) Retained-book | Basis |
|---|---:|---:|---:|---|
| Q2-25 | 84.4 | **16.6 – 60.8 (range)** | 23.6 – 67.8 | DERIVED: floor = FY transfer COs 132.3 − Q3 109.5 − Q4 ≤6.2; cap = 9M 170.3 − Q3 ≥109.5. 10-Q also calls Q2 COs "related to actual **and expected** dispositions" [S10] — HFI loans marked to exit value are in (b) by this measure. |
| Q3-25 | 141.1 | **≥109.5** | ≤31.6 | S8q explicit transfer CO |
| Q4-25 | 12.5 | 6.2 | 6.3 | DERIVED 176.5 − 170.3 |
| Q1-26 | 26.1 | 11.6 | 14.5 (incl C&I 11.5) | S6q |
| Q2-26 | 49.1 | 25.1 | **24.0** | DERIVED 36.7 − 11.6 |
| **TTM Q3-25→Q2-26** | **228.7** | **≥152.4 (≥67%)** | **≤76.3** | |

**Were retained charge-offs already reserved?**
- Q2-26: specific ACL fell $38.4 → $18.5 (−$19.9) while nonaccrual COs were $25.0 (deck NAL roll: 128.8 +36.0 −14.7 paydowns −25.0 CO −14.0 to HFS = 111.1) ⇒ **up to ~80% of Q2 retained COs consumed specific reserves booked in Q1** (DERIVED 19.9/25.0; upper bound — new specifics on new NALs would net against it). 10-Q: ACL decline "primarily due to charge-offs of previously reserved amounts" [S2]. The DC office NAL fell $36.5 → $19.2 (−$17.3) [S4d vs S3 slide 24] — consistent with the Q1-migrated office relationship being written down against its Q1 specific.
- Q1-26: "$16.8M (64.6%) of $26.0M NCOs were classified non-accrual" [S4d].
- Q2-25/Q3-25: **not** pre-reserved — provision was built in the same quarters (Q2-25 provision $138.2 vs NCO $83.9; office coverage 5.78%→11.54%). **Q2-25→Q2-26 cumulative provision $301.7 vs NCO $310.9** (DERIVED): the 0.53yr runway is largely measuring the drawdown of the Q2-25 reserve build.

**Verdict on 0.53yr: (c) MIXED — dominantly a disposition artifact, with a rising genuine run-rate underneath.** ≥67% of the TTM charge-offs are HFS/sale marks; but retained-book charge-offs have risen three straight quarters (6.3 → 14.5 → 24.0).

**Better statistics (computed)**
| Statistic | Value | Arithmetic |
|---|---:|---:|
| Legacy runway (ACL ÷ TTM gross CO) | 0.53 yr | 121.1/228.7 (ledger) |
| ACL ÷ TTM **non-disposition** CO | **≥1.59 yr** | 121.1/≤76.3 (floor; Q3 disposition may exceed 109.5) |
| Post-break window Q4-25→Q2-26, ex-disposition, annualized | 2.03 yr | 44.8/3×4=59.7/yr |
| H1-26 retained, annualized | 1.57 yr | 38.5×2=77.0/yr |
| **Q2-26 retained only, annualized (run-rate warning)** | **1.26 yr** | 24.0×4=96.0/yr |
| Cohort median (context) | 2.97 yr | `BANK_EXPOSURE_MATRIX.md` §3c |
| **ACL ÷ (substandard HFI × realized exit haircut)** | 1.98× @13.3% (H1-26 haircut) · 1.60× @16.5% (Q2-26) · **0.67× @39.6% (FY-25)** | 121.1/(459.8×h) |
| (ACL + TTM PPNR $96.2) ÷ same @39.6% | 1.19× | 217.3/182.1 |

**Recommendation:** replace runway with the **ex-disposition runway (ACL ÷ annualized retained-book CO, trailing 2Q)** plus the **ACL-vs-substandard-at-realized-haircut multiple**. The haircut dependence (0.67×–1.98×) is the real uncertainty, not the charge-off pace.

---

## 4. DETERIORATION vs DELIBERATE REDUCTION vs COMPLETED LOSS RECOGNITION

| Reading | Evidence (dated) |
|---|---|
| **Deliberate reduction — STRONG** | Office $976 (6/23) → $533 (6/26): CO $205 / HFS $82 / paydowns $156 [S3 slide 19]; CRE conc. 336.6%→267.6% in 2 qtrs; C&C incl HFS $1,096 (Q3-25) → $760 (−30.7%) [S3]; NPL outflows > inflows 4 of last 4 quarters. |
| **Completed recognition (office) — MODERATE-STRONG** | Office criticized $287.0 (12/24) → $77.1; 85.5% of office rated pass; office wtd LTV 61% / DSCR 1.3 [S3 slide 20]; HFS sales at/above marks; 2 office NALs $34.3 carry substandard ratings [S3]. |
| **Deterioration — REAL, and it moved to MULTIFAMILY** | C&C **downgrades $159.9 (Q1) → $216.1 (Q2)** [S4d; S3 slide 16]; 10-Q: substandard fell only because of HFS and payoffs, "partially offset by additional downgrades… substantially from loans previously rated watch or special mention" [S2]. **MF criticized $175.1 → $284.2 (+62%) in Q2; 41.0% of MF book criticized; MF wtd DSCR 1.0, LTV 58** [S2; S3 slide 21]. **MF ACL only $6.7 (0.97% of MF; 2.4% of MF criticized)** (DERIVED). $404.6 of MF matures 2026H2. |
| Loan-level stress (S3 slide 25) | 7 criticized loans >$10M mature Aug–Dec 2026 at DSCR <1 ($249 total, e.g. PG apartment $56.0 SS, LTV 88%, DSCR 0.63; storage $56.2 SM, 2022 appraisal; DC apartment $20.5 SS, DSCR 0.15). Mixed-use DC $15.9 SS at **LTV 154%, still accruing**. |

**Verdict: office = completed-recognition-and-exit (high confidence); the book as a whole = deliberate reduction that is being partly REPLENISHED by new multifamily/other migration (medium confidence).** The July grade ("de-risking through realized loss") stands for office. It does not extend to multifamily, which the July grade could not see (the MF criticized table is 10-Q-only, filed 8/6).

---

## 5. LOSS INPUTS

| Item | Value | Source |
|---|---:|---|
| PPNR Q2-26 | 29.1 | DERIVED 62.35+10.76−44.03 (S1) |
| PPNR TTM Q3-25→Q2-26 | 96.2 | DERIVED 28.8+10.7+27.7+29.1; Q4-25 carries $10.0 legal contingency + HFS disposition costs |
| Net income Q2-26 / TTM | 6.9 / **−48.3** | S1 trend table (Q4-25 now −$2.4; the 1/21/26 release printed +$7.6 [S7] — revised, reason not verified beyond the $10.0M legal line) |
| CET1 (holdco) | 14.58% | S1 |
| CET1 bank $ / RWA / ratio | $1,210.6 / $8,098.3 / 14.95% | `workbook/AOCI_COHORT_2026Q2.tsv:5` (Call Report 6/30/26); AOCI-adjusted 13.87%, +0.75×HTM 13.10% |
| CET1 excess over 10% (bank) | $400.8 | DERIVED 1,210.6 − 809.8 |
| TCE / TCE ratio / TBVPS | $1,150.5 / 11.91% / $37.73 | S1 non-GAAP table |
| ACL | 121.1 (1.83%) | S2 |
| Office wtd LTV / DSCR / $PSF | 61% / 1.3× / $224 (LTV 65% on 2026 maturities, 53% on 2027) | S3 slide 20 — LTVs on appraisals mostly >12m old |
| MF wtd LTV / DSCR / debt yield | 58% / 1.0× / 6.0% | S3 slide 21 |
| Realized exit (HFS transfer FV ÷ cost) | 60.4% FY-25; 90.6% Q1-26; 83.5% Q2-26 | DERIVED, §2 |
| Loss severity on resolved office loans (per-loan) | **NOT DISCLOSED** | Deck gives only cycle aggregates |
| DOJ/AML settlement | $9.8 paid, fully accrued at FY-25; 1-yr NPA from 6/30/26 | S11 8-K 8.01; S2 |

---

## 6. INDIRECT EXPOSURE VIA CREDIT FUNDS (kept separate from direct CRE)

| Channel | Value (6/30/26) | Source |
|---|---:|---|
| NDFI total (RC-C 9.a) | $91.7 (1.37% of loans) — **100% Memo 10a mortgage-credit intermediaries** | `workbook/NDFI_COHORT.tsv:6` |
| PC-NDFI (business-credit intermediaries + PE funds) | **$0** | same |
| Unfunded NDFI commitments | $77.9 | same |
| NDFI nonaccrual / past-due | $0 / $0 | same |
| REIT / fund-finance / subscription lending | **NOT DISCLOSED** (no mention in 10-Q or deck) | S2, S3 searched |
| Top-25 loan: "Pledged non-marketable securities," C&I, other-US, $80.5, pass, matures 5/15/2029 | collateral nature (fund interests or not) **UNKNOWN** | S3 slide 26 |
| **Direct CRE booked outside CRE lines** — MI3 (RCON2746, CRE not secured by RE, in C&I) | $152.7; v1a 10.77% (cohort max), down from $305.0 (9/30/23) | `workbook/MI3_COHORT.tsv:43` |

Read: indirect credit-fund exposure is immaterial; the material "hidden" item is MI3 — which is **direct** CRE risk in C&I clothing, not a fund channel.

---

## 7. UNKNOWNS / NEXT DISCLOSURE / WHAT WOULD WEAKEN THE CONCERN

**Next print:** EGBN Q3-26. **No date announced** — no 8-K after 9/14/26 (that one only added Curley to the Risk Committee) [EDGAR submissions, pulled 9/26]; web search found nothing. Pattern: releases 10/22/25, 1/21/26, 4/22/26, 7/22/26 — all Wednesdays AMC ⇒ **Wed 10/21/26 AMC is a four-quarter-pattern ESTIMATE, UNCONFIRMED.** The 10-Q (~early Nov) carries the MF criticized table and ACL by collateral type; the 8-K/deck carries NPL flows, the C&C waterfall and the loan list.

**Unknowns:** exact Q2-25/Q3-25 disposition split (range only); sale price vs par; IO share; per-loan office severity; the $80.5 securities-backed loan; the deck C&C waterfall has 6 labels and 5 values (read as one "HFS Sold" bucket, which ties in Q1 and Q2).

**Falsifiable — concern WEAKENS if Q3-26 shows:**
1. C&C downgrades < $100 (vs $216.1 in Q2) and MF criticized ≤ $284.2.
2. Retained-book charge-offs (gross CO − HFS/sold-linked CO) < $10 (vs $24.0).
3. The Aug–Dec 2026 criticized maturities (PG apartment $56.0, storage $56.2, DC apartment $42.9, Fairfax office $22.1) pay off or refinance without moving to nonaccrual/HFS.
4. The $35.4 DC apartment payoff (deck footnote 5, S3 slide 25) is confirmed in the 30-89 table.
5. New HFS transfers mark at ≥85% of cost.

**Concern STRENGTHENS if:** ACL/NPL < 105% (the July frame's bear line); MF nonaccrual rises from ~1% of MF; HFS transfer haircut moves toward the FY-25 39.6%; provision < NCO for a third straight quarter while downgrades stay > $150.

---

## BOTTOM LINE FOR REGINALD
1. **0.53yr is mostly a disposition artifact:** ≥67% of TTM charge-offs ($152.4 of $228.7) were HFS/sale marks, and the ACL being drawn down is the Q2-25 build (5-qtr provision $301.7 ≈ NCO $310.9).
2. **Replace the metric:** ex-disposition runway is ≥1.59yr TTM, but only **1.26yr on Q2-26 alone**. That rate rose three quarters running ($6.3 → $14.5 → $24.0), though up to ~80% of Q2's was pre-reserved.
3. **Office looks done:** criticized $287 → $77, 85.5% pass, sales cleared at/above marks. The July "de-risking" grade holds for office.
4. **The new risk is multifamily, and it is barely reserved:** MF criticized +62% to $284.2 (41% of the MF book), DSCR 1.0, $404.6 maturing in 2026H2, MF ACL only $6.7. Q2 C&C downgrades were $216.1.
5. **Verdict: MIXED, medium confidence.** Capital is ample (CET1 14.6%, $401 over 10%). The swing factor is the exit haircut on the $459.8 substandard book: ACL covers 2.0× at H1-26 marks but 0.67× at FY-25 marks. Q3 (est. Wed 10/21, unconfirmed) should show downgrades and MF migration.

---

## SOURCES
| Key | Document | Accession / URL |
|---|---|---|
| S1 | Q2-26 8-K EX-99.1 (7/22/26) | 0001050441-26-000088 · sec.gov/Archives/edgar/data/1050441/000105044126000088/final-erq2x2026xearnings.htm |
| S3 | Q2-26 deck EX-99.2 | same filing · …/final-2q2026egbnearnings.htm |
| S2 | Q2-26 10-Q (filed 8/6/26), incl. charts g3–g5 | 0001050441-26-000096 · …/000105044126000096/egbn-20260630.htm |
| S4 / S4d / S6 | Q1-26 8-K release / deck (4/22/26) | 0001050441-26-000062 · …/erq1-2026xearningsreleas.htm, a1q2026egbnearningsdeck3.htm |
| S6q | Q1-26 10-Q | 0001050441-26-000066 · …/egbn-20260331.htm |
| S5 | FY-25 10-K | 0001050441-26-000021 · …/egbn-20251231.htm |
| S7 | Q4-25 8-K release (image pages 1-2) | 0001050441-26-000006 · …/erq4-2025xearningsreleas001-002.jpg |
| S8 / S8q | Q3-25 8-K release; Q3-25 10-Q | 0001050441-25-000122; 0001050441-25-000134 |
| S9 / S10 | Q2-25 8-K release; Q2-25 10-Q | 0001050441-25-000102; 0001050441-25-000108 |
| S11 | 8-K 8.01 DOJ settlement (6/30/26); 8-K/A 5.02 (9/14/26) | 0001050441-26-000081; 0001050441-26-000106 |
| Repo | `AGENTS/REGINALD/BANK_EXPOSURE_MATRIX.md:31,47,139`; `workbook/RUNWAY_COHORT.tsv:59-63`; `workbook/ACL_ROLLFORWARD_COHORT.tsv:57,59-60,63`; `workbook/NDFI_COHORT.tsv:6`; `workbook/AOCI_COHORT_2026Q2.tsv:5`; `workbook/MI3_COHORT.tsv:43`; `reports/2026-07-25_EGBN_Q2_grade_plus_FL_smalltier_watchcard_fill.md`; `AGENTS/CREED/research/2026-09-26_CRE_VULNERABILITY_MAP.md:42` (DC/NoVA = densest new CMBS DQ cluster, Aug) | |
| Web | Q3 date search, 9/26/26 — none found | [IR news](https://ir.eaglebankcorp.com/news/default.aspx) · [Globe and Mail Q2 call notice](https://www.theglobeandmail.com/investing/markets/stocks/EGBN-Q/pressreleases/3179895/eagle-bancorp-announces-earnings-call-on-july-23-2026/) |
