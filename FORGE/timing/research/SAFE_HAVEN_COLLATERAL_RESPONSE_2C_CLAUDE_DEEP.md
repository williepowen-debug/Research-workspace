# Treasury market stress thresholds and Fed response tools: an empirical reference

**The Treasury basis trade — estimated at $600 billion to $1 trillion in gross notional — operates on leverage ratios of 20:1 to 175:1, making it acutely sensitive to margin spirals, yet the binding constraint in past crises has been internal VaR limits, not external margin calls.** The Fed possesses at least eight distinct intervention tools with deployment speeds ranging from same-day (SRF, emergency rate cuts) to weeks (outright purchases at scale, SLR exemption), but each tool carries measurable tradeoffs against inflation-fighting credibility. This report compiles the empirical record — specific dollar amounts, thresholds, and precedents — drawn from BIS working papers, CFTC data, OFR reports, Fed working papers, FRBNY operational data, ICI statistics, and academic literature.

---

## Section 1: Basis trade margin mechanics reveal extreme but heterogeneous leverage

### 1a. Aggregate margin call sensitivity

No published study provides a clean estimate of aggregate dollar margin calls on the basis trade per 10, 25, or 50 bps move in Treasury yields. This is a notable gap in the literature. The closest empirical data:

Kashyap, Stein, Wallen & Younger (Brookings, March 2025) document that across **all central counterparties and all asset classes**, initial margin increases totaled approximately **$300 billion in March 2020**, with variation margin flows peaking at **$140 billion** during mid-March stress. CME customer funds in futures accounts rose from **$214 billion (end-February) to $318 billion (end-March)** — a $104 billion increase in one month. These figures encompass all asset classes, not Treasury futures alone.

The Dallas Fed (Ramaswamy et al., July 2025) offers the most direct sensitivity estimate: **a 40–50 bps increase in repo rates would induce roughly a 3-tick move in the basis** (≈10 bps of notional), characterized as "likely at the lower end of the range of moves that could trigger some de-risking." Their critical finding: **stability of the trade is considerably more sensitive to declines in intermediation capacity than to funding rate increases.**

The **size of the basis trade** itself is contested. NY Fed Manager Roberto Perli (May 9, 2025) stated CFTC leveraged fund net short positions in Treasury futures were **over $1 trillion in March 2025** and **$660 billion in February 2020**, but noted estimates "tend to range from $600 billion to $1 trillion." The FEDS Notes (Glicoes et al., March 2024) measured basis trade volumes using matched TRACE data at only **$260–$574 billion** as of September 2023 — roughly half the CFTC-derived upper bound. Barth & Kahn (JME 2025) report basis traders account for **more than 60% of all hedge fund Treasury positions** and **70% of all hedge fund repo**.

### 1b. CME margin increases across three stress episodes

| Metric | March 2020 | October 2023 | April 2025 |
|---|---|---|---|
| **10Y futures IM ($/contract)** | $1,150 → $1,850 (**+61%**) | Not publicly available; margin leverage ~50× implies ~$2,000 range | Proactively raised; amounts not public |
| **Ultra Bond futures IM ($/contract)** | $4,500 → $14,000 (**+211%**) | Not available | Proactively raised |
| **Margin leverage (5Y / 10Y)** | ~175× / 120× pre-crisis → sharply reduced | ~70× / 50× (BIS, Sept 2023) | Not available |
| **Single-day max IM increase (10Y)** | 16.4% | Not available | Not available |
| **30-day cumulative IM increase (10Y)** | 60.9% | Not available | Not available |
| **Record single-day margin movement** | Not separately reported | — | **$32 billion** (April 9, 2025; prior record $22B) |

The March 2020 data comes from Chicago Fed Letter No. 467 (Patel & Spence, June 2022) using CME Group and Bloomberg data. CME's filtered historic simulation VaR model would have warranted increases of ~120% (10Y) and ~210% (Ultra Bond), but CME applied anti-procyclicality buffers that dampened actual increases to 61% and 211% respectively. All margin increases were issued with at least **24 hours advance notice**. October 2023 and April 2025 per-contract figures are not available in public sources, as CME does not archive historical margin snapshots.

### 1c. Repo haircut changes show bifurcated dynamics

The most granular empirical data comes from Bejarano, Lu & Wallen (HBS Working Paper 26-034, December 2025, "Negative Treasury Haircuts"), using confidential Fed supervisory data on the five largest U.S. bank-affiliated dealers.

| Repo Segment | Normal (pre-stress) | March 2020 Peak Stress | October 2023 | April 2025 |
|---|---|---|---|---|
| **Bilateral (NCCBR) to hedge funds** | **−50 bps** (negative — cash lent exceeds collateral) | **+150 bps** positive (~200 bps swing) | No granular data; 70%+ at zero haircut (OFR 2022 pilot) | **Stable**: 56% zero, 34% positive, 10% negative (OFR permanent collection) |
| **Tri-party** | **2%** | **2%** (unchanged) | **2%** (unchanged) | **2%** (unchanged) |

In normal times, **73.8% of qualifying hedge fund repo borrowing** (~$815 billion) transacted at **zero or negative haircuts** (FEDS Notes, September 2023). During March 2020, bilateral haircuts swung ~200 bps "rapidly over the course of a few weeks." By contrast, tri-party haircuts have been "remarkably stable at 2% for over a decade" (FRBNY statistics). The OFR's permanent NCCBR collection (launched December 2024) confirmed **no fire-sale haircut spikes during April 2025**: the proportion of zero-haircut repo was stable across quarter-ends and during April's market volatility. Among non-affiliate zero-haircut trades, roughly half involved hedge funds, and **65% of hedge fund repo carried zero haircuts**.

### 1d. Deleveraging multiplier and leverage ratios

**No formal "forced Treasury selling per $1 of margin call" multiplier exists in the academic literature.** The relationship is more complex than a simple multiplier, with the most important finding from Kruttli, Monin, Petrasek & Watugala (JFE 2025, "LTCM Redux"): **internal VaR-based risk limits, not external margin calls, were the binding constraint** driving March 2020 forced selling. Repo financing remained available.

Leverage ratio estimates vary significantly depending on measurement:

| Measure | Source | Ratio |
|---|---|---|
| Futures margin leverage (5Y / 10Y), pre-pandemic | BIS (Avalos & Sushko, Sept 2023) | **~175× / 120×** |
| Futures margin leverage (5Y / 10Y), post-2021 | BIS (Avalos & Sushko, Sept 2023) | **~70× / 50×** |
| Treasury repo leverage (repo borrowing / capital) | FEDS Notes (Sept 2023) | **56×** |
| Composite leverage (TBAC/CFTC MRAC assumption) | TBAC Q1 2024; CFTC MRAC Dec 2024 | **20×** |
| Top-10 fund average | Cleveland Fed (Hammack, Feb 2025) | **18:1** |
| Multi-strategy fund leverage (incl. synthetic) | BIS QR (Sept 2024) | **14:1** |
| Average qualifying hedge fund balance sheet leverage | Kruttli et al. (JFE 2025) | **2.5:1** |

**Barth & Kahn (JME 2025) vs. BIS**: Barth & Kahn document that hedge funds sold **roughly $100–$200 billion** in cash Treasuries and reduced short futures by **$105 billion** (from $659B to $554B) between February 18 and March 17, 2020. They report total Treasury exposure reduction of **$430 billion**. The BIS (Schrimpf, Shin & Sushko, BIS Bulletin No. 2, April 2020) documented hedge fund Treasury exposure drops of **approximately $670 billion**. The divergence reflects different measurement scopes — the BIS figure includes broader deleveraging beyond the basis trade specifically.

**April 2025 was a key counter-example**: despite yields rising ~30 bps in one week and elevated MOVE readings, the basis trade was **not unwound**. NY Fed's Perli (May 2025): "The basis remained relatively stable. This stands in sharp contrast to March 2020." The **swap spread trade** partially unwound (contracting 11%, from $707B to $631B per BIS QR December 2025), but the basis trade survived because repo markets remained orderly and dealer intermediation held.

---

## Section 2: Dealer withdrawal is driven by VaR limits interacting with balance sheet capacity

### 2a. Bid-ask spreads reached 6× normal before dealers pulled back

Fleming & Ruela (2020, Liberty Street Economics) provide the definitive BrokerTec interdealer data:

| Security | Normal (post-GFC avg) | Peak Stress (March 12–16, 2020) | Multiple |
|---|---|---|---|
| **30-year bond bid-ask** | ~1/32 | **>5/32** (March 11–13) | **>5×** |
| **10-year note bid-ask** | ~1/32 | **~2/32** | **~2×** |
| **5-year note bid-ask** | baseline | ~1.5× baseline | **~1.5×** |
| **Off-the-run 10Y (yield terms)** | ~few bps | **29 bps** (March 11, ICI/Bloomberg) | **>10×** |
| **30Y closing spread (Tradeweb)** | <0.2 bps | **>3 bps** (March 16) | **>15×** |

Order book depth collapsed to levels comparable with the **nadir of the 2007–09 financial crisis**: 5-year and 10-year depth fell to **as low as 10% of post-crisis averages**; 30-year depth fell to **38%**. Price impacts reached **5–6× post-crisis averages** around March 12–13. In April 2025, 10-year BrokerTec depth plunged from a norm of ~$200 million to **$30 million** on April 8 (per Duffie 2025 congressional testimony).

Duffie, Fleming, Keane, Nelson, Shachar & Van Tassel (2023, FRBNY Staff Report No. 1070) provide the key structural finding: on **March 12, 2020**, the first principal component of Treasury illiquidity reached **5.4 standard deviations** above its mean, while dealer balance-sheet utilization reached its **sample record high**. Goldberg (2020) estimated a **~26% shift in net demand for Treasury liquidity** — the largest in the 1990–2020 sample — alongside a **17% reduction in the supply of liquidity by dealers**.

### 2b. MOVE index thresholds are conditional on dealer capacity utilization

| Episode | Peak MOVE | Outcome |
|---|---|---|
| GFC (Oct 10, 2008) | **264.6** (all-time high) | Severe Treasury illiquidity |
| COVID (mid-March 2020) | **~164** | Treasury market dysfunction |
| SVB/banking (March 2023) | **~199** | Highest since 2008; Treasury volatility |
| Treasury selloff (Oct 2023) | **~140–150** | Elevated but no disorderly unwind |
| Tariff shock (April 2025) | Elevated (~99th percentile per CME CVOL) | Market stress but basis trade intact |
| All-time low (Sept 29, 2020) | **36.6** | Post-intervention calm |

**No single MOVE threshold triggers dealer pullback.** The Duffie et al. (2023) framework demonstrates it is the **interaction of volatility with dealer balance-sheet utilization** that determines when liquidity breaks down. Yield volatility alone explains ~70% of variation in Treasury liquidity. But when dealer capacity utilization is simultaneously high, liquidity deteriorates **far worse** than volatility alone would predict. This is consistent with occasionally binding constraints — dealers have headroom until they don't, at which point the relationship becomes sharply nonlinear.

### 2c. Dealer positioning peaked then froze in March 2020

During March 2020, dealers initially absorbed massive selling: foreign investors sold **~$270 billion**, mutual funds **~$240 billion**, and hedge funds **>$30 billion** in Treasuries (He, Nagel & Song 2022, JFE). Dealers expanded reverse repo financing by **~$400 billion** — then hit balance sheet constraints and **ceased expanding**. The Fed offered **$1.5 trillion** in repo on March 12, but take-up was "abysmally low" because dealers would not expand balance sheets further even with cheap funding.

Primary dealers' net Treasury note/bond and agency MBS holdings reached **record highs for the four weeks ending March 18, 2020** (Fleming et al. 2022/2024). Average weekly Treasury position per dealer: **~$34.3 billion** (Bräuning & Stein). Average weekly turnover per dealer: **~$209 billion**. By 2024, dealers' gross Treasury positions were approximately **$800–820 billion**, with daily turnover of **$545–944 billion**. The structural vulnerability: since 2007, Treasury debt held by the public **relative to primary dealer balance sheets** has increased **four-fold** (Duffie 2025 testimony). CBO projects debt rising from ~$29 trillion to ~$52 trillion by 2035.

### 2d. Bräuning & Stein identify VaR and SLR as dual binding constraints

The paper is by Falk Bräuning and **Hillary Stein** (Boston Fed WP 24-7; conditionally accepted at *Review of Financial Studies*), not Jeremy Stein. Using confidential FR VV-1 Volcker rule data on daily VaR limits from 14 bank-affiliated primary dealers (~75% of total turnover):

**VaR limit effects**: A one-standard-deviation tighter risk-limit shock produces a **2.1% fall in net position**, **1.7% fall in turnover** (~$6 billion decline from ~$351B avg), and a **2.4% increase in bid-ask spreads**. In Treasury auctions, the same shock causes a **5% drop in primary dealer bid-to-cover ratio** and a **~1% increase in high yield**. When Treasury demand shifts coincide with tighter constraints, yield effects are amplified by **~26–33%**.

**SLR effects** (April 2020 natural experiment): When a bank's SLR decreased by 1 percentage point relative to peers, its dealer increased gross Treasury positions by **9.1 percentage points** in the first week. More constrained (lower-SLR) dealers increased holdings more. **Shadow cost of constraints**: approximately **26% (SLR) to 33% (VaR) of the intermediation margin**, translating to **~$2.4–$3.0 billion per year**.

A companion paper — Li, Petrasek & Tian (FEDS WP 2025-034) — confirms: **as VaR limit usage doubles, dealers decrease net position changes by ~10%** over the following week. During March 2020, more constrained dealers sold to the Fed more aggressively, bidding **0.8 cents lower in prices**. After selling, dealer buy volume from clients **increased 8.5%** for every 100% increase in SOMA sale volume. There is a contested finding between the Boston Fed (significant SLR effect) and Fed Board staff (Cochran et al. 2023: "no noticeable effect" of SLR exemption on Treasury intermediation).

**Which binds first?** VaR limits bind first in acute stress because VaR mechanically rises with volatility, consuming headroom without position changes. SLR binds in slow-moving conditions. Both can bind simultaneously.

---

## Section 3: MMF redemption triggers operate through institutional fear of fees and gates, not NAV losses

### 3a. The Reserve Primary Fund broke at $0.97, but $40 billion fled before the announcement

The Reserve Primary Fund held **$62.5 billion** and **$785 million in Lehman Brothers paper** (1.2% of portfolio). The critical timeline: on September 15, 2008, redemption requests reached **~$16.5 billion by 1:00 PM**. By 3:45 PM on September 16, requests totaled **$40 billion** (~64% of assets) — **before** the 4:00 PM NAV announcement at **$0.97**. The shadow NAV had actually fallen below $1.00 by **11:00 AM on September 16** (reaching $0.9944) due to an administrative error in the morning calculation.

**Critically, the run preceded the break**: $40 billion in redemptions caused the NAV failure, not the reverse. NY Fed researchers (Cipriani et al., 2013) found **five MMFs** had shadow NAVs below $0.995 *before* Lehman's bankruptcy; **29 MMFs** reported shadow NAVs below $0.995 during September–October 2008, with one fund reporting a shadow NAV as low as **$0.903**. The distinguishing factor for Reserve Primary was the **absence of sponsor support**. Industry-wide: prime MMFs lost **>$300 billion** (~15% of institutional prime assets) in the worst week; **$498 billion** over the crisis month. Government MMFs received **$409 billion** (+44%).

In **March 2020**, institutional prime MMFs had floating NAVs (post-2016 reform). The largest NAV deviation was **24 basis points** (ESMA WP, 2023). The primary run trigger was not NAV concerns but **fear of the 30% WLA fee/gate threshold**: Cipriani & La Spada (NY Fed Staff Report 956) found the relationship between outflows and shadow NAV minimum was statistically insignificant (p = 0.61, R² = 0.01). A **10 percentage point decrease in WLA** at end-2019 increased daily outflows during the run by **1.1 percentage points** for domestic institutional funds. Two fund sponsors purchased securities from three affiliated funds to prevent WLA breaching 30%; one fund's WLA did dip below 30% but recovered to 40.6% by March 20.

### 3b. Peak redemption rates reached 26% of AUM in a single day

| Metric | September 2008 | March 2020 |
|---|---|---|
| **Worst-week outflow (inst. prime)** | **15%** (~$192B, ICI) | **20%** (~$66B) |
| **Two-week cumulative (public inst. prime)** | — | **30%** (~$100B) |
| **Peak single-fund daily outflow** | ~25%+ (Reserve Primary) | **~26%** of AUM |
| **Peak single-fund weekly outflow** | — | **~55%** of AUM |
| **Total prime outflows** | **$386–$498B** | **$139–$143B** |
| **Duration of outflows** | Persisted weeks | Ceased ~2 weeks after shock |

The MMLF (announced March 18, 2020) peaked at **>$50 billion** in early April. **81% of public institutional prime funds** tapped the facility, selling an average 15% of AUM. Total MMLF absorption: **$58 billion** (NY Fed Staff Report 980).

### 3c. The 2023 SEC reforms eliminated old cliff effects but introduced new ones

The SEC's July 12, 2023 final rule (Release No. IC-34959, 88 FR 51404) made four structural changes:

**Swing pricing was dropped entirely.** In its place, the SEC adopted **mandatory liquidity fees** for institutional prime and institutional tax-exempt MMFs. The trigger: **5% of net assets in daily net redemptions**. The fee is based on a good-faith estimate of the cost of liquidating a pro rata vertical slice of the portfolio, including spread costs, transaction costs, and market impact. There is a de minimis exception below **1 basis point**; a **default fee of 1%** applies if costs cannot be reasonably determined; the fee is otherwise **uncapped**. All ties between WLA thresholds and fee/gate imposition were eliminated; gates were removed entirely.

Minimum liquidity requirements were raised sharply: daily liquid assets from **10% to 25%**, weekly liquid assets from **30% to 50%**. The mandatory fee provision took effect **October 2, 2024**.

**New cliff effect risk**: Commissioner Uyeda (dissenting) warned the 5% threshold could create its own preemptive run dynamic. NY Fed researchers (Cipriani, Martin, McCabe & Riordan, August 2023) argue the fee's same-day structure creates a self-dampening incentive (preemptive redemptions increase the probability of triggering the fee), unlike the old multi-day WLA observation window. **Industry impact was dramatic**: prime institutional MMFs fell from **25 to 9 funds**; $309 billion was driven out; sponsors dropped from 16 to 7 (ICI, January 2025).

### 3d. MMFs attract capital during rate hikes; short-end correlations favor inflows

An IMF Working Paper (July 2025) examining nine countries found **MMFs attract capital during rising interest rates, driven primarily by yield-seeking behavior**. During 2022–2023, government MMFs adjusted yields nearly one-to-one with policy rate changes, making them highly competitive versus bank deposits (which adjusted slowly). In 2023, MMFs saw a **$1.2 trillion (22%) net increase** — with **~40% ($480 billion) flowing in during March 2023 alone** after SVB. Government funds attracted **>75%** of net new cash. Total MMF assets as of March 2026: **$7.86 trillion** (ICI), with government MMFs at **~$6.47 trillion**.

### 3e. Government MMFs face stress only in the debt ceiling scenario

Government MMFs received **$834–$840 billion** in inflows during March 2020 (ICI/SEC/PWG — figures differ slightly by source). Only ~$139 billion could be attributed to rotation from prime funds; the remaining **$695+ billion** came from equity/bond fund redemptions ($348B) and direct cash allocations.

The primary historical stress scenario is the **debt ceiling**. In 2011, government MMFs saw **8% of total assets** flow out, with $77 billion from institutional funds in one week. In 2013, Fidelity's money market funds **refused to hold Treasuries maturing near the X-date**. In 2023, 1-year sovereign CDS spreads jumped to **>160 bps** (record high vs. <20 bps normally). No formal government MMF "run" has ever occurred in the traditional sense. Government MMFs are **not subject** to mandatory liquidity fees, gates, or floating NAV requirements.

---

## Section 4: Eight Fed tools with deployment speeds from hours to weeks

### 4a. The Standing Repo Facility operates overnight at $500B+ capacity

Established **July 28, 2021**. Eligible counterparties: all 25 primary dealers plus depository institutions with ≥**$2 billion** in eligible securities or ≥**$10 billion** in total assets. Rate: top of the fed funds target range. Term: overnight only. In **December 2025**, the FOMC removed the $500 billion aggregate daily limit, moving to full allotment. Morning operations were added **June 26, 2025**. Hedge funds and non-bank financial institutions are **not eligible**.

**Usage**: peaked at **$29.4 billion** (October 31, 2025, the largest single-day operation) amid month-end repo rate spikes when bank reserves fell to $2.8 trillion. During **April 2025** stress, the NY Fed added precautionary extra morning operations (March 27–April 2), but repo rates remained "fairly stable" (Perli, May 2025) and no large take-up was reported.

**Comparison to PDCF (March 2020)**: The PDCF accepted far broader collateral (investment-grade debt, CP, municipals, ABS, equities) at the primary credit rate for terms up to **90 days**. Peak weekly average: **>$35 billion**. In 2008, the original PDCF peaked at **>$140 billion** post-Lehman. The SRF's structural limitation is its restriction to high-quality collateral and overnight term — it cannot address the funding stress of levered non-bank entities holding lower-quality or longer-term collateral.

### 4b. The SLR exemption freed ~$1.6 trillion in leverage exposure capacity

**Terms**: Effective **April 1, 2020**, through **March 31, 2021**. Excluded U.S. Treasury securities and Federal Reserve deposits from total leverage exposure (SLR denominator). Covered Category I–III bank holding companies (≥$100B assets). The exemption decreased binding Tier 1 capital requirements by approximately **$17 billion** and increased leverage exposure capacity by approximately **$1.6 trillion** (Fed Board estimate).

**Measured effect — contested**: Bräuning & Stein (Boston Fed WP 24-7) found lower-SLR dealers increased Treasury positions by about **$3.4 billion per 1 percentage point SLR reduction** in the first week. Fed Board staff (Cochran et al. 2023, FEDS Notes) found "no noticeable effect" on dealer Treasury intermediation, noting dealers' Treasury positions were "overwhelmingly encumbered" (matched-book repo) and Treasuries at dealer subsidiaries account for **less than 2%** of total leverage exposure.

**2025 reform**: On June 25, 2025, regulators proposed replacing the flat 2% eSLR buffer with **50% of each GSIB's Method 1 surcharge** (total eSLR: 3.5–4.25% vs. current 5%). This did **not** exempt Treasuries from the denominator. BPI criticized it as having only a "de minimis" effect (0.74% capital reduction for large banks).

### 4c. March 2020 QE deployed $75 billion/day in Treasuries, normalizing markets in ~2 weeks

| Date | Action | Daily Treasury Purchase Volume |
|---|---|---|
| March 13 | First significant purchases | ~$37–40B/day |
| March 15 | Announced $500B Treasury + $200B MBS program; cut to 0–0.25% | — |
| March 16–18 | Purchases continue; 10Y yield spikes 64 bps from March 9 | ~$37–40B/day |
| **March 19** | **Key turning point**: purchases ramped sharply; yields started falling | **~$68–75B/day** |
| March 23 | Unlimited QE announced | $75B/day Treasuries + $50B/day MBS |
| Late March | Peak combined daily purchases | **Up to $125B/day** |
| April 1 | SLR exemption + FIMA facility; purchases begin declining | Declining |
| Late April | — | ~$18B/day combined |
| Late May | — | ~$9.5B/day combined |
| June 2020 | Formalized pace | $80B/month Treasuries + $40B/month MBS |

Total Treasury purchases mid-March through June 2020: **~$1.6 trillion**. Weekly peak: **~$350 billion**. By mid-August 2020, Fed securities holdings were up **$2.36 trillion** since mid-March. The Fed's share of outstanding Treasuries rose from **15% to 22%**.

**Normalization speed**: Treasury yields started falling on **March 19** — the exact day purchase pace ramped from ~$40B to ~$75B/day. Vissing-Jorgensen (2021, BIS/NBER) confirms this was causal: corporate yields actually *increased* on March 19–20, ruling out confounding factors. The March 15 announcement alone was **insufficient** — unlike corporate bond markets where announcements worked, in Treasuries **actual purchases** drove the reversal. Market functioning substantially normalized within **~2 weeks** of peak stress (by early April), at which point the Fed could reduce purchases without yields rebounding.

### 4d. Operation Twist moved $667 billion and reduced long yields by 15–22 bps

**Phase 1** (September 21, 2011): $400 billion. **Phase 2** (June 2012): $267 billion. **Total: ~$667 billion** in maturity swaps — selling ≤3-year Treasuries, buying 6–30-year Treasuries. **Sterilized by definition**: balance sheet size held constant. Duration: September 2011 through December 2012. The Fed's portfolio shifted from ~50% short-term / ~50% long-term to **~22% short-term / ~78% long-term**.

**Yield impact**: Swanson (2011) estimated the original 1961 Operation Twist lowered long-term yields by **~15 bps** (statistically significant). BIS (Meaning & Zhu, 2011) estimated the 2011 MEP could reduce yields on >8-year securities by **~22 bps on average**. Hamilton & Wu (2011) estimated **14 bps** decline in 10-year yield, **11 bps** increase in 6-month rate. The 10-year/3-month spread fell **~75 bps** during the program. MBS yields fell **~50 bps** immediately after announcement.

### 4e. Emergency inter-meeting rate cuts signaled panic, producing negative market reactions

| Date | Cut | From → To | S&P 500 Day-Of | 10Y Treasury |
|---|---|---|---|---|
| **Jan 22, 2008** | 75 bps | 4.25% → 3.50% | **−1.1%** (DJIA −128; recovered from −312 intraday) | ~3.45%, falling on flight to safety |
| **Mar 3, 2020** | 50 bps | 1.75% → 1.25% | **−2.8%** | Broke **below 1%** for first time in history |
| **Mar 15, 2020** | 100 bps | 1.25% → 0.00–0.25% | **−12%** (March 16; worst since 1987; circuit breaker triggered) | ~0.73% |

In both March 2020 cuts, markets interpreted emergency action as signaling conditions were worse than anticipated, producing **sharply negative equity reactions**. The January 2008 cut was followed by another **50 bps on January 30** (total: 125 bps in 8 days), and seven more cuts through December 2008 to 0–0.25%.

**Lag to real economy**: standard estimate of **6–18 months** for output and employment effects. Fed Governor Waller (January 2023) cited **9–12 months** as a more recent estimate. Financial market transmission is nearly instantaneous; real economy effects take significantly longer.

### 4f. The BTFP lent at par value, peaked at >$165 billion, and largely contained SVB contagion

**Terms**: Rate at 1-year OIS + 10 bps (changed January 24, 2024 to floor at IORB rate). Collateral: Treasuries, agency debt, agency MBS **valued at 100% of par** — the key innovation. Loans up to 1 year. Eligible: all federally insured depository institutions. Treasury provided **$25 billion** ESF backstop.

**Timeline**: Announced **March 12, 2023** (Sunday); operational **March 13**. First week: $11.9 billion. Peaked at **>$165 billion** (BPI loan-level data analysis). Nearly **9,000 loans** to ~**1,327 borrowers**. New loans ceased **March 11, 2024**; final loan repaid **March 11, 2025**.

**Effectiveness**: The BTFP plus FDIC full-deposit guarantees for SVB/Signature largely halted contagion, but **First Republic Bank still failed May 1, 2023**. Discount window borrowing peaked at **$152.9 billion** (March 15, 2023 — above the 2008 record of $111B).

**Arbitrage problem**: When 1-year OIS fell below IORB (5.40%) starting November 2023, banks could borrow at ~4.76% and earn 5.40% risk-free — a **~60+ bps carry**. Borrowing surged from ~$110B to peak levels. Fed closed the arbitrage January 24, 2024 by flooring the rate at IORB.

A Treasury-collateral version for non-banks would require Section 13(3) emergency authority, likely an SPV structure (as in COVID-era PDCF/MMLF/CPFF), and would face greater credit risk assessment challenges without bank examination infrastructure.

### 4g. Regulatory forbearance has extensive precedent across five episodes

**S&L crisis (1980s)**: FHLBB lowered net worth requirements from **5% → 4% → 3%** (1980–82). Regulatory Accounting Principles allowed deferral of losses over 20–30 years. Congress amortized losses from mortgage portfolio sales across mortgage lifetimes. Cost: ~$124 billion to taxpayers.

**2009 fair value relaxation**: FSP FAS 157-4 (April 9, 2009) provided explicit guidance allowing valuation models (not fire-sale prices) for inactive markets. FSP FAS 115-2 split other-than-temporary impairment into credit losses (through earnings) and non-credit losses (through OCI only). Political pressure was intense — the March 12, 2009 House subcommittee hearing explicitly pressured FASB.

**COVID-19 (2020)**: CARES Act Section 4014 deferred CECL adoption. Joint banking agency rule provided a **five-year transition period** for CECL's capital impact. Community Bank Leverage Ratio was lowered from **9% to 8%**. TDR relief for COVID-related modifications.

**VaR model flexibility (2020)**: European regulators (ECB, April 16, 2020; also Canada, Switzerland, UK) temporarily allowed banks to **cap backtesting multipliers to year-end 2019 levels** to prevent procyclical capital increases from March 2020 volatility.

**2023 SVB**: No regulatory forbearance was granted. The BTFP effectively provided liquidity relief without mark-to-market recognition (par-value lending). Industry-wide unrealized losses on bank securities portfolios: **$620 billion at Q4 2022**, declining to **$478 billion** by end of 2023.

### 4h. FIMA and swap lines channeled $449 billion at peak, compressing FX basis within weeks

**Dollar swap lines** in March 2020 encompassed five standing partners (ECB, BOJ, BOE, BOC, SNB — unlimited) plus nine temporary partners ($30–60B caps each: Australia, Brazil, Korea, Mexico, Singapore, Sweden, Denmark, Norway, New Zealand). On March 15, pricing was cut to OIS + 25 bps (from +50 bps); 84-day terms added; frequency increased to daily on March 20. Peak outstanding: **$449 billion** (week of May 27, 2020). ~80% went to ECB and BOJ.

**FIMA Repo Facility**: Announced March 31, 2020; operational April 6, 2020. Made permanent **July 28, 2021**. Terms: overnight (7-day added February 2024) repos of Treasuries held in FRBNY custody. Rate: top of fed funds range. Per-counterparty limit: $60 billion. ~30 central banks initially enrolled (~75% of foreign official Treasury holdings). Notable usage: SNB drew **$60 billion** during the March 2023 Credit Suisse rescue (per McCauley, CEPR 2025).

**FX swap basis response**: EUR/USD overnight FX swap basis peaked at **644 bps on March 17, 2020** (the eve of first enhanced operations). After the March 18 allotment (ECB: $76B at 84-day + $36B at 7-day), short-term funding stress eased immediately. By **early June 2020**, FX swap spreads returned to **prepandemic levels**. Bahaj & Reis (2022, *Review of Economic Studies*) confirm swap lines put a **ceiling on CIP deviations**, functioning as predicted by Bagehot's lender-of-last-resort theory. Currencies with standing swap line access **stopped depreciating on March 19** and regained half their value in one week.

During **April 2025**, Powell publicly assured (April 16): "the Fed stands ready to supply dollar liquidity through standing central bank swaps." No evidence of large-scale activation was found.

---

## Section 5: Inflation constrains the Fed's willingness to intervene but has never fully prevented action

### 5a. Volcker eased in July 1982 partly because financial markets were breaking

The 1979–82 period produced extreme Treasury market stress. **30-year yields peaked at 15.25% in September 1981**, a ~520 bps increase from mid-1980, with prices down **~35%**. A dozen nonbank Treasury dealers failed between 1982 and 1985: **Drysdale Government Securities** (May 1982, $160 million interest payment default on ~$3.2 billion in borrowed securities; Chase Manhattan absorbed **~$270–285 million** in losses); **Lombard-Wall** (August 1982, Chapter 11 with $2.053 billion in borrowings); and others including Comark and E.S.M. Government Securities.

The Fed's response was targeted, not broad: after Drysdale, it **relaxed its securities lending program** for the first time since 1969 to alleviate settlement fails. The Fed did **not** conduct open market purchases to suppress yields. However, Volcker himself acknowledged that financial market stress was "a direct factor" in the July 1982 decision to ease: "By the summer of 1982 the financial fabric of the United States itself was showing clear signs of strain. All this contributed to the timing of our decision to ease policy in July 1982." The effective fed funds rate fell from **~14.92% (July 2) to ~10.4% (September 3)** — a 5 percentage point drop in two months — even though core CPI was still ~7.8%.

**Key precedent**: the Fed did not simultaneously maintain tight policy while supporting markets. Financial stress contributed to **ending** the tightening cycle.

### 5b. The Fed did not intervene during the 1994 "Great Bond Massacre"

The tightening cycle ran from **3.00% to 6.00%** (February 1994–February 1995). Thirty-year yields rose from **6.2% to >8%** (~200+ bps). Estimated global bond value losses: **~$1.5 trillion**. U.S. bond losses: **>$600 billion** (Fortune, October 1994). Specific casualties: Askin Capital Management (**>$400 million** losses, March 1994); Kidder Peabody (GE provided **~$550 million** in capital; shut down); Orange County (**$1.69 billion** loss, Chapter 9 bankruptcy December 6, 1994, on a $7.4 billion pool leveraged to ~$20 billion); Salomon Brothers ($371 million pretax loss in H1 1994); Steinhardt Partners (down **~30%**, losing $4 million per basis point).

**The Fed did not intervene in Treasury markets and did not pause tightening.** There is no public evidence the FOMC considered slowing rate hikes due to market stress. The 1994 experience arguably shaped Greenspan's subsequent approach — the argument that "the 1994 bond crash was one of the key events that turned Greenspan into Wall Street's best pal" has been widely noted.

### 5c. Academic literature is divided between "separation" and "leaning against the wind"

The debate centers on three camps. **The separation principle** (Bernanke, Svensson) holds monetary policy should target inflation/output while macroprudential tools handle financial stability. Svensson (JME 2016) concluded costs of leaning "greatly exceed benefits." The IMF (2015) estimated reducing crisis probability requires "substantial hikes" — probability reduced by only **0.04–0.3 percentage points per 100 bps rate hike**.

**Leaning against the wind** (Borio, Stein, Adrian) argues monetary policy "gets in all the cracks" of the financial system, unlike targeted regulation. Jeremy Stein (*QJE* 2012) provides the theoretical foundation. BIS Working Papers 114 (Borio & Lowe 2002), 440 (Borio 2014), 594, and 706 build the quantitative case. Adrian & Liang (IJCB 2018; NY Fed Staff Report 690) find "accommodative policy can create an intertemporal tradeoff between improving current financial conditions at a cost of increasing future financial vulnerabilities."

**The pragmatic middle** (Smets, IJCB 2014) supports macroprudential policy as the primary tool with monetary policy "keeping an eye on" financial stability. Adrian & Duarte (2017) model optimality of leaning during easy financial conditions. Martinez-Miera & Repullo (ECB WP 2297) find both tools useful but macroprudential "more effective."

### 5d. Current FOMC members acknowledge the tension with increasing specificity

**Governor Lisa Cook** (November 20, 2025, Georgetown — the most comprehensive current Fed statement on basis trade risk): "Achieving maximum employment and price stability depends on a stable financial system." She reported hedge fund Treasury holdings rose from **4.6% to 10.3% of outstanding** Treasuries between Q1 2021 and Q1 2025. On April 2025: the basis trade "remained fully intact" while swap-spread trades unwound.

**Chair Powell** (April 16, 2025, Economic Club of Chicago): "**We may find ourselves in the challenging scenario in which our dual-mandate goals are in tension.** If that were to occur, we would consider how far the economy is from each goal, and the potentially different time horizons over which those respective gaps would be anticipated to close." On Treasury markets during April tariff shock: "They're functioning just about as you'd expect them to function."

**Boston Fed President Collins** (April 11, 2025, Financial Times): The Fed was "**absolutely prepared**" to deploy tools to address market functioning concerns — the clearest public statement of intervention readiness during April 2025.

**Cleveland Fed President Hammack** (February 27, 2025): Top 10 hedge funds account for **40% of total repo borrowing** with **leverage ratios of 18:1**. Federal funds and repo liabilities grew only 19% since 2008 while Treasury debt climbed **five-fold**.

**FOMC minutes** have flagged basis trade risks with increasing frequency: November 2024 noted leverage was "partly on account of the prevalence of the Treasury cash-futures basis trade." May 2025 minutes observed "a durable shift in such correlations or a diminution of the perceived safe-haven status of U.S. assets could have long-lasting implications." January 2026 minutes flagged hedge funds' "growing footprint, rising leverage, and continued expansion of relative value trades."

The **FSOC Hedge Fund Working Group** (December 2024) reported aggregate qualifying hedge fund gross assets of **$9.6 trillion**, repo borrowing at a record **$2.2 trillion**, with the top 10 funds reaching **$1.3 trillion combined**. The 2025 FSOC Annual Report under the Trump Administration "notably moves away from recommending policy actions" on these risks.

---

## Conclusion: the empirical record reveals conditional thresholds, not bright lines

The data assembled here reveals that Treasury market stress thresholds are **endogenous to dealer capacity utilization, not fixed levels** of yield movement or volatility. The March 2020 crisis required $1.6 trillion in Fed purchases over weeks; the April 2025 shock resolved without intervention partly because repo markets held and dealer intermediation capacity was not exhausted. The critical variables are not yields alone but the **interaction of volatility, dealer balance-sheet utilization, and the functioning of repo markets** — the Dallas Fed's finding that intermediation capacity matters more than funding rates is the single most important empirical insight.

The Fed's toolkit is powerful but asymmetric: the SRF and swap lines can address funding stress within hours; SLR exemptions and purchase programs take days to weeks; and each tool carries inflation-credibility costs that the current FOMC has acknowledged but not resolved. The historical record — Volcker eased in 1982 when markets broke, Greenspan did not intervene in 1994 — suggests the **binding constraint on Fed action is not institutional capability but the inflation backdrop**. With current FOMC members explicitly framing this as a tension between dual-mandate goals, the response function will depend on where inflation stands when the next Treasury market dislocation arrives.