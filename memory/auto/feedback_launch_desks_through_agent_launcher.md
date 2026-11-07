---
name: feedback_launch_desks_through_agent_launcher
description: Will (2026-11-05) confirmed PROME can start a desk in its own window through his agent launcher (scripts/agents.py); first use worked for AEOLUS and RED on Opus and he asked to remember it
metadata:
  type: feedback
symptoms: "can PROME use the agent launcher", "open this desk in its own window", "spawn AEOLUS as Opus", "launch a desk Will can talk to"
---

Will, 2026-11-05 09:53 ET in the PROME window, verbatim: *"Okay so can you use the app/agent launcher to spawn AEOLUS and RED as OPUS?"*; after both came up, 09:55 ET: *"Hey the spawn worked. Good job! We shold remember that for future sessions"*.

**The method:** from the repo root, `python3 scripts/agents.py <desk> --opus --new --task "<task>"`. Add `--dry-run` to inspect the command and start nothing. The graphical launcher is Will's to click; this command is the engine under it.

**Why it is useful:** an `Agent` subagent lives inside PROME's session and dies with it. A launcher desk gets its own Windows Terminal window, Will can type into it, it outlives PROME, and it appears in `ListAgents` by name, so `SendMessage` reaches it.

**How to apply:**
- Same-minute Desk-spawn preflight first (`ListAgents` plus `ps`), the launch grants and caps, an `ORCH_LOG.tsv` `1-SPAWN` row, and the closeout ask. The launcher changes the door, not the rules. A desk PROME starts is PROME's to close out.
- rc=0 and "CLI process acknowledged" do not prove the boot. Confirm with `ps` and `ListAgents`.
- The launcher's lock sees only launcher starts, so it is not a preflight. It misses hand-opened sessions and Codex tasks that outlive their windows.
- Each launch opens a window on Will's screen, so use it for desks he may want to talk to or that must outlive PROME; a bounded read stays an `Agent` subagent.
- Task text stays one argument. Put the row keys, the limits and the delivery instruction in it.
- ⚠️ **Scope of this grant, as PROME reads it:** Will's word covered these two launches and remembering the method. It does not establish launching without his word beyond PROME's existing tiers, and it authorizes no unattended launch (WQ-388 RULED DECLINE 2026-10-15: WALTER may not self-schedule an unattended sweep; sessions start only when Will or PROME launches them).

Evidence: AEOLUS and RED launched 09:53 ET, `ps` and `ListAgents` confirmed both, ORCH_LOG commit be576372f. Related: [[feedback_close_finished_subagent_panes]] · [[feedback_doorbell_live_desks_directly_never_paste_blocks]].
