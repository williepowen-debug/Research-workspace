---
name: finding_a_warning_dated_on_its_own_event_fires_too_late
description: "A staleness/expiry date set TO the event it warns about makes the alert fire the day AFTER the event. The mechanism works, the check runs green, the date is 'correct' — and the warning arrives one tick past the moment it existed for. Distinct from a carried claim nobody evaluates: here something DOES evaluate it, on the wrong side of the line."
symptoms: "the alert fired but the thing had already happened" | "Stale_By is the same date as the event" | "the warning was right and useless" | "review_by lands on the day the window closes" | "the check is green until the moment it stops mattering" | "we got told the day after the roll"
metadata:
  node_type: memory
  type: feedback
---

**A warning dated on its own event is not a warning — it is a post-mortem with a scheduler.**

HANS, 2026-09-18: it registered two facts warning that generic gas tickers roll (`KB-HANS-079/081`) and set their `Stale_By` to **9/29 and 9/28 — the roll dates themselves**. Boot flags facts **past** their `Stale_By`, so the alert would have fired **the day after** each roll. It pulled both forward to 9/25 and mechanised it rather than remembering it.

**Why this evades every check.** Nothing is broken. The fact is registered, the date cell is populated, the boot check runs and is correct, and the date is even *defensible* — it is exactly the date the fact stops being true. `[[finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit]]` is the neighbour: presence is satisfied, correctness is not tested. A reviewer reading the row sees a warning with a date on it and moves on.

⚠️ **Distinct from [[finding_dated_carry_item_has_no_expiry_check]]**, and do not merge them. There, nothing evaluates the carried claim at all. Here something **does** evaluate it, faithfully, **on the wrong side of the line**. The failure is an off-by-one in the alert's own date, not an absence of machinery. A fix for one does not fix the other.

**The test, cheap enough to run at write time:** *when this date arrives, is the thing it warns about still preventable?* If the answer is no, the date is wrong — set it to the last moment action still changes the outcome, not the moment the world changes. Applies to `Stale_By`, `review_by`, `needed_by`, expiry-dated allowlist rows, and any gate whose `review_by` lands on the day its own window closes.

**Generalises past dates:** the same shape is a threshold set at the level where the loss is already taken, and a resolver whose observation window opens after the event it resolves. `[[finding_guard_scope_expires_at_the_fill]]` is that family. Ask which side of the event the instrument sits on, always — the date being *accurate* is what disguises it.
