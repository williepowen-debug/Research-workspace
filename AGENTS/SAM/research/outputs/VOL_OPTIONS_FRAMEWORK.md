# SAM Vol/Options Monitoring Framework

**Created:** 2026-04-02 | **Source:** Perplexity deep research + SAM analysis
**Purpose:** Interpret vol surface and options positioning for yen-strength thesis confirmation

---

## TRAFFIC LIGHT DASHBOARD

| Dimension | GREEN (carry-calm) | YELLOW (early shift) | ORANGE (event being priced) | RED (stress/unwind) |
|-----------|-------------------|---------------------|---------------------------|-------------------|
| **JPY CVOL (JPVL)** | Sub-10, flat wings, UpVar ≈ DnVar | 10-12, wings starting to lift | 12-15, DnVar > UpVar, convexity ↑ | 18+, wings bid aggressively |
| **FXY P/C OI Ratio** | Near 52wk avg (~0.2+) | Below avg (~0.10-0.15) | Depressed (0.05-0.10), calls > avg, puts < avg | <0.05, call OI surging at $60-62 |
| **FXY Strike Map** | OI scattered, no clustering | Some call interest at $60 | Persistent OI build at $60-62, post-BOJ expiries | Concentrated, sticky, multi-day OI at $60-62+ |
| **USD/JPY RR (1-3mo)** | Positive, stable (calls > puts) | Compressing toward zero | Near zero to slightly negative | Cleanly negative (-0.3 to -0.7+) |
| **Vol Convergence** | 0 of 4 firing | 1 of 4 | 2-3 of 4 | All 4 aligned |

**CURRENT STATE (Apr 2, 2026): ALL GREEN — market complacent**

---

## 1. CME JPY CVOL (JPVL)

### What It Is
30-day forward implied vol index built from the entire strip of JPY/USD futures options. Uses "simple variance" method weighting all strikes evenly (cleaner than VIX-style). Prints as annualized standard deviation (9 = 9% annualized ≈ 0.6-0.7% daily moves at 1-sigma).

### Regime Interpretation
| CVOL Level | Regime | What It Means |
|------------|--------|---------------|
| Sub-10 | Carry grind | No imminent BOJ shock priced. Narrow daily ranges. |
| 10-13 | Moderate stress / event premium | Options being bid into known CB or macro dates. Out of complacency but not panic. |
| 15-20+ | Outright stress | Acute risk phase. Tail outcomes being priced. Comparable to 2008-09 dislocations. |

### Pattern Rules (MORE important than level)
- **Slow grind over 5-10 sessions** = genuine accumulation of protection/speculation → SIGNAL
- **One-day spike then mean-reversion** = headline scare → NOISE
- **Implied > realized** (CVOL rising but realized vol stays flat) = people overpaying for future risk → KILLER TELL that "yen crash hedge" meme is switching on

### CVOL Family — Decomposition
CME publishes sub-components:
- **UpVar:** OTM call-only (yen weakness convexity)
- **DnVar:** OTM put-only (yen strength convexity)
- **ATM vol**
- **Convexity indicator** (wings vs ATM)

**For our thesis, the signal configuration is:**
- Headline CVOL rising ✓
- DnVar rising FASTER than UpVar ✓ (put side = yen strength demand)
- Convexity expanding (wings bid > ATM) ✓

**The wrong kind of CVOL rise:**
- UpVar driving it while DnVar flat = market worried about MORE yen weakness (bad for us)

---

## 2. FXY Options — OI Structure

### Current Baseline (Apr 2, 2026)
- Put/call OI ratio: ~0.06-0.07 (calls dominate ~15:1)
- Total OI: ~70K contracts, mid-range of 52-week history (~50th percentile)
- Call OI: ABOVE 52-week average
- Put OI: BELOW 52-week average
- Recent 5-day: both slightly increased, call OI still much larger

### Interpretation
The low P/C ratio + call OI above average + put OI below average = **structural preference for upside yen exposure, not just put decay.** Someone is intentionally building yen-strength positions.

### What To Track
| Metric | Where | What Matters |
|--------|-------|-------------|
| P/C OI ratio vs 52wk avg | Barchart FXY | Ratio staying depressed from call buildup (not put decay) |
| Call OI vs 52wk avg | Barchart FXY | Above average = elevated positioning |
| Strike concentration | Barchart OI by strike | Clustering at $60-62 = institutional (target-based) |
| Expiry alignment | Barchart OI by expiry | OI in expiries bracketing BOJ meetings = event positioning |
| OI stickiness | Multi-day comparison | Sticky = conviction. Collapses after pops = flipping. |

### Signal Pattern (institutional yen-strength campaign)
- Concentrated call OI increases at $60-62
- Expiries bracket BOJ dates (not random month-end)
- Multi-day persistent build (sticky, not one-day spike)
- Correlated with rising CVOL and hawkish BOJ chatter
- P/C ratio remaining depressed or falling further

### Noise Pattern (retail/scattered)
- Scattered calls across many strikes/tenors
- Low follow-through in OI
- No expiry alignment with catalysts

---

## 3. USD/JPY 25-Delta Risk Reversals

### What It Is
RR = implied vol of 25-delta call MINUS implied vol of 25-delta put.
- **Positive:** calls richer → market pays more for yen weakness convexity
- **Negative:** puts richer → market pays more for yen strength crash protection

### Regime Interpretation
| RR Level | Regime | Meaning |
|----------|--------|---------|
| Positive, stable | Carry-calm | Topside USD/JPY convexity in demand. Normal. |
| Compressing toward zero | Transition | Put demand increasing. Market less sure carry is one-way. |
| Near zero | Inflection | Yen-strength and yen-weakness convexity equally valued. |
| Negative (-0.3 to -0.7+) | Stress/event | Downside USD/JPY insurance now more coveted than topside. |
| Deeply negative (-5 to -12) | Crisis | Extreme. Historical examples: JPY pairs hit -12 in 2007-09. |

### Tenor Structure
- **1W, 1M:** Highly sensitive to event risk (BOJ meetings, intervention windows). Noisy.
- **1-3M:** Where macro funds express "BOJ may hike" or "intervention risk" views. Our primary focus.
- **3M+:** Structural beliefs about the policy cycle distribution. Slower moving.

### For Our Thesis
Watch for progression: +0.5 → 0 → -0.3 → -0.7
- Movement anchored around BOJ dates, US CPI/Fed, or JGB stress headlines
- RR turning negative while SPOT hasn't broken down = "insurance bought ahead of hypothetical shock" (forward-looking, not backward-looking fear)
- RR vs realized skew divergence = most powerful signal

---

## 4. Convergence Signal — All Three Together

Any ONE moving = noise. All THREE moving = signal.

### "Yen Event Being Priced" Configuration
1. CVOL grinding from sub-10 toward 12-13 (slow, multi-session)
2. DnVar rising faster than UpVar (put-side demand)
3. FXY call OI building at $60-62, post-BOJ expiry alignment, P/C ratio depressed
4. USD/JPY 1-3M risk reversals compressing toward zero or negative

### What To Do When Convergence Fires
- **Highest conviction zone to hold/add FXY**
- Consider if Tranche 2 triggers should be relaxed
- Flag to PROME as cross-agent confirmation signal

### Key Check Dates
- **Apr 14-18:** Pre-BOJ April 23-24 meeting. CRITICAL window.
- **Apr 28-29:** Pre-BOJ May 1 meeting.
- **Any week with intervention headlines or JGB auction stress**

---

## DATA SOURCES

| Data | Source | Access | Limitation |
|------|--------|--------|-----------|
| **FXY ATM IV + 25d RR (PROXY)** | **`fxy_options.py` (yfinance FXY chain)** | **Free, auto-pulled → `FXY_OPTIONS.tsv` cols `ATM_IV_pct`, `RR25_USDJPY`** | **Proxy — see note below. This is now the PRIMARY live feed.** |
| JPY CVOL (JPVL) — true | CME Group market data page / EOD API | Gated (login + entitlement; undisclosed cost — recon 2026-05-28) | Not free-scriptable; CBOE JYVIX discontinued. Use only if Will pursues a CME login. |
| UpVar / DnVar | CME CVOL detail page | Gated | The FXY 25d-RR proxy approximates the DnVar>UpVar tell (put-side/yen-strength demand). |
| FXY options OI / P/C | `fxy_options.py` (yfinance) | Free, auto-pulled | — |
| USD/JPY RR (25d) — true OTC | Investing.com, broker platforms | Free/broker | Hard to get precise numbers without terminal; FXY proxy substitutes. |

---

## FXY-DERIVED VOL PROXY (implemented 2026-05-28 in `fxy_options.py`)

Computes two numbers per expiry from the FXY options chain we already pull, written to `FXY_OPTIONS.tsv`. The boot brief + STATUS surface the **~30-DTE** expiry as the headline.

- **ATM IV (CVOL proxy):** IV at the strike nearest spot, ×100. Roughly comparable scale to CME CVOL (both annualized vol) but runs a touch lower (FXY ETF vs simple-variance USD/JPY-futures strip). IV traffic-light bands in §1 are usable as a soft guide.
- **25d RR (USD/JPY convention):** BS-delta finds the ~25Δ OTM call/put on FXY; reported as `IV(FXY put) − IV(FXY call)`.

  ⚠️ **SIGN:** FXY moves *inversely* to USD/JPY, so a USD/JPY put ≈ an FXY call. A **negative** reported RR = FXY calls bid = yen-strength convexity demand = **thesis-side** (matches §3's "negative = puts richer" in USD/JPY terms).

  ⚠️ **SCALE:** FXY ETF skew runs *structurally much steeper* than OTC USD/JPY RR — the §3 absolute thresholds (−0.3/−0.7) **do NOT transfer**. The script only reads the **sign + trend vs its own history**, not the OTC-calibrated level. (First read 2026-05-28: ATM IV ~8% / RR ~−5.8 across liquid expiries — calm level, heavily thesis-side skew.)

**Limits:** proxy not identical to CVOL/OTC (American FXY options, ATM not full-strip); ATM IV robust, RR noisier (thin wings — script marks "thin wings" / degrades to n/a when the 25Δ strikes aren't cleanly available). Compare to own history, not to the old manual "10.44 / −1.5" reads.

---

*Reference doc — read at boot only if vol/options analysis is the task. Not part of standard boot sequence.*
