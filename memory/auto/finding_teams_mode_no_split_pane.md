---
name: finding-teams-mode-no-split-pane
description: Teams mode does not appear to support split-pane visibility on WSL2 even with teammateMode=tmux + TMUX env present; Agent View is the feature that provides the second pane
metadata: 
  node_type: memory
  type: finding
  originSessionId: a9d22f37-9c4e-4ae2-a981-75a11fa69832
---

Teams-mode named spawns (`Agent(name: "...")`) produce alive, addressable teammates, but do NOT spawn a clickable tmux pane on WSL2 — even when both prerequisites previously suspected are met:

- `TMUX` env var is set (Claude Code launched from inside a tmux session)
- `~/.claude/settings.json` has `"teammateMode": "tmux"`

Validated 2026-05-20 (post-restart from 5/19 PM session). BOND respawn succeeded as an in-process teammate (replies via SendMessage) but no second pane fired.

**The pane visibility Will previously saw was in Agent View, not teams mode.** They are different features. Agent View renders a separate window/pane for the active subagent; teams mode is a coordination/mailbox layer that runs teammates in-process by default with no inherent visualization.

Supersedes the WSL2 caveat in [[finding-teams-mode-domain-agent-spawn]] which assumed `teammateMode: tmux` would fix the missing pane — it does not on this setup.

**Why:** Conflating two adjacent Claude Code features (Agent View vs Agent Teams) led to a chain of false diagnostic hypotheses (env propagation, settings key, restart needed). The two features have overlapping spawn syntax but different visualization layers.

**How to apply:**
- When Will asks for a "second pane to see teammate's work" in teams mode, don't propose tmux/settings fixes — explain the feature distinction and offer in-process visibility (SendMessage replies routed back to lead session) as the working option.
- If true split-pane visibility is required, the workflow is Agent View, not teams. Teams + Agent View together is an untested combination.
- Teams mode strengths: persistent teammates, mailbox semantics, multi-turn via SendMessage. Use it for coordination, not for visibility.
