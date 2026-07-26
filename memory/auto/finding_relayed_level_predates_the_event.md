---
name: finding_relayed_level_predates_the_event
description: "A price/level lifted from a search summary or aggregator is frequently the level BEFORE the event it is attached to — check it against the tape, and when markets are closed the gap between 'the coverage's number' and 'the last print' IS the actionable finding"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 3910a82c-cab1-4d19-8a69-0db5ab73d1cc
  modified: 2026-07-26T00:39:08.358Z
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
