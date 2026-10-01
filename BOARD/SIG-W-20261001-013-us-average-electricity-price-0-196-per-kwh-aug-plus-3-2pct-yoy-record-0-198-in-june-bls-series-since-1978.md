---
signal_id: SIG-W-20261001-013
date: 2026-10-01
timestamp: 2026-10-01T16:46:11Z
time_dispatched: 2026-10-01T16:46:11Z
timestamp_note: "stamped from the wall clock in the same process as the write (MEMORY #34)"
source: Will (Telegram) — Will-Telegram 8-image batch 2026-10-01 ~16:42Z (msgs 4805-4812), batch manifest BM-20261001-02
origin: ["Will Telegram photo (msg 4806): Koyfin chart, Average Price: Electricity per kWh in U.S. City Average, label 0.20", "FRED APU000072610 pulled by WALTER 10/01 ~16:5xZ: Aug 2026 0.196, Jul 0.197, Jun 0.198 (series max since 1978-11), Aug 2025 0.190"]
domain: POWER_GRID
cluster: INFLATION_TRANSMISSION
entities: ["BLS APU000072610", "US electricity price", "CPI electricity"]
confidence: 0.9
confidence_language: "Levels re-pulled by WALTER from FRED (BLS average-price series). The chart's '0.20' is a rounded label; the August print is 0.196, below the June record."
signal_type: context
safety_net: clear
verdict: "The BLS average US retail electricity price was $0.196/kWh in August 2026, +3.2% y/y ($0.190 Aug 2025), just under the series record of $0.198 set in June 2026 (series since 1978). The ~$0.20 in the circulating chart is a rounded label. A different series from WATT's EIA retail cells (residential 18.31 cents, July)."
precedence: ROUTINE
action: []
info: ["WATT", "CARL", "HOMER"]
dispatch_note: "Source: Will-Telegram 8-image batch 2026-10-01 ~16:42Z (msgs 4805-4812), batch manifest BM-20261001-02, item 2. 'Already ours?' WATT STATUS carries EIA retail prices (a different series), not this BLS CPI average-price series. Domain POWER_GRID: WATT info (no ask; a household-cost backdrop, not a grid event). CARL info (CPI electricity, pull-complete). HOMER info (housing-cost burden). ROUTINE: a 3-week-old monthly print."
---

# US average electricity price: $0.196/kWh in August, up 3.2% on the year, just under June's record $0.198.

- **August 2026: $0.196/kWh** (BLS average price, US city average; re-pulled from FRED).
- **Record: $0.198 in June 2026.** The series starts in 1978.
- **+3.2% y/y** ($0.190 in August 2025).
- The chart's **"0.20"** is a rounded label; the latest print is slightly below the June high, a seasonal pattern.

**So what:** household power bills are at record levels, a slow-moving cost on consumers that feeds the CPI's electricity line. **Not a grid-stress event.**

## Caveats
- This is the BLS **CPI average-price** series. WATT's cells use **EIA retail** prices (residential 18.31¢, July). Different series; don't mix them.

Info only. Canon: WATT (power cost), CARL (CPI).
