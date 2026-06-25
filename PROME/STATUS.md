# PROME STATUS.md
**Updated:** 2026-06-25 ~13:10 ET (Claude Code Prome — Desktop CC; do-now batch + regime refresh + agent closeout)

## Core State

**Operational priority:** 6/25 Desktop-CC session ran a do-now batch (SAM/BROCK/HENRY/LIQUID, teams-mode) → full write-back → regime-surface refresh → agent closeout. Boot from the current regime via `PROME/SCRATCH.md` + `PROME/synthesis/2026-06-25_donow_reconciliation.md`. Prior ownership truth still holds: CREED owns REIT equity tape, TERRY supersedes TRADES, ORACLE owns prediction-market diagnostics; no auto-trading.

**Current repo reality:** Clean tree; this session's work committed locally (full 9-commit ledger in `PROME/SCRATCH.md`). Pushing stays Will-coordinated.

**Market priority:** per `HEARTBEAT.md` (6/25): energy tail **DEFLATED** (Brent ~$74, Hormuz resolved non-kinetic; Cushing sub-20M → BRENT Boundary #3); credit-bear **ARMED — pre-trigger/entry-gated** above the <260 kill (HY 271); bank-vs-PC divergence is **MACRO, not credit-substance**. Live bear-root watch = wrapper-leading + HY OAS >280 (both unfired). Refresh dashboard/FRED before citing levels.

**Standing constraint:** no agent domain edits unless scoped by Will. No trade execution. Pushing should stay Will-coordinated.

---

## Live Surfaces / Ownership

| Surface | Role | Current note |
|---|---|---|
| `AGENTS/CREED/` | National CRE / CMBS + public REIT equity tape | REITS tape absorbed; CREED remains explicit-permission Claude Code roster. |
| `AGENTS/CREED/research/REIT_EQUITY_TAPE_MODULE_2026-06-21.md` | REIT tape module | Public REIT tape trigger design; not fresh market data. |
| `AGENTS/REITS/` | Dormant source archive | Do not launch unless Will explicitly revives. |
| `AGENTS/TERRY/` | Trade construction | Now owns old TRADES verification playbook + risk scoring/calibration. |
| `AGENTS/TERRY/RISK_SCORING.md` | TERRY risk scoring | Edge, capped Kelly, Brier calibration, execution-block checklist. |
| `AGENTS/TRADES/` | Dormant source archive | Old candidate scratchpad; not live trade rail. |
| `AGENTS/ORACLE/PREDICTION_MARKET_METRICS.md` | Prediction-market diagnostics | Entropy, KL bits, entropy-collapse alerts, ORACLE→TERRY packet. |
| `WILL/share/claude-code-commands-reference-updated-2026-06-21.*` | User command reference | Updated: REITS/TRADES launch commands removed; path audit clean. |
| `HEARTBEAT.md` | Regime pointer | Weekend/Fri-close orientation only unless refreshed. |

---

## Current Work Queue

| Lane | Priority | Status / owner note |
|---|---:|---|
| Closeout live-state refresh | 🟡 current | Update Prome handoff/scratch/status/memory after pushed cleanup work. |
| Dormant-agent cleanup | ⚪ optional | Inspect before archiving; do not demote folders from vibes. |
| CREED first real work | 🟡 if requested | Monthly CMBS/special-servicing + REIT tape tracker design. |
| TERRY first live dry run | 🟡 if requested | Use risk scoring + snapshot/risk scripts; no execution. |
| ORACLE metrics implementation | ⚪ optional | Metrics doc exists; future script integration could compute entropy/KL from ODDS_LOG. |
| Jun22 Brent / Hormuz tape test | 🔴 next market lane | Refresh live data before citing current levels. |
| HY <260 / post-FOMC confirmation | 🔴 next market lane | Latest HEARTBEAT level stale/Fri-close orientation. |
| Position-state reconciliation | 🟠 pending | Broker/Will truth required. |

---

## Rules of Engagement

- **No auto-trading.** ORACLE measures; TERRY evaluates; Will approves.
- **No REITS/TRADES live launch** unless Will explicitly revives.
- **No CREED full migration** unless explicitly approved.
- **Do not move/delete legacy source archives** unless scoped.
- **Pathspec commits only;** never broad add/reset/stash/force-push.

---

## Next Best Action

After clear, fresh Prome should verify repo state and choose lane: market refresh for Jun22 gates, or continue dormant-agent cleanup only after inspecting actual files and value.
