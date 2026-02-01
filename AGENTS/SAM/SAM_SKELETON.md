# SAM DOMAIN SKELETON v1.3

# Purpose: Structural scaffold for LLM domain orientation
# Domain:  Japan Sovereign, BOJ Policy, JGB Markets, Yen Carry Trade,
#          Life Insurer Repatriation, CLO Transmission, Global Liquidity
# Agent:   SAM (Samurai - Japan-focused monitoring agent)
#
# Version: 1.3
# Created: 2025-12-16
# Updated: 2026-01-23 (Research Update)
# Author:  SAM-X Session
#
# Usage:
#   - Load this file at the start of any SAM session
#   - Provides entity types, relationship vocabulary, core architecture
#   - Named transmission paths define known cascade routes
#   - Thresholds define tripwires for escalation
#
# CRITICAL: v1.3 adds Norinchukin stabilization (CLO nuclear ↓), Feb auction
#           calendar (Feb 5 30Y key), election seat math (LDP 29.7% vs Takaichi 70%+)
#
# Methodology Compliance: Aligned with CARL Methodology Skeleton v0.2

---

## 0. QUICK START

*Load this section for any session. Provides minimum viable orientation.*

### About This System

A **session** is one continuous LLM interaction window. Sessions are numbered sequentially (SAM-I, SAM-II, etc.). At session end, handoff documents transfer context to the next session.

**Storage:** Log entries (ML, FL, FLOW, VX) are maintained in the JPN_LOGS workbook. The workbook and handoff documents are saved locally and uploaded to project files.

**Two Documents:**
- **Domain skeleton** (this document): Defines *what* SAM monitors — entities, vectors, glossary, thresholds
- **Methodology skeleton** (separate): Governs *how* to operate — principles, protocols, templates

Load both at session start.

### Current Thesis

**PRIMARY THESIS: The Impossible Trilemma (EVOLVED)**

Japan faces a three-way policy collision with no exit:

1. **DEFEND YEN** → Requires BOJ rate hikes (triggers carry unwind, JGB valuation compression)
2. **SUPPORT JGB MARKET** → Requires low rates or unlimited buying (destroys yen, monetizes deficit)
3. **FUND FISCAL STIMULUS** → Requires market absorption (impossible if yields spike, buyers flee)

**EVOLUTION (Jan 20, 2026):** Original thesis focused on FX intervention as primary trigger. Bond market has now opened a **new crisis vector**. This is no longer primarily an FX crisis — it is a **fiscal sustainability crisis** manifesting first through bonds, then FX, then credit.

**Confidence:** Pattern 97% | Timing 82% | Magnitude 90%
**Status:** VALIDATED — JGB 30Y at all-time highs, 20Y auction failed Jan 20

**Invalidation Criteria:**
- BOJ explicitly abandons hike path AND announces QE expansion
- 30Y JGB yields fall below 3.00% and hold for 10+ consecutive days
- Life insurers announce INCREASING UST allocations
- Three consecutive JGB auctions clear with BTC >3.0x and minimal tails
- Fed/Treasury announces emergency facility for foreign UST holders

### Scenario Framework

SAM uses a **probability-weighted scenario tree** rather than binary hypothesis tracking. This accommodates macro environments where multiple equilibria are possible.

| Scenario | Probability | Description | Primary Vector |
|----------|-------------|-------------|----------------|
| **A/A+** | 12-17% ↑ | Soft landing via hawkish BOJ | VX-SAM-1.02 |
| **B** | 35-40% ↑ | Controlled chaos via intervention | VX-SAM-3.02 |
| **C** | 20-25% ↓ | Acute carry unwind panic | VX-SAM-3.01 |
| **D1** | 8-10% | Fiscal crisis → Austerity path | VX-SAM-1.05 |
| **D2** | 8-12% ↑ | Fiscal crisis → Monetary dominance | VX-SAM-1.05 |

*Updated Jan 23: Post-BOJ stabilization improves A/B scenarios slightly. BUT Feb 8 election risk keeps D2 elevated. Takaichi's 62-78% approval + fiscal expansion platform = monetary dominance risk.*

### Log Decision Tree

When you have new information, determine where it belongs:

```
IS IT ABOUT CURRENT/PAST STATE (what IS or WAS true)?
├─ YES → ML (Master Log)
│        Example: "30Y JGB hit 3.91% all-time high on Jan 20"
│
└─ NO → DOES IT HAVE A FUTURE DATE (something to watch for)?
        ├─ YES → FL (Future Log)
        │        Example: "BOJ decision Jan 23-24"
        │        CRITICAL: FL entries RETIRE when date passes
        │
        └─ NO → IS IT A STRUCTURAL RELATIONSHIP (if X, then Y)?
                ├─ YES → FLOW (Cascade Map)
                │        Example: "JGB yield spike → fiscal doom loop"
                │
                └─ NO → Probably ML, or doesn't need logging
```

### Entry ID Formats

| Log Type | Format | Example |
|----------|--------|---------|
| Master Log (Japan) | `ML-JPN-###` | ML-JPN-130 |
| Master Log (Global) | `ML-GL-###` | ML-GL-023 |
| Future Log | `FL-JPN-###` | FL-JPN-062 |
| Vectors | `VX-SAM-#.##` | VX-SAM-1.05 |
| Flows | `FLOW-JPN-#.##` | FLOW-JPN-1.06 |

### Coordinating Agents

| Agent | Domain | State Vector Exchange |
|-------|--------|----------------------|
| **LIQUID** | Treasury/Repo, Global Funding, FHLB, SOFR | VX-SAM-3.04 ↔ LIQUID funding stress |
| **REGINALD** | Regional Banks, Leverage, Deposit Flows | VX-SAM-3.04 ↔ REGINALD bank stress |
| **MASTER** | Cross-Domain Synthesis | Receives SAM scenario probabilities |
| **OTTO** | Auto Finance, ABS | CLO overlap via Norinchukin |

### Session Type Routing

| Session Type | Load Sections | Purpose |
|--------------|---------------|---------|
| Update | 0, 4 (thresholds) | Ingest new data, update logs |
| Analysis | 0, 3, 4, 6 | Deep dive on specific cascade |
| Crisis | 0, 3, 4, 11 | Active crisis monitoring |
| Reconciliation | 0, 4, 7 | Cross-reference audit, cleanup |
| Devil's Advocate | 0, 10 | Challenge primary thesis |
| Handoff | Full skeleton | Explicit knowledge transfer |

---

## 1. ENTITY TYPES

*The vocabulary of the domain. Every node belongs to exactly one entity type.*

### Japan Sovereign / Policy Entities

**Central_Bank (BOJ)**
- Singleton entity: Bank of Japan
- Key properties:
  - `jgb_holdings_pct`: Currently 80.1%+
  - `balance_sheet_total`: ¥750T+ (QT cut $502B from balance sheet)
  - `policy_rate`: 0.75% (Dec 2025 hike; Jan 23 held; highest since Sep 1995)
  - `ycc_status`: Abolished (was suspended Jul 2023)
- Key actors:
  - **Ueda Kazuo** (Governor): "Will continue raising rates if forecasts materialize"
  - **Takata Hajime** (Board): Dissented Jan 23 — wanted 1.0% (hawkish)
  - **Uchida Yoshimasa** (Deputy): Hospitalized late Nov — governance risk
- Jan 23-24 Decision: HELD (8-1 vote); raised GDP forecast FY2026 0.9% from 0.7%; inflation 1.9% from 1.8%

**Ministry (MOF/FSA/Kantei)**
- MOF: FX intervention authority, JGB issuance (~$130B FX reserves available)
- FSA: Bank/insurer regulation (ESR implementation)
- Kantei: PM Takaichi political direction

**Key Actor - External:**
- **Bessent Steven** (US Treasury Secretary): "The man who broke the BOJ" — pressing for rate normalization, Japan on Treasury Monitoring List, 24% tariff leverage

### Institutional Investors (Japan)

| Type | Key Holder | JGB Holdings | Foreign Holdings | Status |
|------|-----------|--------------|------------------|--------|
| Life Insurer | Big 4 | ¥30T+ | ¥40T+ (declining) | ESR constrained |
| Pension | GPIF | ¥68.9T | ¥60T+ | Mechanical rebalancing |
| Mega Bank | MUFG, Mizuho, SMFG | ¥80T+ | ¥15T+ | VaR constrained |
| Regional Bank | 64 banks | ¥200T+ | Limited | Capital erosion |
| Agricultural | Norinchukin | ¥3.8T | ¥8.2T CLOs (↓¥500B Q1) | STABILIZING — FY25 ¥1.9T loss realized; back to profit ¥26B Q2; planning ¥10T reallocation to corp debt |
| Postal | Japan Post Bank | ¥60T+ | ¥25T+ | Now BUYING JGBs |

### Transmission Entities (Japan → US/Global)

**CLO Market**
- AAA spread: 125bps current (threshold: 150 yellow, 180 red)
- Japan share: 5-7% of global AAA (Norinchukin dominant)
- Transmission speed: HOURS (fastest pathway)

**BDC (Business Development Companies)**
- Combined exposure: $142B unfunded commitments
- Stress drawdown: ~45% ($64B) based on 2020 precedent
- Transmission speed: DAYS

**US Regional Banks**
- CLO holdings + BDC credit lines
- Tracking proxy: KRE ETF
- Transmission speed: DAYS to WEEKS

**FHLB (Federal Home Loan Banks)**
- Advance rate threshold: >85%
- Delivery Status = 48-72 hour operational freeze
- Critical early warning indicator

---

## 2. RELATIONSHIP TYPES

*How entities connect. Every edge has exactly one relationship type.*

### Policy Relationships
- `holds`: Entity owns/holds assets (BOJ holds 80.1% of JGBs)
- `issues`: Entity creates securities (MOF issues JGBs)
- `intervenes`: Policy entity takes market action (MOF intervenes in FX)
- `constrains`: Regulation limits behavior (ESR constrains life insurer foreign holdings)

### Flow Relationships
- `repatriates`: Sells foreign assets, buys domestic (Life insurers repatriate UST → JGB)
- `hedges`: Manages FX or rate exposure (GPIF hedges USD exposure)
- `funds`: Provides credit/capital (Regional banks fund BDCs via credit lines)
- `draws`: Utilizes credit facility (BDCs draw bank lines in stress)

### Stress Relationships
- `transmits`: Stress propagates (Norinchukin CLO stress transmits to US BDCs)
- `amplifies`: Second-order factor worsens primary stress (SoftBank amplifies JGB yield stress)
- `correlates`: Statistical co-movement (S&P 500 correlates +0.7 with USD/JPY)

---

## 3. TRANSMISSION PATHS (Named Cascade Routes)

*Documented pathways for crisis propagation. Status as of Jan 20, 2026.*

### NEW: FLOW-JPN-1.06 — Fiscal Doom Loop

**ADDED: Jan 20, 2026 — PRIMARY ACTIVE CASCADE**

```
Speed: DAYS
Status: CRITICAL — ACTIVE (triggered Jan 17-20)
Layer: 1 (Domestic)

Pathway:
  Takaichi spending promises (Jan 17-19)
    → Bond market loses confidence in fiscal path
    → JGB yields surge (30Y +44bps in 3 days)
    → Debt servicing costs explode (240% debt-to-GDP)
    → Fiscal situation WORSENS (positive feedback)
    → Market questions: "Can Japan still fund itself?"
    → Yen WEAKENS (fiscal crisis signal, not strengthens)
    → BOJ forced to choose:
        Path D1: Hike aggressively
          → Economy slows → Tax revenue declines
          → Fiscal deficit widens → JGBs sell MORE
        Path D2: Restart QE/YCC
          → Yen collapse → Inflation imports surge
          → Global inflation spike → EM contagion

Trigger: 20Y JGB auction failure (CONFIRMED Jan 20)
Current Position: ACTIVE — 30Y at 3.68-3.91% (all-time high)
Key Insight: Both exit paths lead to worse outcomes than status quo
```

### FLOW-JPN-3.01 — CLO Nuclear Transmission

```
Speed: HOURS (fastest pathway)
Status: ELEVATED — ARMED (downgraded from CRITICAL Jan 23)
Layer: 3 (Global)

Pathway:
  Norinchukin Capital Breach
    → Forced CLO Liquidation (¥8.2T / 5-7% global AAA)
    → AAA CLO Prices Crash (>150-200bps spread widening)
    → US Banks Face Margin Calls (CLO collateral impaired)
    → Credit Lines Pulled / Lending Frozen
    → CREDIT CRUNCH (Systemic)

Trigger: Norinchukin capital breach OR CLO AAA >180bps
Current Position: AAA at 125bps (25bps cushion to Yellow 150bps)

UPDATE Jan 23: Norinchukin PAST ACUTE CRISIS
- FY2025 loss (¥1.9T) realized and absorbed
- Back to profitability (¥26B Q2 2025)
- CLO portfolio shrank ¥500B in Q1 (fastest decline on record)
- New leadership (Kitabayashi since Apr 2025)
- Planning ¥10T reallocation sovereign → corporate (including CLOs)
- Near-term probability REDUCED to ~8% (was 15%)
- Still marginal price-setter; pathway remains armed but less likely
```

### FLOW-JPN-4.01 — BDC/Bank Hidden Feedback Loop

```
Speed: DAYS
Status: LATENT — Activates on CLO stress
Layer: 4 (US Domestic)

Pathway:
  CLO/Credit Stress (FLOW-JPN-3.01 triggers)
    → BDC Portfolio Losses (mark-to-market)
    → BDCs Draw Bank Credit Lines ($142B unfunded / ~45% = $64B)
    → Bank Liquidity Drain (exactly when banks need cash)
    → Deposit Flight Accelerates
    → Banks Forced to Sell Assets
    → Credit Spreads Widen Further
    → [LOOP REINFORCES]

Trigger: CLO AAA >165bps (BDC mark-downs begin)
Current Position: LATENT — awaiting CLO trigger
Key Insight: Hidden second-order effect through shadow banking
```

### FLOW-JPN-2.03 — J-SOLV Structural Demand Void

```
Speed: PERMANENT (regulatory architecture change)
Status: CRITICAL — CONFIRMED
Layer: 2 (Cross-Border)

Pathway:
  ESR Regulation Implementation (June 2025)
    → Punitive Capital Charges for Unhedged FX
    → Life Insurers PERMANENTLY Exit Foreign Bonds
    → ~$120B/yr Structural Void in UST Demand
    → No Panic Selling BUT No Dip Buying (Stabilizer Put GONE)
    → Chronic UST Auction Weakness (lower BTC, wider tails)
    → Term Premium Rises Structurally

Trigger: ESR implementation June 2025
Current Position: Final Adjustment Phase
Key Insight: Regulatory architecture change, not cyclical
```

### FLOW-JPN-3.02 — Desperation Swap Feedback Loop

```
Speed: MONTHS
Status: ACTIVE — Swap complete, awaiting recession trigger
Layer: 3 (Global)

Pathway:
  Japanese Institutions Sell Sovereigns (UST/EGB) — Negative carry
    → Buy Corporate Credit (CLOs/Corp Bonds) — Positive carry
    → [WAIT: US Recession Trigger]
    → Credit Positions Suffer Losses
    → Mark-to-Market Destroys Capital
    → Forced Selling of Credit Positions
    → Japan Institutional Stress AMPLIFIED by US Recession

Trigger: US recession signal (PMI <45, unemployment >5.5%)
Current Position: Swap complete; recession trigger not yet activated
Key Insight: Traded interest rate risk for credit cycle risk
```

### FLOW-JPN-3.03 — Private Market Contagion

```
Speed: WEEKS
Status: ACTIVE — Hidden exposure
Layer: 3 (Global)

Pathway:
  Norinchukin Liquidity Stress
    → Sells LP Stakes at 15-20% Discount ("ATM Mechanism")
    → Hidden CRE/Leasing Exposure (GreenV) Crystallizes Losses
    → Additional Capital Erosion Beyond Bond Losses
    → Accelerates Path to Capital Breach
    → Increases Probability of CLO Nuclear Trigger

Trigger: LP sales accelerate >$2B; CRE writedowns disclosed
Current Position: LP sales ongoing at $1.5-2.0B
Key Insight: Opaque accelerant; could surface suddenly
```

### FLOW-JPN-1.05 — Rural Political Feedback Loop

```
Speed: MONTHS
Status: ACTIVE — Building
Layer: 1 (Domestic Political)

Pathway:
  Norinchukin Investment Losses (¥1.5T+)
    → Capital Call on JA Co-ops (¥1.3T)
    → Dividend Cuts to Co-ops
    → Rural Communities Lose Farm Subsidies/Equipment Financing
    → Agricultural Distress → Political Pressure
    → Rural Caucus Pressures Takaichi Coalition
    → Political Constraint on BOJ Rate Normalization

Trigger: Rural caucus Diet statements; Takaichi links BOJ to rural pain
Current Position: ¥1.3T capital extraction confirmed; political pressure building
Key Insight: ¥1.3T = "Effective Tax on Japanese Agriculture"
```

---

## 4. THRESHOLDS (Consolidated Tripwires)

*All escalation thresholds. Updated Jan 20, 2026.*

**Color Coding:** 🟢 GREEN = Normal | 🟡 YELLOW = Watch | 🟠 ORANGE = Alert | 🔴 RED = Critical

### JGB YIELDS — HIGHEST PRIORITY (NEW PRIMARY VECTOR)

| Maturity | Current (Jan 23) | Yellow | Orange | Red | Status |
|----------|------------------|--------|--------|-----|--------|
| **10Y JGB** | 2.26% | 2.40% | 2.50% | 2.70% | 🟡 YELLOW (off peak) |
| **20Y JGB** | 3.48% | 3.30% | 3.50% | 3.70% | 🟠 ORANGE |
| **30Y JGB** | 3.67% | 3.50% | 3.75% | 4.00% | 🟠 ORANGE (off 3.91 ATH) |
| **40Y JGB** | 4.24% | 3.80% | 4.00% | 4.30% | 🔴 RED (record) |

**Context:** Post-BOJ meeting partial stabilization. 10Y fell from 2.33% to 2.26%. 30Y off peak. BUT 40Y still at record 4.24%. 20Y auction FAILED Jan 20 remains critical signal.

### CLO SPREADS — TRANSMISSION VECTOR

| Metric | Current | Yellow | Orange | Red | Critical |
|--------|---------|--------|--------|-----|----------|
| **AAA Spread** | 125bps | 150bps | 165bps | 180bps | 200bps+ |

**Cushion to Yellow:** 25bps
**Additional Triggers:**
- Norinchukin capital breach = immediate 🟠 ORANGE
- CLO sale >¥500B = immediate 🔴 RED
- Concurrent FTD >$50B = accelerated timeline

### USD/JPY & FX

| Metric | Current (Jan 23) | Threshold | Status |
|--------|------------------|-----------|--------|
| **USD/JPY** | 158.55 | 160 (GPIF trigger) | 1.45 handles away |
| **CCY Basis** | -45bps | -60bps (forced selling) | 15bps cushion |

**Note:** FX is SECONDARY to JGB yields. Yen weakened post-BOJ as expected. 160 intervention level still key. State Street: terminal rate 1.25%, possibly 1.5% if 160 breaches.

### US FUNDING / LIQUIDITY

| Metric | Current | Yellow | Red | Status |
|--------|---------|--------|-----|--------|
| **SOFR** | 3.67% | +15bps above IORB | +25bps | 🟢 GREEN |
| **RRP Balance** | $2.5B | <$50B | <$5B | 🔴 DEPLETED |
| **FTD** | $42.4B | $40B | $50B | 🟡 YELLOW |
| **FHLB Advance** | Normal | >85% | Delivery Status | 🟢 GREEN |

### AUCTION HEALTH

| Auction | Stress Signal | Current Status |
|---------|---------------|----------------|
| **JGB 20Y** | BTC <2.5x, tail >5bps | 🔴 FAILED (Jan 20) |
| **JGB 30Y/40Y** | BTC <2.5x | Watch for contagion |
| **UST** | BTC <2.3x, Indirect <60% | Normal |

### CORRELATION THRESHOLDS

| Pair | Current | Breakdown Signal | Meaning |
|------|---------|------------------|---------|
| **USD/JPY ↔ SPX** | +0.7 | <+0.4 | S&P liquidity-dependent on yen carry |
| **UST ↔ SPX** | -0.4 | >0 (positive) | Risk parity deleverages BOTH |

---

## 5. AMPLIFIERS (Second-Order Risk Multipliers)

*Amplifiers worsen existing crises but do not originate them.*

### Tier 1: Institutional

| Amplifier | Trigger | Amplifies | Conditional P |
|-----------|---------|-----------|---------------|
| **SoftBank Crisis** | Spreads >500bps OR Arm <80 | VX-SAM-1.01, VX-SAM-2.02 | 70% given JGB 3.5%+ |
| **AI Bubble Burst** | Nasdaq >15% drawdown | VX-SAM-2.02 | Chained with SoftBank |
| **Regional Bank Cascade** | Any midsize negative capital | VX-SAM-2.02, VX-SAM-1.01 | If 3+ distressed |
| **GPIF Rebalancing** | USD/JPY >160 OR <130 | VX-SAM-2.01 | Mechanical |
| **Norinchukin Stress** | CLO >180bps OR new fraud | VX-SAM-3.04, VX-SAM-2.01 | Straddles Japan-US |

### Tier 2: Political

| Amplifier | Trigger | Amplifies | Notes |
|-----------|---------|-----------|-------|
| **Takaichi Coalition** | 2-3 seat by-election loss | VX-SAM-1.04 | 231 seats (need 233) |
| **MOF/Kantei Breakdown** | MOF unilateral intervention fails | VX-SAM-3.02, VX-SAM-1.04 | Authority erosion |
| **Bessent Pressure** | Links BOJ hold to tariffs | VX-SAM-1.02, VX-SAM-3.02 | External constraint |
| **China Retaliation** | Sanctions or Taiwan incident | VX-SAM-1.04 | Delays hike but worsens crisis |

### Tier 3: Market Structure

| Amplifier | Trigger | Amplifies | Transmission |
|-----------|---------|-----------|--------------|
| **CLO Dysfunction** | Credit event; AAA >150bps | VX-SAM-3.04 | Hours to US regionals |
| **Credit Spread Collapse** | Recession + carry unwind sync | VX-SAM-3.04, VX-SAM-2.01 | HY currently 400bps |
| **Intervention Failure** | Physical intervention + rally | VX-SAM-3.01 | P(panic) = 95% |
| **SOFR Spike** | +50bps above IORB | VX-SAM-3.04 | Paralyzes USD funding |

---

## 6. VECTOR REGISTRY

*11 original vectors + 1 new. Full tracking in VX sheet.*

### Layer 1: Domestic

| Vector | Name | Status | Confidence | Key Metric |
|--------|------|--------|------------|------------|
| **VX-SAM-1.01** | JGB Yield Stress | 🔴 CRITICAL | 98% | 30Y at 3.68-3.91% ATH |
| **VX-SAM-1.02** | BOJ Policy Trap | 🔴 CRITICAL | 96% | Jan 23-24 decision |
| **VX-SAM-1.03** | JGB Market Dysfunction | 🔴 CRITICAL | 97% | 20Y auction FAILED |
| **VX-SAM-1.04** | Political/Fiscal Dominance | 🔴 CRITICAL | 95% | Takaichi spending spiral |
| **VX-SAM-1.05** | **Fiscal Doom Loop** | 🔴 CRITICAL (NEW) | 92% | Bond vigilante attack active |

### Layer 2: Cross-Border

| Vector | Name | Status | Confidence | Key Metric |
|--------|------|--------|------------|------------|
| **VX-SAM-2.01** | Repatriation Pressure | 🔴 CRITICAL | 92% | GPIF trigger, ESR cliff |
| **VX-SAM-2.02** | Domestic Buyer Collapse | 🔴 CRITICAL | 95% | Nochu losses, no JGB bid |
| **VX-SAM-2.03** | Corporate Margin Stress | 🟡 ACTIVE | 82% | SoftBank monitoring |

### Layer 3: Global

| Vector | Name | Status | Confidence | Key Metric |
|--------|------|--------|------------|------------|
| **VX-SAM-3.01** | USD/JPY Carry Unwind | 🔴 CRITICAL | 94% | 157.99, SPX +0.7 correlation |
| **VX-SAM-3.02** | FX Intervention Constraint | 🟡 ACTIVE | 91% | ~$130B reserves |
| **VX-SAM-3.03** | Geopolitical/China Impact | 🔴 CRITICAL | 85% | Taiwan baseline |
| **VX-SAM-3.04** | CLO Nuclear + Liquidity | 🟠 ELEVATED | 88% ↓ | CLO 125bps; Norinchukin stabilized; RRP depleted |

---

## 7. CURRENT WATCHLIST (Jan 23, 2026)

### 🔴 RED STATUS (Immediate Action)

| Entity | Value | Note |
|--------|-------|------|
| JGB 40Y | 4.24% | RECORD HIGH — First time >4% |
| **Feb 5 30Y Auction** | PENDING | **KEY PRE-ELECTION SIGNAL** — 3 days before vote |
| **Feb 19 20Y Auction** | PENDING | First 20Y since Jan 20 FAILURE |
| RRP Balance | $2.5B | DEPLETED — Floor breached |
| Life Insurer Losses | ~$60B | Unrealized losses on domestic bond portfolios |

### 🟠 ORANGE STATUS (24-Hour Watch)

| Entity | Value | Threshold | Distance |
|--------|-------|-----------|----------|
| JGB 30Y | 3.67% | 4.00% | 33bps (off 3.91 peak) |
| JGB 20Y | 3.48% | 3.70% | 22bps |
| **Feb 8 Election** | PENDING | LDP seat count | **16 days** |
| USD/JPY | 158.55 | 160 | 1.45 handles |
| LDP Seat Projection | 233-260 | <233 = crisis | Narrow majority expected |

### 🟡 YELLOW STATUS (Daily Monitor)

| Entity | Value | Threshold | Distance |
|--------|-------|-----------|----------|
| JGB 10Y | 2.26% | 2.50% | 24bps (improved) |
| Feb 3 10Y Auction | PENDING | BTC, tail | Pre-election test |
| FTD | $42.4B | $50B | $7.6B (85%) |
| CCY Basis | -45bps | -60bps | 15bps (75%) |
| CLO AAA | 125bps | 150bps | 25bps |

### 🟢 GREEN STATUS (Periodic Check)

| Entity | Value | Note |
|--------|-------|------|
| SOFR | 3.67% | On target |
| FHLB | Normal | No delivery stress |
| **Norinchukin** | Stabilizing | Back to profit; CLO nuclear probability ↓ to 8% |

### ⚪ Counter-Signals

| Signal | Meaning | Implication |
|--------|---------|-------------|
| JGB yields off peak post-BOJ | Market partially stabilized | Pause, not resolution |
| BOJ held (as expected) | No surprise hawkish shock | Near-term stability |
| SMFG preparing to buy JGBs | Mega-bank bid forming | Potential demand return |
| Japan Post Bank BUYING JGBs | Domestic absorption capacity | Partial soft landing signal |
| **Norinchukin restructured** | Past acute crisis | CLO blow-up less likely near-term |
| **LDP approval 29.7%** | Takaichi ≠ LDP | Narrow win may constrain fiscal expansion |

**RED Framework:** Full counter-thesis tracking in `C:/Projects/SAM/RED/`
- `SAM_COUNTER_THESIS.md` — Counter-signal categories and competing hypotheses
- `COUNTER_EVIDENCE_LOG.md` — Running log of evidence challenging primary thesis
- `competing_hypotheses/` — Detailed alternative scenario analysis

---

## 8. CRITICAL TIMELINE

### Past Events (Reference)

| Date | Event | Impact |
|------|-------|--------|
| 2025-11-30 | Ueda Hawkish Signal | OIS repriced to 76%+ hike |
| 2025-12-18/19 | BOJ Decision (Hike to 0.75%) | 30-year high in rates |
| **2026-01-17** | Takaichi Campaign Launch | Fiscal spending promises begin |
| **2026-01-18-19** | Opposition Spending Race | Competing tax cut/spending promises |
| **2026-01-19** | "Sanaeconomics" Unveiled | ¥21.3T stimulus, 0% food tax pledge |
| **2026-01-20** | 20Y JGB Auction FAILED | Worst demand since 1987 |
| **2026-01-20** | 30Y/40Y ATH | 3.91% / 4.17% — records broken |
| **2026-01-23** | Lower House Dissolution | Parliament dissolved for Feb 8 election |
| **2026-01-23-24** | BOJ Meeting | **HELD 0.75% (8-1)**; Takata dissented for 1%; raised GDP/inflation forecasts |

### Upcoming Critical (Priority Order)

| Date | Event | Urgency | Why It Matters |
|------|-------|---------|----------------|
| **Jan 24-27** | Post-BOJ Market Reaction | 🟠 ELEVATED | Test if stabilization holds |
| **Feb 3** | 10Y JGB Auction | 🟠 ELEVATED | Pre-election demand test |
| **Feb 5** | **30Y JGB Auction** | 🔴 CRITICAL | **KEY PRE-ELECTION SIGNAL** — 3 days before vote |
| **Feb 8** | **Snap Election** | 🔴 CRITICAL | LDP seat count determines fiscal mandate |
| **Feb 19** | **20Y JGB Auction** | 🔴 CRITICAL | First 20Y since Jan 20 FAILURE — tests if pattern |
| **Post-Feb 8** | Takaichi Policy Speech | 🟠 ELEVATED | Fiscal moderation or doubling down |
| **Mar-Apr 2026** | BOJ April Meeting | 🟠 ELEVATED | Next hike window if election resolves |
| **2026-06** | ESR Full Implementation | Structural | $120B/yr void permanent |

### Election Seat Math (CRITICAL CONTEXT)

| Coalition | Current Seats | Majority = 233 |
|-----------|---------------|----------------|
| LDP + JIP | 233 | 1-seat majority |
| Centrist Reform Alliance | 172 | CDP + Komeito |

**The Takaichi-LDP Gap:**
- Takaichi personal approval: 62-78%
- LDP party approval: 29.7%
- Internal LDP projection: "260 too optimistic, expect 233 at minimum"
- Nippon TV model: LDP retains only 60/132 single-member districts

**Interpretation Matrix:**
| LDP Seats | Outcome | Fiscal Implication |
|-----------|---------|-------------------|
| <233 | Coalition collapse | Crisis — political vacuum |
| 233-250 | Narrow win | **Constrains** fiscal expansion mandate |
| 260+ | Strong win | **Confirms** D2 fiscal expansion pathway |

### Monitoring Schedule

**HOURLY (During Crisis Window Jan 20-27):**
- JGB 10Y/20Y/30Y/40Y yields
- USD/JPY spot
- JGB futures
- Any BOJ/MOF statements

**DAILY:**
- CLO AAA spreads
- CCY Basis (3M USD/JPY)
- FTD levels
- Political developments

**WEEKLY:**
- Treasury auction results
- CFTC positioning
- Norinchukin announcements
- FHLB advance rate

---

## 9. GLOSSARY

### Acronyms

| Acronym | Definition |
|---------|------------|
| BDC | Business Development Company |
| BOJ | Bank of Japan |
| BTC | Bid-to-Cover (auction metric) |
| CCY | Currency |
| CLO | Collateralized Loan Obligation |
| ESR | Economic Value-Based Solvency Regulation |
| FHLB | Federal Home Loan Banks |
| FTD | Fails-to-Deliver |
| GPIF | Government Pension Investment Fund |
| IORB | Interest on Reserve Balances |
| JA | Japan Agricultural Cooperatives |
| JGB | Japanese Government Bond |
| MOF | Ministry of Finance (Japan) |
| OIS | Overnight Index Swap |
| RRP | Reverse Repo (Fed facility) |
| SOFR | Secured Overnight Financing Rate |
| UST | US Treasury |
| VaR | Value at Risk |
| YCC | Yield Curve Control |

### Key Concepts

**Impossible Trilemma:** Japan's three-way policy collision: Defend Yen (requires hikes), Support JGB Market (requires low rates), Fund Fiscal Stimulus (requires market absorption). All three are active; all escape valves sealed.

**Negative Carry Trap:** When hedging costs exceed asset yields. Japanese institutions holding legacy USTs at 2% yield face 5%+ hedging costs = daily capital bleed.

**Bond Vigilante Attack:** When bond market refuses to fund government at any reasonable yield, forcing fiscal/monetary capitulation. Comparisons to 2022 UK Gilt Crisis (Liz Truss).

**Fiscal Doom Loop:** Self-reinforcing spiral where higher yields → higher debt servicing → worse fiscal → higher yields. Japan at 240% debt-to-GDP makes this particularly dangerous.

**Great Rotation:** ¥10T ($65B) flow from Foreign Bonds → Domestic Assets driven by yield differential and ESR pressure. Removes structural bid for USTs.

**CLO Nuclear:** Scenario where Norinchukin (5-7% of global AAA CLO market) is forced to liquidate, causing >150bps spread widening and US credit contagion.

**J-SOLV (Japan Solvency):** Term for Japanese life insurer balance sheet dynamics under ESR regulation. The "Put" they historically provided to UST market is now REMOVED.

---

## 10. INVALIDATION FRAMEWORK

### Overall Thesis Invalidation

| Condition | Confidence Impact |
|-----------|-------------------|
| BOJ explicitly abandons hike AND announces QE expansion | Pattern -25% |
| 30Y JGB yields fall below 3.00% and hold 10+ days | Pattern -20% |
| Life insurers announce INCREASING UST allocations | Pattern -15% |
| Three consecutive JGB auctions BTC >3.0x, minimal tails | Timing -20% |
| Government announces explicit fiscal retrenchment | Pattern -15% |
| Fed/Treasury emergency facility for foreign UST holders | Magnitude -30% |

### Scenario-Specific Invalidation

**Scenario D (Fiscal Crisis) Invalidated If:**
- JGB yields stabilize below 2.40% (10Y) / 3.50% (30Y) for 2+ weeks
- BOJ January meeting signals aggressive rate path + market believes it
- Takaichi announces fiscal consolidation path post-election

**FLOW-JPN-3.01 (CLO Nuclear) Invalidated If:**
- AAA spreads fall <110bps sustained
- Norinchukin completes restructuring without CLO sales
- BDC sector stable through rate cycle

**FLOW-JPN-1.06 (Fiscal Doom Loop) Invalidated If:**
- Three consecutive successful JGB auctions with strong BTC
- Government bond yields stabilize with clear buyer return
- Explicit fiscal discipline announcement from Takaichi coalition

---

## 11. FOUR-SIGNAL CONFIRMATION PROTOCOL

*Use during BOJ decision window (Jan 23-24) and subsequent 48 hours.*

### Signal Definitions

| Signal | Metric | Threshold | Timing | Meaning |
|--------|--------|-----------|--------|---------|
| **1. JGB Yield Break** | 30Y JGB | >4.00% sustained | Post-BOJ | Bond market rejection |
| **2. FX Forward Curve** | USDJPY 3M forwards | Inversions >200 pips | Within 2 hours | Forced yen buying priced |
| **3. SOFR-IORB Spread** | SOFR vs IORB | Spike 15-25 bps | US market open | Funding stress emerging |
| **4. UST Futures** | 10Y/30Y futures | 20-30bp move, no mean reversion | 24-48 hours | Repatriation flow hitting |

### Interpretation Matrix

| Signals Confirmed | Interpretation | Action |
|-------------------|----------------|--------|
| 0 | BOJ decision absorbed; watch for delayed reaction | Continue monitoring |
| 1 | Isolated stress; increase monitoring frequency | Alert coordinating agents |
| 2 | Transmission beginning | Alert all agents, prepare crisis protocols |
| 3 | CASCADE CONFIRMED | Execute crisis protocols |
| 4 | SYSTEMIC EVENT | Coordinate emergency response with MASTER |

---

## 12. SCENARIO TREE (Detailed)

### Scenario A/A+ (10-15%): Soft Landing via Hawkish BOJ

**Trigger:** BOJ January meeting signals aggressive rate path (April hike + multiple 2026 hikes) AND market believes it

**Pathway:**
- JGB yields stabilize as market prices normalization
- Yen strengthens on rate differential narrowing
- Carry unwind is CONTROLLED (gradual, not panic)
- Fiscal pressure eases as yields don't spiral

**Why Probability Downgraded:** JGB crisis suggests market doesn't trust BOJ/fiscal path. Even if BOJ hikes, fiscal spiral may continue.

### Scenario B (30-35%): Controlled Chaos via Intervention

**Trigger:** USD/JPY breaches 160, MOF intervenes with BOJ coordination

**Pathway:**
- Intervention temporarily stabilizes yen
- GPIF mechanical rebalancing triggers ($60-100B UST selling)
- UST yields rise, credit spreads widen
- Fed may need to respond
- BUT: Controlled, not panic

**Why Probability Downgraded:** JGB crisis now dominates. Even successful FX intervention doesn't solve bond market dysfunction.

### Scenario C (25-30%): Acute Carry Unwind Panic

**Trigger:** Intervention fails OR JGB yields break 4.00% 30Y sustained

**Pathway:**
- Carry positions liquidate rapidly
- USD/JPY correlation with SPX causes equity selloff
- Risk parity deleverages both bonds and stocks
- CLO contagion via Norinchukin
- Credit crunch in US

**Why Probability Upgraded:** JGB crisis accelerates FX deterioration. Bond market dysfunction increases probability of all bad outcomes.

### Scenario D1 (8-10%): Fiscal Crisis → Austerity Path

**Trigger:** JGB yields sustain elevated (10Y >2.50%, 30Y >4.00%) for 2+ weeks

**Pathway:**
- Bond market refuses yields at any level
- Japan forced to abandon Takaichi spending plans
- Implement fiscal consolidation (tax increases, spending cuts)
- Japan recession, deflationary shock
- Yen strengthens (fiscal credibility restored)
- Global deflation exports

**Outcome:** -15-25% equity decline but contained; recoverable 12-18 months

### Scenario D2 (7-10%): Fiscal Crisis → Monetary Dominance

**Trigger:** Same as D1, but political choice differs

**Pathway:**
- Bond market refuses yields
- Political pressure on BOJ: "You must stop the bleeding"
- BOJ restarts QE or returns to YCC
- BOJ becomes de facto fiscal agent
- Yen collapse (monetary dominance signal)
- Imported inflation surge
- EM currency crises

**Outcome:** -20-35% equity decline, EM contagion, 2-3 year dysfunction

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-16 | Initial skeleton based on SAM-V session |
| 1.1 | 2026-01-20 | EMERGENCY UPDATE: JGB crisis integration, Scenario D added, thresholds updated, FLOW-JPN-1.06 added, methodology alignment |
| 1.2 | 2026-01-23 | BOJ Jan 23-24 decision update: held 0.75% (8-1); current yield levels updated; Feb 8 election now primary catalyst; Takaichi fiscal platform detailed (¥122.3T budget, 0% food tax); scenario probabilities adjusted post-stabilization |
| 1.3 | 2026-01-23 | Research update: Norinchukin status (past acute crisis, back to profit, CLO nuclear ↓8%); Feb auction calendar added (Feb 5 30Y critical, Feb 19 20Y critical); Election seat math added (LDP 29.7% approval vs Takaichi 70%+, narrow win constrains mandate); VX-SAM-3.04 downgraded to ELEVATED |

---

## USAGE INSTRUCTIONS

1. **LOAD AT SESSION START**
   - Upload this skeleton + methodology skeleton
   - LLM now has domain vocabulary and architecture

2. **LOAD HANDOFF + CURRENT DATA**
   - Upload latest SAM Handoff (SAM-IX, SAM-X, etc.)
   - Upload JPN_LOGS if needed for evidence
   - LLM maps current data to skeleton structure

3. **CRISIS MONITORING (Current State)**
   - Focus on Section 4 (Thresholds) and Section 7 (Watchlist)
   - Check four-signal protocol (Section 11)
   - Monitor JGB yields HOURLY through Jan 27

4. **UPDATE SKELETON (RARELY)**
   - Only update when ARCHITECTURE changes
   - Current VALUES belong in handoffs and live data

5. **COORDINATE WITH OTHER AGENTS**
   - Reference LIQUID for US funding details
   - Reference REGINALD for regional bank exposure
   - Alert MASTER for cross-domain escalation

---

*End of SAM Domain Skeleton v1.1*
