# California and Oregon tides observed 2026-11-25 (AEOLUS, D:L1256, owed #23)
- `coops/wl_<station>.json`: NOAA CO-OPS datagetter 6-minute water_level, MLLW, LST (PST), feet, read 14:32-14:37 ET 11/25, quality p (PRELIMINARY). Data run to 11:18-11:30 PST. Requests paced 3 s, default curl client, `application=research`; 18 requests in all, every one HTTP 200.
- `coops/top_<station>.json`: NOAA top-ten water levels product (dpapi `toptenwaterlevels`, MLLW).
- Flag field `f` is O,F,R,L; L = 1 means the expected high-water limit was exceeded (set on the record samples, as a record would be).
- `LSR_CA_2026-11-25.txt`: NWS Local Storm Reports issued 11/25 by MTR, LOX, SGX (EKA issued none by 14:36 ET), from api.weather.gov products.
- `ca_alerts_1437.json`: api.weather.gov active alerts for CA, read 14:37 ET.
- `nwps_DLAF1_stageflow_from1120.json`: DeLand (St. Johns) NWPS, forecast issued 19:04Z 11/25; observed series trimmed to 11/20 onward.
- `summary.txt`: the highs per station. Findings: `workbook/KB.tsv` KB-AEO-334 to 337.
