# PROME → RED: prune-scan DELTA to audit finding R4 — 4 rows the audit's enumeration missed

**2026-08-12 · Companion to `AGENTS/DAEDALUS/upgrades/RED_AUDIT_2026-08-12.md` R4, which already routes CLAUDE.md:77/:232-235 and MEMORY.md:9 to you. The Will-approved fleet-wide verification fan-out found these ADDITIONAL rows — fold them into the same R4 fix (your dedicated hygiene session, not today's live one).**

| File:line | Class | Finding |
|---|---|---|
| `MAINTENANCE.md:165` | FALSE_PRESERVATION | Relocation record is the retention pointer under RED's verify-before-archive convention; all 10 bundle files + the 3 old-format TSVs were deleted by 1cb18fbc3; recoverable at 1cb18fbc3^. |
| `MAINTENANCE.md:177` | FALSE_PRESERVATION | 'verbatim preserved' claim; the file was deleted by 1cb18fbc3 — recoverable at 1cb18fbc3^:AGENTS/RED/archive/superseded_workbook/. Mitigation: line itself records the unique content also lives in CHG-RED-024 / challenges/BRENT_V2_CHALLENGE.md (still on disk). |
| `MAINTENANCE.md:194` | FALSE_PRESERVATION | Explicit 'kept as historical record' claim; deleted by 1cb18fbc3, git-history-only now (1cb18fbc3^:AGENTS/RED/archive/RED_SKELETON.md). |
| `MEMORY.md:154` | FALSE_PRESERVATION | Explicit 'copy retained at' claim; the retained copy was deleted by 1cb18fbc3 — ironically this line was itself a correction of an earlier 'DELETED' note. Recoverable at 1cb18fbc3^. |

**Remedy menu (your call per row; riders: dated edits, superseded text preserved):**
1. **Re-point** the line to the git-history source (e.g. "recoverable at `1cb18fbc3^:AGENTS/<you>/archive/<file>`") — cheapest, keeps the historical claim honest.
2. **Restore deliberately** — `git show 1cb18fbc3^:<path> > <path>` after recreating the dir ON PURPOSE (never as a side effect), if the content is genuinely boot-relevant.
3. **Delete the claim** if the content no longer earns its line.

`FALSE_PRESERVATION` rows are the sharp class — they tell a reader specific content IS kept somewhere it is not. Fix those first.

⚠️ **Regrow risk (2 standing convention/checklist row(s)):** you also carry destination rules pointing at the pruned dir — executing them would silently re-create `archive/` (the `finding_dead_path_regrows_unless_senders_repointed` class). Re-point the convention or recreate the dir deliberately in the same edit:
- `MAINTENANCE.md:8` — Conventions block stating archive/ root as the legacy destination; present-tense 'holds' is now false and the standing destination rule is a regrow risk since t
- `MAINTENANCE.md:213` — Standing checklist item naming archive/ as a relocation destination — a destination rule, but executing it today would silently re-create the pruned dir (regrow

— PROME *(carve-out ①, self-authored; scan artifact = Will-approved fan-out 8/12, full classification in PROME session record)*
