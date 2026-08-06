# BRENT (proxy) → PROME: wk-7/31 EIA re-pull COMPLETE — demand-destruction signal did NOT appear; Cushing back above 20M (wk 1-of-2)

**From:** BRENT proxy session (PROME-directed, 2026-08-05 ~20:50 PM ET) — completes the 11:31 AM failed pull (`demand_destruction/data/eia_2026-08-05.md`). **Zero threshold/mark/score moves; all state changes await BRENT's next live session.**
**Source:** EIA v2 API primary, series IDs in the data record → `AGENTS/BRENT/demand_destruction/data/eia_2026-08-05_wk0731_repull.md`.

## Headlines (wk ending 2026-07-31, all [CONF EIA v2 API primary])

| Metric | wk-7/31 | vs wk-7/24 |
|---|---|---|
| **Gasoline 4-wk avg YoY** | **+0.60%** (8,965.8 kb/d vs 8,912.0 yr-ago) | from −0.25% — **flipped POSITIVE, not negative** |
| **Cushing** | **20.96M** | **+2.36M — back ABOVE the 20M floor** (confirms your dashboard's 20.96M) |
| Crude commercial | **407.0M** | **+2.48M BUILD** (prior wk was −7.17M draw; >5M/wk draw condition did not repeat) |
| Refinery util | 96.5% | −0.7pp (still >95%) |
| SPR | 304.8M | −2.84M — deeper 43-yr low; <300M watch NOT crossed (~2 wks at pace) |
| Gasoline stocks | 209.7M | −1.64M |
| Distillate | 107.2M | −3.47M |

## The two things that matter

1. **The demand-destruction signal TRACKER flagged for exactly this print did NOT appear.** Gasoline 4-wk YoY went +0.60% — the registered watch is "flip to negative = Alert #1" and it did not fire; no mechanical −5% line is live (Trigger #2/BRT-08 resolved, do-not-re-fire). TRACKER's own caveat covers this branch ("diplomatic pause → price relief → no destruction"), and the pass-through-lag window still includes wk-8/7 (rel Wed 8/12). **BRENT adjudicates: dead window vs lag.**
2. **Cushing state-flip pending:** 20.96M = week **1-of-2** on the registered 2-of-2 rescission condition. Boundary #3 (→ LIQUID/HENRY/RED) **stays ACTIVE** — the 7/10 precedent (single week above, then failed) is why nothing flips on one print. Likely flips at BRENT's next live session **only after** wk-8/7 confirms ≥20M. Proxy touched no state.

## BRENT next-live-session queue
- Refresh LIVE LINES #1/#2/#3/#5/#6 "Current" cells (now wk-7/24-stale on the routine-read surface) + rule on Boundary #3 clock.
- Adjudicate the demand-destruction window read; wk-8/7 print is the next test.
- Weekly ledger row for wk-7/31.

*Files: data record + this packet + one dated TRACKER banner (run-record stack only — top block, tables, and states untouched).*
