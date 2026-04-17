# HENRY MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis, STATUS, or LESSONS and delete, never just accumulate.*

*Audience: next HENRY instance. For Will-facing session closeout see `LAST_COMPLETION.md`.*

---

## Feedback
*Will's guidance on how HENRY should work. Add when corrected or when an approach is validated.*

- [2026-04-17] Always pull fresh EOD levels before closing the week, even when intraday STATUS looks stable — partial retracements during the session are the tell (Apr 17 Brent closed $2.50 off intraday lows, KRE gave back half the AM Hormuz-beta bid).
- [2026-04-17] When a file-system cleanup proposal touches a system-wide convention (LAST_COMPLETION.md is used by VIOLET/REGINALD/BRENT), present options and recommendation, don't just execute. Will picked "keep both, crisp the roles" (Option A) once the tradeoff was explicit.

## Findings
*Non-obvious observations that persist across sessions but don't belong in STATUS, thesis, or LESSONS.*

- [2026-04-17] When oil shocks reverse on unilateral headlines, regional-bank beta (KRE, APO) gives back most of the AM rally by close — the "conviction" bid is small vs the beta bid. Use EOD KRE/APO print as the tell on whether the headline stuck.
- [2026-04-17] SAM's closeout structure (CHANGES SINCE / LAST SESSION / NEXT SESSION in MEMORY.md) is the leanest working pattern in the codebase. Complements — does not replace — LAST_COMPLETION.md.

## References
*Where to find things that aren't in the boot path.*

- [2026-04-17] Live market refresh: `source .venv/bin/activate && python3 FORGE/tools/market-data/fetch.py price ^GSPC ^VIX ^SKEW ^VIX3M KRE JPY=X ^TNX TLT APO HYG LQD BZ=F CL=F`. `SPX`/`VIX` alone fail (delisted in yfinance) — use `^GSPC`/`^VIX`.
- [2026-04-17] HY OAS daily refresh: FRED series `BAMLH0A0HYM2`, 1-day lag (Fri close prints Mon AM).
- [2026-04-17] `workbook/MARKET_DATA.tsv` is the sparse EOD snapshot log — append a row on EOD refresh days. Not exhaustive; use for time-series cross-reference.

---

## Session Notes

### CHANGES SINCE LAST SESSION
*Populated at boot during market refresh — what moved offline.*

- (Apr 17 Session 4 EOD — continuous from Session 3 PM, same day. No offline gap.)

### LAST SESSION (2026-04-17 Fri EOD — Session 4)
- **EOD market refresh.** Pulled live close via FORGE fetcher. SPX 7,123.77 (+1.17%), VIX 17.76 (did NOT break 17), SKEW 140.74, Brent $90.67 (partial retrace from -11% AM → -8.77% close, +$2.51 off intraday lows), KRE $70.38 (gave back $0.55 from AM bid), APO $124.28 (faded $2.20). Three EOD tells documented in STATUS BOTTOM LINE: VIX refused <17, oil partial retrace = skepticism on unilateral Iranian reopen, KRE/APO gave back most AM beta bid.
- **Invalidation criteria NOT triggered.** Requires VIX <15 + HY OAS <260 + SPX >7,100 for 5 sessions — only SPX piece qualifies.
- **Infrastructure: MEMORY.md adopted.** New file, SAM template. CLAUDE.md SPAWN PROTOCOL restructured into Boot/Execute/Write-back/Git phases. FILES table updated.
- **File-structure cleanup.** `research/deep_dives/` created — GEX_CTA_DEEP_DIVE_MAR3 + INFORMED_OPTIONS_TRADING_RESEARCH_THREAD moved off research/ root (mirrors credit/ topic-subdir pattern). research/README.md index updated. `workbook/MARKET_DATA.tsv` added to FILES table; Apr 17 row updated intraday→EOD. LAST_COMPLETION.md vs MEMORY.md role split documented in CLAUDE.md.
- **3 commits pushed:** `351c3a08` (EOD refresh), `55cd72fe` (MEMORY.md adoption), `cb2d53ab` (file-structure cleanup).

### NEXT SESSION (Monday Apr 20, 2026)
1. **🟢 HY OAS Apr 17 settle print** (FRED AM). <280 = compression continuing → thesis amber watch tightens toward invalidation. >290 = reversal, complacency break incipient.
2. **🟡 Weekend Brent gap.** Any fresh US-Iran escalation/de-escalation headlines repricing WTI/Brent Monday open. Hormuz "completely open" was unilateral — watch for US counterparty response.
3. **🟠 Tanker-tracking signal (HAWK/BRENT).** Are tankers actually reaching Iranian ports or still blocked? Per LESSONS "unilateral ≠ bilateral" rule.
4. **🔴 Tue Apr 21 AMC — OZK + WAL Q1 (binary vol event).** Positioning asymmetry: HF short-cover whipsaw (GS Prime) + financials positioning multi-year lows (DB -1.5 to -2z). Both tails fattened. Review TRADE.md if spawned for trade task.
5. **🟠 Tue Apr 21 — Retail Sales Mar (rescheduled).** First consumer print post-CPI 3.3%.
6. **Week ahead:** Apr 23-24 BOJ, Apr 28-29 FOMC, Apr 30 PCE+GDP Q1.

### GAPS — PERSISTENT (not session-specific)
- **0DTE SPX share + GEX regime** STATUS.md PENDING — SpotGamma/Barchart wire-up deferred 3+ sessions. Decision needed: wire up, remove fields, or accept PENDING.
- **VX.tsv 11 STALE Jan/Feb rows** (Put/Call, insider, NAAIM, BTC, tech breadth, GEX, IV%, COT, A-D line, MOVE/VIX). Refresh or archive.
- **1 undelivered outbox signal** to VIOLET (skew-bounce-status-lag, Apr 17 AM). HERMES hasn't swept — messaging-system issue, not HENRY's to fix.

### RESEARCH QUEUE (proposed Apr 17 Session 4 — pick up next session)

**Session-1 picks (Will prioritized):**
1. **Apr 21–30 catalyst scenario matrix.** 6+ events (OZK+WAL, Retail Sales, BOJ, FOMC, PCE+GDP) over 10 days. Joint scenario trees: all hawkish / all dovish / mixed. Expected cascade trigger probability per path. **Do before Monday if possible.**
2. **Historical cascade fired-vs-aborted cases.** Operationalizes Apr 17 "data-right, positioning-early" lesson. Aug 2024 VIX spike, Dec 2024 CTA flip reversal, Nov 2023 regional-bank scare — what distinguished follow-through vs abort? Output: "data confirms / market ignores" row template for scenario grids.

**Structural backlog (durable investments):**
3. **GEX wire-up decision doc.** 3+ sessions deferred. Research SpotGamma alternatives (Barchart, CBOE OI, VolLand, OptionsPro) + home-brewed GEX from free OI + Black-Scholes. Decide: wire up, accept PENDING, or remove fields.
4. **Structural bid decomposition.** Quantify $/day mechanical bid: buybacks, passive creations, 401k biweekly, CTA/vol-control contribution. Cascade math needs a headwind denominator — explains why data has been right but positioning bled.
5. **Regional bank credit-vs-margin playbook.** KRE components weighted by CRE office / C&I / subprime auto exposure. NIM math per yield curve shape. Sharpens OZK/WAL read and the "Hormuz beta vs credit conviction" distinction.

**Nice-to-have:**
6. **Macro-surprise-index as leading indicator.** Econ Surprise 0.338 (Apr 2, longest above-zero stretch since 2023). Historical pattern of surprise-peaks preceding stagflation breaks.
7. **Credit-vol decoupling phase tracker.** Complements VIOLET LOW_VOL regime framework. When does decoupling end + reconvergence begin? HENRY owns the reconvergence signal.

### INFRASTRUCTURE CHANGES (persistent)
- MEMORY.md created (Session 4). Template: Feedback / Findings / References / Session Notes. Cap 100 lines.
- CLAUDE.md SPAWN PROTOCOL: Boot (1-3 reads) / Execute (4) / Write-back (5-9) / Git. Step 3 reads MEMORY.md. Step 8 writes MEMORY.md. Step 9 writes LAST_COMPLETION.md.
- `research/deep_dives/` subdir — matches `credit/` topic pattern.
- Role split: LAST_COMPLETION = Will closeout (session-overwritten); MEMORY = HENRY notebook (cumulative). No overlap.
