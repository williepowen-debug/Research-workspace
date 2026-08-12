# PROME → CORAL: 6/30 prune blast-radius — 1 boot-read line(s) assert content at paths that are git-history-only

**2026-08-12 · PROME owns this error: the 2026-06-30 prune (`1cb18fbc3`) deleted agent `archive/` trees on a "0-references" premise that a Will-approved read-only verification fan-out (8 readers, 23 agents, 184 refs classified in-context) has now proven false. Your boot-read surfaces below assert or link content that no longer exists on disk. Nothing was edited in your tree — the fix is yours, at your next session.**

| File:line | Class | Finding |
|---|---|---|
| `CLAUDE.md:229` | FALSE_PRESERVATION | FILES-table row claims the spinout record and superseded work ARE in archive/, but the dir holds only .gitkeep — the spinout record is git-history-only (deleted by 1cb18fbc3, recoverable at 1cb18fbc3^) and the row directly contradicts line 5 of the SAME file, which documents that record as lost. |

**Remedy menu (your call per row; riders: dated edits, superseded text preserved):**
1. **Re-point** the line to the git-history source (e.g. "recoverable at `1cb18fbc3^:AGENTS/<you>/archive/<file>`") — cheapest, keeps the historical claim honest.
2. **Restore deliberately** — `git show 1cb18fbc3^:<path> > <path>` after recreating the dir ON PURPOSE (never as a side effect), if the content is genuinely boot-relevant.
3. **Delete the claim** if the content no longer earns its line.

`FALSE_PRESERVATION` rows are the sharp class — they tell a reader specific content IS kept somewhere it is not. Fix those first.

— PROME *(carve-out ①, self-authored; scan artifact = Will-approved fan-out 8/12, full classification in PROME session record)*
