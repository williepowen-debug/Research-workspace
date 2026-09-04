---
name: finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit
description: "A required field filled with a POINTER to where the value lives — 'see git log', 'refresh at close', 'TBD' — satisfies every presence audit while carrying nothing the consuming check can compare. It is strictly worse than an absent field, because absence at least fails a coverage grep while this scores as COMPLIANT."
symptoms: "field is present but the check still cannot run · 'see <command>' / 'refresh at close' / 'see below' where a value belongs · coverage audit reports 100% while the consumer is starved · a MANUAL-CHECK or TBD row formatted identically to a live row · guard exists in the data and never reaches the display · compliance rate high and the downstream metric never moves · presence check passes, value check was never written · widened the inclusion criterion but not the alarm · the desks that look compliant are the ones you cannot verify · numeric cell labelled placeholder in prose · DUE recurs on a period for a single-dated item"
metadata:
  node_type: memory
  type: finding
---

**A presence audit asks "is the field there?" The consuming check asks "what does the field SAY?" A field holding a POINTER answers the first and starves the second — and because it scores as compliant, it is the one nobody re-checks.**

⛔ **This is strictly worse than the field being absent.** An absent field fails a coverage grep and shows up on a gap list. **A present-but-valueless field is invisible to the gap list AND useless to the consumer** — it converts a detectable hole into an undetectable one, while improving the compliance number.

## Worked case (NEXUS, 2026-08-28) — measured while correcting a wrong count

The `NEXUS_BRIEF` schema §4.4 defines its staleness trigger as *comparing the STATUS commit hash in the brief header to current STATUS HEAD*, and calls it **"mechanical / always fires."** Across 26 briefs:

| Class | n | |
|---|---:|---|
| A — hash present, comparable | 10 | the check can run |
| B — field absent | 12 | fails a coverage grep — **visible** |
| 🔴 C — field present, **value absent** | **4** | *"see `git log -1 -- …`"* · *"see session commit below"* · *"written this session, refresh at close"* |

**The class-C four PASS any `grep 'STATUS commit:'` presence audit and leave the check exactly as blind as class B.** ⇒ trigger (a) could not fire on **16 of 26 = 62%** of the fleet, and the owner's own three prior rollups had each concluded *"zero defects fleet-wide, the standard is working."*

⚠️ **Note what the pointers have in common: every one is TRUE and HELPFUL-LOOKING.** `see git log -1 -- <path>` is a correct instruction that a human can execute. **That is why it survives review — it reads as diligence, not as a blank.** A `TBD` would have been challenged; a working command was not.

## ⭐ The paired-failure structure — the reason a one-sided fix does not work

Found because the SAME sweep was failing in **both directions at once**, for unrelated reasons *(crystallised by LABOR, who supplied the split)*:

| | mechanism | effect |
|---|---|---|
| **False NEGATIVE** | scanner knew one token (`STATUS commit:`); three desks were compliant in three other forms — one differing **by a single colon** | 3 compliant desks flagged as defective |
| **False POSITIVE** (this finding) | field present, value a pointer | 4 broken desks scored as compliant |

🔴 **The two error classes NEARLY CANCELLED IN THE TOTAL — 15 vs 16 — while disagreeing about 7 of 26 desks.** The near-identical total is the most dangerous artifact: it is precisely the state in which a reconcile gets "settled" by adjusting a count, destroying the evidence (`[[finding_reconcile_mismatch_does_not_say_which_side_is_wrong]]`).

⛔ **A fix to either half leaves the other standing.** Widening the pattern still counts the pointer-desks as compliant; auditing for pointers still mis-flags the variant-form desks. **Both questions must be asked of any presence scan: (1) can my pattern match every legitimate FORM? (2) does a match actually carry a VALUE?** Naming half → `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]` (n=5).

## Independent corroboration, same day, different desk (DAEDALUS, 2026-08-28)

DAEDALUS reported the identical shape in **three** unrelated findings from its own window, arrived at without seeing this one: **a `⚪ MANUAL CHECK` row formatted identically to a live row** · **a tie guard present in the data and absent from the display** · **a 21-day flag that widened inclusion but not the alarm.** Its compression: ⭐ ***"presence-checks certify the wrong thing."*** ⇒ **n=7 across 3 desks in one day** — this is a class, not a schema quirk.

## How to apply

1. **Never write a presence check where you mean a value check.** `grep -L 'field:'` answers a question you do not care about. Require the **shape of the value** — `field:\s*\`?[0-9a-f]{7,40}\`?` — so a pointer fails.
2. **Make the empty state explicit and loud.** If the value genuinely is not knowable at write time, the field says `NONE (reason)` — *not* a pointer to where it could be found. **An honest blank is auditable; a helpful pointer is not.** (In the worked case the value WAS knowable: the schema's own ordering rule put the fold after the STATUS write.)
3. **Report COVERAGE AND CLASS, never a bare defect count.** "N desks lack X" hides class C entirely. Three numbers — has-value / absent / present-but-empty — or the audit misdescribes its own population.
4. ⚠️ **Suspect any compliance metric that is high while the thing it gates never fires.** That gap is the signature. Here: three rollups at "zero defects" over a check that could not run on 62% of its population.
5. **When you specify a required field, specify its VALUE FORM in the same breath** — the worked case's root cause was a schema that named a field and never named a canonical token, so no checker could have been written correctly.

**Cousins, none an exact fit:** `[[finding_record_of_an_action_is_not_the_action]]` (a pointer to where the hash lives is a record-of, not the thing — but that finding is about *records of actions*, this one about *fields in a schema*) · `[[finding_banded_threshold_with_no_metric_surface_is_untrippable]]` (same untrippability, reached by a missing metric surface rather than a hollow field) · `[[finding_silent_blank_evades_review]]` · `[[finding_parse_failure_folded_into_a_benign_bucket]]`.

*Origin: the class was raised by VULCAN as n=1 from its own desk (2026-08-21, absent-field form); NEXUS measured it fleet-wide and mis-counted it; LABOR's re-pin exposed the mis-count within the hour and supplied the false-positive/false-negative split; DAEDALUS corroborated at n=3 the same day.*

## n+1 — a VALUE-SHAPED placeholder is a pointer the parser cannot see (DAEDALUS, 2026-09-04)
My own `sweeps/REGISTRY.tsv` carried `cadence_days=7` on a one-shot dated sweep, with the playbook prose saying *"cadence_days is a placeholder so sweeps_due.py can see it — the run date is the contract."* The integer passed the presence audit (`int()` parsed it), the consumer (the cadence check) acted on it as real, and the tool fired ⏰ DUE seven days after the last run while the row's real contract (`resolve_by` 9/14) sat ten days out — I relayed the false DUE to Will at boot as a distinct weekly sweep. **The twist on the class:** the pointer here was not a string like "see git log"; it was a well-typed NUMBER whose only marker of being a placeholder lived in prose the parser never reads (kin `finding_marker_word_in_prose_disables_the_scanner_that_reads_for_it`, inverted — here the prose marker could not DISABLE the scanner, so the scanner ran on a fake). **Fix form:** give the placeholder its own typed token (`DATED`) that the parser handles by routing the row to the column that carries the real clock; a `DATED` row lacking that column is un-parseable (rc 2), never clean. **Test both paths at the artifact:** the live DUE line before the flip, the clean line after, plus past/future/no-resolve_by drills. **Symptoms:** a numeric cell described as "placeholder" or "so the tool can see it" in a nearby comment · a DUE/alert that recurs on a fixed period for an item that has a single date · a tool's "N tracked" including rows whose cadence nobody set on purpose.
