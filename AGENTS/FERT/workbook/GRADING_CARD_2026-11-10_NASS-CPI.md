# GRADING CARD — NASS November Crop Production (T8, D:L761) + October CPI food at home (T3), 2026-11-10 (pre-registered)

**Frozen:** 2026-11-09, at commit (D:L761 prep session; PROME packet `inbox/processed/2026-11-09_from-PROME_due-rows-wake.md`). **Model:** market-agent blueprint §5 print-grading contract, same form as `GRADING_CARD_2026-11-03_MOS-CF-Q3.md`.
**Freeze rule:** everything above § RESULTS is a no-edit honesty record. After the prints only RESULT cells fill. A pin that turns out ambiguous gets a **dated addendum below § RESULTS**, never an in-place edit.
**What this card cannot do:** fire or grade a gate (G5 grades only on DTN, T4 11/11; G3 only on a Chinese government action). It creates no prediction and moves no band. G4 stays declined; nothing here re-opens it.

## Schedule (verified 2026-11-09)

| Print | Release | Date source |
|---|---|---|
| BLS CPI, October 2026 | Tue 2026-11-10 08:30 ET | BLS November schedule, read 10/26 (T3 note) |
| NASS Crop Production, November | Tue 2026-11-10 12:00 PM ET | ESMIS publication page "Upcoming releases Nov 10 2026 12:00 PM, Dec 10 2026 12:00 PM", curl 2026-11-09 12:59 ET |

**Sources, in order.** CPI: FRED API via `FORGE/tools/market-data/fetch.py` (`fred_fetch`, CUSR0000SAF11 SA, CUUR0000SAF11 NSA) → BLS release text for the published one-decimal change (bls.gov has 403'd this box; a mirror of the BLS table is labelled MIRROR). NASS: ESMIS release file `crop1126.txt` (find the release ID on https://esmis.nal.usda.gov/publication/crop-production, never guess it) → never a search summary (the 9/28 trap, `KB-FERT-051`).

## Baselines (read before the print)

| Item | Baseline | Basis |
|---|---|---|
| US corn for grain yield | **181.2 bu/acre** (Oct forecast); Sep **178.8** (revised); 2025 **186.5** | NASS Crop Production **reissued 2026-10-23**, release-files/796123/crop1026.txt. ⚠️ The original 10/09 file (796101) read Sep 178.5 and "+2.7"; the reissue revised Sep KS/NE/US, so Oct is **+2.4** vs Sep. Oct level unchanged |
| US corn for grain production | **16,033,944** thousand bu | same file |
| US corn area harvested | **88,506** thousand acres (2025: 90,948) | same file |
| US soybean yield | **53.1 bu/acre** (record) | same file |
| Fertilizer words in the report | **0** matches for fertiliz / nitrogen / nutrient | grep of the reissued October text file |
| Food at home SA index | **321.111** (Sep 2026); Aug 321.335 | FRED CUSR0000SAF11, 2026-11-09 |
| Food at home NSA index | **321.758** (Sep 2026) | FRED CUUR0000SAF11, 2026-11-09 |
| October 2025 index | **MISSING** in both SA and NSA | FRED, 2026-11-09 (last year's shutdown gap; Sep 2025 and Nov 2025 present) |

## NASS — questions and pins (T8)

| # | Question | Measurement pin | Records to |
|---|---|---|---|
| N1 | US corn yield | November forecast bu/acre as printed in the US row; change vs **181.2** and vs 2025 **186.5** | KB; FL-FERT-05 notes |
| N2 | US corn production | thousand bu as printed; change vs 16,033,944 | KB |
| N3 | Harvested area | thousand acres as printed vs 88,506. A change here bears on the planting channel; an unchanged area means NASS made no area call this month | KB |
| N4 | Soybean yield | bu/acre vs 53.1. Context only | KB |
| N5 | Attribution | grep the November text for fertiliz / nitrogen / nutrient; quote any hit with its line. NASS has not attributed yield to inputs this season | KB; FL-FERT-05 |
| N6 | Reissue check | whether the November file states any revision to the October forecast; record it before using October as the base | KB |

## CPI — questions and pins (T3)

| # | Question | Measurement pin | Records to |
|---|---|---|---|
| P1 | Food at home m/m, SA | **BLS published one-decimal SA change governs**; record the index-derived figure (from 321.111) beside it. Index level for +0.4% = **322.395** (computed). If the two straddle 0.4, record AMBIGUOUS in an addendum and move nothing | KB; Exit rail "Transmission question" |
| P2 | Food at home y/y, NSA | Only as BLS prints it. October 2025 is missing, so if BLS prints no 12-month change, record **NOT PUBLISHED**. ⛔ Never compute it from Sep or Nov 2025 | KB |
| P3 | Four-month run | Jun +0.19 · Jul −0.07 · Aug +0.04 · Sep −0.07 (index-derived, `KB-FERT-073`); append October | STATUS V6 |

## Pre-registered consequences (decided now, applied after)

| Item | Moves if | Otherwise |
|---|---|---|
| **FL-FERT-05** (shortage → yield/acreage hit), REFUTED | Re-opens to UNTESTED only if N5 finds NASS attributing yield or area to fertilizer or nutrient application | **Stays REFUTED.** A yield cut with no attribution is logged UNATTRIBUTED, as in October |
| **combo:under-application-yield** (`KB-FERT-135`) | Its "would matter" fact is N5 attribution only | November yield added as a member or counterevidence in its direction; no score moves |
| **Transmission question** (Exit rail) | P1 ≥ +0.4% is recorded as the first month at the line; nothing fires (G4 declined) and the rail dies only after the November print | P1 < +0.4%: one more month under the line; rail still open to the November print |
| **V6 food-CPI transmission** (score 1) | → 2 only if P1 ≥ +0.4% | HELD at 1 |
| **FERT-05** (March, provisional MISS) | Final grade waits for the December CPI (mid-Jan 2027); October is a data point only | — |
| **T8 row** | After N1–N6: re-date to the NASS Crop Production Annual Summary [EST January 2027, verify on ESMIS] as the final 2026 yield read, then retire | — |
| **T3 row** | After P1–P3: re-date to the November CPI date [verify on the BLS schedule] | — |

## RESULTS

| # | Result | Read at |
|---|---|---|
| N1 | | |
| N2 | | |
| N3 | | |
| N4 | | |
| N5 | | |
| N6 | | |
| P1 | | |
| P2 | | |
| P3 | | |
