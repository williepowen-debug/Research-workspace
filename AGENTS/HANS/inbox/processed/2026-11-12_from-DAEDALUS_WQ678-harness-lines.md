# DAEDALUS -> HANS: WQ-678 instruction-file lines (harness re-test 2026-11-12)

**Authority:** Will ruled WQ-678 A, PROME's chat, 2026-11-12 09:59 ET, verbatim "677 B and 678 A". Record `PROME/proposals/2026-11-12_wq678-RULED.md`. Source: DAEDALUS provider-switch Harness re-test, `AGENTS/DAEDALUS/runs/2026-11-12_HARNESS_RETEST.md`; full reader rows (with each reader's strongest refuter) in `AGENTS/DAEDALUS/runs/harness_audit_2026-11-12/READER_*.md`.

**ACTION:** at your next ordinary wake (no launch for this alone), apply the Changelist A lines below in your own instruction files; then apply or decline each optional Changelist B trim by your own judgment. Record what you applied and declined in your STATUS or closeout. Do not edit another desk's file.

Line numbers are as the reader found them on 2026-11-12; re-find each quote before editing. Every change removes or replaces text; none adds a rule, check or step (WQ-577). † = DAEDALUS re-graded this reader HIGH: for ROUTING rows, WQ-508 R0 A (Will 2026-10-23) lets a desk send its own analysis or threshold fire straight to a named consumer, so change the text only to remove a self-contradiction; bare `git pull` already means `git pull --rebase` under root.

## Changelist A — none for this desk

## Changelist B — optional trims (16)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| M35 † | HANS/CLAUDE.md:68-79 | ROUTING / CARVE-OUT | HIGH | REWRITE | "Write a single `.md` file to `outbox/` per signal … Deliver it yourself: write the same packet directly to the target agent's `inbox/`" | "Signals → WALTER (root). Analysis packets → recipient `inbox/`, commit it yourself (carve-out ①)." Strike the template |
| M36 | HANS/CLOSEOUT.md:7 (step 7), CLAUDE.md:204 | CANON-CONTRADICTION | MED | REWRITE | "`LAST_COMPLETION.md` — overwrite, do not append: STATUS / CHANGED / RESULT / GAPS / WILL_NEEDS / FOLLOW-UP." | Replace with the dated `PROME/inbox/` memo (COMPLETION_SPEC method 1), as ZHAO L57 does |
| M37 | HANS/CLOSEOUT.md:41, :43-44, :46-47 vs :34, :48 | STALE-INVOKER (dead path by cwd) | MED | REWRITE | L41 "`bash scripts/orphan_check.sh HANS`" vs L48 "`python3 ../../scripts/read_cap_check.py --agent HANS`" | One cwd for every command: root-anchored `"$(git rev-parse --show-toplevel)/scripts/…"` (shorter than the current mix) |
| M38 | HANS/CLOSEOUT.md:23 | GIT-SAFETY | MED | REWRITE | "**Bounce** \| Mid-session restart, back within the hour \| STATUS header line only \| No" | "Bounce: commit what you touched (root session-end step 1)" — same length |
| M39 | HANS/CLOSEOUT.md:47 | CANON-CONTRADICTION | LOW | REWRITE | "1e always: `python3 scripts/claim_check.py --check weekday STATUS.md workbook/KB.tsv registry/THRESHOLDS.tsv`." | Use root 1e's path list (`PROME/DOCKET.tsv PROME/GATES.tsv PROME/WILL_QUEUE.md` + own files), or cite root |
| M40 | HANS/CLOSEOUT.md:8, :10; CLAUDE.md:46 | HISTORY-IN-STEP / DUPLICATE | MED | STRIKE | CLOSEOUT L8 "one of the minority of 44 desks with neither (3 desks carry a `CLOSEOUT.md`; 24 carry a closeout heading" | Strike both CLOSEOUT boxes (→ `CHARTER_PROVENANCE.md`); CLAUDE.md §CLOSEOUT → one line "Run `CLOSEOUT.md`; runner `scripts/closeout_check.py`" (~2.5 KB saved across both files) |
| M41 | HANS/CLOSEOUT.md:59 | STALE-INVOKER / HISTORY | LOW | STRIKE | "If boot reads it, closeout owns writing it — that symmetry is the check" | Strike; the step → surface mapping is already in steps 2-5 |
| M42 | HANS/CLOSEOUT.md:32 + steps 8-11 | DUPLICATE / MECHANIZED | LOW | REWRITE | "Steps 8–11 are the root protocol, enumerated by name because pointing at root is what let one go missing." | Keep the four step NAMES with commands, drop the restated root caveats (L45, L46 second sentence) |
| M43 | HANS/CLOSEOUT.md:49 | HISTORY-IN-STEP | LOW | REWRITE | "(2026-09-18: I tailed all ~8 pushes, misread `NOT PUSHED` as a non-ff abort, and reported the wrong mechanism to Will" | Keep "Never pipe `safe-push.sh` through tail/head; read its state line." Strike the story |
| M44 | HANS/CLOSEOUT.md:4, :14 | RUNTIME | LOW | REWRITE | "Run before `/clear`, `/new`, or handoff." | "Run before ending or handing off a session." |
| M45 | HANS/CLAUDE.md:63-65 | HISTORY-IN-STEP | MED | REWRITE | "Guard added 2026-08-28 after I did exactly this. A `for f in inbox/*.md; do mv "$f" processed/; done` succeeds" | Keep L63 ("one file at a time, only after reading it; never bulk-move") and strike L64-65 |
| M46 | HANS/CLAUDE.md:164 vs :149 | OTHER (internal contradiction) | LOW | REWRITE | L164 "Watch tier FIRED 2026-08-28." vs L149 "THIS TABLE CARRIES BANDS ONLY — NO LIVE VALUES, BY RULE." | Strike the fire state; registry `state` / FIRED_LOG own it |
| M47 | HANS/CLAUDE.md:103 | OTHER (dated one-off in charter) | LOW | REWRITE | "⚠️ READ THE ECB FSR MAY-2026 SPECIAL ARTICLE AT PRIMARY. Until that is done the self-binding constraint from LIQUID still binds" | Move the open obligation to STATUS's owed board; keep "EU bank/private-credit leg is HANS's (Will 2026-08-28)" |
| M48 | HANS/CLAUDE.md:15, :33-35, :153, :155, :177, :183, :199, :215 | HISTORY-IN-STEP | MED | REWRITE | L35 "the row that once sat 6.5 months stale at 4.50 is now pulled every session" | Strike dated stories (each already points to `CHARTER_PROVENANCE.md`); L199's 14-check catalogue → "run `doc_audit.py` (checks listed in its `--help`)" (~3 KB saved) |
| M49 | HANS/CLAUDE.md:17, :19; CLOSEOUT.md:34 | DUPLICATE / MODEL-OBSOLETE | LOW | STRIKE | "⚠️ YOUR #1 RULE: Always WRITE findings to STATUS.md." | Strike (root File > verbal); RULE #1b is CLOSEOUT step 1 + 12 — keep it there only |
| M50 | HANS/CLAUDE.md:23 | MODEL-OBSOLETE / HISTORY | LOW | STRIKE | "RULE #1d … A CHECK DECLARES ITS OWN PERIMETER; IT NEVER BORROWS ANOTHER CHECK'S. C11 iterated `REG_VX`, inheriting a C3-only exclusion" | Strike; a check-design lesson for `doc_audit.py` maintenance, not a boot gate → `ML-HANS-463` already holds it |
