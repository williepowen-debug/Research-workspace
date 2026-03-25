# OZK External Research Prompts
**For Will to run on ChatGPT/Perplexity/Gemini/Claude**
**Updated:** 2026-03-24 (evening)

Run these and drop results into `sources/`. Prome will integrate into KB.tsv.

---

## ✅ COMPLETED

| # | Topic | KB Rows | Notes |
|---|-------|---------|-------|
| 1 | Gleason GFC track record | KB-064/065/066 | 4 LLMs, fully integrated |
| 2 | Construction loan maturity schedule | KB-074–079 | 4 LLMs, fully integrated |
| 3 | Interest reserve depletion model | KB-080/081/088–093 | 4 LLMs, 6 rows |
| 5 | Geographic deep dive (V1–V4) | KB-107–120 | 4 LLMs, 14 rows, EXPOSURE_MAP built |
| 4 | TDR/loan modifications | KB-096–106 | 4 LLMs, 11 rows. 590 mods, 98% classification gap, 59% re-default |
| 6 | FL Paradox stress-test | KB-121–132 | 4 LLMs, 12 rows, FINDINGS.md complete |
| 7 | Peer ACL/NCO comparison | KB-133–136 | 3 LLMs (Claude best), 4 rows. OZK outlier on every metric |
| 15 | IQHQ RaDD leasing + distress | KB-137–141 | Claude + Gemini. 3.3% leased, maturity to Aug 2028, IQHQ in distress cascade |
| 20 | Life sci vacancy deep dive | KB-147–156 | Claude. National 23.0% (first decline), SD 26-31%, Sorrento 38.2%, Boston ATH 28.0%, Bay Area 30.2% (first recovery), 18.7M SF must exit by 2030 |
| 16 | Insider transactions | KB-142–146 | Claude + Gemini. Zero buys 18mo, 65:1 sell ratio, CRO filled (Majumdar), CIK corrected |

---

## 🟠 MEDIUM PRIORITY — Before Apr 10

### PROMPT 8: Metropolitan Capital Bank Failure Comparison
```
Metropolitan Commercial Bank (FDIC CERT ?) failed on January 30, 2026. Pull:
- Pre-failure metrics: CRE concentration, ACL ratio, noncurrent ratio, Memo Item 3 / C&I ratio
- Cause of failure per FDIC
- Total assets at failure
- Estimated loss to DIF
- Any FDIC Material Loss Review published yet?

Compare to Bank OZK's current metrics side by side. How close is OZK to Metropolitan's failure profile?

Note: Metropolitan had a Memo Item 3 / C&I ratio of 39.6% (vs OZK's 37.6%).
```
**Save as:** `sources/METROPOLITAN_FAILURE_COMPARISON.md`

### PROMPT 9: Affinius Capital Bond Details
```
Affinius Capital (formerly USAA Real Estate, San Antonio TX) — I need details on their bond/debt situation:
- Total outstanding bonds/notes
- Current trading prices (any TRACE data?)
- Maturity dates (specifically anything maturing Oct 2026)
- Credit ratings
- Any recent news about financial stress, asset sales, or restructuring

Context: Affinius is Bank OZK's most frequent co-lending partner on construction loans (7+ deals identified). If Affinius faces liquidity stress, it directly threatens OZK's ability to refinance construction loans at maturity.
```
**Save as:** `sources/AFFINIUS_CAPITAL_BONDS.md`

### PROMPT 10: Sell-Side Consensus
```
What is the current sell-side analyst consensus on Bank OZK (ticker OZK)?
- Number of Buy / Hold / Sell ratings
- Average price target vs current price
- Most recent rating changes (last 3 months)
- Any notable analyst commentary on CRE risk or construction exposure

Specifically: did Citi maintain their Sell rating from May 2024? Any other downgrades?
```
**Save as:** `sources/OZK_SELLSIDE_CONSENSUS.md`

### PROMPT 13: Peer 2022 Vintage Maturity Wall
```
Several regional banks had heavy construction lending in 2021-2022. I want to know if other banks with large 2022 construction vintages are showing the same noncurrent step-up pattern as Bank OZK.

Check Q3-Q4 2025 FDIC data for these CRE-heavy construction lenders:
- Glacier Bancorp (GBCI)
- Pacific Premier (PPBI)  
- Banc of California (BANC)
- Customers Bancorp (CUBI)
- Any other banks known for large construction books in 2022

For each: 
1. Construction & development loan balances (2022 peak vs current)
2. Noncurrent loan trend Q1 2025 → Q4 2025
3. NCO rate trend over same period
4. Any management commentary about 2022 vintage performance

If multiple banks show the same noncurrent step-up on 2022 vintages, it confirms OZK's pattern is systemic (maturity wall), not idiosyncratic (bad underwriting). If OZK is an outlier, that's worse — means their specific book is impaired.
```
**Save as:** `sources/PEER_2022_VINTAGE_COMPARISON.md`

### PROMPT 19: CRE Market Conditions by OZK Metro
```
For Bank OZK's top 10 metro exposures, pull current (Q4 2025 or Q1 2026) commercial real estate market conditions:

Metros (ranked by OZK exposure):
1. South Florida / Miami ($7.45B, 23%)
2. New York City ($4.2B, 13%)
3. San Diego ($1.4B, 4.3%)
4. Dallas-Fort Worth ($1.2B, 3.7%)
5. Atlanta ($1.1B, 3.4%)
6. Boston ($700M+)
7. Seattle ($235M+)
8. Chicago ($200M residual)
9. Los Angeles ($140M+)
10. Baltimore ($253M — single project: Peninsula)

For each metro, I need:
- Office vacancy rate (overall + Class A)
- Multifamily vacancy rate + rent growth trend
- Cap rate trend (current vs 2022 origination-era)
- Net absorption (positive or negative last 2 quarters)
- Construction pipeline (sqft under construction)
- Any notable distressed sales or foreclosures in Q1 2026

Sources: CBRE, JLL, Cushman & Wakefield, CoStar quarterly reports, or Moody's Analytics CRE data.

Key question: In which of these metros are market conditions WORSE than at origination (2021-2022)? Where cap rates have expanded most = where OZK's LTVs have deteriorated most.
```
**Save as:** `sources/OZK_METRO_MARKET_CONDITIONS.md`

### PROMPT 20: Life Sciences Vacancy Deep Dive (SD + National)
```
What are the current (Q1 2026) life sciences / lab space vacancy rates for:
1. San Diego overall
2. Sorrento Mesa submarket specifically
3. South San Francisco / Bay Area (for comparison)
4. Boston/Cambridge (for comparison)

Sources: CBRE, JLL, Cushman & Wakefield quarterly reports.

Also: any recent news about life sciences lab space demand trends in early 2026? Are pharma/biotech companies still downsizing lab footprints or has demand stabilized? Any notable lease signings or move-outs in SD specifically?

Context: OZK has ~$1.4B in San Diego life sciences exposure including the $915M IQHQ RaDD project. Sorrento Mesa vacancy was 30%+ as of mid-2025. If vacancy is still rising, the maturity wall on these loans becomes a cliff.
```
**Save as:** `sources/LIFE_SCI_VACANCY_Q1_2026.md`

---

## 🟡 NICE TO HAVE

### PROMPT 11: FHLB Dallas Advance Rates
```
What are FHLB Dallas's current advance rates and eligible collateral policies for:
- Construction loans (are they eligible collateral at all?)
- CRE loans (haircut percentages)
- Any recent policy changes to collateral eligibility

Context: OZK has $23.9B in pledged loans (74% of book) with $8.8B FHLB capacity. If FHLB tightens collateral standards on construction loans, OZK's liquidity buffer could shrink significantly.
```
**Save as:** `sources/FHLB_DALLAS_ADVANCE_RATES.md`

### PROMPT 12: OZK Buyback Activity
```
Bank OZK authorized a $200M stock buyback program in July 2024. As of Q3 2024, only $460K (0.2%) had been used.

Check: has OZK repurchased any additional shares in Q4 2025 or Q1 2026? Look at:
- 10-K buyback disclosure
- Any 8-K filings related to repurchase activity
- Earnings call commentary on capital return strategy

A bank with $200M buyback authority that refuses to buy its own stock at 52-week lows is a powerful signal.
```
**Save as:** `sources/OZK_BUYBACK_ACTIVITY.md`

### PROMPT 14: Options Implied Move for Apr 16
```
For Bank OZK (ticker OZK) earnings on April 16, 2026:

1. What is the current options-implied move for earnings? (straddle price / stock price for the nearest weekly expiry)
2. What have OZK's actual earnings-day moves been for the last 8 quarters? (date, direction, magnitude)
3. How often has OZK exceeded the implied move? (beat rate)
4. What is the current IV rank / IV percentile for OZK options?
5. For the Aug 2026 $42.50 and $45 puts specifically — what's the current delta, IV, and open interest?

Context: I hold Aug $42.50 and $45 puts. I need to know if the market is already pricing in a large move (high IV = thesis partially priced) or if options are cheap relative to the actual risk (low IV = opportunity).
```
**Save as:** `sources/OZK_OPTIONS_IMPLIED_MOVE.md`

### PROMPT 17: State-Level CRE Noncurrent Breakdowns
```
From FDIC Call Report data (FFIEC CDR), pull Bank OZK's (RSSD ID: 107244, FDIC CERT: 110) loan quality data broken down by state or FDIC supervisory region.

Specifically looking for:
1. Schedule RC-C Part II — Loans to Small Businesses and Small Farms, broken by state
2. Any geographic concentration disclosures in the 10-K (Section: Credit Risk — Geographic)
3. FDIC Summary of Deposits data — branch footprint vs lending footprint mismatch
4. State-level noncurrent rates if available in public filings

Key question: OZK lends nationally from an Arkansas charter but has branches in only ~8 states. Which states have the highest noncurrent rates on OZK's book?
```
**Save as:** `sources/OZK_STATE_NONCURRENT_BREAKDOWN.md`

### PROMPT 18: $13.8B 2022 Origination Verification
```
Verify Bank OZK's 2022 loan origination volume. Multiple sources cite approximately $13.8B in new loan originations during 2022 (their peak year).

Check:
1. 2022 10-K (filed Feb 2023) — loan origination/production tables
2. Q4 2022 earnings call transcript — management commentary on origination volume
3. Any investor presentations from 2022-2023 citing annual production figures
4. FDIC Call Report: compare total loans Dec 2021 vs Dec 2022

Key data points needed:
- Gross origination volume for full year 2022
- Breakdown by loan type (construction vs permanent vs C&I)
- Average loan size for 2022 vintage
- How this compares to 2021 and 2023 origination (was 2022 truly the peak?)

Context: If 2022 originations were truly $13.8B with 36-42 month construction terms, most of that vintage matures in H1-H2 2026. This is the "maturity wall" thesis.
```
**Save as:** `sources/OZK_2022_ORIGINATION_VERIFICATION.md`

---

*After running, drop files in `AGENTS/REGINALD/OZK/sources/`. Prome will integrate into KB.tsv and update the research agenda.*
