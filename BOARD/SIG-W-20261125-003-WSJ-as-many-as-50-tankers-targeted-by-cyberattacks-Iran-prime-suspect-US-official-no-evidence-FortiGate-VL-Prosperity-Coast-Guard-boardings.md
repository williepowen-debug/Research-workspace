---
signal_id: "SIG-W-20261125-003"
date: "2026-11-25"
timestamp: "2026-11-25T05:01:38Z"
dispatched: "2026-11-25T05:01:38Z"
source: "Maritime Executive 2026-11-24 13:38; ABC News live 2026-11-24; CNBC 2026-11-24 (pages read); WSJ, FT, Coast Guard advisory not read"
origin: ["Maritime Executive 2026-11-24", "ABC News 2026-11-24 11:49 ET", "CNBC 2026-11-24"]
action: ["CYPHER", "FALCON"]
info: ["HAWK", "BRENT", "YURI", "SHADE", "REGINALD", "VULCAN", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "development"
confidence: 0.75
confidence_language: "several outlets on one WSJ report plus ABC's own officials"
resources: 1
safety_net: "clear"
cluster: "CYBER"
domain: "CYBER"
entities: ["VL-Prosperity", "Vivit-Africa", "FortiGate", "USCG", "WSJ"]
word_count: 261
dispatch_note: "PRIORITY. ACTION CYPHER (event), FALCON (theater actor). Channel info SHADE (marine cover). RED, PROME by BOARD diff."
event_window: "open"
---
# WSJ (Nov 23, read through Maritime Executive, ABC and CNBC, not at WSJ): as many as 50 oil, LPG and chemical tankers believed targeted by cyberattacks, Iran the prime suspect and Russia examined; an administration official says no evidence shows Iran and calls it 'little more than a minor nuisance'

# Tanker cyberattacks

| Object | Read | Basis |
|---|---|---|
| Count | 'as many as 50' ships believed targeted in recent months; ABC: 'at least 50 ... believed' citing multiple officials | **outlets differ on 'up to' and 'at least'; not a confirmed count** |
| Suspect | Iran prime, Russia also examined; some messages in Farsi, not confirmed Iranian | ABC, CNBC, Maritime Executive |
| Against | administration official: no evidence of Iranian involvement, 'little more than a minor nuisance'; Coast Guard 'helped thwart all' (officials, ABC) | Maritime Executive, ABC |
| Entry point | Fortinet FortiGate devices, Coast Guard Cyber Command and FBI warning | Maritime Executive relaying WSJ; advisory not read |
| Ships named | VL Prosperity (August, boarded; ransom note on Russian-language Telegram, bomb threat). Vivit Africa LNG bomb threat: search summary only | the August event is SIG-W-20261002-026, **not new** |
| Boardings | at least four more ships boarded in recent weeks near the US | WSJ through Maritime Executive |
| Ports | FT: hundreds of attempts at Corpus Christi and Los Angeles; a gate outage at Wilmington NC blamed on a cyberattack | through Maritime Executive; FT not read |

- **CYPHER:** new here are the fleet-wide scale, the FortiGate vector and the four boardings. Not established: any ship disabled, any spill or collision.
- **FALCON, HAWK:** attribution is investigators' suspicion; carry the official's denial with it.
- **So what:** the money channel is war-risk and cyber exclusions in hull cover and port delay; no insurer action found.
