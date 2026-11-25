# Regrade to the letter: BRT-23 and BRT-28 (2026-11-25)

**Authority:** PROME C10 (WQ-673 A): a desk grades its own forecast by its own written rule where no level, operator, instrument or consequence changes; PROME verifies. Task: DOCKET L1224 ("take up its three outside-audit proposals only as far as its own grades go"). Origin: outside audit 2026-11-16 items 1 and 2 (PROME packet `inbox/processed/2026-11-16_from-PROME_outside-audit-items-verify-first.md`); BRENT's proposal 2026-11-20 (`PROME/inbox/processed/2026-11-20_from-BRENT_window-cot15-commission-delivery.md`).

**Rule applied:** the registered claim (the letter) is what is graded; a mechanism read is recorded beside the grade, never in place of it (`[[finding_threshold_vs_mechanism]]`; `AGENTS/DAEDALUS/scripts/scorecard.py` maps FAILED to MISS and "RESOLVED — MECHANISM-CONFIRMED" to HIT, so a mechanism-scored row enters the scorecard on the wrong question).

| Row | Registered claim | Prior status (kept verbatim in the row) | Letter evidence | New status |
|---|---|---|---|---|
| BRT-23 | A major DRC SX-EW copper/cobalt operator announces force majeure or significant curtailment within 60 days of Hormuz closure persisting, by May 2026 (70%) | FAILED 2026-05-31 (mechanism falsified) | Glencore force majeure on cobalt supply contracts; my own archive entry already reads "TRUE (in letter)" (`PREDICTIONS_ARCHIVE.md#BRT-23`) | **CONFIRMED** (letter). Mechanism (sulphur cost) FALSIFIED: the DRC export ban drove it. Brier at 70%: 0.09 |
| BRT-28 | Else-branch, since HAW-10 expired unfired: "Brent holds current $90-100 range" to Jul 1; invalidation "HAW-10 expires unfired but Brent breaks $90-100 range by Jul 3" (70%) | RESOLVED — MECHANISM-CONFIRMED/THRESHOLD-MOOT 2026-07-01 | FRED DCOILBRENTEU: 88.64 on 6/12 (first print under 90), 68.53 on 7/2 (pulled 2026-11-25 with the honest client name; `research/2026-11-25_eia-gulf/raw/fred_DCOILBRENTEU_jun-jul.csv`). Dated Brent stands in for front-month; the break is about $21, far outside any spot-futures basis | **FAILED** (letter; invalidation met). The Bab premium bleed-out stays recorded as context. Brier at 70%: 0.49 |

**Not touched:** BRT-22 (scored a hit on mechanism under Will's June 1 split ruling; the letter regrade is Will's, held with PROME). BRT-26 confirmed scored at 85% (the 9/6 mark), answered 11/20. No level, operator, instrument or consequence moved; no live row is affected.

**Caveat:** BRT-23's force-majeure date is not in my records; "within 60 days of Hormuz closure" rests on my own archive's in-letter TRUE, not on a dated Glencore notice re-read today. If PROME's verification wants the date, it is a primary-source read at Glencore, not a change of rule.
