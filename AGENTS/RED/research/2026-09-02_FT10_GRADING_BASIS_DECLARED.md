# RED-FT-10 — GRADING BASIS DECLARED, and the row re-graded on it

**Session:** S40 2026-09-02 ~22:5x ET (`date`-verified) · **Authority:** WQ-162 RULED 2026-09-02 21:29 (Will verbatim *"Approve WQ-162 with your recs"*) — *a grade on an unnamed basis is NO-VERDICT, never a verdict*; canon `FORGE/PREDICTION_DISCIPLINE.md` § Registration.
**Trigger for this pass:** VIOLET `495437ace` (the 8/28 `^SKEW` bar is absent from the yfinance history the row graded on) + CREED `9dce322ba` (a strict inequality against a fixed-precision series has a non-empty tie set, and canon does not require the tie convention to be declared).
**Scope fence:** this declares the BASIS and re-grades on it. **No threshold moved. No sustain window moved. No weight moved. No capital path.** The level (150 / 140) and the sustain (4) are exactly as registered pre-data 2026-08-20.

---

## 1. What was wrong with the old basis — stated as a defect, not as a data note

The pre-WQ-162 letter named the series (**Yahoo `^SKEW` daily bar**) and the operator (**≥150, sustain 4**) and one convention (*"THE BAR OWN DATE governs the sustain count"*). Against WQ-162's six-item checklist it was **silent on four**:

| WQ-162 item | Old letter | Status |
|---|---|---|
| series | Yahoo `^SKEW` daily bar | named — **but not the publisher of record** |
| unit + conversion | — | **UNNAMED** |
| vintage convention (as first published) | — | **UNNAMED** |
| operator / boundary | `>=150` / `<140` | named — **tie convention UNNAMED** |
| consecutiveness | "the bar's own date governs" | **a claim about LAG, silent about ABSENCE** (VIOLET §3) |
| reset | — | **UNNAMED** (carried only as an FT-06 precedent in MEMORY) |

⇒ **Under WQ-162 as ruled, any grade read off the old letter is NO-VERDICT, not a verdict.** That includes RED's own published margin *"0.77 below the line"*, which is **withdrawn** below.

**And the silence was load-bearing, not cosmetic.** VIOLET's §5 shows the omitted bar decided the grade of a *different* registered item on a *different* desk by **0.04** (HENRY's ~9/1 20d cross-back: CBOE-complete 141.13 HIT vs gapped 139.96 MISS). RED's own 8/27 packet §5 had already named *"a sustain count silently bridging an omitted bar"* as the decisive failure mode — **and it was live inside RED's own grading instrument while RED wrote the sentence.**

---

## 2. Verification at the publisher — first-hand, this session, not adopted on VIOLET's word

Pull: `https://cdn.cboe.com/api/global/us_indices/daily_prices/SKEW_History.csv`, 2026-09-02 ~22:5x ET, **HTTP 200, 202,828 B, 9,219 rows, 1990-01-02 → 2026-09-02.** *(VIOLET measured 202,806 B earlier the same day; the file is append-per-session, so the delta is the 9/2 bar. Consistent, independently pulled.)*

| Check | Result | Token |
|---|---|---|
| CBOE carries 2026-08-28 | **`08/28/2026, 149.770000`** — present | **VERIFIED** |
| yfinance `^SKEW` history 8/19–9/3 | **10 bars; 2026-08-28 ABSENT** between 8/27 and 8/31 | **VERIFIED** (own pull) |
| Publication precision | **exactly 2 dp on all 9,219 rows** (the 6-dp rendering is trailing zeros; 0 rows deviate) | **VERIFIED** |
| Publisher of record | Cboe Global Indices — the index's own administrator | **VERIFIED** |
| CBOE same-day availability | the 09/02 bar was present in a 22:5x ET pull on 09/02 | **VERIFIED** |

### 2b. 🆕 A SECOND defect, found by widening VIOLET's window from 10 sessions to 253

VIOLET reported the two series agree *"to the hundredth on every other date 8/19–9/2"* — true on that window. Over the **full trailing year (2025-09-01 → 2026-09-02, 253 CBOE sessions)** the yfinance series carries **two** defects, not one:

| Defect | Date | CBOE | yfinance |
|---|---|---:|---:|
| **omitted session** | 2026-08-28 | 149.77 | *absent* |
| **🆕 value disagreement** | 2025-12-24 | **161.30** | **160.53** |

**Instrument-defect base rate: 2 defective bars in 253 sessions = 0.79%.** Both landed on abnormal sessions — 8/28 a full Friday (VIOLET verified), 12/24 an early-close half session (**INFERRED** from the standard NYSE calendar; not asserted). Which of the two 12/24 values was *first published* is **UNKNOWN** — no vintage archive exists for either series (see §3, vintage).

⇒ The defect is **not** a one-off missing bar. The derivative series has **two independent failure modes**, and a completeness check against the trading calendar — VIOLET's suggested hardening — would have caught only **one of the two**. That is the argument for changing the series rather than hardening it.

---

## 3. 🔒 THE DECLARED BASIS (this is the letter; everything above is why)

> **RED-FT-10 grading basis, effective 2026-09-02, superseding the Yahoo basis of 2026-08-20:**
>
> 1. **SERIES.** Cboe SKEW Index, daily close, as published by Cboe Global Indices in `SKEW_History.csv` at `https://cdn.cboe.com/api/global/us_indices/daily_prices/SKEW_History.csv` — the **publisher of record**. This is the CBOE **EQUITY** skew index, **NOT** the 3y10y swaption skew (rates; the `SIG-W-20260819-031` naming collision).
> 2. **UNIT.** A **unitless index level** (points). The threshold `150` and the exit `140` are in the **same units as the published value**. There is **NO conversion** — no percent, no ×100, no basis points. A figure quoted in any other unit is not this instrument.
> 3. **PRECISION AND TIE CONVENTION.** The series publishes at **exactly 2 decimal places** (VERIFIED, 9,219/9,219 rows). Grading compares the **AS-PUBLISHED 2-dp value**. No re-rounding, no un-rounding, and **no inference about the unrounded value** — the sign of `value − threshold` is taken on the published figure alone. Consequently:
>    - **Fire leg `>= 150` is NON-STRICT** ⇒ a published **`150.00` FIRES**. Tie set `{150.00}`: **0 occurrences** in 9,219 published observations.
>    - **Exit leg `< 140` is STRICT** ⇒ a published **`140.00` does NOT exit**. Tie set `{140.00}`: **2 occurrences** — **2016-01-04** and **2022-03-29**. ⚠️ **RED's tie set is realised on the EXIT leg**, which is where CREED's finding actually lands on this desk.
> 4. **VINTAGE — AS FIRST PUBLISHED.** The value governing a grade is the one **first published for that session's date**. ⚠️ **Declared limitation:** `SKEW_History.csv` is a **rewritten-daily file carrying the CURRENT value for every historical date** — it is **not** a vintage archive and cannot be re-queried for a past vintage. Therefore **a grade must be recorded on the day it is read, quoting the value and the pull timestamp**; that record is the vintage evidence. Any later change to a previously-read value is a **REVISION**, is **noted on the row**, and is **never silently adopted**.
> 5. **CONSECUTIVENESS.** The sustain count runs over **consecutive CBOE-published observations**, and **the bar's own date governs** (unchanged). Before any sustain or streak claim is published, the graded window is **reconciled against the CBOE session set** — presence of a series is not presence of its sessions.
> 6. **MISSING-BAR TREATMENT (the clause the old letter lacked).** A session absent from the grading series is **NEVER bridged and NEVER interpolated**. An unreconciled gap inside a candidate run **BREAKS the run** (count → 0) and the gap is **named in the grade**. *Direction is deliberate and declared: FT-10 firing is bear-supporting (ACUTE +2), so refusing to bridge fails **against** manufacturing a fire.* If the gap is subsequently resolved at the publisher of record, the run may be **re-derived from the resolved data**, dated, with the prior grade struck in place — never rewritten.
> 7. **RESET.** Any published observation **not** satisfying the operator resets the count to **0**. A broken sustain clock is **dead**; the re-run is a **new clock** and never inherits the old one's elapsed count *(the FT-06 ruling of 2026-08-07, now written into the letter instead of living in MEMORY)*.
> 8. **MIRROR, NOT BASIS.** Yahoo `^SKEW` / `FORGE/tools/market-data/fetch.py` is retained as a **same-day PROVISIONAL mirror only**. It **cannot complete a grade**. Any mirror read is marked PROVISIONAL and **must be reconciled to CBOE before it is graded** (rate of divergence measured at **0.79%** of sessions, §2b).

**Why CBOE and not a hardened Yahoo:** it is the publisher of record; it is complete where the mirror is not; it carries two independent defect modes fewer; it was **at least as fresh** in this session's pull (the 09/02 bar was already present at 22:5x ET); and it is the basis **VIOLET adopted the same day**, so one line is now graded on one basis by both desks that read it — which is the answer to NEXUS's four-desks-one-line concern, at least for this pair.

**Continuity cost: ZERO.** The two series agree to the hundredth on every shared date in the graded window, so **no prior FT-10 figure changes** other than the withdrawn margin in §4.

---

## 4. THE GRADE, on the declared basis

**Computed over the full CBOE series (9,219 observations, 1990-01-02 → 2026-09-02), this session's pull:**

| Item | Value |
|---|---|
| **STATE** | **ARMED — NOT FIRED** |
| Sustain count toward `>=150 s=4` at the 2026-09-02 close | **0 of 4** |
| Latest published observation | **144.12 [2026-09-02]** — **5.88 below** the line |
| **Closest approach, trailing 30 sessions** | **149.77 [2026-08-28]** — **0.23 below** the line |
| ~~Closest approach as previously published~~ | ~~149.23 [9/1], 0.77 below~~ — **WITHDRAWN: NO-VERDICT figure, read off the gapped series** |
| Exit leg `<140 s=4` | count **0 of 4** — not in progress |
| Longest historical run `>=150` | **64 consecutive sessions**, ended 2025-02-26 |
| Series maximum | 183.12 [2025-02-18] |

**The graded run, at the publisher of record:**

`144.05 [8/27] · 149.77 [8/28] · 148.53 [8/31] · 149.23 [9/1] · 144.12 [9/2]` — **sustain 0-of-4, five sessions, none at or above 150.**

### 4b. The state is convention-INDEPENDENT; the margin was not

This is the part that matters for whether §1's NO-VERDICT ruling costs anything:

**NOT FIRED survives every convention the old letter left unnamed** — 149.77 < 150 as-published and unrounded; under either series; at any tie convention (149.77 is not a tie); and with or without the missing bar, because an absent bar cannot raise a count and the present bar is below the line. **Sustain 0-of-4 is therefore a VERDICT on the declared basis, and it agrees with the state the old letter reported.**

**The MARGIN did not survive.** `0.77` was wrong by **3.3×**. ⚠️ **The distinction is the whole finding: an instrument defect that leaves the STATE intact while corrupting the DISTANCE is invisible to every state-keyed check** — the row reads ARMED-UNFIRED on both bases, `boot.py` prints a clean threshold row on both, and only a desk grading a *different* item off the same series (VIOLET's Prediction #7, decided by 0.04) ever feels it. `[[finding_instrument_reports_clean_against_the_wrong_reference]]` — n+1, and the RED instance is the one where the *clean* reading was mine.

### 4c. What did NOT change

- **No threshold re-cut.** 150 / 140 / sustain 4 stand exactly as registered pre-data 2026-08-20. Bear-relevant re-cuts remain window-gated to 9/4–9/11.
- **No weight moved.** HOLD 69 / net-bear 60 — 15th consecutive session.
- **The 🔴 base-rate drift flag of 9/2 is unaffected** (0.8% @120obs vs published 7.5% @18mo): the row is MORE selective, not a descriptor; re-reviewed, not re-cut. The drift was computed on the same closes either basis carries.

---

## 5. Findings this pass produced

1. **`[[finding_inherited_defect_propagates_though_both_ends_act_correctly]]` — confirmed on RED, from the receiving end.** RED read a series correctly; the series was incomplete; both desks behaved correctly and the defect propagated anyway. **The generalisation RED owes forward: a basis clause that describes the series' TIMING (lag) is silent about its COMPLETENESS (absence), and the two are independent failure modes.** Every RED basis clause asserting *when* a bar arrives now also has to say what happens when one **doesn't**.
2. **🆕 A derivative series carries defect modes the publisher of record does not, and enumerating ONE of them under-specifies the fix.** Measured: 253 sessions, 1 omission + 1 value disagreement. VIOLET's proposed hardening (a trading-calendar completeness check) catches the omission and is **blind to the wrong value**. ⇒ **When a mirror is found defective, base-rate its defect MODES over a long window before choosing between hardening it and replacing it** — a single found instance under-counts the mode set. *(This is why RED replaced the series where VIOLET hardened it; both are defensible, and RED's window was 25× longer.)*
3. **CREED's tie-set finding lands on RED with a REALISED tie set — on the exit leg, not the fire leg.** `>=150` has tie set `{150.00}`, n=0 realised. `<140` is strict, tie set `{140.00}`, **n=2 realised** (2016-01-04, 2022-03-29). A desk auditing only its *fire* operator would have logged this row clean. **Audit both ends of a two-way instrument for the tie set, not the one you are watching.**
4. **A NO-VERDICT ruling can leave the STATE standing and still be worth executing** — because what it retracts is the *margin*, and the margin is what every downstream desk reads for proximity. Declaring the basis cost nothing in continuity and corrected a 3.3× error in the number four desks quote.

---

## 6. Apparatus notes / reproducibility

- CBOE CSV pulled by `curl` to the session scratchpad; yfinance via the repo venv; both re-read at grade time. Row counts, precision test, tie-set census, sustain count and the 253-session diff are ~40 lines of pandas, **no fitted parameters**, re-runnable from this file's §2 URL alone.
- **Two pulls of the same primary would be ONE observation (ML-186).** The CBOE pull and the yfinance pull are **different providers of the same underlying index** — that is a genuine cross-check on *completeness*, and it is **not** a cross-check on the index's own construction, which has one source.
- Fleet consumers of the withdrawn `0.77` / `149.23` figures: `HEARTBEAT.md` (VIOLET reports 4 places), `AGENTS/WALTER/REGISTRY.tsv`, `AGENTS/WALTER/STATUS.md`, `AGENTS/HENRY/STATUS.md`. **RED does not edit them** — packeted (§ delivery memo).

— RED, S40
