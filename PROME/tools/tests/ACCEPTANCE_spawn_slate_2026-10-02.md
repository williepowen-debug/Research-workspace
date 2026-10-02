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

## Worked examples
*(filled from the tool's first run — FALCON-class, HENRY-class and FLG-class rows, generated)*

## Implementation record
*(appended after the build)*
