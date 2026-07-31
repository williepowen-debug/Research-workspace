# LABOR — PREDICTIONS SCOREBOARD

**LIVE (created 2026-07-10).** Calibration read of LABOR's resolved forecasts + the pre-write checklist that boot **B4** loads before any new prediction is written. Closes the OTTO/PAT-014 learning loop (raw material existed across PREDICTIONS.tsv + LESSONS.md; this rolls it up).

**How to use:**
- **Before writing a NEW prediction (boot B4):** run the **§C Pre-Write Checklist**.
- **When a prediction RESOLVES (closeout C2):** add its row to §A **scored at its as-made confidence** (see method note), recompute the stats, update §B if a new pattern emerged. Keep `PREDICTIONS.tsv` Status vocab **terminal** (`OPEN`/`RESOLVED`) — `predictions_due.py` exact-matches it.
- **Source of truth:** `PREDICTIONS.tsv` (the ledger) + `LESSONS.md` (the durable patterns). This file *aggregates and indexes* them — it does not restate lesson text (see §C).

---

## §A — CALIBRATION READ (9 resolved LABOR predictions, as of 2026-07-31)

**Method:** Brier score = (confidence − outcome)², outcome = 1 if CONFIRMED, 0 if FALSIFIED. Lower is better. Reference points: **0.00** = perfect · **<0.20** = skilled · **0.234** = base-rate (always predict the 3/8 = 37.5% confirm rate) · **0.25** = no skill (always say "50%") · **1.00** = confidently, exactly wrong.

**Scoring convention — AS-MADE, not final (this matters).** Each prediction is scored at the confidence it was **registered** with at `Date_Made`, NOT its walked-down final value. Grading the walked-down number credits a forecaster for conceding *after* the evidence turned — marking your own homework with the answer key visible, and the exact self-flattery a calibration artifact exists to catch (pre-registration discipline: `[[feedback_dont_bank_unpassed_forecast]]`, `[[finding_delta_vs_own_prior_local_extreme]]`). Two rows are affected: **LAB-02**, registered at 65% and walked 65→50→10 as it failed — scored here at **65%**; and **LAB-17**, registered at 30% and walked 30→35→5 — scored here at **30%** (as-made verified in git across commits `b50c6ada`/`0838327f` 7/2, not read off the current ledger value, per `[[finding_loadbearing_number_must_be_reproducible]]`). The walk-downs are a *separate positive signal* (update discipline) noted below, not folded into the Brier. Scope: 9 LABOR-owned predictions resolved by LABOR (LAB-04 excluded — REHOMED to CORAL). Sorted worst-calibration-first.

| ID | Prediction | Conf (as-made) | Outcome | Brier | Calibration verdict |
|---|---|---|---|---|---|
| LAB-01 | Temp Help YoY stays <−6% | **85%** | FALSIFIED | **0.72** | ❌ **catastrophic overconfidence** — 85% on a false outcome. Measure-spec failure (company proxy vs BLS CES industry series), not judgment → **L-01** |
| LAB-02 | U-3 reaches 4.7%+ | **65%** | FALSIFIED | **0.42** | ❌ **overconfident threshold miss** — U-3 fell to 4.2% on supply-shrink (→ L-06). Walked 65→10 as it failed (good *updating*; scored as-made). Was mis-credited at 0.01 in the first draft. |
| LAB-05 | KFRC earnings miss | 55% | FALSIFIED | 0.30 | ⚠️ mild overconfidence on a coin-flip call (large-cap staffing bottomed) |
| LAB-14 | NFP April <100K | 45% | FALSIFIED | 0.20 | ✅ correctly hedged sub-50% (printed +115K) |
| LAB-09 | Shadow payroll gap closes | 60% | CONFIRMED | 0.16 | ✅ good — **mechanism** call |
| LAB-15 | NFP May <100K | 40% | FALSIFIED | 0.16 | ✅ correctly hedged sub-50% (printed +172K) |
| LAB-07 | DOGE separations >400K | 65% | CONFIRMED | 0.12 | ✅ good — **mechanism** call |
| LAB-16 | JOLTS hire-rate freeze persists | 65% | CONFIRMED | 0.12 | ✅ good — **mechanism** call |
| LAB-17 | WARN-cohort claims test: 4-wk MA ≥235K by Aug 6 | **30%** | FALSIFIED | **0.09** | ✅ **best-calibrated row in the book** — first *threshold* call correctly hedged sub-50% **at registration**. The §C gates worked as designed: the cohort-vs-base sizing defect was flagged 7/6 ("small vs 215K national base, so national 4-wk MA→235K still unlikely; mechanism up, threshold nudged only 30→35") and capped the confidence *before* the evidence turned → **L-08** |

### Stats

| Metric | Value | Note |
|---|---|---|
| N resolved | 9 | 3 CONFIRMED / 6 FALSIFIED (base rate 33.3%) |
| **Mean Brier (as-made)** | **0.256** ↓ from 0.277 | ⚠️ **still loses to both** coin-flip (0.25) and base-rate (0.222). Improving, but the raw book *still* does not clear a naive benchmark — one well-hedged row does not fix two overconfident ones. |
| Mean Brier ex-LAB-01 | 0.198 | beats the benchmarks — but leading with this would be dropping our own worst miss to feel better (the bias this artifact exists to catch). Reported, not headlined. |
| Directional lean correct | **6/9 (66.7%)** | did the >50%/<50% lean match the outcome? The 3 misses (LAB-01 85%, LAB-02 65%, LAB-05 55%) are still **all >50% threshold/level calls** |
| Genuine as-made sub-50% hedges | **3/3** | LAB-14 (45%) + LAB-15 (40%) + **LAB-17 (30%)** — all three correctly leaned against. (LAB-02 is NOT here — as-made it was a 65% call, not a hedge.) |
| High-confidence bucket (≥60%) | 3 C / 2 F | 5 preds; **both** misses (LAB-01, LAB-02) are level/threshold calls |
| Update-discipline (separate diagnostic) | LAB-02 walked 65→50→10; LAB-17 walked 30→35→5 | both conceded fast as evidence turned (LAB-02 pre-marked effective-miss Jun 16; LAB-17 cut 35→5 on the 7/23 counter-print, then resolved ❌ on 7/31 rather than running out the formal Aug-6 clock on a path needing a +149K weekly jump). Good *process*; scored as-made per convention, so it earns a note here, not Brier credit. |

### Two findings that drive this scoreboard

1. **The single biggest error wasn't judgment — it was measure specification.** LAB-01 (85% → false) contributes 0.72 of 2.22 total Brier mass (33%). It failed because the prediction was denominated in a company proxy (KELYA/staffing-firm revenue) while the canonical series (BLS CES Temp Help) was *expanding*. Codified as **L-01**. Takeaway for §C: **police the measure before the confidence** — a defeatable measure, not bad judgment, is the calibration killer.

2. **LABOR reads mechanisms well and over-commits to thresholds.** All 3 CONFIRMED were *mechanism* calls (DOGE cuts underway, shadow gap closing, JOLTS freeze persisting). All 6 FALSIFIED were *specific threshold/level* calls (temp <−6%, U-3 4.7%, NFP <100K ×2, KFRC miss, claims MA ≥235K) — and **both** high-confidence misses (LAB-01 85%, LAB-02 65%) are in that threshold set. Genuine sub-50% hedges on level calls went 3/3. → The **threshold-vs-mechanism** pattern (`[[finding_threshold_vs_mechanism]]`) in LABOR's own record: **hold a mechanism at high conviction; cap confidence on any specific-level threshold, especially one denominated in a defeatable gauge (L-06 denominator, L-01 proxy).** This is the spine the §C checklist operationalizes.

3. **🆕 (2026-07-31) The checklist has now demonstrably worked once — on LAB-17, and *before* the evidence turned.** This is the first entry in the record where a *threshold* call was capped sub-50% **at registration** for the right stated reason. The 7/6 ledger note is the receipt: *"CA/WA-concentrated + tech severance runways = small vs 215K national base, so national 4-wk MA→235K still unlikely; **mechanism up, threshold nudged only 30→35**."* The mechanism (WARN→claims, r=0.78) was upgraded on hard filings while the threshold was explicitly *not* — exactly the split finding #2 prescribes. Result: Brier 0.09, the book's best row. **The instructive part is what it does NOT license.** LAB-17 still resolved ❌, and it failed on a defect that was *identifiable at registration* — the cohort (~6,181 across three weeks) was ~3% of one week's claims and could never move a 4-wk MA by 28K. So the right lesson is not "the gates are sufficient" but: **capping confidence is the consolation prize for a threshold you should not have denominated in the aggregate series in the first place.** The gates priced the miss correctly; they did not prevent it. → **L-08** (a WARN cohort needs ≥~10% of the weekly claims base, ~20K+ in one week, to be visible nationally; below that it is a *state-level* test) is the fix that would have. **Installed as §C gate #4 on 2026-07-31** — it was *not* a gate when this paragraph was first written that morning, and saying otherwise was the error: §D step 4 requires writing the lesson **and** adding the gate, and only the first half had been done since 7/24. Cross-ref `[[finding_threshold_spec_fails_before_world]]`.

**Honest one-line verdict:** modest skill at best — the raw as-made book (0.256) still doesn't beat a coin flip; it is carried by three mechanism calls and dragged by two overconfident threshold misses. The book's edge is *directional mechanism reads*, and its leak is *high-confidence level calls on defeatable measures.* **Trend note (7/31): the leak is narrowing at the confidence layer — sub-50% hedges are 3/3 and the newest threshold miss cost 0.09 instead of 0.42 — but LAB-17 also showed the deeper failure is upstream of confidence, in how the threshold is *specified*. Pricing a bad test well is progress; not writing it is the target.**

---

## §B — WHAT WORKED / WHAT DIDN'T

**The edge — hold these:**
- **Mechanism reads at conviction (3/3 confirmed).** Every CONFIRMED call was a structural *mechanism-in-motion* read: DOGE separations underway (LAB-07), shadow-payroll gap closing (LAB-09), JOLTS hire-rate freeze persisting (LAB-16). When LABOR identifies a mechanism already in motion and predicts its continuation, it is reliably right. This is the book's genuine skill.
- **Disciplined hedging on level calls (2/2).** The genuine sub-50% forecasts — NFP Apr <100K at 45% (LAB-14), NFP May <100K at 40% (LAB-15) — both correctly leaned against a threshold that didn't breach. LABOR prices "this specific level probably won't happen" well. (Stated plainly: 2 for 2 — not the inflated "3/3" of the first draft, which mis-counted the walked-down LAB-02 as a hedge.)
- **Fast concession (update discipline).** LAB-02 was walked 65→50→10 as the evidence turned, pre-marked an effective-miss before formal resolution. It scores as a miss (as-made), but the *process* — updating hard toward the truth instead of defending a stale call — is exactly right and worth keeping. (`[[finding_delta_vs_own_prior_local_extreme]]`)

**The leak — police these:**
- **High-confidence threshold/level calls on defeatable measures.** Both high-conviction misses live here: LAB-01 (85%, temp <−6% on a **company proxy** while the BLS industry series expanded → L-01) and LAB-02 (65%, U-3 4.7% on a gauge whose **denominator** moved faster than its numerator → L-06). A "level breaches X" call is only as good as the measure carrying X — and LABOR's two most-defeated measures were a company proxy and a ratio denominator.
- **Coin-flip company-specific calls.** LAB-05 (55%, KFRC earnings miss) — a single-firm earnings call at barely-above-even confidence, missed. Company-tier reads lag and don't equal the industry (L-01 again).

**Net signature:** *over-committing confidence to a specific level denominated in a measure that can be defeated without the underlying mechanism moving LABOR's way.* Every §C gate exists to interrupt that signature before a prediction is registered.

---

## §C — PRE-WRITE CHECKLIST

**Run at boot B4, before registering any new prediction. 11 gates.** Each gate is a yes/no you must clear (or explicitly justify in the prediction's Notes). This is the *index + gate* — pointers go to the full pattern; nothing is restated here (one source of truth).

**Source set (stated explicitly):** LESSONS **L-01, L-02, L-03, L-05, L-06, L-07, L-08** (the prediction-relevant LABOR lessons; L-04 is ledger-hygiene, not a write gate) **PLUS two FLEET auto-memories that are NOT LABOR lessons** — `[[finding_threshold_vs_mechanism]]` and `[[finding_anchor_prediction_to_surprise_not_priced]]` — **PLUS two calibration meta-gates** derived from §A. "References LESSONS" alone would miss the two fleet memories, hence this explicit set.

*Ordered by how often each bit LABOR (measure-spec first — it's the calibration killer):*

1. **MEASURE — canonical, not proxy.** Denominated in the canonical *industry* series (BLS CES / JOLTS / official release), NOT a company proxy (staffing-firm revenue, single-firm earnings)? — killed LAB-01 & LAB-05. (→ **L-01**, `[[feedback_prediction_canonical_measure]]`)
2. **MEASURE — defeatable-gauge check.** If the threshold is a *ratio* (U-3, penetration rate): can its denominator defeat it without the mechanism moving? U-3 graded JOINTLY with LFPR — a participation-driven move = NO-SIGNAL. — killed LAB-02. (→ **L-06**)
3. **THRESHOLD vs MECHANISM — which am I predicting?** A *mechanism-in-motion* call earns conviction; a *specific-level* call does not (record: 3/3 on mechanisms, 0/3 on high-conf thresholds). If it's a level call, cap confidence AND state the defeat condition. (→ `[[finding_threshold_vs_mechanism]]`)
4. **SIZING — cohort-to-base ratio (compute it, write it down).** If the prediction is driven by a *cohort* (WARN filings, a named layoff wave, a sector event) but the threshold is denominated on an **aggregate series**: what fraction of the aggregate's per-period base is that cohort? **Detectability floor: ≥~10% of the weekly claims base (~20K+ separations landing in ONE week).** Below that floor the cohort cannot move the aggregate *regardless of how well the mechanism works* — **register the test against state-level data instead, or do not register a threshold at all.** Killed LAB-17: cohort ~6,181 spread across three weeks vs a ~200K weekly base = ~3% of a single week, against a threshold needing **+28K on a 4-wk MA**. **Write the computed ratio into the prediction's Notes at registration** — this gate is only real if the arithmetic is on the record *before* the print. (→ **L-08**, `[[finding_threshold_spec_fails_before_world]]`)
5. **>80% STOP.** Confidence above 80%? STOP — LABOR's only 85% call (LAB-01) was its single worst miss. 80%+ is earned ONLY by an intact mechanism on a non-defeatable measure. (→ §A)
6. **DATA VINTAGE — revised series.** If NFP/revisable: scoring on the REVISED series, and are Kill/exit rules evaluated on revised (not first-print) data? (→ **L-02**)
7. **BASE-EFFECT — gov/DOGE.** If gov/DOGE/federal: using level + MoM, not a base-effect-poisoned YoY comp? (→ **L-03**)
8. **CROSS-DOMAIN — sign check.** If the driver is cross-domain (ICE/immigration, oil, climate): which way does it move LABOR's headline metric (claims/U-3)? Same-direction = convergence; opposite/sideways = CONTEXT, don't score as employment-bearish. (→ **L-05**)
9. **ANNOUNCEMENT — TYPE + filing existence.** If layoff-announcement-based: tagged the TYPE (VR-offer ≈ 0 claims / involuntary RIF / closure / contract-churn) and verified the WARN filing exists before attributing a surge? Effective date (not notice date) sets the claims week (WARN 60-day). (→ **L-07**, `docket/WARN_COHORT.tsv`)
10. **ANCHOR — surprise, not priced.** Anchored to the SURPRISE vs consensus, not a level the market has already priced? (→ `[[finding_anchor_prediction_to_surprise_not_priced]]`)
11. **PRE-REGISTRATION — score as-made.** Registering a clean confidence at Date_Made that will be scored AS-MADE (§A convention)? Walking it down later is good *process* but earns no calibration credit — don't plan to concede-and-credit. (→ `[[feedback_dont_bank_unpassed_forecast]]`)

---

## §D — MAINTENANCE + WIRE-IN

**Freshness model:** this is a *derived* artifact — source of truth stays `PREDICTIONS.tsv` (ledger) + `LESSONS.md` (patterns). It refreshes on prediction *events* (resolutions), not a data cadence, so it carries **no boot mtime-alert** (unlike KB/CATALYSTS/WARN_COHORT). Its freshness is gated by C2 discipline below.

**Wire-in (where the loop closes — both ends are live in `CLAUDE.md`):**
- **boot B4** → *run §C (pre-write checklist) before registering any new prediction.*
- **closeout C2** → *when a prediction resolves, update §A (score as-made) + recompute.*

**Update procedure (at C2, per resolved prediction):**
1. Add a §A row scored at the **AS-MADE confidence** (registered at `Date_Made` in PREDICTIONS.tsv — NOT any walked-down final value). If the confidence was walked, note the walk as *update-discipline* in the verdict, but Brier uses as-made.
2. Recompute the stats block: mean Brier = mean of (conf − outcome)²; benchmarks = coin-flip **0.25** and base-rate (= running CONFIRMED share); refresh directional-lean and confidence-bucket tallies.
3. If a new success/failure pattern emerges (or an existing one shifts), update §B — state hit-rates plainly, don't inflate.
4. If the resolution produced a NEW durable lesson, write it to `LESSONS.md` (Lxx) and add a §C gate pointing to it — §C stays an index, never a restatement.
5. Keep `PREDICTIONS.tsv` Status vocab **terminal** (`OPEN` / `RESOLVED`) — `predictions_due.py` exact-matches it; no intermediate states.

**Do NOT:** score walked-down confidences (self-flattery — the bias this board exists to catch); drop the worst outlier from the headline number; restate lesson text here (drift). *(All three were caught in this board's own first draft — DAEDALUS adversarial-verify, 2026-07-10.)*

---
*Changelog: created 2026-07-10 (3-step build). §A re-scored to as-made convention after adversarial-verify flagged the walked-down LAB-02 crediting. Next update: LAB-03/06/08/10/11/12/13 as they resolve. (LAB-17 resolved ❌ 2026-07-31 — scored in §A at as-made 30%; its lesson L-08 installed as §C gate #4 the same day.)*
