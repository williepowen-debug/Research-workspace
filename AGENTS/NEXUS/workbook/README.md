# NEXUS workbook

**Latest snapshot: November 4 catch-up**, materialized 2026-11-04T15:35:05-05:00. [Evidence](EVIDENCE_2026-11-04.tsv), [test readings](TEST_READINGS_2026-11-04.tsv), [conditions](CONDITIONS_2026-11-04.tsv), [manifest](MANIFEST_2026-11-04.json). L16 UP and M07 DOWN grades are recorded; L13 and future windows remain open. Source and observation cutoffs differ by row; carried filing-dependent evidence retains its old cutoff. [Current report](../research/2026-11-04_catchup/REPORT.md). These are frozen snapshots; STATUS/PREDICTIONS remain authority. The November2 files below are preserved history.

Dated working tables for the November 2 transmission report. **These are frozen report snapshots, not live market readings or separate forecast ledgers.** The source report read data at 2026-11-02T10:00:13-05:00. Each row retains its observation date, basis and source; unknown values remain distinct from measured zero. No new threshold, probability or duty is introduced.

| Table | Contents |
|---|---|
| [EVIDENCE_2026-11-02.tsv](EVIDENCE_2026-11-02.tsv) | Credit, yields, funding, breadth and bank-panel evidence; units and source limits |
| [TEST_READINGS_2026-11-02.tsv](TEST_READINGS_2026-11-02.tsv) | Existing test readings, counts, no-fire results and unresolved prediction coverage |
| [CONDITIONS_2026-11-02.tsv](CONDITIONS_2026-11-02.tsv) | Open evidence conditions and the recovered T7 grade, with existing owner/resolver dates |

Current synthesis lives in [STATUS.md](../STATUS.md). Live prediction state and frozen-letter pointers live in [PREDICTIONS_MONITOR.md](../PREDICTIONS_MONITOR.md); confirmed historical results live in [CONFIRMED.md](../CONFIRMED.md). Dated source artifacts remain in [the report folder](../research/2026-11-02_transmission-update/REPORT.md), including GRADES.json and raw pulls. The original L16 first-read ledger stays in [analysis/WQ342_grading_log.tsv](../analysis/WQ342_grading_log.tsv).

TSV format: skip lines beginning `#`, then read the tab-separated header. Blank quantitative cells have an explicit value/count state. `MEASURED` includes observed zero; `UNKNOWN` means unavailable at the stated report cutoff. Rows have different units and populations; their numeric columns are not summable. The observation-count field is not a coverage denominator: PRED-38's count is qualifying banks under incomplete coverage. Only L13/L16 carry complete post-anchor counts here; other run fields are not tabulated, as their state explains.

The first-line FROZEN banners are recognized by the existing fleet ledger-staleness tool. No new checker or automatic refresh was added.
