# ACCEPTANCE CONDITIONS — presence reader / spawn_list producer contract
**Written 2026-09-19 18:1x ET, BEFORE any edit** (WQ-229). Author: PROME. Class: **CONSEQUENTIAL** — the check runs inside `prome_gate.py boot`, so an independent reader devising its own counterexample is required before this is called fixed.

## The defect, in its own terms — not the symptom

The reported symptom is `ValueError: too many values to unpack (expected 7)`. That is too narrow: repairing it means widening one unpack, and the same break returns on the next column.

**The property that was violated:** *a downstream reader of `spawn_list.collect()` must survive the producer gaining a field, and when the reader cannot run, the boot summary must say the CHECK FAILED — never render it as the evidence-unavailable verdict a healthy run produces.*

**How it arose:** `40aed8915` (the desk-cadence wire, ruled WQ-269) took `collect()` from 7 fields to 8. ⛔ **DATE CORRECTED 2026-09-19 22:1x ET by the independent reader — this document first said "the 2026-09-14 desk-cadence wire" and that is WRONG by five days.** `git log -1 --format=%as 40aed8915` → **2026-09-19**, 12:08:59 -0400. The break therefore lived for about **4 hours 38 minutes**, from that commit to the 16:46 boot that hit it — not five days. ⚠️ The wrong date had already propagated into the reader's own brief and into PROME's report to Will (*"an instrument broke yesterday"*); both are corrected. ⚠️ **And the field was INSERTED at index 6, not appended** — `catalyst` moved from 6 to 7, which is what breaks an index reader that a true append would not have. `session_presence.report()` positionally unpacks 7. The producer's own consumers were not enumerated when the column landed — the WQ-229 "test the NEIGHBOURS" step, missed on a build whose independent read (DOCKET L446) is still owed.

## Acceptance conditions

| # | Condition | Falsified by |
|---|---|---|
| **A1** | The check runs to completion against the REAL due-row set and emits one `runtime_evidence` line per due row. | any traceback; a short row count |
| **A2** | Adding a field to `collect()` does NOT break this reader. The reader must not positionally unpack the producer's full row. | injecting a 9-field row and getting an exception |
| **A3** | The boot summary DISTINGUISHES *check failed / could not run* from *check ran, evidence unavailable*. These must not render identically. | a crash and a stale snapshot producing the same verdict text |
| **A4** | A genuinely stale/foreign/undated snapshot still reports UNKNOWN **with its reason**. The repair must not convert a real unknown into a pass. | a stale snapshot returning rc 0 / no warning |
| **A6** | An **import-time** failure reaches the same DID-NOT-RUN state. `guarded_main()` cannot catch what is raised while the module loads, so the local imports are guarded. | moving a dependency away and getting rc=1 |
| **A7** | ⛔ The gate's did-not-run rendering keys on the **MARKER**, never on `rc==2`. `CHECK_STANDARD` §9 (RATIFIED) defines rc 2 as **cannot-certify**; `spawn_list.py:322` returns 2 from a run that COMPLETED with UNKNOWN rows, and `docket_view` · `willq_view` · `position_agreement_check` all have rc-2 paths. | a completed cannot-certify run rendering as "DID NOT RUN" |
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

---

## Amendment 2026-09-19 22:2x ET — what the independent reader found, and why A6/A7 exist

The reader returned **3 ❌ / 6 ⚠️ / 6 ✅** and every finding was constructed and run, not re-run from this suite.

- **❌1 → A7.** The first repair relabelled *every* `rc=2` in `prome_gate.run_script` as "DID NOT RUN (UNKNOWN execution — establishes nothing)". That **moved the collision instead of removing it** and broke a RATIFIED contract: `CHECK_STANDARD` §9 sets `0 clean · 1 findings · 2 cannot-certify`, and §9's contract-change discipline requires surveying **every rc-keyed consumer in ONE batch before** changing an rc contract. Neither was done. The reader's fixture rendered "establishes nothing" directly above a live WQ-184 Tier-1 spawn candidate. ⇒ the marker channel is now authoritative and rc is left alone.
- **❌2 → A6.** `guarded_main()` sits inside the module, so an import-time failure never reached it; the reader moved `scripts/docket_view.py` away — the exact event `spawn_list.py:71` annotates "fail LOUD if it moves" — and got rc=1, indistinguishable from a stale snapshot.
- **❌3.** The five-day date error above.
- **⚠️ accepted:** the last positional `r[3]` in `main()` is gone; the `Row` docstring now records that `cadence` was INSERTED at index 6 rather than appended; and the reader's point that **this suite never imports `prome_gate`, so A3 was verified at the wrong artifact** is the reason ❌1 got through at all — `[[finding_instrument_reports_clean_against_the_wrong_reference]]`.
- **⚠️ carried, not fixed:** `_field()`'s `str()`/`getattr` coercion traps, and a non-`Row` row of the wrong width yielding a silent wrong column at rc=0. Declared residue, not repaired this session.
- **Category 5 revisited:** the reader accepts the N/A for *row shape* and rejects it for the *rc contract* — `spawn_list.py:123` names index.lock contention during concurrent commits as a realistic route into the rc=2 state that ❌1 mislabelled. **The N/A was right about the question asked and wrong about the question that mattered.**
