# scorecard.py v1.2 → v1.3 — residue 1–5 + the inline filename twin (2026-10-01, Will "ok approved go ahead" ~16:2x ET)

**Owed:** `runs/2026-09-25_SCORECARD_V1_2_REPAIR.md` §5 residue 1–5, "fixes 1–5 in one pass with their own fixtures before the 10/02 render, and a plan read before the edit." **This file was written BEFORE the edit (WQ-229).**

## 1. What the live file shows (frozen snapshot, `PROME/WILL_QUEUE.md` md5 `626171b2f4276825159a2b3bc92d337c`, ~16:2x ET; stamps checked at `date` 16:30)
v1.2's column 5 for the 10/02 window (2026-09-26 → 2026-10-02): **RULED 33 stamps · DONE 0 · AMENDED 3 · UNDATED 0.** On 9/25, §5 said "none fires on the live file". **Three now do:**

| row | v1.2 counts | truth at the row | defect |
|---|---|---|---|
| 235 | RULED 2026-09-26 | title `— ALREADY RULED 8/13 …`; cell 3 "✅ Not a new ruling" | residue 3 (a non-head verb in the title counts) |
| 287 | RULED 2026-09-26 **and** RULED 2026-10-01 | one ruling, 9/26. The 10/01 "stamp" is `…-RULED.md`. **+2026-10-01 13:34 ET (prome-0c)`, a FILENAME followed by an encode note | **residue 3's twin on the INLINE path** (`STAMP` regex, inherited from v1.1; not in the 9/25 list) |
| 349 | WITHDRAWN 2026-09-30 (col 4) | correct today, but its title reads `**349 WITHDRAWN — a duplicate of WQ-335 …, which you RULED NOT NOW on 9/30**` | **residue 4's fix as WRITTEN ("prefer RULED anywhere in the title") would turn this into a false RULED** |

The residue list's own fix text is therefore not adopted verbatim. The fix below is keyed on the verb's POSITION in the title, which fixes 3 and 4 together without breaking 349.

**Separately, NOT mine:** the full render for the 10/02 window returns **rc=2 CANNOT-RENDER**, because `PROME/state/ORCH_LOG.tsv` (working copy, dirty, PROME's file) fails schema v2: `drained = 'n/a'` and prose in `inbox_before` on L417–L455. Render #6 will refuse until PROME repairs the rows. Goes to PROME by packet.

## 2. Design (v1.3)
- **Head-position title verb.** A title-form verb counts only when it sits at the HEAD of a title clause: directly after the bold row number (`**349 WITHDRAWN`), or directly after an em dash (`— RULED`). It must be followed by a non-word, non-`-`, non-`.` character or the end of the cell. Matched case-insensitively.
- **Choice among head verbs:** if any upper-case head verb is RULED → RULED; else the first upper-case head verb. If the only head verbs are not upper-case (`— Ruled:`) → **not counted**, listed in the not-counted line with `(case)`.
- **Fallback only:** a title-form stamp is used only when the row carries **no valid inline stamp of the same verb at ANY date** (residue 1 and 2). Inline wins.
- **Inline `STAMP` hardened:** the verb may not be preceded by `-`, `_`, `/` or `.`, or by `NOT `, and may not be followed by `.`+letter or `-`+letter (filename and slug forms).
- The render's not-counted label is reworded to cover both reasons (no ISO date in cell 2; non-upper-case head verb).
- `selftest` restores the global `WQ` in a `try/finally` (inherited residue 6, partial; the rest of 6 stays declared).

## 3. Acceptance conditions (each a fixture; watched failing on v1.2 where v1.2 is wrong, passing on v1.3)
| # | Fixture (window) | Must | v1.2 today |
|---|---|---|---|
| C1 | `| **224 X — RULED: APPROVE** | 2026-09-30 (needed-by) | **RULED 2026-09-17 …** |` (9/26–10/02) | NOT counted (inline 9/17 is out of window; title ignored) | counts 9/30 ✗ |
| C1b | same row, window 9/11–9/17 | counted once, at 09-17 | 09-17 ✓ |
| C2 | `| **230 Y — RULED: no** | 2026-09-22 (Will 20:51 ET) | Deck tap RULED 2026-09-23 00:51Z |` (9/19–9/25) | counted ONCE, at 09-23 | twice ✗ |
| C3 | titles `— NOT RULED`, `— proposal x-RULED.md drafted`, `— ALREADY RULED 8/13` (each with an ISO cell 2 in window) | none counted | counts ✗ |
| C3b | row-287 shape: title `— RULED:` cell 2 2026-09-26, inline `` `…-RULED.md`. **+2026-10-01 `` | counted once, at 09-26 | twice ✗ |
| C4 | `| **400 W — CORRECTED letter — RULED: APPROVED** | 2026-09-28 |` | RULED 09-28, not CORRECTED | CORRECTED ✗ |
| C4b | row-349 shape: `**349 WITHDRAWN — a duplicate …, which you RULED NOT NOW on 9/30**` cell 2 2026-09-30 | WITHDRAWN (col 4), never RULED | ✓ (must stay) |
| C5 | `| **401 V — Ruled: APPROVED** | 2026-09-28 |` | not counted; in the not-counted list as `(case)` | dropped silently ✗ |
| C6 | v1.2 fixtures A1–A7 | all still pass (17/17 → 17 + new) | ✓ |
| C7 | LIVE diff on the frozen snapshot, 10/02 window | RULED 33 → **31** (235 out; 287's 10/01 out); every other row identical; any other change = STOP and explain | — |
| C8 | `selftest` | global `WQ` restored even if a check raises | no ✗ |

**Neighbours:** ordinary (a title-only row like 356 stays counted) · overlap (both forms on the same date: A3) · missing (no ISO cell 2: A6, undated) · wrong owner (n/a: one file, one owner) · concurrent (PROME edits the queue mid-session: the diff uses the frozen snapshot, never the live file).

## 4. Plan read (independent Opus reader, before the edit; full report kept in the session scratchpad, findings carried here)
**Verdict: the prediction holds (only 235 and 287 change in the 10/02 window: 33 → 31; 9/19–9/25 identical, 24/6/0), but the design failed C1 and C2.**
| # | Finding | Disposition |
|---|---|---|
| ❌ F1 | `STAMP`'s `[^0-9\n]{0,14}` gap crosses the `|` cell boundary, so a short title tail plus a cell-2 date forms a fake INLINE stamp that bypasses both the head rule and the fallback. C1 (`: APPROVE** | ` = 14 chars) and C2 fail. It fires on snapshot rows 255 · 336 · 340 · 343, harmlessly today (the head verb has the same date). | **ADOPTED:** gap = `[^0-9\n|]{0,14}`. The reader verified C1/C2 pass and the snapshot diff is unchanged. |
| ⚠️ | Head-rule drops (en dash · hyphen · colon · `(` · `— **RULED**`) are SILENT: the silent-zero shape v1.2 was built to remove. | **ADOPTED:** upper-case verbs at non-head title positions are listed in the not-counted line as `(non-head)`. The snapshot shows only 235 and 349, both correct exclusions. |
| ⚠️ | Title lookahead bans a bare `.`, so `— WITHDRAWN.` is dropped, while the inline rule bans only `.`+letter. | **ADOPTED:** one rule for both: reject `.`/`-`/`_` followed by a letter. |
| ⚠️ | The `NOT ` lookbehind is upper-case only; `/` in the lookbehind would drop a real `APPROVED/RULED 2026-…`. | **ADOPTED:** lookbehind rejects `NOT ` · `not ` · `NEVER ` · `never `; `/` removed (filenames are caught by `-`). |
| ⚠️ | Not-counted tuple shape: a 4th field breaks the unpacking at :483 and :654. | **ADOPTED:** stays `(n, ln, kind)`; the reason rides in `kind` (`RULED (case)`, `RULED (non-head)`). |
| ⚠️ | Fallback suppresses a genuine in-window title ruling when the notes carry an older same-verb stamp (a re-ruling) or cite another row's ruling. 0 snapshot rows. | **DECLARED residue R7.** This is the cost of fixing C1; the inline stamp is the stronger evidence. |
| ⚠️ | About 20 rows carry a Will decision whose title verb is outside the counted set (`APPROVED`, `OPTION E`, `DEFERRED`). | **Out of scope (v1 definition A4).** The render's query text already says it counts by verb; declared R8. |
## 5. What changed (`scripts/scorecard.py` v1.2 → v1.3)
- `STAMP` (inline): the gap is `[^0-9\n|]{0,14}` (never crosses a cell); lookbehinds reject `-` `_` `.` and `NOT `/`not `/`NEVER `/`never `; a lookahead `NOT_PART` rejects `.`/`-`/`_` followed by a letter (filenames, slugs).
- `title_form_stamp(text, notes)`: only HEAD-position verbs (after `**N ` or `— `), matched case-insensitively; RULED preferred among upper-case head verbs; non-upper-case head verbs (`(case)`) and upper-case non-head verbs (`(non-head)`) are appended to the not-counted list. The tuple stays `(n, ln, kind)`.
- `col5_rulings`: title form used only when the row carries no inline stamp of the same verb at ANY date.
- Render col-5 query text and the not-counted label describe the v1.3 rule (result-read R1).
- `selftest`: v1.2 A1–A7 kept; v1.3 C1–C5, C3b, C4b, plus one isolated fixture per inline guard (result-read R2); the title-form block runs inside `try/finally` restoring `WQ`.

## 6. Completion — four states, never merged
| state | evidence |
|---|---|
| **IMPLEMENTED** | the diff above; `py_compile` clean (not evidence it works, only that it parses) |
| **TESTED** | `--selftest` **27/27**. The same C-fixtures run on the pre-edit v1.2 copy **fail** C1 · C2 · C3 · C3b · C4 · C5 (watched). **Mutation:** removing each new guard in turn turns the selftest red (`NOT` lookbehind 1/27 · `-_.` lookbehind 1/27 · `NOT_PART` 1/27 · `|` gap 2/27). **C7 live (frozen snapshot md5 `626171b2…`):** 10/02 window RULED **33 → 31**; only 235 (9/26) and 287's fake 10/01 drop; not-counted lists 349 and 235 `(non-head)`, both correct; 9/19–9/25 identical at 24/6/0. Re-run unchanged after the result-read edits. |
| **INDEPENDENTLY VERIFIED** | **PASS-WITH-RESIDUE, 0 ❌** (same Opus reader, plan read then result read, its own probes and mutations). R1 (stale text), R2 (three untested guards) and R3 (a C8 check that could not fail; removed) were fixed after the read. **These three fixes are covered by the selftest and mutation run above, not re-read.** |
| **CONSUMED** | NOT YET. The 10/02 render (#6) is the consumer, and it **cannot run** until PROME repairs `PROME/state/ORCH_LOG.tsv` L417–L455 (15 rows dated 9/27, 30 schema-v2 problems, committed since `2674818ff` and on origin). Packeted to PROME. |

**C8** (`WQ` restored if a check raises) is verified by reading the code (both readers), not by a fixture.

## 7. Declared residue
- **R4** (result read): `NOT YET RULED 2026-…` and `NOT BEEN RULED` still count (the negation guard is one-word adjacent). 0 rows in the snapshot.
- **R7** (plan read): the inline-first fallback suppresses a genuine in-window title ruling when the notes carry an older same-verb stamp (a re-ruling) or cite another row's ruling. 0 rows in the snapshot; this is the cost of fixing C1.
- **R8** (plan read): column 5 counts by VERB; about 20 rows carry a Will decision whose title verb is `APPROVED` / `OPTION E` / `DEFERRED`. This is the v1 definition (A4), now stated in the render's query text.
- **Inherited residue 6** (9/25) stands: roll-off undercounts a re-render after about 7 days; DONE counts table-move stamps; DECLINED excluded by definition.
- A synthetic `ET.RULED 2026-…` (no space after a period) is dropped by the `.` lookbehind. 0 rows; all 31 such adjacencies in the snapshot are filenames.
