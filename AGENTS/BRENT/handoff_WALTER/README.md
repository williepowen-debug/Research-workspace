# BRENT ↔ WALTER liaison channel

**Purpose:** Async dialog between BRENT (oil/energy domain) and WALTER (BOARD signal router) about *what should be routed*, *how it should be tagged*, and *where the cross-cluster interpretation sits*. Not the routing itself — the meta-conversation about routing rules, edge cases, calibration, and cluster-mediating signals.

**Distinct from:**
- **`/BOARD/INDEX.md`** — WALTER's outbound signal feed. (BRENT does NOT yet maintain a `board/BOARD_LOG.tsv` disposition ledger; CARL does. Standing up that infrastructure is itself a candidate topic for this LIAISON.)
- **`AGENTS/BRENT/inbox/` / `outbox/`** — ad-hoc cross-agent signals via degraded HERMES (don't use; messaging system overhaul in flight)
- **`AGENTS/BRENT/STATUS.md`** — BRENT's authoritative thesis state. LIAISON updates may motivate STATUS edits but are not themselves the state.

## Files

| File | Purpose |
|------|---------|
| `README.md` | This file — channel conventions |
| `LIAISON.md` | Active turn-by-turn dialog. Append-only. Each turn marked `## Turn N — AGENT — YYYY-MM-DD HH:MM UTC` |

## Conventions

- **Turn marker:** `## Turn N — AGENT — timestamp`. Increment N globally (not per-agent).
- **Self-contained turns:** each turn should be readable on its own; don't assume reader has scrolled up.
- **Open questions:** flag with `**Q:**` so the responder can answer point-by-point.
- **Decisions:** flag with `**DECISION:**` and reference the turn that proposed it.
- **Cross-references:** use `[file:line]` format — Will pastes turns back-and-forth, so concrete pointers help.
- **Will mediates:** Will copies turns between sessions until live messaging restored. Don't expect synchronous response.

## Scope of the BRENT side of the dialog

BRENT is the **action-primary** agent for energy data substance: oil price/structure, OPEC+, tankers, refining, energy credit cross-feed, and the two-phase oil thesis (Phase 1 squeeze → Phase 2 demand-destruction/unwind). On the BRENT↔WALTER channel, expect calibration on:

| Topic | BRENT's side of the calibration |
|-------|---------------------------------|
| **Energy-cluster routing rules** | What energy-substance signals BRENT wants primary vs info; what HAWK-domain (kinetic/military) signals BRENT needs vs can drop |
| **Tape-vs-substance interpretation** | BRENT owns oil tape — when WALTER tags a signal `cluster_mediating` for tape divergence, BRENT is the data-primary recipient |
| **Cross-feed transmission tagging** | BRENT feeds CARL (pump pass-through), HENRY (inflation), LIQUID (energy credit), SAM (Japan LNG). Tagging the transmission mechanism at dispatch tightens BRENT's batch-fold |
| **Two-phase thesis triggers** | Path A (Phase 2 reopening) verification gates and Path B (demand destruction) EIA triggers — when does WALTER auto-dispatch a threshold-cross signal to BRENT? |
| **Boundary-threshold dispatches** | Brent close ≥$120 / sustained ≤$75 / Cushing <20M / HY Energy OAS >400bps / VLCC WS >200 — IMMEDIATE-precedence dispatches |
| **Workbook hardening cross-refs** | BRT-NN predictions, KB-BRT-NNN claims, VX-BRT-NN indicators — dispatch_note cross-refs let BRENT fold straight to the right vector |
| **Cluster-narrative authority** | Per CARL↔WALTER Turn 4: NEXUS > WALTER > action-primary for cluster-narrative. BRENT is action-primary on energy substance; defers to NEXUS on cluster narrative when a mediating signal hits |

## BRENT identifier index (for WALTER dispatch cross-ref)

All in git, network-readable for grep at dispatch:

- **Predictions BRT-NN** → `AGENTS/BRENT/workbook/PREDICTIONS.tsv` and `AGENTS/BRENT/thesis/THESIS.md`
- **KB-BRT-NNN claims** → `AGENTS/BRENT/workbook/KB.tsv`
- **VX-BRT-NN indicators** → `AGENTS/BRENT/workbook/VX.tsv`
- **FLOW-BRT-N.NN transmission** → `AGENTS/BRENT/workbook/FLOW.tsv`
- **CATALYSTS** → `AGENTS/BRENT/workbook/CATALYSTS.tsv`
- **SCHEMA** → `AGENTS/BRENT/workbook/SCHEMA.tsv`
- **Thesis state** → `AGENTS/BRENT/thesis/THESIS.md` (version string in first line)
- **Convergence matrix** → `AGENTS/BRENT/STATUS.md` (mirror; canonical version in THESIS.md)

Dispatch-time cross-ref like *"transmits to BRENT Vector #X (KB-BRT-NNN); folds to BRT-NN reprice"* tightens BRENT's disposition loop.

## Mirror

WALTER may mirror this dialog at `AGENTS/WALTER/handoff_BRENT/LIAISON.md` for his own session continuity. BRENT does not write to WALTER's tree (Critical Rule #2 — subagents own their files). Will mediates turn copying until live messaging is restored.

## Pattern lineage

Modelled on the CARL↔WALTER liaison pattern established 2026-05-05 (`AGENTS/CARL/handoff_WALTER/LIAISON.md` Turns 1-7). That dialog converged on FORMAT_SPEC v0.8 field additions, ROUTING_TABLE Iran-cluster overrides, scheduled-scan budget, and a calibration cycle (N=20 dispositions or 14 days). The BRENT↔WALTER channel inherits the conventions but starts its own dialog — energy-cluster routing and tape-vs-substance interpretation are the natural opening topics.
