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
- [2026-03-31] MHLW wage data runs ~2 month lag. Release pattern: ~8th-9th of month.
## References
- [2026-04-11] **Primary data sources now wrapped by `AGENTS/SAM/scripts/` toolkit.** Run `boot.py` for one-command morning refresh. For one-off queries: `jgb_yields.py`, `jgb_auctions.py --date YYYY-MM-DD`, `cftc_jpy.py`, `mof_flows.py`, `fxy_options.py`, `thresholds.py`, `catalyst_countdown.py`. Source URLs documented in scripts and CLAUDE.md boot step 7.
- [2026-04-07] FORGE toolkit + yfinance commands moved to CLAUDE.md boot step 7 (permanent). Don't duplicate here.
- [2026-03-31] MOF ITS release schedule: mof.go.jp/english/policy/international_policy/reference/itn_transactions_in_securities/schedule.htm
- [2026-03-31] JGB auction calendar: mof.go.jp/english/policy/jgbs/auction/calendar/index.htm
- [2026-04-01] April 2026 auction calendar: mof.go.jp/english/policy/jgbs/auction/calendar/2604e.htm
- [2026-04-02] Vol/options monitoring sources: CME CVOL (JPVL) for JPY implied vol, Barchart for FXY options OI, Investing.com for USD/JPY risk reversals. All render dynamically — can't auto-scrape, need manual check or Perplexity. Full framework: research/outputs/VOL_OPTIONS_FRAMEWORK.md. (FXY options OI now auto-captured by `fxy_options.py`.)

## Session Notes

### CHANGES SINCE LAST SESSION (Apr 11 → Apr 13 market open)
- Hormuz blockade announced Apr 12 (Islamabad talks collapsed). Brent $95→$100.52 (+5.6%).
- MOF Apr 10 JGB data published: **10Y 2.439% — breached 2.40% stress threshold (confirmed).** 40Y 3.682% — prior 3.92% was data source error (21bp overstated). Reconciliation complete.
- USD/JPY 159.59 (0.3% from 160 intervention trigger). FXY $57.52 (at entry).

### LAST SESSION (Apr 12-13 — housekeeping + Monday market open)
- **Housekeeping audit:** Fixed stale data across all 5 boot files. THESIS had wrong BOJ date (23-24→28), stale CFTC/Brent/position numbers, header version mismatch. TIMELINE week labels and scenario rates corrected. CALENDAR pruned. MEMORY trimmed 5 redundant script findings. STATUS narrative cut to 2 lines. All logged to CHANGELOG.
- **Monday market open:** Boot script ran, MOF Apr 10 data validated both findings: 10Y breach real, 40Y overstated. STATUS and THESIS updated with confirmed levels.
- **Educated Will on:** What 10Y breach means for insurer Channel 1 (unrealized losses → ESR visibility → repatriation pressure), and why 40Y being lower than thought gives more time before mechanical (vs discretionary) selling.

### NEXT SESSION
1. **🔴 Tue Apr 14: 20Y JGB auction.** Run `jgb_auctions.py --date 2026-04-14` after Japan market close. BTC <2.0x = 🔴 signal to LIQUID, HENRY.
2. **🔴 Tue Apr 14: Insurer FY2026 plans window opens.** WebSearch for Fukoku, Nippon Life, Meiji Yasuda, Dai-ichi announcements. Update `insurers/TRACKER.md`.
3. **🟠 Wed Apr 15: Feb TIC data.** Japan UST selling confirmation (>$15B = stress case). Manual WebSearch.
4. **🔴🔴 DECISIVE — Thu Apr 16: MOF ITS weekly release.** `mof_flows.py` auto-pull. IF Apr 5-11 week shows >¥2T selling → execute Option C rebalance (Base 70→55, Stress 25→37, Crisis 5→8). Bump THESIS to v1.3. Send 🔴 signal to LIQUID, PROME.
5. **Wed Apr 22: Ceasefire expiry.** Effectively dead after blockade — watch for formal collapse.
6. **Tue Apr 28: BOJ MPM — live for hike to 1.00%.** Internal call ~60-65%.

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
