# **SOFR Stress Episodes & Early Warning Indicators: An Exhaustive Analysis of Repo Market Dynamics, Volatility Drivers, and Liquidity Monitoring**

## **1\. The Architecture of Secured Funding: From LIBOR to SOFR**

The transition of the global financial system’s primary reference rate from the unsecured London Interbank Offered Rate (LIBOR) to the Secured Overnight Financing Rate (SOFR) represents more than a mere substitution of benchmarks; it constitutes a fundamental restructuring of the financial plumbing. While LIBOR measured the perceived credit risk of bank-to-bank lending—a market that largely evaporated following the Global Financial Crisis (GFC)—SOFR measures the cost of borrowing cash collateralized by U.S. Treasury securities. It is grounded in the deepest, most liquid securities market in the world, with daily transaction volumes regularly exceeding $1 trillion.

However, this transition has introduced a new paradigm of volatility. Because SOFR is a transaction-based rate derived from the repurchase agreement (repo) market, it is inextricably linked to the supply and demand dynamics of collateral and reserves. Unlike LIBOR, which was often smoothed by expert judgment, SOFR is a "hard" number that reflects every tremor in the underlying plumbing. When the pipes of the financial system clog—whether due to regulatory balance sheet constraints, sudden liquidity drains from the Treasury General Account (TGA), or dealer incapacity—SOFR reacts immediately and, at times, violently.

This report provides a comprehensive, expert-level analysis of SOFR stress episodes, dissecting the mechanics of the repo market, the regulatory constraints that amplify volatility, and the specific historical episodes that define the current liquidity regime. Furthermore, it establishes a robust framework of Early Warning Indicators (EWIs) to support LIQUID’s monitoring of the SOFR-IORB spread, a critical barometer for systemic financial health.

### **1.1 The Tri-Segmented Construction of SOFR**

To effectively monitor SOFR, one must first understand its composition. The rate is not a monolithic figure but a volume-weighted median derived from three distinct segments of the repo market. Stress rarely manifests in all three simultaneously; rather, it typically originates in the bilateral segments before spilling over into the broader metric.

#### **1.1.1 The Tri-Party Repo Market**

The Tri-party market represents the institutional core of the repo ecosystem. In this segment, borrowers (primarily Primary Dealers) and lenders (Money Market Funds, Insurance Companies, Government-Sponsored Enterprises) negotiate trades, but the settlement and collateral management are handled by a third-party clearing bank (Bank of New York Mellon).

This segment is characterized by high operational efficiency but rigid access. Money Market Funds (MMFs), which are the dominant cash lenders in this space, maintain strict counterparty lists. They lend primarily to large, high-credit-quality dealers. Consequently, the Tri-party rate tends to be the most stable and "sticky" of the three segments. It often acts as an anchor for SOFR. However, because MMFs are highly sensitive to yield differentials, massive flows of cash out of the Tri-party market and into Treasury bills (when bill yields rise) can rapidly strip liquidity from dealers, forcing them to scramble for funding elsewhere.

#### **1.1.2 The General Collateral Finance (GCF) Repo Market**

The GCF Repo service, offered by the Fixed Income Clearing Corporation (FICC), serves as the inter-dealer redistribution hub. This is where dealers trade with each other. A dealer with excess cash (perhaps borrowed from an MMF in Tri-party) can lend it to another dealer who is short cash via GCF.

The GCF market plays a critical role in "breaking the bulk." Large dealers aggregate cash from institutional lenders and redistribute it to smaller dealers who may not have direct access to MMF funding. Stress in the GCF market—specifically a widening spread between GCF rates and Tri-party rates—is a classic early warning sign of "segmentation." It indicates that liquidity is trapped at the top of the pyramid (among the largest GSIBs) and is not flowing down to the broader street due to balance sheet constraints or credit line limits.

#### **1.1.3 The Bilateral DVP Repo Market**

The third segment involves bilateral Treasury repo transactions cleared through FICC’s Delivery-versus-Payment (DVP) service. This segment is arguably the most critical for monitoring leverage and risk appetite. It captures the interaction between dealers and a broader array of counterparties, including hedge funds and smaller financial institutions, often facilitated through "Sponsored Repo" programs.

This segment is the "marginal" source of funding. When balance sheets tighten, dealers will protect their strategic relationships in the Tri-party market but may cut off or aggressively re-price liquidity in the bilateral DVP market. Consequently, the DVP rate is often the first to spike during stress events, pulling the weighted-median SOFR higher. The inclusion of this segment makes SOFR sensitive to the leverage deployed by the hedge fund community and the capacity of dealers to intermediate that leverage.

### **1.2 The Mechanics of the Calculation and the "Specials" Filter**

The Federal Reserve Bank of New York calculates SOFR each business day based on transaction data from the previous day. A critical component of this methodology is the filtering of "specials".

In the repo market, a "special" occurs when a specific Treasury security (e.g., the most recently issued 10-year note) is in such high demand that cash lenders are willing to accept a lower interest rate—or even a negative rate—just to obtain that specific security as collateral. Since SOFR is intended to measure the cost of borrowing *cash* against general collateral (GC), not the idiosyncratic scarcity of specific bonds, the Fed removes these transactions.

**Methodology:** The NY Fed arranges all transactions from lowest rate to highest rate. It then removes the bottom 25% of the volume. This "trimming" is designed to cut out the specials, which trade at rates significantly below the general collateral rate.

**Implication for Stress:** In a true liquidity crisis, where the shortage is of *cash* rather than *collateral*, the entire distribution of rates shifts upward. In such scenarios, the "specials" filter becomes irrelevant because even the lowest-rated trades are printing well above the policy rate. However, during periods of "collateral scarcity" (where there is too much cash chasing too few bonds), the trim helps maintain SOFR’s stability. Understanding this distinction is vital: a spike in SOFR means cash is scarce; a plunge in SOFR (or specific repo rates) means collateral is scarce.

---

## **2\. The Monetary Policy Implementation Framework: Floors, Ceilings, and Leaks**

To interpret the SOFR-IORB spread, one must situate it within the Federal Reserve’s monetary policy implementation framework. Since the GFC, the Fed has operated a "floor system" (specifically, a regime of ample reserves), but the mechanics of this system have evolved, particularly with the introduction of the Standing Repo Facility (SRF).

### **2.1 The Anchor: Interest on Reserve Balances (IORB)**

The Interest on Reserve Balances (IORB) is the rate the Federal Reserve pays on balances maintained by eligible institutions (banks) in their master accounts. In theory, IORB acts as a magnet for short-term rates.

* **The Arbitrage Logic:** If the repo rate (SOFR) falls significantly below IORB, banks have an incentive to borrow in the repo market and deposit the cash at the Fed to earn the IORB, thereby pushing the repo rate up. Conversely, if SOFR rises significantly above IORB, banks should lend their excess reserves into the repo market to capture the spread, pushing the repo rate down.  
* **The Reality of Spreads:** In a frictionless market with abundant reserves, SOFR should trade slightly below IORB. This negative spread reflects the fact that IORB is a risk-free, unsecured deposit available only to banks, whereas repo involves collateral and operational costs but is open to a wider range of participants (like MMFs via the ON RRP).  
* **The Stress Signal:** A sustained *positive* spread (SOFR \> IORB) is a definitive signal of friction. It implies that the arbitrage mechanism has broken down. Banks are effectively saying, "We will not lend you cash at IORB \+ 5 basis points because the regulatory cost (SLR, GSIB surcharge) of expanding our balance sheet is greater than that profit margin.".

### **2.2 The Floor: Overnight Reverse Repo (ON RRP)**

The ON RRP facility serves as the "soft floor" for overnight rates. It allows non-bank participants (primarily Money Market Funds and Government-Sponsored Enterprises) to lend cash to the Fed against Treasury collateral.

* **Function:** Because MMFs cannot earn IORB (they are not banks), the ON RRP gives them a risk-free investment option. They will generally not lend cash in the private repo market at rates lower than the ON RRP rate.  
* **Liquidity Buffer:** For much of 2021-2023, the ON RRP balances exceeded $2 trillion. This represented "excess liquidity" in the system—cash that banks didn't want on their balance sheets. As long as the ON RRP has significant balances, the system is in a regime of "abundant" reserves. The drain of the ON RRP (as seen in late 2024 and 2025\) marks the transition to a more fragile "ample" reserves regime.

### **2.3 The Ceiling: Standing Repo Facility (SRF)**

Established permanently in July 2021, the SRF serves as the "ceiling" or backstop for the repo market.

* **Mechanism:** The Fed stands ready to *lend* cash to Primary Dealers and eligible banks against Treasury, Agency, and MBS collateral at an administered rate (the SRF bid rate).  
* **Rate Setting:** The SRF rate is typically set at the top of the Fed’s target range (e.g., if the target is 3.50%-3.75%, the SRF might be set at 3.75%).  
* **The "Leaky" Ceiling:** Crucially, the SRF is not an *absolute* ceiling for SOFR. Why?  
  1. **Access:** Only Primary Dealers and eligible banks can access it. Hedge funds, REITs, and smaller broker-dealers cannot.  
  2. **Intermediation Bottlenecks:** If a Primary Dealer borrows from the SRF at 3.75%, they will only lend to a hedge fund client if they can charge a spread (e.g., 3.85%). If the dealer is balance-sheet constrained (e.g., at year-end), they may refuse to intermediate entirely. Thus, the client is forced to pay higher rates in the bilateral market, pushing SOFR above the SRF rate. This phenomenon, observed in December 2025, is a critical monitoring point.

---

## **3\. The Anatomy of Stress: The September 2019 Liquidity Shock**

To anticipate future stress, we must dissect the archetypal crisis of September 2019\. This event dismantled the assumption that aggregate metrics of liquidity are sufficient to guarantee stability.

### **3.1 Preconditions: The Illusion of Sufficiency**

Leading up to September 2019, the Federal Reserve was engaged in Quantitative Tightening (QT), allowing its Treasury holdings to run off. This mechanically reduced the level of reserves in the banking system from a peak of \~$2.8 trillion in 2014 to approximately $1.45 trillion by August 2019\.

Most policymakers believed $1.45 trillion was "ample." However, this aggregate number concealed a dangerous distribution:

1. **Concentration:** A vast majority of these reserves were held by just a handful of Global Systemically Important Banks (GSIBs).  
2. **Dealer Inventory:** Primary dealer inventories of Treasuries had reached all-time highs. Dealers were "stuffed" with collateral they needed to finance.  
3. **LCR Constraints:** Post-crisis Liquidity Coverage Ratio (LCR) rules required banks to hold High-Quality Liquid Assets (HQLA). While Treasuries count as HQLA, reserves are the most usable form. Banks had internally calibrated their "lowest comfortable level of reserves" (LCLoR) much higher than the Fed realized. They viewed their reserve piles not as excess cash to be lent, but as a mandatory compliance buffer.

### **3.2 The Trigger: The Twin Drain of September 16**

On Monday, September 16, 2019, two events occurred simultaneously, creating a massive liquidity vacuum:

* **Corporate Tax Payments:** It was a quarterly corporate tax deadline. Corporations withdrew roughly $35 billion from bank accounts to pay the Treasury. When taxes are paid, cash moves from the commercial banking system into the Treasury General Account (TGA) at the Fed. This is a direct subtraction of reserves.  
* **Treasury Settlement:** On the same day, a net settlement of approximately $54 billion in new Treasury securities took place. Dealers had to pay for these securities, further draining cash and, critically, adding to the pile of collateral that needed financing in the repo market.

### **3.3 The Dislocation: September 17**

The following morning, the imbalance manifested with shocking velocity:

* **The Spike:** SOFR, which had been trading stably around 2.14%, spiked to **5.25%**. Intraday trades in the bilateral market were reported as high as **9.00%** or **10.00%**.  
* **Spillover:** The stress was so acute it broke the barriers of the secured market. The Effective Federal Funds Rate (EFFR)—the unsecured rate the Fed targets—broke through the top of its target range, reaching 2.30%. This signaled a loss of monetary control.

### **3.4 The Breakdown of Arbitrage**

The most alarming aspect of September 2019 was the behavior of the banks. Despite repo rates offering a massive premium over IORB (spreads of 300-400 basis points), cash-rich banks *did not lend*.

Research by the Office of Financial Research (OFR) and the NY Fed later revealed why:

1. **Intraday Friction:** Banks manage liquidity in real-time. They feared that if they lent cash in the morning repo market, they might not receive incoming payments later in the day, leaving them with an overdraft at the Fed.  
2. **Resolution Liquidity (RLAP):** Internal stress tests mandated by regulators (Resolution Liquidity Adequacy and Positioning) required banks to ring-fence liquidity for hypothetical wind-down scenarios. This "trapped" the liquidity inside the banks.

**Lesson for Monitoring:** Liquidity is not fungible during stress. A dashboard showing $3 trillion in aggregate reserves is useless if the marginal lender faces a regulatory cost to deploy it.

---

## **4\. Structural Amplifiers: The Regulatory Straitjacket**

The recurring nature of SOFR stress—particularly at quarter-ends and year-ends—is a feature, not a bug, of the post-2008 regulatory framework. Three specific regulations act as structural amplifiers of volatility.

### **4.1 The Supplementary Leverage Ratio (SLR)**

The SLR is arguably the most significant constraint on repo market intermediation. Unlike risk-weighted capital requirements, which assign lower capital charges to safe assets like Treasuries, the SLR is a simple leverage ratio. It requires large banks to hold Tier 1 capital equal to at least 5% (for GSIBs) of their *total leverage exposure*.

**The Mechanism of Constraint:**

* Total Leverage Exposure includes all on-balance sheet assets (Reserves, Treasuries, Repo loans) and off-balance sheet exposures.  
* Repo is a high-volume, low-margin business. Dealers borrow billions to lend billions, earning a tiny spread (e.g., 5-10 basis points).  
* However, the SLR requires capital to be held against the *gross* size of the repo book (unless strict netting conditions are met).  
* **The ROI Problem:** Holding 5% capital against a safe government bond trade earning 10bps results in a Return on Equity (ROE) that is often below the bank's cost of capital.

**The "Window Dressing" Cycle:** Because U.S. banks report their SLR snapshots at quarter-ends, they actively shrink their balance sheets in the final days of March, June, September, and December. They refuse to roll over repo trades, pushing borrowers into the market to find alternative funding. This creates the predictable "sawtooth" pattern where SOFR spikes at quarter-ends and normalizes days later.

### **4.2 The GSIB Surcharge and the Year-End Wall**

While SLR affects every quarter, the Global Systemically Important Bank (GSIB) surcharge creates a unique and violent distortion at **year-end**.

**Method 2 Scoring:** U.S. GSIBs are assigned a capital surcharge based on a "Method 2" score, which heavily weights reliance on short-term wholesale funding (like repo). Crucially, this score is calculated based on the **year-end snapshot**.

**The Cliff Effect:**

The surcharge is assessed in "buckets" of 0.5% (e.g., 2.5%, 3.0%, 3.5%). If a bank's year-end score pushes it just one point over a threshold, its capital surcharge increases by 0.5% applied to its *entire* risk-weighted asset base. This can translate to billions of dollars in additional required capital.

* **Behavioral Impact:** To avoid jumping a bucket, GSIBs will aggressively shed repo exposure in late December. They essentially close the shop. This creates a liquidity vacuum exactly when the market needs it most to settle year-end balance sheet adjustments.

### **4.3 Netting and the "Sponsored Repo" Solution**

To mitigate these constraints, the market relies on **netting**. If a dealer borrows $10 billion and lends $10 billion with the same counterparty and maturity, accounting rules allow these positions to cancel out, resulting in zero balance sheet impact.

**Sponsored Repo:** Historically, dealers could net trades with other dealers (via FICC) but not with clients like Money Market Funds or Hedge Funds. The "Sponsored Repo" program allows dealers to sponsor these clients into FICC clearing. This allows a dealer to borrow from an MMF (cleared) and lend to a hedge fund (cleared) and net the two positions, bypassing the SLR constraint.

**The Monitoring Signal:**

The volume of Sponsored Repo is a key indicator of dealer capacity. If Sponsored Repo volumes plateau or decline while spreads widen, it suggests that dealers have hit their gross limits or that the netting mechanism is saturated.

---

## **5\. The Post-Pandemic Cycle: From Abundance to "Elasticity Testing" (2022-2025)**

The period following the COVID-19 pandemic saw the largest accumulation of liquidity in history, followed by a rapid draining cycle that has now brought the market back to the precipice of scarcity.

### **5.1 The ON RRP Buffer (2021-2023)**

By 2022, the Fed’s ON RRP facility held over $2.5 trillion. This massive balance represented "excess" cash that banks turned away. During this period, SOFR was essentially pegged to the ON RRP rate. Spreads were nonexistent. Volatility was dead.

### **5.2 The Great Drain and QT 2.0 (2024-2025)**

As the Fed hiked rates and began Quantitative Tightening (QT), reducing its balance sheet by \~$95 billion per month, the system began to drain.

* **The "Crowding In" Phase:** Initially, the drain came from the ON RRP. As Treasury issued more bills and rates rose, MMFs moved cash out of the Fed and into private markets. This was a healthy rotation.  
* **The Inflection Point (Late 2024):** By late 2024, ON RRP balances fell toward zero. This marked the end of the "free" buffer. Any further reduction in the Fed’s balance sheet now had to come from **bank reserves**.

### **5.3 Recent Stress Episodes: The Return of Volatility**

#### **5.3.1 September 2024: The Warning Shot**

On the September 30, 2024 quarter-end, SOFR spiked approximately **20 basis points** above the average of the preceding days.

* **Analysis:** This was the first major signal that the system had transitioned out of "abundance." With the ON RRP buffer depleted, the SLR constraints on dealers were no longer masked by a flood of MMF cash. Dealers pulled back, and rates jumped.  
* **Significance:** It confirmed that the SRF (Standing Repo Facility) acts as a *soft* ceiling. While it prevented a 2019-style blowout, it did not prevent meaningful spread widening.

#### **5.3.2 September 2025: Testing the Ceiling**

On September 15, 2025, a tax payment date, SOFR printed at **4.51%**, significantly above the Effective Federal Funds Rate (EFFR) of 4.33% and the IORB.

* **SRF Usage:** Banks borrowed **$1.5 billion** from the SRF.  
* **Signal:** The usage of the SRF—a penalty rate facility—confirmed that private market liquidity was either exhausted or priced punitively high. This was a direct test of the Fed’s backstop machinery.

#### **5.3.3 December 31, 2025: The "Breach" Event**

The year-end turn of 2025 represents the most critical stress test in the current cycle, highlighting the limitations of the SRF in a segmented market.

**Data Reconciliation:**

* **Date:** December 31, 2025\.  
* **SOFR:** 3.87%.  
* **IORB:** 3.65%.  
* **SRF Rate:** 3.75%.  
* **SRF Usage:** **$74.6 Billion**.

**The Anomaly:** SOFR (3.87%) traded **12 basis points above** the SRF rate (3.75%).

* **The Breakdown:** Why didn't dealers borrow infinite amounts at 3.75% from the Fed and lend at 3.87% to the market, capturing a risk-free profit?  
* **The Explanation:** **GSIB Constraints.** On December 31, expanding the balance sheet to arbitrage this spread would have increased the dealers' GSIB scores. The capital cost of that increase exceeded the 12bps profit.  
* **Segmentation:** The entities paying 3.87% (likely hedge funds and non-primary dealers) could not access the SRF directly. They were trapped in the bilateral market, reliant on constrained dealers who refused to intermediate.  
* **Implication for LIQUID:** The SRF is not a hard cap for SOFR. During GSIB-constrained windows, the spread can and will widen beyond the facility rate.

---

## **6\. Monitoring Framework: Early Warning Indicators (EWIs)**

Based on the mechanics of these stress episodes, we propose a tiered Early Warning Indicator dashboard for LIQUID. This moves beyond lagging indicators (like the rate itself) to leading indicators of capacity and friction.

### **6.1 Quantity-Based Indicators (The Fuel Gauge)**

These metrics assess the raw capacity of the system to handle shocks.

| Indicator | Metric | Data Source | Threshold / Warning | Rationale |
| :---- | :---- | :---- | :---- | :---- |
| **Aggregate Reserves** | Total Reserves held at Fed | FRED (WRESBAL) | Rapid decline toward $3.0 Trillion or \<10-11% of GDP | As reserves fall, the demand curve becomes non-linear. The 2019 crisis hit at \~$1.45T, but the new LCLoR is likely higher due to deposit growth. |
| **ON RRP Balances** | Overnight Reverse Repo Volume | NY Fed / FRED (RRPONTSYD) | Sustained levels \<$50 Billion | When ON RRP is near zero, the system has lost its "excess" buffer. Every dollar of TGA increase drains bank reserves directly. |
| **TGA Volatility** | Treasury General Account Balance | Daily Treasury Statement / FRED (WDTGAL) | Inflows \>$50B in a single day | Large tax inflows or settlement days act as massive liquidity vacuums. Monitor the Treasury's 1-month cash forecast. |
| **Dealer Net Positioning** | Primary Dealer Net Treasury Positions | FR 2004 (NY Fed) | **Net Long \>$200 Billion** | **Critical Indicator.** If dealers are net long historical amounts of Treasuries, their balance sheets are clogged. They cannot intermediate new flows. |

### **6.2 Price-Based Indicators (The Tremors)**

These metrics capture the subtle tightening of conditions before a blowout.

| Indicator | Metric | Data Source | Threshold / Warning | Rationale |
| :---- | :---- | :---- | :---- | :---- |
| **SOFR-IORB Spread Drift** | 30-Day Moving Average | Spread \> \+1 to \+3 bps | In an abundant regime, this spread is negative. A drift into positive territory signals the transition to "Ample/Scarce". |  |
| **Tail Dispersion** | 99th Percentile SOFR \- Median SOFR | Spread \> 10-15 bps | Stress manifests in the tails first. Bilateral borrowers (hedge funds) pay up before the median moves. A widening tail is a proxy for bilateral stress. |  |
| **GCF \- Tri-Party Spread** | GCF Repo Rate \- Tri-Party Rate | Widening (\> 2-5 bps) | Indicates that liquidity is stuck at the large dealers and not flowing to the inter-dealer market. Sign of segmentation. |  |

### **6.3 Behavioral Indicators (The Distress Signals)**

| Indicator | Metric | Data Source | Threshold / Warning | Rationale |
| :---- | :---- | :---- | :---- | :---- |
| **SRF "Pings"** | Standing Repo Facility Usage | Any usage \>$100M (non-test) | Usage of the penalty rate facility confirms private market failure. Small "pings" often precede larger demands. |  |
| **Sponsored Repo Volume** | FICC Sponsored Repo Daily Volume | Plateau or Decline during stress | If Sponsored Repo volume stops growing during a rate spike, it means netting constraints have been hit. |  |

---

## **7\. The Future Landscape: The 2027 Central Clearing Mandate**

Looking ahead, the repo market faces its most significant structural change in decades: the SEC’s requirement for mandatory central clearing of U.S. Treasury repo transactions, scheduled for implementation by June 30, 2027\.

### **7.1 The Mechanism of Change**

Currently, a vast portion of the bilateral repo market (hedge fund to dealer) is uncleared. The mandate will force these trades into the FICC.

* **Netting Benefits:** This should theoretically increase dealer capacity by allowing far more extensive netting of balance sheet positions.  
* **The "All-to-All" Vision:** It moves the market toward an "all-to-all" structure where the credit risk of the counterparty is replaced by the CCP (Central Counterparty).

### **7.2 The Transition Risk**

However, the transition itself poses risks.

* **Margin Calls:** Central clearing requires the posting of initial and variation margin. In a volatility spike, the liquidity drain from margin calls could exacerbate the cash shortage.  
* **Haircut Standardization:** The CCP will impose standardized haircuts, which may be higher than what some aggressive dealers currently offer clients. This could re-price leverage across the system.

For LIQUID, the period leading up to June 2027 will likely see dealers adjusting their business models, potentially withdrawing liquidity from uncleared segments ahead of the deadline.

---

## **8\. Conclusions and Strategic Recommendations**

The era of "set it and forget it" for SOFR monitoring is over. The depletion of the ON RRP buffer and the return of positive SOFR-IORB spreads signal that the U.S. repo market has re-entered a regime of **elasticity testing**. The events of December 2025 demonstrate that even with the SRF backstop, regulatory frictions can cause significant spread widening and segmentation.

**Key Takeaways for LIQUID:**

1. **The SRF is a Porous Ceiling:** Do not model the SRF rate as a hard cap. The spread can breach this level during GSIB-constrained windows (Year-End) due to lack of access for marginal borrowers.  
2. **Inventory is Destiny:** The **FR 2004 Net Positions** report is the most undervalued leading indicator. When dealers are "stuffed" with Treasuries, they possess zero elasticity to absorb TGA shocks.  
3. **TGA Sensitivity is Back:** With the ON RRP empty, the TGA has regained its power to disrupt markets. Daily tracking of tax flows and auction settlements is now mandatory for predicting rate moves.  
4. **Expect Seasonality:** The "Sawtooth" pattern of quarter-end spikes is the new normal. Algorithms should adjust for widened spreads on these dates to avoid false positives for systemic risk.

By integrating the Quantity, Price, and Behavioral EWIs outlined in this report, LIQUID can construct a robust monitoring shield, distinguishing between technical noise and the early tremors of a systemic liquidity event.

---

**Report compiled by:**

*Senior Fixed Income Strategist & Repo Market Specialist*

*January 25, 2026*

**Data Sources:**

Federal Reserve Bank of New York, Office of Financial Research (OFR), Federal Reserve Economic Data (FRED), CME Group, U.S. Department of the Treasury.

**(End of Report)**

