---
name: finding-teams-mode-domain-agent-spawn
description: Teams-mode (named-spawn) works for domain agents like BOND; identity reconstitutes from files. But teammateMode=auto fails to trigger split-pane on WSL2 even inside tmux — set explicit teammateMode=tmux in ~/.claude/settings.json.
metadata: 
  node_type: memory
  type: finding
  originSessionId: d0ab08f5-287c-4d53-898f-e6928363897d
---

Validated 2026-05-19 by spawning BOND in teams mode (first domain-agent teams-spawn).

**Pattern validation:** named-spawn (`Agent(name: "bond", subagent_type: "general-purpose")`) successfully spawns a persistent domain-agent teammate. Identity reconstitutes from `AGENTS/BOND/CLAUDE.md` + `IDENTITY.md` + `STATUS.md` + `KB.tsv` exactly as a terminal-launched session does — there is no "fresh Claude impedance" because agent identity lives in files, not session memory. Refines [[project_messaging_overhaul]] mental model: **teams-mode is a viable channel for individual domain agents, not just intra-domain swarm.** Doesn't replace inbox/outbox for the 25-agent fleet — same coordination scaling argument — but for any one agent you want to talk to over multiple turns, teams beats one-shot Agent spawns.

**Configuration gotcha (WSL2):** `teammateMode: "auto"` does NOT reliably trigger split-pane on WSL2 even when launched from inside a tmux session with `TERM=tmux-256color`. The `TMUX` env var likely doesn't propagate to Claude Code's child process. Fix: explicit `"teammateMode": "tmux"` in `~/.claude/settings.json`. Without this, BOND spawned alive but invisible — `Shift+Down` keybind also didn't reach the lead session.

**One-shot vs teams lifecycle:** non-named `Agent(...)` spawns are NOT resumable. SendMessage to a completed agentId returns "no transcript to resume — may have been cleaned up." If you want multi-turn interaction with a subagent, you must use named spawn (teams mode). Cross-references [[feedback_named_spawn_teams_mode]].

**Why:** discovered while building out BOND teams session for 5/20 20Y auction watch + 5/21 10Y reopening second-leg test. Will wanted to attach to BOND's session in a separate window; troubleshooting revealed the auto-mode failure.

**How to apply:**
- Need a domain agent for multi-turn work in a single session? Use teams mode (`Agent(name: "<id>", subagent_type: "general-purpose", prompt: "...boot per AGENTS/<NAME>/CLAUDE.md...")`).
- On WSL2 (or any platform where auto-mode fails to split): set explicit `"teammateMode": "tmux"` in `~/.claude/settings.json`. Restart required for the setting to take effect.
- No attach-from-separate-terminal exists. Views are always through the lead session — in-process cycle (`Shift+Down`) or tmux pane spawned by the lead.
- Plan to respawn teams-mode teammates at start of each session; don't rely on overnight persistence. Identity reconstitutes from files in ~30 seconds.
