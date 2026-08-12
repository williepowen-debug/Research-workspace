# 2026-08-06 — To: LABOR (from the Will-directed 8/6 commit review)

**Signal:** Three items from the 8/5 session need YOUR reconcile (not mechanically fixable from outside): the free-parameter narrative contradicts itself across surfaces, the mean-Brier propagation is ~0.0015 off, and the "saved 0.060" claim asserts a saving your own gate #14 forecloses.
**Priority:** 🟡 — next boot; none is decision-blocking, all three went out fleet-wide.

## 1. The knowns-count contradiction (R6)

Your ISM sign-error root-cause exists in two mutually exclusive versions, both live:

- **"Only TWO known / two free parameters":** f5525d8 commit message, `LESSONS.md` L-12, the auto-memory, all four packets (PROME/HENRY/CARL/NEXUS), `NEXUS_BRIEF.md:6`, STATUS dashboard row.
- **"Only 3 were known, back-solved the 4th":** `STATUS.md:2` header and the line-4 retraction record.

The numeric demonstration you show in BOTH versions (true 51.2 → SD 54.3; false 47.4 → SD 58.1) only computes with exactly **one** unknown — and it uses the corrected BA=55.4/NO=55.1, which the 7/6 row did not correctly hold. Likely truth: the 7/6 checker held ~2 of 4 correctly (BA wrong at 56.1, NO absent), making "two free parameters" the honest description of the failure and the shown demonstration an anachronism computed with post-correction values. But that reconstruction is yours to confirm from the 7/6 record. **Ask:** pick one version, state it precisely (which sub-indexes were held, at what values, at check time), and sweep the loser — the four packets already sent mean a 1c consumer pass is owed on whichever framing you retire. The methodological lesson (a check with any free parameter validates nothing) survives either version.

## 2. Mean-Brier propagation (~0.0015)

`PREDICTIONS_SCOREBOARD.md` §A prior chain reconciles exactly at 9 rows: 0.277×8+0.09 = 2.306 → **0.2562** ✓. Adding LAB-06's 0.64 as row 10 gives (2.306+0.64)/10 = **0.2946 ≈ 0.295**, not the published **0.293** (and the diagnostic counterpart 0.2346 vs your 0.233). Your stated pair is self-consistent (differs by exactly 0.060) but doesn't propagate from your own prior mean. Re-run §D; if unrounded per-row values reconcile it, note that on the scoreboard so the next reader doesn't re-derive the same discrepancy.

## 3. "The 7/31 decomposition measurably saved 0.060 of mean Brier" (NEXUS packet + scoreboard)

Under your own gate #14 the as-made 0.64 **stays in the mean** — the realized mean is the worse number, and nothing was realized-saved; 0.060 is what the reprice *would have* saved had it scored. The current wording claims a realized saving the same paragraph's scoring treatment forecloses. Reword as counterfactual (and note the diagnostic 0.04 is the evidence the reprice was directionally right, which is the actual credit earned).

FYI — already fixed mechanically on your surfaces at the review (commits on `claude/review-recent-commits-f8lwo2`): STATUS header "(3 → 1)" → "(3 → 2)", and three residual live-LAB-06 spots in NEXUS_BRIEF (lines 25/34/36). Verify at next boot; re-style the correction notes to your conventions freely.

— Will-directed review session, 2026-08-06. Full findings: `reviews/2026-08-06_opus5-window-commit-review.md` (R5, R6, minors).
