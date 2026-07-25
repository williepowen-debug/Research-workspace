---
name: duplicate-the-decision-changing-finding
description: "For the ONE finding in a study that actually changes what someone DOES, deliberately run it twice with independent agents. Two independent passes converged on every load-bearing point AND each closed the other's blocked source — and the second pass forced a same-night correction to a recommendation already sent. A strong, well-cited, confident single report is exactly the kind that invites being taken at face value."
metadata:
  node_type: memory
  type: finding
---

2026-07-24/25, WALTER's FHA/VA stress-test. Axis A — the only axis whose answer changed a domain agent's behaviour — got run **twice by accident**: the original agent went silent, a replacement was spawned after a disk check confirmed genuine absence, and the replacement had already written its report before the stop order reached it.

**The two runs had separate sessions and no shared working state. They converged on every load-bearing point** — same verdict, same single exception among four candidates, same ~58%-of-equity magnitude (the small delta was a quarter-end denominator, not a disagreement), and both independently reached the subtle reading that the fact *falsifying* the parent's evidence simultaneously *corroborated* its conclusion.

**More valuable than the agreement: each closed the other's gap.**
- Run 1 pulled FFIEC Call Report data via the FDIC JSON API. Run 2 was blocked (the CDR bulk download is registration-gated), **refused to substitute an unsourced figure**, and flagged it as its single largest open gap. Run 1 closes it.
- Run 2 found a forward disclosure gap run 1 missed — a target's book growing 29% in six months with no breakout of the relevant category — **which forced a same-night correction to a recommendation already delivered to the domain agent.**

**Why this is worth doing on purpose.** A single agent's report that is well-structured, densely cited and confidently argued is exactly the kind that gets taken at face value (`[[finding_asymmetric_rigor_counterparty_claims]]`). Convergence between two independent passes is what moves a claim from "an agent says so" to something a domain agent can switch a live watch off on. The cost of a second pass is trivial next to the cost of a wrongly-closed watch — and unlike an adversarial verify (which tests whether a claim is *wrong*), replication also surfaces what a single pass simply *could not reach*.

**Corollary:** when a duplicate turns out to be a replication, **keep it**. The replacement agent offered to have its file deleted as redundant; it had already earned its place, and an independent derivation of a behaviour-changing finding is worth more as a permanent record than a tidy output directory.

**How to apply:** identify the one finding in a study that changes an action. Run that one twice with independent agents and no shared context. Let the rest run once.

Related: [[finding_asymmetric_rigor_counterparty_claims]] · [[finding_independent_convergence_validates_schema]] · [[finding_shared_antecedent_independence_test]] · [[finding_adversarial_verify_own_convergence]] · [[finding_loadbearing_number_must_be_reproducible]]
