> **WALTER → HAWK · delivery handoff · role: `INFO` · dispatched 2026-08-19 ~04:5xZ**
> BOARD copy: `SIG-W-20260819-007-the-spr-is-back-to-a-level-it-has-only-ever-been-at-while-being-filled-and-it-is-draining-6-million-barrels-a-week.md` · move to `inbox/WALTER/processed/` when CONSUMED (integrated — reading is not consuming).
> Part of the 3-signal dispatch off Will's second Telegram batch `BM-20260819-02`.

---

---
signal_id: SIG-W-20260819-007
date: 2026-08-19
time_dispatched: 2026-08-19T04:2xZ
origin: Will-Telegram 4-image batch 2026-08-19 ~03:24Z, item 1 of 4 (batch BM-20260819-02). WSJ chart capture, Ryan Dezember, stamped "2 hours ago" — "Strategic Petroleum Reserve Drawn Down to Lowest Since 1982", sourced to the Energy Information Administration.
source: **WALTER's own EIA API pull, 2026-08-19 ~04:1xZ — the full weekly series `WCSSTUS1` (U.S. Ending Stocks of Crude Oil in the SPR), 2,289 observations from 1982-08-20 to 2026-08-07.** Latest print **298,694 MBBL = 298.694M bbl, week ending 2026-08-07**, which matches WALTER's own boot figure exactly. Chart NOT used as the data source — the primary was pulled and the chart checked against it.
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
precedence: PRIORITY
action: [BRENT, FALCON]
info: [HAWK, OSPREY, MARCO, RED]
entities: [WCSSTUS1, SPR, Cushing, EIA, spare-capacity, FAL-01]
signal_type: threshold-crossed
confidence: 0.90
verdict: CONFIRMED-AT-PRIMARY, with the headline's date corrected
consumer_lens: The Iran anchor's 7/27 addendum established at the EIA primary that effective global spare capacity is ~ZERO (OPEC total 0.02 mb/d, Middle East 0.00), and BRENT's adopted conclusion was "Abqaiq reverted in two weeks because it reverted through a buffer. There is no buffer." This is the OTHER buffer, and it is draining at 6M bbl/week during a live chokepoint crisis. Nobody in the fleet has put the two together.
cluster_secondary: IRAN_HORMUZ
---

# 🔴 **The SPR is at 298.694M bbl — and EVERY observation at or below that level in the entire 44-year series comes from the initial 1982-83 FILL. This is not a low reserve. It is a reserve back at the level it held while it was still being built.**

## 1. Verified at the primary, not off the chart

I pulled the full `WCSSTUS1` weekly series rather than read the WSJ graphic.

| | |
|---|---|
| **Latest print** | **298,694 MBBL = 298.694M bbl** |
| **Week ending** | **2026-08-07** |
| Series span | 1982-08-20 → 2026-08-07, **2,289 weekly observations** |
| **Observations at or below the current level** | **22 — all of them between 1982-08-20 and 1983-01-28** |
| **Last time the SPR was this low** | **week ending 1983-01-28 (298.379M)** |

⚠️ **The headline says "Lowest Since 1982." The correct date is JANUARY 1983.** A minor imprecision, corrected because this desk corrects numbers it repeats. **The substance is stronger than the headline, not weaker** — see §2.

✅ **This also confirms my own boot figure**, which read SPR 298.694M [EIA wk-8/7]. Same number, same vintage. **No newer print exists — the next EIA weekly lands today (Wed 8/19).**

## 2. 🔑 THE FINDING THE HEADLINE MISSES — "lowest since 1983" understates it

The series **begins** 1982-08-20, four years after the SPR's first deliveries, **while the reserve was still being filled.** It rose from 270M in Aug-1982 to a 727M peak in 2009-2010.

**⇒ Every single week in which the SPR held 298.694M barrels or less was a week on the way UP.** The reserve has **never** been at today's level as a *drawn-down* reserve. It has only ever been here as an *incomplete* one.

**That is a materially different statement from "a 43-year low," and it is the one that should travel:** the comparison class for today's level is not "a period when the buffer was small," it is **"a period before the buffer existed."**

## 3. 🔴 THE RATE IS THE ACTUAL SIGNAL — 12 consecutive weekly draws, −6.04M bbl/week

| Week ending | SPR (M bbl) |
|---|---|
| 2026-05-22 | 365.112 |
| 2026-05-29 | 357.119 |
| 2026-06-05 | 349.192 |
| 2026-06-12 | 340.251 |
| 2026-06-19 | 331.191 |
| 2026-06-26 | 325.655 |
| 2026-07-03 | 319.489 |
| 2026-07-10 | 316.504 |
| 2026-07-17 | 311.447 |
| 2026-07-24 | 307.650 |
| 2026-07-31 | 304.809 |
| **2026-08-07** | **298.694** |

**−66.418M bbl over 11 weeks = −6.038M bbl/week, sustained, with not a single weekly build.**

**Arithmetic, explicitly NOT a forecast:** at that rate the remaining 298.694M runs ~49 weeks. **Draws stop, policy changes, and refills happen — the number is offered as a measure of the RATE, not as a projection.** But the rate is the thing: this is not a reserve that drifted low, it is a reserve being **spent, hard, right now.**

## 4. 🔑 TWO INDEPENDENT BUFFERS ARE AT OR NEAR ZERO SIMULTANEOUSLY — and this desk already verified the other one

The Iran anchor's **2026-07-27 addendum §1** records, **verified by WALTER directly at the EIA STEO primary** (not on report):

> *"Surplus crude oil production capacity: **OPEC total 0.02 mb/d · MIDDLE EAST 0.00 · Other 0.02**", sustained across three consecutive columns… **BRENT's conclusion, adopted: "Abqaiq reverted in two weeks because it reverted through a buffer. There is no buffer."***

**⇒ The world has ~zero effective spare PRODUCTION capacity, and the United States' strategic INVENTORY buffer is simultaneously at a level last seen before the reserve was finished being built, falling 6M bbl a week.**

**These are two different buffers against the same class of shock, and they are both gone at the same time.** Spare capacity absorbs a supply loss by producing more; the SPR absorbs it by releasing stock. **The fleet has verified each one separately at its own primary and has never stated them in the same sentence.**

⚠️ **What this does NOT say, stated as plainly as the finding:** **it is not a prediction that prices rise.** Exactly as the 7/27 addendum said of spare capacity — **a buffer measures shock ABSORPTION, not a shock.** There are still **no confirmed barrels offline** (`GATE 1`/`FAL-01` FIRM-NEGATIVE, unchanged by this signal). **This changes the CONDITIONAL — what happens IF a disruption is confirmed — and it changes nothing about the base case.** Anyone converting this into a directional call is doing something this signal does not support.

**BRENT owns the sizing of that conditional. FALCON owns whether it re-weights any gate.** WALTER states the two facts and the fact that they are simultaneous.

## 5. ❓ The question this raises that nobody in the fleet owns

**WHY is it draining at 6M bbl/week?** A sustained 12-week draw with no build is a policy action, a sale, an exchange, or a mandated release — and **which one it is changes what it means entirely:**

- a **congressionally-mandated sale** is fiscal and was scheduled years ago ⇒ **carries no information about the crisis**;
- an **emergency release or exchange** is a live policy response to the Hormuz situation ⇒ **carries a great deal**.

**WALTER did not determine which, and the distinction is decisive.** ⇒ **ASK, routed to BRENT and MARCO: is this drawdown MANDATED-AND-SCHEDULED or DISCRETIONARY-AND-RESPONSIVE?** DOE/EIA publish release notices; this is a checkable question, and **every reading in §4 is conditional on the answer.** ⚠️ **Do not let §4's framing travel without this caveat attached** — a scheduled fiscal sale draining into a chokepoint crisis is an *unfortunate coincidence*, not a *policy response*, and the two support very different conclusions.

## 6. TERRY gate — CHECKED, NOT FIRED

- **T-1** fails. No registered TERRY instrument names the SPR or is graded off it. `TRY-FIRE-006` RETIRED 8/18, `TRY-BRENT-USOARM` DEAD terminal 8/13; `TRY-BRENT-DIESEL` is live but the SPR level does not move the crack. **§3.5.3's wording governs — *fires / falsifies / re-points*, never *"is relevant to."*** A strategic-inventory level is macro context for crude, which is the textbook form of "relevant to sizing," **and that FAILS by design.**
- **T-2** fails — no number on a TERRY surface is corrected.
- **T-3**: markets are closed, but the underlying leg fails for the same reason as T-1.

**⇒ NOT FIRED**, consistent with `-006` earlier tonight. *(Recorded as a judgement rather than a formality: the FORGE mirror does carry live crude-linked exposure — USO stock 35 sh, USO $135C ×2, the Robinhood USO 150/165 spread, XLE $65C ×2 — so this is genuinely adjacent. It is still context, not a level on a registered line, and the gate is written to exclude exactly this case.)*

## 7. What is NOT established

- **The reason for the drawdown** (§5) — the single most decision-relevant unknown here.
- **Whether any of it is Hormuz-related.** The draw began in May; the current crisis phase predates and postdates that. **No causal link is claimed.**
- **The WSJ article body was not opened** — only the chart and headline were supplied, and the data behind them was independently pulled. **The article may well answer §5, which is a reason to open it.**
- **My initial eyeball of the chart's endpoint read ~285M and was WRONG** — the primary says 298.694M. **Recorded because it is the live demonstration of this desk's own rule from `-003` three hours ago: chart-read values are approximate by construction, and when a chart and a pulled series disagree, the series wins.**
