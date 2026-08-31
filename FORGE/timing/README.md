> ⚠️ **FROZEN 2026-08-09 (FORGE audit M4, Will-approved batch): this corpus is dated research, not maintained — do not cite as current.** Root `CLAUDE.md` Key Directories row carries the FROZEN banner (landed; "pending" cleared 2026-08-30, WQ-137 pair-fix). Original README below.

# FORGE/timing/

Cross-agent timing research. Where are we in each transmission chain relative to historical analogs?

## Core Findings (Mar 30, 2026)

**Central estimate: acceleration phase May-July 2026, full cascade Q4 2026 (6-9 months).** Consensus "12-24 month slow bleed" is wrong because it ignores: CCC already at Dec '07 levels (ratio 2.96 unprecedented), no Fed cutting room, simultaneous oil shock, and historical ratio compression speed (45 trading days in closest analog).

**We are at Stage 3-4 of 6** in the Gorton panic framework. Three independent LLM analyses converge on this staging. Opacity in PC is WORSE than 2007 CDOs.

## Files

### Thesis (start here)
- `thesis/NARRATIVE.md` — **The thesis in plain language.** What we believe and why.
- `thesis/TIMELINE.md` — Phased framework (5 phases, falsifiable assumptions, position alignment)
- `thesis/PREDICTIONS.md` — 22 specific falsifiable calls with tracking grid
- `thesis/CHANGELOG.md` — Decision journal (every view change logged with evidence)
- `thesis/LECTURE.md` — Full thesis as narrative script (designed for text-to-speech)

### Status
- `STATUS.md` — Current state, monitoring dashboard, research inventory

### Analysis (evidence base)
- `CONVERGENCE_TIMELINE.md` — Master framework: analog mapping, convergence matrix, expiry implications
- `2007_OAS_OVERLAY.md` — Daily HY OAS comparison 2007 vs 2026 (FRED data, not estimates)
- `CCC_HY_RATIO_MULTI_EPISODE.md` — CCC/HY ratio across 4 stress episodes (2007, 2011, 2015, 2020)
- `FCIC_TIMELINE_2007.md` — 40+ dated events Jun '07 → Mar '08 with 2026 analog mapping
- `FED_INTERVENTION_CREDIT_RESPONSE.md` — Fed actions → credit spread response
- *(pending)* `ISSUANCE_FREEZE_ANALYSIS.md` — At what OAS does issuance freeze?

### External Research (LLM responses)
- `research/GORTON_FRAMEWORK_RESPONSE_{1,2,3}.md` — Gorton panic framework applied to PC (3 independent analyses)
- `research/FLOW_OF_FUNDS_RESPONSE_{1,2,3,4}.md` — Z.1 selling sequence (4 independent analyses)
- `research/LIBOR_OIS_EQUIVALENT_RESPONSE.md` + `LIBOR_OIS_RESPONSE_{1,2}.md` — Post-LIBOR counterparty risk
- `research/FABN_MARKET_RESPONSE.md` + `FABN_MARKET_RESPONSE_2.md` — $277B insurer wholesale funding
- `research/PE_INSURER_TRANSMISSION_RESPONSE.md` + `PE_INSURER_TRANSMISSION_RESPONSE_2_GEMINI.md` — Monoline analog speed
- `research/PE_INSURER_CROSS_CONTAMINATION_RESPONSE.md` — Bermuda Triangle circular exposure
- `research/ZOMBIE_LENDING_RESPONSE.md` — Japan analog, forcing function ranking

### Prompts (reusable)
- `prompts/` — 11 research prompts + split sub-prompts (Gorton, LIBOR-OIS, Flow of Funds, PE-insurer, FABN, dealer capacity, Norinchukin, OFR Brief, repo 2019, zombie lending, 2007 OAS overlay)

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
