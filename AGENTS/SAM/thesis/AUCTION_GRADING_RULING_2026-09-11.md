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
