# QQQ DESK CARD — Will's standing pre-trade reference

**Built:** 2026-06-24 (TERRY, from the 5/1–6/23 CSV: 116 closed QQQ trades, 57% win, PF 1.36, **+$3,044**)
**Use:** Glance at this BEFORE entering any QQQ option. It's the rulebook for the one book that makes your money. TERRY refreshes it each review as the sample grows.

> **Prime line:** Your QQQ edge is *buying puts into weakness.* Everything else is either churn or a leak. Protect the edge; cut the rest.

---

## The 5 checks (run in order, every entry)

**1. Which side?  → Puts are the edge. Calls are guilty-until-proven.**
- Puts: 62 trades, **61% win, +$2,232**. Calls: 54 trades, 52% win, **+$812** (and most of your bleed).
- A QQQ **call** is only allowed when you're *reacting to an up-move already on the tape* with a written exit. Not a bounce-guess, not a top-tick. If you're forcing a call, the honest answer is a put or **no trade**.

**2. Both-ways is a CHOP tactic, not a default.  → Only on a range read, and the call leg is junior.**
- The numbers clear it: both-ways days were **net +$1,151, 62% day-win-rate** (vs 53% one-way). On a genuine range/chop tape, playing both sides catches the oscillation — keep it.
- **BUT inside those days the put legs made +$1,292 and the call legs LOST −$141.** "Both ways works" = your puts work and the calls ride along negative. So: **size the call leg ≤ the put leg** — it's the scalp/hedge half, not a profit center.
- **It loses on TRENDING days** — both-ways losers were wrong-leg-into-a-move (6/22: puts +192, calls **−407**, buying calls into the high before the crash). If the tape is trending, pick the side; both-ways is for range, not for "I don't know."

**3. Size.  → 1R = $250. Hard cap 2R = $500 per idea.** ✅ **RATIFIED BY WILL 2026-08-04** *(was "empirical default — confirm w/ Will" since June; this was the desk's longest-open blocker and Rule 3 was unenforceable without it).*
- **THE UNIT IS DOLLARS. `1R ≡ $250` is a fixed dollar anchor — not a percentage of the book, and not a stop-distance.**
  - **Not %:** a % target silently re-sizes as the book moves, so the rule would change without anyone deciding to change it.
  - **Not classic R:** classic R is distance-to-stop, and a long option held toward zero has no stop — its max loss *is* the premium. R here is shorthand for $250, nothing more.
  - **Consistent with the thesis book**, which states every max loss in $ and caps cards at $500.
- Your median bet is $233, your 90th-percentile is $370. Anything north of $500 is off-pattern.
- MRVL at $1,300 was 5R and is the cautionary tale. No single QQQ idea breaks the cap.
- **🔴 THE CAP IS ALREADY BEING BROKEN, and ratifying the unit is what makes that visible:** the **8/3 687P ×3 = $843 = 3.4R** · the **7/30 ticket = $1,431 = 5.7R**. Average realized loss across the 7-ticket review was **~$324/ticket = 1.3R**. **$500 is a real constraint here, not a rubber stamp.**

**4. Define the loss BEFORE the fill.**
- Written invalidation (level or % of premium) + a time-stop. If you can't state the loss, it's not a trade.

**★ 4b. DEFINE THE *PROFIT* BEFORE THE FILL — NEW 2026-08-04, and it is the rule this card was missing entirely.**

> **This card had FIVE loss-side checks and ZERO profit-side lines.** The 8/3 687P was **+23.6% at Friday's close** and **no rule on this card said take it.** It closed near-worthless. **Identical root cause to `TRY-VIOLET-VIXCS`** (−$111.60, every management trigger keyed to the move going *further*, none keyed to being in profit) — which is why `NO_HARVEST_RULE` is now fleet-wide (Will-ruled 7/31, `RISK_RULES.md` durable finding #9). **The day desk was the last surface without it.**

> **P1 — NEVER carry a short-dated option (≤3 DTE) through a non-trading gap while in profit without taking at least half.** If it is **≥+20%** into a weekend/holiday close, **sell at least half.** *(Threshold set at the observed case: the 687P cleared it at +23.6% and was carried anyway.)*
> **P2 — +50% on premium ⇒ sell at least half, immediately.** Not conditional on a further move. Not conditional on a level.

**Why this is not "cutting winners":** the data says you already cut winners in minutes. The failure is the opposite — the tickets you *hold* have no profit-side exit, so a winner that isn't taken in minutes has no other way out but zero. **P1/P2 govern the held ones only.**

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

⏸️ **PARKED 2026-08-04 (Will-decided) — REVIVABLE, not abandoned.** The order-level export has been an open ask since June and has not arrived. **Rather than carry it as a permanently-open item, both dependent findings are marked UNRESOLVABLE-WITHOUT-EXPORT and stop being tracked as live questions.** They revive the day the file exists — *the blocker is the PATH, not the data.*

- **Intraday timing** (no timestamps in the export) — can't tune open-vs-midday-vs-close behavior. `[UNRESOLVABLE-WITHOUT-EXPORT]`
- **IV/theta paid** on 0DTE entries (no option chain) — can't tell if you're overpaying for the scalps. `[UNRESOLVABLE-WITHOUT-EXPORT]`
- **Churn / cancel cost** — the CSV has no cancels, so `cancel_rate_pct` and `both_ways_rt` sit at `UNK` in every LEDGER row. `[UNRESOLVABLE-WITHOUT-EXPORT]`
- **🔴 The RH 0DTE auto-liquidation trap — the costly one.** On 6/26 a forced close of the 709P at ~$19 preceded a ~$346 settlement ≈ **$327 lost on a single ticket.** Whether that was broker auto-liquidation or a manual exit **cannot be established from the CSV.** `[UNRESOLVABLE-WITHOUT-EXPORT]` — and if it *was* auto-liquidation, it is a standing execution risk on every 0DTE ticket, not a one-off.

**To unlock all four:** an **order-level export including cancels and timestamps** (not the positions/activity CSV). One file, revives everything above.

*Source data + method: `daytrading/JOURNAL.md` Session 2, `scripts/csv_pnl.py`.*
