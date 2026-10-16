# Boot rewiring — gate first, read on flag

**Status:** PROPOSAL (for discussion; nothing here is approved or implemented). **Author:** PROME (session prome-ac), on Will's 10/16 11:45 ET ask ("suggest any changes/updates/rewiring which would make the bootup operate better"). **Companion:** five ideas rows dated 2026-10-16 in `PROME/ideas/list.tsv` (commit ef88d6561). **Measurements:** `PROME/tools/measure.py` on the 10/16 boot reads; the boot run is `/tmp/prome-boot-c4a172af/`.

## The problem in one line
The boot reads about 320 KB of text before the mechanical gate runs, and the gate then answers most of the questions the reading was for. Reading comes first, deciding comes second; it should be the other way around.

## Principle
**Gate first, read on flag.** The instrument runs first and prints a short card. PROME reads a surface only when the card names it. Narrative records are written at closeout for history; they are not the boot's input.

## The changes, cheapest first

| # | Change | What it replaces | Saves | Who rules |
|---|---|---|---|---|
| 1 | Add the held names and option underlyings to the dashboard's position tier (HBAN, QQQ, SPY, USO, GLD, VLO, TBT, APD, CMG, CRWV, APO) | A second `fetch.py price` pull after the dashboard | one tool call per boot; one price vintage instead of two | PROME (FORGE tool, own lane) |
| 2 | Gate prints only the spawn slate's "Read this first" block; stanzas stay in the file for drill-down | Reading a 43 KB generated file (133% of its budget) | ~40 KB | PROME (process slot) |
| 3 | Delta brief rule: when WALTER has briefed Will the same morning, PROME's catch-up is what moved since plus the book tie-in, not a second full brief | Two full briefs of the same six signals | Will's time | PROME (operator-surface clause already permits it) |
| 4 | Reorder BOOT.md: step 0 repo state → ONE-SHOT GATE → read gate card → USER/HANDOFF-resume → conditional reads | Reads 1–4 before the gate | no bytes, but the reads become targeted | PROME manual; Will's word since it changes boot order |
| 5 | Move ACTIVE_DECISIONS and GATES from whole-read to instrument-covered in `PROME/registry/READS.tsv`; read a row only when the gate flags it (fired-unexecuted · consumed_by · review_by already checked there) | 91 KB whole read that answered nothing on 10/16 | ~91 KB (28% of the boot) | Will (READS manifest is a declared contract) |
| 6 | One session record: HANDOFF keeps a ≤10-line resume paragraph; SCRATCH ★ NEXT keeps the owed list only; STATUS header keeps a one-line stamp. The prose retelling lives once, in `memory/YYYY-MM-DD.md` § Closeout, and the other two point at it | Three prose retellings of the same session (~53 KB), the drift class spine audits keep finding | ~30 KB and a defect class | Will (changes CLOSEOUT's write-back contract) |
| 7 | HEARTBEAT boot read = the one-liner, the eight section leads, Thresholds and Kill-on-sight; the level table is NOT a boot read (the dashboard pull replaces it by rule anyway) | Reading levels I must re-pull before citing | ~5 KB and a stale-level temptation | PROME (read scope, file unchanged) |
| 8 | Rules de-duplication: Git protocol, spawn preflight and skipped-control rule each live in ONE of root CLAUDE.md / PROME/CLAUDE.md / BOOT.md; the other two point | Reading the same rule two or three times (74 KB of rules) | ~15–20 KB; a change lands once | Will (root canon is Will-gated; 10/25 freeze) |

## What a boot would look like after
1. Repo state and clock (unchanged).
2. One-shot gate → prints the card: fired/unexecuted · BOARD new since cursor · due rows and dark owners (read-first block only) · Will-queue due/passed · Deck taps · capability gaps · book line.
3. Read USER.md and the HANDOFF resume paragraph (≤10 lines).
4. Read only what the card names (a flagged GATES row, a BOARD action line, a due DOCKET row).
5. HEARTBEAT one-liner and leads for regime orientation; dashboard for levels.
6. Report, then continue.

Estimated boot reading: ~140 KB (rules 74 → ~55 after #8, gate card ~9, USER 7, HEARTBEAT ~18, memory index 18, HANDOFF resume ~2), from ~320 KB today. The rules documents remain the largest block; only #8 moves them.

## What this does NOT change
Root rule #4 (live prices), the one-shot gate's checks, the WQ-184 spawn rules, the Desk-spawn preflight, the Deck pickup, the skipped-control report, or any gate letter. Fewer bytes read, same obligations.

## Sequencing
#1–#3 are PROME's own lane and can go one per session under the process ceiling. #4–#7 are one coordinated change to BOOT.md, CLOSEOUT.md and READS.tsv and belong at the 2026-10-25 process review (WQ-299 R3 freeze) with a plan read and a result read. #8 is a root-canon edit on Will's word, same sitting.

## Risks
- #5: a GATES row the gate does not check (a new column, a parser miss) goes unread. Mitigation: the gate's GATES checks already cover the four fields boot step 3 names; add a "columns checked" line to the card so an unchecked column is visible.
- #6: a resume paragraph can hide a load-bearing caveat. Mitigation: the owed list stays itemized in SCRATCH; only the prose retelling moves.
- #4: a gate crash (rc=2) leaves PROME without a card. Mitigation: fall back to today's full read order, declared SKIPPED.
