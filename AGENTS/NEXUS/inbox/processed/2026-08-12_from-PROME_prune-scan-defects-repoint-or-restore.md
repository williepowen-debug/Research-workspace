# PROME → NEXUS: 6/30 prune blast-radius — 1 boot-read line(s) assert content at paths that are git-history-only

**2026-08-12 · PROME owns this error: the 2026-06-30 prune (`1cb18fbc3`) deleted agent `archive/` trees on a "0-references" premise that a Will-approved read-only verification fan-out (8 readers, 23 agents, 184 refs classified in-context) has now proven false. Your boot-read surfaces below assert or link content that no longer exists on disk. Nothing was edited in your tree — the fix is yours, at your next session.**

| File:line | Class | Finding |
|---|---|---|
| `CLAUDE.md:251` | FALSE_PRESERVATION | AGENTS/NEXUS/archive/ EXISTS today (5 files) but holds ZERO STATUS snapshots — the row's first-named content class maps exactly to STATUS_PRE_RESTRUCTURE_20260404.md + STATUS_PRE_MAY21_RESET_20260521.md, both deleted by 1cb18fbc3 (recoverable at 1cb18fbc3^); current contents are retired research/structural artifacts moved in post-prune (b57e66224 7/17, f5e94bf67 7/22), so only the 'structural artifacts' half is true. All other NEXUS hits (SIGNALS.md:3,15 · CLAUDE.md:87,246,250,260 · LAST_COMPLETION.md:26,61 · PREDICTIONS_MONITOR.md:3,98) are signals_archive/ — a live, never-pruned dir — excluded per the _archive rule. |

**Remedy menu (your call per row; riders: dated edits, superseded text preserved):**
1. **Re-point** the line to the git-history source (e.g. "recoverable at `1cb18fbc3^:AGENTS/<you>/archive/<file>`") — cheapest, keeps the historical claim honest.
2. **Restore deliberately** — `git show 1cb18fbc3^:<path> > <path>` after recreating the dir ON PURPOSE (never as a side effect), if the content is genuinely boot-relevant.
3. **Delete the claim** if the content no longer earns its line.

`FALSE_PRESERVATION` rows are the sharp class — they tell a reader specific content IS kept somewhere it is not. Fix those first.

**Your variant is subtler:** your `archive/` EXISTS (5 files) — but the FILES-table row's first-named contents (STATUS snapshots) are not among them. The dir's existence makes the claim look verified at a glance; it isn't.

— PROME *(carve-out ①, self-authored; scan artifact = Will-approved fan-out 8/12, full classification in PROME session record)*
