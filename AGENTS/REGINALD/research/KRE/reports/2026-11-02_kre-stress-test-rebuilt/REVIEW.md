# Rebuilt KRE stress test — integration review

Received November 2, 2026 from Will's supplied lite ZIP. This is a reconstruction of the earlier decoupling stress test, not recovery of its original folder. Source observations end at the October 30 close. [Report](source/REPORT.md) · [comparison table](source/out/comparison_with_original.csv) · [manifest](MANIFEST.json)

## What the bundle adds

The earlier collection had the narrative report and narrow local checks, but not its calculation bundle. This package supplies a unified script, retrieval script, 13 output files, the 54-row original/rebuilt comparison, rolling figure, processed ETF panel, KRE holdings and NAV files, and Treasury history. The original per-ticker Yahoo JSON files are intentionally absent from the lite ZIP; `scripts/fetch.sh` retrieves them.

The main conclusion is unchanged and remains supported: KRE–KBWB correlation is unusually low, the rarity survives matched trimming, and the change predates September/October headline events. The SPY-only partial correlation is less exceptional than the raw correlation. These are descriptive findings, not bank-credit or return forecasts.

## Verification performed

- ZIP integrity and extraction passed: 37 files, with source SHA-256 in the manifest.
- The supplied ETF panel joins the collection's existing Yahoo panel with maximum relative price differences below 0.0001% on the five shared ETFs. It reproduces current KRE–KBWB correlation 0.719338 and KRE SPY beta 0.327529.
- A fresh public-data fetch followed by the supplied analysis was attempted in a temporary copy. As shipped, `fetch.sh` omits USB, COF, PNC, BNY, NTRS, STT, KEY and FITB, although `stress_test.py` requires them; the first full run stopped there.
- For diagnosis only, those eight tickers were added to the temporary fetch list. The archived source was not changed. The analysis then completed, and all 54 rebuilt values matched the supplied comparison table exactly as text.
- Nine of 13 output files were byte-identical. The two large historical CSVs differed only slightly at displayed precision (maximum absolute differences 0.0003 and 0.0011); the regenerated comparison omitted the post-processed status column; and the PNG was not byte/pixel identical. Current headline values were unchanged.
- SciPy was absent from both project and system Python. Verification used a temporary `/tmp` SciPy 1.18.1 install plus the existing temporary Matplotlib 3.11.2 directory. No project dependency or environment file changed.

## Documentation and interpretation caveats

1. **The Markdown report's comparison table is malformed.** Its check names contain a Python bound-method/debug rendering. Use `out/comparison_with_original.csv` or the PDF presentation instead of copying that table.
2. **“50 of 54 reproduce” is the author's classification.** The CSV has 27 `matches`, 23 `matches within rounding/convention`, and four `differs`. Not every item in the second group is just rounding: the 10-day bootstrap interval is [0.65, 0.81] versus [0.61, 0.81], and two block-count comparisons differ. Carry the row-level notes rather than treating 50/54 as an independent audit grade.
3. **Four named differences remain:** volatility-adjusted z −2.6 versus −2.2; 2-day/5-day percentiles 3.7%/0.8% versus approximately 0.1%; NAV correlation 0.700 versus 0.714; five-day bootstrap [0.58, 0.82] versus [0.61, 0.81]. None overturns the core co-movement finding, but the original methods were not recovered.
4. **R² provenance is still not proven.** Correct single-factor values remain 0.517/0.251/0.048. A degrees-of-freedom mismatch reproduces 0.5251 for KBWB, but does not identify the original code or explain all three earlier figures.
5. Existing limits survive: same-vendor prices, overlapping windows, retrospective selections, current-member basket bias, and no unique causal volatility decomposition. The 99.5% historical reversion statistic is not a forward probability.

## Disposition

Integrated as supporting evidence with no change to the KRE synthesis, REGINALD's bank grades, thresholds, predictions or trade state. The bundle materially improves reproducibility and narrows the earlier “reported only” gap after the documented retrieval repair. It does not supply the original session's exact code/data or validate Study 6's separate holdings attribution.
