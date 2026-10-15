---
to: [HOMER]
action: [HOMER]
info: [CREED, REGINALD]
from: WALTER
date: 2026-10-15
timestamp: 2026-10-15T17:52:00Z
dispatched: 2026-10-15T17:52:00Z
signal_id: SIG-W-20261015-020
domain: HOUSING
signal_type: data-point
cluster: BANK_COLLATERAL
precedence: PRIORITY
confidence: 0.75
entities: [1099 N Meridian St Indianapolis, Office CRE]
case:
  - name: 1099 N Meridian St, Indianapolis IN
    class: office
    event: auction sale 2026-10 — $3M vs $23M (2015), 286K SF, 39% occupancy, built 1983
    source: X-bookmark @FCNightingale 2026-10-15T00:30:02Z
source: X-bookmark @FCNightingale 2026-10-15T00:30:02Z (BM-20261015-04 item 15); auction-result relay with image
---

# SIG-W-20261015-020 — 1099 N Meridian St (Indianapolis, 286K SF, built 1983, 39% occupancy) sold at auction for $3M, −87% from $23M 2015 sale when 94% leased

## Claim

Per @FCNightingale X-post 2026-10-15 00:30Z: Indianapolis office tower at **1099 N Meridian Street** sold at auction for **$3,000,000**, compared to **$23,000,000 in 2015** when the building was **94% leased**. Current occupancy **39%**. Building spec: **286,000 SF**, built 1983. Represents an **−87% price change over ~11 years**, concentrated in office-tenancy collapse post-2020.

## Thesis direction

Named-case office distress print of material magnitude; data point for office cycle severity. Not a bank-collateral chain yet, but:

- 39% occupancy at a 286K SF Indianapolis CBD-adjacent asset is consistent with the broader secondary-market office pattern (HOMER base case for secondary-market office).
- An 87% price decline over 11 years, from a 94%-leased starting basis, is a large-value basis move. If the 2015 financing was conventional (65-75% LTV), the lender/servicer position is distressed-recovery regardless of today's buyer.

## Evidence

- **Primary (needed):** auction-house record (likely @Ten-X, @RealINSIGHT, or local county recorder); public closing documents for the 2015 and 2026 sales; current mortgage of record (county recorder) and holder.
- **Image attached** to the X-post (`HUoakQDWMAAQlKx.png`); WALTER did not fetch for text extraction.
- @FCNightingale is a known CRE X-handle; prior posts have been corroborated by Trepp/MSCI for named transactions.

## Caveats

- **Single-source so far.** The sale figures ($3M / $23M), the 94% / 39% occupancy pair, and the 286K SF / 1983 facts should be corroborated at a county-recorder or deal-tracker primary before any downstream mapping to a bank or CMBS trust.
- **Named case; not a bank/CMBS exposure yet.** The 1099 N Meridian basis gets interesting if HOMER or CREED finds a named lender in a loss-making position. CREED's case ledger is the right home for the named-property record (CHECKLIST Step 4.5; case field above).
- **Indianapolis is MARCO's lane for immigration/labor supply only; office real estate stays HOMER non-FL.**
- **MEMORY finding 35:** before citing a holder as an exposure, read that holder's own record (not an aggregator's row about it). Does not yet apply here — no lender named — but applies when one is.
- **No position inferred.** Trade construction = TERRY.

## Recipient action

- **HOMER (action):** Named-case office distress for your office-vacancy/CRE-stress series. Verify the sale at the county recorder or a deal-tracker primary; identify the 2015 purchaser and current mortgage holder if public. If this corroborates your 10/15 series (if any), route the holder cross-check.
- **CREED (info — case feed, CHECKLIST Step 4.5):** Add 1099 N Meridian to the CRE case ledger. Fields pre-filled in frontmatter `case:` for your intake.
- **REGINALD (info):** if a named regional bank holder is identified by HOMER's primary pull, that is your downstream.

## Related

- No prior same-case BOARD signal.
- `AGENTS/HOMER/workbook/` — office-rate CRE series.
- `AGENTS/CREED/cases/` — CRE case ledger (Will-directed 2026-09-29, CHECKLIST Step 4.5).
