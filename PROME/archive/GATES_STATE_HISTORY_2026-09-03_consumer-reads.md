# GATES.tsv history — consumer reads + WQ-170 wording + R1 ≤220 trim (2026-09-03 21:5x ET, PROME; cold-read gated after the file's two-correction stop)

*Each section = the VERBATIM prior text of ONE cell (`state` or `last_checked`) of the named gate_id, byte-exact, rotated out when the live cell was replaced; `entry-crc32` = zlib.crc32 over the section body (UTF-8), `bytes` = its UTF-8 length. Recompute to verify — never trust the banner. The live cell carries the suffix `· hist→GATES_STATE_HISTORY` (the family name; `ls PROME/archive/GATES_STATE_HISTORY_*.md` is the index).*

## GATE-LIQ-069 · last_checked — rotated 2026-09-03 21:5x
entry-crc32: 1336532096 · bytes: 93 · rotated 2026-09-03

2026-09-02 21:3x WQ-162 vintage convention appended (Will's word; no level/count/state moved)

## GATE-LIQ-079 · state — rotated 2026-09-03 21:5x
entry-crc32: 2373282251 · bytes: 330 · rotated 2026-09-03

LIVE / NOT ARMED — FIRE legs UNGRADEABLE-until-banded (owner-declared 9/3: series exist, no thresholds; bands + base rate owed as a PROPOSAL by the 10/31 review_by; the ARM leg +30bp is unaffected) · instrument repaired 8/28 (boot.py rendered SOFR99−SOFR; letter SOFR99−IORB was right): +7bp [8/27], 23bp below +30 arm; n=1

## GATE-TERRY-007 · state — rotated 2026-09-03 21:5x
entry-crc32: 3260250924 · bytes: 173 · rotated 2026-09-03

LIVE — 004 TLT Sep-30 77P exit counter 0 of 5; DGS10 4.79 [9/1 official, PROME consumer read 9/2] = window HIGH, 29bp from 4.50; OWNER-graded through 9/1 (TERRY c8c58a363)

## GATE-TERRY-007 · last_checked — rotated 2026-09-03 21:5x
entry-crc32: 4206869072 · bytes: 862 · rotated 2026-09-03

2026-09-03 12:2x OWNER GRADE (TERRY c8c58a363, H.15 + FRED pulled independently at primary): 9/1 official DGS10 4.79 ≥4.50 ⇒ NOT qualifying, counter 0-of-5, 29bp from the line; DFII10 2.44, add-gate 6bp, NO-ADD. EXECUTABILITY (owner arithmetic): DGS10 publishes D+1 ~16:15 ⇒ the last streak that can be observed AND acted on before the 9/30 expiry must BEGIN by Tue 9/22 — after 9/22 the gate is arithmetically dead. Base rate (499 bars 2024-09-03→2026-09-01): 80.2% of closes <4.50, 8 runs ≥5 ⇒ CALIBRATED not structural (8 runs at 80% below is consistent: the 209-close run alone is 42% of the sample; closes are autocorrelated, not i.i.d.); 41 sessions above since 7/06 = a regime shift; 007 is the DISARM gate — NO-VERDICT-BY-EXPIRY = thesis intact, not 'nothing happened'. 9/2 official publishes ~16:15 9/3 = PROME consumer read (TERRY dark)

## GATE-TERRY-ROLL70-EXIT · state — rotated 2026-09-03 21:5x
entry-crc32: 4136573886 · bytes: 133 · rotated 2026-09-03

LIVE — EXIT count 0 of 3; WAL $79.12 [9/2 close] = $2.78 below the line (9/3 12:20 intraday 80.05, TERRY c8c58a363 — not a close)

## GATE-TERRY-ROLL70-EXIT · last_checked — rotated 2026-09-03 21:5x
entry-crc32: 1754013391 · bytes: 235 · rotated 2026-09-03

2026-09-03 12:5x REGISTERED (PROME, step-2 package): count 0-of-3 carried from the REG-T02 / ROLL70 cells through the 9/2 close; REGINALD grades each official close from 9/3 (its NOTES.md §REG-T-02 STATE RULING is the grading surface)

## GATE-BRK-R2 · state — rotated 2026-09-03 21:5x
entry-crc32: 607380371 · bytes: 224 · rotated 2026-09-03

LIVE — (a) BCRED at 2 consecutive (Q2 ~50% · Q3 ~50%); a third sub-100% print FIRES (~mid-Nov); (b) OCIC 23% [Q1-26] is below 25% — BROCK grades at encode whether it fires or is out-of-window; 0 fired pending that grade

## GATE-BRK-R2 · last_checked — rotated 2026-09-03 21:5x
entry-crc32: 4160629268 · bytes: 86 · rotated 2026-09-03

2026-09-03 REGISTERED at ruling; owner grade of (b) vs OCIC 23% OWED at BROCK's encode
