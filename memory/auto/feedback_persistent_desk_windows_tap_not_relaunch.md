---
name: feedback_persistent_desk_windows_tap_not_relaunch
description: "Will's direction 2026-11-07: move toward desk windows kept open and persistent, which PROME taps by message as needed; a desk that finishes holds rather than closes"
symptoms: "desk delivered so ask it to close out, launch a new session for a follow-up, close the window to free memory, relaunch instead of message"
metadata:
  type: feedback
---

Will 2026-11-07 09:41 ET, verbatim: "I want to start to move towards a workflow where we have agents windows open/spawned/persistent and you can merely tap them or direct them as we deem necessary." Direction, built up gradually; he said "start to move towards".

**Why:** a tap on a live desk costs little and needs no launch. It builds on his 11/6 words (19:46 ET, keep sessions persistent, PROME directs them; 16:38 ET, windows stay open).

**How to apply:** after a delivery, tell the desk to hold with no timer; do not ask it to close out merely because the task ended. Follow-ups go by SendMessage (standalone text, name the artifact, tell it to reread its files, since idle desks auto-compact). Launch only after the Desk-spawn preflight, when no live owner exists. Actual end-of-day and machine-switch closeouts still run. Fresh context for a closed-out desk: PROME stops that session, then launches through scripts/agents.py, as on 11/7 at 09:42 ET.

**Limits, unchanged:** memory sets how many stay open (laptop about 270 to 300 MB per desk with 2.4 GB available at 7 sessions, floor 1 to 2 GB; desktop ceiling about 20 sessions). Windows die with a reboot or machine switch and are not in tmux. A desk does not start itself: no unattended authority. Related: [[feedback_launch_desks_through_agent_launcher]], [[feedback_doorbell_live_desks_directly_never_paste_blocks]], [[feedback_permission_to_act_is_not_a_reason_to_act]].

**Instance 2026-11-12 (PROME prome-e8, desktop), a miss:** PROME ended LABOR, CYPHER and VULCAN within minutes of their deliveries, citing memory, then had to boot VULCAN again eight minutes later for WALTER's urgent Nvidia card. Cause: a NOW-page line ("PROME ends a desk's window after its push receipt is verified") contradicted this memory and was followed instead; free memory was 2.3 to 4.0 GB, above the floor. Will 09:38 ET, verbatim: "I wonder if it would be more efficient to keep the agent window open rather then rebooting a new window?" **Sharper rule (PROME's wording):** hold by default; end a window only when free memory is near the floor AND a launch is owed, furthest next wake first, and say so in chat first. A desk with a row due the next day is never the one to close.
