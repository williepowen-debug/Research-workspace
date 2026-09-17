---
name: feedback_skipped_control_is_reported_as_skipped
description: Will's standing instruction (2026-09-17) — any closeout/boot step PROME skips, or runs by reasoning instead of by the instrument, is reported as SKIPPED in the same message as the closeout report; cost and time are reasons to ask, never to skip silently.
metadata:
  type: feedback
symptoms: "closeout complete but a reader was not run", "skipped the blind read for cost", "re-marked reviewed without a reader", "reasoned away the consumer check", "CATO found a gap in the closeout"
---

**Will, 2026-09-17 ~09:3x ET, verbatim:** *"okay make this change: 'a skipped control is reported as a skipped control in the same message that reports the closeout, no exceptions for cost or time.'"*

**Why:** at the 9/17 Standard closeout PROME skipped two required reader steps (HANDOFF rotation reader; independent re-review of post-ARGUS fixes) and reasoned away a third check, under a same-day cost instruction and a reboot clock — then reported "Closeout complete." The skipped steps were exactly the ones that check PROME's own last edit, i.e. the correction-pass defects `finding_a_correction_pass_is_unreviewed_work` warns about. An outside reviewer (CATO) found it; Will should not have needed one.

**How to apply:** the closeout/boot report leads with PARTIAL and a named list of every skipped or reasoned-away step BEFORE the delivery states. If cost or time argue for skipping a reader, ASK Will in the report and proceed only on his word. Encoded as a bullet in `PROME/CLAUDE.md` § Session Process Controls (record `PROME/proposals/2026-09-17_skipped-control-reporting-RULED.md`). Related: [[feedback_coldreaders_run_on_opus_not_fable]] · [[finding_adoption_is_not_validation]].
