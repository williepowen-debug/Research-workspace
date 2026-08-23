---
signal_id: SIG-W-20260812-003
date: 2026-08-12
time_dispatched: 2026-08-12T14:2xZ
origin: Will-Telegram 7-image batch 2026-08-12 ~13:20Z, item 1 of 7 (ResiClub/@ResidentialClub "U.S. housing foreclosures, by Q2") — batch manifest BM-20260812-01
source: ATTOM Q2/mid-year 2026 Foreclosure Market Report (attomdata.com, PRNewswire 2026-07-16, HousingWire, RISMedia) — 115,714 Q2 filings, −3% QoQ / +15% YoY; H1 227,548, +21% YoY; starts +18%; REO completions +33%; average timeline 563 days, lowest since 2013; state table. ResiClub series (55,160 for Q2 2026) taken from the posted image and NOT reconciled to a named metric — see §2.
domain: HOUSING
cluster: BANK_COLLATERAL
precedence: PRIORITY
action: [HOMER]
info: [CORAL, CARL]
entities: [ATTOM, foreclosure-filings, REO, Florida, South-Carolina]
signal_type: data-release
confidence: 0.85
verdict: CORRECTED-FRAMING
---

# 🟠 TWO FORECLOSURE NUMBERS FOR THE SAME QUARTER, BOTH LABELLED "FORECLOSURES" — 55,160 and 115,714. And the mechanism underneath is a **timeline collapse**, which is not the same story as rising distress. **You have been dark 12 days.**

## 1. What arrived

A ResiClub post giving US foreclosures by Q2, ending **Q2 2026 = 55,160**, with the series rising five straight years off the 2021 trough (8,100):

`2014: 115,300 · 2019: 65,920 · 2020: 23,860 · 2021: 8,100 · 2022: 35,000 · 2023: 38,740 · 2024: 47,180 · 2025: 52,800 · 2026: 55,160`

## 2. ⚠️ THE NUMBER DOES NOT MATCH THE HEADLINE SERIES, AND NEITHER SIDE SAYS WHICH METRIC IT IS

**ATTOM's Q2 2026 figure is 115,714 US properties with a foreclosure filing** (−3% QoQ, +15% YoY; one in every 1,242 housing units). **H1 2026 = 227,548, +21% YoY, +28% vs two years ago.**

**55,160 vs 115,714 — roughly 2×, same quarter.** The ResiClub chart is almost certainly a **narrower metric** (starts, or completions) rather than total filings; its pre-GFC peak of >500K/quarter is consistent with a starts series. **But the post labels it only "foreclosures," so I cannot name the metric variant and I am not going to guess one.**

🔑 **This is the live hazard, not a pedantic one:** anyone carrying "Q2 2026 foreclosures = 55,160" and anyone carrying "115,714" are both right and are silently comparing two different instruments. **Whichever you adopt, name the variant in the cell.**

## 3. 🔑 THE MECHANISM IS A SPEED STORY AND THE BARS INVITE YOU TO READ IT AS A DISTRESS STORY

ATTOM's Q2 internals:

| Metric | Q2 2026 |
|---|---|
| Foreclosure starts | **+18%** |
| **REO completions** | **+33%** |
| **Average timeline** | **563 days — lowest since 2013** |

**Completions +33% alongside timelines falling to a 13-year low is partly ARITHMETIC.** Faster processing mechanically converts an existing stock of distress into completions sooner. **A rising completion count with a falling timeline is not the same object as rising new distress** — and starts (+18%) is the cleaner distress read of the two.

⇒ **Decompose before you mark anything.** The rising-bars framing of the post carries no timeline information at all, so it reads the whole move as deterioration. Some of it is throughput.

*(Same class as the denominator guard CARL applied to the CC 90+ print last night — the headline moved, and the reason it moved changes what it means.)*

## 4. 🔴 FLORIDA IS #2 IN THE COUNTRY

Worst state foreclosure rates, Q2 2026:

1. South Carolina — one in **723** housing units
2. **FLORIDA — one in 726**
3. Delaware — one in 805
4. Indiana — one in 839
5. Nevada — one in 871

**CORAL:** Florida is a top-priority geography and it is second nationally, effectively tied with South Carolina. **Routed to you as a data point on your geography, not as a read** — you own whether it reconciles with the FL bank window you closed 7-of-7 benign on 8/3.

## 5. Ask

- **HOMER (action):** (a) which metric variant does your surface carry, if any — and does it reconcile to ATTOM's 115,714 or to the 55,160 series? (b) split the starts leg from the completions leg before marking anything, given the 563-day timeline. **You have been dark since 7/31 and the mid-year ATTOM report landed 7/16, inside that gap.**
- **CORAL (info):** FL #2 nationally, one in 726 units.
- **CARL (info):** consumer-transmission adjacency to last night's HHDC grading — same household, different collateral.

**TERRY: gate checked, NOT fired.** No registered TERRY instrument names a foreclosure series or any of these state exposures; corrects no number a TERRY surface cites; no closed-market event on a held underlying. **TERRY on no line, including `info:`.**
