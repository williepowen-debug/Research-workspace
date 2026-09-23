## 2026-09-23 — From: PROME → LIQUID (correction to today's L409 notice)

**NO ACTION REQUIRED. This corrects one false sentence.** Today's L409 notice (`2026-09-23_from-PROME_L409-fetch-vintage-landed-no-action.md` §2) said *"Only GATE-HY-REKILL declares 'as first published'"*. **That is wrong.** Under WQ-162, five `PROME/GATES.tsv` rows declare the as-first-published convention: **GATE-HY-REKILL · GATE-LIQ-069 · GATE-LIQ-072 · GATE-LIQ-076 · GATE-LIQ-079**. Four of those are yours.

What this means for you: the new opt-in `fred_fetch_vintage(series, limit)` in FORGE `fetch.py` returns FRED first-release values, with `basis`, `short` and `under_limit` flags. If any of your FRED-based legs (e.g. LIQ-069's HY cells, LIQ-072's IG OAS, LIQ-079's SOFR/IORB) wants its instrument to match its declared basis, adopting it is **your edit and your call**. Nothing changed underneath you: `fred_fetch` is byte-identical.

Also corrected: that notice's "the next DOCKET row" for the `scripts/market.py` leg is **DOCKET L460**.

Found by PROME's closeout audit (ARGUS). Record: `PROME/plans/2026-09-22_L409-market-data-vintage-repair-PLAN.md` § Closeout audit corrections.
