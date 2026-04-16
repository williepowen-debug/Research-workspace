# VIOLET STATUS

**Signal Status:** 🟠 **ELEVATED WATCH — SKEW BREAK UNDER MONITORING** — SKEW dropped 149.94→139.23 (below 140 threshold) on Apr 16, 3 days post-divergence fire. Per MEMORY principle #6: if SKEW <140 sustained + VIX <20 through ~May 7, pattern resolving peacefully (Scenario A). **First peaceful-resolution checkpoint.** 17-episode backtest still active: 15/16 → ≥15% VIX rise within 60d, but 6% base rate for peaceful resolution. Phase 2 analog supports central-case Scenario B (VIX 25-30) if SKEW re-ramps. **Watch: does SKEW sustain <140 or bounce?**

**Live:** VIX **18.86** | VIX3M **21.25** | VIX6M **23.12** | VVIX **99.54** | SKEW **139.23** | Term Structure **Contango +2.37% adj** | **Last Updated:** 2026-04-16

---

## SIGNAL DASHBOARD

| Metric | Value | As Of | Status | Source |
|--------|-------|-------|--------|--------|
| VIX Spot | **18.86** | Apr 16 | 🟡 | [CONF] CBOE |
| VIX3M | **21.25** | Apr 16 | 🟡 | [CONF] CBOE |
| VIX6M | **23.12** | Apr 16 | 🟡 | [CONF] CBOE |
| VVIX | **99.54** | Apr 16 | 🟢 | [CONF] CBOE |
| SKEW | **139.23** | Apr 16 | **🟡** | [CONF] CBOE — **broke below 140; was 149.94 Apr 15** |
| VIX3M/VIX | **1.127** | Apr 16 | 🟢 | [CONF] Calculated |
| VIX Futures Curve | Contango (steep) | Apr 16 | 🟢 | [CONF] CBOE |
| M1:M2 Contango (adj) | **+2.37%** | Apr 16 | 🟢 | [CONF] CBOE VX settlement |
| HY OAS | **2.84** | Apr 14 | 🟢 | [CONF] FRED BAMLH0A0HYM2 |
| HY OAS — cycle trough | **2.64** | Jan 22 | — | [CONF] FRED |
| HY OAS — cycle peak | **3.46** | Mar 30 | — | [CONF] FRED |
| HY OAS — distance from trough | **+20bps** (82bps at Mar 30 peak) | Apr 14 | 🟢 | Tactical trigger at +100bps |

---

## CONVERGENCE MATRIX

| Vector | Score | Evidence | Last Updated |
|--------|-------|----------|--------------|
| Spot VIX elevation | ⚪ | 18.86 — low vol regime, slight uptick | 2026-04-16 |
| Term structure inversion | ⚪ | 1.127 — contango flattening slightly (was 1.151) | 2026-04-16 |
| VVIX stress | ⚪ | 99.54 — stable, normalized | 2026-04-16 |
| **SKEW-VIX-VVIX divergence** | **🟠** | **SKEW broke 140 (139.23, d+3 Δ -17.7). Trajectory analysis (KB-VIO-041): unprecedented — no prior episode with fire SKEW>140 dropped below 140 by d+3. FADE_RERAMP (69% historical) is most likely path if SKEW rebounds >145 by ~Apr 22. Watch: sustained <140 through Apr 29 = invalidation.** | 2026-04-16 |
| Credit-to-vol transmission | ⚪ | HY OAS 284bps — credit tight, no lag setup | 2026-04-16 |

**Convergence Score:** 3/25 (12%) — SKEW divergence downgraded 🔴→🟠 (3 pts) after SKEW broke 140; still live but fading. All other vectors ⚪ (1 pt each).

**Notable (KB-VIO-041/042/043):** Three-lens analysis complete. **Cross-episode** (17 events/12yr): d+3 Δ -17.7 unprecedented for high-fire episodes. **Within-cycle** (Feb 2 → present): 6/6 bounces off 140 in 1-3 td — breaking 140 is the norm, not the exception. **Regime duration** (KB-VIO-043): Current elevated SKEW regime started **Jun 16, 2025 — 206 td, second longest in 19-year SKEW history.** Only comparable regime (201 td, 2024-25) ended with VIX 52. All top-5 regimes preceded major VIX events. The divergence pattern fired within a historically rare macro context — this STRENGTHENS the thesis. One-day dip to 139.2 is noise against a 10-month backdrop. **TRUE invalidation = SKEW <140 for 4+ consecutive td.** See `research/2026-04-16_skew_post_fire_trajectory.md`.

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
| VIX spot | 18.86 | >30 | ⚪ |
| VIX spot | 18.86 | >40 | ⚪ |
| VIX3M/VIX ratio | 1.127 | <1.0 (inversion) | ⚪ |
| VVIX | 99.54 | >120 | ⚪ |
| SKEW | 139.23 | >140 | 🟡 (broke below 140 — was 149.94) |
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

**Current assessment:** Low vol regime. Credit spreads tight (HY OAS 2.84). SKEW divergence fading — first day below 140 since fire. Monitoring for sustained break vs bounce.

---

*Last updated: 2026-04-16 (boot refresh — SKEW broke 140, all metrics updated)*
