# FLG (Flagstar Bank, N.A.) — CRE-vulnerability dossier

**Built:** 2026-09-26 for REGINALD. Read-only; no repo file touched. **Registrant:** FLAGSTAR BANK, N.A., CIK 0000910073, verified via `data.sec.gov/submissions` (former names include Flagstar Financial, Inc. and New York Community Bancorp). The holding company merged into the bank in Oct-2025, so 10-Q figures are bank-level and comparable to RSSD 694904.
**Latest data:** 6/30/2026. **No FLG 8-K has been filed since 2026-07-24.** EDGAR shows only the 10-Q (8/6), two 13G/As and a 13F-NT (8/14) after that date.

Source keys used in the tables:
- **[10Q]**: 10-Q Q2-2026, acc 0000910073-26-000068, https://www.sec.gov/Archives/edgar/data/910073/000091007326000068/fbc-20260630.htm
- **[ER]**: 8-K EX-99.1, Q2-2026 earnings release, acc 0000910073-26-000065, https://www.sec.gov/Archives/edgar/data/910073/000091007326000065/a2q2026earningsrelease.htm
- **[DECK s#]**: EX-99.2 slide #, same accession (`flg_2q26xearningsxpresen0##.jpg`)
- **[ER-Q3/Q4-25]**: prior earnings releases, acc 0000910073-25-000172 and 0000910073-26-000017

---

## 1. EXPOSURE MAP

### 1a. CRE by property type (HFI, 6/30/2026; total loans HFI $60,987M) [10Q]

| Book | $M | % loans | 12/31/25 $M | Note |
|---|---:|---:|---:|---|
| **Multifamily (MF)** | **26,931** | 44.2% | 28,983 | −7.1% H1 |
| · NY State MF | 14,600 | 23.9% | 15,800 | |
| · NY-State MF subject to rent regulation to any degree | 12,800 | 21.0% | 13,900 | 87% of NY MF |
| · **≥50% rent-regulated units (NY State)** | **8,900** | **14.6%** | 9,500 | [10Q]. The NYC-only figure is **$8,490M** [DECK s15]. $7.4B of that has ≥70% of units regulated |
| · NYC "market & <50% RR" | 4,898 | 8.0% | — | [DECK s15] |
| Non-MF CRE, total | 8,244 | 13.5% | 9,314 | −11.5% H1 |
| · Office (owner + non-owner occupied) | 1,784 | 2.9% | 1,954 | |
| · Retail | 1,348 | 2.2% | 1,560 | |
| · Industrial | 3,273 | 5.4% | 3,928 | |
| · Other | 1,839 | 3.0% | 1,872 | |
| Construction / ADC | NOT DISCLOSED separately in the 10-Q | | | It sits inside the SR 07-1 numerator (Call Report) |
| Unsecured CRE booked in C&I (Call Report item RCON2746) | 440.6 | 0.72% | — | `AGENTS/REGINALD/workbook/MI3_COHORT.tsv:127` (MIRROR at FLG, `MI3_FLG.tsv`) |

**CRE concentration uses two bases. They do not conflict; the denominators differ.**

| Basis | Ratio | Numerator / denominator | Source |
|---|---:|---|---|
| SR 07-1 (construction + MF + non-owner-occupied CRE) ÷ total risk-based capital | **327.5%** | $32.76B / $10.00B | `BANK_EXPOSURE_MATRIX.md:79-81` |
| Company basis: CRE excluding $2.6B owner-occupied ÷ (Tier 1 capital + loan-loss reserve) | **350%** (367% at Q1, 381% at Q4-25, 501% at 12/31/23) | $32.6B / (8,441 + 869) = **350.2%, DERIVED** (reconciles to the company's figure) | [DECK s13, s25]; Tier 1 from `AGENTS/FLG/workbook/KB.tsv:40` |

⚠️ The matrix's "~2 quarters to cross 300%" (`BANK_EXPOSURE_MATRIX.md:88`) holds on the SR 07-1 basis only. On the company basis the ratio falls about 14–17pp a quarter, so crossing 300% takes about 3 quarters (DERIVED). Anyone who cites "300%" must name the basis.

### 1b. Geography, MF book (HFI, 6/30/26) [10Q]

| Area | $M | % MF |
|---|---:|---:|
| Manhattan / Brooklyn / Bronx / Queens / Staten Island | 4,513 / 4,175 / 2,604 / 2,028 / 68 | 17 / 16 / 10 / 8 / 0 |
| **NYC total** | **13,388** | **51%** |
| New Jersey / Long Island | 3,314 / 372 | 12 / 1 |
| **Metro NY total** | **17,074** | **64%** |
| Pennsylvania / Florida / Ohio / other NY State / all other | 2,699 / 1,289 / 940 / 872 / 4,057 | 10 / 5 / 4 / 3 / 14 |

- **NYC ≥50% RR by borough [DECK s15]:** Brooklyn 37.9%, Bronx 27.0%, Manhattan 20.6%, Queens 14.2%.
- **Non-MF CRE by state [10Q]:** NY $3,463M (42%), MI 9%, CA 9%, FL 8%, NJ 6%.

### 1c. Repricing / maturity wall (UPB) [10Q via `AGENTS/FLG/workbook/MATURITY_WALL.tsv`, 6/30/26 rows]

"Option" loans are adjustable-rate loans, tabulated by the date their rate resets. "Non-option" loans are fixed-rate, tabulated by contractual maturity. A reset leaves the loan on the book at a new rate; a maturity requires a refinance or repayment.

| Year | MF option resets | MF maturities | **MF total** | Non-MF CRE (reset + maturity) | Weighted avg coupon of MF resets [DECK s14] | NYC ≥50% RR only, $B @ coupon [DECK s15] |
|---|---:|---:|---:|---:|---:|---:|
| 2026 (H2) | 2,035 | 665 | **2,700** | 1,545 | 4.15% | 1.3 @ 4.98% |
| **2027** | 7,038 | 1,465 | **8,503** | 1,553 | **3.87%** | **2.9 @ 3.85%** |
| 2028 | 3,524 | 1,923 | **5,447** | 1,705 | 4.19% | 1.4 @ 4.66% |
| 2029 | 2,238 | 1,605 | 3,843 | 872 | 4.52% | 1.1 @ 5.09% |

- **Quarterly split for the next 8 quarters: NOT DISCLOSED.** Annual buckets only.
- **Office maturities by year: NOT DISCLOSED.** Office is included in the CRE column.
- **Size of the reset shock (DERIVED proxy):** MF loans modified for borrowers in difficulty during H1-26 had their rates cut *from* a weighted 8.03% [10Q, modifications note]. That is the reset rate these borrowers faced. The 2027 cohort's 3.85–3.87% coupon therefore roughly doubles at reset absent modification. This is a proxy, not a disclosed reset rate.
- **Interest-only loans:** $5.3B of MF is interest-only (19.7% of MF, DERIVED). The weighted-average interest-only period left is 25.4 months, and about 31% of these loans start amortizing by end-2026 [10Q].
- **Reset status of the NYC ≥50% RR book [DECK s15]:** 43% already repriced, 34% reset within 18 months. In the criticized + classified subset, **49% reset within 18 months**.

### 1d. Timing of the rent freeze (RGB = NYC Rent Guidelines Board)

- **RGB Order #58** sets 0% on both 1- and 2-year renewals for leases starting 2026-10-01 → 2027-09-30 (`AGENTS/FLG/workbook/RGB_GUIDELINES.tsv`, row 58).
- FLG re-tests debt-service coverage in Q2 each year on the prior year's borrower financials [10Q credit-review text]. The FY2027 financials, reviewed in **Q2-2028**, are the first to carry most of a freeze year (`STATUS_MATRIX.md:29`; `AGENTS/FLG/STATUS.md:75`). **So a quiet Q2-2027 is the expected path.**
- The freeze is contested in court: *Kenilworth Holdings v. NYC RGB*, no stay as of 9/17 (`AGENTS/FLG/STATUS.md:17`).

---

## 2. CREDIT TRAJECTORY

### 2a. Quarterly series

| Quarter-end | Nonaccrual HFI $M (10-Q) | ACL on loans $M | ACL / nonaccrual | Provision, loans, per quarter $M (Call Report) | Gross charge-offs per quarter $M (Call Report) | Criticized + classified $B (incl. held-for-sale, UPB) |
|---|---:|---:|---:|---:|---:|---:|
| 24Q3 | 2,514 | 1,264 | 50.3% | 236.3 | 216.9 | — |
| 24Q4 | 2,615 | 1,201 | 45.9% | 159.2 | 212.0 | — |
| 25Q1 | 3,280 | 1,168 | 35.6% | 81.9 | 124.2 | — |
| 25Q2 | 3,180 | 1,106 | 34.8% | 55.4 | 140.5 | 12.7 |
| 25Q3 | 3,241 | 1,071 | 33.1% | 37.7 | 86.7 | 12.4 |
| 25Q4 | 2,975 | 1,030 | 34.6% | 5.3 | 84.7 | 12.1 |
| 26Q1 | 2,675 | 954 | 35.7% | 1.5 | 112.6 | 11.8 |
| **26Q2** | **2,800** | **869** | **31.0%** | **14.4** | **119.8** | **11.6** |

Sources by column:
- Nonaccrual and coverage: `AGENTS/FLG/workbook/NONACCRUAL_FLOW.tsv` (YTD rows).
- ACL, provision and charge-offs: `AGENTS/REGINALD/workbook/RUNWAY_COHORT.tsv:68-75`.
- Criticized + classified: [DECK s18].

**Other trajectory figures:**
- **Net charge-offs [ER]:** $100M in Q2-26 (0.66% annualised), $78M in Q1-26 (0.52%). **$47M of the Q2 NCOs "had been previously reserved"** [DECK s18].
- **Company-basis provision [ER]:** $18M in Q2-26, $0 in Q1-26. This includes the reserve for unfunded commitments.
- **Nonaccrual rose QoQ in Q2:** +$123M (+5%) including held-for-sale. MF nonaccrual +5%, CRE nonaccrual +7% [ER].

### 2b. Risk ratings by segment (amortized cost $M) [10Q, credit-rating-by-vintage tables]

| Grade | MF 12/31/25 | **MF 6/30/26** | Δ | CRE 12/31/25 | **CRE 6/30/26** | Δ |
|---|---:|---:|---:|---:|---:|---:|
| Pass | 19,632 | 17,860 | −1,772 | 7,279 | 6,406 | −873 |
| **Special mention** | 2,065 | **2,757** | **+692 (+33.5%)** | 352 | 376 | +24 |
| Substandard | 5,025 | 4,182 | −843 | 1,194 | 991 | −203 |
| Nonaccrual | 2,261 | 2,132 | −129 | 489 | 471 | −18 |
| Gross charge-offs, year to date | 285 (FY25) | 162 (H1) | | 41 (FY25) | 31 (H1) | |

- Bank-wide classified loans (substandard + nonaccrual) were **$8.5B vs $9.7B at 12/31/25**. The company says the fall is "primarily attributable to par payoffs of multi-family and CRE substandard loans and the resolution of a single borrower relationship undergoing bankruptcy proceedings" [10Q].
- The criticized + classified slice of the NYC ≥50% RR book is **$4,401M**: 52% of that book. It carries a 1.01x debt-service coverage ratio (amortizing basis) and 78% current LTV [DECK s15].
- **Office criticized balance: NOT DISCLOSED.**

### 2c. ACL allocation [10Q; DECK s17]

| Segment | ACL 12/31/25 | ACL 3/31/26 | **ACL 6/30/26** | Reserve % of loans |
|---|---:|---:|---:|---:|
| MF total | 549 | 509 | **439** | 1.63% |
| · MF ≥50% RR (excl. co-op) | — | 330 | **281** | **2.87%** (NYC basis 3.04% [DECK s16]) |
| · MF market / <50% RR | — | 174 | 153 | 1.00% |
| CRE (10-Q basis) | 229 | 189 | **153** | 1.86% |
| · Office, excluding owner-occupied (deck basis) | — | 61 | **55** | **3.00%**, which implies about $1.83B of such office (DERIVED: 55/0.030) |
| · Non-office CRE | — | 123 | 93 | 1.53% |
| C&I | 150 | 161 | 177 | 0.95% |
| **Total** | 1,030 | 954 | **869** | 1.42% (1.52% including $56M unfunded reserve) |

### 2d. Loan sales and dispositions

| Item | Value | Source |
|---|---|---|
| CRE payoffs **at par**, Q2 / Q1 | $1.1B / $1.1B. MF $0.9B / $0.8B, 44% / 40% substandard. Office $31M / $5M | [DECK s13] |
| MF payoffs at par, H1-26 | $1.7B, **42% from substandard** | [10Q] |
| NYC ≥50% RR payoffs since 1/1/24 | $2.0B, 56% from substandard | [DECK s16] |
| Price of non-par disposals (note sales, discounted payoffs) as % of par | **NOT DISCLOSED**. Net gain on loan sales was "immaterial" in Q2 | [10Q] |
| Transfers to held-for-sale, 2026 | Minimal: nonaccrual "transferred to other assets" $4M in H1; nonaccrual held-for-sale $30M → $5M | [10Q] |

---

## 3. DETERIORATION vs DELIBERATE REDUCTION vs COMPLETED LOSS RECOGNITION

**Why the ACL fell $161M in H1-26, by segment.** Roll-forward [10Q Note 6]; **DERIVED** net changes:

| Segment | Begin | Charge-offs | Recoveries | Provision | End | Net change |
|---|---:|---:|---:|---:|---:|---:|
| MF | 549 | −162 | +10 | **+42** | 439 | −110 |
| CRE | 229 | −31 | +22 | **−67 (reserve release)** | 153 | −76 |
| C&I | 150 | −23 | +18 | +32 | 177 | +27 |
| **Total** | 1,030 | −233 | +55 | +17 | 869 | −161 |

| Reading | Evidence for | Evidence against |
|---|---|---|
| **Completed loss recognition** | Company says the ACL fell "primarily due to charged-off loans which had specific reserves and pay offs" [ER]. **$47M of Q2 NCOs were already reserved** [DECK s18]. The specific allowance on nonaccrual loans fell **$222M → $163M** [10Q; 12/31 total DERIVED 99+60+2+32+29]. The $193M of MF + CRE gross charge-offs were "primarily driven by appraisals received" plus the single bankruptcy resolution [10Q]. **Nonaccrual loans still held in the NYC ≥50% RR book already carry $351M of NCOs, 16.8% of the pre-charge-off balance** [DECK s16]. | MF net charge-off rate flat YoY at 1.17% (`KB.tsv:39`). Whether the appraisals are current is disputed (see §4) |
| **Deliberate reduction** | $1.1B a quarter of CRE payoffs at par, ~40% of them substandard [DECK s13]. That produces a real reserve release in the CRE segment (−$67M provision). MF book −7.1% and non-MF CRE −11.5% in H1 [10Q]. Held-for-sale transfers are negligible, so the ACL did **not** fall by moving loans to held-for-sale | Depends on refinance lenders taking out substandard borrowers at par. That exit is outside the bank's control (`AGENTS/FLG/THESIS.md:34`) |
| **Live deterioration** | **MF special mention +$692M (+33.5%) in H1** while substandard fell. **Modifications for borrowers in financial difficulty were $556M in H1-26 vs $19M in H1-25** (MF $364M, rate cut 8.03% → 5.14%, term +1.1 years) [10Q]. Nonaccrual +5% QoQ in Q2. Gross new nonaccrual $780M in H1. $51M of loans are 90+ days past due and still accruing (`KB.tsv:43`). Cure rate 1.6% (`NONACCRUAL_FLOW.tsv`, 26Q2). The Q2-2028 freeze review has not happened yet | Criticized + classified −9% YoY. 30-89 day delinquencies −63%. Nonaccrual −12% YoY |

**Does FLG's own disclosure explain the ACL decline?** Yes, qualitatively: specific-reserve charge-offs plus payoffs. The segment roll-forward confirms it (MF charge-offs against a positive provision; a CRE release on payoffs).

⚠️ **One gap is unreconciled.** The nonaccrual roll-forward shows **$100M** of H1 charge-offs; the ACL roll-forward shows **$233M** of gross charge-offs. That leaves ~$133M charged off outside the nonaccrual schedule. Possible homes: discounts taken at payoff inside the "payoffs, including dispositions" line, or charge-offs on accruing substandard loans. **The 10-Q does not disclose which.** The ambiguity matters: if the discounts sit inside "payoffs", then some "par payoff" exits were not at par.

**Where I disagree with the FLG desk (their figures, then mine):**
1. FLG leads with a **"$163M specific reserve = 5.8%"** of nonaccrual (`AGENTS/FLG/STATUS.md:31,39`). That is the *remaining* reserve, not total loss recognised. Collateral-dependent loans are written down toward collateral value. The NYC ≥50% RR nonaccrual loans carry **16.8% cumulative NCOs plus a 4.38% ACL, ≈20.5% total** (DERIVED: (351+76)/2,088) [DECK s16]. The 5.8% figure understates recognition; it is not evidence that nothing has been recognised.
2. FLG's H1 "payoff 87.5% of nonaccrual outflow" (`NONACCRUAL_FLOW.tsv`) is correct arithmetic. But the 10-Q attributes the H1 decline **"primarily" to one bankruptcy relationship**, which is lumpy, and FLG's files never mention it. Q2 alone ran at 73.6% payoff with nonaccrual *rising*.
3. The matrix's "NOT release" verdict (`BANK_EXPOSURE_MATRIX.md:107`) is true at the total. **At segment level CRE released $67M in H1 ($35M in Q2).**

**Verdict: mostly completed loss recognition plus deliberate reduction on the book already resolved (confidence: medium-high). The unresolved book shows a live, early-stage deterioration pipeline (confidence: medium).** That pipeline is the $4.4B NYC ≥50% RR criticized pool at 1.01x debt-service coverage, rising special mention, and a jump in modifications. The ACL decline is mainly *consumption of reserves on recognised losses and payoffs*, not under-provisioning of known losses. But **TTM PPNR of $143M is below TTM gross charge-offs of $404M**. Earnings are not rebuilding the reserve, and the bank authorised a **$250M buyback** on 7/24 [8-K Item 8.01].

---

## 4. LOSS INPUTS

| Input | Value | As of | Status | Source |
|---|---:|---|---|---|
| PPNR (pre-provision net revenue), Q2-26 | $66M ($62M adjusted) | Q2-26 | DISCLOSED | [ER] |
| PPNR, trailing 4 quarters | **$143M** (−3 + 48 + 32 + 66). Adjusted: $178M (15 + 60 + 41 + 62) | Q3-25..Q2-26 | DERIVED from disclosed quarters | [ER], [ER-Q3/Q4-25] |
| Net income, Q2 / TTM | $34M / **$48M** (−36 + 29 + 21 + 34) | | DISCLOSED / DERIVED | same |
| CET1 | **$7,937M / 13.16%**; risk-weighted assets $60.3B | 6/30/26 | DISCLOSED | `AOCI_COHORT_2026Q2.tsv:12`; `KB.tsv:40`; [ER] |
| Excess CET1 over the company's 10.5% target floor | $1.6B | 6/30/26 | DISCLOSED | [ER] |
| Total risk-based capital | $10,003M / 16.58% | 6/30/26 | DISCLOSED | `KB.tsv:40` |
| Tangible common equity | **$7,304M**; 8.36% of tangible assets; tangible book value $17.51/share ($15.54 adjusted for warrants) | 6/30/26 | DISCLOSED | [ER] |
| ACL on loans / total ACL | $869M / $925M | 6/30/26 | DISCLOSED | [ER] |
| Current LTV, NYC ≥50% RR: pass / criticized | 61% / **78%** | 6/30/26 | DISCLOSED. LTV = latest appraisal ÷ current loan | [DECK s15] |
| Debt-service coverage (amortizing basis), same two groups | 1.51x / **1.01x** | 6/30/26 | DISCLOSED | [DECK s15] |
| Appraisal recency | 70% of criticized + classified NYC RR loans appraised since 1/1/24; substandard loans re-appraised annually | 6/30/26 | DISCLOSED | [DECK s16]; [10Q] |
| Nonaccrual MF with no related allowance | $1,143M of $2,132M; related allowance $83M | 6/30/26 | DISCLOSED | [10Q]; `KB.tsv:36` |
| Realized sale price as % of par | "Par payoffs" = 100% by label. Discounted exits NOT DISCLOSED | | PARTIAL | [DECK s13] |
| Severity on resolved loans | NOT DISCLOSED for exited loans. For loans still held (NYC RR nonaccrual) the proxy is 16.8% cumulative NCOs | 6/30/26 | DERIVED proxy | [DECK s16] |
| Cumulative MF NCOs since 1/2024 | $689M | 6/30/26 | DISCLOSED | [DECK s14] |
**Sensitivity (DERIVED, illustrative, not a forecast).** Each extra 10pp of loss on the $4,401M NYC ≥50% RR criticized pool = **$440M pre-tax** ≈ 0.5× total ACL, 0.28× the $1.6B excess CET1, 3.1 years of TTM PPNR. A 25pp loss (≈$1.1B) is absorbable by reserve + excess capital without breaching the 10.5% target.
A 25pp loss (78% LTV rising to ~104% implied, pre-costs) ≈ $1.1B, which the reserve plus the capital cushion absorb without breaching the 10.5% target.

---

## 5. INDIRECT EXPOSURE VIA CREDIT FUNDS / NDFI

"NDFI" = non-depository financial institutions: loans to funds, lenders, REITs and other finance companies. Figures below are Call Report memo-10 lines for 6/30/26 (`AGENTS/REGINALD/workbook/NDFI_COHORT.tsv:13`).

| Line | $M | Most likely FLG business line [DECK s5, s20] | Mapping status |
|---|---:|---|---|
| Mortgage credit intermediaries (10a) | 1,108 | "Mortgage Finance" C&I, $940M. Warehouse lending was rebuilt after the 2024 warehouse sale | INFERRED, not disclosed |
| Business credit intermediaries (10b) | 202 | "Lender Finance" | INFERRED |
| **Private-equity funds (10c)** | **867** | "Funds Finance" / "Sponsor Finance" (typically capital-call lines) | INFERRED; facility type NOT DISCLOSED |
| Consumer credit intermediaries (10d) | 764 | "Dealer Finance" / consumer lenders | INFERRED |
| **Other (10e)** | **517** | Residual. **Whether it holds REIT, CRE-debt-fund or mortgage-REIT exposure is NOT DISCLOSED** | UNKNOWN |
| **Total NDFI** | **3,458 (5.65% of loans)** | Up from $2,890M at 3/31/26 (**+19.7% QoQ**, DERIVED from `MI3_COHORT.tsv:126-127`, item9a) | |
| Unfunded NDFI commitments | 1,299 | | |
| NDFI nonaccrual / 30-89 days past due | $0.05M / $13.2M | | Clean |

**Direct vs indirect:**
- **Direct CRE** = §1: $26.9B MF + $8.2B CRE + construction inside the $32.76B SR 07-1 numerator, plus $0.44B of unsecured CRE booked in C&I.
- **Indirect** = NDFI lines whose collateral could be CRE. No line is disclosed as CRE-debt-fund or REIT lending. The 10-Q and deck say nothing about NDFI.
- **Read:** indirect CRE via funds is **not measurable from public disclosure and small next to the direct book (≤$0.5B even if all of "other" were CRE-linked)**. The fast growth in NDFI (Specialized Industries +34% QoQ [ER]) is a C&I and private-credit question for BROCK/LIQUID, not a CRE one.

---

## 6. UNKNOWNS / NEXT REVEALING DISCLOSURE / WHAT WOULD WEAKEN THE CONCERN

**Unknowns (all NOT DISCLOSED):**
- Quarterly reset schedule.
- Office maturities.
- Office criticized balance.
- Prices on discounted exits.
- The $133M gap between the two charge-off schedules.
- How much of the 93% "current or paid off" repriced loans are current vs paid off (`KB.tsv:53`).
- Collateral inside NDFI "other".
- The freeze court outcome (T-12).

**Next disclosures:**

| Date | Event | Anchor |
|---|---|---|
| 2026-10-01 | Rent freeze effective (if no stay) | HARD |
| **~Fri 2026-10-23 [EST]** | Q3 earnings 8-K and deck. **Not yet announced as of 9/26.** The last four fell on 10/24/25, 1/30/26, 4/24/26 and 7/24/26, which suggests ~10/23. FLG desk carries ~10/27 [EST] (`AGENTS/FLG/CALENDAR.md`) | EVENT |
| ~2026-11-06 | Q3 10-Q (risk ratings, modifications, ACL roll-forward) | RULE |
| ~2026-11-14 | Q3 Call Report (SR 07-1, NDFI) | RULE |
| 2028-08 | Q2-2028 10-Q: the review carrying the first full freeze year | RULE |

**What would weaken the concern** (each checkable at the Q3/Q4-26 filings):
1. MF special mention **≤ $2,757M** at 9/30 and substandard still falling. The pipeline stalls.
2. Modifications for borrowers in difficulty in H2-26 **< $556M** (H1).
3. NYC ≥50% RR criticized pool **< $4.0B**, with par payoffs still ≥40% substandard.
4. Nonaccrual HFI back **< $2,675M** (the Q1 level) with cures > 5% of outflow.
5. The NYC RR nonaccrual cumulative-NCO ratio stays **≤ ~17%** as nonaccrual loans resolve. That would indicate the appraisals are holding.
6. Order #58 annulled or stayed (T-12).
7. TTM PPNR rising above TTM net charge-offs, so earnings rebuild the reserve.

**Would strengthen:** special mention migrating into substandard; any disclosed note sale below ~80% of par; ACL/nonaccrual below 31.04% (FLG-02); buybacks executed while coverage falls.

---

## BOTTOM LINE FOR REGINALD

1. FLG's direct CRE is concentrated in NYC rent-regulated MF: $8.5B in NYC at ≥50% RR, half of it criticized at 1.01x debt-service coverage and 78% LTV. The 2027 reset wall is $8.5B of MF at a ~3.9% coupon, and the rent freeze reaches the review cycle in Q2-2028.
2. The ACL's 8-quarter fall is mostly explained, and FLG's disclosures say so: charge-offs of already-reserved loans plus par payoffs of substandard loans (a $67M CRE release). It is not a held-for-sale transfer, and it is not a total-level reserve release.
3. The "5.8% specific reserve" understates loss recognition. NYC RR nonaccrual loans carry ~20.5% combined charge-off plus reserve (DERIVED). The 29%/31% coverage ratios mix bases and ignore write-downs already taken.
4. The live risk is forward-looking: MF special mention +33%, troubled-borrower modifications up 29× YoY, TTM PPNR ($143M) below charge-offs ($404M), and a $250M buyback. Indirect CRE via NDFI is small and unmeasurable.
5. Keep the score at 6/6 but relabel channel 2 "recognised-and-reserved legacy + live special-mention migration". The Q3 prints (~10/23 and ~11/6) test items 1–3 of §6 directly.

## Sources consulted

**Repo files:**
- `AGENTS/REGINALD/BANK_EXPOSURE_MATRIX.md` (lines 44-61, 73-151, 159-167)
- `AGENTS/REGINALD/STATUS_MATRIX.md` (lines 17-29)
- `AGENTS/FLG/STATUS.md`, `THESIS.md`, `CALENDAR.md`
- `AGENTS/FLG/workbook/{MATURITY_WALL, NONACCRUAL_FLOW, KB, TRIGGERS, PREDICTIONS, RGB_GUIDELINES, MI3_FLG}.tsv`
- `AGENTS/FLG/sources/NONACCRUAL_ROLLFORWARD_EXTRACTS_2026-08-28.md`
- `AGENTS/REGINALD/workbook/{NDFI_COHORT, ACL_ROLLFORWARD_COHORT, RUNWAY_COHORT, AOCI_COHORT_2026Q2, MI3_COHORT}.tsv`
- `AGENTS/CREED/research/2026-09-26_CRE_VULNERABILITY_MAP.md`

**SEC filings:**
- EDGAR submissions JSON, CIK0000910073: https://data.sec.gov/submissions/CIK0000910073.json
- 10-Q Q2-2026, acc 0000910073-26-000068: https://www.sec.gov/Archives/edgar/data/910073/000091007326000068/fbc-20260630.htm
- 8-K 2026-07-24, acc 0000910073-26-000065: EX-99.1 `a2q2026earningsrelease.htm`, EX-99.2 deck slides 5/12-18/20/21/25, EX-99.3 `flagstar-sharerepurchase.htm`, cover `nycb-20260724.htm`
- Q3-25 release, acc 0000910073-25-000172: https://www.sec.gov/Archives/edgar/data/910073/000091007325000172/a3q2025earningsrelease.htm
- Q4-25 release, acc 0000910073-26-000017: https://www.sec.gov/Archives/edgar/data/910073/000091007326000017/a4q2025earningsrelease.htm
- Q1-26 release, acc 0000910073-26-000035: https://www.sec.gov/Archives/edgar/data/910073/000091007326000035/a1q2026earningsrelease.htm

**Web:** search for the Q3-26 date announcement returned none; ir.flagstar.com release listings for the Q4-25/Q1-26/Q2-26 dates.
