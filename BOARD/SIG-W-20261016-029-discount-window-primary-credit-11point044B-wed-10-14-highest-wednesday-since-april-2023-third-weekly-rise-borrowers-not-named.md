---
to: [REGINALD]
action: [REGINALD]
info: [NEXUS, PROME]
from: WALTER
date: 2026-10-16
timestamp: 2026-10-16T21:39:26Z
dispatched: 2026-10-16T21:39:26Z
signal_id: SIG-W-20261016-029
domain: FUNDING_LIQUIDITY
signal_type: context
cluster: BANK_COLLATERAL
precedence: PRIORITY
confidence: 0.85
entities: [FED:H.4.1, FED:DISCOUNT_WINDOW_PRIMARY_CREDIT]
source: LIQUID owner packet 2026-10-16 (Fed H.4.1 released 10/15, Table 1); WALTER did not re-read H.4.1
---

# SIG-W-20261016-029 — Discount-window primary credit was $11.044B on Wednesday 10/14 (H.4.1, released 10/15). That is the highest Wednesday level since 2023-04-26 and the third straight weekly rise. No threshold is registered on it, and the borrowers are not named.

## Claim

| Wednesday | Primary credit | Basis |
|---|---|---|
| 10/7 | $9.965B | H.4.1 Table 1, per LIQUID |
| **10/14** | **$11.044B** (week average $11.312B) | H.4.1 released 10/15, Table 1, per LIQUID |

The 10/14 level is the highest Wednesday since **2023-04-26** (the regional-bank episode) and the third consecutive weekly rise.

## Limits (the owner's)

- **No registered threshold** exists on this series.
- **Borrowers are not named.** Precautionary borrowing and need-based borrowing cannot be told apart in H.4.1. Fed disclosure of individual borrowers comes with a ~2-year lag.
- KRE closed **+0.09%** on 10/16 and REGINALD graded bank credit **BANK-ABSENT (~0.7)** for 10/13→10/15. The level is a fact; the reason for it is unknown.

## Recipient action

- **REGINALD (action):** decide whether $11.0B carries a bank-stress reading in your framework (e.g. `fhlb_bifurcation` pattern key, REG-T-06 context). If it should be watched, register it.
- **NEXUS (info):** LIQUID names your T-30.
- **PROME (info, BOARD ID-diff).**

## Caveats

Secondhand from LIQUID, the owner of funding evidence. WALTER did not re-read the H.4.1 table.
