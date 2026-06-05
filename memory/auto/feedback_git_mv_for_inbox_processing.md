---
name: git-mv-for-inbox-processing
description: "When moving inbox files to processed/ subfolder, use `git mv` not bash `mv` — bash mv leaves the deletion unstaged and creates a two-commit hygiene problem."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6a9a8e5c-357a-496c-9533-e39f59f4376c
---

When processing inbox items by moving them to a `processed/` subfolder:

**Use:** `git mv inbox/X.md inbox/processed/X.md`
**Not:** `mv inbox/X.md inbox/processed/` followed by `git add inbox/processed/`

**Why:** Bash `mv` is filesystem-only. Git sees the original tracked path as "deleted in working tree" and the new path as "untracked." When you `git add` the new path, only the addition gets staged — the deletion at the old path stays unstaged. The commit then shows up as "create new file" rather than rename, and the deletion sits as pending git status until separately staged.

**How to apply:** Any time you process an inbox or outbox file by moving it to a subfolder, default to `git mv`. If you've already done `mv` + `git add`, follow up with `git add -u <directory>` to stage the deletions before committing — otherwise you end up with a two-commit cleanup (caught this in 5/21 BROCK session: cd6fcd82 added new paths, 8447f425 cleaned up the deletions).

Related: [[feedback_check_staged_before_commit]] — running `git diff --cached --stat` before commit would have caught this (would have shown only additions, no corresponding deletions, signaling the rename was incomplete).
