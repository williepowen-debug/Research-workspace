---
name: feedback_reconciliation_is_last_line_move_catch_upstream
description: "Cross-agent reconciliation reliably catches errors but is the LAST line of defense — treat every catch-by-another-agent as a signal to install the check at the point of origin so that error class can't leave your desk again."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0e851028-003e-4495-ab70-3adb897442d6
---

The fleet's cross-agent reconciliation layer is a genuine, working error-catcher: on 2026-07-22 WATT primary-refuted an AEOLUS over-fired 🔴 C3 flag and PROME caught a shared-index commit-sweep — both the same evening. But relying on it is defense-in-depth's **last** line, not its first. By the time another agent catches your error it has already propagated to Will and downstream state, and unwinding it costs a multi-surface retraction.

**Why:** a catch feels reassuring ("the system worked"), and that reassurance can mask the real lesson — the error should never have propagated. The cost of a downstream catch is far higher than a source-side check, and the reconciliation layer's scarce attention is best spent on *novel* errors, not ones you already know how to prevent.

**How to apply:** treat every "another agent corrected me" as a trigger to install a guardrail at the ORIGIN — a boot/closeout step, an instruction-file rule, or a verify-before-propagate gate — so the same class can't recur. Log-only (a LESSONS row) is not enough; it's passive. Make it active: something that fires automatically next session. Concrete precedent: the WATT refutation → a 🔴-elevation gate written into AEOLUS CLAUDE.md STANDING DISCIPLINES; the PROME git catch → a path-scoped-commit guardrail in its GIT PROTOCOL. Rule of thumb: the reconciliation backstop should be catching things nobody could have foreseen, not repeats. Related: [[feedback_single_source_liveevent_is_a_lead]], [[finding_pathspec_commit_race_safety]], [[finding_adversarial_verify_own_convergence]], [[finding_sibling_agent_protocol_drift]], [[feedback_flag_friction_realtime]].
