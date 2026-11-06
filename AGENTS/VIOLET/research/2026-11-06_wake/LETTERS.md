# VIOLET prediction letters, 2026-11-06

**Frozen at commit.** Registered 2026-11-06 10:28 ET, before any result in these windows existed, under `PROME/reports/2026-11-05_prediction-registration-brief.md`. The commit that adds this file is the pre-result receipt. These are forecasts: they change no gate, level, score, band, card or trade.

**Common basis, every letter.**

| Element | Term |
|---|---|
| Series | Cboe `<NAME>_History.csv` at cdn.cboe.com, CLOSE column where one exists, otherwise the column named for the index |
| Precision and ties (SL-5) | Published to 2 decimals. The as-published value is the grading value. A print exactly on the line satisfies `≥` and does not satisfy `<` |
| Vintage | As first published on the History file. Cboe index closes are not a scheduled-revision series. A later restatement is noted on the row, never re-graded |
| Sessions | Every Cboe index session in the window, inclusive of both ends. No persistence condition, one close is enough, no reset |
| Anchor type | IMMOVABLE: a fixed calendar date that no participant can move. Not tied to any event date |
| Missing data | History file unavailable or a session absent at the owner's grade: NO-VERDICT with a one-line why, never a silent extension |
| Grading | Owner grades at the first session after History posts the end date. Grade whether the event as written happened |
| Comparison forecast | The base rate below. No market-priced odds used; those are ORACLE's |
| Producibility (SL-4) | Every level has printed on its named series: see each letter |

Base rates: `research/2026-11-06_wake/base_rates.py`, output `base_rates_output.txt`, Cboe History through 11/05. All are small, overlapping-regime samples spaced by construction, not independent draws. The published VVIX and SKEW files carry no high or low, so these letters read closes only.

## VIO-PRED-07: the cash inversion ends within six sessions

**Letter:** VIX3M CLOSE ÷ VIX CLOSE, same date, computed from as-published closes and not rounded, is `≥ 1.000` on at least one session from 2026-11-06 through 2026-11-13.

**Probability: 72%.** Resolves 2026-11-13.

**Base rate:** first inverted close after at least 20 clean closes, exit within the next six sessions: 36 of 42 (85.7%). Where the next close was still inverted: 12 of 18 (66.7%). At or under 0.93 on the first close: 3 of 3. **Difference from base:** priced nearer the still-inverted case, because 11/06 read 0.9552 at 10:20 ET, not a close. **Starting point:** 0.9067 [11/05 History]. **Producibility:** 1.1318 [11/04]. **Premise, OBSERVED:** KB-VIO-034, inversion marks peaks. **If wrong:** the curve stays inverted past CPI 11/10, which would say this is priced as more than a one-day concentration event.

## VIO-PRED-08: VIX closes at or above 30 by November 20

**Letter:** VIX CLOSE `≥ 30.00` on at least one session from 2026-11-06 through 2026-11-20.

**Probability: 25%.** Resolves 2026-11-20.

**Base rate:** from the first inverted close, a later close at least 6.46% higher within 11 sessions: 17 of 42 (40.5%). Where VIX then fell at least 5% next close, and later closed at least 21% above that next close, the rise today's level needs: 5 of 20 (25%). **Difference from base:** the second row is the closer match, since VIX read 24.76 at 10:20 ET on 11/06, not a close. CPI 11/10 and NVIDIA 11/17 sit inside the window; negative dealer gamma (HENRY, 11/06 map) cuts the other way. **Producibility:** 30.61 [3/30/2026]. **Not the declined call:** Will did not take the Path A proposal for the 10/22 episode (VIX close at or above 29.03 by about 12/07, `research/2026-11-05_path-a-f2/REPORT.md` item 3). This letter is a different level, window and question, carries no Path A claim, and the existing VIX 30 line stays as it is.

## VIO-PRED-09: SKEW closes under 140 by year-end

**Letter:** SKEW close `< 140.00` on at least one session from 2026-11-06 through 2026-12-31.

**Probability: 45%.** Resolves 2026-12-31. A later date than the other letters because SKEW's regime moves slowly.

**Base rate:** SKEW 145 to 155 with 20-day mean at or above 150, any close under 140 in the next 38 sessions: 3 of 7 episodes (42.9%), first day of each episode after a 30-day gap; 64.7% of 119 clustered days, which overstates it. **Difference from base:** none intended; the episode count is the honest figure. **Starting point:** 149.37, 20-day mean 154.00 [11/05]. **Producibility:** last close under 140 was 138.36 [8/14/2026]. **Scope:** one close of the SKEW series VIOLET owns. RED-FT-10's exit, under 140 for four closes, is RED's and is a different letter; this does not grade it.

## VIO-PRED-10: VVIX closes under 100 by November 20

**Letter:** VVIX close `< 100.00` on at least one session from 2026-11-06 through 2026-11-20.

**Probability: 55%.** Resolves 2026-11-20.

**Base rate:** first VVIX close at or above 125 within 5 sessions of a close at or below 100, no close at or above 125 in the prior 20 sessions: under 100 within 11 sessions 7 of 13 (53.8%), within 19 sessions 10 of 13. Since 2024: 3 of 3. **Difference from base:** left near it. Recent cases argue higher; NVIDIA on 11/17 and the 11/18 VIX expiry hold vol-of-vol up late in the window. **Starting point:** 134.99 [11/05 History]; 120.84 at 10:20 ET 11/06, not a close. **Producibility:** 90.41 [11/04].
