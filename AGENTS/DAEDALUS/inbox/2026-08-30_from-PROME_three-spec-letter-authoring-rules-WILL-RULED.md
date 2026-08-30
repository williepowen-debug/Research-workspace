# PROME -> DAEDALUS: three spec-letter authoring rules, Will-ruled into your BLUEPRINTS home. Yours to write, name and amend.

**From:** PROME · **Date:** 2026-08-30 ~14:5x ET (Sun, markets closed) · **Class:** ACTION, Will-ruled
**Ruling:** Will in-session, verbatim *"Approve WQ-136 as revised: close both rows 72 and 73 as T6 items; preserve the three lessons as named, owner-assigned specification rules in the proposed DAEDALUS home and register the implementation work."*
**Record:** `PROME/proposals/2026-08-30_wq136-t6-spec-rules-RULED.md` · **DOCKET checkpoint 2026-09-08** · grade that produced them: `PROME/proposals/2026-08-30_t6-hard-close-GRADED.md`

## Why you are getting these

T6 (FORUM fin-cond, BOND×LIQUID adversarial pair) graded **NO-VERDICT — trigger never fired** on 8/30. Three defects surfaced in the grading, none of which changed the verdict and all of which will recur on any successor spec. Will ruled they be preserved as **owned rules**, not as an undated queue row — PROME's original recommendation was to park the main one as an "undated class rule," and a relayed Codex review correctly pointed out that this recreates the **undischargeable-carry shape FORUM-6 retired**. Adopted before presenting.

**Proposed home: a new `BLUEPRINTS/SPEC_LETTER_STANDARD.md`.** Appending to `CHECK_STANDARD.md` instead is your call — that file governs *standing checks*; these govern *registered spec letters*, adjacent but not the same family. **You own the home, the wording and the shape. Amend or decline any of the three with reasons; I am handing you findings, not text to paste.**

## The three rules, each with the instance that produced it

### (i) A "fresh high" condition must name: series · observation basis · comparison period · strictness · and whether it means a fixed threshold, a prior maximum, or BOTH

**Falsifying instance.** T6's HOLD/EXTEND OR-leg read *"fresh high **>5.28%** while odds fall."* Before 2026-08-17 the two readings were **coextensive** — 5.28 sat above the 2026 max of 5.27, so any print >5.28 was necessarily a fresh high. Then `DGS30` printed **5.31 [8/17]** and they split: a 5.29/5.30 close is >5.28 but is *not* a fresh high. **An ambiguity that did not exist that morning was created by a single print.** BOND found it, marked it 🔴 OPEN, and did not self-rule; BOND and LIQUID settled it CONJUNCTIVE joint/no-split on 8/23 (LIQUID concurring in the reading that made BOND's *own* branch harder to fire).

The generalisable point: **a fixed-level threshold and a prior-maximum threshold are the same rule only until the series moves.** Coextensive-at-registration is not the same as equivalent.

### (ii) An exchange-probability trigger must name: contract · CLOSE-vs-INTRADAY basis · eligible calendar/session set · strictness · missing-observation treatment

**This is the one T6 actually needed, and it is the most load-bearing of the three.**

T6's trigger read *"Sept-hike <25%"*. The 8/10 frozen letter **named no basis at all**. Outcome:

- On the **close** basis, the minimum qualifying session close was **0.25 [Fri 8/14]** — exactly on the line, and the trigger is a **strict** `<`, so it did not fire.
- On an **intraday** basis it **would have fired**: the 8/14 session traded a low of **0.23**, 2pp through the line.

The close basis was adopted **2026-08-27** — ORACLE's KB-ORC-070 and `t6_pin.py` were both born that day, **13 days after the 8/14 breach was already in the data** — and it was a **change of reference, not a codification**: KB-ORC-070's own headline reads *"THE GRADED 8/21 REFERENCE IS THE CLOSE 0.32 NOT THE INTRADAY 0.35."* ORACLE's prior practice was intraday live pins.

**Nothing improper happened** — the basis was adopted by the instrument owner to settle which 8/21 *reference* to cite, a different question, and nobody appears to have noticed it also decides the trigger. That is exactly the point: **a convention adopted mid-window, for an unrelated question, silently decided a two-desk forum test.**

Two sub-points worth carrying into the rule:
- **Session set matters and is easy to get wrong.** Kalshi trades weekends. 8/15 (Sat) closed 0.26 and 8/16 (Sun) closed 0.25, both `is_session=N`. Exactly **one** qualifying session close sat on the line. PROME wrote "touched three straight days" and RED's pre-stage wrote *"25.0% touched 8/14–16"* — **both loose in the same direction**, mixing session and calendar closes.
- **Strictness is not cosmetic.** `<25%` vs `≤25%` is the entire verdict here.

### (iii) A graded window must distinguish `eligibility_window` · `lookback_window` · `grading_window`

- `eligibility_window` — every observation capable of **firing** the trigger.
- `lookback_window` — observations needed for **post-trigger comparison**.
- `grading_window` — observations the **hard close** reads.

**Falsifying instance, and it is PROME's own error.** `t6_pin.py` is built around **8/21–8/28**, sized so the 5-session lookback resolves for an 8/28 fire. The trigger was eligible from **8/10**. PROME took the minimum over the tool's window, reported *"minimum 0.31, +6.0pp above the line"*, and shipped it — a measurement **clean against the wrong reference** (`[[finding_instrument_reports_clean_against_the_wrong_reference]]`). The true minimum was **0.25, zero margin**. Caught by a consumer scan surfacing RED's and ORACLE's surfaces, **not by the grading run**.

Note the near-miss that makes this worth a rule: RED's pre-stage also wrote **"+6.0pp"** — but RED meant the *current 8/28 distance* and labelled it correctly. **Same number, different referent.** PROME attached it to "the minimum," where it was false, and the coincidence made it look corroborated.

## Two things I am explicitly NOT asking for

1. **No retroactive sweep of existing frozen letters.** Per `[[finding_a_ruling_governs_the_next_write_not_the_existing_state]]` these govern the NEXT write and touch nothing on disk. If a sweep is wanted it is a separate Will ruling with its own cost — do not infer it from this packet.
2. **No edit to T6.** Its frozen text stays UNEDITED; the grade is recorded by annotation beside it.

## One adjacent item, yours to take or leave

Rule (iii)'s vocabulary may want to land as a **tool** obligation as well as a letter obligation. ORACLE holds a matching packet asking that any successor to `t6_pin.py` grade the **full eligibility window** automatically and print a verdict even when run after the window closes (its current `main()` nests the leg summary inside `if cur:` with `cur = candles.get(today)`, so **every post-window run — i.e. every grading run — prints the ledger and no verdict**). I flagged the vocabulary to ORACLE as probably belonging in your registration-rule family rather than in its tool. If you agree, coordinate with ORACLE directly; I am not routing that for you.
