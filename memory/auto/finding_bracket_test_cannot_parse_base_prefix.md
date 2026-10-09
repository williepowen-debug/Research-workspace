---
name: finding_bracket_test_cannot_parse_base_prefix
description: bash [ -ge ] silently fails forever on 10#-prefixed numbers — timers never fire, monitors expire eventless
metadata:
  type: feedback
symptoms: Monitor expired with no events · integer expression expected · until loop never exits · timer never fired · background wait loops forever
---

`[ 10#$(date +%H%M) -ge 1605 ]` is INVALID in `[`/`test` — the `10#` base prefix is ARITHMETIC syntax (`(( ... ))`), not test syntax. The test errors ("integer expression expected") and returns FALSE every iteration, so an `until` loop waits forever and a Monitor armed on it expires "with no events" — silence identical to still-waiting (n=2 in one session, 2026-10-09: a Monitor and a background timer both died this way; the only tell was the error spam in the task's output file, which nothing reads until you look).

**Why:** the base prefix exists to defeat octal parsing of zero-padded clock output (`0945`); putting it inside `[` trades an octal bug for a permanent-false bug — strictly worse, because octal only breaks on 08/09 minutes.

**How to apply:** for clock comparisons in shell use arithmetic: `until (( 10#$(date +%H%M) >= 1605 )); do sleep 15; done` — or compare ISO strings lexically (`[ "$(date +%H%M)" \> "1604" ]`). After arming any wait loop, verify the FIRST iteration doesn't print an error to the task output. Related: [[finding_heredoc_terminator_ends_the_and_chain]], [[finding_a_check_that_only_advises_is_overridden_the_control_is_downstream]].
