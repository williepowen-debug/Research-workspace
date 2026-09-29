# VIOLET MEMORY

Curated long-term insights on VIX, volatility regimes, and credit-vol transmission. **Boot-read every session** (SPAWN step 3): durable learnings, regime/metric semantics, the analog pattern library. Frameworks, episode databases and live values live elsewhere — one source of truth per metric (canonical homes named per section). **Resolved correction narratives are cold: `archive/MEMORY_DATA_CAVEATS_COLD.md`.**

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

⚠️ **Source-citation discipline (2026-08-04):** every row names its corpus under `research/`, and must keep doing so — **a live doc that cites nothing makes its own sources look retirable** to the >60d sweep. *(The near-miss that established this: `archive/MEMORY_DATA_CAVEATS_COLD.md`.)*

⚠️ **Gap noted, not closed (2026-08-04): the 4 Aug 2026 SKEW configuration has no analog here.** SKEW at a 3-year low (126.41, 0.3rd pct), VIX 16.50, index at a record close — crash protection dumped INTO a melt-up, the inverse of the coiled spring, and *not* the catalogued "SKEW crash during a vol spike" (there was no spike). **Recorded as unmatched rather than forced into the nearest row.** → KB-VIO-186.

| Episode | Trigger class | Credit lead? | Lesson |
|---|---|---|---|
| Feb 2018 Volmageddon | Technical — short-vol crowdedness unwind | No | Positioning unwinds need no credit component; watch vol-product structure, not spreads. *Sources: `research/crisis_analogs/feb2018_vix_spike.md` + `.csv`; M1:M2 study `research/2026-06-01_feb2018_m1m2_volmageddon_analog.md`* |
| Mar 2020 COVID | Exogenous macro shock | Yes, near-simultaneous (shock compresses lead time to days) | Macro shock + credit stress = vol explosion; lead-time discipline breaks in exogenous shocks. *Sources: `research/crisis_analogs/mar2020_pandemic.md` + `.csv`* |
| Feb 2021 meme squeeze | Idiosyncratic / single-stock | No | Single-stock vol can bleed into index vol without systemic content. *Sources: `research/crisis_analogs/feb2021_meme_stocks.md` + `.csv`* |
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
| Backwardation (short-dated volatility above longer-dated volatility) | Crisis-coincident | Crisis confirmation, not foresight |

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

**SKEW > 150:** Fear present / high-severity divergence cohort — crash protection expensive; 6/7 historical episodes with a SKEW peak >150 produced a STRESS +50% VIX rise.

**SKEW 140-150:** Elevated
- Mixed outcomes historically (stress and tension)
- Watch for SKEW divergence pattern (SKEW rising while VIX+VVIX fall)

**SKEW < 120:** Complacency — crash protection cheap, tail risk ignored, contrarian buy signal.

**SKEW < 140 + VIX < 22 sustained:** Peaceful resolution signal — SKEW through 140 within 2 weeks of a divergence fire with VIX <20 = resolving peacefully (6% historical base rate)

**SKEW crash during a vol spike:** puts get monetized, supply of protection overwhelms demand — often marks the vol peak.

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
| CFTC TFF | VIX futures positioning (weekly, Tue-snap, Fri-release) | cftc.gov/dea/newcot/FinFutWk.txt + files/dea/history/fut_fin_txt_YYYY.zip |

**Known data caveats:**
- **^VIX phantom-prints on US market holidays — AND THE SOURCE IS CBOE, NOT YFINANCE (KB-VIO-247).** CBOE's own `VIX_History.csv` publishes a VIX close on days the US equity market was closed — 13 such dates over 2025-01-01→2026-09-04, every one a market holiday. yfinance inherits it; every ^VIX consumer inherits it. **Switching to the publisher of record does NOT escape this defect.** **Discriminator, exact at the source: 13/13 caught, 0 false positives** — on a phantom date VIX is published and `^VIX3M`/`^VIX6M`/`^VVIX`/`^SKEW`/`^VIX9D` are **all** absent. **Orphan ^VIX = phantom; a real session publishes companions.** Enforced in `backfill.py` and `scripts/vx_daily_gapcheck.py`. *(Why this entry once blamed yfinance, and why the attribution mattered: `archive/MEMORY_DATA_CAVEATS_COLD.md`.)*

- **CBOE daily-prices CSVs are the PUBLISHER OF RECORD for all six spot columns — free, complete, key-less** (`cdn.cboe.com/api/global/us_indices/daily_prices/{VIX,VIX9D,VIX3M,VIX6M,VVIX,SKEW}_History.csv`). **Use them, not yfinance, for anything graded** — yfinance has two `^SKEW` defect modes (omission + wrong value) and **no** daily history at all for `^VIX9D`/`^VIX3M`/`^VIX6M` (226 of 416 term-structure cells sat blank until 2026-09-06). `backfill.py`'s CBOE pass runs second and **wins** — fills blanks *and* corrects disagreements, printing every correction. Layout differs: OHLC indices expose `CLOSE`, VVIX/SKEW a column named for the index. → KB-VIO-246/247/248
- **FRED OAS T+1 publication lag** (KB-VIO-060). Latest available FRED HY/CCC/IG OAS is always T-1 close, not same-day. Cite the FRED data-date explicitly, not "today."
- **CBOE ^SKEW: GRADE WHEN THE DATED BAR EXISTS; NEVER SCHEDULE OFF AN ASSUMED HOUR.** The publication schedule is **UNVERIFIED**. Verify with CBOE's own `last_trade_time` (`cdn.cboe.com/api/global/delayed_quotes/quotes/_SKEW.json`), **not** by the value's apparent staleness — a boot run early in the evening sees the prior day's stamp and looks exactly like a publication lag. What is evidenced: the value existed by 18:30 ET the same evening (n=1, 2026-07-27, own `VX_DAILY` `source_ts`). **Inspect the actual dated quote/archive on every pull; neither the clock nor a successful prior-day pull proves today's close is published.** An intraday-bar witness cannot certify an EOD-only series (KB-VIO-283). *(This entry has been WRONG TWICE — a false "T+1 lag" and a false "~17:00 ET" hour, the second of which this desk wrote onto a live gate row as a "correction." Both versions and why each failed: `archive/MEMORY_DATA_CAVEATS_COLD.md`. KB-VIO-137/269.)*

- **CFTC TFF release schedule** — ⛔ **DO NOT ENCODE A CALENDAR RULE FROM THIS LINE** (KB-VIO-243; a guard was built on it three times, wrong each time). Report dates are **usually** Tuesdays, releases **usually** Friday 15:30 ET — **usually is not a schedule.** Holidays can delay a release, and the report date is **not** shifted Tue→Wed by a Monday holiday. **The staleness rule uses observed cadence + a grace window and synthesizes no calendar at all.** *(Evidence and the three failed guards: `archive/MEMORY_DATA_CAVEATS_COLD.md`.)* If precision is ever needed, ingest CFTC's published release calendar — do not re-derive one. Annual zip URL pattern is `fut_fin_txt_YYYY.zip` (NOT `fin_fut_txt_YYYY.zip`). VIX contract = "VIX FUTURES - CBOE FUTURES EXCHANGE", code 1170E1.
- **`vix_options.py` after-hours runs print OI=0** — artifact, use intraday runs for OI work. **fred_fetch DGS10/DGS2 lag** — was flagged with a diagnosis queued; **not reproduced 2026-09-28** (cache frontier 9/25 = FRED's own frontier on a direct pull). Treat as unconfirmed; the old "SCRATCH 7f" pointer is dead.
- **⚠️ `yfinance` `fast_info['lastPrice']` SERVES A PRIOR-SESSION CLOSE WITH NO STALENESS SIGNAL** (KB-VIO-139/149). It returns the last price that *exists*, never saying when it was struck. **`^VIX` quotes during CBOE global trading hours; `^VIX3M` / `^VIX6M` / `^VVIX` / `^SKEW` do NOT publish pre-open** — so any pre-open row silently fill-forwards those four and a derived `VIX3M/VIX` becomes a **cross-date artifact**. The direction is the dangerous one: a fill-forward prior is too HIGH, so every 1-day change against it is **overstated — it manufactures peak-markers.** Guarded in `thresholds.py` since 7/30. **Use the publisher's own timestamp and value together; never trust `lastPrice` alone.**
- **CBOE implied-correlation `^COR1M` / `^COR3M` / `^COR30D`: yfinance has NO daily history** (`period=1mo` returns n=1) — only ~5 days of hourly bars. **CBOE's delayed-quote API gives today's print plus `prev_day_close`** (`cdn.cboe.com/api/global/delayed_quotes/quotes/_COR1M.json`). Series must therefore be **accumulated daily and cannot be reconstructed later** — that is why `implied_corr.py` runs every boot.
- **CBOE VX SETTLEMENT — TWO ENDPOINTS ON TWO AXES (KB-VIO-158).** ① `/us/futures/market_statistics/settlement/csv/?dt=` is keyed by **TRADE DATE**, one request per date, a ~12-month rolling window — good for today, useless for history. ② `cdn.cboe.com/data/us/futures/market_statistics/historical_data/VX/VX_{EXPIRY}.csv` is keyed by **CONTRACT EXPIRY**, one file per expired contract carrying its entire life with a real `Settle` column, **FREE, 2013 → current.** `scripts/vx_history.py` builds 28,555 contract-days in ~1 minute → `workbook/VX_TERM_HISTORY.tsv`. 🔑 **Generalizable: when a source looks limited, ask what OTHER AXIS it might publish on before concluding it cannot be done.** *(This entry once said the opposite and nearly bought a data subscription: `archive/MEMORY_DATA_CAVEATS_COLD.md`.)*

- **`^MOVE`: investing.com is PRIMARY; yfinance is unreliable as a SOLE source** — it returns a lone stale bar days old (`period=10d` once returned exactly one bar, 13 days stale, and no 5m bars at all). `FORGE/tools/market-data/fetch.py price MOVE` also resolves correctly; its As-of column flags a non-today bar `⚠stale` and, when the date is unverifiable, keeps the value and labels it `date?` rather than suppressing it (fail-safe: label, never hide). ⚠️ **The recurrence worth remembering is mine, not the tool's: twice a VIOLET surface advertised a defect as OPEN for days *after another agent had fixed it*. A stale caveat wastes exactly as much of the next session as a stale "unbuilt" does, and no freshness check can see either.** (KB-VIO-151.) *(Full correction trail: `archive/MEMORY_DATA_CAVEATS_COLD.md`.)*
## SESSION NOTES — trajectory log → **COLD, on-demand**

> **Moved 2026-09-02 to `archive/MEMORY_SESSION_NOTES_COLD.md`** (verbatim, 21,363 B) under the READ-CAP ruling — **not a boot read.** Arc: 2026-04-16 → 2026-07-30. Durable lessons already live above in CORE PRINCIPLES / SKEW PATTERNS / METRIC SEMANTICS / DATA SOURCES.

## September 14 sweep — durable clarifications

- **Price changes do not trace money transfers.** Front-end volatility falling while tail pricing rises does not by itself demonstrate the same premium or traders moving between tenors. Identify price evidence, flow evidence and causal inference separately.
- **Roll adjustment precedes expiration.** The current VX helper uses calendar DTE <5; compare both symbols and settlement dates before differencing its adjusted output. The frozen September letter’s roll-date error is documented in a separate erratum.
- **Consensus is a separate input.** Actual core CPI decelerating year over year does not establish an in-line or dovish surprise.
