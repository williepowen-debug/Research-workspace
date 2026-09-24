---
signal_id: SIG-W-20260924-021
date: 2026-09-24
timestamp: 2026-09-24T20:40:55Z
time_dispatched: 2026-09-24T20:40:55Z
source: RESEARCH-INTAKE
origin: ["RESEARCH-INTAKE lane run 2026-09-24T18:47Z, newssweep NEW_WATCH saudi-redsea x7 (BM-20260924-02 item 8)", "Read by WALTER: Reuters via Baird Maritime, 2026-09-24 18:19 (body fetched 20:3xZ); headlines only: Newsquawk, thecradle, Kpler 'Libya vs Yanbu', industrialinfo 09:53 GMT"]
domain: OIL_ENERGY
cluster: IRAN_HORMUZ
cluster_secondary: HYDROCARBON_INFRA
precedence: PRIORITY
action: ["BRENT"]
info: ["FALCON", "HENRY"]
entities: ["Yanbu", "Petroline", "East-West-Pipeline", "Saudi-Aramco", "Kpler", "BG-02", "FAL-05"]
confidence: 0.70
confidence_language: Reuters on unnamed sources plus Kpler scheduling data; Aramco did not comment on record; one contrary headline (industrialinfo) is UNREAD
signal_type: context
resources: 2
safety_net: clear
word_count: 400
anchor_verified_as_of: 2026-09-24
verdict: "Reuters (via Baird Maritime, 9/24 18:19): crude is flowing through the restarted East-West line to Red Sea coast refineries, but crude loading into tankers at Yanbu has NOT resumed as of 9/24. Kpler: two ships due to load 9/23 did not; ~6 crude tankers are due 9/24-27 (4 Aframax, 1 Suezmax, 1 VLCC). Aramco reportedly told European refiners it is building a 'critical mass' of volumes first; full capacity may take six weeks or more. Bears on BRENT's BG-02 grade at 9/25 17:00 ET. One contrary headline (industrialinfo, 'Saudi Oil Loaded from Port at Yanbu') is unread and earlier in the day."
---

# Yanbu: the pipeline restarted, but tankers are not loading crude yet (as of 9/24)

**Short version:** Reuters reported at 18:19 on 9/24 (via Baird Maritime) that crude is again moving through Saudi Arabia's East-West pipeline, **to the Red Sea coast refineries**. **Crude loading into tankers at Yanbu has not resumed.** Kpler data: **two ships due to load on 9/23 did not load.** About **six** crude tankers are due to load **9/24–27** (4 Aframax, 1 Suezmax, 1 VLCC). Aramco has reportedly told European refiners it is still building a "critical mass" of volumes at Yanbu before it resumes crude deliveries.

## Why BRENT gets it as ACTION
**BG-02's window is 9/25 17:00 ET**, tomorrow. That grade depends on restored export throughput. BRENT's STATUS already carries a Kpler "no Yanbu load" read. **This adds a wire report that the pipe is running into refineries, not tankers, and names the 9/23 misses and the 9/24–27 schedule.** Under BG-02 C1–C6, AIS and vendor reads corroborate and never fire. How this report weighs is BRENT's call.

## Carry these states separately (guard ADD#24)
- **RESTARTED** (the pipeline): Reuters, unnamed sources, 9/22. Aramco has not confirmed on record.
- **DAMAGED:** Reuters now states "three pumping stations … were damaged in the September 11 drone attacks." **That is the wire's statement, not an operator confirmation.** The anchor still carries DAMAGE as unconfirmed by an operator.
- **LOADING:** NOT resumed as of 9/24, per Reuters and Kpler.
- ⛔ **Do not carry "4 mb/d" or "4% of global supply" as a loss.** That is the line's throughput when running, i.e. CAPACITY language (ADD#24 ③).
- ⛔ **No force majeure is stated anywhere in this item** (ADD#25).

## Caveats
1. **A contrary headline is UNREAD:** industrialinfo, 9/24 09:53 GMT, "Saudi Oil Loaded from Port at Yanbu after Pipeline Attack." It is earlier than the Reuters piece and may describe a product or pre-shutdown lifting. **WALTER did not read its body. Do not score either source as wrong** (two-track guard).
2. **Attribution:** Reuters' background line says Saudi Arabia "has blamed" the drones on Iraqi militia. WALTER has not verified a Saudi on-record attribution. The anchor carries Rubio naming Kataib Hezbollah (9/22). **FALCON owns attribution.**
3. **Also on the lane, context only (headline read, no state change):** Reuters 9/24, "At UN, 80 countries demand reopening of Hormuz, condemn Iran, Houthi attacks." A statement, not an instrument; ladder item 5 does not move.

## Requested action
BRENT: weigh this in the BG-02 grade at 9/25 17:00 ET. FALCON, HENRY: info.
