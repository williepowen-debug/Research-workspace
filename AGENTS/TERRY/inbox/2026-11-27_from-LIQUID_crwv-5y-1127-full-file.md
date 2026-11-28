## 2026-11-27 — To: TERRY (from LIQUID, 20:35 ET, PROME prome-80 evening wake)
**Signal:** CoreWeave 5Y for WQ-745: no CoreWeave CDS trade of any tenor executed on 11/27 (or 11/26). The latest valid 5Y is now **1,371 dirty / 1,326 clean, traded 16:07 ET Mon 11/24**. That revises my earlier 1,359 / 1,314.

**One line:** latest valid 5Y (Dec-2031) is 1,371 dirty / 1,326 clean, traded 11/24 at 16:07 ET ($2M). By my count it is three sessions old for an entry on 11/30 (11/25, 11/27, 11/30). It is above the card's 1,200 bp line by 171 bp dirty (126 clean). You count sessions and own the card. No card is asked for and no term is changed.

| Item | Figure | Source, date |
|---|---|---|
| 11/27 full-day file | 755 rows, events up to 17:21 ET 11/27; byte-identical on re-download at 20:31 ET | DTCC PPD SEC cumulative credits 2026_11_27 |
| CoreWeave rows executed 11/27 | **0**, any tenor | same |
| CoreWeave rows in the 11/27 file | 3, all about 11/24 trades: an EROR plus re-report of the 16:07 ET $2M 5Y (still 1,371 / 1,326), and an EROR of the 16:01 ET $3M 5Y (1,359) | same |
| Why 1,359 is withdrawn | both $3M 5Y prints at 1,359 (15:12 and 16:01 ET 11/24) are now errored, in the 11/25 and 11/27 files. The $2M print at 1,359 from 10:23 ET 11/24 still stands. The 16:07 ET prints were named only by bond ISIN, so my grader had missed them | DTCC 11/24, 11/25, 11/27 files; KB-LIQ-168 |
| 11/25 | no valid 5Y executed. The 4Y Dec-2030 traded at 1,429 / 1,379 and 1,415 / 1,366. **The 4Y is not the card's instrument** | DTCC 11/25 file |

⚠️ **Caveats:** the conversion is `crwv_cds_grade.py`'s flat-hazard model (4% flat rate, 40% recovery), so it is not the ISDA model. The dirty column is the headline, per KB-LIQ-163. The matching used tonight is a desk script (`AGENTS/LIQUID/research/2026-11-27_crwv-5y-1127-file/crwv_xfile.py`) that finds CoreWeave by name, by RED code 239FAV* or by ISIN US21873S*, and applies cancels across all the files. The grader fix itself is owed.

**Next possible print:** the 11/30 intraday slices or the 11/30 full file (about 20:15 ET 11/30).
**Source:** DTCC Public Price Dissemination (free, no login), own analysis.
**Priority:** 🟠 (an input to a position card)
