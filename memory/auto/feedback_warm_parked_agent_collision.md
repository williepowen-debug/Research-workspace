---
name: warm-parked-agent-collision
description: "leaving named teams-mode agents \"warm\" across sessions causes next-session same-name collisions + cleanup-sweep kills; release at closeout or use collision-proof aliases"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9d416841-d1e3-4b73-96e0-d5506c142ee6
---

Named teams-mode (mailbox) agents left "parked warm" across a session boundary keep occupying their names/tmux panes. When the next session spawns a same-named agent (e.g. a fresh `CARL`), it collides with the lingering warm one — and a parallel session's cleanup sweep keyed on the name (`CARL/CORAL/REGINALD`) kills the fresh spawn as collateral. Happened 2026-06-25: the prior terminus cluster parked CARL/CORAL/REGINALD warm "pending Will release"; a parallel session finally released them mid-spawn and took out the new front-half CARL with them.

**Why:** teams-mode addressability is by name; warm agents persist across sessions; a name is a shared, sweepable handle, so two sessions touching the same names collide.

**How to apply:** (1) RELEASE teams-mode agents at closeout via shutdown_request — do not "park warm" across session boundaries. (2) If warm same-named agents might already exist, spawn under a collision-proof alias (`CARL_FH`, `REGINALD_T`); the alias survives a `CARL`-name sweep and the agent reconstitutes identity from its STATUS regardless of handle. (3) Scope spawns RESEARCH/DRAFT-ONLY so a sweep loses no work — the deliverable returns via the mailbox message even if the agent dies right after. See [[feedback_named_spawn_teams_mode]], [[finding_teams_mode_domain_agent_spawn]].
