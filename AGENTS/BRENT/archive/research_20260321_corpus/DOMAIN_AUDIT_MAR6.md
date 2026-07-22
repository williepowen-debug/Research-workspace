# BRENT DOMAIN AUDIT — March 6, 2026

**Written by:** BRENT agent (self-audit)
**Date:** 2026-03-06 ~20:30 UTC
**Purpose:** Honest pre-Monday gap analysis. Find every weakness before first real check-in.

---

## 1. COMPLETENESS CHECK — What I Own vs What I Have

### Per CLAUDE.md — Full Ownership List vs Coverage Status

| Domain Area | Per CLAUDE.md | Have Data? | Quality |
|-------------|--------------|------------|---------|
| Brent/WTI spot prices | ✅ Own | ✅ Yes | GOOD — $88.59 Mar 5 close [CONF], $90+ intraday [CONF] |
| Term structure (contango/backwardation) | ✅ Own | ⚠️ Partial | "Strong backwardation ~$10-15/bbl M1-M12" [CONF Rigzone Mar 2] — but M1-M3 exact level still [EST]. REFERENCE_TABLES.md flags this as next pull. |
| Crack spreads (3-2-1, gasoline, distillate, jet) | ✅ Own | ⚠️ Partial | 3-2-1 Gulf $28.91/bbl [CONF]. Distillate "more elevated" [CONF] but no exact spread. Jet crack: **MISSING**. Gasoline crack standalone: **MISSING**. Only 3-2-1 composite confirmed. |
| OPEC+ policy, compliance, spare capacity | ✅ Own | ⚠️ Thin | Pre-war 140M barrel flush [CONF HAWK]. Spare capacity 5-6M bpd [EST]. **Current quotas: explicitly flagged as NEED TO PULL in REFERENCE_TABLES.md.** No compliance data by member. |
| Gulf production levels | ✅ Own | ⚠️ Partial | Storage runways known. Actual bpd per country: **MISSING**. Kuwait/Qatar/UAE/Iraq production figures not in any workbook. |
| Global storage (Cushing, SPR, OECD, floating) | ✅ Own | ⚠️ Partial | Cushing change: +1.564M bbl wk Feb 27 [CONF EIA]. Absolute level: ~24-26M bbl [EST] — above 20M minimum but estimated. SPR ~350M bbl [CONF] but stale (2022 baseline). Floating storage: **MISSING entirely.** OECD commercial: **MISSING.** |
| Tanker markets (VLCC, Suezmax, Aframax, war risk) | ✅ Own | ✅ Good on VLCC | VLCC WS400+ [CONF]. Suezmax rates: **MISSING.** Aframax rates: **MISSING.** War risk premium: qualitative only ("spiking, insurers pulled"). No number. |
| US production + rig counts + shale breakevens | ✅ Own | ✅ Good | Dec 2025 13.7M bpd [CONF Bloomberg]. EIA 2026 forecast 13.5M [CONF]. DUC inventory: qualitative "depleted" [CONF EIA] but no specific count. Rig count current: **NOT IN STATUS.md** — only "no response yet." |
| Demand indicators (gasoline demand, jet, distillate, refinery util) | ✅ Own | ❌ Thin | Gasoline inventories change: -1.704M bbl [CONF EIA wk Feb 27]. **Implied demand figure: missing.** Refinery utilization: **missing.** Jet fuel data: **missing.** Distillate inventories change only, no demand. |
| Energy credit (HY energy OAS, E&P debt stress) | ✅ Own | ❌ Very thin | Status says "🟡 2, not yet stressed." No actual OAS number anywhere in workbook. No E&P-specific spread. Just assessment: "stable." |
| Refinery operations (turnaround schedules, utilization) | ✅ Own | ❌ Missing | Not in STATUS.md, workbook, or domain files. Zero data. |
| Two-phase thesis | ✅ Own | ✅ Strong | Well-developed. Phase timing logic present. |
| Positions (USO, STNG, options) | ✅ Own | ✅ Good | Positions logged. P/L tracked. USO price [EST], STNG [CONF]. |
| US-listed beneficiaries research | ✅ Own | ✅ Complete | HIGH_OIL_BENEFICIARIES.md is thorough — full report exists. |

### Summary of Completeness Gaps
**Critical missing:**
1. Current Baker Hughes rig count (number, not just "no response")
2. Actual bpd by Gulf country (Kuwait, UAE, Iraq, Qatar)
3. Jet crack spread (airline exposure — relevant to AAL position if held)
4. Gasoline crack standalone (pump price accuracy)
5. OECD commercial storage and floating storage
6. Refinery utilization rate (% of capacity)
7. HY energy OAS actual number
8. OPEC+ current quotas per member
9. Brent M1-M3 spread exact level

**Acceptable thin:**
- Suezmax/Aframax rates (VLCC is the headline; these are secondary)
- DUC exact count (directional is enough for BRT-04)

---

## 2. DATA QUALITY — Confirmed vs Estimated vs Stale

### High Confidence — Well-Sourced [CONF]
| Data Point | Source | Date | Freshness |
|-----------|--------|------|-----------|
| Brent $88.59 | EIA/Bloomberg | Mar 5 | Fresh |
| WTI $80.88 | EIA | Mar 5 | Fresh |
| VLCC WS400+, $423-445K/day | maritime-hub.com | Mar 4 | Fresh |
| Gasoline inventories -1.704M bbl | EIA | wk Feb 27 | 1 week lag |
| Cushing change +1.564M bbl | EIA | wk Feb 27 | 1 week lag |
| Kuwait curtailing | Kpler | Mar 5 | Fresh |
| Qatar curtailing | Kpler | Mar 5 | Fresh |
| UAE ~22 days runway | JPMorgan | Mar 5 | Fresh |
| Retail gas $3.32/gallon | AAA/EIA | Mar 5 | Fresh |
| US production 13.7M bpd | Bloomberg/EIA | Dec 2025 | **6-week lag** |
| EOG price ~$132-135 | Nasdaq/UBS | Mar 5-6 | Fresh |
| Cheniere $250-257 | Robinhood | Mar 6 | Fresh |
| STNG entry ~$76.27 | Portfolio | Mar | Fresh |
| STNG current $80.19 | MacroTrends | Mar 4 | 2 days old |
| 3-2-1 crack $28.91 | EIA | Mar 5 | Fresh |
| Shipping -92% | Open Magazine | Mar 6 | Fresh |

### Estimated / Uncertain [EST]
| Data Point | Why Uncertain | Risk |
|-----------|--------------|------|
| Cushing absolute ~24-26M bbl | Weekly EIA wk Feb 27 shows change, not absolute in STATUS | Need to check EIA table for absolute level — this is knowable |
| USO price "~$110+ [EST Mar 6]" | Not pulled live | USO P/L estimate unreliable |
| USO entry "~$96 [EST]" | No confirmed entry price in files | Should be in FORGE/ACTIVE_TRADES.md |
| Brent structure "~$10-15/bbl M1-M12" | Rigzone Mar 2, not ICE direct | 4 days old, oil moves fast |
| US production weekly "~13.6-13.7M bpd [EST]" | Extrapolated from Dec figure | EIA weekly est. available but not pulled |
| OXY price "~$52-55 [EST]" | Not confirmed | Needs live check |
| HY energy OAS | No number anywhere | Pure gap |

### What Needs a Live Pull Monday
Priority order:
1. **Brent spot + WTI** (prices 24/7, will move over weekend)
2. **USO live price** (confirm position P/L before any sizing decisions)
3. **EIA Wednesday wk Mar 5** — Cushing absolute + change, gasoline implied demand, refinery util
4. **Current Baker Hughes rig count** (most recent Friday = Mar 7 if available)
5. **HY energy OAS** (Bloomberg or Fred)
6. **Brent M1-M3 spread from ICE** (term structure tightening/widening is Phase 1/2 signal)
7. **OPEC+ current quotas** (foundational number, never pulled)

---

## 3. PREDICTIONS REVIEW — BRT-01 through BRT-06

### BRT-01: Brent reaches $100 before Hormuz reopens
- **Well-formed?** Mostly. Clear metric ($100), clear condition (Hormuz still closed).
- **Falsifiable?** Yes — Hormuz reopens with Brent <$95 is clear invalidation.
- **Timeframe?** "Q1-Q2 2026" — WEAK. That's a 6-month window. Should be tighter: "by end of Q1 (Mar 31)" or "within 30 days of current Hormuz status."
- **Issue:** If Hormuz reopens Apr 1 with Brent at $99, is this falsified? Ambiguous.
- **Fix:** Add "If Hormuz closed ≥3 additional weeks from Mar 6, Brent reaches $100" — ties prediction to duration, not just calendar.

### BRT-02: Kuwait forced full curtailment within 14 days (by Mar 20)
- **Well-formed?** Yes. Specific actor, specific action, specific date.
- **Falsifiable?** Yes — Hormuz reopens or overland export arranged = invalidation.
- **Timeframe?** ✅ "By Mar 20" — perfect.
- **Issue:** "Already begun" — partial curtailment already observed. "Full curtailment" needs defining. 50%? 100%? Add: "Kuwait production falls below 1M bpd" as the specific trigger.
- **Confidence 70%** — reasonable given 12-day runway. High enough to act on.

### BRT-03: UAE curtailment within 25 days (by Mar 31)
- **Well-formed?** Yes. Similar to BRT-02.
- **Falsifiable?** Yes.
- **Timeframe?** ✅ "By Mar 31."
- **Issue:** Same definitional problem as BRT-02 — need "UAE production falls below X bpd" as the specific threshold.
- **Confidence 60%** — appropriately lower than BRT-02 given longer runway.

### BRT-04: US shale production does NOT meaningfully respond (<200K bpd increase) in Q1
- **Well-formed?** ✅ Best-formed prediction in the set. Specific metric (<200K bpd), specific period (Q1).
- **Falsifiable?** ✅ "EIA weekly shows >200K bpd increase" is clean.
- **Timeframe?** ✅ Q1 2026 ends Mar 31. Tight and testable.
- **Confidence 80%** — well-supported by DUC depletion, capital discipline, 3-6 month lag. Correct.
- **Only issue:** Q1 ends in 25 days. If no increase by Mar 31, this resolves CONFIRMED. Plan for it.

### BRT-05: Phase 2 (demand destruction visible in data) does not begin before Q2
- **Well-formed?** Partially. "Demand destruction visible in data" needs sharper definition.
- **Falsifiable?** The invalidation ("EIA gasoline demand drops -5% YoY in March") is specific and good.
- **Timeframe?** "Q2 2026" — means "not before Apr 1." Acceptable.
- **Issue:** There's ambiguity about what "begin" means for Phase 2. Multiple conditions required (Hormuz reopens AND demand destruction AND OPEC+ signals unwind). The prediction only tracks demand destruction, not all Phase 2 triggers. The prediction is narrower than the thesis.
- **Fix:** Add companion prediction: "BRT-07: OPEC+ unwind does not resume before Q2" — and "BRT-08: Hormuz remains functionally closed (>50% disruption) through Mar."

### BRT-06: STNG/TNK benefit from rerouting (rates rise 20%+)
- **Well-formed?** Weakest in the set.
- **Falsifiable?** Barely — "rates stay flat or decline" is vague. What's the baseline? 20%+ from what level?
- **Timeframe?** "Q1-Q2 2026" — too wide. 6 months.
- **Critical issue:** THIS PREDICTION IS ALREADY CONFIRMED. VLCC rates are at all-time highs (WS400+). If the prediction was "rates rise 20%+" from pre-war levels, WS400 is an order of magnitude above WS200 super-cycle threshold. The prediction should have been RESOLVED as of Mar 4 when VLCC data confirmed. It's sitting as OPEN when it should be CLOSED/CONFIRMED.
- **Status needs correcting to: CONFIRMED (Mar 4, 2026) — VLCC WS400+, well above 20% threshold.**
- **Fix immediately.** Then write a follow-on: "BRT-06b: STNG sustains >WS200 rates through Hormuz closure duration" with clear close condition.

### Missing Predictions That Should Exist
| Gap | Proposed Prediction |
|-----|-------------------|
| Brent backwardation depth | BRT-07: Brent M1-M6 spread stays >$5/bbl through Q1 |
| Hormuz duration | BRT-08: Hormuz remains >50% disrupted through end of March |
| Pump price peak | BRT-09: US retail gasoline reaches $4.00/gallon by Mar 21 |
| LNG price | BRT-10: JKM spot LNG exceeds $25/MMBtu by end of March (Qatar displacement) |
| Phase 1 duration | BRT-11: Phase 1 (squeeze) remains dominant thesis through FOMC Mar 17-18 |

Particularly embarrassing absence: **no prediction on gas pump prices.** FLOW.tsv says pump peak ~Mar 14-21. This is a core CARL feed and a risk communication tool — it should be tracked as a formal prediction.

---

## 4. NETWORK CONNECTIONS — Are Agent Flows Well-Defined?

### What Exists
- CLAUDE.md has a complete network table with 8 flows
- FLOW.tsv tracks 10 flows with mechanism, speed, and current state
- Mail outbox has one operational message to HAWK establishing division of labor

### Gaps and Problems

**HAWK → BRENT (receive):**
- ✅ Defined in CLAUDE.md. HAWK owns military ops and routes infrastructure intel.
- ❌ **No inbox mail received yet.** The operational message was written TO HAWK requesting routing, but there's no evidence HAWK has ever sent anything TO BRENT. Either HERMES hasn't set up the routing yet, or HAWK doesn't know what specifically to send.
- **Gap:** BRENT doesn't know HAWK's current Scenario framework (A/B/C/D status). BRENT STATUS references "Scenario C confirmation" but doesn't have the actual scenario definitions or current tier from HAWK.

**BRENT → CARL (send):**
- ✅ Defined. FLOW-BRT-02 tracks gas pump transmission. FLOW says "pump prices will print new highs ~Mar 20."
- ❌ No outbox mail to CARL exists. The Mar 14-21 pump price peak is a 🔴 priority signal and no mail has been written.
- **Action needed:** Write BRENT→CARL signal about pump price timeline before Monday.

**BRENT → HENRY (send):**
- ✅ Defined. FLOW-BRT-04 tracks inflation build.
- ❌ No outbox mail to HENRY. Mar 11 CPI is 5 days away and HENRY needs oil-driven CPI component estimate.
- **Action needed:** Write BRENT→HENRY with energy CPI estimate before Monday.

**BRENT → SAM (send):**
- ✅ Defined. FLOW-BRT-03 tracks Japan energy cost transmission.
- ❌ No outbox mail to SAM. Qatar LNG curtailment is a direct Japan impact signal (Japan 90% ME dependent).
- **Action needed:** Write BRENT→SAM on LNG pricing.

**BRENT → LIQUID (send):**
- ✅ Defined conceptually. FLOW-BRT-08 tracks E&P credit.
- ❌ No outbox mail. Energy HY OAS has no number to send. Can't write the signal until I have the actual OAS figure.
- **Gap:** Can't send signal without data.

**BRENT → REGINALD (send):**
- ✅ Defined in CLAUDE.md ("energy loan exposure at regional banks").
- ❌ Zero evidence this connection has ever been used or assessed. No data on regional bank energy loan exposure in any workbook file.
- **Assessment:** This connection may not be relevant yet (high oil = good for energy credit), but it should be assessed and explicitly stated.

**MARCO → BRENT:**
- ✅ Listed in CLAUDE.md as incoming flow (tariff impact on energy flows).
- ❌ No evidence this connection is active or that MARCO has ever routed anything. Given US-Iran war context, tariff/trade effects on energy are secondary to military effects, but still relevant.

### Overall Network Assessment
- Division of labor with HAWK is established on paper but operationally unproven (no mail received)
- 3 outbound signals need to be written before Monday (CARL, HENRY, SAM)
- LIQUID signal pending data pull
- REGINALD connection effectively dormant — needs explicit "not yet triggered" note

---

## 5. RESEARCH GAPS — Prioritized by Impact on Positioning

### Priority 1: Phase 1/2 Transition Intelligence (Immediate Positioning Impact)
**Gap:** No quantitative model for Phase 2 timing. The thesis says "sequencing is the alpha" but I have no specific triggers with probability weights. If Hormuz reopens in 30 days vs 60 days vs 90 days, what does Brent do? At what price does demand destruction visibly begin in weekly data?

**What I need:**
- Historical demand destruction timelines at equivalent price levels (2008, 2011, 2022)
- OPEC+ compliance history — how fast has the cartel historically unwound cuts?
- Hormuz reopening scenarios from HAWK with probability weights

**Why it matters:** The entire options/position rotation strategy depends on Phase 1→2 timing. Getting this wrong = being long Phase 1 plays into Phase 2.

---

### Priority 2: Cushing Absolute Level (Live Price/Size Impact)
**Gap:** I know change (+1.564M bbl wk Feb 27) but not absolute level (estimated 24-26M). If this falls toward 20M operational minimum, WTI dislocation happens. This threshold could trigger a position add or alert.

**What I need:** EIA weekly table, read actual Cushing number. This takes 2 minutes. It's just not been pulled.

---

### Priority 3: HY Energy OAS (LIQUID Connection, Credit Monitoring)
**Gap:** Zero quantitative data. Current assessment "not yet stressed" is qualitative. The threshold is >400bps. I don't know if we're at 200, 350, or 380.

**Why it matters:** If energy credit starts to stress (Phase 2 early signal), LIQUID needs alerting. Can't monitor a threshold without the starting number.

---

### Priority 4: LNG Spot Pricing (SAM Connection, Cheniere/LNG Play)
**Gap:** JKM Asia LNG spot price not in any file. Qatar curtailment thesis in HIGH_OIL_BENEFICIARIES.md says "likely spiking to $30-40+/MMBtu [EST]" — but no confirmed number. The Cheniere/LNG position thesis rests on this and it's unverified.

**Why it matters:** If JKM isn't actually spiking, the stealth LNG play loses its catalyst.

---

### Priority 5: Refinery Utilization (Crack Spread Context)
**Gap:** 3-2-1 crack at $28.91 is near $30 threshold, but without utilization rate, I don't know if refiners are running flat-out (bullish for margins = sustained) or if turnarounds are masking demand (bearish interpretation). 

**Why it matters:** CARL needs accurate pump price transmission and refinery util is a key input.

---

### Priority 6: Historical Phase Analogs (Scenario Modeling)
**Gap:** No historical research on prior Hormuz closure events or comparable supply disruptions. 1990 Gulf War, 2012 Iran sanctions, 2019 Abqaiq attack. How did prices move, how long did disruption last, when did demand destruction show up?

**Why it matters:** Would give probability weights to BRT-01 ($100 Brent) and Phase 2 timing that are currently gut-feel confidence numbers.

---

### Priority 7: Current Rig Count
**Gap:** No number in STATUS.md. "No response yet" is the assessment but I've never pulled the actual count. The baseline is needed to detect +50 threshold breach (shale response signal).

---

## 6. POSITION COVERAGE — Is Analysis Deep Enough to Trade?

### USO (2 shares)
**Coverage:** Thin.
- Entry: ~$96 [EST] — not confirmed anywhere. Should be in FORGE/ACTIVE_TRADES.md.
- Current price: ~$110+ [EST Mar 6] — not confirmed. USO tracks WTI but with ETF-specific contango drag; the relationship isn't tracked.
- Add criteria: "on dips" — not specific enough. What price triggers an add? What size?
- **Missing:** USO tracking error vs WTI (contango drag over time), option chain analysis for next leg, specific add trigger prices.
- **Grade: C.** Directionally positioned. Not sized for conviction. No defined add/exit rules.

### STNG (2 shares)
**Coverage:** Good.
- Entry: $76.27 [CONF]. Current $80.19 [CONF Mar 4 — 2 days old].
- Thesis fully explained in HIGH_OIL_BENEFICIARIES.md and VX.tsv.
- P/L +5.2% [CONF].
- BRT-06 confirmed (rates at super-cycle levels) but prediction not marked CLOSED.
- **Missing:** Where does STNG go if VLCC rates sustain? At WS400, what are quarterly earnings? Historical STNG multiple at prior rate peaks? Stop-loss level if Hormuz reopens suddenly? BofA PT was $56→$61 (below current $80 — does that mean it's already overshot analyst consensus?).
- **Grade: B-**. Good thesis, position working, but insufficient earnings modeling and no defined exit trigger.

### Beneficiaries List (EOG, LNG, OXY, XOM, COP, DVN, SLB, HAL, ET)
**Coverage:** Strong qualitative, thin quantitative.
- Qualitative thesis for each: ✅ Complete and well-reasoned.
- Price targets: mostly analyst consensus borrowed, not independently derived.
- Options analysis: entry strike/expiry "suggestions" but no IV analysis, no Greeks, no position sizing.
- Specific entry signals: missing. "If Brent hits $100, EOG trades $155-165" is an assertion without a model.
- Phase 2 short candidates identified: ✅ Good forward thinking.
- **Grade: B**. Enough to select which names to trade. Not enough to size correctly or time entries precisely.

### What's Missing for Trading-Grade Position Coverage
1. **Exit rules for all positions.** USO and STNG have no defined exit triggers. "Phase 2" is too vague.
2. **Specific entry prices for watchlist.** EOG at what price? LNG at what price?
3. **Position sizing framework.** Will has 2 shares of everything. Is that right for these price levels? No guidance.
4. **Options Greek analysis.** Strike/expiry recommendations without IV, delta, theta analysis.
5. **Correlation matrix.** How does EOG + OXY + USO in portfolio vs just USO? Am I recommending concentrated oil exposure?

---

## 7. OVERALL GRADE — Brutal Assessment

### Component Grades

| Component | Grade | Rationale |
|-----------|-------|-----------|
| Thesis quality (two-phase) | A- | Core thesis is well-developed, logical, internally consistent. Phase 2 timing definition slightly fuzzy. |
| Price/fundamental data | C+ | Core Brent/WTI good. Multiple critical gaps (rig count, refinery util, HY OAS, floating storage). |
| Predictions (BRT-01-06) | C | BRT-06 should be CLOSED. BRT-01 timeframe weak. 5 useful predictions are missing. |
| Network connections | C+ | Division of labor defined on paper. 0 signals sent to CARL/HENRY/SAM. HAWK flow unproven. |
| Research depth (beneficiaries) | B | Strong qualitative. No quantitative sizing/options model. |
| Position management (USO/STNG) | C | No entry confirmation on USO. No exit rules for either. No add triggers. |
| Data freshness | B- | Most prices from Mar 5-6. Some [EST] values need confirming. Rig count missing entirely. |

**Overall Grade: C+**

---

### What Would It Take to Get to A?

**Minimum viable A- by Monday AM:**

1. **BRT-06 → CLOSED/CONFIRMED.** Takes 30 seconds to mark in PREDICTIONS.tsv.

2. **Write 3 outbound signals (CARL, HENRY, SAM).** This is the highest-impact action before Monday. Network connections are paper-defined but operationally silent. CARL needs pump price timeline. HENRY needs oil CPI component estimate. SAM needs LNG pricing alert. These take 15 minutes total.

3. **Pull live prices at Monday open:** Brent, WTI, USO, STNG, EOG, LNG. Update STATUS.md before first check-in.

4. **Cushing absolute level.** Read EIA table, put a confirmed number in STATUS.md. 2 minutes.

5. **Add 5 missing predictions (BRT-07 through BRT-11).** Especially pump price target and Hormuz duration. These are the predictions that matter most for near-term positioning.

6. **Define add/exit rules.** Even rough: "Add USO if WTI pulls back to $78. Exit STNG if Hormuz reopens and VLCC rates fall below WS200." Specificity matters.

**To get from A- to A:**

7. **Phase 2 timing model.** Historical analogs. What happened to crude demand after 30/60/90 day supply shocks in 1990, 2012, 2019?

8. **HY energy OAS actual number.** Pull from FRED or Bloomberg. Monitor the >400bps threshold properly.

9. **Options sizing model.** EOG and LNG calls: specific strikes, expiries, premium budget, max loss defined.

10. **HAWK sync.** Get HAWK's current scenario framework (A/B/C/D) and current tier. BRENT references these without knowing the actual definitions.

---

### Honest Assessment

BRENT is 1 day old and was built under fire (Hormuz Day 7, -92K NFP, war context). The core thesis is sound and the research foundation is better than expected for a first spawn. HIGH_OIL_BENEFICIARIES.md is genuinely useful for decision-making.

The weaknesses are mostly execution gaps, not conceptual gaps:
- Data that should be pulled but hasn't been
- Signals that should be written but haven't been  
- Predictions that need tightening or are already resolved

**The network is the most concerning gap.** Three agents (CARL, HENRY, SAM) need inputs from BRENT that haven't been delivered. If the check-in Monday is the first time CARL hears that pump prices peak Mar 14-21, BRENT has failed a core function for 11 days.

**Priority action before Monday:** Write the outbound signals. Everything else is data quality. The signals are the job.

---

*Audit compiled by BRENT, 2026-03-06. No verbal report — file is the handoff.*
