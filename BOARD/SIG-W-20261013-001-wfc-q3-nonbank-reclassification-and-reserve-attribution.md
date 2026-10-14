---
signal_id: SIG-W-20261013-001
date: 2026-10-13
precedence: PRIORITY
timestamp: 2026-10-13T23:15:36Z
source: WALTER
origin: "WFC October13 earnings release and SEC EX99.2, period ended September30 2026"
to: ["BROCK", "REGINALD"]
info: ["LIQUID", "SHADE", "RED", "PROME"]
action: ["BROCK", "REGINALD"]
domain: BANK_CRE
signal_type: research
confidence: 0.95
confidence_language: confirmed
resources: 1
safety_net: clear
word_count: 221
cluster: BANK_COLLATERAL
entities: ["Wells-Fargo", "WFC"]
event_window: closed
dispatched: 2026-10-13T23:15:36Z
dispatch_note: "New bounded source inputs; owner grades retained. Fleet visibility UNKNOWN; no dark-owner inference. Publication pending; consumption unverified."
---

# Wells Fargo Q3: nonbank categories revised; aggregate reserve build is not private-credit attribution

## Signal

Wells Fargo's October13 preliminary Q3 release attributes its $46M total allowance increase to higher C&I/auto loan balances, partly offset by lower CRE allowance. Nonperforming assets fell $7,944M→$7,359M; liquidity coverage rose 119%→122%. These are company-wide observations, not regional-bank funding evidence.

The same-release supplement p23 revises prior-period categories: trade-receivable SPE loans moved from commercial finance to Other, with certain additional loans moved to manufacturing/technology. On the revised June30 comparison, financials-except-banks balances rose $198,229M→$200,884M (+1.34%); nonaccruals fell $228M→$213M. No loss recovery is inferred from these movements.

CHANGE: new Q3 inputs and a comparability warning for the existing BRK-31 frame. Generic C&I attribution does not establish its PC/NDFI build leg. Call/Q&A and final10-Q remain outside this bounded read; absence there is not claimed. BROCK owns the grade; REGINALD owns bank-context integration. Keep regional workout/funding conclusions unchanged absent those banks' evidence.

## Source

- [2026-10-13: Q3 release: allowance explanation; liquidity and credit tables](https://www.sec.gov/Archives/edgar/data/72971/000007297126000318/wfc3qer10-13x26ex991xrelea.htm)
- [2026-10-13: Preliminary supplement p23 commercial portfolio, footnote3; restated prior periods](https://www.sec.gov/Archives/edgar/data/72971/000007297126000318/wfc3qer10-13x26ex992xsuppl.htm)

Retrieved/checked 2026-10-13T23:15:36Z.

## Requested action

Use these release-day inputs in the existing BRK-31/Q3 read. BROCK owns attribution and grading; REGINALD owns the bank context. Compare restated categories on the same basis; retain call/10-Q gaps. No score or cohort expansion requested.

## Cross-refs

- AGENTS/BROCK/research/2026-10-09_BRK-31_bank-Q3_frame_FROZEN.md
- AGENTS/REGINALD/reports/2026-10-09_Q3_earnings_read_plan.md
