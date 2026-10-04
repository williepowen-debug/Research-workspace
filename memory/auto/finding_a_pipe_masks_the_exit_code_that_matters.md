---
name: finding_a_pipe_masks_the_exit_code_that_matters
description: A `| tail` / `| cut` after a gated command (commit_check, an apply script) returns the PIPE's exit code, so a refusal reads as success and the next step (push, baseline) runs on the wrong state
metadata:
  type: feedback
symptoms: "commit refused but push ran" · "script printed a traceback and the chain continued" · "rc=0 after a ❌ line" · "baseline recorded at someone else's commit" · "apply did not run but the next step did"
---

A pipeline's exit status is the LAST command's. `python3 commit_check.py … | tail -2` returns `tail`'s 0 even when the commit was refused; `python3 apply.py | tail` returns 0 when the script crashed. The step after then runs on a state that never changed — a push that pushes a peer's commit, an ARGUS baseline recorded at the wrong HEAD, a rotation reported applied that never ran.

**Why:** `set -e` does not see a non-final pipeline member's failure (without `pipefail`), and `&&` chains only test the pipe's tail. The tell is a ❌ or a traceback ABOVE a line that reads like success. n=3 in one day (2026-10-03, PROME): the rotation-bundle apply (SyntaxError, masked), the FALCON packet commit (subject >100, masked ⇒ safe-push + baseline ran one commit early), the Deck-pickup commit (subject >100, masked).

**How to apply:** never put a gated command behind a pipe. Redirect to a file and read it after: `cmd > out.txt 2>&1; rc=$?; tail -2 out.txt; echo rc=$rc`, then gate the next step on `$rc`. Or `set -o pipefail`. Re-measure the TARGET (file size, `git log -1`) before reporting an apply or a commit. Related: [[finding_heredoc_terminator_ends_the_and_chain]] · [[finding_record_of_an_action_is_not_the_action]] · [[finding_attribution_authenticates_a_figure_its_named_source_never_produced]].
