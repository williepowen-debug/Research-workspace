# Scorecard v1.4: column 5 reads the done-form ruling, November 16

**Authority:** Will in this DAEDALUS session, 23:23 ET, "ok go ahead". That was in reply to my 23:2x ET list, whose next item was "fix the scorecard so it reads your rulings again before Friday's run". The repair was declared owed in `runs/2026-11-16_SCORECARD_2026-11-13_DELIVERY.md` (own lane, existing tool).

## Defect

WILL_QUEUE's RECENTLY-DONE rows now carry the ruling in the second cell: `| **682 — title** | Done 2026-11-13 11:37 ET — RULED A, … | RULED A — Will in PROME's chat … |`. v1.3 reads two forms only. The first is an inline `RULED YYYY-MM-DD`, with the verb before the date and at most 14 characters between them. The second is the title form, with the verb in the bold title cell and the date leading cell 2. Neither matches, so column 5 read **0** for 11/7–11/13.

## Acceptance conditions (written before the code; selftest section (i))

| ID | Input | Required result |
|---|---|---|
| D1 | `Done 2026-11-13 11:37 ET — RULED A, …` | counted once at 11-13 |
| D1b | `— RULED-ish note` | not counted (slug) |
| D1c | `Done 2026-11-13 — RULED A` (no time) | counted |
| D2 | `— RECEIPT (RULED by class C9 …)` | not counted; listed `RECEIPT (done-form)` |
| D2b | `— MOOT` | not counted; listed |
| D3 | bare `— RULED` and `— RULED (P1 APPROVED)` | counted |
| D4 | done-form at 11-12 plus inline `RULED 2026-11-10` | counted once, at the inline 11-10 (v1.3 inline-first) |
| D5 | title form and done form both RULED | counted once |
| D6 | `— Ruled A` | not counted; listed `Ruled (done-form)` |
| D7 | open row `\| 643 \| …` (no bold title) | never counted |
| D8 | `— closed; RULED later` | not counted (not the head word) |
| D9 | `— WITHDRAWN by PROME` | not counted; column 4 not fed |
| D10 | done-form dated 11-14, window ending 11-13 | outside the window |

## Evidence

| Test | Result |
|---|---|
| `--selftest` | 32/32 (27 earlier + 5 new checks covering D1–D10 and review fixtures R1–R4; the notes check is an EXACT set, not a subset) |
| Mutant 1: done-form match disabled (the v1.3 behaviour) | 3 FAIL |
| Mutant 2: non-RULED head words not listed | 1 FAIL |
| Mutant 3: inline-first precedence removed | 1 FAIL |
| Mutant 4: case-insensitive `RULED` | 3 FAIL |
| Mutant 5: cell 2 not skipped by the inline scan (R1) | 1 FAIL |
| Mutant 6: undated guard for a counted done-form row off (R3) | 1 FAIL |
| Mutant 7: em dash only (R2) | 2 FAIL |
| Mutant 8: a `Done <date>` cell with no head word dropped silently (R2) | 1 FAIL |
| v1.3 vs v1.4, pinned snapshot, three windows (10/27–11/02, 10/31–11/06, 11/07–11/13) | no v1.3 RULED stamp lost; DONE and column-4 lists identical |
| Live, pinned `916e683f5d` WILL_QUEUE, 11/07–11/13 | v1.3 **0** → v1.4 **31** rows / 31 stamps: 645, 650–671, 673, 674, 676–679, 681, 682. This **equals the hand count** in the 11/13 delivery record (35 Done rows with a RULED verb, minus 4 C9 receipts 672, 675, 680, 683; 649 MOOT excluded). |
| Live, same snapshot, 10/31–11/06 | v1.3 7 stamps (4 rows) → v1.4 60 stamps (57 rows, now including 559 at 11-02). The series row for 11/06 says 20 (rendered 11/07 on an earlier snapshot). **That week was undercounted: about 60 stamps against the recorded 20, on different snapshots.** |
| `--week-ending 2026-11-13 --no-write` | rc 0 |

## Review

Independent Opus reader, given the diff, the intended rules and the snapshot, not my count: **ACCEPT-WITH-RESIDUE**. Its own reading of 11/07–11/13 found the same 31 rows, with no row-by-row disagreement. It confirmed v1.3 behaviour unchanged and column 4 never fed. Five findings; four repaired the same session and each guarded by a mutant above:

| # | Finding | Disposition |
|---|---|---|
| R1 | A later date in the SAME cell (`— RULED A (date ON 2026-12-31 …)`, real row 559) became the ruling date through the inline scan | FIXED: the inline scan skips cell 2 on a done-form row; 559 now counts at 11-02 |
| R2 | Hyphen or en dash, more than 24 characters before the dash, bold verb or bold `Done`: silent misses | FIXED: any dash, gap up to 80 characters, bold allowed; a `Done <date>` cell with no head word is listed `NO-HEAD-WORD (done-form)` |
| R3 | A row with a dateless title-form RULED and a done-form RULED was counted AND listed as not counted | FIXED |
| R4 | `— RULED_note` counted | FIXED: the head word runs to the first non-word character |
| R5 | About 30 new notes (`Will (done-form)` and others) | KEPT: listing is the no-silent-drop rule working; the noise is the price |

Not repaired, declared: (a) an inline `RULED YYYY-MM-DD` in ANOTHER cell still wins over the done-form date (v1.3 inline-first, residue R7 of v1.3); (b) the reviewer's `\|` inside a title shifts the cells, as it already did for v1.3; (c) the older comma form `Done …, Will in the PROME window | RULED A` (rows of about 10/22–11/05) is now LISTED `NO-HEAD-WORD`, still not counted.

## Residue, stated

- **Older variants are still unread.** Some rows dated on or before 11/06 put a different word after the dash, with RULED only in cell 3 beyond the 14-character gap. Examples: 560 and 570 (`— Will's word in this chat`), 601 (`— all units RULED`), 623 (`— DEFERRED`). They are listed `(done-form)`, not counted. Every Will ruling in the 11/07–11/13 window is read.
- **The series is not re-rendered.** The 11/06 (20) and 11/13 (0) rows keep their v1.3 values, so each row stays one method; the VERSION column shows the break. The next render (11/20) is the first at v1.4. Comparing column 5 or column 7 across the 11/13 → 11/20 boundary compares methods, not weeks.
- Column 4 is not fed by the done form, by design. A `— WITHDRAWN` done-form row is listed, not counted.

REVIEW: required (an instrument change behind a Will-facing number).
