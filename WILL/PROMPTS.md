# PROMPTS.md — Research Prompts for Will

Prompts for Will to run through external LLMs (Gemini, Perplexity, ChatGPT, etc.).
Completed prompts archived in `COMPLETED_PROMPTS.md`.

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
*Origin: Mar 9, 2026 — Will realized this inverts the research process.*

---

## 🔴 High Priority

### Oil at $100 — Downstream Economic Impact
**Routes to:** HAWK, CARL, LABOR
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

### Cheniere Energy (LNG) — Margin Sensitivity & Hedging Structure
**Routes to:** HAWK, FORGE
**Why:** LNG $270C/$300C May spread is #5 conviction at 4/5. Haven't done CF-level deep dive on Cheniere yet.
```
Cheniere Energy (ticker: LNG) is the largest US LNG exporter. With 
the Strait of Hormuz closed since March 1, 2026, Qatar LNG offline, 
and TTF gas prices up 74%, analyze Cheniere's investment case:

1. What is Cheniere's current LNG export capacity (mtpa and 
   bcf/d)? How does this compare to total US LNG export capacity?
2. What percentage of Cheniere's contracts are long-term 
   fixed-price vs spot/short-term? This is critical — how much 
   of a TTF spike actually flows to their bottom line?
3. For the SPOT-EXPOSED portion: what is the approximate earnings 
   sensitivity per $1/MMBtu increase in the TTF-Henry Hub spread?
4. Current TTF price vs Henry Hub — what is the current spread? 
   How does this compare to the 2022 peak spread during 
   Russia-Ukraine?
5. What happened to Cheniere's stock price and earnings during 
   the 2022 Russia-Ukraine LNG crisis? Stock went from ~$100 to 
   ~$180 — what was the earnings trajectory that drove that move?
6. Current analyst consensus: EPS estimates, price targets, and 
   how stale are they (pre- or post-Hormuz closure)?
7. Cheniere's Sabine Pass and Corpus Christi terminals — are they 
   running at full capacity? Any expansion projects coming online 
   in 2026?
8. Who are Cheniere's main competitors for spot LNG cargoes? 
   (Shell, TotalEnergies, BP trading desks?)
9. What is the bear case? If China secures a side-deal with Iran 
   for Qatar LNG safe passage, or if Hormuz reopens in 4-6 weeks, 
   how quickly does the LNG premium deflate?
10. Current LNG stock price is ~$245. Options IV levels — are 
    call premiums bloated or still reasonable?

Cite sources with dates. I'm evaluating a May $270C/$300C call 
spread and need to understand how much of the thesis is already 
priced into the stock at $245.
```

---

### Fertilizer Trade — CF Industries / Mosaic / Nutrien Analysis
**Routes to:** HAWK, HENRY
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

## 🟠 Medium Priority

### Kennedy-Wilson Holdings Debt Exchange Status
**Routes to:** REGINALD
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

### BlackRock HLEND Redemption Gate — Private Credit Contagion
**Routes to:** BROCK
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

### Fertilizer Supply Chain — Deep Dive on Gulf Dependency
**Routes to:** HAWK, CARL
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

### MFS (Motor Finance Specialist UK) Fraud — Full Exposure Map
**Routes to:** OTTO, BROCK
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

### Japan FY2026 Budget and JGB Issuance Schedule
**Routes to:** SAM, ZHAO
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

### Senate DHS Funding Vote — March 9 Outcome
**Routes to:** MARCO, LABOR
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
approximately February 2026.
```

---

## 🟡 Lower Priority

### Google Trends — Labor Search Terms
**⚠️ WILL MUST DO MANUALLY** — LLMs cannot access real-time Google Trends data.
**Routes to:** LABOR
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

### Subprime Auto ABS Performance Data
**Routes to:** CARL, OTTO
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

Fitch reported subprime auto 60+ day delinquencies hit all-time 
record ~7.1% in early 2026. Need trend trajectory.
```

---

### Tanker Rates vs Crude Oil Price — Historical Relationship
**Routes to:** LIQUID, HAWK
```
What happens to tanker rates and shipping stocks when crude oil 
price crashes but physical supply disruption continues?

1. Historical precedents: Find episodes where oil prices dropped 
   sharply (>15%) while a physical chokepoint disruption was still 
   active. What happened to:
   a) VLCC spot rates
   b) Suezmax and Aframax rates
   c) Tanker stock prices (STNG, FRO, EURN, TNK, DHT)
   d) The BDTI (Baltic Dirty Tanker Index)

2. Are tanker rates driven primarily by:
   a) Crude oil price level?
   b) Ton-miles (distance × volume shipped)?
   c) Fleet utilization / vessel availability?
   d) Route disruptions (longer voyages = fewer available ships)?
   Which factor has the highest correlation historically?

3. Current situation: Hormuz transits are down 92%, routes are 
   being diverted around the Cape of Good Hope, VLCC rates were 
   +201% before today's oil crash. If crude drops another 10-20% 
   but Hormuz stays closed:
   a) Do tanker rates hold because ton-miles are still elevated?
   b) Or do rates drop because lower crude price = less incentive 
      to ship?

4. Shadow fleet dynamics: 68% of Russian crude is carried by 
   sanctioned shadow fleet vessels. If Russia sanctions ease and 
   shadow fleet becomes legitimate, does this FREE UP vessel 
   capacity (bearish tankers) or does it just relabel existing 
   capacity (neutral)?

5. What is the current orderbook for new tanker builds? How 
   tight is the supply of available vessels? What is fleet age?

6. Scorpio Tankers (STNG) specifically: what percentage of their 
   revenue is spot vs time charter? How quickly does a rate change 
   flow through to earnings?

Cite sources with dates.
```

---

### US Military Seizure of International Strait — Historical Precedents
**Routes to:** HANS, HAWK
```
What are the historical precedents for a US president publicly 
considering or executing military seizure/control of an 
international maritime chokepoint?

1. Has the US ever physically occupied or controlled a major 
   international strait or canal? Include:
   - Panama Canal (construction through handover)
   - Suez Crisis (1956 — US role)
   - Persian Gulf "tanker war" escort operations (1987-88)
   - Any other relevant precedents

2. For each precedent: what happened to oil prices, defense 
   stocks, and regional currencies within 30/60/90 days of the 
   announcement or action?

3. What would "taking over the Strait of Hormuz" mean 
   operationally? What military assets would be required? How 
   long would it take? What are the risks (Iranian anti-ship 
   missiles, mines, submarine threats)?

4. Legal framework: what authority does a US president have to 
   seize an international waterway? Does this require 
   Congressional approval? UN Security Council? Or can it be 
   done under existing war powers?

5. If the US physically secures Hormuz:
   a) Does Gulf oil flow resume immediately?
   b) How long to clear mines and secure shipping lanes?
   c) Does Iran retain ability to disrupt even with US control?
   d) What is the impact on insurance markets (currently Hormuz 
      is uninsurable)?

6. Is this likely posturing to force Iran to negotiate, or 
   genuine operational planning? What signals would distinguish 
   the two?

7. How would China, Russia, and regional powers (Saudi, UAE, 
   Turkey) react to US physical control of Hormuz?

Cite sources with dates.
```

---

### Experian Q4 2025 Auto Lending — Full Breakdown
**Routes to:** CARL, OTTO
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

## Demand Destruction Research Series (Mar 11)

**Context:** RED team challenged our Hormuz duration thesis. Need to understand historical demand destruction patterns to calibrate position duration and portfolio construction. Run through multi-LLM pipeline (Perplexity + Kimi + ChatGPT/Gemini).

**Routing:** P1 → HENRY + FORGE | P2 → HENRY + FORGE | P3 → CARL + LABOR | P4 → HAWK + HANS | P5 → HENRY + HAWK

### Prompt DD-1: Hamilton's Oil-GDP Model Applied to 2026

```
I'm researching the relationship between oil price shocks and GDP decline, specifically James Hamilton's nonlinear model from his 2003 paper and his 2009 Brookings paper "Causes and Consequences of the Oil Price Shock of 2007-2008." Hamilton found that the rate of oil price increase relative to recent history is the key predictor of recession — not the absolute level.

Current situation: WTI crude went from ~$68 in January 2026 to $120+ by early March 2026 (roughly +75% in 8 weeks) due to the Strait of Hormuz closure. Prior to this, oil had been range-bound at $65-75 for most of 2025.

Questions: (1) Using Hamilton's "net oil price increase" measure, how does the current shock compare in magnitude to 1973, 1979, 1990, and 2008? (2) What GDP decline would Hamilton's model predict from a shock of this magnitude? (3) What is the typical lag in quarters between the oil price spike and the GDP trough in his model? (4) Does the model distinguish between supply-driven shocks (embargo/war) and demand-driven shocks in terms of GDP impact timing?
```

### Prompt DD-2: Oil Peak to Financial Trough — Precise Timeline Table

```
I need a precise historical timeline of oil shock transmission to financial markets. For each of the following episodes, provide the specific month/year for each milestone:

Episodes: 1973-74 Arab Embargo, 1979-80 Iranian Revolution, 1990 Gulf War, 2008 oil spike, 2022 Ukraine

For each, provide: (1) Oil price trough before the shock (price + date), (2) Oil price peak during the shock (price + date), (3) Date oil prices first declined 20% from peak, (4) S&P 500 peak before/during the shock (level + date), (5) S&P 500 trough (level + date), (6) Lag in months from oil peak to equity trough, (7) HY/Baa credit spread peak (level + date, if available), (8) Lag in months from oil peak to credit spread peak, (9) NBER recession start and end dates, (10) Lag from oil peak to recession start.

Please present as a table. Note where data is approximate. I'm specifically trying to determine: does the equity/credit trough come BEFORE or AFTER oil prices start falling? How many months of overlap exist between elevated oil and financial stress?
```

### Prompt DD-3: Consumer Elasticity When Already Stretched

```
I'm researching whether oil-driven demand destruction happens faster when consumers are already financially stressed versus when consumer balance sheets are healthy at the time of the shock.

Context: In March 2026, US consumers face: subprime auto delinquencies at 7.1% (highest since 2010), credit card balances at record highs, pandemic savings fully depleted, and real wage growth near zero. Oil has spiked 75% in 8 weeks.

Compare the consumer starting conditions at the onset of each oil shock: (1) 1973 — what was the consumer debt/income ratio, savings rate, and unemployment when oil spiked? (2) 1979 — same metrics, (3) 2008 — same metrics (note: consumers were already overleveraged via housing), (4) 2022 — same metrics (note: consumers had excess pandemic savings).

Key question: In episodes where consumers were already stretched (1979, 2008), did demand destruction in oil/gasoline consumption happen faster (measured in months from price spike to measurable consumption decline) compared to episodes where consumers had more cushion? Is there academic research on the elasticity of gasoline demand varying by consumer financial health?
```

### Prompt DD-4: China Selective Embargo — Quantifying the Hormuz Flow

```
The Strait of Hormuz is currently under selective restriction (March 2026). Iran has closed it to US, Israeli, and Western-allied shipping but is allowing Chinese-flagged vessels to transit. I need to understand the quantitative implications.

Questions: (1) What percentage of total Hormuz oil flow (by volume, barrels per day) was destined for China before the crisis? Break down by crude oil vs LNG vs refined products. (2) What percentage was destined for other Asian buyers (Japan, South Korea, India)? (3) Of the non-China Asian buyers, which have bilateral relationships with Iran that might allow continued transit? India specifically — India has historically maintained oil trade with Iran despite Western sanctions. (4) If Chinese + Indian flows continue (even at reduced volumes), what is the effective supply disruption in million barrels per day versus total closure? (5) Is there historical precedent for a selective maritime embargo where some nations' shipping was allowed through a chokepoint while others were blocked? The closest parallel might be the Iran-Iraq tanker war (1984-88) where some flags were targeted and others weren't. (6) How does a partial flow (say 40% of normal) change the global oil supply/demand balance compared to full closure? What oil price level does partial flow support vs full closure?
```

### Prompt DD-5: Rate of Change vs Level — When Does Oil Stabilize?

```
James Hamilton's research emphasizes that the rate of oil price INCREASE relative to recent history matters more than the absolute price level for economic damage. A rapid spike causes more damage than a gradual rise to the same level.

Current situation: WTI went from $68 to $120+ in 8 weeks (Feb-Mar 2026). The question is what happens AFTER the initial spike.

Historical research questions: (1) In each prior oil shock (1973, 1979, 1990, 2008), how long did oil remain within 10% of its peak price before declining? In other words, how long was the "plateau" at elevated levels? (2) During the plateau period, did the economic damage continue to accelerate, or did the economy begin adapting? Specifically: did consumer gasoline consumption begin adjusting during the plateau, or only after prices started falling? (3) If oil stabilizes at $100-110 for 3-6 months (due to partial Hormuz flows via China), does Hamilton's model treat that differently than a continued rise to $140-150? The distinction matters because stabilization means the "net oil price increase" measure stops growing even though the level is high. (4) Is there research on the difference between a V-shaped oil spike (up fast, down fast — like 1990) versus an elevated plateau (up fast, stays high — like 1979-80) in terms of GDP impact? Which pattern causes more total economic damage? (5) What price level historically triggered measurable US gasoline demand destruction? Is there an estimated price elasticity of US gasoline demand in the short run (3 months) versus medium run (12 months)?
```
