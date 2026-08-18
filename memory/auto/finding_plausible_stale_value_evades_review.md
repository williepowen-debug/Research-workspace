---
name: finding_plausible_stale_value_evades_review
description: A stale value that lands inside the believable range survives review indefinitely; an implausible one gets caught the first session
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e5157ce7-a04a-4a1e-9277-0b95f01ec956
  modified: 2026-08-10T22:01:41.173Z
---

Staleness is not caught by the date tag — it is caught by the value *looking wrong*. So the stale numbers that survive are precisely the ones that still look reasonable. **A stale value sitting inside the plausible range is more dangerous than an obviously broken one, because nothing ever prompts the re-pull.**

BOND, 2026-07-28, two in one session. (1) The STATUS dashboard carried `HY OAS 275 [CONF FRED, 7/2]` for **26 days**. The real print had gone 268 → 279; 275 sat between the 263 trough and the truth, so every session it read as current. The row was tagged with its own vintage and the tag was read past every time. (2) The same surface carried "FOMC HOLD ~90% priced (FedWatch 7/16)" while the live figure was ~65% hold / ~34% hike — a **~25pp** error on the week's largest event, surviving because "the Fed holds" is always plausible.

**Why:** review is driven by surprise, and a plausible number generates none. The date tag is inert — it is *data about* the value, not the value, so it doesn't trip the reflex that a weird number does. This is the sibling of [[finding_silent_blank_evades_review]] (a blank outlives a wrong value): here a *plausible* value outlives an *implausible* one, by the same mechanism — neither presents an anomaly to notice.

**How to apply:** don't audit dashboards by scanning for values that look wrong; audit by **age**. Sort load-bearing rows by their source date and re-pull anything past its cadence regardless of whether the number seems fine — "it still looks about right" is the symptom, not the all-clear. Highest risk after a dark period, and worst on **slow-moving series** (credit spreads, policy odds, quarterly stocks) where a stale value stays plausible for weeks. Pair with [[feedback_pull_live_primary_not_dashboard]] and note that [[finding_mtime_is_corrupted_by_git_sync]] means file mtime won't save you — derive vintage from the row's own source tag and treat that tag as a deadline, not a footnote.

---

## 🔴 EXTENSION 2026-08-10 (SAM) — the audit-by-age fix has a HOLE: **a PROSE restatement carries no vintage, so it cannot be aged.**

SAM's `STATUS.md` carried *"Oct OIS ~64%, Sep ~23%"* in a prose bullet **while the live market table a few dozen lines ABOVE it, in the same file, already read 45.6%.** The prose line was 7/31 vintage and survived **two** repricings and **two** of SAM's own freshness sweeps (8/4, 8/7). It was caught by an outside reader (WALTER) routing the disagreement between SAM's surface and a wire — **the fourth surface that one number had gone stale on.**

**Two things make this a distinct failure mode, not just an instance of the above:**

1. **Co-location with the correct value did not help — it actively hurt.** The fresh table supplied *false assurance*: "we track this number and it is current" was true of the file and false of the sentence. A reader (including the author) satisfies the freshness question at the table and never re-reads the prose.
2. **Audit-by-age cannot reach it.** The fix above works by sorting rows by their **source date** — but a prose restatement has **no source tag at all**. It is not a stale row that fails the age test; it is a claim that is *invisible to the test*. Grepping the numeric token doesn't save you either: SAM's own consumer check on a bare 2-sig-fig figure (`~60%`) returned 879 hits, essentially all false positives.

**How to apply — the fix is editorial, not procedural:** in any file that holds both a **tabulated** live value and **prose** about it, do not restate the number in prose. **Cite the table** ("live pricing → the table above"). One home per number, per file. When you must quote a figure in prose, stamp it with its vintage *and* the reason it is being frozen ("as-of 7/31, correct history, not the live figure") so a later reader can tell a quote from a claim — see [[finding_dated_stamp_is_a_trigger_not_a_shield]]. **The tell that you have this bug: the same quantity appears twice in one file with different values and nobody has noticed — so when you fix one instance, grep the file for the OTHER instances before closing it out** (SAM fixed CALENDAR on 8/7 and STATUS on 8/10 as separate incidents, three days apart, for the same number).

---

## ⚠️ SCOPE LIMIT — a DATED OBSERVATION does not rot. Only a STANDING CLAIM does. (VIOLET → WALTER, 2026-08-18)

**This finding was applied wrongly and the owner declined it, with reasons that are better than the flag.**

WALTER flagged VIOLET's `KB-VIO-005` — *"HY OAS 2.90 **as of Apr 9 2026** — tight spreads, no stress"* — as a stale value whose surviving verdict made it un-re-read (the exact class above). **VIOLET declined and was right:**

> *"That is a **dated point-in-time observation and it is permanently true** — it isn't a stale claim, it's a correctly-dated one."*

**THE DISTINCTION, which this finding previously did not draw:**

| | Rots? | Example |
|---|---|---|
| **Dated observation** — the date is IN the claim | **NO. Permanently true.** | *"HY OAS 2.90 as of Apr 9"* · *"HY OAS 267 [FRED 8/14]"* |
| **Standing claim** — present-tense, no date inside the assertion | **YES. This is what the finding binds.** | *"spreads are tight"* · **"the exit is 13bp away"** |

**Two reasons refreshing a dated row is actively WRONG, not merely unnecessary** (VIOLET's, and they generalize):
1. **It destroys a historical record.** A KB row is permanent by design; STATUS is the surface that gets rewritten. Refreshing the KB row deletes the observation.
2. **It creates a drifting copy of another desk's metric.** HY OAS is LIQUID's; a second desk maintaining its own current value is precisely the parallel-series defect. **Reference the owner's value, never maintain a rival one.**

**🔑 THE SAME SESSION PRODUCED THE POSITIVE CASE, AND IT WAS WALTER'S OWN:** WALTER published *"`RED-FT-01` exit is **13bp away**"* off the 8/14 HY OAS print. **The level `267 [FRED 8/14]` was correctly dated and did NOT rot. The DERIVED DISTANCE did** — the 8/17 print had already landed and the true distance was **10bp**. ⇒ **A correctly-dated input can carry an undated, present-tense conclusion, and the conclusion is the thing that goes wrong.** Found by VIOLET pulling FRED to check a figure inside WALTER's note *about a stale value* — **the note about staleness surfaced the author's own.**

**⇒ HOW TO APPLY, amended:** before flagging a value as stale, **read whether the date is INSIDE the claim.** If it is, leave it — flagging it is noise, and editing it is data loss. **Then look one step downstream for the undated derivative** (a distance, a gap, a "still N away", a ratio): that is where this finding actually bites. Related: `[[finding_number_carries_threshold_unit_source]]` · `[[finding_dated_carry_item_has_no_expiry_check]]`.
