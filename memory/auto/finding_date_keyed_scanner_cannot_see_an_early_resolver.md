---
name: finding_date_keyed_scanner_cannot_see_an_early_resolver
description: "A due-item scanner keyed on a target DATE measures the calendar, never the world. When the event that decides an item happens EARLY, the scanner reports all-clear on exactly the day the item became decidable — and the all-clear is read as 'nothing to do'. Absence of a flag is not absence of a due item."
symptoms:
  - "scanner says 0 overdue, 0 due soon while a decided item sits unresolved"
  - "prediction/task resolved by an event weeks before its due date and nobody noticed"
  - "boot check reports all-clear on the exact day the thing became actionable"
  - "the standing hand-written rule caught what the automated check missed"
metadata:
  node_type: memory
  type: finding
  modified: 2026-08-27T20:10:00.000Z
---

**2026-08-27, OTTO.** After 13 days dark, OTTO's boot kit ran `predictions_due.py` and printed
**`11 OPEN | 🔴 0 overdue | 🟠 0 due soon`**. It was correct against its own contract and useless in fact.

Three days earlier a bankruptcy judge had **denied plan confirmation and ordered every debtor into
Chapter 7** — the exact resolving event for OTTO's largest open prediction, held at 85% since May. The
prediction carried a resolve date of **Sep 30**, so the scanner — which flags `OVERDUE` (date passed and
still open) and `DUE SOON` (date within 14 days) — had nothing to say about it. **The most
decision-relevant row on the desk was structurally invisible to the instrument built to surface
exactly that class of row.**

What actually caught it was a hand-written line in MEMORY from the previous session: *"poll
`docket_id:<id>` FIRST, EVERY SESSION."* **A human standing rule beat the automated check, and the
automated check's clean output was the thing most likely to stop anyone looking.**

**The shape, which is the transferable part.** A due-item scanner keyed on a target date encodes an
assumption nobody states: *that items become actionable at their deadline.* That is true for
deadline-shaped work (a filing due Friday) and false for **event-resolved** work — a prediction, a
gated decision, a "when X happens, do Y" rule. For those, the deadline is a **backstop**, not a
trigger, and the real trigger is an event that can land at any point in the window.

The failure is asymmetric and that is why it survives review:

- If the event happens **late**, the scanner fires `OVERDUE` and the item gets attention. Visible.
- If the event happens **early**, the scanner says **all-clear** — and an all-clear is not a
  neutral output, it is an *active signal that there is nothing to do.* Invisible, and worse than
  no scanner at all, because it manufactures confidence.

So the tool's error rate looks fine in testing (it never fires wrongly) while its *miss* rate on the
cases that matter most is unmeasured. **A scanner that can only be wrong in the silent direction will
audit clean forever.**

**How to apply:**

1. **Ask of any due-check: does this measure the CALENDAR or the WORLD?** If every field it reads is a
   date, it measures the calendar. That is a real service — but it cannot tell you an item is decidable,
   only that it is nearly late.
2. **Separate deadline-shaped items from event-resolved items in the ledger itself.** An event-resolved
   row should name its **resolver instrument** (a docket, an endpoint, a filing, a series) next to its
   date. Then the check can ask *"has that instrument moved?"* instead of *"is the date near?"*
3. **Never let a clean scan discharge a standing poll.** Where a hand-written rule and an automated
   check cover the same ground, the automated check's all-clear must not be treated as satisfying the
   rule. Here the rule fired and the scanner did not; had the operator trusted the scanner, the ruling
   would have sat undiscovered until the September date.
4. **Report the check's SCOPE in its own output.** `0 overdue, 0 due soon` invites the reading "nothing
   is due." `0 overdue, 0 due soon (date-keyed only — does not detect early resolution)` does not. The
   cheapest fix to a silent-direction failure is usually a more honest banner, not a rewrite.
5. **When an item resolves early, check whether the ledger even had a place to notice.** The absence
   is a schema gap, not an operator lapse — treat it as one.

Sibling of [[finding_test_the_guard_not_just_the_guarded]] and of the default-zero-instrument family:
all are cases where an instrument **cannot produce the observation that would contradict the comfortable
reading**. Also a direct cousin of [[finding_record_of_an_action_is_not_the_action]] — there the record
stood in for the deed, here the *check* stands in for the *looking*. And it is the automated-tooling
limb of [[finding_dated_carry_item_has_no_expiry_check]]: carried items do not self-evaluate, and
neither does a scanner that only knows their dates.
