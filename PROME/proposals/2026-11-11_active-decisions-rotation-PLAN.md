# ACTIVE_DECISIONS rotation, 2026-11-11 — PLAN

**Authority:** the two rows' own text ("rotate at the next rotation"; "terminal; rotate this row out at the next ACTIVE_DECISIONS rotation") and Will in PROME's chat 2026-11-11 11:29 ET, verbatim: "Ok please handle housekeeping now". **Owner:** PROME (`PROME/ACTIVE_DECISIONS.md` is PROME's decision index). **Written:** 2026-11-11 11:32 ET (from `date`) by PROME prome-2b, against HEAD 5f8f7790a1.

**Reads (PROME/CLAUDE.md § Review budget, archival split):** ONE plan read of THIS file by a Sonnet cold reader, fix ❌ only, ⚠️ to the residue block; the move in ONE edit set; ONE result read at the commit; declared residue.

## What moves and why

`PROME/ACTIVE_DECISIONS.md` is the index of live decisions, read by digest at every boot; a row classed ACTIONABLE is read whole before new work. Two rows are finished by their own words and still sit in it, one of them classed ACTIONABLE, so every boot reads a finished decision as if it needed action. They move verbatim to a dated archive file. Nothing about either decision changes.

## Measurements (instrument: Python `len(text.encode())` and `zlib.crc32` over each whole table line including its newline, in `PROME/ACTIVE_DECISIONS.md` at HEAD 5f8f7790a1)

| Unit | The line that begins | Bytes | crc32 | Why it is finished |
|---|---|---|---|---|
| R1 | `| **VLO held-share December basis (WQ-386)**` | 859 | 3474124666 | Its own cells: EXECUTED 2026-11-05, Will sold the original share; `GATE-TERRY-VLO-HELD-01` RESOLVED; Next reads "none; L613 RESOLVED; rotate at the next rotation" |
| R2 | `| **OZK Nov-20 $40P ×4 and WAL Dec-18 $65P ×4 — SELL before their prints (WQ-428 / WQ-429)**` | 1393 | 1584353037 | Its own cells: EXPIRED 2026-10-31, DOCKET L709 RESOLVED; Next reads "none — terminal; rotate this row out at the next ACTIVE_DECISIONS rotation" |

File before: 22387 B. After: 22387 B minus the two lines; the stamp line changes length by the difference between the new stamp and the two sentences it loses.

## Exact edits

1. `PROME/ACTIVE_DECISIONS.md`: delete line R1 and line R2 whole (each a single table line). No other table line changes.
2. `PROME/ACTIVE_DECISIONS.md` line 2 (the `**Updated:**` line) keeps the latest stamp and ONE prior, as it does now. It becomes: `**Updated:** 2026-11-11 (rotation: two finished rows, VLO held-share WQ-386 and the OZK and WAL pre-print sells WQ-428 and WQ-429, moved verbatim to the archive; the intake-lane row's alert wording corrected the same day to the ruled "strictly above 280.0"; no decision, guard or authority changed). Prior: ` followed by the present 2026-11-04 stamp sentence unchanged (from `2026-11-04 12:19 ET (Will-directed bounded repair:` through `no later-phase, gate or trade authority changed).`), followed by ` Prior stamps → \`PROME/archive/ACTIVE_DECISIONS_ROTATION_2026-11-11.md\` ③ and earlier rotation files.` The present second prior (the sentence beginning `Prior: 2026-10-30 19:1x ET` through `no gate or authority change).`) and the present pointer sentence (`Prior stamps → \`PROME/archive/ACTIVE_DECISIONS_ROTATION_2026-10-30.md\` ②.`) leave line 2 and go verbatim into the new archive file's section ③.
3. New file `PROME/archive/ACTIVE_DECISIONS_ROTATION_2026-11-11.md`, in the shape of `PROME/archive/ACTIVE_DECISIONS_ROTATION_2026-10-30.md`: a title line; a pass-manifest line naming both rows with their crc32, the stamp text's crc32 and this plan; `## ① VLO held-share December basis (WQ-386)` with the row between `<!-- ROW BEGIN -->` and `<!-- ROW END -->`; `## ② OZK and WAL pre-print sells (WQ-428 / WQ-429)` the same way; `## ③ Prior \`Updated:\` stamp text` with the two sentences removed from line 2 between `<!-- STAMP BEGIN -->` and `<!-- STAMP END -->`. Each row is byte-identical to its line in the index.

## What is NOT rotated, and one thing a reader should know

- R2 does not contain a "standing guards (never rotate)" clause, and neither row is cited as a live guard by another index row. The standing guards of the earlier TRY-FIRE-004 card stay in their own retained row.
- R2 records that the 10/30 broker capture still showed both put lines held and that a later sale is booked from Will's capture. That is a record, not an obligation of this index: positions are read from `FORGE/STATUS.md`, never from this file, and `USER.md` § No expiry nagging means no reminder is owed. Archiving the row removes no position fact, because the index never owned one.
- R2's backstop cell says RED's tail-hold branch on the OZK card "returns to Will only if HY ≥320 ×3 AND LIQ-07 S1 at the 10/16 read". That condition was tied to a read dated 10/16, which has passed; the row calls itself terminal. The clause moves with the row, verbatim.

## Invariants (the result read checks each)

1. Each of the two lines is absent from `PROME/ACTIVE_DECISIONS.md` and present exactly once in the archive file, byte-identical (bytes and crc32 as the table states).
2. Every other line of the index is byte-identical to its state before the commit; only line 2 (the stamp line) differs otherwise, and the two sentences it lost are in the archive file's section ③ verbatim.
3. `python3 PROME/tools/active_decisions_digest.py` returns rc 0 and reports nine rows, none of them the two moved rows.
4. The archive file names the plan and gives each row's crc32.
5. No live PROME file points at either moved row as living in the index (a pointer to the DOCKET or GATES row is fine).

## Residue (filled after each read)

*(empty before the plan read)*
