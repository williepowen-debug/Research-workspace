---
signal_id: SIG-W-20261008-037
date: 2026-10-08
timestamp: 2026-10-08T20:31:28Z
time_dispatched: 2026-10-08T20:31:28Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["TradingEconomics UK 30Y/10Y pages (read ~16:2x ET by sweep agent)", "Investing.com historical data", "ANSA (BTP spread, TTF)", "research/2026-10-08_afternoon-sweep/C_europe-asia-ru-ai-cre.md"]
domain: EUROPE_MACRO
cluster: FED_FRAMEWORK
entities: ["UK-30Y-gilt", "UK-10Y-gilt", "HANS-T-13", "HANS-T-06", "TradingEconomics", "Investing.com", "BTP-Bund spread"]
precedence: PRIORITY
action: ["HANS", "BOND"]
info: ["LIQUID"]
confidence: 0.7
confidence_language: reports
signal_type: threshold-crossed
safety_net: clear
event_window: closed
word_count: 176
dispatch_note: "Grade input only; HANS grades on its registry close source; DOCKET L637 carries the 10/9 close read. UPDATE to -032 (later vendor reads), not a correction. signal_type threshold-crossed is the closest enum for a grade input (as -032)."
---

# Gilt grade input update to -032: after the London close, vendor closes for 10/8 sit well under both HANS lines — TE 30Y 5.9384% / 10Y 5.4238% — but on a London-close basis 10/8 is still too close to call

- **TradingEconomics** (HANS's registered close source for T-13/T-06): 30Y **5.9384%** (~6bp under >6.00), 10Y **5.4238%** (~8bp under >5.50). **Investing.com:** 30Y 5.938 (its day low, "Closed" ~13:00 ET), 10Y 5.4270. Vendor reads, ~16:2x ET.
- ⚠️ **The drop came AFTER the 16:30 BST London close.** HANS's own CNBC path read the 30Y at 5.9914 → 6.0015 at the close. So the TE rows now read not-fired with room, but on a London-close basis 10/8 remains inside the vendor gap. Official DMO close unread (bot wall). **HANS grades; DOCKET L637 carries the 10/9 read.**
- Italy–Germany spread closed **111bp** from 115 (ANSA). TTF unresolved (ANSA €79.5 +1.8% vs TE €77.31 −1%); no HANS rung crossed either way.
- ⛔ Do NOT carry Mitrade's *"French 10Y above 5% / spread 160bp"*: no data source, conflicts with every vendor.
