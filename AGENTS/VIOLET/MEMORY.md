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

**Conditional-NEUTRAL carries NO calming weight vs the external-catalyst tail (KB-VIO-093, 6/11).** Recent-era releases (tariff 4/2025, NFP 6/2026) launched from ≤8th pct conditional VVIX; pre-2024 releases (COVID 90th) launched elevated. NEUTRAL-until-suddenly-not is the GEX-era norm — suppressed vol-of-vol is part of the coiled-spring setup, not evidence against it. The signal is **asymmetric**: >90th conditional remains a real warning; ≤median says nothing about branch (c).

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

**Hedge-composition rotation (added 7/1/2026, KB-VIO-108):** equity put/call COLLAPSING while SKEW RAMPS = hedge demand rotating from near-dated ATM protection into far-OTM crash wings (put spreads/collars). The structure mechanically SUPPRESSES headline VIX while repricing the tail — a low VIX print under this composition is partly artifact, not calm. Read SKEW moves jointly with the P/C series before calling either "fear" or "complacency."

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

### A value carries its DATE (added 2026-06-11, KB-VIO-092)

The "+7.98% re-armed" M1:M2 read for 6/10 was the **6/9 settlement** — `vix_futures.py` defaults to `date.today()−1` and thresholds.py stamped it with the row date; every VX_DAILY m1m2 entry was T-1 vs its row label for the series' entire life. Same family as the anchor/unit rules: a fetched value carries its own as-of date through the pipeline (now mechanized: `m1m2_settle_date` column + `basis` TICK/SETTLE label + `--supersede`). Tick before 16:15 ET ≠ the daily record.

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
- **CBOE ^SKEW publishes SAME-DAY at ~17:00 ET** — ~45 min after the 16:15 VIX settle. ⚠️ **CORRECTED 2026-07-28 (KB-VIO-137): the previous entry here claimed a "T+1 lag" and that was WRONG**, in the direction that cost two sessions of an ungradeable stand-down. A boot run before ~17:00 sees the *prior* day's stamp and looks exactly like a publication lag. **Verify with CBOE's `last_trade_time`, not by the value's apparent staleness** (`cdn.cboe.com/api/global/delayed_quotes/quotes/_SKEW.json` → `last_trade_time`; the 7/27 close 146.60 is stamped `2026-07-27T17:00:19`). **Boot after 17:00 ET and SKEW is same-day; boot before it and you must say "not yet published today," never "T+1."**
- **CFTC TFF release schedule** — Tue close → Fri 3:30 PM ET release; `cftc_cot.py --boot` freshness gate treats Mon-Thu as "use prior week's Tuesday." Annual zip URL pattern is `fut_fin_txt_YYYY.zip` (NOT `fin_fut_txt_YYYY.zip`). VIX contract = "VIX FUTURES - CBOE FUTURES EXCHANGE", code 1170E1.
- **`vix_options.py` after-hours runs print OI=0** — artifact, use intraday runs for OI work. **fred_fetch DGS10/DGS2 lagging** (diagnosis queued, SCRATCH 7f).
- **⚠️ `yfinance` `fast_info['lastPrice']` SERVES A PRIOR-SESSION CLOSE WITH NO STALENESS SIGNAL** (root cause of KB-VIO-139/149, found 2026-07-30). It returns the last price that *exists*, never saying when it was struck. **`^VIX` quotes during CBOE global trading hours; `^VIX3M` / `^VIX6M` / `^VVIX` / `^SKEW` do NOT publish pre-open** — so any pre-open row silently fill-forwards those four, and a derived `VIX3M/VIX` becomes a **cross-date artifact**. The direction is the dangerous one: a fill-forward prior is too HIGH, so every 1-day change against it is **overstated — it manufactures peak-markers.** Guarded in `thresholds.py` since 7/30 (preventive + detective). **Establish a data-date from the last intraday bar; never trust `lastPrice` alone.**
- **CBOE implied-correlation `^COR1M` / `^COR3M` / `^COR30D`: yfinance has NO daily history** (`period=1mo` returns n=1) — only ~5 days of hourly bars. **CBOE's delayed-quote API gives today's print plus `prev_day_close`** (`cdn.cboe.com/api/global/delayed_quotes/quotes/_COR1M.json`). Series must therefore be **accumulated daily and cannot be reconstructed later** — that is why `implied_corr.py` runs every boot.
- **⚠️ CBOE VX SETTLEMENT — TWO ENDPOINTS ON TWO AXES; I recorded only one and drew a false conclusion (KB-VIO-158).** ① `/us/futures/market_statistics/settlement/csv/?dt=` is keyed by **TRADE DATE**, one request per date, and really is a **~12-month rolling window** — good for today, useless for history. ② `cdn.cboe.com/data/us/futures/market_statistics/historical_data/VX/VX_{EXPIRY}.csv` is keyed by **CONTRACT EXPIRY**, one file per expired contract carrying its **entire life** with a real `Settle` column, **FREE, 2013 → current.** **A multi-year VX study is neither an effort problem NOR a paid one** — `scripts/vx_history.py` builds 28,555 contract-days in ~1 minute → `workbook/VX_TERM_HISTORY.tsv`. 🔑 **This entry previously said the opposite and nearly bought a data subscription. The generalizable lesson: when a source looks limited, ask what OTHER AXIS it might publish on before concluding it cannot be done.**
- **`^MOVE` is unreliable via yfinance as a SOLE source** — it returns a lone stale bar days old. *(Re-confirmed 7/30 PM: `period=10d` returned exactly one bar, **7/17**, and no 5m bars at all.)* **Primary = investing.com; `FORGE/tools/market-data/fetch.py price MOVE` also resolves correctly since PROME's 7/30 alias fix** (verified 74.18 to the cent). ✅ **CORRECTED 2026-07-30 PM — this entry previously said "`fetch.py` prints no data-date."** That was true when written and **PROME then fixed it the same day** (`4eb65340`, crediting this defect report): the `price` output now carries an **As-of column that flags a non-today bar `⚠stale`** and, when the date is unverifiable, **keeps the value and labels it `date?` rather than suppressing it** (fail-safe: label, never hide). Verified live — `MOVE`/`SKEW` flag `2026-07-29 ⚠stale`, `VIX` reads `2026-07-30` clean. ⚠️ **The recurrence worth noting is mine, not the tool's:** this is the second time (after KB-VIO-151) that a VIOLET surface advertised a defect as OPEN for days *after another agent had fixed it* — **a stale caveat wastes exactly as much of the next session as a stale "unbuilt" does, and no freshness check can see either.**

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

### 2026-06-12 — The class catches itself twice within the hour (KB-VIO-100, -101); rotation finding holds; FRED 6/11 late
**AM (pre-FRED boot):** KB-VIO-099 ladder re-derivation closed the late-eve owed item — raw rates 11/9/9/8 of 19 stand exactly (`two_anchor_ladder.py` reproduces; Orc-verified to decimal), spot-conditioned clauses RE-DERIVED (sub-20 entries: 23 +18-21% / 24-25 +24-31% from entry / 26 +34-37%); "23 near-spent" struck; "24-25 retest budget zone" RETIRED as a STRUCTURAL CONCEPT FAILURE (anchor-bound to a near-peak entry, doesn't translate to sub-20 entries by re-marking distances). Branch-weight ROTATION surfaced from the re-derivation math — same −12.5% tape move HURT the fade (sub-20 entry economics: ~10-15% to 17.44 episode base vs unchanged historical retest precedent = +24-31% from entry = **unaffordable, not improbable**) AND STRENGTHENED the coiled-spring (vol crushed harder, SKEW R12 margin +0.85 third-straight widening into the −12.5% day = textbook compression signature). Posture rotated toward long-vol/tail away from clean fade economics; KB-VIO-091 distribution HELD per pre-registration discipline. Cross-surface audit (Tier 1/2/3) propagated to STATUS + NEXUS_BRIEF + CHANGELOG POV pivot + research pointer. Orc verification + two wording fixes (anchor discipline + probability-vs-cost distinction).

**Mid-session (Orc verification round 1 ~12:00 ET):** boot.py batch yfinance pull returned MIXED-TIMESTAMP ticks — VIX 18.57 stale-cache (~11:15 ET) alongside VIX9D from open (~21.42); implied tick ratio 1.1292 had NO coincident moment that day. Independent recompute on yfinance 1m bars at 11:59 ET (coherent within 1 min): VIX 19.45 / VIX9D 20.41 / **ratio 1.0494 marginal-through ≤1.05**. Gate-1 direction read FLIPPED ("spot leads down, gate moves AWAY" → "VIX9D leads down on overnight deal-near headline, gate flirts with passage; settle adjudicates; KB-VIO-096 Bin-B block governs regardless"). KB-VIO-100 filed.

**Mid-session (Orc verification round 2 ~13:15 ET):** the same class caught its second variant within the hour of registering the first. NEXUS_BRIEF As-of "12:30 ET" + STATUS line 3 "12:00 ET" were WALL-CLOCK PULL-TIME, not data-time — actual data was 11:59 ET. Cross-agent surface would have shipped a 30-min-stale tick labeled current. Fresh coherent re-pull at 13:03 ET data-time: VIX 18.55 / VIX9D 18.85 / **ratio 1.0162 decisively-through** (gate-1 deeper-through, not less). KB-VIO-101 filed; broadened auto-memory `finding_quote_carries_data_minute.md` authored — **a quote carries its DATA-MINUTE**, two failure modes share one discipline. **Takeaways:** (13) the discipline has to live ABOVE the agent boundary — variant-b was caught by external verifier (Orc) reading the cross-agent surface, not by the agent re-reading its own work; (14) the lesson didn't transfer to the very next stamping action even after registration — provenance discipline is mechanization-grade, not vigilance-grade. Two-variants-in-one-hour fact is what makes the auto-memory promotion earn its keep.

**Smaller propagation fix same session (Orc-flagged):** STATUS CCC−BB row carried "BB 1.70 BROKE its May-Jun range top (1.68)" — KB-VIO-098's own data invalidated this (BB printed 1.73 on 5/8, 1.69 on 5/1; 1.68 was June-only). Corrected to "re-touch of mid-May levels, NOT new territory"; A2 tree line (1.73) survives as breadth-confirmation conjoint with CCC ≥9.55. NEXUS_BRIEF row 43 also caught: two wording fixes from earlier in session ("~10-15% to 17.44 episode-base area" + "unaffordable, not improbable") had landed on STATUS/TRADE/research pointer but missed the cross-agent surface — applied. **Takeaway (15):** retraction-propagation incomplete by default — a retracted interpretation invalidates its consumers, and the consumer list must be enumerated when the retraction is filed (the propagation-misses pattern, third instance this week).

### 2026-06-11 — Sweep completed; the tree beat the print; the record corrects itself by recomputation again
**AM session (RED sweep 035/036/037 + Q3-Q6, all closed):** CHG-035: 9.55 provenance dug — it was a bare June-range-break level (episode high 9.52+3bp) mislabeled "LIQUID tripwire" (LIQUID's line is 1000bp); the 2-bin tree (composition-artifact vs credit-confirms, CCC−BB dispersion ≥8.00 / BB ≥1.73 / CCC ≥9.65 escalator) was **registered before the FRED print existed** — the print hadn't even published by session time. CHG-036: 0.85→0.75 (absorbed-streak struck), translation layer registered (HAWK-C ≠ premium deflation; x≈0.45), fade re-marked **~20-26%** with attribution split between RED's structural point (majority) and overnight escalation. CHG-037: conceded and SHIPPED — the owed settle re-pull found "+7.98% re-armed" was the *6/9* settle (T-1 tool default, systematic for the series' life); actual 6/10 settle +3.74%, M1 absorbed the war premium, M2:M3 half-deflated to 1.81%. Q6: VVIX-conditional-NEUTRAL retired from calming work (recent-era releases launch from ≤8th pct conditional). Overnight: US strikes day 2, IRGC Hormuz closure declaration (AJ-verified), OVX/VIX gap re-opened with equity vol easing. **Takeaways:** (6) pre-registering a decision tree *before its trigger data exists* is the cheapest possible insurance against adjudicating under fire — the whole point of CHG-035, executed cleanly because the print happened to lag; (7) a value carries its DATE (the T-1 settle default) — vigilance never caught it, one mechanical re-pull did; (8) when a "calming" discriminator gets used in three places, test its discriminating power on both outcome classes before it does more work (the KB-VIO-088 lesson recurring within one sweep — now twice in two days).

**Evening (the cross fires, the tape reverses, the gate×tree gap):** CCC 9.57 crossed at midday → tree's first live fire → Bin B, mechanical, zero discretion (KB-VIO-094); by the close the tape had crushed the entire war premium INTO kinetic headlines (VIX 19.44 −12.5%, third headline-vs-tape reversal in 36h — market called the Hormuz closure theater). Orch verification flagged all forward-looking midday numbers stale; ladder re-mark trigger fired (computing-spot 22.22 → 19.44). Gate×tree interaction registered flat the same evening (KB-VIO-096). **Takeaways:** (9) **two registered artifacts referencing the same number can silently disagree about its meaning** — the entry gate (6/9) said "CCC <9.55" as a binary while the tree (6/11) graded the cross Bin A/B; the interaction rule has to be registered too, and re-marks must move BOTH (one source of truth per line); (10) a recommendation carries its tape — the midday 1% hedge rec was priced for VIX 21.5 and expired by the settle; on violent days, re-verify before acting on any intraday-stamped advice, including your own.

**Late-eve (Will working session: the extended pull, the RED challenge, the freshness audit):** Will asked what else FRED's 6/10 vintage held → extended pull (BBB, Euro HY, EM HY, rates, breakevens) found the June widening US-local (KB-VIO-097) — then RED's live challenge (pre-formal CHG-RED-038) landed within the hour and the magnitude backtest confirmed RED: ladder moves 68-78th pctile, the divergence configuration already ran 5/11-19 without consequence, BB round-tripped May. Interpretation retracted, odds restored, abandon condition registered (KB-VIO-098). Tooling: fred_fetch +credit_ladder/+credit_global groups (the tree's own lines weren't scripted — tool lagged framework by 2 days). Freshness audit then refreshed SKEW 20d-avg (140.85, margin +0.85, 3rd straight widening INTO the crush — coiled-spring component re-forming) and the 6/11 strip (M2:M3 re-armed 1.81→3.47%). **Takeaways:** (11) **texture that raises a question is not texture that answers it** — the tell was shading a registered mark (55-60→45-55) before the registered discriminator (LIQUID movers) returned; third instance of an untested inference doing confirmatory work in 48h (after run-length and VVIX-NEUTRAL — the failure class survives even while you're cataloguing it); (12) when a decision tree gets registered, its trigger lines go into the scripted fetch the same day — ad-hoc pulls of load-bearing lines are how a T-1-style drift gets a sibling.

### 2026-07-01 — Five-day-gap boot: first Bin-A, the paying trade the tree killed, wings-rotation suppression

Boot after 6/24-6/30 dark found three shocks at once: VIX 16.59 (6/23 spike fully retraced), SKEW 154.82 (top-decile, +15.4/3 sessions), credit tree in first-ever BIN-A (CCC 9.70/disp 8.06; DISH DBS prepack = idiosyncratic contributor, LIQUID breadth decisive). 5-thread workflow reconstruction; thesis → v3.6; Reversion Fade FALSIFIED per registration. **Takeaways:** (16) **a detector's "no fire" carries its data span** — diet_coiled_spring.py's cache ended 6/1; citing its output as a live no-fire would have been a stale-span error; the live check was recomputed manually from fresh closes (same family as tool-default-asof drift, new variant: backtest-cache staleness). (17) **when a registered kill-switch fires against a paying framework, record the counterfactual cost as a datum ON the switch — don't relitigate the verdict** — the Reversion Fade's directional call paid in full (VIX 19.49→16.59, target 16-17) while Bin-A killed it; verdict held, cost logged (KB-VIO-107), refinement candidate (single-issuer mask) registered for the NEXT calibration pass, not retro-applied. *(Promoted to auto-memory `[[finding_registered_killswitch_cost_datum]]` — instance record kept here.)* (18) **trigger attribution from a fast tape needs next-session re-verification** — KB-VIO-105's "SK Hynix HBM capex slowdown" framing failed web verification (actual stack: Broadcom guide-down/memory-demand/MSCI/hike-fears) and its 6/23 "closes" were intraday snapshots; the KB row now carries CORRECTED status (framing-precision family, 4th instance). (19) the convergence-score script caught a hand-arithmetic error (24 vs 23/45) — mechanical verification of declared sums earns its keep on every rewrite.

### 2026-07-23 → 07-30 — The VIXCS arc: first live VIOLET-thesis trade, and the session that fixed mechanisms instead of numbers

**The trade.** Pre-FOMC defined-risk VIX call spread (`TRY-VIOLET-VIXCS`, 4× VIXW Aug-05 20C/25C, $287.70, Will-approved 7/27) — VIOLET thesis, TERRY construction. **Closed 7/30 on its mandatory dated rule: −$111.60 (−38.8%)**, beating the registered 100%-loss base case. **Zero of five stand-downs ever tripped**; it was ended by the clock, not by a thesis kill. The FOMC delivered the exact event it was built for (VIX 17.45 → 20.88, first >20 settle of the episode) **and it still lost.**

**Calibration takeaways that survive:**
1. **A right forecast plus the wrong vehicle is a loss, and the vehicle needs checking against the forecast VARIABLE.** VIX options settle on the **forward**, whose beta to spot is **a function of tenor** — own OLS, n=246: **0.274 at 21–35 DTE · 0.505 at 11–20 · 0.591 at ≤10.** Quoting "the forward beta" as a scalar is itself a specification error. *(I propagated a relayed 0.28 — the 21–35 figure — onto a ≤10 DTE position across five surfaces including two published Artifacts, without re-deriving it. Re-derive load-bearing numbers even when they arrive from a trusted agent in a well-argued packet; that is precisely when the check does not fire.)*
2. **The real management gap was NO HARVEST RULE**, not the structure: every trigger required the move to go *further* (spot ≥23, ratio <1.0, SKEW crash) and **none fired on the position simply being worth more than it cost.** It went through its strike at the 7/29 close and round-tripped unharvested.
3. **A pre-registered tree earns its keep exactly when it contradicts the tape** — KB-VIO-123, locked 7/23 before the data existed, graded the dramatic 7/29 event **fade-prone**, and the tape confirmed within a session. **Resolve a tree's internal conflicts by its own stated hierarchy, and disclose where your incentive sits.**
4. **Grade the LETTER of a registered test, never your summary of it.** I ran a "two-for-two dispersion" tally for a week against KB-VIO-126, whose registration says nothing about tallies; measured properly (correlations ROSE, constituent vol FELL) it graded **the other way**. **A paraphrase drifts toward the answer you already like.**
5. **A stale surface advertising work as UNDONE wastes the next session** and is invisible to every freshness check — I carried a mechanism as "unbuilt" for three sessions while the packet saying PROME had built it sat unread in my inbox.
6. **Fix defects as MECHANISM, not content.** Six had been fixed as content; the seventh came due at a live grading decision. Five mechanisms built 7/30 (fill-forward guard · doc-cap · CANARY_MAP staleness · H3 tool · implied-corr instrument), each **tested in both directions**, because a guard's own v1 is what fails first — two of mine did, on first run.

*(Thesis v3.6 → v3.8 across this window. Full detail: `thesis/CHANGELOG.md`, KB-VIO-122..157, `MAINTENANCE.md`.)*

---

*Created: 2026-04-12*
*Last Updated: **2026-07-30** (July arc added — the VIXCS trade + the mechanism session; DATA SOURCES gains four hard-won instrument caveats: yfinance `lastPrice` has no staleness signal, `^COR*` has no daily history, **CBOE VX settlement publishes on TWO axes and the contract-keyed one is free back to 2013 — corrected same day after the first version asserted the opposite**, `^MOVE` needs a corroborator). Prior: 2026-07-01 (takeaways 16-19 — detector data-span, kill-switch cost datum, fast-tape attribution re-verify, mechanical sum check. SKEW PATTERNS gains the hedge-composition rotation entry [KB-VIO-108]. Prior: 6/11 late-eve takeaways 11-12.)*
