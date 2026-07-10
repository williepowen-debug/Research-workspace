# INSURANCE LEVEL 3 / CRE TRANSMISSION LAYER

**Created:** 2026-02-25 05:15 UTC  
**Status:** Initial Research Framework  
**Priority:** HIGH — New transmission path for CRE stress

---

## THESIS

Insurers represent a hidden transmission layer for CRE stress:
```
CRE stress → Insurance portfolio markdowns → Capital calls / forced sales → Broader market impact
```

This is distinct from the REGINALD (bank) path. Insurers have:
- **$600B+ in direct commercial mortgages** (life insurers alone)
- **$170B+ in CMBS holdings**
- **Rising Level 3 assets** (illiquid, hard-to-value)
- **Long duration liabilities** matched to long duration CRE assets

If CRE reprices sharply, insurers face simultaneous mark-to-market losses AND potential run risk on runnable liabilities (annuities without surrender penalties).

---

## KEY DATA POINTS (Chicago Fed Study, 2024)

### Life Insurer CRE Exposure
| Category | Amount | Notes |
|----------|--------|-------|
| **Direct Commercial Mortgages** | $600B | 16% of total investments, 14% of GA assets |
| **CMBS Holdings** | $170B | 80% AAA-rated tranches |
| **Total CRE Exposure** | ~$770B | Direct + indirect |

### Geographic Distribution
- **Suburban locations:** $488B (81%)
- **Downtown/CBD:** $109B (18%)
- **NYC/Manhattan:** $40B (single largest metro)

### Loan Quality
- Average LTV at origination: **0.54** (conservative vs residential)
- Average current LTV: **0.53**
- Average remaining maturity: **7.3 years**
- Downtown mortgages have slightly higher LTV (0.56) and shorter maturity (6.9 years)

### CMBS Differences (Hidden Risk)
CMBS mortgages differ systematically from insurer-originated:
- **Higher LTV** on average
- **Downtown exposure tilted toward office** (the worst-performing sector)
- Even AAA tranches exposed to subordination erosion

---

## SCENARIO ANALYSIS (Chicago Fed)

Under a stressed CRE price scenario:

| Loss Type | Estimated Loss | Notes |
|-----------|---------------|-------|
| Commercial mortgage losses | $10B | From direct lending |
| CMBS losses | $26.3B | Price floor methodology |
| **Total losses** | **$36.3B** | |

### Key Findings
- **5 large insurers** (>$10B assets) would face losses >20% of adjusted capital
- Several insurers would face **heightened regulatory scrutiny**
- However, most high-loss insurers have **low runnable liabilities** (mitigates run risk)
- Only **2 large insurers** have both >5% capital loss AND >50% runnable liabilities

---

## LEVEL 3 ASSETS — THE VALUATION RISK

### What Are Level 3 Assets?
Fair value hierarchy (ASC 820):
- **Level 1:** Market prices (stocks, liquid bonds)
- **Level 2:** Observable inputs (model with market data)
- **Level 3:** Unobservable inputs (management estimates) ← RISK ZONE

### Why This Matters
Per IAIS Global Insurance Market Report (Dec 2024):
- Life insurers have **increased Level 3 assets**
- Driven partly by IFRS 9/17 accounting changes (mortgages reclassified)
- Also driven by shift into **private credit, alternatives, private equity**
- Level 3 assets are illiquid — can't be easily sold
- Valuations depend on internal models — can hide losses

### The Apollo/Athene Model
PE-backed insurers (Athene, Global Atlantic, etc.) have aggressive alternative allocation:
- **Athene/Apollo:** Just absorbed $9B CRE loan portfolio from Apollo REIT
- Investment strategy: "excess return at every point along risk-reward spectrum"
- Heavy private credit exposure (originated by affiliated platforms)
- Level 3 concentration likely higher than traditional insurers

**Bloomberg (Nov 2025):** "Insurers and overseas entities pursuing higher returns with exotic asset-backed securities and other bets tied to private credit or private equity."

---

## ATHENE DEEP DIVE (10-K / Q3 2024 Investor Presentation)

### Scale
| Metric | Amount | Notes |
|--------|--------|-------|
| **Gross Invested Assets** | **$315B** | Includes ACRA |
| **Net Invested Assets** | **$243B** | Excludes ACRA noncontrolling interests |
| **Regulatory Capital** | **$29B** | Fortress balance sheet |
| **Excess Capital** | **$2B** | Above 'AA' requirements |
| **LTM Spread Related Earnings** | **$3.1B** | Very profitable |

### Asset Allocation (of $243B Net Invested Assets)
| Category | % | $B | Risk Notes |
|----------|---|-----|------------|
| Corporate & Gov't | 39% | ~$95B | Mostly IG |
| **CML (Commercial Mortgage Loans)** | **12%** | **~$29B** | DIRECT CRE |
| CLO | 10% | ~$24B | Structured credit |
| ABS | 12% | ~$29B | Structured |
| RML | 10% | ~$24B | Residential mortgages |
| RMBS | 3% | ~$7B | Agency/Non-agency |
| **CMBS** | **3%** | **~$7B** | INDIRECT CRE |
| Cash | 3% | ~$7B | Liquid |
| **Alternatives** | **5%** | **~$12B** | Level 3 heavy |
| Other | 3% | ~$7B | Misc |

### CRE Exposure Summary
| Type | Amount | % of NIA |
|------|--------|----------|
| Commercial Mortgage Loans | ~$29B | 12% |
| CMBS | ~$7B | 3% |
| **Total Direct CRE** | **~$36B** | **15%** |

This is MASSIVE — $36B in CRE against $29B regulatory capital = **124% CRE/Capital ratio**

### Alternatives Breakdown ($12B)
| Type | % | Notes |
|------|---|-------|
| AAA (Apollo Aligned Alternatives) | 70% | $8.4B - PE fund investments |
| Retirement Services | 20% | $2.4B |
| Other | 10% | $1.2B |

The alternatives repositioned in Q3 2024 — reduced certain investments by ~$1B.

### Key Strengths (Why It Might NOT Crack)
- 97% of AFS securities rated NAIC 1 or 2 (investment grade)
- 5-year average credit losses: **11 bps** (vs industry 13 bps)
- 86% of funding carries withdrawal penalty or can't be withdrawn
- Average LTV not disclosed but "conservative"

### Key Risks (Why It MIGHT Crack)
1. **$36B CRE = 124% of regulatory capital** — One bad quarter could hurt
2. **Apollo-originated assets** — $33B in LTM deployment from Apollo platforms, model-dependent pricing
3. **Alternatives performance** — Reported 8-10% returns but Level 3 = self-marked
4. **ACRA sidecar complexity** — Capital structure has layers

### What I Couldn't Find
- [ ] Actual Level 3 vs Level 2 breakdown (need fair value footnotes)
- [ ] Geographic concentration of CML portfolio
- [ ] Office vs other CRE property type split
- [ ] Delinquency rates on CML book

---

## TARGET INSURERS FOR RESEARCH

### Tier 1 — High CRE/Level 3 Exposure (PE-Backed)
| Insurer | Parent | Why Watch |
|---------|--------|-----------|
| **Athene** | Apollo | **$36B CRE (15% of assets), 124% CRE/Capital** |
| **Global Atlantic** | KKR | Similar PE playbook |
| **Corebridge** | (ex-AIG) | Large annuity book, alternatives push |

### Tier 2 — Traditional Life Insurers (CRE Heavy)
| Insurer | Ticker | Notes |
|---------|--------|-------|
| **MetLife** | MET | Major CRE lender, suburban focus |
| **Prudential** | PRU | Large GA with CRE allocation |
| **Lincoln National** | LNC | Targeted by hedge funds for CRE (2023), "modestly below average" per Fitch |
| **Principal Financial** | PFG | Midwest CRE concentration |

### Tier 3 — CMBS Heavy / Downtown Office
(Need to identify via SEC filings)

---

## RESEARCH AGENDA

### Phase 1: Quantify Exposure (This Week)
- [ ] Pull 10-K filings for Athene, MetLife, Prudential, Lincoln
- [ ] Extract: Total investments, CRE mortgages, CMBS, Level 3 assets
- [ ] Calculate: Level 3 / Total Assets ratio
- [ ] Map: Geographic concentration (especially downtown office)

### Phase 2: Stress Test Proxies
- [ ] Compare insurer stock performance during:
  - SVB crisis (March 2023)
  - NYCB stress (Feb 2024)
  - Current regional bank selloff (Feb 2026)
- [ ] If insurers aren't moving yet = potential mispricing

### Phase 3: NAIC Data Deep Dive
- [ ] Request NAIC quarterly data on industry CRE exposure
- [ ] Track: Delinquency rates, modifications, charge-offs
- [ ] Compare: Life vs P&C exposure

### Phase 4: Watch for Catalysts
- [ ] Athene Q4 earnings
- [ ] Any insurer downgrade on CRE concerns
- [ ] CMBS spread widening (transmission signal)
- [ ] Office REIT transactions (price discovery)

---

## POTENTIAL TRADES

| Instrument | Thesis | Risk |
|------------|--------|------|
| **LNC puts** | Already targeted by shorts, CRE concerns | May be crowded |
| **MET puts** | Largest traditional CRE lender | Lower LTV = more cushion |
| **APO puts** | Athene parent, aggressive alternatives | Could benefit from distress buying |

**Note:** Insurance stocks may not be the cleanest expression. Consider:
- **CMBS ETF** (if one exists with office exposure)
- **REITs with life insurer debt** (downstream transmission)

---

## KEY QUESTIONS TO ANSWER

1. **How much Level 3 has grown?** (Compare 2022 vs 2025 10-Ks)
2. **Which insurers have downtown office CMBS?** (CUSIP-level analysis)
3. **What's the runnable liability mix?** (Run risk assessment)
4. **Are insurers extending/modifying CRE loans?** (Extend-and-pretend parallel)
5. **What happens if Chicago Fed $36B loss estimate is too low?**

---

## CROSS-LINKS

- **REGINALD:** Bank CRE transmission (parallel path)
- **LIQUID:** Funding market stress (if insurers forced to sell)
- **CARL:** Consumer annuity implications (if insurer stress)

---

## NEXT STEPS

1. **Tonight:** Pull Athene 10-K, extract Level 3 breakdown
2. **This week:** Compare 4-5 major insurers' CRE/Level 3 ratios
3. **Flag:** Any insurer with >15% Level 3 AND >10% downtown office CRE
