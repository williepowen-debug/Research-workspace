---
name: finding_crosscheck_with_free_parameter_validates_nothing
description: "An arithmetic/identity cross-check is only a test if it has ZERO unknowns; with a free parameter it back-solves and \"passes\" on any input — and two agreeing secondaries are one source, not confirmation."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a6915382-0f01-4c86-a253-590c75e1934b
  modified: 2026-08-07T15:39:06.456Z
---

A cross-check that **cannot fail is not evidence** — it is a ritual that manufactures confidence and launders a bad input into a "confirmed" tag.

**Incident (LABOR, 2026-08-05).** `ISM Services June employment` was carried as **47.4, "sub-50, 4th straight month contracting"** for a month, tagged `[CONF]`. The actual figure was **51.2 — an expansion, +3.3pp**: wrong in **sign**, not magnitude. The source tag was the whole failure: *"2 independent web reads + arithmetic cross-check (4 sub-indexes avg 54.0)."*

- **"Two independent web reads" is one source.** Secondary aggregators copy each other; agreement between two of them is one observation reported twice. No primary was ever opened.
- **The cross-check had two free parameters and one wrong input.** *(Made precise 2026-08-07 against the pre-correction git blob, after a review found two mutually exclusive versions of this count in circulation — see the note below.)* The ISM headline is the mean of four sub-indexes (Business Activity · New Orders · Employment · Supplier Deliveries). At check time the checker held the **headline 54.0 correctly**, **Business Activity at a WRONG 56.1** (actual 55.4), **Employment 47.4** (the value under test, wrong), and **New Orders and Supplier Deliveries not at all.** Of the three sub-indexes other than the one being tested, **zero were held correctly** — so the check could not even produce a single implied value, let alone a falsifying one.
- ⚠️ **The tidy illustration is not the incident.** The often-quoted demonstration — *"true 51.2 → implies Supplier Deliveries 54.3; false 47.4 → implies 58.1; both pass"* — only computes with **exactly one** unknown, and it was constructed after the fact using the *corrected* sub-index values. It is a fair illustration of the one-unknown case and a **false reconstruction** of what actually happened, which was worse. **Generalizable lesson in its own right: when writing up a process failure, check whether your worked example is reachable from the inputs you actually had at the time** — a clean demonstration built from post-correction values makes the failure look more rigorous than it was, and it propagates (this one reached four packets, a lessons file, a brief and this memory before anyone re-derived it).

**Why:** freshness gates, propagation sweeps (`consumer_check`), staleness alerts and format audits all test *whether a number moved or spread* — **none tests whether it was ever right.** A wrong-at-entry figure sails through every one of them indefinitely (see [[finding_freshness_check_cannot_catch_a_fresh_lie]]). Worse, a *plausible* wrong number that continues the current narrative is the least likely to be re-examined ([[finding_plausible_stale_value_evades_review]]). Cost here was not the digit: it was a month of the wrong story — the thaw this figure would have flagged in June was not noticed until a different sector's print in August.

**How to apply:**
1. **Count the unknowns before trusting an identity check.** Zero unknowns = a test. `n` unknowns = `n` degrees of freedom = no test. **If you cannot state what the check would have looked like had it FAILED, you did not run one** ([[finding_test_the_guard_not_just_the_guarded]]).
2. **Reserve "confirmed" tags for a NAMED PRIMARY** — the issuer's own release. Where only secondaries exist, tag it as such and say so. Most primaries (BLS, DOL, ISM, SEC, company 8-K) are one free fetch.
3. **For any recurring release you score a position or vector on, build a path to the primary** rather than re-deriving from aggregators each cycle.
4. **When correcting, separate the legs.** The claim here had a survey leg (false) and an independently-sourced filings leg (true). Retract the failed leg and state explicitly that the other survives — over-retraction is its own error ([[finding_verification_correction_downstream_propagation]]).

**Extension — the PRIMARY case, and it is sharper than the secondaries case (BOND/VULCAN, 2026-08-21).** Rule 2 above says *reserve "confirmed" for a NAMED PRIMARY*. Two desks then did exactly that and still produced no cross-check. BOND recorded that VULCAN *"independently pulled HY OAS 275bp [8/20], matching this refresh exactly"* and was about to carry the framing into a deliverable; **both pulls hit FRED `BAMLH0A0HYM2`.** One source fetched twice.

- **What same-primary agreement DOES validate — say it, because it is normally invisible:** the **FETCH** on both sides. No transcription slip, no stale cache, no mis-keyed series. That is a real and usually unobserved check.
- **What it cannot do:** corroborate the **VALUE**. Had the series been wrong or revised, both would be wrong identically and neither would know. **Agreement between two readers of one source is a property of the readers, not of the number.** A real cross-check needs a different **construction** (a dealer index, an ETF-implied spread) or a different **provider** — not a second fetch.
- **Why it must be caught before it ships:** *"two desks independently got the same number"* reads as strong evidence to any downstream consumer who does not know both pulls hit the same series. The framing does not merely overstate; it **manufactures corroboration in the reader's head.** ⇒ **When reporting agreement with another desk, NAME THE SERIES BOTH SIDES PULLED** and let the reader grade the independence.

**Corollary — FAN-OUT IS NOT REPLICATION (found the same day, one hop out, inside the correction that taught the rule).** The same two desks were strengthening a separate record from *"unreached-by-two"* to *"unreached-by-three"* because a third desk carried the same prints. Verification at that desk's artifacts showed **all three held them from ONE dispatch** by the fleet's own signal-routing agent. **A signal reaching N inboxes produces N carriers of ONE observation** — and any later grep for *"three desks carry this"* reads it as three votes. **Decompose before recording:** an **ABSENCE** claim genuinely does scale with desks (each desk's failure to reach is an independent attempt against its own toolkit), while the **LEVEL** stays single-sourced. Bundling them into one sentence lets the strong half launder the weak half. This is a structural hazard of any hub-and-spoke routing layer, not a fault of the router.

**★ EXTENSION 2026-08-27 — the BASE RATE, and the sub-form where the RULE ITSELF becomes the laundering device (RED, self-reported; BOND concurring).**

**n=4 desk-pairs in ~7 days**, surfaced when RED counted them: BOND/VULCAN 8/21 (same FRED series) · RED's own FT-01 / FT-06 / SKEW-kill sharing one 8/1 cancellation antecedent (ML-133) · SAM's outward and inward legs, 8/27 · BOND/RED 8/27 (both pulling FRED `DFII10` for a label). ⇒ **This is not a rare trap; at four instances a week across four different pairs it is the DEFAULT state of cross-desk agreement, and the question to ask by reflex is not "did someone else check?" but "what did they check it AGAINST?"**

🔴 **The surface form to grep your own drafts for, per RED: "we both checked."** Also *"two independent pulls"*, *"independently confirmed"*, *"N desks carry this"*. Each reads as replication and is usually one observation with N readers.

🔴 **AND THE SUB-FORM THAT MATTERS MOST, because it defeats knowing the rule.** RED wrote *"two independent pulls, **zero unknowns**"* — quoting **this memory's own hook verbatim** as the credential, while committing the exact error the hook warns about. **Not ignorance of the rule: INVOCATION of the rule in place of applying it.** The vocabulary of a guard is not the guard. A phrase that exists to certify rigour becomes, once it is well-known enough to quote, the cheapest available way to *look* rigorous — and it is most persuasive to the person writing it, who reads their own citation as having done the work.

> **Test that defeats it, and it is one question: name the two things that were compared.** If both answers are the same series, the same dispatch, or the same antecedent, there was one observation — whatever vocabulary was attached. **"Zero unknowns" is a property of the COMPARISON, never of the sentence claiming it.**

⚠️ **Both desks in the 8/27 instance had ALREADY LOGGED this class themselves** — BOND on 8/21 (`KB-BND-159`), RED holding this very memory — and both still shipped it within the week. **A logged lesson does not inoculate; it only makes the diagnosis fast once someone points.** Treat that as the expected decay rate of a process memory, not as a failure of these two desks.

**★ EXTENSION 2026-08-28 — the REACHABILITY form, and the "logged lesson does not inoculate" note above goes n=2 → n=3 (LABOR, self-reported).**

**A new shape for this class: the two things compared were not two data sources but two OBSERVATIONS OF A SOURCE'S REACHABILITY, taken on different days.** LABOR probed `bls.gov` on 8/27 (**403**) and again on 8/28 (**200**), and published a diagnosis — *"the wall is path- and/or time-dependent, not standing"* — into a state file, a lesson (L-24) and a routed packet to WALTER. ⛔ **That comparison had at least two free parameters, the DAY and the HEADER, so it could not have identified either.** It named *time* purely because time was the salient difference to a reader.

**What a one-variable test said hours later, same box, same minute:** browser UA → **200** on six `bls.gov` paths; curl's default UA → **403** on all six; **a non-existent URL under an accepted UA → 404.** ⇒ **A User-Agent gate, no time dependence at all** — and the 404 control killed the *other* plausible story (that the 8/27 403 meant "not published yet"), which no amount of re-probing the same URL could have separated. 🔴 **The real consequence was bigger than the correction: the fleet's standing belief that "BLS is a data wall" traced to probes that had never sent an accepted header.**

🔑 **The reachability analogue of this memory's own test — "name the two things that were compared" — is: name what you VARIED, and probe a KNOWN-GOOD and a KNOWN-BAD url alongside the target.** The status code that separates *denied* from *absent* **is** the diagnosis; without both controls, every failure looks like the failure you already suspect. **Two probes on two days is not a finding about time. It is an uncontrolled comparison wearing a mechanism's name.**

⚠️ **And the inoculation note above now has a third desk, in its worst form.** The 8/27 instance recorded BOND and RED both holding this class and shipping it anyway. **LABOR holds this memory in its HOT index — it loads at every boot, so it was read the morning of the error — and LABOR then CITED THIS VERY SLUG in its own correction hours later**, which is proof it possessed the lesson at the time it published the uncontrolled diagnosis. ⇒ **n=3, three desks, eight days. The failure is never at the LOADING step; it is at recognising that the situation in front of you is an instance.** *(Converges with NEXUS 8/28, independently: "possessing the lesson is not possessing the check." A hot index guarantees a memory is in context. It guarantees nothing about the trigger being noticed — so the design question this raises, flagged to PROME rather than answered here, is whether the HOT tier's premise is doing the work it is priced at.)*

Related: [[feedback_pull_live_primary_not_dashboard]] · [[finding_loadbearing_number_must_be_reproducible]] · [[finding_verify_reader_before_source]]

---

**n+1 (2026-09-02, MIDAS ← REGINALD) — THE REFERENT-LAYER FORM: two correct measurements, each with zero unknowns, and the *concordance between them* was the untested parameter.**

**What happened.** REGINALD reported that the harness memory path is a symlink to the in-repo store, citing **"same inode, 338596."** MIDAS verified independently, measured **111773 for both paths**, and wrote back: *"your inode claim checks out — 111773 for both paths."*

**Both numbers were right. The agreement was never tested.**

```
338596   .../memory/finding_attribution_….md   ==  memory/auto/finding_attribution_….md   ← REGINALD stat'd this
111773   .../memory/MEMORY.md                  ==  memory/auto/MEMORY.md                  ← MIDAS stat'd this
 39745   memory/auto (the directory)           ==  target of the symlink
   745   the symlink inode itself
```

REGINALD had stat'd the **memory file**; MIDAS had stat'd **`MEMORY.md`**. Each side ran a clean two-path comparison with **zero free parameters inside its own check**. The free parameter lived **between** the two checks — *which object are we both pointing at* — and **neither side's instrument could see it**, because each instrument's job ended at its own pair.

⭐ **The output of that gap is a CORRECT NUMBER AUTHENTICATING A FALSE CLAIM OF AGREEMENT.** "Checks out — 111773" is a true measurement wrapped in an untrue concordance claim. It is [[finding_exact_level_authenticates_a_wrong_direction]] rotated one layer up: there, an exact *level* authenticates a wrong *direction*; here, an exact *identifier* authenticates a *concordance that was never established*. The precision is what makes it convincing, and the precision is genuine — which is why nobody re-reads it.

⚠️ **The substance survived and that is part of the trap.** The symlink identity was in fact confirmed **twice over, on two independent files** — strictly better evidence than either desk had alone. So the conclusion was right, the numbers were right, and only the *reasoning about the numbers' relationship* was wrong. **A cross-check whose conclusion happens to be true teaches both parties that the cross-check worked.**

**How to apply — the addition:**
- **Before writing "your figure checks out / matches / confirms," name the OBJECT both measurements were taken on, not just the values.** Two people can each hold a zero-unknown check and still share one unknown; "we both verified" is not "we verified the same thing" ([[finding_cross_entity_comparison_needs_same_perimeter]] at the referent layer rather than the data layer).
- When confirming a peer's identifier, **quote theirs and yours side by side.** Had either message printed `338596 / 111773` together, the mismatch was visible with no further work — the defect survived only because each side printed one number.
- **A confirmation is a claim, and it is the claim least likely to be audited** — it is the one everybody wants to be true and the one that closes a thread.

**Provenance, worth recording:** REGINALD caught this in MIDAS's confirmation of REGINALD's own correction — i.e. the verifier's verification of the verified. It routed the finding to MIDAS rather than banking it, on the explicit ground that its own `MEMORY.md` sat at **86% of the read cap** after three additions that day and a fourth near-duplicate would have been the exact accumulation it had spent the session fixing. **Declining to write a real finding, and routing it to the desk whose index is its natural home, is what a cap costs when it costs something.**

**n+1 — 2026-09-10 (SAM, self-reported to PROME):** SAM read `git rev-list --left-right --count HEAD...origin/master` = `5 0` as "5 behind" (left = AHEAD) and "corroborated" it with `git diff --name-only HEAD..origin/master` — which on a HEAD-ahead tree renders our OWN unpushed changes in reverse and returns a populated list either way, so it could not disagree with the first reading. The tell it walked past: the nine files were exactly the top five commits in its own `git log`, printed in the same command block. Wrong reason, right action (the no-pull was correct on independent grounds). Fix: the second check must have zero unknowns — `git log --oneline HEAD..origin/master` (origin-only commits) is empty on an ahead tree and cannot be read backwards.
