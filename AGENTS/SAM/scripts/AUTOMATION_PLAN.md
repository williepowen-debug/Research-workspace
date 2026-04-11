# SAM Automation Plan

**Created:** 2026-04-11 | **Status:** DRAFT — awaiting Will approval | **Model:** Adapted from REGINALD/scripts/AUTOMATION_PLAN.md

---

## Context

REGINALD built 8 monitoring scripts + orchestrator in `AGENTS/REGINALD/scripts/`. Will asked SAM to evaluate porting the pattern to Japan macro. This plan is the result of that evaluation.

**Important:** SAM's data sources are almost entirely different from REGINALD's (Japan macro vs US regional banks). Most REGINALD scripts don't port; several SAM-specific scripts need to be net-new. The value is in the **pattern** (standalone + testable + orchestrator), not the content.

---

## Brainstorm — SAM's Actual Manual Pain Points

Every session I currently do these by hand. Reviewing what's automatable:

| # | Task | Current method | Automatable? | Frequency |
|---|------|---------------|--------------|-----------|
| 1 | FX/oil price refresh | FORGE `fetch.py` | ✅ Already tooled | Every session |
| 2 | JGB yields (10Y/20Y/30Y/40Y) | Web search | ✅ But source is fragile | Every session |
| 3 | Threshold breach check | Mental diff vs STATUS.md table | ✅ Trivial | Every session |
| 4 | Catalyst lookahead | Eyeball CALENDAR.md | ✅ Trivial | Every session |
| 5 | FXY options OI snapshot | yfinance one-liner from CLAUDE.md | ✅ Already half-written inline | Weekly |
| 6 | CFTC JPY positioning | Web search Fridays | ✅ CFTC publishes CSV | Weekly (Fri) |
| 7 | MOF weekly foreign bond flows | Scrape tradingeconomics | ✅ Weekly scrape | Weekly |
| 8 | JGB auction results | MOF website URL pattern | ✅ URL known, parseable | 1-2x/week |
| 9 | Insurer news (press releases) | Ad-hoc web search | 🟡 Fragile, still needs judgment | Ad-hoc |
| 10 | BOJ OIS pricing | Web search | ❌ No good free source | Pre-meeting |
| 11 | Thesis impact / narrative synthesis | LLM work | ❌ Needs judgment | Every session |

**Items 1-8 are deterministic data pulls → automate.**
**Items 9-11 need judgment → leave manual.**

The biggest single friction is item 2 (JGB yields) — yfinance has no good JGB tickers, so I spend time each session web-searching for yields I already know the structure of. A working JGB scraper would be a permanent win.

---

## What Ports from REGINALD, What Doesn't

| REGINALD script | SAM port? | Reasoning |
|-----------------|-----------|-----------|
| `thresholds.py` | ✅ YES | Full port, SAM threshold set |
| `options_oi.py` | ✅ YES | FXY-focused, tracks thesis strike zone $58-65 |
| `earnings_countdown.py` | ✅ YES (rename) | → `catalyst_countdown.py`. BOJ/auctions/TIC/CPI |
| `boot.py` | ✅ YES | Direct pattern port |
| `darkpool.py` | ❌ NO | US equity structure (off-exchange %, FINRA short vol) — n/a for FX/rates |
| `insider.py` | ❌ NO | SEC EDGAR Form 4 — Japan has no public equivalent |
| `8k_monitor.py` | ❌ NO | SEC 8-K — Japan corporate filings not scrapable same way |
| `si_refresh.py` | ❌ NO | yfinance SI unreliable for ETFs (REGINALD's own note flags this for KRE — same problem for FXY) |
| `kre_float.py` | 🟡 MAYBE | Could track FXY AUM via same yfinance pattern. Modest value. Deferred. |

**Net takeaway:** 4 of 8 REGINALD scripts port. 4 need SAM-specific replacements targeting Japan data sources.

---

## Net-New SAM Builds (Japan-Specific)

These have no REGINALD equivalent and cover SAM's actual data needs:

| Script | Data source | Output | Complexity |
|--------|-------------|--------|-----------|
| `jgb_yields.py` | MOF interest rate page (primary) → FRED (10Y fallback) → investing.com (last resort) | `JGB_YIELDS.tsv` daily append, 10Y/20Y/30Y/40Y | Medium |
| `jgb_auctions.py` | MOF auction results URL pattern: `mof.go.jp/english/policy/jgbs/auction/calendar/eresul/eresul{YYYYMMDD}.htm` | `JGB_AUCTIONS.tsv` — BTC, tail, accepted yield. Alert BTC <2.0x | Medium |
| `cftc_jpy.py` | CFTC COT public CSV from cftc.gov (Fridays 3:30 ET, reflects Tuesday data) | `CFTC_JPY.tsv` — JPY non-commercial net, vs Jul 2024 peak (-180K). Alert if shorts closing >10% WoW | Easy |
| `mof_flows.py` | tradingeconomics.com/japan/foreign-bond-investment (MEMORY ref) | `MOF_FLOWS.tsv` — 4-week rolling. Alert if net selling >¥1T/mo → signal LIQUID | Medium |

---

## Design Principles (Inherited from REGINALD)

- Each script **standalone + testable** (run individually before integrating)
- **Fail gracefully** — network errors = skip section, never crash the boot sequence
- **Idempotent TSV append** — check for existing (date, ticker) key before writing
- Use workspace `.venv/bin/python3`
- Scripts live in `AGENTS/SAM/scripts/`
- TSV outputs in `AGENTS/SAM/workbook/`
- State files (`.json`, dot-prefixed) in `scripts/` dir
- Match REGINALD naming where applicable (`boot.py`, `thresholds.py`) so the pattern is recognizable

**SAM-specific addition:** Every alert/signal script should have an optional `--signal` flag that writes an outbox file to `AGENTS/SAM/outbox/` when a threshold fires, so HERMES can route it automatically. Phase 3 nice-to-have.

---

## Build Phases

### Phase 1 — Core MVP (~45 min)

Highest ratio of value to effort. Direct REGINALD ports to SAM thresholds/data.

| # | Script | Purpose |
|---|--------|---------|
| 1 | `thresholds.py` | USDJPY 160/155/147/145/130, JGB 10Y 2.40%, JGB 30Y 4.0%, Brent $120/$90, FXY $55.05 stop + $60-62 target. Prints breaches + 5% near-misses. Reads prices from FORGE cache or calls `fetch.py`. |
| 2 | `catalyst_countdown.py` | Reads from `workbook/CATALYSTS.tsv` (new — migrated from CALENDAR.md). Auto-flags anything within 5 trading days. BOJ/auctions/TIC/CPI/ceasefire. |
| 3 | `fxy_options.py` | FXY chain next 4 expiries. Put/call OI aggregates, top 5 strikes each side. Flags OI building at $58-65 thesis zone. Appends `workbook/FXY_OPTIONS.tsv`. |

**Test each individually, commit each after verification.**

### Phase 2 — SAM-Specific Data Sources (~90 min)

Net-new builds targeting Japan macro data. These replace manual web searches.

| # | Script | Purpose |
|---|--------|---------|
| 4 | `jgb_yields.py` | Multi-source fallback hierarchy. Primary MOF page, fallback FRED (10Y), last resort investing.com. Daily append `workbook/JGB_YIELDS.tsv`. |
| 5 | `jgb_auctions.py` | MOF URL fetch + parse BTC ratio, tail, accepted yields. Triggered on CALENDAR auction dates. Alert BTC <2.0x → 🔴 LIQUID/HENRY. Appends `workbook/JGB_AUCTIONS.tsv`. |
| 6 | `cftc_jpy.py` | Download CFTC COT CSV. Extract JPY non-commercial net. Compute: current, WoW change, % of Jul 2024 peak. Append `workbook/CFTC_JPY.tsv`. |
| 7 | `mof_flows.py` | Scrape tradingeconomics Japan foreign bond investment. 4-week rolling. Alert >¥1T/mo net selling → 🟠 LIQUID. Append `workbook/MOF_FLOWS.tsv`. |

**Test each individually, commit after each.**

### Phase 3 — Orchestration (~30 min)

| # | Artifact | Purpose |
|---|----------|---------|
| 8 | `boot.py` | Master orchestrator. Runs all scripts in sequence. Smart scheduling: FXY options (weekly), CFTC (Fridays only), JGB auctions (only if CALENDAR shows auction today). Prints consolidated boot brief. |
| 9 | `CLAUDE.md` step 7 update | Replace multi-step manual instructions with: `.venv/bin/python3 AGENTS/SAM/scripts/boot.py`. Keep manual fallback below. |
| 10 | Retire `tools/usdjpy_monitor.sh` | Move to `archive/`. Functionality absorbed into `thresholds.py`. The current bash script has a stale "moltbot" path anyway. |

### Phase 4 — Deferred (explicitly NOT in initial build)

- `insurer_tracker.py` — Big 4 IR page monitor. Fragile. Revisit after FY2026 plan window closes (Apr 25).
- `fxy_float.py` — FXY shares outstanding. Modest value. Build only if AUM shrinkage becomes a thesis input.
- `boj_watcher.py` — OIS hike pricing. No good free source. Skip until paid data available.

---

## File Layout

```
AGENTS/SAM/
├── scripts/
│   ├── AUTOMATION_PLAN.md        ← this file
│   ├── thresholds.py             ← Phase 1
│   ├── catalyst_countdown.py     ← Phase 1
│   ├── fxy_options.py            ← Phase 1
│   ├── jgb_yields.py             ← Phase 2
│   ├── jgb_auctions.py           ← Phase 2
│   ├── cftc_jpy.py               ← Phase 2
│   ├── mof_flows.py              ← Phase 2
│   ├── boot.py                   ← Phase 3
│   └── .state/                   ← alert state json files
└── workbook/
    ├── CATALYSTS.tsv             ← Phase 1 (migrated from CALENDAR.md)
    ├── FXY_OPTIONS.tsv           ← Phase 1 (new)
    ├── JGB_YIELDS.tsv            ← Phase 2 (new)
    ├── JGB_AUCTIONS.tsv          ← Phase 2 (new)
    ├── CFTC_JPY.tsv              ← Phase 2 (new)
    └── MOF_FLOWS.tsv             ← Phase 2 (new)
```

---

## Time Estimates

| Phase | Scripts | Build | Test | Total |
|-------|---------|-------|------|-------|
| Phase 1 | 3 ports | 30 min | 15 min | **~45 min** |
| Phase 2 | 4 new builds | 60 min | 30 min | **~90 min** |
| Phase 3 | orchestrator + docs | 20 min | 10 min | **~30 min** |
| **Total** | **8 scripts** | | | **~165 min** |

Caveat: Phase 2 time estimate assumes data sources work as expected. If MOF pages have changed structure or tradingeconomics blocks scrapers, add 20-30 min per failed source.

---

## Decision Points for Will

1. **Scope:** Full Phase 1+2+3 (~3 hrs), or minimum viable Phase 1 only (~45 min)?
2. **CATALYSTS.tsv migration:** CALENDAR.md is currently markdown. Migrate dates to TSV now (cleaner for scripts), or parse markdown directly (messier but no migration work)? Recommendation: TSV.
3. **CLAUDE.md boot update:** Auto-update step 7 to reference `boot.py`, or keep manual and add `boot.py` as optional path? Recommendation: update, keep manual as fallback.
4. **Retire `tools/usdjpy_monitor.sh`:** Move to archive? The bash script has a wrong "moltbot" path — likely stale from a VPS migration. Recommendation: archive.
5. **Commit cadence:** One per script (8 commits), one per phase (3 commits), or one big commit? Recommendation: one per phase — clean history, easy to revert a phase.
6. **Signal outbox integration:** Should `thresholds.py` / `jgb_auctions.py` auto-write to `AGENTS/SAM/outbox/` when a 🔴 threshold fires, or just print? Recommendation: print-only in MVP, add `--signal` flag in Phase 3 after core is proven.

---

## Open Questions / Risks

- **JGB yield sourcing** — MOF's interest rate page is the authoritative source but HTML scraping is fragile. FRED has 10Y only (`IRLTLT01JPM156N`, monthly). investing.com scraping violates ToS. May need to live with a fallback chain + manual verification.
- **CFTC COT URL** — Need to confirm exact CSV endpoint. Report releases Fridays ~3:30pm ET, data through prior Tuesday. Lag = 3 days.
- **tradingeconomics anti-scraping** — May require browser-like headers, may rate-limit. Watch for 403s.
- **MOF auction URL stability** — Pattern works for 2026 so far. No guarantee it survives a site redesign.
- **State files + git** — Alert state files (`.state/*.json`) change every run. Should be `.gitignore`d inside scripts/. Need to add.

---

*Ready to build on Will's go-ahead. This file stays here as the reference artifact — will get updated as phases complete.*
