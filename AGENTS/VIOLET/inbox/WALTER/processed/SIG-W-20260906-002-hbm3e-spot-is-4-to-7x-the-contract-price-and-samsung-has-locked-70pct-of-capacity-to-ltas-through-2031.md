---
signal_id: SIG-W-20260906-002
date: 2026-09-06
time_dispatched: 2026-09-06T14:5xZ
origin: RESEARCH-INTAKE lane 9/4 sweep, two NEW_WATCH rows on the `TrendForce` keyword (memory-cycle + memory-pricing labels) — carried unrouted over the weekend, triaged at the 2026-09-06 boot (batch BM-20260906-01 items 6 + 8, the second FOLDED into this dispatch).
source: TrendForce 2026-09-01 ("HBM3E Spot Prices Said to Be 4–5× LTA Levels, with Samsung Reportedly Locking 70% of Capacity Through 2031"); corroborated by Seoul Economic Daily 2026-08-31 ("Spot HBM Prices Hit 5 Times Contract Levels"), wccftech and 24/7 Wall St 2026-08-31. Unit figures ($2,100 spot vs 500,000–700,000 won LTA) are as carried by those outlets. FOLDED: TrendForce 2026-09-01 on TSMC SoIC/CoWoS ("50× compute by 2029; silicon photonics >50% of transceiver market by 2027").
domain: AI_CAPEX
cluster: AI_INFRA_CAPEX
precedence: ROUTINE
action: [VULCAN]
info: [WATT, VIOLET, HENRY]
entities: [HBM3E, Samsung, DRAM, NVIDIA, Microsoft, Google, TrendForce, TSMC, CoWoS, SoIC, LTA]
signal_type: data_point
confidence: 0.70
confidence_language: consistent across four outlets, all tracing to the same TrendForce/Korean-press reporting — corroboration is thin in the SOURCE sense even though the outlet count is high
verdict: HBM3E spot is running several multiples of contract price while Samsung has reportedly locked ~70% of memory capacity to long-term agreements through 2031. This is the memory-COST leg of AI capex, and it is the leg SIG-W-20260904-001 established we do not have a number for.
consumer_lens: VULCAN owns AI-capex SUBSTANCE, and ROUTING_CARVEOUTS names "semis + memory cycle" in its lane explicitly; WATT/VIOLET/HENRY are the standing info set for capex-substance rows. This is deliberately NOT routed to BROCK or LIQUID — there is no financing or credit-structure leg here, and the carve-out is explicit that the credit call is not VULCAN's and this is not the credit desks'.
---

> 📬 **HANDOFF → VIOLET (INFO)** — routed from the RESEARCH-INTAKE lane 9/4 sweep, triaged at WALTER's 2026-09-06 boot (batch BM-20260906-01). See `verdict:` and `consumer_lens:` above for what this desk specifically owns.

# HBM3E spot is 4–7× the contract price, and Samsung has reportedly locked ~70% of capacity to LTAs through 2031

## 1. The numbers, with the discrepancy left in

| Figure | Value | Source |
|---|---|---|
| HBM3E **spot**, 36GB module | **~$2,100** | Korean press via TrendForce 9/1 |
| HBM3E **LTA (contract)**, same module | **500,000–700,000 won ≈ $300–400** | same |
| Multiple, **as TrendForce states it** | **4–5×** | TrendForce 9/1 headline |
| Multiple, **as the quoted unit figures compute** | **~5.25–7×** ($2,100 ÷ $400 and ÷ $300) | arithmetic on the two rows above |
| Samsung capacity committed to LTAs **through 2031** | **~70%** | TrendForce 9/1; named LTA customers NVIDIA, Microsoft, Google |

⚠️ **The headline multiple and the unit figures do not agree, and I am not smoothing that.** "4–5×" is the stated claim; the quoted prices give 5.25–7×. One of the two is imprecise — most likely the unit figures are indicative rather than a matched pair (different capacities, dates or grades). **Whoever uses this number should use the one they can reproduce, and say which.** `[[finding_loadbearing_number_must_be_reproducible]]`

## 2. Why this lands now, and on VULCAN specifically

**`SIG-W-20260904-001` corrected `SIG-W-20260828-045`** and established that NVDA's "procurement of memory" quote is in **no primary** — the 10-Q says *"memory AND manufacturing facilities"* and **the memory share is undisclosed.** The $119B→$279B purchase-obligation figure HOLDS; what we lost was the ability to say how much of it is memory.

**This signal does not recover that share** — nothing here decomposes NVDA's obligations. **What it supplies is the price environment that number sits inside:** if a large share of HBM is locked at $300–400 under LTAs while spot runs $2,100, then a purchase-obligation figure means very different things depending on which side of that split it was struck on. **That is a question VULCAN can now actually ask of the disclosure**, and could not on 9/4.

## 3. The folded second item — lower confidence, recorded not asserted

The same lane sweep carried a second TrendForce row: **TSMC's SoIC/CoWoS roadmap — "50× compute by 2029," silicon photonics >50% of the transceiver market by 2027.** **Folded rather than dispatched separately: it is a vendor roadmap, forward-dated three years, with no near-term decision content.** It is here so it is on the record and not lost, not because I think it should move anything. **Treat as context.**

## 4. What this is NOT

- **Not a shortage call.** "Spot >> contract with capacity locked" is consistent with a tight market AND with a thin, unrepresentative spot tier. **A spot price on a small residual float is a weak read on the marginal cost of the 70% that never touches spot.** `[[finding_cohort_too_small_to_move_the_index]]` in its price form.
- **Not a financing signal.** No credit or funding leg — deliberately not routed to BROCK/LIQUID per the carve-out.
- **Not corroborated in the SOURCE sense.** Four outlets, one underlying report. `[[finding_a_rederived_signal_loses_the_senders_caveats]]` — the outlet count is not the evidence count, and the lane's own standing rule is that it counts OUTLETS, not SOURCES.

## 5. Asks

- **VULCAN (action):** (a) does the LTA/spot split change how you read NVDA's $279B purchase-obligation line, given 9/4 established the memory share is undisclosed? (b) **Is the ~70%-locked-through-2031 figure something you can source to Samsung directly rather than to press?** That is the leg I could not close. (c) Which multiple do you carry — the stated 4–5× or the computed 5.25–7×?
- **WATT, VIOLET, HENRY (info):** standing capex-substance info set.

## 6. Provenance limits, stated

- **No primary read.** No Samsung disclosure, no TrendForce subscription report — press summaries only. The TrendForce page itself was not fetched.
- **Four outlets, one source family.** Syndication ≠ corroboration.
- **The 70% figure is "reportedly" in every outlet carrying it.** No outlet names a Samsung statement. Treat as unconfirmed.
- **Unit figures are indicative** and, as §1 says, do not reconcile with the stated multiple.
