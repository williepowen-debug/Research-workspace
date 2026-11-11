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

## FINAL, as executed (2026-11-11 11:34 ET)

- Archive title line: `# ACTIVE_DECISIONS rotation — 2026-11-11 (\`prome-2b\`, mid-session housekeeping on Will's word 11:29 ET, 2026-11-11 11:34 ET)`.
- Stamp text moved to section ③: 310 B, crc32 3036261603 (the sentence beginning `Prior: 2026-10-30 19:1x ET` and the pointer sentence after it).
- Measured at the move: the index diff is four changed lines (the stamp line replaced, two rows deleted); digest and size by `python3 PROME/tools/active_decisions_digest.py`.

## Residue (filled after each read)

**Plan read, 2026-11-11 11:34 ET: Sonnet cold reader, SCORE 8 of 12 ok · ⚠️ 4 · ❌ 0; measurements reproduced. Episode read count: 1.** Ledger: the session scratchpad file `coldread_plan_ad.md`. Residue, declared, none fixed in the drafts above:

- ⚠️ 3a: the Measurements table says R1's "Next" cell reads "none; L613 RESOLVED; rotate at the next rotation". In the row that text is the BACKSTOP cell; R1's State cell still leads with `WILL_APPROVED`, a non-terminal token, which is why the digest classed a finished row ACTIONABLE. The row's own later text (EXECUTED 2026-11-05; the gate RESOLVED) is what makes it finished. The mislabel is the plan's; the move is unaffected.
- ⚠️ 5a: the new stamp mentions the intake-lane alert wording correction. That edit was already committed earlier the same day (0e5a42e19c); this rotation makes no second edit to that row.
- ⚠️ 6a: the archive title line and the stamp crc32 were not in the draft; they are in FINAL above.
- ⚠️ 7a: invariant 5 names no command. Checked at the move with `grep -rn` over `PROME/SCRATCH.md`, `PROME/STATUS.md`, `PROME/BOOT.md` and `HEARTBEAT.md` for the two row titles and their WQ numbers pointing into the index: no hit.
- The plan was written against HEAD 5f8f7790a1; the index did not change between that commit and the move.

**Result read, 2026-11-11 11:36 ET: Sonnet cold reader on commit 3a782b8689, SCORE 6 of 7 ok · ⚠️ 1 · ❌ 0. Episode read count: 2, the episode's last.** Both rows and the stamp text reproduce bytes and crc32 from the pre-change file; every other index line is unchanged; the digest returns rc 0 with nine rows and 0 ACTIONABLE. Ledger: the session scratchpad file `coldread_result_ad.md`. No edit to the index or the archive after this read. Residue, declared:

- ⚠️ The reader's pointer search covered four files. PROME widened it after the read, as a check and not an edit: `grep` over `PROME/DOCKET.tsv` and `PROME/GATES.tsv` for a row that cites `ACTIVE_DECISIONS` together with WQ-386, VLO, WQ-428, WQ-429 or either TERRY card name returned nothing; the two TERRY setup files that mention the index are other cards (the TLT WQ-339 card and a VIOLET call-spread card). No live pointer to either moved row was found.

**State: IMPLEMENTED · TESTED (author's mechanical checks) · INDEPENDENTLY VERIFIED at 3a782b8689 (result read ❌ 0).**
