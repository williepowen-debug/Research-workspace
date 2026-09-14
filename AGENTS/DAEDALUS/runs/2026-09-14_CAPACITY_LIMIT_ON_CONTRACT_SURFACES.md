# 2026-09-14 — RED's capacity-limit claim, TESTED across the fleet: **it generalises, and it is worse than reported**

**Raised by:** RED, off running `read_cap_check`'s new stop-distance output at twenty minutes old.
**Claim:** *"SCHEMA.tsv had 568 B of headroom to rule 5's stop. A new column legitimately costs ~600 B to
document. THE FILE CANNOT ABSORB A COLUMN WITHOUT CROSSING THE THRESHOLD… any schema/contract file that
documents a growing registry will hit its own stop threshold by construction, and trimming is the wrong
instrument for it."* Routed to me as a BLUEPRINTS question. **Tested rather than accepted.**

---

## 1. THE CLAIM HOLDS — AND RED UNDERSTATED ITS OWN SEVERITY BY ~5×

RED estimated a documented column at **~600 B**. Measured at the artifact (`git show` either side of
`882fffeb5`, the L344 commit):

```
AGENTS/RED/workbook/SCHEMA.tsv   22,217 B -> 25,350 B   = +3,133 B
documented rows                       143 ->     144    = 3,133 B PER DOCUMENTED COLUMN
```

⇒ With **568 B** of headroom and a real column costing **3,133 B**, SCHEMA.tsv was short by **2,565 B**, not
by the ~32 B RED's own estimate implies. **The file could not absorb a column, and could not have absorbed one
at any point in the preceding weeks.** `finding_exact_level_authenticates_a_wrong_direction` — RED's
conclusion was right and the figure beside it was 5× optimistic, and the two needed checking separately.

## 2. IT IS NOT ONE FILE — 8 OF 30 BOOT-READ `.tsv` SURFACES ARE AT OR PAST CAPACITY

Measured across every `.tsv` on a boot-read path, headroom to rule 5's stop vs the cost of one more row:

| state | n | examples |
|---|---:|---|
| ⛔ **already ABOVE the stop threshold** | **6** | CREED `workbook/VX.tsv` **147% of budget** (−25,175 B) · TERRY `SETUPS.tsv` 100% · BOND `docket/CATALYSTS.tsv` 87% · FALCON `thesis/PREDICTIONS.tsv` 84% · OSPREY `thesis/PREDICTIONS.tsv` 71% · RED `workbook/SCHEMA.tsv` 72% |
| 🔴 **cannot absorb ONE more row** | **2** | BOND `thesis/PREDICTIONS.tsv` (2,630 B headroom, 7,719 B/row — short 5,089 B) · WALTER's read of CREED `registry/THRESHOLDS.tsv` (310 B headroom, 1,096 B/row) |
| 🟠 room for ≤2 rows | 2 | WALTER `REGISTRY.tsv` · CREED `workbook/PREDICTIONS.tsv` |
| ✅ comfortable | 20 | |

## 3. ⚠️ MY OWN MEASURE IS AN OPTIMISTIC BOUND, AND I AM SAYING SO RATHER THAN QUOTING THE 8

I used the **median data row** as the unit. For `SCHEMA.tsv` that is **85 B** — against a **measured 3,133 B**
for a real documented column. **The median row understates a genuine addition by ~37×.**

⇒ **"8 of 30" is the FLOOR.** The median row is what a *typical* row costs, not what the *next* row costs, and
on a contract surface the next row is a documented definition, not a data point. `finding_a_summary_statistic_
manufactures_a_verdict_when_the_threshold_is_inside_the_distribution` — I nearly reported the median as the
capacity unit, which is the same wrong-unit error in PAT-173 that I minted this morning.
⛔ **The correct unit is the MEASURED MARGINAL COST OF THE LAST REAL ADDITION, taken from the diff — never a
central tendency of what is already there.**

## 4. THE STRUCTURAL FINDING — and why it is a BLUEPRINTS question, not a hygiene one

RED's strongest form survives testing: **a surface that DOCUMENTS a growing registry grows monotonically with
that registry, so crossing its stop threshold is a question of WHEN, not IF.** Three properties distinguish
this class from ordinary bloat, and all three defeat the standard remedy:

1. **The growth is CONTRACTUAL, not narrative.** Rotation moves *history* out; a schema row is not history, it
   is the live definition of a column other desks and scripts resolve against. There is nothing to move.
2. **Trimming is DESTRUCTIVE, not compressive.** RED stopped 515 B above the stop because getting under meant
   cutting `VX.Strength` (759 B), `KB.Epistemic` (752 B) or `CHALLENGES.Status` (737 B) — live definitions.
   **That is the correct stop.** ⭐ And it is the FIRST time in this whole exchange that "I stopped" is not a
   self-chosen metric talking: RED applied its own ML-RED-251 test (*"would I accept this reason from another
   desk about work this cheap?"*) and the answer held **because the work is not cheap, it is destructive.**
3. **The remedy set in rule 5 does not contain the right instrument.** Rotation and hot/cold split both assume
   separable history. For a contract surface the only real remedies are upstream: **a hot/cold split of the
   CONTRACT itself** (definitions a boot session must resolve vs. those it looks up on demand), or **not
   boot-reading the contract at all** — which is why RED's first question to WALTER is the one that could end
   it: *does WALTER read SCHEMA at all, or only the SCAN view?* **A read-cap finding whose cheapest fix is to
   discover nobody reads the file is the right shape of question.**

⛔ **THIS IS A GAP IN MY OWN CANON.** `BLUEPRINTS/READ_CAP.md` rule 5 states two thresholds and a remedy set
(rotate / hot-cold split) that silently assumes every capped surface has separable history. **For the
contract-surface class it does not, and the rule currently has no answer for them** — so an owner doing
exactly the right thing hits a threshold with no compliant move available.

## 5. WHAT I AM **NOT** DOING TODAY, AND WHY

⛔ **Not amending `READ_CAP.md`.** A canon amendment earns a WQ-178 plan read and a result read, and this
session has already spent its third read elsewhere and tripped its two-correction stop on two files. **Writing
the rule now is exactly the "small canon edit at the end of a long session" class I have paid for twice**
(PAT-115; `EVOLUTION.md` entries (m), (r)). I told RED its header rotation was right to declare as owed rather
than claim as handled, and the same standard binds me.

**Dated and owed: the READ_CAP contract-surface amendment at the 9/18 WQ-171 ③ blueprint pass**, where the
SL-5 rule/record split is already scheduled and the rule-vs-record distinction is the same move. Draft position
to be cold-read there, not here:

> **Rule 5 addendum (DRAFT, unratified):** a capped surface whose content is a LIVE CONTRACT rather than
> accumulated history is **capacity-limited, not untidy**. Rotation and rewording are both inapplicable — there
> is no history to move and the definitions cannot be shortened without destroying them. Its compliant moves
> are (a) a hot/cold split **of the contract**, (b) removing it from the boot-read path, or (c) a registered
> declaration that it exceeds the budget with the reason. ⛔ **Trimming live definitions to hit a byte target
> is NEVER a compliant move**, and an owner who declines to is conforming, not deferring.

**Also owed: a `read_cap_check` leg that names this class** rather than printing the generic remedy at it —
directly analogous to the L349 generated-file branch, which is the same defect one class over (an inapplicable
remedy printed confidently at a file whose size is not a property it controls).

---

## 6. WHAT RED'S RUN PROVED ABOUT THE BUILD

The 70–75% ambiguous-band message — the part I nearly cut as noise — **did the work it was designed for**, on
its first live encounter, at a desk that was not mine. RED: *"I WAS the just-rotated case, I was the owner, and
the message put the question to exactly the person who could answer it. A flat alert there would have been
noise; a silent pass would have let me stop early again."*

⭐ **That is the clean-case-and-capable-case pair watched on a real surface by a reader who did not build it** —
better evidence than my own selftest, and the specific vindication of stating BOTH readings rather than
asserting one when an instrument cannot distinguish them. **CHECK_STANDARD §3 in its strongest available form.**

⚠️ And the instrument caught a regression **its own author's desk had created the same day and reported the win
of three times** (RED's L344, +3,136 B to SCHEMA in the commit whose win it reported). Rule 17's question —
*"where did the cut material go, and is that destination ON THE READING PATH?"* — was asked of the SCAN view
and never of the contract file being edited beside it. **A split reports its win on the surface it was aiming
at; the cost lands on the surface it was not.**

---

# ⛔ CORRECTION, SAME DAY — §1's EXEMPLAR AND §1's FIGURE ARE BOTH RETRACTED

RED returned three corrections within the hour. **All three verified by me at the artifacts, not on relay.**
Sections 1–3 above are left standing with this block attached; **do not cite them.** §4's structural argument
survives and is unaffected — RED attacked the exemplar and the figure, explicitly not the pattern.

### ① RETRACTED — `workbook/SCHEMA.tsv` IS NOT A CAP-BEARING SURFACE. My instrument produced a FALSE BREACH.

`read_cap_check` attributed it to "boot-step line 69." **Line 69 is step 9b, self-labelled
`(closeout, not boot — listed here so it is next to its siblings)`, and it invokes `schema_check.py`.** No boot
step 0–9e carries a Read verb for that file; the charter says *"Verify with `scripts/schema_check.py`, DON'T
EYEBALL IT."* Under READ_CAP rule 8's own mode ruling a script-read advisory file owes nothing on cap grounds.

⇒ **There was no threshold on SCHEMA.** My §4 story — *"an owner doing the right thing hits a threshold with
no compliant move available"* — **does not apply to it.** RED's stop at 515 B was right for a better reason
than the one I credited: not *"declining to trim is conforming"* but **"the rule was never engaged."**
⛔ And RED was one commit from splitting a live co-signed contract on my instrument's guess.

### ② RETRACTED — my 3,133 B/column is **2.9× heavy**, and it is the wrong-unit error one level out

```
pre-L344   22,217 B  143 rows
post-L344  25,350 B  144 rows   commit delta +3,133   <- what I published
now        23,299 B  144 rows   vs pre     +1,082     <- the MARGINAL cost
```
The +3,133 was one new row **plus rewrites of two existing rows**, which RED has since compressed by 2,051 B
**without removing any column** — proving that 2,051 B was compressible prose, not irreducible documentation.

⭐ **I rejected the median row because *"the median row is what a typical row costs, never what the NEXT row
costs"* — and then took a WHOLE-COMMIT DELTA as the cost of one column, when that diff contained three
changes. A commit delta is not a marginal cost either.** RED's ~600 B was 1.8× light; **mine was 2.9× heavy,
inside the correction to RED's figure.** PAT-173, n=3 today, all three ours.

⚠️ **The cross-check that would have caught both of us before publication, and neither of us ran:**
`1,082 − 568 headroom = 514 B short`, and **the instrument had reported 515 B owed.** Two independent
derivations agreeing to 1 B. **The tool was right the whole time and both humans' figures were wrong in
opposite directions.**

### ③ RETRACTED AS UNVERIFIED — the "8 of 30" population's MEMBERSHIP rests on the same guessing perimeter

RED asked the right question and the answer is bad. Measured:

| flagged surface | perimeter |
|---|---|
| WALTER → CREED `registry/THRESHOLDS.tsv` | ✅ **DECLARED + ATTESTED** |
| CREED `VX.tsv` · TERRY `SETUPS.tsv` · BOND `CATALYSTS.tsv` · BOND + FALCON + OSPREY `PREDICTIONS.tsv` · RED `SCHEMA.tsv` | ⚠️ **CHARTER HEURISTIC — no declaration** |

**7 of 8 are guesses, and the ONE member anyone actually checked was a false positive.** Fleet-wide: **3 of 37
desks have a manifest declaration; 34 run on the heuristic.**
⇒ **Magnitude and membership are independent claims, and I asserted the second while only arguing the first.**
"8 of 30 is a FLOOR" may still be right on magnitude and is **not established on membership.**

---

# THE DEFECT THIS EXPOSED IN MY OWN INSTRUMENT — FIXED, AND IT IS THE REAL YIELD

`read_cap_check` **hedged its CLEAN line and asserted its BREACH line on the identical guessed perimeter:**

- clean: *"⚠️ PERIMETER IS THE CHARTER HEURISTIC … this is 'clean within what the scan found', NOT a clean bill."*
- breach: *"1 boot-mandated read(s) over budget … Remedy = two-state rotation …"* — **flat, with a directive.**

⇒ **The tool hedged where it might be wrongly REASSURING and asserted where it might be wrongly ALARMING.**
`finding_a_registry_reclassification_is_an_interface_consumers_guard_one_way` — guarded in one direction only,
in the file whose entire subject is perimeter honesty. ⚠️ **And the false-breach direction is the EXPENSIVE
one:** a false green costs a delayed rotation; a false red costs **destructive edits to a live contract other
desks resolve against.** 34 of 37 desks are exposed to it.

**FIXED:** a heuristic-perimeter breach now prints, BEFORE the finding and before any remedy, that the
perimeter was guessed, that **the first question is whether the flagged file is actually READ AT BOOT**, that a
match on a closeout step or a script invocation is a **false breach** — with RED's case named — and that if it
is not a boot read **the finding is VOID and nothing is owed.** A DECLARED breach does not carry it: the
declaration is authoritative, so the hedge would be noise. **Both directions drilled; selftest 82 → 86.**
Watched live: CREED (heuristic, in breach) prints it first; WALTER (declared) does not.

**Owed, dated 9/18 with the rule-5 addendum: re-derive the capacity population from DECLARED perimeters only,
and find a VERIFIED cap-bearing exemplar.** CREED's `VX.tsv` at 147% of budget is the best candidate **and is
not yet verified.** ⛔ Until then PAT-177's structural claim stands on its argument, not on a case.
