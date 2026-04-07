# **The Information Architecture of Global Capital Markets: Systems of Decision Support and Risk Governance in Institutional Trading Operations**

The information architecture of institutional trading desks represents a sophisticated synthesis of real-time data ingestion, cognitive load management, and rigorous governance protocols designed to convert massive waves of market data into actionable intelligence. In the high-frequency environment of modern finance, the challenge for professional operations has shifted from the acquisition of data to its effective prioritization and display.1 As global capital markets grow in size and complexity, institutional desks utilize "Single Pane of Glass" (SPoG) monitoring architectures and specialized user experience (UX) philosophies to prevent decision paralysis.1 This architectural approach unifies metrics, logs, traces, and alerts into a centralized view, allowing risk managers and traders to maintain a "Single Source of Truth".3 The following analysis explores the specific mechanisms through which sell-side research, risk aggregation, terminal design, and oral communication systems are integrated to support institutional decision-making under both normal and crisis regimes.

## **The Lifecycle of Sell-Side Research and Internal Distribution**

The distribution of sell-side research to traders and institutional clients is a highly structured workflow governed by the dual needs of speed and regulatory compliance. At the core of this process are SaaS applications like BlueMatrix, which provide the authoring and distribution infrastructure for leading investment banks.6 These platforms are designed to streamline the publishing process on a global scale, utilizing a "componentized content framework" that enables simultaneous, multi-author editorial access to individual documents.5 This architecture allows for the rapid generation of morning notes, sector reports, and deep-dive analysis while maintaining strict version control and a centralized database of reusable multimedia assets.5

### **Research Distribution and Sales Enablement**

The prioritization of research is managed through the integration of publishing platforms with Capital Markets CRMs, such as Tier1.9 These systems provide "data-driven intelligence" to help sales and trading teams identify which clients should receive specific research signals first. This prioritization is based on "Client Mindshare and Walletshare" analysis, where the CRM tracks client interactions, research consumption, and corporate access events to determine the "next best action" for revenue generation.9 To ensure compliance with MiFID II and other regulatory mandates, these systems incorporate automated interaction tracking and consumption reporting, which ensures that research is only distributed to entitled clients and that all interactions are properly logged for audit purposes.5

| Workflow Component | Mechanism | Institutional Objective |
| :---- | :---- | :---- |
| Authoring | Cloud-based collaborative editing and model-data integration.5 | Compression of time-to-market for proprietary trade ideas. |
| Validation | Automated data consistency checks and calculation engines.8 | Reduction of "fat-finger" errors and data inaccuracies prior to publication. |
| Distribution | One-click multi-channel delivery (PDF, HTML5, RIXML).5 | Simultaneous delivery to internal desks and external aggregators like Bloomberg. |
| Tracking | Granular readership analytics and interaction logging.5 | Measurement of "broker vote" potential and client engagement.5 |

The interaction between research desks and traders is further facilitated by specialized tools like "RMS Partners," which allow analysts to upload model data directly from Excel into a centralized database.8 This ensures that the data driving a trade recommendation is identical to the data used in the official research report, eliminating discrepancies that can occur during manual entry. Furthermore, sales enablement tools allow for the creation of targeted, custom emails sent directly from Outlook, ensuring that the most relevant research reaches the most active traders without getting lost in general distribution lists.5

## **Portfolio Risk Aggregation and the Single Pane of Glass Architecture**

The risk management function within an institutional desk requires the aggregation of risk metrics across thousands of positions and multiple asset classes on a single screen. This is achieved through "Single Pane of Glass" (SPoG) monitoring, which provides a unified view of the system's health, performance, and risk exposure.3 For a risk manager, this means moving away from "reactive, component-based" monitoring to a "proactive, predictive approach".10

### **The Technical Stack of Risk Dashboards**

Modern enterprise-grade risk dashboards, such as those built for Quantitative Risk monitoring, utilize high-performance data pipelines.11 A typical stack might involve Python for metric calculation, Redis for low-latency caching, and FastAPI for real-time data access, with visualizations rendered in interactive frameworks like Plotly or Streamlit.11 This architecture supports sub-second refresh rates for critical metrics, such as Delta, Gamma, and Vega (the Greeks), alongside more complex calculations like Value-at-Risk (VaR) and Expected Shortfall.11

The "Inverted Pyramid" model of dashboard design is often employed to manage the density of this information:

1. **Top Layer (Status and Targets):** High-level indicators that answer "Are we within our limits?" (e.g., aggregate VaR vs. capital buffers).12  
2. **Middle Layer (Trends and Comparisons):** Charts showing how risk has evolved over the session and how current exposures compare to historical norms.12  
3. **Bottom Layer (Details and Owners):** Granular position-level data and counterparty exposures that allow for immediate troubleshooting or hedging actions.3

### **Standardized Metrics for Institutional Risk Reporting**

| Metric Type | Key Indicators | Institutional Application |
| :---- | :---- | :---- |
| Market Risk | Portfolio VaR, Marginal VaR, Component VaR, Greeks.11 | Determining the sensitivity of the entire portfolio to price, time, and volatility. |
| Credit Risk | Counterparty Exposure, Potential Future Exposure (PFE), Credit Spreads.11 | Monitoring the solvency and default risk of trading partners. |
| Operational Risk | System Downtime, Connectivity Status (FIX/SWIFT), Process Failures.11 | Ensuring the technical plumbing of the desk remains functional during high volatility. |
| Compliance Risk | Residual Risk Scores, Control Effectiveness, Regulatory Breaches.15 | Tracking adherence to internal mandates and external laws like GDPR or SOX.15 |

The effective display of these metrics relies on "Visual Hierarchy" and the "F-Pattern" of scanning.17 The "Golden Triangle" at the top-left of the screen is reserved for the most critical risk indicators, such as the total aggregate risk score and any active limit breaches.17 Semantic coloring is strictly applied: Red signals a breach or negative trend, Green signals compliance, and Neutral tones are used for categorical data to reduce extraneous cognitive load.18

## **The Bloomberg Terminal: UX Design and Alert Ecosystems**

The Bloomberg Terminal's status as a ubiquitous tool on trading desks is largely due to its sophisticated information architecture, which focuses on "concealing complexity".1 With over 20,000 functions, the Terminal could easily overwhelm users; however, Bloomberg's UX philosophy is built on incremental innovation and a deep understanding of trader workflows.1

### **Concealing Complexity through Design**

Bloomberg’s CTO, Shawn Edwards, notes that the secret to the Terminal’s success is providing a "seamless experience" by masking underlying technical complications.1 This is achieved through several specific design principles:

* **Balancing Innovation with Familiarity:** Changes are rolled out gradually (e.g., changing a visual gradient little by little each month) to avoid disrupting mission-critical workflows.1  
* **Specialized Typography:** Modern TrueType fonts were commissioned to include specific finance-related glyphs, such as fraction glyphs for 1/64ths, which are essential for fixed-income traders but often ignored by standard OS fonts.1  
* **Staggered Rollouts:** Using "feature switches," updates are deployed to small groups of users first, creating an early warning system for any potential disruption to the trading day.1

### **Alert Architecture: ALRT and MON**

The Terminal's notification system is divided into two primary categories: market alerts (ALRT) and enterprise monitoring (MON).14 The market alert system allows traders to set custom conditions based on price movements, news keywords, or economic events.21 The "Alert Catcher" centralizes these notifications, providing a persistent feed that can be synced between the desktop and mobile devices.21

For enterprise-level operations, the "Connectivity & Integration" (CIS) monitoring and alerting system tracks the health of data feeds and connectivity protocols like FIX, SWIFT, and FTP.14 This system is designed for technologists and market data teams to identify and self-remediate issues in real-time, such as an MQ connectivity failure or an integration error between an Order Management System (OMS) and an accounting ledger.14 This proactive approach minimizes downtime and ensures that the information flowing into the trader's terminal is accurate and timely.14

| Feature | Mechanism | Effect on Information Flow |
| :---- | :---- | :---- |
| Interactive TV | Side-by-side video with clickable links to Terminal functions.20 | Converts passive news consumption into active, actionable research. |
| ALRT Catcher | Centralized, cross-device feed of condition-based notifications.21 | Ensures traders do not miss critical shifts in sentiment while away from their desks. |
| MON Dashboards | Visual status of all enterprise-level data feeds and FIX sessions.14 | Reduces the "time-to-resolution" for technical failures in the trading plumbing. |
| ASKB Agentic AI | Direct AI integration into Terminal functions for insight discovery.20 | Compresses complex data queries into natural language responses. |

## **Trading Floor Communication: Squawk Boxes and Morning Calls**

Despite the digitization of trading, oral communication through "Squawk Boxes" and morning calls remains a critical layer of the information architecture. These systems are designed to compress complex, multidimensional information into actionable briefings that can be consumed while the trader is focused on their screens.24

### **The Squawk Box and "Hoot 'n' Holler" Systems**

The "Squawk Box" is a speaker box that is part of a "hoot 'n' holler" system—an interoffice intercom that keeps traders in constant contact.26 This system operates on an open telephone circuit, separate from the standard phone system, allowing for the instantaneous broadcast of information such as the morning market report.26 The squawk box acts as a "microphone" for senior analysts to amplify their message to the sales and trading desks, who then distill it into a "short and sweet" version for their clients.24

### **Information Compression via the ADViCE Framework**

To ensure morning calls are efficient, analysts often follow structured frameworks like ADViCE (Aware, Differentiated, Validated, Conclusion-oriented, and Easy to consume).25 This framework forces the speaker to prioritize the most important elements of a trade idea:

* **Conclusion-oriented:** The stock name and recommendation (Buy/Sell) must be mentioned within the first two sentences.25  
* **Differentiated:** The analyst must explain how their view differs materially from the market consensus (e.g., a different earnings forecast or valuation multiple).25  
* **Validated:** The thesis must be supported by independent research, such as conversations with industry sources outside the target company.25  
* **Easy to Consume:** Jargon is minimized, and insights are quantified whenever possible to prevent the listener from having to compute the data themselves.25

### **Verbal and Hand Signal Shorthand**

On high-noise trading floors, or in legacy pit environments like the CME, verbal communication is further compressed into hand signals.28 These signals provide a low-latency method for transmitting price and quantity information without the risk of being drowned out by the noise of the floor.29

| Concept | Hand Signal Mechanism | Meaning/Encoding |
| :---- | :---- | :---- |
| Bid (Buy) | Palms facing toward the body.28 | "Bringing something in toward you." |
| Offer (Sell) | Palms facing away from the body.28 | "Pushing something away from you." |
| Price (1-5) | Fingers straight up.28 | Final digit of the bid/offer (e.g., "5" for $45). |
| Price (6-9) | Hand held sideways (parallel to floor).29 | Final digit for higher-range numbers. |
| Quantity (10s) | Touching price signal to the forehead.30 | Multiples of ten contracts. |
| Quantity (100s) | Flashing price signal, then a fist to the forehead.30 | Multiples of 100 contracts. |

## **Reconciling Conflicting Signals: Bayesian Decision Logic**

Portfolio managers (PMs) are constantly bombarded with conflicting signals from different analysts, news feeds, and quantitative models. Handling this information overload requires a disciplined mental model, such as "Bayesian Edge Investing" (BEI).32

### **Bayesian Edge Investing (BEI)**

The BEI framework replaces "static rationality" with probabilistic reasoning. Investment ideas are treated as evolving hypotheses that must be updated as new evidence emerges.32 Instead of giving every data point equal weight, a manager evaluates new signals based on their "diagnostic power".32 This involves asking:

1. How likely is this information under competing hypotheses (e.g., if the company is succeeding vs. if it is failing)?  
2. How much weight should it carry in updating current conviction levels? 32

The Bayesian update formula is used to quantify the shift in conviction:

![][image1]  
By calculating a specific percentage of confidence (e.g., shifting from 25% to 43.75% based on a positive clinical trial result), the PM can move away from vague emotional reactions and align capital more precisely with conviction.32

### **Group Decision-Making and Consensus Models**

When a desk receives conflicting expert opinions, PMs may use "Bayesian Best-Worst Method" (BWM) or "Consensus-based IF EDAS" models.33 Unlike traditional voting, these models integrate the judgments of multiple experts through a probabilistic approach that avoids losing the impact of singular, "outlier" opinions which may actually carry the "edge".33 This structured approach helps identify the strengths and weaknesses of different investment options by eliminating unnecessary pairwise comparisons and focusing on the relative importance of each criterion.33

## **The Risk Dashboard: Hierarchy, Metrics, and Escalation Triggers**

A risk dashboard is the "nerve center" of the desk, providing a centralized visual interface for Key Risk Indicators (KRIs).2 The architecture of these dashboards is designed to prove that governance structures are working, supporting frameworks like SOX, GDPR, and ISO.16

### **Hierarchy of Information and Action**

The hierarchy of a risk dashboard is established to facilitate "management by exception," a PRINCE2 principle where only deviations from agreed-upon tolerances are escalated.35

* **Operational Level (L1):** Handles routine troubleshooting and minor scheduling adjustments. Triggers include workflow blocks for more than 4 hours.16  
* **Tactical Level (L2):** Authorized for resource reallocation and budget adjustments. Triggers include Resource conflicts or minor budget variances.16  
* **Strategic Level (L3):** Responsible for project cancellation or major scope pivots. Triggers include client churn risk or major system failures.16  
* **Executive Level (L4):** Involves the C-suite for existential risks or major compliance breaches.16

### **Escalation Matrix and Triggers**

| Trigger Event | Response Time | Escalation Path |
| :---- | :---- | :---- |
| System down for all users (Critical).16 | 15 minutes. | Service Desk → SysAdmin → CIO → Vendor. |
| Feature broken for critical department (High).16 | 2 hours. | Support Engineer → Manager → Head of Operations. |
| Potential financial losses exceed acceptable limits.13 | Immediate. | Risk Manager → Risk Committee → Board of Directors. |
| Bias detection in AI output or data privacy flag.16 | 8 hours. | AI Engineer → Data Science Lead → Ethics Committee. |

The escalation matrix kills decision paralysis by giving teams "pre-approved paths for action".16 When a specific threshold is hit (e.g., a 10% budget variance or a critical supplier missing a delivery), the next step happens automatically, ensuring that critical issues receive appropriate senior attention before they develop into larger problems.13

## **Managing Regime Changes: Normal Markets vs. Crisis**

Institutional desks must adapt their information flow protocols as the market shifts between "regimes"—periods of distinct economic behavior and volatility.37 A "MRI" (Market Regime Indicator) is often used to identify the level of risk aversion/appetite using forward-looking market information.38

### **The Six Market Regimes**

Traders often use a 60-second daily framework to identify which of the six market regimes they are in, based on trend direction (price relative to the 200-day moving average) and volatility (VIX readings) 37:

1. **Bull Quiet:** Low volatility, rising prices. Normal position sizes and standard stops apply.37  
2. **Bull Volatile:** Rising prices but with wider swings. Position sizes are typically reduced by 25-50%.37  
3. **Bear Quiet:** Orderly decline. Normal sizing for short trend-following strategies.37  
4. **Bear Volatile:** VIX \> 25\. High correlations across assets. Capital preservation is the priority; position sizes reduced by \>50%.37  
5. **Sideways Quiet:** Mean-reversion strategies (buy at support, sell at resistance) are most effective.37  
6. **Sideways Volatile:** High movement without follow-through. Professional traders often step aside entirely.37

### **Crisis Mode: The War Room Protocol**

When a disruption crosses defined institutional thresholds (e.g., liquidity compression below tolerance or a cyber breach), the desk standingly activates a "Crisis War Room".39 This is a "controlled execution environment" designed to move faster than the threat.39

**Operating Rhythm of the War Room:**

* **Daily Granularity:** Cash crises strike in 24-hour increments. A 13-week cash-flow model serves as the "nerve center," reconciling to yesterday’s bank ledger cent-for-cent.40  
* **Concentrated Authority:** Leadership collapses into a compact structure (Incident Lead, Domain Expert, Comms Owner) to preserve decision velocity.39  
* **The 20-Minute Huddle:** A ritual of "present, challenge, decide, document." Every conversation ends with a binary outcome: Pay, Defer, or Cancel.40  
* **Secure Environment:** Communications are routed through encrypted channels, and document retention policies are strictly enforced to protect future legal defense.39

## **Failure Modes: Flash Crashes and Information Overload**

Despite advanced information architecture, systemic failures occur, most notably during "Flash Crashes." These events demonstrate the danger of "HFT dominance" and the "withdrawal of liquidity" when information flows become too volatile for human or algorithmic interpretation.42

### **The 2010 Flash Crash Analysis**

On May 6, 2010, the U.S. stock market experienced a trillion-dollar crash that lasted 36 minutes.42 The primary cause was the execution of a massive sell order (75,000 E-mini futures) by Waddell & Reed via a simple automated algorithm.43

* **The Domino Effect:** The algorithm sold the contracts in just 20 minutes—a trade that usually takes 5 hours.43 This aggressive selling set off a chain reaction among High-Frequency Trading (HFT) programs.43  
* **Liquidity Evaporation:** As volatility spiked, both human traders and HFT programs opted to "cease trading entirely" to avoid unknown risks.43 This withdrawal of buyers accelerated the crash, as the sell orders were met with no willing participants.43  
* **Information Asymmetry:** The SEC's inability to monitor these technological advances in real-time meant that no specific reason for the plunge was identified until months later, contributing to a permanent loss of investor confidence.45

### **Secondary Failure Modes: Cognitive Overload and "Metric Soup"**

Failure in information flow often stems from "Extraneous Cognitive Load"—mental effort wasted on poor design.19 "Metric Soup" occurs when too many visuals compete for attention, leading to analysis paralysis where managers spend 20 minutes cross-referencing charts instead of making immediate decisions.18 Common design failures include:

* **Lack of Context:** A dashboard displaying "Sales: $50,000" without a historical comparison or target forces the user to ask, "Is that good?" 18  
* **Inconsistent Color Coding:** Overuse of bright colors for decoration rather than signaling alerts confuses the brain’s ability to spot anomalies.47  
* **Poor Data Hygiene:** Lack of a "Single Source of Truth" results in conflicting numbers across different teams, destroying trust in the dashboard during high-stress scenarios.12

## **Conclusion: Synthesizing Information Flow for Decision Support**

The institutional trading desk of the future must be built on the principle of "resilience through simplification." Whether it is Bloomberg's philosophy of concealing complexity, the Bayesian PM's quantitative conviction, or the risk manager's "Single Pane of Glass," the objective remains the same: reducing the friction between data and decision.1

For a multi-agent financial research system, the key takeaways from professional operations involve the implementation of:

1. **Strict Information Hierarchy:** Moving from high-level "Status" to granular "Detail" on demand.12  
2. **Adaptive Regime Protocols:** Shifting the "Operational Rhythm" and "Decision Authority" when market volatility enters a crisis state.37  
3. **Automated Escalation Matrix:** Pre-defining thresholds to ensure that no "Black Swan" event is missed due to organizational confusion.13

By mirroring these professional architectures, automated systems can manage the "unprecedented" complexity of modern markets without falling victim to the information overload that has historically triggered systemic failures.43

#### **Works cited**

1. How Bloomberg Terminal UX designers conceal complexity, accessed April 7, 2026, [https://www.bloomberg.com/company/stories/how-bloomberg-terminal-ux-designers-conceal-complexity/](https://www.bloomberg.com/company/stories/how-bloomberg-terminal-ux-designers-conceal-complexity/)  
2. Your Guide to Effective Risk Management Dashboards | MetricStream, accessed April 7, 2026, [https://www.metricstream.com/learn/risk-management-dashboard.html](https://www.metricstream.com/learn/risk-management-dashboard.html)  
3. What is Single Pane of Glass Monitoring and How It Works \- Last9, accessed April 7, 2026, [https://last9.io/blog/what-is-single-pane-of-glass-monitoring-and-how-it-works/](https://last9.io/blog/what-is-single-pane-of-glass-monitoring-and-how-it-works/)  
4. Top 10 Single Pane of Glass IT Dashboards: Features, Pros, Cons & Comparison, accessed April 7, 2026, [https://www.devopsschool.com/blog/top-10-single-pane-of-glass-it-dashboards-features-pros-cons-comparison/](https://www.devopsschool.com/blog/top-10-single-pane-of-glass-it-dashboards-features-pros-cons-comparison/)  
5. Platforms \- BlueMatrix, accessed April 7, 2026, [https://www.bluematrix.com/www3/Platforms.action](https://www.bluematrix.com/www3/Platforms.action)  
6. Enterprise Account Executive \- BlueMatrix | Built In NYC, accessed April 7, 2026, [https://www.builtinnyc.com/job/enterprise-account-executive/8926627](https://www.builtinnyc.com/job/enterprise-account-executive/8926627)  
7. Enterprise Account Executive @ BlueMatrix \- Teal, accessed April 7, 2026, [https://www.tealhq.com/job/enterprise-account-executive\_7ea1aeda887012e5c5c06441febe28e25373e](https://www.tealhq.com/job/enterprise-account-executive_7ea1aeda887012e5c5c06441febe28e25373e)  
8. RMS Partners for Research \- BlueMatrix, accessed April 7, 2026, [https://www.bluematrix.com/www3/RMSPartners.action;jsessionid=6EBEEAF6C33275A9891DF3DCD3B5A5B0](https://www.bluematrix.com/www3/RMSPartners.action;jsessionid=6EBEEAF6C33275A9891DF3DCD3B5A5B0)  
9. Equity Research, Sales and Trading CRM \- SS\&C Tier1, accessed April 7, 2026, [https://www.tier1fin.com/solutions/research-sales-and-trading/](https://www.tier1fin.com/solutions/research-sales-and-trading/)  
10. Getting Started with Single-Pane-of-Glass Service Health Dashboards \- Interlink Software, accessed April 7, 2026, [https://www.interlinksoftware.com/getting-started-with-single-pane-of-glass-service-health-dashboards](https://www.interlinksoftware.com/getting-started-with-single-pane-of-glass-service-health-dashboards)  
11. Quantitative Risk Dashboard Project Plan | PDF | Greeks (Finance) \- Scribd, accessed April 7, 2026, [https://www.scribd.com/document/985270817/171093B-Quantitative-Risk-Dashboard](https://www.scribd.com/document/985270817/171093B-Quantitative-Risk-Dashboard)  
12. Effective Dashboard Design: Principles, Best Practices, and Examples \- DataCamp, accessed April 7, 2026, [https://www.datacamp.com/tutorial/dashboard-design-tutorial](https://www.datacamp.com/tutorial/dashboard-design-tutorial)  
13. What is Risk Escalation? Definition, Process & Key Metrics \- Hyperbots, accessed April 7, 2026, [https://www.hyperbots.com/glossary/risk-escalation](https://www.hyperbots.com/glossary/risk-escalation)  
14. Monitoring & alerting increase enterprise-wide transparency for critical processes. \- Bloomberg Professional Services, accessed April 7, 2026, [https://data.bloomberglp.com/professional/sites/10/Fact-Sheet-CIS-Monitor-and-Alert.pdf](https://data.bloomberglp.com/professional/sites/10/Fact-Sheet-CIS-Monitor-and-Alert.pdf)  
15. Insights Risk Management Dashboard | MyOneTrust, accessed April 7, 2026, [https://my.onetrust.com/s/article/UUID-055463ac-fb4f-9ffd-55af-a2ce365b699b?language=en\_US](https://my.onetrust.com/s/article/UUID-055463ac-fb4f-9ffd-55af-a2ce365b699b?language=en_US)  
16. Escalation matrix template: how to build your 2026 strategy \- Monday.com, accessed April 7, 2026, [https://monday.com/blog/project-management/escalation-matrix-template/](https://monday.com/blog/project-management/escalation-matrix-template/)  
17. How Visual Hierarchy Improves Dashboard Clarity \- Phoenix Strategy Group, accessed April 7, 2026, [https://www.phoenixstrategy.group/blog/how-visual-hierarchy-improves-dashboard-clarity](https://www.phoenixstrategy.group/blog/how-visual-hierarchy-improves-dashboard-clarity)  
18. Dashboard Design Principles & Best Practices To Enhance Your Data Analysis, accessed April 7, 2026, [https://fireart.studio/blog/dashboard-design-best-practices/](https://fireart.studio/blog/dashboard-design-best-practices/)  
19. Designing Enterprise Dashboards with Cognitive Load Theory \- Fegno Technologies, accessed April 7, 2026, [https://www.fegno.com/designing-enterprise-dashboards-with-cognitive-load-theory/](https://www.fegno.com/designing-enterprise-dashboards-with-cognitive-load-theory/)  
20. Inside UX: Creating a more engaging way to experience Bloomberg Television, accessed April 7, 2026, [https://www.bloomberg.com/company/stories/inside-ux-creating-engaging-way-experience-bloomberg-television/](https://www.bloomberg.com/company/stories/inside-ux-creating-engaging-way-experience-bloomberg-television/)  
21. Bloomberg Mobile Alert Catcher, accessed April 7, 2026, [https://makeyourdesignwork.com/portfolio/work14/](https://makeyourdesignwork.com/portfolio/work14/)  
22. Bloomberg \- Mary Catlin • HCI/AI UX, accessed April 7, 2026, [http://www.marycatlin.com/bloomberg](http://www.marycatlin.com/bloomberg)  
23. How can I create custom alerts to monitor FIX Session health and status? \- Bloomberg.com, accessed April 7, 2026, [https://www.bloomberg.com/faq/question/how-can-i-create-custom-alerts-to-monitor-fix-session-health-and-status/](https://www.bloomberg.com/faq/question/how-can-i-create-custom-alerts-to-monitor-fix-session-health-and-status/)  
24. morning calls \- Wall Street Oasis, accessed April 7, 2026, [https://www.wallstreetoasis.com/forum/equity-research/morning-calls](https://www.wallstreetoasis.com/forum/equity-research/morning-calls)  
25. Use This ADViCE™: 5 Elements for Conveying Stock Calls ..., accessed April 7, 2026, [https://analystsolutions.com/use-advice-5-elements-conveying-stock-calls-successfully/](https://analystsolutions.com/use-advice-5-elements-conveying-stock-calls-successfully/)  
26. We Should Be Glad CNBC's 'Squawk Box' Isn't Called 'Hoot 'n' Holler' \- Market Realist, accessed April 7, 2026, [https://marketrealist.com/p/what-does-squawk-box-mean/](https://marketrealist.com/p/what-does-squawk-box-mean/)  
27. Stock Pitch Guide: How to Pitch a Stock in Interviews \- Mergers & Inquisitions, accessed April 7, 2026, [https://mergersandinquisitions.com/stock-pitch-guide/](https://mergersandinquisitions.com/stock-pitch-guide/)  
28. Introduction to Hand Signals \- Zaner Group, accessed April 7, 2026, [https://www.zaner.com/3.0/education/content.asp?page=ondemand/introtohands.html](https://www.zaner.com/3.0/education/content.asp?page=ondemand/introtohands.html)  
29. Open outcry \- Wikipedia, accessed April 7, 2026, [https://en.wikipedia.org/wiki/Open\_outcry](https://en.wikipedia.org/wiki/Open_outcry)  
30. Trading Floor Hand Signals: The Sign Language of Futures Trading | StoneX, accessed April 7, 2026, [https://futures.stonex.com/blog/trading-floor-hand-signals-the-sign-language-of-futures-trading](https://futures.stonex.com/blog/trading-floor-hand-signals-the-sign-language-of-futures-trading)  
31. Hand signaling (open outcry) \- Wikipedia, accessed April 7, 2026, [https://en.wikipedia.org/wiki/Hand\_signaling\_(open\_outcry)](https://en.wikipedia.org/wiki/Hand_signaling_\(open_outcry\))  
32. Bayesian Edge Investing: A Framework for Smarter Portfolio Allocation, accessed April 7, 2026, [https://rpc.cfainstitute.org/blogs/enterprising-investor/2025/bayesian-edge-investing-a-framework-for-smarter-portfolio-allocation](https://rpc.cfainstitute.org/blogs/enterprising-investor/2025/bayesian-edge-investing-a-framework-for-smarter-portfolio-allocation)  
33. An Integrated Bayesian Best–Worst Method and Consensus-Based Intuitionistic Fuzzy Evaluation Based on Distance from Average Solution Approach for Evaluating Alternative Aircraft Models from a Sustainability Perspective \- MDPI, accessed April 7, 2026, [https://www.mdpi.com/2073-8994/16/8/1086](https://www.mdpi.com/2073-8994/16/8/1086)  
34. Comprehensive Guide to Enterprise Risk Management Dashboards \- Future Ventures Corp, accessed April 7, 2026, [https://www.futureventures.ca/insights/comprehensive-guide-to-enterprise-risk-management-dashboards](https://www.futureventures.ca/insights/comprehensive-guide-to-enterprise-risk-management-dashboards)  
35. When to escalate a risk – and when to handle it yourself \- Prince2, accessed April 7, 2026, [https://www.prince2.com/usa/blog/when-to-escalate-a-risk-and-when-to-handle-it-yourself](https://www.prince2.com/usa/blog/when-to-escalate-a-risk-and-when-to-handle-it-yourself)  
36. The Escalation Matrix: Best Practices and Going Beyond \- SupportLogic, accessed April 7, 2026, [https://www.supportlogic.com/resources/blog/the-escalation-matrix-best-practices-and-going-beyond/](https://www.supportlogic.com/resources/blog/the-escalation-matrix-best-practices-and-going-beyond/)  
37. Market Regimes: Adaptation Is the Edge | by Ashim Nandi | Medium, accessed April 7, 2026, [https://medium.com/@ashimnandi07/market-regimes-adaptation-is-the-edge-b6c90504ca0f](https://medium.com/@ashimnandi07/market-regimes-adaptation-is-the-edge-b6c90504ca0f)  
38. Decoding Market Regimes \- State Street Global Advisors, accessed April 7, 2026, [https://www.ssga.com/library-content/assets/pdf/global/pc/2025/decoding-market-regimes-with-machine-learning.pdf](https://www.ssga.com/library-content/assets/pdf/global/pc/2025/decoding-market-regimes-with-machine-learning.pdf)  
39. Crisis War Room Setup & Execution \- handle.ae, accessed April 7, 2026, [https://handle.ae/business-strategy/crisis-strategy/crisis-war-room-strategy/](https://handle.ae/business-strategy/crisis-strategy/crisis-war-room-strategy/)  
40. Crisis-Liquidity War-Room Handbook | Umbrex, accessed April 7, 2026, [https://umbrex.com/resources/chief-financial-officer-handbook/crisis-liquidity-war-room-handbook/](https://umbrex.com/resources/chief-financial-officer-handbook/crisis-liquidity-war-room-handbook/)  
41. Design a Comms War Room. When your company faces a crisis — a… | by Sarel | Medium, accessed April 7, 2026, [https://medium.com/@sarel-d/design-a-comms-war-room-dbb7db663b89](https://medium.com/@sarel-d/design-a-comms-war-room-dbb7db663b89)  
42. 2010 flash crash \- Wikipedia, accessed April 7, 2026, [https://en.wikipedia.org/wiki/2010\_flash\_crash](https://en.wikipedia.org/wiki/2010_flash_crash)  
43. High-Frequency Trading and the Flash Crash: Structural Weaknesses in the Securities Markets and Proposed Regulatory Responses \- UC Law SF Scholarship Repository, accessed April 7, 2026, [https://repository.uclawsf.edu/cgi/viewcontent.cgi?article=1172\&context=hastings\_business\_law\_journal](https://repository.uclawsf.edu/cgi/viewcontent.cgi?article=1172&context=hastings_business_law_journal)  
44. Flash Crashes \- CFA Institute Research and Policy Center, accessed April 7, 2026, [https://rpc.cfainstitute.org/policy/positions/flash-crashes](https://rpc.cfainstitute.org/policy/positions/flash-crashes)  
45. How to Prevent Future Flash Crashes and Restore the Ordinary Investors' Confidence in the Financial Market \- Colorado Law Scholarly Commons, accessed April 7, 2026, [https://scholar.law.colorado.edu/cgi/viewcontent.cgi?article=1213\&context=ctlj](https://scholar.law.colorado.edu/cgi/viewcontent.cgi?article=1213&context=ctlj)  
46. High-Frequency Financial Market Simulation and Flash Crash Scenarios Analysis: An Agent-Based Modelling Approach \- JASSS, accessed April 7, 2026, [https://www.jasss.org/27/2/8.html](https://www.jasss.org/27/2/8.html)  
47. Cognitive Load in Dashboard Design: What Users Actually Understand, accessed April 7, 2026, [https://www.ghanshyamdatatech.com/cognitive-load-in-dashboard-design-what-users-actually-understand/](https://www.ghanshyamdatatech.com/cognitive-load-in-dashboard-design-what-users-actually-understand/)  
48. 10 Key Dashboard Design Principles: Analytics Best Practice \- Yellowfin, accessed April 7, 2026, [https://www.yellowfinbi.com/blog/key-dashboard-design-principles-analytics-best-practice](https://www.yellowfinbi.com/blog/key-dashboard-design-principles-analytics-best-practice)

[image1]: <data:image/png;base64,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>