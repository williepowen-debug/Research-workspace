# Refining-impairment evidence reconciliation — 2026-09-20

**Trigger:** CATO reviews `80622311e` (F2) + `128a90879` — reconcile the independent refining-offline estimates against this desk's ~30% runs band on consistent definitions, then state explicit implications (or unresolved conditions) for the band and triggers. Owner: OSPREY. **No mark, band or threshold changed by this file.** It (a) separates forecasts from observations, (b) leaves the numerical reconciliation OPEN (definitional direction only, not a demonstrated agreement), (c) evaluates the C1 upgrade trigger **as written** — finding its offline-aggregate limb MET — and (d) records what remains unmeasured. ⚠️ This is the THIRD correction pass (CATO `80622311e` → `128a90879` → `757aed30e`); the recurring failure was over-claiming closure, so nothing here is called "complete."

## Source-by-source comparison

| Source | Pub | Obs period | Measure (definition) | Figure | Denominator | Cause attribution | Eligibility |
|---|---|---|---|---|---|---|---|
| OSPREY band (KB-029) | 7/31 der. | Jul/Aug | **Runs decline** vs pre-campaign | **~30%** (25–35%) | ~5.5 M bpd baseline runs | mixed (proxy, always flagged) | EA Analytics via Bloomberg |
| Rystad | 8/18–9/10 | **H2-2026 FORECAST** | **Forecast** throughput ~30% below baseline (throughput "set to average 4 M bpd" H2) | **~30%** | **2016–2023 seasonal avg** (NOT my ~5.5 pre-campaign anchor) | strikes (Rystad, explicit) | Rystad (⚠️ FORECAST, different baseline — NOT a measured corroboration; CATO 757aed30e) |
| The Insider | 8/31 | older underlying | Runs below normal | 25–30% | normal | mixed | Insider (Sinara=Jun Reuters; RSPP=8/21 RBC) |
| IIR Energy (ECI) | 9/8 | Aug avg | **Unplanned crude+condensate OUTAGE capacity** | **3.8 M bpd** (Jul 4.27) | affected-refinery capacity | Ukrainian strikes | IIR proprietary (not audited here) |
| S&P Global / CERA | 9/3 | end-Aug | **CAPACITY offline** | **~half (~50%)** | total refining capacity | strikes-primary | S&P/CERA independent (403 to me; via CATO + corroborating S&P export data) |
| FT (via CATO) | late Jul | late Jul | nominal offline / idle | 45% nom / >30% idle | nameplate | strikes | FT (not re-read) |
| Bloomberg / Julian Lee | 9/15 | exports 4wk→9/13; prod Aug | Exports; **production** | 3.54 exp; **8.72 prod** | — | below quota; reporting attributes to strikes (causation NOT proven by quota arithmetic) | Bloomberg + OPEC secondary |

## How the measures relate (numerical agreement OPEN — nothing here is "reconciled")

**1. There are TWO families of measure. They are not contradictory BY DEFINITION — but whether these specific numbers AGREE is OPEN (see 2b), so this is a relationship, not a demonstrated reconciliation.**
- **Runs-decline family** (my band, Bloomberg/Rystad, Insider) clusters at **~25–30%** — how much less crude is actually being *processed* vs baseline.
- **Capacity-offline family** (S&P ~50%; IIR 3.8 M bpd ≈ ~55% of ~7 M bpd nameplate; FT 45% nominal) — how much *nameplate capacity* is unavailable.
- Nameplate offline (~50%) exceeds throughput decline (~30%) because normal utilisation was already <100% and surviving units run harder. **The ~50%-vs-~30% gap is a denominator/definition difference — it is NOT measured September deterioration.** (CATO's exact point, confirmed.)

**2. The band HOLDS at ~30% — but "corroborated" was too strong (CATO 757aed30e).** The runs-family figures near ~30% are a **Rystad H2-2026 FORECAST on a 2016–23 baseline** and the older Insider read — **not a measured Aug/early-Sept observation on my ~5.5 baseline.** So the band is HELD, **not independently measured-corroborated**. No band move; do not adopt the ~50% capacity figure as a runs replacement.

**2b. NUMERICAL RECONCILIATION IS OPEN, NOT DEMONSTRATED (CATO).** I have explained the *direction* (nameplate-offline > throughput-decline because utilisation <100%) but supplied **no matched-period calculation** proving the ~50% capacity and ~30% runs figures actually agree on a common denominator and month. Treat the two families as *not-contradictory-by-definition*, **not as reconciled-to-agreement**. Leave open unless a matched-period calc is done.

**3. Production transmission is CONFIRMED and attribution resolves toward STRIKES (not OPEC+ policy).**
- Aug crude output **8.72 M bpd**, −160 kb/d m/m, 9th straight monthly drop, and **1.17 M bpd BELOW Russia's OPEC+ required level**. ⚠️ Below-quota is **consistent with** an involuntary decline and the reporting (Rystad/Bloomberg) **attributes it to strikes** — but the quota arithmetic **alone does not prove causation** (CATO); the attribution rests on the reporting, which is directional ("primarily strikes"), not a measured strike-vs-other split.
- Mechanism, explicit: ~30% processing loss leaves **~1.7 M bpd of crude surplus** that exports + limited storage cannot absorb → **oil companies shutting in wells** (Bloomberg/Rystad).
- ⇒ The **Channel-1 → Channel-2 bridge is active**, the thing my 9/20 read wrongly said "we are not seeing." Attribution is now *primarily strikes* per Rystad/Bloomberg, not merely "unresolved."

## Unresolved conditions (explicitly retained)

- **September is not measured.** Every runs/capacity figure above is Aug or early-Sept (≤9/10); none observes the post-9/15 intensification or the 9/20 Moscow strike. The band is HELD, not re-confirmed for late September. Review ~9/23–25 (a review date, not a promised release).
- **Strike-attributable magnitude is directional, not quantified** — "primarily strikes" (Rystad) and "below quota" establish involuntariness; they do not isolate the exact strike-caused barrels from field decline.
- **The July basis pair (3.6 EA vs 3.91 Bloomberg, OWED-42)** is untouched by this reconciliation.
- **IIR shows outages DOWN Aug (3.8) vs Jul (4.27)** — i.e. the August capacity-offline eased slightly even as strikes continued; do not read a monotonic worsening into the series.

## Implications for triggers

- **C1 upgrade trigger, EVALUATED AS WRITTEN** (thesis/THESIS.md:38): *"Up: sustained runs <3 M bpd **or an independent >40% offline aggregate.**"* Two OR-limbs.
  - Limb 1 (runs <3 M bpd): **NOT met** — runs ~3.85 M bpd.
  - Limb 2 (**independent >40% offline aggregate**): ⛔ **MET on the wording.** S&P/CERA (9/3, independent) puts ~half of refining CAPACITY offline; IIR (9/8) 3.8 M bpd ≈ ~55% of ~7 M bpd nameplate; FT (late Jul) 45% nominal. All are independent, all are "offline aggregates," all >40%. **"Offline" reads naturally as capacity offline — that is what these measure.**
  - ⚠️ **CORRECTION (CATO 757aed30e):** my earlier "not cleanly fired" **narrowed the rule** by inserting a *"runs-based"* qualifier that is NOT in the written trigger. Removed. **The offline-aggregate limb is satisfied as written.**
  - **Eligibility caveats (honest):** the estimates are **end-August**, not post-9/15/current. ⚠️ **CORRECTED (CATO 349eb1d1d): older evidence does NOT imply today is worse** — repairs, restarts and new damage determine the current state, and IIR shows Aug outages (3.8) already *below* July (4.27), i.e. non-monotonic. September is unmeasured; **uncertainty does not automatically favour upgrading.** A single "nearly half" figure is an analyst estimate (though multiple independents agree >40%).

## Proposed 5→4 downgrade test for a capacity-based C1=5 (CATO-required; PROPOSED to Will, NOT enacted)

If C1 is upgraded to 5 on the S&P capacity-offline instrument, the reversal must be keyed to **that same instrument** (per §1b's general form), not the runs-based 4→3 limb. Proposed, symmetric with the upgrade:
- **5→4:** an independent capacity-offline aggregate (S&P/CERA or equivalent) prints **< 40% on two consecutive publications** AND **no new `refinery`-class `STRIKES.tsv` row for 14 days.**
- The existing runs-based limb (EA/Kpler monthly runs ≥ 4.5 M bpd for two months ⇒ 4→3) is unchanged and governs the 4→3 step.
- Rationale: §1b already says a channel steps down when "the evidence that fired its Upgrade Trigger reverses on the SAME instrument for two consecutive prints"; this only fills in the concrete capacity threshold (40%, mirroring the upgrade limb). ⚠️ One better September *runs* print does NOT reverse a capacity-based 5 — the reversal instrument must match the upgrade instrument. **Will-approval required (extends the 9/8 §1b rail); not self-enacted.**
- ⇒ **This is a LIVE, WILL-GATED C1 upgrade-to-5 decision with the written trigger MET** — not a "hold at 4 because the trigger isn't met." I do **not** self-move (upgrades are Will's word, 8/20 precedent). My prior "hold at 4, trigger not met" framing is **withdrawn** as resting on a narrowed rule.
- **No band move; no self-upgrade; OSP-03 (completed prediction, window closed 8/2) NOT regraded** (CATO F2 honoured).
- **BRENT** owns whether any of this reprices crude; this file feeds the inputs, not a price call.

## Residual (separate workstream)
Feed matcher precision + evidence retention (OWED-45): dispositions and MATCHES are gitignored and same-day-overwritable; one false Sochi↔Komysh match reproduced. Not addressed here.
