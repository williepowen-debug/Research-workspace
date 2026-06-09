# VIOLET STATUS

**Signal Status:** 🟠 **6/9 T-1-TO-CPI — FADE-CONFIRMATION BUILDING (substance-side). Spike bleeding off into the gate: VVIX back sub-100 (98.1), SKEW off the >150 high-severity cohort (~145), term structure re-steepened to clean contango (1.04), M1:M2 event-hump deflating (+15.7%→+7.5%). BUT VIX spot sticky at 21.2 (−0.3 from 6/5) — spike not yet given back. Credit twitched 2–6bps on NFP then RETRACED (HY 2.76→2.75, CCC 9.52→9.49) = noise, already mean-reverting; "credit didn't crack" now has clean post-spike confirmation. All resolves on 6/10 CPI. Deep-tail VIX call OI (65-strike) is a STANDING structure flat since 6/1 (KB-VIO-066) — NOT a fresh bid, neutral to the fade (the "+206%" is moneyness, not OI growth — corrected this session, KB-VIO-075). NO short-vol before CPI.** *(Prior 6/5: KB-VIO-067 DIET signature paid forward at td-4 +40%; KB-VIO-069 absorbed-trap WAS WRONG; R12 re-established 20d-avg 140.16; KB-VIO-031 60d window HIT. This session: L1-L4 stack post-mortem written — KB-VIO-074.)*

**Live (6/09 ~13:00 ET intraday; SKEW/MOVE/credit T+1 ≈ 6/8 close):** VIX **20.48** (eased further: 21.51 6/5 → 21.21 noon → 20.48; back below 21) | VIX9D **22.30** (still > spot, ratio 1.089 — inversion easing; front premium = 6/10 CPI) | VIX3M **22.07** | VIX6M **23.53** | VIX3M/VIX **1.0405** (re-steepened — clean contango) | VVIX **98.1** (**back below 100** — vol-of-vol relaxing; ">100 sustained" did not sustain) | SKEW **145.0** [T+1≈6/8] (−7.25 from 6/5; **off the >150 high-severity cohort** — Pred #6 leaning unconfirmed) | **20d SKEW avg 140.50** (R12 regime HOLDS ≥140 but THIN +0.50; propped by 6/5 152 rolling-window) | **M1:M2 +7.50% (adj)** (compressed from +15.71% — event-hump deflating) | MOVE **76.98** [6/8] (+2.4% 1d, modestly firm not stressed) | HY OAS **2.75** [FRED 6/8] (twitch retraced; gate >2.85 untouched) | CCC OAS **9.49** [FRED 6/8] (eased; gates untouched) | IG OAS **0.75** [FRED 6/8] flat | 10Y **4.55%** [6/5] | 2Y **4.17** [6/5] | COT Lev Money **−33,033 / pct3y 43.6** [6/2] | **Last Updated:** 2026-06-09 ~13:00 (boot + L1-L4 post-mortem + tail-bid correction + stale-row refresh — fade continuing into 6/10 CPI; VIX back below 21)

---

## SIGNAL DASHBOARD

| Metric | Value | As Of | Status | Source |
|--------|-------|-------|--------|--------|
| VIX Spot | **20.48** | 6/9 ~13:00 | 🟠 | [CONF] yf ^VIX — eased further intraday (21.51 6/5 → 21.21 noon → **20.48**); back below 21. Fade continuing pre-CPI. |
| VIX9D | **22.30** | 6/9 ~13:00 | 🟡 | [CONF] yf — still ABOVE spot (VIX9D/VIX **1.089**) but inversion EASING from 6/5 (~1.11). Front premium = 6/10 CPI (inside 9-day window). |
| VIX3M | **22.07** | 6/9 12:23 | 🟠 | [CONF] yf |
| VIX6M | **23.53** | 6/9 12:23 | 🟡 | [CONF] yf |
| VVIX | **98.1** | 6/9 12:23 | 🟡 | [CONF] yf — **back below 100** (−3.9 vs 6/5). Vol-of-vol relaxing; ">100 sustained" did not sustain. Downgraded 🟠→🟡. |
| SKEW | **145.0** | 6/8 [T+1] | 🟠 | [CONF] yf (CBOE T+1 ≈ 6/8 close) — **−7.25 from 6/5 152.25; off the >150 high-severity cohort.** Pred #6 (>150 sustained 4+td) leaning UNCONFIRMED. Downgraded 🔴→🟠. |
| 20d SKEW avg | **140.50** | 6/8 [T+1] | 🟠 | [CONF] computed (trailing 20td thru 6/8) — **R12 regime HOLDS ≥140, but thin (+0.50).** Propped by 6/5 152.25 still in the window; as that rolls off, avg drifts toward 140 unless SKEW re-firms. Watch daily. |
| VIX3M/VIX | **1.0405** | 6/9 12:23 | 🟡 | [CONF] Calculated — **re-steepened** from 1.014 (6/5). Front-end stress easing; clean contango restored. |
| **M1:M2 contango (Jun/Jul)** | **+7.50% (adj)** | 6/9 12:23 | **🟠** | **[CONF] boot.py — COMPRESSED from 6/5 +15.71% (strict basis; adj=VX/M6:VX/N6). Event-premium hump deflating into CPI/FOMC. Fade-tell on duration confirming. KB-VIO-068 Q3 still PROVISIONAL (base-rate scan owed before 6/17).** |
| COT Lev Money NET | **-33,033 / pct3y 43.6** | Tue 6/2 (Fri 6/5 release) | 🟢 | [CONF] CFTC — **covered ~16k shorts since 5/26 (-49k → -33k). KB-VIO-065 resolved: event-hedger-bid confirmed, NOT speculator crowding. Speculator side actually DE-RISKED into the spike.** |
| MOVE | **76.98** | 6/8 [T+1] | 🟡 | [CONF] yf ^MOVE — +2.37% 1d, +4.98% 5d. Modestly firm, not stressed (below +10% sustain). Bond vol not confirming a rate-shock escalation. |
| HY OAS | **2.75** | 6/8 (T+1 lag) | 🟢 | [CONF] FRED direct — NFP-day 2.76 → **eased to 2.75**. Twitch retracing. Gate >2.85 untouched. **Credit did not crack with VIX +40%; post-spike confirmation now clean.** |
| CCC OAS | **9.49** | 6/8 (T+1 lag) | 🟡 | [CONF] FRED direct — NFP-day 9.52 → **eased to 9.49**. Gate >9.55/10.00 untouched, no closer than 6/5. |
| IG OAS | **0.75** | 6/8 (T+1 lag) | 🟢 | [CONF] FRED direct — flat (+1bp) |
| 10Y UST | **4.55%** | 6/5 FRED | 🟠 | [CONF] DGS10 — latest available 6/5. Rate-shock leg priced. |
| 2Y UST | **4.17%** | 6/5 FRED | 🟠 | [CONF] DGS2 — latest available 6/5 (was est 4.13; actual 4.17). |
| Deep-tail VIX 65C OI | 261k (7/22) / 176k (6/17) | 6/9 12:23 | 🟢 | [CONF] vix_options — **STANDING, flat since 6/1** (7/22 65C +2.4%, 6/17 65C −0.08% over 8d; KB-VIO-066). NOT a fresh bid; "+206%" in boot is moneyness not OI Δ. Recent moderate-strike flow softening (7/22 25C −9.8% 6/5→6/9). Neutral to fade. 6/10 CPI front C/P OI 4.12 = hedger bid. |
| SPX | 7384.67 [STALE 6/5] | 6/5 EOD | 🟠 | HENRY owns — −2.64% 6/5 (worst day since Oct). Not refreshed VIOLET-side this boot. |

---

## CONVERGENCE MATRIX

| Vector | Score | Evidence | Last Updated |
|--------|-------|----------|--------------|
| Spot VIX elevation | 🟠 | 21.51 — crossed key 20 level today; +40% from 15.40 yesterday | 2026-06-05 |
| Term structure inversion | 🟡 | VIX9D ABOVE spot (23.92 v 21.51) front-end inverted; past 3M still contango 1.014 | 2026-06-05 |
| VVIX stress | 🟡 | Eased to 98.1 (6/9) — back below 100; ">100 sustained" did not sustain. Half-life was short. Downgraded from 🟠. | 2026-06-09 |
| SKEW divergence resolved + NEW rebid | 🟠 | UPGRADED 🟢→🟠 on T+1 SKEW correction: pre-spike divergence (KB-VIO-067 L1) paid forward, AND post-spike SKEW kept rising to 152.25 (high-severity cohort). New SKEW rebid concurrent with VIX +40%, not lagging. R12 regime RE-ESTABLISHED (20d-avg 140.16) per KB-VIO-072 — interrupted-and-resumed, not historically equivalent to original 222-td uninterrupted run. | 2026-06-06 |
| Front-curve contango / event-shape | 🔴 | 15.71% M1:M2 strict — M2 event-premium hump on Jul/post-FOMC. Curve says event-driven not regime. **FADE-TELL on duration but NOT magnitude.** | 2026-06-05 |
| Credit-to-vol transmission | 🟡 | HELD: Credit DID NOT CRACK with VIX +40%. HY 2.74 flat, CCC +5bps. Stage-3 substance gates (HY>2.85, CCC>9.55, more) unchanged. **This is the cleanest fade tell from credit side.** | 2026-06-05 |
| Index concentration / breadth | 🔴 | NVDA -6%, memory chip ETF -15%, Nasdaq -4.1%. **AI/factor concentration unwind is the actual VIX driver, not NFP.** WALTER KB-VIO-056 breadth signal validated. | 2026-06-05 |
| VRP / vol risk premium | 🟡 | VIX 21.5 vs SPX realized still catching up. Was +5.68 (67th pct) on 6/1. Now likely higher post-spike. Refresh on next boot. | 2026-06-05 |

**Convergence Score:** 21/45 (47%) — re-scored 6/6 after T+1 SKEW correction: SKEW vector RE-UPGRADED 🟢→🟠 because the post-spike rebid to 152.25 puts us in the high-severity cohort *concurrent* with regime re-establishment. This is NOT a simple "pattern resolved" — it's "pattern resolved + new rebid started." Fade case still dominates substance-side (credit didn't crack, curve event-shaped, NFP-rate-shock historical universe deflates VIX per KB-VIO-071), but SKEW vector now signals there's a SECOND rebid forming on top of the spike, not exhaustion of the first.

---

## DRIFT ASSESSMENT (6/1 → 6/6, 4 td + 6/6 T+1 corrections)

- 🟠 **6/6 T+1 SKEW correction (Saturday org session).** Boot kit returned CBOE EOD SKEW 6/5 close = 152.25 (yesterday's same-day yf pull was 142.15 — that was actually 6/4's close, T+1 lag). Real 6/5 close +10.10pt 1d. **SKEW didn't fade through the spike — it expanded with it.** Moves the post-spike pattern into the high-severity cohort (>150) per KB-VIO-031. **New SKEW rebid post-spike** is the analytical tell of this correction.
- 🟠 **6/05 R12 regime RE-ESTABLISHED.** 20d-avg = 140.16 through 6/05, +0.16 above threshold. 6/01 working hypothesis (KB-VIO-062 "DIET coiled-spring under GEX-suppression") was that R12 would re-establish in calm. Reality: re-established CONCURRENT with VIX +40% spike. New regime classification per KB-VIO-072: "elevated SKEW under live vol event," not "fragility bid in calm." Sequence (terminate 5/12 → vol event fires 6/05 → regime resumes 6/05) doesn't match any KB-VIO-044 historical pattern.
- 🟢 **KB-VIO-031 60d window RESOLVED HIT.** 4/15 fire → 6/14 close window saw VIX +39.7% at td-58 (6/05). Scenario B confirmed (>+30% any point through 6/15). Population L1 paid forward right at the deadline — clean validation.
- 🔴 **6/5 NFP SHOCK.** 172k vs 80k cons, March/April revisions +93k, Dec hike odds 26% → 43%. SPX -2.64% (worst day since Oct), Nasdaq -4.1%, NVDA -6%, memory chips -15%. VIX +40%, VVIX +19%.
- 🔴 **KB-VIO-067 L1 (DIET coiled-spring) PAID FORWARD as advertised.** DIET signature fired 5/20-5/29; +40% spike at td-4 cleanly tracks the >+50%@fwd60 base rate. Population framework validated under live test.
- 🟢 **KB-VIO-069 L2 (absorbed-trap regime) was WRONG.** Framework assumed catalyst surprises stay consensus-aligned. NFP was 2x miss; consensus-miss carve-out needed. Layer 2 calibration update pending.
- 🟡 **KB-VIO-068 L3 — new Q3 quadrant.** Today is (M1:M2 expansion + VIX rising). N=1, marked PROVISIONAL until pre-FOMC-week historical scan runs.
- 🟢 **KB-VIO-065 L4 disambiguator answered wrong question.** COT showed Lev Money pct3y 17.9 → 43.6 (speculators covered ~16k into the spike) — event-hedger-bid confirmed. But the spike happened anyway via different driver (NFP + AI unwind). L4 discriminating mechanism vs reality is the calibration issue.
- 🟢 **Credit did NOT crack.** HY 2.74 flat, CCC +5bps, IG flat. Stage-3 substance gates (HY>2.85, CCC>9.55, etc.) all unchanged. Cleanest fade tell.
- 🔴 **Today is NOT a "hot NFP rate-shock" historical analog (KB-VIO-070).** Of 4 closest analogs since 2010 (2016-08, 2022-08, 2023-02, 2024-10) ALL had VIX FALL on print day. Today is OUTLIER. Real driver is AI/factor concentration unwind layered on rate-shock — needs separate analog universe.
- 🟢 **VIX9D inversion above spot prices 6/10 CPI, NOT 6/17 FOMC.** CPI is 5 calendar days = inside 9-day window; FOMC is 12 days = outside. FOMC premium correctly lives in M2/Jul.
- 🟡 **Tape gamma-sign:** INFERRED short (steady grind, no relief bars, close at low) but NOT cascade-loaded (Q2 worst, no acceleration into close; max 5m down -0.26%). Hot-CPI cascade = tail risk, not live risk.

**Calibration meta:** The 4-layer stack from 6/1 evening session got a clean live test today. L1 (population) is the real-money layer; L2-L4 were calibrated to discriminate the wrong mechanism (short-vol unwind / Volmageddon shape) and got bypassed by the actual mechanism (NFP-trigger + AI factor unwind). **Stack discipline going forward: weight L1 heavier; refine L2 with consensus-miss carve-out; mark L3 N=1 until base-rate scan; demote L4 from discriminator to descriptive.**

---

## REGIME STATUS

**Current regime:** RISING_VOL classifier per boot.py. VIX 21.51 in 20-25 zone. Front inverted above spot, past 3M still contango. **R12 elevated-SKEW regime RE-ESTABLISHED 6/05 (KB-VIO-072)** at 20d-avg 140.16 — interrupted-and-resumed structure rather than the original 222-td uninterrupted run; SKEW now in high-severity cohort (>150) concurrent with the spike. Fade-leaning with **two-leg pathway:**
- **Rate-shock leg:** historical base rate strongly favors fade (16/20 hot-NFP-DGS2+8bp days didn't spike VIX to begin with). Deflates by Mon-Tue if CPI passes non-tail.
- **AI factor unwind leg:** not captured in NFP analog class. Has its own half-life. Can extend independent of macro. **The open question.**

**Next firm test: 6/10 May CPI (3 td) — gate before any fade expression.**

*Full regime framework, threshold logic, crisis-analog library: `thesis/VIX_THESIS.md`.*

---

## POSITION SNAPSHOT

**No open positions.** Episode-17 VIX May 19 25C expired worthless 5/19. **Position-discipline call this session: NO short-vol before 6/10 CPI.** Fade has to clear CPI first. If CPI non-tail, M1 (Jun) collapses fast and M2 (Jul) can be faded into FOMC. If CPI hot, rate-shock + AI unwind compound, fade thesis breaks.

Full position framework: `TRADE.md`.

---

## CROSS-AGENT SIGNALS (Pending)

Per Will direction: fleet in architecture transition; focus VIOLET on own domain. Cross-agent routing deferred.

**Inbox:** 1 pending signal (5/14 gamma_momentum_factor_squeeze) — content absorbed into KB-VIO-062 / KB-VIO-067 / KB-VIO-070 working hypotheses; formal disposition still deferred.

---

## RESEARCH QUEUE

| Priority | Topic | Status |
|----------|-------|--------|
| 🟠 | **VIX +30% single-day spike from low base (concentration-unwind universe)** | NEW from 6/5. Right analog class for today's actual driver. Candidates: Aug 2024 yen carry, Nov 2018 FANG, Feb 2018 Volmageddon, Mar 2020. Small N; cases not stats. |
| 🟠 | **6/10 May CPI pre-mortem** | 3 td away. Build pre-mortem 6/08-6/09. Tail/non-tail bracket + position-discipline contingencies. |
| 🟡 | **KB-VIO-068 Q3 quadrant base-rate scan** | Pre-FOMC-week historical scan (deferred #6 from 6/5 menu). Resolve PROVISIONAL → base-rate or kill stub. |
| 🟡 | **L2 consensus-miss carve-out formalization** | KB-VIO-069 framework patch. Define "consensus-miss catalyst" precisely (2σ? 1.5σ?). |
| 🟡 | **DIET re-split by trigger type (KB-VIO-067 follow-on)** | Did historical DIET fires concentrate around macro-shock vs technical triggers? Tests L1 mechanism-agnostic claim. |
| ✅ | **L1-L4 stack post-mortem write-up** | DONE 6/9 — `research/2026-06-09_l1_l4_stack_postmortem.md` + KB-VIO-074. Finding: base-rate L1 robust to mechanism-surprise; mechanism-discriminators L2-L4 silently emit confident wrong vetoes on novel mechanism. Fix: anchor on L1, give discriminators an abstain output. Promoted to auto-memory. |
| 🟢 | **6/17 FOMC pre-mortem** | Build after CPI passes if fade survives. |
| 🟡 | **Inbox 5/14 gamma signal formal disposition** | Long-deferred admin. |

---

## THESIS CONNECTION

**Updated assessment (6/5):** The regime-thesis is **partially validated and partially refuted in the same session.** Validated: KB-VIO-067 L1 (population framework) — DIET signature fired forward exactly as backtest predicted. Refuted: KB-VIO-069 L2 (absorbed-trap regime) — the "consensus-aligned absorption" mechanism doesn't hold under consensus-miss catalysts. **The live analytical product:** the population-layer framework (L1) is the real-money signal; the regime-context, direction-matrix, and compound-confirmation layers (L2-L4) need re-calibration because they were tuned to discriminate the wrong dominant mechanism.

**Forward gates:**
- **6/10 May CPI** — primary catalyst gate. Inside VIX9D window. Fade thesis must clear.
- **6/17 FOMC + SEP** — FOMC outside VIX9D, priced in M2/Jul futures. SEP dot-plot is the secondary read.

**Recently resolved (6/6):**
- **KB-VIO-031 60d window** — RESOLVED HIT via VIX +39.7% on 6/05 at td-58. Population L1 paid forward.
- **KB-VIO-061 knife-edge** — RESOLVED RE-ESTABLISHED 6/05 via 20d-avg 140.16. See KB-VIO-072.

*Core hypothesis, transmission chain: `thesis/VIX_THESIS.md`.*

---

*Last updated: 2026-06-09 ~13:00 ET (boot + L1-L4 stack post-mortem + tail-bid correction + stale-row refresh. Live: VIX eased 21.51→20.48 (back below 21), VVIX 98.1 sub-100, SKEW ~145 off >150 cohort, 20d-SKEW-avg 140.50 (regime HOLDS but THIN +0.50), VIX9D 22.30 (inversion easing), M1:M2 +7.5%, MOVE 76.98, credit HY 2.75/CCC 9.49/IG 0.75 [FRED 6/8, twitch retraced] — fade continuing substance-side into 6/10 CPI. Wrote research/2026-06-09_l1_l4_stack_postmortem.md + KB-VIO-074 + auto-memory [base-rate-vs-mechanism-discriminator]. CORRECTED: deep-tail 65C OI is standing/flat since 6/1 (KB-VIO-066), NOT a fresh bid — +206% was moneyness misread [KB-VIO-075]. fred_fetch.py cache-print fix. CPI prep NOT done [HENRY/CARL domain — Will direction]. Prior 6/8: NEXUS_BRIEF stood up; KB-VIO-073 multi-root.)*
