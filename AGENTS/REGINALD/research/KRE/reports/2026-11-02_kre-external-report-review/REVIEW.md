# PROME review: KRE constituent and Q3 report

2026-11-02. User-requested analytical review, not a trade proposal or owner-state update.

## Judgment

Materially useful extension of our ETF study. It adds constituent breadth, business-model dispersion and a systematic Q3 earnings sample. Accept the descriptive evidence of an unusually weak KRE–KBWB relationship and a broad late-October rebound. Retain rate relief plus rotation as a working interpretation, with mixed bank fundamentals. Do not adopt the stronger causal claims that rotation is weak, fundamentals are irrelevant to the rebound, or a December hike necessarily reverses it.

The report reinforces an important distinction: broad equity buying can coexist with worsening credit in individual banks. It neither establishes a sector-wide credit recovery nor demonstrates an imminent sector breakdown.

## What is new or materially stronger

- **Breadth:** the published appendix has 149/167 stocks positive in the rebound, with a 4.5% median gain. Only 31/167 were positive over the longer 63-session window. The top ten contributors account for about 26% of the appendix's weight-times-return approximation. This strengthens the evidence that the rebound extended well beyond a few names; it does not establish improving credit breadth.
- **Construction controls:** cap-weighted and regional-only comparisons are useful attempts to distinguish ETF construction from economic behavior. They remain provisional until point-in-time constituents and weights are supplied.
- **Q3 dispersion:** the report's 17-bank size-spaced sample (16 reporting) has 10 NIM increases, one unchanged and five decreases; deposit costs rose at eight of ten with disclosed comparisons. These sample counts are not estimates of all 167 banks. They illustrate how stronger margins and renewed funding pressure can coexist.
- **Event concentration:** our recalculation finds five days account for 43.8% of squared daily KRE-minus-KBWB return gaps; ten account for 62.2%. Event explanations deserve investigation, but date alignment alone does not identify causes.

## Primary-source additions and corrections

**Preferred Bank:** its release reports $109.4M of nonaccrual/90-day-past-due loans excluding held-for-sale loans, versus $98.9M in June. A separate $56.7M troubled loan was transferred to held for sale; the announced expected sale is not proof of completion. Management reported no significant identified loss content and indicated some resolutions were delayed into Q4/Q1 2027. The margin comparison also needs symmetrical adjustment: Q3 included a $2.1M interest reversal, while Q2 benefited from $2.9M of interest recoveries. Removing only the Q3 adverse item overstates comparability. [Issuer release](https://preferredbank.q4ir.com/press-releases/news-details/2026/Preferred-Bank-Reports-Third-Quarter-Results/default.aspx).

**Texas Capital:** verified NIM increased from 3.28% to 3.44%, while criticized loans increased from $696.3M to $782.4M (12.4% QoQ), versus $529.7M a year earlier (47.7% YoY). CET1 increased to 12.2%. This supports a mixed assessment: earnings improvement, an earlier credit-warning measure worsening, and substantial reported regulatory capital. [SEC earnings release](https://www.sec.gov/Archives/edgar/data/1077428/000107742826000078/a10212026exhibit991.htm).

**Truist:** verified the $1.4B pretax AFS securities-sale loss, alongside a $581M reserve recapture connected to the RAC loan sale. Such transactions require a bridge across earnings, existing AOCI, capital treatment and future income; the realized loss alone does not establish forced distress or an equivalent new economic loss. [SEC earnings release](https://www.sec.gov/Archives/edgar/data/92230/000009223026000108/ex991-3q26.htm).

The report's macro chronology checks against the Fed: September 16 raised the target range to 3.75–4.00%; October 28 held it there. We have not independently verified its December market-implied probability. [September statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm), [October statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm).

## Where interpretation exceeds evidence

1. **Low correlation does not reject rotation.** Rotation toward equal-weight equities, value, banks or rate-sensitive assets can lower correlation with a capitalization-weighted market dominated by other sectors. Our existing study found RSP, VNQ and Treasuries strengthening while QQQ weakened. These are compatible observations. The report's own KBE correlation near 0.99 also contradicts the literal claim that KRE decoupled from everything. Even its regional-only correlation of 0.894 remains strong in absolute terms.
2. **Missing explanatory power is not evidence of no fundamental influence.** June accounting changes versus YTD returns are contemporaneous associations, not a test of earnings surprises or revised future expectations. Their weak relationship with October returns does not eliminate fundamental repricing. Small Q3 samples and simple three-day KRE-adjusted reactions cannot resolve that question.
3. **The estimated 1.6-point rate contribution is a fitted association.** Shared growth/inflation news can move yields and bank equities simultaneously. In-sample regression does not isolate a causal Treasury contribution; the residual is not automatically an identified regional-bank factor.
4. **An anticipated hike is not itself a new shock.** The relevant scenario is a surprise relative to pricing and its effect on different yield maturities, funding costs and asset repricing. Falling yields can help securities values while hurting asset-sensitive banks' prospective margins.
5. **Rare rolling correlations are not reversal probabilities.** Overlapping windows are highly dependent. A 1.5th-percentile correlation does not imply a 98.5% chance of normalization, establish timing, or supply a trade signal.

## Required data and method repairs before stronger use

- Supply code, archived raw inputs, point-in-time holdings, dates and observation counts for each model. Current constituents projected backward create survival/selection bias; current weights are not historical attribution. The report acknowledges its -5.3% replica versus -6.0% actual return but that does not remove the limitation.
- Resolve CFFN/CTBI CET1 entries of zero against original filings. Do not treat potentially missing or nonapplicable regulatory fields as actual zero capital in regressions or rankings.
- Separate holding-company from bank-charter measures, TBV from BV, and nonperforming loans from nonperforming assets; show denominators and treatment of government guarantees. The summary's seven-of-twelve TBV statement mixes TBV/BV; removing HTH/SFST leaves six declines among ten actual TBV observations.
- Reconcile single-factor R-squared with reported correlations on the same sample. For example 0.501 squared is 0.251 rather than 0.282. Different date filtering may explain this; report the sample rather than assume a calculation error.
- Rerun factor results excluding the largest divergence days; use alternative start dates and genuinely out-of-sample coefficients. Account for common shocks and multiple comparisons in the constituent tests. The reported HTM-loss rally coefficient has t=-1.40, insufficient for a strong predictive claim.
- Use earnings surprises/revisions and release timestamps to examine the fundamental channel. Treat business-model classifications and headquarters geography as approximations, not verified loan exposure maps.

## PROME implication

Maintain separate judgments on price breadth, bank earnings, funding and credit. The broad rebound is evidence against describing KRE as already reflecting generalized distress. It does not invalidate specific WAL/OZK/FLG issues, nor justify inferring their resolution from ETF strength. Existing REGINALD work already emphasizes concentrated rather than tier-wide severity; this report supplies additional market evidence consistent with that distinction.

The highest-value follow-up is a corrected comparison of the rebound's strongest and weakest banks using comparable Q3 credit/funding measures and forward earnings changes. This is a research recommendation, not a new desk launch or standing tracker.

## Verification and provenance

Original supplied path: `/mnt/c/Users/willi/Downloads/KRE_regional_banks_full_report.md`; unchanged snapshot: `input_report.md`. SHA-256 in `verification.json`.

Run from repo root: `.venv/bin/python3 PROME/reports/2026-11-02_kre-external-report-review/verify.py`.

Independently recalculated using our saved ETF dataset: 63-session KRE–KBWB correlation 0.719338; minimum in 2026 of 0.632408 on September 15; historical percentile 1.528%. Our baseline has 3,666 rolling windows versus the report's 3,708, so the percentile is approximately corroborated, not an exact replication of its historical sample. Both use Yahoo prices; this is independent calculation, not independent vendor validation.

Constituent checks use the supplied rounded table, not independent stock-price retrieval. We did not audit all 167 FDIC mappings or all 16 Q3 releases. Primary-source spot checks and their interpretive limits are stated above. No owner files or canonical grades were changed.
