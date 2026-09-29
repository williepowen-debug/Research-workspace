# C3 — PJM heat signature: 9/1–9/3 and 9/16–9/17/2026 vs mid-July (asked by WATT)

**Written:** 2026-09-28 20:06 EDT (`date`) · **Author:** AEOLUS measurement worker (spawned) · **Channel:** C3 energy demand · **Status:** PROPOSAL-ONLY — AEOLUS decides what this means; WATT owns the power-system reading.
**Question:** Can weather data REFUTE the supply-side reading of PJM's 9/16–9/17 emergency? And was the 9/1–9/3 heat worse than mid-July?
**Scope:** weather only. PJM load, outage and interchange figures in this memo are **WATT's figures, repeated as given — not checked here.**

---

## 0. Answers in plain words (details below)

**(A) Was 9/1–9/3 hotter than mid-July?** Across PJM as a whole the actual heat was **about the same**. The 3-day cooling-degree-day totals match exactly (51.0 vs 51.0 per station, 7/14–16 vs 9/1–3). September had slightly warmer nights and more humidity (Tmin +1.2°F, dew point +1.1°F). July had slightly hotter afternoons (Tmax +1.2°F, peak heat index 109 vs 106). **Relative to normal for the time of year, September was about 1.7× as abnormal**: +9.4 vs +5.5 CDD a day above normal (3-day like-for-like). September also lasted longer (5 warm nights in a row vs 1) and put heat headlines on more of the map (653 vs 392 NWS zone-days). But the heat sat in different places. September was hottest in **western and southern PJM**: the Ohio Valley, Chicago, West Virginia and Virginia (western stations averaged 93.0°F highs vs 90.1°F in the east; Philadelphia reached only 77°F on 9/2). July's afternoon heat was higher in the **eastern load centres**, DC, Baltimore, Philadelphia and New Jersey: eastern stations averaged 93.7°F highs vs 90.1°F in September. *Confidence: HIGH on the station facts, MEDIUM on "about the same for load" — this is a simple average of airport stations, not PJM's load-weighted temperature. What would change it: PJM's own load-weighted temperature or temperature-humidity index for the peak hour showing a gap of ≥2°F either way.*

**(B) Was there a real heat event over PJM on 9/16–9/17?** **Warm, but not a heat event.** Days and nights were well above normal: Tmax +7.4°F, Tmin +9.0°F, CDD +156%. But **the absolute heat was low**: 10.5 CDD per station-day, about 62% of the July or early-September episodes (16.5–17.0). No station reached 95°F. The highest heat index was 98°F (CVG). **The NWS issued zero heat headlines anywhere in the PJM footprint.** **Neighbours to the south and west were clearly hotter.** Nashville, Memphis, St. Louis and Indianapolis ran 91–99°F (+13 to +19°F above normal). The 7-station neighbour average ran 17.5 CDD, 7 per day more than PJM. NWS heat advisories covered Tennessee, Kentucky (Louisville and Paducah areas), Missouri, southern and central Illinois, southern Indiana, Arkansas, Mississippi, northern Alabama, Oklahoma and Texas. The **Carolinas were NOT materially hotter** (CLT/RDU 86–93°F, dry, no headlines). *Confidence: HIGH that the weather cannot explain a 9/16–9/17 emergency on demand alone. The data is consistent with "above-normal temperatures + exports to hotter regions" and does not refute a supply-side reading. What would change it: a load-weighted PJM temperature-humidity index well above these airport readings (not expected: all 11 stations agree), or interchange data showing PJM was NOT exporting into MISO or TVA on those afternoons (WATT to check).*

---

## 1. Method

| Item | Basis |
|---|---|
| Daily Tmax / Tmin | **NOAA NCEI Access Data Service, GHCN-Daily** (`dataset=daily-summaries`, `dataTypes=TMAX,TMIN`, `units=standard`), pulled 2026-09-28 ~20:00 EDT, window 6/28–9/22. HTTP 200, complete for every station and day, **except IAD 9/17–9/18: TMAX/TMIN missing in GHCND** (checked: the other elements are present, so this is a sensor gap and not a publishing delay). IAD is left out of those two days' averages rather than filled. IEM's daily summary gives IAD 9/17 max = 87°F, min = none (this is a secondary source, shown only for context). |
| Normals | **NCEI `normals-daily` 1991–2020**: `DLY-TMAX-NORMAL`, `DLY-TMIN-NORMAL`, `DLY-CLDD-NORMAL` (base 65°F). Complete for all 18 stations. |
| CDD | `max(0, (Tmax+Tmin)/2 − 65)` per station-day. This is the NCEI method, but NCEI's own CDD normals are rounded to whole degrees. |
| Dew point, heat index, wet-bulb | **Iowa Environmental Mesonet ASOS archive** (`cgi-bin/request/asos.py`, `report_type=3` = hourly METAR only, `data=tmpf,dwpf,relh,feel`). Hours are grouped into **local standard time days** to match GHCND. Heat index = IEM `feel`. Wet-bulb (Tw) = Stull (2011) formula from temperature and RH, **computed by me, not an observed value**. Hourly readings slightly under-read the true peak, so max HI / Td / Tw are **lower bounds**. Every station-day had 23–24 hourly readings. |
| Heat headlines | **IEM NWS VTEC archive** (`cgi-bin/request/gis/watchwarn.py?accept=csv&limitps=yes`). Heat Advisory `HT.Y` = 25,271 product rows. Extreme Heat Warning `XH.W` = 5,345 rows. Legacy `EH.W/EH.Y`, `XH.Y` and `EH.A` returned 0 rows. For each event and zone, the latest product update gives the in-effect window. A zone counts for a date if that window overlaps **12:00–20:00 EDT** that day. |
| PJM footprint (approximation) | NWS zones in DC, DE, MD, NJ, PA, OH, WV, VA, plus IL zones under WFO LOT (ComEd), IN under IWX (AEP I&M, but this also picks up some NIPSCO/MISO counties), KY under ILN/JKL/RLX (Duke KY, EKPC, AEP Kentucky Power), and NC under AKQ (Dominion NC). **Zone counts are not weighted by area or population.** A zone under both an advisory and a warning on the same day counts twice (small effect). |
| Averages | **Simple unweighted station means** ("PJM-11", "NBR-7"). **These are not load-weighted.** |

**Stations (GHCND IDs checked against NCEI station names):**

| Set | Station (GHCND) | PJM zone / neighbour BA |
|---|---|---|
| PJM-East-6 | DCA USW00013743 · IAD USW00093738 · BWI USW00093721 · PHL USW00013739 · EWR USW00014734 · RIC USW00013740 | Pepco/Dominion · BGE · PECO · PSEG · Dominion |
| PJM-West-5 | PIT USW00094823 · CLE USW00014820 · CMH USW00014821 · CVG USW00093814 · ORD USW00094846 | Duquesne · FirstEnergy · AEP · Duke OH/KY · ComEd |
| NBR-7 (south/west) | BNA USW00013897 · MEM USW00013893 · ATL USW00013874 · CLT USW00013881 · RDU USW00013722 · STL USW00013994 · IND USW00093819 | TVA · TVA/MISO-S · Southern · Duke Carolinas · Duke Progress · MISO (Ameren) · MISO (AES Indiana) |

---

## 2. Episode summary (primary: GHCND + normals; HI/Td/Tw from IEM ASOS hourly)

| Episode | Set | days | mean Tmax | mean ΔTmax | mean Tmin | mean ΔTmin | CDD/stn-day | normal CDD/stn-day | CDD anomaly/stn-day | CDD anomaly % | peak HI (stn) | mean daily-max Td | mean daily-max Tw | stn-days Tmax≥95 | stn-days Tmin≥75 | stn-days HI≥100 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| JUL-A 7/01-7/05 | PJM-11 | 5 | 95.3 | +9.5 | 74.2 | +8.2 | 19.7 | 10.9 | +8.9 | +82% | 114 (RIC) | 74.9 | 79.1 | 36/55 | 26/55 | 40/55 |
| JUL-A 7/01-7/05 | NBR-7 | 5 | 95.1 | +6.3 | 75.1 | +5.5 | 20.1 | 14.2 | +5.9 | +41% | 108 (RDU) | 73.7 | 78.7 | 21/35 | 22/35 | 29/35 |
| JUL 7/14-7/17 | PJM-11 | 4 | 91.8 | +5.6 | 71.2 | +4.4 | 16.5 | 11.5 | +5.0 | +43% | 109 (PHL) | 71.7 | 76.5 | 11/44 | 11/44 | 15/44 |
| JUL 7/14-7/17 | NBR-7 | 4 | 91.5 | +2.3 | 73.0 | +2.9 | 17.3 | 14.7 | +2.6 | +17% | 105 (RDU) | 72.8 | 76.6 | 4/28 | 8/28 | 7/28 |
| SEP-A 8/31-9/04 | PJM-11 | 5 | 89.9 | +7.9 | 72.2 | +9.7 | 16.0 | 7.6 | +8.4 | +110% | 106 (RIC) | 73.1 | 76.6 | 13/55 | 8/55 | 17/55 |
| SEP-A 8/31-9/04 | NBR-7 | 5 | 97.5 | +11.7 | 75.5 | +9.3 | 21.5 | 11.1 | +10.4 | +93% | 113 (RDU) | 72.3 | 77.8 | 31/35 | 24/35 | 28/35 |
| SEP-A core 9/01-9/03 | PJM-11 | 3 | 91.4 | +9.4 | 72.6 | +10.1 | 17.0 | 7.6 | +9.3 | +122% | 106 (RIC) | 73.5 | 77.5 | 11/33 | 6/33 | 14/33 |
| SEP-A core 9/01-9/03 | NBR-7 | 3 | 97.9 | +12.1 | 76.2 | +10.0 | 22.0 | 11.1 | +11.0 | +99% | 108 (RDU) | 72.2 | 77.6 | 20/21 | 17/21 | 19/21 |
| SEP-B 9/15-9/18 | PJM-11 | 4 | 83.0 | +5.8 | 64.4 | +6.8 | 8.7 | 4.1 | +4.6 | +111% | 98 (CVG) | 68.1 | 71.3 | 0/42 | 0/42 | 0/44 |
| SEP-B 9/15-9/18 | NBR-7 | 4 | 93.5 | +12.1 | 71.9 | +10.7 | 17.7 | 7.1 | +10.6 | +150% | 107 (MEM) | 69.9 | 75.4 | 13/28 | 12/28 | 14/28 |
| SEP-B core 9/16-9/17 | PJM-11 | 2 | 84.5 | +7.4 | 66.5 | +9.0 | 10.5 | 4.1 | +6.4 | +156% | 98 (CVG) | 70.3 | 73.4 | 0/21 | 0/21 | 0/22 |
| SEP-B core 9/16-9/17 | NBR-7 | 2 | 93.4 | +12.0 | 71.6 | +10.4 | 17.5 | 7.0 | +10.5 | +150% | 105 (STL) | 69.3 | 75.2 | 5/14 | 7/14 | 7/14 |

*Units: °F; CDD in °F-days per station-day (base 65); "normal" = NCEI 1991–2020 daily normal; Δ = observed − normal. HI/Td/Tw = daily maxima of hourly METARs (lower bounds). JUL-A (7/1–7/5) is included as the 7/3 EEA-2 reference.*


### 2a. Like-for-like 3-day windows, split into eastern and western PJM

| Window | Sub-set | mean Tmax | ΔTmax | mean Tmin | ΔTmin | CDD/stn-day | nCDD | CDD sum (stn-avg, window) | nCDD sum | mean daily-max Td | peak HI |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 7/01-7/05 | PJM-East-6 | 98.5 | +11.1 | 75.8 | +8.1 | 22.1 | 12.5 | 110.7 | 62.3 | 75.5 | 114 (RIC) |
| 7/01-7/05 | PJM-West-5 | 91.4 | +7.6 | 72.3 | +8.4 | 16.9 | 9.0 | 84.3 | 44.8 | 74.0 | 107 (CLE) |
| 7/01-7/05 | PJM-11 | 95.3 | +9.5 | 74.2 | +8.2 | 19.7 | 10.9 | 98.7 | 54.4 | 74.9 | 114 (RIC) |
| 7/01-7/05 | NBR-7 | 95.1 | +6.3 | 75.1 | +5.5 | 20.1 | 14.2 | 100.4 | 71.1 | 73.7 | 108 (RDU) |
| 7/14-7/16 | PJM-East-6 | 93.7 | +5.7 | 72.2 | +3.6 | 17.9 | 13.3 | 53.8 | 40.0 | 72.8 | 109 (PHL) |
| 7/14-7/16 | PJM-West-5 | 91.3 | +7.1 | 70.5 | +5.8 | 15.9 | 9.4 | 47.7 | 28.2 | 71.9 | 102 (CMH) |
| 7/14-7/16 | PJM-11 | 92.6 | +6.3 | 71.4 | +4.6 | 17.0 | 11.5 | 51.0 | 34.6 | 72.4 | 109 (PHL) |
| 7/14-7/16 | NBR-7 | 90.7 | +1.5 | 72.3 | +2.2 | 16.5 | 14.7 | 49.5 | 44.1 | 72.2 | 103 (RDU) |
| 7/14-7/17 | PJM-East-6 | 92.7 | +4.7 | 72.1 | +3.5 | 17.4 | 13.3 | 69.7 | 53.3 | 71.8 | 109 (PHL) |
| 7/14-7/17 | PJM-West-5 | 90.8 | +6.6 | 70.2 | +5.4 | 15.5 | 9.4 | 61.9 | 37.6 | 71.5 | 102 (CMH) |
| 7/14-7/17 | PJM-11 | 91.8 | +5.6 | 71.2 | +4.4 | 16.5 | 11.5 | 66.1 | 46.2 | 71.7 | 109 (PHL) |
| 7/14-7/17 | NBR-7 | 91.5 | +2.3 | 73.0 | +2.9 | 17.3 | 14.7 | 69.1 | 58.9 | 72.8 | 105 (RDU) |
| 9/01-9/03 | PJM-East-6 | 90.1 | +6.8 | 71.9 | +7.7 | 16.0 | 8.9 | 48.0 | 26.7 | 73.9 | 106 (RIC) |
| 9/01-9/03 | PJM-West-5 | 93.0 | +12.6 | 73.3 | +12.8 | 18.2 | 6.1 | 54.5 | 18.4 | 73.0 | 103 (ORD) |
| 9/01-9/03 | PJM-11 | 91.4 | +9.4 | 72.6 | +10.1 | 17.0 | 7.6 | 51.0 | 22.9 | 73.5 | 106 (RIC) |
| 9/01-9/03 | NBR-7 | 97.9 | +12.1 | 76.2 | +10.0 | 22.0 | 11.1 | 66.1 | 33.3 | 72.2 | 108 (RDU) |
| 9/16-9/17 | PJM-East-6 | 84.9 | +6.3 | 63.8 | +4.2 | 9.4 | 5.0 | 18.7 | 10.0 | 69.2 | 93 (RIC) |
| 9/16-9/17 | PJM-West-5 | 84.0 | +8.5 | 69.5 | +14.2 | 11.8 | 3.1 | 23.5 | 6.2 | 71.6 | 98 (CVG) |
| 9/16-9/17 | PJM-11 | 84.5 | +7.4 | 66.5 | +9.0 | 10.5 | 4.1 | 21.0 | 8.2 | 70.3 | 98 (CVG) |
| 9/16-9/17 | NBR-7 | 93.4 | +12.0 | 71.6 | +10.4 | 17.5 | 7.0 | 35.0 | 14.0 | 69.3 | 105 (STL) |

**Reading (A), from the tables above:**

| Dimension | 7/14–7/16 (EEA-1, 159,046 MW) | 9/01–9/03 (EEA-1 ×3, ~152,518 MW) | Worse |
|---|---|---|---|
| PJM-11 3-day CDD total | **51.0** | **51.0** | tie |
| CDD vs normal (per station-day) | +5.5 (17.0 vs 11.5) | **+9.4** (17.0 vs 7.6) | Sep (anomaly) |
| Mean Tmax / peak-day mean Tmax | **92.6** / **94.4** (7/15) | 91.4 / 92.9 (9/1) | Jul, by ~1.2–1.5°F |
| Mean Tmin (overnight) | 71.4 | **72.6** | Sep, by 1.2°F |
| Mean daily-max dew point | 72.4 | **73.5** | Sep, by 1.1°F |
| Mean daily-max wet-bulb (derived) | 76.5 (4-day) | **77.5** | Sep, by ~1°F |
| Peak heat index | **109** (PHL 7/15–16) | 106 (RIC 9/3) | Jul |
| Station-days Tmax ≥95 | 11/44 (4-day) | 11/33 | Sep, by rate |
| Duration: consecutive days with PJM-11 mean ΔTmin ≥ +7°F | 1 (7/16) | **5** (8/31–9/4) | Sep |
| Duration: days with PJM-11 mean Tmax ≥ 90°F in the window ±2d | 3 (7/14–7/16) + 7/18 | 2 of 3 (9/1, 9/3); 9/2 = 89.3 | Jul, slightly |
| Breadth: PJM-footprint NWS heat zone-days (HT.Y + XH.W) | 392 (79 / 245 / 68) | **653** (128 / 238 / 287) | Sep |
| Where it was | East-heavy in absolute heat (East-6 Tmax 93.7) | **West-heavy** (West-5 Tmax 93.0, Δ +12.6; PHL only 77 on 9/2) | different geography |
| Weekday? | Tue–Thu | Tue–Thu (Labor Day was 9/7) | — |

*Hypothesis only; the load numbers belong to WATT: PJM-11 CDD on the peak days was 18.1–18.5 in July and 16.0–18.2 in September, and peak load was 159.0 vs 152.5 GW. That is roughly in proportion, so **weather does not rule out demand as the driver for 9/1–9/3.** The lower September peak fits the heat being centred in the less load-dense west. This is not tested here; PJM's zonal load would test it.*

---

## 3. Daily PJM-11 vs neighbour (NBR-7) series

**Mid-July:**

| Date | PJM-11 mean Tmax | ΔTmax | mean Tmin | ΔTmin | CDD | nCDD | NBR-7 mean Tmax | ΔTmax | ΔTmin | CDD | nCDD | NBR−PJM ΔTmax gap |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 07-12 | 85.2 | -1.1 | 68.5 | +1.8 | 11.9 | 11.5 | 88.0 | -1.2 | +2.0 | 15.0 | 14.6 | -0.1 |
| 07-13 | 87.5 | +1.3 | 66.4 | -0.4 | 12.0 | 11.5 | 86.0 | -3.2 | +1.6 | 13.9 | 14.7 | -4.5 |
| 07-14 | 91.1 | +4.8 | 67.8 | +1.0 | 14.5 | 11.5 | 88.4 | -0.8 | +1.1 | 14.8 | 14.7 | -5.6 |
| 07-15 | 94.4 | +8.1 | 71.8 | +5.0 | 18.1 | 11.5 | 91.0 | +1.8 | +1.5 | 16.3 | 14.7 | -6.3 |
| 07-16 | 92.4 | +6.1 | 74.6 | +7.8 | 18.5 | 11.5 | 92.7 | +3.5 | +4.0 | 18.4 | 14.7 | -2.6 |
| 07-17 | 89.5 | +3.3 | 70.6 | +3.7 | 15.1 | 11.5 | 94.0 | +4.8 | +5.0 | 19.6 | 14.7 | +1.5 |
| 07-18 | 91.1 | +4.9 | 71.7 | +4.8 | 16.4 | 11.5 | 94.7 | +5.5 | +5.9 | 20.4 | 14.7 | +0.6 |
| 07-19 | 83.5 | -2.7 | 68.8 | +1.9 | 11.1 | 11.5 | 92.4 | +3.3 | +4.9 | 18.7 | 14.6 | +6.0 |

**Late August to mid-September.** The last column is the neighbour Tmax anomaly minus PJM's (positive = the neighbours were more anomalous):

| Date | PJM-11 mean Tmax | ΔTmax | mean Tmin | ΔTmin | CDD | nCDD | NBR-7 mean Tmax | ΔTmax | ΔTmin | CDD | nCDD | NBR−PJM ΔTmax gap |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 08-29 | 83.1 | +0.2 | 63.5 | -0.1 | 8.3 | 8.5 | 88.7 | +2.0 | +0.5 | 13.2 | 12.0 | +1.8 |
| 08-30 | 85.6 | +3.0 | 66.4 | +3.1 | 11.0 | 8.3 | 91.4 | +4.9 | +3.5 | 15.9 | 11.9 | +1.9 |
| 08-31 | 86.5 | +4.1 | 71.2 | +8.1 | 13.9 | 8.0 | 95.4 | +9.1 | +5.1 | 18.6 | 11.6 | +5.0 |
| 09-01 | 92.9 | +10.7 | 73.5 | +10.7 | 18.2 | 7.7 | 97.3 | +11.2 | +8.8 | 21.3 | 11.4 | +0.5 |
| 09-02 | 89.3 | +7.3 | 72.6 | +10.1 | 16.0 | 7.7 | 98.0 | +12.1 | +10.2 | 22.2 | 11.0 | +4.8 |
| 09-03 | 92.0 | +10.3 | 71.5 | +9.3 | 16.8 | 7.5 | 98.4 | +12.8 | +10.9 | 22.6 | 10.9 | +2.5 |
| 09-04 | 88.7 | +7.3 | 71.9 | +9.9 | 15.3 | 7.2 | 98.4 | +13.0 | +11.2 | 22.6 | 10.7 | +5.8 |
| 09-05 | 83.1 | +1.9 | 68.2 | +6.5 | 10.6 | 6.8 | 99.0 | +13.9 | +10.2 | 22.3 | 10.3 | +11.9 |
| 09-06 | 81.2 | +0.3 | 63.3 | +1.9 | 7.2 | 6.7 | 91.1 | +6.3 | +6.8 | 16.5 | 10.1 | +6.0 |
| 09-07 | 81.7 | +1.2 | 61.6 | +0.6 | 6.7 | 6.5 | 87.7 | +3.2 | +4.0 | 13.2 | 9.7 | +2.0 |
| 09-08 | 85.1 | +4.9 | 61.8 | +1.1 | 8.5 | 6.1 | 91.0 | +6.8 | +3.4 | 14.4 | 9.7 | +1.9 |
| 09-09 | 88.1 | +8.2 | 68.5 | +8.1 | 13.3 | 5.8 | 92.0 | +8.1 | +6.5 | 16.3 | 9.3 | -0.1 |
| 09-10 | 85.9 | +6.3 | 70.3 | +10.3 | 13.1 | 5.7 | 90.9 | +7.2 | +8.9 | 16.7 | 8.7 | +0.9 |
| 09-11 | 81.3 | +2.0 | 65.7 | +6.1 | 8.5 | 5.5 | 91.0 | +7.7 | +7.8 | 16.1 | 8.7 | +5.7 |
| 09-12 | 81.5 | +2.6 | 66.1 | +6.8 | 8.8 | 5.2 | 89.1 | +6.2 | +9.1 | 15.6 | 8.6 | +3.6 |
| 09-13 | 85.4 | +6.8 | 68.1 | +9.2 | 11.7 | 4.8 | 91.1 | +8.5 | +7.7 | 15.7 | 8.0 | +1.7 |
| 09-14 | 76.3 | -1.9 | 58.5 | +0.1 | 3.3 | 4.7 | 90.4 | +8.2 | +7.3 | 14.9 | 7.7 | +10.0 |
| 09-15 | 81.1 | +3.3 | 56.9 | -1.2 | 4.1 | 4.5 | 92.6 | +10.6 | +9.2 | 16.8 | 7.6 | +7.3 |
| 09-16 | 84.1 | +6.7 | 63.8 | +6.1 | 9.0 | 4.2 | 92.4 | +10.9 | +10.3 | 17.1 | 7.0 | +4.1 |
| 09-17 | 84.9 | +8.1 | 69.5 | +12.1 | 12.2 | 4.0 | 94.4 | +13.2 | +10.5 | 17.9 | 7.0 | +5.1 |
| 09-18 | 81.8 | +5.4 | 68.0 | +11.0 | 9.9 | 3.8 | 94.4 | +13.6 | +12.7 | 18.9 | 6.7 | +8.2 |
| 09-19 | 78.1 | +1.9 | 64.8 | +8.4 | 6.5 | 3.7 | 93.6 | +13.1 | +12.7 | 18.2 | 6.4 | +11.2 |
| 09-20 | 79.4 | +3.6 | 67.0 | +11.0 | 8.2 | 3.3 | 92.4 | +12.3 | +11.3 | 16.7 | 6.0 | +8.8 |
| 09-21 | 71.5 | -3.9 | 61.5 | +5.9 | 2.8 | 3.2 | 87.0 | +7.3 | +10.4 | 13.6 | 5.9 | +11.2 |

**What the September series shows:** starting **9/14**, the neighbour Tmax anomaly ran **4–11°F above PJM's every day through 9/21**. On 9/16–9/17 it was +10.9/+13.2 vs +6.7/+8.1. The neighbour heat **kept building after PJM's event** (9/18–9/20: neighbours +12 to +14°F above normal).

---

## 4. NWS heat headlines (IEM VTEC archive, primary-derived)

*Counts are of NWS forecast zones with a headline in effect at some point between 12:00 and 20:00 EDT. In the neighbour column, IL/IN/KY exclude the WFOs assigned to PJM in §1. States checked: TN GA NC SC AL MS KY MO AR IL IN LA TX MI WI MN IA NY. OK and KS appear in the 9/15–9/17 WFO detail below. Different WFOs use different heat index thresholds for issuing a headline, so treat these as counts, not a uniform intensity scale.*

| Date (EDT afternoon) | PJM-footprint HT.Y zones | PJM XH.W zones | PJM WFOs issuing | Neighbour/other states with headlines (HT.Y / XH.W zone counts) |
|---|---|---|---|---|
| 07-01 | 82 | 72 | AKQ,BGM,CTP,LWX,OKX,PHI,RNK | GA 21/0 · AL 10/0 · MS 16/17 · AR 6/1 · LA 38/3 · WI 22/0 · MN 1/0 · IA 15/1 · NY 21/67 |
| 07-02 | 63 | 166 | AKQ,BGM,CTP,LWX,OKX,PBZ,PHI,RNK | TN 0/21 · GA 45/10 · NC 44/0 · SC 16/0 · AL 10/0 · MS 17/4 · MO 0/2 · AR 8/22 · WI 8/0 · MN 4/0 · NY 21/67 |
| 07-03 | 61 | 195 | AKQ,BGM,CTP,IWX,LOT,LWX,OKX,PBZ,PHI,RNK | TN 24/0 · GA 59/0 · NC 55/20 · SC 31/0 · AL 40/0 · MS 51/0 · MO 2/0 · AR 44/0 · IN 3/0 · LA 9/0 · MI 27/0 · NY 29/59 |
| 07-04 | 154 | 195 | AKQ,BGM,CLE,CTP,ILN,IWX,JKL,LWX,OKX,PBZ,PHI,RNK | TN 53/0 · GA 59/0 · NC 54/21 · SC 33/0 · AL 50/0 · MS 51/0 · KY 71/0 · MO 49/0 · AR 47/0 · IL 62/0 · IN 63/0 · LA 9/0 · TX 10/0 · NY 10/12 |
| 07-05 | 125 | 0 | AKQ,LWX,PHI | GA 53/0 · NC 41/0 · SC 11/0 · MS 3/0 · AR 8/0 |
| 07-13 | 0 | 0 | — | MI 30/15 · WI 34/16 · MN 3/76 |
| 07-14 | 79 | 0 | BGM,CLE,CTP,IWX,OKX | MI 76/15 · WI 58/16 · MN 14/68 · IA 3/0 · NY 80/0 |
| 07-15 | 230 | 15 | AKQ,CLE,CTP,ILN,IWX,LWX,OKX,PBZ,PHI | IL 3/0 · IN 16/0 · MI 46/0 · WI 49/11 · MN 38/41 · IA 5/0 · NY 20/0 |
| 07-16 | 68 | 0 | IWX,LWX,PHI | IN 16/0 · MN 4/7 |
| 07-17 | 9 | 0 | AKQ | GA 30/0 · NC 42/0 · SC 14/0 · WI 17/0 · MN 54/7 · IA 11/0 |
| 07-18 | 72 | 0 | AKQ,LWX,PHI | GA 61/0 · NC 56/0 · SC 36/0 · MS 46/0 · KY 19/0 · MO 35/0 · AR 28/0 · IL 27/0 · LA 44/0 · IA 10/0 |
| 08-31 | 0 | 0 | — | TN 12/0 · MS 22/0 · KY 22/0 · MO 112/0 · AR 42/0 · IL 72/0 · IN 6/0 · LA 7/0 · IA 31/0 |
| 09-01 | 128 | 0 | CLE,ILN,IWX,LOT,PHI,RLX | TN 12/0 · MS 32/0 · KY 71/22 · MO 115/11 · AR 44/0 · IL 84/19 · IN 68/6 · LA 9/0 · MI 6/0 · IA 39/0 |
| 09-02 | 238 | 0 | AKQ,CLE,ILN,IWX,JKL,LOT,LWX,PBZ,RLX,RNK | TN 74/0 · GA 10/0 · NC 44/0 · SC 7/0 · AL 50/0 · MS 69/0 · KY 49/22 · MO 102/13 · AR 47/0 · IL 56/63 · IN 62/6 · LA 9/0 · TX 12/0 · MI 25/0 · IA 37/13 |
| 09-03 | 286 | 1 | AKQ,CLE,CTP,ILN,IWX,JKL,LOT,LWX,PBZ,PHI,RLX,RNK | TN 90/0 · GA 10/0 · NC 53/0 · SC 7/0 · AL 50/0 · MS 69/0 · KY 49/22 · MO 73/79 · AR 47/0 · IL 4/80 · IN 62/6 · LA 9/0 · TX 33/0 · MI 6/0 · IA 39/13 |
| 09-04 | 218 | 0 | AKQ,ILN,IWX,JKL,LOT,RLX,RNK | TN 90/0 · GA 90/0 · NC 63/0 · SC 14/0 · AL 50/0 · MS 58/0 · KY 49/22 · MO 36/113 · AR 47/0 · IL 4/80 · IN 62/6 · LA 9/0 · TX 9/0 · WI 1/0 · MN 7/0 · IA 63/13 |
| 09-05 | 3 | 0 | LOT | TN 90/0 · GA 101/0 · NC 39/0 · SC 49/0 · AL 50/0 · MS 58/0 · KY 49/22 · MO 2/113 · AR 92/3 · IL 1/80 · IN 43/6 · LA 9/0 · TX 21/0 · IA 50/13 |
| 09-14 | 0 | 0 | — | TN 21/0 · MS 69/0 · KY 4/0 · MO 35/0 · AR 71/0 · LA 26/0 · TX 114/0 |
| 09-15 | 0 | 0 | — | TN 57/0 · AL 9/0 · MS 54/0 · KY 53/0 · MO 64/0 · AR 71/0 · IL 27/0 · IN 16/0 · LA 26/0 · TX 81/0 |
| 09-16 | 0 | 0 | — | TN 57/0 · AL 11/0 · MS 54/0 · KY 53/0 · MO 68/0 · AR 71/0 · IL 39/0 · IN 16/0 · LA 26/0 · TX 50/0 |
| 09-17 | 0 | 0 | — | TN 57/0 · AL 11/0 · MS 22/0 · KY 53/0 · MO 68/0 · AR 38/0 · IL 45/0 · IN 16/0 |
| 09-18 | 0 | 0 | — | TN 57/0 · AL 11/0 · MS 22/0 · KY 41/0 · MO 68/0 · AR 20/0 · IL 33/0 · IN 9/0 |
| 09-19 | 0 | 0 | — | TN 57/0 · AL 40/0 · MS 54/0 · KY 39/0 · MO 64/0 · AR 20/0 · IL 27/0 · IN 8/0 |

**Across the days tabulated (7/1–7/20 and 8/28–9/20), 471 distinct PJM-footprint zones carried a heat headline at some point.** On 9/3, 287 of them were active. On 7/15, 245 were.

**PJM zones by state:**

| Date | Zones by state |
|---|---|
| 7/14 | PA 33 · IN 21 · OH 16 · NJ 9 |
| 7/15 | OH 61 · PA 47 · VA 34 · NJ 30 · IN 27 · MD 27 · WV 14 · DE 4 · DC 1 |
| 7/16 | MD 22 · VA 16 · IN 12 · WV 7 · PA 5 · NJ 4 · DC 1 · DE 1 |
| 9/1 | OH 58 · IL 22 · WV 17 · KY 16 · IN 5 · PA 5 · NJ 4 · DE 1 |
| 9/2 | OH 78 · VA 56 · WV 33 · KY 31 · IL 17 · PA 9 · NC 9 · IN 5 |
| 9/3 | OH 66 · VA 62 · KY 49 · WV 30 · PA 26 · IN 14 · IL 12 · NC 9 · MD 8 · NJ 8 · DE 3 |
| 9/16, 9/17 | **none** |

**Neighbour heat headlines on 9/15–9/17, by WFO (zone counts, HT.Y; no XH.W):**

| WFO (area) | 9/15 | 9/16 | 9/17 | Balancing area (approximate) |
|---|---|---|---|---|
| OHX Nashville (TN) | 33 | 33 | 33 | TVA |
| MEG Memphis (TN/MS/AR/MO) | 55 | 55 | 55 | TVA / MISO-South |
| HUN Huntsville (AL/TN) | 12 | 14 | 14 | TVA |
| LMK Louisville (KY/IN) | 41 | 41 | 41 | LG&E-KU / MISO (S. Indiana) |
| PAH Paducah (KY/IL/IN/MO) | 58 | 58 | 58 | TVA / MISO |
| LSX St. Louis (MO/IL) | 25 | 35 | 35 | MISO (Ameren) |
| ILX Lincoln (central IL) | 0 | 6 | 12 | MISO (Ameren IL) |
| SGF Springfield (MO/KS) | 37 | 37 | 37 | SPP |
| LZK/JAN/SHV/TSA/OUN/ICT/FWD/HGX/EWX | many | many | fewer | MISO-South / SPP / ERCOT |
| **Carolinas (GSP, RAH, MHX, ILM, CAE, CHS), Atlanta (FFC)** | **0** | **0** | **0** | Duke / Santee / Southern |

---

## 5. Per-station tables

*Columns: Tmax/Tmin observed (GHCND) · nTmax/nTmin = 1991–2020 normal · Δ = anomaly · CDD / nCDD = observed / normal · max HI, max Td, max Tw = daily maxima of hourly readings · mean Td = daily mean dew point · n_obs = hourly METARs that day. "—" = missing in GHCND (IAD 9/17).*

### 5a. Mid-July, 7/14–7/17

| Stn | Date | Tmax | nTmax | ΔTmax | Tmin | nTmin | ΔTmin | CDD | nCDD | max HI | max Td | mean Td | max Tw | n_obs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DCA | 07-14 | 91 | 88.7 | +2.3 | 69 | 71.3 | -2.3 | 15.0 | 15 | 97 | 72 | 67.7 | 76.6 | 24 |
| DCA | 07-15 | 97 | 88.7 | +8.3 | 73 | 71.4 | +1.6 | 20.0 | 15 | 106 | 72 | 69.5 | 79.7 | 24 |
| DCA | 07-16 | 98 | 88.7 | +9.3 | 81 | 71.4 | +9.6 | 24.5 | 15 | 107 | 75 | 70.9 | 80.3 | 24 |
| DCA | 07-17 | 93 | 88.7 | +4.3 | 76 | 71.4 | +4.6 | 19.5 | 15 | 93 | 69 | 62.1 | 74.2 | 24 |
| IAD | 07-14 | 90 | 88.1 | +1.9 | 64 | 65.7 | -1.7 | 12.0 | 12 | 93 | 70 | 67.3 | 75.0 | 24 |
| IAD | 07-15 | 95 | 88.1 | +6.9 | 68 | 65.7 | +2.3 | 16.5 | 12 | 103 | 73 | 70.7 | 79.3 | 24 |
| IAD | 07-16 | 96 | 88.1 | +7.9 | 81 | 65.7 | +15.3 | 23.5 | 12 | 105 | 75 | 71.5 | 80.2 | 24 |
| IAD | 07-17 | 90 | 88.1 | +1.9 | 68 | 65.7 | +2.3 | 14.0 | 12 | 90 | 69 | 62.6 | 73.2 | 24 |
| BWI | 07-14 | 92 | 87.5 | +4.5 | 64 | 67.0 | -3.0 | 13.0 | 12 | 95 | 68 | 65.8 | 75.4 | 24 |
| BWI | 07-15 | 96 | 87.5 | +8.5 | 71 | 67.1 | +3.9 | 18.5 | 12 | 105 | 73 | 70.5 | 79.6 | 24 |
| BWI | 07-16 | 95 | 87.5 | +7.5 | 76 | 67.1 | +8.9 | 20.5 | 12 | 106 | 76 | 71.2 | 80.5 | 24 |
| BWI | 07-17 | 87 | 87.5 | -0.5 | 68 | 67.1 | +0.9 | 12.5 | 12 | 88 | 67 | 62.4 | 71.3 | 24 |
| PHL | 07-14 | 92 | 87.4 | +4.6 | 71 | 69.4 | +1.6 | 16.5 | 13 | 99 | 72 | 67.8 | 77.8 | 24 |
| PHL | 07-15 | 98 | 87.4 | +10.6 | 77 | 69.5 | +7.5 | 22.5 | 13 | 109 | 76 | 71.5 | 81.5 | 24 |
| PHL | 07-16 | 95 | 87.4 | +7.6 | 79 | 69.5 | +9.5 | 22.0 | 13 | 109 | 77 | 68.7 | 81.8 | 24 |
| PHL | 07-17 | 88 | 87.4 | +0.6 | 74 | 69.6 | +4.4 | 16.0 | 13 | 88 | 68 | 61.6 | 71.3 | 24 |
| EWR | 07-14 | 93 | 86.3 | +6.7 | 70 | 68.9 | +1.1 | 16.5 | 13 | 97 | 69 | 64.4 | 76.0 | 24 |
| EWR | 07-15 | 98 | 86.3 | +11.7 | 77 | 68.9 | +8.1 | 22.5 | 13 | 105 | 75 | 69.0 | 78.8 | 24 |
| EWR | 07-16 | 89 | 86.3 | +2.7 | 74 | 69.0 | +5.0 | 16.5 | 13 | 93 | 70 | 61.8 | 75.6 | 24 |
| EWR | 07-17 | 88 | 86.3 | +1.7 | 71 | 69.0 | +2.0 | 14.5 | 13 | 85 | 65 | 55.3 | 69.1 | 24 |
| RIC | 07-14 | 88 | 90.0 | -2.0 | 65 | 69.1 | -4.1 | 11.5 | 15 | 90 | 68 | 65.4 | 72.7 | 24 |
| RIC | 07-15 | 91 | 90.0 | +1.0 | 68 | 69.1 | -1.1 | 14.5 | 15 | 98 | 74 | 69.1 | 78.3 | 24 |
| RIC | 07-16 | 93 | 90.0 | +3.0 | 71 | 69.2 | +1.8 | 17.0 | 15 | 105 | 76 | 73.6 | 80.2 | 24 |
| RIC | 07-17 | 92 | 89.9 | +2.1 | 75 | 69.2 | +5.8 | 18.5 | 15 | 98 | 75 | 71.4 | 77.1 | 24 |
| PIT | 07-14 | 88 | 82.7 | +5.3 | 68 | 63.0 | +5.0 | 13.0 | 8 | 92 | 69 | 67.2 | 74.4 | 24 |
| PIT | 07-15 | 91 | 82.7 | +8.3 | 72 | 63.0 | +9.0 | 16.5 | 8 | 96 | 73 | 70.2 | 77.4 | 24 |
| PIT | 07-16 | 89 | 82.7 | +6.3 | 69 | 63.0 | +6.0 | 14.0 | 8 | 94 | 74 | 68.4 | 76.8 | 24 |
| PIT | 07-17 | 83 | 82.6 | +0.4 | 63 | 63.1 | -0.1 | 8.0 | 8 | 82 | 63 | 59.5 | 67.5 | 24 |
| CLE | 07-14 | 90 | 82.9 | +7.1 | 60 | 64.5 | -4.5 | 10.0 | 9 | 93 | 68 | 63.4 | 74.8 | 24 |
| CLE | 07-15 | 93 | 82.9 | +10.1 | 70 | 64.5 | +5.5 | 16.5 | 9 | 101 | 74 | 70.7 | 78.7 | 24 |
| CLE | 07-16 | 84 | 82.9 | +1.1 | 71 | 64.5 | +6.5 | 12.5 | 9 | 85 | 76 | 64.3 | 76.8 | 24 |
| CLE | 07-17 | 86 | 82.8 | +3.2 | 62 | 64.5 | -2.5 | 9.0 | 9 | 86 | 68 | 61.8 | 71.0 | 24 |
| CMH | 07-14 | 92 | 85.1 | +6.9 | 69 | 65.7 | +3.3 | 15.5 | 10 | 94 | 70 | 67.6 | 74.9 | 24 |
| CMH | 07-15 | 94 | 85.1 | +8.9 | 70 | 65.7 | +4.3 | 17.0 | 10 | 99 | 70 | 68.8 | 77.2 | 24 |
| CMH | 07-16 | 94 | 85.1 | +8.9 | 74 | 65.7 | +8.3 | 19.0 | 10 | 102 | 74 | 71.0 | 78.7 | 24 |
| CMH | 07-17 | 94 | 85.0 | +9.0 | 71 | 65.7 | +5.3 | 17.5 | 10 | 100 | 72 | 65.4 | 77.0 | 24 |
| CVG | 07-14 | 90 | 85.8 | +4.2 | 72 | 66.3 | +5.7 | 16.0 | 11 | 90 | 70 | 66.7 | 73.4 | 24 |
| CVG | 07-15 | 90 | 85.8 | +4.2 | 68 | 66.3 | +1.7 | 14.0 | 11 | 93 | 69 | 67.1 | 74.5 | 24 |
| CVG | 07-16 | 92 | 85.7 | +6.3 | 70 | 66.3 | +3.7 | 16.0 | 11 | 98 | 73 | 70.4 | 77.4 | 24 |
| CVG | 07-17 | 92 | 85.7 | +6.3 | 74 | 66.3 | +7.7 | 18.0 | 11 | 101 | 76 | 73.2 | 79.0 | 24 |
| ORD | 07-14 | 96 | 84.5 | +11.5 | 74 | 64.1 | +9.9 | 20.0 | 9 | 100 | 75 | 69.5 | 77.8 | 24 |
| ORD | 07-15 | 95 | 84.5 | +10.5 | 76 | 64.2 | +11.8 | 20.5 | 9 | 101 | 74 | 71.6 | 78.1 | 24 |
| ORD | 07-16 | 91 | 84.4 | +6.6 | 75 | 64.2 | +10.8 | 18.0 | 9 | 95 | 70 | 65.4 | 75.7 | 24 |
| ORD | 07-17 | 92 | 84.4 | +7.6 | 75 | 64.2 | +10.8 | 18.5 | 9 | 99 | 72 | 70.1 | 77.8 | 24 |
| BNA | 07-14 | 88 | 89.4 | -1.4 | 72 | 69.7 | +2.3 | 15.0 | 15 | 92 | 73 | 70.2 | 75.5 | 24 |
| BNA | 07-15 | 88 | 89.4 | -1.4 | 73 | 69.7 | +3.3 | 15.5 | 15 | 93 | 72 | 70.8 | 75.6 | 24 |
| BNA | 07-16 | 90 | 89.4 | +0.6 | 74 | 69.7 | +4.3 | 17.0 | 15 | 96 | 73 | 71.7 | 77.1 | 24 |
| BNA | 07-17 | 94 | 89.4 | +4.6 | 74 | 69.7 | +4.3 | 19.0 | 15 | 100 | 73 | 72.0 | 77.8 | 24 |
| MEM | 07-14 | 90 | 91.6 | -1.6 | 74 | 74.0 | +0.0 | 17.0 | 18 | 97 | 73 | 70.8 | 77.4 | 24 |
| MEM | 07-15 | 89 | 91.7 | -2.7 | 75 | 74.0 | +1.0 | 17.0 | 18 | 93 | 76 | 73.5 | 77.4 | 24 |
| MEM | 07-16 | 90 | 91.7 | -1.7 | 74 | 74.0 | +0.0 | 17.0 | 18 | 98 | 74 | 72.8 | 78.3 | 24 |
| MEM | 07-17 | 93 | 91.7 | +1.3 | 76 | 74.0 | +2.0 | 19.5 | 18 | 101 | 74 | 72.5 | 78.4 | 24 |
| ATL | 07-14 | 85 | 89.2 | -4.2 | 72 | 71.4 | +0.6 | 13.5 | 15 | 89 | 73 | 70.9 | 74.8 | 24 |
| ATL | 07-15 | 90 | 89.2 | +0.8 | 74 | 71.4 | +2.6 | 17.0 | 15 | 95 | 74 | 71.8 | 76.5 | 24 |
| ATL | 07-16 | 93 | 89.3 | +3.7 | 75 | 71.4 | +3.6 | 19.0 | 15 | 100 | 74 | 72.3 | 78.1 | 24 |
| ATL | 07-17 | 91 | 89.3 | +1.7 | 75 | 71.4 | +3.6 | 18.0 | 15 | 98 | 77 | 72.6 | 78.5 | 24 |
| CLT | 07-14 | 88 | 89.2 | -1.2 | 71 | 68.2 | +2.8 | 14.5 | 14 | 89 | 70 | 66.5 | 73.0 | 24 |
| CLT | 07-15 | 94 | 89.2 | +4.8 | 68 | 68.2 | -0.2 | 16.0 | 14 | 97 | 70 | 67.6 | 75.6 | 24 |
| CLT | 07-16 | 97 | 89.2 | +7.8 | 73 | 68.3 | +4.7 | 20.0 | 14 | 101 | 72 | 69.5 | 77.3 | 24 |
| CLT | 07-17 | 98 | 89.2 | +8.8 | 76 | 68.3 | +7.7 | 22.0 | 14 | 102 | 73 | 70.0 | 77.4 | 24 |
| RDU | 07-14 | 87 | 90.4 | -3.4 | 69 | 70.1 | -1.1 | 13.0 | 15 | 88 | 70 | 65.4 | 71.7 | 24 |
| RDU | 07-15 | 93 | 90.4 | +2.6 | 65 | 70.1 | -5.1 | 14.0 | 15 | 93 | 67 | 63.9 | 73.3 | 24 |
| RDU | 07-16 | 98 | 90.4 | +7.6 | 72 | 70.1 | +1.9 | 20.0 | 15 | 103 | 74 | 69.8 | 78.7 | 24 |
| RDU | 07-17 | 97 | 90.4 | +6.6 | 75 | 70.1 | +4.9 | 21.0 | 15 | 105 | 74 | 71.8 | 79.4 | 24 |
| STL | 07-14 | 90 | 89.3 | +0.7 | 70 | 71.2 | -1.2 | 15.0 | 15 | 94 | 71 | 68.4 | 75.3 | 24 |
| STL | 07-15 | 91 | 89.3 | +1.7 | 74 | 71.2 | +2.8 | 17.5 | 15 | 94 | 72 | 68.9 | 75.2 | 24 |
| STL | 07-16 | 88 | 89.3 | -1.3 | 77 | 71.2 | +5.8 | 17.5 | 15 | 94 | 75 | 73.1 | 77.7 | 23 |
| STL | 07-17 | 92 | 89.3 | +2.7 | 74 | 71.2 | +2.8 | 18.0 | 15 | 98 | 74 | 72.1 | 78.0 | 24 |
| IND | 07-14 | 91 | 85.2 | +5.8 | 70 | 66.0 | +4.0 | 15.5 | 11 | 93 | 69 | 66.0 | 74.5 | 24 |
| IND | 07-15 | 92 | 85.2 | +6.8 | 72 | 66.0 | +6.0 | 17.0 | 11 | 96 | 71 | 68.8 | 76.5 | 24 |
| IND | 07-16 | 93 | 85.1 | +7.9 | 74 | 66.0 | +8.0 | 18.5 | 11 | 97 | 74 | 70.3 | 76.8 | 24 |
| IND | 07-17 | 93 | 85.1 | +7.9 | 76 | 66.0 | +10.0 | 19.5 | 11 | 101 | 75 | 73.4 | 79.0 | 24 |

### 5b. Early September, 9/01–9/03

| Stn | Date | Tmax | nTmax | ΔTmax | Tmin | nTmin | ΔTmin | CDD | nCDD | max HI | max Td | mean Td | max Tw | n_obs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DCA | 09-01 | 98 | 84.2 | +13.8 | 77 | 67.3 | +9.7 | 22.5 | 11 | 103 | 75 | 71.6 | 78.5 | 24 |
| DCA | 09-02 | 91 | 84.0 | +7.0 | 74 | 67.0 | +7.0 | 17.5 | 11 | 97 | 73 | 70.9 | 77.7 | 24 |
| DCA | 09-03 | 91 | 83.7 | +7.3 | 71 | 66.8 | +4.2 | 16.0 | 10 | 100 | 77 | 73.4 | 80.0 | 24 |
| IAD | 09-01 | 94 | 84.4 | +9.6 | 74 | 61.7 | +12.3 | 19.0 | 8 | 101 | 73 | 71.6 | 78.4 | 24 |
| IAD | 09-02 | 92 | 84.1 | +7.9 | 73 | 61.4 | +11.6 | 17.5 | 8 | 99 | 73 | 71.0 | 77.8 | 24 |
| IAD | 09-03 | 92 | 83.8 | +8.2 | 70 | 61.2 | +8.8 | 16.0 | 8 | 102 | 76 | 72.1 | 79.6 | 24 |
| BWI | 09-01 | 95 | 82.8 | +12.2 | 73 | 62.7 | +10.3 | 19.0 | 8 | 103 | 73 | 71.6 | 79.0 | 24 |
| BWI | 09-02 | 81 | 82.5 | -1.5 | 70 | 62.4 | +7.6 | 10.5 | 8 | 83 | 72 | 70.8 | 73.6 | 24 |
| BWI | 09-03 | 91 | 82.3 | +8.7 | 70 | 62.1 | +7.9 | 15.5 | 7 | 96 | 75 | 72.0 | 77.1 | 24 |
| PHL | 09-01 | 93 | 82.8 | +10.2 | 74 | 65.3 | +8.7 | 18.5 | 9 | 102 | 75 | 73.2 | 79.6 | 24 |
| PHL | 09-02 | 77 | 82.5 | -5.5 | 72 | 65.0 | +7.0 | 9.5 | 9 | 77 | 72 | 70.6 | 73.1 | 24 |
| PHL | 09-03 | 89 | 82.3 | +6.7 | 72 | 64.8 | +7.2 | 15.5 | 9 | 97 | 74 | 72.2 | 78.0 | 24 |
| EWR | 09-01 | 87 | 81.5 | +5.5 | 69 | 64.8 | +4.2 | 13.0 | 8 | 93 | 75 | 70.6 | 76.8 | 24 |
| EWR | 09-02 | 73 | 81.3 | -8.3 | 66 | 64.6 | +1.4 | 4.5 | 8 | 73 | 68 | 64.7 | 68.8 | 24 |
| EWR | 09-03 | 89 | 81.0 | +8.0 | 69 | 64.3 | +4.7 | 14.0 | 8 | 93 | 72 | 69.2 | 75.6 | 24 |
| RIC | 09-01 | 97 | 85.6 | +11.4 | 73 | 65.0 | +8.0 | 20.0 | 10 | 100 | 73 | 70.2 | 77.4 | 24 |
| RIC | 09-02 | 96 | 85.4 | +10.6 | 75 | 64.7 | +10.3 | 20.5 | 10 | 103 | 78 | 73.1 | 79.3 | 23 |
| RIC | 09-03 | 95 | 85.1 | +9.9 | 73 | 64.5 | +8.5 | 19.0 | 10 | 106 | 77 | 74.8 | 80.8 | 24 |
| PIT | 09-01 | 88 | 79.4 | +8.6 | 73 | 59.0 | +14.0 | 15.5 | 5 | 94 | 71 | 69.7 | 76.2 | 24 |
| PIT | 09-02 | 92 | 79.1 | +12.9 | 71 | 58.7 | +12.3 | 16.5 | 5 | 98 | 73 | 70.8 | 77.2 | 24 |
| PIT | 09-03 | 89 | 78.9 | +10.1 | 68 | 58.4 | +9.6 | 13.5 | 5 | 96 | 73 | 69.1 | 77.1 | 24 |
| CLE | 09-01 | 88 | 78.7 | +9.3 | 74 | 60.8 | +13.2 | 16.0 | 5 | 95 | 73 | 70.9 | 77.1 | 24 |
| CLE | 09-02 | 93 | 78.5 | +14.5 | 74 | 60.5 | +13.5 | 18.5 | 5 | 101 | 74 | 72.1 | 78.7 | 24 |
| CLE | 09-03 | 92 | 78.3 | +13.7 | 68 | 60.3 | +7.7 | 15.0 | 5 | 102 | 76 | 70.0 | 79.9 | 24 |
| CMH | 09-01 | 93 | 81.9 | +11.1 | 74 | 61.7 | +12.3 | 18.5 | 7 | 99 | 74 | 71.1 | 78.3 | 24 |
| CMH | 09-02 | 96 | 81.7 | +14.3 | 73 | 61.4 | +11.6 | 19.5 | 7 | 101 | 71 | 69.7 | 77.3 | 24 |
| CMH | 09-03 | 97 | 81.4 | +15.6 | 75 | 61.1 | +13.9 | 21.0 | 7 | 100 | 72 | 69.6 | 77.6 | 24 |
| CVG | 09-01 | 94 | 83.2 | +10.8 | 71 | 62.3 | +8.7 | 17.5 | 8 | 99 | 71 | 69.8 | 77.2 | 24 |
| CVG | 09-02 | 95 | 82.9 | +12.1 | 73 | 62.0 | +11.0 | 19.0 | 8 | 100 | 72 | 70.1 | 77.5 | 24 |
| CVG | 09-03 | 96 | 82.7 | +13.3 | 74 | 61.8 | +12.2 | 20.0 | 8 | 100 | 71 | 70.3 | 77.5 | 24 |
| ORD | 09-01 | 95 | 79.8 | +15.2 | 77 | 60.2 | +16.8 | 21.0 | 6 | 103 | 76 | 72.8 | 79.9 | 24 |
| ORD | 09-02 | 96 | 79.5 | +16.5 | 78 | 59.8 | +18.2 | 22.0 | 6 | 101 | 74 | 70.8 | 79.0 | 24 |
| ORD | 09-03 | 91 | 79.3 | +11.7 | 77 | 59.5 | +17.5 | 19.0 | 5 | 96 | 74 | 71.0 | 76.8 | 24 |
| BNA | 09-01 | 98 | 87.1 | +10.9 | 73 | 66.0 | +7.0 | 20.5 | 12 | 100 | 70 | 67.1 | 75.8 | 24 |
| BNA | 09-02 | 99 | 86.9 | +12.1 | 73 | 65.7 | +7.3 | 21.0 | 11 | 101 | 71 | 67.6 | 75.6 | 24 |
| BNA | 09-03 | 100 | 86.6 | +13.4 | 75 | 65.4 | +9.6 | 22.5 | 11 | 103 | 72 | 68.9 | 76.9 | 24 |
| MEM | 09-01 | 99 | 89.6 | +9.4 | 78 | 70.3 | +7.7 | 23.5 | 15 | 102 | 71 | 67.9 | 77.6 | 24 |
| MEM | 09-02 | 100 | 89.3 | +10.7 | 78 | 70.1 | +7.9 | 24.0 | 15 | 102 | 71 | 67.2 | 77.5 | 24 |
| MEM | 09-03 | 101 | 89.1 | +11.9 | 78 | 69.8 | +8.2 | 24.5 | 14 | 105 | 71 | 68.5 | 77.8 | 24 |
| ATL | 09-01 | 94 | 86.2 | +7.8 | 76 | 69.1 | +6.9 | 20.0 | 13 | 97 | 71 | 67.6 | 75.6 | 24 |
| ATL | 09-02 | 95 | 86.0 | +9.0 | 76 | 68.9 | +7.1 | 20.5 | 12 | 101 | 71 | 69.3 | 77.3 | 24 |
| ATL | 09-03 | 96 | 85.8 | +10.2 | 77 | 68.7 | +8.3 | 21.5 | 12 | 101 | 73 | 70.2 | 77.4 | 24 |
| CLT | 09-01 | 96 | 85.4 | +10.6 | 72 | 65.1 | +6.9 | 19.0 | 10 | 99 | 73 | 70.1 | 76.4 | 24 |
| CLT | 09-02 | 97 | 85.1 | +11.9 | 75 | 64.8 | +10.2 | 21.0 | 10 | 103 | 74 | 70.2 | 78.2 | 24 |
| CLT | 09-03 | 97 | 84.9 | +12.1 | 76 | 64.6 | +11.4 | 21.5 | 10 | 102 | 74 | 71.0 | 78.4 | 24 |
| RDU | 09-01 | 98 | 86.2 | +11.8 | 75 | 66.4 | +8.6 | 21.5 | 11 | 102 | 72 | 70.0 | 77.9 | 24 |
| RDU | 09-02 | 100 | 86.0 | +14.0 | 76 | 66.2 | +9.8 | 23.0 | 11 | 104 | 73 | 69.9 | 77.5 | 24 |
| RDU | 09-03 | 101 | 85.7 | +15.3 | 75 | 65.9 | +9.1 | 23.0 | 11 | 108 | 77 | 72.2 | 79.2 | 24 |
| STL | 09-01 | 100 | 85.6 | +14.4 | 79 | 66.5 | +12.5 | 24.5 | 11 | 102 | 70 | 67.4 | 77.9 | 24 |
| STL | 09-02 | 100 | 85.3 | +14.7 | 82 | 66.1 | +15.9 | 26.0 | 11 | 107 | 71 | 68.5 | 79.1 | 24 |
| STL | 09-03 | 99 | 85.0 | +14.0 | 82 | 65.8 | +16.2 | 25.5 | 11 | 104 | 71 | 68.6 | 78.1 | 24 |
| IND | 09-01 | 96 | 82.6 | +13.4 | 74 | 61.9 | +12.1 | 20.0 | 8 | 103 | 73 | 70.8 | 78.5 | 24 |
| IND | 09-02 | 95 | 82.4 | +12.6 | 75 | 61.6 | +13.4 | 20.0 | 7 | 104 | 74 | 71.8 | 79.0 | 24 |
| IND | 09-03 | 95 | 82.1 | +12.9 | 75 | 61.3 | +13.7 | 20.0 | 7 | 103 | 73 | 71.4 | 78.7 | 24 |

### 5c. Mid-September, 9/16–9/17

| Stn | Date | Tmax | nTmax | ΔTmax | Tmin | nTmin | ΔTmin | CDD | nCDD | max HI | max Td | mean Td | max Tw | n_obs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DCA | 09-16 | 83 | 79.5 | +3.5 | 64 | 62.5 | +1.5 | 8.5 | 7 | 85 | 67 | 63.5 | 71.8 | 24 |
| DCA | 09-17 | 87 | 79.2 | +7.8 | 70 | 62.1 | +7.9 | 13.5 | 6 | 89 | 72 | 68.4 | 75.2 | 24 |
| IAD | 09-16 | 85 | 79.4 | +5.6 | 58 | 56.4 | +1.6 | 6.5 | 4 | 86 | 66 | 62.1 | 71.9 | 24 |
| IAD | 09-17 | — | 79.0 | — | — | 55.9 | — | — | 4 | 91 | 74 | 69.4 | 74.9 | 24 |
| BWI | 09-16 | 86 | 77.9 | +8.1 | 57 | 57.7 | -0.7 | 6.5 | 4 | 87 | 67 | 60.7 | 71.0 | 24 |
| BWI | 09-17 | 88 | 77.5 | +10.5 | 69 | 57.3 | +11.7 | 13.5 | 4 | 90 | 74 | 69.3 | 75.6 | 24 |
| PHL | 09-16 | 83 | 78.0 | +5.0 | 62 | 60.4 | +1.6 | 7.5 | 5 | 84 | 66 | 61.7 | 70.8 | 24 |
| PHL | 09-17 | 84 | 77.7 | +6.3 | 69 | 60.0 | +9.0 | 11.5 | 5 | 88 | 72 | 68.7 | 75.2 | 24 |
| EWR | 09-16 | 81 | 76.7 | +4.3 | 60 | 59.7 | +0.3 | 5.5 | 4 | 81 | 66 | 60.1 | 68.8 | 24 |
| EWR | 09-17 | 84 | 76.3 | +7.7 | 70 | 59.3 | +10.7 | 12.0 | 4 | 86 | 70 | 67.5 | 73.0 | 24 |
| RIC | 09-16 | 83 | 81.2 | +1.8 | 59 | 60.2 | -1.2 | 6.0 | 6 | 83 | 66 | 61.5 | 69.1 | 24 |
| RIC | 09-17 | 90 | 80.9 | +9.1 | 64 | 59.8 | +4.2 | 12.0 | 6 | 93 | 71 | 66.4 | 74.2 | 24 |
| PIT | 09-16 | 86 | 74.3 | +11.7 | 63 | 54.0 | +9.0 | 9.5 | 2 | 91 | 72 | 66.7 | 75.5 | 24 |
| PIT | 09-17 | 83 | 73.9 | +9.1 | 71 | 53.6 | +17.4 | 12.0 | 2 | 86 | 72 | 70.5 | 74.2 | 24 |
| CLE | 09-16 | 81 | 74.0 | +7.0 | 71 | 56.0 | +15.0 | 11.0 | 3 | 84 | 73 | 69.9 | 74.9 | 24 |
| CLE | 09-17 | 77 | 73.6 | +3.4 | 70 | 55.6 | +14.4 | 8.5 | 3 | 77 | 71 | 69.7 | 72.3 | 24 |
| CMH | 09-16 | 89 | 77.1 | +11.9 | 70 | 56.5 | +13.5 | 14.5 | 4 | 96 | 74 | 70.7 | 77.1 | 24 |
| CMH | 09-17 | 83 | 76.7 | +6.3 | 73 | 56.1 | +16.9 | 13.0 | 3 | 88 | 73 | 71.5 | 75.2 | 24 |
| CVG | 09-16 | 92 | 78.2 | +13.8 | 74 | 57.0 | +17.0 | 18.0 | 4 | 98 | 71 | 70.0 | 77.2 | 24 |
| CVG | 09-17 | 93 | 77.7 | +15.3 | 73 | 56.6 | +16.4 | 18.0 | 4 | 97 | 72 | 70.9 | 76.3 | 24 |
| ORD | 09-16 | 76 | 74.9 | +1.1 | 64 | 54.2 | +9.8 | 5.0 | 3 | 76 | 66 | 62.4 | 67.9 | 24 |
| ORD | 09-17 | 80 | 74.5 | +5.5 | 66 | 53.8 | +12.2 | 8.0 | 3 | 79 | 72 | 66.8 | 73.9 | 24 |
| BNA | 09-16 | 99 | 82.4 | +16.6 | 75 | 60.7 | +14.3 | 22.0 | 7 | 100 | 70 | 66.6 | 76.4 | 24 |
| BNA | 09-17 | 99 | 82.0 | +17.0 | 75 | 60.3 | +14.7 | 22.0 | 7 | 101 | 68 | 65.5 | 76.0 | 24 |
| MEM | 09-16 | 98 | 85.1 | +12.9 | 78 | 65.2 | +12.8 | 23.0 | 10 | 102 | 70 | 67.5 | 77.1 | 24 |
| MEM | 09-17 | 98 | 84.7 | +13.3 | 77 | 64.8 | +12.2 | 22.5 | 10 | 101 | 72 | 67.7 | 77.3 | 24 |
| ATL | 09-16 | 89 | 82.2 | +6.8 | 73 | 64.9 | +8.1 | 16.0 | 9 | 92 | 71 | 68.4 | 74.4 | 24 |
| ATL | 09-17 | 90 | 81.9 | +8.1 | 69 | 64.5 | +4.5 | 14.5 | 9 | 90 | 66 | 64.2 | 72.0 | 24 |
| CLT | 09-16 | 88 | 81.3 | +6.7 | 66 | 60.5 | +5.5 | 12.0 | 6 | 88 | 65 | 62.1 | 71.3 | 24 |
| CLT | 09-17 | 91 | 81.0 | +10.0 | 65 | 60.1 | +4.9 | 13.0 | 6 | 91 | 68 | 62.2 | 71.2 | 24 |
| RDU | 09-16 | 86 | 82.1 | +3.9 | 60 | 61.8 | -1.8 | 8.0 | 7 | 86 | 63 | 61.0 | 69.4 | 24 |
| RDU | 09-17 | 93 | 81.8 | +11.2 | 63 | 61.4 | +1.6 | 13.0 | 7 | 93 | 65 | 62.8 | 72.5 | 24 |
| STL | 09-16 | 94 | 80.2 | +13.8 | 75 | 60.5 | +14.5 | 19.5 | 6 | 101 | 73 | 71.2 | 78.4 | 24 |
| STL | 09-17 | 99 | 79.7 | +19.3 | 79 | 60.0 | +19.0 | 24.0 | 6 | 105 | 72 | 69.9 | 79.1 | 24 |
| IND | 09-16 | 93 | 77.7 | +15.3 | 75 | 56.1 | +18.9 | 19.0 | 4 | 102 | 74 | 71.4 | 79.3 | 24 |
| IND | 09-17 | 91 | 77.3 | +13.7 | 72 | 55.7 | +16.3 | 16.5 | 4 | 99 | 73 | 71.0 | 77.8 | 24 |

**Reading (B), per station:** within PJM, the 9/16–9/17 heat was **strongest at its south-western edge**: CVG 92–93°F (+14–15), CMH 89°F (+12) on 9/16, PIT 86°F (+12). These are the stations next to the MISO/TVA heat. **The eastern load centres were modest**: DCA/BWI/PHL/EWR at 81–88°F, peak heat index 81–90°F. The biggest anomaly was **overnight lows in the west** (PIT/CLE/CMH/CVG Tmin +9 to +17°F, mostly +13 to +17), which reads as humid air holding the nights warm rather than extreme afternoon heat (cloud cover was not measured). Neighbours: BNA 99/99, MEM 98/98, STL 94/99, IND 93/91, with heat index 99–105°F. ATL/CLT/RDU reached 86–93°F but were dry (daily-max dew point 63–71°F, mean dew point 61–68°F), with no headlines.

---

## 6. Caveats that could change the reading

1. **Not load-weighted.** Eleven airport stations, equally weighted. PJM's own load-weighted temperature or THI is the right comparison and was **not pulled** (PJM Data Miner has not been tried). Six of the 11 are eastern, so eastern heat counts for slightly more in the PJM-11 average.
2. **Timing within the day is not resolved.** Daily max/min cannot show whether 9/16–9/17 was hot at the evening peak (hours ending 17–19). The §7 IEM hourly command can be re-run to answer that if WATT needs it.
3. **The IAD gap on 9/17** is excluded, not filled. This barely affects the average: IEM daily gives IAD max 87°F, in line with its neighbours.
4. **Zone counts are not weighted by area or population**, and WFOs use different heat index thresholds for issuing headlines. "Zero PJM headlines on 9/16–9/17" is robust because no PJM station reached a 100°F heat index. The **ratio** between episodes is approximate.
5. **The PJM footprint mapping is approximate.** It includes some NIPSCO (MISO) counties under IWX and misses small edge areas (e.g. AEP in Michigan).
6. **Wet-bulb is derived** (Stull 2011, ±~1°C), not observed.
7. **The heat-to-load reasoning in §2a is a hypothesis.** Load, outage and interchange figures are WATT's, as given, and were not checked in this memo.

## 7. Reproduce

```
NCEI:  https://www.ncei.noaa.gov/access/services/data/v1?dataset=daily-summaries&stations=<IDs>&startDate=2026-06-28&endDate=2026-09-22&dataTypes=TMAX,TMIN&units=standard&format=json
NCEI:  https://www.ncei.noaa.gov/access/services/data/v1?dataset=normals-daily&stations=<IDs>&startDate=2010-06-28&endDate=2010-09-22&dataTypes=DLY-TMAX-NORMAL,DLY-TMIN-NORMAL,DLY-CLDD-NORMAL&units=standard&format=json
IEM:   https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?data=tmpf&data=dwpf&data=relh&data=feel&station=DCA&...&year1=2026&month1=6&day1=30&year2=2026&month2=9&day2=22&tz=America%2FNew_York&format=onlycomma&report_type=3
IEM:   https://mesonet.agron.iastate.edu/cgi-bin/request/gis/watchwarn.py?accept=csv&year1=2026&month1=7&day1=1&hour1=0&minute1=0&year2=2026&month2=9&day2=22&hour2=0&minute2=0&limitps=yes&phenomena=HT&significance=Y   (and phenomena=XH&significance=W)
```
**Failed or empty pulls, verbatim:** (1) a `watchwarn.py` request using `sts/ets` ISO parameters with multiple `phenomena=` values returned HTTP 200 with a **header row only (0 records)**. It was re-done with `year1…/minute2` parameters, one phenomenon per call, which worked. (2) `phenomena=EH` (`Y` or `W`), `XH&significance=Y` and `EH&significance=A` all returned **0 records**; this is expected, because NWS renamed Excessive Heat to Extreme Heat (XH) in 2025. (3) The first GHCND/normals pull started 7/10 and could not cover the 7/1–7/5 reference (KeyError in my script, not a server error). It was re-pulled for 6/28–9/22, HTTP 200, complete. (4) GHCND **IAD TMAX/TMIN are absent for 9/17–9/18** in the source data.
