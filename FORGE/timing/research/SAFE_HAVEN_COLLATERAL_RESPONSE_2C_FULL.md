# Treasury safe-haven failures and collateral chain exposure

**Treasuries have failed as safe havens in at least five major episodes since 1994, and the financial system's dependence on Treasury collateral has grown so large — roughly $5–7 trillion pledged in repo alone — that any future breakdown could trigger a self-reinforcing margin spiral.** The March 2020 "dash for cash" remains the canonical case: the 10-year yield spiked 64 basis points in nine days while equities crashed 34%, gold fell 12.5%, and every traditional safe haven except literal USD cash failed simultaneously. The Fed required two emergency interventions and ultimately unlimited QE to restore functioning. This report synthesizes empirical data across five sections covering failure episodes, capital flows, collateral mechanics, margin dynamics, and crisis timelines.

---

## Section 1: When Treasuries stopped being safe

### A) March 9–18, 2020: the dash for cash

The 10-year Treasury yield hit a record low of **0.54%** on March 9, then reversed violently — rising to **1.18%** by March 18, a 64-basis-point spike during the fastest equity selloff in modern history. This simultaneous collapse of stocks and Treasuries was unprecedented in the post-2000 negative-correlation regime.

**Daily 10-year yield path** (FRED DGS10, H.15 release):

| Date | 10Y yield | Δ (bps) | S&P 500 close | Gold ($/oz) | DXY |
|------|-----------|---------|---------------|-------------|-----|
| Mar 9 (Mon) | 0.54% | −20 | 2,746.56 (−7.6%) | ~1,676 | ~95.0 |
| Mar 10 (Tue) | 0.73% | +19 | 2,882.23 (+4.9%) | ~1,663 | ~95.6 |
| Mar 11 (Wed) | 0.87% | +14 | 2,741.38 (−4.9%) | ~1,643 | ~96.1 |
| Mar 12 (Thu) | 0.88% | +1 | 2,480.64 (−9.5%) | ~1,588 | ~97.4 |
| Mar 13 (Fri) | 0.95% | +7 | 2,711.02 (+9.3%) | ~1,517 | ~98.0 |
| Mar 16 (Mon) | 0.73% | −22 | 2,386.13 (−12.0%) | ~1,516 | ~97.4 |
| Mar 17 (Tue) | 1.03% | +30 | 2,529.19 (+6.0%) | ~1,472 | ~98.8 |
| Mar 18 (Wed) | 1.18% | +15 | 2,398.10 (−5.2%) | ~1,478 | ~99.6 |

The S&P 500 fell from its February 19 peak of 3,386 to 2,237 on March 23 — a **33.9% decline in 23 trading days**, the fastest drop of that magnitude in history. Gold fell roughly **$200/oz (~12.5%)** from its March 9 high near $1,680 to a trough of $1,472 on March 17. The DXY surged from ~95 to a peak near **103** by March 19–20, an 8% move reflecting the global dollar shortage.

**Who was selling and why.** Three groups drove the Treasury liquidation, per Vissing-Jorgensen (BIS Working Paper 966, 2021) and the Fed Financial Stability Report (November 2020). Foreign investors sold over **$400 billion** in Treasuries (with net foreign sales of $287 billion in Q1 2020). Mutual funds sold **$266 billion** to meet redemptions. Hedge funds and leveraged traders sold an estimated **$173–200 billion**, primarily unwinding Treasury cash-futures basis trades.

The basis trade — buying cash Treasuries financed in repo at 1% haircuts while shorting Treasury futures — operated at **50–100x leverage**. BIS Bulletin No. 2 (Schrimpf, Shin & Sushko, April 2020) documented the self-reinforcing "margin spiral": volatility surged, futures exchanges raised maintenance margins dramatically, funds couldn't meet margin calls, positions were forcibly liquidated, which widened the basis further, triggering additional margin calls. Hedge fund net repo positions had peaked at **$598 billion** in mid-2019, and between 2017–2019, hedge fund Treasury exposure had increased by almost **$1 trillion** (Fed FEDS Notes, August 2023). Risk-parity funds (~$400 billion AUM), CTAs (~$300 billion), and volatility-control funds (~$300 billion) amplified the selling.

**Liquidity collapse.** On-the-run 10-year bid-ask spreads approximately **doubled** from their normal ~1/32 of a point, peaking around March 13 (Fleming & Ruela, NY Fed Liberty Street Economics, April 2020). The 30-year bond spread surged to over **5/32** during March 11–13 versus just over 1/32 on February 28 — more than 6x the post-crisis average. Off-the-run Treasury spreads rose to **almost 30 times normal levels** (Lorie Logan, NY Fed, October 2020 SIFMA speech). Order book depth for 5- and 10-year notes collapsed to as low as **10% of post-crisis averages**. Price impact peaked at 5–6x normal on March 12–13. Customer transaction volumes spiked from ~$400 billion/day to over **$600 billion/day**.

**Fed intervention timeline and effects:**

| Date | Action | Market response |
|------|--------|----------------|
| Mar 3 | Emergency 50bp rate cut | Limited impact |
| Mar 12 | $500B in 3-month repo + composition changes | Take-up low |
| Mar 15 (Sun 5pm) | Rate cut to 0–0.25%, $500B Treasury + $200B MBS QE | 10Y briefly fell to 0.73% (Mar 16), then spiked to 1.18% (Mar 18) |
| Mar 17 | PDCF + CPFF restart | Insufficient |
| Mar 18 | MMLF announced | Partial relief |
| Mar 19–Apr 1 | Purchases at up to $125B/day | Yields begin declining |
| Mar 23 (8am) | **Unlimited QE** announced | 10Y fell from 1.18% to 0.67% by Mar 27 |
| Apr 1 | SLR exemption for Treasuries | Further relief |

**The March 15 announcement failed** because the $500B/$200B quantum was perceived as finite and insufficient against the scale of forced selling, and because the problem was dealer **balance sheet capacity**, not just funding — repo take-up was low because dealers couldn't warehouse more Treasuries. Only the March 23 "unlimited" language shifted the equilibrium from a "run" to a "hold" dynamic, per Vissing-Jorgensen's model. The Fed purchased approximately **$670 billion** of Treasuries in ten trading days (March 19–April 1) and its balance sheet surpassed $7 trillion by May 2020. The 30-year bid-ask spread narrowed from >5/32 to ~2/32 by March 31, and Treasury market functioning was "largely normalized" by late April.

### B) October 15, 2014: the 12-minute flash rally

On October 15, 2014, the 10-year yield experienced a **37-basis-point intraday range**, the fourth-largest on record since 1998 — and the three larger moves were all driven by major policy announcements, while this one had no comparable catalyst. The yield dropped from approximately **2.23% to 1.86%** intraday before snapping back, closing just 6 basis points below its opening level.

The extreme move was concentrated in a **12-minute window** from 9:33 to 9:45 AM ET. Weaker-than-expected retail sales data at 8:30 AM triggered an initial yield decline, but the reaction far exceeded what the modest data surprise warranted. The Joint Staff Report (Treasury/Fed/SEC/CFTC/FINRA, July 13, 2015) found **no single cause** but identified several contributing factors: principal trading firms (PTFs) accounted for over half of interdealer trading volume; order book depth collapsed in the hour before the event window; and bank-dealers temporarily provided **no or very few offers** in the cash Treasury order book. Self-trading incidence increased during the event window, and exchange processing latency rose from elevated message traffic. The market self-corrected within minutes; **no official intervention was needed**.

### C) September 2019 repo crisis

On Monday, September 16, 2019, two transitory shocks collided: **quarterly corporate tax payments and settlement of ~$54 billion in new Treasury coupon securities**, draining $65 billion in reserves to their lowest level since 2011 (below $1.4 trillion). SOFR printed at **2.43%**, up 13 basis points. The effective fed funds rate (EFFR) hit 2.25%, the top of the FOMC target range. Stress first appeared in the afternoon in the interdealer (DVP-brokered) segment.

On Tuesday, September 17, SOFR spiked to **5.25%** (volume-weighted median) — a **282-basis-point increase**. The SOFR 99th percentile reached **9%**, and some intraday bilateral repo transactions traded as high as **10%**. The NY Fed announced its first overnight repo operation around 9:00 AM — roughly **18–20 hours** after the first signs of elevated rates on September 16 afternoon — but execution was delayed by technical difficulties until 9:55 AM. Only $53 billion of the $75 billion offered was taken up, because most of the day's elevated trades had already been negotiated.

By September 19, SOFR and EFFR had moved **back within the FOMC target range**. However, the Fed continued daily repo operations for months and began **$60 billion/month in T-bill purchases** on October 15, 2019. The repo operations were not fully discontinued until **January 2021** — 16 months after the initial event.

### D) 1994 bond market massacre

The Fed surprised markets with a 25-basis-point rate hike on **February 4, 1994**, the first increase after a prolonged easing cycle. The 10-year yield had bottomed at approximately **5.17–5.24%** in mid-October 1993. By November 1994, it peaked near **8.0%** — a total move of roughly **270–280 basis points** over 13 months. The 20-year-plus maturity Treasury segment fell approximately **20.5%** in price, with global bond market losses estimated at **$1.5 trillion**.

The S&P 500 total return for 1994 was **+1.33%**, essentially flat, meaning the bond massacre was largely isolated to fixed income — though equities experienced temporary weakness (a ~6% decline from February to mid-May) before recovering. The stock-bond correlation was **weakly positive** during the episode, consistent with the broader positive-correlation regime that persisted from 1974 to 2000. The Fed hiked six more times through November 1994 (to 5.50%, effectively doubling the funds rate), with the final 75-basis-point move signaling the cycle's peak. Core CPI decelerated to 2.4% by year-end, vindicating the preemptive tightening. The 10-year total return in 1995 was **+23.48%**, a sharp reversal. Orange County declared bankruptcy on December 6, 1994, with $1.7 billion in losses from leveraged inverse-floater bets.

### E) The positive correlation regime

The simultaneous selloff of stocks and bonds is not anomalous in historical context — Morgan Stanley's analysis of two centuries of data finds positive stock-bond correlation in **78% of years since 1870**. The negative-correlation era (2000–2021) was the exception.

**2022** was the most severe modern episode. The S&P 500 returned **−18.04%** while the 10-year Treasury returned **−17.83%** (Damodaran, NYU). The Bloomberg US Aggregate Bond Index returned **−13.01%**, its worst year in roughly five decades. A standard 60/40 portfolio lost approximately **15–17%**. The rolling one-year stock-bond correlation turned persistently positive for the first time since 2000, averaging **0.41** from 2022–2024 versus −0.37 in the prior decade (State Street). Ten-year yields moved from 1.51% to a peak of 4.24% in October, driven by 450 basis points of Fed rate hikes.

**The late 1970s/early 1980s** saw persistently positive stock-bond correlation throughout the 1974–2000 period (Morningstar, 2025). While nominal bond returns were sometimes slightly positive (due to high starting coupon rates), real returns were deeply negative — both stocks and bonds lost purchasing power during the stagflation era.

**April 2025** produced a dramatic "Sell America" episode. After the April 2 "Liberation Day" tariff announcement, Treasuries initially rallied (10-year yield fell from 4.17% to 3.96% by April 4). Then the safe-haven dynamic reversed: yields spiked from below 4.00% to **4.50%** by April 8–9, the 30-year topped **5%**, the S&P fell roughly **20% from recent highs**, and the dollar weakened ~6%. Stocks, bonds, and the dollar all fell simultaneously. Treasury Secretary Bessent reportedly raised bond market concerns directly with Trump, who announced a 90-day tariff pause on April 9. Moody's subsequently downgraded the U.S. credit rating in May 2025.

**Academic consensus on what flips the correlation positive** centers on three conditions identified by Campbell, Sunderam, and Viceira (Critical Finance Review, 2017) and Pflueger (Journal of Financial Economics, 2025): supply-driven "bad" inflation (countercyclical), high inflation uncertainty relative to growth uncertainty, and hawkish monetary policy. AQR's model shows the growth-volatility-to-inflation-volatility ratio explains ~70% of long-term correlation variation. The threshold appears to be around **CPI above 2.4%** for positive correlation to emerge (Morgan Stanley, 150 years of data).

---

## Section 2: Where capital actually flowed in March 2020

During the March 9–18 acute phase, traditional safe-haven assets failed almost universally. Gold fell ~12.5% from $1,680 to its 2020 low of **$1,472** on March 17. All major currencies weakened against the dollar, including the Japanese yen (which initially strengthened to 101–102 on March 9 before reversing above 110) and the Swiss franc. The euro fell from ~1.14–1.15 to ~1.06–1.07 against the dollar. The DXY peaked at **103.96** intraday during the week of March 16 — its highest since 2002. The VIX reached **82.69** on March 16, its highest since the 2008 crisis.

The **only assets that held up** during March 9–18 were: USD cash/bank deposits, very short-duration Treasuries (T-bills, which saw "little net selling by foreigners" per He, Nagel & Song, NBER 2022), government money market funds, and long-volatility instruments (VIX products, put options). One-year T-bill yields "remained largely flat" through the crisis, insulated by their near-term government repayment promise.

**Money market fund flows** tell the story of the flight destination. Government MMFs received **$834 billion** in inflows during March 2020 (ICI/SEC data), increasing pre-stress AUM by almost one-third. Institutional prime MMFs lost **$91 billion**, with the worst single week seeing 20% asset outflows ($66 billion) — exceeding even the 2008 crisis as a percentage of assets. Over March 11–24, net redemptions from institutional prime funds totaled **30% of assets (~$100 billion)** (President's Working Group report). Even accounting for all prime-to-government MMF rotation, approximately **$695 billion** of the government MMF inflows represented new money seeking safety.

Bank deposits surged roughly **$1 trillion** in Q1 2020 alone (Fed FEDS Notes, June 2022), split approximately equally between reserves growth from QE and loan drawdowns on corporate credit lines. The FDIC reported **21.7% year-over-year deposit growth** from June 2019 to June 2020 — among the highest since World War II. Over the full pandemic period through Q4 2021, cumulative deposit growth reached approximately $5.25 trillion.

**Treasury market stabilization** was gradual, not instantaneous. The March 15 announcement produced one day of improvement (10-year yield fell to 0.73% on March 16) before dysfunction returned worse than before (1.03% on March 17, 1.18% on March 18). Only after March 23's unlimited QE did spreads narrow sharply. The 30-year bid-ask spread fell from >5/32 to ~2/32 by March 31. Market depth recovered roughly **half its decline** by end of April. Full normalization took approximately **six weeks** from the March 23 intervention. The MBS-Treasury spread, which had widened from ~90bps to ~180bps, completely reverted to its pre-crisis level within one week of the March 23 announcement (Richmond Fed).

---

## Section 3: The Treasury collateral edifice

### CCP initial margin exposure

Total initial margin across major CCP categories reached approximately **$975+ billion** as of Q4 2024 (CPMI-IOSCO quantitative disclosures, ClarusFT analysis): IRS CCPs held $327 billion (LCH SwapClear alone at $240 billion), CDS CCPs held $61 billion, ETD CCPs reached a record **$522 billion** (CME Base at $220 billion, OCC at $124 billion), and FICC GSD held **$65.5 billion** (up 36% year-over-year, reflecting progress toward the SEC Treasury clearing mandate).

Treasury securities represent the **largest non-cash collateral category** at U.S. CCPs. CME Base reported **$29.4 billion pre-haircut** in domestic sovereign government bonds posted as house IM in Q3 2024 — a new record, up 33% quarter-over-quarter, reflecting a notable collateral-type shift toward Treasuries. At FICC, Treasuries and agency securities are the dominant non-cash collateral given that GSD exclusively clears Treasury transactions. No single aggregate figure exists for total Treasuries posted as IM, but the non-cash Treasury component across all major U.S. CCPs is estimated at **$100–200+ billion**.

### Bank HQLA composition

Under Basel III LCR rules, Level 1 HQLA — which receives a **0% haircut** — includes excess reserves at the Fed, U.S. Treasury securities, and full-faith-and-credit government debt. Treasuries' share of the largest banks' total assets expanded from **3% in 2013 to 11% in 2024** (BPI analysis of FR Y-9C data, February 2025). Approximate HQLA composition for large U.S. banks currently runs: reserves at Fed **~30–40%**, Treasuries **~30–40%**, and agency MBS/GSE securities (Level 2A, carrying a 15% haircut) **~15–25%**. Critically, as of Q3 2024, three of the six largest U.S. GSIBs were bound by the enhanced Supplementary Leverage Ratio, meaning **zero remaining balance sheet capacity** for additional Treasury holdings without raising capital.

### Collateral velocity: stuck at ~2.2–2.5x

Manmohan Singh's series of IMF Working Papers provides the definitive estimates. Pre-crisis collateral velocity was approximately **3.0x** (IMF WP 11/256). It fell to ~2.4x by end-2010 (WP 12/179), ~2.15x by end-2012 (WP 13/186), and has since recovered modestly. By end-2020, the world's 18 largest dealer-banks held **$9.4 trillion** in pledged collateral — up more than 50% from pre-crisis levels (Risk.net, June 2021). However, Singh stated in 2022–2023 that velocity "has stuck roughly there in the last two, three years" at approximately **2.2–2.5x**, constrained by Basel III balance sheet limits. The reduced velocity compared to pre-crisis levels represents roughly **$4–5 trillion** in lost effective collateral.

### The $12 trillion repo market

The U.S. repo market has reached **$11.9 trillion** gross (Fed FEDS Note, July 2025), having grown almost 70% since 2014. Approximately 38% ($4.6 trillion) operates in the less-transparent non-centrally-cleared bilateral segment. SOFR daily volume — covering tri-party, FICC GCF, and bilateral Treasury repo cleared through FICC — regularly exceeds **$2 trillion**. Treasury securities are the dominant collateral type, likely representing 60–70%+ of all repo collateral. Estimated total Treasuries pledged in repo: **$5–7+ trillion**. An OFR pilot study found **74% of non-centrally cleared bilateral Treasury repos carried zero haircuts**, a concentration of risk that amplifies vulnerability during stress.

### Foreign holdings: China declining, total growing

Total foreign holdings of U.S. Treasuries stood at **$8.5 trillion** as of December 2024 (TIC data, CRS Report RS22331, May 2025), representing 30% of the $28.1 trillion in publicly held Treasury debt. Official (central bank) holders accounted for **$3.8 trillion** (44%), while private foreign investors held $4.8 trillion (56%). The top five holders as of December 2025 TIC data: **Japan ($1,185.5 billion), United Kingdom ($866.0 billion), China ($683.5 billion), Belgium ($477.3 billion), and Canada ($468.2 billion)**. China's holdings have declined from a peak of ~$1.3 trillion in 2013 to under $700 billion, while the UK has overtaken China as the second-largest holder during 2025. Total foreign holdings have grown in nominal terms but declined as a share of outstanding debt (from ~33% to 30%), as issuance has outpaced foreign buying.

---

## Section 4: How haircuts and margins amplify stress

### March 2020 margin procyclicality

CCP margin requirements surged across the board during March 2020. CME initial margin on **10-year Treasury futures** rose from $1,150/contract on February 28 to $1,850/contract by March 31 — a **61% increase** across five separate increases (Chicago Fed Letter No. 467). Ultra Bond futures margins jumped from $4,500 to **$14,000/contract — a 211% increase**. Peak daily variation margin calls across all CCPs hit **$140 billion on March 9** (versus a ~$25 billion/day average in January–February), and total IM requirements rose by roughly **$300 billion** during the month (BCBS-CPMI-IOSCO, September 2022).

FICC GSD's current haircut schedule (April 2025) runs: **2%** for maturities under 2 years, **3%** for 2–5 years, **4%** for 5–10 years, **6%** for 10–15 years, and **9%** for 15+ years. TIPS carry higher haircuts (up to 10% for 15+ years) and zero-coupon bonds up to 12% for maturities exceeding 5 years.

### When do Treasuries face LCR haircuts?

Under the U.S. LCR final rule (Fed/OCC/FDIC, September 2014), Level 1 HQLA — which includes Treasuries — carry a **permanent 0% haircut** with no cap on their share of HQLA. There is no market-price threshold at which Treasuries receive a haircut in LCR calculations. The key constraint is encumbrance: Treasuries pledged as collateral elsewhere (repo, discount window) cannot count as HQLA. This creates a structural tension — using Treasuries to meet margin calls during stress simultaneously reduces banks' LCR buffers. The Fed's Standing Repo Facility partially addresses this by allowing Treasuries to be converted to reserves on demand.

### Estimating aggregate margin calls from a 5% Treasury price drop

No single public source provides a comprehensive estimate, but the March 2020 experience offers calibration. During that episode (which involved roughly 3–5% moves in long-duration Treasuries over 2–3 weeks), total IM across centrally cleared markets rose ~$300 billion and peak single-day VM calls hit $140 billion. The hedge fund basis trade — estimated at **$800+ billion** in gross notional by 2025 (OFR data) — at ~6x leverage would face margin calls potentially in the **$40–80 billion range** from a 5% cash-leg price decline, depending on netting. CME Treasury futures open interest of ~$4–5 trillion notional implies enormous aggregate VM exposure. A sudden 5% move (roughly 75–100bps on medium-duration) could plausibly generate **$50–100+ billion** in aggregate margin calls across FICC and CME alone. OFR Working Paper 21-01 (Barth & Kahn) estimated that during March 2020, hedge funds reduced short futures by $105 billion and sold $91–105 billion in cash Treasuries.

### The MOVE index as a stress signal

The ICE BofA MOVE Index — Treasury implied volatility — has reached crisis-level readings at: **264.6** on October 10, 2008 (all-time high), **~198.7** in March 2023 (SVB crisis), **~163.7** in March 2020, and elevated readings after the April 2025 tariff shock. The all-time low was **36.62** in September 2020. Market convention treats readings above 120 as elevated and above 150 as crisis conditions. No formal published study directly maps MOVE levels to specific CCP haircut triggers, but the relationship is implicit: CCP margin models use realized and implied volatility as key inputs, so higher MOVE mechanically produces higher IM via model recalibration. BIS Bulletin No. 13 noted that some CCP margin models "underestimated market volatility" during March 2020, meaning model responses lagged the MOVE spike — haircuts catch up rather than lead.

---

## Section 5: How fast crises actually move

### March 2020: nine days from stress to unlimited QE

Treasury bid-ask spreads first widened noticeably on **Friday, March 6 and Monday, March 9** (Fleming & Ruela, NY Fed). Spreads peaked on March 13 (10-year, 30-year) — approximately **7 days** from the initial widening. The Fed's March 15 emergency announcement came roughly **6–9 days** after the first liquidity deterioration, but it failed to stabilize the market. The 10-year yield spiked 30 basis points on March 17 alone (0.73% to 1.03%). The March 23 unlimited QE announcement — **14 days after the initial stress signal** — was the actual turning point. From March 23 to meaningful bid-ask normalization took roughly **one week**; full market depth recovery took approximately **six weeks**.

The earliest indicators were: (1) bid-ask spread widening on BrokerTec on March 6–9, (2) order book depth collapse by March 12–13, (3) the MOVE index spike near 164, (4) Treasury-OIS spread blowout, and (5) yield curve fitting errors reaching unprecedented levels by mid-March (BIS Bulletin No. 2, Graph 2).

### September 2019: 18 hours from spike to intervention

The first signs of repo stress appeared in the **afternoon of September 16** in the DVP-brokered interdealer market, where domestic bank-affiliated dealers ceased lending despite rising rates. The NY Fed announced its first repo operation around **9:00 AM on September 17** — approximately **18–20 hours** after the initial stress signal. Execution was delayed until 9:55 AM by technical difficulties. By September 19 (two days after the acute spike), SOFR and EFFR had returned **within the FOMC target range**. Operational normalization — the full wind-down of emergency repo facilities — took **16 months** (through January 2021).

### Lehman September 2008: the 18-day sprint to TARP

The sequence ran with terrifying speed. Lehman filed for bankruptcy **early morning September 15**. The Reserve Primary Fund broke the buck roughly **24 hours later** (NAV fell to $0.9944 by 11:00 AM on September 16; SEC later determined it dropped to $0.97). By September 17, **$144 billion** had been withdrawn from U.S. money market funds. Treasury's money market guarantee came on **September 19** (four days after Lehman). The TARP proposal was formally submitted on **September 20** (five days). TARP was signed into law **October 3** (18 days), after an initial House rejection on September 29 that sent the DJIA down 6.98%.

**The single earliest sustained systemic stress indicator** was the LIBOR-OIS spread, which jumped from ~10 basis points to **~50 basis points in early August 2007** — more than **13 months** before Lehman's bankruptcy. BNP Paribas suspending three mortgage fund redemptions on August 9, 2007 is widely considered the true starting date of the acute crisis phase. The TED spread similarly widened starting August 2007, reaching 240 basis points on August 20, 2007. Lehman's own CDS spreads, paradoxically, remained relatively stable through summer 2008 — markets assumed a Bear Stearns-style rescue — making CDS a poor early-warning indicator due to moral hazard.

---

## Conclusion: the collateral chain is the transmission mechanism

The empirical record reveals a consistent pattern across every Treasury stress episode. The safe-haven breakdown is not random — it emerges when forced sellers (leveraged funds meeting margin calls, foreign reserve managers raising cash, mutual funds facing redemptions) overwhelm dealer balance sheet capacity simultaneously. The collateral chain transforms what begins as a market liquidity event into a systemic funding crisis: Treasury price declines trigger margin calls, which force Treasury sales, which increase haircuts, which trigger further margin calls. The $5–7 trillion of Treasuries pledged in repo, the $800+ billion basis trade, the 74% of bilateral repos carrying zero haircuts, and the fact that three of six GSIBs have zero remaining SLR capacity for additional Treasury holdings all represent points of vulnerability that have grown since March 2020.

The timeline calibration is stark. From first stress signal to the Fed intervention that actually worked, March 2020 took **14 days**. The September 2019 repo crisis saw the Fed respond in **18 hours** but required 16 months for full operational normalization. The Lehman sequence moved from bankruptcy to money market guarantee in **four days** and to legislative authority in **18 days**. Each crisis has been faster-moving and more interconnected than models predicted. The shift from negative to positive stock-bond correlation — now supported by elevated inflation uncertainty and fiscal sustainability concerns — means the next Treasury stress episode may coincide with equity weakness, removing the natural buyer that typically stabilizes the market. The collateral velocity stuck at 2.2–2.5x, constrained by Basel III, means the system has less capacity to absorb collateral demand shocks than in the pre-2008 era, even as the total stock of Treasuries outstanding has roughly tripled.