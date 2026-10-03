# Spawn slate — build record, and the architect's read on "staff for PROME"

> **CURRENT DISPOSITION 2026-10-03:** source wiring is verified at PROME boot/closeout callsites (initial wiring `43a4c3bc2`); the NOT wired build receipt below is historical. Independent `review_standards` completed R11's five post-round-2 changes against final code: `../runs/2026-10-03_STANDARDS_SLATE_READER_REPORTS.md` §B. Two new residues are reproduced: top receipt-gap label overclaims activity for dark-this-cycle desks; unpinned upstream Liveness can use a commit newer than the captured HEAD. PROME owns these repairs; no edits to its live files in this catch-up. The v2 cold read/staffing trial is not certified by this bounded review.

**2026-10-02 (Fri) · DAEDALUS, Will-launched.** Commission: `inbox/processed/2026-10-02_from-PROME_spawn-list-harden-into-prepared-slate.md` (PROME `prome-96`; Will: *"okay put in DAEDALUS inbox I will spawn in separate window"*). Acceptance conditions + full verification record: `PROME/tools/tests/ACCEPTANCE_spawn_slate_2026-10-02.md` (conditions committed `2a4344d00`, before the code). Delivery: `PROME/inbox/2026-10-02_from-DAEDALUS_spawn-slate-built-answered-class-withdrawn.md`. Reader ledgers, first output, backtest script: `runs/2026-10-02_spawn_slate/`.

## 1. What was built

| Item | Value (measured 10/02 14:0x EDT) |
|---|---|
| Tool | `PROME/tools/spawn_slate.py` — a SIBLING of `spawn_list.py`, which it imports and does not edit (md5 `0cb871112c38979785a506f8189f4303` unchanged) |
| Output | one generated markdown file, default `PROME/state/SPAWN_SLATE.md`; `--stdout` writes nothing |
| Runtime | 1.8 s at horizon 0 (`spawn_list.py` alone 0.75 s) |
| Size | 26,064 B = 80% of the 32,550 B whole-read budget at horizon 0; 90% at horizon 3 |
| Tests | 37 (`grep -c 'def test_'`), all pass; 20 of 20 hand mutants killed |
| Wiring | NOT wired. One `run_script` line for `prome_gate.py`, handed to PROME as text (PROME is live; its file is not mine to edit) |

## 2. The result that matters: the instrument can FIND an owner's return; it cannot tell whether the return ANSWERS the row

The brief asked the tool to class each due row whose owner has been active as ALREADY ANSWERED / PARTIAL / NO EVIDENCE. v1 did that from keywords beside a citation. An independent reader checked every live verdict against the owner's own packet:

| v1 said | Rows | Reader found |
|---|---|---|
| ALREADY ANSWERED (4) | HENRY · BRENT · CRUISE · MIDAS | 2 right. BRENT's packet: "not gradable before 15:30 … re-spawn". MIDAS's: "WAIT, not graded this spawn … please re-spawn at or after 15:30 ET". v1 told PROME neither needed a spawn |
| PARTIAL ANSWER (3) | SHADE · FERT · LIQUID | 1 right (FERT). SHADE and LIQUID had finished their own legs |

**3 right of 7, and two of the errors were in the direction that suppresses a needed wake.** The verdict classes were withdrawn, not patched: v2 prints `RETURN FOUND` (and lists what to open, strong citations first), `NO CITING RETURN`, or `UNCHECKED`, and an active row's headline is always "READ FIRST". A second read of the rewrite found no path that says "no action" and no dropped row; the one dangerous path it did find (an owner dark for a whole gate cycle reading as "in session") was fixed afterwards and is tested but not re-read.

## 3. What the first live slate said (10/02, horizon 0)

| Bucket | Rows | Meaning for PROME |
|---|---|---|
| Spawn candidate | 1 (VULCAN `D:L564`; the row's own words: not before ~16:00 ET) | one Tier-1 wake, later today |
| Read first — owner returned, row still open | 7 (SHADE · HENRY · BRENT · CRUISE · FERT · LIQUID · MIDAS) | one read each. Per the reader: 2 need a ≥15:30 re-spawn (BRENT, MIDAS), 1 waits on a publication (FERT), 4 need only the registry write-back or another party (HENRY/BOND co-sign, SHADE/Will, LIQUID/WALTER, CRUISE) |
| PROME's own due rows | 24, oldest 15 days overdue | no desk can run these |

**Of 32 due rows, 1 was a spawn-preparation problem. 7 were reading problems. 24 were PROME's own queue.**

## 4. Design decisions and what they cost

| Decision | Reason | Cost / limit |
|---|---|---|
| Sibling file, `spawn_list.py` untouched | three live consumers; a row contract broken once by an insertion; open residue (L455, L459); PROME live | the slate inherits every `spawn_list` limit (first-owner-only, attribution residue, ACTIVE dated from the row's start) |
| Assignment = verbatim row quotes, no per-desk lexicon (pushback on the brief) | the row is already in the desk's words; a phrase table is a second copy of 40 charters with no reader (PAT-099); paraphrase of a narrative cell is well-formed and wrong (PAT-158) | a multi-desk row quotes every desk's leg; long rows are cut and say so |
| No answered/partial verdict (§2) | failed its independent read | PROME reads one artifact per active row; the tool saves the hunt, not the read |
| PROME/WILL rows: census only | 24 of 32 rows; stanzas would breach the read budget | PROME's backlog is a count and a table, not prepared work |
| WQ-206 / WQ-221 lanes not enumerated | WQ-221 has its instrument and enters through DOCKET; WQ-206 has NO instrument in `PROME/tools` or `scripts/` | the aged-ACTION lane is still held in PROME's head |

## 5. The architect's read on "staff for PROME"

**Recommendation: run the slate for the bounded trial week. The build already shows where an instrument stops and a reader is needed — and it is not scheduling.**

| Question | Evidence from this build | Source |
|---|---|---|
| Is spawn PREPARATION the load? | 1 of 32 due rows on 10/02 | §3 |
| Where did the instrument fail? | judging whether a return answers its row: 3 right of 7 by keyword | §2 |
| Would a scheduling helper have woken FALCON sooner today? | No — the cap and the Tier-2 gate stopped it. That is WQ-369, Will's | WALTER's memo, `PROME/inbox/2026-10-02_from-WALTER_scheduling-helper-view-and-bounded-spawn-question.md` row 1 |
| What was the day's real calendar failure? | the collection job ran 3–6 h late on five runs, and no instrument checks it | WALTER's memo row 2 (five `gh run list` rows, not a longer history) |
| What else can no instrument here do? | read timing words in a row · see liveness (in-process teammates are invisible to `ListAgents`; ORCH_LOG was stale for 2 desks today) · write the row back | this build + Reader A |

**If Will wants a seat, the shape the fleet already runs is ANVIL's** (`.claude/agents/anvil.md`: PROME-internal, no roster seat, fresh context, propose-only, PROME commits).

| | Proposal — NOT built, NOT approved; wiring a new agent is always ask-first |
|---|---|
| What | a registrar reader PROME spawns on the slate's `RETURN FOUND` rows: per row it reads the listed artifacts and returns ANSWERED / ONE LEG / NOT YET, the deciding quote, and a drafted DOCKET state cell. PROME reviews and commits |
| Why | this is exactly the job Reader A did by hand today in a few minutes for 7 rows, correctly, where keywords got 3 of 7. It takes the largest measured slice out of PROME's context. It cannot spawn, grade or commit |
| Effort | one agent definition + an acceptance file; about half a session |
| Expected value | unmeasured. The trial week measures it: `RETURN FOUND` rows per boot, and the tokens PROME spends closing them |
| First step | after the trial week PROME brings the counts to Will with this option and the do-nothing option side by side |

**What would change this read:** WQ-369 ruled YES (a prepared assignment could then run without a Will round-trip — WALTER's condition for a scheduler being worth building) · a trial week in which spawn candidates, not reads, dominate · PROME's own-row backlog clearing, which changes the denominator.

**Caveats that travel:** one day's slate is n=1, on a Friday with 13 spawns already made. "24 PROME-owned rows" counts rows, not hours. The slate itself costs PROME roughly 12K tokens if read whole (26 KB at ~2.17 B/token), so it should be read top block first, then by stanza. The reader that judged the 7 rows was one Opus pass with no second reader on its verdicts.
