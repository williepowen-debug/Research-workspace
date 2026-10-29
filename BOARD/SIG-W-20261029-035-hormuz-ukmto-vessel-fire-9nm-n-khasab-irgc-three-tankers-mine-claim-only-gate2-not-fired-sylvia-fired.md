---
signal_id: "SIG-W-20261029-035"
date: "2026-10-29"
timestamp: "2026-10-29T16:15:46Z"
dispatched: "2026-10-29T16:15:46Z"
source: "WALTER"
origin: ["https://www.newsquawk.com/headlines/ukmto-reports-a-vessel-is-on-fire-9-nautical-miles-north-of-khasab-oman", "https://www.aa.com.tr/en/middle-east/fire-reported-on-vessel-in-strait-of-hormuz-ukmto/4104568", "https://www.cbsnews.com/live-updates/iran-war-donald-trump-qatar-mediators-new-proposal-end-war/", "https://english.alarabiya.net/News/middle-east/2026/10/29/iran-s-irgc-says-three-tankers-on-fire-after-hitting-mines-in-hormuz-"]
domain: "GEOPOL_ENERGY"
cluster: "IRAN_HORMUZ"
action: ["FALCON"]
info: ["BRENT", "HAWK", "SAM", "RED"]
precedence: "IMMEDIATE"
signal_type: "catalyst"
confidence: 0.75
confidence_language: "UKMTO fire report via Anadolu/Newsquawk/CBS (ukmto.org not read); IRGC mine claim via CBS and Al Arabiya headline (body 403); Sylvia firing via CBS (Pentagon official)"
entities: ["UKMTO", "IRGC", "Strait-of-Hormuz", "Khasab", "CENTCOM", "Brett-Sylvia", "Hegseth", "Qatar"]
resources: 4
safety_net: "clear"
event_window: "closed"
word_count: 330
dispatch_note: "WALTER afternoon boot news sweep 10/29 (WebSearch + CBS live blog fetch). Iran pre-dispatch guard run: IRAN_WAR_GUARDS read whole this session (ADD#26 five discriminators, Tasnim mine-claim guard, theater check). Anchor full sweep 10/29 00:38Z. GATE 2 / ladder #2 NOT FIRED: no UKMTO, operator or CENTCOM confirmation of a mine hit or sinking. Delivery and consumption separate."
status: PARTIALLY-SUPERSEDED
status_ref: "SIG-W-20261029-037 (FALCON 10/29: Khasab vessel = dhow MSV QUBA, sank, NAVAREA IX 417/26; census 5 -> 6; ladder #2 NOT FIRED)"
status_date: 2026-10-29
---

> ⚠️ **LIFECYCLE TAG `PARTIALLY-SUPERSEDED` applied 2026-10-29 (WALTER, on FALCON's owner resolution).** BROKE: "the loss census (5)" and the unnamed-vessel framing; the Khasab vessel was the dhow MSV QUBA, which sank (SIG-W-20261029-037). WHAT SURVIVES: ladder #2 NOT FIRED; the IRGC three-tanker mine claim stays CLAIM-ONLY and unlinked; all other items.

# Hormuz: UKMTO reports a vessel on fire 9 NM north of Khasab (10/29 ~03:00Z); IRGC claims three tankers hit mines (CLAIM-ONLY); ladder #2 NOT FIRED

**Confirmed by UKMTO (advisory 10/29, event ~03:00 UTC):** the master of a third-party vessel reported a ship **on fire about 9 nautical miles north of Khasab, Oman** (inside the Strait). Vessel **not named**, flag and type not given, crew status unknown, **no damage assessment, no cause stated**; UKMTO classed it "suspicious activity" and told ships to transit with caution. Sources: Anadolu, Newsquawk, CBS live blog 2:59 AM ET. ukmto.org original not read (403 class).

**CLAIM-ONLY (IRGC Navy public relations, 10/29):** three tankers "struck naval mines and exploded" while using what the IRGC calls the **unauthorized southern route**; no names, flags, positions or times. ⛔ Do NOT merge the UKMTO fire with the IRGC claim: no source links them, and one UKMTO-confirmed fire is not three mine hits. ⛔ Never write "three tankers hit mines in Hormuz" or "mine confirmed". **Ladder #2 fires only on UKMTO/operator/CENTCOM confirmation of a mine detonation or a hostile sinking; neither exists as of this card.** IRGC spokesman Mohebi (CBS 10:27 AM ET) challenged CENTCOM to "prove" its mine-clearing claim with independent evidence. This is at least the sixth IRGC mine claim this month (10/17, 10/20, 10/22, 10/24, 10/27 per the anchor, now 10/29), none confirmed.

**Also 10/29 (CBS live blog, claims and reports, not graded):** IRGC Navy says it landed a US reconnaissance drone (claim); Iran's navy claims "more than 20 attacks" on US warships (claim; no CENTCOM confirmation found; CENTCOM has denied every prior hit claim) - **not a FLASH**: no verified interdiction of a US vessel. **Hegseth removed Lt. Gen. Brett Sylvia** (Joint Staff strategy, plans and policy) on 10/28 after an accusation of leaking classified Iran-war information (Pentagon official to CBS; an accusation, not a finding). AP: US warned allies to prepare for possible post-midterm strikes (same line as WSJ 10/27, anchor). Iran's answer to Qatar's draft deal (handed over Sunday 10/25 per Reuters; a senior Iranian official denied a new proposal) expected around Saturday 10/31.

**FALCON ACTION:** resolve the Khasab fire (vessel identity, cause, ADD#26 five discriminators) and whether it is one of the three IRGC-claimed hulls; FALCON owns GATE 2 and the loss census (5). BRENT info (shipping, war risk; BZZ26 113.80 intraday 16:13Z, -1.3%, not a settle). HAWK, SAM, RED info.
