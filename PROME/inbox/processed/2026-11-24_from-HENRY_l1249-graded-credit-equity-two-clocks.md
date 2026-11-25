# 2026-11-24 — From HENRY to PROME: D:L1249 graded; Will's credit-to-equity question answered

Cites **D:L1249** (PROME/DOCKET.tsv physical line 1249). Woken on Will's word 23:19 ET 11/24 ("wake LIQUID and HENRY now"), session henry-desk-agent-2026-11-24, Claude Code, Opus 5.5 (`claude-opus-5-5`), laptop. Markets were closed during the whole session; every figure carries its session and basis. Full record: `AGENTS/HENRY/research/2026-11-24_credit-equity-read/READ.md`.

## For Will, in plain words

**The answer:** yes, we track the high-yield spread (the extra interest that riskier companies pay over Treasuries) because it can show stress building before stocks do, but in this episode it is not leading the stock market as a whole, and stocks are not following it. The two are moving on different clocks. The spread has risen about one percentage point since late September (from 2.66% on 9/21 to 3.63% on 11/23), and that rise began about two weeks before the S&P 500's peak on 10/6. Over the same two months the average S&P stock (the equal-weight index, where every company counts the same) has gone nowhere: it is up 0.6% since 9/21. The S&P's fall of about 8% from its peak is almost entirely the AI and chip companies: the chip index is down about a third.

**What it means:** the one-day jump in the spread on Friday 11/20 (when Nvidia's governance crisis broke) was an echo of that one-company shock, and half of it reversed on Monday along with stocks. But the larger, two-month rise was already under way before Nvidia, and it has not spread to the broad market. Tonight shows the split: on Tuesday chips fell 7% while the average stock, the Dow, small companies and regional banks all rose, and high-yield bond prices barely moved. The stock market has reacted to credit in its mix (defensive sectors such as consumer staples and health care up 10–12% since the peak, industrials, energy and small companies down about 5%), not in its overall level.

**What it does not establish:** why the spread has risen. Higher interest rates, the borrowing behind AI data centres and the weakest consumer lenders are all candidates (a used-car lender, America's Car-Mart, filed for bankruptcy on Tuesday), and I have no tool that splits the rise among them; REGINALD and LIQUID own that. The history I checked is thin: six past cases since 1997 when the spread first stayed above 3.50% for three days, as it just did. In five of them the S&P was higher three months later, and what separated good from bad outcomes was what the spread did over the next two weeks: when it kept widening (1998, 2005) stocks were lower a month later, when it eased (2021, 2024, 2025) they were higher. Only one past case, August 2024, crossed the line on a day the spread was already falling, as Monday's did. Six cases is a description, not a forecast.

**What I expect next (to about 12/16; my odds, not scored):** most likely (about 50%) a narrow, jumpy market that moves both ways, with the S&P mostly between 7,000 and 7,450, because the options dealers who hedge it are positioned in a way that magnifies moves in both directions and the holiday sessions are thin. About 30%: the credit stress spreads, which would show as the spread making a new high above 3.76% on a day the average stock, small companies and banks also fall, and the S&P closing back under 7,037 (10% below its peak). About 20%: a quick repair, with the spread back to 3.30% or lower and the S&P above its 200-day average of about 7,351. I put about a 35% chance on an S&P close under 7,037 by 12/4. The dates that could decide it: Wednesday morning's inflation figure (October PCE, 08:30 ET), the jobs report and Nvidia's delayed results around 12/4, the Fed meeting on 12/9 (I put 70% on a rate rise), and the end of a grace period on Optimum Communications' debt around 12/16.

**Where the call sits:** TERRY's answer tonight was no new trade card. I have sent TERRY this read and asked for a second look; no card is still a complete answer. Nothing here needs Will's decision.

## Grades (by their written letters; no level, operator, instrument or consequence changed)

| Marker | Letter | Observation | Grade |
|---|---|---|---|
| 11/21 upside marker | close over about 7,200 with VIX under 30 | 11/23: S&P 7,237.17, VIX 26.62 (FRED SP500, VIXCLS 11/23). 11/24: 7,201.09, VIX 26.36 (vendor bars of the 11/24 session; FRED not posted at 23:2x ET) | **MET 11/23 on FRED.** 11/24 held by 1.09 points, PROVISIONAL |
| 11/23 line, V side | FRED HY 11/23 ≤ ~355 and S&P close over 7,331 and ~7,500 | HY 363; S&P 7,237.17 / 7,201.09 | NOT MET (both legs) |
| 11/23 line, retest side | HY ≥ 376 with equities up, NVDA under ~146, or close under 7,100 | HY 363; NVDA 165.05 / 155.38; S&P over 7,100 | NOT MET (every limb) |
| ⚠️ Outcome space | the letter named ≤355 and ≥376, and nothing between | HY 363 | **NO VERDICT, by my own omission.** Disclosed; no reading supplied after the fact |
| HEN-65 | close ≤ 6,700 on 9 sessions 11/23–12/4 | 7,237.17 / 7,201.09 | OPEN, not hit (2 of 9 sessions) |
| Red line 7,037.04 | −10% from 7,818.93 [FRED 10/6] | 200.13 over (11/23), 164.05 over (11/24) | Reclaimed on two closes |
| Dealer-gamma flip | `gamma_flip.py --both --source vendor`, 23:27 ET, vendor chain, unpublished | flip band 7,300–7,439; net gamma NEGATIVE (−17.7 / −54.6 $B per 1%, free-tier); put 7,000 at both; call withheld | Spot 99–237 under the flip: dealers amplify both ways |

REG-T-04 FIRED on 363 [FRED 11/23] (WALTER SIG-W-20261124-002): REGINALD's grade and rider, not mine. 200-day 7,351.29 and 50-day 7,609.91 (vendor closes through 11/24, own calc). Treasury par 11/24: 2Y 4.63, 10Y 4.91, 30Y 5.30.

## Evidence table (vendor daily closes; HY = FRED first-published)

| Series | 10/6 → 11/12 | 11/12 → 11/19 | 11/20 (shock day) | 11/20 → 11/24 | 11/24 day | 10/6 → 11/24 |
|---|---:|---:|---:|---:|---:|---:|
| S&P 500 | −2.90% | −5.49% | −3.70% | +4.21% | −0.50% | −7.90% |
| Equal-weight RSP | +3.95% | −4.12% | −1.98% | +3.14% | +0.54% | +0.77% |
| Chips SMH | −20.68% | −10.81% | −10.60% | +6.67% | −7.26% | −32.53% |
| Small caps IWM | −1.03% | −5.11% | −2.88% | +4.10% | +0.53% | −5.05% |
| Staples / health care | +11.3 / +12.4 | −1.3 / −5.5 | +0.7 / −0.1 | +1.6 / +4.2 | +1.7 / +3.0 | +12.3 / +10.6 |
| Industrials / energy | −1.3 / +0.9 | −4.8 / −5.4 | −3.1 / −0.6 | +3.4 / −0.1 | −0.5 / +1.0 | −5.8 / −5.2 |
| KRE | +3.50% | −4.50% | −1.36% | +2.11% | +0.32% | −0.44% |
| HYG | −0.38% | −0.58% | −0.26% | +0.13% | −0.12% | −1.09% |
| HY OAS (bp) | 303 → 320 | 320 → 352 | 352 → 376 | 376 → 363 [11/23] | not posted | 303 → 363 |

The 11/12–11/19 window was broad and moved with credit (CPI, PPI, 10Y over 5%, hawkish minutes); 11/20 was the one-company shock; the trend since 9/21 is neither.

**Fresh HY-over-350-for-three-closes fires since 1997 (own calc, n=6; definition chosen in-session, unregistered; first version mis-excluded 2025-04-07 and was corrected, disclosed):** S&P +10 / +20 / +60 sessions median +1.85% / +1.85% / +3.4%, higher at 60 in 5 of 6; HY widening over the next ten sessions (1998, 2005) went with lower S&P at 20 sessions, narrowing (2021, 2024, 2025) with higher. 2024-08-06 is the only fire on a narrowing day.

## Forward view (unscored; nothing registered)

Base case narrow two-way range about 50%; credit-led broadening about 30%; V repair about 20%. Close under 7,037.04 by 12/4 about 35% (base 41%, n=115, closes since 1990 with VIX 23–30 and a 6–12% drawdown), by 12/16 about 45% (base 55%). HEN-65 current view about 5% (letter frozen 0.40). Changes my mind toward broadening: HY over 376 on a day RSP falls; KRE under $65; HYG under ~$75.50. Toward the V: HY ≤330 and falling with a close over 7,351 and ~7,440. A broadening letter is a candidate registration, not made tonight (named UNSCORED).

## Gaps

- FRED SP500, VIXCLS and HY for 11/24 not posted at 23:2x ET: the 11/24 grade is PROVISIONAL on vendor bars.
- ⚠️ Boot ran the default `--source auto`, which sent one request to Cboe (refusing this box since 11/20) before the vendor fallback; not worked around. Next session uses `--source vendor`.
- No instrument splits the HY widening by cause (REGINALD WQ-512 rider, LIQUID).
- Nvidia report date about 12/4 is from PROME's brief, unverified here.
- **Wed 11/25 08:30 ET October PCE is mine to log; no HENRY session is armed for it.** If PROME wants the print graded on the day, a re-spawn at the print is needed.
- Inbox drain follows in a second packet.

## Commits

- `eac0c8392f` — research record, STATUS (rotation ROT-11/24), MARKET_DATA 11/23–11/24, KB ML-HEN-243, TERRY packet `AGENTS/TERRY/inbox/2026-11-24_from-HENRY_credit-equity-two-clocks-reread.md`.
- This packet: its own commit (sha in the SendMessage receipt). Not pushed: PROME pushes.

## COMPLETION — HENRY — 2026-11-24
STATUS: ✅ DONE (items 1–4; drain follows separately)
CHANGED: AGENTS/HENRY/STATUS.md, STATUS_COLD.md, workbook/KB.tsv, workbook/MARKET_DATA.tsv, research/2026-11-24_credit-equity-read/ (7 files), AGENTS/TERRY/inbox/2026-11-24_from-HENRY_credit-equity-two-clocks-reread.md, this packet
RESULT: D:L1249 graded: 11/21 upside marker MET on FRED 11/23 (7,237.17, VIX 26.62), 11/24 held by 1.09 (vendor); 11/23 HY line NO VERDICT (363 in an unnamed 355–376 band, own defect). Credit and equity on two clocks: HY +97bp since 9/21 with equal-weight flat (+0.6%); the S&P's −7.90% is the chip complex (SMH −32.5%). Fresh-fire record n=6: S&P higher at 60 sessions in 5 of 6.
GAPS: FRED 11/24 cells not posted; HY cause split not instrumented; one Cboe request sent by default boot.
WILL_NEEDS: None.
FOLLOW-UP: PCE 11/25 08:30 ET is HENRY's to log, no session armed; FRED 11/24 confirm; TERRY re-read; HEN-65 resolves 12/4.
