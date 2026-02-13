# RP-ZHAO-4: Hong Kong Dollar Peg (LERS) Analysis

**Source:** Gemini Deep Research (Feb 13, 2026)
**Prompt:** HK peg mechanics, liquidity triggers, geopolitical risk, UST liquidation transmission

---

## Executive Summary

The Hong Kong dollar Linked Exchange Rate System (LERS) is a **fully-backed currency board** operating within a 7.75-7.85 USD band. The system's automatic adjustment mechanism has proven remarkably resilient through 40 years of crises. However, it now faces unprecedented geopolitical tail risk: the potential for US sanctions to cut off USD clearing access. A forced defense of the peg could trigger **hundreds of billions in UST liquidations** — a critical transmission channel from HK stress to global markets.

---

## LERS Mechanics

### The Band
- **Strong-side:** 7.75 (HKD appreciating) → HKMA sells HKD, buys USD → AB expands → HIBOR falls
- **Weak-side:** 7.85 (HKD weakening) → HKMA buys HKD, sells USD → AB contracts → HIBOR rises

### Monetary Base Components
1. **Certificates of Indebtedness (CIs):** Backing for banknotes (HSBC, StanChart, BOC)
2. **Government Currency Notes/Coins**
3. **Aggregate Balance (AB):** Interbank clearing balances — **most sensitive component**
4. **Exchange Fund Bills and Notes (EFBNs):** HKD debt securities, convertible via Discount Window

**Key insight:** The Aggregate Balance is the primary barometer of HK monetary tightness. Its contraction to zero is the **defense** of the peg, not its failure.

---

## Aggregate Balance Historical Phases (2019-2026)

| Phase | Period | AB Range | Driver |
|-------|--------|----------|--------|
| **I** | 2019 | HK$76.4B → HK$54.3B | Social unrest, rate gap, 8 weak-side triggers |
| **II** | 2020-2021 | HK$54B → **HK$457B** | Pandemic QE, tech IPOs, capital inflows |
| **III** | 2022-2023 | HK$457B → **HK$44.7B** | Fed hiking (+500bps), **40 interventions**, -90% |
| **IV** | 2025-2026 | HK$44.7B → HK$174B → **HK$53.9B** | Rollercoaster volatility |

### 2025 Volatility Spike (Phase IV Detail)
- **May 2025:** Southbound Connect surge + IPOs → HKMA sold HK$129.4B in single day → AB quadrupled to HK$174B
- **Jun-Jul 2025:** Low HIBOR (0.96%) triggered massive carry trades → AB drained to HK$101.2B
- **Jan 2026:** Stabilized at **HK$53.9B**

---

## Key Thresholds

### Aggregate Balance

| Level | Significance |
|-------|--------------|
| **<HK$45B** | "Psychological floor" — interbank highly sensitive |
| **<HK$40B** | HIGH sensitivity to liquidity shocks |
| **Zero** | Not failure — rates spike to whatever level stops outflows |

### Interest Rate Differentials

| Period | 1M HIBOR | 1M SOFR | Spread | Impact |
|--------|----------|---------|--------|--------|
| Dec 2019 | 2.49% | 1.50-1.75% | +75bps | Inflow/Stable |
| Dec 2023 | 5.15% | 5.30% | -15bps | Neutral |
| **May 2025** | **0.96%** | 5.00% | **-404bps** | Massive carry trade |
| Aug 2025 | 2.60% | 4.50% | -190bps | HIBOR recovery |
| Dec 2025 | ~4.00% | 4.25-4.50% | -25-50bps | Stabilization |

**Critical threshold:** HIBOR-SOFR spread **>200bps** during weak HKD = carry trade stress

---

## Short-Seller Thesis — Rebutted

### The Bass/Ackman Arguments
- As AB falls to zero, HKMA "runs out of money"
- The "trilemma" will eventually break the peg

### HKMA Rebuttal
1. **AB is a liability, not an asset.** Contraction to zero IS the defense mechanism — rates simply spike.
2. **Reserves depth:** HKMA holds **>US$415B** in reserves (114% of GDP)
3. **PBOC backstop:** $3T+ reserves, signaled willingness to support HKMA
4. **1997 precedent:** HKMA spent HK$118B buying equities to defeat "double play" speculators — willing to use unconventional measures

---

## Geopolitical Tail Risks

### 1. US Sanctions "Nuclear Option"
- **Hong Kong Autonomy Act (HKAA):** Authority to sanction individuals/entities for "erosion of autonomy"
- **SDN listing = death sentence:** Cuts off USD clearing (CHIPS) access
- **Nuclear scenario:** US denies HKMA or major HK banks (e.g., BOCHK) USD clearing
- **Probability:** Low, but **being discussed in NSC circles**

### 2. RMB Pivot
- Theory: De-peg from USD, link to RMB or basket
- **Hurdles:**
  - RMB not fully convertible (currency board prerequisite)
  - 40 years of USD peg credibility — switching during stress = capital flight
  - Reserves are USD-denominated — pivot requires massive asset reallocation

### 3. Property Market Stress
- Prices down ~30% from 2021 peaks
- HIBOR-linked mortgages rise when peg is defended
- Negative equity risk if sharp correction + liquidity squeeze
- **Mitigant:** Banking sector capital ratio 24.4% (Jun 2025) — can withstand 1997-level shocks

---

## Forced UST Liquidation — The Global Transmission Channel

### HKMA Holdings (End-2024)

| Asset Class | HK$ Million | Share |
|-------------|-------------|-------|
| **USD Assets** | 3,230,422 | **79.1%** |
| HKD Assets | 260,243 | 6.4% |
| Other (RMB, EUR) | 590,310 | 14.5% |
| **Total** | 4,080,975 | 100% |

**Implication:** HKMA holds **~US$410B in USTs and agency debt**

### The Liquidation Mechanism
1. HKD hits 7.85 weak-side, capital continues fleeing
2. HKMA must sell USD to buy HKD
3. To get USD, HKMA sells US Treasuries
4. **Severe crisis:** Could force **hundreds of billions** in UST sales in weeks

### Global Market Impact
- **Yield spike:** Sudden UST supply → prices down → yields up
- **Contagion:** If HKMA selling, PBOC may follow → potential UST "crash"
- **Borrowing costs:** Spike for US government and global private sector

### Safety Valve: FIMA Repo Facility
- Fed allows HKMA to **borrow USD using USTs as collateral** instead of selling
- Critical mechanism to prevent disorderly liquidation
- Available since 2020 — explicitly designed for this scenario

---

## Early Warning Indicators (EWIs)

### Quantitative Dashboard

| Indicator | Stressed Threshold | Rationale |
|-----------|-------------------|-----------|
| **Option-implied volatility** | >5.0% (HKD/USD) | Market pricing a break |
| **Aggregate Balance** | <HK$40B | High liquidity sensitivity |
| **12-month forward points** | >1,500 | Devaluation fear |
| **Backing Ratio** | <105% | Exchange Fund surplus depleting |
| **HKD deposit growth** | Negative YoY | Capital flight / dollarization |
| **UST yield spike** | >20bps on HKMA selling | Market can't absorb liquidation |
| **HIBOR-SOFR spread** | >200bps (weak HKD) | Carry trade stress |

### Qualitative Indicators
- **Sanctions escalation:** US Treasury targeting HKMA or BOCHK
- **Mainland stimulus:** Large stimulus → capital into HK → strong-side pressure
- **Discount Window stigma:** Banks avoiding DW → localized liquidity crises

---

## Scenario Analysis: What a Peg Break Looks Like

### Path A: Forced Devaluation (Crisis)
- Extreme capital flight (banking collapse or geopolitical shock)
- HKD floats → immediate sharp depreciation
- Volatile downward spiral until new equilibrium

### Path B: Controlled RMB Pivot
- Multi-stage process: Widen band → Basket peg → RMB anchor
- Final integration of HK into Mainland financial system
- Would mark end of "One Country, Two Systems" in finance

### Path C: One-Off Revaluation
- Move central parity from 7.80 to stronger level (e.g., 7.00)
- Lower import costs, cool property market
- Hurt service hub competitiveness

---

## Key Takeaways for ZHAO

### Transmission to UST Markets
1. **HK stress → HKMA UST liquidation** is a direct transmission channel
2. **~$410B** in potential forced selling
3. **FIMA Repo** is critical safety valve but may not be available in sanctions scenario
4. If HKMA selling triggers PBOC defensive selling → **contagion cascade**

### Current Status (Jan 2026)
- AB: **HK$53.9B** (above $45B floor, stable)
- HIBOR-SOFR spread: **~25-50bps** (normalized)
- Backing ratio: ~110% (healthy)
- **No immediate stress indicators**

### Tail Risk Watch
- Primary: **US sanctions escalation** (SDN listing of HK financial institutions)
- Secondary: **Property crash + liquidity squeeze** coinciding
- Tertiary: **PBOC stress** forcing UST sales that cascade to HKMA

---

## Integration with ZHAO Framework

The HK peg is a **pressure valve** for China stress:

1. **Normal times:** HK functions as China's capital account gateway
2. **Stress times:** Capital flight from China routes through HK → HKD weakens → AB drains
3. **Crisis times:** If PBOC facing liquidity crunch (Feb 2026 $456B event), may force HKMA to assist
4. **Extreme tail:** US sanctions + China stress → HK peg defense triggers massive UST liquidation

**Synthesis:** HK peg is not just a local issue — it's a **global systemic risk transmission channel** from China stress to US bond markets.

---

*Key insight: The LERS is built to withstand economic shocks; its ultimate test will be whether it can withstand a complete rupture in the global rules-based order.*
