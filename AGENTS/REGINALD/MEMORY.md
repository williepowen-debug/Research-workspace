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

### LAST SESSION — 2026-10-23 15:18 → 17:12 ET, Will-launched: boot + catch-up, learning review, rulings; closed at Will's request
- **Catch-up** → `reports/2026-10-23_boot/REPORT.md`: FLG 0/4 readable weakens-if met; AMTB FL HOLDS final; CUBI WQ-318 INCONCLUSIVE; cohort 7/10 problem loans up, 6/8 coverage down; KRE tracks the 10-year, not HY.
- **Learning review (Will-commissioned)** → `reports/2026-10-23_historical-learning-review.md` + 3 addenda. Verdict: method improved (DEMONSTRATED), judgment UNPROVEN. An outside reviewer caught REG-08 graded FAILED though it came true; my re-check found REG-10 too.
- **Will rulings applied:** REG-08/REG-10 → CONFIRMED, originals preserved (`5e0e8b301`; PROME DOCKET L824) · 11/07 ranking-test protocol FROZEN (sha256 `06e37eda…`) · matrix coverage-point wording corrected, scores unchanged · REG-T-04 single-issuer disclosure rider (WQ-512, `8452f2af7`).
- **TERRY answered** (`9938ffae5`): the rate link is the last 4 weeks only; the proposed alarms show no forward edge since 2006.
- **My errors today:** a wrong FLG count (caught pre-commit) · two typed time stamps · REG-08 accepted in my own review beside the contradicting $62.62 · "issuance freeze under way on volume" relayed from one snippet, WITHDRAWN on DEWEY (`8bcdaa8e5`).
- **Skipped:** H.8 (released 10/23 16:15) not read. Consumer check not run: no registered figure superseded (BANK-ABSENT conf and cohort tallies are desk-internal descriptives).

### CHANGES SINCE LAST SESSION

### NEXT SESSION
1. **HY / REG-T-04:** grade 10/23, 10/26, 10/27 closes from FRED (use `FORGE_CACHE_DIR` to bypass a stale cache). A fire → same-session bank cross-check + H.8 C&I/NDFI draw lines + the **WQ-512 single-issuer disclosure** (CSC/Optimum; `registry/NOTES.md`); packet LIQUID + Will chain. DOCKET L818 consumes 10/28; L825 Optimum event.
2. **DEWEY REQ-003** (CCC + under-80 loan composition) due Mon 10/26 → ACTION to me; it decides WQ-509's instrument (TERRY's broad-credit card).
3. **H.8 Fri 10/23 — NOT READ this session:** small-bank borrowings, C&I and NDFI loan lines (draw check). Update the STATUS H.8 row.
4. **SBCF Tue 10/27** after close: last FL frame name (aggregate goes final on ≥3 HOLDS). **REG-28 checkpoint 10/27:** EGBN $42.7M + $27.7M maturities. Nano P&A / DEWEY records route 10/27.
4b. **11/07 ranking test:** verify sha256 `06e37edad2d583074a20f0ca70d0f84079a3eed95fba891204060662bcd00672` of `reports/2026-10-23_ranking-test_FROZEN_protocol.md`, then run it on the Q3 Call Report pull. Retrospective, not blind. Do not edit the protocol.
5. **DOCKET L801 ~10/30:** Q3 cohort re-read vs DEWEY base rate (now 7/10 and 6/8). REG-T-06 Q3 OF Highlights 10/30; grades 11/13 from the CFR.
6. **Pending Will:** charter trim; JWT renewal before 11/05 (11/07 run).
6b. **Read-cap rotation DEFERRED at 10/23 close (conscious skip):** STATUS 79%, ROADMAP 75% of budget (rotate tier ≥75%; rule-5 stop <70%). Rotate verbatim + crc to `archive/` at the next session.
7. **Carried:** 10-Q cells (FLG MF special mention + mods, VLY mods ~11/10, SSB classified share, BKU CRE 30-89) · CCB/CASH/GDOT Q3 dates unchecked · CUBI N at 11/07.

**CARRIED LESSONS — behaviour, not record.** *Newest first. Aging rule (9/02): full entry → one-line rule AND the full text goes to `archive/` verbatim + crc in the same pass. ⛔ Never age a lesson by deletion (the 12-21 compressions archived nothing; git history only). Preamble → BLOCK M7, crc32 `8028ecb4`.*
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
