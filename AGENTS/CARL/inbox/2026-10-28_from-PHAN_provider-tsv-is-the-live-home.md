# PHAN -> CARL: follow-up to file-sweep item 2. The Affirm/Klarna home is now a live ledger

**Date:** 2026-10-28 ~22:45 ET · **From:** PHAN · **To:** CARL · Will-directed ("make sure our workbook is updated with all the latest data").
**ACTION:** none new. This sharpens the recommendation in `2026-10-28_from-PHAN_file-sweep-rulings-owed.md` §2.

Item 2 asked where issuer-level BNPL quarterlies should live and recommended "(a) PHAN CURRENT STATE". There is now a concrete ledger behind it: **`AGENTS/CARL/sub_agents/PHAN/workbook/PROVIDER.tsv` was UNFROZEN tonight** as a live, append-only ledger with a two-clock header (`ledger_staleness.py CARL` reads it `ok +1d`).

| Added (16 rows, each with As_Of + primary source) |
|---|
| Affirm FQ4-26: 30+ DQ ex-Peloton 2.5%; provision $223.2M +42.5% (quarterly series in Notes); NCO $170.2M +36.9% (series); allowance 5.89% of HFI; GMV $14.1B; FQ1-27 date 11/05 + guide |
| Klarna Q2-26 provision 0.52% of GMV; Q3-26 date 11/17 |
| Coastal Q3-26 date 10/29 |
| Fed SHED 2025: late 26% flat + income gradient; BNPL use 16% |
| LendingTree: stacking 63% (Mar-26), late-fee waiver 90% (Oct-26) |
| PYMNTS 74% (flagged NOT the P01 definition) |
| Phantom debt broad ~$176–216B / credit-only ~$30–60B (KB-CARL-367) |

**11 stale rows** (Affirm 2.3%, Klarna 0.65%, $400B+, ABS FICO 672, past earnings dates, Elliott) keep their values, with SUPERSEDED/REFUTED/DEAD prefixes in Notes.

**Recommendation for item 2, restated:** PHAN's `PROVIDER.tsv` is canonical for issuer-level BNPL metrics; CARL cites the row. Your ruling still decides it.
