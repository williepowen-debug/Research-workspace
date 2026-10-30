---
signal_id: "SIG-W-20261030-011"
date: "2026-10-30"
timestamp: "2026-10-30T19:21:04Z"
dispatched: "2026-10-30T19:21:04Z"
source: "Will X bookmarks 10/29-10/30 (9 items) + Rule 9 helper verification 2026-10-30T19:18Z (research/2026-10-30_bookmarks/verify-iran.md): UKMTO Warning 187-26 Update 001 via Safety4Sea/gCaptain; Reuters via syndicators; Oman Maritime Security Centre via Reuters/Anadolu; Siasat 10/30; NIAC 10/30; Al Jazeera 10/30"
origin: ["AGENTS/WALTER/research/2026-10-30_bookmarks/verify-iran.md", "https://www.siasat.com/qeshm-island-hit-by-explosions-as-iran-reports-naval-base-attack-3566996/", "https://www.aa.com.tr/en/middle-east/oman-evacuates-25-crew-from-panama-flagged-vessel-after-attack-sparks-fire/4106562", "https://x.com/Osinttechnical/status/2116012298460610712", "https://x.com/EUxReport/status/2115923125422764309", "https://x.com/HormuzLetter/status/2116191524765515807"]
domain: "GEOPOL_ENERGY"
cluster: "IRAN_HORMUZ"
cluster_secondary: "HYDROCARBON_INFRA"
signal_role: "primary_substance"
action: ["FALCON"]
info: ["HAWK", "BRENT", "SAM", "RED", "TERRY", "PROME"]
precedence: "IMMEDIATE"
signal_type: "divergence"
confidence: 0.75
confidence_language: "two hull attacks confirmed at official/UKMTO level; strike and refinery claims unconfirmed"
entities: ["LOUISE-1", "RITI", "UKMTO", "Oman-Maritime-Security-Centre", "Bandar-e-Jask", "Qeshm", "Ras-Tanura", "CENTCOM", "IRGC"]
resources: 6
safety_net: "not-triggered (no US naval vessel interdiction)"
event_window: "closed"
word_count: 627
dispatch_note: "Batch BM-20261030-01 items 4, 12, 17, 18, 23, 28, 30, 37, 38. Iran pre-dispatch guard executed: anchor read; IRAN_WAR_GUARDS read (vessel-sunk theater check, UKMTO UTC clock, intercepted->struck ratchet, Ras Tanura 2026-03-02 merge hazard, Qeshm/Jask July date traps). Rule 9 verdicts: Jask INDETERMINATE, limpet CORRECTED-FRAMING, Oman CONFIRMED (separate event), Ras Tanura INDETERMINATE leaning not established. Ladder #2 wording ('confirmed mine detonation on a hull') vs UKMTO's 'explosive devices attached above the waterline' is FALCON's adjudication; WALTER does not grade the rung. IMMEDIATE because two confirmed hull attacks plus an unresolved US-strike claim one week before the 11/3 midterms bear on FAL-07 and ladder #2/#3. Helper read Reuters only through syndicators; ukmto.org 403. NOT a full-sweep clock reset (next ~11/05)."
---
# Iran theater 10/29–10/30: two separate hull attacks near Khasab/Musandam confirmed; US strike on Jask unconfirmed; Ras Tanura distillation shutdown not established

**Vintage:** events 10/29 (UTC) into 10/30 local. Verified 10/30 ~15:18 ET by a Rule 9 helper (`AGENTS/WALTER/research/2026-10-30_bookmarks/verify-iran.md`). Maritime times are UKMTO UTC; theater-local reads one day later in the 20:00–24:00 UTC window.

| Claim (as bookmarked) | Verdict | What is established | What is NOT |
|---|---|---|---|
| "IRGC limpet-mined a tanker in the US-protected Hormuz lane, blew a hole in its engine room" (@Osinttechnical) | **CORRECTED-FRAMING** | UKMTO Warning 187-26 Update 001 (10/30): a small boat attached **two explosive devices above the waterline** of a tanker ~25 NM NE of Khasab, outbound, 10/29; engine-room fire, vessel briefly disabled, crew safe, **continued its voyage**. Vessel **LOUISE 1** (Panama), per Reuters citing three maritime security sources; UKMTO did not name it. | Attacker (UKMTO none; Reuters: "not immediately clear"). "IRGC", "hole" and "US-protected lane" are the poster's words. Whether UKMTO's separate 10/29 ~1600 GMT "unknown projectile" report near Khasab is the same hull. |
| "Oman's Navy evacuates 25 crew from vessel struck 1.6 NM off Musandam" (@FirstSquawk, @BRICSinfo) | **CONFIRMED, separate event** | Oman Maritime Security Centre: Royal Navy of Oman evacuated **25 crew** from a Panama-flagged commercial vessel that was "targeted" and caught fire ~1.6 NM off Musandam (Reuters, Anadolu 10/30). Name reported **RITI / RIT1**, unreconciled. | Weapon, attacker, vessel type, sinking (none reported). |
| "US struck the IRGC naval base at Bandar-e-Jask, 4 missiles" (@EUxReport 10/29 21:45Z; @TheLetterxen with a deleted Barak Ravid post on two weeks of US "self-defense strikes") | **INDETERMINATE** | Explosions near Jask and Qeshm night of 10/29–30 reported locally; an Iranian-military-linked platform says four missiles hit a naval facility at Jask. An **anonymous** CENTCOM official (relayed by Faytuks Network) described a US jet striking a **missile launcher on Qeshm**, not Jask. Tasnim/Mehr: a hostile jet was **intercepted**. | Any on-record US (CENTCOM, Pentagon, White House) or Iranian official acknowledgment of a US strike; any tier-1 wire attribution. White House 10/22 line: no attack on Iran before the 11/3 midterms. ⚠️ Date traps live: Anadolu 07-13, AFP 07-16, CENTCOM Qeshm 06-03, US denial 09-10. |
| "Aramco shut the main distillation unit at 550 kb/d Ras Tanura after Houthi attacks, per Bloomberg" (@HormuzLetter 10/30 15:32Z) | **INDETERMINATE, leaning not established** | Houthis claimed Ras Tanura on 10/27 and again on 10/29 (with Abqaiq, Rabigh, airports; Al Jazeera 10/30, uncorroborated). Satellite read (Maritime Executive 10/28) suggests a **cracking** unit and stopped flaring — inference. | Any 10/30 Bloomberg article; any Aramco/SPA/MoE statement. ⚠️ **Merge hazard:** Bloomberg **2026-03-02** "Aramco halts Ras Tanura" carried the same 550 kb/d figure. |

**Posture (items 17, 23, 30):** US Army mass-casualty burial drills (Fox), a large airlift toward the region with Gulf states warned to prepare for a possible resumption — posture only, consistent with the WSJ 10/27 post-midterm-campaign line; ladder #3 not fired on posture. **CENTCOM 10/28:** shipping lanes cleared of sea mines ("These claims are FALSE"); a limpet attached by a small boat is not a sea mine, so the two do not conflict.

**ACTION FALCON:** grade (1) whether LOUISE 1's above-waterline explosive devices count toward ladder #2 ("confirmed mine detonation on a hull"; no sinking) and your loss census (neither hull reported sunk); (2) whether the Qeshm launcher strike, if officially acknowledged, is a qualifying FAL-07 US strike given its reported "self-defense" framing; (3) RITI/RIT1 identity and attribution. WALTER does not grade the rungs.

**INFO HAWK** (synthesis), **BRENT** (Ras Tanura state stays ATTACKED-claim / DAMAGED-inference / SHUT-unestablished; Hormuz risk premium), **SAM** (oil-yen), **RED / TERRY / PROME** (BOARD pull).

**Limits:** Reuters, AP, AFP read only via syndicators; ukmto.org 403 (warning PDF unread); X posts not fetched by the helper.
