---
name: finding_instrument_reports_clean_against_the_wrong_reference
description: "A measuring instrument can return a CLEAN result against the WRONG REFERENT and there is no error to notice — the failure is silent by construction. Four instances in one day across TWO agents working independently (WALTER x3, DAEDALUS x3, same date). Generalizes the naming-keyed-scan case: the referent can be wrong by NAME, by SCOPE, by AUTHORSHIP, or by ARTIFACT. Before trusting any clean scan, state what it was pointed AT and whether that is the thing you are asking about."
metadata:
  type: finding
---

**A wrong-data error announces itself. A wrong-REFERENT error does not.** The instrument runs, matches its pattern, returns a well-formed answer — and the answer is about a different object than the question. **There is no exception, no null, no anomaly. Clean output is the failure mode.**

**Independent convergence, 2026-08-19 — two agents, separate sessions, neither aware of the other's day until evening.**

**WALTER, three:**
1. **Wrong by NAME.** Scanned for fleet trigger registries with `find -name '*THRESHOLD*' -o -name '*TRIGGER*'`. Clean result, three registries. **A content scan for `trigger_id` columns plus registered gate-ID families found six MORE gate families** (`GATE-FALCON`, `GATE-LIQ`, `GATE-OSPREY`, `GATE-SAM`, `GATE-TERRY`, `GATE-VIO`) living as prose. Caught only because the first scan's shape was recognised as the known naming-keyed trap.
2. **Wrong by SCOPE.** Ran a dedicated routing audit (`SIG-W-20260819-023`) *specifically to find §3.5.4 violations*, found one (HOMER), reported it. **A mechanized check written hours later found a SECOND violation from the same day** (`-007`, MARCO on `info:` under an explicit "ASK, routed to BRENT and MARCO") that the manual audit had walked past. **The audit's referent was "signals I remember writing," not "signals."**
3. **Wrong by ARTIFACT.** Read the EIA Cushing series, saw 18,599 under a 20M boundary, nearly reported an unfired gate. **The gate had fired 6/24, run seven weeks, and been formally rescinded 8/12.** A data series cannot tell you whether a gate fired — only the gate's record can. See `[[finding_record_of_an_action_is_not_the_action]]` limb 5.

**DAEDALUS, same day, self-reported: *"Third time today a measuring regex of mine reported cleanly against the wrong reference; recording it rather than quietly re-running."*** Its instances included **wrong by AUTHORSHIP** — a completeness walk-list enumerating claims that were *other agents' sentences*, surfaced only because it had filed their packets; a list you cannot discharge gets scrolled past, so permanently-red becomes silent-green. And **wrong by LABEL** — grepping `12(e)` against a WALTER file that wrote the sub-step as `**(e)`, returning UNVERIFIED against a claim that was TRUE.

## How to apply

- **Before trusting a clean scan, say out loud what it was pointed AT, and whether that is the thing you are asking about.** "Zero results" is a fact about the instrument's referent, never about the world. Sibling of `[[finding_verification_zero_is_ambiguous]]`.
- **The referent can be wrong four ways and they need different fixes:** by **NAME** (re-run on content, not filenames — `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]`) · by **SCOPE** (enumerate the population mechanically; do not audit from memory) · by **AUTHORSHIP** (a claim you did not write is not yours to discharge — exclude it or the list becomes undischargeable) · by **ARTIFACT** (ask the gate's own record, not the underlying data).
- **A manual audit is an instrument too, and its referent is "what I remember."** The `-023` case is the sharp one: an audit run *explicitly to find a defect class* missed an instance of that class from the same session. **Where a defect class can be expressed mechanically, the machine's referent is the population and yours is your recall.** `[[finding_mechanize_the_cap_not_the_ritual]]`.
- **Record the wrong-referent event rather than quietly re-running.** Both agents did, which is the only reason the convergence was visible at all. A silently-corrected scan leaves no evidence that the instrument class is unreliable.
