> ⚠️ **AGENT WORKING NOTES, verbatim** (Opus research agent commissioned by CREED 2026-09-30 night, Will: "do steps 1 and 2"). NOT CREED-verified except the items marked VERIFIED in `research/2026-10-01_LOSS_HOLDER_MAP.md`. Cite the synthesis, not this file.

# Holder map B: Ashford Hospitality Trust (AHT) KEYS pools + Safehold (SAFE) 135 W 50th St
Research subagent for CREED, 2026-09-30 (UTC clock read 2026-10-01 03:46). READ-ONLY on repo. Property -> loss-holder map; NOT a trade recommendation. No share prices quoted.
Tiers: **PRIMARY-READ** = I read the primary document (SEC filing) myself · **SECONDARY** = rating agency / press article I opened · **SNIPPET** = only seen through a search-engine summary, article not opened (lowest tier; do not cite without re-reading) · **DERIVED** = my arithmetic on the cited inputs · **ANALYTICAL** = structural reasoning, no source.

## 0. Bottom line (per name)
| Name | Does the ledger event hurt the tradeable company? | Who actually bore / bears the loss | Materiality verdict |
|---|---|---|---|
| **AHT** (KEYS Pools A, B, F) | **No — these were accounting GAINS for AHT** ($53.4M FY23 Pool F; $167.2M FY24 + $39.1M FY25 on A/B). The hotels' book value was below the non-recourse debt, so handing them back removed negative book equity. The remaining receivership liabilities ($273,971k debt + $94,327k accrued interest at 6/30/26) are **exactly offset** by a $368,298k contract asset. | **CMBS trust Ashford Hospitality Trust 2018-KEYS** (certificateholders) for Pool A/B mortgage shortfalls, **after** the mezzanine lenders (outside the trust, unidentified) are wiped. Pool F mortgage was **paid off to the trust** in the Nov-2023 remittance (DBRS) -> the Pool F loss sat with whoever bought/held the mortgage and the Pool F mezz ($48.52M), identity NOT established. | KEYS itself: **immaterial to AHT's capital now** (net-zero BS block). But AHT is **severely capital-stressed for other reasons**: total equity **deficit $(556.5)M**, going-concern "substantial doubt", preferred dividends suspended, JPM8 $325M loan default notice (6/30/26 10-Q). KEYS is the **template** for what AHT is doing with other pools, not the cause of the stress. |
| **SAFE** (135 W 50th, ground lessor) | **Not yet a realized loss; exposure is real and concentrated.** SAFE's #2 asset (5.0% of gross book value, 6/30/26). Tenant defaulted on a property-tax forbearance; SAFE made an **$8.3M protective tax advance** (Q1-26 10-Q), sent termination notice 5/11/26, and is **stayed by a TRO** (6/4/26). | The 2024 $8.5M price was a **leasehold** sale by the **leasehold owner UBS Realty Investors** (SNIPPET) -> that equity loss sat with UBS Realty's investors, not with SAFE and not (per anything I read) with a lender. SAFE sits senior to the leasehold, but **property-tax liens sit senior to SAFE's fee** (ANALYTICAL), which is why SAFE is advancing taxes. | **Protected in structure, not immaterial in size.** Bracket of basis ~$285M–~$434M (DERIVED, mixed bases) = **~12%–18% of SAFE shareholders' equity ($2,439.1M)**; ground rent ~$9.6M/yr (SNIPPET) = ~2% of annualized revenue. Principal loss requires the land + reverted building to be worth less than SAFE's basis — **not established either way.** |

---
## 1. Ashford KEYS pools — loan stack, lender, history, AHT accounting

### 1a. Loan stack at origination (2018-06-13) — the "$215.1M mortgage" is the WHOLE stack, not the mortgage
| Pool | Hotels | Mortgage (in CMBS trust) | Mezzanine (OUTSIDE trust) | Total = AHT's reported "mortgage loan" | Spread | Source |
|---|---|---|---|---|---|---|
| A | 7 | $144,400,000 | $36,320,000 | **$180,720,000** | L+3.67% wtd (later SOFR+3.70%) | AHT 8-K 2018-06-18 Item 2.03, PRIMARY-READ |
| B | 7 | $149,400,000 | $25,000,000 | **$174,400,000** | L+3.41% (later SOFR+3.44%) | same |
| F | 5 (W Atlanta Downtown, ES Flagstaff, ES Walnut Creek, Marriott Bridgewater, Marriott RTP Durham) | $166,600,000 | Sr $21,630,000 + Jr $26,890,000 | **$215,120,000** | L+3.70% (later SOFR+3.73%) | same |
| A+B+F | 19 | $460.40M | $109.84M | $570.24M (DERIVED sum) | | |
- Lenders at origination: Bank of America N.A., Barclays Bank PLC, Morgan Stanley Bank N.A. (mortgage); mezz lenders BofA, Barclays, Morgan Stanley Mortgage Capital Holdings LLC (8-K 2018-06-18 exhibit list, PRIMARY-READ). Nonrecourse, carve-outs guaranteed by Ashford Hospitality LP.
- **CMBS trust: "Ashford Hospitality Trust 2018-KEYS"** (issuing entity CIK 0001740287; depositor Morgan Stanley Capital I Inc.). EY AUP (ABS-15G EX-99.1, 2018-06-15, PRIMARY-READ): trust assets = "six floating rate whole mortgage loans" on 34 hotels; "Each Mortgage Loan has a related ... senior mezzanine loan and, in certain cases, a related ... junior mezzanine loan ... that will **not be assets of the Issuing Entity**." 144A deal: no 10-D remittance reports on EDGAR, so loan-level realized losses are not public on EDGAR.
- AHT 2023-12-04 EX-99.1 (PRIMARY-READ): "The original lenders previously transferred the loans to a securitization trust. Such trust, acting through its servicer, brought suit seeking the appointment of a receiver" (re A/B); BofA/MS/Barclays "are not party to the litigation." Special servicer NAME not found in anything I read.
- Senior total at issue (DBRS, SECONDARY): mortgage $982.0M + mezz $288.2M across all six pools; all loans to special servicing April 2023.

### 1b. Event history per pool (PRIMARY-READ unless marked)
| Date | Pool | Event | Source |
|---|---|---|---|
| 2023-06-09 | A, B | "effective June 9, 2023, this mortgage loan was in default" (extension paydown not made) | FY2023 10-K debt fns (6),(7) |
| 2023-06-09 | F | 30-day extension to negotiate | FY2023 10-K note 5 |
| 2023-07-07 | A, B, F | AHT "elected not to make the required paydowns ... thereby defaulting"; "most likely outcome will be a consensual transfer" | 8-K 2023-07-07 |
| 2023-11-29 **or** 11-30 | F | Deed in lieu to "the current holder of the mortgage loan". **AHT's own filings carry both dates**: Nov 29 (FY2023 10-K note 5; FY2025 10-K R16); Nov 30 (8-K 2023-12-04; FY2023 10-K debt fn (8)) | as listed |
| Nov-2023 remittance | F | "the payoff of one formerly specially serviced loan, Pool F" — trust received payoff | DBRS 2024-09-23, SECONDARY |
| Dec-2023 | F (W Atlanta Downtown) | Stonebridge Hospitality acquired via DIL for **$24.8M** (AHT paid $56.75M in 2015) | Connect CRE, SECONDARY |
| 2024-03-01 | A, B | AHT notified hotels transferred to court-appointed receiver | Q1-24 10-Q; FY2025 10-K R16 |
| 2024-07-02 | B (CY Plano Legacy Park, RI Plano) | Foreclosed at public auction | FY2025 10-K R16 |
| Aug-2024 | A/B | "A DIL was accepted on 10 other properties in August 2024" | DBRS 2024-09-23, SECONDARY — **UNRECONCILED**: AHT filings mention no August 2024 DIL; AHT says liabilities remain "until final resolution" |
| 2024-11-04 | A (CY Columbus Tipton Lakes) | Receiver transferred to third party | R16 |
| 2025-06-25 | B (CY Oakland Airport) | Receiver transferred to third party; price **$12.5M** (156 keys) | R16; price SNIPPET (Hotel Investment Today, 403 on fetch) |
| 2025-12-22 | B (SHS BWI Airport) | Receiver transferred to third party | R16 |
| 2026-03-04 | A (SHS Plymouth Meeting) | Receiver transferred to third party; price not disclosed | R16; Q2-26 10-Q |
| **2026-07-16** | B (CY Newark Silicon Valley) + A (RI San Jose Newark) | Receiver transferred to third parties — **NEW, post-workbook**; prices **$12.0M** (181 rooms) and **$8.0M** (168 rooms), buyer Capital Insight (Cobby Pourtavosi); Jan-2026 assessed $24.1M / $23.8M | Q2-26 10-Q (event, PRIMARY-READ); prices Hotel-Online 2026-07-22, SECONDARY |
| **2026-08-06** | B (TPS Manhattan Beach) + A (SHS Manhattan Beach) | Receiver transferred to third parties — **NEW, post-workbook**; prices not found | Q2-26 10-Q (subsequent event) |
| Remaining per AHT filings (DERIVED from lists) | A: CY Old Town Scottsdale, RI Hughes Center Las Vegas, RI Phoenix Airport; B: CY Basking Ridge | not yet disposed per 6/30/26 10-Q | DERIVED |

2018 "as is" appraisals (EY AUP, subset only, PRIMARY-READ; pool-number mapping inferred from property lists): SHS Plymouth Meeting $26.0M; RI Las Vegas $47.7M; CY Plano $22.7M; RI Plano $17.7M; ES Walnut Creek $62.4M; Marriott Bridgewater $89.0M; Marriott RTP $33.5M.

### 1c. What AHT recorded (PRIMARY-READ)
| Item | Amount | Period | Source |
|---|---|---|---|
| Pool F gain on extinguishment of debt | **+$53.4M** | FY2023 | FY2023 10-K note 5 + MD&A |
| Pool F debt vs book value of collateral | $215,120k vs $164,792k (book equity ≈ −$50.3M DERIVED) | 12/31/22 | FY2023 10-K debt table |
| Pool A / B debt vs book collateral | A $180,720k vs $121,119k; B $174,400k vs $113,110k (combined book equity ≈ −$120.9M DERIVED) | 12/31/23 | FY2023 10-K debt table |
| Impairments | "no impairment charges were recorded" 2021–2023 | FY21–23 | FY2023 10-K note 5 |
| A/B derecognition gain | **+$133.9M** | Q1-2024 | Q1-24 10-Q; R16 |
| Contract asset recorded | $378.2M ($378,160k) | 3/31/24 | Q1-24 10-Q |
| Further derecognition gains (accrued interest) | +$33.3M (FY24 total $167.2M); +$39.1M FY25; +$14.6M 6M-26 (receivership pool now also includes Hilton Santa Cruz Scotts Valley) | as stated | R16; Q2-26 10-Q |
| Contract asset & receivership debt/interest reduced on dispositions | −$45.0M (as of 12/31/24); −$50.6M (as of 12/31/25) | | R16 |
| Debt assoc. w/ hotels in receivership | $355,120k (3/31/24) -> $314,640k (12/31/24) -> $272,800k (12/31/25) -> $273,971k (6/30/26, **includes Santa Cruz**; KEYS-only ≈ **$252.0M** DERIVED = 273,971 − 21,971 Santa Cruz carrying value at 12/31/25) | | Q1-24 10-Q; FY25 10-K; Q2-26 10-Q |
| Net receivership block | debt $273,971k + accrued interest $94,327k = contract asset $368,298k (exact) | 6/30/26 | Q2-26 10-Q (DERIVED check) |
| Cumulative KEYS-related gains booked | ≈ **+$259.7M** FY23–FY25 (DERIVED sum 53.4+167.2+39.1) | | |

### 1d. Who bore what — the loss-holder map
| Pool | Equity holder (AHT) lost | Mezz lenders (outside trust) | CMBS trust AHT 2018-KEYS | Status |
|---|---|---|---|---|
| F | Its equity in 5 hotels — **negative on book**, so AHT booked a +$53.4M gain. Economic equity lost = market value of hotels minus $215.1M, not disclosed. AHT had taken cash out at the 2018 refi (DBRS: $163.4M cash-equity distribution across all six pools, SNIPPET-level via search summary of DBRS). | Pool F mezz $48.52M original is first-loss behind the mortgage. **Holder(s) NOT identified.** | **No loss reported** — Pool F "payoff ... with the November 2023 remittance" (DBRS). The DIL went to "the current holder of the mortgage loan" (AHT) — i.e., someone held the mortgage outside the trust by then. **Inference, NOT established:** a mezz lender may have bought the mortgage; I found no source naming the buyer. | Resolved for trust; final loss to mezz/mortgage buyer **unknown** |
| A | Same mechanism; gains, not losses | $36.32M mezz first-loss (holders unknown) | Bears mortgage ($144.4M orig) shortfall. DBRS 9/2024 liquidation scenario: severity >30% | Partially liquidated; 3 hotels left |
| B | Same | $25.0M mezz first-loss (holders unknown) | Bears mortgage ($149.4M orig) shortfall. DBRS 9/2024: severity >70% | Partially liquidated; 1 hotel left |
| A+B | | | DBRS 9/2024: "total implied liquidated loss amount, all from Pools A and B, is in excess of $150 million" — a **projection, not a realized loss**; basis (whole-loan vs trust) not stated in the fetched text. Class E downgraded to BB(sf) 9/2024; Class F to CCC(sf) 9/2023 (certificate classes, NOT pools). | **Realized trust losses: not reached** (144A, no EDGAR 10-D; Trepp/KBRA loan-level data not accessed) |

Sale-price read-through (SECONDARY/SNIPPET, partial): known receiver/DIL prices = W Atlanta $24.8M, CY Oakland $12.5M, CY Newark SV $12.0M, RI Newark $8.0M. Too few to estimate pool recovery; do not sum against pool balances (allocated loan amounts per hotel not obtained).

### 1e. Reconciliation to Will's workbook rows
| Workbook field | Workbook value | Primary finding | Verdict |
|---|---|---|---|
| EVT-0079-01 date | 2023-11-29 | Nov 29 (10-K note 5, FY25 R16) **and** Nov 30 (8-K 12/4/23; FY23 10-K debt fn 8) | **MATCH**, with caveat: AHT's own filings disagree by one day |
| CRE-0079 / LN-0079 loan balance | $215.1M "Pool F mortgage" | $215,120,000 = mortgage **$166.6M** + sr mezz $21.63M + jr mezz $26.89M | **MATCH on figure; DIFFERENT on label** — it is the full debt stack; the CMBS trust only held $166.6M |
| LN-0079 "Lender recovery and remaining recourse" | open | Trust: Pool F paid off Nov-2023 remittance (DBRS). Remaining recourse: loans nonrecourse w/ carve-outs (8-K 2018) | NEW info — trust shows no Pool F loss |
| LN-0080 timeline "July 2023 default" | July 2023 | Default effective **June 9, 2023** (FY23 10-K fns 6,7); election not to pay down announced July 7, 2023 | **DIFFERENT** (both dates are AHT's; "default" date = June 9) |
| EVT-0080/0081 receiver | 2024-03-01 | 2024-03-01 notice | MATCH |
| Columbus Tipton Lakes sale | 2024-11-04 | 2024-11-04 | MATCH |
| Plymouth Meeting (EVT-0094-01) | 2026-03-04, price undisclosed | 2026-03-04; no price in AHT filings | MATCH |
| Plano pair foreclosure | 2024-07-02 | 2024-07-02 | MATCH |
| Oakland sale | 2025-06-25 | 2025-06-25; price $12.5M (SNIPPET) | MATCH (+price, low tier) |
| BWI sale | 2025-12-22 | 2025-12-22 | MATCH |
| CRE-0080/0081 hotel lists | 7 + 7 named | Identical to 8-K 2023-07-07 Exhibit A and R16 | MATCH |
| Pool A/B "remaining unresolved" | as of 2026-03-04 / 2025-12-22 | **Stale**: 4 more receiver sales 2026-07-16 and 2026-08-06 (Q2-26 10-Q) | **DIFFERENT — workbook superseded** |
| Lender identity | not stated | CMBS trust AHT 2018-KEYS (mortgage) + mezz lenders outside trust | NEW |

---
## 2. Ashford materiality (PRIMARY-READ, Q2-2026 10-Q, acc 0001232582-26-000183, filed 2026-08-12, balance sheet date 2026-06-30)
| Metric | Value |
|---|---|
| Total equity (deficit) | **$(556,538)k**; stockholders' deficit of the Company $(570,885)k (12/31/25: $(610,841)k / $(626,352)k) |
| Indebtedness, net | $1,905,747k |
| Debt associated with hotels in receivership | $273,971k (+ accrued interest $94,327k) |
| Debt incl. receivership | ≈ $2,179.7M (DERIVED; excludes $74,813k liabilities held for sale, not split) |
| Cash & equivalents | $72,510k on BS ($75.0M incl. held for sale per going-concern note); restricted cash $136,985k |
| Total assets / liabilities | $2,334,450k / $2,643,964k |
| Preferred (redeemable J/K/L/M on BS mezzanine) | $187,498k + $18,972k + $5,658k + $14,096k |
| Common shares outstanding | 6,476,491 |

Capital-structure stress (PRIMARY-READ):
| Item | Detail | Source |
|---|---|---|
| Going concern | "substantial doubt about the Company's ability to continue as a going concern within one year"; $945.2M of non-recourse loans maturing within one year; possible Ashford LLC advisory-agreement termination fee if Annualized Portfolio Cash Flow < $65M | Q2-26 10-Q note 2 |
| Preferred dividends | Suspended 2026-01-13 "to preserve the Company's liquidity position as it evaluates strategic alternatives" (incl. already-declared 12/31/25 dividends); arrears e.g. Series J $7,685k, D $1,174k | Q2-26 10-Q note 11 |
| JPM8 default | Notice of default and acceleration 2026-02-11 on $325M loan, 8 hotels; "does not trigger any cross-defaults"; "no indebtedness at the parent-company level" | Q2-26 10-Q |
| Other defaults | Hilton Santa Cruz Scotts Valley $22.0M matured unpaid 2025-03-06; to receiver 2026-06-01 | Q2-26 10-Q |
| Reverse split | 1-for-10, effective close 2024-10-25 | 8-K 2024-10-15 |
| NYSE notice | <$1.00 average close, notice 2024-09-23 | 8-K 2024-09-23 |
| Rights plan | Adopted 2025-12-15 to protect tax benefits | Q2-26 10-Q |
| Asset sales 2026 | Many Item 2.01 8-Ks, e.g. Marriott Fremont $53.0M (7/1/26), Hyatt Regency Long Island $26.5M (7/31/26), ES Dulles $22.8M (8/24/26) | 8-Ks as dated |

Scale of KEYS vs AHT (DERIVED):
| Comparison | Figure |
|---|---|
| A+B+F original stack $570.24M vs AHT total indebtedness 12/31/22 $3,835.3M | **14.9%** of AHT debt at the time |
| Remaining KEYS A/B receivership debt ≈ $252.0M vs debt incl. receivership $2,179.7M | **≈11.6%** |
| Net effect of the remaining KEYS block on AHT equity | **≈ 0** (contract asset = receivership debt + accrued interest) |
| KEYS cumulative GAAP effect on equity FY23–FY25 | **+$259.7M** (gains) — KEYS *improved* reported equity |
=> **Verdict:** KEYS does not threaten AHT's capital; AHT's deficit and going-concern status are driven by the rest of its debt stack ($945.2M within one year, JPM8 default). For AHT's own securities, the relevant read is that pool-by-pool keys-back (KEYS F/A/B, Santa Cruz, now JPM8 in default) is the company's operating mode.

---
## 3. Safehold at 135 West 50th Street
### 3a. What happened
| Date | Event | Tier / source |
|---|---|---|
| 2006 / 2012 | UBS bought the ground lease for $332.5M (2006) and the fee for $279M (2012) | SNIPPET (PincusCo via search summary) |
| 2019-12-12 | Safehold closes $285M ground lease under the 929k SF office building (building "undergoing capital improvements"); lease expiry 2123 (SAFE top-10 tables) | Safehold press release (company IR, read through a fetch summarizer); expiry PRIMARY-READ |
| 12/31/2019 | 10.9% of SAFE gross book value; flagged as "under development or in transition" | old SAFE FY2019 10-K (CIK 1688852), PRIMARY-READ |
| 2024-07-31 (auction) / 2024-10-08 closing | Leasehold sold by **UBS Realty Investors** (135 West 50th Street Lessee LLC) to **TD 135 West 50 LLC (Thakkar Developers)** for **$8.5M**; ground rent $800k/month ($9.6M/yr) | SNIPPET (PincusCo); auction/price also NY Post per workbook (nypost.com blocked for fetch). Workbook "closing not independently verified" -> closing date now has a SNIPPET-tier source |
| Q3-2024 10-Q | SAFE mentions 135 W 50th only in the top-10 table (4.8%); **no disclosure of the auction found** | PRIMARY-READ |
| by 12/31/2025 | SAFE "entered into a forbearance agreement with a tenant under a significant New York office asset" | FY2025 10-K (filed 2026-02-12), PRIMARY-READ |
| by 3/31/2026 | "The tenant defaulted on such agreement and we made a **$8.3 million protective tax advance**" | Q1-26 10-Q (filed 2026-05-01), PRIMARY-READ |
| 2026-05-11 | Termination notice; SAFE sues: *135 West 50th Street Ground Owner LLC v. TD 135 West 50 LLC*, NY Sup Ct Index No. 652773/2026 (declaration of termination, ejectment, damages) | Q2-26 10-Q note 11, PRIMARY-READ |
| 2026-05-20 | Tenant sues: *TD 135 West 50 LLC v. 135 West 50th Street Ground Owner LLC*, Index No. 156448/2026 (notice "not a viable predicate"; implied-covenant damages) | same |
| 2026-06-04 | TRO stays SAFE from acting on the termination notice or pursuing ejectment pending the tenant's PI motion | same |
| 2026-06-12 | SAFE moves in App. Div. 1st Dept to modify the TRO; tenant answers denying relief. Both motions **pending** as of the 10-Q (filed 2026-07-31) | same |
| May 2026 | Suit alleges "nearly $28 million in unpaid property taxes, interest and other penalties" | SNIPPET (The Real Deal 2026-05-22, not opened) |
| after 2026-07-31 | **Court outcome NOT found** (no SAFE 8-K on it through 2026-09-11 filing list; EDGAR full text Aug–Sep 2026: no SAFE hit) | — |

### 3b. Is SAFE's position impaired or protected?
| Question | Finding |
|---|---|
| Is SAFE a lender here? | **No.** SAFE owns the land (fee) and is the ground landlord; tenant = TD 135 West 50 LLC (Q2-26 10-Q). |
| Seniority | Ground lease is senior to the leasehold interest and any leasehold mortgage (ANALYTICAL; SAFE describes "a Ground Lease's senior position in the commercial real estate capital structure", Q2-26 10-Q). **But unpaid property taxes are a lien senior to the fee** (ANALYTICAL) — consistent with SAFE's $8.3M protective advance (PRIMARY-READ). |
| Leasehold lender? | None identified in any source read. |
| Impairment / specific allowance disclosed? | **None found.** SAFE's total allowance on sales-type leases $11,138k and on GL receivables $5,134k (6/30/26) are portfolio-level; Q2-26 provisions attributed to portfolio growth and macro forecast. I did **not** establish whether 135 W 50th is booked as an operating lease, sales-type lease or GL receivable. |
| SAFE's stated position | "lease has been duly terminated"; "no assurances that it will prevail"; "may suffer losses and incur substantial costs in protecting our investment" (Q2-26 10-Q) |
| Concentration statement | "did not have a significant concentration of interest income ... from any tenant" (Q2-26 10-Q) |

### 3c. Size vs SAFE (6/30/26 unless noted)
| Measure | Value | Tier |
|---|---|---|
| Share of SAFE gross book value | **5.0%** (#2 of top 10; 4.6% 12/31/25; 4.8% 9/30/24; 5.2% 12/31/22; 10.9% 12/31/19) | PRIMARY-READ |
| SAFE basis, low end | $285M (2019 price) | company PR / SECONDARY |
| SAFE basis, high end | ≈ $434M = 5.0% × implied GBV ≈ $8.67B (52% × CPV $16,676M) | DERIVED, rounded inputs; GBV $ not stated in filings read. On the Ground Lease Cost basis ($6,906M, a different perimeter) 5% = $345M |
| vs SAFE shareholders' equity $2,439,146k | ≈ **11.7% – 17.8%** | DERIVED |
| vs SAFE total assets $7,520,024k | ≈ 3.8% – 5.8% | DERIVED |
| Annual ground rent | $9.6M (SNIPPET) ≈ 2.1% of annualized 6M-26 revenue ($225.5M × 2) and ≈ 8% of annualized 6M-26 net income ($59.6M × 2) | DERIVED on SNIPPET input |
| Cash already out | $8.3M protective tax advance ≈ 0.34% of SAFE equity | PRIMARY-READ / DERIVED |
| Alleged tax/penalty arrears | ~$28M | SNIPPET |
=> **Verdict:** Protected by structure (no loan principal at risk; termination would hand SAFE the building), **but not immaterial by size**: a single asset worth roughly an eighth to a sixth of SAFE's equity, with rent stopped or at risk, taxes being advanced, and a court stay in place. Whether there is any *principal* loss turns on the value of land + reverted building (reported ~35% occupancy in 2024 per workbook/NY Post; 866k–929k SF) versus SAFE's basis — **not established.**

---
## 4. What this does and does not establish
**Does establish**
1. AHT's KEYS hand-backs produced GAAP **gains** for AHT (+$53.4M, +$167.2M, +$39.1M); they did not consume AHT capital, and the remaining receivership block nets to zero on AHT's balance sheet.
2. The workbook's "$215.1M Pool F mortgage" is the **whole debt stack**; the CMBS trust held only $166.6M of it; $48.52M was mezz outside the trust.
3. The mortgage-side loss-holder for Pools A/B is the CMBS trust **Ashford Hospitality Trust 2018-KEYS**, behind wiped-first mezz; Pool F's mortgage was paid off to the trust (DBRS).
4. AHT is in going-concern doubt with a $(556.5)M equity deficit, suspended preferred dividends and a $325M loan in default — independent of KEYS.
5. SAFE is the ground landlord at 135 W 50th, has advanced $8.3M of property taxes, is litigating termination under a TRO, and the asset is 5.0% of its gross book value.
6. The 2024 $8.5M price was a leasehold sale by the leasehold owner (UBS Realty Investors) — not a SAFE loss and not a lender foreclosure (SNIPPET tier for the seller identity).

**Does NOT establish**
1. Any **realized** loss to AHT 2018-KEYS certificateholders (DBRS figures are projections; no remittance data reached).
2. Who held the Pool A/B/F **mezzanine** loans or who bought the Pool F mortgage out of the trust; whether they took a loss.
3. Allocated loan amounts per hotel, so no per-hotel recovery rate can be computed from the four known sale prices.
4. Reconciliation of DBRS's "DIL accepted on 10 properties in August 2024" with AHT's filings (which report receiver transfers and liabilities outstanding "until final resolution").
5. The outcome of the 135 W 50th litigation after 2026-07-31; whether SAFE has impaired or reserved specifically against the asset; its accounting classification.
6. SAFE's exact dollar basis in 135 W 50th (the range above mixes a 2019 price with a derived GBV share — do not quote as one number).
7. Anything about stock prices or trade merit (out of scope; Will/TERRY).

---
## 5. Sources opened (all fetched 2026-09-30/10-01 UTC)
| # | Source | URL | Date | Tier | Shapes read |
|---|---|---|---|---|---|
| 1 | AHT FY2025 10-K debt note R16 | https://www.sec.gov/Archives/edgar/data/1232582/000123258226000067/R16.htm | filed 2026-03-23 | PRIMARY-READ | footnote prose + debt table |
| 2 | AHT FY2025 10-K | https://www.sec.gov/Archives/edgar/data/1232582/000123258226000067/aht-20251231.htm | 2026-03-23 | PRIMARY-READ | balance sheet |
| 3 | AHT Q2-2026 10-Q | https://www.sec.gov/Archives/edgar/data/1232582/000123258226000183/aht-20260630.htm | 2026-08-12 | PRIMARY-READ | BS, IS, going-concern note, debt note, equity note |
| 4 | AHT Q1-2024 10-Q | https://www.sec.gov/Archives/edgar/data/1232582/000123258224000068/aht-20240331.htm | 2024-05-09 | PRIMARY-READ | BS, dispositions note, MD&A |
| 5 | AHT Q2-2024 10-Q (workbook source 2) | https://www.sec.gov/Archives/edgar/data/1232582/000123258224000107/aht-20240630.htm | 2024-08-08 | fetched, not mined (superseded by #1–#4) | — |
| 6 | AHT FY2023 10-K | https://www.sec.gov/Archives/edgar/data/1232582/000123258224000035/aht-20231231.htm | 2024-03-14 | PRIMARY-READ | debt table + footnotes, note 5, MD&A |
| 7 | AHT 8-K KEYS default | https://www.sec.gov/Archives/edgar/data/1232582/000123258223000064/aht-20230707.htm | 2023-07-07 | PRIMARY-READ | Item 8.01 + Exhibit A |
| 8 | AHT 8-K + EX-99.1 Pool F DIL | https://www.sec.gov/Archives/edgar/data/1232582/000110465923123295/tm2332146d1_8k.htm ; .../tm2332146d1_ex99-1.htm | 2023-12-04 | PRIMARY-READ | 8-K + press-release exhibit |
| 9 | AHT 8-K KEYS origination (Item 2.03) + EX-99.1 | https://www.sec.gov/Archives/edgar/data/1232582/000110465918040855/a18-15496_18k.htm ; .../a18-15496_1ex99d1.htm | 2018-06-18 | PRIMARY-READ | loan table; exhibit index (loan agreements 10.1–10.16 not opened) |
| 10 | AHT 2018-KEYS ABS-15G + EY AUP | https://www.sec.gov/Archives/edgar/data/1740287/000153949718000878/n1280_x1-abs15g.htm ; .../exh_99-1.htm | 2018-06-15 | PRIMARY-READ | AUP background + appraisal table |
| 11 | AHT 8-Ks 2024-10-15 (reverse split), 2024-09-23 (NYSE), 2024-03-11, 2026-07-08, 2026-08-06, 2026-08-27 | https://www.sec.gov/Archives/edgar/data/1232582/000123258224000130/aht-20241015.htm (others same folder pattern per accession in notes) | as dated | PRIMARY-READ | item text |
| 12 | EDGAR submissions JSON AHT / SAFE | https://data.sec.gov/submissions/CIK0001232582.json ; https://data.sec.gov/submissions/CIK0001095651.json | 2026-09-30 | PRIMARY | filing index |
| 13 | EDGAR full-text search ("KEYS Pool", "2018-KEYS", "135 West 50th", "TD 135 West 50") | https://efts.sec.gov/LATEST/search-index?q=... | 2026-09-30 | PRIMARY index | — |
| 14 | DBRS Morningstar AHT 2018-KEYS | https://dbrs.morningstar.com/research/421309/... | 2023-09-29 | SECONDARY (fetch summarizer) | press release |
| 15 | DBRS Morningstar AHT 2018-KEYS | https://dbrs.morningstar.com/research/439850/... | 2024-09-23 | SECONDARY (fetch summarizer) | press release |
| 16 | Connect CRE, W Atlanta | https://www.connectcre.com/stories/atlantas-troubled-w-hotel-bought-at-discount/ | Dec 2023 | SECONDARY | article |
| 17 | Hotel-Online, East Bay hotels | https://www.hotel-online.com/news/two-east-bay-hotels-linked-to-troubled-property-portfolio-are-bought | 2026-07-22 | SECONDARY | article |
| 18 | SAFE Q2-2026 10-Q | https://www.sec.gov/Archives/edgar/data/1095651/000109565126000025/safe-20260630x10q.htm | filed 2026-07-31 | PRIMARY-READ | BS, IS, Note 11, MD&A top-10 table, risk prose |
| 19 | SAFE Q1-2026 10-Q | https://www.sec.gov/Archives/edgar/data/1095651/000109565126000017/safe-20260331x10q.htm | 2026-05-01 | PRIMARY-READ | MD&A prose, top-10 |
| 20 | SAFE FY2025 10-K | https://www.sec.gov/Archives/edgar/data/1095651/000109565126000010/safe-20251231x10k.htm | 2026-02-12 | PRIMARY-READ | risk factor + top-10 |
| 21 | SAFE Q3-2024 10-Q | https://www.sec.gov/Archives/edgar/data/1095651/000109565124000028/safe-20240930x10q.htm | 2024-10-29 | PRIMARY-READ | top-10 (only mention) |
| 22 | iStar 8-K EX-99.5 | https://www.sec.gov/Archives/edgar/data/1095651/000110465923041210/tm2310731d1_ex99-5.htm | 2023-04-04 | PRIMARY-READ | top-10 at 12/31/22 |
| 23 | old Safehold FY2019 10-K | https://www.sec.gov/Archives/edgar/data/1688852/000168885220000014/safe-12312019x10k.htm | 2020-02-13 | PRIMARY-READ | top-10 + risk prose |
| 24 | SAFE 8-K 2026-08-03 | https://www.sec.gov/Archives/edgar/data/1095651/000109565126000028/safe-20260801x8k.htm | 2026-08-03 | PRIMARY-READ | office relocation only (not relevant) |
| 25 | Safehold press release $285M | https://www.safeholdinc.com/press-releases/safehold-closes-a-new-285-million-ground-lease-in-new-york-city/ | 2019-12-12 | company IR via fetch summarizer | — |

**Could not reach / not tried to completion**
- nypost.com (fetch tool blocked) — workbook EVT-0078-01 source not re-read; therealdeal.com (HTTP 403, both the 2023 W Atlanta and 2026 Thakkar pieces); hotelinvestmenttoday.com (HTTP 403, Oakland price) -> those figures stay SNIPPET.
- PincusCo articles: seen only via search summary (not opened).
- AHT 2018-KEYS loan-level remittance / realized losses: 144A deal, no EDGAR 10-D; Trepp / KBRA / servicer reports not accessed. Special servicer name not found.
- NY court dockets (NYSCEF Index 652773/2026, 156448/2026): not attempted (JS/registration-gated); outcome after 2026-07-31 unknown.
- SAFE total gross book value in dollars and 135 W 50th accounting classification: searched 10-K FY2025 and Q2-26 10-Q prose for a dollar GBV — not found; Schedule III / lease footnote tables not mined.
- AHT loan agreement exhibits 10.1–10.16 (2018) — not opened (mezz purchase-option terms would bear on who bought the Pool F mortgage).
- Retrieval shapes tried: filing tables (debt tables, BS, top-10), MD&A prose, footnotes (debt, dispositions, legal), exhibits (press releases, AUP), EDGAR full-text search, rating-agency releases, trade press. Not tried: XBRL companyfacts API (BS figures were read directly from the HTML statements instead), court dockets, Trepp.

---
## Appendix: raw running notes (written incrementally during research)

## Running notes (raw, PRIMARY-READ unless stated)
- AHT FY2025 10-K debt note R16 (acc 0001232582-26-000067, filed 2026-03-23) READ. Key text: KEYS loans entered 2018-06-13, 2y + five 1y ext; 2023-07-07 AHT elected not to make extension paydowns on Pools A, B, F "thereby defaulting"; 2023-11-29 deed in lieu "for the transfer of ownership of the KEYS Pool F $215.1 million mortgage to the mortgage lender"; 2024-03-01 Pools A+B hotels to court-appointed receiver; derecognized Mar 2024, gain $133.9M (Q1 2024), contract asset $378.2M at 3/31/24; +$33.3M gain rest of 2024 (FY2024 total $167.2M); +$39.1M FY2025; Plano pair foreclosed 2024-07-02; Columbus Tipton Lakes 2024-11-04 (-> contract asset & debt reduced $45.0M as of 12/31/24); Oakland 2025-06-25 + BWI 2025-12-22 (-> reduced $50.6M as of 12/31/25); Plymouth Meeting 2026-03-04.
- AHT Q2 2026 10-Q (acc 0001232582-26-000183, filed 2026-08-12) READ: BS 6/30/26: total assets $2,334,450k; indebtedness net $1,905,747k; debt assoc. w/ hotels in receivership $273,971k; accrued interest assoc. receivership $94,327k; contract asset $368,298k; cash $72,510k; restricted $136,985k; total liabilities $2,643,964k; total equity (deficit) $(556,538)k; stockholders' deficit of Company $(570,885)k. Going concern: "substantial doubt". $945.2M non-recourse loans maturing within 1 yr. Pref dividends suspended 2026-01-13 "as it evaluates strategic alternatives". JPM8 $325M loan default notice 2026-02-11. Further receiver sales 2026-07-16 (Courtyard Newark SV, RI San Jose Newark) and 2026-08-06 (TPS + SHS Manhattan Beach). Hilton Santa Cruz Scotts Valley ($22.0M) to receiver 2026-06-01, contract asset $24.9M (so receivership line now mixes KEYS A/B + Santa Cruz).
- AHT 8-K 2023-07-07 (acc 0001232582-23-000064) READ: Pool A original principal $180,720,000 (7 hotels, L+3.65 -> SOFR+3.70); Pool B $174,400,00[0] (7 hotels, L+3.39 -> S+3.44); Pool F $215,120,000 (5 hotels: Embassy Suites Flagstaff, ES Walnut Creek, Marriott Bridgewater, Marriott RTP Durham, W Atlanta Downtown; L+3.70 -> S+3.73). "most likely outcome will be a consensual transfer of these hotels to the respective lenders".
- AHT 8-K 2023-12-04 + EX-99.1 (acc 0001104659-23-123295) READ: Pool F DIL "on November 30, 2023" to "the current holder of the mortgage loan". EX-99.1: "The original lenders previously transferred the loans to a securitization trust. Such trust, acting through its servicer, brought suit seeking the appointment of a receiver" [re Pools A/B]; BofA, Morgan Stanley, Barclays "are not party to the litigation".
- AHT FY2023 10-K (acc 0001232582-24-000035, filed 2024-03-14) READ: Note 5: Pool F DIL completed "November 29, 2023" -> gain on extinguishment of debt ~$53.4M (FY2023). Debt-table fn (8) says "November 30, 2023" -> AHT's own 10-K carries BOTH dates. Debt table 12/31/22: Pool F debt $215,120k vs book value of collateral $164,792k. 12/31/23: Pool A debt $180,720k / BV collateral $121,119k; Pool B $174,400k / $113,110k; default rate +4.00%; fn(6)(7): Pools A, B "effective June 9, 2023 ... in default". "During the years ended December 31, 2023, 2022 and 2021, no impairment charges were recorded."
- AHT 8-K 2018-06-18 (acc 0001104659-18-040855, Item 2.03) READ: six KEYS loans 2018-06-13 with BofA N.A., Barclays Bank PLC, Morgan Stanley Bank N.A.; "Each Loan is structured as a mortgage loan and one or more mezzanine loans"; nonrecourse w/ carve-outs guaranteed by Ashford Hospitality LP. Original principal: Pool A mortgage $144,400,000 + mezz $36,320,000 (=180.72M); Pool B mortgage $149,400,000 + mezz $25,000,000 (=174.40M); Pool F mortgage $166,600,000 + sr mezz $21,630,000 + jr mezz $26,890,000 (=215.12M). => AHT's single-line "$215.1M mortgage" = TOTAL debt stack incl. mezz.
- AHT 2018-KEYS CMBS (issuing entity CIK 0001740287; depositor Morgan Stanley Capital I Inc.) ABS-15G 2018-06-15 + EY AUP EX-99.1 READ: trust assets "six floating rate whole mortgage loans" on 34 hotels; "Each Mortgage Loan has a related ... senior mezzanine loan and, in certain cases, a related ... junior mezzanine loan ... that will not be assets of the Issuing Entity." AUP 2018 appraisals (subset only): Pool 6 [=F] ES Walnut Creek $62.4M, Marriott Bridgewater $89.0M, Marriott RTP $33.5M; Pool 1 [=A] SHS Plymouth Meeting $26.0M, RI Las Vegas $47.7M; Pool 2 [=B] CY Plano $22.7M, RI Plano $17.7M (all "as is", 1 Apr 2018; mapping Pool1/2/6 -> A/B/F inferred from property lists).
- DBRS Morningstar 2023-09-29 (research/421309) SECONDARY (rating agency): orig senior mortgage $982.0M + mezz $288.2M; all loans to special servicing April 2023; Pools A,B,F "will remain with the special servicer"; est. loss severities >15% Pool A, >20% Pool B, >10% Pool F; Class F certs downgraded to CCC(sf).
- DBRS Morningstar 2024-09-23 (research/439850) SECONDARY: "the payoff of one formerly specially serviced loan, Pool F, with the November 2023 remittance" => trust received payoff on Pool F mortgage (no trust loss reported). Pools A/B workout: DIL to trust on majority; "A DIL was accepted on 10 other properties in August 2024"; lender foreclosed 2 TX properties July 2024; liquidation scenario: severities >30% Pool A, >70% Pool B, "total implied liquidated loss amount, all from Pools A and B, is in excess of $150 million"; Class E downgraded to BB(sf). Collateral reduction 32.4% since issuance.
- Connect CRE (W Atlanta) SECONDARY: Stonebridge Hospitality acquired W Atlanta Downtown via DIL, $24.8M, Dec 2023; AHT bought it 2015 for $56.75M. (Real Deal 2023-12-11 = HTTP 403, not read.)
- AHT receivership debt line: 3/31/24 $355,120k (Q1-24 10-Q) [= 180.72+174.40]; 12/31/24 $314,640k and 12/31/25 $272,800k (FY2025 10-K BS); Q2-26 10-Q recasts 12/31/25 to $294,771k (= 272,800 + 21,971 Santa Cruz). Accrued int. receivership 12/31/25 $82,338k (10-K). Q1-24 10-Q: contract asset $378,160k.
- SAFE Q2 2026 10-Q (acc 0001095651-26-000025) READ: Note 11 Legal Proceedings: 2026-05-11 termination notice to TD 135 West 50 LLC "under one of its New York office properties" for breaches incl. "failure to pay property taxes as required under the lease"; First Action 135 West 50th Street Ground Owner LLC v. TD 135 West 50 LLC, NY Sup Ct Index No. 652773/2026 (declaratory, ejectment, damages); Second Action (tenant) Index No. 156448/2026 filed 2026-05-20; 2026-06-04 TRO staying SAFE from acting on termination/ejectment pending PI motion; 2026-06-12 SAFE moved in App. Div. 1st Dept to modify TRO; both motions pending at filing. SAFE: "lease has been duly terminated". Material-litigation statement says no OTHER proceeding material. SAFE BS 6/30/26: total assets $7,520,024k; SAFE shareholders' equity $2,439,146k; total equity $2,632,247k; debt $4,653,713k; cash $15,922k. GL portfolio GBV mix 39% office. Combined Property Value $16,676M; Ground Lease Cost $6,906M; UCA $9,770M (6/30/26). "did not have a significant concentration of interest income ... from any tenant". Leasehold loans all current.
- SAFE Q2 2026 10-Q MD&A top-10 table READ: 135 West 50th Street, Office, NY, lease exp 2123, "Fixed with Inflation Adjustments", 5.0% of gross book value (6/30/26) [#2 asset]. "The tenant at 135 West 50th Street defaulted on a forbearance agreement in connection with the tenant's failure to pay property taxes, and we sent the tenant a lease termination notice in May 2026 ... TRO ... no assurances". Risk factor: "forbearance agreement with a tenant under a significant New York office asset". GBV footnote: "historical purchase price plus accrued interest on sales-type leases". Total GBV $ NOT stated in the 10-Q text I read.
- Share history (PRIMARY-READ, top-10 tables): 10.9% of GBV 12/31/19 (old SAFE CIK 1688852 FY2019 10-K, which also flags 135 W 50th as "under development or in transition"); 5.2% 12/31/22 (iStar 8-K 2023-04-04 EX-99.5); 4.8% 9/30/24 (Q3-24 10-Q); 4.6% 12/31/25 (FY2025 10-K); 4.7% 3/31/26; 5.0% 6/30/26. Q3-24 10-Q (filed 2024-10-29) mentions 135 W 50th ONLY in the top-10 table — no disclosure of the July 2024 leasehold auction found.
- Check (arithmetic on PRIMARY-READ Q2-26 BS): debt assoc. receivership $273,971k + accrued interest receivership $94,327k = $368,298k = contract asset $368,298k EXACTLY -> receivership block nets to zero on AHT BS.
- SAFE Q1 2026 10-Q (acc 0001095651-26-000017, filed 2026-05-01) READ: "The tenant defaulted on such agreement and we made a $8.3 million protective tax advance." FY2025 10-K (filed 2026-02-12): forbearance agreement with tenant under "a significant New York office asset" (pre-default language).
- SAFE Q2-26: "gross book value as a percentage of combined property value was 52%"; CPV $16,676M -> implied GBV ~ $8.67B (DERIVED, rounded inputs). 6M-26 total revenues $225,500k; net income $59,620k.
- SECONDARY: Safehold press release 2019-12-12 (safeholdinc.com) $285M ground lease, 929k SF, building undergoing capital improvements (read via fetch summarizer). PincusCo (via search summary, not opened): TD 135 West 50 LLC (Thakkar Developers) paid $8.5M to UBS Realty Investors (135 West 50th Street Lessee LLC) for the leasehold; closed 2024-10-08, recorded 2024-10-10; ground rent $800k/mo ($9.6M/yr); UBS bought ground lease 2006 $332.5M, fee 2012 $279M, sold fee to Safehold Dec 2019. The Real Deal 2026-05-22 (search snippet only): Safehold suit alleges nearly $28M unpaid property taxes, interest, penalties.
