# PLAN — closeout rotation bundle, 2026-10-03 PM (`prome-ed` post-`/clear` sitting)

**Rule:** READ_CAP rule 5 — rotate verbatim until under 70% of the 32,550 B budget (22,785 B). Every cut is archived byte-exact with a block crc32; the new text carries every still-live obligation or names the row that does. Sizes = `PROME/tools/measure.py` after apply, never this file.

## HANDOFF — 28834 B → rotate three entries (October 2 — `prome-96` (DESKTOP, Fri 11:39 → 16:45 ET; St · October 1 night — `prome-e4` (DESKTOP, Thu 20:37 → 23:15  · October 1 evening — `prome-2f` (DESKTOP, Thu 15:35 → 20:1; 16285 B) + the 2091 B header paragraph → `PROME/archive/HANDOFF_ROTATED_2026-10-03_prome-ed-pm.md`; add this sitting's entry; header paragraph → one sentence + `ls PROME/archive/HANDOFF_ROTATED_*`.
NEW header sentence:
> <<HANDOFF_HEADER_SENTENCE>>

NEW entry:
> <<HANDOFF_ENTRY>>

## WILL_QUEUE — 210150 B → 31 RECENTLY DONE rows done before 2026-09-26 (26235 B) → `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md`; a one-line roll-off summary appended to § RECENTLY DONE. OPEN untouched.

## STATUS — 30650 B → L2 stamp (8458 B) and the WQ-299 row's state cell (2437 B) → `PROME/archive/STATUS_HISTORY.md` § 2026-10-03; replaced by this sitting's stamp and the current statement.
NEW stamp:
> <<STATUS_STAMP>>

NEW WQ-299 state:
> <<STATUS_WQ299_CURRENT>>

## ACTIVE_DECISIONS — 26106 B → TERRY Next-cell tail (1648 B) + DEWEY row (1245 B, made terminal SUPERSEDED by WQ-300) + prior stamp (1514 B) → `PROME/archive/ACTIVE_DECISIONS_ROTATION_2026-10-03.md`.
NEW DEWEY row:
> | **DEWEY deep-research batch 2 + entitlements + batch 3** | `SUPERSEDED 2026-10-03` — entitlements settled by WQ-300 (Will 2026-09-26: free-tier rating actions APPROVED, paid lines DECLINED); the batch-3 drain lives on DEWEY's DOCKET rows; row verbatim → `PROME/archive/ACTIVE_DECISIONS_ROTATION_2026-10-03.md` | DEWEY (its DOCKET rows) | none here | — | the archive + `PROME/WILL_QUEUE.md` RECENTLY DONE row 300 |

NEW stamp:
> <<AD_STAMP>>

## SCRATCH — 26854 B → the whole ★ NEXT block (9081 B) + the stamp line → `PROME/archive/SCRATCH_ROTATED_2026-10-03_prome-ed-pm.md`; rewritten as this sitting's resume (DOCKET-VIEW and Pending-Will blocks untouched — generated).
NEW ★ NEXT:
> <<SCRATCH_NEXT>>

## Projected sizes after apply (plan-time arithmetic; cite `measure.py` after apply)
- `PROME/HANDOFF.md`: 10504 B
- `PROME/STATUS.md`: 19796 B
- `PROME/ACTIVE_DECISIONS.md`: 22286 B
- `PROME/SCRATCH.md`: 16194 B
- `PROME/WILL_QUEUE.md`: 184080 B (not cap-bearing; the roll-off is W5 hygiene)

## Invariants the reads check
1. Every archived block equals the bytes that left the live file (crc recomputes).
2. No live obligation lost: each owed item in the rotated SCRATCH/HANDOFF text is carried, named by a DOCKET/WQ/GATES row, or stated done with its evidence.
3. The TERRY row's standing guards are byte-identical; the DEWEY row's terminal state names its authority (WQ-300).
4. New statements are true at their sources; no figure a reader can recompute is restated as current; every clock came from `date`.
5. A stranger can resume from the new SCRATCH alone.
