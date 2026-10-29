# GRADING CARD — Mosaic Q3 + CF Industries Q3 2026 (pre-registered)

**Frozen:** 2026-10-28 23:00 ET, at commit (Will-approved set, item 1). **Model:** market-agent blueprint §5 print-grading contract (frozen card · disambiguation pins · two-stage grade); LABOR `docket/GRADING_CARD_*` is the peer form.
**Freeze rule:** everything above § RESULTS is a no-edit honesty record. After the prints, only the RESULT cells are filled. A pin that turns out ambiguous gets a **dated addendum below § RESULTS**; it is never edited in place.
**What this card cannot do:** fire or grade a gate. **G5** grades only on the DTN weekly retail print (T4). **G3** fires only on a Chinese government action (quota revised down / floor reimposed above prevailing FOB); a company's estimate of Chinese exports is not that. **No prediction** is created here (item 3 is held for Will).

## Schedule (verify at consumption)

| Company | Stage 1 — results | Stage 2 — call | Date source |
|---|---|---|---|
| Mosaic (MOS) | Tue 2026-11-03, after close | Wed 2026-11-04 11:00 ET | DTN relay, `KB-FERT-103` (MIRROR) |
| CF Industries (CF) | Wed 2026-11-04, after close | Thu 2026-11-05 11:00 ET | CF schedule release via search summary, T7 (MIRROR) |

**Sources, in order:** issuer release on EDGAR (8-K Ex. 99.1; sec.gov browser-reachable 10/26) → 10-Q if filed → issuer IR (Mosaic IR returned 403 to this box) → call transcript (MIRROR, labelled). Stage 1 reads the release only; Stage 2 adds the call. A Stage-2 statement never overwrites a Stage-1 number; both are recorded.

## Mosaic — questions, pins, consequences

| # | Question | Measurement pin (how it is read) | Records to |
|---|---|---|---|
| M1 | **Q4 2026 sulfur cost** | A number Mosaic states for its Q4 (or Oct–Dec) sulfur contract/delivered cost. Record the value **with Mosaic's unit** ($/long ton, $/tonne). Words without a number ("expected to decline") = **DIRECTION-ONLY**, not a level. Q3 realized raw-material cost ≠ Q4 contract; record separately. Not stated anywhere = `NOT STATED` | VX-FERT-09 Current_Value; KB |
| M2 | **South Fort Meade** | Mosaic's own words: asset type (mine / chemical plant / both), affected capacity with unit, idle start, expected duration. Not mentioned = `NOT STATED` | SUPPLY_EVENTS `MOS-SFM` (upgrade to PRIMARY if issuer-stated) |
| M3 | **Phosphate volumes** | Q4 2026 phosphate production or sales guidance, tonnes, as stated; Q3 actual vs Q2 actual | KB; FL-FERT-06 |
| M4 | **Realized DAP price** | Mosaic's stated average DAP $/tonne (FOB plant or as labelled), Q3 vs Q2. A **Mosaic producer benchmark**, never written as or compared with DTN retail $/ton without saying so | KB |
| M5 | **Other idles / restarts** | Any named facility (Faustina, Bartow, Riverview, New Wales, Brazil sites) with state and date | SUPPLY_EVENTS |
| M6 | Demand / affordability language | Verbatim phrase only; context, no grade | KB notes |

## CF Industries — questions, pins, consequences

| # | Question | Measurement pin | Records to |
|---|---|---|---|
| C1 | **Chinese urea exports, 2026** | CF's stated estimate in Mt with its period, vs its prior **4–6 Mt**. Record verbatim. ⛔ Not a G3 input | VX-FERT-01 notes; KB |
| C2 | **Yazoo City restart** | Latest stated window vs the 8/05 baseline "first half 2027" | SUPPLY_EVENTS `CF-YAZOO` (new dated row) |
| C3 | **Nitrogen outlook** | Whether "constrained supply / constructive demand through 2026 into 2027" is **retained, softened or dropped** — quote the sentence | KB; T7 |
| C4 | **Realized prices** | Product-specific realized $/short ton (ammonia, granular urea, UAN) Q3 vs Q2. Producer realized ≠ NOLA barge ≠ DTN retail | KB |
| C5 | Full operating read | Per `companies/CF/Q3_PREP.md` (earnings quality, gas, cash, Blue Point). Not graded on this card | companies/CF |

## Pre-registered consequences (decided now, applied after)

| Vector | Moves UP if | Moves DOWN if | Otherwise |
|---|---|---|---|
| **V2 phosphate tight leg** (score 3) | → **4** only if BOTH: (a) M1 Q4 sulfur ≥ $705/long ton **or** M3 guides Q4 phosphate production below Q3 actual; **and** (b) the 11/04 DTN print has MAP ≥ $983 | → **2** only if BOTH: (a) M1 Q4 sulfur ≤ $605/long ton (a cut of $100 or more); **and** (b) M2/M5 report a restart or M3 guides Q4 production above Q3 actual | **HELD at 3**. DIRECTION-ONLY or NOT STATED on M1 counts as neither (a) |
| **V1 China export regime** (score 2) | → **3** if C1 is cut below 4 Mt **and** CF attributes it to Chinese policy (stated, not inferred) | → **1** if C1 is raised above 6 Mt | **HELD at 2** |
| **V8 European production** (score 2) | → **3** if CF (or Mosaic) states European nitrogen curtailment at or above Yara's 10/22 reading (≥25% of European ammonia) from its own data | — | **HELD at 2** |
| VX-FERT-09 sulfur | Value only (no bands); the M1 number or `DIRECTION-ONLY` / `NOT STATED` | | |

A score move needs the condition **as written**. A condition that is close but not met is recorded as "not met" with its numbers, and the score holds.

## RESULTS (fill after each stage; RESULT cells only)

| # | Stage 1 (release) | Stage 2 (call) | Consequence applied |
|---|---|---|---|
| M1 | | | |
| M2 | | | |
| M3 | | | |
| M4 | | | |
| M5 | | | |
| M6 | | | |
| C1 | | | |
| C2 | | | |
| C3 | | | |
| C4 | | | |
| V2 / V1 / V8 verdicts | | | |

## Addenda (dated, append-only)

*(none)*
