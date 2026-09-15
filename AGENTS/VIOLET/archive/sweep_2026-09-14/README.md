# VIOLET — VIX Agent

**Domain:** VIX, volatility term structure, implied volatility dynamics, vol-of-vol
**Role:** Early warning system for vol regime shifts. Credit-to-vol transmission specialist.

---

## Quick Reference (Directory Map)

| File | Purpose |
|------|---------|
| `STATUS.md` | Live VIX dashboard + convergence matrix (single source for live values) · **~250-line cap, boot-enforced** |
| `SCRATCH.md` | Session handoff **for VIOLET's own next boot** — CHANGES SINCE / WHAT I DID / NEXT SESSION |
| ~~`LAST_COMPLETION.md`~~ | ⛔ **FROZEN 2026-09-06 — historical record, not maintained.** The **PROME-facing** completion contract is now a **dated memo** at `PROME/inbox/{date}_from-VIOLET_{slug}.md` ending in the `## COMPLETION` block (`PROME/COMPLETION_SPEC.md`, ≤10 lines), plus the same block in the session response. Still **not a SCRATCH duplicate — different consumer** *(spec re-keyed 8/13, home fixed to `PROME/inbox/` 9/5; frozen here on Will's word 9/6)* |
| `NEXUS_BRIEF.md` | Cross-agent synthesis brief — NEXUS reads this in place of raw STATUS |
| `MEMORY.md` | Curated insights, regime principles, metric semantics, session-note trajectory |
| `MAINTENANCE.md` | Structural-change log (docs/scripts/protocol — why VIOLET is organized this way) · **~300-line cap, boot-enforced** |
| `CANARY_MAP.md` | Fleet early-warning layer — instrument → domain → threshold → route map (action-gates stay canonical in `PROME/GATES.tsv`) |
| `SIGNAL_INTAKE.md` | **WALTER subscription spec** — what to route to VIOLET, exclusions, and the durable threshold lines (each carrying **LEVEL + INSTRUMENT + WINDOW**, v3.8) |
| `TRADE.md` | VIX-linked positions, vehicles, sizing, live decision frameworks |
| `CALENDAR.md` | VIX expirations, FOMC/CPI/BOJ catalysts (human twin of `workbook/CATALYSTS.tsv`) |
| `CLAUDE.md` | Agent instructions — spawn protocol, write-back steps, scope, output rules |
| `board_log.tsv` | WALTER signal-intake ledger (`timestamp_read / signal_id / disposition / source / notes`) |
| `thesis/VIX_THESIS.md` | Core framework + L1 canonical base-rate table (current version: see file header) |
| `thesis/CHANGELOG.md` | Old view → new view at each thesis version bump + dated POV pivots |
| `workbook/` | **13 TSVs.** KB (findings, **schema-enforced at boot**) · VX_DAILY (daily surface) · VIX_OPTIONS · COT_VIX · CATALYSTS (machine feed) · FLOW (formal sends) · JPY_VOL · OVX · CHEAP_TAIL · **IMPLIED_CORR** (⚠️ *cannot be backfilled* — `^COR*` has no daily history, so it exists only if boot runs) · **VX_M1_HISTORY** · **VX_TERM_HISTORY** (28,555 contract-days, 2013→, free from CBOE's contract-keyed endpoint) · SCHEMA (the enum contract) · DIET_COILED_SPRING.csv (L1 backtest) |
| `scripts/` | **27 scripts. `boot.py` = the ~12s live boot, 11 stages:** thresholds+daily log · **FRED credit gate** · VIX options OI · CFTC COT · **JPY carry-vol canary** · **OVX oil-vol canary** · **cheap-tail window** · **implied correlation** · catalyst countdown · **CANARY_MAP staleness contract** · **KB schema conformance**. Guards/tests: `_daily_log.py` (shared upsert — canary ledgers UPDATE today's row and print `🔴 STATE CHANGED`; they used to freeze the day at its first read) · `test_daily_log.py` (43 tests) · `validate_workbook.py` · `canary_staleness.py`. Analysis: `backfill.py` (dated-row repair) · `convexity_read.py` · `convergence_score.py` · `regime_termination.py` · `diet_coiled_spring.py` · `two_anchor_ladder.py` · `skew_trajectory.py` · `h3_basis_lead.py` · `vx_history.py` · analog/feb2018/sustain-run tools |
| `research/` | Time-stamped deep dives (post-mortems, analogs, audits, packet specs). **Retirement is transitive** — a reference only counts if the referrer is neither the file itself nor also being retired; see `archive/retired_2026-07-30/README.md` |
| `reports/` | Periodic sweeps (domain / threads) |
| `artifacts/` | Will-facing living HTML Artifacts — `vol_cheatsheet`, `violet_operating_picture` (redeploy to the SAME URLs) |
| `inbox/` · `outbox/` | Inbound packets (+ `inbox/WALTER/` routed lane, both with `processed/`) · **`outbox/` now has a lifecycle too: top level = NOT YET DELIVERED, `outbox/delivered/` = confirmed consumed** (`outbox/README.md`). ⚠️ **Delivered ≠ actioned — an open ask lives in STATUS/NEXUS_BRIEF, never in an undelivered-looking file.** Outbound is 🔴-acute ONLY; NEXUS_BRIEF is the primary cross-agent surface |
| `archive/` | **Re-created 2026-07-30** (the dir had been deleted wholesale in the 2026-06 public-prep prune, `1cb18fbc`/`7133b7d6`). Holds `MAINTENANCE_ARCHIVE.md` (pre-6/11 structural entries) and `retired_2026-07-30/` (17 files, two sweeps — docs/templates AM, research corpus PM, each with its rationale in that dir's README). Docs retired *before* 7/30 are recoverable via git history only |

---

## Core Thesis (durable pillars — live version + state in `thesis/VIX_THESIS.md`)

**1. Credit leads, vol follows — when conditions are right.**
HY OAS leads VIX 2-6 weeks (tactical, +100bps trigger) and ~7 months (cycle) when: shock originates in credit · VIX < 20 at onset · cross-sector widening · yield curve not inverted · no active Fed QE. Relationship inverts above VIX 40. ⚠️ **The "~70% when all conditions met" figure is INHERITED from the v3.0 four-model synthesis and has never been VIOLET-validated** (flagged at v3.1 alongside the other inherited rates); it is not in the same evidentiary class as pillar 2's table below. Since v3.3 this is **Path A** — **Path B** (concentration-unwind) fires with *no* credit confirmation.

**2. SKEW divergence (SKEW rises while VIX+VVIX fall) is the highest-conviction leading signal.**
Threshold-indexed (L1 canonical table, KB-VIO-079): STRICT 94% / DIET 92% episode-level hit rate for ≥+15% VIX rise within 60 trading days — but only 56-60% at ≥+50%. **Quote the rate at the threshold the structure targets; never one unqualified number.**

**3. Term-structure inversion marks vol PEAKS, not onsets** (v3.1 falsification, KB-VIO-034: 2.2% hit rate as onset predictor). Exit-timing signal only.

---

## Cross-Agent Network

**Outbound:** `NEXUS_BRIEF.md` is the primary surface (refreshed every write-back); `outbox/` for 🔴-acute only. Vol-regime broadcast is VIOLET-owned (HENRY keeps gamma/0DTE/put-wall mechanics).
**Inbound:** routed by WALTER per `SIGNAL_INTAKE.md` (subscription spec — categories, exclusions, durable threshold lines).
**Core edges:** HENRY (market structure ↔ vol regime) · LIQUID (credit spreads → transmission) · RED (adversarial) · BROCK (private-credit stress in) · HAWK (geopolitical events in) · SAM (carry-unwind channel in) · BRENT (oil-vol transmission gauge).

---

*Created: 2026-04-12 · **Last refreshed: 2026-07-30 PM.** ⚠️ **This file got its first-ever provenance pass at ~11:00 the SAME DAY and was stale again by 16:30** — the audit was accurate when written, and then the same session's later work (4 new scripts, 3 new boot stages, 2 new ledgers, the `outbox/delivered/` lifecycle, a research retirement) invalidated it. **An audit is a point-in-time snapshot, not a property a file acquires**; a directory map has to be refreshed by whoever changes the directory, in the same commit, or it decays fastest immediately after being checked. PM pass corrected: script count 20 → **27**, boot "8 stages / ~17s" → **11 stages / ~12s**, three ledgers and four scripts that did not exist this morning, `outbox/` lifecycle, `archive/` contents.*

*Prior stamp: **2026-07-30 AM** — first full provenance pass. Directory map had drifted badly: **6 live surfaces were missing entirely** (`LAST_COMPLETION.md`, `CANARY_MAP.md`, `board_log.tsv`, `inbox/`, `reports/`, `artifacts/`), `archive/` was described as deleted **the same day it was re-created**, `boot.py` was described with 4 of its 8 stages, and the workbook/scripts lists were ~half complete. **Substantive catch: VIOLET's own `CLAUDE.md` had called `LAST_COMPLETION.md` "retired" since the 6/01 protocol rewrite while `PROME/COMPLETION_SPEC.md` mandates it fleet-wide and 17 agents keep one** — corrected, and added to the write-back sequence as step 11a. Pillar 1's inherited ~70% hit rate now carries its never-validated caveat. Prior: 2026-06-10 (root-md audit item 2).*
