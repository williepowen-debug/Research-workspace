---
name: finding_count_the_connectives_in_versus_out
description: A state machine that enters disjunctively (any 1 of N) and exits conjunctively (all N) is a ratchet — pure arithmetic, no base rate needed
metadata:
  type: feedback
---

**Count the connectives on the way IN and on the way OUT.** If a state is entered on **any 1-of-N** conditions and exited only on **all N** conditions, `P(enter) ≫ P(exit)` **for any legs whatsoever** — correlated, independent, whatever. Entry is a union; exit is the intersection of the complements. It is a **one-way ratchet**, and it is arithmetic on the connectives, not a claim about the data.

**Why:** found in VIOLET's VIX-packet machine (`TRADE.md:112` arms on any one of three gates; `:117` stands down only when all three are benign) during DAEDALUS's 2026-07-30 compound-gate screen. It is the **cheapest** of the four gate defects and the only one needing zero domain knowledge — and it is invisible to both leg-level and *joint* base-rating, because the defect is not inside either clause: it lives in the **relationship between two gates five lines apart.** The sibling defect it accompanies (BRENT, same week): a conjunction can be healthy on each leg and healthy jointly on an average day, yet **jointly impossible in the trigger state** — `{OVX<44.2 AND ratio<2.89}` opened on 50.4% of all sessions and **0 of 38 escalation days**, so always base-rate `P(all legs | trigger fired)`, never unconditionally.

**How to apply:** on any arm/disarm, escalate/de-escalate, or open/close pair — count connectives both directions before touching the thresholds. Disjunctive-in / conjunctive-out is the defect; symmetric, or conjunctive-in / disjunctive-out, is the conservative shape. **Severity depends on direction:** a stuck *deploy* gate is loud (capital sits, someone asks why), but a stuck *kill / stand-down / retire* gate is **silent — a kill that cannot fire is indistinguishable from a thesis that is still true**, and staying escalated reads as vigilance rather than as a bug. Cheapest standing detector: a **sessions-armed-and-unopened counter** (count the *plain* arm — a counter gated on "armed AND still relevant" is itself a compound gate and inherits the bug).

Related: [[finding_compound_gate_jointly_unsatisfiable]], [[finding_deliberate_and_unnoticed_asymmetry_look_identical]], [[finding_standing_guard_is_a_false_negative_risk]].
