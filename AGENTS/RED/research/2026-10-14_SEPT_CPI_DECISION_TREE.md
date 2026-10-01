# September CPI (Wed 2026-10-14, 08:30 ET) — pre-written decision tree

**Written:** 2026-10-01 (S50), **13 days before the data**. Will-approved sweep item B5. Every figure is RED's own pull, 10/01: FRED CPILFESL / CUSR0000SETG01 / CUSR0000SAS4 / SASLE / SAH1, and the Cleveland Fed `nowcast_month.json` stamped 2026-10-01. **Nothing here moves a weight today.** Its job is to remove discretion on 10/14.

Two separate axes, never bundled (ML-RED-085): **(I) FT-08, a mechanical registered trigger**, and **(II) CHG-028 leg 1, a composition reading.** A third, the market reaction, is recorded and scores nothing.

---

## (I) RED-FT-08 — `CORE-CPI-3MO-ANN >= 3.0`, s=1 → STAGFLATION +3

### Basis ruling, PRE-DATA (amends nothing; resolves an internal conflict)
The registry row describes **two different computations**. Columns `instrument_basis` and `instrument_basis_operative` (8/12, pre-data) say *Table A MoM, compounded over the trailing 3 published months.* The 9/14 grading-rule sentence in `state_detail` says *from the published index levels.* Published Table A MoM values are rounded to 1dp, so the two can land on opposite sides of 3.0. **This happened in 2 of 41 months since 2023** (2024-09: index 2.97 / Table A 3.25; 2026-02: 3.02 / 2.84).
**Ruling: Table A governs**, because it is the letter registered pre-data in both basis columns. The index-level compound is computed beside it as a cross-check. If they straddle the line, the Table A result is the grade and the split is recorded as a disagreement. The exact-decimal discipline of the 9/14 rule still binds: compound the published 1dp values in Decimal and compare at 1dp. *(This favours non-fire inside the straddle band below, so it is labelled. It is chosen because it is the original letter, not because of its direction.)*

### The arithmetic (June's −0.0 rolls out of the window)
| Sept core MoM, published (Table A) | 3-mo annualized (Table A: Jul 0.2 · Aug 0.3 · Sep x) | FT-08 |
|:-:|:-:|:-:|
| ≤ 0.1 | ≤ 2.43 | no fire |
| **0.2** | **2.84** | **no fire** |
| **0.3** | **3.25** | **🔴 FIRE** |
| ≥ 0.4 | ≥ 3.66 | 🔴 FIRE |

Index basis: fire at **unrounded Sept core MoM ≥ 0.2347%** (Sept SA index ≥ 338.558 vs Jun 336.065 / Aug 337.765). **Straddle band = unrounded 0.235–0.249%**: the index basis fires, Table A (publishes "0.2") does not, so Table A governs → **no fire, disagreement recorded**.

### Prior, so the result cannot surprise anyone
- Cleveland Fed nowcast 10/01: **Sept core CPI +0.20% MoM** (headline +0.53%).
- Nowcast core miss, final nowcast vs actual: 2023+ mean −0.035 / sd 0.110 (n=43). Applied to 0.20, the empirical P(fire) is **19–26%** on the 2023+ sample (Table A / index) and **32%** on the 2025+ sample (n=19). We are 13 days out, so the error is wider than the final-nowcast error. **Working prior: P(FT-08 fires 10/14) ≈ 25–35%.**
- ⚠️ **Selectivity caveat, recorded now so it cannot be used after the fact in either direction:** core 3-mo annualized was ≥3.0 in **8 of 19 months since 2025-01** (24/41 since 2023), most recently Feb–May 2026 (3.02 / 2.86 / 3.20 / 3.17). The line marks a return to the spring pace, not a rare state. **The letter is applied anyway, at full magnitude** (RED `MEMORY.md`, S28 line: *"A pre-registered rule only proves itself in the session it CHARGES you"*). The base-rate finding routes to the CHG-051 spec review. **It is not a reason to discount a fire, and it is not a re-cut**: bear-relevant re-cuts stay window-gated.

### Actions on the letter
| Outcome | Action | Pre-registered offset (sum stays 100) |
|---|---|---|
| **FIRE** | **Stagflation +3** (net-bear +3). CONF unchanged: the row carries no CONF leg. | **Managed −2, Soft −1.** A core re-acceleration cuts most directly against muddle-through and the soft landing's inflation leg. Labelled judgment, written now. |
| no fire | Nothing. A non-fire is the default state and scores nothing (S44). Do NOT bank a 0.2 as disinflation evidence: the 3-mo would still be 2.84, up from 1.97. | — |
| **Exit (only if fired)** | Core 3-mo ann **< 2.5** at a later print, s=1 → Stag −3, reversed onto the same buckets. | — |

⚠️ If the B2 weight re-derivation (due 10/09) lands first, the +3 applies to the re-derived weights, with the offset buckets unchanged.

---

## (II) CHG-RED-028 leg 1 — did oil reach core? (composition; resolves on TWO prints, 10/14 + 11/10)

CHG-028 had a date and no numbers. Registered now, pre-data:

**Per-print OIL→CORE leg** = airline fares (CUSR0000SETG01) MoM **≥ 2.35%** (its 2023+ p75) **AND** transportation services (CUSR0000SAS4) MoM **≥ 0.51%** (its p50).
Base rate since 2023-01: **7 of 43 months (16%)**; **two consecutive: 1 of 42 (2%)**; neither of two: 29 of 42 (69%).
Recent: airfares **+2.69 / +0.21 / +2.22 / +2.68** (May–Aug, three of four ≥ p75: the jet-fuel channel is visible). Transportation services −0.58 / −0.35 / +0.28 / **+0.45**. **August missed the joint leg by 6bp on the services half.**

| Verdict at 11/10 | Condition | Reading |
|---|---|---|
| **REALIZED** (bear: stagflation shape) | leg met on **both** Sept and Oct **AND** FT-08 ≥3.0 at either print | the oil→core channel engaged on two witnesses; ~2% base rate, so informative |
| **NOT REALIZED** (bull: RED's S41 view holds) | leg met on **neither** print **AND** core 3-mo ann < 2.5 at the Oct print | ⚠️ the component half is the modal state (69%), so the core-cooling AND-leg carries the information |
| **NO VERDICT** | anything else (incl. one of two) | recorded; no score either way |

**On 10/14 alone nothing resolves.** Record the leg (met / not met, both figures) and wait for 11/10. Per S25 (ML), do not read a single-print energy pass-through as the channel.

---

## (III) Market reaction — recorded, scores nothing
Record the 10/14 closes: DGS30, 5y5y breakeven, HY OAS (T+1), VIX. Only the registered triggers (FT-02 HY >320 s=3, FT-09 5y5y >2.55 s=5) move anything, on their own letters. Substance and reaction are never netted (ML-RED-085).

## Guards
- Headline will likely print hot (nowcast +0.53%) because of energy. **Headline is not FT-08's metric.** A hot headline with core 0.2 is the S25 null.
- If BLS revises the Jul or Aug core MoM in the 10/14 release, use the **published-as-of-10/14** values for all three months (the letter says "trailing 3 published months").
- Grade by 10/14 EOD. Log the FT-08 result to `registry/` state, a `TRIGGER_OUTCOMES` row if fired, CHG-028's Resolution cell, and ML. Route via OUTBOX + NEXUS_BRIEF if a weight moved (A4).

Sources: [Cleveland Fed inflation nowcasting](https://www.clevelandfed.org/indicators-and-data/inflation-nowcasting) (data file `nowcast_month.json`, stamp 2026-10-01) · FRED series above, pulled 2026-10-01.
