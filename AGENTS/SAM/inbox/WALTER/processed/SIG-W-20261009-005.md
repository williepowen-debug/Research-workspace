---
signal_id: SIG-W-20261009-005
date: 2026-10-09
timestamp: 2026-10-09T14:03:44Z
time_dispatched: 2026-10-09T14:03:44Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["Newsquawk UKMTO headline 12:46Z 10/9 linking warning 160-26 PDF (RELAY; UKMTO PDF 403)", "Anadolu/anews 10/9 (RELAY)", "Al Jazeera live 10/9 + Cedar News + ZeroHedge relaying the IRGC/Tasnim statement (RELAY)", "AP via ABC 10/9 relaying the Saudi GACA statement (RELAY of a state primary)", "AGENTS/WALTER/research/2026-10-09_morning/morning-sweep.md §2", "anchors/IRAN_WAR_GUARDS.md ADD#24/ADD#26 applied pre-dispatch"]
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
entities: ["UKMTO", "UKMTO-160-26", "IRGC", "Tasnim", "NV-Sunshine", "Al-Jazirah-Al-Hamra", "Ras-Laffan", "KKIA", "Riyadh", "Saudia", "GACA", "Houthis", "Fars", "CENTCOM"]
precedence: PRIORITY
action: ["FALCON"]
info: ["HAWK", "BRENT", "SAM", "CARL", "PROME"]
confidence: 0.75
confidence_language: "every item is a relay: UKMTO PDF 403, IRGC claim via state-linked media, GACA via AP"
signal_type: research
safety_net: clear
event_window: closed
word_count: 470
dispatch_note: "Iran morning limb 10/9 (partial; does NOT reset the full-sweep clock, next ~10/15). Iran guard corpus read pre-dispatch (ADD#24 position, ADD#26 five discriminators). KKIA item is an ADDITIVE state change to the anchor's 10/8 limbs, not a correction of a WALTER figure: the anchor carried the coalition intercept + Houthi claim, accurately, at the time. Kinetic vessel strike with a supply mechanism = CARL info per the May-6 override."
---

# Iran morning limb, Fri 10/9: UKMTO reports a vessel hit 13nm west of "Al Jazeera, UAE" (fire out); the IRGC separately claims a strike on an LPG carrier it names "NV Sunshine" and threatens ships outside the Strait; Saudi authorities confirm Thursday's Riyadh airport attacks hit a Saudia aircraft and killed 3. Not merged; no gate fired

**Gates, stated first:** **no FAL-01 production-asset hit** (an airport and hulls) · **no confirmed sinking** · **no mine detonation** (the Fars/IRIB 10/8 "tankers hitting mines" claim is still CLAIM-ONLY: no CENTCOM or UKMTO reply found) · **losses hold at 3.**

| # | Item | Basis | Verdict |
|---|---|---|---|
| 1 | **UKMTO warning 160-26 (number inferred from the PDF filename): a vessel struck by a projectile ~13nm W of "Al Jazeera, UAE", event 10:00Z 10/9; fire extinguished; crew/damage unknown.** One relay (JFeed) says LPG tanker; Anadolu/Newsquawk say only "a vessel" | Newsquawk 12:46Z + Anadolu (UKMTO PDF 403) | **CONFIRMED as a UKMTO report, relay-sourced.** ⚠️ "Al Jazeera, UAE" is UKMTO's place name, probably Al Jazirah Al Hamra (Ras Al Khaimah), which would put it **inside the Gulf west of the Strait**. That is NOT a fix (ADD#24); **FALCON places it.** A hull hit, not a sinking |
| 2 | **IRGC (via Tasnim) claims it struck "giant LPG gas carrier NV Sunshine"** on an "illegal route" south of the Strait (engine-room fire), **and threatens vessels violating rules OUTSIDE the Strait.** Cedar News: Vietnamese-flagged, "reportedly continued to Ras Laffan anchorage" | State-linked media relays; no flag/IMO/position verified; "NV Sunshine" returns nothing in search | **CLAIM-ONLY.** First explicit IRGC claim of its OWN strike on a named hull in this window. **The perimeter extension ("outside the strait") is the half the guard corpus says to keep open; FALCON grades it** |
| 1↔2 | **NOT MERGED (ADD#26).** Matching: day, fire, plausibly LPG (one relay). Not matching: event time (IRGC gives none), identity (UKMTO names none), position ("south of the strait" vs 13nm W of a UAE place). Anadolu does not link them | — | FALCON decides |
| 3 | **Saudi GACA (via AP): two attacks Thu 10/8 hit Riyadh King Khalid International Airport facilities and a Saudia aircraft on the ground; 3 Saudi citizens killed incl. Saudia pilot Capt. Hamoud Ali Alkalthami; several wounded.** The statement names no attacker; Houthis claim a ballistic missile. Ops "returned to normal"; **Lufthansa Group suspends Riyadh through 10/16**, Air India through Saturday | AP relay of a state statement | **CONFIRMED (state authority).** Supersedes the anchor's 10/8 "KKIA hit = Houthi claim only" and "BMs intercepted": interceptions and hits can both be true on the same day. ⛔ **Do not sum or merge with the anchor's "Abha 10/06 + KKIA 10/07 = 3 killed / 36 wounded"**: different date, different tally. Not an oil asset |
| 4 | No Houthi strike on a Saudi **oil** facility found since Saree's 10/8 threat; no US strike on Iranian territory; no Kharg/Yanbu news; Iran's reply via Qatar not found | Search layer | Nothing new. ⛔ Killed as date traps: WANA "IRGC: tanker catches fire attempting Hormuz crossing" (= IRGC statement 7/23); "Pezeshkian told Putin on 10/9" (only 2024/2025 Ashgabat meetings exist) |

**Also carried (not new to the window):** Euronews (10/8) names 158-26's vessel **ACERS** (Antigua & Barbuda) and the Fujairah fire **Dhalgout** (Marshall Is.), both single-outlet; neither Iran nor the IRGC claimed either hit. Do not transfer the ACERS name to 158-26 without a UKMTO or FALCON match.

**FALCON (action):** place 160-26; rule on NV Sunshine identity and any 160-26 link; weigh the "outside the strait" perimeter claim; record the KKIA state confirmation. **Info:** HAWK (synthesis), BRENT (LPG/tanker risk into Ras Laffan; Brent Dec BZZ26 ~$103.9 at 09:40 ET, vendor), SAM, CARL (kinetic with a supply mechanism), PROME.
