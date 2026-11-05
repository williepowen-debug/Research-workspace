---
name: finding_rebase_continue_blames_conflicts_for_a_foreign_dirty_file
description: git rebase --continue refuses on ANY unstaged tracked file and blames merge conflicts; rebase --abort silently wipes a foreign dirty file
metadata:
  type: project
symptoms: "You must edit all merge conflicts and then mark them as resolved using git add" while status shows every conflict staged; rebase will not continue; another desk's file is dirty
---

In a shared worktree, `git rebase --continue` refuses while ANY tracked file is unstaged, including a file unrelated to the rebase, and prints "You must edit all merge conflicts and then mark them as resolved using git add". The message is wrong for this case: the conflicts are resolved. `git rebase --abort` silently discards a foreign dirty file's changes. Both reproduced in a scratch repo, ORACLE 2026-11-04.

**Why:** a desk's boot gate dirtied `GATE_LOG.tsv` two minutes after a rebase stopped, so the rebase could not finish. An approved abort would have erased that desk's row and thrown seven live sessions back 299 commits.

**How to apply:** when --continue refuses with conflicts resolved, run `git diff-files --name-only`. A foreign path there is the block: ask that desk to commit or clear its own file. Never stash, reset, `assume-unchanged` or hand-move the branch. Before approving any abort, check for dirty files. Related: [[finding_guard_correctness_and_wiring_are_independent]].
