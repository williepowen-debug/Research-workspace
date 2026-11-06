# REGINALD MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis or delete, never just accumulate. For verified mistake patterns with prevention rules, see `LESSONS.md`.*

---

## Feedback
- [2026-10-20] Will doubts banks accurately report their weaknesses. Do not use reported provisions to validate loss completeness or reported earnings to prove collectibility. Challenge with matched borrower cash flow, independent transactions/court/servicer evidence and outcome bridges; distinguish skepticism from evidence of misstatement. Qualification saved in M&T capacity report.
- [2026-04-02 ×5] Will: **boot transparency** (say what you read, in what order); **freedom over pre-set priorities** (context not directives; ONE open question, not a ranked top-3); think **long-term infrastructure** (scaling + durability); **position data lives in POSITIONS.md** too; **discrete tasks, approval between each.** Full entries → BLOCK M10, crc32 `2d7441a5`.
- [2026-04-16] Will wants REGINALD to read full source documents (PDFs, 10-Ks) before opining, not just spot-check sections. Caught that I only keyword-searched the earnings release initially. Thoroughness > speed for primary source analysis.
- [2026-04-22] **Iteration philosophy validated:** Write Round 1 with available data, then improve as more data arrives. Will explicitly said "begin with what we have and we will improve on it as we learn more" when public press releases were truncated and he was going to provide supplement PDFs. Don't wait for perfect data to start writing.
- [2026-04-22] **"What I NEED FROM YOU" lists work.** When analysis files end with an explicit gap list, Will reads it and delivers the exact files. Keep these lists concise and specific (filename + what's in it).
- [2026-04-22] **Thesis architecture: "synthesis + pointer" pattern.** THESIS.md carries the synthesized takeaway from sub-docs (2-3 sentences + headline number + pointer), not duplicated detail. Sub-docs (IQHQ_PLAYBOOK, SEVEN_CREDIT_DEEP_DIVE) hold the deep analysis. Changelog tracks THESIS.md only. Filter: thesis-level shifts get changelog entries; evidence accumulation stays in sub-docs + KB rows. Scope guard: if writing a 4th sentence of sub-doc summary in THESIS.md, it belongs in the sub-doc.
- [2026-04-22] **Per-bank CHANGELOG** mirrors `thesis/CHANGELOG.md` format (vX.Y; first entry pins prior as v1.0) — now `../OZK/`, `../WAL/`-owned. → BLOCK M11, crc32 `05b22ac4`.
- [2026-06-02] **Scope-clean sessions:** Will will explicitly fence a session ("REGINALD files only, no messaging, no position decisions/analysis"). When fenced, refreshing facts (prices, dates, FRED data) and marking resolved events is in-scope hygiene; recomputing EV/overvaluation, sending outbox replies, and making roll calls are out. Flag stale-but-load-bearing values (e.g. SCENARIOS spot price) rather than recomputing — "flag don't re-rate."

## Findings + References → **`MEMORY_REFERENCE.md`** (COLD, on-demand — **NOT a boot read**)

*Split out 2026-09-14 verbatim, crc32 `5db54789`, 11241 B, under READ_CAP rule 4(b). Nothing deleted.* **Holds the HOW-TO and LOOKUP half:** SEC EDGAR curl pattern (WebFetch 403s on sec.gov) · FFIEC CDR REST/JWT · FRED via `fetch.py` + the T+1 convention · the `perl -0pe` table-extraction recipe (a naive `sed` collapses 8-K tables) · catastrophic-regex warning · two-route derived-figure check · FDIC BankFind as an independent cross-check · the paywall map · **OZK files NO SEC periodic reports** · the cert/RSSD/CIK table · the WALTER LIAISON record. **Pull it when you are about to fetch a filing or debug an instrument — not at boot.** ⚠️ **Mistake patterns are NOT here — they stay in `LESSONS.md`.**

## Session Notes

Original contiguous blocks B01–B08 → `archive/2026-10-20_organisation-cleanup_MEMORY.md`; exact source-line/section map and verified CRCs → `reports/2026-10-20_organisation-cleanup/RECEIPT.md`. Re-check size at any append or on 2026-11-20, whichever first.

⚠️ **Open question at close:** does the 8/20 ranking predict anything? The frozen 11/07 test against simple baselines answers it, as a retrospective check, not a blind one.

### LAST SESSION — 2026-11-05 ~18:00 → 2026-11-06 08:10 ET, Will-launched boot and status; closed on Will's word
- **Runtime:** Claude Code, Opus 5.5, laptop `WilliePOwen`. Evening pull refused on other desks' dirty files, behind 0. `/tmp/mi3/fac` absent here; FFIEC token not re-tested. Failed connectors: definite, mtnewswire, desktop-commander, Indeed; none needed.
- **Rulings found:** WQ-624 A (keep the 14; Preferred and NexBank side list, beside the score) and WQ-622 A covers this desk, so the 11/05 16:05 "NOT adopted" below is overtaken. Set-up not started.
- **Settled 11/05 graded at close:** WAL $75.88, suppressed sub-$78 re-entry, exit 0-of-3, 47 rows; KRE $72.31; FLG $10.60, 21 closes below RED. HY 11/05 not on FRED at 08:10 ET 11/06; latest 332 [11/04]. Primary credit $9.219B [11/04]; FRED series is `WLCFLPCL`.
- **Filings seen, unread:** VLY `0000714310-26-000049`, EGBN `0001050441-26-000113`, BKU `0001504008-26-000091` (16:39 ET, six minutes after my 16:33 scan). CUBI Form 4 sales 11/04: Watkins 5,500 at $86.17; Way 48,796 at $83.88 and 723 at $85.16. EDGAR not re-scanned at close.
- **Intake:** WALTER 062, 063, 066, 067 filed; 067 WOULD-INTEGRATE (M&T Wilmington Trust note, primary unread). Corrections 5 NO-OP receipts. BOARD 0 selected of 105 unlogged at boot.
- **Skipped at close:** all three 10-Qs (Will closed before answering my proposal); combination watch set-up; research retirement sweep; `consumer_check`, no registered figure superseded; derived surfaces other than the brief, no score moved. General inbox left open, 4 packets, listed in NEXT SESSION.

### EARLIER — 2026-11-05 10:30 → 16:33 ET, Will-authorized catch-up via PROME window (prome-98); closed on Will's word
- **Runtime:** Claude Code, Opus 5.5, desktop `DESKTOP-BC6EF81`. Pull refused on AEOLUS dirty files; 52 ahead, 0 behind. FFIEC token live here; `/tmp/mi3/fac` cache rebuilt (138 banks).
- **L895 DONE:** all 4 filed; line diff 0 of 134 changed, 4 added. HSBC USA deposits −$7.69B, not a flag. Frozen universe −$6.54B / +$32.70B; 6 flags unchanged; verdict waits for FDIC.
- ★ **L516:** FDIC posted the P&A today. My first URL 404'd; the right one sat in my 10/9 report. A 404 on a guessed URL is not absence. Schedules redacted, shared figure unchanged, weekly check closed.
- **FL frame:** SBCF, SSB final HOLDS; NO TRANSMISSION line reached; PROVISIONAL until BKU. SBCF $8.4M = PCD measurement-period adjustment.
- **Other:** VLY, OZK 10-Qs not filed; OZK `RIAD5409` flat, sent to OZK channel. CREED T-01a: no bank transmission. HY 332: REG-T-04 NOT FIRED. ROLL70: recommended RETIRE; PROME retired it 11:03 ET (WQ-610 A). Inbox 21 drained. → `reports/2026-11-05_boot/REPORT.md`.
- **Skipped:** NEXUS brief (closeout step); H.4.1 today and H.8 11/06 not yet out; L180 and ranking test stay 11/07.

- **11:38 ET, Will-asked:** PFBC read: route FDIC FLNG cert 33539. Multifamily 30–89 $143.1M (26.5% of book) unexplained; $166.0M problem loans incl. HFS; $51.8M relationship left. Pathward read. Undated threads swept; Chapter 11 and blind-spot builds parked under Will's 10/31 rule → `reports/2026-11-05_PFBC_and_open-threads.md`. **Check the Call Report RC-N past-due column, not just the release: the release showed none of this.**

- **11:47 ET, Will-asked:** one-time scan → `reports/2026-11-05_late-loan-scan.md`. My 10/23 FLG grade did not read the release table showing multifamily 30–89 $392M. The scan script's UNTIED label was my design error; `audit.py` replaces it. **11/07: read each bank's past-due table, not only frozen lines.**

- **12:15 ET, Will-asked:** Ueno → `reports/2026-11-05_Ueno-Paraguay.md`. **My substring filter matched "Buenos Aires" and I told Will 111 fund filings held Ueno; the real figure is 17 series, $17.9M. Match a holdings pull on the CUSIP, and do not report a count before the rows are read.**

- **12:34 ET:** outside PFBC research checked → `reports/2026-11-05_PFBC_deep-research-verification.md`. Base rates rebuilt from FDIC data match its direction. Its Plaza red flag failed against DEWEY's lien figure.

- **13:06 ET:** outside Ueno report checked → `reports/2026-11-05_Ueno_deep-research-verification.md`. Corrected my Fitch 15.2% vs 10.3% misread (a restatement, not a fall). Lesson: Ueno's warning was in the audited notes, not the ratios.

- **13:32 ET, Will via PROME:** FLG review → `reports/2026-11-05_FLG_late-loan-review.md`. **I called FLG "the one that matters" off two quarters; 12 quarters showed a rebound. Pull the bank's own history before calling a jump.** Same day as the PFBC base-rate correction.

- **14:13 ET, WQ-596:** REG-31..34 registered.

- **14:25 ET, WALTER -051:** CommunityAmerica sized → `reports/2026-11-05_CommunityAmerica_35-West-Wacker_sizing.md`. See lesson 50. CYPHER vendor cluster: no consequence, not a clearance → boot REPORT §15.

- **16:05 ET, Will-asked:** read LABOR's combination watch (LABOR `CLAUDE.md` C3; CREED §6a). I recommended adopting it with three themes, review dates, unread items as leads, no backfill, and said it does not fix today's real miss, unread tables. Will closed out without answering: **NOT adopted.**

- **Skipped at close:** VLY and EGBN 10-Qs (filed today, seen 16:33 ET, unread); H.4.1 11/05 (my FRED series id failed, not retried); research retirement sweep; `consumer_check`, no registered figure superseded; NEXUS derived surfaces other than the brief unchanged, no score moved.

### EARLIER — 2026-11-03 12:06 ET, Will-launched boot, intake and write-back
- **Read:** root/desk instructions and canonical STATUS → LESSONS → CALENDAR → MEMORY → ROADMAP boot sequence; fuller `boot.py` completed rc 1 (ALERT only, no FAIL/INCOMPLETE). Runtime Kimi Code CLI, exact model/session UNKNOWN; file-based coordination available.
- **Tape:** 12:06 ET vendor quotes WAL $77.43, KRE $73.19, FLG $10.55; APO −5.58% flagged without cause attribution. Settled 11/02 (Yahoo/Nasdaq agree): WAL $78.67 (REG-T-02 FIRED, exit 0-of-3) and KRE $73.73; FLG $10.75, RED for 18 closes.
- **Credit and flow:** FRED 11/02 HY 343bp / CCC 1,319bp; REG-T-04 NOT FIRED 0-of-3, REG-T-03 exit run 0, CCC/HY 3.85× with no CCC-led escalation. Boot's vendor-derived KRE estimate was 50.58M, −2.2% vs 11/02, but the subsequent official-history review does not treat it as a confirmed daily redemption.
- **KRE official history (Will-asked):** 2025 NAV +7.41% while shares −29.45% and assets −24.22%; 2026 through 11/02 NAV +13.66%, shares −10.39%, assets +1.84%. The divergence is not new, so share contraction alone is not a directional price or bank-credit signal. Consolidated mechanics, 2025–2026 tables, rolling windows, conclusions and source-data map → `research/KRE/REDEMPTIONS.md`; linked from the KRE README, synthesis and evidence guide.
- **Intake:** general/WALTER 0; WAL/OZK unACKed 0; predictions 7 OPEN none due; corrections 0; staleness clean; no unread BOARD signal met the selection rule. Alerts were the known WAL/FLG states, FLG director buy and CFG/WAL 8-Ks. No new TERRY route.
- **Sync/work:** pull withheld on other desks' dirty tracked files; fetch showed local 4 ahead / 0 behind. Report `reports/2026-11-03_boot/REPORT.md`. No score, prediction, probability, position or trade change. Nano P&A check due 11/03 not run in this tape-only boot.

*11/02 evening entry → `archive/MEMORY_rotation_2026-11-05.md` BLOCK M15, crc32 `9a9ba72f`.*

### EARLIER — 2026-11-02 17:24 → 17:29 ET checks, Will-launched evening boot
- **Tape at 17:29 ET, vendor not settled:** WAL $78.67 (+3.12%), KRE $73.73, FLG $10.75; VIX 21.15 (+8.91%). REG-T-02 stays FIRED, exit 0-of-3 through 10/30; FLG RED; no 11/02 settled grade.
- **New CUBI Form 4 verified at SEC:** CEO Jay Sidhu sold 50,000 shares at $87.4039 [11/02, acc 0001222371-26-000011]. Insider observation only; no credit, score, threshold, prediction or trade change.
- **Intake:** general/WALTER 0; WAL/OZK unACKed 0; predictions none due; corrections 0; staleness clean. BOARD -010 BACKFILL (direct DEWEY packet already integrated). boot.py rc 1: known FLG/CFG/WAL alerts plus CUBI sale.
- **Receipt:** `reports/2026-11-02_evening-boot/REPORT.md`. Pull withheld on other desks' dirty tracked files; fetch showed 0/0. No unassigned research or external route.

*11/02 morning and midday, 11/01, 10/31 and 10/30 evening entries → `archive/MEMORY_rotation_2026-11-06.md` BLOCK M16, crc32 `c6b9b3e6`.* *10/30 09:05 ET session entry → `archive/MEMORY_rotation_2026-11-02.md` BLOCK M14, crc32 `6de3a7d5`.* *10/28 PRIOR SESSION entry → `archive/MEMORY_rotation_2026-10-30.md` BLOCK M13, crc32 `5d7d98d1`.*

### CHANGES SINCE LAST SESSION
- **Boot Fri 2026-11-06 09:55 ET, Will-launched, status only.** Claude Code, Opus 5.5, desktop `DESKTOP-BC6EF81`, session name reginald-04. Pull not run: 1 ahead (LABOR `400f6cd60`), 0 behind, other desks' dirty files. Peer list works (PROME prome-51 live). Failed connectors: definite, mtnewswire; none needed. Quartr never called.
- **Tape 09:56 ET, vendor, not settled:** WAL $75.40 (−0.65%), KRE $72.06 (−0.33%), FLG $10.42 (−1.65%), HYG $77.33, VIX 24.93, ^TNX 4.88. No settled bar newer than 11/05, so no grade or state change. KRE shares vendor read 55.36M, +2.4% vs 11/05, not a confirmed flow.
- **HY 11/05 not on FRED at 09:57 ET;** latest stays 332 [11/04], CCC 1,297.
- **Filings at SEC, 09:57 ET:** FLG and CUBI Q3 10-Qs not filed. OZK FDIC FLNG newest 10/20. VLY, EGBN, BKU 10-Qs still unread.
- **Intake:** general 4 open (unchanged, read for awareness, unprocessed); WALTER 0; WAL/OZK unACKed 0; corrections 0; predictions none due; staleness clean; BOARD 0 selected of 107 unlogged since 11/03, none dated 11/06 yet. boot.py rc 1: known alerts only (WAL, FLG ladder, FLG director buy, CFG 8-K 10/30 auditor item, inbox).
- **11/07 run readiness:** FFIEC token live here (HTTP 200, expiry 2027-01-31). `/tmp/mi3/fac` empty after the reboot, so the cache needs rebuilding. DOCKET holiday-counting row for 11/07 is already RESOLVED 10/30.
- **10:09 ET, WALTER doorbell:** cards 002, 005, 006, 007 INFO_ONLY; 010 (ACTION) LABOR freeze thesis stood down, read at LABOR's packet and card. **My TRADE.md §4 refuter 'LABOR's bull-side kill' is now met;** corrected, TERRY packeted. No score, threshold or trade change. My first BOARD note said no surface carried the old wording; a follow-up grep found TRADE.md. **Grep the bar's figure, not just the phrase, before writing 'no surface'.**

- **11:21 ET, BKU graded (CORAL packet + PROME doorbell):** 10-Q and Q2 10-Q read at SEC. Primary cell TRANSMITS, class MIXED FINAL, REG-32 FALSE, FL aggregate NO TRANSMISSION FINAL → `reports/2026-11-06_BKU_10Q_FL-frame-final.md`. Call Report RC-N closed the 'accruing' gap: RCONF179 $21,321K vs $0, multifamily and construction $0. Same line was $23.2M at 3/31. Frame defect disclosed: bar came from the unsplit aging row, accruing Q4-25 was $7.8M; grade unaffected. Cards 012 (HY 348, own FRED fetch agrees), 015 filed. HANS Arkéa packet landed, uncommitted by HANS, seen only.
- **Lesson, 11/06:** when a filing's table cannot answer a cell's qualifier, check whether another primary can before writing a limit. RC-N column A answered 'accruing' in one pull; it also exposed the frozen bar's basis.

- **11:30 ET, VLY and EGBN 10-Qs read on Will's go** → `reports/2026-11-06_VLY-EGBN_10Q_reads.md`. VLY: ~$108M block not paid off, likely modified again; my 11/01 'new' $61.4M NOO reading corrected, the line is lumpy. EGBN: MF criticized line met; deck and 10-Q disagree by $36.2M; basis gap closed; REG-28 u=4. Packets PROME, TERRY, RED.
- **Lesson, 11/06:** compare a cumulative row against the prior filing's cumulative row. The Q3 table looked clean alone; only H1-then vs H1-now exposed the $108M. And tie a pool to the Call Report before reasoning about it.

### NEXT SESSION
00. BKU, VLY and EGBN 10-Qs DONE 11/06. Then H.8 11/06, H.4.1 11/12, FLG 10-Q per review §5 if filed.
00a. **Combination watch set-up owed (WQ-622 A, `PROME/COMBINATION_WATCH.md`):** `combo:<theme>` in KB.tsv Notes, 3–9 themes, one charter line, theme list in the next delivery packet. Mine: late loans outside the 14; bank-vendor breaches; bank lending to private credit.
00b. **General inbox, seen 11/06, not processed:** PROME WQ-624 A (encode side list at the 11/07 run). HOMER: cite Trepp multifamily 8.09% [Oct] only with the Cove at Tiburon caveat, no boot surface carries it now. GIBBS: send file and line when cohort 10-Q reads land ~11/14, it re-tags 42 rows. CARL: ALLY and RITM notes, no ask; co-owner of the 11/06 docket row, bank-side read mine. **M&T Wilmington Trust sizing (WALTER 067): read the Q3 10-Q note with WAL.**
0. **FFIEC short list COMPLETE 11/05** (138 of 138). FDIC full screen ~mid/late Nov gives the frozen verdict. REG-06 EDGAR scan DONE 10/31 (none; next 11/30). **Re-check at each touch: VLY at the 12/31 Call Report: K161+K162 flat again or a real exit (report 11/06 §3); BKU at the 12/31 Call Report: does RCONF179 $21.3M roll into F181/F183 (report §4); OZK at FDIC FLNG (never EDGAR).**
1. **Four carried releases READ 11/02:** CCB Q3, H.4.1 10/29, H.8 10/30 and FHLB Q3 Highlights → `reports/2026-11-02_carried-release-reads/REPORT.md`. Next H.4.1 11/05 / H.8 11/06 (descriptive only; 'deposits down' tell RETRACTED, deep dive §10). CCB 10-Q partner/recourse notes pending. REG-T-06 grades 11/13 from the CFR. Per-bank borrowing screen FROZEN (`reports/2026-10-28_borrowing-screen_FROZEN_rule.md`, sha256 `90e0a4a2…948a`); run once FDIC posts Q3 (~mid/late Nov).
2. **DAEDALUS 10/30 packets: DRAINED 10/31** (reply sent; deferred items carry dates 11/07 · 11/14 · 11/20 in the reply). Prior text: item 1 DONE 10/30 eve (reply with it). Items 2–4 decide L5: VX.tsv 14 stale LIVE rows (3 contradict STATUS) · OZK 37.6% dead-figure notes (bank-side HY report :122 + one more) · POSITIONS.md lacks Nov 66P/67P/68P/70P legs (collapse stacked headers). Then disposition 5–14 + A1–A3 (DONE / DEFERRED with date / DECLINED with reason) in one reply to `AGENTS/DAEDALUS/inbox/`. Charter trim (item 5) is MINE, no Will word (PROME, DOCKET L889). `V1V3-ACCELERATE` rename: coordinate with WALTER per `registry/NOTES.md` or re-date. read_cap rc 1 is NOT mine to clear (DAEDALUS tool, 11/04).
3. **REG-06:** 10/31 scan DONE (none). Next scan Mon 11/30 (424B, S-1/S-3/S-4, 8-K 3.02).
4. **HY:** grade each FRED print for the REG-T-03 exit run (≤300 ×5; 332 [11/04], run 0). REG-T-04 stays NOT FIRED (strict >350 ×3; latest 18bp below, run 0-of-3); 11/05 print is the first to carry that day's selling. CCC/HY 3.91× [11/04]; escalate only on a CCC-led re-cross. B back above 330 since 10/29. REG-T-02 log: graded through 11/05 ($75.88, run 0-of-3); next row = 11/06 settled close.
5. **Pathward release READ 11/05.** **PFBC Q3 10-Q at FDIC most likely Mon 11/9.** GDOT Q3 not filed. WAL 10-Q cohort items logged for me (hotel franchise criticized $75M → $185M, OREO 22 → 27 properties) → read at the 11/07 run.
6. **JWT renewed 11/01 (expiry 2027-01-31; live on the desktop, own pull 11/05).** 11/07: also run the Friedberg like-for-like plan (report 2026-11-01 §4; needs the 9/30 universe file), fix the step detector's round-before-compare (EGBN 6/30 miss) with a boundary fixture, read HBAN Q3 10-Q for the M3 step. **+PROME 11/02: reserve-release breadth count (nonaccrual up AND allowance down, 6/30→9/30, with 3/31→6/30 beside; mods-up/30–89-down where clean) → CALENDAR 11/07 row (d)–(f).** 11/07: verify sha256 `06e37edad2d583074a20f0ca70d0f84079a3eed95fba891204060662bcd00672` of the frozen ranking protocol, decide the cohort-selection question, then run.
7. **10-Qs, early Nov:** SBCF primary cells (CRE+constr 30-89, nonaccrual, resi) and the $8.4M VBI loan · SSB/BKU cells → FL aggregate final ~11/14 · FLG MF special mention and modifications · EGBN MF criticized table and REG-28 maturities · **VLY 10-Q (~11/6–11/9): the six asks in report 2026-11-01 §1d** (mod payment-defaults, NOO 30–89 $61.4M identity, $30.1M construction collateral, ACL roll-forward, $18.5M NDFI borrower type, criticized by class).
8. **Nano:** P&A posted 11/05, schedules redacted; weekly check closed. Next evidence L515 sale, L517, Fed OIG ~3/25/27. Records request is Will's call, not recommended.
9. **Carried:** CUBI N at 11/07.
10. **By 11/20, with the charter trim:** re-validate the reading copy for BOARD/SIG-W-20260619-008 (39,509 B; its class-row member exception is past its review date, the cause of read_cap rc 1; PROME 11/05 says this is mine) and re-attest READS.

**CARRIED LESSONS — behaviour, not record.** *Newest first. Aging rule (9/02): full entry → one-line rule AND the full text goes to `archive/` verbatim + crc in the same pass. ⛔ Never age a lesson by deletion (the 12-21 compressions archived nothing; git history only). Preamble → BLOCK M7, crc32 `8028ecb4`.*
50. **[11/05] I wrote a loss table into the CommunityAmerica sizing before computing it, and three of four ratios matched no calculation; the packet carried one. I also measured against the 7% line without checking which capital regime applied: the 5300 showed the credit union opted into the 9% leverage framework.** A follow-up check, not the first write, caught both.
   - ⇒ **Compute, then write: every derived figure comes from a command run before the sentence exists** (`finding_attribution_authenticates_a_figure_its_named_source_never_produced`). **Before calling a line the line, read which rule the filer is under.**
49. **[10/21, found 10/28 via BROCK] I recorded CFG $12.852B vs $14.727B as 'both June 30 endpoints, not growth' without opening the smaller figure's period-end. It was March 31. My own 10/16 report had already named Q1 as the likely vintage.**
   - ⇒ **Two different figures for one line item are a VINTAGE question before they are a scope question: read each figure's period-end at its source, and grep my own reports, before naming the cause.**
48. **[10/22] I committed 32 `git mv` renames with a pathspec built from `git diff --cached --name-only`, which lists only the NEW name of each rename. The commit added the archive copies and left the old-path deletions staged, so both copies sat on origin for about a minute (f984ce53c, fixed dbfbfc2bd).**
   - ⇒ **For a pathspec commit of renames, pass both paths: `--name-only --diff-filter=D` plus the new paths, or `git diff --cached --name-status` and take both columns. Then `git status --porcelain -- <dir>` must be empty before push.**
47. **[10/10 eve] In a SendMessage to PROME I typed a commit reference ("ab9b-REGINALD") that no command had printed; I sent the real hash (`8d31de2aa`) one message later.** The same session I keyed two FHLBank CIKs from memory (1325878 = Topeka, 1316220 = CAPE Holding); the filer-name check caught both before use.
   - ⇒ **An identifier (hash, CIK, accession) goes into a message only from a command's output in the same turn; a CIK is used only after the response names the intended filer** (lesson 43; `finding_attribution_authenticates_a_figure_its_named_source_never_produced`).
46. **[10/10 late PM] I sent "largest 3-week rise in 160 weeks" to WALTER, STATUS and Will. The 160-week window began 9/13/2023, just AFTER SVB, whose first week alone was ~9× the move.** I had also measured from a 9/09 trough (+11.7% vs +5.9% month-end to month-end). Both were true, and both made it look bigger.
   - ⇒ **A base-rate window must include the episode that defines the scale (here 2023), or name what it leaves out. Quote the change from a neutral base (month-end), not from the trough.**
45. **[10/10 PM] I told Will "the regionals were flat, so this isn't regional stress" from a 6/30 quarterly print, and checked the weekly H.8 only when he asked whether newer data existed.** It showed small-bank borrowings +11.7% in the three weeks to 9/30, the 160-week max. Same day: my own 9/11 receipt had written "Brier on 55%" against WQ-112(i), ratified ten days before it.
   - ⇒ **Before a "this is not happening" read built on a quarterly print, pull the fastest proxy that could contradict it, and date both.**
   - ⇒ **Before writing a scoring rule into a receipt, read the ratified canon (`FORGE/PREDICTION_DISCIPLINE.md`), not the asking packet's framing.**
44. **[10/10] I turned "I can't see deterioration" into "I expect stabilisation," and called the earnings outlook "mixed" without an expectations baseline.** "Mixed" was the expected result of my own test lines, not results against consensus.
   - ⇒ **Not seeing deterioration is not a forecast.** A relief or decline call needs positive evidence plus the market's expectations baseline.
   - **Alarm levels are confirmations, not preconditions.**
   - **Don't swap one unsupported direction for the opposite one.**
43. **[10/9] My 8-K monitor checked VLY under SEC CIK 74260, which is OLD REPUBLIC INTERNATIONAL, and checked OZK at the SEC, where OZK has not filed since 2017.**
   - **Neither could ever look wrong:** a valid feed for the wrong company, and an empty feed for a non-filer, both read as "no 8-K".
   - **Found at the evening boot, not by any check.**
   - ⇒ **An instrument keyed by an identifier must verify the response NAMES the intended entity, and must treat "nothing ever filed here" as a broken route, not a quiet bank.** `finding_instrument_reports_clean_against_the_wrong_reference`.
41. **[10/7] I pre-registered an expiry as 'lapse worthless, decision-free — no roll' (KRE $60P Sep-30). Will sold and rolled it the next day.** His standing practice (USER.md, 9/30) is to sell or roll before expiry. ⇒ **An expiry pre-registration carries a sell-or-roll branch, never a lapse branch, and the write-back reads the broker record, not my forecast.**
42. **[10/7] A Call-Report deposit cost (interest ÷ RC-K average) reproduced the company figure at 3 of 6 banks and was off by 30–60bp at the other 3.** I had built it as the 'one comparable basis'. ⇒ **Check a derived cross-bank measure against each bank's own figure BEFORE using it as the comparable column; the basis that looks cleaner is not the one that is true.**
40. **[9/27] I adopted a peer's 'correction' (CREED's FLG 17.5%) without re-running it, and it was wrong: it added the charge-offs to a denominator that already contained them. My own evidence pack labelled $2,088M as pre-charge-off.** The FLG desk caught it a day later. ⇒ **A correction to my figure gets the same recompute as the figure itself, before I write 'Accepted'** (`finding_a_correction_pass_is_unreviewed_work`). Same session: I told Will PFBC was unchecked against its filings when my own morning report had its Call Report. **Grep my own reports before describing what I have.**
39. **[9/27] A KB fact sourced from an LLM research pass sat INVERTED for 7 months: `ML-REG-044` said 'Fed C&D March 4, 2025'. The date was the Issuu UPLOAD date of the Fed documents, and March 2025 was the order's TERMINATION.** Caught by a peer desk (WAL), not by me. ⇒ **A regulatory action is cited from the regulator's own record (Fed enforcement CSV / agency release), never from a host that re-posts it; a date on a re-host is the host's date until proven otherwise.** Full evidence → `reports/2026-09-27_nano-banc_legal-leg.md` §1.
38. [9/24] Before an inference about a peer's name leaves my desk, read the primary it rests on or label it `INFERENCE FROM SECONDARY`; a brief compresses — check each compressed claim against its own data before sending (three CATO catches in one brief). Full text → BLOCK M6, crc32 `037ca359`.
37. [9/11] A claim about a PEER's ledger stays SEARCH-NOT-FOUND until you open the owner-declared path; assert a peer's STATE from their FILE, never from packet memory.
36. [9/2] A path in my prompt is a claim about the filesystem: resolve symlinks, and `git ls-files --error-unmatch` before claiming an artifact exists. 36-37 full text → `archive/MEMORY_rotation_2026-09-24c.md`.
35. [9/2] A ruling must ship with its retroactive sweep in the SAME commit; sweep by the SHAPE of the thing (a regex), not the value being retired — a supersession marker hides the prior vintage from a token grep.
34. [9/2] A source name authenticates a figure like an exact level does; asked for a construction you never built, return the NEGATIVE WITH EVIDENCE (schema, columns, n=) — silence reads as latency.
33. [8/28] Self-audit before handoff is a fleet standard — measure whether YOU do it on findings you offer.
32. [8/28] Before proposing a threshold, check which DIRECTION it trips and that the level and sign agree — a kill can be sign-inverted as easily as a confirm.
*Lessons 12-31 are indexed in `archive/MEMORY_rotation_2026-09-24d.md` (which points on to their verbatim archives: `MEMORY_carried_lessons_27-31` crc `05486924`, `…22-26` crc `9148add8`; 12-21 in git history).*
*32-35 aged 2026-09-24 to one-line rules (above); full text + the 8/27 housekeeping flags → `archive/MEMORY_rotation_2026-09-24b.md`.*

*CHANGES SINCE is populated at the next market boot; this cleanup does not invent a fresh observation.*
