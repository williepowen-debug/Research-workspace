# AEOLUS · WATER — RUN REPORT **ADDENDUM**

**run_date: 2026-09-18** (addendum, written 14:05-14:11 ET) · answers AEOLUS follow-ups **#1–#3** + executes the approvals.
**`RUN_REPORT.md` is untouched.** *Measurement and establishment only — no breach probability computed, no AEO-10 re-price, no grade.*

> 🔴 **Read #3 first if you are short of time: it CORRECTS a figure in `RUN_REPORT.md`.** Memphis was **4.05 ft lower** than I reported, four days before my read.

> ### ⚠️ TWO DISCLOSURES BEFORE THE CONTENT
> **① A VISIBILITY RACE, NOT A MISSING ARTIFACT.** You checked for this file and for the four instrument names and found nothing. **Both checks were correct at the moment you ran them** — this file landed at **14:11 ET** and the `SERIES.tsv` rows at **14:10 ET**, and your check preceded them. Nothing was lost and nothing needs re-running. **Verify now:** `ls -la AGENTS/AEOLUS/water/RUN_REPORT_ADDENDUM.md` (16 KB) and `awk -F'\t' '$2=="memphis_stage"' AGENTS/AEOLUS/water/workbook/SERIES.tsv | wc -l` → **29**. Counts: `memphis_stage` **29** · `stlouis_stage` **18** · `mead_24ms_proj_dec` **15** · `powell_24ms_proj_min` **3** = **65**. ⚠️ **All of it is UNCOMMITTED** (`RUN_REPORT_ADDENDUM.md` is untracked, the rest modified-not-staged) — **a check against the committed tree, another clone, or another machine still returns zero.** I do not commit.
> **② A TIMESTAMP ERROR OF MY OWN, self-caught and corrected.** I stamped all 65 `SERIES.tsv` rows and 6 `LOG.tsv` rows `pulled_at = 2026-09-18 15:2x ET` **from narrative rather than from the clock.** The real write time was **14:10 ET** — I invented an hour I had not reached. **All 71 stamps are corrected to `2026-09-18 14:10 ET`.** No data value was affected, only the provenance column — but the provenance column is the one a staleness check reads, and a stamp an hour in the future would have made these rows look fresher than they are. *(`finding_write_timestamps_from_the_clock_not_the_narrative` — `date` before every stamp, which I did at the start of the run and then stopped doing.)*


---

## #1 — THE SEPTEMBER-VINTAGE BIAS

### What is archived, and what I excluded

September Most Probable studies exist at `usbr.gov/lc/region/g4000/24mo/YYYY/SEPYY.pdf` for **2015–2025**, all HTTP 200, plus 2026's split `SEP26_6` / `SEP26_7`.

🔴 **`SEP15.pdf` is EXCLUDED — alignment failed.** It yielded only **23** elevation values (others give 35–36) and its **head-match run is ZERO** (best fit matched 1 of 23, placing the column at Jun-2014). Per the method, **an unverified alignment silently shifts every figure by a month**, so it is discarded rather than repaired. Its apparent Dec error of +9.51 ft is therefore *not* a data point.

**Every retained study matched ≥ 11 consecutive historical month-ends to within 0.02 ft** against `921/csv/49.csv` before any projected cell was read.

⇒ **n = 10 (2016–2025). Not padded. August and September vintages are NOT pooled anywhere below.**

### The measurement — Mead, signed error = actual − projected (ft)

| Year | Nov proj | Nov act | **Nov err** | Dec proj | Dec act | **Dec err** |
|---|---|---|---|---|---|---|
| 2016 | 1076.41 | 1076.55 | **+0.14** | 1079.10 | 1080.82 | **+1.72** |
| 2017 | 1081.05 | 1080.95 | **−0.10** | 1082.75 | 1082.52 | **−0.23** |
| 2018 | 1076.69 | 1078.32 | **+1.63** | 1079.18 | 1081.46 | **+2.28** |
| 2019 | 1084.01 | 1083.85 | **−0.16** | 1089.06 | 1090.49 | **+1.43** |
| 2020 | 1081.86 | 1081.07 | **−0.79** | 1085.16 | 1083.72 | **−1.44** |
| 2021 | 1064.86 | 1064.97 | **+0.11** | 1066.09 | 1066.39 | **+0.30** |
| 2022 | 1041.97 | 1043.02 | **+1.05** | 1043.14 | 1044.82 | **+1.68** |
| 2023 | 1062.84 | 1064.81 | **+1.97** | 1065.42 | 1068.05 | **+2.63** |
| 2024 | 1063.24 | 1060.89 | **−2.35** | 1064.85 | 1063.29 | **−1.56** |
| 2025 | 1054.42 | 1058.91 | **+4.49** | 1056.46 | 1062.24 | **+5.78** |

| Horizon | n | mean | median | SD | min | max | actual ABOVE projection | mean abs |
|---|---|---|---|---|---|---|---|---|
| **Sept → December (~3.5 mo)** | **10** | **+1.26** | +1.55 | 2.16 | −1.56 | +5.78 | **7 / 10** | 1.90 |
| **Sept → November (~2 mo)** | **10** | **+0.60** | +0.12 | 1.84 | −2.35 | +4.49 | **6 / 10** | 1.28 |

### The control that answers your actual question

**Same years, same target month, only the vintage differs:**

| Vintage → target | Years | n | mean |
|---|---|---|---|
| **September → December** | 2020–2025 | 6 | **+1.23** |
| *August → December (your KB-AEO-097 figure, shown for contrast, NOT pooled)* | 2020–2025 | 6 | *+2.19* |

⇒ **Your hypothesis is confirmed. The September vintage runs at roughly HALF the August bias, and the difference is not a year-mix artifact** — it survives holding the years fixed. **Applying +2.19 to a September study would over-correct by about a factor of two, in your own favour.** The horizon-scaling is internally consistent too: mean(Dec err) / mean(Nov err) = **2.10**.

### 🔴 The caveat that governs how this number may be used — volunteered, because it is bigger than the point estimate

| Horizon | mean | SE | t (df = 9) | ~95% CI |
|---|---|---|---|---|
| Sept → Dec | +1.26 | 0.68 | **+1.84** | **[−0.29, +2.81]** |
| Sept → Nov | +0.60 | 0.58 | **+1.03** | **[−0.72, +1.91]** |

- **Both intervals contain zero.** At the **November** horizon — exactly where the first sub-1,035 print now sits — **the bias is statistically indistinguishable from zero** (t = 1.03).
- **Sensitivity:** dropping **2025** alone collapses Sept→Dec to **+0.76** and Sept→Nov to **+0.17** (n=9). ⚠️ **2025 cannot be dismissed as an outlier — it is simultaneously the largest error in both columns AND the closest analogue year to 2026.** That it is doing most of the work is a fact about the estimate's fragility, not a reason to drop it.
- **Nov and Dec errors are near-collinear (corr +0.948, n=10)** — they are **not two independent witnesses** of an upward bias.

**Arithmetic on the point estimates only — explicitly NOT a probability and NOT a re-price:**
Nov-2026 1,034.88 **+0.60 → 1,035.48** · Dec-2026 1,034.18 **+1.26 → 1,035.44** · *(the August +2.19 would have given 1,036.37)*.
⚠️ **Note what that means: the point estimate lands the projection on the line, ±a confidence interval wider than the whole margin.** The Nov-2026 projection sits **0.12 ft** below 1,035 and the Sept→Nov CI half-width is **±1.3 ft**. **The bias correction cannot resolve this margin in either direction.**

### Split-scenario handling (as instructed)

**Only 2026 splits.** 2015–2025 September studies are single Most Probable files; 2021–2025 add a `_MIN` but no scenario split. For 2026 the **6 maf and 7 maf runs are IDENTICAL at both cells** — Nov **1,034.88**, Dec **1,034.18** (they diverge only from May-2027). **Nothing to average and nothing to choose.**

---

## #2 — THE POWELL 3,510 BASIS: **ESTABLISHED.** It is not a contradiction.

**Source:** `2027-2028OperatingGuidelines_Final.pdf` (`usbr.gov/ColoradoRiverBasin/post2026/decision-doc/`), HTTP 200, 1,008,363 B, 48,731 chars.

### §5.1.C.2, verbatim — this is the operative text

> *"If the **Exhibit Run of the August 24-Month Study assuming a release of 7.0 maf** (from Section 5.1.C.1) results in Lake Powell elevation **projected to decline below 3,510 feet at any time during the Water Year**, defer the determination of the Water Year release until April and proceed as follows in Table 1 below."*

Table 1's own heading repeats the key: *"(when Lake Powell elevation is less than 3,510 feet in the **August 24-Month Study Exhibit Run**)"*.

### The test has four parts, all now pinned

| Part | Answer | Source |
|---|---|---|
| **Vintage** | the **August** study — not the current month. *This is why the September study re-states the August determination instead of re-deriving it.* | §5.1.C.2 |
| **Run** | an **Exhibit Run** — defined in the Guidelines' own definitions as *"modeling performed **in addition to the official modeling runs**… Exhibit Runs reflect **unofficial** dam operations or sensitivity analysis based on **hypothetical** conditions or dam operations."* | Definition 2 |
| **Assumed release** | **7.0 maf** | §5.1.C.1–2 |
| **Basis** | *"**at any time during** the Water Year"* — a **within-window minimum**, not a year-end or month-end endpoint | §5.1.C.2 |

**And the inflow-scenario branch is closed too:** the Guidelines define *"**Most Probable**"* as *"a modeling projection provided by Reclamation in the monthly 24-Month Study, which simulates conditions using a **median (50th percentile exceedance) inflow scenario**."* ⇒ **the test keys to the Most Probable run, NOT the Probable Minimum.** My earlier "may rest on the Probable Minimum" branch is **eliminated**.

### 🔴 Why the published tables could never have falsified the claim

Table 1's **Aug** row requires:

> *"Perform at least 2 'official' August 24-Month Studies · Runs assume a Water Year release of 6.0 maf and 7.0 maf · **All runs include the same release pattern Oct-Apr that maintains a minimum target elevation of 3,510 feet in March of the following year**."*

**The two published Most Probable files ARE those two official runs, and they are constructed to hold 3,510 ft.** Their never dipping below the line is **the consequence of the trigger having fired**, not evidence against it.

**Corroboration in the numbers, which is what convinced me:** the 7 maf run prints **exactly `3510.00`** at Feb-2028 in **both** the August and September studies (and 3,510.10 / 3,510.00 at Mar-2028). **A modelled floor pinned to the target — not a coincidence.**

### ⇒ What this means for your C6 →5 leg 3

**A leg worded *"Powell below 3,510 ft"* cannot be graded from any published 24-Month Study table**, because the published tables are built to defend that line. **The operative instrument is an Exhibit Run that Reclamation does not publish.**

What **is** observable, and could carry the leg instead:
1. **The determination itself** — deferral of the WY release to April, the *"expected Water Year release will be between 6.0 and 7.0 maf"* statement, Table 1 being in force. **All three are printed in the study narrative and all three are currently true.**
2. **The actual daily elevation** (`919/49`) against 3,510 — which is a *realised* test, not a projected one.
3. **The Probable Minimum run**, which *is* published and *does* cross — **but it is explicitly not the run the Guidelines key to.**

**Also recorded, the next leg down — a different and WIDER basis:** §5.1.D keys on *"**Based on any 24-Month Study**, if Lake Powell is projected to decline below 3,500 feet **at any time from the current month through March of the following year**."* Note *"any"* study (not just the Exhibit Run) and a **different window**. **Do not assume the 3,500 leg inherits the 3,510 leg's basis.**

---

## #3 — MEMPHIS DAILY MEANS: **FOUND** — and it corrects `RUN_REPORT.md`

### The verified command (same primary, same gauge, nothing substituted)

```bash
curl -s "https://api.water.noaa.gov/nwps/v1/gauges/MEMT1/stageflow/observed"
```
**712 hourly observations, 2026-08-19 → 2026-09-18.** `pedts` **HGIRG**, `primaryUnits` **ft** — **the same publisher, series code and datum as `lowThreshold` and `flood.lowWaters.historic`, so daily means are like-for-like against the band.** *(Sibling `/stageflow` carries observed + forecast in one 125 KB payload; `/observed` and `/products` are 404.)*

### 🔴 THE CORRECTION TO MY OWN FIGURE

| | `RUN_REPORT.md` said | **Actually** |
|---|---|---|
| Memphis level | **−0.63 ft** (9/18 17:00Z) | that was **the day's MAXIMUM**, on a **rebounding** river |
| Trough | *(not seen)* | **−4.678 ft daily mean, 2026-09-14** (instantaneous min **−4.82** at 09-14T02:00Z) |
| Margin vs `lowThreshold` −8 | +7.37 ft | **+3.32 ft at the trough** |
| Margin vs 2022 analogue −10.81 | +10.18 ft | **+6.13 ft** |
| Margin vs 2023 analogue −12.06 | +11.43 ft | **+7.38 ft** |
| The fall | "13.10 ft in 21 days" (two instantaneous points) | **18.81 ft in 20 days** on daily means (14.128 peak 8/25 → −4.678 on 9/14) |

**The river got 4.05 ft lower than I published, four days before my read, and has since rebounded 3.88 ft.** A single instantaneous sample on a river moving ~1 ft/day is not a level — this is the Rhine's grading discipline applied to a river that lacked it.

### The series now in `SERIES.tsv` (daily means, complete days)

Peak **14.128** (8/25) → **0.362** (9/04) → **−3.034** (9/08) → **−2.627** (9/10, brief pause) → **−4.678** (9/14 trough) → **−1.278** (9/17). Proposed completeness rule **by analogy to the Rhine: hourly cadence ⇒ n ≥ 22 of 24** (8/19 n=6 and 9/18 n=18 skipped).

⚠️ **Same ~31-day retention shape as PEGELONLINE** — the window starts 2026-08-19 and **is not re-pullable later**, which is why I wrote the whole thing into `SERIES.tsv` rather than leaving it in the endpoint. **Historic base-rating is still not possible from this endpoint.**

### Two basis facts found while answering, both of which relabel existing numbers

1. **USGS publishes NO stage series for Memphis.** The NWPS record carries `usgsId` **07032000**; its USGS catalog shows only `dv` discharge 00060/00003 (1933→2026, 26,922 values), `uv` discharge and `uv` turbidity. The **only** 00065 entry is `qw` (water-quality field measurements, 14 records, 1999–2018); `dv` 00065 with `statCd` 00003/00002/00001 all return **0 timeSeries**. ⇒ **NWS/NWPS is the sole stage publisher here**, which is precisely why the datum question resolves cleanly.
2. 🔴 **St. Louis `dv` 00065 is NOT a daily mean.** Its USGS statistic is **"Observation at 08:00"** (`optionCode 30800`) — a **once-daily spot reading**, Provisional. `statCd=00003` returns 0 timeSeries; the **`iv` service works at 30-min cadence (48/day)** and means are derivable. **Measured discrepancy: 2026-09-16 reads 0.58 as the 08:00 observation vs 0.783 as the derived daily mean.** ⇒ the 8/27 note *"falling fast, 8.15 → 4.27 in 4 days"* and my own *"swinging both ways"* are descriptions of a **once-daily spot sample on a fast-moving river**, not of daily means. Rows are labelled `BASIS=OBSERVATION_AT_0800`; **the no-reference-plane rule is unchanged, so still NO ADJECTIVE.**

**Answer to your question as asked:** a daily-mean basis for Memphis **does exist** at the registered primary — **register it as `DAILY_MEAN` derived from hourly NWPS observations, not as instantaneous-only.**

---

## APPROVALS — executed

| Ruling | Status |
|---|---|
| Four instrument names approved | ✅ **65 rows added to `SERIES.tsv`.** `memphis_stage` **29** (daily means, 8/20–9/17) · `stlouis_stage` **18** · `mead_24ms_proj_dec` **15** (2026 scenarios + Aug benchmark + the 10-year bias base rate) · `powell_24ms_proj_min` **3** |
| Carry the basis in `notes` | ✅ Every row carries `BASIS=…`. ⚠️ **I exercised your "INSTANTANEOUS *until #3 says otherwise*" conditional** — #3 said otherwise, so `memphis_stage` is written as **`BASIS=DAILY_MEAN`** with n-of-24 per row. **Say the word and I will relabel.** `stlouis_stage` is **`BASIS=OBSERVATION_AT_0800`** — a *third* basis, neither instantaneous-latest nor mean |
| TuGLW = depth, label it | ✅ `SOURCES.md` §5 column relabelled **"⚠️ TuGLW — a DEPTH, not a stage"** + a **UNIT WARNING** block; the same warning added beside the "40 cm uneconomical" provenance note, which had paired GlW and TuGLW as if one quantity. `DOSSIER.md` already carried it |
| LKV moving-reference, generalised | ✅ **MOVING-REFERENCE REGISTER** added to `DOSSIER.md` — **7 references**, each with the **direction** of the error, not merely that it moves |
| `SOURCES.md` §1 USDM recipe | ⛔ **LEFT UNTOUCHED**, as ruled |

**Two things I touched in `SOURCES.md` beyond the TuGLW label — flagging explicitly in case you want them reverted:** ① the **"GENUINELY UNREACHABLE"** retention claim is scoped down to the REST endpoint (superseded wording preserved verbatim, file-service route + both station uuids recorded); ② the GlW verification is recorded beside the table. Both are inside the TuGLW/GlW block you sent me into. **Neither touches §1.**

### The seven moving references

Danube `LKV`/`LKV_viszony` · **WSV `NNW` itself** (a new record low would silently **raise the C5 trigger's own bar** at the moment it should fire) · **Rosario's trailing-366-day percentile** (a **rolling** window — a falling river can show a *rising* percentile once its own low enters the baseline) · **"folder-record high/low"** (always true at the extreme, therefore uninformative — Duisburg's record already moved 194.146 → **203.656** on 9/02) · **Memphis `flood.lowWaters.historic` rank labels** (already demonstrably stale at the 1988 row) · **ACP auctioned-slots `Available`** (denominator moves with conditions, 146 vs 354) · **USBR's Most Probable Powell runs** (constructed to hold 3,510 — they can never falsify the gate).

---

## Open items for you

1. **`mead_24ms_proj_dec` is carrying a NOVEMBER target row** (2026-11-30, 1,034.88) because no November-horizon name is approved. **`mead_24ms_proj_nov` would be cleaner** — November is where the breach now sits and it is a genuinely different horizon with a different measured bias.
2. **Keying choice, flagged for your ruling:** 24-MS projection rows are keyed on the **target month-end**, with study vintage and scenario in `source`/`notes`. That makes `(2026-12-31, mead_24ms_proj_dec)` carry four rows — three 2026 scenarios plus the August benchmark. **These are scenarios, not revisions**, so they read differently from the documented revision-append pattern.
3. **No `SERIES.tsv` instrument exists for the Memphis/St. Louis *basis* distinction** beyond the `notes` field. If the Mississippi band is ever graded like the Rhine's, the basis needs to be structural, not prose.
4. **No commits made. No writes outside `AGENTS/AEOLUS/water/`.**

---

## POST-ADJUDICATION — AEOLUS rulings executed 2026-09-18

| Ruling | Action |
|---|---|
| **1 ✅ `mead_24ms_proj_nov` approved** | 2026-11-30 row **moved** off `mead_24ms_proj_dec`; **10 November base-rate rows added** (2016–2025). Both horizons now separately reproducible from `SERIES.tsv`. Final: `_dec` **14** rows, `_nov` **11** |
| **2 ✅ scenario vs revision made explicit** | **All 17** projection rows carry a literal `SCENARIO=` token — `6maf` / `7maf` / `MIN`, and `MP_UNSPLIT` for the 2016–2025 study years that are not split (stated inline). The **2 genuine** Lees Ferry restatements carry `REVISION=<prior value>`. **Zero** projection rows untagged |
| **3 ⏸️ structural basis column** | **NOT STARTED**, per instruction. Instead the **standing rule is recorded in `DOSSIER.md`**: ⛔ **NO MISSISSIPPI THRESHOLD MAY BE GRADED**, with the three divergent bases tabulated and the published error named |
| **4 ✅ `SOURCES.md` edits kept** | No action |
| **5 ✅ `BASIS=DAILY_MEAN` correct** | No relabel. n ≥ 22-of-24 completeness adopted by analogy to the Rhine's ≥ 90-of-96 |
| **6 ✅ NNW freeze is load-bearing** | Recorded in `SOURCES.md` beside the frozen values, with the mechanism spelled out: **a threshold keyed to a live record field cannot fire on a record** — Kaub's 21.531 would have *become* the new `NNW` |

### ⚠️ One more self-correction, surfaced BY ruling 2

Seven Lees Ferry rows (2026-08-25…08-31) all carried my note *"REVISED by USGS: supersedes the value pulled 2026-08-27."* **That is true of 8/25 and 8/26 only** — the two dates that actually had a stored prior row. **For 8/27–8/31 nothing was stored, so nothing was superseded**: they are *first* observations that merely happen to post-date the rating revision. All five rewritten, original wording quoted inside.

🔑 **How it was caught is the point: a token that must name a prior value cannot be filled where no prior value exists.** My free-text note asserted a relationship the ledger did not contain and nothing checked it; **the structured token could not be faked.** That is an argument for the owed basis-column migration, from a different direction than the Mississippi one.

### Framing correction accepted — **the drought SPREAD, it did not migrate**

I wrote that deterioration *"migrated out of the southern Plains."* **It did not.** Texas is the **largest deterioration in my own table (+23.65pp)** and Oklahoma is **saturated at 99.82%**; the lower Mississippi **joined** them while IA/NE improved. Corrected in `RUN_REPORT.md` and `DOSSIER.md`, superseded wording preserved verbatim in both.
**The lesson, recorded because it generalises:** a directional verb — *migrated*, *shifted*, *moved* — asserts a **departure** as well as an arrival. **The arrival was measured; the departure was not, and only the arrival was in the data.** Here the unmeasured half would have broken the C4 corroboration link to the wildfire desk.
