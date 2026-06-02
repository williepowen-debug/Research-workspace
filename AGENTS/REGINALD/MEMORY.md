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
- [2026-06-02] **Scope-clean sessions:** Will will explicitly fence a session ("REGINALD files only, no messaging, no position decisions/analysis"). When fenced, refreshing facts (prices, dates, FRED data) and marking resolved events is in-scope hygiene; recomputing EV/overvaluation, sending outbox replies, and making roll calls are out. Flag stale-but-load-bearing values (e.g. SCENARIOS spot price) rather than recomputing — "flag don't re-rate."

## Findings
- [2026-04-02] `scripts/market.py` pulls live prices via yfinance. Must run with `.venv/bin/python3` from workspace root (not from AGENTS/REGINALD/).
- [2026-04-30] **FRED data via fetch.py.** Hardcoded fallback API key at `FORGE/tools/market-data/fetch.py:40` (also `AGENTS/CARL/scripts/consumer_pulse.py:25`) — works without `FRED_API_KEY` env var. Invocation: `.venv/bin/python3 FORGE/tools/market-data/fetch.py fred <SERIES_ID> --periods <N>`. Verified series: BAMLH0A0HYM2 (HY OAS), BAMLH0A3HYC (CCC OAS), ICSA (claims), SOFR, IORB. Note: hardcoded key in committed source = security smell.
- [2026-06-02] **FRED is T+1 (PROME convention, SIG 5/21).** FRED publishes OAS/yield/claims series next-day, so the latest FRED value during any trading day is yesterday's close at best. Date-stamp FRED cites in STATUS/THESIS/SCENARIOS/KB (e.g. `HY OAS 272bps [FRED 6/1 close]`); yfinance rows are intraday-live (`WAL $80.20 [yfinance live]`). Never call a FRED number "live/today" without verifying the obs date. Note: WAL/THESIS + SCENARIOS carry NO FRED cites (bank-fundamental files) — convention only bites STATUS + cross-agent triggers. Full ref: `FORGE/tools/market-data/README.md` § Citation Convention.
- [2026-06-02] **Thesis-version bumps must sweep PREDICTIONS *consumers*, not just the canonical tsv.** v2.2 ratcheted REG-24 60→70% / REG-25 55→75% in `workbook/PREDICTIONS.tsv` on 5/21, but STATUS.md PREDICTIONS section + CALENDAR checkpoint table were left at 60/55 — found stale 12 days later. When a prediction confidence changes, grep every file that *displays* it (STATUS, CALENDAR), not just the source tsv. Same family as the "Verify State Before Propagating" rule.
- [2026-05-01] **Q1 Call Report data access pattern.** FDIC SDI (banks.data.fdic.gov) lags 30-60 days post-quarter. For early access use SEC EDGAR (data.sec.gov/submissions/CIK<padded>.json) for 10-Qs (filed May 4-10 for accelerated filers; contain NDFI + AOCI but NOT MI3/RCON2746). MI3 requires FFIEC CDR Call Reports — public CDR ManageFacsimiles.aspx is ASP.NET viewstate/cookie-locked, NOT curl-accessible. Practical answer: wait for FFIEC PDD bulk update (~mid-May for Q1) or rely on 10-Q indirect signal.
- [2026-04-02] OZK price sources can conflict ($46 vs $49 in same session) — always verify at broker when discrepancy >5%.
- [2026-04-12] Wasatch fund commentaries: wasatchglobal.com/wp-content/uploads/strategy-and-fund-documents/ — quarterly fund PDFs.
- [2026-04-16] pdfminer works for PDF text extraction (`.venv/bin/python3`, `from pdfminer.high_level import extract_text`). poppler-utils not installed.
- [2026-04-16] CFG 10-K HTML from EDGAR has inline-XBRL markup; use regex `re.sub(r'<[^>]+>',' ',html)` not BeautifulSoup `.get_text()`.
- [2026-04-19] **Paywall map:** Forbes.com, Seekingalpha.com, Journalrecord.com (Reuters wire) return 403 to Anthropic WebFetch. Workable substitutes: MarketScreener, PrismNews, Sharecafe (Reuters), Motley Fool / Investing.com (SA transcripts).
- [2026-04-22] **LAM = Leucadia Asset Management = Jefferies subsidiary** (post-2013 Leucadia/Jefferies merger). Semantic mapping critical for V2 fraud chain — WAL's $126.4M LAM charge-off is on the Jefferies rail.
- [2026-04-22] **Quartr MCP is subscription-gated** — returned `subscription_required`. WebFetch + direct IR page links or user-provided PDFs are the workaround.
- [2026-04-24] **SEC EDGAR direct-fetch pattern** — WebFetch 403s on all sec.gov paths, but `curl` with `User-Agent: REGINALD research willie@research.local` returns 200. Canonical: `https://data.sec.gov/submissions/CIK<padded>.json` → `https://www.sec.gov/Archives/edgar/data/<cik>/<accession-no-dashes>/<filename>`. Accession numbers can start with the FILER's CIK, not the COMPANY's — always cross-check via data.sec.gov.
- [2026-04-24] **Q4CDN IR PDF hosting** — `https://s21.q4cdn.com/<subscriber-id>/files/doc_financials/<year>/<qnum>/<FILENAME>.pdf`. WAL subscriber-id `328636679`. Filename conventions vary per bank.
- [2026-05-08] **yfinance option chain extraction** — `yf.Ticker('SYM').option_chain('YYYY-MM-DD').puts` returns DataFrame (strike/lastPrice/bid/ask/volume/openInterest/impliedVolatility). `.options` gives expiry list. Greeks NOT included — compute via Black-Scholes manually. Friday-close marks; thin chains can show $0 bid even when last is meaningful.
- [2026-05-08] **Gitignore directory-exclude breaks negation** — `dir/` + `!dir/*.md` does NOT work (git won't traverse into ignored dirs). Fix: `dir/*` + `!dir/*.md`. Verify with `git check-ignore -v`.
- [2026-05-08] **10-Q SEC EDGAR fetch is XBRL-heavy** — typical bank 10-Q 3-4MB raw HTML, ~350KB stripped. Strip with `re.sub(r'<[^>]+>',' ',html)` then `re.sub(r'\s+',' ',text)`. Standard terms (NDFI, "fund finance") often DON'T match — banks categorize differently (CFG: "Capital call facilities" / "Secured private credit finance"). Search broad first, then narrow.
- [2026-05-08] **Phantom-detection heuristic** — When a position is referenced in dashboard files but NOT in POSITIONS.md AND NOT in FORGE/STATUS.md, it's stale-tracking. Closed positions need a propagation step to dependent docs. Grep ground-truth (POSITIONS / FORGE) before recommending action on any "decide what to do with X" task.

## References
- [2026-05-10/11] **LIAISON channel WALTER ↔ REGINALD — Turns 1-5 CLOSE-CONVERGED in <13 hr UTC** — Path: `AGENTS/REGINALD/handoff_WALTER/{README.md, LIAISON.md}`. All 8 Qs LOCKED both sides; 5 instantiated files. REGINALD-side: `registry/THRESHOLDS.tsv` 8-row REG-T-NN + `board/BOARD_LOG.tsv` 11-col (32-row backfill stub) + `CLAUDE.md` Boot Step 9b 3-tier BOARD diff scan. **Boot 9b grep schema: `signal_role: cluster_mediating` NOT `cluster_mediating: true`.** `bank_transmission` enum 8-val pre-cosigned for V0_9_STACK.md. Calibration cycle 1 trigger 2026-05-25 (passed — not run) OR N=15 forward BOARD dispositions. Channel state: POST-WRAP CALIBRATION-PENDING.
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

⚠️ **Open question:** Does the full 12-day tape retrace (WAL reclaimed $78; all 4 stress signals faded) weaken the WAL bear-medium read, or is it just risk-on beta with the thesis intact pending the late-Jul Q2 print? My logged call: **print-dependent, not invalidated** — and the credit bifurcation (CCC widening to 946 / HY 272, ratio 3.48x) is the one signal that DIDN'T fade, mildly thesis-supportive. The binary that resolves it stays the same: Q2 print shows ONE Office walk-away ($99M only → v2.2 may overstate) or 2+ (→ v2.5/v3).

**Pending Will calls:** None — analysis + messaging deferred by session scope (Will fenced this session to REGINALD files only).

### CHANGES SINCE LAST SESSION (5/21 → 6/2, 12-day gap)
Tape fully retraced the 5/15-5/21 stress regime: WAL $77.63→**$80.20** (reclaimed $78), Brent $106.93→**$95.91** (−$15, Hormuz re-spike unwound), 10Y 4.62%→**4.46%** (−16bps), VIX 17.61→**15.73** — 4-for-4 risk-on. FRED: HY OAS 282→**272** [6/1], CCC 909→**946** [6/1] (ratio 3.22x→**3.48x** — bifurcation widening, the lone non-fading signal), claims 189K→**215K** [5/23], SOFR-IORB −2→**0bps**. v2.2 weights/positions untouched.

### LAST SESSION (6/2 — boot + file-tree catch-up after 12-day gap)

**Scope:** Will fenced the session to REGINALD files only — no messaging/outbox, no position decisions/analysis. Pure factual hygiene + close write-backs. Ran as 7 phases with a checkpoint between each.

1. **STATUS.md** — Signal Dashboard + Cross-Agent Triggers + THRESHOLD table refreshed to 6/2 tape + 6/1 FRED; adopted PROME's date-stamp convention; WAL note flipped 🔴 breached → 🟢 reclaimed $78; macro-read rewritten as factual 6/2 observation; Brent THESIS-channel price refreshed with status re-rate deferred; **caught + fixed STATUS PREDICTIONS section stale at 60/55** (canonical PREDICTIONS.tsv was already 70/75 from v2.2). 182 lines.
2. **CALENDAR.md** — deleted the fully-past MAY section (all tracked in ROADMAP); JUNE now leads with Jun 18 cluster + AOCI close prominent; added LATER section (Aug/Oct OZK catalysts); pruned resolved prediction checkpoints; synced REG-24/25 to 70/75.
3. **SCRATCH.md** — pruned 4 sections >2wk (5/1, 5/8, 5/10-11, 5/11); rescued 3 orphaned research threads (Juris banking, Slide 113 stress test, Slide 89) before deleting their sections.
4. **WAL/ FRED hygiene** — grep confirmed ZERO FRED cites in THESIS/SCENARIOS (correct by design — bank-fundamental files; macro → STATUS). Added one staleness flag to SCENARIOS header ($77.63 → 6/2 $80.20; EV math NOT recomputed).
5. **ROADMAP.md** — +2 threads (Jun 18 cluster reply owed; SCENARIOS EV refresh deferred); rebuilt Awaiting Data forward-from-6/2 with a "fired during gap — unverified" block; +3 rescued investigations; +6/2 resolved entry; pruned 5/01-and-earlier resolved block.
6. **MEMORY.md** — this rewrite (also de-bloated Session Notes 225→~130 lines; killed the fake "pruned to 1 line" May 8 block + stale recaps).
7. **Git** — closeout commit (pending).

**Read but NOT actioned (held per scope):** 2 PROME inbox signals — FRED convention (5/21, adopted) + Jun 18 cluster bank-trigger calibration (5/22, reply drafted in-conversation but not written to outbox). Key calibration insight surfaced: Q2-print catalyst is post-Jun-18-expiry, so the bank puts are timeline-orphaned — any roll must be Sep, not Jul; EGBN $25P is the only roll candidate (closest to money); else default let-expire / regime-break only.

**Will conversation moments:** model switched mid-session (Opus 4.7 → 4.8); Will asked for the credit-bifurcation signal to be explained (kept in STATUS, no separate tripwire); Will asked whether zero FRED cites in WAL meant it was "built wrong" — explained it's correct doc-ownership architecture, the real WAL staleness is the SCENARIOS EV math (deferred). Will checkpointed after each phase.

### NEXT SESSION — messaging + analysis backlog (both deferred this session)

1. **Boot normally** — git pull, boot docs, market.py, inbox scan, **BOARD diff scan Step 9b** (fixed grep `signal_role: cluster_mediating`) — now 12+ days of unread BOARD inflow.
2. 🟠 **Jun 18 cluster calibration reply to PROME** — write `outbox/REPLY-PROME-2026-05-22-bank-trigger-calibration.md`. Deadline (5/24) lapsed so draft levels stand, but cluster live (decision window ~Jun 11). My slice: KRE two-tier $66 caution / $63 arm; WAL $73 + qualitative C-suite/2nd-walkaway arm; **rolls Sep not Jul**; EGBN only roll candidate; drop late-MI3 hard trigger; no interim trigger before 6/16 (print is post-expiry).
3. 🟠 **MI3 / FFIEC PDD status check** — now 2.5wk+ overdue; if available run v2.2 calibration table.
4. 🟠 **WAL SCENARIOS EV-math refresh** — recompute overvaluation at $80.20 (~14%→~19% vs EV $67.98), weeks-to-expiry, position-rec column. The deferred analysis task.
5. 🟠 **APO Q1 post-print integration** (now ~4wk stale) — Atlas SP segment, warehouse book, non-bank servicer counterparty.
6. 🟠 **OZK 10-Q recheck** (OZK peer primary; REGINALD cohort-fade info pickup).
7. 🔴 **BOARD action-signal backlog** — 13 ACTION signals on 5/11 + 12 days new inflow; no disposition rows written.
8. 🟡 **PROME ZION scaffold-fill** (inbox, now 3wk+) — substantive new work, dedicated session.
9. 🟡 **CARL handover signal** (inbox, now ~1mo). Lower urgency.
10. 🟡 **WALTER LIAISON calibration cycle 1** (trigger 5/25 passed).
11. 🟡 **Q&A transcript hunt** + **cross-bank life-science #3 watch** + investigations (Juris banking / Slide 113 / Slide 89).

**Git: closeout commit pending.**

### LAST SESSION (5/21 — 10-Q drill + V2.2 ship) [1-line recap]
WAL Q1 10-Q drilled (`research/WAL_10Q_DRILL_2026-05-21.md`); V2 inventory CLEAN; 🔴 B1 fired via $99M life-science office walk-away (10-Q subsequent event) + V4 Curley resignation; v2.1→v2.2 shipped (Bear-medium 30%, EV $67.98, REG-24 70%/REG-25 75%); STATUS hygiene 309→182; May 15 cluster cleared. Files: THESIS/SCENARIOS/2x CHANGELOG/PREDICTIONS/STATUS/CALENDAR/POSITIONS.

### LAST SESSION (5/15-17 — Investor Day FINDINGS + clean closeout) [1-line recap]
`WAL/INVESTOR_DAY_FINDINGS_2026-05-12.md` shipped T+3; Bucket scoring A=U1 B/C/D=U2 **E=B3 FIRED** (mgmt held 25-35bps NCO despite Q1 39bps); recommended v2.1.1 (superseded by 5/21 v2.2). SSB $95P expiry-day ladder. Commit `6a20710a`, pushed by WALTER `1b37fccc`.
