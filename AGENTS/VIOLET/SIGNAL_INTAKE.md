# VIOLET SIGNAL INTAKE

What VIOLET watches for — internal monitoring priorities and external signals from other agents.

---

## INTERNAL MONITORING

### VIX Spot Levels

| Level | Significance | Action |
|-------|--------------|--------|
| VIX < 15 | Extreme complacency | Flag for reversal watch |
| **VIX 15-26** | **🎯 SWEET SPOT** | **Buy VIX calls when HY OAS widens >100bps** |
| VIX 26-30 | High vol | Alert HENRY, LIQUID — edge compressing |
| VIX 30-40 | Stress | Too late — already panicking |
| VIX > 40 | Crash | Relationship inverts — VIX leads credit |

### The Sweet Spot Trigger (Credit-Vol Lag)

**When ALL conditions met:**
1. VIX 15-26 ✅ (currently ~18)
2. HY OAS widens >100bps from recent low (currently +20bps from 2.64 trough — NOT triggered)
3. Cross-sector widening (not just energy)
4. Yield curve not inverted ✅ (10Y-2Y +50bps)
5. Sustained >5 days, VVIX confirming

**Action:** Buy VIX calls 30-60 DTE, 1-2% account
**Target:** VIX +10pts within 2-6 weeks
**Stop:** HY OAS reverses 50bps, VIX >30, or yield curve inverts

**Current Status:** VIX in sweet spot — waiting for HY OAS trigger. Tactical trigger at +100bps from trough (HY OAS 3.64).

### SKEW Divergence Trigger (Highest Conviction)

**Pattern:** SKEW rises ≥10pts while VIX falls ≥5pts AND VVIX falls ≥15pts over 20-day window.

**Current Status:** 🔴 **FIRED Apr 13.** SKEW peak 156.9. Episode #17 in 19-year sample. 94% hit rate for ≥15% VIX rise within 60d. See KB-VIO-036.

**Action:** VIX upside trade — proposal submitted to FORGE/INBOX.md (Apr 15). Awaiting Will's vehicle/strike/expiry decision.

**Monitoring:**
- SKEW <140 sustained → pattern resolving peacefully → exit
- SKEW re-ramp >155 → severity confirmation → add
- VIX3M/VIX <1.05 → tactical entry signal
- CCC OAS >10.0 → analog alignment strengthens → add

**Timing:** Median peak at day 39 (IQR 32-46). High-SKEW cohort median 44 days. Central window: **May 15-27**.

### Term Structure Watch

| Pattern | Significance | Action |
|---------|--------------|--------|
| VIX3M/VIX > 1.15 | Steep contango | Normal |
| VIX3M/VIX 1.0-1.15 | Flat contango | Early warning |
| VIX3M/VIX < 1.0 | Inversion | 🔴 Alert — leading indicator |
| VIX6M/VIX3M < 1.0 | Backwardation | 🔴🔴 Critical — stress confirmed |

### VVIX (Vol of Vol) Watch

| Level | Significance |
|-------|--------------|
| VVIX < 80 | Low vol-of-vol — complacency |
| VVIX 80-100 | Normal range |
| VVIX 100-120 | Elevated — option market nervous |
| VVIX > 120 | 🟠 Stress — vol sellers at risk |
| VVIX > 150 | 🔴🔴 Extreme — vol spike likely |

### SKEW Watch

| Level | Significance |
|-------|--------------|
| SKEW < 120 | Complacency — tail risk cheap |
| SKEW 120-135 | Normal range |
| SKEW 135-150 | Elevated tail risk pricing |
| SKEW > 150 | 🟠 Crash protection expensive — fear present |

---

## EXTERNAL SIGNALS (From Other Agents)

### From BROCK (Private Credit)

| Signal | VIX Implication | Priority |
|--------|-----------------|----------|
| BDC gating event | Vol spike likely within 5-10 days | 🔴 |
| Non-accrual spike | Credit stress → vol lag | 🟠 |
| NAV markdowns | Forward-looking stress | 🟠 |

### From LIQUID (Credit/Funding)

| Signal | VIX Implication | Priority |
|--------|-----------------|----------|
| HY OAS +50bps in 1 week | Vol should follow — check lag | 🔴 |
| CCC OAS > 1000 | High yield stress → vol spike | 🔴 |
| SOFR-IORB > 0.25 | Funding stress → vol rise | 🟠 |
| Gold margin cascade | Safe haven bid → vol correlation | 🟠 |

### From HENRY (Market Structure)

| Signal | VIX Implication | Priority |
|--------|-----------------|----------|
| FOMC surprise | Immediate vol spike | 🔴 |
| Zero gamma breach | Acceleration risk | 🟠 |
| Dealer short gamma | Vol expansion likely | 🟠 |
| 0DTE flow spike | Microstructure vol impact | 🟡 |

### From HAWK (Geopolitical)

| Signal | VIX Implication | Priority |
|--------|-----------------|----------|
| War escalation | Immediate vol spike | 🔴 |
| Ceasefire breakdown | Vol reversal | 🔴 |
| Hormuz closure threat | Energy vol → equity vol | 🔴🔴 |

### From RED (Adversarial)

| Signal | VIX Implication | Priority |
|--------|-----------------|----------|
| Scenario D escalation | Vol spike expected | 🔴 |
| Position stress test fail | Hedging review | 🟠 |

---

## CREDIT-TO-VOL LAG TRACKING

**Core thesis (Four-Model Synthesis):** Aggregate HY OAS leads VIX by 2-6 weeks at tactical level (100bps → spike) and ~7 months at cycle level (trough → peak). Relationship is regime-dependent and strongest when shock originates in credit markets.

**Historical Episode Database:**
| Episode | Credit Lead | VIX Lag | Regime | Notes |
|---------|-------------|---------|--------|-------|
| GFC 2007-08 | 6-10 weeks | Aug 2007 spike | Low vol → rising | Credit-led, 14 months to sustained >30 |
| 2011 EU crisis | 8-10 weeks | Aug 2011 spike | Rising vol | Sovereign contagion |
| 2015-16 Energy | 12-18 months | Brief Aug 2015 spike | Low vol | Sector-specific, partial false positive |
| Q4 2018 | Coincident | Oct 2018 | Rising vol | Macro/rate-driven, credit lagged |
| Feb 2018 Volmageddon | N/A (no credit move) | Feb 5, 2018 | Low vol | VIX-led false positive |
| COVID 2020 | Near-simultaneous | Feb-Mar 2020 | Rising → crash | Exogenous shock, VIX peaked 7 days before credit |
| 2022 Rate Shock | VIX led by 10-12 weeks | Jan 2022 | Low vol → rising | Rates-driven, structural divergence |
| Aug 2024 Yen Unwind | N/A (no credit move) | Aug 5, 2024 | Low vol | VIX-led false positive |

**Key Finding:** Credit leads in ~70% of credit-originated crises (GFC, 2011, 2015-16). VIX leads or coincident in exogenous/macro shocks (2018, 2020, 2022, 2024).

**False Positive Patterns:**
- Sector-specific widening without systemic stress (energy 2015-16)
- Technical VIX spikes without credit confirmation (Volmageddon 2018, yen unwind 2024)
- Rate-driven equity selloffs with healthy credit fundamentals (2022)
- Fed QE backstop suppressing credit spreads (2020-21)

---

## SIGNAL PROCESSING PROTOCOL

1. **Receive signal** (inbox/ or direct mention)
2. **Log to FLOW.tsv** — Date, From, To, Type, Content, Status
3. **Assess VIX implication** — Will this move VIX? How much? How fast?
4. **Check current VIX state** — Is market already pricing this?
5. **Update STATUS.md** — If significant, update dashboard
6. **Send outbound signals** — If warranted, write to outbox/
7. **Log to KB.tsv** — Permanent record of signal and response

---

## OUTBOUND SIGNAL TRIGGERS

VIOLET sends signals when:

| Condition | Target | Priority | Content |
|-----------|--------|----------|---------|
| VIX spikes >30% in 5 days | HENRY, RED | 🔴 | Vol regime shift |
| SKEW divergence fires | WALTER, HENRY, RED | 🔴 | Coiled-spring pattern — see KB-VIO-036 |
| Term structure inverts | LIQUID, HENRY | 🔴 | Peak marker (v3.1: marks peak, not onset) |
| VVIX > 120 | RED, HENRY | 🟠 | Vol-of-vol stress |
| Credit spreads widen >50bps, VIX flat | HENRY, RED | 🟠 | Credit-vol divergence |
| Regime shift detected | All agents | 🟠 | Low vol → rising vol |
| CCC OAS >10.0 | LIQUID, RED | 🟠 | Low-quality credit cracking — analog alignment |

**Signals sent this cycle:**
- WALTER: VIX Apr 15 refresh + SKEW divergence escalation (Apr 15)
- LIQUID: HY OAS trigger monitor (outbox, Apr 15)
- FORGE: VIX Upside trade proposal (INBOX.md, Apr 15)

---

*Created: 2026-04-12*
*Last Updated: 2026-04-16*
