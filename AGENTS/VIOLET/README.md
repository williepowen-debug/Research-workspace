# VIOLET — VIX Agent

**Domain:** VIX, volatility term structure, implied volatility dynamics, vol-of-vol
**Role:** Early warning system for vol regime shifts. Credit-to-vol transmission specialist.

---

## Quick Reference (Directory Map)

| File | Purpose |
|------|---------|
| `STATUS.md` | Live VIX dashboard + convergence matrix |
| `LAST_COMPLETION.md` | Handoff contract from prior session |
| `MEMORY.md` | Curated insights, regime principles, historical analogs, session notes |
| `SIGNAL_INTAKE.md` | Action playbook — inbound/outbound triggers + monitoring thresholds |
| `TRADE.md` | VIX-linked positions + framework |
| `CALENDAR.md` | VIX expirations, FOMC dates, forward catalysts |
| `CLAUDE.md` | Agent instructions (spawn protocol, scope, output rules) |
| `thesis/VIX_THESIS.md` | Core hypothesis + regime-dependent framework |
| `workbook/` | TSV data files (KB, VX_DAILY, VIX_OPTIONS, FLOW, fred_cache) |
| `scripts/` | boot.py, thresholds, fred_fetch, regime_termination, etc. |
| `research/` | Time-stamped deep dives (post-mortems, analogs, target distributions) |
| `outbox/` | Outbound signals to other agents + signal templates |
| `archive/` | Retired docs (cold-boot deliverables, etc.) |

---

## Core Thesis

**Credit leads, vol follows — when conditions are right.**
HY OAS leads VIX 2-6 weeks (tactical, +100bps trigger) and ~7 months (cycle, trough → peak) when:
1. Shock originates in credit
2. VIX < 20 at onset
3. Cross-sector widening
4. Yield curve not inverted
5. No active Fed QE

Hit rate ~70% when conditions met. Regime-dependent: relationship inverts above VIX 40.

**Secondary thesis:** SKEW divergence (SKEW rises while VIX+VVIX fall) is highest-conviction leading signal — 94% hit rate for ≥15% VIX rise within 60d (KB-VIO-036).

*Full framework: `thesis/VIX_THESIS.md`.*

---

## Cross-Agent Network

**Sends to:** HENRY (market structure), LIQUID (funding), RED (adversarial), WALTER (image/news intake)
**Receives from:** BROCK (private credit), HENRY (macro/gamma), HAWK (geopolitical), LIQUID (credit/funding), RED (scenarios)

*Specific triggers + priorities: `SIGNAL_INTAKE.md`.*

---

*Created: 2026-04-12 · Last refreshed: 2026-05-03*
