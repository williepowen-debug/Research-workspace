# TODAY.md — Saturday June 27, 2026
**Updated:** 2026-06-27 PM (Claude Code Prome — Sat network day. AM: roster refresh + auto-push sweep. PM: **fleet protocol audit → Lanes 1+2+3** + **coverage-gap analysis → 3 mandate-extension SIGs**. Weekend; levels are 6/25 Fri-close orientation. NEXUS live PM (executing Lane-3); ORACLE/TERRY/WALTER live AM. Pushed via safe-push at closeout.)

**Objective:** "Improve + fill out the network" day — no new market position. AM: roster + auto-push. PM: fleet protocol standardization (Lanes 1-3) + a coverage-gap analysis that verified the network is well-covered (no new agent) and routed funding-plumbing + secondary mandate extensions. **No trigger fired** (standing rule held).

---

## Session Posture
| Item | State |
|---|---|
| Origin | Desktop Claude Code (Prome live surface). |
| Git | All PROME work committed + pushed via the train (ORACLE's mid-session safe-push + closeout safe-push). Only `WILL/` working-tree changes remain (Will's). |
| Agents | ORACLE/TERRY/WALTER live in separate windows this session — self-managing; **not** warm-parked for next Prome. |
| Push rule | ♻️ AUTO-PUSH at closeout via `scripts/safe-push.sh` (ff-gated, single-machine). Non-ff abort = 2nd machine → flag Will. |

## Regime (one-line) — weekend, 6/25 Fri-close orientation
Energy deflated; credit-bear **ARMED, pre-trigger**; **HY OAS 278 [6/25]** — 2bp from the >280 X1-trigger (NOT fired); bank-vs-PC divergence still MACRO. Independent confirmation gated on **HY>280 + wrapper-leading** (both unfired). HY auto-watched between sessions (`liquid-hy-watch`). **Refresh dashboard/FRED before citing any level as live.**

## Standing rule (Will 6/26)
**Deploy fresh capital ONLY on a fired trigger; $500/card max-loss.** No mechanical book-reshape. ([[feedback_deploy_on_trigger_not_calendar]])

## Prome-owned, done today (6/27)
**AM** — Auto-push migration sweep (8 agents + OZK rehab) · Roster refresh (→ root CLAUDE.md + `PROME/ROSTER.md`) · staleness audit · archive sweep.
**PM** — **Fleet protocol audit** (20-agent Workflow) → **Lane 1** (7 agents swept to auto-push; corrected the over-counted "18/21" → real 17+2-holdouts) · **Lane 2** (`scripts/ledger_staleness.py` built + wired into 6 rotting agents; froze REGINALD's 4 orphan feeds) · **Lane 3** (hygiene SIGs → NEXUS/HENRY/BOND). **Coverage-gap analysis** (6-lens Workflow) → network verified well-covered, **no new agent**; routed 3 mandate-extension SIGs (LIQUID funding-plumbing + BOND MBS/FHLB+EU + HENRY semis). Docs in `PROME/cluster/`.

## Open decisions (Will)
1. **Bank-put reshape card** — shelved; fires ONLY on HY>280 sustained / WAL Jul-16 print. Needs live broker book at fire-time. ($500/card.)
2. **NEXUS refresh** — deferred (Will hold). *(New: `PREDICTIONS_MONITOR.md` = NEXUS's stale boot ledger, mislocated in PROME/ — flagged this session.)*

## Watch next 24–72h
0. **AI-capex-correction convergence** — HEN-35 (~52-55%). **Mon transmission test: MU/SMH/SOX open + VIX vs 23.** A WATCH, not a deploy.
1. HY vs 280 (278 [6/25], 2bp — auto-watched). 2. Wrapper-basket (ARCC/FSK/OBDC) vs managers. 3. 10Y 6/30 re-pull. 4. JOLTS 6/30 · NFP 7/3. 5. **Energy: EIA 7/1 · SPR ~7/3 · CFTC COT 7/3** — BRENT processes the RED SIG (downgrade label + re-derive curve). 6. Jul bank prints (CFG/OZK/WAL Jul-16). 7. June CPI 7/14.

## Fresh-boot checklist
1. Verify git (synced via train). 2. Check `AGENTS/LIQUID/alerts/HY_OAS_ALERTS.log` for any between-session HY transition. 3. Refresh dashboard/FRED before citing levels. 4. No agents warm — spawn fresh as needed.
