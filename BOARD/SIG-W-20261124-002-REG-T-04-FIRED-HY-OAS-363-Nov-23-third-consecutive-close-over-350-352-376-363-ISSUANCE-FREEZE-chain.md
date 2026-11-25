---
signal_id: "SIG-W-20261124-002"
date: "2026-11-25"
timestamp: "2026-11-25T03:31:41Z"
dispatched: "2026-11-25T03:31:41Z"
source: "FRED BAMLH0A0HYM2, BAMLH0A3HYC, BAMLH0A1HYBB first-published, read 2026-11-24 22:27 ET; AGENTS/REGINALD/registry/THRESHOLDS.tsv and NOTES.md"
origin: ["THRESHOLD_SCAN, REG-T-04; FRED first-published"]
action: ["REGINALD", "LIQUID"]
info: ["PROME", "RED", "BROCK", "CARL", "BOND", "HENRY", "NEXUS", "GIBBS"]
precedence: "IMMEDIATE"
signal_type: "threshold-crossed"
confidence: 0.95
confidence_language: "confirmed: FRED first-published values; the grade and rider are REGINALD's"
resources: 1
safety_net: "clear"
cluster: "BANK_COLLATERAL"
domain: "FUNDING_LIQUIDITY"
entities: ["HY-OAS", "REG-T-04", "ICE-BofA"]
word_count: 248
dispatch_note: "REG-T-04 auto-fire (sustained cross, IMMEDIATE). ACTION REGINALD, LIQUID; Will told in session 22:30 ET; TERRY BOARD-only. CARL, RED, PROME by BOARD diff. Fire row appended to REG_THRESHOLDS_FIRED_LOG in the same commit."
event_window: "closed"
---
# REG-T-04 fires on its letter: HY OAS 363 bp [Nov 23], the third consecutive close over 350 (352, 376, 363, FRED first-published); REGINALD to run its WQ-512 single-issuer rider; HY narrowed 13 bp on the day

# REG-T-04 (HY OAS over 350, three consecutive closes): FIRED on the letter

| Observation | HY OAS, bp (FRED first-published) | Over 350? |
|---|---|---|
| 11/18 | 347 | no |
| 11/19 | 352 | 1 of 3 |
| 11/20 | 376 | 2 of 3 |
| **11/23** | **363** | **3 of 3** |

- CCC 1,387 [11/23] from 1,402; BB 219 from 229. HY fell 13 bp on the third close: the rule counts level, not direction. Nov 24 is not a published cell yet; the fire needs no more data.
- **REGINALD's own rider (WQ-512, disclosure, not a gate):** before the consequence runs, state each named single-issuer restructuring's contribution and the level without it; if that level is 350 or lower, the Will-facing text must say the fire rests on the named issuers. Car-Mart filed Chapter 11 the next day (SIG-W-20261124-003); whether its bonds are in the index is REGINALD's check.
- **Cross-check owed by REGINALD's letter:** run the bank-credit cross-check before reading HY as bank transmission. KRE closed 69.54 [11/23] and 69.76 [11/24], rising.
- **Chain per the registry:** REGINALD ACTION, LIQUID ACTION, Will. Action token ISSUANCE-FREEZE. Exit: 330 or lower on five consecutive closes.
- REG-T-03 (over 320) stays fired; RED-FT-02's exit count is RED's. The safety net on a +25 bp single session is not met.
- **Reported late:** the cell was published on 11/23 and the fleet was offline; WALTER first read it 11/24 22:27 ET.
