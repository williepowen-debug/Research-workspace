# Falsification Freshness Sweep — detection layer · run 2026-10-30 · in-content stamps only

**Searched:** 40 falsification surfaces across 28 agents (of 46 in FLEET_DIRECTORY) · threshold 21d behind live STATUS/thesis ref

| Verdict | N |
|---|---:|
| STALE-FLAGGED | 8 |
| CURRENT | 24 |
| FROZEN-OK | 6 |
| EVENT-LOG | 1 |
| DORMANT-SKIP | 1 |

| Agent | Surface | Class | Verdict | Stamp | Ref | Age | Cited/Live | Why |
|---|---|---|---|---|---|---:|---|---|
| CORAL | `thesis/CHANGELOG.md` | changelog/pivot log | **STALE-FLAGGED** | 2026-09-28 | 2026-10-29 | 31 | -/v1.1 | stamp 2026-09-28 is 31d behind live ref 2026-10-29 (threshold 21d) — vintage = NEWEST ENTRY (append-only surface) |
| FALCON | `workbook/EXIT_PROTOCOL.md` | thesis/validation | **STALE-FLAGGED** | 2026-10-01 | 2026-10-29 | 28 | -/v3.0 | stamp 2026-10-01 is 28d behind live ref 2026-10-29 (threshold 21d) — ⚠ header also carries 2026-10-26, 25d newer than its own stamp: check which one describes the surface |
| FERT | `STATUS.md:86` | kill rail (in-STATUS) | **STALE-FLAGGED** | 2026-08-17 | 2026-10-28 | 72 | -/- | rail stamp 2026-08-17 is 72d behind its own STATUS 2026-10-28 (threshold 21d) |
| FERT | `workbook/EXIT_PROTOCOL.md` | thesis/validation | **STALE-FLAGGED** | 2026-08-17 | 2026-10-28 | 72 | -/- | stamp 2026-08-17 is 72d behind live ref 2026-10-28 (threshold 21d) — ⚠ header also carries 2026-10-09, 53d newer than its own stamp: check which one describes the surface |
| HANS | `thesis/KILL_TREE.md` | kill tree/memo | **STALE-FLAGGED** | 2026-08-28 | 2026-10-29 | 62 | -/- | stamp 2026-08-28 is 62d behind live ref 2026-10-29 (threshold 21d) — ⚠ header also carries 2026-10-29, 62d newer than its own stamp: check which one describes the surface |
| LIQUID | `workbook/KILL_MEMO_HY_OAS_260.md` | kill tree/memo | **STALE-FLAGGED** | 2026-05-18 | 2026-10-30 | 165 | -/v2.0 | stamp 2026-05-18 is 165d behind live ref 2026-10-30 (threshold 21d) — ⚠ header also carries 2026-10-19, 154d newer than its own stamp: check which one describes the surface |
| VIOLET | `thesis/CHANGELOG.md` | changelog/pivot log | **STALE-FLAGGED** | 2026-09-17 | 2026-10-29 | 42 | v4.1/- | stamp 2026-09-17 is 42d behind live ref 2026-10-29 (threshold 21d) — vintage = NEWEST ENTRY (append-only surface) — ⚠ header also carries 2026-10-14, 27d newer than its own stamp: check which one describes the surface |
| WATT | `KILL_MEMO.md` | kill tree/memo | **STALE-FLAGGED** | 2026-09-17 | 2026-10-29 | 42 | -/- | stamp 2026-09-17 is 42d behind live ref 2026-10-29 (threshold 21d) |

**⚠ HAS A THESIS, NO SEPARATE FALSIFICATION SURFACE (3):** AEOLUS, MIDAS, OSPREY. **These are candidate findings, not clean rows.** The agent carries a live thesis but no kill tree / exit protocol / validation doc this pattern set can find — so its falsification rail is either embedded in STATUS/TRADE prose (unenforceable by any surface-level check) or absent. Judgment read required per agent.

🔴 **MARKET AGENT, NO THESIS-CLASS FILE AND NO SURFACE THIS SCAN CAN SEE (6) — THESE ARE FINDINGS, NOT A CLEAN BILL:** BROCK, CRUISE, LABOR, SHADE, YURI, ZHAO. Market is the ONE class whose L3 ladder leg REQUIRES a dated falsification surface, so 'not applicable' is never the right reading here. Their rails typically live INSIDE `STATUS.md` (## EXIT RULES / Thesis Kill / tripwires), which this pattern set cannot find. **Hand-verify each: a real rail = extract-and-stamp; no rail = a real L3 gap.** Measured 2026-08-23 across the 7 then in this bucket: 4 real rails, 3 real gaps, 0 not-applicable.

**No thesis-class file, non-Market — falsification not applicable (8):** BARON, CATO, DAEDALUS, DEWEY, NEXUS, ORACLE, RAV, TERRY. Expected for utility/meta agents. ⚠️ This bucket is scoped by CLASS as of 2026-08-23 — it previously swallowed Market agents and printed this same reassuring sentence over them (PAT-078 n+1).

**Thesis file is itself dead-bannered (2):** HAWK, REGINALD — STATUS.md is canonical for these, so their child surfaces are graded on the STATUS clock and NO live thesis version is asserted. A version comparison against a retired parent would read as conformance.

**No live reference clock:** BARON, CATO, DEWEY, RAV — no parseable date in STATUS.md or thesis header, so age comparisons are unavailable for them.
