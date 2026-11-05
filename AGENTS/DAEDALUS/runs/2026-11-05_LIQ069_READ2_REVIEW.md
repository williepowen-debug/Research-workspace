# LIQUID Gate 069 L4 line 257 replacement, result read 2 — 2026-11-05

**VERDICT: RELEASE.** The replacement grades correctly at this exact file. One action from the 2026-11-04 packet is not met as written: the new test does not reach the line it was meant to pin. That gap cannot change a grade at this file, so it does not hold the release. LIQUID's hold stays in place until LIQUID removes it; DAEDALUS changed nothing of LIQUID's.

| Field | Value |
|---|---|
| Reviewer | DAEDALUS, claude-opus-5-5, Claude Code. Launched by PROME 2026-11-05 about 09:58 ET |
| Candidate | `AGENTS/LIQUID/scripts/gate069_legs.py` at commit 303bae4a7, SHA256 d4a95a7934251c5547f9699dff5814e39d8106329343523be10b699fb926915c; working tree equal to the commit at review |
| Criteria | `AGENTS/LIQUID/research/2026-11-04_credit-followthrough/ACCEPTANCE.md`; letter KB-LIQ-069; `AGENTS/LIQUID/inbox/processed/2026-11-04_from-DAEDALUS_069-boundary-result-WITHHELD.md` |
| Episode reads | **Read 2 of the episode.** Read 1 was `runs/2026-11-04_LIQ069_RESULT_REVIEW.md`. No third read started. ACCEPTANCE.md's own `reads:` line still says 0; LIQUID owns that line |
| Method | Scratch copies with bytecode writing off. Reproduction: `runs/2026-11-05_LIQ069_READ2_REPRO.py`, run from repo root with `.venv/bin/python -B` |

## Result on the two questions PROME set

| Question | Answer | Evidence |
|---|---|---|
| Do half-cent closes survive? | **Yes.** | 3,311 live closes, full history of all four names, pulled 2026-11-05 10:01 ET: `vendor_close` equals an independent decimal on all 3,311 (0 mismatches). Every four-decimal value from $0.0001 to $1,023.9999, 10,239,999 values, stored as float32, comes back exact (0 bad) |
| Can storage noise change a grade? | **No, below $1,024.** | 1,227,600 near-line cases against an integer oracle that shares no code with the candidate: every half-cent prior from $1.00 to $1,023.995, closes at the line and three half-cents either side, float32 storage on both dates, rotated across the four names, HY +5: 0 wrong. All 10,230 exact ties FIRED at HY +5 and NOT FIRED at HY +4. Without noise removal, 4,919 of those ties would misgrade, so the sweep can fail |

## Live vendor dtype: exercised, hold not released

`yf.download` with `main()`'s exact arguments, yfinance 1.2.0, pandas 3.0.2. The column dtype is **float64, not float32**, and the values carry float32 noise (CRWV 62.130001068115234). The selftest builds float32 columns. Both forms reach the same Python float, so the test form is equivalent, and I also ran the live form directly.

`main()` ran end to end on a scratch copy with only the five hold lines removed, live vendor and live FRED, 2026-11-05 10:03 ET: rc 0. This is the first live run of that path on this candidate. It was a run-the-path check on a scratch copy, not an operational grade.

**Real file re-checked after all tests, 2026-11-05 10:07 ET:** CLI exit 4, selftest PASS under `.venv/bin/python`, SHA256 unchanged, no LIQUID script or inbox path dirty.

## Counterexamples of my own

The two 2026-11-04 cases placed the half-cent on the prior close only. These add the close side and exact ties, all through `main()` on the live float64 form with stubbed sources.

| Case | Exact move | Correct | Candidate | Literal old line |
|---|---:|---|---|---|
| CRWV 54.235 → 46.10, HY +5 (read 1) | −14.99954% | NOT FIRED | NOT FIRED | **FIRED, wrong** |
| NBIS 237.355 → 201.75, HY +5 (read 1) | −15.00074% | FIRED | FIRED | **NOT FIRED, wrong** |
| APLD 54.30 → 46.155, HY +5, half-cent close at an exact tie | −15.00000% | FIRED | FIRED | FIRED |
| Same, HY +4 | −15.00000% | NOT FIRED | NOT FIRED | NOT FIRED |
| APLD 54.30 → 46.16, HY +5 | −14.99079% | NOT FIRED | NOT FIRED | NOT FIRED |
| APLD 20.16 → 17.135, HY +5, close-side half-cent through the line | −15.00496% | FIRED | FIRED | **NOT FIRED, wrong** |

The third wrong row is new: a false miss from a half-cent on the close side. On the near-line grid from $1 to $300, the old two-decimal read was wrong on 42,552 of 358,800 cases, which sizes the repair.

## Finding: the "CLI path" test does not reach the CLI line

Restoring the literal old line at the `main()` call site leaves **selftest PASS, rc 0** (LEG 1 of the reproduction), while `main()` then grades three of the six cases above wrongly. Replacing the call with `float(v)` also leaves PASS.

| Mutant, on a scratch copy | Selftest |
|---|---|
| Literal old line at the `main()` call site | **PASS, not caught** |
| No rounding at the `main()` call site | **PASS, not caught** |
| `vendor_close` to 2dp | FAIL, 3 checks: LIQUID's three, reproduced exactly |
| `vendor_close` to 3dp | PASS (no real close in 3,311 has 4 decimals) |
| `vendor_close` to 5dp | **PASS, not caught** (leaves noise that flips 534 of 1,720 ties from $128 to $300) |
| `vendor_close` to 6dp | FAIL, 1 check |
| `vendor_close` with no rounding | FAIL, 1 check |
| `dropna` removed from `vendor_closes` | PASS, not caught |

LIQUID's report of "copy with 2dp restored fails 3 checks" is accurate for a copy that changes the helper. ACTION 5 asked for a copy of line 257 itself, and that copy passes. The checks named "CLI path" exercise `vendor_closes()` then `grade_l4()`; they never run `main()`. This is the 2026-11-04 finding ("the line has no test") in a smaller form: the rounding logic is now tested, but the one line that wires it in is not.

**Why this does not block:** I read the call site, then ran it end to end at this file. It is correct here, on stubbed and live paths. The gap is a missing regression guard, so it could only matter after a later edit. `PROME/CLAUDE.md` § Review budget withholds by consequence, not defect class, and this gap cannot change a grade at this file.

## Acceptance conditions

| Condition | Verdict |
|---|---|
| 1 Decimal interpretation, exact comparison | PASS at the CLI input and in `grade_l4` |
| 2 Boundary cases, no tolerance widening | PASS on every value the vendor has produced. Limits below |
| 3 Any one name; missing data, dates, first-published basis, L1 unchanged | PASS: the `grade_l4` diff is a comment; L1 and fault tests unchanged and passing; sweep rotated across all four names |
| 4 Reconciliation | PASS. Own re-grade below |
| 5 and addendum, operational withholding | PASS: CLI exit 4 |

## 2026-11-04 actions

| Action | Result |
|---|---|
| 1 Keep hold | Done |
| 2 Decide the non-cent treatment | Done, option (a) |
| 3 Record in KB-LIQ-069 | Done. The row is append-only: first difference at the old row's end, character 19,298, letter text unchanged |
| 4 Replace line, add CLI-path test | Line replaced. Test reaches the helper, not the line. **PARTIAL** |
| 5 Test against a copy of line 257 | **NOT MET as written**: the literal line passes |
| 6 Correct the count, disclose six closes | Done: 42 NYSE sessions from 2026-09-04 is right, 44 from 2026-09-02 is right, six closes match |
| 7 Request one read | Done |

## Reconciliation, own re-grade

LIQUID's `reconcile.py` feeds its oracle the same `vendor_close` values as the candidate, so that oracle cannot disagree with the read path. This repeats the limit noted at read 1. I re-graded with decimals taken from the shortest float32 round-trip of `raw_closes.json`, without `vendor_close`, and an exact fraction comparison.

| Item, `raw_closes.json` and `BAMLH0A0HYM2.json`, LIQUID retrieval 2026-11-05 | Result |
|---|---|
| Closes through 2026-11-04 | 184, 6 non-cent; `vendor_close` differs from the independent decimal on 0 |
| NYSE sessions 2026-09-02 to 2026-11-03 | 44, disagreements 0 |
| Fires | 1: 2026-10-14, HY +9bp |
| Closest name move to the −15% line | CRWV −15.461%, 2026-10-14 |

## Limits, tested rather than assumed

1. **$1,024 ceiling.** The docstring's bound is correct and sharp. From $1,024 to $2,048, 32,768 of 204,800 half-cents do not survive, and 674 of 10,240 exact ties misgrade. Highest cohort close in full history: NBIS $286.69. Nothing in the code fails closed above the bound. No action proposed: the docstring states it and a guard would be a new check for an unreached case.
2. **Fifth decimal.** `vendor_close(2.040000000001)` and `vendor_close(2.04004)` both return 2.04, so through the CLI path such a value meets the line where `grade_l4` alone would not. Any noise removal has a quantum, here 0.00005. The domain claim holds on the evidence: 0 of 3,311 live closes carry more than three decimals, and the first of those two values cannot exist in float32. If the vendor ever published five decimals, this would be a tolerance.
3. **Single vendor.** Whether a Yahoo half-cent matches any official exchange close remains unchecked, as at read 1.

## Residue, non-blocking

1. `import pandas` in `selftest()` means bare `python3 gate069_legs.py --selftest` on this box stops with `ModuleNotFoundError`, rc 1, before the SELFTEST line. It fails loud. The header still calls the selftest offline, and `.venv/bin/python` works.
2. `main()` prints closes at two decimals under the label "raw close" and moves at two decimals. A half-cent close prints altered (46.155 as 46.16), and the CRWV case prints "−15.00%" beside "<=-15%? NO". The grade is right; a reader of the line will think otherwise.
3. Test gaps by mutant: the 5dp and `dropna` rows above. A stored tie such as 128.40 → 109.14 kills the 5dp mutant.

## Question before Will, consequence only

WQ-603 owns whether the letter's "2dp" is descriptive. DAEDALUS does not decide it. If Will rules B, four things follow:
- This RELEASE no longer covers the read path. WQ-603's row says this read does not depend on the ruling: true of the verdict at this file under reading A, not of its coverage under B.
- The "Correct" column above stops being settled for half-cent rows. The answer then depends on a half-cent rule the letter does not have.
- "LIQUID restores that" cannot mean restoring line 257 as it stood. That line let storage noise pick the direction: 54.235 up, 237.355 down, 44.125 to even. It would need the stated rule from option (b), then a fresh read.
- Historical grades do not change under either reading: 0 of 44 sessions differ, closest approach CRWV −15.461%.

Removing the hold before the ruling means a near-line session with a half-cent close would be graded on LIQUID's reading.

## Review limits

Reviewed the replacement, the test, the L4 and L1 read paths and the evidence named above, not the wider LIQUID desk or other Gate 069 legs. FRED was exercised live once and otherwise stubbed. Desk boot: gate rc 0, B1 DUE on two known clocks (Harness Audit, profile-refresh queue). Eight other inbox packets are pending and unread, outside this task's scope. Boot reads: root CLAUDE.md 5 pages, AGENTS.md 1, USER.md 2, charter 4, COMPLETION_SPEC 4, all to `eof: true`; OPERATIONS.md 4 pages to `eof: true`.

Candidate design lesson, not logged to PATTERNS in this bounded session: a test named for a path can reach the helper and stop short of the wiring, and the mutant that proves the test bites can be chosen, unknowingly, to sit inside what the test reaches.
