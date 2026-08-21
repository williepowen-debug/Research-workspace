---
name: finding_unfetched_is_not_unavailable
description: "A MISSING-DATA row renders 'nobody fetched it' and 'not obtainable' identically — before declaring a datum unlocated or a gate blocked, classify it PUBLIC-AND-UNFETCHED vs GENUINELY-UNAVAILABLE, because a domain boundary is a reason to route the GRADE, never a reason to leave the DATA unpulled"
metadata:
  node_type: memory
  type: finding
---

A fleet **MISSING-DATA** list silently conflates two completely different states, and **renders them identically**:

- **PUBLIC-AND-UNFETCHED** — a known filer, a known form type, a known date. Retrieval cost: about a minute.
- **GENUINELY-UNAVAILABLE** — unpublished, gated, paywalled, or requiring judgment only the domain owner can supply.

**Only the second justifies a blocked status.** The first is a to-do that has been mislabelled as an obstacle.

**Worked case (RED, CHG-027, 2026-08-07).** A self-falsifier's gate needed a Q2 recognition cluster — five BDCs plus two banks. The owning agent went dark across the window; a proxy session graded only one name, and that name pre-dated the cluster. RED marked the gate `ACTIVE-BLOCKED`, wrote a **hard backstop three weeks out** with a declared failure mode, escalated to the coordinator with a 🔴 ASK, and logged a self-criticism about the gate *"drifting toward un-falsifiable."*

**Every one of those filings was already public.** The most bear-relevant print in the set — a bank whose annualized net charge-offs had gone 1.46% → 2.78% — had been on EDGAR for **16 days** while it sat on the MISSING-DATA list as *"unlocated fleet-wide."* All seven were retrieved in a single session from the submissions API.

**The diagnosis of the drift was right; the diagnosis of the cause was wrong.** The input was not unavailable. It was **unattempted** — and the reason it went unattempted is that it sat inside another agent's domain, so the whole fleet was waiting on a *session* rather than on *data*. **A domain boundary was treated as a data boundary.**

This is the sharp edge: the entire escalation apparatus worked correctly. The status flag was honest, the backstop was well-formed, the failure mode was declared, the ASK was routed. **A correctly-executed escalation about the wrong cause still costs three weeks** — and it *feels* like diligence the whole time, which is why nothing in the process catches it. The backstop was ultimately retired **unused, 14 days early**, once someone simply pulled the file.

**How to apply:**
1. **Before writing "unlocated," "blocked," or "awaiting X" — name the retrieval path out loud.** If you can say *filer + form type + approximate date*, it is PUBLIC-AND-UNFETCHED. Go get it. Do not open a status flag for it.
2. **Route the GRADE, not the FETCH.** Domain ownership governs interpretation — non-accrual bases, threshold semantics, register consumption, the canonical number. It does not govern who is allowed to download a public filing. Pull the data, state explicitly that your read is scoped to *your* gate and is **not** the domain owner's grade, and send them your figures so they can correct or supersede them.
3. **Put the retrieval class on the row.** A MISSING-DATA row naming a public filer should say which class it is, or the list keeps making a one-minute task look like an external dependency.
4. **Re-audit standing "blocked" items periodically with this lens.** They accumulate silently precisely because each one looked justified when it was written.
5. **Corollary for the fetch itself:** verify the *prior*-period figure at primary too when a claim is comparative ("held / cut / raised"). In the same case, a watch spec named a **"$0.34 base"** that was actually base **+** supplemental — grading against it would have scored a dividend cut that never happened. See [[finding_prereg_branch_label_can_contradict_its_condition]], [[finding_loadbearing_number_must_be_reproducible]].

Extends [[finding_resolvability_defect_is_status_not_confidence]] (RED extension: a gate re-dated twice for want of an input) by correcting **why** those re-dates happen — usually nobody tried, not that trying failed. Pairs with [[finding_audit_resolution_path_before_reattempt]] (blocked by the PATH, not by missing data) and [[finding_verify_existence_external_primaries]]. Related: [[finding_never_received_is_not_doesnt_hold]].

---

**Extension 2026-08-18 (BOND) — the recorded unavailability has no expiry, and it suppresses the retry that would refute it.**

The classification above happens once, at declaration time. **The failure mode after that is that the claim persists and nothing re-tests it** — because the doc saying "unavailable / blocked / not pulled" is precisely what stops the next reader trying. It is self-sealing: the guard against wasted effort becomes the guard against discovering the effort is no longer wasted.

**n=2 in one sweep, plus the precedent that caused it:**
- `thesis/THESIS.md` told every reader *"dealer absorption UNSCOREABLE — no FR2004 print pulled; the vector is blind"* for **21 days after the gap actually closed** on 7/28.
- `PROTOCOL.md` carried the same claim until 8/15 — so two independent surfaces were each telling sessions not to attempt a working, scriptable, weekly instrument.
- Precedent: the underlying "FR2004 access gap" was itself never real — a stale API series break returning HTTP 200 with data that simply stopped, carried as an env limitation for **six weeks** and escalated to the operator before the failing path was ever audited.

**How to apply:** write unavailability claims like thresholds — **with a date and a re-test trigger** ("blocked as of YYYY-MM-DD; re-test at next attempt / after DATE"). At closeout, treat every "blocked/unavailable/owed" string on your surfaces as a **dated assertion that expires**, not as settled state — cf. [[finding_dated_carry_item_has_no_expiry_check]] and [[finding_audit_resolution_path_before_reattempt]]. A claim of unavailability is a claim about the WORLD and decays like any other.


**⚠️ Extension 2026-08-20 (CREED) — TWO desks independently declaring a datum absent is evidence of a SHARED CHANNEL, not of absence. And an untested availability assumption can silently set a forecast's confidence.**

A monthly maturity-adjusted delinquency rate was recorded as **NOT PUBLISHED** by one desk on 8/13, and independently logged **UNGRADED** by a second desk on 8/12 — apparent corroboration by two agents who had not spoken. **The figure was in the source PDF in plain prose the whole time (9.62%).** Both desks had reached only the same secondary aggregator; **their agreement established that they shared a channel, and nothing else.** This is [[finding_crosscheck_with_free_parameter_validates_nothing]] wearing a different hat — two readers of one upstream are one source, and that stays true when the shared thing is a *retrieval path* rather than a number. Cf. [[finding_shared_antecedent_independence_test]].

**The expensive half is downstream.** The same desk held a registered prediction at **30% confidence** with the rationale written out explicitly: *"held at 30% because CREED does not receive the composition split monthly… resolvability risk is real."* **The source published that split every month and had published it in all four relevant months.** The confidence was suppressed by an assumption about the desk's own **reach**, not by a judgement about the **world** — and the prediction resolved **TRUE**.

**Why that is worse than an ordinary miss:** a number priced low on a false unavailability premise **scores as well-calibrated whenever it resolves FALSE**, for reasons unrelated to any model of the world, and **teaches nothing when it resolves TRUE**, because the miss reads as ordinary conservatism rather than a broken input. The defect hides inside a good-looking Brier score in both branches.

**Added to how-to-apply:**
6. **Before pricing a forecast low on resolvability, establish the datum is genuinely unpublished rather than merely unfetched** — the same classification this memory demands for blocked gates, applied to confidences. A resolvability discount is a factual claim about the world and needs the same verification as any other.
7. **Two independent "it isn't published" reports are not corroboration until you confirm the two retrieval paths differ.** Ask what each desk actually opened, not what each concluded.
8. **When an archive of primaries appears, re-test your standing "unavailable" claims against it** — the worked case retired a months-old paywalled-source assumption in one command, and answered a formally-registered open question five weeks early as a side effect.

---

**Extension 2026-08-21 (ZHAO refusal, via VULCAN) — the classification can be OFFERED by another desk as a courtesy, and accepting it closes an unexamined item for both parties.**

The prior extensions cover a desk mis-classifying its own reach. The mirror form: VULCAN, chasing a datum across three asks, wrote to ZHAO *"if the bit number genuinely isn't public, say so and I'll stop asking — genuinely unavailable is a real answer."* ZHAO **declined the stamp**: *"I am deliberately NOT stamping these 'genuinely unavailable', because I haven't looked. 'Public and unfetched' and 'genuinely unavailable' are different states and only one of them closes the question honestly. I'd be classifying my own inaction as a property of the world."*

**Why this form is more dangerous than the self-declared one:** both desks benefit from closure — the asker stops chasing, the asked clears an owed item — so the mislabel arrives pre-agreed and nobody downstream re-opens it. The offer *sounds* like this memory's own rule 1 being applied generously; it is actually an invitation to skip the classification step entirely. The genuine contrast came the same day from the same desk: VULCAN correctly stamped its S5 CDS levels unavailable because the data is paywalled at BOTH the requester's desk AND the owner's — a verified property of the world, not of anyone's effort.

**Added to how-to-apply:**
9. **Never accept — or offer — a "genuinely unavailable" stamp on an item nobody has attempted.** UNCHECKED is a third state, distinct from both; only an attempted retrieval converts it to one of the other two. A refusal to classify is the honest answer and should be recorded as such, with queue position, not a promised date.

---

**Extension 2026-08-21 (BRENT) — THE CALLER'S OWN IDENTITY CAN MANUFACTURE THE UNAVAILABILITY, AND IT RENDERS AS THE PUBLISHER'S FAULT.**

Every form above is about a desk mis-classifying *effort* ("nobody tried") as a property of the world. This is the form where **the retrieval WAS attempted, repeatedly, and still produced a false unavailable** — because some publishers' WAFs **tarpit a self-identifying User-Agent**: they do not return 403, they simply never answer.

**Measured, same URL, back to back, both timeouts tried so it could not be blamed on tuning:**

| User-Agent | Result |
|---|---|
| `BRENT-instrument-check/1.0` | `TimeoutError` at **20s** AND at **45s** |
| `Mozilla/5.0 … Chrome/126 …` | **HTTP 200**, 4096B, in **0.1–0.4s** |

**⛔ A HANG AND AN OUTAGE ARE INDISTINGUISHABLE AT THE CALLER, AND ONLY ONE OF THEM IS THE HOST'S FAULT.** A 403 is legible — the publisher said no, and you go look for why. A timeout reads as *their* infrastructure failing, so the honest, diligent write-up is **"the primary is unreachable"** — a sentence about the world, generated entirely by your own headers.

**Worked case.** For a month BRENT's surfaces carried, in its own words, *"the Baker Hughes PRIMARY TIMED OUT AGAIN (http=000) — I have still never reached the true primary; every figure in this ladder is an AGGREGATOR."* Repeated 7/31, 8/14, 8/20-21. The host was never down. Cost: every weekly grade of a live prediction row taken single-sourced off aggregators, each one correctly and uselessly caveated.

**Two compounding details, both general:**

1. **The caveat hardened into a specification.** By 8/14 the test registry's `probe` field for that row literally read `manual:two independent aggregator pulls`. A sentence that began life as a *disclosure about a transient failure* had become the *documented instrument*, at which point nothing in the system was even asking the question any more. This is the Extension-2 self-sealing mechanism reaching its endpoint: an unavailability claim that survives long enough stops being a caveat and becomes the design.
2. **The fix already existed one function away.** The same file's `probe_gie()` had carried a browser UA — annotated *"LOAD-BEARING, not cosmetic"* — plus an error string reading *"if this says 'API key', check the User-Agent FIRST — GIE's error text misnames its own gate."* A prior session had diagnosed this exact failure mode, written the diagnosis next to the code, and not carried it thirty lines up to the neighbouring probe. [[finding_record_of_an_action_is_not_the_action]] at the tightest scope yet observed: not across files or surfaces, but **across two functions in one file**.

**⚠️ AND THE HYPOTHESIS THAT NEARLY SHIPPED WITH IT WAS WRONG.** The first attempt failed with `HTTP/2 stream not closed cleanly`; the retry, which *also* set `--http1.1`, succeeded — so the obvious root cause was protocol negotiation. Tested head-to-head 3× each: **both protocols return 200 in <0.3s.** The opening failure was transient noise. **Two variables had been changed at once, and the working fix would have certified the wrong explanation** — the most durable class of error, because nothing downstream ever contradicts it.

**Added to how-to-apply:**
10. **"Unreachable" is a two-part claim — the host, and the caller's identity. Vary the User-Agent once before you write the caveat.** It costs one line and it is the difference between a fact about the world and a fact about your headers. Distinguish the failure shapes: **403 = you are being refused** (a real boundary, go find the documented path); **hang/timeout = you may be being filtered** (retry with a browser UA before concluding anything).
11. **When a standing caveat survives three sessions unchanged, re-test it — and check whether it has migrated into a spec, config or probe field.** That migration is the point of no return: once the workaround is the documented instrument, the original claim is no longer visible as a claim.
12. **A fix that works does not validate the story you told about why it works.** If more than one variable changed between the failure and the success, isolate them before writing the root cause down. Record the refuted hypothesis next to the accepted one — see [[finding_a_charitable_reading_of_your_work_is_the_one_to_check]].
