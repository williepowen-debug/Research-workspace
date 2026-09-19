# ACCEPTANCE CONDITIONS — presence reader / spawn_list producer contract
**Written 2026-09-19 18:1x ET, BEFORE any edit** (WQ-229). Author: PROME. Class: **CONSEQUENTIAL** — the check runs inside `prome_gate.py boot`, so an independent reader devising its own counterexample is required before this is called fixed.

## The defect, in its own terms — not the symptom

The reported symptom is `ValueError: too many values to unpack (expected 7)`. That is too narrow: repairing it means widening one unpack, and the same break returns on the next column.

**The property that was violated:** *a downstream reader of `spawn_list.collect()` must survive the producer gaining a field, and when the reader cannot run, the boot summary must say the CHECK FAILED — never render it as the evidence-unavailable verdict a healthy run produces.*

**How it arose:** `40aed8915` (the 2026-09-14 desk-cadence wire, ruled WQ-269) added a 7th element to each row, taking `collect()` from 7 fields to 8. `session_presence.report()` positionally unpacks 7. The producer's own consumers were not enumerated when the column landed — the WQ-229 "test the NEIGHBOURS" step, missed on a build whose independent read (DOCKET L446) is still owed.

## Acceptance conditions

| # | Condition | Falsified by |
|---|---|---|
| **A1** | The check runs to completion against the REAL due-row set and emits one `runtime_evidence` line per due row. | any traceback; a short row count |
| **A2** | Adding a field to `collect()` does NOT break this reader. The reader must not positionally unpack the producer's full row. | injecting a 9-field row and getting an exception |
| **A3** | The boot summary DISTINGUISHES *check failed / could not run* from *check ran, evidence unavailable*. These must not render identically. | a crash and a stale snapshot producing the same verdict text |
| **A4** | A genuinely stale/foreign/undated snapshot still reports UNKNOWN **with its reason**. The repair must not convert a real unknown into a pass. | a stale snapshot returning rc 0 / no warning |
| **A5** | The tool's standing guarantees are unchanged: never asserts absence, never grants spawn authority, `spawn_authorized` stays `False`. | any row claiming a desk is offline, or `spawn_authorized: true` |

⛔ **A3 is the condition the reported symptom would not have produced.** On 2026-09-19 the gate printed the traceback AND assigned the same `UNKNOWN: snapshot is stale…` verdict a healthy-but-stale run gives. Fixing only the unpack would leave a crashed check indistinguishable from a working one.

## The five neighbour categories — CONSIDER, with justified N/A

| # | Category | Disposition |
|---|---|---|
| 1 | **Ordinary** | **TEST.** Real due rows + a well-formed fresh snapshot → complete output, rc 0. |
| 2 | 🔴 **Overlap** | **TEST — and it is today's actual state.** The crash AND a stale snapshot were true *simultaneously*; the stale-snapshot path masked the crash in the summary line. An input in two failure states at once must report BOTH, neither masking the other. |
| 3 | **Wrong owner** | **TEST.** A due row owned by `WILL` / `?` must not yield desk evidence or crash. `main()` filters these for the desk overview but `report()` iterates `rows` directly — the filter is not in the path under repair. |
| 4 | **Missing information** | **TEST.** Snapshot missing `observed_at` / `host` / `codex`; and an EMPTY due-row set. Must fail LOUD, never silently drop rows and never silently claim coverage. |
| 5 | **Concurrent activity** | **N/A, justified.** The producer/consumer row shape is independent of how many sessions are live; concurrency affects which sightings `session_bridge` returns, not the contract under repair. The tool already refuses to infer absence (A5), which is the concurrency-sensitive claim. |

## What passing this establishes

**IMPLEMENTED** and **TESTED** against the above. **NOT INDEPENDENTLY VERIFIED** until a reader who did not write the fix devises at least one counterexample of its own. `[[finding_adoption_is_not_validation]]`
