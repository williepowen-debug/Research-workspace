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

### CHANGES SINCE LAST SESSION (Apr 9 → Apr 11)
- **Islamabad Talks LIVE today** — first DIRECT US-Iran negotiations since 1979. Vance/Witkoff/Kushner vs Ghalibaf/Araghchi. Sharif mediating. Early signals: "some progress" on Lebanon ceasefire, "movement on unfreezing" Iranian assets. Lebanon carve-out remains the contention.
- **JGB 10Y at 28-year high**: 2.41% (vs 2.39% Apr 9). 40Y at 3.92% (+7bp). Market pricing aggressive BOJ normalization.
- **USD/JPY 159.24** (vs 159.16 Apr 9, peaked 159.64 Apr 10). Yen drifting, still in intervention zone.
- **FXY $57.64** (vs $57.69 Apr 9). Essentially flat at entry. 8 shares.
- **Brent $95.20** (down from $98.23 Apr 9). War premium easing on talks.
- A parallel session ran Apr 10 — committed STATUS.md update with "BOJ hike odds rising" narrative. Created merge conflict with my Apr 9 stash (resolved this session in favor of Apr 10 base + Apr 11 refresh).
- Hormuz reopening was theater (Will confirmed Apr 9): 3 ships vs 135/day normal, 800+ stuck.

### LAST SESSION (Apr 9 → Apr 11 closeout)
- Booted Apr 9 via Telegram. Found stale stash from prior session causing merge conflicts in CARL/REGINALD/BRENT/RED files — aborted cleanly with `git checkout -- .` (left stale stash in stash list — flagged to Will).
- Market refresh Apr 9: USD/JPY 159.16, FXY $57.69, Brent $98.23 (bouncing back from $91 ceasefire low).
- Researched 4 priority areas: Hormuz status, ceasefire/Lebanon, insurer plans, BOJ. Found ceasefire fracturing <48hrs in (Israel "Operation Eternal Darkness," 254 dead, Iran disputed Hormuz reopening).
- Updated TIMELINE.md with ceasefire fracturing narrative + 5Y auction (BTC 3.58 orderly) + Kaizuka hawkish signal. Cut oil de-escalation prob 25% → 15%.
- Will corrected my "hawkish chorus" framing — reminded me of vocab basics. He confirmed Hormuz tanker count remained negligible (closed in practice).
- Apr 11 closeout: Resolved STATUS.md merge conflict (kept Apr 10 upstream as base, refreshed for Apr 11). Updated CALENDAR (Islamabad talks live), TIMELINE, MEMORY, LAST_COMPLETION.
- Open question: Will asked if I have a CLOSEOUT.md checklist file. I don't — closeout is the Write-back section in CLAUDE.md (steps 9-14) + Git protocol. Suggested formalizing this. Awaiting his decision.

### NEXT SESSION
1. **Islamabad talks outcome** — did they extend the ceasefire? Did Lebanon carve-out get resolved? Talks started Apr 11.
2. **Mon Apr 14: 20Y JGB auction** — at 28-year-high yields, will demand hold? <2.0x = 🔴 to LIQUID.
3. **Mon-Fri Apr 14-18: Insurer FY2026 plans** — first announcements drop. Fukoku most likely first. Update insurers/TRACKER.md.
4. **Tue Apr 15: Feb TIC data** — Japan UST selling confirmation (>$15B = stress case).
5. **Wed Apr 22: Ceasefire expiry** — even if Islamabad extends, original 2-week clock runs out.
6. **Tue Apr 28: BOJ meeting** — hike to 1.00% (our internal call ~60-65%, market pricing ~45-50%).
7. **Vol/options check** — pre-BOJ, see if FXY OI building at $60+ strikes.
8. **CFTC release Fri Apr 11** — fresh JPY positioning data.
9. **Decide on CLOSEOUT.md formalization** — pending Will's input.
