# VIOLET -> PROME: housekeeping on Will's word, delivered

**Date:** 2026-11-25, 20:22 ET. Will typed it in the VIOLET session at 20:13 ET ("Can we do housekeeping now"). This is direct operator work, not a DOCKET row. No figure or view changed.

- **`vix_options.py` OI-zero defect fixed:** after-hours artifact rows now write the OI leg blank, so the upsert keeps good stored OI. Verified on a live after-hours run; 52 test checks are green.
- **MEMORY.md read cap:** 79% of budget before, 69% after (22,449 B). The moved text went verbatim to `archive/MEMORY_DATA_CAVEATS_COLD.md`, with pointers left behind.
- **KB:** 9 rows past Stale_By reviewed. 6 STALE, 1 CONFIRMED, and 2 kept ACTIVE: 386 (Japan vol import, new member 11/25) and 399 (cited by the 11/26 catalyst row).
- **Retirement:** 2 of 36 research items over 60 days old were moved to `archive/`; the other 34 are still cited by live docs.

## COMPLETION — VIOLET — 2026-11-25
STATUS: COMPLETE
CHANGED: scripts/vix_options.py, MEMORY.md, archive/MEMORY_DATA_CAVEATS_COLD.md, KB.tsv, STATUS, SCRATCH, MAINTENANCE, 2 files to archive/
RESULT: MEMORY.md 79% to 69% of read budget; 9 overdue KB rows dispositioned; OI-zero defect fixed
GAPS: 34 old research items kept because live docs cite them; KB.tsv's mixed CRLF and LF endings predate today and were left as found
WILL_NEEDS: none
FOLLOW-UP: KB-VIO-399 closes after the 11/26 catalyst; 11/27 Cboe confirmation
