# VIOLET STATUS

**As of:** 2026-09-28 20:46 ET (`date`), **post-close**. Market basis: the **September 28 session close** for the VIX complex (Cboe delayed-quote; **Cboe history confirmed through 9/25**) and MOVE; FRED credit **9/25**; CFTC report **9/22**. Every cell dated otherwise says so. Thesis **v4.1.1**. Dark 9/25 03:00 → 9/28 20:39 ET; this session caught up Fri 9/25 and Mon 9/28. Prior state (9/24 basis) is in git.

✅ **Cboe history caught up.** `backfill.py --spot-only`: 2579 cells agreed, **0 corrected**, 9/23 and 9/24 stamped SETTLE, **9/25 row created** (was missing — dark day). `vx_daily_gapcheck` rc=0. Leg 2 KILL now rests on the publisher of record (KB-VIO-316). 9/28 is ahead of the publisher frontier and stays provisional.

## BOTTOM LINE

🔴 **Credit widened in every rating bucket while VIX stayed under 20.** FRED OAS 9/22 → 9/25: HY **2.68 → 2.93** (+25bp), B 2.71 → 3.00 (+29bp), BB 1.56 → **1.76** (+20bp), CCC 10.75 → **11.28** (+53bp), IG 0.77 → 0.81. **The 9/24 read "only CCC moved" is superseded** — it was true on 9/23 data; by 9/25 the whole curve moved. On 9/25, HY's biggest day (+13bp), **VIX fell 5.1% to 14.87**. That is the shape my central claim says leads VIX by 3-8 weeks in LOW_VOL — **but it is ~¼ of the claim's 100bp size, and the claim's origin filter ("shock starts in credit, not rates") is doubtful:** the widening began 9/23, the same session as the 10Y +15bp / MOVE +21.5% move, and WALTER SIG-003 reads the rates move as real-yield-led. Other entry conditions MET: VIX <20, cross-sector, curve not inverted (2s10s **+36bp** [9/25]). **WATCH, not a Path-A fire.** No threshold set or moved. LIQUID owns the credit read. → KB-VIO-313.

🔴 **Rates vol held up; equity vol rebid today.** MOVE 104.58 [9/24] → **96.00** [9/25] → **101.82** [9/28]. 10Y 5.18 [9/24] → **5.17** [9/25 FRED DGS10] — flat, not reversing. VIX 15.67 → 14.87 → **16.07** (+8.07% today); SPX 7743 → 7684 (−0.77%) [yfinance, HENRY owns]. **VIX3M/VIX 1.1344 — flattest since the 9/16 Fed day**, still contango. VVIX **91.02**, highest close since the Fed.

🟠 **GATE-LIQ-069 2-of-2 (CoreWeave CDS) — Path-B read: no Path-B vol fire; the configuration is the opposite.** Path B = index vol fires *without* credit. Now credit moves and index vol doesn't. The dispersion precondition is present (COR1M 9.03 low; constituent-vol [EST] 47.0 [9/17] → 53.5 [9/28]; S5TH 45 [9/24, HENRY]). Read under Will's WQ-301: CoreWeave ≈847bp is **MODEL-DERIVED**, observed = **11.82pt upfront** on 500bp [9/24]; ISDA conversion gap UNMEASURED. → KB-VIO-315.

⚠️ **COR1M first-tell (KB-VIO-188) FIRED 2026-09-02 and was never graded** (9/1 SETTLE 12.64 + 9/2 SETTLE 10.58, both ≥8.43). The 9/2 STATUS rewrite dropped the gate row; nothing re-surfaced it for 26 days. Graded here, late. The 8.43 anchor now sits below almost the whole recent range, so the line discriminates little. No registered action attaches. → KB-VIO-314; mechanized grading flagged to PROME, not built.

**Thesis v4.1.1 stands. Book flat, $0, no proposal, no threshold moved. Convergence 28 → 29/50 (credit 3 → 4). WQ-259 republish DONE (both artifacts, version 7).**

## SIGNAL DASHBOARD

| Metric | Value | As of | Source / interpretation |
|---|---:|---|---|
| VIX | **16.07**; +8.07% vs 14.87 (9/25) | Sep 28 close | [CONF] Cboe delayed-quote; 9/25 **14.87** and 9/24 **15.67** Cboe SETTLE. Regime LOW_VOL |
| VIX9D | **14.39** | Sep 28 | [CONF]; VIX9D/VIX **0.8955** |
| VIX3M / VIX6M | **18.23 / 20.25** | Sep 28 | [CONF]; 9/25 17.93 / 20.01 SETTLE |
| VIX3M / VIX | **1.1344** (9/25 1.2058; 9/24 1.1761; 9/22 1.2393) | Sep 28 | Lowest since 9/16 (event day). p42.2 of 431-row ledger — mid-distribution. Not inverted |
| VVIX | **91.02** (9/25 87.84 SETTLE; 9/24 90.57) | Sep 28 | [CONF]. Above the 90 cheap-line; watch >100; crack 120 |
| SKEW daily | **146.25** · 144.91 [9/25 SETTLE] · 146.04 [9/24 SETTLE] | Sep 24–28 | None ≥150 since 9/15 |
| SKEW 20-session mean | **147.62** (thru 9/28); 147.80 (thru 9/25, all-SETTLE) | Sep 28 | [CONF] VX_DAILY. Above 140 regime line and 145 Q2 line |
| Adjusted M1:M2 | **+4.36%** VX/V6→VX/X6 | Sep 28 settle | [CONF] `thresholds.py`. BELOW_AVG vs 5.6 (KB-VIO-310). 9/25 m1m2 blank (backfill convention) |
| MOVE | **101.82** (9/25 96.00; 9/24 104.58) | Sep 28 | [CONF] investing.com PRIMARY; yfinance agrees. Margins +29.41 F1 / +26.32 confirm-3 |
| OVX | **56.11**, ratio **3.49** p97.1 · FIRE | Sep 28 | [CONF] `ovx.py`. 9/25 55.09 [yfinance hist; no ledger row]. Gap 40.04 p94.9 |
| JPY RV10 | **7.03%** p33.6 CALM; USDJPY 157.46 | Sep 28 | [CONF] `jpy_vol.py`. 9/25 USDJPY 158.81 [yfinance; no ledger row]. FXY IV leg STALE off-RTH |
| COR1M / COR3M | **9.03 / 11.0** (COR30D 8.22); 9/25 COR1M **8.01** (prev_close) | Sep 28 SETTLE | [CONF] `implied_corr.py`. Constituent-vol[EST] **53.5**, DISPERSED. 9/25 COR3M/COR30D unrecoverable |
| HY / B / BB / CCC OAS | **2.93 / 3.00 / 1.76 / 11.28%** | Sep 25 FRED | [CONF] FRED direct. 9/22: 2.68/2.71/1.56/10.75. CCC−BB **9.52pp**. LIQUID owns |
| IG OAS | **0.81%** | Sep 25 FRED | [CONF]; 9/22 0.77 |
| 10Y / 2Y | **5.17 / 4.81%** (2s10s +36bp) | Sep 25 FRED | [CONF] DGS10/DGS2 — HENRY/BOND own. 9/24 5.18 |
| COT VIX positioning | Lev money net **−15,015** p71.8; dealer +66,943 p91.7; asset mgr −55,380 p1.3; OI **412,323** | Sep 22 report | [CONF] CFTC TFF (fetched this session; `--boot` had not pulled it). Prior 9/15: −16,504 p69.9, OI 446,060. OI fall = post-September-expiry roll |
| VIX options C/P OI | 0.00 (after-hours artifact) | Sep 28 | Unusable; call vol 285k / put vol 131k |

## GATE STATUS

| Instrument | State | Exact scope / next step |
|---|---|---|
| **VIO-FOMC-0916** | ⛔ **CLOSED: LETTER FAILED** | Leg 2 KILL now on Cboe SETTLE: VIX 15.18 [9/23] = −14.29% vs kill < −1.41%. 0 CONFIRM · 2 KILL · 1 MISS · 1 VOID · 1 HELD-with-defect |
| **Q2 transmission test** (LIQUID prospective, DOCKET L477) | **NOT FIRING — 3 of 10 sessions elapsed** | `VIX3M/VIX ≤ 1.00 AND VVIX > 120`, two consecutive closes, window 9/24–**10/7** off the 9/23 MOVE spike. 9/28: 1.1344 / 91.02. Disconfirmers (a)–(d): none met — (a) ratio touched 1.2058 on 9/25 but not sustained; (c) VIX 5-session +8.1% is outside ±5% |
| **Cheap-tail alert** | 🟣 **OPEN 4/4 on 9/25 Cboe basis** | VVIX 87.84 ≤90 · VIX 14.87 ≤16 · SKEW 144.91 ≥140 · MU 9/30 in 2d. ⚠️ **On 9/28 delayed-quote L1 (VVIX 91.02) and L2 (VIX 16.07) FAIL → likely 2/4 once Cboe posts 9/28.** OPERATOR SURFACE, NOT A TRADE — TERRY constructs, Will approves |
| **COR1M first-tell** (KB-VIO-188) | **FIRED 2026-09-02 — graded late 9/28** | ≥8.43 × 2 consecutive SETTLE: 9/1 12.64 + 9/2 10.58. No registered action. KB-VIO-314 |
| F-B | **HELD** (window closed 9/16) | Unchanged |
| Coiled spring (STRICT / DIET) | NOT FIRING | VIX and VVIX rising, not falling |
| RED-FT-10 | RED-OWNED | SKEW Cboe bars since 9/15: 146.61 · 145.95 · 145.70 · 148.10 · 142.19 · 144.80 · 146.15 · 146.04 · 144.91 · 146.25 [9/28 dq]. None ≥150 |
| RED-FT-06 | RED-OWNED | VIX 16.07 [9/28] |
| KB-VIO-123 crack/fade tree | **2 of 6** | ③ MOVE ✅ (+26.32) · ① credit leg — widening broad (LIQUID's call) · ② COT p71.8 ✗ · ④ VVIX 91 ✗ · ⑤ ratio 1.13 ✗ · ⑥ VIX <20 ✗ |
| BIN-A / BIN-B | BIN-A STUCK; **BIN-B block active** | CCC 11.28 [9/25] |
| MOVE pause/resume | ARMED | Retire <66.00 far away |
| T9 self-falsifier | NOT MET | MOVE 101.82 ≫ 66 |
| GATE-VIO-RV1 | RETIRED | F2-killed Aug 27 |

## CONVERGENCE MATRIX

**Convergence Score: 29/50** (10 vectors × 5), **+1 vs the prior 28/50** — credit 🟠3 → 🔴4 (widening broadened to every bucket).

| Vector | Score | Current reasoning |
|---|---|---|
| Rates vol | 🔴🔴 **5** | MOVE 101.82 [9/28], back over 100 after 96.00 [9/25]. 10Y 5.17 [9/25] held. Substance HENRY/BOND |
| Credit | 🔴 **4** | **NEW:** HY +25bp, B +29bp, BB +20bp, CCC +53bp 9/22→9/25; VIX fell on the widest day. ¼ of thesis magnitude; origin ambiguous (KB-VIO-313) |
| SKEW / tail bid | 🔴 **4** | 20-session mean 147.62; daily 144.9–146.3, under 150 |
| Oil vol | 🔴 **4** | OVX 56.11, ratio 3.49 p97.1, FIRE since 9/18 |
| Positioning | 🟠 **3** | Lev money p71.8 [9/22]; dealer net long p91.7 |
| Implied correlation | 🟡 **2** | COR1M 9.03, dispersed; constituent-vol[EST] rising 47.0 → 53.5 |
| Equity concentration | 🟡 **2** | S5TH 45 [9/24] with index near highs (WALTER SIG-006, HENRY owns); CoreWeave single-name credit (LIQ-069) |
| VVIX | 🟡 **2** | 91.02, highest since the Fed; <100 |
| Front curve | 🟡 **2** | VIX3M/VIX 1.1344, flattest since 9/16 but p42 of ledger; contango |
| JPY carry vol | ⚪ **1** | RV10 7.03% p33.6 CALM |

## REGIME STATUS AND DRIFT

- **Price classification: LOW_VOL** (VIX 16.07 [9/28]); dipped to COMPLACENCY 14.87 on 9/25.
- **Post-FOMC path from the 9/16 close (17.71):** −14.29% (9/23) → −11.52% (9/24) → −16.04% (9/25) → **−9.26% (9/28)**. The vol premium is rebuilding unevenly.
- 🔴 **New this cycle: credit joined rates.** Through 9/24 the story was a rates-vs-equity-vol spread. Through 9/25 it is rates **and** credit moving, with equity vol lagging both. The thesis's LOW_VOL lead window is 3–8 weeks (to ~2026-11-17 off 9/22) — **inherited hit rates, not VIOLET-reproduced** (thesis v3.1 source note).
- **H-resolution-vs-stress:** n=1; needs the FOMC-date base rate before grading.

## POSITIONS

Last recorded VIOLET book: **FLAT**. FORGE's September 10 mirror confirms. **No broker refresh, no order, no proposal; $0 moved.**

## RESEARCH QUEUE

1. **Next post-close boot:** Cboe stamps 9/28; FRED 9/28 credit (does the broadening continue?); re-run cheap-tail on Cboe 9/28 basis.
2. **Credit-vol watch (KB-VIO-313):** track HY/BB vs VIX through the 3–8 week window. Observe only; no threshold.
3. **Q2 transmission test:** grade each close through 10/7.
4. **Mechanize registered-line grading at boot** (COR1M first-tell, MOVE pause/resume) — KB-VIO-314/231. Flagged to PROME; not built.
5. **Next pre-registered letter** against acceptance conditions ①–⑤ (part 3 §5); build the FOMC-date base rate first.
6. **Thesis-currency advisory:** 47 KB rows since v4.1 (3 retractions). Read the headline against them — overdue.
7. KB-VIO-032 rolling M1:M2 percentile (additive); L441 FORGE `AVG_STEEPNESS` vintage (PROME).
8. Tooling debt: TICK-row defect · `m1m2_settle_date` guard · false-zero COR1M d/d · cheap-tail use-time mirror · OVX/JPY/IMPLIED_CORR scripts have no dated-backfill mode (9/25 rows absent) · `cftc_cot.py --boot` did not pull a released report.
9. **RQ #8 PARKED** (Will 2026-09-25): ***"The corrected ten-event sample does not establish a forward VIX signal in either direction."*** RQ #8a-d HELD.
10. Research: Path-A F2 audit; H-carry RV study; L342 holiday-counter audit before Nov 26.

## OPERATING LIMITS

- **Session:** post-close 9/28, Will's ask "catch up on missed data while dark." Full boot + Cboe backfill + CFTC + FRED.
- **Inbox:** 3 WALTER (003 info-only, 006 noted, 001 ACTION acted → KB-VIO-315) logged and moved; PROME WQ-295 answered by packet (cadence + watch terms).
- **WQ-259 CLOSED** (PROME verified): both artifacts republished to their standing URLs (version 7 each). **WQ-333 done:** CLAUDE.md:194 now points at the memory twins, no date.
- **Hygiene (Will-directed, late session):** stale-intel sweep fixed 7 live-doc items; KB sweep 71 → STALE, KB-VIO-308 → CONFIRMED, 40 durable rows kept ACTIVE (still past Stale_By — review dates owed, SCRATCH 5a). No market figure on this page changed.
- ⛔ **$0 moved.** No trade, card, order, proposal. No threshold set, moved or fired by me.
- Gaps: OVX / JPY_VOL / IMPLIED_CORR have **no 9/25 ledger row** (scripts cannot backfill a date; values cited from yfinance/prev_close above). VX_DAILY 9/25 m1m2 blank.

## Q2 CONTRIBUTION — Will-directed six-questions (DOCKET L477)

*Delivered 2026-09-25 (LIQUID leads Q2). Existing gates only, no new thresholds, no trade proposal. Live grade in GATE STATUS above.*

**Vol confirmation clause (VIOLET):**
> **`VIX3M/VIX ≤ 1.00 AND VVIX > 120` both firing on the same session AND persisting to the next session's close, within 10 sessions of the qualifying MOVE spike (9/23 → window closes 10/7).** Both lines pre-registered (SIGNAL_INTAKE inversion line; KB-VIO-123 VVIX). **Disconfirming (any one):** (a) VIX3M/VIX back toward 1.20 despite MOVE ≥85 sustained; (b) VVIX below 85 despite MOVE holding; (c) VIX 5-session change within ±5% while MOVE p95+; (d) SKEW 20-session mean below 145 sustained. Parked RQ #8 (KB-VIO-312): the ten-event sample establishes no forward VIX signal either way.
