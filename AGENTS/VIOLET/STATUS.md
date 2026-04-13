# VIOLET STATUS

**Signal Status:** 🟡 WATCH — VIX **19.23** | VIX3M **21.86** | VVIX **107.30** | SKEW **144.18** | Term Structure **Contango** | **Last Updated:** 2026-04-12

---

## SIGNAL DASHBOARD

| Metric | Value | As Of | Status | Source |
|--------|-------|-------|--------|--------|
| VIX Spot | **19.23** | Apr 11 | 🟡 | [CONF] CBOE |
| VIX3M | **21.86** | Apr 11 | 🟡 | [CONF] CBOE |
| VIX6M | — | — | ⚪ | — |
| VVIX | **107.30** | Apr 11 | 🟡 | [CONF] CBOE |
| SKEW | **144.18** | Apr 11 | 🟡 | [CONF] CBOE |
| VIX3M/VIX | **1.14** | Apr 11 | 🟡 | [CONF] Calculated |
| VIX Futures Curve | Contango | Apr 11 | 🟡 | [CONF] CBOE |
| HY OAS | **2.90** | Apr 9 | 🟢 | [CONF] FRED |

---

## CONVERGENCE MATRIX

| Vector | Score | Evidence | Last Updated |
|--------|-------|----------|--------------|
| Spot VIX elevation | ⚪ | 19.23 — below 20 threshold | 2026-04-12 |
| Term structure inversion | ⚪ | 1.14 (contango) | 2026-04-12 |
| VVIX stress | ⚪ | 107.30 — below 120 threshold | 2026-04-12 |
| Skew elevation | 🟡 | 144.18 — elevated tail risk bid | 2026-04-12 |
| Credit-to-vol transmission | ⚪ | HY OAS 2.90 — tight, no stress | 2026-04-12 |

**Convergence Score:** 1/25 (4%)

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
| VIX spot | 19.23 | >30 | ⚪ |
| VIX spot | 19.23 | >40 | ⚪ |
| VIX3M/VIX ratio | 1.14 | <1.0 (inversion) | ⚪ |
| VVIX | 107.30 | >120 | ⚪ |
| SKEW | 144.18 | >140 | 🟡 |
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

*Last updated: 2026-04-12 (initialization complete)*
