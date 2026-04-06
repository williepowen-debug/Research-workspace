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
- [2026-03-31] MOF ITS release schedule: mof.go.jp/english/policy/international_policy/reference/itn_transactions_in_securities/schedule.htm
- [2026-03-31] JGB auction calendar: mof.go.jp/english/policy/jgbs/auction/calendar/index.htm
- [2026-04-01] April 2026 auction calendar: mof.go.jp/english/policy/jgbs/auction/calendar/2604e.htm
- [2026-04-02] Vol/options monitoring sources: CME CVOL (JPVL) for JPY implied vol, Barchart for FXY options OI, Investing.com for USD/JPY risk reversals. All render dynamically — can't auto-scrape, need manual check or Perplexity. Full framework: research/outputs/VOL_OPTIONS_FRAMEWORK.md

## Session Notes

### CHANGES SINCE LAST SESSION (Apr 2 → Apr 5)
- ESCALATION RESUMED: Bushehr nuclear plant struck Apr 4, Mahshahr petrochemical hub hit (5 dead, 170 injured). 30+ universities bombed. De-escalation narrative dead.
- Oil head-fake confirmed: Brent $101→$109 (+8% Fri). Apr 1 pullback fully reversed. Phase 1 oil dynamics reasserted.
- USD/JPY back to ~160 — MOF intervention trigger retested. FXY $57.54 (grinding).
- JGB 10Y 2.39% (1bp from 2.40% threshold). JGB 30Y 3.68%.
- Strike pause expires Apr 6 (Sun) 8pm ET — strikes already resumed on Apr 4-5, largely symbolic.
- CFTC: last confirmed reading -67.8K (Mar 20). Apr 4 release not yet confirmed.

### LAST SESSION (Apr 5)
- Booted via Telegram (Will pinged). Full spawn protocol executed.
- Integrated Norinchukin CLO contagion research (Will shared via Telegram):
  - THESIS v1.1→v1.2: Added hedge ratio collapse (44.4%, 14yr low), institutional framing ($3.0-3.5T), GPIF non-risk, Norinchukin CLO shrinkage, USD/JPY 130-135 threshold
  - Saved research to research/outputs/NORINCHUKIN_CLO_CONTAGION.md
  - CHANGELOG updated with full v1.2 entry
  - STATUS.md refreshed: market data table updated, Norinchukin integration section added
  - Outbox signal written for LIQUID: hedge ratio + Norinchukin + UST holdings
- Key new insight: hedge ratio 44.4% means system MORE exposed than we modeled. Repatriation base case may be conservative.

### NEXT SESSION
1. **Apr 7 (Mon): 30Y JGB auction** — THE critical event. BTC vs Mar 3.65x at 3.7%+ yield. If <2.0x = 🔴 LIQUID/HENRY/PROME.
2. Apr 7-9: Feb wage data (MHLW). Low priority unless surprise.
3. Apr 7-14: Big 4 insurer FY2026 investment plans. Signal LIQUID on any announcement.
4. Check CFTC Apr 4 release — have JPY shorts grown past -67.8K?
5. Check MOF FY-end week flow data (still pending from last session).
6. Refresh TRADE.md — update position to 8 shares, fix stale prices.
7. 2 outbox items STILL pending HERMES: BROCK private credit + SK refiner. Flag to PROME.
8. Apr 14-18: Vol check window (pre-BOJ). Ask Will for CVOL/FXY OI/RR data.
