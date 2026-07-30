# HY OAS Trajectory — Tactical Trigger Check

**Source:** FRED BAMLH0A0HYM2 (ICE BofA US High Yield Index OAS), fetched 2026-04-15
**Purpose:** Evaluate credit-to-vol tactical trigger (100bps widening from recent low → 2-6 week VIX spike lead per four-model synthesis) and calibrate current setup against SKEW divergence thesis.

## Cycle map (Oct 2025 → today)

| Phase | Date | HY OAS | Notes |
|-------|------|-------:|-------|
| **Trough** | **2026-01-22** | **2.64** | Cycle low — same date as 2025-01-22 analog episode (KB-VIO-036 #14) |
| Pre-stress widening | 2026-03-04 | 2.97 | +33bps from trough over 6 weeks |
| Pre-peak acceleration | 2026-03-13 | 3.28 | +64bps from trough, VIX already rising |
| **VIX peak day** | **2026-03-27** | **3.42** | +78bps from trough. Jump +21bps in one day |
| **HY OAS peak** | **2026-03-30** | **3.46** | +82bps from trough, 3 days after VIX peak |
| Compression | 2026-04-08 | ~3.0 | (needs verify — approximate from trajectory) |
| **Current** | **2026-04-14** | **2.84** | **20bps above trough, 62bps off cycle peak** |

Cycle widening: **+82bps peak-to-trough** — did NOT hit the 100bps tactical trigger.

## Did the tactical trigger fire around Mar 27? No.

Per four-model synthesis (KB-VIO-026), the tactical trigger is:
- HY OAS widens **≥100bps from recent low**
- VIX at onset **15-26** (sweet spot)
- Cross-sector widening (not just energy)
- Yield curve not inverted
- No Fed QE backstop

Mar 27 cycle hit 82bps (short of 100bps threshold), but VIX spiked anyway on a multi-domain convergence unrelated to credit (see postmortem). **This confirms thesis v3.1 regime-dependence:** in macro-geopolitical-led events, VIX can spike without credit completing the full 100bps precondition.

## Current setup vs Jan 22 trough

- **82 days since cycle trough** — well within the 3-8 week lead window for low-vol regime
- Credit COMPRESSED through the post-spike period (3.46 → 2.84 = -62bps in 2 weeks) even as macro stress accelerated (Apr 14 signal flood)
- This is *unusual* — normally credit is stickier on the widening than it is on the compression; asymmetry suggests liquidity-driven buying (CTA, vol-controlled, pension rebalance) absent fresh stress

## Three paths from here

**Path 1 — Credit-led re-widening (tactical trigger activation):**
HY OAS widens back through 3.0 → 3.2 → 3.64 (100bps from trough 2.64). If this happens in the next 2-4 weeks, it activates the full 2-6 week lead signal for a VIX spike, and matches the SKEW divergence fire on Apr 13 perfectly (credit following, vol market anticipating). Highest-probability path given macro signal escalation.

**Path 2 — Vol-led spike (Mar 27 replay):**
VIX spikes on FOMC/earnings without credit completing the widening move, same as Mar 27. Apr 14 signal stack is denser than Mar 26, so a repeat is structurally plausible. Central case 25-30; tail 40+.

**Path 3 — Null — credit stays tight, vol compresses:**
HY OAS drifts back toward cycle trough, SKEW rolls through 140, VIX settles 15-18. This is Scenario A from KB-VIO-031 (22% probability post-revision). Would imply Apr 13 divergence was a false positive.

## What we're watching (daily, next 4 weeks)

| Signal | Threshold | Path it validates |
|--------|-----------|-------------------|
| HY OAS > 3.20 | Widening resumed | Path 1 forming |
| HY OAS > 3.64 | Tactical trigger fires | Path 1 confirmed, expect 2-6wk VIX spike lead |
| HY OAS < 2.70 | Near-trough revisit | Path 3 gaining |
| HY OAS stays 2.80-3.00 | Drift | Macro-led Path 2 still dominant |
| VIX > 22 with HY < 3.0 | Vol-led rise | Path 2 |
| SKEW > 155 with HY stable | Vol market pricing ahead | Strengthens Path 2 |

## Cross-signal integration

The HY OAS compression while macro signals escalate (Apr 14) is the single most important signal to watch. Two possibilities:
1. Credit is **late** (lag regime) — Path 1 imminent once Apr 16 / 21 / 29 catalysts hit
2. Credit is **right** — the Apr 14 signals don't threaten credit fundamentals (possible if IMF warning is academic, Red Lobster is single-issuer, positioning whipsaw is technical)

**My read:** #1 more likely than #2. The concentration of IMMEDIATE signals across private credit, positioning, and policy channels (3 separate transmission routes) is harder to dismiss than any single one.

## Signal to LIQUID (queued in outbox, not delivered)

**Request:** Daily HY OAS read + IG OAS + CDX HY bid/ask over next 14 days. Tactical trigger monitor at 3.64. Flag if cross-sector widening (not just energy) starts.

*VIOLET 2026-04-15. Source: FRED BAMLH0A0HYM2, two pulls (2025-10-01 base + 2026-03-01 detail).*
