# Codex review of DAEDALUS — findings + dispositions (2026-09-05 EVE)

**Source:** OpenAI Codex (cross-vendor instrument), relayed by Will in-session. **Reviewer scope:** DAEDALUS charter, workload, scorecard, selected profiles, owner responses, push verifier. **Handling:** each finding verified at the artifact before adoption (a relayed reviewer's finding is a finding to check, not a ruling — Codex was right on all three here, and was wrong once earlier today on its own first receipt count, 17→19). Two HIGH fixed + shipped tonight; one MEDIUM split into a correction I own + a ladder question for 9/14.

Codex's own framing, kept honest: *"DAEDALUS is valuable at finding structural failures, but it sometimes turns an observation into a broader requirement before establishing that the requirement is justified."* With explicit counterevidence against a blanket "overbuilds" read: it limited `validate_all` by back-testing YEYOU's actual findings, and the correction walk found the 4th stale HAWK surface. Not a blanket judgment — a specific tendency to watch.

---

## Finding 1 — HIGH — `verify_push.sh` could certify stale evidence as fresh. **FIXED + SHIPPED.**
**Verified** by reading the script + reproducing before/after in a throwaway repo.
- **Bug 1a:** `git fetch` rc ignored (line 34) → a failed fetch fell through to the CACHED `origin/master`.
- **Bug 1b:** "age" measured against the BRANCH TIP's timestamp (line 62), not wall clock → a stale ref whose match IS the tip computed AGE 0 and false-greened a week-old commit. The 8/23 tip-based age only caught "a newer tip exists"; blind to "the whole ref is stale."
- **Reproduction:** throwaway repo, broken remote → OLD `✅ ON ORIGIN … 0m ago` (false green); NEW `CANNOT CERTIFY — fetch FAILED` rc2.
- **Fix (commit `eb6a80d8c`):** certify only after fetch SUCCEEDS (all-3-failed = CANNOT-CERTIFY); age = wall-clock (`date +%s`). Positive control: the fixed tool certified its own fresh push. RESIDUAL noted in-file (Codex): subject+age is a heuristic for identity, not proof — add a content check for load-bearing use.
- **Impeachment check:** tonight's three commits independently re-confirmed on origin (fresh fetch + `merge-base --is-ancestor`) — they shipped; the tool gave right answers tonight only because the fetch happened to succeed.

## Finding 2 — HIGH — scorecard `correction_efficiency` ratio measures incompatible populations. **WITHDRAWN + SHIPPED.**
**Verified** at `scorecard.py:378/476` + `scorecards/2026-09-04.md:20`.
- `correction_efficiency = pre / (pre + post)`: `pre`=28 = ORCH_LOG touches with a brief defect (col 3); `post`=0 = CORRECTIONS.tsv rows + WQ amendment stamps (col 4). **Different populations, different coverage, no shared event identity, no demonstrated decision-ordering.** The 28/28 = 1.00 is an artifact of `post=0`. Counterexample (Codex): the 8/31 MIDAS touch was a briefing correction AFTER the figure reached HEARTBEAT — not prevention before a decision.
- **Fix (commit `0923f5816`):** ratio WITHDRAWN in the renderer (§8 prints the reason; cols 3/4 keep the raw counts); the one published render annotated (figure struck, not erased); v1 spec marked withdrawn. No threshold was ever proposed on this column (descriptive-only), so nothing downstream retracts. `[[finding_cross_entity_comparison_needs_same_perimeter]]`.

## Finding 3 — MEDIUM — prescriptions can exceed the demonstrated defect. **SPLIT: MIDAS corrected (mine); FERT + meta → 9/14.**
**Verified example; broader tendency INFERRED (Codex's own qualifier).**

**3a — MIDAS (corrected by me tonight, `profiles/MIDAS.md` F-2).** I classified MIDAS's unused COT graders as "detection built, invocation missing" (implying all should be wired). MIDAS's implemented answer (`boot.py`) was narrower and correct: wire ONLY `cot_gold.py` (a puller on a standing cadence whose live STATUS figure was rotting), and DELIBERATELY leave `grade_cot3.py`/`settle_check.py` on-demand — they grade CLOSED questions, and a boot cadence would reapply frozen grading logic to new data (a NEW defect). **Discriminator I missed, and it refines the invocation-missing class:** "invocation missing" is a defect ONLY for a detector measuring a MOVING quantity on a STANDING cadence; a grader for a closed question is correctly on-demand. → candidate PATTERNS refinement, 9/14.

**3b — FERT (→ 9/14 ladder-integrity sitting, NOT changed here).** `profiles/FERT.md` F-1 + the FLEET_MAP FERT row gate "≥1 OPEN forward prediction with Resolve_By" translates the market-L3 leg "predictions resolving." My note already argued this is inside the leg's plain meaning ("resolving" = live, not "resolved" past-tense) and distinguished it from the invented-gate cases (ORACLE/ZHAO/MARCO). Codex agrees it is "an interpretation requiring justification, not automatically defective," and adds the point I did not resolve: **the incentive risk** — a desk that correctly grades its whole book (right outcome) drops below L3 and may manufacture a prediction to re-qualify. **Ladder-interpretation question, Will-gated (same class as WQ-180) → 9/14 LADDER-INTEGRITY sitting**, folded into the ~33-row invented-gate audit. The gate is annotated, not retracted.

**3c — the meta-observation → 9/14.** "Turns an observation into a broader requirement before the requirement is justified." The 9/14 sitting's charge (Codex's own words) is to **distinguish required capabilities from preferred implementations**. This is exactly the ~33-row invented-gate audit already scheduled; Codex's finding is a second, independent read of the same class. No new review layer needed (Codex agrees).

---

## Disposition summary
| # | Sev | Status | Commit / venue |
|---|---|---|---|
| 1 | HIGH | FIXED + verified §3 + shipped | `eb6a80d8c` |
| 2 | HIGH | WITHDRAWN + annotated + shipped | `0923f5816` |
| 3a MIDAS | MED | profile corrected (mine) | this commit |
| 3b FERT | MED | annotated; ladder question → 9/14 | 9/14 LADDER-INTEGRITY |
| 3c meta | MED | folded into the 9/14 invented-gate audit | 9/14 LADDER-INTEGRITY |

**Priority Codex named, all addressed:** repair the push verifier (done) · withdraw the efficiency ratio (done) · use the scheduled ladder review to separate required from preferred (routed to 9/14). No new review layer.
