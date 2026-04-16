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

## Findings
- [2026-04-02] `scripts/market.py` pulls live prices via yfinance. Watchlist covers all thesis tickers + Brent (BZ=F). Must run with `.venv/bin/python3`. Added to boot step 5.
- [2026-04-02] FRED API key not configured — HY OAS, claims, and other FRED series at boot require `FRED_API_KEY` env var. Low priority but would close data gap.
- [2026-04-02] OZK price sources can conflict ($46 vs $49 in same session) — always verify at broker when discrepancy >5%.
- [2026-04-02] SAM's architecture is the best-organized agent. All key patterns now adopted: doc ownership rules, CALENDAR.md, MEMORY.md, branch point table in TIMELINE.md, session close checklist.
- [2026-04-02] PROME's SCRATCH.md is useful for system-wide context at boot — but REGINALD should not routinely read it. Only check if cross-agent context is needed.
- [2026-04-02] Inbox signals from HERMES can lag behind STATUS.md — check for staleness before processing.
- [2026-04-12] FDIC EFR system: efr.fdic.gov/fcxweb/efr/ — OZK Form 3/4/5 filings live HERE, not on SEC EDGAR. FDIC cert #110. Standard insider tools miss OZK.
- [2026-04-12] OZK IR page: ir.ozk.com/filings/documents/ — cross-posts FDIC filings but was inaccessible programmatically (timeout). Will can access via browser.
- [2026-04-12] Wasatch fund commentaries: wasatchglobal.com/wp-content/uploads/strategy-and-fund-documents/ — quarterly fund PDFs. OZK held in Small Cap Value, Long/Short Alpha. Dropped from Core Growth.
- [2026-04-16] MTB 10-K filed Feb 18, 2026 (CIK 36270, accession 0000036270-26-000010). PDF saved locally as `MTB/sources/DFIN EZBlue 2.24.26.pdf` (not committed — 4.5MB). Can be re-fetched from EDGAR with User-Agent header.
- [2026-04-16] MTB fund banking built by Michael Sinclair at People's United (2018), NOT acquired from Webster Bank. CFO Bible misspoke on Q1 call. See `MTB/WEBSTER_ANOMALY.md`.
- [2026-04-16] pdfminer works for PDF text extraction (`.venv/bin/python3`). poppler-utils not installed (needs sudo). Use pdfminer for all PDF reads.

## References
- [2026-04-02] FRED API key signup: https://fred.stlouisfed.org/docs/api/api_key.html
- [2026-04-02] EDGAR CIK for OZK: 0001569650 (for 8-K monitoring)
- [2026-04-16] EDGAR CIK for MTB: 0000036270
- [2026-04-16] Cadwalader Fund Finance Friday — tracks fund banking personnel and deals. Profiles of MTB's Sinclair in Issues Nov 2018, Dec 2020, May 2023.

## Session Notes

⚠️ **Open question:** CFG deck Slide 24 introduced an "ABS finance" $1.8B line item that has no equivalent in the 10-K Table 14. Is this a new product or a reclassification from existing C&I? Pulling the FY2024 10-K from EDGAR would test whether ABS finance existed previously — bigger reclassification signal than the original 5% vs 40% question.

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py)*

### LAST SESSION (Apr 16 — CFG Q1 earnings, thesis v1.4, deck mining)

**[Apr 16 Round 2 — accidental respawn, mined CFG deck]**
- Mined `CFG/sources/CFG-earnings-presentation-4-16-26.pdf` (was unread in Round 1)
- Slide 24: $14.7B Private Capital + $4.9B other = $19.6B preliminary NDFI. Disclosure exists in deck only — NOT press release/supplement
- New "ABS finance" $1.8B line item — no 10-K Table 14 equivalent. Possible reclassification.
- 5% vs 40% partially resolved: capital call + PC finance growing ~2.85% QoQ ≈ 11.9% annualized. Trajectory moderated.
- Slide 23 confirms hiding place: capital call + PC finance itemized inside C&I "Finance and Insurance" $13.3B bucket
- Slide 26: ACL release headline (1.53→1.52%) masks Commercial building (+6bps both C&I and CRE), Retail releasing
- Slide 27: Mortgage 90+ accruing UP 0.40→0.51%; FHA/VA/USDA-guaranteed bucket growing ($141M→$179M). CARL FHA stress touches CFG
- **Files updated:** CFG/STATUS.md (3 edits — verdict #3, new DECK FINDINGS section, Priority 6), parent STATUS.md (2 edits — sector tone table + opacity bullet), MEMORY.md
- **Behavior change:** WAL/OZK earnings decks must be mined alongside press release on Apr 21 — pattern shows decks contain disclosure absent from headlines

**[Apr 16 Round 1 — original CFG session]**

**CFG Q1 fully integrated (earnings release + supplement + transcript):**
- `CFG/STATUS.md` — post-earnings dashboard with all Q1 actuals, transcript mining, discrepancy analysis, three-layer C&I framework
- `CFG/sources/` — Q1 transcript uploaded by Will, plus earnings PDFs

**Key CFG findings:**
1. CRE nonaccruals +10% QoQ ($618M→$679M) while CRE balance fell 1% — extend-and-pretend confirmed
2. FHLB 60x YoY ($42M→$2,513M) — prior 10-K assessment of "declining, not stressed" was WRONG
3. Zero fund finance disclosure in press release or supplement — total opacity on $12.5B book
4. 5% vs 40% growth discrepancy — Van Saun + Ted claim "5%/yr" NBFI growth, 10-K shows 39.7%. Likely reclassification (same pattern as MTB)
5. Two analysts asked about private credit (Siefers/Piper, Chiaverini/Jefferies) — first time ever, was zero in Q4
6. Van Saun acknowledged screening counterparties for "liquidity gates" — first gating risk acknowledgment
7. PE line utilization DOWN — contradicts Q4's "pickup." Draws not accelerating at CFG. Partial thesis disconfirmation.
8. AOCI: CET1 10.5% → 9.3% after adjustment. $1.97B unrealized losses.
9. Consumer improving: retail NCO 38bps (from 70bps YoY). CARL channel NOT confirming at CFG.
10. Capital return 96% ($498M vs $517M earned). Buybacks tripled QoQ.

**Thesis v1.4 (new):**
- Added "C&I as Convergence Hiding Place" to thesis/THESIS.md — three masking mechanisms (MI3, NDFI opacity, reclassification) all exploit C&I bucket
- Core insight: the convergence isn't just eight channels hitting the same banks — it's eight channels hiding in the same bucket
- CFG research + MTB cross-reference provided the evidence base

**Parent STATUS.md updated (carry-forward from last session resolved):**
- Q1 earnings wave sector tone tracker (2/2 bear-leaning)
- FHLB upgraded 🟠→🔴
- WAL threshold: back above $78 ($78.23)
- CFG convergence score: 9→12

**Files updated:** CFG/STATUS.md, thesis/THESIS.md (v1.4), thesis/CHANGELOG.md, STATUS.md (parent), CALENDAR.md, MEMORY.md
**Git:** 1 commit pushed to GitHub. CFG source PDFs local only (not committed). Transcript committed.

### NEXT SESSION
1. **KEY earnings (Apr 16)** — results should be available. Consumer credit, provisions, NIM. Lower priority.
2. **RF earnings (Apr 17)** — consumer DQ, CLO marks. No file built.
3. **CFG earnings deck** — `CFG/sources/CFG-earnings-presentation-4-16-26.pdf` unread. May have fund finance slides (Table 14 equivalent). Mine it.
4. **Resolve 5% vs 40%** — pull FY2024 10-K from EDGAR, check if "capital call facilities" existed as Table 14 line item. Quick test of reclassification hypothesis.
5. **WAL + OZK earnings prep (Apr 21)** — position names, 5 days out. Synthesize MTB + CFG read-throughs. Refresh earnings prep files.
6. **Inbox:** 4 signals unprocessed (OTTO Tricolor + 3 WALTER). Process when spawned for it.
7. **Signal to WALTER:** Sector tone read-through from MTB + CFG. Draft after KEY/RF complete the early wave.
