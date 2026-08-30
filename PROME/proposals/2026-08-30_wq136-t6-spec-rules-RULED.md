# RULED — WQ-136: rows 72/73 CLOSED as T6 items; three lessons become owner-assigned specification rules

**Ruled:** 2026-08-30 ~14:5x ET Sun, Will in-session, verbatim: **"Approve WQ-136 as revised: close both rows 72 and 73 as T6 items; preserve the three lessons as named, owner-assigned specification rules in the proposed DAEDALUS home and register the implementation work. Then proceed with the GATES condition pass."**
**Author:** PROME · **Executed:** same sitting.

## What was decided

1. **Rows 72 and 73 CLOSE as T6 items.** T6 graded NO-VERDICT (trigger never fired, 2026-08-30), which made both rows moot for the purpose they were dated for.
2. **Their surviving lessons do NOT stay as an undated queue row.** They become **named specification rules with an owner** — proposed home **`AGENTS/DAEDALUS/BLUEPRINTS/`**, DAEDALUS ruling the final file.
3. **The implementation work is registered** — DOCKET row, owner DAEDALUS, checkpoint 2026-09-08.

## Provenance of the revision — PROME's first rec was worse, and was replaced

PROME originally recommended *"close 72, keep 73's divergence clause as an UNDATED class rule."* A relayed **Codex** review argued that an undated, ownerless class rule recreates exactly the **undischargeable-carry shape the fleet retired at FORUM-6** (the reader-discharge ruling that replaced the undischargeable staleness-flag class). That is correct, and PROME adopted it before presenting. Recorded because the fleet's own rule is that a lesson without an owner and a discharge path is not preserved — it is parked.

## The three rules (as packeted to DAEDALUS)

**(i) Fresh-high conditions.** A "fresh high" leg must name: the **series** · the **observation basis** · the **comparison period** · **strictness** (`>` vs `≥`) · and **whether it means a fixed threshold, a prior maximum, or both**.
*Origin:* T6's `>5.28%` OR-leg. Before 8/17 the two readings were coextensive (5.28 sat above the 2026 max of 5.27); `DGS30` printed **5.31 [8/17]** and they split, creating an ambiguity that had not existed that morning. BOND marked it 🔴 OPEN; the desks settled it CONJUNCTIVE joint/no-split on 8/23.

**(ii) Exchange-probability triggers.** A probability trigger must name: the **contract** · **close-vs-intraday basis** · the **eligible calendar/session set** · **strictness** · and **missing-observation treatment**.
*Origin:* **this is the rule T6 actually needed.** Its frozen letter of 8/10 named no basis at all. The close convention was adopted **2026-08-27** — KB-ORC-070 and `t6_pin.py` both born that day, 13 days after the 8/14 intraday breach already existed — and as a **change** of reference, not a codification (*"THE GRADED 8/21 REFERENCE IS THE CLOSE 0.32 NOT THE INTRADAY 0.35"*). On a close basis the trigger never fired; **on an intraday basis it would have fired on 8/14 (low 0.23, 2pp through the line).** A basis convention adopted mid-window for a different question decided a two-desk forum test.

**(iii) Window vocabulary.** A graded window must distinguish **`eligibility_window`** (every observation capable of firing the trigger) · **`lookback_window`** (observations needed for post-trigger comparison) · **`grading_window`** (observations the hard close reads).
*Origin:* `t6_pin.py` is built around the 8/21–8/28 pin/lookback window while the trigger stayed eligible from **8/10**. PROME measured the minimum over the pin window and reported a margin figure clean against the wrong reference — `[[finding_instrument_reports_clean_against_the_wrong_reference]]`. The tool's design encouraged the error; the vocabulary is the fix, not the indentation bug beside it.

## Scope discipline

- **PROME does not author in `AGENTS/DAEDALUS/`.** The rules travel as an inbox packet (carve-out ①); DAEDALUS writes the blueprint, rules its home, and may amend or decline any of the three with reasons. Proposed home is a new `BLUEPRINTS/SPEC_LETTER_STANDARD.md`; appending to `CHECK_STANDARD.md` is DAEDALUS's call if it prefers — that file governs *standing checks*, these govern *registered spec letters*, which is adjacent but not the same family.
- **No threshold, band, branch or frozen letter moves.** These are authoring rules for FUTURE specs. ⚠️ Per `[[finding_a_ruling_governs_the_next_write_not_the_existing_state]]`, they touch nothing already on disk — **no retroactive sweep of existing letters is authorised here**, and none should be inferred. If a sweep is wanted it is a separate Will ruling with its own cost.
- T6's own frozen text remains **UNEDITED**.

## Execution trail

- `PROME/WILL_QUEUE.md`: rows **136**, **73**, **72** → RECENTLY DONE with the ruling verbatim; reconcile stamp updated; three rows off OPEN (cap relief).
- Packet → **DAEDALUS** (`AGENTS/DAEDALUS/inbox/`), the three rules with origins and falsifying instances.
- `PROME/DOCKET.tsv`: implementation row registered, owner DAEDALUS, **2026-09-08**.
- BOND and LIQUID already hold T6 packets carrying the closure reasoning; no re-packet needed.
