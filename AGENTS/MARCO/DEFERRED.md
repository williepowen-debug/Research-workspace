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

## [2026-06-02] — TOURISM thread 3 on World Cup host-city pull
**Needs:** REGINALD/CORAL
**Question:** Link Miami World Cup match-week hotel RevPAR (7 matches Jun 15–Jul 18; AHLA shows Miami ~55% ahead on booking pace but match-night occ only 24–31%) to FL bank deposit / CRE utilization. Does a temporary WC hospitality-$ spike register at the bank-collateral level, or is it too thin/transient to matter for the winter 2026-27 snowbird-$ stress timing?
**For now:** TOURISM holds the host-city $ series; REGINALD picks up the bank/CRE translation when the snowbird-$ window (Q1-Q2 2027) nears.
**Source thread:** `sub_agents/TOURISM/threads/archive/2026-06-02_worldcup-host-city.md`
**Trigger to resolve:** REGINALD room opened, OR realized Jun-Jul Miami TDT/RevPAR posts (~Sep-Oct).
**Status:** open

## [2026-06-02] — TOURISM thread 3 on World Cup host-city pull
**Needs:** CARL
**Question:** FL regional consumer-spend distribution across the 7 Miami match weeks (retail / F&B), and whether WC visitor spend is incremental or substitutes for displaced local/snowbird spend. Bears on whether the WC TDT cushion is a true add or a wash.
**For now:** OUT of TOURISM lane (visitor-flow only). Flag for CARL's FL regional consumer lens.
**Source thread:** `sub_agents/TOURISM/threads/archive/2026-06-02_worldcup-host-city.md`
**Trigger to resolve:** CARL room opened, OR realized Jun-Jul FL consumer/retail data posts.
**Status:** open

---

## Thresholds to a multi-agent room

Count of open entries per absent agent:

| Absent agent | Open | 3+ threshold? |
|---|---|---|
| REGINALD | 2 | no |
| HOUSING | 1 | no |
| CARL | 1 | no |
| BORDER | 0 | no |
| WORKFORCE | 0 | no |
| MIGRATION | 0 | no |
