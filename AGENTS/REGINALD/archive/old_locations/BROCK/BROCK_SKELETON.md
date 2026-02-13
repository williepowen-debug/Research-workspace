# BROCK — BDC Research & Observation of Credit Kinetics

*Last updated: 2026-02-02*

**Parent:** REGINALD
**Domain:** BDCs, private credit, hidden bank credit lines, PIK trends

---

## 1. THESIS

BDCs have **$142B in unfunded credit commitments** from regional banks. This is the hidden leverage REGINALD tracks.

**The problem:**
- BDC portfolios are floating-rate leveraged loans
- When credit stress hits, borrowers can't pay cash interest → PIK spikes
- BDC NAVs collapse → BDCs draw bank credit lines for liquidity
- Banks face cash drain exactly when they need it most
- Procyclical amplification feeds back to deposit flight

**Current state:**
- Sector NAV: -16% avg discount (was +6% premium Feb 2025)
- Crisis names: PSEC -57%, FSK -34%
- PIK warning: Golub 173% YoY spike
- Bank exposure: CFG $10-11B, VLY/ZION also exposed

**Status:** MONITORING — NAV discounts elevated, PIK rising, waiting for CLO trigger.

---

## 2. CURRENT STATUS

**Source of truth:** `workbook/VX.tsv`

| Status | Count |
|--------|-------|
| GREEN | TBD |
| ORANGE | TBD |
| YELLOW | TBD |

**Key signals:**
- Sector NAV discount (VX-BROCK-1.01)
- PSEC/FSK in crisis territory (VX-BROCK-2.02, 2.03)
- Golub PIK spike (VX-BROCK-2.06)

**What would escalate this:**
- CLO AAA >165bps → credit line draws begin
- 2+ major BDC dividend cuts → market panic
- Any BDC NAV >-40% → contagion risk

---

## 3. TRANSMISSION PATHS

**Full registry:** `workbook/FLOW.tsv`

### FLOW-BROCK-1.01: PIK Deterioration Loop
```
Speed: QUARTERS | Status: ACTIVE | Trigger: PIK >15% income

Floating-rate stress → Borrowers can't pay cash → PIK (IOU) booked as income
→ NII inflated on paper → Dividend appears "covered" → Cash runs dry
→ Forced dividend cut → Market reprices entire sector → Panic

Key insight: "Covered" dividend is fiction when PIK is rising.
Monitor: 10-Q PIK disclosures, cash NII vs declared dividend
```

### FLOW-BROCK-2.01: Credit Line Draw Cascade
```
Speed: DAYS | Status: LATENT | Trigger: CLO AAA >165bps

Credit stress → BDC portfolios mark down → NAV craters
→ BDCs draw bank credit lines ($142B unfunded, ~45% = $64B potential)
→ Banks face liquidity drain exactly when they need cash
→ FHLB surge → [transmit to REGINALD/LIQUID]

Key insight: Hidden second-order effect. BDC stress = bank stress.
Monitor: Credit facility utilization in 10-Q, bank earnings commentary
```

### FLOW-BROCK-3.01: NAV Discount Contagion
```
Speed: WEEKS | Status: LATENT | Trigger: Any major BDC -40%+

Single BDC blows up → Market questions entire sector
→ Retail/institutional redemptions → Non-traded BDCs gate
→ Forced asset sales → Price discovery reveals hidden losses
→ Peer BDCs marked down → Bank credit lines at risk

Key insight: PSEC at -57% is already in crisis. One more name tips the sector.
Monitor: Daily NAV discounts, redemption queue disclosures
```

### FLOW-BROCK-4.01: Dividend Cut Cascade
```
Speed: DAYS | Status: LATENT | Trigger: 2+ major BDCs cut dividend

First cut blamed on idiosyncratic factors → Second cut reveals pattern
→ Income investors flee → Stock prices collapse → NAV discounts widen
→ Credit line covenants tested → Bank exposure crystallizes

Key insight: BDC investors are yield-seekers. Dividend cut = existential event.
Monitor: Dividend announcements, earnings calls for "special" vs "regular" language
```

---

## 4. WATCHLIST

### Crisis Tier (NAV discount >30%)
| BDC | Ticker | NAV Discount | Key Risk |
|-----|--------|--------------|----------|
| Prospect Capital | PSEC | -57% | Largest discount, dividend sustainability |
| FS KKR Capital | FSK | -34% | Size ($15B), bank line exposure |

### Elevated Tier (Watch closely)
| BDC | Ticker | Why |
|-----|--------|-----|
| Golub Capital | GBDC | PIK spike 173% YoY, dividend cut Sept 2025 |
| Blackstone Credit | BCRED | Largest non-traded, gating risk |
| Blackstone Secured | BXSL | Public Blackstone vehicle |

### Benchmark Tier
| BDC | Ticker | Why |
|-----|--------|-----|
| Ares Capital | ARCC | Largest BDC, sector bellwether |
| BlackRock TCP | TCPC | Mid-tier reference |

---

## 5. COORDINATION

| Agent | Direction | Exchange |
|-------|-----------|----------|
| **REGINALD** | ↑ Parent | Bank credit line exposure (CFG, VLY, ZION) |
| **SAM** | ← Input | CLO AAA spreads (transmission trigger) |
| **LIQUID** | ← Input | SOFR levels (floating rate pressure) |

**Signals to REGINALD (send when):**
- Any BDC NAV discount >-40%
- Sector PIK >20%
- 2+ dividend cuts announced
- Credit line utilization >30%

**Signals from SAM (watch for):**
- CLO AAA >150bps (alert)
- CLO AAA >165bps (BDC stress begins)

---

## 6. DATA SOURCES

| Source | Data | Cadence |
|--------|------|---------|
| CEF Connect | NAV discounts | Daily |
| BDC 10-Q/10-K | PIK %, credit facilities, portfolio | Quarterly |
| Press releases | Dividend announcements | As announced |
| Bank 10-Q | Credit commitments to BDCs | Quarterly |
| Earnings calls | Management commentary | Quarterly |

---

*BROCK Skeleton v1.0 — BDC/Private Credit Sub-Agent*
