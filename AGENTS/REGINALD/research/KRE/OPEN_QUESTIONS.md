# Open questions and correction queue

As of November 2, 2026. [Synthesis](SYNTHESIS.md) · [Evidence guide](EVIDENCE_GUIDE.md)

This is a research handoff, not a new commission, recurring tracker or trade instruction. The order below prioritizes bounded repairs to existing evidence. Acquire the named missing inputs before repeating large studies. REGINALD retains domain ownership; this file does not resolve or reassign live desk work.

## First: attribution and reproducibility

| Question or defect | Current evidence | Needed to close it |
|---|---|---|
| Study 6 additive bridge | Named components 1.04 + 0.78 − 0.37 = 1.45pp, not 1.81pp; group-removal endpoints imply 1.81pp | Exact attribution output, formulas and reconciliation; distinguish additive contributions from separate renormalized counterfactuals |
| Study 6 holdings reconstruction | Report claims near-perfect KBWB replication; raw N-PORT, holdings JSON and reconstruction code absent | Exact filings/holdings, dates, share counts, corporate-action/rebalance handling, counterfactual code and return bridge |
| HY history provenance | Study 3 lacked long history; Study 6 uses an unnamed FRED mirror | Mirror URL, retrieval vintage, raw series, units/missing-date policy, official overlap checks and preservation permissions where applicable; do not silently equate the sources |
| Earlier single-factor R² error | Correct values reproduced: 0.517/0.251/0.048; error's original cause unknown | Original model inputs/code to identify actual cause; no need to repeat correct arithmetic. Candidate matches are not provenance |
| Missing external-study assets | Several reports reference absent scripts, CSVs, figures and specifications | Original supplied bundles. Study 3 specification is present; do not call it missing or assign it to a different study |

Sources: [Study 6 review](reports/2026-11-02_study6-drivers/review.json), [R² checks](reports/2026-11-02_kre-cato-sensitivity/results.json), [Study 3 addendum](reports/2026-11-02_kre-study3-review/spec_addendum.json).

## Second: test the strongest remaining claims

| Claim | Why it remains unresolved | Bounded follow-up |
|---|---|---|
| Falling yields predict KRE lagging KBWB | Relative-return sensitivity across all three sampling phases not shown | Report counts, means, medians and uncertainty for KRE-minus-KBWB across phases and fixed horizons; account for dependence and multiple testing |
| Credit-widening analogs resemble this episode | Four of six recent analogs had actual HY narrowing despite proxy widening | Separate actual-HY-widening from proxy-only cases on available overlap; do not call all six confirmed stress rebounds |
| Market controls largely explain the anomaly | Percentile moves from 10.37% to 2.82% when baseline starts in 2015 rather than 2012 | Keep baseline dates fixed and disclosed; compare raw and controlled distributions without treating percentile shifts as causal shares |
| Traditional-bank comparison isolates the remaining anomaly | Study 6 basket, holdings history and rate regressions not reproduced | Supply constituent panel/weights; rebuild matched comparisons with period-appropriate membership and explicit controls |
| Banks stopped responding to credit widening | Current HY coefficients are imprecise; earlier significance is not a test of coefficient change | Confidence intervals, direct period-difference/stability tests, date-alignment checks and dependence-aware errors |
| HY widening is AI-specific | Suggested explanation, sector decomposition absent | Sector/issuer spread contributions and breadth, with dated sources; do not infer concentration from bank-stock resilience |
| Low volatility explains half the decline | Variance identity is correct, causal allocation is not unique | State a model and assumptions, or retain descriptive volatility comparisons without a precise causal percentage |
| Securities losses/funding/CRE identify the rate channel | Few event days, correlated traits, accounting/mapping choices, some results sensitive to four banks | Harmonize measures; show leave-event/group-out results and appropriate cross-bank/date uncertainty; label associations |

Sources: [rate-study review](reports/2026-11-02_kre-study3-review/review.json), [stress-test review](reports/2026-11-02_decoupling-stress-test/review.json), [Study 6 review](reports/2026-11-02_study6-drivers/review.json).

## Accounting and bank-level comparisons

Before extending the fundamentals claims:

- Resolve zero CET1 entries for CFFN/CTBI: missing/nonapplicable is not actual zero capital.
- Keep holding-company and bank-charter measures separate; verify bank mappings and merger boundaries. Mapping errors need not be unbiased.
- Separate TBV from ordinary BV; NPL from NPA; denominators and guarantee treatment must be explicit. The first review records the mixed TBV tally and its correction.
- Count completed Q3 securities loss-taking separately from later transactions and announced plans. Realization of an existing mark is not automatically an equivalent new economic loss.
- Study 3 substitutes Tier 1 for missing total risk-based capital in some CRE ratios. Require denominator flags and a common-denominator or exclusion sensitivity.
- Use filing publication dates when testing predictability. June accounts cannot automatically explain returns before their release, and April–October sensitivity using June accounts is descriptive unless lagged correctly.
- Compare earnings surprises and forward revisions if testing fundamental repricing. Weak associations with a few Q2 metrics do not prove no quality discrimination.
- Recheck KEY/FITB company-level GICS classification before treating the proposed index-exclusion explanation as verified.
- Preserve the Preferred Bank, Texas Capital and Truist source-specific caveats from the [primary-source review](reports/2026-11-02_kre-external-report-review/REVIEW.md). No exhaustive Q3 audit was completed.

## Interpretation guardrails

These are warnings about claims in this collection, not new fleet controls:

- Persistent through October 30 does not mean permanent. Proposed future thresholds in the reports are not adopted monitors.
- Rare correlation is not a reversal probability; overlapping windows and repeated variants are not independent evidence.
- A large share of a small net return gap can come from one day because other days offset. That differs from explaining the correlation anomaly.
- Return attribution identifies contributors, not causes or duration. Event dummies identify date residuals, not the causal effect of a news story.
- Lower yields can support valuation and borrowers while wider credit signals worsening conditions. A stable breakeven does not rule out near-term disinflation; a real-yield decline alone does not identify term premium.
- A priced-in hike is not the same as an unexpected increase in yields. Do not attribute a whole quarter's deposit-cost changes to its final weeks.
- Relative underperformance does not imply an absolute loss or profitable puts. No timing, execution or sizing authority comes from these studies.

## What has already been answered

| Earlier question | Current disposition |
|---|---|
| Do two exceptional days create the entire anomaly? | No on saved data: matched top-five/top-ten trimming preserves rarity |
| Did reduced co-movement begin only in September/October? | No on saved data: June and July blocks already show it |
| Are the original single-factor R² figures valid for the stated sample? | No; corrected values reproduced. Original error provenance remains open |
| Was Study 3's specification supplied? | Yes; archived and reviewed. Execution chronology remains author-attested |
| Is market-adjusted rarity insensitive to historical start? | No; 2012 versus 2015 materially changes the percentile |
| Is this evidence sufficient for a reliable absolute-direction forecast? | No such edge established in these reviews |

The next useful evidence is the existing authors' underlying files and corrected tables. This organizational pass creates no new research assignment.
