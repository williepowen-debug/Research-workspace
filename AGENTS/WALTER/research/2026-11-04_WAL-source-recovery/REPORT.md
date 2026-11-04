# WAL Q3 original-source recovery — NOT RECOVERED

Closed 2026-11-04T21:01:22.576061+00:00. This was Will's single bounded retained-source recovery attempt. No complete original was recovered in the searched local locations or reachable Git history. This does not establish absence on other machines or backups.

## Original provenance

WALTER's existing retrieval.json records FFIEC RetrieveFacsimile, SDF, Western Alliance Bank RSSD 3138146, report date 20260930, retrieved 2026-11-01T02:18:33.515051+00:00 (October 31 ET), 1,792 data rows. Expected SHA-256: `2e04cc7bf1a78e525a68059c358215c8ce9e3c24c3639d84ea74ccb8d69c60a4`.

Recorded location: `/tmp/walter-call-report-availability-6guvqyx_/WAL_20260930.sdf`. That file is absent. The comparison script explicitly depended on this temporary September file; it did not write a durable complete September copy. Its description of raw files as retained outside git did not provide durable preservation.

## Search and limits

Checked the exact path, WALTER retrieval/script/verification records, WAL's November 2 preservation review and source directory, and filename inventories including ignored files under Research-workspace, Research-Intake, /tmp, /var/tmp, Downloads and the local .cache directory where present. Hashed 40 source-file candidates and 11 reachable historical WAL source versions against the original receipt; none matched. Complete candidate/path/hash and scan records are in recovery.json. Historical candidates include other reporting periods; they are not substitutes for Q3.

System-owned private temporary directories denied access, recorded in recovery.json. No remote-machine search, deleted-file forensics, credential inspection, API retry or new retrieval was attempted. No complete document was fabricated from selected rows, and the cohort comparison was not rerun. No original source bytes are claimed preserved by this attempt.

## Selected evidence that remains for WAL

All paths below are under `AGENTS/WALTER/research/2026-10-31_call-report-read/`:

- `retrieval.json`: original provenance receipt, WAL/report_date 20260930 entry.
- `selected-primary-rows.tsv`: 27 WAL September rows; filter bank=WAL and period=20260930. Includes RCON2746 and RCONJ454 alongside balance-sheet, credit, earnings and capital fields.
- `bridge-primary-rows.tsv`: 21 WAL September rows, including equity-bridge and NDFI-category selections. Same bank/period filter. The two extracts contain 45 distinct MDRM codes combined, not 1,792 rows.
- `comparison.json` and `equity-bridges.json`: derived calculations. `REPORT.md` and `VERIFY-BASIS.md`: WALTER's interpretation/verification narrative, not the original or WAL's independent extraction.

**RCON1766 is absent from both surviving Q3 extracts.** They cannot supply WAL's MI3 denominator or complete its independent full-document extraction. Missing is not zero; WAL's domain judgment and existing retrieval assignment remain with WAL. The copies of selected rows inside recovery.json are explicitly labeled remaining selected evidence, not a reconstruction.

## Disposition and delivery

Recovery attempt CLOSED — NOT RECOVERED. No further recovery work commissioned. Create-only administrative notice to WAL: `AGENTS/WAL/inbox/2026-11-04_from-WALTER_Q3-original-not-recovered.md`. This is a source-custody result, not a new market signal, grade, or duplicate BOARD dispatch. Publication and owner consumption must be proved separately.
