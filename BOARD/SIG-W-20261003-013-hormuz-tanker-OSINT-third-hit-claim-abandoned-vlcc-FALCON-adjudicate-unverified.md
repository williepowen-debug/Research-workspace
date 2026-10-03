---
signal_id: SIG-W-20261003-013
date: 2026-10-03
timestamp: 2026-10-03T23:0xZ
time_dispatched: 2026-10-03T23:0xZ
timestamp_note: stamped from the system clock at write, not typed
source: phone
origin: ["Will-Telegram 6-image batch 2026-10-03 ~22:54Z (img 6)", "@MerruX / Ali (quoted post 14h) — single-channel OSINT; plugs 'OverwatchX.app' (a forecast product = promotional/credibility flag)"]
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
entities: ["Strait-of-Hormuz", "VLCC", "tanker-attack", "Iran"]
confidence: 0.3
confidence_language: "UNVERIFIED single-channel OSINT with a product plug; unnamed hulls; date ambiguous ('today' = ?); 'likely abandoned' is NOT 'sunk'. FALCON adjudicates at primary (UKMTO) — do NOT carry any of this as fact."
signal_type: pattern-match
safety_net: clear
precedence: PRIORITY
action: ["FALCON"]
info: ["BRENT", "RED"]
cluster_mediating: false
---

# Hormuz tanker OSINT — "3rd tanker hit / abandoned VLCC still burning" (UNVERIFIED) → FALCON adjudicate at primary

## THE CLAIM (from Will's phone batch — treat as UNVERIFIED)

@MerruX (Ali), quoted post 14h + a satellite-image post: (1) **the VLCC hit in the Strait of Hormuz "on the 2nd" is "still on fire and likely abandoned"** per a landsat image; (2) vessels still **crossing via the Omani route**; (3) quoted: **"WOW Third Tanker hit by Iran today! 2 VLCC and 1 unknown. Strait of Hormuz getting Rough."** The account plugs **OverwatchX.app** (a paid forecast product).

## ⛔ GUARD DISCIPLINE — why this is NOT a fire and must NOT be propagated as fact

Checked against `anchors/IRAN_WAR_GUARDS.md` (pre-dispatch, Iran-cluster):
- **"VESSEL SUNK must be THEATER-checked, then it is still a CLAIM":** this IS the right theater (Hormuz), but **"likely abandoned" ≠ "confirmed sunk."** GATE 2 needs a **confirmed hostile sinking or mine detonation** — not satisfied. **Losses stay 3** (per the 10/01 sweep + FALCON's 10/02 grade); nothing here overturns that.
- **ADD#26 — "unknown projectile, Hormuz" is a recurring phrase, not an event ID.** Key every item on 5 discriminators (event-vs-report time, vessel identity, direction, mechanism, UKMTO position). **Same day ≠ same event; same phrase ≠ same event.** These hulls are **UNNAMED** → not matchable to the anchor's logged 10/02 hits (`-017` Kazimah III, `-018` outbound unnamed).
- **Date ambiguity:** "hit on the 2nd" + "3rd tanker hit **today**" — "today" is unanchored (post is 14h old, screenshot now). The 9/20–21 LR Stephanie / Al Maryah case shows BOTH desks mis-dating tanker OSINT; do not assume "today" = 10/3.
- **Credibility flag:** single channel + a **product plug** (OverwatchX.app) — promotional incentive to dramatize.

## RECIPIENT ACTION

- **FALCON (action, theater owner):** adjudicate at **UKMTO / primary** — is there a 10/3 Hormuz hit beyond the logged 10/02 events, and is any vessel confirmed sunk/abandoned (vs under-way)? This bears on the GATE-2 ladder (a 4th confirmed sinking) and the anchor's transit state. **WALTER carries NONE of this as confirmed; it is a FALCON-verify item.**
- **BRENT / RED (info, via BOARD):** transit-risk context (BRENT); adversarial watch (RED).

## ✅ ADDENDUM 2026-10-03 ~23:1xZ (PROME read-only pre-fetch; additive)

PROME's reader identified the vessel: **the "abandoned VLCC still burning" is KAZIMAH III, hit 10/01** (= the anchor's `-017` Kazimah III), NOT a new 10/03 event — so **`-013`'s "3rd tanker hit today" DATE IS OFF**; this re-reports the 10/01 hit (exactly the ADD#26 date-trap / unnamed-hull class this signal flagged). **Nothing new fires; losses stay 3.** No FALCON session needed tonight (PROME rec). The caveats on this signal held — it was correctly carried as UNVERIFIED and not as fact.
