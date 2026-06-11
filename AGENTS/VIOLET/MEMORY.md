# VIOLET MEMORY

Curated long-term insights on VIX, volatility regimes, and credit-vol transmission. **This file is boot-read every session** (SPAWN step 3); it holds durable learnings, regime/metric semantics, the analog pattern library, and trajectory-level session notes. Frameworks, episode databases, and live values live elsewhere — one source of truth per metric (canonical homes named per section).

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
9. **Prolonged SKEW regimes precede major VIX events — and can interrupt-and-resume.** Elevated regimes (20d avg ≥140) lasting ≥60 td are rare (5 in 19 years); all preceded significant VIX events. R12 (Jun 2025 →) ran **222 td — longest in 19yr** — terminated 5/12/2026, then **re-established 6/5/2026 concurrent with the +40% NFP-shock spike** (KB-VIO-072): "elevated SKEW under live vol event," a sequence with no analog in the KB-VIO-044 life-cycle catalogue. Gap = **17 td (24 calendar — the "24-td" figure in pre-6/10 docs was a calendar/td mislabel)**. Don't compound regime-length statistics across the gap until the end-vs-interruption question (KB-VIO-072 deferred) resolves. See KB-VIO-043/061/072.
10. **SKEW 140-breaks: name the metric, then judge the duration.** Two different things break at 140: (a) **daily closes** — single-day breaks are noise (within-cycle bounce pattern ran 7/7 through May 2026, KB-VIO-042), but sustained daily runs DO occur near termination: **4 consecutive td below 140 on 5/5-5/8 and 8 consecutive td on 5/18-5/28/2026** (verified from raw closes 6/10); (b) the **20d-avg** regime metric — R12's technical termination 5/12 was itself choppy (back above 140 on 5/13 and 5/15, sustained below only from 5/18). The old rule "sustained breaks have not occurred" is FALSE as of May 2026. Don't conflate daily-close breaks with 20d-avg regime termination.

---

## REGIME DEFINITIONS — pointer

**Canonical: `thesis/VIX_THESIS.md` § REGIME-DEPENDENT BEHAVIOR** (with 20-yr day-count distributions, credit lead-times per regime, and the v3.1 COMPLACENCY bucket). Quick bands for boot orientation only: COMPLACENCY <15 · LOW_VOL 15-20 · RISING_VOL 20-30 · HIGH_VOL 30-40 · CRASH >40. The classifier in `scripts/thresholds.py` and the conditional-percentile buckets in `scripts/convexity_read.py` implement the thesis section.

---

## HISTORICAL ANALOGS — pattern library (lessons-only)

**Canonical episode database with VIX paths and full tell-lists: `thesis/VIX_THESIS.md` § CRISIS ANALOGS.** This table is the boot-time classification aid: *which analog class is the live event?*

| Episode | Trigger class | Credit lead? | Lesson |
|---|---|---|---|
| Feb 2018 Volmageddon | Technical — short-vol crowdedness unwind | No | Positioning unwinds need no credit component; watch vol-product structure, not spreads |
| Mar 2020 COVID | Exogenous macro shock | Yes, near-simultaneous (shock compresses lead time to days) | Macro shock + credit stress = vol explosion; lead-time discipline breaks in exogenous shocks |
| Feb 2021 meme squeeze | Idiosyncratic / single-stock | No | Single-stock vol can bleed into index vol without systemic content |
| Nov 2024 → Apr 2025 cluster | Coiled spring released by external policy shock (tariffs) | No — credit was AT TIGHTS (complacency peak), did not lead | Compressed vol+credit + elevated SKEW = fragility; the tail (VIX 50+) required the external catalyst. Only back-to-back cluster in 19yr. Full study: `research/2024-11_2025-01_cluster_analog.md` |
| Mar 2026 stress episode | Macro-geopolitical Fed-trap convergence, VIX-led | HY widened to 3.46 but did NOT sustain | Vol can fire and fully retrace (31→18 in 3wk) when credit doesn't confirm; credit non-confirmation = event, not regime |
| **Jun 2026 NFP-shock + concentration unwind** | Consensus-miss macro trigger + AI/factor concentration amplifier (**Path B**) | **No — credit flat through the +40% spike** | Vol events can fire WITHOUT credit confirmation via breadth/concentration cascade (KB-VIO-071). Mechanism-agnostic L1 paid at td-4; all three mechanism-discriminator layers (L2-L4) failed silently — a novel mechanism bypasses discriminators, never base rates (KB-VIO-070, `research/2026-06-09_l1_l4_stack_postmortem.md`) |

---

## CREDIT-TO-VOL TRANSMISSION — pointer

**Canonical: `thesis/VIX_THESIS.md` § CENTRAL CLAIM** (four conditions, hit rates, source caveats) **+ § REGIME-DEPENDENT BEHAVIOR** (quantified lag table: complacency 6-16wk → crash VIX-leads) **+ § THE ACADEMIC NUANCE** (aggregate-vs-firm reconciliation) **+ yield-curve filter** (require curve NOT inverted for high-confidence signals). One-line version: aggregate HY OAS leads VIX 2-6 weeks tactically when the shock is credit-originated, cross-sector, VIX<20, curve not inverted — and the relationship breaks under exogenous shocks, rate-driven selloffs, technical vol events, Fed backstops, and in crash regimes (where it inverts). Since v3.3 the credit-led chain is **Path A**; the Jun 2026 episode formalized **Path B** (concentration-unwind, no credit confirmation required).

---

## TERM STRUCTURE SIGNALS

| Shape | Reading | Discipline |
|---|---|---|
| Contango (VIX3M > VIX, ratio >1.15 steep) | Normal / mean-reversion priced | Regime-consistent calm |
| Flattening (ratio → 1.0) | Vol uncertainty rising | Warning shape — watch with VVIX |
| **Inversion (VIX > VIX3M)** | **PEAK MARKER, not onset predictor** — Prediction #2 FALSIFIED (553 events, 2.2% hit rate for +50% follow-through, mean **−5%** forward; KB-VIO-034) | Inversion = stress is being *priced*, historically nearer the top than the start. Broadcast it as a peak-marker (CLAUDE.md trigger table); do NOT buy vol on inversion as an entry signal |
| Backwardation (VIX6M > VIX3M > VIX... inverted full curve) | Crisis-coincident | Crisis confirmation, not foresight |

*(Trade-direction advice removed 6/10 — the old "Inversion → Trade: Long vol" line contradicted our own falsification.)*

---

## VVIX PATTERNS

**VVIX > 120:** Option-market stress — vol sellers at risk, gamma squeeze potential, often precedes VIX spike. **Rare-trigger caveat (v3.4):** historically uncommon and especially scarce in the current GEX-suppression era — don't size watchlists as if it fires monthly.

**VVIX > 150:** Extreme stress — vol-of-vol explosion, market structure breaking (2008, 2020 analogs).

**VVIX < 70:** Complacency — short vol crowded, reversal risk high.

**Percentile discipline:** quote VVIX percentiles **conditional on the VIX bucket** (`convexity_read.py`), not unconditional — VVIX 102 is 67th pct 1yr but 46th pct conditional in the VIX 20-30 bucket (6/10 example). Unconditional percentiles overstate stress whenever VIX is elevated.

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
- **Misleading label in old STATUS.md / KB:** Was called "20d-SKEW-slope" through 5/13. Renamed `final_5d_change` 5/21 (KB-VIO-051, KB-VIO-058 corrected with [LABEL CORRECTED] preambles).

### 20d regression slope (separate metric, not the same thing)
- **Definition:** Linear regression of SKEW values on day-index over a trailing 20 trading-day window. Slope in SKEW-points-per-day.
- **Use case:** Background trend health (gradual fade vs sharp termination). Not a discrete trigger threshold.

**Rule:** When STATUS or sub-agent prompts cite a "slope" on SKEW, name it explicitly — `final_5d_change` for the regime-termination indicator, `20d_regr_slope` for the trend health metric. The two will often diverge in shape (5d endpoint can spike on a single day; 20d regression smooths) and they answer different questions.

### Episode % claims must name their anchor (added 2026-06-10, KB-VIO-083/084)

A multi-fire-day episode has no single base: first-fire, last-fire, and lowest-base anchors give materially different % readings (5/20-29 2026 episode: +23.3% vs +40.4% for the SAME 6/5 close; the +50% line = VIX 26.2 vs 22.98). The L1 canonical table's episode-level rates are **max-over-fire-day windows** (verified by exact reproduction, KB-VIO-084), so the **lowest-base fire day governs** when translating a table threshold into a VIX level on a live episode. **Rule:** every % claim about an episode carries its anchor (first-fire / last-fire / lowest-base), same as every hit rate carries its (threshold, tier, unit) tuple. VIOLET violated this twice on 6/10 — once in the thesis ("+40% at td-4," unanchored) and once in the cut's own first draft — both caught in joint review with Orch.

### Calendar days vs trading days (added 2026-06-10, KB-VIO-085)

The R12 gap was logged as "24 td" in KB-VIO-072 and the thesis; actual = **17 td** — 24 was the *calendar*-day count. Same failure class as the anchor rule: a duration carries its unit (td vs calendar), and any td-count gets recomputed from the trading calendar before transcription, not propagated from prior prose. (Caught by Orch verification pass 6/10 when the figure was about to be re-propagated into this file.)

---

## KEY RELATIONSHIPS

| Relationship | Normal | Stress | Implication |
|--------------|--------|--------|-------------|
| VIX vs Realized Vol | VIX > RV (risk premium) | VIX < RV (vol shock) | Premium compression = stress |
| VIX vs HY OAS | Correlated | VIX lags | Credit leads vol (Path A) |
| VIX vs VIX3M | Contango | Backwardation | Term structure marks regime (inversion = peak-marker) |
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
- **CBOE ^SKEW EOD T+1 lag** — boot.py SKEW print is yfinance, which trails CBOE direct by ~1 trading day.
- **CFTC TFF release schedule** — Tue close → Fri 3:30 PM ET release; `cftc_cot.py --boot` freshness gate treats Mon-Thu as "use prior week's Tuesday." Annual zip URL pattern is `fut_fin_txt_YYYY.zip` (NOT `fin_fut_txt_YYYY.zip`). VIX contract = "VIX FUTURES - CBOE FUTURES EXCHANGE", code 1170E1.
- **`vix_options.py` after-hours runs print OI=0** — artifact, use intraday runs for OI work. **fred_fetch DGS10/DGS2 lagging** (diagnosis queued, SCRATCH 7f).

---

## SESSION NOTES — trajectory log (chronological)

*Compressed 6/10: blow-by-blow lives in KB rows + research files + thesis CHANGELOG; this log keeps the arc and the calibration takeaways. The Apr 12 "Open Questions for Will" section was retired this pass — all three resolved by events: data-refresh automation → built (boot.py runs thresholds/options/COT/catalysts every spawn); M1-M4 granularity → M1:M2 adjusted contango wired into thresholds.py and load-bearing daily; outbound-signal automation → overtaken by NEXUS_BRIEF-primary + messaging overhaul (auto-memory `[[project_messaging_overhaul]]`).*

### 2026-04-16/17 — Phase 2 cluster analog + EOD discipline
Phase 2 deep dive complete (2024-11/2025-01 cluster, 21-variable dataset, coiled-spring pattern named — see ANALOGS table). Tools built: fred_fetch, analog_pull, analog_timeline. STATUS pruned 175→96 lines. Citadel C/P institutional signal read as confirming-neutral (coiled-spring consistent). Positioning-data 3-phase plan drafted → Phase 1 (CFTC COT) later built and wired into boot. Posture then: 🟠 central case VIX 25-30 within 60d.

### 2026-05-03 — Boot after 16-day dark; Apr 22 gate failed; GRADUAL_FADE realized
FADE_RERAMP gate ❌ (SKEW never cleared 145). Apr 28 BOJ (3 dissents) + Apr 28-29 FOMC (4 dissents, most since 1992) both absorbed without a VIX spike — first strong evidence of the absorption regime. Episode-17 VIX May 25C held as tail lottery (Will decision; later expired worthless 5/19). KB-VIO-049→053. **Calibration takeaways that survive:** (1) long-regime durability cuts both ways — leans PRE_EVENT_FADE historically but absorbs catalysts better; (2) credit compression alone tells you the cluster-analog tail won't fire (needs external catalyst); (3) use strict invalidation for trade-level, separate from regime-level read.

### 2026-05-21 — Stage-2-late verdict; HENRY LIAISON; FRED discipline; metric audit
Stage-2 CONFIRMED / Stage-3 NOT imminent (calibrated prior 36%, not the ~80% relayed earlier); verdict adopted fleet-wide same day. 7-trigger Stage-3 watch list opened with HENRY (canonical fire-condition matrix). FRED-direct spot-check caught BROCK's stale OAS cite → KB-VIO-060 became the fleet T+1 convention. "20d-SKEW-slope" mislabel exposed → METRIC SEMANTICS section born (KB-VIO-059). Episode-17 expired worthless. **Takeaways:** Stage-2 ≠ pre-Stage-3 (trap-assembled ≠ imminent); positive-gamma suppression became the working absorption mechanism; cheap discipline catches propagate into expensive fleet value.

### 2026-06-01 — R11 dead; R12 termination corrected; DIET hypothesis born
R11 PRE_EVENT_FADE window (5/28-6/02) expired with zero of 7 triggers fired — GRADUAL_FADE/POST_EVENT_PERSIST won. R12 termination date corrected to **5/12** (was "5/18-20"; off by 6 td). DIET coiled-spring pattern identified firing 5/20-5/29 WITHOUT formal magnitude → GEX-suppression hypothesis (KB-VIO-062, ASSUMPTION at filing; upgraded EMPIRICAL same evening via the 19-yr backtest, KB-VIO-067). Three calibration corrections filed (KB-VIO-063), all directional-right/precision-wrong. **Takeaway:** don't let prior-session narrative substitute for fresh measurement — became the CLAUDE.md discipline overlay.

### 2026-06-05 → 06-09 — The NFP shock arc: L1 pays, the stack postmortem, base rates canonicalized
**6/5:** May NFP 172k vs 80k consensus (+92k miss) + AI/factor concentration cascade (NVDA −6%, SMH −15%) → VIX +40% — the DIET fire of 5/20-29 PAID FORWARD at td-5 (last-fire anchor 15.32; KB-VIO-070). Credit stayed FLAT through the spike — Path B (concentration-unwind, KB-VIO-071) formalized as the parallel transmission path; thesis v3.3-v3.5 integrated it 6/6. R12 **re-established 6/5 concurrent with the spike** (17-td gap — see Principle 9; KB-VIO-072), resolving the knife-edge. KB-VIO-031's 60d window RESOLVED HIT (Scenario B, +39.7% at td-58). **6/9:** L1-L4 stack postmortem filed (`research/2026-06-09_l1_l4_stack_postmortem.md`): L1 promoted to real-money, L2 wrong-mechanism, L3 provisional N=1, L4 demoted — *a novel mechanism bypasses discriminator layers silently; it cannot bypass a base-rate layer.* KB-VIO-079 fixed the conflated 94% citation and canonicalized the threshold×tier×unit base-rate table into the thesis. Prediction #6 (post-spike SKEW >150 sustained) armed 6/5, lapsed 6/9 (rebid faded in 2 td). Posture into 6/10 CPI: fade-leaning two-leg, entry pre-registered and gated. **Takeaways:** (1) base-rate layers are the only mechanism-surprise-robust signal class — size from L1, let filters only *reduce*; (2) every hit rate carries (threshold, tier, unit); (3) regime metrics and vol events can resolve *concurrently* — the framework's discrete sequencing assumption (terminate → fire → re-establish) is too clean.

### 2026-06-10 — CPI resolves, Iran takes the tape; the gate works twice; the day of counting discipline
**AM:** CPI non-tail (energy >60% of the monthly increase — oil→Fed channel confirmed, KB-VIO-080) but Iran tit-for-tat opened a third vol leg overnight (KB-VIO-081); pre-registered fade gate FAILED #1 — kept a "CPI passed, sell the hump" reflex from selling war risk. **PM:** path-conditioned cut (KB-VIO-082, Orch-verified): 6/6 historical episodes with our shape touched ≥+50% ≈ VIX 23.0 → invalidation re-graded **close-and-hold** (a 23-touch is the modal path); distribution decomposed P(fade|Iran)×P(Iran) per the catalyst-vs-consequence conditional. MEMORY subtraction pass (this file, ~430→~200). **EOD:** gate FAILED #2 (ratio 1.145), invalidation not triggered (close 21.86), stand down; distribution formalized KB-VIO-087 (~40-45/35-40/15-20, Iran term HAWK-based); CCC 9.51 = 4bp from flip; VIX caught up to oil-vol all day (adverse gauge branch). **Calibration thread of the day — numbers carry their construction:** anchor naming (KB-VIO-083), max-over-fire-days episode rates (KB-VIO-084), calendar-vs-td (KB-VIO-085, six instances swept incl. a no-space variant that beat two greps). **Takeaways:** (1) pre-registration earns its keep under exactly one condition — when the reflex answer is wrong; it was, twice; (2) a verification pass that *recomputes* catches what one that *re-reads* cannot — three separate counting errors died that way today; (3) when a touch of your kill-line is the modal path, the kill-line semantics ARE the framework — grade them before the tape forces it.

**Evening (RED sweep, CHG-033/034):** Falsification architecture registered (KB-VIO-088): credit PRIMARY · time-box carries the grind-failure class · VIX>23 close-and-hold **n=5, TAIL-STOP role** — the derivation itself returned the real finding: *run-length has no discriminating power* (dest-right 2023-09 and dest-wrong 2024-12 both ran exactly 4; the 2024-12 failure lives at the window BOUNDARY). Ladder restated two-anchor (KB-VIO-089): divergence shape = FLATTENING (favorable anchor oversold 24, undersold 26+); (c) → 15-25%; die-or-double magnitude precedent (n=4: clears +109/+225/+248%, the miss never exceeded its early peak). **Takeaways:** (4) a registered trigger carries a stated ROLE, not just a number — deriving n is incomplete until you test what the instrument can and cannot catch; (5) clustering construction is part of a number's identity (DIET-only vs DIET∪STRICT moved an anchor and an episode count) — same family as anchor/unit/threshold.

---

*Created: 2026-04-12*
*Last Updated: 2026-06-10 ~3:45 PM ET (subtraction pass, SCRATCH item 7a executed early per Will: regime-defs + credit-vol transmission pointer-ized to thesis; analogs compressed to lessons-only + Jun 2026 episode added; term-structure trade advice fixed to peak-marker framing per KB-VIO-034; Principles 9-10 corrected against raw data — interrupted-and-resumed R12, 17-td gap, daily-close break runs 4td & 8td with metric named; VVIX rare-trigger + conditional-percentile notes; Apr 12 Open Questions retired resolved; session notes reordered chronologically + compressed + 6/5-9 arc added; calendar-vs-td rule added to METRIC SEMANTICS.)*
