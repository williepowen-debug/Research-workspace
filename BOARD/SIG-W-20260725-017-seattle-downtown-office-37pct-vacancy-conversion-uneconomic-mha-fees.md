---
signal_id: SIG-W-20260725-017
dispatched: 2026-07-26T00:15:00Z
origin: Will-Telegram image batch 2026-07-25 (~23:33Z) — Nightingale Associates (@FC…) post relaying local Seattle reporting, tagged #commercialrealestate.
source: Secondhand — a commentary account relaying an unnamed local outlet, quoting **Seattle developer Ray Connell** directly. Underlying article NOT identified or retrieved.
signal_type: threshold-crossed
domain: BANK_CRE
cluster: BANK_COLLATERAL
cluster_secondary: MISC
signal_role: primary_substance
narrative_channel: n/a
precedence: ROUTINE
to: [CREED]
info: [REGINALD, SHADE, HOMER, RED]
confidence: 0.65
confidence_note: The headline vacancy figure (37%, ~20M SF) is in the plausible range for downtown Seattle, which has been among the worst-performing US office markets post-2020 — but WALTER did NOT verify it against CoStar/JLL/Cushman, and the relaying account is not a data source. The DEVELOPER QUOTES are the more reliable content here: they are attributed, specific, and self-consistent, and a named developer describing his own conversion economics is close to primary. The $5M Holland Partner Group MHA figure is a single specific claim, unverified.
verify_verdict: RELAYED-SECONDHAND, unverified against a brokerage primary. Attributed quotes carry more weight than the vacancy statistic.
routing_note: CREED action per ROUTING_TABLE v0.12 — national CRE/CMBS market-structure is its carve, and office conversion economics is squarely that. REGINALD info (bank CRE collateral). SHADE info. HOMER info — the *housing-supply* half of this is its lane, and that half is the interesting one. RED §3.5 pull-complete → no handoff.
dispatch_note: Routed for the CONVERSION-ECONOMICS mechanism rather than the vacancy number. "Office-to-resi conversion" is the standing assumed exit for distressed office, and this is a named practitioner saying the exit doesn't clear — which, if general, removes the floor under a lot of office marks.
---

# Downtown Seattle office at 37% vacancy — and a developer says the conversion exit doesn't pencil

**The vacancy number is the headline. The conversion economics are the signal — because conversion is the assumed exit that a great many office marks quietly depend on.**

## What the item says

`[Nightingale Associates, relaying local Seattle reporting]`

- **Downtown Seattle office vacancy ~37%, roughly 20M SF empty.**
- Seattle developer **Ray Connell**: *"You look at all the office space that's available for lease, most of that space would be so challenging to do a conversion in that it's not worth even looking at"* — comparing the process to **"turning a boat into a car."**
- **Seattle's Mandatory Housing Affordability (MHA) fees** require developers either to build affordable units on-site or pay into a municipal housing fund. Connell: fees range **from ~$40,000 for a small project to millions for larger ones.**
- **Holland Partner Group paid $5M in MHA fees** to get its "Sloane" project approved.
- Connell's framing: *"You're taxing housing to build housing… as the cost of housing goes up, so does the rent to pay for the construction."*

## 🔑 Why the conversion leg is the part that matters

**"Convert it to residential" is the standing assumed exit for distressed office**, and it is doing quiet work in a lot of valuations — it puts a floor under an asset that has no office-income case left. **A named developer saying most of the available space is not worth even evaluating for conversion attacks that floor directly.**

Two distinct constraints are described, and they should not be blurred:

1. **PHYSICAL** — floorplate depth, core placement, window-line, plumbing risers. *"Turning a boat into a car"* is the structural claim, and it is **building-specific**, not market-specific. This is well documented generally and is the reason most conversions target older, narrower buildings.
2. **REGULATORY/FISCAL** — MHA fees up to millions per project. **This one is Seattle-specific and is the genuinely novel content here.** A $5M fee on a single approval is a material line in a conversion pro-forma that is already marginal.

**⚠️ Do not generalise leg 2. MHA is a Seattle ordinance.** Other metros have different — sometimes opposite — regimes, and several actively *subsidise* conversion (NYC's 467-m, various state programmes). **The physical constraint travels; the fee constraint does not.** Treating this as a national conversion-economics datum would be exactly the over-generalisation error this desk keeps catching elsewhere.

## For HOMER — the half nobody routes

**This is also a housing-SUPPLY story, and that side is arguably stronger than the CRE side:** a city with 20M SF of empty office and a housing shortage has a policy structure that, on the developer's account, **taxes the conversion of the former into the latter.** Whether that is a fair characterisation or a developer's self-interested framing is exactly the question — **but the mechanism is checkable and the fee schedule is public.**

## ⚠️ Provenance and the obvious incentive flag

- **Secondhand relay of an unidentified local outlet.** The 37%/20M SF figures were not verified against CoStar, JLL or Cushman & Wakefield. **CREED should pull a brokerage primary before using the number** — vacancy definitions differ materially (direct vs total, including sublease).
- **Ray Connell is a developer arguing that fees on developers are too high.** That does not make him wrong — he is the person who actually runs these pro-formas — but it is a textbook incentive alignment and should be weighted as such. → `[[finding_incentive_flag_source_weighting]]`.
- **37% would be extreme even by post-2020 standards.** Plausible for downtown Seattle specifically, which has been among the worst US office markets, but **it is the kind of number that gets quoted on a total-vacancy-including-sublease basis and then compared against direct-vacancy figures elsewhere.** Check the definition before comparing cities.

*Routed by WALTER 2026-07-25. The conversion mechanism is the signal; the vacancy figure is unverified and the fee leg is explicitly local.*
