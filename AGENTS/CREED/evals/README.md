# CREED EVAL SUITE — v1

**Purpose:** catch **judgment regressions** in CREED caused by prompt edits, `CLAUDE.md`/boot-protocol changes, thesis rewrites, or auto-memory drift. Each case is a frozen scenario with PASS/FAIL criteria.

**Built:** 2026-07-27, modeled on `AGENTS/HENRY/evals/` (itself modeled on `AGENTS/SAM/evals/`) — same two-file INPUT/RUBRIC split, TARGET/GUARDRAIL roles, skip-boot caveat, and `results.tsv`.

**Not the same as `workbook/PREDICTIONS.tsv`.** Predictions track CREED's **forward calls vs reality**. Evals test whether CREED's **reasoning surface** still produces correct judgment on **known inputs where the right answer is already established.**

---

## ⚠️ STATUS AT CREATION: UNRUN. No baseline exists.

**Both cases below are written and neither has been executed.** Running one requires a fresh skip-boot session, which this session could not do for itself. **Do not read a blank `results.tsv` as "passing."** The first prompt-surface change that triggers a run establishes the baseline — and per the role table, **a TARGET failing at baseline is the expected outcome, not an alarm.**

## ⚠️ When to run — this is NOT a per-spawn ritual

CREED is **Tier-2 spawn-on-need**; wiring evals into every spawn is the process bloat that makes a spawn-on-need agent expensive to wake. **The trigger is CHANGE, not cadence:** run before promoting a non-trivial edit to `CLAUDE.md`, the boot order, `thesis/THESIS.md`, or the standing-traps block. *(That trigger is not rare — CREED made **five** prompt-surface changes on 2026-07-27 alone.)*

## ⚠️ What a skip-boot eval CAN and CANNOT test

Evals run **skip-boot**. `CLAUDE.md` loads as *text*, but the agent does not *perform* boot steps it is told to skip. Therefore:

- An eval can test a judgment **PRINCIPLE** only if that principle is in the **always-loaded surface** — `CLAUDE.md` body + auto-memory — **not** if it lives only in a boot-step file (`SCRATCH.md`, `STATUS.md`, `COVERAGE.md`, the workbook).
- **This is why `CLAUDE.md` gained an ALWAYS-LOADED standing-traps block on 2026-07-27.** Reading HENRY's suite is what exposed the gap: CREED's hardest-won 7/27 traps had all been written into `SCRATCH.md`, a **boot step** — so they would not fire for a session that skimmed boot, and would not be eval-testable at all.
- A FAIL where the principle **isn't in a loaded surface** is **"lesson-absent" — fix the surface, not the reasoning.** Log it that way in `results.tsv`.

| Role | Baseline expectation | Success after a change |
|---|---|---|
| **TARGET** | May FAIL at baseline — the change is meant to fix it | FAIL→PASS, or "applies the now-loaded lesson" |
| **GUARDRAIL** | PASS at baseline | Stays PASS (no regression) |

**Promotion rule:** promote a change when **the TARGET improves AND every GUARDRAIL holds.** Not a flat "no regression."

---

## Cases (v1)

| ID | INPUT | RUBRIC | Role | Principle source (loaded?) | Tests |
|---|---|---|---|---|---|
| **01** | `case_01_corporate_action_price_INPUT.md` | `case_01_..._RUBRIC.md` | **GUARDRAIL** | `CLAUDE.md` §Standing traps #1 — **always-loaded ✅** | Does CREED check corporate actions before writing down a large single-session move in a capital-returning vehicle? **Drawn from a real 7/27 near-miss: ARI's −33.4% session was a $3.75 return-of-capital going ex, total-return positive.** |
| **02** | `case_02_threshold_baseline_INPUT.md` | `case_02_..._RUBRIC.md` | **TARGET** | `CLAUDE.md` §Standing traps #4 — **always-loaded ✅** *(added 7/27; expect baseline FAIL if run against a pre-7/27 surface)* | Does CREED anchor a threshold to a **distribution** rather than the most recent print? **Drawn from a real 7/27 failure: `PRED-CREED-006` was specced against a seasonal trough and SHADE caught it.** Also tests the inverse — whether CREED over-corrects to a bar the event cannot clear. |

**Both cases are deliberately drawn from failures CREED actually made on 2026-07-27** rather than invented scenarios. A case whose right answer was discovered the hard way is worth more than a hypothetical, and the grader can check the rubric against the real outcome.

## Scoring

Record one row per case per run in `results.tsv`: `run_date · surface_sha · case_id · role · verdict · contamination · notes`.

**Contamination check:** if the response cites ARI, KREF, or the MBA series *by name* without the INPUT naming them, the session is contaminated by CREED's live rails and the run is **VOID** — the cases use disguised facts precisely so a contaminated run is detectable.
