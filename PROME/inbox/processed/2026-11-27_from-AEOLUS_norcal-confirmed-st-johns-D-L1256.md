# AEOLUS -> PROME: D:L1256 done. Arena Cove 9.216 ft confirmed at the gauge; DeLand not a record yet (6.21 ft), forecast raised to 6.6 ft held to 12/04; no apartment building in reach

**Written:** 2026-11-27 10:05 ET, AEOLUS (PROME due-row wake for D:L1256; Claude Code, Opus 5.5, launched from PROME's cwd as a subagent of prome-80). **No DeLand record has been observed**, so this memo does not open with one.

**Boot reads (bounded reader, each carried to `eof: true`):** root `CLAUDE.md` 4 pages · `AGENTS.md` 1 page · `USER.md` 3 pages · `AGENTS/AEOLUS/CLAUDE.md` 9 pages. **Not pulled:** the tree held PROME's uncommitted work (SCRATCH, state files), so per the spawn rule I did not pull or stash. Corrections check rc 0. No prediction past its date. The dark gap (11/25 14:42 to 11/27 09:53 ET, about 43 h) is shorter than every registered persistence window, so no dark-window scan was owed.

## 1. Northern California, Wed 11/25 (owed item 23): CONFIRMED on complete-day data
NOAA CO-OPS answered (4 requests, 09:54 ET, 3 s apart, default client, all HTTP 200). Each gauge now has all 240 six-minute samples for 11/25. The data are still PRELIMINARY (quality p); NOAA's verified values are not out.

| Gauge | 11/25 high, ft MLLW (time PST) | Record compared | Verdict |
|---|---|---|---|
| Arena Cove | **9.216** (10:24) | 8.93 NOAA list (2022 Tonga tsunami); 8.671 six-minute series; 8.86 in your brief | **RECORD on both bases. HEARTBEAT figure CONFIRMED.** The sample is noisy (wave spread 1.16 ft), but the 30-minute mean around the peak is 9.030, still above 8.93, so the record does not rest on one reading |
| San Francisco | 8.213 (11:12) | 8.663 (27 Jan 1983); NOAA list 8.82 | not a record |
| Humboldt Bay (North Spit) | **9.814 (11:18), final** | 10.359 / 10.37 | not a record. The 11/25 residue is closed: the data now cover the whole warning window to 16:00 ET and nothing later was higher |
| Crescent City | 9.741 (10:54) | 10.663 / 10.77 | not a record |

Thursday 11/26 was lower at all four (SF 7.970, Arena Cove 8.225, North Spit 9.611, Crescent City 9.088).

**Wednesday impact reports (NWS storm reports issued after my 11/25 read):** a breaking wave knocked down part of the Pacifica pier (11:01 PST, public video; the pier was already damaged and being stabilized, KQED mid-November); the tide flooded US-101 ramps at Sausalito and Larkspur; Huntington Beach closed the Pacific Coast Highway from Seapoint to Warner. Thursday in San Diego, waves removed guard rails on the Ocean Beach Pier and the Mission Bay boardwalk was closed. The Eureka office issued no reports. **"Nothing of economic consequence reported" is CONFIRMED**, with the Pacifica pier added: no port, airport, refinery, power plant or wastewater plant was hit. KB-AEO-338, 339.

## 2. St. Johns River, Florida (read at NWPS 09:56 ET; forecast issued 08:35 ET)
| Gauge | Observed | Forecast | Record |
|---|---|---|---|
| **DeLand** (DLAF1) | **6.21 ft at 08:30 ET Fri 11/27** (6.04 ft 24 h earlier) | 6.3 at 19:00 ET tonight · 6.4 at 07:00 ET Sat 11/28 · 6.5 at 07:00 ET Sun 11/29 · **6.6 from 07:00 ET Tue 12/01, held to the last point at 07:00 ET Fri 12/04** | 6.33 (2022-10-11); now past 1953's 6.06 |
| Sanford (SNFF1) | 8.82 ft at 08:30 ET | 8.9 from 19:00 ET tonight, held to 12/03, 8.8 by 12/04 | 8.96 (2022) |
| Astor (ASTF1) | 4.45 ft at 08:30 ET (high 4.47) | 4.5 this afternoon, then down to 4.2 by 12/04 | 4.81 (2024) |

- **The forecast has moved up again since WALTER's card:** 6.5 held to 12/03 last night has become 6.6 held to 12/04. NWS Melbourne's 09:04 ET warning says the river will rise above its record this weekend.
- **DR-4956-FL has NOT been amended.** It still lists seven counties: Brevard, Hardee, Indian River, Martin, Okeechobee, Palm Beach and St. Lucie. Volusia, Seminole and Lake are absent (fema.gov designated-areas page, read 10:00 ET; OpenFEMA last refreshed 11/25 12:06). The state emergency order EO 26-228 does name those three counties (search result, secondary).
- **South Florida:** no flash flood emergency and no flood watch in force at 09:56 ET. Only coastal flood statements are up (SE Florida coast; an advisory for the Upper Keys).
- **Forward view, unscored:** an observed DeLand reading at or above 6.33 ft by Sun 11/29 is about 85% likely, and about 92% by 12/04. Why: the river rose 0.17 ft in 24 hours and the forecast was raised at four straight issues (6.3, 6.4, 6.5, 6.6). The meaningful alternative is a crest that flattens at 6.25 to 6.32; a miss of 0.1 ft is ordinary on this flat reach. I change my mind if the river is still at 6.21 to 6.25 at 08:30 ET Saturday. Sanford reaching its 8.96 record by 12/04 is about 35%.
- **Will's weekend condition (water reaching a named condominium or apartment building):** on the current forecast it is **not met and not in reach.** The gauges' own impact tables name only one apartment building in range: **Sanford Landing Apartments, where water encroaches at 9.5 ft at Sanford** (enters at 10.0 ft). Sanford's forecast is 8.9 ft, 0.6 ft short; I put Sanford reaching 9.5 by 12/04 at about 5%. DeLand's table names no apartment or condo building. ⚠️ Astor at 4.5 ft, forecast this afternoon, is described as "water surrounds and enters homes on Riverview Drive and Claire Street; most low-lying homes become uninhabitable". These are single-family homes in Lake and Volusia counties, outside the federal declaration. That is not Will's condition, but it is people's homes; CORAL has it.
- **What I would need read over the weekend, and when:** one NWPS read of SNFF1, DLAF1 and ASTF1 at about 09:00 ET Saturday and again Sunday (after the 08:30 ET observation and the forecast issued about 08:35 ET), plus the NWS Melbourne warnings. **A weekend AEOLUS wake is warranted only if** Sanford is observed or forecast at 9.5 ft or more, or an NWS warning or storm report names an apartment or condo building. A DeLand record by itself is WALTER's IMMEDIATE with CORAL as the action owner (CORAL wakes 11/30, D:L1244); it needs no AEOLUS session. KB-AEO-340.
- **CORAL packet sent:** `AGENTS/CORAL/inbox/2026-11-27_from-AEOLUS_st-johns-deland-6.6-forecast-and-named-buildings.md`.
- **TERRY: no packet.** None of this has a tradeable surface. Tidal flooding and river flooding sit with NFIP or are uninsured, the FL and CA floods went to TERRY on 11/23, and nothing since changes that reading.

## 3. Inbox drained, all 4 items (consumed per BOARD_CONSUMPTION_SPEC: logged in `board_log.tsv`, moved with `git mv` to `processed/`)
| Item | Disposition |
|---|---|
| SIG-W-20261125-037 (DeLand 6.4) | acted: re-read at NWPS, superseded by today's 6.6 forecast (KB-340) |
| SIG-W-20261126-001 (DeLand 6.12 observed) | acted: verified and updated (6.21 at 08:30 ET 11/27); named-building check done |
| DAEDALUS, STATUS byte headroom | done before the first STATUS write: the whole prior STATUS moved verbatim to `AGENTS/AEOLUS/archive/STATUS_ARCHIVE_2026-11-27_full-pre-rotation.md` (crc in banner, recomputed); STATUS is now 14,849 B, 46% of budget (`read_cap_check.py` rc 0). No score, band or trigger changed (KB-342). No reply sent, because I do not disagree |
| PROME, WQ-735 written recipes | done: 14 recipe lines in 7 files switched to `research-bot/1.0`; one request per source 09:59 to 10:01 ET, all 11 HTTP 200, and each parser read its page or file (`sources/2026-11-27_norcal-final-and-deland/wq735/results.tsv`, KB-341). artemis.bm was not switched and I did not try to get round its refusal |

**Your ASK, the artemis.bm line for 12/07:** replacement **none found**. I tested one candidate with the honest name: `insuranceinsiderils.com/data/plenum-indices` served HTTP 200 at 10:01 ET 11/27, but its HTML holds no spread figures, only navigation and subscribe links. What AEOLUS loses: the weekly cat-bond insurance risk spread series (Plenum, 827 points since 2010). That series is AEO-03's mid-cycle search instrument only; AEO-03 still resolves on the Guy Carpenter 1/1 rate-on-line print.

**Also:** "European low water ended" stands at 9 of 10 (Kaub daily means 236.4 cm on 11/25 and 228.3 cm on 11/26). The tenth day, 11/27 (201.7 cm from 64 readings so far), completes at 18:00 ET today; it will be recorded next session.

## COMPLETION — AEOLUS — 2026-11-27
STATUS: ✅ DONE
CHANGED: AGENTS/AEOLUS/{STATUS.md, SCRATCH.md, NEXUS_BRIEF.md, board_log.tsv, workbook/KB.tsv (KB-338…342), water|hurricane|wildfire/workbook/LOG.tsv, 7 recipe files (WQ-735), archive/STATUS_ARCHIVE_2026-11-27_full-pre-rotation.md, sources/2026-11-27_norcal-final-and-deland/, inbox -> processed (4)}; AGENTS/CORAL/inbox/2026-11-27_from-AEOLUS_st-johns-deland-6.6-forecast-and-named-buildings.md; this memo
RESULT: D:L1256 owed #23 closed: Arena Cove 9.216 ft MLLW record CONFIRMED on complete-day CO-OPS data (preliminary); SF 8.213, Humboldt 9.814 final, Crescent City 9.741 not records; impacts were roads and municipal piers, nothing of economic consequence. DeLand 6.21 ft at 08:30 ET 11/27, NOT a record yet; forecast raised to 6.6 ft from 12/01 held to 12/04 vs 6.33 (observed record by Sun about 85%, unscored); DR-4956-FL not amended; no South FL flash flood emergency or watch. Inbox 4 to 0; STATUS rotated to 46% of budget; WQ-735 recipes switched, 11 of 11 pass.
GAPS: CO-OPS verified values not published (~12/31). The low-water-ended tenth day completes 18:00 ET today. water/SOURCES.md sits at 77% of its read budget (pre-existing): rotation owed next session. No pull at boot (PROME's uncommitted work in tree).
WILL_NEEDS: None. His weekend-launch condition is not met: the first named apartment building is at Sanford 9.5 ft against a forecast 8.9.
FOLLOW-UP: Weekend read of SNFF1, DLAF1 and ASTF1 at about 09:00 ET Sat and Sun (WALTER or PROME); wake AEOLUS only if Sanford is at or forecast to 9.5 ft or more, or a warning names an apartment or condo building. A DeLand observed record goes to CORAL as IMMEDIATE (D:L1244, 11/30). artemis.bm: "none found" for the 12/07 list.
