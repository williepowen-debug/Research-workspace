# CARL Sub-Agent Team

**Updated:** 2026-06-22 PM (GIG refreshed via catch-up gather — 66d gap closed: driver oversupply confirmed, Dave Q1 1.69% survivorship, FL UI Wave-1 magnitude-constrained 8% recipiency, gas squeeze receding; SV-GIG-2026-06-22-01. STUE/DOC/HOMER now ~13-14d edging stale; PHAN/POLLY/POP 66d.)

> **Status (Jun 9):** 3/7 monitoring agents fresh (DOC Jun-8, HOMER Jun-8, STUE Jun-9). 4 still stale 50-60d: **GIG is priority spawn** — FL UI Wave 1 cliff in 15 days; Dave Q1 (May 7), Uber/DASH/Lyft Q1 (May 6-7) all 33d-stale unintegrated at GIG-level. PHAN/POP/POLLY medium-stale — Affirm Q3 / Klarna Q1 / NFIB Apr-May / Q2 P&C all pending; lower-urgency, parallel-spawn-burst candidates. Forward catalysts + which agent owns each live in `docket/CALENDAR.md` (who_cares column).

---

## ROSTER

| Agent | Domain | Status | Last Refresh | Stale? |
|-------|--------|--------|-------------|--------|
| **STUE** | Student loans (DQ, default, SAVE/RAP, servicers) | 🟢 BUILT | **Jun 9** | 🟢 fresh (CRL-04 BREACHED + SAVE→RAP operational-GO + Treasury Phase 1 cadence resolved) |
| **HOMER** | Housing (foreclosures, MF DQ, builders, state-level) | 🟢 BUILT | **Jun 8** | 🟢 fresh (MF reframed extend-and-pretend; year-misread caught & corrected) |
| **DOC** | Healthcare costs (medical debt, OOP, care avoidance, GLP-1 cost shock) | 🟢 BUILT | **Jun 8** | 🟢 fresh (Mercer +6.7% V14 candidate; ACA cliff realizing 6mo early; NIPA care-avoidance) |
| **GIG** | Gig economy (oversupply, Dave 28DPD, gas squeeze, AV) | 🟢 BUILT | **Jun 22** | 🟢 fresh (driver oversupply confirmed; Dave Q1 1.69% survivorship; FL UI Wave-1 magnitude-constrained 8% recipiency; gas receding — SV-GIG-2026-06-22-01) |
| **PHAN** | Phantom debt / BNPL ($400B+ invisible, stacking, fintech cockroaches) | 🟢 BUILT | **Apr 17** | 🟡 53d (Affirm/Klarna Q1 prints at parent only, not PHAN-level) |
| **POLLY** | Insurance (P&C, FAIR plans, health, FL/CA, auto) | 🟢 BUILT | **Apr 17** | 🟡 53d (Q2 ~late Jul; hurricane Q3; lower urgency) |
| **POP** | Small business (Ch.11, closures, owner guarantees, tariff transmission) | 🟢 BUILT | **Apr 17** | 🟡 53d (NFIB Apr+May unintegrated; Sub-V May +36% in parent only) |
| **META** | Methodology & architecture research | ⚪ SPECIAL | Apr 6 | — |

**Team readiness:** 7/7 monitoring agents built. GIG fresh (Jun 22); STUE/DOC/HOMER ~13-14d (edging stale); PHAN/POLLY/POP 66d (medium-stale — Affirm/Klarna Q2 ~Aug, NFIB, Q2 P&C pending).

---

## UPCOMING CATALYSTS → see `docket/`

Forward catalysts (with the sub-agent that owns each, in the `who_cares` column) now live in **`docket/CALENDAR.md`** / **`docket/CATALYSTS.tsv`** — run `scripts/docket_countdown.py` at boot. The old April/May table here was retired May 29 2026 (all dates fired; superseded by the docket). This file is now just the sub-agent **roster + staleness + spawn rules**; the docket drives *when* to spawn.

**Near-term sub-agent spawn relevance (from docket):** DOC (healthcare GDP drag — priority) · HOMER (Case-Shiller/Freddie HPI/NAHB/home-sales/builder Q2, late June) · GIG/LABOR (JOLTS Jun 2, NFP Jun 5, FL UI cliff Jun 24) · POLLY (insurance Q2 ~Jul + hurricane season) · PHAN (Affirm/Klarna ~Aug) · STUE (SAVE→RAP Jul 1, collections ~Jul) · POP (Sub-V Jul 24).

---

## REFRESH RULES

- **Current:** Refreshed within last 3 trading days. No action needed.
- **Stale (3-7 days):** Refresh on next session if no higher priority.
- **Very stale (>7 days):** Mandatory refresh. Data unreliable.
- **Dormant:** Not operational. Cannot be spawned until built out.

**At session start, check this table. Spawn any BUILT agent that is stale AND has an upcoming catalyst.**
