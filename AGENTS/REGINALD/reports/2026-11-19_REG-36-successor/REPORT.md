# REG-36 near-miss exception: reconciled by successor REG-37 (2026-11-19)

**Session:** REGINALD second window 11/19 (13:35 ET), PROME prome-36 task letter, DOCKET row L1211. Claude Code, Opus 5.5.
**Ask:** `inbox/processed/2026-11-19_from-PROME_REG-36-near-miss-exception.md`, items 1 to 6. **Finding:** CATO FV19-5 (`AGENTS/CATO/runs/2026-11-19_1213_forward-view-review.md`, commit 82bd57ffe7). **Canon:** `FORGE/PREDICTION_DISCIPLINE.md` § Grading & re-marking (WQ-161 items 1 to 3, WQ-163 item 3) and § Registration (WQ-142, SL-5).

## Bottom line

CATO is right. REG-36's resolution cell let one kind of clear miss go unscored and could never do the same for a hit. Deleting that clause from REG-36 would change a grade, which the canon does not allow as an edit to a registered row. So I registered a **successor, REG-37**, with the same event, window, series, operator, resolve-by date and 30%, minus that clause. **REG-37 is the version evaluated for calibration; REG-36 is not scored.** REG-36 keeps its original text and 30% byte for byte; only a pointer was appended to its Notes. Retiring REG-36 with the VOID token needs Will's word: a draft is in §6. REG-37 was registered at 13:39:51 ET, before any observation in its window was published (FRED's latest HY observation was 11/18 at 13:38 ET).

## 1. The defect, tested

REG-36 resolution cell (unchanged): "TRUE if any 3 consecutive sessions print > 350. FALSE if none. NO-VERDICT if the only near-run has 2 prints > 350 and the third in [349, 350], or the series is unavailable for more than 5 sessions in the window."

`grade_cases.py` (this folder) implements both letters on synthetic sequences (no market data). Output, run 2026-11-19:

| Case | REG-36 | REG-37 |
|---|---|---|
| A: CATO counterexample 351, 352, 350, rest below 349 | NO-VERDICT | **FALSE** (differs) |
| B: clean run 351, 352, 351 | TRUE | TRUE |
| C: near-run, third print 349 | NO-VERDICT | **FALSE** (differs) |
| D: near-run, third print 348 | FALSE | FALSE |
| E: three ties 350, 350, 350 | FALSE | FALSE |
| F: two near-runs (third prints 350 and 349) | FALSE | FALSE |
| G: near-run, then a full run later | TRUE | TRUE |
| H: missing session inside a possible run (351, missing, 352) | UNDEFINED (letter silent) | **NO-VERDICT** (differs) |
| I: one missing session, no possible run | FALSE | FALSE |
| J: six missing sessions, no run | NO-VERDICT | NO-VERDICT |
| K: six missing sessions and a full run | NO-VERDICT | NO-VERDICT |
| L: all below 349 | FALSE | FALSE |

Two further REG-36 defects the tests show: **case F** (two near-misses resolve FALSE, but one near-miss is unscored, so the worse path is graded and the milder one excused), and **case H** (a missing session inside a possible run is not covered by the letter, which leaves the grader to choose after seeing the data). The near-run reading used is "two prints > 350 followed by a third in [349, 350]"; the letter does not define it further.

## 2. Route under the canon

| Canon clause | What it says (short) | Applied |
|---|---|---|
| WQ-161 ② retrofit test | A repair to a registered row is allowed only if it moves no scored mass; mass-moving repairs are not retrofits however fresh the row | Dropping the clause moves cases A and C from NO-VERDICT to FALSE: they join the scored set. **Mass-moving, so not an edit to REG-36.** PROME's reading checks out at the text |
| WQ-161 ③ written proof | The scored set, the mapping from outcomes to grades, and thresholds must stay unchanged for every case that was already resolvable | Fails by design for A, C (newly scored) and H (newly defined), as listed in §1. That is why REG-37 is a new row with its own Date_Made, not a patch |
| WQ-161 ① | A non-resolution branch carries no probability mass | REG-36's 30% was P(TRUE); the clause only moved cases between FALSE and unscored, so P(TRUE) for the same event is unchanged. 30% carries to REG-37 with no re-mark |
| WQ-142 ① | A NO-VERDICT band is registered at registration, prospective only, never added mid-window | REG-37's NO-VERDICT set (missing data only) is fixed at its registration, before its window had a published observation |
| WQ-163 item 3 | An amended frozen instrument re-runs its construction checks on the final text | Run on REG-37's final text, §4 |
| WQ-112 | Original marks preserved; the latest dated pre-resolution mark scores | No mark changed. REG-36's 30% stays in its row; REG-37's 30% is its own first mark |

**Which version is evaluated (one sentence):** REG-37 is the only version graded for calibration at its 2026-12-14 resolve-by; REG-36 receives no grade and enters no score, so the HY-above-350-by-12/11 event is scored once.

| Field | REG-36 (12:09:55 ET) | REG-37 (13:39:51 ET) |
|---|---|---|
| Event | HY OAS > 350bp on 3 consecutive sessions, FRED observations 11/19 to 12/11 | same |
| Series, basis | FRED BAMLH0A0HYM2, first-published, percent × 100, strict > 350 | same, plus the SL-5 tie convention written out (precision 1bp; a print of exactly 350 does not count) |
| Near-run 2 > 350 then 349 or 350 | NO-VERDICT | **FALSE** |
| Missing session that decides the outcome | not covered | **NO-VERDICT** |
| More than 5 sessions unavailable | NO-VERDICT | NO-VERDICT (kept as registered) |
| Confidence | 30% | 30% (carried, not re-marked) |
| Resolve-by | 2026-12-14 CHOSEN | 2026-12-14 CHOSEN |
| Status | OPEN (VOID awaits Will) | OPEN |

## 3. Was there a reason for the [349, 350] band? (item 3)

I recorded none. `git log -S` finds the band first in commit caa6e31f6f (REG-34, 11/05 14:18 ET); my 11/05 packet to PROME lists "band: third print in [349, 350]" with no rationale; REG-36 copied REG-34's resolution cell this morning. **Inference, not a recovered record:** the band most likely came from the canon's call for an explicit NO-VERDICT band at registration (WQ-142 ①; `finding_prereg_verdict_boundary_must_be_a_number`). It does not hold here, for three reasons:

1. The series is published to 1bp and the letter fixes the first-published value, so there is no measurement ambiguity at 350 to band; SL-5's default tie convention already decides a print of exactly 350 (it does not satisfy strict >).
2. The band sits only on the miss side. A band meant for noise near the line would also hold back a third print of 351; this one can only remove misses.
3. It grades inconsistently (case F).

**Base-rate reproducibility (disclosed, not a re-mark):** REG-36's 15% (2 of 13 from 340 to 350, within 15 sessions) did not reproduce today on FRED's current vintage, 786 observations 11/20/2023 to 11/18/2026, by three counting methods within 15 sessions: every day in [340, 350] 8 of 28 (29%); every entry into the band 5 of 18 (28%); entries from below 340 only 1 of 8 (12%). All overlapping, clustered and small. None is more than 2× from 30%, so the 30% stands under the cold-number check (`finding_corrective_inherits_the_anchor_it_corrects`). The morning's exact counting method is not recorded.

## 4. Construction checks on REG-37's final text (WQ-163 item 3)

| Check | Result |
|---|---|
| Branches reachable | TRUE: in the three-year FRED history, 51 sessions start a run of three prints above 350 (overlapping starts, not independent runs). FALSE: cases A, C, D, E, L. NO-VERDICT: missing data only (H, J, K) |
| Discrimination | Every complete-data sequence resolves TRUE or FALSE; the near-miss band no longer removes misses |
| SL-4 producibility | The series prints whole basis points above 350: 70 of 786 observations were above 350 in the three-year history |
| SL-5 tie set (a) to (d) | Strict >; published precision 0.01 percent = 1bp; the as-published value grades; base rates were counted on the strict operator; no exit leg in this row |
| SL-5 (e) realisation | Exactly 350 printed 3 of 786 observations (1/10/2024, 2/5/2024, 4/1/2025); 349 or 350 printed 5 times; the near-miss pattern (2 above 350 then 349 or 350) printed twice (starts 1/8/2024 and 1/18/2024). The case CATO built is real, not hypothetical |
| SL-5 sustain weighting | The 3-print sustain means a tie in the third position decides the row; it now resolves FALSE |
| Remaining flag, kept as registered | Case K: more than 5 missing sessions makes even a complete run unscored. It removes hits and misses alike (no mass, WQ-161 ①) and the packet put this half outside scope, so it is unchanged |

History figures come from FRED BAMLH0A0HYM2 current vintage, observation_end 2026-11-18, pulled 11/19 13:38 ET for this check only; no market read for the window, no trigger grade.

## 5. Prose updated to name the evaluated version (item 4)

STATUS (Update 11/19 paragraph, HY threshold row, PREDICTIONS open list), CALENDAR prediction-dates row, `reports/2026-11-19_walter-wave2/REPORT.md` §5 (dated note appended under the original "Registered" line, original text unchanged), NEXUS_BRIEF (REG-36 → REG-37 where it names the call). REG-34, REG-T-04 and `registry/THRESHOLDS.tsv` not touched.

## 6. Needs Will (item 5): draft, not done

> ⚖️ **WQ-<PROME assigns> — VOID REG-36 as superseded by REG-37.** Same call (HY above 350 on three straight sessions by 12/11, 30%); REG-37 drops the clause that let a near-miss like 351, 352, 350 go unscored. Recommendation: approve. Effect: REG-36 never enters the calibration score and REG-37 is graded on 12/14. If declined, both rows stay open on one event and REGINALD asks which one is scored; until a ruling, no grade is written to REG-36.

Encode on approval: REG-36 Status → `VOID`, Date_Resolved = ruling date, Outcome "VOID (superseded by REG-37, mis-lettered resolution cell) — no score either way" with the ruling record, as REG-07 was encoded 10/16.

## 7. Same defect, not touched: REG-34

REG-34 (registered 11/05, 25%, window 11/05 to 12/29) carries the identical clause. The packet excludes it, so it is unchanged. Facts for PROME: the clause has not been reached yet (no print above 350 in REG-34's window through 11/18; the high is 348 [11/05], current vintage, 10 observations). A clean successor can only start at an unpublished observation, the 11/19 print, which FRED posts about 08:00 ET 11/20. If PROME or Will want REG-34 handled the same way before then, I can register it on the word; its confidence would be a new forecast (my 11/19 report §5 view of the 12/29 window is about 35%), not REG-34's 25%. Otherwise REG-34 stays as registered and the exception should be named wherever it is cited.

## 8. Not done

No market read beyond the FRED latest-date and history pull above; no trigger grade; no threshold, gate, level, operator or consequence change; no trade, spend or external send. WALTER card SIG-W-20261119-017 logged INFO_ONLY (BOARD_LOG).
