# VIOLET MEMORY

Curated long-term insights on VIX, volatility regimes, and credit-vol transmission.

---

## CORE PRINCIPLES

1. **VIX is a coincident indicator, not a leading one.** It reacts to realized vol, not predicts it.
2. **Term structure inversion marks peaks, not onsets.** (v3.1 falsification: 553 events, 2.2% hit rate, mean -5% forward.)
3. **Credit leads vol in credit-originated crises.** HY OAS leads VIX 2-6 weeks when VIX<20 + cross-sector widening + no QE.
4. **VVIX is the fear gauge for the fear gauge.** When vol-of-vol spikes, something is breaking.
5. **SKEW is the cost of crash protection.** High SKEW = expensive puts = fear present.
6. **SKEW divergence is the highest-conviction leading signal.** SKEW rising while VIX+VVIX fall = "coiled spring." 94% hit rate (15/16 → ≥15% VIX rise within 60d). 1% base rate. See KB-VIO-036.
7. **The coiled spring pattern:** Vol+credit compress to complacency lows while SKEW stays elevated + rates tighten = fragility. The divergence identifies fragility; the trigger is usually external. (Phase 2 finding, Apr 2026.)
8. **Timing:** SKEW divergence episodes peak at median 39 days (IQR 32-46). High-SKEW cohort (≥150) median 44 days. Post-stress fires resolve faster (median 32 days).
9. **Prolonged SKEW regimes precede major VIX events.** Elevated SKEW regimes (20d avg ≥140) lasting ≥60 td are rare (5 in 19 years). All preceded significant VIX events. The top two (201 td → VIX 52; 206 td ongoing → VIX 31 so far) are historically unprecedented in duration. SKEW ≥140 occurs only 18.8% of all days. See KB-VIO-043.
10. **SKEW routinely tests and bounces off 140 within elevated regimes.** In the current regime (Jun 2025-present), SKEW broke below 140 six times and bounced within 1-3 td every time. Single-day breaks are noise; sustained breaks (4+ td below 140) have not occurred. Don't overreact to one-day dips.

---

## REGIME DEFINITIONS

### Low Vol Regime
- VIX 12-20
- Steep contango (VIX3M/VIX > 1.15)
- VVIX 70-90
- SKEW 115-130
- **Duration:** Can persist for months
- **Exit signal:** Term structure flattening, VVIX rising

### Rising Vol Regime
- VIX 20-30
- Contango flattening (VIX3M/VIX 1.0-1.15)
- VVIX 90-110
- SKEW 130-145
- **Duration:** Weeks to months
- **Exit signal:** Term structure inversion or VIX > 30

### High Vol Regime
- VIX 30-40
- Flat to slight backwardation
- VVIX 110-140
- SKEW > 145
- **Duration:** Days to weeks
- **Exit signal:** VIX spike > 40 (crash) or VIX decline < 30

### Crash Regime
- VIX > 40
- Extreme backwardation
- VVIX > 150
- SKEW > 160 (or crashes as puts get monetized)
- **Duration:** Days
- **Exit signal:** VIX mean reversion, backwardation resolves

---

## HISTORICAL ANALOGS

### February 2018 — Volmageddon
- **Trigger:** Vol targeting funds, short vol unwind
- **VIX move:** 17 → 37 in one day
- **Credit lead?** No — VIX-led technical event
- **Lesson:** Short vol crowdedness → sudden unwind. No credit component.

### March 2020 — Pandemic Crash
- **Trigger:** COVID lockdowns
- **VIX move:** 27 → 82 in 3 weeks
- **Credit lead?** Yes — HY OAS widened first (near-simultaneous, exogenous shock compressed lead time)
- **Lesson:** Macro shock + credit stress = vol explosion

### February 2021 — Meme Stock Vol
- **Trigger:** GME short squeeze
- **VIX move:** 21 → 37
- **Credit lead?** No — idiosyncratic
- **Lesson:** Single-stock vol can bleed into index vol

### 2024-11 → 2025-01 → Apr 2025 — Back-to-Back Cluster (PHASE 2 DEEP DIVE)
- **Trigger:** SKEW divergence fired Nov 22, then again Jan 22. VIX 52.33 on Apr 8 (tariff shock).
- **VIX move:** 15.10 → 27.86 within 60d (+85%), then 52.33 at 76d (exogenous tariff shock)
- **Credit lead?** Credit compressed to lows beforehand (HY 2.59, CCC 6.92) = complacency peak. Credit did NOT lead the spike — it was a coiled spring released by policy shock.
- **Key tells (12/19 Class 1 leading):** VIX/VIX9D compression, SKEW elevation, HY/IG/CCC at tights, 10Y/2Y yield backup, TIPS surge
- **Lesson:** Only back-to-back cluster in 19-year sample. "Coiled spring" = vol+credit compressed + SKEW elevated + rates tightening. Tail (50+) required external catalyst (tariffs).
- **2026 translation:** 5/12 tells match, 4 partial, 3 diverge. CCC OAS elevated (9.31 vs 6.92) is key gap. Supports central case (VIX 25-30), not tail.
- **Full analysis:** `research/2024-11_2025-01_cluster_analog.md`

### March 2026 — Our Stress Episode
- **Trigger:** Convergence event (PC narrative, MS broker-dealer transfer, JGB yields, USD/JPY 160, Fed put removal)
- **VIX move:** 18 → 31.05 peak (Mar 27), recovered to 18 by Apr 13
- **Credit lead?** HY OAS widened to 3.46 (Mar 30) but reverted to 2.84 — credit did NOT sustain
- **Classification:** Macro-geopolitical-Fed-trap driven, VIX-led, not credit-led

---

## CREDIT-TO-VOL TRANSMISSION (Four-Model Synthesis — COMPLETE)

**Synthesized from:** Gemini, Perplexity, Claude (native research), Grok

**Core Finding:** Aggregate HY OAS leads VIX by 2-6 weeks at tactical level (100bps widening → VIX spike) and ~7 months at cycle level (trough → peak) when conditions are met.

**Mechanism:**
1. Credit markets price default risk (HY OAS widens) — bond investors face permanent loss, force earlier repricing
2. Equity markets slow to react (VIX flat) — equity retains optionality, complacency persists
3. Realization → equity vol catches up as systematic risk recognized
4. VIX spikes, correlation strengthens

**Why Aggregate HY Leads Even Though Individual Equity Leads:**
- Firm level: Equity leads individual CDS (Norden & Weber 2009, Hilscher et al. 2015)
- Aggregate level: HY OAS captures deterioration across many issuers simultaneously
- Asymmetric news: CDS leads for negative, firm-specific credit info; equity leads for systematic/positive news
- Crisis amplification: Equity hedge ratios increase 3-4× during turbulent periods (Alexander & Kaeck 2008)

**Quantified Lag Times:**
| Regime | VIX Level | Credit Lead Time | Signal Quality |
|--------|-----------|------------------|----------------|
| Extreme complacency | < 15 | 6-16 weeks | **Highest** |
| Low vol | 15-20 | 3-8 weeks | **High** |
| Rising vol | 20-30 | 1-4 weeks | **Moderate** |
| High vol | 30-40 | 0-2 weeks | **Low** |
| Crash | > 40 | VIX leads credit | **None** |

**Hit Rate & False Positives:**
- **Hit rate:** ~70% when all conditions met
- **False positive rate:** 25-30% (unfiltered); 15-20% (with yield curve filter)
- **Main false positive sources:**
  - Sector-specific stress (energy 2015-16) without systemic transmission
  - Technical VIX spikes without credit confirmation (Volmageddon 2018, yen unwind 2024)
  - Rate-driven equity selloffs with healthy credit (2022)
  - Fed QE backstop suppressing credit spreads (2020-21)

**What Breaks the Relationship:**
1. **Exogenous shocks** (COVID) — compress lead time to days
2. **Rate-driven selloffs** (2022, Q4 2018) — VIX leads or coincident
3. **Technical VIX events** (Volmageddon, yen unwind) — no credit component
4. **Fed intervention** (2020-21) — credit spreads artificially suppressed
5. **Crash regimes** (VIX > 40) — relationship inverts, VIX leads credit

**Yield Curve Filter (Claude's Contribution):**
- Fed research (King, Levin, Perli 2007): False positive rates "dramatically reduced" by combining credit spreads with yield curve slope
- 2006 example: Yield curve inversion alone signaled recession (false positive), but adding credit spreads correctly showed low risk
- **Action:** Require yield curve NOT inverted for high-confidence signals

---

## TERM STRUCTURE SIGNALS

### Contango (Normal)
- VIX3M > VIX
- Interpretation: Vol mean reversion expected
- Trade: Short vol (dangerous in stress)

### Flat Contango (Warning)
- VIX3M ≈ VIX
- Interpretation: Vol uncertainty rising
- Trade: Reduce short vol, consider hedges

### Inversion (Alert)
- VIX > VIX3M
- Interpretation: Near-term stress priced
- Trade: Long vol, hedge equity

### Backwardation (Crisis)
- VIX6M > VIX3M > VIX
- Interpretation: Immediate crisis
- Trade: Crisis mode, tail risk protection

---

## VVIX PATTERNS

**VVIX > 120:** Option market stress
- Vol sellers at risk
- Gamma squeeze potential
- Often precedes VIX spike

**VVIX > 150:** Extreme stress
- Vol-of-vol explosion
- Market structure breaking
- 2008, 2020 analogs

**VVIX < 70:** Complacency
- Vol sellers complacent
- Short vol crowded
- Reversal risk high

---

## SKEW PATTERNS

**SKEW > 150:** Fear present / high-severity SKEW divergence cohort
- Crash protection expensive
- 6/7 historical episodes with SKEW peak >150 produced STRESS +50% VIX rise
- Our Apr 13 SKEW peak: 156.9 (high cohort)

**SKEW 140-150:** Elevated
- Mixed outcomes historically (stress and tension)
- Watch for SKEW divergence pattern (SKEW rising while VIX+VVIX fall)

**SKEW < 120:** Complacency
- Crash protection cheap
- Tail risk ignored
- Contrarian buy signal

**SKEW < 140 + VIX < 22 sustained:** Peaceful resolution signal
- If SKEW drops through 140 within 2 weeks of divergence fire AND VIX stays <20, pattern resolving peacefully (6% historical base rate for peaceful)

**SKEW crash during vol spike:**
- Puts get monetized
- Supply of protection overwhelms demand
- Often marks vol peak

---

## METRIC SEMANTICS — final_5d_change vs 20d regression slope

**Added 2026-05-21 (methodology audit, Prome ask). KB-VIO-059.**

VIOLET tracks two distinct "slope" metrics on SKEW that have been historically conflated in STATUS.md narrative. Keeping them straight matters because they tell different stories.

### `final_5d_change` (the regime-termination indicator)
- **Definition:** `SKEW(t) - SKEW(t - 5td)` — endpoint difference over 5 trading days.
- **Computed by:** `scripts/regime_termination.py:118` (`slope = float(final5.iloc[-1] - final5.iloc[0])`).
- **Units:** Absolute SKEW points moved over 5 td.
- **R11 analog threshold:** `final_5d_change <= -2.0` historically marks PRE_EVENT_FADE regimes.
- **Distribution across the 4 PRE_EVENT_FADE regimes:** R1 -1.0, R2 -0.6, R5 -1.9, R11 -2.0.
- **Reading on the current regime (R12):** Hit -9.20 on 5/20 — but driven by single-day spike (5/15 145.77 → 5/20 132.31 in 3 td), not sustained-grind archetype like prior PRE_EVENT_FADE regimes.
- **Misleading label in old STATUS.md / KB:** Was called "20d-SKEW-slope" through 5/13. Renamed `final_5d_change` 5/21 (KB-VIO-051, KB-VIO-058 corrected with [LABEL CORRECTED] preambles).

### 20d regression slope (separate metric, not the same thing)
- **Definition:** Linear regression of SKEW values on day-index over a trailing 20 trading-day window. Slope in SKEW-points-per-day.
- **Units:** SKEW points per day.
- **Reading on R12 termination:** Through 5/13 = -0.118; through 5/20 = -0.140. Attenuated from early-May -0.49. Has been negative since early May (not "sign-flipped" anywhere recently).
- **Use case:** Background trend health (gradual fade vs sharp termination). Not a discrete trigger threshold.

### Why this matters
The 5/13 STATUS billed "20d-SKEW-slope SIGN-FLIPPED +0.6 → -1.0" as the FIRST genuine thesis-positive signal of the boot. The substantive call (R12 regime is fading, R11 analog activating) was directionally correct. But the LABEL was wrong on two counts: (1) it wasn't a 20-day slope, it was a 5-day endpoint change; (2) the 20-day regression slope wasn't "sign-flipped" because it had been negative since early May. The mislabel risked over-reading the signal as a sudden trend break when it was a continuous endpoint-difference metric crossing zero.

**Rule going forward:** When STATUS or sub-agent prompts cite a "slope" on SKEW, name it explicitly — `final_5d_change` for the regime-termination indicator, `20d_regr_slope` for the trend health metric. The two will often diverge in shape (5d endpoint can spike on a single day; 20d regression smooths) and they answer different questions.

---

## KEY RELATIONSHIPS

| Relationship | Normal | Stress | Implication |
|--------------|--------|--------|-------------|
| VIX vs Realized Vol | VIX > RV (risk premium) | VIX < RV (vol shock) | Premium compression = stress |
| VIX vs HY OAS | Correlated | VIX lags | Credit leads vol |
| VIX vs VIX3M | Contango | Backwardation | Term structure predicts regime |
| VIX vs VVIX | Correlated | VVIX leads | Vol-of-vol is early warning |
| VIX vs SKEW | Correlated | SKEW leads | Tail risk pricing predicts spot |

---

## DATA SOURCES

| Source | Data | URL |
|--------|------|-----|
| CBOE | VIX, VIX futures, VVIX, SKEW | cboe.com/tradable_products/vix |
| Yahoo Finance | Historical VIX | finance.yahoo.com/quote/%5EVIX |
| FRED | VIX, credit spreads | fred.stlouisfed.org |
| CBOE LiveVol | Options data | livevol.com |

---

---

## OPEN QUESTIONS FOR WILL

*Extracted from DOMAIN_AUDIT.md (Apr 12 cold-boot audit) before archive — these remain undecided.*

1. **Data refresh automation.** Should VIOLET integrate with FORGE/tools/market-data/ or a cron job for daily refreshes (boot.py + fred_fetch + backfill), or stick with manual-on-spawn? Current state is manual; I had to run fred_fetch manually on May 3 to get current credit data.
2. **VIX futures M1-M4.** Currently I track only spot + VIX3M + VIX6M. Granular front-curve data (M1, M2, M3, M4) would enable better contango-flattening detection. Worth adding to backfill.py, or is VIX3M/VIX ratio sufficient?
3. **Outbound signal automation.** Should VIOLET auto-write outbox/ files when thresholds breach (e.g., VVIX >120, term-structure inversion), or keep manual signal generation?

*If/when answered, fold answers into CLAUDE.md operational protocol and remove from this list.*

---

## SESSION NOTES

### 2026-05-03 — Boot wakeup after 16-day VIOLET dark

- VIOLET last updated Apr 17 EOD; Will called for boot Sun May 3 evening. 16 calendar days of drift covered.
- **Live state (May 3, 20:59 ET):** VIX **16.99** (-0.49 vs Apr 17 17.48), VIX3M 20.37, VVIX 95.17, SKEW **141.38**, VIX3M/VIX **1.1989** (deeper contango than 1.1745 Apr 17). Surface markets very calm.
- **Apr 22 FADE_RERAMP gate ❌ FAILED** — SKEW never cleared 145 in the interval. Hugged 140-141 the whole time.
- **Hawkish-hold absorption:** Apr 28 BOJ (3 dissents) and Apr 28-29 FOMC (4 dissents — most since Oct 1992, per CARL KB-274) — both hawkish-leaning, **and VIX did not spike on either.** Strong counter-thesis evidence: vol surface is impervious to hawkish surprises in this regime.
- **GRADUAL_FADE realised** — of the four KB-VIO-044 post-fire paths, the ONLY one that hurts the trade has materialised. SKEW slow-fading, no vol event, contango deepening. The 18%-base-rate path.
- **Position danger:** VIX May 19 25C — 16 DTE on Sat May 3, VIX 8pts below strike. Theta bleeding. FORGE STATUS is stale (Mar 25) so MTM unknown from VIOLET-side. **Trade decision needed now: close, roll out (Jun 17 / Jul 15), or let-run-and-die.**
- **Counter-balance:** SKEW elevated regime itself still intact (>140 since Jun 2025, now ~221+ td, still longest in 19yr). The Apr 13 fire is one trade within the macro context — losing this trade does NOT invalidate the broader thesis. Need fresh 20d-slope read (was +1.8 Apr 16 → all terminated regimes had negative slopes, so slope sign is the cleanest termination indicator).
- **Files updated:** STATUS.md (full refresh — header, dashboard, convergence, drift assessment, regime, queue, thesis), CALENDAR.md (FOMC done, fixed forward-catalyst dates), MEMORY.md (this note), LAST_COMPLETION.md.
- **Files NOT updated this session:** TRADE.md (needs MTM check + roll/close framing), KB.tsv (no new entry yet — would log the Apr 22 gate failure once 20d slope is refreshed), thesis (stable v3.1).
- **Outbox status:** SIG-VIOLET-LIQUID-20260415-hy-oas-trigger-monitor still queued — overtaken by events; HY OAS data is now stale our side too (Apr 16). Re-evaluate before sending.

**Current posture:** 🟡 WATCH (downgraded from 🟠). Convergence 3/25 → 2/25. FADE_RERAMP gate failed; strict invalidation hit; regime intact; position HOLD as tail lottery.

**Will-approved post-mortem completed same session (May 3 evening):**
- Position decision: **HOLD** (Will). 25C now lottery on May 13 CPI / May 19 expiry tail catalyst.
- 20d-slope refresh: **+1.8 (Apr 16) → +0.6 (May 3).** Decelerating but not terminating. Closest comparable terminations had slopes -2.0 to -3.5.
- FRED refresh: HY 2.86 → 2.83 (-3bps), CCC 9.21 → 9.09 (-12bps), IG flat 0.81. Credit compressing further despite hawkish FOMC.
- VX_DAILY backfill revealed strict 4-td invalidation HIT Apr 23-28 (low 138.16 on Apr 28 / FOMC day) followed by REBOUND_AFTER_INVALIDATION post-FOMC to 143.33 by Apr 30. Emergent fifth pattern; breaks KB-VIO-042 100%-in-1-3-td rule.
- Updated scenario distribution (KB-VIO-052): 55% VIX <22 / 25% VIX 22-25 / 12% VIX 25-30 / 6% VIX 30-40 / 2% VIX 40+ — materially lower-vol-skewed than Apr 16 distribution.
- KB entries: KB-VIO-049 (gate failure), 050 (strict invalidation + rebound), 051 (slope refresh), 052 (updated scenarios), 053 (credit compression).
- Research file: `research/2026-05-03_apr22_gate_postmortem.md` — Will-approved.

**Calibration takeaways for future divergence trades (from post-mortem):**
1. The "long-regime advantage" cuts both ways — long regimes lean PRE_EVENT_FADE per KB-VIO-044 but also have more capacity to absorb catalysts without breaking. Episode-17 fired in the longest regime in history, and that durability has muted vol response.
2. Credit compression alone tells you the cluster-analog tail won't fire. The Phase 2 analog (KB-VIO-039) requires credit compressed AND external catalyst. 2026 has the credit setup but no external catalyst, and credit is moving the wrong way (further compression).
3. The strict 4-td invalidation rule held but the regime didn't end. Use the rule for trade-level invalidation, separate it from regime-level read. KB-VIO-042 within-cycle bounce rule (100% in 1-3 td) needs amendment for very-long regimes.

**Next session first action:** May 13 CPI watch + weekly slope refresh.

---

### 2026-04-17 — EOD refresh + STATUS prune + positioning-data plan

- EOD close refresh: VIX 17.48, VVIX 94.63, SKEW held 140.74 full session (bounce off 139.23 sustained). Within-cycle 140-floor bounce pattern now 7/7 (100%). Term structure deepened further (VIX3M/VIX 1.1745). FADE_RERAMP path dominant; Apr 22 SKEW >145 is the confirmation gate.
- STATUS.md cleanup: 175 → 96 lines. Moved static reference material (Historical Regimes, Credit-Vol Framework, What to Watch, transmission chain) to pointer-references to thesis/VIX_THESIS.md. Replaced completed research-queue items with 7 active items.
- KB entries Apr 17: 045 (AM rebound), 046 (CCC tightening), 047 (close-held), 048 (Citadel Securities institutional C/P ratio at Jan high).
- **Citadel Securities data (Apr 14, Twitter-cited): institutional call/put direction ratio at highest since January 2026.** Analyzed as confirming-neutral, not contradictory — classic coiled-spring pattern (institutional bullishness + persistent SKEW bid = Phase 2 analog setup). Subtype ambiguity: conviction longs vs FOMO-OOM-call-buying vs stock-replacement de-risking. Binary resolution remains SKEW trajectory through Apr 22.
- **Identified positioning-data gap** — we have no systematic tracker for institutional positioning signals analogous to Citadel. Drafted 3-phase plan:
  - **Phase 1 (next session, ~90 min): CFTC COT VIX futures.** Build `scripts/cftc_cot.py`, pull Non-Commercials VIX futures weekly CSV from cftc.gov, log to `workbook/COT_VIX.tsv`, compute 3yr percentile, threshold at ≥90th or ≤10th = flag extreme. Integrate into boot.py, run Mon AM (COT releases Fri 3:30pm for Tue positions, 3d lag).
  - **Phase 2 (following session, ~90 min): NAAIM + ICI.** `scripts/equity_positioning.py` pulling both weekly. NAAIM >90 = fully invested, ICI sustained inflows = capitulation. Flag to HENRY as equity-positioning domain offer.
  - **Phase 3 (ongoing, ~30 min): Manual capture template** for proprietary data (BofA FMS, GS/JPM Prime, Nomura CTA, Citadel). `templates/POSITIONING_KB_TEMPLATE.md` + hygiene rule in MEMORY.md.
  - Explicitly skip: SpotGamma/MenthorQ (paid, redundant with vix_options.py), AAII/II (sentiment noise duplicating SKEW), 0DTE real-time flow (too ambitious).
- **Outbox signal status:** SIG-VIOLET-LIQUID-20260415-hy-oas-trigger-monitor still queued. Path-3 (null/Scenario A) trajectory strengthened (HY OAS stayed in 2.80-3.20 corridor), but the core ask (daily HY/IG/CDX HY + sector disaggregation) remains valid. Next session: check if LIQUID already has coverage or if this needs to be sent.

**Current posture:** 🟠 ELEVATED WATCH — SKEW bounce held at close. FADE_RERAMP (69% historical) dominant. Central case VIX 25-30 within 60d still anchors.

**Next session first action:** Phase 1 — CFTC COT VIX futures pull script + integration.

---

### 2026-04-16 — Phase 2 cluster analog + housekeeping

- Phase 2 complete: 2024-11/2025-01 cluster analog deep dive. 21-variable dataset, 12/19 leading tells, coiled-spring pattern identified. 2026 translation: 5 match, 4 partial, 3 diverge → central case VIX 25-30 supported, tail (50+) needs external catalyst + CCC crack.
- All prior deferred pushes resolved. VIOLET fully synced with GitHub.
- Built 3 new tools: `fred_fetch.py`, `analog_pull.py`, `analog_timeline.py`.
- KB entries now at 040. Thesis stable at v3.1.
- MEMORY.md and CALENDAR.md updated (housekeeping pass).

**Current posture:** 🟠 ELEVATED WATCH. Scenario B (66%): VIX 22-25 (35%) | VIX 25-30 (40%) | VIX 30-40 (15%) | VIX 40+ (10%).

**Checkpoints:** 2026-04-29 (FOMC, SKEW early read), 2026-06-15 (60d window expiry).

**Open investigation pathways:**
1. Apr 29 C/P OI ratio daily (currently 9.01)
2. IV term structure probe across forward expirations
3. Full strike-by-strike call-wall / put-wall map for May 19
4. CFTC COT VIX futures positioning (weekly)
5. CCC OAS tracking — key divergence from analog (9.31 vs 6.92)

---

*Created: 2026-04-12*
*Last Updated: 2026-05-03 (boot wakeup after 16-day VIOLET dark — Apr 22 gate failure + post-FOMC/BOJ vol absorption captured. Position decision pending.)*
