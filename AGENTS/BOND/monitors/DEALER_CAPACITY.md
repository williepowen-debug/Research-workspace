# BOND Monitor — Dealer Capacity / Absorption

**Owner:** BOND
**Last Updated:** 2026-06-20 by BOND
**Purpose:** Track whether dealers can absorb Treasury and credit supply without creating funding or duration stress.

## Key Inputs

| Metric | Source | Cadence | Interpretation |
|---|---|---|---|
| Primary dealer net Treasury positions | NY Fed FR2004 | Weekly | Rising = absorption capacity used; falling under stress = forced de-risking |
| Treasury auction dealer take-down | Treasury auction results | Every auction | High dealer % = weak end demand / warehousing |
| eSLR / SLR rule changes | Fed/OCC/FDIC / news | Event | Capacity relief or constraint |
| Basis trade leverage | CFTC/SEC/Fed reports / market research | Monthly/event | Hidden duration/funding fragility |
| SOFR/repo pressure | LIQUID | Daily | Funding consequence, not BOND-owned |

## Current Read

**🟠 Dealer-absorption vector = 3 (elevated).** NY Fed FR2004 (5/27) shows dealer long-end inventory near/at record — **11–21Y $67.0B = all-time high** (since 2022), 7–11Y $38.0B (94th pctile), >21Y $49.7B (87th, easing). The ~$550B aggregate from the 5/5 refresh is **stale — re-pull due ~6/23.** NUANCE: the *stock* is at record but June auction *flow* was benign (10Y PD 9.5%, 20Y 8.5%, 30Y 14.7%) — accumulation is secondary-flow, not auction-forced; end-users cleared the June supply. So a thinner backstop in a selloff, but **not tested to failure.** eSLR (effective 4/1/26) eased GSIB Treasury intermediation incrementally but did NOT exclude Treasuries from the SLR denominator — no full balance-sheet relief.

## Rolling Table

| Date | Dealer UST position | Auction take-down note | Repo/SOFR context | Read | Source |
|---|---:|---|---|---|---|
| 2026-05-05 refresh | ~$550B net Treasuries | Capacity expanded post-eSLR | SOFR-IORB normalized | 🟡 capacity-used | Prior BOND STATUS / NY Fed/FT note |
| 2026-05-11 3Y | N/A | Dealer accepted 13.6% | SOFR-IORB -5bps | 🟡 watch | FiscalData + dashboard |
| 2026-05-12 10Y | N/A | Dealer 12.0% | SOFR-IORB ~0 | 🟡 | FiscalData |
| 2026-05-13 30Y | N/A | Dealer 11.7% | SOFR-IORB ~0 | 🟡 | FiscalData |
| 2026-05-27 FR2004 | **11–21Y $67.0B (record); 7–11Y $38.0B (94th pctile); >21Y $49.7B** | — (positioning snapshot) | SOFR-IORB ~0 | 🟠 record *stock* | NY Fed FR2004 (KB-BND-047) |
| 2026-06-10→16 June auctions | (pre-6/23 re-pull) | 10Y PD 9.5%, 20Y 8.5%, 30Y 14.7% — **flow benign** | SOFR-IORB -2bp (6/17) | 🟠 stock-high / flow-benign | TreasuryDirect |

## Triggers

| Trigger | Action |
|---|---|
| Dealer inventories at/near record + weak auctions | Signal LIQUID/ZHAO; watch repo funding |
| Forced inventory decline during selloff | 🔴 market-function stress |
| eSLR relief drives absorption while end-demand weak | Mark as mechanical support, not clean bill of health |
| Weak auction followed by SOFR-IORB positive | Escalate as auction stress funding through repo |
