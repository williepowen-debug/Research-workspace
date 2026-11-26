# LIQUID -> PROME: D:L1290 Part B. No valid CoreWeave 5Y trade on 11/25; the same 4Y contract widened about 130 bp; TERRY's line still reads 1,314 clean [11/24] (2026-11-25)

**ACTION: log Part B of D:L1290 as answered from the full day of DTCC intraday slices; carry to TERRY (WQ-745 card), WALTER (cards 035/036 ask) and SAM (SoftBank). No score, gate or card moves.**

Run early on Will's 18:46 ET word. Basis: DTCC PPD intraday slices 1–631 for 11/25 (reports to 18:44 ET; slice 632 404 at 19:05 ET). The cumulative file was 404 at 18:46 ET; I diff it when it posts (about 20:15 ET) and send a correction only if it changes a figure.

| Name | 11/25 at DTCC (clean / dirty bp) | Last valid 5Y | Read |
|---|---|---|---|
| **CoreWeave** (500 coupon) | **No valid 5Y (SEARCH-NOT-FOUND).** 4Y Dec-2030 **1,379 / 1,429** (08:20 ET, $2M) and **1,366 / 1,415** (12:22 ET, $1M, non-standard flag). Two trades cancelled: 5Y odd lot 1,363 (07:56 ET, slice 306) and 2Y 1,382 (12:29 ET, slice 587) | **1,314 / 1,359 [11/24 15:12 ET]** | Same 4Y contract 1,214–1,239 [11/24] to 1,366–1,379: about **+130 bp in a day**. 5Y INFERRED about 1,440–1,455 clean if the 11/24 4Y–5Y gap (+75) held |
| **SoftBank** (JPY, 100 coupon) | 3.5Y Jun-2030 **548 / 555** (09:32 ET, ¥796M+ capped), as this morning; no other priced trade | 466 / 471 [11/24 Tokyo] | No 11/25 5Y (SEARCH-NOT-FOUND); 5Y INFERRED 560–600 stands, n=1 |
| **Oracle** (100 coupon) | 5Y Dec-2031: 9 live trades **362–372 / 367–377**; high at 10:07 ET, afternoon 362–364, last **364 / 369** (13:32 ET); one 362 cancelled | this day | About flat against 11/24 quotes 365–370 after the morning high |
| **Alphabet** | The one 5Y trade (108 / 112, 14:49 ET) **cancelled** (slice 620) | 96–97 [11/24] | No valid 11/25 5Y |
| **SpaceX** | 5Y **293 / 298** (11:30 ET, capped, non-standard flag) | this day | Flat to +3 dirty against 286–295 [11/24] |

- **For TERRY (GATE-TERRY-CRWV-AIFIN-01, clean basis; terms are TERRY's):** LIQUID's latest CoreWeave 5Y read is **1,314 clean [11/24]**, above 1,200 and far from the 1,000 void. By session count (11/26 no session) it is 2 back for an entry on Fri 11/27 and 3 or more for 11/30 onward unless a 5Y prints 11/27. Whether the 11/27 early close counts is TERRY's reading. The 11/25 4Y and the inferred 5Y point the same way.
- **For WALTER (035/036 ask, Bloomberg-relayed "five-year rose by the most ever", no level):** not confirmable at DTCC, which shows no valid 11/25 5Y. The 4Y +130 bp on 11/25 and the 5Y +190 bp on 11/24 (1,076–1,123 to 1,267–1,314 clean) are each consistent with a record move. Bloomberg's level likely rests on dealer quotes (INFERRED).
- **Withdrawn (my 18:16 ET chat line to Will, not in any file):** "4Y above 5Y means near-term worry" compared 11/25's 4Y with 11/24's 5Y. On 11/24's own trades the curve sloped up (4Y 1,239, 5Y 1,314).
- **Tool defects found and fixed (KB-LIQ-166):** 90 of 114 cancel rows on 11/25 carried no company name, and some trades carry the name only in `UPI Underlier Name`. `crwv_cds_grade.py` filtered by name first, so on the 11/25 data it still listed the cancelled 1,363 odd lot as live (6 prints; fixed: 5). Fixed in place and tested old against new. Morning correction COR-20261125-22 stands. `scripts/dtcc_cds_probe.py` (shared, not mine) is not checked for the same flaw.
- **039 context (WALTER, CoreWeave 10-Q at Sep 30, not re-read by LIQUID):** $2.433B principal due rest of 2026, $10.974B in 2027, against $4.122B cash and $5.7B undrawn. The swap move is consistent with refinancing risk being priced; the cause is not established here and this read does not size it.
- **Limits that travel:** US-reportable sample only; capped sizes; the conversion approximates the ISDA model (script header: 7–8 bp low against ISDA at September levels); the 5Y figure for 11/25 is an inference from two 4Y trades, one flagged.
- **Trade line (WQ-696):** no new investment implication from LIQUID. The live card is TERRY's (WQ-745, NOT-FIRED); its CDS leg is satisfied on the 11/24 read within the count above. Invalidation for the card's CDS leg: a valid 5Y under 1,000 clean.
- Record: `AGENTS/LIQUID/research/2026-11-25_dtcc-full-day/REPORT.md` (reader, output, 46 evidence rows).

## COMPLETION — LIQUID — 2026-11-25
STATUS: ✅ COMPLETE (cumulative-file diff pending, about 20:15 ET)
CHANGED: AGENTS/LIQUID/research/2026-11-25_dtcc-full-day/, AGENTS/LIQUID/scripts/crwv_cds_grade.py, workbook/KB.tsv (KB-LIQ-166), board_log.tsv, inbox/WALTER/processed/ (039, 040), this packet
RESULT: CoreWeave no valid 5Y on 11/25; 4Y 1,366–1,379 clean (+130 bp on the day); last 5Y 1,314 clean [11/24]. SoftBank 3.5Y 548/555, no 5Y. Oracle 5Y 362–372, last 364. Alphabet 5Y cancelled. SpaceX 293/298.
GAPS: cumulative file not yet posted; SoftBank most trading off this report; no dealer quotes reachable.
WILL_NEEDS: None
FOLLOW-UP: diff the cumulative file when posted; closeout after
