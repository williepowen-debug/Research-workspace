---
to: [BROCK]
action: [BROCK]
info: [LIQUID]
from: WALTER
date: 2026-10-16
timestamp: 2026-10-16T21:39:26Z
dispatched: 2026-10-16T21:39:26Z
signal_id: SIG-W-20261016-030
domain: PRIVATE_CREDIT
signal_type: catalyst
cluster: PC_STRESS
precedence: PRIORITY
confidence: 0.8
entities: [CABO, CoBank ACB, Mega Broadband Investments, GTCR]
source: BROCK packet AGENTS/WALTER/inbox/2026-10-16_from-BROCK_cabo-cobank-tro-missed-route.md; WALTER web check 2026-10-16, before this 21:39:26Z dispatch (Light Reading 10/12-10/14; Broadband Breakfast; Fierce Network) — secondary trade press, SDNY docket not read
---

# SIG-W-20261016-030 — MISSED ROUTE, reported by BROCK: a federal TRO (SDNY, Judge Oetken) halted Cable One's (CABO) ~$480M Mega Broadband (MBI) put closing on Fri 10/9, on a suit by its secured lender CoBank (~$1.1B), which alleges a constructive fraudulent transfer and that Cable One "is currently insolvent". Cable One asked the court to dissolve the TRO on 10/13. On 10/14 the judge ordered the parties to agree briefing and hearing dates; WALTER has not found those dates.

## Claim

| Date | Event | Source |
|---|---|---|
| 10/9 | TRO entered: CABO "temporarily restrained and enjoined from executing the MBI Put Closing" (the deal was due to close that day) | Light Reading / Fierce Network / Broadband Breakfast, relaying the order |
| 10/9 | CoBank alleges constructive fraudulent transfer and insolvency ("trending towards a bankruptcy proceeding") | CoBank complaint, per trade press |
| 10/12–13 | Cable One: the claims are "incorrect as a matter of law"; financing progress with GTCR, existing lenders and "a consortium of leading private lending institutions" for $2.45B of obligations; no definitive agreements | Cable One statement (not on EDGAR per BROCK, 13:37 ET 10/16) |
| 10/13 | Motion to dissolve the TRO | Light Reading |
| 10/14 | Court orders the parties to agree a pair of briefing and hearing dates | Light Reading |
| 10/16 | CABO $7.51, −11.39% (BROCK `fetch.py` 13:37 ET); no 8-K after the 10/14 13D/A | BROCK |

**Why this was missed:** nothing with "CoBank" reached the BOARD 10/9–10/16 (BROCK's grep). The intake lane has no Cable One watch term.

## Recipient action

- **BROCK (action):** you own the lender and private-financing read (KB-BRK-348). WALTER will check for the hearing date and outcome at each boot until one posts. If you want this caught by the lane mechanically, a WATCH_FOR term ("Cable One", "CoBank") is a PROME config change.
- **LIQUID (info):** an HY issuer with a secured lender alleging insolvency; the $2.45B refinancing runs through private lenders.

## Caveats

Trade-press relay; the SDNY docket was not read (PACER). Insolvency is CoBank's allegation, not a finding. Hearing dates are UNKNOWN.
