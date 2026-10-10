# AEOLUS · WATER — SOURCES ARCHIVE (cold)

> **COLD — never boot-read; grep it.** Created 2026-10-10 by an AEOLUS-spawned hygiene worker. The pre-split `SOURCES.md` (58,846 B, crc32 215640833; blob at commit `1f0334263`) was over the 32,550 B read cap (`AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md`) and past the ~54,250 B point where the Read tool truncates silently, so workers were reading a cut-off command file. It was split into HOT [`SOURCES.md`](SOURCES.md) (commands, reference values, one-line caveats) and this file.
> **Verbatim, not deleted.** Each block below is a contiguous run of pre-split lines, copied byte-for-byte, under its original section header (copied verbatim too). Lines already kept verbatim in HOT (every command, the characteristic-values and known-bad tables) are not repeated here. The narrative, history, superseded entries, corrections and verification stories live here. HOT's caveats are one-line summaries of them, so read the block before relying on a nuance.
> **Receipts:** `python3 PROME/tools/measure.py` run on each block saved alone (block lines plus one final newline). `Lnn` = line numbers in the pre-split file. To re-check one: `git show 1f0334263:AGENTS/AEOLUS/water/SOURCES.md | sed -n 'a,bp' > /tmp/b.txt && python3 PROME/tools/measure.py /tmp/b.txt`.

| Block | Original section | Pre-split lines | Bytes | crc32 |
|---|---|---|---:|---:|
| B01 | 1. DROUGHT | L10–10 | 177 | 855670553 |
| B02 | US Drought Monitor | L17–19 | 444 | 1142135581 |
| B03 | State granularity | L24–25 | 697 | 3326233919 |
| B04 | State granularity | L33–37 | 1052 | 1448585108 |
| B05 | Palmer Drought Severity Index | L41–41 | 102 | 1571107172 |
| B06 | 2. SNOWPACK | L54–56 | 368 | 3981904956 |
| B07 | 3. STREAMFLOW | L73–73 | 361 | 581691835 |
| B08 | Powell | L89–89 | 168 | 1886742490 |
| B09 | Seasonal base rate | L106–106 | 257 | 2102089632 |
| B10 | ✅ 24-MONTH STUDY ARCHIVE + MIN/MAX PROBABLE | L118–131 | 2095 | 2866970010 |
| B11 | 🔴 24-MONTH STUDY | L135–135 | 148 | 3526036667 |
| B12 | 🔴 24-MONTH STUDY | L143–152 | 1781 | 4212065210 |
| B13 | Colorado Post-2026 Guidelines | L155–159 | 844 | 413314577 |
| B14 | Rhine at Kaub | L170–180 | 564 | 2484329765 |
| B15 | 🔴 WSV CHARACTERISTIC VALUES | L198–213 | 6011 | 130319142 |
| B16 | 🔴 WSV FORECAST endpoint | L221–222 | 611 | 1966865399 |
| B17 | DISCHARGE Q | L225–227 | 670 | 1481060013 |
| B18 | ✅ RHINE BARGE FREIGHT | L230–232 | 671 | 3280754084 |
| B19 | ✅ RHINE BARGE FREIGHT | L245–248 | 2265 | 1070764695 |
| B20 | ✅ RHINE BARGE FREIGHT | L258–264 | 2675 | 3818614415 |
| B21 | ✅ RHINE BARGE FREIGHT | L279–287 | 2520 | 656341668 |
| B22 | ✅ YANGTZE | L299–302 | 739 | 253837434 |
| B23 | ✅ DANUBE | L308–310 | 402 | 3523848654 |
| B24 | ✅ DANUBE | L314–316 | 680 | 1801854103 |
| B25 | ✅ PARANÁ | L322–325 | 831 | 3818978826 |
| B26 | ✅ PARANÁ | L329–332 | 1116 | 625133242 |
| B27 | ✅ MISSISSIPPI | L336–336 | 230 | 3276199610 |
| B28 | ✅ MISSISSIPPI | L347–364 | 1876 | 648192318 |
| B29 | ✅ MISSISSIPPI GRAIN BARGE FREIGHT | L367–367 | 448 | 1687867680 |
| B30 | ✅ MISSISSIPPI GRAIN BARGE FREIGHT | L378–379 | 845 | 3214235400 |
| B31 | 🔴 Panama | L383–385 | 241 | 291695952 |
| B32 | 🔴 Panama | L391–401 | 594 | 1316510398 |
| B33 | ✅ GATUN LAKE ELEVATION | L410–416 | 1718 | 3122336310 |
| B34 | ⬇️ SUPERSEDED | L422–429 | 1310 | 524864364 |
| B35 | ✅ PANAMA | L433–433 | 198 | 2278843912 |
| B36 | ✅ PANAMA | L435–448 | 2578 | 3827809245 |
| B37 | ⚠️ CORRECTED 2026-08-21 | L452–457 | 1231 | 2518549064 |
| B38 | 🔑 GATUN LAKE ELEVATION | L461–465 | 868 | 288213425 |
| B39 | ✅ THE COMPLETE ADVISORY ARCHIVE | L469–470 | 307 | 2470735308 |
| B40 | ✅ THE COMPLETE ADVISORY ARCHIVE | L474–475 | 505 | 460219391 |
| B41 | 🔴 STILL-TRUE NEGATIVES | L479–483 | 710 | 2259797282 |
| B42 | ✅ THE COLUMN THAT REPLACES THE UNPUBLISHABLE | L487–497 | 1074 | 1870191156 |
| B43 | 🔴 DO NOT SCRAPE THE ADVISORIES INDEX | L502–506 | 875 | 310216590 |
| B44 | AEO-04 resolution | L509–509 | 434 | 3187375230 |
| B45 | ⚠️ ACP'S OWN ARITHMETIC DISAGREES WITH ITSEL | L525–531 | 778 | 2566766381 |

---

## 1. DROUGHT — the shared upstream input (C2 · C4 · C5 · C6)

`[B01 · L10–10]`

> 🔑 **This section is the canonical home for drought.** It previously sat in `../wildfire/SOURCES.md`, which made it invisible to the other three channels that depend on it.

### US Drought Monitor — statistics API ✅ verified 8/13

`[B02 · L17–19]`

**Verified CONUS (valid 8/11):** `none 26.38 · d0 73.62 · d1 50.38 · d2 29.50 · d3 10.27 · d4 1.04`
⚠️ **Returns rows for `CONUS` *and* `Total` (US + PR) — read the `areaOfInterest` field.** They differ by ~8 pp and are trivially confused.
⚠️ **The human-facing `droughtmonitor.unl.edu` pages return *"the tabular data did not load"* to a fetch tool.** The web page failing is **not** the data being unavailable — use the API.

### State granularity — 🔴 **RECIPE REPLACED 2026-09-18. THE OLD ONE WAS DEAD AND THIS IS THE FILE WORKERS ARE TOLD TO COPY FROM.**

`[B03 · L24–25]`

**Superseded text, preserved so the failure is visible:** *"State/county granularity — same API, swap `aoi`. `aoi=CO` (state postal) or a county FIPS."*
**Why it was dead:** `aoi=CO` — **its own literal example** — returns `-area of interest not recognized`. It is the wrong ENDPOINT (`USStatistics`), the wrong KEY FORMAT (postal, not FIPS), and it omits a required header. The working recipe existed only in `DOSSIER.md` §1, i.e. **the correct command was in the file nobody is told to copy from, and the broken one was in the file everybody is.** *(Second instance of this class today — see `../hurricane/AGENT.md`. A read-early file's errors are inherited by everything downstream.)*

`[B04 · L33–37]`

**Verified 2026-09-18.** State change 8/25→9/15: **TX +23.65pp · MS +21.97 · MO +17.61 · TN +16.46 · CA +8.42 · AR +3.79** deteriorating; **IA −12.85 · NE −7.11** improving.

**Use this before claiming a drought signal reaches a specific crop belt or fire geography** — the 8/13 C2-vs-C4 discrimination turned entirely on *where* the deterioration was, and so does the 9/18 one.
> 🔑 **One dataset, four consumers, and it currently drives them in OPPOSITE directions** — drought feeds the **fire** channel (TX/OK, and TX is the largest deterioration in the table) and the **river** channel (lower Mississippi, the same basin whose Memphis stage fell 13.10 ft in 21 days) while the **corn belt IMPROVES**. **Never collapse this to a single national adjective; the divergence IS the read.** KB-AEO-138.
> ⚠️ **Extent and intensity moved apart on 9/15:** CONUS D1-D4 plateaued near **59%** (52.70 → 56.61 → 59.05 → 58.59 → **59.37**, ending the four-week acceleration) while **D4 rose 1.75 → 2.02**. Quote both or neither.

### Palmer Drought Severity Index (CPC)

`[B05 · L41–41]`

Longer-memory index than USDM. **Better for multi-season persistence; worse for current conditions.**

## 2. SNOWPACK — sets the following year's allocation

`[B06 · L54–56]`

**Read Apr-1 basin % of median as the allocation-setting figure.**
⚠️ **Seasonal — near-zero Jun–Sep.** In August this is *correctly* empty; do not log it as a gap.
🔑 **The basin that matters for Powell is the UPPER Colorado** — and it sits near the ENSO dipole pivot where the signal is weak. See `DOSSIER.md` § "El Niño does not refill the Colorado."

## 3. STREAMFLOW — USGS NWIS ✅ verified 8/13

`[B07 · L73–73]`

🔑 **Lees Ferry (`09380000`) is the single most informative gauge in this folder.** It is the **Upper/Lower Basin compact division point**, and because it sits just below Glen Canyon Dam **it measures Glen Canyon's releases directly** — i.e. **the water that refills Lake Mead.** It converts the Powell↔Mead coupling from an inference into a measurement.

### Powell (919) and Mead (921) — daily pool elevation ✅ verified 8/13

`[B08 · L89–89]`

⚠️ **The files are long and chronological — you MUST `tail`.** A page-summarizing fetch truncates a 22k-row file and returns **1976 data with a clean HTTP 200**.

### Seasonal base rate — REQUIRED before extrapolating any rate (L-16)

`[B09 · L106–106]`

⚠️ **A base rate is only valid while the mechanism generating it still holds.** Mead's Aug→Sep *rise* is driven by Glen Canyon releases — and **2026 releases are at a 9-year low** (§3). **Check Lees Ferry before trusting Mead's seasonal pattern.**

### ✅ 24-MONTH STUDY **ARCHIVE + MIN/MAX PROBABLE** — probe 2026-08-27, and both were declared non-existent in my own files

`[B10 · L118–131]`

🔴 **AEO-10's notes carried *"USBR 24-month-study projection error NOT base-rated, so the buffer has no error bar"* from 8/13 to 8/27 — while the issuer published an error bar every month and archived every past study, one directory level from a file I used daily.** Same class as the Gatun gap (L-35): **a declared absence I never re-tested.**

**THE BASE RATE, built from the archive in ~15 minutes** — each **August** study's projected end-December Mead vs the **actual** 12/31 elevation (AEO-10's exact horizon and instrument):

| | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|
| **actual − projected (ft)** | −1.56 | +0.54 | +4.04 | +2.78 | +0.97 | **+6.36** |

**n=6 · mean +2.19 · median +1.88 · stdev 2.56 · 5 of 6 finished HIGHER.** ⇒ **USBR's August studies systematically UNDER-project December Mead.**
**Mechanism:** the studies model *scheduled* operations and full contracted deliveries; actual LB use runs below entitlement because conservation (ICS, DCP/500+, LC Conservation Program) is **voluntary and additive** — structurally upside-only. **The bias is growing in the conservation era.** ⚠️ **Which is also its limit — it is DISCRETIONARY, and the 2027-28 Guidelines just replaced the framework that produced it (L-18 applies to error base rates too).**

⚠️ **AND THE AUGUST DEVIATION IS NOT A SIGNAL.** corr(August error, December error) = **+0.287 at n=6 — below the noise floor.** **2025 ran 0.64 ft BELOW in August and finished +6.36 ABOVE.** **Do not use "tracking below the path" as evidence** — I did, in four packets, and had to retract it (KB-098).

**METHOD — do not skip this.** Extract with pdfminer; the elevation tables come out as a bare column with no month labels. **Anchor on a known ACTUAL and match the study's historical head month-by-month against `921/csv/49.csv` to within 0.02 ft before reading ANY projected cell.** *(10–12 consecutive months matched per study in the run above — the alignment is self-verifying, and an unverified alignment silently shifts every figure by a month.)*

### 🔴 24-MONTH STUDY — registered 2026-08-27 as the PRIMARY C6 instrument (it was NOT in this file before)

`[B11 · L135–135]`

**This is the forward-looking instrument. The daily elevations above are the backward-looking one.** It is what moved AEO-10 and it prints monthly.

`[B12 · L143–152]`

⚠️ **AUGUST 2026 IS SPLIT INTO TWO FILES AND EVERY OTHER MONTH IS ONE.** `24Month_08_6.pdf` (6 maf Powell release) and `24Month_08_7.pdf` (7 maf) — **scenarios keyed to the WY2027 release decision.** A scraper expecting one file per month silently misses a branch. *(Mead's path is identical in both through Apr-2027; they diverge from May-2027.)*
⚠️ **`.../lc/region/g4000/24mo.pdf` served the JULY study on 2026-08-27, six days after the August one published.** **Check the document's own title line — never trust "current" in a URL.**

**HOW TO READ IT — this is where I went wrong.** The elevation tables extract as a bare column of numbers with no month labels.
1. **Anchor on a known ACTUAL** (e.g. Mead 2025-12-31 = 1062.24) and count outward; values are **end-of-month**.
2. **VERIFY the mapping** against the daily CSV for ≥6 consecutive months before trusting any projected cell. *(I verified 12 months to the cent.)*
3. 🔴 **READ THE PATH, NOT THE ENDPOINT.** A criterion saying *"at any point through 12/31"* is graded on the projected **MINIMUM over the window**. **Grading AEO-10 on the 31-December value overstated its buffer 2.4× for two weeks** (0.86 ft real vs 2.1 ft claimed) — **L-36**.
4. The narrative pages carry the **release decision, the runoff forecast as % of average, and the operating tier** — often more decision-relevant than the tables.

**Aug-2026 study, key figures (all verbatim/primary):** WY2026 Powell release cut **7.48 → 6.00 maf** · July unregulated inflow **9% of average** · **April–July 1.14 maf = 18% of average** · WY2026 forecast **37%** · *"Lake Powell's elevation is projected to decline below 3,510 feet during water year 2027"* · Mead **Dec-2026 projected 1,034.74 ft** (below the binding 1,035).

### Colorado Post-2026 Guidelines — the policy clock

`[B13 · L155–159]`

`https://www.usbr.gov/ColoradoRiverBasin/` · DOI newsroom · **Federal Register** (search *"Colorado River"* + *"Record of Decision"*) → milestones in `../CALENDAR.md`.

⚠️ **ROD PATH — the one recorded earlier 404s.** ✅ Working, verified 2026-08-27:
`https://www.usbr.gov/ColoradoRiverBasin/post2026/decision-doc/P26_RecordofDecision_Final.pdf` (1.17 MB → 136,430 chars via pdfminer). Same directory: `2027-2028OperatingGuidelines_Final.pdf`, `FutureColoradoOperations_Factsheet.pdf`, `P26_BiologicalOpinion_Final.pdf`. ❌ **`/ColoradoRiverBasin/documents/post2026/…` returns 404 — do not reconstruct it.**
🔑 **The ROD adopts a PROCESS, not a numeric alternative.** Do not go looking for "the selected alternative" — that string does not appear. The binding numbers live in the **Operating Guidelines**, a separate PDF.

### Rhine at Kaub (WSV/PEGELONLINE, German federal primary) ✅ verified 8/13

`[B14 · L170–180]`

**Verified 8/13 15:15 CEST: 13.0 cm**; 3-day range **10–17 cm**. Values in **cm**, 15-min cadence.
**Station names VERIFIED against `stations.json?waters=RHEIN` on 2026-08-13** (36 Rhine stations; these 6 confirmed):

| shortname | Rhine-km | role |
|---|---|---|
| `MAXAU` | 362.3 | upper Rhine |
| `WORMS` | 443.4 | |
| `MAINZ` | 498.3 | |
| **`KAUB`** | **546.2** | **the binding shoal — reference gauge for loading economics** |
| **`DUISBURG-RUHRORT`** | **780.8** | **the station named in the C5 upgrade trigger** |
| `EMMERICH` | 851.9 | Dutch border |

### 🔴 WSV **CHARACTERISTIC VALUES** — probe 2026-08-27, and it reframes the C5 trigger

`[B15 · L198–213]`

🔴🔴 **THE FROZEN `NNW` VALUES ARE LOAD-BEARING — DO NOT "TIDY" THE C5 TRIGGER BY RE-POINTING IT AT THE LIVE FIELD.** *(AEOLUS ruling, 2026-09-18.)*
The C5 →5 trigger is keyed to **`NNW` Kaub 25 / Duisburg 153 as FROZEN on 2026-08-13**, not to whatever the API returns today. **That freeze was done as bookkeeping hygiene and has since become the only thing protecting the trigger.**
**Why:** `NNW` is *"niedrigster bekannter **Tagesmittelwert** des Wasserstandes"* — the lowest known **daily mean** — so **WSV rewrites it whenever a new record is set.** Had the trigger read the live field, the **2026-09-10/11/12 fire would have moved its own threshold out from under itself**: Kaub's daily mean of **21.531** would have *become* the new `NNW`, and the test would have evaluated 21.531 ≤ 21.531 — or, one refresh later, failed against a bar the event itself had just lowered.
⇒ **A threshold keyed to a live record field cannot fire on a record.** Re-pointing this trigger at `characteristicValues` would look like a tidy-up and would silently destroy it. **Re-read `NNW` and its `occurrences` date at every grading to DETECT a republication — never to re-key the trigger.** *(Entry 2 of the MOVING-REFERENCE REGISTER in `DOSSIER.md`.)*

🔴 **UNIT WARNING — the last column is NOT in the same quantity as the other four (labelled 2026-09-18, AEOLUS-approved).** The first four columns are **stages** (cm above gauge zero). **`TuGLW` is *"verkehrsgesicherte Fahrrinnentiefe unter GlW (Tiefe unter GlW)"* — the traffic-secured fairway DEPTH measured DOWNWARD from `GlW`.** WSV defines the maintained navigable channel this way: the guaranteed depth sits *beneath* the GlW plane. **Never difference TuGLW against a gauge reading, and never read Kaub's 190 as "a level of 190 cm"** — it means 190 cm of channel depth is maintained when the river is at GlW (77 cm). Differencing a depth against a stage produces a number with no physical meaning.

✅ **`GlW` VERIFIED AT THE PRIMARY 2026-09-18.** Kaub **77.0** and Duisburg-Ruhrort **227.0**, both `validFrom` **2023-01-01** — the carried candidates were correct. **Definition (WSV/BfG):** the stage **equalled or undercut on average 20 ice-free days per year**, derived by first computing the equivalent discharge **`GlQ`** from ~100 years of daily mean discharge at the gauge, then converting `GlQ` to a stage from measured water-surface elevations at discharges near `GlQ`. ⇒ **a duration-curve NAVIGATION plane — categorically a different kind of object from `NNW`.** Re-check `validFrom`, not just the number: GlW is periodically redetermined.
🔑 **`NNW` is also now pinned at the primary:** PEGELONLINE's definitions page (`/gast/hilfe`) gives **`NNW` = *"niedrigster bekannter **Tagesmittelwert** des Wasserstandes"*** — the lowest known **daily mean**. **This confirms the C5 trigger's basis is like-for-like** (unrounded daily means graded against NNW). ⚠️ Kaub additionally publishes **`NW` 25.0** *"Niedrigster Tageswasserstand"* over 2010-11-01…2020-10-31 with the same occurrence date — **same number, different scope; NW and NNW are NOT two independent witnesses.**

🔴 **SCOPED DOWN 2026-09-18 — this claim was about ONE ENDPOINT, not about WSV.** *(Superseded wording, kept verbatim so the change is visible: "THE MULTI-YEAR SERIES IS GENUINELY UNREACHABLE — confirmed four ways, so the 9/30 obligation cannot be met as written.")* **The REST wall is real and is now confirmed at n=6** — `P31D`/`P45D`/`P60D`/`P90D`/`P150D`/`P365D` all return the identical row set, and explicit 2024 **and 2018** date ranges return zero. **BUT PEGELONLINE's own help page states verbatim that historical stage AND discharge are downloadable *seit dem 1. Januar 2000* (as `ungeprüfte Rohdaten` — unverified raw data), and the file service already serves 91 daily files for Kaub** (`/webservices/files/Wasserstand+Rohdaten/RHEIN/1d26e504-7f9e-480a-b52c-5932be6549ab`, Duisburg `c0f51e35-d0e8-4318-afaf-c5fcbc29f4c1`), each with `down.csv`/`down.txt`/`down.zrxp`. **Unresolved is the ROUTE, not the availability:** dates outside that ~91-day listing 404, and the back-to-2000 bulk download is a JS-driven zip builder on `/gast/pegeltabelle`. **Treat the 9/30 obligation as plausibly meetable and retry — do not re-close this gap from the REST result alone (L-35).** Original supporting detail follows:** PEGELONLINE returns the **identical ~31-day window** for `P31D`, `P45D`, `P60D` and `P90D` (2,976→2,991 rows, 2026-07-28 → 2026-08-28), and an explicit **2024 date-range query returns ZERO rows** — it is a **retention** wall, not a query limit. UNDINE (`undine.bafg.de`) is an **extreme-events narrative portal**, not a series download. GRDC is discharge, not stage.

🔑 **BUT THE PROBE CHANGED THE QUESTION.** My trigger levels — **Kaub ≤25, Duisburg ≤153 — ARE each station's all-time record low (`NNW`).** A record is by construction a ~1-in-record-length event *per station*; requiring **both simultaneously for 3 days** is rarer still. **That is not an upgrade trigger, it is a confirm-the-catastrophe gate**, and it explains why C5 sat at 4 for weeks and then fired only during a genuinely historic event.
**The economically meaningful line is sitting right beside it: `GlW` (gleichwertiger Wasserstand) — the waterway administration's own low-water NAVIGATION reference, derived from a duration curve. Kaub 77 cm · Duisburg 227 cm.** That is far closer to where freight economics actually bite *(my logged ~€150/t and ~16% loadings occurred with Kaub in the 30–40 cm range — well below GlW, well above NNW)*.

⛔ **RE-KEY PROPOSED, NOT EXECUTED.** Two things must happen first: **(1)** confirm `GlW`'s exact definition and exceedance percentile at WSV/BfG documentation — **do not infer it**; **(2)** base-rate the level. **I will not repeat registering a threshold because the number was easy to defend rather than right** — which is exactly how 25/153 got chosen.

### 🔴 WSV FORECAST endpoint — registered 2026-08-13 (found by the water worker, verified by AEOLUS)

`[B16 · L221–222]`

⚠️ **NOT listed in the station's `timeseries` array** (which shows only `Q` and `W`) — **undiscoverable from metadata; found by direct probe.**
⚠️ **HORIZON IS SHORT AND THE WORKER'S REPORT OVERSTATED IT.** My verification pull returned **25 forecast points spanning 8/13→8/15 only (~2 days)**. The run report quoted **8/17** values and a *"Kaub rebounds to 11"* shape; **those are NOT reproducible in my pull, which shows Kaub falling monotonically to 7.0 cm on 8/15 with no rebound in range.** **Adopt the endpoint; do NOT adopt the 8/17 figures.** Re-pull and state the actual horizon each time.

### DISCHARGE `Q` — datum-independent, available at all six

`[B17 · L225–227]`

`/stations/<ST>/Q/measurements.json` — m³/s, 15-min. Kaub ~492 m³/s (8/13). **Prefer discharge for cross-era comparison**, since stage depends on a `gaugeZero` that has been re-referenced at some stations.

⚠️ **PROVENANCE GAP on the carried "40 cm uneconomical" line.** That figure has **no source recorded in this file** — it is carried, not verified. The authority's own navigation references are **`GlW` (Kaub 77 cm — a STAGE)** and **`TuGLW` (Kaub 190 cm — ⚠️ a fairway DEPTH beneath GlW, not a stage; see the unit warning above)**. **The 40 cm line is retained as an unprovenanced working figure and is explicitly NOT the basis of any trigger.**

### ✅ RHINE BARGE FREIGHT — GAP CLOSED 2026-09-28 (two sources, two jobs; Will-directed search, verified by AEOLUS)

`[B18 · L230–232]`

*(Superseded line, verbatim: "⚠️ **No verified source for barge FREIGHT rates.** The ~€150/t figures in my dossier are trade-press relays (PJK/Bloomberg via gCaptain/Insurance Journal), **not a primary I can re-pull.** Finding a resolvable freight series is an open gap." — the ~€150/t relays remain unverified and are NOT promoted by this entry.)*

**① Contargo low-water surcharge (KWZ) — DAILY, a live PRICE, keyed to the same gauges as my C5 trigger.** Contargo (Rhine container-barge operator, Rhenus/HGK group) publishes its own surcharge schedule by gauge and a daily table of 05:00-CET ELWIS levels + tier per departure date, with a 3-day forecast.

`[B19 · L245–248]`

Standard schedule (all tiers, EN): `https://www.contargo.net/en/business/auxiliary-conditions/low-water/` — Kaub standard tiers stop at 81 cm (€120 / €165); **≤80 cm "by agreement"**. The DE page carries the **extended "freie Vereinbarungen" schedule in force now**: **Kaub ≤40 cm → €1,075 per full 20′ / €1,280 per full 40′**; Duisburg 130–121 cm → €800 / €900 (schedule printed down to 121 cm only).
⚠️ **Caveats:** (a) ONE operator's tariff, **container segment only** — not a market index, and not tanker/bulk (heating oil moves by tanker barge); (b) the page is an **episode news item** — its URL may change in a future low-water event (re-find via the EN page's "Waterlevels" widget); (c) the `(KWZ-Staffel)` tier number does not map cleanly onto the printed rows at Kaub (reads `(6)` against a 5-row extended schedule) — **quote the €-row by gauge level, never the tier number**; (d) two operator statements, on DIFFERENT pages (attribution corrected 9/28 after WALTER could not find the first on the DE text it read): **"Transportverpflichtung endet" — transport obligation ENDS at Kaub ≤80 cm / Duisburg ≤180 / Köln ≤105 / Emmerich ≤30 — is on the DE business-news page**, followed by *"Dennoch versuchen wir alles uns Mögliche, um Ihre Container zu transportieren"* (they still try to carry: **obligation ended ≠ service stopped**); **"may become necessary to temporarily suspend" Upper-, Middle-Rhine and Rhine-Main services is on the EN low-water page UPDATE** (conditional: *"should current forecasts materialize"*). Both read 2026-09-28 — an operator's written statement, the closest thing to an operational-leg event I have.

**② CBS (Statistics Netherlands) services PPI, table 85817NED — QUARTERLY, 2021=100, the HISTORY + base rate.** Dutch IWT-company panel, fixed routes, observed twice a quarter, **INCLUDES fuel AND low-water surcharges**, excludes (un)loading. Segments: `A042621` dry bulk SPOT (the low-water-sensitive one) · `A042620` dry bulk contract · `A042619` wet bulk · `A023824` container · `A023820` all goods. Segments from 2018-Q1; all-goods from 2014-Q4. (Old table 84050NED, 2015=100, discontinued 2024-05-17 — same data, different base; do not splice bases.)

`[B20 · L258–264]`

**Base rate (the two recorded low-water autumns):** dry-spot **87.4 (2018-Q2) → 163.3 (2018-Q4), +87%**; **2022-Q3 191.7, +104.1% y/y**. ⚠️ **Fuel contaminates it:** 2021-Q4 dry-spot +43.2% y/y is NOT attributed to low water here. **n=2 low-water episodes is not a band** — no threshold registered. Latest **2026-Q2: dry-spot 130.5 (+11.4% y/y), all-goods 135.9 (+6.5%)** — BEFORE this autumn's record; **2026-Q3 is the first print that can show it** (not yet published 9/28).

**③ TANKER BARGE (heating oil / gasoil) — added 2026-09-28 (Will-directed). NO free €/t series exists; four partial surfaces, ranked.** The €/t assessors are all paywalled: **Insights Global / BargeINSIGHTS** (formerly PJK — the CCNR's own source), **Spotbarge** (JS app, login), **Argus**, **Platts**.
- **(a) CBS 85817NED `A042619` wet bulk (natte bulk) — THE re-pullable tanker instrument.** Quarterly, 2021=100, Dutch tanker-barge operators, includes fuel + low-water surcharges. Same command as ② (the filter already includes `A042619`). **Base rate:** 2018-Q2 94.1 → 2018-Q4 129.7 (**+38%**); 2022-Q3 141.7 (**+51.5% y/y**). **2026-Q2 140.6 (+1.1% y/y)** — ⚠️ the LEVEL is already at the 2022 peak while y/y is flat (2025-Q2 was 139.0): a level read and a y/y read disagree; **quote both**. 2026-Q3 = first print covering this event.
- **(b) Insights Global weekly "Rhine Freight Market" blog — FREE, dated, QUALITATIVE.** `https://www.insights-global.com/category/blogs/freight-rates/` → newest "Rhine Freight Market: …" post (`"datePublished"` in page JSON). Gives **daily direction + DEAL COUNTS** (e.g. week of 9/14: 3 · few · **20** · few · **2** deals) and route notes — **no €/t** (that is the paid product). Record direction + counts, never infer a level.
- **(c) Named-source point quotes via the press — SECONDARY, log to `LOG.tsv` only, never `SERIES.tsv`.** Platts citing **Spotbarge**, ARA→Basel gasoil: **€35/t (6/03) · €69.30 (7/01) · €276.67 (8/14) · €165 (9/11) · €215 (≈9/18–21)** (Platts via hellenicshippingnews republication 9/21; Spotbarge told Platts *"actual freight rates vary widely, depending on the barge and owner"*). Argus free news 7/30: rates to Duisburg/Frankfurt/Karlsruhe at **records since its assessments began in 2012**; Cologne/Basel higher only in Aug 2022. A search summary's "ARA–Karlsruhe €215/t, five-fold from €45" was NOT traced to a page — not logged.
- **(d) CONSUMER end — fastenergy.de heating-oil price by Bundesland, DAILY, free.** €/100 L, 3,000 L order, incl. delivery + VAT; today + yesterday only (build the series forward; **no history, no base rate**).

`[B21 · L279–287]`

⚠️ **Confounded — do not read a state spread as a Rhine signal without a second leg.** Supply differs by region (north via ports, east via pipeline, south via Ingolstadt/Karlsruhe refineries + Rhine). 9/28: Rhine-served Hessen 174.98 · NRW 173.25 · RLP 172.99 are high — but pipeline-served Sachsen-Anhalt is highest (175.58) and Hamburg lowest (162.53). heizoel24's state table is JS-rendered (dashes via curl); tecson's regional note is undated prose.

**④ DRY BULK / GRAIN on the Rhine — searched 2026-09-28 (Will-directed). NO free €/t grain-barge series exists.** Dry-bulk €/t assessors (inlandcargo.eu — dry bulk + container, daily, demo/login; Insights Global; brokers) are paywalled. What is free:
- **CBS 85817NED `A042621` dry bulk SPOT** (quarterly; ② above) — the re-pullable dry-bulk PRICE instrument. Not grain-specific.
- **Schuttevaer "Aan de reis" weekly column** (Dutch trade weekly; analysts Wouter van der Geest — dry cargo — and Lars van Wageningen, Insights Global — tanker). ⚠️ **METERED PAYWALL:** the newest week was fully readable on 9/28 (week 39, published 2026-09-23); weeks 37–38 were already paywalled beyond the lede. **The free LEDE carries total Dutch-fleet dry-cargo tonnage** (wk37 3.5 Mt +19% · wk38 3.2 Mt −8.4% · wk39 3.25 Mt +3%). The full text, when readable, adds **agribulk tonnage** (wk39 **370,000 t, +85,000 / +30%**), Ruhr-corridor and above-the-gorge tonnage (wk39 620,000 t; 75,000 t) and — in the TANKER section, not dry — Insights Global's Rhine **tanker €/t** (wk39: Rotterdam→Duisburg **€45**, Köln €75, Frankfurt €150, Karlsruhe €195, Strasbourg €230, Basel **CHF 220**; Kaub 26 cm at the time). **Log as SECONDARY (named analysts) to `LOG.tsv`; never an instrument row** — it cannot be re-pulled once the meter closes. A German search summary's "€165/t on 9/11" labelled as GRAIN is the ARA→Basel GASOIL figure — mislabelled; discarded.
- **Grain freight is best measured on the MISSISSIPPI** — see the USDA entry in §MISSISSIPPI below.

⚠️ **Candidates NOT adopted:** CCNR market-observation freight indices (built on PJK/Insights Global liquid-bulk ARA-Rhine + the same CBS data; PDF-only, no download) · PJK/Insights Global, Argus, Platts barge freight (paywalled) · agrarheute-type press relays (a secondary claimed €1,350/20′ at Kaub — **NOT on the publisher's page; discarded**).
**Benchmarks:** 2018 all-time low **25 cm** (October) · **≤40 cm** = uneconomical navigation.

### ✅ YANGTZE — gap closed 2026-08-13 (Changjiang Water Resources Commission, the issuing agency)

`[B22 · L299–302]`

⚠️ **The page embeds a clean JSON array (`var sssq = [...]`) — parse that, do not scrape the HTML table.** 14 stations, `z` = level (m), `q` = discharge (m³/s), `tm` = epoch ms.
**Verified 2026-08-13 16:00 UTC:** **Yichang 宜昌 44.43 m / 17,800 m³/s** · **Hankou 汉口 (Wuhan) 20.61 m / 27,600** · **Datong 大通 10.06 m / 31,100** · Shashi 沙市 34.90 · Jiujiang 九江 14.51 · **Three Gorges Reservoir 三峡水库 157.30 m** (outflow 14,900).
**Navigation-relevant stations: Yichang (below Three Gorges), Hankou (Wuhan industrial reach), Datong (the standard downstream gauge).**
⚠️ `www.cjw.gov.cn` does **not** resolve; **`cjh.com.cn` is the working host.** ⚠️ Page is GB/UTF-8 mixed — decode defensively.

### ✅ DANUBE — gap closed 2026-08-13 (OVF, Hungarian national water directorate)

`[B23 · L308–310]`

**Verified 2026-08-13 (18:00 local):** **Budapest 24 cm** · **Baja −4 cm** · **Mohács 10 cm** · Adony −73 cm (Danube km 1598.110).
⚠️ **Values are cm against each station's own local datum — negative is normal, not "below empty."** Same trap as the Rhine.
✅ **SUB-GAP CLOSED 8/13 — the LKV reference is a queryable ArcGIS service, and it ships the authority's own above/below flag.**

`[B24 · L314–316]`

Returns **44 Danube stations from Ingolstadt (km 2457, Germany) to Novo Selo (km 834)** — far beyond the Hungarian reach. Fields: `Vizallas` current cm · **`LKV` lowest-ever cm** · `LKVIdopont` the date it was set · `LNV` highest-ever · `Nullpont` gauge-zero elevation · **`LKV_viszony`** = the authority's own −1/+1 below/above-LKV flag.
⚠️ **EXCLUDE LKV dates of 1799-12-31 / 1884-12-31 / 1894-12-31 — they are null-date sentinels, not real records** (5 of 44 stations). Filter on the year before using an LKV.
⚠️ Danube is **multi-national**; Hungary is one reach. Austria `ehyd.gv.at` (200) and Serbia `hidmet.gov.rs` (200) both respond and are unexplored.

### ✅ PARANÁ — gap closed 2026-08-13 (UNL-FICH, Facultad de Ingeniería y Ciencias Hídricas)

`[B25 · L322–325]`

Whole-basin table: `station | river | current (m) | Δ | previous | ALERT level | EVACUATION level`. **The alert/evacuation columns are published thresholds — this source ships its own reference levels**, unlike the Danube one.
**Verified 2026-08-13:** **Rosario 3.02 m** (Δ −0.01; alert 5.00) · **Santa Fe 3.18** (−0.02; alert 5.30) · Corrientes 3.28 (−0.08; alert 6.50) · Villa Constitución 2.47 · Diamante 3.36 · Barranqueras 3.29.
🔑 **Rosario is the one that matters** — the Up-River port cluster around Rosario handles the large majority of Argentine grain and soy-product exports, so Paraná stage there is a **grain-logistics cost** variable (→ **CARL**, **MARCO**).
✅ **SUB-GAP CLOSED 8/13 — derive the low-water reference from the station's own history rather than looking for a published one.**

`[B26 · L329–332]`

Returns `date | time | level | Δ | — | previous`. **Trailing-year distribution at Rosario (13/08/2025 → 13/08/2026):** min **1.08** · P05 **1.34** · P10 **1.40** · P25 **1.60** · median **2.14** · P75 **2.44** · max **3.03**.
**Use P10 ≈ 1.40 m as the working low-water reference** until a navigation-draft reference is found.
⚠️ **One year is a SHORT base.** The 2021 crisis went far lower — reporting has Rosario near **0.08 m** in May 2020 and 2021 as the lowest since **1944**, with basin discharge ~6,200 m³/s against a ~17,000 normal and a 1944 record of ~5,800. **A trailing-year percentile is a rank within a benign year, not a historic reference.**
🔴 **CORRECTION to my own read from earlier today: 3.02 m is NOT "mid-range" — it is the 99th percentile of the trailing year** (max 3.03, median 2.14). **The Paraná is near the TOP of its recent range, not the middle.** I characterised it as mid-range before pulling the distribution; **the distribution is what made the read possible, and it reversed the adjective.** **This channel is not firing, and it is not close to firing.**

### ✅ MISSISSIPPI — INSTRUMENT GAP CLOSED 2026-08-27 (NOAA NWPS API — the issuing agency)

`[B27 · L336–336]`

🔴 **This band stood with NO METRIC SURFACE AT ALL — a registered threshold under a standing Will directive, graded on an aggregator's word "~normal".** Closed with **~3 weeks to spare** before the Sep–Nov low-water window.

`[B28 · L347–364]`

⚠️ **PIPE IT — never fetch this endpoint raw.** The full JSON is enormous (every historic crest + every flood-impact statement) and will bury a session's context. Ask for the four fields you need.

**Live read 2026-08-27: 12.47 ft @ 2026-08-28T01:00Z. `lowThreshold` = −8 ft. Margin +20.47 ft — NOT STRESSED.**

🔑 **THE `lowThreshold` IS NOT THE RECORD LOW — do not grade a crisis against it.** The same response carries `flood.lowWaters.historic`, which is the far better instrument because it dates the **actual disruption events**:

| Date | Stage | Note |
|---|---|---|
| **2023-10-17** | **−12.06 ft** | the deepest in the series |
| **2022-10-21** | **−10.81 ft** | the other recent barge-disruption autumn |
| 1988-07-10 | −10.70 ft | ⚠️ labelled *"LOWEST STAGE ON RECORD"* — **and two later readings are lower.** NOAA's own statement is stale; **never quote that label** |
| 2012-09-19 | −9.80 ft | |

⇒ **Key the C5 band to the 2022/2023 analogues (≈ −10.8 / −12.1 ft), not to −8 ft.** Those two autumns are when Mississippi barge freight actually repriced into grain logistics — the C5 → goods-CPI path. **A −8 ft reading is a watch, not an event.**

⚠️ **PARTIAL CLOSURE — say so rather than implying full coverage.** **Only Memphis is referenced.** **St. Louis** (USGS `07010000`) returns stage — falling fast, **8.15 → 4.27 ft in 4 days to 8/27** — but **no reference plane was found, so carry that level with NO adjective attached.** **Vicksburg and Cairo AHPS IDs are unresolved** (guessed VICM6/VKBM6/VIKM6, CAIA2/CACT1 all 404; the AHPS `usgsId=` filter did not work as expected). USACE Rivergages + USGS NWIS (§3) remain the fallback routes.

⚠️ **Autumn (Sep–Nov) is the window** — an August "normal" is not evidence of a benign season. I retracted a "firing" read on 7/22 for exactly this.

### ✅ MISSISSIPPI GRAIN BARGE FREIGHT — USDA AMS, registered 2026-09-28 (Will-directed; the issuing agency, free, weekly since 2004)

`[B29 · L367–367]`

USDA AMS "Downbound Grain Barge Rates" (Socrata `deqi-uken`), weekly, **percent of the 1976 Tariff No. 7 benchmark**, 7 origins. **$/ton = rate × benchmark / 100**; benchmarks ($/ton): Twin Cities 6.19 · Mid-Mississippi 5.32 · Illinois 4.64 · **St. Louis 3.99** · Cincinnati 4.69 · Lower Ohio 4.46 · Cairo-Memphis 3.14 (dataset description). ⚠️ The data label is **"Lower Illinois"**, the description says "Illinois" — same benchmark.

`[B30 · L378–379]`

**Base rate (St. Louis, computed 9/28 from 1,179 weekly rows 2004-01-07 → 2026-09-22):** 2022 peak **2,653% ($105.86/t, 10/11)** · 2023 peak **1,326% ($52.92, 9/26)** — the two low-water autumns · 2014 1,033% · 2021 846%. **Latest 2026-09-22: 834.7% = $33.30/t — 97.8th pct of ALL weeks, 87th pct of the SAME calendar week (n=23; median 512.5)**, up 4 straight weeks from 579.7 (8/25).
⚠️ **SEASONALITY + DEMAND confound it:** Sep–Nov is harvest; rates rise every autumn on export demand, not only on low water — **always compare the SAME WEEK across years, never all-weeks.** And river stage does NOT map one-to-one: Memphis troughed 9/14 and rebounded 14 ft while St. Louis's rate kept rising. **No band registered** (low-water episodes n=2: 2022, 2023). Cadence: weekly, posted with the Thursday Grain Transportation Report.

### 🔴 Panama — INSTRUMENT GAP CLOSED 2026-08-13

`[B31 · L383–385]`

**The instrument is the ACP *Monthly Canal Operations Summary*, published as a numbered Advisory to Shipping.** It carries **oceangoing transits, daily average** — exactly the quantity my threshold bands use.

**✅ Verified 2026-08-13:**

`[B32 · L391–401]`

**Returns (April 2026 data, advisory dated 2026-05-08):**

| | Daily Average | High | Low | Total |
|---|---:|---:|---:|---:|
| **Oceangoing transits** | **38.70** | 42 | 31 | 1,161 |
| Arrivals | 40.5 | 54 | 29 | — |

By class: 6.37 (<91′ beam) · 22.07 (91-107′) · 10.27 (Neopanamax). Booking slots 317 available / 273 used (86.12%).

⚠️ **Read TRANSITS (38.70), not ARRIVALS (40.5).** They sit adjacent in the same block and my threshold is on transits.
✅ **This also anchors the "~36 normal" in my threshold table, which had no provenance.** April 2026 actual = **38.70/day**.

### ✅ GATUN LAKE ELEVATION — GAP CLOSED 2026-08-27, and I had declared it unreachable

`[B33 · L410–416]`

**Live read: 83.80 ft (2026-08-26)**; 83.86 (8/24) → 83.84 (8/25) → 83.80 (8/26). Series opens 1965-01-01 at 86.49 ft. **Consistent with the sole prior anchor** (85.02 ft, A-27-2024, 2024-08-09) — **1.22 ft below it** — and inside the 82–87 ft normal operating range.

🔴 **HOW I GOT THIS WRONG FOR SIX DAYS — the lesson is bigger than the source (L-35).** On 8/21 I wrote *"NOT PUBLISHED ANYWHERE I can reach"*, declared the gap, refused to substitute a secondary (correct), and filed it in `SCRATCH.md` under **"WHAT IS AND IS NOT MEASURABLE — settled, do not re-hunt."** **The Tableau dashboard was blocked; the DATA never was**, and a plain CSV sits on ACP's own site navigation. **A negative finding written with the confidence of a positive one suppresses the retry that would overturn it.**
⇒ **Rule: a declared data gap must name what was tried AND carry a retry path. Never write "do not re-hunt." Distinguish RENDERING failure from PUBLICATION absence — a broken chart is evidence about the chart.**

⚠️ **TWO ACP PRIMARIES DISAGREE — unreconciled, and this is live.** ACP also publishes a forward **projection** CSV tying lake level to draft steps, and its modelled step dates (**~9/12, ~10/9**) **do not match Advisory A-29-2026's official dates (9/02, 10/01)**. **Cite the ADVISORY for dates.** The projection is a planning artifact, not the schedule.
🔑 **A lake-elevation band is NOT yet registered — deliberately.** Base-rate it against the 61-year series **before** setting levels; the 2023-24 drought is in that series and is the analogue to beat. *(`finding_base_rate_the_threshold_before_building_it` — the same discipline that deferred the slot-utilisation band.)*

### ⬇️ SUPERSEDED — the 8/21 "UNRESOLVED" entry, kept because the failure is the lesson (opened 2026-08-21, Will-prompted)

`[B34 · L422–429]`

**My Panama band measures TRANSITS. Will asked about WATER HEIGHT. I have no lake-level data at all**, and the transit instrument is **structurally blind** to a draft-only restriction — **ACP states plainly: *"The draft adjustment will not affect the number of daily vessel transits."*** The issuer is deliberately holding constant the exact variable my threshold reads.

**ACP's own primary is `apps.pancanal.com/t/TI/views/GatunH2OIndicators/GatunWaterLevel` ("Official Gatun Water Level"). It is DOUBLY BLOCKED:**
1. **Broken TLS certificate chain** — strict fetch returns **HTTP 000**; `curl -k` returns 200. *(A cert failure, not a 404 — do not read the 000 as "page gone.")*
2. **JS-rendered Tableau shell** — the 200 body is **5,186 B containing no elevation figure**; `Tableau`/`vizql` markers only.

⚠️ **NO SECONDARY SUBSTITUTED, deliberately.** Reference points for whoever closes this: Gatun normal operating range is roughly **82–87 ft PLD**; ACP measures via telemetry buoys at 4 lake locations every 15 min and the data reportedly reach an **AQUARIUS web portal** — **that portal is the lead to chase, unverified by me.**
🔑 **When it is instrumented, add a LAKE-ELEVATION row to the CLAUDE.md threshold table.** The Panama band should key on the driver, not only on transits.

### ✅ PANAMA — VERIFIED URLs AND THE PATTERN (2026-08-21)

`[B35 · L433–433]`

**All returned HTTP 200 this session. Use `curl -sLk` with a browser UA** (the `-k` matters on some ACP hosts) **then pdfminer.** PDFs carry a no-extract metadata flag; pdfminer warns and proceeds.

`[B36 · L435–448]`

| Advisory | Content | URL tail (prefix `https://pancanal.com/wp-content/uploads/`) |
|---|---|---|
| **A-29-2026** | 🔴 **Slot cap + draft postponement** (8/20) | `2026/08/ADV-29-2026-Additional-Measures-to-Address-Reduced-Precipitation-in-the-Canal-Watershed.pdf` |
| **A-33-2026** | 🔴 **POSTPONES the 10/01 47.5 ft step; 48.0 ft stays until further notice** (9/4) — ⚠️ PDF metadata title reads *May 4 2007*; the body is dated Sep 4 2026 | `2026/09/ADV-33-2026-Postponement-of-Maximum-Authorized-Draft-Adjustment-in-the-Neopanamax-Locks.pdf` *(re-executed 9/11, HTTP 200, 287,337 B)* |
| **A-34-2026** | Monthly Ops Summary **Aug 2026** — transits 33.19/day (9/10) | `2026/09/adv-34-2026-monthly-canal-operations-summary-august-2026.pdf` *(lower-case filename — ACP's; re-executed 9/11)* |
| A-22-2026 | Draft adjustment (7/01) | `2026/04/ADV-22-2026-Draft-adjustment-in-the-Neopanamax-Locks.pdf` |
| A-09 / A-14 / A-19 / A-23 / A-26 -2026 | Monthly Ops Summary Mar–Jul 2026 | `2026/04/…March-2026.pdf` · `2026/04/…April-2026-.pdf` · `2026/06/…May-2026.pdf` · `2026/07/…June-2026.pdf` · `2026/08/…July-2026.pdf` |
| A-01-2026 · A-30-2025 · A-04-2025 · A-01-2025 · A-38-2024 · A-21-2024 | Monthly Ops Summary, archive back to Jun-2024 | *(all reachable; discover by search)* |

🔴 **THERE IS NO USABLE PATH PATTERN — MEASURED, NOT ASSUMED. Do not try to construct a URL.**
> I wrote here that `/uploads/YYYY/MM/` tracks the publication month (data month +1). **Measured against all 33 observed URLs it holds 17 of 33 — a coin flip.** And the failure is not random: **15 of the 16 misses collapse into a single `/uploads/YYYY/01/` catch-all** (Sep-2025 lives at `/uploads/2025/01/`, Jun-2024 at `/uploads/2024/01/`). **It holds 16 of 19 from Jul-2024 on and fails 15 of 21 across Nov-2023 → Sep-2025 — i.e. it fails hardest exactly across the 2023-24 drought window, which is the window anyone will most want.** I handed this heuristic to a worker *to speed up that very range.*
> **Filenames are equally unpredictable:** `ADV49-2023` · `ADV02-2024` · `ADV-18-2024` · `ADV-04-2025` · `ADV-14-2026-…-April-2026-.pdf` (trailing dash) · `…-Feburary-2025.pdf` (ACP's typo) · `ADV07-2024-MONTHLY-FEB.pdf.pdf` (doubled extension).
> ✅ **USE THE COMPLETE ARCHIVE INDEX INSTEAD** (below) — it is a lookup, not a guess. **A per-month URL table is in `water/PANAMA_SERIES.md` §10.**
⚠️ **DISCOVER BY SEARCH, NEVER CONSTRUCT.** Every URL I built by pattern 404'd. The pattern is for *recognising* a URL, not generating one.

### ⚠️ CORRECTED 2026-08-21 — MY "THREE THINGS IT DOES NOT CONTAIN" WAS WRONG AT CORPUS SCALE

`[B37 · L452–457]`

> 🔴 **I checked TWO issues, found no tonnage / draft / Gatun elevation, and wrote a negative about the DOCUMENT CLASS. The worker checked THIRTY-THREE and found all three DO appear — never in the statistics table, always in discretionary appendix prose.**
> 🔑 **The generalisation, which is the useful part: the statistics table is FIXED-SCHEMA and genuinely contains none of the three. The appendix is DISCRETIONARY. A schema check of the table is not a check of the document** — so a negative that is true of every table is still false of the corpus. **Scope a negative to what you actually scanned.** *(Third wrong-referent instance of the day on this desk, and the one with the widest blast radius: it would have stopped anyone from ever looking again.)*

**WHAT IS ACTUALLY TRUE:**
- **In the STATISTICS TABLE: no tonnage, no draft, no Gatun elevation, in any of 33 issues.** That part stands and is now n=33, not n=2.
- **In APPENDIX PROSE:** ✅ **maximum authorised draft appears repeatedly** — this is where the 2023-24 trough of **44.0 ft** is recorded (A-53-2023, A-04-2024). ✅ **ONE Gatun elevation exists in the whole corpus** (below). ✅ tonnage appears twice as a **fiscal aggregate**, never monthly.

### 🔑 GATUN LAKE ELEVATION — one primary figure exists, and it anchors the unit and datum

`[B38 · L461–465]`

**A-27-2024** (July-2024 issue, advisory dated **2024-08-09**), verbatim:
> *"The rainy season is gradually bringing the reservoirs to its optimum levels: **Gatun Lake today is at 85.02 feet (25.91 m)**, while **Alhajuela Lake is at 217.24 feet (66.21 m)**."*

**The only numeric Gatun elevation in 33 readable issues.** ⚠️ **It is a single 2024 spot reading — NOT a series, NOT current, and NOT a substitute for the live instrument.** Its value is that it **confirms the unit (feet) and the datum**, and 85.02 ft sits inside the 82–87 ft operating range this file carries. **The 2026 lake state remains UNINSTRUMENTED.**
**Lead, unverified and not chased:** four issues (Oct/Nov/Dec-2023, Apr-2024) close with a link list including *"Daily average level of Gatun Reservoir for the last 12 months."* **That link is the most promising route to a real series.**

### ✅ THE COMPLETE ADVISORY ARCHIVE — a WORKING path beside the known-bad one

`[B39 · L469–470]`

⚠️ **The known-bad entry below is still correct and still stands: `pancanal.com/en/advisories-to-shipping/` (PLURAL) is JS-rendered and silently truncates at `A-46-2024`.**
✅ **But a near-identical sibling URL — `advisory-to-shipping` (SINGULAR) — returns the COMPLETE archive, server-rendered:**

`[B40 · L474–475]`

**762,407 bytes · 1,005 PDF anchors · `a-01-2002` → current.** Each anchor carries the advisory number AND the data month in its link text, so month → URL is a lookup, not a guess.
🔑 **Validated before use: it reproduced all 7 independently-verified URLs.** ⚠️ **Two URLs differing by one character, one useless and one complete — a known-bad entry condemns a STRING, not a capability. When you mark a source bad, try its siblings before concluding the publisher does not serve the data.**

### 🔴 STILL-TRUE NEGATIVES (now n=33, scoped to the statistics table)

`[B41 · L479–483]`

Verified across **thirty-three** advisories: **the fixed-schema statistics table contains no tonnage, no draft and no Gatun elevation.**
- ❌ **TONNAGE** — no tons, no PC/UMS, nothing. A capacity series must be *derived* (transits × authorised draft), not read.
- ❌ **DRAFT** — lives only in the draft-adjustment advisories, never in the monthly.
- ❌ **GATUN ELEVATION** — the one "Gatun" hit in a monthly is a **lock-maintenance schedule**. A-29 says decisions are *"based on the current level of Gatun Lake"* and **prints no number.**
🔑 **ACP publishes watershed INPUTS, not the reservoir STOCK** — A-29 gives rainfall **−34%** and inflows **−44%** (May–Aug). Input deficit ≠ level.

### ✅ THE COLUMN THAT REPLACES THE UNPUBLISHABLE AUCTION PRICE

`[B42 · L487–497]`

⛔ **ACP does NOT publish auction clearing prices** — confirmed at `pancanal.com/en/maritime-services/auction-system/`, which links only to the platform, a user guide and a FAQ. **The $3.78M / $4M figures circulating are broker relays through trade press: unverifiable and unreproducible, so they may inform but must never gate** (`finding_loadbearing_number_must_be_reproducible`).

✅ **But the Monthly Ops Summary publishes `Auctioned booking slots` — Available / Used / Percentage — as its own line**, monthly and archived back years. Primary, reproducible, and it moves when transits do not:

| | Transits/day | **Auctioned slots used** |
|---|---:|---:|
| Jun-2024 | 29.1 | **55.56%** (315 / 175) |
| Sep-2025 | 33.1 | **95.34% as PRINTED** (354 / 348 → 98.31% computed) ⚠️ |
| Apr-2026 | 38.70 | **86.12%** (317 / 273) |

⚠️ **Record `Used` even when it exceeds `Available`** — Apr-2026 shows 105.65 / 111.02 / 114.53 on the non-auction classes because the footnote excludes *additional* auctioned slots. **Print both as given; never normalise.**

#### 🔴 DO NOT SCRAPE THE ADVISORIES INDEX — it is silently stale

`[B43 · L502–506]`

`https://pancanal.com/en/advisories-to-shipping/` is **JS-rendered**. **Both `curl` and `WebFetch` return a server-rendered fragment ending at `A-46-2024`** — while `A-14-2026` demonstrably exists at HTTP 200. **The list renders as complete, so its incompleteness is invisible.**

⚠️ **Two fetch tools agreeing is NOT corroboration here** — they share the same blind spot (neither executes JS). **An absence claim from that index is a claim about the index, not about ACP.** *(This produced a wrong published finding on 2026-08-13 — see L-24, KB-067.)*

**Retrieval that works:** direct PDF URL, or a web search for `"Monthly Canal Operations Summary" pancanal <month> 2026`. **Filenames are NOT predictable** — the advisory number does not increment monthly and the trailing-dash convention varies, so brute-forcing the filename fails. **Discover, then fetch.**

#### AEO-04 resolution — spec tightened

`[B44 · L509–509]`

**AEO-04 resolves on a binding transit/draft RESTRICTION, not a scheduled draft step-down.** Two places a restriction would appear: **(a)** its own numbered Advisory to Shipping, **(b)** the monthly summary's transit figures falling into my bands (**≤32 Yellow · ≤27 Orange · ≤22 Red**, vs the now-anchored ~38.7 baseline). **Check (b) monthly — it is retrievable; (a) needs discovery because the index cannot be trusted.**

### ⚠️ ACP'S OWN ARITHMETIC DISAGREES WITH ITSELF IN THREE MONTHS — report AS PRINTED, never silently recompute

`[B45 · L525–531]`

| Month | ACP prints | Used ÷ Available | Implied denominator |
|---|---|---|---|
| **Sep-2025** (A-30-2025) | **95.34%** | 348/354 = **98.31%** | ≈365 |
| **Aug-2025** (A-26-2025) | **96.18%** | 382/395 = **96.71%** | ≈397 |
| **May-2025** (A-18-2025) | Total **973** | classes sum to **974** | off by 1 transit |

🔴 **I was carrying 98.31% for Sep-2025 — that is MY recomputation, not ACP's printed figure**, and it reached a packet and this file before the worker caught it. **The 354/348 pair is exactly right; the percentage was derived rather than read.** ⚠️ **Store the two LEVELS (`available`, `used`), not the ratio** — utilisation is derivable from levels and the reverse is not, and recomputing silently replaces the publisher's number with your own.
