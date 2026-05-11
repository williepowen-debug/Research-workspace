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
- [2026-05-08] **yfinance option chain extraction** — `yf.Ticker('SYM').option_chain('YYYY-MM-DD').puts` returns DataFrame with strike/lastPrice/bid/ask/volume/openInterest/impliedVolatility. `yf.Ticker('SYM').options` gives the available expiry list. NOTE: greeks (delta/theta/vega) NOT included — must compute via Black-Scholes manually if needed. Friday-close marks; Mon open can move bid 25%+ on thin chains. SSB May 15 chain has only 4 OI total — illiquid weeklies can have $0 bid even when last is meaningful.
- [2026-05-08] **Gitignore directory-exclude breaks negation** — `dir/` followed by `!dir/*.md` does NOT work because git refuses to traverse into ignored dirs. Fix: use `dir/*` (file-level wildcard, doesn't ignore the dir itself) + `!dir/*.md`. Verify with `git check-ignore -v`. The .gitignore line 39-41 pattern is the canonical example.
- [2026-05-08] **10-Q SEC EDGAR fetch is XBRL-heavy** — typical bank 10-Q is 3-4MB raw HTML, ~350KB of stripped text. Inline-XBRL tags inflate size 10x. Use `re.sub(r'<[^>]+>',' ',html)` to strip; then `re.sub(r'\s+',' ',text)`. Standard search terms (NDFI, "fund finance") often DON'T match — banks categorize differently. CFG calls it "Capital call facilities" + "Secured private credit finance" + "Other finance and insurance" under C&I Industry sector. Search broad first ("Allowance", "Commercial real estate", "private credit") then narrow.
- [2026-05-08] **Phantom-detection heuristic** — When a position is referenced in dashboard files (STATUS / ROADMAP / CALENDAR / MEMORY / earnings briefs) but does NOT appear in POSITIONS.md AND does NOT appear in FORGE/STATUS.md, it's stale-tracking. Closed positions need a propagation step to dependent docs; without it, phantoms accumulate and other agents (RED especially) build risk frameworks on them. Quick check on any "decide what to do with X" task: grep ground-truth (POSITIONS / FORGE) before recommending action.

## References
- [2026-05-10/11] **LIAISON channel WALTER ↔ REGINALD — Turns 1-3 in 3 hours** — Path: `AGENTS/REGINALD/handoff_WALTER/{README.md, LIAISON.md}`. Pattern lineage: CARL (5/5-6) + BRENT (5/5) + RED (5/6). **Turn 1** REGINALD opened 2026-05-10 23:11 UTC with disposition retrospective (claimed 48-of-51 BOARD-routed-info gap, ZERO action). **Turn 2** WALTER Turn 2 23:30 UTC empirical reframe — actually 16 ACTION + 33 info + 2 body-mention; pattern locked: target-agents underestimate WALTER dispatch volume because they aren't consuming. **Turn 3** REGINALD 2026-05-11 01:53 UTC accepted correction + shipped 3 files (`registry/THRESHOLDS.tsv` 8-row, `board/BOARD_LOG.tsv` 11-col + 32-row backfill stub, `CLAUDE.md` Boot Step 9b BOARD diff scan) + Q4 exposure-overlap-key list (4 dimensions). **6 of 8 Qs LOCKED both sides:** Q1 boot scoping / Q2 THRESHOLDS schema / Q4 overlap-keys / Q5 ROUTING_TABLE v0.9 "By Convergence" section / Q6 dual-doc CALENDAR (md primary + TSV per CARL/BRENT pattern) / Q7 BOARD_LOG schema. WALTER Turn 4 self-tasks: CROSS_REFS/REGINALD.md scaffold + ROUTING_TABLE v0.9 "By Convergence" section + spawn-protocol step 6b update. Turn 5 = close-loop joint-proposal. **Out-of-channel pickup:** SIG-W-20260509-004 Chapter 11 +42% reroutes REGINALD ACTION (commercial Ch 11 specifically — pull from BOARD canonical not inbox).
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

⚠️ **Open question:** Two inbox signals are unread for next session and one is high-priority — **RED's 2026-05-06 counter-call on WAL THESIS v2.0** ("compounder with concentrated CRE tail risk" framing) directly challenges what was just shipped May 1. RED's mandate is steel-man bull case; whether v2.0 actually overcorrected (vs v1.0 "fast-transmission failure") is the call. CARL handover from 2026-05-02 also unread but lower urgency. Before next session does anything else: read both inbox signals.

**Pending Will calls:** (a) REG-20 resolution (CONFIRMED or hold); (b) synthesis-files gitignore decision (still blocking 2 WAL Round 2 synthesis files from commit).

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py)*

### LAST SESSION (May 8 PM — pending Will-decisions cleared + KRE phantom + POSITIONS refresh + MAY15 memo + Q1 10-Q sweep)

**Scope:** Long Friday session. 4 git commits. Started by clearing two pending Will-decisions (REG-20 + gitignore), then caught a phantom that drove the rest of the session.

**Decisions resolved (Will calls):**
1. **REG-20** → CONFIRMED-PARTIAL (literal-text reading; 1 of 3 OR-triggers fired Apr 21). PREDICTIONS.tsv + STATUS/ROADMAP/CALENDAR all updated.
2. **Synthesis-files gitignore** → Option A negation rule (file-level wildcard `q[1-4]_*/*` + `!q[1-4]_*/*.md`). Hit a gotcha on first attempt — directory-exclude breaks negation since git won't traverse into ignored dirs. Fixed. 4 .md files in `WAL/sources/q1_2026/` now committed.

**Phantom caught + cleaned:**
- Will asked for KRE $70P May 15 decision; cross-check against POSITIONS.md (5wk stale) + FORGE/STATUS.md (6wk stale) showed position doesn't exist anywhere. Will confirmed at broker.
- Memory journals (Feb 11-12) show position WAS real then; closed/exited before Apr 2 broker screenshot, never propagated to dependent docs.
- 6 REGINALD-scope refs cleaned (CALENDAR/ROADMAP×2/MEMORY×2/VLY brief).
- 5 RED-scope refs (RED has May 12 T-3 close trigger on phantom) + TRADES candidate file flagged via direct inbox signal (Will authorized per-instance: `AGENTS/RED/inbox/SIG-REGINALD-RED-20260508-kre-70p-may15-phantom.md`).
- ROADMAP audit entry documents the corrected story (real Feb position, never propagated to dependents).

**POSITIONS.md broker refresh (Apr 2 → May 8):**
- Will sent typed list (after JPG was unreadable for confident extraction). 5 weeks of broker activity caught up.
- New names: FITB ($45P Jun-18) + HBAN ($16P Oct-16). Both warrant thesis-row updates if Will tracks them.
- Restructure visible: WAL added Jul-17 + new Sep-18 strikes; APO added Dec-18 longer-dated; IWM strike up to $257.
- Real May 15 cluster surfaced (was hidden by KRE phantom): WAL $75P + SSB $95P (REGINALD scope); TLT $88P (FORGE); OZK $42.5P/$47.5P (OZK agent).
- Quantity column dropped (broker list was strike/expiry only). FORGE/STATUS.md is also Mar 25 stale and would benefit from same broker data refresh.
- ZION 57.5 Put expiry confirmed Jul-17-2026 by Will (was missing in his list).

**MAY15_DECISIONS.md memo created:**
- Friday-night data via yfinance option chains.
- WAL $75P May-15 → LET EXPIRE (don't roll). +9.2% OTM, drifting away. Existing Sep $67.5P/$70P plays the Q2-print thesis with better strike geometry. $30/contract residual not worth $4.20 roll cost. Pre-registered triggers documented (sell-to-close on real -3% catalyst Mon-Wed).
- SSB $95P May-15 → HOLD AND WATCH. NTM (1.35% OTM) but bid $0 — cannot sell. Roll markets non-investable (Sep zero bid/ask). Pre-registered ITM trigger if SSB <$95.

**Q1 10-Q SWEEP — 3 of 5 watchlist banks filed:**
- CFG May 4: NDFI breaks out at $18.12B (Capital call $8.76B + Secured PC finance $4.10B + Other $5.27B). vs Slide 24 prelim $19.6B → $1.5B gap. C&I criticized $2.5B "stable QoQ".
- VLY May 7: Provision -66% YoY ($21.2M vs $62.7M Q1-25). "Provisions mask deterioration" thesis gaining ground; need NCO + ACL coverage drill to lock in.
- EGBN May 7: 🔴 Strategic de-risk CONFIRMED IN PRIMARY FILING TEXT — "high-risk loans concentrated in commercial real estate office segment" (explicit), HFS transfer mechanism cited. **V1 Hidden CRE thesis getting direct primary-source validation.** Watchlist score depends on HFS transfer $ quantification.
- WAL + OZK 10-Qs not yet filed (likely May 11-13 for WAL).
- 10-Qs do NOT contain MI3/RCON2746 (FFIEC Call Report only — bulk PDD ~mid-May).
- Findings: `research/Q1_10Q_SWEEP_2026-05-08.md`.

**Inbox signals NOT processed this session (next session priority):**
- `SIG-RED-REGINALD-20260506-wal-v20-overcorrected.md` (9.5KB, May 6) — RED challenges WAL THESIS v2.0. **High priority.**
- `SIG-CARL-REGINALD-20260502-misplaced-banking-rows-handover.md` (5.8KB, May 2). Lower priority but still pending.

**Files modified this session (REGINALD scope):**
- AGENTS/REGINALD/STATUS.md, MEMORY.md, ROADMAP.md, CALENDAR.md, POSITIONS.md
- AGENTS/REGINALD/workbook/PREDICTIONS.tsv
- AGENTS/REGINALD/MAY15_DECISIONS.md (new)
- AGENTS/REGINALD/research/Q1_10Q_SWEEP_2026-05-08.md (new)
- AGENTS/REGINALD/earnings_briefs/VLY_Q1_2026.md
- AGENTS/REGINALD/WAL/sources/q1_2026/{DROPZONE.md, WAL Earnings Call.md, 2 synthesis files} (newly committed; previously gitignore-blocked)

**Cross-agent files written this session (with Will per-instance authorization):**
- AGENTS/RED/inbox/SIG-REGINALD-RED-20260508-kre-70p-may15-phantom.md (new)

**Shared files modified this session (with Will per-instance authorization):**
- .gitignore (root) — Option A negation rule

**Git: 4 local commits, push deferred.**
- `d5d08d56` REG-20 + gitignore close
- `486aea0b` KRE phantom cleanup + RED handoff
- `325dc8de` POSITIONS refresh + real May 15 cluster
- `0d876199` MAY15 memo + Q1 10-Q sweep

**Push not done:** Other agents (SENTRY, SIGNALS/, scripts/fetch_feeds.py) have uncommitted work outside REGINALD scope blocking pull-then-push sequence. Try push next session if working dir is clean.

**Will conversation moments:**
- Boot: flagged that Will said Monday but it was Friday May 8.
- Pending decisions section: Will picked CONFIRMED-literal + Option A.
- Phantom catch: Will confirmed at broker; gave per-instance authorization for direct RED inbox write (cross-agent rule waived) and .gitignore commit (shared-root file rule waived).
- POSITIONS scope: kept thesis-pure (banks + credit/convergence); OZK/macro/non-thesis flagged for other owners.
- May 15 cluster: Will couldn't pull live broker data (Friday night); option chain math via yfinance close marks instead.
- Final: Will requested clean session close + save unfinished to ROADMAP.

### NEXT SESSION — clear inbox + WAL prep + 10-Q deep drill

1. **Boot normally** — git pull (check working dir state first; may still need pre-pull cleanup), read STATUS (May 8 PM at top), LESSONS, CALENDAR, MEMORY; market.py refresh; inbox scan.
2. **Process RED inbox signal first** (`SIG-RED-REGINALD-20260506-wal-v20-overcorrected.md`) — direct challenge to THESIS v2.0 shipped May 1. Read carefully, evaluate counter-arguments, decide: revise (CHANGELOG entry, possibly v2.1/v3.0), defend (outbox response addressing each point), or hybrid. Do NOT skip — fresh thesis under direct challenge.
3. **Process CARL inbox signal** (`SIG-CARL-REGINALD-20260502-misplaced-banking-rows-handover.md`) — lower urgency but should not stay unread.
4. **Push deferred commits** if working dir is clean — 4 commits pending (`d5d08d56`, `486aea0b`, `325dc8de`, `0d876199`).
5. **WAL Investor Day prep** (May 12 = T-3 from May 9) — build 1-page "what would change the thesis" outline. Listening posts: Leucadia inventory Q&A pressure, Office de-risking story, Cantor recovery posture. **Time-pressure deadline May 11.**
6. **10-Q deep drill (priority order):**
   - EGBN HFS transfer $ quantification — watchlist score depends on it
   - VLY NCO + ACL coverage trajectory — verify "mask" thesis
   - CFG $1.5B NDFI reconciliation gap (Slide 24 vs 10-Q breakdown)
   - Cross-bank Office classified $ comparison
7. **WAL + OZK 10-Q recheck** (~May 11-13) — highest impact filing for V2.0 thesis.
8. **APO Q1 post-print integration** — printed May 6, 3+ days old, not yet integrated. Atlas SP segment, warehouse book, non-bank servicer counterparty — WAL V3 link.
9. **MAY15 cluster execution** — Mon-Fri. Watch for triggers (WAL -3% catalyst window; SSB <$95 ITM trigger). Default = no action; let market decide. Fri May 15 = expiry day; passive close.
10. **MTB Baltimore Sun verification** (SIG-W-20260426-009) — quick pull when bandwidth.
11. **Wave 2 cross-agent outbox signals** — now expanded with 10-Q findings (8 candidate signals listed in ROADMAP open thread).
12. **MI3 / FFIEC PDD recheck** ~May 14-16 (bulk update timing).
13. **VLY 10-Q drill** specifically per CALENDAR (already Q1-print-resolved; this is the deeper read).

