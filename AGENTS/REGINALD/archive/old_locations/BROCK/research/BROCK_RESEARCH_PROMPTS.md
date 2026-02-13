# BROCK Research Prompts

Research prompts to build out the BDC & Private Credit monitoring domain.

---

## RP-BROCK-1: Sector Exposure Mapping

**Priority:** HIGH
**Estimated Time:** 1-2 hours

**Question:** What are the actual sector concentrations across major BDCs, and which have dangerous tech/software overweight?

**Research Tasks:**
1. Pull latest 10-Q/10-K for top 10 BDCs by AUM
2. Extract sector breakdown (software, healthcare, industrials, etc.)
3. Identify which BDCs have >30% tech/software exposure
4. Map portfolio overlap (are they all in the same deals?)
5. Note any concentration in specific sub-sectors (e.g., vertical SaaS, cybersecurity)

**Output:** Table of BDC sector exposures with concentration risk ratings

**Sources:**
- SEC EDGAR (10-Q, 10-K filings)
- BDC investor presentations
- BDC Buzz sector analysis

---

## RP-BROCK-2: PIK Income Deep Dive

**Priority:** HIGH
**Estimated Time:** 1 hour

**Question:** What does PIK income actually signal, and which BDCs are showing the most stress?

**Research Tasks:**
1. Define PIK income and why it's a shadow default proxy
2. Pull historical PIK % for major BDCs (2019-2026)
3. Identify which BDCs currently have highest PIK ratios
4. Research: What PIK levels preceded actual defaults historically?
5. Find the Golub +173% YoY spike detail and context

**Output:** PIK trend analysis with historical context and warning thresholds

**Sources:**
- BDC quarterly reports
- Credit research (Moody's, S&P)
- Industry commentary (BDC Buzz, Seeking Alpha)

---

## RP-BROCK-3: Redemption Mechanics & Historical Gates

**Priority:** MEDIUM
**Estimated Time:** 1 hour

**Question:** How do BDC redemption gates work, and what happened when they triggered historically?

**Research Tasks:**
1. Explain how redemption limits work (typically 5% quarterly)
2. Research: Which BDCs have triggered gates in the past?
3. What happened to NAV, stock price, and portfolio after gates triggered?
4. How did Blue Owl's merger freeze redemptions? Is this common?
5. What are the legal/regulatory constraints on gates?

**Output:** Redemption mechanics explainer with historical case studies

**Sources:**
- SEC filings
- Legal/regulatory guidance
- News archives for historical gate events

---

## RP-BROCK-4: Asian Investor Dynamics

**Priority:** MEDIUM
**Estimated Time:** 1 hour

**Question:** Who are the Asian LPs in US private credit, and why are they exiting?

**Research Tasks:**
1. Which Asian investors (family offices, institutions) have exposure to US BDCs?
2. Why are they pulling out now? (Yen strength? Local opportunities? Risk-off?)
3. How significant is Asian capital to US private credit (~% of AUM)?
4. Is this connected to SAM's Japan thesis? (Repatriation)
5. What's the timeline risk for continued outflows?

**Output:** Asian investor landscape and outflow risk assessment

**Sources:**
- Bloomberg/Reuters reporting
- Private wealth industry coverage
- Cross-reference with SAM research on repatriation

---

## RP-BROCK-5: Bank Exposure to Private Credit

**Priority:** HIGH
**Estimated Time:** 1-2 hours

**Question:** Which banks have exposure to BDCs and private credit, and through what channels?

**Research Tasks:**
1. **Fund Finance:** Which banks provide subscription lines and NAV facilities to private credit funds? (CFG noted as bellwether)
2. **CLO Holdings:** Which banks hold CLOs that could be impacted by BDC forced selling?
3. **Direct Partnerships:** Any bank-BDC partnerships or warehouse facilities?
4. **Leverage-on-leverage:** Map the CFG "LP borrows for capital call + fund borrows via sub line" risk
5. Size the exposure where possible

**Output:** Bank-private credit exposure map for integration with REGINALD watchlist

**Sources:**
- Bank 10-Ks (fund finance disclosures)
- CLO databases
- Industry reports on bank-private credit relationships

---

## RP-BROCK-6: Historical BDC Stress Episodes

**Priority:** MEDIUM
**Estimated Time:** 1-2 hours

**Question:** How did BDCs behave in past stress periods, and what can we learn?

**Research Tasks:**
1. **2008 GFC:** BDC performance, NAV declines, redemption behavior
2. **2015-16 Energy:** Energy-exposed BDCs, defaults, recovery
3. **2020 COVID:** BDC drawdowns, how quickly did they recover?
4. **2022 Rate Shock:** Impact on floating-rate portfolios
5. What patterns repeat? What leading indicators worked?

**Output:** Historical stress playbook with patterns and lessons

**Sources:**
- Academic research on BDC performance
- Historical NAV data
- News archives

---

## RP-BROCK-7: Current Portfolio Company Stress

**Priority:** HIGH  
**Estimated Time:** 1-2 hours

**Question:** Which portfolio companies in major BDCs are showing stress, and what sectors are they in?

**Research Tasks:**
1. Pull non-accrual lists from latest BDC filings
2. Identify common names across multiple BDCs
3. Research specific stressed companies (news, financials)
4. Map to sectors — is it concentrated in tech/software?
5. Any large positions that could cause outsized losses?

**Output:** Portfolio company stress map with concentration analysis

**Sources:**
- BDC 10-Q schedules of investments
- Company news
- Bankruptcy/restructuring filings

---

## Suggested Order

1. **RP-BROCK-1** (Sector Exposure) — Foundational for understanding concentration risk
2. **RP-BROCK-2** (PIK Deep Dive) — Key signal we're tracking
3. **RP-BROCK-5** (Bank Exposure) — Critical for REGINALD integration
4. **RP-BROCK-7** (Portfolio Stress) — Current state assessment
5. **RP-BROCK-3** (Redemption Mechanics) — Understand the plumbing
6. **RP-BROCK-4** (Asian Investors) — SAM cross-reference
7. **RP-BROCK-6** (Historical) — Context and patterns

---

*Created: 2026-02-03*
