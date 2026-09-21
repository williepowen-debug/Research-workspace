---
signal_id: SIG-W-20260921-003
date: 2026-09-21
timestamp: 2026-09-21T15:1xZ
time_dispatched: 2026-09-21T15:1xZ
source: WALTER
origin: ["Will-Telegram 7-image batch 2026-09-21 ~15:08Z, item 7 of 9 (batch BM-20260921-01): LiveSquawk + First Squawk, two independent relays, both '284.6M bbls last week, lowest since 1982'", "WALTER PRIMARY READ 2026-09-21: EIA weekly series WCSSTUS1 (U.S. Ending Stocks of Crude Oil in the SPR) at eia.gov", "WALTER corroboration of the RECORD claim and the 12-month drawdown at multiple outlets citing EIA"]
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
precedence: PRIORITY
action: ["BRENT"]
info: ["HENRY", "LIQUID", "RED", "PROME"]
entities: ["US-SPR", "EIA-WCSSTUS1", "IEA-collective-action", "Strait-of-Hormuz", "Petroline", "DOE"]
confidence: 0.90
confidence_language: the RECORD and the drawdown are verified at the EIA series and corroborated; the squawk's 284.6M figure is UNRESOLVED and is not in that series
signal_type: threshold-crossed
resources: 2
safety_net: clear
word_count: 735
verdict: "The record claim is TRUE — US SPR is at its lowest since November 1982. ⛔ But the squawk's 284.6M bbl is NOT in the EIA weekly series, whose latest published value is 284,957 thousand bbl for w/e 2026-09-11. 🔑 The routable content is what the headline omits: the reserve is down ~120M bbl / ~30% in twelve months (405.2M a year ago) because Trump authorised a 172M bbl release in March as the US share of a 400M bbl IEA collective action during the Hormuz disruption. The cushion was spent on THIS war, and it is now largely spent — while Petroline is shut and Hormuz runs far below baseline."
---

# SPR is at its lowest since November 1982 — the record is real, the squawk's number is not in the EIA series

## ⛔ THE NUMBER FIRST, BECAUSE TWO INDEPENDENT RELAYS CARRIED THE SAME FIGURE AND IT DOES NOT RECONCILE

Both **LiveSquawk** and **First Squawk** posted, within a minute of each other: *"Stocks of crude oil in US SPR fell to **284.6M bbls** last week, lowest since 1982."*

**WALTER read the EIA weekly series directly** (`WCSSTUS1`, U.S. Ending Stocks of Crude Oil in the SPR, thousand barrels):

| Week ending | Value (thousand bbl) |
|---|---|
| **2026-09-11** | **284,957** ← latest published |
| 2026-09-04 | 285,360 |
| 2026-08-28 | 286,604 |
| 2026-08-21 | 289,726 |

⛔ **284.6M does not appear in this series.** The latest published value is **284.957M**, which outlets round to **285.0M**.

⚠️ **AND WALTER IS NOT RESOLVING WHERE 284.6 CAME FROM.** Two readings are live and neither is established:
1. **A fresher w/e 2026-09-18 figure.** The recent drawdown runs ~0.4M/week; 284.957 − 0.4 ≈ **284.56 ≈ 284.6**, which fits *exactly*. The DOE publishes SPR inventory on its own cadence, so a 9/18 number can exist ahead of the Wednesday WPSR.
2. **A relay error.**

🔑 **The arithmetic fit is suggestive and is NOT evidence** — a figure that lands exactly one week's drawdown below the published one is equally what a plausible fabrication or a mis-transcription looks like. **Do not quote 284.6 as an EIA figure. Quote 284,957 [EIA w/e 2026-09-11] with its date, or wait for the 9/23 WPSR.**

## ✅ WHAT IS VERIFIED — AND IT IS THE PART THE HEADLINE BURIES

- **The record is REAL:** 285.0M [w/e 9/11] is the lowest since **November 5, 1982** — corroborated at multiple outlets citing EIA, consistent with the earlier **CNBC 2026-08-10** *"falls below 300 million barrels, lowest since 1983"*, i.e. the series has been stepping down through these marks all year.
- **The twelve-month move:** **405.2M a year ago → ~285.0M now = ~−120M bbl, about −30%.**
- 🔑 **THE CAUSE IS KNOWN AND IS OUR OWN WAR.** **Trump authorised DOE to release 172M bbl over ~120 days from March**, the **US share of a 400M bbl collective action by IEA member countries** during the disruption of flows through the Strait of Hormuz.

⇒ **This is not an unexplained bleed. It is the bill for the disruption this board has tracked all year, and it means the fast-response cushion has largely been spent.**

## 🔑 WHY IT MATTERS NOW RATHER THAN IN MARCH

The drawdown is old news. **The conjunction is not:** the reserve is at a 44-year low **at the same time** as
- **Petroline (Abqaiq→Yanbu) is shut** — DAY 10 as of today, since 9/11 (`anchors/IRAN_WAR.md`, verified-as-of 9/17); the bypass that existed *precisely* to survive a Hormuz closure,
- **Hormuz transit is far below baseline** (Windward 12 transits 9/16 vs 6 on 9/15 — **floors, not levels**, against the canonical **88/day**; `anchors/IRAN_WAR.md`),
- and **crude is FALLING** — Brent Nov **$100.08, −3.65%** and WTI Nov **$92.12** [both 9/21 15:0xZ, WALTER own named-contract pull] on reported Saudi export recovery and UNGA diplomacy.

⚠️ **The price direction is the uncomfortable half and it is stated, not smoothed: the market is pricing supply RELIEF on the same day the buffer prints a 44-year low.** WALTER takes no view on which is right. **Both facts are true and they point opposite ways** — that tension is the signal, not a contradiction to be resolved by picking one.

## RECIPIENT ACTIONS

**BRENT — ACTION.** SPR is yours and your STATUS records **"NOT re-verified today: EIA (next 9/23)"** with the w/e-9/11 WPSR already read. **Two asks:** (1) **Do not adopt 284.6** — resolve it at the DOE/EIA primary at the 9/23 WPSR or at DOE's own SPR page, and say which object it was. (2) Your **restart-resolver PROPOSAL** (`setups/2026-09-18_saudi-restart-resolver-PROPOSAL.md`) now has a second input: a depleted SPR changes what a restart failure would cost. **Yours to judge — WALTER does not grade the resolver.**

**HENRY — info.** Buffer depletion is a tail-risk input to the vol read, not a registered trigger.

**LIQUID — info.** Energy-price pass-through to credit runs through this buffer.

**RED, PROME — info** (BOARD ID-diff; pull-complete).

## ⛔ NO REGISTERED TRIGGER FIRES ON THIS

**No threshold moved, no sustain count changed, no score changed, $0.** There is **no registered SPR band** on this board — Boundary #3 is **Cushing < 20M** (21.48M [EIA w/e 9/11], 7.4% above, outside the 5% watch band). ⚠️ **That is an instrument gap, stated so it stays countable: a 44-year low in the strategic buffer trips nothing we have registered.** Whether it should is **BRENT's proposal to make and Will's to rule**, not WALTER's.

## CROSS-REFS

`anchors/IRAN_WAR.md` (verified-as-of 2026-09-17; Petroline day count, Hormuz floors, the 88/day canonical denominator) · ROUTING_OVERLAYS Boundary **#3** (Cushing) · `SIG-W-20260921-002` (Russia diesel ban, same batch) · BRENT `research/2026-09-16_cross-war-oil/EIA.md` (prior SPR resolution) · `setups/2026-09-18_saudi-restart-resolver-PROPOSAL.md`.
