# USO research tracker

Setup / review date: October 20, 2026. SCOPED-PARTIAL: historical FINRA and issuer receipts imported; dated vendor lending/short-volume observations transcribed from the pages examined in this session. No new live price, option-chain or technical-chart study. Numerical observations live in [observations.tsv](observations.tsv).

The complete initial investigation and its source receipts are now stored under [research-2026-10-20-short-interest](research-2026-10-20-short-interest/REPORT.md). The subsequent discussion is consolidated in [FINDINGS.md](FINDINGS.md). Relocation does not refresh any source observation.

## Facts and assessment

| Question | Evidence | Assessment / confidence limit |
|---|---|---|
| What is the current short count? | Latest verified public settlement observation in the series is September 30. October 15 publication is scheduled October 26 per the initial report's verified FINRA calendar. | UNKNOWN for October 20. It may have risen or fallen. The next report will also predate today's selloff. |
| What historical pattern exists? | Primary rows show an early-September increase followed by a later net reduction; latest count remains above August 31 and below May 29. | Historical net balance pattern only. Neither all-covered nor newly-minted describes the remaining positions on this evidence. |
| Is borrow tightening continuously today? | One broker proxy's inventory replenished after the open, then fell; its fee was unchanged across those recorded post-open snapshots. | No continuously worsening shortage visible in that interval at this broker. Inventory changes cannot distinguish loan returns, new supply, transfers or borrowing. No market-wide conclusion. |
| Was yesterday's short-sale share exceptional? | Vendor-reported October 19 covered-volume percentage was below its stated 30-day mean. | This single comparison does not show an elevated share of short-marked trades yesterday. Underlying daily FINRA downloads attempted in session returned HTTP403; vendor methodology/mean not independently reproduced. No conclusion about today's flow or net positions. |
| Is USO itself becoming scarce? | Initial issuer receipt provides one dated outstanding-share, redemption and NAV-discount observation; creation/redemption mechanics documented in initial report. | Need a history and current creation-status verification. No current shortage or unrestricted-creation certification. |
| Is a squeeze or coordinated headline trade established? | No authenticated current consolidated loan/short balance, trader identity or motive. | Unproved. Borrow fee/availability and price moves cannot establish motive or imminent forced covering. |

## Missing evidence and next useful work

1. October 26 or later, when available: retrieve the October 15 FINRA row and compare the same series. This is a research dependency, not a promised scheduled run; it cannot answer October 20 positioning.
2. Obtain an authenticated daily USO securities-lending history: loans outstanding, new loans/returns, lendable supply, utilization and fees, with provider coverage. No subscription/account access has been assumed or purchased.
3. Build issuer share-count/creation-redemption and premium/discount history. Authenticate a September 30 denominator before computing its short percentage. Current creation restrictions remain to be checked.
4. Reproduce vendor short-volume observations from primary files when access works, preserving venue scope and its 30-day averaging definition. Do not derive net short balances by summing transactions.
5. During a USO technical review, compare timestamp-aligned USO returns to its actual futures basket and NAV across rolls. Examine relative volume, trend and volatility with a declared lookback; no new trigger levels established here.
6. Examine an authenticated options chain and next-day open-interest changes before drawing positioning inferences. Separate option structure from an outstanding share-short count.

## Conditional inferences to investigate

- Falling loan balances with elevated loan returns across consistent provider coverage would support an unwind/covering interpretation; it would still not identify all traders or motives.
- Rising loan balances alongside tighter supply and rising fees would support increased borrowing pressure. Utilization alone can rise when supply is withdrawn.
- A persistent USO premium to matched-time fair value, together with verified creation constraints and lending stress, would strengthen a share-scarcity interpretation. An oil rally alone would not.

These are analytical interpretations, not registered alerts, entry criteria or trade recommendations. Current holding rules/approvals remain at [TRADE.md](../TRADE.md). Earlier oil thesis and physical-flow evidence retain their original dates.

## Session source receipts

Primary numerical imports: the four `finra-*-USO.json` files and `issuer-dailyprice.json` under [initial research](research-2026-10-20-short-interest/REPORT.md). Vendor additions were read at [borrow history](https://chartexchange.com/symbol/nyse-uso/borrow-fee/) and [short volume](https://chartexchange.com/symbol/nyse-uso/short-volume/); transcribed rows are preserved in this folder's observations file, not claimed as raw primary files. Conflicting stale search snippets were excluded. October 19 short-volume primary retrieval was blocked; the vendor comparison remains provisional. No paid lending feed or current technical/options dataset was required to create the folder.
