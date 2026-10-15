# CHG-RED-051 — registry apparatus review (S52, Wed 2026-10-14 22:13–22:27 ET [stamp corrected at closeout: it was typed from narrative, not the clock; true time from the commit log], on Will's word: "go ahead with #9")

**Why today, not 10/31:** CHG-051's own Resolution cell says it *"Resolves 2026-10-31 **or at the first fire of any registry row**, whichever is sooner."* FT-08 and FT-10 both fired today, so the review is **due today by its own letter**. Boot's DUE-scan listed it as "re-review 10/31", because it reads the date column and not the event clause in the prose. That is finding **N1** below.

**Scope:** CHG-051's charges A/B/C and open falsifier F4; the 8/28 owed full-registry amendment audit; and everything queued for this review (FT-08's 0.4 note, FT-02 vintage pin, the METRIC_MAP check, base-rate 🔴 rows, FT-08 selectivity). **No threshold is changed in this file.** Spec changes are PROPOSALS for Will (§4). The changes applied today are display/record-only and direction-neutral (§5).

---

## 1. The original charges — where they stand

| Charge | 8/27 | Today | Verdict |
|---|---|---|---|
| **A** — no correctness axis | 0 outcome grades ever | `OUTCOME_SPEC.tsv` (pre-committed proxy and horizon, 12 rows) and `TRIGGER_OUTCOMES.tsv`: **13 rows, 10 graded**. Today's two fires got PENDING rows with specs committed before the fire. | **RESOLVED by fix, in use** |
| **B** — base rates never recomputed | computed once | boot 9d `base_rate_review.py` runs every boot. **Today it flagged 🔴 FT-02 and FT-06** (§2), which shows it working. | **RESOLVED by fix, in use** (the two flagged rows are handled in §2/§4) |
| **C** — FT-01 is labelled falsify and fires ~constantly | label ambiguous | Adjudicated 8/27 to `SUSTAINED-CALM-COUNTER-SIGNAL`; falsify power moved to FT-12 (HY <260 s=3). | **RESOLVED 8/27** |
| **F4** — does a pre-committed scorer separate FT-01 from chance at n ≥ 12? | open | **FT-01 outcomes: 4 CORRECT / 4 WRONG of 8 graded** (the 9th resolves ~10/29). Even if the next four are all CORRECT, 8/12 gives one-sided binomial **p = 794/4096 = 0.194**. Separation at α = .05 needs ≥ 10/12, which is now **unreachable**. | **F4 FAILED (foreclosed).** C's coin-flip line **stands**: FT-01 is indistinguishable from chance on its own committed spec. This goes to proposal P4. |

**CHG-051 → RESOLVED.** Its three charges are fixed and in use, and F4 failed. *(This line originally said a successor CHG-053 would carry §4. It was not needed: Will approved all six proposals in-session and they were applied the same night, see §6.)*

## 2. Base-rate 🔴 rows (boot 9d, run 10/14)

| Row | Recorded | Last 120 | Last 60 | Read |
|---|:-:|:-:|:-:|---|
| **FT-02** HY >320 s=3 (bear confirm) | 2.5% | **0.0%** | 0.0% | It has become **rarer**, i.e. more selective, not stale toward descriptor. The line has not been met in 120 sessions, and its max run is 1 (324 on 10/1). **No re-cut.** The recorded cell is refreshed (§5). |
| **FT-06** VIX <16 s=5 (bull managed-decline confirm, **BANKED**) | 5.8% | **15.0%** | **30.0%** | **2.6×: drifting toward a regime descriptor**, the path FT-01 and FT-07 took. Its fire (8/11) graded CORRECT on 10/1. The risk is in a **re-fire** after an exit: at 15–30% it should not re-earn a ±2. → **P6.** |

## 3. New findings

| # | Finding | Evidence | Disposition |
|---|---|---|---|
| **N1** | **An event-keyed resolution clause is invisible to the date-keyed DUE-scan.** CHG-051 was due today ("or at the first fire") while boot showed 10/31. | the CHG-051 Resolution cell vs boot.py §4, which reads `Resolved_Date` only | **Fixed today (display):** boot §4 now flags non-terminal rows whose Resolution text carries an event clause. |
| **N2** | **Holiday bars are counted as sessions by the FRED sustain counters.** FRED's ICE BofA series and VIXCLS carry bars on market holidays: HY 2.68 [9/4] = 2.68 [9/7, Labor Day]; HY 3.11 [10/9] = 3.11 [10/12, Columbus Day, SIFMA full close]; CCC 8.88 [2025-11-10] = 8.88 [11-11, Veterans Day]; VIXCLS 15.30 on 9/7 with NYSE closed. boot.py skips holidays **for the Cboe SKEW counter only** (S41 ruling, which was explicitly "not unilaterally applied to other rows"). | FRED pulls 10/14 | **Near-term false-fire risk on FT-02:** an HY close >320 on Tue 11/10 plus the Veterans Day forward-fill on Wed 11/11 would count **two** of FT-02's three observations from one session. → **P1.** |
| **N3** | **METRIC_MAP ↔ instrument_basis (DAEDALUS prose-remedy, ML-226):** 10 of 11 mapped rows match their declared basis. **BRENT-PAPER (FT-03/04) is evaluated off yfinance BZ=F**, which their own `instrument_basis_operative` declares *"PROVISIONAL and cannot complete a sustain count,"* and the boot output does not say so. | boot.py `METRIC_MAP` vs registry col 18 | **Fixed today (display):** BRENT-PAPER readings are labelled PROVISIONAL. Not binding now: 24 / 31 from the lines. |
| **N4** | **The 8/28 owed full-registry amendment audit (FT-02/03/04/05/09/10/12) never ran in its 9/4–9/11 window.** No ML, CHANGELOG or MAINTENANCE record. | grep, 10/14 | **Run today → CLEAN.** A git trace of every registry version shows **zero entry-condition amendments on any of the 7 rows since registration**. Only exit legs were added (7/29 placeholders, defined 8/12). So no amended text inherited an old base-rate certificate. The 9/4 slip is itself an instance of `[[finding_dated_carry_item_has_no_expiry_check]]`: an owed-forward item with a window and no DUE row. |
| **N5** | **Exit legs were never base-rated.** | `base_rate_review.py --candidate`, 10/14 | **FT-06 exit** VIX ≥18 s=5: last-120 1.7% (selective, fine). **FT-07 exit** CCC <930 s=3: 5.8% (fine). **FT-02 exit** HY <300 s=3: **90% unconditional** (a descriptor), **but conditionally**, over the 3 FT-02 fires in FRED's ~3-year ICE window, the time to exit was **18 / 67 / 255 obs (median 67)**. Not a hair trigger, so no change; the figures are recorded on the rows. |
| **N6** | **FT-08's magnitude is not scaled to its selectivity.** ≥3.0 s=1 held in **40% of months since 2025** (61% since 2023; index-rounded approximation of Table A, which matches the S50 tree's Table A count of 8/19) and carries **+3**, while FT-10 at **0.8%** carries **+2**. Candidates since 2025: ≥3.0 s=2 **20%** · ≥3.5 s=1 **10%** · ≥3.0 with newest MoM ≥0.3 **25%**. Its exit (<2.5) is also **40%**. | FRED CPILFESL, 10/14 | **Today's fire STANDS at +3** (applied on its letter; never undone after the fact). → **P3**, future fires only. |
| **N7** | **FT-08's S29d 0.4 note** gave the opposite instruction to the S50 tree for the 0.3 case (ruled at fire, ML-280). | registry `exit_source` | → **P2.** |
| **N8** | **FT-02 names an observation date but no vintage** (S51). | registry | → **P5.** |

## 4. Proposals for Will (spec changes; none applied without his word)

| # | Proposal | Direction | RED recommends |
|---|---|---|---|
| **P1** | **Registry-wide non-session clause:** a FRED bar dated on a market holiday is a **non-session**. It is excluded from the count domain and the run **bridges** it. This is the FT-10 S41 ruling, applied to the ICE OAS rows (FT-01/02/07/12, WL-03..06) and VIXCLS (FT-06). Calendar: NYSE holidays for VIXCLS; NYSE holidays **plus SIFMA full-close days (Columbus, Veterans)** for ICE. Implemented in boot.py with a test. | **neutral** (cuts both ways by row) | **Approve.** It closes a live FT-02 false-fire path before 11/11. |
| **P2** | **Retire FT-08's S29d 0.4 note.** The S50 Table A ruling governs. The note's roll-off question is kept as a methodology check, *"does the fire need the new print?"*, and is never a grade. | neutral (resolves a conflict) | **Approve** |
| **P3** | **FT-08 future fires** (after the current fire exits): **(a)** cut the magnitude **+3 → +1**, keeping the 3.0 line's economic meaning (core above target), with the weight scaled to a descriptor-grade instrument; **(b)** raise the line to **≥3.5 s=1** (10% of 2025+ months) and keep +3; **(c)** leave it and revisit at exit. | (a)/(b) are **bull-direction for future fires** (fewer or smaller bear moves); labelled | **(a)** |
| **P4** | **FT-01 → log-only** (weight action 0) on future fires and exits. Its committed outcome record is 4/8, and F4 is foreclosed. Falsify power already sits with FT-12. | neutral over a round trip; at any moment it removes a future bull −2 *and* the matching exit +2 | **Approve** |
| **P5** | **FT-02 vintage pin:** the **first-published** value as read at T+1 governs the count; the latest-revised value is recorded beside it; a later revision neither fires nor un-fires retroactively. | neutral | **Approve** |
| **P6** | **FT-06 re-arm guard:** if FT-06 exits (VIX ≥18 s=5), it does **not** re-arm at ±2 without a re-spec. Its base rate is now 15–30%. | bear-direction for future fires (removes a future bull +2) | **Approve** |

## 5. Applied today (display/record only, direction-neutral)

- boot.py: **N1** event-clause flag in §4; **N3** PROVISIONAL label on BRENT-PAPER rows.
- Registry: FT-02 and FT-06 `rolling_base_rate` cells refreshed with dated measurements. The exit base rates (N5) are recorded in `state_detail`.
- CHG-051 → RESOLVED; CHG-053 opened for §4; ML rows.

Sources: `registry/FALSIFICATION_TRIGGERS.tsv` and its git history (13 commits traced); `registry/TRIGGER_OUTCOMES.tsv`; `scripts/base_rate_review.py` (run, and `--candidate` ×3, 10/14); FRED BAMLH0A0HYM2, BAMLH0A3HYC, VIXCLS (holiday windows 2025-11-07..13, 2026-09-03..09, 2026-10-09..13); FRED CPILFESL (2022-09 →); `challenges/2026-08-28_amendment_inherits_cert_audit.md`; CHG-RED-051.


## 6. Will's rulings (in-session, 2026-10-14 ~22:20 ET, AskUserQuestion) [stamp corrected at closeout: it was typed from narrative, not the clock; true time from the commit log] — and what was applied

| # | Ruling | Applied |
|---|---|---|
| P1 | **Approved** | `scripts/nonsession.py` (one calendar; the NYSE function moved verbatim from boot.py, body-identical by check); boot.py `live_value`/`fred_trail` filter + fetch limit 6→10; `base_rate_review.py` filter; `scripts/test_nonsession.py` **13/13 PASS**; the existing `test_tie_atoms` and `test_base_rate_flag` still pass; registry clause on FT-01/02/06/07/12. Verified live: WL-03 trail now reads **316 / 311 / 315** (it was 316 / 311 / 311, with the Columbus Day forward-fill counted). Base rates re-run against the amended count **before** commit (ML-203 standing rule): no row crossed a flag boundary; FT-06 2.6× → 2.4×. |
| P2 | **Approved** | FT-08 `exit_source`: the 0.4 note replaced by a retirement pointer; verbatim text in Appendix A. |
| P3 | **(a) cut to +1 approved** | FT-08 `action_magnitude`: future fires STAG +1 / MANAGED −1. The current 10/14 fire stays +3, and its exit reverses exactly what was executed. |
| P4 | **Log-only approved** | FT-01 `action_magnitude`: future fires and exits move no weight; they are still recorded and outcome-graded. |
| P5 | **Approved** | FT-02 basis: the first-published value at T+1 governs. |
| P6 | **Approved** | FT-06 `action_magnitude`: no re-arm at ±2 after an exit without a re-spec. |

**Also fixed tonight, found during the review:**
- boot.py's outcome DUE-scan keyed on the token `UNRESOLVED`. **S52 itself had filed the FT-08/FT-10 outcome rows as `PENDING`** (outside the schema), which would have hidden them at their horizons, the ML-273 status-token class. The scan now keys on a blank `graded_date`, and both rows are normalized to schema values.
- N1 (event-clause flag) and N3 (PROVISIONAL label) are live in boot.py.

## Appendix A — FT-08's retired 0.4 note, VERBATIM (from `exit_source`, S29d 2026-08-12)

> MoM >= 0.4pct is RETAINED as a human-side confirmation note, NOT as a machine leg: grade the 3-mo line; if it fires while MoM is <0.4 the move is a base-effect roll-off rather than a fresh impulse, which is a NO-VERDICT worth looking at, not an automatic fire.
