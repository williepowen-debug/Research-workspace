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
- [2026-04-30] **FRED data via fetch.py.** Hardcoded fallback API key at `FORGE/tools/market-data/fetch.py:40` (also `AGENTS/CARL/scripts/consumer_pulse.py:25`) — works without `FRED_API_KEY` env var. Invocation: `.venv/bin/python3 FORGE/tools/market-data/fetch.py fred <SERIES_ID> --periods <N>`. Verified series: BAMLH0A0HYM2 (HY OAS), BAMLH0A3HYC (CCC OAS), ICSA (claims), SOFR, IORB. Note: hardcoded key in committed source = security smell.
- [2026-04-02] OZK price sources can conflict ($46 vs $49 in same session) — always verify at broker when discrepancy >5%.
- [2026-04-12] Wasatch fund commentaries: wasatchglobal.com/wp-content/uploads/strategy-and-fund-documents/ — quarterly fund PDFs.
- [2026-04-16] pdfminer works for PDF text extraction (`.venv/bin/python3`, `from pdfminer.high_level import extract_text`). poppler-utils not installed.
- [2026-04-16] CFG 10-K HTML from EDGAR has inline-XBRL markup; use regex `re.sub(r'<[^>]+>',' ',html)` not BeautifulSoup `.get_text()`.
- [2026-04-19] **Paywall map:** Forbes.com, Seekingalpha.com, Journalrecord.com (Reuters wire) return 403 to Anthropic WebFetch. Workable substitutes: MarketScreener, PrismNews, Sharecafe (Reuters), Motley Fool / Investing.com (SA transcripts).
- [2026-04-22] **LAM = Leucadia Asset Management = Jefferies subsidiary** (post-2013 Leucadia/Jefferies merger). Semantic mapping critical for V2 fraud chain — WAL's $126.4M LAM charge-off is on the Jefferies rail. Cross-reference in any WAL/Jefferies/Cantor research.
- [2026-04-22] **Quartr MCP is subscription-gated** — returned `subscription_required` error when searching companies. Cannot use for document/event fetching. WebFetch + direct IR page links or user-provided PDFs are the workaround.
- [2026-04-24] **SEC EDGAR direct-fetch pattern** — WebFetch 403s on all sec.gov paths, but `curl` with a `User-Agent: REGINALD research willie@research.local` header returns 200. Canonical paths: `https://data.sec.gov/submissions/CIK<padded>.json` for recent filings index (returns recent form/accession/filingDate/primaryDocument arrays) → `https://www.sec.gov/Archives/edgar/data/<cik>/<accession-no-dashes>/<filename>` for actual documents. Note: SEC accession numbers can start with the FILER's CIK, not the COMPANY's — stocktitan reported WAL Q1 8-K as `0001212545-26-026302` but the real accession was `0001628280-26-026302`. Always cross-check via data.sec.gov.
- [2026-04-24] **Q4CDN IR PDF hosting pattern** — Most public bank IR pages host earnings materials at `https://s21.q4cdn.com/<subscriber-id>/files/doc_financials/<year>/<qnum>/<FILENAME>.pdf`. WAL's subscriber-id is `328636679`. Filename conventions vary per bank (17 naming variants probed for WAL supplement — none hit; WAL is deck+release only). Direct fetch works without auth.

## References
- [2026-04-16] EDGAR CIK for MTB: 0000036270
- [2026-04-16] Cadwalader Fund Finance Friday — tracks fund banking personnel and deals.

## Session Notes

⚠️ **Open question:** WAL Wave 1 chunks 3-6 (FRAUD V2 / KB / SCENARIOS / INDEX) vs **Q1 Call Reports filing window opening TODAY May 1-10** (V1 MI3 acceleration test for WAL is direct thesis confirmation) — which gets priority next spawn? Bias: if any watchlist Call Report has hit by next boot, prioritize Call Report read; otherwise continue Wave 1 chunk 3 (FRAUD V2 — small, focused).

**Pending Will calls:** (a) REG-20 resolution (CONFIRMED or hold); (b) synthesis-files gitignore decision (still blocking 2 WAL Round 2 synthesis files from commit).

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py)*

### LAST SESSION (May 1 AM — WAL THESIS v2.0 release + Wave 1 chunks 1, 1b, 2)

**Scope:** Will-directed Wave 1 cascade work while BROCK takes primary on OWL Q1 Apr 30 print. Three chunks executed.

**Chunks completed:**

1. **Chunk 1 — `WAL/THESIS.md` v1.0 → v2.0** (rewrite, ~221 lines)
   - Title: "Fast-Transmission Thesis" → **"Compounder With Concentrated CRE Tail Risk"** (rejects v1 binary)
   - V1 hypothesized → **STRENGTHENED via Office single-point** (Slide 12: 38% of classified, 9.5x disproportion, 18.5% stress; Slide 23: $946M Office matures 2026, 43% of book)
   - V2 hypothesized → **RESOLVED in public 8-K** ($152.5M LAM+Cantor, mgmt-labeled "fraud-related")
   - V3 hypothesized → **directionally disconfirmed at aggregate** (Slide 24 cohort median; only $7.15B Mortgage Warehouse confirms — sits in C&I, not NDFI)
   - PT range $47-60 → **$55-70**
   - New predictions REG-24 (Office classified >$500M by Q3, 60%) + REG-25 (ex-fraud NCO >40bps Q2/Q3, 55%)
   - Key v2 framing point: WAL has BOTH patterns — V2 episodic fraud (resolved) AND leading-bucket buildup (slow-grind, 30-89d PD +45% QoQ, Special Mention +24% QoQ). v1 forced binary; v2 acknowledges both.

2. **Chunk 1b — CHANGELOG documentation pair**
   - **NEW:** `WAL/CHANGELOG.md` (103 lines) — first entry pins v1.0 baseline + documents v2.0 transition. Per "Domain CHANGELOG needed per bank" feedback memory.
   - Master `thesis/CHANGELOG.md` — added top entry. **Master THESIS.md NOT edited** — Bank × Cluster + Validation Scorecard refresh deferred to next master-thesis pass to integrate Q1 Call Reports + Investor Day at once.

3. **Chunk 2 — `WAL/STATUS.md` refresh** (Apr 2 → May 1)
   - Header status 🔴🔴 HIGH CONVICTION SHORT → 🟠 SHORT THESIS ACTIVE (V2 resolved + V3 disconfirmed at aggregate justifies softening; V1 sharpening keeps it active)
   - Live price $80.90 (was stale $72.09 Apr 2)
   - Q1 2026 print snapshot table added (GAAP/adj/cons + leading-vs-lagging)
   - V1/V2/V3 each compact section (no duplication of THESIS — STATUS holds *current numbers*, THESIS holds *framework*)
   - Mgmt outlook tensions table (Slide 17 — 39bps already > 25-35bps guide)
   - Stripped stale P/L from positions per "Prices must be live" rule; pointer to ../POSITIONS.md
   - Research agenda restructured by vector with completed items checked

**Master STATUS.md / CALENDAR.md updated:**
- Master STATUS WAL row in RESEARCH — STALE Apr 2 annotation removed, v2.0 thesis pointer added, follow-up sentence stripped
- Master STATUS header — May 1 AM closeout, Q1 Call Report window note
- CALENDAR — OWL Apr 30 ✅ (BROCK primary; REGINALD info-pickup deferred to BROCK ownership)

**Will conversation moment:** I gave honest read on "is WAL looking stronger now?" — yes-somewhat: bull case strengthened (deposits/CET1/TBV/V3 disconfirmed), bear case sharpened-not-weakened (V1 Office, leading-buckets building, Q1 NCO 39bps above guide). PT raised $47-60 → $55-70 is the explicit admission. Recommended NOT to trim ahead of May 1-10 Call Reports + May 12 Investor Day catalysts.

**Wave 1 NOT done (chunks 3-6 carry-over):**
- Chunk 3: WAL/FRAUD/STATUS.md + FRAUD/SYNTHESIS_V2.md
- Chunk 4: WAL/workbook/KB.tsv + KB_INDEX.md
- Chunk 5: WAL/SCENARIOS.md probability re-weight
- Chunk 6: WAL/INDEX.md link map

**Commit this session:** WAL/THESIS.md, WAL/CHANGELOG.md (new), WAL/STATUS.md, thesis/CHANGELOG.md, REGINALD/STATUS.md, REGINALD/CALENDAR.md, REGINALD/MEMORY.md.

### NEXT SESSION — Q1 Call Reports vs Wave 1 chunks 3-6

1. **Boot normally** — git pull, read STATUS (May 1 AM closeout at top), LESSONS, CALENDAR, MEMORY; market.py; inbox.
2. **Triage decision: Q1 Call Reports vs Wave 1 chunk 3.** Check FFIEC for any watchlist filings (WAL, OZK, EGBN, CFG, VLY). If WAL filed → MI3 acceleration test = top priority (V1 confirmation event). Otherwise → Wave 1 chunk 3 (small, focused, FRAUD V2 docs).
3. **Wave 1 chunk 3 — FRAUD V2 docs** — `WAL/FRAUD/STATUS.md` + `WAL/FRAUD/SYNTHESIS_V2.md`. LAM integrated on Jefferies rail. Open question on other Leucadia-era credits.
4. **Wave 1 chunk 4 — KB refresh** — `WAL/workbook/KB.tsv` + `KB_INDEX.md`. Add Q1 print rows, refresh existing rows whose status changed.
5. **Wave 1 chunk 5 — SCENARIOS re-weight** — V2 resolved → reduce raise/regulatory branch; V3 disconfirmed → reduce NDFI shock; V1 Office → tighten path-1.
6. **Wave 1 chunk 6 — INDEX refresh** — link map.
7. **REG-20 resolution call** — Will's decision still pending.
8. **MTB Baltimore Sun primary verification** (SIG-026-009) — quick pull; closes signal for trade-thesis weight.
9. **VLY 10-Q drill (~May 10)** — verify "provisions mask deterioration."
10. **Synthesis files gitignore decision** — Will's call (negation rule / move path / git add -f).
11. **Wave 2 cross-agent outbox signals** — BROCK / CARL / OTTO / PROME / LIQUID / HAWK. After Wave 1 done.
12. **DEF 14A pass (~90pp)** — Only AFTER Wave 1. Optional enhancement.

**Positions unchanged this session** — no broker data. Thread 3 OZK roll still pending ~May 8 deadline (lives in `../OZK/POSITIONS.md`).
