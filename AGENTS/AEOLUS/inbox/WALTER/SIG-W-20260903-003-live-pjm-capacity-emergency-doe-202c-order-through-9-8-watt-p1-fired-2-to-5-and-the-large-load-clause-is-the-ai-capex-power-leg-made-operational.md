---
signal_id: SIG-W-20260903-003
date: 2026-09-03
time_dispatched: 2026-09-03T22:3xZ
origin: WALTER inbox drain 2026-09-03 ~18:2x ET on Will's "process inbox" (BM-20260903-02). Packet author self-committed under carve-out (1); WALTER routes.
source: see the originating packet named in the body; figures re-read at the packet's own artifacts before routing.
domain: POWER_GRID
cluster: AI_INFRA_CAPEX
cluster_secondary: INFLATION_TRANSMISSION
precedence: IMMEDIATE
action: [NEXUS, LIQUID]
info: [BRENT, LABOR, CARL, HENRY, VULCAN, AEOLUS, RED]
entities: [PJM, NERC-EEA-1, DOE-202c, Order-202-26-41, WATT-P1, WATT-02, LMP, PJM-capacity, AI-datacenter-load]
signal_type: threshold-crossed
confidence: 0.95
verdict: CONFIRMED at primary (twice, by WATT). A live PJM capacity emergency: NERC EEA-1 on three consecutive days, Pre-Emergency Load Management dispatched, and a DOE Sec.202(c) emergency order running to 2026-09-08. WATT's P1 moved 2 -> 5 on the 8/17 RED band with the mechanism confirmed. The cascade did NOT trip.
consumer_lens: This is routed because WATT delivered it as an owner grade and routed ANALYSIS packets direct to its own five (AEOLUS/DEWEY/VULCAN/HENRY/CARL) — so the desks OUTSIDE that table have no channel to it but this one. NEXUS owns the cluster narrative and this is where the AI-capex power constraint stops being a forecast; LIQUID because a supply-side price shock with a published end date is a funding-and-credit input, not just a utility story.
corrects: none
---

> 📬 **HANDOFF → AEOLUS (INFO)** — routed from WALTER's 9/3 inbox drain (BM-20260903-02). See `verdict:` and `consumer_lens:` above for what this desk specifically owns.

# A live PJM capacity emergency — DOE §202(c) order through 9/8, WATT's P1 fired 2→5, and the large-load clause is the AI-capex power leg made operational

## 1. The event, primary-verified ×2 by WATT

| Fact | Value |
|---|---|
| NERC **EEA-1** | three consecutive days — 9/1 18:03 · 9/2 16:00 · 9/3 00:01 |
| Pre-Emergency Load Management Reduction | dispatched in **five zones** 9/1 |
| Synchronized Reserve Event | 9/3 05:33 |
| **DOE §202(c) Order No. 202-26-41** | 9/1 → **11:59 PM ET 9/8** — authorises PJM to direct **backup generation at LARGE LOADS** before an EEA-3 |
| RT LMP | **$1,868.78/MWh** @19:30 9/2; eight consecutive 5-min intervals ≥$1,000 |
| Congestion component | **$1.25** ⇒ **99.85% system energy**, not congestion |
| Season peak | 152,518 MW; PJM forecast 152,496 MW for 9/3 evening |

**State at 07:15 9/3: NO EEA-2, no voltage reduction, no load shed ⇒ WATT's cascade did NOT trip.** P1 = 5 is the ceiling short of a cascade.

## 2. 🔑 Why the §202(c) large-load clause is the newsworthy half

A capacity emergency is weather. **An emergency order that authorises the operator to direct backup generation AT LARGE LOADS is a regulatory instrument that treats datacenter load as dispatchable** — which is VULCAN's siting constraint and DEWEY's REQ-001 power half, arriving as an executed order rather than a projection. That is the transmission the lane should carry, and it is why this is filed under `AI_INFRA_CAPEX` rather than a pure grid row.

**Second leg, for CARL:** electricity as a consumer-price pressure — the channel this desk relayed out of the FOMC minutes on 8/19.

## 3. ⚠️ Live window and what would re-open it

**The order runs through 11:59 PM ET 2026-09-08.** PROME registered a DOCKET row with a wake trigger: **any EEA-2 / EEA-3 / voltage reduction / load shed ⇒ PROME spawns WATT same day.** ⛔ **Kill-on-sight: "WATT-02 trending MISS"** — it HIT, on the 202(c) limb.

⚠️ **No trade is proposed and WATT proposed none** — published end date, root rule #6, no live IPP quotes.

## 4. Two board corrections carried in the same delivery
- **`SIG-W-20260828-034`** (Bernstein turbine survey, "75% ordering above need") is **SEARCH-NOT-FOUND at primary across 11 query formulations**; WATT is not carrying its figures. → separately re-scored at `SIG-W-20260903-011`.
- **`SIG-W-20260828-049`** (ERCOT falsifier) reached WATT and is **consumed**; the partial answer leans demand/supply, not gas.
