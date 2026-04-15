# VIOLET STATUS

**Signal Status:** 🟠 **ELEVATED WATCH** — Post-stress recovery with persistent SKEW bid. 17-episode backtest (KB-VIO-036) shows 15/16 completed analogs produced ≥15% VIX rise within 60 days; 9/16 produced ≥50% rise. Our SKEW peak 156.9 places us in the high-severity historical cohort. **Scenario B (new VIX event within 60 days) probability revised 30% → 66%**. See KB-VIO-031 (revised).

**Live:** VIX **18.09** | VIX3M **20.81** | VIX6M **22.85** | VVIX **99.56** | SKEW **149.94** | Term Structure **Contango +2.04% adj** | **Last Updated:** 2026-04-15

---

## SIGNAL DASHBOARD

| Metric | Value | As Of | Status | Source |
|--------|-------|-------|--------|--------|
| VIX Spot | **18.08** | Apr 15 | 🟡 | [CONF] CBOE |
| VIX3M | **20.81** | Apr 15 | 🟡 | [CONF] CBOE |
| VIX6M | **22.85** | Apr 15 | 🟡 | [CONF] CBOE |
| VVIX | **98.77** | Apr 15 | 🟢 | [CONF] CBOE |
| SKEW | **149.94** | Apr 15 | 🟠 | [CONF] CBOE |
| VIX3M/VIX | **1.151** | Apr 15 | 🟢 | [CONF] Calculated |
| VIX Futures Curve | Contango (steep) | Apr 15 | 🟢 | [CONF] CBOE |
| M1:M2 Contango (adj) | **+2.04%** | Apr 14 | 🟢 | [CONF] CBOE VX settlement |
| HY OAS | **2.90** | Apr 9 | 🟢 | [CONF LIQUID Apr 10] |

---

## CONVERGENCE MATRIX

| Vector | Score | Evidence | Last Updated |
|--------|-------|----------|--------------|
| Spot VIX elevation | ⚪ | 18.09 — low vol regime post-recovery | 2026-04-15 |
| Term structure inversion | ⚪ | 1.151 — steep contango, no warning | 2026-04-15 |
| VVIX stress | ⚪ | 99.56 — normalized from Mar peak 133 | 2026-04-15 |
| **SKEW-VIX-VVIX divergence** | **🔴** | **Magnitude-matched 20d divergence fired Apr 13; SKEW peak 156.9 in high-severity cohort. 17-episode backtest: 15/16 → VIX rise ≥15% within 60d** | 2026-04-15 |
| Credit-to-vol transmission | ⚪ | HY OAS 290bps — credit rallying, no lag setup | 2026-04-15 |

**Convergence Score:** 4/25 (16%) — SKEW divergence escalated 🟠→🔴 (5 pts) after empirical backtest; all other vectors ⚪ (1 pt each)

**Notable:** Pattern is rare (1% base rate, 17 events in 19 years) but strongly predictive over 60-day window. Recent analogs 2024-05 → Aug 2024 yen unwind; 2024-11 → Q1 2025 vol regime; 2025-12 → our Mar 2026 event. See `research/2026-04-15_skew_divergence_episodes.md`.

---

## REGIME STATUS

**Current Regime:** LOW VOL (VIX < 20)

**Regime Characteristics:**
- VIX mean-reverts quickly
- Credit-vol correlation weak (~0.06)
- Term structure in contango
- Vol-of-vol (VVIX) subdued
- **Longest lead time when credit widens:** 6-16 weeks

**Historical Regimes Mapped (Four-Model Synthesis):**
| Regime | VIX Range | Credit Lead Time | Signal Quality | Use Case |
|--------|-----------|------------------|----------------|----------|
| Low vol | < 15 | 6-16 weeks | **Highest** | Early warning, begin monitoring |
| Low vol | 15-20 | 3-8 weeks | **High** | Activate tracking, prepare entry |
| Rising vol | 20-30 | 1-4 weeks | **Moderate** | Co-movement — less edge |
| High vol | 30-40 | 0-2 weeks | **Low** | Too late — already panicking |
| Crash | > 40 | VIX leads credit | None | Relationship inverts |

---

## KEY THRESHOLDS

| Metric | Current | Threshold | Status |
|--------|---------|-----------|--------|
| VIX spot | 18.08 | >30 | ⚪ |
| VIX spot | 18.08 | >40 | ⚪ |
| VIX3M/VIX ratio | 1.151 | <1.0 (inversion) | ⚪ |
| VVIX | 98.77 | >120 | ⚪ |
| SKEW | 149.94 | >140 | 🟠 (approaching 150) |
| Credit-VIX divergence | None | HY OAS >4, VIX 15-26 | ⚪ |

## CREDIT-TO-VOL LAG FRAMEWORK (Four-Model Synthesis)

**Core Signal:** HY OAS widening >100bps from recent low + **VIX 15-26** (sweet spot) + normal yield curve = 2-6 week lead time to VIX spike >10pts

**Hit Rate:** ~70% | **False Positive Rate:** ~25-30% (reduced to ~15-20% with yield curve filter)

**Two Lead Times to Track:**
| Horizon | Trigger | Lead | Use |
|---------|---------|------|-----|
| **Strategic** | HY OAS trough | ~7 months to equity peak | Position sizing, regime awareness |
| **Tactical** | 100bps widening | 2-6 weeks to VIX spike | Trade entry, hedge timing |

**Confirmation Checklist:**
1. ✅ HY OAS >100bps from recent low (baseline trigger)
2. ✅ VIX < 20 at onset (ensures longest lead time)
3. ✅ Cross-sector widening (not just energy)
4. ✅ Yield curve not inverted (filters rate-driven shocks)
5. ✅ No Fed QE backstop active (avoids 2020-21 divergence)

**All 5 checks = highest confidence signal | Checks 1-3 = medium confidence | Check 1 only = monitor, don't trade**

---

## WHAT TO WATCH

**From HENRY:**
- FOMC surprises
- Gamma positioning (zero gamma level)
- Macro shocks

**From LIQUID:**
- HY OAS moves >20bps (currently 2.90)
- CCC OAS spikes
- Funding stress (SOFR-IORB)

**From BROCK:**
- Private credit gating events
- BDC stress

**From HAWK:**
- Geopolitical escalation
- War developments

**From RED:**
- Adversarial scenarios with vol impact

---

## CROSS-AGENT SIGNALS (Pending)

**Outbound:** None

**Inbound:** None

---

## RESEARCH QUEUE

| Priority | Topic | Status |
|----------|-------|--------|
| 🟢 | Historical VIX data (2018-present) | **COMPLETE** — 2,019 days loaded |
| 🟢 | Crisis analogs (Feb 2018, Mar 2020, Feb 2021) | **COMPLETE** — documented in research/crisis_analogs/ |
| 🟢 | Credit-to-vol lag quantification | **COMPLETE** — VIX leads credit in crash regimes |
| 🟡 | Term structure regime definitions | Partial — need VIX futures curve data |
| 🟡 | VVIX and SKEW patterns | Partial — baseline established |
| ⚪ | VIX options flow analysis | Not started |

---

## THESIS CONNECTION

**Core hypothesis (REVISED):** Credit-vol relationship is regime-dependent.

- **Low vol:** Weak correlation, no clear lead-lag
- **Rising vol:** Credit and VIX move together (0-5 day lag)
- **Crash:** VIX leads credit (vol shock front-runs credit)

**Transmission chain:**
```
BROCK (PC stress) → LIQUID (HY/CCC spreads) → VIOLET (regime detection) → HENRY (equity impact)
```

**Current assessment:** Low vol regime. Credit spreads tight (HY OAS 2.90). No divergence signal.

---

*Last updated: 2026-04-15 (P1 refresh — VIX/VIX3M/VIX6M/VVIX/SKEW live reads)*
