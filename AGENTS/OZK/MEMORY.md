# OZK MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis or delete, never just accumulate. For verified mistake patterns with prevention rules, see `LESSONS.md`.*

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
- [2026-04-24] **Offer files, not verbal reports.** When asked for audit/review/analysis, write to a named file (AUDIT.md, REPORT.md, etc.) in own agent dir. Cross-session visibility is restricted — the file is the handoff. (Reinforces existing CLAUDE.md "File > verbal" rule; this session produced AUDIT.md per pattern.)

## Findings
- [2026-04-02] `scripts/market.py` pulls live prices via yfinance. Must run with `.venv/bin/python3` from workspace root (not from AGENTS/OZK/).
- [2026-04-02] OZK price sources can conflict ($46 vs $49 in same session) — always verify at broker when discrepancy >5%.
- [2026-04-12] FDIC EFR system: efr.fdic.gov/fcxweb/efr/ — OZK Form 3/4/5 filings live HERE, not on SEC EDGAR. FDIC cert #110. Standard insider tools miss OZK.
- [2026-04-16] pdfminer works for PDF text extraction (`.venv/bin/python3`, `from pdfminer.high_level import extract_text`). poppler-utils not installed.
- [2026-04-22] **OZK public press release is truncated on globenewswire + stocktitan mirrors.** Real data lives in 3 separate docs on IR page: (1) Financial Supplement PDF (228K, balance sheet + income statement + ACL + classified/criticized detail), (2) Management Comments PDF (1.3MB, 38 pages — RESG portfolio deep dive, Figure 24 substandard credit roster, foreclosed asset detail, sub notes repricing schedule, variable-rate floor ladder), (3) earnings call transcript. The press release body is essentially just EPS + CEO quote.
- [2026-04-22] **OZK IR page (ir.ozk.com/filings/documents/) 403s to scripted pulls.** Tried HTTP/1.1, HTTP/2, multiple UAs — all blocked. Browser works. For multi-quarter historical Mgmt Comments PDFs, user must pull via browser.
- [2026-04-22] **Rossow canonical IQHQ exposure quote (Bisnow 3/19/26):** "We have one credit with IQHQ, which is the senior secured loan on their San Diego RaDD project." Michelle Rossow is OZK Chief Communications Officer. Closes the "any other project with IQHQ" ambiguity from Gleason Q1 transcript.
- [2026-04-22] **Boynton Yards Somerville is NOT an IQHQ project** — common misclassification. Sponsor is Leggat McCall + DLJ Real Estate + Deutsche Finance America. OZK lent $246M to Leggat McCall (not IQHQ). This firms SEVEN_CREDIT §2 #5 Candidate B for the $169M Boston Life Sci substandard.
- [2026-04-22] **Other IQHQ-project lenders (disconfirmation map):** Fenway → JPMorgan $165M; Arbor/Elco Yards Redwood City → KKR Real Estate Finance Trust $581M; Spur Phase I SSF → Apollo $275M; 155 N. Beacon Brighton → Citizens Bank $486.5M; 109 Brookline → $130M assumed from Equity Commonwealth 2020 (not OZK-originated).
- [2026-07-04] **⚠️ SEC CIK 0001569650 is NOT OZK's operating-company filer — it's the 13F/13G institutional-investment-manager arm.** OZK dissolved its holding company in 2017; as an FDIC state non-member bank it files 10-K/10-Q/8-K **and** Section 16 insider forms with the **FDIC** (efr.fdic.gov, cert #110), not SEC EDGAR. That CIK's EDGAR history is entirely 13F-HR + 13G/A. **There is no SEC 10-Q for OZK.** Any EDGAR-keyed tool silently misses OZK financials — use FDIC EFR + OZK IR (Mgmt Comments / Financial Supplement). Corrects the old References line.
- [2026-07-04] **Primary transcript beats trade press on the IQHQ maturity.** Bisnow (3/19/26) reported a "two-year extension → ~Aug 2028." REFUTED by the Q1 2026 earnings call (local `raw/Q1_2026_earnings_call_transcript.md`): Mealor "matures in August of this year," Gleason "August is an eternity from now." **Maturity = Aug 2026, re-confirmed from primary.** When a fresh web pull resurrects a date we already corrected, check the local primary before re-opening. [[finding_edgar_fts_refutes_tradepress_negatives]]
- [2026-07-04] **RESG % of loans ≈ mid-50s and falling** (62% Mar'25 → 60% Jun'25; Gleason targets ≤50%). So PROME's unpinned "RESG 88%" is NOT RESG/total-loans. Bluerock IQHQ marks are all H2-2025 vintage (no fresh Q1); public sources call them fund equity/interest, not "PIK debt" — verify our PIK framing. Aimco MTD: no public ruling found (needs Chancery docket pull).

## References
- [2026-04-02→corrected 2026-07-04] ~~EDGAR CIK for OZK: 0001569650~~ — **that CIK is OZK's 13F institutional-investment-manager arm, NOT the operating company. OZK files financials + insider forms with FDIC (cert #110), not SEC EDGAR. No SEC 10-Q exists.** See 2026-07-04 Findings.
- [2026-04-22] OZK IR docs: `ir.ozk.com/filings/documents/` — cross-posts FDIC + SEC filings. Quarterly: Financial Supplement + Management Comments (separate PDFs) + transcript. Will can pull via browser when WebFetch 403/timeouts block.

## Session Notes

⚠️ **Open question:** Should Q2 conviction step down if the RESG-runoff/de-risking bull case (WEAKNESSES C7) is validated at the Jul-21 print? The discriminator is classified+criticized-vs-RESG-balance: both falling together = bull case gains; classified rising while RESG shrinks = adverse-selection tell (thesis holds). Pre-register the read before Jul 21.

**CHANGES SINCE:** *(leave blank — next boot populates via market.py price delta check)*

### LAST SESSION (2026-07-04 — 71-day revival + recent-data incorporation)

- **Boot on 71-day cold state (prior touch 4/24).** Git pull blocked by OTTO's uncommitted changes (other-agent files — flagged to Will, did NOT touch/pull; `git fetch` showed origin 0/0, so nothing missed). Read PROME REVIVAL-PACKET + resg-verification inbox items for catch-up context.
- **Will steer mid-session:** de-prioritize positions (minimal/uncertain current OZK exposure), focus on **incorporating + updating all recent OZK data.** Pivoted accordingly.
- **Web sweep (1 background agent) pulled all post-Apr outcomes.** Key: Q2 = **Jul 21** (not mid-Jul); −5.70% on 7/2 was **idiosyncratic, no public catalyst** (+1.95% AH); $200M buyback 6/29 + dividend +2.1% 7/1; KBRA affirm w/ **negative outlook** (RESG charge-off stress); Street targets low-mid $60s on RESG-runoff de-risking; WAL Investor Day = **no** IQHQ exposure (closes TODO #3); no fresh Q1 Bluerock marks.
- **IQHQ Aug-2026 maturity re-confirmed from PRIMARY** (local Q1 transcript) — refuted a resurfaced Bisnow "2028 extension" claim. Thesis pin holds.
- **Docs re-baselined:** `STATUS.md` (full rewrite — price, PROME-verified Q1 figures $487.5M/1.48% + NCO 0.56% + NPA $446.1M, Q2 Jul-21, dead cross-feed killed, recent-developments table, position table marked STALE/not-managed), `CALENDAR.md` (7 passed catalysts logged w/ outcomes; forward docket), `WEAKNESSES.md` (new **C7** RESG-runoff bull case + adverse-selection rebuttal), `MEMORY.md` (SEC-CIK correction, primary-refutes-Bisnow finding).

### NEXT SESSION

1. **Pin the RESG "88%"** — extract Figure 16 (RESG diversification, 3/31/26) + funded/unfunded from `raw/Q1_2026_mgmt_comments.pdf`; identify what the metric is. Feeds Q2 path-(a).
2. **Verify Bluerock "PIK debt" framing** vs the equity/interest characterization in public sources; reconcile PRIVATE_CREDIT/ + IQHQ_PLAYBOOK capital stack.
3. **Aimco v. IQHQ MTD** — pull Delaware Chancery docket for any ruling.
4. **Pre-register the Jul-21 Q2 read** (WEAKNESSES C7 discriminator; NCO ≤55bps kill-line watch — Q1 was 0.56%, 1bp above).
5. **THESIS/CHANGELOG pass** — decide whether C7 warrants a conviction note (currently 🔴🔴 HIGH). Deferred pending Q2.
6. **Deferred backlog:** KB_INDEX rollup Phases 2-4+6 (TODO.md §H1); refresh REGINALD_CHANNEL.
- **Housekeeping flag for Will/PROME:** OTTO has uncommitted working-tree changes (STATUS, docket/CATALYSTS.tsv, thesis/PREDICTIONS.tsv) blocking clean pulls — a stale/broken OTTO closeout, not mine to fix.
