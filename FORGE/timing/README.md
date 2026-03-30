# FORGE/timing/

Cross-agent timing research. Where are we in each transmission chain relative to historical analogs?

## Core Findings (Mar 30, 2026)

**Central estimate: acceleration phase May-July 2026, full cascade Q4 2026 (6-9 months).** Consensus "12-24 month slow bleed" is wrong because it ignores: CCC already at Dec '07 levels (ratio 2.96 unprecedented), no Fed cutting room, simultaneous oil shock, and historical ratio compression speed (45 trading days in closest analog).

**We are at Stage 3-4 of 6** in the Gorton panic framework. Three independent LLM analyses converge on this staging. Opacity in PC is WORSE than 2007 CDOs.

## Files

### Analysis
- `CONVERGENCE_TIMELINE.md` — Master framework: analog mapping, convergence matrix, expiry implications
- `2007_OAS_OVERLAY.md` — Daily HY OAS comparison 2007 vs 2026 (FRED data, not estimates)
- `CCC_HY_RATIO_MULTI_EPISODE.md` — CCC/HY ratio across 4 stress episodes (2007, 2011, 2015, 2020)
- `FCIC_TIMELINE_2007.md` — 40+ dated events Jun '07 → Mar '08 with 2026 analog mapping
- `FED_INTERVENTION_CREDIT_RESPONSE.md` — Fed actions → credit spread response (partial, agent timed out)
- *(pending)* `ISSUANCE_FREEZE_ANALYSIS.md` — At what OAS does issuance freeze?

### External Research (LLM responses)
- `research/GORTON_FRAMEWORK_RESPONSE_1.md` — Gorton framework applied to PC (model 1)
- `research/GORTON_FRAMEWORK_RESPONSE_2.md` — Gorton framework applied to PC (model 2, w/ 48 citations)
- `research/GORTON_FRAMEWORK_RESPONSE_3.md` — Gorton framework applied to PC (model 3, Bermuda Triangle)

### Prompts (reusable)
- `prompts/2007_OAS_OVERLAY_PROMPT.md` — Original OAS overlay prompt (superseded by script)
- `prompts/GORTON_FRAMEWORK_PROMPT.md` — Gorton/opacity/cascade framework
- `prompts/LIBOR_OIS_EQUIVALENT_PROMPT.md` — What replaces LIBOR-OIS in 2026?
- `prompts/FLOW_OF_FUNDS_SELLING_PROMPT.md` — Who sells first? Z.1 selling sequence

### Scripts
- `scripts/oas_overlay_2007.py` — FRED data pull for HY/CCC OAS overlay

## Key Data Points (cross-reference)

| Indicator | Value | 2007 Equivalent | Source |
|-----------|-------|-----------------|--------|
| HY OAS | 342 | Jul 2, 2007 (~303) | FRED |
| CCC OAS | 1013 | Dec 2007 (~888) | FRED |
| CCC/HY ratio | 2.96 | Never exceeded 1.73 in 2007 | Calculated |
| PC default rate | 9.2% (2025, Fitch record) | — | Fitch |
| Distressed exchanges | 94% of defaults | — | DBRS |
| BCRED first loss | -0.4% Feb 2026 | — | Reuters |
| BDC NAV discount | 17% (CWBDC) | — | JPM |
| Software loans <80¢ | $25B record | — | Morningstar LSTA |
| PE-insurer assets | $700B | — | BIS/IMF |

## Usage

Come back to `CONVERGENCE_TIMELINE.md` when:
- Relief rallies test conviction (reminder: we expect them — 2007 had a 98bp/35-day compression)
- New data moves an analog marker forward or backward
- Expiries approach and roll decisions are needed
- BCRED quarterly NAV reports (the single most important PC data release)
