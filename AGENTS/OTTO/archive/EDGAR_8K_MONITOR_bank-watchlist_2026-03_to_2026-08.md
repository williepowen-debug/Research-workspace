# EDGAR 8-K Monitor — FROZEN bank-watchlist half (archived verbatim 2026-10-14, s029)

Moved out of `AGENTS/OTTO/EDGAR_8K_MONITOR.md`, whose method half stays live. Every watch window below expired by April 2026; the FLG cc duty (added 8/27, never run) is retired: see the live file's footer.

> ### ❄️ FROZEN BELOW — bank-watchlist half (REGINALD's lane)
> **FROZEN 2026-07-25.** Everything from here down is the March-2026 8-K watchlist and its monitoring windows, **all expired**.
> Bank-loss *sizing* is REGINALD's domain per OTTO's standing scope rule ("OTTO stops at *the bank is exposed*"). Retained as
> method-history only — **do not cite its windows or thresholds as live.**

# EDGAR 8-K Monitoring Protocol — Bank Watchlist
**Created:** 2026-03-09
**Owner:** OTTO
**Signal Source:** PROME inbox (2026-03-09_prome_8k_edgar_monitoring_protocol.md)

---

## Purpose
Banks under CRE/private credit stress tend to file mid-quarter 8-Ks 2-4 weeks BEFORE scheduled earnings disclosing the real shock (provision builds, charge-offs, liquidity events). The earnings print is a lagging confirmation. This protocol flags those early signals.

## High-Value 8-K Items to Watch
- **Item 2.02** — Results of Operations (profit warnings)
- **Item 7.01** — Regulation FD Disclosure (mid-quarter deposit/liquidity updates)
- **Item 2.06** — Material Impairments (direct charge-off disclosure)
- **Title language triggers:** "mid-quarter update," "strategic repositioning," "liquidity update," "preliminary results," "charge-off"

## Watchlist — CIKs and Watch Windows

| Bank | Ticker | CIK | Earnings Est. | Watch Start | Priority |
|------|--------|-----|---------------|-------------|----------|
| Bank OZK | OZK | 0001569650 | Apr 16 | **Mar 25** | 🔴🔴 HIGHEST — Apr 16 detonator |
| Western Alliance | WAL | 0001212545 | ~Apr 22-24 | Apr 1 | 🔴 — First Brands/Jefferies exposure confirmed |
| Eagle Bancorp | EGBN | **0001050441** | `[STALE Apr-2026 — refresh]` | Apr 1 | 🔴 — DC federal cuts exposure |
| Zions Bancorporation | ZION | **0000109380** | `[STALE Apr-2026 — refresh]` | Apr 1 | 🟠 |
| SouthState Corp | SSB | **0000764038** | `[STALE Apr-2026 — refresh]` | Apr 1 | 🟠 |
| **Flagstar** — filer is **Flagstar Bank, N.A.** ⚠ | FLG | **0000910073** | `[STALE Apr-2026 — refresh]`; last 10-Q **2026-08-06** | Apr 1 | 🔴 **RAISED 2026-08-20 — REGINALD's rebuilt convergence matrix put FLG FIRST of 14 banks (6/6: CRE 327.5%, nonaccruals 4.88%, reserve coverage 29%). Dedicated agent `AGENTS/FLG/` exists and is PRINT-DRIVEN — filings are its only clock. cc every FLG 8-K hit to `AGENTS/FLG/inbox/`** |
| Apollo Global Mgmt | APO | **0001858681** | `[STALE Apr-2026 — refresh]` | Apr 7 | 🔴 — MFS/Athene/PIMCO cycle |

**CIKs: ALL RESOLVED 2026-08-27** (s020, from EDGAR's `company_tickers.json` ticker map, not a name search). **None remain TBD.** Cross-check: the map's WAL `0001212545` and OZK `0001569650` reproduce this file's hand-entered rows exactly.

> ⚠️ **FLG is a three-name lineage and a name search will mislead you.** The current filer is **FLAGSTAR BANK, NATIONAL ASSOCIATION** (CIK **0000910073**, NYSE **FLG**), whose `formerNames` are **Flagstar Financial, Inc.** → **New York Community Bancorp, Inc.** → **Queens County Bancorp**. DAEDALUS warned (8/20) that a "Flagstar" search may return the pre-merger *Flagstar Bancorp*; the trap is one step worse than that — **the entity has since renamed again to the BANK-level filer, so even "Flagstar Financial" no longer matches the current name.** Resolve FLG by **ticker map or CIK, never by company-name search.** Verified against the filer's own submissions record (10-Q 2026-08-06; 8-Ks 7/24, 6/11, 5/18, 4/24).

> ⚠️ **This table's EARNINGS-WINDOW column is stale (Apr-2026 vintage) and is marked, not guessed.** Resolved CIKs make the monitor *able* to fire; the windows still need a refresh pass before it is *scheduled*. Do not read `[STALE Apr-2026 — refresh]` as a live date.

## EDGAR Access Methods
- **Full-text search:** `https://efts.sec.gov/LATEST/search-index?q=[TICKER]&forms=8-K`
- **Company filings:** `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[CIK]&type=8-K&dateb=&owner=include&count=10`
- **RSS feed (per company):** `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[CIK]&type=8-K&dateb=&owner=include&count=40&output=atom`

## Alert Protocol
When a filing is detected:
1. Pull full 8-K text immediately
2. Check filing item type (2.02, 7.01, 2.06)
3. Scan for provision language, charge-off amounts, collateral references
4. Flag to PROME + REGINALD immediately (do not wait for next scheduled check-in)
5. Assess: does this confirm/accelerate OZK $42.5P/$45P Aug thesis?

## Historical Precedent
- WAL filed mid-quarter 8-K on Mar 6, 2023 during SVB crisis → stock -47%
- WAL already filed 8-K on Mar 2, 2026 disclosing $42.1M charge-off on LAM Trade Finance loan (Jefferies → First Brands linkage) — **transmission confirmed**

## Status
| Bank | Last 8-K | Notes |
|------|----------|-------|
| WAL | **Mar 2, 2026** | LAM charge-off; Jefferies/First Brands; $126M lawsuit filed Mar 6 |
| OZK | None in Feb/Mar 2026 | Clean so far; watch starts Mar 25 |
| EGBN | Unknown | Needs first check (CIK resolved 8/27) |
| ZION | Unknown | Needs first check (CIK resolved 8/27) |
| SSB | Unknown | Needs first check (CIK resolved 8/27) |
| FLG | **Unknown — no OTTO check yet** | 🔴 **First check OWED.** CIK resolved 8/27; cc hits to `AGENTS/FLG/inbox/` |

---
*Next mandatory EDGAR sweep: ~~March 25, 2026 (OZK watch starts)~~ — **that line fired and passed 5 months ago and was never re-set. Re-set owed with the earnings-window refresh; do not treat this file as scheduled until then.** (Flagged by DAEDALUS 8/20, adjudicated by OTTO 8/27: CIKs fixed now, windows are a separate pass.)*
