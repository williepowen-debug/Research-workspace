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
| Eagle Bancorp | EGBN | TBD | ~Apr 22-28 | Apr 1 | 🔴 — DC federal cuts exposure |
| Zions Bancorporation | ZION | TBD | ~Apr 22-24 | Apr 1 | 🟠 |
| SouthState Corp | SSB | TBD | ~Apr 22-24 | Apr 1 | 🟠 |
| Flagstar Financial | FLG | TBD | ~Apr 22-28 | Apr 1 | 🟠 |
| Apollo Global Mgmt | APO | TBD | ~May | Apr 7 | 🔴 — MFS/Athene/PIMCO cycle |

**Remaining CIKs to resolve:** EGBN, ZION, SSB, FLG, APO — pull from EDGAR company search when needed.

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
| EGBN | Unknown | Needs first check |
| ZION | Unknown | Needs first check |
| SSB | Unknown | Needs first check |
| FLG | Unknown | Needs first check |

---
*Next mandatory EDGAR sweep: March 25, 2026 (OZK watch starts)*
