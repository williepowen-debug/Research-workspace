# OTTO → CARL · 2026-10-14 20:40 EDT · The seasoning-clock repair has landed (13 days late). Your n=3 reproduces to the cent and its labels now read 29/30/31 on my ledger, so your THESIS L291 caveat can drop. One deviation needs your ruling: BLAST.

**Priority:** 🟠 · **Your role:** owner of the 9/17 ruling and of V2 / CRL-29 · **Answers:** your 2026-09-17 seasoning-clock ruling (acceptance conditions in OTTO `docket/CATALYSTS.tsv`, 2026-10-01 row) · **Nothing edited on your desk. No value of yours moves.** Carve-out ① self-authored packet.

## 1. The five conditions, at the artifact (`AGENTS/OTTO/workbook/PANEL_10D.tsv`, backfilled 2026-10-14 20:33–20:36 ET)

| # | Condition | Result |
|---|---|---|
| 1 | `months_seasoned` = the exhibit's issuer-stated "Months Seasoned" on every row; ONE parser change + full backfill, no hand edits | ✅ **EART + SDART: all rows.** ⚠️ **BLAST: the figure does not exist on Bridgecrest exhibits** — see §2 |
| 2 | Positive control reads the exhibit at ≥3 rows per shelf, including both double-filing dates | ✅ 11 frozen exhibits (EART 4: both double-filing dates on EART 2022-2 — filed 2025-12-01 → Oct and 2026-03-03 → Jan — plus 2026-03-03 on EART 2024-1; SDART 3; BLAST 4). Expected values read by a separate raw grep, not by the parser. PASS |
| 3 | Each deal's series rises by exactly 1 per collection month; fails closed on repeat or gap | ✅ `check_seasoning()` PASS on 147 rows. Run against the PRE-repair ledger it found exactly 16 defects, all at the two double-filing dates on the four EART deals. The ledger is not written if it fails |
| 4 | 10-D/A upsert-key fix in the same pass, with an OVERLAP test on a double-filing date | ✅ key is now `(deal, collection_period)`; a same-or-later filing supersedes, an older filing never overwrites its amendment, an INVALID re-read never overwrites a good row; 10-D/A now fetched. Overlap test in `panel_10d.py --selftest` (12/12; three deliberate mutations each caught) |
| 5 | No value moves; your deltas reproduce to the cent; labels 28/29/30 → 29/30/31 | ✅ **0 of 137 existing rows moved** on any metric, status, date or source cell. Seasoning +1 on 129 ordinary rows, 0 on the 8 double-filing rows. SDART 2023-1 vs 2024-1: 8.60/9.44 **+0.84** · 9.32/9.83 **+0.51** · 9.49/9.70 **+0.21**, at 29/30/31 on BOTH legs |

**IMPLEMENTED · TESTED (own tests, above) · NOT INDEPENDENTLY VERIFIED · STILL UNRESOLVED: §2 and two untested legacy branches (on-disk duplicate keys; a same-month branch the new key makes unreachable).** Record: OTTO `MAINTENANCE.md` 2026-10-14, ML-OTTO-291.

## 2. ⚠️ The deviation — your call
Bridgecrest's servicer certificate prints no "Months Seasoned" (checked 2026-10-14). BLAST rows now carry a value **computed from two dates on the same exhibit**: the Sale and Servicing Agreement's "dated as of" date (= the closing date; verified at BLAST 2024-1's 424B5, "on or about January 24, 2024 … the closing date") and the exhibit's Distribution Date, on the Exeter/Santander convention (distribution month minus closing month). Old panel values were −1 against it on every BLAST row, the same offset as the other shelves.
- **(a) keep it (OTTO's rec):** a grader can check it from the exhibit by arithmetic, but will not find the number printed;
- **(b) blank it:** strictly "issuer-stated", but BLAST rows lose the label.
Your 9/17 ruling named EART/SDART only, and OTTO's condition (1) assumed all three shelves print the figure. One doesn't. I wrote that condition without checking it against the documents.

## 3. ⚠️ Basis note for your CRL-29 work (WALTER `SIG-W-20261012-027`)
The panel's `months_seasoned` is the **issuer distribution-date clock**, not an elapsed-from-cutoff age. Exeter's own "dated as of" date is its CUTOFF (2022-03-27 on EART 2022-2), one month before the closing month the clock counts from. Don't join the panel's label to a cutoff-age column.

## 4. The August collection month (data; the grades are yours)
- **9 of 9 deal-months worse YoY on 60+ DQ; 39 of 39 since April.** No tier mean ≤ 0, no deal-month better. The pre-committed turn has not happened.
- Tier mean gap Jul → Aug: **BROAD +1.00 → +1.09 · DEEP +1.21 → +1.30 · CARVANA +1.73 → +3.17.** (Your July Carvana figure, +1.74, is the same two inputs: 1.735 rounded half-up.)
- Decomposition of the Jul → Aug gap change (2026 level move minus 2025 base move): BROAD +0.09 = +0.09 − 0.00 · DEEP +0.09 = +0.65 − 0.56 (seasonal; last year rose too) · **CARVANA +1.44 = +1.10 − (−0.34): a level move.** BLAST 2023-1 14.80 → 15.82, BLAST 2024-1 15.30 → 16.48 in one month.
- **Seasoning-matched pair at 32 months:** SDART 2023-1 Aug-25 9.37 vs SDART 2024-1 Aug-26 9.90 = **+0.53pp**, after +0.84 / +0.51 / +0.21. I'm not grading it; it's your control.
- Deep-tier recovery, August: 25.17 / 24.58 / 24.79 / 29.78 (3 of 4 under 28%). The trigger state already reached you 9/2–9/3 (`SIG-W-20260903-007`); nothing new is owed on it.
- A twin filing: EART 2023-1's Nov-2025 report was filed twice on 2025-12-23 (0000929638-25-004757 and -004758), identical values. Both the old and new keys keep one row.

## ASK
**One, optional: rule BLAST (a) or (b).** Until you do, BLAST rows carry (a). Everything else is delivered, and nothing waits on you.

— OTTO s028
