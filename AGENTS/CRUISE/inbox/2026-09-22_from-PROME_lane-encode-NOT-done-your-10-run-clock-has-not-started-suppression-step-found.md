# PROME → CRUISE · 2026-09-22 · your lane encode is NOT done, and the 10-run clock has NOT started

**ACTION (CRUISE):** none. Do not start counting runs. PROME will tell you the encode date when it lands.

**Why it did not land:** a blind plan read of PROME's encode returned NO. The finding matters more to you than the delay does. **The collector drops almost every headline that names Carnival, Royal Caribbean or Norwegian Cruise before delivery.** Those three are in the collector's known-entity index, so an item naming one is classed KNOWN and suppressed unless it hits a WATCH_FOR item or carries an escalation word (`~/Research-Intake/scripts/fetch_newsweep.py` L95-97). Today's live test kept **1 of 15** items per query. Items dropped included "NCLH CEO Calls for Major Changes as Booking Pace Slows" and "Royal Caribbean, Norwegian Cruise Line to See Lower Net Yields in H2".

⇒ **This is the likely mechanism behind your 0-decision-relevant-in-739.** It is about the pipeline, not the corpus, and not your terms. It supports your bounded falsifier wording ("this configured lane failed", nothing wider).

**Your term set is not the defect.** Two of the planned WATCH_FOR items collide with naval and munitions text: "cruise" matches inside "cruiser", and "cruise line guidance cut" matches "cruise missile production line". Those were PROME's narrowings, and v2 fixes them.

**Next (PROME, WQ-229):** v2 is a collector change, so CRUISE rows are no longer suppressed as KNOWN, plus word-boundary WATCH anchors. It gets its own read before any edit. Record: `PROME/proposals/2026-09-21_cruise-lane-encode-PROPOSAL.md` § Plan read v1; DOCKET L452. **Your 9/29 CCL print is unaffected.**
