# TRADE CARD — QQQ — Put DEBIT SPREAD (fade the unconsolidated V into overhead supply)

**Setup ID:** TRY-WILL-QQQ-VFADE · **Date:** 2026-08-03 ~11:10 ET
> ⚠️ **ID collision avoided:** `TRY-WILL-QQQFADE` is already owned by the **PARKED 7/30 card** (`WILL_qqq-downtrend-putspread_2026-07-30.md`, Sep-18 645P/620P). That card is **not dead** — see §4b, which reconciles the two rather than quietly duplicating it.
**Thesis owner:** ⚠️ **WILL** — this is Will's own tape read. **No domain agent has confirmed a QQQ short.** HENRY (market structure) and VIOLET (vol) have not been consulted and do not own this. Graded on structure and levels only; the directional call is Will's and is labelled as such throughout.
**Terry verdict:** 🔴 **DEAD (terminal) — VOID 2026-08-04, formally CLOSED 2026-08-13 (Will-directed, one day ahead of the 8/14 time stop).** Two independent kills fired the same day, 8/4: **① the hard condition breached** (three 0DTE QQQ puts opened alongside — the card's own terms: *"becomes the ONLY QQQ short or the card is void"*) and **② the 712 invalidation line was taken out.** Never approved, never armed, **`$0` at risk from build to death.** **Counterfactual measured at closure (11:59 ET live chain, QQQ 730.01): the 680/670 ×2 marks $0.08–0.10 vs the $2.26 build ⇒ an 8/3 approval would sit ≈−$432/−96% unmanaged; the pre-registered 712 kill would have cut it earlier at a partial loss — the kill line bounds the counterfactual too.** Closure record at end of card. *(was 8/3: 🟡 CONDITIONAL — CLEAN STRUCTURE, UNPROVEN THESIS; the expression was sound, entry rule-#6 clean, conditionality entirely §7.)*
**Confidence in trade structure:** High · **Confidence in thesis:** Not mine to grade.

---

## 1. One-line setup

Fade the **unconsolidated V-recovery** off the 7/29 low (656.30 → 697.55, +6.3% in ~3 sessions with no base) as it runs into the **700 round number and the Jul 22–24 congestion shelf at 704–712** — expressed as a defined-risk put debit spread with time to be early.

## 2. 🔴 THE FIRST QUESTION, ASKED BEFORE ANY LEVELS: is this the same trade that just lost $2,268?

**It has to be asked, because on the surface it is the sixth consecutive QQQ short in fifteen days.** Session-4's review (this morning) convicted the class: **seven short-dated QQQ put tickets since 7/20, ≈ −$2,268 realized**, four of them opened the same day the prior one died.

**The answer is that it differs on all four dimensions every prior ticket failed** — and if any one of them is dropped, it becomes the same trade in a longer costume:

| Failure mode in the 7/20→8/3 cluster | This card |
|---|---|
| **0–1 DTE** — needed to be right *today* | **18 DTE**, spans the 8/12 CPI |
| **No written invalidation** on any ticket | **§5 invalidation + time stop, written before the fill** |
| **Size 1.7–2.0× the cap** ($842, $1,014) | **$452 — under the $500 cap**, $48 dry |
| **Naked long premium**, full decay exposure | **Debit spread** — the short leg funds ~70% of the cost and sells the richer vol |

> **⛔ HARD CONDITION OF THIS CARD, and it is the one that actually matters:** if approved, **this is the ONLY QQQ short position.** No adds, no averaging down, and **no 0-DTE QQQ tickets alongside it.** The leak that cost $6,229 across three reviews is not "buying puts" — it is **running a second, undisciplined position beside a disciplined one.** If a day-trade QQQ ticket appears while this is open, this card is void by its own terms.

## 3. Entry

- **Trigger:** live now. **No trigger to wait for** — the entry condition (green tape) is satisfied at the moment of writing.
- **✅ ROOT RULE #6 — CLEAN, NO BREAK NEEDED.** QQQ is **+1.38% on the day (696.95 vs 687.99 Friday close)**. Buying puts on a green day is the rule, not an exception. *(Worth stating plainly: every ticket in the losing cluster was bought into weakness or into a same-day loss. This is the first one entered on the correct day-colour.)*
- **Preferred entry zone:** QQQ **695–705**. Better if it pushes into 700–705 first.
- **⛔ DO NOT CHASE below QQQ 690.** If QQQ has already rolled over, the spread reprices and the edge is gone — that is buying the move after it happened (leak #2, "post-move chase"). **If QQQ trades under 690 before a fill, this card is dead for today; re-quote tomorrow.**

## 4. Structure

**`BUY 2 × QQQ Aug-21-2026 680P / SELL 2 × QQQ Aug-21-2026 670P`**

| Leg | Strike | Bid | Ask | Mark | Spread% | IV% | OI |
|---|---|---|---|---|---|---|---|
| **BUY** | Aug-21 **680P** | 7.56 | 7.60 | 7.58 | **0.53%** | 23.12 | **74,488** |
| **SELL** | Aug-21 **670P** | 5.34 | 5.40 | 5.37 | **1.12%** | 24.43 | **29,044** |

*Live pull 2026-08-03 11:06 ET, QQQ spot 696.95. **Rule #4: re-pull before any fill.***

- **Net debit:** **$2.26** worst-case (buy ask / sell bid); **$2.21** mid-to-mid. **Enter as ONE spread ticket, limit at net debit. Never leg it.**
- **Cost:** 2 spreads × $226 = **$452.** `risk_calc.py --premium 2.26 --max-loss 500` → max 2 units, $48 unused. **Under the $500/card cap.**
- **Max value:** $10 wide × 2 × 100 = **$2,000** · **Max profit $1,548 · ~3.4:1**
- **Breakeven: QQQ 677.74 (−2.75%)** · **Max profit at QQQ ≤ 670 (−3.9%)**

### Why a spread, and why these strikes

1. **An outright put is not affordable and that is not a preference — it is arithmetic.** The Aug-21 690P costs **$1,047 per contract.** One contract is 2.1× the entire card cap. Every unspread expression of this view is off-budget.
2. **The skew pays you to spread it.** Downside IV runs **24.96% at 665 vs 20.67% at 700** — a ~4.3-vol downside skew. The short 670 leg therefore **sells richer vol than the long 680 leg buys**, which is the structural argument for a debit spread over an outright and it is measured here, not asserted.
3. **Both legs are among the most liquid on the board** — 74,488 and 29,044 OI, spreads of 0.53% and 1.12%. Slippage is negligible, which matters on a 2-lot.
4. **The strikes bracket the standard retracement targets.** Breakeven **677.74 sits essentially on the 50% retracement (676.9)** of the 656.30→697.55 bounce; max profit at **670 ≈ a 65% retrace.** Neither requires a new low. *(A full retest of 656.30 pays the same $2,000 — the spread caps at 670, which is the deliberate trade-off for affording the position at all.)*

## 4b. ⚠️ The PARKED 7/30 card — its park condition has just been DISCHARGED, and I am not quietly duplicating it

`WILL_qqq-downtrend-putspread_2026-07-30.md` (**Sep-18 645P/620P**) was parked 7/30 with this reason on its own face:

> *"Will's stated view was explicitly about **today** … TERRY built this 7-week card against a durable macro thesis **Will never claimed** … **Retained on file in case Will ever wants the durable expression.**"*

**Will has now asked for exactly that** — a swing expression, in his own words, off a two-week chart. **The park reason is spent.** So this card must justify itself against the one already built rather than pretend it doesn't exist.

| | **Parked 7/30 card** | **This card** |
|---|---|---|
| Structure | Sep-18 **645P/620P** | Aug-21 **680P/670P** |
| Moneyness | −7.4% / −11.0% | −2.4% / −3.9% |
| What it needs | a **crash** (QQQ under 645) | a **normal retracement** (QQQ 677) |
| Payoff shape | cheap, high-convexity, low probability | nearer, lower-multiple, higher probability |

**Ruling: build new, and the reason is that Will's stated view changed shape.** On 7/30 the premise was a directional call about a single day. Today it is *"things have been volatile, a negative move isn't out of the question,"* anchored on an **unconsolidated V into overhead supply** — that is a **retracement** thesis, not a crash thesis. **645/620 is priced for a crash and would expire worthless on a textbook 50% give-back of the July bounce**, which is precisely the move Will described.

**The 645/620 card stays PARKED and available** — if Will's view is actually "the July low breaks," that card is the better vehicle and this one is wrong. **The two are alternatives, not a ladder. Do not run both.**

*(Registry defect found while checking this: the 7/30 card is **absent from `setups/INDEX.md` entirely** — a live parked card invisible to the master registry since it was built. Both cards are being added in this session's write-back.)*

### Rejected

- **Outright 690P/685P:** $1,047 / $898 per contract — off-budget (above).
- **Aug-21 685/665 ($454):** only 1 contract fits ⇒ **no ability to harvest half** (§6). Rejected on manageability.
- **Sep-18 tenor:** more room, but 18 DTE already spans the only dated catalyst in view (8/12 CPI) at the halfway point — good structure: half the tenor before the event, half for follow-through. Extra premium not justified.
- **0-DTE / weekly anything:** see §2.

## 5. Risk

- **Max loss budget: $452 (100% of debit).** Defined risk, no margin, no assignment risk if closed before expiry.
- **🔴 Invalidation — THESIS:** QQQ **closes above 712** (the top of the Jul 22–24 congestion shelf). That shelf is the entire structural basis of the trade; through it, the overhead-supply argument is refuted and the V-recovery is a genuine trend reversal. **Exit on the close, do not wait for expiry.**
- **🔴 Invalidation — TIME:** if QQQ has **not traded below 685 by the 8/14 close** (two sessions after CPI), the catalyst has passed without delivering. **Exit for whatever it is worth.** A swing thesis that hasn't started working in two weeks is wrong.
- **⛔ HARD STOP (desk-card rule, and this one gets executed):** spread marks **≤ $1.10** (−50%) ⇒ **close it.** No "it's cheap now, let it ride" — that is verbatim the reasoning behind the −$6,229 leak.
- **Gap/event risk:** an upside gap on Iran-deal headlines. **Negotiations reportedly begin this afternoon** — a live, dated, two-way catalyst inside the position's first session. A spread caps the damage at the debit; an outright would not.

## 6. Target / management

- **★ MANDATORY PROFIT HARVEST (`NO_HARVEST_RULE`, Will-ruled fleet-wide 7/31):** spread marks **≥ $4.52 (2× the debit)** ⇒ **SELL ONE OF THE TWO SPREADS IMMEDIATELY.** Not conditional on the target, not conditional on CPI, not conditional on anything. **This is why the card is sized at 2 and not 1** — a 1-lot cannot obey this rule.
- **T1:** QQQ **677.74** (breakeven / 50% retrace).
- **T2:** QQQ **≤ 670** ⇒ spread at max **$2,000** (~3.4:1). **Close at ≥$9.00 rather than grinding the last dollar into expiry** — the final 10% of a debit spread's value is the slowest and least certain part.
- **Review cadence:** daily at the close while open; hard checkpoints **8/12 (CPI)** and **8/14 (time stop)**.
- **Roll rule:** **NONE PRE-REGISTERED.** Any roll requires fresh Will approval from scratch (Non-Negotiable #6, no roll-by-hope).

> **`NO_HARVEST_RULE` build-time check — Q: is there a path where this is profitable and NO trigger fires?**
> **YES.** QQQ drifts to 682–685 over the next week: the spread marks up meaningfully, but **no** target is hit, the 712 invalidation is untouched, and the 8/14 time stop hasn't landed — a profitable position with no exit rule, decaying into expiry. **The 2× harvest above closes it.** Trigger-variable check: keyed to the position's own mark, which the profit zone reaches by definition. ✅ Valid.

## 7. Why not / counter-trade — the best case against

**Stated at full strength, because §2 makes this the card that most needs it:**

1. **🔴 The thesis has no owner but Will.** No domain agent has been asked, and my morning read of the intraday chart said the opposite — price above all MAs and VWAP, fresh MACD cross with an expanding histogram, dip bought on heavy volume. **A momentum breakout is not usually a good short.** That intraday evidence has not been refuted; the two-week structure is a *different, slower* argument sitting on top of it. **Both can be true, and the fast one is currently winning.**
2. **The capitulation-volume problem.** The 7/29–30 low printed on a genuine volume spike. Capitulation lows tend to *hold*. If 656.30 was a real washout, fading the recovery is fading a durable base.
3. **"Unconsolidated" cuts both ways.** V-recoveries that don't consolidate are fragile — but they also frequently *keep going* precisely because nobody who wanted in got a pullback to buy.
4. **Effective-N:** the live book already carries **KRE/WAL/OZK bank puts** — a QQQ short is not fully independent of them; both are paid by broad risk-off. **N_eff += ~0.5, not +1.** Sizing at $452 (~1.1% of the ~$39.5k book) is appropriate for a half-vote.
5. **Timing risk is dated and adverse:** deal negotiations reportedly begin **this afternoon**, and the tape has spent the morning rewarding de-escalation headlines.

**The honest summary: this is a well-built expression of a view I cannot corroborate.** If Will wants the exposure, this is the right way to own it. **If he is neutral on the view, the correct answer is no trade** — a clean NO is a good outcome, not a failure to find a way.

## 8. Decision

> **BUY 2 × QQQ Aug-21-2026 680P / SELL 2 × QQQ Aug-21-2026 670P**
> **@ $2.26 net debit limit (one spread ticket, never legged) — $452 at risk, max loss $452, max value $2,000.**

**Pre-fill checklist:** ① re-pull the chain (rule #4) · ② confirm QQQ still ≥690 (§3 no-chase) · ③ confirm the 8/12 CPI date · ④ accept the §2 hard condition — **this becomes the only QQQ short.**

**APPROVAL REQUIRED — Will must approve/reject before execution.**

---
*Built 2026-08-03 ~11:10 ET on live marks, barred from use at fill. Thesis is Will's and is not corroborated by any domain agent — see §7.*

---

## CLOSURE RECORD — 2026-08-13 ~12:00 ET (Will-directed, one day ahead of the 8/14 time stop)

**DEAD (terminal). VOID since 2026-08-04 on two independent kills, both that day:**

1. **Hard-condition breach:** three 0DTE QQQ puts (693P ×2 / 698P ×2 / 712P ×1) opened alongside on 8/4 — the card's own terms said *"becomes the ONLY QQQ short or the card is void."* Voided independently of price.
2. **Price invalidation:** the 712 line (Jul 22–24 shelf) was taken out the same day.

Never approved, never armed, `$0` at risk from build to death. The 8/14 time stop was never reached; it is closed a day early because there was nothing left for it to time-stop.

| | Build 8/3 | Closure 8/13 11:59 live |
|---|---|---|
| QQQ | ~697 | **730.01** (+4.7%) |
| 680P/670P ×2 | $2.26 debit ($452) | **$0.08–0.10** (680P 0.26/0.28 · 670P 0.17/0.18) |

**Counterfactual: an approved 8/3 fill sits ≈−$432 / −96% unmanaged; the pre-registered 712 kill would have exited earlier at a partial loss — the kill line bounds even the counterfactual.** Every control on this card fired exactly as written; the card's value was that it defined the loss before asking for one.

**Ledger note:** this card is `RISK_RULES` #16's worked example (the $452 defined-risk twin of the ≈−$4,341 0DTE cluster — same view, 9.6× cost difference from tenor and frequency alone). Postmortem: `POSTMORTEMS.md` 2026-08-13.
