# **Technical Breadth & Internal Market Health: A Quantitative Research Report**

## **Executive Summary**

The structural integrity of the United States equity market as of early February 2026 is defined by a significant divergence between price-level resilience and deteriorating internal participation. While the S\&P 500 and Dow Jones Industrial Average continue to navigate near all-time highs of approximately 6,900 and 49,000 respectively, the technical "engine room" reveals a multi-speed market where cyclical sectors are attempting to offset a pronounced exhaustion in the technology-driven leadership that dominated the 2024–2025 period.1

The primary breadth indicators, specifically the NYSE Advance-Decline (A-D) Line and the McClellan Summation Index, remain in long-term bullish configurations following a confirmed "unofficial" Zweig Breadth Thrust in late November 2025\.3 This thrust historically carries a 100% success rate for positive returns on a six-to-twelve-month horizon.5 However, the tactical environment has become increasingly fragile. The nomination of Kevin Warsh as Federal Reserve Chair in late January 2026 has introduced a hawkish volatility regime, characterized by a sharp rotation out of valuation-sensitive technology stocks—where only 45.7% of components remain above their 50-day moving averages—and into real-economy sectors like Energy and Materials, which currently exhibit participation rates exceeding 95%.1

Internal rot is further evidenced by a widening Z-score in the QQQ/QQQE ratio, signaling that mega-cap concentration is re-emerging as a defensive mechanism while the broader Nasdaq composite lags.3 Current breadth scores sit at 68/100, down from a December peak of 76, reflecting a transition from an aggressive expansion phase into a period of heavy rotation and distribution.3 This report provides an exhaustive quantitative assessment of these internals, utilizing historical analogs from 2000, 2007, and 2022 to contextualize the current market's structural risk.

## **1\. Advance-Decline Line Analysis**

### **Theoretical Foundation and Calculation**

The NYSE Advance-Decline (A-D) Line is the foundational metric of market breadth, serving as a cumulative measure of net participation. Unlike price-weighted or cap-weighted indices, the A-D line treats every listed security as an equal unit, providing a transparent view of the "average" stock's behavior.9 The mathematical construction is a simple recursive summation of the daily difference between advancing and declining issues:

![][image1]  
In this formula, ![][image2] represents the number of stocks that closed higher than their previous session's close, and ![][image3] represents the number of stocks that closed lower.10 Securities that close unchanged are excluded from the daily delta but remain part of the total issues traded, a figure that has been notably declining in recent years.12 The value of the A-D line is not its absolute level, but rather its slope and its correlation—or lack thereof—with the price trend of major indices like the S\&P 500 or the NYSE Composite.9

### **Historical Divergences and the Lead-Time Phenomenon**

The predictive utility of the A-D line is most potent when it diverges from price action during the terminal phase of a bull market. These "bearish divergences" occur when price indices reach new highs while the A-D line forms lower highs, signaling that the rally is being sustained by a dwindling number of stocks while the majority are quietly declining.9

| Epoch | A-D Line Peak | Price Index Peak | Lead Time | Market Correction Outcome |
| :---- | :---- | :---- | :---- | :---- |
| **Dotcom Bubble** | March 1998 | March 2000 | 24 Months | \-50% S\&P 500 Decline 13 |
| **GFC Pre-Crash** | June 2007 | October 2007 | 4 Months | \-56% S\&P 500 Decline 14 |
| **Taper Tantrum** | Early 2018 | Late 2018 | 5 Months | Sharp Q4 2018 Sell-off 11 |
| **2022 Bear Market** | June 2021 | January 2022 | 7 Months | \-25% S\&P 500 Decline 11 |

In the 1998–2000 instance, the divergence was extreme. While the S\&P 500 marched higher for two years, the average NYSE stock peaked in early 1998, reflecting the massive concentration in early internet and telecommunications giants. By the time the price index peaked in March 2000, the underlying breadth was already in a confirmed bear market.13

The 2007 divergence followed a similar pattern but with a shorter duration. The NYSE A-D line peaked in early June 2007, whereas the NYSE Composite and the S\&P 500 pushed to final new highs in October 2007\.15 Technical analysts frequently cite the "dual divergence" of October 2007, where the A-D line failed to exceed its July high and then formed a lower high within the month of October itself, as the definitive signal of the Great Financial Crisis.15

In the current cycle, the A-D line reached a new all-time high alongside the indices in December 2025 and January 2026\.16 While some researchers noted stagnation in late 2024 and early 2025—similar to the lead-up to the 2022 correction—the recent "breadth thrust" has reset the cumulative line to a healthy trajectory, suggesting that a major multi-year peak is not yet in place.4

### **Calculation of "New Price Highs with Lower A-D Line"**

To quantify a bearish divergence, quantitative researchers utilize a two-stage detection system. A signal is triggered if:

1. The price index's two-year range rank reaches 100% (a new 2-year high).  
2. The A-D line's percentile rank remains below a specific threshold (typically 80% or 90%).13  
3. Confirmation occurs if, within 10 subsequent trading sessions, the index hits a 15-day low while the A-D line has failed to hit a new high for at least 30 days.13

When this system triggered for the S\&P 1500 in previous cycles, the index struggled over the following three months, with average maximum losses significantly outweighing maximum gains.13

### **Data Sources and Real-Time Tracking**

For professional-grade monitoring, analysts prioritize "final" breadth numbers released after the market close. While preliminary numbers are available via major financial media, the "gold standard" for A-D data includes:

* **WSJ/Barron's:** Utilized by the McClellan Oscillator research team for definitive breadth counts.17  
* **mcoscillator.com:** Provides daily updates on the A-D for Oscillator Unchanged and A-D for Oscillator Zero.17  
* **StockCharts.com:** Offers symbols like $NYAD (NYSE Advance-Decline Line) and $NAAD (Nasdaq A-D Line) for intraday analysis.15

## **2\. New Highs \- New Lows**

### **Definition and Internal Mechanics**

The New High-New Low (NH-NL) indicator measures the extremes of the price distribution within the market. It tracks the number of stocks reaching new 52-week highs versus those falling to new 52-week lows on the NYSE.18 This indicator is the purest measure of "momentum expansion." In a healthy bull market, as prices rise, the number of stocks reaching new highs should expand, reflecting a growing "class" of winners. Conversely, an expanding number of new lows during a price rally is a hallmark of terminal exhaustion.11

### **Interpretation and Historical Thresholds**

The High-Low Index is the primary oscillating derivative of this data, calculated as:

![][image4]  
Historical analysis has identified several critical thresholds for market diagnostic purposes:

| Level | Classification | Market Context |
| :---- | :---- | :---- |
| **\> 80%** | Extreme Strength | Broad-based bullish momentum; high-conviction buying.3 |
| **50% \- 70%** | Bullish Healthy | Normal market environment; consolidation and rotation.3 |
| **30% \- 50%** | Neutral/Deteriorating | Warning of internal weakness; risk of correction.18 |
| **\< 30%** | Extreme Bearishness | Oversold condition; often seen near intermediate bottoms.18 |

As of February 1, 2026, the High-Low Index stood at 88.0%, a 15.8% increase over the preceding seven days.3 This reading is particularly significant because it shows that despite the volatility in late January, the "expansion" of new highs (57) far outweighed the presence of new lows (2).3 This remains a high-conviction bullish signal, suggesting that the "under-the-surface" health of the broad market is stronger than the price action of the tech-heavy indices might suggest.3

### **Cumulative NH-NL Line vs. Daily Readings**

While daily spikes in new highs can be transient, the Cumulative New High-New Low Line provides a structural view of the market's progress. Similar to the A-D line, a divergence in the cumulative NH-NL line is a prerequisite for major market tops. In 2015, the cumulative NH-NL line provided a "significant warning" before the Brexit correction, as new lows began to spike even while the indices attempted to recover.11

During late 2025, the market experienced a "spiky" increase in new lows during the October-November dip, which served as the setup for the eventual breadth thrust.5 The fact that new lows have since retracted to near-zero is a powerful indicator that the current correction is likely a "pause in the advance" rather than the start of a bear market.3

### **Data Access**

Real-time and historical NH-NL data are most accurately sourced from:

* **Barchart.com:** Excellent for identifying specific stocks hitting new highs/lows and their sector distribution.  
* **The Wall Street Journal (WSJ):** Publishes the official daily counts for NYSE, Nasdaq, and AMEX.  
* **StockCharts.com:** The $NYHLO symbol tracks the daily difference on the NYSE.

## **3\. McClellan Oscillator & Summation Index**

### **The McClellan Oscillator: Calculation and Logic**

Developed in 1969 by Sherman and Marian McClellan, the McClellan Oscillator is a breadth-based momentum indicator that applies exponential moving averages to Net Advances (Advances minus Declines). The oscillator captures the acceleration or deceleration of breadth participation.21

The calculation involves two distinct EMAs of Net Advances:

1. **Short-term:** A 19-day EMA (using a 0.10 smoothing constant).  
2. **Long-term:** A 39-day EMA (using a 0.05 smoothing constant).

![][image5]  
The oscillator fluctuates around a zero line. A move into positive territory indicates that the short-term breadth momentum is accelerating relative to the long-term trend, a bullish condition.3 Conversely, a move below zero signals breadth deceleration.21

### **McClellan Summation Index: The Cumulative Momentum**

The McClellan Summation Index is the running cumulative total of all daily McClellan Oscillator values. Because it is a "cumulative oscillator," it is a much slower indicator that captures long-term shifts in the market's character.21

| Indicator | Reading (Feb 2, 2026\) | Significance |
| :---- | :---- | :---- |
| **McClellan Oscillator** | \-10.34 16 | Short-term momentum is slightly negative; digestion phase. |
| **Summation Index** | 2589.01 16 | Extremely positive; structural bull market remains intact. |
| **Prior Oscillator** | \-30.46 17 | Shows improvement from the late-January volatility. |
| **Prior Summation** | 2599.35 17 | Reflects a minor rounding top in long-term momentum. |

### **Interpretation of Levels and Signals**

Professional analysts use specific numeric "end-zones" for the Summation Index to identify extreme market conditions:

* **Bullish Bias:** A sustained move above \+500 is considered a long-term bull signal. The current reading of 2589 is well above this threshold, providing a significant "buffer" against a bear market.21  
* **Bearish Bias:** A sustained move below \-500 indicates a long-term bear regime.21  
* **Overbought/Oversold:** For the Oscillator, readings above \+100 are considered overbought, while those below \-100 are oversold. The current reading of \-10.34 is squarely in the "neutral/digestion" zone.16

A critical difference between the McClellan Indicators and the simple A-D line is their responsiveness. The A-D line is a "trend" indicator, while the Oscillator is a "momentum" indicator.21 This means the Oscillator will often diverge from price action weeks before the A-D line does, providing a more timely, if more volatile, warning.

### **Historical Performance and Extremes**

The Summation Index provided a key signal in June 2025 when it crossed above \+500, a move that analysts at the time predicted would be "different this time" due to the underlying yield curve steepening.12 During the "Taper Tantrum" of 2018 and the 2022 correction, the Summation Index plunged below \-500 months before the final market bottoms, identifying the periods of maximum liquidation.11

## **4\. Percent of Stocks in Downtrends**

### **Measuring Technical Erosion**

While major indices are often propped up by a few mega-cap names (the "Magnificent 7" effect of 2024–2025), the percent of stocks trading above or below key moving averages provides a true census of market health.9 A market where the S\&P 500 rises while fewer stocks trade above their 200-day moving average is a "narrowing" market, which is inherently fragile.9

| Downtrend Metric | Reading (Feb 2026\) | Healthy | Concern | Danger |
| :---- | :---- | :---- | :---- | :---- |
| **% \> 200-day MA** | 63.02% 23 | \> 60% | 40% \- 60% | \< 40% |
| **% \> 50-day MA** | 55.66% 8 | \> 50% | 30% \- 50% | \< 30% |
| **% \> 20-day MA** | 62.20% 3 | \> 50% | 35% \- 50% | \< 35% |
| **% Down \> 20% from High** | \~2.0%\* 24 | \< 15% | 15% \- 25% | \> 30% |

\*Calculated based on wealth creation concentration and narrow leadership reports in late January 2026\.25

### **Short-term (50-DMA) vs. Long-term (200-DMA) Trends**

The relationship between these two metrics is a powerful predictor of market cycles. In early February 2026, the 200-day breadth (63.02%) is higher than the 50-day breadth (55.66%).8 This configuration typically occurs during a "pullback in a bull market," where short-term momentum is lost but the long-term structural uptrend remains intact.3

However, professional analysts note that the "technicals are garbage" in specific segments.25 For example, despite the headline strength, the percent of stocks trading above their 30-week moving averages has shown a bearish divergence relative to the January 2022 lows, suggesting that a significant portion of the market has never truly recovered from the 2022 bear market and is instead propped up by liquidity inflows to the top 2% of companies that create 90% of aggregate wealth.24

### **Bear Market Territory and New Lows**

A "bear market" at the individual stock level is defined as a decline of 20% or more from its 52-week high. Tracking this metric by sector reveals hidden pockets of distress. As of early February 2026, the Technology sector shows a significant percentage of stocks in this category—with PayPal and Disney recently changing CEOs following aggressive valuation resets.2

Thresholds for broad weakness are generally identified when:

* Less than 40% of stocks are above their 200-day MA.  
* More than 30% of stocks are down \>20% from their 52-week highs.  
* New 52-week lows exceed new 52-week highs for more than five consecutive sessions.12

## **5\. Sector Breadth Analysis**

### **Relative Strength and Internal Rotation**

Sector breadth allows analysts to identify the "character change" in the market. In late 2025 and early 2026, the market has undergone a dramatic rotation away from "growth/AI" and toward "cyclical/real-economy" sectors.3 This is evidenced by the massive disparity in participation rates between Energy/Materials and Information Technology.8

### **Sector Breadth Heat Map (January/February 2026 Data)**

| Sector | % \> 50-day MA | % \> 200-day MA | Momentum Status | vs. S\&P 500 |
| :---- | :---- | :---- | :---- | :---- |
| **Materials (XLB)** | 96.15% | Very High | Leading | Strong Outperformer 3 |
| **Energy (XLE)** | 95.45% | Very High | Leading | Strong Outperformer 3 |
| **Industrials (XLI)** | 76.25% | Moderate | Healthy | Outperforming 3 |
| **Consumer Staples** | 75.00% | Moderate | Defensive | Improving Participation 8 |
| **Utilities (XLU)** | 70.96% | Moderate | Defensive | Improving Participation 8 |
| **Comm. Services** | 69.56% | Moderate | Mixed | Neutral 8 |
| **Real Estate (XLRE)** | 64.51% | Moderate | Improving | Neutral 8 |
| **Consumer Disc.** | 60.41% | Moderate | Struggling | Lagging 8 |
| **Financials (XLF)** | 57.33% | High | Breaking Out | Strong Internals 8 |
| **Health Care (XLV)** | 55.00% | Moderate | Volatile | Neutral 3 |
| **Technology (XLK)** | 45.71% | Low | Declining | **Underperforming** 2 |

### **Divergence Analysis: Technology vs. The Broad Market**

The most alarming data point in the current market structure is the collapse of Technology (XLK) breadth. While the S\&P 500 attempted to make new records in early February, only 45.71% of technology stocks remained above their 50-day moving average.8 This is a "bearish sector divergence," where the sector's price may be buoyed by a few giants (Apple, Microsoft, Meta) while the average software and semiconductor component is in a downtrend.2

Specifically, the QQQ/QQQE divergence (Z-score 1.14) confirms that poor breadth within tech is being masked by mega-caps.3 Historically, when sector breadth fails so dramatically, it eventually forces a correction in the price index as the few remaining leaders succumb to the weight of the declining majority.9

### **Building a Sector Breadth Heat Map**

To build a professional breadth heat map, one must:

1. **Calculate Component Status:** For each sector (e.g., XLF), determine what percentage of its components are above their 20-day, 50-day, and 200-day moving averages.  
2. **Assign Z-Scores:** Compare current participation levels to the 3-year historical average for that sector.  
3. **Cross-Reference Volume:** Overlay Up/Down volume ratios for each sector to confirm if the price participation is backed by institutional liquidity.3

## **6\. Small Cap vs. Large Cap Breadth**

### **Russell 2000 as a Sentiment Barometer**

Small-cap stocks, represented by the Russell 2000 (IWM), serve as a high-beta proxy for economic confidence and interest rate expectations.19 Because small caps are more sensitive to the cost of capital and domestic growth, their breadth often leads the S\&P 500 at major turning points.16

In early 2026, the small-cap versus large-cap cycle is at a historic extreme. US small caps are in their cheapest quintile versus large caps since 1990\.26 Historically, when small caps reach this level of relative undervaluation, they tend to outperform over the following 5-to-10-year periods.26

### **Current Divergence and "Animal Spirits"**

| Index / Indicator | 12-Month Performance | Current Breadth Reading | Implication |
| :---- | :---- | :---- | :---- |
| **S\&P 500 (SPY)** | \+14.16% 2 | 55.66% \> 50-DMA | Large-cap resilience propped by mega-caps. |
| **Russell 2000 (IWM)** | \+14.16% 2 | Improving/Strong | Broadening participation; "Equal Weight" trade.3 |
| **S\&P 500 Equal-Weight** | Breaking out of base | Higher Highs | Healthy shift toward the "average stock".19 |
| **Yield Curve (10y-3m)** | Steepening | roadmap for Small Caps | Highly bullish for IWM outperformance.16 |

The S\&P 500 Equal Weighted Index ($SPXEW) is currently approaching its own all-time high and has broken its pattern of lower highs/lows.19 This "broadening" of participation is a significant positive. If the equal-weighted index can reach a new high before the cap-weighted S\&P 500, it would confirm that the bull market has transitioned to a much more sustainable footing.19

### **Small Cap Weakness as a Leading Indicator**

Small cap weakness typically serves as a leading indicator of large-cap bear markets during periods of "liquidity droughts." However, in early February 2026, we are seeing the opposite: small-cap strength and large-cap (tech) consolidation.3 This suggests that "animal spirits" are returning to the real economy, potentially shielding the broader market from a full-blown bear market despite the tech sector's struggles.3

## **7\. Volume Patterns**

### **Up/Down Volume and Institutional Conviction**

Volume is the "gasoline" of the market. Breadth indicators that incorporate volume data—such as the Up/Down Volume Ratio—measure the conviction behind the price move.3

Key metrics as of February 1, 2026:

* **Up/Down Volume Ratio:** 3.05. This indicates that for every 1 share traded in declining stocks, 3.05 shares were traded in advancing stocks, a sign of strong institutional accumulation.3  
* **TRIN (Trading Index):** 1.28. The TRIN is calculated as:  
  ![][image6]  
  A reading above 1.2 is contrarian-bearish, suggesting that volume is flowing into decliners more aggressively than the advance-decline ratio would suggest.3 This indicates a "wrinkle" in the bull case—more stocks are going up, but the selling in the losers is highly aggressive.3

### **On-Balance Volume (OBV) and Accumulation/Distribution**

On-Balance Volume (OBV) provides a running total of volume by adding volume on "up days" and subtracting it on "down days".11

* **Bullish Case:** Price hits a new high and OBV hits a new high, confirming institutional support.  
* **Bearish Case:** Price hits a new high and OBV remains flat or declines, signaling "stealth distribution" by smart money.11

In early 2026, volume in the QQQ (Nasdaq 100\) has been characterized by "spikes" that frequently act as bottom markers.16 Conversely, the S\&P 500 volume remains stable, suggesting that the broader market is in a "normal rotation" and "consolidation" phase rather than a panic liquidation.3

## **8\. Breadth Thrust Catalog**

### **The Mechanics of Market "Thrusts"**

A Breadth Thrust occurs when market participation shifts from extremely negative to extremely positive in a very short time frame. These are rare events that capture "final capitulation" followed by "hot and heavy" buying.29

| Indicator | Definition | Signal Date | Historical Success (12-mo) |
| :---- | :---- | :---- | :---- |
| **Zweig Breadth Thrust** | 10-day EMA of (A / (A+D)) from \<40% to \>61.5% in \<10 days.32 | Nov 28, 2025\* | 100% (16/16 instances).5 |
| **Whaley Breadth Thrust** | 10-day Average Advance-Decline Ratio (ADR) \> 1.97.22 | April 24, 2025 | Very High; Leading Indicator.33 |
| **Super Zweig** | Rare extreme variation of ZBT.34 | N/A | Mid-20% average returns.34 |

\*Considered an "unofficial" signal by some due to reaching 58% rather than 61.5% in 5 days.4

### **Historical Success and Forward Outlook**

Since 1945, only 14–16 "official" Zweig Breadth Thrusts have occurred.30 The average S\&P 500 gain following these signals is 24.6% over the subsequent 11 months.30 The signal on November 28, 2025, which saw the S\&P 500 rally 5.3% in just 7 days, is particularly noteworthy because it occurred when the market was within 5% of its all-time high—an unprecedented context that may test the indicator's historical reliability.5

The forward target for the S\&P 500 based on the November 28 thrust is approximately 6,650 to 6,800, a level the market reached in early January before consolidating.6 Because the Zweig thrust is a "character change" indicator, it signals that any subsequent corrections are likely buying opportunities rather than the start of a bear market.4

## **Internal Rot Detection Framework**

To identify "healthy index, sick market" conditions, professional analysts utilize a multi-factor score.

### **1\. The Breadth-Divergence Checklist**

* **Price vs. A-D:** Index makes a higher high, NYSE A-D line makes a lower high.9  
* **Price vs. Highs:** Index makes a higher high, number of New 52-Week Highs makes a lower high.11  
* **Price vs. Moving Averages:** Index makes a higher high, % stocks above 200-DMA declines.9

### **2\. Liquidity and Momentum Alignment**

* **TRIN \> 1.2:** Selling pressure in laggards is outweighing the buying in leaders.3  
* **Yield Curve Divergence:** 10y-3m spread fails to support the rotation into small caps.16  
* **VIX Term Structure:** Spot VIX (17.01) significantly below futures (19.10), indicating a "contango" that masks building stress.3

### **3\. Current Diagnostic Score (Feb 2026\)**

As of early February 2026, the Internal Rot Score is **Moderate**. While Tech breadth is "sick" (45% participation), the broader market participation is "improving" (Cyclicals \> 90%). This is a scenario of "healthy rotation" rather than "terminal exhaustion".3

## **Proposed HENRY Vectors**

The High-Efficiency Network of Risk Yield (HENRY) vectors provide standardized quantitative triggers for institutional risk management.

| ID | Name | Current Value | Thresholds (Alert / Danger) | Source |
| :---- | :---- | :---- | :---- | :---- |
| **VX-HEN-12.01** | A-D Line Divergence | Positive | Lower High / Stagnation | mcoscillator.com 16 |
| **VX-HEN-12.02** | High-Low Index | 88.0% | \< 50% / \< 30% | WSJ / Barchart 3 |
| **VX-HEN-12.03** | McClellan Summation | 2589 | \< 500 / \< \-500 | mcoscillator.com 16 |
| **VX-HEN-12.04** | Short-Term % \> 50-DMA | 55.7% | \< 50% / \< 30% | MacroMicro 8 |
| **VX-HEN-12.05** | Tech Participation | 45.7% | \< 40% (Danger) | MacroMicro 8 |
| **VX-HEN-12.06** | Zweig Signal Status | ACTIVE | Price \< ZBT Entry | Merrill Lynch 6 |
| **VX-HEN-12.07** | TRIN Volatility | 1.28 | \> 1.2 / \> 1.5 | SignalPlus 3 |

## **Data Sources**

The accuracy of breadth analysis depends on the quality of the "final" data counts.

| Metric | Free Source | URL / Symbol | Update Freq |
| :---- | :---- | :---- | :---- |
| **A-D Line** | Fidelity / WSJ | $NYAD (StockCharts) | Daily 9 |
| **NH-NL Counts** | Barchart | NYSE Highs/Lows | Real-Time 11 |
| **Oscillators** | mcoscillator.com | [Link](https://www.mcoscillator.com/) | Daily (Post-Close) 16 |
| **MA Breadth** | MacroMicro | [Link](https://en.macromicro.me/) | Daily 8 |
| **Sector Health** | StockCharts | $XLF, $XLK, etc. | Real-Time 19 |
| **Volume Ratio** | SignalPlus | Market Recap Blog | Weekly 3 |
| **ZBT Signals** | Real Inv. Advice | [Link](https://realinvestmentadvice.com/) | Occasional 5 |

## **Conclusions and Forward Outlook**

The quantitative internals of the United States equity market as of February 2026 reveal a market that is fundamentally "in gear" on a long-term basis but experiencing a high-velocity tactical rotation. The confirmed Zweig Breadth Thrust from November 2025 provides a structural floor, suggesting that the broader indices will likely be significantly higher by year-end 2026\.5

However, the "illness" within the Technology sector is the primary risk factor. With participation in Information Technology dropping below 46%, the market is relying on Energy, Materials, and Financials to maintain the index levels.3 If the Kevin Warsh nomination and subsequent yield curve steepening continue to compress tech valuations without a corresponding increase in cyclical earnings, the S\&P 500 will face a "narrowness" trap.2

Investors should prioritize equal-weighted exposure and cyclical sectors while monitoring the VX-HEN-12.05 Tech Participation vector. A move in Tech breadth below 40% alongside a reversal in the McClellan Summation Index below \+2000 would signal that the "healthy rotation" has failed and a broader market correction is imminent.8 At present, the 88% High-Low Index and positive Summation Index suggest the path of least resistance remains upward.3

#### **Works cited**

1. Stock Market News for Feb 2, 2026 \- Nasdaq, accessed February 3, 2026, [https://www.nasdaq.com/articles/stock-market-news-feb-2-2026](https://www.nasdaq.com/articles/stock-market-news-feb-2-2026)  
2. United States Stock Market Index \- Quote \- Chart \- Historical Data \- Trading Economics, accessed February 3, 2026, [https://tradingeconomics.com/united-states/stock-market](https://tradingeconomics.com/united-states/stock-market)  
3. Market Recap — February 1st 2026 | by Daniel S. | Feb, 2026 | Medium, accessed February 3, 2026, [https://medium.com/@signalpluspro/market-recap-february-1st-2026-ab74fb870614](https://medium.com/@signalpluspro/market-recap-february-1st-2026-ab74fb870614)  
4. (12/08/25) Markets: "Breadth Thrust" Signals Suggest More Gains Ahead \- MoneyShow, accessed February 3, 2026, [https://www.moneyshow.com/articles/tradingidea-64657/](https://www.moneyshow.com/articles/tradingidea-64657/)  
5. This Rare 'Perfect' Market Indicator Says a Major Bull Market Is Coming \- 24/7 Wall St., accessed February 3, 2026, [https://247wallst.com/investing/2025/11/28/this-rare-perfect-market-indicator-just-flashed-a-major-bull-market-is-coming/](https://247wallst.com/investing/2025/11/28/this-rare-perfect-market-indicator-just-flashed-a-major-bull-market-is-coming/)  
6. A Stock Market G.O.A.T. Appears: Perfect Historic Track Record, accessed February 3, 2026, [https://oakharvestfg.com/stock-talk/a-goat-appears-perfect-historic-track-record/](https://oakharvestfg.com/stock-talk/a-goat-appears-perfect-historic-track-record/)  
7. Market navigator: week of 2 February 2026, accessed February 3, 2026, [https://www.ig.com/en/news-and-trade-ideas/weekly-market-navigator--2-feb-2026-260202](https://www.ig.com/en/news-and-trade-ideas/weekly-market-navigator--2-feb-2026-260202)  
8. US \- S\&P 500 Share of Stocks Above 50-Day Moving Average by ..., accessed February 3, 2026, [https://en.macromicro.me/collections/34/us-stock-relative/72169/sp500-sectors-50ma-breadth](https://en.macromicro.me/collections/34/us-stock-relative/72169/sp500-sectors-50ma-breadth)  
9. Advance decline indicator | Market breadth \- Fidelity Investments, accessed February 3, 2026, [https://www.fidelity.com/learning-center/trading-investing/advance-decline](https://www.fidelity.com/learning-center/trading-investing/advance-decline)  
10. Advance/Decline Line \- TradingView, accessed February 3, 2026, [https://www.tradingview.com/support/solutions/43000589092-advance-decline-line/](https://www.tradingview.com/support/solutions/43000589092-advance-decline-line/)  
11. Why the NYSE Advance-Decline Line Is More Important Than Ever ..., accessed February 3, 2026, [https://au.investing.com/analysis/why-the-nyse-advancedecline-line-is-more-important-than-ever-in-todays-market-200606115](https://au.investing.com/analysis/why-the-nyse-advancedecline-line-is-more-important-than-ever-in-todays-market-200606115)  
12. Chart In Focus \- McClellan Financial Publications, accessed February 3, 2026, [https://www.mcoscillator.com/learning\_center/weekly\_chart/](https://www.mcoscillator.com/learning_center/weekly_chart/)  
13. The granddaddy of market breadth indicators triggered a warning ..., accessed February 3, 2026, [https://sentimentrader.com/blog/the-granddaddy-of-market-breadth-indicators-triggered-a-warning](https://sentimentrader.com/blog/the-granddaddy-of-market-breadth-indicators-triggered-a-warning)  
14. United States bear market of 2007–2009 \- Wikipedia, accessed February 3, 2026, [https://en.wikipedia.org/wiki/United\_States\_bear\_market\_of\_2007%E2%80%932009](https://en.wikipedia.org/wiki/United_States_bear_market_of_2007%E2%80%932009)  
15. Advance-Decline Line \- ChartSchool \- StockCharts.com, accessed February 3, 2026, [https://chartschool.stockcharts.com/table-of-contents/market-indicators/advance-decline-line](https://chartschool.stockcharts.com/table-of-contents/market-indicators/advance-decline-line)  
16. McClellan Financial Publications, accessed February 3, 2026, [https://www.mcoscillator.com/](https://www.mcoscillator.com/)  
17. Stock Market Breadth Data | Daily Oscillator Data, accessed February 3, 2026, [https://www.mcoscillator.com/market\_breadth\_data/](https://www.mcoscillator.com/market_breadth_data/)  
18. Market Breadth: Definition, How it Works, Purpose, and Indicators \- Strike Money, accessed February 3, 2026, [https://www.strike.money/stock-market/market-breadth](https://www.strike.money/stock-market/market-breadth)  
19. The Stock Market Is Quiet… but Something Big Is Brewing Under the ..., accessed February 3, 2026, [https://articles.stockcharts.com/article/stock-market-is-quiet-but-something-big-is-brewing-under-the-surface/](https://articles.stockcharts.com/article/stock-market-is-quiet-but-something-big-is-brewing-under-the-surface/)  
20. S\&P 500 Index Ideas \- SPX \- TradingView, accessed February 3, 2026, [https://www.tradingview.com/symbols/SPX/community-ideas/page-23/?](https://www.tradingview.com/symbols/SPX/community-ideas/page-23/)  
21. McClellan Summation Index \- ChartSchool \- StockCharts.com, accessed February 3, 2026, [https://chartschool.stockcharts.com/table-of-contents/market-indicators/mcclellan-summation-index](https://chartschool.stockcharts.com/table-of-contents/market-indicators/mcclellan-summation-index)  
22. Whaley Breadth Thrust: A Deep Dive into Market Momentum \- QuantifiedStrategies.com, accessed February 3, 2026, [https://www.quantifiedstrategies.com/whaley-breadth-thrust/](https://www.quantifiedstrategies.com/whaley-breadth-thrust/)  
23. US \- S\&P 500 Stocks above 200-Day Average | Series \- MacroMicro, accessed February 3, 2026, [https://en.macromicro.me/series/22718/sp-500-200ma-breadth](https://en.macromicro.me/series/22718/sp-500-200ma-breadth)  
24. Probabilities and Payoffs \- Morgan Stanley, accessed February 3, 2026, [https://www.morganstanley.com/im/publication/insights/articles/article\_probabilitiesandpayoffs.pdf](https://www.morganstanley.com/im/publication/insights/articles/article_probabilitiesandpayoffs.pdf)  
25. CAPITAL IDEAS: ABCDEFU Allen Harris \- The Berkshire Edge, accessed February 3, 2026, [https://theberkshireedge.com/capital-ideas-abcdefu-allen-harris/](https://theberkshireedge.com/capital-ideas-abcdefu-allen-harris/)  
26. Making the case for US smaller companies | Fidelity Singapore, accessed February 3, 2026, [https://www.fidelity.com.sg/articles/analysis-and-research/2025-09-12-making-the-case-for-us-smaller-companies-1757638987592](https://www.fidelity.com.sg/articles/analysis-and-research/2025-09-12-making-the-case-for-us-smaller-companies-1757638987592)  
27. What Market Indicators Suggest a Bull Run Is Coming? – Entomology Lesson Plans for Elementary Educators \- University of Nebraska Pressbooks, accessed February 3, 2026, [https://pressbooks.nebraska.edu/unlentomologylesson/back-matter/what-market-indicators-suggest-a-bull-run-is-coming/](https://pressbooks.nebraska.edu/unlentomologylesson/back-matter/what-market-indicators-suggest-a-bull-run-is-coming/)  
28. US 500 (SPI) / US Dollar Ideas — EASYMARKETS:SPIUSD \- TradingView, accessed February 3, 2026, [https://www.tradingview.com/symbols/SPIUSD/community-ideas/page-23/?](https://www.tradingview.com/symbols/SPIUSD/community-ideas/page-23/)  
29. Watching for a Zweig Breadth Thrust Signal \- Free Weekly Technical Analysis Chart, accessed February 3, 2026, [https://www.mcoscillator.com/learning\_center/weekly\_chart/watching\_for\_a\_zweig\_breadth\_thrust\_signal/](https://www.mcoscillator.com/learning_center/weekly_chart/watching_for_a_zweig_breadth_thrust_signal/)  
30. Breadth Thrust Indicator Explained: Key to Market Momentum \- Investopedia, accessed February 3, 2026, [https://www.investopedia.com/terms/b/breadth-thrust-indicator.asp](https://www.investopedia.com/terms/b/breadth-thrust-indicator.asp)  
31. What the Zweig Breadth Thrust Indicator Is Telling Us \- Explosive Options, accessed February 3, 2026, [https://explosiveoptions.net/stock-market-analysis/zweig-breadth-thrust-indicator/](https://explosiveoptions.net/stock-market-analysis/zweig-breadth-thrust-indicator/)  
32. Two Ways to Use the Zweig Breadth Thrust \- Plus an Added Twist \- StockCharts, accessed February 3, 2026, [https://articles.stockcharts.com/article/articles-arthurhill-2025-03-two-ways-to-use-the-zweig-brea-495/](https://articles.stockcharts.com/article/articles-arthurhill-2025-03-two-ways-to-use-the-zweig-brea-495/)  
33. October Monthly QUANT Recap \- Finom Group, accessed February 3, 2026, [https://www.finomgroup.com/october-monthly-quant-recap/](https://www.finomgroup.com/october-monthly-quant-recap/)  
34. A Rare Zweig Breadth Thrust Provides Optimism \- RIA \- Real Investment Advice, accessed February 3, 2026, [https://realinvestmentadvice.com/resources/blog/a-rare-zweig-breadth-thrust-provides-optimism/](https://realinvestmentadvice.com/resources/blog/a-rare-zweig-breadth-thrust-provides-optimism/)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAAhCAYAAABkzPe+AAAE50lEQVR4Xu3cW8isUxzH8b8cIue2SI7JjUIOSZRDIlwQIULYtkNJLrggN/Z2KJKcchYbiaKkKBfSREm5kCIXUoiEciGEcvj/WrPM//nP88zMtp9nXm++n/rXO+t53nfWrPXW/FprzZgBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP4Dtva6zeuQ1L67156pdmncUexhs68P6UEr/Yx2sGaf1T+9xizes226thK28DorNwa6dkVu7MmWtthcV2d4XZkbAQDAcE7x+tXr5NR+ttf7Xh95Xeh1jdeHXi/Gm9xar6+9PvA6Ol0b2vdeB6W2I7z+8LrD61yvx72+8jo93uQ2WLnvKa+90rWVcJzXVrkx0Dw8kBt7srM151rjVuda1zL18/7cCAAAhvOu119WVk2iXa28iSv4VHrzftvKalB1gNc3XheFtmU40OtnryPzBSv9Ub+q862Eykj9zfcNYZ3XmtyYbOf1fG4MNN5/ej2TL/Soa67vC22Rxl39BgAAA1Po2cfrC68b07WuQKP7tGVW6U1eb/YKeMui1ahrrQS2tqAZg4eov3qNUQ4oQ9F2cxyvNtdbd1+0nXunlbA2srLlO4Suuc7jFqnfAABgQFq1udlKABh5Pdm4WrbfXrfm+S79ztNWzoVVI5v+3VkUXu6xslXZVtdNbm2lVZ27rJxdU5jIoUFbpHl7V6tBCnfRjza9TTqERQKbwtjVuXFMr+VyK+HpM2uOfZ+65lrP2WVT5h0AAPwLdZWqBra83da2ArWb18fWPGvVtR2qlaHtc2MPLrDJ4fyulcG8UqQw9Ftqa1tREoWWeR9CUJg5ITd2mBfYNJYv2/RKoWgrVeFWc1RXu+rf6nN821Yl61y/MH68o5UPJ0T5fwYAAPQohh7RG+874bHkQKMzTW96PRLaJG6HKnyst/J7OpN1u5U3/kgrY3fb9MpaLX24oYuCUjyzNrLyPGqXeu4uOsfKazk8tOWAom1h9VWrd29YWeWbF4ZyUOwyL7CJxr8tsN1qk3Cs6794HeV1rE3Gtw9tIbfOtZ5/rZX/j5MadxDYAAAY1MPWPDCezyopAOUtspe8HrXm72nlR9tmNTDpgP1GK6s/+oShvipEP/dFn0KtzyUKDCObnOtSmPvhn6tlRehTr2NCm+i+M8Pj56yEWN2vfu8//nmWPgObtp/z39O4HRwe121dBbd9bTK+m0vjqTmMc61QHef6Eq9bbPqrPvKqHAAA6IGCzUNWVmp0Lkr0+CcrnxQ9zMq5rre8fvf6MtTx1gxL2mbU10B8ZyU4vWflk4ynja8/YfO3FhelwPOKla/hqKs8alMf1faa171WPgmq11H7rPNXO43vFwUOhdVvrXwNifqtQPeJTc6G6XxcdZWVQFjr1HAtB6wuiwQ2hcVnw+NLrbyWjTZZ6fvcymtTu1bD+hjfOtcawzjXWk2Lc73eps8F6noMvQAAYBW6yesy63eFbRm0JXueNQNLppW+V71OtNnfnSZtZ78yPdeG3DiDAl4d32V4zErAPzS0XRx+BgAAq9Tmrv6slG1yw5LojODeuXGGZY6vQmkMpvvZ9FlGAACA/4UbbOUC46LUP20Hb0q4BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALCq/A0eecidSSnQ4AAAAABJRU5ErkJggg==>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAYCAYAAAD6S912AAABAklEQVR4Xu3TsWoCQRQF0BEVFLRSFIsgKYMEC/2CVDZpbC3yExLBSlKZwlqwyzeIYOfWlmKRxsIvCAi2mnvZOyGuWuzOdnrhsMMO+5jH7DPmnitpwkfwZdRkYQozyIhTOnAAD3ISKSX5hAFsoCyREmvBBLxLA3qwhYqETg36wuKvsIO6hEoahvAgDAvujX9aChV+zPaW4sEKjtojG54+L1xfTGwFCzIy5/8a22TLbbHhjX8Ji/6F1bvS+r+h8GZ5at42MVWt5/Ks9+YFvo0/DbQwp/8a99fGb/lHONdFPTlJFOwqdFIwhidxTuwF7YXYceQwOOURJvAmdgicwqlKyq3mF/AvNFP/lS5+AAAAAElFTkSuQmCC>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAYCAYAAAD+vg1LAAABLklEQVR4Xu3UMUtCURQH8BMaFA0aRCFCQ5uDX8ChKaHGwCFycfYLWHvu4mLQ0BQFzW7RUGNTkKODDTr4BSII+h/u/z7fu90XSu8t4R9+IJzrkXfOu4osE5MMbEPhF/ng9ALJwTG8wBudQg2a9Ap3PKvmzqaYxm1yo82eoEMr0XJ8SjCFI/KlBQPacmqxSa1xHSawR75o4xHpQudKF/qwRm50ptcwpJ1o2Z/w4uKij64juKVstOyPzncMB24hlEP4gCppVmEjOOFJao3Di3NjL8QD9MSMwI5B355zfo5EF2KXYhcXjl7ze7qEdZl9pwI3cCFm/sHrp7/2SF/wCe+OZ9gne9Ns410xV7wsZiQqkejYruTnU/45qTW2iyvK7K81kZzAGTQk4RlrEh/DP8o3bKQ53lMtcx8AAAAASUVORK5CYII=>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAAvCAYAAABexpbOAAAK/ElEQVR4Xu3da4itVRnA8Se6X+x+JaNjWREZlZGSdjlo0Y0iMjAqJPxQkVZmV81gxPqQmUhmdhMzie5ZqBkhMlBIF9CKpFCEKYroQwVRfRCi1n/W+5y9Zs2+nZl9Zvac8//B4sy79rvXfvc7B/Yzz7PW2hGSJEmSJEmSJEmSJEmSJEmSJEmSJEmSJEmSJEmSJEmSJEmSJEmSlB5W2sP7Th1RXlXaa/tOSZK0++5b2uWlva5/YImcWNr5pf2otAcOfW8q7Xelfb20ew19W8X4F5b239JOLe1Bpe0fjj9a2kkHzow4p7QHNMfjcP53SrtP/8AewP+HE/pOSZK0u95Z2qWx/aDnUDujtP+U9sLhmKDpktIefeCM7XlLaX/p+n5Z2iO6PgLFWbi2D/ede8iPSzu675QkSbvj2NJuKe1J/QNLhmByJWpG7bPD8ROHvkUEmoxxdWmrTd9Dhr6tjM+1vajv3EMINi+Lrb13SZK0YLeXdkzfuYSeHzUTeFxp/yjt7OGY/sQcvB+Wdu/SnhM1+3Zx1MDpV1HLk5Qpz42aQbqmPm0d4/x76P/i0G4a+tMnSju+tJ80fbzm6aXdP2pw97ihn4DnzKiv+cmhDxy/prSjSru+tJc1jy2blajBsSRJ2mVbzSDttNOiBl4EPF8u7WelXRSjciXvgYwQc9yYg3Veae+IGhBRwrw1atbrjqjj0C5Yf2aV5dCnNH0EaG05lHMox5LlQ75mzlMjSONnyqE3Do/jM8O/eELU9/KY0t4//LusCFZ/03dKkqSdxdyvZV5okLIcSsAFgibmstGXQRGZrbujZsjIqhFs8Fhm1QimCN7ujDrOKVFXRKYsh1IGBf9y3AezBF+ZdWKcteHnDNKyn8AQZOAIFhMLJv4XdTHD+2Lz+Msk74EkSdpFBDGU5pYdwde7uz6yZpQ9E8HnL2I0b+zxUUumzyztrqhjEJRlGfS9sTFY+mdsDF75mb4WAR6vQUBG4EUpmQwU47wt6uuA+0qQCLJ0rGJlhetzo5ZzwXVeFcu/ivQNMQqUJUk67LCfGeUv2qOizqvKY1rq+zm3xXH72KIyMpl5Wnbcx3uiZtQocyYyav3qTYILMmwER1eU9sio5dErowZrlFJvizr/7cnDcxj/c1GzXr+PGghyLoEVfScP52F/aT8t7ePDMb+Ld0UNvH4eo208MqMHgsYbor4ev79vlfae0r439C07guK9vHhCkqSJ+NDeH3Xieu7h9eCok9gJBM46cGYNKpj4/8fS3h71eS2OGYcSGj8vKiNDRirLdocTSpPj9kjLDYEJ4LazDQhlwn78LIcyZw78rnmdRFk0EeTtpc2JCYzzfS0C94Ug+Lqu/ytRM5EE3O0fJQS710ZdTCJJ0sKNmwO1FuP35qL01s6nauU4ZH0WiRLhX/tOzY3fC0EEwTSrRl+68eHDBn8gZBl5HAKwfksY/gihTcI3KfyhOaZs3a7GzUUazDnMbDT3e5GBoyRJ61ht2G/CyrYR48pL/erEFh9mf4u6QnGR+NDkeqRZVmO0GKPHHySUmFuUoNusYq8P2DhupwncHDVLyR83+boEjpS0JUlaKCatU8bMPb1oa7F5AjcfePkBNQ7jUEZtJ9i3mHPVvkbbCPYmMWDTvFZjcsAG5mEyfxDMy5sWrKEP2HhuG7CtRn095iK2rzst0ydJ0pawOpCvNUo5Gb2fg8bEec6dhPLQuK9H2q5ZARv7g9mOrDbJakwP2MCech+Iml2bpQ/YKHWOC9j4v2/AJkk6ZLIc2pYxc7PWHuf05VD2GUuzyqFvjM2ZtWxPb87rzQrYpLQaswM2AjX+qDinf2CMPmB7QWzMIH8tauaZzBuLHpAZN0mSFib38GonUjMfZ1w5lMUE+WHI8StiY0mpH2dRDNg0r9WYHrAdG6P/sxloTdMHbDyXBQZgfzvK/DgmRmV9Arf2DxlJkrZlX2n/irqHF6VMNkv9ftS9xPjapGcM57EqlL27mOf2zajz2P4e9Xl4atStDjheLe3lQ/+ikO07mFWiuRdcbmnBvKXHDn2L2Kai37eu3X/uYMd/Wmmvj80B8qFAIMM1tkF3Xvsi9s3L8fv7v5NujMmvy+8m96VLbE/zvK4P+0r7fGl/jvr/+oMxGne1tBNL+0hs3BKFfevIvl0e27+XkiTtOXz4t1mOWShHfaO0PzV97Gc26YN8K9q5ejnnj9biA33afCuQrbkzthewUU6e92u7vhR1Y9/MAHFPLhk9vG3jyuY7hd/HuK1oJEnSDmBVKlm9eZFFOSlGX62ERZZqySRRHs4sCsHWWmwtWOA54xZ4HAzeG99SMAvXe3zUL4Rvv2N0JU/YpiybT1pFfKgRKFLClCRJu4RVePNmyM6NGgCxG33OVzpj9PA6goq3Rl3wQFmLYOMlMVr8wDFZOTJk5w19icCgXVxBlow5drlQox8rMX/qwqjPp0QLSnh8wwSlOZ7TltIeGvV7RF/Z9ffmDdh4P9yXlRhlH7n20/OEAcEu9/tjw/HRUVcHU7oF22E8u7QzSzt16AMZrna1cY/3wv1+83Cc4+Z7Y1yurx+X0vzFUUvv03D/J20pI0mSdgBBzriVq+NkSY5MGEEbJdWLRg+vB0tnNz8/K+p2DeyCvzL0U2LMkucFw7+JIKPduiTLoZkl68fCWoyu/47mZ/oJ5EBpNAMOgjC+L5TSJYEOE9wnmTdgO234l+tkY1cmx3Nf8r0QOF0W9bUIYglUCd4I6phcf2vUjFxeP629NwSx/QbMIDD7dXNMFox5kTkuQXWOi3ZcMpAEtVzrtOwZ76kvSUuSpB2WmaFZCNLaVYLM1yLgaQMaggW2YyDbw55ciUAvS6dkmDLzw55dibFXY2PGay02l0NZMXhcc9zOeaMkmVtAtIEeAVFmBAkkfxt1wntmthLn86XsuSXKdVGfm8efHp16ANe70hwTCH5o6Mv3wjXdHXUMMlp5LzIY4j0SZOWcu1Ni9DVlWQ69eThO3FMC2AzGwDiZ7csgK8dFOy4LWFjswn2Y9gX0bcAnSZJ2URvQTNJ/YwLBEVmfNjtHyW3cl6qzxQNBVTtnjmMWD6Tct67FXLk++0cGj2vN+Vy5XxcySKNloJcBKWVf2slRX5vsHyt37zecN848GTbeb5tlJIt2T2wsh1LCZVVkjwwZ2T7eI+XmvP6zom5ngSyHthsrk2XkvGtiFJjx3siYcS9yXOS4yHG55hNKO6q0V0f9vU2SGUBJkrTLCKi+G+PLg/tKuyFqNqadX0aW6wsxymKBch+lPz7kr4i67QfI4LB9A9syEGARBJ0/nL8vank1t0EhoMptUHjNdhsUghK2eMjn4qbSro06RgZ3/JurQ8mokdViLhvBzA+ivg/mt80KUmcFbFdFDc7INrb34aux+VspuMfcF66dewPew5VRM2iUUm+LGpBmxovtMth2hftye2l3Rb0nBMugJE2QRpnz+qj3EjkuQWuO+6kYjcu8Q7J9XA+Pt1nN1otLuyXq1iSSJGmXEagRsM3a7HQeBBkESRmsJfpyccPB7qnWYtxxAQalv8zu9a/dBma5d1xb3p1kVsB2sCbtoZb3g0BrXIZyGu7FpPfSjtvfE66DUm0GvuN8Oxa/958kSdqGfVHnbOUqy72AyfJcL0FHux3IojDubm2lsQwujcXfU0mStABMxPdD+shG6ZRvI5AkSUusL5/pyEJWcVqpVJIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZrf/wEfF6sYHmsZzAAAAABJRU5ErkJggg==>

[image5]: <data:image/png;base64,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>

[image6]: <data:image/png;base64,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FfTHJgmOETy5log31gcOiJkwrOPm2jFXkHniyTsmZh7LCs/NviH7XrR2+UqzXLuEZxDWBL6/HGcVmYw3146xjGunYBMREdmGIJ7SGwZ4h35cjgm78f7JEQQCP+acJ/R27PQZECKULmGjwSI4z71AQv2l0cUdQpHQ5fHTOYRY9oFXCu8U72xFoCAsUrhcFrMQJu14rvBm7RPd45XiDa8S4ikZw56AyLmpHBNSxIuFZy25JGY1+PAUPnX6zHi4n/FSHJl1RRASTqRtHDdidI/pfJKhV7xai0AgZt/cS988L9cu58ra0SeevFw7rkMcIhKTFJA5Zjyu1Vu4aO0QzRfE2jxHERERWRIIkW/FfBFgvCtHRvfMnBs9OX1kNbpwwftyXMwn8yMOCKdtSnTgrUE0ECbEa7X71M7zyJVDMADeH8QGYblvN/t8dLGHZ2c1Zt62K2KWc8czTogeikWEnBE9P45csKNiVgcO4YI4TagfR983RBebv50MIZSJ/UkKGxL09yvtrAHnGCPeLsZOeRPEKIzj/lH0sVZPFeHizEVbBPdm39+Z2hBluXYJa8e60ZZrhweQtSfPDpg/oiy9pwhs8gBpZy65dvxb144xrsbaPEcRERFZEvw4U7QXb1QFzw05S1WIVRAVeIOysG6FcBs/6psDMTWGS+lr5+lcbeN5tOHtQTTQRuJ7UsUm56oQA8Y4isdxvrcXnrlo7rWdsdRCweO4EY2L1mDvoW1kUd+5dhXWjf5z7YDPdb34nGOs1yX0U+cA7MJFCNbvSURERJYMP/YnjY2bgaT/a6N7k0hk395AJOHdk9sP3lNC5Io1ERGR/wN4pUavzUaF3K+ayyZbDjtQN+V1FREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREZFtxr8ADXWHz2v3nzYAAAAASUVORK5CYII=>