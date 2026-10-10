# AEOLUS · WATER — verified primary sources
> HOT file, split 2026-10-10. History, superseded entries, verification stories → [`SOURCES_ARCHIVE.md`](SOURCES_ARCHIVE.md) (verbatim).

**Every command below was RUN and returned the stated value on the date its own entry gives (first batch 2026-08-13; later entries carry their own verify dates; split hot/cold 2026-10-10 — history in `SOURCES_ARCHIVE.md`).** No reconstructed URLs.
**Re-verify a failing command rather than substituting a secondary** (L-15). A 403 or an empty return is a fact about *one method*, not proof the primary is unreachable.

---

## 1. DROUGHT — the shared upstream input (C2 · C4 · C5 · C6)

### US Drought Monitor — statistics API ✅ verified 8/13
```bash
curl -s -H "Accept: application/json" \
 "https://usdmdataservices.unl.edu/api/USStatistics/GetDroughtSeverityStatisticsByAreaPercent?aoi=us&startdate=7/28/2026&enddate=8/11/2026&statisticsType=1"
```
Valid 9/15: CONUS D1–D4 **59.37%**, D4 **2.02**. ⚠️ Rows for `CONUS` *and* `Total` (US+PR), ~8 pp apart — read `areaOfInterest`.
**Cadence:** valid Tuesday 8 a.m. ET, **released Thursday.** New map ≈ every Thursday morning.

### State granularity — 🔴 **RECIPE REPLACED 2026-09-18**
⛔ `USStatistics` + `aoi=CO` is DEAD (`-area of interest not recognized`). Use:
```bash
# StateStatistics — NOT USStatistics. 2-digit FIPS — NOT postal. Accept header REQUIRED.
curl -s -H "Accept: application/json" \
 "https://usdmdataservices.unl.edu/api/StateStatistics/GetDroughtSeverityStatisticsByAreaPercent?aoi=48&startdate=8/25/2026&enddate=9/15/2026&statisticsType=1"
# aoi=48 Texas · 40 Oklahoma · 19 Iowa · 31 Nebraska · 06 California · 29 Missouri · 28 Mississippi · 05 Arkansas · 47 Tennessee
```
Verified 9/18 (8/25→9/15: TX +23.65pp · MS +21.97 worse; IA −12.85 better). 🔑 **Never one national adjective — the divergence IS the read** (KB-AEO-138). ⚠️ Extent vs intensity can diverge: quote both.

### Palmer Drought Severity Index (CPC)
`https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/cdus/palmer_drought/`
Multi-season persistence, not current conditions.

### Soil moisture (CPC monitoring)
`https://www.cpc.ncep.noaa.gov/products/Soilmst_Monitoring/` — the direct **crop-yield** link; leads USDM at the agricultural margin.

---

## 2. SNOWPACK — sets the following year's allocation

**NRCS SNOTEL / National Water and Climate Center** ✅ page reachable 8/13 (225 KB)
`https://www.nrcs.usda.gov/resources/data-and-reports/sno-tel-and-snow-course-data-and-products`
Interactive basin reports: `https://nwcc-apps.sc.egov.usda.gov/imap`
Read **Apr-1 basin % of median**. ⚠️ Near-zero Jun–Sep — not a gap. 🔑 Powell's basin = UPPER Colorado (weak ENSO signal).

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
🔑 **`09380000` Lees Ferry** = compact division point below Glen Canyon — **measures the releases that refill Mead.**
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
⚠️ **You MUST `tail`** — a page-summarizing fetch returns **1976 data with HTTP 200**.

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
⚠️ Mead's Aug→Sep rise rides Glen Canyon releases (2026 = 9-yr low) — **check Lees Ferry first.**

### ✅ 24-MONTH STUDY **ARCHIVE + MIN/MAX PROBABLE** — probe 2026-08-27
```bash
# EVERY PAST STUDY. Pattern verified HTTP 200 back to 2020.
curl -sL -o AUG25.pdf "https://www.usbr.gov/lc/region/g4000/24mo/2025/AUG25.pdf"   # /24mo/YYYY/MONYY.pdf
# MIN and MAX PROBABLE — the issuer's own inflow envelope, published monthly beside the Most Probable:
curl -sL -o AUG26_MIN.pdf "https://www.usbr.gov/lc/region/g4000/24mo/2026/AUG26_MIN.pdf"
curl -sL -o AUG26_MAX.pdf "https://www.usbr.gov/lc/region/g4000/24mo/2026/AUG26_MAX.pdf"
```
**Error base rate** (Aug study vs actual end-Dec Mead, 2020–25): **n=6, mean +2.19 ft, 5 of 6 HIGHER**; framework now replaced (L-18). ⚠️ **August deviation is NOT a signal** (KB-098).
⚠️ **METHOD:** pdfminer gives an unlabelled column — **match the head to `921/csv/49.csv` within 0.02 ft before reading ANY projected cell.**

### 🔴 24-MONTH STUDY — registered 2026-08-27 as the PRIMARY C6 instrument
```bash
# The UC index lists every month. VERIFIED 2026-08-27.
curl -sL "https://www.usbr.gov/uc/water/crsp/studies/index.html" | grep -oiE 'href="[^"]*24Month[^"]*"'
# Current-month Lower Colorado copy (Mead + Powell in one file):
curl -sL "https://www.usbr.gov/lc/region/g4000/24mo.pdf" -o 24mo.pdf
```
⚠️ **Aug-2026 = TWO files** `24Month_08_6.pdf` / `24Month_08_7.pdf` (6 / 7 maf release). ⚠️ `24mo.pdf` served the JULY study on 8/27 — **check the title line.**
**Read:** anchor on an ACTUAL (Mead 2025-12-31 = **1062.24**), end-of-month, verify ≥6 months; 🔴 **READ THE PATH** — "at any point" grades on the window MINIMUM (L-36).
**Aug-2026:** Powell release **7.48→6.00 maf** · Powell below **3,510 ft** in WY2027 · Mead Dec-2026 **1,034.74 ft** (< binding 1,035).

### Colorado Post-2026 Guidelines — the policy clock
`https://www.usbr.gov/ColoradoRiverBasin/` · Federal Register (*"Colorado River"* + *"Record of Decision"*) → `../CALENDAR.md`.
ROD ✅ 8/27: `https://www.usbr.gov/ColoradoRiverBasin/post2026/decision-doc/P26_RecordofDecision_Final.pdf`; same dir: `2027-2028OperatingGuidelines_Final.pdf` (binding numbers) · `FutureColoradoOperations_Factsheet.pdf` · `P26_BiologicalOpinion_Final.pdf`. ❌ `/ColoradoRiverBasin/documents/post2026/…` 404s.

---

## 5. RIVER STAGE — navigation (C5)

### Rhine at Kaub (WSV/PEGELONLINE, German federal primary) ✅ verified 8/13
```bash
curl -s "https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations/KAUB/W/measurements.json?start=P3D" \
 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d[-1]); print('min',min(x['value'] for x in d),'max',max(x['value'] for x in d))"
```
cm, 15-min. `MAXAU` 362.3 · `WORMS` 443.4 · `MAINZ` 498.3 · **`KAUB` 546.2** (binding shoal) · **`DUISBURG-RUHRORT` 780.8** (C5 trigger) · `EMMERICH` 851.9.
⚠️ **`KOELN` is NOT a valid shortname in the API** — do not use it. List stations with:
```bash
curl -s "https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations.json?waters=RHEIN" | python3 -c "import json,sys;[print(s['shortname'], s.get('km')) for s in json.load(sys.stdin)]"
```
### 🔴 WSV **CHARACTERISTIC VALUES** — probe 2026-08-27
```bash
curl -s "https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations/KAUB/W.json?includeCharacteristicValues=true" \
 | python3 -c "import json,sys;[print(c['shortname'],c['value'],c.get('validFrom')) for c in json.load(sys.stdin)['characteristicValues']]"
```

| | **NNW** record low | **MNW** mean low water | **MW** mean stage | **GlW** navigation reference | ⚠️ **TuGLW — a DEPTH, not a stage** |
|---|---|---|---|---|---|
| **Kaub** | **25** | **65** | 208 | **77** | 190 |
| **Duisburg-Ruhrort** | **153** | **201** | 394 | **227** | 280 |

🔴🔴 **C5 →5 keys to `NNW` Kaub 25 / Duisburg 153 FROZEN 2026-08-13 — NEVER re-point at the live field** (WSV rewrites `NNW` on a record, so a live key cannot fire on one). Re-read only to DETECT republication.
🔑 `NNW` = lowest known **daily mean** ⇒ **grade on UNROUNDED daily means.** Kaub `NW` 25.0 is not an independent witness.
✅ `GlW` verified 9/18 (Kaub 77.0 · Duisburg 227.0, `validFrom` 2023-01-01) = stage undercut ~20 ice-free days/yr; re-check `validFrom`. GlW re-key: PROPOSED, NOT EXECUTED.
🔴 **`TuGLW` is a DEPTH below GlW, not a stage** — never difference it against a gauge reading.
🔴 REST caps at ~31 days. A raw-data route back to 2000 exists, unresolved (paths in archive) — retry; never re-close from REST alone (L-35).

### 🔴 WSV FORECAST endpoint — registered 2026-08-13
```bash
curl -s "https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations/KAUB/WV/measurements.json" \
 | python3 -c "import json,sys;[print(x['timestamp'][:16],x['value']) for x in json.load(sys.stdin) if x.get('type')=='forecast']"
```
**Available at `KAUB`, `DUISBURG-RUHRORT`, `EMMERICH` only — HTTP 404 at Maxau, Worms, Mainz** (verified).
⚠️ Not in metadata. **Horizon ~2 days** — state it each pull.

### DISCHARGE `Q` — datum-independent, available at all six
`/stations/<ST>/Q/measurements.json` — m³/s, 15-min. **Prefer discharge across eras** (`gaugeZero` re-referenced at some stations).
⚠️ **"40 cm uneconomical" is UNPROVENANCED — not the basis of any trigger.**

### ✅ RHINE BARGE FREIGHT — GAP CLOSED 2026-09-28
**① Contargo surcharge (KWZ)** — DAILY, by gauge:
```bash
curl -sL -A 'Mozilla/5.0' "https://www.contargo.net/de/business/business-news/detail-business/pegelstaende-am-rhein-und-kleinwasserzuschlag-1/" \
 | python3 -c "
import re,html,sys
s=re.sub(r'<script.*?</script>|<style.*?</style>','',sys.stdin.read(),flags=re.S)
t=re.sub(r'(\s*\|\s*)+',' | ',html.unescape(re.sub(r'<[^>]+>',' | ',s)))
m=re.search(r'Aktuelle Wasserstände.*?Mindestniveau[^A-Za-z]*',t); print(m.group(0) if m else 'NO GAUGE TABLE')
for st in ('Pegel Kaub','Pegel Duisburg-Ruhrort'):
    m=re.search(re.escape(st)+r' \| 20. Container \| 40. Container \|(.*?)(Bitte|Der Anstieg)',t)
    print(st,'::',m.group(1) if m else 'NO SCHEDULE')
"
```
EN: `https://www.contargo.net/en/business/auxiliary-conditions/low-water/`. DE extended: **Kaub ≤40 cm → €1,075 / €1,280** per full 20′/40′; Duisburg 130–121 cm → €800 / €900.
⚠️ One operator, containers only; URL may change. **Quote the €-row by gauge level, never the tier number.** "Transportverpflichtung endet" (Kaub ≤80 / Duisburg ≤180 / Köln ≤105 / Emmerich ≤30) = obligation ended ≠ service stopped. ~€150/t dossier figures stay unverified.
**② CBS 85817NED** — QUARTERLY, 2021=100 (never splice 84050NED), incl. fuel. `A042621` dry SPOT · `A042620` dry contract · `A042619` wet bulk · `A023824` container · `A023820` all.
```bash
curl -s "https://opendata.cbs.nl/ODataApi/odata/85817NED/TypedDataSet?\$filter=CPA2015%20eq%20'A042621'%20or%20CPA2015%20eq%20'A023820'%20or%20CPA2015%20eq%20'A023824'%20or%20CPA2015%20eq%20'A042619'" \
 | python3 -c "
import json,sys
n={'A042621':'dry_spot','A023820':'goods_all','A023824':'container','A042619':'wet_bulk'}
for x in json.load(sys.stdin)['value']:
    if 'KW' in x['Perioden'] and x['Prijsindex_1'] is not None and x['Perioden']>='2025': print(x['Perioden'].strip(),n[x['CPA2015'].strip()],x['Prijsindex_1'],'yoy%',x['Jaarmutaties_3'])
"
```
Base: dry-spot 2018 **+87%**, 2022-Q3 **+104% y/y**. ⚠️ Fuel contaminates; **n=2 — NO band.** 2026-Q3 = first print of this event.
**③ TANKER** — no free €/t. (a) CBS `A042619`: level and y/y disagree — quote both. (b) `https://www.insights-global.com/category/blogs/freight-rates/` — direction + deal counts only. (c) press quotes → `LOG.tsv`. (d) fastenergy.de, €/100 L, no history:
```bash
curl -sL -A 'Mozilla/5.0' "https://www.fastenergy.de/heizoelpreise.htm" \
 | python3 -c "
import re,html,sys
s=re.sub(r'<script.*?</script>|<style.*?</style>','',sys.stdin.read(),flags=re.S)
t=re.sub(r'(\s*\|\s*)+',' | ',re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' | ',s))))
m=re.search(r'Heizölpreise in den Bundesländern \| Bundesland \| (\S+) \| (\S+) \| Differenz \|(.*?)\| Heizölpreise in den Großstädten',t)
print('dates',m.group(1),m.group(2)) if m else print('NO TABLE')
if m:
    for st,a,b in re.findall(r'([A-ZÄÖÜ][\w\-äöüß]+) \| ([\d.,]+) € \| ([\d.,]+) €',m.group(3)): print(st,a,b)
st=re.search(r'Stand: [^|]+',t); print(st.group(0) if st else 'NO STAND')
nat=re.search(r'Der Heizölpreis in Deutschland beträgt heute \| ([\d,]+ € / 100 l)',t); print('national',nat.group(1) if nat else '?')
"
```
⚠️ Confounded by regional supply — never a Rhine signal alone.
**④ GRAIN** — no free €/t; use CBS `A042621`. Schuttevaer → `LOG.tsv` only. ⚠️ "€165/t grain 9/11" is GASOIL — discard.
- **Grain freight is best measured on the MISSISSIPPI** — see the USDA entry in §MISSISSIPPI below.

### ✅ YANGTZE — gap closed 2026-08-13
```bash
curl -sL "http://www.cjh.com.cn/sqindex.html" \
 | python3 -c "
import re,sys,json,datetime
s=sys.stdin.read()
d=json.loads(re.search(r'var sssq = (\[.*?\]);', s, re.S).group(1))
for x in d: print(x['stnm'], x.get('z'), 'm', x.get('q') or x.get('oq') or '-', 'm3/s')
"
```
⚠️ Parse the `var sssq` JSON. `z` m · `q` m³/s. Yichang · Hankou · Datong = navigation gauges.
⚠️ `www.cjw.gov.cn` does not resolve. GB/UTF-8 mixed — decode defensively.

### ✅ DANUBE — gap closed 2026-08-13
```bash
curl -sL "https://www.vizugy.hu/index.php?mapModule=OpVizallas&mapData=VizmerceLista"
```
⚠️ cm vs each station's own datum — **negative is normal.** LKV reference + the authority's own flag:
```bash
curl -s "https://terkeptar.vizugy.hu/server/rest/services/Vizugy_hu/LKV_folyok/MapServer/0/query?where=VizfolyasNev%3D%27Duna%27&outFields=Nev,Fkm,Vizallas,LKV,LKVIdopont,LKV_viszony&returnGeometry=false&f=json"
```
`LKV` lowest-ever cm · **`LKV_viszony` −1/+1 below/above.** ⚠️ **Exclude LKV dates 1799/1884/1894-12-31** (null sentinels).

### ✅ PARANÁ — gap closed 2026-08-13
```bash
curl -sL "https://fich.unl.edu.ar/cim/rios/parana/alturas"
```
Ships its own ALERT / EVACUATION levels. **Rosario** (grain ports) 3.02 m on 8/13, alert 5.00.
```bash
curl -sL "https://fich.unl.edu.ar/cim/rios/historico/39"     # 39 = Rosario; 366 daily records
```
Trailing year to 13/08/2026: min 1.08 · **P10 1.40** · median 2.14 · max 3.03. **Use P10 ≈ 1.40 m as the low-water reference.** ⚠️ One year is a SHORT base.

### ✅ MISSISSIPPI — INSTRUMENT GAP CLOSED 2026-08-27
```bash
# Memphis — live stage + the published low-water reference. VERIFIED 2026-08-27 (HTTP 200).
curl -s "https://api.water.noaa.gov/nwps/v1/gauges/MEMT1" | python3 -c "
import json,sys; d=json.load(sys.stdin)
print(d['name'], d['status']['observed']['primary'], d['status']['observed']['primaryUnit'], d['status']['observed']['validTime'])
print('lowThreshold:', d['lowThreshold'])
for r in d['flood']['lowWaters']['historic'][:6]: print(' ', r['occurredTime'][:10], r['stage'], r.get('statement',''))
"
```
⚠️ **PIPE IT** — the raw JSON is enormous. 8/27: **12.47 ft; `lowThreshold` −8 ft.**
🔑 **−8 ft is NOT the record low** — grade crises vs `lowWaters.historic`: **2023 −12.06 · 2022 −10.81** ft (C5 analogues; −8 = watch). Never quote the 1988 "LOWEST STAGE ON RECORD" label.
⚠️ **Only Memphis is referenced.** St. Louis (USGS `07010000`): **no reference plane — no adjective.** Vicksburg/Cairo IDs unresolved (VICM6/VKBM6/VIKM6, CAIA2/CACT1 404). **Sep–Nov is the window.**

### ✅ MISSISSIPPI GRAIN BARGE FREIGHT — USDA AMS, registered 2026-09-28
**$/ton = rate × benchmark / 100** (1976 Tariff No. 7).
```bash
curl -s "https://agtransport.usda.gov/resource/deqi-uken.json?\$order=date%20DESC&\$limit=14" \
 | python3 -c "
import json,sys
B={'Twin Cities':6.19,'Mid-Mississippi':5.32,'Lower Illinois':4.64,'Illinois River':4.64,'St. Louis':3.99,'Cincinnati':4.69,'Lower Ohio':4.46,'Cairo-Memphis':3.14}
for r in json.load(sys.stdin):
    if 'rate' in r: print(r['date'][:10], r['location'], r['rate'], '%% -> \$%.2f/ton' % (float(r['rate'])*B[r['location']]/100))
"
```
Full history for one origin: `...deqi-uken.json?location=St.%20Louis&$limit=5000&$order=date` (some weeks have no `rate` key — skip, do not zero).
St. Louis peaks: 2022 **2,653%** · 2023 **1,326%**; 9/22 834.7%. ⚠️ **Compare the SAME WEEK across years only.** NO band. Weekly (Thu GTR).

### 🔴 Panama — INSTRUMENT GAP CLOSED 2026-08-13
ACP Monthly Canal Operations Summary — **oceangoing transits, daily average**.
```bash
curl -sL -A "Mozilla/5.0 (research)" \
 "https://pancanal.com/wp-content/uploads/2026/04/ADV-14-2026-Monthly-Canal-Operations-Summary-April-2026-.pdf" -o adv.pdf
python3 -c "from pdfminer.high_level import extract_text; print(' '.join(extract_text('adv.pdf').split()))"
```
⚠️ **Read TRANSITS (Apr-2026 38.70), not ARRIVALS.** ⚠️ Transits are blind to draft-only restrictions.
⚠️ **SLOTS ≠ TRANSITS** (charter 8/21): A-29-2026 caps *slots* at 32/day; the band is ≤32 *transits*. Baseline re-based to **35.86/day**.

### ✅ GATUN LAKE ELEVATION — GAP CLOSED 2026-08-27
```bash
# ACP's own daily series, 1965-01-01 → present. VERIFIED 2026-08-27 (HTTP 200, 405,357 B).
curl -s "https://evtms-rpts.pancanal.com/eng/h2o/Download_Gatun_Lake_Water_Level_History.csv" -o gatun.csv
head -1 gatun.csv; tail -3 gatun.csv     # header: DATE_LOG,GATUN_LAKE_LEVEL(FEET)
```
83.80 ft (8/26); normal **82–87 ft**. ⚠️ **Cite the ADVISORY for step dates**, not the projection CSV. No lake band yet — base-rate first.

### ⬇️ SUPERSEDED — the 8/21 "UNRESOLVED" entry
→ archive. ⛔ The Tableau `GatunWaterLevel` dashboard is cert-broken + JS-rendered — use the CSV.

### ✅ PANAMA — VERIFIED URLs AND THE PATTERN (2026-08-21)
HTTP 200: **`curl -sLk` + browser UA, then pdfminer** (it warns on a no-extract flag and proceeds).

| Advisory | Content | URL tail (prefix `https://pancanal.com/wp-content/uploads/`) |
|---|---|---|
| **A-29-2026** | slot cap + draft postponement (8/20) | `2026/08/ADV-29-2026-Additional-Measures-to-Address-Reduced-Precipitation-in-the-Canal-Watershed.pdf` |
| **A-33-2026** | postpones 10/01 47.5 ft step; 48.0 ft stays (9/4; PDF metadata date wrong) | `2026/09/ADV-33-2026-Postponement-of-Maximum-Authorized-Draft-Adjustment-in-the-Neopanamax-Locks.pdf` |
| **A-34-2026** | Monthly Ops Aug 2026 | `2026/09/adv-34-2026-monthly-canal-operations-summary-august-2026.pdf` |
| A-22-2026 | Draft adjustment (7/01) | `2026/04/ADV-22-2026-Draft-adjustment-in-the-Neopanamax-Locks.pdf` |
| A-09/14/19/23/26 -2026 | Monthly Mar–Jul 2026 | `2026/04/…March-2026.pdf` · `2026/04/…April-2026-.pdf` · `2026/06/…May-2026.pdf` · `2026/07/…June-2026.pdf` · `2026/08/…July-2026.pdf` |

🔴 **NO usable path pattern — never construct a URL**; use the index below or `PANAMA_SERIES.md` §10.

### ⚠️ CORRECTED 2026-08-21 — MY "THREE THINGS IT DOES NOT CONTAIN" WAS WRONG AT CORPUS SCALE
APPENDIX prose (not the table) carries max draft (2023-24 trough **44.0 ft**). Scope a negative to what you scanned.

### 🔑 GATUN LAKE ELEVATION — one primary figure exists
A-27-2024: **85.02 ft** — a spot reading, not a series.

### ✅ THE COMPLETE ADVISORY ARCHIVE — a WORKING path beside the known-bad one
⚠️ PLURAL `advisories-to-shipping/` truncates at A-46-2024. ✅ SINGULAR = complete (1,005 PDFs):
```bash
curl -sLk -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" "https://pancanal.com/en/maritime-services/advisory-to-shipping/"
```

### 🔴 STILL-TRUE NEGATIVES (now n=33, scoped to the statistics table)
The fixed-schema statistics table (n=33) has: ❌ **TONNAGE** (derive transits × draft) · ❌ **DRAFT** (draft advisories only) · ❌ **GATUN ELEVATION** (A-29 prints none). 🔑 ACP publishes watershed INPUTS, not the STOCK.

### ✅ THE COLUMN THAT REPLACES THE UNPUBLISHABLE AUCTION PRICE
⛔ **No published auction clearing prices** — $3.78M/$4M are relays; never gate. ✅ Monthly Ops prints `Auctioned booking slots` Available / Used. ⚠️ Record `Used` > `Available` as given.
⚠️ **NOT YET A BAND.** Three non-monotonic points is not a base rate.

#### 🔴 DO NOT SCRAPE THE ADVISORIES INDEX — it is silently stale
⚠️ `pancanal.com/en/advisories-to-shipping/` is JS-rendered; curl + WebFetch agreeing is NOT corroboration. **Discover, then fetch:** search `"Monthly Canal Operations Summary" pancanal <month> 2026`.

#### AEO-04 resolution — spec tightened
Resolves on a binding RESTRICTION, not a scheduled draft step-down: its own Advisory, or transits **≤32 Yellow · ≤27 Orange · ≤22 Red**.

---

## KNOWN-BAD / DO-NOT-USE

| Source | Why |
|---|---|
| `lakepowellwaterlevel.com`, `lakebrief.com` and similar | **Disagreed with USBR by 3.83 ft on 8/12 and inverted the trend sign.** Cost a published wrong conclusion. |
| Any **percent-full** figure | Different capacity bases across sources (19% vs 23.1%, same lake, same week). **Cite elevation.** |
| Page-summarizing fetch of USBR CSVs | Truncates and returns **1976 data with HTTP 200**. Use `curl … \| tail`. |
| `droughtmonitor.unl.edu` HTML tables | Returns a load error to fetch tools. **Use the statistics API.** |

### ⚠️ ACP'S OWN ARITHMETIC DISAGREES WITH ITSELF IN THREE MONTHS
Sep-2025 prints **95.34%** (computes 98.31%) · Aug-2025 96.18% (96.71%) · May-2025 973 vs 974. **Store `available`/`used`; report AS PRINTED.**
