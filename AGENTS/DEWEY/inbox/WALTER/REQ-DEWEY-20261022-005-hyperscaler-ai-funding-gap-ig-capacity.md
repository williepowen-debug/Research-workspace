---
request_id: REQ-DEWEY-20261022-005
from: WALTER (Will-approved in the WALTER terminal, 2026-10-22 ~12:30 ET, option A of WALTER's shortlist)
to: DEWEY
created: 2026-10-22 (UTC stamp in the commit)
state: NEW
flag_trigger: T2 cross-channel (AI capex to investment-grade credit supply to rates) + T4 thesis pivot (VULCAN capex-cut gate; LIQUID credit read)
originating_evidence: SIG-W-20261021-015 (Meta Q3 8-K: capex $34.91B, 2026 guide $135-145B, free cash flow -$2.12B, $9.89B legal charge) + SIG-W-20261022-006 (Meta 5-year CDS at a record on two vendors; Lam supply constraints; Tesla capex cut) + SIG-W-20261020-010 / -023 (data-center bond and project-finance leads)
clusters: AI_INFRA_CAPEX (secondary POSITIONING_VALUATION)
ledger_ref: AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv row REQ-DEWEY-20261022-005
kill_condition: At intake, grep AGENTS/VULCAN and AGENTS/LIQUID for an existing per-company capex-versus-operating-cash-flow table dated after 2026-09-30. If one exists, extend it rather than rebuild it, and say so. Do not wait for MSFT/GOOGL/AMZN Q3 prints; use what is filed and mark later prints as pending.
deliver_by: useful before or soon after the remaining hyperscaler Q3 prints (late October)
---

# DEEP-RESEARCH REQUEST — Can the hyperscalers fund their AI capex without leaning on the bond market?

**Why now:** Meta's Q3 free cash flow turned negative (-$2.12B) while it raised its capex floor, and its credit default swaps hit a record on 10/22. VULCAN tracks capex guidance; nobody in the fleet has added up the external funding gap across the big spenders or asked whether the investment-grade market can absorb it with the 10-year near 5%.

**Decision question:** for Microsoft, Alphabet, Amazon, Meta and Oracle, how far do 2026 and 2027 capex (including finance leases) exceed operating cash flow after dividends and buybacks? How is the gap being filled (bonds, commercial paper, finance and operating leases, off-balance-sheet project vehicles such as joint-venture data-center financings, private credit), and what share of expected investment-grade issuance would it take?

**What changes with the answer:** VULCAN learns whether a capex cut is being forced by funding rather than chosen; LIQUID learns whether AI borrowing is a driver of the current credit widening or a separate track. If the gap is small and cash-funded, the Meta CDS move is idiosyncratic.

## Scope (in bounds)

1. **Per-company table, filings first.** Latest 10-Q/10-K and Q3 8-Ks: operating cash flow, capex incl. finance-lease principal, dividends, buybacks, cash and investments, debt maturities through 2027. Company guidance for 2026–27 capex with dates.
2. **Off-balance-sheet and lease financing.** Disclosed lease commitments not yet commenced, and named project financings (e.g. joint ventures with private-credit or infrastructure funds). Give amounts, counterparties and dates; mark reported-not-filed items.
3. **Issuance record.** 2025–26 bond deals by these five (size, tenor, spread at pricing, order book if reported) and how their spreads have moved since.
4. **Market capacity.** Total US investment-grade issuance forecasts for 2026–27 and the tech share; whether dealers, insurers and foreign buyers have shown strain (new-issue concessions, order-book coverage).
5. **CDS context.** Meta and Oracle CDS levels and history; who trades them (hedging of loans and project exposure) so a record is not over-read.
6. **Counter-evidence, required.** Cash piles, ability to slow buybacks, and analysis arguing the gap is manageable.

## Out of bounds

Stock or bond trade ideas (TERRY); grading VULCAN's thesis.

## Deliverable

Tables over prose, every cell sourced and dated: (1) per-company funding-gap table; (2) off-balance-sheet and lease table; (3) issuance and spread table; (4) market-capacity view; (5) counter-evidence; (6) explicit UNKNOWNs.

**On return:** archive to AGENTS/DEWEY/output/, then hand back via a create-only handoff in AGENTS/WALTER/inbox/DEWEY/ naming REQ-DEWEY-20261022-005. WALTER routes it as a research-output signal: VULCAN action; LIQUID, HENRY, BOND, RED and PROME info.
