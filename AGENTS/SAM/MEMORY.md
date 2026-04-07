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

### CHANGES SINCE LAST SESSION (Apr 6 → Apr 7)
- U.S. struck 50+ military targets on Kharg Island overnight (military, not oil infra — yet). Maximum escalation into Trump 8pm ET deadline.
- Trump: "a whole civilization will die tonight" if no deal. Iran rejected ceasefire. "Highly unlikely" to postpone.
- Brent $109 → $110-111 (+3%). Oil rising on deadline pressure.
- USD/JPY 159.70 → 159.81. FXY $57.53 → $57.44 (drifting lower — oil headwind persists, Phase 1 in force).
- DXY fell below 100 — dollar broadly weak, but yen weakening anyway = oil import cost dominating.
- JGB 10Y hit 2.40% — THRESHOLD BREACHED. Highest since July 1997.
- 30Y JGB auction: BTC 3.11x, tail 1.3bp at 3.70% coupon. PASSED. Demand held at record yields.
- BOJ April hike probability ~70% (market consensus, up from 35-40% last week).

### LAST SESSION (Apr 7)
- Booted via Telegram. Full spawn protocol executed.
- CRITICAL DATA ERROR: Web search returned FXY $58.50 (secondary aggregator). Real price $57.44. Built false "yen strengthening into oil" narrative, had to correct. Lesson saved to auto-memory: always cross-check ETF vs underlying FX before building narrative.
- Updated STATUS.md with corrected Apr 7 data: auction, Kharg, 10Y breach, corrected FXY.
- Updated TRADE.md: auction ✅, BOJ hike prob 70%.
- Updated CALENDAR.md: auction ✅, geopolitical refresh, BOJ prob 70%.
- Updated TIMELINE.md: Apr 6 strike pause resolved (BEAR — Kharg struck), Apr 7 auction resolved (BULL — BTC 3.11x), Apr 7 deadline added as pending branch point, JGB 10Y breach documented.
- Updated THESIS.md: 10Y threshold from "2bps away" → "BREACHED."
- Researched Big 4 insurer FY2026 plans: no formal announcements yet (expected Apr 14-25), but pre-announcement signals overwhelmingly confirm repatriation thesis.
- **Built new insurers/ subfolder** with TRACKER.md + 7 per-insurer profiles (nippon-life, meiji-yasuda, dai-ichi, sumitomo, fukoku, norinchukin, japan-post). Updated CLAUDE.md file table.
- Will working on new signal/messaging system — leave outbox alone.

### NEXT SESSION
1. **Trump deadline aftermath** — check what happened at 8pm ET Apr 7. Energy infra struck? Deal? Delay? Update STATUS + TIMELINE accordingly. Oil direction is THE variable.
2. **Feb wage data (MHLW)** — expected Apr 7-9. Low priority unless surprise negative.
3. **Big 4 insurer FY2026 plans** — Fukoku expected ~Apr 14-18 (first mover). Watch for any early announcements. Update insurers/TRACKER.md.
4. **MOF FY-end week flow data** — still pending from prior session.
5. **3 outbox signals still in outbox** — Will reworking mail system, leave alone.
6. **Apr 14-18: Vol check window (pre-BOJ).** Ask Will for CVOL/FXY OI/RR data.
7. **20Y JGB auction Apr 14** — second super-long test. If 30Y passed at 3.11x, 20Y should be fine, but watch.
