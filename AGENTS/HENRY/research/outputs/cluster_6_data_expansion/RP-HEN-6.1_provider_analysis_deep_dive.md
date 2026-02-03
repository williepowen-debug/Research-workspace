# **Market Microstructure and the Architecture of Gamma Exposure: A Comprehensive Analysis of Dealer Hedging and the Analytical Ecosystem**

The structural evolution of global equity markets has been characterized by a paradigm shift in which derivatives activity increasingly dictates the price discovery process of underlying assets. Central to this transformation is the phenomenon of Gamma Exposure (GEX), a metric that quantifies the reflexive relationship between options market positioning and the mechanical hedging requirements of financial intermediaries. As market makers and institutional dealers maintain delta-neutral portfolios, their continuous rebalancing activities create predictable liquidity flows that either dampen or exacerbate realized volatility. This report provides an exhaustive examination of the mathematical foundations of gamma exposure, the behavioral dynamics of dealer hedging regimes, and a critical evaluation of the professional and retail data ecosystem providing these insights.

## **1\. Gamma Exposure (GEX) Fundamentals**

### **Theoretical Underpinnings and the Role of the Market Maker**

To understand the Gamma Exposure Index (GEX), one must first delineate the operational mandate of the options market maker. Unlike directional speculators, market makers—often referred to as dealers—provide liquidity by quoting two-sided markets, simultaneously offering to buy and sell options contracts.1 To mitigate the inherent directional risk of these positions, dealers engage in dynamic delta hedging. Delta represents the sensitivity of an option's price to a change in the underlying asset's price; if an option has a delta of 0.50, the dealer who has sold that option is "short" 50 shares of delta for every contract.3 To achieve delta neutrality, the dealer must purchase 50 shares of the underlying stock or an equivalent amount of futures.1

Gamma is the second-order Greek that measures the rate of change of delta relative to the underlying price movement.3 It represents the acceleration of directional exposure. From the dealer's perspective, gamma is the risk that their delta hedge will become obsolete as the market moves.8 The Gamma Exposure Index (GEX) aggregates this sensitivity across the entire universe of open options contracts, providing a dollar-denominated estimate of the hedging requirements triggered by a 1% move in the underlying asset.2

### **Mathematical Framework and Aggregate Calculation**

The calculation of aggregate market GEX is a bottom-up process that requires the summation of gamma contributions from every active strike and expiration. The foundational formula for a single option's gamma exposure, expressed in terms of share impact, is as follows:

![][image1]  
In this LaTeX-formatted expression, ![][image2] represents the unit gamma of the specific option, ![][image3] is the open interest at that strike and expiration, and ![][image4] is the standard contract multiplier.5 To translate this into the standard Gamma Exposure Index—the dollar value of the underlying that must be traded for a 1% move—the formula is expanded:

![][image5]  
Here, ![][image6] denotes the spot price of the underlying asset. The term ![][image7] accounts for the fact that a 1% move in a stock trading at ![][image8] is a ![][image9] move, but a 1% move in a stock trading at ![][image10] is a ![][image11] move. The resulting GEX figure provides a quantifiable measure of potential market impact.4

| Variable | Description | Impact on GEX Magnitude |
| :---- | :---- | :---- |
| **Gamma (![][image2])** | Rate of change of Delta | Higher for ATM options and near-dated expiries |
| **Open Interest (OI)** | Total outstanding contracts | Higher OI leads to larger potential hedging flows |
| **Spot Price (![][image6])** | Current market price | Quadratic impact on dollar-denominated GEX |
| **Contract Multiplier** | Standardized at 100 shares | Constant factor for US equity options |

4

### **Positive vs. Negative GEX: Volatility Regimes**

The aggregate GEX value informs the market of the prevailing volatility regime. A positive GEX value indicates that dealers are "net long gamma," while a negative value indicates they are "net short gamma".2 These two states produce diametrically opposed price behaviors.

In a positive GEX environment, dealers typically hold long call options and short put options that have been sold to them by investors looking for yield or protection.8 When the market rises, the delta of their long calls increases, making them more "long" than intended. To remain neutral, they must sell the underlying asset. Conversely, when the market falls, they must buy it back. This "sell-high, buy-low" mechanic acts as a stabilizing force, compressing realized volatility and creating a mean-reverting environment.3

In a negative GEX environment, the opposite occurs. Dealers are modeled as being net short gamma, often due to a high volume of puts purchased by the public for downside protection.1 As the market declines, the delta of their short puts increases, requiring them to sell more of the underlying to stay neutral. As the market rises, they must buy it back to cover their hedges. This "sell-low, buy-high" cycle creates a pro-cyclical feedback loop that accelerates price moves and expands volatility.5

### **The Gamma Flip and Gamma Neutral Levels**

The "Gamma Flip" or "Zero Gamma" level is the critical price point where the aggregate market gamma transitions from positive to negative.9 This level serves as a structural inflection point. Above the Gamma Flip, the market is historically characterized by lower volatility and price stability. Below the Gamma Flip, the environment shifts toward higher volatility and wider daily trading ranges.9

Professional analysts use the Gamma Flip as a primary risk management threshold. When the spot price approaches the flip level from above, it often encounters significant liquidity as dealers buy the dip.1 However, if the price breaches the flip level, a "volatility trigger" is often activated, where the mechanical selling required by dealers can lead to rapid price cascades.9

### **Impact on Expected Daily Price Ranges**

The distribution of GEX across strike prices allows for the identification of "Call Walls" and "Put Walls," which define the expected daily price range. A Call Wall is the strike with the largest net positive gamma, acting as a formidable resistance level where dealer selling slows upward momentum.18 A Put Wall is the strike with the largest net negative gamma, serving as a support level where dealer buying typically stabilizes declines.1

Analysis of the S\&P 500 suggests that the index remains within its Call and Put walls in a significant majority of trading sessions.22 When GEX is high and positive, the "expected move" or daily range is compressed, as dealer flows provide a constant buffer against directional expansion. When GEX is negative or near zero, the "implied order book" is thin, allowing for much larger realized moves for a given amount of trade volume.23

## **2\. Data Providers and Sources**

The analytical landscape for gamma exposure is divided between retail-facing dashboards and institutional-grade data terminals. Each provider utilizes varying methodologies, from "naive" models based on open interest to complex trade-classification algorithms.

### **SpotGamma: Metrics, Cost, and Architecture**

SpotGamma has established itself as a premier provider of derivatives-driven market levels for active traders. Their methodology focuses on the "hedging impact" of options flows rather than just static open interest.9

* **Key Metrics:** SpotGamma provides the "Gamma Flip," "Volatility Trigger," and "Call/Put Walls" for major indices and over 3,500 individual stocks.9 Their "HIRO" (Hedging Impact of Real-Time Options) indicator is a proprietary tool that tracks how dealer hedging is shifting intraday by analyzing the options tape.25  
* **Cost and Tiers:** As of 2025-2026, pricing is tiered based on the frequency of analysis. The "Essential" tier is priced at approximately $99/month, while the "Alpha" tier, which includes the HIRO indicator and the full volatility dashboard, is $299/month.26 Annual subscriptions provide a 25% discount, bringing the Alpha tier to $2,691/year.25  
* **Data Format:** Data is delivered via a web-based dashboard, with integrations available for platforms like TradingView and ThinkOrSwim.18 Professional users can access intraday file delivery and API support.21

### **SqueezeMetrics: The DIX/GEX Ecosystem**

SqueezeMetrics focuses on the intersection of dark pool equity prints and options gamma. Their thesis is that institutional sentiment in opaque dark pools often leads the hedging activity seen in the public options market.16

* **The DIX (Dark Index):** This is a dollar-weighted measure of institutional buying in dark pools. A high DIX (above 45%) suggests institutional accumulation, which often leads to positive returns in the subsequent weeks.16  
* **GEX Offering:** SqueezeMetrics provides a dollar-denominated GEX metric for the S\&P 500\. Their model is known for its "volatility distribution" charts, which demonstrate the exponential increase in realized volatility as GEX trends below zero.5  
* **Methodology:** They utilize a constant-volatility Black-Scholes model to derive GEX, ensuring that the metric is comparable across different time periods and assets.5

### **GammaLab: Index-Level Flow and CTA Tracking**

GammaLab is a specialized provider targeting traders who focus on the relationship between dealer flows and systematic trend-followers.31

* **Capabilities:** Their platform offers index-level gamma data, which is critical for understanding the "dealer tailwind" or "headwind" in the SPX and NDX.31  
* **CTA Tracker:** A unique feature of GammaLab is their tracker for Commodity Trading Advisors (CTAs). This helps users understand how trend-following funds are positioned and where they might be forced to trigger large-scale liquidations or additions to their equity exposure.31  
* **Cost:** Positioned as an affordable alternative, GammaLab's services are priced at approximately $14.99/month.31

### **Unusual Whales: Options Flow Quality and GEX**

Unusual Whales has democratized options flow data, providing real-time tracking of institutional "whale" activity across all US exchanges.33

* **Options Flow Quality:** They track over 2 million options daily with real-time streaming.33 While their GEX visualizations utilize a "naive" model—assuming customers are long puts and short calls—the sheer volume of their data makes it highly effective for identifying unusual positioning at specific strikes.11  
* **GEX Tools:** Their "Gamma View" provides daily GEX, GEX by strike, and GEX by expiry. This allows traders to identify where gamma is most concentrated, which is particularly useful for 0DTE (Zero Days to Expiration) strategies.4  
* **Cost:** Their "Buffet" plan starts at $50/month, providing institutional-grade flow and dark pool data to retail traders at a fraction of the cost of legacy competitors.33

### **CBOE: Raw Data and Indices**

As the primary exchange for US index options, CBOE Global Markets is the ultimate source of raw data for gamma calculations.37

* **Raw Data Availability:** CBOE offers the "Open-Close Volume Summary," a proprietary dataset that breaks down volume by participant type (Market Maker, Customer, Broker-Dealer).38 This is the most accurate data for modeling GEX because it reveals if a trade was an "opening" or "closing" transaction.36  
* **Public Indices:** CBOE publishes the "Realized Volatility Index" (Ticker: GAMMA), which tracks the performance of a delta-hedged portfolio of short-dated SPX straddles.39  
* **LiveVol Pro:** For $380/month, CBOE provides a professional-grade analytical platform with real-time Greeks, volatility skew analysis, and Excel integration.40

### **Bloomberg and Refinitiv (LSEG): Professional Terminals**

In the institutional sphere, Bloomberg and Refinitiv (now LSEG Data & Analytics) remain the gold standards for cross-asset risk and volatility modeling.41

* **Bloomberg Terminal:** Professional users utilize the OVME (Option Pricer Equity/IR) function to structure and price complex derivatives strategies while monitoring real-time gamma and vanna exposure.43 The VCA (Volatility and Correlation Analysis) tool allows for in-depth analysis of skew and term structure across global indices.43  
* **Refinitiv (LSEG Workspace):** LSEG provides "Instrument Pricing Analytics," which delivers intraday Greeks and implied volatility for listed and OTC options.45 Their "StarMine" predictive analytics and "MarketPsych" sentiment data are often used alongside gamma metrics to contextualize dealer flows.46  
* **Cost:** These platforms are priced for institutions, with Bloomberg costing approximately $25,000/year and Refinitiv costing around $15,000/year per user.33

### **Provider Ranking and Synthesis**

The following table ranks providers based on four critical dimensions for professional practitioners.

| Provider | Accuracy | Timeliness | Cost Efficiency | Accessibility | Best For |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **CBOE (Open-Close)** | Tier 1 (Raw) | Intraday (1-10m) | Tier 3 (High) | Restricted | Quant Developers |
| **SpotGamma** | Tier 1 (Advanced) | Real-time (HIRO) | Tier 2 (Moderate) | Public | Day/Swing Traders |
| **Bloomberg** | Tier 1 (Pro) | Real-time | Tier 4 (Very High) | Pro Terminal | Portfolio Managers |
| **SqueezeMetrics** | Tier 2 (Model) | End-of-Day | Tier 1 (Low) | Public | Macro Analysts |
| **Unusual Whales** | Tier 3 (Naive) | Real-time | Tier 1 (Low) | Public | Retail Momentum |
| **GammaLab** | Tier 3 (Index) | Intraday | Tier 1 (Low) | Public | Systematic/CTA |

5

## **3\. Advanced Market Dynamics: The Impact of 0DTE and Convexity**

The proliferation of options with zero days to expiration (0DTE) has fundamentally altered the gamma landscape. Because gamma is inversely proportional to the time remaining until expiration for at-the-money options, 0DTE contracts possess "massive" gamma.6 This makes the market extremely sensitive to intraday price shifts, as dealers must re-hedge their positions minute-by-minute.24

### **The Convexity Effect and Vanna/Charm Flows**

Traders also monitor second-order sensitivities such as Vanna and Charm to predict dealer behavior. Vanna measures the change in delta relative to implied volatility (IV). In a typical market sell-off, IV increases, which increases the delta of OTM puts. If dealers are short those puts, they must sell more of the underlying to hedge, even if the price doesn't move further, creating a "vanna-fueled" cascade.1

Charm, or "delta decay," measures the change in delta as time passes. As expiration approaches, the delta of out-of-the-money options decays toward zero. For dealers who are long these options, their "long delta" vanishes, requiring them to buy the underlying asset to remain neutral. This often leads to "market drift" toward the end of the trading day or near monthly options expiration (OpEx).6

### **The Role of Skew and Term Structure**

The reliability of GEX metrics is also influenced by the "volatility skew"—the fact that out-of-the-money puts typically trade at higher implied volatilities than out-of-the-money calls due to hedging demand.43 Advanced models, such as those found on Bloomberg or SpotGamma Alpha, incorporate these skew variations into their Black-Scholes calculations to provide a more accurate picture of "synthetic" open interest and the true location of the Gamma Flip.24

## **4\. Implementation and Strategic Conclusion**

The synthesis of gamma exposure data into a trading framework requires an understanding of structural liquidity.

### **Tactical Application of Gamma Levels**

1. **Regime Identification:** Use the aggregate GEX and the Gamma Flip level to determine the day's volatility regime. Above the flip, focus on theta-positive strategies like credit spreads. Below the flip, prioritize long-volatility or momentum strategies.8  
2. **Structural Support/Resistance:** Treat the Call Wall and Put Wall as "magnetic" levels. Price often stalls or reverses as it approaches these concentrations due to the overwhelming volume of dealer hedging.10  
3. **The 0DTE Pulse:** Monitor intraday gamma shifts via real-time tools like HIRO or the Unusual Whales flow feed. Large block trades in 0DTE options can shift the Gamma Flip level intraday, turning a calm market into a volatile one in minutes.24  
4. **Confirmation via Flow:** Always cross-reference GEX levels with actual options flow. A Call Wall is a resistance level, but if institutional buyers are aggressively "sweeping" strikes above the wall, it may indicate a "gamma squeeze" where dealer buying will actually fuel a breakout.14

### **Final Assessment**

Gamma Exposure (GEX) has transitioned from a niche academic concept to an essential pillar of modern market analysis. By quantifying the mechanical requirements of market makers, GEX provides a structural map of market liquidity and volatility. While no single metric can guarantee market direction, the awareness of dealer hedging flows allows professional and retail participants alike to navigate the complexities of a derivatives-dominated financial system with greater precision and risk control. As markets continue to evolve toward shorter-dated expiries and higher leverage, the analytical ecosystem supporting gamma exposure will remain indispensable for the identification of structural support, the anticipation of volatility regimes, and the execution of sophisticated options strategies.

#### **Works cited**

1. What is Gamma Exposure (GEX)? | Quant Data Help Center, accessed February 3, 2026, [https://help.quantdata.us/en/articles/7852449-what-is-gamma-exposure-gex](https://help.quantdata.us/en/articles/7852449-what-is-gamma-exposure-gex)  
2. Cboe Global Markets Inc. Option Gamma Exposure (GEX) \- OptionCharts.io, accessed February 3, 2026, [https://optioncharts.io/options/CBOE/gamma-exposure](https://optioncharts.io/options/CBOE/gamma-exposure)  
3. Gamma Exposure: Understanding Support, Resistance, and Price Reversal \- Reddit, accessed February 3, 2026, [https://www.reddit.com/r/options/comments/1hzx1m1/gamma\_exposure\_understanding\_support\_resistance/](https://www.reddit.com/r/options/comments/1hzx1m1/gamma_exposure_understanding_support_resistance/)  
4. What is Gamma Exposure (GEX)? \- Unusual Whales, accessed February 3, 2026, [https://unusualwhales.com/faq/what-is-gamma-exposure-gex](https://unusualwhales.com/faq/what-is-gamma-exposure-gex)  
5. Disclaimer The information contained in these documents is ... \- sqzme, accessed February 3, 2026, [https://squeezemetrics.com/monitor/download/pdf/white\_paper.pdf](https://squeezemetrics.com/monitor/download/pdf/white_paper.pdf)  
6. Gamma Explained: Why It Matters & How to Trade It \- Unusual Whales, accessed February 3, 2026, [https://unusualwhales.com/news/what-is-gamma-a-primer](https://unusualwhales.com/news/what-is-gamma-a-primer)  
7. Introduction to Gamma Exposure(GEX) \- TradingFlow, accessed February 3, 2026, [https://www.tradingflow.com/blog/introduction-to-gamma-exposure-gex](https://www.tradingflow.com/blog/introduction-to-gamma-exposure-gex)  
8. S\&P 500 Index Gamma Exposure (GEX) \- Barchart.com, accessed February 3, 2026, [https://www.barchart.com/stocks/quotes/%24SPX/gamma-exposure](https://www.barchart.com/stocks/quotes/%24SPX/gamma-exposure)  
9. Gamma Flip – SpotGamma Support Center, accessed February 3, 2026, [https://support.spotgamma.com/hc/en-us/articles/15413261162387-Gamma-Flip](https://support.spotgamma.com/hc/en-us/articles/15413261162387-Gamma-Flip)  
10. Gamma Exposure Explained: How to See the Hidden Price Points Where Market Makers Move Stocks \- Barchart.com, accessed February 3, 2026, [https://www.barchart.com/story/news/35756961/gamma-exposure-explained-how-to-see-the-hidden-price-points-where-market-makers-move-stocks](https://www.barchart.com/story/news/35756961/gamma-exposure-explained-how-to-see-the-hidden-price-points-where-market-makers-move-stocks)  
11. What is Gamma Exposure (GEX)? \- Unusual Whales, accessed February 3, 2026, [https://unusualwhales.com/information/what-is-gamma-exposure-gex](https://unusualwhales.com/information/what-is-gamma-exposure-gex)  
12. How to Calculate Gamma Exposure (GEX) and Zero Gamma Level, accessed February 3, 2026, [https://perfiliev.com/blog/how-to-calculate-gamma-exposure-and-zero-gamma-level/](https://perfiliev.com/blog/how-to-calculate-gamma-exposure-and-zero-gamma-level/)  
13. GEXStream \- Real-Time Gamma Exposure Analytics for Options Traders, accessed February 3, 2026, [https://gexstream.com/](https://gexstream.com/)  
14. What Is Gamma Exposure? An In-Depth Analysis for Traders \- Cheddar Flow, accessed February 3, 2026, [https://www.cheddarflow.com/blog/what-is-gamma-exposure-an-in-depth-analysis-for-traders/](https://www.cheddarflow.com/blog/what-is-gamma-exposure-an-in-depth-analysis-for-traders/)  
15. Gamma Flip: What It Means & How To Trade It \- Unusual Whales, accessed February 3, 2026, [https://unusualwhales.com/news/gamma-flip-a-primer](https://unusualwhales.com/news/gamma-flip-a-primer)  
16. When the big players make their move: DIX and GEX \- 11Onze, accessed February 3, 2026, [https://www.11onze.cat/en/magazine/dix-gex/](https://www.11onze.cat/en/magazine/dix-gex/)  
17. Understanding Gamma Exposure Mechanics Guide \- MenthorQ, accessed February 3, 2026, [https://menthorq.com/guide/understanding-gamma-exposure-mechanics/](https://menthorq.com/guide/understanding-gamma-exposure-mechanics/)  
18. Understanding the Gamma Chart and Key Levels | Wall St. Jesus & Sang Lucci Help Center, accessed February 3, 2026, [https://help.wallstjesus.com/en/articles/9708418-understanding-the-gamma-chart-and-key-levels](https://help.wallstjesus.com/en/articles/9708418-understanding-the-gamma-chart-and-key-levels)  
19. GEX Profile \[Lite\] Real Auto-Updated Gamma Exposure Levels \- TradingView, accessed February 3, 2026, [https://www.tradingview.com/script/2iIjQYTo-GEX-Profile-Lite-Real-Auto-Updated-Gamma-Exposure-Levels/](https://www.tradingview.com/script/2iIjQYTo-GEX-Profile-Lite-Real-Auto-Updated-Gamma-Exposure-Levels/)  
20. Learn How Gamma Exposure Reveals Volatility 'Fault Lines' for Your Favorite Stocks, and How to Trade It With Options \- Barchart.com, accessed February 3, 2026, [https://www.barchart.com/story/news/35528101/learn-how-gamma-exposure-reveals-volatility-fault-lines-for-your-favorite-stocks-and-how-to-trade-it-with-options](https://www.barchart.com/story/news/35528101/learn-how-gamma-exposure-reveals-volatility-fault-lines-for-your-favorite-stocks-and-how-to-trade-it-with-options)  
21. What is included in each SpotGamma subscription level?, accessed February 3, 2026, [https://support.spotgamma.com/hc/en-us/articles/360062942133-What-is-included-in-each-SpotGamma-subscription-level](https://support.spotgamma.com/hc/en-us/articles/360062942133-What-is-included-in-each-SpotGamma-subscription-level)  
22. Call Wall \- SpotGamma Support Center, accessed February 3, 2026, [https://support.spotgamma.com/hc/en-us/articles/15297391724179-Call-Wall](https://support.spotgamma.com/hc/en-us/articles/15297391724179-Call-Wall)  
23. SqueezeMetrics, accessed February 3, 2026, [https://squeezemetrics.com/](https://squeezemetrics.com/)  
24. SPX Net Gex: Market Makers & Gamma Guide \- MenthorQ, accessed February 3, 2026, [https://menthorq.com/guide/spx-net-gex-market-makers-gamma/](https://menthorq.com/guide/spx-net-gex-market-makers-gamma/)  
25. SpotGamma Review 2026: Pricing, Pros, Cons & Alternatives \- Bullish Bears, accessed February 3, 2026, [https://bullishbears.com/spotgamma-review/](https://bullishbears.com/spotgamma-review/)  
26. Plans & Pricing | SpotGamma™, accessed February 3, 2026, [https://spotgamma.com/subscribe-to-spotgamma/](https://spotgamma.com/subscribe-to-spotgamma/)  
27. What is the cost of a SpotGamma Subscription?, accessed February 3, 2026, [https://support.spotgamma.com/hc/en-us/articles/1500002666102-What-is-the-cost-of-a-SpotGamma-Subscription](https://support.spotgamma.com/hc/en-us/articles/1500002666102-What-is-the-cost-of-a-SpotGamma-Subscription)  
28. How do I change my subscription level? \- SpotGamma Support Center, accessed February 3, 2026, [https://support.spotgamma.com/hc/en-us/articles/1500002502721-How-do-I-change-my-subscription-level](https://support.spotgamma.com/hc/en-us/articles/1500002502721-How-do-I-change-my-subscription-level)  
29. Dark Index \- sqzme, accessed February 3, 2026, [https://squeezemetrics.com/monitor/dix](https://squeezemetrics.com/monitor/dix)  
30. Documentation \- sqzme, accessed February 3, 2026, [https://squeezemetrics.com/monitor/docs](https://squeezemetrics.com/monitor/docs)  
31. GammaLab, accessed February 3, 2026, [https://gammalab.io/](https://gammalab.io/)  
32. GammaLab — Trading Ideas and Scripts \- TradingView, accessed February 3, 2026, [https://www.tradingview.com/u/GammaLab/](https://www.tradingview.com/u/GammaLab/)  
33. Unusual Whales Pricing | Plans for Every Trader, accessed February 3, 2026, [https://unusualwhales.com/lp/unusual-whales-pricing](https://unusualwhales.com/lp/unusual-whales-pricing)  
34. Unusual Whales Subscription | Plans & Features, accessed February 3, 2026, [https://unusualwhales.com/lp/unusual-whales-subscription](https://unusualwhales.com/lp/unusual-whales-subscription)  
35. Plans & Pricing | Options Flow, Discord Bot, Portfolios, API | Unusual Whales, accessed February 3, 2026, [https://unusualwhales.com/pricing](https://unusualwhales.com/pricing)  
36. Webiste for gex : r/options \- Reddit, accessed February 3, 2026, [https://www.reddit.com/r/options/comments/1oqorab/webiste\_for\_gex/](https://www.reddit.com/r/options/comments/1oqorab/webiste_for_gex/)  
37. Cboe US Market Data | Data Analytics \- LSEG, accessed February 3, 2026, [https://www.lseg.com/en/data-analytics/financial-data/pricing-and-market-data/equities-market-data/cboe-us-data](https://www.lseg.com/en/data-analytics/financial-data/pricing-and-market-data/equities-market-data/cboe-us-data)  
38. Cboe Open-Close Volume Summary \- Cboe DataShop, accessed February 3, 2026, [https://datashop.cboe.com/cboe-options-open-close-volume-summary](https://datashop.cboe.com/cboe-options-open-close-volume-summary)  
39. Cboe Global Indices: GAMMA Index Dashboard, accessed February 3, 2026, [https://www.cboe.com/us/indices/dashboard/gamma/](https://www.cboe.com/us/indices/dashboard/gamma/)  
40. LiveVol Pro & LiveVol Core Options Analytics Platforms \- Cboe DataShop, accessed February 3, 2026, [https://datashop.cboe.com/livevol-pro](https://datashop.cboe.com/livevol-pro)  
41. Bloomberg Terminal vs. Refinitiv Eikon: Key Financial Data Platform Differences, accessed February 3, 2026, [https://www.investopedia.com/articles/investing/052815/financial-news-comparison-bloomberg-vs-reuters.asp](https://www.investopedia.com/articles/investing/052815/financial-news-comparison-bloomberg-vs-reuters.asp)  
42. Bloomberg vs. Refinitiv vs. BlueGamma \- Navigating the Market Data Maze, accessed February 3, 2026, [https://www.bluegamma.io/post/bloombergvsrefinitiv](https://www.bluegamma.io/post/bloombergvsrefinitiv)  
43. Navigating derivatives market sentiment with volatility and correlation analysis | Insights | Bloomberg Professional Services, accessed February 3, 2026, [https://www.bloomberg.com/professional/insights/trading/navigating-derivatives-market-sentiment-with-volatility-and-correlation-analysis/](https://www.bloomberg.com/professional/insights/trading/navigating-derivatives-market-sentiment-with-volatility-and-correlation-analysis/)  
44. Creating options strategies with pre-trade analytics | Insights \- Bloomberg.com, accessed February 3, 2026, [https://www.bloomberg.com/professional/insights/trading/creating-options-strategies-with-pre-trade-analytics/](https://www.bloomberg.com/professional/insights/trading/creating-options-strategies-with-pre-trade-analytics/)  
45. Options Analytics | Financial Date | Data Analytics \- LSEG, accessed February 3, 2026, [https://www.lseg.com/en/data-analytics/financial-data/analytics/pricing-analytics/options-analytics](https://www.lseg.com/en/data-analytics/financial-data/analytics/pricing-analytics/options-analytics)  
46. LSEG Workspace | Data Analytics, accessed February 3, 2026, [https://www.lseg.com/en/data-analytics/products/workspace](https://www.lseg.com/en/data-analytics/products/workspace)  
47. Portfolio Management | Workspace | Data Analytics \- LSEG, accessed February 3, 2026, [https://www.lseg.com/en/data-analytics/asset-management-solutions/portfolio-management](https://www.lseg.com/en/data-analytics/asset-management-solutions/portfolio-management)  
48. Unusual Options Activity: Data Provider Comparison | TrendSpider Blog, accessed February 3, 2026, [https://trendspider.com/blog/unusual-options-activity-data-provider-comparison/](https://trendspider.com/blog/unusual-options-activity-data-provider-comparison/)  
49. 0DTE Trading & Gamma Exposure \- Interview w/ Mat Cashman from OIC, accessed February 3, 2026, [https://optionalpha.com/podcast/0dte-trading-gamma-exposure-interview-w-mat-cashman-from-oic](https://optionalpha.com/podcast/0dte-trading-gamma-exposure-interview-w-mat-cashman-from-oic)  
50. Understanding Gamma: The Secret Force Behind Price Movement \- Barchart.com, accessed February 3, 2026, [https://www.barchart.com/education/understanding\_gamma](https://www.barchart.com/education/understanding_gamma)  
51. Learn How to Use Gamma Exposure to Spot Chart Support, Resistance, and Stock Squeezes, accessed February 3, 2026, [https://www.palmettograin.com/news/story/34895735/learn-how-to-use-gamma-exposure-to-spot-chart-support-resistance-and-stock-squeezes](https://www.palmettograin.com/news/story/34895735/learn-how-to-use-gamma-exposure-to-spot-chart-support-resistance-and-stock-squeezes)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAAhCAYAAABkzPe+AAAFBElEQVR4Xu3cWah1YxzH8Z/wRobXlHkOpYhCUi5ecsGFIRSiXqG4kESmuDgvKSJTpsxD5gsXKCGtKBkulAxXChmu5AY3Ev+f/3rsZz/v2ufsnP12ts73U//OWWuvtZ61177Yv/7PWlsCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMypzaOujbov6qR+ee/q9d2i9hioraptdq3Wb9lX2W+Hart55ffSvr9Zn/tmyuv8YNTZzWtWX+dtm9cAAMAqdkzUZ1GHKYPCBVGPajyw3RT1S9TnyqCxIer1qOOrbc6J+iLqj6idlPu/GXV71KHVdvNqr6gron6Muizq/Khvo55TBq3l2j/qrai1ynB4VdR+9QbKa/tp1NeazTVzALyyWvb78Ofk83hM+TkVT0W90L82i/cLAABm5Myo75VdtcJf1vdrvHvm8PCzMsQU3u6IatnOjfqz/99hxKHg/6bTqLu1j/I9LLfbdXTUlxq/zlsoA5L/FrsoQ++t1br/wp/dNVF3RF1XrT8u6t2onZXB/Hnl+C4vm1/zdgAAYA54yvJDZcendWGz7KnST6J2VHZoTu7X+xithahXNZsO0UroNB7QHDy3rpbLOl+Tcu0cXutOVs2vORQf0L6g7FoeXi1fGvVT1IHVuprHrT8vj+nQPYnfRx3YumrZY7ibeErUqcruavFO1DbVMgAAWCFHafpOThf1nXKq9BtNDhTmqdVpj7spudv3yIRaLEx2mq6jdlDUQxqFtUnBydOSQ9OqXvaUax2UntTSYcljOrR5/0ljFm1ge79a9rge32HNx6nPo9N01wAAAGxi/qJ2d2Ua9XTo08pA0QYQ87rLNblzV3tPef/cvOk0fVhxaFvQ4sHJwdj3q7U8/fmGxqeep5kO9ZgPK8ddShvYfPyhwObOHoENAIA55Pup6nuqzA8R/DawvkyHFp4KvbtaNocWd5oc2r7SxvdnmcPB9v3/7hSt0+g+OE87nhC1r0b3xx2i0ZSh19X7+1xdfqJ1iG/gbztrpXzcSTpNF1Y87tXKacrS9Rribl597595WwfWdkp5senQwmP6WrfTo0PawOZOX7mv0EHSU7UOza76fsShjiAAAFgB/jL3FFwJDf6CvkU55eknJovtNP7wgIPKxVF3Veu8r3+uooSnBeX9WZ4eLXwju4OgO3D2hPLY9yqDx53KnwbxU6UHR52hfMr0WeW53qx8CKDcHO9tNmjjBx+Wq9PSga2EtdJZK6FtiK/vy/1fczD19Xzl3y2Sr2Gnxcf2uHU3b7GgaG1g8zTxa8qunu9DdGj0/q4S0n1+3g4AAMyJD5Q/I+EA9oByOu4ejabpPFXmn/Jw+Hop6vGoX5VdOHdo3EG7MeqHqI+j9szd/ln+q/+7pl+3Tvn7YyVguDvmrp2nWB3iXA4tDnDe50RleHPQ8Vg+T2+zu3dWHvuifp9ZOFL5BKWfcv1IeU0mOSvq9GadQ1vbUSzeVgZUv2f/f57GO4OnKcf+XXmNHUyHeNyax7xew+P6/H3M8tn5/TnAPRN1gzIM++nVoos6Vnm8tvMHAABWgfJUpTtiDmyeJnTQ8rTlgvJeuvXKbtCLysDg4FYeDvA+t0VdouyoucvkfWcZ2AAAAFCZdN9Zre0aEcwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKvR35tstSlYkHt2AAAAAElFTkSuQmCC>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAVCAYAAACQcBTNAAAAX0lEQVR4XmNgGJpAAIglicDCIMVWQDwPiv8B8UIojgDiLiC+AsUHSFYMAsZQ/BWIfaEYBnigGGQYGOBTDAMJMAYxiqVhDGIUw8GoYhhIB+IbUPwfiJ9CcT8DJJENNgAAQY8pR48DaEEAAAAASUVORK5CYII=>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAAYCAYAAAAPtVbGAAABU0lEQVR4Xu3UvytGURzH8SMUUUrKj8ivUgYTizIyGBhkEVntBj9m+RcM8mOSYrYgyWowYTIoZZJSxKB8Pp3Pub7PufcuejzTfddreO65zz333nPvda6oDFXBgKzAFsxCvWRVC63QHmm0O4V64BTWpAnqYBmupTvsbGp2/kRu4EEWYdDuNCJ3MG4HVA0cGvwd1wK3sCkldcK9rDt/u7JaFZ4lb03cMLzBtJT075PwgBvwJL12MCpM8gpD0RhbgmfokySeEa/gQPKugtv35dH5J8cWxs+hQZJ4ie/OPz2UV1hUOnH+ibPZRU81Cl8wJXnNwKdMRGMsrMdkPMAqMglflheYl6z4Ql7BtvDtjrOLnop/ODLiA/AzsgPHzk9GNi54WPRLl/MZYW1wJnswBgvCbXNQnez9G9+FC/mGD9iFLkkVzqjD+fvaL1kH/3MVmaSoqLz9AD14TL4OGyiUAAAAAElFTkSuQmCC>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB0AAAAXCAYAAAD3CERpAAABU0lEQVR4Xu3UvytFYQDG8feGIqRQKIOYTBSSMioUi4XBZrBa5MdiMllkNqCQWUmSbvwNSpmUrP4C5fne+7z3Htc9EoMf3ac+9fb+OM/pnNMJoZL/njbZkKXSBSUjs3Yhx7IrzRbTLnvGHvZOhfx55FIry7Yld7ISFxMZkStr8dy8HFm1MWYehL2c4TzepUGyoXzpjuxbzIDcW68xZh4xnOE83uVXlSbnk2vd8mSTMi0P0mExm3Jp9Yn5XNJKG+XG88k1LkwJKJzxuLSUM1mj403SSlvl1vMflS56/HdL095ppzwapWnvdD18oTQjhyH/M0AMX2gsHTJK+yyGr5fz4FpvklZK5uTU+KGQCbm2JmM8ZqROzkL+PApZMP4cL/IsJ9bvPdzQga3JsJzLoMWMh+KjZM+qbEuNFfIjpZ9NlfXIaCg+5tJwg2BPVyjzHiup5Nt5BZBFczVx28oOAAAAAElFTkSuQmCC>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAAmCAYAAAB5yccGAAAHPUlEQVR4Xu3deYhkVxXH8SPGJWjUqDGuOIkScMGFuKAoCEZQxAUTRYy4IK4JIjEx7gZUUFTcwH0HMYkGBFc0xIAghviH/iGGqKASCVGiICgquJwvt+7U7dP1al5Nd80MzfcDh+l6VVOv7q2G95tzb9VESJIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIOgJOyPpf1v6zLss5bUa/L+syi/r14LHWb0IngCVkXZN2p3iFJkg6OB2bdmHV11l3LfdVtsx6VdU3Ww8p9OvbOyHp71oVZHwlDtCRJB9rTonXN5l70CW7vrAfTKfWAtuo+We/LelLWt+LE67Lx+8DviiRJJ4RDWddmPTHaRfTpWddlPXb5kHh11h+ybo621PimrK9nnT885llZP8j6b9b9onW8WIr8VLTn3iY6bIS239Y7Znhw1lez7px1TtbXoj3Xl6ON89tZfzv86L1jbl+cdcdoIfO7sbM7yNy9POsnWS9c3N6L07PelfWG4RjBlveKsbKs3N0u66Ksq7Lem3XycN9ePCbrEVl3yHpFtN+n7pUxL2gfydSYRozvO7Ec34h5GucIl0R7ryRJOq64kN6U9bJy/JdZ9xxu8zPH6kXuGeU2e5L+tfiZEPLZ4b5tYonzz9GCFsFrEx+OFlK7s7P+Hi2AdpcOP+/F87IeMtxmjn4abQ/eiMeMYfhoEQo/kHVD7BwD79M9Fj8TSNgPCALiFdHCz7tj9+s6GvfK+tFwm9dEVw2PjHYu5uX2hx9xdKbGNGJ8hLY+PvB6CGbMU32fCcsEPEmSjqtfRbtw1Q7HJ8oxQgxdpmdH67rQLenHR9z3/azTst6f9bidd2/VuVn/idYVq+NZh9dLd6VbFdjGbmPHhf8B5djdF7XKo7NuqQejdfLoEI6Y5zq33aHYPb51y4kE2GtjZxj52PAz5yEgElwIJ/1xjJ+QXjFX9XyHYvdr6gj1vxtu8zj+AXD/aL9/hOzx9Yzq/GJqfleNadTH1zG+8R8lzFMNbLzWL5RjkiQdU3QPvhGrOxHVF7P+mvWlrD/FskOyChf0uc/bsRT7oVh+orPW62Pe89FhIQDwQQQ+kDBHDQurAtsU9jjRHQLnm/rgw8Ojzd9by/Eepqh6bAoh4vnRlu843ydj/VhrYGNv1o8P39vmnrESoOi29nEzDyyDr8IyMufmtdRlxIrH9SXrf2S9dufdazG/b4w2x4yRsa6a46kxjfr4OsY3huJVgQ0EzhpQJUk6ZrhYsV9pjnE5lP1eY0eqem60C+MZ9Y5073pgCwhGhAOC3hz1Ir1JYAOB4uJoYWIKz8VrqkvIdIFujZ2hsR9bp4c29geuC2uoga0vb3c93PTzzgls4NyXxTKwrkM3ko4rYZ+53UQPbVNhDVNjGtV5nRvYeMymy+ySJO0b9vyMF7WXZn0l2gW1drRYDu1h41WL+whkdRmMizcdF/ax8XUNI/4+y68vKsf322uihSOW2+aoF+lNA9tZWb+IFqCmsHeK5xwDAjg3e+/GrxlhOZTQeSR0E+cs/9bAVjt4dJ4YKyHn94ufwTLw2JGq3hFtk/9UiAL718YlzN5p3BRzvG5+p8Y06uPrGJ+BTZJ0wqPjMH5aD2dG+yRoxTHu6wgJbxlug/1qdFHoprAvjM30/WJ+arRw8dRoy6Xj3iFwYWfTd10K7cUX4M79igVe589i/v65epHeNLDR+WF865YGz4n2nHUp+dexO3TRbbt+uL0KIYgOVw/I60JbDWw8li5px3gJL6dEW1bsXVfGPxXY+lJwX6acwjnHUMR78/Ph9hwsv3IOxjnVzZsa06iPr2N8BLtuKrDxPAY2SdJxdXm0DeF01AhMH4wWBDq6YtdF+18CvhktPP0l2ld39IsnnbnfRLu49w8j8KlEulx0U+6yOMaX1v4zpi+6+4GweG49eATfi+V3sL0t64/RXvst0TbTT7lb1nvKMbqPfLhgFQIyYYXOJgH0h7EzaPF3CWqcm6XDPm8Vna26DPqccnvEFwXzYQzeC94DEEAI3I+PFq47ulB0zfjULF9nUs8D5ree782xeo8hvzN8bQnfe/fpaF+3scl+MOZ37OAxX8zTKlNjekEs3xPG95JYjq/jq0aYJ+boiljOE+q+Q0mSjguCx1OifYpuW7jQPjTrmVmfj+10LDjHJYs/N8GFm6W6Y4HOFCH4vrH569xvD4rW8avvO6GXr3vhz73id4txMt7Ty33bMDWmEcvPc8d3cuzs3EmSdKCxBEqHhdBGF4slxP1EKLgw6+P1jgl0efoFm+/sWvU/H0hPzvpoPShJ0kHHktQ2XBnrN7+P6JrUgMbfZS+Z1LG/c1walSRJe8A+q1V7rSqWydg/x367+mlNSZIkbQlB7cbY/anSsdhEzv8xymb+XnTZJEmSJEmSJEmSJEmSJEmSJEmSJEmSJEmSJEmSJEmSJEmSJEmSJEmSJEnSfP8HhLgmp782bKcAAAAASUVORK5CYII=>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAYCAYAAAAs7gcTAAAAx0lEQVR4XmNgGPRABYgbgbgYiiVRpRkYGIE4C4pnAbEwECtC8UYkdWBAkmJtIN4AxfxockFofIYiIF4KxSBbkIEvGh+s+CsUpzKgms6GxAYDkhRrAvFzKP4PxYegWAZJHRxwQzHIjasZEJomISuCAYKKlaEYPbhAoBWKV8IE6qAYI0qBoAqKQRrAgGjFgkB8AIot4UogABTdm6EYFLvg4ILF2h4gzoPiaCDeDsSeUAwGIJNhIcDKADEBhB2AmAOmCAZIUjzUAAC3HS3XCm+iMgAAAABJRU5ErkJggg==>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAE8AAAAYCAYAAAC7v6DJAAAC3klEQVR4Xu2YS6hNURjHP3nneZFX5HiklEhISkbyCCURAzN55Q6U9yNSFBPJxCMDV2FgQClJ4sbQhIEMTCgMTIwY4vtZ39dZZ9t7n3PuucdV1q9+de5ae6+993+vx15XJNEnLFVPqXvNYbXViTJSeAWMVLebl9QVEsJZbk5XT6gD1U7zotqPk/9nFqmP1HnmYAkhvld3mZPUc+pwdZn5QP5e7+MlbTEfq3fU6+oYs4yJ6g2T8zh/nYQ245fP74p5TV0b1eUyXn2mzs2UD1HvSjUohwucNndH5e2GKeOpOdbKtqm3zQFWloVy6jkWgfNphzYRRkvoHO5Xdb3VFbJGQg+jZ8UQEsN0nOnQ4A6z3pBliOPUbEWE95x6vYeppMt0FqrvzDlReQzl1HMsOrRDmxhDDvhBUnjtD++HekGq491DYT7jt/89X10ZlW1UB1ldHn4ci8uGTB1MUy+ro8wimGe71cOmM0P9bPIceRAAQXgozln1iRnP202Fx03TwM/I7+oeqe1ZU9S3meOyb62I/up+CWE7cXD1GKG+kD/D84cse1CumRce7XSbvBynqfCAocWKe978on6T2m7eKh7gAbPR4IBp4430LDy+FHo9PFZZzJtrWHkbWm2aZLb62tycqSujaNgyGj6aRfdaNGyPSQqvb8LzG8kbmkzEr6R4BesJsyQM1Q5zn9TOgWUw996S8FGMDvfu4S2OymMoJwgWO3S6JLSJ8dxeNzw+gO+Z8QPQCB6SsPrGjbaCBxfPcbTdTIBbJexokPuH1epzk7Zp87h6xRxq5dSz3USg/KGENjGmbnj0rPsmjZxUN6lXTd5ub2y7+GrHM5K/OPCwO9UFZhkMrZvmUXWJhC0lCx0Cuwnq2X6hD8dVUh2inHdEwr7cv0OBF3JQfWnyNfFJwkuomL/hnwD+YDzAZAkXmGD+q7Bi40wJW0bvgY1AkL4vr0gLoyqF10J4iUQikUgk2skvnf2xY02GFh4AAAAASUVORK5CYII=>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAAWCAYAAABDhYU9AAACCElEQVR4Xu2WS8hOQRyH/25FKaFcSrmtrBDii5VLCBsLLOyVvVwWSpLUtxAlpFwKOxZySdKHsrFSlLJS2FvY2PB7zvzGGec7Y2Hzvep96mlq5n9mfuc9M+e8Ef8Zs+S0budEMsmuka/lWbnQTjgDG45QR+wpeVMekNft6ra0edy4Ud6P/vAL5A17Vz6Vu6P9AYB2v8eQumtyjsd/s1Tes7PlRbkhUlAcdd0qeclekZ9ifLip8o48aGGufC5HLNDSxxgC9VzLHNjAo6QwFxNui3xhz+XCgj3RH26F/BhpTszwNC5YoKWvhHquZQ5sINBb+1A+duHfqIUr+8uxM/KZnSfH5NFiHJbJr3KnbRjocLDLfpc/5Q952OZNXFILt7foL8cIMmY5MK/cV0I91zI3jmN6pE35JlJA3PZHRaIW7lDRXwu3WL53X0lvOL4Ixy0/LQdirTxt8yYuqYWrPdYT0Yab77YbbpH8HJ1w7K9vdl+kcPTlIt4/XWrh1rl/pc1wMm/byW6787Im4ZgDGzgQJy0vWMKNyKt2Ry4sqIXjKbyUWy3MkI8ivdgRaB9E2kYIrMO1zIENAx0ONlsm+SDfRdonmP+hLJGX7ZdIp5qDkz99eZHt0e6v9fKYPB/tpw9mylvR7nXqnkTa61WmRPoilPvlX2Bx3BTppvpeR6y13FKXb27IkCF9/AJUL411/nAIkwAAAABJRU5ErkJggg==>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAAXCAYAAADpwXTaAAABHUlEQVR4Xu3TP0tCYRgF8CcicJNwasu+gEYNRVshBNEqfgb3hhyEaJCgqSAqgmhprKnaAhcXJ8HBtaEP0NDSkuf4nHtfvHgF+yMEHfgt1+ee633f95r9crIwl7z41Xy7bEZWoAUNWJCJwpI9OYAbqMC1LIfRwT+mDbi3EQ/Lw53MwymsmRfTseaKcCYX8GIjyvhqz5IzL9uCphyF0Ti7No0yFnTkAZ7MHzAuqWXMjrzDJ3xAVbhByYwti5KBW2ibF1JpaMIznTKe+H1ZMt+AVTiUkzAaJ7WMi/0mZfMyXuMNdBVG46SWcTfrwtPNsnW4lO0wGie1jNmUR+hBF2oSffSLcC6v5rvOtY0+Ra73ID9aFmXW/MQXkj/85w+kDwWVTwpo6qk9AAAAAElFTkSuQmCC>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAXCAYAAABNq8wJAAACbElEQVR4Xu2WS6hNURjHv4NbRHnc8ijllYGR5HnLQB4hTAwwMJUylTwGShJKklsGUlyFGQN5JGmjTIwUpYwIcwMTA3y/vf5fZ+99zlkDE53T+dev1V37W/+1/mevtdc1G0DNdEaanf2kvgzQEqudN855Z4HIabqlsP81MAs/Js44E84B56ZY1S6tadR5Zik0hOY7t8Q9SzW7BXMh2v2C59TdcOaIUC+v+MFLLXHui9nOuLPBUhi4FIUVMfis89PqAaY4d52DAhH0hRhTH2308RxRz1jAJ+fF+PAqJ6+aEWCL81JcjMKKNjrXnC9WD7DC+dToQ7xVuKq/aaMvRD1jAZ+cF+PDq/8DsOh34pHzxOoDqqIWLjibrDPAHuezdX4AzonnzlyncI6L0FLnu9hpeS98gI9IqV2CPf3H+eUcES3V0B4VHGwW3Qyw17pPGostLB3M15W+EPWMBRaf8yrEjEp/qamWDs5bSyFgm56tcw4J1C3AYes9aUy8yPlQ6Qs1A+S8CjEYAbh5Twr24bizxtJnEjgsFF52lgsMtzvf1AI1vfbtKVE489Q2Ayx0vgp8cl6FKAPw6/0Q+ywFoC9MuGBmWTq41ys8sPSGaIGDt9bSpCtFaELccSapxRdCzBkB8Ml5MR5adIw6p8WIpQBj1l7ojnJYp7ptId7mK2erQNOcx4IbHtE+FGxbxDyMBXxyXowPr1KbBQ8/Ou+t/doJ1RT7k7rfaoErHrGdCrHeOeFcEeHFq78t2LrUPbW0dSHUywuf2rr6PkBosqWbt7rn/kUsELixF1vjny+JuWCZpbrYSk118xpqqKEGRX8BgdLeSU0wrIsAAAAASUVORK5CYII=>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB0AAAAXCAYAAAD3CERpAAABvElEQVR4Xu3UvytFYRgH8EcootBd2FAGk+R3GeRHCItBBquUVfJjUJJQkiiDFAZsTChJl8FiUgZlovwBBosB3+95nuOec+6hCPcO91ufTr3nfc/z3vd97yuSJMmDzGDjX+ffiqaZKriEOSgyXyVHdILfniSLjZpp2IZ+2DSVsa6+ROBEdKLkphC2zJ5on26J/TAnJbBvCmAV6kUnQItuR084eAaexV80A3ZhwDCc3Bk0GCccwEZiBxZtgXOz4Hb0pBHW4EH8RcvhLtDGcPVWjJOEFGWha3MIx+If4A370jw0SXzRHriX+EM4C6eGh89Jl+EevcELDBt38/kcMTxcLBQs2ivhRccganI97U6yRA/ClWhharN3tTBomLCiQ5LMRXkDTZhS0YNULfqXIG4+Oy5BmeEH2+HRnsQ+n+3ppASKcpZPpk+0KNv4AdqAfNHDs+5xILoSfFIn1IgWrTBueHp3jHNGIjBleJ2xKP/E7sc7nGHxCVtertoFtBomG45Ebzn6SLPhy1u4EV0SCrtXuXfs92pP4lXHcKmjpg7GYVlC7uiEFHWTLnoDeffjJ+FhId5cxeK56FNJ5dfyDgQEgyQzrGvvAAAAAElFTkSuQmCC>