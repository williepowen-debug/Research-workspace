---
signal_id: SIG-W-20260928-008
date: 2026-09-28
timestamp: 2026-09-28T20:07:46Z
time_dispatched: 2026-09-28T20:07:46Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34)"
source: Will-Telegram
origin: ["Will-Telegram BM-20260928-05 items 7-8 (msgs 4701, 4702): @bonzerbarry X 9/27 21:38 relaying NBC; @HormuzReport X 9/27 12:47", "https://www.nbcnews.com/politics/national-security/us-marines-injured-recent-iranian-attack-rcna600097 (NBC primary, search summary)", "https://gcaptain.com/nbc-news-eight-marines-injured-in-previously-undisclosed-iranian-attack-in-hormuz/", "https://www.military.com/eight-marines-injured-with-smoke-inhalation-and-possible-tbi-in-previously-unreported-iranian-attack", "https://www.iranintl.com/en/202609275111 (IRGC-linked outlet claim of 19 ships)", "https://www.criticalthreats.org/analysis/iran-update-september-27-2026", "AGENTS/FALCON/workbook/KB.tsv KB-FALCON-164 (9/9 IRGC mass-targeting claim precedent)"]
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
entities: ["USMC", "NBC News", "Pentagon", "IRGC Navy", "Fars", "UKMTO", "The Hormuz Report", "Strait of Hormuz"]
confidence_language: "PART A (Marines) is REPORTED by NBC on three unnamed US officials and carried by gCaptain, Military.com, JPost and i24; the vessel is unidentified. PART B (19 ships) is an IRGC CLAIM via Fars with no evidence offered; UKMTO has reported no attacks since 9/23. The 'strait is empty' post is one account's reading of Sentinel imagery, not verified."
signal_type: catalyst
safety_net: clear
verdict: "A: NBC (9/27, three US officials) reports that on 9/14 an Iranian cruise missile struck a vessel in the Strait of Hormuz with US Marines aboard; 8 were injured (7 enlisted, 1 officer; smoke inhalation and possible traumatic brain injury; none serious; all returned to duty). The vessel was NOT a US Navy ship and is unidentified ('maritime vessel'); the Pentagon had not disclosed it. It sits one step short of FALCON's registered D 75→85 trigger (d), 'a US service member KILLED by Iranian/proxy action on/after 9/8': injured is not killed, so (d) is NOT met. B: the IRGC Navy claims (Fars, 9/27) it 'targeted' 19 vessels trying to transit since 9/25 (12 Friday, 7 Saturday); no evidence offered, and UKMTO reports no attacks since 9/23 while noting continued intimidation. A viral post says Sentinel imagery shows the strait 'completely empty'. Unverified."
precedence: IMMEDIATE
action: ["FALCON"]
info: ["HAWK", "BRENT", "SAM", "RED", "PROME"]
confidence: 0.75
dispatch_note: "Will-Telegram items 7+8 combined (Phase 1b, same theater, same owner), kept as two separately-graded parts. Iran guards read pre-dispatch: declaratory-control (an IRGC 'enforcing closure' statement is not a closure) · 'INTERCEPTED'→'STRUCK' drift · ADD#26 date-discrimination (A's event date is 9/14, reported 9/27; the relayer's 'possibly the same incident' as a 'US contracted vessel' attack is SPECULATION: do NOT merge) · mediated≠bilateral n/a. Already ours? No owner hit (FALCON/HAWK/BRENT/anchor) for the Marines or the 19-ship claim; FALCON KB-164 holds the 9/9 precedent claim. Bypass check: the FLASH line keys on a US NAVAL vessel; NBC says it was not one. IMMEDIATE on the US-personnel fact. Anchor next full sweep ~10/01. CARL not cc'd (no supply mechanism established)."
---

# NBC: 8 US Marines were injured 9/14 when an Iranian cruise missile hit a (non-Navy) vessel in Hormuz. Separately, the IRGC claims it "targeted" 19 ships 9/25–27, with no evidence

## A. Marines injured (reported, NBC on three US officials)

| Fact | Status |
|---|---|
| Iranian cruise missile struck a vessel in the Strait of Hormuz with US Marines aboard, **9/14** | ✅ reported (NBC primary; gCaptain, Military.com, JPost, i24) |
| **8 Marines injured** (7 enlisted, 1 officer): smoke inhalation, possible TBI; none serious; all back on duty | ✅ reported |
| The vessel was **NOT a US Navy ship**, described only as a "maritime vessel"; unidentified | ✅ reported |
| The Pentagon had **not disclosed** it; injuries entered in casualty tracking ~10 days later | ✅ reported |
| It is the same incident as the "US-contracted vessel hit by 4 drones and a cruise missile" | ⛔ **SPECULATION by the relaying account, not NBC. Do not merge.** |

**Why it matters:** Iranian fire has now reportedly injured US service members, and the event was **withheld for two weeks.** 🔑 **FALCON's D 75→85 rung trigger (d) is a US service member KILLED by Iranian/proxy action on/after 9/8 (KB-FALCON-147, Will-registered). These Marines were INJURED, so (d) is NOT met: a near-miss on a registered trigger, not a fire.** And the 9/5 IRGC missile fire at a US carrier and destroyer (KB-FALCON-121) shows US forces had been targeted before; WALTER did not establish whether any earlier injury is on record. That is a fact about the war's escalation state and about how complete the US-government record is. It does **not** by itself fire GATE 1 (no production asset) or GATE 2 (no sinking or mine). **FALCON grades the ladder.**

## B. The IRGC's 19-ship claim (claimed, not substantiated)

- **IRGC Navy (Fars, 9/27):** "targeted" **19 vessels** attempting to transit since 9/25: 12 on Friday evening, 7 on Saturday evening.
- **No evidence offered** (Iran International; Critical Threats). **UKMTO: no attacks reported since 9/23**, continued intimidation.
- **Precedent:** on **9/9** the IRGC claimed it targeted 2 US vessels, 8 tankers and 10 "violating" ships (FALCON KB-164).
- **@HormuzReport (9/27, 289K views):** "strait completely empty" per Sentinel-2 imagery. ⚠️ **One account; optical imagery at this resolution with clouds and haze does not establish a zero count.** Transits remain **FLOORS, not levels** (anchor).
- ⛔ **"Iran is enforcing its closure" is DECLARATORY CONTROL**: kill-on-sight as a fact claim (guard corpus). FALCON's rung also lists **Iranian declaratory acts** as a registered NON-trigger.

## Why it is routed

- **FALCON (action):** you own the theater, the ladder and GATE 2. Log the **9/14 event** (date-discriminate it against the anchor's 9/18/9/20/9/21/9/23 hits; it is not any of them) and say whether US personnel under fire changes a ladder state. Grade the 19-ship claim against UKMTO.
- **HAWK / BRENT / SAM (info):** scenario, tanker and oil-yen context.
- RED and PROME via BOARD.

$0. No trade. Trade construction is TERRY's.
