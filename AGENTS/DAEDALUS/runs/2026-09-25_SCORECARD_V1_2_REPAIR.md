# scorecard.py v1.1 → v1.2 — WILL_QUEUE title-form stamps (col 5 / col 4 input)

**Opened:** 2026-09-25 12:3x ET (DAEDALUS, prome-2e spawn, L290 render). **Status:** see §4 (four states, never merged).

## 1. Defect (found at the render, before delivery)
The 9/25 render printed `rulings=1` (9/18: 14). `PROME/WILL_QUEUE.md`'s RECENTLY-DONE table now carries a ruling in a
new form: the verb is in the TITLE cell and the date is the SECOND cell —
`| **294 SPAWN HANS … — RULED: APPROVED with PROME's rec** | 2026-09-25 (Will in-session 11:20 ET, prome-2e) | …`.
`STAMP` requires the date within 14 non-digit chars of the verb, so every title-form row is invisible. PAT-162 /
`finding_scan_keyed_on_naming_reads_local_form_as_absence`: a correct record the instrument cannot parse counts as zero,
and col 7 (`decision_yield` = loops ÷ rulings) printed 26.00 on it.

## 2. Acceptance conditions (written BEFORE the edit — in the defect's terms, not the symptom's)
- **A1** A WQ row whose TITLE cell (cell 1) carries a stamp verb and whose SECOND cell begins `YYYY-MM-DD` yields ONE stamp of that verb at that date.
- **A2** Every inline-form stamp v1.1 found is still found, unchanged (no regression on the old table).
- **A3** A row carrying BOTH forms for the same verb+date counts ONCE (rows and stamps are the printed units).
- **A4** Title verbs outside the v1 set (DECLINED · OVERTAKEN · MOOT · CLOSED · REGISTERED) are NOT counted as RULED — the column's definition does not widen with the repair.
- **A5** An open row (`| 295 | ⚖️ … |`: number in its own cell) is never read as title-form, whatever its prose says.
- **A6** A title-form verb whose second cell is NOT an ISO date (`| **194 … WITHDRAWN** | 9/7 |`) is printed as UNDATED — visible, never silently zero and never guessed.
- **A7** Out-of-window second-cell dates are excluded exactly like inline stamps.

Neighbour categories (WQ-229, considered): ordinary = A1 · overlap = A3 · wrong owner = A4/A5 · missing information = A6 ·
concurrent activity = N/A for code; WILL_QUEUE.md was dirty (PROME live) at read — recorded in the render addendum, not the parser.

## 3. What changed
`scripts/scorecard.py`: `title_form_stamp()` (bold title cell verb + ISO-leading second cell); `col5_rulings(start, end, undated)` merges it (skipped when the same verb+date is inline); col-5 query text states the v1.2 form and prints the UNDATED list; selftest (f) = four fixtures over A1–A7; `VERSION` → v1.2.

## 4. Completion — four states, never merged
- **IMPLEMENTED:** yes (this session, uncommitted until the L290 commit).
- **TESTED:** `--selftest` 17/17. Fire case watched: with `title_form_stamp` stubbed to v1.1 behaviour, 2 of the 4 new checks FAIL (A1 bundle, A6). One fixture defect found and fixed before the read: the open-row fixture planted `RULED: pending | 2026-09-25`, which the INLINE regex (v1.1, unchanged) already matches at ≤14 chars — a fixture error, not a repair error.
- **INDEPENDENTLY VERIFIED:** Opus reader, fresh context, own counterexamples (ten synthetic rows) + every live in-window row checked at its text. **PASS-WITH-RESIDUE, zero ❌.** Live window 9/19→9/25: 28 RULED stamps on 28 rows (v1.1: 1); v1.1 ⊆ v1.2 on 9/05–9/11 (34/2/0 both), 9/12–9/18 (14/1/1 both), 9/19–9/25 (adds 27 RULED + DONE 265).
- **STILL UNRESOLVED:** §5.

## 5. Declared residue (read budget: ❌ fixed only; every ⚠️ declared here — 2026-09-25 12:3x ET, DAEDALUS)
None fires on the live file at 12:28 ET; each is a row SHAPE the queue could carry.
1. **Mis-date when cell 2 is not the ruling date** (row-224 shape: cell 2 = a needed-by date, inline `RULED 2026-09-17` the real one): a title `RULED` would count at the cell-2 date. Fix: title form only as a FALLBACK when the row carries no inline stamp of the same verb at ANY date.
2. **Double count across a midnight-UTC Deck tap** (title date ET 9/22 + inline `RULED 2026-09-23 00:51Z`). Same fix as 1.
3. **Negated verb / proposal filename in the title** (`NOT RULED`, `…-RULED.md drafted`) counts as RULED — the 14-char date gap was acting as a guard the title path lacks. Fix: require `— RULED` + `:`/space/`**`, reject a preceding `NOT` and `-RULED.`.
4. **First verb wins** loses a ruling when another verb precedes it in the title (`CORRECTED letter, then RULED`). Fix: prefer RULED anywhere in the title.
5. **Mixed-case `Ruled:`** is dropped silently (not counted, not UNDATED). Fix: case-insensitive match, route to UNDATED.
6. **Inherited from v1.1:** DONE counts table-move stamps ("Moved OPEN→DONE … by prome-68"); `wq_rows()` reads only the live file, so a re-render after roll-off (~7d) under-counts — the 9/18 col-4 re-read (6 → 4) is this in action; selftest swaps global `WQ` without `try/finally`; DECLINED is excluded by the v1 definition (277 not counted) — intended, now written down.
**Next touch:** fixes 1–5 in one pass with their own fixtures before the 10/02 render, and a plan read before the edit (a second correction to this file this session would trip the two-correction stop — not attempted today).
