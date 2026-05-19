# **MMF Post-RRP Research Results**

## **Executive Summary**

As of January 2026, the United States financial system has completed a historic transition in its funding markets. The Federal Reserve’s Overnight Reverse Repurchase Agreement (ON RRP) facility—a mechanism that acted as the dominant liquidity sink for nearly four years—has been effectively drained. From a peak utilization of approximately $2.55 trillion in late 2022, the facility’s balance has fallen to a negligible \~$2.5 billion. This depletion marks the end of the "abundant liquidity" regime that characterized the post-pandemic recovery and the beginning of a more fragile, market-dependent era of "ample" but unevenly distributed reserves.

The primary objective of this research is to trace the migration of that $2.5 trillion and assess the structural implications for the $7.7 trillion Money Market Fund (MMF) industry. Our analysis confirms that the liquidity buffer previously housed at the Fed did not evaporate; rather, it was aggressively redeployed into the private sector through two primary channels: the U.S. Treasury bill market and the private repurchase agreement (repo) market. This reallocation was driven by rational economic incentives—specifically, the emergence of a positive spread between private market rates and the ON RRP floor, catalyzed by heavy Treasury issuance and dealer balance sheet optimization via central clearing.

However, the "normalization" of the Fed’s balance sheet has reintroduced pre-2020 systemic vulnerabilities. In the absence of the ON RRP as a passive shock absorber, MMFs have become the critical marginal lenders in the repo market. A significant portion of MMF liquidity is now actively funding hedge fund leverage through the Fixed Income Clearing Corporation (FICC) Sponsored Repo service. This creates a direct transmission mechanism wherein volatility in the Treasury cash/futures basis trade can rapidly spill over into funding markets, potentially forcing MMFs to withdraw liquidity during stress events—precisely when it is most needed.

We identify three critical risks in this post-RRP environment:

1. **The Basis Trade Fragility:** MMFs are financing a record accumulation of Treasury basis positions (estimated at \~$1.85 trillion exposure). A chaotic unwind of these positions could trigger a liquidity lockup similar to March 2020, but without the RRP cash pool to dampen the shock.  
2. **Structural Rigidity:** While MMF assets are at record highs ($7.70 trillion), this liquidity is largely deployed in term assets or matched-book repo. Unlike the overnight RRP, this capital cannot be instantaneously redeployed without price impact.  
3. **The "Soft Ceiling" Uncertainty:** With the RRP floor removed, the market relies on the Standing Repo Facility (SRF) to act as a ceiling on rates. Recent testing suggests the SRF may dampen volatility but is unlikely to prevent intraday dislocations, as evidenced by SOFR spikes in late 2025\.

The following report provides an exhaustive analysis of the MMF landscape, the mechanics of the RRP drain, the specifics of cash reallocation, and a stress-test assessment of the new funding regime.

---

## **1\. MMF Landscape**

The U.S. Money Market Fund industry serves as the primary intermediary for short-term liquidity in the global financial system. As of early 2026, the sector has not only retained the assets accumulated during the pandemic but has expanded further, solidifying its role as the dominant non-bank lender.

### **1.1 Market Size and Segmentation**

Total assets under management (AUM) in U.S. money market funds reached **$7.70 trillion** as of the week ending January 21, 2026\. This figure underscores a structural shift in depositor behavior, often referred to as "cash sorting," where institutional and retail capital permanently migrated from low-yielding bank deposits to higher-yielding market instruments.

The industry remains heavily bifurcated by regulatory classification, which dictates investment behavior:

* **Government MMFs ($6.32 trillion / \~82% of assets):** This segment is the behemoth of the industry. Regulatory reforms (Rule 2a-7) incentivize these funds to hold 99.5% of their assets in cash, government securities, or repos collateralized by government securities. Because they cannot invest in credit instruments like commercial paper (CP), Government MMFs are the primary drivers of flows into the RRP, T-bills, and Treasury repo markets. Their sheer size means their asset allocation decisions set the marginal price for government funding.  
* **Prime MMFs ($1.24 trillion / \~16% of assets):** Unlike Government funds, Prime funds can invest in unsecured corporate debt (CP) and bank certificates of deposit (CDs). Despite offering higher yields, this sector faces stringent regulatory constraints, including mandatory liquidity fees introduced in the 2023 SEC reforms, which have curbed their growth relative to Government funds.  
* **Tax-Exempt/Municipal MMFs ($145 billion / \~2% of assets):** A smaller niche focused on short-term municipal debt, largely insulated from the systemic repo dynamics discussed in this report.

### **1.2 Structural Constraints and Investment Mandates**

The behavior of MMFs is governed by strict mandates regarding liquidity, maturity, and credit quality. Understanding these constraints is essential to explaining why MMFs utilized the RRP and why they left it.

**Regulatory Constraints (SEC Rule 2a-7):**

* **Daily Liquidity:** Taxable money funds must hold at least 25% of their total assets in daily liquid assets (cash, Treasuries, or ON RRP).  
* **Weekly Liquidity:** They must hold at least 50% in weekly liquid assets (agencies, discount notes).  
* **Weighted Average Maturity (WAM):** The portfolio WAM must not exceed 60 days to limit interest rate risk.  
* **Weighted Average Life (WAL):** The WAL must not exceed 120 days to limit credit spread risk.

During the "abundant reserves" era (2021–2023), the scarcity of eligible T-bills often made it difficult for MMFs to meet these diversification and liquidity requirements without using the Fed’s facility. The ON RRP provided infinite daily liquidity with zero credit risk, making it the perfect regulatory compliance tool. As we moved into 2026, the surge in T-bill issuance eased these constraints, allowing managers to extend WAM to capture yield.

### **1.3 Major Industry Players**

The MMF industry exhibits high concentration, with the top 10 sponsors controlling the vast majority of assets. This concentration simplifies the transmission of monetary policy but creates "single point of failure" risks in decision-making.

Key sponsors in 2026 include:

* **Fidelity Investments:** The largest operator, managing massive liquidity pools like the Fidelity Government Money Market Fund (SPAXX). Fidelity's aggressive management of WAM often signals broader industry trends.  
* **Vanguard Group:** A dominant player in the government space (e.g., Vanguard Federal Money Market Fund \- VMFXX). Vanguard funds are historically conservative, often favoring T-bills over aggressive repo strategies.  
* **BlackRock:** Through its liquidity funds (e.g., FedFund, T-Fund), BlackRock is a critical connector between MMF cash and the repo market, leveraging its technological platform (Aladdin) to optimize collateral flows.  
* **JPMorgan Asset Management:** A key player in Prime and Government space, often innovating in the use of sponsored repo to facilitate client needs.  
* **Federated Hermes & Dreyfus (BNY Mellon):** Institutional stalwarts that manage significant corporate cash pools.

These firms operate with fiduciary mandates to maximize yield for shareholders consistent with preservation of capital. In 2024 and 2025, as private market rates rose above the Fed’s RRP rate, these managers aggressively reallocated portfolios to capture the spread, driving the depletion of the RRP.

---

## **2\. RRP Usage History**

The trajectory of the ON RRP facility—from a backwater tool to a $2.5 trillion juggernaut and back to near-zero—is the defining narrative of post-pandemic money markets.

### **2.1 The Mechanics of the Facility**

The Overnight Reverse Repurchase Agreement (ON RRP) facility allows eligible counterparties (primarily MMFs and GSEs) to lend cash to the Federal Reserve overnight, collateralized by Treasuries held in the Fed's System Open Market Account (SOMA). Crucially, the Fed sets a fixed "offering rate" (the RRP rate) which acts as a **soft floor** for short-term interest rates. No rational actor should lend cash in the private market at a rate significantly below what they can earn risk-free from the Fed.

### **2.2 The Era of Buildup (2021–2022)**

The accumulation of $2.55 trillion in the RRP was driven by a confluence of supply-demand imbalances:

1. **Fiscal Stimulus & Deposit Flight:** Trillions in pandemic stimulus landed in bank deposits. Banks, constrained by the Supplementary Leverage Ratio (SLR), discouraged these non-operating deposits, pushing them into MMFs.  
2. **Collateral Scarcity:** Simultaneously, the U.S. Treasury reduced bill issuance to manage the debt ceiling and spend down its general account. There were simply not enough T-bills to absorb the cash flooding into MMFs.  
3. **The "Repo Floor":** Private repo rates traded below the RRP rate due to the glut of cash. MMFs, seeking the highest risk-free yield, flocked to the Fed.

During this period, the RRP acted as a "sterilization" tool, keeping excess liquidity from pushing rates into negative territory. It was efficient, but it represented "dead money"—capital removed from the private credit creation cycle.

### **2.3 The Drivers of Depletion (2023–2026)**

The drawdown of the facility, which accelerated in 2024 and completed in early 2026, was not a passive event. It was the result of a deliberate shift in market incentives orchestrated by the Fed (via QT) and the Treasury (via issuance).

* **Quantitative Tightening (QT):** As the Fed reduced its balance sheet, it drained reserves from the banking system. While RRP usage remained high initially, the aggregate reduction in liquidity eventually forced private funding rates (SOFR) to rise.  
* **The Rise of SOFR:** By late 2025, the Secured Overnight Financing Rate (SOFR)—the cost of borrowing cash against Treasuries in the private market—began to trade consistently **5 to 15 basis points above** the ON RRP rate. This spread was the signal MMFs needed to leave the Fed.  
* **The T-Bill Deluge:** The Treasury Department, acknowledging the need to refill its general account without draining bank reserves, tilted its issuance heavily toward short-term bills. Net bill issuance in 2025 exceeded $1 trillion, providing MMFs with an ample supply of high-yielding, safe assets.

**The Reallocation Trigger:** The drawdown mechanism was purely economic. MMF managers face intense competition on yield. If a fund stays in the RRP earning 5.00% while a competitor moves into T-bills earning 5.20%, the former loses assets. Thus, the "herd" moved in unison, draining the facility to \~$2.5 billion by Jan 2026\.

---

## **3\. Cash Reallocation Analysis**

The question of "Where did the $2.5 trillion go?" is answered by analyzing the asset composition of Government MMFs. The capital bifurcated into two distinct streams: direct government financing (T-bills) and private market financing (Repo).

### **3.1 The Shift to Treasury Bills**

The most significant recipient of MMF cash was the U.S. Treasury.

* **Holdings Growth:** Between April 2023 and the end of 2025, MMF holdings of Treasury bills surged by approximately **$1.7 trillion**.  
* **Current Allocation:** As of December 31, 2025, total Treasury holdings in MMFs stood at **$3.515 trillion**, representing roughly **42.4%** of total industry assets.  
* **Yield Dynamics:** This reallocation was supported by a persistent "term premium" in the bill market. Throughout late 2025, 3-month bill yields traded significantly above the overnight RRP rate (e.g., 4.09% vs implied lower RRP rate), offering attractive pickup for funds willing to extend Weighted Average Maturity (WAM).

This shift had a beneficial macroeconomic effect: it allowed the U.S. government to fund large deficits by tapping the pool of "sideline cash" at the Fed, rather than draining scarce reserves from the banking system.

### **3.2 The Resurgence of Private Repo**

The second major destination was the private repurchase agreement market.

* **Repo Holdings:** MMFs held **$2.992 trillion** in total repo agreements as of Dec 31, 2025\.  
* **Composition Shift:** In 2022, nearly all MMF repo was with the Fed (ON RRP). In 2026, with RRP at zero, this $2.99 trillion represents lending to **private dealers**. This is a massive rotation of credit risk—from the central bank to the private banking sector.  
* **The Mechanism: Sponsored Repo:** A critical enabler of this shift was the expansion of the Fixed Income Clearing Corporation’s (FICC) Sponsored Service.  
  * *Volume:* Sponsored repo volumes reached peak levels of over **$2.48 trillion** in mid-2025.  
  * *Function:* This service allows MMFs (who are not direct members of the clearinghouse) to lend cash to FICC, with a dealer sponsoring the trade. FICC then nets this trade against the dealer's reverse repo (lending) to hedge funds.  
  * *Importance:* This netting allows dealers to intermediate trillions of dollars without clogging their balance sheets or violating SLR requirements. Effectively, MMF cash is flowing through FICC to fund hedge fund arbitrage positions.

### **3.3 Bank Deposits and Other Assets**

A smaller portion of cash moved into bank deposits (certificates of deposit and time deposits), primarily via Prime funds.

* **Bank Deposits:** While data is less granular, Prime funds increased holdings of CDs and CP slightly, but regulatory liquidity fees limit the attractiveness of this sector.  
* **Agency Debt:** MMFs also increased holdings of Federal Agency debt (GSEs) to **$1.01 trillion** (12.2% of assets), providing funding for the housing market.

**Summary of Reallocation:**

The "dead money" of the RRP has been successfully recycled. Roughly 60% went to fund the fiscal deficit (T-bills) and 40% went to fund market liquidity and leverage (Private Repo).

---

## **4\. Market Impact Assessment**

The reallocation of $2.5 trillion has fundamentally altered the pricing structure and volatility profile of short-term markets.

### **4.1 Impact on T-Bill Yields**

The T-bill market has transitioned from a state of acute scarcity (yields below RRP) to a state of equilibrium.

* **Yield Normalization:** With MMFs now holding \>$3.5 trillion in bills, they have become the marginal buyer. T-bill yields now trade consistently above the OIS curve, reflecting the supply pressure from the Treasury.  
* **Issuance Sensitivity:** The market is now highly sensitive to auction sizes. In late 2025, fears of increased issuance led to temporary yield spikes, as MMFs demanded higher concessions to absorb additional supply.  
* **Supply Dependency:** The stability of the MMF sector is now partially dependent on the Treasury maintaining high bill issuance. A reduction in bill supply (e.g., due to a shift to coupons or a debt ceiling standoff) would force MMFs back into the repo market, crushing rates.

### **4.2 Impact on Repo Rates (SOFR)**

The private repo market has become the primary venue for price discovery, leading to higher volatility.

* **SOFR \> IORB:** In the "abundant" regime, SOFR traded well below the Interest on Reserve Balances (IORB). In the current "ample/scarce" regime, SOFR frequently trades *above* IORB. This indicates that banks are no longer flooding the market with excess reserves; instead, they are conserving cash, forcing borrowers to pay a premium.  
* **Volatility Events:** The market has witnessed periodic spikes in SOFR, particularly around month-end and quarter-end dates (e.g., September 2025, December 2025). These spikes, ranging from 5 to 20 basis points, signal that the "excess" liquidity buffer is gone. The market clears, but at a higher and more volatile price.  
* **The Dealer Squeeze:** Dealers are operating with lower excess capacity. When MMFs pull back lending (even slightly) or when hedge fund demand surges, repo rates snap higher. This "inelasticity" is a hallmark of the post-RRP environment.

### **4.3 Dealer Funding & The Balance Sheet Trilemma**

The depletion of the RRP has exposed the "Balance Sheet Trilemma" facing the Federal Reserve and dealers.

* **The Trilemma:** The Fed cannot simultaneously achieve (1) a small balance sheet, (2) low rate volatility, and (3) limited market intervention. By shrinking the balance sheet (draining RRP), the Fed has accepted higher volatility (2) and effectively mandated private sector intervention.  
* **Dealer Constraints:** Dealers are constrained by the GSIB surcharge and SLR. They cannot expand their balance sheets infinitely to absorb MMF cash.  
* **The Sponsored Repo Fix:** The market's solution has been the massive adoption of FICC Sponsored Repo. This allows dealers to net trades, effectively making the balance sheet cost of intermediation near zero. *However*, this concentrates risk in the clearinghouse and relies on the continued availability of netting. If netting breaks (e.g., due to asymmetric flows), dealer capacity would collapse, and rates would spike.

---

## **5\. Stress Scenario Analysis**

The most critical question for risk managers is: *What happens when the system is stressed?* The RRP acted as a passive shock absorber. Its removal changes the physics of a crisis.

### **5.1 Historical Lessons: March 2020 & Sept 2019**

To understand 2026 risks, we recall two key events:

* **September 2019 (Repo Spike):** Reserves fell too low due to tax payments. Repo rates spiked to 10%. MMFs had cash but dealers couldn't intermediate due to balance sheet constraints. *Lesson: Cash doesn't matter if pipes (dealers) are clogged.*  
* **March 2020 (Dash for Cash):** Prime MMFs faced runs. Government MMFs saw inflows. However, the Treasury market seized up because hedge funds (basis traders) had to liquidate Treasuries, and dealers couldn't absorb the selling. *Lesson: Leverage unwinds break the Treasury market.*

### **5.2 The 2026 "No Buffer" Scenario**

In a hypothetical 2026 stress event (e.g., a geopolitical shock or sudden rate recalibration), the dynamics would be distinct:

* **Liquidity Lock:** In 2023, MMFs could meet redemptions by just reducing their RRP balance (which settles daily). In 2026, MMFs hold T-bills and Term Repo. To raise cash, they must *sell bills* or *refuse to roll repo*.  
* **The Transmission Mechanism:**  
  1. **Shock:** Investors redeem from Prime/Govt funds.  
  2. **Reaction:** MMFs stop rolling sponsored repo trades to hoard liquidity.  
  3. **Impact:** Hedge funds (the borrowers in sponsored repo) lose funding.  
  4. **Result:** Hedge funds are forced to sell Treasuries (unwind basis trades).  
  5. **Feedback Loop:** Treasury prices fall \-\> MMF NAVs fluctuate \-\> more redemptions.

### **5.3 The Role of the Standing Repo Facility (SRF)**

The Federal Reserve established the Standing Repo Facility (SRF) to act as a ceiling on rates, replacing the RRP floor.

* **Function:** Dealers can borrow cash from the Fed against Treasuries at a penalty rate (top of target range).  
* **Performance:** In late 2025, SRF usage reached **$74.6 billion**, its highest level yet. This confirms the facility works to cap extreme spikes.  
* **Limitation:** The SRF is reactive. It requires dealers to hold eligible collateral and be willing to endure the "stigma" or operational cost of usage. It does not provide the passive, frictionless elasticity that the RRP provided. While it prevents a 2019-style explosion, it does not prevent intraday volatility or the credit contraction described above.

---

## **6\. Key Data Points**

The following table synthesizes the most current data available (as of Jan 2026\) to benchmark the ecosystem.

| Metric | Value | Date | Source | Context |
| :---- | :---- | :---- | :---- | :---- |
| **Total MMF Assets** | **$7.70 Trillion** | Jan 21, 2026 | ICI | Record high; continued inflows despite rate normalization. |
| **Gov. MMF Assets** | **$6.32 Trillion** | Jan 21, 2026 | ICI | Dominant sector; primary lender in repo markets. |
| **Prime MMF Assets** | **$1.24 Trillion** | Jan 21, 2026 | ICI | constrained by liquidity fee rules; steady growth. |
| **ON RRP Usage** | **\~$2.5 Billion** | Jan 2026 | NY Fed | Effectively zero; down from $2.55T peak. |
| **MMF Repo Holdings** | **$2.99 Trillion** | Dec 31, 2025 | SEC N-MFP | Represents private lending to dealers/hedge funds. |
| **MMF Treasury Holdings** | **$3.52 Trillion** | Dec 31, 2025 | SEC N-MFP | Massive shift to direct government financing. |
| **Sponsored Repo Volume** | **\~$2.5 Trillion** | Mid-2025 | OFR/DTCC | Proxy for MMF-to-Hedge Fund liquidity flow. |
| **Hedge Fund UST Exposure** | **\~$1.85 Trillion** | Dec 2024 | SEC Form PF | Estimated size of basis trade positions (lagged). |
| **SRF Usage** | **$74.6 Billion** | Dec 31, 2025 | NY Fed | Record high; indicates funding stress at year-end. |
| **3M T-Bill Yield** | **\~4.09%** | Late 2025 | Market Data | Trading above RRP rate; sensitive to supply. |

---

## **7\. Flow Diagram**

The following conceptual visualization illustrates the structural transformation of the funding market.

### **Phase 1: The RRP Buffer Era (2021–2023)**

*Characterized by passive sterilization and severed links between MMFs and private borrowers.*

Code snippet

graph TD  
    Households\[Households / Institutions\] \--\>|Cash Inflows| MMFs\[Money Market Funds\]  
    MMFs \--\>|Excess Cash ($2.5T)| FedRRP  
    FedRRP \-- "Dead Money" \--\> FedBalanceSheet  
      
    subgraph Private Market  
    Dealers \-- Limited Repo \--\> HedgeFunds\[Hedge Funds\]  
    Treasury \-- Limited Bill Supply \--\> MMFs  
    end  
      
    style FedRRP fill:\#f9f,stroke:\#333,stroke-width:4px

### **Phase 2: The Post-Depletion Era (2026)**

*Characterized by active lending, re-leveraging, and high interconnectedness.*

Code snippet

graph TD  
    Households\[Households / Institutions\] \--\>|Cash Inflows| MMFs\[Money Market Funds\]  
      
    MMFs \--\>|\~$3.5T (Direct Financing)| Treasury  
    MMFs \--\>|\~$3.0T (Repo Lending)| FICC  
      
    subgraph "The Leverage Machine"  
    FICC \-- Netting Mechanism \--\> Dealers  
    Dealers \-- Repo Funding \--\> HedgeFunds\[Hedge Funds\]  
    HedgeFunds \-- "Basis Trade" \--\> TreasuryFutures  
    end  
      
    FedRRP \-.-\> MMFs  
    Dealers \-.-\>|Backstop ($75B)| SRF  
      
    style FICC fill:\#bbf,stroke:\#333,stroke-width:4px  
    style Treasury fill:\#dfd,stroke:\#333,stroke-width:2px

**Key Shift:** In Phase 2, MMF cash is no longer sitting at the Fed. It is supporting the T-bill market (green flow) and, crucially, the Hedge Fund leverage complex (blue flow) via FICC. A breakage in the "FICC" node transmits stress directly to MMFs and the Treasury market.

---

## **8\. Risk Assessment**

With the ecosystem rewired as described above, several specific risks emerge that were dormant during the RRP era.

### **8.1 The "Basis Trade" Unwind**

The most acute risk is the concentration of MMF cash funding the Treasury Basis Trade.

* **The Structure:** Hedge funds are short futures and long cash Treasuries. They fund the cash position via repo. MMFs provide the repo cash (via FICC).  
* **The Risk:** If repo rates spike (due to scarcity) or margins increase (volatility), the trade becomes unprofitable. Hedge funds unwind by selling cash Treasuries.  
* **Amplification:** In 2020, dealers absorbed these sales. In 2026, dealers are SLR-constrained. If MMFs pull back repo funding simultaneously (due to their own liquidity needs), the market faces a "buyer's strike." This could crash Treasury prices, causing a VaR shock that ripples through the system.

### **8.2 The "Debt Ceiling" Cliff (Mid-2026)**

Projections indicate the U.S. will reach its debt limit again in mid-2026.

* **The Scenario:** The Treasury must stop issuing bills to conserve cash.  
* **Impact on MMFs:** MMFs face a shortage of assets (T-bills maturing without replacement).  
* **The Trap:** In 2021/2023, MMFs dumped excess cash into the RRP. In 2026, with the RRP rate potentially unattractive vs. market rates (or if the Fed actively discourages usage), MMFs may be forced to lend at depressed rates or take on unwanted credit risk to maintain yield. This compresses spreads and increases fragility.

### **8.3 Reserve Scarcity Miscalculation**

The Federal Reserve is targeting a "Lowest Comfortable Level of Reserves" (LCLoR) to end QT.

* **The Risk:** The distribution of reserves is uneven. While aggregate reserves may look ample, smaller banks or specific dealers may face acute shortages.  
* **MMF Role:** MMFs are the "swing factor." If MMFs suddenly decide to extend WAM (buy more bills) and reduce repo, they drain liquidity from dealers. If they shorten WAM (hoard cash), they flood the repo market. The unpredictability of MMF behavior makes estimating LCLoR incredibly difficult for the Fed.

---

## **9\. Monitoring Recommendations**

To anticipate funding stress in this new regime, analysts should monitor the following high-frequency indicators:

### **Primary Indicators (Daily/Weekly)**

1. **FICC Sponsored Repo Volumes:**  
   * *Source:* DTCC / OFR Short-term Funding Monitor.  
   * *Signal:* A sharp contraction (e.g., \>$100B drop in a week) suggests hedge fund deleveraging or dealer capacity constraints.  
2. **SOFR vs. IORB Spread:**  
   * *Source:* NY Fed.  
   * *Signal:* SOFR trading consistently \>5 bps above IORB signals structural reserve scarcity. Intraday spikes \>20 bps signal acute stress.  
3. **SRF Usage:**  
   * *Source:* NY Fed (H.4.1 release).  
   * *Signal:* Regular usage outside of quarter-end dates indicates the "soft ceiling" is being tested and the interbank market is broken.

### **Secondary Indicators (Monthly)**

4. **MMF Weighted Average Maturity (WAM):**  
   * *Source:* Crane Data / SEC Form N-MFP.  
   * *Signal:* A rapid shortening of WAM (e.g., from 40 days to 15 days) indicates MMF managers are "hoarding liquidity" in anticipation of redemptions or volatility.  
5. **Net T-Bill Issuance Forecasts:**  
   * *Source:* U.S. Treasury Quarterly Refunding Announcement (QRA).  
   * *Signal:* Unexpected cuts to bill issuance will force MMF cash back into repo/RRP, distorting rates.

---

## **10\. Data Gaps**

Despite the wealth of data, significant blind spots remain:

1. **Real-Time Hedge Fund Leverage:** SEC Form PF data is lagged by months. We cannot see the *current* size of the basis trade, only verify its existence in retrospect. Proxy measures (Futures Open Interest) are imperfect.  
2. **Bilateral Repo Opacity:** While FICC Sponsored Repo is transparent, a portion of the market remains "Non-Centrally Cleared Bilateral Repo" (NCCBR). This segment is opaque and may harbor hidden leverage or concentration risks that official statistics miss.  
3. **MMF Shareholder Concentration:** We lack granular, real-time data on *who* owns the MMF shares (e.g., how much is "hot money" from tech corporates vs. sticky retail cash). This makes predicting redemption waves difficult.

---

## **Sources**

