# Gold research and data

Gold and GLD research, real-yield sensitivity, official buying, ETF bullion flows and positioning.

This folder is the topic entry point. [STATUS](../STATUS.md) owns current state; [THESIS](../THESIS.md) owns mechanisms and standing rules; [PREDICTIONS](../workbook/PREDICTIONS.tsv) owns forecast letters. The links below are dated artifacts, not independent live summaries.

## Knowledge base

[KB.tsv](KB.tsv) contains gold entries from the [permanent MIDAS KB](../workbook/KB.tsv). This is a generated view: original IDs, sources, dates, confidence and historical corrections are preserved. Paired-metal findings appear in each relevant metal's KB and in shared. Edit the permanent ledger and [metal tags](../KB_METALS.tsv), then refresh; do not edit this view directly. [Maintenance instructions](../README.md#knowledge-bases). Current judgments remain in STATUS.

## Research and interpretation

- [Gold COT vintage #3 — GRADE (as-of Tue 2026-08-25, released Fri 2026-08-28 15:30 ET)](../analysis/2026-08-28_cot3-grade.md)
- [MIDAS-06 — PROVISIONAL READ (Fri 2026-08-28) + Gold COT #3 pre-registration](../analysis/2026-08-28_midas-06-provisional-read-and-cot3-prep.md)
- [Row 66 — DFII10 NO-VERDICT band: DESIGN DRAFT](../analysis/2026-08-28_row66-noverdict-band-DESIGN-DRAFT.md)
- [MIDAS-06 — TERMINAL GRADE: **(a) DIVERGE PERSISTS**](../analysis/2026-08-31_midas-06-TERMINAL-GRADE.md)
- [MIDAS-08 — REGISTRATION: the M1 successor test. Did the crowded gold spec long unwind into a −6.35% week?](../analysis/2026-09-02_MIDAS-08-registration-m1-cot-successor.md)
- [MIDAS-08 — TERMINAL GRADE: **(b) INDETERMINATE.** M1 holds 4. The conditional did NOT trigger.](../analysis/2026-09-05_MIDAS-08-GRADE.md)
- [MIDAS — VECTOR 3: is GLD the wrong hedge under an oil-shock / real-yield regime?](../analysis/2026-09-11_VECTOR-3-gld-under-an-oil-shock-real-yield-regime.md)
- [MIDAS — expanded M1 conditional reference](../analysis/2026-10-12_M1-expanded-reference.md)
- [M1 successor — preferred prospective DRAFT](../analysis/2026-10-12_M1-successor-DRAFT.md)
- [GLD outlook after the rate and bullion flow review](../analysis/2026-10-20_GLD-OUTLOOK.md)
- [WQ-451 — gold decomposition letter: haven vs de-dollarisation vs liquidation (2026-10-23)](research/2026-10-23_WQ451-decomposition-letter.md) — instrument in `sources/2026-10-23_wq451/`; includes the GLD outlook invalidation lines (§5).
- [MIDAS catch-up, 2026-10-23: the 10/22 liquidation day, flip-rule status, COT](../shared/research/2026-10-23_catch-up.md) — shared with all metals.
- [Gold and silver news sweep, 2026-10-23: Russia CB selling, estimated vs reported CB buying, China deleveraging](../shared/research/2026-10-23_gold-silver-news-sweep.md) — shared with silver.

**Open gold forecasts (registered; letters live in [PREDICTIONS](../workbook/PREDICTIONS.tsv)):** MIDAS-11 (11/20) · MIDAS-12 (2027-01-20) · MIDAS-13 rebound touch $378.95 (11/20) · MIDAS-16 COT as-of 10/27 (~10/30) · MIDAS-17 rate catch-up (11/20) · WQ-451 tests DOCKET L819–L822 (11/06 → early December). Grade status is in PREDICTIONS, not here.
- [MIDAS — THE 8/19 GOLD SESSION: RATES ATTRIBUTION WRITE-UP](../reports/2026-08-23_gld-rates-attribution.md)

## Data and sources

- [sources/2026-10-12_m1-draft](../sources/2026-10-12_m1-draft) — Dated material; inspect its source dates and approval status.
- [sources/2026-10-12_m1-expanded](../sources/2026-10-12_m1-expanded) — Dated material; inspect its source dates and approval status.
- [sources/2026-10-20_GLD-review](../sources/2026-10-20_GLD-review) — Dated material; inspect its source dates and approval status.
- [sources/2026-10-23_wq451](sources/2026-10-23_wq451) — WQ-451 instrument code, panel and outputs; frozen 2026-10-23 before forward grades.
- [shared/sources/2026-10-23_catch-up](../shared/sources/2026-10-23_catch-up) — Treasury curves, GLD issuer archive, vendor bars (10/23 capture).
- [shared/sources/2026-10-23_predictions](../shared/sources/2026-10-23_predictions) — base rates for MIDAS-13..17.
- [sources/cot_gold_history_2010_2026.tsv](../sources/cot_gold_history_2010_2026.tsv) — Frozen positioning reference; preserve bytes and grading basis.
- [sources/cot_vintages_consumed.tsv](../sources/cot_vintages_consumed.tsv) — Append-only consumption record used by boot; do not move or duplicate.

## Shared studies and source bundles

- [MIDAS — BOTH REMAINING OPEN PREDICTIONS ARE KEYED TO REFERENTS THAT HAVE MOVED](../analysis/2026-08-27_registered-specs-keyed-to-moving-referents.md) — shared with copper.
- [MIDAS-01 + MIDAS-02 — RESOLVED 2026-10-01 on their FROZEN LETTERS, every basis printed](../analysis/2026-10-01_MIDAS-01-02-RESOLUTION.md) — shared with copper.
- [MIDAS — news sweep, October12,2026](../analysis/2026-10-12_MIDAS-news-sweep.md) — shared with silver, platinum, palladium, copper.
- [MIDAS — due metals review and held GLD — 2026-10-12](../analysis/2026-10-12_due-metals-review-held-GLD.md) — shared with silver, platinum, palladium, copper.
- [Precious metals news and implications as of October 20 2026](../analysis/2026-10-20_PRECIOUS-METALS-NEWS.md) — shared with silver, platinum, palladium, copper.
- [MIDAS — Domain Sweep (4-lens), 2026-07-12](../archive/reports/2026-07-12_domain-sweep.md) — shared with silver, platinum, palladium, copper.
- [2026-10-12_maintenance](../sources/2026-10-12_maintenance) — shared with silver, platinum, palladium, copper.
- [2026-10-12_news-sweep](../sources/2026-10-12_news-sweep) — shared with silver, platinum, palladium, copper.
- [2026-10-12_review](../sources/2026-10-12_review) — shared with silver, platinum, palladium, copper.
- [2026-10-20_news](../sources/2026-10-20_news) — shared with silver, platinum, palladium, copper.

## Filing new work

Put new gold-specific writeups in `gold/research/` and supporting captures/calculations in `gold/sources/YYYY-MM-DD_topic/`, relative to MIDAS. Keep reports and evidence linked. Classify evidence by prices, positioning, investment flows, physical stocks, supply, demand, and macro context when relevant; create subfolders when material exists.

Put inseparable multi-metal work in [shared](../shared/README.md), once, and link it from every relevant metal. Existing `analysis/`, `reports/` and `sources/` paths remain valid for scripts, frozen references and peer citations. Add new artifacts to [METALS_CATALOG.tsv](../METALS_CATALOG.tsv) and this index. Do not create separate copies of STATUS, forecast ledgers, source registers or shared datasets.

- [Sunday October 25 catch-up and assignment reconciliation](../shared/research/2026-10-25_sunday-catch-up.md) — dated prices, source limits, completed PRD3 correction and next owner work.
