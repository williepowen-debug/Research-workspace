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
- [2026-04-12] Wasatch fund commentaries: wasatchglobal.com/wp-content/uploads/strategy-and-fund-documents/ — quarterly fund PDFs.
- [2026-04-16] pdfminer works for PDF text extraction (`.venv/bin/python3`, `from pdfminer.high_level import extract_text`). poppler-utils not installed.
- [2026-04-16] CFG 10-K HTML from EDGAR has inline-XBRL markup; use regex `re.sub(r'<[^>]+>',' ',html)` not BeautifulSoup `.get_text()`.
- [2026-04-19] **Paywall map:** Forbes.com, Seekingalpha.com, Journalrecord.com (Reuters wire) return 403 to Anthropic WebFetch. Workable substitutes: MarketScreener, PrismNews, Sharecafe (Reuters), Motley Fool / Investing.com (SA transcripts).
- [2026-04-22] **LAM = Leucadia Asset Management = Jefferies subsidiary** (post-2013 Leucadia/Jefferies merger). Semantic mapping critical for V2 fraud chain — WAL's $126.4M LAM charge-off is on the Jefferies rail. Cross-reference in any WAL/Jefferies/Cantor research.
- [2026-04-22] **Quartr MCP is subscription-gated** — returned `subscription_required` error when searching companies. Cannot use for document/event fetching. WebFetch + direct IR page links or user-provided PDFs are the workaround.
- [2026-04-24] **SEC EDGAR direct-fetch pattern** — WebFetch 403s on all sec.gov paths, but `curl` with a `User-Agent: REGINALD research willie@research.local` header returns 200. Canonical paths: `https://data.sec.gov/submissions/CIK<padded>.json` for recent filings index (returns recent form/accession/filingDate/primaryDocument arrays) → `https://www.sec.gov/Archives/edgar/data/<cik>/<accession-no-dashes>/<filename>` for actual documents. Note: SEC accession numbers can start with the FILER's CIK, not the COMPANY's — stocktitan reported WAL Q1 8-K as `0001212545-26-026302` but the real accession was `0001628280-26-026302`. Always cross-check via data.sec.gov.
- [2026-04-24] **Q4CDN IR PDF hosting pattern** — Most public bank IR pages host earnings materials at `https://s21.q4cdn.com/<subscriber-id>/files/doc_financials/<year>/<qnum>/<FILENAME>.pdf`. WAL's subscriber-id is `328636679`. Filename conventions vary per bank (17 naming variants probed for WAL supplement — none hit; WAL is deck+release only). Direct fetch works without auth.

## References
- [2026-04-02] FRED API key signup: https://fred.stlouisfed.org/docs/api/api_key.html
- [2026-04-16] EDGAR CIK for MTB: 0000036270
- [2026-04-16] Cadwalader Fund Finance Friday — tracks fund banking personnel and deals.

## Session Notes

⚠️ **Open question:** OWL Q1 print Apr 30 AMC is the time-sensitive next anchor (BROCK primary, REGINALD info — PC-stress meta-cluster ≥9 nodes). WAL Wave 1 cascade still pending from prior session — no deadline but quality-of-life. My bias next session: OWL Apr 30 PM/post-print pickup → then WAL Wave 1.

**Pending Will calls:** (a) REG-20 resolution (CONFIRMED or hold); (b) synthesis-files gitignore decision (still blocking 2 WAL Round 2 synthesis files from commit).

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py)*

### LAST SESSION (Apr 29 PM — 5-day catch-up + RITM transcript pull)

**Scope:** Will-directed catch-up after 5-day gap. Goal: integrate what fired in Apr 24 → Apr 29 window without starting Wave 1 cascade.

**Findings integrated:**

1. **4 watchlist Q1 prints pulled via WebSearch:**
   - **VLY (Apr 23):** Adj $0.29 / $0.28 GAAP vs $0.28 cons; Rev $540.4M (+12.6%) beat. **FHLB DECLINE confirmed** (-$350M advances, -$300M brokered) — cohort bifurcation now 4/3 (DECLINE: FITB/RF/ZION/VLY vs SURGE: MTB/CFG/PNC). Coverage flags "**provisions mask deterioration**" — possible CFG-tell candidate; needs Round 2 verification via 10-Q.
   - **SSB (Apr 23):** $2.28 EPS beat $0.05; Rev $661.7M missed cons by $14.8M; ROA 1.37%, ROTCE 17.6%; loans +7.5% ann, pipeline +33% YoY. Beat-rev-miss-fade. CORAL FL/TX pickup needed.
   - **EGBN (Apr 22):** $0.48 vs $0.29 (65% beat). Returned to profitability from Q4 LOSS. **Mgmt: "reduced high-risk CRE and land development concentrations" + "strategic shift underway"** — V1 thesis prediction firing. Low-quality beat (legal-charge absence, no run-rate change). Watchlist score 12 hold; Q2 sustain → downgrade to 8-9.
   - **RITM (Apr 28):** $0.51 / $0.12 GAAP (hedging gap); Rev $1.38B beat 10.4%; servicing UPB $850B; AUM $59B (Crestline). Core-vs-GAAP gap technical, not thesis-relevant.

2. **RITM transcript pull (Motley Fool + Benzinga) — DQ-reversal claim soft fail:**
   - Silverstein (President): "delinquencies remain stable QoQ and FHA delinquencies **flattened** as we normalize the impact of the new FHA modification guidelines."
   - "Stable + flattened" ≠ "reversed." Modification guidelines cited driver = mod-re-aging suppresses measured DQ without underlying credit improvement (composition-masking pattern, cross-reads to ALLY framework Apr 17).
   - **No specific 30+/90+ %s disclosed.** Disclosure quality degraded.
   - **Sector silence is data:** no PennyMac/loanDepot/Lakeview/Freedom comp; no warehouse line / counterparty risk discussion.
   - **WAL V3 thesis read:** not disconfirmed; modestly bearish on NewRez asset quality. RITM offers no mitigating evidence for warehouse counterparty quality.

3. **Cohort fade pattern: 8/8 → 12/12.** All Apr 23 names (VLY -2.3%, SSB -1.9%, EGBN -1.9% over 5d) faded post-print. Pattern fully universal across the Q1 wave.

4. **Cross-agent context absorbed** (not re-derived):
   - SAM Apr 28 — BOJ hawkish hold + 3 dissents (modal v1.3, biggest split since 2016, June hike 74% locked). Ch4 timeline tightens.
   - CARL Apr 29 — Brent reprice $100→$115 intraday, +12% leg unprocessed prior to Apr 24 STATUS. WTI $107.30. IEA "largest supply shock on record" framing.
   - WALTER Apr 29 — 5 dispatches, including SIG-029-005 ROAD Act 76-lawmaker letter (REGINALD action).

5. **4 BOARD signals integrated into STATUS table** (HERMES inbox routing not running per WALTER GAPS — bypass via direct integration):
   - SIG-026-009 Baltimore CRE -$1B (MTB primary; Sun primary verification mandatory before trade weight)
   - SIG-024-001 FL labor 4.6% > US 4.4% (OZK FL CRE info; CARL primary)
   - SIG-029-005 ROAD Act letter (BTR financing-freeze probability adjusts; ROUTINE)
   - SIG-029-002 Blue Owl OCIC/OTIC redemption-cap reactivation (BROCK primary; OWL Q1 Apr 30)

**Files updated:**
- `STATUS.md` — added ~85-line "APR 29 — 5-DAY CATCH-UP" section at top with cohort table + 5 thesis reads + BOJ + BOARD signals + 6 follow-ups. RITM bullet upgraded post-transcript (🟡→🟠 with verdict).
- `CALENDAR.md` — pruned Apr 14 + Apr 20 resolved entries. Added "WEEK OF APR 28" (RITM ✅, BOJ ✅, OWL Apr 30). Refreshed MAY (ROAD Act House vote watch, VLY 10-Q drill, EGBN MI3 trajectory).
- `MEMORY.md` — this rewrite.

**NOT done (carry-over from prior session, deferred again):**
- WAL Wave 1 cascade (THESIS.md v2 + STATUS.md + FRAUD/ + KB.tsv + SCENARIOS + INDEX + thesis/CHANGELOG)
- WAL Wave 2 cross-agent outbox signals
- DEF 14A pass (~90pp)
- OZK post-mortem dedicated file (per WALTER follow-up)
- MTB Baltimore Sun primary verification
- Synthesis files gitignore decision
- REG-20 resolution call

**Commit this session:** `STATUS.md + CALENDAR.md + MEMORY.md`. Synthesis files still blocked by gitignore (decision pending).

### NEXT SESSION — OWL Q1 post-mortem (Apr 30 PM) → then WAL Wave 1

1. **Boot normally** — git pull, read STATUS (Apr 29 catch-up at top), LESSONS, CALENDAR, MEMORY; market.py; inbox.
2. **OWL Q1 print post-mortem** (top priority — print Apr 30 AMC ~5pm ET):
   - Forward fee-base trajectory (real risk per WALTER verify)
   - OCIC/OTIC redemption-cap commentary
   - Founder unwind ($1.1B pledged loans) + Boaz Saba rejected exit context
   - Fed PC-inquiry exposure
   - Cross-update STATUS RESEARCH — Blue Owl section + check BROCK STATUS for primary read
3. **REG-20 resolution call** — Will's decision still pending.
4. **Wave 1 cascade** (carry-over from prior session — order matters):
   - `WAL/THESIS.md` v2 — Round 2 integration; "good compounder with CRE tail risk" framing; PT range $55-70 candidate vs $47-60 prior
   - `WAL/STATUS.md` post-Round-2 refresh
   - `WAL/FRAUD/STATUS.md` + `FRAUD/SYNTHESIS_V2.md` — LAM integrated with Jefferies rail
   - `WAL/workbook/KB.tsv` + `KB_INDEX.md` — row refresh
   - `WAL/SCENARIOS.md` — probability re-weight
   - `WAL/INDEX.md`
   - `thesis/CHANGELOG.md` — Round 2 integration entry
5. **Wave 2 cross-agent outbox** (after Wave 1) — BROCK/CARL/OTTO/PROME/LIQUID/HAWK signals.
6. **DEF 14A pass (90pp)** — only AFTER Wave 1. Optional enhancement.
7. **VLY 10-Q drill (~May 10)** — verify "provisions mask deterioration" via charge-off composition.
8. **MTB Baltimore Sun primary verification** (SIG-026-009) — pull Sun primary to confirm $1B / 29% / 28.7% figures before trade-thesis weight.
9. **Q1 Call Reports May 1-10** — WAL MI3 ≥25% acceleration test; EGBN MI3 trajectory; CFG NDFI reconcile to $19.6B prelim; VLY composition.
10. **Synthesis files gitignore decision** — Will's call (negation rule for *.md / move path / git add -f).

**Positions unchanged this session** — no broker data. Thread 3 roll still pending May 8 deadline (lives in `../OZK/POSITIONS.md`).
