---
signal_id: "SIG-W-20261118-001"
date: "2026-11-18"
timestamp: "2026-11-18T15:19:18Z"
dispatched: "2026-11-18T15:19:18Z"
source: "RTE News (Reuters copy) https://www.rte.ie/news/middle-east/2026/1118/1599631-iran-us/ published 2026-11-18T07:26:51Z, modified 10:46:30Z; TIME https://time.com/article/2026/11/18/qeshm-island-strikes-us-iran-end-forever-war-vance/ published 2026-11-18T10:15:44Z; RESEARCH-INTAKE data/2026-11-18/news.json (gulf-theater titles 121 to 128)"
origin: ["RESEARCH-INTAKE lane, gulf-theater query, collect 2026-11-18T13:11Z (b771325)", "WALTER read of RTE and TIME pages 2026-11-18 15:1xZ"]
action: ["FALCON"]
info: ["HAWK", "BRENT", "SAM", "CARL"]
precedence: "IMMEDIATE"
signal_type: "catalyst"
confidence: 0.75
confidence_language: "two dated pages read (Reuters copy via RTE, TIME); Iran's targeting claim is Iran's word, interceptions are Kuwait's, Bahrain's and CENTCOM's words; ADNOC hull unnamed"
resources: 1
safety_net: "clear"
cluster: "IRAN_HORMUZ"
domain: "GEOPOL_ENERGY"
entities: ["Iran", "Kuwait", "Ali Al Salem", "Bahrain", "CENTCOM", "IRGC", "Qeshm Island", "ADNOC", "UKMTO", "Khasab", "Houthis", "Riyadh", "Oman", "Qatar", "Reuters", "RTE", "TIME"]
word_count: 567
dispatch_note: "War-theater carve-out: Iran/Gulf kinetic -> FALCON action, HAWK info (synthesis), BRENT info (ADNOC hull, oil transmission), SAM info (GEOPOL_ENERGY row). CARL info under the May-6 override: explicit kinetic event with a supply-disruption mechanism (a tanker struck). Iran pre-dispatch guard: anchor stale (full sweep due 11/18), routed first per CLAUDE.md, anchor_unverified_as_of 2026-11-11; guards applied: June/July Kuwait date trap checked, INTERCEPTED not STRUCK, ADD#26 unknown-projectile not merged with a named hull. PROME launched FALCON 10:16 ET with this item as unverified (PROME message). TERRY BOARD-only; CARL INFO by BOARD."
event_window: "open"
anchor_unverified_as_of: "2026-11-11"
---

> ⚠️ **PARTIALLY CORRECTED by SIG-W-20261118-006 (FALCON grade): the Kuwait and Bahrain attacks are CONFIRMED by the states, damage NOT ESTABLISHED; the claimant is NOT settled (Iranian army per IRIB in AP, CBS, Reuters; IRGC per Tasnim in Stars and Stripes), so 'Iran's army says' below is one account; the ADNOC hull is PROBABLY distinct from TARA GAS, not established (Seatrade: NAVIG8 MESSI, unverified).**
# Iran's army says it targeted US drone and missile installations at Kuwait's Ali Al Salem base (Wed Nov 18, early); Kuwait says its air defences countered hostile drones; Bahrain intercepted Iranian aerial attacks for the third time this week; no damage to US sites confirmed; first Iranian attack on Kuwait since September (Reuters via RTE). ADNOC: one of its ships struck in Hormuz Nov 17, 11 crew injured, 1 missing (vessel unnamed in the text read; whether it is a hull already in FALCON's census is NOT established)

# Iran fires at Kuwait and Bahrain after the US Qeshm strike; ADNOC ship hit in Hormuz

**Sources read (pages opened, publication dates checked):** RTE News, 'Iran attacks Kuwait and Bahrain after US strike on Qeshm Island', published 2026-11-18 07:26Z, updated 10:46Z (Reuters copy). TIME, Chad de Guzman, 2026-11-18 10:15Z. Lane titles, not opened (WSJ 11:17Z 'Iran Attacks Kuwait and Bahrain, Further Escalating Fight Over Strait'; AP 12:44Z 'Iran widens Gulf attacks by targeting a US air base in Kuwait and sites in Bahrain'; Reuters 23:15Z Nov 17 'Iran fires at Kuwait after US strike on Iranian island'; SCMP 07:27Z; Bloomberg 07:40Z and 09:20Z). AP, Reuters and WSJ pages are not reachable by this desk's tools. **Date trap checked:** Iranian attacks on Ali Al Salem and Bahrain also ran in June and July 2026 and rank first in searches; both pages read are dated today and tie the attack to the Nov 17 Qeshm strike.

| Item | Words in the source | State |
|---|---|---|
| Kuwait | Kuwait's Armed Forces said early Wednesday its air defences were responding to 'hostile drone' attacks; the Iranian army said it targeted 'US drone and missile installations' at Ali Al Salem base (RTE/Reuters; TIME: 'Iran later took responsibility') | ATTACK CLAIMED by Iran; Kuwait reports interception activity; **no damage reported** |
| First since September | 'It was the first Iranian attack on the oil-rich country since September' (RTE/Reuters) | REPORTED (Reuters' count) |
| Bahrain | Bahrain 'intercepted Iranian aerial attacks for the third time this week'; accused Tehran of a 'systematic hostile approach' (RTE/Reuters). TIME: CENTCOM said the Nov 17 Iranian one-way drones at Bahrain 'were intercepted without any damage to U.S. equipment or injury to American personnel' | INTERCEPTED (not struck) |
| Riyadh | Saudi-led coalition says it destroyed a Houthi cruise missile launched toward Riyadh (RTE/Reuters) | INTERCEPTED |
| ADNOC ship | ADNOC said 11 crew injured and one missing after a ship belonging to the company was struck in the Strait of Hormuz 'yesterday' (Nov 17); UKMTO: tanker struck 'by an unknown projectile' about 13 nm north of Khasab (RTE/Reuters) | STRUCK, casualties per the operator; **vessel not named in the text read**; RTE's wording on the event day is ambiguous ('a day earlier') |
| Qeshm | US fighter jets fired on an IRGC missile launch site on Qeshm Nov 17, per an anonymous US military official (as card 028); Iranian media: no infrastructure damage | CONFIRMED by FALCON 11/17 (card 028) |
| Washington plot | Trump: US takes seriously a possible Iranian plot against Washington (CNN report citing intelligence, 'dirty bomb'); RTE/Reuters | REPORTED words; card 015 carried the plot title |
| Diplomacy | Talks via Oman and Qatar continue (TIME); Vance: Trump 'is not going to let this become a forever war' (Fox, Monday) | mediated, not bilateral |

**For FALCON:** the ADNOC hull needs the five ADD#26 discriminators (event day, vessel name, direction, mechanism, UKMTO position) before any census use; FALCON's 11/17 census holds TARA GAS (abandoned after a second attack), ON PHOENIX (probable) and AL DHANNAH (IMO list). 'Intercepted' is not 'struck' for Kuwait and Bahrain: no source read reports damage. Not an in-port hit (the anchor's Kuwait/Bahrain trigger is an EXECUTED in-port hit).

**Anchor:** WALTER's Iran anchor full sweep is due today (last 2026-11-11 13:55Z); this card is routed before that sweep: anchor_unverified_as_of 2026-11-11.
