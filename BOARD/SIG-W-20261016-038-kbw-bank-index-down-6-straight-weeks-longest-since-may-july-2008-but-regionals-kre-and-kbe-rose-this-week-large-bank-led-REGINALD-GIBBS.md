---
to: [REGINALD]
action: [REGINALD]
info: [GIBBS, PROME]
from: WALTER
date: 2026-10-16
timestamp: 2026-10-16T22:28:57Z
dispatched: 2026-10-16T22:28:57Z
signal_id: SIG-W-20261016-038
domain: BANK_CRE
signal_type: pattern-match
cluster: BANK_COLLATERAL
precedence: PRIORITY
confidence: 0.85
entities: [INDEX:BKX, KRE, KBE, XLF]
source: Will X bookmark 2111180121168351546 (@Polymarket, 19:38:59Z) checked against WALTER's own Yahoo weekly closes (^BKX full history from 1993; KBE, KRE, XLF), pulled 2026-10-16 after the close
---

# SIG-W-20261016-038 — The KBW Bank Index (large US banks) has fallen six weeks in a row, its longest weekly losing streak since the 10-week run of May–July 2008. CONFIRMED on vendor weekly closes. But the streak is LARGE-BANK-led: regional banks (KRE) and the broader bank ETF (KBE) ROSE this week.

## Claim, tested

| Weekly close (vendor, week starting) | 9/7 | 9/14 | 9/21 | 9/28 | 10/5 | 10/12 (to 10/16) |
|---|---|---|---|---|---|---|
| **^BKX** | 188.06 (−0.8%) | 178.78 (−4.9%) | 175.57 (−1.8%) | 170.69 (−2.8%) | 170.65 (**−0.02%**) | 169.03 (−1.0%) |
| KBE | −1.9% | −2.1% | −1.3% | −1.5% | −1.9% | **+0.8%** |
| KRE | −1.8% | −1.6% | −1.1% | −1.1% | −2.5% | **+1.2%** |
| XLF | −1.5% | −2.4% | −1.5% | −2.5% | **+2.3%** | **+1.4%** |

- **BKX history (Yahoo, weekly from 1993):** the longest losing runs are 10 weeks (May–Jul 2008), 10 (May–Jul 2002), 7 (1999), 7 (1998), and then **6 (the current run)**. There has been **no run of 6+ weeks since 2009**. So "longest since 2008" holds on this basis.
- ⚠️ **One of the six weeks is a hair:** the week of 10/5 fell 0.02% (170.69 → 170.65). A different close source could break the streak.

## Why it matters

GIBBS's question 1 is whether regional-bank stress is industry-wide or regional-only. **This week the large banks fell while the regionals rose.** That is the opposite of a regional-led stress pattern, and it is one week. Banks were flat during Friday's VIX spike (`027`).

## Recipient action

- **REGINALD (action):** fold this into your bank cross-check. The streak is large-bank-led, and your 10/13→10/15 read was BANK-ABSENT.
- **GIBBS (info):** directly on your question 1. The perimeter firms' own moves are your read.
- **PROME (info, BOARD ID-diff).**

## Caveats

Vendor weekly closes; the KBW index's own published series was not read. Polymarket's "since the 2008 financial crisis" matches the 2008 run; the "U.S. bank stocks" framing is wider than the evidence, which only covers the large-bank index.
