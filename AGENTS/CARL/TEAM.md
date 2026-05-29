# CARL Sub-Agent Team

**Updated:** 2026-05-29 (staleness refresh — all 7 monitoring agents now 42+ days stale; catalyst feed moved to `docket/`)

> ⚠️ **All 7 monitoring sub-agents are STALE (last refreshed Apr 9-17, now 42-50d).** A dedicated refresh-burst session is overdue (Sonnet, parallel spawns). **DOC is the priority spawn** — healthcare-services GDP drag (5/28 Q1 2nd-est) = care-avoidance primary data in DOC's domain. Forward catalysts + which agent owns each now live in `docket/CALENDAR.md` (who_cares column), not the table below.

---

## ROSTER

| Agent | Domain | Status | Last Refresh | Next Catalyst | Stale? |
|-------|--------|--------|-------------|---------------|--------|
| **STUE** | Student loans (DQ, default, SAVE/RAP, servicers) | 🟢 BUILT | **Apr 17** | AFT/MOHELA May 28, SAVE transition Jul 1 | ⚠️ 42d+ stale |
| **HOMER** | Housing (foreclosures, MF DQ, builders, state-level) | 🟢 BUILT | **Apr 17** | DHI Apr 21, PHM Apr 23, Fannie MF Mar (late Apr), CS Feb Apr 28 | ⚠️ 42d+ stale |
| **GIG** | Gig economy (oversupply, Dave 28DPD, gas squeeze, AV) | 🟢 BUILT | **Apr 17** | May 6-7 cluster: Uber+DoorDash May 6, **Dave May 7 CONFIRMED**, Lyft May 7 | ⚠️ 42d+ stale |
| **PHAN** | Phantom debt / BNPL ($400B+ invisible, stacking, fintech cockroaches) | 🟢 BUILT | **Apr 17** | **Affirm Q3 FY2026 May 7 AMC CONFIRMED**, Klarna ~May 18 est, CFPB 1033 EFFECTIVELY DEAD | ⚠️ 42d+ stale |
| **POLLY** | Insurance (P&C, FAIR plans, health, FL/CA, auto) | 🟢 BUILT | **Apr 17** | **UNH Apr 21, ELV Apr 22**, CB Apr 22, ALL May 1 | ⚠️ 42d+ stale |
| **POP** | Small business (Ch.11, closures, owner guarantees, tariff transmission) | 🟢 BUILT | **Apr 17** | Jul 24 Sec 122 cliff, NFIB monthly, Census BFS monthly | ⚠️ 42d+ stale |
| **DOC** | Healthcare costs (medical debt, OOP, care avoidance, GLP-1 cost shock) | 🟢 BUILT | **Apr 9** | ACA enrollment, KFF survey fall | 🔴 50d — PRIORITY spawn (GDP healthcare-services drag) |
| **META** | Methodology & architecture research | ⚪ SPECIAL | Apr 6 | N/A — not a monitoring agent | — |

**Team readiness:** 7/7 monitoring agents built. All operational but ALL STALE (42-50d) — refresh-burst overdue.

---

## UPCOMING CATALYSTS → see `docket/`

Forward catalysts (with the sub-agent that owns each, in the `who_cares` column) now live in **`docket/CALENDAR.md`** / **`docket/CATALYSTS.tsv`** — run `scripts/docket_countdown.py` at boot. The old April/May table here was retired May 29 2026 (all dates fired; superseded by the docket). This file is now just the sub-agent **roster + staleness + spawn rules**; the docket drives *when* to spawn.

**Near-term sub-agent spawn relevance (from docket):** DOC (healthcare GDP drag — priority) · HOMER (Case-Shiller/Freddie HPI/NAHB/home-sales/builder Q2, late June) · GIG/LABOR (JOLTS Jun 2, NFP Jun 5, FL UI cliff Jun 24) · POLLY (insurance Q2 ~Jul + hurricane season) · PHAN (Affirm/Klarna ~Aug) · STUE (SAVE→RAP Jul 1, collections ~Jul) · POP (Sub-V Jul 24).

---

## BUILDOUT STATUS

All 7 monitoring agents built as of Apr 9. No further buildouts needed.

| Agent | Built | Notes |
|-------|-------|-------|
| STUE | Apr 6 | Student loans — operational |
| HOMER | Apr 7 | Housing — operational |
| GIG | Apr 9 | Gig economy — full buildout with 3 domain TSVs |
| PHAN | Apr 9 | Phantom debt — full buildout with 3 domain TSVs |
| POLLY | Apr 9 | Insurance — full buildout with CARRIER + STATE_MARKET TSVs |
| POP | Apr 9 | Small business — full buildout with SECTOR + TARIFF TSVs |
| DOC | Apr 9 | Healthcare — full buildout with COST_DRIVER + COVERAGE TSVs |

---

## REFRESH RULES

- **Current:** Refreshed within last 3 trading days. No action needed.
- **Stale (3-7 days):** Refresh on next session if no higher priority.
- **Very stale (>7 days):** Mandatory refresh. Data unreliable.
- **Dormant:** Not operational. Cannot be spawned until built out.

**At session start, check this table. Spawn any BUILT agent that is stale AND has an upcoming catalyst.**
