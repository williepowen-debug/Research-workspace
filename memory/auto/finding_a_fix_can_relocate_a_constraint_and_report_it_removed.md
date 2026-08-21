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
