# RED SCRATCH — canonical session handoff
**Written:** 2026-09-14 13:5x ET [`date`-verified] · **Session:** S45 (PROME WQ-184 Tier-1 spawn, DOCKET L341 + L344) · **Supersedes:** S44 (2026-09-12)

---

## CHANGES SINCE (what moved while RED was offline, 9/12 → 9/14)

- **WALTER CO-SIGNED the `state`/`state_detail` split** (live session `walter-d9`, this session). Q1 YES · Q2 co-signed with one condition · Q3 **no WALTER executable parses `state`**.
- **PROME independently reproduced the `27 of 45` false extraction** and found a **second** false candidate in the same cell, `23-of-40`.
- **Nothing published.** ^SKEW has no 9/14 bar; FRED's frontier is still **2026-09-10** on all five Treasury series — the fourth session with no 9/11 cell.
- **ICE BofA DID publish 9/11:** HY 265 · BB 150 · CCC 1,076 ⇒ **CCC−BB 926bp, a fresh high.**

## WHAT I DID

1. **L344 SHIPPED — `state`/`state_detail` split, co-signed.** Canon 18 → 19 cols, `state_detail` appended LAST. `state` 15,346 B → 178 B. **SCAN view 30,691 → 15,523 B = 94.3% → 47.7% of BUDGET.** 🔴 **Proof it is a FIX and not headroom: today's grades added +4,493 B to canon and the view did not move ONE BYTE.** Acceptance conditions written before the edit, verified mechanically after (zero information loss 12/12 · exactly one `N-of-M` per projected cell and it IS the sustain count · 16 columns byte-identical · neighbours ordinary/overlap/missing-info tested).
2. **L341 DISCHARGED BY MEASUREMENT — 2 vectors measured at the primary, 6 routed, 0 rubber-stamped.** VX debt **8 → 6**. Plus 15 KB terminal rows re-classed `n/a-historical` **by pattern** (the tool named 14 and printed 6).
3. **Today's grades: BOTH UNGRADEABLE, and that is the finding.** FT-10 **held at 1-of-4** — no 9/14 bar, archive byte-identical to my 9/12 pull. FT-11 **NO NEW GRADEABLE WINDOW** — re-grading the 9/10 window would manufacture a second data point out of one observation set.
4. **FT-12 composition disagreement PRE-REGISTERED before any fire**, on WALTER's pre-fire flag. Letter stands, no re-cut.
5. 🔴 **FT-11 leg (iv) was NOT "benign by luck" — my own S44 reading was false, in my favour.** Raw float **rejected satisfactions the letter accepts** (80 of 201 realistic levels, registered non-strict operator). Fixed to exact decimal; regression test added to the EXISTING control.
6. **Whole inbox drained** — 11 top-level + 1 WALTER-lane, all dispositioned and moved. **`board_log.tsv` BREACHED at 101.8% on the append and was rotated to 41.6%.**
7. Packets → **CARL · HAWK · REGINALD · HENRY · LABOR**. Live doorbells → **WALTER · DAEDALUS**.

## NEXT SESSION (dated, priority-ordered)

1. 🔴 **TONIGHT / FIRST THING: grade the 9/14 ^SKEW bar.** It publishes after ~17:00 ET and was **held, not pushed** — the count is owed for HOURS, not rescheduled. ⛔ **Basis is `SKEW_History.csv` ONLY.** ⚠️ **The delayed-quotes mirror returned HTTP 403 today** — do not silently substitute it; if the archive is late the grade is HELD again, and say so.
2. 🔴 **FT-10 chain 9/15 · 9/16. EARLIEST FIRE IS WED 9/16** = FOMC decision + SEP + VIX quarterly SOQ. Bar 1 = 154.49 [9/11]. **Write the decision framework BEFORE 9/16** — do not improvise on the most consequential grade of the quarter.
3. 🔴 **FT-12 is the nearest line on the board: HY 265 vs <260, and it is moving TOWARD it, not away.** The 9/6 STATUS cell said "widening AWAY" and that is now FALSE (corrected today). **The composition disagreement is pre-registered — apply the letter, then record the disagreement. Both halves are obligatory.**
4. 🟠 **A PRE-APPEND SIZE GATE for read-capped surfaces — this is the one to actually build.** S44 predicted the `board_log` breach in writing, S45 read the prediction at boot, intended to avoid it, and breached anyway. **A written prediction is not a control** (ML-RED-246). Same class: `STATUS.md` is still **94.1%** after today's rotation — real headroom is 1,920 B, but it is still rotate-tier and the next substantive session hits it again.
5. 🟠 **STATUS hypothesis-weight table is stamped `S29 8/12` — 33 days — and its Key Driver cells cite CCC 1023 · Brent 88.48 · SKEW 135.59 · VIX 14.82** against today's 1,076 · 106.08 · 154.49 · 16.74. **Not touched today: I had already made two correction passes on STATUS and stopped per the two-correction rule.** The weights themselves are a real analytical pass, not a margins edit. **Do it as its own session.**
6. 🟠 **CHG-RED-042 hard backstop 9/30 — 16 days.** HAWK's TD3C impeachment is **accepted as scoped**: it kills TD3C as a *transaction print*, NOT as a series. **Letter unchanged, deliberately** — re-specifying a resolver inside its own window after learning which way it would resolve is the move RED refuses on other desks. "Retires unverified" is a live and honourable outcome and is now arguably the more likely one.
7. 🟠 **5 ACTIVE challenge rows still carried, NOT resolved** — CHG-RED-027 (**124d**, RED's own pre-registered self-falsifier — look here first) · -044 (45d) · -045 (33d) · -049 (18d) · -051 (18d). Resolution events are prose, so the DUE-scan can only flag age.
8. 🟠 **KB: 14 ACTIVE rows past their own `Stale_By`** (oldest KB-RED-068, 24d) and **13 terminal rows cited by live surfaces** (the KB-RED-001 axis-② class). Axis ② is not automatable — it needs a read of each citing surface.
9. 🟡 **CARL owes the denominator, and it is the whole ask.** Not a fourth anecdote: **every CRL revision since registration, with direction-of-benefit and magnitude.**

## OPEN THREADS

- **My own pattern framing on CARL was RETRACTED today, not carried.** *"Three is a prior, a fourth makes it a finding"* is **wrong as stated**: CARL's own three instances already contain a counterexample (**CRL-05 CUT its score**), and counting instances measures nothing without a base rate split by direction-of-benefit. A fourth instance is diagnostic **only if it helps**, and even then only against that denominator.
- **The generalisable half of the FT-11 error:** the float drift is **sign-varying with operand magnitude**. My first sweep sampled the benign end, saw six examples pointing one way, and generalised. **A drift direction is not a property of a float computation — it is a property of the operands you happened to sample.** The same population error then produced 123 phantom failures when over-corrected. Both wrong, opposite directions, one cause.
- **WALTER's reframe of my own finding is better than the finding and I adopted it:** there is no parser at 6b, but **6b is executed by a MODEL reading the rows**, which is exposed to the same false extraction as a regex and plausibly more. I had measured the wrong reader.
- **FT-11's aim** — still routed to BOND as a joint-design question, deliberately not re-spec'd (ML-RED-240).

## PENDING WILL-DECISIONS

**None from this session.** Two non-grades, one shipped schema change under an existing co-sign, one apparatus repair, one vector pass. **No weight moved, no trade implication, nothing gated on Will's hands.**

## GIT STATE

Committed inside `AGENTS/RED/` + 5 self-authored packets (carve-out ①). ⚠️ **Commit `8e1b341c6` has a 103-char subject, over the ≤100 cap (root CLAUDE.md 4d). NOT amended — rule 4b forbids it; recorded here and in the next commit message as documentation debt.** ⚠️ **NO PULL THIS SESSION** — `reviews/` files are modified outside RED's directory (same condition as S44), so "Before pulling" step 2 applies: STOP, do not pull. Push deferred on that basis and flagged to PROME.

---

## ADDENDUM — 2026-09-14 ~14:1x ET (second ending; W-A floor A1/A2/A3 + A5/A6/A7)

**DAEDALUS INDEPENDENTLY VERIFIED the FT-11 leg-(iv) repair** — it attacked with two counterexamples of its own and its own tests refuted both. **State on that repair upgrades: IMPLEMENTED → TESTED → INDEPENDENTLY VERIFIED.** Its correction to its own L258 record is accepted: it had put the "luck" in the off-grid cut, which is a real structural property, not luck — the exposure was a *different leg of the same letter*.

**What it found, and what it missed.** The fail-open `try/except` raw-float fallback I removed from `ft11_delta5()` on principle **was still live in `_scaled()`** — the function my own docstring called "identical in kind." Forced, it returns `930.0000000000001` and fires FT-07's `>930` that the letter forbids. ⚠️ **DAEDALUS named only `_scaled`; the same branch was ALSO in `boot.py scaled()` — the live path, by its own L258 packet's words.** Both removed. **A peer verification narrowed the perimeter without closing it; checking the CLASS rather than the named site is the only reason the live path got fixed.**

🔴 **My own fix for the unreachable-test defect REPRODUCED the unreachable-test defect.** Adopting PAT-172's remedy I made the suite assert its own case count, incremented the counter between the verdict and the accumulator, and **the suite printed a visible FAIL line and "ALL PASS" in the same output.** A meta-check is not exempt from the class it polices. Now computed once and **FALSIFIED rather than trusted** — deleting one check's increment makes the suite exit 1, verified in a temp copy.

**FT-08 perimeter gap closed by declaration** (DAEDALUS's second point, accepted): unmapped BY DESIGN, so the compound is computed outside both instruments and inherits no exact-decimal discipline, and `>= 3.0` makes a corrupted compound a **silent false negative on a re-arm trigger**. The grading rule is now in its basis cell because no code will ever tell a hand-grader. ⛔ Not a claim it has mis-graded.

**Nothing analytical moved: no weight, no threshold, no trigger state, no thesis implication.** FT-07 sits +146bp from its tie. `boot.py` re-run — all 12 legs identical, FT-10 still reads the 09/11 bar, re-confirming today's held grade. ML-RED-248. SCAN view 16,608 B = 51.0% of BUDGET.

**Unchanged from the main handoff:** NEXT SESSION items 1–9 all stand, **item 1 (grade the 9/14 ^SKEW bar tonight after ~17:00, archive only) is still the first thing.** No pull, no push — `reviews/` still dirty outside RED's dir.

### ⚠️ ADDENDUM-2 CORRECTION — my "rotation" was a TRIM and did not meet canon's own stop criterion

**DAEDALUS flagged a denominator error and checking canon surfaced a worse one underneath it.**

**① The label, fixed (5 files).** `32,550 B` is the **BUDGET**; the harness single-read **CAP** is **~54,250 B** (`READ_CAP.md` rule 1: the budget is 60% of the cap). I wrote "of cap" throughout. Harmless at 51%, which is exactly why it is worth fixing now rather than at the number where it isn't — and it is a registered class, `[[finding_instrument_reports_clean_against_the_wrong_reference]]`, n=9, with READ_CAP's own table warning "do not conflate the two constants."

**② 🔴 THE REAL FINDING: `READ_CAP.md` rule 5 sets rotation tiers — START at ≥75% of budget (24,412 B), STOP at <70% (22,785 B). STATUS.md is 31,449 B. I never came within 8,664 B of the stop threshold.**

99.2% → 94.1% → 96.6%. **Canon's stated reason for the stop threshold is precisely what happened to me:** *"so a surface does not re-breach the same week (PAT-055 regrowth)."* **Mine re-breached within the same SESSION, in hours.**

⛔ **So "rotation" was the wrong word and "7.6× the headroom" measured the wrong thing** — a headroom delta instead of the canonical threshold. PROME's brief said a desk at 99% can annotate but cannot learn; **at 96.6% of budget that is still true, and I reported progress against a number canon does not use.** `[[finding_level_without_a_reference_has_two_failure_modes]]`.

**DATED RE-TRIGGER (rule 7 — a remedy leaves a re-trigger, never a leanness claim):**
> **STATUS.md trimmed 2026-09-14 from 32,297 → 31,449 B. This is NOT a completed rotation. Canonical target: < 22,785 B (70% of budget), i.e. 8,664 B still to remove. Re-check at ANY append, or on 2026-09-21, whichever is first.**

**The mass is identified and the work is NOT mechanical:** the hypothesis-weight table's six `Key Driver [8/12]` cells. Rotating them means either re-measuring six hypotheses (a real analytical pass) or folding them verbatim and leaving the weights citing nothing. **Do it as its own session — that is now a canon obligation, not a preference.**

