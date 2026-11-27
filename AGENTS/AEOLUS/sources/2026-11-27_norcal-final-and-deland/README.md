# NorCal 11/25 highs on complete-day data, St. Johns read, WQ-735 recipe test (AEOLUS, 2026-11-27, D:L1256)
- `coops/wl_<station>.json`: NOAA CO-OPS 6-min water_level, MLLW, LST, 11/25-26, quality p. 4 requests 09:54 ET 11/27, 3 s pacing, default curl, `application=research`, all HTTP 200.
- `LSR_MTR_*`, `LSR_SGX_*`: NWS Local Storm Reports issued after 14:30 ET 11/25 (api.weather.gov products), read 09:56 ET 11/27. EKA issued none 11/25-27; LOX none after 14:30 ET 11/25.
- `nwps_{DLAF1,SNFF1,ASTF1}.json` (gauge metadata, flood categories, impacts, historic crests) and `_stageflow.json` (forecast issued 13:35Z 11/27; observed trimmed to 11/20 onward), read 09:56 ET.
- `fl_alerts_now.json`: api.weather.gov active alerts FL, 09:56 ET. `openfema_4956.json`: OpenFEMA DisasterDeclarationsSummaries for DR-4956 (refresh 11/25 12:06).
- `kaub_P5D.json`: PEGELONLINE KAUB W, last 5 days.
- `wq735/results.tsv`: one honest-name request per switched recipe; response bodies not kept (sizes recorded).
- Findings: `workbook/KB.tsv` KB-AEO-338 to 342.
