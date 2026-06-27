# PROME STATUS.md
**Updated:** 2026-06-27 (Claude Code Prome — Sat agent-build-out: **auto-push migration COMPLETE [18/21]** + **roster refresh** [→`PROME/ROSTER.md`] + pre-closeout staleness audit + archive sweep. ORACLE/TERRY/WALTER live in separate windows; pushed via train. No trigger fired, no capital deployed.)

## Core State

**Operational priority:** 6/26 session ran the detection/action HARDENING cluster (LIQUID/SENTRY/TERRY, Prome-directed) + a 3-way arch peer-review + fix round. **Standing rule (Will 6/26): deploy fresh capital ONLY on a fired trigger; $500/card.** Boot from `PROME/SCRATCH.md`. Key new machinery: a LIVE `liquid-hy-watch` systemd timer auto-catches an HY>280 cross between sessions; `grade_print.py`/`chain_fetch.py`/fire-card template are the trigger→card toolchain. Prior ownership truth holds: CREED owns REIT equity tape, TERRY supersedes TRADES, ORACLE owns prediction-market diagnostics; no auto-trading.

**Current repo reality:** Clean tree, **synced 0/0** (only WILL/trading-journal = Will's, untouched). This session's commits (HAWK ×3, RED ×1, BRENT SIG, auto-push migration) all pushed via `scripts/safe-push.sh` — a 7-commit ff train (incl. a stray WALTER commit), exit 0, zero tripwire. **Auto-push is now the canonical closeout tail** (promoted off soak 6/26).

**Market priority:** per `HEARTBEAT.md` (6/25): energy tail **DEFLATED** (Brent ~$74, Hormuz resolved non-kinetic; Cushing sub-20M → BRENT Boundary #3); credit-bear **ARMED — pre-trigger/entry-gated** above the <260 kill (HY 271); bank-vs-PC divergence is **MACRO, not credit-substance**. Live bear-root watch = wrapper-leading + HY OAS >280 (both unfired). Refresh dashboard/FRED before citing levels.

**Standing constraint:** no agent domain edits unless scoped by Will. No trade execution. **Push is now auto at closeout** via ff-gated `safe-push.sh` (single-machine; promoted 6/26) — a non-ff abort = 2nd machine returned → stop, flag Will.

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
| WALTER 9-signal processing | ✅ done 6/26 PM | 5 owners ×2 rounds, ingest-notes committed. **HEN-35 30%→~52-55%** (AI-capex-correction convergence). Mon discriminators = MU/SMH/SOX, VIX vs 23. |
| OZK revival (63d cold) | 🟠 packet delivered | `AGENTS/OZK/inbox/...REVIVAL-PACKET.md`. **Position-state UNSAFE** (broker reconcile needed); Q2 print ~Jul-16. OZK's next session gated on current broker book. |
| HAWK catch-up | ✅ packet delivered | `AGENTS/HAWK/inbox/...CATCHUP-PACKET.md`. 9-sig backlog triaged (all confirm); decoupling test resolved (Brent shrug). 4 to ingest. |
| Detection/action hardening | ✅ done 6/26 AM | config retune + live HY watch timer + trigger→card toolchain + grade_print; verified, pushed. |
| Bank-put reshape card | 🟡 shelved | `PROME/proposals/2026-06-26_bank-put-reshape-roll.md`; fires ONLY on HY>280 sustained / WAL Jul-16 print. $500/card. Needs live broker book at fire-time. |
| Dormant-agent cleanup | ⚪ optional | Inspect before archiving; do not demote folders from vibes. |
| CREED first real work | 🟡 if requested | Monthly CMBS/special-servicing + REIT tape tracker design. |
| TERRY first live dry run | 🟡 if requested | Use risk scoring + snapshot/risk scripts; no execution. |
| ORACLE metrics implementation | ⚪ optional | Metrics doc exists; future script integration could compute entropy/KL from ODDS_LOG. |
| Energy decoupling adjudication | ⚠️ RE-OPENED 6/26 LATE-NIGHT | RED red-team **DOWNGRADED** "STRUCTURAL settled" → **"structural LEAN, unconfirmed"** (~0.55 on regime; 0.63 fair only as a 2-wk price call). Catches: decisive COT graded 1/2 by BRENT's own trigger (same datum, two standards), declaratory-not-kinetic test, unverified contango. Routed → BRENT inbox SIG. **Discriminators: Jul-1 EIA WPSR Cushing + re-derive prompt-spread; Jul-3 CFTC COT 2nd-week test.** BRENT processes on its Jul-1/Jul-3 docket. |
| HAWK 2 follow-ups | ✅ done 6/26 LATE-NIGHT | PREDICTIONS.tsv tab fix (HAW-10/11 delimiter-only, byte-identical) + SOURCES.md refresh-not-retire. Committed+pushed. |
| Auto-push migration | ✅ COMPLETE 6/27 | **18/21 CLAUDE.md flipped** (8 swept incl. OZK git-rehab + ORACLE self-flip + LIQUID/CLOSEOUT.md). 3 deliberate holdouts: TERRY (live/self-sweep), WALTER (architectural), YEYOU (manual). See `PROME/ROSTER.md` + `AUTOPUSH_MIGRATION_PLAN.md`. |
| Roster refresh | ✅ done 6/27 | Verified-active pass (commit-activity map). root CLAUDE.md Active=20/Tier-2=4 + new `PROME/ROSTER.md`. VIOLET→Active (was unslotted), OZK→Dormant, DARWIN removed, 4 scaffolds retired→`AGENTS/_archive/`. |
| PREDICTIONS_MONITOR → NEXUS | 🟡 flagged 6/27 | `PROME/PREDICTIONS_MONITOR.md` is NEXUS's live boot-read ledger (mislocated in PROME/, stale April rows). NEXUS to refresh + consider migrating to `AGENTS/NEXUS/`. |
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

After clear, fresh Prome should check `AGENTS/LIQUID/alerts/HY_OAS_ALERTS.log` for any between-session HY transition (watch timer daily 13:00 ET). Live regime: HY 278 [6/25] Fri-close, 2bp from >280 X1 — auto-watched; no action unless a trigger fires. **Auto-push migration + roster refresh COMPLETE this session** (see `PROME/ROSTER.md`). **Flag to NEXUS:** `PROME/PREDICTIONS_MONITOR.md` is NEXUS's live boot-read ledger (mislocated in PROME/, stale April rows) — NEXUS to refresh/migrate. **Energy is a LEAN, unconfirmed structural read** — BRENT processes the RED SIG on its **Jul-1 EIA WPSR / Jul-3 COT** docket. AI-capex (HEN-35 ~53%) = **Mon: MU/SMH/SOX + VIX vs 23 + HY vs 280.** **Forward docket:** Mon MU/semis · 10Y 6/30 · JOLTS 6/30 · NFP 7/3 · **EIA 7/1 · SPR re-auth ~7/3 · CFTC COT 7/3 · OZK+WAL+CFG Jul-16** · CPI 7/14 · late-Jul Q2 FCF + BDC marks ~7/25.
