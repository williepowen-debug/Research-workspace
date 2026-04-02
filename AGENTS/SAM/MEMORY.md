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

### CHANGES SINCE LAST SESSION (Apr 1 → Apr 2)
- Trump speech: NO exit plan, NO Hormuz reopening. De-escalation narrative collapsed.
- Brent reversed $102→$109 (+7%). Phase 1 oil dynamics reasserting.
- USD/JPY weakened 158.42→159.68. Back toward 160 intervention trigger.
- 10Y JGB auction WEAK: BTC 2.56x, tail 0.36 (widest since Aug '24), coupon 2.4% (28yr high).
- S&P -1.5%, Nasdaq -2.1%.

### LAST SESSION (Apr 2)
- Boot process audit → 6 structural fixes to CLAUDE.md (new boot order, market refresh step, doc ownership rules, session notes template, predictions at boot, CHANGES SINCE section)
- STATUS.md trimmed ~34 lines redundancy, refreshed with live market data + auction results
- CALENDAR.md: marked Apr 2 auction ✅. TIMELINE.md: Apr 2 resolved + branch points updated.
- Resolved SAM-06 → CONFIRMED TRUE. Prediction scoreboard: 5 true, 0 false, 3 open.
- Gap audit: filled 20Y auction blind spot (Feb 3.08x, Mar 3.25x — improving trend). Updated EUR/JPY (183.84, still RED). Searched for BOJ post-Tankan comments (none yet) and insurer FY2026 plan previews (none yet).
- NEW: Built vol/options monitoring framework with Will (via Perplexity research):
  - research/outputs/VOL_OPTIONS_FRAMEWORK.md — full technical reference (CVOL, UpVar/DnVar, FXY OI, risk reversals, convergence signal)
  - 4 new workbook vectors: VX-SAM-12.00 (convergence), 12.01 (CVOL ~9), 12.02 (FXY P/C ~0.06), 12.03 (risk reversals, est. positive)
  - Key insight: all three vol signals complacent = market NOT pricing our thesis yet = we're early, not wrong
- NEW: Created STRATEGY.md at SAM root — decision playbook (when to add/hold/exit, vol signals mapped to position decisions, 5-stage framework, asymmetry table)
- Educated Will on: insurer hedge ratio spiral mechanics, stage framework, trade patience
- Will agreed: hold 8 shares, don't add into headwind, let triggers work
- TRADE.md is STALE (Mar 30, shows 4 shares, some prices may be wrong) — needs refresh next session

### NEXT SESSION
1. Apr 3: Check MOF FY-end week flow data (w/e Mar 28). If net selling >¥1T = 🟠 LIQUID signal.
2. Apr 4 (Fri): CFTC positioning update — have JPY shorts grown beyond -67.8K?
3. Apr 6: Strike pause expiry. Did strikes resume? Oil impact. BINARY.
4. Apr 7: 30Y JGB auction — THE stress test. BTC vs Mar's 3.65x. If <2.0x = 🔴 signal LIQUID/HENRY/PROME.
5. Apr 7-9: Feb wage data (MHLW). Low marginal value unless surprise negative.
6. Apr 7-14: Big 4 insurer FY2026 investment plans. Signal to LIQUID whatever they announce.
7. Refresh TRADE.md — update position to 8 shares, fix stale prices, align with STRATEGY.md.
8. 2 outbox items STILL pending HERMES: BROCK private credit + SK refiner. Flag to PROME.
9. Apr 14-18: CRITICAL vol check window (pre-BOJ Apr 23-24). Ask Will for CVOL/FXY OI/RR data.
