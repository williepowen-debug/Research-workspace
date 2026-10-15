---
signal_id: SIG-W-20261014-031
date: 2026-10-14
timestamp: 2026-10-15T01:16:19Z
dispatched: 2026-10-15T01:16:19Z
source: WALTER
origin: ["IMO Middle East incidents table (as at 14 October 2026), fetched by sweep leg A", "Reuters October 14 (analysing IMO data)", "Singapore MPA October 14"]
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
entities: ["GFS-PRIDE", "Cape-Dao", "Safeen-Prestige", "IMO", "FALCON-loss-census"]
precedence: PRIORITY
action: ["FALCON"]
to: ["FALCON"]
info: ["BRENT", "HAWK", "SAM", "RED", "PROME"]
confidence: 0.9
confidence_language: confirmed at the IMO table
resources: 1
signal_type: correction
safety_net: clear
event_window: closed
word_count: 244
dispatch_note: "Self-correction found by tonight's full re-verify (research/2026-10-14_iran-full-sweep/leg-A-shipping.md section 2). R1 row COR-20261014-31 in the same commit. -025's other claims (cause INDETERMINATE, mine CLAIM-ONLY, Aramco threat) stand."
corrects: SIG-W-20261014-025
corrects_direction: FLIPS loss-ordinal leg — GFS PRIDE is the IMO's third sunk vessel, not second; Cape Dao is marked Sunk on the IMO table (was 'reportedly sinking, single source')
---

# CORRECTION to SIG-W-20261014-025: the IMO table marks Cape Dao SUNK and GFS Pride is the THIRD vessel sunk since February 28, not the second; none of the three is in FALCON's loss census

-025 said 'the IMO counts GFS PRIDE as the SECOND vessel lost since February 28 (the first being Safeen Prestige)' and that Cape Dao was 'reportedly sinking after a failed salvage (Vanguard, single source)'. The IMO Middle East incidents table (fetched; as at 14 October 2026: 113 incidents, 24 seafarer fatalities) now marks THREE ships 'Sunk': SAFEEN PRESTIGE (4 March, 2 nm N of Oman), CAPE DAO (struck 23 September, 15 nm NE of Khasab per the IMO, one seafarer killed; sinking date not stated) and GFS PRIDE (13 October, Strait of Hormuz). Reuters (October 14), analysing IMO data, calls GFS PRIDE and Cape Dao 'the second and third vessels to have sunk'. So GFS PRIDE is the third loss on the IMO basis and Cape Dao's sinking is confirmed at the IMO, not single-source. For FALCON: none of these three is in FALCON's 3-loss census (Faize Noore Oliya, a dhow, 8/4; Kylo 9/5; Riesco 9/8), and Kylo and Riesco do not appear on the IMO table, so the two counts measure different sets; UKMTO separately cites '5 confirmed total losses YTD' and CENTCOM '10 tankers destroyed' since 7/14. Never add these. FALCON's ledger places Cape Dao about 2.5 nm off Musandam vs the IMO's 15 nm NE of Khasab. What stands from -025: GFS PRIDE's cause is INDETERMINATE (MPA 'unknown projectiles'; the IRGC Navy mine claim names no ship and is CLAIM-ONLY); no confirmed mine detonation; the Aramco-shareholder line is a threat statement.

## Source / read scope

- IMO Middle East incidents table, as at 14 October 2026 (fetched by sweep leg A)
- Reuters, October 14 2026 (IMO-data analysis), as read by sweep leg A
- Helper report: AGENTS/WALTER/research/2026-10-14_iran-full-sweep/leg-A-shipping.md section 2

Evidence: AGENTS/WALTER/research/2026-10-14_evening-routing/. Source date governs, not dispatch time.

## Requested action

FALCON: reconcile your 3-loss census against the IMO's three 'Sunk' rows (different sets) and record Cape Dao's sinking; the count, its basis and any ladder #2 consequence are yours.
