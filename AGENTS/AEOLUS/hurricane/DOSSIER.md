# AEOLUS · HURRICANE — live dossier

**As-of: 2026-08-21.** Basin state, ACE and both seasonal outlooks re-pulled from primaries this date. **C1 score: 2 🟡 as last graded by AEOLUS 8/13 — a worker does not score; nothing below re-grades it.**

> **Last real data refresh: 2026-08-21**  ·  **Dossier written: 2026-08-21**
> *Two-clock header (PAT-044) — `scripts/ledger_staleness.py` reads the first line. **The data date, not the edit date**: a hygiene edit must NOT bump it.*
> **Observations → `hurricane/workbook/SERIES.tsv`** · findings → central `workbook/KB.tsv` · synthesis → `STATUS.md`. **Flow is one-way.**
> **Feeds:** C1
**We are in peak season (mid-Aug → mid-Oct).** *(CSU's own 8/19 words for the current window: "This period historically marks the real ramp-up for Atlantic TC activity.")*

---

## 0. 🔴 THE HEADLINE — EIGHT DAYS OF COMPLETE ATLANTIC SILENCE

**Between 2026-08-13 and 2026-08-21 the Atlantic basin produced NOTHING.** Not a storm, not an advisory, not a best-track write. Three independent NHC primaries agree:

| Primary | Evidence |
|---|---|
| `CurrentStorms.json` | **0 Atlantic active.** The 2 active systems are both **Central Pacific** — `cp012026` Lala (HU 80 kt) and `cp022026` Two-C (TD 30 kt) |
| ATCF `/atcf/btk/` | Only `bal012026`, `bal022026`, `bal032026` exist. **`bal032026.dat` last modified 2026-08-13 14:57** — no Atlantic best-track write in 8 days. **No `bal04`.** Both invest decks (AL92/AL94) purged |
| ATCF `/atcf/dis/` | Only `al01/al02/al03` discussion sets. **No `al04` discussion exists.** Last Atlantic advisory of any kind: **Cristobal Discussion #5, 2026-08-13 1500Z** |

**NHC's own 2026 season archive index lists the complete Atlantic named-storm set: Arthur, Bertha, Cristobal — three, all Tropical Storms. ZERO Atlantic hurricanes. ZERO majors.**

> 🔑 **The cross-basin fingerprint is visible in the storm-name list itself.** The same NHC archive lists **8 E-Pacific storms including Hurricanes Fausto and Genevieve**, and **C-Pacific Hurricane Lala + TS Moke**. Pacific enhanced, Atlantic empty — the El Niño signature, read off a name list rather than an index.

---

## 1. BASIN STATE (NHC TWO, 200 PM EDT Fri Aug 21 2026 — Forecaster Mahoney/Cangialosi)

| System | Odds 48h / 7d | Location | Fires the trigger? |
|---|---|---|---|
| Non-tropical low | **20% / 20%** | several hundred mi **N-NE of the Azores**, moving ESE toward **Portugal / NW Spain** | ❌ NE Atlantic, European-bound; NHC defers to Météo France High Seas |
| Weak low | **10% / 20%** | few hundred mi **ESE of Bermuda** | ❌ central subtropical Atlantic |

**Peak formation odds in the basin: 20%. On 8/13 it was 80%.**

> 🔴 **GULF / FLORIDA: NO — and the negative is unusually strong.** The TWO's own header covers *"the North Atlantic…Caribbean Sea and the Gulf of America"* and **lists nothing in either the Gulf or the Caribbean.** Neither area is Gulf/FL, neither is even in the western basin. And **CSU's 8/19 forecast records that at that date "the National Hurricane Center is not monitoring areas for TC formation in the next week"** — i.e. the Atlantic TWO was **blank basin-wide on 8/19**. Combined with the absence of any AL04, there is **no evidence of a Gulf/FL system at any point in the 8/13–8/21 window**, and positive evidence against one. *(Residual gap: archived TWO text for 8/14–8/18 and 8/20 was not retrievable from a verified command — see RUN_REPORT `gaps`.)*
>
> **Escalation line NOT FIRED.** Reported as state; AEOLUS grades.

### The shear prose — still there, but not in today's TWO

| Product | Date | Prose |
|---|---|---|
| **NHC Cristobal Discussion #5** | 8/13 1500Z | *"entrenched in a hostile environment, with cool SSTs, **strong northerly vertical wind shear** and dry mid-level air"* |
| **CSU two-week forecast** | **8/19** | *"the base state across the Atlantic is quite TC-unfavorable, given the **strong El Niño and associated high levels of vertical wind shear**"* |
| **NHC TWO** | **8/21** | generic *"unfavorable environmental conditions"* — **does not name shear** |

> ⚠️ **The phrase is absent from today's TWO because the product has no subject, not because the mechanism left.** The storm-level discussion that carried it on 8/13 was the *last Atlantic discussion issued*. **Absence of the phrase is not absence of the mechanism** — and the mechanism is stated explicitly, by name, in the 8/19 CSU product that sits inside the same window.

---

## 1b. ACE — recomputed 8/21, method re-validated end-to-end

| | value |
|---|---:|
| **2026 season-to-date ACE** | **3.09** — Arthur 0.405 · Bertha 2.2425 · Cristobal 0.4425 |
| **Change since 8/13** | **0.00 — zero ACE accrued in 8 days** |
| 1991-2020 normal, **full season** | **122.58** (mean) · **129.25** (median) |
| **To-date normal, Aug 21** | **18.98** *(exclusive convention — the one the 8/13 figure used)* · **20.00** *(inclusive)* |
| **2026 vs Aug-21 to-date normal** | **16.3%** *(exclusive)* · 15.4% *(inclusive)* — was **23.3%** on Aug 13 |
| **Seasonal accrual by Aug 21** | **15.48%** of seasonal ACE *(vs 10.81% by Aug 13)* |
| AEO-01 criterion | season-end **< 110.3** ⇒ **margin 107.2 ACE units of headroom remain** |

✅ **Parse re-validated:** the same computation returns **14.40 mean named storms / 7.20 mean hurricanes** for 1991-2020, matching NOAA's published 14 / 7. Full-season normal reproduces at **122.58** (the recorded 122.6) and the numerator reproduces at **3.09** exactly.

⚠️ **DO NOT reuse the Aug-13 to-date normal of ~13.2 on a later date.** It is date-specific. On Aug 21 it is **18.98**. Reusing 13.2 would have reported 2026 at 23.3% of normal when the correct figure is **16.3%** — flattering by 7 points, in the direction of "less quiet than it is."

⚠️ **Convention sensitivity — flagged, not chosen.** Under the **inclusive** convention 2026 is the **lowest of all 30 years** through Aug 21. Under the **exclusive** convention (the one that reproduces the recorded 8/13 figures) 2026 is **2nd-lowest**, and the single year below it is **1998 at 3.08** — AEOLUS's own standing counter-analogue. **The dramatic reading and the folder-consistent reading differ. AEOLUS picks the convention.**

⚠️ **Denominator hazard vs NOAA.** NOAA CPC states 2026 ACE as **30-90% of the MEDIAN**. AEOLUS's bands are % of the **MEAN**. Recomputed from the same file: mean 122.58, **median 129.25**. NOAA's band = **38.8–116.3 ACE = 31.6–94.9% of the mean**. **NOAA's upper bound of 116.3 sits ABOVE AEO-01's <110.3 line.** The two "90%" figures are not the same number.

### ⚠️ The Aug-13 base rate does NOT hold at the same strength on Aug 21

Like-for-like recompute — share of the lowest-to-date seasons that finished **<90% of normal**:

| Slice | at **Aug 13** | at **Aug 21** |
|---|---:|---:|
| bottom-6 | **5/6 = 83%** | **3/6 = 50%** |
| bottom-8 | 6/8 = 75% | 5/8 = 62% |
| bottom-10 | 7/10 = 70% | **7/10 = 70%** |

**Why it moves:** the Aug-21 bottom-6 cohort is **1998 (148%), 2002 (55%), 1992 (62%), 2019 (108%), 1999 (144%), 1993 (31%)** — it picks up **three big-finish seasons** the Aug-13 cohort did not contain. Seasons that are quiet *through late August* include some that then exploded in September.

> ⚠️ **Read the sensitivity, not the headline.** n=6 is small and **bottom-10 is stable at 70% on both dates**, so this is partly a ranked-head artefact. But it is a real directional caution against carrying the "5 of 6" figure forward as though it were date-independent. **AEO-01 is AEOLUS's to grade — this is reported as an observation.**

---

## 2. SEASON OUTLOOKS — both re-verified UNCHANGED, plus a product that was being missed

| Source | 2026 forecast | Date | State on 8/21 |
|---|---|---|---|
| **CSU (Klotzbach)** seasonal | **9 / 4 / 1** (NS/H/MH) · **ACE 50** | 8/5 | **RE-VERIFIED UNCHANGED** |
| **NOAA CPC** | **7-13 / 2-6 / 0-2**, **75%** below-normal | 8/6 | **RE-VERIFIED UNCHANGED** — page still carries the 6 Aug issuance |

**NEW — CSU's seasonal table carries an explicit ACE forecast the folder was not recording: `2026 = 50` vs a 1991-2020 average of 123**, plus *"ACE West of 60°W" 25 vs 73*. **50 is 40.8% of the 122.58 normal — CSU's own central forecast sits far below AEO-01's <110.3 criterion.**

### 🔴 A standing folder assumption is WRONG: CSU has a live peak-season cadence

`SOURCES.md` and **open question #5 below** both said *"CSU issues no further 2026 updates — from here the read is basin observation, not outlook revision."* **False.** CSU runs a separate **two-week forecast** series on a published schedule: **Aug 5 · AUG 19 · Sep 2 · Sep 16 · Sep 30.**

**The Aug 19 issue landed inside the 8-day dark window and was missed.** AEOLUS had a dated forecast cadence running straight through peak season and believed it had none.

| CSU two-week | Window | Terciles (1966-2025) | Forecast |
|---|---|---|---|
| issued **8/5** | Aug 5-18 | <2 / 2-6 / >6 ACE | **below-normal 80%** |
| issued **8/19** | **Aug 19 - Sep 1** | **<7 / 7-22 / >22 ACE** | **BELOW-NORMAL 70% · near 28% · above 2%** |

**The 8/5 window is now gradeable: observed Atlantic ACE for Aug 5-18 = 0.4425** (Cristobal only — 3 synoptic times at 40/40/35 kt), inside the forecast tercile. *Stated as an observation; AEOLUS grades.*

CSU's 8/19 reasoning, verbatim: *"There are currently no active TCs, and the National Hurricane Center is not monitoring areas for TC formation in the next week… The MJO is forecast to be relatively weak but favoring enhanced convection across the tropical Pacific… the base state across the Atlantic is quite TC-unfavorable, given the strong El Niño and associated high levels of vertical wind shear."*

> ⚠️ **Note the tercile widening — Aug 5-18 below-normal was `<2 ACE`; Aug 19-Sep 1 below-normal is `<7 ACE`.** CSU's own climatology confirms the ramp the accrual base rate measures. **A "below-normal" label means a different quantity in each window; do not compare the labels across windows.**

---

## 3. ⚠️ PERIL vs LOSS — NOT RE-PULLED THIS RUN

**The loss leg carries its 8/13 vintage and is now 8 days older.** Commercial publishers run on their own schedule (H1 ~Jul-Aug, full-year ~Jan); nothing new was expected or pulled. **Labelled stale rather than substituted.**

Last read (8/13): July renewal global cat **−16%**, NA **−20/25%**; capital at a record **>$700-790B**; H1 US insured nat-cat **~$36B, ~25-28% BELOW** the 10-yr average.

⇒ **Peril and loss remain different instruments — and the divergence has now inverted in an interesting way.** On 8/13 the tension was *"active basin, soft market."* On 8/21 the basin is **empty**, so peril and loss now point the **same** way: **nothing is happening on either leg.** The 8/13 warning against inferring a hard market from an active basin has, for the moment, no active basin to guard against.

---

## 4. THE ENSO MECHANISM (sign from `../regime/` — cited, not copied)

**El Niño → increased vertical wind shear over the tropical Atlantic → suppressed cyclogenesis.**

Corroboration state as observed **inside my own products** this run:

1. **Seasonal** — CSU held at 9/4/1 with ACE 50; NOAA held at 75% below-normal.
2. **Sub-seasonal** — **NEW LEVEL:** CSU's 8/19 two-week forecast names the mechanism explicitly for the current window.
3. **Storm-level** — NHC's final Cristobal discussion named *strong northerly vertical wind shear and dry mid-level air*.
4. **Outcome-level** — **NEW:** three 2026 Atlantic named storms, **zero hurricanes**, ACE 3.09; the Pacific basins carry three hurricanes over the same season.
5. **NOAA's own base rate, verbatim:** *"All hurricane seasons coincident with strong (≥1.5 °C Niño3.4) El Niño events since 1950 have featured below-normal seasonal activity."* NOAA's July ENSO forecast: **90%** chance of strong-or-very-strong El Niño during ASO (RONI ≥1.5 °C), **48%** very strong (RONI ≥2.0 °C).

⚠️ **ENSO index values are `regime/`'s instrument** (SHARED-INPUT RULE). The RONI/Niño3.4 figures above are quoted **as they appear inside my own outlook products** and are **not** copied into this folder's series. Reconcile at `regime/`.

⚠️ **Standing caveat unchanged (L-14/L-17):** at record amplitude the underpinning composites are least reliable.

---

## 5. 🔑 THE TELL TO WATCH THROUGH PEAK SEASON — one more confirming instance

**Do 80%-probability systems keep shearing apart before 60°W?**

**AL92 — 80%/80% on both 8/12 and 8/13, NHC forecasting it to weaken on shear + dry air — NEVER DEVELOPED.** No `bal04`, no `al04` discussion, invest deck purged. **AL94 (30%/50%) likewise never developed.** AGENT.md open question #2 is answered: the only candidate to become a Gulf/FL system died where NHC said it would, for the reason NHC gave.

**Running tally of the tell: two 80% systems logged (AL92, AL93), both failed to become anything that reached the western basin** — AL93 became TD Cristobal near the Azores and dissipated; AL92 never got a number.

⚠️ **The falsifier, both directions, unchanged:** a single **Gulf/FL major landfall** reverses ROL, the C1 score and the pre-registered RNR entry. **A suppressed season is a probability statement, not a guarantee** — 1992 (Andrew, in a quiet season) is the standing reminder. **Note that 1992 appears in the Aug-21 bottom-6 to-date cohort above**, which is exactly the point.

---

## 6. PREDICTIONS — **not resolved here; worker reports value and margin only**

- **AEO-01** — season-end ACE **< 110.3** AND ≤7 hurricanes, resolves **11/30**.
  **State 8/21: ACE 3.09 → 107.2 units of headroom below the threshold. Hurricanes: 0 → 7 of 7 remaining.** Season-to-date is **16.3% of the Aug-21 to-date normal** (exclusive convention), **2nd-lowest of 30** — or lowest, under the inclusive convention.
  ⚠️ **Two things moved AGAINST the 8/13 write-up and AEOLUS should see both:** (a) the like-for-like **bottom-6 base rate falls from 83% to 50%** between Aug 13 and Aug 21; (b) the single season below 2026 on the folder's own convention is **1998**, the counter-analogue. Neither is a resolution — **AEOLUS grades AEO-01.**
- **AEO-03** — property-cat reinsurance still soft at the **Jan-2027** renewal (ROL ≤+5% YoY), resolves **1/15/27**. **Loss leg not re-pulled this run** — no new evidence either way.

---

## OPEN QUESTIONS / GAPS

1. ✅ **ACE instrument — CLOSED 8/13, RE-VALIDATED 8/21.** Method runs clean end-to-end; both legs reproduce. ⚠️ **`AGENT.md` has not caught up** — its instrument table still says `ace` has "NO VERIFIED SOURCE — do not invent a figure" and its open question #1 still calls finding an ACE source "the highest-value thing you can return." A worker reading the brief in the prescribed order **hits the stale prohibition before the fix.** *(Proposed correction — AEOLUS owns `AGENT.md`.)*
2. ✅ **AL92's track — ANSWERED.** Never developed. See §5.
3. **Peak-season tell (§5)** — two instances logged, both confirming. Track through mid-Oct.
4. **Jan-2027 renewal** — AEO-03's resolution; watch Artemis / Guy Carpenter from December.
5. ❌ **CORRECTED — this entry was wrong.** It said *"CSU issues no further 2026 updates."* **CSU issues two-week forecasts on Aug 5 / Aug 19 / Sep 2 / Sep 16 / Sep 30.** The read from here is **basin observation AND a live 2-week outlook cadence**. **Next issue: 2026-09-02.** *(Proposed `SOURCES.md` addition — AEOLUS owns it.)*
6. **NEW — archived TWO text is not in `SOURCES.md`.** The 8/14-8/18 and 8/20 outlooks could not be retrieved from any verified command; the graphical archive at `/archive/xgtwo/gtwo_archive.php` (linked from the verified TWO page) is JS-driven and did not yield text. The window answer above rests on b-deck/discussion absence plus CSU's 8/19 attestation, not on the archived products themselves. **A verified TWO-archive command would close this.**
7. **NEW — denominator reconciliation.** NOAA quotes ACE vs **median**; AEOLUS's bands use **mean**. Decide which the folder speaks and label it. See §1b.
