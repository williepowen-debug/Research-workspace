# VIX THESIS (v3.0 — Four-Model Synthesis Apr 2026)

VIOLET's core framework: Credit-vol relationship is **regime-dependent, crisis-type-dependent, and directionally asymmetric**.

---

## CENTRAL CLAIM (Four-Model Synthesis)

**Synthesized from:** Gemini, Perplexity, Claude (native research), Grok

**Core claim:** Aggregate HY OAS leads VIX by 2-6 weeks at tactical level (100bps widening → VIX spike) and ~7 months at cycle level (trough → peak) **when:**
1. VIX < 20 at onset (low vol regime)
2. Shock originates in credit markets (not rates/macro)
3. Widening is cross-sector (not sector-specific)
4. Yield curve is not inverted (filters rate-driven shocks)

**Hit rate:** ~70% | **False positive rate:** 25-30% (15-20% with yield curve filter)

---

## THE ACADEMIC NUANCE (Claude's Contribution)

> "Academics observe equity leading credit at the firm level, while practitioners observe aggregate HY spreads leading equity selloffs."

**Reconciliation:**
1. **Aggregate vs. individual:** HY OAS reflects deterioration across many issuers simultaneously
2. **Asymmetric by news type:** CDS leads for negative, firm-specific credit info; equity leads for systematic/positive news
3. **Crisis amplification:** During turbulent periods, equity hedge ratios increase 3-4×, making implied volatility the predominant driver

**Key insight:** Even though equity leads at the micro level, HY OAS can lead at the macro level because it captures systemic credit deterioration.

---

## REGIME-DEPENDENT BEHAVIOR (All Four Models)

### Low Vol Regime (VIX < 20)
| Characteristic | Value |
|----------------|-------|
| Days observed | 1,264 (63% of time) |
| Credit-VIX correlation | 0.06 (weak) |
| Lead-lag | **Credit leads by 6-16 weeks** (when shock is credit-originated) |
| Term structure | Contango |
| Signal quality | **Highest** — longest lead time, most edge |

**Implication:** This is the actionable window. Credit provides early warning while equity remains complacent.

### Rising Vol Regime (VIX 20-30)
| Characteristic | Value |
|----------------|-------|
| Days observed | 606 (30% of time) |
| Credit-VIX correlation | 0.48 (moderate) |
| Lead-lag | **1-4 weeks** (compressed) |
| Term structure | Flattening |
| Signal quality | **Moderate** — co-movement, less edge |

**Implication:** Lag trade window still open but shorter. Faster feedback loops.

### High Vol Regime (VIX 30-40)
| Characteristic | Value |
|----------------|-------|
| Days observed | 111 (5% of time) |
| Credit-VIX correlation | 0.33 |
| Lead-lag | **Near-simultaneous** (0-2 weeks) |
| Term structure | Mixed/backwardation |
| Signal quality | **Low** — too late |

**Implication:** Both markets pricing stress. No lead-lag edge.

### Crash Regime (VIX > 40)
| Characteristic | Value |
|----------------|-------|
| Days observed | 38 (2% of time) |
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

## REGIME-DEPENDENT BEHAVIOR

### Low Vol Regime (VIX < 20)
| Characteristic | Value |
|----------------|-------|
| Days observed | 1,264 (63% of time) |
| Credit-VIX correlation | 0.06 |
| Lead-lag | None reliable |
| Term structure | Contango |
| Mean reversion | Strong |

**Implication:** In low vol, credit stress doesn't reliably predict VIX moves. Vol is driven by flows, positioning, technicals.

### Rising Vol Regime (VIX 20-30)
| Characteristic | Value |
|----------------|-------|
| Days observed | 606 (30% of time) |
| Credit-VIX correlation | 0.48 |
| Lead-lag | ~5 days (credit slightly leads) |
| Term structure | Flattening |
| Mean reversion | Weakening |

**Implication:** This is the "lag trade" window. Credit stress starts to predict VIX, but relationship still noisy.

### High Vol Regime (VIX 30-40)
| Characteristic | Value |
|----------------|-------|
| Days observed | 111 (5% of time) |
| Credit-VIX correlation | 0.33 |
| Lead-lag | Simultaneous |
| Term structure | Mixed |

**Implication:** Both markets pricing stress. No lead-lag edge.

### Crash Regime (VIX > 40)
| Characteristic | Value |
|----------------|-------|
| Days observed | 38 (2% of time) |
| Credit-VIX correlation | High |
| Lead-lag | VIX leads by ~20 days |
| Term structure | Backwardation |

**Implication:** In crashes, vol shock front-runs credit repricing. Relationship inverts.

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

### The Regime Shift Trade

**Setup:**
- Low vol regime persistent (VIX < 20 for >3 months)
- Credit stress emerging (HY OAS >4)
- Term structure flattening (VIX3M/VIX < 1.2)

**Entry:** VIX calls 60-90 DTE
**Target:** Regime shift to rising vol (VIX 25-30)
**Stop:** VIX breaks below 15, credit stress resolves
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

| Prediction | Resolution Date | Confidence |
|------------|-----------------|------------|
| HY OAS > 400bps + VIX 20-30 → VIX > 30 within 10 days | TBD | Medium |
| Term structure inversion (VIX3M/VIX < 1.0) → VIX spike > 50% within 5 days | TBD | High |
| VVIX > 120 → VIX > 25 within 3 days | TBD | Medium |
| VIX > 40 → HY OAS > 600bps within 20 days | TBD | High |

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

Current status:
- **BROCK/SHADE:** Private credit gating (ongoing)
- **LIQUID:** HY OAS 2.90 (tight, not stressed yet)
- **VIOLET:** Low vol regime — no signal yet
- **HENRY:** Equity markets stable

The VIX lag window will open when:
1. HY OAS breaks above 4.0 (enter rising vol regime)
2. VIX stays below 25 (divergence)
3. Term structure flattens

Until then: Watch, wait, track.

---

*Created: 2026-04-12*
*Status: ACTIVE — historical research complete, live testing pending*
