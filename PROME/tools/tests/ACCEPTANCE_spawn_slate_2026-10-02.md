# ACCEPTANCE CONDITIONS — the prepared spawn SLATE (`PROME/tools/spawn_slate.py` → `PROME/state/SPAWN_SLATE.md`)

**Written 2026-10-02 13:32 EDT by DAEDALUS, BEFORE any code** (WQ-229). Commission: `AGENTS/DAEDALUS/inbox/2026-10-02_from-PROME_spawn-list-harden-into-prepared-slate.md` (PROME `prome-96`, Will: *"okay put in DAEDALUS inbox I will spawn in separate window"*). At this stamp `PROME/tools/spawn_list.py` md5 = `0cb871112c38979785a506f8189f4303`, HEAD `3892a8e40`; `spawn_slate.py` does not exist.

## The property, in its own terms

`spawn_list.py` answers WHO is due. PROME then spends boot context answering five more questions by hand for every row: is it already answered, which rows belong to one wake, what is the assignment, what else would ride along, and what it costs against the cap. The slate pre-computes those five from committed state.

**The property is not "print more fields."** It is: *the slate is a deterministic projection of DOCKET · GATES · ROSTER · ORCH_LOG · git history that (P1) loses no row the census has, (P2) never asserts more than its evidence and fails toward MORE PROME reading, never toward a hidden row or a suppressed spawn, and (P3) changes nothing about `spawn_list.py`'s contract.*

## Design decisions fixed before the edit (two are pushbacks on the brief — PROME rules them)

| # | Decision | Why |
|---|---|---|
| D1 | **A sibling, `spawn_slate.py`, importing `spawn_list`; `spawn_list.py` is not edited.** | The brief allows "or a sibling it writes". `spawn_list` has three live consumers (`prome_gate`, `session_presence`, `desk_activity`), a row contract broken once by an insertion (9/19), and open residue (L455 R2-1/R2-2, L459). PROME is in a live session, so I do not edit its file (DAEDALUS AUTHORITY guard 2). The gate wiring is one added `run_script` line, handed to PROME as text. |
| D2 | **PUSHBACK on brief item 3 ("owner's own vocabulary … FALCON vs HENRY vs FLG").** The assignment is assembled from VERBATIM spans of the row (description, source cell, `Done when` clause), never paraphrased, and never from a per-desk lexicon. | The row is already written in the desk's vocabulary by the desk and PROME. A per-desk phrase table is a second hand-maintained copy of 40 charters with no reader (PAT-099), and a deterministic paraphrase of a narrative cell returns something well-formed and wrong (PAT-158). Worked examples for three desks are in §Worked examples below, generated, not hand-written. |
| D3 | **PUSHBACK on the token `ALREADY ANSWERED` as a verdict.** The token is kept, but it is defined as an EVIDENCE class (an explicit owner return citing the row, with no hedge word on the citing lines), and its stanza always says what PROME still owes: one read of the cited artifact, then the row's write-back. | An instrument cannot tell "answered" from "answered a different question" (the brief's own bullet 4). FERT on 10/02 is the live case: a return packet citing T11 whose content is *not published yet*. |
| D4 | PROME-owned and WILL-owned rows get NO stanza; they stay in the census, every row, with a one-line count above the stanzas. | 24 of today's 32 rows are PROME-owned. A stanza each would put the slate over the 32,550 B whole-read budget and bury the eight that need a spawn decision. Nothing is hidden: the census lists them. |
| D5 | WQ-206 (aged ACTION) and WQ-221 (aged waits) candidates are NOT enumerated in v1. Each stanza prints the desk's inbox count and oldest packet so the whole-inbox drain is visible; the lane column says `WQ-184 L0` because that is the only lane this instrument computes. | WQ-221 has its instrument (`prome_gate.check_aged_waits`) and by rule enters through a DOCKET row, so it arrives here already. WQ-206 has no instrument anywhere in `PROME/tools` or `scripts/` (grep at this stamp) — a finding for the delivery packet, not a silent addition. One process change per session (WQ-299 R1). |

## Pre-check classes (ACTIVE rows only) — definitions the tests and the reader grade against

Evidence window opens at: DOCKET single date → that date · DOCKET window → its start · GATES → `review_by` − 7d.
A **citation** = the row key (`L475`, `D:L475`, `DOCKET L475`, the gate id) or a **discriminating identifier** from the row's description cell (`WQ-n`, `GATE-…`, `FORUM-n`, prediction ids like `FERT-11`, `CRU-05`, `HEN-F1`) that appears in the description of at most 2 open rows.
An **explicit return** = an owner self-commit (by `spawn_list.attributed`) inside the window whose MESSAGE carries a citation, or a packet `PROME/inbox/**/<date>_from-<OWNER>_*` added inside the window whose name or text carries one.

| Class | Rule | What the stanza tells PROME to do |
|---|---|---|
| `ALREADY ANSWERED` | ≥1 explicit return AND no hedge marker on the citing line(s) | read the ONE cited artifact, then write the row's state — no spawn |
| `PARTIAL ANSWER` | an explicit return whose citing line carries a hedge marker (`not yet`, `not published`, `pending`, `WAIT`, `armed`, `owed`, `deferred`, `partial`, `re-date`, `unresolved`, `open`, `not done`, `ungraded`) · OR the owner touched a file the row's source cell names, with no citation | read the cited artifact; the remainder decides re-ping vs wait |
| `NO EVIDENCE` | the owner has self-commits in the window and none of the above | the receipt gap is real: doorbell/re-ping the owner on this row |
| `UNCHECKED` | the check could not run or could not finish (git failure, commit window truncated, no window date) — the reason is printed | treat as NO EVIDENCE until run by hand |

## Acceptance conditions — ALL must hold

1. **(ORDINARY — conservation, P1)** Every row `spawn_list.collect()` returns at the same inputs appears in the slate exactly once: each desk-owned row inside exactly one stanza; every row in `## Mechanical census`. The census body is the output of `spawn_list.render()` itself, not a re-implementation. The slate prints `rows in = stanza rows + PROME + WILL + UNKNOWN`; a mismatch sets rc 2 and a `SLATE INCOMPLETE` banner as the first line.
2. **(NO CONTRACT CHANGE, P3)** `spawn_list.py` md5 unchanged; `--selftest`, `--cadence-selftest`, `test_spawn_list_fail_closed.py`, `test_spawn_list_desk_commit_attribution_L455.py`, `test_presence_reader_contract.py` stay green. `spawn_slate.py` returns the same rc as `spawn_list.py` on the same inputs (2 UNKNOWN · 1 DARK · 0), except rc 2 on a conservation failure.
3. **(PRE-CHECK, P2)** The four classes follow the table above. Direction on ambiguity: a hedge marker can only DOWNGRADE to PARTIAL; a git failure is UNCHECKED, never NO EVIDENCE and never ANSWERED; a DARK row is not pre-checked and says so. Every ANSWERED/PARTIAL line names the sha and the file.
4. **(WRONG OWNER)** A citation in a commit that is not the owner's own (PROME's annotation commit, another desk's packet, a body-line mention) is never an explicit return. `_from-WAL_` never matches `_from-WALTER_`. A packet from the owner that cites a DIFFERENT row is not evidence for this one.
5. **(OVERLAP)** (a) a desk with one DARK and one ACTIVE row gets ONE stanza headed as a spawn candidate, with both rows classed separately; (b) a packet present in both `PROME/inbox/` and `processed/` history counts once; (c) a row with an explicit return AND a later PROME annotation in its state cell shows both; (d) a desk IN-FLIGHT in `ORCH_LOG` today is flagged `IN-FLIGHT — do not spawn; corroborate with ListAgents` whatever its class.
6. **(ASSIGNMENT)** ≤120 words per stanza (measured by the test, not asserted). Every quoted span is a verbatim substring of its row cell after whitespace normalisation. Truncation is always marked `[…]` with `read D:L### whole`. Sentences in the row carrying `⛔` are carried verbatim in a separate `Must travel` field, outside the word count, never dropped (anti-laundering: a caveat that could change the action survives).
7. **(MERGE)** One stanza per desk. Rows ordered by due date then key, numbered as a sequence. No judgement of "independent" rows is attempted (declared), because one spawn is one desk session.
8. **(RELATED)** Same-desk rows landing in +14d sit under `Would also fit`, never under `Why now`. Rows naming the desk as a NON-first owner are listed as `named, not first owner` — `spawn_list` reads the first token only, and L287 (LABOR / CARL) on 10/02 shows the second owner was a real spawn.
9. **(CAP)** Only stanzas with ≥1 DARK row and no IN-FLIGHT flag take a slot, numbered in slate order: `slot k of 4`; k > 4 prints `beyond the ordinary cap → Will's slate, unless the C6 terms hold (PROME's judgement)`. Today's `ORCH_LOG` `1-SPAWN` count is printed as context with its limit stated (cap is per BOOT; cap-bearing classification is open at DOCKET L444).
10. **(MISSING INFORMATION)** Unreadable ROSTER / ORCH_LOG / packet dir ⇒ that field reads `CANNOT-EVALUATE (<reason>)` and the stanza still prints. Unreadable DOCKET or GATES ⇒ rc 2 and the slate file is overwritten with a FAILED banner — never left as a stale file that looks current. Owner absent from ROSTER's launch classes (ACTIVE · TIER-2 · SPECIAL) ⇒ `NOT LAUNCHABLE per ROSTER — re-own the row`, no cap slot.
11. **(STALENESS)** Line 1 carries the generation stamp from the wall clock, the as-of date and HEAD sha. Weekday names are computed from the date, never typed.
12. **(READ CAP)** The byte size and % of 32,550 B are printed in the header. Over budget ⇒ a banner; never silent truncation.
13. **(DETERMINISM / NO LLM / NO NETWORK)** Two runs at the same HEAD and `--as-of` are byte-identical below line 1. Imports: stdlib + `spawn_list` only. Reads committed state (`git show`/`git grep` at one captured HEAD) for evidence.
14. **(CONCURRENT ACTIVITY — justified N/A beyond 13)** HEAD is captured once and every evidence read uses that sha; a commit landing mid-run changes the next run, not this one.
15. **(NO SPAWN AUTHORITY, NO SECOND CALENDAR)** The tool writes exactly one file (`--out`) and nothing else; it stores no dates of its own.

## Independent verification (states kept distinct: IMPLEMENTED · TESTED · INDEPENDENTLY VERIFIED · STILL UNRESOLVED)

- **Reader A (three-reader test, brief item 2):** an Opus reader who did not write the tool reads the cited commit/packet for EVERY live `ALREADY ANSWERED` row on the first slate and says SURVIVES / FAILS per row, plus ≥1 counterexample of its own against the class rules. Pass = zero FAILS.
- **Reader B (cold read, brief item 5):** an Opus reader given the slate ALONE answers "which desks to spawn, in what order, with what brief, and which rows only need PROME's write-back". Graded against today's `ORCH_LOG` (what PROME actually did on 10/02).
- **Backtest (reported, not gated):** replay the pre-check over the daily DOCKET vintages since 2026-09-19; for each row classed `ALREADY ANSWERED`, its state at HEAD (terminal · re-dated · still PENDING on the same date). The count is a first base rate; a threshold is PROME's to set after the trial week.

## Worked examples (generated 2026-10-02 14:0x EDT by `spawn_slate.assignment`, not hand-written)

| Row class | Output |
|---|---|
| VULCAN `D:L564` (a slot reading) | *VULCAN: 1 registered row due. 1) D:L564 (due Fri 10/02): "VULCAN FRIDAY POST-CLOSE SLOT — `mag7.py` slot 4 + GPU reading 4 (the first `GPU_SERIES.tsv` row). A POST-CLOSE reading: a spawn before ~16:00 ET cannot take it. […]" Return: your own record updated + one packet to PROME/inbox/ citing each row key.* (81 words) |
| FALCON gate + window, merged (horizon 30) | *FALCON: 2 registered rows due — in this order. 1) G:GATE-FALCON-001 (due Tue 10/06): "Bab el-Mandeb EXECUTION tripwire, ANY of 3: (1) UKMTO/Ambrey/JMIC-confirmed post-7/20 Houthi enforcement attack […]" […] read G:GATE-FALCON-001 whole. 2) D:L229 (due Mon 10/26): "★ IRAN-OMAN PERMANENT-ROUTE WINDOW — […]" […] read D:L229 whole. Return: …* (117 words) |
| HENRY `D:L475` (a forum verdict) | *HENRY: 1 registered row due. 1) D:L475 (due Thu 10/01): "FORUM-7 — PATH vs PREMIUM pre-registered verdict rule for the 9/23–9/24 rates move […]" […] read D:L475 whole. Return: …* (88 words) |
| FLG | no FLG first-owner row inside +30d at this stamp (L522's window ends 11/09) — no example |

## Implementation record — 2026-10-02 14:0x EDT (DAEDALUS)

**STATE: IMPLEMENTED · TESTED · INDEPENDENTLY VERIFIED: PARTLY (see Reader A) · NOT WIRED · STILL UNRESOLVED listed below.**

| Item | Value (measured at this stamp) |
|---|---|
| Tool | `PROME/tools/spawn_slate.py`; `spawn_list.py` md5 still `0cb871112c38979785a506f8189f4303` |
| Tests | `test_spawn_slate.py`, `grep -c 'def test_'` = 37, all pass; throwaway repo only |
| Guard falsification | 18 hand mutants of v2 + 2 of the round-2 fixes: 20/20 killed (v1: 12 mutants, 2 survived until two tests were added) |
| Regressions | `--selftest` 11/11 · `--cadence-selftest` PASS · fail_closed 15/15 · L455 attribution OK · presence-reader contract PASS |
| rc parity | slate rc 1 = `spawn_list` rc 1 on the live inputs |
| Determinism | two `--stdout` runs byte-identical below line 1 |
| Runtime | 1.8 s at horizon 0 (`spawn_list` alone 0.75 s) |
| Size | 26,064 B = 80% of 32,550 B at horizon 0; 29,297 B = 90% at horizon 3 (a Friday closeout) |

### ⛔ Condition 3 as written FAILED its independent read, and the classes were WITHDRAWN (not patched)

**Reader A, round 1 (Opus, did not write the tool; ledger `AGENTS/DAEDALUS/runs/2026-10-02_spawn_slate/readerA_ledger.md`): THREE-READER TEST FAIL — 2 SURVIVES of 4.**

| Row v1 marked `ALREADY ANSWERED` | Reader's verdict | Deciding words in the owner's own return |
|---|---|---|
| `D:L475` HENRY | SURVIVES for HENRY's leg; right by luck (decided by a later "consistency" memo, not the FINAL); BOND's co-sign still pending | "HENRY-graded, BOND co-sign PENDING" |
| `G:GATE-BRENT-COT-35B` | **FAILS-WRONG** | "Not gradable before 15:30 … re-spawn BRENT >=15:35 ET to grade" |
| `D:L502` CRUISE | SURVIVES | CRU-11 registered with the six elements |
| `D:L582` MIDAS | **FAILS-PARTIAL** | "COT 9/29 — WAIT, not graded this spawn … Please re-spawn at or after 15:30 ET" |

Two of three `PARTIAL ANSWER` rows were false alarms the other way (SHADE: legs delivered in a packet that says "W1", never "L182"; LIQUID: pending on WALTER only). The reader reproduced the failure on history (`--as-of` 9/30, 10/01) and showed the stated rule "a hedge only downgrades" was false (a clean commit subject out-voted the hedged packet it carried).

**Disposition (DAEDALUS): the brief's four-token classification is not buildable from keywords and v2 does not attempt it.** Pushback D3 said `ALREADY ANSWERED` could only be an evidence class; the read showed it cannot be even that without suppressing needed spawns (BRENT and MIDAS both asked for a ≥15:30 re-spawn and v1 said "no spawn"). v2 tokens:

| v2 token | Rule | Stanza says |
|---|---|---|
| `RETURN FOUND` | ≥1 owner self-commit or owner→PROME packet in the window cites the row (strong first, then newest; up to 3 shown; hint words printed, deciding nothing) | READ FIRST — it may answer the row, one leg, or only say why it cannot be answered yet |
| `NO CITING RETURN` | none cites it; a touched cited file and the owner's uncited packets are listed; zero owner commits in the window is said as "dark this cycle" | re-ping text is prepared |
| `UNCHECKED` | git failure | treat as NO CITING RETURN |

Conditions amended by this: **3** (tokens above; no verdict token is ever printed — tested) · **5(d)** (IN-FLIGHT is a flag, never a suppression: the ledger was stale for CRUISE and MIDAS on 10/02, both had delivered) · **9** (an in-flight DARK desk keeps its slot and carries "check liveness first") · evidence window for GATES = `review_by` − 6d, not − 7d (a weekly gate's previous review day fell inside −7d). Conditions 1, 2, 4, 6–8, 10–15 hold as written; LANDS-only desks render as a table (still conserved).

**Reader A, round 2 (same reader, one bounded read of the rewrite): 7 of 13 items RESOLVED · 6 MITIGATED · 0 open · dangerous-direction paths: 1.** The one path (a gate's ACTIVE class dates from REGISTRATION in `spawn_list`, so an owner dark all cycle read as "in session") was fixed after the read and is NOT re-read: zero owner commits in the window now prints "dark this cycle: weigh it as a spawn candidate" (replayed on the reader's case, GATE-FERT-G5 as-of 9/30; test + mutant). The reader confirmed no path says "no action" and no due row is dropped.

**Reader B (cold read of the v1 slate alone, Opus `coldreader`; ledger same dir): 18 ✅ · 24 ⚠️ · 2 ❌ of 44 claims.** Its plan matched the day: spawn VULCAN only, not before ~16:00 ET. Both ❌ fixed in v2 (the in-flight summary line contradicted two stanzas; non-first-owner lists drew on rows outside the census). Ambiguities fixed: timing words now in the headline and the top list; `## Terms` defines ACTIVE (two senses), cap, C6, boot, re-ping, strong return. **v2 has NOT had a cold read.**

**Backtest (reported, not gated; run on v1 classes):** 13 daily vintages 9/19–10/01, 7 distinct rows seen ACTIVE at end of day — thin, because PROME closes most rows the same day. It is not evidence for v2.

### STILL UNRESOLVED (declared)

| # | Residue | Direction |
|---|---|---|
| R1 | Whether a return ANSWERS a row is not computed. It is a read — PROME's, or a reader's | by design |
| R2 | The before-due flag tests only the first-listed return, by date; a forward reference dated ON the due date is not flagged | costs a read |
| R3 | An answer that names neither the row key nor a discriminating id is found only among "other packets" (6 shown, newest first) | costs a hunt (SHADE L182) |
| R4 | Junk identifiers are still extracted (`SL-5`, `PR-6`, `PASS-2`…); they can produce a body-mention return | costs a read |
| R5 | Hint words on a packet come from its whole body: they describe the packet, not the row | advisory only |
| R6 | Inherits `spawn_list`: first-owner-only classing; attribution residue L455 R2-1/R2-2; cadence reader L459; DARK/ACTIVE from the row's START date | as `spawn_list` |
| R7 | A `git log --since` walk stops at the first older commit; live history has 1 date inversion in 4,000 commits (−1 s) | toward NO CITING RETURN |
| R8 | Timing words are matched by pattern; a row whose timing is phrased another way gets no ⏱ | PROME's read |
| R9 | 80% / 90% of the whole-read budget on a quiet Friday; a heavy day will exceed it. The banner prints; nothing truncates | read by section |
| R10 | WQ-206 (aged ACTION) has no instrument anywhere; not added here | PROME's call |
| R11 | Fixes made after round 2 (gate window −6d, dark-this-cycle line, uncited-packet list of 6, annotation window, notes-cell timing words) are tested and mutant-checked but unread by an independent reader | declared |
