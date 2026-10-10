# REGINALD MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis or delete, never just accumulate. For verified mistake patterns with prevention rules, see `LESSONS.md`.*

---

## Feedback
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

⚠️ **Open question (10/10 PM):** does the late-September jump in smaller banks' borrowing (H.8 `H8B3094NSMA` +$32.9B / +11.7% in 3 weeks to 9/30; deposits flat) **continue, hold or reverse in the Fri 10/16 print (week of 10/7)**, and does any Q3 print show it **with deposits leaving** (the PNC pattern spreading)?
- The L180 breadth test (11/07 Call Reports) stays the CRE question; it is in the read plan, not here.
*Prior open question + LAST SESSION 10/9 PM (incl. 10/10 AM) + PRIOR SESSION 10/9 AM → `archive/MEMORY_rotation_2026-10-10.md` BLOCK M1, crc32 `1548bf8c`.*

### LAST SESSION — 2026-10-10 Sat ~12:39 → ~14:xx ET (Will-launched, Opus 5.5; AM bookkeeping is in BLOCK M1)
**1. Boot:** full read set · market.py (10/9 settled, stale-weekend) · ladder rc 1 (FLG RED, 3 closes) · staleness · corrections 0 · inbox 0 at boot (+1 MARCO Pharr wording NO-OP, filed).
**2. ★1 as-made audit (`28c7dd7dd`):** all 20 rows by text; REG-13 re-formed; REG-07 "Brier on 55%" corrected to 68% (WQ-112(i)); REG-10 registered after its outcome, kept scored (WQ-161 ②). DAEDALUS packeted (10/12 sitting).
**3. ★2 FHLB (`e4916e89a`, `11f3a8a4b`, `e1fc74154`):**
- **Composition (6/30):** ~half of H1 +$136.2B = PNC/Citi/USB/WFC; mid/small flat; Atlanta +6.9%, SF −10.6%. Why: Citi says growth funding; USB borrowed and held cash (inference); WFC growth; PNC alone replaced lost deposits.
- **`REG-T-06` letter non-discriminating:** >$700B in 12 of 26 quarters → WQ ask to PROME (doorbelled).
- **Weekly H.8 (Will asked about newer data):** small-bank borrowings +11.7% in 3 wks to 9/30 (160-wk max); discount window >p90 two weeks; credit-side bars quiet → WALTER signal to LIQUID (doorbelled). ⚠️ **I had told Will "regionals flat" from June data before checking this.**
**4. ★3 July threads (`004b3a238`):** five closed, archive crc `fd8df983`; the CCC/HY counter went to backlog.
**5. Write-back pass (Will):** TRADE (credit-bet line + trigger states) · CALENDAR (+funding row, +`REG-T-06` ~10/29 row) · dashboard pointer · ROADMAP · STATUS headline + rows refreshed to 10/9 settled · rotations STATUS T20–T25, ROADMAP R3–R5, MEMORY M1.
### CHANGES SINCE LAST SESSION
(leave blank — next-boot market.py + drift-grep populates)
### NEXT SESSION
**★ NEXT BOOT (set 10/10 PM; Will's three catch-up items are DONE, see LAST SESSION):**
1. **Weekly funding read: Thu 10/15 H.4.1 · Fri 10/16 H.8** (`H8B3094NSMA`, `WLCFLPCL`, small-bank deposits + cash, SA AND NSA). Continue / hold / reverse? A deposit decline alongside = the PNC pattern spreading → packet LIQUID + PROME the same session. Bars stay descriptive (base-rate before any registration).
2. **`REG-T-06` re-letter:** Will's word via PROME's WQ row, BEFORE the ~10/29 Q3 figure. On his word: update `registry/THRESHOLDS.tsv` + `registry/NOTES.md`, then ONE packet to LIQUID + BOND (held until then). Without a word, it grades as lettered with the composition read attached.
3. **REG-07 (WQ-412): Will's VOID-or-grade before SSB prints Wed 10/21 AMC;** without a word, it grades on the CHANGE (scores at 68%).
4. **HBAN puts (WQ-302):** Will sells or rolls by Wed 10/14; write the fill back to POSITIONS from the broker export.
5. **Large-bank desk:** DAEDALUS holds the packet (`32d24f8ff`). Citi / USB / WFC FHLB purpose is that desk's perimeter if built.
*Full 9/29 list (every carried item's text) → `archive/MEMORY_rotation_2026-10-07.md` BLOCK M2, crc32 `401793b1`. Items marked (M2) keep their full text there.*
**🔴 0-Q3. RUN THE Q3 READ PLAN AT EACH PRINT — `reports/2026-10-09_Q3_earnings_read_plan.md` §5 schedule** (CFG **Fri 10/16** first). Grade only the frozen frames: WQ-318 list · CRE top-3 §6 · L35 / L521 · FL frame + A3 · §2.3 AMTB lines. Read the WAL / OZK / FLG desks' grades for their names; the cross-bank row is mine.
- **§2.0 rules govern:** individual ≠ spread · original total-CRE basis, multifamily separate · missing → UNKNOWN · release = provisional.
- **11/07 = planned Call Report retrieval; check completeness FIRST.**
- **Update the §0 judgment only on L180 BROADER or FL-rail TRANSMISSION.**
- **CUBI / FLG dates:** update the CALENDAR earnings table when announced. The countdown reads it, and FLG's T-03 looks 10/16.
**🔴 0a. WAL exit grading:** 10/9 GRADED 10/10 (row 28, 0-of-3). Grade **10/12 onward** from settled bars (`scripts/settled_bars.py WAL`: two routes, today's bar excluded). Count from `registry/REG_T02_EXIT_LOG.tsv` (28 rows through 10/9, 0-of-3). 2-of-3 → packet TERRY.
**🔴 0a-NEW. Tier test each boot:** FRED HY/CCC/B/BB. ⚠️ The cache-busted CSV route FAILED 10/9 (HTTP/2 error / timeout), so the API route (`fetch.py fred`) was used. If HY prints >320 again, START the REG-T-03 count and run the bank-credit cross-check.
**🟢 0-DAEDALUS. DONE 10/10 (Will go-ahead):** REG-03/06/07 instruments named (REG-07 grades on the CHANGE in SSB NPL/loans vs 0.62% base, since its level reading was true at birth; **flagged to Will before 10/21**) · F#4 wording fixes (registry token `V1V3-ACCELERATE` rename DEFERRED, WALTER reads it) · wiring ⑰ VX re-cut · stale tables (VX 27 STALE, FLOW frozen, AOCI/FUNDING FROZEN-VINTAGE, KB +3).
**🟡 0-LIMB. L180's "new foreclosure build" is unquantified.** Read literally (any QoQ rise), WAL met it at Q2 (+2.3%). Print the size beside every grade. A floor is Will's rule to make; don't add one.
**🟠 0-HBAN. `HBAN $16P Oct-16 ×2` ITM — Will rules by Wed 10/14 (WQ-302, card `MGMT-HBAN16P-OCT16`).** Supply the bank-side read if asked; write back the ruling. HBAN prints 10/22, after expiry.
**🟠 0-NEW-PUTS. Fidelity WAL Dec-18 $65P ×4 / OZK Nov-20 $40P ×4 (FORGE D-74):** fills/approval unrecorded; WAL/OZK desks own the position records; TERRY owns any card. My Q3 rows (WQ-318 + CRE top-3) are the thesis reads that bear on them.
**🟠 0a-NANO.** 10/9: P&A **still NOT posted**; FDIC **bid summary posted 10/8** → §3 re-run done (`reports/2026-10-09_nano-banc-bid-summary-and-section3-rerun.md`: retained-pool ≈32–42%). **Re-check P&A Tue 10/13**, then Tuesdays; none by 10/27 → DEWEY records route. On posting: size Pools A/D, place the $97.1M HFS book + WAL O1 DOTs, re-run §2 with pool sizes. Bar date not posted.
**🟠 0a-FL.** ✅ Dates done 10/7 (BKU 10/21 BMO · SSB 10/21 AMC · AMTB 10/22 AMC · SBCF 10/27 AMC; VLY 10/22 BMO). Grade the frozen frame `reports/2026-09-24_FL_bank_rail_Q3_FROZEN_frame.md` at each print; ≥2 TRANSMITS → packet CORAL + PROME the same session.
**🟡 0a-0. FLG ladder is RED and EXHAUSTED** — no band beyond RED. Exit-code defect FIXED `b6544d45d`. **Intraday-bar defect FIXED 10/9 (`8255c2d13`).** Census other frozen-baseline bands into the script (M2) — NOT this cycle (Will: no further tooling expansion).
**🔴 0a-bis (M2).** **11/05 FFIEC JWT expiry (Will), two days before the 11/07 run.** *(As-made packet DONE 10/10 PM; the DAEDALUS VX re-cuts were DONE 10/10 as wiring ⑰, per STATUS §OPEN PROCESS ASKS.)*
**🔴 0a-ter (M2). Carry-premise audit** — the most valuable item on this list; unchanged.
**🟠 2 (M2). Pre-print observables into `boot.py`** — base-rate before building. WQ-318 adds the per-bank observables (NIB average, IB cost, FHLB) but they are quarterly.
**🟠 3 · 4 · 6 · 6d · 6f · 6g · 6h · 6i · 6j · 6k · 7 (M2)** — ~~FHLB Atlanta/SF 10-Qs~~ (DONE 10/10) · OREO vector base-rate; REG-07 re-mark + REG-03/07 re-specs at the Q3 print, deliberately; EGBN runway post-break re-audit; read-cap every closeout; `boot.py` SHORT_INTEREST writes; aged 9/2 items. Unchanged; full text in M2.
**🟢 Done 10/10 PM:** catch-up ①–③ + FHLB follow-ups + write-back pass (LAST SESSION). **🟢 Done 10/9 PM:** monitor repair (OZK FDIC route · VLY CIK · coverage · no false all-clear · countdown · settled bars) · Q3 read plan + Will's clarifications. **🟢 Done 10/7:** 0-CARD (TERRY `TRY-COND-KREADD`, conditional, not armed) · 0-EXP (KRE rolled) · 0-WB · 0-WQ318 · item 1 TRY-FIRE-002 dates · DAEDALUS header · R3 phrases.

**CARRIED LESSONS — behaviour, not record.** *Newest first. Aging rule (9/02): full entry → one-line rule AND the full text goes to `archive/` verbatim + crc in the same pass. ⛔ Never age a lesson by deletion (the 12-21 compressions archived nothing; git history only). Preamble → BLOCK M7, crc32 `8028ecb4`.*
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

(leave blank — next-boot market.py + drift-grep populates)
