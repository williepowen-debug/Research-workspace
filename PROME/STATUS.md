# PROME STATUS.md
**Updated:** 2026-06-26 ~13:05 ET (Claude Code Prome — detection/action hardening cluster + arch peer-review + closeout; pushed synced 0/0)

## Core State

**Operational priority:** 6/26 session ran the detection/action HARDENING cluster (LIQUID/SENTRY/TERRY, Prome-directed) + a 3-way arch peer-review + fix round. **Standing rule (Will 6/26): deploy fresh capital ONLY on a fired trigger; $500/card.** Boot from `PROME/SCRATCH.md`. Key new machinery: a LIVE `liquid-hy-watch` systemd timer auto-catches an HY>280 cross between sessions; `grade_print.py`/`chain_fetch.py`/fire-card template are the trigger→card toolchain. Prior ownership truth holds: CREED owns REIT equity tape, TERRY supersedes TRADES, ORACLE owns prediction-market diagnostics; no auto-trading.

**Current repo reality:** Pushed — local+origin synced 0/0 at `3d4afafa` (9 commits this session). Only WILL/trading-journal working-tree changes remain (3 intentional deletions + 2 book JPGs — Will's, left untouched).

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
| Detection/action hardening | ✅ done 6/26 | config retune + live HY watch timer + trigger→card toolchain + grade_print; verified, pushed. |
| Bank-put reshape card | 🟡 shelved | `PROME/proposals/2026-06-26_bank-put-reshape-roll.md`; fires ONLY on HY>280 sustained / WAL Jul-16 print. $500/card. Needs live broker book at fire-time. |
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

After clear, fresh Prome should check `AGENTS/LIQUID/alerts/HY_OAS_ALERTS.log` for any between-session HY transition (the watch timer runs daily 13:00 ET). Live regime: HY 278 [6/25], 2bp from the >280 X1 — watched automatically now. No action unless a trigger fires; then the shelved $500/card reshape is the ready response (needs live broker book).
