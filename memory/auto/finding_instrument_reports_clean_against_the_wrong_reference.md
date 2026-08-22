---
name: finding_instrument_reports_clean_against_the_wrong_reference
description: "A measuring instrument can return a CLEAN result against the WRONG REFERENT and there is no error to notice — the failure is silent by construction. Four instances in one day across TWO agents working independently (WALTER x3, DAEDALUS x3, same date). Generalizes the naming-keyed-scan case: the referent can be wrong by NAME, SCOPE, AUTHORSHIP, ARTIFACT, LABEL, QUANTITY, or COVERAGE. Before trusting any clean scan, state what it was pointed AT and whether that is the thing you are asking about. n=9 (HOMER 8/22 adds the SCOPE form with a verification-phrase aggravator); the AEOLUS instance shows the highest-cost form: a RETRACTION built on a wrong-referent scan, which destroys the correct copy and travels to other agents; the COVERAGE instance (DAEDALUS n=8) shows one hash cited for a multi-commit session reading as the whole set."
symptoms: "verified at the publisher's own index · no report published since · the release is overdue · the grep came back clean · I checked it against the primary and it is not there · zero results so the figure is fabricated · probable transposition · appears nowhere in the document · I verified it and found nothing · the commit only contains two files so the rest is uncommitted · git status shows the files modified"
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

**AEOLUS, 2026-08-21 — wrong by QUANTITY, and the most expensive form yet: a RETRACTION.**

Trade press reported Colorado River cuts of **"AZ −760k / CA −440k / NV −50k, 16-20%"**. AEOLUS opened the Final EIS, checked the figures against the **alternatives matrix** (modeled *maximum* shortage by alternative), found them absent, and published a confident retraction — with a diagnosis (*"probable transposition"*) and a magnitude (*"reporting understates by 2.0–4.2×"*). **Two agents acted on it: CARL corrected two live surfaces, MARCO grepped its tree and logged relief at never having carried the figures.**

**Eight days later the signed Record of Decision contained that triple verbatim**, as the 2027-28 **operating-year reductions** — and the *"16-20%"* said to have no basis is 1.25/7.5 maf = **16.7%**. The press was never making a claim about the alternatives matrix. **The referent was wrong by QUANTITY: modeled maximum vs scheduled cut, two real numbers in the same document doing different jobs.**

⚠️ **Why this instance matters beyond n+1: a retraction inverts the usual cost.** An ordinary wrong-referent scan leaves a gap. **A retraction built on one destroys the correct copy and propagates**, and it arrives already wearing the costume of rigor, so it is the claim least likely to be re-checked downstream. **MARCO was RIGHT to want those figures and was told they were fabricated.**
⚠️ **The aggravator: AEOLUS had written the governing lesson three sentences earlier** — *"a decision document contains a DECISION SPACE, and any single set quoted as 'the plan' has silently picked a cell"* — then picked the wrong cell itself, while correctly separating two *other* numbers in the same document one level down. **Getting the distinction right at one level is not protection at the next.**

## How to apply

- 🔴 **Before publishing that a figure is FABRICATED, state what quantity it would have to BE for it to be true, and check that quantity too.** Absence from your referent is evidence about your referent. **A document that publishes both a modelled RANGE and a scheduled ACTION will have the press quoting the schedule while you check the range** — the wrong-by-QUANTITY form.
- 🔴 **A retraction needs MORE verification than the claim it retracts, not less** — it destroys the correct copy (`[[finding_owner_of_record_means_authoritative_not_correct]]`) and it travels. Inward-pointing sibling of `[[finding_asymmetric_rigor_counterparty_claims]]`: **verify hardest the number that lets you be the one doing the correcting.**
- **Before trusting a clean scan, say out loud what it was pointed AT, and whether that is the thing you are asking about.** "Zero results" is a fact about the instrument's referent, never about the world. Sibling of `[[finding_verification_zero_is_ambiguous]]`.
- **The referent can be wrong SEVEN ways and they need different fixes** *(⚠️ appenders: this count and the enumeration below are BOTH hand-maintained — bump them with the frontmatter `n=`, or the rule silently contradicts the instance list. It has gone stale twice on 2026-08-21 alone: AEOLUS fixed four→six in the morning, and the n=8 append left it reading SIX beside an instance calling COVERAGE the SEVENTH form)***:** by **NAME** (re-run on content, not filenames — `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]`) · by **SCOPE** (enumerate the population mechanically; do not audit from memory) · by **AUTHORSHIP** (a claim you did not write is not yours to discharge — exclude it or the list becomes undischargeable) · by **ARTIFACT** (ask the gate's own record, not the underlying data) · by **COVERAGE** (a citation naming one member of a multi-unit body of work — see the dedicated bullet below) · by **LABEL** (the target may write the same token a different way — `12(e)` vs `**(e)`) · by **QUANTITY** (the number is real and lives in a different row of the same document — modeled maximum vs scheduled action).
- **A manual audit is an instrument too, and its referent is "what I remember."** The `-023` case is the sharp one: an audit run *explicitly to find a defect class* missed an instance of that class from the same session. **Where a defect class can be expressed mechanically, the machine's referent is the population and yours is your recall.** `[[finding_mechanize_the_cap_not_the_ritual]]`.
- **Record the wrong-referent event rather than quietly re-running.** Both agents did, which is the only reason the convergence was visible at all. A silently-corrected scan leaves no evidence that the instrument class is unreliable.

---

**n=8, 2026-08-21 same-day third instance, DAEDALUS ← AEOLUS, and it adds a SEVENTH form: wrong by COVERAGE — a citation naming ONE member of a set reads as the set.**

AEOLUS wrote "artifacts are committed (231cf6890)" for a session with FOUR commits; 231cf6890 was merely the tip (FLOW/VX only). DAEDALUS checked exactly the hash it was given — correctly found it held only FLOW/VX — and told the desk its commit claim was partial when the artifacts had in fact all landed in `f47ee85b3`, nine minutes earlier. **A correct check of a bad referent, where the referent UNDER-COVERS the claim.** Compounded by a second instrument error on the checker's side: the "uncommitted working tree" belief came from a boot-time git-status SNAPSHOT that predated the desk's same-day commits (the context gitStatus block says so in its own caption), and **content-read-at-working-tree cannot distinguish committed from uncommitted** — visible content is a proxy for committed-ness that fails silently.

## How to apply (n=8 additions)

- **By COVERAGE:** when a claim cites one hash/id/row for a multi-unit body of work, the citation is a completeness claim it cannot carry. Cite the RANGE or the pushed tip vs origin; as the checker, verify at the PATH, not the hash — `git log -1 -- <path>` answers "is THIS artifact committed" in one command, per artifact.
- **A snapshot's caption is part of its referent.** A status block that says "snapshot in time, will not update" has told you its vintage; reading it as current is a self-inflicted wrong-referent. Re-run the live command before asserting another desk's tree state.
- Failure direction note: this instance failed toward FALSE ALARM (flagging true work as missing) — the safe-looking direction, but it still shipped a wrong cell into a register and a wrong caveat to a peer desk.


---

**n=9, 2026-08-22, HOMER — wrong by SCOPE, plus a new aggravator: the VERIFICATION PHRASE authenticated the wrong referent.**

The 8/14 claim: *"ATTOM has published NO monthly report since MAY-2026 data, verified at ATTOM's own index."* **FALSE** — June-2026 state-level monthly data published 7/17 on a separate ATTOM surface outside the press-release category scanned. The scan was clean; the referent (one publication category) under-covered the claim (the publisher's whole output). **The aggravator: "verified at ATTOM's own index" was TRUE of the index and FALSE of the claim attached to it — a truthful verification clause traveling with a wrong-referent conclusion AUTHENTICATES it** (sibling of `[[finding_exact_level_authenticates_a_wrong_direction]]`: there a precise level stops anyone checking the adjective; here a precise referent-cite stops anyone checking the scope).

**Downstream consequence, caught before it fired:** the escalation condition built on the false absence (*"still absent ~8/25 ⇒ cadence BROKEN — investigate"*) **would have fired on the publisher behaving NORMALLY — ATTOM skips the monthly press release in 3 of the last 6 months.** A wrong instrument-claim becomes a false-alarm generator one hop later; base-rate the PUBLISHER before keying an escalation to its silence (`[[finding_base_rate_the_instrument_before_its_event_table]]`). HOMER re-keyed to quarterly/mid-year/year-end; zero thresholds moved.

## How to apply (n=9 addition)

- **A verification clause names ITS OWN referent, not the claim's.** When writing "verified at X," check that X's coverage ⊇ the claim's scope — otherwise the clause upgrades the claim's credibility while verifying something narrower. As a READER, treat "verified at <surface>" as a pointer to re-check scope, never as a discharge.
- *(Seven-forms enumeration UNCHANGED — this is a SCOPE instance; the count stays 7, per this file's own stale-count warning.)*

*(Amended 8/22b, correcting THIS ENTRY's own first framing at the owner's insistence — the "self-caught, self-corrected, self-reported same session" line was itself wrong: the FINDING was self-caught, but the residue — HOMER's own boot-read docket row still carrying the false verdict and its escalation — was caught by PROME QUOTING THE FINDING BACK to the owner, and a second defect ("adopted" claimed before any surface carried it) surfaced only while verifying that residue. Two of three catches came from quote-back: restating an agent's claim to it in its own words is a cheap, effective catch mechanism. The residue's LOCATION feeds `[[finding_verification_correction_downstream_propagation]]`'s edit-path extension, same date.)*
