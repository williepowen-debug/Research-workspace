# Eagle Bancorp (EGBN) research

**REGINALD's research entrypoint for Eagle Bancorp, Inc. / EagleBank (SEC CIK1050441). Organized and populated with copies October20,2026 at Will's request.** This is a subject folder within REGINALD, not a separate agent or revived sub-agent. Current desk judgment/scores remain in [REGINALD STATUS](../../STATUS.md); dates remain in [CALENDAR](../../CALENDAR.md).

## Start here

| Read | What it contains |
|---|---|
| **[October20 cash-recovery investigation](reports/2026-10-20_EGBN_cash-recovery_investigation.md)** | Latest investigation: four loan outcomes still unverified at its cutoff; extension/downgrade evidence, secondary July expectations, appraisal-table discrepancy, independent-record access limits and exact next-disclosure tests. |
| [October20 source audit](sources/2026-10-20_EGBN_cash-outcome/SOURCE_AUDIT.md) | Primary/secondary distinction, claim locators, property nonmatches, search coverage and access failures. |
| [EGBN loan-outcome extract](data/workbook/WORKOUT_OUTCOME_BRIDGE.tsv) | Existing EGBN case rows008/009/013/014 and portfolio rows006/007. Same-basis cash, loss, transfers and retained-exposure fields; UNKNOWN remains explicit. |
| [October13 cash/loss/valuation next-evidence note](context/2026-10-13_Q3_cash-loss-valuation_next-evidence.md) | How to translate an actual loan outcome into incremental earnings/book effects; historical capacity and conditional sensitivities. |

## Evidence and prior work

| Date | Material | Purpose / limit |
|---|---|---|
| Oct20 | [Raw source collection](sources/2026-10-20_EGBN_cash-outcome/), [request receipts](sources/2026-10-20_EGBN_cash-outcome/retrieval.json), [additional receipts](sources/2026-10-20_EGBN_cash-outcome/extra-retrieval.json) | SEC originals, slide images, filings, secondary transcript and record-access evidence. Failed responses are retained as failures; a login/player page is not records/audio. |
| Oct20 | [Calculator](sources/2026-10-20_EGBN_cash-outcome/calculate.py), [results](sources/2026-10-20_EGBN_cash-outcome/calculations.json) | Source hash verification, reported portfolio reconciliation and hypothetical recovery arithmetic. Scenarios are not loss forecasts. |
| Oct12 | [Cleanup figure verification](reports/2026-10-12_EGBN_cleanup_figure_verification.md), [verification receipts](sources/2026-10-12_EGBN_cleanup_verification/) | Verifies earlier claims about loan reductions, sales and recognition; preserves carrying-value versus cash distinctions. |
| Oct12 | [Workout-outcome bridge report](context/2026-10-12_workout-outcome-bridge.md) | Cross-bank accounting framework; dated Oct20 EGBN update appended. |
| Oct12 | [Apartment-loan candidate question](reports/2026-10-12_L694_EGBN_candidate-question.md) | Existing decision question and contrary evidence. Earlier prices/valuations are historical; no demonstrated pricing edge. Oct20 scope continuation appended. |
| Oct12 | [PROME EGBN/KRE checkpoint](reports/2026-10-12_PROME_EGBN-KRE_checkpoint.md) | Dated coordinator checkpoint; not a current quote or standalone trading instruction. |
| Sep27 | [Fairfax observability investigation](reports/2026-09-27_EGBN_fairfax_observability.md) | Identification/access constraints; Oct20 qualification corrects the earlier description of future issuer evidence as definitive. |
| Sep27 | [EGBN/VLY/PFBC news sweep](reports/2026-09-27_news_sweep_EGBN_VLY_PFBC.md) | Historical cross-bank news review; keep its evidence date. |
| Sep26 | [Detailed Q2 inputs](reports/2026-09-26_CRE_top3_dossiers/q2_EGBN.md), [EGBN dossier](reports/2026-09-26_CRE_top3_dossiers/dossier_EGBN.md) | Baseline collateral, credit grades, appraisals, reserves, accounting perimeters and scenario inputs. |
| Sep26 | [CRE top-three loss bridge](context/2026-09-26_CRE_top3_loss_bridge.md) | Cross-bank conditional loss scenarios and subsequent corrections; not actual realized losses. |
| Jul25 | [Q2 grade and regional watchcards](reports/2026-07-25_EGBN_Q2_grade_plus_FL_smalltier_watchcard_fill.md) | Historical release outcome. |
| Jul18 | [Frozen Q2 grading frame](reports/2026-07-18_EGBN_Q2_grading_frame.md) | Historical pre-release expectations; preserve rather than rewrite. |

## Unresolved cases at the October20 investigation cutoff

| Case | Existing workbook row | Evidence still needed |
|---|---|---|
| Prince George's apartments | WOB-REG-008 | Outcome/terms after extension; actual cash and its source; concessions, new advances, retained exposure and attributable new recognition. |
| Fairfax office | WOB-REG-009 | Outcome after maturity; borrower/property identification and matched cash/loss evidence. |
| Montgomery storage | WOB-REG-013 | Actual payoff versus secondary management expectation of payment by year-end; funding source and residual exposure. |
| Anne Arundel storage | WOB-REG-014 | Outcome after maturity; identification, cash and any loss/retained claim. |

The existing Q3 release/call/filing review owns these next observations. Timing is maintained in CALENDAR, not duplicated here. Absence from a future table alone is not evidence of repayment. No new standing monitor or research approval is created by this index.

## Files now stored here

| Folder / file | Contents |
|---|---|
| [reports/](reports/) | Ten EGBN reports and dossiers, copied verbatim. |
| [sources/](sources/) | Both EGBN source collections, including October12 local raw downloads and October20 originals, receipts and calculations. |
| [data/](data/README.md) | EGBN extracts from16 shared workbook tables and six dated market CSVs. |
| [context/](context/) | Six cross-bank studies supporting the EGBN work. |
| [peer-research/](peer-research/README.md) | Dated TERRY feasibility study, data and delivery packet. |
| [historical/](historical/README.md) | Frozen per-bank archive, separate from current findings. |
| [INVENTORY.json](INVENTORY.json) | Complete source-to-copy manifest, timestamps, hashes and extract selection details. |
| [verify_inventory.py](verify_inventory.py) | Verifies copy integrity and flags originals that have changed since capture. |

**Copies/extracts captured October20,2026:**140 files, including203 selected data rows. No original file was moved or altered by consolidation. These are dated snapshots; their observation dates remain unchanged. The source manifest identifies every original, including files outside REGINALD.

## Where to save future work

- Original dated reports and sources retain their established homes. After substantive EGBN work, explicitly refresh the relevant folder copies/extracts and manifest so this folder stays useful; do not silently treat an old snapshot as updated evidence.
- Update the existing loan-outcome workbook rather than create a second case ledger. Keep original expectation dates, source vintages and outcome qualifications.
- This folder now contains physical copies as well as the index. Originals remain authoritative; run the inventory verifier to detect drift. Relative references inside verbatim report copies retain their original context; use the manifest for original locations.
- [The copied old per-bank EGBN folder](historical/per-bank/) is **historical and frozen**. Its retired thesis, figures and position records are not current research or broker truth.

Organization only; no new economic evidence, score, forecast, threshold or trade change. Re-check links whenever adding or moving a source.
