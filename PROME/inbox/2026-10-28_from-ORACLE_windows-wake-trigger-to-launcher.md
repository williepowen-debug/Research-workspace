# ORACLE → PROME — Windows wake trigger for scheduled runs: Will wants it in the Agent Launcher, not as an ORACLE install

**Will, 2026-10-28 21:18 ET, verbatim:** "I think this should be a part of the agent launcher I have been building if anything. Lets just send a note to Prome inbox instead"

**Context:** ORACLE's daily pulls-only routine (WQ-527 C, L847) runs from a laptop user crontab, which fires only while WSL is up. A Windows Task Scheduler task would close that gap: on a weekday schedule it runs `wsl.exe -d Ubuntu -u willi -- bash <script>`, which starts WSL if it is down, runs the job, and lets WSL idle back down. Its settings can also catch up a run missed while the laptop was off ("run as soon as possible after a missed start") and wake the laptop from sleep. The routine is idempotent, so a Windows trigger and cron can coexist without double reads. **Not installed** (ORACLE offered; Will declined in favour of the launcher).

**Will's direction:** if built, the Windows wake/catch-up trigger belongs to the Agent Launcher (CATO's custody per `scripts/AGENT_LAUNCHER.md`) as a general facility for scheduled desk jobs, not as a one-off ORACLE task.

**Design notes for whoever builds it (from ORACLE's look tonight):** distro name `Ubuntu` (WSL2) on the laptop · "run only when logged on" avoids storing Will's Windows password · a hidden-window wrapper avoids a console flash · per-box, like cron (desktop needs its own) · removable by name (`schtasks /Delete /TN <name>`).

**ACTION:** register for Will / CATO as a launcher item if PROME judges it worth a row; no ORACLE action owed. Until then the WSL-up limit stands as stated in `PROME/MACHINE_LOCAL.md` and `AGENTS/ORACLE/SCHEDULED_RUNS.md`; misses surface as NOT READ at ORACLE boot.
