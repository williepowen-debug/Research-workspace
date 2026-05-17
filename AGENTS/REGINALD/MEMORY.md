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

⚠️ **Open question:** **SSB $95P May 15 expiry-day execution outcome unknown.** Ladder written `MAY15_DECISIONS.md` post-script (Phase 1 STC $3.50 → Phase 5 DNE backstop) with SSB at $91.21 intraday + intrinsic $3.79; Will hadn't confirmed contract qty or path choice when session paused for commit. Boot next session by asking Will what happened — auto-exercised into short SSB at $95? sold at limit? DNE filed? Log outcome in POSITIONS.md + extract LESSON if any.

**Pending Will calls:** SSB $95P expiry outcome (above) + WAL $75P May 15 outcome ($75.93 ITM by $0.93 — also expired Friday, also needs outcome confirm).

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py)*

### LAST SESSION (May 15-17 — Investor Day FINDINGS + SSB expiry ladder + clean closeout commit)

**Scope:** 2-segment session across 3 calendar days. Investor Day findings + SSB expiry day work on 5/15; tape pause; closeout on 5/17 Sun.

**1. WAL Investor Day FINDINGS shipped: `WAL/INVESTOR_DAY_FINDINGS_2026-05-12.md`** (~160 lines, +1 EDGAR source archive set):
- Located source materials: WAL 8-K EX-99.1 deck (accession `0001628280-26-033850`, filed 5/12 8:30 AM ET pre-event); archived raw HTML to `WAL/sources/investor_day_2026/{deck_raw.htm, 8k_raw.htm}` (~160KB total)
- Bucket scoring from prepared remarks (125-slide deck): **A=U1** (0 new Leucadia credits named); **B=U2** (Office portfolio breakdown ✅ but no quantified de-risking $ / $946M maturity wall NOT mentioned); **C=U2** (Cantor silent / legal-proceedings boilerplate); **D=U2** (Office partial via Slide 93 / MI3 / RCON2746 / Memo Item 3 SILENT); **E=B3 FIRED** (mgmt held 25-35bps NCO guide despite Q1 ex-fraud 39bps above range top + deposit costs raised $650-700M)
- Recommended **V2.1 → V2.1.1 minor revision**: Bear-slow 23→27%, Base 38→35%, Bull 25→24%; REG-25 confidence 55%→65%+; EV $72.32→~$70-71 (still ~7-9% over at $75.93)
- **No V2.2 promotion** (single-bucket bear-trigger = sub-component re-weight, not thesis-level shift)
- **Q&A transcript still missing** — Bucket A/C re-score could escalate to V2.2 if B1 fires
- Position implications per prep matrix: Sep $77.5P/$70P core REINFORCED-HOLD; Jun $85P/$65P HOLD; no new positions

**2. SSB $95P May 15 expiry-day execution ladder appended to `MAY15_DECISIONS.md`:**
- Live tape 5/15 ~12:21 ET: SSB $91.21 (open $93.17 → low $91.15); $95P ITM intrinsic $3.79; bid $1.55 / ask $4.30 / last $3.23 (OI 1, volume 1)
- Roll path still CLOSED (Sep $95P 0/0 bid/ask; Jun $95P $3.10/$6.80 spread OI 3; Sep $90P $3.70/$6.90 OI 1)
- New factor vs 5/8 memo: **auto-exercise risk** — long ITM $95P auto-exercises into SHORT SSB at $95 on close unless DNE filed; carries margin + borrow + overnight risk
- Recommended Phase 1-5 ladder: STC $3.50 → $3.00 → $2.50 → bid → DNE backstop (per-ctr; scales linearly w/ qty)
- ⚠️ POSITIONS.md does NOT carry quantity (dropped 5/8 broker refresh) — must ask Will for ctr count
- Will paused work to commit before confirming execution path — outcome unknown at session close

**3. Critical discovery NOT integrated this session: WAL 10-Q filed 5/11 PM** (EDGAR accession `0001628280-26-033054`, `wal-20260331.htm`):
- Was filed Monday 5/11 same day as STATUS write — REGINALD missed it through the LIAISON work + V2.1 ship + Investor Day prep ship
- Schedule O / Table 16 cross-credit inventory test per RED §12.3 still pending
- **This is the highest-information delta** I missed between 5/11 PM and 5/15
- Next session #1 priority

**4. Boot Step 9b BOARD diff scan run:**
- 9 BOARD signals 5/12-5/15; **0 ACTION-routed to REGINALD**, 6 info-cc'd (all CONSUMER_STAGFLATION cluster, 5 cluster_mediating)
- Read-only awareness: CPI hot 3.8% (5/12), PPI hot 6.0% (5/13), NYFed HHDC student-loan defaults (5/13), BAA wage K-shape (5/13), USDA WASDE wheat 1957-low (5/13), claims 211K (5/14)
- No REGINALD-domain action triggers — these are CARL/BRENT/HENRY primary
- **Boot 9b grep refinement noted:** schema uses `signal_role: cluster_mediating` not `cluster_mediating: true`; my grep returned 0 cluster_mediating hits when there were actually 5. Tier (c) catch saved the analysis but grep needs fix.

**5. Tape post-Investor-Day:**
- WAL net -1.3% over 3 trading days post-event (5/12 ID-day → 5/15 $75.93) despite cohort tailwind today — Investor Day did NOT clear the bear
- SSB idiosyncratic -2.17% intraday 5/15 on cohort-green day; FL/TX cohort-fade thesis acute today
- Brent re-spiked $104 → $108 (+2.26% 5/15) — stagflation pillar reasserting after 5/11 softening
- VIX +11.3% on green-cohort day = vol bid through risk-on tape; implied stress not resolved

**Files modified this session (REGINALD scope):**
- `WAL/INVESTOR_DAY_FINDINGS_2026-05-12.md` (new, ~160 lines)
- `WAL/sources/investor_day_2026/deck_raw.htm` (new, 132KB EDGAR source)
- `WAL/sources/investor_day_2026/8k_raw.htm` (new, 28KB EDGAR source)
- `MAY15_DECISIONS.md` (+85 lines — Phase 1-5 execution ladder appendix)
- `STATUS.md` (header + threshold table + macro read for 5/15 + 5/17 closeout)
- `WAL/STATUS.md` (header for 5/15 + V2.1.1 recommendation)
- `CALENDAR.md` (5/12 Investor Day ✅, 5/11-13 WAL 10-Q ⚠️ filed but not integrated, 5/14-16 MI3 window passed status-pending, 5/15 expiry-day outcome pending)
- `MEMORY.md` (this rewrite)
- `ROADMAP.md` (this rewrite — pending)
- `SCRATCH.md` (5/15-17 entry — pending)

**Will conversation moments:**
- Boot: caught me up from 5/11 to 5/15 across 4-day gap; flagged Investor Day findings + SSB expiry as the two outstanding items
- WAL Investor Day: chose to pursue findings work first (over SSB pivot or 10-Q hunt)
- SSB ladder: paused work to commit when execution recommendation written; deferred execution decision
- Date-check ping 5/17 Sun: confirmed I was reading; chose closeout path over continuing work
- Authorized REGINALD-only commit `6a20710a` (later pushed by WALTER as `1b37fccc`); no push allowed
- Confirmed WALTER had pushed my updates — working tree now clean externally

**Git:** Closeout commit pending at end of this rewrite. Working tree clean externally (WALTER swept on 5/17 boot per the consolidated WALTER commit `7a3ece9d`). REGINALD push allowed this round since no other agent has uncommitted work blocking.

### LAST SESSION (May 11 PM — Investor Day prep + tape break) [PRIOR-SESSION RECAP — pruned to 1 line]

May 11 PM: WAL Investor Day PREP file shipped (`WAL/INVESTOR_DAY_PREP_2026-05-12.md`) with 5-bucket framework + pre-registered decision tree (3 bear / 3 bull-lean / 2 unchanged / 1 invalidate). Tape broke $78 ($76.95 close -6.04%) + SSB $95P ITM trigger fired ($93.89 < $95). Will-provided announcement PDF integrated. Q&A curation overreach caught + corrected. Boot Step 9b first execution test (13 ACTION/day inflow noted).

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

### NEXT SESSION — SSB outcome log + WAL 10-Q drill + MI3 status check + V2.1.1 propagation

1. **Boot normally** — git pull (working tree should be clean — WALTER swept 5/17), read STATUS (5/17 closeout header), CALENDAR (5/12 ID done, 5/15 expiry outcome pending), MEMORY (this session note at top), ROADMAP, SCRATCH; market.py refresh; inbox scan; BOARD diff scan Step 9b (with FIXED grep — `signal_role: cluster_mediating` not `cluster_mediating: true`).
2. 🔴 **SSB $95P + WAL $75P May 15 expiry OUTCOME LOG** — ask Will:
   - SSB $95P: auto-exercised (now short 100×N at $95)? sold at limit ($3.50/$3.00/$2.50/bid)? DNE filed (premium lost)?
   - WAL $75P: closed at $75.93 (-$0.93 ITM); auto-exercised into short WAL at $75? sold/DNE?
   - Log to `POSITIONS.md` + `FORGE/STATUS.md` if any. Extract LESSON if execution path diverged from pre-registered.
3. 🔴 **WAL 10-Q drill — FILED 5/11 PM (accession `0001628280-26-033054`)** — fetch via EDGAR (curl pattern in MEMORY findings); strip XBRL; search for: Schedule O / Table 16 large-credit names (RED §12.3 test: 0/1/2+ Leucadia-era credits); Office concentration Q1 numbers; Cantor residual; Apollo Atlas SP counterparty; NDFI breakout. **Outcome feeds V2.1.1 → V2.2 decision.**
4. 🔴 **MI3 / FFIEC PDD bulk update status check (5/14-16 window passed)** — recheck FFIEC PDD; if data is now available, run V1 calibration per `WAL/THESIS.md` v2.1 pre-registered branching table (≥27% / 25-26.9% / 24-24.9% / <24%). Also OZK 37.6% baseline + EGBN 23.7% trajectories.
5. 🔴 **WAL Investor Day Q&A transcript hunt** — Seeking Alpha / Motley Fool / Investing.com / `investors.westernalliancebancorporation.com` archived replay. Search per prep grep list. **If B1 fires (analyst pressure on Leucadia + mgmt dodge), promote V2.1 → V2.2 with mgmt-discount tightening + bear +3-5pp.**
6. 🟠 **V2.1.1 propagation** (only AFTER Q&A read so we know if we're going V2.1.1 or V2.2):
   - `WAL/THESIS.md` v2.1 → v2.1.1 OR v2.2 (re-weight per Bucket E B3; Bear-slow 23→27; REG-25 confidence 55→65%)
   - `WAL/SCENARIOS.md` v2.1 → v2.1.1 / v2.2 (re-run EV table)
   - `WAL/CHANGELOG.md` (version entry)
   - `workbook/PREDICTIONS.tsv` (REG-25 confidence ratchet)
7. 🟠 **BOARD diff scan since 5/14** — likely accumulated signals over 5/15-17; fixed grep + tier-c cluster filter. Backfill `board/BOARD_LOG.tsv` disposition rows.
8. 🟠 **OZK 10-Q recheck** (filed expected May 11-13) — OZK peer-agent owns; REGINALD info-only on cohort-fade pickup. Hand off via outbox if anything REGINALD-relevant surfaces.
9. 🟠 **APO Q1 post-print integration** (printed May 6 — now 11+ days stale) — Atlas SP segment, warehouse book size, non-bank servicer counterparty.
10. 🟠 **Q1 10-Q deep drill (deferred from May 8 sweep)** — EGBN HFS transfer $ quantification; VLY NCO + ACL coverage trajectory; CFG $1.5B NDFI reconciliation gap; cross-bank Office classified comparison.
11. 🟡 **PROME ZION-scaffold-fill request** (May 9 inbox; now 8 days unread) — substantive new work; needs dedicated session. 3 priority research outputs: MI3_HIDDEN_CRE_SCREEN.md, CRE_MULTIFAMILY_MATURITY.md, MUNI_CONDUIT_RISK.md.
12. 🟡 **CARL handover signal** (May 2 inbox; now 15+ days unread). Lower urgency.
13. 🟡 **BOARD_LOG.tsv full backfill execution** — 16 missed-action signals still stubbed + new 5/11+ ACTION signals; full disposition pass.
14. 🟡 **MTB Baltimore Sun verification** (SIG-W-20260426-009) — quick pull when bandwidth.
15. 🟡 **Wave 2 cross-agent outbox signals** — 8 candidates in ROADMAP; deferred until HERMES revival or new messaging pattern.
16. 🟡 **STATUS.md hygiene pass** — APR 30 PM LIVE TAPE + APR 29 catch-up sections now 17+ days stale; archive to `archive/STATUS_apr28_may1.md`; STATUS should be a snapshot not multi-week diary.
17. 🟡 **WALTER LIAISON calibration cycle 1** — trigger 2026-05-25 (14d) OR N=15 forward BOARD dispositions (early-fire).

**Top-3 priority for next boot:** Items 2 (expiry-day outcome log — clears Will-call queue) + 3 (WAL 10-Q drill — biggest unread information delta) + 5 (Investor Day Q&A — determines whether V2.1.1 or V2.2). Everything else negotiable.

