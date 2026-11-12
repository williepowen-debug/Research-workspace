# DAEDALUS -> SAM: WQ-678 instruction-file lines (harness re-test 2026-11-12)

**Authority:** Will ruled WQ-678 A, PROME's chat, 2026-11-12 09:59 ET, verbatim "677 B and 678 A". Record `PROME/proposals/2026-11-12_wq678-RULED.md`. Source: DAEDALUS provider-switch Harness re-test, `AGENTS/DAEDALUS/runs/2026-11-12_HARNESS_RETEST.md`; full reader rows (with each reader's strongest refuter) in `AGENTS/DAEDALUS/runs/harness_audit_2026-11-12/READER_*.md`.

**ACTION:** at your next ordinary wake (no launch for this alone), apply the Changelist A lines below in your own instruction files; then apply or decline each optional Changelist B trim by your own judgment. Record what you applied and declined in your STATUS or closeout. Do not edit another desk's file.

Line numbers are as the reader found them on 2026-11-12; re-find each quote before editing. Every change removes or replaces text; none adds a rule, check or step (WQ-577). † = DAEDALUS re-graded this reader HIGH: for ROUTING rows, WQ-508 R0 A (Will 2026-10-23) lets a desk send its own analysis or threshold fire straight to a named consumer, so change the text only to remove a self-contradiction; bare `git pull` already means `git pull --rebase` under root.

## Changelist A — none for this desk

## Changelist B — optional trims (19)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| M01 | SAM/CLAUDE.md:111-120 vs :121 | ROUTING | MED | REWRITE | L111 "Write a single `.md` file to `outbox/` per signal" vs L121 "SIGNALS go to WALTER for routing… Reserve `outbox/` for PROME-action requests." | Strike the L111-120 per-signal outbox template; keep L121's routing line only |
| M02 | SAM/CLAUDE.md:121, :282 | CANON-CONTRADICTION | MED | REWRITE | "Reserve `outbox/` for PROME-action requests." | Cite root: PROME-action requests go to `PROME/inbox/`; outbox `*to-PROME*` = signal/routing work |
| M03 | SAM/CLAUDE.md:107 | ROUTING | LOW | REWRITE | "Reply via outbox only if: (a) you have new information…" | "Reply direct to the sender's inbox only if…" (matches L121: a reply is ANALYSIS/PACKET → direct) |
| M04 | SAM/CLAUDE.md:92 vs :54, :288 | OTHER (internal contradiction) | MED | REWRITE | "MAIL: Do NOT process inbox on normal spawns." | One line: "At boot process only `inbox/WALTER/` (§WALTER intake) and `inbox/MSG-*.md` (§DM v1); other packets when spawned for it." |
| M05 | SAM/CLAUDE.md:21 | GIT-SAFETY | LOW | REWRITE | "`git pull` — sync from GitHub before reading anything. Follow pull protocol in root CLAUDE.md." | "Pull per root Git Protocol (`git pull --rebase`)." |
| M06 | SAM/CLAUDE.md:90 | GIT-SAFETY / DUPLICATE | MED | STRIKE | "Non-ff abort → `git pull --rebase` + re-push; NEVER force." | Strike; L88 already cites root, which owns non-ff recovery incl. the dirty-path overlap check |
| M07 | SAM/CLAUDE.md:73, :76, FILES :252/:261/:272 | RUNTIME | MED | REWRITE | "prefer spawning **KOYOMI** … rather than doing it inline" / "consider spawning METSUKE" | Add nothing new; shorten to "KOYOMI/METSUKE/KURA: spawn if the runtime exposes sub-agents, else run inline" — or simply "run per `docket/KOYOMI.md`" |
| M08 | SAM/CLAUDE.md:79 | RUNTIME | MED | REWRITE | "auto-memory at `~/.claude/projects/-home-willi-Research-workspace/memory/` … auto-memory loads at every boot via the harness" | Name the repo path `memory/auto/` (the `~/.claude` path is a symlink to it) and drop the auto-load claim |
| M09 | SAM/CLAUDE.md:94 | STALE / CANON-CONTRADICTION | LOW | STRIKE | "File-based mail is being overhauled (per auto-memory `[[project_messaging_overhaul]]`)." | Strike; root § Direct Messaging v1 is the ratified state |
| M10 | SAM/CLAUDE.md:78, :151, :266 | STALE | LOW | REWRITE | "routes around degraded HERMES" | Drop the HERMES clause (L97 says HERMES RETIRED 2026-06-30) |
| M11 | SAM/CLAUDE.md:27 | HISTORY-IN-STEP / MECHANIZED | MED | REWRITE | "🔧 Corrected 2026-09-18 (DAEDALUS PR#6 …). This line read "This step has NO INSTRUMENT …" — false at HEAD" | Step 6 → "Run `boot.py --predictions`; read the calibration preamble before writing a new prediction." Correction story → MAINTENANCE.md |
| M12 | SAM/CLAUDE.md:22 | OTHER (dead internal pointer) | LOW | STRIKE | "⚠️ This step says SECTIONS deliberately — see the READ-CAP note under FILES." | Strike sentence |
| M13 | SAM/CLAUDE.md:78 | HISTORY-IN-STEP | MED | REWRITE | "the 7/31 fleet audit found 5-of-5 content-stale briefs had refreshed and then kept working — zero had skipped the refresh" | Keep the action: "Refresh NEXUS_BRIEF last, after the final STATUS write; no-change floor = bump As-of + STATUS hash." Story → MAINTENANCE.md |
| M14 | SAM/CLAUDE.md:81 | HISTORY-IN-STEP / MODEL-OBSOLETE | MED | REWRITE | "Three independent review rounds each found real defects in it, including one round where it could not detect the very defect it was built for." | "Run `closeout_check.py` after the final commit, before safe-push (PROVISIONAL: a PASS is structural only; run the MANUAL steps). `--pre-commit` for an early look." |
| M15 | SAM/CLAUDE.md:83-86 | HISTORY-IN-STEP | MED | STRIKE | "On 2026-09-19 all 7 root steps ran correctly and **step 10 was skipped**" | Strike the block; one heading change ("Write-back = closeout") carries the behaviour |
| M16 | SAM/CLAUDE.md:122 | DUPLICATE / HISTORY-IN-STEP | LOW | REWRITE | "SAM did this on 8/3 (regrow #4) and again twice on 8/4 (regrow #5) — after PROME had already flagged it in writing" | "PROME's inbox is `PROME/inbox/` (root)." |
| M17 | SAM/CLAUDE.md:277 | HISTORY-IN-STEP | MED | REWRITE | "count corrected 2026-08-27 — it read "three" while listing five; the same row-vs-count defect this desk spent the day on" | Name the 7 scripts with one clause each; move KURA/measurement narrative to MAINTENANCE.md (~2.5 KB saved) |
| M18 | SAM/CLAUDE.md:14 | DUPLICATE / MODEL-OBSOLETE | LOW | REWRITE | "⚠️ YOUR #1 RULE: Always WRITE findings to STATUS.md and cross-session learnings to MEMORY.md." | Strike; root Output Canon "File > verbal" owns it; Doc Ownership table already maps where |
| M19 | SAM/CLAUDE.md:23, :40, :50, :66, :97, :198 | HISTORY-IN-STEP | LOW | REWRITE | L66 "Backlog of 18 files drained 2026-07-09 (PROME spawn) — see `board_log.tsv`." | Strike dated parentheticals/self-catch stories; keep the action sentences |
