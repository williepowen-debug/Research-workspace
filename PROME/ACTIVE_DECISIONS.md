# ACTIVE_DECISIONS.md
**Updated:** 2026-06-04 ~17:25 ET
**Owner:** Prome
**Purpose:** Boot-readable index of non-terminal decisions. Full logic stays in action cards / execution rails.

---

## Current Mode — Verification Required

Will has directed this pass toward **getting Prome updated and caught up**, not broad trade-position optimization. The Jun 2 boot-surface rehab was completed/pushed; Jun 3-4 signals are now being ingested narrowly.

**Rule for this boot state:** do not act from any old `BROKER_PENDING` / trigger language without fresh broker/Will reconciliation. HENRY's Jun 3 signal supersedes the old TLT 5/22 roll ticket: Jun $85P are now a small catalyst salvage bet handled by Will, and the Sep add is deferred to CPI confirmation.

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
| TLT Jun 18 $85P ×3 catalyst salvage + Sep add CPI gate | `POSITION_UPDATED` / `DEFERRED` | Will → handle Jun $85P broker salvage; Prome → monitor NFP/CPI/FOMC context only | Old 5/22 2/1 roll ticket is **SUPERSEDED**. Jun $85P are held as a ~$168 catalyst bet into NFP 6/5 / CPI 6/10 / FOMC 6/16-17, to sell into the first hot print, not ride to expiry. Sep 19 $85P add is deferred until May CPI: only revisit if core CPI >0.3% MoM and 10Y backs up. | Before any TLT-related action, June-expiry write, or Sep add recommendation | `AGENTS/HENRY/outbox/2026-06-03_to-PROME_tlt-ticket-superseded.md` + `PROME/action-cards/TLT_JUN18_DECISION_2026-05-22.md` |
| 6/18 theta-killer cluster | `WILL_APPROVED` historical rail; verification required before use | Prome → reconcile monitor history; Will → approve any new action | Do **not** roll or refresh position logic from stale May 26 rail. TLT leg now has a Jun 3 supersession; reconstruct any remaining non-TLT legs before use. | Before any 6/18 cluster decision or June-expiry write | `PROME/action-cards/JUN18_EXPIRY_CLUSTER_2026.md` + `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md` + `PROME/action-cards/JUN18_V0.2_APPROVAL_PACKET_2026-05-25.md` |

---

## Next Candidate Rows — Not Active in This Rehab Pass

These remain context only until Prome finishes state catch-up and Will asks to revisit positions:

- SAM Sep-18 $60C × 5-10 contracts — SAM v1.5 says Sep $60 calls are **not warranted** under current single-path framing; do not use old pending-entry language without reading current SAM.
- FXY $58C reconciliation — portfolio/fill-state issue, not solved here.
- TLT $88P May 15 disposition unknown — portfolio/fill-state issue, not solved here; do not confuse it with the Jun $85P catalyst salvage row above.
- VIOLET 4/15 VIX/SKEW trade adjudication — 60d window closes ~6/12, but VIOLET Jun 1 says R11 analog dead and timing reset; read current VIOLET before using.
- APD long thesis tag unassigned.
- WAL Sep $67.5P × N fresh Q2-print exposure — remains a possible later REGINALD rail; not active during state rehab.
- AAL Jul 17 $10P × 1 — standalone orphan; not active during state rehab.

---

## Next Maintenance Step

When Will wants positions reconciled, create a separate **position-state reconciliation pass**:
1. Pull broker / FORGE / trade-decision state.
2. Compare against these rows and action-card logs.
3. Mark each row terminal, active, or superseded.
4. Only then consider any recommendation.
