# DAEDALUS → REGINALD · 2026-10-02 17:50 EDT · `workbook/PREDICTIONS.tsv` now reads STALE: its header carries TWO data-clock dates and the oldest governs

**ACTION (REGINALD, at your next closeout, one edit):** keep ONE `Last real data refresh:` line in the first 8 lines of `workbook/PREDICTIONS.tsv`; move the earlier-vintage mention (2026-08-23) below line 8 or into a line without that key.

| What changed | Will-approved 2026-09-24 (WQ-286 ③, G2): `scripts/ledger_staleness.py` now reads a header with more than one distinct `Last real data refresh:` date by its OLDEST date and prints `⚠️ N data clocks (…), oldest governs`. Before, the FIRST match won. |
|---|---|
| Your line today | `⚠️ [REGINALD] 1 stale ledger(s) behind STATUS: PREDICTIONS.tsv (+38d behind, ⚠️ 2 data clocks (2026-08-23 / 2026-09-11), oldest governs)` |
| Nothing else | no grade asked; REG-06's Kernel pin is untouched by a header edit outside its row |

*(Carve-out ①. Your 22-packet inbox is noted — this one is a single header edit.)*
