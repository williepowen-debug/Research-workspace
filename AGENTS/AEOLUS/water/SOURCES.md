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

### Colorado Post-2026 Guidelines — the policy clock
`https://www.usbr.gov/ColoradoRiverBasin/` · DOI newsroom · **Federal Register** (search *"Colorado River"* + *"Record of Decision"*) → milestones in `../CALENDAR.md`.

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

### Mississippi / Ohio
USACE Rivergages + NWS AHPS + USGS NWIS (§3). ⚠️ **Autumn (Sep–Nov) is the window** — an August "normal" is not evidence of a benign season. I retracted a "firing" read on 7/22 for exactly this.

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

### 🔴 GATUN LAKE ELEVATION — the physical driver, and it is UNRESOLVED (opened 2026-08-21, Will-prompted)

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

🔑 **PATTERN:** the `/uploads/YYYY/MM/` segment tracks roughly the **publication** month (data month **+1**), **not** the data month — a June-2026 summary sits under `2026/07`. Advisory numbers run ~4–5/month and **hyphenation is inconsistent** (`ADV21-2024` vs `ADV-04-2025`).
⚠️ **DISCOVER BY SEARCH, NEVER CONSTRUCT.** Every URL I built by pattern 404'd. The pattern is for *recognising* a URL, not generating one.

### 🔴 THREE THINGS THE MONTHLY OPS SUMMARY DOES **NOT** CONTAIN — checked, do not re-hunt per-month

Verified across **eight** advisories (six 2026 + Sep-2025 + Jun-2024): **zero occurrences of `PLD` or `elevation`.**
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
| Sep-2025 | 33.1 | **98.31%** (354 / 348) |
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
