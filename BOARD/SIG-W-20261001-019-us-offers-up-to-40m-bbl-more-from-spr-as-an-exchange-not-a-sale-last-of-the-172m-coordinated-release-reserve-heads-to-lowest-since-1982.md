---
signal_id: SIG-W-20261001-019
date: 2026-10-01
timestamp: 2026-10-01T17:05:24Z
time_dispatched: 2026-10-01T17:05:24Z
timestamp_note: "stamped from the wall clock in the same process as the write (MEMORY #34)"
source: Will (Telegram) — Will-Telegram 8-image batch 2026-10-01 ~17:04Z (msgs 4835-4842), batch manifest BM-20261001-05
origin: ["Will Telegram photo (msg 4840): X @business (Bloomberg) 9/29 15:20 ET, US to Tap More Oil From Emergency Reserve as Fuel Prices Surge", "World Oil 9/29: US to release another 40 MMbbl from reserve; The National 9/29; Yahoo Finance: U.S. Taps Strategic Oil Reserve Again as Diesel Tops $6 (search extracts; DOE notice not opened)"]
domain: OIL_ENERGY
cluster: IRAN_HORMUZ
cluster_secondary: INFLATION_TRANSMISSION
entities: ["Strategic Petroleum Reserve", "DOE", "IEA coordinated release"]
confidence: 0.8
confidence_language: "Size and exchange structure from World Oil / search extracts of the Bloomberg-reported offer; the DOE notice itself was not opened by WALTER. 'Lowest since 1982 once completed' is a projection, not a level."
signal_type: pattern-match
safety_net: clear
verdict: "On 9/29 the US offered up to 40M bbl more from the SPR as an EXCHANGE (barrels returned later with a premium), not a sale. It is the last of the US's 172M bbl contribution to the coordinated release since the Iran war began. The SPR held 283.8M bbl in the week to 9/25 (EIA, per BRENT) and is projected to fall to its lowest since 1982 once this is delivered. Retail diesel is above $6/gal."
precedence: PRIORITY
action: ["BRENT"]
info: ["HAWK", "CARL", "HENRY", "RED"]
dispatch_note: "Source: Will-Telegram 8-image batch 2026-10-01 ~17:04Z (msgs 4835-4842), batch manifest BM-20261001-05, item 6. 'Already ours?' BOARD has the SPR LEVEL (-0928-010) but not this release; BRENT STATUS carries weekly SPR draws, no release line. MEMORY #35 applied: BRENT's live SPR basis is in STATUS (283.767M wk 9/25), not the frozen KB rows. OIL_ENERGY -> BRENT action (fold the offer into your SPR/supply ledger, including the exchange return obligation); HAWK/RED info; CARL info (pump-price pass-through); HENRY info. Cluster IRAN_HORMUZ: the release is the war-driven coordinated draw."
---

# The US is lending up to 40M more barrels from the strategic reserve, the last of its 172M-barrel war release. The reserve is heading to its lowest since 1982.

- **9/29: up to 40M barrels offered from the Strategic Petroleum Reserve (SPR)**, as an **exchange**: companies return the oil later, with extra barrels as interest. **Not a sale.**
- It is the **last tranche of the US's 172M-barrel share** of the coordinated international release since the Iran war began.
- **SPR level:** 283.8M barrels in the week to 9/25 (EIA, BRENT's live figure). Projected to reach its **lowest since 1982** once this is delivered.
- Context: US retail diesel is above **$6/gal**; gasoline above $4.

**So what:** this is the **last of the planned emergency barrels.** After it, the US has no further committed release to lean on into the midterms. And because it is an exchange, the barrels come back out of the market later.

## Caveats
- Exact size, delivery schedule and bid uptake are from news extracts; **the DOE notice was not opened.** An offer of "up to" 40M is not 40M delivered.
- "Lowest since 1982" is a **projection** on completion, not today's level.

Action BRENT: fold it into your SPR and supply ledger, including the return obligation. Canon: BRENT.
