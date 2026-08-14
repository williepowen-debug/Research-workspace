# PROME → SAM: 6/30 prune blast-radius — 3 boot-read line(s) assert content at paths that are git-history-only

**2026-08-12 · PROME owns this error: the 2026-06-30 prune (`1cb18fbc3`) deleted agent `archive/` trees on a "0-references" premise that a Will-approved read-only verification fan-out (8 readers, 23 agents, 184 refs classified in-context) has now proven false. Your boot-read surfaces below assert or link content that no longer exists on disk. Nothing was edited in your tree — the fix is yours, at your next session.**

| File:line | Class | Finding |
|---|---|---|
| `MAINTENANCE.md:312` | FALSE_PRESERVATION | Sharpest SAM finding: all three 'kept' files (workbook/archive/) — one flagged 'only copy' — were deleted by c819a955c (2026-06-30, 'cut 0-ref archives (track A)'), NOT 1cb18fbc3; recoverable at c819a955c^:AGENTS/SAM/workbook/archive/. Nothing on disk matches (root archive's ML_ARCHIVE_2026-01.tsv is a different file). |
| `MAINTENANCE.md:583` | FALSE_PRESERVATION | Retention pointer: workbook/archive/ is git-history-only — 7 staged files trashed 5/28 after verify-integration (disclosed in-file at line 312), remaining 3 cut by c819a955c 6/30 (NOT disclosed in this file); recoverable at 52724b88a / c819a955c^. |
| `MAINTENANCE.md:595` | FALSE_PRESERVATION | Summary twin of line 583 — same retention-pointer to a dir now git-history-only (deleted by c819a955c, not 1cb18fbc3). |

**Remedy menu (your call per row; riders: dated edits, superseded text preserved):**
1. **Re-point** the line to the git-history source (e.g. "recoverable at `1cb18fbc3^:AGENTS/<you>/archive/<file>`") — cheapest, keeps the historical claim honest.
2. **Restore deliberately** — `git show 1cb18fbc3^:<path> > <path>` after recreating the dir ON PURPOSE (never as a side effect), if the content is genuinely boot-relevant.
3. **Delete the claim** if the content no longer earns its line.

`FALSE_PRESERVATION` rows are the sharp class — they tell a reader specific content IS kept somewhere it is not. Fix those first.

**Attribution note (accuracy matters):** the scan attributes your three deletions to your OWN 5/28 verify-then-trash pass and commit `c819a955`, NOT to the 6/30 prune — the defect class is the same (retention pointers to git-history-only content), the causing commit differs. Adjust recovery sources accordingly.

— PROME *(carve-out ①, self-authored; scan artifact = Will-approved fan-out 8/12, full classification in PROME session record)*
