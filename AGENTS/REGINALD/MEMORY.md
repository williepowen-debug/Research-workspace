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

⚠️ **Open question at close:** when the Q4 CRE maturities resolve (EGBN $265.7M MF in 4Q26; VLY deferrals to ~Q1-27), do the "well-secured, no specific reserve" loans resolve near carrying value — or does realized loss show the falling reserve coverage (5/5 Q3 names) was under-reserving?

### LAST SESSION — 2026-10-22 ~11:0x–11:2x ET, Will-directed catch-up + PROME assignment
Boot (root/AGENTS/USER/COMPLETION_SPEC/Runtime mechanics + desk boot 1–9c); no pull needed (origin 0 ahead). Read at primary: SSB/BKU/EGBN/VLY/HBAN/ZION Q3 8-Ks (3 readers: EGBN Opus, VLY/BKU Sonnet; decisive figures self-verified), OCC GENIUS final rule PDF. Graded: REG-27 Q3 0.57% not met (OPEN); FL frame SSB HOLDS provisional, BKU HOLDS-PENDING-P; VLY L521 early flag strengthens; EGBN 008 → nonaccrual, re-extended 12/21/26, no cash. Answered Will's HY question (SIG-W-20261022-005): BANK-ABSENT 9/21→10/20 conf ~0.6, leg2 CCC-only. Drained 5 WALTER + 3 general inbox. Files: `reports/2026-10-22_catchup/REPORT.md`, `domain/sources/2026-10-22_catchup/`, `reports/2026-10-22_boot/`. Then Will's docx (AI-agent banking security) analysed → `reports/2026-10-22_AI-agent-banking-doc_analysis.md`. AI-generated synthesis, secondary-heavy; VLY 'acquired Bluevine' wrong (pending); HBAN '4 hrs/week' not in release. Read for us: run-speed caveat on weekly funding gauges, not credit. Run-speed column idea → PROME ideas list (not approved).

Prior handoff (10/21) preserved in git history of this file and `archive/MEMORY_session-handoff_2026-10-21.md`.

Later 10/22: EGBN Q4-wall dive (`reports/2026-10-22_EGBN_Q4_maturity_wall.md`) and the appraisal-discount cohort test (`reports/2026-10-22_appraisal-discount_cohort_test.md`, Will-approved). FLG SR 07-1 basis note added to matrix §3b (FLG packet verified at FDIC API). Quartr needs a Pro subscription (unavailable). EGBN call transcript not public; replay on the IR site through 11/5.

Afternoon 10/22 (Will-approved): DAEDALUS D:L793 fixes done. Charter step 9 now obliges ACKs on the OZK/WAL pair channels (WQ-484), with ACKs written. Exit rail re-derived (CBRE leg retired; CRE anchor re-keyed to WAL-01/02, NOT FIRED). TRADE/POSITIONS reconciled to the FORGE 10/22 capture (HBAN Oct-16 terminal, outcome UNKNOWN). boot.py: inbox/channel/resolve-by checks, non-zero exit. Resolve-by sidecar registry/PREDICTION_RESOLVE_BY.tsv. CALENDAR rotated to 22,977 B. CREED launched 12:19 and answered the CRE leg (rate shock, not credit).

### CHANGES SINCE LAST SESSION

### NEXT SESSION
1. Grade AMTB (10/22 AMC) FL cells and CUBI WQ-318 row; FLG 10/23 ~06:00 'weakens if' lines (MF SM ≤$2,757M; mods <$556M); SBCF 10/27. FL aggregate stays UNKNOWN until AMTB/SBCF + 10-Q cells.
2. H.4.1 10/22 16:30 primary credit vs descriptive lines (>12.9B / >15.7B, catchup §1e); H.8 Fri 10/23 small-bank deposits/borrowings. Not a registered threshold; registration needs base-rate pass + Will.
3. EGBN call 10/22 transcript (not heard): Prince George's reserve, 4Q MF maturities, 009/014 destination. VLY 10-Q (~11/10): mods/re-defaults, MF buckets. SSB 10-Q: classified accrual-share cell + REG-27 confirm.
4. WAL settled log complete through 10/21 (36 rows, run 0). REG-T-06 leg 3 grades 11/13 CFR (RULED B). JWT renewal before 11/5 Will-owned; 11/07 run.
5. Nano P&A/DEWEY checkpoint 10/27. CCB/CASH/GDOT Q3 dates still unchecked (add to the earnings table when verified at issuer).
6. Run boot.py at next boot: first live run of the new built-in legs + exit codes (tested in isolation 10/22, guard falsified on a synthetic channel). Design fix owed (DAEDALUS note 12:38 ET 10/22): boot.py → kre_float.py rewrites the TRACKED `scripts/.kre_float_state.json` on every run, so a reader's verification run dirties the tree. Add `--dry-run` or move the state file out of the tracked tree. Deferred D:L793 findings: frozen feeds still in BOOT_SEQUENCE (READS change needs PROME), glued-word re-spacing on next touch of each surface, MTB/ banner + root-file retirement at the 11/20 re-check.

**CARRIED LESSONS — behaviour, not record.** *Newest first. Aging rule (9/02): full entry → one-line rule AND the full text goes to `archive/` verbatim + crc in the same pass. ⛔ Never age a lesson by deletion (the 12-21 compressions archived nothing; git history only). Preamble → BLOCK M7, crc32 `8028ecb4`.*
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
