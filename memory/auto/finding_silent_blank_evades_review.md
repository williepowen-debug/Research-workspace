---
name: finding_silent_blank_evades_review
description: A defect that writes NO value survives far longer than one that writes a WRONG value — nothing is displayed to be wrong; catch it by counting blanks stratified along the dimension the defect follows
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 07d98c18-5876-41ea-b44c-48b2f9d4e407
  modified: 2026-07-27T20:43:05.261Z
---

A bug that produces a **wrong value** gets caught, because someone eventually reads it and it looks off. A bug that produces **no value** can run for months: there is nothing displayed to be wrong, and every individual run looks like a run that simply had nothing to say.

VIOLET 2026-07-27: `thresholds.py` blanked the M1:M2 front-curve column on **8 of the last 12 Mondays — the last 8 consecutively** — because the shared `vix_futures.py` CLI defaults to `today − 1 CALENDAR day`, which on a Monday is Sunday, a day with no settlements. Every Monday boot printed `UNAVAILABLE` and wrote an empty cell. It went unnoticed for two months even though the column feeds a live Convergence Matrix vector, and even though a human read that boot output every single week.

**Why:** and it went dark on exactly the session that digests the whole weekend's news flow. A silent gap is not evenly distributed — it follows whatever dimension the defect keys on (weekday, holiday, market session, locale, tenant). That is also what makes it findable.

**How to apply:**
- When a field is optional-looking or intermittently empty, do not spot-check it. **Count blanks stratified along the dimension you suspect** — by weekday, by hour, by source, by branch. The 8/12-Mondays-vs-2/11-Fridays split *was* the diagnosis; a random sample of rows would have shown "sometimes blank" and explained nothing.
- Treat `UNAVAILABLE` / `N/A` / empty in a boot or dashboard as an **assertion that must be justified**, not as neutral. Ask "when was this last non-empty, and is there a pattern to when it isn't?"
- Prefer a loud failure to a blank: a resolver that walks back to the nearest valid input beats one that gives up and writes nothing.
- Same session, same file, sibling lesson: a **hardcoded provenance label is a lie waiting for its fix.** The display asserted `"T-1 vs row date"`, which was true when written and became false the moment the fetch improved to same-day. **Compute provenance, never assert it** — see [[finding_selfstamp_estimate_drift]] and [[finding_quote_carries_data_minute]].

Related: [[finding_tool_default_asof_date_drift]] (same root cause — a CLI's default as-of date — but that variant produced a *wrong-dated* value, which is the loud version of this bug), [[finding_comprehensive_grep_over_sampling]], [[finding_fail_loud_on_incomplete_data]], [[finding_derived_surface_band_rot]].
