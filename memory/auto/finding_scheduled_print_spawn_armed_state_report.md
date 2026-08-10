---
name: finding_scheduled_print_spawn_armed_state_report
description: Agents spawned ahead of a scheduled release (BLS print, AMC earnings) go idle on a poll timer — indistinguishable from a dropped task unless the spawn prompt REQUIRES an armed-state report before first idle; 4/4 nudges on 7/21 found armed-not-dropped, but only the nudge proved it.
metadata:
  type: feedback
---

Agents spawned to grade a SCHEDULED future release (BLS 10:00 print, 4:05 PM earnings, a settle time) correctly arm a background timer/poller and go idle until it fires. But their idle notification is byte-identical to a dropped-task idle, so the coordinator can't distinguish "armed and waiting" from "boot-completed and forgot the poll loop" without a status-check round-trip.

On 2026-07-21 (four-rail day), 4 print-graders (LABOR, CORAL, REGINALD, OZK) all used the armed-timer pattern successfully — but 3 of them idled silently first and each cost a coordinator nudge + reply cycle to verify. REGINALD, unprompted, sent an armed-state report before idling (scaffold staged · frozen terms located · poller target + cadence + landing precedent) and needed zero chasing — that report format is the fix.

**Why:** deliver-before-idle can't apply literally to a task whose input doesn't exist yet; the deliverable before the print is the ARMED STATE itself. An unreported armed state is indistinguishable from a silent failure, and the failure mode it hides (agent waits for a filing on the wrong surface — e.g. OZK files with FDIC, not EDGAR) is exactly the one you want surfaced pre-deadline, when there's still runway to fix it.

**How to apply:** any spawn prompt for a scheduled-release grade must require, BEFORE first idle: (1) boot/frozen-terms confirmation, (2) scaffold staged with RESULT columns pending, (3) poller armed — target surface + cadence + expected landing time (and the verified release calendar), (4) any pre-stageable partial grade (a leg that is already arithmetically decidable — e.g. a streak leg dead regardless of the print). Treat a silent idle before the scheduled time as a status-check trigger, not an alarm. Related: [[finding_terminated_notice_can_precede_delivery]], [[feedback_subagent_prompt_discipline]].

**Instance 2 (2026-08-10, fin-conditions forum — the coordinator-side half of the same lesson):** an idle teams-mode agent CANNOT wait for a clock — "hold your post until the 16:15 settle prints" + "deliver before idling" is a self-contradictory contract, because idling is the only thing an agent between tool rounds can do, and nothing wakes it at settle time. VIOLET idled holding exactly as instructed and would have sat forever. The fix is ownership of the clock: the COORDINATOR sets the timer (background `sleep` task → re-invoke) and sends the wake message at the scheduled time; the agent's job is only to be resumable. Corollary of the same root as instance 1: before a scheduled input exists, the agent's deliverable is its armed/resumable state — the WAITING itself always belongs to whoever has a timer, and in teams-mode that is the coordinator, never the idle spawn.
