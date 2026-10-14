# REGINALD workbook

Closeout inventory checked October14,2026. Current desk judgment and prices live in `../STATUS.md`; these files retain their own observation dates. A recent commit or header does not refresh older rows.

| Files | Purpose / handling |
|---|---|
| `KB.tsv` | Curated evidence and source references. Each row retains its source date and verification scope. |
| `VX.tsv` | Vector observations and existing bands. Refresh only rows supported by newly retrieved evidence; STALE/RETIRED rows remain explicit. |
| `PREDICTIONS.tsv` | Registered expectations and original grading authority. Update only on eligible outcomes; preserve Kernel-pinned rows. A boot is not a reason to regrade probabilities. |
| `WORKOUT_OUTCOME_BRIDGE.tsv` | Existing21-row cash/recovery/recognition bridge. Append outcomes at the already-assigned disclosures; missing cash, retained exposure and loss allocation remain unknown. |
| `CRE_RCN_COHORT.tsv`, `MI3_COHORT.tsv`, `ACL_ROLLFORWARD_COHORT.tsv`, `RUNWAY_COHORT.tsv`, `NDFI_COHORT.tsv` | Dated quarterly Call Report evidence. Refresh under each existing cadence and `../CALENDAR.md`; no new pull to make an old quarter look current. |
| `AOCI_COHORT_2026Q2.tsv`, `FUNDING_COHORT_2026Q2.tsv` | Fixed Q2 baselines for already-defined comparisons. New October13 screen artifacts are in `../domain/sources/2026-10-13_bounded-securities-screen/`, not silently substituted into these baselines. |
| `FLOW.tsv`, `OPTIONS_OI.tsv`, `DARKPOOL.tsv`, `SHORT_VOL.tsv`, `SHORT_INTEREST.tsv` | FROZEN historical records. Do not append, grade from them as current or revive automatically. Boot writers now honor the three market-feed freeze banners. |
| Other workbook Markdown | Research/navigation or explicitly historical snapshots; follow their banners and the desk’s canonical owner pointers. |

The exit-close count lives in `../registry/REG_T02_EXIT_LOG.tsv`. Routed-signal dispositions live in `../board/BOARD_LOG.tsv`. The14-bank compound-risk join and primary-cell audit live in `../domain/sources/2026-10-14_compound-risk/`; they are a one-time research result, not a new monitor.

This closeout checked column counts across all16 workbook TSVs and found no malformed rows. Active updates are limited to retrieved price/spread observations, the eligible settled-close log and the coordinator evidence receipt. Frozen predicates, scoring, quarterly vintages and trade authority retain their existing rules. Recheck the inventory after any schema or ownership change.
