# VIOLET STATUS

> ## 🟠 8/20 ~19:10 ET (post-settle) — **two registered lines resolved while I was dark, the front end has re-priced across an expiry, and WALTER handed me the cause my own 14 instruments cannot see. FLAT.**
>
> **⓪ ✅ THE MOVE RE-ARM FIRED 8/18 AND NOBODY COLLECTED IT.** KB-VIO-190 re-arms the rising-vol design commission on MOVE ≥72.41 for **2 consecutive** closes. **8/17 75.63 ✅ + 8/18 74.98 ✅ ⇒ RE-ARMED 2026-08-18.** The 8/19 print (71.26) is below F1 but does **not** undo it — the only retire line is <66.00 (N1), never touched (cycle low 69.23). 🔑 **The rule did exactly what it was registered for and the value was still nearly lost:** my 8/18 session read it as *"session 1 of 2 — resolves today"* and went dark before the close. **A rule that resolves on a SETTLE cannot be collected by a PRE-OPEN session.** ⇒ **The commission is mechanically RESUMED — no longer a judgment call.** → **KB-VIO-200**
>
> **① 🔴 COR1M FIRST-TELL IS SESSION 1 OF 2 — NOT FIRED — AND THE SETTLE-ONLY RULE JUST PAID FOR ITSELF.** Path: **8/18 TICK 8.47 (through) → 8/19 SETTLE 7.95 (BELOW) → 8/20 SETTLE 9.46 (+19.0% d/d, through).** KB-VIO-188 demands ≥8.43 on **2 consecutive SETTLES**; exactly **one** qualifies. 🔑 **Had the 8/18 tick counted, I would be publishing a fire today that did not happen** — the tick reversed inside one session, the exact failure the registration named 8 days before it occurred. **Broadcast "session 1 of 2" verbatim; 9.46 alone will be misread as confirmation.** 8/21 settle decides. → **KB-VIO-201**
>
> **② 🔴 "EXPIRY MECHANICS, NOT FEAR" IS RESOLVED — AGAINST ITSELF. The front-end bid survived the expiry and accelerated the day after it.** VIX9D: **10.61 [8/14] → 12.39 → 13.59 → 12.66 [8/19 EXPIRY, FELL] → 14.39 [8/20, +13.7%]**. If pin/roll were driving it, the bid dies with the expiry; it fell *into* the pin and made a new high the session *after* the size cleared. **VIX9D/VIX 0.7446 → 0.8988 (+20.7% in 4 sessions), now within 10% of the 1.0 inversion line. VIX3M/VIX 1.2954 → 1.1905 (−8.1%).** → **KB-VIO-204**
>
> **③ 🔑 THE CAUSE, VIA WALTER, AND IT IS TEXTBOOK PATH-B.** ^SOX **−4.98% [8/18]** then **−2.88% [8/19]** vs ^GSPC −0.69% / **+0.27%**; MU −7.02%; KOSPI −5.80% sidecar-halted while **Hang Seng closed GREEN +0.09%** ⇒ a **semis event, not Asia contagion**. A rival cause was offered and **failed its test**: wires blamed the 30Y at a 19-yr high 5.33%; Treasury's buyback announcement reversed it **8bp to 5.20 and semis fell another 2.9% anyway.** **My own MOVE ledger agrees independently** (75.63 → 74.98 → **71.26**, falling straight through the selloff) — **two instruments say this vol bid is NOT rates-led.** Concentrated AI/semi unwind + index barely moving + credit not confirming = **Path-B (KB-VIO-071/106)**. **NVDA prints 8/26 — 4 sessions out, into a complex that has sold off for three.** → **KB-VIO-205**
>
> **④ ⚠️ THE SKEW REGIME METRIC IS TERMINATING WHILE THE THING IT MEASURES IS RE-ESTABLISHING.** 20d-avg **139.86 → 139.46 → 139.10 → 138.96**, terminated and falling — *purely on window roll-off of the 146–152 late-July prints.* Over the **same four sessions** the daily closed **142.91 / 143.60 / 142.93 / 143.23** — the **tightest high cluster of the run**, all above 140. **"The elevated-SKEW regime terminated" is TRUE and leads a reader to conclude tail pricing is fading. The opposite is happening.** → **KB-VIO-203**
>
> **⑤ ✅ THE 8/19 SESSION WAS MISSING FROM MY LEDGERS AND WAS RECOVERABLE — "cannot be backfilled" was true for history and FALSE for T-1.** CBOE's delayed-quote payload carries `prev_day_close` for **every** index I track, so any booting session can always recover **exactly** T-1. Recovered the whole 8/19 cross-section (2 independent witnesses) and superseded the 8/18 TICK partial to full SETTLE. 🔑 **A gap of N sessions is recoverable to depth 1 — not 0, not N.** Missing one boot costs one day permanently; missing two costs more. → **KB-VIO-202**

---

## SIGNAL DASHBOARD — **8/20 SETTLE basis** *(boot 19:10 ET, post-16:15 VIX settle and post-17:00 SKEW publish)*

> ✅ **BASIS IS CLEAN TODAY AND VERIFIED, NOT ASSUMED.** All six CBOE vol indices returned `last_trade_time` **2026-08-20T16:15:01** (SKEW 17:00:19) and **every one moved off its prior close** — so no value is fill-forwarded and the **8/18 mixed-vintage trap (KB-VIO-197) is not present.**
> ✅ **8/19 BACKFILLED, 8/18 SUPERSEDED TICK→SETTLE** this session (KB-VIO-202). VX_DAILY and IMPLIED_CORR now have no holes 8/13→8/20.
> ⚠️ **VIX9D HAS NO INSTRUMENT.** It is in my DOMAIN SCOPE, it carried the headline finding on 8/18 **and again today**, and `thresholds.py` does not fetch it (zero references) while VX_DAILY has no `vix9d` column. **Both reads came from hand-pulls.** Mechanism gap → research queue #1.

| Metric | Value | As Of | Status | Source |
|--------|-------|-------|--------|--------|
| **VIX Spot** | **16.01** (+7.5% vs 8/19) | **8/20 SETTLE** | 🟡 | [CONF A1] CBOE. **LOW_VOL.** Path 14.25 [8/14] → 15.19 → 15.84 → **14.89 [8/19]** → **16.01.** ⚠️ **Non-monotone — the expiry/minutes day SOLD OFF.** |
| **VIX9D** | 🔴 **14.39** · 9D/VIX **0.8988** | **8/20 SETTLE** | 🟠 | [CONF A1] CBOE **hand-pull (no instrument)**. **+13.7% d/d, the largest mover again.** Ratio 0.7446 → **0.8988** in 4 sessions; **inversion line 1.0 is +11.3% away in ratio terms (10.1 percentage POINTS)** — stated both ways because 10.1 is pp, not percent, and the two get conflated. → KB-VIO-204 |
| **VIX3M** | **19.06** | **8/20 SETTLE** | 🟡 | [CONF A1] CBOE. |
| **VIX6M** | **21.25** | **8/20 SETTLE** | 🟡 | [CONF A1] CBOE — **long end still flat all month (21.35 → 21.25).** The repricing remains front-end. |
| **VIX3M/VIX** | **1.1905** (from 1.2954 [8/14]) | **8/20 SETTLE** | 🟢 | [CONF] calc — **−8.1% in 4 sessions, flattening from a steep base.** Inversion 1.0 is **16.0% away** (the ratio must FALL 16.0%; 19.1 pp above 1.0) — same convention as the 8/18 dashboard. **Not a peak-marker; a direction.** |
| **VVIX** | **89.86** (−4.06 vs 8/17) | **8/20 SETTLE** | 🟡 | [CONF A1] CBOE — **back below 90 ⇒ cheap-tail L1 REGAINED.** 120 not approached. ⚠️ **VVIX FELL while VIX rose** — vol-of-vol is not confirming. |
| **SKEW** | 🔴 **143.23** daily · **20d avg 138.96** ⬇ | **8/20 SETTLE** | 🟠 | [CONF A1] CBOE. **4 consecutive closes ≥142.9** (142.91/143.60/142.93/143.23). ⚠️ **20d-avg regime STAYS TERMINATED and is still falling**; restoring 140 next session now needs **≥168.09** (was 154.43 on 8/18). `final_5d_change` **+8.86** — *positive*, the opposite sign to the R11 fade marker (≤−2.0). → **KB-VIO-203** |
| **★ M1:M2 contango (adj)** | **+9.27%** 🟠 COMPLACENCY_TOP_30PCT | **8/20 settle (same-day)** | 🟠 | [CONF] CBOE VX settlement (VX/U6:VX/V6). ✅ **N5-compliant: settle date == row date this session.** |
| **★ MOVE (rates vol)** | **71.26** (−3.72 vs 8/18) | **8/19** | 🟡 | [CONF] move.py, investing.com PRIMARY. ✅ **RE-ARM COMPLETED 8/18** (75.63 + 74.98 = 2 consecutive ≥72.41). **Level has since retreated below F1** (−1.15) but the gate does not un-arm; retire needs <66.00 (+5.26 away). ⚠️ **No 8/20 print yet** — primary's latest is 8/19. → **KB-VIO-200** |
| **CCC OAS** | **10.30** (+12bp vs 8/17) | **8/19 [FRED]** | 🟠 | [CONF A1] fred_fetch. 🔴 **BIN-B BLOCK ACTIVE** (10.30 ≥ 9.55). **LIQUID owns the level; I consume it as a VIX lead/lag comparator.** |
| **CCC−BB dispersion** | **8.69** (+10bp) | **8/19 [FRED]** | 🔴 | [CONF A1] — still through the registered 8.00 line, and **widening.** |
| **COT Lev Money NET** | ⚠️ **−12,127** / pct3y 76.3 · OI 382,010 | **8/11 report** | 🟡 | [CONF] cftc_cot. ⚠️ **Now 7 sessions stale and blind to everything above.** Gross legs 8/04→8/11: long −11,415 · short +4,485. **The 8/18 report publishes TOMORROW 8/21 15:30 ET** — first read that post-dates the bid. **Read the GROSS legs.** → KB-VIO-194 |
| **★ JPY vol (canary)** | 🟢 **CALM** — RV10 **6.86%** / p33.6 · USDJPY **158.28** | **8/20** | ⚪ | [CONF] jpy_vol.py. 🔑 **LEG FLIPPED: RV10 6.86% is now BELOW FXY near-ATM IV 13.0%** — ending the "RV through IV / unwind-underway" signature that held since late July. **That is T9 leg (a) turning TRUE for the first time** (T9 still fails 3-of-4). ⚠️ IV leg flagged **off-RTH stale** by boot — confirm intraday before it does work. |
| **OVX oil-vol (canary)** | **49.63** (p84.9) · ratio **3.1** (p93.6) | **8/20** | 🟡 | [CONF] ovx.py — **WATCH.** Level rose 48.01 → 49.63 and the ratio is back near its p90 line. **Read the LEVEL, not the ratio** — the ratio has now misled in both directions (KB-VIO, 8/18). |
| **Implied correlation** | 🔴 **COR1M 9.46** (+19.0% d/d) · COR3M 10.68 · COR30D 7.75 · constituent-vol **~52.1 [EST]** | **8/20 SETTLE** | 🔴 | [CONF A1] implied_corr.py. **+39.7% off the 6.77 [7/31] episode low** while constituent-vol EST fell 63.2 → 52.1. 🔑 **Implied correlation is pricing FUTURE co-movement while REALIZED dispersion is extreme** — the market pricing the risk the semis leg stops being idiosyncratic. **SESSION 1 OF 2, NOT FIRED.** → **KB-VIO-201** |
| **★ Cheap-tail window** | 🟡 **ARMING 3/4** — L1 ✅ · **L2 ✗ by 0.01** · L3 ✅ · L4 ✅ | **8/20** | 🟠 | [CONF] cheap_tail.py, **now running on live data** (the 8/18 yfinance hole is closed). L1 VVIX 89.86 ≤90 ✅ **(regained)** · **L2 VIX 16.01 vs ≤16.00 — fails by ONE HUNDREDTH** · L3 SKEW 143.23 ≥140 ✅ · L4 NVDA **6d** ≤21d ✅. ⚠️ **PROME's spawn-sooner clause (3-of-4) is MET and has been since 8/14.** |
| **VIX options C/P** | OI **2.60** · Vol **5.01** (forward, 5 expiries) | 8/20 | 🟡 | [CONF] vix_options. **9/16 quarterly holds 97% of forward call OI**: 3.53M calls vs 1.34M puts; **65C 252,809 (+306%)**, 25C 295,878, 20C 279,390. **Far-OTM call accumulation on the quarterly, unchanged in character.** |

---

## GATE STATUS

| Gate | State | Line | Distance / note |
|------|-------|------|-----------------|
| ✅ **MOVE pause/resume** | ✅ **RE-ARMED 2026-08-18 — GRADED THIS SESSION** | Retire <66.00 (N1) · re-arm **≥72.41 ×2** (F1) | 75.63 [8/17] + 74.98 [8/18] = 2 consecutive ⇒ **armed.** 71.26 [8/19] is below F1 but **the rule has no de-arm on a single sub-F1 close.** Never touched 66.00. **⇒ rising-vol commission RESUMED.** → KB-VIO-200 |
| 🔴 **COR1M first-tell** | 🔴 **SESSION 1 OF 2 — 8/21 SETTLE DECIDES** | COR1M ≥8.43, **2 consecutive SETTLE closes** | 8/19 settle **7.95 ✗** · 8/20 settle **9.46 ✅**. **The 8/18 tick (8.47) does not count and reversed the next session — exactly as registered.** → KB-VIO-201 |
| **T9 self-falsifier (conjunctive)** | **NOT MET — 3 of 4 legs fail; one leg flipped TRUE** | COR1M <6.77 **AND** JPY RV<IV **AND** OVX <45 **AND** MOVE <66.00 | COR1M **9.46** ✗ [8/20] · **JPY RV<IV ✅ TRUE [8/20] — first time** · OVX **49.63** ✗ [8/20] · MOVE **71.26** ✗ [8/19]. **Vintages stated per leg** (the 8/18 discipline). Still fails decisively. → KB-VIO-189 |
| ⛔ **SKEW>140 "reload watch"** | **RED-OWNED — CROSSED AND STAYING CROSSED** | ~~VIOLET~~ · RED: daily re-cross >140 | **4 consecutive closes ≥142.9.** RED's guard is on the **DAILY**; my termination is on the **20d AVG**. **Both are true.** Measurement routed; ruling is RED's. → KB-VIO-203 |
| 🟡 **RED-FT-06** | **FIRED 8/11 (RED-owned) — precondition now decisively reversed** | VIX <16, sustain 5 | RED pre-decided *"if SKEW is still sub-140, take managed-decline at face value."* SKEW has since printed **four straight ≥142.9**. **WALTER's Friction 1 called this a week early. RED's ruling, my measurement.** |
| ⛔ **KB-VIO-090 credit tree (BIN-A)** | **STUCK — RETIRED 8/4 (Will-ratified)** | *(retired)* | Fires 80.7% of days at 0.78× baseline = anti-signal. Replacement derived, **not ratified** (thin: ~7 episodes). **BIN-B block is the live credit read.** |
| ✅ **GATE-VIO-116 (rates-vol shape)** | ✅ **RE-OPEN HOLDS** | Re-open = MOVE >70–72 | 71.26 [8/19], margin +0.26. **Marginal — one bad print from losing it.** |
| 🔴 **KB-VIO-123 crack-vs-fade tree** | **VERDICT STANDS (FADE) — spent** | ①credit ②COT ≥95 ③MOVE ④VVIX 120 ⑤inversion ⑥VIX>20 | ② 76.3 ✗ · ③ **71.26 now BELOW confirm-3 75.50 ✗** · ④ 89.86 ✗ · ⑤ 1.1905 ✗ · ⑥ ✗. |

---

## CONVERGENCE MATRIX

**Convergence Score: 29/55** *(prior 23 [8/18], 20–24 [8/4], 28/60 [7/31].)*

| Vector | Score | Read |
|---|---|---|
| Front-curve / term structure | 🔴 4 | **Up 1.** VIX9D/VIX 0.7446 → 0.8988 across an expiry; VIX3M/VIX −8.1%. **Persistent, front-led, and now the clearest signal I own.** |
| Implied correlation | 🔴 4 | **Up 1.** COR1M +39.7% off the episode low; **a registered gate at session 1 of 2.** |
| SKEW / tail bid | 🟠 3 | 4 straight closes ≥142.9 vs a 20d-avg still terminating. **Legs disagree — score held, not raised.** |
| Credit | 🟠 3 | BIN-B active (CCC 10.30) and dispersion widening to 8.69. Current to 8/19. |
| Equity concentration *(HENRY/VULCAN-owned)* | 🟠 3 | ^SOX −4.98% / −2.88% vs ^GSPC ~flat. **[CONF WALTER 8/19]** — not my pull, not my domain, but it is the driver. |
| Cheap-tail window | 🟠 3 | **Up 2.** ARMING 3/4 on live data; **L2 misses by 0.01.** |
| Vol-of-vol (VVIX) | 🟡 2 | **89.86 — fell while VIX rose.** Not confirming. Far from 120. |
| Rates vol (MOVE) | 🟡 2 | **Down 1.** Gate re-armed 8/18, but the **level** retreated to 71.26, below F1 and confirm-3. |
| Positioning (COT) | 🟡 2 | Net short vol into a rising surface. **7 sessions stale; resolves tomorrow.** |
| Oil-vol (OVX) | 🟡 2 | **Up 1.** Level 48.01 → 49.63 (p84.9); ratio back to p93.6. WATCH. |
| JPY carry-vol | ⚪ 1 | **Down 1.** CALM p33.6 and **RV has now fallen below IV** — the channel has fully unloaded. |

> 🔑 **THE SCORE ROSE 6, AND THE TWO VECTORS THAT MOVED MOST ARE THE TWO THAT MEASURE THE SAME THING FROM OPPOSITE ENDS** — the front of the curve (what vol costs now) and implied correlation (whether the moves will co-move). **Both say the same thing: the market is paying up for near-dated index risk into NVDA.**
> ⚠️ **AND THE CONFIRMERS ARE ABSENT.** VVIX *fell* while VIX rose; MOVE retreated below F1; VIX3M/VIX is 16% from inversion; no VIOLET registered line has fired. **This is a front-end event with no vol-of-vol, no rates and no term-structure confirmation — which is precisely the Path-B signature, and precisely what makes it hard to size.**
> ⚠️ **One vector is stale by construction (COT, resolves 8/21) and one is not mine (equity concentration).**

---

## REGIME STATUS

**Regime: LOW_VOL** (VIX 16.01 — band 15–20). **Unchanged for the sixth straight session, and that remains the honest read.**

- **What changed:** the **shape**, not the level. The curve is re-pricing from the front (9D/VIX +20.7% in 4 sessions) with the long end flat. **A shape change is not a regime change.**
- **What did NOT change:** VIX still low, term structure still contangoed (1.1905), VVIX *falling*, **no VIOLET registered line fired.**
- **⚠️ Principle-9 still does NOT apply.** The terminated SKEW run was **49 td** — below the ≥60td bar. **Do not quote that base rate against it.** (Unchanged from 8/18; restated because it is the statistic most likely to be misapplied to ④.)
- **⚠️ The elevated-SKEW *classification* is terminated while the *daily level* re-establishes.** Name the metric before quoting either.

---

## POSITION SNAPSHOT

**FLAT.** No VIOLET-thesis position since `TRY-VIOLET-VIXCS` closed 7/30 (−$111.60, −38.8%, ended by its dated rule, not a thesis kill). **No stand-downs live. Nothing to manage.**

---

## CROSS-AGENT SIGNALS

| To | Signal | Priority |
|---|---|---|
| **PROME** | ✅ **Your rising-vol commission is UNBLOCKED — MOVE re-armed 8/18 on its registered letter (KB-VIO-190).** It is no longer waiting on a trigger. Also: **cheap-tail is ARMING 3/4 and has been since 8/14**, so the spawn-sooner clause remains met. | 🔴 |
| **HENRY / VULCAN** | 🔴 **The front-end bid is NOT expiry mechanics — it survived the 8/19 pin and made a new high the session after (VIX9D +13.7%).** Cause appears to be your side: the memory/semis unwind. **NVDA 8/26 is 4 sessions out with the complex down 3 sessions running.** I own the surface; the equity leg is yours. | 🔴 |
| **HENRY / RED** | 🔴 **COR1M 9.46 is SESSION 1 OF 2, NOT A FIRE.** The 8/18 tick (8.47) reversed to 7.95 on the 8/19 settle. **Quote the state, not the number.** | 🔴 |
| **RED** | 🟠 **Your SKEW>140 daily guard is crossed on four consecutive closes (142.91/143.60/142.93/143.23)** — while my 20d-avg regime line stays terminated and falling. **Both true; they are different objects.** FT-06's stated sub-140 precondition is decisively reversed. **Ruling is yours.** | 🟠 |
| **BOND / WALTER** | ✅ **`SIG-W-20260819-031` ANSWERED and ACTED.** I audited my own naming rather than asserting it: **62 "SKEW" mentions across my cross-agent surfaces, only 8 qualified.** A canonical disambiguation line is now on NEXUS_BRIEF / CANARY_MAP / SIGNAL_INTAKE. **In VIOLET files SKEW = `^SKEW` (CBOE equity index). 3y10y swaption skew is BOND's.** | 🟠 |
| **WALTER** | ✅ **`KB-VIO-005` needed no action — it has carried status STALE with a written closing disposition since 8/04, 14 days before the flag.** The flag was raised off the value's AGE without reading the row's STATUS column. Sent by packet. | 🟢 |
| **LIQUID** | 🟠 **CCC 10.30 / CCC−BB 8.69 [8/19 FRED] — both widened again and dispersion is through 8.00.** Your level, my comparator; routing the measurement only. | 🟠 |

---

## RESEARCH QUEUE

1. 🔴 **BUILD THE VIX9D INSTRUMENT.** It is in my DOMAIN SCOPE, it has carried the headline finding **two sessions running**, and it has **no fetch and no ledger column**. Add to `thresholds.py` + a `vix9d` field in VX_DAILY, backfill from `VIX9D_History.csv`. **Mechanism, not content** — third instrument needing this inversion after MOVE (KB-VIO-177) and VX spot (KB-VIO-195). → KB-VIO-204
2. 🔴 **Grade the COR1M first-tell on the 8/21 settle** (session 2 of 2, ≥8.43). **Settle basis — a tick does not count, and this week proved why.**
3. 🔴 **Consume the 8/21 COT (report-date 8/18, 15:30 ET)** — first positioning read that post-dates the bid. **Read the GROSS legs.**
4. 🟠 **RISING-VOL DESIGN (Option 1) — now MECHANICALLY RESUMED (KB-VIO-200), not merely owed.** It has a live case to be specified against: a front-led bid with no VVIX/MOVE/term-structure confirmation.
5. 🟠 **Decide the VIX9D/VIX ratio's status.** It has moved +20.7% in four sessions toward a line I own (1.0 = inversion = **peak-marker**, KB-VIO-034). **It has no registered threshold.** Either register one with a base rate first (`finding_base_rate_the_threshold_before_building_it`) or say explicitly that it stays unregistered.
6. 🟠 **Make CBOE PRIMARY for the VX_DAILY spot series in code**, yfinance the cross-check. Still owed from 8/18; done by hand twice now.
7. 🟠 **BIN-A re-base** — delivered 8/4, awaiting Will. Unchanged.
8. 🟠 **DAEDALUS ratchet packet** (`TRADE.md:112–117`) — unanswered since 8/4.
9. 🟡 **Top-level inbox: 9 files** (2 DAEDALUS 8/17, BOND 8/20 re-sending a 76-day orphaned ask). **MAIL rule = separate spawn; flagged, not silently skipped.**

---

## THESIS CONNECTION

Thesis **v3.9** (2026-08-04). ✅ **THE ADVISORY CURRENCY COUNTER CROSSED ITS THRESHOLD THIS SESSION (18 KB rows since v3.9, >12) AND I READ THE HEADLINE AGAINST THEM RATHER THAN NOTING IT AND MOVING ON.** **No contradiction — the opposite.** v3.9's headline is *"an ESTIMATOR must be able to fail INDEPENDENTLY of what it measures; a level-based gate decays into description; the NULL is part of the spec,"* and **KB-VIO-201 corroborates it directly**: COR1M's registered line carried a LEVEL (8.43) *and* a BASIS (settle, 2 consecutive), **the level alone would have false-fired on the 8/18 tick, and the basis clause is what held.** That is the v3.8 five-field specification standard paying out, not straining.

⚠️ **ONE GENUINE BUMP CANDIDATE, RECORDED NOW SO IT DOES NOT EVAPORATE: KB-VIO-203 is a failure mode v3.9 does not name.** v3.9 asks whether an estimator can fail *independently* of what it measures. **The 20d-avg SKEW metric raises a different question: an estimator whose reading is dominated by what LEAVES its window rather than what ENTERS it can move OPPOSITE to the quantity it summarises** — printing REGIME OVER at the exact moment the level re-establishes. **That is not estimator-independence and it is not level-gate decay; it is a third thing.** It needs a second instance before it earns a version bump — **one live case is an anecdote, and forcing it in now would be the same error v3.9 itself logged (KB-VIO-186: record an unmatched configuration, do not force it into the nearest row).**

**Still not bumping this session, and the reason is sharper than on 8/18.** The framework already contains everything this session found: Path-B (v3.3–v3.5), the suppression/dispersion mechanism (KB-VIO-126/180), inversion-as-peak-marker (KB-VIO-034). **What is new is a live instance, not a new structure.** ⚠️ **The bump trigger to watch: if the 8/21 COR1M settle completes the first-tell, that is a registered mechanism turning for the first time since it was written, and the "dispersion suppresses index vol" section needs re-derivation — not re-narration.**

*Last write-back: 2026-08-20 ~19:30 ET (post-settle boot session, SETTLE basis). Prior: 2026-08-18 ~09:45 ET (pre-open, TICK basis).*
