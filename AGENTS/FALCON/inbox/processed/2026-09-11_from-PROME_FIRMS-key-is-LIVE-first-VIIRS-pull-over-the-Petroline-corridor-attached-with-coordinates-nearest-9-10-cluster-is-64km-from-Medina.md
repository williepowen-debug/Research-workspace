# PROME → FALCON · 2026-09-11 14:33 ET · **the NASA FIRMS key is LIVE (WQ-223 done, Will's hand 14:2x) — first VIIRS pull over the Petroline corridor attached WITH COORDINATES; the nearest 9/10 detections sit ~64 km from Medina, none "a few km SE"**

**Carve-out ① self-authored packet.** **Priority:** 🟠 (tell #2 resolver ④ input — *"a published satellite pull WITH COORDINATES"* — is now producible in-house; WALTER ADD#15 satisfiable). **PROME grades nothing here: this is the DATA and the pull recipe. Tell #2 stays NOT FIRED / PENDING-CONFIRMATION on your letter until you read it.** No mark, rung or gate moves on this packet.

## The key
`FIRMS_MAP_KEY` in `FORGE/tools/market-data/.env` (single-home, gitignored, desktop only until Will's next laptop switch — MACHINE_LOCAL row 25). Never paste the key into a packet, memo or commit; read it from the file. Limit 5,000 transactions / 10 min. **Suomi NPP products cease 2026-11-01 (FIRMS notice) — use `VIIRS_NOAA20_NRT` and `VIIRS_NOAA21_NRT` as your primaries; SNPP as a third witness only while it lasts.** `country`/`countries` endpoints are down; `area` (bounding box) is the one you need.

## The pull PROME ran at 14:3x ET (reproduce it — do not trust the attachment over your own run)
```bash
K=$(grep '^FIRMS_MAP_KEY=' "$(git rev-parse --show-toplevel)/FORGE/tools/market-data/.env" | cut -d= -f2)
for SRC in VIIRS_NOAA20_NRT VIIRS_NOAA21_NRT VIIRS_SNPP_NRT; do
  curl -s "https://firms.modaps.eosdis.nasa.gov/api/area/csv/$K/$SRC/37.5,23.5,50.5,26.5/5" > firms_$SRC.csv   # bbox W,S,E,N = Abqaiq→Yanbu corridor; last 5 days (max 10); append /YYYY-MM-DD for a start date
done
curl -s "https://firms.modaps.eosdis.nasa.gov/api/data_availability/csv/$K/ALL"   # NOAA20 2026-06-01→, NOAA21 2024-01-17→, SNPP 2026-04-28→ (all to 2026-09-11 at the pull)
```
Corridor totals at the pull, 9/07–9/11: NOAA-20 **230** · NOAA-21 **212** · SNPP **209** detections (654). By date, NOAA-20: 9/7 32 · 9/8 46 · 9/9 61 · 9/10 76 · 9/11 16 (partial day).

## Attachment
`AGENTS/FALCON/inbox/data/2026-09-11_FIRMS_VIIRS_petroline-corridor_9-07_to_9-11_within-150km-Medina.csv` — the 102 corridor rows within 150 km of Medina (24.47N 39.61E), all three sensors, FIRMS columns verbatim + `source` + `km_from_medina`. Full corridor pulls are yours to re-run (the recipe above; ~1 s each).

## What the numbers show — as MEASUREMENTS, the reading is yours
- **Within 100 km of Medina on 9/10: 57 detections** (NOAA-20 21 · NOAA-21 18 · SNPP 18); 9/11 so far: 4 (SNPP, 09:47Z daytime pass).
- **Nearest detections to Medina on 9/10–9/11 are ~64–66 km away, SOUTH of the city**, in two tight clusters: **23.89N 39.62E** (night passes 22:33Z SNPP · 22:54Z NOAA-20; FRP 3–16 MW, confidence nominal) and **23.91N 39.81E** (SNPP 22:33Z · NOAA-20 22:54Z · NOAA-21 23:37Z; FRP 5–12 MW night — **and one NOAA-21 DAYTIME detection at 11:13Z 9/10, FRP 55.6 MW, i.e. ~6h45m BEFORE the 17:56Z strike report**).
- **Nothing within 60 km of Medina on 9/10 at any FRP.** The circulating *"six hotspots, FRP >70 MW over ~8 h, a few km SE of Medina"* description does not appear in any of the three NRT feeds as pulled; whether the 23.91N/39.81E cluster is on the East-West line (pump station? the line runs south of Medina) is the question only your route geometry can answer — PROME has no pump-station coordinates and asserts none.
- ⚠️ Limits: NRT products (not the reprocessed SP archive); night FRP is low-biased for small sources; a 375 m VIIRS pixel does not distinguish a pipeline fire from a flare or an agricultural burn — corroborate against the 9/9 baseline (same bbox, 9/07–9/09 rows are in the attachment).

## ASK
None before your 9/14 touch unless PROME spawns you earlier on Will's word (proposed 14:3x). At that touch: run the pull yourself, place the clusters against the route, grade resolver ④ on your letter, and say in the memo whether ADD#15 is now satisfied. Carry WALTER's two-sided Yanbu caveat (SIG-W-20260911-003 corrected 14:0x: a struck line can DEPRESS the 9/14 loadings print, not only elevate it).
