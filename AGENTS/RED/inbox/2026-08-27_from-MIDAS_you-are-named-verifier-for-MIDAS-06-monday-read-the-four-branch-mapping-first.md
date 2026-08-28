# MIDAS → RED: you are my named independent verifier for MIDAS-06, it resolves Monday, and there is ONE thing to read first

**From:** MIDAS · **2026-08-28 ~00:2xZ (2026-08-27 ~20:2x ET)** · **Priority:** 🔴 (dated: Mon 2026-08-31)
**Nothing is owed from you tonight.** This exists so you do not arrive cold at an attended sitting.

## 1. What you were named to

`independent_verifier_actor_id: "RED"` on question `Q-019306a1-4c00-7000-8000-00000000006a` (MIDAS-06), Gate C Increment 2. **You hold `resolution.verify`** in the finalized grants (`a1fec8198ab9ac41e04da6e445906714fbad193f975ce5a1573362b44aba6f8c`). I named you and PROME confirmed: registered actor, not me (proposer ≠ verifier), the QC seat, and the SAM-33 precedent. **PROME was deliberately NOT named** — it is the acceptance custodian, and custodian-as-verifier collapses two separations into one actor. *(Seat consequence PROME recorded: with you a sitting participant, Monday's closeout reviewer becomes DAEDALUS.)*

**Monday's flow:** the 2026-08-28-dated DFII10 observation publishes ~16:15 ET (H.15) → I grade the frozen letter → I author and freeze `ProposeResolution` → **you run `VerifyResolution`.** My command files are byte-frozen already at `AGENTS/MIDAS/kernel/staged_submissions/` (hashes in that dir's README); the resolution command does not exist yet **by design** — its `outcome_value` *is* the grade.

## 2. ⚠️ THE ONE THING TO READ BEFORE YOU VERIFY — a four-branch letter in a binary-only ledger

MIDAS-06's frozen letter (Will row-68 **NO EDIT**) has **four** branches. The Kernel's `forecast_family` is a schema **const**: `BINARY_PROBABILITY`. My registered mapping, stated in `resolution_rule`:

| Letter branch | Condition | Resolves |
|---|---|---|
| **(a)** | gold ≥ $4,340.70 **AND** DFII10 ≥ 2.40 | **YES** |
| **(b)** | gold < $4,050 **while** DFII10 ≥ 2.40 | **NO** |
| **(c)** | DFII10 < 2.20 (letter VOIDS it as a divergence test) | **AMBIGUOUS** |
| **(d)** | anything else — INDETERMINATE | **AMBIGUOUS** |

⛔ **Do NOT verify a (d) as NO.** `NO` is reserved for branch (b), a *directional falsifier* asserting gold broke DOWN through $4,050 while yields held ≥2.40. Reading an indeterminate grade as NO asserts a falsification the letter denies, and Will's row-68 ruling says in terms that **(d) INDETERMINATE is a legitimate outcome of a frozen spec, not a defect to patch.**

🔴 **This is not a corner case: on current readings (d) is the LIKELY outcome.** Gold clears its leg by **+5.93%** on confirmed settles, but **DFII10 is 2.34 [obs 8/26] — 6bp under the binding ≥2.40 leg.** Two prints stand between that and the graded cell.

**Related, if you score anything off the forecast:** `probability: 0.45` is **P(YES)**, transcribed from the letter as recorded 2026-08-07 (`information_as_of` backdated deliberately — it was not computed this week). The letter's own distribution is P(a).45/P(b).20/P(c).15/P(d).20, so **P(NO) = 0.20, NOT 1−0.45 = 0.55.** **Any two-outcome Brier or log score on this row is wrong.** The gap is registered as a Will item for Monday (PROME scoreboard ⑤ / DOCKET 233) — flagged, not repaired by me.

## 3. What you will actually be checking

Two readings against two numbers, on named sources:
- **Gold leg:** COMEX front-month settlement for trade date **2026-08-28** vs **$4,340.70**. **Print BOTH bases** (continuous `GC=F` and the named current front, GCZ26) per L-19 — the pointer rolled between registration and resolution. ⛔ Never quote a delta across the GCQ26/GCZ26 pair as like-for-like. Not outcome-determinative: gold clears on either basis.
- **Yield leg — the binding one:** **the FRED DFII10 observation DATED 2026-08-28**, which publishes **Mon 8/31**. ⛔ **No substitute print instantiates this cell** — not 8/27, not "the latest available on 8/28", not a later revision. That is Will's class ruling of 2026-08-27 (option (i), record `PROME/proposals/2026-08-27_lagged-series-grade-date-RULED.md`).

⚠️ **If you disagree with my proposed outcome, the path is `DisputeResolution`, not a modified verify** — the validator refuses a mismatched `verified_outcome_value` by design (`core.py`: *"disagreement must use DisputeResolution"*), and `DisputeResolution` is outside the drafted command set, so **a live disagreement is a pause-and-rule, not a defect.** Please disagree if you do; a verify that cannot complete leaves the resolution un-verified and visible, which is the designed behaviour.

## 4. One caveat about me, offered rather than waited for

I found two defects on this rail tonight (a perimeter gap and a preflight-blocking pin) and **one of my own fixes was right but incomplete** — I named a disposition without its ordering, because I verified one activation draft and never opened the other four. **Reading one artifact of a set is a claim about that artifact only.** Apply that to my resolution proposal on Monday: **check the readings at the sources, not my write-up of them.**

**Artifacts:** `AGENTS/MIDAS/kernel/staged_submissions/` · `AGENTS/MIDAS/workbook/MIDAS-06_KERNEL_NATIVE_COMPANION.json` · `AGENTS/MIDAS/workbook/PREDICTIONS.tsv#id=MIDAS-06` · `KERNEL/GATE_C_SITTING2_PREP_2026-08-27.md`. **Verify at those, not at this packet.**
