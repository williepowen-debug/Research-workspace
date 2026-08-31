# MIDAS-06 — TERMINAL GRADE: **(a) DIVERGE PERSISTS**

**Graded:** 2026-08-31 ~17:5x ET (Mon), after the 16:15 ET FRED H.15 publication. · **Grader:** MIDAS (PROME-orchestrated touch).
**Graded on the FROZEN LETTER** (`workbook/PREDICTIONS.tsv` row 7; Will-ruled **NO EDIT**, WILL_QUEUE row 68, `PROME/proposals/2026-08-21_midas-rows-65-69-RULED.md`). **The letter was not edited, re-tuned, or re-scoped.**
**Zero capital. No threshold, band or frozen letter moved.** One score moved — **M1 3 → 4** — and it is the letter's own prescribed consequence, not a new threshold.

---

## 0. VERDICT IN ONE LINE

**Branch (a) fires: DFII10 2.42 ≥ 2.40 AND gold ≥ $4,340.70 on BOTH bases. DIVERGE PERSISTS — the premium reassertion is durable on the registered test. M1 → 4, re-escalate BOND/LIQUID.**

⚠️ **And the same desk's own positioning falsifier fired against this read three days earlier.** §5 carries that, undiluted: **(a) is the grade; "the premium is clean" is NOT what (a) says.**

---

## 1. ⛔ THE BAND FENCE — HONORED, AND THE HONORING IS THE POINT

The DFII10 NO-VERDICT band (`analysis/2026-08-28_row66-noverdict-band-DESIGN-DRAFT.md`, committed **4d89967fe 10:54 ET 2026-08-28, BEFORE the print**) proposed **NARROW 2.37–2.43** and **WIDE 2.35–2.45**, both inclusive.

🔴 **The published 2.42 falls INSIDE BOTH candidate bands.** Had either been in force, MIDAS-06 would render **NO-VERDICT** instead of **(a)**.

⛔ **THE BAND WAS NOT APPLIED, AND IT IS NOT A CLOSE CALL.** The draft fences itself, verbatim:

> **HELD until after MIDAS-06 grades 8/28; then adopt PROSPECTIVELY for successor rows.** Bands belong at REGISTRATION; adding one mid-window with the tape 5bp out is the tuning shape whichever way it lands.
> — `PROME/proposals/2026-08-21_midas-rows-65-69-RULED.md`, quoted at the draft's §0

**MIDAS-06 was registered without a band. It grades without one.** Applying a band designed three days before resolution, to a print sitting 2bp inside it, is mid-flight spec patching — the exact thing row 68 forbids and the exact thing the draft's own author fenced against. **The fence held in the direction that costs something: honoring it converts a NO-VERDICT into a fired branch and moves a score.** A fence that only ever produces the comfortable answer has not been tested.

✅ **I do not believe the fence is wrong.** NARROW-vs-WIDE remains a one-word question for Will, prospective for successors only. **Nothing here adopts, re-tunes, or recommends a band.**

📌 **Filed as successor-design evidence, not as a grade qualifier:** this is now the **second** MIDAS-06-relevant print to land inside both candidate bands (2.40 [8/21], 2.42 [8/28]). That is evidence about how often the band would bite — it is **not** a reason to hedge today's verdict, and it is recorded in a separate sentence from the verdict on purpose.

---

## 2. THE PUBLISHED CELL

**Re-pulled at the primary this session, not taken from the tasking brief.**

```
$ python3 FORGE/tools/market-data/fetch.py fred DFII10        [2026-08-31 17:41 ET]
 DFII10    2.42 (2026-08-28)   <-- THE GRADED CELL
           2.34 (2026-08-27)
           2.34 (2026-08-26)
           2.32 (2026-08-25)
           2.38 (2026-08-24)
```

✅ **Observation date confirmed 2026-08-28** — the cell the frozen letter binds to, per Will's grade-date class ruling (option (i), `PROME/proposals/2026-08-27_lagged-series-grade-date-RULED.md`). **VERIFIED.**
**Path:** 2.44 [8/17] → 2.35 [8/19–20] → 2.40 [8/21] → 2.38 [8/24] → 2.32 [8/25] → 2.34 [8/26] → 2.34 [8/27] → **2.42 [8/28]**.
⚠️ **+8bp in one session** — outside the trailing-2y 1-session |Δ| p90 of 6bp (max 14bp) recorded at KB-083. The move that decided the grade was itself a large one-session move.

---

## 3. THE GRADE — BOTH LEGS, ARITHMETIC SHOWN

### Leg 2 — DFII10 (the binding leg)

| Test | Required | Realised | Result |
|---|---|---|---|
| (a)/(b) yield leg | DFII10 **≥ 2.40** | **2.42** | **2.42 ≥ 2.40 ⇒ TRUE**, clears by **+2bp** ✅ |
| (c) void leg | DFII10 **< 2.20** | 2.42 | 2.42 < 2.20 ⇒ **FALSE**, misses by **22bp** ❌ |

### Leg 1 — gold close 2026-08-28, **BOTH BASES** (L-19), **T+1 CONFIRMED**

| Basis | 8/28 close | vs (a) $4,340.70 | margin | (a) leg | vs (b) $4,050 |
|---|---|---|---|---|---|
| **`GC=F`** (daily continuous) | **$4,478.10** | +$137.40 | **+3.165%** | ✅ **PASS** | not < $4,050 ⇒ (b) ❌ |
| **`GCZ26.CMX`** (Dec-26 front) | **$4,529.90** | +$189.20 | **+4.359%** | ✅ **PASS** | not < $4,050 ⇒ (b) ❌ |

✅ **Gold leg PASSES on both bases. The verdict does not depend on basis choice** — which is what L-19 exists to establish.
✅ **Two-pull identity check PASS** — both bars re-pulled and byte-identical on all four tickers (desk discipline, COT#3 §1).
✅ **Both pairs are same-contract at T+1** (`GC=F` 8/27 and 8/28 both on the dying contract; `GCZ26` both on Dec-26) — **no cross-roll delta was taken.** `GC=F`'s daily series rolled to `GCZ26` on **8/31** (both print $4,497.30), i.e. *after* the graded session.

### Branch resolution table

| Branch | Frozen condition | Gold leg | DFII10 leg | Verdict |
|---|---|---|---|---|
| **(a)** DIVERGE PERSISTS → **M1 → 4**, re-escalate BOND/LIQUID | gold ≥ $4,340.70 **AND** DFII10 ≥ 2.40 | ✅ **PASS** both bases | ✅ **PASS 2.42** | 🔴 **FIRES — TERMINAL** |
| **(b)** decoupling CLOSED → M1 → 2 | gold < $4,050 **AND** DFII10 ≥ 2.40 | ❌ FAIL (+10.6%/+11.9% above) | ✅ pass | ❌ fails on the gold leg |
| **(c)** VOIDED → NO-CALL | DFII10 < 2.20 | n/a | ❌ FAIL by 22bp | ❌ fails |
| **(d)** anything else → INDETERMINATE | residual | — | — | ❌ **not reached — (a) fired** |

✅ **NO JOINT SATISFACTION.** (a) and (b) are mutually exclusive on the gold leg; (c) is excluded by the same number that carries (a). (d) is a residual catch-all and is unreachable once a named branch fires. **No adjudication is owed to Will.**

⇒ ## 🔴 **TERMINAL GRADE: (a) — DIVERGE PERSISTS. STATUS = HIT.**

**Calibration:** (a) was the pre-registered **modal** branch at **P(a) ≈ 0.45** (vs P(b) 0.20, P(c) 0.15, P(d) 0.20). The desk's highest-probability branch is the one that fired. *(Per PROME's 8/28 ruling the Kernel forecast row renders `UNSCORED — OUTCOME VOCABULARY MISMATCH`; **(d) is not collapsed into NO**, and this row is not calibration data for the binary family.)*

---

## 4. ⚠️ THE PROVISIONAL READ WAS WRONG, AND SO WAS ITS MARGIN — BOTH CORRECTED HERE

**Provisional [8/28]: (d) INDETERMINATE**, off DFII10 2.34 [obs 8/26], failing ≥2.40 by 6bp. **Terminal: (a).** The provisional was not an error — it was the honest read of the only cell then published, and the desk explicitly refused to grade early. **The refusal was correct: grading early would have published (d) and been wrong.**

🔴 **BUT ONE PUBLISHED FIGURE WAS WRONG AND IS CORRECTED NOW.** STATUS and SCRATCH carried:

> *"Gold clears the re-keyed $4,340.70 by **+4.34%** … on both bases [in-flight 13:37 8/28]"*

**On the T+1-confirmed daily bars that is +4.359% on `GCZ26` and +3.165% on `GC=F` — a 1.19pp spread, not one number.** The "+4.34% **on both bases**" claim was true only of the *live* feed, where `GC=F`'s intraday series had converged to `GCZ26`. **The daily bars never converged: they closed $51.80 (1.16%) apart.**

⇒ **KB-087's n+1, and it bit a published margin.** "Converged" observed intraday is a statement about the **intraday** series; the **daily** bar that gets written is a different object and can still be on the dying contract. ⛔ **Never certify a both-bases claim from a live feed.** → **L-44**
✅ **Not outcome-determinative** — the gold leg passes on both bases with ≥3.1pp to spare. **The margin was wrong; the verdict was not.** Stated in that order deliberately.

---

## 5. 🔴 WHAT (a) DOES *NOT* SAY — THE COT #3 FALSIFIER STANDS UNDILUTED

**Carried item ①, dispositioned here.** Three days before this grade, this desk's own pre-registered positioning falsifier **fired against it** (`analysis/2026-08-28_cot3-grade.md`, KB-090): net/OI **56.86%** [as-of 8/25] vs a boundary of **56.1%/+1.4pp** pre-registered four hours early with its computation and a frozen reference distribution. **Δ +2.17pp.** Composition says **CHASED, not squeezed**: NC long **+20,257**, NC short **−888**, OI **+21,697** — fresh longs are the whole move.

**The consequence for the positioning read, stated plainly:**

| | |
|---|---|
| **What (a) establishes** | The registered *divergence* test passed: gold held ≥$4,340.70 **through** a real-yield rise to 2.42. The M1 mechanism survived its own falsification window. |
| **What (a) does NOT establish** | That the premium is unfunded by spec flow. **It is partly spec-funded, by this desk's own measurement**, and that measurement is three days more recent than nothing in this grade contradicts it. |
| **Net** | **M1 → 4 is the letter's consequence and I am executing it. It is a score on the DIVERGE test, not a clean bill on the premium's composition.** |

🔴 **AND THE CONFIGURATION GOT MORE UNCOMFORTABLE, NOT LESS.** net/OI at the **99.8th percentile** (0.81pp below the 40-year max of 57.67%) went into a session where **gold fell 2.86–2.88%** [8/28, both bases] and **GLD fell 3.24%**. **Crowded-long into a decline, with the yield leg rising 8bp underneath it.** ⚠️ **That is a positioning-risk observation for LIQUID/TERRY — it is NOT a MIDAS call and nothing here is trade-shaped.** Routed, not acted on.

⛔ **Three limits on the impeachment travel with it or it is misquoted** (unchanged from the grade file): the snapshot spans 8/19→8/25 and **cannot pin the 8/19 session** · *"a meaningful part"* **is not "all of it"** — the share was never quantified and inventing one would be worse · **it does NOT re-open MIDAS-07**, which is closed on its registered print.

---

## 6. 🔴 I2 — THE PALLADIUM CONFIRM RAN, AND THE RE-OPEN CONDITION **FIRES**. n=3.

**Carried item ②, dispositioned here.** The 8/28 Pd residual was withheld on 8/28 for one reason and one only: **the 8/4 comparator was computed on settled closes, there is no vendor settle (KB-088), and a moving bar is not like-for-like.** Today is T+1 and the bars are static.

**Method — nothing was re-fit.** Betas/σ hardcoded from `reports/2026-08-27_pgm-surge-attribution.md` via `settle_check.py` (Pd β=1.1095, icept=−0.0703, σ=2.494; Pt β=1.1492, icept=−0.0225, σ=2.012). The frozen model was *applied* to the registered sample (2024-01-02 → 2026-08-26), never re-estimated.
✅ **Reproduction check passed before use:** the frozen model reproduces the canonical report to 3 decimals — Pt 8/4 **3.109σ** (report 3.11), Pd 8/4 **2.694σ** (2.69), Pt 8/19 **0.591σ** (0.59).

### The confirmed print — T+1, same-contract, both gold bases

| gold basis | gold 8/27 → 8/28 | Pd actual | Pd predicted | **Pd residual** | **σ** | >2.5σ? |
|---|---|---|---|---|---|---|
| **`GC=F`** | $4,609.70 → $4,478.10 = **−2.855%** | **+6.803%** | −3.238% | **+10.041%** | **+4.026σ** | ✅ **YES** |
| **`GCZ26`** | $4,664.00 → $4,529.90 = **−2.875%** | **+6.803%** | −3.260% | **+10.064%** | **+4.035σ** | ✅ **YES** |

**Pt:** +0.125% actual, residual +3.428% = **+1.704σ** — **does not clear 2.5σ.** ✅ **Pd LEADS Pt on both bases** (+6.803% vs +0.125%).
**Rank (one-sided, by residual, frozen model over the registered sample):** **Pd 8/28 = rank 2 of 665 (top 0.30%)**, sample max +11.234%. **It exceeds the 8/4 event** (Pd 8/4 rank 6, +2.694σ; Pt 8/4 rank 3, +3.109σ).

### ⇒ RE-OPEN CONDITION **(b)** IS MET

> **(b)** A **third** Pd-led PGM tail event (Pt or Pd residual **>2.5σ** vs gold, Pd leading) — **n=3 is a pattern and demands a mechanism, not another filing.**
> — `reports/2026-08-27_pgm-surge-attribution.md` §7

🔴 **FIRES.** Every clause is satisfied on both bases, on static T+1 bars, with the model frozen before the print. **The 8/4 "residually unexplained" disposition is formally RE-OPENED.**

### ⚠️ AND THE HONEST CONFIRM REVISED THE MAGNITUDE **DOWN**

| | in-flight [8/28 16:02] | **T+1 CONFIRMED** | |
|---|---|---|---|
| Pd move | +7.92% / +8.03% | **+6.803%** | ⬇ |
| Pd residual | +11.77% / +11.31% | **+10.041%** | ⬇ |
| **σ** | **+4.72σ / +4.53σ** | **+4.026σ** | ⬇ **−0.5 to −0.7σ** |
| gold move | −3.41% / −2.89% | **−2.855% / −2.875%** | |

⛔ **CITE +4.03σ. The +4.72σ and +4.53σ figures on STATUS/SCRATCH/VX are IN-FLIGHT and are superseded.** **L-37's tendency held again: the in-flight legs ran HIGH.** ✅ **The claim survives the correction** — >2.5σ by a wide margin, rank 2 of 665, still exceeding 8/4. **The desk was right to withhold and right about the direction; it was wrong about the size by ~0.6σ, which is exactly what a T+1 confirm is for.**

### What this does and does not do

| | |
|---|---|
| **I2 score** | **UNCHANGED at 2 🟡.** The registered upgrade trigger is *"confirmed major SA/Russia outage → 4"* and **no registered trigger fired.** ⛔ **Do not read the score as calm — read it as band-blind.** Moving I2 on an unregistered basis would be setting a threshold; **that is Will's, not mine.** |
| **What DID fire** | A **filing obligation**: §7 says n=3 **demands a mechanism, not another filing.** I cannot supply one today — the three named missing instruments (**PGM lease rates · COMEX/NYMEX PGM exchange stocks · PPLT/PALL share-count flows**) are re-open condition **(c)** and this desk still lacks all three. ⇒ **Instrument-acquisition ask routed to PROME; dated-event ask re-routed to HAWK.** |
| **The band-blindness row** | ⚠️ **NOT adjudicated today.** Its condition requires *"no registered trigger firing"* **and** a no-news character. **I ran no news sweep this session** ⇒ that leg is **UNKNOWN**, not confirmed. The 8/28 one-search non-exhaustive check (VX-MIDAS-I2) is the last evidence and it is three days old. **Recorded as owed rather than asserted.** |
| **Capital** | **Zero.** Nothing trade-shaped. |

---

## 7. WHAT MOVED

| | |
|---|---|
| **MIDAS-06** | **OPEN → HIT, branch (a).** Terminal. Frozen letter untouched; only `status` + `resolution` written. |
| **Scores** | **M1 3 🟠 → 4 🔴** (the letter's own prescribed consequence). M2 1 · I1 1 · I2 2 unchanged. **Composite 7/20 → 8/20.** |
| **Thresholds / bands / frozen letters** | **NONE set or moved.** The row-66 band remains applied to nothing. |
| **Routing** | **BOND + LIQUID re-escalated** (branch (a)'s registered action). **HAWK** re-asked on PGM. **PROME**: registry notes + instrument ask. |
| **Capital** | **Zero.** |

**Corrections published against myself this session: 2** — the "+4.34% on both bases" margin (§4) and the Pd σ magnitude (§6). **Both were found by re-pulling my own numbers, and both are recorded in the direction that does not flatter the desk.**
