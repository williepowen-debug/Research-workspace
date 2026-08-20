---
name: finding_impeachment_must_be_scoped_to_the_claim_not_the_source
description: "Retiring a source retracts every claim it carried, but the evidence usually refutes only ONE (the level, not the change, not the parse) — enumerate what the source was used FOR and invalidate per use."
metadata:
  type: feedback
---

**A stored reading is not one claim, it is at least three: the LEVEL, the day-over-day CHANGE, and the PARSE.** Evidence against one does not touch the others. **Impeaching the SOURCE retracts all of them, and the ones you did not mean to kill die silently** — because a guard firing correctly and a guard firing too widely look identical from the console.

**Incident (SAM, 2026-08-20).** A peer found `BOJ_OIS.tsv` publishing a central-bank-pricing figure from an aggregator SAM had just declared dead — `quality: ok`, timestamped ~30 minutes *before* the packet retiring it, so **the dead number was the freshest-stamped, cleanest-flagged, only machine-readable one SAM published, and the do-not-cite existed only in packet prose.** SAM re-stamped all 24 of that source's rows non-`ok` and patched the writer so future pulls would stamp themselves.

**That fix broke something the evidence never spoke to.** The reader `prior_curve()` filters `quality == "ok"` to build the comparison baseline, so re-stamping every row **silently emptied it and blanked the "vs prior" delta column** (previously `+1.2pp`). No error, no warning. **The defect was in MEETING ATTRIBUTION — it refutes the LEVEL and says nothing about whether yesterday-to-today moved 1.2pp.** An impeached row is an *accurately-parsed reading of a defective source*, not garbage.

**A second scoping error in the same fix, opposite direction:** the good replacement figure was added as a row dated three days earlier than the file's newest row, on a series labelled FALLING. ⇒ **the only citable value became the OLDEST observation in the file, precisely because the newer rows were the impeached ones** — "dead number wearing a fresh timestamp" replaced by "live number wearing a stale one."

**Why:** impeachment feels like a safety action, so it is applied generously and reviewed lightly — and *over*-retraction produces no error, no failing test, and no complaint. It just quietly removes capability. The blast radius is invisible because the reader keys on the **row**, not on the **claim**. There is a second trap attached: **the instrument you flee to deserves the audit you gave the one you left.** Here the replacement derivation had *three* defects worse than the source it replaced, and it got less scrutiny because it arrived carrying the credibility of the correction — **having just been right about something makes the next number harder to doubt, exactly when it deserves more doubt.**

**How to apply:**
1. **Before invalidating a source, enumerate what it is USED FOR and invalidate per use.** Grep the readers. Ask of each: *does my evidence actually refute this use?* Level-vs-change is the most common split; parse validity almost never dies with the level.
2. **Express the impeachment where the consumer reads, not where you write.** Prose in a packet stops nobody. Stamp the row, patch the WRITER (or the next pull re-creates it), and check the CONSOLE separately — the human-facing display often reads a freshly-parsed value and never touches the stored cell you just fixed.
3. **After any impeachment, re-run the tool and diff the output.** The regression here was one blank column. **A capability that vanishes without an error is the signature of an over-scoped guard** ([[finding_guard_correctness_and_wiring_are_independent]]).
4. **Give the replacement its own staleness and provenance check** — an observation date, a last-traded date for a market mark, and a re-pull instruction. Do not let "best available" render as "current."
5. **Audit the instrument you flee to at least as hard as the one you left** ([[finding_agreement_at_one_date_can_be_cancelling_errors]], [[finding_rejecting_an_instrument_is_an_audit_of_it]]).

Related: [[finding_claim_outlives_its_discredited_instrument]] (the mirror: instrument fails ≠ claim false) · [[finding_single_witness_guard_deletes_real_data]] · [[finding_standing_guard_is_a_false_negative_risk]] · [[finding_a_ruling_governs_the_next_write_not_the_existing_state]]
