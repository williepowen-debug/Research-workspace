# AEOLUS · SEISMIC — verified primary sources

**All three commands below were RUN and returned live 2026 data on 2026-08-13.** This folder is wired, not stubbed.

---

## 1. EARTHQUAKES — USGS (the issuing agency) ✅ verified 8/13

### Significant events, past 30 days — the S-2 screen
```bash
curl -s "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson" \
 | python3 -c "
import json,sys,datetime
for f in sorted(json.load(sys.stdin)['features'], key=lambda x:-x['properties']['mag']):
    p=f['properties']
    t=datetime.datetime.fromtimestamp(p['time']/1000, datetime.UTC).strftime('%Y-%m-%d')
    print(f\"M{p['mag']:<4} {t}  {p['place'][:55]:<55} tsunami={p.get('tsunami')}\")
"
```
**Verified return (8/13): 12 significant events**, largest **M7.4 Colombia (8/10)**.

### Other feeds — same URL pattern, swap the filename
`{significant,4.5,2.5,all}_{hour,day,week,month}.geojson`
- `4.5_week.geojson` — the standard global working set
- `significant_week.geojson` — the weekly screen

**Full API for custom queries** (bounding box, depth, min magnitude):
`https://earthquake.usgs.gov/fdsnws/event/1/`

⚠️ **Magnitude alone is never the signal.** The S-2 trigger needs **magnitude AND proximity to an insured/populated zone AND a loss estimate.** An M7 in the open ocean and an M6.5 under a city are different objects; the smaller one is the routable event.
⚠️ **`tsunami=1` is a FLAG that a warning was evaluated, not that a wave occurred.** Do not read it as damage.

---

## 2. US VOLCANOES — USGS Volcano Science Center ✅ verified 8/13

### Current elevated alert levels — the S-5 screen
```bash
curl -s "https://volcanoes.usgs.gov/vsc/api/volcanoApi/elevated" \
 | python3 -c "
import json,sys
for v in json.load(sys.stdin):
    print(f\"{v.get('vName'):<22} {v.get('alertLevel'):<9} {v.get('colorCode'):<7} threat={v.get('nvewsThreat')}  {str(v.get('alertDate'))[:10]}\")
"
```
**Verified return (8/13):** 5 elevated — Kilauea ADVISORY/YELLOW (**Very High Threat**), **Great Sitkin WATCH/ORANGE** (High Threat), Shishaldin, Kupreanof, Ahyi Seamount.

⚠️ **Use the `vName` field.** The obvious-looking `volcanoName` key **does not exist** and returns `None` for every row — a silent-blank failure that looks like "no volcanoes named" rather than an error. Cost me a pull on 8/13.

**Alert ladder (two independent scales — quote both):**
| Ground | Aviation |
|---|---|
| NORMAL · **ADVISORY** · **WATCH** · **WARNING** | GREEN · **YELLOW** · **ORANGE** · **RED** |

**`nvewsThreat`** is the National Volcanic Early Warning System threat ranking (Very Low → Very High). **A WATCH at a Very High Threat volcano is a materially different object from a WATCH at a Very Low Threat seamount** — the S-5 trigger is written to require both legs for that reason.

---

## 3. GLOBAL VOLCANISM — Smithsonian GVP / USGS Weekly Report ✅ verified 8/13

### Weekly Volcanic Activity Report (RSS)
```bash
curl -s -A "Mozilla/5.0 (research)" "https://volcano.si.edu/news/WeeklyVolcanoRSS.xml" \
 | grep -oP '(?<=<title>).*?(?=</title>)' | head -25
```
**Verified return (8/13): 23 items**, week of **30 July – 5 August 2026**. New eruptive activity: **Etna** (Italy), **Fuego** (Guatemala), **Krakatau** (Indonesia), **Puracé** (Colombia), **Telica** (Nicaragua). Continuing: Aira (Japan), Ambae, Dukono, Great Sitkin, Ibu, Kilauea + others.

⚠️ **`volcano.si.edu/reports_weekly.cfm` returns HTTP 403 to a plain fetch tool.** That is a fact about **one method**, not an unreachable primary — **the RSS endpoint with a user-agent works fine.** (`finding_blocked_mirror_is_not_an_unreachable_primary`.) Do not record GVP as unavailable.

⚠️ **The weekly report lags ~1 week** (the 8/13 edition covers 7/30–8/5). **For a fast-moving event, USGS/VAAC beats it** — use GVP for the standing global picture, not for breaking status.

### VEI — the S-1 instrument
GVP's Eruptive History database carries VEI. ⚠️ **VEI is assigned *after* an eruption, often revised, and the climate-relevant variable is not VEI itself but the *stratospheric SO₂ mass*.** The S-1 trigger requires **confirmed stratospheric injection**, not a VEI number alone — a large but tropospheric eruption has **no climate forcing** and must not be logged as a C2 event.

**SO₂ monitoring:** NASA **OMPS/OMI** SO₂ products via `https://so2.gsfc.nasa.gov/`

### Aviation — ash advisories (S-3)
**VAAC** (Volcanic Ash Advisory Centers) — nine regional centres; Washington VAAC via NOAA/NESDIS. **This is the instrument for the aviation/supply-chain path**, not the eruption report.

---

## PRECEDENTS WORTH KNOWING (for calibrating S-1)

| Event | VEI | Climate effect |
|---|---|---|
| **Tambora 1815** | 7 | "Year without a summer" (1816) — Northern-Hemisphere crop failure, food prices |
| **Krakatau 1883** | 6 | ~−0.4 °C, multi-year optical effects |
| **Pinatubo 1991** | 6 | **~−0.5 °C global for ~2 years** — the modern reference case |
| **Eyjafjallajökull 2010** | 4 | **No climate effect; ~100k flights cancelled** — the S-3 archetype |

⚠️ **Eyjafjallajökull is the calibration warning:** a *low*-VEI eruption produced the largest aviation/supply-chain disruption in modern memory, while contributing **nothing** to climate. **S-1 and S-3 are independent paths — an event can fire one, both or neither, and VEI predicts the wrong one.**
