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

⚠️ **Open question:** Hamblen (President/COO) Mar 11, 2026 Form 4 — unopened. Is it a comp grant, sale, or both? Will was about to pull it when session ended. This is the most important remaining insider filing to check.

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py + darkpool.py)*

### LAST SESSION (Apr 12 — institutional ownership + FDIC insider deep-dive)
- **INSTITUTIONAL OWNERSHIP ANALYSIS:** Will screenshotted OZK institutional ownership page. Extracted full 13F data (Dec 31 2025). Key finding: fundamental credit shops selling (Wellington -43%, D.E. Shaw -26%, AQR -20%, Wasatch -6.6%) while quant/index adding (Citadel +260%, Renaissance +36%, State Street +9%). Smart money divergence = thesis supportive.
- **FDIC DATA SOURCE DISCOVERY:** OZK dissolved its holding company in 2017 and files Form 3/4/5 with FDIC (cert #110), NOT SEC EDGAR. Standard insider tools miss OZK entirely. This explains prior "zero filings" results. Authoritative source: efr.fdic.gov/fcxweb/efr/ (JS-rendered, browser-only).
- **FULL FDIC EFR PULL (cert #110):** Will navigated FDIC system, extracted all Form 4 filings. 18 filings in 2026, all sells/grants. Zero purchases by any insider.
- **DIRECTOR KENNY FULL HISTORY:** Traced complete transaction record. Received 3,725 shares in comp grants over 2 years, sold 3,770. Net seller despite ~$170K in free stock. Sells 60-86% of each grant within weeks. Position declined from 7,053 to 7,008.
- **CEO GLEASON CONFIRMED FROZEN:** Zero Form 4 filings going back to Jul 2023. Neither buying nor selling.
- **WASATCH FUND RESEARCH:** OZK dropped entirely from Wasatch Core Growth Fund (was "strong position" in Q4 2023, absent by Q4 2025). Still in Small Cap Value (#3) and Long/Short Alpha (#10). No published commentary explaining the reduction. Wasatch dropped below 5% threshold Jun 2025 (13G/A filing).
- **13D/13G SEARCH:** No new 5% threshold crossings in 2026. Only filing = Vanguard technical restructuring.
- **CREATED:** OZK/INSTITUTIONAL_OWNERSHIP_PLAN.md (verification plan for 13F data)
- **UPDATED:** OZK/INSIDERS/SELLING.md (Kenny section + institutional data), TIMELINE.md (Kenny transactions + batch filing), STATUS.md (FDIC source fix, pre-earnings pull done)
- **Git:** NOT YET COMMITTED — pending session close

### LAST SESSION (Apr 10 — automation toolkit + EGBN deep-dive)
- Automation toolkit built (8 scripts). EGBN continuity awards deep-dive. boot.py created.

### LAST SESSION (Apr 9 PM — microstructure completion + 13F discovery)
- RP-REG-5.1 all 7 tasks complete. Dark pool, options, short interest analysis. 13F institutional exits documented.

### NEXT SESSION
**Immediate (Will has browser open for these):**
1. **Open Hamblen (President) Mar 11, 2026 Form 4** on FDIC EFR — grant, sale, or both? Most important remaining filing.
2. **Trace Hamblen full history** — same drill as Kenny. He has 5 filings (Aug 2024 → Mar 2026).

**Institutional ownership plan (remaining items):**
3. **OZK Q4 2025 earnings call transcript** — check if Wellington/Wasatch analysts asked CRE questions (selling + probing = conviction)
4. **Wellington N-PORT (Jan 2026)** — monthly fund holdings on EDGAR, 60-day lag. Shows if Wellington continued selling after Dec 31.
5. **Short interest update** — FINRA mid-Apr data imminent

**EGBN (carried forward, 9 days to earnings Apr 21):**
6. Confirm Riel family relationship (proxy/10-K)
7. EGBN Q4 10-K / earnings transcript — DOGE commentary
8. EGBN earnings date confirmation

**Other carryover:**
9. WAL position decision
10. OZK 8-K check (~Apr 14)
11. Read-through watchlist — MTB, CFG, RF
12. Cantor PACER docket (needs access)
13. OZK remaining prompts (#13, #19)
