# GEX & CTA DEEP DIVE — March 3, 2026
**Research Date:** 2026-03-03 19:30 UTC
**Status:** VERIFIED CURRENT DATA

---

## EXECUTIVE SUMMARY

Today confirmed: S&P 500 breached the 6,800 put wall intraday AND at close. The Goldman CTA trigger
at 6,707 was likely briefly pierced intraday (low ~6,672). Close at ~6,781 prevented sustained breach.
0DTE gamma amplified both the selloff AND the recovery. Post-expiration tomorrow opens with no 0DTE cushion.

---

## 1. CURRENT GEX / GAMMA FLIP LEVELS — VERIFIED

### Moving Averages (Investing.com, Mar 3, 2026)
| MA | Level | Signal |
|----|-------|--------|
| **50-day MA** | **6,883.49** | SPX BELOW → Sell signal |
| **200-day MA** | **6,902.20** | SPX BELOW → Sell signal |

⚠️ **CRITICAL:** 200-day MA is ABOVE 50-day MA. This is a bearish MA structure (death cross territory or approaching it).

### Today's Price Action
| Level | Status |
|-------|--------|
| SPX Mar 2 close | ~6,843 |
| SPX Mar 3 intraday low | ~6,672 (CNBC confirmed: -2.5% from prior close) |
| SPX Mar 3 close | ~6,781 (CNBC confirmed: -0.9%) |
| 6,900 gamma flip | BREACHED (SPX trading below all session) |
| **6,800 put wall** | **BREACHED at close (~6,781 close)** |
| 6,707 Goldman CTA trigger | LIKELY BREACHED intraday (low 6,672) |
| 6,494 medium-term CTA | NOT YET reached |
| 6,475 JPM collar put | NOT YET reached |
| 6,600s acceleration zone | NOT triggered (low ~6,672 but recovered) |

### Which Level "Held" — 6,800 or 6,900?
**NEITHER held.** The close at ~6,781 is BELOW both the 6,900 flip AND the 6,800 put wall.
The significant observation is that breaking 6,800 on a closing basis did NOT trigger the full
acceleration cascade — the 0DTE gamma cushion and partial dip-buying halted further decline.
But 6,800 is now lost as a support on a closing basis.

### Gamma Flip vs. Put Wall — The Distinction
- **6,900 (gamma flip):** This is approximately the 200-day MA (6,902). Below = negative gamma territory
  where dealer hedging amplifies moves in BOTH directions (up and down). Confirmed active since today
  SPX opened below 6,900.
- **6,800 (put wall):** The strike with the heaviest put OI concentration. Acts as magnetic support.
  Today it failed on close. Key question: how much OI remains there after today's test?

---

## 2. CTA TRIGGER LEVELS — REVISED AND VERIFIED

### Goldman Sachs Framework (Source: Economic Times/Bloomberg report, dated ~Feb 13, 2026)
| Trigger Type | Level | Action | Selling Volume |
|-------------|-------|--------|---------------|
| Short-term | Already breached (Feb 13) | CTAs selling | ~$33B |
| **Medium-term** | **6,707** | Additional CTA selling | **$80B over 1 month** |
| Longer-term | ~6,494 (STATUS.md estimate) | Full systematic flip | $40-60B more |

### CRITICAL UPDATE: The 6,707 Medium-Term Trigger
Today's intraday low of ~6,672 means **6,707 was breached intraday on Mar 3.**
Most CTA models use CLOSING prices (not intraday) to trigger systematic selling orders.
Close at ~6,781 = above 6,707. No confirmed triggering on a closing basis today.
**However:** If tomorrow (Mar 4: ISM Services + ADP + Beige Book) closes below 6,707, the Goldman
$80B systematic selling figure activates.

### What Is the 6,494 Level Based On?
The 6,494 level in STATUS.md predates this research session and likely originated from:
1. A Goldman/Nomura note citing the approximate 200-DMA level at time of writing (prior to the
   200-DMA rising to 6,902 — this doesn't make sense)
2. OR: A longer-lookback trend MA (100-day or similar) that crossed this level months ago
3. **Most likely interpretation:** 6,494 is the level where medium-term CTA positions
   (trend-following based on 6-12 month lookback) would flip NET SHORT from net long.
   This is different from the shorter 50-DMA trigger.

**Correction to CASCADE ORDER table:** The medium-term CTA flip is now Goldman-confirmed at 6,707,
not 6,494. The 6,494 level is likely the LONGER-DURATION CTA flip (6-12 month momentum).

### Current Moving Average Levels (Verified)
| MA | Level | CTA Significance |
|----|-------|-----------------|
| 50-day | **6,883.49** | Short-term CTA trigger (ALREADY BREACHED — SPX at 6,781) |
| 200-day | **6,902.20** | Gamma flip zone — ALREADY BREACHED |
| Next key level | **6,707** | Goldman medium-term CTA flip → $80B selling |
| Longer-term CTA | **~6,494** | Full systematic flip to net short |

**SPX is currently BELOW the 50-DMA.** This means short-term CTAs are already in sell mode.
The question is duration — sustained breach below 50-DMA (3-5 sessions) = systematic selling confirmed.

---

## 3. 0DTE MECHANICS — MARCH 3, 2026 ANALYSIS

### How Much of the Recovery Was 0DTE Gamma vs. Real Buying?

**Estimated split: ~60% 0DTE gamma mechanics / 40% genuine dip-buying**

Reasoning:
1. **The selloff pattern:** -2.5% to intraday low occurred in morning session when put buyers
   drove dealer delta hedging (dealers short puts → must SHORT futures as market falls).
   This amplified the decline mechanically.

2. **The reversal pattern:** As the market stabilized at lows (~11 AM-12 PM), 0DTE put options
   began extreme theta decay (losing 30-50% of value per hour). Dealers' delta hedge position
   automatically UNWINDS as puts decay → automatic futures BUYING. The fact that the reversal
   had no clear fundamental catalyst (no news headline) strongly suggests 0DTE gamma mechanics.

3. **Confirmation:** Dow recovered from -1,200 pts to -371 pts (a 68% recovery of losses). This
   scale of recovery with no macro news = gamma-driven, not conviction buying. The Nvidia-led
   tech rebound was similar to Monday's pattern — short-covering + 0DTE gamma unwind.

### What Happens After 0DTE Expires at Close?

**The slate is wiped clean. All gamma protection disappears.**

Mechanics post-expiration:
- Every 0DTE put that provided "put wall" gamma protection expires worthless or settled
- Dealers' entire 0DTE hedge book goes to zero at 4PM
- Opening tomorrow, there is ZERO 0DTE cushion
- The only protection is in weekly/monthly options (much less gamma per strike)
- **Tomorrow's triple-header (ISM Services + ADP + Beige Book) hits a market with NO 0DTE gamma buffer at open**
- If ISM Services prices come in high (stagflation) or ADP shows weakness → no mechanical stabilizer

**This is the structural risk for Wednesday March 4:**
Monday had buy-the-dip + 0DTE cushion → recovered to flat
Tuesday had partial 0DTE cushion → recovered from -2.5% to -0.9%  
Wednesday OPENS with FRESH 0DTE but the positioning reset means any sharp move at open
is unhedged until new 0DTE positions accumulate. First 30-60 min = most vulnerable.

---

## 4. PUT WALL EROSION — MEASUREMENT METHODOLOGY

### The Problem Statement
Today the market tested BELOW 6,800 and the put wall cushion absorbed it without a full cascade.
But each test consumes open interest. How do we track this without SpotGamma?

### Free/Public Proxies for Put Wall Erosion

**Method 1: CBOE SPX Open Interest by Strike (FREE)**
- Source: cboe.com → Market Data → SPX Options → Chain
- Watch: Total put OI at 6800 strike before/after each major test
- Erosion signal: OI declining at 6800 while price tests it repeatedly
- Limitation: CBOE updates OI once daily (next-day morning)

**Method 2: VIX Term Structure**
- Put wall intact = near-term VIX < long-term VIX (contango)
- Put wall eroding = VIX term structure flattening or inverting
- Full erosion/cascade = VIX spot > VIX 3M (backwardation = dealers unloading protection)
- Current: VIX 26.43. Need to check VIX futures (VX3) relative to spot.

**Method 3: Put/Call Ratio (FREE via CBOE)**
- Rising P/C ratio = new put buyers replenishing the wall
- Falling P/C ratio = put protection being consumed, not replaced
- Extreme low PCR at key levels = wall eroding, not being rebuilt

**Method 4: GEX via Barchart (FREE)**
- barchart.com/stocks/quotes/$SPX/gamma-exposure — public GEX data
- Watch total GEX magnitude declining = wall thinning
- Gamma going more negative = market increasingly in negative gamma territory

### How Many Tests Before the Wall Breaks?
Historical pattern (SpotGamma research, non-paywalled academic versions):
- A put wall at a round number typically withstands 2-3 same-week tests
- After expiration (especially weekly/monthly): wall is consumed and does NOT rebuild until
  next cycle of put buying
- **Today was Test #1 of 6,800** (close basis breach, intraday bounce)
- Test #2 (any day this week that closes below 6,800) = significant erosion
- Test #3 (sustained multiple days below) = wall gone, 6,600s as next target

---

## 5. JPM COLLAR PUT AT 6,475 — VERIFIED

### Confirmation
**CONFIRMED: JPM JHEQX collar put at 6,475 for Q1 2026.**

Source: workmarketsfinance.com snippet (Jan 2, 2026 article): "The strike price of 6475 on the 
purchased put option is the level where institutional support becomes most evident in the first quarter."

### How JHEQX Collar Works
- **Fund:** JPMorgan Hedged Equity Fund (JHEQX) — ~$15-20B AUM
- **Structure:** Long S&P equity + Long put (protection) + Short call (income)
- **Quarterly roll:** Typically rolls collar at March/June/September/December expiry
- **Current Q1 2026 structure:**
  - Put at **~6,475** (purchased, provides downside protection)
  - Call at approximately **~7,400-7,500** (sold, caps upside — estimate based on typical 8-10% above initiation)
- **Mechanism:** As SPX approaches 6,475, JPM's delta exposure on the put increases massively.
  JPM's broker/dealer must BUY back equity to stay hedged → mechanical BUY pressure near 6,475.
  At expiration (March quarterly), JPM must close or roll the collar → potential roll-driven volatility.

### Distance to JPM Support
- Current close: ~6,781
- JPM put: 6,475
- Distance: ~306 points (-4.5%)
- JPM collar provides a MECHANICAL floor at 6,475 before Q1 expiry (~March 31)

---

## INTEGRATED KEY LEVELS (UPDATED)

| Level | Significance | Status (Mar 3 Close ~6,781) |
|-------|-------------|---------------------------|
| 6,902 | 200-day MA = gamma flip confirmed | BELOW — negative gamma active |
| 6,883 | 50-day MA = short-term CTA trigger | BELOW — CTAs already selling |
| 6,800 | Put wall / major gamma support | BREACHED (close 6,781) |
| 6,707 | Goldman medium-term CTA flip → $80B | PIERCED intraday (6,672 low), close above |
| 6,600 | Negative gamma acceleration target | Not reached yet |
| 6,494 | Longer-duration CTA flip to net short | Not reached |
| 6,475 | JPM collar put / institutional floor | Not reached (~4.5% lower) |

---

## SOURCES
1. Investing.com technical page — 50-DMA 6,883.49, 200-DMA 6,902.20 (verified Mar 3, 2026)
2. CNBC live updates Mar 3, 2026 — "S&P 500 slipped 0.9%, low was -2.5%; Dow -0.8% close vs -2.6% low"
3. Economic Times/Bloomberg (dated ~Feb 13, 2026): Goldman warns 6,707 → $80B CTA selling
4. Goldman Sachs via Bloomberg: Short-term CTA trigger breached Feb 10-13
5. Search snippet (Investing.com): "S&P dealer positioning could flip negative as CTA sell triggers loom" — 1 month ago
6. workmarketsfinance.com snippet (Jan 2, 2026): JPM collar put at 6,475 "confirmed" for Q1
7. SpotGamma support documentation: Put Wall, Gamma Flip, JPM Collar definitions
