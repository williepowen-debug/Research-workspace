# Will's Prompt Playbook

Prompt formats that actually worked. Reuse on purpose, not by accident.

---

## Prompt Templates

### "Top 5 Questions" — Research Stress Test

**When to use:** After completing a major research piece or before a heavy catalyst window.

**Prompt:**
> What are the top 5 questions or threads you would ask or look into if you were me attempting to understand what's going on through our research? Tell me what those questions would be and then answer them if you can.

**Why it works:** Forces synthesis over summary. The agent has to prioritize (what matters most?) and then deliver new insight, not just restate the research. Best answers surface connections that weren't explicit in the original work (e.g., oil and plumbing as same causal chain).

**Watch out for:** Answers restating context you already know. Push back if it's summarizing instead of synthesizing.

**First used:** Mar 14, 2026 — Fed plumbing research. Produced genuine insight on portfolio concentration risk and sequence vs. thesis distinction.

---

## Active Research Queue (Generated Mar 14)

*Priority order. Run through multiple LLMs (ChatGPT, Gemini, Perplexity, Kimi) and cross-verify. Route findings to listed agents.*

### 🔴 P1: Japan FY-End Repatriation Mechanics — How the Money Actually Moves
**Why now:** We hold TLT puts and think Japanese institutions will sell US Treasuries around fiscal year-end (March 31). Need to understand the actual plumbing.
**Route to:** SAM, HENRY, LIQUID

**Prompt:**
> Japan's fiscal year ends March 31. Japanese institutions — life insurers, pension funds, banks, and corporates — are widely expected to repatriate capital around this date, which could mean selling US Treasury bonds. I need to understand the actual mechanics, not the headline narrative.
>
> (1) Who sells and in what order? Break down the specific institutional types — life insurers (Nippon Life, Dai-ichi, etc.), GPIF, megabanks (MUFG, SMFG, Mizuho), corporates. Do they all move at the same time, or is there a sequence?
> (2) How do they sell — do Japanese institutions sell USTs outright on the secondary market, or do they primarily hedge via FX forwards/cross-currency swaps? What's the difference in impact on UST yields between these two approaches?
> (3) What's the timing pattern? Is the selling front-loaded in early March, concentrated in the final week, or does it actually happen in early April after books close? Pull historical daily or weekly data from prior fiscal year-ends (2023, 2024, 2025) if available.
> (4) US Treasury TIC data shows foreign holdings with a lag. If Japan sold $15B in Treasuries in January 2026, when would that show up in TIC data? What's the typical reporting delay?
> (5) The BOJ is simultaneously tapering its bond purchases (QT). How does BOJ QT interact with life insurer selling of JGBs? Is there a circular flow where BOJ absorbs domestic selling while institutions sell foreign bonds?
> (6) What makes a "stressed" fiscal year-end different from a normal one? Current conditions: yen at ~159 (weakest in decades), oil import costs surging (Brent $100+), and the BOJ just dumped ¥399.8B in foreign bonds in a single day (March 12). How do these conditions change the repatriation calculus vs. a normal year?

### 🔴 P2: CRE Bondholder Revolt — Historical Precedents and Cascade Risk
**Why now:** A major CRE operator (Kennedy-Wilson) just had bondholders organize to refuse a $1.8B debt exchange. Need to know if this is isolated or a template.
**Route to:** REGINALD, BROCK, HENRY

**Prompt:**
> Kennedy-Wilson Holdings (KW), a US commercial real estate operator, launched a $1.8 billion debt exchange offer in early March 2026, seeking to swap three tranches of notes (due 2029/2030/2031) into new longer-dated 2032/2034 notes. The exchange is tied to a go-private merger with Fairfax Financial at $10.90/share. Bloomberg reported (March 6) that a majority bondholder bloc organized to REFUSE the exchange and demand cash repayment instead.
>
> (1) What happened in 2008-2009 when CRE bondholders began refusing debt exchange and roll offers? Walk me through the cascade sequence with specific company examples — General Growth Properties, Extended Stay, Stuyvesant Town, Centro, etc. How did refusals at one issuer spread to others?
> (2) What are the mechanics of a failed exchange offer? Does it trigger cross-default provisions in other debt? Can it force involuntary bankruptcy or liquidation, or just deadlock?
> (3) How does a bondholder revolt at a company in the middle of a go-private merger differ from a public company situation? If bondholders block the exchange, does the Fairfax merger fall apart?
> (4) Build me a watchlist: which other US CRE operators and REITs have significant unsecured bond maturities coming due in 2026-2031 that might need similar exchange offers? Focus on companies with high leverage (>60% LTV) and office/multifamily exposure.
> (5) Walker & Dunlop, a major CRE lender, stated in their 2025 10-K filing that CRE origination fraud is "systemic, no longer anecdotal" and disclosed $221.6 million in repurchase/indemnification obligations from inflated NOI at origination. How does widespread origination fraud (meaning actual property values and LTV ratios are worse than reported across the industry) affect bondholder willingness to extend or roll CRE debt?
> (6) What's the read-through for CMBS spreads and regional bank CRE portfolios if bondholder revolts become a pattern in Q2 2026? Regional banks like OZK and Western Alliance have large CRE books — how exposed are they to a repricing cascade?

### 🔴 P3: FOMC Hawkish Hold Into Deteriorating Growth — Historical Transmission
**Why now:** FOMC is March 17-18. GDP just revised to 0.7%, Core PCE reaccelerating at 3.1%, live oil shock ongoing. The Bank of Japan meets the very next day. Need to understand the mechanical market response.
**Route to:** HENRY, LIQUID, SAM

**Prompt:**
> The Federal Reserve is expected to hold rates at the March 17-18 FOMC meeting and likely project zero rate cuts for 2026 in the dot plot. This comes as Q4 2025 GDP was just revised down to 0.7%, Core PCE is reaccelerating at 3.1% YoY, the February jobs report showed -92,000 payrolls, and there is a live oil shock with Brent crude at $100+ due to the Hormuz Strait closure.
>
> (1) Historical precedent: when has the Fed held rates with hawkish forward guidance (dot plot showing no cuts) while GDP was clearly deteriorating and inflation was reaccelerating? The closest analogs might be late 1973 (oil embargo + stagflation), mid-2008 (pre-Lehman, inflation concerns delaying cuts), or late 2022 (aggressive tightening into slowing growth). What happened to high-yield credit spreads (HY OAS), regional bank stocks (KRE ETF equivalent), long-term Treasury yields (TLT), and the VIX in the 1-4 weeks following each of these episodes?
> (2) Does a hawkish FOMC hold in this context typically produce a sharp gap repricing (within 24-48 hours) or a slow grinding move over days/weeks? Which asset classes react fastest — rates, credit, or equities?
> (3) The Summary of Economic Projections (SEP) will be released alongside the decision. If the Fed revises GDP projections down significantly but KEEPS the same dot plot (no cuts), is that net hawkish or does the GDP revision dominate? How has the market historically weighed SEP GDP revisions vs. dot changes?
> (4) The Bank of Japan meets March 18-19 — literally the next day after the Fed decision. Governor Ueda's press conference is March 19. Has there ever been a Fed + BOJ meeting within 24 hours of each other during a period of macro stress? How did USD/JPY and carry trades respond to the sequential announcements? Current context: USD/JPY is at ~159, just 100 pips from the 160 level that both the US Treasury Secretary and Japan's Ministry of Finance have reportedly coordinated on as an intervention threshold.
> (5) Implied volatility dynamics: if I currently hold June 2026 put options on various assets and want to roll them to December 2026, is the post-FOMC volatility spike a good window to execute that roll? Specifically: does a hawkish FOMC surprise inflate near-term IV (June) more than far-term IV (December), making it advantageous to sell expensive June and buy relatively cheaper December? Or does IV crush hit uniformly across the curve?

### 🟠 P4: Insider Selling as a Bank Stress Predictor — Historical Validation
**Why now:** We found unanimous C-suite selling at two regional banks we're short. Need to validate whether this pattern has historically predicted bank stress.
**Route to:** REGINALD

**Prompt:**
> I'm researching whether insider selling patterns at US banks can predict future credit deterioration or stock declines. I've identified two cases that seem significant:
>
> **Bank A (OZK, $27B assets):** The CEO, CFO, former CFO, Chief Risk Officer, and a board director ALL sold shares in recent months. Total insider sales ~$2.4 million vs. only $37,000 in purchases. Notably, the CRO's sales were discretionary (not under a pre-arranged 10b5-1 plan). This bank has an unusually high ratio of commercial real estate loans that have been reclassified into the "commercial & industrial" category on regulatory filings.
>
> **Bank B (Western Alliance / WAL, $80B assets):** The company replaced its 22-year veteran CFO with a new CFO hired from JPMorgan's Financial Institutions Group (the division that advises distressed banks). The outgoing Chief Accounting Officer retired and sold shares. Two new directors with risk management backgrounds were added to the board in December 2025. Executive compensation shifted from stock to cash-settled RSUs.
>
> Research questions:
> (1) Historical hit rate: when 3 or more bank C-suite executives are selling simultaneously with zero insider buying, how often has material credit deterioration, a stock decline of >30%, or regulatory action followed within 6-12 months? Examine specific cases: Silicon Valley Bank (2022-23), Signature Bank (2022-23), First Republic (2022-23), Washington Mutual (2007-08), Countrywide (2006-07), IndyMac (2007-08), Colonial BancGroup (2008-09).
> (2) What's the typical lead time between an insider selling cluster and public recognition of the problem? In the cases above, how many months elapsed between peak insider selling and the stock's major decline or failure?
> (3) Is there a measurable difference in predictive value between sales made under pre-arranged 10b5-1 plans vs. discretionary sales? Academic research or empirical data preferred.
> (4) The CFO replacement pattern at Bank B is striking. Has the specific pattern of replacing a long-tenured CFO with a crisis/restructuring specialist from a major bank's FIG practice preceded stress events at other banks? Name every case you can find.
> (5) Practical screen: what tools and data sources can I use to monitor insider transactions at US banks in real-time? Form 4 filings on SEC EDGAR, OpenInsider, Finviz, etc. Could I build a monthly automated scan for "3+ insiders selling, zero buying" at banks above $10B in assets?

### 🟠 P5: US Munitions Depletion and War Duration — What Happens When You Run Low
**Why now:** FT reported the US has burned through "years" of munitions in two weeks of operations against Iran around the Strait of Hormuz. Duration of the conflict directly determines the magnitude of oil price impact and economic damage.
**Route to:** HAWK, HENRY, LIQUID

**Prompt:**
> The Financial Times reported in mid-March 2026 that the United States has consumed "years" worth of certain munitions in approximately two weeks of military operations related to the Iran-Hormuz crisis. The US is conducting strikes on Iranian military targets, attempting mine clearance in the Strait of Hormuz, and defending against Iranian missile and drone attacks.
>
> (1) What specific munitions categories are being consumed at the highest rate? Break this down by type: Tomahawk cruise missiles (TLAM), Joint Direct Attack Munitions (JDAM), SM-6 interceptors (for ballistic missile defense), mine countermeasure equipment, and precision-guided munitions. What are publicly known US stockpile levels for each, and what are annual production rates? At current consumption, how many weeks/months of supply remain for each category?
> (2) Historical analogs: has the United States ever had to de-escalate, change strategy, or negotiate due to munitions constraints? Examine: Kosovo 1999 (NATO ran low on precision munitions after 78 days), Libya 2011 (European allies exhausted stocks, US had to backfill), the 2022-25 Ukraine support (depleted Stinger, Javelin, and 155mm stocks significantly). What were the strategic consequences in each case?
> (3) The mine problem specifically: Iran has been mining the Strait of Hormuz. How many mine countermeasure vessels (MCM) does the US currently have deployed or available? What is the realistic daily mine clearance rate for a modern MCM vessel? Reports suggest Iran can deploy sea mines faster than they can be cleared — is this assessment supported by the technical capabilities of both sides?
> (4) If the US cannot sustain current operational tempo due to munitions constraints, what are the realistic strategic options? (a) Negotiate/accept ceasefire; (b) Escalate to a different type of campaign requiring different munitions (e.g., air campaign vs. ground targets); (c) Impose a counter-blockade on Iran; (d) Accept a prolonged Hormuz closure and shift to economic containment. Which is most likely given current political dynamics?
> (5) Fiscal impact: what does emergency wartime spending typically look like in terms of supplemental appropriations? Would emergency munitions procurement and operational costs require additional Treasury issuance? How large — rough order of magnitude — based on the Iraq/Afghanistan supplementals as templates?
> (6) Duration scenarios: if munitions constraints prevent the US from forcing Hormuz open militarily, does this make the Strait closure LONGER (can't clear it by force, Iran has no incentive to stop) or SHORTER (political pressure to negotiate rather than spend into a depleted stockpile)? Walk through the logic for each direction.
