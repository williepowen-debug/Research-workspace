# ACTIVE_DECISIONS.md
**Updated:** 2026-06-27 (Prome — auto-push lazy-sweep effectively complete: 18/21 CLAUDE.md flipped + LIQUID/CLOSEOUT.md)
**Owner:** Prome
**Purpose:** Boot-readable index of non-terminal decisions. Full logic stays in action cards / execution rails.

---

## Current Mode — Verification Required

Prome state has been cleaned up for reboot, but position/trade rails remain **verification-required**. Do not act from old `BROKER_PENDING`, May-roll, Jun18-trigger, CPI/refunding, or HYG language without fresh broker/Will reconciliation. CPI/refunding/BOJ/FOMC have passed; Geneva de-escalation fired and the Jun-20 Hormuz re-closure then resolved **non-kinetic** (Brent fell ~8%, energy tail deflated); claims/FRED HY update arrived; CFTC/FXY and expiry cleanup remain context only unless Will/broker truth is provided.

Key supersessions:
- **HYG Jun $75P:** LIQUID says written off / let expire 6/19. **Stop surfacing as actionable.**
- **Duration/TLT:** CPI/refunding/FOMC rails resolved into mixed read: Fed hawkish, but long-end did not break. Hormuz tail is back in play but not kinetic-confirmed. No add/roll/expiry action without broker/Will truth.
- **FXY/BOJ:** BOJ hike was as-priced; Will had chosen hold on Jun18 $58C. TIC/expiry are context, not auto-action.
- **Bank basket:** broad-cohort fade retired; WAL/OZK are idiosyncratic/Q2-print gated.
- **Position truth:** broker/fill state remains unreconciled. Any expiry action requires Will/broker check first.

---

## Rules

- Include decisions in non-terminal states: `DRAFT`, `PROPOSED`, `WILL_APPROVED`, `BROKER_PENDING`, `ORDER_PLACED`, `FILLED`, `POSITION_UPDATED`, `LOGGED`, `DEFERRED`.
- Remove or archive when terminal: `COMPLETED`, `REJECTED`, `EXPIRED`, `SUPERSEDED`, `CANCELLED`.
- Keep this file short. It is an index, not a thesis document.
- Every row must name an owner, next action, backstop, and source file.
- If current state is unknown, mark the row `DEFERRED` and set next action to **reconcile**, not execute.

---

## Live Decision Index

| Decision | State | Owner | Next | Backstop | Source |
|---|---|---|---|---|---|
| Post-FOMC / Hormuz / credit-bear watch | `MONITOR_ONLY` / `NO_TRADE_ACTION` / `KILL_LINE_RECEDED` / `ENERGY_TAIL_DEFLATED` | Prome/NEXUS/HENRY/LIQUID/HAWK/BRENT → grade; Will → any trade decision | Geneva/Islamabad MOU held; the Jun-20 Hormuz re-closure resolved **non-kinetic** — energy tail **DEFLATED** (Brent ~$74, Cushing <20M → BRENT Boundary #3), NOT re-fattened. The <260 soft-kill has **receded** (HY climbed well above it; reset/broken) and the live credit-bear watch is now the **>280 decoupling trigger** (HY>280 sustained + wrapper-leading). **Pull the live HY level from `HEARTBEAT.md`** (auto-watched by `liquid-hy-watch`) — do not cite it from this index. Broad cascade still **not** confirmed; bank-vs-PC divergence MACRO. | HY vs >280 (auto-watched) / wrapper-leading / next HY print — per HEARTBEAT | `HEARTBEAT.md` + `PROME/TODAY.md` + `AGENTS/NEXUS/STATUS.md` |
| WALTER Routing / DEWEY loop / Quick-WALTER boundary | `REAL_PATH_PROVEN` / `QUICK-WALTER_RETIRED` (cutover 0d, 6/26) / `FULL_WALTER_STANDARD` / `WALTER_OWNS_CLEANUP` | WALTER owns routing docs/tools/spec tuning; Prome owns Will-facing coordination and behavior review | **Quick-WALTER RETIRED 2026-06-26 (cutover 0d) — Full WALTER is the only signal-judgment path.** Prome may still do non-routing delivery repair/backfill + pre-registered RED-FT / REG-T / safety-net triggers with fixed recipient_chain. DEWEY Phase 2 wiring is shipped; any WALTER-specific registry/spec cleanup remains WALTER-owned. Prome should not edit WALTER unless scoped. | Before any new signal/news routing from Prome/Quick; monitor WALTER behavior/doctor after WALTER cleanup | `AGENTS/WALTER/design/SIGNAL_PROCESSING_CHECKLIST.md` + `AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv` + `AGENTS/WALTER/tools/walter_doctor.py` + `PROME/SCRATCH.md` |
| CORAL boot/inbox/thesis maturity | `INFRA_PUSHED` / `INBOX_PROCESSED` / `THESIS_RAILS_INSTALLED` | CORAL owns future session execution; Prome monitors integration | CORAL now has boot card, WALTER board-log intake, processed WALTER inbox, NEXUS brief, and installed thesis/changelog rails. Next CORAL work is analytical: per-metro convergence grid and Q2 FL-bank earnings prep. Bank-transmission upgrade rail requires synchronized deterioration across ≥2 FL-exposed banks or explicit USCB condo-association loan deterioration with corroborating consumer/collateral data. | Next CORAL analytical pass / before Q2 FL-bank earnings | `AGENTS/CORAL/CLAUDE.md` + `AGENTS/CORAL/thesis/THESIS.md` + `AGENTS/CORAL/SCRATCH.md` + `AGENTS/CORAL/NEXUS_BRIEF.md` |
| TLT Jun 18 $85P catalyst salvage + Sep add gate | `DEFERRED` / `VERIFICATION_REQUIRED` | Will → broker/position truth; Prome → monitor only | Old 5/22 roll ticket and pre-CPI/refunding add logic are superseded. Jun $85P were a catalyst salvage bet; CPI/refunding/FOMC have passed and TLT did not break post-FOMC. Do **not** recommend add/roll/expiry action without fresh broker/Will check. | Before any TLT-related action, June-expiry write, or Sep add recommendation | `AGENTS/LIQUID/STATUS.md` + `PROME/action-cards/TLT_JUN18_DECISION_2026-05-22.md` |
| 6/18 theta-killer cluster / expiry cleanup | `WILL_APPROVED` historical rail; `VERIFICATION_REQUIRED` before use | Prome → reconcile monitor history; Will → approve any action | Do **not** roll or refresh position logic from stale May rail. This is an expiry cleanup / reconciliation problem, not an execution rail. HYG leg is dead/written-off per LIQUID. TLT/WAL/non-TLT legs require broker truth before action. | Before any 6/18 cluster decision, expiry write, or position update | `PROME/action-cards/JUN18_EXPIRY_CLUSTER_2026.md` + `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md` + `AGENTS/LIQUID/STATUS.md` |
| FXY Jun 18 $58C salvage / Japan gate | `POSITION_UPDATED` / `VERIFY_BEFORE_ACTION` | Will → position decision already made; Prome/SAM → monitor TIC/expiry context | SAM says Will decided to hold the Jun18 $58C salvage. BOJ hike was as-priced; TIC Jun18 remains context. Do not infer any new action without broker/Will check. | Before any FXY expiry action or Japan-position recommendation | `AGENTS/SAM/STATUS.md` + `PROME/TODAY.md` |
| Concurrent-session isolation *(was: separate-clones migration)* | `MULTI-MACHINE_SUPERSEDED` / `WORKTREE_ISOLATION_OPEN` | Prome → scope; Will → decision-maker | **Multi-machine separate-clones is SUPERSEDED by the single-machine cutover (2026-06-26).** But the underlying need survives in its *intra-machine* form: many concurrent CC sessions share one `.git/index` → stage/commit races (53-file foreign-stage + dangling-deletion incidents 2026-06-26). Mitigations live now (pre-commit `git status` check in root CLAUDE.md; pathspec commits). Open = whether to adopt per-session **worktree isolation** for write-heavy parallel runs (see playbook §concurrency). Old SAM/HENRY M3 multi-machine slate = historical. | Before any write-heavy parallel multi-agent run | `PROME/ORCHESTRATION_PLAYBOOK.md` + root `CLAUDE.md` Git Protocol + `AGENTS/SAM/proposals/2026-06-04_separate_clones_*.md` (historical) |
| Bank-put reshape / (b)(c) deploy | `PROPOSED` / `SHELVED_PENDING_TRIGGER` | Will → fire decision; Prome → monitor trigger | **Standing rule (Will 6/26): deploy fresh capital ONLY on a fired trigger; $500/card max-loss** ([[feedback_deploy_on_trigger_not_calendar]]). Reshape proposal built but SHELVED — book dated 2026 / thesis 2027 (duration mismatch); (b) AOCI + (c) WAL the live paths, (a) regional trimmed. Fires ONLY on HY>280 sustained (auto-watched by `liquid-hy-watch` timer) OR WAL Jul-16 print (corrected from Jul-30, 6/26). Needs live broker book at fire-time (rule #4). | HY>280 sustained / WAL Jul-16 grade / monoline Jul-21 gate | `PROME/proposals/2026-06-26_bank-put-reshape-roll.md` + `AGENTS/TERRY/setups/` |
| DAEDALUS onboarding / Phase-4 | `WIRED` / `PHASE_4_PENDING_WILL` | Will → approve Phase-4 batches + name idle targets; DAEDALUS → propose; PROME → consume map as input | New **meta-agent** (fleet architect) merged + onboarded 2026-06-27 (`d13d34c6`): git-aligned to fleet auto-push, wired into root `CLAUDE.md`/`ROSTER`(SPECIAL)/`AGENTS.md`, SPEC→APPROVED; reviewed + methodology-verified (`maturity_scan.py` reproduces, accurate). **Non-terminal:** its **Phase-4 first real (non-dry-run) maintenance pass** — Rec-1 = add BOTTOM LINE to the 14 missing agents — needs Will approval + idle targets before it edits any live agent. PROME treats its maturity map as a hygiene *input*, subordinate to analytical quality (don't let "L4" become the scoreboard). | Will approval of a Phase-4 batch + idle target per agent | `AGENTS/DAEDALUS/STATUS.md` + `AGENTS/DAEDALUS/MATURITY_MAP.md` + `AGENTS/DAEDALUS/inbox/2026-06-27_PROME-onboarding.md` |
| Auto-push migration | `TIER_1_PROMOTED` / `LAZY_SWEEP_COMPLETE` | Prome → done (3 holdouts deliberate); Will → greenlit single-desktop + full promotion 6/26 | **Soak passed → Tier 1 canonical FLIPPED 2026-06-26 (Will-approved):** root `CLAUDE.md` Git Protocol, `GIT_COORDINATION.md`, `feedback_defer_push_coordinate` (rewritten, slug kept), `finding_push_train_pattern`, MEMORY hooks now say auto-push-at-closeout. **GENUINELY COMPLETE 6/27 PM** (after audit correction). The 6/27-AM "18/21 complete" was **over-counted** — the PM fleet-protocol audit found **7 active agents still on defer-push** (NEXUS/BRENT/VIOLET/REGINALD/BROCK/HAWK/SHADE; VIOLET/REGINALD/BROCK were never in the migration inventory). All 7 swept 6/27 PM (commit `c7d216e1`, residual-defer=0). **Now: all 19 active on auto-push EXCEPT 2 intentional holdouts** — **TERRY** (live/self-sweep), **WALTER** (architectural, `BOARD_CONSUMPTION_SPEC §7`); **YEYOU** manual/branch (Decision C). CREED Tier-2 lacks a git section (separate item). **Tripwire unchanged:** non-ff abort = 2nd machine pushed → flag Will, per-agent branches. | TERRY self-sweeps (live); WALTER/YEYOU left by design; optional TERRY/YEYOU CLOSEOUT.md | `PROME/AUTOPUSH_MIGRATION_PLAN.md` + `PROME/CLOSEOUT.md` + `PROME/GIT_COORDINATION.md` |

---

## Next Candidate Rows — Not Active During State Correction

- SAM Sep-18 $60C × 5-10 contracts — SAM v1.5 said Sep $60 calls were not warranted under then-current single-path framing; do not use old pending-entry language without reading current SAM.
- TLT $88P May 15 disposition unknown — portfolio/fill-state issue, not solved here; do not confuse it with Jun $85P catalyst salvage.
- VIOLET 4/15 VIX/SKEW trade adjudication — no new entry unless VIOLET/NEXUS current vol rails re-arm.
- WAL Sep $67.5P × N fresh Q2-print exposure — possible later REGINALD rail; not active during state correction.
- AAL Jul 17 $10P × 1 — standalone orphan; not active during state correction.
- APD long thesis tag unassigned.

---

## Explicitly Dead / Do Not Surface

- **HYG Jun $75P** — written off / let expire 6/19 per LIQUID. Not actionable.
- **Pre-CPI / pre-refunding TLT Sep-add packet** — historical. Post-FOMC review required.
- **Broad bank-cohort fade** — retired by REGINALD; WAL/OZK are idiosyncratic/Q2-print, not current sector cascade.

---

## Next Maintenance Step

When Will wants positions reconciled, create a separate **position-state reconciliation pass**:

1. Pull broker / FORGE / trade-decision state.
2. Compare against these rows and action-card logs.
3. Mark each row terminal, active, or superseded.
4. Only then consider any recommendation.
