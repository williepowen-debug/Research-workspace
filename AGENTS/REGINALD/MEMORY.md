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

⚠️ **Open question:** Counterparty mapping on mortgage warehouse lines — WAL/FHN/TCBI 10-Ks don't name servicer counterparties. Reverse-mapping non-bank servicer 10-Ks (PFSI, LDI, RITM, COOP) to their bank warehouse providers is the key data gap for sizing actual regional bank exposure to FHA servicer stress. Flagged to CARL via outbox reply.

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py + darkpool.py)*

### LAST SESSION (Apr 14 AM — CARL warehouse signal integration)
- **CARL signal processed:** SIG-CARL-REGINALD-20260413 (non-bank servicer → warehouse transmission). Signal was in CARL's outbox — HERMES hadn't delivered yet; pulled directly when Will flagged.
- **Four CARL asks worked:**
  1. WAL 10-K warehouse disclosure — not new; already captured in V3 (SSFA/NDFI), $9.2B est. mortgage warehouse within $10.8B "Other OBS"
  2. FHN/TCBI — both have material warehouse exposure. FHN growing aggressively ($767M Q4 2025 increase, mgmt explicit NDFI driver). TCBI runs SSFA-style capital arb (59% in "enhanced credit structures," $275M freed).
  3. JPM Q1 (today) — beat ($5.94 vs $5.46), NII guide CUT $1.5B. Dimon "increasingly complex risks." No explicit NDFI/warehouse commentary in coverage — need transcript.
  4. RITM Apr 28 — added to CALENDAR as testable "DQ will reverse" claim.
- **Key insight:** CARL's signal doesn't add a new WAL vector. It SHARPENS V3 from pure regulatory-reclassification risk into dual regulatory + counterparty credit risk (MFS UK $669M Barclays template).
- **Files created/updated:** `domain/WAREHOUSE_EXPOSURE.md` (new synthesis), STATUS.md (dashboard + AM brief), CALENDAR.md (RITM), `outbox/2026-04-14_to-CARL_warehouse-exposure-integrated.md` (reply).
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
1. **Tuesday Apr 15 (MTB pre-market):** Listen for CRE provisions, NIM, criticized CRE trend, AOCI commentary. Update MTB/STATUS.md with actuals. Flag read-throughs to OZK/WAL. **NEW: listen for any NDFI / warehouse / mortgage-company-loan commentary.**
2. **Wednesday Apr 16 (CFG + KEY pre-market):** CFG is THE call. Watch fund finance balances (Table 14), C&I NCO inflection, management tone on sponsors. KEY: office NPLs, NIM, IB fees.
3. **Thursday Apr 17 (RF):** Consumer DQ, CLO marks. No file built — lower priority.
4. **Monday Apr 21 (OZK after close + WAL):** Position names report. All read-through data should be synthesized by then.
5. **Monday Apr 28 (RITM):** Test CARL's "DQ will reverse in Q1" hypothesis. If fails → confirms servicer stress → warehouse transmission thesis.

**Warehouse thesis follow-ups:**
6. Pull JPM Q1 transcript (not just press coverage) — look for NDFI, warehouse, mortgage-company-loan, non-bank FI commentary
7. Request CARL/HOMER counterparty mapping (non-bank servicer 10-Ks → bank warehouse providers)
8. Monitor PFSI/LDI/RITM/COOP/Lakeview/Freedom for any covenant/liquidity disclosures
9. Watch for any regional bank Q1 transcript commentary on loan-to-mortgage-company or "enhanced credit structures"

**Carried forward (lower priority during earnings week):**
10. EGBN earnings prep (grade C, ~10 days) — date still unconfirmed (~Apr 22-25)
11. WAL position decision
12. OZK Q4 earnings call transcript — Wellington/Wasatch questions
13. Cantor PACER docket (needs access)
14. OZK remaining prompts (#13, #19)
15. CPI Apr 10 results — check what printed
