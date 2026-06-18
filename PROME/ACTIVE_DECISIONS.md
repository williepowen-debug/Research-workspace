# ACTIVE_DECISIONS.md
**Updated:** 2026-06-17 21:32 ET (Prome — WALTER delivery-push model pending)
**Owner:** Prome
**Purpose:** Boot-readable index of non-terminal decisions. Full logic stays in action cards / execution rails.

---

## Current Mode — Verification Required

Will has directed this pass toward **getting Prome right before anything else**. Do not act from old `BROKER_PENDING`, May-roll, Jun18-trigger, CPI/refunding, or HYG language without fresh broker/Will reconciliation. CPI/refunding/BOJ/FOMC have passed; claims/TIC/FRED HY update and expiry 6/18 are the next live gates.

Key supersessions:
- **HYG Jun $75P:** LIQUID says written off / let expire 6/19. **Stop surfacing as actionable.**
- **Duration/TLT:** CPI/refunding/FOMC rails resolved into mixed read: Fed hawkish, but long-end did not break. No add/roll/expiry action without broker/Will truth.
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
| Post-FOMC hawkish re-arm / HY <260 kill-line | `MONITOR_ONLY` / `NO_TRADE_ACTION` / `CONFIRMATION_PENDING` | Prome/NEXUS/HENRY/LIQUID → grade; Will → any trade decision | Hawkish-of-pricing branch fired: hold 3.50–3.75 but SEP/dots materially hawkish vs March; equities/HYG/KRE/WAL/BIZD sold, VIX 18.44, USDJPY >160. Broad cascade **not** confirmed: HY OAS **271 [FRED 6/16]** remains above <260 kill and <300; TLT held. Confirm with 6/18 FRED HY + claims/TIC + persistence in VIX/HYG/KRE/WAL. | FRED HY confirmation 6/18 + claims/TIC + expiry/opex digestion | `HEARTBEAT.md` + `PROME/TODAY.md` + `AGENTS/NEXUS/STATUS.md` |
| WALTER Routing v2 / delivery reliability | `REAL_PATH_PROVEN` / `PUSH_POLICY_PENDING` / `SYSTEM_HEALTH` | WALTER owns routing docs/tools; Prome owns Will-facing delivery/push policy | Real Quick-WALTER spawn passed, Iran guard fired, BRENT/HAWK consumed backfills, and doctor shows zero WALTER handoffs in flight. Will clarified serious domain-agent work happens in Claude Code desktop/laptop sessions, so origin push is the practical visibility boundary. Next: choose Prome push policy for WALTER routes (immediate vs urgency-tiered vs explicit flush queue). | Before relying on routed signals reaching Claude Code sessions without manual push/pull coordination | `AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md` + `AGENTS/WALTER/tools/walter_doctor.py` + `PROME/SCRATCH.md` |
| TLT Jun 18 $85P catalyst salvage + Sep add gate | `DEFERRED` / `VERIFICATION_REQUIRED` | Will → broker/position truth; Prome → monitor only | Old 5/22 roll ticket and pre-CPI/refunding add logic are superseded. Jun $85P were a catalyst salvage bet; CPI/refunding/FOMC have passed and TLT did not break post-FOMC. Do **not** recommend add/roll/expiry action without fresh broker/Will check. | Before any TLT-related action, June-expiry write, or Sep add recommendation | `AGENTS/LIQUID/STATUS.md` + `PROME/action-cards/TLT_JUN18_DECISION_2026-05-22.md` |
| 6/18 theta-killer cluster / expiry cleanup | `WILL_APPROVED` historical rail; `VERIFICATION_REQUIRED` before use | Prome → reconcile monitor history; Will → approve any action | Do **not** roll or refresh position logic from stale May rail. This is an expiry cleanup / reconciliation problem, not an execution rail. HYG leg is dead/written-off per LIQUID. TLT/WAL/non-TLT legs require broker truth before action. | Before any 6/18 cluster decision, expiry write, or position update | `PROME/action-cards/JUN18_EXPIRY_CLUSTER_2026.md` + `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md` + `AGENTS/LIQUID/STATUS.md` |
| FXY Jun 18 $58C salvage / Japan gate | `POSITION_UPDATED` / `VERIFY_BEFORE_ACTION` | Will → position decision already made; Prome/SAM → monitor TIC/expiry context | SAM says Will decided to hold the Jun18 $58C salvage. BOJ hike was as-priced; TIC Jun18 remains context. Do not infer any new action without broker/Will check. | Before any FXY expiry action or Japan-position recommendation | `AGENTS/SAM/STATUS.md` + `PROME/TODAY.md` |
| Separate-clones fleet migration | `PROPOSED` — accumulating readiness | SAM → architect; Will → decision-maker post-FOMC | Bundle CARL readiness + HENRY auto-memory collision proposal into one Will-decision packet after FOMC/calm window. M3 atomic cutover slate remains SAM/HENRY/REGINALD/OZK/CARL. | Before any auto-memory format change or fleet-cutover scheduling | `AGENTS/SAM/proposals/2026-06-04_separate_clones_*.md` + `AGENTS/CARL/outbox/2026-06-06_to-PROME_separate_clones_CARL_readiness.md` + `AGENTS/HENRY/outbox/2026-06-06_to-PROME_automem_proposal_folder.md` |

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
