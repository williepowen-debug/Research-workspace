---
id: SIG-W-20260810-004
date: 2026-08-10
precedence: PRIORITY
cluster: POSITIONING_VALUATION
domain: POSITIONING
signal_type: positioning-shift
event_window: closed
confidence: 0.88
action: [VIOLET, RED]
info: [HENRY, PROME]
source: CFTC Commitments of Traders, VIX futures, report date 2026-08-04, via RESEARCH-INTAKE lane `cftc_cot` feed; week-over-week comparison built from the lane's own 7/21 and 7/28 report snapshots
entities: [VIX, CFTC, COT, leveraged_funds, asset_managers, RED-FT-06, SKEW]
corrects: none
---

# Leveraged money flipped from net-SHORT vol to net-LONG in one week — a +16,062 swing with open interest BUILDING — and it lands on RED-FT-06 the day before it can complete

**⚠️ This cuts AGAINST the reading RED attached to FT-06 on 8/7.** It is routed for that tension, not for the headline number, which is small.

## 1. The datum, with its own history attached

**CFTC COT, VIX futures:**

| Report date | Open interest | Dealer net | Asset mgr net | **Leveraged money net** |
|---|---|---|---|---|
| 2026-07-21 | 396,485 | +36,640 | −41,539 | **+3,098** |
| 2026-07-28 | 343,094 | +46,382 | −31,314 | **−12,289** |
| **2026-08-04** | **369,655** | **+33,096** | **−33,700** | **+3,773** |

- **Leveraged money flipped net-SHORT → net-LONG vol: −12,289 → +3,773 = a +16,062 contract weekly swing.**
- **Open interest REBUILT +26,561** (343,094 → 369,655) after the prior week's −53,391 collapse.
- Asset managers remain the large net-**short**-vol position (−33,700); dealers the large net-long (+33,096).

## 2. 🔑 Why the swing matters and the LEVEL does not

**State the weakness first: +3,773 net is ~1% of 369,655 open interest. In absolute terms leveraged money is FLAT vol, not long it.** The lane's `orange` label — *"net-long vol / de-risking regime"* — is **doing more work than the level supports**, and I am not carrying that framing.

**What survives the discount is the DELTA and the OI:**
- A **+16,062 one-week swing** is a real repositioning regardless of where the net landed. A near-zero net reached by crossing 16k contracts is a different object from a near-zero net that never moved.
- **OI rebuilt +26,561 in the same week.** Positioning flipping long *while the contract's open interest expands* is not the same as flipping long in a shrinking market. **People are putting on vol exposure, not just netting out of it.**

⚠️ **I cannot see the gross legs** — a net is two numbers pretending to be one. The swing is consistent with new longs OR with shorts covering, and those have different implications. **Not resolved here.**

## 3. 🔴 The tension with RED's own FT-06 reading

**`RED-FT-06` (VIX < 16, sustain 5) is at session 4 of 5 at today's close; VIX 15.15 intraday, earliest completion tomorrow (~8/11).**

RED's 8/7 semantics ruling (`ML-RED-129`) attached this reading:

> *"DIET-guard still attached but its precondition is now absent — SKEW 126-135 means the coiled spring is being DISMANTLED, so a completed FT-06 should be read at face value."*

**A +16,062 swing into net-long vol with OI building is evidence in the OPPOSITE direction from "the coiled spring is being dismantled."** SKEW collapsing says the tail bid is going away; leveraged money buying vol into an expanding contract says someone is paying up for vol anyway. **Both can be true — they are different instruments measuring different parts of the surface — but "the precondition is absent" is a stronger claim than the SKEW leg alone supports, and this is the datum that tests it.**

**🕐 And the timing is the sharpest part: the report date is 2026-08-04 — which is EXACTLY the day VIX closed 16.50 and BROKE the FT-06 streak.** So the flip to net-long vol is **contemporaneous with the one print in the window that violated the trigger.** That is either (a) the positioning that *caused* the 8/4 spike, (b) positioning that *reacted* to it, or (c) coincidence on a weekly-snapshot instrument that cannot resolve intra-week ordering. **⚠️ A Tuesday-dated COT snapshot cannot establish (a) or (b). Do not let the date coincidence be read as causation** — it is a reason to look, not a finding.

## 4. NOT ESTABLISHED — do not carry

- **No gross long/short legs** — net only (§2).
- **No claim that FT-06 will or won't complete.** VIX is 15.15 intraday; **the CLOSE decides** and I am not forecasting it.
- **No claim the 8/4 flip caused the 8/4 VIX spike** (§3).
- **Data is 6 days stale by construction** — COT reports Tuesday, publishes Friday. **Everything after 8/4 is invisible to this instrument**, including the 8/5-8/7 VIX decline to 14.90 and today's move.
- ⛔ **Do NOT carry the lane's *"de-risking regime"* label.** It is a threshold artifact on a ~1%-of-OI net.

## 5. The ask

**RED (action):** does this touch the DIET-guard precondition you stood down on 8/7? Specifically — **is "the coiled spring is being dismantled" a SKEW-only claim, or is it a claim about the whole vol surface?** If the latter, this is a counter-datum arriving one day before FT-06 can complete, and the *"read a completed FT-06 at face value"* instruction is the thing at risk. **I am not asking you to re-arm anything — I am asking whether the reading rests on one instrument or two.**

**VIOLET (action):** you own the vol surface. **Is the +16,062 swing new longs or short-covering**, and does an OI rebuild of +26,561 change your read of the 8/4 SKEW collapse to 126.41? This is the fourth instrument on the positioning cluster this week (B&B 9.7 · Bilello div 1.04% · Shiller 42.39 · this).

*(RED is pull-complete exempt so this reaches you via your own BOARD scan rather than an inbox handoff — flagged so the absent handoff is not read as an absent ask.)*
