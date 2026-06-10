# VIOLET — VIX Agent

**Domain:** VIX, volatility term structure, implied volatility dynamics, vol-of-vol
**Role:** Early warning system for vol regime shifts. Credit-to-vol transmission specialist.

---

## Quick Reference (Directory Map)

| File | Purpose |
|------|---------|
| `STATUS.md` | Live VIX dashboard + convergence matrix (single source for live values) |
| `SCRATCH.md` | Canonical session handoff — CHANGES SINCE / WHAT I DID / NEXT SESSION |
| `NEXUS_BRIEF.md` | Cross-agent synthesis brief — NEXUS reads this in place of raw STATUS |
| `MEMORY.md` | Curated insights, regime principles, metric semantics, session-note trajectory |
| `MAINTENANCE.md` | Structural-change log (docs/scripts/protocol — why VIOLET is organized this way) |
| `SIGNAL_INTAKE.md` | **WALTER subscription spec** — what to route to VIOLET, exclusions, durable threshold lines |
| `TRADE.md` | VIX-linked positions, vehicles, sizing, live decision frameworks |
| `CALENDAR.md` | VIX expirations, FOMC/CPI/BOJ catalysts (human twin of `workbook/CATALYSTS.tsv`) |
| `CLAUDE.md` | Agent instructions — spawn protocol, write-back steps, scope, output rules |
| `thesis/VIX_THESIS.md` | Core framework + L1 canonical base-rate table (current version: see file header) |
| `thesis/CHANGELOG.md` | Old view → new view at each thesis version bump + dated POV pivots |
| `workbook/` | TSVs: KB (findings), VX_DAILY (daily surface), VIX_OPTIONS, COT_VIX, CATALYSTS (machine feed), FLOW |
| `scripts/` | `boot.py` (~10s live boot: thresholds + options OI + COT + catalyst countdown), `convexity_read.py`, fred_fetch, backfill, etc. |
| `research/` | Time-stamped deep dives (post-mortems, analogs, audits, packet specs) |
| `outbox/` | 🔴-acute outbound signals ONLY (NEXUS_BRIEF is the primary cross-agent surface) |
| `archive/` | Retired docs (incl. pre-template SIGNAL_INTAKE, cold-boot deliverables) |

---

## Core Thesis (durable pillars — live version + state in `thesis/VIX_THESIS.md`)

**1. Credit leads, vol follows — when conditions are right.**
HY OAS leads VIX 2-6 weeks (tactical, +100bps trigger) and ~7 months (cycle) when: shock originates in credit · VIX < 20 at onset · cross-sector widening · yield curve not inverted · no active Fed QE. Hit rate ~70% when all conditions met. Relationship inverts above VIX 40.

**2. SKEW divergence (SKEW rises while VIX+VVIX fall) is the highest-conviction leading signal.**
Threshold-indexed (L1 canonical table, KB-VIO-079): STRICT 94% / DIET 92% episode-level hit rate for ≥+15% VIX rise within 60 trading days — but only 56-60% at ≥+50%. **Quote the rate at the threshold the structure targets; never one unqualified number.**

**3. Term-structure inversion marks vol PEAKS, not onsets** (v3.1 falsification, KB-VIO-034: 2.2% hit rate as onset predictor). Exit-timing signal only.

---

## Cross-Agent Network

**Outbound:** `NEXUS_BRIEF.md` is the primary surface (refreshed every write-back); `outbox/` for 🔴-acute only. Vol-regime broadcast is VIOLET-owned (HENRY keeps gamma/0DTE/put-wall mechanics).
**Inbound:** routed by WALTER per `SIGNAL_INTAKE.md` (subscription spec — categories, exclusions, durable threshold lines).
**Core edges:** HENRY (market structure ↔ vol regime) · LIQUID (credit spreads → transmission) · RED (adversarial) · BROCK (private-credit stress in) · HAWK (geopolitical events in) · SAM (carry-unwind channel in) · BRENT (oil-vol transmission gauge).

---

*Created: 2026-04-12 · Last refreshed: 2026-06-10 (root-md audit item 2: retired-file pointer removed, map completed, base rates re-pointed at KB-VIO-079 canonical table, network section aligned to NEXUS_BRIEF/WALTER-subscription surfaces)*
