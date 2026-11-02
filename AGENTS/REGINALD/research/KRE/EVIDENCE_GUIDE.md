# Evidence guide and study catalog

Updated November 2, 2026. [Start here](README.md) · [Synthesis](SYNTHESIS.md) · [Open questions](OPEN_QUESTIONS.md)

## How to read evidence status

**Reproduced on saved data:** PROME reran a calculation on the stored inputs. Usually the same Yahoo vendor data as the researcher, not an independent price source.

**Primary-source spot check:** a specific issuer/SEC/Fed claim was checked in the earlier review. It does not certify the entire report or constitute a new check today.

**Reported only:** retained from a supplied study; its calculation or inputs have not been independently replicated here.

**Interpretation:** an explanation or hypothesis; association, accounting attribution and cause are different. Reviews and raw reports deliberately coexist. Consult the latest synthesis and open questions before repeating a raw report's conclusion.

The catalog below is chronological by our discussion, not a reconstructed numbering scheme. “Study 3” and “Study 6” are the supplied authors' labels. Files called REPORT.md, REPORT (2).md and REPORT (5).md were distinct uploads; gaps in their numbering do not imply missing approved work.

## 1. October 23 transition study — historical context

[Original report](reports/2026-10-23_kre-qqq-transition-signature/REPORT.md) · [episodes](reports/2026-10-23_kre-qqq-transition-signature/episodes.csv) · [build script](reports/2026-10-23_kre-qqq-transition-signature/build.py)

Earlier KRE/QQQ transition-signature research, preserved at its original vintage. It was not newly revalidated in the November 2 collection. Use for history and method context, not current levels or a validated forecast.

## 2. November 2 ETF relationships study — the common data foundation

[Report](reports/2026-11-02_kre-etf-relationships/REPORT.md) · [aligned adjusted closes](reports/2026-11-02_kre-etf-relationships/aligned_adjusted_closes.csv) · [performance](reports/2026-11-02_kre-etf-relationships/performance.csv) · [correlations](reports/2026-11-02_kre-etf-relationships/daily_return_correlations.csv)

**Question:** How does KRE compare with banks, financials, equities, credit, bonds and real estate?

**Contribution:** separates short rebounds from longer declines; places KRE strength in the wider technology/equal-weight/rate-sensitive rotation; supplies the frozen panel used by subsequent local checks. Prior-year fitted models and historical analogs are exploratory, not causal allocations or trade probabilities.

**Available data:** 13 ETF daily histories (KRE, KBWB, XLF, IWM, SPY, RSP, QQQ, HYG, LQD, IEF, TLT, VNQ, SHY), aligned dividend-adjusted closes, short FRED snapshots, model outputs, charts, source manifests and sensitivity results. The common saved 63-session history contains 3,666 windows; supplied studies sometimes use 3,708. Match endpoints and baseline coverage before treating percentiles as exact replications.

**Important price caveat:** HYG's raw November 2 move cannot be read as credit deterioration without distribution adjustment. [Distribution verification](reports/2026-11-02_kre-etf-relationships/hyg_distribution_verification.json).

[ETF source manifest](reports/2026-11-02_kre-etf-relationships/source_manifest.json) · [FRED source manifest](reports/2026-11-02_kre-etf-relationships/fred_source_manifest.json) · [validation](reports/2026-11-02_kre-etf-relationships/validation_and_sensitivity.json)

## 3. Supplied constituent and Q3 study — breadth and bank fundamentals

[Original supplied report](reports/2026-11-02_kre-external-report-review/input_report.md) · **[Readable PROME review](reports/2026-11-02_kre-external-report-review/REVIEW.md)** · [numerical receipt](reports/2026-11-02_kre-external-report-review/verification.json)

Original upload: `KRE_regional_banks_full_report.md`.

**Contribution:** constituent breadth, portfolio-construction comparisons and a Q3 sample. The supplied table has 149/167 rebound winners but only 31/167 positive over the longer window. The Q3 sample reports 10 margin increases, one unchanged and five decreases; deposit costs increased in eight of ten disclosed comparisons. These are sample/appendix checks, not whole-universe primary audits.

**Primary spot checks already recorded:** Preferred Bank troubled-loan classification and symmetrical margin adjustments; Texas Capital margin/criticized-loan divergence; Truist realized securities loss and reserve recapture. Their source links and dates live in the readable review.

**Limits:** mixed TBV/BV and other accounting classifications; June fundamentals versus returns partly preceding publication; merger effects; current-member/weight bias; uncertain zero capital fields. Broad improvement in profitability is not proof of late-rally causation. [Corrections queue](OPEN_QUESTIONS.md).

### CATO's review, as supplied by Will

The following is a summary of the supplied assessment, not a separately obtained CATO delivery or a verbatim transcript:

- Preserve unusual co-movement as the main discovery, subject to reproducing it.
- Reconcile single-factor R² with squared correlation on identical observations.
- Remove September 14, October 22, both, and the largest divergence days; overlapping windows can magnify a few shocks.
- Treat fitted yield contributions as associations, not causal percentages. Do not attribute a whole quarter's deposit costs to a late-quarter hike.
- Moderate the fundamentals conclusion: profitability improved and some characteristics correlate modestly with YTD returns, but explanatory power for the late rally is weak.
- Distinguish completed Q3 loss-taking from later or announced repositioning, and TBV from ordinary BV. The proposed GICS explanation for KEY/FITB exclusion remained a company-level verification question.
- Keep the next work bounded. A December risk scenario concerns an unexpected yield increase, not merely delivery of an already anticipated policy decision.

## 4. CATO-prompted local checks — the narrow replication

[Results](reports/2026-11-02_kre-cato-sensitivity/results.json) · [script](reports/2026-11-02_kre-cato-sensitivity/check.py)

**Reproduced:** 63-session correlation 0.719338; the requested removals; top-five squared-gap share 43.76%; matched historical trimming; and single-factor R² with intercept of 0.517447 (KBWB), 0.250958 (IWM), 0.048089 (SPY).

**Meaning:** the unusual relationship survives exceptional-day removal. The old R² figures do not describe the stated single-factor sample. The actual origin of those old errors is still unknown; matching a number to a candidate formula does not prove provenance. No bank-grade update followed.

## 5. Study 3 — when falling Treasury yields help or hurt

[Original report](reports/2026-11-02_kre-study3-review/input_report.md) · [supplied specification](reports/2026-11-02_kre-study3-review/PREREGISTERED_SPEC.md) · [initial review](reports/2026-11-02_kre-study3-review/review.json) · [specification addendum](reports/2026-11-02_kre-study3-review/spec_addendum.json)

Original uploads: `REPORT.md` and `PREREGISTERED_SPEC.md`. The addendum supersedes the initial review's statement that the specification was missing. The specification belongs to this study, not automatically to Study 6.

**Contribution:** shows why a negative bank rate beta is not a unique crisis signal; distinguishes immediate relief from subsequent performance; explicitly reports that its constructive/stress-rebound classification does not reliably separate outcomes. A limited local calculation supports the recent negative yield-response sign for KRE and KBWB, not the full history.

**Method clarity added by the specification:** Treasury par yields; carry prior yield on bond holidays; intercept and regression units; grids anchored to October 30; every-third-window selection for 60-session outcomes on a 20-session grid. Crisis exclusions, analog scans and other additions are explicitly labeled post-result explorations. Pre-run chronology is author-attested, not independently proven by the file.

**What remains weak:** the phase-sensitivity table shows absolute returns rather than the strongest claim, KRE-minus-KBWB returns; four of six recent proxy-widening analogs actually had narrowing HY OAS; CRE denominators mix capital measures; the reported real-yield decomposition does not identify a term-premium contribution. “AOCI relief,” “flight to quality,” and an absolute-return forecast exceed the demonstrated evidence.

**Concrete source correction:** the October 28 Fed statement directly names Cook and Hammack and their preference for a quarter-point hike. The report's secondary-only designation for their names was unnecessary. [Recorded source](https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm).

The later [PDF upload](reports/2026-11-02_kre-study3-review/REPORT.pdf) preserves the Study 3 presentation, including embedded regime-map and rolling-rate-beta charts on pages 5–6. [Searchable text](reports/2026-11-02_kre-study3-review/REPORT_pdf_text.txt) · [PDF provenance](reports/2026-11-02_kre-study3-review/PDF_MANIFEST.json). It adds visual access, not a new empirical study. The original study code, master data, result CSVs and standalone chart assets were not supplied. References to its `out/` and `scripts/` assets inside the raw report are not evidence those assets are present here.

## 6. Decoupling stress test — persistence and factor controls

[Original report](reports/2026-11-02_decoupling-stress-test/input_report.md) · [review](reports/2026-11-02_decoupling-stress-test/review.json) · [reproduced checks](reports/2026-11-02_decoupling-stress-test/checks.json) · [script](reports/2026-11-02_decoupling-stress-test/check.py)

Original upload: `REPORT (2).md`. Later upload `REPORT (6).md` is byte-for-byte identical (SHA-256 verified November 2); it is the same study, not additional evidence. The alternate source path is recorded in the [package manifest](reports/2026-11-02_decoupling-stress-test/MANIFEST.json).

**Reproduced:** top-ten trimmed correlation 0.8535; multiple window-length correlations; June/July step down; KRE/KBWB SPY betas; residual correlation; annualized return-gap volatility. The reported persistence statistic is approximately reproduced, but its many conditioning windows overlap heavily.

**Reported only:** issuer-NAV replication, KBE/QABA/IAT histories, current-constituent baskets, bootstrap interval and full historical baseline. The issuer factsheet's 2011 benchmark change was primary-checked in the review; that does not validate its NAV calculations.

**Readable judgment:** the report directly answers the unusual-day challenge and strengthens observed persistence. “Stopped moving with the market,” “half explained by low volatility,” and “artifacts ruled out” need narrower wording. A rank among overlapping windows and the historical reversion percentage are not forecast probabilities. Study 6's baseline comparison below qualifies the earlier residual-correlation framing.

**Rebuilt package supplied later:** [integration review](reports/2026-11-02_kre-stress-test-rebuilt/REVIEW.md) · [54-row reconciliation](reports/2026-11-02_kre-stress-test-rebuilt/source/out/comparison_with_original.csv) · [manifest](reports/2026-11-02_kre-stress-test-rebuilt/MANIFEST.json). The lite ZIP preserves the report, unified scripts, outputs, processed ETF panel, holdings/NAV and Treasury files; per-ticker Yahoo JSON requires retrieval. As shipped, the fetch list omits eight required banks. A temporary diagnostic repair allowed a full rerun, with all 54 rebuilt values matching the supplied table as text. Four named original/rebuilt differences and the existing causal/dependence caveats remain; the malformed Markdown comparison table should not be reused.

## 7. Study 6 — different drivers of returns and co-movement

[Original report](reports/2026-11-02_study6-drivers/input_report.md) · [review and numerical receipts](reports/2026-11-02_study6-drivers/review.json)

Original upload: `REPORT (5).md`. The later [supplied four-panel chart and reading guide](reports/2026-11-02_study6-drivers/CHART_NOTE.md) now preserve its visual comparisons. The image is separate from `fig_timeline.png`; original asset filename identity remains unverified.

**New contribution:** a holdings-based explanation for much of the cumulative gap; comparison with traditional banks; and a hypothesis that banks' credit-spread sensitivity changed. It distinguishes securities accounting attribution from daily correlation more clearly than the earlier studies.

**Reproduced locally:** 2.414-point compounded gap; 2.565-point sum of daily gaps; September 14's 2.174-point gap; approximately 0.40 volatility-unit scale; residual-correlation percentile of 10.37% since 2012 versus 2.82% since 2015. The latter is an important qualification to the prior roughly-11th-percentile narrative.

**Verification bundle supplied later:** [integration review](reports/2026-11-02_study6-verification/REVIEW.md) · [corrected linked attribution](reports/2026-11-02_study6-verification/source/out/corrected_attribution_linked.csv) · [manifest](reports/2026-11-02_study6-verification/MANIFEST.json). The N-PORT, Invesco holdings, prices and reconstruction code are now present. Offline `run_all.sh` regenerated 16 of 17 outputs byte-for-byte; only the rendered figure differed. Ex-five −6.619%, the +5.001% rebound and the 1.772-point like-for-like effect reproduce. The original 1.81 includes 0.044 tracking; its components were non-additive separate removals. Correct linked groups: BAC +1.038, GS+MS +0.899, JPM+C −0.166. The 73% share is specific to 8/3–10/30 and ranges 37–98% across nearby dates.

**Still reported only / open:** traditional-bank basket, long HY regressions and most company-level claims. A nonsignificant current HY coefficient does not establish no credit exposure or a statistically significant regime change. Capital-markets weakness is not proven temporary. AI-specific spread widening is unmeasured. Selected weak fundamental associations do not prove investors ignore quality.

## 8. Prospective evaluation — unapproved draft

[Original PREREGISTRATION.md](reports/2026-11-02_prospective-evaluation-draft/PREREGISTRATION.md) · **[Readable review](reports/2026-11-02_prospective-evaluation-draft/REVIEW.md)** · [Manifest](reports/2026-11-02_prospective-evaluation-draft/MANIFEST.json)

Proposes three tests over November 2–February 2: correlation persistence, market-beta recovery and rate-response persistence. Useful as a framework for distinguishing outcomes; its probabilities and historical base rates are unreplicated. This is a separate document from Study 3's `PREREGISTERED_SPEC.md`.

**Not approved or activated.** The author and approver have seen first-session information; preserve late-registration status if adopted. The later [combined-package review](reports/2026-11-02_prospective-evaluation-draft/COMBINED_PACKAGE_REVIEW.md) adds printed resolver/base-rate code and selected historical rows. Exact standalone code and full inputs remain absent. Synthetic checks reproduce incomplete-window resolution and incorrect counting of missing sessions. The C1 benchmark sums to 0.99, and dropped-session rules conflict with exactly 63 daily returns. A KRE-only rate test cannot establish a bank-wide regime. The review explains the repairs; no schedule or forecast ledger entry was created.

**Latest intake:** [full state-series and chat-code review](reports/2026-11-02_prospective-evaluation-draft/STATE_SERIES_REVIEW.md) supplies all 5,059 derived rows and reproduces the three conditional reference forecasts. The C1 0.99 total is explained by rounding; exact counts are 300/142/383 out of 825. Raw prices/yields and original code byte identity remain unverified; resolver defects remain. This supersedes the earlier missing-full-table status. A subsequent run of the chat-supplied `prereg_base2.py` also reproduces the listed episode counts and episode-weighted comparisons; its preserved output and interpretation are linked in the same addendum.

## 9. Study 4 — market leadership and style factors (received after Study 6)

[Readable review](reports/2026-11-02_study4-market-leadership/REVIEW.md) · [Report](reports/2026-11-02_study4-market-leadership/source/REPORT.md) · [Specification](reports/2026-11-02_study4-market-leadership/source/SPEC.md) · [Full inventory](reports/2026-11-02_study4-market-leadership/MANIFEST.json)

Distinct new study with a complete supplied ZIP containing 66 files. A later [self-contained HTML version](reports/2026-11-02_study4-market-leadership/KRE_Study4_Market_Leadership_Report.html) preserves the report presentation with its timeline image embedded. Selected offline reruns regenerate 17 outputs byte-for-byte, including the processed panel, sector comparisons, factor models and decompositions. Independent calculations confirm KRE's 0.328 SPY beta, 1.094 controlled market loading, 0.623 five-factor R² and 0.537 KRE–KBWB residual correlation. All ten comparators have low SPY betas relative to their pre-2025 histories. This strengthens a broad-market/style explanation without establishing cause or improved bank credit.

**Carry these caveats:** October ETF-factor splice; model-dependent decompositions; pooled versus rolling reference statistics; small recent out-of-sample groups; author-attested chronology with post-result diagnostics. The “frozen-loading forecast” uses future realized factor relationships and is a conditional attribution test. A ddof mismatch in q3b's secondary R² output gives 0.6294 instead of 0.6235; the main model table is correct. No proposed future test is activated.

The package preserves its own `out/fig_timeline.png`. Do not confuse this with Study 6's four-panel chart or assume it is byte-identical to other timeline uploads.

## Earlier conversation and pictures

[DISCUSSION.md](DISCUSSION.md) preserves Will's intent and the earlier ETF comparisons. The [14:15 ET snapshot](market_snapshot_2026-11-02_1415ET.csv) is transcribed from retrieved tool output; exact exchange timestamps were not captured and prices may be delayed. It is not part of the October 30 closing sample.

[Capture.JPG](screenshots/Capture.JPG) · [Capture2.JPG](screenshots/Capture2.JPG) · [KRE YTD.JPG](<screenshots/KRE YTD.JPG>) preserve the original supplied filenames. Screenshots show displayed charts, not machine-readable price histories.

## Reproduction and preservation

From repository root, the existing bounded scripts are:

```sh
.venv/bin/python3 AGENTS/REGINALD/research/KRE/reports/2026-11-02_kre-external-report-review/verify.py
.venv/bin/python3 AGENTS/REGINALD/research/KRE/reports/2026-11-02_kre-cato-sensitivity/check.py
.venv/bin/python3 AGENTS/REGINALD/research/KRE/reports/2026-11-02_decoupling-stress-test/check.py
```

These write their local result artifacts. Inspect the scripts first and use a separate copy for extensions. The original ETF `analyze.py`/`fetch_data.py` workflow can overwrite data and charts; re-fetching may change historical vendor adjustments. It requires pandas/numpy/matplotlib, with yfinance for retrieval. The bounded tests do not need fresh market retrieval. The copied CATO script has only its repository-root discovery adapted for this folder.

No single manifest covers every authored navigation file. Use the appropriate provenance record:

| Coverage | Record |
|---|---|
| Initial research copies and screenshots, plus Study 3/CATO additions | [COPY_MANIFEST.json](COPY_MANIFEST.json) |
| Decoupling stress-test source and generated artifacts | [Package manifest](reports/2026-11-02_decoupling-stress-test/MANIFEST.json) |
| Study 6 source and review | [Package manifest](reports/2026-11-02_study6-drivers/MANIFEST.json) |
| Original download identity for Study 3/spec | Source paths and hashes in its review/addendum above |

Copies are frozen, not synchronized. Originals remain in their PROME/Downloads locations; some retained provenance links intentionally point there. Existing relative paths were preserved to avoid breaking scripts or citations. The original reports' missing assets remain gaps, not files manufactured by this organizational pass.
