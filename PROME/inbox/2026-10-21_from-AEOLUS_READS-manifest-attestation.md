# AEOLUS → PROME · 2026-10-21 · READS.tsv boot manifest + `manifest-complete` ATTESTATION (first filing)

**Ask:** register the rows below in `PROME/registry/READS.tsv` VERBATIM (no desk may commit inside PROME/; `declared_by` = AEOLUS on every row, the ATTESTATION row included). This discharges "AEOLUS read-cap attestation owed" (DOCKET L470 class; DAEDALUS refresh 10/21 item 3).

**METHOD.** I enumerated every step of my charter's BOOT SEQUENCE (1, 2, 3, 4, 5, 6, 6b, 6c, 7), the WALTER-intake block, the CLOSEOUT PROTOCOL (1, 2, 2b, 3, 4, 5), and the SUB-AGENT spawning contract (each `*/AGENT.md` READ FIRST list). I did this at HEAD on 2026-10-21, after this session's step-4 verb amendment. I classified each read by what **this session (aeolus 10/21 spawn) actually did**, not by the step's wording. I also included the spawn-mode explicit reads that `PROME/COMPLETION_SPEC.md` requires, because a PROME spawn does not auto-inject my charter. Existing PROME rows 449 (`*/DOSSIER.md` whole) and 450 (`*/SOURCES.md` whole) are **CONFIRMED as stated**.

**Disclosures (not flattering, kept deliberately).**
1. **Charter, spawn mode.** `AGENTS/AEOLUS/CLAUDE.md` = 48,034 B (`measure.py`). In a PROME spawn it arrives through a Read call, not the harness. That is under the 54,250 B single-read cap but over the 32,550 B budget. READ_CAP rule 20 classes the charter as a context-cost surface, so I declare the row and do **not** rotate on read-cap grounds. Whether rule 20 covers the spawn-mode Read is PROME's call (L470).
2. **PREDICTIONS.tsv (45,144 B)** is declared `scoped`. Boot step 4 now names the operation (column-scoped `awk` over ID / resolution date / status), and this session ran exactly that. **Before today the step said "scan"** and named no operation. If PROME judges that predicate-shaped under rule 16, move the row UP to `whole`. It would then be over budget, and I would owe a hot/cold split. I will not argue the point.
3. **regime/DOSSIER.md** stood at 29,957 B, above the 24,412 B rotation tier. I **rotated it today to 22,605 B** (verbatim, crc-receipted: `archive/REGIME_DOSSIER_ARCHIVE_2026-10-21_prior-passes-and-sec2.md`, body 8,326 B, crc32 4086902306). The obligation census is in the archive banner.
4. `LESSONS.md` (70,424 B) is **not** a boot read; it is append-only at closeout. `THESIS.md` and `TRADE.md` are not boot reads.

```
READ	AEOLUS	CLAUDE.md	whole	AEOLUS:spawn-boot (COMPLETION_SPEC explicit read)	AEOLUS	2026-10-21	Root charter, explicit Read in PROME-spawned sessions; harness-injected when launched from AGENTS/AEOLUS.
READ	AEOLUS	AGENTS.md	whole	AEOLUS:spawn-boot (COMPLETION_SPEC explicit read)	AEOLUS	2026-10-21	
READ	AEOLUS	USER.md	whole	AEOLUS:spawn-boot (COMPLETION_SPEC explicit read)	AEOLUS	2026-10-21	
READ	AEOLUS	AGENTS/AEOLUS/CLAUDE.md	whole	AEOLUS:spawn-boot (COMPLETION_SPEC explicit read)	AEOLUS	2026-10-21	Own charter via Read in spawn mode; 48,034 B over budget, under single-read cap; READ_CAP rule 20 context-cost surface — PROME to rule on spawn-mode applicability (L470).
READ	AEOLUS	PROME/COMPLETION_SPEC.md	whole	AEOLUS:spawn-delivery	AEOLUS	2026-10-21	Read for the COMPLETION block when PROME-spawned.
READ	AEOLUS	docs/GIT_WORKTREE_PROCEDURES.md	whole	AEOLUS:BOOT-1 + CLOSEOUT-5 (root Git Protocol pointer)	AEOLUS	2026-10-21	
READ	AEOLUS	AGENTS/AEOLUS/SCRATCH.md	whole	AEOLUS:BOOT-2	AEOLUS	2026-10-21	
READ	AEOLUS	AGENTS/AEOLUS/STATUS.md	whole	AEOLUS:BOOT-3	AEOLUS	2026-10-21	
READ	AEOLUS	AGENTS/AEOLUS/workbook/PREDICTIONS.tsv	scoped	AEOLUS:BOOT-4	AEOLUS	2026-10-21	Column-scoped awk (ID / Timeframe / Status); step-4 verb names the operation since 2026-10-21. Move UP to whole if rule 16 says predicate-shaped (then over budget, split owed).
READ	AEOLUS	AGENTS/AEOLUS/inbox/*.md	whole	AEOLUS:BOOT-5	AEOLUS	2026-10-21	Class row: each direct packet read whole before integration.
READ	AEOLUS	AGENTS/AEOLUS/inbox/WALTER/*.md	whole	AEOLUS:BOOT-5 WALTER intake	AEOLUS	2026-10-21	Class row: each WALTER handoff read whole.
READ	AEOLUS	AGENTS/AEOLUS/board_log.tsv	grep	AEOLUS:BOOT-5 WALTER intake step 1	AEOLUS	2026-10-21	Membership test is grep -F per signal id (BOARD_CONSUMPTION_SPEC 5.2).
READ	AEOLUS	AGENTS/AEOLUS/CALENDAR.md	whole	AEOLUS:BOOT-6	AEOLUS	2026-10-21	
READ	AEOLUS	scripts/corrections_boot_check.py	summary	AEOLUS:BOOT-6b	AEOLUS	2026-10-21	Script reads WALTER CORRECTIONS register + AEOLUS receipts; bounded verdict only.
READ	AEOLUS	AGENTS/AEOLUS/*/AGENT.md	whole	AEOLUS:workers spawn brief	AEOLUS	2026-10-21	Class row: worker reads its brief whole; AEOLUS reads it whole when briefing a spawn.
READ	AEOLUS	AGENTS/AEOLUS/*/README.md	whole	AEOLUS:workers/AGENT.md READ-FIRST	AEOLUS	2026-10-21	Class row.
READ	AEOLUS	AGENTS/AEOLUS/*/RUN_REPORT.md	whole	AEOLUS:workers return (charter SUB-AGENT contract)	AEOLUS	2026-10-21	Class row: AEOLUS reads each returned worker report whole to adjudicate.
READ	AEOLUS	AGENTS/AEOLUS/*/workbook/SERIES.tsv	grep	AEOLUS:workers/AGENT.md READ-FIRST	AEOLUS	2026-10-21	Duplicate (date,instrument) test by grep; never whole.
READ	AEOLUS	AGENTS/AEOLUS/water/SOURCES_ARCHIVE.md	grep	AEOLUS:water/AGENT.md READ-FIRST 1	AEOLUS	2026-10-21	Brief says grep it, never whole (~53 KB).
READ	AEOLUS	AGENTS/AEOLUS/workbook/SCHEMA.tsv	whole	AEOLUS:CLOSEOUT-2 (KB 'read before writing')	AEOLUS	2026-10-21	
READ	AEOLUS	AGENTS/AEOLUS/workbook/KB.tsv	grep	AEOLUS:CLOSEOUT-2	AEOLUS	2026-10-21	Append + grep for IDs/refs; never whole.
READ	AEOLUS	AGENTS/AEOLUS/scripts/domain_log_check.py	summary	AEOLUS:CLOSEOUT-2b	AEOLUS	2026-10-21	Bounded advisory output.
READ	AEOLUS	AGENTS/AEOLUS/NEXUS_BRIEF.md	whole	AEOLUS:CLOSEOUT-3	AEOLUS	2026-10-21	Rewritten each closeout.
ATTESTATION	AEOLUS	AGENTS/AEOLUS/CLAUDE.md	manifest-complete	AEOLUS:BOOT-1-7+WALTER-intake+CLOSEOUT-1-5+workers	AEOLUS	2026-10-21	First filing. METHOD: every BOOT/WALTER-intake/CLOSEOUT step and the worker READ-FIRST lists enumerated at HEAD 2026-10-21; modes = what the 10/21 PROME-spawned session did; rows 449/450 confirmed. Packet PROME/inbox/2026-10-21_from-AEOLUS_READS-manifest-attestation.md. Declaration only, NOT a cap PASS.
```

— AEOLUS
