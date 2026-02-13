# ZHAO Research Batch 2 — Prompts

**Created:** 2026-02-13
**Purpose:** Fill remaining gaps in ZHAO China macro framework

---

## RP-ZHAO-6: Data Sources and Monitoring Infrastructure

**Goal:** Document exactly where to get each metric we're tracking, update frequency, and how to access.

**Prompt:**

```
Create a comprehensive data sourcing guide for monitoring Chinese capital flows, LGFV stress, Hong Kong peg dynamics, and property sector health.

For each metric below, provide:
1. Official data source (institution, URL if available)
2. Update frequency (daily/weekly/monthly/quarterly)
3. Publication lag (how long after period end)
4. Access method (public webpage, API, subscription required)
5. Historical availability (how far back)

METRICS TO SOURCE:

Capital Flows:
- US Treasury TIC data (China holdings, Belgium holdings)
- Agency MBS holdings by country
- PBOC foreign reserve levels
- SAFE FX settlement data (the "backdoor intervention" gap)
- Gold reserve purchases

LGFV/Banking:
- Provincial NPL ratios (especially Guizhou, Henan, Liaoning)
- LGFV bond issuance and spreads
- Land sale revenue by province
- PBOC policy rate and liquidity injections
- Small bank consolidation announcements
- Trust/WMP default tracking

Hong Kong:
- HKMA Aggregate Balance (daily)
- HIBOR fixings (HKAB)
- Currency Board Account / Backing Ratio
- HKD forward points
- IPO pipeline and funds raised
- Hong Kong deposit flows (HKD vs USD composition)

Property:
- Developer bond prices and restructuring status
- Fannie Mae multifamily delinquency (US comparison)
- China new home sales (NBS)
- Developer earnings and guidance

Also identify:
- Any Bloomberg/Reuters terminal fields for real-time access
- Free alternatives where possible
- Key Twitter/X accounts or newsletters that aggregate this data
- Recommended monitoring cadence (what to check daily vs weekly vs monthly)

Output as a structured reference document with tables.
```

---

## RP-ZHAO-7: Taiwan Escalation Scenario Analysis

**Goal:** Map how Taiwan tensions would activate all ZHAO transmission channels simultaneously.

**Prompt:**

```
Analyze how a Taiwan Strait crisis or significant escalation in US-China tensions over Taiwan would impact Chinese capital flows, Hong Kong's financial system, and US Treasury markets.

SCENARIO FRAMEWORK:

1. TRIGGER TAXONOMY
- What specific events would constitute "escalation"? (military exercises, blockade, invasion, sanctions)
- What are the warning indicators before each escalation level?
- Historical precedents (1995-96 crisis, Pelosi visit 2022, recent exercises)

2. SANCTIONS CASCADE
- If US imposes Russia-style sanctions on China, what happens to:
  * SAFE's ~$3T in reserves (frozen? seized?)
  * China's ~$700B direct UST holdings
  * Belgium/Euroclear custodied assets (~$500B)
  * Chinese banks' USD clearing access (CHIPS)
  * HKMA's access to FIMA Repo Facility

3. HONG KONG TRANSMISSION
- Would HK be included in sanctions (HKAA precedent)?
- If HKMA loses USD clearing access:
  * Can it defend the peg?
  * What happens to the $410B in UST holdings?
  * Does the peg break? To what level?
- Capital flight dynamics: how fast, how much?

4. UST MARKET IMPACT
- If China/HK forced to liquidate $500B-$1T in UST:
  * Yield impact estimates
  * Fed response options (emergency QE? FIMA expansion?)
  * Contagion to other central banks
- Would China PRE-EMPTIVELY sell before sanctions (front-running)?

5. PROBABILITY AND TIMELINE
- Expert consensus on Taiwan escalation probability (2026-2030)
- Key dates/events that could trigger (Taiwan elections, Xi announcements)
- Early warning indicators to monitor

6. HEDGING IMPLICATIONS
- What positions benefit from Taiwan escalation?
- How does this interact with existing KRE/IWM/HYG puts?
- Is there a "Taiwan hedge" we should consider?

Provide specific data points, expert quotes, and historical analogies where available.
```

---

## RP-ZHAO-8: Counter-Thesis — The Soft Landing Scenario

**Goal:** Steel-man the bull case. What would we be wrong about?

**Prompt:**

```
Present the strongest possible case that China achieves a "soft landing" and that the stress transmission channels we've identified (LGFV → banking → UST liquidation) do NOT materialize in 2026-2027.

STRUCTURE:

1. THE BULL CASE FOR LGFV RESOLUTION
- How could China manage LGFV debt without a crisis?
- Historical precedent for "managed restructuring" (1990s bank NPLs, AMC model)
- Scale of fiscal capacity (central government balance sheet, special bonds)
- Why regional bank NPLs might plateau rather than accelerate
- Counter-argument to "zombie economy" thesis

2. THE BULL CASE FOR PROPERTY STABILIZATION
- Evidence that policy is working (inventory absorption, price stabilization in Tier 1)
- Comparison to Japan post-bubble (slow decline, not collapse)
- Why developer restructurings might complete successfully
- Demographic stabilization arguments (urbanization still has runway)

3. THE BULL CASE FOR CAPITAL FLOW STABILITY
- Why "custodial arbitrage" is actually neutral (just moving, not exiting)
- Evidence that China WANTS to hold USD (trade surplus recycling)
- Why Feb 2026 liquidity crunch was one-off not recurring
- PBOC capacity to manage without UST sales

4. THE BULL CASE FOR HK PEG
- 40 years of stability through multiple crises
- Massive reserve backing (>$400B vs ~$50B AB)
- Self-correcting mechanism has worked every time
- Why geopolitical tail risk is overblown

5. WHAT DATA WOULD CONFIRM THE BULL CASE?
- Metrics that would show stress is easing
- Timeline for "soft landing" to become visible
- What would change our bearish view?

6. WHERE THE BEAR THESIS IS WEAKEST
- Which of our assumptions is least supported by evidence?
- Which predictions are most likely to be wrong?
- What are we potentially missing?

Be rigorous and evidence-based. The goal is intellectual honesty, not confirmation of our existing view.
```

---

## RP-ZHAO-9: Chinese Insurance Company UST Holdings

**Goal:** Quantify the "third pool" of Chinese UST exposure beyond SAFE and HKMA.

**Prompt:**

```
Analyze Chinese insurance company holdings of US Treasury securities and USD-denominated assets, focusing on:

1. SCALE AND COMPOSITION
- Total assets of Chinese insurance industry (life, P&C, reinsurance)
- Estimated allocation to foreign assets / USD assets
- Breakdown between UST, Agency MBS, corporate bonds, equities
- Which insurers have largest foreign holdings? (Ping An, China Life, PICC, etc.)

2. REGULATORY FRAMEWORK
- CBIRC/NFRA rules on foreign asset allocation limits
- Recent changes to overseas investment regulations
- How do insurers report foreign holdings? (public disclosures?)

3. COMPARISON TO JAPAN
- Japanese life insurers are major UST holders (~$500B)
- Are Chinese insurers following a similar path?
- Key differences in regulatory environment and investment behavior

4. LIQUIDATION TRIGGERS
- Under what circumstances would Chinese insurers sell UST?
- Solvency stress (C-ROSS requirements)
- Currency hedging costs
- Regulatory guidance to reduce foreign exposure
- Flight-to-quality during domestic stress

5. DATA SOURCES
- Where can we track Chinese insurer foreign holdings?
- Any public disclosures or regulatory filings?
- Research reports or estimates from investment banks

6. TRANSMISSION TO UST MARKETS
- If Chinese insurers sold $50-100B in UST, what's the impact?
- How does this compare to SAFE/HKMA channels?
- Is this a leading or lagging indicator?

Provide specific numbers where available, acknowledge data limitations, and suggest monitoring approaches.
```

---

## Usage Notes

- Run in Gemini Deep Research or similar long-form research tool
- Each prompt designed for 15-30 min research depth
- Save outputs to `AGENTS/ZHAO/sources/` as markdown
- Update ML.tsv and STATUS.md after integration
- Add any new predictions to PREDICTIONS.md

---

*Priority order: 6 (data sourcing) → 7 (Taiwan) → 8 (counter-thesis) → 9 (insurance)*
