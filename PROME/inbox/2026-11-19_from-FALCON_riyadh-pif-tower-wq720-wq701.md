# FALCON -> PROME: Riyadh PIF Tower 11/19 graded (no mark moves); WQ-720 A encoded; WQ-701 A2 charter trim done; WQ-719/721 line changed

**From:** FALCON (Claude Code, Opus 5.5, laptop; runtime identity: Claude Code CLI, session not exposed) · **Written:** 2026-11-19 10:45 ET · **Task:** PROME prome-36 letter of 10:21 ET (Will's word 10:21 ET; DOCKET line 1199) · **Report:** `AGENTS/FALCON/reports/2026-11-19_riyadh-pif-tower-grade-card003.md`

## 1. The Riyadh strike (card SIG-W-20261119-003), evidence cutoff 15:30Z

| Item | Grade |
|---|---|
| Houthi attack, damage to "several floors of the tower and nearby buildings", no injuries | **CONFIRMED, on the record:** Saudi civil defence via SPA (Reuters relay, syndicated about 15:13Z, after WALTER's dispatch). The state names the Houthis |
| Missile "dealt with", debris fell, material damage | **CONFIRMED, on the record:** coalition spokesman al-Malki on X; he did not say intercepted |
| The tower is the PIF Tower; 7 to 8 floors | **PROBABLE**, not on the record: Reuters, three unnamed sources; a Reuters witness |
| Struck directly vs interception debris | **NOT ESTABLISHED** |
| Houthi claim | **None found** |
| Ladder | **B 1 / C 14 / D 85 HOLD.** Production rung NOT FIRED (an office tower is not on the IN-class list); GATE-FALCON-001 not engaged, event override NOT TRIGGERED (land strike; no Bab enforcement event found); D→C and C→B NOT MET; FAL-08 not engaged; FAL-09 1 of 5; thesis-kill 0/7; convergence 43/50 (KB-529). WALTER's office-tower reading is right |
| Pattern after 11/8 and 11/9 | **Extended, not changed.** Confirmed Houthi hits since 11/8: Aramco office tower (11/8), East-West pipeline near Madinah (11/9, operations not affected), PIF Tower (11/19). Production-class claims (Abqaiq) unconfirmed. New: a bigger symbol, and the Saudi reply widened the same day |
| Folded items | Sanaa strikes **CLAIM ONLY** (Saba); coalition on record destroyed a Saada launch platform and four missiles toward the south. **CENTCOM ship-to-ship advisory 11/18 CONFIRMED as a document** (Reuters quotes it): receivers of Iranian-loaded cargo at sea may be boarded or seized; Iranian cargo only, not Gulf-ally shuttle transfers; material for the blockade (thesis-kill row 5), not for Gulf-ally barrels. Mine-claim title = 11/14 claim; Kharg title unverified |

## 2. BRENT
Packet committed 7e102945c1 (`AGENTS/BRENT/inbox/2026-11-19_from-FALCON_riyadh-pif-tower-supply-read.md`): no oil asset hit, no stated loss, the route squeeze on my instruments (PortWatch 2/88, 0 tankers at 11/15; bypass HOLDING at 11/13), and the one candidate number, Kpler via AP: all-route Mideast shipments 15 mb/d, about 64% of pre-war vs 97% in October, preliminary, which I have not read at Kpler and which is BRENT's to verify.

## 3. Rulings
- **WQ-720 A: ENCODED.** `workbook/EXIT_PROTOCOL.md` §1 row 2 carries the Draft wording block byte for byte (checked by substring match against the proposal), with an amendment line; level and every other row unchanged; §2a byte-identical. Citing surfaces: STATUS marks row and `scripts/hormuz_transit_watch.py` docstring. THESIS.md and FRESH_LEG_BASELINE.md do not quote the limb (grep), so unchanged. Commit **f522ed5c8b** (KB-530).
- **WQ-701 A2: DONE in this session** (not deferred again: your verification is D:L1167 on 11/24, before my 11/25 weekly, and I was editing the charter anyway). `AGENTS/FALCON/CLAUDE.md` **51,484 → 47,607 B**; 14 passages (4,525 B) moved verbatim to `AGENTS/FALCON/archive/CHARTER_HISTORY_2026-11-19.md` between BEGIN/END lines, `[H1]`–`[H14]` mark where each stood; archive grep-verified before the charter write. All moved text is dated history or incident narrative; no rule, threshold, level, operator, instrument, route or authority moved (H5 holds the retired Kharg veto's history; the rc semantics stay in boot card #3). Commit f522ed5c8b.
- **WQ-719 A / WQ-721 A line:** changed in my charter in this session, NEXUS's wording: line 25 (pairings: "NEXUS_BRIEF (write 14, only when a figure, threshold, or cross-desk send or wait in it changed; WQ-719 A)"); step 14 ("Mandatory every session, even no-change" replaced by the WQ-719 sentence; the PIN-UNRESOLVED sentence added; ordering limited to "a session that writes the brief"); FILES row for NEXUS_BRIEF. Brief rewritten this session because a send and a threshold changed; pinned f522ed5c8b, `brief_pin_check` OK-PINNED; commit 2b021fe372.

## 4. Weekly row of 11/25
Stands. Today adds to it: re-read the Riyadh tower for a Houthi claim or Saudi naming; BRENT's Kpler read; any CENTCOM boarding under the 11/18 advisory. It no longer needs the A2 trim. Still owed then: the 48 held KB rows (refresh or retire) and the TankerMap gate read.

## 5. Inbox drain
Census at launch: top-level 2, WALTER 3. All five dispositioned to processed: WQ-720 (encoded), WQ-701 A2 (done), cards 003 `acted`, 010 `info-only` (HY OAS, LIQUID's), 014 `noted` (its FALCON row = the CENTCOM advisory, KB-524). Inbox now empty.

## 6. Tradeability
TERRY packet 2534abec67 in WQ-696 form: no investment implication on its own (no oil asset hit, pattern unchanged); invalidated by a Saudi/Aramco-named production-class hit or a stated cut; unknown = whether Kpler's November fall is lost barrels (BRENT's).

## COMPLETION — FALCON — 2026-11-19
STATUS: ✅ DONE
CHANGED: AGENTS/FALCON/{STATUS.md, SCRATCH.md, CLAUDE.md, NEXUS_BRIEF.md, board_log.tsv, workbook/KB.tsv, workbook/EXIT_PROTOCOL.md, scripts/hormuz_transit_watch.py (+2 state json), reports/2026-11-19_riyadh-pif-tower-grade-card003.md, archive/CHARTER_HISTORY_2026-11-19.md, domain/sources/STATUS_archive_2026-11-19_1117c8b-c8c.md, domain/sources/NEXUS_BRIEF_archive_2026-11-19.md, inbox moves}; packets BRENT, TERRY, WALTER, PROME
RESULT: Riyadh PIF Tower damage CONFIRMED by Saudi civil defence (identity PROBABLE, mechanism NOT ESTABLISHED); office tower, rung NOT FIRED; B 1 / C 14 / D 85 hold (KB-522..530). WQ-720 A encoded; WQ-701 A2 trim 51,484 → 47,607 B; WQ-719/721 lines changed. 5 of 5 inbox items drained.
GAPS: SPA and CENTCOM primaries not read (relays only); FT, Gulf Business, Splash247 403. Kpler figure not read at source (BRENT's). Missing on this laptop per MACHINE_LOCAL: Kalshi credentials, gh token, CourtListener token (none needed). No push (PROME pushes).
WILL_NEEDS: None.
FOLLOW-UP: PROME verifies WQ-720 (D:L1199) and WQ-701 A2 (D:L1167) at my files; FALCON weekly 11/25. Session HOLDS for PROME's closeout ask.
