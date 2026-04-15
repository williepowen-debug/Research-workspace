# VIX THESIS (v3.1 — Empirical Audit Apr 15, 2026)

VIOLET's core framework: Credit-vol relationship is **regime-dependent, crisis-type-dependent, and directionally asymmetric**.

---

## CHANGELOG

**v3.1 (2026-04-15) — First empirical audit against 20y VIX/VIX3M history (4,968 days)**
- ✅ Regime distributions confirmed within noise (VIX<20 = 64.5% vs thesis 63%)
- ✅ Added COMPLACENCY (VIX<15) as distinct regime — 33% of days, not to be bucketed with LOW_VOL
- ❌ **Prediction #2 (term-structure inversion → VIX spike) FALSIFIED.** 553 historical inversion events produced 2.2% hit rate for >50% VIX spike in next 5 days; mean forward VIX move was -5.1%. Inversion MARKS PEAK, does not lead. See KB-VIO-034.
- ⚠️ KB-VIO-023 "gold standard" framing corrected — article cherry-picked 2008/2020; base rate is opposite.
- Added local crisis analog: Mar 18–Apr 8 2026 stress episode (KB-VIO-030).
- Marked inherited hit rates (70% / 25-30% FP) as four-model-synthesis-derived, not VIOLET-validated.
- Regime-shift trade entry signal revised: flattening contango is NOT an entry for VIX calls.

**v3.0 (2026-04-12)** — Four-model synthesis (Gemini, Perplexity, Claude, Grok).

---

## CENTRAL CLAIM (Four-Model Synthesis)

**Synthesized from:** Gemini, Perplexity, Claude (native research), Grok

**Core claim:** Aggregate HY OAS leads VIX by 2-6 weeks at tactical level (100bps widening → VIX spike) and ~7 months at cycle level (trough → peak) **when:**
1. VIX < 20 at onset (low vol regime)
2. Shock originates in credit markets (not rates/macro)
3. Widening is cross-sector (not sector-specific)
4. Yield curve is not inverted (filters rate-driven shocks)

**Hit rate:** ~70% | **False positive rate:** 25-30% (15-20% with yield curve filter)

> ⚠️ **Source note (v3.1):** Hit-rate figures are INHERITED from the four-model research synthesis (Gemini/Perplexity/Claude/Grok). They have NOT been independently reproduced or back-tested by VIOLET against our own data. Treat as directional framework, not validated statistics.

---

## THE ACADEMIC NUANCE (Claude's Contribution)

> "Academics observe equity leading credit at the firm level, while practitioners observe aggregate HY spreads leading equity selloffs."

**Reconciliation:**
1. **Aggregate vs. individual:** HY OAS reflects deterioration across many issuers simultaneously
2. **Asymmetric by news type:** CDS leads for negative, firm-specific credit info; equity leads for systematic/positive news
3. **Crisis amplification:** During turbulent periods, equity hedge ratios increase 3-4×, making implied volatility the predominant driver

**Key insight:** Even though equity leads at the micro level, HY OAS can lead at the macro level because it captures systemic credit deterioration.

---

## REGIME-DEPENDENT BEHAVIOR (All Four Models + VIOLET 20y backtest)

> **v3.1 note:** Day counts below updated from thesis v3.0's 2019-day sample to VIOLET's 20-year verification sample (4,968 days, 2006–2026). Distributions confirmed within noise. **COMPLACENCY regime added** as distinct bucket — was previously lumped into LOW_VOL.

### Complacency Regime (VIX < 15) — *added v3.1*
| Characteristic | Value |
|----------------|-------|
| Days observed | 1,652 (33.3% of time) — **largest single bucket** |
| Credit-VIX correlation | Very weak |
| Lead-lag | **Credit leads by 6-16 weeks** (longest lead, highest signal quality per KB-VIO-022) |
| Term structure | Steep contango |
| Signal quality | **Highest** — greatest window for positioning |

**Implication:** This is the *pre-stress* regime — the volatility paradox zone where complacency builds up structural risk. Most actionable for strategic credit-vol lag positioning. Our Mar 27 episode started from ~20, so we haven't recently been here.

### Low Vol Regime (VIX 15-20)
| Characteristic | Value |
|----------------|-------|
| Days observed | 1,550 (31.2% of time) |
| Credit-VIX correlation | 0.06 (weak) |
| Lead-lag | **Credit leads by 3-8 weeks** |
| Term structure | Contango |
| Signal quality | **High** — actionable lag window |

**Implication:** Active monitoring zone. Credit stress starts becoming predictive. **Current regime as of Apr 15 (VIX 18.09).**

### Rising Vol Regime (VIX 20-30)
| Characteristic | Value |
|----------------|-------|
| Days observed | 1,317 (26.5% of time) |
| Credit-VIX correlation | 0.48 (moderate) |
| Lead-lag | **1-4 weeks** (compressed) |
| Term structure | Flattening |
| Signal quality | **Moderate** — co-movement, less edge |

**Implication:** Lag trade window still open but shorter. Faster feedback loops. **Mar 18–Apr 8 2026 episode spent most of its duration here.**

### High Vol Regime (VIX 30-40)
| Characteristic | Value |
|----------------|-------|
| Days observed | 270 (5.4% of time) |
| Credit-VIX correlation | 0.33 |
| Lead-lag | **Near-simultaneous** (0-2 weeks) |
| Term structure | Mixed/backwardation |
| Signal quality | **Low** — too late |

**Implication:** Both markets pricing stress. No lead-lag edge. **Mar 27 2026 peak (VIX 31.05) briefly entered this regime.**

### Crash Regime (VIX > 40)
| Characteristic | Value |
|----------------|-------|
| Days observed | 179 (3.6% of time) |
| Credit-VIX correlation | High |
| Lead-lag | **VIX leads credit by ~20 days** (relationship inverts) |
| Term structure | Backwardation |
| Signal quality | **None** — relationship breaks down |

**Implication:** In crashes, vol shock front-runs credit. Don't trade lag here.

---

## THE TRANSMISSION CHAIN

```
BROCK (Private Credit Stress)
    ↓
LIQUID (HY OAS, CCC OAS widen)
    ↓
VIOLET (Regime detection: low vol → rising vol → crash)
    ↓
HENRY (Equity market impact)
    ↓
Portfolio P&L
```

**VIOLET's role:** Detect regime shifts and credit-vol divergences. Signal when vol markets are complacent relative to credit stress.

---

<!-- v3.1: duplicate regime table removed; see canonical version above. -->

---

## CRISIS ANALOGS (Complete Episode Database)

### Credit-Led Episodes (VIX < 20 at onset)

**GFC 2007-08 (Canonical Credit Lead)**
- HY OAS: 241 bps (June 2007) → 2,182 bps (Dec 2008)
- VIX: 12 → 80.86 (Nov 2008 peak)
- **Lead:** 6-10 weeks to first spike, 14 months to sustained >30
- **Lesson:** Credit stress in low vol regime provides months of warning

**2011 EU Sovereign Crisis**
- HY OAS: 500 bps (May 2011) → 910 bps (Oct 2011)
- VIX: 18-23 → 48 (Aug 2011)
- **Lead:** 8-10 weeks
- **Lesson:** Sovereign contagion transmits through credit first

**2015-16 Energy/China (Partial False Positive)**
- HY OAS: 336 bps (Jun 2014) → 887 bps (Feb 2016)
- VIX: 12-17 → 53 briefly (Aug 2015), then revert
- **Lead:** 12-18 months credit lead, but VIX didn't sustain
- **Lesson:** Sector-specific stress can produce credit warning without systemic vol spike

### VIX-Led or Coincident Episodes

**Feb 2018 Volmageddon (VIX False Positive)**
- VIX spike: 17.31 → 37.32 (+115%, largest % move on record)
- HY OAS: Stable at ~320 bps
- **Lead:** VIX led, credit never confirmed
- **Lesson:** Technical unwind (short-vol ETP blowup) without credit stress = VIX spike is noise

**Q4 2018 (Macro/Rate-Driven)**
- HY OAS: 316 bps → 526 bps (Q4)
- VIX: 12 → 36 (Dec 24)
- **Lead:** Coincident to VIX-led (2-3 weeks)
- **Lesson:** Rate-driven equity selloffs invert the typical pattern

**Mar 2020 COVID (Exogenous Shock)**
- HY OAS: 362 bps → 1,087 bps (Mar 23)
- VIX: 12.5 → 82.69 (Mar 16, all-time high)
- **Lead:** Near-simultaneous; VIX peaked 7 days before credit
- **Lesson:** Exogenous shocks compress lead time to days

**2022 Rate Shock (Structural Divergence)**
- HY OAS: 310 bps → 580 bps (Jun-Jul 2022)
- VIX: 25-38 sustained, Mar 11 VIX 30.75 implied HY OAS ~774 bps, actual ~405 bps
- **Lead:** VIX led by 10-12 weeks
- **Lesson:** Rates-driven equity correction with healthy credit = VIX leads, credit never catches up

**Aug 2024 Yen Carry Unwind (VIX False Positive)**
- VIX: Largest single-day spike (+180% to ~66 intraday)
- HY OAS: No meaningful widening
- **Lead:** VIX led, credit unaffected
- **Lesson:** Positioning-driven vol spikes without credit confirmation are transient

**Mar 18 – Apr 8 2026 Local Episode (*added v3.1, VIOLET-observed*)**
- VIX: 25 (Mar 18) → **31.05 peak (Mar 27)** → 18.09 (Apr 15)
- VVIX: 126 → 133 (peak) → 99
- M1:M2 steepness: Deep backwardation -7.02% at peak (13/22 observed days in backwardation)
- HY OAS: No significant widening — tightened through 300bps on Apr 10
- **Lead:** Coincident / VIX-led — RISING_VOL origin, not credit-driven
- **Duration:** ~2 weeks backwardation (vs 2008 ~1Q, 2020 ~10w)
- **Lesson:** Contained stress event, not systemic. Confirmed VIX-leads pattern for rising-vol-originated episodes. See KB-VIO-030.

---

## TRADE IMPLICATIONS

### The Lag Trade (Revised)

**Setup:**
- Regime: Rising vol (VIX 20-30)
- HY OAS widens >50bps in 1 week
- VIX flat or down
- Term structure NOT inverted

**Entry:** VIX calls 30-60 DTE
**Target:** VIX catches up to credit-implied level
**Stop:** HY OAS reverses, or VIX spikes >30
**Sizing:** 1% account (lowered from 2% — thesis less certain)

### The Regime Shift Trade (revised v3.1)

**Setup:**
- COMPLACENCY / LOW_VOL regime persistent (VIX < 20 for >3 months)
- Credit stress emerging (HY OAS >4)
- VVIX > 120 **while VIX < 20** (divergence — per KB-VIO-027, not KB-VIO-023)
- ~~Term structure flattening (VIX3M/VIX < 1.2)~~ **REMOVED v3.1 — empirical data shows inversion is a PEAK signal, not entry signal. See KB-VIO-034.**

**Entry:** VIX calls 60-90 DTE
**Target:** Regime shift to rising vol (VIX 25-30)
**Stop:** VIX breaks below 15, credit stress resolves, or 7-day sustained contango re-steepening
**Sizing:** 1.5% account

---

## RISK FACTORS

**What breaks the relationship:**
1. **Central bank intervention** — Fed puts floor under credit, vol decouples
2. **Technical flows** — VIX driven by option dealers, not credit
3. **Idiosyncratic credit stress** — Single-name default, not systemic
4. **Equity-led selloff** — VIX spikes before credit (crash regime)

**Mitigation:**
- Require systemic credit stress (HY OAS, not single names)
- Check term structure (inversion confirms vol catch-up likely)
- Monitor VVIX (vol-of-vol confirms option market stress)
- Only trade "lag" in rising vol regime

---

## PREDICTIONS (Falsifiable)

**v3.1 review protocol:** Each prediction gets a resolution date when conditions fire. Predictions that pass/fail with n>10 events get promoted to KB as empirical findings. Review monthly.

| # | Prediction | Status (Apr 15) | Confidence | Resolution |
|---|------------|-----------------|------------|------------|
| 1 | HY OAS > 400bps + VIX 20-30 → VIX > 30 within 10 days | Untested — trigger conditions not met since thesis written | Medium | Review when HY OAS >400 |
| 2 | ~~Term structure inversion (VIX3M/VIX<1.0) → VIX spike >50% within 5 days~~ | **FALSIFIED 2026-04-15** (KB-VIO-034: 553 events, 2.2% hit rate, mean -5% forward) | ~~High~~ → **rewritten below** | — |
| 2' | **Sustained** term structure inversion (VIX3M/VIX<1.0 for ≥7 consecutive days) → VIX sustains above 25 for ≥10 days following | Untested (only 13 such events in 20y — rare) | Medium | Next event |
| 3 | VVIX > 120 **with VIX < 20** (divergence) → VIX > 25 within 10 days | Untested — divergence form required (not coincidence) | Medium | Next event |
| 4 | VIX > 40 → HY OAS > 600bps within 20 days | Untested — VIX hasn't reached 40 since thesis | Medium (downgraded from High — inherited, not VIOLET-validated) | Next event |

**Scoring rules:**
- "Untested" = trigger conditions have not occurred
- "PASSED" = prediction fired and outcome followed within window
- "FAILED" = prediction fired and outcome did not follow
- "FALSIFIED" = backtest proved prediction wrong before it was tested forward

---

## RESEARCH AGENDA

**Phase 1: Historical Analysis** ✅ COMPLETE
- ✅ Download VIX and HY OAS data (2018-present)
- ✅ Calculate correlation and lead-lag
- ✅ Identify regime-dependent behavior

**Phase 2: Crisis Analogs** ✅ COMPLETE
- ✅ Mar 2020: VIX led credit by 21 days
- ✅ Feb 2018: Credit didn't lead (technical spike)
- ✅ Feb 2021: Equity-specific vol

**Phase 3: Live Testing**
- [ ] Track credit-vol divergence in real-time
- [ ] Paper trade lag signals
- [ ] Measure hit rate by regime

---

## CONNECTION TO SYSTEM THESIS

System thesis (Scenario D 82%): Credit stress → bank stress → equity crash.

**VIOLET's role:** Time the equity vol leg and detect regime shifts.

### Current status (Apr 15, 2026)
- **BROCK/SHADE:** Private credit gating (ongoing, verify with agent)
- **LIQUID:** HY OAS 290bps (Apr 10, tightened through RED 300bps falsification — credit rallying, not stressing)
- **VIOLET:** LOW_VOL regime. **Just exited Mar 18–Apr 8 local stress episode** (peak VIX 31.05 Mar 27). VIX 18.09, VVIX 99.56, SKEW 149.94 (persistent bid), M1:M2 +2.04% (86th percentile of recent 22 days — regime-relative, BELOW_AVG vs static). See KB-VIO-030/031 for pattern analysis.
- **HENRY:** Needs refresh — last snapshot Apr 12.

### The VIX lag window opens when:
1. HY OAS breaks above 4.0 (currently 2.90, distant)
2. VIX stays below 25 (currently 18.09 ✓)
3. **VVIX > 120 while VIX < 20** (divergence form — KB-VIO-027 Pattern A, NOT the term-structure-flattening signal from v3.0)

### Open questions for next session
- What triggered the Mar 27 peak? Cross-reference HENRY/LIQUID/RED STATUS from Mar 25-28.
- Is the persistent SKEW bid (KB-VIO-031) Pattern A (pre-crash) or post-stress retention? Re-evaluate 2026-04-29.
- Need HENRY Apr 15 refresh for equity-side confirmation.

Until then: Watch, wait, track.

---

*Created: 2026-04-12 (v3.0)*
*Empirical audit: 2026-04-15 (v3.1 — first backtest against own data)*
*Status: ACTIVE — live testing phase, monthly prediction review*
