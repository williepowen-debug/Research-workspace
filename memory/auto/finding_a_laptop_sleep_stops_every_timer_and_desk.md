---
name: finding_a_laptop_sleep_stops_every_timer_and_desk
description: A Windows sleep suspends WSL whole: timers, waiting desks and watchers all stop with no error; check the sleep setting before relying on any of them
metadata:
  type: project
symptoms: timer never fired; desk window idle for a day; watcher last poll hours ago; Network is unreachable on wake; the close launch did not happen; uptime looks continuous
---

On the laptop (`WilliePOwen`, WSL2), Windows sleep suspends everything at once: PROME's own session, every desk window, background timers and polling watchers. Nothing errors. On wake the processes resume as if no time passed; `uptime -s` still shows the original boot, and a timer set for a clock time that passed during the sleep fires late or its work is simply gone.

Instance (n=1): Fri 2026-11-20 about 14:53 ET to Sat 2026-11-21 about 17:50 ET. PROME had set a 16:03 ET timer for the close launches at 14:42 ET, in the same message in which it told Will the laptop had to stay awake. The close reads (HENRY, VIOLET, TERRY), the closeout and VULCAN's weekly slot 11 and GPU reading 11 were all missed; the slot readings are not recoverable off-cadence. VULCAN logged it as its L-123, BRENT's wait job failed with "Network is unreachable" on wake.

**Why:** a caution said aloud is not a control; nobody checked the machine's sleep setting, and the setting is Will's.

**How to apply:** before relying on a timer, a held-open desk or a watcher across more than a few minutes on the laptop, ask Will whether the laptop is set to stay awake on power, and say plainly that the work is lost if it sleeps. For a dated slot that must be read at a clock time (a close read, a cadence slot), prefer a cloud routine or the desktop. On any wake, compare `date` with the last commit or log line before trusting that a "running" desk did anything. Related: [[finding_a_stamp_written_from_narrative_drifts_from_the_wall_clock]], [[finding_closed_out_teammate_does_not_resume_on_reping]].
