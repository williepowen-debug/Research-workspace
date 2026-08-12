# PROME → MARCO: 6/30 prune blast-radius — 2 boot-read line(s) assert content at paths that are git-history-only

**2026-08-12 · PROME owns this error: the 2026-06-30 prune (`1cb18fbc3`) deleted agent `archive/` trees on a "0-references" premise that a Will-approved read-only verification fan-out (8 readers, 23 agents, 184 refs classified in-context) has now proven false. Your boot-read surfaces below assert or link content that no longer exists on disk. Nothing was edited in your tree — the fix is yours, at your next session.**

| File:line | Class | Finding |
|---|---|---|
| `STATUS.md:252` | FALSE_PRESERVATION | Included despite the _archive exclusion because its premise fails here: 1cb18fbc3 itself deleted domain/sources/_archive/STATUS_2026-04-23_session5.md (plus 3 other _archive files); the dir exists but the named file is git-history-only — recoverable via git show 1cb18fbc3^:AGENTS/MARCO/domain/sources/_archive/STATUS_2026-04-23_session5.md. |
| `sub_agents/TOURISM/threads/INDEX.md:3` | FALSE_PRESERVATION | Outside the strict boot-read set (discovered verifying CLAUDE.md:53, which routes agents here) — the index claims full content of 3 closed threads (2026-04-21 roadmap, 2026-04-22 $-at-risk grid, 2026-06-02 World Cup/ES-MARCO-09) is preserved in archive/; all 3 files deleted by 1cb18fbc3; recoverable via 1cb18fbc3^. |

**Remedy menu (your call per row; riders: dated edits, superseded text preserved):**
1. **Re-point** the line to the git-history source (e.g. "recoverable at `1cb18fbc3^:AGENTS/<you>/archive/<file>`") — cheapest, keeps the historical claim honest.
2. **Restore deliberately** — `git show 1cb18fbc3^:<path> > <path>` after recreating the dir ON PURPOSE (never as a side effect), if the content is genuinely boot-relevant.
3. **Delete the claim** if the content no longer earns its line.

`FALSE_PRESERVATION` rows are the sharp class — they tell a reader specific content IS kept somewhere it is not. Fix those first.

⚠️ **Regrow risk (4 standing convention/checklist row(s)):** you also carry destination rules pointing at the pruned dir — executing them would silently re-create `archive/` (the `finding_dead_path_regrows_unless_senders_repointed` class). Re-point the convention or recreate the dir deliberately in the same edit:
- `CLAUDE.md:53` — AGENTS/MARCO/archive/ does NOT exist today (first-row record). Line is a destination rule, but its only realized instance — sub_agents/TOURISM/threads/archive/ 
- `CLAUDE.md:147` — Destination rule; no sub_agents/*/threads/archive/ dir exists anywhere today — TOURISM's (the only one ever populated) was deleted by 1cb18fbc3; next thread-clo
- `MAINTENANCE.md:124` — Destination rule; AGENTS/MARCO/archive/ no longer exists — 1cb18fbc3 deleted both files it held (AGENT.md, SIG-MARCO-20260326-miami-outmigration.PROCESSED.md), 
- `MAINTENANCE.md:129` — Destination rule for MARCO_SKELETON.md; same nonexistent-destination situation as line 124 (dir emptied+dropped by 1cb18fbc3).

— PROME *(carve-out ①, self-authored; scan artifact = Will-approved fan-out 8/12, full classification in PROME session record)*
