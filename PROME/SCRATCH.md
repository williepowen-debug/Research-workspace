# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-05-23 ~17:12 ET (OpenClaw Prome — execution-rails architecture pass)

## What Just Happened

Will redirected focus from domain research to **system architecture**, specifically the execution gap between research → approval → broker action → file updates. We built and indexed the execution-rails system, then promoted the existing 6/18 FORGE trigger set into Prome's live decision cockpit.

### Architecture created / updated

| File | State | Purpose |
|---|---|---|
| `PROME/EXECUTION_RAILS.md` | ✅ New | Canonical state vocabulary, rail standard, cluster rails, active-decision index rules, artifact taxonomy |
| `PROME/ACTIVE_DECISIONS.md` | ✅ New | Boot-readable cockpit of non-terminal decisions: state, owner, next, backstop, source |
| `PROME/DECISION_ARTIFACTS_INDEX.md` | ✅ New | Inventory/taxonomy of action cards, execution rails, decision memos, trigger sets, trade logs |
| `PROME/action-cards/TEMPLATE.md` | ✅ Updated | Compact `State/Owner/Next/Backstop/Default` header + Execution Rail + Verification sections |
| `PROME/DECISION_FLOW.md` | ✅ Updated | Five layers → six layers; added Action Card / Execution Rail + Decision State Tracking |
| `PROME/TRADE_DECISIONS.md` | ✅ Updated | Decision-state and next-owner/verification fields added |
| `PROME/BOOT.md` | ✅ Updated | `ACTIVE_DECISIONS.md` added to doc ownership + boot sequence |
| `PROME/STATUS.md` | ✅ Updated | This architecture pass stamped into Prome state |

### Live decision promotions

| Decision | State | Source | Next |
|---|---|---|---|
| TLT Jun18 $85P ×3 2/1 roll | `BROKER_PENDING` | `PROME/action-cards/TLT_JUN18_DECISION_2026-05-22.md` | Tue 5/27 open broker execution if invalidation has not fired; Will sends fills; Prome updates files |
| 6/18 theta-killer cluster | `DRAFT` | `PROME/action-cards/JUN18_EXPIRY_CLUSTER_2026.md` + `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md` | BROCK/REGINALD calibration/default-pass by 2026-05-24 EOD → v0.2 Will approval packet |

## Design Decisions

1. **Agents keep native memos.** Prome does not force BROCK/REGINALD/etc. into the Prome template. Prome promotes their work into standardized rails only when action/state/default matters.
2. **Source files remain source-of-truth.** For 6/18, `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md` owns detailed R1-R4 and line-specific logic; Prome wrapper owns operational state.
3. **`WILL_APPROVED` is not complete.** `BROKER_PENDING` is now a first-class risk state.
4. **No trigger = default.** For theta-killer positions, default is explicitly let-expire unless a pre-registered trigger fires.
5. **`ACTIVE_DECISIONS.md` comes before new research at boot.** It is the cockpit for unfinished decisions.

## Current Git / Dirty Tree Notes

Architecture changes are Prome-scope and intentionally uncommitted pending user direction. Existing unrelated dirty files from fleet-scan subagent remain present:

- `AGENTS/PROME/LAST_COMPLETION.md`
- `PROME/FLEET_SCAN.md`

Do not conflate those with the execution-rails pass when reviewing/staging.

## Immediate Next Actions

1. 🔴 **Tue 5/27 open — TLT broker action**
   - State: `BROKER_PENDING`.
   - Will places: sell-to-close 3 × TLT Jun18 $85P; buy-to-open 1 × TLT Sep19 $85P, unless invalidation fires.
   - Prome needs fill prices/confirmation to update `FORGE/STATUS.md`, `TRADE_DECISIONS.md`, action card, and `ACTIVE_DECISIONS.md`.

2. 🟠 **Sun 5/24 EOD — 6/18 calibration/default-pass**
   - Check BROCK + REGINALD outboxes / relevant files for calibration replies.
   - If no replies, apply default-pass and move `JUN18_EXPIRY_CLUSTER_2026.md` from `DRAFT` → `PROPOSED`.
   - Present Will approval packet: adopt rail v0.2; no trigger = let expire; trigger = named review/roll; hard backstop 6/16 close.

3. 🟡 **HAWK May 23 close re-check still outstanding**
   - If no Gulf/framework text, update HAWK status/calendar language to hold expired without framework; May 25–29 grind/re-ratchet pressure active.

4. 🟡 **State-file hygiene later**
   - `TODAY.md` stale May 17.
   - `HEARTBEAT.md` levels still May 21; only architecture pointer may need surgical update later.

## Cautions

- Do not trade without Will approval.
- Do not spawn persistent agents: CARL, REGINALD, OZK, SAM, RED, BRENT, Claude Code Prome.
- Do not stash/commit other agents' dirty files.
- If staging, use explicit paths only; never `git add .` / `git add -A`.
