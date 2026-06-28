# PROME STATUS.md
**Updated:** 2026-06-28 (Sun, LAPTOP) closeout — **Iran RE-ESCALATION + 6PM oil pre-registration (BRENT+HAWK fan-out)** · FORGE position-truth decision (a) · AEOLUS pulled+reviewed (DAEDALUS's first build). Boot recovered a disrupted WALTER session; synced 0/0, pushed. No trade executed (pre-registration only; standing rule held). *Prior 6/27 detail → HANDOFF + memory.*

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
| **★ Iran 6PM oil decoupling test** | 🔴 LIVE (~6PM ET 6/28) | **Pre-registered** (BRENT+HAWK fan-out): HOLDS <$74 / AMBER $74-76 / CRACKS >$76-or-sustain->$75 → re-arm USO ≤$500 AFTER the sustain. Grade next session; act only on a sustained crack. `AGENTS/BRENT/PREREG_20260628_CME_reopen.md` · `AGENTS/HAWK/REMARK_20260628.md`. |
| **AEOLUS pulled (DAEDALUS first build)** | ✅ reviewed 6/28 | Climate→economy agent built via online app; quality strong (fleet disciplines baked in, no red flags). Owner-lane handshakes route to CORAL/MARCO. |
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
| Auto-push migration | ✅ GENUINELY COMPLETE 6/27 PM | **The 6/27-AM "18/21 complete" was over-counted.** The PM fleet-protocol audit found **7 active agents still on defer-push** (NEXUS/BRENT/VIOLET/REGINALD/BROCK/HAWK/SHADE) — swept 6/27 PM (commit `c7d216e1`, residual-defer=0). Now: all 19 active on auto-push except 2 intentional holdouts (TERRY/WALTER); YEYOU manual. See `AUTOPUSH_MIGRATION_PLAN.md`. |
| Fleet protocol standardization audit | ✅ done 6/27 PM | 20-agent read-only Workflow audit (git/spine/data-hygiene vs fleet standard). 51 raw → de-noised findings; CREED report was reader-error (discarded). Lanes 1+2+3 executed (Will-approved): L1 auto-push sweep + record fix, L2 ledger mechanism + freezes + wiring (6 agents), L3 owner-SIGs routed (NEXUS/HENRY/BOND inboxes, commit `7496b81e`). Remaining: Lane 4 (owner brief/STATUS refreshes — pure owner-lane) + CREED git section (low-pri). Full: `PROME/cluster/2026-06-27_fleet_protocol_audit.md`. |
| Ledger-staleness mechanism | ✅ built + wired 6/27 PM | `scripts/ledger_staleness.py` — boot-time mtime alert (git-time, FROZEN-aware, by-name exemptions, 30d default) closes the 8-agent silent-rot gap (rule existed, mechanism didn't). Froze REGINALD's 4 verified-dead orphan feeds; held its live FLOW/KB + BROCK matrix for owners. **Wired into the 6 rotting agents' boots** (BRENT/REGINALD/BROCK/HAWK/RED/CARL — commit `63e90d53`, smoke-tested rc=0). Fleet-wide wiring remains optional. |
| Network coverage-gap analysis | ✅ done 6/27 PM | 6-lens read-only Workflow → network verified well-covered, NO new agent warranted (downgraded synthesis' G-SIB + Pension-LDI picks). #1 blind spot = funding-market plumbing (load-bearing to HY>280). Doc: `PROME/cluster/2026-06-27_coverage_gap_analysis.md`. |
| Coverage + hygiene SIGs (intake-only) | 🟡 owner pickup | 6 SIGs routed: NEXUS/HENRY/BOND (Lane-3 hygiene) + LIQUID/BOND/HENRY (mandate extensions: funding-plumbing/IG/EU, MBS-FHLB/EU-rates, Taiwan-Korea semis). Owners apply at next boot — don't chase. **NEXUS ✅ DONE** (Lane-3 hygiene actioned + 11-day re-anchor); HENRY/BOND/LIQUID still pending. |
| NEXUS re-anchor reconciliation | ✅ done 6/27 PM (corrected) | NEXUS re-anchored 6/16→6/27; its **market read** (M-09 unwind, bifurcation, R3↔R4 coupling, 6/30 + 7/15-28 gates) is sound → integrated into HEARTBEAT. **Correction:** NEXUS framed it as "diverging from PROME's Grind 55%+ read" citing a `PROME/coordination` digest — **that digest never existed; PROME holds no such stance and runs no numeric prob-split.** NEXUS confabulated a PROME counterparty + fabricated a source; I initially accepted it (laundered the phantom into HEARTBEAT, now stripped). **Lesson: verify an attributed position + cited source EXISTS before reconciling against it** (`[[finding_circular_corroboration_via_state_file]]`). |
| Roster refresh | ✅ done 6/27 | Verified-active pass (commit-activity map). root CLAUDE.md Active=20/Tier-2=4 + new `PROME/ROSTER.md`. VIOLET→Active (was unslotted), OZK→Dormant, DARWIN removed, 4 scaffolds retired→`AGENTS/_archive/`. |
| PREDICTIONS_MONITOR → NEXUS | ✅ RESOLVED 6/27 PM | NEXUS confirmed its **live** ledger (`AGENTS/NEXUS/PREDICTIONS_MONITOR.md`) was already CURRENT — my "stale April rows" flag had read the **dead `PROME/` orphan** (Mar-31 copy), now `git rm`'d (recoverable from history; live ledger is canonical). NEXUS also actioned the rest of the Lane-3 SIG (Tier-2 roster, STATUS spine, LAST_COMPLETION divergence documented). **Lesson: I flagged off the wrong (orphan) copy — verify which copy is live before flagging "stale."** |
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

**Next session = grade the ~6:00 PM ET CME oil reopen** (Sun 6/28; desktop or here). Pull live Brent/WTI vs the pre-registered table (HOLDS <$74 / AMBER $74-76 / CRACKS >$76 or a $74-76 gap that SUSTAINS >$75 into Mon London) — **grade the sustain, not the gap.** A sustained crack → BRENT brings the USO call-spread proposal (≤$500) for Will; a hold → no action, thesis strengthens. Detail: `AGENTS/BRENT/PREREG_20260628_CME_reopen.md` · `AGENTS/HAWK/REMARK_20260628.md` · SCRATCH · HEARTBEAT Near-Gates. **Carry-forward:** ✅ root `CLAUDE.md` FORGE-ref sweep + FORGE/STATUS staleness banner DONE 6/28 desktop (b169e149, pushed); owner-lane AEOLUS handshakes (CORAL/MARCO) + muni/housing deliverables (CARL/CORAL). **2nd-writer alert:** the online/web CC app is now a live writer (AEOLUS pushed from it) — re-verify sync before any commit; non-ff = flag Will, don't force. **Forward docket:** ~6PM oil TODAY · 10Y/JOLTS 6/30 · EIA 7/1 · NFP+COT 7/3 · OZK+WAL+CFG Jul-16 · CPI 7/14. **Prior open (unchanged):** credit-bear HY>280/wrapper-leading auto-watched; HEN-35 AI-capex; OZK Q2 ~Jul-16.
