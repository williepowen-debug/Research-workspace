# PROME STATUS.md
**Updated:** 2026-07-02 ~13:15 ET (Prome, desktop AM→midday, Standard closeout) — **★ X1 TAGGED not-sustained (283→280→275→274 [7/1]; BROCK adjudication owed)** · **MOF 7/2 candidate NO-STRIKE (SAM)** · Challenger early-print RESOLVED(cooling) · **FRED rotation half-done + `scripts/env_doctor.py` in boot gate** · LABOR graded+reviewed+fixed (37/75) · 6-inbox routing pass (`21561615`) · intake lane proven (first HY row correct). *Narrative → SCRATCH + HANDOFF + `memory/2026-07-02.md`.* Prior (laptop AM, stamps ~1h fast): **★ DEWEY BATCH 2 QUEUED (13 prompts, Will-approved all — fleet-mining 108→13, adversarial-verified, all T3) · VIX COT band LIVE in intake (VIOLET-ratified, `dfab4f9`) · NFP June SOFT first-read (+57K, −74K revisions, U-3 4.2% = participation artifact; 10Y ~4.47 muted bid — the "+3bp hawkish" first-read was a bad tick, corrected via HENRY cross-check) · 🔴 candidate MOF strike on the 8:30 NFP bar (SAM verifies).** No trade (deploy-on-trigger held — advice to Will at open: no action, nothing fired). Prior day (7/1): cwd-proof fleet sweep · serial-multi-machine amendment · HY watch → RESEARCH-INTAKE · FRED key scrub · PROME .md hygiene + freshness mechanisms. *Detail → SCRATCH + HANDOFF + memory/2026-07-02.md.*
**Last spine audit:** 2026-07-01 (first run — 5 readers, 5 blocking found + fixed same session; re-run when >7d, missing = stale).

## Core State

**Operational priority:** 6/26 session ran the detection/action HARDENING cluster (LIQUID/SENTRY/TERRY, Prome-directed) + a 3-way arch peer-review + fix round. **Standing rule (Will 6/26): deploy fresh capital ONLY on a fired trigger; $500/card.** Boot from `PROME/SCRATCH.md`. Key new machinery: the RESEARCH-INTAKE lane auto-watches the HY>280 X1-breach / <260 re-kill lines between sessions (machine-independent PRIMARY since 7/1; the desktop `liquid-hy-watch` timer is machine-local redundancy — dark when that box is off); `grade_print.py`/`chain_fetch.py`/fire-card template are the trigger→card toolchain. Prior ownership truth holds: CREED owns REIT equity tape, TERRY supersedes TRADES, ORACLE owns prediction-market diagnostics; no auto-trading.

**Current repo reality:** Clean tree, **synced 0/0** (both the main repo and the RESEARCH-INTAKE repo). **6/30: Will pruned the repo via GitHub web (19 deletions — OpenClaw vestiges + retired agents + `WILL/` private journal + SOUL/IDENTITY) for a public-facing role;** my session commits rebased cleanly onto them (no force) + safe-push ff. **Position truth is now OFF-repo** (WILL/trading-journal deleted → Will/broker direct). Public-prep follow-ups DONE (dangling-ref sweep 6/30 + history scrub verified `b01c0346`); only Will's public-flip gate remains (ACTIVE_DECISIONS). **Auto-push is the canonical closeout tail.**

**Market priority:** per `HEARTBEAT.md` (base 6/25, amended through 7/1): energy tail **FRAGILE-WATCH** (the 6/28 Iran re-escalation superseded the "deflated" read; the 6/29 CME-reopen decoupling test HOLDS — Brent held <$74; Cushing sub-20M → BRENT Boundary #3); credit-bear **ARMED — X1 line TAGGED 6/26-6/29 (283→280), not sustained; settled 275 [6/30]** (LIQUID canonical; BROCK wrapper-adjudication owed; <260 re-kill reset/distant); bank-vs-PC divergence is **MACRO, not credit-substance**. Live bear-root watch = wrapper-leading + HY OAS >280 (both unfired; intake lane auto-watches). Refresh dashboard/FRED before citing levels.

**Standing constraint:** no agent domain edits unless scoped by Will. No trade execution. **Push is auto at closeout** via ff-gated `safe-push.sh` (serial multi-machine canon, root amendment 7/1) — a non-ff abort is **routine**: `git pull --rebase` + re-push; escalate to Will only on out-of-dir rebase conflicts or mid-session recurrence (simultaneous-use signatures).

---

## Live Surfaces / Ownership

| Surface | Role | Current note |
|---|---|---|
| `AGENTS/CREED/` | National CRE / CMBS + public REIT equity tape | REITS tape absorbed; CREED remains explicit-permission Claude Code roster. |
| `AGENTS/CREED/research/REIT_EQUITY_TAPE_MODULE_2026-06-21.md` | REIT tape module | Public REIT tape trigger design; not fresh market data. |
| `AGENTS/TERRY/` | Trade construction | Now owns old TRADES verification playbook + risk scoring/calibration. |
| `AGENTS/TERRY/RISK_SCORING.md` | TERRY risk scoring | Edge, capped Kelly, Brier calibration, execution-block checklist. |
| `AGENTS/ORACLE/PREDICTION_MARKET_METRICS.md` | Prediction-market diagnostics | Entropy, KL bits, entropy-collapse alerts, ORACLE→TERRY packet. |
| `HEARTBEAT.md` | Regime pointer | Base 6/25, amended through 7/1; refresh dashboard/FRED before citing any level as current. |

---

## Current Work Queue

| Lane | Priority | Status / owner note |
|---|---:|---|
| **★ DEWEY batch 2 — 13-prompt queue drain** | 🔴 QUEUED (Will approved all, 7/2) | 13 adversarially-verified T3 prompts in `AGENTS/DEWEY/inbox/WALTER/` (05-17, docket order; deliver-by ladder 7/2→7/22) + loop manifest. **Will launches DEWEY → "drain the queue"** (3-5 reports/session, commit per report). WALTER: ledger rows + routing (packet in its inbox). Hottest: 05 HY/CCC · 06 Hormuz (7/4) · 07 funding-seizure X1. Bench ~60 → slate JSON (batch-3 source). |
| **★ RESEARCH-INTAKE lane** | ✅ VIX band LIVE 7/1 (`dfab4f9`); consumer wiring = WALTER next boot | Consumer wiring decided **option A**: WALTER routes lane-flagged breaches via its **existing delivery lane** (gated + de-duped — NOT a passive dashboard; COP/BOARD-v0.1 rotted read-side). Packet in WALTER inbox → WALTER implements next boot. EIA/CFTC uniform-alerts layer live (Cushing<20M=Boundary#3; **VIX lev-net band `(-75k,0)` ACTIVATED 7/1** — VIOLET-ratified, boundary-tested, quiet at −18,863 [6/23]). [[project_research_intake_collection_lane]]. |
| *Completed 6/26–6/29 lanes (collapsed 7/1)* | ✅ | 13 rows folded into this line (per the 7/1 PROME .md audit — completed history lives in HANDOFF + `memory/2026-06-2*.md`, not the live queue): Iran 6PM decoupling test GRADED HOLDS (BRENT owns thesis-integrity follow-up) · AEOLUS build reviewed · SHADE/CREED/BROCK + HAWK catch-ups (BRK-29 leans LAPSE ~7/3; SHADE = canonical insurer-exposure owner) · WALTER 9-signal (HEN-35 →~52-55%) · detection/action hardening · HAWK PREDICTIONS/SOURCES follow-ups · auto-push migration COMPLETE (TERRY/WALTER intentional holdouts; YEYOU manual) · ledger-staleness mechanism built+wired (6 agents) · coverage-gap analysis (no new agent warranted; #1 blind spot = funding-market plumbing) · NEXUS re-anchor reconciled (confabulated-counterparty lesson → auto-memory) · roster refresh (→ `PROME/ROSTER.md`) · PREDICTIONS_MONITOR resolved (orphan copy removed). |
| OZK revival (63d cold) | 🟠 packet delivered | `AGENTS/OZK/inbox/...REVIVAL-PACKET.md`. **Position-state UNSAFE** (broker reconcile needed); Q2 print ~Jul-16. OZK's next session gated on current broker book. |
| Bank-put reshape card | 🟡 shelved | `PROME/proposals/2026-06-26_bank-put-reshape-roll.md`; fires ONLY on HY>280 sustained / WAL Jul-16 print. $500/card. Needs live broker book at fire-time. |
| Dormant-agent cleanup | ⚪ optional | Inspect before archiving; do not demote folders from vibes. |
| CREED first real work | 🟡 if requested | Monthly CMBS/special-servicing + REIT tape tracker design. |
| TERRY first live dry run | 🟡 if requested | Use risk scoring + snapshot/risk scripts; no execution. |
| ORACLE metrics implementation | ⚪ optional | Metrics doc exists; future script integration could compute entropy/KL from ODDS_LOG. |
| Energy decoupling adjudication | ⚠️ RE-OPENED 6/26 LATE-NIGHT | RED red-team **DOWNGRADED** "STRUCTURAL settled" → **"structural LEAN, unconfirmed"** (~0.55 on regime; 0.63 fair only as a 2-wk price call). Catches: decisive COT graded 1/2 by BRENT's own trigger (same datum, two standards), declaratory-not-kinetic test, unverified contango. Routed → BRENT inbox SIG. **Discriminators: Jul-1 EIA WPSR Cushing + re-derive prompt-spread; CFTC COT 2nd-week test (slid Jul-3 → Mon 7/6, July-4 observed).** BRENT processes on its Jul-1/Jul-6 docket. |
| Fleet protocol standardization audit | ✅ done 6/27 PM | 20-agent read-only Workflow audit (git/spine/data-hygiene vs fleet standard). 51 raw → de-noised findings; CREED report was reader-error (discarded). Lanes 1+2+3 executed (Will-approved): L1 auto-push sweep + record fix, L2 ledger mechanism + freezes + wiring (6 agents), L3 owner-SIGs routed (NEXUS/HENRY/BOND inboxes, commit `7496b81e`). Remaining: Lane 4 (owner brief/STATUS refreshes — pure owner-lane) + CREED git section (low-pri). Full: `PROME/archive/cluster/2026-06-27_fleet_protocol_audit.md` (report archived 7/1 — served its purpose; residuals tracked here). |
| Coverage + hygiene SIGs (intake-only) | 🟡 owner pickup | 6 SIGs routed: NEXUS/HENRY/BOND (Lane-3 hygiene) + LIQUID/BOND/HENRY (mandate extensions: funding-plumbing/IG/EU, MBS-FHLB/EU-rates, Taiwan-Korea semis). Owners apply at next boot — don't chase. **NEXUS ✅ DONE** (Lane-3 hygiene actioned + 11-day re-anchor); HENRY/BOND/LIQUID still pending. |
| HY >280 X1 watch (live bear-root lane) | 🔴 live market lane | **X1 line TAGGED 6/26-6/29: 283 → 280 → settled 275 [6/30]** — first-ever tag, NOT sustained (LIQUID canonical 7/1; solo-half rule = log+hold; **BROCK wrapper-leads adjudication OWED**, LIQUID outbox 7/1). <260 re-kill reset/distant. First intake HY row lands ~11:00-13:00 ET 7/2 (7/1 obs); **post-NFP 7/2 obs arrives via the Fri 7/3 holiday run**. Soft-NFP + hawkish-rates leaking into spreads is the combination the ladder cares about. |
| NFP June grade + MOF strike verify | ✅ both landed 7/2 (follow-ups open) | **LABOR DONE** (freeze-deepening re-pin `b50c6ada`; caught the early Challenger print; +PM intake sweep `eafd569b` — MSFT layoff watch line). PROME review: mostly clean, 0 data errors — **both follow-ups RESOLVED same-hour (`70f0d683`, verified applied):** matrix recount 40→**37/75** (owner correctly diverged from the reviewer's /80 — a merged-out vector shrinks the max too; ≈41/80 like-for-like bridge kept), TRADE Aug-7 renumbered #1-of-fresh-streak, nits adopted (stamps now from `date`). Next LABOR trigger: ISM Services Mon 7/6. **SAM verdict NO-STRIKE** (ambush-regime caveat; integrated `01ce16a3`) — **session UNCOMMITTED (19 files + 2 outbox notes): closeout owed.** 🔴 JGB overlay + LABOR follow-ups + lane extras ✅ **ALL ROUTED** (Will-authorized, `21561615`, 6 inboxes, recipient-state-aware — BOND/LIQUID had already processed their Jun-30 packages → post-hoc-correction framing). |
| Position-state reconciliation | 🟠 pending | Broker/Will truth required. |

---

## Rules of Engagement

- **No auto-trading.** ORACLE measures; TERRY evaluates; Will approves.
- **No REITS/TRADES/HERMES revival** without Will — folders were removed entirely 6/30 (git-history recoverable; per `PROME/ROSTER.md`), so revival = history-restore + Will approval, not a launch.
- **No CREED full migration** unless explicitly approved.
- **Do not move/delete legacy source archives** unless scoped.
- **Pathspec commits only;** never broad add/reset/stash/force-push.

---

## Next Best Action

**Launch queue (Will accepted 7/2 midday):** **DEWEY** (PROMPT-06 Hormuz deliver-by 7/4 — hottest) → **WALTER** (consumer wiring + DEWEY ledger) → **BROCK** (owed X1 wrapper-leads adjudication + BRK-29 ~7/3 grade) → **NEXUS** if slot (6/30 rebalance grade owed). **Mon 7/6:** LIQUID · BOND (pre-refunding + JGB-overlay re-open) · BRENT (COT test) · HENRY. LABOR done thru ISM Services 7/6; SAM finishing (closeout check next boot). **Public-prep unchanged:** only Will's public-flip remains (DELIBERATE WAIT, don't nag) + rotate the FRED key pre-flip. **Carried (parked, not blocking):** essay revise; BOARD→WALTER thinning; AEOLUS→MARCO handshake; BROCK reframe; RESEARCH-INTAKE consumer wiring (WALTER — VIX band half DONE 7/1); DAEDALUS utility-cohort firming; MEMORY.md index trim. **Forward docket (canonical → `PROME/DOCKET.tsv`):** BRK-29 ~7/3 (Challenger RESOLVED early 7/1) · COT 7/6 · JGB 30Y 7/7 · UST refunding 7/7-9 · WASDE 7/10 · CPI 7/14 · monolines 7/15-22 · OZK/WAL 7/16 · BDC marks 7/25-28 · MOF data ~7/31. Credit-bear HY>280/wrapper-leading auto-watched; bank-put reshape shelved pending trigger.
