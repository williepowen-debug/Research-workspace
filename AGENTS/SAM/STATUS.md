# SAM STATUS

**Signal Status:** 🔴 **CARRY-CONVEXITY TAIL — MED-HIGH (THESIS v1.6.11), PROVISIONAL on the Fri 8/7 CFTC print. Position FLAT.**

CFTC Jul-28 data **−163,412 = 90.8% of the −180K peak** (episode-deepest; WoW −11,287 REBUILD) fired the registered −153K/85% flip-condition → amplifier +5pp → **+8-10pp**, buckets **~8/23/32**. Provisional *by construction*: the fuel measurement is 7/28-vintage and **predates** both the 7/30 op and the 7/31 hawkish hold — SAM-22 (intervention → mass cover) and the 7/10 <12h whipsaw are the two named reversion paths. **Will's standing disposition: WAIT-FOR-8/7.** Nothing executed.

**Both frame legs remain simultaneously evidenced** — fuel at episode-max AND two trigger routes partially fired (intervention: an officially-confirmed, publicly **pledged two-sovereign** regime whose yen gains have now held **three sessions**, not just day+1; BOJ-hawkish: Oct OIS ~64%, Sep ~23%, Sep 17-18 MPM in-window at ~77% unpriced, now with **US Treasury publicly pressuring Japan on rates**). Conviction flip-conditions unchanged (CFTC-through-85% ✅ fired · yen-haven re-couple ⬜).

**8/4 in one line:** nothing crossed a registered line, so **no re-mark** — but three things moved that a later reader should not have to reconstruct: the **10Y auction printed the softest of the series** (belly, not super-long), **oil went through $80** (route-5 decaying), and **SAM-39's base rate was corrected upward** after repairing truncated range data (mark stands, claimed edge cut ~9pp).

*Detail → `thesis/THESIS.md` v1.6.11 · `CHANGELOG.md` 2026-08-04 · `outbox/2026-08-02_to-PROME_sam30-refire-adjudication.md` (canonical adjudication + the 8/7 entry resolver §5) · `thesis/INTERVENTION_2026-07-30_CONFIRMATION.md` (confirmation ladder).*

---

## 🟠 2026-08-04 BOOT NOTE (Tue ~10:33 ET — full boot sweep. Live levels below; JGB = MOF 8/3 pub.)

**(1) 🔴 JGB 10Y auction (today) — SOFTEST OF THE SERIES, and the deterioration is monotone.** Own MOF primary (`eresul20260804`): **BTC 2.558×, tail 6.0bp**, lowest accepted 2.900%, avg 2.840%. Four consecutive months of decay in **both** legs — BTC 3.904 [5/12] → 3.530 [6/2] → 3.130 [7/2] → **2.558**; tail 0.4 → 0.7 → 2.6 → **6.0bp**. Wires add (not own-verified): lowest BTC **since May-2025**, widest tail **in two years**; 10Y yield +3bp to 2.850%; named drivers = **consumption-tax funding uncertainty (fiscal) + BOJ early-hike risk** — precisely SAM's two tracked mechanisms. ⚠️ **This is the BELLY, not the super-long** — the demand-vacuum thesis and the Meiji ~4.0% floor are 30/40Y objects and are **not** what softened here. Read as hike-path + fiscal repricing, **not** as vacuum spreading. **Flagged, not re-marked** (no registered line crossed). Next super-long test = **Thu 8/6 30Y**.

**(2) 🟢 BOJ current account: NO third op indicated Monday.** Own primary `jp20260805.xlsx` (T+2 from Mon 8/3): 財政等要因 **−¥3.35T** — against SAM's own measured early-month peer group (day ≤6, n=10: median −2.54T, worst −6.21T) this is **ORDINARY**, nowhere near the −11.42T Aug-4 anomaly. The round does not appear to have continued into Monday. ⚠️ "No evidence of," not proof of absence — the instrument is **sovereign-blind** and cannot see a US-Treasury-only op at all. Full ladder + the Aug-4 grade → **`thesis/INTERVENTION_2026-07-30_CONFIRMATION.md`**. `jd20260804.xlsx` (the *actual* vs that projection) **404s — not yet published**; re-pull (the `jd` archive is durable, so it does not perish).

**(3) 🔴 SAM-39's registered base rate was measured on truncated data — CORRECTED, and it cuts the claimed edge.** Yesterday's L3 disagreement alarm fired on **4 pre-fix sessions outside the 10d self-heal window**; backfilled via a new `--revise-window` hatch (below). On repaired data the prior-year count is **3/259 = 1.16%/session → naive P(≥1 in 33 sessions) ≈ 32%**, not the registered **2/250 ≈ 23%**. SAM-39 @55% is therefore **~+23pp discriminating, not the ~+32pp written at registration.** ✅ **The mark itself stands** — the 60-session-pre-episode leg is unchanged (**0/60 ≥2.5y**; max 1.98y, not the stated 1.90y). ⚠️ **And the reference class is arguably wrong in SAM's favour:** 7/30 **5.82y**, 7/31 **3.73y**, 8/3 **2.67y** — three consecutive qualifying sessions immediately *before* the window opened. **8/3's 2.67y does NOT resolve SAM-39** (window starts 8/4) and is **not** being counted; recorded so nobody later mistakes it for a fired leg.

**(4) 🔧 `usdjpy.py` gains a `--revise-window N` backfill hatch.** L3 audits the full 60d hourly lookback but L2 only rewrote inside 10d — so pre-fix truncated rows were re-reported every run and could never self-heal. One-off `--revise-window 90` repaired the window (59 sessions, **all** stored ranges under-stating, direction consistent with the known defect); 1366 rows in → 1366 out, second run revises 0, alarm clears. Widening rewrites history, so it is a **flag, not a default**; both negative branches tested.

**(5) 🟠 Bessent doubles down (8/4) — US Treasury is now publicly pressuring Japan on RATES.** "Yen level problematic"; weakness "raises risks for Japan and other Asian currencies"; Treasury "would not hesitate" to intervene again — **but purchases "only curb volatility in the short term and would need to be followed by Japanese policies addressing the forces driving the yen lower"** [Bloomberg/CNBC 8/4]. That last clause is a **new mechanism on the BOJ-hawkish-of-priced route** (the largest in-window catalyst: Sep 17-18 MPM, ~77% unpriced). ⚠️ **NOT re-marked — could not source current Sep/Oct OIS today**, and rhetoric ≠ priced policy. This is exactly the SAM-08/20 failure cluster (two BOJ-hike calls lost to reading officials' words as policy). **Watch input; the re-mark needs an OIS print.**

**(6) 🟢 Oil de-escalation is now substantive — Brent $79.98, THROUGH $80.** −4.5% today, round-tripped from $100.43 [7/23]. Trump paused strikes on Iran **and announced talks to reopen Hormuz**; Iran denies direct talks but says Oman shipping discussions progress. **Phase-1 oil-in-yen pressure is decisively unwinding = yen-POSITIVE via the oil channel, NOT the Phase-2 haven bid.** Route-5 (oil/MOU re-escalation, ~10-11%/60d) is **decaying**; BRENT owns the sustain verdict.

**(7) Buckets UNCHANGED at ~8/23/32 — and the reason is not "nothing moved."** Two named anchors moved in **opposite** directions: route-5 oil/MOU **down** on the de-escalation, BOJ-hawkish-of-priced **up-risk** on the US rate pressure. Net ≈ offsetting, neither individually >5pp, and the hawkish leg is unpriced-unverified. Recording the offset rather than the silence, per the named-driver rule.

---

## LIVE MARKET DATA

*Live 2026-08-04 ~10:33 ET unless stamped. Root rule #4: never trade off these — pull live.*

| Instrument | Level | Note |
|---|---|---|
| **USD/JPY** | **157.49** | +0.19% d/d — **flat vs the 157.40 Fri close**, i.e. the post-op ~157 range is HOLDING into day 3. 5d −6.4y. 30d range 155.2-164.0 |
| FXY | $58.26 | −0.42% |
| EUR/JPY · GBP/JPY · AUD/JPY | 181.53 · 211.84 · 110.87 | all **+0.4-0.8%** = mild yen-side *softness* today, the mirror of Friday's move |
| **Brent (BZ=F)** | **$79.98** 🟢 | **−4.5%, THROUGH the $80 line**; round-tripped from $100.43 [7/23]. Hormuz-reopening talks |
| **JGB (MOF pub 8/3)** | 10Y **2.824%** 🔴 · 30Y **3.982%** · 40Y **3.948%** | 10Y breaches the 2.40% stress crossover (from 2.801 [7/30]); 30Y 1.8bp under the 4.0% Meiji floor |
| **JGB 10Y auction (8/4)** | **BTC 2.558× · tail 6.0bp** 🔴 | Softest of the tracked series, 4th straight month of decay in both legs. See boot note (1) |
| **CFTC JPY (Jul-28 data)** | **−163,412 / 90.8%** | own primary pull 8/2. Amplifier +8-10pp ON, residual ON. **Next print Fri 8/7 = THE print** |
| Intraday range | **5.82y 7/30** 🔴 INTERVENTION-GRADE · 3.73y 7/31 · **2.67y 8/3** | post-backfill (revised up from 5.74/2.17); see boot note (3)/(4) |
| Days since 160 touch | 4d — actors **MOF Jul2026 + US Treasury Jul2026** | |
| MOF weekly LT-debt | wk 7/19-25 **−¥811.4B SELL** (latest posted) | 2nd straight SELL week; **wk 7/26-8/1 not yet posted (~Thu 8/6) = the 3rd-week TRANSIENT confirm** |
| FXY options (8/4 snap) | Sep-18 **$60 call OI 33,980** (of 45,564 total) | ⚠️ **The 25d RR proxy is UNREADABLE right now — do not cite it.** Aug-21 printed +3.42 [8/2] → −77.0 [8/3] → −32.18 [8/4]; Sep-18 −24.66 → −5.66 → **+19.95**. The *sign* flips daily, so KB-183's "read sign not level" has no signal left to read. **OI is a count and remains readable:** the crowded $60 strike still sits exactly on the locked Sep-18 window-end |

**Durable reference rows:** PPI (CGPI) 7.1% YoY [Jun, rel 7/9] · BOJ subsidy-stripped trend gauge 2.8% [Apr] vs official core 1.4% (wedge +1.4pp) · insurer hedge ratio 44.4% [Mar 2025, 14-yr low — Pillar 3] · Tankan Q2 +22 [6/30] · Tokyo July CPI core **1.9** / core-core **2.0** [7/31] · National June CPI core 1.6 / core-core 1.7 [7/24] · Japan June TB **−¥406.9B** (imports +25.4%, crude value +59.3% YoY).

---

## CARRY UNWIND PROBABILITY (decomposed estimate — method → `thesis/THESIS.md` § CARRY-UNWIND PROBABILITY METHOD)

**LIVE: 7d ~8 · 30d ~23 · 60d ~32** (8/2, v1.6.11). Amplifier **+8-10pp**, residual ON.

| Re-mark | Buckets | Named driver (single-anchor discipline) |
|---|---|---|
| **8/2 (v1.6.11) — LIVE** | **~8 / ~23 / ~32** | **CFTC amplifier +5pp → +8-10pp** on the Jul-28 print through the strengthened band (−163,412 / 90.8%) — the registered >85% step, same mechanical class as v1.6.4. 7d 5→~8 additionally carries the live post-op tape (MOF #3 route **DECAYING → PARTIALLY-FIRED/LIVE**; its sustained-unwind conditional ~0.20 [CH-003 cap] now in evaluation) |
| 7/31 (v1.6.10) | 5 / 19 / 29 | **BOJ-hawkish-of-priced route ~8-9% → ~11-12%/60d** — Ueda presser repriced Oct OIS ~26-40% → **~64%** (through the registered >40% bar); Sep ~23% and named by Ueda; **Sep 17-18 MPM is IN-window** (decision day ON the inclusive Sep-18 boundary) → the "telegraphed before Sep-18" condition is MET |
| 7/16 (v1.6.8) | 5 / 18 / 27 | Last **full four-anchor re-pencil** (CFTC round-trip + Hormuz closure + USD/JPY 162.24). Anchor set: amplifier +5pp · oil/MOU ~10-11%/60d · Fed walk-back ~0 · BOJ-surprise ~8-9% · risk-off ~7-8% · residual ~10%. *Derivation retained in git history + CHANGELOG 2026-07-16* |

*(Superseded historical marks — Jun-3 measurement correction, Jun-14 six-input re-mark, the v1.6 ship-to-LIQUID/HENRY 5-6/17-20/24-28 — compressed 2026-08-02 → git history + CHANGELOG.)*

**Method caveats (standing).** The framework treats intervention as unwind-CAUSING, so a *lower* MOF probability lowers the buckets — it does **not** price the countervailing "no-MOF-cap → USDJPY overshoot → later disorderly unwind" path. Bucket shifts >5pp must attribute to a named driver. Future re-pencils must touch **all** changed anchors, not just one (Jun-14 derivation rule); the 7/31 and 8/2 marks are deliberately single-anchor mechanical steps, not re-pencils. Cross-agent disclosure uses "decomposed estimate (X%)," never "true probability."

---

## INTERVENTION STATUS — MOF posture

**Live posture (8/4): a PLEDGED, OFFICIALLY-CONFIRMED TWO-SOVEREIGN regime — this is no longer an "ambush-watch."** Both governments are on the record (Bessent 8/2; reaffirmed 8/4). MOF #3 route **PARTIALLY-FIRED/LIVE**. USD/JPY **157.49**, ~6 yen below the 163.49 pre-op level and **holding** into session 3 — the strike-watch's original premise (defending a one-way slide to 40-yr lows) is **inverted**: the live question is not "will MOF fire at 165" but **"is the crowd folding?"** — which the 8/7 print adjudicates. S1-A's ambush framing still governs *un-announced* ops (the 8/3 read says none fired Monday), but the regime's *existence* is now public, so silence is no longer the informational state it was.

**Hard-confirm clock:** MOF monthly for **Jul-30→Aug-27 releases ~Aug-31** and covers **both** days. Semi-confirm ladder → the table below (⚠️ the series is **`jp`** for projections, **`jd`** for actuals — the registered `jd` path for the projection was wrong; see `MOF_INTERVENTION_PLAYBOOK.md` S1-A SERIES CORRECTION). *(The prior window, Jun-29→Jul-29, printed **¥0** — hard-confirming the 7/2 no-strike adjudication; CH-011's cleanest stamp, MOF sat out the entire orderly grind to 40-yr lows.)*

| Date | Size | USD/JPY | Outcome |
|---|---|---|---|
| Apr 30 | ~¥5.48T ($35B) | 160.70 → 155.55 | same-day reclaim (5.15y range) |
| May 6 | ~¥4.3T ($28B) | 157.89 → 155.05 | same-day reclaim (2.84y range) |
| **Official aggregate Apr 28–May 27** | **¥11,734.9B ($73B)** | — | MOF monthly 5/29; largest round since 2022 |
| Jun 29 – Jul 29 window | **¥0** | — | MOF monthly 7/31 — 7/2 no-strike HARD-CONFIRMED |
| **Jul 30** | **~¥8.45T ($52.8B) — ESTIMATE, not MOF-official** (Bloomberg 7/31 off the BOJ Fri projection gap; ~1.5× the biggest prior single-day; Reuters source-confirmed the op itself) | 163.49 → **157.92** low → 159.46 NY settle; **day+1 close 157.3950 BELOW the op-day low** | **Gains EXTENDED day+1 — first of cycle; the n=2 reclaim-then-erode pattern is BROKEN.** SAM's own detector now grades it **INTERVENTION-GRADE (5.74y)**. Confound: 7/31 hawkish hold + Sep telegraph |
| **Jul 31 (16:00-17:00 ET)** | US Treasury size not disclosed; **MOF leg implied by the −¥11.42T Aug-4 settlement** (not a size) | 159.18 → **157.15** low → 157.40 close | ✅ **CONFIRMED — and it was TWO sovereigns.** The **US Treasury** (NY Fed selling **euros** on Treasury's own account) is officially confirmed by Bessent 8/2 — which is what mechanically explains the EUR/JPY leg. SAM's own 8/3 BOJ-projection read then evidences **MOF firing alongside**. The 8/2 "CANDIDATE / 35-min-grind-is-the-weak-leg" framing is **DEAD** — the shape read was the weaker discriminator and the official record overtook it |
| **Mon Aug 3** | — | ~156.80, session low 155.215 | 🟢 **No op indicated** — Aug-5 settlement projection −¥3.35T = ordinary for an early-month day. ⚠️ Japanese instrument only; a US-only op would be invisible |

**Actionable trigger (unchanged):** a **disorderly ≥1.5–2%/day** move (or ~2–3 yen in 1–2 sessions). S1-A: silence ≠ safe; the next op arrives unsignalled, so catch the follow-through, not the gap. Method → `MOF_INTERVENTION_PLAYBOOK.md` S1/S1-A.

### 🔧 CONFIRMATION LADDER — pre-registration, grade, and the 8/4 re-read

**→ Full record: `thesis/INTERVENTION_2026-07-30_CONFIRMATION.md`** (bands written *before* any file was opened, committed `aa3ad1980`; the measured base rate; two instrument-scoping corrections). Moved out of STATUS 2026-08-04 — a closed pre-registration whose value is the timestamping. **External citations point at that path; do not delete it without re-checking who points there.**

| Settlement | Instrument | Reading | Verdict |
|---|---|---|---|
| **Aug-4** (T+2 from Fri 7/31) | `jp20260804.xlsx` projection | 財政等要因 **−¥11.42T** | 🔴 **ANOMALOUS — 1.44× the largest ordinary fiscal day in a measured n=62 sample.** Evidences **MOF ALSO firing** around 7/31 = a genuinely **two-sovereign op**; fires the pre-registered second-MOF-op branch |
| **Aug-5** (T+2 from Mon 8/3) | `jp20260805.xlsx` projection | 財政等要因 **−¥3.35T** | 🟢 **ORDINARY** for its early-month peer group (day ≤6: median −2.54T, worst −6.21T) → **no third op indicated Monday** |
| **Aug-3** (T+2 from Thu 7/30) | `jp20260803.xlsx` | **rotated off** — HTTP 200 with an HTML body | ⚠️ **UNVERIFIED, not refuted.** The `jp` endpoint retains only the current projection. Only remaining independent read = MOF monthly ~Aug-31 |
| Aug-4 *actual* | `jd20260804.xlsx` | **404 — not yet published** (8/4 ~10:35 ET) | Owed re-pull; the `jd` archive is durable, so this does not perish |

⚠️ **Three standing limits on this whole ladder:** (1) **no Tanshi broker forecast** — the real signal is the *gap*, and the BOJ projection alone cannot separate an op from a large ordinary fiscal day; (2) these are **projections**, not provisional/final; (3) the instrument is **sovereign-blind** — it reads *Japanese* fiscal factors, so a **US-Treasury-only op is invisible here by construction** and a null can never be graded "no op." **Do not restate any of these figures as an intervention size** — each is a fiscal-factor line containing an op plus ordinary flows.

## KEY THRESHOLDS

| Level | Significance | Status (live 8/4 ~10:33 ET; JGB = MOF 8/3 pub) |
|-------|-------------|--------|
| USD/JPY 160 | MOF/US zone (disorder-not-level) | 🟢 **157.49 — BELOW the zone**, 4d since the 160 touch. Direction reversed hard off the 163.83 [7/23] 40-yr low and is **holding**, not reverting |
| USD/JPY 155 | Phase 2 carry-unwind onset | 🟡 **1.6% away.** Mon 8/3 traded a **155.215 session low — the closest approach since May-6** (155.05) |
| USD/JPY 147 | Forced carry unwind | SET |
| USD/JPY 145 | Mechanical insurer selling (Pillar 3) | SET |
| JGB 10Y 2.40% | Stress crossover | 🔴 **BREACHED — 2.824%**, up from 2.801 [7/30]. **8/4 auction cleared with a 6.0bp tail** = the belly is being repriced, not bid |
| JGB 30Y 4.0% | v1.6.3: **demand FLOOR with a named bid under it** (Meiji Yasuda) — not a clean disorderly trigger (SAM-26 trap / CH-014) | 🟠 **3.982% — 1.8bp under the floor**, up from 3.971 [7/30]. Floor confirmed REAL FLOW (7/7 30Y BTC 4.55x; 7/22 40Y BTC 2.83x). **Next test: 8/6 30Y auction — and the 8/4 belly softness makes it a live test, not a formality** |
| JGB 40Y | — | 🟠 **3.948%** (from 3.967 [7/30]) |
| Brent $90 | Headwind resolved | 🟢 **RESOLVED — $79.98, THROUGH the line** (−4.5% d/d; round-tripped from $100.43 [7/23]). Phase-1 oil-in-yen pressure decisively unwinding |
| Brent $120 | Kharg-scenario Phase 1 shock | 🟢 far off; $115 "Phase-1-reasserts" line no longer proximate |
| **CFTC −153K / 85%** | **convexity-tail flip-condition** | 🔴 **FIRED — −163,412 / 90.8%** (Jul-28 data), through by 10,412. Amplifier +8-10pp |
| **CFTC −108K / 60%** | leg-1 invalidation (SAM-29 cover-tail → frame LOW) | 🟢 **55,412 away** — moved further out of reach |
| CFTC −140K | DE-LOAD line (Will's 7/10 resolver, re-used 8/7) | watch at the 8/7 print |
| DXY | USD-side carry signal | ~sub-101 — Warsh Fed-HIKE regime intact |

---

## WHAT TO WATCH (forward only — full docket → `docket/CALENDAR.md`)

| When | Event | Why it matters |
|---|---|---|
| **Thu 8/6** | **JGB 30Y auction** | First super-long under the reaffirmed FY2027 purchase path; 30Y is 1.8bp under the Meiji floor. **Upgraded to a live test by the 8/4 belly softness** — does the ~4.0% super-long bid still show up when the 10Y just cleared at a 6bp tail? |
| Thu 8/6 | MOF weekly wk 7/26-8/1 | **3rd-week confirm** of the SELL reversal — 2 SELL weeks already overturned the 7/16 DURABLE read |
| 🔴 **Fri 8/7 3:30 PM ET** | **CFTC (Aug-4 data) — THE print** | First attribution-capable read (saw both the op and the hold) **and** the pre-registered entry resolver. Terms (memo §5B): **≤−153K held = CONFIRM/enter** · **−140K to −153K = NOT-CONFIRMED**, decompose legs (longs-up materially = fresh haven = SAM-31 candidate → escalate HENRY) · **past −140K = DE-LOAD repeats**, revert MEDIUM |
| Fri 8/21 | Japan National July CPI — **first 2025-BASE print** | Measurement discontinuity: re-baseline the subsidy wedge + core-core **before** any YoY comparison |
| ~Mon 8/31 | MOF monthly (Jul-30→Aug-27) | **Hard confirm + the only independent size read** for BOTH days. The 7/30 projection leg is permanently unverified (file rotated off) — this is what closes it |
| **Fri 9/18** | **Convexity-tail window END (LOCKED, inclusive)** | Sep 17-18 BOJ MPM decision lands ON the boundary; retire-check runs at Sep-18 close, after the decision prints |

**Watch-for-entry triggers (flat book):** disorderly spike (catch the follow-through) · ~~CFTC through −153K/85%~~ ✅ **FIRED 8/2, provisional on 8/7** · risk-off yen-haven re-couple / VIX spike (SAM-31, still decoupled) · Fed-dot walk-back (route 4 — Warsh regime intact, 3 hawkish FOMC dissents 7/29, stays cold) · 30Y 4.5% disorderly (v1.6.7: J-GAAP statutory-impairment TAIL, **mid-cap Fukoku/Asahi bifurcation watch** — precursor only). **Early-entry overrides (memo §5C):** fresh ≥2%/day disorderly move · **confirmed** second op · haven re-couple.

⚠️ **Override §5C is adjudicated FIRED ON THE LETTER and deliberately NOT ACTED ON (8/3 ruling, unchanged 8/4).** The text says "a confirmed second op of the round," not "second **MOF** op — and the US op is confirmed. It is not being acted on because **the trigger was announced to SAM and to the whole options market in the same public statement: there is no informational lead to monetise.** Plus root rule #6 (long FXY = the call side into a green tape, with no refuting direct measurement on the card). **Standing disposition: WAIT-FOR-8/7.** Recorded here because a fired-but-unacted override is exactly the thing a later reader mistakes for an oversight.

---

## POSITION — 🟢 FLAT (Will-confirmed 2026-06-29)

SAM carries **no FXY position**. No close price / date / realized-P&L recorded — none provided; **do NOT fabricate one** (TBD from Will).

The carry-convexity-tail is a **WATCH-FOR-ENTRY thesis on a flat book.** At MED-HIGH the registered flip-up math reclaims net EV ~+1.3% — **but that math equates 7/28-vintage measured fuel with current fuel, and that equality is exactly what 8/7 adjudicates.** Will's standing disposition is WAIT-FOR-8/7. Vehicle reopens cleanly (no legacy spot) → **defined-risk options preferred over spot** when a trigger fires; TERRY constructs, Will [Approve]s, root rule #4 at any fill.

*Historical decision record (13→6 trim 6/22, stop FXY ≤$55.05, the expired Jun-18 $58C, the declined Sep $60 call) → `TRADE.md` Entry Decision Card + CHANGELOG. Modal band (7/10 re-derivation): modal $55.3-57.7 / 159-166 · downside tail $59.2-62.0 / 148-155 · upside disorder-tail <$54.9 / >167 — ⚠️ **the 7/30-31 move pierced the 159 modal floor; band re-derivation owed** (METSUKE E2).*

---

## CHANNELS · BOJ · FED (compressed — canonical taxonomy → `thesis/THESIS.md`)

- **Ch1 Life-insurer repatriation — RETIRED.** 4-of-4 institutions grew US credit through their 2026 windows; Norinchukin CLO record ¥10.1T. Re-add **only** on a direct foreign-SALES print across ≥2 consecutive windows at ≥2 institutions; JGB-30Y / ESR-sub-200% = accelerant co-conditions **never** the necessary leg (double-counting Pillar 2 under a Ch1 label — [[finding_threshold_vs_mechanism]]). Next reads: Norinchukin interim ~Nov 2026; H2 FY2026 plans Oct-Nov 2026; FY2026 ESR May 2027.
- **Ch2 → CARRY-CONVEXITY TAIL** = the live frame. **Ch3 MOF #3** = PARTIALLY-FIRED/LIVE (above). **Ch4 POSITIONING-CONVEXITY** = the v1.6 center; leg-1 invalidation −108K, leg-2 Sep-18 no-trigger.
- **BOJ:** policy rate **1.00%**. July MPM held 8-1 with a **hawkish Takada dissent for 1.25%**; Outlook = upside-dominant price risks, underlying inflation "risks overshooting 2%", new overshoot-*management* framing, FX pass-through "stronger than in the past"; FY2027 purchase plan untouched. **Oct OIS ~64%, Sep ~23%; Ueda named September** as the start of upside-risk debate. Takaichi political ceiling **fading** (Reuters) — directly relevant to SAM's #1 failure cluster (SAM-08 @90%, SAM-20 @60%, both FAILED on that ceiling). Board dovish-on-path via Sato/Asada. *Full grade → `thesis/BOJ_2026-07-31_PREREGISTRATION.md`.*
- **Fed — HIKE regime under Warsh (route 4 cold).** Jun-17 dots +40bp inverted Pillar 1; 7/29 FOMC held 3.50-3.75% with **3 hawkish dissents** (Hammack/Kashkari/Logan — first unified 3-dissent since Sep-2016). Tripwire = any walk-back of the Jun-17 dot revision; needs a US-credit cascade to break the frame.

---

## COMPRESSED SESSION-NOTE POINTERS

> ### ↪️ MOVED: § BOJ MPM PRE-REGISTRATION · § GRADE · SAM-38 contamination clause
> **These sections now live at `thesis/BOJ_2026-07-31_PREREGISTRATION.md`** (verbatim, 2026-08-02 compression pass). Redirect kept here because **external consumers cite them by section name** — notably `AGENTS/WALTER/design/SIGNAL_PROCESSING_CHECKLIST.md` §v0.30 (the fleet-wide pre-decision-contamination guard) and WALTER's processed 7/31 packet. Per [[finding_external_consumer_check_before_restructure]]: do not delete this line without re-checking who points here.

*Narratives live in `thesis/timeline/TIMELINE.md`; full bodies in git history. Compressed 2026-08-02 (this pass): 7/29 boot + BOJ pre-registration/grade → `thesis/BOJ_2026-07-31_PREREGISTRATION.md`; 7/9, 7/10 AM+PM, 7/11, 7/17, 7/21, 7/23 notes → pointers below. Prior passes: 7/11 (7/6-7/8 + late-June), 7/23 (7/16).*

- **7/31** — BOJ July MPM graded live: **SAM-38 CONFIRMED at FULL-C**, SAM-34 CONFIRMED. MOF monthly ¥0. Buckets → 5/19/29 (v1.6.10). → TIMELINE Jul 24-31 + the archive file.
- **7/30** — 🔴 yen +2.7% intraday, suspected ~¥8.45T MOF op. VIOLET canary first-ever FIRE→WATCH; **equity vol never transmitted** (VIX −17.3% = evidence against an Aug-2024 replay). → TIMELINE Jul 24-31.
- **7/29** — CFTC RE-BUILD to −152,125/84.5% (875 ct from the re-fire line); MOF weekly REVERSAL (2 SELL weeks overturn the 7/16 DURABLE read); **oil-yen war-attribution test FAILED** (USD/JPY held 163.6-163.8 through an ~11% Brent round-trip → oil is decoration on a structurally-driven weak yen); VIOLET IV/RV correction (3.24× was OVX, not JPY); FOMC 3-dissent hold. → archive file §§1-5.
- **7/23** — Brent through $100 on actual tanker strikes; **SAM-35 CONFIRMED** (40Y BTC 2.83x firm-lean, marginal; tail unverifiable); USD/JPY 163.83 fresh 40-yr low, orderly; Bloomberg BOJ-faster-pace tell (watch input, **not** re-marked — failure-cluster discipline). → TIMELINE Jul 11-23.
- **7/21** — USD/JPY through 163 orderly; oil-escalation cluster all risk-premium not supply-loss (FAL-01 unfired); **June TB −¥406.9B = Phase-1 oil-in-yen CONFIRMED yen-negative** (own MOF-customs pull); JGB 30Y rally hard-verified 4.013→3.905. → TIMELINE Jul 11-23.
- **7/17** — CFTC Jul-14 **STALL** −122,663/68.1%, **SAM-37 CONFIRMED**; positioning sticky ~68% post-flush, two-sided. → TIMELINE Jul 11-23.
- **7/16** — double-discriminator day: MOF weekly +¥1.09T → BND-11 DURABLE-leaning *(since reversed by two SELL weeks)*; four-anchor re-pencil 5/18/27; MSG-002 DM v1 first live test closed. → TIMELINE Jul 11-23.
- **7/10-7/11** — **SAM-30 CONFIRMED (AM) → SAM-36 FALSE/DE-LOAD (PM), the <12h whipsaw** — the precedent making today's fire provisional; Katayama GPIF jawbone; `gpif_flows.py` PARTIAL-path bug fixed; CH-010 re-scoped → v1.6.7 (J-GAAP impairment TAIL, mid-cap bifurcation watch). → TIMELINE Jul 6-10.
- **7/9** — Japan-leg read on the US 30Y reopen's 77.74% indirect surge = **safe-haven-transient, not duration-extension-durable** (MEDIUM); GPIF tracker built (FY2025: domestic bonds +¥14.75T vs foreign bonds +¥2.65T — Japan's largest pool added ~5.5× more at home); WALTER consume-step installed, 18-file backlog drained. → TIMELINE Jul 6-10.
- **6/29 – 7/8** — position reconciled to **FLAT**; JGB demand-vacuum thesis executed → v1.6.1, RED-corrected → v1.6.2; **SAM-32 FALSE** (Meiji Yasuda ~4% floor) → v1.6.3; MOF-verify NO-STRIKE + ambush regime (S1-A); 7/7 30Y auction FIRM (BTC 4.55x) = floor confirmed real flow. → TIMELINE Jun 22-Jul 2 + Jul 6-10.
- **Pre-6/29 resolved pointers** — MOF playbook built 6/25 (S1 amended → S1-A 7/2) · FOMC Jun-17 Warsh (+40bp dots → Pillar 1 inverted) · BOJ Jun-16 hike as-priced, **no unwind = CH-004 confirmed** (SAM-21/24 ✅, SAM-23/26 ❌, both pre-marked) · Jun 1-6 Iran MOU break + CFTC build. → TIMELINE Jun blocks.

---

## 🔴 PRE-REGISTRATION — INTERVENTION CHARACTER (written 2026-08-03 ~11:15 ET, **BEFORE** the Fri 8/7 15:30 ET print)

*Closes `MSG-PROME-20260803-001#SAM-01`. Timestamped pre-print by design: answered after Friday, the answer is contaminated by the outcome. Falsifiable form → `thesis/PREDICTIONS.tsv` **SAM-39**.*

**QUESTION:** does an officially-confirmed, publicly *pledged*, US-backstopped yen appreciation **COMPRESS** the disorderly-move tail a long-FXY convexity structure buys, or **FATTEN** it?

**VERDICT: FATTEN — in yen-space only, NOT the Aug-2024 cross-asset cascade. Confidence MEDIUM.**

**Mechanism (3 legs):**
1. **Intervention ops *are* the highest-range events in the series** — own repaired data: 7/30 **5.82y**, 7/31 **3.73y**, Apr-30 5.15y, against a 60-session pre-episode max of **1.98y** *(corrected 8/4 from 1.90y after the historical backfill)*. A pledged, repeatable two-government regime is therefore a **high-realized-range** regime in USD/JPY, directionally aligned with long-FXY. ⚠️ *The intuitive read inverts here:* their **stated objective** is countering disorder, but their **method** — large one-sided buying — **is itself the disorderly move.*
2. **The reaction function is asymmetric in our favour.** They act against yen *weakness*; having declared the yen **"substantially undervalued"** (Bessent 8/2) they have no political appetite to cap yen *strength*. The official put sits **under** the yen, upside uncapped.
3. **Same-side flow.** Official buying and short-covering are *both* yen-buying; at 90.8% of record short the carry crowd is the only structural seller — fuel, not damper.

**Why MEDIUM and not HIGH (the honest counterweight):**
- **The Aug-2024 replay is NOT supported by my own evidence** — on 7/30, the largest yen move since Dec-2023, **VIX FELL 17.3%** and equity vol never transmitted. Cross-asset legs stay decoupled; SAM-31 unfired.
- **A managed, gradual appreciation is a live alternative** that pays a convexity structure nothing — and it **cuts at my own leg (1)**: if the yen keeps strengthening unaided (156.80 on 8/3), officials need not act, so my mechanism *requires official action that may prove unnecessary*.
- Oil de-escalation removes Phase-1 yen pressure, further reducing the need to intervene.

**Base rate — 🔧 RE-MEASURED 2026-08-04 on repaired data (the registered figure was computed on truncated ranges):**

| | Registered 8/3 | **Corrected 8/4** |
|---|---|---|
| 60 sessions pre-episode ≥2.5y | 0/60 | **0/60** — unchanged |
| pre-episode max range | 1.90y | **1.98y** (7/2) |
| prior-year ≥2.5y | 2/250 (~0.8%/sess) | **3/259 (~1.16%/sess)** — adds 2025-08-01 alongside Apr-30 / May-6 |
| naive P(≥1 in ~33 sessions) | ~23% | **~32%** |
| SAM-39 @55% edge vs base | ~+32pp | **~+23pp** |

**The mark STANDS at 55%; the *rationale* was overstated by ~9pp and is corrected here** — the edge is real but ~28% smaller than written. Held deliberately below enthusiasm given the documented over-confidence cluster (SAM-08 @90%, SAM-20 @60%, both FAILED).

⚠️ **The counterweight, stated against my own interest:** the naive base rate may be the *wrong reference class* — 7/30 **5.82y**, 7/31 **3.73y** and 8/3 **2.67y** are three consecutive qualifying sessions immediately before the window. Drawing from "a random year" understates a live pledged-intervention regime. **8/3's 2.67y does NOT resolve SAM-39** — the window opens 8/4 and the row is not being credited — but it is why 55% is more likely too LOW than too high. **Not re-marking mid-flight on one day's tape.**

**→ CONVERSION-RULE IMPACT: NONE. The GATE-SAM-30 resolver map is UNCHANGED** (≤−153K = CONFIRM/enter · −140K..−153K = decompose legs · past −140K = DE-LOAD, revert MEDIUM). The resolver measures whether the **fuel** is intact; this verdict measures whether the **payoff mechanism** survives. Different questions — **a fatten read does not license loosening the fuel test.** Explicitly *not* relaxing the rule on an unpriced mechanism read: that is the exact shape of the SAM-30 → SAM-36 <12h whipsaw.

**Out of scope, unresolved:** **pricing.** A fattened tail at a fat price is not an edge. ⚠️ **The FXY vol proxy is still unreadable on 8/4 — and now demonstrably so, not merely "degraded":** the 25d RR *sign* has flipped on consecutive days at both live tenors (Aug-21 +3.42 → −77.0 → −32.18; Sep-18 −24.66 → −5.66 → +19.95). KB-183 says read the sign not the level; there is currently **no stable sign to read.** **Distribution is SAM's call; price is TERRY's — and TERRY should price off the live chain, not this proxy.**

---

## PREDICTIONS

**6 OPEN — SAM-28** (≥1 tail-route fires ≥+3% FXY by Sep-18, 40%) · **SAM-29** (net does NOT cover below −108K by Sep-18, 65%) · **SAM-31** (yen-haven channel re-couples by Sep-18, 35%) · **SAM-33** (no BOJ emergency long-end capping through Dec-31, 72%) · **SAM-39** (intervention-character test — ≥1 session ≥2.5y USD/JPY range 8/4→9/18, 55%; base rate corrected 8/4, mark unchanged) · 🆕 **SAM-40** (the 8/7 CFTC resolver, 45% CONFIRM-band). **Scoreboard 14 CONFIRMED / 12 FAILED / 1 special.** Canonical → `thesis/PREDICTIONS.tsv` (read the calibration preamble before writing any new row); post-mortems → `PREDICTIONS_ARCHIVE.md`.

✅ **SAM-40 REGISTERED 2026-08-04 ~11:10 ET, before the Fri 8/7 15:30 ET print** — closes the owed item. The resolver terms were already a *disposition* (memo §5B); scoring them converts it into a calibration datum, so the 8/7 outcome grades SAM's judgment rather than only triggering an action. **Terms unchanged from §5B — deliberately not re-tuned while writing the row** (re-tuning a resolver at scoring time is how a resolver becomes unfalsifiable): **net ≤−153K held = CONFIRM/enter (45%)** · **−140K..−153K = NOT-CONFIRMED, decompose legs (~30%)** · **past −140K = DE-LOAD repeats, revert MEDIUM (~25%)**.

---

*Thesis: `thesis/THESIS.md` v1.6.11 · audit trail: `thesis/CHANGELOG.md` · cross-agent surface: `NEXUS_BRIEF.md` · playbook: `MOF_INTERVENTION_PLAYBOOK.md` · decision rules: `STRATEGY.md`.*
