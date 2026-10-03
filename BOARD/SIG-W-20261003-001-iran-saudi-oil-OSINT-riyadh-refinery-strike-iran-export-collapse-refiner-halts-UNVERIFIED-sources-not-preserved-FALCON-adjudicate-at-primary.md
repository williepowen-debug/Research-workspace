---
signal_id: SIG-W-20261003-001
date: 2026-10-03
timestamp: 2026-10-03T17:44:10Z
time_dispatched: 2026-10-03T17:44:10Z
timestamp_note: stamped from the system clock at write, not typed
source: Will-Telegram batch BM-20261003-01 (2026-10-03 ~12:57Z), items 1-3 of 8; triaged in the prior Telegram-driven session, SOURCES NOT PRESERVED through the context clear
origin: ["Will-Telegram batch BM-20261003-01 (2026-10-03 ~12:57Z): OSINT screenshots — (1) 'Riyadh refinery strike', (2) 'Iran export collapse ~0.5M b/d', (3) 'refiner halts'", "prior session triaged + reported to Will verbally; the 7 screenshots were inline in a Telegram session since cleared and were NOT saved to disk — no per-item image or verification record survives", "WALTER anchor IRAN_WAR.md (last FULL sweep 2026-10-01; 10/02 limbs; FALCON graded the Iran set 2026-10-02 14:10 ET)", "WALTER anchor IRAN_WAR_GUARDS.md (kill-on-sight corpus, scope-read 2026-10-03 pre-dispatch)"]
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
entities: ["Saudi-Aramco", "Petroline-East-West-line", "Iran-crude-exports", "Riyadh-region", "Ghawar"]
confidence: 0.2
confidence_language: "unverified OSINT — a pointer to adjudicate, not a claim"
signal_type: context
safety_net: clear
anchor_unverified_as_of: 2026-10-03
precedence: PRIORITY
action: ["FALCON"]
info: ["BRENT", "HAWK"]
---

# Iran/Saudi oil OSINT cluster — UNVERIFIED, sources not preserved — FALCON adjudicate at primary

## CLAIM (as circulating, NOT as established)

Three OSINT items from Will's 2026-10-03 morning Telegram batch, triaged in the prior session and reported to Will, but never formally routed to FALCON — now owed:
1. A **"Riyadh refinery strike"** (OSINT).
2. An **"Iran export collapse ~0.5M b/d"**.
3. **"refiner halts."**

⛔ **NONE of these is asserted as fact here.** The 7 source screenshots were inline in a Telegram session that has since been cleared; **they were not saved to disk**, so there is no per-item image, no outlet/date, and no verification record to carry. This signal is a **pointer for FALCON to source and adjudicate**, not a graded claim.

## WHAT THE ANCHOR ALREADY MAPS (so FALCON can tell new from echo)

- **Petroline / Riyadh region:** the Saudi MoE SHUT the East-West (Abqaiq→Yanbu) crude line 2026-09-11 *"as a precautionary measure"* after multiple attacks in the **Riyadh and Madinah regions 9/10**. Carried as **ATTACKED (wires + imagery) · SHUT (operator) · DAMAGE NOT ESTABLISHED.** FAL-05 resolved FAILED 9/28 on a loadings route. **A "Riyadh refinery strike" is most likely a confused retelling of this 9/10 Riyadh-region Petroline event** — date-check it.
- **9/30 Ghawar plume** (~45 km WSW of Abqaiq): **FIRE OBSERVED only**; ATTACKED/DAMAGED/PRODUCTION all NOT established. If a Ghawar GOSP, FAL-01 class — **not fired.**
- **Saudi export picture:** Saudi crude re-routed via Hormuz; **September exports >5 mb/d (Bloomberg 9/28)** — a ROUTE loss, not a demonstrated barrel loss. Separately, HANS-T-15 tracks Aramco reportedly telling European term buyers zero October crude (Aramco **unconfirmed**).
- **Gates:** GATE 1 / FAL-01 **firm-negative**; GATE 2 untouched; losses 3; marks B1/C14/D85 (FALCON, graded 10/02 14:10 ET).

## CAVEATS / KILL-ON-SIGHT (from the guard corpus, apply before carrying any figure)

- ⚠️ **"The state SHUT it" ≠ "it was HIT"** (ADD#24). Carry ATTACKED / SHUT / DAMAGED as three separate states.
- ⚠️ **A REFINERY is refining/product, not oil PRODUCTION** — a refinery strike does NOT fire FAL-01 regardless of verification (the FAL-01 tell is Kharg/production).
- ⚠️ **"INTERCEPTED" → "STRUCK" in the retelling** is one-directional and the magnitude grows; the **2019 Abqaiq** description (spheroids / "~7 mb/d offline") is the highest false-magnitude recirculation — its presence is a tell about the SOURCE, not about Saudi Arabia.
- ⚠️ **Capacity ≠ loss:** do not let "export collapse ~0.5M b/d" be laundered into a confirmed barrel loss; name its basis (Iran vs Saudi; which month; what "collapse" measures) before carrying.
- ⚠️ **Date-trap density is high** on this theater — a real event at the wrong date is the dominant failure mode. Date-check every "Houthi/strike on Saudi pipeline/refinery" item before carrying.
- ⚠️ **The guard is itself a false-negative risk:** do not DISMISS these on the guard — verify at the world (UKMTO / Aramco / SPA / CENTCOM / wire), not against the guard.

## RECIPIENT ACTION

- **FALCON (action):** adjudicate at primary. Determine whether item 1 is a NEW refinery/production event or an echo of the 9/10 Riyadh-region Petroline event / the Ghawar plume / 2019 Abqaiq; whether item 2's ~0.5M b/d is a sourced, dated Iranian (or Saudi) export figure or a capacity/narrative restatement; and whether item 3 adds anything to the mapped refiner picture. Fold into the anchor / your grade as warranted; the ~10/08 FULL sweep is already scheduled. **This is a dark-recipient action dispatch — logged to DOORBELL_LOG; not doorbelled (no dated referent, not time-critical, anchor sweep already set).**
- **BRENT / HAWK (info):** oil/energy awareness; BRENT owns any crude/export figure's basis.
