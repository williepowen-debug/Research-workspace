# PROME STATUS.md
**Updated:** 2026-06-21 19:40 ET (OpenClaw Prome — post REITS/TRADES archive + ORACLE/TERRY tooling push)

## Core State

**Operational priority:** System cleanup lane completed for CREED/REITS/TRADES/TERRY/ORACLE. Future sessions should boot from the new ownership truth: CREED owns REIT equity tape, TERRY supersedes TRADES, ORACLE owns prediction-market diagnostics, and no auto-trading is allowed.

**Current repo reality:** ORACLE/TERRY/CREED cleanup commits were rebased over newer WALTER/SAM remote work and pushed cleanly. Pre-closeout state was clean/synced with origin.

**Market priority:** unchanged from `HEARTBEAT.md`: signed-but-fraying MOU; Hormuz re-closure declared; official/declaratory/contested, not yet kinetic. Energy tail is re-fat, broad cascade still unconfirmed. Refresh dashboard/FRED before citing fresh levels.

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
