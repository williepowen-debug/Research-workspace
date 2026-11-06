# CORAL -> DAEDALUS: add CORAL's new prediction ledger to the scorecard registry

**Date:** 2026-11-06. **Priority:** 🟡. **Requested by:** Will, 11:29 ET in CORAL's window.

**Fact:** `AGENTS/CORAL/workbook/PREDICTIONS.tsv` was created 11/06 on the fleet header, holding CORAL-01 to CORAL-04 (WQ-596). PROME registered the DOCKET rows L1047 to L1050. `AGENTS/DAEDALUS/scorecards/LEDGERS.tsv` has 0 CORAL rows, and `PROME/tools/forecast_report.py` builds its perimeter from that file plus its `EXTRA` list, so the monthly report will not read CORAL's ledger.

**The row, same shape as AEOLUS's line 5:**

`AGENTS/CORAL/workbook/PREDICTIONS.tsv	Status	Date_Resolved	COLUMN	Outcome	LIVE`

**Also stale:** `forecast_report.py`'s printed note says CORAL has no ledger (`PROME/reports/2026-11-05_forecast-report-1.md:66` carries it). That report is a dated record; the tool is PROME's. I name it only so the next run reads true.

ACTION: DAEDALUS adds the row to `scorecards/LEDGERS.tsv`, its own file. CORAL edited nothing there. No figure, grade or rule changes. Reply only if the row should differ.
