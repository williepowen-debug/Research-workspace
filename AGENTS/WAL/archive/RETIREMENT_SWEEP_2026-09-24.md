# WAL — retirement sweep record, 2026-09-24 (session #7)

**Authority:** PROME's 8/23 disposition item ② (the 8-file candidate set, "run file-by-file"; carried as MEMORY N-6 since) + Will in-session 2026-09-24 ("lets do housekeeping items"). **Rule:** root `CLAUDE.md` § Data Hygiene retirement, as amended 2026-08-21: >60 days old AND not boot-read AND not referenced by a live doc → `git mv` to `archive/`; ① a pending-event artifact is never eligible; ② index/inventory refs don't count. **Precedent applied:** `archive/RETIREMENT_SWEEP_2026-08-23.md` — age by CONTENT date (git shows every file created 2026-07-25, which is the promotion `git mv`, not authorship); dated records (CHANGELOG entries, MEMORY/MEMORY_ARCHIVE, outbox packets, archives, other desks' logs) are records, not live docs; a `THESIS.md` file-table row IS a live-doc reference (the EARNINGS_PREP hold).

**Run FILE-BY-FILE. 7 archived, 1 HELD.**

| File | Content date (>60d?) | Boot-read? | Live-doc reference? (checked: THESIS, SCENARIOS, STATUS, WEAKNESSES, CLAUDE.md, NEXUS_BRIEF, POSITIONS, LEADERSHIP, scripts/*, KB Source/Notes, other desks' STATUS/THESIS/CLAUDE, PROME DOCKET/GATES) | Pending-event artifact? | Disposition |
|---|---|---|---|---|---|
| `AUDIT_MAR25.md` | 2026-03-25/26 (~182d) ✅ | ❌ | ❌ — INDEX (index-ref), CHANGELOG / MEMORY / outbox 8/23 / OZK INDEX (records or index) | ❌ | 🗄️ ARCHIVED |
| `EXTERNAL_PROMPTS.md` | 2026-03-25 ✅ | ❌ | ❌ — INDEX, MEMORY, AUDIT_MAR25 (itself a March record) | ❌ | 🗄️ ARCHIVED |
| `PRIOR_RESEARCH_EXTRACTS.md` | 2026-02-23 ✅ | ❌ | ❌ — same set | ❌ | 🗄️ ARCHIVED |
| `V21_RESPONSE_TO_RED_CHG_025.md` | 2026-05-11 (~136d) ✅ | ❌ | ❌ — INDEX, CHANGELOG, the two INVESTOR_DAY files (co-archived) | ❌ — CHG-RED-025 RESOLVED-CONVERGED 2026-05-13 (`AGENTS/RED/workbook/ML.tsv` ML-RED-059) | 🗄️ ARCHIVED |
| `INVESTOR_DAY_FINDINGS_2026-05-12.md` | 2026-05-15 (~132d) ✅ | ❌ | ❌ — INDEX, STATUS_ARCHIVE (cold), CHANGELOG, RED thesis CHANGELOG + REGINALD BOARD_LOG (records) | ❌ | 🗄️ ARCHIVED |
| `INVESTOR_DAY_PREP_2026-05-12.md` | 2026-05-11 ✅ | ❌ | ❌ — STATUS_ARCHIVE, INVESTOR_DAY_FINDINGS (co-archived) | ❌ | 🗄️ ARCHIVED |
| `TECHNICALS_20260401.md` | 2026-04-01 (~176d) ✅ | ❌ | ❌ — INDEX, MEMORY, outbox (records) | ❌ | 🗄️ ARCHIVED |
| `Q1_2026_ANALYSIS.md` | Apr-22 content ✅ | ❌ | ✅ **YES — `THESIS.md:406` file table** (*"Round 1 8-K mining (Apr 22) — TL;DR, fraud detail…"*) + `SCENARIOS.md:536` footer | ❌ | ⛔ **HELD — fails the live-doc leg** (same shape as the 8/23 EARNINGS_PREP hold). *The OZK `STATUS/THESIS/CLAUDE` hits are OZK's OWN `Q1_2026_ANALYSIS.md`, not this file.* |

**Mechanics:** `git mv` (all seven showed `R` in `git status`); a dated ARCHIVED banner prepended to each, content otherwise unchanged; the banner tells a reader that bare file names now resolve one level up (`../`) rather than rewriting pointers inside historical content. No script hard-codes any of the seven paths (grepped `AGENTS/WAL/scripts/` + root `scripts/`). `INDEX.md` deep-dive line re-pathed. Drift check re-run after (see commit).

*To un-hold `Q1_2026_ANALYSIS.md` later: fold whatever THESIS still travels it for into THESIS/KB, drop the file-table row, and it becomes eligible.*
