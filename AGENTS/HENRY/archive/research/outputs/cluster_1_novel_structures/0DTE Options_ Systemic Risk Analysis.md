# **0DTE Options & Gamma Dynamics \- Research Output**

# **Structural Fragility in the Age of 0DTE: A Systemic Risk Assessment of Short-Dated Option Gamma**

## **Executive Summary**

The financial architecture of the United States equity markets has undergone a radical transformation since 2022, characterized by the unprecedented dominance of Zero Days to Expiration (0DTE) options. As of early 2026, these instruments—options that are listed and expire within a single trading session—constitute approximately 57% to 60% of the total volume in S\&P 500 (SPX) derivatives. This report, commissioned under Priority 1 for the HENRY cluster, provides an exhaustive and granular analysis of the systemic risks introduced by this novel market structure. We find that the migration of liquidity from monthly and quarterly tenors to daily expirations has created a "barbell" risk profile: markets exhibit artificially suppressed volatility during benign regimes due to massive mean-reverting yield harvesting flows, but possess a latent, structural fragility that makes them susceptible to rapid, non-linear dislocations during liquidity shocks.

The comparison to the 1987 "Black Monday" crash is mechanically sound but operationally distinct. Both eras feature potential feedback loops driven by price-insensitive, algorithmic selling—portfolio insurance in 1987 and dealer gamma hedging in 2026\. However, the transmission mechanism has accelerated from minutes to microseconds, and the daily expiration cycle prevents the multi-day accumulation of toxic imbalances that characterized the 1987 collapse.

**Key Findings:**

* **Structural Dominance:** 0DTE SPX options volume averaged 2.3 million contracts daily throughout 2025, surpassing all other maturities combined. This shift is structural, not cyclical, driven by institutional adoption of precise intraday event hedging and systematic yield enhancement strategies.1  
* **The Gamma Paradox:** Contrary to initial regulatory fears, 0DTE volumes have primarily acted as volatility dampeners. The prevalence of institutional option selling (short volatility) positions dealers as net long options (positive gamma), forcing them to buy dips and sell rallies, thereby compressing realized volatility. However, this creates a "volatility paradox" where stability breeds leverage, masking the risk of a sudden regime shift to negative gamma.3  
* **Stress Test Resilience (August 5, 2024):** The market dislocation on August 5, 2024, served as a critical stress test. Amidst a VIX spike to \~65, 0DTE liquidity evaporated rather than exacerbated the crash. Volume in 0DTE contracts dropped to 26% of the total as participants fled to longer-duration hedges. This suggests that the primary systemic risk is not necessarily an explosion of 0DTE volume during a crash, but the sudden withdrawal of liquidity, forcing price discovery back into the underlying futures markets at the worst possible moment.5  
* **Regulatory Gap Closure:** The Options Clearing Corporation (OCC) introduced an "Intraday Risk Charge" in September 2025, acknowledging that legacy end-of-day margining models were structurally incapable of capturing the risk of positions that open and close within a single session. This underscores the material risk of a clearing member default driven by intraday 0DTE exposure.6

The following report details the mechanics of this ecosystem, assesses the probability of cascading feedback loops, and provides a framework for ongoing surveillance.

## ---

**1\. Scale & Growth**

The evolution of the US options market from a monthly hedging venue to a daily transactional ecosystem represents a fundamental shift in market microstructure. The "financialization of time" has reached its theoretical endpoint: the daily reset.

### **1.1 The Trajectory of Volume and Market Share (2020–2026)**

The growth of 0DTE options has been exponential, driven by regulatory changes in listing cadences and a feedback loop of liquidity begetting liquidity.

**Historical Context:**

Prior to 2022, options on the S\&P 500 (SPX) had weekly expirations (Monday, Wednesday, Friday). In 2022, Cboe Global Markets completed the calendar by adding Tuesday and Thursday expirations, enabling a 0DTE trade every single day of the week. This structural change unlocked massive latent demand for daily hedging and speculation.

**Volume Analysis:**

By the close of 2025, the dominance of 0DTE was absolute.

* **Daily Notional Volume:** The notional value traded in 0DTE options fluctuates but frequently exceeds **$1 trillion** daily. This figure dwarfs the underlying cash volume of the S\&P 500 constituents, signaling that the "tail" (derivatives) now wags the "dog" (spot market) intraday.  
* **Contract Volume:** In 2025, SPX 0DTE options averaged **2.3 million contracts daily**. This represents a staggering 59% of the total SPX options volume, up from approximately 40-45% in 2022\.1  
* **Record Activity:** On October 10, 2025, the market set an all-time record with **110 million contracts** traded across all U.S. listed options, with 0DTE SPX contracts serving as the primary engine of this liquidity event.1

**Table 1: Evolution of SPX 0DTE Market Share**

| Year | Avg. Daily Volume (Contracts) | % of Total SPX Volume | Structural Milestone |
| :---- | :---- | :---- | :---- |
| **2020** | \~400,000 | \< 10% | Friday Expirations dominate; Niche strategy. |
| **2021** | \~850,000 | \~20% | Growth of Mon/Wed Expirations. |
| **2022** | \~1,200,000 | \~42% | **Full Daily Expirations** (Tue/Thu added). The "0DTE Era" begins. |
| **2023** | \~1,600,000 | \~46% | Institutional adoption for CPI/FOMC hedging. |
| **2024** | \~2,100,000 | \~53% | Systematization of 0DTE strategies by hedge funds. |
| **2025** | **2,300,000** | **59%** | Saturation point; 0DTE becomes the primary liquidity venue.1 |

This growth trajectory suggests that 0DTE is not a cyclical phenomenon tied to a bear or bull market, but a permanent structural feature. The liquidity gravity is so strong that traders *must* utilize 0DTE to execute large size with minimal slippage, reinforcing the volume concentration.

### **1.2 Participant Analysis: Who is Driving the Flow?**

A critical component of systemic risk analysis is understanding the sophisticatedness and capitalization of the participants. A market driven purely by retail speculation (like the "meme stock" era) behaves differently than one driven by institutional hedging.

**Institutional Dominance (The "Vol Suppression" Cohort):**

Contrary to the popular narrative of "degenerate gamblers," institutional flows are the primary driver of the structural shift.

* **Yield Harvesting:** Asset managers and systematic volatility funds extensively use 0DTEs to sell premium. Strategies like "Iron Condors" (selling both out-of-the-money puts and calls) allow funds to harvest the rapid time decay (Theta) of daily options. Because these funds are *selling* options, dealers are *buying* them, positioning dealers with **positive gamma** (long options). This institutional selling pressure is a key reason why VIX has remained structurally suppressed; every rally is sold (calls), and every dip is bought (puts) by volatility harvesters.8  
* **Event Hedging:** Institutions now prefer 0DTE options to hedge specific binary risks (e.g., an employment report or Fed decision). Buying a 30-day put to hedge a 1-hour event is capital inefficient. 0DTEs allow for "surgical" hedging—paying only for the hours of risk required.

**Retail Participation (The "convexity" Cohort):** Retail traders remain a significant, though likely minority, force in notional terms, estimated at **40-53% of contract volume** depending on the broker data analyzed.10

* **Behavior:** Retail flow is typically directional (buying calls or puts) and often net long gamma (buying options).  
* **Impact:** While smaller in individual size, the aggregate retail herd can create massive "gamma swarms" at specific psychological strike prices (e.g., SPX 5500), forcing dealers to hedge aggressively at those levels.11

### **1.3 Intraday Open Interest and Liquidity Patterns**

The "lifecycle" of a 0DTE option is compressed into 6.5 hours, creating a unique intraday rhythm that differs from traditional markets.

* **09:30 AM \- 10:15 AM (The Build):** Volume explodes at the open. This is when institutional "yield harvesting" strategies are typically deployed (selling the daily range). Open interest (OI) builds rapidly.  
* **10:15 AM \- 2:30 PM (The Decay):** A period of relative stability where Theta (time decay) is the primary driver. If the market remains within the "expected move," implied volatility tends to crush, profiting the option sellers.  
* **2:30 PM \- 4:00 PM (The Gamma Zone):** The most dangerous window. As options approach expiration, their Gamma (sensitivity to price) becomes asymptotic. An option that is slightly Out-of-the-Money (OTM) can flip to deep In-the-Money (ITM) with a 0.2% market move.  
* **3:45 PM (The Clearing Cliff):** Most retail brokerages and risk desks force the closure of 0DTE positions 15 minutes before the bell to avoid "pin risk" or assignment (though SPX is cash-settled, risk models still flag it). This creates a mechanical wave of closing volume that can reverse intraday trends.12

## ---

**2\. Mechanics of Gamma Exposure (GEX)**

To understand why 0DTEs pose a systemic risk, one must understand the mechanical hedging obligations they impose on the market makers (dealers) who facilitate the trades. This is governed by **Gamma Exposure (GEX)**.

### **2.1 Gamma: The Acceleration of Risk**

In option pricing theory (Black-Scholes), **Delta** (![][image1]) measures how much an option's price changes for a ![][image2]\\Gamma$) measures how much the *Delta* changes for a $1 change in the underlying.

* **High Gamma \= Instability:** High gamma means the dealer's hedge ratio is changing rapidly. They must trade *more* volume to stay hedged.  
* **The 0DTE Multiplier:** Gamma is inversely proportional to the time remaining until expiration.  
  ![][image3]  
  As ![][image4] (expiration approaches), ![][image5] for At-The-Money (ATM) options.  
  * *Implication:* A 0DTE option has significantly higher gamma than a 30-day option. A market dominated by 0DTEs requires exponentially more hedging activity for the same price movement than a market dominated by monthly options.13

### **2.2 Delta Hedging: The Engine of Mechanical Flow**

Market makers generally do not take directional bets. Their goal is to capture the bid-ask spread and remain "delta neutral" (flat directionally). To do this, they trade the underlying asset (S\&P 500 futures, ES) against their option book.

* **The Stabilizing Loop (Positive Gamma):**  
  * *Condition:* Dealers are **Long Options** (e.g., they bought calls/puts from institutions selling income strategies).  
  * *Mechanism:* When dealers own options, their position gets *longer* as the market rises (Delta increases). To stay neutral, they must **sell futures**. Conversely, as the market falls, their position gets *shorter* (Delta decreases). To stay neutral, they must **buy futures**.  
  * *Result:* Dealers **buy dips and sell rips**. This suppresses volatility and creates mean-reversion. This is the dominant regime in 2024-2025.3  
* **The Destabilizing Loop (Negative Gamma):**  
  * *Condition:* Dealers are **Short Options** (e.g., they sold puts to hedgers fearing a crash).  
  * *Mechanism:* When dealers are short options, they get *shorter* as the market falls (short puts go ITM). To hedge, they must **sell futures** into the decline. As the market rises, they get *longer* (short calls go ITM). To hedge, they must **buy futures** into the rally.  
  * *Result:* Dealers **sell dips and buy rips**. This accelerates volatility and creates "runaway" trends. This is the condition necessary for a crash.4

### **2.3 The "Gamma Squeeze"**

A gamma squeeze occurs in a **Negative Gamma** regime.

1. Speculators buy massive amounts of OTM calls (forcing dealers short calls).  
2. The stock price rises.  
3. The Delta of the short calls held by dealers increases rapidly (due to high Gamma).  
4. Dealers are forced to buy the underlying stock/futures to hedge their short call exposure.  
5. This buying pushes the price higher, increasing the Delta further.  
6. *Loop repeats.*

While associated with meme stocks, this dynamic applies to the S\&P 500 on 0DTE timescales. If the market gaps down, putting dealers "offside" on short put positions, their mechanical selling can trigger a downside gamma squeeze (or "gamma slide").15

### **2.4 Second-Order Greeks: Vanna and Charm**

In the ultra-short duration of 0DTE, Delta and Gamma are not the only drivers. Two "second-order" Greeks play a massive role in intraday flows.

* **Charm (Delta Decay):** The sensitivity of Delta to the passage of time.  
  * *Mechanism:* As the day progresses, OTM options lose Delta (decay to 0\) while ITM options gain Delta (decay to 1). Dealers must hedge this drift.  
  * *0DTE Impact:* On a quiet day, Charm flows create a natural "drift" that can support markets into the close as dealers unwind hedges associated with OTM puts.17  
* **Vanna (Vol Sensitivity):** The sensitivity of Delta to changes in Implied Volatility (IV).  
  * *Mechanism:* When IV drops, the probability of OTM options finishing ITM drops. Their Delta shrinks.  
  * *0DTE Impact:* After a "clearing event" (like a Fed meeting), IV crushes. Dealers who were short puts see the Delta of those puts shrink. They can buy back the short futures hedges they held. This **"Vanna Rally"** is a powerful force that often drives markets higher after news events, independent of fundamentals.18

## ---

**3\. Dealer Positioning Dynamics**

The market structure has evolved into a game of identifying where the dealers are positioned. Are they the "shock absorbers" (Positive Gamma) or the "accelerant" (Negative Gamma)?

### **3.1 The "Gamma Flip" Level**

Analysts use real-time data to calculate the **Gamma Flip Level** (or Zero Gamma Level)—the price of the S\&P 500 at which dealer positioning switches from positive to negative.

* **Above the Flip:** Dealers dampen volatility. Markets are "sticky" and mean-reverting.  
* **Below the Flip:** Dealers amplify volatility. Markets become "slippery" and prone to large directional moves.  
* **HENRY Monitoring:** Tracking the S\&P 500 relative to this level is arguably the single most important metric for assessing intraday crash risk. If the SPX gaps below the Gamma Flip level, the "safety net" of dealer bid-support is removed.19

### **3.2 The "Pinning" Phenomenon at Key Strikes**

A unique feature of the 0DTE landscape is the "pin."

* **Mechanism:** When Open Interest is massive at a specific strike (e.g., 5500 Call/Put straddles), and dealers are net long gamma, any move away from 5500 triggers hedging that pushes the price *back* to 5500\.  
  * Price goes to 5510 \-\> Dealers sell futures \-\> Price drops to 5500\.  
  * Price drops to 5490 \-\> Dealers buy futures \-\> Price rises to 5500\.  
* **Consequence:** The market often trades in a incredibly tight range around a "Strike of Interest" until the very end of the day.  
* **Risk:** This creates a false sense of security. The "Pin" holds only as long as dealers have the capacity to absorb flow. If a large external seller overwhelms the pin, the snap-back can be violent as all those hedges are unwound simultaneously.20

### **3.3 Liquidity Fractals and the "Gamma Hour"**

Liquidity is not constant. In the 0DTE era, liquidity follows a U-shaped curve, but fragility follows an inverted U-shape.

* **Mid-Day Stability:** High liquidity, low gamma risk (relatively).  
* **The Gamma Hour (3:00 PM \- 4:00 PM):** This is the window of maximum fragility. Dealer gamma is highest (as ![][image4]). A small move here necessitates massive hedging volume.  
* **Negative Convexity:** If a shock happens at 3:30 PM, the "Gamma Trap" is most potent. Dealers have almost no time to recover, and their hedging demands can overwhelm the available liquidity in the futures order book. This is the specific timeframe where a "Flash Crash" is most likely to initiate.12

## ---

**4\. 1987 Portfolio Insurance Comparison**

The comparison between 0DTE options and the Portfolio Insurance strategies of 1987 is central to the systemic risk thesis. While the *mechanism* of feedback loops is similar, the *structure* and *speed* act as key differentiators.

### **4.1 1987: The Analog Era of Algorithmic Destruction**

In 1987, institutional investors utilized "Portfolio Insurance"—a dynamic hedging strategy designed to replicate a Put option synthetically.

* **The Algo:** "If the market drops by X%, sell Y% of the portfolio in S\&P 500 futures to hedge."  
* **The Execution:** Trades were executed via the **DOT (Designated Order Turnaround)** system and telephone.  
* **The Crash Dynamics:**  
  1. Market opened lower on Oct 19 due to weekend news.  
  2. Portfolio Insurance models signaled "Sell."  
  3. Orders flooded the floor.  
  4. Market makers (Specialists) were overwhelmed and stepped away/widened spreads.  
  5. Prices gapped down.  
  6. *Crucially:* The models were "path dependent." The lower it went, the more they *had* to sell.  
  7. The loop took hours/days to fully capitulate because execution lagged signal.22

### **4.2 2026: The Digital Era of Gamma Fragility**

* **The Algo:** Dealer risk engines calculating Delta/Gamma in real-time.  
* **The Execution:** High-Frequency Trading (HFT) algorithms executing in microseconds.  
* **The Crash Dynamics:**  
  1. Market gaps down.  
  2. Dealers (Short Gamma) must sell futures to hedge.  
  3. HFT liquidity providers sense toxic flow and pull quotes.  
  4. Price gaps down.  
  5. *Loop repeats immediately.*

### **4.3 Detailed Comparison Table**

**Table 2: Systemic Risk Comparison \- 1987 vs. 2026**

| Feature | 1987 Portfolio Insurance | 2026 0DTE Gamma Hedging | Comparison |
| :---- | :---- | :---- | :---- |
| **Primary Driver** | Synthetic Puts (Dynamic Hedging) | Dealer Short Gamma (Hedging OTM Puts) | **Similar:** Both involve price-insensitive, mechanical selling into weakness. |
| **Accumulation** | Multi-day accumulation of imbalance. | **Intraday only.** Positions expire at 4:00 PM. | **Difference:** 0DTEs act as a "pressure release valve" daily. Risk does not compound overnight like in 1987\. |
| **Latency** | Minutes to Hours (Human/DOT). | Microseconds (HFT). | **Difference:** Modern crashes are faster but potentially shallower due to automated circuit breakers. |
| **Feedback Loop** | Sell Futures \-\> Market Down \-\> Sell More. | Sell Futures \-\> Market Down \-\> Delta drops \-\> Sell More. | **Identical:** The core feedback loop is mathematically the same. |
| **Visibility** | Opaque (Traders didn't know the size). | **Transparent.** GEX levels are calculable in real-time. | **Difference:** The market can "front-run" the gamma levels today, anticipating the squeeze. |
| **Settlement** | Physical/Futures basis disconnect. | **Cash Settlement (SPX).** No delivery mess. | **Difference:** 1987 saw a breakdown between cash and futures. SPX cash settlement simplifies the "plumbing." |
| **Circuit Breakers** | None effective. | **Rule 80B (MWCB).** | **Mitigant:** Hard halts at \-7%, \-13%, \-20% prevent a continuous 22% drop in one session. |

**Synthesis:** The "1987 Scenario" for 0DTE is likely bounded. While the *acceleration* could be faster than 1987, the **Circuit Breakers** and the **Daily Expiration** act as firebreaks. We are unlikely to see a 20% drop in a single day purely from 0DTE, but we could see a 5-7% "Flash Crash" that triggers a halt, followed by a chaotic reset.22

## ---

**5\. Stress Scenario Analysis**

To operationalize this research, we model specific stress scenarios relevant to HENRY's risk mandate.

### **5.1 Scenario A: The "Gap Down" (Volmageddon 2.0)**

* **Setup:** An exogenous shock (Geopolitical/Macro) causes SPX to gap down **\-2.5%** at the open.  
* **Dealer State:** Dealers are Short Puts (Negative Gamma) with huge OI at strikes just below the open.  
* **The Cascade:**  
  * **09:30:00:** Market opens \-2.5%. Millions of 0DTE puts written at strikes \-1% and \-2% are instantly deeply ITM.  
  * **09:30:01:** Dealer risk engines calculate massive negative delta. They need to sell $30B of futures *now*.  
  * **09:30:05:** This "market sell" order hits the book. Liquidity providers (HFTs) detect the toxicity and widen spreads or pull bids.  
  * **09:30:10:** The market drops another 0.5% on the dealer selling.  
  * **09:31:00:** The "Gamma Flip" is breached. Dealers are now accelerating the move. New strikes come into play.  
  * **Outcome:** A rapid slide to **\-4% or \-5%**, potentially triggering the Level 1 Circuit Breaker (-7%).  
  * **Systemic Risk:** Liquidity evaporation disrupts ETF pricing and broader collateral valuation.

### **5.2 Scenario B: The "Melt-Up" (Vanna Rally)**

* **Setup:** SPX rallies into a resistance level on a day with a macro event (e.g., CPI).  
* **Dealer State:** Dealers are Long Calls and Short Puts.  
* **The Mechanism:**  
  * Event passes \-\> Implied Volatility (IV) crushes.  
  * **Vanna Flow:** The drop in IV reduces the delta of the OTM puts dealers were short. They buy back their short futures hedges.  
  * **Gamma Flow:** As price rises, dealers (long calls) might sell into strength (dampening), *BUT* if they are short upside calls (common in call overwriting), they must buy.  
  * **Outcome:** A "grind up" where the market refuses to tick down. Every tick lower is met with Vanna buying.  
  * **Systemic Risk:** Asset bubbles and forced chasing by active managers, leading to fragility later.

### **5.3 Case Study Analysis: August 5, 2024 (The Carry Trade Crash)**

The events of August 5, 2024, provide the most important empirical data point for this study. The VIX spiked to \~65 pre-market, and SPX futures were limit down.

* **The 0DTE Behavior:** Instead of exacerbating the crash, **0DTE volume collapsed**.  
  * Volume dropped to **26%** of total SPX volume (vs \~50% average).5  
* **Why?**  
  * **Pricing Out:** With VIX at 65, option premiums were astronomically expensive. The "lottery ticket" was no longer cheap.  
  * **Liquidity Withdrawal:** Market makers widened spreads so much that retail could not trade efficiently.  
  * **Flight to Duration:** Institutional hedgers realized a 6-hour option is useless for a multi-day systemic crisis (Yen unwind). They bought monthly/quarterly puts instead.  
* **Implication:** This contradicts the "Doom Loop" theory. In a *true* crisis, the 0DTE market may self-immolate and cease to be the primary driver, passing the baton of risk back to the futures and spot markets. The 0DTE market is a "fair weather" fragility engine; in a storm, it shuts down.

## ---

**6\. Regulatory Status & Structural Reforms**

Regulators have moved from passive observation to active infrastructure hardening.

### **6.1 The OCC Intraday Risk Charge (Rule SR-OCC-2024-010)**

Implemented in September 2025, this is the most critical regulatory change.

* **The Issue:** The OCC (central counterparty) previously calculated margin based on *end-of-day* positions. A clearing member could blow up their account with 0DTEs at 11:00 AM, but the OCC wouldn't margin them until 4:00 PM.  
* **The Rule:** The OCC now implements **intraday margin calls** and an "Intraday Risk Charge." It can call for collateral *during the session* if a member's risk exceeds thresholds driven by 0DTE activity.  
* **Impact:** This dramatically reduces the risk of a Clearing Member Default (a Lehman-style event at the clearing house). However, it imposes higher liquidity costs on broker-dealers, who may pass this on by restricting leverage during volatile days.6

### **6.2 Regulatory Sentiment (SEC/CFTC)**

* **SEC:** Chairman Atkins (in the 2025 context) and the Division of Trading and Markets have focused on ensuring exchange capacity and clearing resilience rather than banning the product. They view 0DTE as a valid hedging tool if margined correctly.25  
* **CFTC:** Has expressed concern about the "blurring" of lines between regulated futures and securities options, monitoring the cross-market impact on E-mini S\&P futures liquidity.26  
* **Bank of International Settlements (BIS):** Released a bulletin warning that 0DTEs allow leverage to hide in the "shadows" of intraday timeframes, invisible to overnight regulatory reporting.27

## ---

**7\. Monitoring Recommendations**

HENRY requires a dedicated "Intraday Liquidity & Gamma" module to monitor these risks. End-of-day data is obsolete for this asset class.

### **7.1 Metrics to Track (The "Gamma Dashboard")**

| Metric | Definition | Signal | Source |
| :---- | :---- | :---- | :---- |
| **Net Gamma Exposure (GEX)** | Total $ value of dealer gamma per 1% move. | **Negative:** High Crash Risk. **Positive:** Low Risk. | SpotGamma / Tier1Alpha |
| **Gamma Flip Level** | The SPX price where Net GEX \= 0\. | **Price \< Flip:** Enter defensive posture. | SpotGamma / MenthorQ |
| **0DTE Volume Ratio** | 0DTE Vol / Total SPX Vol. | **\>65%:** Overheated/Speculative. **\<30%:** Fear/Liquidity Dry-up. | Cboe DataShop |
| **VIX1D vs. VIX** | Spread between 1-day and 30-day Vol. | **Inversion (1D \> 30D):** Immediate intraday stress. | Cboe Global Markets |
| **HIRO Indicator** | Hedging Impact of Real-time Options. | Real-time visualization of dealer buying/selling pressure. | SpotGamma 28 |
| **DIX (Dark Index)** | Dark Pool Buying vs. Selling. | Divergence between DIX and Price often precedes corrections. | SqueezeMetrics 29 |

### **7.2 Data Sources & URLs**

* **SpotGamma:** Essential for the "Gamma Flip" and HIRO.  
  * *URL:* [https://spotgamma.com](https://spotgamma.com) 30  
* **SqueezeMetrics:** For GEX and Dark Pool data.  
  * *URL:* [https://squeezemetrics.com/monitor](https://squeezemetrics.com/monitor) 31  
* **Cboe DataShop:** For raw exchange data and Volume statistics.  
  * *URL:* [https://datashop.cboe.com](https://datashop.cboe.com) 32  
* **Option Alpha:** For retail-accessible visualizations.  
  * *URL:* [https://optionalpha.com](https://optionalpha.com) 33

## ---

**Key Risks Identified (Ranked)**

1. **Intraday Liquidity Cascade:** A \-3% shock triggers negative gamma hedging that overwhelms HFT liquidity, causing a "Flash Crash" to circuit breakers before humans can react.  
2. **Clearing Member Intraday Default:** A prime broker or clearing firm fails to meet an OCC intraday margin call during a volatility spike, threatening the central counterparty (mitigated by new OCC rules, but still a nonzero tail risk).  
3. **The "Volatility Trap":** Prolonged suppression of volatility by positive gamma flows blinds risk models (VaR) to the true potential for movement, leading to excessive leverage in the broader system (e.g., Basis Trade, Volatility Targeting Funds).  
4. **Operational Bandwidth Failure:** The exponential rise in quote traffic required to update 0DTE prices in microseconds could cause latency or outages in exchange matching engines during peak stress.

## **Sources**

1

#### **Works cited**

1. The State of the Options Industry: 2025 \- Cboe Global Markets, accessed January 26, 2026, [https://www.cboe.com/insights/posts/the-state-of-the-options-industry-2025](https://www.cboe.com/insights/posts/the-state-of-the-options-industry-2025)  
2. The State of the Options Industry: 2025 \- Cboe Global Markets, accessed January 26, 2026, [https://www.cboe.com/insights/posts/the-state-of-the-options-industry-2025/](https://www.cboe.com/insights/posts/the-state-of-the-options-industry-2025/)  
3. SpotGamma Levels Reveal Dealer Positioning \- LuxAlgo, accessed January 26, 2026, [https://www.luxalgo.com/blog/spotgamma-levels-reveal-dealer-positioning/](https://www.luxalgo.com/blog/spotgamma-levels-reveal-dealer-positioning/)  
4. How Gamma Exposure Works: Unraveling the Dynamics of Risk Hedging \- Medium, accessed January 26, 2026, [https://medium.com/@thegeeksoffinance/how-gamma-exposure-works-unraveling-the-dynamics-of-risk-hedging-76382c10f19a](https://medium.com/@thegeeksoffinance/how-gamma-exposure-works-unraveling-the-dynamics-of-risk-hedging-76382c10f19a)  
5. Zero-day options and financial market vulnerability – Bank ..., accessed January 26, 2026, [https://bankunderground.co.uk/2024/12/04/zero-day-options-and-financial-market-vulnerability/](https://bankunderground.co.uk/2024/12/04/zero-day-options-and-financial-market-vulnerability/)  
6. Intraday Risk Charge, accessed January 26, 2026, [https://infomemo.theocc.com/infomemos?number=56867](https://infomemo.theocc.com/infomemos?number=56867)  
7. Cboe Global Markets Reports Trading Volume for December and Full Year 2025, accessed January 26, 2026, [https://ir.cboe.com/news/news-details/2026/Cboe-Global-Markets-Reports-Trading-Volume-for-December-and-Full-Year-2025/default.aspx](https://ir.cboe.com/news/news-details/2026/Cboe-Global-Markets-Reports-Trading-Volume-for-December-and-Full-Year-2025/default.aspx)  
8. Record 0DTE volume reshapes the S\&P 500 | SpotGamma Weekly, accessed January 26, 2026, [https://spotgamma.com/record-0dte-volume-reshapes-the-sp-500/](https://spotgamma.com/record-0dte-volume-reshapes-the-sp-500/)  
9. Henry Schwartz's Zero-Day SPX® Iron Condor Strategy: A Deep Dive \- Cboe Global Markets, accessed January 26, 2026, [https://www.cboe.com/insights/posts/henry-schwartzs-zero-day-spx-iron-condor-strategy-a-deep-dive/](https://www.cboe.com/insights/posts/henry-schwartzs-zero-day-spx-iron-condor-strategy-a-deep-dive/)  
10. SPX® 0DTE Options Jump to Record 62% Share in August | Cboe, accessed January 26, 2026, [https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august/](https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august/)  
11. How retail traders drive record options volumes \- FinTech Global, accessed January 26, 2026, [https://fintech.global/2025/10/23/how-retail-traders-drive-record-options-volumes/](https://fintech.global/2025/10/23/how-retail-traders-drive-record-options-volumes/)  
12. Same-Day Options, Same-Day Alpha? Institutional Lessons from 0DTE's Boom | Resonanz Capital, accessed January 26, 2026, [https://resonanzcapital.com/insights/same-day-options-same-day-alpha-institutional-lessons-from-0-dtes-boom](https://resonanzcapital.com/insights/same-day-options-same-day-alpha-institutional-lessons-from-0-dtes-boom)  
13. What Is Gamma Exposure? An In-Depth Analysis for Traders \- Cheddar Flow, accessed January 26, 2026, [https://www.cheddarflow.com/blog/what-is-gamma-exposure-an-in-depth-analysis-for-traders/](https://www.cheddarflow.com/blog/what-is-gamma-exposure-an-in-depth-analysis-for-traders/)  
14. Understanding 0DTE Gamma Exposure Guide \- MenthorQ, accessed January 26, 2026, [https://menthorq.com/guide/understanding-0dte-gamma-exposure/](https://menthorq.com/guide/understanding-0dte-gamma-exposure/)  
15. Understanding Gamma Squeeze vs. Short Squeeze: A Deep Dive \- Oreate AI Blog, accessed January 26, 2026, [https://www.oreateai.com/blog/understanding-gamma-squeeze-vs-short-squeeze-a-deep-dive/025f58ea02da29ba4fff7d9b6bb35a03](https://www.oreateai.com/blog/understanding-gamma-squeeze-vs-short-squeeze-a-deep-dive/025f58ea02da29ba4fff7d9b6bb35a03)  
16. Short Squeeze and Gamma Squeeze Guide \- MenthorQ, accessed January 26, 2026, [https://menthorq.com/guide/short-squeeze-and-gamma-squeeze/](https://menthorq.com/guide/short-squeeze-and-gamma-squeeze/)  
17. Charm and Vanna: OTM vs ITM Puts Guide \- MenthorQ, accessed January 26, 2026, [https://menthorq.com/guide/charm-and-vanna-otm-vs-itm-puts/](https://menthorq.com/guide/charm-and-vanna-otm-vs-itm-puts/)  
18. Options Vanna & Charm | SpotGamma™, accessed January 26, 2026, [https://spotgamma.com/options-vanna-charm/](https://spotgamma.com/options-vanna-charm/)  
19. GEX Profile \[Lite\] Real Auto-Updated Gamma Exposure Levels \- TradingView, accessed January 26, 2026, [https://www.tradingview.com/script/2iIjQYTo-GEX-Profile-Lite-Real-Auto-Updated-Gamma-Exposure-Levels/](https://www.tradingview.com/script/2iIjQYTo-GEX-Profile-Lite-Real-Auto-Updated-Gamma-Exposure-Levels/)  
20. What Are 0DTE Options? Learn the Basics \- Charles Schwab, accessed January 26, 2026, [https://www.schwab.com/learn/story/zeroing-on-0dte-options-learn-basics](https://www.schwab.com/learn/story/zeroing-on-0dte-options-learn-basics)  
21. Pinning the Strike: Meaning, Example, FAQs \- Investopedia, accessed January 26, 2026, [https://www.investopedia.com/terms/p/pinningthestrike.asp](https://www.investopedia.com/terms/p/pinningthestrike.asp)  
22. How "0DTE" Options Will Cause the Next Black Monday \- Articles \- Advisor Perspectives, accessed January 26, 2026, [https://www.advisorperspectives.com/articles/2023/02/01/how-0dte-options-will-cause-the-next-black-monday](https://www.advisorperspectives.com/articles/2023/02/01/how-0dte-options-will-cause-the-next-black-monday)  
23. Portfolio Insurance and Other Investor Fashions as Factors in the 1987 Stock Market Crash \- National Bureau of Economic Research, accessed January 26, 2026, [https://www.nber.org/system/files/chapters/c10958/c10958.pdf](https://www.nber.org/system/files/chapters/c10958/c10958.pdf)  
24. Research Update: Options Clearing Corp. 'AA' Rati | S\&P Global Ratings, accessed January 26, 2026, [https://www.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/3500780](https://www.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/3500780)  
25. SEC and CFTC Staff Issue Joint Statement on Trading of Certain Spot Crypto Asset Products, accessed January 26, 2026, [https://www.sec.gov/newsroom/press-releases/2025-110-sec-cftc-staff-issue-joint-statement-trading-certain-spot-crypto-asset-products](https://www.sec.gov/newsroom/press-releases/2025-110-sec-cftc-staff-issue-joint-statement-trading-certain-spot-crypto-asset-products)  
26. Shifting Enforcement Priorities at the CFTC and the SEC \- Foley & Lardner LLP, accessed January 26, 2026, [https://www.foley.com/insights/publications/2026/01/shifting-enforcement-priorities-at-the-cftc-and-the-sec/](https://www.foley.com/insights/publications/2026/01/shifting-enforcement-priorities-at-the-cftc-and-the-sec/)  
27. Anatomy of the VIX spike in August 2024 \- Bank for International Settlements, accessed January 26, 2026, [https://www.bis.org/publ/bisbull95.pdf](https://www.bis.org/publ/bisbull95.pdf)  
28. How to Use The SpotGamma HIRO Indicator, accessed January 26, 2026, [https://spotgamma.com/how-to-use-spotgamma-hiro-indicator/](https://spotgamma.com/how-to-use-spotgamma-hiro-indicator/)  
29. Dark Index \- sqzme, accessed January 26, 2026, [https://squeezemetrics.com/monitor/dix](https://squeezemetrics.com/monitor/dix)  
30. All About 0DTE Options | SpotGamma™, accessed January 26, 2026, [https://spotgamma.com/0dte/](https://spotgamma.com/0dte/)  
31. sqzme | Fresh perspectives on stock data, accessed January 26, 2026, [https://squeezemetrics.com/](https://squeezemetrics.com/)  
32. Historical Options Data Download \- Cboe Global Markets, accessed January 26, 2026, [https://www.cboe.com/us/options/market\_statistics/historical\_data/](https://www.cboe.com/us/options/market_statistics/historical_data/)  
33. What's New in Option Alpha: December 2025, accessed January 26, 2026, [https://optionalpha.com/blog/whats-new-in-option-alpha-december-2025](https://optionalpha.com/blog/whats-new-in-option-alpha-december-2025)  
34. Zero-day options (0DTE) Start 2025 Off with a Bang | Numerix, accessed January 26, 2026, [https://www.numerix.com/resources/blog/zero-day-options-0dte-start-2025-bang](https://www.numerix.com/resources/blog/zero-day-options-0dte-start-2025-bang)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAYCAYAAADzoH0MAAAAv0lEQVR4Xu3SsQpBURzH8aMYlLKZ3MHMC1iV8gCKFxCDzQvcxCbTXYwm5Sk8hPICNoNN3UH8ftePdHQ5dSbyrc9y/vWvczrG/GwZGUPDmjlVlQOsISfOjWQJJ6iLc14LAphIGXYQCd/lYz1oCgvhKDWdpVaCOeSFVWAvoc5S817Qked47/sbcAkXvlSQGRStGePdie8wtGZJLenbA5WVFWzN7ar0yGsBv+hCBtB+Ywpn6EoSf1gsF0cb4bv9+/6uWvIz6j0umUwAAAAASUVORK5CYII=>

[image2]: <data:image/png;base64,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>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAAvCAYAAABexpbOAAACxUlEQVR4Xu3dO6tUVxiA4aXijYiIiBcSr7GJoBFEG4vEMohirBQhROMFBLVSiSa1lzJBSVIoFvEfJJAm2IhGCxFsRSxiQAt/geD3sWbMdmfEc46TOVvO88DLmdl7w2kXa+21phQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoBNmRlujZe0bAABMvo3R5ejnYsAGANBpO4oBGwBApxmwAQB0nAEbAEDHGbABAHScARsAQEetin6K/o7uRiejOc0HAACmuhwc5czWoAAA6IAPo+PRP9GTaF90KXocTWs8BwDAJLsW3Wh8Xx7Na3wHAGCStQdsaW7re5oRbY9ORPMb178v3j8DAPhfDRqwDXIsOhRdj+5HK6Mt0ermQwAADN9YBmyLSn3fLd9tyx9svxo9iP5oPjTArujikPq2AABMUWMZsG2Kdja+r4oeRmca1wb5fMgBAExJYxmw5Tttp3p/c4btu2hv9Eu0sPHcRC2JVrylYfwfAID3ysboz+hFr29ev/0fn5Z60O3t6Gipy6MflHokyNnybpsOctPCubf05aunAQB4o9wpmjNsTXkEyILWtfGYVepsHQAAHTQ92tb7fCR6WuoS7aPoWambG26VumTrbDgAgEmQmxkOl7qc+mOpmxnSb9GvpS67roku9K4DADBin0VfR5+Ues5bX/5cVs64pXx3rv8ZAIARyk0PB6N10dJSz3rrex5t7n3O3aGLG/cAABiyHGzlMSDtM9v2Rxta11Iuj/aXQwEAGIG10e7o91Jn1fpywJY7RNvynTVLoAAAIzS71B+LvxOd7l3Ld9Y+fvXE674o/y6HAgAwQnuim9EPpc64NeU5buejv0o9xDf/5mG673IYLwAA45Szanmu2r3oq9Y9AAA6IGfLDkRXovWtewAAdMRHpZ6rlu+1AQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAT8RL101qxIaRT4wAAAABJRU5ErkJggg==>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADYAAAAYCAYAAACx4w6bAAABqElEQVR4Xu2WvytFYRjHH0URkixMmGRB+ZUyKikWk2KTbFYyKINBGWQUxYBVKYOkGyPlD7AwmWwWE9/veZ/Xfe97zuFet3Pv7Tqf+izPe87pfep5v+8RSUmpKJrUjjytN69VNtzkhfoI9+EJ/FAftHYIX9XV4M3y0Q6P1DN4BadhjRrQC3fUOqf2ps5qjcyrM06t1NTCU7igkjZ4A8fUAC7mFMRs3jbGJi2L6qBTK4Y+td9f+AHu50nMHtx9HMM9NaBqG+sRM4J2DAkX79Rmp96pNji1YuhW18U5G7/AY/Ai2SCzbMFrtdGpf9MK78XrPiHsYV+CQ95aHDzzUY0x0DIqEz6EDQ5+wA2OJOG0bMIJ8ZItgmX5Y2P2fLFB93zlAxNrRcz1UKgZMdeNf3Z84kaR45xR/1djB5INDTc4kmQEbktugMUxLKYxJqmbpkxF/ljQ0Ci7wVEKmK50A7Z4a3HwuVsx55ESfuMSzqkBA2K6pc/wE77Dc3XKPpgA9v60fxD5MinZsRuFa3BXwtdW2eB/qrVQ7I/7OOySiPErJ1XbWEpKSkpl8QVQHGtrRhq0yQAAAABJRU5ErkJggg==>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD4AAAAXCAYAAABTYvy6AAABo0lEQVR4Xu3WzStEURjH8UcIUUSJIi+xshFhoViwkVhggcRS2FCKlFJmY2GlKAt7WVA2XnZW/gQbiYWFjZSVl/g9znNud46ZuXNnjFt3zrc+Td3TxHNfzlwimy1rKoPqJBTqL4SlLtgRn3AB4zAvjuANRvQXwpS+qvewYqxxPPSSeTAMeQ1eAxvmwTSqhV4RaHZwij14HjSbB9OoFDZFkbHmlf5f12EXBiFX6IphSuzDJMX5O16DZ6Ihl2RrJLXZsmFYgBc4F+XQBJcwJgqgFdYgXzgFMXiOmINpir5i8Vok9ZgwXRs8iis4g07Xuq4PeoSTHZxSH5x/+/l58usUbkk9q4kqIXVr6xPmblTwe8g2/V7n+DGZEU5/Mbjf6sQeqc3OK35z5CvOn+ZbJD/X7AHeSZ0Es3aYEE7/PThfkWVRH72UMN6d+TZ238pVcCy6Sd1Fz9AvON7QItAifpqFG/EFr3BCaidkmaiB1An2e5J5gFVxAIdwDR2C45+tLfgQT3AHA7LulLWDBxEPwC8ZLNV4s6ug2BsZp3+zK+XTZrPZwt83xZ1nhj1vyJIAAAAASUVORK5CYII=>