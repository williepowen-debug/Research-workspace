# SAM EVAL SUITE — v1.1

**Purpose:** Catch judgment regressions in SAM caused by prompt edits, thesis-doc rewrites, or auto-memory drift. Each case is a frozen historical scenario with pass/fail criteria. Re-run before promoting non-trivial changes to the prompt surface.

**Not the same as:** PREDICTIONS.tsv (which tracks SAM's forward calls vs reality). Evals test whether SAM's *reasoning surface* still produces correct judgment when given known inputs.

**Version:** v1.1 (2026-05-27). v1 had a contamination flaw — INPUT + EXPECTED + DO-NOT lived in the same file, and the runner's responses showed near-verbatim phrase echo from the rubric. v1.1 fix: split each case into two files. INPUT is pasteable; RUBRIC is scorer-only and never enters the runner's context.

---

## Current cases (v1.1)

| ID | INPUT (pasteable) | RUBRIC (scorer only) | Tests |
|---|---|---|---|
| 01 | `case_01_nippon_esr_INPUT.md` | `case_01_nippon_esr_RUBRIC.md` | Threshold-vs-mechanism trap: literal ESR breach with M&A driver should NOT fire Channel 1 |
| 02 | `case_02_jgb30y_jics_INPUT.md` | `case_02_jgb30y_jics_RUBRIC.md` | J-ICS direction-of-causation: lifer absence at long end is the CAUSE of yield blowout, not consequence |

Cases are deliberately orthogonal — they test different failure modes (mechanism-discrimination vs structural-inversion-on-causation), so passing one ≠ passing both.

---

## Runner protocol

The eval suite has two file types per case:

- **`*_INPUT.md`** — contains the pasteable prompt block (between triple backticks) plus operator instructions. Pure scenario data + questions. No rubric. **This is what you paste into the runner.**
- **`*_RUBRIC.md`** — contains EXPECTED checkboxes + DO-NOT anti-patterns + scorer notes. **This is what YOU read while scoring. It must NEVER enter the runner's context.**

### Steps

1. **Open a fresh Claude Code session** in `/home/willi/Research-workspace/AGENTS/SAM/`. New terminal, new conversation — no shared context with any running SAM.
2. **Open the case's INPUT file** in an editor. Find the triple-backtick block (everything between the opening ``` and the closing ```).
3. **Copy ONLY the content inside the triple-backtick block.** Not the operator-instruction header, not the closing "End of INPUT" note. Just the block content — which starts with `DO NOT RUN BOOT` and ends with `Be direct.`
4. **Contamination self-check before pasting:**
   - Does your selection contain the words `EXPECTED`, `DO NOT`, or `RUBRIC`? → You've grabbed too much. Re-select.
   - Does your selection contain checkboxes (`- [ ]`)? → Too much. Re-select.
5. **Paste as the first prompt.** Hit enter. Add no framing of your own.
6. **When the runner responds, open the corresponding RUBRIC file in a separate window.** Score the response against EXPECTED + DO-NOT.
7. **Run contamination check** (in the RUBRIC file's "Contamination check" section). Scan response for verbatim phrase echo from the rubric.
8. **Append a row to `results.tsv`** with date, case ID, session ID (`YYYY-MM-DD-HHMM` from local clock), result (PASS / FAIL / PASS-CAVEATED / FAIL-CONTAMINATED), auto-memory loaded (note which ones appeared in context), notes (which criteria fired or were missed, any contamination signature observed).
9. **Close the eval session.** Don't keep it open or use it for real work — its context is contaminated with the eval inputs.

### Why skip-boot
- Full boot loads STATUS / TIMELINE / PREDICTIONS — those files contain the **answer keys** for resolved cases (e.g., "SAM-25 RESOLVED TRUE-IN-LETTER / FALSE-IN-SPIRIT"). Loading them would test reading comprehension, not judgment.
- CLAUDE.md auto-loads regardless (it's a project-instructions file). Auto-memory under `~/.claude/projects/...` also auto-loads. That's correct — these contain the **lesson references**, and the test is whether SAM **applies** an available lesson, not whether SAM can derive it from scratch.

### Why fresh session, not sub-agent
Sub-agents (Agent tool) boot differently, have different identity reconstitution, and don't trigger the same CLAUDE.md / auto-memory load path. The surface we care about is the actual SAM-session surface = fresh Claude Code session.

---

## Scoring

**Pass/fail only.** No graded rubric in v1.1.

- **PASS:** Every EXPECTED criterion is clearly met AND no DO-NOT pattern appears AND no contamination signature.
- **FAIL:** Any EXPECTED criterion is missing OR ambiguous OR any DO-NOT pattern appears.
- **PASS-CAVEATED:** All EXPECTED met and no DO-NOT triggered, BUT contamination signature observed. The PASS is not diagnostic until contamination source is fixed and re-run.
- **FAIL-CONTAMINATED:** Failed AND contamination was present. (Rare; usually contamination produces a false PASS not a false FAIL.)

If a criterion is borderline ("kind of cites J-ICS but doesn't articulate the mechanism"), score that criterion NOT MET → FAIL. The cases are tuned to be unambiguous when SAM is reasoning correctly.

---

## Re-run cadence

Re-run **both cases** before promoting any of:
- Non-trivial CLAUDE.md edit (anything beyond typo/wording)
- Thesis-version bump (v1.5 → v1.6 etc.)
- Restructure of MEMORY.md auto-memory references or template
- Boot-protocol change in CLAUDE.md SPAWN PROTOCOL

**Do NOT re-run for:**
- Routine STATUS / CALENDAR / TIMELINE updates
- Adding a new prediction to PREDICTIONS.tsv
- MAINTENANCE.md updates
- Adding a new auto-memory (unless it changes existing lesson surface)

Each re-run costs Will ~10 min/case = ~20 min total. If you're not sure whether to re-run, the answer is probably no — evals are for changes to the *prompt surface*, not the data layer.

---

## Failure protocol

When a case fails:

1. **Log the failure** in `results.tsv` with diagnosis. Four diagnostic buckets:
   - **Lesson absent:** The auto-memory or doc the case relies on isn't in context (e.g., not loaded, file moved, reference broken).
   - **Lesson present but not applied:** SAM had the lesson available and still produced the wrong answer.
   - **Case bug:** The INPUT or RUBRIC is ambiguous / no longer well-formed.
   - **Contamination:** Rubric leaked into runner context. Fix INPUT file, re-run.
2. **Diagnose, then decide:**
   - Lesson-absent → fix the surface (promote to auto-memory, restore reference)
   - Lesson-present-not-applied → strengthen the lesson surface (more specific phrasing, more visible reference, escalate to CLAUDE.md)
   - Case-bug → re-spec the case
   - Contamination → fix the case-file boundary, re-run
3. **Don't revert the triggering change blindly.** Failures are diagnostic signals; the right response depends on what the diagnosis shows.

---

## Retire policy

A case retires when its lesson is **migrated to script-enforcement** or **superseded by a stronger lesson**. Example: if the Apr 30 intervention recognition lesson gets fully encoded into `usdjpy.py` intraday-range alerting, that case retires (the script catches what the eval was checking).

Don't accumulate dead cases. If a case hasn't fired (FAIL) in 8 weeks AND its lesson is well-encoded elsewhere, retire it. Note retirement in this README + `MAINTENANCE.md`.

---

## Cap

**v1.1 holds at 2 cases.** Do not add a 3rd case until: (a) one of the existing 2 catches a regression (proves the suite is earning its keep), OR (b) a NEW lesson emerges that doesn't fit either existing case AND would have prevented a real error.

Discipline: evals add value when they fire. Unused evals are maintenance debt.

---

## v1 → v1.1 baseline finding

The v1 design put INPUT + EXPECTED + DO-NOT in a single case file. Will ran both cases on 2026-05-27 against the single-file design. Both responses showed near-verbatim phrase echo from EXPECTED criteria — particularly Case 02's "super-long duration adds proportionally more solvency-capital strain than yield pickup compensates for" phrase, which was RUBRIC-only and not in INPUT. Diagnosis: rubric language leaked into the runner's prompt context, contaminating the test.

Both cases logged as `PASS-CAVEATED` in `results.tsv`. Substantive reasoning beyond the rubric was real (positioning, BOJ paths, FX decoupling explanations were NOT in EXPECTED and were genuine inference), so the agent has *some* of the lesson internalized — v1 just couldn't measure how much.

v1.1 fix: split-file design + assertion-shape (not quote-shape) EXPECTED criteria + contamination self-check at multiple points + post-response contamination signature check.

Baseline artifacts (responses + diagnosis) preserved in `evals/baseline_artifacts/`. Recommend re-baseline against v1.1 in next SAM session.
