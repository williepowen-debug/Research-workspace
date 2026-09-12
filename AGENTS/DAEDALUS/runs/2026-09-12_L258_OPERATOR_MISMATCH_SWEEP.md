# DOCKET L258 — ONE-TIME SWEEP: registered base rates vs the operator their letter carries

**DAEDALUS · 2026-09-12 (Sat) · SL-5(c) · item 4 of the wiring sweep's own §4 list**
⛔ **A DATED SPEC/REGISTRY-HYGIENE MEASUREMENT, NEVER A RETROACTIVE RE-GRADE.** Nothing below says a
prediction was wrong. It asks one question: **does a registered base rate agree with the operator its own
letter carries?** SL-5(c): *a base rate on the other operator is a different letter's base rate.*
⛔ **SL-5 IS FORWARD-ONLY** (Will 9/3). A letter registered before 2026-09-03 that lacks a tie convention is
**un-covered legacy, NOT a violation.** Every count below is split at that line. Getting this wrong turns a
hygiene measurement into a false accusation.

## COUNTS
| | n |
|---|---|
| Registered rows scanned on machine-readable threshold surfaces | **65** (RED 12 · CREED 11 · REGINALD 8 · HANS 14 · GATES 20) |
| Numeric operator legs on those rows | **107** |
| Over a fixed-precision published series (the exposed population) | **≈95 of 107** (INFERRED — precision is declared on only a handful of rows, *which is itself the finding*) |
| Candidate pairs (a base rate beside an operator-carrying threshold) | **≈54 distinct** |
| 🔴 **MISMATCH** | **9** — and **8 of 9 are pre-SL-5 legacy or already corrected; ONE is live and new** |
| 🟠 **UNSTATED-CANNOT-EVALUATE** | **≈20** — the bigger population |
| ✅ MATCH | **≈30** |
| UNKNOWN (each with a named unchecked artifact) | 5 |

**Compliance, split at the forward-only line:**
| | registrations | declare a tie convention | rate |
|---|---:|---:|---:|
| **Before 2026-09-03** — un-covered legacy, **not a violation** | 106 of 107 legs | 6 rows | **9.2%** |
| **On/after 2026-09-03** | 6 | 4 | **67%** |

⭐ **SL-5 FORWARD-ONLY IS WORKING, and that is the headline.** 9.2% → 67% in nine days. **Zero** new threshold
rows entered RED/CREED/REGINALD/HANS since 9/3 (verified by diffing row counts against each file's last pre-9/3
commit); `GATES.tsv` gained exactly one. LABOR (LAB-18/19, 9/4) and FERT (FERT-11/12, 9/5) registered fully
conforming letters — FERT-11 is MECE (`>170.0 MISS-HIGH · =170.0 HIT · <170.0 MISS-LOW`), LAB-19 ships a
**fixture** at `scripts/tests/test_epop_thresholds.py:78`. BOND re-declared its pre-existing `I′` letter
post-SL-5 and **cites RED FT-11 by name**.

## 🔴 M1 — THE ONE NEW, LIVE, UNCORRECTED MISMATCH: RED-FT-07, and the mechanism is FLOAT
**Claim:** FT-07's letter carries `CCC-OAS **> 930 bp**`, strict. The instrument computes
`float(published) * 100`, and `float("9.30") * 100 == 930.0000000000001`. **So a print of exactly 9.30% FIRES a
band the letter says must not fire** — the instrument's effective operator is `≥`, which is not the letter's.
**Artifact:** `AGENTS/RED/scripts/base_rate_review.py:66-78, 109-115, 222-224`; same scaling at
`AGENTS/RED/scripts/boot.py:77, 218-234`. Letter: `FALSIFICATION_TRIGGERS.tsv` row `RED-FT-07`.
**Verification:** `python3 -c "print(repr(float('9.30')*100), float('9.30')*100 > 930)"` → `930.0000000000001 True`.
**Observed:** a sweep of all 20 mapped RED legs at their tie values flips **exactly one** — FT-07 fire. FT-01,
FT-02, FT-05, FT-06, FT-09, FT-10, FT-12 and **every exit leg** evaluate correctly. FT-11's precondition is off
the integer-bp grid, so its tie set is empty — **benign by luck, not by design**, since the delta is still
differenced in raw float.
**Second-order, and it is the sharper half:** the letter leaves the value `930` **UNALLOCATED** — fire is `>930`,
exit is `<930` — so a 9.30% print is *neither* a fire nor an exit under the letter, **and the instrument silently
resolves it to FIRE.** `finding_float_precision_empties_the_tie_set_and_voids_the_operator`.
**Magnitude: UNKNOWN.** Whether `930` has ever printed in `BAMLH0A3HYC` needs a full-history FRED pull, not made.
**Method note — this used the test RED itself ratified.** RED **withdrew** the "recompute under both operators"
test on 9/6 (`AGENTS/RED/OUTBOX.md:75` — *"DO NOT ROUTE IT"*) and named the valid one: *a positive fixture, an
observation exactly on the boundary at the declared precision.* **That is the fixture used.** The withdrawn
test was not routed. ⭐ **RED's own ML-RED-221 already named FT-01/02/07/09/12 as exposed and deliberately
touched none of them; this measurement narrows that list from five to one.**

## 🔴 CORRECTION TO MY OWN CANON — found by this sweep, fixed today
`SPEC_LETTER_STANDARD.md:29` read *"the registered `≤ −4bp` base rate (5.0% / 3.8%, **LR≈34**) was computed on
the STRICT cut."* **The RATES reproduce on the strict cut. The LR reproduces on NEITHER** — RED measures
**LR≈28 strict / LR≈21 non-strict** and states *"Neither reproduces the registered LR ≈ 34"*
(`AGENTS/RED/research/2026-09-02_FT11_v1.1_second_path_partition_AND_tie_set.md:75`, **verified at the artifact,
not from the report**). I bundled a correct pair of rates and an unreproducible LR into one parenthesis and
attributed the whole to one operator — in the canon file whose own rule is that a base rate belongs to exactly
one operator. `finding_exact_level_authenticates_a_wrong_direction`: **verify an exact figure and the claim
beside it as TWO claims.** **FIXED in SL-5 today.** The same imprecision propagated into RED's FT-11 registry
cell — RED's row, RED's to fix, packeted.

## THE OTHER EIGHT MISMATCHES — all pre-SL-5 legacy or already corrected
| # | desk | the disagreement | live? |
|---|---|---|---|
| **M3** | **FERT** | GATE-FERT-G5's letter is `DTN retail DAP/MAP **> $1,000/ton**`; its base rate is *"only 7.1% of months **≥$780/mt**"* — a **different series, unit, level AND operator** (Pink Sheet $/mt). The gate cell itself warns *"NEVER conflate w/ Pink Sheet $/mt."* **Largest magnitude of the eight.** | 🔴 **LIVE**, 9/16 graded read |
| **M4** | WATT | P1 RED band `RT LMP > $1,000`; base rate on `≥$1,000` (5 of 4,149). Band's own registration date UNKNOWN. | legacy |
| **M5** | REGINALD/TERRY | REG-T-02 letter `WAL close **< $78**`; base rate on a `≤ −1.45%` *return* cut. Figure already marked "do not re-cite" for a **different** reason — so this is an undisclosed wrinkle on an already-caveated number. | low |
| **M6** | TERRY | `P(WAL < $70)` vs a `≤ −9.4%` move base rate. TERRY already labels it *"a shape read, not a probability."* | note only |
| **M7** | MIDAS | MIDAS-06 branch (c) `DFII10 **< 2.20**`; distance stat on `≤ −14bp`, which lands at **exactly 2.20** ⇒ branch **(d)**, not (c). Level partition is MECE and correct; only the statistic's cut is mis-allocated. n=1 ⇒ over-count is 0 or 1. | note |
| **M8** | VIOLET | Canonical table `≥+30% / ≥+50%`; source computes `>`. Continuous ratio ⇒ tie almost certainly empty ⇒ **nil magnitude.** | nil |
| **M2 · M9** | RED | v1.0 float partition · the S39b registration — **both already CORRECTED** (9/6, 9/2). | closed |

## 🟠 THE BIGGER FINDING: ≈20 UNSTATED, AND A SCAN KEYED ON BASE RATES READS EXPOSURE AS CLEANLINESS
**HANS carries 24 operator legs and ZERO base rates. REGINALD carries 16 legs and zero in-registry.** They are
**maximally exposed and structurally invisible to a base-rate-keyed scan** — "no base rate registered" reads as
clean and is the opposite. `finding_scan_keyed_on_naming_reads_local_form_as_absence`.
**The MISMATCH count is a count of DETECTABLE defects** — ones where the base rate's operator was written down at
all. ~20 UNSTATED rows could be mismatches and cannot be tested. Notable: RED's `published NN.N%` figures
(hand-computed pre-tool; RED's own words, *"a base rate whose construction lives in a transcript is not
registered — it is remembered"*) · AEOLUS C5, where **the tie set IS the most important value in the series**
(25 cm and 153 cm are the WSV all-time record lows, each a realised integer print) · VIOLET, where a threshold's
evidence is the adjective *"uncommon"* with no n.

## ⚠️ SL-5(d) IS THE LEAST-OBSERVED CLAUSE — measured
**Every one of the 9 mismatches is on a FIRE leg. Exit legs are base-rated at all on exactly TWO rows
fleet-wide** (RED FT-06, RED FT-10). 🔴 **CORRECTED — see ADDENDUM 2: it is ~1.5.
FT-10's exit carries NO base rate; it passed my count because I counted PRESENCE, not independent
establishment.** **HANS registers no exit legs whatsoever across 14 rows.** SL-5(d) exists
because RED's realised tie set sat on FT-10's EXIT leg — and nine days on, almost nobody base-rates an exit.

## 🔴 A DISTRIBUTION GAP THAT EXPLAINS THE COMPLIANCE PATTERN — and it is mine to raise
**`FORGE/PREDICTION_DISCIPLINE.md` does not carry SL-5's tie-set clause.** Verified by reading every line
matching `base.rate|operator|strict|tie|precision`. That file is the one *"cited from every prediction ledger /
registration template"*; **WQ-172's negative-existence clause and WQ-175's frozen-on-revisable clause were both
transplanted into it — the tie-set row was not.** So the rule lives only in a DAEDALUS blueprint, and the
compliant post-9/3 registrations came from the desks that read `SPEC_LETTER_STANDARD.md` directly.
`finding_ask_which_surface_the_reader_travels_not_where_the_fact_belongs`. **PROME's file → proposed, not edited.**

## PRIOR ART, AND AN INSTRUMENT THAT ALREADY EXISTS
My own `profiles/RED_REFRESH_2026-09-03_READER_REPORT.md:105-124` tallied RED at 3 of 12 rows declaring
strictness, 1 of 12 naming precision — **independently reproduced exactly** by this sweep.
⭐ **`sweeps/GATE_BASIS_SWEEP.md` step 4 IS this check**, scoped to `PROME/GATES.tsv`, with an
`OPERATOR-MISMATCH` verdict token **already registered** — **run #1 due 2026-09-16, Run Log shows zero runs.**
L258 covers the desk registries that playbook's perimeter does not reach; **M3 sits inside its perimeter and is
the first `OPERATOR-MISMATCH` it would have found.** Per WQ-229 — prefer promoting an existing control —
**L258's recurring form should be step 4 of that playbook widened to the desk registries, not a new sweep.**

## DISPOSITIONS
| item | disposition |
|---|---|
| SL-5's own LR≈34 | **FIXED TODAY** in `BLUEPRINTS/SPEC_LETTER_STANDARD.md`. |
| **M1 RED-FT-07** | **PACKET TO RED** (live — doorbelled). Compare in published integer units in both `base_rate_review.py` and `boot.py`; declare FT-07's tie convention; **allocate the `930` atom**, which the letter leaves unowned. RED's row, RED's threshold decision. |
| M3 FERT | **PROME to route**, and it is inside GATE_BASIS run #1 (9/16) — flagged in the delivery memo rather than a second packet to a dark desk. |
| M4–M8 | Legacy/low/nil. Named in the record; **no packets** — SL-5 is forward-only and these are un-covered, small or self-disclosed. Sending five packets over nil-magnitude legacy is the paperwork reflex. |
| `FORGE/PREDICTION_DISCIPLINE.md` gap | **PROPOSED to PROME** — transplant the tie-set registration line, as WQ-172 and WQ-175 already were. |
| The recurring form | **Widen `GATE_BASIS_SWEEP.md` step 4 to the desk registries at run #1 (9/16)** — promote the existing control. |

**COVERAGE LIMITS — do NOT read a clean line as coverage:** inbox/outbox and archive dirs were not swept
(except FERT and one named packet), so a frozen letter living only in a delivered packet is invisible here. The
scan keyed on `< > ≤ ≥ <= >= above below strictly non-strict`; **a letter expressing its cut as prose ("clears
the band") reads as absence** — VIOLET's confirm legs are exactly that shape and were not evaluable. A tie set
marked "non-empty" means the value is REPRESENTABLE at the published precision, **not that it has ever printed**
— including M1's own magnitude. No network pulls were made.

---

## ADDENDUM 2026-09-12 ~15:0x ET — M1's MAGNITUDE IS NO LONGER UNKNOWN. THE TIE SET IS **REALISED**.

**I recorded above: *"Magnitude: UNKNOWN. Whether `930` has ever printed in `BAMLH0A3HYC` needs a
full-history FRED pull, not made."* That was honest, and it was ONE QUERY AWAY.** RED pulled the series;
**I then re-verified from an INDEPENDENT artifact rather than adopting the report** —
`FORGE/tools/market-data/.cache/fred_BAMLH0A3HYC_20000.json`, a different cache from RED's pull.

| claim | RED | DAEDALUS, independent | verdict |
|---|---|---|---|
| prints at exactly `9.30` | 5 | **5** | **EXACT MATCH** |
| dates | 2024-02-14 · 2024-07-16 · 2024-07-18 · 2025-06-04 · 2025-06-10 | **all five identical** | **EXACT MATCH** |
| denominator | 787 obs | **787 obs**, 2023-09-11 → 2026-09-09 | match |
| rate | 0.64% | **0.64%** | match |

**So the tie atom is not a curiosity — it is five live instances**, and every observation in the window
publishes at exactly 2dp, so the tie value sits squarely on the publication grid.
**Downstream, per RED:** full-history base rate 36.47% → 35.83% (exactly the 5 ties). **Rolling-120
UNCHANGED at 84.17%** — no tie in the last 120 obs — so RED's registered `84.2%` cell **was never wrong**
and RED correctly did not restate it. *A defect in the instrument did not imply a defect in every figure the
instrument produced* — `finding_claim_outlives_its_discredited_instrument`, applied in the right direction.

**⚠️ THE AGGRAVATING FACTOR I DID NOT MEASURE AND RED DID: `sustain_window = 1`.** FT-07 is the worst row
on the board for a tie, because **the FIRST tie print fires.** Every other mapped leg has a window that
would have to swallow the tie repeatedly. **0.64% at sustain 1 is a live number; the same 0.64% at sustain 5
is a footnote.** My sweep measured the tie's EXISTENCE and its OPERATOR and never asked what the row's
sustain window did to its weight. **That is a gap in SL-5 as written, not just in my sweep** — see the
amendment plan, `runs/2026-09-12_SL5e_REALISATION_PLAN.md`.

**⚠️ AND THE DIRECTION THE DEFECT RAN — RED's finding, and it is the generalisable half.** FT-07 is
bear-relevant; FIRE is the bear direction; **RED's bear-relevant re-cut window (9/4–9/11) had closed the day
before.** So the float defect was handing the desk a free fire that RED was, by its own ratified fence, no
longer permitted to legislate. **A dated discretion fence holds against the owner's HANDS and not against
the owner's TOOLS.** Minted as **PAT-157**; RED carries it as ML-RED-241.

**RED's fix, reported:** exact-Decimal scaling on the published string in BOTH `boot.py` and
`base_rate_review.py`; `930` allocated as a **one-atom HOLD band** (neither fires nor exits) — which
*documents* the ratified letter rather than re-cutting it, the correct move inside a closed fence;
`scripts/test_tie_atoms.py` 5/5 with a positive fixture at the declared precision **and** a non-strict
control so the fix cannot over-correct. Commit `9cbabc23b`.
⚠️ **RED's own declared residue, carried here so it is not lost:** the test covers the 20 legs `METRIC_MAP`
maps; **FT-08 and FT-11 are unmapped and unswept**, and FT-11 remains benign *by luck* — `ft11_delta5()`
still differences in raw float. RED has carried it to a pre-window check rather than calling it clean.

**⭐ AND A COMMON-MODE FINDING THAT UPGRADES PAT-083:** RED's two tools agreed on every tie value — and
agreed **only because both multiplied in raw float in the same direction.** Cross-tool agreement was doing
**no verification work at all** while looking like the strongest kind. *Agreement between a tool and its own
copy is one measurement, not two.* PAT-083 extended.

**WHAT THIS CHANGES ABOUT THE SWEEP'S OWN CONCLUSIONS:** M1 stays the one live uncorrected mismatch, and it
is now **CORRECTED** by the owner. The ≈20 UNSTATED population is unaffected. **But my coverage-limit line
#4 — *"tie sets I marked non-empty are representable, never known to be realised"* — should be read as an
admission rather than a caveat: every one of those ≈35 non-empty tie sets is one query from being measured,
and I measured none of them.**

---

## ADDENDUM 2 — 2026-09-12 ~14:2x ET · **MY "TWO ROWS FLEET-WIDE" FIGURE IS WRONG. It is ~1.5, and RED found the half inside its own submission.**

I wrote above, and repeated it in the PROME memo and to RED: *"Exit legs are base-rated at all on exactly TWO
rows fleet-wide (RED FT-06, RED FT-10)."* **RED delivered the SL-5(d) worked examples I asked for, and its FIRST
finding cuts against its own row: FT-10's exit does NOT meet SL-5(d).**

Its entire `exit_source` is one sentence. **No base rate on the exit leg at all** — `rolling_base_rate` carries
four figures for the FIRE and none for the exit. No symmetric-guess refusal, no named historical episode. The
line is INHERITED from VIOLET, and **inheritance transfers the LEVEL, not the base rate**: nothing checked that a
`<140 s=4` built for VIOLET's kill-switch also suits FT-10's un-fire.
**It passes every presence audit while carrying no base rate** —
`finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit`, **and my own count is how it passed
mine: I counted rows that HAD an exit figure, not rows whose exit figure was independently established.** The
sweep's unit was PRESENCE, and presence is exactly what that class defeats.

**⇒ Corrected figure ~1.5 of 107 legs — and the error ran in the bad direction**, overstating fleet compliance on
the clause I was calling the least-observed. Corrected here and in what I have told RED and PROME.

**RED's remedy is better than a demerit and I accept it:** SL-5(d) should ADMIT an inherited exit line — one
independently established, already observed firing, on an instrument and basis **stated** identical to the fire
leg — as a legitimate, cheaper route, **WITH a required disclosure that no independent base rate was computed.**
That converts a silent shortfall into a documented one, which is what a registration standard is for. **9/14.**

## ⭐ THE FINDING I DID NOT ASK FOR, AND IT IS THE BIGGEST THING THE SWEEP PRODUCED
**RED recomputed FT-06's two legs from the primaries today** (VIXCLS n=9,271; CBOE SKEW_History n=9,225) **and
THE ASYMMETRY HAS INVERTED.** At registration: fire 6.9% vs exit 27.0% — the exit **~4× MORE** likely. Trailing-3y
today: fire 28.86% vs exit 18.88% — the exit **0.65×, LESS** likely.
**Nothing looked, and nothing was going to.** The exit never fired, so there was no event, no row, no grade and
nothing for a staleness clock to key on. `base_rate_review.py` recomputes each LEG; **the RATIO between a row's
two legs is not a tracked quantity anywhere in the fleet.** A fire leg that drifts gets caught because the fire
is what people watch and what leaves a trace; **an exit leg's justification can expire in silence — and it is the
leg that decides WHEN YOU STOP BEING WRONG.** Minted **PAT-159**.
RED kept the two perimeters explicitly apart (only the RATIO compares across them, never the levels) and made
**no re-cut** — window closed, and RED is the interested party. *(Incidental self-reproduction: FT-06 full-3y
29.2% registered vs 28.86% recomputed; FT-10 17.8% vs 17.53%.)*
**Proposed SL-5(d) content, ACCEPTED for 9/14:** the scheduled review recomputes **BOTH legs on ONE perimeter and
records the RATIO**, not the levels.

## THE GOVERNANCE HALF — PAT-160
FT-06's **fire is anti-bear**; its **exit is pro-bear**. The ~4× looser leg ran in this bear desk's **own book
direction** — and RED kept it, disclosed it in `action_magnitude`, and declined to re-cut post-fire.
**RED's line, and it is the usable one: the tell that you are about to re-tune a leg improperly is that the fix
happens to help you.** *"27% is too loose for an exit" is a real rigour argument, and acting on it would have
removed a pro-bear trigger a bear desk has every incentive to keep loose.* The discriminator is **DIRECTION, not
sincerity** — no judgement about motive is needed and a third party can check it from the letter alone. Minted
**PAT-160**; it composes with the FERT `≥1 OPEN prediction` incentive risk already on the 9/14 agenda, which is
the same shape mirrored.

⚠️ **AND A NOTE ON THIS ADDENDUM'S OWN GUARD:** the script that wrote it first refused, because its
already-applied check tested for the substring `ADDENDUM 2` and the FIRST addendum is titled
*"ADDENDUM 2026-09-12"*. A containment test on a prefix that is also a date. Harmless here because it failed
CLOSED — but it is `finding_lenient_parser_reports_unparseable_as_a_behavior`'s neighbour, in a guard I wrote
thirty seconds earlier, in the record about operator and boundary precision.
