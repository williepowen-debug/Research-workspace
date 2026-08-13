# AEOLUS · WATER — worker run report

> ⚠️ **This report covers ONE worker run (Rhine). It is NOT a summary of the folder's day.** `water/` also gained the Colorado EIS shortage matrix, the Panama transit instrument, the Danube LKV references and the Paraná distribution on 2026-08-13 — **all AEOLUS-direct work, not worker runs**, so none appear below. **For the folder's state read `DOSSIER.md`; this file only ever describes the most recent worker run.**

**run_date: 2026-08-13** · **scope: RHINE ONLY** (WSV/PEGELONLINE primary, six verified stations)
**Data timestamp: 2026-08-13T17:45:00+02:00** (latest 15-min observation at every station)

---

## observations_added

**38 rows → `workbook/SERIES.tsv`** · **5 rows → `workbook/LOG.tsv`**

- Daily values for **8/07–8/13** at all six stations, instruments `maxau_stage`, `worms_stage`, `mainz_stage`, `kaub_stage`, `duisburg_ruhrort_stage`, `emmerich_stage`. All `cm`, source `WSV-PEGELONLINE-<STATION>`.
- **4 rows skipped as already present** — `kaub_stage` 8/10, 8/11, 8/12, 8/13. Append-only respected; nothing overwritten or reordered. 7-column schema validated across the whole file before write.
- **8/06 deliberately NOT recorded** — the `P7D` window opens at 18:00, so only 24 of 96 intervals exist. Too partial to be a daily value.
- **Recording convention: daily mean of the 15-min observations, rounded to whole cm.** This is *inferred, not documented* — it reproduces the three pre-existing full-day Kaub rows exactly (8/10 16.51→17, 8/11 14.61→15, 8/12 11.32→11), which is an independent confirmation of the prior worker's method. Partial days are flagged in `notes` with their sample count.

## threshold_state

*Values and margins only. No grading, no trigger call.*

| Station | current (cm) | 7d min–max | **7d trend** (daily mean 8/07→8/12) |
|---|---:|---|---|
| MAXAU | **294** | 292–328 | 318.6 → 298.1 = **−20.5 cm** (−4.09/d) |
| WORMS | **−15** | −15–13 | 8.0 → −10.3 = **−18.4 cm** (−3.67/d) |
| MAINZ | **110** | 109–128 | 124.1 → 110.8 = **−13.4 cm** (−2.67/d) |
| **KAUB** | **13** | 10–28 | 24.2 → 11.3 = **−12.8 cm** (−2.57/d) |
| **DUISBURG-RUHRORT** | **134** | 134–153 | 145.4 → 136.8 = **−8.7 cm** (−1.73/d) |
| EMMERICH | **−11** | −11–0 | −5.7 → −10.4 = **−4.6 cm** (−0.93/d) |

**KAUB vs the two benchmarks:**
- vs **2018 all-time low 25 cm** → **12 cm BELOW** *(and the 25 cm figure is now primary-verified — see findings)*
- vs **40 cm uneconomical navigation** → **27 cm BELOW**
- vs **GlW 77 cm** (WSV's own navigation reference level) → **64 cm below**

**DUISBURG-RUHRORT (the trigger station):** **134 cm**, 7-day trend **−8.7 cm (−1.73 cm/d)**, **currently sitting exactly at its 7-day minimum**. It is **19 cm below its all-time low of 153 cm (2018-10-23)**. Its 7-day *maximum* was 153 — i.e. **it fell through the record inside this window**. *Trigger not interpreted — AEOLUS's call.*

**All six stations return `stateMnwMhw: "low"`** — the API's own classification field.

## changes

**The headline: the answer to "still falling, stabilising, or recovering?" is FALLING — at all six stations, with no station yet stabilised — but the forecast splits the basin in two.**

1. **Measured, last 7 days: every station falling.** The gradient is **steepest upstream and shallowest downstream** — Maxau −4.09 cm/d → Emmerich −0.93 cm/d. The drawdown is still propagating down-basin; the top of the reach is not yet easing.
2. **🔴 FOUR of six gauges are now BELOW their published all-time lows** — not just Kaub, which is how this section previously read:

| Station | current | all-time low (`NNW`) | margin |
|---|---:|---|---:|
| WORMS | −15 | 2 (2018-10-20) | **−17** |
| **KAUB** | 13 | 25 (2018-10-22) | **−12** |
| **DUISBURG-RUHRORT** | 134 | 153 (2018-10-23) | **−19** |
| EMMERICH | −11 | −1 (2022-08-18) | **−10** |
| MAINZ | 110 | 110 (1947-11-02) | **±0** — *7d min of 109 is 1 cm through* |
| MAXAU | 294 | 231 (1885-01-28) | +63 |

3. **MAINZ is sitting exactly on its 1947 record**, and has already dipped 1 cm through it intraday. Not previously tracked.
4. **EMMERICH has gone flat while everything upstream still falls** — −10/−11 cm every day since 8/08, oscillating 1 cm. It is the only station that has stopped moving, and it is doing so *below* its own record.
5. **New instrument found — WSV publishes an official FORECAST** (below). It is the first forward-looking read this folder has had on the Rhine.

| forecast (init 2026-08-13T07:00) | now | min | **8/17** | shape |
|---|---:|---:|---:|---|
| **KAUB** | 13 | **6** (8/14–15) | **11** | falls further, then **partial rebound** |
| **DUISBURG-RUHRORT** | 134 | 129 | **129** | **monotonic decline** |
| **EMMERICH** | −11 | −15 | **−15** | **monotonic decline** |

⇒ **The binding shoal is forecast to trough near 6 cm and recover slightly; the two downstream stations are forecast to keep falling.** A Kaub-only read over the next four days would say "stabilising" and would be wrong about the lower Rhine.

## proposed_findings

*Proposals only — AEOLUS adjudicates and owns any `KB-AEO-NN` row.*

1. **The 25 cm Kaub benchmark is now PRIMARY-VERIFIED, not carried.** Station metadata returns `NNW = 25.0 cm, occurrences: ["2018-10-22"]` and `NW = 25.0 cm` for the 2010-11→2020-10 reference decade. The figure this folder has been carrying is confirmed at the issuing agency and now has an exact date. *(Source: `stations/KAUB.json?includeCharacteristicValues=true`.)*
2. **The Rhine low-water event is basin-wide, not a Kaub shoal effect.** Four of six gauges below all-time lows across **490 km** of reach (Worms km 443 → Emmerich km 852). This is a materially stronger statement than "Kaub broke its record."
3. **WSV publishes an official ~4-day water-level forecast** at `/stations/<S>/WV/measurements.json` (`type=forecast`, with an `initialized` field). Available at **KAUB, DUISBURG-RUHRORT, EMMERICH**; **HTTP 404** at Maxau, Worms, Mainz. ⚠️ **It is NOT listed in the station's `timeseries` array** (which shows only `Q` and `W`) — it is undiscoverable from metadata alone and was found by direct probe. **Recommend registering it in `SOURCES.md` §5.**
4. **A discharge series `Q` exists at all six stations** (m³/s, 15-min) — e.g. **Kaub 492 m³/s at 17:30**. Discharge is the physically conserved quantity and is **datum-independent**, unlike stage. **Recommend registering it**; it would sidestep the datum caveat below entirely. No instrument name exists for it in the vocabulary — AEOLUS's to name.
5. **`GlW` / `TuGLW` are the authority's own navigation-economics reference levels**, and are a better-grounded basis than the carried "40 cm uneconomical" figure, whose provenance is not recorded in `SOURCES.md`. Kaub `GlW = 77 cm`, `TuGLW = 190 cm` (assured fairway depth at GlW). **Recommend AEOLUS decide whether the 40 cm line should be re-keyed onto `GlW`** — flagged, not acted on.
6. **Precision hazard on the newly re-specified C5 trigger.** `SERIES.tsv` stores daily means **rounded to whole cm**, but the trigger tests `daily mean ≤ 25 cm`. **A true mean of 25.4 rounds to 25 and would read as satisfying a threshold it does not meet.** No such case occurs in this window — the nearest is **25.72 on 8/08**, which fails on both bases — but **grade the trigger on unrounded means.** Unrounded values are in `DOSSIER.md` §3 and recomputable from the API.

## gaps

1. **⚠️ DATUM CAVEAT — unresolved, and load-bearing on a 12 cm margin.** Each gauge publishes its own `gaugeZero` with a `validFrom`: **Kaub's is 2019-11-01, i.e. AFTER its 2018-10-22 record**; Maxau's is 2017-07-18 against an **1885** record; Mainz's is 2019-11-01 against a **1947** record. **The API does not state whether historic `NNW` values were re-referenced to the current datum.** Kaub's 25 cm matches the independently carried/reported 2018 value, so it is at least self-consistent — but **cross-era margins of a few cm should not be treated as exact.** This bears directly on the Mainz "exactly at its 1947 record" reading. *Unresolved: I could not find a datum-history endpoint.*
2. **EMMERICH has missing observations** — 91–94 of 96 expected 15-min records on 8/08, 8/09, 8/10, 8/11 (and 23 of 24 on 8/06). Values are tightly banded (−11 to −9), so the effect on daily means is sub-cm, but the gaps are real and not explained by the API. The other five stations returned complete 96/96 days.
3. **🔴 NO VERIFIED FREIGHT SOURCE — nothing reported as measured.** `rhine_freight_eur_t` remains an instrument with no primary behind it. The **~€150/t vs ~€20 normal**, the **~16% of normal loadings (~800 t vs 5,100 t)**, and the **Kiel Institute German Q3 GDP −0.1/−0.2%** figures carried in the dossier are **unverified trade-press relays (PJK/Bloomberg via gCaptain/Insurance Journal)** — **not re-pullable, not measured, and not entered into `SERIES.tsv`.** I did not search for a substitute. Registering a resolvable freight series remains an open gap.
4. **No forecast at MAXAU, WORMS, MAINZ** — `WV/measurements.json` returns **HTTP 404** at those three. Reported as the API's actual behaviour; no substitute sought.
5. **Not attempted this run (out of the Rhine-only scope):** Colorado system (Powell/Mead/Lees Ferry), USDM drought, snowpack, Mississippi/Ohio, Panama, Yangtze/Danube/Paraná. **No instrument in scope failed to pull** — all six stations returned HTTP 200 with distinct content (md5-verified, since three responses had identical byte counts).
6. **`SOURCES.md` not edited** — it was already modified in the working tree when I started, and the new endpoints in `proposed_findings` (3) and (4) are registrations for AEOLUS to make, not substitutions. Proposed, not written.

---

### ⚠️ One reconciliation flag for AEOLUS

`DOSSIER.md` §3 now contains **two different 7-day trend figures** because AEOLUS wrote a trigger section into the same file while this run was in progress. They are **not in conflict**: my table is **daily mean 8/07 → daily mean 8/12**; the "Full profile, 7-day change" line is **spot 8/06 → spot 8/13**. Hence Maxau reads **−20.5** in one and **−32** in the other. **Both are correct on their own basis; neither is a revision of the other.** I added an explicit basis note between them rather than deleting either. **Recommend picking one basis as canonical** so the number does not drift as it travels.

*No git commands run. No files written outside `AGENTS/AEOLUS/water/`. No channel scored, no trigger fired or graded, no prediction resolved.*
