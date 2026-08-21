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
