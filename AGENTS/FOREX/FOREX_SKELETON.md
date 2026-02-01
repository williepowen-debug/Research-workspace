# FOREX DOMAIN SKELETON v1.0

# Purpose: Structural scaffold for LLM domain orientation
# Domain:  Currency Markets, DXY, Major Pairs, Carry Trades, EM FX, Intervention Risk
# Agent:   FOREX (Foreign Exchange Monitoring Agent)
#
# Version: 1.0
# Created: 2026-01-26
# Updated: 2026-01-26
# Author:  PROME Network
#
# Usage:
#   - Load this file at the start of any FOREX session
#   - Provides entity types, relationship vocabulary, core architecture
#   - Named transmission paths define known cascade routes
#   - Thresholds define tripwires for escalation

---

## 0. QUICK START

*Load this section for any session. Provides minimum viable orientation.*

### About This Agent

FOREX monitors global currency markets with focus on:
- Dollar regime (DXY strength/weakness)
- Yen dynamics (carry trade, BOJ policy, intervention)
- EM currency stress and contagion
- Cross-border transmission to other PROME agents

**Coordination:** Primary linkages to SAM (yen/BOJ), LIQUID (dollar funding), BARON (trade policy)

### Current Thesis

**PRIMARY THESIS: Peak Dollar Transition**

The US dollar has entered a structural weakening phase after reaching "peak dollar" in early 2025. Key dynamics:

1. **DXY Retreat** → Dollar Index fell ~9% in 2025, largest drop since 2017
2. **Intervention Regime Change** → US-Japan coordination signaled; 160 ceiling now hard
3. **Carry Trade Recalibration** → Yen carry trade unwinding gradually (~$261B, not trillions)
4. **EM Resilience** → EM FX index +7.5% YoY; JP Morgan signals overbought

**Confidence:** Pattern 75% | Timing 65% | Magnitude 70%
**Status:** INITIALIZING — First session pending

**Invalidation Criteria:**
- DXY rallies above 105 and holds for 2+ weeks
- Fed signals return to aggressive hiking cycle
- EM currency crisis spreads to 3+ major economies
- Carry trade unwind accelerates to panic (>$50B/week outflows)

### Scenario Framework

| Scenario | Probability | Description | Primary Vector |
|----------|-------------|-------------|----------------|
| **A** | 35% | Orderly dollar decline | VX-FOREX-001 (DXY) |
| **B** | 30% | Coordinated intervention stabilizes yen | VX-FOREX-002 (USD/JPY) |
| **C** | 20% | Carry unwind panic | VX-FOREX-007 (Carry Trade) |
| **D** | 15% | EM contagion spreads | VX-FOREX-005 (EM FX) |

### Coordinating Agents

| Agent | Domain | Key Linkages |
|-------|--------|--------------|
| **SAM** | Japan sovereign/BOJ | USD/JPY intervention; BOJ policy; JGB-FX correlation |
| **LIQUID** | Treasury/funding | Dollar funding stress; cross-currency basis |
| **BARON** | Political-financial | Tariff policy; trade tensions; currency manipulation |
| **CARL** | Consumer stress | Import price inflation via dollar moves |
| **MARCO** | Regional stress | EM stress affecting migration corridors |

---

## 1. ENTITY TYPES

*The vocabulary of the domain. Every node belongs to exactly one entity type.*

### Central Banks (FX Policy)

| Bank | Currency | Key Policy Tools | Current Stance |
|------|----------|------------------|----------------|
| **Federal Reserve** | USD | Rates, balance sheet | Cutting cycle |
| **BOJ** | JPY | Rates, intervention coordination | Hiking (0.75%) |
| **PBOC** | CNY | Band management, fixing | Managed depreciation |
| **ECB** | EUR | Rates | Cutting cycle |
| **SNB** | CHF | Intervention, rates | Alternative funding currency |

### Currency Pairs (Major)

| Pair | Description | Current Level | Key Dynamics |
|------|-------------|---------------|--------------|
| **DXY** | Dollar Index (basket) | ~97 | 9% decline in 2025; "peak dollar" passed |
| **USD/JPY** | Dollar-Yen | ~154 | Intervention risk HIGH; 160 hard ceiling |
| **EUR/USD** | Euro-Dollar | ~1.17-1.18 | ECB-Fed divergence narrowing |
| **USD/CNY** | Dollar-Yuan | ~7.20-7.30 | PBOC managing; tariff pressure |
| **GBP/USD** | Cable | ~1.28 | BOE policy dependent |

### Currency Pairs (EM)

| Region | Key Currencies | Stress Indicators |
|--------|----------------|-------------------|
| **LatAm** | BRL, MXN, ARS | Commodity linkage; political risk |
| **Asia** | INR, IDR, KRW, TWD | China spillover; tech cycle |
| **EMEA** | TRY, ZAR, PLN | Geopolitical; commodity |

### Market Structures

| Structure | Description | Risk Transmission |
|-----------|-------------|-------------------|
| **Carry Trade** | Borrow low-yield, invest high-yield | Unwind = risk-off cascade |
| **FX Swaps** | Cross-currency basis market | Funding stress indicator |
| **Options Market** | CVIX, risk reversals | Volatility regime |
| **Central Bank Reserves** | FX intervention capacity | Sustainability of defense |

---

## 2. RELATIONSHIP TYPES

*How entities connect.*

### Policy Relationships
- `intervenes`: CB takes market action (MOF/BOJ intervenes in USD/JPY)
- `coordinates`: Joint action between CBs (US-Japan coordinated intervention)
- `manages`: CB controls currency band (PBOC manages CNY fixing)

### Flow Relationships
- `funds`: Currency used as funding leg (JPY funds carry trade)
- `hedges`: FX exposure managed (Japanese insurers hedge USD)
- `repatriates`: Capital returns home (Japan repatriation flow)

### Stress Relationships
- `transmits`: Stress propagates (EM weakness transmits to risk assets)
- `correlates`: Statistical co-movement (USD/JPY +0.7 with SPX)
- `amplifies`: Second-order worsening (Carry unwind amplifies equity selloff)

---

## 3. TRANSMISSION PATHS (Named Cascade Routes)

### FLOW-FOREX-01: Carry Trade Unwind Cascade

```
Speed: HOURS to DAYS
Status: LATENT — Armed but not triggered
Layer: Global

Pathway:
  BOJ hawkish surprise OR coordinated intervention
    → Yen strengthens rapidly (>3% in session)
    → Carry positions face margin calls
    → Forced liquidation of risk assets (funded by yen)
    → USD/JPY-SPX correlation (+0.7) transmits to equities
    → VIX spikes → Risk parity deleverages
    → Credit spreads widen → LIQUID funding stress

Trigger: USD/JPY <150 rapid move OR BOJ surprise hike
Current Position: USD/JPY at ~154; intervention risk elevated
Historical Precedent: August 2024 unwind
```

### FLOW-FOREX-02: Dollar Funding Stress

```
Speed: HOURS
Status: LATENT
Layer: Global

Pathway:
  Offshore dollar shortage emerges
    → Cross-currency basis widens (>50bps)
    → EM CBs draw reserves to provide USD
    → Reserve depletion accelerates
    → Currency defense fails
    → Contagion to other EM

Trigger: Cross-currency basis >50bps; swap line activation
Current Position: Basis at ~45bps; normal
Historical Precedent: March 2020, September 2019
```

### FLOW-FOREX-03: EM Contagion Cascade

```
Speed: DAYS to WEEKS
Status: LATENT
Layer: EM

Pathway:
  Idiosyncratic EM crisis (single country)
    → Capital flight from country
    → Investors reduce EM exposure broadly
    → EM FX basket weakens
    → CB intervention depletes reserves
    → Multiple countries hit simultaneously
    → Risk-off reaches DM markets

Trigger: Major EM CB exhausts reserves; >5% weekly EM basket decline
Current Position: EM FX +7.5% YoY; overbought per JP Morgan
Historical Precedent: 2015 China deval, 1997 Asian crisis
```

### FLOW-FOREX-04: Competitive Devaluation

```
Speed: WEEKS to MONTHS
Status: LATENT
Layer: Global

Pathway:
  Major economy devalues (China most likely)
    → Trading partners face competitiveness loss
    → Retaliatory devaluations OR tariffs
    → Trade tensions escalate
    → Supply chain disruption
    → Global growth impact

Trigger: CNY fixing >7.50; unannounced band widening
Current Position: CNY at ~7.25; PBOC managing orderly
Historical Precedent: 2015 China devaluation
Coordination: BARON for tariff/trade policy
```

---

## 4. THRESHOLDS (Consolidated Tripwires)

*All escalation thresholds. Updated Jan 26, 2026.*

**Color Coding:** 🟢 GREEN | 🟡 YELLOW | 🟠 ORANGE | 🔴 RED

### DOLLAR INDEX (DXY)

| Metric | Current | Yellow | Orange | Red | Status |
|--------|---------|--------|--------|-----|--------|
| **DXY Level** | ~97 | <95 | <92 | <90 | 🟢 GREEN (off highs) |
| **DXY Weekly Change** | -0.5% | -2% | -3% | -5% | 🟢 GREEN |

**Context:** DXY down 9% in 2025. "Peak dollar" narrative dominant. Further weakness expected but orderly.

### USD/JPY — PRIMARY VECTOR

| Metric | Current | Yellow | Orange | Red | Status |
|--------|---------|--------|--------|-----|--------|
| **USD/JPY Level** | ~154 | >157 | >158 | >160 | 🟡 YELLOW |
| **USD/JPY Rapid Move** | Stable | >2%/day | >3%/day | >5%/day | 🟢 GREEN |
| **Intervention Risk** | HIGH | Verbal | Physical | Joint US-Japan | 🟠 ORANGE |

**Context:** NY Fed rate checks conducted Jan 24. Takaichi warned of action. 160 now hard ceiling. Joint intervention possible.

### CROSS-CURRENCY BASIS

| Metric | Current | Yellow | Orange | Red | Status |
|--------|---------|--------|--------|-----|--------|
| **USD/JPY 3M Basis** | -45bps | -60bps | -75bps | -100bps | 🟢 GREEN |
| **EUR/USD 3M Basis** | Normal | -30bps | -50bps | -75bps | 🟢 GREEN |

**Context:** Funding markets normal. No stress signals.

### EM FX

| Metric | Current | Yellow | Orange | Red | Status |
|--------|---------|--------|--------|-----|--------|
| **MSCI EM FX Index** | +7.5% YoY | -3% weekly | -5% weekly | -7% weekly | 🟢 GREEN |
| **JP Morgan EM Risk Appetite** | Overbought | Neutral | Oversold | Panic | 🟡 YELLOW (overbought) |

**Context:** EM FX rally extended. JP Morgan signals overbought. Vulnerable to reversal but not in stress.

### VOLATILITY

| Metric | Current | Yellow | Orange | Red | Status |
|--------|---------|--------|--------|-----|--------|
| **CVIX (FX Vol)** | ~10 | >12 | >15 | >20 | 🟢 GREEN |

**Context:** Low vol regime. Carry trades attractive but vulnerable to vol spike.

### CHINA (USD/CNY)

| Metric | Current | Yellow | Orange | Red | Status |
|--------|---------|--------|--------|-----|--------|
| **USD/CNY** | ~7.25 | >7.35 | >7.45 | >7.50 | 🟢 GREEN |
| **PBOC Fixing** | Stable | Weak bias | Band stress | Unannounced move | 🟢 GREEN |

**Context:** PBOC managing orderly. Tariff risk from BARON domain could pressure.

---

## 5. VECTOR REGISTRY

*7 primary vectors for FOREX domain.*

### VX-FOREX-001: Dollar Regime (DXY)

| Field | Value |
|-------|-------|
| **Name** | Dollar Index Trend |
| **Category** | Dollar |
| **Current** | ~97 |
| **Status** | 🟢 GREEN |
| **Confidence** | 80% |
| **Mechanism** | Fed policy, relative growth, safe haven flows |
| **Downstream** | EM stress, commodity prices, import inflation |
| **Coordination** | LIQUID (funding), CARL (import prices) |

### VX-FOREX-002: USD/JPY Dynamics

| Field | Value |
|-------|-------|
| **Name** | Yen Carry Trade / Intervention |
| **Category** | Major Pairs |
| **Current** | ~154 |
| **Status** | 🟡 YELLOW |
| **Confidence** | 85% |
| **Mechanism** | BOJ policy, intervention risk, carry positioning |
| **Downstream** | Risk asset correlation, Japan repatriation |
| **Coordination** | SAM (primary), LIQUID |

### VX-FOREX-003: EUR/USD Dynamics

| Field | Value |
|-------|-------|
| **Name** | Euro-Dollar Rate |
| **Category** | Major Pairs |
| **Current** | ~1.17-1.18 |
| **Status** | 🟢 GREEN |
| **Confidence** | 75% |
| **Mechanism** | ECB-Fed divergence, growth differential |
| **Downstream** | European export competitiveness |

### VX-FOREX-004: USD/CNY Dynamics

| Field | Value |
|-------|-------|
| **Name** | Yuan Management |
| **Category** | Major Pairs |
| **Current** | ~7.25 |
| **Status** | 🟢 GREEN |
| **Confidence** | 70% |
| **Mechanism** | PBOC fixing, capital flows, tariff pressure |
| **Downstream** | EM contagion, trade tensions |
| **Coordination** | BARON (tariffs) |

### VX-FOREX-005: EM FX Basket

| Field | Value |
|-------|-------|
| **Name** | Emerging Market Currencies |
| **Category** | EM |
| **Current** | +7.5% YoY |
| **Status** | 🟡 YELLOW (overbought) |
| **Confidence** | 70% |
| **Mechanism** | Risk appetite, dollar strength, commodity prices |
| **Downstream** | EM credit, migration flows |
| **Coordination** | MARCO (regional), LIQUID |

### VX-FOREX-006: Cross-Currency Basis

| Field | Value |
|-------|-------|
| **Name** | FX Funding Stress |
| **Category** | Funding |
| **Current** | -45bps (USD/JPY) |
| **Status** | 🟢 GREEN |
| **Confidence** | 85% |
| **Mechanism** | Offshore dollar demand, swap line usage |
| **Downstream** | Global funding stress |
| **Coordination** | LIQUID (primary) |

### VX-FOREX-007: Carry Trade Risk

| Field | Value |
|-------|-------|
| **Name** | Yen Carry Trade Unwind |
| **Category** | Positioning |
| **Current** | ~$261B (gradual unwind) |
| **Status** | 🟠 ORANGE |
| **Confidence** | 75% |
| **Mechanism** | Vol spike, intervention, BOJ surprise |
| **Downstream** | Risk asset correlation cascade |
| **Coordination** | SAM, LIQUID |

---

## 6. CURRENT WATCHLIST (Jan 26, 2026)

### 🔴 RED STATUS (Immediate Action)

*None currently*

### 🟠 ORANGE STATUS (24-Hour Watch)

| Entity | Value | Threshold | Note |
|--------|-------|-----------|------|
| **Intervention Risk** | HIGH | Joint action | NY Fed rate checks; Takaichi warning |
| **Carry Trade** | Armed | Unwind trigger | Low vol masks vulnerability |

### 🟡 YELLOW STATUS (Daily Monitor)

| Entity | Value | Threshold | Distance |
|--------|-------|-----------|----------|
| USD/JPY | ~154 | 160 | 6 handles |
| EM FX | Overbought | Reversal | JP Morgan signal |

### 🟢 GREEN STATUS (Weekly Check)

| Entity | Value | Note |
|--------|-------|------|
| DXY | ~97 | Peak dollar passed |
| Cross-currency basis | -45bps | Normal |
| CVIX | ~10 | Low vol |
| USD/CNY | ~7.25 | PBOC managing |

### ⚪ Counter-Signals

| Signal | Meaning |
|--------|---------|
| Dollar weakness orderly | No panic; managed decline |
| Intervention coordination | US supportive of yen strength |
| EM FX resilience | Risk appetite intact |

---

## 7. CRITICAL TIMELINE

### Past Events (Reference)

| Date | Event | Impact |
|------|-------|--------|
| 2025 Full Year | DXY -9.4% | Largest drop since 2017 |
| 2025-08 | Carry unwind episode | USD/JPY dropped to ~140 briefly |
| 2026-01-24 | NY Fed rate checks | Joint intervention signal |
| 2026-01-25 | Takaichi intervention warning | 160 ceiling hardened |

### Upcoming Critical

| Date | Event | Urgency | Why It Matters |
|------|-------|---------|----------------|
| **Feb 8** | Japan snap election | 🔴 CRITICAL | Takaichi mandate; fiscal policy |
| **FOMC** | Fed meeting | 🟠 ELEVATED | Rate path; dollar direction |
| **Ongoing** | US-Japan coordination | 🟠 ELEVATED | Intervention regime change |

---

## 8. DATA SOURCES

### Primary

| Source | Content | Frequency |
|--------|---------|-----------|
| Bloomberg/Reuters | Spot rates, vol | Real-time |
| TradingView | DXY, majors | Real-time |
| CFTC COT | Positioning | Weekly |
| BIS | Cross-border flows | Quarterly |

### Secondary

| Source | Content | Frequency |
|--------|---------|-----------|
| NY Fed | FX intervention data | As announced |
| PBOC | CNY fixing | Daily |
| IMF COFER | Reserve composition | Quarterly |
| JP Morgan | EM risk appetite | Weekly |

---

## 9. GLOSSARY

### Acronyms

| Acronym | Definition |
|---------|------------|
| DXY | Dollar Index |
| CVIX | Currency Volatility Index |
| CCY | Currency |
| EM | Emerging Markets |
| CB | Central Bank |
| COT | Commitment of Traders |
| COFER | Currency Composition of Foreign Exchange Reserves |

### Key Concepts

**Carry Trade:** Borrowing in low-yield currency (JPY, CHF) to invest in higher-yield assets. Profitable in low-vol; vulnerable to unwind in stress.

**Cross-Currency Basis:** Premium/discount for swapping one currency for another. Widening = offshore funding stress.

**Intervention:** Central bank buying/selling currency to influence exchange rate. Can be unilateral or coordinated.

**Rate Checks:** Central bank queries dealers for market rates. Precursor to intervention.

**Competitive Devaluation:** When countries deliberately weaken currency for export advantage, triggering retaliation.

---

## 10. INVALIDATION FRAMEWORK

### Overall Thesis Invalidation

| Condition | Confidence Impact |
|-----------|-------------------|
| DXY rallies >105 sustained | Pattern -25% |
| Fed returns to hiking cycle | Pattern -20% |
| EM crisis spreads to 3+ majors | Scenario shift |
| Carry unwind becomes panic (>$50B/week) | Timing -30% |

### Flow-Specific Invalidation

**FLOW-FOREX-01 (Carry Unwind) Invalidated If:**
- Vol remains suppressed (<10 CVIX) for 3+ months
- BOJ abandons hike path
- US-Japan coordination breaks down

**FLOW-FOREX-03 (EM Contagion) Invalidated If:**
- EM FX holds gains through Fed cutting cycle
- No major EM reserve depletion
- Risk appetite remains strong

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-26 | Initial skeleton created with current data |

---

*FOREX Domain Skeleton v1.0 | Created: 2026-01-26*
