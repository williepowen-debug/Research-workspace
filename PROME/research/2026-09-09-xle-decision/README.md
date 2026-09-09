# XLE September 30 $65 calls: first decision research

September 9, 2026, morning. PROME synthesis for Will; research authorized in this conversation. BRENT is being opened separately by Will. This is a research artifact, not a new trading rule or a domain-owner forecast. Existing approved exit remains the recorded instruction; no order or fill is recorded here.

**Provisional conclusion:** the evidence supports Will's objection that rising oil can still help XLE. It does not establish that retaining these September calls has better expected value than taking today's recoverable premium. Selling the calls is compatible with remaining bullish on oil, particularly given the USO exposure shown in Will's screenshot. A green day improves potential exit proceeds; it does not by itself invalidate the exit or establish a new hold thesis.

## Position and quote evidence

**VERIFIED at the supplied screenshot, whose capture time is not visible:** XLE September 30, 2026 $65 calls, quantity 2; displayed premium $1.92, value $384.00, cost $455.35, day change +$86.00 / +28.85%, lifetime P/L −$71.35. This is a positions image, not an order/activity receipt or a bid/ask screen. Open orders and executable sale price remain **UNKNOWN**. The image was supplied in this September 9 conversation; no broker execution access is used.

The same image shows USO shares $5,499.21 (37 shares) plus the October 16 $135 call $1,680.00 (1 contract), totaling **$7,179.21**, or **18.64%** of the displayed $38,510 account. Including XLE brings these energy positions to 19.64% by displayed market value. This is account-specific, excludes other accounts, and is not a delta-adjusted risk measure. Cash shown is $17,489.02. Holding the XLE pair risks its recoverable value from here, about 1% of this account at the screenshot mark; original cost is a separate historical P/L question.

Public capture [options.json](options.json), September 9 09:42:06–09:42:07 EDT:

| Field | Observed result | Use |
|---|---|---|
| Exact contract | XLE260930C00065000; REGULAR contract size | Matches requested expiry/strike; screenshot quantity/value implies 100 multiplier |
| September 30 $65C bid / ask | 0 / 0 | **Rejected as unusable**, not a worthless-option conclusion |
| Its last trade | $1.49, September 8 15:51:13 EDT | Historical, not current |
| Vendor IV | 0.00001 as a fraction | **Rejected** alongside absent quotes |
| September 18 / 25 and October 16 $65 calls | Also zero bids/asks, previous-day trades | No valid term-structure or roll pricing obtained |
| Underlying last trade | $65.81, September 9 09:42:03 EDT | Dated vendor observation, not a synchronized broker quote |
| Underlying bid / ask | $65.55 / $65.59 | Inconsistent with last trade; asynchronous fields cannot prove current execution levels |

Will was asked for the broker's current bid/ask. The calculations below use **$1.92 only as a conditional sale-price reference**, not verified liquidation proceeds. A fresh retrieval is not proof of a fresh option quote.

## Exact expiration comparison

For two standard calls, expiration value is `200 × max(XLE − 65, 0)`. Selling at premium `b` yields `200 × b`. Thus expiration indifference is **XLE = $65 + b**, ignoring fees and interest on cash. At $1.92, that is **$66.92**, about 1.69% above the vendor's $65.81 underlying observation. This hurdle is achievable; the calculation alone says nothing about its probability. A sale before expiration can outperform through residual time value or rising IV without reaching that terminal hurdle.

| XLE at September 30 expiration | Pair payoff | Difference versus selling for $384 |
|---|---:|---:|
| $65 or below | $0 | −$384 |
| $66 | $200 | −$184 |
| $67 | $400 | +$16 |
| $68 | $600 | +$216 |
| $70 | $1,000 | +$616 |

The original cost implies historical expiration breakeven $67.27675 before exit/exercise costs. That is **not** the forward hold-versus-sell hurdle. At bids of $1.80 / $1.90 / $2.00, today's pair proceeds would be $360 / $380 / $400 and terminal indifference $66.80 / $66.90 / $67.00. Foregone interest on $384 over 21 days at the rate proxy below is less than $1.

Expected-value comparison requires a distribution: `200 × E[max(S_T−65,0)]` versus sale proceeds plus cash carry. Neither the probability of any oil rise nor the probability XLE exceeds $65 supplies that distribution. As an explicitly artificial two-outcome illustration, $68 at expiry versus $65 or less requires a probability above 64% for the $68 outcome to beat $384; changing the upside endpoint to $70 changes that threshold to 38.4%. These are sensitivity examples, not forecasts.

## How much does waiting cost under explicit assumptions?

**INFERRED, conditional model only:** escrowed-dividend CRR American-call approximation, 600 steps, 21 calendar days initially, strike $65, spot $65.81, rate 3.79% (September 4 [FRED DGS1MO](https://fred.stlouisfed.org/series/DGS1MO), used as an approximate continuously compounded rate). Assume a $0.385 distribution on September 21, matching the two latest historical Yahoo distributions. September's amount is **UNKNOWN**; the [issuer calendar, page 3](https://www.ssga.com/library-content/products/fund-data/etfs/us/distribution/SPDR_Dividend_Distribution_Schedule.pdf) verifies the date, not the amount. Dividends are an anticipated pricing input, not an extra surprise loss to subtract a second time.

Fit the model to the $1.92 reference: approximately **25.0% volatility**. This is a conditional fitted parameter using unsynchronized inputs, **not measured current XLE IV**. Quote-based Greek and relative-value claims remain unavailable. The approximation puts volatility on stock net of the present value of the assumed cash dividend and permits early exercise; it is not an exact discrete-dividend local-volatility model. Calendar days are rounded, and all displayed model values precede spreads and transaction costs.

| XLE scenario price on the date shown | Pair value September 16 | Pair value September 23 | September 30 payoff |
|---|---:|---:|---:|
| $64 | $144 | $99 | $0 |
| $65 | $228 | $184 | $0 |
| $65.81 | $316 | $279 | $162 |
| $66 | $340 | $305 | $200 |
| $67 | $479 | $456 | $400 |
| $68 | $641 | $629 | $600 |

At fixed spot and fitted IV, the first calendar day's modeled decay is about **$8.71 for the pair**; the September 16 value is about **$68 below** the $384 reference. Do not extrapolate daily theta linearly. If XLE is $65.81 on September 16, model value is **$269 at 20% volatility**, **$316 at 25%**, or **$414 at 35%**. Thus an IV increase can offset decay. Full grid: [scenarios.csv](scenarios.csv). Holding the same quoted stock price across an ex-dividend date presupposes that other price movement offsets the mechanical distribution adjustment; the September 23 fixed-price scenario is not a zero-total-return scenario.

Model sensitivity near the starting assumptions is about **$121 per $1 XLE move** for the pair and **$11.84 per volatility point**. That illustrates why a 1% market-value position can still have meaningful directional sensitivity. Replacing $384 of calls with $384 of shares buys only about 5.84 shares at $65.81; replacing their approximately 121-share local delta would require around $7,950 of shares and a very different downside profile. These are comparisons, not proposals. An October roll cannot be costed from today's invalid public chain.

XLE's trailing realized annualized volatility is **15.4% / 21.9% / 23.7%** over 20 / 60 / 126 completed sessions through September 8. That does not prove the calls expensive: future event risk can differ, and we lack a valid observed IV. OVX is crude-related volatility, not a substitute for this contract's XLE IV. [OIC pricing factors](https://www.optionseducation.org/optionsoverview/options-pricing) and [theta explanation](https://www.optionseducation.org/advancedconcepts/theta) support these distinctions.

## Does rising oil still transmit to XLE?

**VERIFIED computation on captured vendor/official series:** January 2023 onward, Yahoo adjusted equity closes versus [EIA Brent spot through FRED](https://fred.stlouisfed.org/series/DCOILBRENTEU), latest oil observation September 1. Returns use exact 1 / 5 / 15 US equity-session endpoints with no forward filling. Oil assessments and US closes are not simultaneous; FRED publication lag means these are contemporaneous economic relationships, not signals available to trade at that historical close. Equity data extend through September 8, but the oil relationship sample does not.

| Horizon | Rolling periods with Brent up | XLE rose in those periods | Average XLE total return | Disjoint oil-up intervals / XLE-up share |
|---|---:|---:|---:|---:|
| 1 session | 449 | 73.3% | +0.66% | 449 / 73.3% |
| 5 sessions | 443 | 80.1% | +1.96% | 86 / 77.9% |
| 15 sessions | 425 | 84.7% | +3.94% | 26 / 80.8% |

Multi-day rolling observations overlap substantially; the disjoint intervals are anchored backward from the last oil observation, and even disjoint intervals are not guaranteed statistically independent. These are descriptive fractions, **not probabilities that the current calls will pay**. Conditioning on a rise occurring during the same period is not a forecast. A WTI robustness check gives corresponding rolling XLE-up shares **75.5% / 82.2% / 84.4%**.

Splitting at February 27, 2026, with both endpoints in the regime, preserves a positive oil association. Post-split five-session oil-up intervals have mean XLE return +3.11% and 91.7% positive outcomes, but only **13 disjoint oil-up intervals** remain (12 positive). At 15 sessions only **3** disjoint post-split oil-up intervals remain. Do not promote these tiny regime samples into high-confidence trading odds.

Controlling descriptively for same-period SPY returns, the full-sample five-session oil coefficient is about **0.34**; it is about **0.18** after the regime split. These are in-sample associations, not causal elasticities or stable forecasts. The corresponding post-split SPY coefficient turns negative, emphasizing regime instability. Even with oil up and SPY down, full-sample five-session XLE returns averaged +1.73% (157 overlapping windows). A categorical claim that broad equity weakness prevents XLE from benefiting is unsupported here.

The more immediate concern is **magnitude**:

| Completed sessions through September 8 | XLE | XOM | CVX | SPY | USO |
|---|---:|---:|---:|---:|---:|
| 1 | +1.11% | +0.75% | +0.58% | −0.55% | +2.87% |
| 5 | +1.27% | −0.18% | +1.78% | −0.14% | +9.22% |
| 15 | +3.50% | −0.50% | +4.41% | −0.87% | +12.08% |

USO is an oil-futures fund, not spot crude; roll and fund effects apply. Its return is used here as the actual portfolio instrument comparison, not relabeled as Brent's return. XLE is participating, with less recent upside than USO. The [issuer's September 8 fund holdings](https://www.ssga.com/us/en/individual/etfs/state-street-energy-select-sector-spdr-etf-xle) put XOM at **19.62%** and CVX at **15.00%** (34.62% together). These supersede the earlier September 4 weights for this dated comparison. XOM's recent softness matters, but present weights are insufficient for a formal historical contribution attribution; that requires weights through each period and all holdings.

Both Yahoo Close and Adj Close are retained. Historical Close is already split-adjusted; Adj Close also adjusts distributions. Average XLE total-return minus price-return differences in the Brent sample are about 0.01 / 0.06 / 0.19 percentage points at the three horizons. Option payoff depends on actual stock price, so dividend-adjusted return statistics must not be substituted directly into the terminal strike calculation.

Fixed November/January Brent contracts were also captured, but **not used in the regression**: early history includes zero-volume far-dated observations, and September 8 bars have zero reported volume. These records cannot establish an authenticated settlement curve. No continuous-futures roll splice was used. BRENT should own the fresh matched-time curve interpretation.

## Upcoming evidence and questions for BRENT

**VERIFIED calendars:** EIA's [STEO](https://www.eia.gov/outlooks/steo/) still displayed August's report at this morning's read, with September 9 as next release; its [release schedule](https://www.eia.gov/outlooks/steo/release_schedule.php) gives the normal noon–12:15 EDT publication window. The [weekly petroleum report](https://www.eia.gov/petroleum/supply/weekly/) is holiday-delayed to September 10 at noon, with later files at 14:00 EDT. The [Fed calendar](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm) lists September 15–16. These are all before expiration; passing OPEC's meeting did not exhaust the catalyst calendar.

OPEC's [September 6 primary statement](https://www.opec.org/pr-detail/1835613-6-september-2026.html) maintains September required production into October and schedules the next meeting October 4. It does not independently prove unchanged actual output or that the market response must be zero.

Prepared questions for Will's BRENT session; **not yet delivered to or answered by that session**:

1. Update dated September 16 and September 30 oil scenarios, with downside/base/upside prices, timing and explicit subjective probabilities if supportable. Separate higher oil levels from another rise from today's levels.
2. How much of the latest rise is verified lost production/export throughput versus a reversible shipping/security premium? Identify the evidence vintage and which reports could falsify it.
3. Does the matched-contract curve show longer-lived scarcity, or mainly prompt tightness? Use the same instruments, timestamp convention and settlement/live basis. Explain whether the change should improve XOM/CVX earnings expectations within this option window.
4. In today's STEO and tomorrow's weekly report, what inventory/demand/output results would strengthen or weaken the near-term thesis? Prestate the test before reading the release. Do not reuse an old forecast as a refreshed probability.
5. Given the remaining USO shares and October call, what incremental economic exposure would retaining XLE add? If duration is the objection, TERRY needs a valid simultaneous chain and equal-risk comparison before any roll proposal.

## Decision status and remaining work

The [approved TERRY exit tracker](../../../AGENTS/TERRY/setups/XLE65C_approved-exit-tracking_2026-09-08.md) records the September 8 close test at $64.77 versus $66.50 and selects selling both at the September 9 open. The [issuer](https://www.ssga.com/us/en/individual/etfs/state-street-energy-select-sector-spdr-etf-xle) independently publishes the $64.77 close. Today's rebound does not satisfy yesterday's specified test. Whether that test was economically optimal is a separate question, still unproven. This research does not rescind the approval or assert a completed exit.

**First pass complete:** captured price histories; oil/equity relationship and regime checks; conditional call valuation; portfolio comparison; primary-source catalyst calendar. **UNKNOWN / outstanding:** executable broker bid/ask and open orders, confirmed fill if any, valid observed IV/term structure, September dividend amount, fresh BRENT physical/curve forecast, full historical constituent attribution, and a probability-weighted hold-versus-sell conclusion. The two scheduled EIA releases had not occurred at the research cutoff. No background job or follow-up agent was launched.

## Reproduction and verification

From repository root, `.venv/bin/python3 PROME/research/2026-09-09-xle-decision/analyze.py` reproduces [results.json](results.json) and the scenario CSV from captured inputs. `collect.py` refreshes public inputs and **overwrites captures**; preserve this dated snapshot before any refresh. Its graph CSV requests returned 404, and the successful `collect.py --fred-only` fallback used the official FRED API. [capture.json](capture.json) records transport and vintages without credentials.

Analysis self-checks passed: unique/sorted and matching equity calendars, positive/non-null closes, September 8 last completed session, exact expiry payoffs, price/volatility/dividend sensitivity directions, and 400/600/1200-step convergence within $0.02 per option. Calendar agreement is not an independent exchange-calendar audit. Models and descriptive statistics remain subject to the stated source and synchronization limits; no backtested trading edge is claimed.
