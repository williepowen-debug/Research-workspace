---
name: feedback_defer_push_coordinate
description: Commit locally but do NOT push to GitHub unless Will says so — he coordinates pushes across many concurrent agents
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 00ec0950-e775-4a07-8003-3c090c4b2848
---

When many agents are operating at once, Will wants to coordinate pushing to GitHub himself. Commit locally at closeout, but do NOT `git push` unless he explicitly says he's ready. State that the commit is local-only and the push is deferred. **This OVERRIDES the root `CLAUDE.md` Git Protocol's "push at session end" line** — if root and this disagree, this wins (root is a known-stale default pending PROME reconciliation; see CARL→PROME outbox 2026-06-08).

**Why:** Concurrent agents share ONE working tree and ONE branch. An uncoordinated push moves shared origin while other agents have unpushed commits queued on it — sweeping the whole train up on the wrong trigger, forcing rebase-churn on everyone's SHAs ([[finding_forced_update_rebase_churn]]), or diverging origin mid-flight. **PROME makes this acute, not incidental:** as coordinator it has the most push-reach and often shares the same tree — an uncoordinated PROME push is the highest-blast-radius case. Only Will holds the full picture of who is mid-session, so the push decision is his, not any local closeout's. Validated 2026-06-08: CARL pushed at closeout (clean, but premature) while BROCK/HAWK/PROME had concurrent work.

**How to apply:** At session end, commit with **pathspec** (`git commit AGENTS/<NAME>/<file>`; new files `git add <specific files> && git commit <same files>`) — **never `git reset HEAD` or `git add <dir>`** ([[finding_pathspec_commit_race_safety]]). Skip the push. Surface "committed local-only, ready to push — your call" and note pending push in SCRATCH. Never pull/rebase while other agents have uncommitted working-tree changes. Push only on Will's explicit go.
