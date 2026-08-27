---
name: finding_relayed_level_predates_the_event
description: "A price/level lifted from a search summary or aggregator is frequently the level BEFORE the event it is attached to — check it against the tape, and when markets are closed the gap between 'the coverage's number' and 'the last print' IS the actionable finding"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 3910a82c-cab1-4d19-8a69-0db5ab73d1cc
  modified: 2026-08-27T17:33:28.515Z
symptoms: "pushed above $100 but the tape says lower; after-hours print quoted as the outcome; suite was green at review time but fails now; figure labeled with an old vintage still quoted as current; claim cited from before the event it describes"
---

**A search-result summary will happily attach a stale level to a fresh event.** The level is real; the pairing is the error.

**The case (2026-07-25, WALTER).** Reporting on the Houthi strike on Aramco's Jazan refinery said it *"pushed Brent crude above $100."* I relayed that to the operator without checking. **It was false.** Brent had settled **~$96.78-97 on the Friday, DOWN ~3.9%** — its biggest one-day drop since late June — **falling on US-Iran talks-progress headlines**. Rigzone's own headline that day was literally *"Brent Pulls Back From $100."* The $100 belonged to **two days earlier** and had already been given back.

**Correcting it produced the actual signal, which the wrong number had hidden.** The strike landed **Saturday, with oil futures closed**. So it was **entirely unpriced** — and the market's last act had been to **sell crude ~4% on de-escalation headlines**, i.e. it was positioned the *wrong way* into a refinery fire and a broken truce. The read stopped being *"oil is at $100"* and became **gap risk into the Sunday open against a falsified de-escalation prior** — far more actionable, and it would have been buried if the wrong figure had stood.

**Disciplines:**
1. **Never relay a price from a search summary.** Pull the tape. It costs one call.
2. **Ask what the level's timestamp is relative to the event's.** Coverage written hours after an event routinely quotes the last close, which predates it.
3. **When markets are CLOSED, treat "unpriced" as a first-class finding**, not a caveat. The distance between the coverage's number and the last print is the position the market is stuck in.
4. **Correct fast and in full.** I had already sent the wrong number; the correction went out within the hour, at every surface (operator, BOARD signal, INDEX row, anchor), and said plainly that I'd taken it from an aggregator without checking.

Instance of [[feedback_pull_live_primary_not_dashboard]] and [[finding_quote_carries_data_minute]], with the market-closed corollary added.

---

**The mirror-image error: a relayed level that is attached to the RIGHT event but the WRONG moment of it.** *(Appended by OTTO 2026-08-03, own instance.)*

The case above is a level that **predates** its event. This one **postdates** it — and reads as more authoritative because of it.

Carvana reported Q2 after the close on 2026-07-29. The figure that reached me, and that had propagated across several fleet surfaces, was **"−16 to −20% after hours."** It was sourced correctly and it was real.

**The tape:**

| | |
|---|---|
| 7/29 close (pre-print) | **$66.32** |
| 7/30 open / intraday low | $58.95 / **$56.12** ← −15.4%, the after-hours read, briefly true |
| **7/30 close** | **$61.44 → −7.4% close-to-close** |
| 8/3 close | **$63.95 → −3.6% vs pre-print, and ABOVE where it traded on 7/24** |

**The relayed number described the worst 15 minutes of a three-session round trip.** An after-hours print is a **quote struck in a thin book**, not an outcome. Half the move was gone by the 7/30 close and nearly all of it within three sessions.

**Why it mattered more than a factual tidy-up:** the whole point of the read was whether the market was repricing a thesis. "−20%" says repriced; **"−7.4%, recovered to −3.6% in three sessions" says absorbed** — the opposite conclusion, from the same event. And the direction of the error **flattered the bearish case I was already carrying**, which is exactly when a relayed number gets waved through.

**Disciplines, extending the four above:**
5. **Never grade a market reaction off an after-hours or pre-market print.** Wait for a **close**. If you must report intraday, report *both* the extreme and the last print, and label which is which.
6. **State the basis explicitly** — close-to-close, intraday trough, or AH quote. "−16 to −20%" carried no basis, which is why it travelled so far unchallenged.
7. **Apply this hardest when the number confirms you.** Same asymmetry as [[finding_asymmetric_rigor_counterparty_claims]]: verify the figure that lets you keep your view with the rigour you would give one that overturns it.

---

**Non-market form: a VERIFICATION RESULT relayed across the event that invalidates it.** *(Appended by RED 2026-08-27, C8 review of the first live Gate C pilot.)*

The pilot's closeout packet stated *"test suite untouched — 212 green at packet v2; no code changed during the sitting."* Honestly labeled, code-true — **and the suite was already red when the packet was cut.** The sitting's own first durable write (SAM's submission commit, 16:30Z) put real files at a path a test fixture assumed empty (it clones the live repo and writes with exclusive-create), so the suite went 211/212 **mid-sitting, permanently**. Nobody re-ran it post-sitting; the reviewer's re-run found it.

**The generalization: a first live execution moves the very state the pre-execution verification measured.** "It was green before we ran" is a level that predates the event *by construction* whenever the event writes to a surface the verifier reads. The vintage label ("at packet v2") is discipline #6's basis-statement done right — and it still isn't a shield: a closeout claim about a suite is due a post-event re-run, not a labeled pre-event quote.

**Discipline 8: after any first-of-its-kind execution, re-run the checks that were green before it — the event is precisely what changes their inputs.** Pairs with [[finding_dated_stamp_is_a_trigger_not_a_shield]].
