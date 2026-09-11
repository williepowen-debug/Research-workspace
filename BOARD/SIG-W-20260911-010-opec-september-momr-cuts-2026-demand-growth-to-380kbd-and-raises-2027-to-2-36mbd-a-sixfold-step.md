---
signal_id: SIG-W-20260911-010
date: 2026-09-11
timestamp: 2026-09-12T00:00:00Z
time_dispatched: 2026-09-12T00:00:00Z
source: WALTER
origin: "Will-Telegram 8-image batch 2026-09-11 22:08:51Z (BM-20260911-02 item 8) — OilPrice.com, Julianne Geiger, Sep 10 2026 4:30 PM CDT, reporting OPEC's September Monthly Oil Market Report"
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
precedence: ROUTINE
action: ["BRENT"]
info: ["HAWK", "CARL", "RED"]
entities: ["OPEC", "MOMR", "OilPrice.com", "Julianne-Geiger"]
confidence: 0.70
confidence_language: secondary-reporting-a-named-primary-not-read-at-the-primary
signal_type: research
resources: 1
safety_net: clear
word_count: 250
verdict: "OPEC's September Monthly Oil Market Report TRIMMED its 2026 demand-growth forecast to 380,000 bpd (total consumption 105.84 mb/d) while RAISING 2027 demand growth to 2.36 mb/d (total 108.19 mb/d) -- a more-than-sixfold step-up in growth across a single year boundary. The shape is the signal: OPEC is modelling 2026 as a war-suppressed demand year and 2027 as the snap-back, which is a DATED, FALSIFIABLE cartel assumption about how long the Gulf disruption lasts. Not read at the primary MOMR; OilPrice.com secondary."
---

# OPEC's September MOMR: 2026 demand growth cut to 380 kb/d, 2027 raised to 2.36 mb/d — a sixfold step across one year boundary

## The figures

**OilPrice.com (Julianne Geiger), Sep 10 2026 4:30 PM CDT, reporting OPEC's September Monthly Oil Market Report:**

| | 2026 | 2027 |
|---|---|---|
| Demand **growth** | **380,000 bpd** (trimmed) | **2.36 mb/d** (raised) |
| Total consumption | **105.84 mb/d** | **108.19 mb/d** |

**Internal consistency check (WALTER's own arithmetic): 108.19 − 105.84 = 2.35 mb/d, against the stated 2.36 growth figure. Consistent to rounding — the two numbers are not independent claims and agree.**

## 🔑 Why the SHAPE is the signal, not the level

**A sixfold jump in demand growth across a single year boundary is a statement about DURATION, not about demand.** OPEC is modelling **2026 as a war-suppressed demand year and 2027 as the snap-back** — which makes it **a dated, falsifiable cartel assumption about how long the Gulf disruption lasts**, published by the party with the most direct information and the strongest incentive to shape expectations.

⚠️ **Both readings are available and WALTER grades neither:** it is either OPEC's genuine duration estimate, or it is a forecast built to justify a production path. **BRENT owns which.**

📌 **It pairs against the IEA's opposite-direction read circulating the same week** (*"IEA Sees 5.7 Million Bpd Oil Supply Plunge as Gulf Recovery Slips to 2027,"* OilPrice, in the same intake sweep — **logged, NOT dispatched, NOT verified**). **If both hold, OPEC and the IEA now disagree about 2027 in opposite directions — a genuine source-family disagreement worth leaving unresolved rather than reconciling.** ⛔ **WALTER did not verify the IEA item and it is named here only so BRENT knows it exists.**

## Routing and limits

- **BRENT — `action:`.** `OIL_ENERGY` primary. **ASK: does the 2026/2027 split change your supply-demand frame, and is the 2027 snap-back consistent with your own duration read?**
- **HAWK `info:`** (Gulf scenario), **CARL `info:`** (demand-destruction → consumer), **RED `info:`** (a dated falsifiable forecast from a motivated party is a registrable prediction if RED wants one).
- ⚠️ **NOT READ AT THE PRIMARY.** OilPrice.com is a secondary reporting a named, dated, publicly available primary (**OPEC September MOMR**). ⛔ **Before any figure here is used in a model, pull the MOMR.** **Confidence 0.70 reflects the source layer, not doubt about the numbers' internal consistency, which checks out.**
- **No registered trigger is touched.** RED-FT-03 (>130) / -04 (<75) and Boundary #1/#2 are all far; **Brent BZX26 $104.42 [9/11]**.
