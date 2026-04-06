# Phase 2 Transition Matrix — BRENT Review
**Reviewer:** BRENT  
**Date:** 2026-03-07  
**Source reviewed:** `demand_destruction/TRANSITION_MATRIX.md` (formerly `research/PHASE2_TRANSITION_INDICATORS_MAR8.md`)  
**Purpose:** Cross-reference PROME's matrix against BRENT's existing framework. Flag agreements, disagreements, additions, and VLCC rate question.

---

## EXECUTIVE VERDICT

PROME's matrix is solid and largely convergent with my existing framework. The key innovation is **explicit bifurcation into Resolution (Trigger A) vs. Demand Destruction (Trigger B) paths**, each with different indicator sets and different action cadences. This is an upgrade over my prior single-playbook approach. The historical analog methodology is sound. I have four substantive additions and one disagreement on thresholds.

**Net assessment: Adopt the matrix as operational framework with modifications below.**

---

## AGREEMENTS

### 1. Historical analog selection ✅
The three-cycle framework (1990 / 2008 / 2022) is the right universe. These are the only modern shocks with (a) scale, (b) documented data, and (c) resolution events we can measure lead times from. I independently converged on the same three.

### 2. Resolution path is binary — no leading market indicator ✅
1990 is the canonical example. The only "market" signal was M1-M12 spread narrowing — and even that lagged diplomatic/military signals. My STATUS already says "exit on announcement, not on physical reopening." PROME's matrix formalizes this correctly: Trigger A requires acting within 4 hours. Waiting for "confirmation" from market data is how you get Gulf War Syndrome'd — 33% in 24 hours.

### 3. Demand destruction timeline confirms BRT-05 and BRT-08 ✅
20-24 week minimum for EIA data to show -5% YoY. PROME's analysis matches my research. The 2026 demand-more-inelastic adjustment (EVs removed marginal drivers) is valid and correctly stretches the timeline. BRT-05 (Phase 2 not visible before Q2) and BRT-08 (earliest EIA signal May-June) are confirmed.

### 4. CFTC managed money divergence is the strongest Tier 2 signal ✅
In 2008 it led by 3-4 months. In 2022 by 3 months. The pattern — positioning declining while price holds or rises = distribution — is well-documented blow-off top behavior. The backlog on COT data is a real handicap. My STATUS flagged this same gap.

### 5. The "dangerous scenario" — both paths converging ✅
PROME correctly identifies this as the most violent outcome. It's what happened in 2022 (supply shock + demand shock + policy tightening = $139→$85 in 6 months). Given our current setup (oil shock + -92K NFP + munitions depletion timeline + Ras Laffan independently offline), the probability of convergence is non-trivial. My BRT-16 (macro transmission chain) maps the same pathway.

---

## DISAGREEMENTS / THRESHOLD DIFFERENCES

### 1. M1-M3 threshold: $3/bbl vs. my $2/bbl
**PROME's matrix:** <$3/bbl for 3 consecutive days = Trigger B signal  
**My STATUS playbook (X trigger):** <$2/bbl  

**BRENT assessment: PROME is right. Revising to $3/bbl.**

At $2/bbl you're already very late. If the spread has compressed from $10+ to $2, the market has been pricing transition for weeks and fast money is already repositioning. The $3/bbl threshold provides 1-2 extra weeks of lead time — enough to actually rotate. Three consecutive daily closes prevents false signals (one bad print on thin trading doesn't count).

**Action:** Update Phase 2 playbook trigger X from <$2/bbl to <$3/bbl.

### 2. Combination rule for Resolution is different from my prior playbook
**My old playbook:** Required ALL THREE of X (M1-M3 <$2), Y (VLCC <WS300), Z (ceasefire/escort/50%+ flow).  
**PROME's matrix:** Resolution path = ANY ONE of P&I coverage, escort ops, OR diplomatic shift → act immediately. VLCC and spread aren't required.  

**BRENT assessment: PROME is right for Resolution specifically.**

My old three-trigger requirement made sense for Demand Destruction (need multiple confirming signals for a gradual process). But for Resolution, waiting for VLCC rates to confirm is backwards — rates fall BECAUSE of the announcement, not before it. Requiring VLCC <WS300 as a Resolution trigger means you act AFTER the fact. PROME's framework correctly separates these. I was conflating two different action logics.

**Correction:** For Resolution (Trigger A): binary, act on any one diplomatic/military signal. VLCC rates are confirming AFTER exit, useful for sizing Phase 2 entry timing.

---

## ADDITIONS — INDICATORS PROME MISSED

### A. Aviation capacity announcements (should be Tier 2)
My STATUS and BRT-09 both flag airline route cuts as a Phase 2 leading indicator by 4-8 weeks. Singapore jet crack at $145/bbl ALL-TIME RECORD. Airlines with heavy ME exposure or thin margins will announce groundings and ASM cuts before EIA gasoline data moves. **This is actionable and should be formalized:**

> **Add to Tier 2:** Track weekly ASM capacity announcements from major US carriers (United, Delta, American) and Gulf-hub carriers (Emirates, Qatar Airways if still operational). IATA weekly capacity data.  
> **Threshold:** 2+ major carriers announce >5% ASM reduction → Phase B demand destruction signal.  
> **Lead time:** Historical 4-8 weeks ahead of EIA gasoline data.

This is especially relevant NOW because Singapore jet crack at $145 is unsustainable for unhedged carriers. Route cuts are coming if Brent stays $90+.

### B. Initial jobless claims — weekly watch
PROME flagged this in Part 6 research gaps but didn't formalize it in the matrix. Given -92K NFP already confirmed, weekly initial claims are a DIRECT MONITOR for the front-running demand destruction scenario PROME described. If claims start rising sharply (say, >280K 4-week average vs ~215K current) WHILE oil stays elevated, we have simultaneous supply AND demand shock — the dangerous scenario is developing.

> **Add to Tier 2:** DOL initial jobless claims (Thursday 8:30 ET).  
> **Threshold:** 4-week average >260K AND rising → demand destruction may be frontrunning historical timeline.

### C. ATA Truck Tonnage Index
Already in STATUS but not in matrix. Trucking is the canary for goods-sector demand destruction. If trucking volume is falling while oil is high, industrial demand is cracking before consumer data shows it.

> **Add to Tier 3 (confirming, monthly cadence):** ATA monthly Truck Tonnage Index.  
> **Threshold:** YoY negative for 2 consecutive months.

### D. Cushing inventory absolute level — Phase 2 price target calibration
PROME lists Cushing in Tier 2 (#9) correctly. But the matrix doesn't note the Phase 2 price target implication. If Cushing is near operational minimum (<20M bbl) when Resolution fires, WTI won't fall as far or as fast — there's genuine physical bid from drawdown-depleted storage. This matters for sizing Phase 2 put spreads (strike selection on USO bear put spread). Need Monday's EIA data.

---

## THE VLCC QUESTION: IS IT A LEADING INDICATOR?

**PROME's call:** VLCC rates are NOT a leading indicator (Tier 2 confirming, noting 2022 as the key data point where rates fell -59% WHILE oil hit $130+, then spiked Q4 2022 on EU embargo — completely detached from oil price cycle).

**BRENT's assessment: PROME is correct, but the nuance matters for how we manage STNG.**

### Why PROME is right:
1. **2022 data is dispositive.** Russia-Ukraine: VLCC rates fell 59% from invasion week through March 2022 while Brent surged to $139. Oil price and tanker rates diverged completely. Then Q4 2022 tanker spike was a separate mechanism (EU embargo → route extension → ton-mile demand). Two completely different phenomena in the same year.

2. **In our 2026 scenario**, the VLCC super-cycle (WS400+) is driven by: (a) existing cargoes rerouting to avoid Hormuz, (b) trapped LNG carriers, (c) strategic stockpiling globally. These are all Phase 1 dynamics. When Hormuz reopens, VLCC rates will FALL — but they'll fall CONCURRENTLY with or AFTER the announcement, not before.

3. **Mechanically**: VLCC rates can't lead Hormuz closure events. They respond to transit counts, cargo availability, and insurance coverage — all of which change at the event, not before.

### The nuance for STNG:
**VLCC rates are a lagging indicator for oil prices but a CONCURRENT indicator for STNG exit timing.** 

The exit trigger for STNG (BRT-15) is the escort/ceasefire announcement — which is the same trigger that collapses VLCC rates. So in practice:

- If you're watching VLCC rates to decide when to exit STNG → you will exit late (after the announcement is already public).
- If you're watching diplomatic/military signals (PROME's Tier 1 indicators #1-3) → you exit STNG during the announcement window, before rates have meaningfully moved.

**Conclusion:** PROME is right that VLCC rates are not a leading indicator. But the STNG position doesn't need VLCC as a leading indicator — it needs Tier 1 diplomatic signals (P&I coverage, escort announcement, ceasefire). BRT-15 already captures this correctly.

**The only scenario where watching VLCC rates adds value:** If VLCC rates start declining from WS400+ WITHOUT a diplomatic announcement (say, due to alternative routing discovery or DFC backstop gaining credibility), that could signal market anticipating resolution before it's formally announced. Watch for unexplained VLCC rate decline as a weak signal. But this is Tier 3 at best.

---

## CALIBRATION CONFIDENCE UPDATES

| Prediction | Prior Confidence | New Confidence | Reason |
|------------|-----------------|----------------|--------|
| BRT-05 (Phase 2 not visible before Q2) | 82% | **85%** | Matrix analysis confirms 20-24 week floor; -92K NFP complicates but doesn't shorten EIA data visibility |
| BRT-08 (demand data earliest May-June) | 72% | **72%** | No change — matrix confirms same timeline |
| BRT-15 (STNG exit on announcement not reopening) | 85% | **90%** | PROME's matrix + VLCC analysis reinforces this. The binary nature of Trigger A makes this nearly certain. |
| BRT-07 (OPEC+ meeting + $20-40 drop within 7 days of reopening) | 80% | **80%** | No new information changes this |

**New prediction warranted:** BRT-21 — The three-signal combination (M1-M3 <$3, gasoline -5% YoY, COT declining) if all present, gives 4-6 week lead on Phase 2 top with ~80-85% historical accuracy. Not a new market call — formalizes the combination rule.

---

## WHAT THE MATRIX DOESN'T ADDRESS

1. **The Ras Laffan variable.** PROME's matrix treats Hormuz reopening as the key Phase 2 trigger. But BRT-17 confirms Ras Laffan is offline 60-90 days post-reopening minimum. This means even after Trigger A fires, US LNG (Cheniere/VG) remains elevated. The matrix doesn't capture this — Phase 2 for OIL could be Trigger A while Phase 2 for LNG is later and shallower. Different exit sequences for USO vs LNG positions.

2. **The munitions depletion duration limiter.** BRT-19 at 65%: Pentagon flagged dwindling stocks by Mar 6. This creates a 30-60 day hard limit on current posture, which means Resolution path probability INCREASES after Day 30-40 regardless of diplomatic signals. The matrix should note that Trigger A probability rises mechanically over time as US options narrow.

3. **Saudi Aramco East-West pipeline ceiling.** At 3.3-3.5M bpd Yanbu loading limit, Saudi bypass is maxed. If Brent prices this in, the squeeze continues even with Saudi pumping at surge levels. The matrix correctly identified SPR releases as a signal but doesn't note that a joint SPR + IEA release is more likely than US solo (2022 was IEA coordinated). An IEA coordinated release announcement would be a Tier 1.5 signal — not Resolution but meaningful cap.

---

## OPERATIONAL PROTOCOL (for STATUS.md)

Derived from PROME's matrix:

**Monitoring schedule:** (See STATUS.md update)  
**Combination rule:** 
- Path A: ANY ONE of P&I coverage resumption, US naval escort announcement, or credible ceasefire dialogue → EXIT ALL Phase 1 longs within 4 hours. No waiting.
- Path B: ALL THREE of (M1-M3 <$3/bbl × 3 days) + (gasoline demand -5% YoY × 3 weeks) + (managed money net long declining × 2 weeks) → Begin gradual rotation. Historical lead time to top: 4-6 weeks.

---

*Review complete. Files updated: STATUS.md (Operational Protocol section), PREDICTIONS.tsv (BRT-15 confidence update).*
