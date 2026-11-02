# What is happening with regional-bank stocks?

**Synthesis prepared November 2, 2026; completed-session evidence through October 30.** [Study map](EVIDENCE_GUIDE.md) · [Unresolved questions](OPEN_QUESTIONS.md)

## The central picture

Regional-bank stocks have been following a different rhythm from much of the market. That difference is real in the saved data and has lasted for months. It does not by itself establish healthier banks, a permanent regime change, or the direction of the next move.

Two separate questions explain much of the apparent contradiction:

1. **Where did prices finish?** KRE outperformed KBWB by a modest amount over the 63-session window. A later study suggests much of that advantage came from weakness in major capital-markets banks that KRE does not own.
2. **How did they get there?** KRE and other bank stocks moved together less consistently each day. That anomaly predates the headline shocks and survives removal of unusual days.

Two runners can finish near one another after following very different paths. Return comparisons describe their finish; correlation describes how consistently their steps lined up. Neither establishes the business health of the banks underneath.

## 1. The rally and the longer decline are both real

| Period, adjusted-close basis | KRE | KBWB | Meaning |
|---|---:|---:|---|
| August 3 close to October 30 close | −6.02% | −8.43% | KRE lost less; advantage about 2.41 percentage points |
| October 14 close to October 30 close | +5.06% | +3.43% | A rebound inside the longer decline |

The supplied constituent table shows 149 of 167 stocks positive in the rebound, but only 31 positive over the longer window. Those counts were checked against the supplied rounded appendix, not independently rebuilt from every stock history. Broad participation means the buying was widespread; it does not establish widespread credit improvement.

The first ETF study also found strength outside banks: equal-weight equities, property stocks and Treasuries outperformed KRE over some recent horizons while technology weakened. Rotation is compatible with the evidence, not ruled out by low correlation.

Sources: [ETF study](reports/2026-11-02_kre-etf-relationships/REPORT.md), [constituent review](reports/2026-11-02_kre-external-report-review/REVIEW.md), [Study 6 numerical receipts](reports/2026-11-02_study6-drivers/review.json).

## 2. Reduced co-movement is the best-established discovery

The typical historical 63-session KRE–KBWB correlation in our saved sample is about 0.94. For the 63 returns from August 4 through October 30 it is 0.719.

| Sensitivity check | KRE–KBWB correlation |
|---|---:|
| All 63 sessions | 0.719 |
| Exclude September 14 | 0.749 |
| Exclude October 22 | 0.753 |
| Exclude both | 0.785 |
| Exclude five largest daily return gaps | 0.821 |
| Exclude ten largest daily return gaps | 0.8535 |

Removing extreme days raises correlation. But applying the same removal to historical windows raises their correlations too: the top-five and top-ten results remain near the bottom 1–1.3% of their matched histories. The five largest days account for 43.8% of squared daily gaps; that is different from their contribution to cumulative returns.

Independent 21-session blocks show correlations of 0.677 in June 3–July 2 and 0.640 in July 6–August 3. The change therefore existed before September 14 and October 22. Persistence is observed through October 30, not proven into the future.

Sources: [five-day tests](reports/2026-11-02_kre-cato-sensitivity/results.json), [ten-day and block checks](reports/2026-11-02_decoupling-stress-test/checks.json). These reproduce calculations on the same saved vendor data. Overlapping historical windows are not independent episodes; percentiles are not reversal probabilities.

## 3. Broad-market exposure matters, but the historical comparison matters too

KRE's recent single-factor sensitivity to SPY is about 0.328, compared with 0.825 for KBWB. This describes a fitted relationship across daily returns, not a promised response to the next 1% market move.

After removing each fund's fitted relationship with SPY, their residual correlation is 0.728, only slightly above the raw 0.719. Its historical rarity changes more because the historical benchmark also changes:

| Historical starting point | Current residual correlation | Percentile in our saved sample |
|---|---:|---:|
| 2012 | 0.728 | 10.37% |
| 2015 | 0.728 | 2.82% |

Earlier discussion called the market-adjusted relationship less exceptional using the first baseline. Study 6 exposed the second. **Both must travel with the conclusion.** Market exposure is an important descriptive dimension; it does not remove all unusual bank-specific co-movement, and it is not a causal explanation by itself.

The report's statement that low volatility explains roughly half the anomaly is not an established causal decomposition. Scaling both return series down does not mechanically change correlation. The balance of common and separate shocks matters; substituting median volatilities into an identity does not uniquely allocate causes.

Sources: [stress-test checks](reports/2026-11-02_decoupling-stress-test/checks.json), [baseline comparison](reports/2026-11-02_study6-drivers/review.json).

### Study 4 adds stronger evidence for a market-wide explanation

The later-supplied Study 4 asks whether SPY itself has become a less useful yardstick for value and smaller stocks. Its saved data show SPY's correlation with equal-weight RSP at about 0.64, and unusually low SPY sensitivity across all ten comparison ETFs, including several nonbank sectors.

Controlling for market, size, value, momentum and yields raises KRE's fitted R² to about 0.62. Its market-factor loading is about 1.09, even though its simple SPY beta is 0.33. These are different quantities: the first separates overlapping influences; the second combines them. When value moves against SPY, a fund exposed to both can have low overall SPY sensitivity without losing its usual conditional market exposure.

The remaining KRE–KBWB residual correlation is about 0.54, near the model's historical 14th percentile (about 24th after volatility matching). This supports a broader market/style explanation and a modest unresolved bank-specific remainder. It does not establish that banks' credit risk improved. These controls differ from the SPY-only baseline comparisons above.

The supplied package is reproducible: selected scripts regenerated 17 outputs exactly. But October uses ETF proxies for unavailable French factors, and decompositions depend on the chosen model. Its “frozen-loading forecast” uses future realized factor relationships, so it is a conditional diagnostic, not proof that the beta collapse could have been forecast in advance. [Study 4 review and checks](reports/2026-11-02_study4-market-leadership/REVIEW.md).

## 4. Holdings composition may explain much of the finishing gap

Study 6 removes JPMorgan, Bank of America, Goldman Sachs, Morgan Stanley and Citi from KBWB and renormalizes the remaining holdings. It reports:

| August 3–October 30 | Return |
|---|---:|
| KRE | −6.02% |
| KBWB | −8.43% |
| Reconstructed KBWB excluding those five | −6.62% |

If verified, the return advantage shrinks from 2.41 points to 0.60. Its reconstructed October rebound is 5.00%, almost identical to KRE's 5.06%. This would explain much of relative performance through businesses absent from KRE, rather than exceptional regional-bank strength.

**This is reported-only attribution.** We have not audited the holdings reconstruction. Its component table also fails to add: 1.04 + 0.78 − 0.37 = 1.45 points, not its stated 1.81. Removing the whole group may still explain 1.81 points, but the parts require reconciliation. Accounting for which securities dragged on returns does not prove why they fell or that the weakness is temporary.

The same report finds unusually weak KRE co-movement even against traditional commercial banks. That separate result remains unreplicated, but would further distinguish the endpoint explanation from the daily-path question.

Sources: [Study 6](reports/2026-11-02_study6-drivers/input_report.md), [review](reports/2026-11-02_study6-drivers/review.json).

## 5. Falling yields can help banks while credit conditions worsen

Lower yields can improve the market value of existing fixed-rate securities and reduce some borrowers' refinancing pressure. Funding costs may ease, but deposits and assets reprice at different speeds, so margin effects vary by bank. Falling yields can also accompany growth fears, weaker demand and expected loan losses. Relief and deterioration can coexist.

The recent regressions show a negative relationship between bank-stock returns and yield changes: banks tended to benefit from falling yields after the chosen controls. A limited saved-data check supports this sign for both KRE and KBWB. Study 6 reports nearly identical sensitivities for KRE and traditional banks, so rate relief may help explain a shared rally without explaining regional separation.

Unrealized securities losses have not consistently identified the stocks most responsive to rate relief in these studies. That weakens a simple securities-loss explanation; it does not disprove every balance-sheet channel. Funding measures show suggestive associations, but some disappear when a few banks are excluded.

Study 6's recent HY-spread coefficients are statistically uncertain. Failure to detect a negative relationship does not prove banks have stopped responding to credit. Its suggestion that widening was concentrated in AI borrowers is untested here. The earlier rate study also classified several analogs as credit-widening using proxies even though their actual HY spreads narrowed.

Sources: [rate study review](reports/2026-11-02_kre-study3-review/review.json), [specification addendum](reports/2026-11-02_kre-study3-review/spec_addendum.json), [Study 6 review](reports/2026-11-02_study6-drivers/review.json).

## 6. Fundamentals remain mixed; the forecasting evidence is weaker

The supplied work finds broad profitability improvement through June, but modest associations with YTD stock returns and little explanatory power for the short rebound. Its Q3 sample contains improving margins alongside rising deposit costs and uneven credit. The existing primary-source review records specific examples: Texas Capital's stronger margin alongside rising criticized loans; Preferred Bank's troubled-loan transfer rather than proven resolution; and Truist's securities-sale loss requiring a full earnings/capital bridge.

Those examples are evidence against collapsing earnings, funding and credit into one good/bad label. They are not a full audit of the sector. Individual WAL/OZK/FLG problems remain separate owner questions; neither ETF strength nor one troubled bank settles generalized stress.

Historical falling-yield studies suggest possible later KRE underperformance versus KBWB, but sampling choices, thin groups and credit-proxy failures limit confidence. Relative underperformance could occur while both funds rise. There is no dependable forecast here of an outright KRE decline or a timing signal for options.

Sources: [fundamentals review](reports/2026-11-02_kre-external-report-review/REVIEW.md), [rate study](reports/2026-11-02_kre-study3-review/input_report.md), [open questions](OPEN_QUESTIONS.md).

## Terms in plain language

| Term | Meaning here |
|---|---|
| KRE / KBWB / XLF | Regional-bank ETF / broader banking ETF including major banks / broader financial-sector ETF; overlapping, not disjoint groups |
| Correlation | How consistently daily returns move together; not relative return or business health |
| Beta | Fitted sensitivity to a chosen variable, under a stated model and window |
| Partial correlation | Correlation after removing fitted relationships with specified controls |
| R² | Share of sample return variation explained by a regression; not causal certainty |
| NIM / ROA | Net interest margin / return on assets; profitability measures |
| HY OAS | High-yield corporate-bond spread adjusted for embedded options; not a direct bank-loan loss measure |
| AOCI / HTM | Accumulated other comprehensive income / held-to-maturity securities accounting classification; economic exposure and accounting recognition differ |
| Basis point / percentage point | 0.01 percentage point / arithmetic difference between percentage rates or returns |
| Historical percentile | Rank within a specified sample, not probability of a future event |

The working conclusion is persistent reduced co-movement with stronger evidence for a broad market/style explanation, while causality remains incomplete. Holdings composition is a separate proposed explanation for cumulative outperformance. Neither establishes improving credit or an inevitable reversal. These are research findings, not owner-grade changes or trading instructions.
