# Breadth, credit and historical outcomes — first pass, October 19, 2026

**The evidence favors a fragile, selective market with recent broadening, rather than an established sequence of steadily deteriorating participation. Narrowing was followed by smaller average gains in our historical ETF proxy samples, but it was not a dependable selloff signal. The fundamental refinancing-attribution test is still incomplete.**

Will approved three investigations in this thread. Persistence and historical proxy analyses are calculated and checked; the credit mechanism has a sector-matched quality screen and a three-filing pilot, not a completed market-wide maturity test. No trade, standing monitor, owner grade or threshold changed. All comparable closing-data results below end **October16**; Monday's earlier intraday snapshot remains separate.

## 1. Is participation persistently deteriorating?

| Completed window | SPY adjusted return | RSP adjusted return | IWM adjusted return | Current-basket stocks up / covered |
|---|---:|---:|---:|---:|
| 5 sessions, October9–16 | −1.97% | +0.49% | −3.05% | 348/501, 69.5% |
| 20 sessions, September18–October16 | +0.20% | +1.23% | −4.81% | 291/492, 59.1% |
| 60 sessions, July23–October16 | +3.65% | +1.40% | −7.17% | 241/485, 49.7% |

The longer window contains meaningful weakness: smaller companies lag, and about half the available current basket is lower. The shorter windows show recovery across many stocks. This is consistent with Monday's rebound being narrow without establishing that every preceding week was narrowing.

Across60 reconstructed completed sessions, five had SPY up with a majority of covered stocks down; **none were in the latest20 completed sessions**. Daily coverage500–503. This is a current-holdings reconstruction, not an official historical index A/D series. Fifty-day moving-average coverage221/486 above;200-day237/447 above. Those partial denominators must never become percentages of all503.

Limits: October16 holdings applied retrospectively; share classes separately counted; raw constituent prices omit distributions and may contain corporate-action artifacts. Stable cohorts require every exact SPY session, never bridge gaps. Two daily raw moves exceed30% (MRNA August19, PTC October5); corporate-action/event verification remains open. Counts and medians are exploratory; historical membership and official new-high/new-low census were not recovered. ETF results use adjusted daily prices and avoid today's constituent-survivor reconstruction, but have sector/style exposures.

## 2. Does credit explain which stocks are weakening?

Over the same20 sessions, HY OAS widened63bp, CCC214bp and IG8bp. These are observed spread changes, not proof of a causal equity channel. QUAL gained2.62% while IWM fell4.81%; high-beta SPHB fell5.45%. Another quality proxy, SPHQ, gained only0.22%, showing that the choice of basket matters. Quality is not a pure refinancing factor.

The stronger screen compares current QUAL members with other SPY holdings **within each sector**, then gives each sector equal weight. All503 SPY security lines mapped unambiguously to issuer sector-ETF holdings datedOctober16;113 intersect QUAL's118 equity lines.

| Window | Quality-member minus other-stock mean return, average across9 sectors excluding financials/REITs | Sectors with positive gap |
|---|---:|---:|
| 5 sessions | +0.51 percentage points | 6/9 |
| 20 sessions | +1.44 percentage points | 7/9 |
| 60 sessions | +0.21 percentage points | 6/9 |

The20-session gap stays positive when any one sector is removed: +0.76 to+2.03pp. This reduces the chance that one broad sector alone explains it. It does **not** control for industry, size, valuation, earnings events or all other quality attributes. Current QUAL membership is applied retrospectively and nonmembership does not establish high debt. Raw constituent returns omit distributions. QUAL's sector neutrality is against MSCI USA, not the S&P500.

**Working inference:** investors appear selective about company quality as well as sector and size. A retreat from financially vulnerable borrowers is plausible, but refinancing risk has not been isolated.

The [telecom pilot](TELECOM-PILOT.md) verifies three pre-window filings and demonstrates why debt/cash shortcuts fail: Verizon current debt includes substantial receivable-backed funding; AT&T cash preceded an acquisition; lease, hedge and facility perimeters differ. All three stocks fell over20 sessions but recovered last5. No stress ranking is assigned.

**Unfinished required work:** construct a broader industry/size-matched cohort with fundamentals available before the return window; reconcile12/24-month unsecured maturities, unrestricted cash, committed facilities, interest coverage, net floating exposure and intervening transactions. The repo search found no ready reconciled dataset. Standard SEC tags alone can silently return years-old figures, so missing fields remain missing. This is substantive remaining work under Will's existing approval, not a request for another approval.

## 3. What happened historically?

Definitions were written before the new calculation in PLAN.md. Main proxy: trailing20-session SPY adjusted return positive, RSP/SPY ratio return negative. Broadening counterpart: same positive SPY condition, ratio nonnegative. This is **equal-weight underperformance, not the exact majority-of-stocks-falling condition**.

Daily ETF history begins2003; no1999 test. Formation dates eligibleMay30,2003–April17,2026, with all126-session outcomes complete throughOctober16. Select chronologically at least126sessions apart within each arm. Different arms can overlap and represent different regimes; they are not matched experimental groups. Requiring the longest horizon excludes newer observations even when shorter outcomes have matured.

| 20-session formation state | Selected observations | Mean subsequent1-month return | Mean3-month return | Positive3-month outcomes | At least10%3-month closing drawdown | Mean6-month return |
|---|---:|---:|---:|---:|---:|---:|
| Rising index, equal weight lagging | 42 | +0.52% | +1.86% | 28/42 | 7/42 | +5.47% |
| Rising index, equal weight keeping up | 42 | +1.50% | +3.28% | 32/42 | 7/42 | +6.53% |
| Deterministically spaced unconditional benchmark | 46 | See analysis.json | +1.77% | 31/46 | 11/46 | See analysis.json |

One/three/six months mean21/63/126 equity sessions. Drawdown is peak-to-trough **closing** adjusted-price decline within the following window; not an intraday drop or simply loss from entry. All event dates and outcomes, including adverse cases, are in analysis.json.

The sample supports smaller average gains after narrow advances. It does **not** show a higher three-month10% drawdown frequency in the main comparison. Most selected narrow episodes still had positive three-month and six-month outcomes. These counts are historical descriptions, not calibrated probabilities for today.

Declared60-session formation check: narrow n36, mean subsequent63-session return+2.92%, positive26/36; broad n35, mean+4.31%, positive27/35. Posthoc sampling-phase check across126 starting offsets keeps narrow-minus-broad mean returns negative (20-session formation−1.60 to−1.03pp;60-session−1.89 to−1.29pp). This is sensitivity analysis of the same sample, not out-of-sample validation, and does not remove regime confounds.

### Credit overlay is too small to evaluate

FRED now supplies only three years of these credit series. Recovered history beginsOctober20,2023; matched20-session formations beginNovember17,2023. Only **three** internally spaced index-up/equal-weight-lagging/HY-widening observations have full126-session follow-through. Their positive outcomes cannot validate or refute a general rule. Requiring at least20bp widening still produces three selected events, with mean three-month return changing to+1.54% and one10% closing drawdown. The result's sensitivity and tiny sample prevent a useful historical risk estimate.

OAS observation dates are not verified release-time availability. This is a retrospective association study, **not an executable historical trading backtest**. No unobserved pre-2023 credit history was imputed or substituted.

### External primary evidence

[Bespoke's July23,2026 study](https://bespokeinvest.substack.com/p/extreme-price-and-breadth-divergences) also found that similar one-day sector divergences often preceded gains, but its definition and tiny sample differ. [HISTORICAL-EVIDENCE.md](HISTORICAL-EVIDENCE.md) records it, systematic technical-indicator counterevidence and helper verification. The earlier historical explanation identified a real vulnerability mechanism; this fuller evidence does not support treating that mechanism as a reliable market-top timer.

## Sources, checks and continuation

- Prices: public Yahoo chart daily adjusted ETF series, exact URLs/clocks/hashes in source-receipt.json; old SPY holdings/security snapshots in sibling2026-10-19_breadth. New and earlier recent ETF histories agree exactly on64 common bars for5 core proxies. This is same-vendor consistency, not independent-source validation.
- Holdings: State Street sector ETF files and iShares QUAL CSV, October16; quality-source-receipt.json. [QUAL issuer methodology](https://www.ishares.com/us/products/256101/ishares-msci-usa-quality-factor-etf).
- Credit: [FRED HY](https://fred.stlouisfed.org/series/BAMLH0A0HYM2), [CCC](https://fred.stlouisfed.org/series/BAMLH0A3HYC), [IG](https://fred.stlouisfed.org/series/BAMLC0A0CM); credit-source-receipt.json. Credit history truncation is stated in source notes.
- validate.py independently recomputes1,299 event-horizon returns/drawdowns, all spacings, quality CSV sector gaps and breadth partitions. Read-only helper independently checked outcome arithmetic and found the at-least20bp wording mismatch; corrected before final persistence, main results unchanged.
- Initial curl attempts carrying a browser User-Agent returned empty credit files; explicit no-header retries succeeded and have separate receipts. Initial sector parser admitted the cash ticker `-`; its conflict assertion stopped the run. Parser now accepts only tradable ticker forms; all503 final mappings unique. No failed intermediate result was published.
- Raw source bundle and member hashes preserve reproducibility. Run analyze.py, quality_screen.py --reuse, then validate.py after extracting sources.tar.gz into raw/. Network pull scripts create new vintages and must not overwrite this study silently.

**Next substantive step under existing approval:** finish the company-level matched refinancing dataset, starting with subsequent-event/debt-note reconciliation and recording coverage/exclusions. An official historical point-in-time A/D/new-high-low series and longer licensed/archive credit history would improve the exact-condition test; their absence is not repaired by the ETF proxy. No new standing collection protocol was installed. Domain owners retain thesis/grade judgment.
