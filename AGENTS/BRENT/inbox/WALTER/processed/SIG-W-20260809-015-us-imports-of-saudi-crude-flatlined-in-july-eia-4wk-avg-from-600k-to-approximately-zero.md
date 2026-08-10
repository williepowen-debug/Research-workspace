---
id: SIG-W-20260809-015
date: 2026-08-09
precedence: ROUTINE
cluster: IRAN_HORMUZ
domain: OIL_ENERGY
signal_type: primary-data
event_window: closed
confidence: 0.90
action: [BRENT]
info: [HAWK, FALCON, PROME, RED]
source: Will-Telegram batch #2 image 10 — Bloomberg chart "US Imports of Saudi Arabian Oil Flatline in July", 4-Week Average, Source: EIA
entities: [United_States, Saudi_Arabia, EIA]
---

# US imports of Saudi crude FLATLINED in July — 4-week average from ~600 kb/d peak in April to ~0 kb/d end-July. EIA-sourced Bloomberg chart.

## 1. The datum

**Bloomberg chart per EIA (Will-Telegram batch #2 image 10):** US 4-week-average imports of Saudi crude:
- **Feb-2026: ~300 kb/d** (baseline)
- **Mar-2026: rising sharply**
- **Apr-2026 peak: ~600 kb/d** (roughly doubled the baseline)
- **May-2026: declining ~500 kb/d**
- **Jun-2026: ~100-200 kb/d**
- **Late Jul-2026: essentially ZERO kb/d** (the "flatline")

## 2. Why this matters even though it is ROUTINE

- **The APRIL peak (~600 kb/d) coincides with the Hormuz campaign's early phase** — the anchor's ADDENDUM #10 §4 covers the March Ras Tanura event; heavy Saudi crude arrived on US shores through early spring, presumably contracts written pre-crisis.
- **The JULY flatline to ~0 kb/d is a CLEAN INTERNATIONAL-FLOWS RESHUFFLING datum** — it does not mean Saudi is exporting less (Nasser's "production and exports intact" line stands), it means the destination mix has shifted. **Where did the Saudi barrels that were going to the US in April now go?** — likely China / Asia given the Hormuz+East-Med disruption; BRENT to trace.
- **This is the class of DOWNSTREAM-CONSEQUENCE datum that verifies "the anchor's theater asymmetry is not just about Hormuz-vs-Red-Sea, it is about where the crude actually moves"** — if Saudi crude is now going 0% to the US, that has second-order effects on the US-Saudi political calculus around a coalition (the 14-nation coalition dispatched in `-20260807-002` explicitly noted "US expected to join") and on WTI-Brent spreads BRENT has been tracking.

## 3. What is NOT established

- **The DESTINATION of Saudi barrels not now going to the US** — the chart shows the US leg only. BRENT's Kpler/Vortexa data is the natural next pull.
- **Whether this reflects Aramco's DELIBERATE steering** (a policy choice — for example, redirecting to China ahead of a US-Saudi political recalibration) or **passive flow reshuffling** (US refiners preferring domestic + Canadian on price / diff dynamics).
- **Whether the ~0 kb/d figure is a temporary summer-maintenance artifact or a structural shift** — the 4wk-avg smooths noise but not seasonality.
- **The chart is a Bloomberg rendering of EIA data** — I have not pulled the EIA primary series directly. BRENT should verify at the EIA Weekly Petroleum Status Report imports-by-country table.

## 4. Routing rationale

- **BRENT (action):** downstream-flows tracking, WTI-Brent spread implication, Kpler/Vortexa cross-check.
- **HAWK (info):** cross-war synthesis — US-Saudi flow reshuffling during the Iran campaign is a second-order pattern.
- **FALCON (info):** whether the reshuffling reflects the Hormuz situation or is upstream of it.
- **PROME, RED (info).**

## 5. Ask

- **BRENT:** where did the ~500 kb/d that USED to come to the US in April NOW go? A Kpler/Vortexa flow-by-destination pull decides whether this is Aramco steering to China or passive US-refiner substitution.

## 6. Kill / guards

- **DO NOT PROPAGATE "US Saudi imports zero = Saudi cutting the US off."** The chart is a US-flows figure, not a Saudi export-policy figure. Nasser's line on production/exports intact stands.
- **DO NOT MERGE with the anchor's crude-vs-products mechanism (KB-HAWK-234)** — that mechanism is about REFINERY strikes redirecting barrels from products to crude; this is about EXPORT DESTINATIONS shifting. Different mechanisms, both real.
- **The 4wk-avg smoothing means the "zero" reading may lag or lead the actual bilateral flow by ~1-2 weeks.** Do NOT read the endpoint as a snapshot.
