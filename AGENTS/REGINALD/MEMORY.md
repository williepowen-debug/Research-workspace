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

⚠️ **Open question:** Has Will executed the Thread 3 roll yet? Recommendation (per `OZK/THREAD3_ROLL_MATH.md`) is to close May $42.5P × 2 + open Jan27 $42.5P × 2 (~$510 debit). Hard deadline ~May 8 for decision. This session (Apr 23) focused on OZK file-tree restructure + thesis self-audit; roll execution not addressed.

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py)*

### LAST SESSION (Apr 23 morning → afternoon — OZK restructure + thesis audit)

**OZK file tree restructure, 4 phases, 4 commits:**
- **Phase 1** (`9a2d05ee`) — 4 top-level orphans → archive/ (AUDIT_MAR25, TEMPLE8, INSTITUTIONAL_OWNERSHIP_PLAN, EXTERNAL_PROMPTS). Top-level 15 → 11.
- **Phase 2** (`80e8eeba`) — `sources/` 50+ → 10 primary-source extracts. `OZK 2026 Q1 data/` renamed `raw/` with snake_case PDFs (Q1_2026_mgmt_comments.pdf, etc.). 30 LLM outputs → `raw/llm_outputs/`. 15 V1-V3 drafts deleted (~2,700 lines). 74 files changed.
- **Phase 3** (`23e28087`) — `MARKET/` archived entirely (abandoned Mar 24, superseded by darkpool/short_vol tools). `GEOGRAPHY/FL_PARADOX/` flattened 5 files → single `GEOGRAPHY/FL_PARADOX.md`. Subdomains 5 → 4.
- **Phase 4a** (`d58b2b92`) — INDEX.md refresh. Storage-tier contract documented in footer (sources/raw/raw-llm_outputs/historical/archive semantics).

**OZK thesis self-audit, 5 fixes, 2 commits:**
- **Audit commit 1** (`d45c8bcc`, v1.1 → v1.2) — INVALIDATION section added to THESIS.md (5 concentrated kill criteria with thresholds + cross-refs to REG-22/23 + IQHQ_PLAYBOOK). WEAKNESSES.md C5 retracted and corrected (was still saying "IQHQ pushed to 2028" — directly contradicted THESIS Aug 2026 Wave 3 framing).
- **Audit commit 2** (`9322e2cc`, v1.2 → v1.3) — Q1 NCO deceleration engaged in ACL Thinning section (new paragraph acknowledging 0.57% in-line with guide, connecting to Invalidation §2). Two unverified claims removed: KB-OZK-061 ($13.8B quarterly origination breakdown) and KB-OZK-062 (DBRS 3.4yr time-to-default). SCENARIOS.md first reweight since Mar 23: Bear 50→55%, Bull 15→12%, Tail 5→3%, Base 30% unchanged. New EV $38.97 (vs $37.45). April 16 Decision Framework retracted, replaced with Post-Q1 Decision Gates.

**Final OZK map:** 11 top-level .md (was 15) | 4 subdomains (LIFE_SCI, GEOGRAPHY, INSIDERS, PRIVATE_CREDIT) | clean 3-tier storage (sources/raw/historical) | archive/ quarantined | zero broken cross-refs verified at each phase.

**Pushed to GitHub:** All 6 commits live. Session total 7 with the earlier session-close commit.

**What I did NOT do this session:**
- Thread 3 roll execution check (unchanged from prior carryover)
- Checkpoint 1 persistence (KB-OZK-178 through 184 + 3 PREDICTIONS) — still queued
- Root REGINALD `STATUS.md` pruning (572+ lines) — still queued
- OZK/STATUS.md refresh (still dated Apr 7, pre-earnings) — known flag from audit
- PRIVATE_CREDIT/ post-Q1 refresh (Mar 24 data, missing Jake Munn Fund Finance pullback)
- WAL Round 2

### NEXT SESSION — priorities by urgency

1. **Thread 3 roll execution check.** Did Will close May $42.5P × 2 → open Jan27 $42.5P × 2? Update POSITIONS.md + IQHQ_PLAYBOOK §6 after broker confirmation. If not yet executed, re-quote the chain (May premium decays fast; hard deadline ~May 8).

2. **Checkpoint 1 — persistence (~20 min):** Append KB-OZK-178 through 184 to `OZK/workbook/KB.tsv` + 3 PREDICTIONS rows (REG-21/22/23). Detail list same as prior memo — see `OZK/CHANGELOG.md` v1.1/v1.3 for KB row contents.

3. **OZK/STATUS.md refresh (Phase 4b, known audit flag).** File is dated Apr 7 pre-earnings. Current stock $47.52; needs Q1 26 actuals (past-due $465M / 1.41%, NCO 0.57%, CET1 11.64%, TBV $47.15) + current position table + updated catalyst calendar (IQHQ Aug 2026, sub notes Oct 1). ~15 min.

4. **Root REGINALD STATUS.md pruning** — 572+ lines. Apr 7/9/10 briefs → archive/ (~20 min).

5. **PRIVATE_CREDIT post-Q1 refresh** — 5 files dated Mar 24. Jake Munn Q1 call disclosed OZK pulling BACK from Fund Finance capital-call subscriptions (non-bank lender + insurance competition). This is material data that directly contradicts the "regionals pressing into NDFI for growth" narrative at OZK specifically. Needs integration into STATUS.md + TRANSMISSION.md + COUNTERPARTY_WATCH.md. ~30-45 min.

6. **WAL Round 2** if supplement/transcript delivered.

**Ask of Will — still open / historical:** Apr 22 ask for browser-pull of Q4 24 / Q1 25 / Q2 25 / Q3 25 OZK Management Comments PDFs — FULFILLED. All 5 quarterly extracts live in `OZK/historical/` (Q4 24 through Q4 25). No new ask this session.

**Note on POSITIONS.md:** Root REGINALD POSITIONS.md not touched this session — no broker data received. Current known positions (per STATUS top): WAL $85P/$77.5P/$70P/$65P (Jun/Sep), OZK $42.5P May15 × 2 (rolling), $42.5P Aug21 × 1, $45P Aug21 × 4, EGBN $25P Jun, SSB $90P Jun, FLG $13P Jul, ZION $57.5P Jul (monitor only), plus KRE/IWM/HYG macro hedges.
