# ACTIVE_DECISIONS.md
**Updated:** 2026-06-14 PM ET (Prome — post-pull boot-surface refresh; stale rails verification-required)
**Owner:** Prome
**Purpose:** Boot-readable index of non-terminal decisions. Full logic stays in action cards / execution rails.

---

## Current Mode — Verification Required

Will has directed this pass toward **getting Prome updated and caught up**, not broad trade-position optimization. Phase 0–3 are a Prome boot-surface refresh after a large GitHub pull. **Do not edit agents.**

**Rule for this boot state:** do not act from any old `BROKER_PENDING`, May-roll, Jun18-trigger, CPI/refunding, or HYG language without fresh broker/Will reconciliation. CPI 6/10 and Treasury refunding have passed; pre-event rails are now historical context, not live instructions.

Key supersessions:
- **HYG Jun $75P:** LIQUID Jun 13 says written off / let expire 6/19. **Stop surfacing as actionable.**
- **Duration/TLT:** CPI/refunding rails resolved into a mixed read; LIQUID frames duration as oscillation, not regime. FOMC 6/17 is the next resolver.
- **Bank basket:** REGINALD retired broad-cohort fade; WAL bear is idiosyncratic/Q2-print gated.
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
| TLT Jun 18 $85P catalyst salvage + Sep add gate | `DEFERRED` / `FOMC_RESOLVER` / `VERIFICATION_REQUIRED` | Will → broker/position truth; Prome → monitor only | Old 5/22 roll ticket and pre-CPI/refunding add logic are superseded. Jun $85P were a catalyst salvage bet; CPI/refunding have passed and LIQUID now frames duration as oscillation, not regime. Do **not** recommend add/roll/expiry action without fresh broker/Will check. FOMC 6/17 is next macro resolver. | Before any TLT-related action, June-expiry write, or Sep add recommendation | `AGENTS/HENRY/outbox/2026-06-03_to-PROME_tlt-ticket-superseded.md` + `AGENTS/BOND/outbox/2026-06-05_to-PROME_longend-deescalation.md` + `AGENTS/LIQUID/STATUS.md` + `PROME/action-cards/TLT_JUN18_DECISION_2026-05-22.md` |
| 6/18 theta-killer cluster / expiry cleanup | `WILL_APPROVED` historical rail; `VERIFICATION_REQUIRED` before use | Prome → reconcile monitor history; Will → approve any action | Do **not** roll or refresh position logic from stale May rail. As of Jun 14, this is an **expiry cleanup / reconciliation problem**, not an execution rail. HYG leg is dead/written-off per LIQUID. BROCK R2.5 HY OAS ≥285 single-close remains monitoring-only; Phase 0 HY OAS is 278 [FRED 6/11]. TLT/WAL/non-TLT legs require broker truth before action. | Before any 6/18 cluster decision, expiry write, or position update | `PROME/action-cards/JUN18_EXPIRY_CLUSTER_2026.md` + `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md` + `PROME/action-cards/JUN18_V0.2_APPROVAL_PACKET_2026-05-25.md` + `AGENTS/BROCK/outbox/2026-06-08_to-PROME_jun18-credit-trigger-calibration-late-response.md` + `AGENTS/LIQUID/STATUS.md` |
| FXY Jun 18 $58C salvage / Japan gate | `POSITION_UPDATED` / `VERIFY_BEFORE_ACTION` | Will → position decision already made; Prome/SAM → monitor BOJ/TIC context | SAM says Will decided to hold the Jun18 $58C salvage. BOJ Jun16 and TIC Jun18 remain context, but do not infer any new action without broker/Will check. SAM-23 MOF/intervention probability marked down ~72%→~30%; BOJ still live. | Before any FXY expiry action or Japan-position recommendation | `AGENTS/SAM/STATUS.md` + `PROME/BOOT_SURFACE_REFRESH_2026-06-14_PHASE1.md` |
| Separate-clones fleet migration (post-Jun16/FOMC calm window) | `PROPOSED` — accumulating readiness | SAM → architect; Will → decision-maker post-Jun16/FOMC | Bundle CARL readiness + HENRY auto-memory collision proposal into one Will-decision packet after FOMC/calm window. M3 atomic cutover slate remains SAM/HENRY/REGINALD/OZK/CARL. HENRY interim “regenerate index instead of hand-append” fixes ~95% without full migration if needed. | Before any auto-memory format change or fleet-cutover scheduling | `AGENTS/SAM/proposals/2026-06-04_separate_clones_*.md` + `AGENTS/CARL/outbox/2026-06-06_to-PROME_separate_clones_CARL_readiness.md` + `AGENTS/HENRY/outbox/2026-06-06_to-PROME_automem_proposal_folder.md` |

---

## Next Candidate Rows — Not Active in This Rehab Pass

These remain context only until Prome finishes boot-surface catch-up and Will asks to revisit positions:

- SAM Sep-18 $60C × 5-10 contracts — SAM v1.5 says Sep $60 calls are **not warranted** under current single-path framing; do not use old pending-entry language without reading current SAM.
- TLT $88P May 15 disposition unknown — portfolio/fill-state issue, not solved here; do not confuse it with Jun $85P catalyst salvage.
- VIOLET 4/15 VIX/SKEW trade adjudication — VIOLET Jun 14 says no new entry; short-vol fade gated by Bin-B; long-vol/tail is not auto-on.
- WAL Sep $67.5P × N fresh Q2-print exposure — remains a possible later REGINALD rail; not active during state rehab.
- AAL Jul 17 $10P × 1 — standalone orphan; not active during state rehab.
- APD long thesis tag unassigned.

---

## Explicitly Dead / Do Not Surface

- **HYG Jun $75P** — written off / let expire 6/19 per LIQUID. Not actionable.
- **Pre-CPI / pre-refunding TLT Sep-add packet** — historical. FOMC is next resolver.
- **Broad bank-cohort fade** — retired by REGINALD; WAL/OZK are idiosyncratic/Q2-print, not current sector cascade.

---

## Next Maintenance Step

When Will wants positions reconciled, create a separate **position-state reconciliation pass**:

1. Pull broker / FORGE / trade-decision state.
2. Compare against these rows and action-card logs.
3. Mark each row terminal, active, or superseded.
4. Only then consider any recommendation.
