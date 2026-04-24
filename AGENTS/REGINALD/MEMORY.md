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

⚠️ **Open question:** WAL Round 2 deep-mine sequencing — does the next session prioritize deck (25pp) → press release PDF tables (pp7-19) → DEF 14A (~90pp), or flip the order? Press release PDF probably closes the most Q1_ANALYSIS §11 open items fastest. Deck is the broadest thesis surface. DEF 14A is specifically for the LEADERSHIP/insider/governance layer and could be parallelized.

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py)*

### LAST SESSION (Apr 24 late-afternoon — WAL Q1 Step 1 source fetch + transcript synthesis; OZK spinout wrap)

**WAL Q1 2026 primary-source acquisition complete.** Step 1 of the WAL Q1 post-print plan landed all fetchable materials:
- Earnings deck (Q4CDN direct CDN, 25pp) — `q1_2026/WAL-Q1-2026-Earnings-Presentation-Final-v2.pdf`
- Press release PDF (Will dropped, 20pp with 13pp of tables) — `q1_2026/Press-Release-3-31-2026-Final.pdf`
- Press release HTML (SEC Ex 99.1 via curl+UA — redundant with PDF) — `q1_2026/WAL-Q1-2026-Press-Release.htm`
- 8-K form (SEC) — `q1_2026/WAL-Q1-2026-8K.htm`
- **Full earnings call transcript (Will dropped, 706 lines verbatim)** — `q1_2026/WAL Earnings Call.md`
- DEF 14A proxy (Will dropped, 7.3MB / ~90pp) — `q1_2026/14A.pdf`
- DEFA14A annual meeting notice (Will dropped, 7pp, procedural) — `q1_2026/14A 2.pdf`
- Confirmed negative: no separate financial supplement — WAL is deck+release only (matches FITB pattern)
- Correct SEC accession is **`0001628280-26-026302`** (stocktitan's `0001212545-26-026302` was wrong — filer CIK ≠ company CIK)

**Transcript fully analyzed** → `WAL Q1 2026 - Transcript Synthesis.md` (248 lines, tracked). 7 headline findings:
1. 🔴 **WAL at $98.9B — Q2 or Q3 crosses $100B** (Cat III/IV threshold). Net-new V4 thesis lever independent of V1-V3; intersects Jun 18 AOCI comment period close.
2. 🟢 Mgmt framed LAM+Cantor as "largely behind us" — binary read: clean Q2/Q3 vindicates, another credit = gaffe on record.
3. 🟠 Buybacks ending — Vecchione explicit: "not in our models right now."
4. 🟠 HFI growth deliberately throttled; Bruckner: pulled back on "commercial real estate related segment."
5. 🟡 $26M of LAM charge DELIBERATELY unmitigated — analyst consensus advice.
6. 🟡 Slide 20+24 reconcile — WAL lender finance $2.3B = majority of $3B NDFI bucket; top fund $60M/$30M funded; **Janet Lee asked for count of >$100M exposures, Vecchione refused.**
7. 🟢 Street disengaged from V1/V3 — zero analyst probe of MI3, SSFA, other Leucadia credits. Thesis runway preserved, unvindicated.

**Deck + press release PDF + DEF 14A — NOT yet deep-read.** Only sampled. Round 2 integration pending next session.

**OZK spinout finalized.** Step 13 boot test (OZK side) passed 6/7 during this session. OZK side also executed:
- Step 15 (OZK_SPINOUT_PLAN.md → OZK/archive/) — staged in OZK's work, committed by REGINALD
- PREDICTIONS.tsv split — REG-16/21/22/23 → OZK-01..04; REG-17 (WAL/OZK/EGBN multi-bank screen) retained in REGINALD with spinout note
- Full cross-boundary audit fixes per Will's authorization

**REGINALD↔OZK pair channel established** at `AGENTS/OZK/REGINALD_CHANNEL.md`. Convention: newest-at-top, ACK line after read, archive at ~300 lines. OZK has ACKd + replied twice this session. Will approved this pattern. *Messaging-overhaul note in user MEMORY still applies; this is a point-in-time solution for the REGINALD↔OZK pair specifically.*

**Mid-session side-fix: Telegram plugin conflict.** REGINALD's main session (PID 773) was spawning a competing telegram poller alongside WALTER's dedicated `--channels plugin:telegram` session. Investigated + root-caused to global `enabledPlugins.telegram=true` in `~/.claude/settings.json`. Recommended move to WALTER-scoped `.claude/settings.json`. WALTER separately resolved it (commit `2c0acf90`).

**Commit this session:** `121452be` — WAL Q1 Step 1 sources (3 tracked files) + PREDICTIONS.tsv spinout cleanup + OZK_SPINOUT_PLAN.md archive rename. 436 insertions, clean push.

### NEXT SESSION — WAL Round 2 deep-mine (primary work)

1. **Boot normally** — git pull, read STATUS, LESSONS, CALENDAR, MEMORY; run market.py; check inbox (likely empty).
2. **Start Round 2 deep-mine** of the 3 unread primary sources:
   - `WAL/sources/q1_2026/Press-Release-3-31-2026-Final.pdf` (pp7-19, 13 financial table pages) — probably closes the most §11 open items fastest
   - `WAL/sources/q1_2026/WAL-Q1-2026-Earnings-Presentation-Final-v2.pdf` (23 unread slides — capital walk, credit tables, CRE detail, management outlook)
   - `WAL/sources/q1_2026/14A.pdf` (DEF 14A ~90pp — CFO Idnani comp package, ownership table, related party transactions, audit committee, board committee assignments)
3. **Update `WAL/Q1_2026_ANALYSIS.md` to Round 2** — close §11 open items, integrate $100B lever as new section, fold in deck findings. Preserve Round 1 structure where still correct.
4. **Wave 1 cascade** — rewrite in order (each depends on the previous):
   - `WAL/THESIS.md` v2 (V2-CONFIRMED paradigm, LAM integrated, ex-fraud clean credit, $100B lever, deposit strategy reversal)
   - `WAL/STATUS.md` (current prices, post-print key numbers, new position P&L)
   - `WAL/FRAUD/STATUS.md` + `FRAUD/SYNTHESIS_V2.md` (LAM added, Cantor resolved)
   - `WAL/workbook/KB.tsv` + `KB_INDEX.md` (row count refresh, LAM rows, updated Cantor rows)
   - `WAL/SCENARIOS.md` (post-print probability re-weight)
   - `WAL/INDEX.md` (housekeeping)
   - `thesis/CHANGELOG.md` (document V2-CONFIRMED as thesis event)
5. **Wave 2 cross-agent outbox** — per Transcript Synthesis cross-agent section: BROCK (LAM=fund-of-LAM Jefferies rail), CARL (consumer disconfirming at WAL), OTTO ($152.5M fraud ledger), PROME (duration extends, $100B lever new), LIQUID (WAL funding NOT stressed), HAWK/BRENT (no dedicated ME reserve).
6. **Carry-over: OZK Spinout Step 14** — trim `REGINALD/STATUS.md` "RESEARCH — OZK" section (lines ~327-349) to 5-10 line pointer to `../OZK/STATUS.md`. OZK confirmed stable on its side, safe to proceed whenever. Low priority vs WAL work.
7. **Calendar-gated (May 1-10): Auto-fetch** WAL 10-Q + Call Report when filed. Use SEC `data.sec.gov/submissions/CIK0001212545.json` + `curl + UA` pattern (see Findings below). MI3 ratio refresh is V1 thesis test.

**Positions unchanged this session** — no broker data received. Thread 3 roll still pending with May 8 deadline (lives in `../OZK/POSITIONS.md` now).
