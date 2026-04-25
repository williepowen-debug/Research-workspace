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

## References
- [2026-04-02] EDGAR CIK for OZK: 0001569650 (note: most insider Form 3/4/5 filings live on FDIC EFR, not SEC — see Findings)
- [2026-04-22] OZK IR docs: `ir.ozk.com/filings/documents/` — cross-posts FDIC + SEC filings. Quarterly: Financial Supplement + Management Comments (separate PDFs) + transcript. Will can pull via browser when WebFetch 403/timeouts block.

## Session Notes

⚠️ **Open question:** KB_INDEX rollup **Phase 2** — architectural decision: (a) Do SELLSIDE / SHORT_INTEREST / FAILURE_COMP warrant a new "Market Evidence / Precedent" layer in the index, or cross-cut into existing layers? (b) Rule for single-row groups — fold into parent cluster (KB.tsv retag) or keep standalone? Decision-only, no writing. Phases 3 + 4 blocked on this. Full plan in TODO.md §H1.

**CHANGES SINCE:** *(leave blank — next boot populates via market.py price delta check)*

### LAST SESSION (2026-04-24, second OZK session)

- **Doc cleanup batch.** Fixed INDEX.md positions (× 1 → × 3, + missing $47.5P May × 2 line); Q1_2026_ANALYSIS.md header (REGINALD → OZK); research/README.md removed Feb25 row (file in archive/, not research/); shrunk TRADE.md 93 → 40 lines (Will approved Option 2 — kept conviction thesis + anti-trade warning, dropped Mar 7 earnings playbook + position assessment). Commit `ee0d599c`.
- **KB_INDEX rollup — 6-phase plan documented in TODO.md §H1.** Will approved phasing. Each phase bounded, with own commit, no judgment carried forward without approval. Two phases shipped this session.
- **Phase 1 done.** Header 159/17 → 195/28; naming-drift merge EXTEND_AND_PRETEND → EXTEND_PRETEND (KB.tsv row 176 retagged); LIFE_SCI range 21→26; GEOGRAPHY range 13→15; EXTEND_PRETEND range 8→9. Commit `93655ad0`.
- **Phase 5 done.** Quick Lookup replaced "By earnings prep (Apr 16)" → "By 2026 catalyst" (May Call Report / Jul Q2 / Aug IQHQ / Oct sub notes + Affinius). Standalone Research +3 post-Q1 threads (CIB_MARGIN_COMPRESSION, IQHQ_SECONDARY_EXPOSURE, RESG_MIX_DETERIORATION). Commit `8bd512dc`.
- **Phase 2-4 + 6 remain.** Phase 2 (15 min decision) blocks 3 + 4. Phase 6 closes after 3+4. Single next session can cover the lot (~60-80 min).
- **Other agents active in tree mid-session.** REGINALD modified STATUS.md + workbook/PREDICTIONS.tsv (parallel session — flagged to Will, didn't touch). WALTER touched STATUS + filter/route logs; BOARD added 13 SIG-W files + INDEX. All non-OZK paths left untouched. My commits passed pre-push sanity check (`git diff origin/master..HEAD --name-only | grep -v '^AGENTS/OZK/'` → empty).
- **STATUS.md price refresh at boot:** $47.59 → $47.47 (-0.25%, no threshold breach). Regional cohort idio-red on a green tape day (SPY +0.77%, QQQ +1.91%) — divergence noted, not OZK-specific.

### NEXT SESSION

1. **KB_INDEX rollup Phase 2** (~15 min, decision-only) — settle SELLSIDE layer + single-row rule. See TODO.md §H1.
2. **KB_INDEX rollup Phase 3 + 4** (~45 min, after Phase 2) — multi-row cluster rollup + single-row reconciliation. Can co-execute.
3. **KB_INDEX rollup Phase 6** (~10 min, after 3 + 4) — audit close.
4. **Refresh `THREAD3_ROLL_MATH.md` chain quotes** — May 8 deadline now ~14 days out. Priority if Will signals roll execution.
5. **Check REGINALD_CHANNEL on boot** for any new entries since 16:40 ET 2026-04-24 (REGINALD ran parallel session this session — may have written).

### Prior note (pre-spinout seed): Initial Session Notes (2026-04-24, REGINALD migration session)

OZK spun out from REGINALD sub-scope to top-level peer agent at `AGENTS/OZK/`. See `archive/OZK_SPINOUT_PLAN.md` for full migration plan. MEMORY.md seeded per plan §4a (6 Findings + 2 References moved, 1 Finding copied, 9 cross-cutting Will feedback rows + 2 shared tool findings duplicated). Boot test now complete — first genuine session above.
