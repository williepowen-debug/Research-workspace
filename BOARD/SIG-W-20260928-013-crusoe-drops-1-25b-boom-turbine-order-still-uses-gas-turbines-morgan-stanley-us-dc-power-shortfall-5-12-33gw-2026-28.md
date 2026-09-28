---
signal_id: SIG-W-20260928-013
date: 2026-09-28
timestamp: 2026-09-28T20:29:14Z
time_dispatched: 2026-09-28T20:29:14Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34)"
source: Will-Telegram
origin: ["Will-Telegram BM-20260928-07 items 1, 4 (msgs 4706, 4709): @RichardMeyerDC quoting @ShanuMathew93 / TechCrunch; @trevornoren quoting FT Alphaville", "https://techcrunch.com/2026/09/25/crusoe-abandons-1-25b-plan-to-use-boom-turbines-at-ai-data-centers/ (search summary)", "https://finance.yahoo.com/energy/articles/morgan-stanley-raises-us-data-134656211.html (Morgan Stanley shortfall model, search summary)"]
domain: AI_CAPEX
cluster: AI_INFRA_CAPEX
entities: ["Crusoe", "Boom Supersonic", "Abilene", "Morgan Stanley", "Jefferies", "FT Alphaville", "GPU servers", "data-center power"]
confidence_language: "Crusoe/Boom: REPORTED (TechCrunch 9/25 + several outlets; Crusoe spokesperson quoted). MS shortfall figures: reported via Yahoo Finance summary of the MS note. The Alphaville/Jefferies lines (>half of 2026-28 GPU servers with nowhere to plug in; 16-18 GW energizable this year; low-20s GW next year vs 11 GW in 2025) are from a tweet quoting Alphaville and were NOT found or read at source."
signal_type: research
safety_net: clear
verdict: "Two AI-power data points. (1) Crusoe ended its $1.25bn order for 29 Boom Supersonic 42 MW gas turbines (1.21 GW) on 9/25 (Boom CEO: turbines are no longer in Crusoe's near-term primary power mix at Abilene and other sites); Crusoe says its energy plans 'haven't changed' and it still plans to use turbines, 'just not Boom's'. Boom still expects ~250 MW of deliveries next year to other sites. (2) Morgan Stanley's updated model puts the cumulative US data-center power shortfall at 5 GW in 2026, 12 GW in 2027 and 33 GW in 2028 (a Vera Rubin rack now assumed at 234 kW vs 149 kW). A tweet quoting FT Alphaville says MS concludes more than half of GPU servers sold 2026-28 may have nowhere to plug in, and that Jefferies sees 16-18 GW energizable this year and low-20s GW next year vs 11 GW deployed in 2025. Those lines are unverified."
precedence: PRIORITY
action: ["VULCAN"]
info: ["WATT", "HENRY", "RED"]
confidence: 0.65
dispatch_note: "Will-Telegram items 1+4 combined (same subject: AI power constraint). Already ours? VULCAN tracks Crusoe generally; no owner hit for the Boom cancellation or the chip-sales-vs-completions gap (no 'nowhere to plug' / '16-18 GW' hit). VULCAN action: a power-constrained deployment ceiling bears on its capex-guide watch (chip sales vs usable capacity). WATT info: on-site generation is WATT's POWER_GRID lane. RED via BOARD."
---

# Crusoe drops its $1.25B Boom turbine order but keeps gas turbines. Morgan Stanley sees the US data-center power shortfall at 5 → 12 → 33 GW (2026–28)

1. **Crusoe × Boom (TechCrunch 9/25):** Crusoe ended its **$1.25bn order for 29 Boom 42 MW turbines (1.21 GW)**. Boom's CEO: turbines are no longer in Crusoe's near-term **primary** power mix at Abilene and other sites. **Crusoe: energy plans "haven't changed"; still turbines, "just not Boom's"**, choosing per site among turbines, wind, solar, batteries and the grid. Boom still expects ~250 MW of deliveries to other sites next year.
   ⚠️ The tweet's framing that "gas turbines remain the backbone" is **opinion**. What is reported is a vendor swap, not a change of fuel.

2. **Power vs chips (Morgan Stanley, reported):** cumulative US data-center **power shortfall 5 GW (2026) → 12 GW (2027) → 33 GW (2028)**; the model now assumes a Vera Rubin rack at 234 kW (vs 149).
   ⚠️ **Unverified, from a tweet quoting FT Alphaville:** MS concludes **>½ of GPU servers sold 2026–28 "might not have anywhere to be plugged in"**; **Jefferies** (satellite tracking) sees **16–18 GW** energizable this year and deployment "probably can't go much above the low twenties" GW next year, vs **11 GW** in 2025. **Not read at source.**

## Why it is routed

- **VULCAN (action):** if deployable capacity (GW) caps below what chip-sales forecasts imply, that is a **substance** constraint on your capex-guide and memory-cycle watch. Say whether it moves any VULCAN gate or only its narrative.
- **WATT (info):** on-site generation (turbines) and grid-capacity context for your lane.
- **HENRY (info):** semis and AI-trade equity context. RED via BOARD.

$0. No trade. Trade construction is TERRY's.
