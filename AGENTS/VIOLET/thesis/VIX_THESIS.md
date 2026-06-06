# VIX THESIS (v3.3 — 6/5 NFP-shock live test integration, 2026-06-06)

VIOLET's core framework: Credit-vol relationship is **regime-dependent, crisis-type-dependent, and directionally asymmetric**. Operational signal stack runs L1 (population framework, real-money) over L2-L4 calibration filters. Two transmission paths now formal: standard credit-led, and concentration-unwind parallel.

---

## CHANGELOG

> Canonical "old view → new view" per-bump log lives in `thesis/CHANGELOG.md`. This section is the in-body version history.

**v3.3 (2026-06-06) — 6/5 NFP-shock live test integration**
- L1-L4 operational stack discipline codified: L1 PROMOTED to real-money; L2 wrong-mechanism (consensus-miss carve-out pending); L3 N=1 PROVISIONAL; L4 demoted to descriptive. KB-VIO-070.
- KB-VIO-067 DIET signature backtest upgraded from ASSUMPTION → EMPIRICAL; 19yr base rate 94% / 60d for ≥15% VIX rise.
- Concentration-unwind formalized as **parallel transmission path** (KB-VIO-071): hot-NFP rate-shock universe DEFLATES VIX historically; 6/5 +40% required amplifier (AI/factor concentration unwind). Vol event can fire via HENRY-side breadth cascade without credit confirmation.
- R12 regime **interrupted-and-resumed** structure recognized (KB-VIO-072): 5/12 termination → 6/05 vol event → 6/05 regime re-establish at 20d-avg 140.16. New classification "elevated SKEW under live vol event."
- KB-VIO-031 60d window RESOLVED HIT (Scenario B confirmed; VIX +39.7% at td-58 of 4/15 fire window). KB-VIO-058 ARCHIVED (PRE_EVENT_FADE was wrong framework not direction).
- Predictions table: #3 CLOSED INCONCLUSIVE; new #5 (L1 DIET → ≥15% VIX in 60d, PARTIAL HIT 6/5) and #6 (post-spike SKEW >150 sustained → back-to-back vol event) added.
- Trade Implications gains 3rd pattern: **DIET Coiled-Spring Trade** (L1 operational entry).
- Crisis Analogs gains **2026-06-05 NFP-shock + AI/factor concentration unwind** episode.

**v3.2 (2026-06-01) — Diet coiled-spring + GEX-suppression hypothesis as live analytical product**
- KB-VIO-062 filed (DIET coiled-spring + GEX-suppression, ASSUMPTION-grade at filing-time; upgraded to EMPIRICAL via KB-VIO-067 backtest same day).
- R11 PRE_EVENT_FADE analog confirmed DEAD; GRADUAL_FADE or POST_EVENT_PERSIST realized.
- Stage-2 trap framing intact; imminence read materially weaker than 5/13 / 5/21.
- (Originally filed as v3.1 in thesis/CHANGELOG.md on 6/01; mislabel corrected to v3.2 on 6/06 per v3.3 changelog entry.)

**v3.1 (2026-04-15)** — First empirical audit against 20y VIX/VIX3M history (4,968 days). Regime distributions confirmed; COMPLACENCY (VIX<15) added as distinct bucket; Prediction #2 FALSIFIED (KB-VIO-034); inherited hit rates flagged as four-model-derived not VIOLET-validated; Mar 18-Apr 8 2026 episode added (KB-VIO-030).

**v3.0 (2026-04-12)** — Four-model synthesis (Gemini, Perplexity, Claude, Grok).

---

## OPERATIONAL LAYER STACK (added v3.3)

Live signals are organized into four layers; only L1 is the real-money signal as of v3.3.

| Layer | Role | Status as of 6/6 | Evidence |
|-------|------|------------------|----------|
| **L1 — Population framework** | Backtest-derived signature: SKEW rises + VIX falls + VVIX falls over multi-day window. | **REAL-MONEY** (EMPIRICAL). 94% hit rate ≥15% VIX rise in 60d (KB-VIO-067 19yr backtest). PAID FORWARD 5/20-5/29 → +40% VIX at td-4. | KB-VIO-036, KB-VIO-067 |
| **L2 — Regime-context filter** | Absorbed-trap classification: consensus-aligned catalysts get absorbed; only consensus-miss prints break the trap. | **WRONG-MECHANISM** as of 6/5. Consensus-miss carve-out pending (define σ threshold + backtest). | KB-VIO-069, KB-VIO-070 |
| **L3 — Direction matrix** | M1:M2 contango × VIX direction quadrant map (Q1-Q4). Q3 (M1:M2 expansion + VIX rising) new quadrant. | **PROVISIONAL N=1.** Resolve via pre-FOMC-week historical scan. | KB-VIO-068, KB-VIO-070 |
| **L4 — Compound confirmation** | CFTC TFF Lev Money positioning as discriminator between event-hedger-bid vs speculator-crowding mechanisms. | **DEMOTED — descriptive only.** Tuned to discriminate short-vol unwind / Volmageddon-shape; got bypassed when actual mechanism shifted (NFP+AI). | KB-VIO-065, KB-VIO-070 |

**Discipline rule:** L1 fires the trade; L2-L4 are calibration filters that may bypass when the dominant mechanism shifts. Do not require L2-L4 confirmation if L1 has fired; do not size positions on L2-L4 signals alone.

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

> 📌 **Operational refinement (v3.3):** The four conditions above remain the **entry-filter** for the lag trade. The **fire signal** within that filter is the L1 DIET coiled-spring signature (KB-VIO-067, VIOLET-backtested 19yr): SKEW rises + VIX falls + VVIX falls over a multi-day window. L1 is the population framework that determines *when* the lag is paying forward; the four conditions determine *whether the regime is right* for the lag to exist at all. Use both: conditions = regime gate; L1 = fire trigger.

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

**Implication:** This is the *pre-stress* regime — the volatility paradox zone where complacency builds up structural risk. Most actionable for strategic credit-vol lag positioning.

### Low Vol Regime (VIX 15-20)
| Characteristic | Value |
|----------------|-------|
| Days observed | 1,550 (31.2% of time) |
| Credit-VIX correlation | 0.06 (weak) |
| Lead-lag | **Credit leads by 3-8 weeks** |
| Term structure | Contango |
| Signal quality | **High** — actionable lag window |

**Implication:** Active monitoring zone. Credit stress starts becoming predictive.

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

### Regime Life-Cycle: Interruption-and-Resumption (added v3.3, KB-VIO-072)

The 20d-avg ≥ 140 elevated-SKEW regime definition (KB-VIO-043) treats regime termination and re-establishment as discrete binary events. R12 (2025-06-16 → 2026-05-12, 222 td) terminated cleanly 5/12; **re-established 6/05 at 20d-avg 140.16 after a 24-td gap.** The vol event (VIX +40%) fired *concurrent with* the re-establishment, not in the post-termination window predicted by R11 PRE_EVENT_FADE analog (which would have placed the spike at td-8 from termination; actual lag td-18).

**Open question:** Does the 24-td gap count as a full regime end (cohort-comparison perspective — R12 ends, a new "R13" starts on 6/05) or as a single regime with an interruption (continuous-regime perspective — R12 is now 222+1 td with a 24-td hole)? KB-VIO-044's historical regime-life-cycle catalogue has no analog for this sequence. **Operational implication:** Don't compound regime-length statistics across the gap until this is resolved. Deferred for research.

---

## THE TRANSMISSION CHAIN

Two paths now formal (v3.3 update). Path A is the canonical credit-led chain; Path B is the parallel concentration-unwind path identified via the 6/5 NFP-shock live test.

### Path A — Standard credit-led (canonical)

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

**Path A fires when:** four conditions hold (VIX<20 at onset, credit-originated shock, cross-sector widening, no curve inversion). Credit leads by 2-6 weeks tactical / ~7 months cyclical. **This remains the high-confidence path.**

### Path B — Concentration-unwind parallel (added v3.3, KB-VIO-070/071)

```
Macro trigger (rate-shock, geopolitical, surprise data)
    ↓
HENRY (Single-name / factor concentration cascade — NVDA, SMH, AI factor)
    ↓
VIOLET (Vol amplification via single-name vega + 0DTE flow)
    ↓
Portfolio P&L (no credit-side firing required)
```

**Path B fires when:** standard-Path-A conditions are NOT met (credit flat, no cross-sector widening) but HENRY-side concentration risk is high (top-N market cap concentration > historical threshold, single-name vega-weighted index influence > threshold). Trigger amplifies through HENRY → VIOLET without LIQUID confirmation. **Hot-NFP-rate-shock historical universe (KB-VIO-071):** rate-shock alone deflates VIX 16/20 days; amplifier required. 6/5 +40% VIX day is the canonical Path B example: NFP triggered, AI/factor concentration unwound, VIX spiked without HY OAS moving.

**VIOLET's role across both paths:** Detect regime shifts, credit-vol divergences (Path A), AND concentration-vol amplifications (Path B). Signal when vol markets are mispriced relative to either source of stress.

**Operational rule:** Path A signals (LIQUID upstream) get high confidence and standard sizing. Path B signals (HENRY upstream) get medium confidence and reduced sizing until backtest matures. Don't require Path A confirmation when Path B is firing — the 6/5 episode proves they can be independent.

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

**Jun 5 2026 NFP-Shock + AI/Factor Concentration Unwind (*added v3.3, VIOLET live-test canonical*)**
- Trigger: May NFP 172k vs 88k cons (+95% beat); March/April revisions +93k; DGS2 +6-7bp; Dec hike odds 26% → 43% in one day.
- VIX: 15.40 → **21.51 (+40% 1d)**; worst SPX day since October (-2.64%).
- Nasdaq -4.1%; NVDA -6%; memory chip ETF -15%; VVIX +19% to 102.04 (first sustained >100 in 2026); SKEW +10.10pt 1d to 152.25.
- HY OAS: 2.74 flat through window. Credit DID NOT crack. Gold -3.65% (rate-shock signature, not flight-to-safety).
- **Lead:** VIX-led; no credit confirmation. Path B (concentration-unwind parallel) — NOT Path A.
- **Mechanism:** NFP triggered; AI/factor concentration amplified. Hot-NFP-rate-shock historical universe (KB-VIO-071) deflates VIX (16/20 fell/flat 2010-2026). Without the concentration-unwind amplifier, today would have been a -2 to -5% VIX day, not +40%.
- **Lesson:** Path B is real and operationally distinct from Path A. Concentration-unwind alone insufficient (needs a macro trigger); macro trigger alone insufficient (deflates historically); joint condition required. References KB-VIO-070 (L1-L4 stack), KB-VIO-071 (analog universe), KB-VIO-072 (regime re-establishment).

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

### The DIET Coiled-Spring Trade (added v3.3)

**Setup (KB-VIO-067 19yr backtest, EMPIRICAL):**
- L1 DIET signature fires: SKEW rises ≥+10pt + VIX falls ≥-5pt + VVIX falls ≥-15pt over a 20-day window (formal magnitude). Population base rate: 1.0% of days; 46 trigger days / 17 distinct episodes 2007-2026.
- *Or* directional/half-magnitude variant (KB-VIO-062 working hypothesis): same signs, smaller magnitudes — calibration pending L1 re-split by trigger type.

**Entry:** VIX calls 60-90 DTE struck near 1.3× spot VIX (matches historical median forward-60d move magnitude)
**Target:** ≥15% VIX rise within 60 days (94% historical hit rate). SKEW>150 cohort: 6/7 produced STRESS +50% (high-severity sub-trade).
**Stop:** SKEW falls below 140 sustained 4+ td during window (cohort-A peaceful resolution, 6% base rate); VIX>30 already-fired (window resolved).
**Sizing:** 2% account (L1 is real-money signal per v3.3 stack discipline; population framework with 94% hit rate justifies higher sizing than Lag or Regime Shift trades).
**Mechanism caveat (v3.3):** L1 is mechanism-agnostic by construction — fires the same whether the trigger is macro-shock, technical unwind, or concentration cascade. Timing varies widely (1 week to 3 months; median 39 days IQR 32-46). 6/5 fired at td-4 of the 60d window; not typical timing.

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

| # | Prediction | Status (6/6) | Confidence | Resolution |
|---|------------|--------------|------------|------------|
| 1 | HY OAS > 400bps + VIX 20-30 → VIX > 30 within 10 days | Untested — HY 2.74 still distant from 400bps trigger | Medium | Review when HY OAS >400 |
| 2 | ~~Term structure inversion (VIX3M/VIX<1.0) → VIX spike >50% within 5 days~~ | **FALSIFIED 2026-04-15** (KB-VIO-034: 553 events, 2.2% hit rate, mean -5% forward) | ~~High~~ → **rewritten below** | — |
| 2' | **Sustained** term structure inversion (VIX3M/VIX<1.0 for ≥7 consecutive days) → VIX sustains above 25 for ≥10 days following | Untested. Front-end inversion 6/5 (VIX9D > VIX) does NOT count — VIX3M still above spot (1.014). | Medium | Next event |
| 3 | VVIX > 120 **with VIX < 20** (divergence) → VIX > 25 within 10 days | **CLOSED INCONCLUSIVE 6/6.** 6/5 had VVIX 102.04 (not 120) but VIX cleared 20 anyway via Path B mechanism. Threshold-conditional setup doesn't capture mechanism-substitution. Replace with #5/#6. | — | Closed |
| 4 | VIX > 40 → HY OAS > 600bps within 20 days | Untested — VIX hasn't reached 40 since thesis | Medium (downgraded from High — inherited, not VIOLET-validated) | Next event |
| **5** | **KB-VIO-067 L1 DIET signature** (SKEW +10 / VIX -5 / VVIX -15 over 20d formal, or half-magnitude directional variant) → ≥15% VIX rise within 60 days | **PARTIAL HIT 6/5.** Directional/half-magnitude variant fired 5/20-5/29 → VIX +40% at td-4 (well above 15% threshold). Mechanism-attribution uncertain (NFP + AI confounder); count as partial. Population framework 94% / 60d hit rate (KB-VIO-067). | High (EMPIRICAL via 19yr backtest) | Each L1 fire; 60d window |
| **6** | **Post-spike SKEW > 150 sustained 4+ td** → back-to-back vol event within 60 days (Phase 2 cluster analog) | LIVE 6/6 (SKEW 152.25 on 6/5; need 3 more td to confirm sustained). Tests whether 2024-11/2025-01 back-to-back cluster (KB-VIO-031 phase 2 analog) is recurring. | Medium (small N: 1 prior cluster in 19yr) | 7/5 (60d from 6/5) |

**Scoring rules:**
- "Untested" = trigger conditions have not occurred
- "PASSED" = prediction fired and outcome followed within window
- "FAILED" = prediction fired and outcome did not follow
- "PARTIAL HIT" = prediction fired and outcome followed, but mechanism-attribution unclear (confound present)
- "INCONCLUSIVE / CLOSED" = threshold not hit but outcome happened via different path; prediction-structure misspecified
- "FALSIFIED" = backtest proved prediction wrong before it was tested forward

---

## RESEARCH AGENDA

**Phases 1-2 complete** — historical analysis (VIX/HY OAS correlation, regime-dependent behavior) and crisis-analog catalog (Mar 2020, Feb 2018, Feb 2021). See `research/` for backtest + analog files.

**Phase 3: Live Testing** *(in progress)*
- [x] Track credit-vol divergence in real-time (ongoing)
- [x] Paper trade lag signals — Episode-17 (4/13 → 5/19 expiry) traded the post-stress KB-VIO-031 setup; outcome: worthless (positive-gamma suppression + GEX hypothesis KB-VIO-062)
- [x] L1 DIET coiled-spring 19yr backtest (KB-VIO-067 — 2026-06-01)
- [x] L1 live test 6/5: PARTIAL HIT, +40% VIX at td-4

**Phase 4: Stack Calibration (added v3.3)** *(active)*
- [ ] L2 consensus-miss carve-out: define σ threshold (1.5σ? 2σ?) + backtest the absorbed-trap mechanism
- [ ] L3 Q3 quadrant (M1:M2 expansion + VIX rising) historical base-rate scan — pre-FOMC-week conditioning
- [ ] L4 demotion formalization: COT positioning → descriptive context, not discriminator
- [ ] L1 re-split by trigger type: do DIET fires concentrate around macro-shock vs technical vs concentration-unwind?
- [ ] Path B (concentration-unwind parallel) backtest: identify historical analogs (Aug 2024 yen, Nov 2018 FANG, Feb 2018 Volmageddon, Mar 2020) and characterize joint trigger+amplifier condition

---

## CONNECTION TO SYSTEM THESIS

System thesis (Scenario D 82%): Credit stress → bank stress → equity crash.

**VIOLET's role:** Time the equity vol leg and detect regime shifts.

### Current status (2026-06-06)
- **BROCK/SHADE:** Private credit substance gradually firming; Stage-3 gates intact (verify with agent).
- **LIQUID:** HY OAS 2.74 (6/4 EOD, T+1 lag), flat through the 6/5 spike. CCC 9.46 (+5bps over 4td). IG 0.74. **Credit DID NOT crack on 6/5** — clean Path A counter-signal.
- **VIOLET:** RISING_VOL regime as of 6/5. VIX 21.51, VVIX 102.04 (first sustained >100 in 2026), SKEW **152.25** (high-severity cohort, KB-VIO-031), M1:M2 strict +15.71% (M2 event-premium hump on Jul/FOMC). VIX9D ABOVE spot (23.92 vs 21.51) — front-end inverted, but VIX3M 21.82 still above so not regime-shift-grade. **R12 elevated-SKEW regime RE-ESTABLISHED 6/05** at 20d-avg 140.16 (KB-VIO-072) — interrupted-and-resumed structure, not historically equivalent to original 222-td run.
- **HENRY:** AI/factor concentration cascade fired 6/5 (NVDA -6%, SMH/memory chip ETF -15%, Nasdaq -4.1%). Path B amplifier on rate-shock trigger.

### Current posture
**Fade-leaning with two-leg pathway** (KB-VIO-070, KB-VIO-071):
- Rate-shock leg fades by historical base rate (16/20 hot-NFP+rate-shock days didn't spike VIX to begin with).
- AI/factor concentration unwind leg has its own half-life decoupled from macro — open question.
- **Position discipline: NO short-vol before 6/12 May CPI.** Fade must clear CPI first.

### The VIX lag window opens when (Path A):
1. HY OAS breaks above 4.0 (currently 2.74, distant)
2. VIX stays below 25 (currently 21.51 ✓)
3. **VVIX > 120 while VIX < 20** (divergence form — KB-VIO-027 Pattern A)

### The Path B window opens when:
1. HENRY-side concentration metric > historical threshold (NVDA + top-10 weighting in SPX > N%)
2. Macro trigger imminent (data, FOMC, geopolitical)
3. **L1 DIET signature has fired or is actively firing**

### Open questions for next session
- Does AI/factor concentration unwind have a half-life longer than the macro fade? Tests: NVDA/SMH price action Mon-Wed, single-stock vol surface, 0DTE flow concentration.
- Will post-spike SKEW rebid (152.25 6/5) sustain ≥4 td above 150 → Prediction #6 fire?
- Does the 24-td R12 gap count as a regime end (cohort perspective) or as an interruption (continuous perspective)? KB-VIO-072 deferred research.

Until then: 6/12 CPI is the gate.

---

*Version history: `thesis/CHANGELOG.md`. v3.0 → v3.3 (2026-04-12 → 2026-06-06).*
*Status: ACTIVE — Phase 4 stack calibration in progress.*
