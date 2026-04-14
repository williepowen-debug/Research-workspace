# REGINALD MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis or delete, never just accumulate. For verified mistake patterns with prevention rules, see `LESSONS.md`.*

---

## Feedback
- [2026-04-02] Will values boot transparency — wants to know what REGINALD read, in what order, and whether the process is working. Don't orient silently; confirm orientation.
- [2026-04-02] Will prefers sessions to have freedom rather than being laser-focused on pre-set priorities. Provide context, not directives. Rejected ranked TOP 3 queue in favor of a single "open question."
- [2026-04-02] Will thinks long-term about infrastructure. When proposing solutions, address scaling and durability, not just immediate need.
- [2026-04-02] Will wants position data stored in REGINALD's domain (POSITIONS.md), not just FORGE. "That was just for you."
- [2026-04-02] Will prefers breaking large implementation work into discrete tasks done one at a time, with approval between each.

## Findings
- [2026-04-02] `scripts/market.py` pulls live prices via yfinance. Watchlist covers all thesis tickers + Brent (BZ=F). Must run with `.venv/bin/python3`. Added to boot step 5.
- [2026-04-02] FRED API key not configured — HY OAS, claims, and other FRED series at boot require `FRED_API_KEY` env var. Low priority but would close data gap.
- [2026-04-02] OZK price sources can conflict ($46 vs $49 in same session) — always verify at broker when discrepancy >5%.
- [2026-04-02] SAM's architecture is the best-organized agent. All key patterns now adopted: doc ownership rules, CALENDAR.md, MEMORY.md, branch point table in TIMELINE.md, session close checklist.
- [2026-04-02] PROME's SCRATCH.md is useful for system-wide context at boot — but REGINALD should not routinely read it. Only check if cross-agent context is needed.
- [2026-04-02] Inbox signals from HERMES can lag behind STATUS.md — check for staleness before processing.

## References
- [2026-04-02] FRED API key signup: https://fred.stlouisfed.org/docs/api/api_key.html
- [2026-04-02] EDGAR CIK for OZK: 0001569650 (for 8-K monitoring)
- [2026-04-12] FDIC EFR system: efr.fdic.gov/fcxweb/efr/ — OZK Form 3/4/5 filings live HERE, not on SEC EDGAR. FDIC cert #110. Standard insider tools (OpenInsider, Fintel, etc.) miss OZK entirely.
- [2026-04-12] OZK IR page: ir.ozk.com/filings/documents/ — cross-posts FDIC filings but was inaccessible programmatically (timeout). Will can access via browser.
- [2026-04-12] Wasatch fund commentaries: wasatchglobal.com/wp-content/uploads/strategy-and-fund-documents/ — quarterly fund PDFs. OZK held in Small Cap Value, Long/Short Alpha. Dropped from Core Growth.

## Session Notes

⚠️ **Open question:** Does WAL have material exposure to Apollo Atlas SP? If Apollo's Atlas SP warehouse book blows up on non-bank servicer stress, and WAL has any correspondent/syndicate participation in Atlas SP facilities, WAL has a back-door exposure we haven't priced. Also: who ARE WAL's actual warehouse counterparties? Today's research ruled out FHA-stressed public non-bank servicers; still unknown who the $9.2B is actually lent to.

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py + darkpool.py)*

### LAST SESSION (Apr 14 AM+PM — CARL warehouse signal integrated + deep counterparty pull)
**Morning (CARL signal initial integration):**
- CARL signal SIG-CARL-REGINALD-20260413 processed. Initial view: refines WAL V3 (SSFA/NDFI) from pure regulatory risk into dual regulatory + counterparty credit risk. MFS UK $669M Barclays template cited.
- Added FHN + TCBI to warehouse watchlist (FHN growing, TCBI doing SSFA-style capital arb).
- JPM Q1 earnings reviewed: beat headline, NII full-year guide CUT $1.5B. Dimon "increasingly complex risks."
- RITM Apr 28 added to CALENDAR.

**Afternoon (deep counterparty pull — Will manually pulled 10-Ks from SEC EDGAR):**
- Pulled PFSI FY2025, LDI FY2025, RITM FY2025, COOP FY2024 10-Ks (saved to `domain/sources/warehouse_counterparty/`).
- Saved as HTML, stripped tags via Python html.parser.
- **Key extraction technique:** Exhibit Index (10-K Item 15) names counterparties in amendment titles even when Note 12 tables anonymize. "Master Repurchase Agreement dated X among [BANK NAME] and [BORROWER]" — title contains full party list.
- Per-servicer counterparty disclosure:
  - PFSI: Note 15 fully transparent. $8.8B book. **Atlas SP (Apollo) = $6.9B = 78% concentration.** Plus BofA, RBC, JPM, Nomura, MS, Citi, Wells, BNP, Barclays, Mizuho, Goldman — each $7-90M.
  - LDI: Note 12 anonymized (Facility 1-11). Exhibit Index reveals: BofA (primary, "BA Warehouse LLC" SPV), JPM, Citi, Nomura, UBS, **Atlas SP (Nov 14 2024 entry)**, BMO (Apr 2025 new), U.S. Bank trustee.
  - RITM: Parent 10-K fully opaque. Only Goldman (historical Marcus acquisition) + U.S. Bank (trustee) in exhibits. Subsidiaries (NewRez etc.) file separately.
  - COOP: Note 12 anonymized. Exhibit Index: **Barclays dominant** (52 refs, going back to 2011 Nationstar era) + BofA, JPM, MS, Wells, Citi, Goldman. Flagstar appears but only as MSR BUYER (not warehouse lender).

**Critical finding:**
- **ZERO US regional banks** as warehouse counterparties across all 4 servicers examined.
- **CARL direct-regional-exposure thesis NOT SUPPORTED** by public 10-K counterparty data.
- **Transmission landing point = Apollo** (Atlas SP Partners, acquired Credit Suisse SPG 2023). This is the real "MFS UK template" target.
- APO now has NEW vector on watch stack (already tracked for MFS/First Brands/Epstein/Athene).

**Implications:**
- WAL V3 unchanged in size (~$9.2B SSFA mortgage warehouse book). Refined in framing: WAL's warehouse borrowers are NOT the FHA-stressed public non-bank servicers. They're other (unidentified) entities — smaller correspondent lenders, conventional GSE-focused originators, or non-mortgage NDFI (BDC lines, capital call facilities, CRE debt fund warehouse).
- WAL V2 (Jefferies/First Brands via Point Bonita, $126.4M disputed) remains the PRIMARY near-term exposure — unaffected by today's research.
- OZK unchanged — confirmed has ZERO SSFA and zero mortgage warehouse. NDFI book is CRE-only per CEO Gleason Q3 2025.

**Files created/updated:**
- `domain/WAREHOUSE_EXPOSURE.md` — rewrote as definitive synthesis (replaced AM version)
- `domain/sources/warehouse_counterparty/` — 4 10-K HTML files + parsed text files
- STATUS.md dashboard — replaced "Non-bank Servicer Warehouse" row with refined finding; added Apollo Atlas SP row
- `outbox/2026-04-14_to-CARL_warehouse-research-complete.md` — CARL pivot notification
- MEMORY.md open question updated to new gap (WAL's actual counterparty identity; Apollo Atlas SP exposure channel)
- **Git:** NOT YET COMMITTED — pending session close.

### LAST SESSION (Apr 12-13 — Hamblen + earnings week prep)
- **HAMBLEN FULL HISTORY (5 filings, FDIC EFR):** Aug 2024 transferred 60,142 shares → Family LP (estate planning vehicle). Jan-Feb 2025 sold 6,000 shares at $51-53 via LP (open market, Code S). Mar 2025 + Mar 2026 comp grants (net +57,523 after tax withholding). Zero open-market purchases ever. Updated SELLING.md with full transaction table.
- **COMPLETE C-SUITE INSIDER PICTURE:** Gleason (CEO) frozen since Jul 2023. Hamblen (President) zero purchases, LP sales at highs. Hicks (CFO) staged $944K selling. Majumdar (CRO) discretionary sell during reserve cuts. Kenny (Director) net seller. Whipple (Director) $5.2M exit at top. ZERO open-market purchases across entire leadership.
- **WELLINGTON FULL TRAJECTORY (WhaleWisdom, 13F):** 6-quarter history shows Q3 2024 peak 4.22M → Q4 2025 1.25M (-70.4%). Briefly re-entered Q2 2025 (+873K shares), immediately reversed with accelerating sells. Bounce-then-dump = reassessed and exited faster. Updated SELLING.md institutional section.
- **WELLINGTON N-PORT — DEAD END:** N-PORT filings are structured XML, not indexed by EDGAR text search. WhaleWisdom shows only 13F data for Wellington/OZK. No post-Dec 31 data available from any programmatic source.
- **SHORT INTEREST (yfinance, Mar 12 settlement):** OZK 15.28% SI unchanged (13.7 days to cover). EGBN 11.10% HIGH. WAL 0.06% (shorts fully covered). Shorts not flinching on OZK into earnings.
- **OZK EDGAR DISCOVERY:** OZK has filed ZERO 8-Ks on SEC EDGAR. All EDGAR filings under OZK CIK are institutional ownership (13F/13G) filed by OTHER investors. Same FDIC-only pattern as Form 4.
- **OZK EARNINGS CONFIRMED:** Apr 21 after market close, conference call Apr 22 7:30 AM CT. Source: GlobeNewsWire press release Mar 31. Fixed incorrect "Apr 16" references in STATUS.md.
- **EARNINGS READ-THROUGH FILES BUILT:**
  - MTB/STATUS.md — Created. Sector tone-setter. CRE/Tier 1 128% (3-4x less than our targets). $7.8B criticized CRE declining. NIM 3.67%. Earnings Apr 15.
  - CFG/STATUS.md — Updated existing (had excellent 10-K data from Mar 30). Added Q4 results, Q1 estimates, "What to Watch" section. $12.5B fund finance (+40% YoY), zero analyst questions. Earnings Apr 16.
  - KEY/STATUS.md — Created. Lower priority read-through. CRE 15%, credit improving, CET1 11.7%. Blackstone fund finance partnership new vector. Earnings Apr 16.
- **Git:** NOT YET COMMITTED — pending session close

### LAST SESSION (Apr 12 — institutional ownership + FDIC insider deep-dive)
- 13F analysis, FDIC EFR discovery, Kenny full history, Wasatch fund research, Gleason frozen confirmed.

### LAST SESSION (Apr 10 — automation toolkit + EGBN deep-dive)
- Automation toolkit built (8 scripts). EGBN continuity awards deep-dive. boot.py created.

### NEXT SESSION
**EARNINGS WEEK — priority by date:**
1. **Tuesday Apr 15 (MTB pre-market):** Listen for CRE provisions, NIM, criticized CRE trend, AOCI commentary. Update MTB/STATUS.md with actuals. Flag read-throughs to OZK/WAL. Also: listen for any NDFI / warehouse / mortgage-company-loan commentary.
2. **Wednesday Apr 16 (CFG + KEY pre-market):** CFG is THE call. Watch fund finance balances (Table 14), C&I NCO inflection, management tone on sponsors. KEY: office NPLs, NIM, IB fees.
3. **Thursday Apr 17 (RF):** Consumer DQ, CLO marks. No file built — lower priority.
4. **Monday Apr 21 (OZK after close + WAL):** Position names report. All read-through data should be synthesized by then. **NEW LISTEN-FOR: ask any analyst question about warehouse counterparty detail — WAL 10-K doesn't disclose; call Q&A is our chance to learn who they actually lend to.**
5. **Monday Apr 28 (RITM):** Test CARL's "DQ will reverse in Q1" hypothesis. If fails → servicer stress confirmed → APO Atlas SP concentration activates.

**Post-warehouse-research follow-ups (after earnings week):**
6. APO earnings (when does APO report Q1?) — scan for Atlas SP segment disclosure, warehouse book size, any non-bank servicer counterparty commentary
7. Try NewRez LLC direct SEC filings + RITM securitization trust prospectuses to deanonymize RITM warehouse counterparties
8. WAL Q1 10-Q disclosure (early May) — may add color on NDFI subsegments
9. Pull JPM Q1 transcript (not just press coverage) for warehouse commentary

**Carried forward (lower priority):**
10. EGBN earnings prep (grade C, ~10 days) — date still unconfirmed (~Apr 22-25)
11. WAL position decision
12. OZK Q4 earnings call transcript — Wellington/Wasatch questions
13. Cantor PACER docket (needs access)
14. OZK remaining prompts (#13, #19)
15. CPI Apr 10 results — check what printed
