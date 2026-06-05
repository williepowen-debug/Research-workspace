---
name: Check staged files before committing
description: Always run git diff --cached before committing to catch pre-staged files from other agents/sessions
type: feedback
---

Always run `git diff --cached` (or `git status` checking both staged AND unstaged sections) before committing. Other agent sessions may leave files in the staging area. A `git add` of specific files + `git commit` will include ALL staged files, not just the ones you just added.

**Why:** On Apr 2, a CARL-only commit accidentally included pre-staged RED and REGINALD changes (11 RED files deleted, REGINALD inbox/thesis modified). The git add only specified CARL files but the commit picked up everything in the index.

**How to apply:** Before every `git commit`, run `git diff --cached --stat` to verify ONLY the intended files are staged. If unexpected files appear, unstage them with `git restore --staged <file>` before committing.
