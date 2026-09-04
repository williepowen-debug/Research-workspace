# Registered-Gate Basis Sweep — playbook (WQ-162, Will 2026-09-02 21:29 "Approve WQ-162 with your recs")

**Registry row:** `sweeps/REGISTRY.tsv` "Registered-Gate Basis Sweep" (21d; `resolve_by` 2026-09-16 for run #1). **Ruling record:** `PROME/proposals/2026-09-02_wq162-RULED.md` item 4 (the fleet-sweep leg). **Canon this sweep enforces:** `FORGE/PREDICTION_DISCIPLINE.md` § Registration (name series · unit + conversion · vintage convention · operator/boundary · consecutiveness · reset, for EVERY observation the grade reads; a grade on an unnamed basis is NO-VERDICT) and, from 2026-09-03, `BLUEPRINTS/SPEC_LETTER_STANDARD.md` SL-5 (tie set: strictness + published precision + tie convention + base rate on the same operator + exit legs). Written 2026-09-03 — the registry row had pointed at this file for a day before it existed (`finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit`; `sweeps_due.py` reads the row, not the playbook — a candidate guard).

## When to run
Every 21d, or on demand after a gate letter is re-written or a new published-series gate registers. Run #1 by **2026-09-16**.

## Perimeter
Every gate in `PROME/GATES.tsv` (LIVE + FIRED-pending rows) whose condition is keyed to a **published series** (FRED, Trepp, DTN, CFTC, MOF, BLS, exchange closes …) — plus **pipelines and upsert keys** that GRADE such a gate (OTTO's 10-D/A case: the letter can be clean while the pipeline re-keys the observation). Level-triggers that are watched by `config.py` bands are in scope if a GATES row cites them. Out of scope: judgment gates (`scannable = JUDGEMENT`) and owned-elsewhere rows — list them as NOT GRADED with the reason, never skip silently.

## Procedure
### 1. Vintage-check (read-only, mechanical, observation-count form)
For each in-scope gate, COUNT the observations the grade reads (both endpoints of every delta · each day of a persistence condition · both series of a spread) and, per observation, check that the letter names: series (ticker, not concept) · unit + conversion · vintage convention (as-first-published vs latest-revised) · operator + boundary/strictness (+ published precision and tie convention, SL-5) · consecutiveness rule · reset rule. Record `named / unnamed` per element per observation. **A gate with any unnamed element on any observation = BASIS-UNNAMED** (its next grade is NO-VERDICT under canon).
### 2. Blind grade-read (a STRANGER briefed as the grader)
Hand the letter — and only the letter — to a reader who does not own the gate, briefed to GRADE it today from the named source. Their questions and mis-reads are findings the vintage-check cannot see (run #0 evidence: 8 defects found this way, 0 by the element count). Owner never grades own letter in this sweep (LIQUID's owner-sweep undercounted 4 of its own 5 gates).
### 3. Negative control on the retrieval path — REQUIRED before any "unrevised" verdict ships
Prove the retrieval path can distinguish vintages: fetch the same series at two vintage dates plus one INVALID date and confirm the payloads DIFFER. **Known false path:** FRED `fredgraph.csv?...&vintage_date=` returns HTTP 200 and silently ignores the parameter (OTTO `9cdd27494`: four URLs incl. an invalid date, identical sha256) — a sweep through it manufactures "unrevised" for every series. Use ALFRED (`api.stlouisfed.org/fred/series/observations?…&realtime_start=…`) or the vintage endpoint the source actually honors; if none exists, the verdict is CANNOT-CERTIFY, never "unrevised".
### 4. Base-rate operator check (SL-5, added 2026-09-03 — one-time leg for run #1, then standing)
For each gate carrying a base rate: was it computed on the SAME operator the letter carries (strict vs non-strict)? Positive control: RED FT-11 (strict base rate 5.0%/3.8% vs non-strict letter 8.5%/6.2%; tie atom 41% of fires). Mismatch = a dated re-registration ask to the owner, never a retroactive re-grade.

### 5. Revisable-series bare-number check (WQ-175 FROZEN-ON-REVISABLE, added 2026-09-04 — PROME "YES at your cadence" on my proposal; standing from run #1)
For each in-scope gate keyed to a series the issuer RESTATES (payrolls · GDP · JOLTS · QCEW · CPI seasonals · any series with a published revision schedule): the letter must carry the threshold as a FORMULA with a dated illustration and a recompute instruction (`… ⇒ X ≥ +303K [2026-09-02 vintage — RECOMPUTE on the revised vintage before grading]`), name the resolving vintage (FIRST PRINT · THIRD PRINT · BENCHMARKED), and register a REVISION WATCH. A bare number on such a series with no bracket beside it = `BASIS-UNNAMED (vintage)` and a dated re-registration ask to the owner. Forward-only: a letter registered before 2026-09-04 that named no vintage grades AS FIRST PUBLISHED (WQ-162) and is annotated, never re-graded. Canon: `FORGE/PREDICTION_DISCIPLINE.md` § Registration FROZEN-ON-REVISABLE; form: `BLUEPRINTS/SPEC_LETTER_STANDARD.md` Registration row.

## Verdict tokens (STATE_VOCABULARY)
per gate: `BASIS-NAMED` · `BASIS-UNNAMED (<elements>)` · `OPERATOR-MISMATCH` · `NOT GRADED (<reason>)` · retrieval path: `VINTAGE-PATH-VERIFIED` / `CANNOT-CERTIFY`.

## Disposition & authority
Detection read-only. Dispositions are TASK-PACKET-ONLY to the gate owner (re-writing a letter is domain judgment); PROME cc'd because GATES.tsv cells are PROME's. No pre-approval class.

## Record
`runs/<date>_GATE_BASIS_SWEEP_<n>.md` (perimeter · per-gate table · stranger's read verbatim · negative-control payload hashes · packets sent) → registry row `last_run` + `last_findings` → this Run Log.

## Run Log
| # | date | gates | BASIS-UNNAMED | OPERATOR-MISMATCH | stranger findings | notes |
|---|---|---|---|---|---|---|
| 0 | 2026-09-02 | 5 (LIQUID's, at dispatch) | 4 | — | 8 | pre-registration evidence in the WQ-162 packet; not a run of this playbook |
