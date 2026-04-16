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

⚠️ **Open question:** Does MTB's Q2 provision continue building (>$150M while NCO stays low)? Two consecutive quarters of reserve builds ahead of losses would confirm the "managed deterioration" thesis and move MTB from WATCH toward position candidacy.

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py)*

### LAST SESSION (Apr 15-16 — MTB full build, crash recovery)
**Crash recovery:**
- Session started with unclean shutdown. Recovered `MTB/NON_BANK_EXPOSURE.md` (18KB, intact on disk). Git diverged 14 local / 3 remote — OTTO resolved conflicts in parallel session. Full rebase + push completed.

**MTB Tier 3 architecture built (6 files):**
- `STATUS.md` — post-earnings dashboard, all Q1 actuals integrated, all gaps closed
- `EARNINGS_Q1_2026.md` — canonical record from transcript + deck + release + 10-K
- `NON_BANK_EXPOSURE.md` — NDFI deep-dive (pre-crash, recovered)
- `THESIS.md` — position candidacy at WATCH (25% conviction), 8 upgrade triggers
- `WEBSTER_ANOMALY.md` — resolved: CFO misspoke, fund banking from People's United
- `WAREHOUSE_COUNTERPARTY.md` — 10-K NDFI analysis, Bayview deep-dive, Tricolor trustee

**Key MTB findings (chronological discovery):**
1. Provision $140M (+12%) while NCO fell 31bps — forward-looking reserve build
2. NDFI commitments $23.9B (2x the $12.5B outstanding) — $11.4B contingent
3. Bayview is massive: $984M lending + $3.5B deposits + $157B servicing + $224M revenue, all growing 40-80% YoY
4. Zero counterparty disclosure — WORSE opacity than WAL (no exhibits filed)
5. 100% of Q1 NDFI growth in mortgage credit intermediaries ($5.6B→$6.5B) — riskiest bucket
6. NCO FY guide 40bps (Q1 was 31bps) — mgmt telegraphing deterioration
7. FHLB period-end $7.85B (+265%), tripled in one quarter. 190bps cost premium.
8. Capital return 228% of earnings. Buyback avg ~$255 vs $207 close — overpaid.
9. FHA/VA 90+ DPD $634M (+72% YoY). Expanding FHA subservicing into deteriorating pool.
10. Office CRE $3.4B, 22.3% criticized. $7.9B CRE matures 2026. Criticized LTV eroding (67% from 63%).

**Assessment:** MTB is "managed, not steady." Classical metrics strong but NDFI opacity, Bayview concentration, FHLB draw, reserve build, and extend-and-pretend ($818M) tell a different story than the confident call tone. WATCH at 25%, revisit after Q2.

**Files updated:** STATUS.md (parent REGINALD — NOT updated this session, carry forward)
**Git:** 4 commits pushed to GitHub. Source PDFs local only (not committed).

### NEXT SESSION
1. **Update parent REGINALD/STATUS.md** with MTB sector-tone read — this was not done this session
2. **CFG earnings (Apr 16)** — $10-11B BDC + $12.5B fund finance. MTB's disclosure template predicts CFG will give aggregate comfort without counterparty names. Watch Table 14 fund finance balances, C&I NCO inflection.
3. **KEY earnings (Apr 16)** — office NPLs, NIM, consumer. Lower priority read-through.
4. **RF earnings (Apr 17)** — consumer DQ, CLO marks. No file built.
5. **WAL + OZK earnings prep (Apr 21)** — position names. All MTB read-through signals should be synthesized by then.
6. **Inbox:** 3 WALTER signals unprocessed (TCW/Red Lobster, Road-to-Housing, DB financials). Process when spawned for it.
7. **Signal to WALTER:** Sector tone read-through for WAL/OZK/EGBN/CFG from MTB findings. Draft but don't send until parent STATUS updated.
