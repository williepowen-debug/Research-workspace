# TRADE CARD — QQQ — Sep-18 645P / 620P PUT DEBIT SPREAD
**Card ID:** `TRY-WILL-QQQFADE`
**Date:** 2026-07-30 (built ~11:20 ET, market open, live marks stamped inline)
**Thesis owner:** **WILL** — his own directional read (*"I do not buy the upswing of the market today"*). ⚠️ **NO domain agent has confirmed this thesis.** TERRY does not own thesis (HARD BOUNDARY #3). See §7 for a live fleet-internal conflict.
**Terry verdict:** ⏸️ **PARKED 2026-07-30 ~11:40 ET — Will-directed. DO NOT ACTION.**
> **Why parked:** Will's stated view was explicitly about **today** (*"I do not buy the upswing of the market today"*), and he holds 0–1 DTE instruments that **correctly match that horizon.** TERRY built this 7-week card against a durable macro thesis **Will never claimed** — importing the morning's VIXCS "right thesis, wrong tenor" lesson as a lens rather than testing it as a hypothesis. **The tenor critique that motivated this card was not valid.** Retained on file in case Will ever wants the durable expression; **it answers a question he did not ask.**
>
> *Prior verdict (superseded): 🟡 CONDITIONAL — structure clean and the tenor fix real, but the thesis premise Will stated is NOT the one the data supports, and I re-based it before building (§0). Conditional on Will accepting the re-based premise.*
**Confidence in trade structure:** **Medium-High** (structure/liquidity/sizing) · **Medium** (thesis, un-confirmed by any owner)

---

## 0. ⚠️ READ FIRST — I MEASURED YOUR PREMISE AND HAD TO RE-BASE IT

**You said the rally is narrow and you don't buy it. I checked, and the "narrow rally" version of that argument is REFUTED over every window except today.**

| Window | QQQ | QQQE (equal-wt NDX) | Gap | SPY | RSP (equal-wt SPX) | Gap |
|---|---|---|---|---|---|---|
| **Today** | **+2.66%** | **+0.07%** | **+2.59pp** | +0.81% | **−1.18%** | +1.99pp |
| 5d | −1.94% | −0.50% | **−1.44pp** | −0.42% | +0.62% | **−1.04pp** |
| 10d | −3.89% | −2.39% | **−1.50pp** | −2.09% | −0.85% | **−1.24pp** |
| 21d | **−7.86%** | −5.26% | **−2.60pp** | −1.57% | +0.22% | **−1.78pp** |

**Today is the ONLY window where cap-weight beats equal-weight.** Over 5/10/21 days the megacaps have been the **laggards** and breadth has been *better* than the index. **"Unhealthy narrow melt-up" is not what is happening** — that thesis would have cost you money for a month.

**THE RE-BASED PREMISE — and it is a stronger argument than the one you gave me:**

> **QQQ is in an established downtrend and today is a one-stock earnings bounce.**

| Evidence | Figure |
|---|---|
| QQQ 7/29 close → now | **661.73 → ~678.5 (+2.5%)** |
| Drawdown from 6mo high (745.34, 6/2) | **−8.97%** |
| vs 20d MA / 50d MA | **702.01 / 714.91 — below BOTH** |
| Lower highs since 7/15 | 717.74 → 708.97 → 705.35 → 691.96 → 684.23 → 682.12 → 675.49 → **661.73** |
| Today's move, attribution | **MSFT +14.02%** (Azure +43% cc vs 40.2% est) vs **META −8.09%** — a dispersion/earnings event, not broad risk-on |

**Shorting a one-stock bounce inside a confirmed downtrend is a far more defensible setup than shorting a narrow melt-up.** ⚠️ **But it is a different trade than the one you described, and you should approve the premise, not just the ticket.**

---

## 1. One-line setup
Buy a defined-risk put spread on QQQ to express *"the 7/15→7/29 downtrend resumes and today's MSFT-driven bounce fails"* — **with 50 days of life instead of 0–1**, which is the entire point of rebuilding this.

## 2. Preconditions (all must hold at fill)
- ✅ **Downtrend intact:** QQQ below the 20d MA (702.01). *Currently 678.5 — holds.*
- ✅ **Rule #6 (root) — puts on a GREEN day:** QQQ **+2.5%** today. **Clean, no break required.**
- ✅ **Liquidity:** both legs OI >7,000, quoted spreads <1.5%.
- ✅ **Cap:** net debit ≤ **$4.90** → ≤$495 all-in, inside the standing **$500/card** limit.
- ❌ **What must NOT be happening:** QQQ reclaiming the 20d MA (702) on a *closing* basis, or RSP/QQQE flipping to sustained **under**performance (that would mean breadth is *narrowing* into strength — a different, bullish-blowoff regime this card is not built for).

## 3. Entry
- **Trigger:** none required — this is a **discretionary, Will-directed entry**, not a fired trigger. ⚠️ **Flagging the standing rule it departs from:** *"fresh capital deploys ONLY on a fired trigger (Will 2026-06-26)."* **Your call to override; I am naming it, not hiding it.**
- **Preferred entry zone:** **now**, on today's green tape.
- **★ The real entry trade-off, stated plainly:** for a put *buyer*, **a higher QQQ is a cheaper entry.** If this bounce extends toward the **20d MA at 702** (+3.5%), the identical spread gets materially cheaper. **Waiting is a better price but requires a second forecast** (that the bounce extends). I recommend taking today's clean green day rather than layering forecasts — but the patient alternative is legitimate and its exact terms are: *work the same spread only if QQQ trades 695–705, cap $4.20.*
- **Do NOT chase:** **do not pay above $4.90 net debit.** If it will not fill at $4.90 — **no trade.** No exceptions, no "just this once."

## 4. Structure

**Instrument:** QQQ **Sep-18-2026** **645 Put** (long) / **620 Put** (short) — vertical put **debit** spread, 25 wide, **1 contract**.

**Live marks — QQQ spot 678.51, pulled 2026-07-30 11:17 ET (`chain_fetch.py`, re-pull before filling per rule #4):**

| Leg | Bid | Ask | Mark | Spread% | IV% | OI | Vol |
|---|---|---|---|---|---|---|---|
| **645P (buy)** | 12.78 | 12.89 | 12.84 | 0.86% | 26.69 | 7,201 | 252 |
| **620P (sell)** | 7.97 | 8.08 | 8.03 | 1.37% | 29.15 | 40,484 | 344 |

**Net debit bracket:** aggressive **$4.70** · **mid $4.81** · worst-case **$4.92**

**Order (per the rule I adopted THIS MORNING — §11.D-2 of the VIXCS card):** open in the **aggressive third** of the bracket. For a *buyer* that is the **low** end.
- **Open $4.75**, walk **up** $0.05 every ~5 min → 4.80 → 4.85 → **hard cap $4.90.**
- Single spread order, net **debit** limit, **never leg it, never market.**

**Why this expression beats the alternatives:**
| Alternative | Why rejected |
|---|---|
| **0–1 DTE QQQ puts (what you own)** | The documented failure. A macro view cannot be expressed in instruments that expire before the view can play out. |
| Outright Sep 645P (~$1,289) | 2.6× the risk cap, and pays full freight on **26.7% IV**. |
| Deeper spread, e.g. 610/595 (~$180) | 🔴 **The book's known leak.** BE would be −10.4% = a *crash* bet on a *trend* thesis — the exact error diagnosed 7/17 (*"slow-GRIND thesis expressed with CRASH instruments"*; KRE 60P = 0% empirical 3y reachability). **Refused.** |
| 650/625 (~$5.16 mid) | Better BE (640→645) but **$516 breaches the $500 cap.** |

**★ Vega note (why IV level matters less than you'd think):** the short 620P carries **higher IV (29.15) than the long 645P (26.69)** — put skew. A debit spread is therefore near **vega-neutral to mildly vega-short**, so an IV crush after tonight's prints is roughly **neutral, not harmful**. **This is why I am not telling you to wait for event vol to bleed out** — with an outright it would matter; with this spread it largely offsets.

## 5. Risk
- **Max loss budget:** **$490 + ~$5 fees ≈ $495** — the full debit. Inside the $500/card cap. Defined risk, no stop needed, cannot lose more.
- **Invalidation — three, any one closes it:**
  1. **Price:** QQQ **closes above the 20d MA (702.01)** → the downtrend premise is broken.
  2. **Thesis:** **breadth narrows into strength** — QQQE/RSP sustainedly *under*performing their cap-weight versions over 10 days (i.e. today's one-day pattern becomes the regime). That would mean a concentration blowoff, which this card is not built for.
  3. **Time:** **2026-09-04** — if QQQ has not broken below **655** by then, the move has not started, ~2 weeks remain, **salvage what is left.** No expiry drift.
- **Gap/event risk:** **AAPL + AMZN report after today's close** (⚠️ **"~15% of QQQ combined" is UNVERIFIED — asserted from memory, never checked against the fund's holdings file. Flagged in the 7/30 self-audit. Verify before this figure is used in any decision; the *direction* of the risk stands regardless, both are top-5 holdings.**) and **BOJ is 7/31.** A strong AAPL/AMZN print gaps QQQ up and this spread opens tomorrow worth less. **That risk is real and it is the price of entering today rather than Friday.**
- **⚠️ You are long 15 AAPL shares ($4,977) into tonight's print** — so this position is a *partial* hedge to your own stock. Intended or not, it is now true.

### ★ EFFECTIVE-N — independence audit
**N_eff = 1.** One view: *NDX declines.* Today's breadth split, the MA structure, and the lower-high sequence are **one trend observation seen three ways, not three votes.**

**🔑 The book-level point that matters most — this does NOT double your bearishness, and may partially cancel it:**
> **`TRY-FIRE-004` (TLT Sep-30 77P) pays on yields UP. This card pays on equities DOWN.** In a **classic flight-to-quality selloff**, equities fall *and bonds rally* → TLT **up** → **004 dies while this wins.** They only pay **together** in a **yields-up / stocks-down** regime (2022-style). **Do not read "QQQ puts + TLT puts" as two bear bets — read it as two different regimes, one of which kills the other.** That is genuine diversification, not conviction stacking, and it is the honest frame.

## 6. Target / management
- **Target 1 — QQQ ~645 (−4.9%, BE zone):** spread ≈ **$10–11** → **+105% to +130%. Take HALF.** *(1 lot cannot be halved — see the sizing note; with 1 contract this becomes "take it all at Target 1 or hold for Target 2," a binary you should decide **now**, not in the moment.)*
- **Target 2 — QQQ ≤620 (−8.6%):** approaching max value. **Close.**
- **Realistic payoff, stated honestly:** on a genuine 5–8% continuation, **+100% to +250%.** ⚠️ **The 4.2:1 headline requires holding to 9/18 expiry below 620 — do NOT anchor on it.** (Same discipline as the VIX card, where the advertised ratio was never collectable.)
- **Breakeven at expiry: QQQ 640.19** — **−5.6% from here, but only −3.3% below the 7/29 close of 661.73.** *That is a normal continuation of an existing downtrend, not a crash.*
- **Roll rule:** ❌ **NONE pre-registered. Any roll = fresh Will approval from scratch, re-underwritten.**
- **Time stop:** **2026-09-04** (see §5).
- **Review cadence:** at each catalyst below.

**Catalyst map (all inside the position's life):**
| Date | Event | Note |
|---|---|---|
| **7/30 AH** | **AAPL + AMZN earnings** | ~15% of QQQ. Immediate gap risk **tonight**. |
| 7/31 | BOJ | |
| **8/12** | July CPI | ⚠️ **base-effect PROTECTED** — a soft print is **NOT** the mechanism failing; do not read it as invalidation. |
| ~8/20–22 | Jackson Hole | |
| **9/11** | Aug CPI | **The real passthrough test.** |
| **9/15–16** | **FOMC (SEP dots)** | Falls **inside** the expiry. |
| 9/18 | **Expiry** | |

## 7. Why not / counter-trade — the honest case against

1. **🔴 THE STRONGEST ONE — your stated premise was wrong and I had to replace it (§0).** If the argument you actually believe is *"narrow unhealthy rally,"* **the data refutes it over 5/10/21 days** and you should not trade it. Approve the *re-based* premise or decline the card. **A trade built on a premise its owner does not actually hold is the worst kind.**
2. **🔴 FLEET CONFLICT, LIVE TODAY: VIOLET's fade verdict cuts against this.** This morning (KB-VIO-144) she graded the vol event **shared-surface-alone → FADE-PRONE**, with a 20y base rate that post-inversion VIX **falls in 68% of 5-day windows**. **A fading vol event is near-term risk-ON.** Her call is about *vol*, not 7-week equity direction — but it is a genuine tension and **I am not going to bury it.** → confirm-ask routed to VIOLET.
3. **MSFT +14% is a real fundamental beat, not froth.** Azure +43% cc vs 40.2% est. Shorting an index because a component genuinely beat is not obviously edge.
4. **The market just absorbed a hawkish hold.** VIOLET: **MOVE fell 2.51% *on* FOMC day** — the policy channel did not transmit. Tape strength is real.
5. **You are paying 26.7% IV** on the long leg. The spread caps it (§4 vega note), but this is not cheap vol.
6. **Your book is already net-short risk in size** (regional banks ≈ −$5.3k realized-equivalent, APO, rates). This deepens a directional posture that has been bleeding — though see §5's regime-offset argument for why it is *not* simply "more of the same."
7. **QQQ is already −8.97% off its high.** Some of the move you want has happened. Mean-reversion risk from an oversold condition is real, and today is what that looks like.

## 8. Sizing
**1 contract, ~$490.** Full $500 card budget. ⚠️ **This is a NEW card with its own cap** — it does **not** touch 004's remaining ~$170 dry powder or the $200 Kharg fence.
⚠️ **1 lot cannot be scaled out of.** Target 1's "take half" is unexecutable. **Decide now**: exit whole at Target 1 (~+110%), or ride to Target 2. **Pre-register it on this card before filling.**

---

## Decision

**Terry verdict: 🟡 CONDITIONAL.** The structure is clean — liquid legs, sub-1.5% spreads, defined risk inside the cap, near-vega-neutral, a reachable breakeven (−3.3% below yesterday's close), a real catalyst map, and **50 days of life instead of 0–1, which was the entire reason to rebuild it.** Rule #6 is satisfied without needing a break.

**It is CONDITIONAL on exactly two things, both yours:**
1. **Do you accept the RE-BASED premise (§0) — "downtrend + one-stock bounce" — rather than the "narrow rally" version, which the 5/10/21-day data refutes?**
2. **Target 1 policy on a 1-lot: exit whole at ~+110%, or ride to Target 2?**

**Open, not blocking:** no domain agent has confirmed this thesis, and **VIOLET's own fade verdict from this morning leans the other way near-term** (§7.2).

**▶ ONE-LINE TICKET**
> **BUY TO OPEN 1× QQQ Sep-18-2026 645P / 620P put debit spread — net DEBIT limit $4.75, walk up $0.05 to a HARD CAP of $4.90, Day. Single spread order. Never leg, never market. No fill at $4.90 = NO TRADE.**

**APPROVAL REQUIRED — Will must approve/reject before execution.**
