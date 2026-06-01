# VIOLET SCRATCH — June 1, 2026 (evening session)

**Purpose:** Ephemeral session handoff — canonical "where are we / what next." Read at boot, rewritten at closeout. Persistent learnings → `MEMORY.md`; dated catalysts → `CALENDAR.md`.

---

## EVENING SESSION (6/1 ~18:00-20:00 ET — post-power-loss recovery)

**Will lost power mid pass-4 closeout; verified all 5446b64e commits pushed to origin — no work lost.**

- **Fresh boot via boot.py:** VIX 16.05 (+0.12 since EOD), VVIX 91.6 (flat), SKEW 142.46 (-1.72 from 144.18). Knife-edge math unchanged (~5td to resolve). COT no change (next refresh 6/05).
- **KB-VIO-066 added:** Deep-tail call OI concentration (65-strike) ranks #3 on 6/17 (176,503) and #2 on 7/22 (254,923). CALIBRATION CHECK: 4/17 baseline already had 70-strike at 281,828 OI ranked #3 → deep-tail call concentration is PERSISTENT not a fresh surge. What IS notable: tail concentration spans BOTH sides of 6/17 quad-event = hedgers carrying through July, not unwinding after. Corroborates KB-VIO-062 (SKEW rebid + tail-bid) and KB-VIO-064 (M2 IV event-hedger support) from positioning angle. Mid-session framing-precision correction filed: boot output "(+X%)" is %OTM-vs-spot NOT growth metric.
- **KB-VIO-067 added — DIET COILED-SPRING BACKTEST (Priority 1 closure):** Built `scripts/diet_coiled_spring.py` (re-runnable), scanned 2007-01 to 2026-06 daily ^VIX/^VVIX/^SKEW (4811 obs). STRICT signature exactly reproduced (46 days/17 episodes including open 4/13/26). DIET signature (ΔSKEW≥+10, ΔVIX≤-2, ΔVVIX≤-10, 20d, NOT also STRICT) yields 37 fires/25 episodes — comparable forward returns to STRICT (fwd60 peak>+50% hit-rate: DIET 65% vs STRICT 62% vs NEITHER 38%). **Era split shows NO GEX-suppression specificity** — DIET fires 2024-25 perform similarly to DIET fires 2012-20. KB-VIO-062 GEX-mechanism claim PARTIALLY SUPERSEDED → STATUS Call-notional/GEX vector downgraded 🟡→⚪.
- **Position implication:** DIET fires should be treated as KB-VIO-036-class signals for watch-flag purposes. Sizing discipline unchanged (catalyst-then-position; compound-confirmation entry).
- **Commits (evening):** `f27dfd0e` (KB-VIO-066) pushed; KB-VIO-067 + backtest research file + STATUS amendments pending this closeout commit.

---

## CHANGES SINCE LAST SESSION (5/21 → 6/1, 8 td)

- **VIX crushed further:** 17.39 → 15.93 (low 15.32 on 5/29). VVIX eased 94 → 89. VIX9D 13.62, deeper contango.
- **SKEW rebid hard:** 132.31 (5/20 low) → 144.18 (5/29). **+11.87 pts in 7 td.** Tail risk being repriced UP while everything else relaxes.
- **R12 SKEW regime TECHNICALLY TERMINATED 5/12** (20d-avg 139.917). 5/21 framing said "5/18-5/20" — off by 6 td. Currently 20d-avg 138.985 = **knife-edge**, -1.015 below threshold.
- **R11 analog DEAD.** 8 td post-termination window (5/28-6/02) expired today; VIX trended DOWN, zero of 7 watch-list triggers fired. GRADUAL_FADE / POST_EVENT_PERSIST is the realized path.
- **Credit substance EASED across all tiers.** HY -12bps, CCC -7bps (re-firmed +3bps last 2td), IG flat, 10Y -20bps. Stage-3 substance triggers (HY>2.90 / CCC>10.00) all FARTHER away.

## WHAT I DID THIS SESSION

**Pass 1 — Catch-up (4 phases):**
- Phased catch-up plan (Will-approved): data refresh → analytical pass → KB hygiene → STATUS rewrite. Cross-agent routing skipped per Will direction (fleet in architecture transition).
- Filed **3 calibration corrections** (5/21 directional reads were right, precision was off): termination date (off by 6td), VIX9D not "structurally extreme" (27th pct of 10y), VRP not "compressed" (67th pct = above-median).
- Discovered **diet coiled-spring pattern** 5/20→5/29: directional KB-VIO-036 signature (SKEW +11.87 / VIX -2.54 / VVIX -10.39) **without formal magnitude** — tested 5/10/15/20/25/30d windows, zero formal fires.
- Filed **working hypothesis** (KB-VIO-062, ASSUMPTION): record GEX mechanically pins VIX/VVIX legs while SKEW reprices tail. Empirically supported by SPX 5d realized 3.98%, VRP +5.68 (67th pct). Implies KB-VIO-036's 94% hit rate may have lower effective magnitude floor in current regime — UNBACKTESTED. Do not size positions on it yet.
- KB.tsv: +3 (KB-VIO-061 regime termination + knife-edge sensitivity, KB-VIO-062 diet coiled-spring + GEX hypothesis, KB-VIO-063 VRP measurement); KB-VIO-058 marked STALE with closing disposition.
- STATUS.md full refresh (130 lines, under cap). Convergence Score 8/40 → 7/45.

**Pass 2 — Closeout codification:**
- Created `SCRATCH.md` (this file) — canonical session handoff mirroring SAM/CARL/BRENT fleet pattern.
- Rewrote `CLAUDE.md` SPAWN PROTOCOL as symmetric BOOT/EXECUTE/CLOSEOUT sequence adapted from BRENT (write-back tail; auto-load is decisive). Discipline overlay added.
- Created `thesis/CHANGELOG.md` with backfilled v3.1 entry.
- Retired `LAST_COMPLETION.md` → `archive/2026-06-01_LAST_COMPLETION_final.md`. SCRATCH is canonical handoff.
- Reconciled `workbook/CATALYSTS.tsv` (pruned 8 fired rows; added 6/05/6/09/6/12/6/17 forward catalysts) + `CALENDAR.md` (reconciled to CATALYSTS as source of truth; flagged Jun 17 FOMC+SEP+VIX-quarterly convergence as highest forward gate).

**Pass 3 — VX_DAILY backfill + analytical re-read (intra-day, 16:20-16:30 ET):**
- Ran `scripts/backfill.py` (default 90d spot, 30d M1:M2). 115 → 132 rows; 5/14 → 6/1 EOD now present with VIX/VIX3M/VIX6M/VVIX/SKEW + M1:M2 steepness.
- **Caught yfinance ^VIX phantom-print on Memorial Day (5/25).** yfinance returned a ^VIX close of 16.59 on a US holiday; all four companion tickers correctly skipped. Removed the orphan 5/25 row.
- **Patched `scripts/backfill.py`** with a holiday guard: drop rows where ^VIX3M is missing (orphan ^VIX = phantom). Re-ran spot-only and confirmed 5/25 stays out. Logged in MEMORY DATA SOURCES caveats.
- CALENDAR.md `VX_DAILY.tsv time series` row updated 5/13 → 6/1.
- 6/1 SKEW EOD still empty (CBOE T+1 publication lag — next-boot refresh).

**Pass 4 — CFTC COT VIX futures pipeline build (17:00 ET):**
- Built `scripts/cftc_cot.py` (~350 lines) — fetches CFTC TFF (Traders in Financial Futures) weekly VIX positioning. URL pattern confirmed: `https://www.cftc.gov/dea/newcot/FinFutWk.txt` (latest, no header) + `https://www.cftc.gov/files/dea/history/fut_fin_txt_YYYY.zip` (historical zips, with header). VIX contract = "VIX FUTURES - CBOE FUTURES EXCHANGE" / code 1170E1.
- Schema (`workbook/COT_VIX.tsv`): report_date + open_interest + L/S/Net for dealer/asset_mgr/lev_money/other/nonrept + 3yr rolling percentiles for lev_money/dealer/asset_mgr NETs + flag (EXTREME_SHORT/ELEVATED_SHORT/NORMAL/ELEVATED_LONG/EXTREME_LONG).
- CLI: default `cftc_cot.py` (fetch latest), `--backfill` (full 2023-current rebuild), `--summary` (no fetch), `--boot` (freshness-gated for boot.py integration).
- Backfilled **178 weekly observations 2023-current** (52 + 53 + 52 + 21).
- Wired `boot.py` with `--boot` freshness gate: 0.1s overhead vs prior, only hits network when local data older than expected latest-available Tuesday.
- **Latest reading (Tue 5/26 / Fri 5/29 release):** Open Interest 384,562 | Lev Money NET -49,336 (long 65,926 / short 115,262) | **pct3y 17.9 = ELEVATED_SHORT** | Dealer NET +51,650 (76.9 pct) taking other side | Asset Mgr near-flat.
- **KEY CALIBRATION FINDING (KB-VIO-065):** Current Lev Money positioning is directionally short-vol-piled-up but ~half the depth of historical pre-spike crowding. Aug-Oct 2025 peak = pct 0-1.4 / -90 to -106k contracts (long elevated-SKEW regime grind). Mar 2026 pre-spike = pct ~13 / -64k contracts. Today = pct 17.9 / -49k. **M1:M2 price evidence (13% contango, KB-VIO-064) currently MORE extreme than COT positioning evidence (pct ~18, mid-elevated).** Two interpretations: (a) NEW shorts not yet in 5/26 COT — 6/05 release for 6/02 positions disambiguates; (b) M1:M2 partly M2-event-hedger-bid-driven not pure M1-crushing (consistent with KB-VIO-062 conjecture).
- **Disambiguation event scheduled: Fri 6/05 3:30 PM ET COT release** for Tue 6/02 positions. If Lev Money pct3y breaks <10 = EXTREME_SHORT confirmed → M1:M2 driver = pure speculator crowding → upgrade Volmageddon-shape. If stays >15 = driver = M2-event-hedger-bid → mechanism differs, asymmetry less extreme.
- KB-VIO-065 added. STATUS dashboard new row "COT Lev Money NET (VIX futures)". MEMORY DATA SOURCES table + Known caveats updated. CALENDAR data-refresh schedule updated (CFTC row now wired). CLAUDE.md FILES table adds COT_VIX.tsv.

**Pass 3 analytical findings (Will-asked walkthrough):**
- **Front-curve contango M1:M2 EXPLOSION** — biggest finding. 5.66% (5/15) → 12.93% (6/1), peaked 13.40% on 5/29. Front (Jun, pre-FOMC) crushed; M2 (Jul, post-FOMC) refuses to compress. Volmageddon 2018 setup shape. Asymmetric short-vol pile-up specifically refusing to price through 6/17 quad-event (FOMC + SEP + VIX Jun quarterly). **VIX3M/VIX ratio only moved 1.159 → 1.218 (+5%) over same window — M1:M2 is ~27x more pronounced than the 3M/spot ratio.** STATUS framing materially under-weighted the asymmetry-size. KB-VIO-064 added; KB-VIO-062 amended with M1:M2 as 5th leg.
- **SKEW shape was spike-crash-rebid, not clean rebid** — 5/15 145.77 ceiling (delayed PPI reaction, 2 td post-print) → 5/20 132.31 low (NVDA-IV-crush) → 5/29 144.18. **Current rebid still BELOW 5/15 ceiling**, sitting in upper half of 12-pt range. Knife-edge re-establishment requires holding upper-third against mid-range gravity (20d-avg 138.985 = midpoint).
- **VVIX EOD bid** — STATUS 14:30 intraday showed 89.25; EOD 91.61 = +2.36 late-session move. +5.58 over 2 sessions from 5/28 low 86.03. **First 2-day VVIX bid >5pts since early May** — earliest stir of vol-of-vol leading-indicator. If 92+ by 6/05, the "no VVIX leg" piece of KB-VIO-062 weakens.
- **Convergence Score:** 7/45 → 11/50. Divergence vector renamed SKEW-VIX-VVIX-M1M2 and upgraded 🟡→🟠. New "front-curve contango / Volmageddon-shape" vector at 🟠. VVIX upgraded ⚪→🟡.
- **Action call (Will-asked): watch-flag, NOT trade-trigger.** VIOLET discipline = catalyst-then-position. Best entry condition (compound): CCC >9.50 OR HY >2.85 WITH M1:M2 still >10% = confirmation + asymmetric setup intact. Do NOT pre-position June VIX calls; they're cheap precisely because M1 is being smashed and expire 6/17 (pure theta-killer on timing). KB-VIO-064 carries the falsifiable trigger: M1:M2 ≤8% by 6/10 = trap releasing without event → downgrade; ≥10% = pile-up intensifies → upgrade asymmetry-weighted snap impact.

**Commits (all pushed to origin):** `80a10ed5` (catch-up), `ac376e9f` (SCRATCH creation), `7d8f8fb2` (closeout codification + CHANGELOG + LAST_COMPLETION archive), `fca7e6c8` (pass-2 reconciliation), `e6d02ccd` (pass-3 VX_DAILY backfill + yfinance holiday guard).

## NEXT SESSION (priority-ordered — refreshed after evening session)

1. **🟠 Episode-17 trade post-mortem** (Priority 1 residual from triple-package — only (b) backtest closed this session). Reframed by KB-VIO-067: less about GEX-suppression specificity, more about "Episode-17 was a STRICT fire that bucked the 62% peak>+50% hit-rate due to event-absorption mechanics." Needs dedicated session. Now leaner because the backtest already provides the population-level context.
2. **🟠 Feb 2018 M1:M2 Volmageddon analog** (Priority 1 residual — package piece (c)). KB-VIO-064 raises this from "watch-flag" to "trigger-bearing watch-flag" needing historical grounding. Requires extending `backfill.py` to fetch CBOE settlements for Jan-Feb 2018. Existing `research/crisis_analogs/feb2018_vix_spike.csv` has VIX/VIX3M/VVIX/SKEW/HYG/HY_OAS but no M1:M2 series.
3. **🟠 6/05 COT release disambiguation** (auto-pulled by `boot.py` on next-boot after Fri 6/05 3:30 PM ET) — KB-VIO-065 watch threshold. Cleanest near-term thesis-discriminating data point.
4. **🟠 M1:M2 daily refresh through 6/17** (~2 min/boot) — KB-VIO-064 falsifiable trigger. ≤8% by 6/10 = trap releasing → downgrade; ≥10% = pile-up intensifies. Pair with knife-edge monitor.
5. **🟡 Daily knife-edge monitor through 6/10** (~3 min/boot) — recompute 20d_avg + project re-establishment date.
6. **🟡 Diet multi-window + threshold-grid sensitivity** (KB-VIO-067 follow-on) — 7d/10d/15d/25d/30d windows × (ΔVIX, ΔVVIX) cuts to find smooth-curve equivalence with STRICT. Lower priority — calibration refinement, not thesis-shifting.
7. **🟡 6/12-6/17 catalyst pre-mortem** — Best built 6/08-6/10 once knife-edge + M1:M2 trajectory resolves.
8. **🟡 Cross-agent re-engagement** once fleet architecture work settles.

## CARRY-FORWARD (lower priority)

- KB-VIO-042 within-cycle bounce rule revision — needs amendment for very-long regimes
- Inbox 5/14 gamma signal formal disposition — content absorbed into KB-VIO-062, admin step pending
- 6/1 SKEW EOD + 6/1 FRED OAS refresh — T+1 publication lags; refresh next boot
- **vix_options.py snapshot** — last 4/17, overdue. Would inform C/P-OI shifts pre Jun 17 FOMC.

## OPEN HYPOTHESES (flagged, NOT actionable until backtested)

- **GEX-suppression specificity** (KB-VIO-062): record GEX mechanically suppresses VIX/VVIX legs of divergence pattern. **STATUS: PARTIALLY SUPERSEDED by KB-VIO-067 era-split.** DIET signature worked across full 19yr sample including pre-record-GEX eras → not regime-specific. Standalone GEX-conditional efficacy test still open (would need multi-year SPX gamma series; Spotgamma/SqueezeMetrics archive candidates).
- **Event-hedger-bid mechanism** (post-KB-VIO-067 working hypothesis): the better explanation for current M1:M2 + tail-call + DIET-but-not-STRICT signature is that hedgers are SPECIFICALLY supporting M2/Jun-quad-event/7/22 pricing while M1 is being smashed by short-vol carry. NOT a generic suppression. **Test:** 6/05 COT release — if Lev Money pct3y stays >15 = event-hedger-bid confirmed; if breaks <10 = pure-speculator-crowding.

---

*Last rewritten: 2026-06-01 19:30 ET (evening session — post-power-loss recovery confirmed clean. KB-VIO-066 tail-call OI persistence + KB-VIO-067 diet coiled-spring backtest filed. Priority 1 piece (b) closed; (a) Episode-17 post-mortem and (c) Feb 2018 M1:M2 analog now top of NEXT SESSION docket.)*
