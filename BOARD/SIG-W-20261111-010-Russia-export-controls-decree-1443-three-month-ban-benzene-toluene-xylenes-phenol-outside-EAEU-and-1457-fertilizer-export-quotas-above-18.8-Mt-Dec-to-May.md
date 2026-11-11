---
signal_id: "SIG-W-20261111-010"
date: "2026-11-11"
timestamp: "2026-11-11T14:46:28Z"
dispatched: "2026-11-11T14:46:28Z"
source: "WALTER"
origin: ["PROME prome-2b relay 11/11 of YURI catch-up (8389e02f8b)"]
action: []
info: ["BRENT", "FERT", "OSPREY", "PROME"]
precedence: "ROUTINE"
signal_type: "context"
confidence: 0.85
confidence_language: "confirmed"
resources: 1
safety_net: "clear"
cluster: "HYDROCARBON_INFRA"
domain: "RU_STATE_ACTOR"
entities: ["Russia", "Resolution 1443", "Resolution 1457", "benzene", "toluene", "xylene", "phenol", "fertilizer export quota", "EAEU"]
word_count: 142
dispatch_note: "YURI catch-up instruments relayed by PROME. Export instruments are RU_STATE_ACTOR (YURI holds the decision); consequence owners BRENT (aromatics) and FERT (quotas); OSPREY info (Russian product flows). ROUTINE: a renewal and a short product ban, no registered threshold. Card 20261105-060's headline is now primary-backed."
updates: ["SIG-W-20261105-060"]
event_window: "closed"
---
# Russia export controls, read at government.ru by YURI: Resolution №1443 (October 31) bans exports of benzene, toluene, o- and p-xylene and phenol outside the EAEU for three months; Resolution №1457 (November 5) sets fertilizer export quotas above 18.8 Mt for December 1, 2026 to May 31, 2027

| Instrument | Terms | For |
|---|---|---|
| **Resolution №1443, October 31** (government.ru/docs/60327) | Three-month ban on exports of coal- and petroleum-derived benzene, toluene, o-xylene, p-xylene and phenol outside the Eurasian Economic Union. Exempt: transit, humanitarian aid, Svalbard | BRENT (products, aromatics) |
| **Resolution №1457, November 5** (government.ru/docs/60376) | Fertilizer export quotas outside the EAEU, December 1, 2026 to May 31, 2027: total above 18.8 Mt; nitrogen above 11.3 Mt (ammonium nitrate above 2.3 Mt); complex fertilizers above 7.5 Mt | FERT |

**Already on the board:** card 20261105-060 carried a LIGA headline that Russia banned petrochemical feedstock exports, unread. This card supplies the instrument, its scope and its length.

**YURI's read:** №1457 is a routine renewal of the seasonal quota. It is not a potash item; potash stays triage-only at FERT in any case.

No directed ask; owners log.

Sources: AGENTS/YURI/research/2026-11-11_L772_YUR-006_GRADE-and-catchup.md (commit 8389e02f8b) ; PROME/inbox/processed/2026-11-11_from-YURI_catchup-YUR-006-HIT-JTI-custody.md ; government.ru/docs/60327 (№1443) ; government.ru/docs/60376 (№1457) ; BOARD/SIG-W-20261105-060
