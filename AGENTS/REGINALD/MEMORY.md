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

⚠️ **Open question:** Thread 3 roll execution status still unresolved across two Apr 23 sessions. Recommendation per `OZK/THREAD3_ROLL_MATH.md` remains close May $42.5P × 2 + open Jan27 $42.5P × 2 (~$510 debit). Hard deadline ~May 8. Chain quotes may need refresh if executed this week.

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py)*

### LAST SESSION (Apr 23 PM — OZK subdir refresh + $495M gap characterization + KB additions)

**Scope:** Post-Q1 integration session. Cleared the subdir refresh queue identified during the AM session, characterized the $495M unmapped classified/criticized gap, added 7 KB rows, logged two new material findings.

**Spawn pattern:** 3 parallel Explore agents (single message, independent): (1) Q1 transcript + Mgmt Comments extraction for Fund Finance / NDFI / non-bank lender quotes, (2) staleness survey across LIFE_SCI / GEOGRAPHY / PRIVATE_CREDIT subdirs, (3) raw PDF catalog of classified/criticized detail beyond the 11 named credits. One retry needed on spawn #3 (prompt-too-long on first attempt). Clean context hygiene — 3 big PDFs never entered main window.

**Two new material findings:**
1. **LFG ALSO compressing** (not just Fund Finance). Jake Munn's Q1 call disclosed pricing + structure compression in Lender Finance Group too — so 2 of 4 CIB sub-segments in managed retreat, not 1. Broader story than prior framing.
2. **Asymmetric disclosure.** Jake Munn's pullback statements appear in the spoken earnings call transcript ONLY — NOT in the durable written Management Comments PDF (which shows Fund Finance growing $210M → $1.275B YoY with no commentary on the margin erosion). Management reluctant to formalize the competitive problem in durable documentation. Signal fits the broader extend-and-pretend posture noted elsewhere in thesis. Watch Q1 10-Q (~May 5) — does written disclosure pick it up?

**$495M gap — characterized (not solved):**
- Special Mention $397M is fully opaque at project level. Only resolvable at May 1-10 Call Report (FFIEC RC-N). Do NOT chase via forensic research.
- ~$98M sub-threshold RESG tail ($57M non-accrual + $37M accrual + $4M foreclosed) is probably not individually actionable; watch Q2 26 Figure 24 for cohort migration.
- Non-RESG classified (CIB, Community Banking, Indirect) is a blind spot — implied near-zero but not itemized. 10-Q (~May 5) MD&A can verify.

**Files touched (OZK-only):**
- `PRIVATE_CREDIT/` (4 files): NDFI_EXPOSURE.md (+Q1 Update section), TRANSMISSION.md (+Channel 3 amplifier), STATUS.md (rewrite), README.md (rewrite). Narrative: "lends to the lenders" → "lends to AND competes with the lenders."
- `LIFE_SCI/` (3 files): FINDINGS.md (Finding 2 corrected — Aug 2028 extension was a research error; Finding 18 added for Q1 new credits), README.md (rewrite), STATUS.md (rewrite). IQHQ Aug 2028 error propagation fixed across all three files.
- `GEOGRAPHY/STATUS.md`: +3 new metro credits (Seattle U Dist $127M, Santa Monica $45M foreclosed, Chicago Life Sci $50M foreclosed). Distressed cluster total $2.9B → $3.1-3.3B.
- `SEVEN_CREDIT_DEEP_DIVE.md`: new §3A "Rest of Problem Book" with gap decomposition + prioritization logic (don't chase Special Mention).
- `workbook/KB.tsv`: +7 rows. 186-188 PRIVATE_CREDIT (Fund Finance pullback, LFG compression, asymmetric disclosure). 189-191 LIFE_SCI (Boston $169M, Seattle U Dist $127M, Chicago foreclosed $50M). 192 GEOGRAPHY (Santa Monica foreclosed $45M).
- `TODO.md`: subdir queue cleared, gap char marked done, KB_INDEX staleness flagged as deferred.

**KB ID collision caught and fixed mid-session:** Drafted subdir updates using KB-178-180 for new credits, but those IDs already held Rossow / Boynton Yards / Vertical Compression rows from the prior AM session. Re-numbered to 186-192 across 4 files (LIFE_SCI ×3, GEOGRAPHY/STATUS.md ×2 edits).

**Known deferred staleness:**
- `workbook/KB_INDEX.md` — dated Mar 25, claims 159 rows, actual 192. Rows 160-192 not in cluster rollups. 30-60 min to refresh. Not blocking — agents read KB.tsv directly.
- Root REGINALD `STATUS.md` pruning (still 572+ lines, Apr 7/9/10 briefs should archive). Carryover.
- OZK/STATUS.md was refreshed earlier this session (AM) — that part is done.

### NEXT SESSION — priorities

**New (from this session):**

1. **May 1-10 Call Report triage** — when filings appear, 30-60 min pass on FFIEC RC-N for Special Mention breakdowns (asset class + geography). Informs how much of the $397M sits in RESG vs elsewhere.
2. **10-Q (~May 5) MD&A scan** — 30 min. Verify near-zero classified in CIB / Community Banking / Indirect (the non-RESG blind spot). Also watch for written Fund Finance pullback disclosure — does the asymmetry persist?

**Carryover (unchanged):**

3. Thread 3 roll execution check (carryover from AM + prior sessions).
4. Root REGINALD STATUS.md pruning (572+ lines). ~20 min.
5. Checkpoint 1 KB persistence for rows 178-184 + 3 PREDICTIONS (REG-21/22/23) — flagged in AM session. **Now superseded?** Rows 178-185 were added Apr 22-23; rows 186-192 added this session. Verify no orphans before acting.
6. KB_INDEX.md refresh (60 min) — deferred housekeeping.
7. B1 Boston Life Sci $169M MassLandRecords search (TODO #1) — tractable external lookup (Session 2 Tier B from today's plan).
8. B2 "The Jack" King County records (TODO #7) — paired Session 2 item.
9. May $47.5P × 2 decision by May 8 (position TODO P1).
10. WAL Round 2 if supplement/transcript delivered.

**Ask of Will:** No new ask this session. Q4 24 / Q1-Q4 25 Mgmt Comments extracts already live in `OZK/historical/`.

**Positions unchanged** — no broker data this session.
