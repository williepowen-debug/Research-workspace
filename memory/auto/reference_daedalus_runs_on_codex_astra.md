---
name: reference_daedalus_runs_on_codex_astra
description: DAEDALUS runs on Codex Astra, not Claude, so SendMessage may not reach it; use inbox packets
metadata:
  type: reference
symptoms: DAEDALUS missing from ListAgents; DAEDALUS commits appear with no listed session; message to DAEDALUS not delivered
---

DAEDALUS is spawned on Codex Astra, not Claude (Will 2026-11-07 10:28 ET: "It is spawned as codex Astra as opposed to claude so it might be more difficult for you to message directly"). It will not show in ListAgents, and fresh DAEDALUS commits can appear with no listed peer.

**How to apply:** reach it by a committed packet in `AGENTS/DAEDALUS/inbox/`. An absent ListAgents row is not evidence the desk is down; run the Desk-spawn preflight with a host check that covers Codex before any launch. Related: [[feedback_launch_desks_through_agent_launcher]].
