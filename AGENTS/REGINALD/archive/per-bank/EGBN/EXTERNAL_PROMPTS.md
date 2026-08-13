# EGBN External Research Prompts
**For Will to run on ChatGPT/Perplexity/Gemini/Claude Deep Research**
**Created:** 2026-04-07

Run these and drop results into `sources/`. REGINALD will integrate into KB.tsv.

---

## ✅ COMPLETED

| # | Topic | KB Rows | Notes |
|---|-------|---------|-------|
| — | Web search baseline (Apr 7) | KB-EGBN-013→018 | Q4 earnings, insider, consensus, DOGE, CEO transition |

---

## 🔴 HIGH PRIORITY — Before Apr 22

### PROMPT 1: EGBN Q4 2025 Earnings Call Deep Dive + DOGE Impact Assessment
```
Eagle Bancorp (EGBN, NASDAQ) is a $10.5B community bank headquartered in Bethesda, MD, with 100% geographic concentration in the DC/MD/VA metro area. They reported Q4 2025 earnings on January 21-22, 2026 (EPS $0.25, beating consensus of -$0.12).

I need a detailed analysis of the Q4 2025 earnings call transcript (January 22, 2026). Specifically:

1. DOGE / Federal Layoff Commentary:
   - What exactly did management say about DOGE, federal workforce reductions, or government contractor clients?
   - CFO Eric Newell reportedly said GovCon line-of-credit usage declined 30% — what was the full context?
   - Any mention of DC metro office vacancy, federal tenant departures, or GSA lease cancellations?
   - Did any analyst ask about DOGE exposure? What was the response?

2. CRE Portfolio Detail:
   - CRE concentration is 547% of Tier 1 Capital (#3 nationally). What did they say about reducing this?
   - Office exposure is down 41% from peak — what's the current $ amount and where are the remaining office loans?
   - Any specific troubled credits discussed? Any new nonaccruals or charge-offs beyond the Q3 $140.8M?
   - Construction/ADC exposure detail — are they still originating or winding down?

3. CEO Transition:
   - Susan Riel announced retirement in November 2025. What's the search status for a successor?
   - Any timeline given for transition?
   - Who is running day-to-day operations? Who spoke on the call?

4. Forward Guidance:
   - NIM guidance of 2.6-2.8% for 2026 — what assumptions underpin this?
   - Provision outlook — was the Q3→Q4 drop ($113.2M→$15.5M) described as normalization or one-time?
   - Deposit strategy — the core +$692M / brokers -$602M shift was positive. Is this intentional?
   - Any mention of capital raise, dividend restoration, or share buyback?

5. AOCI / Unrealized Losses:
   - What is EGBN's AFS/HTM portfolio composition?
   - Any mention of the AOCI capital rewrite (Fed/FDIC/OCC rule, comment period closes Jun 18)?
   - Unrealized loss position on securities?

Context: EGBN is our "crisis-in-progress" thesis. 100% DC geographic exposure + 547% CRE concentration + DOGE federal layoffs = three independent stress vectors on one bank. Q4 was a recovery quarter but Q1 2026 is when DOGE impact should show up in the numbers.
```
**Save as:** `sources/EGBN_Q4_EARNINGS_CALL_ANALYSIS.md`

### PROMPT 2: DC Metro Commercial Real Estate — Q1 2026 Conditions
```
What are the current (Q4 2025 or Q1 2026) commercial real estate market conditions in the Washington DC metro area?

Specifically:
1. Office vacancy rate — overall, Class A, and Class B
   - Trend direction (rising/falling/stable?)
   - How does current vacancy compare to pre-COVID and GFC peaks?
   - Are federal agencies reducing footprint? Any GSA lease non-renewals or cancellations?

2. DOGE impact on DC CRE:
   - Have federal workforce reductions (DOGE, 307K+ confirmed layoffs nationally) visibly impacted DC office demand?
   - Any specific buildings or submarkets losing federal tenants?
   - Government contractor office demand — are contractors subleasing or downsizing?

3. Multifamily conditions in DC metro:
   - Vacancy rates, rent growth trends
   - New supply pipeline — is there oversupply?
   - Any connection between federal layoff corridors (NoVA, Bethesda, Silver Spring) and multifamily stress?

4. Construction lending conditions:
   - Are DC-area banks pulling back on construction lending?
   - Any construction projects stalling or being cancelled?
   - Impact of higher rates + federal uncertainty on new development

5. Suburban vs urban dynamics:
   - Is stress concentrated in downtown DC or spreading to Bethesda/Tysons/Arlington/Silver Spring?
   - Which submarkets have the highest vacancy?

Sources: CBRE, JLL, Cushman & Wakefield quarterly reports, CoStar, Moody's Analytics CRE.

Context: Eagle Bancorp (EGBN) has 100% geographic concentration in DC metro, 547% CRE/Tier 1 capital, and 10.9% office CRE exposure. Understanding whether DC CRE is improving or deteriorating in Q1 2026 directly determines our thesis.
```
**Save as:** `sources/DC_METRO_CRE_Q1_2026.md`

### PROMPT 3: EGBN Sell-Side Coverage + M&A Assessment
```
Eagle Bancorp (NASDAQ: EGBN) — I need a comprehensive analysis of:

PART A — Sell-Side Coverage:
1. How many analysts currently cover EGBN? List each with rating and price target.
2. Any rating changes in the last 6 months?
3. What are consensus EPS estimates for Q1 2026 and full-year 2026?
4. Any notable analyst commentary about DOGE risk, DC CRE exposure, or the CEO transition?

PART B — M&A Assessment:
1. Is EGBN considered a potential acquisition target? Any analyst or media speculation?
2. Atlantic Union Bankshares (AUB) acquired Sandy Spring Bancorp in 2025. Could AUB or another regional acquirer target EGBN?
3. What would an acquirer get? ($10.5B assets, DC franchise, government contractor relationships)
4. What would an acquirer inherit? (547% CRE concentration, CEO vacancy, DOGE exposure, $0.01 dividend)
5. Precedent transactions — what multiples have DC-area community banks been acquired at in the last 2 years?
6. Is EGBN more likely to be acquired or to continue as a standalone turnaround?

PART C — AUB Relative Comparison:
1. AUB vs EGBN — key financial metrics side by side (CRE concentration, ROA, NPA, capital ratios, deposit trends)
2. AUB successfully de-risked by selling $2B CRE to Blackstone. Could EGBN replicate this?
3. Is there a long AUB / short EGBN pairs trade opportunity?

Context: EGBN is a pure DC play in crisis. $25P Jun position. The M&A floor is both the biggest risk to the short thesis and the most important question to answer before earnings.
```
**Save as:** `sources/EGBN_SELLSIDE_AND_MA.md`

### PROMPT 4: EGBN Government Contractor Lending — DOGE Exposure Detail
```
Eagle Bancorp (EGBN) has a Government Contractor lending division. I need specifics:

1. How large is the GovCon lending book? (total $ amount, % of total loans)
2. What types of government contractors does EGBN lend to? (defense, IT, professional services, construction?)
3. Which federal agencies are the primary end-clients of EGBN's GovCon borrowers?
4. Has DOGE (Department of Government Efficiency) targeted any agencies that are major clients of DC-area government contractors?
5. What is the typical loan structure for GovCon lending? (revolving lines, term loans, receivables financing?)
6. Are there any public reports of government contractors in the DC area facing financial stress from DOGE budget cuts, contract cancellations, or delayed payments?
7. How does EGBN's GovCon exposure compare to other DC-area banks (AUB, BHRB)?
8. On the Q4 2025 earnings call, CFO Eric Newell said GovCon LOC usage declined 30% — is declining LOC usage a bullish signal (less need to borrow) or bearish (contractors pulling back, activity slowing)?

Context: EGBN has 100% DC geographic exposure. The government contractor lending division is a key differentiator but also a concentrated risk if DOGE continues reducing the federal workforce and cancelling contracts. 307K+ federal layoffs confirmed nationally, with DC metro bearing the heaviest impact.
```
**Save as:** `sources/EGBN_GOVCON_DOGE_ANALYSIS.md`

---

## 🟡 NICE TO HAVE

### PROMPT 5: EGBN MI3 Trend + AOCI Exposure
```
For Eagle Bancorp (EGBN, FDIC CERT ?, RSSD ?):

1. Pull the Memo Item 3 / C&I ratio from FFIEC Call Reports for the last 4 quarters (Q1 2025 through Q4 2025). Is the 23.7% ratio stable, rising, or falling?
2. What is EGBN's AFS (Available for Sale) securities portfolio size and unrealized loss position?
3. What is the HTM (Held to Maturity) portfolio size and unrealized loss?
4. Is EGBN classified as Category III or IV for the proposed AOCI capital rewrite?
5. What would the estimated CET1 impact be if AOCI were fully included in capital?

Context: The AOCI capital rewrite (Fed/FDIC/OCC, comment period closes Jun 18, 2026) would force Cat III/IV banks to include unrealized securities losses in capital. For a bank with 547% CRE concentration and a $0.01 dividend, an AOCI capital hit could push capital ratios toward regulatory action thresholds.
```
**Save as:** `sources/EGBN_MI3_AOCI_DETAIL.md`

---

*After running, drop files in `AGENTS/REGINALD/EGBN/sources/`. REGINALD will integrate into KB.tsv.*
