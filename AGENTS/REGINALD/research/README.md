# REGINALD Research Status

**Updated:** 2026-02-15  
**Research Packages:** 17+ complete  
**Sub-Agents:** BROCK, CREED, CORAL, RENO, TEX

---

## RESEARCH SERIES

### RP-REG-3.x — Geographic & Municipal Analysis

| # | Title | Status | Key Finding |
|---|-------|--------|-------------|
| 3.1 | Regional Bank Geographic Footprints | ✅ Complete | No KRE constituent has material TX border exposure |
| 3.2 | Municipal Securities Exposure | ✅ Complete | ZION = $5.78B total muni (lender, not just holder); WAL = $1.36B UNRATED |
| 3.3 | DC Corridor Bank Analysis | ✅ Complete | EGBN 100% DC, already in crisis; NoVA has "Defense Shield" |
| 3.4 | Texas Border Municipal Analysis | ✅ Complete | Barclays void; CFR/TCBI filling gap; Laredo water crisis |
| 3.5 | Florida Insurance-Banking Nexus | ✅ Complete | Citizens $678B "Sword of Damocles"; VLY commercial reinsurance risk |

### RP-REG-4.x — Systemic Channels

| # | Title | Status | Key Finding |
|---|-------|--------|-------------|
| 4.1 | Stablecoin Deposit Flight | ✅ Complete | $500B outflow projected by 2028; systemic NIM compression |
| 4.2 | Florida HOA/Condo Crisis | ✅ Complete | Post-Surfside SB 4-D → $10K-$224K assessments on 900K+ condos |
| 4.3 | FL Institutional Capital | ✅ Complete | Private capital flows to distressed FL assets |

### RP-FL-x.x — Florida Deep Dives (CORAL)

| # | Title | Status | Key Finding |
|---|-------|--------|-------------|
| 1.1 | Florida Condo Receivership | ✅ Complete | 1,438 blacklisted buildings |
| 1.2 | FL Private Insurer Health | ✅ Complete | Carrier stress mapping |
| 1.3 | VLY Florida Exposure | ✅ Complete | FL 27% of loans, $3.3B Miami CRE |
| 1.4 | Florida Bridge Loan Market | ✅ Complete | Refinancing gap analysis |
| 1.5 | Florida Developer Acquisitions | ✅ Complete | Distressed deal flow |
| 2.1 | Private Insurer Health (v2) | ✅ Complete | Updated carrier analysis |

### RP-REG-5.x — Market Microstructure & Volume

| # | Title | Status | Key Finding |
|---|-------|--------|-------------|
| 5.1 | KRE Volume Deep-Dive (Tasks 1-4) | 🟡 In Progress (5-7 pending) | KRE shares -12.4% while price +6.8% (AP redemption). OZK 0.53x up/down ratio = persistent distribution. Selling anticipatory, buying reactive. XLF inflows vs KRE outflows = surgical regional de-risking. |

### RQ-REG-x — Research Questions (Ad Hoc)

| # | Title | Status | Key Finding |
|---|-------|--------|-------------|
| A01 | WAL/ZION Fraud Comparison | ✅ Complete | Both -13% post-Tricolor; WAL "hyper-vigilant" |
| A02 | Stupin Syndicate Mapping | ✅ Complete | Sector exposure mapping |
| A02B | Forensic Insurance Auditor | ✅ Complete | Deep forensic analysis |
| A03 | Fraud Contagion Signals | ✅ Complete | Sector transmission paths |
| B01 | LP Liquidity / CFG Transmission | ✅ Complete | Fund finance $10-11B exposure |
| C01 | FHLB Haircut Policy | ✅ Complete | Haircut mechanics during stress |

---

## KEY FINDINGS SUMMARY

### 1. Multi-Channel Exposure Matrix
Banks scored by exposure to 8 convergence channels. WAL (10), VLY (9), CFG (9), ZION (9) have multiple paths to break.

### 2. Hidden Exposures Discovered
| Bank | What Market Sees | What We Found |
|------|------------------|---------------|
| ZION | $1.4B muni securities | $5.78B total (+ $4.36B loans + $524M unfunded) |
| WAL | $2.28B muni securities | $1.36B is UNRATED = private placements |
| CFG | Big muni investor? | $1M — effectively zero |

### 3. Florida Doom Loop
Citizens Property Insurance emergency assessment can levy 10% on ALL FL policies indefinitely. Banks hit both sides: loan losses + AFS/OCI losses on muni holdings.

### 4. BDC Transmission Path
PIK masks 6% shadow default rate (vs 2.1% reported). PSEC 8.6% (verified — prior 35% was hallucinated), FSK 27%. Dividend cuts → NAV crashes → bank fund finance losses.

---

## DATA GAPS

| Gap | Priority | Notes |
|-----|----------|-------|
| Burke & Herbert (BHRB) deep dive | 🟡 Medium | DC corridor, >50% AFS in munis |
| Nevada gaming/tourism stress | 🟡 Medium | RENO sub-agent territory |
| Texas border bank forensics | 🟡 Medium | IBOC is only public play |
| 2013 sequester precedent analysis | 🟢 Low | Historical comparison |

---

## SUB-AGENT RESEARCH STATUS

| Sub-Agent | Research Packages | Status |
|-----------|-------------------|--------|
| **BROCK** | BDC analysis, bankruptcy tracking, AI capex | Active |
| **CREED** | CMBS DQ, maturity wall, Chicago repricing | Active |
| **CORAL** | FL condo, HOA, insurance, VLY exposure | Active |
| **RENO** | Canadian tourism, housing | Dormant |
| **TEX** | Border, munis | Dormant |

---

## EXHAUSTED TOPICS

*Do not re-research without new data:*

- Regional bank CLO holdings (RF is outlier, not systemic)
- Japan BOJ FSR — they're BUYING CLOs, not selling (trigger is US credit cycle)
- SoCal/Imperial Valley — coastal only, no KRE exposure to ag stress
- SBCF deep dive — fortress balance sheet, skip as short target

---

## NEXT RESEARCH PRIORITIES

| Priority | Topic | Trigger |
|----------|-------|---------|
| 🔴 High | PSEC/FSK Q4 analysis | Feb 15-20 earnings |
| 🔴 High | Q1 bank earnings preview | Mar 2026 |
| 🟠 Medium | Phoenix CRE repricing | If Chicago pattern spreads |
| 🟡 Low | BHRB DC exposure | If DOGE accelerates |

---

## FILE LOCATIONS

```
research/
├── README.md              # This file — master research index
├── prompts/               # Research prompts for external LLM execution
├── outputs/
│   ├── RP-REG-3.x/       # Geographic/Municipal
│   ├── RP-REG-4.x/       # Systemic Channels
│   ├── RP-FL-x.x/        # Florida (CORAL)
│   └── RQ-ad-hoc/        # Ad hoc research questions (A01-C01)
└── FL_CONVERGENCE.md     # Florida convergence synthesis
```

---

*For bank exposure details, see `BANK_EXPOSURE_MATRIX.md`*
