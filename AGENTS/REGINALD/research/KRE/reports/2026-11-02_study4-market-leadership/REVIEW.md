# Study 4 — market leadership review

Received November 2, 2026; observations through October 30. [Report](source/REPORT.md) · [PDF](KRE_Study4_Market_Leadership_Report.pdf) · [Self-contained HTML](KRE_Study4_Market_Leadership_Report.html) · [Specification](source/SPEC.md) · [Source inventory](MANIFEST.json) · [Checks](key_checks.json) · [Rerun receipt](rerun_receipt.json)

## What it adds

This is a distinct study, arriving after Study 6 in our collection. It tests whether KRE looks unusual partly because SPY has become a less representative benchmark for value, small-cap and several nonbank stocks. It strengthens the broader-market explanation and reduces the case for reading low raw bank correlation as a uniquely regional-bank signal. It does not prove that bank fundamentals are healthy or that AI caused the market split.

In plain language: the relationship between the market index and several kinds of stocks changed. A bank fund can become less synchronized with SPY while retaining familiar exposure to value and size factors. This is a model-dependent explanation of co-movement, separate from Study 6's holdings explanation for cumulative returns.

## What was reproduced

The ZIP includes 66 files: reports/specification, 21 ETF price JSONs, French factor files, a Study 3-derived Treasury/BAA master, processed panel, scripts, result tables and a timeline figure. The separately supplied PDF is byte-identical to the bundled PDF. Originals are retained under `source/` and in the intact ZIP.

PROME reran `build.py`, `q124.py`, `q3.py`, `q3b.py` and `q5_nexttest.py` offline in a temporary copy. All 17 generated panel/result CSVs were byte-identical to the supplied versions. Other outputs were preserved but not rerun. The q5 check uses the supplied q4b intermediate output. Reproducibility on supplied inputs is not independent-vendor or primary-source validation.

A separate [bounded calculation](check_key_claims.py) confirms:

| Metric | Reproduced value |
|---|---:|
| KRE–KBWB correlation, 63 sessions | 0.719338 |
| KRE sensitivity to SPY alone | 0.327528 |
| SPY–equal-weight RSP correlation | 0.640827 |
| KRE market-factor loading with style/rate controls | 1.093949 |
| KRE five-factor R² | 0.623456 |
| KRE–KBWB residual correlation under that model | 0.537245 |

All ten listed comparison ETFs have current SPY betas below their own pre-2025 10th percentile. The supplied/reproduced rolling model places KRE's residual correlation near the 14th percentile, rising to about the 24th under volatility matching. These are different controls and baselines from Study 6's SPY-only comparison; they do not overwrite that earlier result.

## Important qualifications and repairs

1. **The frozen-loading test is conditional, not a fully advance forecast.** `q5_nexttest.py` freezes asset loadings at the prior window but multiplies them by factor betas observed in the NEXT window. Its historical error standard deviation of about 0.27 versus 0.55 for a naive forecast reproduces, but the methods have different information sets. Saying the June–August drop was “predicted ahead of time” is too strong without forecasting the future factor relationships too. The same issue applies to the 126-session-fit/21-session-test returns: coefficients are out of sample, while test-period factor returns are contemporaneously observed. These are useful conditional model checks, not evidence of an executable market-timing edge.
2. **October changes the factor measurement.** French factors end September 30; the final 22 sessions use ETF proxies. In October MKT is SPY minus RF and SMB includes minus SPY, so part of the decomposition is tied directly to the benchmark by construction. The September pure-French result supports the broad interpretation, but changing both dates and factor source is not a same-window splice sensitivity test. HML/momentum proxy correlations of 0.80/0.68 are imperfect.
3. **Decomposition is accounting, not causal attribution.** The split into changed loadings and changed factor relationships depends on model choice, reference period and allocation of interaction terms. A −1.10 “structure” term against a −0.87 total beta change does not prove market structure caused 126% of the change. Broad value/size factors may themselves include bank risk. The proposed characteristic-matched nonbank control is absent.
4. **A smaller R² convention error recurs in q3b.** Its correlation-decomposition CSV uses NumPy residual variance with ddof=0 divided by pandas outcome variance with ddof=1. Current KRE R² there is 0.629433 instead of 0.623456. `q3.py` and the report's main 0.62 model table use consistent conventions. This does not change the central findings, but that CSV needs correction before reuse. The earlier unrelated R² error's origin is still unproven.
5. **Keep reference statistics distinct.** The decomposition's −0.87 change uses a pooled 2012–2024 regression, whereas the opening 1.13→0.33 comparison uses a rolling historical median. Likewise, 26.6% factor volatility is pooled, while the quoted 8.3% residual-volatility benchmark is a rolling median (pooled residual volatility is 11.5%). Also, 26.6%→12.3% is roughly halving volatility, but about a 79% decline in variance—not merely halving variance. Avoid blending these baselines.
6. **Chronology and sample limits remain.** The spec says the main plan was fixed before computation, but this is author-attested. Its change log expressly labels decompositions, alpha checks and frozen-loading calibration as added after initial results. Do not describe every result as preregistered. Five recent 21-session blocks and overlapping reference windows limit inference. AI/mega-cap leadership is a label for observed index relationships; its underlying cause was not tested.

## How to use it

Use this study as stronger support for a broad market/style explanation of the co-movement anomaly. Retain a modest unresolved bank-specific component and the raw anomaly itself. The supplied source package makes this more auditable than the earlier report-only uploads.

The proposed November–February frozen-loading test is distinct from the earlier three-claim preregistration. Neither is activated by this archive. No thresholds, probabilities, schedules, bank grades or trade instructions were adopted.

## Navigation and reproduction

- `source/REPORT.md`: complete narrative; `source/SPEC.md`: main plan and post-result additions.
- `source/out/`: frozen numerical outputs and [timeline chart](source/out/fig_timeline.png).
- `source/data/`: supplied raw and processed data; the Study 3 master is derived, not a replacement for its original official downloads.
- `source/*.py`: supplied analysis code; running in place overwrites outputs. Work in a temporary copy to preserve the archive.
- `check_key_claims.py`: narrow local verification, writes `key_checks.json` only.

The supplied `fig_timeline.png` should not be confused with Study 6's four-panel chart; this package has its own figure and provenance.

## Additional HTML upload

The self-contained HTML has the same title, cutoff and main conclusions as the saved report. Its embedded timeline has identical decoded pixels to `source/out/fig_timeline.png`, although the PNG bytes differ. This adds a browser-readable format, not another study or fresh validation. Existing review caveats remain.
