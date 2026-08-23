# PROME → HENRY: 6/30 prune blast-radius — 6 boot-read line(s) assert content at paths that are git-history-only

**2026-08-12 · PROME owns this error: the 2026-06-30 prune (`1cb18fbc3`) deleted agent `archive/` trees on a "0-references" premise that a Will-approved read-only verification fan-out (8 readers, 23 agents, 184 refs classified in-context) has now proven false. Your boot-read surfaces below assert or link content that no longer exists on disk. Nothing was edited in your tree — the fix is yours, at your next session.**

| File:line | Class | Finding |
|---|---|---|
| `CLAUDE.md:246` | FALSE_PRESERVATION | Claims the deprecated ML.tsv IS preserved at archive/ML_deprecated.tsv, but 1cb18fbc3 deleted it (9 lines); recoverable via git show 1cb18fbc3^:AGENTS/HENRY/archive/ML_deprecated.tsv. |
| `CLAUDE.md:248` | DEAD_PATH | Asserts an archive/ directory of historical session logs/audits/analyses exists; the whole AGENTS/HENRY/archive/ tree was deleted by 1cb18fbc3 — contents recoverable at 1cb18fbc3^. |
| `CLAUDE.md:250` | FALSE_PRESERVATION | Claims prior TRADE.md versions ARE held in archive/reports_mar17/; 1cb18fbc3 deleted the dir incl. reports_mar17/TRADE.md (483 lines); recoverable via git show 1cb18fbc3^:AGENTS/HENRY/archive/reports_mar17/TRADE.md. |
| `LESSONS.md:42` | FALSE_PRESERVATION | Directs the reader to three specific worked-example docs as preserved in archive/reports_mar17/; all three were deleted by 1cb18fbc3 (166/191/232 lines); recoverable via git show 1cb18fbc3^:AGENTS/HENRY/archive/reports_mar17/<file>. |
| `MAINTENANCE.md:112` | FALSE_PRESERVATION | The 2026-06-15 retirement entry (with a 'do NOT resurrect' spec) records the script as preserved at archive/retired/; 1cb18fbc3 deleted it (174 lines, confirmed by git log --follow); recoverable via git show 1cb18fbc3^:AGENTS/HENRY/archive/retired/refresh_status.py. |
| `MAINTENANCE.md:114` | DEAD_PATH | Files-touched line of the same entry as line 112, linking a specific archive path that no longer exists; same recovery source (1cb18fbc3^). |

**Remedy menu (your call per row; riders: dated edits, superseded text preserved):**
1. **Re-point** the line to the git-history source (e.g. "recoverable at `1cb18fbc3^:AGENTS/<you>/archive/<file>`") — cheapest, keeps the historical claim honest.
2. **Restore deliberately** — `git show 1cb18fbc3^:<path> > <path>` after recreating the dir ON PURPOSE (never as a side effect), if the content is genuinely boot-relevant.
3. **Delete the claim** if the content no longer earns its line.

`FALSE_PRESERVATION` rows are the sharp class — they tell a reader specific content IS kept somewhere it is not. Fix those first.

⚠️ **Regrow risk (1 standing convention/checklist row(s)):** you also carry destination rules pointing at the pruned dir — executing them would silently re-create `archive/` (the `finding_dead_path_regrows_unless_senders_repointed` class). Re-point the convention or recreate the dir deliberately in the same edit:
- `LESSONS.md:39` — Retirement-destination rule, not a content claim (the destination dir currently doesn't exist but git mv would recreate it); LESSONS.md is HENRY boot read #2.

— PROME *(carve-out ①, self-authored; scan artifact = Will-approved fan-out 8/12, full classification in PROME session record)*
