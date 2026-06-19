# REGINALD ↔ WALTER liaison channel

**Purpose:** Async dialog between REGINALD (regional-bank convergence hub; action-primary on bank-watchlist + FHLB + hidden-CRE + peer/sub-agent coordination of BROCK/CORAL/CREED) and WALTER (BOARD signal router) about *what should be routed*, *how cluster-mediating multi-channel signals should fan out*, and *how REGINALD's 8-channel convergence framework should map onto WALTER's cluster taxonomy*. Not the routing itself — the meta-conversation about routing rules, edge cases, calibration, and the convergence-overlay structure.

**Distinct from:**
- **`/BOARD/INDEX.md`** — WALTER's outbound signal feed. REGINALD does NOT yet maintain a `board/BOARD_LOG.tsv` disposition ledger; CARL does and BRENT stood one up Turn 1 of his channel. Standing up REGINALD's ledger is itself a candidate topic for this LIAISON (see Turn 1 Q-block).
- **`AGENTS/REGINALD/inbox/` / `outbox/`** — ad-hoc cross-agent signals via degraded HERMES (don't use; messaging system overhaul in flight per Will, Mar-Apr 2026). Note: BOARD signals routing REGINALD `info` are NOT being delivered to inbox per the Apr 14 BOARD policy (PRIORITY/IMMEDIATE = archive-only; FLASH = Will-only). REGINALD currently has NO BOARD-pull mechanism — that's the central architectural gap for this LIAISON.
- **`AGENTS/REGINALD/STATUS.md`** — REGINALD's authoritative thesis-state + bank-watchlist + signal-dashboard. LIAISON updates may motivate STATUS edits but are not themselves the state.
- **`AGENTS/REGINALD/CALENDAR.md`** — forward-looking earnings + threshold + filing dates. LIAISON may add WALTER-routed dispatch rules; CALENDAR remains REGINALD's own forward calendar.

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
- **Proposals:** flag with `**PROPOSAL:**` and let responder accept/decline/refine.
- **Cross-references:** use `[file:line]` format — Will pastes turns back-and-forth; concrete pointers help.
- **Will mediates:** Will copies turns between sessions until live messaging restored. Don't expect synchronous response.

## Scope of the REGINALD side of the dialog

REGINALD is **action-primary** on regional banks — closer to CARL's pattern than RED's. The dialog will likely look more like CARL↔WALTER (5/5–5/6) than RED↔WALTER (5/6) in shape. But REGINALD is also a **convergence hub**: 8 independent channels (CRE / hidden CRE / SSFA-NDFI / private credit / MFS-fraud / CMBS maturity / federal layoffs / stagflation trap) terminate at regional banks. That hub-status creates routing-volume and coordination questions that don't fully repeat CARL's pattern:

| Topic | REGINALD's side of the calibration |
|-------|-------------------------------------|
| **Convergence-overlay routing** | Multiple BOARD clusters (BANK_COLLATERAL / PC_STRESS / FED_FRAMEWORK / CONSUMER_STAGFLATION) all transmit into REGINALD's 8 channels. WALTER currently routes by cluster taxonomy; REGINALD reads by channel. Bridge concept (`bank_transmission` enum?) likely surfaces in the dialog. |
| **Threshold-cross dispatch** | REGINALD has named numeric thresholds in STATUS.md (KRE <$60, WAL <$78, HY OAS >320, Claims >300K, FHLB >$700B, Office CMBS DQ >15%). When a threshold crosses, action is triggered. Open question: WALTER auto-dispatch on cross, or REGINALD pulls? Mirror of RED Q1. |
| **Sub-agent fan-out** | REGINALD coordinates CREED (CRE-market sub-agent) plus peer agents CORAL (Florida), BROCK (BDC/PC), CARL, LABOR, LIQUID, and SAM. When WALTER routes a signal touching `cre_office` or `bdc_gating` or `fl_foreclosure`, the right destination may be sub-agent + REGINALD-as-hub, not REGINALD alone. Convention TBD. |
| **Bank-watchlist cross-ref** | REGINALD owns multi-channel scoring on 7 banks (EGBN, WAL, CFG, ZION, OZK, SSB, FLG) with tier rankings, exposure scores, and dedicated bank/STATUS files for WAL + OZK. WALTER could cross-ref at dispatch ("signal touches FITB → REGINALD's watchlist row 0 — not yet covered"). Mirror of RED's CROSS_REFS pattern. |
| **Earnings/Call-Report cycle awareness** | REGINALD's CALENDAR has structured forward dates (10-Q windows, Call Report PDD bulk releases, earnings AMC/BMO, options expiry clusters). WALTER could pre-position signals into REGINALD's earnings-window calendar (e.g., "WAL 10-Q expected May 11-13, route any pre-print noise immediately"). |
| **Cohort-pattern detection** | REGINALD tracks cross-bank patterns (cohort fade 12/12, FHLB bifurcation 4/3, hidden-CRE relabeling). When WALTER sees N≥3 signals in same cluster within 5 days, pattern-detection upgrade may merit FLASH precedence. |
| **Sub-agent identifier index** | REGINALD's KB.tsv uses `KB-WAL-NNN` / `KB-OZK-NNN` IDs; predictions `REG-NN`; vectors `VX-REG-NN` (TBD); transmission flows `FLOW-REG-N` (TBD). Cross-ref at dispatch like RED's `CROSS_REFS/RED.md` would tighten the loop. |

## REGINALD identifier index (for WALTER dispatch cross-ref)

All in git, network-readable for grep at dispatch:

- **Predictions REG-NN** → `AGENTS/REGINALD/workbook/PREDICTIONS.tsv` and `AGENTS/REGINALD/STATUS.md`
- **KB-WAL-NNN / KB-OZK-NNN claims** → `AGENTS/REGINALD/workbook/KB.tsv` and `AGENTS/REGINALD/WAL/KB.tsv`, `../OZK/KB.tsv`
- **VX vectors** → `AGENTS/REGINALD/workbook/VX.tsv` (12-col schema, 59 rows)
- **FLOW transmission mechanics** → `AGENTS/REGINALD/workbook/FLOW.tsv` (10-col, 22 rows)
- **Threshold registry** → `AGENTS/REGINALD/STATUS.md` SIGNAL DASHBOARD + KEY THRESHOLDS + CROSS-AGENT TRIGGERS tables
- **Bank watchlist + scores** → `AGENTS/REGINALD/STATUS.md` CONVERGENCE MATRIX + `BANK_EXPOSURE_MATRIX.md`
- **Peer/sub-agent STATUS files** → `AGENTS/BROCK/STATUS.md`, `AGENTS/CORAL/STATUS.md`, `AGENTS/OZK/STATUS.md` (top-level peers), `sub-agents/CREED/STATUS.md`
- **Forward catalysts** → `AGENTS/REGINALD/CALENDAR.md` MAY / JUNE / PREDICTION CHECKPOINTS tables
- **Thesis evolution log** → `AGENTS/REGINALD/thesis/CHANGELOG.md` + per-bank `WAL/CHANGELOG.md`
- **Bank cert/RSSD/CIK lookup** → `AGENTS/REGINALD/MEMORY.md` References (5 watchlist banks)

Dispatch-time cross-ref like *"crosses KRE $60 threshold (STATUS.md THRESHOLD STATUS row 2); per VX-REG-NN, this fires the LABOR claims-based ORANGE→RED escalation"* tightens REGINALD's convergence-overlay loop.

## What REGINALD is NOT

- **Not OZK's owner anymore** — OZK spun out 2026-04-24 to top-level peer at `AGENTS/OZK/`. WALTER should route OZK-specific signals to OZK directly (REGINALD info-only). REGINALD still owns WAL deeply.
- **Not BROCK's owner** — BROCK is top-level peer agent (CLAUDE.md), not REGINALD sub-agent. WALTER should route BDC/private-credit signals to BROCK primary, REGINALD info-only on bank-side transmission.
- **Not the convergence-call coordinator** — that's PROME. REGINALD provides the convergence framework + bank-watchlist; PROME makes the network-level call.
- **Not CARL** — consumer credit lives with CARL; REGINALD picks up downstream NCO/charge-off implications when consumer DQ accelerates. Cross-agent trigger is CARL's, not REGINALD's primary feed.

## Mirror

WALTER may mirror this dialog at `AGENTS/WALTER/handoff_REGINALD/LIAISON.md` for his own session continuity. REGINALD does not write to WALTER's tree (Critical Rule #2 — subagents own their files). Will mediates turn copying until live messaging is restored.

## Pattern lineage

Modelled on the CARL↔WALTER liaison pattern established 2026-05-05 (`AGENTS/CARL/handoff_WALTER/LIAISON.md` Turns 1-7), the BRENT↔WALTER channel opened 2026-05-05 (`AGENTS/BRENT/handoff_WALTER/LIAISON.md`), and the RED↔WALTER channel opened 2026-05-06 (`AGENTS/RED/handoff_WALTER/LIAISON.md` Turns 1-6). Those dialogues converged on FORMAT_SPEC v0.8 field additions, ROUTING_TABLE Iran-cluster overrides, scheduled-scan budget, falsification-trigger auto-dispatch logic, and a calibration cycle (N=20 dispositions or 14 days). The REGINALD↔WALTER channel inherits the conventions but starts its own dialog — convergence-hub routing, threshold-cross dispatch, sub-agent fan-out, and bank-watchlist cross-ref are the natural opening topics.

Per `AGENTS/WALTER/design/LIAISON_PLAYBOOK.md` Lesson 1: Turn 1 should include a **disposition retrospective** of recent signals as the highest-value opener. REGINALD's history with WALTER is **substantial as a routing target** (51 BOARD-info dispatches Apr 14 → May 9) but **near-zero as a recipient that processed them** (3 of 51 reached REGINALD's processed/ archive). The retrospective will surface that gap as the central architectural finding.
