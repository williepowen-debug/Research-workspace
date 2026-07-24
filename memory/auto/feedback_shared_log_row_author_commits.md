---
name: feedback_shared_log_row_author_commits
description: "Will ratified (2026-07-24, to LABOR) that the agent who authors a row in the shared AGENTS/SIGNALS.md commits that row itself rather than flagging it to PROME — uncommitted shared-file edits orphan by design."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 93ff7242-52ba-4bb8-9d56-def621bbbcae
  modified: 2026-07-24T20:56:59.647Z
---

When you append a row you authored to the shared cross-agent log `AGENTS/SIGNALS.md`, **commit it yourself** in the same session — path-scoped (`git commit AGENTS/SIGNALS.md -m "..."`). Do not append-then-flag-to-PROME.

**Why:** an uncommitted shared-file edit **orphans by construction**. `orphan_check.sh` shows it to every other agent as `[not yours] — do not sweep`, which is correct behavior and exactly why nobody picks it up. The row then sits indefinitely and the cross-agent visibility layer (which NEXUS scans) silently loses the entry. Same failure the 2026-07-23 inbox-packet carve-out was created to fix (~12% of packets orphaned pre-detector) — this is the narrow extension of it to shared logs.

**How to apply:** append the row → commit `AGENTS/SIGNALS.md` path-scoped, same session, recipient named in the subject. **Scope is narrow and does not widen on its own:** it covers *rows you authored in that file*. It does **not** cover editing rows other agents wrote, restructuring the file, or any other shared/root doc (`HEARTBEAT.md`, root `CLAUDE.md`, `FORGE/`) — those still route to PROME/Will per root CLAUDE.md.

**Provenance caveat worth respecting:** Will gave this ruling to **LABOR** on 2026-07-24. Root `CLAUDE.md` still carries the older blanket "flag it to Prome — don't commit it yourself" for shared files, so there is a **documented divergence** until PROME/Will generalizes it. If you are not LABOR, treat this as strong precedent and a reason to *ask*, not as standing fleet-wide authority to edit root docs on your own. Flagged to PROME in `AGENTS/LABOR/outbox/2026-07-24_to-PROME_signals-md-row-needs-commit.md`.

Related: [[feedback_agent_git_isolation]] · [[finding_pathspec_commit_race_safety]] · [[feedback_cross_agent_inbox_writes]] · [[finding_documented_divergence_as_discipline]]
