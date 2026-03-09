# PROMPTS.md — Research Prompts for Will

Prompts for Will to run through external LLMs (Gemini, Perplexity, ChatGPT, etc.).
These are standalone prompts — no internal system knowledge required by the LLM.
Prome adds prompts here; Will picks them up and runs them; results come back for integration.

---

## Meta-Prompts (Reusable)

### 🔑 "What Should I Be Asking You?"
*Use when you have a lot of signals but need to prioritize research direction. Works with any LLM or agent system.*
```
Based on everything in our current data — positions, thesis, signals, 
and what just happened in the market — give me your top 5 prompts 
that I should be giving you right now. 

For each prompt:
1. The exact question I should ask
2. WHY you need this answered (what gap does it fill?)
3. What decision it unlocks (position sizing, entry/exit, thesis 
   confirmation or kill)

Prioritize by: what's most likely to change what we do tomorrow.
```
*Origin: Mar 9, 2026 — Will realized this inverts the research process. Instead of human guessing what to ask, the system identifies its own blind spots. Works best after a batch of new signals when direction is unclear.*

---

## Queued

### Google Trends — Labor Search Terms
**Priority:** 🟡 | **Routes to:** LABOR
**⚠️ WILL MUST DO MANUALLY** — LLMs cannot access real-time Google Trends data. Go to trends.google.com directly.
```
Go to Google Trends (trends.google.com) and look up US search interest 
(past 90 days) for these terms:

1. "unemployment benefits"
2. "file for unemployment"
3. "laid off"
4. "severance package"
5. "hiring freeze"
6. "food stamps" / "SNAP benefits"
7. "job openings near me"

For each: current week's index (0-100), 4-week average, 90-day trend 
(rising/flat/declining), any spikes in the past 30 days. Compare to the 
same period in 2025 and 2024 if possible. Flag any breakout patterns.
```

---

### Taiwan LNG Reserves and Power Supply Status
**Priority:** 🔴 CRITICAL | **Routes to:** HAWK, HENRY
```
What is the current status of Taiwan's natural gas reserves and power 
supply as of March 9-10, 2026?

1. How many days of LNG reserves does Taiwan currently hold? What is 
   the normal buffer level?
2. Has Taiwan's state power company (Taipower) issued any rationing 
   notices, emergency procurement orders, or public statements about 
   supply concerns since the Strait of Hormuz closure began in early 
   March 2026?
3. What percentage of Taiwan's LNG imports transit the Strait of 
   Hormuz or originate from Qatar and the UAE?
4. Are there any reports of industrial power curtailment affecting 
   semiconductor manufacturing (TSMC, UMC, or other fabs)?
5. Has Taiwan activated emergency energy protocols or sought 
   alternative LNG supply from the US, Australia, or other sources?
6. What are analysts or government officials saying about the timeline 
   before reserves become critically low?

Cite all sources with dates. Focus on information from the past 7 days.
```

---

### Oil at $100 — Downstream Economic Impact
**Priority:** 🔴 | **Routes to:** HAWK, CARL, LABOR
```
With WTI crude oil above $100/barrel as of March 9, 2026, driven by 
the Hormuz Strait closure and Iraqi production disruption, provide a 
current snapshot of downstream economic impacts:

1. US national average gasoline price — most recent data from AAA 
   or GasBuddy. How does this compare to one month ago?
2. Diesel and ultra-low sulfur diesel (ULSD) rack prices — trend 
   over the past 7 days
3. Jet fuel spot price (Gulf Coast or NY Harbor) — current level 
   vs 30 days ago, and percentage change
4. Have any major US airlines announced fuel surcharges, route 
   cuts, or capacity reductions since March 1, 2026?
5. Have any major trucking or freight companies announced fuel 
   surcharges or service changes?
6. Fertilizer prices (urea, DAP, potash) — current vs pre-Hormuz 
   closure levels
7. US Strategic Petroleum Reserve — any announced or rumored 
   releases? What is the current SPR inventory level?

Cite sources with dates. Focus on data from the past 7 days only.
```

---

### Kennedy-Wilson Holdings Debt Exchange Status
**Priority:** 🟠 | **Routes to:** REGINALD
```
What is the current status of Kennedy-Wilson Holdings' (ticker: KW) 
debt exchange offer as of early March 2026?

1. What were the terms of the exchange offer — what did KW propose 
   to bondholders?
2. Have any bondholder groups publicly rejected or pushed back on 
   the exchange?
3. What are the key deadlines, court dates, or expiration dates 
   for the offer?
4. What is KW's current credit rating, and have any rating agencies 
   taken action recently?
5. What is the total debt outstanding and maturity schedule?
6. Are there other commercial real estate (CRE) companies currently 
   facing similar bondholder resistance to debt restructuring or 
   exchange offers? If so, list them with details.

Cite sources with dates.
```

---

### ✅ Hormuz Closure Impact on Global Fertilizer Supply — COMPLETED
**Completed:** Mar 9 via Gemini. IFPRI: "rival or exceed 2022." 280 vessels confirmed trapped. 91% transit reduction. India 75% urea from GCC. Arkansas stopped quoting prices.
**Routes to:** HAWK, CARL — signals already routed.
```
Assess the impact of the Strait of Hormuz closure (since approximately 
March 1, 2026) on the global fertilizer market:

1. What percentage of global urea, DAP (diammonium phosphate), and 
   potash exports normally transit the Strait of Hormuz?
2. Which countries are the largest Gulf-origin fertilizer exporters, 
   and who are their primary customers?
3. How dependent is India on Gulf-origin nitrogen fertilizers? What 
   percentage of India's fertilizer imports come through Hormuz?
4. What are current urea and DAP spot prices compared to pre-closure 
   levels (late February 2026)?
5. Have any major importing countries (India, Brazil, Southeast Asia) 
   announced emergency procurement, rationing, or subsidy changes?
6. What is the timeline pressure for Northern Hemisphere spring 
   planting — by when must fertilizer be procured and applied to 
   avoid crop yield impacts?
7. Reports suggest approximately 280 dry bulk carriers may be 
   trapped or rerouted — is there confirmation of shipping 
   disruption affecting agricultural commodity transport?

Cite sources with dates. This is a second-order economic effect of 
the Hormuz closure that may not be receiving mainstream attention.
```

---

### BlackRock HLEND Redemption Gate — Private Credit Contagion
**Priority:** 🟠 | **Routes to:** BROCK
```
BlackRock's HLEND private credit fund (~$26B AUM) reportedly gated 
redemptions around March 6, 2026, paying only a portion of total 
redemption requests. Provide a comprehensive update:

1. Has BlackRock issued any public statement about HLEND's 
   redemption situation since the gate was imposed?
2. Have any OTHER private credit funds announced redemption limits, 
   gates, or liquidity restrictions since early March 2026? List 
   each with fund name, manager, AUM, and details.
3. What is the current status of Blackstone's BCRED fund — are 
   they still honoring full redemption requests?
4. What is the status of Blue Owl Capital's OCSL II fund — has 
   the liquidity restriction changed?
5. Have any Business Development Companies (BDCs) announced 
   dividend cuts or NAV markdowns in the past two weeks?
6. Has the SEC or any financial regulator commented publicly on 
   private credit fund liquidity or gating?
7. What are the total reported redemption requests across the 
   major non-traded private credit funds (BCRED, HLEND, OCSL, 
   others) for Q1 2026?

Cite sources with dates. Focus on events since March 1, 2026.
```

---

### Fertilizer Trade — CF Industries / Mosaic / Nutrien Analysis
**Priority:** 🔴 | **Routes to:** HAWK, HENRY
```
The Strait of Hormuz has been closed since approximately March 1, 2026, 
disrupting oil AND dry bulk shipping from the Persian Gulf. Several Gulf 
nations (Saudi Arabia, Qatar, UAE, Oman, Iran) are major fertilizer 
exporters, particularly nitrogen-based fertilizers (urea, ammonia) and 
phosphate (DAP). Analyze the fertilizer investment thesis:

1. What percentage of global urea production and exports comes from 
   Gulf states that ship through Hormuz? Break down by country.
2. What percentage of global DAP/MAP (phosphate) production ships 
   through Hormuz?
3. Current spot prices for urea (Yuzhny, Middle East, US Gulf), 
   DAP, and ammonia — current levels vs February 2026 (pre-closure). 
   What is the percentage change?
4. CF Industries (CF): What percentage of their revenue comes from 
   nitrogen products? What is their production capacity vs Gulf 
   competitors now offline? How much do they benefit from higher 
   global nitrogen prices? Recent earnings, guidance, analyst targets.
5. Mosaic (MOS): Exposure to phosphate price increases. Production 
   breakdown. Recent earnings and guidance. How much Gulf phosphate 
   disruption benefits them?
6. Nutrien (NTR): Production mix (potash/nitrogen/phosphate). How 
   exposed to Gulf disruption vs potash-driven? Recent earnings.
7. Historical precedent: What happened to US fertilizer stocks 
   during the 2022 Russia-Ukraine conflict when Russian/Belarusian 
   fertilizer exports were sanctioned? What were the returns for 
   CF, MOS, and NTR from Feb-Jun 2022?
8. Current options market: What is implied volatility on CF, MOS, 
   and NTR options? Are call premiums elevated or still cheap?
9. Timing risk: When does the Northern Hemisphere spring planting 
   window close? If fertilizer isn't applied by [date], what is 
   the crop yield impact?
10. What is the bear case — could US domestic production or 
    non-Gulf imports (Russia via Pacific, Morocco phosphate) fill 
    the gap quickly?

Cite sources with dates.
```

---

### Fertilizer Supply Chain — Deep Dive on Gulf Dependency
**Priority:** 🟠 | **Routes to:** HAWK, CARL
```
Provide a detailed analysis of global fertilizer supply chain 
dependency on the Persian Gulf and Strait of Hormuz:

1. Map the top 10 global urea exporters by volume (million metric 
   tons/year). For each, state whether exports transit Hormuz.
2. Map the top 10 global DAP/phosphate exporters similarly.
3. What is the current global urea inventory level vs historical 
   average? Are inventories lean or well-stocked heading into 
   spring 2026?
4. India imports roughly what percentage of its fertilizer needs? 
   What percentage comes from Gulf sources? Has India announced 
   any emergency tenders or strategic reserve releases since 
   March 1, 2026?
5. Brazil's upcoming planting season (safrinha) — what is their 
   Gulf fertilizer dependency and timeline pressure?
6. How long can global fertilizer markets sustain a Hormuz closure 
   before physical shortages materialize at the farm level? 
   Estimate in weeks.
7. Are there any reports of fertilizer cargo ships being rerouted 
   around Africa (Cape of Good Hope)? What does the additional 
   transit time do to delivery schedules and spot prices?
8. US domestic fertilizer production capacity — what percentage 
   of US farmer needs can be met domestically without any imports?
9. Have any US farm cooperatives, ag retailers, or state 
   agriculture departments issued warnings or guidance about 
   fertilizer availability for spring 2026?
10. What happened to global food prices (wheat, corn, rice, 
    soybeans) when fertilizer prices spiked in 2022? What is the 
    transmission lag from fertilizer price to food price?

Cite sources with dates. Focus on actionable data for evaluating 
an investment in US-based fertilizer producers.
```

---

### Subprime Auto ABS Performance Data
**Priority:** 🟡 | **Routes to:** CARL, OTTO
```
Provide the most recent auto loan asset-backed securities (ABS) 
performance data, likely from January or February 2026 remittance 
reports:

1. Subprime auto 60+ day delinquency rate — Fitch composite index 
   or S&P tracking. What is the current level and YoY change?
2. Prime auto 60+ day delinquency rate for comparison
3. Subprime auto ABS annualized net loss rate — current vs 6 and 
   12 months ago
4. Recovery rates on repossessed vehicles — current level vs 12 
   months ago. Are recoveries improving or declining?
5. Have any new subprime auto ABS deals been priced in February 
   or March 2026? If so, what were the subordination levels 
   compared to 2024 and 2025 vintage deals?
6. Are there any specific ABS trusts (particularly those backed 
   by Carvana/DriveTime originations) with recent trustee reports 
   or rating actions?
7. What is the current average auto loan term for new subprime 
   originations, and what percentage of new loans have negative 
   equity at origination?

The context is that Fitch reported subprime auto 60+ day delinquencies 
hit an all-time record of approximately 7.1% in early 2026. We need 
to understand the trend trajectory, not just the headline level.
```

---

### Japan FY2026 Budget and JGB Issuance Schedule
**Priority:** 🟠 | **Routes to:** SAM, ZHAO
```
Japan's new Prime Minister Sanae Takaichi passed a ¥122 trillion 
FY2026 budget, the largest in Japanese history, with an LDP 
supermajority in the Diet. Provide details on:

1. What is the total planned Japanese Government Bond (JGB) 
   issuance for FY2026 (April 2026 - March 2027)? How does this 
   compare to FY2025?
2. What is the breakdown of planned issuance by maturity bucket 
   (2Y, 5Y, 10Y, 20Y, 30Y, 40Y)?
3. What is the Ministry of Finance (MoF) JGB auction calendar 
   for April through June 2026?
4. Has the Bank of Japan (BOJ) signaled any changes to its JGB 
   purchase tapering plan in response to the larger budget?
5. What percentage of JGB issuance is the BOJ currently absorbing 
   through its purchasing program?
6. What are analysts saying about the impact of increased JGB 
   supply on long-end yields (20Y, 30Y)? Any specific yield 
   forecasts for Q2-Q3 2026?
7. How is the market pricing the combination of Takaichi's fiscal 
   expansion and BOJ monetary policy — any notable moves in JGB 
   futures or USD/JPY forward rates?

USD/JPY is currently around 158.60 and JGB 10Y yield is approximately 
2.22%. Cite sources with dates.
```

---

### MFS (Motor Finance Specialist UK) Fraud — Full Exposure Map
**Priority:** 🟠 | **Routes to:** OTTO, BROCK
```
Provide a comprehensive map of financial institution exposure to the 
MFS (Motor Finance Specialist) fraud in the United Kingdom, which 
involves alleged double-pledging of vehicle collateral across multiple 
lenders and securitization vehicles. As of March 2026:

1. List every financial institution with confirmed or reported 
   exposure to MFS, including: institution name, confirmed exposure 
   amount (£), type of exposure (direct lending, SPV participation, 
   warehouse facility), and source/date of confirmation.
2. Known exposures to verify/update: Barclays (~£500M), Jefferies 
   (~£100M+), Elliott Investment Management (~£200M), SMBC, 
   Macquarie, Wells Fargo, Castlelake, TPG, Santander.
3. What is the status of regulatory investigations — is the Serious 
   Fraud Office (SFO) or Financial Conduct Authority (FCA) involved?
4. Has an administrator been appointed for MFS? If so, who, and 
   what have they reported?
5. How many Special Purpose Vehicles (SPVs) were involved, and who 
   was the auditor?
6. Is there any connection between MFS and Atlas SP (the structured 
   products platform associated with Apollo Global Management)?
7. What is the estimated total shortfall between claimed collateral 
   value and actual asset value?
8. Are there any related lawsuits filed by exposed institutions 
   against each other or against MFS principals?

Cite all sources with dates. This is a developing story with 
significant cross-border financial institution exposure.
```

---

### Senate DHS Funding Vote — March 9 Outcome
**Priority:** 🟠 | **Routes to:** MARCO, LABOR
```
What was the outcome of the US Senate vote on Department of Homeland 
Security (DHS) funding on March 9, 2026? This was reportedly the 
4th attempt to pass the House bill (which passed 221-209).

1. Did the Senate pass the DHS funding bill? What was the final 
   vote count?
2. If it passed: when does DHS officially reopen? When will 
   employees receive back pay? When does E-Verify resume 
   operations?
3. If it failed: what is the next procedural step? Is there a 
   5th vote scheduled? What are Senate leaders saying about 
   the timeline?
4. Have there been any statements from the White House, Senate 
   Majority Leader, or Senate Minority Leader about next steps?
5. What is the current status of TSA staffing — are there 
   reports of agents calling out or airports experiencing 
   extended delays?
6. How many federal employees remain furloughed or working 
   without pay?

Cite sources with dates. The DHS shutdown has been ongoing since 
approximately February 14, 2026.
```

---

### Experian Q4 2025 Auto Lending — Full Breakdown
**Priority:** 🟡 | **Routes to:** CARL, OTTO
```
Experian published its Q4 2025 State of the Automotive Finance Market 
report around March 5, 2026. Provide the complete data breakdown:

1. Subprime share of total vehicle financing for Q4 2025, broken 
   out by new vehicles and used vehicles separately
2. Delinquency rates by credit tier: 30-day, 60-day, and 90-day 
   for subprime, near-prime, prime, and super-prime
3. Average loan amount and average loan term by credit tier 
   (new and used)
4. Percentage of loans with negative equity at origination
5. Year-over-year change for each of the above metrics compared 
   to Q4 2024
6. Quarter-over-quarter change compared to Q3 2025
7. Any Experian commentary on outlook for 2026
8. Average monthly payment by credit tier
9. Repossession trends — any data on volume or rate changes

Compare key metrics to Q3 2025 and Q4 2024 to show the trend 
direction. Cite the Experian report directly where possible.
```

---

## Completed

### Hormuz Resolution Oil Reversal Analogs (Mar 9)
Gemini deep research doc. 5 historical analogs (1991 Gulf War, 2003 Iraq, 2011 Libya, 2019 Abqaiq, 2022 Russia). 18 signal files routed to 11 agents.

### UCFE Mechanics / March 12 Claims Framework (Mar 9)
Gemini deep research doc. Federal unemployment claims plumbing, SF-50 bottleneck, 126-160K suppressed backlog estimate, 3 scenarios for March 12.

### Bank Forced Disclosure / 8-K Pre-Announcement Framework (Mar 9)
Gemini deep research doc. 2008 + 2023 patterns, FDIC Call Report indicator hierarchy, OZK watch window Mar 25-Apr 10.

### Tech Goods Deflation / TSMC Dependency (Mar 9)
Gemini deep research doc. Core PCE relief valve math, hedonic reversal mechanism, 3 TSMC disruption scenarios.

### DHS Shutdown Status Verification (Mar 9)
Perplexity + Gemini. CONFIRMED ONGOING Day 23+. Senate blocked 51-45.

### Indeed Job Postings (Mar 9)
4 LLMs cross-verified. Index 104.7 (FRED-confirmed), -5.9% YoY.

### Cass Freight Index (Mar 9)
4 LLMs cross-verified. Shipments 0.886 = new cycle low, -7.1% YoY, 36th consecutive decline.

### Continuing Claims + JOLTS (Mar 9)
3 LLMs cross-verified. 213K initial, 1,868K continuing (+46K WoW), JOLTS Jan not yet released (Mar 13).

### PSEC PIK Verification (Mar 9)
4 LLMs. 35% figure CONFIRMED POISONED. Actual 8.6%.
