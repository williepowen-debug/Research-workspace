# California tides, 2026-11-24 (AEOLUS, D:L1248)
- `ca_tides_scan.py`: CO-OPS 6-min observed highs vs predictions (MLLW, LST), datum-page max, monthly-highest record scan. Output: `scan_2026-11-24_2330.txt`; raw per station in `coops/`.
- ⚠️ CO-OPS datagetter returned HTTP 403 from about 23:27 ET 11/24 after this script's ~300 requests (10-year monthly chunks x 17 stations). Stations from Port Chicago south have no observations in this pull. Pace any rerun; never change the client string to get past a refusal.
- `nws_alerts_CA_*.json`: api.weather.gov active alerts for CA, read 23:24 ET.
- `nwps_*`: NWS NWPS gauges (api.water.noaa.gov). HBYC1 = North Spit, ANVC1 = Arena Cove, CECC1 = Crescent City, FTPC1 = San Francisco. Their observed series match CO-OPS MLLW to 0.01 ft (11/22-24). Forecast series are the astronomical tide only. The stageflow files are trimmed to 11/20 onward.
- Findings: `workbook/KB.tsv` KB-AEO-326 to 329.
