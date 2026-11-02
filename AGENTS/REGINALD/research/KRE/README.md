# KRE study collection

Saved 2026-11-02 by PROME at Will's explicit request to keep the discussion's data under REGINALD. This is a research collection, not an update to REGINALD's canonical thesis, grades or monitoring rules. Original files remain in place. Copies are frozen at collection time, not automatically synchronized.

## Start here

- [ETF relationships study](reports/2026-11-02_kre-etf-relationships/REPORT.md): KRE versus banks, financials, equities, credit, bonds and real estate; historical comparisons and exploratory analogs.
- [Supplied regional-bank report](reports/2026-11-02_kre-external-report-review/input_report.md): constituent-level study and Q3 sample supplied by Will.
- [PROME review](reports/2026-11-02_kre-external-report-review/REVIEW.md): reproduced findings, primary-source spot checks, methodological corrections and unresolved questions.
- [Discussion and market context](DISCUSSION.md): later intraday sweep, three-ETF comparison, synthesis and Will's clarification of intent.
- [Earlier October 23 transition study](reports/2026-10-23_kre-qqq-transition-signature/REPORT.md): historical context, preserved at its original vintage; not newly revalidated.
- [Copy manifest](COPY_MANIFEST.json): original locations, byte counts and SHA-256 hashes for every copied artifact, including screenshots.

## November 2 follow-up: rate study and CATO checks

- [Study 3: falling yields and regional banks](reports/2026-11-02_kre-study3-review/input_report.md), supplied by Will; [specification and change log](reports/2026-11-02_kre-study3-review/PREREGISTERED_SPEC.md).
- [PROME review](reports/2026-11-02_kre-study3-review/review.json) and [specification addendum](reports/2026-11-02_kre-study3-review/spec_addendum.json). Read together: the addendum supersedes the earlier statement that the specification was missing.
- [CATO-prompted correlation and regression checks](reports/2026-11-02_kre-cato-sensitivity/results.json), with [reproduction script](reports/2026-11-02_kre-cato-sensitivity/check.py). The script uses the frozen ETF data already in this collection; only repository-root discovery was adapted for this location.

**Verified on saved data through October 30:** KRE–KBWB correlation rises from 0.719 to 0.821 after removing the five largest divergence days, but remains near the 1.3rd percentile when historical windows receive the same removal. Identical-sample single-factor R² values are 0.517 (KBWB), 0.251 (IWM) and 0.048 (SPY). Historical windows overlap; these are descriptive diagnostics, not independent probability estimates or trade signals.

**Study 3 remains partially reviewed, not fully reproduced.** Its raw data, analysis code and referenced charts were not supplied. Preserve the report's broken relative chart links as evidence of that missing package, not as existing collection assets. Outstanding: relative-return results across sampling phases; four of six recent proxy-widening analogs had narrowing actual HY spreads; mixed CRE-capital denominators; causal claims beyond the displayed evidence; and the original report's unexplained R² mismatch. The specification clarifies method and explicitly labels post-result explorations; its claimed pre-run timing is not independently verified. Our original source files and reviews remain preserved at PROME.

Reproduce the sensitivity checks from repository root with `.venv/bin/python3 AGENTS/REGINALD/research/KRE/reports/2026-11-02_kre-cato-sensitivity/check.py`. It overwrites only its own results file; requires numpy and pandas. No REGINALD canonical state or grade changes are implied by this archive.

## Data and visuals

The November 2 ETF folder contains 13 ETF daily histories, aligned dividend-adjusted closes, performance/correlation tables, FRED yield and credit-spread series, source manifests, sensitivity checks, exploratory models, scripts and two charts. Completed-session analysis ends October 30; November 2 observations are intraday and must not be presented as closing values.

The report-review folder contains the supplied report, review, verification script and numerical receipts. Its constituent checks use the report's rounded table; they are not an independent audit of all underlying stock prices or bank filings.

Screenshots supplied by Will: [Capture.JPG](screenshots/Capture.JPG), [Capture2.JPG](screenshots/Capture2.JPG), [KRE YTD.JPG](<screenshots/KRE YTD.JPG>). Original filenames retained. Image files are evidence of the displayed chart, not machine-readable price histories.

[Later market snapshot](market_snapshot_2026-11-02_1415ET.csv) preserves the numbers retrieved during the conversation around 14:15 ET. It was transcribed from the actual tool output, not downloaded again; exact exchange quote timestamps were not captured. Values may be delayed. Raw ETF price changes are not distribution-adjusted returns.

## Reproduction

The copied November 2 scripts resolve their inputs relative to their own files; the two dated folders retain their original sibling names. From repository root:

```sh
.venv/bin/python3 AGENTS/REGINALD/research/KRE/reports/2026-11-02_kre-external-report-review/verify.py
```

The ETF analysis additionally needs numpy, pandas and matplotlib; retrieval needs yfinance. Running scripts may overwrite snapshot outputs, and re-fetching historical data can change vendor adjustments. Use a separate working copy when refreshing. Original reports/manifests may contain provenance paths to PROME; these were preserved deliberately.

## Related REGINALD material already on disk

- [Market technicals hub](../market-technicals/README.md)
- [October 12 whole-basket study](../market-technicals/studies/2026-10-12_KRE_whole_basket_study.md)
- [October 12 price-pattern study](../market-technicals/studies/2026-10-12_KRE_price_patterns.md)
- [October 12 basket source artifacts](../../domain/sources/2026-10-12_KRE_basket_study/)

These older owner materials remain in their established locations; the links are navigation, not a claim of fresh verification. No active REGINALD state files were edited.
