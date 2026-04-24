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

⚠️ **Open question:** Step 5 of OZK spinout — create `AGENTS/OZK/MEMORY.md` (move OZK-specific rows from REGINALD/MEMORY.md + duplicate cross-cutting Will feedback per D2=A). Spec in plan §4a.

⚠️ **NEXT SESSION PRIORITY #1 (updated 2026-04-24 PM): RESUME OZK SPINOUT at Step 5.**

**Plan doc is the source of truth:** `AGENTS/REGINALD/OZK_SPINOUT_PLAN.md` (rev 3, decisions locked).

**Steps 1-4 complete (commits in this session):**
- Step 1 ✅ `git mv AGENTS/REGINALD/OZK → AGENTS/OZK` — 131 files, pure rename. Commit `29df4f6d`.
- Step 2 ✅ 3 cross-boundary `../` refs fixed in OZK/INDEX.md, TODO.md, STATUS.md. **Judgment call:** STATUS.md:65 "Full cross-bank calendar → ../CALENDAR.md" pointer was *dropped entirely* rather than mechanically swapped (plan said swap to local; semantics didn't match — Will's call: drop). Commit `df333272`.
- Step 3 ✅ Checkpoint verification passed — OZK tree intact at new path, REGINALD/OZK gone, intra-OZK `../` refs resolve, self-fixing `../../BROCK/STATUS.md` now points at real file. Dangling MEMORY.md / CALENDAR.md refs expected until Steps 5-6.
- Step 4 ✅ `AGENTS/OZK/CLAUDE.md` written — 247 lines, BROCK-modeled, OZK-scoped. Commit `f99bc4c8`.

**Current state:**
- `AGENTS/OZK/` exists at top level alongside BROCK/CARL/etc. Has CLAUDE.md.
- Still missing: MEMORY.md, CALENDAR.md, LESSONS.md, POSITIONS.md, TRADE.md, inbox/, outbox/.
- REGINALD-side `OZK/` references NOT yet updated (that's Step 11).
- Root CLAUDE.md agent list NOT yet updated (Step 12).

**Context for next session:**
- SAM was actively working during this session (grew from 5 → 12 modified files in `AGENTS/SAM/`). Git hygiene: strict path staging only, never `git add .`. SAM may have pushed by next session — follow pull protocol.
- Will handles position decisions himself; no tape/exit analysis self-directed.
- Plan had one inconsistency I worked around: §5's optional `../REGINALD/MEMORY.md` boot step conflicts with §8 D2=A "local only". I kept it as "Situational, not routine" in OZK/CLAUDE.md. If Will prefers strict removal, one-line edit.
- Will's preferred rhythm: ask before each commit, stop at checkpoints (Steps 3 and 13).

**On boot:** normal boot sequence, then ask Will "ready to start Step 5 (OZK/MEMORY.md)?"

See auto-memory `project_ozk_spinout_direction.md` for persistent direction.

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py)*

### LAST SESSION (Apr 24 PM — OZK spinout Steps 1-4)

Executed first 4 steps of the 16-step spinout plan. Three commits all pure/additive — no content drift, no REGINALD edits yet (Step 11 does those). Pre-boot Apr 23 PM session notes about the $495M gap / Jack & Boston resolutions are still relevant research context and carry forward into the OZK agent's memory via Step 5.

### NEXT SESSION — RESUME AT STEP 5

Steps 5-10 create the remaining OZK agent infrastructure (MEMORY, CALENDAR, LESSONS, POSITIONS, TRADE, inbox/outbox). All specs in plan §4 + §5. Checkpoints at Step 13.

**Positions unchanged** — no broker data this session.
