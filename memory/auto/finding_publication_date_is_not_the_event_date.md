---
name: finding_publication_date_is_not_the_event_date
description: "A dateline is when it was PRINTED, not when it HAPPENED — and a weekday that disagrees with its date is not a typo, it is the detector telling you two different dates are in one sentence. Usually the weekday names the event and the number names the publication. Resolves cleanly against finding_date_gate_beats_weekday_name: DROP the weekday when you author, KEEP it when you read."
metadata: 
  node_type: memory
  type: finding
  originSessionId: 5c0fd258-4a11-40d6-b25c-371cd07589e0
  modified: 2026-08-21T14:46:22.577Z
---

**A publication date is not an event date, and the gap is almost always exactly +1 day** — an evening post, statement, capture or filing, reported the following morning. Never random, never large, which is why it survives every review.

**⇒ THE DETECTOR IS FREE AND ALREADY IN THE TEXT: when a source's WEEKDAY disagrees with its DATE, two different dates are in that sentence.** Reporters write *"Trump said **Wednesday**"* about the thing that happened; the CMS stamps the day it shipped. **So the weekday usually names the EVENT and the number usually names the PUBLICATION.** A mismatch is not sloppiness to note in passing — it is the answer.

**BRENT, 2026-08-21 (n=5 on this desk).** Reported to the operator that Trump's *"ECONOMIC D-DAY"* post was **8/20**, sourced to a USA TODAY article. **The post was Wed 8/19 ~19:55 EDT**; 8/20 was the article's publication date. ⛔ **The fetch had returned *"Date: August 20, 2026 (Wednesday, per article)"* — and 2026-08-20 is a THURSDAY. The mismatch was noticed, written down as a minor aside, and not chased.** The prior four instances (2026-08-17) were Bloomberg pieces *dated* 8/12 and 8/13 whose own text read *"a satellite image … captured **Tuesday**"* / *"captured **Thursday**"* ⇒ observations 8/11 and 8/13, logged across four surfaces as the publication dates.

**Guards:**
- For every dated claim entering a state file, ask the one question: **"is this when it HAPPENED or when it was PRINTED?"** If the source does not distinguish them, the claim carries **two** dates and you must record both.
- **A dateline is publication. A verb tense is the event.** *"said Wednesday"* is an event date; *"August 20, 2026"* at the top of the page is not.
- Highest-risk surfaces: incident ledgers, catalyst rows, falsifier windows, and anything grading a threshold against a named survey week — all of which resolve on the EVENT date and will silently mis-grade on the publication date.

**★ IT RESOLVES CLEANLY AGAINST [[finding_date_gate_beats_weekday_name]], WHICH SAYS THE OPPOSITE ABOUT THE SAME FIELD — and the reconciliation is the useful part.** That finding says **DROP** the weekday from anything operative, because a day-name *you* author is a second unchecked assertion that propagates at full confidence. This one says **KEEP** the weekday on anything *inbound*, because a day-name *someone else* wrote is a free checksum on their own date field.

**⇒ OUTBOUND: drop it — you are the author and it can only add error. INBOUND: keep it — you are the reader and it can only reveal error.** Same field, opposite treatment, decided entirely by which end of the pipe you are on.

Related: [[finding_write_timestamps_from_the_clock_not_the_narrative]] (the clock-side sibling — a time you infer reads as measured) · [[finding_a_charitable_reading_of_your_work_is_the_one_to_check]] (the mismatch got the flattering reading: "sloppy article", not "I have the wrong date").
