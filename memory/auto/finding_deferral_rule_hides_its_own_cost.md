---
name: deferral-rule-hides-its-own-cost
description: "A hold/defer/wait rule is the one class of rule whose cost is INVISIBLE WHEN YOU FOLLOW IT — a bad send is visible immediately, a non-send looks exactly like a quiet day. Price the deferral against what it actually protects, out loud, every time. Corollary: for a PULL-COMPLETE recipient the PUSH is the delivery, so 'committed' is not 'delivered'."
metadata: 
  node_type: memory
  type: finding
  originSessionId: e01dbca8-7314-4a08-849f-aacf5982f7a2
  modified: 2026-08-11T23:10:17.144Z
---

**The incident (WALTER, 2026-08-11).** WALTER's own closeout step 16 says *defer the push entirely on observed concurrent uncommitted foreign work*. MARCO was live on the same box — files written one to three minutes earlier — so WALTER deferred the push, wrote the deferral into `STATUS.md` as a considered decision, and reported it to Will with reasoning. It looked like discipline.

**Then a check made the cost visible.** `walter_doctor` flagged the two handoffs as *"committed but NOT on origin — recipient can't pull it."* The dispatch being withheld was an **IMMEDIATE on a falsification trigger that had just FIRED** (`RED-FT-06`), and its ACTION owner is **`RED`, which is PULL-COMPLETE** — exempt from inbox handoffs under `BOARD_CONSUMPTION_SPEC` §3.5, and therefore reachable **only** via BOARD on origin. **Deferring delivered the fire to nobody.**

**The rule was guarding against a race its own subject cannot produce.** `git push` reads refs and sends objects; it cannot touch another agent's uncommitted working tree. `safe-push` is fast-forward-gated and aborts cleanly if the other agent commits underneath. So the deferral bought nothing and cost the delivery of the session's only IMMEDIATE.

**Why this generalises past git.** A *send / act / publish* rule fails loudly — the bad output is right there. A *hold / defer / wait* rule fails **silently and symmetrically with success**: a correct deferral and a costly one produce the identical observable, which is nothing happening. That asymmetry means deferral rules never accumulate the corrective feedback that action rules do, and they drift toward over-application.

**How to apply:** when a rule tells you to hold, name **what it protects** and **what the hold costs**, in one line each, before complying. *"I followed the rule"* is the start of the reasoning, not the end. If the mechanism you are withholding cannot cause the harm the rule anticipates, the rule does not apply to this case — say so and proceed.

**⚠️ The corollary, which is the operationally sharper half:** for a **PULL-COMPLETE recipient, the push IS the delivery.** The §3.5 exemption removes the inbox handoff, which silently makes origin the single point of failure for exactly the recipients most likely to be the **ACTION owner** on a dispatch. Everywhere else "committed locally" is a safe intermediate state that the next push train resolves; for a pull-complete recipient it is indistinguishable from never having written the signal. **Check the recipient's delivery mode before treating an unpushed commit as delivered work.**

Caught by an instrument, not by the author. Related: [[finding_mechanize_the_cap_not_the_ritual]], [[finding_push_train_hides_a_failed_commit]], [[finding_delivery_check_is_not_a_knowledge_check]].
