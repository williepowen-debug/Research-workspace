---
name: feedback_defer_push_coordinate
description: Commit locally but do NOT push to GitHub unless Will says so — he coordinates pushes across many concurrent agents
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 00ec0950-e775-4a07-8003-3c090c4b2848
---

When many agents are operating at once, Will wants to coordinate pushing to GitHub himself. Commit locally at closeout, but do NOT `git push` unless he explicitly says he's ready. State that the commit is local-only and the push is deferred.

**Why:** Concurrent agents share one branch; uncoordinated pushes cause divergence/rebase churn and risk other agents' uncommitted work (see [[feedback_git_reconcile_scope]]). Will serializes pushes when the tree is clean across agents.

**How to apply:** At session end, do `git reset HEAD` → `git add AGENTS/<NAME>/` → commit. Skip the push. Note "pending push, local-only" in SCRATCH. Never pull/rebase while other agents have uncommitted working-tree changes.
