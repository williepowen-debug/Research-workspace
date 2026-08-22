# AEOLUS · WATER — worker run report

```
run_date:   2026-08-21 (Friday)
window:     closes the 8-day observation gap 2026-08-13 → 2026-08-21
scope:      AGENTS/AEOLUS/water/ only. Nothing outside was read for write or written.
grading:    NONE. No channel scored, no trigger fired, no prediction resolved. Values + margins only.
```

> **Headline: two of this folder's three standing watches resolved inside the dark window.**
> **The Colorado River ROD was SIGNED TODAY, 2026-08-21** — ~6 weeks ahead of Interior's ~10/1 target and 9 days ahead of the ~8/30 earliest-legal estimate this folder was running on.
> **Lake Powell printed through its all-time low on 2026-08-15** and is now 0.72 ft below it.

---

## observations_added

| File | Rows |
|---|---|
| `workbook/SERIES.tsv` | **+113** (138 → 251 lines) |
| `workbook/LOG.tsv` | **+18** (15 → 33 lines) |
| `DOSSIER.md` | rewritten §1 §2 §3 + OPEN QUESTIONS; two-clock header → **`Last real data refresh: 2026-08-21`** (data date, not edit date); the 8/12–8/13 Colorado snapshot given an explicit ⛔ SUPERSEDED banner |

**Integrity checks run:** all 251 SERIES rows have exactly 7 fields; all 33 LOG rows have exactly 6. The only duplicate `(date, instrument)` pairs are **six deliberate 8/13 Rhine revisions** — the 8/13 rows were partial-day (through 17:45 CEST) or spot readings; the full-day means are now available. Each appended row carries `REVISED: supersedes the 8/13 partial-day row` in `notes`, per AGENT.md's revision rule. **Nothing was overwritten.**

**No new instrument names were invented.** Every row uses a name already in the AGENT.md vocabulary or already present in SERIES.tsv. Danube per-station LKV margins beyond the two existing `*_vs_lkv` names are recorded in `LOG.tsv` and `DOSSIER.md` rather than as new SERIES instruments — **AEOLUS's call whether to mint `baja_vs_lkv` / `paks_vs_lkv`.**

---

## threshold_state

**Reported as level + margin. NOT GRADED — AEOLUS adjudicates every line below.**

| Threshold | Value | As-of | Margin | State |
|---|---:|---|---:|---|
| Powell vs all-time low **3,519.92 ft** | **3,519.20** | 8/20 | **−0.72 ft (BELOW)** | first print through **8/15** (3,519.91) |
| **Mead vs Hoover 1,035 ft** *(the BINDING one)* | **1,039.44** | 8/20 | **+4.44 ft** | above; margin narrowed 0.38 ft in 8 days |
| Powell vs min power pool **3,490 ft** | 3,519.20 | 8/20 | **+29.20 ft** | above |
| Kaub vs **25 cm** NNW | **44.728** *(unrounded, n=92 partial)* | 8/21 | **+19.73 cm** | **ABOVE** — first time since 8/08 |
| Duisburg-Ruhrort vs **153 cm** NNW | **151.902** *(unrounded, n=92 partial)* | 8/21 | **−1.10 cm** | still below |
| **C5 trigger: consecutive days BOTH below NNW** | **11** *(2026-08-09 → 08-19)* | — | run **BROKEN 8/20** | **COUNT ONLY — AEOLUS grades vs the 10-day rule** |
| USDM CONUS **D1–D4** | **52.70%** | valid 8/18 | +2.32 pp w/w | 3rd straight week every tier up |
| Panama **oceangoing transits/day** vs Yellow ≤32 | **34.03** *(Jul-26 data)* | adv. 8/10 | **+2.03 above Yellow** | not in a band |
| Colorado guideline milestone | **ROD SIGNED** | **8/21** | — | the milestone this row watched has **occurred** |
| Western snowpack | — | — | — | **correctly empty** (seasonal, Jun–Sep) — not a gap |

### ⚠️ The C5 run count deserves AEOLUS's direct attention

The registered trigger fires when **both** stations sit below their NNW on **10 consecutive days**. **The observed joint-below run was 11 consecutive days (8/09 → 8/19) and then broke on 8/20.** On 8/13 the folder recorded this as "5 of 10." **I am reporting the count, not the verdict** — whether an 11-day run that has since broken satisfies a trigger written in the present tense is a spec question, and spec questions are AEOLUS's.

✅ **The unrounded-grading rule was applied and it was not academic.** 8/08 Kaub's true daily mean is **25.719** — above the 25.0 threshold. **No day in the 16-day window falls in the deceptive 25.0–25.5 band** (where a true mean would round *down* to 25 and falsely read as satisfying `≤25`). All new Rhine rows carry the unrounded mean in `notes`; the `value` column stays rounded per the standing convention.

---

## changes

### 1 · Lees Ferry — deficit is a flat LEVEL, not a deteriorating slope

| Window | 2026 mean | 2018-25 same-window mean | Deficit |
|---|---:|---:|---:|
| Aug 01–12 | 7,861.7 cfs | 13,647.3 | **−42.4%** |
| **Aug 13–20** | **7,922.5 cfs** *(n=8; 8/21 not yet posted)* | **13,540.2** | **−41.5%** |

**Deficit essentially unchanged — 0.9 pp narrower, on a release that rose 60.8 cfs (+0.8%).** ✅ The Aug 01–12 calculation **reproduces the carried −42.4% exactly**, which validates the baseline method before it is applied to the new window. 2026 is the lowest of the nine years in **both** windows, by ~3,500 cfs. Daily range 8/13–20: 7,810–8,000 cfs, no trend.

⚠️ **Driver note (L-16), not extrapolated:** this is the water that refills Mead. Mead's 8/14–8/17 plateau sits on releases running 41.5% below the sample that produced its usual Aug→Sep rise.

### 2 · 🔴 Colorado ROD — SIGNED 2026-08-21

| Element | Content |
|---|---|
| **Signed by** | Interior Secretary **Doug Burgum**, **2026-08-21** |
| **Documents** | *ROD — Decision Framework for Colorado River Guidelines: Coordinated Operations of Lake Powell and Lake Mead (**2027–2036**)* + *Guidelines for Operating Years **2027 and 2028*** |
| **Posted at** | `usbr.gov/ColoradoRiverBasin/post2026/decision-doc/` — page **Last Updated 8/21/26** |
| **Structure** | a **10-year Decision Framework** (operational *range*, through 2036) with **2-year** specific guidelines inside it |
| **2027 Lower Basin reduction** | **1.25 maf** — **AZ 760 kaf · CA 440 kaf · NV 50 kaf** |
| **Powell WY2027** | release **6.0–7.0 maf**; begins Oct 1 between **3,540–3,510 ft** = *Lower Elevation Infrastructure Protection Range* |
| **7-state consensus** | **NOT reached.** Interior proceeded without one and says it will incorporate an agreement if the states reach one. |
| **Alongside** | the **August 2026 24-Month Study** was released with the ROD |

**Corroborated at two primaries** — the DOI press release and the USBR decision-documents page. Trade coverage (Maven's Notebook, Colorado Sun, Desert Review, all 8/21) agrees but was **not** the basis of this finding.

**Also primary-verified: the 7/31 Final EIS NOA.** Federal Register **Vol 91 No 146, p. 48385, FR Doc 2026-15536** (EPA weekly EIS NOA, filed 7-30-26): *"EIS No. 20260089, **Final**, BR, CO, Post-2026 Operational Guidelines and Strategies for Lake Powell and Lake Mead Final Environmental Impact Statement."*

> ⚠️ **The ~8/30 "earliest legal ROD" was an inference, and it was wrong in the direction that mattered.** Unlike the adjacent EIS 20260088 entry (*"Review Period Ends: 08/31/2026"*), **the Colorado entry prints NO review-period end date.** The 30-day waiting period was assumed from standard NEPA practice, not read off the notice. **Actual ROD came 9 days before the assumed floor.**

**No ROD notice appears in the Federal Register as of 2026-08-21** — 5 "Colorado River" documents since 7/1, 2 Reclamation documents since 6/1, none a ROD. **This is an absence report, not a contradiction:** a signed ROD posted to the agency site need not have hit the FR yet.

### 3 · USDM — third straight week every tier up, geography split HARDER

| Category | 8/04 | 8/11 | **8/18** | Move |
|---|---|---|---|---|
| **D1–D4** | 48.54% | 50.38% | **52.70%** | +2.32 pp |
| D0–D4 | 70.95% | 73.62% | **76.21%** | +2.59 pp |
| D2–D4 | 28.57% | 29.50% | **29.87%** | +0.37 pp |
| D3 | 9.51% | 10.27% | **10.60%** | +0.33 pp |
| D4 | 0.95% | 1.04% | **1.35%** | **+30% in a week** |

*CONUS, not Total — Total D1–D4 is 44.34%, an 8.4 pp gap.*

**AEOLUS's live distinction did not just hold — it widened:**

| Deteriorating (southern Plains) | 8/11 → 8/18 | | IMPROVING (corn belt) | 8/11 → 8/18 |
|---|---|---|---|---|
| **OK** D4 | **2.29% → 8.68%** | | **IL** D0 | 31.09% → **5.53%** |
| **OK** D3 | 28.14% → **34.94%** (D0 = 100%) | | **IN** D0 | 3.91% → **0.00%** |
| **TX** D0 | 57.28% → **77.91%** | | **IA** D0 | 36.54% → **30.48%** |
| **AR** D2 | 26.63% → **39.82%** | | **NE** D3 | 18.49% → **12.79%** |
| **KS** D2 | 6.64% → **12.28%** | | CO / AZ | flat to slightly better |

⇒ **The national headline and the crop geography moved in opposite directions this week.**

### 4 · Danube — upper reach recovered, lower reach DEEPENED

**14 of 44 stations below their non-sentinel LKV.** **Longest consecutive run: 11 stations, Kvassay zsilip km1642.2 → Duna Mohács km1446.9 = 195.3 km** *(was 13 consecutive, Vác km1679.5 → Mohács, 233 km)*.

| Station | 8/13 vs LKV | **8/21 vs LKV** |
|---|---:|---:|
| Vác | −56 | **+16** ✅ |
| Budapest | −9 | **+8** ✅ |
| Pfelling (Bavaria) | below | **+30** ✅ |
| Paks | −23 | **−26** |
| Dombori | — | **−40** |
| Baja | −31 | **−55** 🔻 |
| **Mohács** | **−40** | **−66** 🔻 |

⚠️ **A real divergence from the Rhine, which recovered basin-wide.** Two rivers that share the 2018-10-24/26 record week are no longer moving together. Sentinel LKV dates (1799/1884/1894-12-31) excluded per SOURCES.md. ⚠️ **Two further stations carry `12-31` LKV dates not on the documented sentinel list — Bogojevo 1953-12-31 and Novi Sad 1946-12-31.** Both counted as real here, but the shared pattern is suspicious; **flagging for AEOLUS, not deciding.**

### 5 · Paraná — still near the TOP of its range

**Rosario 2.97 m (8/21)**, from 3.02 on 8/13 = **96.2nd percentile** of its rolling 366-day distribution (min 1.08 · P05 1.34 · P10 1.40 · median 2.20 · P75 2.46 · max 3.03). **The trailing-year max of 3.03 was set 2026-08-12 — inside this window.** Santa Fe 3.13 · Corrientes 3.00. **Not firing, not near firing; a high Paraná is GOOD for grain logistics.** Caveat unchanged: one year is a short base — 2021 went far lower.

### 6 · Yangtze — stages falling, Datong diverging

| Station | 8/13 | **8/21 20:00 local** | Δ |
|---|---|---|---|
| Yichang 宜昌 | 44.43 m / 17,800 m³/s | **44.23 m / 16,900** | −0.20 m, −900 |
| Hankou 汉口 (Wuhan) | 20.61 m / 27,600 | **19.95 m / 23,400** | −0.66 m, −4,200 |
| Datong 大通 | 10.06 m / 31,100 | **9.65 m / 32,100** | −0.41 m, **+1,000** |
| Three Gorges 三峡水库 | 157.30 m, outflow 14,900 | **157.65 m, outflow 16,300** | +0.35 m (impounding) |

⚠️ **Datong stage-down / discharge-up is an internal inconsistency** — possibly a rating-curve or reporting-time artefact. **Reported as observed, not reconciled.**

### 7 · 🔴 Panama — the oldest open gap, closed as a SERIES

**Oceangoing transits, daily average.** Every value self-verifies against its own monthly total ÷ days:

| Data month | Advisory | **Transits/day** | Total | Self-check |
|---|---|---:|---:|---|
| Mar 2026 | A-09-2026 | 37.03 | 1,148 | 1148/31 = 37.03 ✓ |
| **Apr 2026** | A-14-2026 | **38.70** | 1,161 | 1161/30 = 38.70 ✓ |
| May 2026 | A-19-2026 | 37.06 | 1,149 | 1149/31 = 37.06 ✓ |
| Jun 2026 | A-23-2026 | **32.50** | 975 | 975/30 = 32.50 ✓ |
| **Jul 2026** *(latest)* | **A-26-2026** | **34.03** | 1,055 | 1055/31 = 34.03 ✓ |

**Latest 34.03/day = 2.03 above the Yellow band (≤32).** 5-month mean **35.86**. July detail: arrivals 35.4 (read transits, not this), transits high 37 / low 25; by class 5.65 / 18.39 / 10.00.

⚠️ **The anchored "normal" of 38.70 is the MAXIMUM of the five months available.** Anchoring a baseline on the window extremum overstates the deficit of every later month. **AEOLUS should decide whether the threshold table re-bases** — I have not touched it.

#### 🔴 A binding restriction now exists — Advisory A-29-2026, 2026-08-20

Primary PDF read (not a news relay). ACP Vice Presidency for Operations, signed Boris Moreno Vásquez.

- **Eff. 8/21/26, booking dates from 9/4/26:** Neopanamax daily slots → **9**, Panamax → **25**, **TOTAL 34**.
- **Eff. 9/1/26, booking dates from 9/15/26:** Panamax → **23**, **TOTAL 32**.
- **Cause given:** May–Aug cumulative watershed rainfall **34% below** historical average; watershed inflows **44% below**; a forecast *potentially severe* **2026-27 El Niño** raising concern for the **2027 Jan–Apr dry season**.
- **Draft steps were POSTPONED, not advanced:** 14.63 m (48.0 ft) moved **8/26 → 9/2**; 14.48 m (47.5 ft) moved **9/3 → 10/1**.

> ⚠️ **DISCRIMINATOR — SLOTS ≠ TRANSITS, and the two numbers collide at 32.**
> A-29's **34** and **32** are **booking slots** — an administrative cap on *reservable* transits. The AEOLUS bands (Yellow ≤32 · Orange ≤27 · Red ≤22) are on **oceangoing transits daily average** — *realised* traffic, which includes unbooked transits. July ran **34.03 realised transits** against **247 of 306** booking slots used. **A slot cap of 32 is NOT a transits reading of 32.** This is the transits-vs-arrivals adjacency trap one level up, and it would produce a false band call if read carelessly.
> ⚠️ **10-day reversal on the record:** the July summary (dated 8/10) reprints ACP's own line that the draft adjustment *"will not affect the number of daily vessel transits."* **A-29 on 8/20 then cut daily slots.**

**AEO-04's spec says it resolves on a binding transit/draft RESTRICTION. One now exists — but it is a SLOT cap, not a transits reading. AEOLUS owns whether leg (a) is satisfied.**

### 8 · Rhine — sharp basin-wide recovery

Daily means, **unrounded** (grading basis):

| Station | NNW | 8/13 | 8/17 (min) | 8/20 | **8/21** *(n=92, partial)* | margin |
|---|---:|---:|---:|---:|---:|---:|
| **Kaub** | 25.0 | 11.917 | **6.417** | 34.812 | **44.728** | **+19.73** |
| **Duisburg-Ruhrort** | 153.0 | 135.271 | **128.760** | 150.344 | **151.902** | **−1.10** |
| Maxau | 231.0 | 296.323 | 305.594 | 336.198 | 334.380 | +103.38 |
| Worms | 2.0 | −13.635 | −8.740 | 17.333 | 14.750 | +12.75 |
| Mainz | 110.0 | 111.115 | 108.646 | 140.521 | 140.380 | +30.38 |
| Emmerich | −1.0 | −10.677 | −25.093 | −10.292 | −0.967 | +0.03 |

**Kaub gained ~38 cm in four days.** Five of six stations are now above their all-time low; only Duisburg-Ruhrort remains below, by 1.10 cm.

**WSV forecast** (init 2026-08-21T07:00, horizon **8/21 → 8/23**, 25 points ≈ 2 days — **the same short horizon AEOLUS measured on 8/13**, confirming the endpoint does not give a 4-day view): Kaub peaks ~47 cm midday 8/21, eases to 41 by 8/22. **Duisburg-Ruhrort rises monotonically 149 → 167 by 8/22 17:00, crossing its NNW 153 during 8/21 evening.** Emmerich 0 → 12.

⚠️ **Emmerich 8/14–8/17 has sparse coverage** (n=56, 2, 1, 75). Those daily means are logged with a `SPARSE n=…: low-confidence mean` note. **8/15 and 8/16 rest on 2 and 1 observations respectively — do not treat them as daily means.**

---

## proposed_findings

**PROPOSALS ONLY. AEOLUS adjudicates; none of these was written to `KB.tsv`, `STATUS.md` or `PREDICTIONS.tsv`.**

1. **The Colorado ROD was signed 2026-08-21 — the C6 policy clock has run out early.** 10-year Decision Framework (2027–2036); 2027 Lower Basin cut 1.25 maf (AZ 760 / CA 440 / NV 50 kaf); Powell WY2027 release 6.0–7.0 maf; **no 7-state consensus.** *Sources: DOI press release 8/21; USBR `/post2026/decision-doc/` (Last Updated 8/21/26).* **Downstream question AEOLUS owns: does the Decision Framework retire the shortage-tier language the C6 threshold row is written against, given the 2007 guidelines expire 12/31/26?**
2. **Lake Powell broke its all-time low on 2026-08-15** and is 0.72 ft below it at 8/20. *Source: USBR 919/49.* **AEO-06 is AEOLUS's to grade.**
3. **The Lees Ferry deficit is a stable level, not a deteriorating slope** — −42.4% → −41.5% across adjacent windows on like-for-like same-calendar-window baselines. **A level that stable is a policy/operations variable, not a hydrological one** — Glen Canyon is releasing to a schedule.
4. **Panama transits are a five-month series now, and April was its maximum.** The 38.70 anchor in the threshold table is the extremum of the available window. **Re-basing candidate: the 5-month mean 35.86.**
5. **A binding Panama restriction exists (A-29-2026) while realised transits sit above the Yellow band.** The restriction is on **slots**, the band is on **transits**. **The spec collision is the finding.**
6. **The Rhine and the Danube have decoupled.** The Rhine recovered basin-wide; the lower Danube (Baja, Mohács) set new depth against 2018 records. **They shared the 2018-10-24/26 record week — the 8/13 "one event, count once" independence note may no longer hold.**
7. **The USDM national print and the crop geography are diverging.** Third straight week all tiers up, with the corn belt *improving*. **Candidate rule: a CONUS D-tier move is not usable as a C2 input without the state cut.**
8. **`SOURCES.md` needs three corrections** — §gaps below. **Worker does not edit `SOURCES.md`.**
9. **Reconciliation owed:** the 8/13 LOG rejected a trade-press triple **AZ .76 / CA .44 / NV .05 maf** as *"describing no alternative that exists."* **The ROD's actual 2027 reduction is AZ 760 / CA 440 / NV 50 kaf — numerically that triple.** The 8/13 reasoning may still be correct about the FEIS *max-shortage matrix* (a different quantity from a single-year cut) while the trade press was reporting the forthcoming 2027–28 guidelines. **Flagged, not adjudicated.**

---

## gaps

### ❌ FAILED — `SOURCES.md` §1 state/county drought recipe is WRONG

SOURCES.md says: *"State/county granularity — same API, swap `aoi`: `aoi=CO` (state postal) or a county FIPS."*

```
$ curl -s -H "Accept: application/json" "https://usdmdataservices.unl.edu/api/USStatistics/GetDroughtSeverityStatisticsByAreaPercent?aoi=OK&startdate=8/11/2026&enddate=8/18/2026&statisticsType=1"
"-area of interest not recognized.\r\n"
```
Also failed: `aoi=40` (state FIPS), `aoi=us_OK` — **same error string.**

**Re-verified within the same API rather than substituting a source (L-15). Two working forms found:**
```bash
# State — note the StateStatistics endpoint and the 2-digit state FIPS (NOT postal)
curl -s -H "Accept: application/json" \
 "https://usdmdataservices.unl.edu/api/StateStatistics/GetDroughtSeverityStatisticsByAreaPercent?aoi=40&startdate=8/11/2026&enddate=8/18/2026&statisticsType=1"
# County — 5-digit county FIPS
curl -s -H "Accept: application/json" \
 "https://usdmdataservices.unl.edu/api/CountyStatistics/GetDroughtSeverityStatisticsByAreaPercent?aoi=40017&startdate=8/11/2026&enddate=8/18/2026&statisticsType=1"
```
⚠️ `StateStatistics` with `aoi=OK` returns **`[]`** — an *empty array*, not an error. **A silent empty result on the wrong parameter form is worse than the error string**: a script would log "no drought in Oklahoma." **The state cut in this report used the FIPS form.**
⚠️ The `Accept: application/json` header is **required**; without it the response is not JSON and a plain `urllib` call dies on a parse error.

### ❌ FAILED — no registered primary for the 24-Month Study

**AGENT.md open question #2** (base-rate USBR's 24-month-study projection error) needs it, and **the August 2026 study was released with the ROD**. **`SOURCES.md` registers no URL for it.** URLs I constructed myself both returned **HTTP 404**:
```
404  https://www.usbr.gov/lc/region/g4000/24mo/24mo.pdf
404  https://www.usbr.gov/lc/region/g4000/riverops/24mo-MTOM-forecast-data.html
```
**I did not go hunting for an alternative** — per the hard limit, a reconstructed URL failing is reported, not worked around. **This is a source-registration gap, the same class as the 8/13 Yangtze/Danube/Paraná blocker, and AEOLUS must register a primary before the next attempt.**

### ⚠️ STALE POINTER — `SOURCES.md` §4 Colorado policy clock went false-negative

`https://www.usbr.gov/ColoradoRiverBasin/` — the URL registered for the highest-value watch in this folder — **was last updated 7/22/26**, still describes the process as in the **Draft** EIS phase with no preferred alternative, and mentions **neither the 7/31 Final EIS nor the 8/21 ROD.** It returns HTTP 200 and reads as complete.

**The live surface is the child page:** `https://www.usbr.gov/ColoradoRiverBasin/post2026/decision-doc/` (Last Updated 8/21/26). **Proposed as a SOURCES.md amendment.**

### ✅ POSSIBLE FIX — the ACP advisories index may no longer need the search workaround

SOURCES.md's known-bad JS-rendered index is `https://pancanal.com/en/advisories-to-shipping/`.
**A different path — `https://pancanal.com/en/maritime-services/advisory-to-shipping/` — returns HTTP 200 and enumerates the COMPLETE current 2026 set A-01-2026 → A-29-2026 with direct PDF URLs**, including advisories published this week. That is how A-26 (July summary) and A-29 (the restriction) were located.

**Proposed, NOT adopted — AEOLUS should verify before amending `SOURCES.md`.** The 8/13 lesson (L-24/KB-067) was that an index *reading* as complete is not evidence that it *is*; that caution applies to this path too until independently checked. The "discover by web search" fallback still works and was used in parallel here.

### ⏸️ NOT PULLED — by design

- **Western snowpack** — seasonal, near-zero Jun–Sep. **Correctly empty per SOURCES.md §2, logged as not-a-gap.**
- **Mississippi / Ohio** — still has a working USGS primary but **no registered instrument name** in the vocabulary. Unchanged from 8/13. ⚠️ **Sep–Nov is the Mississippi window — this needs a name before autumn, not after.**
- **Rhine barge freight rates** — still no verified primary. Unchanged.
- **Austria `ehyd.gv.at` / Serbia `hidmet.gov.rs`** Danube reaches — respond HTTP 200, still unexplored.

### 📋 Data-quality flags carried forward

- **Emmerich 8/15 (n=2) and 8/16 (n=1)** — the "daily mean" rests on 1–2 observations. Logged with a SPARSE note; **do not grade against them.**
- **8/21 is a partial day for all six Rhine stations** (n=92 of 96, through 22:45 CEST). Logged as PARTIAL.
- **Datong stage-down / discharge-up** — internal inconsistency, unreconciled, reported as observed.
- **Two Danube stations carry undocumented `12-31` LKV dates** (Bogojevo 1953-12-31, Novi Sad 1946-12-31) matching the sentinel *pattern* but not on the documented sentinel *list*. Counted as real in the 14; **flagged for AEOLUS.**
- **Kaub datum caveat** (SOURCES.md) unchanged and still load-bearing: gauge-zero `validFrom` for Kaub is 2019-11-01, *after* its 2018-10-22 record. **Cross-era margins of a few cm remain approximate** — which is precisely the size of the Duisburg-Ruhrort margin (−1.10 cm) being reported today.

---

## hard-limit compliance

- ✅ **Wrote only inside `AGENTS/AEOLUS/water/`** — `workbook/SERIES.tsv`, `workbook/LOG.tsv`, `DOSSIER.md`, `RUN_REPORT.md`. Nothing else touched.
- ✅ **No channel scored, no trigger fired, no prediction resolved.** Values and margins only; every threshold line says who grades it.
- ✅ **No routing, no packets written.**
- ✅ **No source substituted.** Two failures reported with their exact error text; the one re-verification (USDM) stayed inside the same API, per L-15.
- ✅ **No percent-full figure cited** — elevation throughout.
- ✅ **No threshold described as "approached."** Powell is reported as *0.72 ft below*; Duisburg-Ruhrort as *1.10 cm below*; Panama as *2.03 above the Yellow band*.
- ✅ **No rate extrapolated without its driver** — the Lees Ferry deficit is stated as the driver alongside Mead's plateau.
- ✅ **No git commit.**
- ✅ **No new instrument name invented.**

---
---

# ADDENDUM — 2026-08-21, follow-up ask from AEOLUS

*Narrow ask, no new research. All figures below come from PDFs already open from the main pass, plus a live re-check of every URL. **Nothing graded.***

## A · The exact URLs

**All six re-checked live at 2026-08-22T01:48Z — every one HTTP 200.**

| Advisory | Data month | URL | Re-check |
|---|---|---|---|
| **A-29-2026** *(the restriction)* | — | `https://pancanal.com/wp-content/uploads/2026/08/ADV-29-2026-Additional-Measures-to-Address-Reduced-Precipitation-in-the-Canal-Watershed.pdf` | **200**, 309,277 B |
| **A-09-2026** | Mar 2026 | `https://pancanal.com/wp-content/uploads/2026/04/ADV-09-2026-Monthly-Canal-Operations-Summary-March-2026.pdf` | **200**, 511,204 B |
| **A-14-2026** | Apr 2026 | `https://pancanal.com/wp-content/uploads/2026/04/ADV-14-2026-Monthly-Canal-Operations-Summary-April-2026-.pdf` | **200**, 425,217 B |
| **A-19-2026** | May 2026 | `https://pancanal.com/wp-content/uploads/2026/06/ADV-19-2026-Monthly-Canal-Operations-Summary-May-2026.pdf` | **200**, 727,963 B |
| **A-23-2026** | Jun 2026 | `https://pancanal.com/wp-content/uploads/2026/07/ADV-23-2026-Monthly-Canal-Operations-Summary-June-2026.pdf` | **200**, 695,992 B |
| **A-26-2026** | Jul 2026 | `https://pancanal.com/wp-content/uploads/2026/08/ADV-26-2026-Monthly-Canal-Operations-Summary-July-2026.pdf` | **200**, 442,643 B |

⚠️ **Slugs are NOT guessable and the upload-month folder does NOT track the data month** — A-14 (April data) sits under `/2026/04/` with a **trailing dash before `.pdf`**; A-19 (May data) sits under `/2026/06/`; A-23 (June data) under `/2026/07/`. My own attempts to construct A-29's and A-28's filenames before I had the list **all returned 404**. **These six strings are the artifact — copy them, never rebuild them.**

**How they were located** (search does not surface A-29, as you found): the enumerating page `https://pancanal.com/en/maritime-services/advisory-to-shipping/` — HTTP 200, lists the complete current set **A-01-2026 → A-29-2026** with direct PDF URLs. **This is the `/en/maritime-services/…` path, NOT the known-bad `/en/advisories-to-shipping/`.** Still proposed-not-adopted pending your verification.

**Retrieval command that worked (verbatim):**
```bash
curl -sL -A "Mozilla/5.0 (research)" "<url from the table above>" -o adv.pdf
python3 -c "from pdfminer.high_level import extract_text; print(' '.join(extract_text('adv.pdf').split()))"
```
⚠️ These PDFs set a **no-text-extraction metadata flag**; pdfminer prints a warning and proceeds. **The warning is not a failure** — do not treat it as one.

---

## B · Follow-up 1 — TONNAGE: **NO. The instrument does not carry it.**

**Checked all five monthly summaries. The §2 Traffic Statistics block contains exactly four measured rows and nothing else:**

> **Arrivals · Oceangoing Transits · Canal Waters Time (hours) · In-Transit Time (hours)** — then Oceangoing Transits split by beam class, then Booking Slots.

**There is no tonnage row, in any month.** Keyword count for `tonnage`: **0 in A-09, A-19, A-23, A-26.**

**The one hit, in A-14, is not in the statistics table.** It sits inside an **appended news article** ("Panama Canal Meets Rising Demand"), and it is a **fiscal-half aggregate, not a monthly figure**:

> *"During the first half of FY2026 (October 2025 through March 2026), the Panama Canal recorded 6,288 transits… Over the same period, **254 million PC/UMS (Panama Canal Universal Measurement System) tons** moved through the waterway, which translates to approximately 5% more than the **243 million tons** recorded in the same period of the prior fiscal year."*

**Unit exactly as printed: `PC/UMS (Panama Canal Universal Measurement System) tons`.** Period: **FY2026 H1 = Oct 2025 – Mar 2026**, i.e. it does not even overlap four of your five months.

### ⇒ Your diagnosis is right and this instrument cannot fix it

**A draft cut reducing tonnage-per-transit while the transit COUNT is held flat is exactly the effect you named — and the Monthly Canal Operations Summary is structurally blind to it.** It measures **counts and times, never mass or volume.** So the blindness is not a gap in my pull; it is a property of the instrument.

⚠️ **Two cautions before anything is built on PC/UMS tons, flagged not resolved:**
1. **It is a measurement-system unit, not cargo weight.** The advisory expands the acronym and defines it no further. Whether PC/UMS responds to a *draft* cut the way cargo tonnage would is a real question, and **I am not the one to answer it.**
2. **A half-year aggregate cannot be differenced into months.** Two published points (254M, 243M) one year apart are not a series.

**I did not go looking for a tonnage source elsewhere** — per the hard limit. **Registering one is a `SOURCES.md` decision that is yours.**

**Adjacent column you already have, offered because it costs nothing:** *Canal Waters Time* (hours) is in every block I pulled — **Mar 21.39 · Apr 32.33 · May 31.20 · Jun 23.80 · Jul 25.38**. It is a congestion/dwell measure, not a mass measure, so it does **not** close the tonnage gap. **Reported as available, not analysed.**

---

## C · Follow-up 2 — GATUN LAKE ELEVATION: **NOT THERE. Saying so plainly.**

**Zero occurrences of `PLD` or `elevation` across all six advisories.** No feet, no metres, no datum, no figure.

**A-29-2026 mentions Gatun Lake exactly once, and only qualitatively** — quoted in full:

> *"Additionally, **based on the current level of Gatun Lake** and the latest weather projections, the ACP will postpone until September 2, 2026, the maximum authorized draft of 14.63 meters (48.0 feet) TFW in the Neopanamax Locks…"*

**It invokes the lake level as the stated decision basis and prints no number.**

You read my §7 correctly: **A-29's quantified hydrology is watershed INPUTS only** — May–Aug cumulative rainfall **34% below** the historical average, watershed inflows **44% below**. **Those are the flows into the reservoir, not the reservoir state.** The lake level is the variable ACP says it is deciding on, and it is the one variable it does not publish here.

**No secondary substituted, none sought.** **A Gatun Lake level instrument remains UNREGISTERED in `SOURCES.md`** — logged as a gap for you, not filled by me.

---

## D · One correction to my own main-pass report, unprompted

**In the main pass I reported April 38.70 as `ACP-ADV-14-2026` but I had CARRIED it from `SOURCES.md` — I did not re-pull that PDF.** It is now a genuine primary read this session, and it **confirms**:

> Daily averages **40.5 arrivals / 38.70 oceangoing transits /** 32.33 h Canal Waters Time / 11.84 h in-transit; transits **high 42, low 31, total 1,161**; by class 6.37 / 22.07 / 10.27.

Matches `SOURCES.md` exactly, including the arrivals-vs-transits adjacency. **All five monthly anchors are now primary-read.** Flagging it because a carried figure presented under a primary source tag is the defect I am supposed to catch, not commit.

---

## E · ⚠️ A concurrent-append collision in `workbook/LOG.tsv` — found and repaired

**Your row `panama_draft_restriction_live` was written without a terminating newline.** My `>>` append therefore began **on the same line**, fusing your row and my first addendum row into a single 11-field line. A second artifact, an empty line, sat just above it.

**Repaired — mechanically, content untouched:** the fused line was split at the exact `…\tAEOLUS` / `2026-08-21\t…` boundary and the empty line dropped. **`LOG.tsv` is now 37 rows, every one exactly 6 fields.**

**Proof no content changed:** stripping all newlines and tabs from the before and after files yields **byte-identical** output — nothing added, removed or altered. Your row's text stands exactly as you wrote it. Pre-repair copy at `/tmp/LOG.precollision.tsv`.

> **I repaired this because my own append created the fusion.** I did not otherwise touch your row. ⚠️ **Worth a durable note: this file is now written by both an orchestrator and a spawned worker in the same session, and a missing trailing newline silently corrupts the next appender's first row.** Both writes looked successful to their authors. **A field-count check catches it; nothing else in the closeout does.**

---

```
addendum_observations_added:  +3 rows to workbook/LOG.tsv (34 -> 37, all 6-field)
files_touched:                workbook/LOG.tsv, RUN_REPORT.md   (both inside AGENTS/AEOLUS/water/)
graded:                       nothing
sources_substituted:          none
urls_that_404'd_on_recheck:   none — all six returned HTTP 200
git:                          no commit
```

---
---

# ⬛ SECOND WORKER RUN, SAME DAY — PANAMA MONTHLY CAPACITY SERIES

> ⚠️ **APPENDED, NOT OVERWRITTEN — deliberate deviation from `AGENT.md`, flagged for AEOLUS.**
> `AGENT.md` says *"Overwrite it each run — it holds the most recent run only."* **I did not overwrite.** The report above is a **different run** (Colorado River ROD signed, Powell through its all-time low) and was **uncommitted** at the time I ran. Overwriting would have destroyed the only copy of a run that resolved two standing watches. `AGENT.md`'s overwrite rule assumes one worker per session; **two scoped workers ran today**, and the rule has no case for that. **Reported rather than resolved — AEOLUS rules on whether `AGENT.md` needs an amendment.**

```
run_date:   2026-08-21
scope:      AGENTS/AEOLUS/water/ only. Nothing outside was read for write or written.
task:       build the ACP Monthly Canal Operations Summary series 2023-10 .. 2026-07 (34 months)
grading:    NONE. No channel scored, no trigger fired, no prediction resolved.
deliverable: water/PANAMA_SERIES.md  (360 lines, 33-month table + per-row advisory URLs)
```

**observations_added:** 34 rows to `workbook/SERIES.tsv` (28 × `panama_transits`, 6 × `panama_max_draft_ft` historical backfill) · 11 rows to `workbook/LOG.tsv`. **No new instrument name was created** — 10 proposals are listed in `PANAMA_SERIES.md` §9 for AEOLUS to accept or reject.

**coverage:** **33 of 34 months.** Every one passed the `monthly total ÷ days-in-month == printed daily average` self-check. Parsed twice by independent methods (coordinate/band reconstruction + text-order blocks) and reconciled row by row — **the two agreed on every reported value in all 33 months.**

**threshold_state (reported, NOT graded):**
- `panama_transits` Jul-2026 = **34.03/day** · trough of the series = **22.60/day** (Jan-2024) · max = **38.70/day** (Apr-2026).
- Distance to the registered Yellow band (≤32): Jul-2026 is **2.03 above**. Jun-2026 printed **32.50**, **0.50 above**. **NOT-FIRED. Not graded.**
- ⚠️ **The band's own instrument is disclaimed by its issuer** — A-26-2026: *"The draft adjustment will not affect the number of daily vessel transits."*

**the four things AEOLUS should read first:**
1. 🔴 **Gatun elevation EXISTS in the corpus** — A-27-2024 prints *"Gatun Lake today is at 85.02 feet (25.91 m)"* (+ Alhajuela 217.24 ft). One spot reading, not a series, but it **corroborates the carried 82–87 ft PLD range at the issuing agency** and fixes unit + datum. → §5b
2. 🔴 **Sep-2025 auctioned utilisation is printed as 95.34%, not 98.31%.** The 354/348 pair is right; **98.31 is a recomputed value that replaced the printed one.** Root `CLAUDE.md`'s new Panama guard row currently cites 98.31. Same class in Aug-2025 (printed 96.18 vs computed 96.71). → §8
3. 🔴 **Draft is fully recoverable** as an 8-step series 44 ft (trough) → 50 ft (recovered) → 47.5 ft (Sep-2026) — **but only from the discretionary news article ACP appends, never from the statistics table.** The earlier "no draft/tonnage/Gatun" finding was right for 2 issues and wrong for the corpus: **a schema check of the table is not a check of the document.** → §5a, §5c
4. 🔴 **Auctioned utilisation is ambiguous as a ratio.** Oct-2023 = 95.21% on **146** slots; Sep-2025 = 95.34% on **354**. Near-identical ratios, **2.5× the absolute demand**; ACP controls the denominator as a policy lever, and utilisation *fell* to its 48.16% series low as conditions *improved*. **Store both levels.** → §6

**gaps (exact errors, no substitution):**
- **Mar-2024 `A-11-2024`** — HTTP 200, 508,177 B, **AES-128 encrypted with a user password**. `pdfminer: PDFPasswordIncorrect` · `pdftotext: Command Line Error: Incorrect password` · `pikepdf: PasswordError: invalid password`. Non-`-1` filename variant = HTTP 200 but an **HTML soft-404** (`No /Root object`). It sits between Feb-2024 (22.8/day) and Apr-2024 (26.3/day) — **the steepest part of the ramp. Do not interpolate it.**
- **Gatun lake level for 2026 remains UNINSTRUMENTED.** A-26-2026 invokes *"current water levels … in Gatun Lake"* as its basis for cutting draft and **prints no figure**. Lead, unverified by me: the vessel-queue bullet in the 2023 issues is hyperlinked to `apps.pancanal.com/t/TI/views/DashboardColadeEspera/DashboardCola-EN`, **confirming the Tableau host+path pattern `SOURCES.md` records for `GatunH2OIndicators`**; the two reservoir-level bullets are **not** hyperlinked (checked at the PDF annotation level).

**proposed SOURCES.md amendment (AEOLUS ratifies):** `https://pancanal.com/en/maritime-services/advisory-to-shipping/` returns the **complete** archive server-rendered (762 KB, 1,005 PDF anchors, back to 2002). **Validated before use: it reproduced all 7 of AEOLUS's known-good URLs byte-identical, 7/7**, including the `ADV21` vs `ADV-04` inconsistency and the trailing-dash quirk. **This does NOT retire the known-bad `/en/advisories-to-shipping/` entry — different URL, still stale.**

**→ Full tables, all four booking-slot lines, and per-row advisory URLs: `water/PANAMA_SERIES.md`**

### ⬛ ADDENDUM — reconciliation with AEOLUS's mid-run guidance (arrived after the build completed)

**All six supplied URLs match mine byte-identical.** The three "answers that narrow your job" reconcile as follows — full working in `PANAMA_SERIES.md` §11.

| Guidance | Verdict | Evidence |
|---|---|---|
| `/uploads/YYYY/MM/` ≈ publication month (data+1) | 🔴 **52% — do not use** | Holds **17 of 33** observed URLs. Fails **15 of 21** in Nov-2023→Sep-2025 — the drought window it was offered to speed up. 15 misses collapse to a `/YYYY/01/` bucket; the 16th is **Apr-2026**, which is *inside the six-URL sample the rule came from*. |
| "Tonnage/draft/Gatun are NOT in the Monthly Summary" | 🟠 **right about the table, wrong as a stop-hunting order** | Literal `PLD`=0 and `elevation`=0 across all 33 — **I reproduce that exactly.** But A-27-2024 prints *"Gatun Lake today is at 85.02 feet"*, a sentence containing **neither token**. Draft appears in **6** issues, tonnage in **5** — incl. **two inside AEOLUS's own 8-issue sample** (A-21-2024 47 ft; A-26-2026 47.5/48 ft). |
| Auctioned slots are the highest-value column; record `used > available` as printed | ✅ **done** | All 33 months, §4. >100% rows reproduce exactly (Apr-2026: 105.65/111.02/114.53), unnormalised. |

🔑 **Both corrections point the same way: the statistics table is fixed-schema, the appended news article is discretionary.** A schema fact about the table cannot generalise to the document, so per-issue sweeping is the only method that finds these — and it costs one regex pass over already-extracted text. **Had I applied the "note the absence and move on" instruction, I would have skipped the single item the brief named as highest-value.**

⚠️ **Sep-2025 was quoted as 98.31% a second time in the guidance. A-30-2025 prints 95.34%.** The 354/348 pair is right; the percentage was recomputed rather than read, and the recomputation has now propagated into root `CLAUDE.md`'s Panama guard row.

**Drought-trough priority satisfied:** Nov-2023 → May-2024 complete except **Mar-2024** (password-protected, §7a). Trough values: **Jan-2024 22.60/day · Feb-2024 22.80/day**, against 38.70 at the Apr-2026 peak.
