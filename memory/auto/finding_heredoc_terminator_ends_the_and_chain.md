---
name: finding_heredoc_terminator_ends_the_and_chain
description: "A heredoc inside a shell && chain ends the chain at its terminator; every statement after it runs UNCONDITIONALLY — so a gated commit commits after its gate aborted (n=2, PROME, one day)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: a5d581cd-9acc-4397-bf1b-7f3094abfbe7
symptoms: "commit landed after the gate printed nothing; commit message describes fixes the tree does not hold; edit aborted but the commit ran; chain stopped early yet git add/commit still executed; a 2-file commit where 4 were expected; heredoc followed by git commit in one tool call"
---

**The mechanism (PROME 2026-09-18, twice in one day — `f00ece4f9` at 09:18 in `prome-2a`, `507495a6e` at 10:4x in `prome-0e`):** a Bash tool call of the shape

    test <gate> && python3 edit.py && cat > msg.txt <<'EOF'
    subject
    EOF
    git add A B && git commit A B -F msg.txt

reads as one chain and is not. The heredoc's terminator line ends the `&&` chain; `git add … && git commit …` on the next line is a NEW statement that runs whatever the gate returned. In both instances the gate FAILED (a byte-cap check; a subject-length test), the edits were never made, and the commit ran anyway, with a message describing work the tree did not hold. The second instance happened ~75 minutes after the first had been written into the day's memory note and HANDOFF as a lesson, by the same desk.

**Why it is invisible:** the transcript shows the gate's failure and the commit's success in one tool result; a reader who expects a chain sees "the chain ran" and does not check WHICH links ran. The message, written before the gate, asserts the gated work as done (`finding_adoption_is_not_validation`; `finding_a_correction_pass_is_unreviewed_work`).

**The rule:** files first, as SEPARATE statements (message file, edit script, test script); then ONE `&&` chain with NO heredoc anywhere in it, whose LAST link is the commit; and a gate that must stop the chain runs BARE, never `gate | tail` (the `&&` sees `tail`'s rc; `PROME/tools/hooks/pipeline_rc_block.py` only sees an explicit `$?` read). A commit that ran after a failed gate is documentation debt: note it in the NEXT commit's body (root 4b), never amend.

Related: [[finding_add_with_one_bad_pathspec_stages_nothing]] (in an &&-chain the exit code is the only tell) · [[finding_a_check_that_only_advises_is_overridden_the_control_is_downstream]] (the subject-length hook that now blocks pre-execution caught the same author's 4th and 5th over-cap subjects the same morning) · [[finding_write_timestamps_from_the_clock_not_the_narrative]].

**n=3 (PROME 2026-09-24 00:4x ET, `prome-4d`, commit `3a27103d6` at 00:48 ET):** an ORCH_LOG update script (the WAL touch-2 receipt) (`python3 - "$TS" <<'PY' … PY`) raised an AssertionError, and because the heredoc terminator ended the `&&` chain the `git mv` and `git commit` that followed ran anyway — the commit shipped the DOCKET edits and the memo rename with the ORCH_LOG update missing, and the failure was found seven hours later at consume time. Two independent mitigations both worked afterwards: (1) wrap the gated tail in `if python3 - <<'PY' … PY\nthen …; else echo FAILED; fi` — the heredoc closes INSIDE the `if` condition, so the `then` branch really is conditional; (2) build every edit in memory and write files only after every assertion passes, so a failed script leaves no half-written file for an unconditional commit to sweep. **Promotion flag (n=3) → PROME's next flow pass.**
