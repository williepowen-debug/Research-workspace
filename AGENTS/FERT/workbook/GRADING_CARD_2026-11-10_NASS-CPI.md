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
| N1 | **179.6 bu/acre** (November 1 forecast). **−1.6** vs 181.2 (Oct) · **−6.9** vs 2025 186.5. Largest state cuts: Illinois 208→200, Michigan 180→170, Indiana 200→195, Missouri 181→176, Nebraska 188→184; Minnesota up 195→204. Record yields forecast in AR, IA, MN, MS, OH, TN, VA | NASS ESMIS release-files/796144/crop1126.txt, HTTP 200, 161,866 B, "Released November 10, 2026", curl 13:07 ET (PRIMARY) |
| N2 | **15,893,419** thousand bu (15.9 billion). **−140,525** thousand bu (−0.88%) vs 16,033,944; −6% vs 2025 16,963,628. NASS: "second highest production for grain on record" | same |
| N3 | **88,506** thousand acres, **unchanged** ("unchanged from the previous estimate", Crop Comments); 2025 90,948. **No area call this month** | same |
| N4 | **53.3 bu/acre**, record (+0.2 vs 53.1; +0.3 vs 2025 53.0). Context only | same |
| N5 | **0** hits for fertiliz / nitrogen / nutrient (system grep and Python, both 0). No cause stated for the corn cut (0 hits for drought / dry-as-condition / disease / heat in the corn narrative). **UNATTRIBUTED** | same |
| N6 | No revision to October stated. The "previous forecast" column reads **181.2**, the reissued October level; "Revision policy: The November 1 production forecast will not be revised". 0 hits for reissue / correct. October base stands as reissued | same |
| P1 | **BLS published: +0.4% SA** (Sep–Oct, Table 2 "Food at home"; release text: "the food at home index rose 0.4 percent"). **Index-derived: +0.443%** (322.535 / 321.111). Line level 322.395 → **both at or above the line, not AMBIGUOUS.** Food (total) +0.5; food away from home +0.5. Groups: other food at home +0.7 (snacks +1.0), meats/poultry/fish/eggs +0.5 (beef +0.9), dairy +0.6, fruits and vegetables +0.6, **cereals and bakery 0.0**, nonalcoholic beverages −0.3. NSA Sep–Oct +0.3 | BLS cpi.nr0.htm + cpi.t02.htm via WebFetch, HTTP 200 (curl 403s this box); index from FRED CUSR0000SAF11 (MIRROR of BLS), pulled ~13:08 ET; BLS API v1/v2 refused: daily request threshold reached |
| P2 | **NOT PUBLISHED.** Table 2 12-month cell is "-". BLS: "BLS cannot publish 12-month percent changes for October 2026 for indexes where October 2025 data are unavailable." Not computed from any substitute month | same |
| P3 | Jun +0.19 · Jul −0.07 · Aug +0.04 · Sep −0.07 · **Oct +0.44** (index-derived). BLS one-decimal SA: Aug 0.0 · Sep −0.1 · Oct 0.4. First month at or above +0.4 **since April**; earlier 2026 months at or above it: Feb +0.44 (318.985/317.589), Apr +0.68 (320.633/318.462). Q3 −0.10% | same |

**Graded 2026-11-10 13:11 ET** (FERT, D:L761 + T3 for D:L579, PROME prome-07 wake, WQ-184).

## Addendum 2026-11-10 — applying the pre-registered consequences

| Item | Applied |
|---|---|
| FL-FERT-05 | **Stays REFUTED** (N5 = 0). The −1.6 yield cut is logged UNATTRIBUTED |
| combo:under-application-yield | November yield added as a member in the theme's direction, flagged UNATTRIBUTED; record soybeans 53.3 added as counterevidence. No score moves |
| Transmission question | P1 ≥ +0.4%: recorded as the **first month at the line**. Nothing fires (G4 declined). See ⚠️ below on the close rule |
| V6 | **1 → 2** per this card's own row ("→ 2 only if P1 ≥ +0.4%"). ⚠️ Composition disagrees with the headline: cereals and bakery, the most grain- and fertilizer-intensive group, was **0.0**; the move came from beef (+0.9, cattle herd), snacks (+1.0), dairy and produce. Applied as pre-registered; the disagreement is recorded, not used to override the card (`finding_headline_keyed_conditional_inherits_its_composition`) |
| FERT-05 | Data point only; final grade after December CPI (mid-Jan 2027) |
| T8 | Re-dated to the Crop Production Annual Summary, **2027-01-12 [EST]** — ESMIS lists no upcoming date as of 11/10 13:10 ET |
| T3 | Re-dated to **2026-12-10** (November CPI, 08:30 ET; BLS December calendar, HTTP 200, and the October release text "scheduled to be published on Thursday, December 10, 2026") |

⚠️ **Close-rule reading, unresolved and not edited (limits: no threshold changed).** Two FERT texts state the transmission close differently. `EXIT_PROTOCOL.md` §C: food at home "stays below the **G4 threshold** through the November-2026 print"; G4 as specced was "≥ +0.4% m/m **×2**". STATUS and EXIT_PROTOCOL line 95: "stays **<+0.4%** through the Nov-2026 print". On the per-month reading, October already broke the close and the question **cannot be declared shut at the November print**. On the two-print reading, it still closes if November prints below +0.4%. A November print at +0.4% or higher keeps it open on both readings. The card's own row ("the rail dies only after the November print") does not decide between them. Routed to PROME for a ruling before 12/10.

⚠️ **Tooling note.** This shell's `grep` is a wrapper that printed nothing for the scratchpad NASS file (exit 1). All counts above are from `command grep` and Python, which agree.


## Addendum 2026-11-10 13:23 ET — close-rule reading RULED

WQ-665 **B**, Will 2026-11-10 13:21 ET, verbatim "665 B" (record `PROME/proposals/2026-11-10_wq665-RULED.md`): the **per-month** reading governs. October +0.4% blocks a close at the November print. FERT recommended the two-print reading; Will chose per-month. `EXIT_PROTOCOL.md` §C aligned; no RESULT cell changed.
