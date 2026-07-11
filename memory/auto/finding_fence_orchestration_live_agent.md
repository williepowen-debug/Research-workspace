---
name: fence-orchestration-live-agent
description: "Directory-fence teams-mode orchestration against a LIVE agent works, but the fence must be announced to the live session AND its commits watched — a broad-pathspec commit from the live side silently sweeps the orchestrator's in-flight edits into the wrong commit."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ded45980-2963-4f40-90b6-2ebbba95b375
---

Pattern validated 2026-07-10 (DAEDALUS restructuring CARL's `sub_agents/` while CARL ran live): orchestrator claims ONE subdirectory as an exclusive fence, spawns named editor agents (disjoint file sets, no git commands), batch-commits per work package by explicit pathspec, routes everything touching the live agent's judgment or top-level files as drafts/task-packets instead of edits.

**Why:** it un-blocks structural work from the owner's session bandwidth without violating the permission+idle guard — the fence substitutes for idle on a bounded path set, per operator direction.

**How to apply:**
- The fence is only real if the LIVE session is told (operator relays one line: "X owns dir Y this session — hands off; name files in commits"). Without it, expect the failure observed: CARL's `528f3754` committed with a broad pathspec mid-window and swept the orchestrator's in-flight edits into its own commit.
- After any live-side commit in the window, diff the swept files against the editor's intended final state before your own batch commit (content survived intact in the observed case, but verify — don't assume).
- Drafts for judgment items go INSIDE the fenced dir as clearly-bannered DRAFT files (owner ratifies); the completion note to the owner's inbox lifts the fence explicitly and carries the ratification queue.
- **PROME advisor refinements (7/10 review):** (1) prefer target-idle or hand-edits-to-owner-to-commit over live-concurrent — "verified intact" won't always hold; worktree isolation is the escalation for write-heavy concurrent runs. (2) Draft-only purity has an exposure cost: a canonical surface known to assert falsified facts needs a mechanical `BYPASSED / do-not-cite` banner ON THE SURFACE ITSELF even when the fix is judgment-gated — the warning in a sibling draft file doesn't protect a direct reader (GIG got this stamp late; PHAN got it right at conversion). (3) The meta-agent's cross-dir write authority stays per-batch gated — never a standing license.

Relates [[finding_pathspec_commit_race_safety]], [[feedback_named_spawn_teams_mode]], [[feedback_check_staged_before_commit]].
