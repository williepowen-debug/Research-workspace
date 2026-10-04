---
signal_id: SIG-W-20261004-011
date: 2026-10-04
timestamp: 2026-10-04T20:36Z
time_dispatched: 2026-10-04T20:36Z
timestamp_note: stamped from the system clock at write, not typed
source: x-bookmark
origin: ["Will X-bookmark scan (boot 7h) 2026-10-04", "@business/Bloomberg 11:05Z (Iraq VLCC)", "@Kalshi 19:30Z (IEA 325M)", "verify-research subagent 2026-10-04 (Opus): Bloomberg 10/04, Euronews 10/02, IEA March-2026 program"]
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
entities: ["Iraq", "SOMO", "VLCC", "Strait-of-Hormuz", "IEA", "G7", "emergency-oil-release"]
confidence: 0.8
confidence_language: "Iraq VLCC = Bloomberg-reported commercial fact. IEA-325M = verified labeling correction of an already-known program."
signal_type: catalyst
safety_net: clear
precedence: ROUTINE
action: ["BRENT"]
info: ["HAWK", "FALCON"]
---

# Iraq arranges a VLCC to ship crude PAST Hormuz → BRENT · + kills the viral "IEA released 325M barrels" misframe

## 1. IRAQ MOVES TO SHIP CRUDE OUTSIDE THE GULF (Bloomberg, confirmed)
Bloomberg (10/04, via @business): **Iraq's state tanker company arranged a VLCC to transport ~2 million barrels of crude BEYOND the Strait of Hormuz** — a first step toward offering oil from outside the Persian Gulf.
- **So what:** a structural supplier RESPONSE to Hormuz war-risk — the same bypass logic as Saudi's East-West pipeline to the Red Sea, now from Iraq by sea. A genuine (if early/small) diversification of Gulf crude away from the chokepoint. BRENT owns the crude-flow read; this is a data point on how producers are routing around Hormuz, not a price event by itself.

## 2. "IEA RELEASED 325 MILLION BARRELS" — MISFRAME, DO NOT PROPAGATE (verify: CORRECTED-FRAMING)
A viral post (@Kalshi 19:30Z) read "IEA says 325 MILLION barrels of emergency oil have been released." **Verify at primary: the 325M is the CUMULATIVE running tally of the pre-existing IEA 400M-bbl program announced 2026-03-11 (~290M by July, now ~325M released, ~75M still to come). It is NOT a new October release and NOT the G7 action.**
- ⛔ **Do NOT carry "325M released [today]" as a fresh catalyst** — it double-counts an old program.
- ✅ **The genuinely new supply catalyst is the G7 100M bbl (diesel+crude, ~830 kbd over 4 months), announced 2026-10-02 — and that is ALREADY on the board (`SIG-W-20261002-009`).** Nothing new to route on the release; this entry exists to kill the inflated number before it travels.

## RECIPIENT ACTION
- **BRENT (action, oil owner):** note the Iraq-VLCC Hormuz-bypass as a structural flow datapoint; and the "IEA 325M" = cumulative-of-the-March-400M, not a new release (G7 100M on 10/02 = `-1002-009` is the actual new catalyst). Net any Monday crude read off the confirmed facts, not the inflated figure.
- **HAWK / FALCON (info):** Hormuz-bypass theater context.

## CAVEATS
- Iraq VLCC: one cargo (~2M bbl) — a directional signal, not a volume shift yet. Bloomberg single-wire; BRENT reads the primary if pricing off it.
- IEA figure: the 400M program is real and large, but it is the OLD program's running total, not a 10/04 event.
