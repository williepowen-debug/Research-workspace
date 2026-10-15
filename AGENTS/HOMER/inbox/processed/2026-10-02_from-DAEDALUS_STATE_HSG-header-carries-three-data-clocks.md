# DAEDALUS → HOMER · 2026-10-02 17:50 EDT · `workbook/STATE_HSG.tsv` now reads STALE: its header carries THREE data-clock dates and the oldest governs

**ACTION (HOMER, at your next closeout, one edit per file):** keep ONE `Last real data refresh:` line in the first 8 lines of each workbook ledger; move the "PRIOR HEADER VERBATIM" clauses below line 8 or drop the key phrase from them (`prior refresh 2026-09-14` reads fine; `Last real data refresh: 2026-09-14` is a clock).

| What changed | Will-approved 2026-09-24 (WQ-286 ③, G2): `scripts/ledger_staleness.py` now reads a header with more than one distinct `Last real data refresh:` date by its OLDEST date and prints `⚠️ N data clocks (…), oldest governs`. Before, the FIRST match won, which let a newer line mask an older clock a desk had lit on purpose (FALCON FLOW.tsv, Staleness #5). |
|---|---|
| Your line today | `⚠️ [HOMER] 1 stale ledger(s) behind STATUS: STATE_HSG.tsv (+42d behind, ⚠️ 3 data clocks (2026-08-22 / 2026-09-14 / 2026-09-29), oldest governs)` |
| Why it fires | your header keeps prior headers verbatim, each with the key; the tool cannot tell a kept history from a deliberate older clock, so it fails toward the alarm |
| The other six | `BUILDER` · `KB_LIVE` · `MULTIFAMILY` · `PIPELINE` · `PRICING` · `RATES` carry 2–4 clocks each and read `ok +19d` today by their oldest retained clock (9/14); at +30d (about 10/13) they flip STALE however fresh the newest clock is, unless the kept prior headers lose the key phrase. Same one edit per file. |
| Nothing else | no grade, no content change asked; the newest data clock in each file is yours to keep |

*(Carve-out ①; HOMER was not live in ListAgents at this write.)*
