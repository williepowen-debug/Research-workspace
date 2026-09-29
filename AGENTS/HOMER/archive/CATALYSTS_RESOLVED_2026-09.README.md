# CATALYSTS_RESOLVED_2026-09.tsv: README

**Archived 2026-09-29 (Will's session; PROME prome-82 asked for it, item #9 of the 9/29 boot sweep).** These are the **20 rows whose date key began `RESOLVED`**, moved **verbatim** out of `docket/CATALYSTS.tsv` with the same 7-column header. The TSV has no banner so it still parses. This README carries the banner.

⛔ **This is history. Never cite a row here as current.** Each row carries its own grade or disposition in `date` and `notes`.

**Why the rows moved:** they were 44.7KB of a 150KB live docket. The boot sweep skipped them (`$1 !~ /^RESOLVED/`), but anyone reading the file whole hit truncation before reaching the forward rows. Same convention VULCAN adopted the same day: mark a row resolved, then move it here verbatim at the next closeout. Never delete one.

**Moved by row, not by status.** Each row was read for forward commitments before it moved:
- **Row "TX CRE foreclosure-auction pipeline"** said `NEXT: September report ~2026-09-01` and **there was no live recurring row.** The September list was found late by the 9/29 news sweep for exactly this reason. **A recurring live row was added.**
- **Row "BEA GDP residential fixed investment" (Q2 second estimate)** was labelled RECURRING but had **no live successor.** **A recurring live row was added** for the Q3 advance estimate.
- **Row "builder NET-EFFECTIVE price gap"** left a residual: re-source the FQ2 buydown-cost figure, and at PHM Q3 / DHI FQ4 check whether either issuer states incentive load as a separate line. **Carried onto the live CRL-23 checkpoint row.**
- **Row "P1 READ-CAP remediation"** carried the **2026-12-02** re-measure of `LESSONS.md` / `STATUS.md`. That date also sits on `LESSONS.md` line 6 (boot-read), but a dated obligation belongs on the docket (LESSONS §20). **A live row was added.**
- Fannie/Freddie July, NAR July, both MBA Q2 NDS rows, HUD ML 2026-08: their `NEXT` pointers were already live rows (GSE monthly, NAR EHS, MBA Q3 NDS, ICE First Look).
- The `(cleared this session)` row from July was an empty placeholder.

**Conservation (checked by command, not asserted):** 57 rows before = 37 live + 20 archived. The sorted union of live + archive rows is byte-identical to the committed file's rows (`diff` clean against `git show HEAD:`). The new rows were added to the live file **after** that check.

crc32 of `CATALYSTS_RESOLVED_2026-09.tsv`: `0x13dc1b4d` (computed by `zlib.crc32` on the file, not typed from memory).
