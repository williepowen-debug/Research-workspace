# QQQ DESK CARD — Will's standing pre-trade reference

**Built:** 2026-06-24 (TERRY, from the 5/1–6/23 CSV: 116 closed QQQ trades, 57% win, PF 1.36, **+$3,044**)
**Use:** Glance at this BEFORE entering any QQQ option. It's the rulebook for the one book that makes your money. TERRY refreshes it each review as the sample grows.

> **Prime line:** Your QQQ edge is *buying puts into weakness.* Everything else is either churn or a leak. Protect the edge; cut the rest.

---

## The 5 checks (run in order, every entry)

**1. Which side?  → Puts are the edge. Calls are guilty-until-proven.**
- Puts: 62 trades, **61% win, +$2,232**. Calls: 54 trades, 52% win, **+$812** (and most of your bleed).
- A QQQ **call** is only allowed when you're *reacting to an up-move already on the tape* with a written exit. Not a bounce-guess, not a top-tick. If you're forcing a call, the honest answer is a put or **no trade**.

**2. One direction only.  → No "both ways."**
- You bought a QQQ call *and* a put on the same expiry on **17 separate days** this month — paying two spreads + double theta to be neutral. That's "I don't know," not a trade.
- If you can't name the direction, **don't enter.** A real event-straddle is allowed only as ONE deliberately-sized, time-stopped structure — decided in advance, not legged into out of indecision.

**3. Size.  → 1R = $250. Hard cap 2R = ~$500 per idea.** *(empirical default — confirm w/ Will)*
- Your median bet is $233, your 90th-percentile is $370. Anything north of ~$500 is off-pattern.
- MRVL at $1,300 was 5R and is the cautionary tale. No single QQQ idea breaks the cap.

**4. Define the loss BEFORE the fill.**
- Written invalidation (level or % of premium) + a time-stop. If you can't state the loss, it's not a trade.

**5. Match tenor to the read.**
- **Conviction put-into-weakness → 1–3 DTE, size toward 2R.** This is the engine: +$3,352 on 17 trades (~$197 each), incl. your 3 biggest wins (735P +1,522 / 722C +1,173 / 726C +687).
- **0DTE scalp → keep it small.** +$1,584 on 93 trades is only ~$17 each — thin yield for high effort. Trade it lighter and less; put the effort into the swing setups.

---

## ⛔ THE HARD STOP — No-Hold-to-Zero

**6 QQQ options walked to $0 expiry cost −$1,892 this month (4 of them calls).** You cut winners in minutes; you must cut losers the same way. This is mechanical, not discretionary:

> **A QQQ option is DEAD — sell the residual or eat the loss NOW, never hold to expiry — when ANY of:**
> - it's **down ≥60%** from your entry, OR
> - **<60 minutes** to expiry and still **OTM**, OR
> - your written **invalidation level** has printed.

No "let it run to zero to save the spread." No "maybe it comes back." The expiry bleed is the only behavior the data actually convicts — this rule kills it.

---

## Do-not-chase reminders
- Don't buy the **call** at the high of an up-day (745C/746C on 6/22 = walked to ~zero).
- Don't buy premium **after** a >2% index move — you're paying peak IV in the direction of a move already made (Rule 2 of the master rulebook).
- Don't average a losing QQQ contract past the 2R cap "to fix the basis."

## What this card can't see yet
- **Intraday timing** (no timestamps in the export) — can't tune open-vs-midday-vs-close behavior.
- **IV/theta paid** on 0DTE entries (no option chain) — can't yet tell if you're overpaying for the scalps.
- Pull an order-level export (with cancels) and an option-chain export to unlock both.

*Source data + method: `daytrading/JOURNAL.md` Session 2, `scripts/csv_pnl.py`.*
