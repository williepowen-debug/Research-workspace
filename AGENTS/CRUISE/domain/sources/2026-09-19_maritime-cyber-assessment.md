# Maritime cyber targeting — what it is, what it isn't, and what it means for the Big 3

**CRUISE · 2026-09-19 · prompted by Will (Sal Mercogliano, *What's Going On With Shipping*, transcript supplied)**
**Verdict up front: REAL EVENTS, OVERSTATED HEADLINES, NO CRUISE EXPOSURE ON THE EVIDENCED CHANNEL — and a live cruise cyber exposure the video never mentions, running through data rather than the helm. $0, no trade, no vector moved.**

⚠️ **Sourcing class: this whole file is SECONDARY.** Every figure below is press or a press-quoted official. No primary filing, no agency document read. Graded **C2–D3** and should not carry a trade on its own.

---

## 1. What is actually established, and by whom — three tiers, and the sourcing runs INVERSE to the alarm

The single most important thing in this story is **who says what about the VL Prosperity**, because the three available versions disagree and the most frightening one has the weakest provenance.

| Claim | Source | Grade |
|---|---|---|
| Networks of both vessels were compromised; USCG/FBI boarded 8/21 and 8/24, Gulf of Mexico; *"foreign cyber actors"*, unidentified | **FBI + USCG joint statement** | **B2** — the official record |
| ⛔ **"no reports of operational disruptions, vessel instability, physical danger to crews, or environmental impacts"** | **USCG**, reported Bloomberg/gCaptain 9/16–17 | **B2** |
| Hackers "interfered with the ship's speed and fuel systems"; lost comms >1 day | **CBS News — sourced to IRANIAN MEDIA** | **D3** |
| Headline: hackers "took control of navigation, propulsion and cargo systems" | TechCrunch **headline**; its own body text reverts to *"interfered with"* and notes the agencies' statement **does not specify which systems** | **D4 as written** |

🔑 **The alarming version traces to Iranian state media during an active US–Iran conflict — a party with an obvious incentive to overstate its reach — and the US agencies' own position is that nothing operational was disrupted.** A headline and its own article body disagree here, which is the tell.

⇒ **The video's cautious framing is better calibrated than the coverage it is reacting to.** Mercogliano's core claim — that remotely steering a ship is not the realistic threat — survives contact with the official record.

**Established pattern (not in dispute):** three suspected tanker/LNG incidents in about a month, and **US agencies tracking cyber threats against ~20 vessels worldwide**, with the Coast Guard asking for advance notice before any of them enters a US port. VL Prosperity is Liberian-flagged, 333 m, >2M bbl, compromised 8/7 en route Egypt→US, now anchored off Galveston.

**The one incident with a real-world commercial effect is the LNG carrier, and it is BRENT's, not mine:** **Vivit Africa** (⛔ *not* "Vivid Africa" — the transcript misspells it), H-Line Shipping (South Korea), on long-term charter to **Vitol**, carrying US gas to the Adriatic LNG terminal at Rovigo. Crew lost access to internal control networks, the vessel **idled off Italy without discharging**, then **turned back toward Algeciras**. That is an actual cargo-delivery failure, not merely an IT event.

---

## 2. Where the video is wrong

1. ⛔ **"It cost Maersk $10 billion in damages" — wrong by roughly 33×.** Maersk's own guidance put its NotPetya loss at **$250–300M** (Aug 2017). The **~$10B is the global NotPetya total** (White House assessment), across all victims. The video has swapped a worldwide aggregate for one company's loss. **This is the most citable error in the piece** and the one most likely to propagate, because it is stated as a hard number attached to a named company.
2. **"Vivid Africa"** → **Vivit Africa**. Also transcription artifacts that break searches: *"Maris lines"* → Maersk · *"Napeta"* → NotPetya · *"Costco"* → COSCO · *"the dolly"* → the **Dali**.
3. **"We have not seen that level yet"** (a system failing near a navigational hazard) — **arguably overtaken, on weak sourcing.** If the speed/fuel interference on VL Prosperity is real, that is the beginning of that class. It rests on Iranian media, so it is not established — but the video's flat negative is no longer safe either.
4. **Everything else in the piece that I checked holds up**: the Maersk/NotPetya mechanism (cargo and loading systems, not ship control), the IT-vs-OT distinction, ports being the softer target, and the connectivity-raises-exposure argument.

---

## 3. The industry-wide weakness the video gestures at, confirmed

Vessel navigation and propulsion run on **CAN bus and NMEA 2000** — protocols with **no security designed in**, leaving critical systems visible to basic network scanning. Starlink/LEO was on **~75,000 vessels by end-2024**, and the emerging classification standard is **IACS UR E26/E27**. So the attack surface is genuinely widening; the video's direction of travel is right even where its numbers are not.

---

## 4. ⚓ CRUISE domain — the actual answer for CCL / RCL / NCLH

### (a) On the evidenced channel, cruise is not in this story at all
**No cruise vessel appears anywhere** — not among the ~20 monitored, not in any of the three incidents. Every named target is a **tanker or LNG carrier**, and the theater link is Iran/energy. **The targeting logic is energy supply, not passenger shipping.** ⛔ A search returning no cruise vessel is weak evidence: the ~20 ships are unnamed, so this is **SEARCH-NOT-FOUND, not a verified absence.**

### (b) But cruise has a real, current cyber exposure — through DATA, not the helm — and Carnival is the sector's worst offender
| When | What |
|---|---|
| 2019–2021 | Four separate cybersecurity events |
| Aug 2020 – Mar 2021 | Three more, incl. **two ransomware**; names, addresses, DOBs, passport numbers, SSNs, health data, card numbers exposed |
| **Jun 2022** | **$5M NYDFS penalty** + **$1.25M to 45 state AGs = $6.25M**; cited failures incl. a **10-month** reporting delay and **no MFA** on internal email |
| **14 Apr 2026** | **Fresh breach** — social engineering of an employee account; **ShinyHunters**; **~6M people**, 8.7M records / 7.5M unique emails; **Holland America's Mariner Society** loyalty programme. Notices dated **27 May 2026**; 24-month TransUnion monitoring, enrolment by 31 Aug 2026 |

### (c) 🔑 The conclusion that matters, and it is a NEGATIVE
**For cruise the financial channel is regulatory fines, notification and remediation cost, and booking-system downtime — not hull loss or grounding.** At every magnitude observed so far this is an **opex line, not a thesis**: the 2022 penalties totalled **$6.25M** against CCL's guided **~$1.86B** Q3 adjusted net income — about **0.3%**. **⛔ This is not a trade and I am not proposing one.**

### (d) The two paths on which it WOULD reach a registered vector — neither is live
- **`VX-CRU-04`** (re-cut today) fires on **ONE** announced Big-3 **Gulf/Red Sea/Suez** itinerary cancellation. A cyber-forced cancellation would count. **Nothing here does that.**
- **`VX-CRU-03`** (booking pace) — a booking/reservation-system outage during a wave period would be a genuine demand-side hit. **Not observed.**

### (e) The structural point worth carrying forward
Cruise ships are **the most connected vessels afloat** — fleet-wide Starlink, guest wifi, payment, medical and casino systems — **and they carry thousands of people.** So the *tail* is worse for cruise than for a tanker even though *current targeting* is not aimed at them, and the large guest-facing IT estate is exactly what makes Carnival's repeat data breaches the sector's live exposure. **Bluntly: the realistic cruise cyber disaster is a ransomware event that takes down bookings and embarkation in wave season, not a hacker steering a ship into a bridge.**

---

## 5. ⚠️ Flagged, NOT carried — a date-check I owe before this becomes a finding
A search surfaced **"Norwegian cancels 50+ sailings, redeploys four ships"** (Gem, Dawn, Getaway, Joy). **I am not logging it as a signal**, for two reasons: the itineraries are **Caribbean/Bahamas homeports** (Tampa, Jacksonville, PortMiami, Port Canaveral), **so it is NOT a `VX-CRU-04` trip** — that band counts Gulf/Red Sea/Suez; and the earliest dated copy is **Cruise Industry News, September 2025**, for the 2026-27 season, i.e. **possibly a year-old story re-surfacing**. Date-check before mechanism-check — the exact contaminant WALTER warned about with the 2018 Saudi-halt story. **Owed: confirm the announcement date at NCLH before treating it as current.** If it IS current it is a demand-side datum for `VX-CRU-03`/`VX-CRU-05`, not a cyber one.

---

## 6. Routing — the parts that are not mine
- **FALCON** — the Iran attribution, the ~20-vessel monitoring list, and the fact that the scariest claim is Iranian-media-sourced. FALCON's own *"Cyber / data chokepoint"* row is scored **2** and marked *"Not freshly reviewed"*, carried since **Jun 8** — this is new evidence against a stale row.
- **BRENT** — **Vivit Africa is a physical LNG delivery failure**, not just an IT incident: idled off Rovigo, turned back to Algeciras with US cargo undelivered.
- **Not mine at all:** COSCO intelligence allegations, ZPMC crane modems, Port of LA / GAO maritime-cyber oversight.

⛔ **Fleet-wide blind spot, stated plainly:** grep finds **zero** mentions of Vivit Africa, VL Prosperity or this incident class anywhere in `AGENTS/` or `BOARD/`. Nobody had it. Will brought it in from outside — which is the WQ-245 weekend/collector gap doing exactly what it does.
