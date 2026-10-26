# MARCO — Spirit seat replacement and Las Vegas Canadian capacity

**As of:** 2026-10-25, session 35; commissioned by Will through PROME packet `0c0221120`. **Data ends July 2026, verified live in both BTS forms and downloaded files** — 86 days after July month-end, approximately a three-month lag. These are flown capacity observations, not current October schedules or bookings. Thesis v3.2 and forecast definitions unchanged.

## Judgment

Domestic supply explains a material part of the observed weakness, but its importance varies by airport and month. At MCO, airlines replaced only 56% of Spirit's lost domestic seats in June and 76% in July; total domestic seats remained below 2025. At FLL replacement rose from 67% in June to 108% in July: July domestic seats and passengers were both above 2025. The old blanket statement that raw declines were mechanically “locked” until Spirit's anniversary was unwarranted. These are net changes by other airlines, not proof that each added seat was a response to Spirit.

**Material correction: MIA was NOT Spirit-free.** The older BTS summary carrier query ends at February 2023 for NK/MIA; that missing coverage was incorrectly treated as an airline exit. Direct segment filings show Spirit at MIA in 2025 and May 2026. Miami-Dade's independently published fiscal seat report also records Spirit in October–December 2025. Withdraw “MIA is the only clean leg.” MIA is a smaller-exposure comparison, not an unaffected causal control. Its existing two-negative-month trigger retains the Will-ruled airport-own basis; the carrier-capacity caveat must accompany any firing. No threshold is redefined or retrospectively graded here.

For LAS, Canadian-airline capacity was down **33.22% in winter November 2025–March 2026** versus the same 2024–25 window. The latest comparable observed month without a known whole-carrier filing hole is **May 2026**, down 31.97% year over year. June/July have known missing filings; their raw declines cannot certify a current grade. Under the existing NV-01 bands, latest complete May is **CRITICAL** (≥20% decline); April was −27.85%, so May alone does not extend the prior sustained ≥30% run. The stale carried December-2025 BREACHED mark is replaced with this dated May grade, and June/July are explicitly unscored. No major-carrier exit is newly established from a missing filing.

## 1. Domestic seat arithmetic — scheduled service, outbound segments only

Source: BTS T-100 Domestic Segment (All Carriers), `GEE`, geography Florida; retain ORIGIN MCO/FLL/MIA and CLASS F. All operating airlines, including regional operators, are retained; Spirit = UNIQUE_CARRIER NK. Compare each 2026 month to the same 2025 month. Seats and passengers come from the same rows. Airport-reported totals and the older market/enplanement summary are different series and are not used in this seat denominator.

`Spirit seat loss = NK seats in 2025 − NK seats in 2026`

`Replacement fraction = (other-airline seats in 2026 − other-airline seats in 2025) / Spirit seat loss`

Only calculate a fraction when the denominator is positive. Negative and >100% outcomes are retained. Above 100% means other-airline net growth exceeds Spirit's lost seats; it is not an error or a measure of individual passenger recapture.

| Airport | Month | NK seats 2025 | NK seats 2026 | Other seats 2025 | Other seats 2026 | Total seats 2025 | Total seats 2026 | Replacement |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| MCO | 5 | 316,570 | 8,395 | 2,185,341 | 2,379,888 | 2,501,911 | 2,388,283 | 63.13% |
| MCO | 6 | 307,708 | 0 | 2,119,926 | 2,291,756 | 2,427,634 | 2,291,756 | 55.84% |
| MCO | 7 | 312,451 | 0 | 2,146,177 | 2,383,830 | 2,458,628 | 2,383,830 | 76.06% |
| FLL | 5 | 339,891 | 9,144 | 921,889 | 1,126,784 | 1,261,780 | 1,135,928 | 61.95% |
| FLL | 6 | 329,152 | 0 | 853,558 | 1,073,323 | 1,182,710 | 1,073,323 | 66.77% |
| FLL | 7 | 337,830 | 0 | 890,497 | 1,254,327 | 1,228,327 | 1,254,327 | 107.70% |
| MIA | 5 | 67,461 | 2,187 | 1,469,991 | 1,499,853 | 1,537,452 | 1,502,040 | 45.75% |
| MIA | 6 | 65,000 | 0 | 1,364,010 | 1,406,867 | 1,429,010 | 1,406,867 | 65.93% |
| MIA | 7 | 62,169 | 0 | 1,389,487 | 1,451,980 | 1,451,656 | 1,451,980 | 100.52% |

Full January–July calculations and passenger offsets: `research/2026-10-25_capacity/domestic_replacement.csv`. Exact Spirit/other/total seat and passenger levels: `domestic_airport_month_groups.csv`; every operating-carrier component: `domestic_carrier_month.csv`.

### Passengers and load factors on those same domestic segments

| Airport | Month | Total seat YoY | Total passenger YoY | Passenger replacement | Distance-weighted load factor 2025 → 2026 |
|---|---|---:|---:|---:|---:|
| MCO | 5 | -4.54% | -0.82% | 93.32% | 84.03% → 86.90% |
| MCO | 6 | -5.60% | -5.44% | 54.39% | 84.44% → 84.32% |
| MCO | 7 | -3.04% | -4.18% | 65.86% | 85.33% → 84.61% |
| FLL | 5 | -9.97% | -7.07% | 73.27% | 82.74% → 84.98% |
| FLL | 6 | -9.25% | -7.58% | 71.89% | 84.59% → 86.09% |
| FLL | 7 | +2.12% | +1.54% | 105.86% | 84.06% → 84.33% |
| MIA | 5 | -2.30% | -1.37% | 69.14% | 83.38% → 83.64% |
| MIA | 6 | -1.55% | -1.73% | 62.42% | 86.25% → 85.52% |
| MIA | 7 | +0.02% | -0.92% | 79.01% | 85.76% → 84.97% |

Load factor = sum(passengers × segment distance) / sum(seats × segment distance); also save the unweighted passenger/seat utilization separately. SEATS is already a monthly segment total: e.g. AS MCO–SAN July 2026 has 3,738 seats over 21 departures = 178 per flight. Do not multiply the monthly seat total by departures again. Operating-aircraft and service definitions are stable across years.

**Interpretation:** MCO June seats and passengers declined almost together; July passenger decline exceeded the seat decline and distance-weighted load factor fell about 0.71 percentage point. FLL July restored aggregate domestic capacity and passenger levels, with load factor roughly flat (+0.27pp). This weakens a generalized domestic-flight collapse claim. It does not establish whether prices, route mix, competition, displaced travelers, demand or absent capacity caused the changes. The older all-service, domestic-plus-international passenger offsets (MCO June 35.6%, FLL 54.5%) remain dated calculations on a different basis; they are not replaced by the scheduled-domestic 54.39% / 71.89% as if the series matched.

## 2. MIA correction — two independent primary-source routes

- BTS direct GEE: Spirit departing scheduled domestic seats **67,461 / 65,000 / 62,169** in May/June/July 2025; **2,187** in May 2026, no reported June/July service. July-2025 Spirit share was **4.28%** of domestic seats (FLL 27.50%, MCO 12.71%). By July-2026 other airlines had added 62,493 MIA seats versus 62,169 lost from Spirit: **100.52% net replacement**. Total seats +0.02%, passengers −0.92%, distance-weighted load factor −0.79pp.
- Miami-Dade Aviation Department, [Fiscal Year Seat Use Summary](https://www.miami-airport.com/library/pdfdoc/Airport%20Stats/FY%202025-2026/December%202025/December%2025%20Fiscal%20Yr%20Seats.pdf), published January 21, 2026, printed page 38 (PDF index 37), report period October–December 2025: Spirit **160,484 domestic departing seats**. This independently disproves an absence since 2023; its quarter and counting system do not need to match the BTS monthly total to establish presence.
- Old `Data_Elements` NK/MIA query: valid airline/airport selections, just **17 rows ending February 2023**, reproduced on this pass. All-carrier MIA is current through July 2026; NK/MCO and NK/FLL are also through July. This is a carrier/airport coverage defect, not proof of zero later operations. `summary_endpoint_coverage.json` records it. A parser that returned rows without checking their period did not detect this gap.

MIA's September report remains pending. Neither this July domestic evidence nor a subtraction across different source bases can identify its August/September demand component. The carrier-adjusted all-three-airport rule still does not fire; the old MCO/FLL adjusted legs are positive, and MIA's missing carrier-summary coverage cannot be manufactured into an adjusted total.

## 3. Las Vegas ↔ Canada — exact geography and carrier families

BTS International Segment All Carriers (`FJE`), geography Canada, CLASS F; retain LAS→Canadian airport and Canadian airport→LAS, both directions. These are **seats on Canada routes**, not Canadian-resident visitor counts or unique tourists. Canadian family selection: Air Canada (AC/QK/RV), WestJet (WS/WR), Porter (PD/P3), Flair (BTS code **07Q**, not its marketing code), Transat (TS) and Lynx (Y9). TS has no observed LAS service in the retrieved 2024–26 interval; its national exit is not a new LAS loss. The all-carrier route tables retain rare third-country/US tag segments separately; the family table below excludes them. No prior Florida international study was rerun as new research.

| Canadian family | Winter 2024–25 seats | Winter 2025–26 seats | Change | Jan–May 2025 seats | Jan–May 2026 seats | Change |
|---|---:|---:|---:|---:|---:|---:|
| ALL CANADIAN | 901,511 | 602,044 | -33.22% | 867,273 | 600,388 | -30.77% |
| Air Canada family | 334,712 | 236,101 | -29.46% | 307,107 | 242,791 | -20.94% |
| WestJet | 359,319 | 266,541 | -25.82% | 370,464 | 269,037 | -27.38% |
| Porter family | 113,124 | 72,204 | -36.17% | 112,332 | 66,660 | -40.66% |
| Flair | 94,356 | 27,198 | -71.18% | 77,370 | 21,900 | -71.69% |

Monthly all-carrier Canada-route capacity (Canadian airlines only produce the same latest May/June/July numbers):

| 2026 month | 2025 seats | 2026 observed seats | Observed YoY | Coverage |
|---|---:|---:|---:|---|
| 1 | 174,355 | 116,823 | -33.00% | No known whole-carrier-month hole detected |
| 2 | 164,136 | 114,416 | -30.29% | No known whole-carrier-month hole detected |
| 3 | 190,774 | 132,012 | -30.80% | No known whole-carrier-month hole detected |
| 4 | 170,394 | 122,936 | -27.85% | No known whole-carrier-month hole detected |
| 5 | 167,872 | 114,201 | -31.97% | No known whole-carrier-month hole detected |
| 6 | 128,576 | 98,260 | -23.58% | INCOMPLETE - Air Canada June filing missing |
| 7 | 114,192 | 90,219 | -20.99% | INCOMPLETE - Porter July filing missing |

### Missing filings and explicit sensitivity, not observations

The source-wide hole scan reproduces QK June-2025, AC June-2026 and PD/P3 July-2026 missing carrier filings from the October 14 study. QK's June-2025 hole does not affect LAS because its adjacent LAS summer months are also zero; P3 has no observed LAS service. AC June and PD July do affect LAS. AC's small adjacent LAS month would fall below the generic 5,000-seat screen, so the source-wide carrier-hole finding is propagated to the airport, not dismissed.

| Month | Missing carrier | Observed total | Explicit assumed addition | Estimated total | Estimated YoY |
|---|---|---:|---:|---:|---:|
| 6 | AC | 98,260 | 3,603 | 101,863 | -20.78% |
| 7 | PD | 90,219 | 11,880 | 102,099 | -10.59% |

June assumes AC equals its May/July LAS mean; July assumes Porter equals June. These are the previously documented local-neighbor/prior-month sensitivity methods, shown separately, **not reported seats, confidence intervals, forecasts or scored grades**. July's apparent −20.99% becomes −10.59% under this assumption, a material classification difference. Missing filings cannot be silently treated as zero, and the assumption is not proof of recovery. Flair's summer zeros persist and its comparator July is also zero; Lynx's exit predates 2025. Neither is imputed as a one-month filing hole. Seasonal suspension versus permanent exit is not established for Flair.

## 4. Coverage, revisions and reproducibility

- Both source forms and actual 2026 files end July; all seven 2026 months are present. Retained sources include 2025 full-year domestic plus 2024–26 Canada/LAS. Domestic hole scan finds no zero-carrier-month candidate affecting May–July MCO/FLL/MIA; its one MCO/YX candidate is November 2025, outside the matched-month study window. A zero-hole scan does not prove every individual filing is complete.
- Re-pulled old all-carrier summary endpoint: **no changes to any overlapping 2024–June-2026 cell in the committed airport baseline**. July total-airport YoYs reproduce the carried October 14 values: MCO −5.28%, FLL −5.97%, MIA −1.47%. Domestic segment passengers differ slightly from market enplanements because through passengers are counted on each segment; they are not forced to reconcile by mixing bases.
- No older raw seat-download snapshot survives in the repository (`scratchpad/t3dl` and scripts are absent). Thus this pass cannot certify every seat-row revision since October 14. Its FJE row counts and named hole values reproduce the prior methodological record. Treat these as a dated/revisable seat vintage; the existing Q3 forecast-vintage cutoff remains February 1, 2027.
- Exact relevant source rows: `GEE_2025_segments.csv`, `GEE_2026_segments.csv`, `FJE_2024_segments.csv`, `FJE_2025_segments.csv`, `FJE_2026_segments.csv`. Full source-geography carrier-month totals retained for hole diagnostics. `source_manifest.json` contains full download row counts, selected fields, URL/payload basis and SHA-256 hashes; complete source ZIPs remain in `/tmp/marco_capacity_20261025` and can be downloaded again from the scripts.
- Manual reproduction from repo root: `.venv/bin/python3 AGENTS/MARCO/research/2026-10-25_capacity/download.py` (network/source vintage may advance), then `analyze.py` from the same directory path (offline saved-input reproduction). `crosscheck.py` checks the old summary source independently and writes only this study directory. No scheduled collector, canonical-baseline overwrite or new standing tracker.
- Validation: geography and service-class perimeters; component totals; exact identity `Spirit loss − other-airline addition = total seat shortfall`; passengers ≤ seats at carrier/month level; ASM/RPM formula and raw aircraft-row check; domestic and Canadian hole scans. Both directions and operating-carrier names are retained in LAS tables.

## 5. Owner consequences and stop point

Capacity replacement is now measured for the commissioned domestic scope; it remains unidentified as a unique demand cause and does not size total domestic-plus-international replacement. The MIA “Spirit-free” claim is retracted across current owner surfaces; archived statements remain history. Latest comparable LAS capacity grade is now dated May CRITICAL, with June/July incomplete; winter capacity is a measured contextual window, not a new forecast definition. Thesis v3.2 and prediction confidence held. No Florida dollar-loss estimate is revived.

WALTER receives the correction and evidence for routing to CORAL/REGINALD/CARL/NEXUS; PROME receives completion. Existing MIA/LVCVA ~October 28, November data reads and February-vintage resolver remain scheduled. The bounded assignment is complete; no running tool is held for a future release and no extra investigation is auto-commissioned.

Primary definitions: [BTS T-100 domestic segment](https://www.bts.gov/browse-statistical-products-and-data/bts-publications/data-bank-28ds-t-100-domestic-segment-data-us), [BTS reporting guide](https://www.bts.dot.gov/sites/bts.dot.gov/files/docs/explore-topics-and-geography/topics/airlines-and-airports/219466/t100-guide-april-2007.pdf), and [USDOT/NTL market versus segment explanation](https://transportation.libanswers.com/faq/166158). Download form URLs and retrieved times are in the manifest. Airport corroboration URL appears in §2.

Consumer verification: CORAL STATUS tourism row and NEXUS_BRIEF demand bullet carry the superseded MIA clean-tell interpretation. WALTER correction packet names those owners/surfaces for routing; other scanner matches were bank/oil prose or a dated receipt, not MIA evidence. No other owner files edited.
