# CATALYSTS_FIRED_2026-09.tsv: README

**Archived 2026-09-29 (Will's session, at PROME prome-82's request).** These are the 18 past-dated rows moved **verbatim** out of `docket/CATALYSTS.tsv`, with the same 8-column header. The TSV has no banner so that it still parses; this file holds the banner.

⛔ **This is history. Never cite a row here as current.** Each row carries its own disposition in `notes` (FIRED / SWEPT / MISSED / GRADED / SUPERSEDED), and the prune asserted that before it moved anything.

**Why the rows moved (the convention changed today):**
- PROME's boot summons check (`PROME/tools/prome_gate.py` `check_desk_catalyst_summons`, `SUMMONS_LEDGERS`) flags **every past-dated row still present** as `PAST-DUE — ungraded?`. It does not read status markers.
- It prints only the four oldest flags, so 18 swept rows were burying the forward rows that summon this desk.
- **New convention:** mark a fired row, sweep it, then MOVE it here verbatim at the next closeout. Never delete one.

**Archived by ROW, not by status.** Each row was read for forward commitments first:
- 9/30, 10/05, 10/19, 11/10 and the `mag7.py` Fridays were already live rows.
- **TSMC's September 6-K had no live row.** One was added to the register (estimated 2026-10-09).
- The **8/28 DAEDALUS row's three residuals** went to `STATUS.md` OPEN ④.
- The **9/15 GATE-LIQ-069 row** was annotated as SUPERSEDED by the 9/26 two-of-two fire before it moved.

crc32 of the TSV: `0xed0ccdc9` (computed by the command, not typed). Conservation: 18 archived + 29 live = 47 = 46 before the prune + 1 TSMC row added.
