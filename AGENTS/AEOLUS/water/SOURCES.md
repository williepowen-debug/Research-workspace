# AEOLUS · WATER — verified primary sources

**Every command below was RUN and returned the stated value on 2026-08-13.** No reconstructed or remembered URLs.
**Re-verify a command the first time it fails rather than substituting a secondary** (L-15). A 403 or an empty return is a fact about *one method*, not proof the primary is unreachable (`finding_blocked_mirror_is_not_an_unreachable_primary`).

---

## C6 — COLORADO SYSTEM (USBR, the issuing agency)

### Lake Powell — daily pool elevation ✅ verified 8/13
```bash
curl -s "https://www.usbr.gov/uc/water/hydrodata/reservoir_data/919/csv/49.csv" | tail -5
```
Returns `datetime,pool elevation` in **feet**, full daily series back to **1963-12-28** (~22,875 rows).
**Verified return (8/13):** `2026-08-12,3520.37`
⚠️ **The file is long and chronological — you MUST `tail` it.** Fetching it through a page-summarizing tool truncates and hands back **1976 data with a clean HTTP 200** (this happened to me on 8/13; see `finding_partitioned_source_returns_stale_window_at_200`).

### Lake Mead — daily pool elevation ✅ verified 8/13
```bash
curl -s "https://www.usbr.gov/uc/water/hydrodata/reservoir_data/921/csv/49.csv" | tail -5
```
**Verified return (8/13):** `2026-08-12,1039.82`

### Storage (acre-feet) — datatype 17, same pattern
```bash
curl -s "https://www.usbr.gov/uc/water/hydrodata/reservoir_data/919/csv/17.csv" | tail -3
```
*Use only if storage is genuinely needed. **Elevation is the threshold instrument** — see README.*

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
**Why this is not optional:** on 8/13 the current-rate extrapolation was **right for Powell and badly wrong for Mead**. Powell falls Aug→Sep every year; **Mead RISES in 4 of 5** as downstream demand drops and Powell releases arrive. Skipping this would have produced a false 🔴 on the Hoover threshold in its first week.

### Colorado River Post-2026 Guidelines — the policy clock
- Program page: `https://www.usbr.gov/ColoradoRiverBasin/` · DOI newsroom for the ROD
- **Federal Register** is the authoritative notice venue: search *"Colorado River"* + *"Record of Decision"*
- Milestones → `../CALENDAR.md` (Final EIS **published 7/31/26**; earliest legal ROD **~8/30**; stated target **~10/1**; **12/31/26 hard expiry**)

---

## C5 — RIVER NAVIGATION

### Rhine at Kaub (WSV / PEGELONLINE — the German federal primary) ✅ verified 8/13
```bash
curl -s "https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations/KAUB/W/measurements.json?start=P3D" \
 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d[-1]); print('min',min(x['value'] for x in d),'max',max(x['value'] for x in d))"
```
Values in **cm**, 15-minute cadence. **Verified return (8/13 15:15 CEST): 13.0 cm**; 3-day range **10–17 cm**.
Swap `KAUB` for other stations (`DUISBURG-RUHRORT`, `KOELN`, `EMMERICH`). **Kaub is the binding shoal** — it is the reference gauge for loading economics.
**Benchmarks:** 2018 all-time low **25 cm** (set in October) · **≤40 cm** = uneconomical navigation (AEO-05's threshold).

### Mississippi / Ohio
USACE Rivergages + NWS AHPS. **Autumn (Sep–Nov) is the window** — an August reading of "normal" is not evidence of a benign season. I retracted a "firing" read on 7/22 for exactly this.

### Panama Canal
ACP advisories to shipping — `https://pancanal.com`. ⚠️ **AEO-04 resolves on a binding transit/draft RESTRICTION announcement, not on a scheduled draft step-down.** Do not grade the step-down as the event.

---

## SNOWPACK (sets the following year's allocation)

USDA NRCS **SNOTEL / NWCC** basin % of median — `https://www.nrcs.usda.gov/wps/portal/wcc/home/`
**Read Apr-1 % of median as the allocation-setting figure.** ⚠️ **Upper Colorado Basin is the inflow basin that matters** — and it sits near the ENSO dipole pivot where the signal is weak (see `DOSSIER.md` § "El Niño does not refill the Colorado").

---

## KNOWN-BAD / DO-NOT-USE

| Source | Why |
|---|---|
| `lakepowellwaterlevel.com`, `lakebrief.com` and similar trackers | **Disagreed with the USBR primary by 3.83 ft on 8/12 and inverted the trend sign.** Cost me a published wrong conclusion. |
| Any **percent-full** figure | Different capacity bases across sources (19% vs 23.1% for the same lake, same week). **Cite elevation.** |
| Page-summarizing fetch of the USBR CSVs | Truncates a 22k-row file and returns **1976 data with HTTP 200**. Use `curl … \| tail`. |
