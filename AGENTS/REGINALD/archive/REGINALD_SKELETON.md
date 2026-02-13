# REGINALD — Regional Banks & Hidden Leverage

*Last updated: 2026-02-02*

## 1. THESIS

US regional banks face concentrated exposure to CRE and shadow banking that surface metrics don't capture.

**Core risks:**
- Regional banks hold 80%+ of CRE loans, many underwater
- Hidden credit lines to BDCs ($142B unfunded) create liquidity risk
- Post-SVB deposit flight risk persists
- Federal employment cuts create new geographic credit channel

**Key transmission:** US credit cycle deteriorates → Japan CLO trust NAVs collapse → Japan bid disappears → CLO spreads gap → Regional bank marks decline → Deposit flight.

Note: Japan is BUYING CLOs (anchoring spreads), not selling. Trigger is US credit cycle, not Japan policy.

**Status:** MONITORING — Surface GREEN, hidden indicators ORANGE.

---

## 2. CURRENT STATUS

**Source of truth:** `workbook/VX.tsv`

| Status | Count |
|--------|-------|
| GREEN | 14 |
| ORANGE | 10 |
| YELLOW | 4 |

**Key ORANGE signals (action items):**
- BDC NAV -16% (VX-REG-2.03) — market pricing stress not yet in bank marks
- DC UCFE claims +543% YoY (VX-REG-11.03) — federal employment leading indicator
- EGBN deposits -4% QoQ (VX-REG-11.04) — flight from weakest DC bank
- CRE extend-and-pretend (VX-REG-9.01-9.04) — $7.7B+ modified, exhaustion signals

**What would change this:**
- Employment break (claims spike, NFP negative) → ORANGE signals convert to RED
- CLO spreads >150bps → Japan transmission activates
- Regional bank earnings miss + deposit outflows → crisis protocols

---

## 3. TRANSMISSION PATHS

How stress propagates. These are the mental models for reasoning.

**Full registry:** `workbook/FLOW.tsv` (12 paths). Below are the 5 most critical.

### FLOW-REG-1.01: CLO Transmission
```
Speed: DAYS | Status: LATENT | Trigger: CLO AAA >150bps

US credit deteriorates → Japan trust NAVs collapse → Forced redemptions
→ Japan bid disappears → CLO spreads gap wider (currently 115bps)
→ Regional bank marks decline → Capital pressure → Deposit flight risk

Key insight: Japan is buyer, not seller. They amplify US stress, don't initiate it.
Monitor: PSQA ETF (CLO AAA proxy), Norinchukin commentary
```

### FLOW-REG-2.01: CRE Doom Loop
```
Speed: QUARTERS | Status: ACTIVE (slow burn) | Trigger: CRE DQ >5%

Office vacancy (20.5%) → Property values decline → LTV ratios breach
→ Loan modifications fail (>50% re-default) → NPLs spike → Provisions rise
→ Earnings collapse → Stock decline → Deposit flight

Key insight: Banks masking via modifications. $7.7B+ modified. Exhaustion coming.
Monitor: FRED CRE delinquency, bank 10-Q modification disclosures
```

### FLOW-REG-11.01: BDC Credit Line Cascade
```
Speed: DAYS (when triggered) | Status: LATENT | Trigger: CLO AAA >165bps

Credit stress event → BDC portfolios mark down → BDCs draw bank lines
→ $142B unfunded / ~45% draw = $64B liquidity drain
→ Banks need cash exactly when BDCs are pulling it
→ FHLB advance surge → [transmit to LIQUID]

Key insight: Hidden second-order effect. BDC NAV at -16% is early warning.
Monitor: BDC NAV discounts (FSK, PSEC in crisis territory)
```

### FLOW-REG-10.01: Deposit Flight
```
Speed: HOURS | Status: LATENT | Trigger: Bank stock -20% in day

Bank stress signal (earnings miss, loss announcement, stock crash)
→ Depositor panic (>$250K at risk) → Digital bank run
→ Liquidity crisis → FHLB advance surge → [transmit to LIQUID]

Key insight: Social media accelerates runs. SVB went in 48 hours.
Monitor: Regional bank stocks, Twitter/Reddit sentiment on stress days
```

### FLOW-REG-12.01: Federal Employment Channel (NEW)
```
Speed: QUARTERS | Status: ACTIVE | Trigger: DC unemployment >4.5%

DOGE federal cuts (277K+ separations) → Geographic concentration
→ DC 24.6%, Colorado Springs 16.4%, Virginia Beach 16.1% federal share
→ Consumer/mortgage stress in federal metros → Bank credit losses

Key insight: DC UCFE claims +543% (leading), unemployment 3.5% (lagging). Gap will close.
Monitor: UCFE claims, DC/MD/VA unemployment, AUB/EGBN credit quality
```

---

## 4. COORDINATION

| Agent | Domain | Exchange |
|-------|--------|----------|
| **SAM** | Japan / CLO | VX-REG ↔ CLO spreads, Norinchukin flows |
| **LIQUID** | Treasury / Funding | VX-REG ↔ FHLB stress, SOFR |
| **LABOR** | Employment | VX-REG ↔ Federal employment, claims data |
| **CARL** | Consumer / Household | VX-REG ↔ Employment break signals |

**Signals IN (watch for):**
- SAM: CLO AAA >150bps, Norinchukin stress
- LIQUID: SOFR spike, FHLB advance surge
- LABOR: Claims spike, NFP negative, federal layoff acceleration

**Signals OUT (send when):**
- Regional bank stock -15%+ → alert LIQUID (funding stress coming)
- BDC NAV <-20% → alert SAM (CLO stress transmission)
- DC bank credit deterioration → alert LABOR (confirm federal channel)

---

## 5. WATCHLIST CONTEXT

Bank-specific narratives that don't fit in VX.tsv.

### AUB (Atlantic Union Bank) — YELLOW
- **Profile:** $38B assets, 175 branches VA/MD/NC/DC
- **Key event:** Acquired Sandy Spring Bank (April 2025, $14.4B MD regional)
- **Defensive action:** Sold $2B CRE to Blackstone (June 2025)
- **Why YELLOW:** Federal metro exposure but proactive management
- **Watch:** Q1/Q2 2026 credit quality, mortgage DQ in DC/MD/VA

### EGBN (Eagle Bancorp) — ORANGE
- **Profile:** $10.5B assets, pure DC/NoVA/MD play
- **Red flag:** Dedicated government contractor lending division
- **Already in crisis:** Q3 2025 -$67.5M loss, CEO retiring, dividend cut to $0.01
- **Flight signal:** Q4 deposits -4% QoQ despite small profit
- **Why ORANGE:** Weak balance sheet + federal exposure = compounding risk
- **Watch:** Deposit trends, government contractor commentary in earnings

### Blackstone Signal
- Bought $22B in bank loan portfolios in 24 months (Signature $17B, AUB $2B, others)
- Buying "performing but underwater" at ~7% discount
- **Interpretation:** Smart money positioning for continued regional bank stress

---

## 6. SUB-AGENTS

### CREED (Commercial Real Estate Exposure & Distress)
- **Status:** ACTIVE
- **Purpose:** Deep dive on CRE-specific vectors (maturity wall, modifications, special servicing)
- **Location:** `CREED/` folder with own skeleton, workbook, handoffs
- **Last activity:** Session 003 (2026-01-30)
- **Key research:** 12 completed items including maturity wall ($936B), FL condo crisis, special servicing analysis

### BROCK (BDC Research & Observation of Credit Kinetics)
- **Status:** ACTIVE
- **Purpose:** Deep dive on BDC/private credit (hidden leverage, PIK trends, bank credit lines)
- **Location:** `BROCK/` folder with own skeleton, workbook, handoffs
- **Last activity:** Session 000 (2026-02-02) — Initialization
- **Key vectors:** PSEC -57% (RED), FSK -34% (ORANGE), Golub PIK +173%
- **Thesis:** $142B unfunded bank commitments = procyclical amplifier

Load CREED for CRE analysis. Load BROCK for BDC/private credit analysis.

---

*REGINALD Skeleton v2.0 — 150 lines of signal*
