# VIOLET STATUS

> ## 🟠 8/18 ~10:40 ET — **the elevated-SKEW regime terminated on 8/17, every gauge bid together the same session, and my catalyst feed was blind to three HIGH events inside seven trading days. FLAT.**
>
> **⓪ 🔴 CHEAP-TAIL IS *ARMING* 3/4, NOT DORMANT 2/4 — I PUBLISHED THE WRONG COUNT EARLIER TODAY AND CORRECTED IT.** Investigating whether a dated event sat inside the VIX9D window, I found `CATALYSTS.tsv` held only a LOW expiry and a LOW COT before a **24-day gap**. The true forward set: **FOMC MINUTES 8/19 14:00 ET** (first minutes of the new hike-signal regime, first full cycle under Warsh) · **NVDA Q2 FY27 8/26 ~16:20 ET** (PRIMARY-verified at NVIDIA IR 7/29) · **JACKSON HOLE 8/27-29, Warsh's first keynote as chair 8/28**. ⇒ **cheap_tail's L4 leg computed 24–29 days when the true nearest was 1–5, and graded ⬜ when it should have been ✅.** Corrected: **ARMING 3/4 on BOTH 8/14 and 8/17** — arming for two sessions while this dashboard published DORMANT. **PROME's spawn-sooner clause ("if cheap-tail reaches 3-of-4 before the design session") FIRES.** ⚠️ **This does NOT convert the 8/17 bid into event pricing** — Jackson Hole was 11 days out on 8/17, *outside* the 9-day tenor, so it cannot explain that day's VIX9D move. It weakens my "no catalyst, leans mechanical" reasoning **without establishing the alternative.** → **KB-VIO-198**
>
> **① 🔴 THE 20d-AVG SKEW REGIME TERMINATED 2026-08-17 at 139.86 — first sub-140 print since 2026-06-04.** The regime that re-established 6/5/2026 (KB-VIO-072, concurrent with the +40% NFP shock) ran **6/5 → 8/14 = 49 trading days**. ⚠️ **NAME THE METRIC — the two SKEW metrics crossed 140 in OPPOSITE directions on the same session:** the **daily close** went **ABOVE** (142.91, first since 7/31) while the **20d-avg regime line** went **BELOW** (139.86). Conflating them inverts the read both ways (MEMORY principle 10). **The termination is mechanically robust, not marginal:** the average is falling because the window is rolling off the 146–152 late-July prints, so **even if daily SKEW holds 142.91 the avg projects 139.42 → 139.06 → 138.91 → 138.69 → 138.50 and does not recover 140 within ten sessions**; restoring it *next* session needs a daily print **≥154.43 (+8.1%)**. → **KB-VIO-192**
>
> **② 🟠 BROAD FRONT-LED VOL BID ON 8/17 — and it is NOT the coiled spring.** 8/14 → 8/17: **VIX 14.25 → 15.19 (+6.6%) · VVIX 87.48 → 93.92 (+7.4%) · SKEW 138.36 → 142.91 (+3.3%) · VIX9D 10.61 → 12.39 (+16.8%) · MOVE 69.58 → 75.63 (+8.7%).** VIX9D led by ~2.5× the next mover ⇒ the bid is in the **front of the curve** (VIX9D/VIX 0.745 → 0.816; VIX3M/VIX 1.295 → 1.254, flattening from a steep base). ⚠️ **Explicitly NOT KB-VIO-036/principle-6:** the coiled spring needs SKEW rising while VIX **and** VVIX **fall**. All three rose together. That is a near-dated **event bid**, not a tail-reload divergence, and must not be scored as a divergence fire. **8/18 pre-open extends it: VIX 15.78 [PROVISIONAL, +3.9%], cumulatively +10.7% off the 8/14 low.** → **KB-VIO-193**
>
> **③ 🔑 THE MECHANISM UNDERNEATH BOTH: the dispersion regime that was arithmetically suppressing index vol is unwinding.** Implied correlation **COR1M 6.77 [7/31 episode low] → 8.47 [8/18]**, **+25%**, while derived constituent-vol fell **63.2 → 54.2**. Through 8/4 I argued a sub-16 VIX was *partly arithmetic* — low correlation mechanically suppresses index vol (KB-VIO-126/180/181). **That arithmetic is now running the other way.** ⚠️ Not yet a registered fire: the COR1M first-tell needs **≥8.43 on 2 consecutive SETTLE closes** and 8.47 is a **TICK** — session **0 of 2**, today's settle would be session 1.
>
> **④ ⚠️ POSITIONING IS ON THE WRONG SIDE OF THIS AND THE DATA IS 5 SESSIONS STALE.** Recovered the missing 8/04 COT report this session and decomposed the swing WALTER could not: **93% of the +16,062 flip was NEW LONGS** (+14,961) **not short-covering** (−1,101) — then **it round-tripped at a loss**: 8/04 → 8/11 longs **−11,415** liquidated, shorts **+4,485** added, net back to **−12,127** while VIX fell 16.50 → 15.28. **Leveraged money bought the 8/04 spike, lost, and re-shorted — and is net short vol into the 8/17 bid, which this instrument cannot see** (latest report 8/11; the 8/18 report publishes **Fri 8/21**). → **KB-VIO-194**
>
> **⑤ ⚠️ HOW ①–② WERE NEARLY MISSED: yfinance silently dropped 8/17 for ^VIX/^VVIX/^SKEW while returning ^VIX3M for the same date.** `backfill.py` reported success (*"touched 36 rows"*) and left the hole; nothing downstream flagged it. It was found only because the **N5 (i-b) capture-time rule forced me to establish the provenance of the 15.78 pre-open print**, which led to the CBOE primary — where 8/17 turned out to carry the session's two biggest findings. **A gap-filler whose own source has holes reports success while leaving the hole.** → **KB-VIO-195**

---

## SIGNAL DASHBOARD — **8/18 ~09:45 ET · basis TICK (pre-open)**

> ⚠️ **BASIS DISCIPLINE (N5 i-b, adopted 8/13):** `^`-index rows below are **8/17 SETTLE** unless marked TICK. **VIX 15.78 is a PROVISIONAL LIVE BAR, not a close** — verified, not assumed: CBOE quote payload gives `prev_day_close` **15.19** with `last_trade_time` **2026-08-17T16:15:01**. VIX cash disseminates to **16:15 ET**.
> ✅ **8/17 spot recovered from the CBOE primary** (`*_History.csv`) after yfinance returned a partial date — see ⑤. **CBOE should become PRIMARY for this series; yfinance demoted to cross-check** (owed, not done — KB-VIO-195).
> 🔴 **MIXED-VINTAGE TRAP, CAUGHT 09:44 ET (KB-VIO-197):** at 14 min into RTH the CBOE feed returned `current_price` for all six vol indices, but **only ^VIX had actually printed** (15.84). ^VIX9D/^VIX3M/^VIX6M/^VVIX/^SKEW all returned `current_price` **exactly equal to** `prev_day_close` with `last_trade_time` still `2026-08-17T16:15:01` — **stale values served as current with a 0.00% change**, confirmed independently at yfinance (zero intraday bars). ⚠️ **Ratios built across that mix are artifacts**: the mixed read gives VIX9D/VIX 0.7822 and VIX3M/VIX 1.2020, which look like a violent flattening. **The true 8/17 settle-basis ratios are 0.8157 and 1.2535, and those are what this dashboard carries.** 🔑 **A percent-change field cannot distinguish "unchanged" from "unpublished."**
> ⚠️ **Dark 8/11–8/17 (no VIOLET session).** VX_DAILY, COT and IMPLIED_CORR all had holes from irregular boots; VX_DAILY + COT backfilled this session, **IMPLIED_CORR 8/11–8/17 remains empty.**

| Metric | Value | As Of | Status | Source |
|--------|-------|-------|--------|--------|
| **VIX Spot** | **15.19** SETTLE · **15.84** LIVE (+4.28%) | **8/17 SETTLE** / 8/18 09:44 ET live | 🟡 | [CONF A1] CBOE VIX_History.csv + delayed_quotes 09:44 ET. **LOW_VOL.** +6.6% on 8/17 off the 14.25 [8/14] low; +10.7% cumulative incl. the pre-open tick. Path 14.55 → 14.63 → 14.25 → **15.19**. |
| **VIX9D** | **12.39** · 9D/VIX **0.8157** (from 0.7446) | **8/17 SETTLE** | 🟠 | [CONF A1] CBOE — 🔑 **+16.8%, the largest mover on the surface.** Front-end re-loading fast, still below 1.0. |
| **VIX3M** | **19.04** | **8/17 SETTLE** | 🟡 | [CONF A1] CBOE. |
| **VIX6M** | **21.33** | **8/17 SETTLE** | 🟡 | [CONF A1] CBOE — long end flat all month (21.35 → 21.33): **the repricing is front-end, again.** |
| **VIX3M/VIX** | **1.2535** (from 1.2954) | **8/17 SETTLE** | 🟢 | [CONF] calc — **flattening from a steep base.** Inversion line 1.0 is **20.3%** away; nowhere near a peak-marker. |
| **VVIX** | **93.92** (+7.4%) | **8/17 SETTLE** | 🟡 | [CONF A1] CBOE — highest since 7/29 (109.47). **120 not approached.** Cheap-tail L1 (≤90) **now fails.** |
| **SKEW** | 🔴 **142.91** daily (**+4.55**) · **20d avg 139.86** ⬇ | **8/17 SETTLE** | 🟠 | [CONF A1] CBOE SKEW_History.csv. **Daily back ABOVE 140** (first since 7/31 141.23); path off the 8/4 low **126.41 → 133.32 → 134.73 → 132.57 → 137.13 → 135.59 → 136.54 → 134.37 → 138.36 → 142.91 = +16.50 pts in 9 sessions.** ⚠️ **20d-avg REGIME TERMINATED at 139.86** — opposite direction, same session. `final_5d_change` **+5.78**. → **KB-VIO-192** |
| **★ M1:M2 contango (adj)** | **+9.40%** 🟠 COMPLACENCY_TOP_30PCT | **8/17 settle (T-1)** | 🟠 | [CONF] CBOE VX settlement (VX/U6:VX/V6), **T-1 stamped** per N5. ⚠️ **`m1m2_strict +15.63%` is ROLL-CONTAMINATED (2d to M1 expiry) — do not quote it as a level.** |
| **★ MOVE (rates vol)** | **75.63** (+6.05 vs 8/14) | **8/17** | 🟠 | [CONF] move.py, investing.com PRIMARY (yfinance *agrees*). 🔑 **Re-crossed BOTH lines on 8/17 after breaking below:** 77.92 [8/11] → 72.09 → 69.23 → **69.58 [8/14, below F1]** → **75.63.** F1 72.41 **+3.22** · confirm-3 75.50 **+0.13 (marginal)**. **KB-VIO-190 re-arm (≥72.41 ×2) is at session 1 of 2 — today's print decides it.** |
| **CCC OAS** | **10.18** (+6bp) | **8/17 [FRED]** ✅ | 🟠 | [CONF A1] fred_fetch, refreshed 8/18 — **was carrying 8/14; the 8/17 print had landed.** 🔴 **BIN-B BLOCK ACTIVE** (10.18 ≥ 9.55). |
| **CCC−BB dispersion** | **8.59** (+4bp) | **8/17 [FRED]** ✅ | 🔴 | [CONF A1] — still through the registered 8.00 line. |
| **Credit breadth** | 🆕 **EVERY SERIES WIDENED ON 8/17** — CCC +6 · HY +3 · B +3 · BB +2 · BBB +1 · IG +1 bp | **8/17 [FRED]** ✅ | 🟠 | [CONF A1] — **a clean quality sort** (lower tranches widened more), on the **same session as the vol bid**. ⚠️ **DIRECTION AGREES, MAGNITUDE SAYS NOTHING HAPPENED:** 8/17 only retraces 8/14's tightening, and **HY 2.70 is still BELOW its 8/11–8/13 level of 2.71–2.72.** This is *not* credit confirmation of a stress event. Levels: HY 2.70 · BB 1.59 · B 2.88 · BBB 0.99 · IG 0.81 · EuroHY 2.53 · EM_HY 2.85. **LIQUID owns the level; I consume it as a VIX lead/lag comparator (KB-VIO-006).** → KB-VIO-199 |
| **COT Lev Money NET** | ⚠️ **−12,127** / pct3y 76.3 · OI **382,010** | **8/11 report** | 🟡 | [CONF] cftc_cot --backfill (189 rows, 2023→). Gross legs 8/04→8/11: **long −11,415 · short +4,485.** Dealer +40,168 (p62.8) · Asset Mgr −27,104 (p16.7). ⚠️ **The `ELEVATED_LONG` flag sits on a NET SHORT book — a percentile label, not a position.** → KB-VIO-194 |
| **★ JPY vol (canary)** | 🟢 **CALM** — RV10 **5.13%** / p20.1 · USDJPY **159.65** | **8/18** | 🟡 | [CONF] jpy_vol.py. 🔴 **RV still through IV (5.13% vs 2.6%)** — unwind-underway signature persists, but RV has collapsed from 12.94% [8/4]. Channel **unloaded**, not transmitted. |
| **OVX oil-vol (canary)** | **48.01** (p82.5) · ratio **3.06** (p90 WATCH) | **8/18** ✅ | 🟡 | [CONF] ovx.py, re-pulled 8/18 — 🔽 **DOWNGRADED FIRE → WATCH; the dashboard was publishing FIRE off the 8/14 read.** 🔑 **The downgrade VINDICATES the standing caveat:** the ratio fell 3.48 → 3.06 **not because oil-vol collapsed** (49.52 → 48.01, −3%) **but because VIX ROSE** — the denominator moved. The level barely budged and is still p82.5. **Read the level, not the ratio** — it has now misled in both directions. |
| **Implied correlation** | **COR1M 8.47** · COR3M 11.12 · COR30D 8.09 · constituent-vol **~54.2 [EST]** | **8/18 TICK** | 🟠 | [CONF] implied_corr.py — **DISPERSED but unwinding: +25% off the 6.77 [7/31] episode low** while constituent-vol EST fell 63.2 → 54.2. **The suppression arithmetic is reversing** (③). ⚠️ TICK, not settle. |
| **★ Cheap-tail window** | ⚪ **DORMANT 2/4 — the COUNT is unchanged and the COMPOSITION fully rotated** | **8/17** *(hand-computed)* | 🟠 | ⚠️ **The instrument is STUCK on 8/14 data** — `cheap_tail.py` reads yfinance, which has no 8/17 row (KB-VIO-195), so it prints a 4-day-old state as current. **Hand-computed on the CBOE 8/17 settles:** L1 VVIX 93.92 **✗ (lost)** · L2 VIX 15.19 ✅ · L3 SKEW **142.91 ✅ (GAINED — first time since the 8/4 collapse)** · L4 nearest HIGH/MED 25d ✗. **8/14 was L1+L2; 8/17 is L2+L3.** 🔑 **Same scalar, different instrument — the KB-VIO-178 rotation class again.** **The 3-of-4 spawn-sooner clause is NOT met.** |
| **VIX options C/P** | OI **2.71** · Vol **0.97** (forward, 6 expiries) | 8/18 pull | 🟡 | [CONF] vix_options. **8/19 (1d) carries the size** — call OI 3.63M vs put 1.25M. 9/16 quarterly: call OI 3.36M, **65C 251k (+312%)**, 25C 292k. Far-OTM call accumulation on the quarterly. |

---

## GATE STATUS

| Gate | State | Line | Distance / note |
|------|-------|------|-----------------|
| 🆕 **COR1M first-tell** | 🟠 **SESSION 0 of 2 — a tick is not a settle** | COR1M ≥8.43, **2 consecutive SETTLE closes** | **8.47 [8/18 TICK] is through the line but does not count.** Today's settle would be session 1. ⚠️ IMPLIED_CORR has **no 8/11–8/17 rows**, so I cannot rule out that settles crossed while I was dark — **unresolved, do not assume 0**. → KB-VIO-188 |
| 🆕 **MOVE pause/resume** | 🟠 **RE-ARM SESSION 1 of 2 — resolves today** | Retire <66.00 (N1) · re-arm **≥72.41 ×2** (F1) | Broke below F1 on 8/13–8/14 (69.23 / 69.58), **re-crossed 75.63 [8/17]** = session 1. Never touched the 66.00 retire line. → KB-VIO-190 |
| 🆕 **T9 self-falsifier (conjunctive)** | **NOT MET — all four legs fail** | COR1M <6.77 **AND** JPY RV<IV **AND** OVX <45 **AND** MOVE <66.00 | COR1M **8.47** [8/18 TICK] · JPY RV through IV [8/18] · OVX **48.01** [8/18] · MOVE **75.63** [8/17]. ⚠️ **VINTAGES NOW STATED PER LEG, and that is the finding:** this cell previously asserted *"all four legs fail"* from **four different dates with none disclosed**, including an OVX leg 4 sessions stale. **The verdict was right and the disclosure was not** — a conclusion is present-tense even when each input is dated somewhere else. Re-checked on fresh data: still fails 4-of-4. The antidote to a standalone-low-COR1M misread. → KB-VIO-189 |
| ⛔ **SKEW>140 "reload watch"** | **WITHDRAWN 8/10 — RED owns it, AND IT HAS NOW FIRED ON RED'S LINE** | ~~VIOLET SKEW>140~~ | RED's standing guard is *"SKEW re-cross >140 re-opens the Acute vol leg"* — **single-session, no sustain.** **SKEW closed 142.91 [8/17] ⇒ RED's line is crossed.** **Measurement routed; the ruling is RED's.** → KB-VIO-191 |
| 🟡 **RED-FT-06** | **FIRED 8/11 (RED-owned) — but its stated precondition has since reversed** | VIX <16, sustain 5 | Streak verified at the CBOE primary: 15.81 · 15.15 · 14.90 · 15.46 · **15.28 = 5 of 5.** RED pre-decided *"if SKEW is still sub-140, take managed-decline at face value"* — true on the letter at 135.59 [8/11]. ⚠️ **WALTER's Friction 1 (8/11) warned SKEW was travelling TOWARD 140, not away. Six sessions later it closed 142.91.** WALTER called the mechanism a week early. **RED's ruling, my measurement.** |
| ⛔ **KB-VIO-090 credit tree (BIN-A)** | **STUCK — RETIRED 8/4 (Will-ratified)** | ~~CCC ≥9.65 · BB ≥1.73 · HY ≥2.85 · disp ≥8.00~~ | Fires 95.5% of days at 0.97× baseline = noise. **No validated replacement** (ΔCCC tree failed re-derivation, p=0.27). **BIN-A answers nothing.** BIN-B block is the live credit read. |
| ✅ **GATE-VIO-116 (rates-vol shape)** | ✅ **RE-OPEN CONFIRMED** | Re-open = MOVE >70–72 | Held through the 8/13–8/14 dip below F1 and re-crossed 8/17. |
| ✅ **KB-VIO-126 suppression hook** | ✅ **GRADED 8/4 — benign branch lost** | correlations rise + constituent vol falls = benign | ⚠️ **Both legs are now printing the BENIGN direction** (COR1M +25%, constituent-vol 63.2 → 54.2) — **but the window closed 8/1 and the test is spent.** Do not re-grade a resolved test on new data; **register a new one or say nothing.** |
| 🔴 **KB-VIO-123 crack-vs-fade tree** | **VERDICT STANDS (FADE) — spent** | ①credit ②COT ≥95 ③MOVE ④VVIX 120 ⑤inversion ⑥VIX>20 | ② 76.3, fails · ③ ✅ above · ④ no (93.92) · ⑤ no (1.2535) · ⑥ no. |

---

## CONVERGENCE MATRIX

**Convergence Score: 23/55** *(prior 20 [8/4 settle], 21, 22, 24 [8/4 AM], 28/60 [7/31].)*

| Vector | Score | Read |
|---|---|---|
| Front-curve / term structure | 🟠 3 | VIX9D +16.8%, 9D/VIX 0.745 → 0.816, VIX3M/VIX flattening. **Up 1–2 — the clearest mover.** |
| SKEW / tail bid | 🟠 3 | Daily +16.50 pts in 9 sessions, back >140. ⚠️ **20d-avg regime terminated** — the two legs disagree. |
| Vol-of-vol (VVIX) | 🟡 2 | 93.92, +7.4%, highest since 7/29. Far from 120. |
| Rates vol (MOVE) | 🟠 3 | Re-crossed both lines 8/17; re-arm session 1 of 2. |
| Credit | 🟠 3 | BIN-B block active (CCC 10.18 ≥ 9.55); dispersion 8.59 through 8.00. ✅ **Now current (8/17), was 4 sessions stale.** Widened with the vol bid but only retraced the prior session — **score unchanged, staleness removed.** |
| Implied correlation | 🟠 3 | +25% off the episode low — **suppression unwinding.** Not yet a registered fire. |
| Positioning (COT) | 🟡 2 | Net short vol into a rising-vol tape; failed 8/04 long. ⚠️ 5 sessions stale. |
| Oil-vol (OVX) | ⚪ 1 | 48.01 [8/18] — **FIRE → WATCH**, and the downgrade came from VIX rising, not oil-vol falling. |
| JPY carry-vol | 🟡 2 | CALM, RV collapsed to 5.13% — but still through IV. |
| Equity level (HENRY-owned) | 🟡 2 | Not re-pulled this session. **[STALE — reference HENRY]** |
| Cheap-tail window | ⚪ 1 | 2/4 on 8/14 data; **a live re-run prints 0/4.** |

> 🔑 **THE SCORE ROSE 3 AND THIS TIME THE MOVE IS REAL, NOT A ROTATION.** Unlike 8/4 (where a 2-point move hid a re-composition — KB-VIO-178), **four vectors moved the same direction on one session**: front-curve, SKEW, MOVE and implied correlation all up on 8/17. ⚠️ **One vector remains stale: COT (8/11), and it cannot improve until Friday 8/21 by construction.** Credit refreshed to **8/17** (widened) and OVX to **8/18** (**FIRE → WATCH**) this session. 🔑 **Both stale values were biased toward the reading nobody re-checks** — credit flattered calm, OVX overstated stress. Neither would have prompted a look. **The score is a lower bound on staleness, not a confidence statement.**

---

## REGIME STATUS

**Regime: LOW_VOL** (VIX 15.19 settle / 15.78 tick — band 15–20). **Unchanged, and that is the honest read.**

- **What changed:** the **SKEW regime classification**, not the VIX regime. The elevated-SKEW (20d-avg ≥140) regime **terminated 8/17** after 49 td. That is a *tail-pricing* regime change, not a *vol-level* one.
- **What did NOT change:** VIX is still low, term structure still steeply contangoed (1.2535, 20% from inversion), VVIX far from stress, no gate has fired on my own registered lines.
- **⚠️ Principle-9 does NOT apply here.** *"Elevated regimes lasting ≥60 td are rare (5 in 19 yrs); all preceded significant VIX events."* **This run was 49 td — below the bar.** The ≥60td base rate **must not** be quoted against it. (Same discipline the 8/4 collapse needed: do not force an unmatched configuration into the nearest row.)
- **⚠️ Interrupt-and-resume, second instance.** 6/5 was itself a re-establishment 17 td after the 5/12 termination. **Do not compound regime-length statistics across the gaps** (KB-VIO-072, still deferred).

---

## POSITION SNAPSHOT

**FLAT.** No VIOLET-thesis position since `TRY-VIOLET-VIXCS` closed 7/30 (−$111.60, −38.8%, ended by its dated rule, not a thesis kill). **No stand-downs live. Nothing to manage.**

---

## CROSS-AGENT SIGNALS

| To | Signal | Priority |
|---|---|---|
| **RED** | 🔴 **Your SKEW>140 line is crossed — SKEW 142.91 [8/17 CBOE close].** Also: FT-06's stated precondition (*"SKEW sub-140 ⇒ spring being dismantled"*) has reversed since the 8/11 fire, exactly as WALTER's Friction 1 warned. **Measurement only — the ruling is yours.** | 🔴 |
| **RED / LIQUID** | 🟠 **RED-FT-01's exit is 10bp away, not 13 — HY OAS 2.70 [8/17 FRED, own pull], up from 2.67 [8/14].** WALTER flagged the 13bp proximity off the 8/14 print; the 8/17 print closes 3bp of it. **LIQUID owns the level, RED adjudicates the exit — routing the measurement only.** | 🟠 |
| **WALTER** | ✅ **Your SIG-W-20260810-004 ask is ANSWERED with the gross legs you said you could not see: 93% new longs, 7% covering — and it round-tripped at a loss by 8/11.** Full decomposition in KB-VIO-194 / board_log. | 🟠 |
| **HENRY** | 🟠 **Front-led vol bid 8/17 (VIX9D +16.8%) with no cause established on my side.** VIX Aug expiry is 8/19 (1d) — **pin/roll is an untested alternative to "fear" and I am not discriminating it.** Equity-side cause is yours. | 🟠 |
| **NEXUS / PROME** | 🟠 Elevated-SKEW regime terminated 8/17 (49 td); dispersion-suppression unwinding (COR1M +25%). | 🟠 |
| **PROME** | ✅ **Your 8/12 data note is DISCHARGED — VIX 14.55 [8/12] independently confirmed** at the CBOE primary (VIX_History.csv, own pull 8/18). Second witness owed, now delivered. | 🟢 |

---

## RESEARCH QUEUE

1. 🔴 **Grade the MOVE re-arm on today's print** (session 2 of 2, ≥72.41) and the **COR1M settle** (session 1 of 2, ≥8.43). Both resolve today; both are registered lines, so grade the **letter**.
2. 🔴 **Make CBOE `*_History.csv` PRIMARY for the VX_DAILY spot series, yfinance the cross-check.** Second feed needing the same inversion (MOVE was the first, KB-VIO-177). **A mechanism fix, not a content fix.** → KB-VIO-195
3. 🔴 **Backfill IMPLIED_CORR 8/11–8/17** — the gap makes the COR1M first-tell ungradeable on settles.
4. 🟠 **Rising-vol design (Option 1)** — still unbuilt, flagged since 8/10. **New input: this session gives it a live case to be specified against.**
5. 🟠 **BIN-A re-base** — delivered 8/4, awaiting Will. Unchanged.
6. 🟠 **DAEDALUS ratchet packet** (`TRADE.md:112–117`, arms 1-of-3 / stands down 3-of-3) — still unanswered.
7. 🟡 **Reconcile CATALYSTS.tsv against CALENDAR.md** — they have diverged (CALENDAR still shows 8/5 as "tomorrow"); CATALYSTS holds only 2 rows. Add the late-Sept MU print (SIG-W-20260807-001).

---

## THESIS CONNECTION

Thesis **v3.9** (2026-08-04). **This session is a candidate bump but I am not taking it:** a regime *termination* on the 20d-avg is a classification event the thesis already describes (§ SKEW regimes, KB-VIO-043/061/072), and one session of a broad vol bid is not a structural change. **Re-assess after today's settle** — if MOVE re-arms and COR1M starts a settle streak, that is two registered lines turning in one week and the framework's "dispersion suppresses index vol" section needs revisiting.

*Last write-back: 2026-08-18 ~09:45 ET (boot session, pre-open, basis TICK). Prior: 2026-08-10 (PROME-committed forum session).*
