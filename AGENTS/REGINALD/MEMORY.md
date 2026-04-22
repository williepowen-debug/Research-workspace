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

⚠️ **Open question:** Persistence debt is the blocker — three completed threads (IQHQ_SECONDARY_EXPOSURE, CIB_MARGIN_COMPRESSION, RESG_MIX_DETERIORATION) are on-disk but NOT yet integrated into KB.tsv, PREDICTIONS.tsv, or THESIS.md. Checkpoint 1 (7 KB rows + 3 PREDICTIONS) and Checkpoint 2 (create `OZK/CHANGELOG.md`, v1.1 bump on THESIS.md) are queued. Thread 3 options roll math (May 8 deadline) remains the hard-deadline priority.

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py)*

### LAST SESSION (Apr 22 midday — transcript deep dive + 3 parallel Opus threads)

**Boot:** Will back post-Q1 prints. OZK $48.52 → $47.56 (-1.98% intraday). WAL $77.83 → $80.21 (+3.06% reversal back above $78) — divergence trade playing out on the tape, STATUS post-print framing stale by noon.

**Main work: read OZK Q1 transcript (250 lines), surfaced 10-item investigation menu, ran top 3 🔴 threads in parallel as Opus 4.7 agents.**

**Thread A → `OZK/IQHQ_SECONDARY_EXPOSURE.md` (verdict: NO EVIDENCE)**
- Triggered by Gleason's "any other project with IQHQ" phrasing on Apr 22 call (line 213).
- **Killshot: Michelle Rossow (OZK Chief Comms Officer) to Bisnow 3/19/26:** "We have one credit with IQHQ, which is the senior secured loan on their San Diego RaDD project."
- Disconfirmation map for IQHQ sister properties: Fenway→JPM $165M, Arbor→KKR $581M, Spur→Apollo $275M, Brighton→Citizens $486.5M, 109 Brookline→assumed from Equity Commonwealth 2020.
- **Material correction:** Boynton Yards Somerville is NOT IQHQ — sponsor is Leggat McCall + DLJ + Deutsche Finance America. OZK $246M to Leggat McCall. **Firms SEVEN_CREDIT §2 #5 Candidate B for $169M Boston Life Sci.**
- Gleason quote read as defensive re: Aimco suit, not a signal of multiple credits.
- **IQHQ_PLAYBOOK weighted EL stands at $140M on $555M RaDD funded. No thread-3 duration change.**

**Thread B → `OZK/CIB_MARGIN_COMPRESSION.md` (verdict: VERTICAL-SPECIFIC, NET-NEUTRAL)**
- CIB $6.197B = 18.8% of loans (up from 9.7% Q1 25, 16.3% Q4 25) — growing very fast.
- 3/6 verticals (ABLG, Fund Fin, LFG) compressing; defense is rotation to CBSF/NRG/EFG, not pricing power.
- "+12bp new-vs-legacy" is a mix metric, not a broad lift.
- NIM 4.20% Q1 (-11bp YoY, flat QoQ); loan yield 7.24% (-55bp YoY, -26bp QoQ); deposit cost 3.29% (-49bp YoY).
- Securities build $1.44B Q1 is NIM-dilutive → why NIM held flat despite deposit-cost relief.
- Franchise Capital Solutions launched Q1 — no disclosed size/team/targets; implied <$50M.
- **2026 NIM path:** 4.20% plausible flat-rate; **4.10-4.15% drift more likely**. Confirmatory but not decisive — IQHQ Aug + RESG criticized remain higher-beta catalysts.
- Figure 17 p.17 ambiguity flagged — bar mapping to verticals not fully extractable.

**Thread C → `OZK/RESG_MIX_DETERIORATION.md` (verdict: CONFIRMED, 2Q window — the biggest find)**
- Problem-category share (Office + LS + Land + Hotel) **27.1% → 29.6% of RESG in ONE quarter (+250bps QoQ)**.
- Life Sci +190bps (10.7%→12.6%, +$0.4B absolute). Office +80bps (12.8%→13.6%).
- Multifamily $7.9B→$7.6B absolute decline; % flat only because total RESG shrank.
- Total RESG $29.0B→$27.7B (down from $34.5B Mar 2024 peak).
- **8Q forward:** problem share → 36.4% if MF runoff continues at observed pace with zero new problem originations.
- Denominator collapse alone adds 5-10bps to NCO rate → **50bps FY guide only holds in base scenario**.
- **Data gap:** Q1 24 / Q1 25 / Q2-Q3 25 Mgmt Comments PDFs needed for 8Q history. OZK IR 403'd all scripted pulls — Will needs to browser-pull.
- Possible Q4 25 Hotel/Land transposition in REGINALD 10-K extract ($0.1B Hotel vs Q1 26 $0.8B) — flagged for verification.

**Architectural decisions made this session (now in Feedback):**
- **Thesis architecture pattern:** THESIS.md carries "synthesis + pointer" (2-3 sentences + headline number + → sub-doc), not duplicated detail. Sub-docs hold the deep math. Changelog tracks THESIS.md only.
- **Per-bank CHANGELOG:** OZK needs own `OZK/CHANGELOG.md` mirroring master `thesis/CHANGELOG.md` format. Authorized creation — deferred to next session as part of Checkpoint 2.

**Files created this session:**
- `OZK/IQHQ_SECONDARY_EXPOSURE.md` — NEW (~625 words)
- `OZK/CIB_MARGIN_COMPRESSION.md` — NEW (~880 words)
- `OZK/RESG_MIX_DETERIORATION.md` — NEW (~950 words)
- `OZK/OZK 2026 Q1 data/` — 3 new PDFs from Will (Financial Supplement + Management Comments + short-form Fin supp)
- `MEMORY.md` — this rewrite

**Intentionally deferred (Checkpoint 1 + 2, next session):**
- Checkpoint 1: Append 7 KB rows (KB-OZK-178 through 184) + 3 PREDICTIONS rows; update SEVEN_CREDIT_DEEP_DIVE §2 #5 (Leggat McCall Candidate B HIGH confidence); one-line update on IQHQ_PLAYBOOK noting Rossow sole-exposure confirmation. ~20 min.
- Checkpoint 2: Create `OZK/CHANGELOG.md` with v1.1 entry; add version header to `OZK/THESIS.md`; update THESIS.md body (remove 1.18% NCO leading-indicator framing, add 3rd leading indicator = mix-shift, add 2-3 sentence synthesis of IQHQ_PLAYBOOK and SEVEN_CREDIT with pointers, note RaDD sole OZK-IQHQ exposure). ~30 min.

### NEXT SESSION — Checkpoints, then Thread 3

**Boot:** standard + read this MEMORY carefully + pull recent OZK docs (STATUS, THESIS).

**Sequence:**

1. **Checkpoint 1 — persistence (~20 min):**
   - Append KB-OZK-178 through 184 to `OZK/workbook/KB.tsv`:
     - 178: Rossow IQHQ sole-exposure quote (Bisnow 3/19/26)
     - 179: Leggat McCall = 808 Windsor/Boynton Yards $246M (firms SEVEN_CREDIT §2#5 Candidate B)
     - 180: CIB 3/6 vertical compression (ABLG/FundFin/LFG); rotation to CBSF/NRG/EFG
     - 181: CIB Q1 2026 NIM decomp (4.20% / -11bp YoY / loan yield 7.24% / -55bp YoY)
     - 182: RESG problem-category share +250bps QoQ (27.1%→29.6%)
     - 183: Hamblen MF-heaviest-runoff admission (transcript line 183-185)
     - 184: Forward projection mechanics (8Q → 36.4% problem share at observed MF runoff)
   - Append 3 new PREDICTIONS rows: Q4 2026 problem-category ≥32%; FY 2026 NCO ≥60bps; Q4 2026 classified/RESG ≥3.8%
   - Update `OZK/SEVEN_CREDIT_DEEP_DIVE.md` §2 #5 → Candidate B (Leggat McCall / 808 Windsor) HIGH confidence; Candidate A (US2 / 10 Prospect St) downgrade
   - One-line update on `OZK/IQHQ_PLAYBOOK.md` citing Rossow quote as sole-exposure confirmation

2. **Checkpoint 2 — thesis + changelog (~30 min):**
   - Create `OZK/CHANGELOG.md` — header, versioning convention, v1.1 entry (draft in Will+Claude chat Apr 22 session)
   - Add `v1.1 — Updated 2026-04-22` header to `OZK/THESIS.md`
   - THESIS.md edits: (a) correct NCO framing (1.18% was vintage-specific Q4, Q1 0.57% in-line); (b) add 3rd leading indicator = mix-shift; (c) 2-3 sentence syntheses of IQHQ_PLAYBOOK ($140M EL / 68% prob $140M+ event) and SEVEN_CREDIT ($719M problem book / $628M ACL / 2.2-3.0x coverage today); (d) RaDD = sole OZK-IQHQ exposure

3. **Thread 3 — options roll math (May 8 hard deadline):**
   - Same exec plan as prior MEMORY (4 candidate rolls, delta/vega/P&L grid by scenario, recommend single roll)
   - Benefits from Checkpoint 2 (updated scenario weights)

**Ask of Will (cheap, high-value):** Browser-pull Q4 24 / Q1 25 / Q2 25 / Q3 25 OZK Management Comments PDFs from ir.ozk.com/filings/documents/ — gives 8Q history for mix-shift trajectory (Thread C currently limited to 2Q window, scripted pulls 403'd).

**Other carryovers:**
- `OZK/STATUS.md` focused refresh (still stale since Apr 7 — ~45 min)
- Root `STATUS.md` pruning (572+ lines, Apr 7/9/10 briefs → archive)
- WAL Round 2 (awaits WAL supplement/transcript)
