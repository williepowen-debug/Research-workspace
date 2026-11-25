# CRL-32 leg 1 and KILL check: BEA October 2026 Personal Income and Outlays

Graded 2026-11-25 by CARL (Claude Code, Opus 5.5, session carl-1125, launched by PROME prome-77 for DOCKET L860). Rule of record: `research/2026-10-29_WQ537/LETTER.md` §3 and `thesis/PREDICTIONS.tsv` CRL-32 (the TSV wins on any disagreement). No level, operator, instrument or consequence changed.

## 1. Source and vintage

| Item | Value |
|---|---|
| Release | BEA 26–51, "Personal Income and Outlays, October 2026", embargoed until 8:30 a.m. EST Wednesday 2026-11-25 |
| Primary files read | `https://www.bea.gov/sites/default/files/2026-11/pi1026.pdf` (5 pages) and `.../pi1026-hist.xlsx` (Historical Comparisons, dated 2026-11-25), downloaded 2026-11-25 about 09:01 ET; release page `bea.gov/news/2026/personal-income-and-outlays-october-2026` read the same minute |
| Cross-check | FRED PSAVERT first-published vintage via `FORGE/tools/market-data/fetch.py fred PSAVERT --first-published` (09:01 ET): October 4.1, first_published 2026-11-25; September 3.8, first_published 2026-10-29 |
| Vintage graded | October's FIRST-PUBLISHED saving rate (this release) |

## 2. Grade

| Leg | Rule | Observed (first print) | Result |
|---|---|---|---|
| Leg 1: October saving rate | ≤3.8% keeps the letter alive; ≥3.9% = NOT-FIRED-REBUILD, early resolution | **4.1%** (BEA PDF p.1: "the personal saving rate—personal saving as a percentage of DPI—was 4.1 percent"; hist.xlsx row "Personal saving rate" 4.1) | **≥3.9: NOT-FIRED-REBUILD** |
| KILL: September revised | KILL if September is revised to ≥4.3% | **3.6%** (hist.xlsx: "Last period with smaller value 2026M09 3.6"; FRED PSAVERT latest 3.6) | **Not met** (revised DOWN 0.2 pp, away from the kill) |

**Outcome: CRL-32 resolves NOT-FIRED-REBUILD on 2026-11-25 (early resolution). Ledger status MISSED** (the FIRE branch was priced at 25%, so this is the 75% branch; same convention as CRL-33). The 12/23 print no longer grades this letter.

Consequence, by the letter §6 only: STATUS Savings row 🟠 "buffer drawdown" → 🟡 "one-month drawdown, not sustained". Nothing else: no score, threshold, card, trade or capital meaning.

## 3. Revisions (logged beside, never graded; M70: old report vs new report)

| Month | Saving rate first print | At 10/29 vintage | At 11/25 vintage | Real DPI $bn ch. 2017, 10/29 → 11/25 |
|---|---|---|---|---|
| July | 3.0 (8/26) | 4.5 | 4.4 | 18,414 → 18,394 |
| August | 4.1 (9/30) | 4.0 | 3.9 | 18,416 → 18,402 |
| September | 3.8 (10/29) | 3.8 | **3.6** | 18,366 → 18,368 |
| October | **4.1** (11/25) | — | 4.1 | — → 18,460.3 |

September's drawdown was DEEPER than first printed (3.6%, equal to October 2022's low). The revision changes no outcome (only the KILL row could, and it points the other way).

## 4. Shape (descriptive, not a leg)

| Series, 11/25 vintage | September (rev) | October |
|---|---|---|
| Personal income, % m/m | 0.3 | 0.7 (+$201.8B) |
| Nominal DPI, % m/m | 0.3 | 0.8 (+$200.5B) |
| Real DPI, % m/m | −0.2 | **+0.5** (+$92.8B chained) |
| Nominal PCE, % m/m | 0.6 | 0.3 (+$63.8B) |
| Real PCE, % m/m | 0.1 | **0.0** (−$5.8B chained) |
| PCE price index, % m/m | 0.5 | 0.3 (3.8% y/y; core 0.3, 3.3% y/y) |
| Personal saving, $bn SAAR (FRED PMSAVE) | 871.4 | 1,002.7 (+$131.2B per BEA) |

October's shape is the opposite of September's: income up, real spending held flat, saving rebuilt. Households did not spend the income gain.

⚠️ **One-off in the income (BEA technical note, verbatim):** "The increase in government social benefits was led by other social benefits, primarily reflecting one-time payments associated with the Medicare Improvement Fund premium rebate." BEA gives no dollar size in the release. **CARL estimate (INFERRED, not graded):** personal current transfer receipts (FRED PCTR) rose $58.6B SAAR in October against $17.9B in September; treating the $40.7B excess as the rebate, the saving rate ex-rebate is 3.93% (rounds to 3.9); removing the whole $58.6B transfer rise gives 3.86% (rounds to 3.9). So the REBUILD outcome does not hinge on the rebate at one decimal, but most of the margin over 3.8 is one-off. Dividend income also contributed (BEA). The grade stands as published; the caveat travels with it.

## 5. Cost leg (pointer, letter §4)

October CPI-U all items SA m/m **+0.350%** as HENRY records it (BLS 11/10; CARL STATUS KB-615). Label: the NOT-FIRED occurred **with costs still climbing** (PCE prices also +0.3% m/m). CARL does not grade CPI.

## 6. Cohort leg (letter §5)

Descriptive only. The DFA Q3 read on Thu 2026-12-10 (with Z.1) stays on the docket as a descriptive read of who drew down in Q3; it no longer serves a live letter.

## 7. Forward view (unscored, Will 2026-11-19)

| Question | View | Why / alternative / what changes my mind |
|---|---|---|
| November first-print saving rate (BEA Wed 2026-12-23) | about 60% it prints ≤3.9%, about 40% ≥4.0% | The rebate drops out of November income, which mechanically lowers the rate by roughly 0.15–0.2 pp from 4.1 if spending holds; base: the rate has been 3.6–4.4 over July–October in the current vintage. Alternative: holiday spending soft and wage income firm keeps it ≥4.0. Changes my mind: November retail control group (12/16) under 0 would raise the ≥4.0 odds. |
| September 3.6% revised further | about 50% it moves again by ±0.1 at 12/23 | the last three releases each revised the prior months down 0.1–0.2 pp |
| Is the "buffer drawdown" mechanism dead? | No. One month of rebuild, a third of it one-off, after a month revised to 3.6% | A second month ≥4.0% on 12/23 without one-offs would make the drawdown a single-quarter episode, not a trend. |

Not registered: no new letter (Will 2026-11-19: register material, resolvable calls only under existing rules). The view above is for PROME's brief.
