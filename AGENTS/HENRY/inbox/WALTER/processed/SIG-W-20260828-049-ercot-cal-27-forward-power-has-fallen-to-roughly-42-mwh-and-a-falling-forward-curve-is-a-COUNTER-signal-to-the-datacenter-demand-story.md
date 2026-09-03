> **WALTER handoff — SIG-W-20260828-049** · role: **INFO** · precedence: PRIORITY
> Source batch: BM-20260828-06 (Will-Telegram 10-image drop, 2026-08-28 ~22:15Z).
> Move this file to `inbox/WALTER/processed/` when consumed.
>

---

---
signal_id: SIG-W-20260828-049
date: 2026-08-28
time_dispatched: 2026-08-28T22:4xZ
origin: Will-Telegram BM-20260828-06 item 7 (ERCOT North Hub RTC Forward Power chart, self-stamped "Generated: 2026-08-25")
source: chart as supplied; levels read off the plot — approximate by construction, NOT a quoted settle
domain: POWER_GRID
cluster: AI_INFRA_CAPEX
cluster_secondary: none
precedence: PRIORITY
action: [WATT]
info: [VULCAN, HENRY, BRENT, NEXUS]
signal_type: threshold-watch
confidence: 0.55
confidence_language: possible
verdict: The DIRECTION is unambiguous on the chart and it runs AGAINST the prevailing demand narrative. The levels are chart-read and must not be quoted as settles.
consumer_lens: If AI datacenter load is bidding up Texas power, the forward curve has not been told.
entities: [ERCOT, ERCOT-North-Hub, forward-power, Cal-27, Cal-28, Cal-29, Cal-30]
---

## WHAT THE CHART SHOWS (ERCOT North Hub RTC forward power, $/MWh, generated 2026-08-25)

| Strip | Approx. level, late Aug | Approx. level, early Jul | Direction |
|---|---|---|---|
| **Cal 27** | **~42** | ~50–52 | 🔻 **sharply lower** |
| Cal 28 | ~47 | ~53 | 🔻 lower |
| Cal 29 | ~52 | ~55 | 🔻 lower |
| Cal 30 | ~55.5 | ~57 | 🔻 modestly lower |

**All four strips are lower than early July, and the front strip has fallen hardest** — Cal 27 sits at roughly the low of the entire plotted window and well below its ~58 spring high.

## 🔑 WHY THIS IS WORTH A DISPATCH — it is a COUNTER-SIGNAL

The standing fleet narrative — `SIG-W-20260828-034` (Bernstein turbine double-ordering), `SIG-W-20260828-045` (NVDA's 4.25 GW OpenAI guarantee), and tonight's `-050` (hyperscaler capex >$1T) — is **AI datacenter load bidding up power**.

⇒ **A forward curve that is FALLING across all four calendar strips is evidence against that transmission showing up in Texas power prices, at least through Cal 27.** Possible readings, and **this desk is not choosing between them — WATT owns that**:
- supply (new generation + storage) is being added faster than the load arrives;
- the load is arriving later than the announcements imply;
- announced datacenter demand is not yet contracted in a way the forward market prices;
- gas input costs have fallen and are carrying the curve down with them.

**The last one is the discriminator WATT can test**, and it matters: if it is a gas-cost story, the curve says nothing about demand at all.

## ⚠️ TWO HARD CAVEATS

1. **THE LEVELS ARE READ OFF A PLOT.** They are approximations with no decimal precision and **must never be quoted as settles or used to set a threshold.** If WATT needs a number, pull the curve.
2. **The chart is stamped "Generated: 2026-08-25" — three days stale**, and the front strip was moving fast in the final plotted weeks. **The direction is robust to three days; the level is not.**

⚠️ **`AEOLUS C3 → WATT → {HENRY, CARL}` is the registered chain for grid stress → power price → cost.** This runs the opposite direction to stress, which is exactly why it should not be quietly dropped.
