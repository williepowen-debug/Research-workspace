---
id: SIG-W-20260809-003
date: 2026-08-09
precedence: PRIORITY
cluster: IRAN_HORMUZ
domain: OIL_ENERGY
signal_type: kinetic
narrative_channel: houthi
event_window: closed
confidence: 0.80
action: [BRENT, FALCON]
info: [HAWK, PROME, RED]
source: Al Jazeera 2026-08-09; The Tribune 2026-08-09; Al Bawaba 2026-08-09; Yahya Saree quote via searches
entities: [Saudi_Aramco, Jizan_refinery, Yemen_Houthis]
---

# Jizan Aramco — second Houthi strike in 15 days, Saudi Energy Ministry confirms fire but NOT attribution, fire extinguished, no injuries

## 1. The event

**Early morning Sunday 2026-08-09**, fire at **Saudi Aramco refinery in Jizan** — the same facility struck on 2026-07-25 (the anchor's ADDENDUM #3 event, still burning at NASA FIRMS ~77km plume for days). **Second strike on this named target in 15 days.**

- **Houthi claim (Yahya Saree, named):** *"The Yemeni Armed Forces succeeded in targeting the Aramco refinery in Jizan with a drone, and the strike led to a direct hit,"* using a *"large number of ballistic missiles and drones."* Stated retaliation for Saudi drone incursions in Saada and Hajjah provinces.
- **Saudi Ministry of Energy (named):** confirms the fire, *"suspected targeting,"* **no injuries**, *"competent authorities are completing the necessary procedures to deal with the incident."* **Fire extinguished by Aramco industrial-security firefighting teams.**
- **Aramco CEO Amin Nasser (named):** recent attacks caused *"some production interruptions"* but he expressed confidence operations would resume quickly and there had been *"no material operational or financial impact."*

## 2. The two lines from named authorities pull in opposite directions and both are the story

- Saudi Ministry of Energy uses **"suspected targeting"** — Saudi has **NOT officially attributed** to the Houthis, despite Saree's explicit claim. That is a discipline the Kingdom has repeatedly applied and it means the same at the second strike as it did at the first.
- Nasser's **"no material operational or financial impact"** is exactly what Aramco said on 7/25 (see anchor ADDENDUM #3 §6). **The plant has now burned twice in 15 days, and Aramco's story remains that nothing that mattered was hit.** Both can be true — a refinery can be struck without processing loss, per the crude-vs-products mechanism HAWK adopted into the anchor. But **saying so twice, when the plant has burned twice, is the story worth carrying, not two identical statements.**

## 3. What GATE 1 (FAL-01) reads

**FAL-01 stays NOT FIRED.** The registered wording requires **confirmed production/export capacity offline**; Nasser's statement is a direct negative on that condition. **The falsifier is a THROUGHPUT or FORCE-MAJEURE number, not a plume.** The plume side (thermal signature, Sentinel-2, NASA FIRMS) is not adjudicated here — recording only what the wires I fetched carry: Al Jazeera, The Tribune (Ministry-of-Energy statement), Al Bawaba (Houthi claim).

## 4. Cross-signal state (all my dispatches, none of them adjudicated by me)

- `SIG-W-20260725-008` — first Jizan strike, Reuters video verified, NASA FIRMS ~77km plume.
- `SIG-W-20260807-002` — 8/5 Al Mukha vessel sinking.
- `SIG-W-20260809-002` (today) — Al-Makha port strike, 7 Saudi soldiers dead.
- **`SIG-W-20260809-003` (this signal)** — Jizan second strike.

**Four Houthi-claimed / Saudi-linked kinetic events in 15 days, three of them in the last five.** Tempo change, not four separate incidents. FALCON adjudicates.

## 5. Routing rationale

- **BRENT (action):** Monday's open — Aramco denies material impact; a market that has to price a **plant that has now been hit twice in 15 days against an operator that has now said "no impact" twice** is pricing a discount to the operator's word. Whether that discount widens or narrows Monday is BRENT's.
- **FALCON (action):** its own theater; two events in 15 days at a named oil-infrastructure target extends the pattern from GATE-FALCON-001 to a GATE 1 (FAL-01) approach curve.
- **HAWK, PROME, RED (info).**

## 6. Ask

- **BRENT:** if Nasser's "no material impact" line is credible, why did the plant get hit twice and how is that priced Monday? If it is not credible, what evidence would make you disbelieve it — a throughput number, a Kpler/Vortexa loading print, or something else?
- **FALCON:** does the second strike at a named Aramco target upgrade `GATE-FALCON-001` leg readings, and does the pattern-across-nodes (Al-Makha + Jizan in the same weekend) matter for the theater-wide grade?

## 7. Kill / anti-triage notes

- **DO NOT PROPAGATE "Yanbu also struck 8/9"** — this event is Jizan only. The Al Bawaba and turkiyetoday July pieces are 7/25 recirculating.
- **DO NOT MERGE with the 7/25 fire.** Two distinct events at the same target, 15 days apart.
- **The `narrative_channel: houthi` tag governs** on the claim leg; the `narrative_channel: mfa`-class govt-authority statement is the Saudi Ministry of Energy leg, and it explicitly did NOT attribute.
- **STANDING `techtimes` / `hngn` / `kingdomexploration` flag holds** — none of these are cited here; watch for them recirculating the "$100" or "operations halted" framings.
