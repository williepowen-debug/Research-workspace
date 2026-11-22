# Forecast figures: reconciliation with the outside read-only check of f7fd02a504

**Written:** 2026-11-22 (Sunday), PROME prome-77, laptop, on Will's pasted word of 04:02 ET (item 1; record `PROME/proposals/2026-11-22_wq727-seven-ideas-RULED.md`). Every figure below is from a command run this session; the commands are at the end. This is a reconciliation, not report 2, and re-classes no row.

## Why the outside review could not see the newer figures

| Fact | Evidence |
|---|---|
| The reviewed snapshot is BRENT's commit of Fri 11/20 16:22 ET | `git log -1 f7fd02a504` |
| The scorer change that produced 295 was committed locally Fri 11/20 13:37 ET (096756a5fb) and the seven ideas at 14:52 ET (0ae708683d) | `git log f7fd02a504..HEAD -- PROME/tools/forecast_report.py PROME/ideas/list.tsv` |
| Neither was on GitHub at the snapshot: the laptop slept from about 14:53 ET 11/20; PROME's commits were rebased on top of the snapshot on 11/21 and pushed at the closeout | both commits are in `f7fd02a504..HEAD`; push receipt 525f530926 on origin/master, 2026-11-22 03:48 ET |
| Published now | HEAD equals origin/master after a fresh fetch |

## The figures at each revision

| Run | Scored / decided | Fleet Brier | Hit-rate baseline | Gain, scored | Bootstrap 95%, scored gain | Gain, first-logged | Revised calls |
|---|---|---|---|---|---|---|---|
| Snapshot tree, snapshot's own scorer | 291 / 375 | 0.227 | 0.249 | +0.022 | +0.000 to +0.041 | +0.005 | 38 |
| Snapshot tree, today's scorer | 295 / 375 | 0.226 | 0.248 | +0.022 | +0.002 to +0.041 | +0.005 | 38 |
| Today's tree (525f530926), today's scorer | 295 / 377 | 0.226 | 0.248 | +0.022 | +0.002 to +0.041 | +0.005 | 38 |

**The 291 to 295 difference is the scorer, not the data.** Commit 096756a5fb made the scorer read three ways of stating a probability that it had skipped (a bare decimal; a tier word followed by `P(TRUE) = x`; an opening `PROBABILITY n%`). Four decided calls gained a readable probability. Run on the same snapshot tree, the old scorer gives 291 and the new one 295. Two more calls were decided between the snapshot and today (375 to 377); neither carries a probability.

**Matches the outside review:** 291 calls, 0.227 against 0.249, scored gain +0.022, bootstrap +0.000 to +0.041.

**NOT reproduced (three figures):**
- First-logged gain +0.010: the snapshot's own scorer prints +0.005 (Brier 0.244 at the first-logged probability against a 0.249 baseline).
- 24 revised calls: the scorer prints 38 at both revisions.
- 51 born-decided rows: the scorer's printed table shows 0, because it classes only calls known after 2026-11-05 (40 calls). Counted over all 295 scored calls, 30 are born-decided, all 30 in report 1's closed population.

PROME cannot say how the outside figures were computed. A copy of the repository without its full history would change all three (first-logged values and born-decided classes are read from the commit record), but that is a guess, not a finding. The reviewer's method would settle it.

## What the uncertainty estimates support

| Estimate | Result | Assumption |
|---|---|---|
| Scorer's bootstrap, scored gain | +0.002 to +0.041 | 2,000 resamples, fixed seed, each call treated as independent. The scorer says this overstates certainty: many calls share one root event. |
| Resampling whole desks instead of calls (29 desks) | −0.005 to +0.046 | One run by PROME today, not reviewed. Allows calls within a desk to move together; does not allow for one event shared across desks. |
| First-logged gain, call-level bootstrap | −0.015 to +0.023 | Same independence assumption. |

| Population | n | Gain, scored | Gain, first-logged |
|---|---|---|---|
| All scored calls | 295 | +0.022 | +0.005 |
| Excluding the 30 born-decided rows | 265 | +0.016 | −0.003 |
| Rows whose probability entered the record before the outcome was known (BEFORE) | 245 | +0.015 | −0.001 |

**Plain reading.**
1. The final probabilities score a little better than always saying the base rate. Under the kinder assumption the range just clears zero; when desks are resampled whole it does not. The evidence does not establish forecasting skill.
2. The first-logged probabilities show no measured edge: +0.005 with a range that spans zero, and zero or slightly negative once born-decided rows are left out.
3. About a quarter of the measured gain (0.022 to 0.016) comes from 30 rows whose first committed record was already decided, where the probability cannot be shown to precede the outcome. The rest of the difference between first-logged and scored comes from the 38 revised calls.
4. First-logged means first in a prediction ledger's commit record. A view held earlier in another file is not seen, so "first-logged" can be later than the first judgment.
5. The hit-rate baseline is computed on the same calls it is compared with, which favours the baseline slightly.

⚠️ The class counts over report 1's closed population (30 born-decided) were read today only to answer the outside review's count. Will stopped historical timing checks on report 1 on 2026-11-05; nothing in report 1 is re-labelled by this note.

## For report 2 (2026-12-04), per Will's item 4

Descriptive only, no desk ranking, no per-desk view (WQ-715, 2026-11-17; WQ-619 A stands). It explains where the measured gain comes from (the three-row table above is the start) and what baseline supports it.

## Commands

- `python3 PROME/tools/forecast_report.py` at 525f530926 (today's tree).
- A detached worktree of f7fd02a504 in the session scratchpad: the same command with that tree's scorer, then with today's scorer; the worktree was removed afterwards.
- `PROME/reports/2026-11-22_forecast-figures-reconciliation.recon.py` (beside this file): class counts over all scored calls, the three populations, the first-logged bootstrap and the whole-desk resample. Read only; it imports the scorer and writes nothing.
