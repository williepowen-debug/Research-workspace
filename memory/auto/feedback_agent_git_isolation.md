---
name: Agent Git Isolation
description: When pushing changes for one agent, never stash/commit other agents' files — scope strictly to the agent's directory
type: feedback
---

When committing and pushing for a single agent (e.g., SAM), NEVER use `git stash` on the full working directory — it captures all agents' uncommitted changes and can leak them into the wrong commit on stash pop. Instead: (1) only `git add` specific files in the target agent's directory, (2) always verify scope with `git diff --cached --stat` before committing, (3) treat other agent directories as READ-ONLY.

**Why:** Accidentally committed CARL's file deletions (80 files) while pushing SAM's structural upgrade. The stash pop left CARL changes staged, and they got swept into SAM's commit. Had to revert. Will was rightfully upset — agents should never touch each other's files.

**How to apply:** Any time git pull/push requires resolving upstream divergence while other agents have local changes, use `git fetch && git rebase` with only the target agent's files staged, or commit the target files first before pulling. Never stash the whole repo. **Additional:** When unstaging other agents' files before committing, watch for staged renames — a rename is two operations (delete old path + add new path). Always `git reset HEAD` BOTH paths together, or verify with `git diff --cached --stat` that no other-agent files remain staged before committing.
