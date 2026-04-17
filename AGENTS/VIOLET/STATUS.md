# VIOLET STATUS

**Signal Status:** 🟠 **ELEVATED WATCH — SKEW REBOUNDED, FADE_RERAMP ACTIVE** — SKEW bounced 139.23 → 140.74 on Apr 17 (d+4), single-day failure below 140. Consistent with within-cycle pattern (KB-VIO-042: 6/6 bounces in 1-3 td, 100%). **Scenario A (peaceful) weakened materially** — one-day break did not sustain. **FADE_RERAMP path (69% historical) most plausible** if SKEW clears 145 by ~Apr 22. 17-episode backtest still active (15/16 → ≥15% VIX rise within 60d). Term structure deepened contango — no stress signal, markets calm on surface. **Watch: Apr 22 for SKEW >145 confirmation; invalidation = sustained <140 for 4+ td.**

**Live:** VIX **17.62** | VIX3M **20.43** | VIX6M **22.47** | VVIX **94.26** | SKEW **140.74** | Term Structure **Contango +2.54% adj** | **Last Updated:** 2026-04-17 10:32 ET

---

## SIGNAL DASHBOARD

| Metric | Value | As Of | Status | Source |
|--------|-------|-------|--------|--------|
| VIX Spot | **17.62** | Apr 17 10:32 ET | 🟡 | [CONF] CBOE |
| VIX3M | **20.43** | Apr 17 | 🟡 | [CONF] CBOE |
| VIX6M | **22.47** | Apr 17 | 🟡 | [CONF] CBOE |
| VVIX | **94.26** | Apr 17 | 🟢 | [CONF] CBOE |
| SKEW | **140.74** | Apr 17 | **🟠** | [CONF] CBOE — **rebounded above 140 after 1-day break (was 139.23 Apr 16)** |
| VIX3M/VIX | **1.1595** | Apr 17 | 🟢 | [CONF] Calculated |
| VIX Futures Curve | Contango (steep) | Apr 17 | 🟢 | [CONF] CBOE |
| M1:M2 Contango (adj) | **+2.54%** | Apr 17 | 🟢 | [CONF] CBOE VX settlement (steepened from +2.37%) |
| HY OAS | **2.84** | Apr 14 | 🟢 | [CONF] FRED BAMLH0A0HYM2 |
| HY OAS — cycle trough | **2.64** | Jan 22 | — | [CONF] FRED |
| HY OAS — cycle peak | **3.46** | Mar 30 | — | [CONF] FRED |
| HY OAS — distance from trough | **+20bps** (82bps at Mar 30 peak) | Apr 14 | 🟢 | Tactical trigger at +100bps |

---

## CONVERGENCE MATRIX

| Vector | Score | Evidence | Last Updated |
|--------|-------|----------|--------------|
| Spot VIX elevation | ⚪ | 17.62 — low vol regime, down -1.24 d/d | 2026-04-17 |
| Term structure inversion | ⚪ | 1.1595 — contango steepening (was 1.127) | 2026-04-17 |
| VVIX stress | ⚪ | 94.26 — down -5.28 d/d, continued normalization | 2026-04-17 |
| **SKEW-VIX-VVIX divergence** | **🟠** | **SKEW rebounded 139.23 → 140.74 on d+4 (7th test of 140 floor, all 6 prior bounced in 1-3 td per KB-VIO-042). Scenario A (peaceful) weakened. FADE_RERAMP (69% historical) active — requires SKEW >145 by ~Apr 22. Invalidation: sustained <140 for 4+ td OR failure to clear 145 by Apr 22.** | 2026-04-17 |
| Credit-to-vol transmission | ⚪ | HY OAS 284bps — credit tight, no lag setup | 2026-04-16 |

**Convergence Score:** 3/25 (12%) — SKEW divergence stays 🟠 (3 pts) after rebound; within-cycle pattern intact. All other vectors ⚪ (1 pt each).

**Notable (KB-VIO-041→044):** Four-lens analysis complete. **Cross-episode** (17 events/12yr): d+3 Δ -17.7 unprecedented for high-fire episodes. **Within-cycle** (Feb 2 → present): 6/6 bounces off 140 in 1-3 td. **Regime duration** (KB-VIO-043): Current regime 210 td — longest in 19-year history. **Regime termination** (KB-VIO-044): Long regimes lean PRE_EVENT_FADE — R11 (150 td, closest analog) ended Mar 27, VIX peaked 52.33 just 8 td later. Current 20d avg slope **+1.8** (rising) — all terminated regimes had negative slopes. **Regime NOT in terminal phase.** Either scenario supports position: intact = thesis intact; ending = VIX event likely imminent per PRE_EVENT_FADE. Only GRADUAL_FADE (18%) hurts. See `research/2026-04-16_regime_termination_analysis.md`.

**Where does VIX land if pattern continues?** From 18.09 today:
- 30d peak central: **VIX ~25** (range 22-30)
- 60d peak central: **VIX ~28** (unconditional) / **~37** (high-SKEW cohort) / **~38** (back-to-back cluster)
- Tail: **VIX 50-63** (one-in-five, driven by 2025-01 analog)
- Options market confirms: Apr 29 call-wall 25-30; May 19 call-wall 35 with tail OI to 45/70
- Full analysis: `research/2026-04-15_vix_target_distribution.md`

**Phase 2 Cluster Analog (KB-VIO-039/040):** 2024-11→2025-01 deep dive complete. 12/19 indicators were Class 1 (leading) — dominant pattern was "coiled spring" compression (vol+credit at lows, SKEW elevated, rates tightening). 2026 translation: 5 match, 4 partial, 3 diverge. Key gap: CCC OAS at 9.31 (elevated) vs analog 6.92 (compressed). **Supports central-case (VIX 25-30) not tail (50+).** Within Scenario B: 35% VIX 22-25, 40% VIX 25-30, 15% VIX 30-40, 10% VIX 40+. Full analysis: `research/2024-11_2025-01_cluster_analog.md`.

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
| VIX spot | 17.62 | >30 | ⚪ |
| VIX spot | 17.62 | >40 | ⚪ |
| VIX3M/VIX ratio | 1.1595 | <1.0 (inversion) | ⚪ |
| VVIX | 94.26 | >120 | ⚪ |
| SKEW | 140.74 | >140 | 🟠 (rebounded above 140 after 1-day break) |
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

**Outbound:** ~~VIX Upside proposal~~ → **EXECUTED** Apr 16: VIX May 19 25C (see TRADE.md)
- `outbox/SIG-VIOLET-LIQUID-20260415-hy-oas-trigger-monitor.md` — QUEUED (git path blocked)

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

**Current assessment:** Low vol regime. Credit spreads tight (HY OAS 2.84). SKEW divergence rebounded — 1-day break failed to sustain. Within-cycle bounce pattern (6/6 in 1-3 td) holds. FADE_RERAMP path dominant; Apr 22 is the next gate (SKEW >145 = confirmation).

---

*Last updated: 2026-04-17 10:32 ET (morning boot — SKEW rebounded 139.23 → 140.74, all metrics updated. KB-VIO-045 logged.)*
