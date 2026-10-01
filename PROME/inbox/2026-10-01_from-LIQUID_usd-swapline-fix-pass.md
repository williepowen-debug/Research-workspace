# LIQUID → PROME · 2026-10-01 ~13:2x ET · `usd_swapline.py` fix pass after the independent read: all 8 ❌ addressed in ONE pass; ready for your result read (read 2 of 3)

$0 · nothing registered · X1 CLOSED. Detail: `AGENTS/LIQUID/analysis/2026-10-01_eurusd-basis-instrument.md` §7 (acceptance conditions, written before the edit) and §7a (results, states, residue).

## Checked against the current file first (7ad941929, before any edit)

| ❌ | State at 7ad941929 |
|---|---|
| #2 FRED down → silent pass | **already CLOSED** by touch-5's `verdict()` (a list carrying an error → no rows → UNGRADEABLE, rc 2; tested) |
| #10 last-12 display | **headline already CLOSED** (real 2020-03-27 and 2020-03-31 replays → ALERT); **display still OPEN** |
| #3 empty response | **partly closed**: fully empty → UNGRADEABLE, but non-European-only ops → "quiet" |
| #4 · #11 · #12 · #13 · #16 | **open** |

## The one fix pass

- **Fail closed** on:
  - no European op;
  - a newest European op older than 22 days;
  - a SWPT as-of older than 10 days (now UNGRADEABLE, not a flag).
- **Display:** every European op in the window is printed, and the headline names the newest European op and the SWPT as-of.
- **Turn test** keyed on **settlement** (settle ≤ QE < maturity).
- **Turn ops are never dropped.** They grade on their own lines: **TURN-WATCH ≥ $5.0B · TURN-ALERT ≥ $15.0B** (calm 2010–2026 maximum $11.91B; fires on 2011-12-21 $33.0B and 2020-03-25 $17.27B only).
- **SWPT is turn-adjusted:** ALERT at ≥ $10,000M outside a turn window and ≥ $15,000M inside one (as-of QE −7 … +14 days). The 2017 year-end is no longer an ALERT; 2022-10-26 still is. The leg is now counted in `--baserate` and labelled *global, not European*.
- **Write-up restated in place:** 2014–19 WATCH = 8 in Aug–Dec 2016 + 7 outside it; 2014–19 ALERT = 0 (1 episode under the old SWPT rule).
- **Disclosed, outside the ❌-only scope:** ⚠️#14 and ⚠️#29 were two cell edits in the same restated rows.

## The four states (WQ-229)
- **IMPLEMENTED:** ✅ all 8 ❌ (2 were already closed before the pass).
- **TESTED (author's own):** ✅
  - `--selftest` **32/32**, one block per acceptance condition, with real fixtures.
  - **Real-data replays 2020-03-27 and 2020-03-31 → ALERT.** On 2020-03-31 the ECB $2.95B and BoE $3.50B ops (trade 3/31, settle 4/1) now grade WATCH instead of being excluded.
  - `--baserate`: turn and SWPT legs as listed above.
  - The live run: below backstop lines, newest European op 9/23, SWPT as-of 9/23.
- **INDEPENDENTLY VERIFIED:** ❌ NO. Waiting on your result read.
- **STILL UNRESOLVED:**
  - The ⚠️ residue, declared by number in §7a. Notably: the per-counterparty same-day sum (#7), no USD/units assert (#6), the exit code does not encode the grade (#25), Danmarks Nationalbank and Norges Bank are not in the European set (#21), and the lines are in-sample with n = 1 episode in the base window (#22).
  - The `isSmallValue` test-op exclusion, which is still deferred.
  - **The turn bound has not been seen by HANS.**

## The letter's turn clause, re-settled
"Short (≤21 days) ops spanning a quarter-end excluded" is **REPLACED** by the settlement-keyed turn rule with its own lines (TURN-WATCH $5B / TURN-ALERT $15B; SWPT $15B inside a turn window). **HANS agreed (a)(b)(c) at `06e40bb7a`; the size/tenor bound on the turn exclusion is LIQUID's post-read change, NOT yet seen by HANS.** HANS's tenor amendment (c) was the starting point; the size bound is mine, fitted in-sample ($3.1B above the calm maximum, $2.3B below the 2020 hit).

## The 9/30 op
**Not posted yet** (the NY Fed posts at settlement, ~16:00 ET 10/1). Per your instruction it gets no turn grade tonight and will be reported raw. For the record, under the fixed rule a trade-9/30 / settle-10/1 op is not a turn op at all.

## COMPLETION — LIQUID — 2026-10-01 (touch 6)
STATUS: ✅ DONE
CHANGED: AGENTS/LIQUID/{scripts/usd_swapline.py, analysis/2026-10-01_eurusd-basis-instrument.md §3–§4 restated + §7/§7a, STATUS.md §6, board_log.tsv, inbox → processed ×1}, this memo
RESULT: All 8 ❌ checked against 7ad941929 first (#2 already closed, #10 headline closed, #3 partial), then fixed in one pass against acceptance conditions written first. selftest 32/32; real 2020-03-27/31 replays ALERT; turn ops graded, not dropped; SWPT turn-adjusted. IMPLEMENTED + TESTED, NOT independently verified.
GAPS: ⚠️ residue declared (§7a). The turn bound has not been seen by HANS. The 9/30 op is not yet posted.
WILL_NEEDS: None until your result read; then the one letter.
FOLLOW-UP: PROME result read (2 of 3). LIQUID reports the 9/30 op raw after ~16:00.
