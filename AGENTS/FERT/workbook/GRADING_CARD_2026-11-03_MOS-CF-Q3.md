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
| M1 | **$615/long ton** Q4 contract with US Gulf refiners; Q3 realized **$715/long ton** [8-K 11/03] | Q4 realized in cost of goods sold guided **$800–850/ton**; contract below spot [transcript, MIRROR] | VX-FERT-09 value 615. Not ≥$705, not ≤$605 |
| M2 | "South Fort Meade and Miski Mayo **mines**", additional curtailments, costs rise in Q4 [8-K]. Capacity, start, duration NOT STATED | "idled mining at South Fort Meade and Miski Mayo" to avoid rock inventory build; capacity NOT STATED | SUPPLY_EVENTS MOS-SFM new vintage, asset = mine, PRIMARY |
| M3 | Sales Q3 1.4 Mt, Q2 1.4 Mt; production 1,289 kt vs Q2 1,433 kt. Q4 **sales** guide 1.3–1.6 Mt; Q4 **production** guide NOT STATED | Same guide; Q4 availability sold out; Florida operating rate low- to mid-60% | Production guide absent, so up-leg (a) second limb and down-leg restart limb both unmet |
| M4 | DAP FOB plant **$838/tonne** Q3, **$773** Q2; Q4 guide $820–840/tonne [Mosaic producer benchmark] | Same | KB-FERT-121 |
| M5 | Louisiana idled, Miski Mayo curtailed, Cajati DCP running, Araxá sale process; no restart | Bartow, Louisiana, Brazil curtailed; New Wales and Riverview production improving; no restart date | KB-FERT-121/122; no restart |
| M6 | "Phosphate markets remain tight with improving demand and lingering supply disruptions." | Fall North American demand "much stronger than many of us anticipated" | Context only |
| C1 | "2-4 million metric tons higher than in 2025" [8-K 11/04]. Level implied about 6.9–8.9 Mt | "export authorizations now total almost nine million tons"; last year "just a little under five" (Frost); some may slip into early 2027 (Bohn) [transcript, MIRROR] | **Raised above 6 Mt: V1 → 1** |
| C2 | "resume operations during the first half of 2027" [8-K] | Ramp begins toward the end of H1 2027, AN production in H2 2027 (Bohn) | SUPPLY_EVENTS CF-YAZOO new row |
| C3 | **RETAINED:** "global nitrogen supply-demand balance to remain constructive"; title "Constructive into 2027" | "constructive into 2027"; "positive trajectory in at least the first half of 2027 for nitrogen pricing" (Frost) | KB-FERT-115; T7 consumed |
| C4 | $/product short ton Q3 vs Q2: ammonia $532 vs $677; granular urea $423 vs $593; UAN $322 vs $441. Producer realized, not NOLA, not DTN | UAN Q3 average $322; fill program started $280–290 | KB-FERT-115 |
| V2 / V1 / V8 verdicts | V2 **HELD 3**: sulfur $615 sits between $605 and $705, no production guide, no restart. V1 condition met. V8 level clears 25% but filed text says "reportedly" | V1 **2 → 1**. V8 **HELD 2**, NOT MET AS WRITTEN; see addendum | Convergence 16 → **15** |

## Addenda (dated, append-only)

**2026-11-05, filled 2026-11-05 18:34 ET (D:L578 wake).** Sources: CF 8-K Ex. 99.1 and Mosaic 8-K Ex. 99.1 read at EDGAR; call stages read from Motley Fool transcripts (MIRROR, machine-quality in places); the calls were not heard.

- **C1 pin, form of the figure.** CF stated a delta to 2025, not a level. The level is FERT arithmetic: CF's "just a little under five" plus 2–4 Mt, about 6.9–8.9 Mt. Every point of that range is above 6 Mt, so the condition is met on any reading of the delta. Separately, "almost nine" is authorizations, and CF itself doubts all of it ships in 2026.
- **V8 pin, "from its own data".** The pin was ambiguous. The filed release says "reportedly"; Frost says "our estimates of 35%" on the call. Stage 2 does not overwrite Stage 1, and no CF data or source footnote was read (the slide deck could not be reached), so the condition is recorded NOT MET and V8 holds at 2. It flips only if the deck's source line shows CF's own count.
