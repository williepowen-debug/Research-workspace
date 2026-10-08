# AEOLUS → PROME · 2026-10-08 08:39 ET · Hurricane Isaias: acute-landfall channel read, CORAL/BRENT reconciliation, what it arms, whole-inbox drain

**Wake:** WQ-369 narrow C8 (IMMEDIATE dispatch · dark owner · own theater), brief `PROME/tasks/2026-10-08_wakes/AEOLUS.md` + COMMON.md, spawner `prome-fc`. **$0 · no trade proposal · no threshold moved.** One score moved (C1 1→2) — forced by the dispatch item, named below.

## Boot receipt
Runtime: Claude Code sub-agent (Agent tool) on Anthropic **Opus 5.5 (`claude-opus-5-5`)**; session id **UNKNOWN** (scratchpad path suggests `b525ba3f-…`, INFERRED); repo `/home/willi/Research-workspace`, branch master. Explicitly read: root CLAUDE.md, AGENTS.md, USER.md, `AGENTS/AEOLUS/CLAUDE.md` (boot + closeout), COMPLETION_SPEC, both wake files, BOARD_CONSUMPTION_SPEC §5. Tools used: Bash (curl to primaries, pdfminer, fetch.py), WebSearch (⚠️ its index returned nothing for 2026 events — every figure below is from a direct primary pull, not search), SendMessage. MCP `definite` / `Prisma-Local` failed to connect — not needed. **SKIPPED:** boot step 1 pull (tree carries other desks' uncommitted work — per COMMON, did not pull); step 6 channel liveness for C2/C3/C4 and the 30-day CALENDAR items (bounded session — listed under GAPS); no domain workers spawned. Ran: 6b corrections check (rc 0), 6c dark-window scan, domain_log_check (clean), read_cap_check (rc 0; STATUS 71% of budget), consumer_check (own surfaces fixed; cross-agent hits are DAEDALUS defect records + unrelated "15-30%" strings — no 🔴 owner packet owed beyond DAEDALUS), claim_check (clean), orphan_check (4 packets, all committed).

## 1 · The acute-landfall read (primaries, 10/8 08:22–08:29 ET)
| Item | Figure | Source / basis |
|---|---|---|
| Isaias now | **70 kt (80 mph) / 975 mb, 23.7N 90.6W, ENE 9 mph** | NHC Intermediate Adv 7A, 12Z |
| Forecast | 85 kt 10/8 18Z → **peak 95 kt 10/9 06Z** ("just shy of major") → 90 kt 10/9 18Z at 28.4N 87.6W → **inland 55 kt 10/10 06Z at 31.0N 87.6W** → post-tropical, Tennessee Valley | NHC #7, 09Z |
| Landfall | **late Fri 10/9 – early Sat 10/10**; track points cross the coast along ~87.6W = **near the AL/FL line** (INFERRED from the points; NHC names no landfall point) | NHC 7A / #7 |
| Warnings | Hurricane Warning **Ocean Springs MS – Bay/Gulf County Line FL**; Storm Surge Warning Mississippi mouth – Steinhatchee FL; TS Warnings either side; Surge Watch Steinhatchee – Yankeetown | NHC 7A |
| Surge | **5–7 ft** Ocean Springs – Indian Pass and Mobile Bay; 4–6 ft Indian Pass – Steinhatchee; 3–5 ft Mississippi mouth – Ocean Springs | NHC 7A |
| Wind odds (5-day cum 34/50/64 kt) | Pensacola **69/29/7%** · Mobile 51/18/4 · Destin 49/15/3 · Panama City 38/8/2 · Gulfport 23/7/1 · offshore 29N 87W **91/64/35** · 28N 89W 61/22/14 | NHC PWS #7 |
| Intensity risk | NHC: "somewhat tricky" — RI **+35 kt/24 h** through ~20 kt shear on 30 °C water; shear 40–50 kt in the final 12–24 h, but the wind field broadens | NHC #7 + ATCF b-deck |
| Gulf shut-in | **oil 511,619 b/d = 25.08%; gas 350.25 MMcf/d = 16.37%; 8 of 371 platforms evacuated** — as of **10/7 11:00 CDT**. **No 10/8 release found** (index "Access denied"; guessed slugs 404) — SEARCH-NOT-FOUND, not absence | MMA (BOEM+BSEE reunified 7/10) release 10/7 |
| FL emergency | **EO 26-202 (signed 10/6): 25 north-Florida counties** (list in the CORAL packet) | flgov.com EO PDF |
| Season | ACE **12.6675** = **12.37%** of the Oct-8 to-date normal 102.4190 (HURDAT2 1991-2020, re-validated 14.4 NS / 7.2 HU); AEO-01 (96%) cannot miss on any of 59 years' post-10/8 accrual (max 70.34 vs 97.66 needed) | ATCF b-decks AL01–09 + HURDAT2, computed |
| Insurance price surface | cat-bond spread **4.57% [9/25], −16.6% YoY, lowest since 2020** (pre-storm; NOT rate-on-line) · FL primaries **closed UP 10/7**: UVE $45.25 +4.00%, HRTG +1.08%, HCI +1.25%, AII +2.64%; RNR −0.43%, EG −1.24% | Artemis series; fetch.py (10/7 closes, read 08:24 ET) |
**Touches:** C1 peril leg (live test of the major-landfall trigger); C4's >$10B insured-cat leg (same event — counted ONCE); BRENT's Gulf supply theater; CORAL's Panhandle. **Does NOT touch:** South Florida (not while the track holds); C3 (shut-in is supply, not demand); C5/C6 (Rhine/Colorado unaffected). ⚠️ **Not read by me:** refinery status in the warning zone (Chevron Pascagoula inside the Hurricane Warning) — BRENT's gap; any insured-loss estimate (none exists yet).

## 2 · Reconciliation (one figure per shared metric)
- **FL property-cat reinsurance 6/1 renewal = CORAL's Guy Carpenter −15/−20% risk-adjusted.** My "−15–30%" was a three-publisher envelope (Howden · GC · Citizens), not a Florida number — KB-AEO-005 superseded as a FL figure; KB-AEO-167; THESIS/VX/FLOW/TRADE re-cut. Closes DAEDALUS PR#7 item 1.
- **Citizens policies in force = CORAL's 254,918 (9/25, prelim).** ⚠️ citizensfla.com "Current Policies" still shows the 12/31/2025 vintage (395,337 / $128.5B) — flagged to CORAL so it does not leak in.
- **CORAL packet** (`AGENTS/CORAL/inbox/2026-10-08_from-AEOLUS_isaias-FL-figures-for-friday.md`, `9cec2b2f9`): FL peril figures + five Friday asks (Citizens warning-county exposure; why FL primaries rose 10/7; Panhandle condo/bank exposure; flood vs wind on wet Panhandle soils; Citizens/FLOIR claims post-landfall). **For CORAL's Friday brief:** the hurricane is a Panhandle event; the reinsurance figure is CORAL's own.
- **BRENT packet** (`b154f4231`): theater only — shut-in, track over the producing area, offshore wind odds, coastal warnings/surge incl. Pascagoula and the Mississippi mouth. No grade of BRENT's gates or the USO card.

## 3 · What this arms (own ledger)
- **C1 upgrade trigger — letter: "a peak-season Gulf/FL major landfall" → ARMED, not fired** (forecast peak 95 kt is over water and 1 kt under major; weakening forecast before landfall). **Registered:** `CALENDAR.md` row **2026-10-09 → 10-10** — grade ≥96 kt AT landfall from the NHC landfall statement; then read MMA restart, modeler loss estimates, Citizens/FLOIR (CORAL), cat-bond weekly points, final ACE, outages (WATT).
- **C1 exit rule leg 2** ("no major US landfall by 11/30") resolves on the same read. **C4 >$10B insured-cat leg** armed by the same event.
- **Score:** **C1 1→2 (watch)** — forced by SIG-W-20261008-001 verified at NHC 7A (a "dormant" 1 is false at write time with a US hurricane warning in my theater). Composite 18→19/30. VX-AEO-39. No threshold moved; no prediction re-priced.
- **Boot catch-up (6c):** C5 →5 **still FIRED** — Rhine below its record low every complete day 9/18→10/7 (20 days), no exit in the gap (KB-AEO-172); C6 legs not fired (Mead 1,037.69 [10/7], Powell 3,519.04 [10/6]).

## 4 · Whole-inbox drain — 10 of 10 logged (`AGENTS/AEOLUS/board_log.tsv`, 10/8 08:33ET), all `git mv`'d to processed/
| Item | Disposition | Note |
|---|---|---|
| SIG-W-20261008-001 | acted | Isaias — this memo; KB-164/165/166 |
| SIG-W-20261001-020 (ACTION) | acted | Pacific Cat-5 season = El Niño signature; no new channel (KB-168) |
| SIG-W-20261002-033 (ACTION) | acted | Arctic NSR out of C5 scope (KB-169) |
| SIG-W-20261002-020 / -030 / 20261003-015 | noted | FL rain/water → CORAL's figures; Panhandle antecedent wetness = flood amplifier (KB-171) |
| SIG-W-20261004-008 | noted | Swiss glaciers = Tier-2 Rhine watch-note (KB-170) |
| SIG-W-20261007-005 | info-only | Pink Sheet — FERT's |
| DAEDALUS PR#7 (10/1) | acted | item 1 done · item 2 proposed (AEO-03 instrument, full session) · item 3 partial → packet `b6d4218b3` |
| WALTER R3 watch-for (10/1) | acted | adopt/decline by name → `PROME/inbox/2026-10-08_from-AEOLUS_R3-watch-for-adopt-decline.md` (`e28fa841b`) — **PROME lands the clean set of 12** |

## COMPLETION — AEOLUS — 2026-10-08
STATUS: ⚠️ PARTIAL
CHANGED: AGENTS/AEOLUS/{STATUS,SCRATCH,CALENDAR,THESIS,TRADE,NEXUS_BRIEF}.md, board_log.tsv, workbook/{KB,VX,FLOW}.tsv, hurricane/{DOSSIER,SOURCES}.md + workbook/{STORMS,SERIES,LOG}.tsv, water/workbook/{SERIES,LOG}.tsv, archive/NEXUS_BRIEF_ARCHIVE_2026-09-28_fold.md, 10 inbox→processed moves; packets to CORAL, BRENT, DAEDALUS, PROME (R3); this memo
RESULT: Isaias read at NHC 7A/#7 (70 kt, peak 95 kt fcst, landfall Fri night–Sat near AL/FL line), MMA 10/7 25.08% oil shut-in, EO 26-202 25 counties; C1 1→2 (19/30), major-landfall trigger ARMED with a 10/9–10 CALENDAR row. FL reinsurance reconciled to CORAL's −15/−20% (KB-167); C5 still fired 20 days, no exit (6c). Inbox 10/10 drained and logged; KB-AEO-164…173.
GAPS: Dispatch fully done; PARTIAL = boot catch-up bounded out: 10/01 cluster (NIFC AEO-09, Colorado guidelines, CSU 9/30) OVERDUE, CPC 10/08 ENSO not read (released ~09:00 ET, after my reads), C2/C3/C4 + Contargo/Danube/Panama/Mississippi not refreshed; no 10/8 MMA release found (index Access denied); refinery state and loss estimates unread (BRENT's / not yet published).
WILL_NEEDS: None.
FOLLOW-UP: Re-spawn AEOLUS after the NHC landfall statement (Sat 10/10) to grade the C1 trigger (CALENDAR row); put Isaias in CORAL's Friday brief (packet 9cec2b2f9); PROME lands the R3 clean set (e28fa841b); next weekly session owes the 10/01 cluster + CPC 10/08.
