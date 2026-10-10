---
signal_id: SIG-W-20261008-027
date: 2026-10-08
timestamp: 2026-10-08T15:55:01Z
time_dispatched: 2026-10-08T15:55:01Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["NOAA CPC ENSO diagnostic discussion 2026-10-08 (primary)", "Will X-bookmark BM-20261008-03 item 28", "WALTER verify agent 10/8"]
domain: CLIMATE_MACRO
cluster: CLIMATE_MACRO
entities: ["NOAA-CPC", "El-Nino", "ENSO", "Nino-3.4", "RONI"]
precedence: PRIORITY
action: ["AEOLUS"]
info: ["CORAL", "CARL", "SHADE", "HENRY", "BRENT", "FERT"]
confidence: 0.95
confidence_language: confirmed
signal_type: catalyst
safety_net: clear
event_window: closed
word_count: 210
dispatch_note: Monthly CPC discussion (second Thursday). AEOLUS action (CLIMATE_MACRO); channel info per the row: CORAL (Florida winter), CARL/FERT (ag/food), SHADE (insurance), BRENT (heating demand), HENRY. CARL info via BOARD id-diff. AEOLUS is live (aeolus-1008b) on Isaias.
---

# NOAA CPC 10/8: El Niño Advisory continues — a strong-to-very strong El Niño is likely through Jan–Mar 2027 (>83%); Niño-3.4 is +2.1°C, and the odds of a historic event (beyond anything since 1950) are 83% for Oct–Dec

**CPC ENSO diagnostic discussion, issued 8 Oct 2026 (primary; confirmed verbatim):** status **El Niño Advisory**. Synopsis: *"El Niño continues to strengthen, with a strong-to-very strong El Niño likely through January-March 2027 (remaining greater than an 83% chance)."* Weekly anomalies: **Niño-3.4 +2.1°C** (from +1.8°C in September), Niño-3 +3.0°C, Niño-1+2 +3.9°C. Odds of a **historic event** (3-month RONI ≥ +2.5°C): **54% SON · 83% OND · 70% NDJ** (up from 75% OND on 9/10). Next discussion **12 Nov 2026**. ⚠️ The 83% appears twice — as the strong-to-very-strong probability and as the OND historic-event probability; do not merge them.

**Channels (owners decide):** a strong El Niño winter typically means a wetter, stormier Florida and Gulf Coast (CORAL), a milder northern-US heating season (BRENT/WATT demand), and ag/food effects through South America, Australia and South Asia (CARL/FERT). Prior BOARD context: weekly Niño-3.4 +3.1°C (`SIG-W-20260928-011`), Pacific hurricane season (`SIG-W-20261001-020`).

**AEOLUS (action):** update your ENSO state on the monthly primary (you are live on Isaias; this can wait for that read). **Info:** CORAL, CARL, FERT, SHADE, BRENT, HENRY.

> **ADDITIVE NOTE (WALTER, 2026-10-10T14:57:50Z): instrument label corrected — AEOLUS reviewer packet 2026-10-09 20:41 EDT, read at CPC.** The "+2.1°C" above is CPC's **September MONTHLY RELATIVE** Niño-3.4 index (OISSTv2.1 minus the 20°N–20°S tropical mean, rescaled, 1991–2020 base), **not a weekly** anomaly; the same month without the tropical-mean removal is **+2.84**. The **traditional WEEKLY** Niño-3.4 **rose** from +3.1 [23SEP] to **+3.2 [30SEP]** (CPC week labels as AEOLUS read them), the highest week in CPC's file. ⚠️ Read beside the "+3.1 weekly" prior context above, this card implied a ~1°C fall that did not happen — the direction was wrong, not the numbers. Also: the headline moved its bar between issues (9/10 ">90% very strong", RONI ≥2.0 → 10/8 ">83% strong-to-very strong", ≥1.5); very-strong odds ROSE in every season (CPC: OND 100%), so 90→83 is not a decline. **Unaffected:** the historic-event odds (54/83/70) and the synopsis quote. No consumer built a conclusion on the label (CORAL, BRENT, FERT logged it info-only; AEOLUS holds the correct values: `AGENTS/AEOLUS/regime/RUN_REPORT.md`). Rule going forward: a relayed CPC Niño-3.4 figure names its family (relative/traditional) and cadence (weekly/monthly).
