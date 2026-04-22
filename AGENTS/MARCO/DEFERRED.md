# MARCO — DEFERRED.md

Running log of items from closed rooms that needed absent sub-agents or cross-agent input. When **3+ open entries accumulate for the same absent sub-agent**, a multi-agent room with them is earned.

Status values: `open` | `resolved [YYYY-MM-DD]`

---

## [2026-04-22] — TOURISM thread 2 on $-at-risk v0 grid decisions
**Needs:** REGINALD
**Question:** What spatial resolution does REGINALD need for the bank-exposure hand-off from the TOURISM $-at-risk series? If strict county-level commercial-loan matching is required on non-TDT counties, the proxy-quality bar rises and the mixed-grid native design must be revisited. If metro-level (MSA) is acceptable, current design works as-specced.
**For v0:** TOURISM builds at mixed-grid native; REGINALD aggregates as needed. Revisit only if REGINALD contests proxy quality.
**Source thread:** `sub_agents/TOURISM/threads/archive/2026-04-22_dollar-at-risk-v0-grid-decisions.md`
**Trigger to resolve:** REGINALD room opened, OR REGINALD signal contesting proxy quality.
**Status:** open

## [2026-04-22] — TOURISM thread 2 on $-at-risk v0 grid decisions
**Needs:** HOUSING
**Question:** Is Canadian-owner snowbird ground-spend (owner-occupied condos/SFRs — groceries, dining, services with no hotel/STR trace) in or out of the $-at-risk v0 model? Joint model requires HOUSING Canadian-owner inventory × TOURISM spend-per-snowbird-week.
**For v0:** OUT — documented as known underestimate. v1 pickup via joint model.
**Source thread:** `sub_agents/TOURISM/threads/archive/2026-04-22_dollar-at-risk-v0-grid-decisions.md`
**Trigger to resolve:** HOUSING sub-agent outfit complete + thread opened.
**Status:** open

---

## Thresholds to a multi-agent room

Count of open entries per absent agent:

| Absent agent | Open | 3+ threshold? |
|---|---|---|
| REGINALD | 1 | no |
| HOUSING | 1 | no |
| CARL | 0 | no |
| BORDER | 0 | no |
| WORKFORCE | 0 | no |
| MIGRATION | 0 | no |
