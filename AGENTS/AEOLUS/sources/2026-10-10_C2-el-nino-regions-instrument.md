# C2 — El Niño crop regions: base rates, substitute exit instrument, band proposal

**Worker output for AEOLUS (proposal only: nothing here is scored, fired, resolved or registered).** Written 2026-10-10 ~11:58 EDT; clock from `date` in the session (first stamp `Sat Oct 10 11:42:06 EDT 2026`).
**Scratch (scripts + downloads):** `/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-AEOLUS/6c123771-9ca2-4110-985a-a5179561245c/scratchpad/c2/` (`scripts/baserate.py`, `scripts/sens.py`, `scripts/extra.py`; raw output in `baserate_out.txt` and `extra_out.txt`).

## 0. Headline findings

| # | Finding | Basis |
|---|---|---|
| 1 | **Southern Africa maize carries the strongest and most discriminating El Niño signal in the set.** South Africa (SA) corn ≤−15% vs trailing 5-yr: strong El Niño **5/6**, all El Niño **8/21**, neutral **1/17** (Fisher one-sided p=0.001 strong vs neutral; p=0.023 all El Niño vs neutral). The 4-country aggregate (SA+Zambia+Malawi+Zimbabwe) gives strong **6/6**, all El Niño 8/21, neutral **0/17** (p=0.004). | PSD Online + CPC ONI, n=60 |
| 2 | **Australian wheat (KB-103) reproduces exactly**, but the strong-El Niño subset is *not* worse. ASO ≥1.5: n=4, median −10.8%, **0/4 ≤−15%**. The current read of −10.3% sits on the strong-El Niño median. | same |
| 3 | **Absent at the ≤−15% level:** Malaysia and Indonesia palm oil (0 fires in 57 years, any regime, lag 0 or lag 1), India wheat (0/61 ≤−10%), Vietnam rice, Thailand rice (1 fire, 2015). India rice has a real but small signal: ≤−3% in El Niño 5/11 vs neutral 3/38 (p=0.009), with only 1 fire at ≤−15%. | same |
| 4 | **The NASS crop-condition series is not dead. It moved.** KB-092's 404s were at `nass.usda.gov`. The same `progNNYY.txt` files are served keylessly at `esmis.nal.usda.gov` (the Cornell ESMIS URL now redirects there). I pulled 15 weekly reports, 6/29–10/5/2026. | §3 |
| 5 | **The Australian wheat raise to 31.0 MMT happened in the SEPTEMBER 11 WASDE, not October.** wasde0926.txt shows 2026/27 Australia wheat production **Aug 28.00 → Sep 31.00**; wasde1026.txt shows **Sep 31.00 → Oct 31.00 (unchanged)**. KB-182 records it as an October raise. AEOLUS should adjudicate. | WASDE text files, §4 |
| 6 | **USDA's SA corn figure for the El Niño crop (MY2026/27 = the 2027 harvest) is an unchanged pre-planting projection: 16.50 MMT in Aug, Sep and Oct.** Grading it before Feb 2027 grades USDA's placeholder, not the weather. The SA Crop Estimates Committee (CEC) reports on the **same basis** (verified, §4) and leads USDA. | WASDE + CEC |

---

## 1. Commands and returns (all pulled 2026-10-10 ~11:42–11:57 EDT)

| Instrument | Command | Return |
|---|---|---|
| PSD grains | `curl -sS -D grains.hdr -o grains.zip "https://apps.fas.usda.gov/psdonline/downloads/psd_grains_pulses_csv.zip"` | HTTP 200, 2,873,599 B, `last-modified: Fri, 09 Oct 2026 15:40:43 GMT`; sha256 `7047570ee818e791…` |
| PSD oilseeds (**URL verified**) | `curl -sS -o psd_oilseeds_csv.zip "https://apps.fas.usda.gov/psdonline/downloads/psd_oilseeds_csv.zip"` | HTTP 200, 3,844,435 B, `last-modified: Fri, 09 Oct 2026 15:41:05 GMT`; sha256 `c5b770f5a515c59d…`; contains `psd_oilseeds.csv`, commodity `"Oil, Palm"` (code 4243000) |
| PSD all-data (exists, unused) | `…/psdonline/downloads/psd_alldata_csv.zip` | HTTP 200, last-modified 09 Oct 2026 19:02:03 GMT |
| CPC ONI | `curl -sS -o oni.ascii.txt "https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt"` | HTTP 200; last row `JAS 2026 29.12 2.16`; sha256 `5d6fa3a2f857d916…` |
| NASS Crop Progress (revived) | `P=$(curl -sS "https://esmis.nal.usda.gov/publication/crop-progress" \| grep -oE '/sites/default/release-files/[0-9]+/prog[0-9_]+\.txt' \| head -1); curl -sS "https://esmis.nal.usda.gov$P" -o prog.txt; grep -A22 '^Corn Condition - Selected States' prog.txt \| grep -E '^1[0-9] States'` | HTTP 200 text/plain; latest `prog4026.txt` "Released October 5, 2026"; the 18-States row parses |
| WASDE text | `curl -sS -o wasde1026.txt "https://esmis.nal.usda.gov/sites/default/release-files/796099/wasde1026.txt"` (also `…/796054/wasde0926.txt`; also at `https://www.usda.gov/oce/commodity/wasde/wasde1026.txt`) | HTTP 200 |
| WASDE schedule | `curl -sS -L -A "Mozilla/5.0" "https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report"` | HTTP 200; 2026 and 2027 date lists (§5) |
| SA CEC dates | `curl -sS -A "Mozilla/5.0" -o CEC_Dates_2026.pdf "https://www.sagis.org.za/wp-content/uploads/2025/08/CEC_Dates_2026.pdf"`, then pdfminer | Department of Agriculture meeting-dates sheet (§5) |
| SA CEC 8th estimate | `…/wp-content/uploads/2026/09/CEC_2026-09-29.pdf` | §4 |
| MPOB | `curl -sS -L -A "Mozilla/5.0" "https://bepi.mpob.gov.my/"` | "Monthly Release of Malaysian Palm Oil Industry Performance (September 2026) Release Date: 12th October 2026"; "release on 10th. of every month by 12.30 noon"; statistics are behind a login |
| FAO FFPI | `curl -sS -L -A "Mozilla/5.0" -o ffpi.csv "https://www.fao.org/media/docs/worldfoodsituationlibraries/wfs-library/food_price_indices_data.csv?sfvrsn=523ebd2a_84&download=true"` | HTTP 200, `last-modified: Fri, 02 Oct 2026 13:25:45 GMT` (the `sfvrsn` token rotates monthly; take the current link from the FFPI page) |

---

## 2. Method (pre-stated, same metric as KB-103)

- **Metric:** production in market year (MY) N ÷ mean(MY N−1 … N−5) − 1, computed on **revised PSD actuals**. Base period runs through **MY ≤2025**, so no 2026 forecast enters a base rate.
- **Regimes:** single anchor-season ONI. Strong El Niño ≥+1.5 (a subset of El Niño); El Niño ≥+0.5; neutral −0.5 to +0.5; La Niña ≤−0.5.
- **Statistics:** quantiles use linear interpolation. Discrimination uses a one-sided Fisher exact test (El Niño or strong vs neutral), plus AUC = P(El Niño value < neutral value).

**Market-year → crop → El Niño season mapping.** Each mapping was checked against known drought years in the data.

| Crop | PSD market year → harvest | ONI anchor ("the season that hits the crop") | Mapping check |
|---|---|---|---|
| Australia wheat | MY N = harvest Nov–Dec N | **ASO N** (KB-101) | KB-103 reproduced exactly |
| SA corn | **MY N = harvest Apr–Jun N+1** (USDA "2026/27" = CEC "2027" crop) | **DJF of harvest year** (Dec–Feb) | MY1982=4,399 · MY1991=3,277 · MY1994=4,866 · MY2015=8,214 · MY2023=13,425 = the 1983/1992/1995/2016/2024 droughts. USDA MY2024 17,345 = CEC 2025 total 17,346.5 |
| Zambia, Malawi corn | MY N = harvest N | DJF of harvest year | Zambia MY1992=470, MY2024=1,511; Malawi MY1992=660, MY2016=2,369 |
| Zimbabwe corn | ⚠️ **Convention break:** MY ≤1998 → harvest MY+1; MY ≥2000 → harvest MY; **MY1999 dropped** (2,148, a duplicate of MY2000) | DJF of harvest year | MY1991=360 (1992 harvest); MY2002=500, MY2016=512, MY2024=635. Hand alignment, not a USDA statement |
| Malaysia, Indonesia palm oil | MY N = Oct N–Sep N+1 | **OND of El Niño year E**: lag0 = MY E, lag1 = MY E+1 | Malaysia MY2015 = 17,700 (−11.0% YoY, the 2016 drop) |
| India wheat | MY N = harvest Mar–May N | OND N−1 (primary); JAS N−1 (sensitivity) | — |
| India rice | MY N = kharif N | JAS N | MY2002 = 71,814, MY2009 = 89,083 (drought monsoons) |
| Thailand rice | MY N = main crop N | ASO N | MY2015 = 15,800 |
| Vietnam rice | **unverified** | OND N and OND N−1 | no signal either way |

---

## 3. US crop condition: the "dead" exit instrument is live at a new host (observations only, not graded)

18-States rows from the weekly ESMIS `progNNYY.txt` files. Dented = corn dented % this week.

| Release | Week ending | Corn G/E | Soy G/E | Corn dented |
|---|---|---|---|---|
| Jun 29 | 6/28 | 67 | 65 | — |
| Jul 27 | 7/26 | 63 | 63 | — |
| Aug 17 | 8/16 | 60 | 61 | 29 |
| Aug 24 | 8/23 | 57 | 60 | 45 |
| Aug 31 | 8/30 | 57 | 58 | 62 |
| Sep 8 | 9/6 | **56** (window minimum) | 58 | 76 |
| Sep 14 | 9/13 | 57 | 58 | 86 |
| **Sep 21** | **9/20** | 57 | 58 | **92 ← first week ≥90** |
| Sep 28 | 9/27 | 57 | 58 | 96 |
| Oct 5 | 10/4 | **54** | 57 | (table dropped) |

- **What the old exit text would need is now observable for the whole 2026 window.** Corn's minimum before 90% dented was 56% (9/6). Soy's minimum was 58%. Corn printed 54% on 10/4, after dented passed 90%.
- The adjudication is AEOLUS's. I report the readings and do not grade the exit.
- **Fragility:** the release-file node ID (`796095`) cannot be predicted, so the command must scrape the listing page first. The ESMIS pager exposes only about the last 12 months of releases.

---

## 4. Base-rate tables (production vs trailing 5-yr mean, %, MY ≤2025)

### 4a. Regions WITH a signal

**South Africa corn** (DJF anchor, harvest 1966–2025, n=60; corr(ONI, metric) = −0.47; AUC 0.70)

| Regime | n | mean | median | p25 | p10 | ≤−15% | ≤−25% | ≤−45% |
|---|---|---|---|---|---|---|---|---|
| Strong El Niño ≥1.5 | 6 | −38.5 | −36.8 | −54.0 | −61.4 | **5/6** | 4/6 | 2/6 |
| El Niño ≥0.5 | 21 | −7.7 | −8.1 | −24.1 | −45.1 | **8/21 (38%)** | 5/21 | 3/21 |
| Neutral | 17 | +17.9 | +9.1 | +1.8 | −8.4 | **1/17 (6%)** | 0/17 | 0/17 |
| La Niña | 22 | +13.2 | +13.5 | −9.1 | −15.1 | 3/22 (14%) | 2/22 | 1/22 |

- p values: strong vs neutral at ≤−15% = 0.001; El Niño vs neutral = 0.023 (≤−15%) and 0.041 (≤−25%).
- **Strong years:** 1973 −40 · 1983 −59 · 1992 −64 · 1998 −21 · 2016 −33 · 2024 −14.
- **Near-miss counterexample:** 2010 (DJF +1.47) at **+30%**.
- **Bimodal:** weak and moderate El Niños sit near zero, while strong events are severe.

**Southern Africa-4 aggregate** (SA + Zambia + Malawi + Zimbabwe, DJF, n=60; corr −0.50)

| Regime | n | median | p25 | p10 | ≤−15% | ≤−25% |
|---|---|---|---|---|---|---|
| Strong El Niño | 6 | −32.1 | −44.6 | −56.8 | **6/6** | 4/6 |
| El Niño | 21 | +1.7 | −22.6 | −35.2 | 8/21 | 5/21 |
| Neutral | 17 | +8.0 | −2.2 | −9.5 | **0/17** | 0/17 |
| La Niña | 22 | +14.7 | −4.2 | −10.4 | 2/22 | 1/22 |

- El Niño vs neutral at ≤−15%: p=0.004.
- **Robust to the anchor season:** with ONI ≥1.5, NDJ gives 5/7, DJF 6/6 and JFM 5/5, against 0/17–0/22 for neutral. The NDJ misses are 1966 and 2010.

**Zimbabwe alone** (DJF): strong 6/6 ≤−15% (median −49.9%) vs neutral 4/17 (p=0.002). Noisy: neutral p10 is −30.7%.
**Zambia alone:** no broad signal (El Niño 5/21 vs neutral 4/17, AUC 0.53), though strong is 3/6.
**Malawi:** no broad signal (AUC 0.45). ⚠️ PSD Malawi MY1993 = **200** kMT, between 660 and 1,050 — likely a dropped zero. Excluding harvests 1993–98 does not change the verdict.

**Australia wheat** (ASO, MY 1965–2025, n=61): **KB-103 reproduced exactly.**

| Regime | n | mean | median | p25 | p10 | ≤−15% | ≤−20% | ≤−30% | ≤−40% |
|---|---|---|---|---|---|---|---|---|---|
| Strong El Niño | 4 | −4.4 | −10.8 | −14.1 | −14.5 | **0/4** | 0/4 | 0/4 | 0/4 |
| El Niño | 16 | −14.8 | −14.3 | −30.1 | −43.6 | 7/16 | 7/16 | 4/16 | 2/16 |
| Neutral | 31 | +13.3 | +10.0 | −3.3 | −19.5 | 5/31 | 2/31 | 2/31 | 0/31 |
| La Niña | 14 | +23.5 | +28.4 | −7.5 | −23.4 | **4/14** | 2/14 | 0/14 | 0/14 |

- p values: El Niño vs neutral = 0.046 at ≤−15%, 0.0042 at ≤−20%. corr −0.44; AUC 0.79.
- **Strong years:** 1965 −15 · 1997 +19 · 2015 −14 · 2023 −8.
- **Threshold sensitivity:** 1972 (+1.49) at −33 and 1982 (+1.45) at −37 fall just below the 1.5 cut.

**India rice** (JAS, n=61; corr −0.42; AUC 0.81): El Niño median −3.0% vs neutral +8.9%. ≤−3%: El Niño 5/11 vs neutral 3/38 (p=0.009). ≤−15%: 1/11 vs 0/38.
- The strong JAS subset is n=2 (1997 +5.1, 2015 +0.7), with no hit.
- **JAS 2026 = +2.16 is the highest JAS in the 1950–2026 record** (previous high 1997 +1.79), so 2026 is out of sample.

### 4b. Regions where the signal is ABSENT (absence is a result)

| Crop | Anchor | ≤−15% El Niño vs neutral | AUC | Why |
|---|---|---|---|---|
| Malaysia palm lag0 / lag1 | OND E | 0/20 vs 0/15 · 0/21 vs 0/15 | 0.51 / 0.45 | Neutral median is **+19%** (structural growth), so ≤−15% is never reached. On a **YoY** basis, ≤−5% fires in **strong 3/5** vs neutral 1/15 (p=0.032, n=5): 1982 −5.1, 1997 −5.5, 2015 −11.0. **Strong 2023 = +7.2%**. Lag1 shows nothing. |
| Indonesia palm lag0 / lag1 | OND E | 0/20 vs 0/15 · 0/21 vs 0/15 | 0.70 / 0.58 | Neutral median **+42%**. YoY ≤0: strong 3/5 vs neutral 0/15 (p=0.009); the worst El Niño YoY is −7.1% (1997). |
| India wheat | OND N−1 / JAS N−1 | 0/22 ≤−10% · 0/11 | 0.57 / 0.69 | No year in 61 is ≤−10% vs trailing 5. GEOGLAM (10/1) says El Niño tends to favour South and Central Asian rainfed wheat. |
| Thailand rice | ASO | 1/16 vs 1/31 (only 2015 −21.1) | 0.52 | Strong 1/4 |
| Vietnam rice | OND N / N−1 | 0/22 vs 0/17 | 0.57 / 0.51 | Mapping unverified |
| Argentina soy / corn | DJF N+1 | 0/15 · 1/21 | 0.46 / 0.54 | El Niño is a **tailwind**; La Niña is the hazard (soy ≤−15% La Niña 3/16) |
| Brazil soy / corn | DJF N+1 | 0/15 · 1/21 | 0.55 / 0.53 | Corn ≤−10% El Niño 4/21 vs neutral 0/18 (p=0.07), weak |

### 4c. Current reads vs trailing 5-yr (USDA PSD, Oct-9-2026 vintage)

| Crop (the El Niño crop) | USDA kMT | 5-yr mean | vs 5-yr | YoY | Note |
|---|---|---|---|---|---|
| SA corn, 2027 harvest (PSD MY2026) | 16,500 | 16,421.4 | **+0.5%** | −8.8% | Aug, Sep and Oct all 16.50: pre-planting placeholder |
| Australia wheat MY2026 | 31,000 | 34,567.4 | **−10.3%** | −13.9% | Raised **28.00 → 31.00 in the Sep 11 WASDE**; Oct unchanged |
| India rice MY2026 | 147,000 | 141,451.8 | +3.9% | −4.6% | Kharif already in harvest |
| Thailand rice MY2026 | 20,300 | 20,466.0 | −0.8% | −1.9% | — |
| Malaysia palm MY2026 (lag0) | 19,600 | 19,166.2 | +2.3% | −3.0% | — |
| Indonesia palm MY2026 (lag0) | 45,000 | 44,440.0 | +1.3% | −3.6% | — |
| Zambia, Malawi, Zimbabwe 2027 harvest | — | — | — | — | **Not in PSD until USDA adds the new market year (May 12, 2027 WASDE).** PSD MY2026 for these is the already-harvested 2026 crop (Zambia 4,938 = +65%; not the El Niño crop). Southern Africa-4 trailing mean for 2027 = 24,275 kMT |

**SA CEC 8th estimate, 29 Sep 2026 (primary PDF), 2026 crop:**
- Commercial maize **17,522,840 t** (7th estimate 17,401,840)
- Total maize RSA, commercial + non-commercial: **18,217,865 t**
- 2025 final total: 17,346,500 t

The 2025 total equals USDA MY2024 (17,345). **The CEC total and USDA SA corn are the same basis, and the CEC publishes first.**

**FAO Food Price Index** (primary CSV, released Fri **2 Oct 2026**, September data):

| Index | Value | m/m | y/y | Context |
|---|---|---|---|---|
| FFPI | **136.0** | +2.0 / +1.5% | +5.8% vs Sep 2025 (128.6) | — |
| Cereals | **122.8** | +6.0 / +5.1% | +17.2% vs 104.8 | Highest since Dec 2023 (122.8) |
| Vegetable oils | **198.6** | +1.7 / +0.9% | +18.3% vs 167.9 | Highest since Jun 2022 (211.8) |

- The FAO page text says the oils index rose +1.8. The CSV shows +1.7 (196.9 → 198.6).
- Next releases: **6 Nov 2026, 4 Dec 2026** (from the FAO page via WebFetch summary: secondary).

---

## 5. Dated catalysts (next ~9 months)

| Date | Event | Region | Verified at publisher? |
|---|---|---|---|
| **Mon 12 Oct 2026** | MPOB September data (then the 10th of each month by 12:30 MYT, moved off weekends) | MY palm | ✅ bepi.mpob.gov.my (numbers behind login) |
| **Tue 27 Oct 2026** 14:30 SAST | CEC: **Summer intentions to plant (2027)** + 9th forecast for the 2026 crop | SA corn | ✅ CEC_Dates_2026.pdf |
| **Tue 10 Nov 2026** | WASDE + PSD refresh | all | ✅ usda.gov |
| Thu 26 Nov 2026 | CEC: final 2026 summer crop estimate | SA | ✅ |
| **Tue 1 Dec 2026** 8am AEST | ABARES Australian Crop Report (December) | Aus wheat | ⚠️ secondary (search relay; agriculture.gov.au timed out) |
| **Thu 10 Dec 2026** | WASDE | all | ✅ |
| 2027: Jan 12 · Feb 10 · Mar 10 · Apr 9 · **May 12** · Jun 11 · Jul 9 | WASDE. **May 12** = first 2027/28 market year: Zambia, Malawi, Zimbabwe 2027 crops and India rabi wheat appear in PSD | all | ✅ |
| ~mid-Feb 2027 / ~late Feb 2027 | CEC preliminary area planted; **revised area + 1st production forecast for the 2027 crop** | SA corn | ⚠️ **projection** by analogy to the 2026 sheet (12 Feb / 26 Feb 2026). The 2027 sheet is not yet published |
| ~late Mar / Apr / May / Jun 2027 | CEC 2nd–5th production forecasts | SA corn | ⚠️ projection (2026 dates: 26 Mar, 23 Apr, 26 May, 25 Jun) |
| ~early Nov 2026, monthly | GEOGLAM Crop Monitor for Early Warning (No. 120 published **Oct 1, 2026**: *"the developing El Niño event makes poor yield outcomes likely in Zimbabwe and South Africa"*) | S. Africa, SE Asia | ✅ issue date; ⚠️ next date inferred (first-Thursday pattern) |
| — | FEWS NET Southern Africa: latest is *"Food Security Outlook June 2026 – January 2027"* (no date on page); next outlook date not listed | S. Africa | ⚠️ no date available |
| ~early Mar 2027 | CPC DJF 2027 ONI (confirms the strong-regime conditioning for the SA band) | ENSO | not checked |

**Strongest, most discriminating regions with resolution inside ~9 months:**
1. **South Africa corn.** Planting is Oct–Dec 2026, with the first CEC crop forecast around late Feb 2027, harvest Apr–Jun 2027 and USDA fully updated by the May 12 WASDE. The Southern Africa-4 aggregate confirms from May 12, 2027.
2. **Australia wheat.** Harvest is Oct–Dec 2026, with the ABARES report on Dec 1 and WASDE on Dec 10 and Jan 12. It is a weaker discriminator, and the strong subset is not worse.

---

## 6. PROPOSALS (not registered; AEOLUS adjudicates)

**(a) Substitute C2 exit instrument.** Two legs.
- **A1: restore the US leg as it was written.** Use the ESMIS Crop Progress command in §1.
  - It is keyless and verified on 15 weekly files.
  - It replaces the dead `nass.usda.gov` path in KB-092 and removes the INSTRUMENT-DEAD state for the *instrument*.
  - Its window for 2026 closed in the week ending 9/20 (corn dented 92%). The readings are in §3; the grading is AEOLUS's.
- **A2: an El Niño-correct exit for the 2026-27 event.**
  - **Instrument:** USDA PSD Online `psd_grains_pulses_csv.zip`. SA corn PSD MY2026 production vs the trailing 5-yr mean (16,421.4 kMT). Graded on each WASDE day. CEC "Total Maize RSA" is the same-basis leading read from the late-Feb 2027 first forecast.
  - **Proposed flip test, testable at a dated release:**
    - **UP:** any CEC or WASDE read **≤13,958 kMT (−15%)**.
    - **DOWN (a channel-kill for this event, not a thesis-kill):** DJF 2027 ONI ≥1.5, AND the May 12, 2027 WASDE shows SA corn **>13,958**, AND Australia's final wheat figure is >−15%.
  - **Archive each month's zip.** PSD keeps only the current vintage, which is why the September revision was invisible in the PSD file (KB-182).

**(b) Band for the best region: South Africa corn**, PSD MY N (= the N+1 harvest), conditioned on DJF ONI, production vs trailing 5-yr mean. Levels are anchored to El Niño quantiles (KB-103 method).

| Level | Threshold | 2027 level (kMT) | Anchor | Fire rate (strong · El Niño · neutral · La Niña) |
|---|---|---|---|---|
| Yellow | ≤−15% | ≤13,958 | Uniform with Australia; neutral-tail cut (neutral p10 is −8.4) | 5/6 · 8/21 · 1/17 · 3/22 |
| Orange | ≤−25% | ≤12,316 | El Niño p25 (−24.1) | 4/6 · 5/21 · 0/17 · 2/22 |
| Red | ≤−45% | ≤9,032 | El Niño p10 (−45.1) | 2/6 · 3/21 · 0/17 · 1/22 |

Caveats attached to this band:
- **Deviation from the KB-103 rule:** the SA El Niño *median* is only −8.1% because the distribution is bimodal, so Yellow is set at −15% rather than at the median.
- **Strong subset is n=6, with a threshold-edge counterexample:** 2010 (DJF +1.47) was +30%. Event flavour (eastern vs central Pacific) was not tested.
- **≤−15% is not El Niño-exclusive:** La Niña fires 3/22, including the second-year drought of 1984 (−49%).
- **Basis:** levels come from revised actuals; reads will be forecast vintages. A USDA/CEC forecast-error base rate is NOT done (§7).
- **Confirming leg (optional), Southern Africa-4 aggregate:** Yellow ≤−15% (≤20,634 kMT for 2027). Strong 6/6 · El Niño 8/21 · neutral 0/17 (p=0.004). Gradeable only from May 12, 2027.

**(c) Australian wheat band (KB-103): register as-is, but as the SECOND leg, not the lead.**
- **For as-is:**
  - It reproduces exactly at n=61.
  - The levels were pre-specified.
  - Moving Yellow to −20% would lower p from 0.046 to 0.0042 with the same 7/16 El Niño hits, but that cut sits in an empty gap in the sample (−14.8 → −24.4). This is post-hoc, so I do not recommend it without out-of-sample support.
- **Against making it the lead leg:**
  - The strong subset is 0/4 ≤−15%.
  - La Niña fires more often than neutral (4/14 vs 5/31).
  - The basis mismatch on forecast vintages is still open.
- **Grade from the Dec 2026 vintage onward**, after harvest has progressed.

---

## 7. What I could NOT do

1. **No USDA forecast-vs-final error base rate** (the next step registered in KB-103). PSD keeps only the current vintage. What I tried:
   - The ESMIS WASDE pager and `?date=` filter return only Nov 2025 onward.
   - `usda.gov/.../historical-wasde-report-data` returns **403** to both curl and WebFetch.
   - Older `usda.gov/oce/commodity/wasde/wasdeMMYY.txt` paths return 404.
2. **SA Department of Agriculture site unreachable:** `old.dalrrd.gov.za` timed out, `www.dalrrd.gov.za` failed DNS, and `nda.gov.za` failed SSL. I used the Department's PDFs hosted on sagis.org.za instead. The **2027 CEC dates sheet is not yet published.**
3. **ABARES schedule page timed out** (HTTP/2 and HTTP/1.1). The Dec 1 date is secondary.
4. **MPOB monthly statistics are behind a login.** No monthly palm series was pulled, so palm stays base-rated only at the annual PSD resolution.
5. **Zimbabwe and Malawi PSD irregularities** (convention break; MY1993=200) are handled by hand, with sensitivity runs. Neither is confirmed by USDA.
6. **No detrending.** The trailing-5 metric carries structural growth, which mechanically blinds it to fast-growing series (palm, India wheat). This is a property of the metric, not a finding about the weather.
7. **FEWS NET and GEOGLAM next-issue dates were not verifiable.** GEOGLAM, FEWS NET and FAO page text came through WebFetch's summariser and should be treated as relayed (the FFPI numbers themselves are from the primary CSV).
