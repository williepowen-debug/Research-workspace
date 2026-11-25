# CORAL -> PROME: Florida declaration confirmed, the southeast watch, Flagstar, the client-string answer, MSI #16 (2026-11-25)

**Session:** coral-1125, Opus 5.5 (claude-opus-5-5) in Claude Code, in-process desk spawn from PROME prome-77 on Will's word (PROME's chat 11:36 ET). Started 11:37 ET (`date`); this packet begun 11:49 ET (`date`). **Boot reads (bounded reader `PROME/tools/boot_read.py`, each to `eof: true`):** root `CLAUDE.md` 4 pages · `AGENTS.md` 1 · `USER.md` 3 · `AGENTS/CORAL/CLAUDE.md` 6 · `AGENTS/CORAL/STATUS.md` 6. Also read: `SCRATCH.md`, `STATUS_DETAIL.md` § AM and § AL3/AL7, `PREDICTIONS.tsv`, D:L1244, the 11/23 `SYNTHESIS.md` § Corrections, § Open and § Follow-up (before writing anything), the WQ-735 ruling. Not read this session: THESIS, LESSONS, CALENDAR whole, MEMORY whole, COMPLETION_SPEC (read 11/24, not re-read). `boot.py` not run. Pull not run (the tree carries HOMER's uncommitted work). Not pushed (PROME pushes). Every fetch sent `research-bot/1.0`.

## The answer in five lines

1. **DR-4956-FL is the state's FIRST request (dated 11/09), granted narrower than asked:** household aid in six counties; county reimbursement only for debris and emergency work (Public Assistance A and B), not permanent repairs; no Hazard Mitigation; DeSoto and Highlands requested and not designated. The **second request** (filed 11/24: Seminole, Volusia, Broward, Orange, Flagler, Putnam) is **not on the record: pending, not denied** (nothing found either way).
2. **It is a permission, not money:** 0 household registrations and 0 funded county projects in FEMA's data. NFIP claims **have not reloaded** (asOfDate still 11/16: **1,157**, same as carried). New cuts of that same data: **623 of 1,157 (54%) are on insured homes rated outside the mapped flood zone**, and **14 are condominium-association master policies (11 in Brevard), $0 paid**.
3. **The southeast watch is not yet the event that turns a contained river flood into a large one.** AEOLUS's hazard read (11:47 ET): the heaviest rain falls on **Broward and Miami-Dade, which are not declared**; declared counties had 0.3 to 2.5 in; WPC Day 1 is SLIGHT (2 of 4) and the rain ends tonight; tide stages are below the late-October peaks. No Flash Flood Warning at 16:45Z. It bears on **none** of CORAL-01 to -04 or GATE-CORAL-MSI-01.
4. **Flagstar (order read):** 82 violations of the notice-and-force-place rule, Sept 2022 to June 2024, no state named. It shows a mechanism (required cover lapsing at a servicer), not Florida evidence; it does not move the "mostly uninsured" HYPOTHESIS.
5. **Client strings:** the 11/24 fema.gov refusals were to **curl's default string `curl/8.5.0`**, no switch involved (CORAL had nothing to switch under WQ-735). Today **`research-bot/1.0` is refused the same way**. Two plain, honest strings refused, so the WQ-735 switch is not shown to be the cause; the cause is not isolated.

**MSI reading #16 (PROME's add-on):** taken, re-fire fails; GATES wording below. **No colour, gate, grade, level, operator, instrument or consequence moved.**

## Item 1. What the confirmed declaration changes (primary: OpenFEMA, 16:39Z 11/25, lastRefresh 12:06Z)

| Field | Record | Token |
|---|---|---|
| Number, type, title | DR-4956-FL, Major Disaster, "Severe Storms and Flooding"; incident type Flood | VERIFIED |
| Dates | declared 2026-11-24; incident from 2026-10-31, **no end date** | VERIFIED |
| Which request | **declarationRequestDate 2026-11-09 = the first request** | VERIFIED |
| Household aid (IH, with housing assistance, disaster unemployment, crisis counseling) | Brevard, Indian River, Martin, Okeechobee, Palm Beach, St. Lucie | VERIFIED |
| Public Assistance | **Categories A (debris) and B (protective measures) only**: Brevard, Hardee, Indian River, Martin, Okeechobee, Palm Beach. St. Lucie none. No category C to G (roads, bridges, buildings, utilities, parks) anywhere | VERIFIED |
| Hazard Mitigation | not declared | VERIFIED |
| First request, not designated | DeSoto, Highlands (request list from Wisevoter, 11/24 session; the denial or deferral itself is not on any record I can read) | INFERRED |
| Second request (11/24) | none of Seminole, Volusia, Broward, Orange, Flagler, Putnam on the record; FDEM's fall-flooding page posts no status; two press searches found no amendment or denial. OpenFEMA is current (4956 is the newest row nationally), so this absence is not lag. **Pending, not denied** | SEARCH-NOT-FOUND |
| Money | IHP valid registrations for 4956: 0 rows; PA funded projects: 0 rows | VERIFIED (a data lag of weeks is normal) |
| Cost share | not in OpenFEMA; no FEMA Federal Register notice (FR API, published since 11/20: none); fema.gov refused (item 4) | UNKNOWN |

**What it changes on CORAL's side.** (a) The six-county household-aid clock is real; HOMER's derived FHA 90-day foreclosure pause to about 2/22/2027 now has a confirmed declaration under it (HOMER's figure, DERIVED, no HUD notice read). (b) The counties' own bill is wider than the 11/24 read implied: with A and B only, permanent repair of roads, drainage and buildings is not federally reimbursable unless an amendment adds C to G. That is where the Amendment 3 squeeze and local borrowing would show, and it is the county-spending check D:L1244 already holds. (c) The St. Johns record-flood counties (Seminole, Volusia) and Broward get nothing until the second request is acted on. (d) Nothing moves CORAL's colour: the bank rail is untouched, and the Seacoast trigger (a federal declaration with damage in Martin, Palm Beach, St. Lucie) is REGINALD's to grade; HOMER already sent REGINALD the confirmation.

**NFIP against the 1,157 carried.** Unchanged: the load still stops at asOfDate 11/16 (1,157 for loss on or after 11/01; 1,165 counting 10/31; last loss 11/12; Brevard 745, St. Lucie 191, Palm Beach 89, Broward 35, Indian River 32, Martin 21; building paid $4,844,412 on 213 claims; contents $661,679). Two new cuts of the same rows:
- **Rated zone:** X 623, A 523, V 10. In Brevard 442 of 745 are zone X. ⚠️ These are insured homes only. A high zone-X share of claims does NOT measure the uninsured share: the rival reading (zone-X policies are simply numerous in Brevard) moves the same statistic the same way. The discriminator is claims per policy in force by zone (`FimaNfipPolicies`), not pulled.
- **Condominium associations:** 14 claims under association master policies (RCBAP, code A), 11 in Brevard all dated 11/02, 2 Broward, 1 Martin; 8 in coastal zone VE; 1 to 28 units per policy; $0 paid at 11/16. This is the **first observation of flood claims by condominium associations in this event**: anonymous (no name, no city in the data), and **all insured**. It does not supply the missing case (an uninsured, flood-hit association paying from reserves or assessments), and a filed claim is not confirmed damage.

**Notices since 11/24.** Citizens: newest item 11/20 (CEO to step down); policies in force 196,511 at 11/20, no flood notice. OIR: the orders page lists an order on **Citizens dated 11/20/2026 (OIR 2026-109, case 403670-26-CO)**; it is a scanned image and this machine has no OCR, so **its content is UNREAD**; no 2026 flood emergency order appears on that page. FEMA: no Federal Register notice; fema.gov refused.

**Today versus 11/30 (D:L1244).** Done today: the primary record, its programs and which request. **Still waits for 11/30:** the second request or an amendment; the FR notice (cost share); the first IHP and PA dollars; the NFIP load after 11/16; county and city spending (a press search today found none; agendas unread); Citizens' December board and 2027 rate; HOMER's flooded-home counts; reading OIR 2026-109 (needs a person or an OCR tool; the PDF is at floir.gov, orders/property-and-casualty/2026).

## Item 2. The southeast watch, on CORAL's own rows (hazard side: AEOLUS's packet of 11:47 ET, used as given)

| Row | Does the watch bear on it? | Grade by its written rule |
|---|---|---|
| CORAL-01 (Cape Coral MSI > 6.00 by the 12/15 data date) | No (Gulf coast supply index) | OPEN; first print for 11/24 is 5.78 |
| CORAL-02 | — | RESOLVED FALSE 11/17 |
| CORAL-03 (OIR Isaias insured loss ≥ $800M by 12/31) | No: a different storm (Panhandle) | OPEN; OIR still $735,515,012 at 11/06 |
| CORAL-04 (FEMA FR notice for DR-4955, 75% share) | No: the letter names FEMA-4955-DR only; a DR-4956 notice does not count | OPEN; no DR-4955 FEMA notice found |
| GATE-CORAL-MSI-01 | No | reading #16 below |
| Six falsify criteria (THESIS) | No; next grade 2027-02-16 | not graded today (their rule forbids it) |
| STATUS "what would change the read" | Yes, as a watch: the declaration half has now happened; household aid added for Seminole, Volusia or Broward (or a denial), first dollars and county borrowing remain | a read-changer list, not a rule; no colour moves |
| Owed row AC / D:L1244 | Yes: "what the 11/24 to 11/26 watches did on the southeast coast" | answered below, partially; final outcome after 01:00 ET 11/26 |

**Is the southeast coast now the "event that could turn a contained river flood into a large one" (11/23 synthesis)?** **Not yet, on today's evidence.** For: soils at 200 to 600% of normal 30-day rain; up to 10 in possible in spots; road flooding in Miami-Dade and standing water in Pembroke Pines (NWS reports via AEOLUS). Against: the declared counties are getting 0.3 to 2.5 in; WPC Day 1 is SLIGHT, Day 2 has no Florida risk; no Flash Flood Warning at 16:45Z; tide stages are below the 10/27–28 peaks; on the St. Johns this is the tail (0.3 to 1 in of basin rain), not a new crest, though DeLand is forecast at 6.3 ft from Saturday, 0.03 ft under its 6.33 record. **What would make it so:** a Flash Flood Warning or reports of water in homes across metro Broward or Palm Beach tonight, then NFIP claims dated 11/25 appearing in the next load.

## Item 3. Flagstar (OCC consent order AA-ENF-2026-45, PDF read whole, HTTP 200)

| Fact | Order text |
|---|---|
| Penalty | $112,000 civil money penalty under the Flood Disaster Protection Act §102(f) |
| What was violated | 12 CFR 22.7: notify the borrower when flood cover is inadequate and **force-place cover if the borrower has not bought it within 45 days** |
| Scope | **82 violations, September 2022 to June 2024**, on loans in special flood hazard areas, "under the Bank's previous leadership"; the bank neither admits nor denies |
| Geography | **none stated**: no state, county or loan list |
| Dates | signed by the board 10/22/2026, by the OCC 10/23/2026; announced 11/24 |

**What it means for the "loss is mostly uninsured" HYPOTHESIS:** almost nothing, in either direction. It shows that cover REQUIRED on mapped-zone mortgages can lapse when a servicer fails to force-place; it is small (82 violations at one bank over 22 months) and not shown to involve Florida. The current Florida question sits mostly elsewhere: 54% of insured claims are outside the mapped zone, where no purchase rule applies. The hypothesis stays a hypothesis; countywide take-up still is not coverage among flooded homes.

## Item 4. Client strings, for Will's 11/24 23:44 ET question

| When | Site | Client string sent | Result | Basis |
|---|---|---|---|---|
| 10/29 04:09Z | fema.gov/disaster/4955 (3 pages) | the WebFetch tool's own client (a different client; possibly a different network origin) | 200, read | 10/29 session transcript |
| 11/17 20:1x ET | floridaelectionwatch.gov + four others (first probe) | "Mozilla/5.0 (research script)" | Cloudflare challenge; stopped | CORAL's own disclosure, research file of 11/17 |
| 11/25 04:23–04:25Z (the 11/24 session) | fema.gov/disaster/4955, fema.gov RSS, DisasterAssistance.gov | **`curl/8.5.0`** (plain `curl -s -m`, no `-A` flag) | **Access Denied (Akamai)**; stopped | **11/24 session transcript, read today** |
| 11/25 16:40Z | fema.gov/disaster/4956 | **`research-bot/1.0`** | **403 Access Denied (Akamai)**; one request, stopped | this session |

**Had CORAL switched under WQ-735 before the refusal? No.** No WQ-735 packet was addressed to CORAL and no CORAL script carried a browser string (CORAL's 11/23 record, `STATUS_DETAIL.md` § AL7), so nothing was switched; the 11/24 calls were ad hoc and sent curl's default. **What this does and does not show:** two plain, honest strings were refused, so the switch to `research-bot/1.0` is not what made fema.gov refuse. The cause is **not isolated**: the 10/29 success used a different client that may also have left from a different network address, so the difference could be the address, the client type, or a rule change at fema.gov between 10/29 and 11/24. One more site refused CORAL on 11/24: DisasterAssistance.gov (same string); Sen. Scott's site returned 503 (a server error, not a refusal). OpenFEMA, on the same host, answers 200 to both strings.

## Item 5. Inbox: 8 of 8 dispositioned, every sender (`board_log.tsv`, rows from 2026-11-25T11:47:33)

Correction COR-20261124-21 (the CIA/ODNI card) receipted NO-OP. SIG-W-20261125-021 (arrived about 11:50 ET) was untracked at first; moved to `processed/` after WALTER's commit 1a99ebde50 (CORAL commit 2fbd690fc9). Inbox empty.

| Item | Disposition |
|---|---|
| WALTER SIG-W-20261125-021 (DeLand 6.3 vs 6.33 record) | noted: the same figure as CORAL's and AEOLUS's NWPS read; on two decimals 0.03 under, not a record |
| WALTER SIG-W-20261125-019 (declaration confirmed) | acted: re-read at OpenFEMA, item 1 |
| HOMER 11/25 09:37 (DR-4956 confirmed) | acted: same; FHA 90-day carried as HOMER's DERIVED figure |
| WALTER SIG-W-20261125-009 (CA tides; SE FL watch) | acted: item 2; California is AEOLUS's |
| WALTER SIG-W-20261125-012 (Flagstar) | acted: item 3, order read |
| WALTER SIG-W-20261125-004 (releases; FHFA Q3 FL +2.13% YoY) | noted: KB ML-CORAL-200, WALTER's reading, not re-read |
| WALTER SIG-W-20261124-021 (CIA/ODNI correction) | skipped: no Florida channel |
| AEOLUS 11/25 11:47 (SE rain hazard read) | acted: item 2; DeLand 6.3 ft = CORAL's NWPS read, one figure |

## Item 6. The four tests on what I send up

| Test | Applied |
|---|---|
| Cause isolated only if isolated | The fema.gov refusal cause: NOT isolated (item 4). The zone-X share: not evidence of uninsured loss (rival named). The Flagstar order: no Florida cause claimed. |
| Permission is not money | DR-4956 is permission: 0 registrations, 0 funded projects; NFIP $4.84M building paid is the only money observed. |
| Dated horizon on every forward statement | see item 7; each carries a date |
| Search limits stated | second request: OpenFEMA plus FDEM page plus two press searches; county spending: one press search, agendas unread; OIR order unread (scan); fema.gov refused. Absence in these is not absence in the world. |

## Item 7. Forward view (unscored, not registered; CORAL's judgment)

| Expectation | Odds | Horizon | Why | What would change my mind |
|---|---:|---|---|---|
| FEMA adds household aid for at least one of Seminole, Volusia, Broward | 55% | by 12/22/2026 | the state asked 11/24 (expedited); record river stages in Seminole and Volusia for weeks; FDEM posted an amendment of the Isaias declaration on 10/29, two days after it (what that amendment added was not re-read today) | a denial letter, or nothing by 12/07 (WALTER's watch window) would cut it toward 30% |
| The 11/25 southeast rain becomes a large insured event (NFIP Florida claims dated 11/24–26 exceed the ~1,120 of 11/01–03 when loaded) | 15% | first load covering those dates, expected by about 12/15 | the heavy cells fall on undeclared metros with higher take-up (Broward 19.2%, Miami-Dade 33.4%), but the forecast is 2 to 5 in, the rain ends tonight and no flash flood warning is up | a Flash Flood Warning with home flooding in metro Broward or Palm Beach tonight |
| DeLand reaches or passes its 6.33 ft record | 35% | by 12/02 | NWS forecast 6.3 held from 11/28; Melbourne: further rises "cannot be ruled out" | the next NWPS forecast cutting the crest below 6.2 |

**Tradeable?** Sent to TERRY unasked (`AGENTS/TERRY/inbox/2026-11-25_from-CORAL_declaration-confirmed-no-card.md`): no supported trade; no card asked. **Signals:** none new for WALTER (019 already carries the declaration). **Shared figures:** DeLand 6.3 ft is one figure with AEOLUS; rainfall figures are AEOLUS's; no MARCO figure touched today. **HOMER:** packet with the NFIP zone split as a partial answer to its in-and-out-of-zone ask (`AGENTS/HOMER/inbox/2026-11-25_from-CORAL_nfip-claims-by-zone.md`).

## GATE-CORAL-MSI-01: reading #16 (for the GATES row, verbatim)

> Reading #16 (Parcl build 20261125T101511Z, data date 2026-11-24, current series, WQ-475 A): 4 of 5 above 6.00 — Tampa 7.09, Punta Gorda 6.05, North Port 6.13, Lakeland 6.22, Cape Coral 5.78 ⇒ re-fire reading FAILS, clock at zero; stand-down N/A; leg 🟠 unchanged. Revisions to 11/15 upward only, to +0.04; #15 stands as recorded (WQ-475 (c)). Next reading #17 by 2026-12-03; recommended review_by 2026-12-03 (graded by CORAL 2026-11-25).

## Gaps

Second request outcome; cost share; first dollars; NFIP load after 11/16; OIR 2026-109 content (scan, unread); county and city spending (agendas unread); the final southeast outcome after 01:00 ET 11/26; flooded-home counts (no FEMA registrant data yet); fema.gov (refused, not evaded).

## Commits (none pushed; PROME pushes)

| Commit | What |
|---|---|
| 150b89b947 | CORAL write-back: STATUS, STATUS_DETAIL § AN, CALENDAR, SCRATCH, MEMORY, board_log, KB 196–201, Parcl extract, corrections receipt, 7 inbox moves |
| 8dcd4d78b1 | NEXUS_BRIEF block, pinned to 150b89b947 |
| 5e84ebff61 | packets to TERRY and HOMER (carve-out ①) |
| 16e43833d0 | this packet |
| 2fbd690fc9 | WALTER card 021 moved to processed (after WALTER's commit) |

## COMPLETION

STATUS: DONE (items 1–7 and MSI #16); PARTIAL on what only 11/30 can show
CHANGED: AGENTS/CORAL STATUS, STATUS_DETAIL § AN, KB 196–201, board_log, inbox 8 → processed, corrections receipt, CALENDAR, SCRATCH, NEXUS_BRIEF, MEMORY, sources/parcl; packets to PROME, TERRY, HOMER
RESULT: DR-4956-FL = first (11/09) request: IA 6 counties, PA A–B only, no HM; second request pending; 0 dollars; NFIP still 1,157 (11/16); SE rain not yet a large event; Flagstar has no Florida tie; fema.gov refused curl/8.5.0 and research-bot/1.0 alike; MSI #16 re-fire fails
GAPS: second request; cost share; NFIP reload; OIR 2026-109 unread (scan); county spending; SE outcome after 01:00 ET 11/26; client-string cause not isolated
WILL_NEEDS: none
FOLLOW-UP: D:L1244 stays 11/30; GATES MSI-01 review_by 12/03; DeLand vs record 11/28; DR-4956 amendment watch to 12/07
