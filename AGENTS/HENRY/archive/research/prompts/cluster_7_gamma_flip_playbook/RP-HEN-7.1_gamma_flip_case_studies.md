# Research Prompt: "When Gamma Flips" — Historical Case Study Reconstruction

**Prompt ID:** RP-HEN-7.1
**Cluster:** 7 - Gamma Flip Playbook
**Priority:** HIGH
**Estimated Effort:** 2-3 hours
**Dependencies:** RP-HEN-6.1 (gamma mechanics understanding)

---

## Research Objective

Reconstruct the hour-by-hour and day-by-day sequence of historical gamma flip events to build an actionable playbook for recognizing and navigating the phase transition from positive to negative gamma regimes.

**Core Question:** When the market breaks through dealer support levels and gamma flips negative, what is the actual sequence of events, and what are the leading/coincident/lagging indicators at each stage?

---

## Historical Events to Analyze

### Primary Case Studies (Deep Dive)

**1. August 5, 2024 — Japan Carry Trade Unwind**
- Most relevant (0DTE era, current market structure)
- VIX spiked to 65 intraday
- 0DTE volume dropped 26%
- Started overnight in Japan, transmitted to US
- Questions to answer:
  - What time did US gamma flip negative?
  - What were GEX/DIX readings before, during, after?
  - How did Put Wall / Call Wall levels behave?
  - What was the intraday sequence (9:30am → 4pm)?
  - What stopped the cascade?

**2. February 5, 2018 — Volmageddon**
- XIV (inverse VIX) collapse
- VIX spiked from 17 to 50 in hours
- Reflexive loop: VIX rise → XIV rebalancing → more VIX buying → repeat
- Questions to answer:
  - How did equity gamma interact with VIX product gamma?
  - What was the timeline from "normal" to "crisis"?
  - Role of after-hours vs regular session
  - What levels broke and in what order?

**3. March 9-23, 2020 — COVID Crash**
- No 0DTE then, but gamma dynamics still present
- Multiple circuit breakers triggered
- Fed intervention sequence
- Questions to answer:
  - How did gamma evolve across multiple down days?
  - When did credit finally break (timeline vs equity)?
  - What was the dealer hedging pattern across the 2-week crash?
  - What marked the actual bottom (Fed announcement timing)?

### Secondary Case Studies (Lighter Analysis)

**4. December 2018 — Powell Pivot Selloff**
- Less severe but instructive
- Powell's "long way from neutral" → Christmas Eve low → pivot
- Useful for understanding Fed response timing

**5. January-February 2022 — Fed Tightening Selloff**
- Gamma dynamics in a slower grind
- Not a "flip" event but shows how positioning erodes

---

## Data Points to Collect for Each Event

### Pre-Event (T-5 days to T-1)
- [ ] VIX level and percentile
- [ ] VIX term structure (contango/backwardation)
- [ ] Net GEX estimate (if available)
- [ ] Put/Call ratio
- [ ] Credit spreads (HY OAS, IG OAS)
- [ ] MOVE index
- [ ] Key gamma levels (Put Wall, Call Wall, Gamma Flip)
- [ ] SPX distance from 200 DMA
- [ ] Any notable options positioning (large OI strikes)

### Event Day(s) — Hourly Reconstruction
- [ ] Overnight futures action (6pm-9:30am ET)
- [ ] Opening gap size and direction
- [ ] First hour price action (9:30-10:30am)
- [ ] Intraday GEX evolution (if data available)
- [ ] When did Put Wall break? Time and price.
- [ ] When did Gamma Flip level break?
- [ ] VIX intraday high and timing
- [ ] 0DTE volume vs normal (if applicable)
- [ ] Bid-ask spread behavior (liquidity withdrawal)
- [ ] Circuit breaker triggers (if any)
- [ ] Final hour dynamics (3-4pm)
- [ ] After-hours/overnight following

### Recovery Phase (T+1 to T+10)
- [ ] How long until gamma returned to positive?
- [ ] New support levels established
- [ ] Credit spread peak and timing vs equity bottom
- [ ] VIX decay pattern
- [ ] What catalyzed the turn? (Fed? Technical? Exhaustion?)

---

## Specific Questions to Answer

### Timing & Sequence
1. How much warning did leading indicators give before the flip?
2. Once Put Wall broke, how long until Gamma Flip level broke?
3. What's the typical duration from "flip" to "maximum stress"?
4. Does credit lead, lag, or move coincident with equity during flip?
5. What time of day do these events typically accelerate?

### Mechanics
6. How does 0DTE behavior change during a flip event?
7. Do dealers hedge more or less aggressively during crisis?
8. What happens to bid-ask spreads in SPX options during flip?
9. How does the VIX term structure behave (contango → backwardation timing)?
10. Are there predictable intraday patterns during multi-day events?

### Intervention & Recovery
11. What stops the cascade? (Fed, exhaustion, level, time?)
12. How long does negative gamma regime typically last?
13. What signals the "all clear" to return to positive gamma?
14. Does the first bounce hold, or is there typically a retest?

### Cross-Asset
15. How did Treasury vol (MOVE) behave relative to VIX?
16. Did USD strengthen or weaken during each event?
17. Any notable cross-asset correlations that broke down?

---

## Output Deliverables

### 1. Event Timeline Template
A standardized timeline showing:
- T-5d to T-0: Setup conditions
- T-0: Trigger and initial break
- Intraday sequence (hourly)
- T+1 to T+5: Aftershocks and recovery
- Key levels and when they broke

### 2. Leading Indicator Checklist
Ranked list of signals that preceded gamma flip events:
- How much lead time each provided
- False positive rate (how often signal fired without event)
- Current reading for each

### 3. "In The Moment" Decision Tree
When you see X, expect Y within Z timeframe:
- If Put Wall breaks → expect [outcome] within [time]
- If VIX >30 with backwardation → expect [outcome]
- If 0DTE volume drops >20% → expect [outcome]

### 4. Recovery Signal Checklist
What to watch for to know the flip is ending:
- VIX term structure normalization
- Credit spread stabilization
- Gamma returning to positive
- Volume/breadth signals

### 5. Comparison Table
Side-by-side of all events showing:
- Pre-event conditions
- Trigger type
- Duration
- Max drawdown
- Recovery time
- What stopped it

---

## Data Sources to Use

### Primary (Free/Accessible)
- CBOE VIX historical data (cboe.com)
- Yahoo Finance (hourly charts for SPX, VIX)
- FRED (credit spreads, MOVE)
- TradingView (intraday chart reconstruction)
- News archives (Bloomberg, Reuters, FT) for contemporaneous reporting

### Secondary (If Available)
- SpotGamma historical data or commentary
- SqueezeMetrics historical GEX
- Barchart historical gamma levels
- Academic papers on these events

### Media/Analysis
- SpotGamma blog posts from event dates
- Zero Hedge / Financial Twitter commentary (contemporaneous)
- Reddit r/options threads from event dates
- Sell-side research notes published during/after events

---

## Research Approach

### Phase 1: Data Collection (1 hour)
1. Pull daily data for each event (VIX, SPX, credit spreads)
2. Find contemporaneous news/analysis from each event
3. Locate any available gamma data from that period

### Phase 2: Timeline Reconstruction (1 hour)
1. Build hour-by-hour timeline for Aug 5, 2024
2. Build day-by-day timeline for Feb 2018 and March 2020
3. Note key levels and when they broke

### Phase 3: Pattern Extraction (30 min)
1. Identify common sequences across events
2. Note differences and why they might matter
3. Extract leading indicators that appeared in multiple events

### Phase 4: Playbook Synthesis (30 min)
1. Build the decision tree
2. Create the checklist
3. Write the "what to watch" summary

---

## Success Criteria

This research is successful if it produces:
1. A clear sequence of events for at least 2 major gamma flip events
2. Actionable leading indicators with approximate lead times
3. A decision tree usable in real-time during a potential flip
4. Specific levels/thresholds for current market (Feb 2026)

---

## Integration Points

**LIQUID:** Treasury auction stress → equity vol transmission
**SAM:** Japan overnight session as leading indicator
**CARL/LABOR:** Employment data releases as potential triggers
**REGINALD:** Bank stress → credit stress → equity transmission

---

*Prompt created: 2026-02-03*
*For execution by: Research agent or manual research*
