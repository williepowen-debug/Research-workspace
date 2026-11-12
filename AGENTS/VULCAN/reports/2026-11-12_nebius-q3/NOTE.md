# Nebius Q3 2026 — read at the issuer primary (catalyst row 2026-11-12)

**Read:** 2026-11-12 08:53–08:58 ET by VULCAN (session launched by PROME prome-e8, WQ-184 C6 wake). KB-VULCAN-424.

**Sources (primary, issuer):** Nebius newsroom "Nebius reports third quarter 2026 financial results" (2026-11-12) and its two PDFs:
- Financial results press release — sha256 `b046024af42ebc2877fc34c044b938ac2beea256268236670d29726209d4d408` (8,106,921 B); layout extract `sources/nebius_q3_2026_release_layout.txt`
- CEO letter to shareholders Q3 2026 — sha256 `af27fdee7bcc060f8654b09a6f2074f76d7c3d135c046a271896f232dfd86908` (15,780,370 B); layout extract `sources/nebius_q3_2026_shareholder_letter_layout.txt`
- PDFs not committed (size); URLs on the newsroom page under `assets.nebius.com`.

**Not read:** EDGAR had no Q3 6-K from Nebius at 08:52 and 08:56 ET (submissions API, CIK 1513845; last 6-K 2026-10-22). The 8:00 AM ET call was not heard and no transcript was available.

## What the catalyst row asked

| Question (CATALYSTS 2026-11-12) | Answer | Where |
|---|---|---|
| Microsoft contract status | **In place.** New Jersey will deliver more than half the Microsoft-contracted capacity by year-end; remaining tranches now **2Q27**. "Microsoft has been part of the planning process." | Letter, Capacity |
| Non-renewal or oversight language | **None found** (grepped both documents for oversight, non-renew, terminat, cancel) | — |
| Capacity delays | **Yes.** "Where we rely on third parties, there have been delays." Several colocation sites shifted into 1H27; NJ because DataOne retired temporary generation ahead of permanent Bloom fuel-cell power, which "reset the schedule". "The contracts behind that capacity remain in place." | Letter, CEO letter and 2026 Guidance |

## Figures (US$, unaudited, company)

| Item | Q3 2025 | Q3 2026 | 9M 2026 |
|---|---|---|---|
| Revenue | 146.1M | **980.8M** (+571% YoY, +68% QoQ; incl. ~325M non-recurring asset-light) | 1,962.1M |
| Adjusted EBITDA | (5.2)M | 465.8M | 831.5M |
| Net income / (loss), continuing | (119.6)M | (37.5)M | 393.3M |
| Operating cash flow, continuing | (80.6)M | **(273.0)M** | 4,231.1M |
| Purchases of PP&E and intangibles | (955.5)M | **(7,300.4)M** | (15,430.7)M |
| Financing inflow | 4,200.6M | 7,457.6M | 16,618.0M |

Balance sheet 9/30/2026: cash 7,425.6M; receivables 4,039.9M (720.3M at 12/31/2025); deferred revenue 1,445.5M current + 7,963.7M non-current; debt 187.5M current + 14,003.3M non-current. RPO $38.7B (+3% from $37.5B at 6/30).

## Guidance

| | Before | Now |
|---|---|---|
| 2026 revenue | $3.0–3.4B | **low end** of $3.0–3.4B |
| 2026 adj. EBITDA margin | ~40% | ~40% (unchanged) |
| 2026 capex | $20–25B | **~$27B** (above range; owned sites for 2027) |
| ARR | $7–9B by December | **>$7B for February** (~2 months later) |
| Contracted power | 5 GW by YE | 5 GW by YE (>4 GW now) |
| 2027 | — | revenue $12–13B; capex $40–45B; pre-tax breakeven Q4 2027; 75–85% of capex from prepayments + asset-backed financing of IG contracts; prepayments $10B committed 2026, $17–20B 2027 |

## Reading for the channels

- **S3 (power):** a developer-side power-source transition delayed a contracted build; the contract is kept. The letter is grid-side refusal or curtailment that **removes** firm capacity ⇒ **NOT FIRED**, S3 stays 3. New member of the KB-387 theme (contracted sites slipping a quarter at a time).
- **S1:** a neocloud **raised** capex; no hyperscaler cut. Leading indicator stays ARMED; this is neither a lease pause nor an order cancellation.
- **S5:** nothing pulled or flexed. The October Citi $3.5B (KB-300) is a 364-day corporate bridge; the July $775M ABS (SOFR+2.50%) is secured on an IG contract. Not like-for-like, so not a VULCAN-13 leg (b) datum on its face; the 11/15 grading judges.
- **GPU rentals:** company says Q3 prices rose more than 20% per GPU-hour vs Q2; ACV/MW >$25M; reserve auctions cleared >15% above reserve. A seller's claim, consistent with the panel's "no rent glut".

## Caveats that travel

1. About $325M of Q3 revenue is one-off asset-light partner revenue; ex that, about $656M (INFERRED subtraction).
2. Q3 operating cash was −$273.0M: receivables +$3,761.8M against deferred revenue +$3,434.0M ⇒ prepayments billed but not collected at 9/30 (INFERRED from the cash-flow lines). "Prepayments cover capex" was not yet cash at quarter end.
3. RPO rose only $1.2B in the quarter while the letter cites "$12B TCV signed since the beginning of Q3" ⇒ most of that sits in early Q4 (INFERRED, not stated).
4. Servers depreciated over five years, up from four before 2026 (company); Nebius is not one of the S1 useful-life sub-read's four names.
5. Company, unaudited; the call and the eventual 6-K may qualify any of this.
