# VIOLET MEMORY

Curated long-term insights on VIX, volatility regimes, and credit-vol transmission.

---

## CORE PRINCIPLES

1. **VIX is a coincident indicator, not a leading one.** It reacts to realized vol, not predicts it.
2. **Term structure inversion marks peaks, not onsets.** (v3.1 falsification: 553 events, 2.2% hit rate, mean -5% forward.)
3. **Credit leads vol in credit-originated crises.** HY OAS leads VIX 2-6 weeks when VIX<20 + cross-sector widening + no QE.
4. **VVIX is the fear gauge for the fear gauge.** When vol-of-vol spikes, something is breaking.
5. **SKEW is the cost of crash protection.** High SKEW = expensive puts = fear present.
6. **SKEW divergence is the highest-conviction leading signal.** SKEW rising while VIX+VVIX fall = "coiled spring." Two tiers, threshold-indexed (canonical table: VIX_THESIS § L1 canonical base rates, KB-VIO-079): STRICT 94% (15/16) / DIET 92% (23/25) episode-level peak ≥+15% within 60d; at ≥+50% only 56%/60%. Quote the rate at the threshold the trade targets — never one unqualified number. See KB-VIO-036/067/079.
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
| CFTC TFF | VIX futures positioning (weekly, Tue-snap, Fri-release) | cftc.gov/dea/newcot/FinFutWk.txt + files/dea/history/fut_fin_txt_YYYY.zip |

**Known data caveats:**
- **yfinance ^VIX phantom-prints on US market holidays** (caught 2026-06-01 on Memorial Day 5/25 row: ^VIX returned a 16.59 close while ^VIX3M/^VIX6M/^VVIX/^SKEW all correctly skipped). `scripts/backfill.py` has a holiday guard that drops rows where ^VIX3M is missing — orphan ^VIX = phantom. If using a different fetch path, apply the same companion-corroboration rule.
- **FRED OAS T+1 publication lag** (KB-VIO-060). Latest available FRED HY/CCC/IG OAS is always T-1 close, not same-day. Cite the FRED data-date explicitly, not "today."
- **CBOE ^SKEW EOD T+1 lag** — boot.py SKEW print is yfinance, which trails CBOE direct by ~1 trading day. The 6/1 16:20 ET backfill found 6/1 ^SKEW still empty.
- **CFTC TFF release schedule** — VIX futures positioning data: Tue close → Fri 3:30 PM ET release. So `cftc_cot.py --boot` freshness gate treats Mon-Thu as "use prior week's Tuesday" and Fri-Sun as "use current week's Tuesday." Annual zip URL pattern is `fut_fin_txt_YYYY.zip` (NOT `fin_fut_txt_YYYY.zip` — easy to swap). VIX contract = "VIX FUTURES - CBOE FUTURES EXCHANGE", code 1170E1.

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

### 2026-05-21 — Boot after 7d gap; Stage-2-late verdict; HENRY LIAISON open; FRED-discipline propagation

- **Verdict delivered:** STAGE 2 CONFIRMED (trap maximally assembled), STAGE 3 NOT IMMINENT. R12 SKEW>140 regime likely terminated 5/18-5/20 (4/5 closes <140, low 132.31 on 5/20). R11 analog clock running, window 5/28-6/02, **but prior is 36% not 80%** — GRADUAL_FADE 18% and POST_EVENT_PERSIST 45% are also live trajectories. Calibrated label is **Stage-2-LATE**, not "Stage 3 imminent."
- **Verdict adoption: fleet-wide.** Stage-2-late call validated and adopted across 4 agents today (BROCK + REGINALD + HENRY + VIOLET). Convergence under stress is the empirical signal.
- **NVDA print absorbed cleanly.** Post-print IV crush: 5/22 ATM 37%, 5/26 ATM 30%. 20d realized 40.1% > short-dated implied = options pricing forward calm. Modest -3-4 vol-pt put-call skew, NOT tail-bid. NVDA was not a Stage-3 trigger.
- **HENRY-VIOLET LIAISON opened (Will-approved).** 7-trigger Stage 3 watch list (3 vol-side VIOLET-owned + 4 substance-side HENRY/LIQUID/BROCK-owned) relayed via outbox + integrated by HENRY (commit `15f450b1`). Confirmation rule: 2 of #1-3 fire same week as 1 of #4-7 by ~6/05 = R11 confirming. **This is now the canonical Stage 3 fire-condition matrix for the fleet.** Framing sharpening included: corrected HENRY's "R11 pathway WEAKENS" to "R11 pathway ACTIVATES with conditional prior" (transition from dormant-to-live, not weakened).
- **FRED-discipline catch propagated fleet-wide.** Direct FRED fetch (BAMLH0A0HYM2 etc.) caught BROCK's morning HY OAS cite was 1-2 days stale (BROCK cited 5/19 prints on 5/21; FRED OAS publishes T+1, so latest available is always T-1 close). Logged KB-VIO-060. Will/Prome propagated to fleet-wide FRED-fix Phases 1-3 today (dashboard convention + agent SIGs). **KB-VIO-060 is now canonical reference for the convention.** Single discipline catch → fleet hygiene fix. Lesson: ground-truth the boot-brief numbers against the primary source whenever feasible; the catch matters more than the time cost.
- **Methodology audit completed.** The metric labeled "20d-SKEW-slope" in pre-5/21 STATUS/KB was actually `final_5d_change = SKEW(t) - SKEW(t-5td)` per `regime_termination.py:118`. KB-VIO-051 and KB-VIO-058 prepended with [LABEL CORRECTED] preambles in-place; KB-VIO-059 logs the canonical methodology note; STATUS dashboard split into two distinct rows (`final_5d_change` for regime-termination indicator vs `20d_regr_slope` for trend health); durable "METRIC SEMANTICS" section added to MEMORY between SKEW PATTERNS and KEY RELATIONSHIPS. **Rule going forward:** name "slope" metrics explicitly; the two metrics will often diverge in shape and answer different questions.
- **Episode-17 VIX May 19 25C EXPIRED WORTHLESS 5/19** (VIX ~18 vs strike 25). Position closed. Mechanism candidate for clean absorption: positive-gamma suppression per KB-VIO-055 + 5/14 WALTER gamma-momentum signal (record GEX mechanically damping realized vol). **Post-mortem deferred** — needs reflection time + room for real write-up; next session.
- **Convergence Score:** 9/35 (26%) → 8/40 (20%). Score DROPPED because SKEW divergence vector downgraded (regime ended without firing) and VVIX eased rather than stressed. Stage-2 framing intact but Stage-3 imminence read WEAKER than 7d ago, not stronger.
- **Commits this session:** `1608fac2` (boot + Stage-2-late verdict + R11 watch list); `60b2e49c` (gap-fill: SKEW deferred + KB rename + FRED spot-check); this MEMORY session-log entry.

**Carry-forward for next-boot continuity:**
1. **Episode #17 post-mortem** — deferred, owed; write to `research/` with positive-gamma-suppression mechanism analysis as primary hypothesis. Cross-reference KB-VIO-055 + 5/14 WALTER signal.
2. **7-trigger watch list daily refresh** through ~6/05 — test R11 vs GRADUAL_FADE. If 2 of #1-3 fire with 1 of #4-7 same week = R11 confirming; if none fire by 6/05 = GRADUAL_FADE winning, push timing to 6/12-6/17 FOMC + SEP gate.
3. **5/21 SKEW close** — refresh next boot once CBOE EOD publishes.
4. **KB-VIO-058 staleness** — KB-VIO-058 still tagged Stale_By 2026-05-20; re-evaluate next boot whether to ARCHIVE (R12 ended, no longer ACTIVE) or keep ACTIVE as R11-analog reference.
5. **HENRY LIAISON ping-back** — if HENRY responds in his outbox with refined matrix or additional structure-side triggers (gamma flip threshold, vol-control de-risk flow), integrate.
6. **FRED-fix Phases 1-3** — fleet-wide convention now established; next boot, verify VIOLET's daily-data-refresh routine cites FRED date explicitly and accounts for T+1 publication lag.

**Calibration takeaways for the broader thesis:**
1. **Stage 2 ≠ pre-Stage 3.** Stage 2 can persist and intensify for weeks or months without transmitting to Stage 3. The trap-clinching evidence (BROCK/REGINALD/HENRY) is real; the *imminence* read is a separate question that requires firing-signal evidence (the 7-trigger matrix). Don't conflate "trap maximally assembled" with "Stage 3 next week."
2. **Positive-gamma suppression is the working mechanistic hypothesis for sustained absorption.** Five-to-six absorbed catalysts (FOMC, BOJ, CPI hot, PPI hot, NVDA, +42bps 10Y) with VIX in a tight band is not random — it's structural. The corresponding *un-pinning* event (vol-control de-risk, gamma flip) becomes the structural trigger to track in parallel with the 7-trigger matrix.
3. **Fleet hygiene catches matter more than their time cost.** The FRED-direct spot-check took 1 tool call and propagated to a fleet-wide convention fix. Cheap discipline → expensive payoff. Apply this lesson to other "accepted on authority" data flows.

**Current posture (end-of-session 5/21):** 🟡 STAGE-2-LATE. R11 analog clock running with conditional 36% prior. Window 5/28-6/02 for vol firing if R11 plays. Convergence 8/40. No open positions. Trade-thesis post-mortem deferred. Episode-17 closed.

---

### 2026-06-01 — Catch-up boot after 8td gap; R11 dead; R12 termination correction; diet coiled-spring + GEX hypothesis

- **Phased plan executed** (Will ask): (1) data refresh, (2) analytical pass, (3) KB hygiene, (4) STATUS rewrite + closeout. Cross-agent routing skipped per Will direction (fleet in architecture transition).
- **R11 analog CONFIRMED DEAD.** Window 5/28-6/02 expired today. VIX trended DOWN -1.46 in 8td post regime-end, not up. Zero of 7 watch-list triggers fired. GRADUAL_FADE or POST_EVENT_PERSIST won. KB-VIO-058 marked STALE with closing disposition.
- **R12 termination DATE CORRECTION.** 5/21 STATUS said "regime terminated 5/18-5/20"; actual technical break per 20d-avg<140 was **5/12** (139.917). 1d bounce 5/13, sustained <140 since. Off by 6 td. Regime ran 222 td (longest in 19yr). Filed as KB-VIO-061 with full knife-edge sensitivity analysis.
- **Knife-edge:** 20d-avg 138.985 = -1.015 from threshold. If SKEW holds 144 daily, regime re-establishes 6/05; if 142, 6/09. Aligns with 6/12 CPI / 6/17 FOMC. Binary resolves on 5td of incoming data — daily-refresh tool worth ~3 min/boot through 6/10.
- **DIET COILED-SPRING pattern firing 5/20-5/29.** SKEW +11.87 / VIX -2.54 / VVIX -10.39 — directional KB-VIO-036 signature WITHOUT formal magnitude. Tested 5/10/15/20/25/30d windows; zero formal fires. Closest = 7td with SKEW✅ only, VIX/VVIX at half/two-thirds threshold. KB-VIO-062.
- **Working hypothesis (KB-VIO-062, ASSUMPTION not EMPIRICAL):** record GEX (KB-VIO-055 + 5/14 WALTER gamma signal) mechanically pins VIX/VVIX legs. Empirically supported by SPX 5d realized 3.98%, 20d realized 10.09%, VRP +5.68 (67th pct = above-median, NOT compressed). If correct, KB-VIO-036's 94% hit rate may have a lower effective magnitude floor in current GEX regime — but unbacktested. **Do NOT size positions on this hypothesis until backtest exists.**
- **Three calibration corrections this session** — R12 termination date (off by 6td), VIX9D 12.59 not "structurally extreme" (27.84 pct of 10y = normal low-vol), VRP not "compressed" (67th pct = above-median). All 5/21 directional reads were intact; precision was off. **Pattern: don't let prior-session narrative substitute for fresh measurement.** Filed as KB-VIO-063 + drift-assessment meta-note.
- **Credit substance EASED across all tiers.** HY 2.86→2.74 (-12bps, 4.2%), CCC 9.48→9.41 (-7bps, 0.7%), IG flat. Bifurcation milder but directionally intact (HY eased 6x faster than CCC in % terms). CCC re-firmed +3bps last 2td (9.38→9.41) — early margin re-acceleration to watch. Stage-3 triggers (#4 HY>2.90 / #5 CCC>10.00) FARTHER away than 5/21. Credit-to-vol vector downgraded 🟠→🟡.
- **Convergence Score:** 8/40 (5/21) → 7/45 (6/1). DROPPED. One new vector added (VRP) at ⚪. Credit-vol downgraded. VVIX further relaxed. **Stage-2 trap framing intact; imminence read materially weaker than 5/21, which was itself weaker than 5/13.**
- **Commits this session:** [pending — to be filled in at closeout commit]

**Carry-forward for next-boot continuity:**
1. **Episode-17 post-mortem** (now-doubly-deferred — 5/21 + 6/1) — write to `research/` pairing with KB-VIO-062 GEX-suppression mechanism as primary hypothesis.
2. **Diet coiled-spring historical backtest** — new dedicated research thread. (a) half-magnitude divergence forward returns, (b) GEX-conditional KB-VIO-036 efficacy. Pairs with Episode-17 post-mortem (same underlying hypothesis).
3. **Daily 20d-avg refresh** through 6/10 — knife-edge resolution. Tool: simple yfinance + window math. Refresh at each boot.
4. **6/12 CPI / 6/17 FOMC catalyst prep** — first named macro test post this window. Build pre-mortem framing before 6/10.
5. **6/1 SKEW EOD + 6/1 FRED OAS** — refresh next boot (T+1 publication lags).
6. **Inbox 5/14 gamma signal formal disposition** — content absorbed into KB-VIO-062 but admin step pending.

**Calibration takeaways for the broader thesis:**
1. **Stage 2 can persist and weaken concurrently.** The trap-substance is real (SKEW rebid, GEX record, breadth narrowed) but the *imminence* read has now degraded twice — first 5/13→5/21, now 5/21→6/1. Trap framing intact ≠ Stage-3 next month. The diet-coiled-spring + GEX-suppression hypothesis is the live analytical product.
2. **Calibration corrections are cheap to file but expensive to skip.** Three corrections this session, all directional-right / precision-wrong. The aggregate cost: 5/21 framing risked over-conviction on regime imminence and vol-compression that didn't exist. Empirical-first discipline pays.
3. **Knife-edge regime status is the right uncertainty acknowledgement.** Not "regime ended" (terminated 5/12 by technical rule) and not "regime intact" (20d-avg below 140 for 14td) but "data-determined this week." Boot framing should reflect this rather than premature classification.

**Current posture (end-of-session 6/1):** 🟡 STAGE-2-LATE held. R11 dead. R12 knife-edge re-establishing. Diet coiled-spring firing without formal magnitude. GEX-suppression hypothesis is the active analytical product. Credit substance eased. Next firm test 6/12 CPI / 6/17 FOMC. No open positions. Episode-17 post-mortem owed.

---

*Created: 2026-04-12*
*Last Updated: 2026-06-01 (catch-up boot after 8td gap. R11 dead; R12 termination date correction (5/12 not 5/18-20); diet coiled-spring pattern + GEX-suppression hypothesis filed; 3 calibration corrections; convergence 8/40 → 7/45. KB-VIO-061/062/063 added, 058 marked STALE.)*
