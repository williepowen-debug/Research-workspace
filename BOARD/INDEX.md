# BOARD — Network Signal Archive

Central, network-shared archive of every signal WALTER has dispatched. This is the **single source of truth** for signal content. Located at repo root `/BOARD/` so any agent or Will can pull signals without reaching into WALTER's directory.

*Renamed and relocated from `AGENTS/WALTER/signals/` on 2026-04-14 per Will's direction — BOARD is the network-shared pull point; WALTER still owns all writes.*

## How to use this folder

**Other agents:** at boot, scan this INDEX for signals addressed to you (`to:` or `info:` column). Read the signal file(s) from `/BOARD/`. Do not rely solely on your `inbox/` — only FLASH signals are delivered there going forward; IMMEDIATE/PRIORITY/ROUTINE are archive-only in BOARD.

**WALTER:** every dispatched signal gets a canonical copy here. Filename convention: `SIG-W-YYYYMMDD-NNN-slug.md`. Append new signals to the table below at dispatch time. Never delete or rename.

## Precedence → delivery rules

**Active policy (Apr 14 2026 — BOARD + Will-alert on FLASH):**

| Precedence | BOARD archive (here) | Recipient inbox | Telegram to Will |
|-----------|:--------------------:|:---------------:|:----------------:|
| FLASH     | ✅ always            | ❌              | ✅ always        |
| IMMEDIATE | ✅ always            | ❌              | ❌               |
| PRIORITY  | ✅ always            | ❌              | ❌               |
| ROUTINE   | ✅ always            | ❌              | ❌               |

Will activated target policy 2026-04-14 23:48 UTC (dual-delivery off). Will refined 2026-04-14 23:50: on FLASH, alert Will via Telegram only — no inbox push. Rationale: other agents can't read BOARD yet, so inbox push is useless; Will will spawn the relevant agent if a FLASH requires action.

**Known gap:** other Tier 1 agents don't yet have `/BOARD/INDEX.md` in their boot sequences. They will miss BOARD signals until their CLAUDE.md files are updated. Will owns that rollout decision.

## Archive

| ID | Date | Domain | Precedence | Action → Info | Summary | File |
|----|------|--------|------------|---------------|---------|------|
| SIG-W-20260410-001 | 2026-04-10 | MACRO_INFLATION | IMMEDIATE | CARL → LIQUID | CPI 3.3% YoY hot + UMich 47.6 record low + 1Y inflation exp 4.8% = stagflation lock | [SIG-W-20260410-001-cpi-umich-stagflation.md](SIG-W-20260410-001-cpi-umich-stagflation.md) |
| SIG-W-20260411-001 | 2026-04-11 | Adversarial meta | IMMEDIATE | RED → — | RED pre-registered falsification rule pierced: HY OAS 290 <300 Day 1 of 5 sustained | [SIG-W-20260411-001-red-falsification-hy-oas-pierced.md](SIG-W-20260411-001-red-falsification-hy-oas-pierced.md) |
| SIG-W-20260411-002 | 2026-04-11 | Coordination | PRIORITY | PROME → — | FORGE/STATUS.md 17 days stale, refresh request for COP exposure section | [SIG-W-20260411-002-forge-status-stale-refresh-request.md](SIG-W-20260411-002-forge-status-stale-refresh-request.md) |
| SIG-W-20260414-001 | 2026-04-14 | CONSUMER_CREDIT | PRIORITY | CARL → RED | Sen. Lummis (R-WY) admits consumer stress ("record Meals on Wheels, I'm worried") while saying "Golden age" | [SIG-W-20260414-001-lummis-meals-on-wheels.md](SIG-W-20260414-001-lummis-meals-on-wheels.md) |
| SIG-W-20260414-002 | 2026-04-14 | PRIVATE_CREDIT | IMMEDIATE | BROCK → LIQUID, REGINALD, RED | TCW Private Credit Fund slashed Red Lobster equity 98% — loan still at par. Mark-to-model fiction confirmation | [SIG-W-20260414-002-tcw-red-lobster-98-writedown.md](SIG-W-20260414-002-tcw-red-lobster-98-writedown.md) |
| SIG-W-20260414-003 | 2026-04-14 | MARKET_VOL | PRIORITY | HENRY → LIQUID, RED | SEC approved SR-FINRA-2025-017 — PDT eliminated, intraday margin framework applies to ALL margin accounts | [SIG-W-20260414-003-sec-pdt-rule-elimination.md](SIG-W-20260414-003-sec-pdt-rule-elimination.md) |
| SIG-W-20260414-004 | 2026-04-14 | FUNDING_LIQUIDITY | IMMEDIATE | LIQUID → BRENT, HAWK, SAM, RED, BROCK | IMF GFSR Apr 2026: prepare liquidity/funding facilities; equities -8% since Feb, sovereign yields up; NBFI+PC+AI+ME drivers | [SIG-W-20260414-004-imf-gfsr-liquidity-dysfunction.md](SIG-W-20260414-004-imf-gfsr-liquidity-dysfunction.md) |
| SIG-W-20260414-005 | 2026-04-14 | BANK_CRE | PRIORITY | REGINALD → BROCK, RED | ROAD to Housing Act Senate-passed 89-10 stalled in House; Freddie K-098 deep dive (corrected to $1.2B UPB, not $1.4B); drafting errors would *decrease* FHA MF limits | [SIG-W-20260414-005-road-to-housing-act-freddie-k098.md](SIG-W-20260414-005-road-to-housing-act-freddie-k098.md) |
| SIG-W-20260414-006 | 2026-04-14 | MARKET_VOL | IMMEDIATE | HENRY → LIQUID, RED, BROCK | GS Prime: HF short cover fastest since 2020 (not 10yr) — WHIPSAW; covered on ceasefire trigger now dead post-Islamabad | [SIG-W-20260414-006-gs-prime-hf-short-cover-whipsaw.md](SIG-W-20260414-006-gs-prime-hf-short-cover-whipsaw.md) |
| SIG-W-20260414-007 | 2026-04-14 | MACRO_INFLATION | IMMEDIATE | CARL → HENRY, LIQUID, RED | Mar PPI +4.0% headline / +3.8% core — but core-core only +3.6% decelerating; half of MoM jump = gasoline +15.7% (goods/energy shock, not broad reaccel) | [SIG-W-20260414-007-march-ppi-goods-energy-shock.md](SIG-W-20260414-007-march-ppi-goods-energy-shock.md) |
| SIG-W-20260414-008 | 2026-04-14 | MARKET_VOL | PRIORITY | HENRY → REGINALD, RED | DB: Financials positioning at multi-year lows vs consensus +20-40% EPS growth — widest gap since 2020; resolves at OZK Apr 16 / WAL Apr 21 | [SIG-W-20260414-008-db-financials-positioning-gap.md](SIG-W-20260414-008-db-financials-positioning-gap.md) |
| SIG-W-20260414-009 | 2026-04-14 | OIL_ENERGY | PRIORITY | BRENT → HAWK, SAM, RED | Baker Hughes rig count flat through 1mo+ elevated oil — supply-response lag intact post-Islamabad, BOJ hike urgency rises (via SAM) | [SIG-W-20260414-009-baker-hughes-rig-count-flat-oil-elevated.md](SIG-W-20260414-009-baker-hughes-rig-count-flat-oil-elevated.md) |
| SIG-W-20260414-010 | 2026-04-14 | ASIA_CONTAGION | PRIORITY | ZHAO → RED, CARL, HENRY, LIQUID, SAM, PROME | FT "China Shock 2.0" Part 1/3 — $1T+ 2025 trade surplus; exports EU +21%/SEA +21%/US DOWN Q1'26; CNY REER -16%; OECD: CN subsidies 3-9x rich-world. Counter-evidence to stagflation lock; Trump-Xi May summit. ZHAO stale Apr 2 — awaits spawn | [SIG-W-20260414-010-ft-china-shock-2-high-end-exports.md](SIG-W-20260414-010-ft-china-shock-2-high-end-exports.md) |
| SIG-W-20260414-011 | 2026-04-14 | ASIA_CONTAGION | PRIORITY | ZHAO → BRENT, HAWK, SAM, HENRY, LIQUID, RED, PROME | FT: China export controls tripled (30 vs 11 5yr); Li-Qiang-signed "State Council Supply Chain Security" regs in force Mar 31, announced Apr 8 — Arts 13/15/16 criminalize due-diligence + authorize exit bans; Trump Beijing mid-May (postponed from April); rare earths named; historical: 2010 Japan, 2020 Australia coercion templates | [SIG-W-20260414-011-ft-china-export-controls-tripled.md](SIG-W-20260414-011-ft-china-export-controls-tripled.md) |
| SIG-W-20260414-012 | 2026-04-15 | BANK_CRE | PRIORITY | RED → REGINALD, BROCK, CARL | Seeking Alpha KRE piece (Mar 28 stale) — counter-evidence: KRE YTD -1.94% vs XLF -12.56% (KRE outperforming broad financials ~10pts); FLG 1.57% top holding w/ Fitch upgrade; $936B CRE maturing 2026 ($59.5B office); Q4 GDP 0.7% | [SIG-W-20260414-012-kre-relative-outperformance-vs-xlf-counter.md](SIG-W-20260414-012-kre-relative-outperformance-vs-xlf-counter.md) |

---

*Audit trail (one-line-per-signal TSV): `../routed/route_log.tsv`. Filtered/killed signals: `../filtered/kill_log.tsv`. Drafts in flight: `../outbox/`.*
