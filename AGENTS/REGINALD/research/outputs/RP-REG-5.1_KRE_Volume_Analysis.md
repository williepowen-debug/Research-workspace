# RP-REG-5.1: KRE & Regional Bank Volume Deep-Dive
**Date:** 2026-04-09 | **Status:** Tasks 1-4 complete, Tasks 5-7 pending

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

## Remaining Tasks (for next session)

5. **Dark pool / off-exchange %** — What share of volume is going through dark pools? Rising dark pool % during rally = hidden distribution.
6. **Options volume vs equity volume** — Are views being expressed through derivatives instead of shares?
7. **Short interest trend overlay** — SI changes paired with volume patterns.

---

## Sources
- yfinance (daily OHLCV, 400 days of history)
- SSGA KRE fund page (shares outstanding, NAV, AUM confirmed Apr 8)
- Nasdaq (KRE outflow detection articles)
- ETF.com ("biggest outflow in four years" headline)
- etfdb.com (flow summary data)
- stockanalysis.com (shares outstanding confirmation)
