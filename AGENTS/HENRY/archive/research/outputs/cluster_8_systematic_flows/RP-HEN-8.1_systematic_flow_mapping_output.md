# **Systematic Flow Mapping and the Architecture of Mechanical Selling: Predicting Cascades in the 2025-2026 Market Regime**

The structural evolution of global financial markets has transitioned from a landscape dominated by discretionary human decision-making to one increasingly governed by systematic, rules-based architectures. As of 31 March 2024, institutional investors managing an estimated $22.3 trillion in assets utilized structured quantitative models and algorithms to inform their investment processes.1 This massive concentration of capital within systematic frameworks—encompassing risk parity, volatility targeting, and Commodity Trading Advisor (CTA) trend-following strategies—has introduced a new dimension of market reflexivity. During periods of relative stability, these strategies provide liquidity and facilitate smooth price discovery. However, when market conditions deteriorate, the mechanical nature of their deleveraging processes can transform these strategies into "forced sellers," exacerbating drawdowns through procyclical feedback loops.2

The 2025 market environment, punctuated by the April "Liberation Day" tariff shock and subsequent technical corrections in February and August, has underscored the importance of systematic flow mapping.5 Understanding the "cascade order"—the sequence in which different systematic cohorts are forced to liquidate positions—is critical for predicting market depth and the severity of drawdowns. By mapping approximate assets under management (AUM) and the technical trigger levels associated with these strategies, market participants can identify the "who breaks first" dynamics that govern modern volatility regimes.9

## **The Systematic Investment Landscape: AUM and Asset Class Proliferation**

The scope of systematic investing expanded significantly between 2023 and 2025, moving beyond traditional liquid equities into more complex multi-asset frameworks. In 2024, approximately 99% of systematic investors applied these strategies to equities, but the application in fixed income reached 88%, while 40% of investors utilized systematic models in real estate and 36% in commodities.1 This expansion suggests that the mechanical selling pressure historically associated with equity market corrections now has the potential to manifest simultaneously across a broad spectrum of asset classes, particularly as strategies seek to manage "overheating" risks and inflationary pressures.11

The growth in assets is not merely a reflection of market appreciation but also of structural shifts in asset allocation. Total worldwide assets managed by the largest money managers rose 9.8% in 2024 to $94.61 trillion, with institutional assets managed globally climbing to $59.74 trillion.13 Within this universe, specific systematic sub-strategies have carved out dominant positions.

### **Table 1: Estimated Global Systematic Strategy AUM and Adoption (2024-2025)**

| Strategy Classification | Estimated Segment AUM | Adoption Rate (Equities) | Adoption Rate (Fixed Income) | Primary Rebalancing Mechanism |
| :---- | :---- | :---- | :---- | :---- |
| Institutional Systematic Investing | $22.3 Trillion 1 | 99% | 88% | Model-Driven 1 |
| Risk Parity Strategies | \~$1.0 Trillion 14 | High | High | Volatility/Correlation 4 |
| Managed Futures (CTA) | $345.36 Billion 15 | Variable | High | Momentum/Trend 16 |
| Volatility-Targeting (ETFs/Annuities) | Multi-Trillion (Aggregated) | High | Moderate | Realized Volatility 18 |

The managed futures industry, specifically CTAs, reported approximately $345.36 billion in AUM by the second quarter of 2025\.15 Within this sector, "Diversified Traders" account for $212.16 billion, while "Currency Traders" manage roughly $30.64 billion.15 These figures represent the pool of capital most sensitive to short-to-medium-term price trends, acting as a primary catalyst for mechanical selling when technical levels are breached.7

## **The Mechanics of Volatility Targeting and Portfolio Deleveraging**

Volatility targeting is a foundational tool in modern portfolio management, aimed at maintaining a constant risk profile by adjusting leverage inversely to predicted or realized volatility.18 The logic is rooted in the empirical observation that while returns are difficult to forecast, volatility tends to cluster, making it relatively predictable over short horizons.20

The general formula for determining the exposure of a volatility-managed portfolio is expressed as:

![][image1]  
Where ![][image2] is the annualized volatility target (commonly 10% or 12%) and ![][image3] is the expected or realized volatility estimated over a specific look-back window.18 When market volatility is low, these strategies often utilize leverage to increase exposure above 100% of net asset value (NAV) to meet their return and risk targets.20 Conversely, a spike in realized volatility forces a rapid reduction in exposure to stabilize the portfolio's risk contribution.4

### **Look-Back Windows and Signal Sensitivity**

The speed of the mechanical response is determined by the length of the look-back window used to calculate ![][image3]. Industry standards typically oscillate between 20-day and 60-day windows, though "fast" models may use 5-day or 10-day metrics to respond to sudden shocks.20 In 2025, the discrepancy between these windows created a multi-stage deleveraging process. During the August 2025 period, 10-day realized volatility sat at 8.47, whereas 30-day volatility was 9.54 and 3-month (approx. 60-day) volatility remained significantly elevated at 26.64.8 This "lag" ensures that even if a market stabilizes, the mechanical selling pressure from longer-term models can persist for weeks as high-volatility data points remain within the calculation window.8

### **Table 2: Volatility Targeting Thresholds and Signal Lag Impacts**

| Look-Back Window | Strategy Tier | Typical Response Speed | 2025 Market Impact |
| :---- | :---- | :---- | :---- |
| 10-Day Realized | Vol-Control / Fast CTA | Intraday to T+2 | Triggered 20% exposure cut in Nov 2025 10 |
| 20-Day Realized | Standard Vol-Targeting | T+2 to T+5 | "Thins the tails" of return distributions 20 |
| 60-Day Realized | Institutional Risk Parity | Monthly/Quarterly | Lagged selling during April tariff shock 5 |

## **Risk Parity: Diversification and the Correlation Breakdown**

Risk parity strategies extend the principles of volatility targeting by equalizing the risk contribution across different asset classes, such as equities, bonds, credit, and commodities.23 A traditional 60/40 portfolio is often dominated by equity risk; risk parity addresses this imbalance by over-weighting lower-volatility assets (like bonds) and using leverage to achieve the desired expected return.28

### **The Role of Cross-Asset Correlation**

The effectiveness of risk parity is predicated on the assumption of "well-behaved" or normal markets where asset classes exhibit negative or low correlations.28 Historically, the negative correlation between U.S. equities and 10-year Treasury yields has allowed bonds to act as a natural hedge during equity drawdowns.14 However, the 2020s—and specifically the period leading into May 2025—have seen a shift toward positive correlations, particularly during inflationary regimes.11

When correlations between equities and bonds turn positive, the diversification benefit vanishes. In such an environment, a spike in volatility across both asset classes causes the portfolio's total risk to climb exponentially, triggering a "strict risk parity rule" for massive unwinding.4 During the March 2020 downturn and the April 2025 tariff shock, stylized models suggest that risk parity investors were required to sell assets worth up to 225% of the portfolio's capital to maintain an 8% annualized volatility target.4 Notably, this selling pressure extends to "safer" sovereign and higher-rated corporate bonds, potentially intensifying broader market liquidity stress.4

### **Enhanced Risk Parity and the CTA "Risk-Off" Sleeve**

To address these vulnerabilities, institutional managers in 2024 and 2025 increasingly adopted "Enhanced Risk Parity" models. These frameworks integrate a fifth sleeve: the "CTA Risk-Off" overlay.27 This component utilizes time-series momentum signals to provide a systematic hedge that loads negatively on procyclical risk exposures during adverse conditions.27 Operationally, this sleeve trades a diversified set of futures—including S\&P 500, Bund, and WTI crude—and nets positions with other sleeves before execution to ensure efficient order flow.27

## **The CTA Trend-Following Ecosystem: Signals and Triggers**

CTAs and managed futures programs operate on the principle of market persistence, utilizing quantitative rules for entry and exit based on historical price trends.17 Unlike risk parity, which is risk-focused, CTAs are primarily signal-focused, taking long or short positions as price action deviates from moving averages or other technical indicators.17

### **Performance and Constituent Dynamics (2025)**

The performance of CTAs in 2025 was marked by significant volatility. The SG Trend Index, which tracks the 10 largest institutional CTAs, gained 2.74% in August 2025 but remained down 7.56% year-to-date.32 The constituents of the SG Trend Index for 2025 include major programs such as Man AHL (Evolution, Alpha, and Dimension), Winton Capital Management (re-entering the index in 2025), and Mulvaney Capital Management.32

### **Table 3: Managed Futures Industry Performance Metrics (August 2025\)**

| Index | August 2025 Return | Year-to-Date (YTD) | 12-Month Trailing |
| :---- | :---- | :---- | :---- |
| SG Trend Index | \+2.74% | \-7.56% | \-6.38% 32 |
| TTU TF Index | \+2.31% | \-9.01% | \-9.82% 32 |
| BTOP50 Index | \+1.29% | \-2.94% | \-0.53% 32 |
| Barclay CTA Index | \+2.41% (Sept) | \+0.31% (Sept) | N/A 16 |

The "BTOP50 Index," which seeks to replicate the overall managed futures industry, historically delivers a smoother return profile with a compound annual growth rate (CAGR) of 3.90% and a maximum drawdown of 15.94%.32 In contrast, pure trend-following indices like the SG Trend Index exhibit more convex payoff profiles but are prone to sharp reversals when V-shaped market turns occur, as seen during the 2025 tariff announcements.5

## **Flow Mapping: The Cascade of Forced Selling**

The core value of systematic flow mapping lies in predicting the "cascade order" during a market drawdown. This sequence is governed by the reactivity of the underlying strategies and their specific technical trigger levels.9

### **The "Who Breaks First" Sequence**

1. **Fast Volatility-Control Funds**: These strategies respond almost immediately to spikes in realized volatility. By November 2025, models targeting 10% volatility had already reduced exposure by over 20% following early-month turbulence.10  
2. **Short-Term CTAs**: Using short-lookback momentum signals, these funds are the second to liquidate. They often "flip" from long to short within days of a trend reversal.7  
3. **Medium-Term CTAs and Trend Followers**: This cohort represents the "heavy" capital. Their liquidation triggers are typically tied to 50-day and 200-day moving averages or mid-term Bayesian graphical decoders.5  
4. **Risk Parity and Strategic Multi-Asset Funds**: These strategies rebalance on longer horizons (monthly or quarterly) and respond to the convergence of cross-asset correlations. They are often the final sellers in a cascade but do so in massive size.4

### **Critical Trigger Levels (2025)**

In 2025, market strategists monitored specific price levels in the S\&P 500 (SPX) and Nasdaq 100 (NDX) that functioned as mechanical liquidation thresholds. In February 2025, the S\&P 500 fell below the critical mid-term CTA liquidation trigger of 5887, closing at 5861.57.7 This breach triggered an estimated $12.6 billion in selling over the subsequent week, with a potential for $58 billion in liquidations over the following month if momentum failed to recover.7

### **Table 4: Systematic Liquidation Triggers and Flow Estimates (2025)**

| Period | Asset/Index | Trigger Level (Approx.) | Spot Level (at Breach/Warning) | Estimated Flow Potential |
| :---- | :---- | :---- | :---- | :---- |
| February 2025 | S\&P 500 (ES1) | 5887 7 | 5861.57 | $40B \- $60B (Selling) 7 |
| August 2025 | S\&P 500 (ES1) | 6003 8 | 6280 | "Buffer" Zone 8 |
| August 2025 | Nasdaq 100 (NQA) | 21861 8 | 23006 | "Buffer" Zone 8 |
| October 2025 | S\&P 500 (SPX) | 6494 9 | \~6500 | Critical Threshold 9 |

By October 2025, the "big medium-term threshold" for CTAs to flip from long to short was identified at 6494\.9 As spot prices hovered near these levels, the market entered a "full but fragile" positioning phase where any additional downside would accelerate mechanical selling.9

## **Case Study: The April 2025 "Liberation Day" Shock**

The "Liberation Day" tariff announcements in April 2025 provided a definitive stress test for systematic liquidity. Over a four-day trading period, the S\&P 500 fell by 12.1%—the fifth-largest such decline since 1990\.5

### **Why Trend Following Failed to Protect**

Trend-following CTAs, often heralded for their "convex" payoff during crises, failed to provide downside mitigation during this episode, with the SG Trend Index declining 6.1% during the shock.5 The failure was attributed to three factors:

* **Trend Horizon Mismatch**: The models analyzed typically utilized a half-life of one calendar quarter. The 12.1% drop was too rapid for medium-term signals to adjust, leaving CTAs positioned long into a precipitous reversal.5  
* **Broad-Based Detraction**: Commodity sectors, particularly precious and base metals, contributed approximately 3.5% to the total loss, as gold and other traditional diversifiers dropped in tandem with equities.5  
* **V-Shaped Market Reversal**: Large trend followers struggled with sharp reversals triggered by macroeconomic policy shocks, marking their worst performance for any equity sell-off exceeding \-9% in a four-day span.5

## **The Role of Option Gamma and Dealer Hedging Dynamics**

Systematic flows are further amplified by the hedging activities of options dealers. In February 2025, over $2.7 trillion in nominal options expired in a single day, including $1.2 trillion in SPX options.34 The positioning of these options determines whether dealers act as a volatility buffer or a volatility catalyst.

### **Gamma as a Buffer and Accelerator**

When traders are long options, dealers are "long gamma," requiring them to buy futures into market weakness and sell into strength to remain delta-neutral.34 In early 2025, dealers held approximately $9.8 billion in long gamma positions on the S\&P 500, which served to dampen volatility.34 However, if systematic selling pushes the market below critical "gamma flip" levels, dealers become "short gamma," forced to sell into a falling market to manage their risk.10 This transition from a buffer to an accelerator often occurs simultaneously with CTA trigger breaches, creating the "mechanical selling cascade" that leads to technical corrections.10

## **Counter-Cyclical Buffers: Retail Demand and Corporate Buybacks**

The 2025-2026 market regime is characterized by a unique tug-of-war between institutional systematic fragility and resilient retail and corporate demand.

### **Retail Resilience: The "Under 40" Cohort**

Retail flows reached record gross activity levels in 2025, with retail investors acting as net buyers in 23 out of 26 weeks leading into October.9 A structural change has occurred in the composition of retail investors; households under 40 years old have increased their equity holdings by 300% since 2020, and the "final 50%" of households by net worth saw a 542% increase.9 This group, characterized by a lack of bear-market memories and a strong "buy-the-dip" mentality, provided the essential liquidity to absorb systematic outflows during the April and August corrections.9

### **Corporate Buyback Demand**

Corporate demand remains a powerful counter-cyclical force. In 2025, U.S. corporate authorizations reached $1.3 trillion for the Russell 3000, with projections reaching $1.5 trillion by year-end.9 This translates to roughly $5.3 billion in daily "VWAP" execution demand.9 While buybacks pause during "blackout windows" (peaks occurring in late October), they historically fill authorizations by year-end, providing a fundamental floor to prices even as mechanical funds de-risk.9

### **Table 5: Market Liquidity Buffers and Seasonal Flows (Late 2025\)**

| Liquidity Source | Current Demand Status (Q4 2025\) | Seasonal Outlook | Stability Role |
| :---- | :---- | :---- | :---- |
| Retail Cash Equities | Net Buyers (24+ week streak) | Strong Nov-Dec | Absorb systematic selling 9 |
| Corporate Buybacks | Blackout Peak (Late Oct) | Peak Execution (Nov-Dec) | Floor for technical drawdowns 9 |
| Institutional Flows | De-risking/Hedging | "Exhausted" by March | Source of volatility 10 |
| Systematic Positioning | "Full but Fragile" | Re-levering potential | Catalyst for cascades 9 |

## **2026 Outlook: Dispersion, AI Capex, and Strategy Evolution**

As the market transitions into 2026, the systematic landscape is expected to shift from a "casino" environment—where almost any risk was rewarded between 2020 and 2024—to an "investor's market" characterized by rising dispersion.38

### **From Scarcity to Selection**

The return to a higher cost of capital is re-introducing dispersion across sectors, balance sheets, and countries.38 In 2025, roughly 40% of the S\&P 500 was heading for a negative year despite strong index-level gains.38 This dispersion is a double-edged sword for systematic strategies:

* **Alpha Opportunities**: Global macro and multi-strategy platforms are expected to thrive in 2026 as they hunt for alpha that purely quantitative approaches cannot easily access.39  
* **Fragility in Concentration**: S\&P 500 concentration remains extreme, with $0.35 of every SPY dollar flowing into the "Magnificent Seven".37 This concentration heightens "factor fragility," where a technical break in a single sector (e.g., AI/Technology) can trigger a broad-market systematic cascade.10

### **The AI Build-Out and Credit Divergence**

A significant theme for 2026 is the "AI Big Build-Out," with an estimated $4 trillion set to be invested in AI capacity and data centers by 2030\.40 Asset managers are increasingly providing the financing (debt and equity) for these off-balance-sheet infrastructure projects.40 However, this concentration of capital into hyperscale data centers poses risks of overspending and overcapacity, creating new systematic triggers within private credit and alternative asset classes.38

## **Conclusion: Synthesizing Systematic Risk and Flow Dynamics**

The research and performance data from 2024 and 2025 confirm that systematic investment strategies have become the primary drivers of short-term market volatility and liquidity dynamics. The "feedback loop" mechanism, where realized volatility triggers mechanical selling, is no longer a theoretical risk but a documented reality, as evidenced by the $40 billion CTA liquidation event in February 2025 and the SG Trend Index's 6.1% drop during the April shock.3

Predicting the next market cascade requires a disciplined approach to flow mapping: identifying the reactivity of fast vol-control funds, monitoring the 50-day and 200-day moving average triggers for CTAs (such as the 6494 level in SPX), and assessing the cross-asset correlation regimes that dictate risk parity deleveraging.4 While resilient retail demand and record corporate buybacks provide a significant buffer, the "full but fragile" nature of institutional positioning means that any sudden, non-fundamental shock can trigger a cascade that temporarily overwhelms the market's liquidity "center book".9

As we enter 2026, the integration of "macro-aware" signals and CTA "Risk-Off" sleeves into traditional systematic frameworks represents a necessary evolution. For practitioners, the priority must shift from simple volatility targeting to a more nuanced understanding of the causal relationships between macroeconomic policy shifts, technical trigger levels, and the mechanical behavior of the $22 trillion systematic universe.1

#### **Works cited**

1. Invesco Global Systematic Investing Study 2024, accessed February 3, 2026, [https://www.invesco.com/content/dam/invesco/apac/en/pdf/insights/2024/october/invesco-igsis-oct-2024.pdf](https://www.invesco.com/content/dam/invesco/apac/en/pdf/insights/2024/october/invesco-igsis-oct-2024.pdf)  
2. Systematic investment strategies: momentum vs mayhem \- keep calm & be systematic, accessed February 3, 2026, [https://globalmarkets.cib.bnpparibas/systematic-investment-strategies/](https://globalmarkets.cib.bnpparibas/systematic-investment-strategies/)  
3. Risk Parity and Volatility Targeting as a Danger \- Let's Get Real with Some Numbers \- IASG, accessed February 3, 2026, [https://www.iasg.com/blog/2017/08/11/risk-parity-volatility-targeting-danger-lets-get-real-numbers](https://www.iasg.com/blog/2017/08/11/risk-parity-volatility-targeting-danger-lets-get-real-numbers)  
4. Volatility-targeting strategies and the market sell-off \- European Central Bank, accessed February 3, 2026, [https://www.ecb.europa.eu/press/financial-stability-publications/fsr/focus/2020/html/ecb.fsrbox202005\_02\~f6616db9be.en.html](https://www.ecb.europa.eu/press/financial-stability-publications/fsr/focus/2020/html/ecb.fsrbox202005_02~f6616db9be.en.html)  
5. Quantica Capital \- Quarterly Insights, accessed February 3, 2026, [https://quantica-capital.com/publications/pdf/2025Q2\_QuanticaQuarterlyInsights.pdf](https://quantica-capital.com/publications/pdf/2025Q2_QuanticaQuarterlyInsights.pdf)  
6. Q4 2025 Market Observations | MONTAG Wealth Management, accessed February 3, 2026, [https://montagwealthmanagement.com/q4-2025-market-observations/](https://montagwealthmanagement.com/q4-2025-market-observations/)  
7. U.S. stocks plunge, panic selling will trigger the first $40 billion in CTA liquidations \- Binance, accessed February 3, 2026, [https://www.binance.com/en/square/post/20893132825386](https://www.binance.com/en/square/post/20893132825386)  
8. August Views \- Citadel Securities, accessed February 3, 2026, [https://www.citadelsecurities.com/news-and-insights/global-market-intelligence-gmi-august-views/](https://www.citadelsecurities.com/news-and-insights/global-market-intelligence-gmi-august-views/)  
9. Equity FLASH Update \- Citadel Securities, accessed February 3, 2026, [https://www.citadelsecurities.com/news-and-insights/equity-flash-update/](https://www.citadelsecurities.com/news-and-insights/equity-flash-update/)  
10. Equity Snapshot \- Citadel Securities, accessed February 3, 2026, [https://www.citadelsecurities.com/news-and-insights/equity-snapshot/](https://www.citadelsecurities.com/news-and-insights/equity-snapshot/)  
11. Macro-aware risk parity | Macrosynergy, accessed February 3, 2026, [https://macrosynergy.com/research/macro-aware-risk-parity/](https://macrosynergy.com/research/macro-aware-risk-parity/)  
12. Nomura Issues Report on Avoided Emissions from Investor Perspective | News Releases | Media Room, accessed February 3, 2026, [https://www.nomuraholdings.com/en/news/nr/news20250501102966.html](https://www.nomuraholdings.com/en/news/nr/news20250501102966.html)  
13. THE LARGEST MONEY MANAGERS 2025 \- Research Center, accessed February 3, 2026, [https://researchcenter.pionline.com/uploads/datastore/moneymanager/moneymanager-special-report-1750338524.pdf](https://researchcenter.pionline.com/uploads/datastore/moneymanager/moneymanager-special-report-1750338524.pdf)  
14. Stress-Testing Risk-Parity Strategies \- MSCI, accessed February 3, 2026, [https://www.msci.com/research-and-insights/blog-post/stress-testing-risk-parity-strategies](https://www.msci.com/research-and-insights/blog-post/stress-testing-risk-parity-strategies)  
15. CTA Industry Assets Under Management \- ION Analytics, accessed February 3, 2026, [https://ionanalytics.com/barclayhedge/solutions/assets-under-management/cta-industry-assets-under-management/](https://ionanalytics.com/barclayhedge/solutions/assets-under-management/cta-industry-assets-under-management/)  
16. CTAs Into the Black for 2025 After Strong September \- The Full FX, accessed February 3, 2026, [https://thefullfx.com/ctas-into-the-black-for-2025-after-strong-september/](https://thefullfx.com/ctas-into-the-black-for-2025-after-strong-september/)  
17. Trend-Following CTAs vs Alternative Risk-Premia \- The Hedge Fund Journal, accessed February 3, 2026, [https://thehedgefundjournal.com/trend-following-ctas-vs-alternative-risk-premia/](https://thehedgefundjournal.com/trend-following-ctas-vs-alternative-risk-premia/)  
18. Harnessing Volatility Targeting in Multi-Asset Portfolios \- Research Affiliates, accessed February 3, 2026, [https://www.researchaffiliates.com/content/dam/ra/publications/pdf/1014-harnessing-volatility-targeting.pdf](https://www.researchaffiliates.com/content/dam/ra/publications/pdf/1014-harnessing-volatility-targeting.pdf)  
19. Volatility ETFs \- ETF Database, accessed February 3, 2026, [https://etfdb.com/etfdb-category/volatility/](https://etfdb.com/etfdb-category/volatility/)  
20. The point of volatility targeting | Macrosynergy, accessed February 3, 2026, [https://macrosynergy.com/research/the-point-of-volatility-targeting/](https://macrosynergy.com/research/the-point-of-volatility-targeting/)  
21. Harnessing Volatility Targeting in Multi-Asset Portfolios \- Research Affiliates, accessed February 3, 2026, [https://www.researchaffiliates.com/publications/articles/1014-harnessing-volatility-targeting](https://www.researchaffiliates.com/publications/articles/1014-harnessing-volatility-targeting)  
22. Volatility Targeting Improves Risk-Adjusted Returns \- \- Alpha Architect, accessed February 3, 2026, [https://alphaarchitect.com/volatility-targeting-improves-risk-adjusted-returns/](https://alphaarchitect.com/volatility-targeting-improves-risk-adjusted-returns/)  
23. Editor's Letter | CAIA, accessed February 3, 2026, [https://caia.org/sites/default/files/editorsletter.pdf](https://caia.org/sites/default/files/editorsletter.pdf)  
24. MSCI World 12% Volatility Target Select Index Methodology, accessed February 3, 2026, [https://www.msci.com/documents/10199/2a6a8d3b-ca0d-af9c-02dc-2914b2b72608](https://www.msci.com/documents/10199/2a6a8d3b-ca0d-af9c-02dc-2914b2b72608)  
25. Figure 1.21. Leveraged and Volatility-Targeting Strategies, accessed February 3, 2026, [https://www.imf.org/-/media/files/publications/gfsr/2017/october/chapter-1/pdf-data/figure1-21.pdf](https://www.imf.org/-/media/files/publications/gfsr/2017/october/chapter-1/pdf-data/figure1-21.pdf)  
26. An Introduction to Volatility Targeting \- QuantPedia, accessed February 3, 2026, [https://quantpedia.com/an-introduction-to-volatility-targeting/](https://quantpedia.com/an-introduction-to-volatility-targeting/)  
27. Ai For Alpha \- Ai-powered investment decision, accessed February 3, 2026, [https://aiforalpha.com/dist/img/Strategy\_Spotlight\_\_\_Risk\_Parity\_v2.pdf](https://aiforalpha.com/dist/img/Strategy_Spotlight___Risk_Parity_v2.pdf)  
28. Risk Parity Trading Strategies: A Complete Guide 2024, accessed February 3, 2026, [https://tradewiththepros.com/risk-parity-trading-strategies/](https://tradewiththepros.com/risk-parity-trading-strategies/)  
29. Understanding Risk Parity \- AQR Capital Management, accessed February 3, 2026, [https://www.aqr.com/-/media/AQR/Documents/Insights/White-Papers/Understanding-Risk-Parity.pdf](https://www.aqr.com/-/media/AQR/Documents/Insights/White-Papers/Understanding-Risk-Parity.pdf)  
30. Risk Parity: A Primer \- Callan, accessed February 3, 2026, [https://www.callan.com/blog/risk-parity-primer/](https://www.callan.com/blog/risk-parity-primer/)  
31. An Introduction to Tail Risk Parity \- AllianceBernstein, accessed February 3, 2026, [https://www.alliancebernstein.com/research-publications/cma-created-content/investments\_us/instrumentation/anewversionofriskparity.pdf](https://www.alliancebernstein.com/research-publications/cma-created-content/investments_us/instrumentation/anewversionofriskparity.pdf)  
32. Trend Following Performance Report — August, 2025 | Top Traders Unplugged, accessed February 3, 2026, [https://www.toptradersunplugged.com/trend-following-performance-report-august-2025/](https://www.toptradersunplugged.com/trend-following-performance-report-august-2025/)  
33. CTA Hedge Fund Report \- With Intelligence, accessed February 3, 2026, [https://www.withintelligence.com/insights/cta-hedge-fund-report/](https://www.withintelligence.com/insights/cta-hedge-fund-report/)  
34. Goldman Sachs Flow Master: Weakened capital flows, U.S. stock market will correct, accessed February 3, 2026, [https://www.binance.com/en/square/post/20596560423721](https://www.binance.com/en/square/post/20596560423721)  
35. The Wall Street boss who accurately predicted the “summer sell-off” made a big statement: retail investors in the US are fanatical about buying or temporarily suspended in September \- Webull.ca, accessed February 3, 2026, [https://www.webull.ca/news-detail/13365426669970432](https://www.webull.ca/news-detail/13365426669970432)  
36. Rules and Tools \- Citadel Securities, accessed February 3, 2026, [https://www.citadelsecurities.com/news-and-insights/rules-and-tools/](https://www.citadelsecurities.com/news-and-insights/rules-and-tools/)  
37. “What's the RUB?” \- Citadel Securities, accessed February 3, 2026, [https://www.citadelsecurities.com/news-and-insights/whats-the-rub/](https://www.citadelsecurities.com/news-and-insights/whats-the-rub/)  
38. The Odds Are Changing: Investing in 2026 \- BlackRock, accessed February 3, 2026, [https://www.blackrock.com/us/financial-professionals/insights/investing-in-2026](https://www.blackrock.com/us/financial-professionals/insights/investing-in-2026)  
39. Hedge Fund Outlook 2026 \- With Intelligence, accessed February 3, 2026, [https://www.withintelligence.com/insights/hedge-fund-outlook-2026/](https://www.withintelligence.com/insights/hedge-fund-outlook-2026/)  
40. Global Asset Manager Sector View 2026: Partnerships Propel Growth While Adding Complexity, accessed February 3, 2026, [https://www.spglobal.com/ratings/en/regulatory/article/global-asset-manager-sector-view-2026-partnerships-propel-growth-while-adding-complexity-s101662130](https://www.spglobal.com/ratings/en/regulatory/article/global-asset-manager-sector-view-2026-partnerships-propel-growth-while-adding-complexity-s101662130)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAAqCAYAAAAOCwd9AAAE3klEQVR4Xu3dWahvYxjH8Uco85A5jjkyhQwXphIXJBJOmZKUIYkiY+QUkoyZMyRKxkiOIVwcQ3KhUMgFF67kyhV34vn2vG9r7X22vdU+tfY+5/upX3v913/9h/2/enqf931XhCRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkqRlaePMeaMcNPNpSZIkTWmPzGeZ1Zl/Mh9lTppxhSRJkiZzWua7zC7t8YuZm4enY7PR8WJsmtly9klJkiQtjOLs5cxGme0zX0YVcd31o+PFOD1z6+yTkiRJWtiVUaNquDjzTmbzqBGxUzIfRo2MUdAdnjmyHe+WOa5dw7WgjXpEZot2jscntOsoCu9u10mSJM2LQmOuMOl+Q0UBtsPsk1HF1n2ZQ6MKLgq5s6J+q92jCr3eMuU8GEVjNO2DzE2Z8zP7Zp6NdddelSRJ67mXMn9nXslclHk0831UO1Az0Q49J6rouqeduz2zT9Qq0qfaOdBapSCjMKNAO7Odpxjs7VCKPEmSpAXRAvwtqqjoWCXphPi13ZK5OrMiqlBbmXk76veikOO37GiX3ha10pTf8sbM8Zkrogo+3uvSfrEkSdJ8fohhtOjeqNWRtPq6A6OKjB2jRoV6IcfcrQMyB0eNyl3QzmObzDOZC2N4L/7ymOv6HC8+9+yoUSfe/9h2zOdc3s6NP5O/zCvjvft7LEU7Zz7OPB5VzEmSJC3Kn5k1UUXQ65lNRs8xSnRd1LwttrpgtSTtPAqSVZm/okaJeA3FHo6OWllJ4XVX5pH2/AOZMzLvZk6NmiPGnLBvM3tFFW/PRTk582nm/cyvMazS/DFqwj74HvNhHt6DUf/XXBn/n5IkSUtab4dSYPUtK3oxQ/uP4owRNLJfDKshKbreHF1L+48RNwo72oNg3hYjeLyGv+dmbsjsFFWU0RqkuNs280nUHDpWVFIo/hxV0NF65Hm+xzVROD6kHa/r/cwYTZwikiRJc6Ll2Nuh3f6Zh9oxk+YJxVa/NVNfPcqEeQqqfvxL1CrJXsTxuvei2oK0Omm1UvB9E8MKzJ9ieA8WOnDN1lHfqe+F1l0W9X07nptvewyKuvtj7ZG1ng15FawkSVpGjomZrUXmnr0Q1YJkVOurzNOZz6MKKc5t1a5lhK3Pz2JeGXO2xpvOnpj5Oqrd+UcMn/N8DKNytEN5D67ndbRTmeNGoTeewA8+b7xylf3O9sy8mjlsdF6SJGm9sF3myczvUaNcFFGvRW3vsSaqKCNvRY1esVksc9keiwHF2cNRbdQ3MrtGtT4ptmh7Mldt73Ytc+OuylwbVcB1rLBkFOyOzBftmAKOQu6o0XWg9cl8ONqoT0SNkLmfmSRJ0n+gBUqbdGpLYXsMVr8yb68vhpAkSZoc23iwQIA5axxPbcrRNVq7LLZg0QOjg30hhCRJkiRJkqT/gxu70xpmUQbz/5iT11fTSpIkaWIsjmCLElbUMo+NhRn9fqFgVa0kSZImxCa+FGkUa6yoXRNDwcacNrZHkSRJ0oS48wNbm6Dfgov95FgEcUnmzvacJEmSJsJ+cqujbivFDerHN6NfFbXRryRJkibG5r3j22Wht0NXzDovSZKkJYT92frttyRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkqTl618DPa/4K1jW+wAAAABJRU5ErkJggg==>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADEAAAAYCAYAAABTPxXiAAACAUlEQVR4Xu3Wy0uUURgG8Fe84BVLQxEVVEoIvBShCxXxtsiFEVrQIqJcKIiIKHYRwUFwIW5EBPECoiAoLiQQytyEgnv/Inse3vfwncYRhilmhuF74Mc457uec95zHJEwYcKECRMm/mRDF7yJ4al3XlqmxlzCbziDW/MLtqHbnZyOKYZzMwlZZsN8CU5N37yEG1Ppte+bWJ0oES29ZCff3ElGdIIveWhYRsxDuDbspEuR2RNdQ8nODAxHNzLjEoy6y3v4bgqs7RF8MlfQJ8H6oVZ4DqVeWxV0QCP0m1zR8JObBT2DQq/dHeNOyZF31/6EKdGB/Ct86LGZhSVYl2DUXXizD2YRHoi+KDcD6oFeOBDdLGgEdmEMTgy3ah7jpvHEfIRl0U7zenoMA9AGzeYI6uSeUnYjVy731JwlYnhzpkmCUuSMvYI50YdQtegMcxb9euZ5a/Y38w0GRUv7h/kM70RnhTNCK+6CWMmITsQTt6CpFl7AkGgZELMAr6HesHQ2IceOu/BluUBdx3agQbSMeU9iOLAcDC5ot6hZfizlhMK1s2VGoUV0h+KL01s4hWlrJz6UG0d0uAmswrzhLwQOUrvoTFKn6Foqg69mQvQ57FzC4Yg68YSjGP1AfucWzmMsS4p4x93ulOe1uXL321KaCrgQnSH30yYV/3P+KRnRif+eP6b9Xpx2yI8LAAAAAElFTkSuQmCC>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAXCAYAAADtNKTnAAAA+ElEQVR4Xt3TvY4BURjG8SNIfIaEkqglYgvdliJCo0ErIRKJkkKisY24BaqVuAKJuACUW2zhPtyC5515Tnwua0zDP/k1Z07OzDkzo9Tb54YoWcoJXdjQ5+nl/9WEKvhoBKmTGS+VH/JQOVMEL/1Zkn5hDlvawRQGEKCrRWBFBY7F6EeZi9/NlkVKsCS9Z72IbO+DY8cFlflNCaMeDEmXI3m60NG4JIf/rQ43MupAnyT57MdU1pPU4Veowxqy5JCLCVhQG2bQImMC81BNmW8rTEa2LCLpQ5LHle3c6kuZ52UpOVB9qHHI0EPJWxITaECaLOWip7JlkYv2KnMpo046J2UAAAAASUVORK5CYII=>