# Nonrecurring Level 3 collateral-dependent loan / OREO fair-value disclosure: FLG, EGBN, AMTB, VLY, OZK
Q1-2026 (3/31/26) vs Q2-2026 (6/30/26). Read-only extraction 2026-10-22 by REGINALD sub-reader. Source: SEC 10-Qs (accessions in tenq/list.txt); OZK from local FDIC-filed PDFs converted to text.
Locator base: /tmp/claude-1000/-home-willi-Research-workspace-AGENTS-REGINALD/6c4d79ab-0929-4559-a8f4-ceacf4c6c976/scratchpad/tenq/ ; "file:line" = full stripped text line number (one table cell per line, so a table spans a range). Dollar units as stated per bank.
Marking: **[DERIVED]** = my arithmetic from disclosed figures, not a bank-stated number. NOT DISCLOSED = absent from the filing text I searched (nonrecurring-FV note, loan note, MD&A credit section).

Headline: only AMTB gives a quantified appraisal-discount input (range plus "typical" band, unweighted). OZK, FLG, EGBN name a "management discount" / "may discount from appraisal" input but give NO range or weighted average. VLY gives a qualitative discounting description and a bridge from amortized cost to net carrying amount (the best comparable mark for VLY).

---
## FLG (Flagstar)  -- $ millions

| item | Q1-2026 | Q2-2026 | verbatim | locator |
|---|---|---|---|---|
| Loans HFI at FV, nonrecurring, Level 3 | $2,489M (Dec-25 comparative $2,784M) | $2,621M (Dec-25 $2,784M) | "Loans held for investment (1) ... 2,489 ... 2,489" / "... 2,621 ... 2,621"; fn (1) "Represents the fair value of impaired loans, based primarily on the value of the collateral less costs to sell." | FLG_Q1.txt:5668-5683 ; FLG_Q2.txt:6784-6799 (fn 6812) |
| By loan category (FV table) | NOT DISCLOSED (single line, no CRE/multifamily split) | NOT DISCLOSED | n/a | same |
| Other assets at FV (equity securities w/o readily determinable FV) | $27M | $28M | "Other assets (2) ... 27" / "... 28"; total nonrecurring $2,516M / $2,649M | FLG_Q1.txt:5683-5690 ; FLG_Q2.txt:6797-6810 |
| Valuation technique | "appraisal values less costs to sell or other observable market data" (no table row) | same | "The fair values of collateral-dependent loans are determined using various valuation techniques, including appraisal values less costs to sell or other observable market data." | FLG_Q1.txt:5735 ; FLG_Q2.txt:6851 |
| Unobservable input name | NOT DISCLOSED (no quantitative Level 3 input table) | NOT DISCLOSED | none | n/a |
| Range / weighted average | NOT DISCLOSED | NOT DISCLOSED | none | n/a |
| OREO / repossessed assets at FV (nonrecurring) | NOT DISCLOSED in FV note. Carrying value only (NPA table): repossessed assets $8M | repossessed assets $8M | "Repossessed assets | 8 | 11" (vs Dec-25 11) | FLG_Q1.txt:1518 ; FLG_Q2.txt:1645 |
| Losses / FV adjustments on the nonrecurring assets | NOT DISCLOSED in FV note. Related: gross charge-offs on multi-family and CRE $99M, 3 months ended 3/31/26 | $193M, six months ended 6/30/26 (Q2 alone = $94M **[DERIVED]** 193 minus 99) | "Gross charge-offs of $99 million were recorded on multi-family and CRE loans during the three months ended March 31, 2026, primarily driven by appraisals received on those loans..." / "Gross charge-offs of $193 million ... during the six months ended June 30, 2026, primarily driven by appraisals received..." | FLG_Q1.txt:1930 ; FLG_Q2.txt:2106 |
| Appraisal age / policy | Policy only: "order updated appraisals for all substandard and non-accrual loans ... if the most recent appraisal on file ... is more than one year old"; "All substandard loans, including non-accrual loans, are appraised at the time of downgrade and are re-appraised annually." | same policy text | policy statements, not portfolio ages | FLG_Q1.txt:1931 (re-appraised annually: ~1924) ; FLG_Q2.txt:2107 (~2101) |
| Collateral-dependent loans HFI, recorded investment (loan note) | $2,454M: multi-family $2,017M, CRE $374M, 1-4 family first mortgage $63M | $2,555M: multi-family $2,130M, CRE $346M, 1-4 family $54M, C&I $25M | "Total collateral-dependent loans held for investment $ 2,454" / "$ 2,555" | FLG_Q1.txt:4230-4240 ; FLG_Q2.txt:4884-4896 |
| Weighting basis | n/a (no weighted average disclosed) | n/a | | |

Notes: FV of "impaired loans" ($2,489M / $2,621M) is slightly ABOVE recorded investment of collateral-dependent loans ($2,454M / $2,555M) (ratio 1.014 / 1.026 **[DERIVED]**), so the two perimeters differ and no implied mark below appraisal can be backed out. FLG's markdown evidence is the charge-off disclosure, not an FV input.

---
## EGBN (Eagle Bancorp) -- $ thousands

| item | Q1-2026 | Q2-2026 | verbatim | locator |
|---|---|---|---|---|
| Individually assessed loans at FV, Level 3 (total of six lines) | $90,849K **[DERIVED sum of lines below]** | $92,933K **[DERIVED]** | table title "Individually assessed loans:" | EGBN_Q1.txt:3792-3845 ; EGBN_Q2.txt:4683-4742 |
|  - Commercial | 10,420 | 15,890 | "Commercial | - | - | 10,420 | 10,420" | EGBN_Q1.txt:3807 ; EGBN_Q2.txt:4698 |
|  - Income producing CRE | 54,150 | 66,021 | | EGBN_Q1.txt:3813 ; EGBN_Q2.txt:4704 |
|  - Owner occupied CRE | 5,052 | 5,095 | | EGBN_Q1.txt:3818 ; EGBN_Q2.txt:4709 |
|  - Real estate mortgage, residential | 564 | 552 | | EGBN_Q1.txt:3823,3833 ; EGBN_Q2.txt:4709-4720 |
|  - Construction, commercial and residential | 20,293 | 4,883 | | EGBN_Q1.txt:3828 ; EGBN_Q2.txt:4719 |
|  - Consumer | 370 | 492 | | EGBN_Q1.txt:3823,3833 ; EGBN_Q2.txt:4709-4720 |
| Loans held for sale at FV (Level 3, nonrecurring) | 55,702 (Dec-25 90,650) | 49,663 | "Loans held for sale | - | - | 55,702" | EGBN_Q1.txt:3838 ; EGBN_Q2.txt:4729 |
| Valuation technique | Market valuation approach, "based on an appraisal conducted by an independent, licensed appraiser"; non-collateral-dependent loans: income approach / DCF at original contract rate | same | "For the collateral-dependent loans and other real estate owned, the Company measures the fair value utilizing a market valuation approach, based on an appraisal conducted by an independent, licensed appraiser. ... For loans that are not collateral dependent, the Company uses an income approach, specifically, the discounted cash flow method." | EGBN_Q1.txt:3919-3925 ; EGBN_Q2.txt:4806-4812 |
| Unobservable input name | "Management may discount the value from the appraisal" (qualitative only; no named input row) | same | "Management may discount the value from the appraisal in determining the fair value if, based on its understanding of the market conditions, the collateral had been impaired below the appraised value (Level 3)." | EGBN_Q1.txt:3919-3925 ; EGBN_Q2.txt:4811-4812 |
| Range / weighted average | NOT DISCLOSED (no quantitative input table) | NOT DISCLOSED | none | n/a |
| OREO at FV (Level 3) | 2,059 (unchanged vs Dec-25 2,059) | 1,966 | "Other real estate owned | - | - | 2,059" / "1,966" ; OREO "initially recorded at fair value less estimated selling costs. Fair value is based upon independent market prices, appraised values of the collateral or management's estimation" | EGBN_Q1.txt:3843 ; EGBN_Q2.txt:4734 |
| Total nonrecurring Level 3 | 148,610 (Dec-25 180,011) | 144,562 | "Total assets measured at fair value on a nonrecurring basis" | EGBN_Q1.txt:3851 ; EGBN_Q2.txt:4742 |
| Losses / FV adjustments recognized in period | NOT DISCLOSED in this table. Text: "Adjustments to the fair value of these assets usually result from ... write-downs of individual assets after they are evaluated for impairment." | NOT DISCLOSED | general statement only | EGBN_Q1.txt:3919 ; EGBN_Q2.txt:4806 |
| Appraisal dates/ages | NOT DISCLOSED for the FV table. OREO policy (Q2): updated third-party appraisals "not less frequently than annually", plus when current appraisal "does not accurately reflect current value" | same | "obtain updated third party appraisals on OREO properties generally not less frequently than annually" | EGBN_Q2.txt:6953 |
| Cross-reference: amortized cost of collateral-dependent HFI loans (loan note) | Total $129,230K = business/other assets 16,185 + real estate 113,045 | Total $111,525K = 23,571 + 87,954 | "The table below presents the amortized cost basis of collateral-dependent HFI loans by portfolio segment." | EGBN_Q1.txt:1628-1670 ; EGBN_Q2.txt:2090-2128 |
| **[DERIVED]** FV of individually assessed line / amortized cost of same-name collateral-dependent line | Income producing CRE 54,150 / (75,781+880) = 70.6%; Commercial 10,420 / (15,305+3,215) = 56.3%; Construction 20,293 / 28,016 = 72.4% | Income producing CRE 66,021 / (74,185+880) = 87.9%; Commercial 15,890 / (22,554+2,669) = 63.0%; Construction 4,883 / 4,952 = 98.6% | arithmetic only | see rows above |

Caveats: the derived ratios mix two perimeters (the FV table covers loans where an allowance is set off collateral FV plus loans "not requiring a specific allowance"; the amortized-cost table covers all collateral-dependent loans). Treat as indicative only; it is NOT a bank-stated appraisal discount. Weighting basis: n/a.

---
## AMTB (Amerant) -- $ thousands

| item | Q1-2026 | Q2-2026 | verbatim | locator |
|---|---|---|---|---|
| Loans HFI measured for credit deterioration using FV of collateral, Level 3 | $9,478K (commercial $7.1M + owner-occupied $2.4M) (Dec-25 $7,497K) | $5,941K (commercial $5.9M) | "Loans held for investment measured for credit deterioration using the fair value of the collateral (1) | 9,478 | - | - | 9,478 | 2,801" ; Q2 "... 5,941 ... -" ; col header "Carrying Amount" | AMTB_Q1.txt:3918-3943 ; AMTB_Q2.txt:4705-4730 |
| Cash flow dependent loans measured for ECL (separate line, Level 3) | $68,244K, all commercial; specific reserves $3.9M | $67,008K (commercial $64.9M + owner-occupied $2.1M); specific reserves $3.1M + $0.5M | "Cash flow dependent loans measured for expected credit losses (3) | 68,244 ... 15,596" | AMTB_Q1.txt:3952-3953 ; AMTB_Q2.txt:4739-4743 |
| Loans HFS at lower of cost or FV (Level 3) | $190,014K | $122,172K | "Loans held for sale, at lower of cost or fair value" | AMTB_Q1.txt:3930 ; AMTB_Q2.txt:4717-4723 |
| Valuation technique | "Appraisal value, as adjusted" | "Appraisal value, as adjusted" | unobservable-input table: "Collateral dependent loans | Discount to fair value | Appraisal value, as adjusted | 0 - 30 % | 6 - 7 %" | AMTB_Q1.txt:4024-4049 ; AMTB_Q2.txt:4818-4843 |
| Unobservable input name | "Discount to fair value" (real-estate collateral); also Inventory, Accounts receivables, Equipment (for cash-flow/non-RE collateral) | same | table column headers "Unobservable Inputs | Valuation Methods | Discount Range | Typical Discount" | same |
| Range (low-high), RE collateral loans | 0% - 30% | 0% - 30% | "0 - 30 %" | AMTB_Q1.txt:4033 ; AMTB_Q2.txt:4827 |
| "Typical Discount" (NOT a weighted average) | 6% - 7% | 6% - 7% | "6 - 7 %" ; column titled "Typical Discount", no weighting stated | AMTB_Q1.txt:4034 ; AMTB_Q2.txt:4828 |
| Non-RE collateral discount ranges | Inventory 0-100% (typical 30-50%); A/R 0-100% (20-30%); Equipment 0-100% (20-30%) | identical | | AMTB_Q1.txt:4035-4047 ; AMTB_Q2.txt:4829-4841 |
| OREO at FV (Level 3) | $15,542K ($14.0M commercial + $1.6M residential); input "Discount to fair value", "Appraisal value, as adjusted", range N/A, typical 6-7% | $15,542K (same split); same input; range N/A; typical 6-7% | "Other Real Estate Owned (2) | 15,542 ... -" ; "Other Real Estate Owned | Discount to fair value | Appraisal value, as adjusted | N/A | 6 - 7 %" | AMTB_Q1.txt:3946-3949, 4048 ; AMTB_Q2.txt:4733-4736 |
| Total write downs recognized in period (nonrecurring table) | Loans HFS $3,375K; collateral-FV loans HFI $2,801K; OREO nil (Dec-25: $1,114K); cash-flow-dependent $15,596K; total $21,772K | Loans HFS $2,745K; collateral-FV loans HFI nil ("There were no write downs on these loans at June 30, 2026"); OREO nil; cash-flow-dependent $18,398K; total $21,143K | "Total Write Downs" column | AMTB_Q1.txt:3935-3955 ; AMTB_Q2.txt:4717-4745 |
| Appraisal age | Policy: valuations requested on all RE securing NPLs "with existing valuations older than 12-months and outstanding balances in excess of $1.0 million"; 8 recently downgraded loans, $98.9M, with appraisals older than 12 months, new appraisals ordered | 12 loans, $74.7M, appraisals older than 12 months, new appraisals ordered | "No additional provision for credit losses was deemed necessary in both periods as a result of these valuations." | AMTB_Q1.txt:4762 ; AMTB_Q2.txt:5985 |
| Weighting basis | Unweighted: only a range and a "typical discount" band | same | | |

---
## VLY (Valley) -- $ thousands unless noted

| item | Q1-2026 | Q2-2026 | verbatim | locator |
|---|---|---|---|---|
| Collateral dependent loans at FV (net carrying amount), Level 3 | $105,559K (Dec-25 $105,107K) | $113,921K | "Collateral dependent loans (3) | $ | 105,559 | $ | - | $ | - | $ | 105,559" / "113,921" | VLY_Q1.txt:1200-1209 ; VLY_Q2.txt:1665-1674 |
| By loan category | NOT DISCLOSED (single line; text notes taxi medallion loans $46.6M amortized cost) | NOT DISCLOSED (taxi medallions $42.5M amortized cost) | | VLY_Q1.txt:1354 ; VLY_Q2.txt:1820 |
| Valuation technique | Fair value of underlying collateral; "individual third party appraisals that may be adjusted based on certain discounting criteria" | "individual third-party appraisals that may be adjusted based on certain discounting criteria" | "Collateral values are estimated using Level 3 inputs, consisting of individual third party appraisals that may be adjusted based on certain discounting criteria. Certain real estate appraisals may be discounted based on specific market data by location and property type." | VLY_Q1.txt:1354 ; VLY_Q2.txt:1820 |
| Unobservable input name | "discounting criteria" (qualitative; no quantitative table) | same | | same |
| Range / weighted average | NOT DISCLOSED | NOT DISCLOSED | no quantitative unobservable-input table in either 10-Q | n/a |
| Amortized cost of collateral dependent loans | $184.0M (incl. taxi medallions $46.6M) | $204.4M (incl. taxi medallions $42.5M) | "Collateral dependent loans with a total amortized cost of $ 184.0 million ..., were reduced by specific allowance for loan loss allocations totaling $ 78.5 million to a reported total net carrying amount of $ 105.6 million at March 31, 2026." / "$ 204.4 million ... $ 90.5 million ... $ 113.9 million at June 30, 2026." | VLY_Q1.txt:1354 ; VLY_Q2.txt:1820 |
| Specific reserve allocations netted | $78.5M (Dec-25 $82.0M) | $90.5M | fn (3) "Net of specific reserve allocations reported within the allowance for loan losses totaling $ 78.5 million ..." | VLY_Q1.txt:1343 (fn 3) ; VLY_Q2.txt:1808 |
| **[DERIVED]** net carrying / amortized cost | 105.6 / 184.0 = 57.4% (reserve 42.7% of amortized cost) | 113.9 / 204.4 = 55.7% (reserve 44.3%) | arithmetic only; includes taxi medallions (not real-estate collateral) | |
| Foreclosed assets at FV (OREO + other repossessed), Level 3 | $3,356K (Dec-25 $5,680K) | $4,868K | "Foreclosed assets | 3,356 | - | - | 3,356" / "4,868" | VLY_Q1.txt:1211-1214 ; VLY_Q2.txt:1676-1679 |
| OREO technique / input | "third party appraisal less estimated cost to sell"; Q1: "There were no adjustments to the appraisals of foreclosed assets at March 31, 2026 and December 31, 2025." | "third-party appraisal less estimated cost to sell" | | VLY_Q1.txt:1355 ; VLY_Q2.txt:1820 |
| Losses / FV adjustments | Collateral-dependent loans: remeasured "through direct loan charge-offs to the allowance"; amount of period charge-offs on these NOT DISCLOSED in the FV note. Foreclosed assets write-downs: "There were no write-downs of foreclosed assets during the three months ended March 31, 2026 and 2025." | Foreclosed assets: "write-downs totaling $ 1.0 million for both the three and six months ended June 30, 2026" | verbatim as quoted | VLY_Q1.txt:1355 ; VLY_Q2.txt:1820 |
| Appraisal dates/ages | NOT DISCLOSED | NOT DISCLOSED | | |
| Weighting basis | n/a | n/a | | |

---
## OZK (Bank OZK) -- $ thousands unless noted. Source: FDIC-filed 10-Q PDFs (text converted, tab-separated)

| item | Q1-2026 | Q2-2026 | verbatim | locator |
|---|---|---|---|---|
| Nonaccrual loans at FV, Level 3 nonrecurring | $281,475K (Dec-25 $327,215K) | $286,664K | "At March 31, 2026 and December 31, 2025, the Bank had reduced the carrying value of its nonaccrual loans to the estimated fair value of $281.5 million and $327.2 million" / Q2 "... of $286.7 million and $327.2 million" | OZK_Q1.txt:4067, 4113, 4180 ; OZK_Q2.txt:5380, 5426, 5452 |
| By loan category | NOT DISCLOSED | NOT DISCLOSED | single "Nonaccrual Loans" line | same |
| Valuation technique | "Third-party appraisal (1) or discounted cash flows" | same | fn (1) "The Bank utilizes valuation techniques consistent with the market, cost, and income approaches, or a combination thereof in determining fair value." | OZK_Q1.txt:4180 ; OZK_Q2.txt:5452 |
| Unobservable input name | "Management discount based on underlying collateral characteristics and market conditions" | same | verbatim | OZK_Q1.txt:4180-4186 ; OZK_Q2.txt:5452-5457 |
| Range / weighted average | NOT DISCLOSED (no numeric range or average) | NOT DISCLOSED | none | n/a |
| ALL allocation embedded in the FV mark (nonaccrual loans) | $15.2M (Dec-25 $14.0M) | $13.7M | "The adjustment to reduce the carrying value of such nonaccrual loans to the estimated fair value included $15.2 million and $14.0 million of ALL allocations as March 31, 2026 ..." | OZK_Q1.txt:4113 ; OZK_Q2.txt:5426 |
| Gross nonaccrual loans (NPA table) | $296,575K | $300,416K | "Nonperforming/nonaccrual loans" | OZK_Q1.txt:6325 ; OZK_Q2.txt:8185 |
| **[DERIVED]** FV / gross nonaccrual | 281,475 / 296,575 = 94.9% (gap $15.1M, matches ALL $15.2M within rounding) | 286,664 / 300,416 = 95.4% (gap $13.75M, matches ALL $13.7M) | arithmetic; shows OZK's mark vs recorded balance is ALL-only, i.e. prior charge-offs are already outside it | |
| Foreclosed assets (OREO) at FV, Level 3 | **$154,496K** (Dec-25 $61,076K) | **$292,744K** | "Foreclosed Assets | 154,496" / "292,744" | OZK_Q1.txt:4068, 4187 ; OZK_Q2.txt:5381, 5458 |
| OREO technique / inputs | "Third-party appraisal, broker price opinions and/or discounted cash flows"; inputs: "1. Management discount based on underlying collateral characteristics and market conditions 2. Discount rate 3. Holding period" | same | verbatim | OZK_Q1.txt:4187-4196 ; OZK_Q2.txt:5458-5468 |
| OREO range / weighted average | NOT DISCLOSED | NOT DISCLOSED | | |
| OREO composition | Construction/land 54,447; other CRE 95,100; residential 23; total RE 149,570; consumer 4,926 (total 154,496). Increase "primarily related to two RESG assets with a total outstanding balance of $95.1 million ... collateralized by life science and office properties" | Construction/land 54,447; other CRE 233,483; residential 204; total RE 288,134; C&I 3,202; consumer 1,408 (total 292,744). "primarily consisted of three office buildings totaling $137.5 million, two life science buildings totaling $96.0 million and one parcel of land totaling $54.4 million." | | OZK_Q1.txt:3581-3593, 6345 ; OZK_Q2.txt:4906-4947, 8205 |
| Foreclosed-asset writedowns (period) | $333K (3 months to 3/31/26; Q1-25 $350K) | $2,983K for six months to 6/30/26; Q2 alone $2,650K **[DERIVED]** 2,983 minus 333 | "Writedowns of foreclosed assets | (333)" / "(2,983)" (six-month column, activity table beginning balance 61,076) | OZK_Q1.txt:3621-3640 ; OZK_Q2.txt:4951-4956 |
| Transfers into foreclosed assets | $97,322K (Q1) | $241,569K six months; Q2 alone $144,247K **[DERIVED]** | "Loans and other assets transferred into foreclosed assets" | same |
| Loan-side losses recognized on nonaccrual-loan FV | NOT DISCLOSED separately (only ALL allocation above) | NOT DISCLOSED | | |
| Appraisal dates/ages | NOT DISCLOSED for the nonrecurring table. Policy: appraisals at origination/renewal via independent Appraisal Services team; no "updated within X months" statement in FV note. Unrelated: LTV "based on the most recent appraisals ... approximately 43%" (RESG unfunded context) | same | | OZK_Q1.txt:5649-5653, 6285 ; OZK_Q2.txt:7510-7514, 8145 |
| Weighting basis | n/a | n/a | | |

---
## Summary (one line per bank)
- **FLG:** loans HFI nonrecurring L3 FV $2,489M -> $2,621M (+5.3%); discount input NOT DISCLOSED (no unobservable-input table; "appraisal values less costs to sell"); direction NOT COMPARABLE. Only markdown evidence: multi-family/CRE gross charge-offs $99M in Q1, $193M six-month (Q2 about $94M, derived), "driven by appraisals received".
- **EGBN:** individually assessed loans FV $90.8M -> $92.9M (derived sum; CRE income-producing $54.2M -> $66.0M; construction $20.3M -> $4.9M; OREO $2.06M -> $1.97M); discount input "management may discount the value from the appraisal", no range or w-avg; NOT COMPARABLE (derived FV/amortized-cost on CRE 70.6% -> 87.9% is perimeter-mismatched and indicative only, would read as shallower).
- **AMTB:** collateral-FV loans HFI $9.5M -> $5.9M (cash-flow-dependent loans $68.2M -> $67.0M; OREO $15.5M flat); "discount to fair value" range 0-30%, typical 6-7% (unweighted) in both quarters; FLAT (table unchanged verbatim; the typical-discount band is static boilerplate, not a measured weighted average). Appraisals older than 12 months: 8 loans/$98.9M -> 12 loans/$74.7M.
- **VLY:** collateral-dependent loans net FV $105.6M -> $113.9M; no input range/w-avg, only "discounting criteria"; best comparable is the bridge: net carrying / amortized cost 57.4% -> 55.7% (reserve $78.5M of $184.0M -> $90.5M of $204.4M, incl. taxi medallions $46.6M -> $42.5M), derived; direction DEEPER (modestly, derived, mixed collateral). Foreclosed assets $3.4M -> $4.9M with $1.0M write-downs in Q2.
- **OZK:** nonaccrual loans FV $281.5M -> $286.7M; input "management discount based on underlying collateral characteristics and market conditions", range/w-avg NOT DISCLOSED; FV/gross nonaccrual 94.9% -> 95.4% (ALL-only gap $15.2M -> $13.7M), derived: FLAT/NOT COMPARABLE. Bigger signal is OREO (foreclosed assets) $154.5M -> $292.7M (three offices $137.5M, two life-science $96.0M, land $54.4M) with six-month writedowns $2.98M (Q2 about $2.65M, derived) and no disclosed discount range.
