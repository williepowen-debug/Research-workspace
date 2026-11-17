---
name: feedback_start_walter_at_weekday_boot
description: On weekdays, if no WALTER window is live when PROME boots, PROME starts one (Will 2026-11-17, WQ-709); it is not an unattended run and WQ-388's decline of self-scheduled sweeps stands
symptoms: PROME boots on a weekday morning and ListAgents shows no walter session; scheduled 08:30 ET releases with no news card hours later; a desk woken late because WALTER's card came late; the collector ran and nothing read it
metadata:
  type: feedback
---

Will, 2026-11-17 18:16 ET in PROME's chat, verbatim: "agreed", to PROME's recommendation shown at 18:15 ET, whose first part read: on weekdays, if no WALTER window is live when PROME boots, PROME starts one. Record: `PROME/WILL_QUEUE.md` row 709.

**Why:** on 11/17 PROME booted at 08:30 ET, WALTER's window was opened by Will at about 11:43 ET and its first cards came at 11:49 ET, so the 08:30 ET releases (retail sales, import prices) went without a card for over three hours and CARL was woken only at 11:53 ET. The collector had run; nothing was reading it. The same delay left BRENT writing its 11/16 oil read without knowing of two tanker hits.

**How to apply:** at a weekday boot, after the gate and before the report, check ListAgents and the process list for a WALTER session (the ordinary launch preflight). If none is live, launch WALTER through `scripts/agents.py WALTER --opus --new` with its ordinary startup, log the touch in ORCH_LOG, and name it in the boot report under "Done without asking". If one is live, do nothing: it is Will's window. This is not an unattended run: it happens only inside a PROME session Will has started. WQ-388 (WALTER may not self-schedule an unattended sweep) is unchanged. Weekends and holidays: no launch unless Will asks. Will can withdraw this by saying so. PROME's reading, not Will's words: a WALTER window PROME starts this way is PROME's touch for closeout purposes (ask, receipt), unlike a window Will opens himself.
