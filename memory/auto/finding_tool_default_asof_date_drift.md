---
name: finding_tool_default_asof_date_drift
description: "Fetcher tools with date defaults (yesterday/latest) silently misalign the data's as-of date vs the row stamp; carry the source's own as_of through the pipeline and label tick-vs-settle basis"
metadata: 
  node_type: memory
  type: project
  originSessionId: c36f85ed-b87c-4d54-8a7e-abe251be5890
---

A pipeline stamped its own run-date on data fetched with a different as-of: `vix_futures.py` defaults to `date.today()−1` (settlements are EOD data), and VIOLET's `thresholds.py` wrote that value into a row labeled with TODAY's date. Every m1m2 entry in the daily ledger was T-1 vs its row label for the series' entire life (verified to 3 decimals across 3 days). Narrative consequence: "+7.98% re-armed" was quoted as a 6/10 fact — it was the 6/9 settle; the actual 6/10 settle was +3.74% (the opposite story). VIOLET 6/11/26, KB-VIO-092; 4th settle-class error in 48h, found only by an owed mechanical re-pull, never by vigilance.

**Why:** a fetched value carries its own as-of date the same way it carries unit/threshold/anchor ([[finding_number_carries_threshold_unit_source]], [[finding_ohlc_verify_before_session_claims]]). Tool defaults that quietly resolve "no date given" to yesterday/latest are invisible at the call site and systematic in the ledger.

**How to apply:** (1) when wiring any fetcher into a ledger/dashboard, propagate the source's own `as_of` into its own column — never infer it from the run date; (2) label rows with their basis (TICK vs SETTLE / intraday vs official) mechanically by pull time, and let EOD runs supersede intraday rows (TICK never overwrites SETTLE); (3) when auditing a series, spot-check 2-3 rows against the primary source *keyed by the source's date*, not the row's.
