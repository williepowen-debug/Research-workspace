---
name: feedback_bound_follow_up_reviews_to_the_diff
description: Will wants reviews not laborious — a follow-up read gets ONLY the fix diff, a time box and its own few counterexamples, never a whole re-review
metadata:
  type: feedback
symptoms: "reviews take very long", "just re-reading", a fourth/third read re-running every earlier counterexample suite, a reviewer re-auditing unchanged code
---
Will, 2026-11-01 10:26 ET (WQ-584, verbatim): *"However can we make sure its not TOO laborous or burdensome? Sometimes these reviews seem like that take very long and I am not sure if they are productive or just re-reading."*

Evidence from that episode (WQ-583 code half): reads #1–#3 were whole-change reviews (~9, ~48 and ~13 min of agent time); every real defect they found came from a NEW counterexample the reader built, none from re-reading. The bounded read #4 (only a ~120-line tightening diff, 4–6 own counterexamples, <40-line report, "delete nothing") took ~3 min and still found two real residue gaps.

**Why:** cost and attention are Will's; re-verification of unchanged code adds time, not catches. Productive review = a stranger trying to break the specific change.

**How to apply:** a first read of a consequential change may be whole; every follow-up read gets the diff since the last read, the prior ledger's relevant entries only, a time box (~15 min), a counterexample budget, a short report cap, and "delete nothing / no cleanup" (a reader's rm -rf cleanup prompted Will 10/31). Do not ask it to re-run earlier suites — PROME's own test run covers regressions. Related: [[feedback_fewer_checkers_and_rules]] · [[finding_a_correction_pass_is_unreviewed_work]] · [[feedback_coldreaders_run_on_opus_not_fable]].
