# RP-REG-5.1: KRE & Regional Bank Volume Deep-Dive
**Date:** 2026-04-09 | **Status:** ALL 7 TASKS COMPLETE

---

## Overview

Will identified unusually low KRE volume and initiated a structured multi-task volume investigation. This research applies a relative volume framework across KRE and thesis names (WAL, OZK, EGBN, ZION, CFG) to understand who is positioned, how, and what the volume signature implies for our put positions.

## Task 1: Individual Name Volume vs KRE

**Method:** 10/20/60/252-day moving average volume, relative volume ratios, divergence analysis.

**Key Data (Apr 9, intraday):**

| Ticker | Close | Tod/20d | 20d/60d | 60d/252d | Apr/252d |
|--------|-------|---------|---------|----------|----------|
| KRE | $68.69 | 0.85x | 0.90x | 1.23x | 0.79x |
| WAL | $75.00 | 1.19x | 0.99x | 1.22x | 0.88x |
| OZK | $47.49 | 1.06x | 0.98x | 1.21x | 0.83x |
| EGBN | $26.69 | 1.34x | 0.87x | 0.83x | 0.75x |
| ZION | $61.00 | 1.18x | 0.88x | 1.13x | 0.86x |
| CFG | $63.78 | 1.20x | 0.85x | 1.09x | 0.88x |

**Findings:**
1. KRE is the LEAST active name (0.85x), every individual name is ABOVE 1.0x their 20-day average. Volume migrating from ETF to single names.
2. WAL has the largest divergence vs KRE (+0.34). Pre-earnings positioning likely.
3. EGBN highest relative activity (1.34x) but from a low structural base (60d/252d = 0.83x, only name below normal).
4. April universally quiet (0.75-0.88x annual avg). Quarter was hot (Iran panic). Month is dead.
5. The divergence (names active, ETF dead) is 90th percentile over the past year (1.1 sigma). Occurs ~10% of trading days. Top divergence days cluster around OpEx — today is NOT OpEx, making it more organic.

**Historical forward returns after KRE<1.0x + names>1.0x days:**
- 5d avg: +1.3% (61% win rate), 10d: +1.3% (52%), 20d: +2.6% (52%). Weak signal — regime indicator, not price predictor.

---

## Task 2: Up-Day vs Down-Day Volume (Accumulation/Distribution)

**Method:** Classify days by direction, compare average volume on up vs down days, compute ratios across 20/60/252-day windows. Magnitude-weighted analysis (volume * |% move|).

**Simple Up/Down Volume Ratios (20-day):**

| Ticker | Up Vol | Dn Vol | Ratio | Signal |
|--------|--------|--------|-------|--------|
| KRE | 17.18M | 20.06M | 0.86x | Distribution |
| WAL | 1.38M | 1.44M | 0.96x | Near-balanced |
| OZK | 1.05M | 1.96M | 0.53x | HEAVY distribution |
| EGBN | 0.30M | 0.37M | 0.81x | Distribution |
| ZION | 1.68M | 1.77M | 0.95x | Near-balanced |
| CFG | 4.28M | 4.93M | 0.87x | Distribution |

**Key Findings:**
1. Every name has more volume on down days than up days (all ratios <1.0 over 20 days).
2. OZK at 0.53x is extreme — down days carry DOUBLE the volume of up days. Persistent seller.
3. WAL at 0.96x is the best of the group — nearly balanced. Volume profile has recovered.
4. Pattern is RECENT, not structural. 252-day ratios are all near 1.0x. Distribution started with Iran panic.

**Rolling 20-day ratio evolution:**
- KRE: 1.12x (Jan) → 0.71x (mid-Mar peak selling) → 0.86x (recovering)
- WAL: 1.06x (Jan) → 0.63x (mid-Mar) → 0.96x (RECOVERED)
- OZK: 1.07x (Jan) → 0.50x (now) → 0.53x (STILL DETERIORATING)

WAL recovered. OZK did not. Different animals.

**Magnitude-Weighted Analysis (20-day):**

| Ticker | Up Force | Dn Force | Ratio | Signal |
|--------|----------|----------|-------|--------|
| KRE | 2.5M | 1.2M | 2.03x | Buying force dominates |
| WAL | 0.3M | 0.2M | 1.24x | Lean accumulation |
| OZK | 0.1M | 0.1M | 1.04x | Balanced |
| ZION | 0.3M | 0.2M | 2.19x | Buying force dominates |

**But 60-day magnitude-weighted tells opposite story:**
- KRE: 0.84x (lean distribution)
- WAL: 0.47x (SELLING FORCE DOMINATES — worst in table)
- OZK: 0.71x (lean distribution)

**Interpretation:** The quarter's selling was high-participation (many shares, moderate down days = institutional distribution). The month's buying is low-participation, high-magnitude (sharp bounces on thin volume = short covering). OZK is textbook: 0.53x raw (selling conviction) but 1.04x magnitude-weighted (pops on thin book). That's short covering, not accumulation.

---

## Task 3: Volume Around Catalyst Dates

**Method:** 5-day windows [-2, +2] around 10 identified catalysts. Relative volume (vs 20-day trailing avg) computed for each window day. Events classified as stress/relief, macro/sector/name-specific.

**Catalysts Analyzed:**
- Iran war escalation (Mar 3), Quad witching (Mar 20), WAL Fiserv (Mar 17), WAL downgrades (Mar 25), First Brands (Mar 31), PC media coverage (Apr 1), Blue Owl redemptions (Apr 2), Barings gating (Apr 6), OZK dividend (Apr 7), Brent crash (Apr 7)

**Stress vs Relief Volume (event day averages):**

| | KRE | WAL | OZK |
|---|-----|-----|-----|
| Avg RV stress events | 0.83x | 0.74x | 1.20x |
| Avg RV relief events | 0.67x | 0.66x | 0.73x |
| Stress/Relief ratio | 1.24x | 1.11x | 1.65x |

OZK's volume spikes on bad news (1.65x more than good news). Market engages with OZK on fear, ignores it on optimism.

**Anticipation Test — THE KEY FINDING:**

Stress events — avg relative volume by offset:
- D-2: KRE 1.08x (elevated BEFORE event)
- D-1: 0.91x (declining into event)
- D0: 0.83x (event day)
- D+1: 0.72x (collapses)
- D+2: 0.67x (stays dead)

Relief events — avg relative volume by offset:
- D-2: 0.70x (dead)
- D-1: 0.46x (VERY dead — half normal)
- D0: 0.67x (low)
- D+1: 0.84x (waking up)
- D+2: 1.07x (finally normal)

**Interpretation:** Selling is ANTICIPATORY (volume elevated before bad news). Buying is REACTIVE (volume only rises after good news). Classic institutional distribution footprint — informed money sells ahead, uninformed money buys late.

**WAL-specific events:** All three (Fiserv, triple downgrade, First Brands) had LOW volume and POSITIVE returns. Market not reacting to known WAL catalysts. Thesis will resolve on something market ISN'T positioned for (MI3, AOCI in Call Reports).

**OZK dividend hike:** Stock FELL -0.53% on 0.64x volume. Market saw through the confidence signal.

---

## Task 4: ETF Creation/Redemption (Fund Flows)

**Method:** Web research for KRE shares outstanding, AUM, fund flow data from SSGA, etfdb.com, Nasdaq, ETF.com. Derived shares outstanding from AUM/price where direct data unavailable.

**KRE Shares Outstanding:**
- Week of Mar 3: -14.4% in one week ($670.8M outflow). Biggest in 4 years (ETF.com).
- Mar 24: ~65.0M shares (derived: AUM $4.18B / price $64.34)
- Apr 8: 56.9M shares (confirmed SSGA)
- **Mar 24 → Apr 8: -8.1M shares (-12.4%) while price +6.8%**

**Fund Flows:**
- 5-day: +$235M (recent bounce-back)
- 1-month: -$8M (flat)
- 3-month: -$66M (net outflow)
- 6-month: +$283M
- 1-year: +$178M

**KRE vs XLF (critical comparison):**
- KRE 1-month: -$8M | XLF 1-month: +$1,220M
- KRE 3-month: -$66M | XLF 3-month: +$759M

Money flowing INTO broad financials, OUT OF regionals. Surgical de-risking of regional banks specifically.

**Interpretation:** APs are dismantling the ETF — redeeming shares (turning units into stock baskets) and selling underlying individually. This directly explains Task 1 (ETF volume dying = ETF shrinking). Price rising despite shrinkage = thinner market, remaining holders self-selected. Rally is less informative than it appears. The +$235M 5-day inflow is worth watching — if sustained, distribution thesis has shorter shelf life.

---

## Synthesis Across Tasks 1-4

1. **ETF volume dying, single-name volume diverging** — because APs are redeeming the ETF and selling components individually
2. **Selling has more conviction than buying** — especially OZK (0.53x up/down ratio, persistent distribution)
3. **Selling is anticipatory, buying is reactive** — informed money positioned ahead of stress, uninformed money chases relief
4. **Regional bank de-risking is surgical** — money leaving KRE while flowing into XLF. Market discriminating regionals from G-SIBs.
5. **The rally is a thin-market bounce** — price up 6.8% on 12.4% fewer shares. Short covering and passive flows, not institutional accumulation.

**For Positions:**
- OZK puts have cleanest volume confirmation of any name
- WAL volume profile is more ambiguous (recovered to near-balanced) — be selective with Jun puts
- KRE puts face structural headwind (shrinking ETF, less liquid)
- Single-name puts are cleaner thesis expression than ETF puts in current regime
- Timing risk on Jun expiries due to thin-market volatility; Sep+ gives runway

**The thesis hasn't changed. The market microstructure now confirms the thesis hasn't been priced in by buyers — it's been partially priced by seller absence. The real test is Q1 earnings and Call Reports.**

---

## Task 5: Dark Pool / Off-Exchange Volume

**Method:** Chartexchange.com daily off-exchange volume data (sourced from FINRA OTC Transparency). Off-exchange includes dark pools (ATS) and non-ATS OTC venues (wholesalers, single-dealer platforms). Short volume from FINRA reporting venues. Compared today's readings (intraday Apr 9) against 30-day averages.

### Off-Exchange % — Today vs 30-Day Average

| Ticker | Today Off-Ex % | 30d Avg | Delta (pp) | Signal |
|--------|---------------|---------|------------|--------|
| KRE | 28.84% | 28.65% | +0.2 | Normal |
| WAL | **54.47%** | 37.55% | **+16.9** | VERY ELEVATED |
| OZK | **42.26%** | 33.58% | **+8.7** | ELEVATED |
| EGBN | **45.85%** | 32.73% | **+13.1** | VERY ELEVATED |
| ZION | 38.17% | 36.04% | +2.1 | Normal |
| CFG | 38.69% | 35.36% | +3.3 | Normal |

**The three weakest fundamental names (WAL, OZK, EGBN) have massively elevated dark pool activity on a big risk-on day. Clean names (ZION, CFG) and the ETF are at baseline.** This is the distribution signature — someone is using the rally to offload via dark pools.

### Daily Off-Exchange Trend (April)

**WAL — escalating:**
| Date | Off-Ex % | Direction | Note |
|------|----------|-----------|------|
| 3/30 | 29.34% | — | Pre-rally baseline |
| 3/31 | 33.64% | ↑ | |
| 4/1 | 40.99% | ↑ | Brent tensions |
| 4/2 | 32.61% | ↓ | |
| 4/6 | 38.80% | ↑ | |
| 4/7 | 32.01% | ↓ | Brent crash starts |
| 4/8 | 38.30% | ↑ | Risk-on day |
| 4/9 | **54.47%** | ↑↑ | Biggest up day → highest dark pool day |

**OZK — steady escalation:**
| Date | Off-Ex % | Direction |
|------|----------|-----------|
| 4/1 | 33.21% | — |
| 4/2 | 35.71% | ↑ |
| 4/6 | 29.42% | ↓ |
| 4/7 | 36.28% | ↑ |
| 4/8 | 36.68% | ↑ |
| 4/9 | **42.26%** | ↑ |

**KRE — stable, no signal:**
| Date | Off-Ex % | Direction |
|------|----------|-----------|
| 3/31 | 27.75% | — |
| 4/1 | 22.50% | ↓ |
| 4/2 | 25.61% | ↑ |
| 4/6 | 29.71% | ↑ |
| 4/7 | 26.99% | ↓ |
| 4/8 | 28.92% | ↑ |
| 4/9 | 28.84% | → |

### Short Volume Overlay

FINRA short volume data adds a second dimension — what fraction of reported volume is short sales.

| Ticker | 30d Avg Short Vol % | Recent Peak | Recent Low | Trend |
|--------|-------------------|-------------|------------|-------|
| KRE | **65.26%** | 81.77% (Mar 31) | 53.72% (Apr 7) | Declining from extreme |
| OZK | **47.66%** | 64.40% (Apr 1) | 38.16% (Mar 30) | Declining from spike |
| WAL | ~40% | 50.83% (Mar 26) | 34.25% (Apr 8) | Declining |

**KRE daily short volume:**
| Date | Short Vol | Total Vol | Short % |
|------|-----------|-----------|---------|
| 3/27 | 6,264,633 | 9,893,417 | 63.32% |
| 3/30 | 6,725,074 | 9,820,817 | 68.48% |
| 3/31 | 13,575,353 | 16,601,398 | **81.77%** |
| 4/1 | 7,375,690 | 10,437,085 | 70.67% |
| 4/2 | 5,188,479 | 7,570,298 | 68.54% |
| 4/6 | 3,061,608 | 4,477,236 | 68.38% |
| 4/7 | 3,870,499 | 7,204,716 | 53.72% |
| 4/8 | 5,911,650 | 9,696,941 | 60.96% |

**OZK daily short volume:**
| Date | Short Vol | Total Vol | Short % |
|------|-----------|-----------|---------|
| 3/26 | 144,447 | 305,791 | 47.24% |
| 3/27 | 122,278 | 247,963 | 49.31% |
| 3/30 | 115,768 | 303,350 | 38.16% |
| 3/31 | 221,272 | 473,803 | 46.70% |
| 4/1 | 227,162 | 352,732 | **64.40%** |
| 4/2 | 205,666 | 360,783 | 57.01% |
| 4/6 | 114,232 | 203,147 | 56.23% |
| 4/7 | 145,604 | 350,649 | 41.52% |
| 4/8 | 206,225 | 492,936 | 41.84% |

### FINRA Short Volume — Full Month History (Feb 27 – Apr 8)

Pulled directly from FINRA Reg SHO daily files (cdn.finra.org/equity/regsho/daily/). All venues combined. Full data in `workbook/SHORT_VOL.tsv`.

**WAL — Volume collapse is the headline:**
- Total volume: 2.7M (Mar 6) → 176K (Apr 6) → 500K (Apr 8). **93% peak-to-trough decline.**
- Short %: volatile 26-61%, no clear trend. Average ~43%.
- Key dates: 61.3% on Mar 5 (thin vol spike), 58.0% on Apr 2 (222K total — very thin)
- **Critical insight: Today's 54% off-exchange spike is NOT driven by short selling** (short % was only 40.7% yesterday). The dark pool activity is dominated by LONG HOLDERS EXITING, not shorts entering.

**OZK — Active short pressure, unlike WAL:**
- Short % range: 23-80%. Average ~49%.
- Extreme readings: 80.4% on Mar 18, 72.1% on Mar 6, 70.7% on Mar 19
- The 80.4% is extraordinary — 4 of 5 shares traded were short sells
- Recent: declining to 41-42% in April, but structurally higher than WAL
- OZK has genuine short pressure on top of long distribution. Double headwind.

**KRE — AP redemption mechanics confirmed:**
- Short % range: 52-85%. Average ~68%. Consistently the highest.
- Extreme: 85.0% on Mar 25, 83.9% on Mar 10, 82.0% on Mar 31
- Declining to 52-57% in April as redemption wave eases
- This IS the AP mechanism — market makers short KRE while redeeming creation units

**EGBN — Bifurcated pattern:**
- March: very high short % (67-84%). Active shorting.
- April: collapsed to 18-30%. Short activity dried up.
- Combined with today's 46% off-exchange spike → longs exiting, not shorts entering. Same pattern as WAL.

### Key Findings

1. **Dark pool activity discriminates by fundamental quality.** WAL (+17pp), OZK (+9pp), EGBN (+13pp) all spiking above 30d averages on today's rally. ZION, CFG, and KRE are flat. Whoever is trading off-exchange knows which names are weakest.

2. **WAL's 54.47% off-exchange on its biggest up day is the single most important number in this analysis.** On the day WAL rallies +6.3%, more than half of all volume moves through dark pools. This is the textbook definition of selling into strength off-exchange. If this were accumulation, you'd buy on-exchange to move the visible bid.

3. **KRE ETF has LOWER off-exchange % (~29%) than single names (~33-42%).** This is structurally unusual — ETFs normally have higher dark pool %. Explanation: AP redemptions happen on-exchange (lit market, visible), while single-name distribution goes off-exchange (hidden). Two different mechanisms, same direction: institutional exit.

4. **KRE short volume at 65% average, peaked at 82% on Mar 31.** This is consistent with AP redemption mechanics: market makers short KRE while simultaneously redeeming creation units. The extreme 82% reading on the day of the largest stress spike confirms the mechanism. Now declining (54-61%) as redemption pressure eases — but still well above the ~50% equilibrium.

5. **OZK short volume spiked to 64% on Apr 1 (the Brent tension peak) and remains elevated at ~42%.** This pairs with the off-exchange spike: short sellers are using dark pools to build/maintain positions. The Apr 1 spike was the day after the Iran escalation peak — informed positioning ahead of further stress.

6. **The rally is being distributed through.** Combine with Task 2 (selling has more conviction) and Task 4 (AP redemption): institutions are using every up day to offload, and they're doing it off-exchange to minimize visible footprint. The price can rise while smart money exits — this is the defining characteristic of a thin-market rally.

### Structural Insight: ETF vs Single-Name Distribution Mechanics

Two parallel distribution channels are operating simultaneously:

**Channel 1 — ETF (on-exchange, visible):**
- APs redeem KRE creation units → short KRE → deliver underlying basket
- Shows up as: shrinking shares outstanding (56.9M, -12.4%), high short volume (65%), declining total volume
- This is VISIBLE and STRUCTURAL — it's the plumbing of the de-risking

**Channel 2 — Single names (off-exchange, hidden):**
- Institutions sell WAL, OZK, EGBN through dark pools on up days
- Shows up as: off-exchange % spiking to 42-54% on green days, vs normal ~33-37%
- This is HIDDEN and TACTICAL — using rallies as liquidity events to exit

The two channels are complementary. The ETF shrinks structurally while individual names get distributed tactically. Both reduce institutional regional bank exposure. The price rises because remaining flows (retail, passive, short covering) dominate the thinner lit market.

---

## Updated Synthesis (Tasks 1-5)

1. **ETF volume dying, single-name volume diverging** (Task 1) — because APs are redeeming ETF on-exchange
2. **Selling has more conviction than buying** (Task 2) — especially OZK (0.53x up/down ratio)
3. **Selling is anticipatory, buying is reactive** (Task 3) — informed money positioned ahead
4. **Regional bank de-risking is surgical** (Task 4) — KRE shrinking while XLF grows
5. **Dark pool activity confirms hidden distribution in weakest names** (Task 5) — WAL, OZK, EGBN spiking off-exchange on up days; clean names normal
6. **Two-channel distribution mechanism identified** — ETF structural (on-exchange AP redemption) + single-name tactical (off-exchange dark pool selling on rallies)

**For Positions (updated):**
- OZK remains cleanest put confirmation: persistent distribution (0.53x up/down), rising dark pool % (42% vs 33% avg), elevated short volume (64% peak)
- WAL dark pool signature TODAY is extreme (54%) but was otherwise recovering — watch for persistence vs one-day anomaly
- EGBN dark pool spike (46% vs 33% avg) is notable given lowest structural volume — small-cap, low-float, easier to move
- KRE puts face two headwinds: shrinking float AND higher short volume (65%) creates squeeze risk on up days
- Thesis conviction on single-name puts strengthened; KRE put conviction weakened

---

## Task 6: Options Volume vs Equity Volume

**Method:** yfinance options chains for all thesis names. Pulled volume, open interest, and implied volatility across all available expiries. Compared options/equity ratios, put/call ratios, and identified OI concentration by strike.

### Options/Equity Volume Ratio

| Ticker | Opt Vol | Equity Vol | Opt/Eq % | Signal |
|--------|---------|-----------|----------|--------|
| KRE | 71,475 | 8,100,925 | 0.9% | Highest — ETF options active |
| ZION | 2,613 | 877,134 | 0.3% | Normal |
| OZK | 2,431 | 889,757 | 0.3% | Normal |
| WAL | 2,028 | 651,912 | 0.3% | Normal |
| EGBN | 691 | 248,395 | 0.3% | Normal |
| CFG | 3,520 | 2,941,410 | 0.1% | Very low |

**Finding:** Options volume is LOW relative to equity across all single names (~0.3%). Distribution is happening through shares, not options. The equity market is the battlefield — options are being used for positioning, not for daily trading.

### Put/Call Ratios — THE DISCRIMINATING SIGNAL

**By daily volume (today's flow):**

| Ticker | P/C Vol | Signal |
|--------|---------|--------|
| EGBN | **2.70** | Extreme put dominance |
| KRE | **2.36** | Heavy put flow |
| WAL | 0.91 | Balanced |
| OZK | 0.46 | Call-dominated today |
| ZION | 0.42 | Call-dominated |
| CFG | 0.33 | Call-dominated |

**By open interest (cumulative positioning):**

| Ticker | P/C OI | Signal |
|--------|--------|--------|
| EGBN | **11.10** | EXTREME — 11x more put OI than call OI |
| OZK | **1.56** | Put-heavy |
| KRE | **1.54** | Put-heavy |
| WAL | **1.19** | Slight put lean |
| ZION | 0.97 | Balanced |
| CFG | 0.64 | Call-dominated |

**Key insight:** Today's volume shows call-buying in OZK and ZION (short-covering rally via options), but the CUMULATIVE positions (OI) are put-heavy for all thesis names. The daily flow is noise; the established positioning is bearish. EGBN at 11x put/call OI is one of the most extreme readings you'll find in a mid-cap bank.

### Open Interest Concentration — Where Are the Big Bets?

**KRE Apr 17 (expires in 8 days) — MASSIVE put walls:**

| Strike | Put OI | $ from current ($69.89) | Contracts × 100 shares |
|--------|--------|------------------------|----------------------|
| $68 | **57,432** | -2.7% | 5.74M shares of delta |
| $60 | **39,212** | -14.1% | 3.92M shares |
| $64 | **29,093** | -8.4% | 2.91M shares |
| $67 | **23,166** | -4.1% | 2.32M shares |
| $63 | **22,260** | -9.9% | 2.23M shares |
| $62 | **21,040** | -11.3% | 2.10M shares |
| $65 | **17,301** | -7.0% | 1.73M shares |
| Total Apr 17 put OI | **300,488** | | 30M shares |

300,488 put contracts = control of 30M shares' worth of notional. KRE only has 56.9M shares outstanding. That means Apr 17 put OI alone represents ~53% of the float. Dealers hedging these puts are a MASSIVE mechanical force.

The $68 strike (57K OI) is particularly dangerous — it's only 2.7% below current price. If KRE dips below $68, dealer delta hedging accelerates selling. That strike is a gravity well.

**KRE Jun 18 — Even larger concentrations:**

| Strike | Put OI | $ from current |
|--------|--------|---------------|
| $58 | **61,148** | -17.0% |
| $40 | **58,840** | -42.8% |
| $55 | **40,265** | -21.3% |
| $50 | **27,776** | -28.5% |
| $52 | **15,612** | -25.6% |
| $63 | **15,000** | -9.9% |
| $64 | **14,052** | -8.4% |

The $58 Jun put with 61K OI is the largest single position in the entire options universe for KRE. Someone (or many someones) is positioned for KRE to be at $58 or below by June — a 17% decline from here. The $40 strike with 59K OI is a catastrophe bet.

**WAL Jun 18 — Concentrated at $60:**

| Strike | Put OI | $ from current ($77.10) |
|--------|--------|------------------------|
| $60 | **1,744** | -22.2% |
| $75 | **669** | -2.7% |
| $65 | **464** | -15.7% |
| $70 | **130** | -9.2% |
| $77.50 | **114** | -0.5% |

The $60 put is the monster — 1,744 contracts. That's a bet on WAL dropping 22% to crisis levels. Not a hedge; at $60, WAL is in existential territory. The $75 strike (669 OI) is the pragmatic position — just slightly OTM, betting on a moderate decline through earnings.

**OZK May 15 — Near-term put wall at $40:**

| Strike | Put OI | $ from current ($48.29) |
|--------|--------|------------------------|
| $40 | **1,647** | -17.2% |
| $42.50 | **835** | -12.0% |
| $22.50 | **501** | -53.4% |
| $45 | **483** | -6.8% |

The $40 put with 1,647 OI in MAY — that's a near-term conviction bet. OZK at $40 would be -17% from here, which maps closely to the kind of move a bad earnings report or Call Report reveal could trigger. The $22.50 put (501 OI) is a zero-to-hero catastrophe position.

**EGBN Jun 18 — The $5 put mystery:**

| Strike | Put OI |
|--------|--------|
| $5 | **1,301** |

EGBN has 1,301 put contracts at the $5 strike — that's a bet the stock goes to essentially zero. At $0.05 per contract, it's cheap insurance. Given EGBN's hidden CRE ratio (23.7%) and thin float, this isn't as crazy as it looks. But it heavily inflates the 11x P/C OI ratio. Adjusting for the $5 strike, the ratio is still ~1.2x put-heavy — modest but directional.

### Implied Volatility Levels

| Ticker | Near-money Jun IV | Normal bank IV | Elevated? |
|--------|------------------|---------------|-----------|
| WAL | 46-55% | 25-35% | YES — significantly |
| OZK (May) | 35-50% | 25-35% | YES — moderately |
| KRE (Jun) | 31-42% | 20-30% | YES — moderately |

WAL's IV is the most elevated — the options market is pricing 46-55% annualized vol vs what would normally be 25-35% for a regional bank. This means:
- Puts are "expensive" relative to normal times
- But the market EXPECTS elevated moves — it's not mispricing, it's risk-aware
- Realized vol has been running high (thin market, violent moves), so IV may actually be fair

### Key Findings

1. **Distribution is happening through shares, not options.** Opt/equity ratios of ~0.3% across single names. The dark pools and equity flow (Tasks 1-5) are the main event. Options are the secondary positioning layer.

2. **But cumulative options positioning is bearishly skewed.** Put/call OI ratios: EGBN 11x, OZK 1.56x, KRE 1.54x, WAL 1.19x. The established positions are directionally bearish even as today's daily flow shows call-buying (rally chasing).

3. **KRE put OI is a mechanical force.** 300K put contracts expiring Apr 17 (8 days). 57K at the $68 strike — just 2.7% below current price. Dealer hedging creates gravitational pull toward these strikes. If KRE breaks $68, delta hedging accelerates the move.

4. **The KRE $58 Jun put (61K OI) is the market's consensus downside target.** Largest single position across all KRE options. Implies the market expects ~17% downside by June.

5. **WAL's $60 Jun put (1,744 OI) is a crisis bet.** Not a hedge — a directional position expecting a 22% decline. Someone is positioned for WAL to break.

6. **OZK's May $40 put (1,647 OI) is near-term conviction.** Betting on -17% by mid-May. That's an earnings-driven bet — OZK reports ~Apr 17-22.

7. **Options confirm what equity microstructure shows, but add a timeline.** The put OI tells us WHEN the market expects the move: Apr 17 (KRE, OZK earnings) and Jun 18 (Call Report season). Our Jun puts are aligned with the market's timeline.

---

## Updated Synthesis (Tasks 1-6)

1. **ETF volume dying, single-name volume diverging** (Task 1) — APs redeeming ETF on-exchange
2. **Selling has more conviction than buying** (Task 2) — OZK 0.53x up/down ratio
3. **Selling is anticipatory, buying is reactive** (Task 3) — informed money positioned ahead
4. **Regional bank de-risking is surgical** (Task 4) — KRE shrinking while XLF grows
5. **Dark pool activity confirms hidden distribution in weakest names** (Task 5) — WAL/OZK/EGBN spiking off-exchange on up days
6. **Options positioning is bearishly skewed with massive KRE put walls** (Task 6) — distribution through shares, conviction through options, dealer hedging creates mechanical downside risk

**For Positions (updated with Task 6):**
- OZK: cleanest single-name setup. Distribution on every metric + 1,647 May $40 put OI = near-term conviction from the options market. Hold Jun puts.
- WAL: hidden distribution (dark pools) + $60 Jun put (1,744 OI crisis bet) + elevated IV (46-55%). Jun $85P is aligned with the options market's expectation but timing risk remains. Revisit after earnings.
- KRE: the options tail is wagging the dog. 300K put contracts in Apr 17 alone. The $68 strike (57K OI) is a mechanical pin/acceleration level. If KRE closes below $68, dealer hedging cascades. BUT — squeeze risk is equally real. Short covering + shrinking float + this much put OI = violent moves in both directions.
- EGBN: most extreme P/C ratio (11x OI) but driven by deep OTM catastrophe bets. The options market is pricing tail risk, not base-case decline.

---

## Task 7: Short Interest Trend Overlay

**Method:** Benzinga bi-monthly short interest reports (sourced from FINRA/exchange filings). Pulled 6+ months of SI history for all thesis names. Most recent settlement date: Mar 13, 2026 (disseminated Mar 24).

### Current Short Interest Snapshot

| Ticker | SI Shares | SI % Float | Days to Cover | 6-Mo Trend | Signal |
|--------|-----------|-----------|--------------|-----------|--------|
| OZK | **15.67M** | **15.28%** | **12.04** | Rising (13.74→15.28) | EXTREME — shorts adding |
| EGBN | 2.77M | **11.10%** | **9.45** | Declining (13.25→11.10) | High but easing |
| KRE | **69.35M** | — | 2.8 | **Rising +64% (42.2M→69.4M)** | ETF is the short vehicle |
| CFG | 14.20M | 4.44% | 2.45 | Declining (5.17→4.44) | Normal |
| ZION | 5.06M | 4.03% | 3.24 | Declining (5.31→4.03) | Shorts covering |
| WAL | 3.69M | **3.46%** | 1.59 | **Declining (4.47→3.46)** | Shorts covering |

### Short Interest History (6 months)

**OZK — Shorts keep adding through the rally:**
| Date | SI Shares | % Float | Days to Cover |
|------|-----------|---------|---------------|
| 10/31/25 | 14.29M | 13.74% | 8.77 |
| 11/14/25 | 14.71M | 14.14% | 12.10 |
| 11/28/25 | 15.01M | 14.43% | 14.02 |
| 12/15/25 | 14.94M | 14.36% | 15.47 |
| 12/31/25 | 15.43M | 14.84% | 16.73 |
| 01/15/26 | 15.37M | 14.99% | 11.92 |
| 01/30/26 | 15.17M | 14.80% | 7.42 |
| 02/13/26 | 15.54M | 15.16% | 14.52 |
| 02/27/26 | 15.55M | 15.17% | 14.66 |
| 03/13/26 | **15.67M** | **15.28%** | **12.04** |

Steady climb from 13.74% to 15.28% over 5 months. No covering during the rally. Shorts have HIGH conviction and are adding. 12 days to cover = extreme squeeze risk if thesis is wrong, but extreme downside fuel if thesis is right.

**WAL — Shorts are leaving:**
| Date | SI Shares | % Float | Days to Cover |
|------|-----------|---------|---------------|
| 10/31/25 | 4.43M | 4.13% | 2.23 |
| 11/14/25 | 4.30M | 4.01% | 5.32 |
| 12/15/25 | 3.47M | 3.24% | 3.78 |
| 12/31/25 | 3.88M | 3.62% | 4.81 |
| 01/15/26 | 4.52M | 4.25% | 5.82 |
| 01/30/26 | 4.48M | 4.20% | 4.15 |
| 02/13/26 | 4.76M | 4.47% | 3.92 |
| 02/27/26 | 4.74M | 4.45% | 3.00 |
| 03/13/26 | **3.69M** | **3.46%** | **1.59** |

Peaked at 4.76M (Feb 13), then dropped to 3.69M by Mar 13. **1.07M shares covered in 4 weeks.** That's real buying pressure contributing to the rally. Days to cover collapsed to 1.59 — shorts can exit quickly, low squeeze risk remaining.

**KRE — ETF short interest surging:**
| Date | SI Shares | Days to Cover |
|------|-----------|---------------|
| 01/15/26 | 42.24M | 2.71 |
| 01/30/26 | 45.58M | 2.51 |
| 02/13/26 | 58.89M | 2.49 |
| 02/27/26 | 55.79M | 2.49 |
| 03/13/26 | **69.35M** | **2.80** |

**+64% increase in 2 months (42.2M → 69.4M).** Combined with shares outstanding declining from ~65M to 56.9M (Task 4), this is remarkable: short interest now EXCEEDS shares outstanding. Shorts sold short more shares than exist in the fund. This is mechanically possible because of AP creation/redemption, but it means the ETF is extraordinarily leveraged to both directions.

**EGBN — High but declining from peak:**
| Date | SI Shares | % Float | Days to Cover |
|------|-----------|---------|---------------|
| 12/15/25 | 3.30M | 13.25% | 6.49 |
| 12/31/25 | 3.05M | 12.23% | 8.16 |
| 01/15/26 | 2.84M | 11.39% | 10.11 |
| 01/30/26 | 2.77M | 11.12% | 4.46 |
| 02/13/26 | 2.67M | 10.70% | 8.19 |
| 02/27/26 | 2.65M | 10.62% | 9.39 |
| 03/13/26 | **2.77M** | **11.10%** | **9.45** |

Declined from 13.25% to 10.62%, then ticked back up to 11.10%. 9.45 days to cover is still elevated. Shorts partially covered but are coming back.

### Key Findings

1. **Shorts are CONCENTRATING into OZK and KRE, covering WAL/ZION/CFG.** The short trade is getting more targeted — betting on the weakest fundamental name (OZK) and the broad ETF (KRE), while reducing exposure to names that could squeeze. This is informed positioning.

2. **OZK is the most heavily shorted name at 15.28% of float.** This has been steadily climbing for 5 months — through the Iran rally, through every bounce. Shorts are not flinching. 12 days to cover means a squeeze would be violent, but also means shorts are very committed. This pairs with the 80% short volume peak (Task 5) — shorts are both holding existing positions AND actively pressing with new shorts.

3. **WAL shorts covered 1.07M shares in 4 weeks (Feb-Mar).** This EXPLAINS part of the WAL rally. Combined with Task 5 (longs exiting through dark pools), we now have the full picture: WAL's rally is fueled by short covering (buying) while longs simultaneously exit (selling through dark pools). Both sides are leaving. The stock is becoming a vacuum — less directional conviction from either longs or shorts. Catalyst-dependent.

4. **KRE short interest now exceeds shares outstanding (69.4M SI vs 56.9M shares).** This is the single most structurally loaded position in the entire regional bank complex. Combined with 300K put contracts (Task 6) and AP redemptions (Task 4), KRE is a coiled spring. Direction TBD — but the magnitude of the eventual move will be enormous.

5. **EGBN shorts ticked back up (+120K shares in latest period).** Still 11.1% of float with 9.45 days to cover. The reversal from the covering trend is worth watching — something changed in late Feb/early Mar.

### Pairing SI with Tasks 1-6 — The Complete Picture by Name

**OZK — Maximum Convergence (Bearish):**
- Equity: 0.53x up/down ratio (Task 2), volume spikes on bad news (Task 3)
- Dark pools: 42% off-exchange today vs 33% avg (Task 5), 80% short volume peak
- Options: 1.56x put/call OI, 1,647 contracts at May $40 (Task 6)
- Short interest: 15.28% of float, RISING, 12 days to cover (Task 7)
- **Every signal bearish. Highest conviction short in the group. Our puts are aligned with the market.**

**WAL — Vacuum Forming:**
- Equity: up/down recovered to 0.96x (Task 2), volume collapsed 93% (Task 5)
- Dark pools: 54% today — extreme spike, longs exiting hidden (Task 5)
- Options: $60 Jun put (1,744 OI) — crisis bet (Task 6)
- Short interest: 3.46%, DECLINING — shorts covering (Task 7)
- **Longs AND shorts both leaving. No one wants to hold. Catalyst will determine direction. Low squeeze risk (1.59 days to cover) but also less short fuel for downside.**

**KRE — Loaded Spring:**
- Equity: dying volume, AP redemption shrinking float (Tasks 1, 4)
- Dark pools: normal 29% (stable) — the action is in options/SI, not equity (Task 5)
- Options: 300K put contracts Apr 17, 61K at Jun $58, $68 strike = gravity well (Task 6)
- Short interest: 69.4M shares vs 56.9M outstanding, rising +64% (Task 7)
- **Structurally leveraged to both directions. Puts benefit from mechanics if $68 breaks. But squeeze risk is real — SI > shares outstanding is historically rare and dangerous.**

**EGBN — Quietly Loaded:**
- Dark pools: 46% today vs 33% avg (Task 5)
- Options: 11x P/C OI (inflated by $5 catastrophe bet), active put buying today (Task 6)
- Short interest: 11.1% of float, 9.45 days to cover, ticking back up (Task 7)
- **Second-most shorted name after OZK. Thin float amplifies everything. The $25P Jun is well-positioned.**

---

## FINAL SYNTHESIS (All 7 Tasks)

The market microstructure tells a complete story:

**WHO is positioned:** Institutions are exiting long positions through dark pools (Task 5) and ETF AP redemptions (Task 4). Shorts are concentrating into OZK and KRE (Task 7). Options market is loaded with puts (Task 6). No evidence of institutional accumulation on the buy side (Tasks 2, 3).

**HOW they're positioned:** Two-channel distribution — ETF structural (on-exchange AP redemption) + single-name tactical (off-exchange dark pool selling on rallies). Shorts using the ETF as the broad vehicle (KRE SI +64%) and OZK as the single-name conviction short (15.28% of float).

**WHEN they expect the move:** Options OI clusters around Apr 17 (earnings) and Jun 18 (Call Reports). Our Jun puts are aligned with the market's timeline.

**WHAT the rally actually is:** Short covering (WAL SI declined 22%) + thin-market mechanics (KRE shares -12.4%, volume dried up) + risk-on relief (Brent crash). Not institutional accumulation. The rally is mechanically rational but not informationally meaningful.

**Position implications:**
1. OZK Jun puts: HIGHEST CONVICTION. Every signal aligned. Hold.
2. WAL Jun $85P: Directionally correct but timing risk elevated. Short covering is done (SI at 3.46% — not much left to cover). Dark pool distribution ongoing. Revisit after earnings.
3. KRE puts: Mechanical upside from $68 gravity well and SI > shares outstanding. But squeeze risk is equally real. Hold with awareness.
4. EGBN $25P Jun: Well-positioned. Second-most shorted, thin float, dark pool distribution active.

---

---

## Data Tracking Files

Three TSV files in `workbook/` provide ongoing monitoring (one data type per file):

| File | Tracks | Source | Update Frequency |
|------|--------|--------|-----------------|
| `DARKPOOL.tsv` | Off-exchange volume as % of total | Chartexchange / FINRA OTC Transparency | Each session |
| `SHORT_VOL.tsv` | Daily short sale volume as % of total | FINRA Reg SHO daily files (cdn.finra.org) | Each session |
| `SHORT_INTEREST.tsv` | Outstanding short positions | Exchange reports / MarketBeat / Fintel | Twice monthly |

**Separation rationale:** Each data type answers a different question. Off-exchange % = where are trades happening? Short volume = what type of trade? Short interest = how big is the cumulative bet? Keeping them separate prevents confusion and means you only read the file relevant to your question.

---

## Sources
- yfinance (daily OHLCV, 400 days of history; options chains, OI, IV)
- SSGA KRE fund page (shares outstanding, NAV, AUM confirmed Apr 8)
- Nasdaq (KRE outflow detection articles)
- ETF.com ("biggest outflow in four years" headline)
- etfdb.com (flow summary data)
- stockanalysis.com (shares outstanding confirmation)
- chartexchange.com (off-exchange volume %, daily breakdowns for all thesis names)
- FINRA Reg SHO daily files: cdn.finra.org/equity/regsho/daily/CNMSshvol{YYYYMMDD}.txt
- FINRA OTC Transparency Data (short volume by venue, via chartexchange aggregation)
- Benzinga short interest reports (bi-monthly FINRA/exchange filings, 6+ month history)
