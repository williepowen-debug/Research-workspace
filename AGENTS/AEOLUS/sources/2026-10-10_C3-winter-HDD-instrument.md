# C3 — winter heating-demand instrument: CPC population-weighted HDD, base-rated on strong El Niño winters

**Written:** 2026-10-10 11:52 EDT (`date`) · **Author:** AEOLUS measurement worker (spawned) · **Channel:** C3 energy demand · **Status:** PROPOSAL-ONLY. Nothing here is registered, scored, fired or resolved. AEOLUS decides. WATT owns the PJM power reading. BRENT owns the gas-price reading.
**Question:** C3's band, "CDD/HDD vs 10-yr normal (region) ±10/20/30%", has no instrument behind it, so its exit cannot fire. Is there a no-auth regional heating-degree-day series with a published normal? What does a strong El Niño winter look like on it? What band and exit would the base rate support?

---

## 0. Answers in plain words

1. **Instrument found and verified:** NOAA CPC's **daily population-weighted heating degree days by census division** (plus a CONUS total). It is one pipe-delimited text file per year, with no key needed. It runs from **1981 to 2026-10-08**, refreshes daily (file stamped 10-Oct-2026 08:07) and lags about 2 days. ⚠️ **CPC publishes only a 1981–2010 normal for it.** I derived a 1991–2020 normal from the same product's own archive. The 1991–2020 DJF normal is **2.2–3.0% lower** than CPC's 1981–2010 normal (MidAtl 3,069 vs 3,139; US 2,342 vs 2,415).
2. **Base rate (n is small).** Strong El Niño means DJF ONI ≥ +1.5. **n = 5 winters in the CPC daily era (1982–2026)** and **n = 7 since 1951** (NCEI nClimDiv state HDD, which I rolled up to divisions myself). **Middle Atlantic DJF HDD has median −11.9% vs 1991–2020** (CPC era, range −13.4 to −3.4, **5/5 below normal**). E N Central has median −12.7%, 5/5 below. US has median −7.8%, 5/5 below. Neutral winters have median +4.3 / +2.9 / +2.7%; La Niña winters +0.3 / +1.0 / +1.2%. **The sharpest discriminator is the 30-day window.** In 0 of 5 strong El Niño winters did any 30-day window inside DJF reach +10% above normal, on any of MidAtl, ENC or US. That happened in 9–10 of 14 neutral and 11–13 of 16 La Niña winters.
3. ⚠️ **Caveats that change the read:** **(a)** **2009-10 (DJF ONI +1.47) sits 0.03 below the class line and was COLD:** MidAtl DJF +4.4%, US +10.4%, a 30-day MidAtl window of +16.8%. Classify by NDJ instead and "0/5" becomes "1/6". **(b)** The **pre-1982 strong events were NOT mild in the East:** MidAtl 1957-58 +8.4%, 1972-73 +1.5%. The warm composite is a post-1982 result. **(c)** The early season does not discriminate. In Nov–Dec 30-day windows, 1–2 of 5 strong El Niño winters still had a window ≥ +10%.
4. **The registered ±10/20/30% band cannot fire on the warm side at season scale.** In 76 DJF seasons (1951–2026), **no region was ever ≤ −20%** (lowest MidAtl −15.3%, ENC −17.5%, US −12.2%). **None was ever ≥ +30%.** The band only behaves like a real distribution on **7-day** windows (all-winter US q95 ≈ +30%).
5. **Live read (shoulder season; % is noisy at these small totals, which is why CPC itself suppresses % when normal < 100).** Jul 1–Oct 8 2026 vs the derived 1991–2020 normal: **US 74 vs 104.5 HDD (−29%) · MidAtl 131 vs 157.5 (−17%) · ENC 110 vs 182.3 (−40%)**. Trailing 30 days (9/09–10/08): MidAtl −10.5%, ENC −33.6%, US −27.7%.
6. **Forecasts are much less warm than the composite:** **CPC 9/17 degree-day outlook** has DJF US −3.9% / MidAtl −5.7% / ENC −6.0% vs **1981–2010**. Rebased to 1991–2020 that is about −0.4 / −3.3 / −4.0%. **EIA STEO 10/6** has DJF US −3.2% / MAC −3.5% / ENC −1.8% vs **EIA's prior-10-year average**. The El Niño composite medians are −8 to −13%.
7. **Catalysts:** **CPC long-lead outlook Thu 2026-10-15** (8:30 ET maps; the degree-day outlook file was stamped 3 PM EDT last month), then 11/19 (DJF at 0.5-month lead) and 12/17. **EIA storage report Thursdays 10:30 ET**, next 10/15 (exceptions: Fri 11/13, Wed 11/25 noon). **STEO** came out 10/6, next 11/10. **Henry Hub Nov-26 (NGX26) $3.22**, last trade 2026-10-09 17:00 ET. ⚠️ This is **not the settle**: the tool flagged an evening-session bar and withheld the change.

---

## 1. The instrument: commands, returns, cadence, normal

### 1a. PRIMARY — CPC daily population-weighted HDD by census division (VERIFIED, no auth)

```
curl -s "https://ftp.cpc.ncep.noaa.gov/htdocs/degree_days/weighted/daily_data/2026/Population.Heating.txt"
```
**Return (HTTP 200, 9,222 B, pulled 2026-10-10 ~11:45 EDT):**
```
Product: Daily Heating Degree Days
Regions: CPC::Regions::CensusDivisions
Weights: Population
Region|20260101|20260102|...|20261004|20261005|20261006|20261007|20261008
1|41|...|12|8|14|16|10
2|43|...|9|6|14|12|8
3|47|...|6|9|8|4|6
...
CONUS|29|...|4|3|5|4|3
```

| Property | Value |
|---|---|
| Regions | 9 census divisions + CONUS. IDs from `.../daily_data/regions/CensusDivisions.txt`: **1 NEW ENGLAND · 2 MIDDLE ATLANTIC (NJ NY PA) · 3 E N CENTRAL (IL IN MI OH WI)** · 4 WNC · 5 SOUTH ATLANTIC (DE DC FL GA MD NC SC VA WV) · 6 ESC · 7 WSC · 8 MTN · 9 PAC · CONUS |
| Unit | whole °F-days, base 65°F, one integer per day |
| Weights | "Population". Census 2010 file at `.../daily_data/populations/Census/2010/Populations.txt`, by climate division |
| Cadence / latency | daily. Directory stamp **10-Oct-2026 08:07**, last column **20261008**, so about a 2-day lag |
| History | one folder per year, **1981–2026** (`.../daily_data/<YYYY>/`). 1981–2013 files were stamped 29-Oct-2013 (a reprocessing). 2014+ files are stamped 3 Jan of the next year. **I fetched all 46 years; every one returned 200 and parsed.** |
| Year rollover | DJF spans two files. Pull both `2026/` and `2027/`. `latest/` holds only the current year. |
| Other files, same folders | `StatesCONUS.Heating.txt` (daily, by state), `UtilityGas.Heating.txt` (weighted by gas-heating customers), `Electricity.Heating.txt`, `ClimateDivisions.Heating.txt` |
| **Published normal** | **ONLY 1981–2010**: `.../daily_data/climatology/1981-2010/Population.Heating.txt` (MMDD columns, 366 days). **No 1991–2020 climatology exists on the server** (the `climatology/` dir lists only `1981-2010/`). |
| **Normal used here** | **1991–2020 daily mean by MMDD, derived by me from the same product's 30 archived years.** Feb 29 is dropped everywhere. Reproducible: the script in §1e. |

**DJF normal (90 days), two bases:**

| Division | 1991–2020 (derived) | CPC 1981–2010 (published) | diff |
|---|---:|---:|---:|
| New England | 3,277.9 | 3,364 | −2.6% |
| Middle Atlantic | 3,068.7 | 3,139 | −2.2% |
| E N Central | 3,376.7 | 3,451 | −2.2% |
| South Atlantic | 1,590.1 | 1,661 | −4.3% |
| CONUS | 2,342.4 | 2,415 | −3.0% |

⚠️ **The basis choice moves every reading by 2–4%.** That is the same size as the CPC and EIA forecast anomalies (§3).

### 1b. Live read (CPC daily file through 2026-10-08)

| Leg | Jul 1–Oct 8 obs | 1991–2020 norm | dev | CPC 1981–2010 norm | trailing 30d (9/09–10/08) | trailing 7d (10/02–10/08) |
|---|---:|---:|---:|---:|---:|---:|
| Middle Atlantic | 131 | 157.5 | −17% | 175 | 126 vs 140.8 (**−10.5%**) | 53 vs 56.2 (−5.7%) |
| E N Central | 110 | 182.3 | −40% | 201 | 106 vs 159.7 (**−33.6%**) | 46 vs 60.8 (−24.3%) |
| CONUS | 74 | 104.5 | −29% | 115 | 68 vs 94.0 (**−27.7%**) | 24 vs 37.6 (−36.2%) |
| New England | 195 | 215.4 | −9% | 245 | — | 65 vs 69.6 |
| South Atlantic | 21 | 32.3 | −35% | 39 | — | 8 vs 16.0 |

*Not base-rated: shoulder-season windows lie outside the DJF domain in §2. Report these; do not grade them.*

### 1c. SECONDARY CPC products found. **Do NOT grade on these.**

**① CPC weekly/monthly tables (`cdus`).** Weekly: `curl -s "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/cdus/degree_days/wsahddy.txt"`. Monthly: `msahddy.txt`. Both returned HTTP 200. Weekly: "LAST DATE OF DATA COLLECTION PERIOD IS OCT 3, 2026". Monthly: "MONTHLY DATA FOR SEP 2026". They carry population-weighted plus gas-, oil- and electric-heating-customer-weighted regional rows.
⚠️ **Normal basis UNVERIFIED and inconsistent with 1a.** The explanation page (`ddayexp.shtml`, "Page last modified: November 18, 2009") says the deviation is from the "normal (1971-2000)" and weights use the "2000 Census". The table's implied normals are higher than 1a's 1981–2010 climatology: Sep MidAtl **105** vs 97, NE 153 vs 138, US 77 vs 66. ⚠️ **The table's observed totals also differ from 1a for the same days.** Week 9/27–10/3: NE 36 vs 32, MA 21 vs 23, ENC 36 vs 28, US 18 vs 16. These are two separate CPC computations. **A band must not mix them.**

**② CPC population-weighted degree-day OUTLOOK (a forecast instrument).**
```
curl -s "https://www.cpc.ncep.noaa.gov/pacdir/DDdir/ddforecast.txt"
```
HTTP 200, 86,898 B, header "300 PM EDT THU 17 SEP 2026". Monthly mean plus 90%/10% bounds by census division, state and US. **Normals stated in-file as (1981-2010).** DJF 2026-27, summing monthly means:

| Region | DJF fcst mean | 1981–2010 normal | vs 1981–2010 | ≈ vs 1991–2020 (1a basis; cross-product, approximate) |
|---|---:|---:|---:|---:|
| New England | 3,211 | 3,399 | −5.5% | −2.0% |
| Mid Atlantic | 2,967 | 3,146 | −5.7% | −3.3% |
| East North Central | 3,243 | 3,449 | −6.0% | −4.0% |
| South Atlantic | 1,647 | 1,689 | −2.5% | +3.6% |
| United States | 2,334 | 2,429 | −3.9% | −0.4% |
| Pennsylvania | 2,940 | 3,139 | −6.3% | — |
| Ohio | 2,969 | 3,180 | −6.6% | — |

⚠️ **The FTP archive of this product is STALE.** `https://ftp.cpc.ncep.noaa.gov/htdocs/degree_days/weighted/llf/` lists files up to `ddforecast_y2026m05.txt` (21-May-2026) and nothing for the Jun–Sep 2026 issues. The **live** file is at the `pacdir` path above. Use that path, never the `llf/` listing.

### 1d. EIA STEO regional HDD (forecast; carries EIA's own "prior 10-year average")
```
curl -sL -A "Mozilla/5.0" -o STEO_m.xlsx "https://www.eia.gov/outlooks/steo/xls/STEO_m.xlsx"
```
HTTP 200, 1,098,385 B. Sheet `9ctab` "U.S. Regional Weather Data" has series `ZWHDPUS`, `ZWHD_NEC/MAC/ENC/SAC…` and `…_10YR` ("Heating Degree Days, Prior 10-year average"). Forecast date: Thursday, October 1, 2026 (October STEO). Footnote: *"Regional degree days … calculated by EIA as contemporaneous period population-weighted averages of state degree day data published by NOAA."* Reading it needs `openpyxl` (present in `.venv`; absent in system python).

| DJF | US | MAC | ENC | NEC | SAC |
|---|---|---|---|---|---|
| **2026-27 STEO fcst vs prior-10yr avg** | 2,150 vs 2,222 **(−3.2%)** | 2,848 vs 2,951 **(−3.5%)** | 3,191 vs 3,248 **(−1.8%)** | 3,052 vs 3,169 (−3.7%) | 1,406 vs 1,467 (−4.2%) |
| 2025-26 (history in file) | +3.5% | +19.2% | +11.3% | +17.4% | +16.0% |

STEO text, 10/6: *"On average across the United States, our forecast assumes temperatures this winter will be about the same as last winter and the previous 10-winter average"* and *"a milder winter this year in the Northeast."*

### 1e. Grading script (tested end-to-end from a fresh download on 2026-10-10, output in 1b)
```bash
mkdir -p "$DL" && cd "$DL"   # DL = a fresh empty dir
for y in $(seq 1991 2020) 2026 2027; do mkdir -p $y; curl -s -o $y/Population.Heating.txt \
  "https://ftp.cpc.ncep.noaa.gov/htdocs/degree_days/weighted/daily_data/$y/Population.Heating.txt"; done
python3 -I c3_hdd_grade.py "$DL"     # script kept OUTSIDE $DL
```
(A 2027 folder that does not exist yet saves a 404 HTML body. Delete it, or skip the year until January.)
```python
"""C3 winter HDD read: trailing 30-day and 7-day pop-weighted HDD vs a 1991-2020 normal derived from the same CPC product."""
import sys, os, glob, statistics as st, datetime as dt
D=sys.argv[1]; obs={}
for f in glob.glob(os.path.join(D,'*','Population.Heating.txt')):
    hdr=None
    for l in open(f):
        l=l.rstrip('\n')
        if l.startswith('Region|'): hdr=l.split('|')[1:]; continue
        if hdr and '|' in l:
            p=l.split('|')
            for k,v in zip(hdr,p[1:]): obs[(p[0],k)]=float(v)
LEGS=[('2','MIDDLE ATLANTIC'),('3','E N CENTRAL'),('CONUS','CONUS')]
last=max(dt.datetime.strptime(k,'%Y%m%d').date() for (r,k) in obs if r=='CONUS')
def norm(reg,d):
    v=[obs.get((reg,f'{y}{d:%m%d}')) for y in range(1991,2021)]
    if None in v: raise SystemExit(f'normal incomplete for {reg} {d:%m%d}')
    return st.mean(v)
print(f'latest complete day in file: {last}')
for W in (30,7):
    days=[last-dt.timedelta(i) for i in range(W)]
    days=[d for d in days if not (d.month==2 and d.day==29)]
    for reg,name in LEGS:
        o=sum(obs[(reg,f'{d:%Y%m%d}')] for d in days); n=sum(norm(reg,d) for d in days)
        print(f'{W:>2}d {min(days)}..{last} {name:<15} obs {o:6.0f} norm9120 {n:7.1f} dev {o-n:+7.1f} ({100*(o/n-1):+.1f}%)')
```

---

## 2. Base rate

### 2a. Method
- **ENSO class** comes from `curl -s "https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt"` (HTTP 200; last row `JAS 2026 29.12 2.16`). The class uses the **DJF ONI of that winter**: strong El Niño (SEN) ≥ +1.5 · moderate (MEN) 1.0–1.49 · weak (WEN) 0.5–0.99 · neutral (NEU) −0.49…+0.49 · La Niña (LAN) ≤ −0.5. **DJF alone, with no 5-season persistence requirement.** That is a simplification.
- **The confirmed SEN list differs from the brief's.** DJF ≥ 1.5: **1957-58 (+1.69), 1972-73 (+1.55), 1982-83 (+2.14), 1991-92 (+1.54), 1997-98 (+2.22), 2015-16 (+2.50), 2023-24 (+1.84).** **1987-88 does NOT qualify** (DJF 1988 ONI = **+0.63**; its peak was ASO 1987 +1.49; the +1.18 is DJF 1987, i.e. winter 1986-87). **2009-10 is +1.47 and 1965-66 is +1.24**; both have NDJ ≥ 1.5 and are shown separately as boundary cases.
- **Series A (CPC era, n = 45 winters, 1981-82 … 2025-26):** the §1a product. DJF is Dec 1–Feb 28 with Feb 29 dropped, and the % is vs the derived 1991–2020 normal.
- **Series B (1951-52 … 2025-26, n = 76):** NCEI nClimDiv state monthly HDD, `curl -sL "https://www.ncei.noaa.gov/monitoring-content/data/us/climdiv/monthly/current/climdiv-hddcst-v1.0.0-20261006"` (HTTP 200; `/pub/data/cirs/climdiv/` 301-redirects there). Element 25 is HDD. The readme says "Population weights utilize the 2010 Census data". **I rolled states up to census divisions myself** using CPC 2010 populations. US = NCEI code 110. "PJMcore7" = population-weighted PA NJ MD DE VA WV OH; that is **my construction, not PJM's load weighting**.
- **Cross-validation, A vs B on DJF totals 1982–2026:** r = **0.992 (NE), 0.995 (MidAtl), 0.996 (ENC), 0.985 (US)**. Means 3,290/3,309 · 3,084/3,084 · 3,391/3,399 · 2,360/2,354. B is a valid long-run proxy for A.

### 2b. DJF season % vs 1991–2020, by regime — Series A (CPC daily, 1982–2026)

| Region | SEN n=5 median [range] | SEN below normal | MEN n=2 | WEN n=8 med | NEU n=14 med [q25, q75] | LAN n=16 med [q25, q75] | ALL n=45 [q10, q90] |
|---|---|---|---|---|---|---|---|
| **Middle Atlantic** | **−11.9** [−13.4, −3.4] | **5/5** | +4.5, +5.0 | +0.9 | +4.3 [−5.2, +10.7] | +0.3 [−2.6, +5.7] | [−11.9, +11.8]; min −15.9 / max +17.0 |
| **E N Central** | **−12.7** [−15.9, −7.8] | **5/5** | −3.7, +6.2 | −1.1 | +2.9 [−0.1, +9.7] | +1.0 [−3.7, +9.3] | [−12.2, +11.0]; min −15.9 / max +19.1 |
| **US (CONUS)** | **−7.8** [−11.6, −4.5] | **5/5** | +1.9, +10.4 | +1.5 | +2.7 [−1.1, +7.0] | +1.2 [−4.2, +7.5] | [−9.4, +10.2]; min −11.6 / max +12.2 |
| New England | −7.6 [−15.0, +0.7] | 4/5 | | +1.2 | +6.7 | −0.1 | [−11.5, +10.0] |
| South Atlantic | −7.3 [−12.1, +0.4] | 4/5 | | +5.8 | +3.5 | +0.8 | — |

**SEN winters one by one (Series A, raw % / detrended %):**

| Winter (DJF ONI) | MidAtl | ENC | US |
|---|---|---|---|
| 1982-83 (+2.14) | −5.6 / −9.0 | −11.5 / −14.9 | −4.5 / −9.1 |
| 1991-92 (+1.54) | −3.4 / −5.6 | −7.8 / −10.0 | −5.9 / −8.8 |
| 1997-98 (+2.22) | −11.9 / −13.1 | −14.0 / −15.1 | −7.8 / −9.5 |
| 2015-16 (+2.50) | −13.4 / −12.4 | −12.7 / −11.2 | −11.6 / −10.0 |
| 2023-24 (+1.84) | −12.3 / −10.2 | −15.9 / −13.3 | −10.1 / −6.9 |
| ⚠️ *2009-10 (+1.47, NDJ +1.50), boundary* | ***+4.4*** | ***+6.3*** | ***+10.4*** |

*Very-strong subset (DJF ≥ +2.0: 1982-83, 1997-98, 2015-16), n = 3:* MidAtl −5.6 / −11.9 / −13.4 · ENC −11.5 / −14.0 / −12.7 · US −4.5 / −7.8 / −11.6.

### 2c. Same view since 1951 — Series B (NCEI states rolled up to divisions; n = 7 SEN)

| Region | SEN n=7 raw median [q25, q75] | SEN below normal | SEN detrended median | NEU n=25 med | LAN n=26 med | trend (HDD/yr) | trend line at 2027 vs 1991–2020 |
|---|---|---|---|---|---|---|---|
| Middle Atlantic | −3.7 [−12.7, −0.6] | 5/7 | −8.2 | +5.6 | +2.5 | −5.27 | −2.7% |
| E N Central | −10.7 [−13.4, −3.3] | 5/7 | −11.5 | +2.6 | +3.7 | −4.90 | −2.4% |
| PJMcore7 *(mine)* | −4.7 [−12.3, −1.8] | 5/7 | −8.9 | +6.4 | +1.8 | −4.93 | −2.6% |
| US (code 110) | −5.7 [−9.3, +2.3] | 5/7 | −8.6 | +5.5 | +2.7 | −4.12 | −3.0% |
| New England | −3.4 [−10.9, +1.8] | 4/7 | −7.2 | +7.1 | +3.1 | −5.01 | −2.6% |

⚠️ **The pre-1982 strong events were near or above normal in the East.** MidAtl: 1957-58 **+8.4%** (detrended −0.7), 1972-73 **+1.5%** (detrended −4.8). 1965-66 (NDJ only): +6.3%. **The "strong El Niño = mild East" result is a post-1982 result.** Its 1951+ form is weaker: median −3.7% raw, −8.2% detrended.

**"10-yr normal" basis (the registered row's literal wording):** each winter vs the mean of the 10 winters before it (Series A, winters ending 1992–2026). SEN: MidAtl **−6.1 / −13.9 / −15.0 / −9.8**; ENC −11.0 / −16.0 / −15.5 / −14.2; US −10.0 / −10.1 / −13.4 / −7.1 (1991-92 / 1997-98 / 2015-16 / 2023-24). Other winters (n = 31): MidAtl median +0.7, ENC +0.6, US +2.0. The current 10-winter mean (2016-17…2025-26) sits **−3.3% (MidAtl), −4.3% (ENC), −4.1% (US)** vs 1991–2020.

### 2d. 30-day windows fully inside DJF (Series A, 1982–2026; windows end Dec 30 … Feb 28)

| Leg | ALL windows q50 / q75 / q90 / q95 [min, max] | SEN q10 / q50 / q90 | **Largest 30-d window in any SEN winter** | Winters with a 30-d window ≥ +10%: SEN · NEU · LAN | ≥ +20%: SEN · NEU · LAN |
|---|---|---|---|---|---|
| **Middle Atlantic** | −0.1 / +9.8 / +17.3 / +22.6 [−36.1, +47.6] | −16.8 / −8.0 / −0.7 | **+7.8** (1991-92) | **0/5 · 9/14 · 12/16** | 0/5 · 6/14 · 5/16 |
| **E N Central** | −0.9 / +9.6 / +18.9 / +25.1 [−30.9, +41.0] | −21.6 / −9.5 / −2.6 | **+0.2** (2015-16) | **0/5 · 10/14 · 13/16** | 0/5 · 5/14 · 9/16 |
| **US** | +0.7 / +8.1 / +15.7 / +20.3 [−26.9, +36.9] | −14.4 / −5.7 / +1.8 | **+5.9** (1982-83) | **0/5 · 9/14 · 11/16** | 0/5 · 4/14 · 3/16 |
| New England | 0.0 / +8.0 / +15.3 / +19.4 | −16.3 / −8.2 / +2.5 | +10.7 (1991-92) | 1/5 · 8/14 · 11/16 | 0/5 · 4/14 · 3/16 |

⚠️ **2009-10 boundary case:** largest 30-day window MidAtl **+16.8%**, ENC +15.8%, US +17.7%. If 2009-10 counts as SEN, the "0/5 at +10%" becomes **1/6** on all three legs.
Mild side: share of SEN 30-day windows ≤ −20%: MidAtl 6%, ENC 14%, US 4%. Most extreme: 2015-16 MidAtl −36.1%.

**Early season does NOT discriminate:** 30-day windows starting Nov 1–30. Winters with a window ≥ +10%: **MidAtl SEN 1/5** (1997: +17.5) vs others 21/39 · **ENC SEN 2/5** (1991 +17.6, 1997 +15.2) vs 19/39 · **US SEN 2/5** vs 19/39. SEN q50: −6.4 / −6.9 / −5.4%.

### 2e. 7-day windows inside DJF (the cold-tail view; relevant context for AEO-08, which resolves on PJM postings, not on HDD)

| Leg | ALL q75 / q90 / q95 | SEN q50 / q90 | Largest 7-d window per SEN winter (82-83, 91-92, 97-98, 15-16, 23-24) | Winters with a 7-d ≥ +20%: SEN · NEU · LAN | ≥ +30% | ≥ +40% |
|---|---|---|---|---|---|---|
| Middle Atlantic | +13.1 / +25.5 / +32.6 | −9.6 / +11.4 | +29.0, +20.3, +8.8, +24.1, +17.7 | **3/5** · 12/14 · 14/16 | 0/5 · 8/14 · 12/16 | 0/5 · 6/14 · 5/16 |
| E N Central | +14.3 / +28.6 / +36.5 | −13.2 / +8.0 | +16.8, +20.1, +10.7, +23.8, +33.6 | **3/5** · 13/14 · 15/16 | 1/5 · 12/14 · 14/16 | 0/5 · 10/14 · 9/16 |
| US | +12.2 / +23.5 / +30.0 | −7.4 / +10.0 | +18.2, +22.5, +11.8, +13.2, +31.6 | 2/5 · 14/14 · 14/16 | 1/5 · 9/14 · 10/16 | 0/5 · 6/14 · 6/16 |

*A 7-day HDD window is a proxy for a regional cold spell, not a PJM Cold Weather Alert. The two are different instruments.* 2009-10's largest 7-day window: MidAtl +28.0, ENC +29.8, US +31.7.

### 2f. How reachable is the registered ±10/20/30% band? (Series B, DJF season, 76 winters, 1951–2026)

| Region | ≥ +10% | ≥ +20% | ≥ +30% | ≤ −10% | ≤ −20% | min / max |
|---|---|---|---|---|---|---|
| Middle Atlantic | 21 | 2 (1962-63, 1976-77) | **0** | 7 | **0** | −15.3 (2001-02) / +23.1 (1976-77) |
| E N Central | 17 | 5 (1962-63, 1976-79, 2013-14) | **0** | 9 | **0** | −17.5 (2023-24) / +26.1 (1976-77) |
| PJMcore7 | 22 | 3 | **0** | 8 | **0** | −14.7 (2022-23) / +27.1 (1976-77) |
| US | 18 | 3 (1976-79) | **0** | 4 | **0** | −12.2 (2023-24) / +22.1 (1978-79) |

**Orange and Red on the warm side (−20/−30%) have never been reached at season scale in 76 winters. Red on the cold side (+30%) has never been reached either.** On the same series, the band only matches a real distribution on 7-day windows (§2e: US all-winter q90 +23.5, q95 +30.0).

---

## 3. Dated catalysts and the gas price

| Date (ET) | Event | Source / verification |
|---|---|---|
| **Thu 2026-10-15, 8:30 AM** | **CPC long-lead outlook** (seasons NDJ 2026 … NDJ 2027; **DJF at 1.5-month lead**). The degree-day outlook file follows. The 9/17 issue was stamped "300 PM EDT". | `https://www.cpc.ncep.noaa.gov/products/predictions/schedule.php` (HTTP 200): "Oct 2026 · 15 Oct 2026 · NDJ 2026 - NDJ 2027". Page: "issued once each month near mid-month at 8:30am Eastern Time". ⚠️ A separate NOAA "Winter Outlook" press event was **not verified**. Historically it coincides. |
| Thu 2026-11-19 | CPC long-lead, **DJF 2026 - DJF 2027 at 0.5-month lead** | same schedule page |
| Thu 2026-12-17 | CPC long-lead (JFM 2027 …) | same |
| **Thursdays 10:30 AM** (next **10/15**) | **EIA Weekly Natural Gas Storage Report**. 2026 exceptions: **Fri 11/13 10:30** (Veterans Day), **Wed 11/25 12:00** (Thanksgiving). No Columbus Day exception is listed. | `https://ir.eia.gov/ngs/schedule.html` (HTTP 200) |
| 2026-10-06 (out) · **next 2026-11-10** | EIA STEO (HDD forecasts in sheet `9ctab`). The **2026–27 Winter Fuels Outlook was published with the 10/6 STEO.** | `https://www.eia.gov/outlooks/steo/` (HTTP 200): "Release Date: October 6, 2026 … Next Release Date: November 10, 2026". ⚠️ The same page also carries "We will release our Winter Fuels Outlook on Wednesday October 15". That **contradicts** its own header (10/15/2026 is a Thursday, and the outlook says it is already published). **It looks like a stale 2025 banner; do not calendar it.** |
| daily ~08:00 | CPC daily HDD file refresh (data through D−2) | §1a |

**Henry Hub:** `python3 FORGE/tools/market-data/fetch.py price NG=F` (run from the repo root at 11:47 EDT 10/10) returned **$3.22**, labelled `contract: Nov 2026 (NGX26)`, As-of `10-09⚠eve→10-12`. The tool's note: *"evening-next-session: withheld … last trade 2026-10-09 17:00:00 [America/New_York]"*. `fetch.py price NGX26.NYM` returned the identical $3.22 and volume 282,250, which confirms the contract mapping. ⚠️ **This is the 17:00 ET last trade, NOT the 14:30 settle, and no change is available.** For context only: STEO 10/6 forecasts Henry Hub spot at **$3.16/MMBtu average for 2027** (−9% vs 2026).

---

## 4. PROPOSAL (not registered; AEOLUS adjudicates)

**P1 — Instrument.** CPC daily population-weighted HDD (§1a). **Grading legs: Middle Atlantic (ID 2) and E N Central (ID 3).** Together they approximate PJM east and west, though neither is PJM's load weighting, and Middle Atlantic includes NY, which is not PJM. **CONUS** is a reported gas-demand leg for BRENT and is **not separately scored**, so the same cold spell is not counted twice. **Normal: 1991–2020 daily mean derived from the product's own 1991–2020 files** (§1e). CPC's 1981–2010 file is the cross-check. *Why not CPC's published 1981–2010 normal:* it is 2.2–3.0% colder (higher HDD) than the current WMO period, so every winter reads 2–3% milder than on a 1991–2020 basis. *Why not "10-yr normal" as the band row says:* this product has no published 10-year normal, and EIA's prior-10-year series comes from a different calculation. The 10-yr numbers are in §2c if AEOLUS prefers that basis. **Name the basis on every figure.**

**P2 — Quantity.** **Trailing 30-day HDD, % vs normal for the same days,** on the most recent complete day in the file. **Gradeable domain: windows ending Dec 30 – Feb 28** (the base-rated domain). Windows ending Oct–Dec 29 are **reported, not graded**, because §2d shows Nov–Dec windows do not separate SEN from other winters. *Why 30 days:* the full-season DJF total cannot move within the season, while the 30-day window is where SEN and other winters separate cleanly (§2d).

**P3 — Band (cold side = heating-demand stress; graded per leg; the channel band = the highest band reached on either PJM leg):**

| Band | Trailing-30d HDD vs 1991–2020 | Traced to |
|---|---|---|
| 🟡 Yellow | **≥ 0%** | SEN 30-d **q90 = −0.7% (MidAtl), −2.6% (ENC)**. All-winter median ≈ 0 (−0.1 / −0.9). Meaning: the El Niño mildness is not showing. |
| 🟠 Orange | **≥ +10%** | **Above the largest 30-d window in every SEN winter on record** (MidAtl +7.8, ENC +0.2; **0/5** winters). All-winter **q75 = +9.8 / +9.6**. Reached in 9/14 NEU and 12/16 LAN winters (MidAtl). ⚠️ 2009-10 (DJF +1.47) reached +16.8 / +15.8. |
| 🔴 Red | **≥ +20%** | All-winter **q90–q95** (MidAtl +17.3 / +22.6; ENC +18.9 / +25.1). 0/5 SEN · 6/14 NEU · 5/16 LAN (MidAtl). |
| *(mild-side marker, not a stress band)* | ≤ SEN 30-d median (**MidAtl −8.0%, ENC −9.5%, US −5.7%**) | Records "El Niño mildness confirmed". Bearish heating demand and gas; route to BRENT. |

**P4 — Exit / invalidation (symmetric, no ratchet, in the style of the C5 trigger).** **The C3 winter-stress read is killed when BOTH PJM legs' trailing-30d HDD are < 0% (below Yellow) on 4+ consecutive sessions inside the gradeable domain.** It re-arms when the same test fails. Channel-kill, not thesis-kill: the El Niño thesis then sits on the gas price (BRENT) and on AEO-07, not on C3 stress. Base-rate expectation: SEN 30-d q75 is −2.8% (MidAtl) and −5.9% (ENC), so in a typical strong El Niño winter **the exit is likely to fire in January.** That is the falsifiable statement.
**Bidirectional flip, testable each daily file:** ↑ any PJM leg's 30-day window ≥ +10%, which is outside every SEN winter on record, falsifies the mild read. ↓ both legs < 0% for 4+ sessions falsifies the stress read.
**Dark-window rule:** the file holds every day, so after a gap, recompute **every** 30-day window in the gap (your 6c procedure). A hit is a REGISTERED HISTORICAL FIRE and never back-fills the score.

**P5 — Retire or replace the ±10/20/30% row.** At season scale its warm-side Orange and Red have **never** been reached in 76 winters, and its cold-side Red (+30%) has never been reached either (§2f). It is a 7-day-scale band labelled as a regional-normal band. If kept at all, it belongs on **7-day** windows (§2e), as context for AEO-08.

**P6 — Also untrippable, flagged and not fixed:** C3's upgrade trigger names a **"Henry Hub break"** with **no level**. That is the same defect class as the band. I did not base-rate a gas level (it is BRENT's domain).

**Independence:** this is the same ENSO root as C1/C2/C6. A mild C3 winter read is **not** independent evidence for any ENSO-driven channel. Count the root once.

**Confidence:** PROVISIONAL. **n = 5** SEN winters for every window statistic. The class boundary is doing real work (2009-10 at +1.47), and the post-1982 vs pre-1982 split is unexplained here.

---

## 5. What I could NOT do or verify

1. **No published 1991–2020 normal for the CPC daily product.** The 1991–2020 normal is my derivation (30 archived years, simple daily mean). The only published normal is 1981–2010.
2. **The `cdus` weekly/monthly tables' normal basis is unresolved.** Their observed totals also disagree with the daily product. Not used.
3. **The New England / Vermont mapping is ambiguous.** CPC's `regions/StatesCONUS-CensusDivisions.txt` maps **VT to MOUNTAIN (8)**, while the outlook file lists VT in New England. Rebuilding division 1 from the state file (Jan–Mar 2026, 90 days), excluding VT fits slightly better than including it (mean |diff| 0.327 vs 0.386 HDD, both inside integer rounding). **Unresolved.** NE is not proposed as a grading leg.
4. **Revision behaviour of the latest days is untested.** The `cdus` page calls CPC degree days "preliminary". I did not re-pull later to see whether D−1/D−2 values change. **Re-pull and diff before grading a band edge.**
5. **No n beyond 5 for 30-day and 7-day windows.** Daily population-weighted data before 1981 was not found on this server. Series B (monthly) supports season-level n = 7 only.
6. **PJM's own load-weighted temperature (Data Miner) was not tried.** The census-division legs approximate PJM and are not PJM.
7. **No separate NOAA "Winter Outlook" press date verified.** Only the CPC long-lead schedule (10/15).
8. **No Henry Hub settle.** Only the 10/9 17:00 ET last trade (§3).
9. **Failed or odd pulls, verbatim:** (a) `https://www.ncei.noaa.gov/pub/data/cirs/climdiv/` returned **HTTP 301** to `…/monitoring-content/data/us/climdiv/monthly/current/`. Followed with `-L`; works. (b) The CPC `llf/` archive is **stale since 21-May-2026** (§1c②). (c) System `python3` lacks `openpyxl`; `.venv/bin/python` has it. (d) My first parse of the CPC outlook file picked up a 4th month (Dec-2027; the file runs 15 months). Fixed by keying explicit (year, month) pairs. **No figure above comes from the faulty parse.**

*Scratch (ephemeral, not committed): downloads and scripts under `/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-AEOLUS/6c123771-9ca2-4110-985a-a5179561245c/scratchpad/c3/` (`scripts/baserate.py`, `windows.py`, `extra.py`, `early.py`, `llf.py`, `steo2.py`, `vtcheck.py`, `c3_hdd_grade.py`).*
