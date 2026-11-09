# HHDC Q3 2026 — grade prep for Tue 2026-11-10 11:00 ET (CARL, written 2026-11-09 13:05 ET)

PROME due-row wake, Will's word 12:07 ET. Rows: PROME DOCKET L1017 (CRL-33). Same release also carries the frozen card's §1 shadow grade, CRL-30 first grade, CRL-04 basis note, CARL-AUTO-OUTFLOW-01 re-check. Card of record: `thesis/HHDC_Q3_2026_GRADING_CARD_TEMPLATE.md` (frozen 11/06; addenda only).

## Tomorrow is a lookup

1. 11:00 ET: `curl -A "<generic browser UA>" -o research/2026-11-09_HHDC_prep/raw/HHD_C_Report_2026Q3.xlsx https://www.newyorkfed.org/medialibrary/interactives/householdcredit/data/xls/HHD_C_Report_2026Q3.xlsx` (11/09 13:00 ET the URL returns a 302 redirect, not published; Q1 and Q2 return 200 on the same pattern). Year-trap: confirm the PDF header reads 2026:Q3.
2. From the repo root: `.venv/bin/python3 -I AGENTS/CARL/research/2026-11-09_HHDC_prep/hhdc_lookup.py --prior AGENTS/CARL/research/2026-11-09_HHDC_prep/raw/HHD_C_Report_2026Q2.xlsx --new AGENTS/CARL/research/2026-11-09_HHDC_prep/raw/HHD_C_Report_2026Q3.xlsx --quarter 26:Q3`
3. Copy figures onto the card as a dated addendum; fill §1 both rows before any interpretation.
4. If the script prints `§1 DIVERGENCE`, write it on the card and send it to Will through PROME the same session (Rider 1).

**Script test, 11/09:** run Q1 vintage → Q2 vintage, quarter 26:Q2. It reproduced the Q2 card: AS-WRITTEN 13.12 → 12.92 = decline #1 (prior quarter not a decline); RE-SPEC 7.1293 → 7.10 → 6.97 = −15.9 bp vs 100 bp floor, not met; 0 revisions on Page 14 CC or Page 12 CC. Tie logic exercised (6.97 vs 6.97 = NO-VERDICT). Files: Q1 sha256 ff913fca…cfade9, Q2 sha256 ddfba16b…d99237 (pulled 11/09 from newyorkfed.org).

## Thresholds, written before the print

| Letter | Reads | Q3 outcome rule | Note |
|---|---|---|---|
| CRL-33 (25%) | Page 14 CC 26:Q3, two decimals | > 6.97 YES; < 6.97 NO; = 6.97 NO-VERDICT | No re-grade on later revision |
| CRL-30 (25%) | Page 14 CC | ≥ 7.50 fires; < 6.50 twice running invalidates | Quote same-quarter YoY: 25:Q3 = 7.05 (Q2 vintage) |
| §1 RE-SPEC (live kill leg 2) | Page 14 CC 26:Q1→Q2→Q3 | Both moves down AND cumulative ≥ 100 bp: needs Q3 ≤ 6.10 | Q2 vintage: 26:Q1 7.10, 26:Q2 6.97 |
| §1 AS-WRITTEN (superseded, shadow) | Page 12 CC QoQ | Q3 < Q2 on the Q3 vintage = decline #2 of 2 = leg 2 met | Q2 vintage 26:Q2 12.92 |
| Leg 1 (both) | ICSA < 220K 8+ weeks | Met: 14 straight weeks < 220K, 8/01 to 10/31, latest 189K (FRED pull 11/09 13:00 ET; next print Thu 11/12) | Filters nothing (RED rider 1) |
| CRL-04 basis note | Page 12 student share | Row CONFIRMED; note only | Q2 10.60 |
| AUTO-OUTFLOW-01 | Page 12 auto share | Scoring verdict needs the stock to fall in two seasoning-matched months (trust panel); HHDC is context | Q2 5.49, Q1 5.60 |

## ⚠️ The divergence is a live possibility, not a formality

If Q3 card 90+ share prints below Q2, the superseded rule fires (leg 1 already met) while the live rule cannot (needs Q3 flow ≤ 6.10, about 87 bp below Q2). That is a §1 divergence and goes to Will the same session.

Base rates, Page 12 CC, Q2 vintage, 03:Q1–26:Q2 (computed 11/09 from the file, not from memory):
- Q2→Q3 moves: 16 down, 7 up of 23.
- Q3 after a Q2 decline: 11 down of 14.
- Last three Q3s were up: 23:Q3 +1.43, 24:Q3 +0.20, 25:Q3 +0.14 (the retention-era regime, NY Fed Liberty St 8/11 on charged-off balances staying on reports).
- Read: the full history puts a divergence near 70–80%; the recent regime points the other way. Treat it as roughly even, and have the Will escalation ready either way. CARL benefits from the reset; the shadow row exists so that cannot hide.

Page 14 CC context for CRL-33: Q2→Q3 moves 10 up of 23; after a QoQ decline 9 up of 49 on this count (the registration note says 8 of 48; the one-row difference is not reconciled, and it does not move the 25% at registration). 25:Q3 was +0.12.

## What does not count (from the card §4, restated only as reminders)
- A share decline is not a numerator improvement: decompose share, dollars, balances.
- Page 13 (flow into 30+) and Page 14 are one pipeline, one witness.
- Never Page 28; never the PDF prose for the flow series.
- One vintage for both quarters; the script prints the Q2→Q3 revision diff.
