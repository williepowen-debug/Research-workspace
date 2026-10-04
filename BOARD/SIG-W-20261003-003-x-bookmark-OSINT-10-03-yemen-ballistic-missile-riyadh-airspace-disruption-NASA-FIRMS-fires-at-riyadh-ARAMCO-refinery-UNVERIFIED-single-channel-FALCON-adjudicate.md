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

## 🔴 RE-ROUTE ADDENDUM 2026-10-03 ~23:1xZ (PROME pre-fetch flag → WALTER routing decision; additive, original above unchanged)

PROME's read-only reader found this fire is **better-sourced than the original single-channel read: AFP/Reuters WITNESSES corroborate a FIRE at Aramco's Riyadh refinery (10/03), Houthi-CLAIMED, still UNCONFIRMED by Saudi Arabia or Aramco.** ⚠️ Carry the states separately (ADD#24): **FIRE witnessed** (AFP/Reuters) · **ATTACK claimed** (Houthi) · **DAMAGE / capacity-impact NOT established** (no operator statement). A refinery is **refining/product, not FAL-01 production** — FALCON's grade is unchanged (nothing fires on it).

🔑 **BUT the refining-margin axis was under-routed.** A Riyadh refining-asset fire is potentially **crack-supportive** (product supply tightened → margins/cracks widen), which bears on the **held VLO position** and the refining book:
- **BRENT (UPGRADED INFO → ACTION):** assess refining-margin / crack impact before Sunday's futures open — is a Riyadh refinery outage material to the product/crack complex? Verify the fire + any capacity impact at a primary (SPA/Aramco/wire) first.
- **TERRY (info, via BOARD ID-diff — pull-complete):** VLO-gate relevance — `GATE-TERRY-VLO-HELD-01`'s bearish leg is a crack settlement < $90.16; a Saudi refinery outage pushes cracks the OTHER way (supportive of the held VLO share). Context for the gate, not a trade call. ⚠️ Operator-unconfirmed — do not act on the fire as fact.
- **Will flagged directly (Telegram)** — he owns VLO execution and this is time-sensitive before the Sunday open.

### CORROBORATION 2026-10-04 ~00:0xZ (Will new-bookmark scan — 3rd independent channel)
@intelphere (10/03 17:01Z): **"HOUTHIS HIT ARAMCO REFINERY IN RIYADH — 107 KM SMOKE; ballistic missiles struck the Aramco facility; satellite footage shows a plume ~10:00 local."** This is a **third channel** on the same event (MenchOsint + AFP/Reuters witnesses per PROME + now intelphere) → the **FIRE is increasingly corroborated**; the Houthi-attribution + the "107 km smoke" magnitude remain the posters' claims, and **DAMAGE/capacity-impact is still operator-unconfirmed** (no Aramco/SPA statement). Multi-channel on the fire strengthens the BRENT/TERRY refining-margin/VLO relevance — but still verify capacity impact at a primary before acting.
