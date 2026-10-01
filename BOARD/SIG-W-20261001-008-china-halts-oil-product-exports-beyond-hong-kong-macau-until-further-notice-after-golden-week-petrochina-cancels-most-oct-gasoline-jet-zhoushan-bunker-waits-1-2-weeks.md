---
signal_id: SIG-W-20261001-008
date: 2026-10-01
timestamp: 2026-10-01T16:31:23Z
time_dispatched: 2026-10-01T16:31:23Z
timestamp_note: "stamped from the wall clock in the same process as the write (MEMORY #34)"
source: Will (Telegram) — Will-Telegram 7-image batch 2026-10-01 ~16:28Z (msgs 4796-4802), batch manifest BM-20261001-01
origin: ["Will Telegram photos (msgs 4800, 4802): X @staunovo relaying Reuters 10/01; X @mercoglianos relaying gCaptain 10/01", "Reuters 10/01 (via TradingView newsml_L1N45N04W, Business Recorder): four people briefed, said Thursday", "Bloomberg 10/01: China cancels some fuel shipments to support domestic supply", "gCaptain 10/01: Ships Face Fuel Delays at China's Zhoushan on Supply Squeeze; ENGINE East of Suez outlook 9/29"]
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
cluster_secondary: ASIA_CHINA
entities: ["PetroChina", "Zhejiang Petrochemical (ZPC)", "Zhoushan", "Beijing export quota", "gasoline", "jet fuel", "VLSFO", "HSFO"]
confidence: 0.8
confidence_language: "Export halt: Reuters (four sources) + Bloomberg, unofficial (no Beijing notice published). Zhoushan waits: gCaptain + ENGINE, vendor lead times. Pre-10/01 Zhoushan items (typhoon, Lunar New Year) are DATE TRAPS and are not carried."
signal_type: pattern-match
safety_net: clear
verdict: "Chinese refiners have suspended oil-product exports beyond Hong Kong and Macau until further notice from Beijing after Golden Week (ends 10/7), per Reuters (four sources, 10/01). PetroChina cancelled most of its planned October gasoline and jet cargoes, and ZPC scheduled none for the holiday week; Bloomberg corroborates. Beijing set no restart date. Separately, ships at Zhoushan, China's main bunker hub, now wait ~1-2 weeks for fuel vs 1-2 days normally (gCaptain; ENGINE: VLSFO ~14d, HSFO 7-10d) as refiners shift output away from fuel oil. This widens -1001-003's context line ('PetroChina cancellations') into a country-level halt."
precedence: PRIORITY
action: ["BRENT"]
info: ["ZHAO", "HAWK", "CARL", "RED"]
dispatch_note: "Source: Will-Telegram 7-image batch 2026-10-01 ~16:28Z (msgs 4796-4802), batch manifest BM-20261001-01, items 3 + 7 of 7 (images 3 and 7), folded: same mechanism (Chinese refiners prioritising domestic gasoline/diesel). 'Already ours?' check: PetroChina appears only as price-attribution context in -1001-003; BRENT STATUS (10/01 10:17) has no China line; Zhoushan absent from BOARD. Domain OIL_ENERGY -> BRENT action. ZHAO info (Beijing export-quota policy, ASIA_CONTAGION). CARL info (fuel-price pass-through; same CARL line as -0930-006). HAWK/RED per row. Not IMMEDIATE: no registered boundary row keys on Asian product exports; BRENT grades magnitude."
---

# China has halted fuel exports beyond Hong Kong and Macau until Beijing says otherwise after Golden Week, and ships at Zhoushan are waiting 1–2 weeks for bunker fuel.

**What happened (Reuters 10/01, four sources; Bloomberg corroborates):**
- Chinese refiners **suspended oil-product exports beyond Hong Kong and Macau until further notice from Beijing**, to follow the Golden Week holiday (ends **10/7**). **No restart date was set.**
- **PetroChina** cancelled **most of its planned October gasoline and jet cargoes**, many committed in the past two weeks. **ZPC** scheduled none during the holiday week.
- The stated cause is protecting domestic supply, with Chinese gasoline and diesel stocks reported at multi-year lows.

**Same squeeze, shipping leg (gCaptain 10/01; ENGINE 9/29):** ships at **Zhoushan**, China's main bunkering hub, wait **~1–2 weeks** for fuel vs 1–2 days normally. Lead times: VLSFO ~14 days, HSFO 7–10. Refiners are shifting yield toward gasoline and diesel and cutting residual fuel oil.

**So what:** this lands on top of `-0930-006` (India MRPL tenders cancelled, Russia's diesel ban to 10/31, the US October diesel squeeze). **A third major exporter is pulling product off the market in the same week.** Brent December traded **$101.36 (+3.4%)** at 12:14 ET 10/01 (vendor intraday), and the wire attributes the move to the Chinese cancellations.

## Caveats
- **Unofficial:** no published Beijing notice. Sources-say, two independent wires.
- **No volume figure** for the suspended exports is in either wire. Do not size it from China's monthly export totals.
- ⛔ Older Zhoushan stories (typhoon, Lunar New Year) surface in search and are **date traps**.

Action BRENT: size it against your product balance. Canon: BRENT.
