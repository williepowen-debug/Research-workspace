# **Structural Determinants of Market Microstructure: An In-Depth Analysis of Gamma Exposure and Hedging-Induced Volatility**

The contemporary financial landscape has undergone a fundamental transition from a price-discovery mechanism driven by fundamental valuation to one increasingly dictated by the mechanical flows of derivative hedging. At the center of this transformation is the concept of Gamma Exposure (GEX), a metric that quantifies the dollar-denominated hedging obligations of option market makers. As the volume of options trading continues to outpace the growth of underlying equity markets, the structural positioning of these market makers has become a primary driver of market stability and fragility. This report provides an exhaustive examination of GEX, analyzing its historical impact during catastrophic market events, its integration with traditional volatility indicators, and the practical methodologies required for its calculation and implementation in systematic trading frameworks.

## **The Theoretical Framework of Delta-Gamma Hedging**

To understand the systemic implications of gamma exposure, one must first delineate the operational constraints of the option market maker. Market makers facilitate liquidity by taking the opposing side of trades initiated by retail and institutional participants. Because their primary objective is to capture the bid-ask spread rather than take directional bets, they must maintain a delta-neutral portfolio. Delta, representing the sensitivity of an option’s price to changes in the underlying asset, is dynamic. As the price of the underlying asset moves, the delta of an option changes—a rate of change defined as gamma.1

When a market maker sells a call option, they become "short delta." To hedge this, they must buy a specific amount of the underlying stock. However, as the stock price rises, the delta of that call option increases toward 1.0, necessitating further purchases of the stock to maintain neutrality. This relationship is governed by the gamma of the position. In a regime of "Positive Gamma," market makers are positioned in a way that their hedging activity is mean-reverting. If the market rises, they sell the underlying to reduce their long delta; if it falls, they buy the underlying to cover their short delta.3 This provides a stabilizing "volatility dam" that dampens price swings.

Conversely, in a "Negative Gamma" regime, market makers are forced into pro-cyclical hedging. They must sell as the market falls and buy as it rises to keep their deltas in balance. This mechanical necessity creates a feedback loop that amplifies volatility and can lead to rapid, cascading price movements.6 The "Gamma Flip" point represents the price level where the aggregate dealer position transitions from positive to negative gamma, often serving as a structural pivot between low-volatility mean reversion and high-volatility trend continuation.8

| Greek | Definition | Market Maker Impact |
| :---- | :---- | :---- |
| Delta (![][image1]) | Sensitivity of option price to underlying price change. | Determines the initial hedge size (shares to buy/sell). |
| Gamma (![][image2]) | Rate of change of Delta. | Dictates the frequency and direction of re-hedging flows. |
| Vanna | Sensitivity of Delta to changes in Implied Volatility (IV). | Forces hedging when volatility regimes shift rapidly.5 |
| Charm | Sensitivity of Delta to the passage of time. | Drives "pinning" effects as options approach expiration.10 |

## **Historical Case Studies in Gamma-Driven Market Instability**

Historical volatility events provide a laboratory for observing the real-world consequences of dealer positioning. While fundamental catalysts—such as a pandemic or a central bank rate hike—often ignite a move, the structural "plumbing" of the options market frequently determines the terminal velocity and depth of the correction.

### **Volmageddon: February 2018 and the Collapse of Short Volatility**

The events of February 5, 2018, known as "Volmageddon," illustrate the dangers of a concentrated trade in the volatility complex. Prior to this event, the market had experienced a prolonged period of suppressed volatility, with the VIX fluctuating between 10 and 15 for months.11 This environment encouraged a massive buildup in short volatility strategies, primarily through inverse VIX exchange-traded products (ETPs) like XIV and SVXY.12 These products effectively engaged in a short volatility carry trade, profiting from the steep contango of the VIX futures curve.6

The catalyst for the unwind was a minor macroeconomic shock on Friday, February 2, which triggered a 6% correction in US equity markets.11 However, the structural failure occurred on Monday, February 5\. As the VIX began to rise, the inverse ETPs were forced to buy VIX futures to rebalance their leverage and stay within their mandates. This created a self-feeding loop: rising VIX ![][image3] forced futures buying by ETPs ![][image3] higher VIX ![][image3] more ETP buying. By the end of the day, the VIX had surged over 100%, and products like XIV lost 90% of their value in a single session.12

A critical and often overlooked component of Volmageddon was the gamma positioning in the VIX options market. Analysis of the IvyDB Signed volume dataset shows that between 9:55 a.m. and 10:05 a.m. on February 5, over 500,000 net VIX calls were purchased.13 This occurred while the VIX was still near 19, well before the afternoon's parabolic surge. These trades placed market makers in an extreme negative gamma position. As the VIX rose, dealers were forced to buy VIX futures to hedge their short call positions, significantly accelerating the surge toward the close.13

| Metric (Feb 5, 2018\) | Value | Significance |
| :---- | :---- | :---- |
| VIX Opening Level | 18.44 | Near long-term averages before the spike.13 |
| VIX Closing Level | \> 37.00 | Historic single-day percentage move.13 |
| Peak VIX Options Volume | 400k Calls in 5 mins | Exceeded median daily total call buying for the prior 2 years.13 |
| XIV Market Impact | \> 90% Loss | Termination event for short-volatility ETPs.12 |

### **The March 2020 COVID-19 Crash: Liquidity Failure and Gamma Mainstreaming**

The March 2020 crash remains a definitive case study in systemic liquidity dislocation. While the pandemic was the exogenous trigger, the velocity of the \-33.7% decline was driven by a total failure of market liquidity.2 On March 12, "Black Thursday," electronic futures liquidity in the E-mini S\&P 500 fell to a median of just 10 contracts ($1.5 million notional) on the bid-ask screen, down from 120 contracts ($18 million notional) in 2019\.2

In this illiquid environment, dealer hedging became the primary source of order flow. As the index plummeted, market makers who were short puts were forced to sell futures aggressively to maintain delta neutrality. Because the market was already below the "Gamma Flip" or "Volatility Trigger" level, every downward move required more selling from dealers to remain hedged, creating a pro-cyclical cascade.2 This period is cited as the moment gamma analysis became "mainstream" among professional traders, as traditional support levels were obliterated by mechanical hedging flows.2

| Notable Date (2020) | S\&P 500 Performance | Market Microstructure Condition |
| :---- | :---- | :---- |
| February 19 | Record High | Market characterized by peak complacency.2 |
| March 9 | \-7% (Black Monday I) | Circuit breakers triggered; liquidity begins to evaporate.17 |
| March 12 | \-9.5% (Black Thursday) | Liquidity in E-mini futures reaches record lows.2 |
| March 16 | \-12% (Black Monday II) | Peak volatility; GEX reaches extreme negative territory.2 |

Historical decomposition of the S\&P 500 index confirms that the negative effects of the pandemic were most concentrated in March 2020, exactly when the gamma profile was at its most negative and liquidity at its most scarce.18 The subsequent recovery was equally gamma-driven; as the index reclaimed the flip level, dealers were forced to buy back their short hedges, fueling a 29% surge between March 24 and April 17\.15

### **The January 2021 GameStop (GME) Gamma Squeeze: The Retail Offensive**

The January 2021 short squeeze of GameStop (GME) introduced the concept of a "Gamma Squeeze" to the public consciousness. Unlike index-level crashes driven by systematic selling, the GME event was a targeted exploitation of market maker hedging mechanics. Approximately 140% of GME's public float was sold short, a mathematically fragile position that left institutional short sellers vulnerable to any upside price pressure.20

Retail investors, organized primarily through the r/wallstreetbets subreddit, realized that by purchasing deep OTM call options instead of just the underlying stock, they could force market makers to buy the stock to hedge their deltas.20 As the stock price rose due to these purchases, the gamma of the calls increased, requiring market makers to buy even more shares to remain neutral. This created a recursive loop where call buying led to dealer buying, which drove the price higher, necessitating more dealer buying.6

| GME Timeline (Jan 2021\) | Event | Market Reaction |
| :---- | :---- | :---- |
| January 11 | Board Appointment | Ryan Cohen joins GME board; positive momentum begins.20 |
| January 22 | Peak Short Float | 140% short interest identified; volatility spikes.20 |
| January 26 | Musk Tweet | "Gamestonk\!\!" tweet fuels retail frenzy.20 |
| January 27 | Peak Gamma Squeeze | GME rises 93%; intraday gains hit record levels.24 |
| January 28 | Buying Restriction | Robinhood halts purchases; stock hits intraday high of $483.20 |

The GME episode demonstrated that gamma is not just a passive indicator but a "weaponizable" force. The massive influx of call volume—over 175 million shares traded on January 25—forced a total capitulation of institutional short sellers and required billions in liquidity from market makers who were caught on the wrong side of the gamma profile.20

### **August 5, 2024: Japan Carry Trade Unwind and Global GEX Contagion**

The market turbulence of early August 2024 represents a modern intersection of global macro deleveraging and equity market microstructure. The yen carry trade, a strategy where investors borrow yen at near-zero interest rates to fund high-yielding investments in U.S. tech and emerging markets, became the locus of a global sell-off.26

Signs of fragility appeared in mid-July as rumors of Bank of Japan (BOJ) interventions began to reverse the yen's depreciation trend.26 On July 24, a brief tech sell-off saw AI/tech stock valuations drop by $1 trillion, signaling that the carry trade was beginning to unwind.26 The crisis peaked on Monday, August 5, when the Japanese TOPIX index lost 12%—its worst day since 1987—and the Nikkei Volatility Index spiked to levels seen only during the Great Financial Crisis and COVID-19.26

In the U.S., the S\&P 500 tumbled 3%, and the VIX briefly registered levels above 60 in off-hours trading.26 The magnitude of the VIX spike far exceeded what was predicted by historical relationships between the VIX and S\&P 500 returns.26 This discrepancy was driven by forced deleveraging and margin calls. As hedge fund leverage had been on an upward trajectory leading into the event, the initial rise in volatility forced participants to cover short volatility positions or purchase VIX futures, thereby further amplifying the shock.26

| Market Indicator (Aug 5, 2024\) | Value/Change | Context |
| :---- | :---- | :---- |
| TOPIX Daily Return | \-12% | Record drop since Black Monday 1987\.26 |
| S\&P 500 Daily Return | \-3% | Contagion from yen carry trade unwind.27 |
| VIX (Off-hours Peak) | \> 60 | COVID-era levels of extreme fear.26 |
| Speculative Yen Shorts | ¥2 Trillion ($14B) | Historical peak positions unwound rapidly.26 |

The August 2024 event highlighted how "procyclical deleveraging" can override fundamental data. The BOJ’s unexpected rate hike, combined with weak U.S. jobs data, created a "perfect storm" that pushed the S\&P 500 into a negative gamma regime where dealer hedging exacerbated the global carry trade retreat.26

## **Integration of GEX with Quantitative Market Indicators**

The utility of GEX is maximized when integrated with other technical and sentiment indicators. By understanding the interaction between dealer positioning and price-based volatility metrics, traders can more accurately identify regimes of stability versus impending breakout.

### **GEX and the Volatility Index (VIX) Interaction**

The relationship between GEX and the VIX is foundational to understanding market "regimes." Positive GEX values are inherently stabilizing; market makers hedge by buying into dips and selling into rallies, which effectively stifles realized volatility.1 In these regimes, the VIX tends to be low or declining. Conversely, negative GEX implies that dealers must sell into weakness, which magnifies price swings and leads to higher realized volatility, eventually pushing the VIX higher.3

Research indicates that GEX provides a more granular view of volatility than the VIX alone. While the VIX is a 30-day implied variance metric derived from option prices, GEX focuses on the *quantity* of existing contracts and the *necessity* of dealer re-hedging.3 Significant volatility expansion typically occurs as GEX trends below the zero line.5 In some instances, GEX can lead the VIX, identifying structural fragility before it is reflected in the prices of protective options.

### **Predicting Realized Volatility and Next-Day Returns**

The predictive power of GEX on future market behavior is supported by both practitioner data and academic research. When GEX is in its highest quartiles, subsequent realized volatility is significantly lower. For example, historical analysis of an index trading at 2000 showed that the 1-day standard deviation for the highest GEX quartile was 0.55%, compared to 0.85% for lower quartiles.3 This 4-point daily range difference illustrates the pervasive impact of options-originated liquidity on the underlying market.3

Academic studies, such as the thesis "Convexity in Motion," have utilized Autoregressive Distributed Lag (ARDL) models to quantify the relationship between changes in GEX and S\&P 500 returns.31

| Period | Relationship Observed | Statistical Finding |
| :---- | :---- | :---- |
| Pre-2020 | Strong Positive Correlation | 1B unit GEX increase led to \+0.24% S\&P 500 return.31 |
| Post-2020 | Moderate Correlation | Weakened by the rise of 0DTE options noise.31 |
| Long-term (2011-2025) | Directional Significance | GEX inclusion significantly improves forecast accuracy over random walk.31 |

These findings suggest that market maker hedging introduces "mechanically induced flows" that have immediate directional implications for short-term returns. However, the rise of Zero Days to Expiration (0DTE) options has introduced a new layer of complexity, as intraday hedging flows for these contracts may create "gamma noise" that is not fully captured by aggregate end-of-day GEX figures.10

### **Combining GEX with the Put/Call Ratio**

While GEX focuses on dealer hedging, the Put/Call ratio provides insight into the sentiment and positioning of the directional traders who are the market makers' counterparties. Combining these indicators offers a more complete picture of market sentiment.

* **The GEX Ratio (GR):** Calculated as ![][image4]. A ratio ![][image5] indicates call dominance (bullish), while ![][image6] indicates put dominance (bearish).32 Unlike the standard Put/Call ratio, the GR incorporates time sensitivity, naturally weighing near-term options—which have higher gamma—more heavily.32  
* **Leading Signals:** The GEX Ratio frequently leads price movement. A declining ratio while price continues rising often warns of upcoming weakness, while an improving ratio during a price decline may signal a potential bottom.32  
* **Sentiment vs. Hedging:** Combining "Net Flow" (actual trader sentiment) with "Net GEX" (dealer hedging impact) allows traders to identify setups where directional conviction aligns with supportive market structure. For instance, high positive Net GEX combined with high bullish Flow Ratio (![][image7]) indicates a robust, stable uptrend.4

| Scenario | Net GEX | Volatility Q-Score | Trading Strategy Recommendation |
| :---- | :---- | :---- | :---- |
| Market Pinned | Positive | Low (0-1) | Short premium; Iron Condors/Credit Spreads.4 |
| High Volatility | Negative | High (4-5) | Long premium; Straddles/Directional calls or puts.4 |
| Trend Potential | Near Zero | Rising | Watch for breakout confirmation at key GEX pivot levels.4 |

## **Practical Implementation and Calculation Methodologies**

For market participants seeking to internalize gamma analysis, the transition from conceptual understanding to practical implementation requires a robust data pipeline and a rigorous mathematical framework.

### **Fundamental Calculation Mechanics**

The primary goal of a GEX calculation is to estimate the notional dollar amount that dealers must buy or sell per 1% change in the underlying asset price. The spot gamma exposure for a single option contract is defined by:

![][image8]  
In practice, practitioners often simplify this to the dollar value of gamma per 1% move. If a market maker is net short gamma, they must SELL a dollar amount equivalent to their GEX figure for every 1% move DOWN in the index to remain delta neutral.8

To build a comprehensive GEX profile, a trader must:

1. Source the entire options chain (strikes, expiries, open interest).  
2. Calculate or source the unit gamma for each individual strike.  
3. Apply the counterparty assumption: in index options, aggregate customers are generally net short calls and net long puts (making dealers long calls/short puts).1  
4. Aggregate the results across all strikes and expirations to find the Net GEX and the Gamma Flip level.1

### **Data Sourcing and Frequencies**

The frequency of data updates is critical to the utility of the GEX metric. While End-of-Day (EOD) data is sufficient for swing trading and macro analysis, real-time data is required for intraday delta hedging or trading 0DTE options.

| Frequency | Data Source Type | Application |
| :---- | :---- | :---- |
| Real-Time (Intraday) | OPRA Feed / CBOE 1-min | Scalping, 0DTE hedging, intraday support/resistance.1 |
| End-of-Day (EOD) | CBOE EOD Summary / CSV | Risk management, identifying next-day volatility regimes.1 |
| Weekly | OCC Open Interest Reports | Long-term structural analysis; monthly OpEx positioning.35 |

CBOE's "Open-Close Volume Summary" is the gold standard for high-fidelity calculations. This dataset categorizes every trade by participant type—customer, professional customer, broker-dealer, and market maker—and indicates whether the position was an "open" or "close".36 This allows for a much more precise estimation of the aggregate dealer book compared to simple assumptions.7

### **Approximation Without Subscriptions**

It is possible to approximate GEX without expensive terminal subscriptions by utilizing free data provided by exchanges like CBOE.

1. **Manual CSV Downloads:** CBOE provides delayed quotes for the entire options chain of any ticker (e.g., SPX, AMZN) at the bottom of their quote table pages.8  
2. **Black-Scholes Modeling:** Since free data usually lacks unit gamma, traders must calculate it themselves using Black-Scholes formulas. This requires sourcing the spot price, strike, time to expiry, interest rate (swap rates), and implied volatility (IV), the latter of which is often provided in the free CBOE data.8  
3. **Excel/Python Aggregation:** Once the unit gamma is calculated for each strike, a simple pivot table or Python script can aggregate the data to create a GEX profile.8

### **Open-Source Tools and APIs**

Several open-source projects and platforms facilitate gamma calculation:

* **QuantConnect:** Provides a basic algorithm framework for calculating gamma exposure across SPX strikes and exporting the data for visualization in Jupyter notebooks.23  
* **OpenBB Terminal:** A community-driven terminal that has explored automating the download of CBOE option chains and performing GM/GN/DN (Gamma/Delta) calculations.37  
* **TradingView Scripts:** Various community scripts allow traders to visualize GEX histograms, call/put walls, and zero-gamma levels directly on their charts.34

## **Synthesis and Strategic Implications**

The structural evolution of the equity market has reached a point where the "tail" of the options market is frequently "wagging the dog" of the underlying cash market. Gamma exposure serves as the most effective lens for viewing this dynamic. From the explosive collapse of Volmageddon in 2018 to the targeted gamma squeezes of 2021 and the cross-asset contagion of 2024, the evidence is consistent: when dealers are forced into pro-cyclical hedging, volatility becomes self-perpetuating.

For professional market participants, GEX should not be viewed as a standalone predictive indicator but as a measure of structural constraint. A negative GEX reading does not guarantee a market crash, but it identifies a regime where the "volatility dam" has broken, and the market is susceptible to rapid, liquidity-driven drawdowns. Conversely, a high positive GEX regime identifies a market with deep mechanical support, where mean reversion is the dominant force.

The integration of GEX with indicators like the VIX and Put/Call ratios, supported by academic evidence of its predictive power on next-day returns, provides a robust framework for systematic strategy development. As the market for 0DTE options continues to expand, the necessity of real-time gamma analysis will only increase. For the modern trader, understanding the hedging obligations of the market maker is no longer an optional edge—it is a fundamental requirement for navigating the modern volatility-driven environment.

In summary, GEX analysis allows for the construction of an "implied order book," revealing where option-originated liquidity is abundant and where it is scarce.5 By monitoring "gamma walls" (large clusters of call or put gamma), participants can identify key levels of support and resistance that are defined by mechanical hedging rather than psychological levels. As the "snake eats its own tail"—with volatility feeding into risk-taking and financial engineering—the importance of monitoring these structural flows will remain paramount for maintaining market stability and identifying opportunities in regimes of volatility-induced fragility.14

#### **Works cited**

1. CBOE Volatility Index Gamma Exposure (GEX) \- Barchart.com, accessed February 3, 2026, [https://www.barchart.com/stocks/quotes/%24VIX/gamma-exposure](https://www.barchart.com/stocks/quotes/%24VIX/gamma-exposure)  
2. The Trading Review of 2020 That You've Heard About...and the One You Haven't, accessed February 3, 2026, [https://bridgeway.com/perspectives/the-trading-review-of-2020-that-youve-heard-about-and-the-one-you-havent/](https://bridgeway.com/perspectives/the-trading-review-of-2020-that-youve-heard-about-and-the-one-you-havent/)  
3. Disclaimer The information contained in these documents is ... \- sqzme, accessed February 3, 2026, [https://squeezemetrics.com/monitor/download/pdf/white\_paper.pdf](https://squeezemetrics.com/monitor/download/pdf/white_paper.pdf)  
4. GEX Meets Volatility Q-Score Guide \- MenthorQ, accessed February 3, 2026, [https://menthorq.com/guide/gex-meets-volatility-q-score/](https://menthorq.com/guide/gex-meets-volatility-q-score/)  
5. sqzme | Fresh perspectives on stock data, accessed February 3, 2026, [https://squeezemetrics.com/](https://squeezemetrics.com/)  
6. The real danger of 'Gammageddon' \- Trium Capital, accessed February 3, 2026, [https://trium-capital.com/trium-talks/the-real-danger-of-gammageddon/](https://trium-capital.com/trium-talks/the-real-danger-of-gammageddon/)  
7. Impact of option dealer flows on equity returns \- Vol.land, accessed February 3, 2026, [https://vol.land/VollandWhitePaper.pdf](https://vol.land/VollandWhitePaper.pdf)  
8. How to Calculate Gamma Exposure (GEX) and Zero Gamma Level, accessed February 3, 2026, [https://perfiliev.com/blog/how-to-calculate-gamma-exposure-and-zero-gamma-level/](https://perfiliev.com/blog/how-to-calculate-gamma-exposure-and-zero-gamma-level/)  
9. Invesco QQQ Trust Series I Trade Ideas — NASDAQ:QQQ — TradingView, accessed February 3, 2026, [https://www.tradingview.com/symbols/NASDAQ-QQQ/community-ideas/page-27/?sort=recent](https://www.tradingview.com/symbols/NASDAQ-QQQ/community-ideas/page-27/?sort=recent)  
10. Inferring Latent Market Forces: Evaluating LLM Detection of Gamma Exposure Patterns via Obfuscation Testing \- arXiv, accessed February 3, 2026, [https://www.arxiv.org/pdf/2512.17923](https://www.arxiv.org/pdf/2512.17923)  
11. amf \- heightened volatility in early february 2018: the impact of vix products, accessed February 3, 2026, [https://www.amf-france.org/sites/institutionnel/files/contenu\_simple/lettre\_ou\_cahier/risques\_tendances/Heightened%20volatility%20in%20early%20February%202018%20the%20impact%20of%20VIX%20products.pdf](https://www.amf-france.org/sites/institutionnel/files/contenu_simple/lettre_ou_cahier/risques_tendances/Heightened%20volatility%20in%20early%20February%202018%20the%20impact%20of%20VIX%20products.pdf)  
12. Volmageddon and the Failure of Short Volatility Products (Summary) \- CFA Institute Research and Policy Center, accessed February 3, 2026, [https://rpc.cfainstitute.org/research/financial-analysts-journal/2021/volmageddon-failure-short-volatility-products](https://rpc.cfainstitute.org/research/financial-analysts-journal/2021/volmageddon-failure-short-volatility-products)  
13. Volmageddon & the Role of Massive Options Trades Dissected, accessed February 3, 2026, [https://www.barchart.com/story/news/27336349/volmageddon-the-role-of-massive-options-trades-dissected](https://www.barchart.com/story/news/27336349/volmageddon-the-role-of-massive-options-trades-dissected)  
14. Volatility and the Alchemy of Risk \- CAIA, accessed February 3, 2026, [https://caia.org/sites/default/files/03\_volatility\_4-2-18.pdf](https://caia.org/sites/default/files/03_volatility_4-2-18.pdf)  
15. What Explains the COVID-19 Stock Market? \- NBER, accessed February 3, 2026, [https://www.nber.org/system/files/working\_papers/w27784/w27784.pdf](https://www.nber.org/system/files/working_papers/w27784/w27784.pdf)  
16. SpotGamma SPX Key Levels Statistics, accessed February 3, 2026, [https://support.spotgamma.com/hc/en-us/articles/31209900542867-SpotGamma-SPX-Key-Levels-Statistics](https://support.spotgamma.com/hc/en-us/articles/31209900542867-SpotGamma-SPX-Key-Levels-Statistics)  
17. 2020 stock market crash \- Wikipedia, accessed February 3, 2026, [https://en.wikipedia.org/wiki/2020\_stock\_market\_crash](https://en.wikipedia.org/wiki/2020_stock_market_crash)  
18. COVID-19 Effects on the S\&P 500 Index \- FIU Economics, accessed February 3, 2026, [https://economics.fiu.edu/research/pdfs/2021\_working\_papers/21171.pdf](https://economics.fiu.edu/research/pdfs/2021_working_papers/21171.pdf)  
19. COVID-19 and March 2020 Stock Market Crash. Evidence from S\&P1500 \- ResearchGate, accessed February 3, 2026, [https://www.researchgate.net/publication/341340631\_COVID-19\_and\_March\_2020\_Stock\_Market\_Crash\_Evidence\_from\_SP1500](https://www.researchgate.net/publication/341340631_COVID-19_and_March_2020_Stock_Market_Crash_Evidence_from_SP1500)  
20. GameStop short squeeze \- Wikipedia, accessed February 3, 2026, [https://en.wikipedia.org/wiki/GameStop\_short\_squeeze](https://en.wikipedia.org/wiki/GameStop_short_squeeze)  
21. What is the impact of the GameStop short squeeze on rest of the financial market? \- Reddit, accessed February 3, 2026, [https://www.reddit.com/r/UKPersonalFinance/comments/l5z3or/what\_is\_the\_impact\_of\_the\_gamestop\_short\_squeeze/](https://www.reddit.com/r/UKPersonalFinance/comments/l5z3or/what_is_the_impact_of_the_gamestop_short_squeeze/)  
22. The GameStop Episode: What Happened and What Does It Mean? | Cato Institute, accessed February 3, 2026, [https://www.cato.org/cato-journal/fall-2021/gamestop-episode-what-happened-what-does-it-mean](https://www.cato.org/cato-journal/fall-2021/gamestop-episode-what-happened-what-does-it-mean)  
23. Sharing Gamma Exposure Calculator (useful for 0DTE analysis) : r/algotrading \- Reddit, accessed February 3, 2026, [https://www.reddit.com/r/algotrading/comments/1niqfdr/sharing\_gamma\_exposure\_calculator\_useful\_for\_0dte/](https://www.reddit.com/r/algotrading/comments/1niqfdr/sharing_gamma_exposure_calculator_useful_for_0dte/)  
24. Revisiting GameStop's epic 2021 short squeeze: A timeline of notable events (NYSE:GME), accessed February 3, 2026, [https://seekingalpha.com/news/4106226-revisiting-gamestops-epic-2021-short-squeeze-a-timeline-of-notable-events](https://seekingalpha.com/news/4106226-revisiting-gamestops-epic-2021-short-squeeze-a-timeline-of-notable-events)  
25. how Gamestop's shares have skyrocketed 2000% in January 2021 \- Student Work, accessed February 3, 2026, [https://studentwork.prattsi.org/infovis/labs/how-shares-for-gamestop-have-skyrocketed-2000-by-reddit-at-the-beginning-of-2021/](https://studentwork.prattsi.org/infovis/labs/how-shares-for-gamestop-have-skyrocketed-2000-by-reddit-at-the-beginning-of-2021/)  
26. The market turbulence and carry trade unwind of August 2024 \- Bank for International Settlements, accessed February 3, 2026, [https://www.bis.org/publ/bisbull90.pdf](https://www.bis.org/publ/bisbull90.pdf)  
27. The Yen Carry Trade and Its Global Implications Guide \- MenthorQ, accessed February 3, 2026, [https://menthorq.com/guide/the-yen-carry-trade-and-its-global-implications/](https://menthorq.com/guide/the-yen-carry-trade-and-its-global-implications/)  
28. August market volatility and the importance of the Yen | Envestnet, accessed February 3, 2026, [https://www.envestnet.com/financial-intel/august-market-volatility-and-importance-yen](https://www.envestnet.com/financial-intel/august-market-volatility-and-importance-yen)  
29. When Carry Trades Crack: How a Hidden FX Strategy Moves Global Markets | Investing.com, accessed February 3, 2026, [https://www.investing.com/analysis/when-carry-trades-crack-how-a-hidden-fx-strategy-moves-global-markets-200663052](https://www.investing.com/analysis/when-carry-trades-crack-how-a-hidden-fx-strategy-moves-global-markets-200663052)  
30. The SpotGamma Index, accessed February 3, 2026, [https://spotgamma.com/spot-gamma-index/](https://spotgamma.com/spot-gamma-index/)  
31. Convexity in Motion \- Diva-portal.org, accessed February 3, 2026, [https://www.diva-portal.org/smash/get/diva2:1972044/FULLTEXT01.pdf](https://www.diva-portal.org/smash/get/diva2:1972044/FULLTEXT01.pdf)  
32. GEX Ratio Trading Strategy: How to Predict Market Reversals Before Price Action, accessed February 3, 2026, [https://www.gammaedge.us/gex-ratio-trading-strategy-market-reversals/](https://www.gammaedge.us/gex-ratio-trading-strategy-market-reversals/)  
33. GEXStream \- Real-Time Gamma Exposure Analytics for Options Traders, accessed February 3, 2026, [https://gexstream.com/](https://gexstream.com/)  
34. Ratio Put/Call (PCR) — Indicateurs et Stratégies \- TradingView, accessed February 3, 2026, [https://fr.tradingview.com/scripts/putcallratio/](https://fr.tradingview.com/scripts/putcallratio/)  
35. What is Gamma Exposure (GEX)? \- Unusual Whales, accessed February 3, 2026, [https://unusualwhales.com/information/what-is-gamma-exposure-gex](https://unusualwhales.com/information/what-is-gamma-exposure-gex)  
36. Cboe Open-Close Volume Summary \- Cboe DataShop, accessed February 3, 2026, [https://datashop.cboe.com/cboe-options-open-close-volume-summary](https://datashop.cboe.com/cboe-options-open-close-volume-summary)  
37. Gamma Max, Gamma Neutral, Delta Neutral calculations · OpenBB-finance OpenBB · Discussion \#2741 \- GitHub, accessed February 3, 2026, [https://github.com/OpenBB-finance/OpenBBTerminal/discussions/2741](https://github.com/OpenBB-finance/OpenBBTerminal/discussions/2741)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAVCAYAAAB2Wd+JAAAArUlEQVR4XmNgGNnABIpbgZgVTQ4nAClcBcU/gdgSVRo3IFujLRDPhuInQLwciFlQVGABIAV9QKwCxQ0MRNoKUlAJxIxQrMiAaitWm5FtQwYNQPwViI2hGAOQrRHkzBYGiBORAcigZ0A8B4rhzoW5vR2ItWGCSABkUDMDxFaYzWAAc0IjVBE2ADLwNRRPgQmSpRGksBeKq4A4BAcOBeJjUPwepFEHygDh/yTgoQIA36Yz1lShGDMAAAAASUVORK5CYII=>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAVCAYAAACQcBTNAAAAX0lEQVR4XmNgGJpAAIglicDCIMVWQDwPiv8B8UIojgDiLiC+AsUHSFYMAsZQ/BWIfaEYBnigGGQYGOBTDAMJMAYxiqVhDGIUw8GoYhhIB+IbUPwfiJ9CcT8DJJENNgAAQY8pR48DaEEAAAAASUVORK5CYII=>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAAXCAYAAADpwXTaAAAAaklEQVR4XmNgGAWjwA+IBdAFyQVUNSwEiN3RBckF/EBcC6WpAuSBeBIQy0AxRQCrYZJA3AvFs0jAs4H4PpQGYWEGMgEjEBcAcRC6BDlAB4jTGSCGUgxygVgTXZBcQFXDeIGYGV1wFAwwAAA89xDsve3pkAAAAABJRU5ErkJggg==>

[image4]: <data:image/png;base64,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>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAXCAYAAAAcP/9qAAAAyklEQVR4Xu3TwQpBQRgF4F9SxEtY2UlZ2CsLWZCVhYXY2nsPaxuKsuAR5I08gXJO8y9+invnTuLWnPq6i5numWlmRGJiwlKGMWyhpr6avlrDCa7ypngKG9V4GQvNSv6xmKmqOeygowp2UoYkFtuUYKLO0IXi04z08Sq2YeFQ3CXhl3wWkb9ihkU9cT+gth1MiHcxz5lGcICBuAX47JZJXVyBmbhLRaE3+2Mxn9FS7aEprixrYUsd4QZ3uKiFmfebYp4Z32tdxcTkOw+Z/CxprYxYkQAAAABJRU5ErkJggg==>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAXCAYAAAAcP/9qAAAAyklEQVR4XmNgGAWjgDLAAcRBQLwQiHmgmKbAE4onAfFaID7AQKbFzEDszwAxBIR1UaXxgnKGoWIxJxQnAPE6ILZigDgAhEkBRFvMDcR5QLwCivWAmBFFBWkAr8V8QFwFxQuAWB1FljIw+CwGxRnMQhBWRJakAsBpMQyAfA3z+QIGiK+p4XOCFiMDUAJLgmJQijZnID+BkWQxMmAF4gggXgnETlBMKEsZQDFIz3sg/gvE+6A4GUkdXjBgFsMAyDKYxaSUXKNgFNAXAAAlpSytEH/GtQAAAABJRU5ErkJggg==>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAC0AAAAXCAYAAACf+8ZRAAABrklEQVR4Xu3VvytFYRgH8Eco4maxKOXHIik/QhaTKCU/RkWSlMVkMVhuyWA1SGJRyEApFhZls1j4A0iKsii779f7PJzOdV/n3usOp863Pt3be95z7nPOfd73iCRJEqukVGn4QLFTrpbgHI5hTVUG5oVTAafqDnZhO6Tze/Y/Z1IdiSu+BFZV+mdaRmrhRj0GvKpLqLHJ02oHWmwwz/Bp8enScmB8VN2LK+63NMO8svCm11VXYDyeRVuqYA72oE/xr80ldfCgWKSlXz1DR2A8GBbIGsgyBhPKG55sfXkCAxJ9NdfDkwoW3a3Yo/yMkkbYFLd4fQs4Iyx2XNwOwE/y3UArvKlCi07DQngwSmJZNMMih+BK+X40W0/3KraN73wLF+stDIYP+GIvCC6AAxgRV7zvKTMpuFZ8uVhs92DR7Pu/wkX7ItFu8KvhZ8UtQMpnB0mrjcDYojqEMnHXXFFbkrnQpuBDPEXbNsOL7kO7uIvmWqyFLUIXMAPDcKYadA4L59ZKnFet4xb+S++SfXuMX9HsUduTm0LHCg3XRBv06HeKGrYL35D5PrgkSZIUM5/vImBRRN4blAAAAABJRU5ErkJggg==>

[image8]: <data:image/png;base64,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>