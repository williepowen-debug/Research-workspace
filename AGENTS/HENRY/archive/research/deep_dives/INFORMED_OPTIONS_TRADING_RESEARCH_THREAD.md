# Informed Options Trading Research Thread

**Created:** April 5, 2026  
**Purpose:** Academic foundation for detecting informed flow in WAL/OZK options  
**Related Agents:** HENRY (market structure), REGINALD (WAL/OZK positions), RED (signal detection)  
**Priority:** Tier 1 — Directly applicable to current positioning

---

## Executive Summary

These papers provide the empirical foundation for detecting informed trading in options markets before corporate events. The core thesis: **options markets lead equity markets when information is complex, requires analytical work, or when CDS markets are inaccessible.** This validates monitoring WAL/OZK put flow for signs of informed participants arriving at similar CRE stress conclusions.

---

## Tier 1 — Read First (Directly Applicable)

### 1. Augustin, Brenner & Subrahmanyam (2019)
**"Informed Options Trading Prior to M&A Announcements: Insider Trading?"**  
*Management Science*

**Key Contribution:** Most rigorous study of how informed trading shows up in options before corporate events.

**Methodology:**
- Isolate abnormal options activity relative to baseline
- Test whether it predicts subsequent stock moves
- Transferable to monitoring WAL/OZK for informed participant arrival

**Application:** Use same methodology to track unusual put volume/open interest in WAL/OZK as earnings approach (Apr 16/21).

**Status:** ⏳ Not yet read  
**Priority:** 🔴 Critical

---

### 2. Augustin & Subrahmanyam (2020)
**"Informed Options Trading Before Corporate Events"**  
*Annual Review of Financial Economics*

**Key Contribution:** Comprehensive survey tying together 20 years of research. Literature review that saves reading 30 individual papers.

**Coverage:** Full chain from theory to empirics.

**Application:** Establish baseline understanding of how informed flow manifests across different event types (earnings, M&A, distress).

**Status:** ⏳ Not yet read  
**Priority:** 🔴 Critical

---

### 3. Bogousslavsky, Fos & Muravyev (2024)
**"Informed Trading Intensity"**  
*Journal of Finance*

**Key Contribution:** Most recent high-impact paper. Develops measure of *how much* informed trading is happening (not just *whether*).

**Innovation:** Quantitative intensity metric vs. binary detection.

**Application:** Could build continuous "informed flow intensity" score for WAL/OZK options. Track elevation as earnings approach.

**Status:** ⏳ Not yet read  
**Priority:** 🔴 Critical

---

### 4. Pereira da Silva & Vieira (2022)
**"Informed trading in the CDS and OTM put option markets"**  
*Review of International Economics*

**Key Contribution:** Investigates how informed traders straddle CDS and options markets.

**Critical Finding:** When CDS market is relatively illiquid, informed investors trade in **OTM put options instead**.

**Application:** **Directly validates your venue choice.**
- CDS on regional banks is thin/inaccessible to retail
- Put option market is exactly where informed flow should concentrate
- Your WAL/OZK put positions align with informed trader venue selection

**Status:** ⏳ Not yet read  
**Priority:** 🔴 Critical — validates thesis

---

### 5. Chen & Lu (2017)
**"Slow Diffusion of Information and Price Momentum in Stocks: Evidence from Options Markets"**  
*Journal of Banking & Finance*

**Key Contribution:** Documents that information embedded in options prices diffuses slowly into stock prices.

**Mechanism:** Options lead stocks when information is complex or requires analytical work to uncover.

**Application:** **Directly applies to your FFIEC forensics.**
- Your CRE analysis is precisely "complex, non-obvious information"
- Should see options lead stocks as market slowly digests implications
- Explains why you can be early — information diffusion lag

**Status:** ⏳ Not yet read  
**Priority:** 🔴 Critical — explains timing advantage

---

### 6. Weinbaum, Fodor, Muravyev & Cremers (2023)
**"Option Trading Activity, News Releases, and Stock Return Predictability"**  
*Management Science*

**Key Contribution:** Links option trading activity directly to specific news events.

**Metric:** Measures how far in advance options market prices the information.

**Application:** Framework for timing around OZK (Apr 16) and WAL (Apr 21) earnings releases.
- How many days in advance does informed flow typically appear?
- What volume thresholds signal high conviction?

**Status:** ⏳ Not yet read  
**Priority:** 🟠 High — earnings timing

---

## Research Questions to Answer

### For WAL/OZK Specifically
1. What is the normal baseline of put volume/open interest in WAL/OZK?
2. How much deviation from baseline constitutes "abnormal" activity?
3. How many days before earnings does informed flow typically peak?
4. Does OTM put skew (difference between OTM and ATM implied vol) predict stock moves?

### For Broader Application
5. Can we build a real-time "informed trading intensity" metric?
6. What is the lag structure between options signal and stock price response?
7. How does retail vs. institutional flow differ in signatures?

---

## Methodology to Adapt

### Step 1: Establish Baseline
- Calculate historical average daily put volume for WAL/OZK
- Account for earnings seasonality (volume typically rises before earnings)
- Establish "expected" vs. "abnormal" thresholds

### Step 2: Monitor Abnormal Activity
- Track deviations >2σ from baseline
- Focus on OTM puts (90-95 delta) — where informed flow concentrates per Silva & Vieira
- Watch for volume without corresponding stock volume (options-specific signal)

### Step 3: Correlate with Events
- OZK earnings: Apr 16, 2026
- WAL earnings: Apr 21, 2026
- TIC data release: Apr 15, 2026
- BOJ meeting: Apr 23-24, 2026

### Step 4: Validate Predictive Power
- Did abnormal put flow before past earnings predict stock moves?
- Cross-validate with actual post-earnings price action

---

## Files / Cross-References

- Related: `AGENTS/HENRY/` (market structure, options flow analysis)
- Related: `AGENTS/REGINALD/trade/WAL/` and `/OZK/` (position-specific analysis)
- Related: `AGENTS/RED/` (adversarial detection of informed flow)
- Related: `MEMORY.md` (options flow as leading indicator)

---

## Next Steps

1. **Acquire papers** — Download from academic sources (Sci-Hub, SSRN, institutional access)
2. **Read order:** Start with Augustin & Subrahmanyam (2020) survey → Silva & Vieira (2022) → Chen & Lu (2017)
3. **Build baseline** — HENRY to calculate historical WAL/OZK put volume baselines
4. **Monitor flow** — Set up alerts for abnormal OTM put activity in WAL/OZK
5. **Test thesis** — Document whether pre-earnings put flow predicts post-earnings moves

---

*Created: April 5, 2026*  
*Source: User research thread — academic foundation for informed options flow detection*
