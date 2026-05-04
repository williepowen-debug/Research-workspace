# Apr 22 Gate Post-Mortem + Scenario Re-Anchoring

**Date:** 2026-05-03
**Author:** VIOLET
**Approval:** Will, May 3 boot session
**Trigger:** 16-day VIOLET dark interval (Apr 18 → May 3) with both gate criteria from KB-VIO-045/047 resolving

---

## TL;DR

- **FADE_RERAMP gate (SKEW >145 by Apr 22) FAILED.** SKEW peaked 140.84 on Apr 22; never cleared 145.
- **Strict invalidation rule (sustained <140 for 4+ td) WAS HIT.** Apr 23-28: four consecutive trading days below 140 (139.59 → 139.08 → 139.64 → 138.16). Then bounced post-FOMC to 143.33 by Apr 30.
- **Both BOJ (Apr 28, 3 dissents) and FOMC (Apr 28-29, 4 dissents — most since 1992) hawkish-tilted holds. VIX absorbed both: peaked 19.50 Apr 21, crushed to 16.89 Apr 30.**
- **Credit COMPRESSED further:** HY OAS 2.86 → 2.83, CCC OAS 9.21 → 9.09 (moving AWAY from 10.00 analog threshold).
- **20d-SKEW-slope decelerated from +1.8 (Apr 16) → +0.6 (May 3).** Still positive — regime NOT in terminal phase. Closest comparable terminations had final 5d slopes of -2.0 to -3.5.
- **Re-classification:** Pattern is GRADUAL_FADE-WITH-REBOUND. The specific Apr 13 divergence trade is invalidated under strict rule. The broader SKEW regime (>140 since Jun 2025, now 212 td) is intact but decelerating.
- **Updated scenario distribution (within 60d window from Apr 13, ~10-30 td remaining):**
  - **55% VIX <22** (low outcome — surface absorbs catalysts)
  - **25% VIX 22-25** (modest)
  - **12% VIX 25-30** (original central case)
  - **8% VIX 30+** (tail, requires external catalyst)

---

## 1. Original Framework (Apr 16-17)

From KB-VIO-044/045/047:

| Path | Historical Base Rate | 2026 Probability (Apr 16) | Trade Implication |
|------|---------------------|---------------------------|-------------------|
| FADE_RERAMP | 69% | DOMINANT | VIX 25-30 within 60d (favorable) |
| POST_EVENT_PERSIST | 5/11 long regimes | secondary | VIX event with regime intact |
| PRE_EVENT_FADE | 4/11 long regimes | secondary | Vol event imminent (favorable) |
| GRADUAL_FADE | 2/11 long regimes (18%) | tail | **The only path that hurts the position** |

**Confirmation gate:** SKEW >145 by ~Apr 22 (3 td after fire d+3 trough at 139.23) = FADE_RERAMP confirmed.

**Strict invalidation:** Sustained SKEW <140 for 4+ consecutive trading days OR failure to clear 145 by Apr 22.

---

## 2. What Actually Happened (Apr 17 → May 1)

### SKEW trajectory
| Date | SKEW | VIX | VVIX | Notes |
|------|------|-----|------|-------|
| Apr 17 | 141.82 | 17.48 | 95.13 | last VIOLET update before dark |
| Apr 20 | 141.90 | 18.87 | 98.15 | Mon open — slight uptick |
| Apr 21 | 140.91 | **19.50** | 101.89 | **VIX local high before FOMC** |
| **Apr 22** | **140.84** | 18.92 | 98.73 | **❌ GATE DAY — failed to clear 145** |
| Apr 23 | 139.59 | 19.31 | 98.57 | <140 td 1 |
| Apr 24 | 139.08 | 18.71 | 97.18 | <140 td 2 |
| Apr 27 | 139.64 | 18.02 | 93.86 | <140 td 3 |
| Apr 28 | **138.16** | 17.83 | 91.03 | **<140 td 4 — STRICT INVALIDATION HIT** + BOJ |
| Apr 29 | 141.88 | 18.81 | 96.02 | FOMC decision day — bounce |
| Apr 30 | 143.33 | **16.89** | 93.70 | **post-FOMC bounce + vol crush** |
| May 1 | 141.38 | 16.99 | 95.17 | |

### Key observations
1. **Gate failure was not narrow.** SKEW ceiling on/near Apr 22 was ~141 — 4 points short of the 145 trigger. This was a clear miss, not a near-miss.
2. **Strict invalidation triggered.** Apr 23-28 = 4 consecutive trading days below 140, the exact threshold from KB-VIO-042/045. SKEW hit 138.16 (lowest since the divergence fire on Apr 13).
3. **Post-FOMC rebound.** SKEW bounced from 138.16 → 143.33 in 2 td across the FOMC decision. This is the within-cycle pattern (KB-VIO-042) re-asserting — but it came AFTER the strict invalidation window had closed.
4. **Vol crush on FOMC day.** VIX 18.81 (Apr 29) → 16.89 (Apr 30). Classic post-decision IV crush despite 4 dissents (most since 1992). Vol surface treated the dissents as priced in.
5. **VVIX symmetry.** VVIX rose 95.13 → 101.89 into FOMC, crushed to 91.03 by Apr 28 — meaning the option market priced in vol expansion that didn't arrive.

### Credit during the interval
| Series | Apr 16 | Apr 22 (gate) | Apr 28 (FOMC) | Apr 30 |
|--------|--------|---------------|---------------|--------|
| HY OAS | 2.86 | 2.84 | 2.85 | 2.83 |
| CCC OAS | 9.21 | 9.13 | 9.11 | **9.09** |
| IG OAS | 0.81 | 0.79 | 0.81 | 0.81 |

Credit compressed across the interval — even on FOMC days. CCC moved 12bps tighter, away from the 10.00 analog confirmation threshold (KB-VIO-040). This is **not** the credit setup that supports a Phase 2 cluster-analog tail outcome.

---

## 3. Path Re-Classification

**Original 4 paths from KB-VIO-044, what each looks like ex-post:**

| Path | Required Pattern | What 2026 Looks Like | Verdict |
|------|------------------|---------------------|---------|
| FADE_RERAMP | SKEW <140 brief, rebound >145 by d+9 | Hit 138, rebounded only to 143.33 | ❌ Did not confirm |
| PRE_EVENT_FADE | Slope strongly negative; vol event within 8 td | Slope still +0.6; no event | ❌ Not active |
| POST_EVENT_PERSIST | Regime survives a vol event | No vol event yet | N/A |
| GRADUAL_FADE | Slow SKEW fade, no event in 60d | Best fit so far | ✅ Realising |

**But also: a fifth pattern emerging — REBOUND_AFTER_INVALIDATION.** SKEW broke the strict <140 4-td rule yet bounced to 143.33 on Apr 30. This is a within-cycle anomaly: the regime is more durable than the divergence-trade rules anticipated. KB-VIO-042 noted 6/6 prior bounces off 140 happened in 1-3 td; this one took 4 td (and crossed FOMC). The regime is **bending but not breaking**.

**Implication for the open trade:** The specific Apr 13 divergence fire is technically invalidated. The regime itself remains intact. These are two different things: a regime can be intact and still fail to produce the specific outcome (VIX 25-30 in 60d) that the trade was sized for.

---

## 4. Termination Slope Re-Read

20d-SKEW-slope analysis (KB-VIO-044): regime termination is best identified by sign-flip of the 20d-rolling-average slope.

| Regime | Final 5d Slope | What Followed |
|--------|---------------|---------------|
| R1 (60 td, 2018) | -3.5 | VIX 36.07 (PRE_EVENT_FADE) |
| R5 (107 td, 2021) | -3.5 | VIX 31.12 (PRE_EVENT_FADE) |
| R6 (59 td, 2022) | -2.6 | VIX 36.45 (GRADUAL_FADE 27 td later) |
| R9 (63 td, 2024) | -3.5 | VIX 19.23 (POST_EVENT_PERSIST) |
| R11 (150 td, 2025) | -2.0 | VIX 52.33 8 td later (PRE_EVENT_FADE) |
| **Current R12 (212 td)** | **+0.6** | **TBD — slope still positive** |

Apr 16 reading: +1.8. May 3 reading: +0.6. Decelerated by 1.2 in 12 td. If linear, slope would cross zero around mid-May and reach -2.0 around early June. But linear extrapolation is unreliable for slopes — the regime can reaccelerate or terminate abruptly.

**Read:** The regime is decelerating but not terminating. PRE_EVENT_FADE (the favorable termination scenario) is not yet activated. If the slope flips negative AND the trade window is still open (≤Jun 12), the position thesis re-strengthens via this path.

---

## 5. Updated Scenario Distribution

**Trade window from Apr 13 fire = 60 td closes ~Jun 12.** May 3 = ~14 td post-fire. **~30-40 td remaining** depending on how strict you are about "60 cal vs 60 td."

### Original distribution (Apr 16, KB-VIO-040, within Scenario B)
- 35% VIX 22-25
- 40% VIX 25-30
- 15% VIX 30-40
- 10% VIX 40+

### Updated distribution (May 3 post-mortem)

| VIX Bucket | Original | Updated | Driver of Change |
|-----------|----------|---------|------------------|
| **<22** (no event) | implicit | **55%** | FOMC + BOJ both absorbed, credit compressing, slope decelerating |
| **22-25** | 35% | **25%** | Mild move possible from May 13 CPI or May 19 expiration mechanics |
| **25-30** (central) | 40% | **12%** | Window compressed from 60→30-40 td; needs catalyst |
| **30-40** | 15% | **6%** | Tail; would need external catalyst |
| **40+** | 10% | **2%** | Cluster analog requires CCC crack — tightening |

### Key calibration anchors
- **Surface vol absorbs hawkish surprises.** Both BOJ and FOMC hawkish-tilted holds priced as carry-on. This is itself a regime characteristic — markets are not reactive in the current zone.
- **Credit is the leading indicator and it is compressing.** Without credit confirmation, the cluster-analog tail outcome is structurally weak.
- **SKEW regime is decelerating but intact.** Removes PRE_EVENT_FADE near-term. Removes the cleanest path to a favorable termination event.
- **Time decay is now the dominant force on the open trade.**

---

## 6. Implications for the Open Position

**VIX May 19 25C — Will's decision: HOLD (May 3 boot session).**

What HOLD means under updated probabilities:
- Position becomes a **lottery ticket on tail** (CPI surprise May 13, geopolitical shock, credit crack between now and May 19).
- Expected outcome: ~80%+ probability of expiring worthless or near-worthless.
- Optionality remains valuable IF the catalyst arrives — VIX move to 22+ on a CPI shock or credit event would deliver outsized return.
- The trade is no longer a divergence-thesis trade; it is a **macro-tail-hedge trade** in its remaining 16 DTE.

**This is consistent with HOLD as a position-management choice** — the premium is sunk, the convexity is asymmetric, and the marginal cost of carry to expiration is lower than the prospective gain on a tail-event print.

---

## 7. What This Means for Future Divergence Trades

Three calibration takeaways for the next divergence fire:

1. **The "long-regime advantage" cuts both ways.** Long regimes lean PRE_EVENT_FADE (KB-VIO-044) but they also have more capacity to absorb catalysts without breaking. Episode-17 fired in the longest regime in history; that durability has muted vol response.
2. **Credit compression alone tells you the analog won't fire the tail.** The Phase 2 (KB-VIO-039) cluster analog fired because credit was compressed AND the catalyst was external (tariffs). 2026 has the credit setup but no external catalyst yet — and credit is moving the wrong way (further compression).
3. **The strict 4-td invalidation rule held, but the regime didn't.** Use the 4-td rule for trade-level invalidation, but separate it from regime-level read. KB-VIO-042 may need revising — Episode-17 produced a 4-td <140 break followed by rebound, breaking the 100% within-cycle bounce-in-1-3-td pattern.

---

## 8. Files / KB Entries Generated

- This file: `research/2026-05-03_apr22_gate_postmortem.md`
- KB-VIO-049: Apr 22 gate failure
- KB-VIO-050: Strict invalidation rule triggered Apr 23-28 + post-FOMC rebound
- KB-VIO-051: 20d-slope refresh +1.8 → +0.6 (regime decelerating, not terminating)
- KB-VIO-052: Updated 60d-window scenario distribution
- KB-VIO-053: Credit-compression update through Apr 30 (HY 2.83, CCC 9.09)

**Status updates:**
- `STATUS.md` refreshed with May 3 dashboard + new convergence read
- `TRADE.md` HOLD decision recorded
- `MEMORY.md` May 3 session note expanded with post-mortem summary
