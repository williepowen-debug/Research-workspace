# SAM MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis or delete, never just accumulate.*

---

## Feedback
- [2026-03-31] Will values boot transparency — wants to know what SAM read, in what order, and whether the process is working well. Don't just orient silently; confirm orientation.
- [2026-03-31] Will thinks long-term about infrastructure. When proposing solutions, address scaling and durability, not just immediate need.
- [2026-04-01] Key dates were getting buried in STATUS.md. Will approved CALENDAR.md as standalone living doc — pure table format, forward-looking only, pruned weekly. Added to boot sequence as step 5.
- [2026-04-02] When explaining complex financial mechanics, Will needs the simplified version first. Start with the plain-English punchline, then layer in detail only if asked. He asked for a re-explain on hedge ratios/repatriation spiral — the second attempt (simpler) landed, the first (detailed) didn't.
- [2026-04-02] Will uses Perplexity for deep research and shares outputs. Treat Perplexity data as high-quality but verify framework logic independently. Will explicitly asked SAM to validate the vol/options framework rather than accepting it uncritically.

## Findings
- [2026-03-31] PROME's SCRATCH.md is the single most useful file at boot for system-wide context. The "QUICKSTART" line and handoff notes give instant orientation.
- [2026-03-31] Inbox items from HERMES often lag behind STATUS.md — check for staleness before processing.
- [2026-03-31] EUR/JPY went unmonitored for 8 weeks and blew through RED (175) to 183. Cross-pair yen weakness can be a blind spot when USD/JPY dominates attention. Check EUR/JPY alongside USD/JPY.
- [2026-03-31] SocGen ¥7.5T "buying" figure from web searches was from 2025, not 2026 — always verify article dates on flow data.
- [2026-03-31] MOF weekly data available on TradingEconomics (tradingeconomics.com/japan/foreign-bond-investment) with ~1 week lag. More accessible than MOF PDFs which can be encrypted.
- [2026-03-31] MHLW wage data runs ~2 month lag. Release pattern: ~8th-9th of month. Feb data expected ~Apr 7-9.
- [2026-04-01] MOF JGB auction results published same day (JST afternoon). URL pattern: mof.go.jp/english/policy/jgbs/auction/calendar/eresul/eresul{YYYYMMDD}.htm. Also accessible via WebFetch for the monthly calendar page (2604e.htm = April).
- [2026-04-01] MOF cutting super-long issuance to ¥17T (17-year low) — they know demand is fragile. Context for interpreting auction BTC ratios.
- [2026-04-01] Mar 5 30Y auction: BTC 3.65x at 3.406% yield. Jan: 3.14x. Feb: firmer. Trend data for comparison when Apr 7 results come in.

## References
- [2026-03-31] MOF weekly flows: tradingeconomics.com/japan/foreign-bond-investment (easier than MOF PDFs)
- [2026-04-07] FORGE toolkit + yfinance commands moved to CLAUDE.md boot step 7 (permanent). Don't duplicate here.
- [2026-03-31] MOF ITS release schedule: mof.go.jp/english/policy/international_policy/reference/itn_transactions_in_securities/schedule.htm
- [2026-03-31] JGB auction calendar: mof.go.jp/english/policy/jgbs/auction/calendar/index.htm
- [2026-04-01] April 2026 auction calendar: mof.go.jp/english/policy/jgbs/auction/calendar/2604e.htm
- [2026-04-02] Vol/options monitoring sources: CME CVOL (JPVL) for JPY implied vol, Barchart for FXY options OI, Investing.com for USD/JPY risk reversals. All render dynamically — can't auto-scrape, need manual check or Perplexity. Full framework: research/outputs/VOL_OPTIONS_FRAMEWORK.md

## Session Notes

### CHANGES SINCE LAST SESSION (Apr 7 → Apr 8)
- 2-WEEK CEASEFIRE reached 90 min before Trump's 8pm deadline. Hormuz reopening. Pakistan talks Fri Apr 11.
- Brent CRASHED $110 → $91.14 (-16.6%). $1 from $90 threshold.
- USD/JPY 159.81 → 158.18 (-1.0%). FXY gapped to $58.06 (+1.1%). Position green.
- Feb wage data BEAT: real +1.9%, nominal +3.3%, base pay +3.3% (34-year high).
- JGB 30Y eased 3.70% → 3.59%. Yen strengthening vs USD only (EUR/JPY 185 flat).

### LAST SESSION (Apr 8)
- Booted via Telegram. Caught BOJ rate discrepancy in THESIS.md (0.50% → should be 0.75%). Fixed.
- Ceasefire analysis: thesis accelerating, oil is noise, wages are signal. Ceasefire likely fragile.
- Position: hold 8 shares, wait for dip to add Tranche 2 at $57-57.50.
- Created SIGNAL_INTAKE.md (WALTER routing spec). Added to CLAUDE.md file table.
- Will building group chats. SAM core group: SAM + LIQUID + HENRY.
- Diagnosed git collision: LIQUID's push/pull/stash cycle overwrote SAM's uncommitted edits. Fixed root CLAUDE.md pull protocol (check for other agents' uncommitted work before pulling). Added Step 0 (git pull) to boot sequences for SAM, RED, REGINALD, CARL.
- STATUS.md was overwritten 4 times by sync issues. Final version committed to prevent recurrence.

### NEXT SESSION
1. **Ceasefire durability** — has Brent held below $95?
2. **Pakistan talks Apr 11** — outcome?
3. **Big 4 insurer FY2026 plans** — Fukoku first (~Apr 14-18). Update TRACKER.md.
4. **20Y JGB auction Apr 14**
5. **Feb TIC data Apr 15** — Japan UST selling confirmation
6. **Vol check Apr 14-18** — pre-BOJ, CVOL compressed = cheaper options
7. **Ceasefire expiry Apr 22** — next binary
8. **BOJ Apr 28** — hike to 1.00% (~70%)
