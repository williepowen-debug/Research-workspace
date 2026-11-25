---
name: reference_in_process_desk_agents_survive_clear
description: A desk launched as an in-process agent (Agent tool) keeps running through the parent's /clear, reports to the new context, and resumes by message after its closeout; several fit inside the PROME process
metadata:
  type: reference
symptoms: checkpoint for restart with a desk in flight; restart NOT READY; will the subagent survive /clear; how many desks fit on the laptop; index.lock exists another git process
---

Observed on the laptop, Claude Code, 2026-11-24 (n=1 for each line):

- **Survives `/clear`.** REGINALD was launched as an in-process desk agent about 22:25 ET; PROME ran `/clear` at the checkpoint; ListAgents in the new context at 22:27 ET still showed the agent running, and its completion message and task notification arrived in the new context about 22:40 ET. The NOW page had marked the restart NOT READY because survival was UNKNOWN. It is not known whether an agent survives the PROCESS exiting (a closed terminal, a crash): treat that as lost, as on 11/23 when a reader died in the outage.
- **Resumes by message after its own closeout.** TERRY closed out at 22:55 ET and was resumed by SendMessage at 23:38 ET in the same PROME session; it did the follow-up and closed out again. See [[finding_closed_out_teammate_does_not_resume_on_reping]] for the cases where a re-ping was silence (a separate window, a later session).
- **Capacity.** In-process desk agents run inside the PROME process, not as 300 to 500 MB windows. Four ran at once (LIQUID, HENRY, CORAL, AEOLUS) and then six in flight across the hour, with `free -m` available falling from about 3,750 MB to about 3,430 MB on a 5.9 GB WSL cap. Still measure before each launch.
- **Shared index.** Several desks committing in one working tree collide on `.git/index.lock` for a second; the failed command changes nothing, so check state and re-run it once. A desk can also `git mv` another desk's uncommitted packet while consuming it (CORAL and AEOLUS, 11/24); the brief should say packets are committed before the recipient is told.

**How to apply:** at a restart checkpoint an in-process desk is a surviving owner under `PROME/CLOSEOUT.md` § Restart checkpoint, so the restart need not wait for it; on pickup, ListAgents first, then wait for its message.
