# 11/9 due-row wake — preparation for 11/10 (stamp 2026-11-09T12:14:46-05:00)

Owner NEXUS. Bounded prep under PROME's packet (Will 12:07 ET). Nothing here grades a row; grades happen at the first session on/after each resolver.

| Row | Resolver | Prepared | Grade rule (frozen; quoted from PREDICTIONS_MONITOR) |
|---|---|---|---|
| GATE-NEXUS-T12S-DFII10 / L13 | FRED DFII10 cell 15 (obs 11/6), unpublished 12:10 ET 11/9 | Cells 1–14 pulled 12:10 ET: 2.80 2.77 2.76 2.64 2.66 2.66 2.64 2.67 2.63 2.60 2.62 2.65 2.64 2.60 vs L2 2.74 [10/16]; edges 2.84 / 2.64; DOWN run 2, UP 0 | Cell 15 can bring DOWN to at most 3 of 5 ⇒ C#2 certain, EXHAUSTED at publication; split line "currently un-falsifiable"; no third window without Will |
| DOCKET L572 PRED-38 | Q3 bank releases and 10-Qs | 10/31 sweep k = 0 across 27 banks; 19 of 21 pending 10-Qs filed by 12:20 ET 11/9 (WBS, SNV not); read-only Opus helper pre-sweeping them to scratchpad | k ≥ 2 HIT · k = 1 NO-VERDICT (closes) · k = 0 MISS; NCO only, NBFI-attributed in the bank's words, ≥ $100.0M per bank |
| DOCKET L575 PRED-41 | NY Fed HHDC Q3-26, 11/10 11:00 ET | `pred41_lookup.py` here; tested on the Q2 workbook: sheet "Page 14 Data", CC column, 25:Q4 7.13 · 26:Q1 7.10 · 26:Q2 6.97, matches the letter | ≥ 7.47 HIT · ≤ 6.47 MISS · strictly inside ⇒ no crossing on this print; Q4-26 (≈Feb) decides; neither crosses ⇒ NO-VERDICT, non-renewable. Register the Q4 wake row when L575 resolves |
| DOCKET L554 | weekly wake 11/10 | M-01 and M-05 closed NEITHER on 11/5 (hold EARNED once, letters 10/8 line 9) | Owed: a successor window or withdrawal for each. A successor's second "neither" withdraws the number. Working view (not decided): withdraw both to "judgment, no number" unless a successor instrument would add information the fired L16 (HY) and the KRE read do not already carry — decided at L554 after the brief read |

Run tomorrow: `.venv/bin/python -I AGENTS/NEXUS/research/2026-11-09_due-rows/pred41_lookup.py 2026Q3 <scratch dir>` from repo root after 11:00 ET.
