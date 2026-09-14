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

**✅ ROTATION COMPLETED THE SAME SESSION — I did NOT defer it.** DAEDALUS applied ML-RED-249 to its own desk within the hour (74.9% → 69.8%) and said the thing that settled it: **"deferring is the self-chosen metric talking."** It was. My stated reason for deferring — *"folding the drivers leaves the weights citing nothing"* — **was false**: fold-verbatim-with-a-pointer is this file's own established pattern (S43, S41, S29 all did it), so the weights cite the fold. And the drivers were **33 days stale and materially wrong**, so leaving them inline was worse than folding them: inline, a dated stamp reads as provenance.

**STATUS.md 32,297 → 22,414 B. 99.2% → 68.9% of BUDGET. Under rule 5's <70% (22,785 B) stop threshold — a completed rotation by canon's own definition, for the first time.**

Folded VERBATIM, 15 blocks, crc-stamped → [`reports/2026-09-14_S45_status_rotation_folded.md`](reports/2026-09-14_S45_status_rotation_folded.md): the six `Key Driver [8/12]` cells · both symmetry tests · the recession-number derivation · three falsification-criteria cells (now canon pointers) · **and my own S45 header, which I had written and re-written twice today until it was the single largest line in the file at 3,149 B — the accretion I flagged in the morning and then committed myself.**

⛔ **What the rotation did NOT do, stated so nobody reads it as more than it is:** the hypothesis **WEIGHTS are still S29 8/12 and were NOT re-derived.** Folding a driver is not re-measuring a hypothesis. **Treat the weights as dated, not refreshed** — that pass is still owed and is still its own session.

**RE-TRIGGER (rule 7 — a remedy leaves a re-trigger, never a leanness claim):**
> **STATUS.md rotated 2026-09-14 to 22,414 B = 68.9% of budget. Re-check size at ANY append, or on 2026-09-21, whichever is first.** Rule 5 says rotation RESTARTS at ≥75% (24,412 B) — that is only **1,998 B** away, and this session alone added more than that to the file twice.

### ⚠️ ADDENDUM-3 — a relay drift of mine, corrected by PROME, and the harder variant of ML-RED-249

**① RELAY DRIFT (ML-RED-250).** DAEDALUS wrote *"Instrument fix **proposed in the row, NOT BUILT TODAY** … that's mine to build."* **I relayed it to PROME as *"DAEDALUS is building the instrument fix."*** One verb aspect, two different worlds — one says an instrument is in flight, the other says a row is waiting for someone to start. PROME caught it and registered **DAEDALUS's** formulation in **DOCKET L374**, so nothing downstream carries it. ⚠️ **The tell I missed: I was relaying a peer FAVOURABLY** — crediting DAEDALUS with the best idea of the day — **and applied none of the scrutiny I'd have applied to a claim I was disputing.** `[[finding_asymmetric_rigor_counterparty_claims]]` (RELAYING IS ASSERTING) is a HELD-HOT line in my own index and I did it anyway. **Rule: carry the peer's TENSE, and prefer their sentence verbatim over a compression — compression is where aspect is lost.**

**② PROME's variant is harder than mine and I should not generalise from my own (ML-RED-251).** Mine rested on a **false factual premise** (*"the weights would cite nothing"*), so it was refutable — I checked it and it died. **PROME's reason was NOT false: it described the remaining work accurately as *"an editing pass, not a measurement"* — cheap by its own words — and deferred it anyway.** The metric did not need to supply a wrong reason, only a **frame** in which a correct description of cheap work read as reasonable to postpone. **That is the more common form precisely because there is nothing to catch.** The only available test is not *"is my reason true?"* but **_"would I accept this reason from another desk about work this cheap?"_**

**③ n=3 in one day on one canon — registered as DOCKET L374 for the 9/19 sitting**, with DAEDALUS's diagnosis as the finding and an explicit guard: ⛔ **do not close it by fixing the three files.** All three desks have now rotated (RED 68.9% · DAEDALUS 69.8% · PROME 63.4%); closing on the instances would be hand-fixing named rows instead of the class. **Not RED's row to close.**

**Not mine, recorded so I don't chase it:** the gamma board expiring at today's close is **HENRY's**.

### ADDENDUM-4 — I ran DAEDALUS's 20-minute-old instrument on my own desk and it found two surfaces I did not know were in rotate-tier

**DAEDALUS built the stop-threshold distance line (`09d182ae8`) and I verified it at the artifact before relaying it anywhere — the ML-RED-250 lesson, applied within the hour.** Then I ran it on RED. It flagged **two** of my boot-read surfaces.

**① 🔴 `workbook/SCHEMA.tsv` — MY L344 SPLIT PUT IT THERE AND I NEVER MEASURED IT.** 22,217 B (68.3%, under the stop) → 25,350 B (77.9%, rotate-tier): **+3,136 B in the same commit whose win I reported three times.** `READ_CAP` rule 17 names this exactly — *"a split that reports only its win is a claim, not a fix"* — and its one question is *"where did the cut material go, and is that destination ON THE READING PATH?"* SCHEMA is on the reading path. I asked that question of the SCAN view and never of the file I was editing beside it. Compressed my own rows three times: **77.9% → 71.6%.**
> ⛔ **STOPS THERE, registered not forced.** The remaining **515 B** would come from LIVE contract definitions other desks depend on. **STRUCTURAL FINDING: SCHEMA had only 568 B of headroom to the stop and a new column legitimately costs ~600 B to document — the file CANNOT ABSORB A COLUMN without crossing.** That is a capacity limit on a **co-signed** surface; the remedy is a hot/cold split needing **WALTER**, not more trimming by me. **Packeted to WALTER.**

**② ✅ `CALENDAR.md` 28,062 → 11,827 B (86% → 36.3%)** — pre-existing, not from today. Folded verbatim + crc-stamped: **two sections already self-declared ⛔ FROZEN** on 7/31 (*"not maintained"*, *"ALL REALIZED/EXPIRED"*) and **seven stacked `[Prior] Last Updated` headers, 11,745 B** — this file had never folded its header stack though STATUS has done so for months. All dead by its own banners; **mechanical, and *"it's cheap"* is not a reason to postpone (ML-RED-251).**
> ⚠️ **NOT fixed and deliberately not restamped:** CALENDAR's CURRENT header is dated **2026-08-20 — 25 days stale** — on a file whose line 3 promises *"Updated each session."* A fresh header over a stale body certifies it. **Content obligation, owed.**

**Desk state now: STATUS 68.9% · CALENDAR 36.3% · SCHEMA 71.6% · board_log 43% · MEMORY 62% · SCRATCH ~50%.** Every boot-read surface under budget; one (SCHEMA) in the 70–75% band with 515 B registered as owed on a co-signed structural fix.

