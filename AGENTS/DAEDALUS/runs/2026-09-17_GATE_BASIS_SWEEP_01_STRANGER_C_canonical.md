# GATE BASIS SWEEP 01 — STRANGER READ C (CANONICAL DEFINITION SURFACES)

**Date:** 2026-09-17 (Thu) · **Reader:** stranger grader, zero fleet context beyond the brief
**Method:** read ONLY the three named ranges + public data. No GATES.tsv, no STATUS bodies, no other agent files.
**Difference from the earlier read:** that one used a summary/pointer cell; this one grades the **canonical letter**.
**Standing caution:** a canonical surface being *right* is not the same as being *self-sufficient*. Everything below is scored on self-sufficiency to a stranger — could I grade it with no other file open?

---

## GATE 1 — GATE-CORAL-MSI-01 (stand-down condition)
Canonical text: `AGENTS/CORAL/STATUS.md` lines 92–104, quoted block "🔴 MSI SUPPLY-SIDE LEG — REGISTERED STAND-DOWN CONDITION (Will-ruled 2026-08-23, adopted unamended)".

### (1) The condition in my own words
A supply-side price-discovery leg currently sits at 🔴. It stands down to 🟠 when **breadth falls below 5-of-5**: i.e. when **fewer than five of five Florida metros** show a **Parcl MSI above 6.0** — and that sub-threshold state is observed **twice**, where the **second observation is at least 10 days after the first**. One sub-threshold reading does nothing but start a clock. Two readings closer than 10 days count as one observation. Scope is the supply-side leg only; nothing else in CORAL moves either way.

### (2) Questions I had to answer by ASSUMPTION
| # | Question the text does not answer | My assumption |
|---|---|---|
| A1 | **Which five FL metros?** The set is never enumerated in the canonical block. | Assumed CORAL has a fixed, elsewhere-declared list of 5. I cannot name it. |
| A2 | **What is "Parcl MSI"?** The acronym is never expanded; no product, endpoint, or metric definition. | Assumed a Parcl Labs supply metric on a months-of-inventory-like scale where 6.0 is a meaningful level. Could equally be an index. |
| A3 | **Unit of 6.0** — months? index points? ratio? | Assumed "months of supply"; the threshold 6.0 is the classic balanced-market line, which is suggestive, not stated. |
| A4 | **What is a "reading"?** A scheduled snapshot, or whatever the analyst pulls? | The text's own phrase "however many times the pages are pulled" tells me the reading series is **operator-generated**, not a fixed cadence. I assumed a reading = a deliberate pull recorded by CORAL. |
| A5 | **Vintage / as-of** — Parcl data updates continuously; does a reading carry the pull date or the data as-of date? | Assumed pull date. Not stated. |
| A6 | **Must the SECOND reading also be sub-threshold?** Leg 2 only says it must be ≥10 days after the first sub-threshold reading. | Assumed yes (that is what "two consecutive readings" implies) — but the sentence as drafted does not say it. |
| A7 | **Reset rule.** If an intervening (or the second) reading returns to 5-of-5, is the clock reset or does it survive? | Assumed reset. **Nothing in the text says so.** |
| A8 | **Precision / tie on MSI.** Is 6.00 above 6.0? Is 6.04 displayed as 6.0? | Assumed strict `>` on the displayed value; rounding convention unknown. |
| A9 | **"≥10 days"** — calendar days, and inclusive? | Assumed calendar days, inclusive of the boundary (`≥` is explicit). |
| A10 | **What grades it** — the metro count, or a breadth percentage? | Assumed integer count of metros with MSI>6.0, compared to 5. |

### (3) Element-by-element NAMED / UNNAMED
| Element | Status in the canonical text |
|---|---|
| Series / dataset | **UNNAMED** — "Parcl MSI"; no product, endpoint, table, or metric definition |
| Population (which metros) | **UNNAMED** — "5 FL metros", set never enumerated here |
| Unit | **UNNAMED** — 6.0 carries no unit |
| Operator + boundary (metro leg) | **NAMED** — `MSI > 6.0`, strict |
| Operator + boundary (breadth leg) | **NAMED** — `< 5-of-5`, i.e. ≤4 |
| Precision / tie | **UNNAMED** — no rounding or display convention |
| Consecutiveness | **NAMED in words, UNGROUNDED in fact** — "TWO CONSECUTIVE readings" over an undefined reading series |
| Spacing quantifier | **NAMED** — ≥10 days, and explicitly flagged as the load-bearing anti-noise leg |
| Reset | **UNNAMED** — the single largest hole |
| Vintage / as-of convention | **UNNAMED** |
| Direction / scope | **NAMED and unusually well** — supply-side price-discovery leg only, both directions, bank rail untouched |
| Amendment discipline | **NAMED** — future amendments move spacing toward MORE, never less |

### (4) Grade attempt
**Blocked at the instrument.** Parcl Labs is not public data:
- `GET https://api.parcllabs.com/v1/search/markets?query=Miami` → HTTP **403**, body `{"detail":"Not authenticated"}` (fetched 2026-09-17 ~14:0x UTC)
- `https://www.parcllabs.com/markets` → HTTP **404**
- `FORGE/tools/market-data/.env` holds keys for EIA, FRED, PJM, FFIEC, ESTAT, SEC, AGSI, FIRMS — **no PARCL key of any kind.**

Even with a key I could not grade: I do not know **which** five metros, **which** Parcl metric, or **which** two dated readings the 9/13 "CONDITION MET" rests on — the canonical block asserts the condition met on 2026-09-13 but **records neither reading's date nor its value**, so the grade of record is not auditable from its own definition surface.

**VERDICT: CANNOT-GRADE (instrument not publicly reachable — Parcl requires an API key the repo does not hold — AND the metro population, metric definition, and the two firing readings are all absent from the canonical text).**
*Note for the record: the owner reports the condition MET on 2026-09-13 and the leg STOOD DOWN 🔴→🟠. I can neither confirm nor contradict that from this surface. This is a statement about auditability, not a dispute.*

### (5) Misreads two reasonable graders would split on
1. **Does the second reading have to be sub-threshold?** Grader A: obviously yes. Grader B: the letter only constrains its *timing*, so a second reading taken ≥10d later showing 5-of-5 still "counts as the second reading" and the condition fires. B's reading is perverse but textually available — and it inverts the verdict.
2. **Reset vs. survive.** Sub-threshold on day 0, back to 5-of-5 on day 6, sub-threshold again on day 12. Grader A: clock reset on day 6; day 12 is a new first reading; NOT FIRED. Grader B: day 0 and day 12 are two sub-threshold readings ≥10 days apart; FIRED. Both defensible; opposite verdicts.
3. **What a "reading" is.** Because the reading series is operator-generated, a grader who pulls daily and a grader who pulls weekly see different "consecutive" pairs from the *same underlying data*. The anti-noise leg the text calls load-bearing is defined against a series the text never fixes.
4. **`MSI > 6.0` on a metro sitting at exactly 6.0** (or at 6.04 displayed as 6.0). Metro counted or not — which flips the breadth integer, which is the whole gate.

### (6) Smallest edit that removes the largest remaining ambiguity
Add one sentence after leg 2:

> *"A READING is the Parcl `<metric name>` value for each of the five metros — Metro1 · Metro2 · Metro3 · Metro4 · Metro5 — pulled on a fixed weekly cadence (every Monday, data as-of the preceding Sunday) and recorded with its date and five values. Both readings must be sub-threshold; any recorded reading at 5-of-5 RESETS the clock."*

One sentence closes five holes at once: population, metric identity, cadence, vintage, reset — and it converts "consecutive" from a word into a testable fact. If only one clause survives editing, make it **the reset clause**: it is the only gap that flips a verdict without anyone noticing.

---

## GATE 2 — GATE-BRK-R2 (two legs)
Canonical text: `AGENTS/BROCK/workbook/PC_REDEMPTION_REGISTER.tsv` header lines 1–6 (letter) + data rows 7–17 (population).

### (1) The condition in my own words
Two independent escalation legs over a register of private-credit / private-markets redemption vehicles:
- **(a) FIRES** when a **single vehicle** posts **≥3 CONSECUTIVE quarters** in which redemption requests were satisfied at **less than 100%** — where the sub-100% fact must be **issuer-stated** (a filed proration statement), never inferred by the analyst.
- **(b) FIRES** when **any one quarter at any counted vehicle** shows a satisfaction rate **below 25%**, where satisfaction = `SUM(accepted) / SUM(validly submitted)` **across the quarter** — never a mean of monthly rates. Monthly readings are recorded, never graded. Only quarters whose **repurchase pricing date falls on or after 2026-09-03** are in window.
- **SATISFACTION** = accepted / validly submitted, at the same offer, **filing-primary**; an issuer-stated proration percentage qualifies; a cap/requests figure the analyst computes does **not**.

### (2) Questions I had to answer by ASSUMPTION
| # | Question | My assumption |
|---|---|---|
| B1 | **Does an ungradable quarter BREAK a run or merely pause it?** ADS has two sub-100% quarters that "don't count"; CCLFX has quarters that are "not measurable". Does a non-counting quarter reset the consecutive count to 0, or is it skipped? | Assumed **skipped/pause is NOT stated**; I graded conservatively as "an uncounted quarter is not a sub-100% quarter, therefore the run is broken." The text does not say this. This is the single biggest assumption in the gate. |
| B2 | **Is "sub-100%" exact?** Is 99.8% sub-100%? Is a de-minimis odd-lot shortfall sub-100%? | Assumed any issuer-stated proration = sub-100%, whatever the rate. |
| B3 | **Which "quarter"?** Calendar quarter, fiscal quarter, or the vehicle's own tender cycle? CCLFX's fiscal year ends 3/31; BCRED's Q3 letter is filed 9/3 for a quarter priced 9/30. | Assumed the **vehicle's own repurchase-offer cycle**, labelled by the register's `last_period` cell. |
| B4 | **Does (b)'s 2026-09-03 window apply to (a) too?** The prospective-only ruling is written inside the (b) grade-of-record. | Assumed **NO** — (a) counts pre-registration quarters, which is how BCRED/MS-PIF/OCIC each stand "at 2". This is load-bearing and is nowhere stated as a general rule. |
| B5 | **Boundary on (b): is exactly 25.0% a fire?** Letter says "<25%". | Assumed strict `<`; 25.00% does not fire. Named. |
| B6 | **Precision on (b).** BREIT's validating quarter is 24.6% with a published rounding band of 24.0–25.2%, per the header's own fragility flag. Is the graded value the issuer's rounded figure or a re-derived one? | Assumed the **issuer's stated figure as printed**, per "issuer-stated ... qualifies". |
| B7 | **The counted population.** | **NAMED explicitly** — and the exclusion of ASIF is named with its reason and its pending-Will status. No assumption needed. |
| B8 | **Anchor for "when does the quarter's reading exist"** — the pricing date, the letter date, or the 10-Q? | (b) names the **repurchase pricing date** for the window. (a) does not name an anchor; assumed the issuer-stated disclosure date. |
| B9 | **Can (a) and (b) fire on the same quarter?** | Assumed yes, independently. Not stated either way. |

### (3) Element-by-element NAMED / UNNAMED
| Element | (a) | (b) |
|---|---|---|
| Series / dataset | **NAMED** — SEC filings, filing-primary, issuer-stated | **NAMED** — same, plus "issuer-stated proration % qualifies" |
| Unit | **NAMED** — the FACT of sub-100% (rate not required) | **NAMED, and explicitly** — "THE UNIT IS PART OF THE LEVEL: quarterly, SUM(accepted)/SUM(submitted), NEVER a mean of monthly rates" |
| Vintage / window | **UNNAMED** — no in-window rule; inferred from usage | **NAMED** — prospective only, pricing date ≥ 2026-09-03, with the *reason* given |
| Operator + boundary | **NAMED** — `≥3` | **NAMED** — `<25%` |
| Precision / tie | **UNNAMED** — "sub-100%" has no precision rule | **PARTLY** — fragility flag discloses the 24.0–25.2% rounding band on the sole validating observation but sets no grading convention |
| Consecutiveness | **NAMED** — "CONSECUTIVE ... at ONE vehicle" | N/A (single quarter) |
| Reset | **NAMED ONLY BY EXAMPLE** — Monroe "run = 1, NOT 2, because Q1-2026 was satisfied in full". A 100% quarter resets. **A non-measurable quarter is UNNAMED.** | N/A |
| Population / quantifier integers | **NAMED, best in the sweep** — per-vehicle runs enumerated (BCRED 2 · MS-PIF 2 · OCIC 2 · Monroe 1 · ADS 0 · CCLFX 0 · Partners Group never gradable · ASIF excluded) with the ruling behind each | **NAMED** — gradable only where a rate is disclosed: MS-PIF, OCIC, BCRED(est); not Monroe/ADS/CCLFX/PG |
| Independence caveat | **NAMED** — per-vehicle count is unaffected by the shared H1-2026 antecedent, but convergence scoring must count the wave ONCE | — |
| Non-fire semantics | — | **NAMED and unusually good** — "a non-fire of (b) is NOT evidence of health" |

### (4) Grade attempt — with fetched numbers
Checked at primary via the SEC submissions API (`data.sec.gov`, fetched **2026-09-17**), for the three vehicles at a run of 2:

| Vehicle | CIK | Latest filing relevant to a 3rd print | Status as of 2026-09-17 |
|---|---|---|---|
| Blue Owl Credit Income (OCIC) | 1812554 | Q3 **SC TO-I filed 2026-08-26** (acc 0001628280-26-059106). Most recent filings after it: 424B3 + 8-K 2026-09-15. **No SC TO-I/A.** | Q3 results **NOT YET FILED** |
| BCRED | 1803498 | Most recent = the already-graded **SC TO-I/A 2026-09-03** (acc 0001213900-26-096935). Nothing newer. | Q4 letter ~2026-12-03 per the register's own cadence |
| MS North Haven PIF | 1851322 | Q3 **SC TO-I filed 2026-08-13** (acc 0001193125-26-349128); newest filing 8-K 2026-08-25. **No results amendment.** | Q3 results **NOT YET FILED** |

- **(a):** maximum consecutive issuer-stated sub-100% run at any counted vehicle = **2** (three vehicles tied at 2). 2 < 3. → **NOT FIRED.**
- **(b):** zero quarters with a **repurchase pricing date on or after 2026-09-03** have a disclosed satisfaction rate yet. The lowest rate anywhere in the register is OCIC Q1-2026 at **22.82%**, which is below 25% but is explicitly **OUT-OF-WINDOW** (pre-registration, and one of the three observations used to *place* the level). → **NOT FIRED.**

**VERDICT: NOT FIRED (both legs), verified independently at primary 2026-09-17.** The owner's own run state (0 fired, three vehicles at 2) reproduces exactly from the filing record. **This is the only one of the three gates I could grade end-to-end from its canonical surface plus public data.**

### (5) Misreads two reasonable graders would split on
1. **The ungradable-quarter gap (B1) — the real one.** Suppose ADS files a Q3-2026 10-Q with an issuer-stated proration. Grader A: ADS's counted run is 0 (the 2026 quarters were inference-only), so this is run=1. Grader B: the two 2026 quarters *happened* and were merely undisclosed; the issuer-stated Q3 makes ADS a vehicle whose run is arguably 3. The letter's "issuer-stated only" rule supports A — but the letter never says what an unmeasurable quarter *does to a run in progress*, and the Monroe example only covers an explicit 100% quarter. A and B differ by a **fired gate**.
2. **Whether (b)'s 2026-09-03 window binds (a).** A grader reading only the "0 FIRED as of 2026-09-03 / GRADES PROSPECTIVELY ONLY" line could apply it to both legs, which would reset every vehicle to run=0 and push the earliest possible (a) fire out by ~three quarters. The text places that ruling inside the (b) discussion but never scopes it.
3. **BCRED's ~50% estimates counting toward (a).** BCRED Q2 and Q3 are marked `~50 (est)` on a transfer-agent estimate as of 9/2/26, not a final figure. (a) needs only the FACT of sub-100%, which is issuer-stated — so they count. But a grader applying the register's own anti-inference principle (the one used to zero ADS) could argue an estimate-based cell is the same class of thing. That would drop BCRED from 2 to 0.
4. **BCRED's "75% of requested capital."** The letter states 75%; the register correctly demonstrates that this is a cumulative two-quarter construction and Q3 satisfaction is ~50%. A stranger reading the filing alone and not this register would grade 75%. Both are "issuer-stated"; only one is right. **(b) would not fire on either, but the class of error is live.**
5. **ASIF.** Excluded pending Will's ruling. A grader who found ASIF at primary and did not read the header's authorization-staleness note would count it, adding a sixth firing path.

### (6) Smallest edit that removes the largest remaining ambiguity
Append one clause to the **(a)** line:

> *"A quarter that is NOT MEASURABLE or NOT ISSUER-STATED is a GAP, not a satisfied quarter: it neither counts toward a run nor resets one — the run is suspended and resumes at its prior count on the next issuer-stated sub-100% quarter. Only an issuer-stated 100%-satisfied quarter resets a run to 0."*

(Or the opposite disposition — the direction matters less than *stating* one.) This is the only gap in Gate 2 that can silently flip the verdict, and it will be exercised the moment ADS or CCLFX files a proration.

---

## GATE 3 — GATE-BRENT-COT-35B (COT-FUEL-35B successor band)
Canonical text: `AGENTS/BRENT/setups/2026-08-12_35b-COT-successor-band-N1-build.md` lines 1–12 and 50–60, plus the `AGENTS/BRENT/scripts/cot_grade.py` docstring lines 1–40.

### (1) The condition in my own words
A weekly two-leg test on CFTC disaggregated **futures-only** positioning in `WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE`, asking whether managed-money short "fuel" is SPENT:
- **Leg A (raw):** MM gross shorts **≤ 109,164** ⇒ SPENT. **109,165 – 118,325 ⇒ NO-VERDICT deadband.** **≥ 118,326** ⇒ NOT-SPENT. (The nominal bar is 113,745 = trailing-8wk-median base 122,904.5 minus one frozen median unit of 9,160; the deadband is ±0.5 median unit = ±4,580 around that bar.)
- **Leg B (share):** `MM gross shorts / Open Interest × 100` **≤ 4.909%** ⇒ SPENT, else NOT-SPENT. **Leg B is gating.**
- **Verdict:** both legs must AGREE. Disagreement ⇒ **NO-VERDICT**, which is a real answer that defaults sizing to the base case (accepted NO-VERDICT rate 33.6%, on the record).
- Every parameter is **FROZEN**. Re-basing is a new build plus a fresh Will ruling, never maintenance.
- Grade off the **RAW** CFTC file; **Socrata is explicitly forbidden** (it lagged all 40 polls on 7/17).

### (2) Questions I had to answer by ASSUMPTION
| # | Question | My assumption |
|---|---|---|
| C1 | **Which Open Interest field?** The disaggregated file carries OI_All, OI_Old and OI_Other. The spec says only "Open Interest". | Assumed **OI_All** (1,939,911 on the 9/8 print). OI_Old is 1,853,037 — using it gives a share of 5.787%, same side of the bar here, but the two are not interchangeable in general. |
| C2 | **Which print is "current"?** Report date, or release date? | Assumed the latest **report date** in the raw file = **2026-09-08** (released Fri 2026-09-11; the file's `last-modified` header confirms 2026-09-11 19:27 UTC). Today is Thursday 9/17; the next print lands Friday 9/18. |
| C3 | **Is the test still LIVE?** Line 6 banners this build as HISTORICAL and redirects to the `COT-FUEL-35B` row in `workbook/REGISTRY.tsv`, which I was instructed not to open. | Assumed the frozen letter reproduced in the `cot_grade.py` docstring is current. **I cannot verify this from the ranges given** — and the docstring's own cautionary history is precisely about a tool grading a retired test confidently. |
| C4 | **"Gating" vs "must agree."** The docstring says both. | Assumed the AGREE rule governs; "Leg B is gating" I read as emphasis that Leg B can veto a Leg-A SPENT. Same outcome on this print. |
| C5 | **Rounding on the OI-share.** 4.909% is 4 s.f.; is the computed share rounded before comparison? | Assumed compare unrounded. Not material here (5.5275% vs 4.909%). |
| C6 | **RAW file URL.** "Grade off the RAW file" names no endpoint in lines 1–40. | Assumed `https://www.cftc.gov/dea/newcot/f_disagg.txt`. |
| C7 | **Deadband boundary rounding.** 113,744.5 ± 4,580 = 109,164.5 … 118,324.5, but the spec writes 109,164 / 109,165–118,325 / 118,326. | Assumed the spec's stated integers govern (they floor both ends). Note the top end is asymmetric: 118,325 is inside the deadband though it exceeds 118,324.5. |
| C8 | **Does a missed week do anything?** | Assumed the test is stateless per print — no run, no reset. |

### (3) Element-by-element NAMED / UNNAMED
| Element | Status |
|---|---|
| Series / dataset | **NAMED, best in the sweep** — CFTC disaggregated **futures-only**, market string given verbatim, Socrata explicitly **forbidden** with the reason |
| Endpoint of the permitted RAW source | **UNNAMED** in these ranges — "the RAW file", no URL |
| OI field (All / Old / Other) | **UNNAMED** — the one substantive gap in Leg B |
| Unit | **NAMED** — contracts (Leg A), percent of OI (Leg B) |
| Vintage | **PARTLY** — parameters are FROZEN with explicit basis windows (median unit n=235, 2022-02-08…2026-08-04; base 2026-06-16…2026-08-04); the **as-of convention for "current shorts" is UNNAMED** |
| Operator + boundary | **NAMED to the contract** — ≤109,164 / 109,165–118,325 / ≥118,326 / ≤4.909% |
| Precision / tie | **NAMED by construction** — integer contract boundaries leave no tie on Leg A; Leg B tie at exactly 4.909% resolves SPENT via `≤` |
| Consecutiveness | **N/A and correctly so** — single-print test |
| Reset | **N/A**, and re-basing is explicitly forbidden without a fresh ruling — a *stronger* statement than a reset rule |
| Population / quantifier | **NAMED** — one market, one trader category (managed money), gross shorts |
| Verdict algebra | **NAMED** — both legs agree; disagreement ⇒ NO-VERDICT; NO-VERDICT is a real answer with a pre-registered 33.6% base rate |
| Liveness of the test itself | **AMBIGUOUS** — the build doc banners itself historical and points at a file outside my permitted range |

### (4) Grade attempt — with fetched numbers
**Source (the permitted one):** `https://www.cftc.gov/dea/newcot/f_disagg.txt`, fetched 2026-09-17 ~14:03 UTC; 447,622 bytes; `last-modified: Fri, 11 Sep 2026 19:27:46 GMT`. Row, verbatim head:

```
"WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE",260908,2026-09-08,067651,NYME,01,067 ,
  1939911, 655691, 346775, 110812, 585913, 122583, 218960, 107229, ...
```

| Quantity | Value | Source |
|---|---:|---|
| Report date | **2026-09-08** | RAW `f_disagg.txt`, fetched 2026-09-17 |
| Open Interest (All) | **1,939,911** | same |
| MM gross **shorts** | **107,229** | same |
| MM gross longs | 218,960 | same (context only) |

*(Cross-check only, not the grading source: Socrata `72hh-3qpy` returns identical 9/8 figures — 1,939,911 / 107,229 / 218,960 — and shows the prior two prints at 111,019 (9/1) and 112,862 (8/25). The spec forbids grading off Socrata; it is used here solely to confirm the raw parse, and the agreement means the 7/17 lag defect is not present on this print.)*

**Leg A:** 107,229 ≤ 109,164 → **SPENT.** (It clears the deadband floor by 1,935 contracts, i.e. by 0.21 median units — a genuine clearance, not a boundary case.)
**Leg B:** 107,229 / 1,939,911 × 100 = **5.5275%**. 5.5275% > 4.909% → **NOT-SPENT.** (Misses by 0.619pp, ~12.6% above the bar — also not a boundary case.)
**Legs DISAGREE.**

**VERDICT: NO-VERDICT** on the 2026-09-08 print — which under this spec is a real answer, defaulting sizing to the base case.

⚠️ **Certified against the letter as reproduced in `cot_grade.py`'s docstring, NOT against `REGISTRY.tsv`.** The build doc's own banner (line 6) says the LIVE frozen letter lives in the registry row, and warns that this document "predates the frozen-window and September base/deadband wording corrections." If those corrections moved either bar, this verdict is wrong in exactly the way the docstring's own ⛔ history describes. **I did not run the script** (per instruction) and did not open the registry (per instruction).

*Mechanism worth naming: this print is the textbook illustration of why Leg B exists. Raw shorts fell to a level that reads as capitulation, but open interest rose to 1.94M — so the short position shrank in contracts while remaining **large as a share of the book**. Leg A reads the numerator; Leg B reads the ratio; they disagree; the spec refuses to resolve it. That is the leg-suppression defect (⑤) the successor build was written to kill, firing correctly on live data.*

### (5) Misreads two reasonable graders would split on
1. **Which OI.** OI_All → 5.5275%. OI_Old → 107,229/1,853,037 = 5.787%. Both exceed 4.909%, so the verdict holds today — but the bar itself (4.909%, a trailing-104wk median of the share) was computed against *one* of these denominators, and the text never says which. On a print near the bar, two careful graders split.
2. **"Leg B is gating" vs "both legs must AGREE."** On the *same print*, "gating" reads as *Leg B decides* ⇒ **NOT-SPENT**; the agree rule reads ⇒ **NO-VERDICT**. Those are different sizing instructions. Today they happen to point the same direction (not SPENT), which is exactly the condition under which the contradiction goes unnoticed.
3. **Reading the build doc's line-50 table alone.** It gives Leg A as "shorts ≤ base − 1.0 median unit (−9,160), with a ±0.5 median-unit deadband". A grader computing from the table gets bar = 122,904.5 − 9,160 = **113,744.5**, and may read SPENT as ≤113,744 with the deadband *around* that (109,165–118,325) — i.e. the same numbers but SPENT and deadband **overlapping**. It also gives Leg B as "≤ its own trailing-104wk median" with **no number at all** — 4.909% appears ONLY in the script docstring. A grader with only the build doc cannot compute Leg B.
4. **Which print.** Today is Thursday; the newest print is 9/8 (released 9/11) and a new one lands 9/18. A grader who graded on 9/1 (shorts 111,019) would get Leg A = **NO-VERDICT** (inside the deadband) and Leg B = NOT-SPENT — a different Leg-A state from the same week's-old data. The spec never says which print is "current" or when a verdict expires.
5. **Is the test even live?** One grader reads line 6's banner and refuses to grade; another grades off the docstring, as I did.

### (6) Smallest edit that removes the largest remaining ambiguity
Add one line to the frozen spec block in `cot_grade.py`'s docstring (and mirror it into the registry row):

> *"Leg B denominator = the `Open_Interest_All` field of the RAW disaggregated futures-only file at `https://www.cftc.gov/dea/newcot/f_disagg.txt`; the 4.909% bar was measured on that same field. On disagreement the VERDICT rule governs — 'Leg B is gating' means Leg B can veto a Leg-A SPENT, it does NOT override the NO-VERDICT rule."*

Two clauses, one line: it names the denominator (killing misread 1) and reconciles "gating" with "must agree" (killing misread 2), which are the only two ambiguities here capable of changing a live sizing instruction. Gate 3's remaining gaps are documentation gaps; these two are grading gaps.

---

## CROSS-GATE SUMMARY

| | GATE-CORAL-MSI-01 | GATE-BRK-R2 | GATE-BRENT-COT-35B |
|---|---|---|---|
| **Verdict** | **CANNOT-GRADE** (instrument paywalled + population/metric/readings absent) | **NOT FIRED** (a): max run 2 of 3 · (b): no in-window quarter | **NO-VERDICT** on the 2026-09-08 print (legs disagree) |
| Graded end-to-end from canonical text + public data? | **No** | **Yes** | **Yes, but against the docstring, not the registry** |
| Series / dataset | UNNAMED | NAMED | NAMED (endpoint unnamed) |
| Unit | UNNAMED | NAMED (emphatically) | NAMED |
| Vintage / window | UNNAMED | (b) NAMED · (a) UNNAMED | Params FROZEN · as-of UNNAMED |
| Operator + boundary | NAMED | NAMED | NAMED to the unit |
| Precision / tie | UNNAMED | UNNAMED (a) · partial (b) | NAMED |
| Consecutiveness | NAMED but ungrounded | NAMED | N/A |
| **Reset** | **UNNAMED** | NAMED by example only; **gap case UNNAMED** | N/A (re-base forbidden) |
| Population integers | **UNNAMED** (which 5 metros) | **NAMED, per-vehicle, with rulings** | NAMED |

**One observation a stranger can offer.** The three gates are not at three different quality levels by accident. Gate 2 is gradable by a stranger because its definition surface **carries its own population, its own exclusions, and the reasoning behind each ruling** — and because it names what a non-fire does *not* prove. Gate 3 is gradable because a **tool** was forced to implement it, and implementation refuses to accept an unnamed number. Gate 1 has never been forced through either discipline: it was ratified as prose, and prose can hold a threshold without holding a denominator, a population, or a reset. **The letter is excellent at the thing it was arguing about (spacing, anti-noise, symmetry) and silent on everything it was not arguing about.** That is not a CORAL failing; it is what happens when a gate is ratified in a conversation rather than against a schema — the ratification captures the contested clause perfectly and the uncontested ones not at all.

**The generalizable design fact:** across all three, the elements that are NAMED are the ones somebody *argued about or had to execute*; the elements that are UNNAMED are the ones everybody agreed on implicitly. Reset rules and denominators are almost never argued about at ratification — which is exactly why they are the two things missing here, and the two things that flip verdicts silently.

