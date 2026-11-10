# The HYG hedge, explained — for Will

**Written:** 2026-11-09 22:30 EST (from `date`) by TERRY, on Will's 2026-11-09 22:27 ET instruction relayed by PROME (prome-1e). Explanation only: no rule, threshold or card term is changed, no new card, no order. Markets are closed; there is no live option quote in this note.

## The whole story

The approved card (WQ-615 A) is a five-contract bet that junk bonds fall between now and mid-January. It costs at most $306.50 and pays at most $1,193.50. It was built on November 5 to protect against one thing: the stock selloff spreading into the junk-bond market. It was never designed to protect against the stock selloff itself.

Both timing rules were met on Monday: credit confirmed on Friday, and HYG was up on Monday (11/9) at 09:32 ET and at the close. The desk did not watch it in between. What stood between the card and an order on Monday was not a rule. It was the price: the desk's data feed showed no quote for the options, so only your broker screen can say whether the spread costs $0.60 or less. The order itself is your hand. The desk has no record of a fill.

My judgment on fit: the credit trigger fits the job the card was built for. The green-day rule fits it poorly: on HYG it saves a cent or two and costs days. If what you wanted was protection against the stock drop itself, this card is the wrong tool. Redesigning it is your decision, not mine.

## What it is

| Item | Figure |
|---|---|
| What you buy | HYG January 15, 2027 puts: buy the $76 strike, sell the $73 strike, 5 times (one order, never in pieces) |
| Most you can lose | $306.50 at the $0.60 price cap, fees included |
| Most it can pay | $1,193.50, if HYG is at or below $73 on January 15 |
| Break-even at expiry | HYG $75.39, about 2.7% under Monday's close of $77.51 |
| Plan for taking profit | Sell when the spread bids $1.50 or more: about +$437 after fees |
| Plan for getting out | Sell if junk-bond spreads ease back to 330 or below for 5 days running; sell by the close on Friday January 8 at the latest |

HYG is a fund that holds junk bonds. When investors start to doubt weaker companies can pay their debts, those bonds fall and HYG falls with them. That is the risk this card pays on.

⚠️ **"Hedge" is a loose word here.** The card measures no link to anything you own. In the record it shares the same cause as your bank and private-credit puts: if credit breaks, they all pay together. So it adds to that bet more than it offsets a loss elsewhere.

⚠️ **History says junk bonds tend to dip and recover.** In 14 past episodes where stocks fell 3% or more while HYG held up, HYG later dipped 3% or more within about ten weeks in 10 of them, but finished that stretch down 1.4% or more in only 4 (TERRY research, 11/5). That is why the plan sells into a dip at $1.50 rather than holding to January. No win rate is claimed.

## When protection can begin

Only after a fill. Four things have to line up, and they are of different kinds:

| Condition | Kind | State tonight |
|---|---|---|
| Junk-bond spreads above 344 on one day (the high of this episode) | **Rule condition** | **Met.** 348 for Nov 5, published Friday Nov 6 at 10:09 ET. It cannot un-fire. The Nov 6 reading eased to 342, which does not cancel anything (cancel needs 330 or below five days running; count 0 of 5) |
| HYG up on the day when you buy | **Rule condition** | **Met Monday** at the two reads the desk has: $77.42, +0.24%, at 09:32 ET, and the close $77.51, +0.36% (vendor daily bar, read 22:28 ET). Tuesday's colour is unknown; CPI comes out at 8:30 ET Tuesday, before the open. Window runs to Friday December 4 |
| Spread costs $0.60 or less | **Missing broker quote** | **Unknown.** On Monday the desk's feed showed 0.00 / 0.00 for all four HYG January options at three pulls (09:32–09:33 ET), so no price was computed. ⚠️ The desk pulled only in the first two minutes after the open and then closed for the machine switch; a later pull might have shown a price. Last real screen: Friday 10:09 ET, $0.345 mid / $0.44 at the worst side, three sessions old |
| Placing the order | **Your decision** | The card is approved; the order is always your hand. TERRY reported Monday's entry day to PROME at 09:34 ET; whether it reached you is PROME's record, not mine |
| Knowing whether it filled | **Missing fill evidence** | No fill known. The position mirror has no HYG line. If you placed it, the desk needs your word or a screenshot to book it |

## Why the two waiting conditions exist

**Credit confirmation.** On November 5 stocks sold off hard, but junk bonds barely moved: HYG fell only 0.31%. Nobody had shown the selloff was a credit problem; one read (VIOLET) said it was crowded stocks unwinding, not credit. The trigger makes the card wait until junk-bond spreads actually widen, so you do not pay for credit protection when credit is calm. The cost of waiting is that you buy after the first move. Here that cost has been small: HYG is higher now ($77.51) than when the card was written ($77.14).

**The green day (root rule #6: puts on green days).** Puts are usually cheaper on a day the underlying rises, so the rule is a quick check against overpaying. On HYG it is a weak check. HYG moves a few tenths of a percent a day. From the card's own screens: on Nov 5 at $77.14 the spread was $0.365 at mid; on Nov 6 at $77.29 it was $0.345. HYG was 15 cents higher and the spread was 2 cents cheaper, about $10 across five contracts. The gap between the bid and the ask on the $76 put alone was 8 to 11 cents. On this fund the rule saves less than the cost of crossing the spread, and it can cost whole days.

## Do the conditions fit the protection you want?

| If the job is… | Fit |
|---|---|
| Pay out if the stock selloff spreads into junk bonds | **Fits.** The credit trigger is the right gate for that job, and waiting has cost little so far |
| Protect against the stock selloff itself | **Does not fit.** The card was written after the first drop and waits for credit to move. It cannot protect against a stock-only decline |
| Get the protection on at a fair price without losing days | **Green-day rule fits poorly** on HYG: about $10 saved against days of delay. It was not what blocked an order on Monday |

That is where I stop. A different design, or dropping the green-day rule for this card, is your decision.

## The older HYG card (WQ-513 A), for comparison

Approved October 23: HYG January 77/74 puts, 4 contracts, at most $1.00 each, most you can lose $405.20. It waits for a stricter trigger: spreads above 350 on three published days in a row. The highest reading so far is 348; the latest is 342; count 0 of 3. Its window ends Friday November 13, so it can fire only if the next three readings all clear 350. It has not fired. ⚠️ If both cards end up filled, the pair can lose up to $711.70 on the same idea, past your usual $500 per idea; the second one would need your word at that moment.

## Sources

- Card: `AGENTS/TERRY/setups/HYG_jan15-76-73P_credit-follows-hedge_2026-11-05.md` (WQ-615 A; record `PROME/proposals/2026-11-05_wq614-617-RULED.md`)
- Older card: `AGENTS/TERRY/setups/CREDIT_hyg-jan15-77-74P_or_htgc-16P_REG-T-04_2026-10-23.md` (WQ-513 A)
- Monday 11/9 open: `AGENTS/TERRY/research/2026-11-08_wq650-pass/IDEAS.md` § 4b and `live_1109.txt` (commit 063e542caf)
- HY 342 [11/6]: PROME commit f6bf10391c (dashboard pull 2026-11-09 10:33 ET)
- HYG 11/9 close $77.51 +0.36%: `FORGE/tools/market-data/fetch.py price HYG`, vendor daily bar, read 2026-11-09 22:28 ET
- Dip-and-recover history: `AGENTS/TERRY/research/2026-11-05_selloff-read/NOTE.md`
- Background only, not relied on: CATO `AGENTS/CATO/runs/2026-11-09_2050_process-value-review.md` § PV3
