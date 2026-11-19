# D:L823 — the 10/22 "banks bid, tech sold" alarm at +20 sessions; H4 against the study; first map on the 11/19 chain

**HENRY · written 2026-11-19 from 10:07 ET (`date`) · PROME prome-36 task letter (10:02 ET), D:L823 · Claude Code, Opus 5.5 (`claude-opus-5-5`), laptop.** Zero dollars, no threshold or level changed.

## 1. The grade: UNRESOLVED at +20 sessions, by the study's own letter. Not a hit, not yet a sixteenth false positive

**The study's definition, read in its code** (`PROME/reports/2026-10-23_kre-qqq-transition-signature/build.py`, lines 15, 26, 28, 234–235):
- A **qualifying day t** = KRE **and** QQQ close-to-close return from t to **t+60 sessions** both ≤ −10%.
- **Hit** = a qualifying day in [alarm day, alarm day + 20 sessions] (line 234, inclusive of the alarm day).
- **Resolved only where H + 20 = 80 forward sessions exist** (line 235; the report's Method table says the same).

So the +20-session date (today, 11/19, the 20th session after 10/22, counted from the vendor bars below) closes the **window in which a decline may start**. It does not resolve whether one did: each candidate day needs its own close 60 sessions later. **The earliest candidate (10/22) resolves on 2027-01-20; the last (11/19) on 2027-02-18** (NYSE holidays entered by hand: 11/26, 12/25, 1/1, 1/18, 2/15; an unscheduled closure would push both).

⚠️ DOCKET L823 paraphrases the hit as "a joint ≥10% decline of KRE and QQQ starting within 20 sessions of 10/22; otherwise a 16th false positive", which reads as decidable today. The study's letter is not. **The row was dated at the end of the start window, not at the resolution date.** Recommendation to PROME: re-date the row to 2027-02-18 (first possible resolution 2027-01-20). PROME owns the DOCKET.

**Closes used** (yfinance auto-adjusted daily closes, the study's vendor, pulled 10:04 ET 11/19; 11/19 is intraday and only a candidate start day):

| t | session | KRE close | QQQ close | KRE needs ≤ at t+60 | QQQ needs ≤ at t+60 | KRE t → 11/18 | QQQ t → 11/18 | t+60 date |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 10/22 | 0 | 72.41 | 704.47 | 65.17 | 634.02 | −2.6% | −6.4% | 2027-01-20 |
| 10/23 | 1 | 72.46 | 704.40 | 65.21 | 633.96 | −2.7% | −6.4% | 2027-01-21 |
| 10/26 | 2 | 72.73 | 712.20 | 65.46 | 640.98 | −3.0% | −7.4% | 2027-01-22 |
| 10/27 | 3 | 72.58 | 721.25 | 65.32 | 649.12 | −2.8% | −8.6% | 2027-01-25 |
| 10/28 | 4 | 72.11 | 725.61 | 64.90 | 653.05 | −2.2% | −9.1% | 2027-01-26 |
| 10/29 | 5 | 72.86 | 715.34 | 65.57 | 643.81 | −3.2% | −7.8% | 2027-01-27 |
| 10/30 | 6 | 72.01 | 690.49 | 64.81 | 621.44 | −2.1% | −4.5% | 2027-01-28 |
| 11/2 | 7 | 73.73 | 681.09 | 66.36 | 612.98 | −4.4% | −3.2% | 2027-01-29 |
| 11/3 | 8 | 72.88 | 685.28 | 65.59 | 616.75 | −3.2% | −3.8% | 2027-02-01 |
| 11/4 | 9 | 74.13 | 691.95 | 66.72 | 622.76 | −4.9% | −4.7% | 2027-02-02 |
| 11/5 | 10 | 72.31 | 647.05 | 65.08 | 582.34 | −2.5% | +1.9% | 2027-02-03 |
| 11/6 | 11 | 72.20 | 656.10 | 64.98 | 590.49 | −2.3% | +0.5% | 2027-02-04 |
| 11/9 | 12 | 73.45 | 679.35 | 66.10 | 611.41 | −4.0% | −2.9% | 2027-02-05 |
| 11/10 | 13 | 73.09 | 674.76 | 65.78 | 607.28 | −3.5% | −2.3% | 2027-02-08 |
| 11/11 | 14 | 72.95 | 690.38 | 65.65 | 621.34 | −3.3% | −4.5% | 2027-02-09 |
| 11/12 | 15 | 72.52 | 688.17 | 65.27 | 619.35 | −2.8% | −4.2% | 2027-02-10 |
| 11/13 | 16 | 72.74 | 679.89 | 65.47 | 611.90 | −3.1% | −3.0% | 2027-02-11 |
| 11/16 | 17 | 72.19 | 661.75 | 64.97 | 595.58 | −2.3% | −0.3% | 2027-02-12 |
| 11/17 | 18 | 70.85 | 656.95 | 63.76 | 591.26 | −0.5% | +0.4% | 2027-02-16 |
| 11/18 | 19 | 70.52 | 659.51 | 63.47 | 593.56 | 0 | 0 | 2027-02-17 |
| 11/19 (intraday 10:04 ET) | 20 | 70.38 | 672.74 | 63.34 | 605.47 | — | — | 2027-02-18 |

**Where it stands (path, not the letter):** the deepest joint close-to-close decline from any window day so far is **−4.9% KRE / −4.7% QQQ (11/4 → 11/18)**, under half the 10% bar. The KRE leg is the one far away: from no window day has KRE fallen more than 4.9%. A hit now needs KRE at or under **$63.34–$66.72** (by start day) on the matching day in late January to mid-February, with QQQ at or under **$582–$653**.

**Read:** the alarm has not produced a joint 10% decline inside its start window, and cannot be scored until 2027-01-20 at the earliest. No grade is entered as a hit or a false positive. The study's own caution stands: 3 hits in 18 is indistinguishable from the 10.6% base rate (about 30% chance of 3+ hits by luck), and the rule was chosen after seeing the episodes.

## 2. The state since 10/22: the see-saw has ended, the coupling has come back

Same vendor closes, the study's definitions (c20 = 20-session correlation of daily returns; see-saw share = opposite-sign days in the last 10; ratio DD = KRE/QQQ vs its own 20-session high):

| Close | c20 | see-saw share, last 10 | ratio DD | KRE 10-session | QQQ 10-session | S12 ("banks bid, tech sold") |
|---|---:|---:|---:|---:|---:|---|
| 10/22 (alarm) | −0.24 | 80% | 0.0% | +4.1% | −5.8% | fired |
| 11/4 | −0.18 | 70% | −1.0% | +5.0% | −4.6% | fired (inside the 20-session quiet rule, not a new alarm) |
| 11/5 | **+0.21** | 60% | 0.0% | −0.1% | −8.2% | off |
| 11/11 | +0.25 | 50% | **−5.4%** | +1.2% | −4.9% | off |
| 11/18 | **+0.31** | **40%** | **−4.3%** | **−4.9%** | **−4.7%** | off |

- Correlation crossed back above zero on 11/5 (the study's S1 shape, which has 1 hit in 12 alarms and a lift under 1: no information in it).
- On 11/18 three of the study's "pre-snap state" marks are inside the nine episodes' range: c20 +0.31 (range −0.02 to +0.71), see-saw 40% (max 60%), KRE lagging at −4.3% (5 of 9 were at −4% or worse). Two are not: VIX 24.56 [Cboe settle 11/18] against a nine-episode median of 14.6, and QQQ −9.1% from its 10/28 close instead of near its high. The nine started calm; this is not calm.
- **The study's own "what would change this read" sentence** (REPORT.md, § What this means): *"HY OAS keeps rising from 3.40% and KRE closes below its 20-session relative high by 4% or more, while QQQ is still falling."* On the 11/18 close: ratio DD **−4.3%** (met), QQQ 10-session **−4.7%** (met), HY OAS **343bp [FRED 11/17]**, over 340 and up three sessions running (323, 334, 343); **HY for 11/18 not posted at 10:05 ET**. On its letter the description is met on two legs and the third is met on the last posted print. ⚠️ **This sentence is a plain-language watch item written for Will, not a registered trigger:** no precision was ever measured for it, it describes one analog (July 2024, which fell KRE −10.2% / QQQ −7.6% over 7/31 → 8/5/2024 and then recovered within weeks), and the study found no early-warning read beating chance by a usable margin. Today's intraday tape (SPX +0.9%, QQQ +2.0%, KRE −0.2% at 10:04 ET) is not a close.

## 3. Charter rule H4 against the study's 2-of-9 result

**H4 (charter § CORE METHODOLOGY):** "Equity CANNOT bottom until HY OAS peaks. Credit leads equity by 2-3 sessions. Rate of change matters more than absolute level."

| H4 clause | What the study tested | Verdict |
|---|---|---|
| "Credit leads equity by 2–3 sessions" | Onset of a +30bp 10-session HY OAS jump vs the equity snap (day 0) in the nine KRE/QQQ joint declines, 2007–2024 (Table B3, Table N) | **Contradicted for onsets.** HY jumped before day 0 in **2 of 9** (anchor B; 1 of 9 on anchor A), median **+6.5 sessions after** the snap, against a 41% chance share in random windows. In these nine, credit followed equity. HY Δ10 at day 0 was a median −6bp (8 of 9 at +8bp or less) |
| "Equity cannot bottom until HY OAS peaks" | Not tested: the study measures starts, not bottoms | **Untested.** I have used this clause live (11/18 MAP § 7: "no low called under H4 while HY widens"); that use rests on the clause's own record, not on this study |
| "Rate of change matters more than level" | Not tested directly | Untested |

**What I change in my own practice now:** I stop citing the lead clause. A quiet credit tape is not an all-clear for an equity break (the nine broke with credit flat), and widening credit is not a lead indicator of a break that has not happened.

**What I do not change without PROME:** the charter text. The letter's limits send charter changes back as a draft. Draft for PROME (and the settled LESSONS heading "[Analysis] — Credit Leads Equities, Not Vice Versa", which says the same):

> **Credit-Primary Rule (H4):** Equity cannot bottom until HY OAS peaks (**untested as of 2026-11-19**). ~~Credit leads equity by 2–3 sessions.~~ In the nine KRE/QQQ joint declines 2007–2024, HY OAS widened **after** the equity break (onset before the break in 2 of 9, median 6.5 sessions after; `PROME/reports/2026-10-23_kre-qqq-transition-signature/REPORT.md` Tables B3 and N), so a quiet credit tape is no all-clear for an equity break. Rate of change matters more than absolute level.

A pre-declared test of the bottom clause (trough of the KRE+QQQ basket vs the HY OAS peak, inside a fixed window after each of the nine day-0s, the window fixed before looking) is cheap on `build.py`'s data. Offered, not run.

## 4. First dealer map on the 11/19 chain (open interest through 11/18, the first carrying Nvidia results-day trades)

`gamma_flip.py --both --spot <vendor live> --publish`, Cboe chain stamped asof 2026-11-19, read 10:04–10:05 ET (after the 09:47 ET IV-zero window).

| Chain | Spot (vendor live) | Flip 14d / 35d | Net gamma 14d / 35d ($B per 1%) | Put wall | Call wall | Published |
|---|---|---|---|---|---|---|
| SPX | 7,390.00 (Cboe feed 7,400.29) | **7,545 / 7,556** | **NEGATIVE −43.9 / −62.2** | ⛔ WITHHELD: put = call at 7,400 (14d) and 7,000 (35d), put side unresolved | ⛔ WITHHELD: 14d 7,400 near-tie (band 7,400–7,500) vs 35d 7,000 | flip and net gamma PUBLISHED; walls NONE |
| QQQ | 673.05 | **673 / 673** | **0.0 / 0.0** (35d read −0.1, NEGATIVE, one run earlier) | ⛔ WITHHELD: put = call at 680 | **680 PUBLISHED** (clean at both, +40% / +15%), overhead | flip and net gamma PUBLISHED; call wall 680 supersedes 700 [11/12]; put wall NONE supersedes 680 [11/12] |

**So what:** the S&P is still about 155 points (2.1%) under its flip, so dealers still amplify moves in either direction; the results-day trading moved the flip down only about 7 points (7,552 / 7,561 at the 11/18 close on 11/17 open interest → 7,545 / 7,556). The Nasdaq ETF sits exactly on its flip: no regime either way, and 680 overhead is the heaviest strike. A close over about 7,550 turns the S&P regime; this map says how big moves get, not which way. ⚠️ Free-tier proxy: sign and flip robust, $B assumes long-call / short-put dealers, IV held fixed.

**Tape (vendor, boot 10:02:59 ET):** SPX 7,377.18 (+0.73%), VIX 22.83 (−7.04%), VIX9D 22.20 < VIX3M 23.22 (contango), VVIX 113.33, KRE $70.34, 10Y 5.09, USD/JPY 159.91. **FRED (read 10:05 ET):** SP500 11/18 **7,323.63** and VIXCLS 11/18 **24.56** both confirm my 11/18 closes; HY 11/18 not posted (HY 343, CCC 1,329 [11/17]).
