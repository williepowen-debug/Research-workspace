# UNG trigger source verification — November 2, 2026

Authority: Will selected “Check trigger and refresh the card” in WALTER's active session. The bounded coordination packet is PROME/inbox/2026-11-02_from-WALTER_UNG-trigger-check-and-TERRY-refresh.md, committed f28fc802172900067c88568e8cc199561c8faa1c and sent by verified native Codex channel to active PROME. Notification acceptance is not consumption. Existing TERRY task was directly read as notLoaded/interrupted; no duplicate owner launched by WALTER.

## Observation, not owner grade

Primary NOAA GFS 0.25-degree analysis (f000), November 2 06:00 UTC: arithmetic mean of U wind at exactly 60N and 10 hPa over all 1,440 equally spaced longitudes = **+5.531545627 m/s**. This analysis is above the card's strict below-zero reversal condition; it does not establish a reversal. It is an analyzed model field, not a direct station observation and not a forecast lead.

Daily 00Z analyses on the same fetched basis:

| Analysis | Zonal mean, m/s |
|---|---:|
| October 29 | +14.326738078 |
| October 30 | +13.244741428 |
| October 31 | +12.284259332 |
| November 1 | +10.468449368 |
| November 2 | +6.305083008 |

Daily observations show weakening while staying positive in this sample. The October 29 NOAA GFS control is +0.0467 m/s above AEOLUS's saved NOAA scout +14.28; cause not adjudicated, sign unchanged. It is not a replacement for AEOLUS's +14.1 ECMWF analysis. No ECMWF rerun or proof of US surface cold/downward coupling is supplied. Daily sampling alone cannot exclude an intraday reversal; canonical T1 grade and logging remain with AEOLUS/TERRY.

## Reproducible data basis

NOAA NOMADS GRIB filter: https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl . Parameters recorded in gfs-access.json/daily-observation-check.json select gfs.20261102/06/atmos, gfs.t06z.pgrb2.0p25.f000, UGRD, 10 mb, exact latitude 60N, longitudes 0..359.75. HTTP 200, binary GRIB2, 2,339 bytes, SHA256 6ee4182f9bd333c1c5e47e6f3eee54a458f15ff2df0cdea8560b87c1329965ec for the 06Z file.

Sections explicitly checked: valid total length and end marker; grid template 3.0, Ni=1440/Nj=1, both endpoint latitudes 60N, 0.25-degree longitude spacing; product template 4.0, category/parameter 2/2 (UGRD), pressure surface 1000 Pa, lead 0; packing template 5.0, 1440 values, no bitmap. Decode Y=(R+X*2^E)*10^(-D), reference IEEE float, signed-magnitude scaling. Independent integer-bit extraction and numpy.unpackbits agree at every point for the 06Z field. Saved metadata include min/max; individual negative longitudes do not establish a negative zonal mean. No eccodes installation required.

Primary format docs: https://www.nco.ncep.noaa.gov/pmb/docs/grib2/grib2_doc/grib2_temp5-0.shtml ; https://www.nco.ncep.noaa.gov/pmb/docs/grib2/grib2_doc/grib2_temp3-0.shtml ; https://www.nco.ncep.noaa.gov/pmb/docs/grib2/grib2_doc/grib2_temp4-0.shtml . NOAA official filter documentation: https://www.cpc.ncep.noaa.gov/products/tools/scripting_grib_filter.html . Raw public fields and metadata retained here. This is a bounded analysis, not a new registered instrument or unattended monitor.

## Card boundary

WQ-573/GATE-TERRY-UNG-01: January 15 2027 UNG 10/12 call spread x5, debit <= $0.50, planned max loss $256.50, contingent on observed reversal by November 12 and the existing day/price conditions. Fresh option-chain/underlying quotes and any re-cut belong to TERRY; old October 30 screening marks are not live. No order, new sizing grant or condition waiver is conveyed. The gross-short bookmark is positioning context (SIG-W-20261102-002), not T1 evidence. Next result needed is AEOLUS/TERRY's source acceptance and refreshed owner card, not another approval of the already conditional structure.
