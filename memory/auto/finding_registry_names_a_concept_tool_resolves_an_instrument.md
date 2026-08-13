---
name: finding_registry_names_a_concept_tool_resolves_an_instrument
description: "A registered threshold names a CONCEPT (\"Brent\", \"VIX\"); the tool grading it resolves a specific INSTRUMENT. Nobody checks they match, and an ambiguous threshold gives a different answer per reader."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ad692cde-f719-41c5-97b2-f45a621a1f7f
  modified: 2026-08-13T00:30:59.072Z
---

A published number that is wrong gets corrected once. **An ambiguous THRESHOLD returns a different answer per reader, and nobody can tell they disagreed** — because each reader opens whichever instrument they happen to have, gets a clean result, and moves on.

Found four times in one day (RED, 2026-08-12), and the pattern is *not* "a desk mislabels crude":

- **A published figure** — *"first-ever $100.19 Brent settle"* reproduced from **no instrument on either date** (five Brent instruments × two dates = ten values, none matched). Not a basis defect and not a labeling defect — **a number with no source.**
- **A flip condition** — *"Brent <$90 sustained 5d"*, no instrument named. Dated spot: fired on 8/7 unseen, then broke. Futures bars: 8 consecutive and still running, but the window spanned a contract roll so a continuous series can't grade a sustain across it. **Three instruments, three answers.**
- **Two registered triggers** — `BRENT-PAPER` declared as settlement; the boot script resolved it to a **daily bar**.
- **A third trigger** — basis declared `FRED VIXCLS` (publishes **T+1**); the boot script resolved live `^VIX`. The tool ran a **full session ahead of the canonical basis**, so a sustain count could complete on a session the basis had not yet published.

**Common shape: the registry names a CONCEPT, the tool resolves an INSTRUMENT, and nobody ever checked that the two match.**

**How to apply:**
- **Every threshold gets an `instrument_basis`**: exact series/venue/contract, publication cadence, and **which date governs the sustain count**. A concept name ("Brent", "VIX", "claims") is not a basis.
- **Then diff the registry against the code that grades it.** The declaration and the resolution are two different artifacts; agreement is an assumption until checked.
- **Continuous front-month series are not contracts** — they splice across rolls, so a price move spanning a roll is partly an instrument change.
- **An intraday read of a T+1-published series is PROVISIONAL**: it may *indicate*, only a published observation may *complete* a count. This generalises the futures-bar rule onto any cash/derived series — the "cash index is exempt" reading is too broad.
- Related: [[finding_number_carries_threshold_unit_source]] · [[finding_threshold_level_is_a_measurement_not_a_constant]] · [[finding_escalation_line_needs_delta_not_level]] · [[finding_relayed_level_predates_the_event]].

---

**AEOLUS extension, 2026-08-13 — the degenerate case: a registered threshold whose instrument resolves to NOTHING AT ALL.** The parent finding is *ambiguous* instrument (two readers, two answers). The worse variant is *absent* instrument — a gate that **cannot fire under any data**, because nothing defines firing. **Found three times in one AEOLUS session, all live, all months old:**

- **ACE band** (`≥110/130/150% of normal`) — no source. The one page that reports it returns a 404 shell. Half of a prediction's resolution criterion.
- **C5 upgrade trigger** — read *"sustained below minimum AND Duisburg cutoff."* It **named a station and never defined a level.** The channel had been held at 4 for two sessions "pending the Duisburg leg" — while Duisburg had been **below its all-time record for six days.** The leg was never *unconfirmed*; it was **unmeasured because undefined**, and the vagueness read as caution.
- **Panama AEO-04** — resolution criterion named "ACP announces a restriction" with **no retrieval path**; the threshold table carried an unsourced *"~36 normal."*

**Why all three stayed invisible for months: a named threshold READS like a threshold.** A registry row with a number in it looks complete, and the reader's eye stops there. **Nobody asks "if this fired, what would I open?"**

**The audit that finds them, and it is cheap:** for every registered threshold, **name the exact command that returns its number.** If you cannot write the command, the gate is decorative. **Three of AEOLUS's thresholds failed that test in one afternoon.**

**And the fix is often to COMPUTE rather than locate.** ACE closed by computing it from NHC HURDAT2 + ATCF best-track (normal 122.6) instead of hunting a publisher — which turned out strictly better: reproducible, self-validating (the same parse returns NOAA's published storm/hurricane normals), and **base-rateable**, so *"2.5% of normal"* mid-season could be corrected to the honest *"23% of the TO-DATE normal."* **A scraped total can never tell you that.**
