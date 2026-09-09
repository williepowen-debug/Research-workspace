# September 9 source package

This directory supports `../../../reports/2026-09-09_followthrough.md` and the September 11/18 docket packets. Run `analyze.py` from SAM with the repository venv to reproduce the captured-data calculations; it writes research artifacts only, never live ledgers or grades.

- `source-manifest.json`: first official-source collection, with successful hashes and failures.
- `market-manifest.json`: named vendor symbols, row counts, retrieval times and quote metadata. Raw CSV date labels preserve vendor timezones; daily labels do not synchronize markets.
- `followup-manifest.json`: corrected BOJ links and existing FRED-client receipts. FRED rows later than the matched September 8 comparison were not used.
- `broker-manifest.json`: first broker download receipts. `broker-final-manifest.json` is the authoritative manifest for the final broker files after the expanded follow-up; the dynamic Ueda HTML was retrieved again and its hash changed. Original first-fetch HTML bytes were overwritten, so the earlier HTML hash is a receipt only, not a claim that those bytes remain. The dated Ueda PDF and its pre-event Last-Modified are preserved in the final manifest.
- `cme-reference.json`: primary bulletin fields transcribed from browser PDF text. No downloaded CME PDF/hash is claimed: direct requests returned 403. Two official bulletin sections cross-check the values; both reflect the same exchange, not independent markets.
- `analysis.json`, `candidate-pair-observations.csv`, `episode-screen.csv`: calculations and screens, with no automated prediction grade. The candidate CSV intentionally preserves suspect vendor observations; it is not a live funding ledger.
- `prediction-rows-frozen.json`: exact original SAM-28/31 rows and source hash; no amended criterion.
- `FUTURES_PAIR_REVIEW.md`: contract validation, precision discrepancy and activation hold.

Collectors were used for this bounded session, with network failures retried under approved access. They are not scheduled jobs. Reusing this dated folder would overwrite evidence; use a new dated capture directory for future observations. Sep-9 final settlement, Sep-11 CFTC and Sep-18 policy/CPI were not yet published at their respective capture times.
