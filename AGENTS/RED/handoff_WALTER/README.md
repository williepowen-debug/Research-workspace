# RED ↔ WALTER liaison channel

**Purpose:** Async dialog between RED (adversarial / thesis-stress-tester) and WALTER (BOARD signal router) about *what should be routed*, *how falsification triggers should fire*, and *where unanimity-risk and cross-cluster contradictions sit*. Not the routing itself — the meta-conversation about routing rules, edge cases, calibration, and the adversarial overlay.

**Distinct from:**
- **`/BOARD/INDEX.md`** — WALTER's outbound signal feed. RED does NOT yet maintain a `board/BOARD_LOG.tsv` disposition ledger; CARL does and BRENT stood one up Turn 1 of his channel. Standing up RED's ledger is itself a candidate topic for this LIAISON.
- **`AGENTS/RED/inbox/` / `outbox/`** — ad-hoc cross-agent signals via degraded HERMES (don't use; messaging system overhaul in flight per Will, Mar-Apr 2026).
- **`AGENTS/RED/STATUS.md`** — RED's authoritative thesis-stress state. LIAISON updates may motivate STATUS edits but are not themselves the state.
- **`AGENTS/RED/OUTBOX.md`** — formal RED challenges and PROME-bound reports. LIAISON is calibration-of-routing; OUTBOX is the dispatch surface.

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

## Scope of the RED side of the dialog

RED is **not action-primary on any domain data** — the network's adversarial overlay reads what others produce and stress-tests it. That makes the RED↔WALTER channel different from CARL↔WALTER and BRENT↔WALTER in ways worth flagging:

| Topic | RED's side of the calibration |
|-------|-------------------------------|
| **Falsification-trigger registry** | RED maintains the canonical list of thesis-falsification thresholds (`STATUS.md` FALSIFICATION CRITERIA section). When a threshold crosses, **all action-primary agents AND RED** need to know IMMEDIATELY. Open question: does WALTER auto-dispatch threshold crosses, or does RED need to publish a registry WALTER pulls from? |
| **Unanimity-risk detection** | RED's #1 blind-spot trigger is network unanimity — when all agents converge on the same call, RED's job is to find what they're all missing. WALTER sees the whole network at signal-dispatch time → strongest position to flag "9/9 RED" or "all clusters bear-confirming" patterns. Calibration on what counts. |
| **Cross-cluster contradiction tags** | Cluster-mediating signals (per CARL Turn 1, BRENT Turn 1) are RED's bread and butter — when one agent's bull signal contradicts another's bear thesis, RED steelmans the disagreement. Want explicit tagging at dispatch. |
| **Counter-signal weighting** | RED's `VX.tsv` is the network's standing counter-evidence registry with explicit bull/bear weights. WALTER could cross-ref VX-RED-NN at dispatch to flag whether a routed signal has an existing adversarial frame. |
| **Formal challenge routing** | RED issues formal challenges via OUTBOX (CHG-RED-NNN). Recent: CHG-RED-024 to BRENT (May 6). Open question: does WALTER help dispatch challenges as `formal_challenge` precedence, or stay out of OUTBOX? |
| **Resolved-prediction calibration** | RED's published predictions (RED-NN) have a public scoring record (4 WRONG / 1 CORRECT / 9 ACTIVE as of May 6). When a prediction resolves, the score affects RED's credibility on related challenges. WALTER may want a tag for "RED-NN-resolved" signals so other agents can recalibrate adversarial weight. |
| **Adversarial-overlay tape** | RED reads tape independently of action-primary agents to flag when paper markets disagree with structural signals (paper-vs-structural bifurcation; current state). Open question: should RED be cc'd on `cluster_mediating` tape-vs-substance signals as a structural matter, even when not action-primary? |

## RED identifier index (for WALTER dispatch cross-ref)

All in git, network-readable for grep at dispatch:

- **Predictions RED-NN** → `AGENTS/RED/thesis/PREDICTIONS.tsv` and `AGENTS/RED/STATUS.md`
- **KB-RED-NNN claims** → `AGENTS/RED/workbook/KB.tsv`
- **VX-RED-NN counter-evidence vectors** → `AGENTS/RED/workbook/VX.tsv`
- **CHG-RED-NNN formal challenges** → `AGENTS/RED/workbook/CHALLENGES.tsv`
- **FLOW-RED-N transmission-break pathways** → `AGENTS/RED/workbook/FLOW.tsv`
- **ML-RED-NNN findings audit trail** → `AGENTS/RED/workbook/ML.tsv`
- **SCHEMA** → `AGENTS/RED/workbook/SCHEMA.tsv`
- **Falsification triggers** → `AGENTS/RED/STATUS.md` "FALSIFICATION CRITERIA" table (≤200 line discipline) and `CALENDAR.md` "FALSIFICATION WATCH"
- **Competing hypotheses + probabilities** → `AGENTS/RED/STATUS.md` "COMPETING HYPOTHESES"
- **Bull-case steelman** → `AGENTS/RED/STATUS.md` "BULL CASE STEELMAN" section (refreshed each session)
- **Thesis evolution log** → `AGENTS/RED/thesis/CHANGELOG.md`

Dispatch-time cross-ref like *"crosses falsification threshold (STATUS.md FALSIFICATION CRITERIA row 3); per VX-RED-NN, prior bull-leaning weight 60/40 → review"* tightens RED's adversarial-overlay loop.

## What RED is NOT

- **Not action-primary** on any domain. RED reads CARL, REGINALD, BRENT, LIQUID, HAWK, etc. and challenges. Routing-volume to RED should be cluster-mediating signals + falsification-trigger crosses + unanimity-detection events, **not** raw domain primary data (RED has no thesis to update from a JOLTS print directly — REGINALD/CARL do).
- **Not a domain-data producer.** RED has no primary feed. Anything RED publishes derives from other agents' work + adversarial framework. Counter-evidence in VX.tsv is sourced from network observations, not RED-original research.
- **Not the network's coordinator.** PROME is. RED reports to PROME via OUTBOX; doesn't replace PROME's routing role.

## Mirror

WALTER may mirror this dialog at `AGENTS/WALTER/handoff_RED/LIAISON.md` for his own session continuity. RED does not write to WALTER's tree (Critical Rule #2 — subagents own their files). Will mediates turn copying until live messaging is restored.

## Pattern lineage

Modelled on the CARL↔WALTER liaison pattern established 2026-05-05 (`AGENTS/CARL/handoff_WALTER/LIAISON.md` Turns 1-7) and the BRENT↔WALTER channel opened 2026-05-05 (`AGENTS/BRENT/handoff_WALTER/LIAISON.md`). Those dialogues converged on FORMAT_SPEC v0.8 field additions, ROUTING_TABLE Iran-cluster overrides, scheduled-scan budget, and a calibration cycle (N=20 dispositions or 14 days). The RED↔WALTER channel inherits the conventions but starts its own dialog — falsification-trigger dispatch rules, unanimity-detection tagging, and cross-cluster contradiction surfacing are the natural opening topics.

Per `AGENTS/WALTER/design/LIAISON_PLAYBOOK.md`: Turn 1 should include a **disposition retrospective** of recent signals as the highest-value opener. RED's history with WALTER is light (RED has been a downstream recipient of one falsification-derived alert, SIG-W-20260411-001-red-falsification-hy-oas-pierced, and a subject of multiple `verify-research` references); the retrospective will be smaller than CARL's 12-signal pass but should still anchor the calibration.
