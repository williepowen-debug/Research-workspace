# **Market Microstructure and the Reflexivity of Modern Derivatives: A Comprehensive Analysis of Gamma, Vanna, and Dealer Hedging Dynamics**

The transition of global financial markets from a regime of fundamental value discovery to one dominated by structural flows and derivative-driven reflexivity represents a fundamental shift in market microstructure.1 At the center of this transformation is the role of the options dealer, whose mechanical hedging requirements often dictate the path of least resistance for underlying assets, particularly the S\&P 500 (SPX) index.3 The proliferation of zero-days-to-expiration (0DTE) options, which now frequently account for over 50% of total daily SPX volume, has compressed the timeframe of these hedging flows, creating a environment where intraday price action is increasingly decoupled from macroeconomic data and instead driven by the expiration of billions in notional delta.5 To navigate this landscape, professional market participants utilize a suite of second-order Greeks—Gamma, Vanna, and Charm—to anticipate the reflexive behavior of market makers and identify structural support and resistance levels that are invisible to traditional technical analysis.8 This report provides an exhaustive analysis of these metrics, their calculation methodologies, and their practical application in institutional risk management and alpha generation.

## **Quantitative Framework for Dealer Exposure Metrics**

The primary objective of an options dealer is to facilitate liquidity while maintaining a delta-neutral position.3 Because every option contract possesses directional sensitivity (delta), dealers must constantly trade the underlying asset or its futures equivalent to offset the risk of the options they have written to customers.11 The metrics tracked by professional desks quantify the rate at which this hedging must occur under different market conditions.

### **Net GEX: The Second Derivative of Price**

Net Gamma Exposure (GEX) measures the rate of change of an option’s delta with respect to the underlying price.3 For a dealer, GEX represents the "acceleration" of their hedging requirement.9 If the underlying asset moves, the dealer's delta changes, requiring an offsetting trade in the spot or futures market to regain neutrality.3

The calculation methodology for aggregate Net GEX involves a summation of gamma across the entire options chain, weighted by open interest and the assumed directionality of the dealer's book.9 The standard institutional model assumes that dealers are net short call options (sold to retail speculators) and net long put options (bought from institutional hedgers).8

![][image1]  
In this formulation, ![][image2] denotes the spot price and ![][image3] is the contract-level gamma.9 The multiplication by ![][image4] and ![][image5] normalizes the exposure to reflect the dollar value of the underlying that must be traded for every 1% move in the index.3

| GEX Reading | Interpretation | Market Environment | Dealer Behavior |
| :---- | :---- | :---- | :---- |
| **High Positive** | Bullish / Neutral | Stabilizing; Mean Reverting | Buy Dips / Sell Rallies 1 |
| **Near Zero** | Transitional | High Noise; Unpredictable | Minimal Hedging Necessity 14 |
| **High Negative** | Bearish / Volatile | Destabilizing; Trending | Sell Dips / Buy Rallies 1 |

Historical readings for SPX GEX suggest that gross gamma exposure can reach $80 billion, while net GEX typically oscillates between ![][image6] several billion dollars.2 In a positive GEX environment, dealers act as a volatility dampener, providing liquidity to the market by buying as prices fall and selling as prices rise.1 Conversely, a negative GEX environment creates a "gamma squeeze" or a "liquidity vacuum," where dealers are forced to trade in the same direction as the market move, amplifying trends and increasing the probability of "gap" moves.2

### **The Gamma Flip Level and Volatility Regime Shifts**

The Gamma Flip Level, also known as Zero Gamma, is the estimated price at which the aggregate dealer position transitions from net positive to net negative gamma.14 This level serves as the primary boundary for market regime identification. Above the Gamma Flip, realized volatility tends to be suppressed as dealers stabilize price action.2 Below the flip, the market enters a "Short Gamma" regime where hedging flows become destabilizing.1

The location of the Gamma Flip is dynamic, shifting intraday as options are traded and as the Greeks decay.3 Professional desks track the distance between the spot price and the Gamma Flip to gauge the "margin of safety" in the current volatility regime.17

### **Vanna Exposure: The Volatility Feedback Engine**

Vanna is a second-order Greek that measures the sensitivity of an option’s delta to changes in implied volatility (IV).3 For dealers, Vanna Exposure (VEX) quantifies how their hedging requirements will shift if market fear (volatility) rises or falls.4

![][image7]  
Vanna exposure is particularly significant because of the high correlation between spot price and IV (the "leverage effect").4 In most market conditions, when the spot price falls, IV rises. If a dealer is short OTM puts, those puts have positive vanna.8 As IV rises during a market drop, the vanna effect causes the delta of those puts to become more negative, forcing the dealer to sell more of the underlying to remain delta-neutral.4 This creates a "vanna-induced selling loop".4

| Vanna Dynamic | Market Context | Dealer Requirement | Resulting Price Action |
| :---- | :---- | :---- | :---- |
| **IV Crush (Falling IV)** | Post-FOMC; Post-Earnings | Forced Buying (Covering Shorts) | "Vanna Rally" 7 |
| **IV Expansion (Rising IV)** | Market Panic; Hedging Demand | Forced Selling (Increasing Shorts) | Accelerated Downside 4 |

Professional traders use Vanna as a leading indicator of "volatility-driven" price moves.8 A high positive VEX reading suggests the market is "coiled" for a rally if a volatility-dampening event occurs.8 Current readings in early 2026 show that vanna exposure remains a dominant factor in post-event market drifts.6

### **Charm Exposure: The Mechanics of Time Decay**

Charm, or delta decay, measures the rate of change of an option's delta with respect to the passage of time.3 Unlike Gamma or Vanna, which require price or volatility movement to trigger hedging, Charm-driven hedging occurs simply because the clock is ticking.4

![][image8]  
As options approach expiration, their deltas gravitate toward their terminal values (0 or 1).8 If a dealer is short OTM puts that are expiring in two days, the delta of those puts will decay toward zero every hour.21 To maintain neutrality, the dealer must buy back the short underlying positions they held as a hedge.8 This creates a consistent intraday "bid" known as charm flow.21

| Charm State | Open Interest Concentration | Dealer Hedging Impact | Expected Intraday Pattern |
| :---- | :---- | :---- | :---- |
| **Positive CEX** | Short OTM Puts | Forced Buying of Underlying | Steady Upward Drift (Grind Higher) 8 |
| **Negative CEX** | Short OTM Calls | Forced Selling of Underlying | Steady Downward Pressure (Fade) 21 |

Charm flows are most potent during OPEX week and are a primary driver of the "afternoon grind" often seen in range-bound markets.21

## **Structural Indicators: Barriers and Triggers**

Market structure is defined not just by the Greeks, but by the physical concentration of open interest at specific strike prices.11 These concentrations act as psychological and mechanical anchors for price action.1

### **Put Wall and Call Wall Dynamics**

The Put Wall and Call Wall represent the strikes with the highest net gamma or open interest in the current options complex.2

1. **The Put Wall:** This is identified as the major structural floor for the market.2 As the index approaches this level, dealers who are long puts (the standard assumption) must buy the underlying aggressively to hedge the surging delta.2 This creates a "mechanical bid" that makes the Put Wall difficult to breach on a closing basis.2  
2. **The Call Wall:** Conversely, the Call Wall is the "ceiling".2 Dealers who are short calls must sell the underlying as the market rises toward this level to offset the increasing delta of the calls.2

| Level | Statistical Significance | Strategy |
| :---- | :---- | :---- |
| **Call Wall** | Holds in 83% of sessions (Intraday) | Sell calls/call spreads at or above 23 |
| **Put Wall** | Breach leads to 14bps 1-day return | Buy reversal/Sell puts at level 26 |

### **The Volatility Trigger**

The Volatility Trigger (VT) is a proprietary indicator that identifies the specific price level below which realized volatility is modeled to expand significantly.18 It is typically located between the spot price and the Put Wall.25

The VT represents the "event horizon" for market makers.25 Above this level, dealers are generally "stabilizing".19 Once the market falls below the VT, dealers transition into a "Short Gamma" posture where they must sell into weakness to manage risk.18

| Volatility Metric | SPX Above Vol Trigger | SPX Below Vol Trigger |
| :---- | :---- | :---- |
| **Avg. 5-Day Realized Vol** | 13% | 18% 25 |
| **Std. Dev. 1-Day Return** | 0.9% | 1.3% 25 |

### **Dealer Delta: Net Directional Exposure**

Dealer Delta measures the aggregate directional position of market makers.3 Unlike Gamma, which measures the *change* in delta, Dealer Delta tells us the total amount of the underlying asset dealers must hold to be neutral at the current moment.9

A high positive Dealer Delta indicates that dealers are net long the underlying (hedging a net short call position), while a negative Dealer Delta suggests they are net short (hedging a net short put position).10 Transitions in Dealer Delta, particularly when price crosses a "Delta Transition Zone," are often leading indicators of trend acceleration.7

## **Intraday Evolution and Patterns in the 0DTE Era**

The intraday behavior of the SPX has been fundamentally altered by the dominance of 0DTE options.5 With expirations occurring every session, the market exists in a state of constant structural realignment.7

### **0DTE-Specific GEX vs. Longer-Dated Exposure**

The Greeks of a 0DTE option are mathematically distinct from longer-dated contracts.22 Because time-to-expiration (![][image9]) is near zero, the gamma (![][image3]) of an at-the-money (ATM) 0DTE option spikes to near-infinity.3

![][image10]  
As ![][image11], the ![][image12] term in the denominator causes gamma to explode.22 This makes 0DTE contracts extremely reactive to price movements, forcing dealers to rebalance hedges every few minutes.4

| Characteristic | 0DTE Gamma | Monthly (30D) Gamma |
| :---- | :---- | :---- |
| **Sensitivity** | Extreme; Spikes at ATM | Moderate; Distributed |
| **Vega (Vol)** | Negligible 29 | Significant |
| **Theta (Time)** | Maximum (Accelerates hourly) | Lower (Daily decay) |
| **Market Impact** | Drives Intraday Mean Reversion | Drives Systematic Trends |

The CBOE notes that 0DTE flows typically supply "positive gamma" to the market because the majority of customer volume consists of selling options (e.g., iron condors, credit spreads).5 This creates an intraday environment where volatility is suppressed by dealer "buy-on-dip" flows.5

### **The Typical Intraday GEX Lifecycle**

1. **The Morning Open (9:30 \- 10:30 AM):** High activity as dealers adjust to overnight gaps.29 0DTE volume spikes as traders set up their intraday ranges.5 GEX is often erratic as the "Gamma Landscape" for the day is established.5  
2. **The Mid-Day Lull (11:00 AM \- 2:00 PM):** The "Pinning" regime.1 If GEX is positive, the index often gravitates toward the strike with the highest gamma (Max GEX) and enters a narrow range.1 Dealer hedging acts as a "magnetic force," preventing breakouts.1  
3. **The Afternoon Unwind (2:30 \- 4:00 PM):** The most volatile period.7 As 0DTE options approach their final hour, their gamma reaches its peak.3 Dealers must unwind their hedges as these options expire.5 If the market is trending, this unwind can lead to "melt-ups" or "flushes" as the structural support of the 0DTE bid vanishes.5

## **Patterns Around Options Expiration (OPEX)**

Options expiration, specifically the Monthly OPEX (third Friday), creates predictable structural anomalies that professional traders exploit.23

### **The Pinning Effect and Strike Magnets**

"Pinning" is the tendency of the underlying asset to settle at a major strike on expiration day.23 This is driven by the fact that as an option approaches expiration, its gamma is highest.3 If a dealer is long gamma (the stabilizing side), their hedging activity—buying below the strike and selling above it—physically prevents the price from moving away from that strike.1

Major quarterly expirations can see 50% or more of the total SPX gamma concentrated in a single session.23 In these cases, the pinning effect is so dominant that it can neutralize even significant fundamental news catalysts.22

### **The OPEX Release and Drift**

Once the options expire, the dealer hedges associated with that open interest are removed.23 This "unwind" releases the market from its pinning constraints.23 Historically, the week following a major OPEX is characterized by the "OPEX Drift," where the market establishes a new directional trend as structural flows reset.23

| OPEX Stage | Market Behavior | Structural Driver |
| :---- | :---- | :---- |
| **T-2 to T-0 Days** | "Sticky" prices; Narrow ranges | Peak Gamma Pinning 23 |
| **Post-Expiration** | Trend Acceleration | Hedge Unwind / Re-positioning 23 |

## **Strategic Implementation and HENRY Alert Thresholds**

For professional desks and High Earner, Not Rich Yet (HENRY) participants, the value of gamma analytics lies in identifying high-conviction "inflection points" where the market transition from stability to reflexivity.2

### **Leading Indicators of Gamma-Driven Reversals**

1. **DEX Transition Breaches:** The Delta Exposure transition zone marks the point where call or put speculators take control.24 A clean break of the transition zone toward a Max GEX level is a high-conviction signal for a "magnet move".7  
2. **HIRO Volume Spikes:** Using tools like SpotGamma's HIRO (Hedging Impact Real-Time Options), traders monitor real-time 0DTE buy/sell pressure.30 A spike in "Directionalized Volume Gamma" often precedes a price move as dealers adjust hedges in real-time.30  
3. **GEX Ratio Extremes:** The GEX Ratio (Call Gamma / Put Gamma) provides a normalized view of positioning.32 A ratio below 0.3 indicates extreme fragility and a high risk of a "Short Gamma" collapse.36

### **Recommended Alert Thresholds for Professional Trading**

| Metric | Bullish Alert (Stability/Support) | Bearish Alert (Fragility/Momentum) | Actionable Strategy |
| :---- | :---- | :---- | :---- |
| **GEX Ratio** | \> 0.60 | \< 0.35 | Fade extremes in high GEX; follow breakouts in low GEX 19 |
| **Spot vs. VT** | Spot \> VT (Stable) | Spot \< VT (Chaos) | Sell premium above VT; Buy protection below VT 25 |
| **Put Wall Proximity** | within 0.2% | Breach of level | Look for reversal candles (Pin Bars/Hammers) 19 |
| **IV Percentile** | \< 20% (Complacency) | \> 80% (Panic) | Buy "Cheaplies" (Long VEX) during panic 16 |

### **The Speed of Gamma Flips**

In the current 0DTE-dominated environment, the "Gamma Landscape" can flip from positive to negative in minutes.7 This occurs most frequently during the final hour of trading (3:00 \- 4:00 PM ET) or immediately following economic releases like CPI or NFP.4 On August 15, 2023, for example, dealer gamma was noted to shift significantly intraday as price breached short gamma zones, triggering rapid selling pressure.2 Traders should monitor "Net GEX relative to 90-day average" to identify when intraday fluctuations are becoming systemically meaningful.32

## **Historical Ranges and Current Market Readings (February 2026\)**

The current market context in early February 2026 reflects an environment of extreme complacency and high structural concentration.6

| Level / Metric | Reading as of Feb 3, 2026 | Historical Context / Percentile |
| :---- | :---- | :---- |
| **SPX Spot Price** | 6,976.69 41 | Near all-time highs |
| **Max GEX Strike** | 7,000 40 | Primary "Gamma Magnet" and Resistance |
| **Put Wall** | 6,920 40 | Major structural support floor |
| **IV Percentile** | 37% 39 | Mid-to-low range; stable regime |
| **IV Rank** | 7.94% 39 | Extreme complacency; "coiled" for vol |
| **Put-Call Ratio (OI)** | 1.61 42 | Heavy hedging presence (Institutional) |

The current net gamma exposure for SPX is approximately $62 billion per 1% price change based on open interest.37 This is a high positive reading, suggesting that the "Dealer Bid" is currently active and the market is in a "Positive Gamma" regime.36 However, the extremely low IV Rank (7.94%) suggests that market participants are not pricing in any immediate downside risk.39

### **The JPM Collar and Quarterly Magnetism**

For the current quarter (Q1 2026), institutional desks are closely monitoring the J.P. Morgan Equity Premium Income collar, which consists of a sold 7,155 call and a bought 6,475/5,470 put spread expiring March 31\.6 Historically, these collars act as "Gamma Magnets".22 In September 2024, the SPX gravitated toward the JPM collar strike with high precision; a similar pattern is expected as the index nears the 7,000 \- 7,155 zone in early 2026\.22

## **Conclusions and Risk Management Implications**

The reflexive nature of modern markets dictates that the "map" (the options chain) often creates the "territory" (the price action).1 Net GEX, Vanna, and Charm are the fundamental components of this map.9

For the professional participant, the following principles are paramount:

1. **Regime Identification:** One must first determine if the market is above or below the Volatility Trigger and the Gamma Flip.2 Strategies that work in high-positive GEX (e.g., selling straddles/condors) are catastrophic in high-negative GEX.7  
2. **Structural Confluence:** Technical support and resistance are most effective when they align with the Put Wall, Call Wall, or a major OTM Open Interest cluster.2 A "Pin" at 7,000 is not a random occurrence but the result of billions in mechanical hedging.22  
3. **The Temporal Dimension:** Intraday behavior is governed by the 0DTE lifecycle.5 The "Morning Chop" and "Afternoon Unwind" are structural realities of an options-dominated market.5  
4. **Vanna and Charm as Alpha Drivers:** Anticipating the "Charm Drift" during range-bound weeks or the "Vanna Rally" following a volatility crush provides a quantitative edge over participants relying solely on fundamental data.4

As we navigate the high-valuation, low-volatility environment of 2026, the reliance on structural stability provided by 0DTE sellers creates a "fragile equilibrium".6 While current readings suggest a robust "Dealer Bid," the proximity of the Volatility Trigger and the extreme complacency of IV Rank demand a disciplined approach to risk.25 The "tail" of the options market is currently wagging the "dog" of the equity market with more force than ever before; understanding the mechanics of that motion is the only way to avoid being caught in its reflexive snap.

#### **Works cited**

1. SPX Net Gex: Market Makers & Gamma Guide \- MenthorQ, accessed February 3, 2026, [https://menthorq.com/guide/spx-net-gex-market-makers-gamma/](https://menthorq.com/guide/spx-net-gex-market-makers-gamma/)  
2. SpotGamma Levels Reveal Dealer Positioning \- LuxAlgo, accessed February 3, 2026, [https://www.luxalgo.com/blog/spotgamma-levels-reveal-dealer-positioning/](https://www.luxalgo.com/blog/spotgamma-levels-reveal-dealer-positioning/)  
3. What is Gamma Exposure (GEX)? | Quant Data Help Center, accessed February 3, 2026, [https://help.quantdata.us/en/articles/7852449-what-is-gamma-exposure-gex](https://help.quantdata.us/en/articles/7852449-what-is-gamma-exposure-gex)  
4. Dealer Hedging Mechanics Guide \- MenthorQ, accessed February 3, 2026, [https://menthorq.com/guide/dealer-hedging-mechanics/](https://menthorq.com/guide/dealer-hedging-mechanics/)  
5. Volatility Insights: Much Ado About 0DTEs \- Evaluating the Market ..., accessed February 3, 2026, [https://www.cboe.com/insights/posts/volatility-insights-evaluating-the-market-impact-of-spx-0-dte-options/](https://www.cboe.com/insights/posts/volatility-insights-evaluating-the-market-impact-of-spx-0-dte-options/)  
6. Record 0DTE volume reshapes the S\&P 500 | SpotGamma Weekly, accessed February 3, 2026, [https://spotgamma.com/record-0dte-volume-reshapes-the-sp-500/](https://spotgamma.com/record-0dte-volume-reshapes-the-sp-500/)  
7. All About 0DTE Options Guide \- MenthorQ, accessed February 3, 2026, [https://menthorq.com/guide/all-about-0dte-options/](https://menthorq.com/guide/all-about-0dte-options/)  
8. Options Vanna & Charm | SpotGamma™, accessed February 3, 2026, [https://spotgamma.com/options-vanna-charm/](https://spotgamma.com/options-vanna-charm/)  
9. So You've Heard About Gamma Exposure (GEX). But What About Vanna and Charm Exposures? | by Chris Frewin \- Medium, accessed February 3, 2026, [https://medium.com/option-screener/so-youve-heard-about-gamma-exposure-gex-but-what-about-vanna-and-charm-exposures-47ed9109d26a](https://medium.com/option-screener/so-youve-heard-about-gamma-exposure-gex-but-what-about-vanna-and-charm-exposures-47ed9109d26a)  
10. Introducing VannaCharm: Dealer Gamma, Vanna, and Charm Exposure Analysis \- Medium, accessed February 3, 2026, [https://medium.com/option-screener/introducing-vannacharm-dealer-gamma-vanna-and-charm-exposure-analysis-f2f703d2de59](https://medium.com/option-screener/introducing-vannacharm-dealer-gamma-vanna-and-charm-exposure-analysis-f2f703d2de59)  
11. Gamma Exposure: Understanding Support, Resistance, and Price Reversal \- Reddit, accessed February 3, 2026, [https://www.reddit.com/r/options/comments/1hzx1m1/gamma\_exposure\_understanding\_support\_resistance/](https://www.reddit.com/r/options/comments/1hzx1m1/gamma_exposure_understanding_support_resistance/)  
12. How the Options Market Dictates Intraday Futures Moves (Even If You Don't Trade Options), accessed February 3, 2026, [https://bookmap.com/blog/how-the-options-market-dictates-intraday-futures-moves-even-if-you-dont-trade-options](https://bookmap.com/blog/how-the-options-market-dictates-intraday-futures-moves-even-if-you-dont-trade-options)  
13. Option Gamma Explained: The Greeks for Beginners | TradingBlock, accessed February 3, 2026, [https://www.tradingblock.com/blog/option-gamma](https://www.tradingblock.com/blog/option-gamma)  
14. Gamma Flip – SpotGamma Support Center, accessed February 3, 2026, [https://support.spotgamma.com/hc/en-us/articles/15413261162387-Gamma-Flip](https://support.spotgamma.com/hc/en-us/articles/15413261162387-Gamma-Flip)  
15. Introducing floe: Static and Real-time Calculation of ... \- GitHub Pages, accessed February 3, 2026, [https://fullstackcraft.github.io/floe/whitepaper.pdf](https://fullstackcraft.github.io/floe/whitepaper.pdf)  
16. SPYI Gamma Exposure (GEX) for Neos S\&P 500 Highome ETF \- Barchart.com, accessed February 3, 2026, [https://www.barchart.com/etfs-funds/quotes/SPYI/gamma-exposure](https://www.barchart.com/etfs-funds/quotes/SPYI/gamma-exposure)  
17. 0DTE Gamma Levels and Skew Guide \- MenthorQ, accessed February 3, 2026, [https://menthorq.com/guide/0dte-gamma-levels/](https://menthorq.com/guide/0dte-gamma-levels/)  
18. volatility trigger Archives | SpotGamma™, accessed February 3, 2026, [https://spotgamma.com/tag/volatility-trigger/](https://spotgamma.com/tag/volatility-trigger/)  
19. Gamma — Indicators and Strategies \- TradingView, accessed February 3, 2026, [https://www.tradingview.com/scripts/gamma/](https://www.tradingview.com/scripts/gamma/)  
20. Gamma and Vanna for 0 DTE Trading : r/options \- Reddit, accessed February 3, 2026, [https://www.reddit.com/r/options/comments/1lwwjk5/gamma\_and\_vanna\_for\_0\_dte\_trading/](https://www.reddit.com/r/options/comments/1lwwjk5/gamma_and_vanna_for_0_dte_trading/)  
21. Charm, Decay, and Flow Guide \- MenthorQ, accessed February 3, 2026, [https://menthorq.com/guide/charm-decay-and-flow/](https://menthorq.com/guide/charm-decay-and-flow/)  
22. How Institutional Traders Exploit Gamma Explosion at Options Expiration \- Navnoor Bawa, accessed February 3, 2026, [https://navnoorbawa.substack.com/p/how-institutional-traders-exploit](https://navnoorbawa.substack.com/p/how-institutional-traders-exploit)  
23. Option Matrix: Opex Guide \- MenthorQ, accessed February 3, 2026, [https://menthorq.com/guide/option-matrix-opex-guide/](https://menthorq.com/guide/option-matrix-opex-guide/)  
24. Trading SPX 0DTE | GammaEdge's Proven Framework, accessed February 3, 2026, [https://www.gammaedge.us/trading-spx-0dte-key-levels/](https://www.gammaedge.us/trading-spx-0dte-key-levels/)  
25. Volatility Trigger™ – SpotGamma Support Center, accessed February 3, 2026, [https://support.spotgamma.com/hc/en-us/articles/15297954935699-Volatility-Trigger](https://support.spotgamma.com/hc/en-us/articles/15297954935699-Volatility-Trigger)  
26. SpotGamma SPX Key Levels Statistics, accessed February 3, 2026, [https://support.spotgamma.com/hc/en-us/articles/31209900542867-SpotGamma-SPX-Key-Levels-Statistics](https://support.spotgamma.com/hc/en-us/articles/31209900542867-SpotGamma-SPX-Key-Levels-Statistics)  
27. Option Expiration Week (OPEX) Guide \- MenthorQ, accessed February 3, 2026, [https://menthorq.com/guide/option-expiration-week/](https://menthorq.com/guide/option-expiration-week/)  
28. Volatility Trigger: The Gamma Flip Point. Explanation \+ Stats | SpotGamma \- YouTube, accessed February 3, 2026, [https://www.youtube.com/watch?v=D9F6Pip0Rl8](https://www.youtube.com/watch?v=D9F6Pip0Rl8)  
29. Understanding Zero DTE Options Guide \- MenthorQ, accessed February 3, 2026, [https://menthorq.com/guide/understanding-zero-dte-options/](https://menthorq.com/guide/understanding-zero-dte-options/)  
30. All About 0DTE Options | SpotGamma™, accessed February 3, 2026, [https://spotgamma.com/0dte/](https://spotgamma.com/0dte/)  
31. 0DTE Trading & Gamma Exposure \- Interview w/ Mat Cashman from OIC, accessed February 3, 2026, [https://optionalpha.com/podcast/0dte-trading-gamma-exposure-interview-w-mat-cashman-from-oic](https://optionalpha.com/podcast/0dte-trading-gamma-exposure-interview-w-mat-cashman-from-oic)  
32. Realtime GEX : r/options \- Reddit, accessed February 3, 2026, [https://www.reddit.com/r/options/comments/1ia80j8/realtime\_gex/](https://www.reddit.com/r/options/comments/1ia80j8/realtime_gex/)  
33. Gamma Decay in Options Trading & How Market Makers Manage Risk \- Cheddar Flow, accessed February 3, 2026, [https://www.cheddarflow.com/blog/gamma-decay-in-options-trading-how-market-makers-manage-risk/](https://www.cheddarflow.com/blog/gamma-decay-in-options-trading-how-market-makers-manage-risk/)  
34. Pinning in the S\&P 500 futures, accessed February 3, 2026, [https://d-nb.info/1112655492/34](https://d-nb.info/1112655492/34)  
35. Gamma Levels for FX Traders Guide \- MenthorQ, accessed February 3, 2026, [https://menthorq.com/guide/gamma-levels-for-fx-traders/](https://menthorq.com/guide/gamma-levels-for-fx-traders/)  
36. GEXStream \- Real-Time Gamma Exposure Analytics for Options Traders, accessed February 3, 2026, [https://gexstream.com/](https://gexstream.com/)  
37. SPX Options Greek Exposure (GEX, DEX, Vanna, Charm) \- Unusual Whales, accessed February 3, 2026, [https://unusualwhales.com/stock/SPX/greek-exposure](https://unusualwhales.com/stock/SPX/greek-exposure)  
38. Gamma Zone Reversal Strategy – Real Data Based Intraday Setup\! \- TradingView, accessed February 3, 2026, [https://in.tradingview.com/chart/NIFTY/kvfmU5GD-Gamma-Zone-Reversal-Strategy-Real-Data-Based-Intraday-Setup/](https://in.tradingview.com/chart/NIFTY/kvfmU5GD-Gamma-Zone-Reversal-Strategy-Real-Data-Based-Intraday-Setup/)  
39. S\&P 500 Index Gamma Exposure (GEX) \- Barchart.com, accessed February 3, 2026, [https://www.barchart.com/stocks/quotes/%24SPX/gamma-exposure](https://www.barchart.com/stocks/quotes/%24SPX/gamma-exposure)  
40. Options Market Summary \- Flow, GEX, Greeks, Unusual Contracts \- Tradytics, accessed February 3, 2026, [https://tradytics.com/options-market](https://tradytics.com/options-market)  
41. $SPX: S\&P 500 Index Gamma Exposure History \- OptionCharts.io, accessed February 3, 2026, [https://optioncharts.io/options/$SPX/option-history-gex](https://optioncharts.io/options/$SPX/option-history-gex)  
42. $SPX Open Interest \- S\&P 500 Index \- OptionCharts, accessed February 3, 2026, [https://optioncharts.io/options/$SPX/open-interest](https://optioncharts.io/options/$SPX/open-interest)

[image1]: <data:image/png;base64,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>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAAZCAYAAADqrKTxAAAA5klEQVR4Xu3Ssa4BQRQG4KMQEgkiQqhEJxENpagkNwqN3De4hXgBGtFrFDqJN1BQiULiFTyCWqO6Svxn55+1u7ptROJPvmJn5szunFmRj0wS/mgObUhQy7POTQN2UKOYmOIT9e1CmxwcoBoYj8OKmoG5cEUdMZ9QCIxHYEzZwJxTdIMZlEgLNLYR9tlNCvZw97jCQMzilwJNqCJNVEzbp3SGf6iTG+2ayngHGe3kBbrkZkS+nZgyHKFCTvQO1tSzg/I8w1BMN31nClWkr9/QFibwCwtairkfX/SPTpPuVIQfyNM3788D2yEs5TJxUlIAAAAASUVORK5CYII=>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAYCAYAAADOMhxqAAAAbklEQVR4XmNgGJRAAIglCWBhKGYEabAC4nlQ/A+IFwJxBBR3AfEVID4AxTwgDSBgDMVfgdgXJggFIEUwA8VhglTVAAIJUCwDEyCkQRqKhWAChDRggFENaHIYIB2Ib0DxfyB+CsT9UAxKmKOA9gAA5eYi8o3H/0IAAAAASUVORK5CYII=>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABUAAAAZCAYAAADe1WXtAAABIUlEQVR4Xu3TvUtCURzG8V/0QuDQGxSBS9iQNATi4taoQ4trSwQtBRK1NQQRTm2N7Q7loji4CEn/TFOjcz4P5zlx9JiWcKnBL3wQvfeee7znHrN/VAou5B7yg4ena6pBd+UOrmEbcrIKl8H3LXiFfYmag3N4kg3YgWaAszyFoizAC5QkindqwIr4yvAow/EftWFTohIZ9Apq5h4D+Y7MDUw+f+MHSAe/R3HQHpyJn+0SLArj54mswx4cSFQW3uEz8GbxTPhGhOd8mLuWohIZlPGV4TOkurmLRi3QxDISrrivCs8wLz/uVrhzhrsxN/CvWoOuFAaOuB3Vsm+237gSGZQrxheeOlCBY+FOGbmfJ8WZcsWJLzVndSjLX2fNmvV39QEiNT7fbFpYaAAAAABJRU5ErkJggg==>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACIAAAAXCAYAAABu8J3cAAABcklEQVR4Xu3VsStFURwH8N8rirwyGLB5pVcmSkLIovSKN5gMNoOMJrLbxWogIWKTAXGzKPkPZDAb/AXK99v9Hvd475zC9Hrdb32W37vn3N8997xzzfLk+V16ZB9O4BrmpJBdFkxZLuEQrmBE/LTJAhxA8efPZi1wLEuqdcGdjKsWSifcyJRq/fAoJdUqsCMXkFigkQF4kWGvzq6Jg2OZsWxsr2q8QSIrqvlZt0ZvZB7exE3GbMktdHh1P25SchPzVZ/Lnmp+oo1w84Qa4YDoIGXT6hth3GpSbaJzcvn+2whfWyLN00hsj3DZ3dLXDVJCe6QAR/KnRnjwuEYGvbp7Ik7IyUPh/nqVbtV4g0T4ILWJNsJD6UH4d2TaLT0haVG1MtzLhGoleBYeAwwbepLQYRhthJmVBEZhA7alVdeMwbtUVWNW5czSFd2FNXErOQSn8gGflp7ay/KdhmnEhcs1CX2WThLbG6Hw+zRt2V7Jk6c58wWpKYDJku02SQAAAABJRU5ErkJggg==>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAXCAYAAADUUxW8AAAAYklEQVR4XmNgGAXIIAmK9dEliAEZUGyMLkEMGOSaWYFYHIgl0XAFFLtjkRMGYkaQZm4g9gbiEDQ8G4rLschZUUUzLkCUn3EB2muWBeJ+IJ6Fho9B8XoscllAzEyx5lFALwAAb/gkPLJM5oUAAAAASUVORK5CYII=>

[image7]: <data:image/png;base64,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>

[image8]: <data:image/png;base64,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>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAZCAYAAADnstS2AAAAa0lEQVR4XmNgGAX0BJJQHADEIWjYH4qFQArlgXgHFM8F4mNQvB6IZwFxLxSDDCNNcRYQC0MxCxD3QLEMSBIfkAbi+VDMgyaHAVyAeA4UEwStQFwOxQQBUYq5oXgXEHtCMUHAC8TMUDwKqAcAmXgX77l6rZ8AAAAASUVORK5CYII=>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAAvCAYAAABexpbOAAAEb0lEQVR4Xu3dSYhcRRgH8JJoVIwajbsHJaBiXHHfFRdUXBDxIKJ4cNegB3EPEQIeEkTBFRcQBRE3yEFEVHBuHryqZw960EMOglf1+6h+068rPUn3zMDMJL8f/JnX33vTM8ePqnpVpQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwcPtFDmqLu3FwZFVbBABgaJ/IM5GrIh9FzolsjWyO3BE5YfbJXcvnb2+L4fDI85Ed7Y2ep9oCAMDeaN/IlshML2dFzo18Gjmw1MZpdalN3KllOh+X+h3j3Br5uS32HB85ui0CAFDdEnlpcH3Z4OcBkSMG15Pa2BZ68vs/aIs92SDe2RYBAPZ0X0eeK3V92MvNvXFyRC0btdSuKcuRs02RayJvRg4ptbnrRsWOLaMjcrmWLZ97ttT/4Z9SR/J25dsy/fo3AIAVK0esvim10crm6aHR2zs5MfJl5Mym3tkQuavUNWrrBrVs2LJRS+t71+nuyC+lNnTddGiO2GUjeFHkjOGjs7ZH1rRFAIA9VTZKOWL1bmRbqQ3cYnitd50vKnQjcrkWrt+wzZThszkdmuvb8n+4fFDPadiWhg0A2KvkaFa3Hi09XOpLBwuRU545apZyevPXyBOlNof59/pTnj+VYVP2e+SSyIuDz9nojWvYvigL/x8BABZFjjTlaFSbbHxy+nKx5AhbLuTPLTVya42FyiZrZnB9SuTHQS1lo9Xf0iOvP4w8Hvk+8nbkgcG9uRq2rAMALAvZ3HwS+a/UpubpyFeRvyPn955bqJyuzEawm7ZcqHZT3PZ7Xy+jU695f22pv5cNY3dvXMOWa+1Ob2oAAEsqpw/zzcl+45LNWjcKtRJdUOp6tWmnNQ8tdQQOAGBZGdew5SjTpKcKLFfXR25ui7uRb7Ce3RYBAJbauIZtnFyDlm96jstbZfrTCAAAmNCkDdt8HbnCAwCw5CZt2PLw9XZkrcsbkZOHjwIAsJgmbdhWqkvnyMX9hwAAlqvc7uKPUrf1+LPUY6GWUp4Lel+pJxDkth1XjN6e2v6RrZFHx+TB3nMAAEzghzK6/9nnZfSEhGnlnmtXt0UAAObvtzJ6BuimUo+Zmq/cluSetggAwPz9G3ml1GnZPIkgp0S7EwlWlTrali8+dNnVNiK5Ye51kRcGn8f9fv+kBAAAJpBTmOeVuubsrzI8wH1NZGOpzVumPecza+2JBvlSQW6Cmy6M3DS43jb4CQDAlI5qPudatu6t1RtKPYy+02/Yslk7puz8xue1kduaWuqaOAAAptSOmq0vwynPvNdNjR5WagPXOSnyWWRHr5bGnYOao3DZyAEAMKVszrZHNpe6tuydyPu9+3kg+5ORLaVu99GXa9OyEXskcu+gdmVk9ewTQzeW+l0AAEwp915bGzmu1APb+9OfnXWl7hk3lw2lNnmnlfod4+QaOQAAlkiOqH0XeS9yf3MPAIBl4rHIq6WuawMAYBnKKdVcD2fqEwAAAAAAAAAAAAAAAAAAAAAAAAAAAADm8j/RSX7pWAuddQAAAABJRU5ErkJggg==>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAYCAYAAAC4CK7hAAABZklEQVR4Xu3VzStEURgG8Fc+y1dho5Ripax8RnY2LCSlKLY2NpayoqyUlYWFlI/Cxs5Gs5Ao+QesrJT8HZ7Hfe503Obeabh3mm7nqd/mnTMf75xz32Pm4+OTh9TJChTgBk6ly1lX85mSB+hWbV2uoUG1qqYJFqEl+kJCjuTCqY3KOww59aol00Y6ZAGWS5i24IymlS0YjhZj0gaPsu3UB+QL5lnohxdhx3fwCieOVS5MMfxO/qhGSUo7PIvbSK98WLABtmHBBxOzaeow44zAofA0xKUH3iSxETc8t2dW2cPDtXRsv3exnHP4lH1ottKJO1p9wvfntxE+PAULtjPL8Lk4gAlJCofMlfACDBNOLTYy7tR/sga3lv0FMwtL0WJCOGyIgygc23PyBJ2qFcOO96LFlMM/adcq23UeL7qEHZiEexlz1hXTauXH4X/Do8KR+pd7qR4GYcaCnYm9VHPTiI+Pj09t5xs4yVBbWsT+3QAAAABJRU5ErkJggg==>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAXCAYAAAD6FjQuAAABMElEQVR4XtXTv0vDQBjG8RO1KtqhUBBBJIJTB11baKmDY0ERcXR1chKXLlLUzU6lQ9uhU8dOHRycHAQHFxfB/0PqJPi85FHuXvoraRPwCx8I9+a4EBJj/lFeQFPlBRS6VWjQ7YRCdwwXFGnL8KAXo6oEl3oxqmI7bAEe1doc7MHJAEeU/rs7QAdQ5rUcIq7gCVr0Dh1oQpU2uMdJNo+qbV3v0Jnx961T3fi/xthiO8yDol5kHl27y07yisW9HtgVqA8favabvH+xqAdWd3SuB3b7JF/UN+TtIdqCCg0rZfyPROj9Tgmah2fouWNTgzUaljzoG22rmVOsh9kdwhdkaRNunDsGJw+apIlbgRfokvyQu84dM+4UPkn+q1Ff4NTJq3ilnJrNvFgPkzK0pAdh+wFN/ztJ2D8RIAAAAABJRU5ErkJggg==>