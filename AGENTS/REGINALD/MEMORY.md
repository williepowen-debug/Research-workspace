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
- [2026-05-01] **Q1 Call Report data access pattern.** FDIC SDI (banks.data.fdic.gov) lags 30-60 days post-quarter — risview index timestamp shows when SDI was last refreshed. For early access to Q1 data, use SEC EDGAR (data.sec.gov/submissions/CIK<padded>.json) for 10-Qs (typically filed May 4-10 for accelerated filers, contain NDFI + AOCI but NOT MI3/RCON2746). MI3 requires FFIEC CDR Call Reports — public CDR ManageFacsimiles.aspx is ASP.NET viewstate/cookie-locked, NOT curl-accessible. FFIEC NIC institution profile returns 403 to standard UA. Practical answer: wait for FFIEC PDD bulk update (~mid-May for Q1) or rely on 10-Q indirect signal. Confirmed externally that Nelnet Bank filed Q1 2026 Call Report Apr 29, so the window IS open at FFIEC, just not query-friendly.
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
- [2026-05-01] **Watchlist bank ID lookup (cert / RSSD / CIK)** — confirmed via FDIC BankFind + SEC EDGAR May 1:
  | Bank | FDIC Cert | Bank-level RSSD | Holding Co CIK |
  |---|---|---|---|
  | Western Alliance Bank (WAL) | 57512 | 3138146 | 0001212545 |
  | Bank OZK | 110 | 107244 | 0001569650 |
  | EagleBank (EGBN) | 34742 | 2652092 | 0001050441 |
  | Valley National Bank (VLY) | 9396 | 229801 | **0000714310** |
  | Citizens Bank, NA (CFG) | 57957 | 3303298 | 0000759944 |
  CAUTION: CIK 0000740260 = Ventas (real-estate REIT), NOT Valley National.

## Session Notes

⚠️ **Open question:** With Wave 1 fully closed and Q1 Call Reports not yet filed, the next-spawn priority is between (a) **REG-20 resolution call with Will** (still pending — should I mark CONFIRMED on miss + $152.5M fraud + tape -2%, or hold for higher bar?), and (b) **other 4 of the morning's 5-task list** — specifically the KRE $70P May 15 expiry decision (mechanical, time-sensitive), APO Q1 May 6 prep (5 days out), or MTB Baltimore Sun verification. Bias: if Will is around, get REG-20 closed; otherwise tackle KRE $70P decision (mechanical-before-creative) since the May 8 roll deadline is approaching.

**Pending Will calls:** (a) REG-20 resolution (CONFIRMED or hold); (b) synthesis-files gitignore decision (still blocking 2 WAL Round 2 synthesis files from commit).

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py)*

### LAST SESSION (May 1 PM — Q1 Call Report sweep + Wave 1 chunks 3-6 closeout)

**Scope:** Per Will's task triage from morning ("5 tasks for today"), executed Task 1 (Q1 Call Report sweep) → empty → pivoted to Wave 1 chunks 3-6 per pre-set decision rule.

**Task 1 — Q1 Call Report sweep (executed first, ~25 min):**
- Confirmed cert/RSSD/CIK numbers for all 5 watchlist banks (now in References section)
- VLY CIK confirmed = 0000714310 (NOT 740260 = Ventas — earlier guess was wrong)
- FDIC SDI: all 5 banks' most recent REPDTE = 20251231 (Q4 2025); risview index dated Feb 18, 2026 — SDI lags 30-60 days
- SEC EDGAR: no Q1 2026 10-Q filed for any of WAL/OZK/EGBN/CFG/VLY (all most recent 10-Qs Nov 7, 2025 = Q3 2025)
- WAL Apr 30 8-K = routine $0.42/sh quarterly dividend (no thesis content)
- FFIEC CDR public ManageFacsimiles is ASP.NET viewstate-locked; NIC returns 403; cannot curl
- Background: Nelnet Bank filed Q1 2026 Call Report Apr 29 — window IS open
- **Decision rule from morning MEMORY held:** "if no Call Reports filed yet, continue Wave 1 chunk 3" → pivoted to Wave 1

**Wave 1 chunks 3-6 (executed second, ~90 min):**

3. **Chunk 3 — `WAL/FRAUD/STATUS.md` + `FRAUD/SYNTHESIS_V2.md` post-print rewrite**
   - STATUS.md (82→106 lines): 4-row vector table now organized RESOLVED / PARTIALLY RESOLVED / SILENT (LAM full / Cantor partial / First Brands silent / Tricolor silent)
   - SYNTHESIS_V2.md (93→136 lines): converted "Apr 21 attack plan" to retrospective hypothesis-vs-outcome table; RSM auditor case demoted from primary to tertiary; Leucadia inventory question elevated to PRIMARY open thread
   - Pulled from transcript (line 28+): "fund of Leucadia Asset Management" specificity; "no further commentary while matter is ongoing" lockdown; Cantor recovery via $13M senior liens + UHNW springing guarantees + mortgage fraud policy; "complex and potentially of long duration"; Vecchione "largely behind us"

4. **Chunk 4 — KB.tsv + KB_INDEX.md** (KB 80→105 rows; KB_INDEX rewrite)
   - 25 new Q1-print rows (KB-WAL-081 through KB-WAL-105) covering: Cantor charge taken/residual/validated; LAM charge/lockdown/net-new; Q1 fraud total + mgmt label + sector silence; Office Slide 12/23 + CRE-NOO + Hotel; NDFI Slide 24 + warehouse + lender finance + CLN; PD-30-89 + SM (new LEADING_CREDIT group); securities offset; Q1 EPS + deposit lead + capital + NCO guide tension + revised outlook
   - Pre-print rows 014/015/016/018/046/050 pointed back via DerivedFrom (KB is event log, not state table — old rows stay ACTIVE)
   - KB_INDEX 16 groups (added LEADING_CREDIT); replaced "Earnings Prep Quick-Reference" with "Post-Apr 21 Quick-Reference"; added prediction-to-row mapping for REG-20/24/25
   - Flagged 2 pre-existing column-drift rows (KB-WAL-056/057 have 14 cols not 13) for cleanup pass — OUT OF SCOPE this session, NOT introduced by me

5. **Chunk 5 — SCENARIOS.md probability re-weight** (243→259 lines)
   - Bear 45%→**30%** (V2 binary catalyst RESOLVED removed "$100M+ surprise charge-off" path; range $42-52→$58-68)
   - Base 30%→**38%** (most likely is multi-quarter grind; range $55-65→$70-78)
   - Bull 20%→**25%** (V3 disconfirmed + deposits + Juris upside structurally strengthens bull case; $75-88→$85-95)
   - Tail 5%→**7%** (LAM inventory + Office maturity wall + Apollo Atlas SP linkage justify marginal raise; $28-38→$35-45)
   - EV $57.10 → **$72.32** (current $81.22 → 11% overvalued, down from v1.0 18%)
   - PUT EV refreshed at $81.22: $85P Jun $13.93 / $77.5P Sep **$8.31 best risk-adj** / $70P Sep $4.20 / **$65P Jun $0.75 — flagged for close/roll**

6. **Chunk 6 — INDEX.md refresh** (85→131 lines)
   - Q4 2025 numbers replaced with Q1 2026 (Office classified $407M, $946M maturity wall, $152.5M fraud, deposits cohort lead, NCO 39bps vs 25-35bps guide)
   - KB row count 61→105, groups 10→16
   - Boot sequence adds CHANGELOG step
   - File map adds FRAUD/ subdir + sources/q1_2026/
   - 7 open threads listed at bottom

**REGINALD master files updated:**
- STATUS.md header: PM closeout note + Wave 1 done note + Q1 CR sweep finding
- STATUS.md WAL line in RESEARCH section: KB rows 70→105, groups 10→16, "Wave 1 carry-over" line removed, SCENARIOS EV summary added, position EV line added
- MEMORY.md: 2 new findings (FFIEC Q1 access pattern, watchlist cert/RSSD/CIK reference table)

**Will conversation moments:**
- Morning: "5 tasks for today" → I delivered the list, Will picked Task 1
- After Task 1 dead end: I recommended pivot to Wave 1 chunk 3, Will approved
- Mid-chunk-3: I asked "review now or commit at session close" — Will picked (b) commit at end

**Files modified this session (REGINALD scope):**
- AGENTS/REGINALD/STATUS.md
- AGENTS/REGINALD/MEMORY.md
- AGENTS/REGINALD/WAL/FRAUD/STATUS.md
- AGENTS/REGINALD/WAL/FRAUD/SYNTHESIS_V2.md
- AGENTS/REGINALD/WAL/workbook/KB.tsv
- AGENTS/REGINALD/WAL/workbook/KB_INDEX.md
- AGENTS/REGINALD/WAL/SCENARIOS.md
- AGENTS/REGINALD/WAL/INDEX.md

### NEXT SESSION — REG-20 close + remaining 4 of morning's 5-task list

1. **Boot normally** — git pull, read STATUS (May 1 PM closeout at top), LESSONS, CALENDAR, MEMORY; market.py; inbox.
2. **REG-20 resolution call with Will** — should still be open. Q1 print delivered: GAAP miss -4.6% + $152.5M fraud + tape -2%. Mark CONFIRMED, or hold for capital raise / regulatory action threshold?
3. **KRE $70P May 15 expiry decision** — mechanical-before-creative; deadline ~May 8. KRE is broad-regional canary; REGINALD owns the strategic call. Was Task 3 of morning's 5-task list, deferred today.
4. **APO Q1 May 6 prep** — 5 days out. Atlas SP segment + warehouse book size + non-bank servicer counterparty. Was Task 4 of morning's list.
5. **MTB Baltimore Sun primary verification** (SIG-W-20260426-009: -$1B / 29% reassessed CRE) — was Task 5; quick pull, closes signal for trade-thesis weight.
6. **Q1 Call Report recheck** — re-query SEC EDGAR + FDIC SDI on May 4-5 (when 10-Qs typically start landing for accelerated filers). If anything is filed → MI3 / NDFI / AOCI deep read.
7. **Synthesis-files gitignore decision** — Will's call still pending. 2 WAL Round 2 synthesis files (sources/q1_2026/) still blocked from commit.
8. **VLY 10-Q drill (~May 10)** — verify "provisions mask deterioration."
9. **WAL Investor Day prep (May 12)** — start outline of "what would change the thesis"; add to KB row tracking on the day.
10. **Wave 2 cross-agent outbox signals** — BROCK / CARL / OTTO / PROME / LIQUID / HAWK. Wave 1 now fully closed → Wave 2 unblocked.
11. **DEF 14A pass (~90pp)** — Only AFTER Wave 2 starts. Optional enhancement.

**Positions unchanged this session** — no broker data. Thread 3 OZK roll still pending ~May 8 deadline (lives in `../OZK/POSITIONS.md`).
