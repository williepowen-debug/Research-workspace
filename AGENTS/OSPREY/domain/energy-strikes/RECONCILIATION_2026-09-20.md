# Refining-impairment evidence reconciliation — 2026-09-20

**Trigger:** CATO reviews `80622311e` (F2) + `128a90879` — reconcile the independent refining-offline estimates against this desk's ~30% runs band on consistent definitions, then state explicit implications (or unresolved conditions) for the band and triggers. Owner: OSPREY. **No mark, band or threshold changed by this file — it resolves a definitional comparison and records what remains unmeasured.**

## Source-by-source comparison

| Source | Pub | Obs period | Measure (definition) | Figure | Denominator | Cause attribution | Eligibility |
|---|---|---|---|---|---|---|---|
| OSPREY band (KB-029) | 7/31 der. | Jul/Aug | **Runs decline** vs pre-campaign | **~30%** (25–35%) | ~5.5 M bpd baseline runs | mixed (proxy, always flagged) | EA Analytics via Bloomberg |
| Bloomberg / Rystad | **9/10** | Aug→early-Sept | **Runs/processing decline** | **~30%** | normal processing | strikes (Rystad VP, explicit) | Bloomberg + Rystad |
| The Insider | 8/31 | older underlying | Runs below normal | 25–30% | normal | mixed | Insider (Sinara=Jun Reuters; RSPP=8/21 RBC) |
| IIR Energy (ECI) | 9/8 | Aug avg | **Unplanned crude+condensate OUTAGE capacity** | **3.8 M bpd** (Jul 4.27) | affected-refinery capacity | Ukrainian strikes | IIR proprietary (not audited here) |
| S&P Global / CERA | 9/3 | end-Aug | **CAPACITY offline** | **~half (~50%)** | total refining capacity | strikes-primary | S&P/CERA independent (403 to me; via CATO + corroborating S&P export data) |
| FT (via CATO) | late Jul | late Jul | nominal offline / idle | 45% nom / >30% idle | nameplate | strikes | FT (not re-read) |
| Bloomberg / Julian Lee | 9/15 | exports 4wk→9/13; prod Aug | Exports; **production** | 3.54 exp; **8.72 prod** | — | strikes, **involuntary** | Bloomberg + OPEC secondary |

## What reconciles, and how

**1. There are TWO families of measure, and the apparent contradiction is definitional, not deterioration.**
- **Runs-decline family** (my band, Bloomberg/Rystad, Insider) clusters at **~25–30%** — how much less crude is actually being *processed* vs baseline.
- **Capacity-offline family** (S&P ~50%; IIR 3.8 M bpd ≈ ~55% of ~7 M bpd nameplate; FT 45% nominal) — how much *nameplate capacity* is unavailable.
- Nameplate offline (~50%) exceeds throughput decline (~30%) because normal utilisation was already <100% and surviving units run harder. **The ~50%-vs-~30% gap is a denominator/definition difference — it is NOT measured September deterioration.** (CATO's exact point, confirmed.)

**2. The band HOLDS at ~30% and is now independently corroborated** — Bloomberg/Rystad (9/10) put processing "fallen by 30%," an independent, current-ish runs figure landing on the band centre. **No band move**; do not adopt the ~50% capacity figure as a runs replacement.

**3. Production transmission is CONFIRMED and attribution resolves toward STRIKES (not OPEC+ policy).**
- Aug crude output **8.72 M bpd**, −160 kb/d m/m, 9th straight monthly drop, and **1.17 M bpd BELOW Russia's OPEC+ required level** → the shortfall is **involuntary** (policy compliance would sit at/above quota, not 1.17 under it).
- Mechanism, explicit: ~30% processing loss leaves **~1.7 M bpd of crude surplus** that exports + limited storage cannot absorb → **oil companies shutting in wells** (Bloomberg/Rystad).
- ⇒ The **Channel-1 → Channel-2 bridge is active**, the thing my 9/20 read wrongly said "we are not seeing." Attribution is now *primarily strikes* per Rystad/Bloomberg, not merely "unresolved."

## Unresolved conditions (explicitly retained)

- **September is not measured.** Every runs/capacity figure above is Aug or early-Sept (≤9/10); none observes the post-9/15 intensification or the 9/20 Moscow strike. The band is HELD, not re-confirmed for late September. Review ~9/23–25 (a review date, not a promised release).
- **Strike-attributable magnitude is directional, not quantified** — "primarily strikes" (Rystad) and "below quota" establish involuntariness; they do not isolate the exact strike-caused barrels from field decline.
- **The July basis pair (3.6 EA vs 3.91 Bloomberg, OWED-42)** is untouched by this reconciliation.
- **IIR shows outages DOWN Aug (3.8) vs Jul (4.27)** — i.e. the August capacity-offline eased slightly even as strikes continued; do not read a monotonic worsening into the series.

## Implications for triggers

- **C1 upgrade trigger** ("independent >40% national aggregate OR national runs <3 M bpd"): the capacity-offline family (~50%) **touches** the ">40%" letter but is a *capacity* measure at *end-August*, not the runs-based aggregate the band uses; runs sit ~3.85 M bpd (>3). **Not cleanly fired.** ⇒ **NOT self-upgraded.**
- ⚠️ **But the C1 picture has HARDENED** — multi-source ~50% capacity offline, ~30% runs corroborated, and production now transmitting involuntarily. **This is flagged to Will as a genuine C1 upgrade-to-5 candidate** (upgrades are Will-gated per the 8/20 precedent). Not a self-move.
- **No band move; no self-upgrade; OSP-03 (completed prediction, window closed 8/2) NOT regraded from later publications** (CATO F2 constraint honoured).
- **BRENT** owns whether any of this reprices crude; this file feeds the inputs, not a price call.

## Residual (separate workstream)
Feed matcher precision + evidence retention (OWED-45): dispositions and MATCHES are gitignored and same-day-overwritable; one false Sochi↔Komysh match reproduced. Not addressed here.
