---
signal_id: SIG-W-20261003-003
date: 2026-10-03
timestamp: 2026-10-03T17:57:29Z
time_dispatched: 2026-10-03T17:57:29Z
timestamp_note: stamped from the system clock at write, not typed
source: x-bookmark
origin: ["Will X-bookmark id=2106369474... slice (backlog recent-slice pull 2026-10-03)", "@MenchOsint, X post 2026-10-03T17:41:08Z: 'Update: ~16:20 UTC Local report of Ballistic Missile launch from Yemen; ~16:20 UTC Disruption over Riyadh airspace; 16:35 UTC NASA FIRMS detects additional fires at Riyadh ARAMCO Refinery'", "WALTER anchor IRAN_WAR.md + IRAN_WAR_GUARDS.md (scope-read 2026-10-03)"]
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
entities: ["Saudi-Aramco", "Riyadh-refinery", "Yemen-Houthi", "NASA-FIRMS"]
confidence: 0.25
confidence_language: "unverified single-channel OSINT — a current pointer to adjudicate, not a claim"
signal_type: context
safety_net: clear
anchor_unverified_as_of: 2026-10-03
precedence: PRIORITY
action: ["FALCON"]
info: ["BRENT", "HAWK"]
---

# CURRENT (10/03) OSINT: Yemen ballistic missile + NASA FIRMS fires at Riyadh ARAMCO refinery — UNVERIFIED single-channel — FALCON adjudicate

## CLAIM (as circulating, NOT as established)

@MenchOsint (X, **2026-10-03 17:41:08Z**): a **ballistic missile launch from Yemen ~16:20 UTC**, **disruption over Riyadh airspace ~16:20 UTC**, and **NASA FIRMS additional fires at Riyadh's ARAMCO refinery 16:35 UTC**. This is the **current, dated** version of the "Riyadh refinery strike" item that arrived vaguer in the morning batch (see SIG-W-20261003-001) — now with a specific source and time.

## STATUS / why this is a pointer, not a fact

⛔ **Not asserted.** Applicable guard cautions, all firing here:
- **NASA FIRMS is a fire-detection feed, NOT a strike confirmation** — ADD#15: do NOT propagate NASA FIRMS as confirmed without published coordinates. A FIRMS thermal anomaly is fire observed, not "refinery struck."
- **@MenchOsint is a flagged single channel** (guard corpus: Rozbiani/Marins/MenchOsint are aligned commentators = ONE channel, not independent corroboration). Load-bearing sources are Reuters/WaPo/Maritime Executive/SPA/Aramco.
- **A refinery is refining/product, NOT oil production** — even if confirmed, this does NOT fire FAL-01 (the FAL-01 tell is Kharg/production). It would be a refining-asset event.
- **Riyadh-region collision:** the 9/10 Petroline attacks were in the Riyadh/Madinah regions; carry ATTACKED/SHUT/DAMAGED separately and do not merge a new Riyadh fire with the mapped pipeline event.
- **"INTERCEPTED → STRUCK" one-directional retelling** + the 2019 Abqaiq recirculation remain the highest false-magnitude risks.

## RECIPIENT ACTION

- **FALCON (action):** this is a CURRENT (today) Iran-cluster OSINT item, unlike the stale batch items in -001. Adjudicate at primary (SPA/Aramco/CENTCOM/wire + published FIRMS coordinates): is there a confirmed missile impact on a Riyadh refining asset, or is this a FIRMS thermal anomaly + airspace-disruption report on a single channel? Fold into the anchor / your grade; any confirmed production-asset or refining-asset hit is a state change. Pre-dispatch Iran-cluster re-verify trigger fires on this. **Dark-recipient action — logged DOORBELL_LOG; not doorbelled (no dated referent; FALCON's ~10/08 sweep already set; FALCON consumes at next boot).**
- **BRENT / HAWK (info):** oil/energy awareness.
