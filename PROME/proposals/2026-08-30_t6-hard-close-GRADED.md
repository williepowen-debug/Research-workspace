# T6 HARD CLOSE — GRADED: **NO-VERDICT (trigger never fired)**

**Graded:** 2026-08-30 ~14:2x ET Sun, PROME, on the DESKTOP (`DESKTOP-BC6EF81`) — the first desktop boot since the row was annotated `COVERED:PROME-DESKTOP` (DOCKET row 20, BOOT step-8 third-boot rule). The grader's authed-Kalshi path is desktop-only; public reads from the laptop could not settle it.
**Test:** FORUM fin-cond slate item 6 — **T6, 30Y benign-bucket test.** BOND (instrument, original spec) / LIQUID (co-spec).
**Status of this record:** **PROME-recorded, owner-confirmable.** Both co-owners are dark; the outcome is mechanically determined by the frozen letter with zero discretion, and NO-VERDICT scores neither desk — so PROME records rather than adjudicates. Packets to BOND + LIQUID invite confirm-or-correct at their next touch.

---

## The frozen letter (unedited, quoted from `04_synthesis/06_HENRY_joint-synthesis-FINAL.md` line 213)

> **Trigger: Sept-hike <25%.** RETRACE: DGS30 <5.05 ×2 within 5 sessions. HOLD/EXTEND: ≥5.10 for those 5, **or** fresh high >5.28 while odds fall. **NO-VERDICT band: 5.05–5.10, or trigger never fires**

Effective last gradeable data = **Fri 2026-08-28 session closes** (Option C, Will-ruled 2026-08-21 verbatim *"Rule T6 Option C off your rec"* — `PROME/proposals/2026-08-21_t6-saturday-option-c-RULED.md`). Hard close 2026-08-29 (Sat) stood as written.

## The measurement — Kalshi `KXFED-26SEP-T3.75`, the FULL eligibility window

⚠️ **CORRECTED 2026-08-30 ~14:4x, same session, before the second commit.** My first pass measured **8/21–8/28 only** — that is `t6_pin.py`'s *pin* window, chosen so the 5-session lookback resolves for an 8/28 fire, and it is **NOT the trigger's eligibility window.** The trigger could fire on any session between registration (8/10) and the last gradeable data (8/28). Taking the minimum over the pin window produced a margin figure that was clean against the wrong reference (`[[finding_instrument_reports_clean_against_the_wrong_reference]]`). Caught by the consumer scan surfacing RED's and ORACLE's own surfaces — **not by the grading run.** Corrected below; **the verdict is unchanged, the margin is not.**

Captured 2026-08-30 14:19 / 14:4x ET from the exchange's daily candlestick record (`period_interval=1440`), read-only. Reproduced verbatim so the evidence is durable in a PROME-owned file independent of ORACLE's workbook and of post-settlement candle retention:

| day | dow | sess | **close** | low | high | volume |
|---|---|---|---:|---:|---:|---:|
| 2026-08-10 | Mon | Y | 0.46 | 0.35 | 0.46 | 10,738 |
| 2026-08-11 | Tue | Y | 0.42 | 0.42 | 0.45 | 39,560 |
| 2026-08-12 | Wed | Y | 0.36 | 0.27 | 0.49 | 9,117 |
| 2026-08-13 | Thu | Y | 0.29 | 0.27 | 0.36 | 14,727 |
| **2026-08-14** | **Fri** | **Y** | **0.25** | **0.23** | 0.29 | 11,513 |
| 2026-08-15 | Sat | N | 0.26 | 0.25 | 0.27 | 2,691 |
| 2026-08-16 | Sun | N | 0.25 | 0.25 | 0.27 | 333 |
| 2026-08-17 | Mon | Y | 0.31 | 0.25 | 0.32 | 6,053 |
| 2026-08-18 | Tue | Y | 0.30 | 0.27 | 0.32 | 1,107 |
| 2026-08-19 | Wed | Y | 0.29 | 0.29 | 0.30 | 6,643 |
| 2026-08-20 | Thu | Y | 0.29 | 0.27 | 0.29 | 1,518 |
| 2026-08-21 | Fri | Y | 0.32 | 0.28 | 0.35 | 34,347 |
| 2026-08-22 | Sat | N | 0.30 | 0.28 | 0.33 | 325 |
| 2026-08-23 | Sun | N | 0.34 | 0.32 | 0.34 | 182 |
| 2026-08-24 | Mon | Y | 0.34 | 0.32 | 0.55 | 8,637 |
| 2026-08-25 | Tue | Y | 0.35 | 0.33 | 0.35 | 46,786 |
| 2026-08-26 | Wed | Y | 0.32 | 0.31 | 0.35 | 10,113 |
| 2026-08-27 | Thu | Y | 0.31 | 0.30 | 0.34 | 796 |
| 2026-08-28 | Fri | Y | 0.48 | 0.30 | 0.65 | 53,314 |

`t6_pin.py`'s 8/21–8/28 pin window returned **MARKED GAPS: 0**. Weekend rows carry `is_session=N` per BOND's ruled weekday count and never enter the count; they are printed because gap-marking is mandatory (BOND 2026-08-21: *"a daily pin without gap-marking is WORSE than no pin"*). Two days settled since ORACLE's 8/27 14:41 pin: 8/27 was `LIVE-INTRADAY 0.32` and **settled 0.31**; 8/28 was `PENDING` and **settled 0.48**.

*(Basis note for ORACLE: RED's pre-stage cites "Registration 8/10: 35.5%", while the Kalshi daily close for 8/10 is **0.46** — a platform/basis difference, not a contradiction, and not verdict-relevant at 20pp+ from the line. Worth reconciling in ORACLE's own log so the registration anchor has one stated basis.)*

## The grade

- **Minimum session CLOSE over the full eligibility window: `0.25` [Fri 8/14]** — **exactly ON the line, 0.0pp of margin.** The trigger reads `<25%`, **strict**; 0.25 does not satisfy it. The weekend closes 0.26 [8/15] and 0.25 [8/16] sit on the same level and are non-sessions besides.
- The trigger was **touched on three consecutive days (8/14–8/16) and never crossed**, then ground away: 0.31 [8/17] → 0.29 [8/20] → 0.31 [8/27] → **0.48 [8/28]**, +17pp on the Warsh keynote.
- ⇒ **TRIGGER NEVER FIRED** ⇒ the frozen letter's own **"NO-VERDICT ... or trigger never fires"** branch.

### ⇒ **T6 = NO-VERDICT. Neither desk scored. Earned, not an artifact.**

### ⚠️ The verdict rests on the close-vs-intraday basis convention — which is now outcome-determinative

**On an intraday basis T6 WOULD HAVE FIRED: the 8/14 session traded to a low of `0.23`, 2pp BELOW the trigger** (8/16 and 8/17 also printed lows at 0.25). The grade survives only because the canonical reference is the **daily close** — ORACLE's own **KB-ORC-070** rules *the graded reference is the CLOSE, not the intraday*; it is the basis `t6_pin.py` pins, and BOND's locked fallback accepted it on both legs.

ORACLE flagged this abstractly in its 8/28 BOTTOM LINE: *"a graded reference value that changes T6's verdict depending on whether you read a close or an intraday capture."* **This record supplies the number that makes it concrete.** ORACLE was right that it mattered — and it mattered more than which 8/21 reference to cite: it decides the test. Neither RED's pre-stage nor ORACLE's STATUS stated the sub-25 intraday print numerically; both correctly reported the close-basis result (*"25.0% touched 8/14–16, strict less-than never crossed"*) without surfacing that the intraday went through the line.

**Nothing here changes the grade.** The close basis was pre-committed, is ORACLE-ruled, and was not selected after the fact. It is recorded because a future reader comparing T6 against a successor spec must know this NO-VERDICT is a **basis-convention outcome, not a comfortable miss** — and any successor keying a probability trigger to an exchange series should name close-vs-intraday **in the letter**.

## RED's falsifier seat — F3 discharged, provenance now on the grade record

RED holds the **T6 falsifier seat** (Will-assigned via DAEDALUS relay, Will-confirmed in-session verbatim **"A"**, 2026-08-28) and pre-staged this verdict independently on 8/28: **NO-VERDICT (trigger-never-fired branch), confidence VERY HIGH** — `AGENTS/RED/reports/2026-08-28_T6_falsifier_pre_stage.md`. Two independent seats reached the same branch by the same route. RED's four findings, disposed:

| | RED's finding | Disposition at this grade |
|---|---|---|
| **F1** | OR-leg spec ambiguity; asks BOND/LIQUID to name their reading **on the record at grade time** | **Moot for this grade** — the OR-leg is post-trigger and was never reached. Named anyway per RED's ask: the settled joint reading (BOND+LIQUID, 8/23, no split) is **CONJUNCTIVE** — `close >5.28% AND strictly above the prevailing 2026 max 5.31 [8/17], ratcheting`; 5.29/5.30 does **not** fire. RED's class point stands. |
| **F2** | Missing 8/28 Sept-hike pin | **DISCHARGED by this run** — 8/28 settled **0.48** (was `PENDING` in ORACLE's ledger). |
| **F3** | RED-seat provenance owed on the grade record | **DISCHARGED — this section.** |
| **F4** | pre-stage-vs-grade language ambiguity | Addressed in this record's header: RED pre-staged, **PROME recorded**, BOND/LIQUID own the formal grade and are packeted to confirm-or-correct. |

RED's **R4** rider also stands unused: an ungradeable *"keeps falling"* qualifier defaults the OR-leg to **NOT firing**, never to firing.

## Three things this record fixes, stated because they read identically to a future reader and only one of each is true

1. **This is NOT `NO-VERDICT-BY-COMPRESSION`.** Option C pre-named compression for a trigger firing *too late to complete a branch*. No fire occurred at all. The grade lands on the **primary NO-VERDICT branch both co-owners wrote into the frozen text at registration** — the spec anticipated this outcome and named it. DOCKET row 20's annotation read "NO-VERDICT-bound per the 8/21 Option C ruling"; the correct attribution is the letter itself, and Option C never had to carry it.
2. **The DGS30 legs were never reachable, so Monday's publication cannot move this.** RETRACE and HOLD/EXTEND are both *post-trigger* legs. The 8/28-dated DGS30 observation publishes Mon 8/31 under the lagged-series class ruling (option (i), Will 2026-08-27) — **that ruling still governs its class and still governs MIDAS-06 on Monday; its T6 application is now moot.** The UNGRADEABLE-PENDING-PUBLICATION rider BOND and LIQUID jointly asked for is **discharged, not owed**.
3. **The D-DIVERGENCE clause never bit, would not have, and the desks had already settled it between themselves.** Observed DGS30 across the window: **5.27 [8/21] → 5.23 [8/24] → 5.17 [8/25] → 5.18 [8/26] → 5.19 [8/27]** (FRED, 8/28 unpublished). No print exceeded 5.28, and the 2026 max of 5.31 [8/17] predates the window — so even on a counterfactual trigger fire, the fresh-high vs `>5.28` split BOND marked 🔴 OPEN would not have been reached. What was outstanding on that clause was **Will's word, not the co-owners' position**: BOND and LIQUID settled all six items **joint, no split, on 8/23**, LIQUID concurring in BOND's CONJUNCTIVE reading verbatim — a reading that made BOND's *own* branch harder to fire. LIQUID called the never-fires branch **MODAL** the same day and said *"if it never fires T6 is NO-VERDICT and this whole stack is moot."* **LIQUID was right.**

BOND's standing position — *"if Will does not rule the repairs before the close, T6 grades AS WRITTEN, defects and all"* (LIQUID and PROME both held it) — is what executed here. The frozen text was never edited. Every defect BOND and LIQUID found sits inside HOLD/EXTEND and went unreached.

## Consumer note — one superseded figure

`HEARTBEAT.md` carried **"Kalshi Sept-hike 0.50 LIVE [8/28 16:06]"** on its §Stress dashboard, beside its own note *"daily close = ORACLE's."* The canonical daily close is now settled at **0.48**. HEARTBEAT amended (chain 3). LIQUID's STATUS already read `0.48 live [8/28]` and needs no correction.

## Execution trail

- FORUM synthesis: dated resolution annotation appended beside the frozen T6 text — **annotate, never rewrite** (PROME = sole committer for the forum tree).
- `PROME/DOCKET.tsv` row 20 → `RESOLVED(NO-VERDICT 2026-08-30 — trigger never fired)`.
- `HEARTBEAT.md` AMENDMENT #3 (0.48 settled close; DGS30 5.19 [8/27] refresh).
- Packets: **BOND** + **LIQUID** (co-owners, confirm-or-correct) · **ORACLE** (write its own `workbook/T6_PIN.tsv` — PROME ran read-only and did not author in ORACLE's workbook).
- **WQ-136** registered: rows 72/73 re-scope, Will's call.
