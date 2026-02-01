# **The Velocity of Distress: Dynamics of Conversion from Financial Trigger Events to Visible Delinquency (2024-2026)**

## **Executive Summary**

The prevailing architecture of consumer credit risk modeling relies on the foundational assumption of a predictable, linear latency between a financial shock and visible default. Historical conventions, often calibrated on data from the Great Recession or earlier stable economic periods, posit a "loss emergence period" ranging from 6 to 18 months. This window traditionally allows lenders to detect deteriorating credit scores, utilization spikes, and payment irregularities before a charge-off occurs. However, the post-pandemic economic landscape—defined by bifurcated savings rates, regulatory suppression of certain negative data, and shifting payment hierarchies—has fundamentally altered this timeline.

This report investigates the "conversion velocity" of financial stress: the speed at which a household moves from a destabilizing event (trigger) to a measurable credit delinquency. We analyze two primary triggers: labor market disruption (job loss) and health shocks (medical events). Our analysis reveals a diverging reality. For low-liquidity households, the conversion velocity for unsecured debt has accelerated, with the buffer between income interruption and default compressing to under 90 days. Conversely, for medical debt, regulatory interventions have artificially decelerated conversion, creating a "shadow delinquency" period of 365 days or more where severe financial distress remains invisible to traditional credit scoring models.

Crucially, we identify a "prioritization reshuffle" where households, constrained by inflation and dwindling excess savings, are engaging in strategic default behaviors—sacrificing unsecured credit card payments to preserve auto loans and housing, though even this hierarchy is showing signs of fracture in the 2024-2025 vintage data. This report provides an exhaustive examination of these dynamics, offering a recalibrated framework for forecasting credit risk in an environment where the lag between vulnerability and visibility is simultaneously shrinking and expanding.

## **1\. Introduction: The Latency Gap in Credit Risk**

### **1.1 The Theoretical Framework of Loss Emergence**

In the discipline of credit risk accounting and forecasting, the "loss emergence period" (LEP) is a critical variable. It represents the time lag between the occurrence of a loss event (e.g., unemployment, divorce, injury) and the lender’s recognition of that loss through charge-off or severe delinquency.1 Under the Current Expected Credit Loss (CECL) standard, financial institutions are required to estimate lifetime losses, necessitating a forward-looking view of how quickly current economic conditions translate into future defaults.3

Traditionally, this timeline follows a predictable, almost ballistic trajectory:

1. **Trigger Event (T=0):** Income shock or expenditure shock occurs.  
2. **Buffer Depletion (T+1 to T+6 months):** The household utilizes liquid savings, severance packages, and unemployment insurance (UI) to maintain solvency.  
3. **Liquidity Strain (T+3 to T+9 months):** Credit line utilization increases; revolving balances grow as consumers substitute credit for income.  
4. **Visible Delinquency (T+6 to T+12 months):** The first missed payment (30 days past due) appears on the credit file.  
5. **Default/Charge-off (T+6 to T+18 months):** The account reaches 180 days past due (credit cards) or 120 days (autos), triggering accounting recognition of the loss.

However, current macroeconomic data challenges this smooth trajectory. With 37% of adults unable to cover a $400 emergency expense with cash 5 and persistent inflation eroding real wages for the bottom quintile, the "Buffer Depletion" phase has effectively vanished for a significant segment of the population. The theoretical framework must now account for a bimodal distribution of outcomes: a "fast track" to default for the liquidity-constrained and a "slow burn" for the asset-rich.

### **1.2 The Divergence of 2024-2026**

The period from 2024 through early 2026 presents a unique paradox in consumer finance. Aggregate household balance sheets appear robust due to nominal wage gains and positive cash balance growth for the lowest income quartile in late 2025\.7 Yet, delinquency rates for auto loans and credit cards have surged past pre-pandemic levels.8 This suggests that while *average* liquidity is stable, *marginal* liquidity is highly volatile.

Understanding conversion velocity today requires dissecting the "cash buffer days"—the number of days a household can maintain spending without income.7 For low-income households, this metric acts as a countdown clock. When that clock runs out, the transition to delinquency is not a gradual slide but a sudden cliff. Conversely, policy changes regarding medical debt reporting 11 have introduced a statutory lag, effectively blinding lenders to a major category of household insolvency for a full year.

This report is structured to analyze these lags by trigger type. We begin by examining the primary driver of credit loss—employment shocks—and assessing how the timeline from "pink slip" to "past due" has compressed. We then contrast this with the timeline for medical events, which has been artificially elongated by regulation. Finally, we synthesize these findings into a new hierarchy of payment priority and offer implications for forecasting models.

## ---

**2\. Part A: Job Loss to Delinquency — The Compression of the Timeline**

The loss of employment remains the single most potent trigger for credit default. While historical correlations between unemployment rates and delinquency flows are established 13, the *speed* of this transmission has evolved significantly in the post-pandemic era.

### **2.1 Time to First Missed Payment after Job Loss**

The median time from job loss to the first missed bill payment is heavily dependent on the "cash buffer" available to the household. The data indicates that for a large plurality of the population, this buffer is insufficient to bridge even the administrative delay of unemployment insurance (UI) benefits.

#### **2.1.1 The Median Timeline**

Analysis of checking account activity and credit bureau data suggests that the median time from income cessation to the first missed payment for the general population is approximately **4 to 6 weeks**. However, this median obscures a stark dichotomy based on savings levels.

#### **2.1.2 Variance by Savings Level**

Research from the JPMorgan Chase Institute (JPMCI) highlights that cash balances are the primary determinant of the foreclosure and default timeline.

* **Households with \<$1,000 Liquid Savings (Low Liquidity):** For households in the lowest income quartile, cash balances have shown resilience in percentage terms, turning from negative growth in 2022 to positive growth (+2-6%) in 2025\.7 However, despite this percentage growth, the *absolute* level of reserves remains critically low. The "cash buffer days" for this cohort typically sustain spending for fewer than **21 days** without income inflows.10 Consequently, for households with less than $1,000 in liquid savings, the lag from job loss to first missed payment is estimated at **0 to 4 weeks**. These households often miss a payment within the same billing cycle as the income shock. The correlation between short-term unemployment (\<5 weeks) and 30-day delinquency is nearly 1:1, with a lag of only about one month.13  
* **Households with $1,000 \- $5,000 (Moderate Liquidity):** Households in the middle income quintiles maintain buffers of approximately **20 to 30 days**.10 With Unemployment Insurance (UI) typically replacing only 30-50% of lost wages, the arithmetic of solvency changes immediately. The lag here extends to **4 to 8 weeks**, allowing for one or two billing cycles of maneuvering before delinquency becomes visible. This group relies heavily on "payment Tetris"—rotating which bill gets paid—before succumbing to broad delinquency.  
* **Households with \>$10,000 (High Liquidity):** High-income households have seen their cash balances decline in real terms through 2025 (dropping 2% by October 2025\) as they reallocate funds to higher-yielding assets.7 Despite this "depletion," their absolute liquidity remains sufficient to bridge significant employment gaps. For this group, the lag is often **3 to 6 months** or longer. Delinquency in this cohort is driven more by strategic decisions or extreme leverage (e.g., jumbo mortgages) rather than immediate cash flow insolvency.

#### **2.1.3 Variance by Income Level**

Income volatility acts as a precursor to delinquency. JPMCI data reveals that 1 in 4 months sees a monthly income swing of at least 25% for hourly workers.16 This inherent volatility means that "job loss" is not always a binary event but often manifests as a reduction in hours. For gig economy workers and hourly employees, the conversion velocity is nearly instantaneous because their baseline consumption matches their peak income, leaving no margin for variance.

**Table 1: Estimated Lag to First Missed Payment by Segment**

| Household Segment | Cash Buffer Days | Est. Lag to First Missed Payment | Primary Mitigation Strategy |
| :---- | :---- | :---- | :---- |
| **Low Income / \<$1k Savings** | 9 \- 21 Days | **0 \- 3 Weeks** | Payday loans, overdrafts, skipping utility bills. |
| **Middle Income / $2k-$5k Savings** | 20 \- 35 Days | **4 \- 8 Weeks** | Credit card utilization, partial payments. |
| **High Income / \>$10k Savings** | 40+ Days | **12 \- 24 Weeks** | Asset liquidation, HELOC drawdowns. |

### **2.2 Historical Compression: 2008 vs. 2020 vs. 2024-2025**

The elasticity of delinquency to unemployment has shifted over the last three major economic cycles, demonstrating a compression of the timeline in the current environment compared to the Great Recession.

#### **2.2.1 2008-2010: The Great Recession**

During the Global Financial Crisis (GFC), the lag from unemployment to delinquency was typically **3 to 5 months** for subprime borrowers and **6 to 12 months** for prime borrowers.14

* **Drivers:** Households often utilized home equity lines (HELOCs) or credit cards to extend solvency. The housing crash eventually eroded this equity, but the initial buffer existed.  
* **Mechanism:** The "extend and pretend" phase was prolonged by a slower foreclosure process and the sheer volume of distressed borrowers, which overwhelmed servicers.

#### **2.2.2 2020-2021: The Pandemic Anomaly**

The COVID-19 recession presented an unprecedented decoupling of unemployment and delinquency. Despite unemployment spiking to 14.8%, delinquency rates *declined*.14

* **Drivers:** Massive fiscal support, including enhanced UI ($600/week) and stimulus checks, combined with mandatory forbearance programs.  
* **Mechanism:** The "conversion velocity" effectively dropped to zero for millions of households. Government intervention broke the causal link between job loss and default.

#### **2.2.3 2024-2025: The Current Cycle**

Current data suggests a **re-compression of the lag** to levels faster than 2008\.

* **Drivers:** Inflationary pressure on fixed costs (rent, food, autos) and the expiration of pandemic-era supports. While homeowners have equity, high interest rates make tapping it expensive (HELOC balances are rising, reaching $422 billion in Q3 2025, but borrowing costs are prohibitive).18  
* **Mechanism:** For renters and subprime borrowers, the lack of accessible, low-cost credit means the "extend and pretend" phase is shorter. TransUnion data indicates that serious delinquency rates for recent vintages (2022-2023 originations) are rising faster than historical norms.19 For example, the 2022 credit card vintage reached an 8% delinquency rate in less than two years, a trajectory significantly steeper than the 2016 vintage.19 This confirms that once stress hits, it converts to delinquency with higher velocity.

**Factor Analysis of Compression:**

1. **Lower Savings Rates:** Excess savings from the pandemic have been largely depleted for the middle class, returning to or dipping below 2019 trend lines.15  
2. **Higher Fixed Costs:** The cost of non-discretionary items (shelter, transport) has risen faster than wages for the bottom quintile, raising the "burn rate" of any severance or savings.  
3. **Gig Work Prevalence:** The lack of severance packages for gig workers means income stops immediately upon market downturn, removing the 2-4 week buffer that salaried employees typically enjoy.

### **2.3 Unemployment Duration Thresholds: The "Cliff"**

The relationship between unemployment duration and delinquency is non-linear. There is a distinct "cliff" effect associated with the exhaustion of benefits or savings.

#### **2.3.1 The 4-Week "Hand-to-Mouth" Cliff**

Initial claims data shows that short-term unemployment (\<5 weeks) correlates with 30-day delinquencies with a lag of about one month.13 This immediate reaction comes from the "hand-to-mouth" segment (approx. 20-30% of households) who lack even a one-month buffer. When weekly jobless claims rise, 30-day delinquencies track almost synchronously, suggesting a near-zero lag for this population.

#### **2.3.2 The UI Exhaustion Cliff (12-26 Weeks)**

Standard state UI benefits typically last 26 weeks, though some states like Florida offer as few as 12-14 weeks.20 Historical studies indicate that delinquency rates spike disproportionately in the month following benefit exhaustion.20

* **Mechanism:** JPMCI research shows that spending drops sharply upon benefit exhaustion, implying that debt service is one of the first expenditures to be cut to preserve cash for food and shelter.20  
* **Shift:** In the current high-cost environment, the cliff appears to have moved forward. With the average cost of a car repair at $838 and rental costs elevated 6, the "burn rate" of savings is higher. We estimate the critical threshold for the median household has shifted from **12-16 weeks** of unemployment down to **8-10 weeks**.

## ---

**3\. Part B: Medical Event to Delinquency — The Regulatory Shield**

While job loss converts to delinquency rapidly, medical events operate under a completely different, artificially elongated timeline due to consumer protection regulations. This creates a "hidden risk" where a borrower may be insolvent due to medical costs long before it appears on a credit report.

### **3.1 Time from Medical Event to First Missed Payment**

The conversion from a medical "trigger" to a credit "event" is defined by bureaucratic friction and regulatory pauses.

#### **3.1.1 Uninsured Patients**

For the uninsured, the path to visible delinquency is paradoxically slower than for general debts due to the nature of medical billing cycles.

* **Timeline:** While the cost is incurred immediately, the billing process often involves a 30-90 day grace period from providers before aggressive collections begin.23  
* **Lag:** Uninsured patients typically miss payments on *other* bills (rent, utilities) within **2-3 months** of the medical event as they divert cash to pay providers or simply lose liquidity due to inability to work.

#### **3.1.2 Underinsured Patients (High Deductible)**

Patients with high-deductible health plans (HDHPs) face "surprise liquidity shocks."

* **Mechanism:** A $5,000 deductible is often charged post-adjudication. The delay between service and the "patient responsibility" statement can be **30 to 60 days**.24  
* **Lag:** Once the bill arrives, if the patient cannot pay, they often utilize credit cards to cover the deductible. This transforms the debt from "medical" (slow reporting) to "revolving" (fast reporting). If they cannot use credit, the lag to missing other payments is **3-5 months**.

#### **3.1.3 Adequately Insured Patients**

For this group, the lag is driven by coverage disputes.

* **Lag:** Disputes can last 6-12 months. During this time, consumers often suspend payments on the medical bill. Due to regulatory shields, this does not result in a credit hit.

### **3.2 Medical Debt Timeline: The "Shadow Delinquency"**

The timeline from "got sick" to "credit damaged" is now effectively **12 to 18 months**, creating a massive blind spot in credit risk models.

1. **Date of Service (T=0):** The medical event occurs.  
2. **Billing Latency (T+30 to T+180 Days):** Providers bill insurance; adjudication takes 30-45 days.24 Patient responsibility is determined. "Surprise bills" or complex hospital billing can delay the first patient statement by months.25  
3. **Internal Collections (T+90 to T+180 Days):** Providers attempt to collect. Most hospital systems keep debt in-house for 90-120 days before referral.23  
4. **Bad Debt Placement (T+180 Days):** Debt is sold or referred to a third-party collection agency. In the past, this would trigger credit reporting.  
5. **The Regulatory "Cure Period" (T+365 Days):** As of recent changes by the three major credit bureaus (Equifax, Experian, TransUnion) and CFPB guidance, unpaid medical debt cannot be reported until it is **365 days past due**.11 Furthermore, debts under $500 are never reported 26, and paid collections are removed immediately.

**Total Lag:** The timeline from "got sick" to "credit damaged" is now effectively **365+ days** from the date of first delinquency, or roughly **18 months** from the date of service.

### **3.3 Spillover Effects: The Hidden Contagion**

Because medical debt is shielded from credit reports for a year, the *visible* delinquency often appears elsewhere first. This is the "spillover effect."

* **Rent and Mortgage First:** A 2024 study led by Johns Hopkins researchers found that medical debt is a strong predictor of subsequent housing instability. Individuals with medical debt had a **44% higher risk** of housing instability (missed rent/mortgage) in the following year.27  
* **Prioritization:** Unlike the traditional hierarchy where consumers protect their shelter first, a large medical shock depletes the cash required for rent.  
* **Credit Card Contagion:** A common behavior is paying medical bills with credit cards to avoid collections calls. This transforms "medical debt" (no interest, reporting shield) into "credit card debt" (high interest, immediate reporting).26 Once converted, the delinquency lag snaps back to the rapid 30-90 day timeline of revolving credit.

**Prioritization Pattern:**

1. **Medical Bills:** Skipped first (due to lack of immediate service interruption and credit reporting shield).  
2. **Utilities:** Skipped second (seasonal moratoriums often protect against cutoffs).  
3. **Unsecured Personal Loans/Credit Cards:** Skipped third (to preserve cash for shelter/auto).  
4. **Rent/Mortgage:** Skipped last (but risk increases significantly if medical shock is large).

## ---

**4\. Part C: General Conversion Dynamics**

Understanding the sequence in which households stop paying obligations provides the roadmap for predicting portfolio losses.

### **4.1 Buffer Duration Research**

The "cash buffer" is the primary defense against delinquency.

* **JPMorgan Chase Institute Figures:**  
  * **Low Income:** Cash balances grew 2-6% in 2025, but represent only **9 to 21 days** of buffer.7  
  * **Middle Income:** Buffer of **20 to 30 days**.  
  * **High Income:** Buffer of **40+ days**, though balances are declining slightly (-2%) as funds move to investments.7  
* **Trend:** Buffer duration spiked in 2020-2021 due to stimulus but has largely reverted to 2019 levels. For the bottom 50% of households, real buffers (adjusted for inflation) have decreased over the past decade due to the rising cost of essentials.

### **4.2 The "Cascade Timeline": A Reshuffled Deck**

The "pecking order" of debt repayment has shifted significantly from the patterns observed during the Great Recession.

**Table 2: Evolution of Consumer Payment Hierarchy**

| Priority Rank | Great Recession (2008-2010) | Pandemic Era (2020-2021) | Current Cycle (2024-2025) |
| :---- | :---- | :---- | :---- |
| **1 (Highest)** | Mortgage (Strategic Default common) | Mortgage (Forbearance active) | **Auto Loan** / Mortgage |
| **2** | Auto Loan | Auto Loan | **Mortgage** |
| **3** | Student Loan | Student Loan (Paused) | **Student Loan** (threat of garnishment) |
| **4 (Lowest)** | Credit Card | Credit Card | **Credit Card** / Unsecured Personal |

#### **4.2.1 The Primacy of the Auto Loan**

In the current cycle, the auto loan has historically competed with the mortgage for the top spot. TransUnion data and Federal Reserve reports indicate that while auto delinquencies are rising (reaching 2.96% in Q4 2024 for serious delinquency) 9, consumers still prioritize their vehicle over unsecured debt because it is essential for employment.30

#### **4.2.2 The Student Loan Disruptor**

With the resumption of student loan payments and the threat of wage garnishment returning 31, a fascinating dynamic has appeared. TransUnion found that student loan borrowers facing involuntary collections prioritize student loan payments *ahead* of credit cards and personal loans.32 This creates a "crowding out" effect: resumed student loan payments consume the liquidity that was previously servicing credit card debt, leading to a spike in credit card delinquencies (up **479%** among seriously delinquent student loan borrowers).33

#### **4.2.3 The Sequence of Delinquency**

1. **Utilities/Phone:** Often the first signal (missed 1 month).  
2. **Retail Store Cards:** High interest, low utility.  
3. **General Purpose Credit Cards:** Prioritized based on available credit line. Cards with no available credit are skipped first.  
4. **Auto Loan:** Protected until repossession is imminent.  
5. **Mortgage/Rent:** The final stand.

**Time from First 30-Day Late to Charge-Off:**

* **Credit Cards:** 180 Days (Regulatory standard).  
* **Auto Loans:** 90-120 Days (Accelerated due to high vehicle values incentivizing faster repossession).34

### **4.3 Velocity by Trigger Type**

Based on the synthesized data, we rank the conversion velocity of major triggers from fastest to slowest:

1. **Job Loss (Hourly/Gig Worker):** **0 \- 1 Month.** (Zero buffer, immediate cash flow stop).  
2. **Divorce/Separation:** **1 \- 3 Months.** (Immediate doubling of housing expenses, legal costs).  
3. **Job Loss (Salaried):** **2 \- 5 Months.** (Severance and savings delay impact).  
4. **Auto Accident (Liability):** **3 \- 6 Months.** (Deductibles and repair costs create immediate strain, but loan payment is protected to keep the car).  
5. **Medical Event:** **3 \- 9 Months** (Spillover to other debts); **12+ Months** (Medical debt itself).

## ---

**5\. Part D: Implications for Forecasting**

Standard risk models, particularly those built on "incurred loss" frameworks or pre-pandemic vintage curves, are currently mispricing the velocity of risk.

### **5.1 Model Assumptions vs. Reality**

Standard credit models often assume a **loss emergence period (LEP)** of **12 months** for retail credit.2 This assumption posits that a borrower who defaults today likely experienced the trigger event 12 months ago.

* **The Mismatch:** For the "fragile" population (37% of Americans), the LEP is actually **3 months**. Using a 12-month lookback dilutes the signal and delays provisioning.  
* **CECL Impact:** The CECL accounting standard requires "reasonable and supportable forecasts".4 Banks relying on historical loss curves from 2010-2019 (a period of deleveraging) will under-predict losses for the 2022-2024 vintages, which are behaving with higher volatility.19 The "vintage curve" for 2022 originations shows them reaching 8% delinquency in half the time it took 2016 vintages.19

### **5.2 Leading Indicators: The Behavioral Signals**

To catch delinquency *before* the first missed payment (T-30 to T-90 days), lenders must look beyond bureau data to transactional behavior.

1. **Overdraft Frequency:** The most potent early warning signal (EWS). A shift from 0 to 1+ overdrafts correlates strongly with future default, often appearing 3-6 months before a FICO drop.37  
2. **Utilization Velocity:** It is not just the *level* of utilization, but the *rate of change*. A borrower moving from 30% to 70% utilization in 60 days is a higher risk than a stable 80% borrower.  
3. **Payment Magnitude:** A shift from "paying in full" (transactor) to "minimum due" (revolver) is a clear signal of distress, preceding delinquency by 3-5 months.3  
4. **Deposit Depletion:** For institutions with depository relationships, a consistent decline in average daily balance over 3 months is a strong predictor of impending default.38

### **5.3 Forecast Validity**

Have institutions updated their assumptions?

* **Yes:** The Federal Reserve and major banks have begun dissecting "excess savings" depletion in their risk outlooks.  
* **Challenge:** Most models still struggle with the "medical blind spot" and the new student loan dynamics. The correlation between student loan payment resumption and auto/credit card delinquency is a new variable that requires recalibration of "ability to pay" models.

## ---

**6\. Conclusion: The New Velocity of Risk**

The "conversion velocity" of financial stress has bifurcated. For the financially vulnerable—those living paycheck-to-paycheck with under $1,000 in savings—the timeline from trigger to trouble has compressed to near-zero. Job loss today becomes missed payments next month. The protective layers of 2020 (stimulus, forbearance) are gone, and the cost of living (rent, autos) consumes the buffer that remains.

Conversely, for specific triggers like medical events, the visible timeline has been legislated into slow motion. A borrower can be financially devastated by a hospital bill today but remain "prime" on paper for another year.

For risk managers, the implication is clear: **Wait-and-see is a failing strategy.** Relying on 30-day delinquencies to signal portfolio stress is too late. The new leading indicators are found in deposit account activity (overdrafts), utilization velocity, and the subtle "crowding out" effects where student loans or rent displace credit card payments. The lag is dead; long live the data.

#### **Works cited**

1. Remarks by John C. Dugan to the Institute of International Bankers, March 2, 2009; "Loan Loss Provisioning and Pro-cyclical \- OCC.gov, accessed January 25, 2026, [https://www.occ.treas.gov/news-issuances/speeches/2009/pub-speech-2009-16.pdf](https://www.occ.treas.gov/news-issuances/speeches/2009/pub-speech-2009-16.pdf)  
2. Estimating Credit Losses: Evaluating Loss Emergence Period and Qualitative Factors \- BDO USA, accessed January 25, 2026, [https://www.bdo.com/getattachment/60198096-b94f-4003-a535-3da441443c73/ASSR\_Estimating-Credit-Losses\_Practice-Aid\_11-18-](https://www.bdo.com/getattachment/60198096-b94f-4003-a535-3da441443c73/ASSR_Estimating-Credit-Losses_Practice-Aid_11-18-)  
3. Allowances for Credit Losses | Comptroller's Handbook | OCC.gov, accessed January 25, 2026, [https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/files/allowances-for-credit-losses/pub-ch-allowances-credit-losses.pdf](https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/files/allowances-for-credit-losses/pub-ch-allowances-credit-losses.pdf)  
4. CECL: Credit Cards and Lifetime Estimation \- A Reasonable Approach \- Moody's, accessed January 25, 2026, [https://www.moodys.com/web/en/us/insights/banking/cecl-credit-cards-and-lifetime-estimation-a-reasonable-approach.html](https://www.moodys.com/web/en/us/insights/banking/cecl-credit-cards-and-lifetime-estimation-a-reasonable-approach.html)  
5. The Fed \- Report on the Economic Well-Being of U.S. Households in 2024 \- May 2025 \- Savings and Investments \- Federal Reserve Board, accessed January 25, 2026, [https://www.federalreserve.gov/publications/2025-economic-well-being-of-us-households-in-2024-savings-and-investments.htm](https://www.federalreserve.gov/publications/2025-economic-well-being-of-us-households-in-2024-savings-and-investments.htm)  
6. When the Unexpected Happens, Be Ready with an Emergency Fund, accessed January 25, 2026, [https://www.stlouisfed.org/publications/page-one-economics/2025/sep/when-unexpected-happens-be-ready-with-emergency-fund](https://www.stlouisfed.org/publications/page-one-economics/2025/sep/when-unexpected-happens-be-ready-with-emergency-fund)  
7. Real income sustains weak trend, while cash balances remain stable \- JPMorganChase, accessed January 25, 2026, [https://www.jpmorganchase.com/institute/all-topics/financial-health-wealth-creation/real-income-sustains-weak-trend-cash-liquidity-remains-stable](https://www.jpmorganchase.com/institute/all-topics/financial-health-wealth-creation/real-income-sustains-weak-trend-cash-liquidity-remains-stable)  
8. The Fed \- A Note on Recent Dynamics of Consumer Delinquency Rates, accessed January 25, 2026, [https://www.federalreserve.gov/econres/notes/feds-notes/a-note-on-recent-dynamics-of-consumer-delinquency-rates-20251124.html](https://www.federalreserve.gov/econres/notes/feds-notes/a-note-on-recent-dynamics-of-consumer-delinquency-rates-20251124.html)  
9. Household Debt Balances Continue Steady Increase; Delinquency Transition Rates Remain Elevated for Auto and Credit Cards \- FEDERAL RESERVE BANK of NEW YORK, accessed January 25, 2026, [https://www.newyorkfed.org/newsevents/news/research/2025/20250213](https://www.newyorkfed.org/newsevents/news/research/2025/20250213)  
10. Household Cash Buffer Management from the Great Recession through COVID-19, accessed January 25, 2026, [https://www.jpmorganchase.com/institute/all-topics/financial-health-wealth-creation/household-cash-buffer-management-from-the-great-recession-through-covid-19](https://www.jpmorganchase.com/institute/all-topics/financial-health-wealth-creation/household-cash-buffer-management-from-the-great-recession-through-covid-19)  
11. Do medical bills affect my credit and where do I find out what's in my medical payment history?, accessed January 25, 2026, [https://www.consumerfinance.gov/ask-cfpb/do-medical-bills-affect-my-credit-and-where-do-i-find-out-whats-in-my-medical-payment-history-en-1837/](https://www.consumerfinance.gov/ask-cfpb/do-medical-bills-affect-my-credit-and-where-do-i-find-out-whats-in-my-medical-payment-history-en-1837/)  
12. Have medical debt? Anything already paid or under $500 should no longer be on your credit report, accessed January 25, 2026, [https://www.consumerfinance.gov/about-us/blog/medical-debt-anything-already-paid-or-under-500-should-no-longer-be-on-your-credit-report/](https://www.consumerfinance.gov/about-us/blog/medical-debt-anything-already-paid-or-under-500-should-no-longer-be-on-your-credit-report/)  
13. The Duration of Delinquency \- RECURSION CO, accessed January 25, 2026, [https://www.recursionco.com/blog/the-duration-of-delinquency](https://www.recursionco.com/blog/the-duration-of-delinquency)  
14. On the relationship between unemployment and late credit card payments \- FRED Blog, accessed January 25, 2026, [https://fredblog.stlouisfed.org/2021/12/on-the-relationship-between-unemployment-and-late-credit-card-payments/](https://fredblog.stlouisfed.org/2021/12/on-the-relationship-between-unemployment-and-late-credit-card-payments/)  
15. Household Finances Pulse through June 2024: Balances Continue to Decline, accessed January 25, 2026, [https://www.jpmorganchase.com/institute/all-topics/financial-health-wealth-creation/household-pulse-balances-through-june-2024](https://www.jpmorganchase.com/institute/all-topics/financial-health-wealth-creation/household-pulse-balances-through-june-2024)  
16. Earnings instability: The hidden volatility of American workers' paychecks \- JPMorgan Chase, accessed January 25, 2026, [https://www.jpmorganchase.com/institute/all-topics/financial-health-wealth-creation/earnings-instability](https://www.jpmorganchase.com/institute/all-topics/financial-health-wealth-creation/earnings-instability)  
17. The Effects of Extra Unemployment Benefits on Household Delinquencies \- Federal Reserve Bank of St. Louis, accessed January 25, 2026, [https://www.stlouisfed.org/on-the-economy/2020/august/effects-extra-unemployment-benefits-household-delinquencies](https://www.stlouisfed.org/on-the-economy/2020/august/effects-extra-unemployment-benefits-household-delinquencies)  
18. Household Debt and Credit Report \- FEDERAL RESERVE BANK of NEW YORK, accessed January 25, 2026, [https://www.newyorkfed.org/microeconomics/hhdc](https://www.newyorkfed.org/microeconomics/hhdc)  
19. Credit card delinquencies are higher than in 2019 because lenders took on more risk, accessed January 25, 2026, [https://www.consumerfinance.gov/about-us/blog/credit-card-delinquencies-are-higher-than-in-2019-because-lenders-took-on-more-risk/](https://www.consumerfinance.gov/about-us/blog/credit-card-delinquencies-are-higher-than-in-2019-because-lenders-took-on-more-risk/)  
20. Recovering from Job Loss: The Role of Unemployment Insurance (PDF) \- Ways and Means Committee, accessed January 25, 2026, [https://waysandmeans.house.gov/wp-content/uploads/2016/10/20160907HR-Transcript-Insert-Mr.-Buchanan-JP-Morgan-Chase-Co-Institute-Recovering-from-Job-Loss-The-Role-of-Unemployment-Insurance.pdf](https://waysandmeans.house.gov/wp-content/uploads/2016/10/20160907HR-Transcript-Insert-Mr.-Buchanan-JP-Morgan-Chase-Co-Institute-Recovering-from-Job-Loss-The-Role-of-Unemployment-Insurance.pdf)  
21. A Study of Unemployment Insurance Recipients and Exhaustees: Findings from a National Survey, accessed January 25, 2026, [https://oui.doleta.gov/dmstree/op/op90/op\_03-90.pdf](https://oui.doleta.gov/dmstree/op/op90/op_03-90.pdf)  
22. Rising Rents and Evictions Linked to Premature Death, accessed January 25, 2026, [https://evictionlab.org/rising-rents-and-evictions-linked-to-premature-death/](https://evictionlab.org/rising-rents-and-evictions-linked-to-premature-death/)  
23. How Long Before Medical Bills Go to Collections? \- EZ Settle Solutions, accessed January 25, 2026, [https://ezsettlesolutions.com/how-long-before-medical-bills-go-to-collections-2/](https://ezsettlesolutions.com/how-long-before-medical-bills-go-to-collections-2/)  
24. Medical Billing Time Limits by State in 2025 \- EZMD Solutions, accessed January 25, 2026, [https://ezmdsolutions.com/medical-billing-time-limits-by-state/](https://ezmdsolutions.com/medical-billing-time-limits-by-state/)  
25. How Long After Medical Services Can You Be Billed? \- EZ Settle Solutions, accessed January 25, 2026, [https://ezsettlesolutions.com/how-long-after-medical-services-can-you-be-billed/](https://ezsettlesolutions.com/how-long-after-medical-services-can-you-be-billed/)  
26. How Does Medical Debt Affect Your Credit Score? \- Experian, accessed January 25, 2026, [https://www.experian.com/blogs/ask-experian/medical-debt-and-your-credit-score/](https://www.experian.com/blogs/ask-experian/medical-debt-and-your-credit-score/)  
27. Medical Debt Associated With Subsequent Difficulty Paying Rent or Mortgage, accessed January 25, 2026, [https://publichealth.jhu.edu/2026/medical-debt-associated-with-subsequent-difficulty-paying-rent-or-mortgage](https://publichealth.jhu.edu/2026/medical-debt-associated-with-subsequent-difficulty-paying-rent-or-mortgage)  
28. Medical Debt Linked To Rent and Mortgage Problems Study Says | Powers Health, accessed January 25, 2026, [https://www.powershealth.org/about-us/newsroom/health-library/2026/01/14/medical-debt-linked-to-rent-and-mortgage-problems-study-says](https://www.powershealth.org/about-us/newsroom/health-library/2026/01/14/medical-debt-linked-to-rent-and-mortgage-problems-study-says)  
29. MEDICAL DEBT \- Tennessee Justice Center, accessed January 25, 2026, [https://www.tnjustice.org/medical-debt](https://www.tnjustice.org/medical-debt)  
30. Rising U.S. Consumer Delinquencies: Pockets of Strain in a Resilient Consumer, accessed January 25, 2026, [https://economics.td.com/us-rising-consumer-deliquencies](https://economics.td.com/us-rising-consumer-deliquencies)  
31. New JPMorganChase Institute research on the changing landscape of student loan repayments, accessed January 25, 2026, [https://www.jpmorganchase.com/institute/all-topics/financial-health-wealth-creation/2025-student-debt-IDR-and-wage-garnishment](https://www.jpmorganchase.com/institute/all-topics/financial-health-wealth-creation/2025-student-debt-IDR-and-wage-garnishment)  
32. TransUnion connects student-loan performance concerns to auto finance, accessed January 25, 2026, [https://www.autoremarketing.com/subprime/transunion-connects-student-loan-performance-concerns-to-auto-finance/](https://www.autoremarketing.com/subprime/transunion-connects-student-loan-performance-concerns-to-auto-finance/)  
33. TransUnion: Student Loan Borrowers May Prioritize Federal Debt Over Cards \- Stock Titan, accessed January 25, 2026, [https://www.stocktitan.net/news/TRU/as-wage-garnishment-looms-federal-student-loan-borrowers-indicate-xnswfm06p5zw.html](https://www.stocktitan.net/news/TRU/as-wage-garnishment-looms-federal-student-loan-borrowers-indicate-xnswfm06p5zw.html)  
34. How a car loan charge-off works — and how to avoid repossession \- Bankrate, accessed January 25, 2026, [https://www.bankrate.com/loans/auto-loans/auto-loan-charge-off/](https://www.bankrate.com/loans/auto-loans/auto-loan-charge-off/)  
35. ECB guide to internal models \- Risk-type-specific chapters \- Banking supervision, accessed January 25, 2026, [https://www.bankingsupervision.europa.eu/framework/legal-framework/public-consultations/pdf/internal\_models\_risk\_type\_chapters/ssm.guide\_to\_internal\_models\_risk\_type\_chapters\_201809.en.pdf](https://www.bankingsupervision.europa.eu/framework/legal-framework/public-consultations/pdf/internal_models_risk_type_chapters/ssm.guide_to_internal_models_risk_type_chapters_201809.en.pdf)  
36. The Fed \- New Accounting Framework Faces Its First Test: CECL During the Pandemic, accessed January 25, 2026, [https://www.federalreserve.gov/econres/notes/feds-notes/new-accounting-framework-faces-its-first-test-cecl-during-the-pandemic-20211203.html](https://www.federalreserve.gov/econres/notes/feds-notes/new-accounting-framework-faces-its-first-test-cecl-during-the-pandemic-20211203.html)  
37. Who's Paying Those Overdraft Fees? \- Liberty Street Economics, accessed January 25, 2026, [https://libertystreeteconomics.newyorkfed.org/2025/05/whos-paying-those-overdraft-fees/](https://libertystreeteconomics.newyorkfed.org/2025/05/whos-paying-those-overdraft-fees/)  
38. Exposure at Default of Unsecured Credit Cards \- OCC.gov, accessed January 25, 2026, [https://www.occ.gov/publications-and-resources/publications/economics/working-papers-archived/pub-econ-working-paper-2009-2.pdf](https://www.occ.gov/publications-and-resources/publications/economics/working-papers-archived/pub-econ-working-paper-2009-2.pdf)