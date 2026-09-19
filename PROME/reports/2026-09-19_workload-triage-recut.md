# PROME workload — re-cut into three buckets
**2026-09-19 18:3x ET · author PROME · origin: CATO point 4, 2026-09-19 17:25**
⛔ **This report corrects a PROME claim made to Will the same morning.** No trade, threshold, gate or capital implicated; $0 moved.

## The claim being corrected

PROME's boot diagnosis headlined: *"Two-thirds of the fleet's open work is PROME's — of 140 live pending docket rows, 95 name PROME."* **The headline does not follow from the sentence under it.** "Names PROME" is not "is PROME's work": the owners cell names registrars and consumer readers alongside implementers.

CATO measured 103 mentioning PROME against 48 listing it first. Re-measured here, independently:

| measure | count | of 142 live PENDING |
|---|---|---|
| owners cell **mentions** PROME | 97 | 68% |
| owners cell **lists PROME first** | 47 | 33% |
| PROME anywhere in owners **or catalyst** | 106 | 75% |

CATO's two figures reproduce within one row (its snapshot predates L451/L452). **Neither establishes sole ownership, and the 68% figure is roughly 2× the defensible one.**

## The three buckets

Classified on the clause naming PROME inside the owners cell, top-level `/`-split with parens respected.

| bucket | count | what it means |
|---|---|---|
| **A — receipt / consume** | 32 | PROME registers, carries, or does a consumer read. Often already satisfied at the owner's artifact; cheap to close |
| **B — implementation** | 48 | PROME owns a tool, repair, spec or encode. Real engineering |
| **C — unclear** | 17 | the clause does not say which |
| *(touches Will)* | *35* | *cross-cutting, not a fourth bucket — a row can be in A or B and still need his word* |
| not PROME at all | 45 | another desk's row |

⚠️ **MEASURED ERROR RATE, not assumed: a 12-row hand sample found 10 correct and 2 wrong — ~1 in 6.** The two misses show the direction of the error: **L414** (*"presents at the sitting; registers"*) was bucketed A when it is Will-gated and belongs with the Will rows, and **L358** (*"every item above is PROME-lane and PROME-owned"*) was bucketed C when it is plainly B. ⇒ **C undercounts B, and A can swallow a Will-gated row.** Treat the counts as a first cut with a stated error bar, never as a ledger. `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]` — a keyword scan over a prose cell is exactly the class that produced two of today's other errors.

## 🔑 The finding that survives the error bar

**The rows dated TODAY are not the cheap kind.** Of the 19 PENDING rows dated 2026-09-19:

| bucket | count | rows |
|---|---|---|
| **B — implementation** | **16** | L359 · L360 · L361 · L362 · L364 · L367 · L368 · L370 · L378 · L392 · L393 · L402 · L403 · L413 · L423 · L424 |
| A — receipt / consume | 2 | L350 · L414 (L414 is really Will-gated) |
| C — unclear | 1 | L358 (really B) |

⇒ **~17 of 19 of today's pile is PROME engineering work on PROME's own instruments** — gate legs, `argus_scope`, `spawn_list`, `fleet_dashboard`, `decision_deck`, `consumer_check`, the ORCH_LOG mechanisation. It is not a backlog of unread receipts that can be drained by reading.

**But fleet-wide the picture differs and that is the actionable half:** across all 142 rows, **32 of the 97 PROME-touching rows are bucket A** — about a third are registrations and consumer reads that may already be discharged at the owner's artifact. Those are closable by *reading*, not building, and PROME has never separated them from the engineering pile before attempting a triage.

## What this changes

1. ⛔ **The flat "triage the 19 rows dated today" plan PROME recommended to Will twice is the wrong first move.** Sixteen of them are engineering tasks; a triage pass cannot dispose of them, it can only re-date them, which is the row-clustering CATO and PROME both warned against.
2. ✅ **The right first move is the bucket-A sweep across all 142 rows** — check each of the 32 at the owner's artifact and close the ones already discharged. Cheap, mechanical, and it is the only lever that reduces the count honestly. Precedent: CRUISE discovered this morning it had carried a discharged L221 obligation for 17 days.
3. **Bucket B is a work queue, not a backlog** — it wants sequencing by consequence (gate legs before dashboards), not triage.
4. **Two rows dated today were closed by this session's own work** — L368 (`spawn_list` suppression) and part of L393's class are touched by the presence repair and the renderer compaction; they are NOT self-graded here. A consumer read at the artifacts is owed before either moves.

## Owed, named rather than implied

- The ~1-in-6 misclassification is **not** fixed; these buckets are a first cut.
- `docket_view.py --check` reports **4 pre-existing `[DATE]` flags** on SCRATCH (lines 11, 30 ×2, 54), unchanged by today's work. A DATE flag earns a full logic re-read of the artifact. Not done.
- DOCKET L446 — the independent read of the desk-cadence build whose column break caused the presence crash — remains owed.
