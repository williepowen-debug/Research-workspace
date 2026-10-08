# OZK MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Condensed 2026-09-24 (Will-directed): duplicates merged, LESSONS restatements → pointers, old session blocks → git. Cap at 100 lines — promote to thesis or delete, never just accumulate. For verified mistake patterns with prevention rules, see `LESSONS.md`.*

---

## Feedback
- [2026-04-02] Will values boot transparency — wants to know what was read, in what order, and whether the process is working. Don't orient silently; confirm orientation.
- [2026-04-02] Will prefers sessions to have freedom rather than being laser-focused on pre-set priorities. Provide context, not directives. Rejected ranked TOP 3 queue in favor of a single "open question."
- [2026-04-02] Will thinks long-term about infrastructure. When proposing solutions, address scaling and durability, not just immediate need.
- [2026-04-02] Will prefers breaking large implementation work into discrete tasks done one at a time, with approval between each.
- [2026-04-16] Will wants full source documents (PDFs, 10-Ks) read before opining, not just spot-check sections. Thoroughness > speed for primary source analysis.
- [2026-04-22] **Iteration philosophy validated:** Write Round 1 with available data, then improve as more data arrives. Will explicitly said "begin with what we have and we will improve on it as we learn more." Don't wait for perfect data to start writing.
- [2026-04-22] **"What I NEED FROM YOU" lists work.** When analysis files end with an explicit gap list, Will reads it and delivers the exact files. Keep these lists concise and specific (filename + what's in it).
- [2026-04-22] **Thesis architecture: "synthesis + pointer" pattern.** THESIS.md carries the synthesized takeaway from sub-docs (2-3 sentences + headline number + pointer), not duplicated detail. Sub-docs (IQHQ_PLAYBOOK, SEVEN_CREDIT_DEEP_DIVE) hold the deep analysis. Filter: thesis-level shifts get changelog entries; evidence accumulation stays in sub-docs + KB rows.
- [2026-04-22] **Domain CHANGELOG per bank.** OZK/CHANGELOG.md tracks OZK/THESIS.md only — mirrors format of REGINALD's `thesis/CHANGELOG.md`. Version convention: vX.Y where major = structural, minor = refinement.
- [2026-04-24] **Cross-agent channel writing — strip pleasantries.** REGINALD_CHANNEL is LLM-to-LLM. Skip "welcome," "thanks," social glue. Tight bullets, shorthand that matches the other agent's, link-don't-restate. Will corrected initial draft on this.
- [2026-04-24] **Don't frame editorial judgment as tests/pass-fail.** Describing channel inclusion decisions as "test passed" made collaborative comms sound evaluative. Use "filter" or just state the reasoning. Writing to a collaborator isn't a gauntlet. Will pushed back on this framing.
- [2026-04-24] **Offer files, not verbal reports** — audit/review/analysis goes to a named file in own dir (the file is the handoff).
- [2026-07-04] **When Will asks for a priority ORDER, propose one, then work it one task at a time with a checkpoint between each** (overrides the 4/2 single-open-question default when he asks). **Direct writes to another desk's inbox are sanctioned on his explicit instruction.**

## Findings

**Sources & access (OZK files with the FDIC, not the SEC)**
- [2026-07-04 · consolidated 2026-09-24] **OZK files 10-K / 10-Q / 8-K AND Section 16 insider forms with the FDIC (cert #110), not the SEC.** Mechanism: a bank registered under Exchange Act §12(i) files with its primary federal banking regulator; the holding company was dissolved in 2017. **There is no *SEC* 10-Q — there IS an FDIC 10-Q** (`raw/Q1_2026_10Q.pdf` cover: "FEDERAL DEPOSIT INSURANCE CORPORATION · FORM 10-Q · FDIC Certificate No. 110"). SEC CIK 0001569650 is OZK's 13F/13G investment-manager arm; CIK 0001038205 (Bank of the Ozarks Inc) has nothing after 2017. **An empty EDGAR CIK is the EXPECTED observation, not evidence of absence** — the 8/23 note that dropped "SEC" closed this desk's best primary for 5 days (→ `LESSONS.md` §"Compressing a Finding Drops Its Qualifier", KB-OZK-228).
- [2026-10-02] **FDIC FLNG does NOT carry OZK's press releases.** OZK's 9/30 Q3-date release and 10/1 dividend release were both absent from `/api/instflng/cert/110` at 10/2 08:31 ET (newest id still 11981). A quiet FLNG answers only "was an 8-K/10-Q filed?" — never "was anything announced?" For dates/dividends/notices also search GlobeNewswire (ir.ozk.com 403s scripts; WebFetch times out; syndications such as manilatimes.net render). On 10/1 this desk wrote "Q3 date not announced — FLNG quiet" a day after it was announced.
- [2026-07-06] **⭐ FDIC securities-filings JSON API** (`securitiesfilings.fdicconnect.fdic.gov`; old efr.fdic.gov redirects here; browser User-Agent only): `/api/instdiscl/cert/110` = every Form 3/4/5 · `/api/instdiscl/{disclID}` = transaction lines (`asetSctyAcqDspsCde` A/D, `…Cnt` shares, `…ShrAmt` $/sh, `asetSctyOwnCnt` post, `asetSctyTranDte`; exact price range is in the footnote text) · `/api/instflng/cert/110` = all company filings · `/api/instflng/{id}/attachment/{n}` = **the PDF itself** (bypasses 403'd ir.ozk.com). Mechanized as `scripts/flng_watch.py` (in boot.py; `--selftest`).
- [2026-04-22 · 07-18] **What lives where.** Quarterly 8-K bundle (FDIC) = press release + Management Comments (RESG deep dive, substandard roster, sub-notes schedule) + Financial Supplement; the GlobeNewswire/StockTitan release is truncated to EPS + quote. **10-Qs are text PDFs** (pdfminer, tab-delimited; grep "debt-on-debt", "nonaccrual", "subordinated"); **10-Q p.37 carries mgmt's debt-on-debt balance every quarter.** Image-only PDFs (Atrium) need the Read tool's `pages` param. ir.ozk.com 403s scripts — browser only, rarely needed now.
- [2026-08-07 · 09-24] **⭐ FFIEC CDR PWS (REST + JWT).** Base `https://ffieccdr.azure-api.us/public/<function>`, GET. **Every parameter is a HEADER** — `UserID`, **`Authentication: Bearer <token>`** (not "Authorization"), `dataSeries: Call`, `reportingPeriodEndDate`, `fiIDType: ID_RSSD`, `fiID: 107244`, `facsimileFormat: SDF`; query-string forms return 500 "Error Code 5001" (looks like auth, isn't). `RetrievePanelOfReporters` verifies RSSD (OZK = **107244**). `RetrieveFacsimile` body = JSON string of base64 → `;`-delimited SDF. python-urllib default UA is 403'd by the WAF (UA block, not auth). Creds: `FORGE/tools/market-data/.env` (desktop). ⏰ **JWT expires 2026-11-05 — Will action; the Q3 pull (~Nov 1-10) straddles it.**
- [2026-08-07 · 09-24] **Call Report card.** Past-due "OZK basis" = RCON1406+1407+1403 ÷ RCON2122. **NPA% over TOTAL ASSETS** (RCON2170). **NCO ann. on RC-K average loans** (RCON3360), YTD-differenced (RIAD4635/4605 are YTD) — Q1-26 0.56% avg / 0.55% period-end. RCON3123 = ALLL only (~$148M below reported ACL). **No classified/criticized line, no credit names.** **MI3 `RCON2746` ≡ `RCONPV09` (9.a "Other NDFI") ≡ the 10-Q debt-on-debt book** at every quarter checked; Memo-10 `PV05-09` (funded) / `PV12-16` (unfunded) tie the 10-Q NDFI breakdown to the dollar.
- [2026-07-18] **Nasdaq short-interest API** — `api.nasdaq.com/api/quote/OZK/short-interest?assetClass=stocks` (browser UA) = ~24 FINRA settlements with DTC; yfinance gives only the latest two. Float % must be derived. [KB-214]
- [2026-04-02 · 08-23] **Price tooling.** `scripts/market.py` is repo-root (run from root with `.venv/bin/python3`). `fetch.py price --json` carries `asof`/`prev_asof` — branch on vintage, not on "JSON parsed"; `change_pct` is **null** when there's no prior bar (crashed boot.py 9/24). A stale price feeds the <$45/<$40 bands that page other desks, so a stale-as-live bug is an escalation bug.

- [2026-10-08] **San Diego County Recorder (`arcc-acclaim.sdcounty.ca.gov`) returns 403 to curl and WebFetch** — the RaDD instrument (a "Fifth Modification", filed 10/2) is browser-only. Citi read it before any FDIC filing or OZK release existed. **A sell-side read of a RECORDED instrument can be the first disclosure**: quiet FLNG + EFR + EDGAR + releases did not mean no news on 10/6.
- [2026-10-08] **`scripts/boot.py` INBOX lists `inbox/*.md` only — blind to `inbox/WALTER/`** (an ACTION signal sat there on 10/8 while boot said "1 unprocessed"). Always run `python3 PROME/tools/inbox_census.py OZK` too; note it counts `.gitkeep` as a top-level file. Fix owed (TODO T1).

**Domain facts**
- [2026-04-22] **IQHQ exposure is ONE credit** — "one credit with IQHQ… the senior secured loan on their San Diego RaDD project" (Rossow, OZK CCO, Bisnow 3/19/26). Boynton Yards is **not** IQHQ (Leggat McCall/DLJ/Deutsche Finance). Other IQHQ lenders: Fenway→JPM $165M · Elco Yards→KREF $581M · **Spur Ph I→Apollo $275M (deed-in-lieu to Apollo 9/17/26, single-source TRD)** · 155 N. Beacon→Citizens $486.5M.
- [2026-07-04 · 09-24] **⛔ Vintage trap — seen 5× (5th: 9/27 search summary, via Bisnow 3/19/26 restating the 2024 extension):** search surfaces a "two-year RaDD extension → Aug 2028" and a "Citi downgrade" as current; both trace to **Jun-2024 Bisnow / May-2024 Citi**. Maturity = **Aug 2026**, from the primary Q1'26 transcript (Mealor, Gleason). Check article dates; check the local primary before re-opening. RaDD funded static at $555M since May 2024.
- [2026-07-04] **RESG concentration (6-qtr primary):** share of unfunded 71→60% (Q4'24→Q1'26; ~79% peak), commitments $34.5B→$27.8B; "88%" is a phantom. [KB-196]
- [2026-07-04 s2] **Bluerock = Bluerock Total Income+ (now BPRE), not "Bluerock Homes."** PIK loans real ($160M@13.5% + $86M@14%); first-loss equity ~$488M; its NAV mark leads RaDD credit. Trade press can confirm a figure while misnaming the entity — verify both. [KB-197/198]
- [2026-07-06] **Sterling Bay: one loss (Lincoln Yards, foreclosed, 320K SF), one PAR exit (Pacific Center, full repayment per Q4'25 Mgmt Comments).** Grep our own quarterly extracts before banking a severity claim from trade press. [KB-199]
- [2026-09-24] **Use pdfplumber layout mode for FDIC PDFs with tables** (`.venv` has pdfplumber; no poppler/fitz). pdfminer plain text scrambles table columns and moves row notes — it caused the Dec 18 / Boston misattribution. `extract_text(layout=True)` keeps rows readable; the Q2 10-Q is 69 pp / 2,875 layout lines.
- [2026-10-08] **RaDD maturity history:** original 4-year term from Aug-2022 → stated maturity **2026-08-26**; "Fifth Modification" (effective 8/26, signed 9/30–10/1, filed 10/2) → **2026-10-09** [Citi 10/6 via SA/Bisnow — single-source terms; OZK CCO confirms short extensions "routinely occur"]. Citi's own words: "OZK has done this before (short duration extensions) with other sponsors." [KB-243]
- [2026-07-06] **Square Mile Capital = Affinius Capital** (2023 rebrand); OZK holds $95M of the Affinius-originated 777 Industrial note. [KB-203]
- [2026-07-06] **LLM-sourced KB rows can garble primary figures** (KB-117 vs Atrium primary) — treat Conf one notch worse when Source is an LLM output. **Date a third-party report by its citations, not its label** (Atrium said "2026"; citations stop Sep-2025).
- [2026-07-18] **OZK is a beta/range name** — the Nov'25 low was beta to the Oct'25 NDFI-contagion selloff, and the Sep'26 −6.1% was mostly sector (Fed hike, financials selloff). Check the cohort's move before attributing a price move to own-credit. [KB-215]

**Method (the rules themselves live in `LESSONS.md` — pointers only)**
- [2026-07-06] **Partial propagation is this desk's dominant doc-rot mode** — when correcting a figure, grep ALL surfaces for the old value; at revival, check TODO/KB resolutions before re-opening a "gap."
- [2026-08-07] Reproduce a baseline before grading against it (the 37.6% MI3) · never threshold a transit bucket (kill-§1) → `LESSONS.md`. **Don't fix another desk's number, even when disproved** — banner it, write the evidence, route it to the owner.
- [2026-08-23] **Reproduce the other desk's number first** (REGINALD's +$98M, exact) — it shows you're disputing *coverage*, not *accuracy*, and it lands as collaboration. A YoY window nets out a single-quarter step.
- [2026-09-24] **Net quarter-end balances can't exclude a transfer offset by runoff; watch scripts fail closed** → `LESSONS.md` (CATO RB2/RB3).

## Session Notes

⚠️ **Open question:** what replaced the RaDD bridge at its **Fri 10/9** maturity — a multi-year extension with new money (A-path evidence), another bridge, or default/forbearance? And will Will rule **P-OZK-6** (a stopgap is NOT an "executed extension" for OZK-09) before the 10/21 call makes the reading outcome-contaminated? *Carried: does OZK report memo item 3 from the debt-on-debt book only (TODO R4)?*

**CHANGES SINCE:** *(leave blank — next boot populates via boot.py)*

### LAST SESSION (2026-10-08 Thu — PROME `prome-fc` wake, WQ-391 item 3; laptop; Claude Code, claude-opus-5-5)
- **<$45 band graded FIRED on the 10/6 close $44.58** (10/7 $43.56; two routes agree). The letter's only consequent (🔴 to REGINALD + PROME) was discharged two sessions late: REGINALD packet, PROME memo, SIGNALS row, WALTER routing packet.
- **Cause search, 12 legs** (thread §2): every primary reachable was quiet (FLNG, EFR, EDGAR, releases, ratings). **Found at the secondary level: the Citi 10/6 note on the RaDD Fifth Modification** — maturity 8/26 → **10/9**, signed 9/30–10/1. Terms single-source; the bridge's existence is issuer-corroborated (CCO to Bisnow). Attribution of the −4.31% day: INFERRED. The BPRE webinar was after the close.
- **Zero grades/weights/thresholds/conviction moved.** Proposed **P-OZK-6** (Will-gated, not applied). Corrected the record: the 8/26 maturity was bridged, not quietly extended (STATUS, PLAYBOOK, INDEX). KB +243/244 → 244/37.
- **Inbox 1+1 → 0:** WALTER SIG-W-20261008-003 (`board_log.tsv` created — first row) · PROME Fidelity capture → `POSITIONS.md` LIVE (Nov-20 $40P ×4, no card; G2 discharged — the Aug-21 legs are absent from the capture). `.consumed.tsv` created.
- **REGINALD b92113ed0 consumed + reconciled:** 154%/78% = ALLL basis (reproduces); "Seattle office sold at 58%" vs our "marked to an offer" — REGINALD to confirm; 95–100% scope = the 3 Q2 transfers.
- → `research/threads/2026-10-08_BAND_FIRE_CAUSE_RADD_STOPGAP.md` · memo `PROME/inbox/2026-10-08_from-OZK_band-fired-cause-radd-stopgap.md`.

### PRIOR SESSIONS (one line each — detail in `git log -p -- AGENTS/OZK/MEMORY.md`)
- **10/2** (`prome-70`, L463): FLNG rc 0 ⇒ sub-notes reset HAPPENED, uncontradicted; Q3 date CONFIRMED 10/20 AMC / call 10/21 (OZK release 9/30 — FLNG omits press releases); query A `when:7d "IQHQ"` ADOPTED; regional-bank calendar 10/2–10/16 filed for PROME.
- **10/1** (`prome-0c`, L126): indenture read ⇒ coupon ≈6.19%, drag ≈+$12.3M/yr; R3 lane phrases IQHQ + Campus at Horton adopted, BPRE declined; L126 RESOLVED.
- **9/27** quiet catch-up + CRE-transmission leg + RaDD severity label fixed (50–65%, $275–360M) · **9/24** Q2 10-Q full read, L181 LEGITIMATE, CATO OZ1–4, Dec-18 = Baltimore.

### ARMED FOR NEXT WAKE (set 2026-10-08 — no live pane will re-ping)
1. **On/after Fri 10/9 — RaDD bridge maturity read (TODO D7):** a sixth modification, another bridge, default/forbearance, or silence. Sources: OZK/Citi statements, Bisnow, SD Business Journal, recorder (browser). Default/forbearance language = 🔴 REGINALD/BROCK/PROME.
2. **CHECK-BY Wed 10/14 — TODO C1 Campus at Horton leasing check.**
3. **Before Tue 10/20 after close — TODO D3 Q3 scoring card** (new legs: RaDD term, RaDD 9/30 rating + past-due, P-OZK-6 status); then the print **10/20 AMC / call Wed 10/21 8:30 ET** = the RaDD report-back + DOCKET L520 W1–W14 (CHECK-BY 10/31).
4. **Nov 2 → Dec 22 — sub-notes 1/1/2027 call-notice window:** `flng_watch.py` + a press search.
5. **~early Nov — Q3 10-Q** (VERIFY ≈6.19%) · **FFIEC JWT expires 11/5 (Will)** before the ~Nov 1–10 Call Report pull.
6. Price lines: **<$40 band = $3.56 / 8.2% below the 10/7 close** (→ REGINALD, PROME, FORGE). Will's Nov-20 $40P sits there (TERRY's; C5 card by 11/18).

### NEXT SESSION — open queue (priority order; CATO 9/24: evidence before restructuring)
1. Armed items 1–3 above.
2. **TODO R1** — re-derive the $150-300M reserve-build estimate on the Q2 roster + SM concentration (INFERRED; no grade moves).
3. **TODO T1** — boot.py INBOX: add the `inbox/WALTER/` lane.
4. **TODO R2** subdomain refresh, one file at a time with a checkpoint (Will offered 9/27, not yet approved).
5. Carried: C3 Aimco docket · C4 severity comps (Spur deed-in-lieu) · C5 Affinius (UNVERIFIED EVENT) · R3 $87M date · R4 MI3-population · P-OZK-1/4/5/6 Will-gated · charter lines 13/17/19/157/177 stale (Will-gated; offered 9/24).

⛔ **Standing:** D1/OZK-salvage is **RULED-CLOSED.** Do not re-present, re-litigate or propose a successor. Any OZK expression is TERRY-built and Will-approved; Will's 10/7 Nov-20 $40P line is his own, carded (or not) by TERRY.

*Prior session notes (8/28 integrity sweep, 8/31 window-close sweep) → `SWEEP_2026-08-28.md`, `research/threads/IQHQ_AUG_WINDOW_CLOSE_SWEEP.md`, `git log -p -- AGENTS/OZK/MEMORY.md`.*
