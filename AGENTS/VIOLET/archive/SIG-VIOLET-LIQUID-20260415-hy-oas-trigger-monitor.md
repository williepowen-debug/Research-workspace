---
signal_id: SIG-VIOLET-LIQUID-20260415-hy-oas-trigger-monitor
precedence: PRIORITY
timestamp: 2026-04-15
source: VIOLET
origin: VIOLET HY OAS trajectory analysis (research/2026-04-15_hy_oas_trajectory.md) + SKEW divergence backtest (research/2026-04-15_skew_divergence_episodes.md)

to: LIQUID (ACTION)
info: HENRY, BROCK
group: CREDIT_CHAIN
dispatched: QUEUED (git path blocked — VIOLET outbox only)

signal_type: research-request
confidence: 0.85
confidence_language: likely
---

## Signal

VIOLET requesting daily HY OAS + IG OAS + CDX HY monitoring over next 14 days for tactical-trigger confirmation.

## Context

- HY OAS (BAMLH0A0HYM2) cycle trough: **2.64 on 2026-01-22**
- Widened to 3.46 peak Mar 30 (+82bps) alongside VIX 31.05 spike Mar 27
- Now re-compressed to **2.84 (Apr 14) — 20bps above trough, 62bps off peak**
- This compression is happening WHILE Apr 14 macro signals are escalating (IMF GFSR, TCW Red Lobster 98% writedown, HF short-cover whipsaw, PPI 4.0%)
- Credit-vol four-model synthesis says tactical trigger = 100bps widening from trough → 2-6wk VIX lead. Current is 20bps; threshold = HY OAS 3.64

## What VIOLET needs

1. Daily HY OAS read (we're pulling FRED; OK to deduplicate)
2. **IG OAS (BAMLC0A0CM) trajectory** — cross-sector widening filter per synthesis
3. **CDX HY bid/ask + positioning** — LIQUID-owned data we can't replicate
4. Flag if any **sector disaggregation** shows energy-only vs broad widening
5. LIQUID's current STATUS posture — 5 days stale at VIOLET boot

## Why

SKEW-VIX-VVIX divergence fired Apr 13 (episode #17, backtest library). 15 of 16 completed historical analogs produced ≥15% VIX rise within 60d; 9 of 16 ≥50%. If HY OAS starts widening again over next 14 days, we get tactical-trigger confirmation of a 2-6wk spike lead and Scenario B (new VIX event within 60d) moves from 66% base rate to 80%+.

## Cross-reference

- SIG-W-20260414-002 (TCW Red Lobster) — PC Stage 3 predecessor
- SIG-W-20260414-004 (IMF GFSR) — explicit liquidity-facilities warning
- SIG-W-20260414-006 (GS HF short cover whipsaw) — positioning trap mechanism

## VIOLET's bucketed paths

| Path | HY OAS trajectory | VIX implication |
|------|-------------------|-----------------|
| 1 — Credit-led re-widening | >3.20 within 2 weeks, then >3.64 | Tactical trigger, 2-6wk VIX spike lead; central 25-30, tail 40+ |
| 2 — Vol-led (Mar 27 replay) | Stays 2.80-3.20 | VIX spikes on catalyst (FOMC, earnings) without credit lead |
| 3 — Null / Scenario A | Drifts toward 2.70 and below | SKEW divergence false positive; VIX stays 15-18 |

*VIOLET 2026-04-15. Queued in outbox pending git path resolution.*
