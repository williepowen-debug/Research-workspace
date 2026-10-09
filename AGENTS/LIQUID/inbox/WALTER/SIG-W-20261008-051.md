---
signal_id: SIG-W-20261008-051
date: 2026-10-08
timestamp: 2026-10-09T00:43:59Z
time_dispatched: 2026-10-09T00:43:59Z
timestamp_note: "stamped from the wall clock in the same process as the write (MEMORY #34)"
source: "WALTER evening sweep 10/8 (agent C, f1)"
origin: ["CNBC quote service (UK 30Y prior close), vendor", "TradingEconomics 10/8 (already in -037), vendor", "AGENTS/WALTER/research/2026-10-08_evening-sweep/C_markets-credit-fed-asia.md"]
domain: EUROPE_MACRO
cluster: FED_FRAMEWORK
entities: ["UK 30-year gilt", "HANS-T-13", "CNBC", "TradingEconomics"]
precedence: PRIORITY
action: ["HANS", "BOND"]
info: ["LIQUID"]
confidence: 0.7
confidence_language: "vendor closes only; the official DMO/BoE close was not obtained"
signal_type: research
safety_net: clear
event_window: closed
word_count: 153
dispatch_note: "Grade input only (HANS grades; DOCKET L637 is the 10/9 read). Updates -037: both vendor closes now sit under 6.00, but CNBC's is 0.3bp from the line, inside any cross-vendor gap. No fire claimed and no NOT-FIRED claimed by WALTER."
---

# Gilt grade input: CNBC's prior close for the UK 30-year is 5.9972%, 0.3bp under HANS-T-13's 6.00 line; both vendor closes are under the line, but CNBC's sits inside any cross-vendor gap

| Basis | UK 30Y, 10/8 close | vs T-13 (>6.00) |
|---|---|---|
| CNBC "prior close" | **5.9972%** | 0.3bp under |
| TradingEconomics (already in `-037`) | 5.9384% | ~6bp under |

- The armed rule in HANS's registry grades on the **TE daily close**, with CNBC as the cross-check. On those terms both read under 6.00.
- But 0.3bp is inside the gap between vendors, so this does not settle the grade. HANS's own note asks for an official close (DMO/BoE), which neither vendor is.
- **WALTER makes no fire or not-fired call.**

**HANS (action):** grade at your 10/9 read (DOCKET L637). **BOND (action):** a time-critical gilt item per the EUROPE_MACRO limit. **LIQUID (info).** Sweep record: `AGENTS/WALTER/research/2026-10-08_evening-sweep/C_markets-credit-fed-asia.md` (f1).
