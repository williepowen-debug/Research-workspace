---
signal_id: SIG-W-20260622-004
dispatched: 2026-06-23T02:56:00Z
origin: Will-Telegram 6-image batch 2026-06-22 (img #4) — @mercoglianos (Sal Mercogliano / "What's Going On With Shipping") X post relaying Lloyd's List, 8:11 PM 6/22
source: Sal Mercogliano / WGOW (X, 6/22) relaying Lloyd's List ("VLCC rates spike yet again as 'confusion continues to reign' at Strait of Hormuz") citing Baltic Exchange VLCC index assessments
signal_type: pattern-match
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
cluster_secondary: HYDROCARBON_INFRA
signal_role: cluster_mediating
narrative_channel: n/a
precedence: PRIORITY
to: HAWK
info: [BRENT, SAM, RED, TERRY]
confidence: 0.80
verify_verdict: SKIP-VERIFY — Sal Mercogliano (WGOW) is a credible maritime analyst relaying Lloyd's List + named Baltic Exchange VLCC index assessments (WAF-China / US Gulf-China / Oman-China). Directional claim (Hormuz "confusion" → VLCC rate spike) is corroborated by the IRAN_WAR anchor's elevated-premium read (war-risk premiums elevated, 0/4 reopening legs). Specific WoW %s relayed as "per Lloyd's List / Baltic Exchange," not independently re-priced.
routing_note: GEOPOL_ENERGY (Hormuz / chokepoint shipping) → HAWK action per ROUTING_TABLE; BRENT (price/decoupling authority), SAM, RED info. signal_role cluster_mediating (flat Brent FALLING / decoupling holds vs Hormuz FREIGHT spiking +82-92% WoW = tape-vs-substance: the physical/insurance leg is NOT decoupling) → RED auto-cc per v0.7 By-Tag. TERRY info added per ROUTING_TABLE v0.13 — freight-rate spike + Hormuz confusion is a latent squeeze-risk on the live oil-short book (Will named "all the shorts on oil"); bears on oil-short trade timing/structure. **Iran-anchor pre-dispatch check (Quick-WALTER-guard discipline):** IRAN_WAR.md fresh (6/22, re-stamped today); this signal CORROBORATES the anchor's physical leg (premiums elevated, shipping not normalizing, 0/4 reopening legs) — no framing conflict; defer throughput/price authority to BRENT per the anchor. Relates to ROUTING_TABLE Boundary #5 (VLCC ≥2× trailing-30d median sustained) but does NOT strictly fire it (single-week print, not sustained ≥3 sess) — referenced as corroboration, not a threshold fire.
---

# VLCC rates spike again on Hormuz "confusion" — Baltic WAF-China +92% WoW, US Gulf-China +46%, Oman-China WS276 +82%

**One line:** Lloyd's List (via Sal Mercogliano): VLCC freight rates spiked *again* as "confusion continues to reign" at the Strait of Hormuz — Baltic Exchange West Africa-China VLCC index $188,957/day (+92% WoW, highest since Mar 10), US Gulf-China $154,987/day (+46% WoW, highest since Apr 2), Oman-China Worldscale 276 (+82% WoW, highest since the index launched Mar 24). The flat oil price is decoupling (Brent ~$78, falling); the **cost of moving the barrel is not.**

## What it is (per Lloyd's List / Baltic Exchange, 6/22)

- **WAF-China VLCC:** $188,957/day — up **92% week-on-week**, highest since March 10.
- **US Gulf-China VLCC:** $154,987/day — up **46% WoW**, highest assessment since April 2.
- **Oman-China VLCC:** Worldscale **276** — up **82% WoW**, highest since the index was introduced March 24.
- Framing: "confusion continues to reign" at Hormuz — owners pricing war-risk + routing uncertainty, not a clean reopening.

## Why it routes (the genuine delta — the tape-vs-substance split)

The network's current read is **decoupling holds**: Brent fell ~3.5% into the Switzerland walkout + max-short positioning (SIG-W-20260621-010), and the Iran anchor stamped the Mon-6/22 decoupling test as resolved-toward-decoupling. This signal is the **counterweight on the physical layer** — freight is doing the opposite of decoupling. Flat price can fall while the *delivered* cost of crude rises because the war-risk/insurance/routing premium loads onto freight and hull, not the front-month flat price. That is precisely the anchor's "0/4 reopening legs / premiums stay elevated / shipping not normalizing" leg, now quantified in VLCC rates.

### → HAWK (ACTION)
- This is your chokepoint-shipping read: VLCC rates re-accelerating across three China-bound routes (WAF / US Gulf / Oman) = owners are *not* treating Hormuz as reopening, regardless of the diplomatic roadmap. Reconcile against your transit-count series (CENTCOM ~55 / Windward ~12-dark) — freight spiking while declared transits are disputed is consistent with the "confusion reigns" framing, not normalization.
- The Oman-China WS276 (a Gulf-origin route) +82% is the most Hormuz-proximate of the three — weight it heaviest for the strait-specific read vs the WAF/US-Gulf routes (which also carry a general tonnage-tightness / rerouting component).

### → BRENT (INFO — price/decoupling authority)
The decoupling thesis you own runs on *flat price*; this is the freight/physical-cost layer pulling the other way. Worth holding both: flat Brent decoupled on the open, but a +82-92% VLCC spike says the delivered-cost and war-risk premium is re-widening. If freight stays elevated into next week it pressures the "clean decoupling" read and feeds the crack/distillate-tightness thread (SIG-W-20260604-010). Your call on whether this is signal or one-week tonkage noise.

### → SAM (INFO)
Hormuz freight re-spiking is an Asia-import cost-push vector (China/Japan crude landed-cost) that composes with the USD/JPY-161 energy-import-burden channel — a not-yet-firing macro cross to keep tagged.

### → RED (INFO — cluster_mediating auto-cc)
- **Decoupling-intact read:** "flat Brent shrugged + fell; VLCC is a thin, volatile freight tape; +82-92% WoW off a low base after weeks of confusion is rerouting-driven, not a supply-disruption repricing — the decoupling holds where it matters (flat price)."
- **Decoupling-incomplete read:** "the war premium just moved venue — out of flat price and into freight/insurance; 'decoupling' that only holds on the front-month while delivered cost re-spikes is a measurement artifact, not a real de-escalation."
- Your call: which layer is the true read on whether the Iran energy risk has actually faded?

### → TERRY (INFO — trade-construction, oil-short timing)
For any live/candidate **oil short** (the near-record-short book, SIG-W-20260621-010): a +82-92% VLCC spike on Hormuz confusion is a latent **squeeze-risk** the flat-price short is blind to — physical tightness premium that flat Brent isn't carrying. Bears on entry timing / invalidation placement / whether to express via flat price vs a structure that doesn't bleed on a freight-led re-escalation. Not a thesis call — a "what could squeeze this short" timing input.

## Reopening-expectations counter-read (folded from a Chris Shipping/Greg Miller dup, 6/22)

A second relay of the identical Baltic numbers (Chris Shipping @christankerfund, with $DHT/$FRO/$ECO tags) was killed as a dup — but it carried one **material framing addition** worth folding here. **Greg Miller (@GMJournalist):** "Another VLCC rate spike, this time due to **expectations of strait REOPENING, even if partial/chaotic, pulling tonnage from the Atlantic.** Uncertainty = fleet inefficiency = shipowners win again."

This is a genuine alternate causation that **partially reverses the war-risk reading**: the freight spike may be **reopening-anticipation tonnage repositioning** (owners pulling ships toward the Gulf expecting Hormuz to reopen, draining Atlantic tonnage and tightening rates globally) rather than a pure war-risk premium. If Miller is right, the +82-92% is *constructive-for-reopening* (the market is positioning for flow to resume), not a fear bid — which makes the signal **more cluster_mediating, not less**: the same freight print supports both "confusion/war-risk = decoupling incomplete" AND "reopening-expectations = decoupling-toward-normalization." Either way, freight ≠ flat price, and "shipowners win on uncertainty" is the durable read. HAWK/BRENT/RED should weigh both causations; the Oman-China WS276 (Gulf-origin) tilts toward the reopening-tonnage-pull interpretation.

## Sources
- Sal Mercogliano / WGOW @mercoglianos (X, 6/22, 1.7K views) relaying Lloyd's List, "VLCC rates spike yet again as 'confusion continues to reign' at Strait of Hormuz."
- Chris Shipping @christankerfund (X, 6/22, 4.2K views, killed as dup) + the folded Greg Miller @GMJournalist reopening-expectations counter-read.
- Underlying: Baltic Exchange VLCC index assessments (WAF-China / US Gulf-China / Oman-China), 6/22.
- Corroboration: IRAN_WAR.md anchor 6/22 (premiums elevated, 0/4 reopening legs); SIG-W-20260618-002 (Maersk Cape-routing), SIG-W-20260619-004 (Hormuz tanker flow dark).
