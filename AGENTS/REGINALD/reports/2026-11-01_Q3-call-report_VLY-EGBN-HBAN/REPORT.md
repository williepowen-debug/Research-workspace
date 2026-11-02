# Q3 Call Report read: VLY and EGBN credit composition, HBAN M3 step, Friedberg test plan

**Date:** 2026-11-01, 23:16–23:5x ET (`date`). **Session:** PROME-spawned C9 research commission (WQ-587, WQ-538 class), one bounded session, $0. **Finding on record:** WALTER card SIG-W-20261031-026 and `AGENTS/WALTER/research/2026-10-31_call-report-read/REPORT.md` (34806ae91).
**Basis, every figure below unless labelled otherwise:** BANK-level FFIEC Call Report (VLY RSSD 229801, FFIEC 031; EGBN RSSD 2652092, FFIEC 041; HBAN RSSD 12311, FFIEC 031), $ thousands in the evidence file, quarter-end 3/31, 6/30 and 9/30/2026. Quarterly flows = September YTD minus June YTD. Parent (issuer release) figures are labelled PARENT.
**Retrieval:** my own pull through the FFIEC CDR REST route with the renewed token, 2026-11-02T04:18Z (23:18 ET 11/1). All nine SDFs hash-identical to WALTER's (same artifact; the arithmetic below is mine) → `retrieval.tsv`; every row used → `primary-rows.tsv`.
No trade proposal, no threshold, score, gate or prediction move. Positions are Will's; cards are TERRY's (root rule #5).

## 0. What this says

| Question | Answer |
|---|---|
| WALTER's VLY figures | **VERIFIED** at the filing: nonaccrual $462.629M → $511.390M (+10.54%); Q3 NCO $37.078M; equity +0.30%; deposits +1.96%. Q2 NCO is **$22.046M** (WALTER printed 22.045, a $1K arithmetic difference; PARENT release prints 22,046). |
| What drove VLY | Nonaccrual +$48.8M = **construction +$30.1M** (one loan, matches the release) + **loans to nondepository financial institutions (NDFI) +$18.5M** (RC-N Memo 9, from zero) − NOO CRE −$7.0M + small items. NCO up $15.0M = **multifamily +$11.1M** and **C&I +$7.1M**. |
| Did VLY's allowance keep pace | **No.** Loan allowance $590.1M → $580.3M (−$9.8M) while nonaccrual rose $48.8M: allowance ÷ nonaccrual **127.55% → 113.47%**. By RI-C category, CRE −$15.5M and construction −$4.1M (together −$19.7M), commercial +$12.8M. Q3 provision $27.3M < NCO $37.1M. |
| Release vs filing | **Matches in amount, not in label.** The release's "higher non-accrual C&I" is, on the Call Report, an $18.5M NDFI loan; the issuer's C&I line = Call Report C&I + all other loans + leases, to the dollar. |
| L521 (Q2 multifamily 30–59 cohort) | **Mostly modified, not paid.** MF 30–89 days past due fell $101.5M → $21.7M while MF performing modifications to borrowers in financial difficulty rose **$23.3M → $96.9M (+$73.5M)**; MF 90+ rose $5.5M → $10.3M; MF nonaccrual +$3.8M after $16.4M gross MF charge-offs. INFERRED from category totals, not loan-matched. New: **NOO CRE 30–89 $0 → $61.4M**. |
| EGBN | **VERIFIED**: nonaccrual $136.915M → $179.722M (+31.27%); allowance $121.141M → $120.781M; coverage 88.48% → 67.20%. Driver: **multifamily nonaccrual +$46.6M** (to 11.9% of the MF book), consistent with the Prince George's $56.0M loan moving in. Q3 NCO only $4.2M (no MF charge-off in Q3): Q2 was the charge-off quarter ($47.9M), Q3 the problem-stock quarter. |
| HBAN M3 step | **STEP-CANDIDATE** on the existing detector exactly as written: M3 (RCFD2746) $2,206.5M → $2,836.8M (+28.6%) with total loans +0.9%. A prompt to look, never a finding. NDFI (item 9.a) $17.51B → $19.94B (+13.9%). |
| Incidental instrument finding | The same detector **missed EGBN 6/30/2026**: raw M3 change −25.02% with loans −4.6%, but the script rounds to one decimal (−25.0) before testing "> 25", so the ledger cell is blank. Round-before-compare, the L546 float-tie class. Fix at the script's next touch (the 11/07 roll), not now. |
| Friedberg "20% / 95 of 4,295" | Primary statement **SEARCH-NOT-FOUND** (§4). Four candidate measures written into the 11/07 plan with one like-for-like test each; the 14-bank samples settle nothing either way. |

## 1. VLY — Valley National Bank (bank-level)

### 1a. Nonaccrual by RC-N category ($K, column C)
| Category (MDRM) | 6/30 | 9/30 | Change |
|---|---:|---:|---:|
| Construction, other + 1–4 (F177+F176) | 9,139 | 39,257 | **+30,118** |
| Multifamily (3501) | 61,550 | 65,383 | +3,833 |
| NOO CRE (F183) | 169,848 | 162,875 | −6,973 |
| OO CRE (F182) | 24,683 | 24,830 | +147 |
| 1–4 family first/junior/HELOC (C229+C230+5400) | 49,452 | 50,792 | +1,340 |
| C&I, US (1253) | 138,511 | 139,114 | +603 |
| All other loans (5461), of which NDFI (Memo 9, PV25) | 3,286 (0) | 22,803 (18,522) | **+19,517 (+18,522)** |
| Consumer + leases (K215+K218+F171) | 6,160 | 6,336 | +176 |
| **Total (1403)** | **462,629** | **511,390** | **+48,761** |

Rates: construction nonaccrual 0.41% → 1.68% of construction loans; MF 0.72%; NDFI nonaccrual 0.90% of a $2.06B NDFI book (+16.8% QoQ; private-equity fund loans $814M → $1,154M). RC-N Memo 5 shows $8.750M of nonaccrual held-for-sale loans at 9/30 (equal to the old construction nonaccrual balance; column assignment INFERRED from MDRM order, not checked against the form).

### 1b. Q3 charge-offs by RI-B category ($K)
| Category | Gross CO Q2 | Gross CO Q3 | Net Q2 | Net Q3 |
|---|---:|---:|---:|---:|
| Multifamily (3588/3589) | 5,152 | 16,439 | 5,062 | **16,159** |
| C&I (4645/4617) | 10,232 | 16,975 | 8,787 | **15,883** |
| NOO CRE (C897/C898) | 7,989 | 2,026 | 5,292 | 1,646 |
| OO CRE (C895/C896) | 1,293 | 610 | 1,290 | 570 |
| Auto, other consumer, leases, residential | 2,960 | 4,008 | 1,615 | 2,820 |
| **Total** | **27,626** | **40,058** | **22,046** | **37,078** |

PARENT release (EX-99.1, acc 0000714310-26-000045): gross $40.1M included an **$11.6M partial C&I charge-off** (with $2.0M allocated reserve) and **$9.1M of partial charge-offs on three CRE loans** ($24.7M net) that rolled 30–59 → nonaccrual with no allocated reserve. The filing places Q3 CRE charge-offs mostly in multifamily, so those three loans are INFERRED to be multifamily.

### 1c. Allowance (RI-B II item 7; RI-C Part II by category; loans held for investment)
| | 6/30 | 9/30 |
|---|---:|---:|
| Loan allowance (3123) | 590,072 | 580,272 |
| ÷ total nonaccrual | **127.55%** | **113.47%** |
| Construction ACL / construction loans | 50,623 / 2.05% | 46,490 / 1.75% |
| Construction ACL ÷ construction nonaccrual | 554% | 118% |
| CRE ACL / CRE loans | 268,445 / 0.96% | 252,903 / 0.90% |
| Commercial ACL / loans | 200,648 / 1.64% | 213,427 / 1.69% |

PARENT ratio prints 127.66% → 113.57% (parent allowance $590.6M → $580.8M). The release names the mechanism: "a decline in quantitative reserves largely within certain CRE loan categories, including construction" offset by economic-forecast, qualitative and specific reserves. The filing agrees on direction and size. Under L801 (10/30) a coverage decline is **not** a predictor on its own; it remains a question about collateral claims (the $30.1M construction loan is "well-secured", no specific reserve; its appraisal date and value are not disclosed).

### 1d. L521 checkpoint (DOCKET L521 stays the 10-Q read)
- **MF 30–59 cohort:** cured mainly by **modification** (+$73.5M MF performing modifications, RC-C Memo 1.c K160), a few rolled to nonaccrual with charge-offs, ~$4.8M moved to 90+. Modification to a borrower in financial difficulty is a deferral, not a repayment. INFERRED, category totals only.
- **CRE nonaccrual vs $256.1M:** $253.1M (MF+NOO+OO, 256,081 → 253,088; matches the release).
- **Modifications:** total performing modifications $186.4M → $242.9M; modifications in nonaccrual $86.8M → $91.2M (mostly C&I). The MF modified loan at 90+ ($5.454M at Q2) shows $4.454M at 9/30, plus a new $3.138M MF modification in nonaccrual (INFERRED identity).
- **New early stage:** NOO CRE 30–89 days past due **$0 → $61.4M**. Release: one $10.9M CRE relationship in 60–89. This is the Q4 roll candidate.
- **The Q3 10-Q (expected ~11/6–11/9; Q2 10-Q filed 8/6) must add:** (1) the modification table by class with payment-default of modified loans (the ~$108M payment-delay mods and the +$73.5M MF performing mods); (2) CRE past-due by property type, to identify the $61.4M NOO 30–89 build; (3) the $30.1M construction loan's collateral basis, appraisal date and individual evaluation; (4) the ACL roll-forward by segment, quantitative vs qualitative; (5) the $18.5M NDFI nonaccrual borrower type (issuer files it under C&I); (6) criticized/classified by class (7.3% → 7.1% of loans, PARENT).
- **REG-30** (VLY nonaccrual ≥ $511,390K at 12/31, 60%): the Q3 baseline equals the Call Report to the dollar. Both directions moved: $61.4M of new NOO 30–89 and $10.3M MF 90+ argue up; a payoff or sale of the $30.1M construction loan argues down. No probability change (that needs Will's word and this evidence does not force one).

## 2. EGBN — EagleBank (bank-level, FFIEC 041)

| Nonaccrual ($K) | 6/30 | 9/30 | Change |
|---|---:|---:|---:|
| Multifamily (3501) | 35,891 | 82,506 | **+46,615** |
| NOO CRE (F183) | 42,136 | 46,977 | +4,841 |
| Construction (F176+F177) | 18,914 | 18,483 | −431 |
| OO CRE (F182) | 5,372 | 3,501 | −1,871 |
| C&I (1608) | 15,719 | 13,807 | −1,912 |
| All other loans (5461; Q3 all NDFI) | 13,242 | 9,541 | −3,701 |
| Residential | 5,641 | 4,907 | −734 |
| **Total (1403)** | **136,915** | **179,722** | **+42,807 (+31.27%)** |

- **Allowance:** $121,141K → $120,781K (−0.3%); ÷ nonaccrual **88.48% → 67.20%** (VERIFIED). CRE ACL (RI-C 1b) $79.3M → $78.8M while CRE loans fell 5.8%, so CRE ACL/loans rose 2.10% → 2.22%, but CRE ACL ÷ CRE nonaccrual fell 95% → 59%. Q3 provision $2.9M.
- **Two clocks:** Q2 net charge-offs $47.9M (gross MF $11.1M, NOO $25.4M); Q3 $4.2M (NOO $2.9M, an NDFI/all-other $3.5M; **zero MF charge-off in Q3**). The Q3 MF nonaccrual jump arrived without a charge-off.
- **Prince George's $56.0M (DOCKET L791; RED owns the bank tree):** consistent with the filing, not identity-proven (no borrower named). MF nonaccrual +$46.6M net, and MF modifications in nonaccrual (RC-N Memo 1.c K113) $16.3M → $67.5M (+$51.2M), which fits a loan extended to 12/21/2026 and placed on nonaccrual. On the deck's 3/9/2026 $63.7M appraisal (LTV 88%), a 13–22% realized discount (my 10/22 appraisal test) gives $49.7M–$55.4M of collateral vs $56.0M, i.e. $0.6M–$6.3M of loss before costs: a sensitivity holding the appraisal and balance fixed, not a forecast.
- **Basis gap, UNRESOLVED:** PARENT nonaccrual (deck) $111.1M → $166.0M vs Call Report $136.9M → $179.7M (gaps $25.8M and $13.7M). Not reconciled here; RC-N Memo 5 (held for sale) reports nothing.
- **REG-28 lead (CREED 10/28):** EGBN's Q2 30–89 bucket was NOO CRE (F179 $42,704K → $0 at 9/30), not multifamily. L02 is "DC apartments $42.685M" (multifamily), so the near-equal amount sits in a different Call Report category: weak evidence **against** that identity. The REG-28 tally stays h=0 x=0 u=4.

## 3. HBAN M3 — existing step detector, applied as written

Rule (`scripts/mi3_cohort_screen.py`, Will-approved 2026-08-13): STEP-CANDIDATE if |QoQ M3| > 25% and |QoQ total loans| < 5%, M3 = RCON2746 else RCFD2746, loans = RCON2122 else RCFD2122.

| HBAN | 3/31 | 6/30 | 9/30 |
|---|---:|---:|---:|
| M3, RCFD2746 ($K) | 2,262,570 | 2,206,543 | 2,836,768 |
| QoQ M3 | +32.1% (loans +26.0%, acquisition quarter) | −2.5% | **+28.6%** |
| QoQ total loans (RCON2122) | — | +0.8% | **+0.9%** |
| Flag | none | none | **STEP-CANDIDATE** |
| NDFI 9.a (J454) | 16,368,218 | 17,511,739 | 19,938,764 (+13.9%) |

**Result: STEP-CANDIDATE, the first for HBAN in the ledger series.** It is a prompt to check whether the step is a re-designation or new lending; the Call Report cannot tell. Next look (existing work, 11/07 cohort run): HBAN Q3 10-Q C&I/CRE narrative and whether item 9.a and M3 grew together. M3 sits inside C&I/other loans: never add it to NDFI or secured CRE. No v1/v1a ratio or rank is cited (DO-NOT-CITE until the 11/07 rerun). VLY (−3.2%, loans +1.4%) and EGBN (+14.2%, loans −1.4%) do not flag at Q3.

**Funded + unfunded check (method from the FLG desk's packet, 11/01, commit e9f170314):** HBAN unfunded commitments for CRE/construction/land finance not secured by real estate (RC-L 1.c.(2), RCFD6550) rose too, $1,367,955K → $1,586,821K, so funded + unfunded went $3,574,498K → $4,423,589K (**+23.7%**). At FLG the unfunded line FELL (funded + unfunded +12.1% against funded +54%). A rise on both lines with no offsetting RC-C decline points to new commitments, not a relabel: INFERRED, not established. HBAN NDFI Memo 10 also grew across types (private-equity funds $4.13B → $4.87B, +18.0%; business credit intermediaries +14.2%); C&I (1763+1764) +2.3%. **FLG (FLG desk, not re-read here):** its M3 +54.12% is also a STEP-CANDIDATE on this rule; FLG attributes the NDFI step to Funds/Lender Finance lending and reports no reclassification signature; its total-loans rise for two quarters is a mix shift (multifamily −3.56%), not an end to the run-off.

**Incidental: the detector missed EGBN at 6/30/2026.** 152,732 / 203,695 − 1 = **−25.02%**, loans −4.6%. The script rounds to one decimal before comparing (`mi3_qoq_pct = round(..., 1)` then `abs(m) > 25.0`), so −25.0 fails the test and the published `MI3_COHORT.tsv` cell is blank. Under the rule's wording it is a STEP-CANDIDATE. Same class as the deferred L546 float-tie (`kre_float.py`, `si_refresh.py`). Repair (compare raw, round only for display) at the 11/07 roll, with a boundary fixture; not changed this session.

## 4. Friedberg claim — what it measures, and the 11/07 like-for-like test

**Primary statement: SEARCH-NOT-FOUND.** Checked: three web searches (claim figures; "Friedberg" + banks + 4,295; David Friedberg / All-In) found nothing; repo history first shows the claim 2026-10-13 as a quotation supplied in conversation, never committed (my 10/13 screen treated it as an additional-rate-loss claim and marked it unauthenticated). Not upgraded to absence: the original link is with Will or PROME.
**Population clue (INFERRED):** 4,295 is the size of the FDIC-insured Call Report population (BankingLENS: 4,296 filers at Q2 before excluding 58 trusts; FDIC API 4,313 June rows per WALTER). 95 is 2.2% of it.

| Candidate measure | Numerator | Denominator | Like-for-like test at the universe |
|---|---|---|---|
| A. Existing unrealized loss | (AFS cost 1772 − FV 1773) + (HTM cost 1754 − FV 1771), pretax and at 21% tax | GAAP bank equity (RC 27.a, 3210); repeat on tangible (3210 − goodwill − other intangibles) | Count banks ≥ 20% on each denominator, 6/30 and 9/30 |
| B. Additional loss from an assumed rate shock | modified duration × shock × securities FV; duration from RC-B maturity/repricing buckets (bucket-midpoint proxy), shock stated | same as A | Count ≥ 20% at the shock that best matches the claim's wording; report the shock |
| C. Actual quarterly equity decline | 3210 Q3 − 3210 Q2, split by the RI-A bridge into OCI, distributions, treasury stock, income | 3210 Q2 | Count declines ≥ 20% (WALTER's 14-bank maximum is AMTB −8.83%) |
| D. Capital-basis claim | A or B | CET1 (RC-R) | Report separately: opt-out banks exclude AOCI from CET1, so an equity hit is not a capital hit |

Common rules: the same definition for every bank; both tax bases shown; AOCI opt-out election read from RC-R per bank before any capital wording; fair-value hedges on securities are not visible in Call Report securities lines, so counts overstate for hedged banks: hedges are checked in the 10-Q only for banks a measure flags. **Identification test:** the measure whose count and population reproduce 95 and 4,295 (same quarter) is what the claim measured; report all four counts, whichever matches.
**Why the 14-bank work cannot settle it:** the cohort was chosen for CRE/credit exposure and size, not at random. At a 2.2% base rate a random 14 would show zero hits 73% of the time ((1 − 0.0221)^14), so WALTER's "no bank lost 20%" and my 10/13 "no 20% case" are uninformative about 95-of-4,295 in either direction.
**Data dependency:** the universe needs the FFIEC bulk Call Report file or the FDIC financials API for 9/30/2026 (FDIC returned 0 September rows at WALTER's check, 10/31). If neither is complete on 11/07, the pass records UNKNOWN with the missing count and runs when it posts. No full-universe run tonight (brief).

## 5. Thesis meaning for the held lines (context only; TERRY constructs, Will approves)
- **VLY (Dec-18 $12P on the book):** the bank-specific early flag (L521) holds and is not escalated: problem loans up 10.5%, reserves released, the MF cohort resolved mainly by modification rather than cash, and a new $61.4M NOO 30–89 bucket. Realized loss is still small (Q3 NCO 0.28% annualized, PARENT). The 10-Q decides whether modifications are performing.
- **ZION, OZK, WAL, KRE:** not re-verified here (WALTER's helper checked OZK/WAL; ZION was parent-checked only). Nothing here changes the live claim: severity is concentrated, not tier-wide. VLY and EGBN add problem-loan stock; HBAN is a classification question, not a loss.
- **FLG:** read by the FLG desk in parallel; not duplicated.

## 6. Limits and confidence
VERIFIED: every VLY/EGBN/HBAN Call Report figure above (my own pull and arithmetic). INFERRED: the MF cure-by-modification reading, the three-CRE-loans-are-MF reading, the Prince George's tie, the HFS column assignment, the Friedberg population. UNKNOWN: EGBN parent-vs-bank nonaccrual gap; collateral values; the HBAN step's cause; the Friedberg primary. Not an independent audit of WALTER's other eleven banks.
