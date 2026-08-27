# Gate C Checkpoint C5 — Bounded Native Record Inspection

**Date:** 2026-08-26

**Authorization:** Will authorized bounded read-only C5 inspection.

**Status:** CANDIDATE SELECTED — OPERATOR APPROVAL AND NATIVE COMPANION REQUIRED

## Inspection perimeter

Only the known canonical SAM prediction ledger named in repository documentation
was inspected:

```text
source_commit: 7395352da0ff1e8b68b92dd3281b98b4427da0c5
path: AGENTS/SAM/thesis/PREDICTIONS.tsv
locator_type: TSV_RECORD_ID
locator: Pred_ID=SAM-33
selected_row_sha256: 3c306e845447193698076d12e45325bb118b12d7d7fab2b972589f08705a0fbe
whole_blob_sha256: 99fb21faf4a1c8abd9dffbcc9b8bce5d3051a6aa03fccfa854bb681afe2a52c4
row_width: 9 fields, matching the committed header
```

No submission directory was scanned. No command, event, receipt, policy,
activation, projection, or registered view was created from this record.

## Bounded candidate comparison

The open rows visible in the inspected ledger were narrowed to three binary
candidates:

| Record | Mark | Assessment |
|---|---:|---|
| SAM-28 | 40% | Reject for first pilot: multi-route union and payoff condition add avoidable interpretation |
| SAM-31 | 35% | Reject for first pilot: “genuine VIX-spike regime” requires a judgment-heavy episode classifier |
| SAM-33 | 72% | Recommend: one actor, one explicit horizon, activated falsifiable condition, and stable binary outcome |

## Recommended record

**SAM-33** forecasts that through December 31, 2026 the BOJ will not deploy an
emergency or unscheduled long-end capping operation to cap a gradual super-long
JGB yield rise. The ledger states the material-stress precondition has already
been met and names the falsifier: an unscheduled fixed-rate operation or increase
in JGB purchases explicitly aimed at a gradual rise. A response to a genuinely
disorderly spike is excluded.

This is the least ambiguous candidate in the bounded set, but it is not yet
native-complete for the Kernel contract.

## Read-only preflight

| Check | Status | Finding |
|---|---|---|
| Exact commit/path/row | PASS | Full commit resolves; one nine-field `SAM-33` row selected |
| Binary family | PASS | Forecast is a binary no-operation-by-horizon claim |
| Probability | PASS | `72%` maps mechanically to `0.72` |
| Open state | PASS | Committed row is `OPEN` |
| Stable horizon | PASS WITH PRECISION GAP | Date is December 31, 2026; exact UTC close instant is absent |
| Material Question terms | EXCEPTION | Ledger lacks registered IDs, precise opens/closes, resolver assignments, complete source/fallback rules, ambiguity and annulment rules, and negative-search procedure |
| Material Forecast terms | EXCEPTION | Ledger lacks a precise information cutoff and registered rationale/evidence references required by the strict command |
| Aggregate | EXCEPTION | Exact row is suitable, but no accepted command can be built faithfully from this row alone |

No required check is silently `UNKNOWN`; the two completeness failures are known
and blocking.

## Required native companion

If Will approves SAM-33, SAM—not PROME—must author and commit one strict JSON
native companion under SAM's normal owned path. It must register, without changing
the forecast thesis:

- stable Question and Forecast identifiers;
- precise `opens_at`, `closes_at`, and `information_as_of` UTC timestamps;
- the exact binary resolution condition and gradual-vs-disorderly discriminator;
- primary and fallback resolution sources;
- ambiguity, annulment, and negative-search rules;
- resolver and independent verifier actor IDs;
- rationale and evidence references; and
- intervention stage and decision consequence.

The later command must cite both the exact `SAM-33` TSV row and exact JSON Pointer
selections from that committed companion. PROME may check fidelity but may not
invent or fill SAM's missing research terms.

## Operator decision

Approve **SAM-33** as the C5 pilot record and authorize preparation of a bounded
SAM-owned native companion. This approval would not accept a command, activate
the carve-out, or start live shadow operation. The companion must return for exact
read-only preflight before C5 can close.
