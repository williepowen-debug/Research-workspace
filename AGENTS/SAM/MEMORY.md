# SAM MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis or delete, never just accumulate.*

---

## Feedback
- [2026-03-31] Will values boot transparency — wants to know what SAM read, in what order, and whether the process is working well. Don't just orient silently; confirm orientation.
- [2026-03-31] Will thinks long-term about infrastructure. When proposing solutions, address scaling and durability, not just immediate need.
- [2026-04-01] Key dates were getting buried in STATUS.md. Will approved CALENDAR.md as standalone living doc — pure table format, forward-looking only, pruned weekly. Added to boot sequence as step 5.
- [2026-04-02] When explaining complex financial mechanics, Will needs the simplified version first. Start with the plain-English punchline, then layer in detail only if asked. He asked for a re-explain on hedge ratios/repatriation spiral — the second attempt (simpler) landed, the first (detailed) didn't.
- [2026-04-02] Will uses Perplexity for deep research and shares outputs. Treat Perplexity data as high-quality but verify framework logic independently. Will explicitly asked SAM to validate the vol/options framework rather than accepting it uncritically.
- [2026-04-11] **Script-defined alert thresholds MUST match THESIS scenario bucket definitions** — not invented independently. Built `mof_flows.py` with arbitrary "CRISIS ¥4T/4wk" threshold and reported MOF flows at "crisis pace" to Will. When Will asked "how dramatic would Option C be?" I re-checked and found: 4-week rolling was in THESIS stress-case range ($25-40B/mo), not crisis case ($100B+/mo). My "crisis" label was 3.5× too lenient relative to THESIS. Fixed script to calibrate at ¥1.4T elevated / ¥3.5T stress / ¥14T crisis based on THESIS midpoints. **Lesson:** when a script introduces a severity label (CRISIS/STRESS/etc.), that label must cross-reference THESIS.md or use distinct vocabulary. Don't allow label collision with canonical scenario names.
- [2026-04-11] Will prefers intellectually honest corrections over doubling down. When I over-reported "CRISIS PACE" and then had to correct to "STRESS CASE", he didn't push back on the retraction — he took the corrected read and approved the more conservative Option B. Lean toward restraint on thesis-level updates; the data may support it but one data point rarely justifies 15-25pp probability shifts.

## Findings
- [2026-03-31] PROME's SCRATCH.md is the single most useful file at boot for system-wide context. The "QUICKSTART" line and handoff notes give instant orientation.
- [2026-03-31] Inbox items from HERMES often lag behind STATUS.md — check for staleness before processing.
- [2026-03-31] EUR/JPY went unmonitored for 8 weeks and blew through RED (175) to 183. Cross-pair yen weakness can be a blind spot when USD/JPY dominates attention. Check EUR/JPY alongside USD/JPY.
- [2026-03-31] SocGen ¥7.5T "buying" figure from web searches was from 2025, not 2026 — always verify article dates on flow data.
- [2026-04-01] MOF cutting super-long issuance to ¥17T (17-year low) — they know demand is fragile. Context for interpreting auction BTC ratios.
- [2026-04-01] Mar 5 30Y auction: BTC 3.65x at 3.406% yield. Jan: 3.14x. Feb: firmer. Trend data for comparison when Apr 7 results come in.
- [2026-03-31] MHLW wage data runs ~2 month lag. Release pattern: ~8th-9th of month. Feb data expected ~Apr 7-9.
- [2026-04-11] **MOF JGB daily yield CSV: `mof.go.jp/english/policy/jgbs/reference/interest_rate/jgbcme.csv`** — authoritative, all tenors 1Y-40Y, ~1 business day lag. Clean CSV, no encoding issues. Replaces web searches for JGB yields entirely.
- [2026-04-11] **MOF weekly ITS CSV: `mof.go.jp/policy/international_policy/reference/itn_transactions_in_securities/week.csv`** — CP932 encoded (decode with `cp932`, NOT `shift_jis` — raises UnicodeDecodeError on some byte sequences). Periods use full-width Japanese dot "．" and tilde "～" not ASCII. Column 6 = "Long-term debt securities Net" under Portfolio Investment Assets — that's the repatriation signal. 1,109+ rows of weekly history available. Replaces tradingeconomics scraping.
- [2026-04-11] **CFTC JPY COT: `cftc.gov/dea/newcot/deafut.txt`** (deacot.txt is 404'd). Find "JAPANESE YEN - CHICAGO MERCANTILE EXCHANGE" row. Parse with csv.reader. Col 7 = OI, col 8 = Noncomm Long, col 9 = Noncomm Short, col 37 = OI WoW delta, col 38-39 = Noncomm Long/Short WoW deltas. Data releases Friday PM ET, reflects Tuesday data. **Always 3-day lag** — if your last read is >7 days old, you're looking at TWO releases back.
- [2026-04-11] MOF auction result page structure: 14-15 `<td>` cells in a single data row. `cells[0]` = security type (e.g., "30-Year"), `cells[6]` = competitive bids (¥B), `cells[7]` = accepted (¥B), `cells[9]` = yield at lowest (%), `cells[12]` = yield at average (%). BTC = cells[6]/cells[7]. Tail (bp) = (cells[9] - cells[12]) × 100.
- [2026-04-11] Normal JGB auction reference: BTC 3.0-3.5x, tail 0.5-2bp. Soft demand <2.8x, buyer strike <2.0x, quality problem tail >3bp. Apr 2 10Y auction (BTC 2.565x, tail 4.5bp) correctly flags "🟠 Soft demand + quality problem" with these cutoffs — matches TIMELINE's historical treatment.

## References
- [2026-04-11] **Primary data sources now wrapped by `AGENTS/SAM/scripts/` toolkit.** Run `boot.py` for one-command morning refresh. For one-off queries: `jgb_yields.py`, `jgb_auctions.py --date YYYY-MM-DD`, `cftc_jpy.py`, `mof_flows.py`, `fxy_options.py`, `thresholds.py`, `catalyst_countdown.py`. See also raw source URLs in Findings section above.
- [2026-04-07] FORGE toolkit + yfinance commands moved to CLAUDE.md boot step 7 (permanent). Don't duplicate here.
- [2026-03-31] MOF ITS release schedule: mof.go.jp/english/policy/international_policy/reference/itn_transactions_in_securities/schedule.htm
- [2026-03-31] JGB auction calendar: mof.go.jp/english/policy/jgbs/auction/calendar/index.htm
- [2026-04-01] April 2026 auction calendar: mof.go.jp/english/policy/jgbs/auction/calendar/2604e.htm
- [2026-04-02] Vol/options monitoring sources: CME CVOL (JPVL) for JPY implied vol, Barchart for FXY options OI, Investing.com for USD/JPY risk reversals. All render dynamically — can't auto-scrape, need manual check or Perplexity. Full framework: research/outputs/VOL_OPTIONS_FRAMEWORK.md. (FXY options OI now auto-captured by `fxy_options.py`.)

## Session Notes

### CHANGES SINCE LAST SESSION (Apr 11 morning → Apr 11 evening)
- Same trading session — this is a continuation of the Apr 11 morning boot, not a cross-session delta.
- Will requested SAM build a scripts toolkit modeled on REGINALD's. Built, tested, shipped across 3 phases (commits c44da1a1, 5ed7bbfc, fe4628ad).
- 4 STATUS-level data corrections surfaced on first automation run. Option B approved by Will — STATUS refreshed, LIQUID signal sent, CHANGELOG audit entry logged. Scenario weights held pending Apr 16 MOF release.

### LAST SESSION (Apr 11 afternoon/evening — tooling buildout + data audit)
- **Built `AGENTS/SAM/scripts/` toolkit** from scratch. 8 Python scripts + orchestrator + plan doc. Modeled on REGINALD's pattern but 4 scripts are Japan-macro-specific (JGB yields, auctions, CFTC, MOF flows). Full plan lives in `scripts/AUTOMATION_PLAN.md`. Phase 1: thresholds/catalyst countdown/FXY options. Phase 2: jgb_yields/jgb_auctions/cftc_jpy/mof_flows. Phase 3: boot.py orchestrator + CLAUDE.md boot step 7 rewrite + retired `tools/usdjpy_monitor.sh` to archive.
- **Boot sequence is now one command: `python3 AGENTS/SAM/scripts/boot.py`** — ~15 seconds for the full Japan-macro sweep.
- **Data audit findings (Option B executed):**
  - CFTC JPY: -72.9K → **-93,742** (STATUS was reading Mar 31 release, not Apr 7). 52.1% of Jul 2024 peak (was 38%). Shorts built +17K WoW — still accumulating, not covering.
  - JGB yields: 10Y 2.41% / 40Y 3.92% → MOF authoritative Apr 9: **10Y 2.397% / 40Y 3.678%**. The 40Y 3.92% figure is 17bp above the MOF April peak and could not be reconciled — likely prior-session data source error. 10Y actually NOT breached the 2.40% stress threshold (sits 1.3bp below). Apr 10 MOF publishes Mon — will confirm then.
  - MOF LT-debt flows: Prior STATUS "¥2.2T / 3wk / 2x base case" → Actual 4-week rolling **¥-5.0T ($-33B)**, squarely in THESIS stress-case range. Latest single week (Mar 29-Apr 4) was ¥-2.46T — 2.5× prior weeks. Single extreme week + 4-week in stress range, but 12-week still at base/stress boundary. NOT yet regime change.
  - FXY options (net-new visibility, not a correction): Aggregate P/C 0.06x, 83.9% of call OI in $58-65 zone, 19,014 Jun 18 $58 calls — institutional positioning is directionally aligned with SAM thesis.
- **Correction to self:** Initial report to Will used "CRISIS PACE" language for MOF flows which was from my arbitrary script threshold, NOT from THESIS scenario bucket definitions. Will asked me to quantify how dramatic an Option C rebalance would be. Re-reading the scenario buckets forced me to realize: 4-week rolling is STRESS case, not crisis case. Corrected to Will in reply #988. mof_flows.py thresholds rewritten to match THESIS language ($25-40B/mo = stress, $100B+/mo = crisis). Lesson in next session note.
- **Will approved Option B** (not C): STATUS refresh + LIQUID signal + CHANGELOG data audit entry + Apr 16 MOF checkpoint. Scenario weights held. This is intellectually honest — one data point doesn't justify a 15-25pp thesis shift.
- Still have not used --quick flag or tested boot.py in offline mode. Fine for now.

### NEXT SESSION
1. **🔴 Mon Apr 13: Verify MOF Apr 10 JGB yields when MOF publishes.** If 40Y < 3.8% → prior-session STATUS cite was wrong (very likely); if >3.85% → there was a real Apr 10 spike we missed the data source for. Update CHANGELOG entry accordingly.
2. **🔴 Mon Apr 14: 20Y JGB auction** (2 trading days away). Run `jgb_auctions.py --date 2026-04-14` after market close. Will auto-parse MOF results page. Alert if BTC <2.0x → signal LIQUID, HENRY.
3. **Mon-Fri Apr 14-18: Insurer FY2026 plans begin.** Fukoku most likely first. Build insurer-specific tracker in Phase 4 if volume justifies. Otherwise manual web searches.
4. **🟠 Tue Apr 15: Feb TIC data.** Japan UST selling confirmation (>$15B = stress case). No automation yet — manual WebSearch.
5. **🔴🔴 DECISIVE — Thu Apr 16 JST / Wed Apr 15 ET: MOF ITS weekly release.** `mof_flows.py` run will auto-pull new data. IF Apr 5-11 week shows another ¥2T+ weekly outflow → execute Option C rebalance (Base 70→55, Stress 25→37, Crisis 5→8). Bump THESIS to v1.3. Send 🔴 signal to LIQUID, PROME.
6. **Wed Apr 22: Ceasefire expiry.** Original 2-week clock.
7. **Tue Apr 28: BOJ MPM — live for hike to 1.00%.** Internal call ~60-65%, market ~45-50%.

### INFRASTRUCTURE CHANGES (persistent)
- Boot step 7 in `AGENTS/SAM/CLAUDE.md` now says "preferred: run `boot.py`". Old manual instructions preserved as fallback.
- `AGENTS/SAM/tools/usdjpy_monitor.sh` retired — moved to `archive/tools/`. Had a stale "moltbot" VPS path from an old migration. Functionally replaced by `scripts/thresholds.py`.
- All 6 new TSV workbook files seeded with live data:
  - `CATALYSTS.tsv` — 13 events forward-looking
  - `FXY_OPTIONS.tsv` — 4 expiries as of Apr 11
  - `JGB_YIELDS.tsv` — 7 days from MOF CSV
  - `JGB_AUCTIONS.tsv` — Apr 2/7/9 parsed from MOF pages
  - `CFTC_JPY.tsv` — Apr 7 snapshot
  - `MOF_FLOWS.tsv` — 1,109 rows of historical weekly data
