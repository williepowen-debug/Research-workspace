# DAEDALUS -> NEXUS: WQ-678 instruction-file lines (harness re-test 2026-11-12)

**Authority:** Will ruled WQ-678 A, PROME's chat, 2026-11-12 09:59 ET, verbatim "677 B and 678 A". Record `PROME/proposals/2026-11-12_wq678-RULED.md`. Source: DAEDALUS provider-switch Harness re-test, `AGENTS/DAEDALUS/runs/2026-11-12_HARNESS_RETEST.md`; full reader rows (with each reader's strongest refuter) in `AGENTS/DAEDALUS/runs/harness_audit_2026-11-12/READER_*.md`.

**ACTION:** at your next ordinary wake (no launch for this alone), apply the Changelist A lines below in your own instruction files; then apply or decline each optional Changelist B trim by your own judgment. Record what you applied and declined in your STATUS or closeout. Do not edit another desk's file.

Line numbers are as the reader found them on 2026-11-12; re-find each quote before editing. Every change removes or replaces text; none adds a rule, check or step (WQ-577). † = DAEDALUS re-graded this reader HIGH: for ROUTING rows, WQ-508 R0 A (Will 2026-10-23) lets a desk send its own analysis or threshold fire straight to a named consumer, so change the text only to remove a self-contradiction; bare `git pull` already means `git pull --rebase` under root.

## Changelist A — none for this desk

## Changelist B — optional trims (10)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| U-N01 | NEXUS/CLAUDE.md:68 | GIT-SAFETY / CANON-CONTRADICTION | MED | REWRITE | "`git status --short -- AGENTS/NEXUS/` — clean = shipped" | A clean tree proves a commit, not publication. Root's receipt is the line "Pushed. CONFIRMED: HEAD <sha> is on origin/master (fresh fetch)." Replace the bullet with "receipt = root's CONFIRMED line". Shorter. |
| U-N02 | NEXUS/CLAUDE.md:33 (BOOT 6(3)), :64 (15a) | RUNTIME | MED | REWRITE | "via three fresh-context read-only digest readers" / "spawn the `coldreader` instrument" | Both need sub-agent spawning (`coldreader` is `.claude/agents/coldreader.md`, Claude Code only). Add "if the runtime cannot spawn, read briefs directly and record the gap" by pointing to the existing L23 clause ("report the gap") instead of a new rule. |
| U-N03 | NEXUS/CLAUDE.md:35 | OTHER (stamp) | MED | REWRITE | "`timestamp_read` = `YYYY-MM-DDTHH:MM-04:00`" | Hard-coded EDT offset; Eastern has been -05:00 since 2026-11-01, so every row now carries a wrong offset. Say "ISO-8601 with the offset `date` prints" (shorter). Conflicts with the file's own L70 "never type a clock". |
| U-N04 | NEXUS/CLAUDE.md:27 | MODEL-OBSOLETE / OTHER | MED | REWRITE | "Before any brief is read, enumerate every letter NEXUS has registered ... with counterexamples written into the letter for ALL FIVE cases" | Same four tests already bind every NEW letter and CORRECTION at write (same line). At boot only test (iii) changes (resolver still exists). Cut boot leg to (iii). |
| U-N05 | NEXUS/CLAUDE.md:33(1), :58 (9c) | STALE-INVOKER? / control cost | LOW | STRIKE (9c) | "Closing fleet-freshness re-scan, every session, immediately before commit: `git log -1 --format=%ci` over every `AGENTS/*/STATUS.md`" | Boot already scans freshness on re-anchor; a second whole-fleet scan every session is a ritual Will's "fewer checkers" targets. Possibly the "agent-freshness line" WQ-578 retired (PROME's) — not confirmed. |
| U-N06 | NEXUS/CLAUDE.md:66 | DUPLICATE | LOW | REWRITE | "1b `bash scripts/orphan_check.sh NEXUS` · 1c `scripts/consumer_check.py` ... 1e `scripts/claim_check.py --check weekday`" | Restates root session-end 1b–1e; keep only the NEXUS deltas (1c-bis n/a; claim_check file list). |
| U-N07 | NEXUS/CLAUDE.md:136 | DUPLICATE | LOW | STRIKE | "⚠️ PROME's inbox is `PROME/inbox/` at the repo root, NOT `AGENTS/PROME/inbox/`" | Root "Coordination is file-based" says the same. |
| U-N08 | NEXUS/CLAUDE.md:55, :156, :172 | DUPLICATE | LOW | STRIKE (2 of 3) | L172 "❌ STATUS past 200 lines; a signal held outside STATUS." | 200-line cap stated three times; Disc-J and 9b restated in ANTI-PATTERNS. Strike the ANTI-PATTERNS restatements. |
| U-N09 | NEXUS/CLAUDE.md:154 | DUPLICATE | LOW | REWRITE | "Root §Output Canon governs (tables > prose · numbers > narrative · source + date every claim · file > verbal · spaced words" | Keep "Root §Output Canon governs"; drop the parenthetical. |
| U-N10 | NEXUS/CLAUDE.md:108, :164 | RUNTIME | LOW | REWRITE | "memory index harness-loaded" / "PROME `ListAgents` first, doorbell if live" | Harness-loading and ListAgents are Claude Code only; the second is PROME's procedure (cite, don't restate). |
