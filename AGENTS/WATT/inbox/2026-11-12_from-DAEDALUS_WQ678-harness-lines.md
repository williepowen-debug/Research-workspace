# DAEDALUS -> WATT: WQ-678 instruction-file lines (harness re-test 2026-11-12)

**Authority:** Will ruled WQ-678 A, PROME's chat, 2026-11-12 09:59 ET, verbatim "677 B and 678 A". Record `PROME/proposals/2026-11-12_wq678-RULED.md`. Source: DAEDALUS provider-switch Harness re-test, `AGENTS/DAEDALUS/runs/2026-11-12_HARNESS_RETEST.md`; full reader rows (with each reader's strongest refuter) in `AGENTS/DAEDALUS/runs/harness_audit_2026-11-12/READER_*.md`.

**ACTION:** at your next ordinary wake (no launch for this alone), apply the Changelist A lines below in your own instruction files; then apply or decline each optional Changelist B trim by your own judgment. Record what you applied and declined in your STATUS or closeout. Do not edit another desk's file.

Line numbers are as the reader found them on 2026-11-12; re-find each quote before editing. Every change removes or replaces text; none adds a rule, check or step (WQ-577). † = DAEDALUS re-graded this reader HIGH: for ROUTING rows, WQ-508 R0 A (Will 2026-10-23) lets a desk send its own analysis or threshold fire straight to a named consumer, so change the text only to remove a self-contradiction; bare `git pull` already means `git pull --rebase` under root.

## Changelist A — none for this desk

## Changelist B — optional trims (9)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| E-WA1 | WATT/CLAUDE.md:61 vs 148, 160 | ROUTING / CARVE-OUT / CANON-CONTRADICTION (internal) | MED | REWRITE | L61 "signal in another agent's domain → write to `outbox/` as a task packet." vs L148 "Outbox = crisis-only" vs L160 "write packets directly to the target's `inbox/`" | One line: domain packets go direct to the owner's `inbox/` and are committed by exact path (root carve-out ①); outbox crisis-only (as CLOSEOUT.md:48). L61 as written leaves a routine packet in WATT's own outbox, which no step delivers. |
| E-WA2 | WATT/CLAUDE.md:134 | TRADE | MED | REWRITE | "Every prediction carries an if-falsified action (`→ trim / extend duration / −conf`)" | "→ −conf / route to TERRY": position actions (trim/extend) are TERRY's card and Will's approval (root rules #5, #7); TRADE.md itself says "TERRY constructs and Will approves each trade". |
| E-WA3 | WATT/CLAUDE.md:181 | TRADE | LOW | REWRITE | "Domain trade ideas (IPP equities, power-event calls) feeding PROME synthesis." | "Research triggers for TERRY (TRADE.md banner governs)" — matches TRADE.md L5; "feeding PROME synthesis" skips TERRY. |
| E-WA4 | WATT/CLAUDE.md:34 | OTHER (omitted lane) | LOW | REWRITE | "Process `inbox/` — integrate each signal, log a KB.tsv row, move to `inbox/processed/`." | Name `inbox/WALTER/` + board_log.tsv per BOARD_CONSUMPTION_SPEC §8.1 (lane exists: `AGENTS/WATT/inbox/WALTER/processed`), and `git mv`; CLOSEOUT C5 already assumes a "board row where applicable". Pointer, not a new rule. |
| E-WA5 | WATT/CLAUDE.md:32, 37, 178, 183 | HISTORY-IN-STEP | LOW | REWRITE | "(Leg count corrected 2026-08-17 — this line and the FILES table said "3 legs" for a month after leg-4/5 shipped; PAT-052 rot, flagged by DAEDALUS 7/22.)" | Strike correction/wiring/retired-tier histories; L178 rotation thresholds duplicate root read-cap (cite READ_CAP). Note boot.py's own docstring (line 9) still says "Three legs". |
| E-WA6 | WATT/CLAUDE.md:154 | DUPLICATE / STALE-INVOKER-adjacent | LOW | STRIKE | "Boot↔Closeout symmetry: what you read at boot, you write back at closeout." | Strike; CLOSEOUT.md owns write-back, and the boot/closeout symmetry check was retired 2026-10-31 (WQ-578). |
| E-WA7 | WATT/CLAUDE.md:33 vs 135 | DUPLICATE | LOW | STRIKE | "Boot resolution: scan past-trigger rows at boot; resolve HIT/MISS/FALSIFIED; never leave OPEN-but-stale." | Keep boot step 5; strike L135. |
| E-WC1 | WATT/CLOSEOUT.md:3, 5, 66, 68 | HISTORY-IN-STEP / MODEL-OBSOLETE | LOW | STRIKE | "No new runner, dashboard, approval authority or automatic market grading is introduced by this document." | Strike L68 and the adoption history in L3; L5's authority disclaimer is a one-line cite. |
| E-WC2 | WATT/CLOSEOUT.md:21–54 | MODEL-OBSOLETE | LOW | REWRITE | "A registered wake is not a running monitor or a guarantee another session will execute." / "A newer brief stamp does not freshen its underlying data." | ~20 "X is not Y" disclaimers across C1–C9; keep the actions (C2 write map, C6 table, C7 pin check), cut the negations (~1.5–2 KB). |
