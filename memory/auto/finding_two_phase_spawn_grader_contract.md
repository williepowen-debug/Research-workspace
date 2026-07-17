---
name: finding_two_phase_spawn_grader_contract
description: "For a session that must wait hours for a scheduled data release: split it into two spawns with a FROZEN MECHANICAL GRADER as the handoff contract (prep session builds grader+memo, shuts down; fresh session at release-time runs the grader). Zero context loss, no idle session, and the grader's input-refusal doubles as stale-data discipline."
metadata: 
  node_type: memory
  type: finding
  originSessionId: d486914a-6e91-4f37-a4b2-9bf0d4ffeeaa
---

**The pattern (validated 2026-07-17, BRENT COT session):** a graded event (CFTC COT, 3:30 PM release) sat ~4.5h after the natural prep window. Instead of holding an idle teammate or cramming prep+grade into one session, PROME ran a **two-phase split**: Phase-1 spawns early → does all prep → **writes the handoff as executable artifacts, not prose** — (a) a mechanical grader script that pulls the primary, self-checks the frozen baseline anchor, and **refuses to run unless the release's report-date matches** (exit-coded), (b) a pre-print memo with frozen thresholds + branch read-throughs pre-registered → commits, pushes, **shuts down**. At release-time (coordinator alarm), a **fresh Phase-2 spawn** reads the memo, runs the grader, grades, integrates, delivers.

**Why it beats the alternatives:** an idle-held session burns nothing but risks API-error death mid-wait and same-name collision classes; a single crammed session grades under time pressure with un-frozen terms. The split forces the pre-registration to be COMPLETE (the Phase-2 agent can't ask Phase-1 anything — if the grader+memo don't suffice, the handoff was underspecified, which is itself the test). Validated: Phase-2 reproduced the grade with zero context loss; the grader's report-date refusal rejected **40 consecutive stale API polls** and pushed the agent to a faster primary path (raw CFTC text file) rather than a stale grade.

**How to apply:** (1) Phase-1's deliverable = grader + frozen-terms memo, explicitly written for a cold reader; (2) the grader must verify its OWN baseline anchor against the primary (drift check) AND refuse wrong-vintage input (stale-data discipline as code, not vigilance); (3) the coordinator holds the wake alarm (event-anchored, not clock-narrated — see the wall-clock corollary in [[finding_subagent_prefire_date_verification]]); (4) release Phase-1 only after verifying its commits are on origin. Related: [[finding_teams_mode_domain_agent_spawn]], [[feedback_subagent_prompt_discipline]].

**Corollary (same day):** the deliver-before-idle contract in spawn packets should name the agent's NEXUS_BRIEF fold explicitly — 2 of 11 agents (RED, LIQUID) delivered everything else but skipped the brief unprompted, leaving 7-11d-stale synthesis inputs; the ones told explicitly all folded it.
