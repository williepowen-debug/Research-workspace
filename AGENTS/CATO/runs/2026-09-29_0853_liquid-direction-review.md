# LIQUID — finish reliable grading, then September 30 reviews

**Disposition:** September 29 advice to Will on LIQUID's morning receipt. Useful repairs, but blanket completion is premature: one date-selection defect independently reproduced; current-state/consumer reconciliation incomplete. Recommend bounded owner completion and the already-dated definition/review work, protecting publication and quarter-end observations. No LIQUID edits, dispatch, new tooling project, threshold change or approval granted. No automatic CATO follow-up.

## Scope and limits

Read LIQUID's instructions, commits `7620c7e38` and `77bda9ad9`, full gate069 script, DAEDALUS's five-ask packet, WQ-88/106/114 ruling packet, selected current STATUS/MEMORY/KB/calendar/gate rows and relevant letters. Earlier September 28 clarification closures remain closed. Entry HEAD `77bda9ad9`; master five commits ahead of cached remote, with many other owners' dirty/staged paths. No pull over concurrent work. Later owner work can supersede this snapshot.

This is a bounded review of the receipt and next-step choice, not a complete desk audit, live-market grade or broker review. Broad reads that truncated were followed by separate reads of decision-bearing rows/sections. No claim to have read all historical memory. MEMORY's 72,530-byte size illustrates the cost of carrying history in the resume file, but startup touches NEXT SESSION; size alone does not prove a whole-file read-cap breach.

## LR1 — Material: repaired daily equity leg can still grade a multi-session move

`AGENTS/LIQUID/scripts/gate069_legs.py` constructs `d` from the intersection of BB, CCC and HY dates. L4 takes `last=d[-1]`, `prev=d[-2]` for both stocks and HY. BB/CCC are L1 inputs: a missing CCC date changes L4's interval even when HY and all equity bars exist.

**Independent counterexample:** the saved [offline probe](2026-09-29_0853_liquid-gate069-probe.py) injects fixture fetches into the actual script, with no network or owner writes. September 24/25 each has a −10% stock move and +3bp HY widening; neither day meets −15% and +5bp. Complete data prints NOT FIRED. Removing only CCC's September 24 observation makes the script compare September 25 with September 23: −19% and +6bp, printed FIRED as a session move. Removing a required equity bar correctly prints INSTRUMENT-FAULT, confirming that part of the owner's repair.

**Correction/closure:** select L4's observation and previous eligible equity session independently of L1's BB/CCC intersection; require HY and each required equity close for exactly those dates. Missing input must not stretch the period. Demonstrate ordinary, missing-equity and unrelated-CCC-gap cases; also apply the consecutive-session principle when naming L1's five-session basis. No evidence this synthetic case occurred in production; the reported September 25 grade is not disproved by it.

## LR2 — Medium: implementation is ahead of effective records and delivery

New STATUS line 45 declares asks #1/#3 done. Line 51 still presents both as due; GATE-LIQ-072 at line 65 still says pin SpaceX or declare it ungradeable. CALENDAR's September 24 row and CATALYSTS row 28 lack completion annotations. `DEALER_POSITIONING_NEXUS_WATCH.md:10` repeats the broad unavailable-vintage reason by reference to the corrected kill memo. DAEDALUS ask #1 explicitly included mirrors.

PROME's GATE-LIQ-072 row still carries unpinned dates and an ungraded leg. LIQUID accurately discloses that coordinator propagation is pending; this prevents calling the whole correction delivered. Correcting OBDC's stale owed lines is useful; remaining duplicates show why the problem recurs.

**Correction/closure:** supersede contradictory live rows, annotate existing calendar/docket entries as completed where warranted, and give PROME the exact remaining registry delta through the authorized owner workflow. Retain dated history separately. Use the existing STATUS gate table as the current home; do not create another tracker or rewrite every historical mention. Separate source repair, testing, consumer update and push. The accessible-ALFRED correction does not establish that every publisher has an accessible vintage endpoint.

SpaceX's per-leg CANNOT-FIRE fits the missing-producer disposition in STATE_VOCABULARY; it is not a measured non-fire. Preserve the missed expired window and other three registered alternatives. Only the IG-index alternative has a standing producer in LIQUID's new KB note: three live legs does not mean three continuously measured legs. Describe absence of an established reachable source, not universal impossibility or a consequence of private-company status alone. No paid-data search, retrospective re-grade or successor registration recommended here.

## LR3 — Medium: tool labels contradict adopted definitions and source availability

The script's header/runtime calls the CCC-flat and HY-underperformance definitions PROPOSED, NOT ADOPTED. The September 1 WQ-114 packet adopts both prospectively. Its unconditional L2 footer says NO_INSTRUMENT even though current LIQUID/PROME records accept DTCC observations and report that separately graded CDS leg. The L1/L4 helper need not implement L2; it should say it does not evaluate it and point to the current owner grade.

**Correction/closure:** carry adopted definitions/effective dates into the helper; distinguish not evaluated here from no source exists. Preserve WQ-301(b)'s held permanent anchor rebase and sign/curve limits. Encoding an adopted definition needs no repeat approval; new outcome-changing semantics remain proposals.

## Reliable observations and verification limits

- The ALFRED correction uses a path consistent with [official FRED documentation](https://fred.stlouisfed.org/docs/api/fred/series_observations.html), which distinguishes real-time/vintage queries and initial-release output (`output_type=4`). The watcher uses that initial-release output. This verifies documented method, not LIQUID's new 195-observation census or exact API controls; those were not rerun.
- CATO counted 57 distinct observation dates in the local arrival log, June 25–September 25, with wall-clock reads later than observation dates. This supports existence of an arrival witness. The 57 value matches and 195 single-vintage results remain LIQUID-reported. First local sightings need not be first publication; sparse polling cannot exclude every intervening revision. Keep no revision observed in the checked sample, not never revised or complete intraday publication history.
- The pasted reply says Friday had not posted. Current STATUS and the logged September 25 value show Friday was available; Monday September 28 was pending at the 08:45 snapshot. Correct the observation-date wording without inventing a new data incident.
- The missing-equity-bar test passed independently. No live watcher execution, alert-delivery test or current-market refresh performed. OBDC closure was not re-audited at BROCK; this receipt does not reopen it.

## Recommended sequence and expected benefit

1. Repair LR1 and reconcile directly affected records/labels (LR2/LR3); complete ordinary delivery. A future release is not a prerequisite for reporting these repairs.
2. Combine DAEDALUS #4 with September 30's dealer-positioning review: exact NY Fed series IDs/units, frozen threshold versus contextual record, MOVE producer, reset/window basis. PROME replaced its moving-record phrase September 17; do not treat that copy as still unrepaired. Preserve WQ-88's accepted blind spot; no longer-window redesign.
3. Finish #5's calendar exclusions, rounding and reset before interpreting the quarter-end turn; finish #2's precision/ties/window basis alongside the corrected AI helper. Keep outcome-changing interpretations prospective and distinguish proposals from existing authority.
4. Grade the two due reviews on admissible observations, naming what remains unmeasurable. Protect the next HY publication and existing October 1–8 persistence reads. Leave October 31 FIRE-band research on schedule; no broad redesign or automation project.

The recurring problem in this sample is consistent operational meaning across code, letters, state and handoffs. Consolidating current state and testing a targeted counterexample should reduce false grades and repeated cleanup; productivity benefit is not yet measured. LIQUID's candor and willingness to reject its own explanations are strengths worth retaining. This advice does not commission owner work or authorize a send.

## Delivery and validation

Only this report, the offline probe and CATO continuity are authored here. The probe produced the three results above. No owner code repaired. Routine checks and exact-path Git delivery follow; final receipt belongs in-session. Other owners' concurrent work is preserved.

Validation: three offline probe cases completed as recorded; weekday claim check passed all five supplied files; continuity whitespace check passed. Orphan advisory identified only other-owner work outside CATO, including active LIQUID watcher edits; none authored by this review. Shared index contains other-owner inbox moves, preserved through exact-path CATO staging/commit. No numeric consumer migration, memory-index check or owner code suite applies: this review changes no canonical market figures, memory/auto files or operational implementation.
