# Row 66 — DFII10 NO-VERDICT band: DESIGN DRAFT

**Written:** 2026-08-28 (Fri), MIDAS orchestrated touch.
**Status:** ⛔ **DRAFT. NOT APPLIED TO ANY LIVE ROW.** Row 66 is **HELD by Will** until MIDAS-06 grades, and is **PROSPECTIVE for successor rows only.**
**For:** the **~8/29–8/31 re-present** to Will (owner PROME → Will; DOCKET row registered).
**Authority:** ⛔ **None of this is mine to rule.** L-20 / tier test 4 bars me from moving a spec that is both falsifier and threshold. This draft supplies **measurement and a decision shape**, not a decision.

---

## 0. WHAT WAS HELD, VERBATIM

> **66 (f)** — NO-VERDICT band ±Nbp around the DFII10 2.40 boundary (evidence: 2026 σ=3.42bp ⇒ ±1σ ≈ ±3.4bp). **HELD until after MIDAS-06 grades 8/28; then adopt PROSPECTIVELY for successor rows.** Bands belong at REGISTRATION (`finding_prereg_verdict_boundary_must_be_a_number`); adding one mid-window with the tape 5bp out is the tuning shape whichever way it lands. At today's readings ±3.4bp would not change the verdict (2.35 < 2.366) — which is exactly why it is not being ruled against a live tape.
> — `PROME/proposals/2026-08-21_midas-rows-65-69-RULED.md`

---

## 1. 🔴 THE HEADLINE FINDING — "which window?" has only TWO answers, not five

`DFII10` is published to **two decimal places = a 1bp grid.** A band `|print − 2.40| < w` is therefore a **step function of `w` with breakpoints at whole basis points.** Five defensible σ windows collapse to **two** distinct bands:

| σ window | measured 1-session σ | ±1σ band | **admissible prints INSIDE** | flip margin |
|---|---|---|---|---|
| trailing 1y (n=248) | 3.26 bp | ±3.26 | **2.37 – 2.43** | 0.26 down / 0.74 up |
| **2026 YTD (n=163)** — *the row-66 evidence* | **3.42 bp** | ±3.42 | **2.37 – 2.43** | 0.42 down / 0.58 up |
| trailing 2y (n=497) | 3.97 bp | ±3.97 | **2.37 – 2.43** | 0.97 down / **0.03 up** ⚠️ |
| full series 2003+ (n=5,916) | 5.15 bp | ±5.15 | **2.35 – 2.45** | 0.15 down / 0.85 up |
| trailing 5y (n=1,246) | 5.66 bp | ±5.66 | **2.35 – 2.45** | 0.66 down / 0.34 up |

**Two designs, and no defensible window produces the intermediate band 2.36–2.44.** The window argument — which reads like an unresolvable methodological dispute — has exactly two outcomes:

- **NARROW: prints 2.37 – 2.43 inclusive** (recent-regime σ, 2026 YTD / 1y / 2y)
- **WIDE: prints 2.35 – 2.45 inclusive** (long-regime σ, 5y / full series)

⚠️ **This is a decision Will can take in one word, not a research programme.** That is the point of writing it this way.

### 1.1 ⚠️ Therefore: register the PRINT SET, not the sigma

The trailing-2y estimate (**3.97bp**) sits **0.03bp** from flipping the band from narrow to wide. A trivially different missing-value convention (**L-22**, which already forked this desk's n by one observation) or one extra week of data moves it.

⇒ **A spec that registers "±1σ" registers a number that is recomputed at grade time, and therefore a band that silently re-specifies itself.** That is the **KB-059 moving-referent class** — the exact defect escalated on 2026-08-27 for MIDAS-01/02 (`analysis/2026-08-27_registered-specs-keyed-to-moving-referents.md`), where a hardcoded 2yr median drifted through **four vintages in eight days**.

> **📌 RECOMMENDATION 1 (design, not a level):** a successor row registers the **admissible print set** — *"NO-VERDICT if the graded observation is 2.37 ≤ x ≤ 2.43 inclusive"* — and records the σ, window and n **as the derivation, in a non-load-bearing field.** The band then cannot move; the evidence for it is still auditable.

---

## 2. 🔴 THE COLLISION NOBODY HAS RULED: NO-VERDICT vs (d) INDETERMINATE

MIDAS-06 **already has a catch-all**: *"(d) anything else ⇒ INDETERMINATE, hold M1 at 3."* A successor carrying **both** a NO-VERDICT band **and** a residual (d) has **two no-call states**, and a print at 2.38 satisfies both. **The letter must say which fires — before registration, or the grader picks at the grade.**

They are **not** the same claim:

| State | What it asserts |
|---|---|
| **(d) INDETERMINATE** | *The world did not do any of the things I named.* A statement about the **tape**. |
| **NO-VERDICT** | *The instrument cannot distinguish pass from fail at this distance.* A statement about the **measurement**. |

Three dispositions, priced:

| Option | Rule | Consequence |
|---|---|---|
| **(i)** Band takes precedence near the boundary; (d) keeps the rest | a print inside the band grades **NO-VERDICT**; outside, the branch tests run and (d) is the residual | Preserves the distinction. Costs: two no-call outcomes to score, and the calibration ledger needs a vocabulary for both (**cf. L-38** — a ledger's vocabulary is a claim about what it can score). |
| **(ii)** (d) absorbs it — no separate NO-VERDICT | band is decorative on any spec that already has a catch-all | Cheapest. But then the band's only use is on specs **without** a residual branch, and row 66's motivating case (MIDAS-06) is not one. **Makes the band nearly pointless where it was asked for.** |
| **(iii)** Band applies only to the **branch-defining** boundary tests; (d) remains the residual for everything else | a 2.38 print fails (a)'s ≥2.40 test as NO-VERDICT rather than FAIL, and then falls to (d) anyway | Formally tidy, **behaviourally identical to (ii)** in any four-branch letter. |

> **📌 RECOMMENDATION 2:** **(i)**, and say so in the letter. Reason: the whole value of a NO-VERDICT band is that it separates *"the tape said no"* from *"my ruler is too coarse to tell"* — and (ii)/(iii) both throw that away in exactly the letters where it was wanted. ⛔ **Will's call, not mine.** If (i) is taken, the successor's calibration entry needs a **third** outcome token, which is a Kernel-schema question (**L-38**), not a MIDAS one.

---

## 3. WHAT THE BAND WOULD ACTUALLY COST — measured, both candidates

Share of `DFII10` observations landing inside each band:

| Band | 2026 YTD (n=164) | trailing 2y (n=498) |
|---|---|---|
| **NARROW 2.37–2.43** | **20 = 12.2%** | **20 = 4.0%** |
| **WIDE 2.35–2.45** | **27 = 16.5%** | **27 = 5.4%** |

⚠️ **Read the 3× gap correctly.** All 27 in-band observations in the trailing 2y occurred in 2026 — the capture rate is **not a property of the band**, it is a property of **where the tape happens to sit relative to the chosen boundary.** A capture rate estimated at registration can be badly wrong by resolution, for the same reason the referent class exists. **State the capture rate with its window, or not at all.**

### 3.1 The band is not decorative — it would have bitten MIDAS-06

| DFII10 obs | value | NARROW 2.37–2.43 | WIDE 2.35–2.45 |
|---|---|---|---|
| 2026-08-17 | 2.44 | outside | **INSIDE** |
| 2026-08-18 | 2.41 | **INSIDE** | **INSIDE** |
| 2026-08-19 | 2.35 | outside | **INSIDE** |
| 2026-08-20 | 2.35 | outside | **INSIDE** |
| **2026-08-21** | **2.40** | **INSIDE** | **INSIDE** |
| 2026-08-24 | 2.38 | **INSIDE** | **INSIDE** |
| 2026-08-25 | 2.32 | outside | outside |
| **2026-08-26** | **2.34** | **outside** | **outside** |

🔴 **The 8/21 print is 2.40 — the print that SATISFIED MIDAS-06's binding leg (2.40 ≥ 2.40 is TRUE) — and it lands INSIDE both candidate bands.** Had the band been live and applied to MIDAS-06, that print would have graded **NO-VERDICT instead of a pass.**

**This is the strongest possible vindication of the 8/21 hold.** Adopting a band mid-window would have moved the verdict on the very leg it was supposed to be neutral about. ✅ And the ruling record's own claim checks out on today's tape: **2.34 [obs 8/26] is outside both bands**, so a band adopted now still changes nothing about Monday's grade — which is exactly the state in which it is safe to rule.

---

## 4. THREE THINGS THE HELD ROW DOES NOT YET SPECIFY

| # | Gap | Why it matters |
|---|---|---|
| **4.1** | **Which boundary?** Row 66 names only **2.40**. MIDAS-06 has **two** DFII10 boundaries — 2.40 (branches a, b) and **2.20** (branch c). | A band on one boundary and not the other says the ruler is precise at 2.20 and coarse at 2.40. Either band both, or state the reason. **Recommend: band every numeric boundary in the row, same width.** |
| **4.2** | **Symmetric band on a one-sided test.** Branch (a) is `≥ 2.40`. A symmetric ±band makes a one-sided test three-state. | Defensible — measurement error is symmetric even when the test is not — but it should be *said*, because a reader will otherwise expect the band only on the failing side. |
| **4.3** | **Does the band apply to the observation, or to a revision?** FRED H.15 can revise. The grade-date CLASS ruling (Will 8/27) fixes *which observation date* governs; it does not say which **vintage** of that observation. | A print at 2.43 that revises to 2.44 crosses the narrow band's edge. **Recommend: register `first published vintage of the named observation date`**, which is also what the 8/27 ruling's "waits for publication" language most naturally means. Cheap to specify now, expensive to argue at a grade. |

---

## 5. THE PROPOSED SHAPE, ASSEMBLED (for the re-present — a menu, not a recommendation of level)

```
NO-VERDICT BAND  [successor rows only; never retrofitted to a live row]
  boundary(ies) banded : every numeric boundary in the row          [4.1]
  band                 : NARROW  2.37 <= x <= 2.43   (recent-regime sigma)
                    OR   WIDE    2.35 <= x <= 2.45   (long-regime sigma)
                         -- registered as the PRINT SET, not as "+-1 sigma"   [Rec 1]
  derivation (non-load-bearing, for audit only):
                         NARROW  <- 1-session sigma 3.26-3.97bp, 2026 YTD / 1y / 2y
                         WIDE    <- 1-session sigma 5.15-5.66bp, 5y / full series 2003+
  precedence           : band fires BEFORE the branch tests; (d) is the residual  [Rec 2 / opt (i)]
  vintage              : first published vintage of the named observation date    [4.3]
  outcome token        : NO-VERDICT is distinct from INDETERMINATE and needs its
                         own slot in any calibration ledger                       [L-38]
```

**The only genuinely open question for Will is one word: NARROW or WIDE.** Everything else above is a specification gap with a cheap default.

---

## 6. WHAT THIS DRAFT DELIBERATELY DOES NOT DO

- ⛔ **Not applied to any live row.** MIDAS-06 grades Mon 8/31 on its **frozen letter**, band-free. MIDAS-01/02 grade 9/30 on their frozen letters (Option A, KB-070). **Nothing here touches any of them.**
- ⛔ **No level recommended.** NARROW vs WIDE is Will's. This draft's job was to prove the choice is **binary**, not continuous — and it is.
- ⛔ **Not registered anywhere.** No DOCKET row, no GATES row, no `PREDICTIONS.tsv` edit. It is a file in my own directory awaiting the ~8/29–8/31 re-present.
- ⛔ **No fleet generalisation.** DFII10's 1bp grid is what makes the step-function argument work. **A series with finer granularity would not collapse to two answers** — do not port §1's conclusion to another series without re-running it there.

---

## 7. INPUTS

| Input | Source | As-of |
|---|---|---|
| `DFII10` daily observations, five windows (n = 163 / 248 / 497 / 1,246 / 5,916) | FRED primary, `fredgraph.csv?id=DFII10` | pulled 2026-08-28 ~10:5x ET; last obs **2026-08-26** |
| Held-row text | `PROME/proposals/2026-08-21_midas-rows-65-69-RULED.md` row 66 (f) | 2026-08-21 |
| Grade-date class ruling | `PROME/proposals/2026-08-27_lagged-series-grade-date-RULED.md` | 2026-08-27 |
| Moving-referent precedent | `analysis/2026-08-27_registered-specs-keyed-to-moving-referents.md`; KB-059, KB-070 | 2026-08-27 |
| Ledger-vocabulary constraint | **L-38** | 2026-08-28 |
