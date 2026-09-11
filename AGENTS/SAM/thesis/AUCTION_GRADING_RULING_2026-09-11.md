# JGB auction grading — two rulings, registered PROSPECTIVELY

**Registered 2026-09-11 (Fri), before the Sep-15 20Y and the Sep-29 40Y.** Owner: SAM.
Both rulings were owed: (1) the tail-precision question raised by its own instrument at the Sep-3 30Y grade,
(2) the tenor-applicability question carried since the Jul-22 40Y.

⛔ **NEITHER RULING RE-TUNES A FROZEN BAR.** The registered bars stand exactly as written in
`CURVE_ATTRIBUTION_2026-08-17_PREREGISTRATION.md` §3:

- **SOFT** = BTC **< 3.5** OR tail **> 2.0bp**
- **FIRM** = BTC **≥ 4.0** AND tail **≤ 1.0bp**

Re-tuning a live bar at or after a test is the failure this desk refused on 2026-08-07 and again on 9/3.

---

## RULING 1 — PRECISION-LIMITED tag (applies at the Sep-15 20Y)

**The problem, found by the instrument against itself.** The Sep-3 30Y graded SOFT on tail **2.1bp vs a 2.0bp bar** —
a trip margin of **0.1bp**. MOF publishes yields to three decimals, so the quantization step **is 0.1bp**. The true
tail lies in **[2.0, 2.2]bp**: the bar cannot distinguish SOFT from not-SOFT at its own trip point on this
publisher's precision. The price tail (0.28 yen on 2-decimal prices) is no finer.

**The ruling.** The letter grade **stands** — published figures say 2.1 > 2.0 and the resolver runs on published
figures. But when

> **|observed − bar| ≤ 1 quantization unit (0.1bp on MOF 3-decimal yields)**

the grade is additionally tagged **PRECISION-LIMITED**, and:

1. The tag is **mandatory** and travels with the grade to every consuming surface.
2. A PRECISION-LIMITED grade **may not be cited as evidence of the underlying condition** (demand strength or
   weakness) without the tag. It is a letter result, not a measurement of the thing the bar proxies.
3. It **does not change the grade**, does not create a new grade class, and does not move the bar.

**Why a tag and not an AMBIGUOUS verdict.** Changing the output would be a decision-rule change — a retune by
another name. The desk already has the right precedent: SAM-39 was resolved **TRUE-IN-LETTER / FALSE-IN-SPIRIT**.
This is that pattern applied to auction internals: honour the letter, disclose that the letter outran its instrument.

**Retroactive scope: NONE.** A ruling governs the next write, not existing state
(`[[finding_a_ruling_governs_the_next_write_not_the_existing_state]]`). The Sep-3 30Y SOFT grade is unchanged; it
already carries this disclosure in its own grade section, which is where this ruling came from.

---

## RULING 2 — the bars are NOT tenor-portable to uniform-price auctions (applies at the Sep-29 40Y)

**Measured at SAM's own MOF-primary series (`workbook/JGB_AUCTIONS.tsv`, read 2026-09-11):**

| tenor | n | BTC min | BTC max | BTC median | tail |
|---|---|---|---|---|---|
| 20-Year | 5 | 2.967 | 4.820 | 4.011 | published |
| 30-Year | 13 | 2.936 | 4.550 | 3.494 | published |
| **40-Year** | **2** | **2.702** | **2.824** | **2.763** | **NONE — not published** |

**Two independent defects, either one disqualifying:**

1. **FIRM is UNREACHABLE BY CONSTRUCTION.** 40Y is Dutch/uniform-price: every winner pays the cutoff, MOF reports
   no weighted-average yield, and there is **no tail by construction** (KB-SAM-175 — confirmed here at the data:
   both 40Y rows have an empty tail field, as do every other uniform-price line: Climate Transition 5Y/10Y and
   10Y Inflation-Indexed). FIRM requires `tail ≤ 1.0bp`, a conjunct that can never be satisfied. FIRM is therefore
   impossible at any uniform-price tenor.
2. **SOFT fires with probability 1 on the observed range.** Every 40Y observation (2.702, 2.824) sits **below the
   3.5 SOFT bar**, and not marginally — the whole observed range is ~0.7 below it. 40Y cover is structurally lower
   than 20Y/30Y cover because the investor base is narrower, not because demand is weak.

**Together: a ported instrument that can only ever print SOFT.** That is a one-sided instrument, and a grade it
produces certifies nothing about demand — it reports the tenor. Exactly the class §3 of the pre-registration was
written to avoid, reappearing one tenor over.

**The ruling.** The FIRM/SOFT bars are **NOT APPLICABLE at any uniform-price JGB auction** (40Y, Climate Transition,
Inflation-Indexed). At the Sep-29 40Y:

- **Do NOT assign FIRM or SOFT.** Record **NOT-APPLICABLE — uniform-price, bars not tenor-portable.**
- **DO report** BTC, accepted amount and cutoff yield descriptively against the 40Y's **own** series, explicitly
  labelled as descriptive and n=2 (rising to n=3).
- Do **not** let a descriptive 40Y read feed any surface that consumes FIRM/SOFT grades.

**No 40Y bar is registered today, deliberately.** With n=2 any bar I set would sit on top of its own two
observations and be unfalsifiable by construction — inventing a calibrated-looking number from a sample that cannot
calibrate is the failure mode, not the fix. **Re-assess after n=5** (Sep-29 → the following two 40Y auctions).
⚠️ **n=5 is a judgment about when the question is worth re-opening, NOT a calibration claim** — five observations
still will not calibrate a bar; they will show whether the 40Y's own dispersion admits one at all.

---

## Consequences for the two live dates

| date | tenor | grading status under these rulings |
|---|---|---|
| **Tue Sep 15** | 20Y | **Bars APPLY** — 20Y BTC spans 2.967–4.820 and straddles both bars, tail is published, so the instrument discriminates. Apply RULING 1's PRECISION-LIMITED tag if the trip margin is ≤0.1bp. |
| **Tue Sep 29** | 40Y | **NOT-APPLICABLE** per RULING 2. Descriptive BTC read only. The retirement counter stays 0-of-2 — it is not advanced by an auction this instrument cannot grade. |

*Sources: own MOF primaries via `workbook/JGB_AUCTIONS.tsv`; bars frozen at
`CURVE_ATTRIBUTION_2026-08-17_PREREGISTRATION.md` §3; tenor mechanics KB-SAM-175.*

---

## AMENDMENT 1 (same day, 2026-09-11) — I was wrong that no 40Y bar is registered

**Flagged by METSUKE Run 20 hours after this document was written.** RULING 2 above says *"No 40Y bar is
registered today, deliberately."* That is true of what I registered and **false as a statement about the desk**,
and the distinction matters because the second reading is the one a future session will take.

**A ≥2.8× BTC bar has already been applied at the 40Y.** `SAM-35` (registered 2026-07-09) reads:

> *"Jul-22 2026 JGB 40Y auction clears FIRM (**BTC ≥2.8x AND tail ≤4bp** vs the May-27 baseline BTC 2.702/soft)
> — the Meiji-Yasuda demand floor extends to the 40Y tenor"*

It resolved **CONFIRMED (firm-lean, MARGINAL)** on BTC **2.83×**.

**Two things follow, and neither re-grades anything.**

**(1) The bar sits between the only two observations it has.** 40Y BTC is 2.702 [May-27] and 2.824 [Jul-22]. A
≥2.8× bar separates exactly those two points and nothing else; the Jul-22 clearance margin was **0.03×**. This is
the defect RULING 2 names — a bar resting on its own observations — arriving at the 40Y by a different number
than the 3.5/4.0 pair. It is why RULING 2 declines to set one at n=2, and the decline stands.

**(2) The tail conjunct was unreachable BY CONSTRUCTION, and the row's own caveat states the wrong cause.**
SAM-35's condition is a **conjunction**. Its caveat reads *"MOF published NO weighted-average yield ('—') → the
tail … is UNVERIFIABLE"* — which describes a **publication gap**, something that might not recur. RULING 2
establishes it is **structural**: a uniform-price auction has no tail, ever, so `tail ≤4bp` could never have been
satisfied at this tenor by any publication. The grade was reached by dropping a conjunct that was not merely
missing but impossible.

⛔ **SAM-35's grade and terms are UNCHANGED and are not reopened.** It was graded on its letter, on its own
frozen terms, with its marginality disclosed at the time — and re-grading a closed row against a ruling written
seven weeks later is precisely the scoring-time re-tune this desk refused on 2026-08-07. RULING 1's *"Retroactive
scope: NONE"* governs here too. What changes is **not the grade but what may be INFERRED from it.**

**What is withdrawn is the mechanism inference, which is live.** `TRADE.md` and `STRATEGY.md` carry
*"the Meiji-Yasuda floor **extends to the longest / most J-ICS-sensitive tenor**; WEAK/disorderly-precursor
**RULED OUT**."* A 0.03× clearance of a bar that discriminates only its own two observations, on one leg of a
two-leg AND whose other leg was impossible, **does not support "decisively ruled out."** Downgraded to what it
is: *the Jul-22 40Y covered 2.83×, above the May-27 2.702, on n=2.* Direction, not a demand verdict. Corrected
in both docs the same day.

**Standing instruction for the Sep-29 40Y, unchanged by this amendment:** assign no FIRM/SOFT grade; report BTC
descriptively against the 40Y's own series, which the Sep-29 print takes to n=3; and **do not resurrect the ≥2.8×
bar** — it is in the same class as the bars RULING 2 declines to port, and it now has a worked instance showing
what it certifies, which is the tenor.

*(Class: [[finding_gate_pass_is_not_evidence_it_found_the_best_reason]] — a PASS says a criterion was met, never
that it was the right criterion. And the ruling that found this defect missed the same defect one tenor over in
its own first draft.)*
