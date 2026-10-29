# HOMER — 2026-10-28 catch-up: WALTER intake disposition (29 signals, 10/20–10/27)

**Session:** Claude Code, Opus 5.5 (`claude-opus-5-5`), Will-launched from `AGENTS/HOMER/`, 2026-10-28 ~22:46 ET. First HOMER session since the 10/19 closeout.
**Scope of this file:** the disposition of every unlogged `inbox/WALTER/` signal. The data prints released 10/20–10/28 are integrated in `reports/2026-10-28_catchup-prints.md` and the workbook ledgers. Nothing here moves a band level, a frozen thesis criterion or a prediction.

## A. Signals that touch a dashboard row or registered instrument

| Signal | Content (WALTER kernel, source as stated) | HOMER disposition |
|---|---|---|
| SIG-W-20261020-001 | NAR 10/20: Sept pending home sales −7.3% MoM, −11.3% YoY; all four regions down. Record-low framing NOT established | Integrated from the issuer release in the prints report (PRICING row). Record-low claim not adopted unless the index level is read against the Apr-2020 69.0 trough |
| SIG-W-20261020-014 | Census CB26-162 (10/20): Sept starts 1,221K (−5.2% ±11.8, not significant); SF 859K; permits 1,400K (−0.2%); SF permits 845K; Aug revised 1,275→1,288K, Jul 1,309→1,369K | Integrated in the prints report (PRICING row) with significance and revisions carried. Not a post-COVID low (May 1,182K was lower) |
| SIG-W-20261020-028 | Payment-hours chart (dated 10/04, 10/01 rate basis); a 209bp four-week-average spread outside its own 150–200 band; mixed windows | ACCEPTED as a basis note. HOMER's house spread (weekly PMMS minus Wednesday 10Y close) is a different convention from a four-week average; neither is MBS OAS. The payment-hours model is a hypothetical new purchase, not existing owners. No causal reclassification adopted |
| SIG-W-20261022-029 | FRED MORTGAGE30US 7.32% [10/22] vs 7.40% [10/15] | Re-read at the issuer page (prints report); A2 weekly print |
| SIG-W-20261025-012 | White House EO 10/22 "Decreasing Housing Costs": FHFA MI-cancellation pilot for loans originated AFTER the pilot exists; title-acceptance alternatives for eligible refis; USDA/VA DIRECT-loan rate reductions; 180-day manufactured-housing task force | Recorded as KB-HOMER-039 with the existing-loan exclusion and direct-loan scope attached. No current-rate effect; no milestone has occurred yet. Implementation checks go to the docket (first: FHFA pilot announcement) |
| SIG-W-20261027-062 | Treasury 10/22 NPRM under the ROAD to Housing Act: purchase restriction from 2027-01-07; large investor = control of ≥350 SF homes; BTR / renovate-to-rent / homeownership exceptions | Recorded as KB-HOMER-040: proposal, not a final blanket ban; statute effective date 2027-01-07; threshold is ≥350 (not >350) |

## B. Multifamily evidence (C2 neighbourhood) — retained with WALTER's limits

None of these is a C2 criterion input (C2 grades Trepp MF DQ and the GSE serious-DQ books only). They are realized-mark / maturity / counterevidence context for `MULTIFAMILY.tsv`.

| Signal | Kernel | Disposition |
|---|---|---|
| -031 Blackjack | Bisnow 10/20 (Morningstar Credit attribution): Blackstone Blackjack missed 10/09 maturity, special servicing; remaining $517.7M / 6 properties / 1,842 units after ~60% paydown of original $1.3B; analyst says cash flow exceeds underwriting | MULTIFAMILY row: **maturity/refinance case, not an income collapse**; $1.3B is NOT the current balance. Bradenton leg is CORAL's |
| -056 S2 Capital | S2 release (dated 10/13, posted 10/20): ~$1.2B / 26 properties / 8,223 units modified or refinanced; 12 foreclosure proceedings terminated; North Dallas 531-unit maturity waiver to 7/2031 | MULTIFAMILY row beside the July "$0 to LPs" fund row. **Counterevidence to a liquidation path for these assets**; not proof of LP recovery. Workout funded by a continuation vehicle |
| -045 CRED iQ | 10/15 model: $136B fixed-rate GSE/CMBS apartment loans maturing 10/2026–12/2028; 31% of balance needs $6.8B equity (2025 NOI, 1.25 DSCR, +25bp) | MULTIFAMILY row as **modelled future equity need, not defaults**. Park West Village mod (Nov-2025) is historical |
| -044 Denver | Trepp 10/20: Denver securitized MF watchlist $3.83B of $28.24B (13.6%) vs 1.13% DQ; 98% of watchlist current; $1.32B DSCR <1 | MULTIFAMILY row: watchlist ≠ delinquent; pre-default cash-flow pressure, same family as the 10/16 CRE CLO cohort |
| -043 Trepp correction | Trepp 10/20 corrects 10/16: a $1.3B seasoned pool skewed 2026 securitization stats; ex-pool MF LTV 67.4% vs 61% | KB note: 2026 MF securitization underwriting is NOT as conservative as first reported |
| -035 MSCI/Blackstone | Bisnow: MSCI distressed sales $13.2B 9M (+26.4%) vs non-distressed +50.3%; **MF distress sales +62.8%**; distress share 2.4% of volume; Blackstone opportunistic −3.2% QoQ | MULTIFAMILY row (attributed, MSCI tables unread). Distress dollars up, distress share down — neither measures the stock of troubled loans |
| -046 UDR–Apollo | UDR 10/21: JV 19 communities / 7,059 homes at ~$2B, implied ~6% cap; Apollo $1.34B equity for ~2/3; close expected 10/29 | MULTIFAMILY row: **a ~6% cap rate print on stabilized apartments** = a market-clearing price point, counterevidence to forced marks for core assets. Closing NOT yet established |
| -042 Concessions | RealPage Sept: incentives on 14.5% of stabilized units (17% May), avg 11.1% where offered; occupancy 95.2%; same-store effective rent +1.5% YoY. Apartment List new measure: 31.3% of properties ≥1 month free (25.4% yr ago). FL usage fell in 14 of 17 markets | MULTIFAMILY row. Three populations — RealPage stabilized units, Apartment List thresholded properties, Zillow listings (39.6%) — **never spliced**. Direction disagrees: RealPage breadth easing, Apartment List prevalence rising |
| -064 RealPage Q3 | Absorption ~304.8K vs completions ~318K (annual); occupancy 95.4%; effective rent +0.9% YoY; South negative | MULTIFAMILY row: supply still outrunning demand slightly; South (Sun Belt) rents negative — consistent with rent breadth 46/100 |
| -065 Sun Belt starts | M&M May 2026: MF starts ~75% below the 2022 peak (historical); CO 10/13 Sun Belt application | Context: future-delivery relief is a 2027–28 story, conditional on demand |
| -022 Seniors housing | Trepp 10/23: $2.24B / 156 seniors-housing loans maturing 11/2026–12/2027, 95% agency, 1.75% DQ | Logged; healthcare-adjacent, agency-performing. No MF row change |
| -033 Anecdote | Unnamed 150K-unit operator: "worst in 40 years" | INFO; confidence floor. Not relayed |
| -071 Lake Meadows | Investor suit vs Antheus over blocked exit (allegation) | INFO-logged; not a loan event |
| -059 RAD auction | 46 Philadelphia homes, bidding 10/13–15; outcome UNKNOWN | Logged, outcome UNKNOWN; no polling commissioned |
| -020 / -034 Trepp Q3 recap | Delinquent CMBS balance $48.65B (+11.64% YTD balance growth); SS transfers $24.38B vs resolutions $18.71B 9M; hard maturities $78.1B by end-2027 vs $61.1B calendar-2027 (different windows) | INFO; CREED-owned. No MF rate supplied; do not sum incompatible maturity totals |
| -036 Town Lane | $1.9B fund final close (commitments) | INFO; capital-availability counterexample, CREED |

## C. Florida / Texas / other

| Signal | Disposition |
|---|---|
| -042 (1022) Zillow FL drawdowns | Cape Coral metro −18.9% from peak, North Port −16.5%, Naples −11.9%, Miami −4.4% (Sept ZHVI). **Metro-level, HOMER may cite as sub-statewide**; consistent with ICE Cape Coral −16.5% drawdown (different index). Logged in STATE_HSG |
| -037 Sunbeam | INFO; CORAL owns |
| -069 FL leads | INFO; CORAL owns. Orlando MF construction −65.9% from 2023 peak noted as supply context |
| -026 Texas data centres | INFO; no housing channel |
| -052 OZK Culver City | INFO; REGINALD/OZK owns construction exposure |
| -007 Nashville resale / Goldman 2.2% negative equity | One resale −28% is an anecdote; the 2.2% negative-equity attribution lacks table/as-of. Consistent with HOMER's own arithmetic (KB-HOMER-021: buydowns do not create negative equity). Logged, not adopted as a figure |

**Count check:** 6 (A) + 16 rows in B covering 17 signals (-020 and -034 share a row) + 6 (C) = 29. ✅
