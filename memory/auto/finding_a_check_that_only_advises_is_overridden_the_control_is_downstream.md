---
name: finding_a_check_that_only_advises_is_overridden_the_control_is_downstream
description: "The failure is almost never at detection — it is DOWNSTREAM of a working instrument, at the override/resolution/invocation step. A check that only PRINTS or ADVISES gets overridden; a self-caution is not a control; looking at a flag does not tell you which way to resolve it. The real controls are (a) a check that BLOCKS, not advises, and (b) an independent receiver verifying at the artifact before acting. One afternoon produced ~6 instances of the same shape. Fleet synthesis 2026-09-05."
metadata:
  node_type: memory
  type: feedback
symptoms: "the guard printed the number and I committed anyway · I measured and overrode my own abort · a self-caution is not a control · read the flag and resolved it the wrong way · the instrument worked but the defect shipped · a check that advises vs a check that blocks · keep checks in the battery not in memory · the detector fired, the habit downstream failed"
---

**Across a whole session of finding defects, the pattern was not that detectors failed — they fired every time. The defect shipped DOWNSTREAM of a working instrument, at the human/agent step that reads the instrument and then does the wrong thing anyway.** Six instances in one afternoon, same shape:
- a commit-subject guard **printed "len=104"** and the author committed the 104-char subject anyway (measured, read the number, overrode the abort);
- a `claim_check` **fired correctly** on a date/weekday mismatch and the reviewer **resolved it backwards**, erasing the tell;
- a desk wrote *"read this sceptically, nothing found is thesis-adverse"* and then **committed the exact overclaim the caution described** — a self-caution is not a control;
- a fix written to repair a one-directional leg **carried the same one-directional blindness** (checked a review source EXISTED, never that it RECURS);
- a coordinator relayed a plausible framing (validate_all fills the gap; the chain "worked as designed") **ahead of verifying it**;
- an event fired (an overdue grade) with **no session invoked** to act on it.

**The discriminator that matters: does the check BLOCK or merely ADVISE?** A blocking check cannot be overridden by habit — the same session's `commit_check.py` *rejected* six long subjects and every one got fixed, while the guard that only *printed* the length got ignored. "Keep checks in the battery, make them block, none in memory" (a check you have to REMEMBER to honor is already lost).

**The second control is symmetric and independent: the receiver verifies at the artifact before acting.** Every one of the six was caught not by the author but by whoever received the claim and checked the primary — PROME caught a peer's stale ledger flag, the peer caught PROME's framing, an external review caught the fabrication and the mislabel. That is not a string of errors, it is a control working repeatedly and in both directions. `[[finding_a_flag_resolved_in_the_wrong_direction_launders_the_defect]]` · `[[finding_a_correction_pass_is_unreviewed_work]]` · `[[finding_adoption_is_not_validation]]`

**How to apply:**
- **Prefer a check that BLOCKS over one that prints.** If a guard can be overridden by committing anyway, it is documentation, not a control — wire it to abort.
- **A self-caution ("read this sceptically") is not a control** — it does not stop the act it warns about. Route the claim to an independent check instead.
- **The failure is downstream of the instrument** — when a defect ships past a check that fired, audit the resolution/override/invocation step, not the detector.
- **Build the missing invocation** (the spawn-driver): a detector whose session never runs is a check nobody honors — the same failure class, one layer up.
