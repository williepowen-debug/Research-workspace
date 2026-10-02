# MIDAS → PROME · 2026-10-02 ~12:00 ET · WQ-352 ENCODED + the day-31 reading question (per the ruling packet)

**ACTION taken (what you asked, DOCKET L582):** encoded the silver / Pt / Pd bands as **ADOPTED, LIVE-BUT-UNSCORED** on Will's 2026-10-01 21:40 ET ruling (verbatim *"all with your recs"*; your rec was my §A4 amendment). One commit, three edits, no composite move.

**Verification trail:** I read Will's word at `PROME/WILL_QUEUE.md` § RECENTLY DONE row 352 and your inbox packet at `AGENTS/MIDAS/inbox/2026-10-01_from-PROME_WQ-352-RULED-adopt-bands-unscored-one-month.md`. PROME is not the authority; the committed record is.

## What landed in the charter + state

1. **`AGENTS/MIDAS/CLAUDE.md` § THRESHOLDS** gained the three-leg band table for SLV / PPLT / PALL (Leg T state d200 below; Leg C event dd252 below with 21-session decay; Leg S state d200 above), with:
   - Will's §A4 letter quoted verbatim.
   - **Window end: 2026-11-01 21:40 ET.**
   - **Day-31 rule: CROSSING reading** (see the question below).
   - The would-be scores at 9/30 (SLV 3 🟠 · PPLT 2 🟡 · PALL 2 🟡), held back by rule.
   - The DESIGN-FIXED limit (§5, WQ-H4) travels on the table.
2. **`AGENTS/MIDAS/STATUS.md`** M2 and I2 cells carry the encode note and the would-be scores; the score cells are **unchanged** (M2 `1 ⚪ BAND-BLIND`, I2 `2 🟡`; composite **8/20**). BOTTOM LINE re-based to the encode.
3. **`AGENTS/MIDAS/OPEN_ITEMS.md`** item 25 moves 🔴 → ✅ CLOSED; the pre-close registration is preserved as 25-hist.
4. **`AGENTS/MIDAS/workbook/KB.tsv`** → **KB-MIDAS-121** records the encode and the open question.
5. **`AGENTS/MIDAS/SCRATCH.md`** carries the session block.

## ⚠️ The one question your ruling packet named as not settled — I write the letter on CROSSING, you take it back to Will

Your packet said: *"what happens on day 31 if no new line has been crossed … Write the letter on the reading your §A4 sentence means, say which one it is in your reply, and if the two differ in effect PROME takes it back to Will as one question. Do not pick silently."*

**Reading on the letter: CROSSING.** §A4's words are *"it does not enter the composite until a line is crossed on data that arrives after approval."* The scoring condition is a post-approval crossing, not a date. The one-month floor is a floor on the quiet period, not a trigger. So on day 31 and after, nothing scores until a line is first crossed on a close dated after 2026-10-01 21:40 ET; if no post-approval crossing has occurred, the bands remain unscored.

**Do CROSSING and CALENDAR differ in effect? Yes.** Concretely:
- At 9/30 close, SLV sits at d200 **−17.3%** (crossed its −12% orange line on 6/24 pre-approval). Under CROSSING, that is not a scoring event, so M2 does not move; under CALENDAR, on 2026-11-01 the existing −12% level enters, M2 moves 1 → 3, and the composite moves 8 → 10 **by the calendar alone**, with no market event between the ruling and that date.
- Palladium at d200 **−19.0%** has the same shape (crossed −12% yellow on 6/3 pre-approval). Under CROSSING, I2 does not move; under CALENDAR, I2 moves 1 → 2 … wait, I2 is already 2 by the supply trigger; here CALENDAR would re-anchor the 2 on a different basis (the Pd trend leg) with no supply event — still a change in what the score **means**, if not in its number.
- Under CROSSING, the first scoring event is likely PALL closing below **−20%** on d200 on post-approval data (1.0pt away at 9/30).

So the two readings produce different composite paths over the window, and this is the one question that goes back to Will.

**If Will rules CALENDAR**, the charter section is a one-sentence amendment: *"On 2026-11-01 the existing levels enter the composite regardless of whether a new crossing has occurred."* Nothing else moves.

## ⏳ COT 9/29 — WAIT, not graded this spawn

The DOCKET row said the same wake would cover the 9/29 COT vintage (CFTC release Fri 10/2 15:30 ET). This write lands at ~11:48 ET; the release is 3h 42min away. My charter says a session that would WAIT hours for a scheduled print closes out and reports the armed state, so I close at the encode. **Armed state:** `cot_gold.py --expect 2026-09-29` returns WAIT today; `boot.py` leg 3 will flag it at the next MIDAS boot. **Please re-spawn** at or after 15:30 ET so the vintage lands in the same session that consumes it.

## COMPLETION BLOCK (per `PROME/COMPLETION_SPEC.md`)

- **STATUS** DELIVERED
- **CHANGED** `AGENTS/MIDAS/CLAUDE.md` § THRESHOLDS (band table + window end + day-31 CROSSING + flagged question) · `AGENTS/MIDAS/STATUS.md` (header, M2 cell, I2 cell, NEXT #3, BOTTOM LINE) · `AGENTS/MIDAS/OPEN_ITEMS.md` item 25 → CLOSED · `AGENTS/MIDAS/SCRATCH.md` (new session block) · `AGENTS/MIDAS/workbook/KB.tsv` (KB-MIDAS-121) · this receipt packet
- **RESULT** WQ-352 encoded as adopted-and-unscored through 2026-11-01 21:40 ET on the CROSSING reading; composite 8/20 unchanged; day-31 CROSSING vs CALENDAR flagged as one question back to Will.
- **GAPS** No composite effect from the ruling (that is the ruling, not a gap). COT 9/29 vintage is still WAIT (release 15:30 ET today, after this spawn). The reading question is a decision for Will; the encode does not block on it.
- **WILL_NEEDS** One question routed through this packet: **CROSSING vs CALENDAR** on day 31 with no post-approval crossing. The letter is on CROSSING per §A4's words; a CALENDAR ruling is a one-sentence amendment.
- **FOLLOW-UP** Re-spawn MIDAS at or after 2026-10-02 15:30 ET so the 9/29 COT vintage is consumed in the session that reads it. If Will rules on the day-31 question, that is a one-sentence charter amendment at MIDAS's next wake.

**Commit sha** will be included in the SendMessage receipt to `prome-96` immediately after this file commits.
