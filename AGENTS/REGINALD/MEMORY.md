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
- [2026-05-10/11] **LIAISON channel WALTER ↔ REGINALD — Turns 1-5 CLOSE-CONVERGED in <13 hr UTC** — Path: `AGENTS/REGINALD/handoff_WALTER/{README.md, LIAISON.md}`. Pattern lineage: CARL (5/5-6) + BRENT (5/5) + RED (5/6). **All 8 Qs LOCKED both sides; 5 instantiated files end-to-end.** REGINALD-side: `registry/THRESHOLDS.tsv` 8-row REG-T-NN (sustain=1 on KRE/WAL/Claims binary triggers; sustain=3 on slower credit metrics) + `board/BOARD_LOG.tsv` 11-col (CARL 9 + Channels_Touched + Bank_Tickers) with 32-row backfill stub + `CLAUDE.md` Boot Step 9b 3-tier BOARD diff scan + `design/JOINT_PROPOSAL_2026-05-11_reginald_sections.md`. WALTER-side: `design/CROSS_REFS/REGINALD.md` v0.1 + `registry/REG_THRESHOLDS_FIRED_LOG.tsv` + ROUTING_TABLE v0.9 "By Convergence" + spawn-protocol step 6b. **Empirical correction Turn 2:** my Turn 1 "zero action" claim was wrong — 16 of 51 BOARD signals routed REGINALD ACTION; pattern locked across 3 LIAISONs (target-agents underestimate WALTER dispatch volume because they aren't consuming). **`bank_transmission` enum 8-val pre-cosigned for V0_9_STACK.md** alongside BRENT's `energy_transmission` + `regime_state`. Calibration cycle 1 clock: 2026-05-25 (14d calendar) OR N=15 forward BOARD dispositions (early-fire), synced w/ BRENT. **Channel state: POST-WRAP CALIBRATION-PENDING.** Open externalities (not LIAISON-blockers): CARL DATA_RELEASE_CALENDAR.md pattern landing (~May 17-20) → REGINALD ships CALENDAR_DATA.tsv ~7d later; full BOARD_LOG backfill execution on 16 missed-action signals = separate REGINALD-session task; Will-stitch joint-proposal at repo root. **Out-of-channel pickup:** SIG-W-20260509-004 Chapter 11 +42% reroutes REGINALD ACTION (commercial Ch 11 specifically — pull from BOARD canonical not inbox).
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

⚠️ **Open question:** **WAL Investor Day TOMORROW Tue May 12 at 8:30 AM ET — live read.** Prep file shipped (`WAL/INVESTOR_DAY_PREP_2026-05-12.md`) with 5-bucket framework + pre-registered decision tree. Going in with WAL below $78 threshold ($76.95 close, -6.04%) — tape pre-priced bearish narrative. Modal expectation U1: "Vecchione repeats 'past peak' without quantification → V2.1 stands; passive into MI3 print May 14-16." Webcast at `investors.westernalliancebancorporation.com`.

**Pending Will calls:** None outstanding. SSB $95P May 15 ITM trigger fired today (SSB $93.89 < $95) — needs decision tomorrow/Wednesday window per MAY15_DECISIONS.md.

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py)*

### LAST SESSION (May 11 PM — Investor Day prep + tape break)

**Scope:** Short focused session. 1 deliverable, 3 edits, 1 Will-correction caught. ~2 hours.

**1. WAL Investor Day prep file shipped: `WAL/INVESTOR_DAY_PREP_2026-05-12.md`** (~150 lines):
- 5-bucket listening framework (A Leucadia inventory / B Office de-risking / C Cantor recovery / D MI3 + Office maturity / E 2026 outlook NCO guide)
- Pre-registered decision tree: 3 bear-triggers (B1/B2/B3) / 3 bull-lean (L1/L2/L3) / 2 unchanged (U1/U2 modal) / 1 invalidate (I1)
- Analyst Q&A grep list (8 prioritized terms for transcript drop)
- Position implications matrix mapping each trigger outcome to action
- Logistics checklist; tape-on-the-day ≠ signal rule explicit (3-5 day read window)

**2. Will-provided announcement PDF integrated:**
- Confirmed Tue May 12 8:30 AM ET; NYC in-person invitation-only; live webcast at `investors.westernalliancebancorporation.com`
- Filed to `WAL/sources/investor_day_2026/announcement_2026-02-20.pdf` (mirrors q1_2026/ pattern)
- IR contact Miles Pondelik / WAInvestorDay@ inbox captured
- No pre-released agenda — presenter list / topic breakdown lands day-of

**3. Will-correction caught — Q&A curation overreach:**
- I framed "invitation-only attendance" as "Q&A pool curated by IR" and tightened Bucket A bear-reads
- Will pushed back: invitation-only is capacity-management, not question-filtering; covering sell-side analysts (KBW/Wolfe/Citi/JPM/MS/Wells) get seats by default
- Fixed prep file — removed curation theory, replaced with venue/format note (atmospheric softening only, not structural filter)
- **Pattern:** I had clean operational text and layered an unsupported interpretation on top. Per MEMORY [Evaluate Evidence Standalone] feedback — present what data says before reaching for what it might imply. Caught and corrected.

**4. Tape broke $78 going into Investor Day:**
- WAL close $76.95 (-6.04%) — first sub-$78 close since Apr 22-23 breach
- SSB close $93.89 (-2.48%) — $95P May 15 **ITM trigger fired** per MAY15_DECISIONS.md
- Whole regional cohort red (KRE -1.86%, ZION -2.72%, EGBN -2.81%); VIX +6.92%
- Brent pulled back to $104 from $111 — stagflation pillar softening
- "Calm-before-disclosure" window from Apr 30 STATUS framing broke today

**5. Boot Step 9b first execution test:**
- Tier (a) action-recipient grep: **13 ACTION-routed signals on 5/11 alone** — massive inflow vs ~1-2/day baseline
- Tier (b) cluster_mediating grep: ~18 signals incl. those above
- Tier (c) info-recipient cluster-filtered: deferred (volume + time)
- **Result:** identified universe but didn't write BOARD_LOG.tsv disposition rows — deferred to next session as bandwidth task
- Architecture works mechanically; volume is real (13 ACTION/day is a sustained analytic load if pattern continues)

**Files modified this session (REGINALD scope):**
- `WAL/INVESTOR_DAY_PREP_2026-05-12.md` (new)
- `WAL/sources/investor_day_2026/announcement_2026-02-20.pdf` (new — moved from inbox)
- `WAL/STATUS.md` (price + Investor Day prep ref + WALTER 023 note + threshold breach)
- `STATUS.md` (header + threshold table + macro read)
- `CALENDAR.md` (Investor Day time confirmed + prep done marker)
- `MEMORY.md` (this rewrite)
- `ROADMAP.md` (this rewrite)
- `SCRATCH.md` (entry for tonight)

**Will conversation moments:**
- Confirmed Investor Day time + dropped announcement PDF in inbox
- Caught my Q&A curation overreach — clean correction
- Authorized session close at the right point (pre-Investor-Day prep done, no need to start new threads tonight)

**Git: pending closeout commit.** Other agents' uncommitted work (WALTER anchors / BOARD INDEX / 6 new BOARD signals) outside REGINALD scope — they own those commits. Push deferred if working dir still divergent at commit time.

### LAST SESSION (May 10/11 AM — WALTER LIAISON converged + V2.0 → V2.1 ship) [PRIOR-SESSION RECAP — pruned to 1 line]

May 10/11 AM: WALTER ↔ REGINALD LIAISON Turns 1-5 converged in <13 hr UTC (all 8 Qs locked; 5 files instantiated; `bank_transmission` 8-val enum pre-cosigned; calibration cycle 1 = 5/25); RED CHG-RED-025 OVER-CORRECTED hybrid response → V2.0 → V2.1 ship (M2 + M4 full accept; V1 restored pending MI3; Bear split 12%/23%; Jun-conditional EV; $65P Jun close-rec withdrawn); 2 LESSONS.md methodology entries added. Commits `f59f715b` / `6e216fd4` / `c771aaae` / `2baead6d`.

### LAST SESSION (May 8 PM — pending Will-decisions cleared + KRE phantom + POSITIONS refresh + MAY15 memo + Q1 10-Q sweep) [PRIOR-SESSION RECAP — pruned to 1 line per Sub-Agent Prompt Discipline lesson]

May 8: REG-20 resolved CONFIRMED-PARTIAL; gitignore Option A negation rule; KRE $70P May 15 phantom caught + 6 REGINALD-scope refs cleaned (cross-agent RED inbox signal sent w/ Will per-instance auth); POSITIONS broker refresh Apr 2→May 8 (FITB+HBAN added); MAY15_DECISIONS.md (WAL $75P let-expire / SSB $95P hold-and-watch); Q1 10-Q sweep 3-of-5 banks (CFG/VLY/EGBN — EGBN "high-risk office" CONFIRMED in primary filing). Full detail in commit history `d5d08d56` / `486aea0b` / `325dc8de` / `0d876199`.

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

### NEXT SESSION — Investor Day live read + SSB ITM decision + WAL 10-Q monitor

1. **Boot normally** — git pull (other agents may have uncommitted work; check status carefully), read STATUS (price + Investor Day prep at top of header), CALENDAR (May 12 8:30 AM ET ✅), MEMORY (this session note at top of history), ROADMAP, SCRATCH; market.py refresh; inbox scan; BOARD diff scan Step 9b.
2. 🔴 **WAL Investor Day live or transcript read — Tue May 12, 8:30 AM ET** — execute the pre-registered framework in `WAL/INVESTOR_DAY_PREP_2026-05-12.md`:
   - Live webcast at `investors.westernalliancebancorporation.com` → Events & Presentations
   - 5-bucket listening posts (A Leucadia / B Office / C Cantor / D MI3 + maturity / E NCO guide)
   - Decision tree: B1/B2/B3 (bear) / L1/L2/L3 (bull-lean) / U1/U2 (unchanged, modal) / I1 (invalidate)
   - **Tape-on-the-day ≠ signal rule:** read over 3-5 days post-transcript, not intraday
   - Post-event: write findings to `WAL/INVESTOR_DAY_FINDINGS_2026-05-12.md` (companion to prep file)
3. 🔴 **SSB $95P May 15 ITM trigger decision** — SSB closed $93.89 May 11 < $95. Per `MAY15_DECISIONS.md` pre-registered trigger. Bid was $0 last week (Friday close marks) — option likely still illiquid. Decision options: (a) hold to expiry pin-watch (default if cannot sell); (b) close at any bid Mon-Wed window if liquidity returns; (c) roll to Sep if cost analysis works (unlikely on $0-bid weeklies). Check live option chain Mon AM.
4. 🔴 **WAL 10-Q drill (filed expected May 11-13)** — Schedule O / Table 16 large-credit detail per RED §12.3 cross-credit inventory test (0/1/2+ Leucadia-era credits). Office concentration Q1 numbers in 10-Q form; Cantor residual; Apollo Atlas SP counterparty.
5. 🔴 **MI3 print monitoring (FFIEC PDD bulk ~May 14-16)** — V2.1 → V2.2 trigger; pre-registered branching table in `WAL/THESIS.md` v2.1.
6. 🟠 **BOARD diff scan completion — 13 ACTION signals from 5/11 + new 5/12** — Boot Step 9b identified universe this session; write disposition rows to `board/BOARD_LOG.tsv`. Highest-impact integration: SIG-W-20260511-023 (already integrated to V2.1 framing); SIG-W-20260511-030 (cohort counter-evidence — challenges 12/12 fade if confirmed); SIG-W-20260511-029 (NDFI 5-cat schema May 15 CDR Q1 bulk release context); SIG-W-20260511-014 (NDFI $1T threshold new Call Report rules MI3-adjacent); SIG-W-20260511-021 (EGBN Q1 NCO 1.46%); SIG-W-20260511-008 (OZK Q1 5 problem loans $409M). Plus STWD/KREF/WFC/MS-BCI/CUBI/BANC/Trepp/FDIC-Fed-cuts.
7. 🟠 **OZK 10-Q recheck** (filed expected May 11-13) — OZK peer-agent owns; REGINALD info-only on cohort-fade pickup. RESG classified detail; specific reserves on 11 problem credits.
8. 🟠 **APO Q1 post-print integration** (printed May 6 — 5+ days old) — Atlas SP segment, warehouse book size, non-bank servicer counterparty.
9. 🟠 **Q1 10-Q deep drill (deferred from May 8 sweep)** — EGBN HFS transfer $ quantification; VLY NCO + ACL coverage trajectory; CFG $1.5B NDFI reconciliation gap; cross-bank Office classified comparison.
10. 🟡 **PROME ZION-scaffold-fill request** (May 9 inbox) — substantive new work; needs dedicated session. 3 priority research outputs: MI3_HIDDEN_CRE_SCREEN.md, CRE_MULTIFAMILY_MATURITY.md, MUNI_CONDUIT_RISK.md.
11. 🟡 **CARL handover signal** (May 2 inbox; now 9+ days unread). Lower urgency.
12. 🟡 **BOARD_LOG.tsv full backfill execution** — 16 missed-action signals still stubbed; full disposition pass requires reading each `/BOARD/SIG-W-*.md`.
13. 🟡 **MTB Baltimore Sun verification** (SIG-W-20260426-009) — quick pull when bandwidth.
14. 🟡 **Wave 2 cross-agent outbox signals** — 8 candidates in ROADMAP; deferred until HERMES revival or new messaging pattern.
15. 🟡 **STATUS.md hygiene pass** — APR 30 PM LIVE TAPE section + APR 29 catch-up are 11+ days stale; should be archived to `archive/STATUS_apr28_may1.md` or similar; STATUS should be a current-state snapshot not a multi-week diary.
16. 🟡 **WALTER LIAISON calibration cycle 1** — trigger 2026-05-25 (14d) OR N=15 forward BOARD dispositions.

**Top-3 priority for tomorrow morning:** Items 2 (Investor Day live read 8:30 AM ET) + 3 (SSB ITM trigger decision) + 4 (WAL 10-Q if filed). Everything else negotiable.

