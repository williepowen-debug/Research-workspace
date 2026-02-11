# REGINALD STATUS
**Last Updated:** 2026-02-11 | **Status:** 🟠 ELEVATED — Convergence Thesis Active

*Updated by Prome*

**Recent Research:**
- ✅ RP-REG-4.1: Stablecoin/Crypto Banking Exposure — $500B systemic deposit flight risk
- ✅ RP-REG-4.2: Florida HOA/Condo Assessment Crisis — Compounds FL doom loop
- ✅ **RP-FL-1.1 through 2.1: Complete Florida thesis** — See CORAL sub-agent

---

## Sub-Agent Signal Dashboard

*Quick scan of sub-agent status. Update when sub-agent STATUS.md changes.*

| Agent | Signal | Value | Threshold | Status | Updated |
|-------|--------|-------|-----------|--------|---------|
| **CREED** | Office CMBS DQ | **12.34%** (+103bps MoM) | >10% RED | 🔴 **ATH** | Feb 10 |
| **CREED** | MF CMBS DQ | 6.94% (+232bps YoY) | >8% RED | 🟠 | Feb 10 |
| **CREED** | Special Servicing | 17.16% | >12% RED | 🔴 | Feb 3 |
| **CREED** | 2026 Maturity Wall | $936B | — | 🔴 | Feb 3 |
| **BROCK** | PSEC PIK % | 35% | >25% RED | 🔴 | Feb 10 |
| **BROCK** | HRZN NAV Δ | -21% | >-15% RED | 🔴 | Feb 10 |
| **BROCK** | Bank-NDFI Exposure | $1.2T | >$1T ORANGE | 🟠 | Feb 10 |
| **BROCK** | Shadow Default Rate | ~6% | >5% ORANGE | 🟠 | Feb 10 |
| **BROCK** | BDCs Burning Cash | >50% | >40% RED | 🔴 | Feb 10 |
| **CORAL** | Blacklist Count | 1,438 | >1,500 RED | 🟠 | Feb 6 |
| **CORAL** | Assoc. Bankruptcies | 1 | >3 ORANGE | 🟡 | Feb 6 |
| **CORAL** | VLY Non-accruals | 0.87% | >1.0% ORANGE | 🟡 | Feb 6 |

**Summary:** CREED 🔴 (Office ATH) | BROCK 🟠 | CORAL 🟠

**Transmission paths active:**
1. CRE → Bank losses (CREED) — waiting for employment trigger
2. AI Capex → BDC NAV → Bank fund finance (BROCK) — HRZN first canary down
3. Condo crisis → FL bank stress (CORAL) — building, no cascade yet

---

## CRE Stress Dashboard (Trepp Data)

### CMBS Delinquency (January 2026)

| Sector | Rate | MoM Δ | YoY Δ | Status |
|--------|------|-------|-------|--------|
| **Office** | **12.34%** | +103 bps | +211 bps | 🔴 ALL-TIME HIGH |
| Multifamily | 6.94% | +30 bps | +232 bps | 🟠 Spreading |
| Retail | 7.04% | +12 bps | -48 bps | 🟡 Stable |
| Lodging | 5.56% | -105 bps | -67 bps | 🟢 Improving |
| Industrial | 0.62% | -18 bps | +16 bps | 🟢 Low |
| **Overall** | **7.47%** | +17 bps | +91 bps | 🟠 Rising |

**Shadow stress:** Including matured balloons (extend-and-pretend), effective rate = **9.14%**

**Full data:** `domain/workbook/CMBS_DELINQUENCY.md`

---

## FHLB Advance Monitoring Dashboard

**🟢 Status: GREEN** — System advances well below stress thresholds

### Current Reading (Week of Feb 11, 2026)
| Metric | Current | Threshold | Status |
|--------|---------|-----------|--------|
| **FHLB System Advances** | **~$480B (est)** | 🟡 $700B / 🟠 $750B / 🔴 $800B | 🟢 **GREEN** |
| vs 2023 Crisis Peak | -29% | Peak was $675B (March 2023) | Normalized |
| vs Historical Average | Normal | $450-550B pre-crisis | Within range |

**Data Source:** Federal Reserve H.8 "Assets and Liabilities of Commercial Banks" — Table: "Borrowings from Federal Home Loan Banks"
**Update Frequency:** Weekly (every Friday ~4:15pm ET)
**Vector:** VX-REG-7.01

### What This Measures
**FHLB advances = regional bank emergency liquidity usage**
- Federal Home Loan Bank system provides secured loans to member banks
- Spike in advances = banks can't fund themselves in private markets
- 2023 SVB crisis: Advances spiked from ~$450B to **$675B peak** in March
- Normal range: $450-550B
- System has joint & several liability — one bank's failure = everyone's problem

### Why It Matters
**FHLB is the convergence point for ALL regional bank stress:**
1. **CRE losses** → Banks need liquidity → FHLB borrowing
2. **Deposit flight** → Replace lost deposits → FHLB borrowing  
3. **NDFI fraud** → Cover fraud losses → FHLB borrowing
4. **Consumer defaults** → Capital depletion → FHLB borrowing
5. **Maturity walls** → Can't refi in market → FHLB borrowing

**When FHLB advances spike, it means multiple stress channels are activating simultaneously.**

### Monitoring Protocol

**Every Friday (H.8 Release Day):**
1. Check Fed H.8 release at https://www.federalreserve.gov/releases/h8/current/
2. Navigate to Table showing bank borrowings breakdown
3. Find "Borrowings from Federal Home Loan Banks" line item
4. Update VX-REG-7.01 with current value
5. Calculate week-over-week and month-over-month change

**Alert Triggers:**
- 🟡 **YELLOW**: Advances >$700B (approaching 2023 peak)
- 🟠 **ORANGE**: Advances >$750B (exceeds 2023 peak by 11%)
- 🔴 **RED**: Advances >$800B (systemic stress, +19% above crisis peak)

**What to check when advances spike:**
- Which banks are borrowing? (Individual FHLB bank filings, quarterly lag)
- What collateral? (FHLB collateral acceptance tightening = stress amplifier)
- How fast? (Rapid spike = acute crisis; gradual = chronic stress)

**Cross-reference with:**
- VX-REG-7.02: FHLB collateral haircuts (tightening = liquidity squeeze)
- VX-REG-7.03: FHLB pledging status (banks moving to Delivery Status = forensic audit)
- VX-REG-4.01: Deposit flight rate (cause of FHLB need)
- Fed discount window usage (if both spike = severe stress)

### Historical Context
| Period | FHLB Advances | Context |
|--------|---------------|---------|
| **Pre-2023** | ~$450-550B | Normal range |
| **Mar 2023 (SVB Crisis)** | **$675B peak** | +50% spike in weeks |
| **Late 2023** | ~$500-550B | Normalization |
| **Q4 2024 - Q1 2025** | ~$450-500B | Stable |
| **Feb 2026 (Current)** | **~$480B (est)** | 🟢 Normal range |

### The 2023 Pattern (Why We Watch This)
- **March 9, 2023**: SVB fails
- **March 10**: Signature Bank fails  
- **March 15**: First Republic stress emerges
- **Week of March 13**: FHLB advances spike to **$675B** (from ~$450B)
- **Signal**: Banks can't access private funding → systemic liquidity crisis

**If advances cross $700B again, history says we're in early stages of regional banking crisis.**

### Data Notes
- Current reading is **estimated** from H.8 total borrowings (Feb 11, 2026)
- Exact FHLB line item requires accessing detailed H.8 tables
- Updates every Friday with actual data
- Seasonally adjusted vs not seasonally adjusted: Use NSA for raw stress signal

**Files:** `domain/workbook/VX.tsv` (Vector VX-REG-7.01)

---

## BDC Cash Flow Divergence Dashboard  

**🟠 Status: ORANGE** — >50% of BDCs burning cash, PSEC/FSK at high risk

### Framework Overview
**New monitoring system** (implemented Feb 11, 2026) tracking **cash NII vs dividend coverage** for 7 key Business Development Companies. 

**Key insight:** BDCs report "earnings" that include PIK (Payment-In-Kind) interest — non-cash income from borrowers who can't pay. This inflates reported NII but doesn't generate cash to cover dividends.

**Cash Coverage Ratio = Cash NII / Dividend**
- Cash NII = Total NII - PIK Interest  
- Ratio <1.00x = BDC is burning cash reserves
- Ratio <0.90x = Dividend cut imminent

### Canary BDCs (High PIK = High Risk)
| BDC | Ticker | PIK % of Income | Status | Implication |
|-----|--------|-----------------|--------|-------------|
| **Prospect Capital** | **PSEC** | **35%** | 🔴 **CRITICAL** | Highest PIK concentration, likely burning cash, dividend cut risk |
| **FS KKR Capital** | **FSK** | **27%** | 🟠 **HIGH RISK** | Second-highest PIK, watch for following PSEC |

**If PSEC cuts dividend → validation that middle market stress is real → banks next**

### Q1 2026 Coverage Estimates (Baseline Being Established)
| Ticker | BDC Name | Cash Coverage | Status | Next Report | Notes |
|--------|----------|---------------|--------|-------------|-------|
| **PSEC** | Prospect Capital | **TBD** | 🔴 | ~Feb 20 | 35% PIK - highest risk |
| **FSK** | FS KKR Capital | **TBD** | 🟠 | ~Feb 15 | 27% PIK - close second |
| **TCPC** | TCP Capital | **TBD** | 🟡 | Mid-Feb | Middle market exposure |
| **MFIC** | MidCap Financial | **TBD** | 🟡 | ~Feb 20 | Middle market focus |
| **BXSL** | Blackstone Secured | **TBD** | 🟢 | ~Feb 15 | Senior secured, defensive |
| **ARCC** | Ares Capital | **TBD** | 🟢 | Quarterly | Largest, quality benchmark |
| **GSBD** | Goldman Sachs BDC | **TBD** | 🟢 | Quarterly | Small but high quality |

**Status Legend:**
- 🟢 Coverage >1.00x (sustainable)
- 🟡 Coverage 0.90-1.00x (tight)  
- 🟠 Coverage 0.75-0.90x (unsustainable)
- 🔴 Coverage <0.75x or dividend cut

### Why This Matters for Regional Banks

**Transmission Path #1: Direct Bank Exposure**
- Banks provide **$1.2T in loans to non-depository financial institutions** (VX-REG-6.05)
- Includes fund finance, warehouse lines, NAV-based loans to BDCs
- BDC dividend cuts → NAV crashes → loan covenant violations → bank losses

**Transmission Path #2: Credit Cycle Confirmation**
- BDCs lend to middle market companies (non-investment grade)
- PIK spike = companies can't pay CASH interest anymore  
- This is **early warning** that credit stress is spreading
- Bank corporate loan losses lag 2-4 quarters

**Canary Signal Hierarchy:**
1. **BDC PIK spikes** (already happened — PSEC 35%, FSK 27%)
2. **BDC cash coverage <1.00x** ← WE ARE HERE
3. **BDC dividend cuts** (next phase — watch PSEC/FSK)
4. **Bank C&I loan delinquencies rise** (lags by 2-3 quarters)
5. **Bank fund finance losses** (CFG, WAL exposure)

### Monitoring Protocol

**Weekly Check (Every Monday):**
1. Scan for monthly reports from PSEC, FSK, TCPC, MFIC, BXSL
2. Extract: Cash NII, PIK income, Dividends declared
3. Calculate Cash Coverage Ratio  
4. Flag threshold breaches

**Monthly Deep Dive (First Friday):**
1. Update `domain/workbook/BDC_CASH_COVERAGE.tsv` with all available data
2. Calculate trend: Coverage improving or deteriorating?  
3. Update ML.tsv with significant findings
4. Update this STATUS.md dashboard

**Immediate Alert Triggers:**
- Any BDC cash coverage crosses below 0.90x for first time
- Any dividend cut announcement (automatic RED status)
- PSEC or FSK coverage <0.80x (sector canary flashing)
- ARCC struggling (if quality leader fails, sector is broken)

### Where to Find Monthly Data

**Monthly Reporters (Fastest Signal):**
- **PSEC**: ~20th of month → https://www.prospectstreet.com/investor-relations/monthly-portfolio-statistics
- **FSK**: ~15th of month → https://www.fskkcapital.com/investor-relations  
- **TCPC**: Mid-month → https://ir.tcgbdc.com/financial-information/monthly-stockholder-reports
- **MFIC**: ~20th of month → https://ir.midcapfinancial.com/financial-information
- **BXSL**: ~15th of month → https://ir.bxsl.com/financial-information/monthly-reports

**Quarterly Reporters (Lag Signal):**
- **ARCC**: 45 days post-quarter → https://ir.arescapitalcorp.com  
- **GSBD**: Quarterly → https://www.goldmansachsbdc.com/investor-relations

### Data Extraction Method
From monthly reports:
1. Find "Interest Income" breakdown
2. Separate "Cash Interest Income" from "PIK Interest Income"  
3. Calculate: Cash NII = Total NII - PIK Income
4. Compare to monthly dividend (usually 1/3 of quarterly rate)
5. Cash Coverage = Cash NII / Monthly Dividend

**Example (PSEC Hypothetical):**
```
Total NII: $25M  
PIK Income: $9M (35%)
Cash NII: $16M
Monthly Dividend: $18M
Coverage: 0.89x → 🟡 YELLOW (tight, watch closely)
```

### Bank Vectors to Monitor When BDC Coverage Fails
- **VX-REG-6.05 (CFG)**: Fund finance leader, $10-11B exposure
- **VX-REG-6.04 (WAL)**: Multi-channel stress includes fund finance  
- **VX-REG-2.03**: BDC NAV discount (already -16% avg, -21% median)
- **BROCK sub-agent**: Tracks BDC sector stress comprehensively

### Historical Context: The PIK Inflation Era (2023-2025)
| Period | PSEC PIK % | FSK PIK % | Implication |
|--------|-----------|-----------|-------------|
| **2022** | ~15% | ~18% | Normal range |
| **2023** | ~22% | ~22% | Starting to spike |
| **2024** | ~30% | ~25% | Acceleration |
| **Q4 2025** | **35%** | **27%** | Critical levels |

**Pattern:** When companies can't pay cash interest, they convert to PIK. BDCs report "earnings growth" but are actually burning cash. Eventually dividends must be cut.

**Golub Capital signal:** PIK interest spiked **+173% YoY** (2024-2025) — sector-wide phenomenon, not idiosyncratic.

### Q1 2026 Action Items
1. ✅ Framework created (Feb 11, 2026)
2. ⏳ Pull Jan 2026 data from monthly reports (PSEC ~Feb 20, FSK ~Feb 15)
3. ⏳ Establish baseline coverage ratios for all 7 BDCs
4. ⏳ Begin weekly monitoring routine
5. ⏳ First monthly update: Early March 2026

**Full tracking framework:** `domain/workbook/BDC_CASH_COVERAGE.tsv`

---

### CRE Maturity Wall (Fed Z.1, Q3 2025)

| Metric | Value | Implication |
|--------|-------|-------------|
| **Total CRE Debt** | $4.88T | Banks hold 36.3% ($1.77T) |
| **Bank 2026 Maturities** | $359B | 20% of book must refi this year |
| **Bank 2025-2026 Total** | $488B | 28% of book in near-term stress window |
| **Bank YoY Growth** | +1.7% | Cautious — barely expanding |
| **Securitized 2026** | $174B | 23% of book — even more front-loaded |

**The stress point:** $488B of bank CRE maturing by end of 2026. Loans from 3.5% era hitting 7%+ refi rates. LTVs blown, DSCRs don't work. Extend & pretend running out of runway.

**Full data:** `domain/workbook/CRE_MATURITY.md` | **Source:** `domain/sources/Trepp_CRE_Universe_Feb2026.md`

---

## Core Thesis: The Convergence

**Eight independent research streams all terminate at regional banks.**

This wasn't designed — it emerged from research. Regional banks are the common node where all stress transmits:

| Channel | Source Agent | Mechanism |
|---------|--------------|-----------|
| **CRE** | REGINALD/CREED | 70% of CRE loans at regionals, extend-and-pretend masking 70-97% loss severity |
| **NDFI/Auto Fraud** | OTTO | $1.7T bank exposure to non-depository lenders, $591M+ losses disclosed |
| **Federal Layoffs** | LABOR | DOGE cuts hitting DC corridor banks (EGBN, BHRB) |
| **Consumer Credit** | CARL | 37% of Americans can't cover $400, stress transmission accelerating |
| **BDC/Fund Finance** | BROCK | $1.2T bank-NDFI exposure, PIK masking 6% shadow defaults, AI infrastructure risk emerging |
| **Migration** | MARCO | Border city stress, FL triple exposure, workforce exit |
| **FHLB/Funding** | LIQUID | RRP at zero, FHLB is convergence point for all stress |
| **Japan Contagion** | SAM | Repatriation → UST → CLO → BDC → banks |

**The key insight:** Banks with exposure to MULTIPLE channels have more "paths to break." The convergence thesis says these channels will correlate during stress.

---

## The Matrix: What It Reveals

### Convergence Score Rankings (Multi-Channel Exposure)

| Rank | Bank | Score | Primary Vulnerabilities |
|------|------|-------|------------------------|
| 1 | **EGBN** | 12 | Pure DC (100%), already in crisis, CRE 547% |
| 2 | **WAL** | 10 | NDFI + Fraud + Fund Finance + FHLB + **$1.36B unrated muni "shadow book"** |
| 3 | **VLY** | 9 | NYC/NJ multi-family primary + BDC + Consumer — FL is 27% but diversified |
| 4 | **CFG** | 9 | Fund finance ($10-11B) + Consumer 18.7% + FHLB 5.1% |
| 5 | **ZION** | 9 | **$5.78B total muni exposure** (hidden) + NDFI fraud + $524M unfunded |

### Key Pattern: Multi-Channel > Single-Channel

Pure plays (EGBN, SBCF, IBOC) are binary bets on one geography. Multi-channel names (WAL, VLY, CFG, ZION) have multiple paths to stress — they don't need ALL channels to break, just 2-3 to correlate.

### Hidden Exposures Discovered

| Bank | What Market Sees | What We Found |
|------|------------------|---------------|
| **ZION** | $1.4B muni securities | $5.78B total (+ $4.36B loans + $524M unfunded) |
| **WAL** | $2.28B muni securities | $1.36B is UNRATED = private placements, shadow loan book |
| **CFG** | Big muni investor? | **$1M** — they're not in munis at all |

---

## Geographic Stress Analysis

### DC Corridor — The "Value Trap vs Apex Predator" Split

| Bank | DC % | Verdict | Why |
|------|------|---------|-----|
| **EGBN** | 100% | "Value Trap" | Already taking pain ($140.8M NCOs Q3), may be priced for distress |
| **BHRB** | 35% | "Safe Harbor" | Hedged via WV/KY merger, but $922M muni portfolio at risk |
| **AUB** | 25% | "Apex Predator" | Purged Sandy Spring CRE, defense-focused, 0% NCOs in GovCon |

**Municipal fracture:**
- DC proper: Moody's NEGATIVE outlook, $140M annual revenue loss
- PG County: AAA but Moody's negative watch (9% federal workforce)
- NoVA: AAA maintained — "Defense Shield" from national security contractors

### Florida — The "Coral Bleaching" (See CORAL Sub-Agent)

**🟠 CORAL Status: ORANGE — Stress Accumulating, Catalyst Pending**

The FL thesis has grown into its own sub-agent. Key findings from RP-FL research:

**The Evolved Doom Loop:**
- Citizens has SHRUNK (1.42M → 385K policies) — risk shifted to private insurers
- 14 companies under OIR "Enhanced Monitoring" (~15% of domestic market)
- Insurance channel now AMPLIFIER, not primary trigger
- Primary trigger = **condo reserve cascade** (SIRS mandate + special assessments)

**Condo Crisis Metrics:**
- 1,438 associations on Fannie/Freddie blacklist (696 in Miami/Palm Beach)
- +44% complaint surge FY 2024/2025
- Palm Greens bankruptcy ($43.7M) — first association bankruptcy of cycle
- Heron Pond auction: $67K/unit vs $180-210K market (**60% discount = valuation floor**)
- 1,500 associations at high risk by 2027

**Biscayne 21 Ruling (Oct 2025):** FL Supreme Court upheld 100% owner consent for termination. Developer buyouts frozen — receivership is now the primary resolution path. **Extended workout timelines for banks.**

| Bank | FL Concentration | Specific Exposure | Risk | Notes |
|------|------------------|-------------------|------|-------|
| **SBCF** | **~100%** | Pure FL ($16B) | 🟢 SKIP | Fortress (14.4% CET1), M&A target, counter-cyclical strategy |
| **CNB** | ~100% | Pure FL | 🟠 HIGH | Small, less liquid |
| **BKU** | ~47% | Miami commercial | 🟢 SKIP | Well-managed (12.3% CET1), credit improving |
| **SSB** | FL 23% + TX 19% | **$17.9B CRE (37%)** | 🔴 **POSITION** | **2x $90P Jun 18 — MF 9.36% substandard, "Support & Survive" masking stress** |
| **VLY** | **27%** | $14B of $51B loans | 🟡 MODERATE | **NJ/NY is primary market** — FL is secondary exposure |
| **ABCB** | ~22% | SE regional | 🟡 MODERATE | Diversified, FL not dominant |
| **HOMB** | 28% | $4.15B | 🟢 PREPARED | **$33M hurricane reserve** — proactive management |

**VLY Deep Dive (Updated Feb 11 from FL Research):**
- **27.3% FL exposure** ($14.0B of $51.2B loans) — significant but NOT primary market
- **NJ/NY is primary vulnerability** — multi-family rent stabilization, office conversion pressures
- Already struggling: dividend cut, strategic review announced
- Non-accruals trending up: 0.72% → 0.87% (H2 2025)
- De-risking via Brookfield sale ($1B at 1% discount)
- **Trading implication:** VLY is multi-channel stress play, not pure FL bet
- **For pure FL exposure:** SBCF (~100% FL) is cleaner expression

**Full Florida analysis:** `sub-agents/CORAL/STATUS.md`

### Texas Border — The Absence

**No major KRE constituent has TX border exposure.**
- IBOC (IBC Bank) is the only publicly traded bank with Laredo/McAllen dominance
- MARCO thesis impacts IBOC directly, but doesn't transmit through KRE
- Water crisis in Laredo (S&P flagged), pension stress in El Paso

---

## Bank Watchlist (Updated Ratings)

### Tier 1: Maximum Stress (4+ channels)

| Ticker | Bank | Rating | Convergence Score | Primary Risk |
|--------|------|--------|-------------------|--------------|
| **EGBN** | Eagle Bancorp | 🔴 RED | 12 | DC 100% + CRE 547% + already in crisis |
| **WAL** | Western Alliance | 🔴 RED | 10 | Multi-channel: NDFI + Fraud + Fund Finance + FHLB + Unrated Munis |
| **VLY** | Valley National | 🟠 ORANGE | 9 | **NYC/NJ multi-family primary risk** — FL is 27% but diversified; dividend cut, profitability struggles already manifesting |

### Tier 2: Elevated Multi-Channel

| Ticker | Bank | Rating | Convergence Score | Primary Risk |
|--------|------|--------|-------------------|--------------|
| **CFG** | Citizens Financial | 🟠 ORANGE | 9 | Fund finance ($10-11B) + Consumer + FHLB |
| **ZION** | Zions Bancorp | 🟠 ORANGE | 9 | $5.78B muni exposure + NDFI fraud + unfunded |
| **BHRB** | Burke & Herbert | 🟠 ORANGE | 5 | DC exposure + munis = majority of AFS |
| **MTB** | M&T Bank | 🟡 YELLOW | 4 | 61% NY State muni concentration |

### Tier 3: Geographic Pure Plays

| Ticker | Bank | Rating | Region | Trade Expression |
|--------|------|--------|--------|------------------|
| **SBCF** | Seacoast Banking | 🟢 SKIP | FL ~100% | Fortress balance sheet (14.4% CET1), M&A target risk |
| **BKU** | BankUnited | 🟢 SKIP | FL ~47% | Well-managed (12.3% CET1, credit improving) |
| **SSB** | SouthState | 🔴 **POSITION** | FL ~36% + TX | **2x $90P Jun 18 — MF 9.36% substandard, 64% floating, HOA direct** |
| **IBOC** | Int'l Bancshares | 🟠 ORANGE | TX Border | MARCO thesis (only publicly traded option) |

### Tier 4: Defensive/De-Risked

| Ticker | Bank | Rating | Why |
|--------|------|--------|-----|
| **AUB** | Atlantic Union | 🟢 GREEN | "Apex Predator" — purged CRE, defense-focused |
| **HOMB** | Home BancShares | 🟢 GREEN | $33M hurricane reserve, proactive management |
| **MTB** | M&T Bank | 🟢 GREEN | CRE down from 183% to 124%, model de-risker |

---

## Current Position Context

**Live Positions (Feb 11, 2026):**

| Ticker | Position | Expiry | Entry | Risk | Thesis |
|--------|----------|--------|-------|------|--------|
| KRE | 2x $70P | May 15 | — | ~$400 | Broad regional bank stress |
| KRE | 2x $60P | Jun 18 | — | ~$400 | Tail risk / cascade |
| HYG | 10x $75P | Jun 18 | $0.30 | $307 | Credit canary (cracks before banks) |
| IWM | 1x $250P | Jun 30 | ~$7.50 | ~$750 | Small cap stress transmission |
| **SSB** | **2x $90P** | **Jun 18** | **$1.86** | **$373** | **FL single-name — MF stress visible** |

**Total defined risk:** ~$2,230

**KRE captures broad stress but:**
- Includes "apex predators" (AUB) and "prepared" names (HOMB)
- Averages across all geographies
- SSB is the targeted FL/TX single-name expression

**SSB thesis (CORAL):**
- MF substandard 9.36% (highest CRE category), NPLs 0.02%
- "Support and Survive" masking true stress
- 64% floating rate = Fed sensitivity
- FL 23% + TX 19% = Sunbelt correlation risk
- Full thesis: `sub-agents/CORAL/research/SSB_THESIS.md`

---

## Key Signals to Monitor

| Signal | Current | Status | Trigger |
|--------|---------|--------|---------|
| **NFP (Feb 7)** | Pending | 🟡 | <100K or negative = risk-off |
| **Japan 30Y auction (Feb 5)** | Tomorrow | 🟡 | Weak auction = repatriation pressure |
| **EGBN stock** | Distressed | 🟠 | Below $19 or capital raise |
| **Laredo water levels** | S&P flagged | 🟡 | Moratorium = development halt |
| **Citizens assessment** | None active | 🟢 | Any activation = FL credit event |
| **WAL fraud resolution** | Pending | 🟡 | Insurance denial = reserve increase |
| **First Brands examiner (Feb 25)** | Pending | 🟡 | Findings = OTTO thesis validation |
| **FL condo listings** | +56% YoY | 🟠 | Continued surge = market dysfunction |
| **FL blacklist count** | 1,438 | 🟠 | Growth toward 2,000 = acceleration |
| **FL association bankruptcies** | 1 (Palm Greens) | 🟡 | Cluster of 3-5 = thesis validation |
| **VLY non-accruals** | 0.87% | 🟡 | >1.0% = FL stress manifesting |
| **VLY Q1 earnings (~Apr 23)** | Pending | 🟡 | HOA loan performance, reserve build |
| **SSB MF substandard** | 9.36% | 🟠 | Watch for NPL migration (currently 0.02%) |
| **SSB Q1 earnings (~late Apr)** | Pending | 🟡 | NCO trajectory, MF commentary, reserve changes |
| **Stablecoin market cap** | ~$180B | 🟡 | Growth >$200B/year = deposit pressure |
| **Fed H.8 deposit data** | Weekly | 🟡 | Regional bank deposit outflows |
| **CUBI earnings** | Quarterly | 🟡 | Crypto deposit trends, regulatory updates |

---

## What Would Change Our View

**More bearish:**
- Hurricane hits FL urban corridor → Citizens assessment → doom loop activates
- Additional NDFI fraud discoveries
- FHLB tightens collateral requirements
- NFP goes negative
- BDC dividend cuts cascade

**More bullish:**
- Fed cuts 100bp+ (extends runway)
- Employment holds better than leading indicators
- Congress reverses DOGE cuts
- VLY/WAL beat earnings cleanly
- Reinsurers return to FL market

---

## ⚠️ THESIS HEADWIND: Fed Regulatory Relief (Feb 11, 2026)

**Development:** Fed announced it will "drop some prior demands for banks to address deficiencies and reassess certain warnings issued to individual lenders."

**Impact on thesis:**
- Banks get more runway to "extend and pretend"
- Stress recognition DELAYED
- Classified → NPL migration slows
- Regulatory pressure removed = longer fuse

**Assessment:** Does NOT fix underlying credit quality — just lets banks hide it longer. Could actually make the eventual break WORSE (larger loss recognition when it finally comes). But extends timeline.

**Position implication:** May need longer-dated puts if forbearance becomes sustained policy. June may be tight.

---

## Sub-Agents

### RENO (Nevada Stress Monitor) 🟡 YELLOW — **[NEW - BUILDING]**
Monitors Nevada's converging stress channels: Canadian tourism decline, housing vulnerability, water crisis. Nevada is a "canary state" — led into 2008 crisis by 6-12 months.

**Key channels:**
- Tourism (25% of GDP, Canadian exposure)
- Housing (2008 epicenter, boom/bust)
- Water (Lake Mead, structural constraint)

**Bank transmission:** WAL (Bank of Nevada), ZION (Nevada State Bank)

**Files:** `sub-agents/RENO/STATUS.md`, `sub-agents/RENO/research/RENO_RESEARCH_PROMPTS.md`

### CORAL (Florida Real Estate Stress) 🟠 ORANGE
Monitors Florida condo crisis and transmission to regional bank balance sheets. Owns the "Coral Bleaching" thesis — SIRS mandates, insurance stress, bridge loans, developer activity.

**Key metrics tracked:**
- Fannie/Freddie blacklist (1,438 → watch for 2,000)
- Association bankruptcies (1 so far)
- VLY non-accruals (0.87% and rising)
- Insurance channel health (14 under OIR monitoring)

**Files:** `sub-agents/CORAL/STATUS.md`, `sub-agents/CORAL/workbook/`

### CREED (CRE Deep Dive) 🟠 ORANGE
Monitors commercial real estate stress — delinquencies, valuations, maturity walls.

**Current signals:**
- Office CMBS DQ: **12.34%** (ATH, exceeds GFC peak)
- Special Servicing: **17.16%** (2x GFC)
- Maturity Wall: **$936B** in 2026, ~$336B refinancing gap
- Loss Severity: 49.7-63% (vs 20-40% in bank models)
- Bank mods +66% YoY, re-defaults +90% YoY

**Key finding:** Extend-and-pretend masking stress. Employment is the trigger that breaks it.

**Predictions:** 5 active | See `CREED/STATUS.md`

---

### BROCK (BDC & Private Credit) 🟠 ORANGE
Monitors Business Development Companies and private credit stress.

**Current signals:**
- PIK concentration: PSEC 35%, FSK 27%, BXSL 20%
- Shadow default rate: ~6% (vs reported 2.1%)
- >50% of BDCs burning cash (dividends > cash generated)
- Bank-NDFI exposure: **$1.2T** (10.4% of bank loans)

**NEW — AI Infrastructure Risk:**
- $450B+ deployed to tech/AI via private credit
- GPU collateral depreciates 40-60% in 18mo vs 6-year loans
- **HRZN collapsed 21%** (forced Monroe merger) — first AI canary
- Nvidia has $110B customer financing (vs Lucent's $15B in 2000)
- Blue Owl walked from Oracle data center deal

**Two transmission paths to KRE:**
1. **Classic:** CRE stress → Bank CRE losses → KRE (CREED)
2. **NEW:** AI Capex → Neocloud/BDC NAV → Bank fund finance → KRE (BROCK)

**Canaries:** PSEC (PIK), HRZN (AI/tech)
**Predictions:** 11 active | See `sub-agents/BROCK/STATUS.md`

---

## Key Files

- **BANK_EXPOSURE_MATRIX.md** — Complete 8-channel convergence analysis
- **research/outputs/RP-REG-3.*/** — Geographic and municipal research reports
- **research/outputs/RP-FL-*/** — Florida thesis research (6 reports)
- **sub-agents/CORAL/** — Florida sub-agent (STATUS, workbook, DATA_SOURCES)
- **workbook/** — ML.tsv, VX.tsv, FL.tsv evidence logs

---

## Open Questions

1. **VLY vs SBCF for single-name short?** VLY has quantifiable exposure + no M&A floor; SBCF is purest FL expression but smaller, potential takeover target
2. Will Santander/Webster deal trigger more regional M&A (floor under shorts)?
3. How long until ZION's $524M unfunded muni commitments get tested?
4. Is EGBN's distress already priced, limiting short upside?
5. **How many association bankruptcies before bank reserves build?** Palm Greens was first — watch for cluster
6. **Will 2026 hurricane season stress reformed insurance market?** First real test post-SB 2-A

---

*This document reflects current understanding. The BANK_EXPOSURE_MATRIX.md contains the detailed evidence. Update when interpretation changes.*
