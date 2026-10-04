# FALCON — UKMTO 150-26 adjudication (SIG-W-20261004-005)

**Session:** 2026-10-04 ~17:25–17:5x ET · PROME-spawned (prome-ed) on Will's direct word 17:23 ET · BOUNDED to one item (not an inbox drain) · no gate change, no trade.
**Inputs:** PROME packet `inbox/processed/2026-10-04_from-PROME_ukmto-150-26-SIG-W-20261004-005.md`; WALTER handoff + BOARD card `SIG-W-20261004-005` (its final CORRECTION governs: screenshot ATTRIBUTED to UKMTO, not source-authenticated); CATO baseline `AGENTS/CATO/runs/2026-10-04_1702_bookmark-owner-followthrough.md` §BF3; WALTER's Bright Data fetch `AGENTS/WALTER/research/2026-10-04_ukmto-150-26-primary.md` (commit `7525bb064`).

## Decision read

**Nothing fires. B 1 / C 14 / D 85 HELD. Losses stay 3. GATE-FALCON-001 untouched (review 10/06 stands). Production rung ARMED, NOT FIRED.** 150-26 is a **new hull strike** (INFERRED), corroborated in content but **not authenticated at the UKMTO primary**. It is a strike: not a sinking, not a mine. The account's "ninth vessel in five days" is **not supported** by my ledger (8 struck hulls over 7 days by event date). Reconciling it turned up a **missing hull in my own ledger**: UKMTO 149-26, the second 10/02 hit, now backfilled as VI-2026-0044.

## (a) Source status — CANNOT-AUTHENTICATE at the primary; content CORROBORATED by independent secondaries

| # | Request (2026-10-04, UTC) | Response | What it establishes |
|---|---|---|---|
| 1 | curl, browser UA: `https://www.ukmto.org/recent-incidents`, `/indian-ocean/recent-incidents`, `/`, `/ukmto-products/warnings` (21:25:58Z) | **403**, 4,546 B, Cloudflare "Sorry, you have been blocked — You are unable to access ukmto.org", Ray `a457434cb9df5838` | A WAF block on **this client**. It says nothing about the document |
| 2 | WebFetch `https://www.ukmto.org/recent-incidents` | **403** | Same block, from a second egress |
| 3 | curl + WebFetch `https://www.ukmto.org/-/media/ukmto/products/20261004-ukmto_warning_150_26.pdf` (filename inferred from the search-indexed 148-26 product URL `…/20261002-ukmto_warning_148_26.pdf?rev=2a8f…`); also the `20261003-` variant | **403** on all three, **including the 148-26 URL a search engine has indexed** | The 403 hits a known-real file too ⇒ it is a client block, not a missing 150-26 |
| 4 | MSCIO (EU) mirror `https://mscio.eu/folder/documents/UKMTO%20Warnings/` | 200; control `20260526-UKMTO_WARNING_062_26.pdf` = 200 PDF; the listing **ends at 134-26 Update 001 (9/12)**; guessed 147–150 names = 404 | The mirror lags by about 3 weeks. Its silence is not evidence. **It does show UKMTO's convention: new information on a logged incident goes out as "NNN-26 Update 001" under the same number** (used in (b)) |
| 5 | WALTER Bright Data Web Unlocker (`7525bb064`): `ukmto.org` + `/recent-incidents` | exit 0; portal reached; incident feed rendered a static **"0 reports"** shell | **NOT OBTAINED.** A 1,079 B shell whose feed loads by script is a claim about the request. It never means "150-26 absent or withdrawn" (PROME caution, `finding_negative_reachability_is_a_claim_about_your_request`) |

**Corroboration of the attributed text.** I downloaded the image myself (`pbs.twimg.com/media/HTxY-jmWsAAAwxC.jpg`, 843×1194) and read it. Every element matches outlets that reported the UKMTO product independently of that tweet:

| Element on the screenshot | Arab Times 10/04 | Reuters via Middle East Eye 10/04 10:07 BST | Arab News 10/04 12:21Z (AFP style) |
|---|---|---|---|
| Number 150-26, issued 04 Oct 2026 | ✅ "warning number 150-26, issued October 4" | — | issued "Sunday" |
| Tanker, Strait of Hormuz, unknown projectile | ✅ | ✅ | ✅ |
| Engine-room damage | ✅ | ✅ | ✅ |
| Crew safe, no environmental impact | ✅ | ✅ | ✅ |
| Report Date/Time **TBC** | "did not identify the tanker, its flag, the location within the Strait, or the source" | no timing given | ✅ "without specifying when the incident occurred" |

Timeline: @UK_MTO pointer 07:53Z → the tweet carrying the image 08:03Z → Reuters/MEE 09:07Z → Arab News 12:21Z. Consistent.
**Grade:** the event is **B2** (UKMTO product, read through three independent secondaries). The screenshot as an artifact is **unauthenticated**: no provenance metadata, and the primary is unreachable. Its content is corroborated. Next authentication step: the exact product URL in row 3, sent through WALTER's Web Unlocker. That spends Bright Data budget, so it is PROME's call.

## (b) Event identity — NEW EVENT (INFERRED), opened as VI-2026-0045

Ledger before this session: VI-0042 = 147-26 (KAZIMAH III, 10/01 ~1750Z), VI-0043 = the 10/02 outbound hit. **Reconciling 150-26 required establishing the full prior set, and the set was incomplete:**

| UKMTO | Report time (source) | Hull / position | Damage | Ledger |
|---|---|---|---|---|
| 147-26 | 10/01 ~1750Z (third party) | KAZIMAH III (KOTC VLCC), transiting Hormuz | fire on board | VI-0042 |
| 148-26 | 10/02 1122Z (Master) | tanker, OUTBOUND; Ambrey matched it to a **Panama-flagged** tanker (regulasshipping 10/03, single secondary) | small fire + blackout; underway | VI-0043 (mapped today) |
| 149-26 | 10/02 2142Z (Master) | **crude** tanker ~4 nm E of Oman | projectile on the port side; crew safe | **VI-0044 — BACKFILLED today** (Reuters/US News 10/02, AFP/Manila Times 10/04, The Star, Asharq Al-Awsat, MEE, SBS) |
| 150-26 | **TBC / TBC** (Master), issued 10/04 | tanker, area circle just N of the Musandam tip | **engine room**; no fire stated | **VI-0045 — NEW** |

**Why I call 150-26 new, on evidence and not on the number:** (1) UKMTO puts new information on a logged incident under the **same** number as "Update 001" (134-26 precedent), and 150-26 is a new number. (2) 147, 148 and 149 each had a report time UKMTO already held; 150 is TBC, and UKMTO would not lose a time it had logged. (3) The damage differs: 147 fire, 148 fire + blackout, 149 port side, 150 engine room with no fire. SBS (10/05) and kucoin (10/04) both count it as the fourth October incident, separate from 147/148/149.
**Residual UNKNOWN:** the event date. 150-26 could be a *late* report of a hull struck on 10/03 or 10/04 that no other channel reported. One 10/03 search found nothing for 10/03 (its "Saturday" results were 8/29–8/31 events, a date trap). Hull name and flag: none published.
**Side-result (prior events):** WALTER -018's "possible Panama-flagged INBOUND 10/02 hit" is most likely the **outbound** 148-26 hull with its direction mis-stated (Ambrey's Panama match). INFERRED. The other 10/02 hull is 149-26.

## (c) The screenshot's claims and the account's tally, assessed separately

**Screenshot (UKMTO-attributed):** one tanker, **STRUCK** by an unknown projectile, engine-room damage, crew safe, no pollution. **Not a sinking** (nothing says the vessel was lost, and every secondary has it afloat or doesn't say). **Not a mine** (the mechanism is a projectile). Underway versus not-under-command is **unstated**. ⇒ GATE 2-class sinking/mine evidence: none. **Losses stay 3** (VI-0016 dhow 8/4, VI-0024 Kylo 9/5, VI-0028 Riesco 9/8).

**Account tally (@BrettErickson28, 08:03Z): "NINTH vessel in 5 days… highest rate of the entire war"**, which is not in the UKMTO card:

| Test | My ledger (event date) | Verdict |
|---|---|---|
| Struck hulls 9/28–10/04 | 8 (AL FUNTAS; MERSIN PROSPERITY, SINBAD, AL RUWAIS; KAZIMAH III; 148-26; 149-26; 150-26) over **7** days | — |
| Max in any 5-day window | **7** (9/28–10/02); 4 in 9/30–10/04 | "9 in 5" **NOT SUPPORTED** |
| How 9 could arise | counting late reports by report date; double counting (146-26 vs AL RUWAIS; the Panama relay vs 148-26); adding the 10/04 Bab el-Mandeb **near-miss** (SIG-W-20261004-010, not a hit) | method error, not new hulls (INFERRED) |
| "Highest rate of the war" | 9/05–9/09 = **10 hulls** (8 US strikes on Iranian export tankers + 2 unattributed); ledger coverage before 7/12 is thin; ADNOC alone disclosed 15 hulls hit by 8/8 | **CONTRADICTED** on all axes; on the unattributed-merchant axis alone, the 9/28–10/04 run is the densest in my ledger since its 8/10 build, which is not exhaustive |
| Strike vs loss | 8 strikes, 0 sinkings, 0 mines | a strike rate, never a loss rate |

**Fars claim (relayed by SBS 10/05):** the IRGC "attacked at least seven oil tankers over the past five days", including two Kuwaiti and three UAE vessels. That matches my seven hulls from 9/28–10/02 (two Kuwaiti, AL FUNTAS and KAZIMAH III; two ADNOC-managed, MERSIN PROSPERITY and AL RUWAIS; the third UAE hull is unmatched). One query found nothing at Fars itself, so it is **F3, a claim**. If a Fars/IRGC primary confirms it, `attacker_axis` on VI-0038..0044 moves UNATTRIBUTED → IRGC_IRAN (CLAIMED). That would be a ledger change, not a gate.

**Other -005 threads:** Iran's 10/04 restatement of the closure conditions (seven conditions under the June Islamabad MOU, sequencing dispute, denial that it offered inspections for sanctions relief) is a **DECLARATORY** closure claim. It fires no gate; diplomacy stays 3 (KB-239). CNBC's plural "more tankers struck" is consistent with the 147–150 run. On my evidence, 10/04 itself adds one struck hull.

## Implications

| Item | Disposition | Reason |
|---|---|---|
| B/C/D 1/14/85 | **NO-CHANGE** | D75→85 already fired (one move); no registered letter above 85 is keyed on hull strikes; the production rung is facilities-only. The run (8 hulls in 7 days, continuing) **argues against** the D→C trigger (72h two-sided halt) |
| Losses | **NO-CHANGE (3)** | 150-26 and 149-26 are strikes, afloat |
| GATE-FALCON-001 | **NO-CHANGE** | Leg 2 is Bab transit (TankerMap); Hormuz hull hits are outside its letter; the 10/06 review is not pre-empted |
| Convergence | NO-CHANGE (43/50) | Iran/proxy ops already at the 5 ceiling |
| 150-26 hull name / flag / status (underway vs NUC, any CTL) | **WATCH** | Ambrey, Vanguard, TradeWinds, Lloyd's List; a CTL would make it a 4th loss candidate only on a total-loss letter |
| KAZIMAH III "Abandoned" (Wikipedia, tertiary) | **WATCH** | one search found no corroboration; abandoned is a pre-CTL state (cf. CAPE DAO). Normal window |
| Fars 7-tanker IRGC claim | **WATCH** | read the primary; an attribution-axis ledger change if confirmed |
| Primary authentication of 150-26 | **DEFER → PROME's call** | exact URL known (row 3); needs WALTER's Web Unlocker (Bright Data budget) or UKMTO's VRS channel |
| SIG-W-20261004-010 (Houthi Khurais strike CLAIM, disputed) | **NOT CONSUMED — flagged** | outside this bounded scope; Khurais is a PRODUCTION-class facility, so a counting-source confirmation would FIRE the production rung (D 85→92). WALTER's verify found Saudi/Aramco silent and the coalition calling the claim "misleading". Needs the desk's normal window **before** the 10/06 review, or a PROME call |

## Records written (this session)

`domain/vessel-incidents/VESSELS.tsv` (VI-2026-0044 and 0045 opened; 0043 mapped to 148-26 with the Panama flag; 0042 abandoned-watch; data clock → 2026-10-04) · `workbook/KB.tsv` KB-FALCON-236..239 · `board_log.tsv` (2 rows) · `inbox/WALTER/processed/SIG-W-20261004-005.md` + `inbox/processed/2026-10-04_from-PROME_…` (git mv) · STATUS · SCRATCH · NEXUS_BRIEF.
