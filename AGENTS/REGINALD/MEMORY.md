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

### LAST SESSION — 2026-10-30 17:25 → 19:07 ET (`date`), Will-launched: boot, status report, then DAEDALUS-review follow-ups and thresholds.py fix
- **Boot/status only** (Will: no unassigned work). Tape 10/30 vendor quotes, not settled: WAL $76.29, KRE $72.01, FLG $10.51, VIX 19.42 (+12.9%). New 8-Ks 10/30: CFG 4.01 auditor Deloitte → PwC after FY2026, no disagreements (acc 0001193125-26-441754); WAL 8.01 dividend $0.46 (acc 0001628280-26-068622; prior rate NOT compared).
- **Intake:** WALTER 2 INFO_ONLY (SLRK claim closed, outside cohort; RC-B read offered to Will, not started) `56aa57c85`; WAL channel ACK no-change `63ec034ac`. WAL 🔴 Q3 10-Q packet verified at WAL's grade file → STATUS exit-rail WAL row NOT FIRED, FINAL for Q3 (NCO 0.30%, no fraud) `82030c0e7`. KRE $68P Nov-27 ×10 on TRADE §2 (held per PROME; card/owner UNKNOWN).
- **DAEDALUS item 1 DONE (Will "fix it now"):** `scripts/thresholds.py` exits 0 clean / 1 any BREACHED line / 2 no prices or any threshold ticker NO DATA (2 outranks 1, fail closed); yfinance missing → 2. `--selftest` 7/7 cases, and a mutant `verdict` scores 2/7 (rc 2), so the test can fail. Added to boot.py TRI_STATE. ⚠️ **Thresholds now reads ALERT every boot while WAL < $78** (REG-T-02 standing breach, and the KRE<65/WAL<70/65 context lines also count) — same permanent-ALERT shape as DAEDALUS item 9 (FLG ladder); decide with item 9.
- **My error:** first selftest fixture (KRE exactly $60 → 0) was wrong: KRE $60 is still under the script's KRE <$65 context line. The test caught my fixture, not the code; boundary re-tested on WAL $78.
- **Skipped:** CCB Q3, H.4.1 10/29, H.8 10/30, FHLB Q3 Highlights all unread. DAEDALUS items 2–14 + A1–A3 + falsification #5 + wiring ⑰ undispositioned. No PROME completion memo (Will-launched, not spawned). Consumer check not run: no registered figure superseded. ARGUS n/a (desk).

### PRIOR SESSION — 2026-10-30, started 09:05 ET (`date`), PROME-spawned (WQ-184 Tier 1, DOCKET L801) + whole-inbox drain
- **L801 decided** → `reports/2026-10-30_L801/REPORT.md`, KB ML-REG-260: problem-loan leg KEPT (7 of 10 up [10/23]; 2007–10 ρ +0.46); coverage-decline leg DROPPED as a predictor (2 of 10 episodes vs 25% unconditional; ρ −0.06; adds R² 0.088→0.094). Coverage stays a question about no-reserve collateral claims (FLG $1,571M; FLG cure 59.5%→1.6%, payoff/disposition 87.5%). Matrix coverage POINT untouched until the 11/07 S1-vs-S2 test. No score/threshold/probability change.
- **Q3 Call Reports:** FDIC BankFind 0 rows at 10/30 09:09 ET. Not waited for.
- **Inbox:** 13 drained (3 CYPHER + 10 WALTER) + 1 BOARD backfill; CYPHER boundary CONFIRMED with a CU→P3 amendment; COR-20261029-43 NO-OP. HY 314 [10/28], CCC/HY 4.16×; WAL $77.80 / KRE $72.86 [10/29]; REG-T-02 log +2 rows.
- **My error:** typed semicolons into a corrections `--scope` again (lesson from 10/28 repeated; the writer refused, re-sent clean).
- **Skipped:** CCB Q3 (10/29) and H.4.1 (10/29) unread — outside this spawn's task.

*10/28 PRIOR SESSION entry → `archive/MEMORY_rotation_2026-10-30.md` BLOCK M13, crc32 `5d7d98d1`.*

### CHANGES SINCE LAST SESSION

### NEXT SESSION
0. **⏰ FFIEC short-list RE-RUN between Sat 10/31 and Wed 11/04 (token expires 11/05):** `.venv/bin/python3 AGENTS/REGINALD/scripts/borrowing_shortlist_ffiec.py --out AGENTS/REGINALD/domain/sources/2026-10-28_boot/borrowing_shortlist`. 28 of 139 filed on 10/28 (net −$4.3B; Simmons flag explained as a brokered-to-FHLB swap). Read any NEW flag at the issuer before routing (deep dive §14).
1. **Printed, unread (read first):** CCB Q3 (10/29; Bluevine deposit detail, partner concentration, provisions; reconcile with CARL's consumer leg to one figure per metric) · H.4.1 10/29 · H.8 10/30 (descriptive only; 'deposits down' tell RETRACTED, deep dive §10) · FHLB Q3 Highlights (REG-T-06 descriptive; grades 11/13 from the CFR). Per-bank borrowing screen FROZEN (`reports/2026-10-28_borrowing-screen_FROZEN_rule.md`, sha256 `90e0a4a2…948a`); run once FDIC posts Q3 (~mid/late Nov).
2. **DAEDALUS 10/30 packets (4 in `inbox/`):** item 1 DONE 10/30 eve (reply with it). Items 2–4 decide L5: VX.tsv 14 stale LIVE rows (3 contradict STATUS) · OZK 37.6% dead-figure notes (bank-side HY report :122 + one more) · POSITIONS.md lacks Nov 66P/67P/68P/70P legs (collapse stacked headers). Then disposition 5–14 + A1–A3 (DONE / DEFERRED with date / DECLINED with reason) in one reply to `AGENTS/DAEDALUS/inbox/`. Charter trim (item 5) is MINE, no Will word (PROME, DOCKET L889). `V1V3-ACCELERATE` rename: coordinate with WALTER per `registry/NOTES.md` or re-date. read_cap rc 1 is NOT mine to clear (DAEDALUS tool, 11/04).
3. **Sat 10/31:** REG-06 EDGAR scan (WAL/EGBN capital raise; 424B, S-1/S-3/S-4, 8-K 3.02).
4. **HY:** grade each FRED print for the REG-T-03 exit run (≤300 ×5). CCC/HY escalates only on a CCC-led re-cross. REG-T-02 log: grade 10/30 settled close (vendor $76.29).
5. **Pathward (CASH) September-quarter release 10/21:** partner-credit and deposit lines (BaaS row). GDOT Q3 date still unannounced. WAL 10-Q cohort items logged for me (hotel franchise criticized $75M → $185M, OREO 22 → 27 properties) → read at the 11/07 run.
6. **JWT renewal before 11/05 (Will).** 11/07: verify sha256 `06e37edad2d583074a20f0ca70d0f84079a3eed95fba891204060662bcd00672` of the frozen ranking protocol, decide the cohort-selection question, then run.
7. **10-Qs, early Nov:** SBCF primary cells (CRE+constr 30-89, nonaccrual, resi) and the $8.4M VBI loan · SSB/BKU cells → FL aggregate final ~11/14 · FLG MF special mention and modifications · EGBN MF criticized table and REG-28 maturities · VLY ~11/10.
8. **Nano:** weekly P&A re-check from Tue 11/3; DEWEY's passive-route answer.
9. **Carried:** CUBI N at 11/07.

**CARRIED LESSONS — behaviour, not record.** *Newest first. Aging rule (9/02): full entry → one-line rule AND the full text goes to `archive/` verbatim + crc in the same pass. ⛔ Never age a lesson by deletion (the 12-21 compressions archived nothing; git history only). Preamble → BLOCK M7, crc32 `8028ecb4`.*
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
