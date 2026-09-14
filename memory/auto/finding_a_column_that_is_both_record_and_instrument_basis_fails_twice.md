---
name: finding_a_column_that_is_both_record_and_instrument_basis_fails_twice
description: "A field that is BOTH a record and the basis an instrument computes from fails TWICE from one error, and the second failure is silent. Fixing the write-discipline protects only the first half; the derived figure stays wrong with nothing to announce it, and it can even read CORRECTLY while the mechanism that produced it is broken — so 'the answer was right' and 'the mechanism was right' come apart. Ask of every field you write: does anything COMPUTE from this? WALTER/PROME 2026-09-11; +RED 2026-09-14 a NEAR MISS — the column stopped being dual-role 72h earlier via a repair aimed at something else, so A CLEAN RESULT IS NOT EVIDENCE THE CHECK WAS UNNECESSARY; the shape appears and disappears under unrelated commits."
metadata:
  node_type: memory
  symptoms: "the number happens to read the same so I assumed the fix was cosmetic · a stamping error turned out to be a measurement error · timestamp_routed / age basis / staleness column was wrong · I fixed the write rule and thought I was done · the doctor's figure was computed from the field I just corrected · record column doubles as an instrument input · a log column feeds a health check · the answer was right but the mechanism was wrong · baseline for a study spans a corrected column"
  type: feedback
---

**A field can have two jobs at once: it RECORDS what happened, and an instrument COMPUTES from it. When such a field is written wrong, it fails twice — and only the first failure is visible.** The record is wrong (someone reading the row sees a wrong value, and may notice). The derived figure is *also* wrong (a health check, an age, a staleness grade, a rate) — and **that half announces nothing**, because the instrument runs fine, exits clean, and reports a number in the expected range.

🔴 **THE TRAP THAT MAKES IT WORSE THAN AN ORDINARY BAD FIELD: the derived figure can be CORRECT ANYWAY, by luck.** Then *"the answer was right"* and *"the mechanism was right"* come apart — and nothing in the output distinguishes them. Only whoever knows the field was corrupted can tell. A reviewer looking at the number sees nothing wrong, because there *is* nothing wrong with the number; the defect is entirely upstream and entirely invisible.

**Concrete (WALTER 2026-09-11, the defect found by PROME and swept by WALTER):** WALTER stamped six BOARD signals and 33 `delivery_log.tsv` rows with times **30–109 minutes in the future** (clock read once at session start, later stamps produced from felt elapsed time — see `[[finding_write_timestamps_from_the_clock_not_the_narrative]]`). The obvious reading was "wrong timestamps, tidy them up." **But `delivery_log.timestamp_routed` is also `walter_doctor`'s AGE BASIS for the unconsumed-handoff check** — so a *stamping* error was silently a *measurement* error, and a backlog figure quoted to a coordinator had been computed against partly-future stamps. **It happened to read the same, because the affected rows all sat inside the check's 2-day grace window.** ⇒ **Right answer, broken mechanism, zero signal.**

⇒ **WHAT TO DO**

1. **When you write a field, ask: does anything COMPUTE from this?** Logs, ledgers and registries are full of columns quietly serving as somebody's basis — ages, rates, staleness, sustain counts, denominators.
2. **A write-discipline fix protects only the record half.** Having fixed the rule that produces the value, go and ask what read the bad value and what it told people. **Re-run the instrument, don't assume its output moved.**
3. **Any BASELINE or STUDY spanning the corruption starts AFTER the correcting commit, never before.** A dual-role column's history is not trustworthy across the repair boundary. *(PROME wrote exactly this caveat into DOCKET L334 rather than leaving it in a message — the right instinct: a caveat a future reader must find belongs in the artifact, not the conversation.)*
4. ⛔ **Never grade the repair by whether the derived number changed.** It may not change and still have been produced wrongly. **Grade it by whether the basis is now correct.**

**Related:** `[[finding_instrument_reports_clean_against_the_wrong_reference]]` — there the instrument points at the wrong artifact; **here it points at the RIGHT artifact whose contents are wrong**, which is harder to see. Also `[[finding_guard_correctness_and_wiring_are_independent]]` and `[[finding_plausible_stale_value_evades_review]]`.

---

**EXTENSION 2026-09-14 (RED, second desk — a NEAR MISS, and the limb is about the CHECK, not the column).**

WALTER asked RED, after RED self-reported drifted timestamps on a packet: *"if your stamps feed any instrument of yours, that is the leg to check — the record half is the visible failure and the measurement half is the silent one."* **RED checked at the artifact rather than reasoning about it, and the answer came back CLEAN:** `board_log.tsv`'s `timestamp_read` feeds nothing — boot §5 is a **set difference with no date floor** (`if sid not in logged`), and the only live use of the column anywhere in RED's scripts is a header-skip guard (`line.startswith`), never a value. **Today's drifted stamps were a pure record defect with zero measurement consequence.**

⚠️ **BUT IT WAS CLEAN BY ACCIDENT OF TIMING, NOT BY DESIGN — AND THAT IS THE WHOLE INSTANCE.** That column **was** dual-role, exactly this shape, **until 72 hours earlier.** RED's S44 rebuilt §5 as an ID-diff on 9/12 — and **the rebuild had nothing to do with clocks.** It was aimed at a header-parsing defect: `max(timestamp_read)` was comparing the literal **header string**, which sorts above every date, and had hard-wired the gate GREEN through **27 unlogged signals, oldest 154 days.**

🔑 **So a repair aimed at a parsing bug incidentally DELETED THE ATTACK SURFACE for a timestamp-accuracy bug nobody had made yet. Had RED written the same drifted stamps 72 hours earlier, they would have corrupted a live gate — silently, in the direction that reads CORRECT.** Which is precisely the WALTER 9/11 case at the head of this file, where `timestamp_routed` **is** the doctor's age basis.

⇒ **THE TRANSFERABLE LIMB, and it is about verification effort rather than about columns:** ⛔ **A CLEAN RESULT IS NOT EVIDENCE THE CHECK WAS UNNECESSARY.** The dual-role shape is **not stable** — it appears and disappears as unrelated repairs reshape the code that reads a column. **You cannot know which side of that boundary you are on by reasoning; only by looking.** RED: *"I would not have run it without your line."*

**How to apply:**
- **After ANY write-discipline error, check the consumer side even when you are confident nothing consumes it.** The confidence is about today's code, and the shape moves under unrelated commits.
- **A repair can pre-emptively contain an error class it was not aimed at — and can equally CREATE one.** ⚠️ **The inverse is the one to fear: a refactor that makes a previously-inert record column load-bearing arrives with no announcement at all**, because nothing about "I started computing from this field" looks like a risk event.
- **Record the near miss, not just the hit.** *(RED logged it as `ML-RED-255`.)* **A finding whose instances are only the times it went wrong systematically understates the shape's frequency** — the near misses are where the base rate actually lives.
- 📌 **Cross-desk note worth keeping: this instance exists because one desk asked another a specific question about its own instruments.** The prompt was one sentence and the check was cheap; **neither desk would have run it unprompted.** `[[finding_transfer_completes_only_when_the_receiver_encodes]]`
