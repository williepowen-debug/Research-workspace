# TIMING THESIS — CHANGELOG

*How our view has evolved. Read this to understand not just what we believe, but why and when it changed.*

---

## 2026-03-31 — INITIAL THESIS CODIFIED

**Action:** First formal write-up of timing thesis.
**View:** Acceleration May-Jul, full cascade Q4, peak selling Q1-Q2 2027. 85% confidence.
**Basis:** 11 completed research pieces in FORGE/timing/ — 2007 OAS overlay, CCC/HY multi-episode analysis, Gorton framework (3 independent analyses), Z.1 selling sequence (4 analyses), Fed intervention response mapping, FABN sizing, PE-insurer transmission, zombie lending research.
**Key data points at time of writing:**
- HY OAS: 342 (= Jul 2, 2007)
- CCC OAS: 1013 (= Dec 2007)
- CCC/HY ratio: 2.96 (unprecedented — prior ATH was 2.83 pre-COVID)
- Brent: $108 (Hormuz closed, NOPI=47)
- Gas: $4.00 (behavioral breakpoint breached)
- PC defaults: 5.8% Fitch, 8% MS estimate
- Fund gates: 7+ active, $4.6B trapped
- Fed: No cuts priced, PCE hot
- Gorton staging: 3-4 of 6
- Z.1 position: Stage 1-2 (shadow blowups done, retail gating active)

**What preceded this:** Research built over ~1 week (Mar 23-30). RED Team assessment upgraded to 85% on Mar 20. Prior to codification, thesis existed informally across CONVERGENCE_TIMELINE.md and agent STATUS files but was never stated as a single coherent call.

---

## 2026-03-31 (PM) — CCC/HY RATIO DOWNGRADED AS SYSTEMIC INDICATOR

**Action:** Downgraded the CCC/HY ratio from "single most important finding" to "important but partially distorted signal." Adjusted interpretation of CCC OAS from systemic leading indicator to sector-concentrated stress with transmission risk.
**Previous view:** CCC at 1013bp = Dec 2007 equivalent. CCC/HY ratio of 2.96 unprecedented = "coiled spring" that compresses via violent HY widening. The junk end is 5-6 months ahead of the broad credit cycle.
**New view:** CCC at 1013bp is substantially driven by sector concentration — cable/media (~24-30% weight), PE-healthcare (~12-17%), software (~5-8%). Ex-software CCC OAS: ~930-960bp (still elevated). Ex-software AND ex-cable/media: ~650-780bp (stressed but not crisis-level). The 2015-16 energy sector blowout is a better analog for CCC specifically than 2007 GFC. The ratio is also inflated on the denominator side: broad HY is structurally higher quality than 2007 (BB now 58% vs 38%), compressing the 342bp reading.
**Trigger:** Three-source independent analysis (Perplexity, Claude, Gemini) of CCC index sector composition. All three converge on "concentrated, not systemic" for the CCC signal specifically.
**Evidence:**
- BondBloxx XCCC ETF holdings (Oct 2025): Communications 24.3%, Financial 17.4%, Healthcare 14.8%, Technology 7.6%
- Software is 3% of HY bonds vs 13-16% of leveraged loans vs 21% of private credit — the distress is a loan/PC story, not a bond story
- $32B of software loans below 80¢ distress threshold (33% of all distressed loans from 13% index weight)
- Cable/satellite (DISH, Altice, Clear Channel) contributes est. 430-600bp to CCC OAS — secular death spiral, not credit cycle
- PE-backed insurance brokers (~17% weight) trade at 500-750bp OAS — high leverage but NOT operationally impaired, dampening the index
- BB/IG spreads NOT confirming systemic risk: BBB OAS ~114bp, BB OAS ~189bp — benign
- Fitch forward default guidance: ~2% for broad HY (well below 4.5% long-term average)
- First-lien recovery rates collapsed to 37.7% vs 62.3% 25-year average (genuine broad red flag)
- 40% of ALL CCC borrowers have operating cash flow coverage below 1.0x (broad, not sector-specific)
**Confidence:** 85% → 80% on overall thesis. The CCC signal was one of six convergence pillars. Removing it as a systemic indicator weakens the "everything converging on May-July" argument but does NOT invalidate the other five pillars (Fed trapped, oil shock, Z.1 selling lags, PC gating/contagion, Hamilton demand destruction).
**Position impact:** No immediate changes. The thesis adjustment affects *interpretation* of one indicator, not the trade structure. The transmission channel thesis (BROCK 6-stage: concentrated stress → CLO mechanics → BDC redemptions → insurance re-rating → systemic) remains intact — we're betting on transmission, not on CCC as a standalone systemic signal.
**Key nuance preserved:** Even at ex-software 930-960bp, CCC is still meaningfully elevated. Recovery rates at 37.7% and 40% of CCC borrowers below 1.0x cash flow coverage are genuine broad stress signals. The sector-specific framing doesn't mean "nothing to see here" — it means the CCC OAS is overstating systemic risk by ~100-200bp, not that the risk is zero.
**Methodological note:** Gemini estimated software at 18-22% of CCC bonds (producing ex-software OAS of ~791bp). Perplexity and Claude both anchored to XCCC ETF holdings data showing 7.6% Technology. We weight Perplexity/Claude higher — they used the actual bond index proxy. Gemini appears to conflate loan market exposure with bond index composition.
**Files added:** `research/CCC_SECTOR_DECOMPOSITION_PERPLEXITY.md`, `research/CCC_SECTOR_DECOMPOSITION_CLAUDE.md`, `research/CCC_SECTOR_DECOMPOSITION_GEMINI.md`

---

## 2026-03-31 (Late PM) — TREASURY SELLER ESTIMATES CORRECTED: NON-BASIS SELLERS OVERSTATED ~3x

**Action:** Downgraded four of five simultaneous seller classes. Reframed Treasury dislocation thesis from "aggregate volume overwhelms dealers" to "basis trade single-point-of-failure + selling speed vs. buying speed mismatch."

**Previous view:** Five seller classes could simultaneously liquidate $107-330B/quarter in Treasuries in Q2-Q3 2026, overwhelming dealer intermediation capacity ($65-85B net positions). Non-basis sellers (PC funds, PE insurers, Japan life, China/Gulf) collectively contribute $57-130B/quarter. Market clears at 5.00-5.25% 10Y through severe nonlinear illiquidity.

**New view:** Non-basis sellers are overstated ~3x. Revised aggregate: **$60-245B/quarter stress, $10-45B/quarter base** (from $107-330B). Four of five classes corrected downward, one (Gulf) reversed from seller to buyer. The basis trade ($50-200B) remains the dominant — and essentially the only — acute systemic risk. The thesis now rests on: (1) basis trade as single-point-of-failure, (2) the speed mismatch between forced selling (days) and buyer deployment (weeks-to-months), and (3) the Duffie et al. nonlinearity in dealer capacity utilization. Market clearing price (~5% 10Y) and the nonlinear mechanism both survive.

**Trigger:** Three-source analysis of Prompt 2A (Simultaneous Sellers). Perplexity deep research delivered the decisive empirical audit against primary regulatory filings (NAIC, TIC, MOF, Form PF, 10-Qs). Gemini deep research provided the framework and price impact models. Perplexity without deep research provided the initial nonlinearity insight.

**Evidence — seller corrections:**
- **PE-controlled insurers ($10-30B → $0-3B):** NAIC Capital Markets Bureau Special Report (Aug 2025): all 137 PE-owned US insurers hold only **$14.1B total in Treasuries** (3% of bonds, ~2% of total assets). They systematically underweight govt securities (3% vs 7% industry-wide) and overweight ABS (31% vs 13%). Chicago Fed WP 2025-09 confirms they've been moving FROM liquid TO illiquid (+7.7pp private placements 2017-24). Apollo/Athene: 11bps avg annual credit losses. Fitch: neutral outlook, no broad rating pressure expected. The mechanism we described runs backwards from documented behavior.
- **Private credit funds ($15-25B → $2-5B):** Goldman "$45-70B outflows" is over TWO years, not annual (~$5.6-8.75B/qtr total, not Treasury-specific). BDCs (bulk of retail PC, $222B AUM) must invest ≥70% in nonpublic companies. BCRED: only ~15-17% in liquid/Treasury-equivalent holdings. Redemptions met through gating (5% caps), credit facility draws, secondary loan sales. PitchBook: $25B distressed software loans trading <80¢ — managers sell loans first. OFR Brief 26-02: Form PF doesn't include "private credit" as strategy category — Treasury-specific data extraction impossible. Critical data gap persists.
- **Gulf sovereigns (net seller → NET BUYER):** TIC data: SA $132.0B→$149.5B (+$17.5B), UAE $64.0B→$95.6B (+$31.6B), Kuwait $46.4B→$66.1B (+$19.7B). Combined Gulf: **+$46.3B in 2025 (+$11.6B/qtr)**. Nasser Saidi & Associates (Jan 2025) confirms accumulation. "Petrodollar recycling broken" narrative NOT supported by holding data.
- **Japan life insurers ($12-30B → $3-12B):** Observed selling pace: ¥756B (~$5B) in 6 months ending Mar 2025 = ~$2.5B/qtr (MOF data). Japan OVERALL was net buyer: TIC holdings $1,061.5B→$1,185.5B (+$124B in 2025). Banks/GPIF/pensions more than offset life insurer sales. Setser (CFR): "best bet is Japan will continue to be modest net buyer." Hedge ratio/return data confirmed but selling velocity overstated.
- **China ($20-45B combined → $5-25B China alone):** 8-quarter average: -$14.3B/qtr (peak -$34B Q2 2025). Setser notes custody shift to Belgium (Euroclear)/Luxembourg — actual divestment likely less than China TIC line suggests. Belgium TIC +$162.9B over 2 years.
- **Basis trade ($50-200B):** Fully validated. $1T+ confirmed (BIS, CFTC, FEDS Notes). March 2020 precedent: >$200B sold. BUT: practical leverage more like 10-20x than 50-100x (TBAC assumed 20x, Resonanz analysis 15x). April 2025 partial test showed SRF + term repo prevented March 2020 replay. eSLR reform frees ~$213B capital.

**Evidence — price impact (new synthesis from three sources):**
- Normal/gradual: 3-10bps per $100B (Somogyi et al. 2025)
- Moderate stress: 10-40bps per $100B (April 2025 implied; Bräuning-Stein ~30% amplification)
- Severe stress/dysfunction: 50-125+bps per $100B (March 2020 realized; NBER WP 30476 SVAR)
- Key finding: auction demand elasticity collapsed **5x since 2010** (Somogyi et al. HBS WP 26-033). 1% supply increase: 2bps pre-2010 → 9bps post-2010. ~3.2bps per $100B vs 0.7bps.
- Duffie et al. nonlinearity confirmed: dealer utilization 40%→80% triggers discontinuous illiquidity jump. 96% utilization = 5.4 SD (March 2020 peak).

**Evidence — buyer step-in (~5% 10Y confirmed from multiple angles):**
- Pensions: $60-130B capacity at 5%+ (107.1% funded ratio, discount rate 5.34-5.43%). October 2023 evidence: Florida SBA, NYC Pensions, Boeing all moved at ~5%.
- Banks: $4,674B in UST/agencies (Jan 2026). Step-in requires 50-100bps spread over SOFR. eSLR lowers threshold 10-15bps.
- SWFs: $100-190B deployable (GPFG 3.4pp underweight, GIC $40-80B capacity, ADIA ~$42B).
- Insurance: $50-100B marginal capacity (1-2pp shift from corporate credit).
- Retail: activated at 5% but concentrates in short end (T-bills/MMFs), not duration.
- **Critical gap: buyer deployment speed is weeks-to-months. Selling speed is days.**

**Confidence:** 80% → 75% on overall thesis. The reduction reflects: (a) non-basis seller classes providing less fuel than modeled, (b) April 2025 showing post-2020 infrastructure (SRF, term repo) meaningfully reducing forced-unwind probability, (c) Gulf being a buyer rather than seller. The 5pp reduction is partially offset by the strong empirical validation of the nonlinear mechanism and the speed mismatch insight.

**Position impact:** No immediate changes. The trade structure targets credit cascade → equity repricing, not Treasury yields directly. However, the weaker-than-expected selling pressure reduces the probability of a Treasury-market-triggered cascade, making it more likely that the credit cascade originates from the private credit/CLO/insurance channel (BROCK domain) rather than from Treasury market dysfunction (LIQUID domain). This strengthens the case for maintaining BROCK-linked positions (APO, ARES shorts) relative to pure Treasury-market positions.

**What survives intact:**
- Basis trade as dominant systemic risk
- Duffie et al. nonlinearity in dealer capacity
- 5% 10Y as market clearing level
- Selling speed vs. buying speed mismatch
- Convenience yield collapse (5x elasticity deterioration)
- eSLR as key policy variable

**What's weakened:**
- "Five simultaneous sellers overwhelm dealer capacity" narrative — it's really "one seller (basis trade) + one structural seller (China) + speed mismatch"
- PE-insurer Treasury liquidation mechanism — they don't hold enough to matter
- Gulf demand withdrawal — reversed, they're buying
- Aggregate volume as the stress variable — it's about concentration and speed, not total dollars

**Files added:** `research/SIMULTANEOUS_SELLERS_RESPONSE_2A_PERPLEXITY.md`, `research/SIMULTANEOUS_SELLERS_RESPONSE_2A_GEMINI.md`, `research/SIMULTANEOUS_SELLERS_RESPONSE_2A_PERPLEXITY_DEEP.md`

---

<!-- TEMPLATE FOR FUTURE ENTRIES

## YYYY-MM-DD — [TITLE: what changed]

**Action:** [Upgraded/Downgraded/Adjusted/Confirmed] [specific element]
**Previous view:** [what we believed before]
**New view:** [what we believe now]
**Trigger:** [what data/event caused the change]
**Evidence:** [specific data points, sources]
**Confidence:** [X% → Y%]
**Position impact:** [any changes to sizing, expiries, or rolls]

-->
