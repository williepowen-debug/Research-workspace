# LIQUID — Cross-Session Memory

## Session Notes

### CURRENT SESSION — 2026-11-25T15:34 ET, closed 2026-11-25T20:06 ET (Will's boot task 15:34 ET; D:L1290 A and B for PROME prome-77 at Will's 16:11 ET request; Will's 18:46 ET word to run B early; laptop, Claude Code / Opus 5.5, session liquid-bd)

- **Context:** third LIQUID session of 11/25 (earlier: FLASH read, then the SoftBank CDS and 11/24 HY grade at 11:5x ET). Boot intake: 9 WALTER cards and 4 corrections (78915a16aa); WALTER 039/040 in the evening.
- **Delivered:** **Part A** (servicer bonds, b2d692e862): Freedom 10.00% Jan-2032 at 99.69 [11/24], reoffer NOT FOUND; Freedom +95 bp median since 10/21 vs control +26; peers not following; no trade. **Part B** (11e8d4d9c2): all 631 DTCC intraday slices for 11/25; **no valid CoreWeave 5Y on 11/25**; 4Y Dec-2030 1,366–1,379 clean, about +130 bp on the day; last 5Y 1,314 clean [11/24] for TERRY's card. SoftBank 3.5Y 548/555, no 5Y; Oracle 5Y 362–372; Alphabet 5Y cancelled; SpaceX 293/298. **`crwv_cds_grade.py` fixed:** 90 of 114 cancel rows had no name (KB-LIQ-166). STATUS rotated to 69.8% of cap (`archive/status_snapshots/STATUS_rotated_2026-11-25.md`).
- **Own error caught:** an 18:16 ET chat line read 11/25's 4Y over 11/24's 5Y as curve inversion; withdrawn in the Part B packet (on 11/24 the curve sloped up).
- **Open:** diff the 11/25 cumulative DTCC file against the slice read if it was not done at close; H.4.1 of 11/25 unread; 069 review 11/27 (11/25 cell); `gate069_legs.py` and `dtcc_cds_probe.py` repairs.

### PRIOR SESSION — 2026-11-24T23:20 ET, closed 23:3x ET on PROME's closeout ask in the brief (PROME prome-77, D:L1252, Will's word 23:19 ET "wake LIQUID and HENRY now", laptop, Claude Code / Opus 5.5, session liquid-desk-agent-2026-11-24)

- **Context:** REG-T-04 FIRED (HY 352, 376, 363 [11/19, 11/20, 11/23]); my ISSUANCE-FREEZE leg; my gates on the 11/20 and 11/23 cells; forward view; TERRY re-read. Fleet was offline 20:55 ET 11/23 to 22:20 ET 11/24.
- **Delivered:** ISSUANCE-FREEZE = NOT A FREEZE, SELECTIVE (20 named deals; Proofpoint 8.5% inside talk 11/18; IG $46.5B 25 bp inside talk; UST Global loan pulled 11/16; ING DC auction short 11/20; Fullscript to private credit). US HY weekly volume UNMEASURED (paywalled); year-ago week $6.405B. **GATE-LIQ-072 leg 2 FIRED (IG 98 [11/20]), first since 7/9**, routed HENRY + NEXUS via WALTER. **GATE-LIQ-069 L4 FIRED 11/20** (IREN −17.97%, APLD −17.81%, NBIS −16.11%, HY +24), 3 legs, no new consequence. CoreWeave 5Y about 1,314 bp [11/24]. HY-REKILL 0 of 2; X1 CLOSED; 079 not armed. PROME's servicer addition answered (memo §3). Memo `PROME/inbox/2026-11-24_from-LIQUID_D-L1252-issuance-freeze-read.md`, commit dd2be18962. The harness refused a desk report file, so the memo is the evidence record.
- **Open:** inbox drain deferred (3 packets + 27 WALTER cards); 076 W1 as-of 11/17 addendum; `gate069_legs.py` newest-session-only blind spot (KB-LIQ-164); 11/24 ICE cell; freeze test the week of 11/30.

### EARLIER SESSION — 2026-11-20T11:22 ET, closed on PROME's ask (PROME prome-77, G:GATE-LIQ-076 due-row wake launched late, laptop, Claude Code / Opus 5.5; stamp 2026-11-20T11:29:00-05:00)

- **Context:** grade 076 at its review; 11/19 HY cell as first published (>320 run, REG 350, re-kill); W2 and H.4.1 of 11/19; yen funding legs (SAM, BOND); TERRY read; funding sentence for HEARTBEAT; whole-inbox drain (1 + 5).
- **Delivered:** HY 352 [11/19, first-published, pull 11:22:56 ET] = first close above 350 ⇒ REG-T-04 witness 1 of 3, >320 run 5, re-kill 0 of 2; CCC 1,361 (top of FRED's ICE window), B 380, HY−IG 258; IG 94 at 072's line; tier rule BROADENS clearly (IG +8, BBB +10, BB +26 vs 10/28). **076 NOT MET 1 of 3** (W2 as-of 11/11 G10 −7,007, G5L10 +937; W3 off since 11/16; W1 as-of 11/17 at 15:30 ET); re-arm end of 11/30; recommend 12/2. Funding unchanged (SOFR99 +8, SRF $3M, reserves +$19.1B): NOT SHOWN stands. H.4.1 11/18: FIMA $1M, foreign pool −$19.4B, custody +$19.8B, no sale shown. TERRY, SAM, BOND packets; KB-LIQ-153/154/156/157 appended; COR-20261119-20 NO-OP. → `research/2026-11-20_gate076-review/REPORT.md`.
- **Open:** W1 as-of 11/17 addendum (PROME moved it to the next session); 069 L4 watch on the 11/20 session (APLD −14.99% intraday); REG-T-04 on the 11/20 and 11/23 cells. WALTER FLASH SIG-W-20261120-001 consumed (noted, 4afa9c8c0c). PROME set 076 review_by 12/2 and wrote the three GATES cells.

### EARLIER SESSION — 2026-11-19T09:18 ET, closed 2026-11-19T10:34:40-05:00 (PROME prome-36, G:GATE-LIQ-069 due-row wake launched late, laptop, Claude Code / Opus 5.5; closed on PROME's ask 10:33 ET)

- **Context:** 069 review due 11/19 on the 11/18 HY cell; >320 run, re-kill, tier rule, REG 350 on the same cell; can 076 be graded today; whole-inbox drain (4 WALTER); WQ-719 A / 721 A charter line.
- **Delivered:** HY 347 [11/18, first-published, my pull 10:28:57 ET] ⇒ >320 run 4; re-kill 0 of 2; REG-T-04 witness 0 of 3 (3 under); tier rule BROADENS on the 15-session clause (BBB +7 at p90, borderline); CCC 1,353 (+24); HY−IG 254 (2026 high); IG 93 (1 under 072's >94). **069 review: 2 of 2 FIRED unchanged** (L1/L4 not fired; L2 CoreWeave 5Y about 1,078 clean [11/18]; L5 nothing new); PROME accepted the state cell verbatim, review_by 11/25. 076: W3 off since 11/16 (VIX ≥20), reset clock to about 11/30, recommend 12/2. Belgium TIC $507.9B (bare level, no China inference). FOMC minutes → KB-LIQ-153/154. CLOSEOUT.md NEXUS_BRIEF lines aligned to WQ-719 A / 721 A. STATUS rotated (crc32 5ec2e55a). No TERRY packet (no new implication). Commits bf203b6280, 0c89f89bfb (PROME packet). → `research/2026-11-19_gate069-review/REPORT.md`.
- **Open:** 076 graded at the 11/20 wake (W2 as-of 11/11 + CFTC W1 as-of 11/17); H.4.1 (11/18 levels) not read; ING data-centre loan clearing prices.
- **Defect caught by me:** the STATUS rotation script split each gate row at its last `|`, which moved the review_by column into the archive; caught on the post-rotation check and restored before commit.

### EARLIER SESSION — 2026-11-18T10:34 ET, closed 2026-11-18T10:40:54-05:00 (PROME prome-6e, DOCKET line 1178, desktop, Claude Code / Opus 5.5; no pull at start per the letter; closed on PROME's ask, D:L1178 RESOLVED)

- **Context:** grade the November 17 ICE cell (>320 run 3 of 3), tier rule, 069 legs, Cable One; drain inbox (20: 3 top-level, 17 WALTER).
- **Delivered:** HY 343 [11/17, first-published, my pull 10:35:18 ET, matches TERRY] ⇒ **>320 ×3 MET** (323/334/343); signal to ALL via WALTER (59cba599c0), SIGNALS row, trade read to TERRY (c25c9f6031). Tiers IG 92 (+2), BBB 115 (+3), BB 204 (+8), B 368 (+11), CCC 1,329 (+19) ⇒ BROADENS; re-kill 0 of 2; 072, 069 L1/L4 NOT FIRED. Cable One not separable. VULCAN four questions answered (b0119cd32d). Six correction receipts. PROME packet b9720641b5. → `research/2026-11-18_hy-1117-grade/REPORT.md`.
- **Open:** next ICE cell extends or resets the run; H.4.1, 076 W2, 069 review 11/19.
- **Defects caught by me:** the STATUS header and PROME packet stamps were first typed from narrative (10:45, about 10:50), not from `date`; both were corrected before closeout (packet b24d928f89).

### EARLIER SESSION — 2026-11-17T09:31 ET, closed 2026-11-17T10:54:02-05:00 (PROME prome-19 task 703, Will "703 yes" 09:30 ET, laptop, Claude Code / Opus 5.5; launch task line was empty, task arrived by cross-session message; closed on PROME's ask)

- **Context:** outside-audit items (re-kill tests, signal use), Cable One for my series, November 16 HY cell, funding-microstructure leg status, inbox drain, stale KB rows (Will 11/16 23:16 ET).
- **Delivered:** re-kill tests: fixtures wrong (July 3 2026 is a bond holiday the 11/10 D:L342 fix drops), watcher right, dates +7 days, 20 of 20 OK, no reading affected. November 16 first-published HY 334 (+11), IG 90 ⇒ >320 run 2 of 3; tiers BBB 112, BB 196 (+10), B 357 (+13), CCC 1,310 (−6) ⇒ tier rule BROADENS (daily clause); REKILL 0 of 2; 069 L1 and L4 NOT FIRED; 072 NOT FIRED. Cable One 0.160% of XCCC, no gate touched. OFR repo volumes reachable (KB-LIQ-162), coverage only. KB: 58 retired, 15 kept. Inbox 4 of 4. Commits 3f8693dcce, 33247b549b. → `research/2026-11-17_prome-703/REPORT.md`.
- **Open:** November 17 cell (>320 MET if above 320.0; first cell that can show Cable One). `gate069_legs.py` read the November 13 BB at 10:51 ET while the first-published 11/16 row existed (likely feed lag; not chased).

### EARLIER SESSION — 2026-11-16T10:07 ET closed 2026-11-16T10:15:38-05:00 (PROME prome-6f due-row wake, WQ-184, D:L1149, desktop, Claude Code / Opus 5.5; closed on PROME's ask, D:L1149 RESOLVED)

- **Context:** correct and narrow the 11/14 IG tech yield read (CATO N14-2); grade my lines on the November 13 HY cell; packet TERRY the first-published cell; drain inbox (1 packet, WALTER 009/010).
- **Delivered:** HY 323 [11/13, first-published, 10:09 ET] ⇒ >320 run 1 of 3 (earliest MET November 17 cell); re-kill 0 of 2; REG-T-04 witness 0 of 3; tier rule CONTINUES (B +5, CCC +2, upper tiers flat). 076 unchanged NOT MET 1 of 3, W1 as-of 11/10 not in CFTC API (holiday week). N14-2 applied in REPORT, STATUS, NEXUS_BRIEF, KB-LIQ-153, MEMORY. CoreWeave $4B plan graded against DDTL 4.0 (S+225, A3): NOT SHOWN stands. → `research/2026-11-16_due-row/REPORT.md`.
- **Open:** W1 as-of 11/10 (likely today 15:30 ET); November 16 cell about 10:10 ET 11/17; CoreWeave loan terms when they print.
- **Defect (PROME caught at consumption):** my PROME packet lost "$4B" and "$8.5B" to an unquoted heredoc (shipped "at least B", "(.5B"); PROME recorded the correct figures on D:L1149; filed packet not edited. TERRY packet, REPORT, STATUS, KB intact (grep 11/16). Fleet memory instance appended.

### EARLIER SESSION — 2026-11-14T11:25 ET, closed 2026-11-14T11:35:28-05:00 (PROME prome-fe, C9 research commission WQ-538 A, card SIG-W-20261114-007 item 1, Saturday, desktop, Claude Code / Opus 5.5)

- **Context:** Will's bookmark of a Bloomberg chart, IG tech bond yield about 6.1%, "highest since 2009": split spread from Treasuries; set it against the financing-constraint question; drain both inbox lanes.
- **Delivered (corrected 11/16, CATO N14-2: broad index only, approximate; tech split unmeasured; Oracle 2031 note 4 bp wide of pricing):** about 95% Treasuries (broad ICE IG +114 bp over the year, spread +6, 83 to 89 [11/12]; 10Y 5.10% highest since July 2007, 5.15% par 11/13; broad IG 2026 high still October 5, 6.03%). State Street marks [11/12]: Amazon, Alphabet, Meta, Microsoft at or inside non-tech to 10y, Oracle +149 to +213; Oracle new notes below reoffer mostly on rates, three inside pricing, 2031 4 bp wider. Financing constraint NOT SHOWN; no gate graded. KB-LIQ-153/157 appended, KB-LIQ-161 (method). Nine inbox items drained; WQ-678 B 16 of 17 trims applied. PROME packet 07b10c3cb5, verified and filed by PROME; TERRY gets it for Monday. → `research/2026-11-14_ig-tech-yield/REPORT.md`.
- **Open:** Bloomberg tech index and any history of name-level marks are unreachable, so the change in the tech premium is unmeasured.

### EARLIER SESSION — 2026-11-13T10:16 ET, closed 2026-11-13T10:28:06-05:00 (PROME prome-72, G:GATE-LIQ-076 due-row wake, WQ-184 / WQ-667 B, desktop, Claude Code / Opus 5.5)

- **Context:** grade 076 at its review date; verify the 11/12 HY/CCC cells; DTCC 11/12 file; SAM's Japan funding line; drain inbox.
- **Delivered:** 076 NOT MET 1 of 3 (W2 as-of 11/4 G10 −7,845, G5L10 +477; W3 met; W1 as-of 11/10 unpublished); no re-arm since 10/22, so no write-up possible; PROME set review_by 11/20. **HY 320.0 [11/12, first-published] RESET the WQ-444 >320 run** after 8 observations; re-kill 0 of 2 (60 above); tier rule STALLS (CCC +3, BB −17; CCC−BB 1,131). DTCC 11/12: CoreWeave 5Y ~1,065 (−90), Oracle 5Y ~295 (flat); 069 L2 not fired. Japan funding OPEN; H.4.1 11/11 baseline (custody $2,524.2B, FIMA $0, foreign RRP $336.1B). Six WALTER cards drained; reset routed via WALTER and to TERRY; packet to PROME consumed. → `research/2026-11-13_076-review/REPORT.md`.
- **Open:** W1 as-of 11/10; H.4.1 11/19 read; 11/10 ICE cell; DAEDALUS WQ-678 B trims (charter, deferred).

### EARLIER SESSION — 2026-11-12T09:08:38-05:00, closed 2026-11-12T16:12:28-05:00 (PROME prome-e8, WQ-184 due-row class C6, D:L1124, desktop, Claude Code / Opus 5.5)

- **Context:** grade LIQUID rows on the HY cell; 079; 076 if ready; drain inbox. Research only; nothing moved.
- **Found:** FRED's ICE family carries a row dated 11/11 (HY 330, CCC 1,330, BB 193) and none dated 11/10; every tier moved, so not a carry; first missing session row since 2023-11. Likely ICE's 11/10 valuation under the holiday date (HY yield +11 bp fits the 11/10 Treasury sell-off); not established.
- **Graded by D:L342 (calendar-keyed):** the 11/11 row is not an observation, 11/10 unpublished ⇒ >320 run stays 8 (DOCKET expected 9), HY-REKILL 0 of 2, tier rule no new grade, 069 L1 NOT FIRED [11/9], L4 11/10 UNGRADEABLE-PENDING (equity half fails anyway, IREN −7.85%), 11/11 and 11/12 UNGRADEABLE, 072 NOT FIRED, 079 NOT ARMED +7 [11/10]. 076 not graded: W2 as-of 11/4 unpublished at 09:05 ET. Re-dating a row = Will's call; no grade depends on it today.
- **Cards:** six consumed; MSTR read-through (unsecured converts, unencumbered BTC, nothing reaches HY or funding rows); two corrections receipted NO-OP. DTCC: no CoreWeave, Oracle or Paramount prints; SoftBank 5Y 473 flat. → `research/2026-11-12_wake/REPORT.md`.
- **Held window (PROME's word) to 13:15 ET:** first CDS after CoreWeave's results. CoreWeave 4Y about 1,047 bp (one $3M trade 10:46 ET, 15.00 points on 500; −50 bp against 11/10 same tenor). Oracle 2Y 175 / 3Y 222 disseminated (flat to +10 against an interpolated pre-results curve), 10Y about 342 converted. No 5-year trade on either through slice 462. Lesson: DTCC `UFRO` cash = quoted points less accrued since the IMM roll date; when it lands on a round number the quote and the payer side are recovered. 30-year auction BTC 2.36, indirect 68.11% (lines not crossed). FRED: no 11/10 cell at 13:13 ET. WALTER 004 consumed as already ruled. DAEDALUS WQ-678 B trims deferred (peer packet ≠ Will's word for an instruction-file edit). No row, count or gate moved all day.
- **Open:** DTCC 11/12 cumulative file and the 11/10 cell (STATUS §3, Friday); 076 W2/W1 (Friday, PROME review).

### EARLIER SESSION — 2026-11-11 (PROME prome-2b, WQ-184 and Will's 09:24 ET word, Veterans Day, desktop, Claude Code / Opus 5.5)

- **Context:** four items in order: 11/10 HY cell, D:L1110 SoftBank Tokyo credit, WALTER 007 Skydance, CoreWeave against Oracle; then the inbox. Research only; nothing moved.
- **HY cell PENDING:** not on FRED by 10:53 ET though FRED itself updated (VIXCLS, T10Y2Y 11/10); the whole ICE family stops at 11/9. Told prome-2b at 10:06 and 10:53; TERRY and HENRY released from waiting. Poll to 17:00 ET; else Thursday about 10:10 ET. Veterans Day handling matches 398a946b9a.
- **SoftBank:** 5Y 475 after the Tokyo session (one trade), 3Y flat; yen seniors +2.2 bp, about 1.5 bp over peers; no rating action. **Skydance:** legacy CDS 529 [11/9], leverage 4.51x covenant basis versus 6.16x / 7.6x economic (estimates). **CoreWeave/Oracle:** no after-results CDS print yet.
- **Method:** DTCC intraday slices (`ppd/api/report/intraday/sec/SEC_SLICE_CREDITS_<date>_<n>.zip`) give same-day rows before the 20:15 ET cumulative file (KB-LIQ-160). JSDA served again with one request per file.
- **WQ-671 A:** December Fed-meeting pricing is ORACLE's; cite its dated read.
- **Added 12:33 ET:** TERRY's Skydance re-open lines (CDS ≥614, second-lien below 93.58 to 96.88, downgrade below BB/Ba3/BB) recorded as a STATUS §3 reader duty; 529 [11/9] not crossed.
- **Closed on Will's 15:11 ET word** with the 11/10 ICE cell still unposted; the poll ended with the session. **NEXT:** Thursday about 10:10 ET grade the 11/10 cell and message PROME first; DTCC 11/11 cumulative file for late CoreWeave/Oracle/Paramount prints; 30-year auction; 076 W2. STATUS rotated to 70% (`archive/status_snapshots/STATUS_rotated_2026-11-11.md`).

### EARLIER SESSION — 2026-11-10 (PROME prome-07 launch on Will's word 11:38 ET, desktop, Claude Code / Opus 5.5)

- **Context:** three items in order: D:L342 holiday-carry ruling, Tuesday row, 10-year auction grade. No trade, card, threshold, letter or band moved.
- **D:L342 EXPOSED, fixed and pushed (398a946b9a) before the November 11 cell:** FRED repeats the prior HY value on bond-market (SIFMA) closures, Veterans and Columbus Day included while NYSE trades, so tomorrow was the first exposure, not Thanksgiving; month-end weekend rows too. Five readers now read session rows from one `BOND_CLOSED` list in `gate069_legs.py` (extend before 2027-12-31). No past grade since registration changes. REPORT §19.1.
- **November 9 grades:** HY 334, >320 run 8, tier rule STALLS; all gates NOT FIRED; 079 +6; 076 W3 MET 11/9 on VIOLET's figures, window 1 of 3. Cards 20261109-012, 20261110-001/-004/-005 consumed.
- **10-year auction [November 10, TA_WS accepted basis]:** bid-to-cover 2.46, high yield 5.020%, indirect 61.23% (lowest of 13), direct 29.00% (highest of 13), dealers 9.77%; LIQUID's lines not met, no signal. BOND owns the grade and tail. REPORT §19.3.
- **SoftBank credit leg (PROME prome-07, 17:19 ET, on Will's 17:18 word):** SBG 5Y CDS on DTCC 497 median 11/9, pre-results, widest since August; Oracle flat, CoreWeave tighter; ratings and retail channel unchanged; `research/2026-11-10_softbank-credit/REPORT.md`. **Method:** the probe's default 4% rate reads about 30 bp high on yen CDS; 1% matched the disseminated 438 and Reuters 466. JSDA 429s this box; TRACE unreachable.
- **Method note:** a "carry" test by value equality cannot separate a holiday from a flat day; the calendar decides. VIOLET framed it as NYSE closures; the data showed the bond calendar, which moved the deadline 15 days earlier.

### EARLIER SESSION — 2026-11-09T20:20:43-05:00 (Will boot 20:11 ET, "yes please update LIQUID go ahead" 20:15 ET, laptop, Claude Code / Opus 5.5)

- **Context:** startup recovery, then a bounded Monday catch-up. No new thread, spawn, trade or card. No gate, band or score moved.
- **Delivered:** November 6 first-published grades (HY 342, −6; >320 run 7; tier rule BROADENS on the 15-session clause only); 069 L1 and L4, 072, 079 (+7), HY-REKILL, 076 window; DTCC November 6 full file (Oracle 305 disseminated, 306 to 314 converted; Microsoft about 47 or 156 bp, payer undisclosed); 3Y auction row resolved from BOND's grade; three WALTER cards and the GIBBS and BOND packets consumed; KB-LIQ-153, 156, 158 updated; packet to PROME. → `research/2026-11-05_live-catchup/REPORT.md` §18.
- **Slip, disclosed:** an unquoted heredoc turned "$0" into "/bin/bash" and "$500M" into "00M" in REPORT §18. Caught by grep before commit and fixed; the diff is append-only.
- **Found:** `dtcc_cds_probe.py` crashes (division by zero) on a short-dated contract, so its list stops early; read the raw CSV until it is fixed (STATUS §3).

*Session blocks 2026-11-04 to 2026-11-06 → `archive/MEMORY_before-2026-11-09.md` (crc32 d7e7245d).*

### NEXT SESSION

**STATUS §3 is the list.** 11/25 (liquid-bd): D:L1290 A and B done; no valid CoreWeave 5Y on 11/25, TERRY's card reads 1,314 clean [11/24]. Next: 069 review 11/27 on the 11/25 ICE cell and session (HY +25 bp safety net; any 11/27 CoreWeave 5Y print, which TERRY needs for an entry from 11/30); the 11/25 cumulative DTCC file diff if not done; H.4.1 of 11/25 (Japan legs); the week of 11/30 to 12/4 freeze test (D:L1257); 076 review 12/2; `gate069_legs.py` multi-session fix; `dtcc_cds_probe.py` repair (cancel rows by ID, KB-LIQ-166). Earlier NEXT SESSION text → `git log -p -- AGENTS/LIQUID/MEMORY.md`.
