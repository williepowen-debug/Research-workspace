# docket_owed.py + gate step B5 — the DOCKET → DAEDALUS hop (2026-10-01, Will "ok approved go ahead")

## 1. Defect
DOCKET L526 · L538 · L546 · L548 were registered by PROME on 9/28–9/29 with DAEDALUS in the owner cell (three session-keyed `next-DAEDALUS-session`, one dated 10/01). None reached `STATUS.md`. Found by hand at the 10/01 catch-up boot; all four premises re-tested live and all four still reproduce. **Cause:** no DAEDALUS boot step read the DOCKET for rows naming DAEDALUS. The gate read DOCKET only for `claim_check`'s weekday leg. The registrar wrote and no reader was registered (PAT-108 one hop over; PAT-150's sink shape).

## 2. Acceptance conditions (written before the tool; each a selftest fixture)
| # | Must |
|---|---|
| D1 | FIRE: an open row naming DAEDALUS, uncited in STATUS ⇒ rc 1, row listed (session-keyed and past-due both) · D1b a past-due row is marked `(PAST)` |
| D2 | CLEAN: all such rows cited ⇒ rc 0, the clean line prints and says "acknowledged, not done" |
| D3 | a TERMINAL row (fleet definition, `docket_view.state_kind`) is never listed |
| D4 | a row beyond the horizon (30d) is not listed but IS counted |
| D5 | a row whose DAEDALUS owner segment says "informed" is listed separately and does not gate · D5b a row not naming DAEDALUS is never listed |
| D6 | `L2` is not cited by `L22` (digit boundary) |
| D7 | UNKNOWN rc 2 on: zero rows naming DAEDALUS in ANY state (PAT-155) · missing DOCKET · ragged DOCKET (docket_view's own refusal) · unreadable STATUS |

**Neighbours:** ordinary (dated row in window) · overlap (two owners in one cell: segment split on ` / `) · wrong owner (D5b) · missing (D7) · concurrent (PROME appends rows mid-session: the check reads at run time and is re-run at the next boot; no state kept).

## 3. Evidence: watched, not inferred
- `--selftest`: **12/12**, with the fire output (`rc=1 uncited=2 cited=0 informed=1`) and the clean output (`rc=0 … CLEAN`) both printed.
- **Real fire case:** run against `STATUS.md` as of `0d126e4de` (before the catch-up) with as-of 2026-10-01: **rc 1, 25 uncited, and all four hand-found rows (L526 · L538 · L546 · L548) listed.** The tool found 21 more that the hand search had not.
- **Real case the tool caught that I caused:** after the 9/25 header and bottom lines were rotated out of STATUS (blocks AS/AT), B5 went from 0 to **2 uncited: L470 (WQ-236 strict flip) and L487 (dark-days check, due 10/02).** Their only citations had been in the rotated text, so the byte remedy had deleted two duties (PAT-141). Both were re-homed on the live board.
- **Real clean case:** after triage and re-homing, live run: `rc=0 uncited=0 cited=43`.
- Gate: `daedalus_gate.py --selftest` PASS; `daedalus_gate.py boot` shows `⏰ B5 DUE` (pre-triage) with rc map 0 CLEAN · 1 DUE · 2 UNKNOWN; the step list now reads `checked: 4 steps ['B1','B2','B4','B5']`.

## 4. Triage of the 25 (each row's role and state cell read; not blanket-cited)
On `STATUS.md`'s owed list, in three groups: **ACT, dated** (L41 · L309 · L471 → 10/06; L380 · L423 · L459 → 10/07; L499 → 10/09; L188 · L40 → 10/12; L321 → PR#7; L440 → 10/25; plus the four hand-found) · **SEAT ONLY** (L208 · L314 · L334 · L350 · L381 · L386 · L387 · L417 · L550 · L556; act when asked or when the named condition occurs) · **informed-only** (L473 · L504 · L557 · L561 · L562).

## 5. What PASS proves, and what it does not
PASS proves that every open, in-window DOCKET row naming DAEDALUS has its line number written somewhere in STATUS.md. It does **not** prove the row was understood, scheduled sensibly, or done. A citation is acknowledgement. The "informed" discriminator is one word in a prose owner cell (PAT-185 risk), but it only ever moves a row from gating to a printed non-gating list, never out of sight. Rows past the 30-day horizon are counted, not listed.

## 6. Declared residue
- R1: line-number citations go stale if DOCKET rows are ever renumbered. The DOCKET convention forbids that (header: "never insert, delete or reorder rows").
- R2: a row that names DAEDALUS only in the catalyst or notes cell, not the owner cell, is invisible. This is by design: the owner cell is the assignment.
- R3: not independently read. This is an agent-local boot check in my own directory and gates nothing outside it. The fire and clean paths were watched on real cases (§3). An independent read is owed only if it is promoted to the fleet (a `scripts/` twin keyed on any agent name is the obvious generalisation; that is PROME's call, not done).
