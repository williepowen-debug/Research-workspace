# A3 — Rent band successor: "% of top-100 with negative rent YoY" (Zillow ZORI, with Apartment List cross-check)

> 📁 **Filed 2026-09-29 by HOMER from a research subagent's output.** Files this report names "in this directory" (part files, scripts, series CSVs) are in `reports/2026-09-29_A3_evidence/`. Large raw downloads (source CSVs, PDFs) were not retained; their URLs are given below. ⛔ Proposed levels here are NOT installed: they are a Will-gated retune (packet in `PROME/inbox/`).

Compiled 2026-09-29 (UTC) · read-only research for HOMER · scripts in this directory: `zori_neg.py`, `al_neg.py`, `summ.py` · outputs: `zori_neg_series.csv`, `al_top100city_neg_series.csv`

## 0. Headline: the dead feed can be rebuilt, and Zillow measures something different

| # | Finding | Basis |
|---|---|---|
| 1 | **Apollo/Slok's "56%" is Apartment List data.** The Jan-2026 Apollo *US Housing Outlook* chart is titled *"100 largest US cities: Share of cities with negative rent growth: 56%"*, and its source line reads **"Source: Apartmentlist.com, Apollo Chief Economist"**. | Apollo deck PDF `USHousingOutlookJan2026_v2.pdf` (info as of January 2026), fetched 2026-09-29, extracted text line 4457 |
| 2 | **I rebuilt the statistic from Apartment List's public CSV, and it matches.** Taking the 100 largest cities by population (overall bed size, YoY < 0), the rebuild gives **56% for Dec-2025**, 57% for Jan-2026 and 56% for Feb-2026. | `Apartment_List_Rent_Estimates_2026_09.csv`, fetched 2026-09-29T14:30Z |
| 3 | ⇒ **The premise that the band has no live feed is false.** The original source is public, updated monthly and current through **Sep-2026, which reads 46%**. On the old 20/40/55 levels that is **Orange**: Red (>55%) is the highest level not crossed, and the reading is 9pp below it. Red was crossed in 7 of the last 13 months (Dec-25 to Jul-26, excluding Jun-26, which printed exactly 55). | same |
| 4 | **Zillow ZORI on the top-100 metros is a different statistic, not a substitute on the same scale.** Jan-2026: **Zillow 11% vs Apartment List 57% / Apollo 56%**, a gap of about 45pp. The top-100 median YoY in Jan-2026 was **+2.3% on Zillow vs −0.5% on Apartment List**. Zillow's distribution sits about 2.8pp to the right, so only its left tail is negative. | §3 |
| 5 | Either way, **adopting a feed and levels for this band is Will's decision.** Option A (the Apartment List rebuild) keeps the source and the method, so the 20/40/55 levels can arguably carry over. Option B (Zillow) needs the new levels derived in §4. | HOMER CLAUDE.md, rent-band re-spec note |

⚠️ **Caveat on #2.** The rebuild uses the Sep-2026 file vintage: Apartment List revises history, and population comes from the current file. Apollo's exact data month (Dec-25 or Jan-26) is not stated on the slide. A ±1pp match is what the evidence supports; "exact" is not.

## 1. Source record

| Item | Value |
|---|---|
| Zillow URL (confirmed HTTP 200) | `https://files.zillowstatic.com/research/public_csvs/zori/Metro_zori_uc_sfrcondomfr_sm_month.csv` |
| Series | ZORI, all homes (SFR + condo/co-op) **plus multifamily**, **smoothed**, monthly, not seasonally adjusted (the `_sm_sa_` variant also exists, HTTP 200). ⚠️ I could not read the label on the Zillow data page (zillow.com/research/data returned **403** to both curl and WebFetch). The description comes from the filename and from Zillow's ZORI methodology page. The methodology describes a repeat-rent index over the 35th–65th percentile of asking rents, weighted to the rental stock, then smoothed with a 3-month (exponentially weighted) moving average. |
| Download time | **2026-09-29T14:28:16Z** · 1,066,873 B · sha256 `4177880b…0b22f4c38` · server `last-modified: 2026-09-16 02:11:30 GMT` |
| Latest month in file | **2026-08** (column `2026-08-31`) · first month 2015-01 |
| Rows | 750 = 1 national row (`United States`, excluded) + 749 MSAs |
| No unsmoothed metro ZORI | `Metro_zori_uc_sfrcondomfr_month.csv` and the `_raw_` variant both returned **404** |
| Apartment List URL | `https://assets.ctfassets.net/jeox55pd4d8n/1aoESqmaesHQkkZaIOJN8g/0c954c4b9906672e3ce6cdf38346b394/Apartment_List_Rent_Estimates_2026_09.csv` (link scraped from apartmentlist.com/research/category/data-rent-estimates) · fetched **2026-09-29T14:30:19Z** · sha256 `aa05b458…a2d3a644` · latest month **2026-09** · starts 2017-01, so YoY starts 2018-01 |

**Method.** For each metro and month, YoY = value(t) / value(t−12) − 1, computed only when both ends are present. The share is the % of metros with YoY < 0.
- Universe (a) is every MSA with a valid YoY that month.
- Universe (b) is the **100 lowest Zillow SizeRank** MSAs. SizeRank 33 is absent from the file, so (b) spans SizeRank 1–101. Membership is fixed at the **Sep-2026 file's** ranking.
- Three (b) metros have no 2015-01 value (Springfield MA, Syracuse NY, Jackson MS), so n was 97–99 in 2016–2017.

## 2. Universe (b) — Zillow top-100 metros, % with negative rent YoY (full monthly series)

Cells are % of metros. When n = 100 the % equals the count. Other n values are shown in brackets.

| Year | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 0.0 (n=97) | 1.0 (n=98) | 1.0 (n=98) | 0.0 (n=98) | 0.0 (n=98) | 0.0 (n=98) | 1.0 (n=98) | 1.0 (n=98) | 4.1 (n=98) | 3.1 (n=98) | 3.1 (n=98) | 4.1 (n=98) |
| 2017 | 3.0 (n=99) | 1.0 (n=99) | 1.0 (n=99) | 0.0 (n=99) | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 1 |
| 2018 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 |
| 2019 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2020 | 1 | 1 | 1 | 1 | 1 | 3 | 4 | 5 | 9 | 10.1 (n=99) | 9 | 10 |
| 2021 | 10 | 8 | 7 | 7 | 5.1 (n=99) | 3 | 2 | 0 | 0 | 0.0 (n=99) | 0 | 0 |
| 2022 | 0 | 0 | 0 | 0 | 0.0 (n=99) | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| 2023 | 1 | 1 | 1 | 1 | 1 | 5 | 5 | 10 | 12 | 7 | 10 | 8 |
| 2024 | 8 | 6 | 9 | 8 | 8 | 5 | 6 | 6 | 6 | 5 | 5 | 5 |
| 2025 | 5 | 5 | 4 | 5 | 6 | 6 | 9 | 9 | 10 | 10 | 10 | 9 |
| 2026 | 11 | 11 | 15 | 13 | 10 | 9 | 7 | 6 | — | — | — | — |

### Summary statistics by regime

| Universe | Regime | Window | Months | Min (month) | Median | Mean | Max (month) |
|---|---|---|---|---|---|---|---|
| **(b) Zillow top-100** | pre-2020 normal | 2016-01..2020-02 | 50 | 0.0 (2016-01) | 1.0 | 0.8 | **4.1 (2016-09; 2016-12 also 4.1)** |
| (b) | COVID dip | 2020-03..2021-06 | 16 | 1.0 (2020-03) | 6.0 | 5.8 | **10.1 (2020-10; 10 of 99)** |
| (b) | boom | 2021-07..2022-12 | 18 | 0.0 | 0.0 | 0.2 | 2.0 (2021-07) |
| (b) | 2023–26 soft patch | 2023-01..2026-08 | 44 | 1.0 (2023-01) | 6.5 | 7.0 | **15.0 (2026-03)** |
| (b) | ALL | 2016-01..2026-08 | 128 | 0.0 | 1.0 | 3.5 | 15.0 (2026-03) |
| **(a) Zillow all MSAs** | pre-2020 normal | 2016-01..2020-02 | 50 | 0.7 | 2.3 | 2.4 | 6.0 (2016-12) |
| (a) | COVID dip | 2020-03..2021-06 | 16 | 1.6 | 4.2 | 3.7 | 6.0 (2020-10) |
| (a) | boom | 2021-07..2022-12 | 18 | 0.0 | 0.3 | 0.4 | 1.7 |
| (a) | 2023–26 soft patch | 2023-01..2026-08 | 44 | 0.8 | 4.5 | 4.4 | **8.9 (2026-03)** |
| (a) | ALL | 2016-01..2026-08 | 128 | 0.0 | 2.5 | 3.0 | 8.9 (2026-03) |
| Apartment List top-100 cities | pre-2020 | 2018-01..2020-02 | 26 | 7.1 (2019-12) | 10.2 | 11.9 | 18.8 (2018-01) |
| Apartment List | COVID | 2020-03..2021-06 | 16 | 13.0 | 37.5 | 35.6 | **61.0 (2020-06)** |
| Apartment List | boom | 2021-07..2022-12 | 18 | 0.0 | 1.0 | 4.8 | 26.0 (2022-12) |
| Apartment List | 2023–26 | 2023-01..2026-09 | 45 | 24.0 | 51.0 | 50.9 | **72.0 (2023-08)** |

Universe (a) by year (**n roughly triples over the sample, from 211 to 602**, so the composition drifts):

| Year | (a) n range | (a) % neg min–max | (a) Dec |
|---|---|---|---|
| 2016 | 211–232 | 1.8–6.0 | 6.0 (2016-12) |
| 2017 | 234–265 | 1.5–6.0 | 1.5 (2017-12) |
| 2018 | 267–282 | 0.7–3.4 | 1.8 (2018-12) |
| 2019 | 284–294 | 0.7–2.4 | 2.0 (2019-12) |
| 2020 | 299–302 | 1.7–6.0 | 4.7 (2020-12) |
| 2021 | 300–309 | 0.0–4.7 | 0.0 (2021-12) |
| 2022 | 315–348 | 0.0–1.1 | 1.1 (2022-12) |
| 2023 | 367–427 | 0.8–5.3 | 4.7 (2023-12) |
| 2024 | 437–500 | 2.1–5.4 | 2.6 (2024-12) |
| 2025 | 508–558 | 2.4–7.3 | 7.2 (2025-12) |
| 2026 | 573–602 | 4.5–8.9 | 4.5 (2026-08) |

## 3. Latest readings, and the Jan-2026 comparison

| Measure | Latest | Jan-2026 | Dec-2025 |
|---|---|---|---|
| (b) Zillow top-100 metros | **6% (6/100), 2026-08** | **11% (11/100)** | 9% |
| (a) Zillow all MSAs | **4.5% (n=602), 2026-08** | 8.7% (n=573) | 7.2% (n=558) |
| Apartment List top-100 cities (rebuild) | **46%, 2026-09** (52% 2026-08) | 57% | 56% |
| Apollo/Slok (published) | — (feed lapsed) | **56%** (deck "as of January 2026") | — |
| Top-100 median YoY: Zillow / Apartment List | +2.4% / −0.1% (2026-08) | **+2.3% / −0.5%** | +2.4% / −0.7% |

**Why the two series differ by roughly 45pp:**
- **Level offset.** Across the overlap, the Apartment List median YoY runs on average **1.95pp below** Zillow's (2.84pp below in Jan-2026). A share-negative statistic is extremely sensitive to where the centre of the distribution sits relative to zero.
- **Geography.** Apartment List ranks **cities** (the principal city only); Zillow ranks **MSAs**, which include suburbs.
- **Method and smoothing.** Both measure asking or new-lease rents, but with different estimation methods, and ZORI is smoothed.

**Lag.** The two series are highly correlated. Zillow(b) against Apartment List has corr **0.82** contemporaneously, peaking at **0.885 with Zillow lagging 2 months** (104-month overlap 2018-01..2026-08). Turning points:

| Episode | Apartment List peak | Zillow peak | Zillow lag |
|---|---|---|---|
| COVID | 2020-06 | 2020-10 | 4 mo |
| 2023 | 2023-08 | 2023-09 | 1 mo |
| 2026 | 2026-04 | 2026-03 | Zillow 1 mo **earlier** |

⇒ **The lag is real on average but not stable.**

## 4. Proposed levels for universe (b), Zillow top-100 metros (only if Option B is chosen)

Counts are shown alongside percentages because at n = 100 one metro equals 1pp. The rung tests use rounded values to avoid float artefacts at the boundary.

| Rung | Level | Basis (sourced from the series' own history) | Last 13 mo (2025-08..2026-08: 9,10,10,10,9,11,11,15,13,10,9,7,6) | Full history, months crossed |
|---|---|---|---|---|
| 🟡 Yellow | **>4.1% (≥5 of 100)** | Top of the pre-2020 normal range: 4.1% = 4 of 98 in 2016-09 and 2016-12. The 2017–2020-02 maximum is lower still (3.0%). | **⛔ PINNED: crossed 13/13** (min 6%, 2026-08). **It is a label in this window, not a signal.** It last failed to cross in **2025-03 (4%)**, so this is a soft-patch regime effect, not a permanent one. | 48 / 128 |
| 🟠 Orange | **>10.1% (≥11 of 100)** | **Sourced, not bracketed:** the COVID-dip peak, 10.1% (10 of 99, 2020-10). | Discriminates: crossed **4/13** (2026-01..04) | 5 / 128 at ≥11 metros (2023-09, 2026-01..04) |
| 🔴 Red | **>15.0% (≥16 of 100)** | The series maximum: the 2023–26 soft-patch peak, 15% (2026-03). The soft patch is the worst episode in the data (worse than COVID at 10.1%). | Never crossed (0/13), so it is untested. | 0 / 128 |

⚠️ **Weaknesses of this ladder:**
1. **Red is anchored to the peak of the episode it would be grading.** It means "worse than anything in 11 years", and those 11 years contain **no GFC and no pre-2015 recession**. It is closer to FL's ">2.9× worst observed decoupling" rung than to a regime anchor like FL's 2013 workout peak. It could be labelled BRACKETED-by-history.
2. **The whole ladder spans 4–15%.** A single metro is a 1pp move, so Orange and Red sit 5 metros apart, and noise from 2–3 metros can flip a band.
3. **Yellow is pinned now.** Under HOMER's reporting rule, the live statement would be *"6% (6/100, Aug-2026) — 5 metros below Orange (≥11), Red (≥16) untested"*.

**For comparison — the old 20/40/55 levels on the Apartment List rebuild (Option A)**, last 13 months (2025-09..2026-09: 47,46,55,56,57,56,57,60,56,55,57,52,46):

| Rung | Test | Status |
|---|---|---|
| Yellow >20% | crossed 13/13 | **PINNED** |
| Orange >40% | crossed 13/13 | **PINNED** |
| Red >55% | crossed **7/13** | discriminates |

The old levels do line up with this source's own history:
- Yellow 20% ≈ the top of pre-2020 normal (max 18.8%, 2018-01).
- Red 55% sits below both stress peaks (COVID 61%, 2023 72%).

⇒ The old ladder appears to have been calibrated on exactly this series.

Apartment List top-100 cities, full series:

| Year | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2018 | 18.8 (n=96) | 18.6 (n=97) | 17.7 (n=96) | 18.8 (n=96) | 14.4 (n=97) | 15.6 (n=96) | 13.5 (n=96) | 11.5 (n=96) | 13.3 (n=98) | 13.3 (n=98) | 9.2 (n=98) | 10.2 (n=98) |
| 2019 | 10.2 (n=98) | 10 | 10 | 8 | 8 | 10.1 (n=99) | 9.1 (n=99) | 9.1 (n=99) | 10.1 (n=99) | 9.1 (n=99) | 10.1 (n=99) | 7.1 (n=99) |
| 2020 | 9.1 (n=99) | 14 | 13 | 24 | 48 | 61 | 57 | 49 | 43 | 40 | 39 | 41 |
| 2021 | 36 | 35 | 30 | 23 | 17 | 14 | 5 | 2 | 2 | 1 | 1 | 1 |
| 2022 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 7 | 13 | 22 | 26 |
| 2023 | 24 | 29 | 32 | 37 | 46 | 61 | 68 | 72 | 71 | 67 | 64 | 57 |
| 2024 | 54 | 52 | 53 | 51 | 51 | 53 | 54 | 47 | 48 | 47 | 49 | 44 |
| 2025 | 43 | 37 | 41 | 42 | 48 | 49 | 51 | 49 | 47 | 46 | 55 | 56 |
| 2026 | 57 | 56 | 57 | 60 | 56 | 55 | 57 | 52 | 46 | — | — | — |

## 5. Limitations

| # | Limitation | Consequence |
|---|---|---|
| 1 | **ZORI starts in 2015-01** (YoY from 2016-01); Apartment List starts in 2017-01 (YoY from 2018-01). | **No GFC observation.** Every "worst episode" anchor is at most a 2020 or 2023–26 event. Red cannot be tied to a crisis regime. |
| 2 | **Smoothing.** ZORI is a 3-month moving average, and YoY is taken on the smoothed level. | The share-negative statistic lags turning points: peak cross-correlation with Apartment List at a 2-month lag, a 4-month lag at the COVID trough. |
| 3 | **Coverage changes.** Universe (a) n goes from 211 (2016-01) to 602 (2026-08); the 2026-08 column has 750 non-null values versus 692 for 2026-06, so newly added metros enter late. | Universe (a) is **not** comparable across time. That is why (b) is the recommended universe. |
| 4 | **Fixed top-100 membership.** It uses the current SizeRank (Sep-2026 file). SizeRank 33 is absent and 3 members lack early data. | This introduces mild look-ahead or survivorship bias. The n = 97–99 months in 2016–17 are flagged in the grid. |
| 5 | **Revisions.** Both the Zillow and Apartment List files are re-estimated each release. | Every figure here is "as published in the files fetched 2026-09-29". A future pull may shift individual months by a metro or two. |
| 6 | **Granularity.** n = 100, so 1 metro equals 1pp. | Zillow levels in the 4–15% range are only a handful of metros apart. |
| 7 | **The Apartment List rebuild is HOMER-computed, not Apollo-published.** | It matched ±1pp at the one published point I hold (56%). One match point is n = 1. |

## 6. Decision framing (for HOMER to route; not a ruling)

- **Option A: grade the old 20/40/55 band on the Apartment List rebuild.** It keeps the source and the method of the original band.
  - Read today: **Orange, 46% (Sep-2026)**. Red was last crossed in Jul-2026 (57%).
  - Yellow and Orange are pinned and Red discriminates.
  - Carry the ±1pp replication caveat.
- **Option B: Zillow top-100 metros with the new levels ≥5 / ≥11 / ≥16 metros.**
  - Read today: **6% (Aug-2026), Yellow with Yellow pinned**.
  - It is a different, lagging, right-shifted statistic.
- Both options are Will-gated per HOMER CLAUDE.md, because each one changes the feed behind a band.

Sources: [Zillow ZORI methodology](https://www.zillow.com/research/methodology-zori-repeat-rent-27092/) · [Apollo US Housing Outlook, Jan 2026 (PDF)](https://www.apolloacademy.com/wp-content/uploads/2026/01/USHousingOutlookJan2026_v2.pdf) · [Apartment List rent estimates data page](https://www.apartmentlist.com/research/category/data-rent-estimates) · Zillow CSV URL above.
