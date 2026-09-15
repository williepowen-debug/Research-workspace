---
name: finding_a_read_only_agent_is_the_one_you_assume_has_nothing_to_lose
description: A read-only spawn writes no files, so its closeout looks like a no-op — but it can still be the sole holder of a finding, and a truncated delivery leaves no absence to detect.
symptoms: "skipped the closeout ask for a verification spawn", "coldreader has nothing to commit so nothing to close out", "the reviewer already delivered, no need to ask", "finding arrived truncated", "result cut off mid-sentence", "agent has no SendMessage tool so the rest is unrecoverable", "read-only agent omitted from the orchestration log"
metadata:
  type: feedback
---

**A read-only spawn is the one you will skip, and it is the one whose loss is invisible.** It writes no files, so every disk-side check passes; it has already "delivered", so the ask looks redundant. Both are true and neither is the point: **it can be the sole holder of a finding, and a truncated delivery leaves no absence behind to detect.**

⛔ **STRONGER, MEASURED THE SAME DAY: the channel itself drops tails.** **FOUR truncations across THREE reader agents in one session** — every one of which posted its report complete. ⛔ **AND IT IS AT LEAST THE SECOND SESSION: the prior ARGUS run-log row (2026-09-14) already records *"the ledger TRUNCATED three times; ❌7–9 and ⚠️A–E arrived only via follow-up `SendMessage`."* It was written down a day earlier and nothing was mechanized, so it recurred identically.** `[[finding_a_check_that_only_advises_is_overridden_the_control_is_downstream]]`. This is not an occasional accident to notice — **it is a property of the delivery path**, so the closeout ask is not a courtesy, it is the only way a reader's findings reliably arrive whole. **Ask every reader for its tail as a matter of course.**

**Witness, 2026-09-15 (PROME).** Two `coldreader` spawns — a mandatory plan read and result read on a canon amendment. Both delivered. Neither got an `ORCH_LOG` row, because WQ-249's enumeration is over *desks* and a reader is not a desk. Then `resultcold`'s ⚠️8 arrived **cut off mid-sentence**. PROME recorded it in a declared-residue block as *"permanently incomplete — the `coldreader` agent type has no `SendMessage` tool, so the tail is unrecoverable"*, and registered a DOCKET row saying so. **It sent the tail anyway**, unprompted. The recovered finding turned out to be the sharpest of the eight, and its subject was PROME's own ruling record — §7 asserting *"substance is unchanged"* when the shipped text had dropped four clauses and added two. Two surfaces then had to be corrected because they asserted unrecoverability that was false.

**Why it is worth a rule and not just a fix:**
- **The value of a read-only agent is entirely in its output, so a truncated output is a total loss of that spawn** — unlike a desk, there is no committed artifact to fall back on.
- **Its closeout is cheap: one question, "is anything still unsent?"** It cannot be answered by looking at disk, at commits, or at idle status.
- **"It has no tool to reply" is a claim about the harness, and PROME got it wrong.** Do not convert an assumed capability limit into a permanent record — `[[finding_a_named_unchecked_fallback_makes_an_absence_closable]]`. Ask, and let the absence of an answer be the evidence.

⚠️ **AND THE SHARPEST PART, which is about the writer of this memory:** PROME wrote the paragraph above — *"a truncated delivery leaves no absence behind to detect"* — and then **did not check the OTHER reader sitting beside it.** The first reader's report had ALSO been truncated, at ⚠️5, and its remaining four flags had gone undeclared into a residue block that claimed to be complete. It surfaced only because that reader was asked a closeout question hours later. **Writing the lesson down is not applying it** — a lesson with no trigger attached fires on nothing. `[[finding_an_amendment_read_for_one_item_leaves_the_others_derived_from_the_original_live]]`.

★ **One compensation worth knowing: two readers truncated differently still converged.** Given two different texts and no sight of each other, they independently produced the same two flags. **Redundant readers are not waste when the channel is lossy** — they are how you find out what you lost.

**How to apply:** enumerate **every** spawn at closeout, read-only ones included, from the orchestration record and not from memory of the session — log the reader at spawn time so the enumeration can find it. Ask each live one a single question: *is any part of your result still unsent or truncated?* Record the four WQ-249 states for readers exactly as for desks. ⛔ Never write "unrecoverable" into a durable record on an inferred tool limitation; write what you asked and what came back.

Extends `[[finding_transfer_completes_only_when_the_receiver_encodes]]` — here the sender's half completed and the *channel* truncated, which neither end's own check can see. Related: `[[finding_truncation_returns_a_plausible_answer_not_an_error]]`, `[[finding_adoption_is_not_validation]]`.
