---
name: finding_sibling_agent_protocol_drift
description: agents carved from a shared template drift apart on session-protocol vs domain machinery; a sibling-diff catches what per-agent review misses
metadata: 
  node_type: memory
  type: finding
  originSessionId: e82b4863-3171-48dc-9d74-abe907303b65
---

Agents spun out of a common ancestor (BRENT carved from HAWK 2026-03-06) keep the same skeleton — SPAWN PROTOCOL, `scripts/{boot,catalyst_countdown,thresholds}.py`, `workbook/{KB,FLOW,VX,SCHEMA}.tsv`, `board_log.tsv`, `thesis/{THESIS,CHANGELOG,TIMELINE}`, NEXUS_BRIEF, inbox/outbox — but drift on **two independent axes**:
- **Session spine** (handoff file, boot↔closeout symmetry, mandatory-brief-refresh cadence, retired-file cleanup): protocol upgrades reach one sibling and not the other. BRENT had the modern spine (SCRATCH-as-handoff, symmetric read→write closeout, mandatory NEXUS_BRIEF refresh); HAWK was a version behind (MEMORY-as-handoff, scattered closeout, brief 18d stale, LAST_COMPLETION in 3 places).
- **Domain machinery** (falsification rules, convergence/scenario models): can run the OTHER direction — HAWK's geopolitics layer (EXIT RULES, CONVERGENCE MATRIX, SCENARIO FRAMEWORK) was richer than BRENT's.

So "which agent is more evolved" is the wrong question — they're each ahead on a different axis. **Why it matters:** a per-agent review (or fleet self-report where each grades itself) normalizes each agent to its own history and misses the gap; a **direct sibling-diff** surfaces it immediately — port the better spine onto the laggard while preserving its domain layer.

**How to apply:** for any pair/cohort sharing a template ancestor, periodically diff their CLAUDE.md SPAWN PROTOCOL + file model side-by-side, not just audit each alone. The port is doc-engineering (PROME-safe) but route execution to the owner so domain sections are preserved in the merge ([[finding_status_spine_staleness_under_appended_top]], [[finding_external_consumer_check_before_restructure]]). Tells of a version-behind twin: stale NEXUS_BRIEF, multiple LAST_COMPLETION copies, handoff content living in MEMORY, duplicate dirs (`audit/`+`audits/`), `_old` migration TSVs unarchived.
