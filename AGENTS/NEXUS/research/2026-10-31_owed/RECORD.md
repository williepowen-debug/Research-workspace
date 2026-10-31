# NEXUS — 2026-10-31 owed-work pass (Will-direct) — RECORD

**Session:** Claude Code, claude-opus-5-5 (session ID not exposed). Will 12:03 ET: "Okay lets work on owed and incomplete/unstarted tasks for NEXUS." Boot 12:01 ET: root CLAUDE/AGENTS/USER + local CLAUDE explicitly read; no local AGENTS.md; 0a rc 0 (STATUS 24,048 B = 74%); 7a rc 0; HEAD = origin/master (fetch 12:0x ET); foreign dirty paths (CATO ×2) untouched; no pull needed.
**Tier:** HEAVY (READ_CAP rule-5 rotation of STATUS before writing; 15a cold read). Not a full matrix review: no digest readers; owner deltas read directly and annotated.

## 1. Owed items found at boot and what this pass did

| Item | Source of the obligation | Done this pass |
|---|---|---|
| DAEDALUS prose-remedy census #2 (CLAUDE.md:155) | inbox packet 10/30 | **DECLINE**, reason written on the line; reply `AGENTS/DAEDALUS/inbox/2026-10-31_from-NEXUS_prose-remedy-census-2-DECLINE.md` |
| M-03 premium mechanism RESOLUTION-UNVERIFIED | 10/26 grade; BOND ACM carry | **Resolved TRUE-in-spirit** from the NY Fed ACM primary (§2) |
| PRED-38 pre-deadline count (resolves 11/10) | 10/28 handoff "start early" | Helper sweep → `PRED38_SWEEP.md` (§3) |
| PRED-45 pre-deadline read (resolves 11/20) | 10/28 handoff "start early" | Helper sweep → `PRED45_SWEEP.md` (§3) |
| PRED-41 HHDC Q3 date (DOCKET L575 placeholder) | L575 text | No NY Fed advisory found (§4); placeholder kept |
| 9c deferred owner movers (10/28 → 10/31) | 10/30 LAST_COMPLETION | Commit bodies read for all; load-bearing owners read at STATUS/brief (§5) |
| STATUS 364 B from rotation trigger | 10/30 handoff | Rotated to <70% (§6) |

## 2. M-03 premium mechanism — graded at the primary

Letter (`research/2026-10-08_disc-J_letters.md` line 21): premium half = ACM 10Y term premium moves the same sign as DGS10 over the run ⇒ TRUE-in-spirit. NY Fed `ACMTermPremium.xls` pulled 2026-10-31T12:07:08-04:00 (file crc32 a7bb28d7; not committed, 10 MB); calculation `M03_ACM_mechanism.json`.

| Reading of "the run" | DGS10 (FRED first-published) | ACMTP10 | ACMRNY10 (expected path) | Same sign? |
|---|---|---|---|---|
| anchor 10/8 → fire completion 10/23 | 5.22 → 5.00 = −22bp | 0.920 → 0.674 = **−24.6bp** | 4.297 → 4.296 = −0.1bp | yes |
| anchor 10/8 → first fire cell 10/22 | 5.22 → 4.96 = −26bp | **−28.1bp** | — | yes |
| between fire cells 10/22 → 10/23 | +4bp | +3.5bp | — | yes |

**Verdict: DOWN HIT (graded 10/26, 78→74) is TRUE-in-spirit; the premium mechanism is no longer RESOLUTION-UNVERIFIED.** The fall was essentially all term premium; the expected-rate path was flat. Letter closed; number stays withdrawn (no successor); no Conf % moves. ⚠️ ACM daily values are model estimates that can revise; vintage = this pull. Cross-check: BOND STATUS ACM 10Y TP 0.6061% [10/27] = file 0.6061. The letter named HENRY's read; HENRY has not refreshed ACM, so NEXUS read the primary BOND also cites. C-36 LEVEL/SPLIT label is not re-adjudicated here (a duration-driver window, not the label's test).

## 3. PRED-38 / PRED-45 running reads

**Helpers:** two fresh-context read-only Opus helpers (general-purpose, model opus per Helper-model selection), one per letter; files beside this record. NEXUS spot-checked at the downloaded artifact.

**PRED-38 (`PRED38_SWEEP.md`, helper 12:04–12:22 ET): running k = 0 among 27 banks examined; no near-miss in $50–99.9M; coverage INCOMPLETE.** No bank attributes any Q3-26 net charge-off to a non-depository financial borrower in its own words. Closest, none counting: TFC C&I NCO $106M (10-Q 0000092230-26-000129 Table 15, no NDFI attribution; NEXUS did not re-locate the cell) · GS Q3 provision $368M "primarily reflected impairments related to wholesale loans" (8-K 0000886982-26-000529 release — **verified by NEXUS in the downloaded release text**; a provision, not an NCO; 10-Q pending — the one to watch) · JPM CIB NCO $211M unattributed (exhibit 99.1 narrative not read) · PNC commercial NCOs up, no attribution or figure. **Q3 10-Q not yet filed (27):** JPM, C, GS, MS, USB, PNC, COF, FITB, KEY, RF, ZION, MTB, EWBC, FHN, ALLY, FCNCA, WTFC, PNFP, BOKF, BPOP, COLB, VLY, FLG, FNB, BKU, SCHW, SHUSA; OZK files at the FDIC. ⚠️ **Access limit:** `www.sec.gov` document fetches returned HTTP 403 "Undeclared Automated Tool" to the fleet UA (`Prome Filing Radar contact: research@local`, `FORGE/tools/filing-watch/poll_edgar.py:30`); `data.sec.gov` and `efts.sec.gov` worked. All document text was read from issuer-hosted copies of the same filings or the bank's own release; byte-identity to EDGAR not checked. The 403 is a claim about this request header, not about SEC availability (flagged to PROME; not NEXUS's tool). **State:** PRED-38 stays 🔴 ACTIVE; resolve at the first boot on/after 11/10 (DOCKET L572) after the 10-Q wave (large-filer deadline ~11/9).

## 4. PRED-41 — HHDC Q3-26 release date
NY Fed media advisories probed at `newsevents/mediaadvisory/2026/<MMDD>-2026` for 10/20–10/31: only 10/21 exists (NY Fed–ECB NBFI workshop, Fri 11/13 — context for PRED-38/BROCK, not a release). Prior pattern: advisory → release 8/4 → 8/11, 5/5 → 5/12 (web search, NY Fed advisory pages). ⇒ **Q3 release date UNVERIFIED; with no advisory by 10/31 a release before ~11/6 is unlikely, not excluded** (the probe covers one URL pattern only). DOCKET L575 stays a placeholder; first post-release boot governs.

## 5. FRED cells and owner deltas since 10/30 (delta-annotated, not re-swept)
FRED first-published pull 2026-10-31T12:08:43-04:00 (`fred/`): latest cells obs 10/29 (ICE, VIXCLS), 10/29 (DFII10/DGS10, published 10/30). **New: L13 cell 9 = DFII10 2.63 [10/29] ≤2.64 ⇒ DOWN run 1 of 5**; earliest fire still cell 13 (obs 11/4). ICE 10/30 cells publish Mon 11/2. M-01/M-04b/M-07/M-08b: no run on these cells.

## 6. Rotation and 15a cold read
STATUS 24,048 B (74%) → **22,738 B (69.9%)**. Three verbatim blocks to `STATUS_COLD.md` from the file as committed at 501555a51, each payload line verified present in HEAD: **§H25** (crc32 c526c913, 6 lines: 10/30 header, 10/26 review header paragraph, T-31, two narrative paragraphs, closing owner deltas) · **§H25b** (4de973a5: T-18/20/22/24 row, done `Fri10/30` docket row) · **§H25c** (e3d8a88e: M-06, M-09 rows; live rows keep state). Obligation audit: matrix, root, docket and letter tokens compared HEAD vs live — only the rotated finished rows dropped. Stale owner labels refreshed (BOND through 10/28, BRENT committed 10/29, SAM BOJ primary, LIQUID H.4.1). 48 glued dates spaced (claim_check glued clean).
**15a cold read** (Sonnet `coldreader`, ledger `COLDREAD.md`): ❌1 applied — M-04 row still said HENRY gamma STALE 10/22 against the new narrative; now HENRY 10/30 gamma NEGATIVE, cells to 10/29, Last upd 10-31. ⚠️ applied: L13 "Cells 1–8" → 1–9; T-24 pointer → STATUS_COLD §H25b; HY<260 guard distance → 326 [10/29], 66bp; real 10Y → 2.63 [10/29]; PRED-38 denominator "banks read"; claims wording → LABOR's DOL 10/29 read; glued text (already fixed by the glued pass). ⚠️ not changed, with reason: two term-premium figures carry different end dates (−24.6bp to 10/23 is the letter's run; −25.5bp to 10/29 is the level row) · "week 10/28" is LIQUID's own H.4.1 label · line 9 "Neither test fired" and the M-02 gap sit in unrewritten text owed to the 11/3 full pass · "gpt-6.1-sol" is the true 10/26 record.

**PRED-45 (`PRED45_SWEEP.md`, helper 12:04–12:25 ET): no qualifying arms-length loan-level transfer ≤90.0¢ found; NOT a clean MISS — the window runs to 11/20 and the decisive 10-Q realized-loss notes were mostly unreadable today.** `www.sec.gov` returned "Rate Threshold Exceeded" (~12:05) then 403 "Undeclared Automated Tool" to the fleet UA; WebFetch truncates a 10-Q at ~75k characters (NEXUS confirmed: Saratoga 10-Q text = 74,892 characters, ends inside the 2/28 schedule). Not evaded. Nearest items, none qualifying: TCPC ~$523M / 78 companies sold to Pantheon at "95% of the gross fair value as of December 31, 2025" (8-K 0001193125-26-336845, 8/6) — a pool priced to fair value, not a loan priced to par; its Q3 10-Q may itemize it · ARCC $1.2B loans to its affiliate Ivy Hill (not arms-length, no price) · HTGC / OFS realized losses with no loan or price (INSUFFICIENT) · Onex figure is a mark. **Saratoga lead closed by NEXUS at the issuer release:** fiscal Q2 (quarter ended 8/31) 8-K Ex 99.1 (0001213900-26-107199, read via WebFetch 12:2x ET): no First Brands mention; "$2.1 million of realized gains, primarily from the Gen4 and Modis Dental equity conversions"; no realized losses reported; Exigo exited at $8.0M (equity, −6.1% IRR); Pepper Palace and the CLO F-Note sold after quarter-end, no price. A First Brands sale near its 7.38¢ mark would have produced a large realized loss ⇒ none in that quarter (inference from the release; the 10-Q note itself unread). Coverage: Q3 10-Qs filed only ARCC, HTGC, OFS (releases read); ~29 listed BDCs + 10 non-traded due ~11/2–11/16. Court dockets not checked. **State:** PRED-45 stays 🔴 ACTIVE, 35% HELD; resolve 11/20 (DOCKET L574).

## 7. Follow-up after WQ-565 (Will "ok approved" 12:38 ET; PROME 7981db15c set the SEC UA to PROME-Research + Will's email, 0.25 s pacing) — 2026-10-31T12:41:47-04:00
sec.gov document fetches now return 200 (sequential, one at a time; UA read from `poll_edgar.py`, never typed).
- **Saratoga lead CLOSED at the primary:** 10-Q 0001213900-26-107187 (filed 10/6, quarter to 8/31) still carries the First Brands positions in its Saratoga CLO 2013-1 schedule at 8/31 (1st-lien 3/21 principal $1,346,904 + $57,237 split tranche vs $1,404,140 at 2/28; New Money DIP A $1,581,855; Roll-Up DIP B $3,569,559, unchanged). Held, not sold ⇒ no PRED-45 transfer.
- **OFS:** 10-Q 0001487918-26-000091 — the Q3 $7.8M realized loss is "the sale of a Structured Finance Security (Apex Credit CLO 2022-1 Ltd.)": a CLO security, not a private-credit loan ⇒ NO.
- **HTGC Simon Data — LEAD, INSUFFICIENT under the letter:** 10-Q 0001280784-26-000054: Q3 gross realized losses $2.2M "primarily from the sale of our debt investment and write-off of our warrant investment in Simon Data, Inc." plus other write-offs. Prior marks: 6/30 10-Q 0001280784-26-000042 principal **$5,033K, cost $5,272K, fair value $2,194K (43.6¢)**; absent from the 9/30 schedule. No sale price, buyer or arms-length status disclosed. Bound from the aggregates only: debt loss ≤ ~$2.1M ⇒ proceeds ≥ ~$3.17M ⇒ **≥ ~63¢ of par**; >90¢ would mean a loss ≤ ~$0.74M. The price can sit either side of 90¢, so it is not a documented ≤90¢ transfer. To settle: HTGC disclosure of proceeds (call transcript / later filing) or BROCK.
- PRED-38 not re-read: most Q3 10-Qs unfiled; the 11/10 grade reads them.
**State:** PRED-45 stays 🔴 ACTIVE, 35% HELD; no fire.
