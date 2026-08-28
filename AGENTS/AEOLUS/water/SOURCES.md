# AEOLUS · WATER — verified primary sources

**Every command below was RUN and returned the stated value on 2026-08-13.** No reconstructed URLs.
**Re-verify a failing command rather than substituting a secondary** (L-15). A 403 or an empty return is a fact about *one method*, not proof the primary is unreachable.

---

## 1. DROUGHT — the shared upstream input (C2 · C4 · C5 · C6)

> 🔑 **This section is the canonical home for drought.** It previously sat in `../wildfire/SOURCES.md`, which made it invisible to the other three channels that depend on it.

### US Drought Monitor — statistics API ✅ verified 8/13
```bash
curl -s -H "Accept: application/json" \
 "https://usdmdataservices.unl.edu/api/USStatistics/GetDroughtSeverityStatisticsByAreaPercent?aoi=us&startdate=7/28/2026&enddate=8/11/2026&statisticsType=1"
```
**Verified CONUS (valid 8/11):** `none 26.38 · d0 73.62 · d1 50.38 · d2 29.50 · d3 10.27 · d4 1.04`
⚠️ **Returns rows for `CONUS` *and* `Total` (US + PR) — read the `areaOfInterest` field.** They differ by ~8 pp and are trivially confused.
⚠️ **The human-facing `droughtmonitor.unl.edu` pages return *"the tabular data did not load"* to a fetch tool.** The web page failing is **not** the data being unavailable — use the API.
**Cadence:** valid Tuesday 8 a.m. ET, **released Thursday.** New map ≈ every Thursday morning.

### State/county granularity — same API, swap `aoi`
`aoi=CO` (state postal) or a county FIPS. **Use this before claiming a drought signal reaches a specific crop belt or fire geography** — the 8/13 C2-vs-C4 discrimination turned entirely on *where* the deterioration was (OK/TX Panhandle, not the corn belt).

### Palmer Drought Severity Index (CPC)
`https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/cdus/palmer_drought/`
Longer-memory index than USDM. **Better for multi-season persistence; worse for current conditions.**

### Soil moisture (CPC monitoring)
`https://www.cpc.ncep.noaa.gov/products/Soilmst_Monitoring/` — the direct **crop-yield** link; leads USDM at the agricultural margin.

---

## 2. SNOWPACK — sets the following year's allocation

**NRCS SNOTEL / National Water and Climate Center** ✅ page reachable 8/13 (225 KB)
`https://www.nrcs.usda.gov/resources/data-and-reports/sno-tel-and-snow-course-data-and-products`
Interactive basin reports: `https://nwcc-apps.sc.egov.usda.gov/imap`

**Read Apr-1 basin % of median as the allocation-setting figure.**
⚠️ **Seasonal — near-zero Jun–Sep.** In August this is *correctly* empty; do not log it as a gap.
🔑 **The basin that matters for Powell is the UPPER Colorado** — and it sits near the ENSO dipole pivot where the signal is weak. See `DOSSIER.md` § "El Niño does not refill the Colorado."

---

## 3. STREAMFLOW — USGS NWIS ✅ verified 8/13

```bash
curl -s "https://waterservices.usgs.gov/nwis/dv/?format=json&sites=09380000&parameterCd=00060&startDT=2026-08-01&endDT=2026-08-12" \
 | python3 -c "
import json,sys
t=json.load(sys.stdin)['value']['timeSeries'][0]
print(t['sourceInfo']['siteName'])
for v in t['values'][0]['value'][-5:]: print(' ', v['dateTime'][:10], v['value'], 'cfs')
"
```
**Verified: `COLORADO RIVER AT LEES FERRY, AZ` — 7,930 cfs on 2026-08-12.**

🔑 **Lees Ferry (`09380000`) is the single most informative gauge in this folder.** It is the **Upper/Lower Basin compact division point**, and because it sits just below Glen Canyon Dam **it measures Glen Canyon's releases directly** — i.e. **the water that refills Lake Mead.** It converts the Powell↔Mead coupling from an inference into a measurement.

**Key params:** `00060` discharge (cfs) · `00065` gauge height · `72019` groundwater depth.
**Other useful sites:** `07289000` Mississippi at Vicksburg · `05331000` Mississippi at St. Paul · `09521000` Colorado at Yuma.
**Site search:** `https://waterdata.usgs.gov/nwis`

---

## 4. RESERVOIRS — USBR (the issuing agency)

### Powell (919) and Mead (921) — daily pool elevation ✅ verified 8/13
```bash
curl -s "https://www.usbr.gov/uc/water/hydrodata/reservoir_data/919/csv/49.csv" | tail -5   # Powell
curl -s "https://www.usbr.gov/uc/water/hydrodata/reservoir_data/921/csv/49.csv" | tail -5   # Mead
```
**Verified:** Powell `2026-08-12,3520.37` · Mead `2026-08-12,1039.82`. Datatype `49` = elevation (ft), `17` = storage (af).
⚠️ **The files are long and chronological — you MUST `tail`.** A page-summarizing fetch truncates a 22k-row file and returns **1976 data with a clean HTTP 200**.

### Seasonal base rate — REQUIRED before extrapolating any rate (L-16)
```bash
python3 - <<'EOF'
import csv,urllib.request
for name,sid in [("POWELL",919),("MEAD",921)]:
    u=f"https://www.usbr.gov/uc/water/hydrodata/reservoir_data/{sid}/csv/49.csv"
    d={r['datetime']:float(r['pool elevation'])
       for r in csv.DictReader(urllib.request.urlopen(u).read().decode().splitlines())
       if r['pool elevation']}
    print(name, "current:", d.get('2026-08-12'))
    for y in range(2021,2026):
        a,b=d.get(f'{y}-08-12'),d.get(f'{y}-09-30')
        if a and b: print(f"   {y}: Aug12 {a:.2f} -> Sep30 {b:.2f}  ({b-a:+.2f})")
EOF
```
⚠️ **A base rate is only valid while the mechanism generating it still holds.** Mead's Aug→Sep *rise* is driven by Glen Canyon releases — and **2026 releases are at a 9-year low** (§3). **Check Lees Ferry before trusting Mead's seasonal pattern.**

### 🔴 24-MONTH STUDY — registered 2026-08-27 as the PRIMARY C6 instrument (it was NOT in this file before)

**This is the forward-looking instrument. The daily elevations above are the backward-looking one.** It is what moved AEO-10 and it prints monthly.

```bash
# The UC index lists every month. VERIFIED 2026-08-27.
curl -sL "https://www.usbr.gov/uc/water/crsp/studies/index.html" | grep -oiE 'href="[^"]*24Month[^"]*"'
# Current-month Lower Colorado copy (Mead + Powell in one file):
curl -sL "https://www.usbr.gov/lc/region/g4000/24mo.pdf" -o 24mo.pdf
```
⚠️ **AUGUST 2026 IS SPLIT INTO TWO FILES AND EVERY OTHER MONTH IS ONE.** `24Month_08_6.pdf` (6 maf Powell release) and `24Month_08_7.pdf` (7 maf) — **scenarios keyed to the WY2027 release decision.** A scraper expecting one file per month silently misses a branch. *(Mead's path is identical in both through Apr-2027; they diverge from May-2027.)*
⚠️ **`.../lc/region/g4000/24mo.pdf` served the JULY study on 2026-08-27, six days after the August one published.** **Check the document's own title line — never trust "current" in a URL.**

**HOW TO READ IT — this is where I went wrong.** The elevation tables extract as a bare column of numbers with no month labels.
1. **Anchor on a known ACTUAL** (e.g. Mead 2025-12-31 = 1062.24) and count outward; values are **end-of-month**.
2. **VERIFY the mapping** against the daily CSV for ≥6 consecutive months before trusting any projected cell. *(I verified 12 months to the cent.)*
3. 🔴 **READ THE PATH, NOT THE ENDPOINT.** A criterion saying *"at any point through 12/31"* is graded on the projected **MINIMUM over the window**. **Grading AEO-10 on the 31-December value overstated its buffer 2.4× for two weeks** (0.86 ft real vs 2.1 ft claimed) — **L-36**.
4. The narrative pages carry the **release decision, the runoff forecast as % of average, and the operating tier** — often more decision-relevant than the tables.

**Aug-2026 study, key figures (all verbatim/primary):** WY2026 Powell release cut **7.48 → 6.00 maf** · July unregulated inflow **9% of average** · **April–July 1.14 maf = 18% of average** · WY2026 forecast **37%** · *"Lake Powell's elevation is projected to decline below 3,510 feet during water year 2027"* · Mead **Dec-2026 projected 1,034.74 ft** (below the binding 1,035).

### Colorado Post-2026 Guidelines — the policy clock
`https://www.usbr.gov/ColoradoRiverBasin/` · DOI newsroom · **Federal Register** (search *"Colorado River"* + *"Record of Decision"*) → milestones in `../CALENDAR.md`.

⚠️ **ROD PATH — the one recorded earlier 404s.** ✅ Working, verified 2026-08-27:
`https://www.usbr.gov/ColoradoRiverBasin/post2026/decision-doc/P26_RecordofDecision_Final.pdf` (1.17 MB → 136,430 chars via pdfminer). Same directory: `2027-2028OperatingGuidelines_Final.pdf`, `FutureColoradoOperations_Factsheet.pdf`, `P26_BiologicalOpinion_Final.pdf`. ❌ **`/ColoradoRiverBasin/documents/post2026/…` returns 404 — do not reconstruct it.**
🔑 **The ROD adopts a PROCESS, not a numeric alternative.** Do not go looking for "the selected alternative" — that string does not appear. The binding numbers live in the **Operating Guidelines**, a separate PDF.

---

## 5. RIVER STAGE — navigation (C5)

### Rhine at Kaub (WSV/PEGELONLINE, German federal primary) ✅ verified 8/13
```bash
curl -s "https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations/KAUB/W/measurements.json?start=P3D" \
 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d[-1]); print('min',min(x['value'] for x in d),'max',max(x['value'] for x in d))"
```
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

⚠️ **`KOELN` is NOT a valid shortname in the API** — do not use it. List stations with:
```bash
curl -s "https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations.json?waters=RHEIN" | python3 -c "import json,sys;[print(s['shortname'], s.get('km')) for s in json.load(sys.stdin)]"
```
### 🔴 WSV FORECAST endpoint — registered 2026-08-13 (found by the water worker, verified by AEOLUS)
```bash
curl -s "https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations/KAUB/WV/measurements.json" \
 | python3 -c "import json,sys;[print(x['timestamp'][:16],x['value']) for x in json.load(sys.stdin) if x.get('type')=='forecast']"
```
**Available at `KAUB`, `DUISBURG-RUHRORT`, `EMMERICH` only — HTTP 404 at Maxau, Worms, Mainz** (verified).
⚠️ **NOT listed in the station's `timeseries` array** (which shows only `Q` and `W`) — **undiscoverable from metadata; found by direct probe.**
⚠️ **HORIZON IS SHORT AND THE WORKER'S REPORT OVERSTATED IT.** My verification pull returned **25 forecast points spanning 8/13→8/15 only (~2 days)**. The run report quoted **8/17** values and a *"Kaub rebounds to 11"* shape; **those are NOT reproducible in my pull, which shows Kaub falling monotonically to 7.0 cm on 8/15 with no rebound in range.** **Adopt the endpoint; do NOT adopt the 8/17 figures.** Re-pull and state the actual horizon each time.

### DISCHARGE `Q` — datum-independent, available at all six
`/stations/<ST>/Q/measurements.json` — m³/s, 15-min. Kaub ~492 m³/s (8/13). **Prefer discharge for cross-era comparison**, since stage depends on a `gaugeZero` that has been re-referenced at some stations.

⚠️ **PROVENANCE GAP on the carried "40 cm uneconomical" line.** That figure has **no source recorded in this file** — it is carried, not verified. The authority's own navigation references are **`GlW` (Kaub 77 cm)** and **`TuGLW` (190 cm)**. **The 40 cm line is retained as an unprovenanced working figure and is explicitly NOT the basis of any trigger.**

⚠️ **No verified source for barge FREIGHT rates.** The ~€150/t figures in my dossier are trade-press relays (PJK/Bloomberg via gCaptain/Insurance Journal), **not a primary I can re-pull.** Finding a resolvable freight series is an open gap.
**Benchmarks:** 2018 all-time low **25 cm** (October) · **≤40 cm** = uneconomical navigation.

### ✅ YANGTZE — gap closed 2026-08-13 (Changjiang Water Resources Commission, the issuing agency)
```bash
curl -sL "http://www.cjh.com.cn/sqindex.html" \
 | python3 -c "
import re,sys,json,datetime
s=sys.stdin.read()
d=json.loads(re.search(r'var sssq = (\[.*?\]);', s, re.S).group(1))
for x in d: print(x['stnm'], x.get('z'), 'm', x.get('q') or x.get('oq') or '-', 'm3/s')
"
```
⚠️ **The page embeds a clean JSON array (`var sssq = [...]`) — parse that, do not scrape the HTML table.** 14 stations, `z` = level (m), `q` = discharge (m³/s), `tm` = epoch ms.
**Verified 2026-08-13 16:00 UTC:** **Yichang 宜昌 44.43 m / 17,800 m³/s** · **Hankou 汉口 (Wuhan) 20.61 m / 27,600** · **Datong 大通 10.06 m / 31,100** · Shashi 沙市 34.90 · Jiujiang 九江 14.51 · **Three Gorges Reservoir 三峡水库 157.30 m** (outflow 14,900).
**Navigation-relevant stations: Yichang (below Three Gorges), Hankou (Wuhan industrial reach), Datong (the standard downstream gauge).**
⚠️ `www.cjw.gov.cn` does **not** resolve; **`cjh.com.cn` is the working host.** ⚠️ Page is GB/UTF-8 mixed — decode defensively.

### ✅ DANUBE — gap closed 2026-08-13 (OVF, Hungarian national water directorate)
```bash
curl -sL "https://www.vizugy.hu/index.php?mapModule=OpVizallas&mapData=VizmerceLista"
```
**Verified 2026-08-13 (18:00 local):** **Budapest 24 cm** · **Baja −4 cm** · **Mohács 10 cm** · Adony −73 cm (Danube km 1598.110).
⚠️ **Values are cm against each station's own local datum — negative is normal, not "below empty."** Same trap as the Rhine.
✅ **SUB-GAP CLOSED 8/13 — the LKV reference is a queryable ArcGIS service, and it ships the authority's own above/below flag.**
```bash
curl -s "https://terkeptar.vizugy.hu/server/rest/services/Vizugy_hu/LKV_folyok/MapServer/0/query?where=VizfolyasNev%3D%27Duna%27&outFields=Nev,Fkm,Vizallas,LKV,LKVIdopont,LKV_viszony&returnGeometry=false&f=json"
```
Returns **44 Danube stations from Ingolstadt (km 2457, Germany) to Novo Selo (km 834)** — far beyond the Hungarian reach. Fields: `Vizallas` current cm · **`LKV` lowest-ever cm** · `LKVIdopont` the date it was set · `LNV` highest-ever · `Nullpont` gauge-zero elevation · **`LKV_viszony`** = the authority's own −1/+1 below/above-LKV flag.
⚠️ **EXCLUDE LKV dates of 1799-12-31 / 1884-12-31 / 1894-12-31 — they are null-date sentinels, not real records** (5 of 44 stations). Filter on the year before using an LKV.
⚠️ Danube is **multi-national**; Hungary is one reach. Austria `ehyd.gv.at` (200) and Serbia `hidmet.gov.rs` (200) both respond and are unexplored.

### ✅ PARANÁ — gap closed 2026-08-13 (UNL-FICH, Facultad de Ingeniería y Ciencias Hídricas)
```bash
curl -sL "https://fich.unl.edu.ar/cim/rios/parana/alturas"
```
Whole-basin table: `station | river | current (m) | Δ | previous | ALERT level | EVACUATION level`. **The alert/evacuation columns are published thresholds — this source ships its own reference levels**, unlike the Danube one.
**Verified 2026-08-13:** **Rosario 3.02 m** (Δ −0.01; alert 5.00) · **Santa Fe 3.18** (−0.02; alert 5.30) · Corrientes 3.28 (−0.08; alert 6.50) · Villa Constitución 2.47 · Diamante 3.36 · Barranqueras 3.29.
🔑 **Rosario is the one that matters** — the Up-River port cluster around Rosario handles the large majority of Argentine grain and soy-product exports, so Paraná stage there is a **grain-logistics cost** variable (→ **CARL**, **MARCO**).
✅ **SUB-GAP CLOSED 8/13 — derive the low-water reference from the station's own history rather than looking for a published one.**
```bash
curl -sL "https://fich.unl.edu.ar/cim/rios/historico/39"     # 39 = Rosario; 366 daily records
```
Returns `date | time | level | Δ | — | previous`. **Trailing-year distribution at Rosario (13/08/2025 → 13/08/2026):** min **1.08** · P05 **1.34** · P10 **1.40** · P25 **1.60** · median **2.14** · P75 **2.44** · max **3.03**.
**Use P10 ≈ 1.40 m as the working low-water reference** until a navigation-draft reference is found.
⚠️ **One year is a SHORT base.** The 2021 crisis went far lower — reporting has Rosario near **0.08 m** in May 2020 and 2021 as the lowest since **1944**, with basin discharge ~6,200 m³/s against a ~17,000 normal and a 1944 record of ~5,800. **A trailing-year percentile is a rank within a benign year, not a historic reference.**
🔴 **CORRECTION to my own read from earlier today: 3.02 m is NOT "mid-range" — it is the 99th percentile of the trailing year** (max 3.03, median 2.14). **The Paraná is near the TOP of its recent range, not the middle.** I characterised it as mid-range before pulling the distribution; **the distribution is what made the read possible, and it reversed the adjective.** **This channel is not firing, and it is not close to firing.**

### ✅ MISSISSIPPI — INSTRUMENT GAP CLOSED 2026-08-27 (NOAA NWPS API — the issuing agency)

🔴 **This band stood with NO METRIC SURFACE AT ALL — a registered threshold under a standing Will directive, graded on an aggregator's word "~normal".** Closed with **~3 weeks to spare** before the Sep–Nov low-water window.

```bash
# Memphis — live stage + the published low-water reference. VERIFIED 2026-08-27 (HTTP 200).
curl -s "https://api.water.noaa.gov/nwps/v1/gauges/MEMT1" | python3 -c "
import json,sys; d=json.load(sys.stdin)
print(d['name'], d['status']['observed']['primary'], d['status']['observed']['primaryUnit'], d['status']['observed']['validTime'])
print('lowThreshold:', d['lowThreshold'])
for r in d['flood']['lowWaters']['historic'][:6]: print(' ', r['occurredTime'][:10], r['stage'], r.get('statement',''))
"
```
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

### 🔴 Panama — INSTRUMENT GAP CLOSED 2026-08-13

**The instrument is the ACP *Monthly Canal Operations Summary*, published as a numbered Advisory to Shipping.** It carries **oceangoing transits, daily average** — exactly the quantity my threshold bands use.

**✅ Verified 2026-08-13:**
```bash
curl -sL -A "Mozilla/5.0 (research)" \
 "https://pancanal.com/wp-content/uploads/2026/04/ADV-14-2026-Monthly-Canal-Operations-Summary-April-2026-.pdf" -o adv.pdf
python3 -c "from pdfminer.high_level import extract_text; print(' '.join(extract_text('adv.pdf').split()))"
```
**Returns (April 2026 data, advisory dated 2026-05-08):**

| | Daily Average | High | Low | Total |
|---|---:|---:|---:|---:|
| **Oceangoing transits** | **38.70** | 42 | 31 | 1,161 |
| Arrivals | 40.5 | 54 | 29 | — |

By class: 6.37 (<91′ beam) · 22.07 (91-107′) · 10.27 (Neopanamax). Booking slots 317 available / 273 used (86.12%).

⚠️ **Read TRANSITS (38.70), not ARRIVALS (40.5).** They sit adjacent in the same block and my threshold is on transits.
✅ **This also anchors the "~36 normal" in my threshold table, which had no provenance.** April 2026 actual = **38.70/day**.

### ✅ GATUN LAKE ELEVATION — GAP CLOSED 2026-08-27, and I had declared it unreachable

```bash
# ACP's own daily series, 1965-01-01 → present. VERIFIED 2026-08-27 (HTTP 200, 405,357 B).
curl -s "https://evtms-rpts.pancanal.com/eng/h2o/Download_Gatun_Lake_Water_Level_History.csv" -o gatun.csv
head -1 gatun.csv; tail -3 gatun.csv     # header: DATE_LOG,GATUN_LAKE_LEVEL(FEET)
```
**Live read: 83.80 ft (2026-08-26)**; 83.86 (8/24) → 83.84 (8/25) → 83.80 (8/26). Series opens 1965-01-01 at 86.49 ft. **Consistent with the sole prior anchor** (85.02 ft, A-27-2024, 2024-08-09) — **1.22 ft below it** — and inside the 82–87 ft normal operating range.

🔴 **HOW I GOT THIS WRONG FOR SIX DAYS — the lesson is bigger than the source (L-35).** On 8/21 I wrote *"NOT PUBLISHED ANYWHERE I can reach"*, declared the gap, refused to substitute a secondary (correct), and filed it in `SCRATCH.md` under **"WHAT IS AND IS NOT MEASURABLE — settled, do not re-hunt."** **The Tableau dashboard was blocked; the DATA never was**, and a plain CSV sits on ACP's own site navigation. **A negative finding written with the confidence of a positive one suppresses the retry that would overturn it.**
⇒ **Rule: a declared data gap must name what was tried AND carry a retry path. Never write "do not re-hunt." Distinguish RENDERING failure from PUBLICATION absence — a broken chart is evidence about the chart.**

⚠️ **TWO ACP PRIMARIES DISAGREE — unreconciled, and this is live.** ACP also publishes a forward **projection** CSV tying lake level to draft steps, and its modelled step dates (**~9/12, ~10/9**) **do not match Advisory A-29-2026's official dates (9/02, 10/01)**. **Cite the ADVISORY for dates.** The projection is a planning artifact, not the schedule.
🔑 **A lake-elevation band is NOT yet registered — deliberately.** Base-rate it against the 61-year series **before** setting levels; the 2023-24 drought is in that series and is the analogue to beat. *(`finding_base_rate_the_threshold_before_building_it` — the same discipline that deferred the slot-utilisation band.)*

---

### ⬇️ SUPERSEDED — the 8/21 "UNRESOLVED" entry, kept because the failure is the lesson (opened 2026-08-21, Will-prompted)

**My Panama band measures TRANSITS. Will asked about WATER HEIGHT. I have no lake-level data at all**, and the transit instrument is **structurally blind** to a draft-only restriction — **ACP states plainly: *"The draft adjustment will not affect the number of daily vessel transits."*** The issuer is deliberately holding constant the exact variable my threshold reads.

**ACP's own primary is `apps.pancanal.com/t/TI/views/GatunH2OIndicators/GatunWaterLevel` ("Official Gatun Water Level"). It is DOUBLY BLOCKED:**
1. **Broken TLS certificate chain** — strict fetch returns **HTTP 000**; `curl -k` returns 200. *(A cert failure, not a 404 — do not read the 000 as "page gone.")*
2. **JS-rendered Tableau shell** — the 200 body is **5,186 B containing no elevation figure**; `Tableau`/`vizql` markers only.

⚠️ **NO SECONDARY SUBSTITUTED, deliberately.** Reference points for whoever closes this: Gatun normal operating range is roughly **82–87 ft PLD**; ACP measures via telemetry buoys at 4 lake locations every 15 min and the data reportedly reach an **AQUARIUS web portal** — **that portal is the lead to chase, unverified by me.**
🔑 **When it is instrumented, add a LAKE-ELEVATION row to the CLAUDE.md threshold table.** The Panama band should key on the driver, not only on transits.

### ✅ PANAMA — VERIFIED URLs AND THE PATTERN (2026-08-21)

**All returned HTTP 200 this session. Use `curl -sLk` with a browser UA** (the `-k` matters on some ACP hosts) **then pdfminer.** PDFs carry a no-extract metadata flag; pdfminer warns and proceeds.

| Advisory | Content | URL tail (prefix `https://pancanal.com/wp-content/uploads/`) |
|---|---|---|
| **A-29-2026** | 🔴 **Slot cap + draft postponement** (8/20) | `2026/08/ADV-29-2026-Additional-Measures-to-Address-Reduced-Precipitation-in-the-Canal-Watershed.pdf` |
| A-22-2026 | Draft adjustment (7/01) | `2026/04/ADV-22-2026-Draft-adjustment-in-the-Neopanamax-Locks.pdf` |
| A-09 / A-14 / A-19 / A-23 / A-26 -2026 | Monthly Ops Summary Mar–Jul 2026 | `2026/04/…March-2026.pdf` · `2026/04/…April-2026-.pdf` · `2026/06/…May-2026.pdf` · `2026/07/…June-2026.pdf` · `2026/08/…July-2026.pdf` |
| A-01-2026 · A-30-2025 · A-04-2025 · A-01-2025 · A-38-2024 · A-21-2024 | Monthly Ops Summary, archive back to Jun-2024 | *(all reachable; discover by search)* |

🔴 **THERE IS NO USABLE PATH PATTERN — MEASURED, NOT ASSUMED. Do not try to construct a URL.**
> I wrote here that `/uploads/YYYY/MM/` tracks the publication month (data month +1). **Measured against all 33 observed URLs it holds 17 of 33 — a coin flip.** And the failure is not random: **15 of the 16 misses collapse into a single `/uploads/YYYY/01/` catch-all** (Sep-2025 lives at `/uploads/2025/01/`, Jun-2024 at `/uploads/2024/01/`). **It holds 16 of 19 from Jul-2024 on and fails 15 of 21 across Nov-2023 → Sep-2025 — i.e. it fails hardest exactly across the 2023-24 drought window, which is the window anyone will most want.** I handed this heuristic to a worker *to speed up that very range.*
> **Filenames are equally unpredictable:** `ADV49-2023` · `ADV02-2024` · `ADV-18-2024` · `ADV-04-2025` · `ADV-14-2026-…-April-2026-.pdf` (trailing dash) · `…-Feburary-2025.pdf` (ACP's typo) · `ADV07-2024-MONTHLY-FEB.pdf.pdf` (doubled extension).
> ✅ **USE THE COMPLETE ARCHIVE INDEX INSTEAD** (below) — it is a lookup, not a guess. **A per-month URL table is in `water/PANAMA_SERIES.md` §10.**
⚠️ **DISCOVER BY SEARCH, NEVER CONSTRUCT.** Every URL I built by pattern 404'd. The pattern is for *recognising* a URL, not generating one.

### ⚠️ CORRECTED 2026-08-21 — MY "THREE THINGS IT DOES NOT CONTAIN" WAS WRONG AT CORPUS SCALE

> 🔴 **I checked TWO issues, found no tonnage / draft / Gatun elevation, and wrote a negative about the DOCUMENT CLASS. The worker checked THIRTY-THREE and found all three DO appear — never in the statistics table, always in discretionary appendix prose.**
> 🔑 **The generalisation, which is the useful part: the statistics table is FIXED-SCHEMA and genuinely contains none of the three. The appendix is DISCRETIONARY. A schema check of the table is not a check of the document** — so a negative that is true of every table is still false of the corpus. **Scope a negative to what you actually scanned.** *(Third wrong-referent instance of the day on this desk, and the one with the widest blast radius: it would have stopped anyone from ever looking again.)*

**WHAT IS ACTUALLY TRUE:**
- **In the STATISTICS TABLE: no tonnage, no draft, no Gatun elevation, in any of 33 issues.** That part stands and is now n=33, not n=2.
- **In APPENDIX PROSE:** ✅ **maximum authorised draft appears repeatedly** — this is where the 2023-24 trough of **44.0 ft** is recorded (A-53-2023, A-04-2024). ✅ **ONE Gatun elevation exists in the whole corpus** (below). ✅ tonnage appears twice as a **fiscal aggregate**, never monthly.

### 🔑 GATUN LAKE ELEVATION — one primary figure exists, and it anchors the unit and datum

**A-27-2024** (July-2024 issue, advisory dated **2024-08-09**), verbatim:
> *"The rainy season is gradually bringing the reservoirs to its optimum levels: **Gatun Lake today is at 85.02 feet (25.91 m)**, while **Alhajuela Lake is at 217.24 feet (66.21 m)**."*

**The only numeric Gatun elevation in 33 readable issues.** ⚠️ **It is a single 2024 spot reading — NOT a series, NOT current, and NOT a substitute for the live instrument.** Its value is that it **confirms the unit (feet) and the datum**, and 85.02 ft sits inside the 82–87 ft operating range this file carries. **The 2026 lake state remains UNINSTRUMENTED.**
**Lead, unverified and not chased:** four issues (Oct/Nov/Dec-2023, Apr-2024) close with a link list including *"Daily average level of Gatun Reservoir for the last 12 months."* **That link is the most promising route to a real series.**

### ✅ THE COMPLETE ADVISORY ARCHIVE — a WORKING path beside the known-bad one

⚠️ **The known-bad entry below is still correct and still stands: `pancanal.com/en/advisories-to-shipping/` (PLURAL) is JS-rendered and silently truncates at `A-46-2024`.**
✅ **But a near-identical sibling URL — `advisory-to-shipping` (SINGULAR) — returns the COMPLETE archive, server-rendered:**
```bash
curl -sLk -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" "https://pancanal.com/en/maritime-services/advisory-to-shipping/"
```
**762,407 bytes · 1,005 PDF anchors · `a-01-2002` → current.** Each anchor carries the advisory number AND the data month in its link text, so month → URL is a lookup, not a guess.
🔑 **Validated before use: it reproduced all 7 independently-verified URLs.** ⚠️ **Two URLs differing by one character, one useless and one complete — a known-bad entry condemns a STRING, not a capability. When you mark a source bad, try its siblings before concluding the publisher does not serve the data.**

### 🔴 STILL-TRUE NEGATIVES (now n=33, scoped to the statistics table)

Verified across **thirty-three** advisories: **the fixed-schema statistics table contains no tonnage, no draft and no Gatun elevation.**
- ❌ **TONNAGE** — no tons, no PC/UMS, nothing. A capacity series must be *derived* (transits × authorised draft), not read.
- ❌ **DRAFT** — lives only in the draft-adjustment advisories, never in the monthly.
- ❌ **GATUN ELEVATION** — the one "Gatun" hit in a monthly is a **lock-maintenance schedule**. A-29 says decisions are *"based on the current level of Gatun Lake"* and **prints no number.**
🔑 **ACP publishes watershed INPUTS, not the reservoir STOCK** — A-29 gives rainfall **−34%** and inflows **−44%** (May–Aug). Input deficit ≠ level.

### ✅ THE COLUMN THAT REPLACES THE UNPUBLISHABLE AUCTION PRICE

⛔ **ACP does NOT publish auction clearing prices** — confirmed at `pancanal.com/en/maritime-services/auction-system/`, which links only to the platform, a user guide and a FAQ. **The $3.78M / $4M figures circulating are broker relays through trade press: unverifiable and unreproducible, so they may inform but must never gate** (`finding_loadbearing_number_must_be_reproducible`).

✅ **But the Monthly Ops Summary publishes `Auctioned booking slots` — Available / Used / Percentage — as its own line**, monthly and archived back years. Primary, reproducible, and it moves when transits do not:

| | Transits/day | **Auctioned slots used** |
|---|---:|---:|
| Jun-2024 | 29.1 | **55.56%** (315 / 175) |
| Sep-2025 | 33.1 | **95.34% as PRINTED** (354 / 348 → 98.31% computed) ⚠️ |
| Apr-2026 | 38.70 | **86.12%** (317 / 273) |

⚠️ **Record `Used` even when it exceeds `Available`** — Apr-2026 shows 105.65 / 111.02 / 114.53 on the non-auction classes because the footnote excludes *additional* auctioned slots. **Print both as given; never normalise.**
⚠️ **NOT YET A BAND.** Three non-monotonic points is not a base rate.

#### 🔴 DO NOT SCRAPE THE ADVISORIES INDEX — it is silently stale

`https://pancanal.com/en/advisories-to-shipping/` is **JS-rendered**. **Both `curl` and `WebFetch` return a server-rendered fragment ending at `A-46-2024`** — while `A-14-2026` demonstrably exists at HTTP 200. **The list renders as complete, so its incompleteness is invisible.**

⚠️ **Two fetch tools agreeing is NOT corroboration here** — they share the same blind spot (neither executes JS). **An absence claim from that index is a claim about the index, not about ACP.** *(This produced a wrong published finding on 2026-08-13 — see L-24, KB-067.)*

**Retrieval that works:** direct PDF URL, or a web search for `"Monthly Canal Operations Summary" pancanal <month> 2026`. **Filenames are NOT predictable** — the advisory number does not increment monthly and the trailing-dash convention varies, so brute-forcing the filename fails. **Discover, then fetch.**

#### AEO-04 resolution — spec tightened
**AEO-04 resolves on a binding transit/draft RESTRICTION, not a scheduled draft step-down.** Two places a restriction would appear: **(a)** its own numbered Advisory to Shipping, **(b)** the monthly summary's transit figures falling into my bands (**≤32 Yellow · ≤27 Orange · ≤22 Red**, vs the now-anchored ~38.7 baseline). **Check (b) monthly — it is retrievable; (a) needs discovery because the index cannot be trusted.**

---

## KNOWN-BAD / DO-NOT-USE

| Source | Why |
|---|---|
| `lakepowellwaterlevel.com`, `lakebrief.com` and similar | **Disagreed with USBR by 3.83 ft on 8/12 and inverted the trend sign.** Cost a published wrong conclusion. |
| Any **percent-full** figure | Different capacity bases across sources (19% vs 23.1%, same lake, same week). **Cite elevation.** |
| Page-summarizing fetch of USBR CSVs | Truncates and returns **1976 data with HTTP 200**. Use `curl … \| tail`. |
| `droughtmonitor.unl.edu` HTML tables | Returns a load error to fetch tools. **Use the statistics API.** |


### ⚠️ ACP'S OWN ARITHMETIC DISAGREES WITH ITSELF IN THREE MONTHS — report AS PRINTED, never silently recompute

| Month | ACP prints | Used ÷ Available | Implied denominator |
|---|---|---|---|
| **Sep-2025** (A-30-2025) | **95.34%** | 348/354 = **98.31%** | ≈365 |
| **Aug-2025** (A-26-2025) | **96.18%** | 382/395 = **96.71%** | ≈397 |
| **May-2025** (A-18-2025) | Total **973** | classes sum to **974** | off by 1 transit |

🔴 **I was carrying 98.31% for Sep-2025 — that is MY recomputation, not ACP's printed figure**, and it reached a packet and this file before the worker caught it. **The 354/348 pair is exactly right; the percentage was derived rather than read.** ⚠️ **Store the two LEVELS (`available`, `used`), not the ratio** — utilisation is derivable from levels and the reverse is not, and recomputing silently replaces the publisher's number with your own.
