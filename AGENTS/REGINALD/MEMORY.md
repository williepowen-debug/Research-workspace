# REGINALD MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis or delete, never just accumulate. For verified mistake patterns with prevention rules, see `LESSONS.md`.*

---

## Feedback
- [2026-04-02] Will values boot transparency — wants to know what REGINALD read, in what order, and whether the process is working. Don't orient silently; confirm orientation.
- [2026-04-02] Will prefers sessions to have freedom rather than being laser-focused on pre-set priorities. Provide context, not directives. Rejected ranked TOP 3 queue in favor of a single "open question."
- [2026-04-02] Will thinks long-term about infrastructure. When proposing solutions, address scaling and durability, not just immediate need.
- [2026-04-02] Will wants position data stored in REGINALD's domain (POSITIONS.md), not just FORGE. "That was just for you."
- [2026-04-02] Will prefers breaking large implementation work into discrete tasks done one at a time, with approval between each.
- [2026-04-16] Will wants REGINALD to read full source documents (PDFs, 10-Ks) before opining, not just spot-check sections. Caught that I only keyword-searched the earnings release initially. Thoroughness > speed for primary source analysis.
- [2026-04-22] **Iteration philosophy validated:** Write Round 1 with available data, then improve as more data arrives. Will explicitly said "begin with what we have and we will improve on it as we learn more" when public press releases were truncated and he was going to provide supplement PDFs. Don't wait for perfect data to start writing.
- [2026-04-22] **"What I NEED FROM YOU" lists work.** When analysis files end with an explicit gap list, Will reads it and delivers the exact files. Keep these lists concise and specific (filename + what's in it).
- [2026-04-22] **Thesis architecture: "synthesis + pointer" pattern.** THESIS.md carries the synthesized takeaway from sub-docs (2-3 sentences + headline number + pointer), not duplicated detail. Sub-docs (IQHQ_PLAYBOOK, SEVEN_CREDIT_DEEP_DIVE) hold the deep analysis. Changelog tracks THESIS.md only. Filter: thesis-level shifts get changelog entries; evidence accumulation stays in sub-docs + KB rows. Scope guard: if writing a 4th sentence of sub-doc summary in THESIS.md, it belongs in the sub-doc.
- [2026-04-22] **Domain CHANGELOG needed per bank.** Each bank subdirectory (OZK/, WAL/) should have its own CHANGELOG.md that tracks its THESIS.md only — mirrors format of master `thesis/CHANGELOG.md`. OZK was missing one; authorized creation. Version convention: vX.Y where major = structural, minor = refinement. First entry describes change AND pins prior state as v1.0.

## Findings
- [2026-04-02] `scripts/market.py` pulls live prices via yfinance. Must run with `.venv/bin/python3` from workspace root (not from AGENTS/REGINALD/).
- [2026-04-02] FRED API key not configured — HY OAS, claims, and other FRED series at boot require `FRED_API_KEY` env var. Low priority but would close data gap.
- [2026-04-02] OZK price sources can conflict ($46 vs $49 in same session) — always verify at broker when discrepancy >5%.
- [2026-04-12] FDIC EFR system: efr.fdic.gov/fcxweb/efr/ — OZK Form 3/4/5 filings live HERE, not on SEC EDGAR. FDIC cert #110. Standard insider tools miss OZK.
- [2026-04-12] Wasatch fund commentaries: wasatchglobal.com/wp-content/uploads/strategy-and-fund-documents/ — quarterly fund PDFs.
- [2026-04-16] pdfminer works for PDF text extraction (`.venv/bin/python3`, `from pdfminer.high_level import extract_text`). poppler-utils not installed.
- [2026-04-16] CFG 10-K HTML from EDGAR has inline-XBRL markup; use regex `re.sub(r'<[^>]+>',' ',html)` not BeautifulSoup `.get_text()`.
- [2026-04-19] **Paywall map:** Forbes.com, Seekingalpha.com, Journalrecord.com (Reuters wire) return 403 to Anthropic WebFetch. Workable substitutes: MarketScreener, PrismNews, Sharecafe (Reuters), Motley Fool / Investing.com (SA transcripts).
- [2026-04-22] **OZK public press release is truncated on globenewswire + stocktitan mirrors.** Real data lives in 3 separate docs on IR page: (1) Financial Supplement PDF (228K, balance sheet + income statement + ACL + classified/criticized detail), (2) Management Comments PDF (1.3MB, 38 pages — RESG portfolio deep dive, Figure 24 substandard credit roster, foreclosed asset detail, sub notes repricing schedule, variable-rate floor ladder), (3) earnings call transcript. The press release body is essentially just EPS + CEO quote.
- [2026-04-22] **LAM = Leucadia Asset Management = Jefferies subsidiary** (post-2013 Leucadia/Jefferies merger). Semantic mapping critical for V2 fraud chain — WAL's $126.4M LAM charge-off is on the Jefferies rail. Cross-reference in any WAL/Jefferies/Cantor research.
- [2026-04-22] **Quartr MCP is subscription-gated** — returned `subscription_required` error when searching companies. Cannot use for document/event fetching. WebFetch + direct IR page links or user-provided PDFs are the workaround.
- [2026-04-22] **OZK IR page (ir.ozk.com/filings/documents/) 403s to scripted pulls.** Tried HTTP/1.1, HTTP/2, multiple UAs — all blocked. Browser works. For multi-quarter historical Mgmt Comments PDFs, user must pull via browser.
- [2026-04-22] **Rossow canonical IQHQ exposure quote (Bisnow 3/19/26):** "We have one credit with IQHQ, which is the senior secured loan on their San Diego RaDD project." Michelle Rossow is OZK Chief Communications Officer. Closes the "any other project with IQHQ" ambiguity from Gleason Q1 transcript.
- [2026-04-22] **Boynton Yards Somerville is NOT an IQHQ project** — common misclassification. Sponsor is Leggat McCall + DLJ Real Estate + Deutsche Finance America. OZK lent $246M to Leggat McCall (not IQHQ). This firms SEVEN_CREDIT §2 #5 Candidate B for the $169M Boston Life Sci substandard.
- [2026-04-22] **Other IQHQ-project lenders (disconfirmation map):** Fenway → JPMorgan $165M; Arbor/Elco Yards Redwood City → KKR Real Estate Finance Trust $581M; Spur Phase I SSF → Apollo $275M; 155 N. Beacon Brighton → Citizens Bank $486.5M; 109 Brookline → $130M assumed from Equity Commonwealth 2020 (not OZK-originated).

## References
- [2026-04-02] FRED API key signup: https://fred.stlouisfed.org/docs/api/api_key.html
- [2026-04-02] EDGAR CIK for OZK: 0001569650
- [2026-04-16] EDGAR CIK for MTB: 0000036270
- [2026-04-16] Cadwalader Fund Finance Friday — tracks fund banking personnel and deals.
- [2026-04-22] OZK IR docs: `ir.ozk.com/filings/documents/` — cross-posts FDIC + SEC filings. Quarterly: Financial Supplement + Management Comments (separate PDFs) + transcript. Will can pull via browser when WebFetch 403/timeouts block.

## Session Notes

⚠️ **Open question:** Has Will executed the Thread 3 roll yet? Recommendation (per `OZK/THREAD3_ROLL_MATH.md`) is to close May $42.5P × 2 + open Jan27 $42.5P × 2 (~$510 debit). Hard deadline ~May 8 for decision; execution ideally this week before May premium fully decays. Checkpoint 1 persistence debt (KB-OZK-178 through 184 + 3 PREDICTIONS rows) remains unaddressed — Will redirected priority to Thread 3 + file-tree cleanup this session.

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py)*

### LAST SESSION (Apr 22 evening → Apr 23 — Thread 3 + OZK file tree cleanup)

**Thread 3 executed → `OZK/THREAD3_ROLL_MATH.md` (160 lines).** Live yfinance chain pull + BS deltas/vegas + time-aware scenario P&L grid across May/Jun/Aug/Nov/Jan27 expiries, $40/$42.5/$45 strikes. Recommendation: **close May $42.5P × 2 → open Jan27 $42.5P × 2** (~$510 debit). Raw-ROI winner is Aug $42.5 (+53%) but existing book is Aug-heavy (5 contracts) — Jan27 (+39%) picked for duration diversification + Scenario D coverage (18% prob, Oct-Dec foreclosure tempo). Hard deadline ~May 8.

**File tree cleanup (OZK top-level 19 → 15 .md files):**
- `EARNINGS_PREP.md` → `archive/EARNINGS_PREP_Q1_2026.md` (Q1 resolved)
- 3 Apr 22 threads → `research/threads/`: IQHQ_SECONDARY_EXPOSURE, CIB_MARGIN_COMPRESSION, RESG_MIX_DETERIORATION
- `INDEX.md` rewritten — Data Ownership table, new Boot Sequence (12 min), research-threads rule, purged Mar 25 refs
- Cross-refs updated in THESIS (3), STATUS (1), SEVEN_CREDIT (1), CHANGELOG (3 replace_all), thesis/TIMELINE (1)
- `historical/README.md` created — documents quarterly extract naming convention + boundary vs archive/

**Archive vs historical resolved (not collapsed):** Confirmed two dirs serve different lifecycles — `archive/` = agent-generated dead work (audits, plans, legacy narrative); `historical/` = live primary-source extracts (quarterly Mgmt Comments, actively used for 6Q trajectory). Both kept; historical/README.md now makes the rule explicit.

**Commits (2):**
1. `196cc3e0` — Thread 3 + file tree cleanup (11 files, +284/-111)
2. Pending: `historical/README.md` + this MEMORY update

**What I did NOT do this session (unchanged carryover):**
- Checkpoint 1 (KB-OZK-178 through 184 + 3 PREDICTIONS rows) — still queued
- Checkpoint 2 — partial. `OZK/CHANGELOG.md` was created in a parallel session (already exists with v1.1 entry per boot observation). THESIS.md already updated with v1.1 framing. So Checkpoint 2 is largely DONE — just verify vs spec.
- Root `STATUS.md` pruning — still queued (Apr 7/9/10 briefs → archive)
- WAL Round 2 — awaits supplement/transcript

### NEXT SESSION — priorities by urgency

1. **Monitor roll execution.** Did Will close May $42.5P × 2 and open Jan27 $42.5P × 2? Update POSITIONS.md + IQHQ_PLAYBOOK §6 after broker confirmation. If not yet executed, re-quote the chain (prices will have moved).

2. **Checkpoint 1 — persistence (~20 min):** Append KB-OZK-178 through 184 to `OZK/workbook/KB.tsv`:
   - 178: Rossow IQHQ sole-exposure quote (Bisnow 3/19/26)
   - 179: Leggat McCall = 808 Windsor/Boynton Yards $246M
   - 180: CIB 3/6 vertical compression
   - 181: CIB Q1 2026 NIM decomp
   - 182: RESG problem-category share +250bps QoQ (⚠️ note: retracted in CHANGELOG v1.1 — enter as historical claim, mark superseded)
   - 183: Hamblen MF-heaviest-runoff admission
   - 184: Forward projection mechanics (⚠️ marked SUPERSEDED per CHANGELOG)
   - Append 3 PREDICTIONS rows: REG-21 problem-cat ≥32% (25% conf), REG-22 FY 26 NCO ≥60bps (55%), REG-23 classified/RESG ≥3.8% Q4 26 (60%)

3. **Checkpoint 2 verification:** Confirm `OZK/CHANGELOG.md` v1.1 entry and `OZK/THESIS.md` v1.1 body match CHANGELOG spec. If any gap, close.

4. **Root REGINALD `STATUS.md` pruning** — 572+ lines, Apr 7/9/10 briefs → `archive/` (~20 min).

5. **WAL Round 2** if Will delivered supplement/transcript.

**Ask of Will (still open):** Browser-pull Q4 24 / Q1 25 / Q2 25 / Q3 25 OZK Management Comments PDFs — gives 8Q mix-shift trajectory. Note Apr 23 parallel session already created `historical/Q4_24_extract.md` through `historical/Q4_25_extract.md` per boot observation, so this ask may already be fulfilled — verify first.
