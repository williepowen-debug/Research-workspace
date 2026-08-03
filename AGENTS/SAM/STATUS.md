# SAM STATUS

**Signal Status:** 🔴 **CARRY-CONVEXITY TAIL — MED-HIGH (THESIS v1.6.11), PROVISIONAL on the Fri 8/7 CFTC print. Position FLAT.**

CFTC Jul-28 data **−163,412 = 90.8% of the −180K peak** (episode-deepest; WoW −11,287 REBUILD) fired the registered −153K/85% flip-condition → amplifier +5pp → **+8-10pp**, buckets **~8/23/32**. Provisional *by construction*: the fuel measurement is 7/28-vintage and **predates** both the 7/30 suspected ~¥8.45T MOF op and the 7/31 hawkish hold — SAM-22 (intervention → mass cover) and the 7/10 <12h whipsaw are the two named reversion paths. **Will dispositioned this 8/2: WAIT-FOR-8/7 + TERRY re-mark of TRY-FIRE-005 Mon 8/3** (Aug-21 tenor excludes the Sep 17-18 MPM — must roll past Sep-18). Nothing executed.

**For the first time both frame legs are simultaneously evidenced** — fuel at episode-max AND two trigger routes partially fired (MOF #3: record-size op whose yen gains EXTENDED day+1; BOJ-hawkish: Oct OIS ~64%, Sep ~23%, Sep 17-18 MPM in-window at ~77% unpriced). Conviction flip-conditions unchanged (CFTC-through-85% ✅ fired · yen-haven re-couple ⬜).

*Detail → `thesis/THESIS.md` v1.6.11 · `CHANGELOG.md` 2026-08-02 · `outbox/2026-08-02_to-PROME_sam30-refire-adjudication.md` (canonical adjudication + the 8/7 entry resolver §5).*

---

## 🔴 2026-08-02 BOOT NOTE (Sun ~17:06 ET — real-SAM boot, Will-directed. Integrates + owns the 8/2 proxy run. Markets: FX week reopening; all levels are Fri 7/31 closes or stamped publication vintages.)

**(1) ✅ Proxy re-mark VERIFIED AND OWNED.** Re-pulled CFTC at primary myself (`cftc.gov/dea/newcot/deafut.txt`, vintage 260728): noncomm **101,271L − 264,683S = −163,412**, OI 432,366, WoW longs −6,319 / shorts +4,968. Reproduces the proxy, PROME and NEXUS **to the contract**. MED-HIGH / +8-10pp / ~8/23/32 stand as written. Will's disposition (WAIT-FOR-8/7 + TERRY re-mark) already landed via PROME `6c1d17bed` — the memo §5 hand-off is CLOSED.

**(2) 🔴 SAM's own MOF-disorder detector was silently blind — FIXED (commit `34069b8c0`).** `scripts/usdjpy.py` compared London-labelled yfinance bar dates against a **local (Eastern) "today"**, so any boot run after ~19:00 ET appended the *next* London-day's few-hours-old partial bar as final; idempotent-by-date then made it permanent. **10 of the last 60 sessions were truncated, every one under-stating the range.** Worst case is the one that matters: **2026-07-30 was recorded as a 0.33y day — true range 5.74y.** The intraday-range alert (SAM's independent intervention detector, CRIT 4.0y) printed *"normal daily range"* on the largest yen move since Dec-2023. Post-fix it fires **INTERVENTION-GRADE 5.74y on 2026-07-30** — against Apr-30-2026's 5.15y, a *confirmed* ¥5.48T op. **SAM now corroborates the 7/30 op from its own instrument, not only from the wires.** Failure mode was FALSE-NEGATIVE and silent; workbook repaired from fresh bars + re-sorted. *(Class: [[finding_mtime_is_corrupted_by_git_sync]]-adjacent — a freshness/vintage guard keyed to the wrong clock.)*

**(3) 🟠 NEW — Fri 7/31 closed on a yen-specific slide in the final hour: CANDIDATE MOF op #2, UNRESOLVED.** Verifying the proxy's 157.3950 close surfaced the shape nobody had logged. Between **16:00 and 16:57 ET**:

| Pair | 16:00 → low | Move |
|---|---|---|
| USD/JPY | 159.18 → 157.15 | **−1.28%** |
| EUR/JPY | 183.55 → 181.12 | −1.33% |
| GBP/JPY | 214.51 → 211.69 | −1.32% |
| AUD/JPY | 111.97 → 110.29 | −1.50% |
| EUR/USD | 1.1534 → 1.1533 | **flat** |
| GBP/USD | 1.3476 → 1.3483 | **flat** |

Yen up ~1.3% against **every** major while the dollar crosses did not move = **pure yen-side**, the same signature as 7/30 (EUR/JPY −400 pips in minutes). Placed in the **thinnest liquidity window of the week**, in the **NY session** — the same venue as the Reuters-source-confirmed 7/30 op, two days later. ⚠️ **Honest limit — do not book this as an op:** the move was a ~35-min *progressive* slide, not 7/30's ballistic candle; month-end real-money flow and a stop cascade into the weekly close are live competing causes, and the shape is the weaker discriminator. **Discriminators:** T+2 settles into the **Tue 8/4** BOJ current account (same Tanshi-gap method as the 7/30 semi-confirm, manual per playbook S1-A); both 7/30 and 7/31 fall in the **same MOF monthly window (Jul-30→Aug-27, ~Aug-31)**. **Registered relevance: "a confirmed second op of the round" is a pre-registered EARLY-ENTRY OVERRIDE (memo §5C). It has NOT fired — candidate only.**

**(4) The "gains extended" finding is stronger than the proxy stated.** Not merely that Friday closed below the op-day low — the yen made **new lows of the entire move at the week's close** (157.151 on 7/31 < 157.923 on 7/30), going into a weekend. That is the inverse of the n=2 same-day-reclaim-then-erode pattern (Apr-30, May-6). Confound stands: hawkish hold + Ueda's September telegraph are live competing causes for Friday's strength, and n=2 sessions is not durability.

**(5) Intake — read, not processed** (normal-boot protocol; no DM v1 `MSG-*.md` present). **PROME 8/2 GasLog Shanghai:** Qatari LNG carrier struck **in Hormuz 8/1** — 3rd LNG kinetic event, 2nd GasLog hull in 4 days; theater-checked Hormuz (not Bab), does not corroborate the separate IRGC 7/31 two-tanker claim. Feeds the **owed Japan-LNG/JKM item**. **WALTER SIG-W-20260802-001 (landed mid-session):** Trump **ordered then cancelled** strikes on Iranian **energy sites** on claimed deal parameters; **daily exchange PAUSED** (3rd pause of the cycle; the 7/24 one broke in 4 days); Tehran has not confirmed. Kpler Hormuz transits 22 → 5 (−77%). **SAM read: a genuine de-escalation unwinds oil-side Phase-1 yen pressure — yen-POSITIVE via the oil channel, NOT the Phase-2 haven bid.** No re-mark (unconfirmed, and Phase-1 relief is not a convexity trigger). WALTER had live uncommitted work — its files left untouched; lane file not `git mv`'d.

**(6) Hygiene:** STATUS compressed 409 → under cap this pass (3 sessions overdue, now cleared). The resolved BOJ-July frozen pre-registration + grade moved verbatim to **`thesis/BOJ_2026-07-31_PREREGISTRATION.md`** (kept as a retrievable *path*, not just git history — it carries the contamination clause, an audit artifact). **Batch-3 P3-Asia packet NOT started** — its gate is "first boot on or after Mon 8/3"; today is Sun 8/2.

---

## LIVE MARKET DATA

*Fri 7/31 closes unless stamped. Root rule #4: never trade off these — pull live.*

| Instrument | Level | Note |
|---|---|---|
| **USD/JPY** | **157.40** | Fri 7/31 FX-week close (17:00 ET), verified 3 ways (hourly bar · investing.com · live quote). −1.39% d/d. ⚠️ `usdjpy.py`'s headline still prints ~160.18 — Yahoo's daily FX *Close* field is a bar-boundary snapshot (Open≈Close on every row). Separate open defect; needs a source decision, not a one-liner |
| FXY | $57.66 | +0.14%. NB: 4 PM ET equity close — **misses** the 16:00-17:00 ET yen leg above, so FXY-implied USD/JPY (~159.4) reads high vs the true 157.40 |
| EUR/JPY · GBP/JPY · AUD/JPY | 181.50 · 212.05 · 110.69 | all −1.3%-class = yen-side |
| Brent (BZ=F) | $90.12 | round-tripped from $100.43 [7/23] |
| **JGB (MOF pub 7/30)** | 10Y **2.801%** 🔴 · 30Y **3.971%** · 40Y **3.967%** | 10Y breaches the 2.40% stress crossover; long end back up toward the 4.0% Meiji floor (from 3.905 [7/21]) |
| **CFTC JPY (Jul-28 data)** | **−163,412 / 90.8%** | own primary pull 8/2. Amplifier +8-10pp ON, residual ON |
| Intraday range | **5.74y on 7/30** 🔴 INTERVENTION-GRADE · 2.17y on 7/31 | post-fix; see boot note (2) |
| Days since 160 touch | 2d, no MOF | |
| MOF weekly LT-debt | wk 7/19-25 **−¥811.4B SELL** (latest posted) | 2nd straight SELL week; **wk 7/26-8/1 not yet posted (~Thu 8/6) = the 3rd-week TRANSIENT confirm** |
| FXY options (8/2 snap) | Aug-21 ATM IV 13.65%, 25d RR **+3.42** · Sep-18 ATM IV 9.42%, RR **−24.66** | Aug-21 RR positive = FXY puts bid (yen-weakness demand, counter-thesis). ⚠️ **Sep-18 carries 48,860 call OI, 33,987 at the $60 strike — sitting exactly on the locked window-end.** Observation only: KB-183 says read this proxy's *sign*, not its level, and it is non-physical at extremes |

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

**Live posture (8/2): AMBUSH regime (S1-A) + disorder-not-level (CH-011). MOF #3 route re-marked DECAYING → PARTIALLY-FIRED/LIVE.** The 7/30 op is source-confirmed as an *occurrence* (Reuters, NY session; Nikkei) though **not MOF-official** on size. USD/JPY **157.40**, roughly **6 yen below** the 163.49 pre-op level and below the op-day low — the strike-watch's whole premise (defending a one-way slide to 40-yr lows) is, for now, **inverted**: the live question is no longer "will MOF fire at 165" but **"is MOF still firing, and did the crowd fold?"** — which the 8/7 print adjudicates.

**Hard-confirm clock:** MOF monthly for **Jul-30→Aug-27 releases ~Aug-31** and now covers **both** the 7/30 op and the 7/31 candidate. Semi-confirm: BOJ current-account T+2 — `jd20260803.xlsx` (~8/4) for the 7/30 op, `jd20260804.xlsx` for the 7/31 candidate. *(The prior window, Jun-29→Jul-29, printed **¥0** — hard-confirming the 7/2 no-strike adjudication; CH-011's cleanest stamp, MOF sat out the entire orderly grind to 40-yr lows.)*

| Date | Size | USD/JPY | Outcome |
|---|---|---|---|
| Apr 30 | ~¥5.48T ($35B) | 160.70 → 155.55 | same-day reclaim (5.15y range) |
| May 6 | ~¥4.3T ($28B) | 157.89 → 155.05 | same-day reclaim (2.84y range) |
| **Official aggregate Apr 28–May 27** | **¥11,734.9B ($73B)** | — | MOF monthly 5/29; largest round since 2022 |
| Jun 29 – Jul 29 window | **¥0** | — | MOF monthly 7/31 — 7/2 no-strike HARD-CONFIRMED |
| **Jul 30** | **~¥8.45T ($52.8B) — ESTIMATE, not MOF-official** (Bloomberg 7/31 off the BOJ Fri projection gap; ~1.5× the biggest prior single-day; Reuters source-confirmed the op itself) | 163.49 → **157.92** low → 159.46 NY settle; **day+1 close 157.3950 BELOW the op-day low** | **Gains EXTENDED day+1 — first of cycle; the n=2 reclaim-then-erode pattern is BROKEN.** SAM's own detector now grades it **INTERVENTION-GRADE (5.74y)**. Confound: 7/31 hawkish hold + Sep telegraph |
| **Jul 31 (16:00-17:00 ET)** | — | 159.18 → **157.15** low → 157.40 close | 🟠 **CANDIDATE op #2 — UNRESOLVED.** Yen-specific across all majors, dollar crosses flat; thin-liquidity weekly close, NY session. Shape (35-min grind, not ballistic) is the weak leg. Discriminators: BOJ c/a T+2 ~8/5 · MOF monthly ~8/31 |

**Actionable trigger (unchanged):** a **disorderly ≥1.5–2%/day** move (or ~2–3 yen in 1–2 sessions). S1-A: silence ≠ safe; the next op arrives unsignalled, so catch the follow-through, not the gap. Method → `MOF_INTERVENTION_PLAYBOOK.md` S1/S1-A.

### 🔧 PRE-REGISTERED BANDS — BOJ current-account pull (written 2026-08-03 ~11:40 ET, **BEFORE** opening either file)

*Closes `MSG-PROME-20260803-001#SAM-02`. Bands written before the pull so tomorrow is **mechanical, not a rediscovery** — and so the read cannot be fitted to the number.*

**File:** `boj.or.jp/en/statistics/boj/fm/juq/d_release/jd/2026/jd20260803.xlsx` (7/30 op, T+2 = Mon 8/3) · `…/jd20260804.xlsx` (7/31, T+2 = Tue 8/4).
**Row:** **"Treasury funds and others"** (財政等要因) — there is **no FX-intervention line item**; a yen-buying op settles here as a **drain** (negative). Per the 7/11 NOT-BUILD scoping this is a manual read: the signal is the **gap vs private money-broker (Tanshi) forecasts**, which SAM cannot automate.
**Reference figures to test:** BOJ Friday projection ≈ **−¥8.2T** fiscal-factors decline against broker forecasts of an **increase** → implied op ≈ **¥8.45T** (Bloomberg 7/31).

| Band ("Treasury funds and others", Aug-3 settlement) | Verdict |
|---|---|
| Decline **≥¥7.0T** | **CORROBORATES** an op of roughly the reported scale (~15% slack for projection→actual revision + fiscal noise) |
| Decline **¥2.0T – ¥7.0T** | **AMBIGUOUS** — an op occurred but materially smaller than reported, or ordinary fiscal flows were conflated. Decompose; **do not restate ¥8.45T** |
| Decline **<¥2.0T**, or a net **increase** | **REFUTES the SIZE** — the ¥8.45T estimate fails on its own instrument. *(Occurrence is separately Reuters-source-confirmed; refuting size ≠ refuting the op)* |

⚠️ **The ¥2.0T noise floor is a JUDGMENT, not a measurement** — the playbook calls this line "large, noisy" (tax receipts, JGB settlements, pensions) but SAM has never measured its distribution. **Pre-registered method step: compute the trailing ~60-session distribution of this row from the `jd` series first, and re-state the floor empirically before grading.** Base-rate the instrument before reading its event table.

⚠️ **NOT AN INDEPENDENT WITNESS — do not launder this into "independently confirmed."** Bloomberg's ¥8.45T was **itself derived from this same BOJ projection**. Pulling the file is own-primary **verification of Bloomberg's arithmetic** (real value: replaces a relayed wire number with one SAM read itself) — it is **not** a second, independent confirmation of the operation. The genuinely independent confirm remains **MOF monthly ~Aug-31**.

🔴 **SCOPE CORRECTION — this instrument is sovereign-blind (registered 2026-08-03).** It reads **Japanese** fiscal factors. The **7/31 op was the US TREASURY** (NY Fed selling euros on Treasury's own account), which does **not** appear as a Japanese fiscal factor. Therefore:
- `jd20260803.xlsx` tests the **MOF** 7/30 op — valid as originally registered.
- `jd20260804.xlsx` **cannot refute the 7/31 op.** A null there means only that **MOF did not *also* fire on 7/31** — still genuinely open, since "coordinated" may mean both. **A null must NOT be graded "candidate #2 DENIED"**; that would be a false negative on an intervention both governments have confirmed.
- **A LARGE drain on the 8/4 file is the live upside branch:** it would evidence a **second MOF op of the round**, firing the §5C override on the narrow MOF reading too (it is already adjudicated fired on the letter via the US op).

#### 🔴 GRADED SAME SESSION (2026-08-03 ~12:20 ET) — **the upside branch FIRED.** Bands above were committed at `aa3ad1980` *before* any file was opened.

**🔧 REGISTERED URL WAS THE WRONG SERIES — corrected.** The playbook named `jd` (same-day / provisional / final, path `…/d_release/jd/2026/`). The **forward projection** — the file the Tanshi-gap method actually needs, and the one Bloomberg read — is a **separate `jp` series** at `…/d_release/jp/jp<YYYYMMDD>.xlsx` (**no year subdirectory**), published **~18:00 JST for the NEXT business day**. ⚠️ **The `jp` endpoint retains only the current projection**: `jp20260803.xlsx` now returns **HTTP 200 with an HTML body** (not a 404) — a clean 200 that is not the resource ([[finding_partitioned_source_returns_stale_window_at_200]]). **Consequence: the Aug-3 file carrying the ~¥8.2T figure has already rotated off and was NOT verifiable today** — the original 7/30 target is *unverified*, not refuted.

| Item | Reading |
|---|---|
| `jp20260804.xlsx` — "for August 4 (Tue)", **Projections** col | **財政等要因 / Treasury funds and others = −114,200 億円 = −¥11.42T** |
| Aug-4 = **T+2 from Fri 7/31** | the 7/31-session settlement |
| Units / precision | 億円 (¥100mn); BOJ note: *"rounded off to 10 billion yen"* |
| Provisional / Final cols | **BLANK** — Aug-4 JST has not occurred. This is a **projection only** |

**Base rate, measured as pre-registered (n=31 sessions, May–Jun, own `jd` pull):** rest-of-month |median| **0.72T**; **sample max drain −7.94T** (May 7, no known op); **early-month peer group (day ≤6): median −3.32T, worst −6.21T**; sessions ≤−7.0T = **1/31**; ≤−2.0T = **8/31 (26%)**.

**→ MY OWN BANDS WERE MIS-CALIBRATED, and the base-rate step caught it.** The ¥2.0T "noise floor" is meaningless — **26% of ordinary sessions clear it**. The ≥¥7.0T CORROBORATE bar would have **false-positived on May 7**. Re-stated empirically: **the honest comparison is not "10× a normal day" (that overstates it by anchoring on 7/31's −1.17T) but ~1.44× the largest ordinary fiscal day ever observed, and ~1.84× the worst early-month day.** Aug-4 is itself an early-month date, so part of −11.42T is ordinary seasonal flow.

**VERDICT: −¥11.42T is genuinely anomalous — larger than every session in the visible sample by 44% — and is strong evidence that MOF ALSO intervened around the 7/31 session, i.e. a genuinely two-sovereign operation.** That is the pre-registered **second-MOF-op-of-the-round** branch, and it fires the §5C override on the narrow MOF reading as well.

⚠️ **Three limits, held deliberately:** (1) **no Tanshi broker forecast** — the actual signal is the *gap*, and the BOJ projection alone cannot separate a large op from a large ordinary fiscal day (exactly the 7/11 NOT-BUILD finding); (2) **projection, not provisional/final** — re-read on the Aug-4 JST update; (3) **op-date attribution is NOT resolvable from this instrument** — a 16:00-17:00 ET Friday execution sits at/after the Tokyo value-date cutoff, so which session's op this settles cannot be pinned here. **Do not restate ¥11.42T as an intervention size** — it is a fiscal-factor line containing an op plus ordinary flows. Independent size confirm remains **MOF monthly ~Aug-31**.

---

## KEY THRESHOLDS

| Level | Significance | Status (8/2; JGB = MOF 7/30 pub) |
|-------|-------------|--------|
| USD/JPY 160 | MOF zone (disorder-not-level; ambush regime) | 🟢 **157.40 — BELOW the zone**, 2d since the 160 touch. Direction reversed hard off the 163.83 [7/23] 40-yr low |
| USD/JPY 155 | Phase 2 carry-unwind onset | 🟡 **1.5% away** — closest since May 6 (155.05). First time this cycle it is a live near-term level rather than a direction-away one |
| USD/JPY 147 | Forced carry unwind | SET |
| USD/JPY 145 | Mechanical insurer selling (Pillar 3) | SET |
| JGB 10Y 2.40% | Stress crossover | 🔴 **BREACHED — 2.801%**, back up from 2.731 [7/21] |
| JGB 30Y 4.0% | v1.6.3: **demand FLOOR with a named bid under it** (Meiji Yasuda) — not a clean disorderly trigger (SAM-26 trap / CH-014) | 🟠 **3.971% — 2.9bp under the floor**, back up from 3.905 [7/21]. Floor confirmed REAL FLOW (7/7 30Y BTC 4.55x; 7/22 40Y BTC 2.83x). **Next test: 8/6 30Y auction** |
| JGB 40Y | — | 🟠 **3.967%** (from 3.852 [7/21]) |
| Brent $90 | Headwind resolved | 🟡 **$90.12 — sitting ON the line** (round-tripped from $100.43). De-escalation headlines 8/1-8/2 = downside risk to the oil leg → Phase-1 yen pressure unwinding |
| Brent $120 | Kharg-scenario Phase 1 shock | 🟢 far off; $115 "Phase-1-reasserts" line no longer proximate |
| **CFTC −153K / 85%** | **convexity-tail flip-condition** | 🔴 **FIRED — −163,412 / 90.8%** (Jul-28 data), through by 10,412. Amplifier +8-10pp |
| **CFTC −108K / 60%** | leg-1 invalidation (SAM-29 cover-tail → frame LOW) | 🟢 **55,412 away** — moved further out of reach |
| CFTC −140K | DE-LOAD line (Will's 7/10 resolver, re-used 8/7) | watch at the 8/7 print |
| DXY | USD-side carry signal | ~sub-101 — Warsh Fed-HIKE regime intact |

---

## WHAT TO WATCH (forward only — full docket → `docket/CALENDAR.md`)

| When | Event | Why it matters |
|---|---|---|
| **Mon 8/3** | TERRY re-mark of TRY-FIRE-005 (Will-approved, PROME-tasked) | Aug-21 tenor **excludes** the Sep 17-18 MPM — must roll past Sep-18. Batch-3 P3-Asia gate also opens |
| ~**Tue 8/4** | BOJ current account `jd20260803.xlsx` | Semi-confirm of the 7/30 op (~¥8.2T fiscal-factor gap vs broker forecasts). `jd20260804.xlsx` (~8/5) does the same for the **7/31 candidate** |
| Tue 8/4 | JGB 10Y auction | Follow-on to the softer Jul-2 10Y; belly-softening watch |
| **Thu 8/6** | **JGB 30Y auction** | First super-long under the reaffirmed FY2027 purchase path; 30Y is 2.9bp under the Meiji floor |
| Thu 8/6 | MOF weekly wk 7/26-8/1 | **3rd-week confirm** of the SELL reversal — 2 SELL weeks already overturned the 7/16 DURABLE read |
| 🔴 **Fri 8/7 3:30 PM ET** | **CFTC (Aug-4 data) — THE print** | First attribution-capable read (saw both the op and the hold) **and** the pre-registered entry resolver. Terms (memo §5B): **≤−153K held = CONFIRM/enter** · **−140K to −153K = NOT-CONFIRMED**, decompose legs (longs-up materially = fresh haven = SAM-31 candidate → escalate HENRY) · **past −140K = DE-LOAD repeats**, revert MEDIUM |
| Fri 8/21 | Japan National July CPI — **first 2025-BASE print** | Measurement discontinuity: re-baseline the subsidy wedge + core-core **before** any YoY comparison |
| ~Mon 8/31 | MOF monthly (Jul-30→Aug-27) | **Hard confirm** for the 7/30 op *and* the 7/31 candidate |
| **Fri 9/18** | **Convexity-tail window END (LOCKED, inclusive)** | Sep 17-18 BOJ MPM decision lands ON the boundary; retire-check runs at Sep-18 close, after the decision prints |

**Watch-for-entry triggers (flat book):** disorderly MOF spike (ambush — catch the follow-through) · ~~CFTC through −153K/85%~~ ✅ **FIRED 8/2, provisional** · risk-off yen-haven re-couple / VIX spike (SAM-31, still decoupled) · Fed-dot walk-back (route 4 — Warsh regime intact, 3 hawkish FOMC dissents 7/29, stays cold) · 30Y 4.5% disorderly (v1.6.7: J-GAAP statutory-impairment TAIL, **mid-cap Fukoku/Asahi bifurcation watch** — precursor only). **Early-entry overrides (memo §5C):** fresh ≥2%/day disorderly move · **confirmed** second op · haven re-couple.

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
1. **Intervention ops *are* the highest-range events in the series** — own repaired data: 7/30 **5.82y**, 7/31 **3.73y**, Apr-30 5.15y, against a 60-session pre-episode max of 1.90y. A pledged, repeatable two-government regime is therefore a **high-realized-range** regime in USD/JPY, directionally aligned with long-FXY. ⚠️ *The intuitive read inverts here:* their **stated objective** is countering disorder, but their **method** — large one-sided buying — **is itself the disorderly move.*
2. **The reaction function is asymmetric in our favour.** They act against yen *weakness*; having declared the yen **"substantially undervalued"** (Bessent 8/2) they have no political appetite to cap yen *strength*. The official put sits **under** the yen, upside uncapped.
3. **Same-side flow.** Official buying and short-covering are *both* yen-buying; at 90.8% of record short the carry crowd is the only structural seller — fuel, not damper.

**Why MEDIUM and not HIGH (the honest counterweight):**
- **The Aug-2024 replay is NOT supported by my own evidence** — on 7/30, the largest yen move since Dec-2023, **VIX FELL 17.3%** and equity vol never transmitted. Cross-asset legs stay decoupled; SAM-31 unfired.
- **A managed, gradual appreciation is a live alternative** that pays a convexity structure nothing — and it **cuts at my own leg (1)**: if the yen keeps strengthening unaided (156.80 on 8/3), officials need not act, so my mechanism *requires official action that may prove unnecessary*.
- Oil de-escalation removes Phase-1 yen pressure, further reducing the need to intervene.

**Base rate (measured, not asserted):** **0/60** sessions ≥2.5y in the 60 before 7/30; **2/250** over the prior year (~0.8%/session) → naive P(≥1 in ~33 remaining sessions) ≈ **23%**. SAM-39's 55% is a **discriminating** mark (~+32pp), not consensus-tracking — and held deliberately below enthusiasm given the documented over-confidence cluster (SAM-08 @90%, SAM-20 @60%, both FAILED).

**→ CONVERSION-RULE IMPACT: NONE. The GATE-SAM-30 resolver map is UNCHANGED** (≤−153K = CONFIRM/enter · −140K..−153K = decompose legs · past −140K = DE-LOAD, revert MEDIUM). The resolver measures whether the **fuel** is intact; this verdict measures whether the **payoff mechanism** survives. Different questions — **a fatten read does not license loosening the fuel test.** Explicitly *not* relaxing the rule on an unpriced mechanism read: that is the exact shape of the SAM-30 → SAM-36 <12h whipsaw.

**Out of scope, unresolved:** **pricing.** A fattened tail at a fat price is not an edge. FXY vol was unreadable 8/3 (degraded snapshot — pre-open, stale underlying, thin wings; KB-183 = read sign not level). **Distribution is SAM's call; price is TERRY's.**

---

## PREDICTIONS

**5 OPEN — SAM-28** (≥1 tail-route fires ≥+3% FXY by Sep-18, 40%) · **SAM-29** (net does NOT cover below −108K by Sep-18, 65%) · **SAM-31** (yen-haven channel re-couples by Sep-18, 35%) · **SAM-33** (no BOJ emergency long-end capping through Dec-31, 72%) · 🆕 **SAM-39** (intervention-character test — ≥1 session ≥2.5y USD/JPY range 8/4→9/18, 55%). **Scoreboard 14 CONFIRMED / 12 FAILED / 1 special.** Canonical → `thesis/PREDICTIONS.tsv` (read the calibration preamble before writing any new row); post-mortems → `PREDICTIONS_ARCHIVE.md`.

⚠️ **The 8/7 resolver is still un-scored — formalize it as SAM-40 before the print** (SAM-39 is now taken by the character test above; never-reuse numbering). The terms are already registered in the memo §5B; writing them as a scored row before Friday converts a disposition into a calibration datum.

---

*Thesis: `thesis/THESIS.md` v1.6.11 · audit trail: `thesis/CHANGELOG.md` · cross-agent surface: `NEXUS_BRIEF.md` · playbook: `MOF_INTERVENTION_PLAYBOOK.md` · decision rules: `STRATEGY.md`.*
