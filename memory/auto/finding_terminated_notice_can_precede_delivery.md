---
name: finding_terminated_notice_can_precede_delivery
description: "A teammate_terminated notice + an empty disk check does NOT prove a spawned agent delivered nothing — its commits/message can land after the check; never assert absence in a re-spawn prompt, instruct verify-existing-first instead."
metadata: 
  node_type: memory
  type: project
  originSessionId: 8c12aacc-d9ba-4741-843a-dd434a995c55
  modified: 2026-07-20T20:56:10.498Z
---

2026-07-20 eve (ZION Q2 grade): PROME received `teammate_terminated` for a freshly spawned REGINALD, disk-checked its dir (no new commits), and re-spawned with the assertion "a prior spawn died before doing any work — you are starting clean; nothing has been graded yet." That assertion was FALSE: the first spawn completed both deliverables and committed (e8371ebf + 47243447) in the window between the disk check and the re-spawn's start; its delivery message arrived later. The re-spawn only avoided duplicate/conflicting work because it checked disk itself and switched to verify-not-redo (net add 235237f5, every figure independently re-verified off the primary).

**Why:** the termination signal and the agent's actual work/commit tail are not synchronized — a "died" notice can be premature or spurious, and commits land asynchronously. A single point-in-time disk check only bounds what existed *then*.

**How to apply:** on a terminated/failed signal for a spawned agent, (1) disk-check, then (2) re-spawn with "check `<dir>` for existing partial/complete work FIRST; if found, verify it rather than redo" — never with a positive claim that nothing exists. Related: [[finding_never_received_is_not_doesnt_hold]], [[finding_two_phase_spawn_grader_contract]].
