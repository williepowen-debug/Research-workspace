# SAM STATUS

**Signal Status:** ⚰️ **CARRY-CONVEXITY TAIL — RETIRED TO LOW (THESIS v1.7, 2026-08-07). Leg-1 SPF FIRED. Position FLAT; $0 was at risk.**

🔴 **The 8/7 print broke the frame.** CFTC Aug-4 data **−45,473 = 25.3%** of the −180K peak (from −163,412 / 90.8%) — **through the −108K/60% leg-1 invalidation line by 62,527 contracts and 34.7pp**, 42 days before the Sep-18 horizon. WoW **+117,939** (longs +45,957 / shorts −71,982) = **3.8× the largest prior weekly cover in the series**. Open interest barely moved (−12,973) ⇒ **position REVERSAL, not liquidation**: the crowd *turned around* inside the two-sovereign intervention window (7/30, 7/31, 8/3, 8/4) after a ~5.3% adverse move. Verified twice before propagation — `cftc_jpy.py` and an independent hand-parse of raw `deafut.txt`, agreeing to the contract.

**Resolver run ON THE LETTER** (terms frozen 8/4, not re-tuned): **DE-LOAD**. ⚠️ **But it exceeded the map** — §5B's *"revert MEDIUM"* was written for a 7/10-style de-load at 68.8%, which does not trip leg-1. This print does. Applying both registered rules as written → **LOW, a thesis-BREAK, not a downgrade of degree.**

**Predictions:** ❌ **SAM-40 FAILED** (45% CONFIRM modal missed; the ~25% DE-LOAD branch fired) · ❌ **SAM-29 FAILED** (leg-1). Scoreboard **14 CONFIRMED / 14 FAILED / 1 special / 4 OPEN**.

**Calibration, stated plainly:** SAM assigned **45%** to CONFIRM and **~25%** to what happened. A real miss on the modal lean, and the third member of the documented over-confidence cluster (SAM-08 @90%, SAM-20 @60%) — this time in the *opposite* direction. **What worked, recorded with equal precision because it is repeatable:** the MED-HIGH grade carried a **PROVISIONAL** flag from award *because* the fuel measurement predated the op; **SAM-22's mechanism (intervention → mass cover) and the 7/10 <12h whipsaw were both named in advance** and the path that fired was on the list; the resolver was frozen 3 days early and run on the letter; the book was **FLAT**; and the §5C override that fired **on the letter** on 8/3 was deliberately **not acted on** — had it been, the book would have been long into this print.

⚠️ **NO SUCCESSOR FRAME IS DECLARED.** The open question for v1.8+, written down so it cannot be quietly skipped: **the carry trade substantially unwound — and the yen is at 157.5, not 145. What is the thesis when the positioning fuel has already burned and the level barely moved?** Do not answer it from inside the old frame.

*Detail → `thesis/THESIS.md` v1.7 · `CHANGELOG.md` 2026-08-07 · `outbox/2026-08-07_to-TERRY-PROME_RESOLVER-COMPLETE-section8-DE-LOAD-leg1-fired-frame-LOW.md` · pre-print re-pencil `thesis/REPENCIL_2026-08-07_PREPRINT.md` (committed BEFORE the print).*

---

## 🔴 2026-08-07 CLOSEOUT — THE PRINT, AND WHAT ELSE MOVED

**(1) 🔴 CFTC Aug-4: −45,473 / 25.3%.** Covered above. **The single largest positioning event in the tracked series.**

**(2) 🟢 JGB 30Y auction 8/6 PASSED its live test — the one clean piece of good news.** BTC **3.864×**, tail **1.5bp**, avg 3.937% (own MOF primary). The Meiji ~4.0% super-long floor held on the first real test after the 8/4 10Y cleared at a 6.0bp tail — **belly softness did NOT spread to the super-long.** Third consecutive floor confirmation (7/7 4.55× → 7/22 40Y 2.83× → 8/6 3.864×). Long end rallied into it. **Pillar 2 and the JGB demand-vacuum thesis are UNAFFECTED by the carry break.**

**(3) 🟡 MOF weekly (wk 7/26-8/1) = NO VERDICT. +¥478B** — reverses two SELL weeks but misses the ≥+¥500B DURABLE bar by ¥22B. 🔧 **BND-11 RULING: the 3-week test is SPENT/INCONCLUSIVE and the single-week form is STOOD DOWN** — its bar sits at **0.49σ** of the series' own dispersion (σ ≈ ¥1.02T, n=26), i.e. inside noise, with 4 sign flips in 8 weeks. 4-week rolling replacement proposed; **BOND ratifies** (it is BOND's gate). Current 4-wk rolling **+¥33B ≈ flat**.

**(4) 🔴 Sep BOJ pricing repriced AGAIN, and the single-witness problem is now fixed.** Sep 17-18 cumulative **39.7% → 45.6%** (8/6). Derived independently from **TFX 3m-TONA futures settlements** — the actual instrument — with the Reference Quarter verified against the TFX rulebook rather than assumed. Method reproduces centralbank.watch to **−0.5bp on 8/3**, then diverges **+3.4bp on 8/6** (futures price MORE tightening than the meeting-attribution captures). Curve shift concentrated **26.09/26.12/27.03, dying past 27.06** = a **hike PULL-FORWARD**, not term premium. **Carry Sep unpriced as a BAND, ~40-54%, never a point estimate; the Sep/Oct split is NOT identified — the blend caveat travels on every citation.**

**(5) 🟠 Route 4 (Fed walk-back) re-rated COLD → LIVE-but-UNFIRED** on the 8/7 NFP (−23K, −103K net revisions; Sep Fed **hike** odds 57% → 43.9%). ⚠️ **Not fired** — the tripwire is an **FOMC** walk-back of the Jun-17 dots, not a market repricing. **LABOR's composition caveat (which trimmed my own mark):** private **+30K** vs government **−53K**; the U-3 fall to 4.1% is participation-driven = **NO-SIGNAL** under LABOR's L-06; LABOR's matrix went **34 → 32/75, cycle-low bearishness**.

**(6) 🟢 SAM-31 still UNFIRED, and today was counter-evidence.** Today's yen strength is **dollar-side**: DXY −0.45% of USD/JPY's −0.59%, and against USD the yen was **mid-pack** (CHF +0.62% > JPY +0.59% > AUD +0.56% > EUR/GBP +0.37%). **A high-beta commodity currency matched the yen and the franc beat it** — that is not a haven bid. VIX 14.88 (−1.8%) with equities rallying on a negative payroll. Second failed re-couple test in 9 days.

**(7) ⚠️ The BOJ `jd` current-account archive path appears DEAD, not merely unpublished.** `jd20260804` 404s at every registered pattern including `…/d_release/jd/<YYYY>/` — **and so does `jd20260731`, which must exist**, since the SAM-39 base rate (n=62, May 1–Jul 31) was measured from that archive. **Consequence: that base-rate measurement is not currently reproducible.** n=3 failed sessions. Owed: proper path discovery, not another blind retry.

---

## ↪️ 8/4 BOOT NOTE — COMPRESSED 2026-08-07 (superseded by the closeout above)

*The 8/4 session's seven notes (10Y auction V-shape correction · no-third-op read · SAM-39 base-rate correction · `usdjpy.py --revise-window` · Bessent rate-channel + the OIS sign correction · oil through $80 · CPI pipeline restored + the KB-169 self-falsification) are **retained verbatim in git history** and their surviving conclusions are carried in the 8/7 closeout above, `CHANGELOG.md` 2026-08-04, and `MAINTENANCE.md`. Compressed here because the print superseded the frame they were describing.*

## LIVE MARKET DATA

*Live 2026-08-07 ~15:0x-16:0x ET unless stamped. Root rule #4: never trade off these — pull live.*

| Instrument | Level | Note |
|---|---|---|
| **CFTC JPY (Aug-4 data)** | 🔴 **−45,473 / 25.3%** | **THE PRINT.** From −163,412/90.8%; WoW **+117,939** (longs +45,957 / shorts −71,982) on ~flat OI (419,393, −12,973) = **position REVERSAL**. **Amplifier OFF · residual OFF · leg-1 FIRED** |
| **USD/JPY** | **157.53** | −0.59% d/d. Intraday 158.576 / 156.652 = **1.924y** (widest since 8/3's 2.67y; **short of the SAM-39 2.5y bar**, session not closed at time of write) |
| FXY | $58.23 | +0.59% |
| EUR/JPY · GBP/JPY · AUD/JPY · CHF/JPY | 182.20 · 212.67 · 111.36 · 195.08 | −0.22 · −0.22 · −0.03 · **+0.03** — ⚠️ **yen mid-pack: vs USD, CHF +0.62 > JPY +0.59 > AUD +0.56 > EUR/GBP +0.37.** A high-beta commodity FX matched the yen ⇒ **dollar-side move, NOT a haven bid** |
| DXY · EUR/USD · VIX | 99.52 (−0.45%) · 1.1600 (+0.37%) · **14.88 (−1.8%)** | Risk-**on** tape on a negative payroll; equities rallied |
| **Brent (BZ=F)** | **$83.31** | +0.99%; retraced UP from the 8/4 $79.98 low, still far below $100.43 [7/23]. ⚠️ Route 5 is **proxy-marked** — BRENT v5.4: throughput is the test, and PortWatch `chokepoint6` is dark since 7/23 |
| **JGB (MOF pub 8/6)** | 10Y **2.773%** 🔴 · 30Y **3.919%** · 40Y **3.912%** | Long end **rallied ~7bp** off 8/4 into a firm auction. 10Y still breaches the 2.40% crossover |
| **JGB 30Y auction (8/6)** | 🟢 **BTC 3.864× · tail 1.5bp** | **PASSED its live test** — Meiji ~4.0% floor held; belly softness did NOT spread to the super-long. 3rd consecutive floor confirmation |
| **BOJ OIS (as-of 8/6)** | Sep **45.6%** cum · Oct 75.6% · Dec 88.4% | ⚠️ Sep unpriced = a **BAND, ~40-54%**, never a point estimate; **Sep/Oct split NOT identified — the blend caveat travels on every citation.** TFX 3m-TONA primary corroborates direction; +3.4bp richer than the meeting-attribution on 8/6 |
| MOF weekly LT-debt | wk 7/26-8/1 **+¥478B** | **NO VERDICT** (misses the ≥+¥500B bar by ¥22B). BND-11 single-week form **stood down** — bar was 0.49σ of the series' own noise. 4-wk rolling **+¥33B ≈ flat** |
| Days since 160 touch | 7d — actors **MOF Jul2026 + US Treasury Jul2026** | USD/JPY ~6.2 yen below the 163.74 pre-op close; **has not round-tripped** |
| FXY options | Sep-18 **$60 call OI 33,980** | ⚠️ **25d RR remains UNREADABLE** (non-physical, sign flips daily) — TERRY prices off the live chain, never this proxy. OI is a count and stays readable |

**Durable reference rows:** PPI (CGPI) 7.1% YoY [Jun, rel 7/9] · BOJ subsidy-stripped trend gauge 2.8% [Apr] vs official core 1.4% (wedge +1.4pp) · insurer hedge ratio 44.4% [Mar 2025, 14-yr low — Pillar 3] · Tankan Q2 +22 [6/30] · **Tokyo July CPI core 1.9 / core-core 2.0 [7/31] · National June core 1.6 / core-core 1.7 [7/24]** — 🔴 **Tokyo is now running ABOVE national on core-core** (June pairing +0.2pp), the FIRST inversion in 8 paired months; Tokyo's 2.0 is AT target · Japan June TB **−¥406.9B** (imports +25.4%, crude value +59.3% YoY).

---

## CARRY UNWIND PROBABILITY (decomposed estimate — method → `thesis/THESIS.md` § CARRY-UNWIND PROBABILITY METHOD)

🔴 **LIVE: 7d ~3 · 30d ~8 · 60d ~13** (8/7, v1.7). Amplifier **OFF**, residual **OFF**.

| Re-mark | Buckets | Named driver |
|---|---|---|
| **8/7 (v1.7) — LIVE. Full four-anchor re-pencil, fuel plugged in.** | **~3 / ~8 / ~13** | **TWO named drivers.** ① **Fuel collapse 90.8% → 25.3%** → amplifier **+8-10pp → OFF**, residual **OFF** (both gates need >60%). ② **Route 6 (residual positioning cascade) ~10% → ~2-3%** — 🔴 *the structural point, not a haircut:* **a carry unwind requires a carry position to unwind, and it just unwound.** The remaining routes (BOJ ~7-8 · MOF ~8 · risk-off ~6-7 · Fed ~7-8 · oil ~8-9) still exist, but their payoff-conditional-on-firing is far smaller with no crowd to cascade. **Non-fuel anchors were computed and COMMITTED BEFORE the print** (`thesis/REPENCIL_2026-08-07_PREPRINT.md`, `ce71c5cbf`) so the fuel outcome could not contaminate them |
| 8/2 (v1.6.11) | 8 / 23 / 32 | CFTC amplifier +5pp → +8-10pp on the Jul-28 print (−163,412 / 90.8%). **Reversed 5 days later** |
| 7/31 (v1.6.10) | 5 / 19 / 29 | BOJ-hawkish-of-priced ~8-9% → ~11-12%/60d on the Ueda presser (Oct OIS → ~64%) |
| 7/16 (v1.6.8) | 5 / 18 / 27 | Last prior full four-anchor re-pencil |

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
| ~~CFTC −153K / 85%~~ | ⚰️ **VOID** — was the convexity-tail flip-condition | Fired 7/31 (Jul-28 data), **reversed 8/7**. ⚠️ **A future re-build back through this line re-arms NOTHING** — it was a *reclaim* condition inside a frame that no longer exists |
| **CFTC −108K / 60%** | leg-1 invalidation (SAM-29) | 🔴 **FIRED 2026-08-07 — −45,473 / 25.3%, through by 62,527 contracts and 34.7pp.** SAM-29 FAILED; frame → LOW |
| CFTC −140K | DE-LOAD line | 🔴 **BREACHED 8/7** — SAM-40's DE-LOAD branch fired |
| DXY | USD-side carry signal | ~sub-101 — Warsh Fed-HIKE regime intact |

---

## WHAT TO WATCH (forward only — full docket → `docket/CALENDAR.md`)

*⚰️ The **watch-for-entry trigger list and the §5C override block are DELETED**, not archived-in-place: the frame they served is retired, and a stale trigger list on a live surface is exactly what a later reader mistakes for a plan. Their full text + the 8/3 fired-but-unacted §5C adjudication survive in git history and in `outbox/2026-08-02_to-PROME_sam30-refire-adjudication.md`.*

| When | Event | Why it matters |
|---|---|---|
| Wed 8/12 | US CPI (July data) | **Route-4's now-binding leg.** The labor blocker weakened 8/7; inflation is what is left holding the Warsh HIKE regime in place |
| Mon 8/17 | Japan Q2 GDP 1st prelim | Wage/activity input to a live Sep/Oct hike debate |
| Thu 8/20 | JGB 20Y auction · Japan July TB | Super-long demand series (**Pillar 2 — unaffected by the carry break**) · Phase-1 oil-in-yen read |
| Fri 8/21 | **Japan National July CPI — first 2025-BASE print** | ⚠️ Measurement discontinuity: re-baseline the subsidy wedge + core-core **before** any YoY comparison |
| ~Mon 8/31 | **MOF monthly (Jul-30→Aug-27)** | **Hard confirm + the only independent size read** for BOTH op days. Now the *only* remaining independent read — the BOJ `jd` archive path appears dead (see closeout note 7) |
| Thu 9/3 | JGB 30Y auction | Meiji ~4.0% floor series — the live Pillar-2 test after 8/6's firm print |
| 🔴 Tue-Wed **Sep 15-16** | **FOMC (SEP) — dot plot** | **Route 4's actual test.** A walk-back of the Jun-17 +40bp revision is the registered tripwire; the 8/7 payroll only weakened the blocker |
| ⚠️ **Sep 17-18** | **BOJ MPM** | Sep unpriced is a **BAND ~40-54%** (not a point estimate; Sep/Oct split unidentified). ⚠️ **This is now a macro watch, not an entry catalyst** |
| **Fri 9/18** | **SAM-28 / SAM-39 grading horizon** | ⚠️ **No longer a "window-end retire-check"** — the frame already retired on 8/7 via leg-1. Sep-18 survives **only** as the grading date for the two remaining window-scoped predictions |

## POSITION — 🟢 FLAT (Will-confirmed 2026-06-29; still flat through the 8/7 break)

SAM carries **no FXY position, and never opened one.** **$0 was at risk through the entire convexity-tail episode (Jun-22 → Aug-7).** Do NOT fabricate a close price or P&L — there is no trade.

⚰️ **There is no longer a watch-for-entry list.** The frame those triggers served is RETIRED (THESIS v1.7). The old gate — *disorderly MOF spike / CFTC through −153K/85% / haven re-couple / Fed-dot walk-back* — **is void, not unfired**: every one paid off *through the positioning fuel*, and the fuel is gone. **Re-entry requires a fresh, independently-argued build thesis (v1.8+), not a threshold tag.**

**TERRY: TRY-FIRE-007 STANDS DOWN** — no Monday re-mark, do not arm (packet sent 8/7 ~15:5x ET).

> **Why $0 was at risk is repeatable, not lucky:** ① the MED-HIGH grade was flagged **PROVISIONAL at award** because the fuel measurement predated the op; ② **WAIT-FOR-8/7** held; ③ Will's **Monday-execution ruling was pre-registered the morning of the print, before the number existed**; ④ the **§5C early-entry override fired ON THE LETTER on 8/3 and was deliberately not acted on** (no informational lead — it was announced to SAM and the options market in the same public statement — plus root rule #6). **Had ④ been taken, the book would have been long into this print.**

*Historical decision record (13→6 trim 6/22, stop FXY ≤$55.05, the expired Jun-18 $58C, the declined Sep $60 call) → `TRADE.md` + CHANGELOG. ⚠️ Modal-band re-derivation (METSUKE E2) is **moot** for the retired frame; do not re-derive bands for a dead structure.*

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

**4 OPEN — SAM-28** (≥1 tail-route fires ≥+3% FXY by Sep-18, 40%) · **SAM-31** (yen-haven re-couples by Sep-18, 35%) · **SAM-33** (no BOJ emergency long-end capping through Dec-31, 72%) · **SAM-39** (≥1 session ≥2.5y USD/JPY range 8/4→9/18, 55%).
**Scoreboard 14 CONFIRMED / 14 FAILED / 1 special.**

🔴 **CLOSED 2026-08-07 — both FAILED:**
- **SAM-40** (the 8/7 resolver, 45% CONFIRM-band) — **the ~25% DE-LOAD branch fired.** A real miss on the modal lean. Resolver run **on the letter**, terms frozen 8/4, **not re-tuned at scoring time**.
- **SAM-29** (net does NOT cover below −108K by Sep-18, 65%) — **leg-1 fired, 42 days early.** 65% said the cover was the *tail*; it was neither tail nor mode but a **single-week regime break** (+117,939 WoW) inside an intervention window.

**Calibration note:** this is the third member of the over-confidence cluster (SAM-08 @90%, SAM-20 @60%) — **but in the opposite direction**: the prior two over-weighted a *thesis-favourable* outcome on a political-ceiling read; this one over-weighted *positioning persistence* against a named, pre-registered mechanism (SAM-22: intervention → mass cover) that I had **already written down as one of the two ways the grade could die.** ⚠️ **The failure was not missing the mechanism — it was pricing it at 25% while holding a MED-HIGH grade that the same document called PROVISIONAL.** *Naming a risk and then under-weighting it is a distinct error from not seeing it, and it is the one to carry forward.*

**SAM-28 is now very likely to fail and is deliberately NOT graded early** — its horizon is Sep-18 and grading it today would be exactly the resolver re-tuning I refused this afternoon.

Canonical → `thesis/PREDICTIONS.tsv` (read the calibration preamble before writing any new row); post-mortems → `PREDICTIONS_ARCHIVE.md`.

---

*Thesis: `thesis/THESIS.md` v1.6.11 · audit trail: `thesis/CHANGELOG.md` · cross-agent surface: `NEXUS_BRIEF.md` · playbook: `MOF_INTERVENTION_PLAYBOOK.md` · decision rules: `STRATEGY.md`.*
