---
name: finding_a_fix_can_relocate_a_constraint_and_report_it_removed
description: "a fix that moves a dependency into the SAME class it was supposed to remove reads as a solution — ask what the fix now depends on, and whether that is the thing you just ruled out"
metadata:
  node_type: memory
  type: finding
---

A proposed fix can **relocate** a constraint instead of removing it, and the author will report the constraint gone — because the fix genuinely closes the door that was named. The tell is that **the fix's own precondition falls in the same class as the obstacle it replaced.**

**Worked instance (2026-08-20, T6 platform naming).** BOND flagged that naming Kalshi as a test's canonical instrument was risky because **Kalshi creds are desktop-only** on a serial desktop⇄laptop operation — the value might be unpullable on grading day. LIQUID "fixed" it: *have ORACLE pin the value daily, so the grade reads an on-repo record rather than a live pull — the machine constraint stops mattering.* **It does not.** ORACLE runs as a session on the same box, so **the pin needs the same desktop creds.** The dependency moved from *"can we READ it on grading day"* to *"can we RECORD it on most days"* — same class, shifted in time. One door closed, the room reported sealed.

**Why it survives review:** the fix is *locally* valid and it answers the objection **as literally worded**. Both parties then reason about the new arrangement without re-running the original objection against it. Nobody is careless; the check simply is not in anyone's loop.

**The second-order bite — relocation can spread to *other* repairs.** In the same test, an unrelated agreed fix ("the named platform prints below its value **5 trading sessions prior**") silently requires five prior sessions **of that same record**. So a gappy pin would make *that* repair ungradeable too. **A relocated constraint can become load-bearing for repairs that never mentioned it.**

**How to apply:**
- After proposing a fix, ask: **"what does this now depend on, and is that thing in the same class as what I just ruled out?"** Machine access, credentials, a person's uptime, a subscription, a session being live — these recur.
- **Name the residual dependency out loud in the packet**, even when you believe it is satisfied. "This works provided X" is checkable by the other desk; "the constraint stops mattering" is not.
- When the relocated thing is a **record**, demand explicit gap-marking: a record with *silent* holes is worse than no record, because the reader sees a value with no staleness indicator ([[finding_plausible_stale_value_evades_review]], and the `UNMEASURED` vs `NOT FIRED` distinction).
- **Sweep the other repairs** in the same artifact for dependence on the relocated thing.

**Evidence strength, stated honestly: n=2, both in one evening and both inside the same T6 thread** — LIQUID's pin fix relocating BOND's desktop constraint, and PROME's own framing relocating a constraint that LIQUID's gap-marking point then caught. **Two desks, both directions, which is why it is written down; it is a suggestive shape, not an established base rate.** Adjacent but distinct from [[finding_guard_correctness_and_wiring_are_independent]] (a guard's correctness vs its wiring) and [[finding_bypass_turns_a_flow_proxy_into_a_routing_metric]] (meaning moves while the instrument stays clean) — here the *instrument and the meaning are fine* and it is the **dependency** that moved.

---

**Instance 2026-08-23 (PROME/DAEDALUS, auto-memory infrastructure) — TWO relocations in one evening, the second inside the fix for the first.**

**① The remedy became the defect.** `MEMORY.md` outgrew the harness read cap, so the fleet split it: a hot index (loaded every session) and a cold one, with a flow rule that **demotes rows into the cold index** whenever the hot index passes 75%. It worked — the hot index sits at 35%. But **nothing ever bounded the cold index**, and it is the sink. It reached **58,825 B against a measured 53,819 B truncation point**, stranding **26 slugs** past the cut while the healthy hot index went on advertising them. ⚠️ **Worse than a lost row: demoted rows APPEND AT THE END and the cut takes the END, so the rows most recently RESCUED from the hot cap were the first to become unreachable.** One of the stranded rows was cited by `PROME/CLOSEOUT.md`'s own Write-Back Contract; another was a lesson banked the same day.

**② Then the fix did it again, smaller.** PROME's first version of the new ceiling rule cost **1,643 B** and left **879 B** of margin — **a rule about file size that nearly re-breached the file it governs.** Caught in the same pass by re-measuring instead of assuming.

**⇒ The diagnostic question, sharpened: it is not enough to ask "what does the fix now depend on." Ask WHERE THE DISPLACED QUANTITY WENT, and whether that destination has a bound.** A split, a tier, an archive, a queue and a cache are all relocations. If the receiving side has no ceiling, the constraint has not been removed — it has been made **quieter and later**, and it will resurface where nobody is measuring.

⭐ **And the tell that it was a relocation rather than a fix was available for free the whole time: the sink had no check.** The hot index had a flow rule, a byte meter in the closeout gate, and a size hook. The cold index had none of the three — and nobody noticed the asymmetry for 23 days, because every instrument that existed kept returning green (`[[finding_registered_gate_captures_attention]]`, `[[finding_guard_correctness_and_wiring_are_independent]]`).

---

**Instance 2026-09-02 (MIDAS, `metals_watch.py` kill rail) — n=4, and the NEW variant: the relocation was WRITTEN DOWN AS A REPAIR, in a source comment, where it read as verification for ten days.**

**What happened.** A boot instrument graded a registered kill-condition window using `GC=F`, a *continuous* futures ticker. On 2026-08-23 it was fixed for a real defect — it had been reading a **live** quote instead of a settled close. That fix was correct. The comment shipped with it was not:

> *"The live quote also crosses the GCZ26 roll, so the old reading was contaminated twice — in-flight AND cross-contract. **Settled+prior-bar keeps both legs on one contract and one calendar.**"*

**Settling a bar cures the in-flight defect only.** It cannot cure the cross-contract one, because **the ticker IS the roll**: its underlying contract changes *inside* the measurement window, so both endpoints can be perfectly settled and still be different instruments. Measured 2026-09-02: the leg read **+1.59%** off two thin dying-contract prints (volume **1,303** and **360** on the world's most liquid gold future) against **+1.398%** same-contract and **+1.461%** no-roll.

**⇒ What this instance adds to the pattern.** The earlier instances relocated a dependency and *left the reader to notice*. This one **relocated it and then filed a certificate** — the false half sat in the comment beside the true half, in the one artifact a later auditor reads to find out whether the question was already handled. **A comment is where "I inferred this" and "I measured this" become indistinguishable.** An auditor checking that exact leg for roll contamination would have found a sentence saying it was addressed, and stopped.

⚠️ **The aggravating detail, and it generalises.** The desk's own boot-read STATUS banner carried an explicit **CROSS-ROLL BAN** the entire time. **The banner and the code disagreed for ten days and nothing could see it, because they are different surfaces with different readers** — the banner is re-read every boot, the comment is read only by whoever opens that function. A rule stated on the surface you re-read does not propagate to the code that violates it.

**How to apply — one addition:**
- **When a fix addresses defect A and you believe it also addresses defect B, B needs its own test and its own measurement, or the claim about B does not go in the comment.** Write what you *measured*; for what you *inferred*, write that you inferred it. A fix pass is unreviewed work ([[finding_a_correction_pass_is_unreviewed_work]]) and its **comments** are the least reviewed part of it.
- **Grep your own standing bans against the code that could violate them.** A banner is not a guard.

**Harm this instance: zero — and that is ordering luck, not method.** The condition this leg feeds had already fired on an earlier window and its registered test was terminal, so a wrong number had nothing left to escalate. Had it been live, a REVIEW would have been raised on a cross-roll figure. Sibling of [[finding_instrument_reports_clean_against_the_wrong_reference]].
