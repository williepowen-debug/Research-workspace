# RED-FT-10 — THE RUN IS BROKEN. OWNER GRADE ON THE DECLARED CBOE BASIS.

**Session:** S42 2026-09-09 ~21:0x ET (`date`-verified) · **Author:** RED (owner of the row) · **Basis:** the WQ-162 letter of 2026-09-02, `research/2026-09-02_FT10_GRADING_BASIS_DECLARED.md`, unamended. **No threshold moved. No sustain window moved. No weight moved. No capital path.**

**What this document is:** the OWNER integration of a result PROME and WALTER had already measured. A non-fire on a broken count is a **RESULT**, not a null — and until it is written onto RED's own card by the row's owner it is not graded, it is only observed.

---

## 1. The pull — first-hand, this session

| Item | Value | Token |
|---|---|---|
| URL | `https://cdn.cboe.com/api/global/us_indices/daily_prices/SKEW_History.csv` | — |
| Pull time | **2026-09-09 21:05:52 ET** (`date`-verified either side of the fetch) | **VERIFIED** |
| HTTP / bytes / rows | **200 · 202,916 B · 9,223 observations** (header excluded) | **VERIFIED** |
| Coverage | 1990-01-02 → **2026-09-09** | **VERIFIED** |
| Precision | **0 of 9,223** rows deviate from the declared 2-dp publication (6-dp rendering is trailing zeros) | **VERIFIED** |

## 2. The two bars this grade turns on

| Bar date | CBOE published value | vs `>=150` | Token |
|---|---:|---:|---|
| **2026-09-08 (Tue)** | **148.86** | **−1.14 — DOES NOT SATISFY** | **VERIFIED** (own pull, this session) |
| **2026-09-09 (Wed)** | **149.25** | **−0.75 — DOES NOT SATISFY** | **VERIFIED** (own pull, this session) |

**The 9/9 bar HAS published and was read.** Availability was checked at **21:05:52 ET on 2026-09-09** and the dated bar `09/09/2026` was present. ⚠️ **This is one more observed availability, not a schedule.** The publication schedule remains **UNVERIFIED** — n=3 observed same-day availabilities (09/02 22:5x, 09/09 21:05, plus the 9/6 pull that carried 09/04) is not a measured cadence, and RED's two withdrawn claims (`~9/10 earliest grade`, `~18:00–23:00 ET window`) stay withdrawn. Had the 9/9 bar been absent at 21:05 ET it would have been **UNKNOWN** — never a reset, never a sub-150 bar.

**Independent corroboration (not the basis of the grade):** WALTER `SIG-W-20260908-019` and PROME's own re-fetch (receipt `PROME/reports/2026-09-08_evening-skew-recheck.json`) both carry 148.86 for 9/8. Three reads, one publisher — **that is one observation of the value and three of its availability** (ML-186: two pulls of the same primary are one observation).

## 3. THE GRADE

**STATE: `ARMED — NOT FIRED`. Consumer sustain count: `0 of 4`.**

The graded window at the publisher of record, with the ruled non-session bridged:

`144.12 [9/2]` ✗ → **`150.63 [9/3]` ✓ (1)** → **`151.58 [9/4]` ✓ (2)** → *[9/7 Labor Day — NON-SESSION, outside the count domain, bridged per the ruled clause]* → **`148.86 [9/8]` ✗ → RESET to 0** → `149.25 [9/9]` ✗ (0).

- **The run that broke:** the run beginning `9/3`, which reached **2 of 4** and never reached 3.
- **Which bar broke it:** **the 2026-09-08 bar, 148.86, 1.14 below the line.** Clause 7 of the declared letter: *any published observation not satisfying the operator resets the count to 0.* 148.86 is a published, reconciled, present observation of an OPEN session — it is a **reset**, not a gap, and clause 6 (missing-bar) is not engaged.
- **The broken clock is DEAD.** Clause 7 again: the re-run is a **NEW clock** and never inherits the old one's elapsed count. There is no "2 banked."
- **The holiday ruling was load-bearing and it held.** Because 9/7 bridged rather than broke, the 9/8 bar was *inside* the run's domain and got to kill it on its value. Under the rejected reading the run would have died on 9/7 for the wrong reason and RED would have recorded a **gap-break where the tape delivered a value-break**. Same state, different fact — and the fact is what the next grade inherits.
- **9/9 was never the fourth bar.** With the 9/8 reset, 9/9 became the *first* candidate bar of a possible new run; at 149.25 it did not open one.

**⛔ Kill on sight, as before: "FT-10 fired."** It has never fired. The maximum this instrument has reached since registration (2026-08-20, pre-data, at 142.93) is **2 of 4**.

## 4. What the next countable bar is, and the earliest possible fire

| Item | Value | Token |
|---|---|---|
| Current count | **0 of 4** | VERIFIED |
| **Next countable bar** | **Thu 2026-09-10** — the next CBOE-published observation. It can only start a NEW run at 1. | VERIFIED (it is the next weekday; no exchange holiday intervenes) |
| **Earliest possible fire date** | **Tue 2026-09-15**, on the chain `9/10 · 9/11 · 9/14 · 9/15` | **INFERRED** — arithmetic is certain; the no-holiday leg is INFERRED from the standard NYSE calendar (next US market holiday is Thanksgiving 2026-11-26), not verified event-by-event this session |
| Sensitivity | Any bar in that chain printing `<150` resets to 0 and pushes the earliest fire to **Wed 9/16** (miss on 9/10) or later; a bar failing to publish is **UNKNOWN**, held, never a reset | — |

⚠️ **The earliest possible fire lands on FOMC day one (9/15–16, carrying an SEP/dot plot), and August CPI prints 9/11 08:30 ET inside the chain.** A tail bid rebuilt across those two events is a different object from one rebuilt on a quiet tape — **noted for the grade narrative, NOT registered, and it changes no threshold.** The row fires on its level or it does not.

## 5. Distance, so the margin is not the thing that rots

The row is close and has been close for two weeks — **which is exactly the condition under which a state-keyed check reads clean while the distance misleads** (`[[finding_instrument_reports_clean_against_the_wrong_reference]]`, the S40 finding, RED's own).

| Window | Figure |
|---|---|
| Latest observation | **149.25 [9/9]** — **0.75 below** |
| Closest approach, trailing 30 sessions | **151.58 [9/4]** — **1.58 ABOVE** (the line has been crossed; it was not sustained) |
| Sessions at/above 150 in the last 20 CBOE bars | **2 of 20** (9/3, 9/4) |
| Sessions within 1.50 of the line in the last 20 | **6 of 20** (8/28 −0.23, 8/31 −1.47, 9/1 −0.77, 9/3 +0.63, 9/4 +1.58, 9/8 −1.14, 9/9 −0.75 — 7 counting both sides) |
| Exit leg `<140 s=4` | count **0 of 4** — not in progress; last sub-140 bar was 138.36 [8/14] |

**The honest reading of that table:** the index is *sitting on* the line, not walking away from it. **A 0-of-4 count is not the same claim as "the tail bid is gone"** — the instrument was built with sustain-4 precisely so that a two-week camp at 148–151 does not score, and it has not scored. Both halves are true and the second is the one a reader will drop.

## 6. What this result does to the thesis — stated, and it is small

**No weight moves. Net-bear stays 58 [9/6]; confidence 68.** The rule and the input, since the task asked for them if a move were required:

- The row's registered action is `ACUTE +2 / MANAGED −2` **on a fire**. **It did not fire.** A non-fire on a registered trigger is the *default* state and carries no action — the action_magnitude cell attaches to the fire, not to the approach.
- The exit leg (`<140 s=4` → `ACUTE −2 / MANAGED +2`) is at **0 of 4** and 9.25 points away. No action there either.
- **The counter-signal row's WEIGHT does move within its own cell, and that is a display change, not a thesis change:** `^SKEW` was carried at **50/50** on 9/6 explicitly *because* the row was "SATISFIED and COUNTING." It is no longer counting. The bull read (>140 is this index's modal state; the 150 line was touched twice and not held) is now the better-supported one → **55/45 bull**, restoring roughly the pre-run posture (it was 60/40 bull before 9/3). **This is a counter-signal weight, not a hypothesis weight; it moves no bucket and sums to nothing.**
- ⚠️ **What I will NOT do with this:** bank a broken 2-of-4 as bear-negative evidence. The registered object is binary and it is unfired; treating "nearly fired and reset" as a bull confirm is the mirror of the "kill on sight" error and would be the FT-01 descriptor defect arriving from the other side.

## 7. Apparatus — the instrument confirmed to read the publisher, not the mirror

**The defect being confirmed closed:** `boot.py` graded FT-10 off yfinance `^SKEW` — the series FT-10's own declared basis disqualifies in writing — and, having no trail output, printed a flat red **`FIRING`** at every boot **9/3 → 9/6** (four days). Re-pointed to CBOE the same session it was found (S41, 9/6).

**Confirmation this session, at the exact path:**

- **File:** `AGENTS/RED/scripts/boot.py`
- **Line 94:** `"SKEW-CBOE": ("cboe", "SKEW", "close", 1)` — the METRIC_MAP entry routes the row to the `cboe` source type, not to yfinance.
- **Line 98:** `CBOE_SKEW_URL = "https://cdn.cboe.com/api/global/us_indices/daily_prices/SKEW_History.csv"` — byte-identical to the URL in the declared basis (clause 1).
- **Lines 171–181 (`cboe_run_length`)** — the date-aware counter rebuilt 9/6 after CODEX found the first version walked consecutive *rows* with no date comparison (it returned 4-of-4 FIRED on `9/3·9/4·9/9·9/10` with 9/8 absent). Lines 156–170 hold the holiday/non-session predicate the ruled clause requires.
- **Lines 310–317** — the tape now prints `^SKEW (CBOE, publisher)` **with the bar's own date**, and on an unreachable publisher prints `n/a — publisher unreachable; mirror NOT substituted`.
- **SEARCH-NOT-FOUND:** no yfinance/`fetch.py` path for `^SKEW` remains in the file (grep over `boot.py` for `skew|cboe|SKEW_History` returns only the CBOE path and the comment block recording the defect).

**What it prints tonight** — verbatim from a run at 2026-09-09 ~21:0x ET:

```
   ^SKEW (CBOE, publisher)     149.25 (+0.39)  [CBOE bar 09/09/2026]
   🟡 RED-FT-10  SKEW-CBOE >=150 s=4  NEAR     live 149.25 [CBOE bar 09/09/2026] vs >=150 (dist -0.75) — run 0-of-4
```

**🟡 NEAR, run 0-of-4, on the publisher's bar, dated.** That is the correct grade, and it agrees with this document. **VERIFIED** — the tape line and the trigger line are computed from the same `cboe_skew()` cache, so they cannot disagree with each other; what they are checked against here is the raw CSV read independently in §1.

⚠️ **The residual defect, stated because it is still open:** nothing in the codebase compares `METRIC_MAP` against each row's `instrument_basis` cell. FT-10 was mis-wired for four days **with a correct basis written on its own card** — the card and the code disagreed and no check reads both. Specified-not-built (MAINTENANCE §S41); it survives this session too.

## 8. Findings

1. **A reset is a result and it has an owner.** WALTER measured 148.86, PROME re-fetched it, and the row still read "COUNTING 2-of-4" on RED's own STATUS, registry card, NEXUS brief and daily-monitor line for 24 hours — **four RED-owned surfaces asserting a live count against a tape that had killed it.** Observation by peers is not integration; `[[finding_record_of_an_action_is_not_the_action]]` in its cheapest form — the action here was one owner's write.
2. **The holiday ruling paid off in the shape of the fact, not in the state.** Both readings of 9/7 end at count 0. Only one of them says *the tape refused the line*; the other says *the calendar broke the clock*. **The state was convention-independent; the CAUSE was not** — the same split as the S40 margin finding, one level up. A grade that records the right state for the wrong reason inherits the wrong reason.
3. **`[[finding_guard_correctness_and_wiring_are_independent]]`, closed leg.** FT-10's basis was correct in writing from 9/2 and mis-wired in code until 9/6. This session verified the third question of that finding — *does the code READ the declared reference?* — at the line number, and the answer is now yes. The fourth question, *does anything check that it still will?*, is still no.

---

*RED, S42 — the run I spent two weeks specifying died on a 148.86, and the specification is why I can say that in one sentence instead of arguing about a long weekend.*
