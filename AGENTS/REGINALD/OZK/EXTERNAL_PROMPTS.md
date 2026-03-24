# OZK External Research Prompts
**For Will to run on ChatGPT/Perplexity/Gemini**
**Generated:** 2026-03-24

Run these and drop results into `sources/`. I'll integrate.
**When results land → update STATUS.md "Research Agenda" checklist** (that's the single task tracker).

---

## 🔴 HIGH PRIORITY (This Week)

### PROMPT 1: Gleason's GFC Track Record (strongest bull counter — we need data)
```
Pull Bank of the Ozarks (now Bank OZK, FDIC CERT 110) quarterly financial data from 2007-2012. I need:
- Net charge-off rate by quarter
- Noncurrent loan ratio by quarter  
- CRE concentration ratio (CRE/total risk-based capital)
- Any FDIC enforcement actions during this period
- Total assets growth trajectory

Compare to peer regional banks that failed or were stressed during GFC. Did Bank of the Ozarks avoid losses while running high CRE concentration? This is critical — I need to understand if CEO George Gleason has genuinely navigated a severe CRE downturn before, or if his track record is untested.
```
**Save as:** `sources/OZK_GFC_TRACK_RECORD.md`

### PROMPT 2: Construction Loan Maturity Schedule
```
For Bank OZK (ticker OZK), I need their construction loan maturity schedule. Check:
1. The 2024 10-K (filed Feb 2026) — look for tables showing loan maturity by type, especially construction & land development
2. Q3 and Q4 2025 earnings call transcripts — any management commentary on construction loan maturity timing, paydown expectations, or "pipeline" rolling off
3. Any investor presentations from 2025-2026

Specifically: how much of their ~$7.8B construction book matures in each quarter of 2026? Is it front-loaded (Q1-Q2) or spread evenly? This determines whether the "maturity wall" is a cliff or a slope.
```
**Save as:** `sources/OZK_CONSTRUCTION_MATURITY_SCHEDULE.md`

### PROMPT 3: Interest Reserve Depletion Model
```
Bank OZK has $7.8B in construction loans, with 89.7% ($7.0B) on interest reserves. In Q4 2025, $108.6M in interest was capitalized (added to loan balances from reserves).

Help me model when these reserves deplete:
- Standard construction loan interest reserve = 12-24 months of interest at origination
- Most of these loans were originated in 2021-2022 (the $13.8B peak)
- Current weighted average rate on construction loans ~8-9%
- Construction terms are typically 36-42 months

Questions:
1. If a loan originated mid-2022 with an 18-month interest reserve, when does the reserve run out?
2. What percentage of OZK's construction book likely has DEPLETED reserves already?
3. When reserves deplete on a construction loan that hasn't stabilized, what happens mechanically? (Goes to cash-pay → borrower can't pay → nonaccrual?)
4. Is $108.6M/quarter in capitalized interest consistent with a book that still has healthy reserves, or does it suggest reserves are thinning?
```
**Save as:** `sources/OZK_INTEREST_RESERVE_MODEL.md`

### PROMPT 4: TDR / Loan Modification Data
```
Pull Bank OZK's troubled debt restructuring (TDR) and loan modification disclosures from their most recent 10-K (2024, filed Feb 2026) and 10-Q filings. Under ASC 326, look for:
- Total modified loans ($ amount and % of portfolio)
- Modifications by type (rate reduction, term extension, payment deferral, combination)
- Modified loans that subsequently defaulted (re-default rate)
- Any discussion of "financial difficulty" modifications

Also check FFIEC Call Report for OZK (RSSD 107244):
- RC-C Memoranda Item 1 (restructured loans)
- RC-N Memoranda (past due restructured loans)

Rising TDRs + flat NPLs = extend-and-pretend evidence at the institution level.
```
**Save as:** `sources/OZK_TDR_MODIFICATIONS.md`

### PROMPT 5: Current Short Interest
```
What is the current short interest for Bank OZK (ticker: OZK)?
- Shares short
- Short interest as % of float
- Days to cover
- Most recent reporting date
- Trend over last 3 months (increasing or decreasing?)
- Compare to WAL, ZION, FLG short interest levels

Sources: FINRA short interest data, Ortex, S3 Partners, or any recent financial coverage.
```
**Save as:** `sources/OZK_SHORT_INTEREST_CURRENT.md`

---

## 🟠 MEDIUM PRIORITY (Before Apr 10)

### PROMPT 6: Life Sciences Vacancy Q1 2026
```
What are the current (Q1 2026) life sciences / lab space vacancy rates for:
1. San Diego overall
2. Sorrento Mesa submarket specifically
3. South San Francisco / Bay Area (for comparison)

Sources: CBRE, JLL, Cushman & Wakefield quarterly reports. 

Also: any recent news about life sciences lab space demand trends in early 2026? Are pharma/biotech companies still downsizing lab footprints or has demand stabilized?
```
**Save as:** `sources/LIFE_SCI_VACANCY_Q1_2026.md`

### PROMPT 7: Peer ACL/NCO Comparison Table
```
Build a comparison table of CRE-heavy regional banks using Q4 2025 data:

Banks: OZK, WAL (Western Alliance), ZION (Zions), COLB (Columbia Banking), FNB Corp, EWBC (East West Bancorp), HBAN (Huntington), TFC (Truist)

For each bank, pull:
- Total CRE / Total Risk-Based Capital ratio
- Construction & Development / Total Risk-Based Capital
- Allowance for Credit Losses (ACL) as % of total loans
- Net Charge-Off rate (annualized)
- Noncurrent loan ratio
- ACL / Noncurrent coverage ratio

Rank by CRE concentration. Highlight where OZK is an outlier.
```
**Save as:** `sources/OZK_PEER_COMP_Q4_2025.md`

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

### PROMPT 13: Peer 2022 Vintage Maturity Wall — Same Pattern?
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

### PROMPT 14: OZK Options Implied Move vs Historical Earnings Moves
```
For Bank OZK (ticker OZK) earnings on April 16, 2026:

1. What is the current options-implied move for earnings? (straddle price / stock price for the nearest weekly expiry)
2. What have OZK's actual earnings-day moves been for the last 8 quarters? (date, direction, magnitude)
3. How often has OZK exceeded the implied move? (beat rate)
4. What is the current IV rank / IV percentile for OZK options?
5. For the Aug 2026 $42.50 and $45 puts specifically — what's the current delta, IV, and open interest?

Context: I hold Aug $42.50 and $45 puts. I need to know if the market is already pricing in a large move (high IV = thesis partially priced) or if options are cheap relative to the actual risk (low IV = opportunity). This directly affects whether to add, hold, or trim into earnings.
```
**Save as:** `sources/OZK_OPTIONS_IMPLIED_MOVE.md`

---

*After running, drop files in `AGENTS/REGINALD/OZK/sources/`. I'll integrate into KB.tsv and update the thesis.*
