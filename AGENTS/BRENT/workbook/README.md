# BRENT workbook — start here

Reconciled September 8, 2026. This is navigation and maintenance guidance, not another copy of market figures or trading rules. Supersedes the assumption that every TSV in this folder is a maintained research ledger. Existing file ownership is unchanged.

## What is maintained here

| File | Role | What an update means |
|---|---|---|
| [REGISTRY.tsv](REGISTRY.tsv) | Machine thresholds consumed by `thresholds.py`, plus instrument enrollments used by `instrument_check.py` | A rule/instrument record. Its `last_verified` dates are not a blanket market refresh. Complete letters remain at each `spec_home`. |
| [LESSONS_INDEX.tsv](LESSONS_INDEX.tsv) | Machine index of [LESSONS.md](../LESSONS.md) | Reconcile both together when a lesson changes. Text verification is distinct from source-data freshness. |
| [LEDGER_GLOB](LEDGER_GLOB) | Declares the existing ledger-check perimeter, including live files outside this folder | Schema/configuration maintenance; it does not contain observations. |
| [TRADE_OBLIGATIONS.md](TRADE_OBLIGATIONS.md) | Dispositions and complete decision-reader paths | Rule migration inventory. For current holdings or actions, start at [TRADE.md](../TRADE.md). |
| [TRADE_CLAUSES.json](TRADE_CLAUSES.json) | Exact preserved trade-excerpt hashes and destinations | Provenance from the September 8 migration; retain the original source line ranges. |

The registry does not implement every BRENT grade. EIA routines still have constants in `scripts/eia_weekly.py`; prediction and trading rules have their own named readers. A blank numeric field is not proof a test has been automated.

## Where to read and update current research

| Question | Canonical destination |
|---|---|
| What does BRENT currently think? | [THESIS.md](../thesis/THESIS.md) |
| What are the dated physical/market readings? | [STATUS.md](../STATUS.md); [demand tracker](../demand_destruction/TRACKER.md) owns its routine alert block |
| What predictions are open, and how are they graded? | [PREDICTIONS.tsv](../thesis/PREDICTIONS.tsv), every field plus the linked complete prediction note |
| What position/action is recorded? | [TRADE.md](../TRADE.md), then its complete decision paths; broker receipts govern execution |
| What is due next? | [CATALYSTS.tsv](../docket/CATALYSTS.tsv); STATUS calendar is generated from it |
| What happened to energy infrastructure? | [INCIDENTS.tsv](../refinery_damage/INCIDENTS.tsv), with each event's source/date and restart uncertainty; not a summable outage table |
| What did the last research passes establish? | [Catch-up report](../research/2026-09-08_catchup/REPORT.md), [batch 2 report](../research/2026-09-08_batch2/REPORT.md) |
| What still needs work? | [SCRATCH.md](../SCRATCH.md); evidence gaps stay at the relevant mandatory reader |
| What can other agents consume? | [NEXUS_BRIEF.md](../NEXUS_BRIEF.md), with its scoped freshness boundary |
| Which incoming packets were consumed? | [board_log.tsv](../board_log.tsv) plus `inbox/processed/` |

## Historical files in this folder

**KB.tsv, VX.tsv, FLOW.tsv and GROUP_MAP.tsv are frozen history.** Their old ACTIVE cells, estimates, routing references and maintenance instructions are historical too. Do not populate them with the latest research or treat their old successor wording as current navigation. The current owners are above. Preserving the files keeps provenance and existing archive links intact.

[SCHEMA.tsv](SCHEMA.tsv) describes that old KB format, not the live registry, predictions or incidents. [PILOT_STATE_REPLACEMENT_MEASUREMENT.md](PILOT_STATE_REPLACEMENT_MEASUREMENT.md) records the August pilot; its “now” values and historical findings are dated to that experiment. The `STATUS_archive*` and `NEXUS_BRIEF_archive*` files are also history.

[CLEANUP_VERIFICATION.json](CLEANUP_VERIFICATION.json) is the earlier cleanup's immutable test receipt, not today's health dashboard. Later evidence is [RECONCILIATION_2026-09-08.json](RECONCILIATION_2026-09-08.json). Neither receipt promises future checks remain green.

## What this reconciliation repaired

- Repaired registry `spec_home` links and normalized consumer-document paths to paths relative to BRENT.
- Moved two long historical amendments out of `consumer_scripts` into `notes`, preserving their text.
- Added the saved LMA, SPR-authority and invalid-FRED-ID corrections to the relevant registry rows, preserving dated originals and retirement states.
- Marked three existing probes `component_only`: diesel crack probes HO alone, WTI–Brent probes CL alone, and tanker liveness probes STNG alone. The existing instrument check now reports `PARTIAL_COVERAGE` even when that component is fresh. This extends the existing check; it does not change a threshold or authorize a trade.
- Verified the preserved trade excerpts and the next ordinary closeout's file-growth check. Original archived files and numerical trading rules were retained.

## What remains evidence work

The original BRT-12 futures construction and upstream E&P credit history, BRT-29's full carrier-event evidence, current incident/restart estimates and specified flow observations still need source work. September 9–11 scheduled releases retain their own publication dates. The November-contract diagnostic cannot replace the original prediction instrument.

The workbook is reconciled structurally; its source gaps are visible. A healthy individual feed, a fresh file timestamp or this reconciliation does not establish that a full multi-part measurement is available.
