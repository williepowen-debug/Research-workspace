# ACTIVE_DECISIONS.md
**Updated:** 2026-06-26 ~14:35 ET (Prome — + auto-push migration pilot live)
**Owner:** Prome
**Purpose:** Boot-readable index of non-terminal decisions. Full logic stays in action cards / execution rails.

---

## Current Mode — Verification Required

Prome state has been cleaned up for reboot, but position/trade rails remain **verification-required**. Do not act from old `BROKER_PENDING`, May-roll, Jun18-trigger, CPI/refunding, or HYG language without fresh broker/Will reconciliation. CPI/refunding/BOJ/FOMC have passed; Geneva de-escalation fired but Jun20 Hormuz re-closure re-fattened the energy tail; claims/FRED HY update arrived; CFTC/FXY and expiry cleanup remain context only unless Will/broker truth is provided.

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
| Post-FOMC / Hormuz re-closure / HY <260 kill-line | `MONITOR_ONLY` / `NO_TRADE_ACTION` / `KILL_LINE_NEAR` / `ENERGY_TAIL_RE-FAT_UNCONFIRMED` | Prome/NEXUS/HENRY/LIQUID/HAWK/BRENT → grade; Will → any trade decision | Geneva/Islamabad MOU still matters, but Jun20 Hormuz re-closure declaration re-fattened the energy tail. Treat as official/declaratory/contested, not kinetic, until behavior/tape confirms. Broad cascade **not** confirmed. HY OAS remains **263 [FRED 6/17]**, only 3bp above <260 kill; VIX/banks calm; USDJPY/FXY carry remains red. Monitor for Jun22 Brent/vol response, sustained HY <260, or offsetting bank/PC deterioration. | Jun22 Brent reopen / next HY print / CFTC-FXY-carry / bank+PC re-weakening / physical Hormuz confirmation | `HEARTBEAT.md` + `PROME/TODAY.md` + `AGENTS/NEXUS/STATUS.md` |
| WALTER Routing / DEWEY loop / Quick-WALTER boundary | `REAL_PATH_PROVEN` / `QUICK_NEWS_PAUSED` / `FULL_WALTER_STANDARD` / `WALTER_OWNS_CLEANUP` | WALTER owns routing docs/tools/spec tuning; Prome owns Will-facing coordination and behavior review | Boundary holds: Full WALTER owns fresh signal judgment; Quick/Prome may route only pre-registered RED-FT / REG-T / safety-net triggers with fixed recipient_chain, plus non-routing delivery repair/backfill. DEWEY Phase 2 wiring is shipped; any WALTER-specific registry/spec cleanup remains WALTER-owned. Prome should not edit WALTER unless scoped. | Before any new signal/news routing from Prome/Quick; monitor WALTER behavior/doctor after WALTER cleanup | `AGENTS/WALTER/design/SIGNAL_PROCESSING_CHECKLIST.md` + `AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv` + `AGENTS/WALTER/tools/walter_doctor.py` + `PROME/SCRATCH.md` |
| CORAL boot/inbox/thesis maturity | `INFRA_PUSHED` / `INBOX_PROCESSED` / `THESIS_RAILS_INSTALLED` | CORAL owns future session execution; Prome monitors integration | CORAL now has boot card, WALTER board-log intake, processed WALTER inbox, NEXUS brief, and installed thesis/changelog rails. Next CORAL work is analytical: per-metro convergence grid and Q2 FL-bank earnings prep. Bank-transmission upgrade rail requires synchronized deterioration across ≥2 FL-exposed banks or explicit USCB condo-association loan deterioration with corroborating consumer/collateral data. | Next CORAL analytical pass / before Q2 FL-bank earnings | `AGENTS/CORAL/CLAUDE.md` + `AGENTS/CORAL/thesis/THESIS.md` + `AGENTS/CORAL/SCRATCH.md` + `AGENTS/CORAL/NEXUS_BRIEF.md` |
| TLT Jun 18 $85P catalyst salvage + Sep add gate | `DEFERRED` / `VERIFICATION_REQUIRED` | Will → broker/position truth; Prome → monitor only | Old 5/22 roll ticket and pre-CPI/refunding add logic are superseded. Jun $85P were a catalyst salvage bet; CPI/refunding/FOMC have passed and TLT did not break post-FOMC. Do **not** recommend add/roll/expiry action without fresh broker/Will check. | Before any TLT-related action, June-expiry write, or Sep add recommendation | `AGENTS/LIQUID/STATUS.md` + `PROME/action-cards/TLT_JUN18_DECISION_2026-05-22.md` |
| 6/18 theta-killer cluster / expiry cleanup | `WILL_APPROVED` historical rail; `VERIFICATION_REQUIRED` before use | Prome → reconcile monitor history; Will → approve any action | Do **not** roll or refresh position logic from stale May rail. This is an expiry cleanup / reconciliation problem, not an execution rail. HYG leg is dead/written-off per LIQUID. TLT/WAL/non-TLT legs require broker truth before action. | Before any 6/18 cluster decision, expiry write, or position update | `PROME/action-cards/JUN18_EXPIRY_CLUSTER_2026.md` + `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md` + `AGENTS/LIQUID/STATUS.md` |
| FXY Jun 18 $58C salvage / Japan gate | `POSITION_UPDATED` / `VERIFY_BEFORE_ACTION` | Will → position decision already made; Prome/SAM → monitor TIC/expiry context | SAM says Will decided to hold the Jun18 $58C salvage. BOJ hike was as-priced; TIC Jun18 remains context. Do not infer any new action without broker/Will check. | Before any FXY expiry action or Japan-position recommendation | `AGENTS/SAM/STATUS.md` + `PROME/TODAY.md` |
| Separate-clones fleet migration | `DEFERRED_ARCHITECTURE_DECISION` | SAM → architect; Will → decision-maker | Bundle CARL readiness + HENRY auto-memory collision proposal into one Will-decision packet only if/when Will wants the migration lane reopened. M3 atomic cutover slate remains SAM/HENRY/REGINALD/OZK/CARL. Do not do halfway. | Before any auto-memory format change or fleet-cutover scheduling | `AGENTS/SAM/proposals/2026-06-04_separate_clones_*.md` + `AGENTS/CARL/outbox/2026-06-06_to-PROME_separate_clones_CARL_readiness.md` + `AGENTS/HENRY/outbox/2026-06-06_to-PROME_automem_proposal_folder.md` |
| Bank-put reshape / (b)(c) deploy | `PROPOSED` / `SHELVED_PENDING_TRIGGER` | Will → fire decision; Prome → monitor trigger | **Standing rule (Will 6/26): deploy fresh capital ONLY on a fired trigger; $500/card max-loss** ([[feedback_deploy_on_trigger_not_calendar]]). Reshape proposal built but SHELVED — book dated 2026 / thesis 2027 (duration mismatch); (b) AOCI + (c) WAL the live paths, (a) regional trimmed. Fires ONLY on HY>280 sustained (auto-watched by `liquid-hy-watch` timer) OR WAL Jul-16 print (corrected from Jul-30, 6/26). Needs live broker book at fire-time (rule #4). | HY>280 sustained / WAL Jul-16 grade / monoline Jul-21 gate | `PROME/proposals/2026-06-26_bank-put-reshape-roll.md` + `AGENTS/TERRY/setups/` |
| Auto-push migration | `PILOT_LIVE` / `SOAK` | Prome → run pilot + report; Will → greenlit single-desktop | Prome auto-pushes at closeout via `scripts/safe-push.sh` (ff-gated, fails safe). Canonical docs + ~17 agent CLAUDE.md still "Will-coordinated" (deliberate soak divergence). After clean soak → Tier 1 canonical → remaining closeouts → lazy-sweep. **Tripwire:** non-ff abort = 2nd machine pushed → switch to per-agent branches. **Soak status (6/26):** multiple clean ff auto-pushes to date incl. 2 this session, zero tripwire — soak passing; Tier-1 canonical promotion ready when Will wants. | A clean soak (no non-ff aborts) → proceed to Tier 1 | `PROME/AUTOPUSH_MIGRATION_PLAN.md` + `PROME/CLOSEOUT.md` + `PROME/GIT_COORDINATION.md` |

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
