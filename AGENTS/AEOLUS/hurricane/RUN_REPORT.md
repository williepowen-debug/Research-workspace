# AEOLUS · HURRICANE — RUN REPORT

**run_date: 2026-08-21** *(data date 2026-08-21; NHC TWO 200 PM EDT Fri Aug 21 2026)*
**Gap-closing pass — AEOLUS dark 8 days (8/13 → 8/21), across the climatological ramp to peak (~9/10).**

---

## observations_added

**6 rows → `workbook/SERIES.tsv`** · **17 rows → `workbook/LOG.tsv`** · **3 rows → `workbook/STORMS.tsv`**

SERIES (new `(date, instrument)` pairs only; no overwrites):
`nhc_atlantic_active=0` · `ace=3.09` · `noaa_below_normal_prob=75` (re-verified unchanged) · `csu_named_storms=9` / `csu_hurricanes=4` / `csu_major_hurricanes=1` (re-verified unchanged).
Re-verification rows are labelled **RE-VERIFIED UNCHANGED — NOT a new issuance** in the notes column, so they cannot later be misread as revisions.

---

## threshold_state
*(value + margin only — a worker does not grade)*

| Instrument | Value 8/21 | Margin | State |
|---|---|---|---|
| **🔴 C1 escalation line — "NHC lights a GULF/FL system"** | **NO Gulf/FL system.** Peak basin formation odds **20%**, in two systems: NE Atlantic (Azores→Portugal) and central subtropical Atlantic (ESE of Bermuda) | Neither is Gulf, Caribbean, FL, or even western-basin | **NOT FIRED** |
| **ACE vs normal — Yellow ≥134.8** | **3.09** | **131.7 below Yellow** | **NOT FIRED** |
| ACE — Orange ≥159.4 / Red ≥183.9 + landfall | 3.09 | 156.3 / 180.8 below | **NOT FIRED** |
| **AEO-01 criterion — season-end ACE <110.3** | 3.09 season-to-date | **107.2 units of headroom** | *open, resolves 11/30 — AEOLUS grades* |
| AEO-01 second leg — ≤7 hurricanes | **0 Atlantic hurricanes** | 7 of 7 remaining | *open* |
| Reinsurance ROL / cat-loss tally | **NOT RE-PULLED** — carries 8/13 vintage | — | **stale, labelled** |

---

## changes  *(since the 8/13 read, with numbers)*

**1. 🔴 The Atlantic basin went completely silent for 8 days.** Confirmed by three independent NHC primaries: `CurrentStorms.json` shows **0 Atlantic active** (the 2 active are Central Pacific — `cp012026` Lala HU 80 kt, `cp022026` Two-C TD 30 kt); ATCF `/btk/` holds only `bal01/02/03` with **`bal032026.dat` last modified 2026-08-13 14:57** and **no `bal04`**; ATCF `/dis/` holds only `al01/al02/al03` — **no `al04` discussion exists.** Last Atlantic advisory of any kind: **Cristobal Discussion #5, 2026-08-13 1500Z.**

**2. Formation odds collapsed 80% → 20%.** 8/13: AL92 at 80%/80%. 8/21: highest anything in the basin is **20%/20%**.

**3. AL92 and AL94 never developed** — AGENT.md open question #2 answered. AL92 died exactly where and for the reason NHC forecast (shear + dry air). **Peak-season tell: one more confirming instance.**

**4. Zero ACE accrued in 8 days** — 3.09 → 3.09, recomputed and identical. Over the same 8 days a normal season accrues **~5.7** ACE units.

**5. ACE vs to-date normal WORSENED: 23.3% → 16.3%.** Recomputed to-date normal for **Aug 21 = 18.98** (exclusive convention — the one that reproduces the recorded 8/13 figures) vs **13.25** for Aug 13. Seasonal accrual by Aug 21 = **15.48%** (vs 10.81% by Aug 13). **Reusing the 8/13 figure of ~13.2 would have reported 23.3% instead of 16.3% — flattering by 7 points, in the "less quiet than it is" direction.**

**6. NHC's own 2026 archive: the complete Atlantic named-storm set is Arthur, Bertha, Cristobal — three, all TS. ZERO hurricanes, ZERO majors.** Same index lists **8 E-Pacific storms (incl. Hurricanes Fausto, Genevieve)** and **C-Pacific Hurricane Lala + TS Moke** — the El Niño cross-basin fingerprint readable off a name list.

**7. Both seasonal outlooks RE-VERIFIED UNCHANGED.** NOAA page still carries the **6 Aug 2026** issuance (75/20/5; 7-13 NS, 2-6 H, 0-2 MH). CSU seasonal still 9/4/1 from 8/5. **No revision in either direction during the window.**

---

## proposed_findings
*(candidate KB rows — PROPOSALS ONLY, AEOLUS adjudicates)*

**P1 — 🔴 A live CSU forecast cadence was running through peak season and the folder said it did not exist.**
`SOURCES.md` and DOSSIER open-question #5 both assert *"CSU issues no further 2026 updates — from here the read is basin observation, not outlook revision."* **False.** CSU runs a separate **two-week forecast** on a published schedule: **Aug 5 · AUG 19 · Sep 2 · Sep 16 · Sep 30.** The **Aug 19** issue landed inside the dark window and was missed.
- **CSU 8/19, window Aug 19 – Sep 1: BELOW-NORMAL 70% / near-normal 28% / above-normal 2%.** Terciles for this window: `<7 / 7-22 / >22` ACE.
- Verbatim: *"the base state across the Atlantic is quite TC-unfavorable, given the strong El Niño and associated high levels of vertical wind shear"*; *"the National Hurricane Center is not monitoring areas for TC formation in the next week"*; *"This period historically marks the real ramp-up for Atlantic TC activity."*
- **Source: `https://tropical.colostate.edu/Forecast/2026-0819.pdf`** — proposed `SOURCES.md` addition. **Next issue: 2026-09-02.**

**P2 — the prior CSU two-week window is now gradeable.** CSU 8/5 forecast Aug 5-18 below-normal (**<2 ACE**) at 80%. **Observed Atlantic ACE Aug 5-18 = 0.4425** (Cristobal only; 3 synoptic times at 40/40/35 kt) — inside the tercile. ⚠️ **Terciles differ per window** (Aug 5-18 below = `<2`; Aug 19-Sep 1 below = `<7`) — **do not compare the LABEL across windows.**

**P3 — ⚠️ the Aug-13 base rate does not survive the move to Aug 21.** Like-for-like recompute, share of lowest-to-date seasons finishing **<90% of normal**: bottom-6 **83% → 50%**; bottom-8 75% → 62%; bottom-10 **70% → 70%**. The Aug-21 bottom-6 cohort picks up **three big-finish seasons** (1998 148%, 2019 108%, 1999 144%) the Aug-13 cohort lacked. **Read the slice sensitivity, not the headline** — n=6, and bottom-10 is stable. **But do not carry "5 of 6" forward as though date-independent.**

**P4 — ⚠️ convention sensitivity decides the rank, and the two readings point opposite ways rhetorically.** **Inclusive** (through Aug 21 18Z): to-date normal **20.00**, 2026 = 15.4%, **lowest of all 30 years.** **Exclusive** (through Aug 20 18Z — the convention that reproduces the recorded 8/13 numbers): to-date normal **18.98**, 2026 = 16.3%, **2nd-lowest** — and the one year below it is **1998 at 3.08**, AEOLUS's own standing counter-analogue (finished 147.8% after the 1997-98 El Niño collapsed). **AEOLUS should pick and label the convention.**

**P5 — ⚠️ denominator mismatch with NOAA.** NOAA CPC states 2026 ACE as **"30-90% of the MEDIAN."** AEOLUS's bands and AEO-01 use the 1991-2020 **MEAN**. Recomputed from the same HURDAT2 file: **mean 122.58, median 129.25.** NOAA's band = **38.8 – 116.3 ACE = 31.6 – 94.9% of the mean.** **NOAA's upper bound (116.3) sits ABOVE AEO-01's <110.3 line** — the two "90%" figures are not the same number and must not be read across.

**P6 — CSU publishes an explicit seasonal ACE forecast the folder does not record: `2026 = 50`** vs a 1991-2020 average of 123 (CSU's rounding), plus *"ACE West of 60°W" 25 vs 73*. **50 = 40.8% of the 122.58 normal — CSU's own central forecast sits far below AEO-01's <110.3 criterion.** Proposed new SERIES instrument **`csu_ace_forecast`** — **NOT created; vocabulary requires AEOLUS approval.**

**P7 — the shear mechanism persists in primary prose, but NOT in today's TWO, and the distinction matters.** Present: NHC Cristobal Discussion #5 (8/13) *"strong northerly vertical wind shear and dry mid-level air"*; CSU 8/19 *"strong El Niño and associated high levels of vertical wind shear."* Absent: today's TWO says only *"unfavorable environmental conditions."* **The phrase is gone from the TWO because the product has no tropical subject — the discussion that carried it was the last Atlantic discussion issued. Absence of the phrase is not absence of the mechanism.**

**P8 — NOAA's own base rate, verbatim:** *"All hurricane seasons coincident with strong (≥1.5 °C Niño3.4) El Niño events since 1950 have featured below-normal seasonal activity."* NOAA July ENSO forecast: **90%** strong-or-very-strong El Niño during ASO (RONI ≥1.5 °C), **48%** very strong (RONI ≥2.0 °C). ⚠️ **ENSO indices are `regime/`'s instrument** — quoted here only as they appear inside my own outlook product, **not copied into this folder's series.** Reconcile at `regime/`.

**P9 — peril/loss divergence has changed shape.** On 8/13 the tension was *"active basin, soft market."* On 8/21 the basin is **empty**, so both legs now point the same way. **The 8/13 guard against inferring a hard market from an active basin currently has no active basin to guard against.** *(Loss leg not re-pulled — 8/13 vintage.)*

**P10 — `AGENT.md` is stale against `SOURCES.md` on the load-bearing instrument.** `AGENT.md`'s table still says `ace` has **"NO VERIFIED SOURCE — do not invent a figure"** and its open question #1 still calls finding an ACE source *"the highest-value thing you can return."* `SOURCES.md` closed that gap on **8/13**. **A worker reading the brief in the prescribed order hits the stale prohibition before the fix** — it read as an instruction not to compute the number this run was sent to compute. **Proposed `AGENT.md` correction; AEOLUS owns the file.**

---

## gaps
*(required output — a reported gap beats a worked-around one)*

**G1 — Archived Tropical Weather Outlook text for 8/14–8/18 and 8/20 was NOT retrieved.** `SOURCES.md` has no archived-TWO command. Following the archive link **on the verified TWO page** — `https://www.nhc.noaa.gov/archive/xgtwo/gtwo_archive.php` (175,247 bytes) — returned a **JS-driven page with no server-rendered outlook text**; the only forms present are the site search widgets. **No error message; it simply yields no product text.** `https://www.nhc.noaa.gov/archive/2026/` is a storm-index page, not a TWO archive.
➡️ **Consequence, stated plainly: the Gulf/FL window answer rests on (a) absence of any `bal04` / `al04`, (b) CSU's 8/19 attestation that NHC was monitoring nothing basin-wide, and (c) today's TWO — NOT on the archived outlooks themselves.** A verified TWO-archive command is the highest-value `SOURCES.md` addition available. **No source was substituted to fill this.**

**G2 — Loss leg not pulled** (Gallagher Re / Munich Re / Aon / Artemis / Guy Carpenter). Commercial publishers on their own schedule; nothing new expected between H1 (~Jul-Aug) and full-year (~Jan). **Deliberately labelled stale rather than backfilled with a peril figure.**

**G3 — invest-level history is unrecoverable after the fact.** ATCF purges `bal9x` invest decks once inactive; `/atcf/archive/2026/` contains no Atlantic files. **A disturbance that was lit at high odds mid-window and never developed would leave no trace in any source I hold.** This is a structural blind spot in the window question, independent of G1.

**G4 — `csu_ace_forecast` not recorded.** CSU's ACE 50 is a real published figure but the instrument name is outside AGENT.md's controlled vocabulary. **Logged to `LOG.tsv`, deliberately kept out of `SERIES.tsv`.** Needs AEOLUS approval.

**G5 — CSU's own page carries a self-contradiction, noted so it is not mistaken for a new issuance:** it states *"Additional forecast updates will be released on August 5th"* (already past) while the schedule block lists Nov 2026 verification as the next seasonal item. **The 8/5 seasonal update remains the final seasonal forecast; only the two-week series continues.**

---

## sources run this pass

| Command / URL | Result |
|---|---|
| `https://www.nhc.noaa.gov/CurrentStorms.json` | ✅ 2 active, both Central Pacific → **0 Atlantic** |
| `https://www.nhc.noaa.gov/text/MIATWOAT.shtml` | ✅ 24,252 bytes, TWO 200 PM EDT 8/21 parsed from `<pre>` |
| `https://ftp.nhc.noaa.gov/atcf/btk/` + `bal01/02/032026.dat` | ✅ 3 decks; ACE numerator **3.09** reproduced exactly |
| `https://www.nhc.noaa.gov/data/hurdat/hurdat2-1851-2024-040425.txt` | ✅ 7,034,638 bytes; normal **122.58**, validation **14.40 / 7.20** vs NOAA 14 / 7 |
| `https://tropical.colostate.edu/forecasting.html` | ✅ 160,720 bytes; 9/4/1 unchanged; **ACE 50 found** |
| `https://www.cpc.ncep.noaa.gov/products/outlooks/hurricane.shtml` | ✅ 31,488 bytes; still the 6 Aug issuance, 75/20/5 |
| `https://ftp.nhc.noaa.gov/atcf/dis/` *(followed from the verified `/atcf/` listing)* | ✅ only `al01/02/03`; final Cristobal discussion read |
| `https://www.nhc.noaa.gov/archive/2026/` *(linked from the verified TWO page)* | ✅ complete 2026 Atlantic named-storm set confirmed |
| `https://tropical.colostate.edu/Forecast/2026-0819.pdf` + `2026-0805.pdf` *(linked from the verified CSU page)* | ✅ two-week forecasts — **new instrument, see P1** |
| `https://www.nhc.noaa.gov/archive/xgtwo/gtwo_archive.php` | ❌ **G1** — JS-driven, no outlook text |

*Every URL beyond the four in `SOURCES.md` was reached by following a link on a source `SOURCES.md` already verifies, from the same publisher and the same product family. **No source was substituted, and nothing was reconstructed from memory.** All are proposed as `SOURCES.md` additions for AEOLUS to ratify.*

---

## ⛔ limits observed

Nothing written outside `AGENTS/AEOLUS/hurricane/`. **No channel scored** (DOSSIER carries AEOLUS's 8/13 score of 2 🟡 explicitly labelled as AEOLUS's, not re-graded). **No trigger fired** — thresholds reported as value + margin. **No prediction resolved** — AEO-01 reported as headroom. **No packet written, no agent routed to.** **No git commit.** Appends only; `SERIES.tsv` / `STORMS.tsv` / `LOG.tsv` all backed up before write and field counts verified consistent.
