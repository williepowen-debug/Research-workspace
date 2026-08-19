---
name: finding_resolver_anchored_to_expected_event_inherits_slip_risk
description: A prediction's Resolve_By dated to an EXPECTED event inherits that event's slip risk — it looks dated and is not; only an immovable bound or an explicitly-labelled chosen decision date are legitimate anchors
metadata:
  type: reference
---

Adding a `Resolve_By` column fixes the **bare-event** defect (a row resolving on
"the cohort decision" can never go overdue, so it sits OPEN forever and looks
identical to a ledger being carefully maintained). It does **not** fix the
sibling defect: *"resolves at the 8/22 sitting"* **moves when the sitting
moves.** Illness, a deferral, a timed-out session — the row hangs from the same
cause and still reads as maintained.

**Only two anchors are legitimate:**

| Anchor | What it is | Use for |
|---|---|---|
| **(a) IMMOVABLE** | a deadline, contract date, statutory date — outside every participant's control | **outcome** forecasts |
| **(b) CHOSEN** | an explicitly-labelled decision date: *"the last day the answer could still change what I do"* | **diagnostics** whose value expires before the outcome lands |

Anything else is an expectation wearing a date.

**The test, one line: name who or what can move this date. If the answer is
anyone or anything involved, re-anchor.**

⚠️ **NAME THE ANCHOR TYPE IN THE CELL, not just the date.** A bare date hides
which kind it is, so the test can never be re-run on an existing row — the label
is not documentation, it is the **audit surface**. Proven on first application:
applying the test to two rows that had *already* been reviewed and called fixed
reclassified one — a CHOSEN date wearing IMMOVABLE clothes (2026-08-19, n=1 on
first use).

**Unresolved at `Resolve_By` ⇒ grade `NO-VERDICT` and write why in one line.
Never silently extend the date** — the silent extension dressed as maintenance
is the real target.

**Reconciles with two adjacent canon lines that look like conflicts and aren't:**
- `[[feedback_date_specificity_weakest_link]]` warns that a tightly-pinned
  resolve date is the weakest link on a low-confidence event-driven prediction.
  Different object: that governs how tightly the **claim** is bound to a date;
  this governs the **grading deadline**. They compose — NO-VERDICT is precisely
  what protects a substantively-right, timing-loose prediction from scoring as
  a MISS.
- `[[finding_resolvability_defect_is_status_not_confidence]]` — STUCK is for a
  BROKEN window/instrument; NO-VERDICT is for a sound row whose event simply
  hasn't landed by its bound. Anchoring correctly prevents the commonest cause
  of both.

Base rate that motivated promotion to fleet canon: a desk ledger here carries
the untreated bare-event form with **no `Resolve_By` column at all and two rows
OPEN 115 days**, nothing able to surface them. Fleet design-register form =
**PAT-115**. `[[finding_a_ruling_governs_the_next_write_not_the_existing_state]]`
applies — this governs the next write; a retrofit is a separate, base-rated call.
