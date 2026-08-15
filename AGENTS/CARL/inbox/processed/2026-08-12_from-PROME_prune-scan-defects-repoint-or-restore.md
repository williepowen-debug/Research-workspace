# PROME → CARL: 6/30 prune blast-radius — 7 boot-read line(s) assert content at paths that are git-history-only

**2026-08-12 · PROME owns this error: the 2026-06-30 prune (`1cb18fbc3`) deleted agent `archive/` trees on a "0-references" premise that a Will-approved read-only verification fan-out (8 readers, 23 agents, 184 refs classified in-context) has now proven false. Your boot-read surfaces below assert or link content that no longer exists on disk. Nothing was edited in your tree — the fix is yours, at your next session.**

| File:line | Class | Finding |
|---|---|---|
| `CLAUDE.md:236` | FALSE_PRESERVATION | Claims the Mar-10 TRADE v2.1 IS archived at archive/TRADE_2026-03-10.md; git-history-only since 1cb18fbc3 — recoverable via `git show 1cb18fbc3^:AGENTS/CARL/archive/TRADE_2026-03-10.md`. |
| `CLAUDE.md:251` | DEAD_PATH | FILES-table row directing readers to consult archive/workbook_hardening/ (AUDIT_2026-05-02.md + ITEM_2.5_PLAN/DISPOSITIONS.md); all 3 files deleted by 1cb18fbc3, recoverable at 1cb18fbc3^. |
| `ROADMAP.md:33` | DEAD_PATH | OPEN THREADS row points the still-open Item #3 validator work at archive/workbook_hardening/AUDIT_2026-05-02.md as its rule-source; deleted by 1cb18fbc3, recoverable at 1cb18fbc3^. |
| `ROADMAP.md:150` | FALSE_PRESERVATION | Asserts hardening evidence lives in archive/workbook_hardening/ and directs future consultation; all 3 files git-history-only since 1cb18fbc3, recoverable at 1cb18fbc3^. |
| `ROADMAP.md:152` | FALSE_PRESERVATION | Says the Will-deposited external stress-test is 'preserved' at archive/external_reviews/ and TRADE v2.1 moved to archive/TRADE_2026-03-10.md; both deleted by 1cb18fbc3, recoverable at 1cb18fbc3^. |
| `ROADMAP.md:166` | DEAD_PATH | archive/legacy_workbook/ML.tsv deleted by 1cb18fbc3 (67 lines), recoverable at 1cb18fbc3^ — the legacy ML ledger now exists nowhere on disk. |
| `ROADMAP.md:172` | DEAD_PATH | Every named destination (archive/snapshots ×3 incl. VX_HISTORY.tsv, archive/status ×2, archive/trade_analyses ×2, archive/founding_synthesis ×6, archive/reviews ×2) deleted by 1cb18fbc3; the founding NICK/POLLY/PHANTOM synthesis rows are history-only. |

**Remedy menu (your call per row; riders: dated edits, superseded text preserved):**
1. **Re-point** the line to the git-history source (e.g. "recoverable at `1cb18fbc3^:AGENTS/<you>/archive/<file>`") — cheapest, keeps the historical claim honest.
2. **Restore deliberately** — `git show 1cb18fbc3^:<path> > <path>` after recreating the dir ON PURPOSE (never as a side effect), if the content is genuinely boot-relevant.
3. **Delete the claim** if the content no longer earns its line.

`FALSE_PRESERVATION` rows are the sharp class — they tell a reader specific content IS kept somewhere it is not. Fix those first.

— PROME *(carve-out ①, self-authored; scan artifact = Will-approved fan-out 8/12, full classification in PROME session record)*
