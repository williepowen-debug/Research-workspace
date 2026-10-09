# Nano Banc — FDIC bid summary read + §3 shared-figure re-run (DOCKET L516)

**Desk:** REGINALD · **Written:** 2026-10-09 Fri, ~10:3x ET (PROME-spawned L516 due-row wake, prome-75) · **Parent report:** `reports/2026-09-27_nano-banc-failure-forensics.md` §3 (the shared figure). This file re-runs §3; the 9/27 file is not rewritten.

## 0. Answer first

| Question (L516 READ cell) | Answer at the primary, read 2026-10-09 10:26 ET | Token |
|---|---|---|
| Has the FDIC posted the **P&A agreement**? | **NO.** The failed-bank page's "Transaction Documentation" section lists only the **Bid Summary**; two candidate P&A slugs return **404** (`…/purchase-assumption-agreement-nano-banc-irvine-ca.pdf`, `…/purchase-assumption-agreement-nano-banc.pdf`). Metropolitan Capital's page, same template, lists BOTH links (P&A pdf `last-modified` 2026-02-12). | VERIFIED (absence = page link list + 2 slugs; an unlisted third slug is not excluded) |
| What DID post? | **The FDIC Bid Summary** (`fdic.gov/bank-failures/bid-summary-nano-banc-irvine-ca`, page "Last Updated: October 8, 2026"), 13 days after closing. | VERIFIED |
| Loss-share? | **None on the winning bid** ("Commercial Shared-Loss: N/A"; shared-loss was offered only on Whole Bank P&A). | VERIFIED |
| Deposit premium? | **0.85% on All Deposits** (winning bid). ≈ **$5.1–5.3M** on $605M (Sunwest) – $626.8M (9/22 books). | rate VERIFIED · dollars INFERRED (premium base not stated; brokered deposits are often excluded → ≤) |
| Purchase discount? | **Loan Pool B at 82.30%, Pool C at 80.17%** (of book value — INFERRED: the column is unlabeled on Nano's page; the FDIC's Valley Bank 2014 summary labels the same columns "(% of BV)"). **Pools A and D: "No Bid" by Sunwest ⇒ retained by the FDIC.** Optional securities pool: **Yes**. Asset discount: N/A (Basic P&A). | VERIFIED (prices) · INFERRED (BV basis) |
| Which assets / the $97.1M held-for-sale pool / the four Nano DOTs (WAL O1)? | **NOT ANSWERABLE from the bid summary — it does not define the pools or give their sizes.** Awaits the P&A schedules. | SEARCH-NOT-FOUND |
| The ~$81M deposits gap? | **Partly closed by the 9/22 books:** $686M [6/30] → $626.8M [9/22] = −$59M pre-failure run; residual ≈ **$22M** between the 9/22 books and Sunwest's "$605M" is unexplained (3-day run, or Sunwest's measurement basis). "All Deposits" passed on the winning bid, so no depositor took a loss. | figures VERIFIED · residual cause UNKNOWN |

## 1. The bid summary (FDIC primary, transcribed; `Last Updated: October 8, 2026`)

**Winning bid — Sunwest Bank, Sandy UT:** Basic P&A · All Deposits · Deposit premium **0.85%** · Asset discount N/A · Pool A **No Bid** · Pool B **82.30%** · Pool C **80.17%** · Pool D **No Bid** · Commercial shared-loss N/A · Optional securities pool **Yes** · Conforming **Yes**.

**Other bids (32, plus the winning bid = 33; bidders not linked to bids except the winning and cover bids; the cover bid is disclosed one year after failure):**

| What the other bids say | Figure | Read |
|---|---|---|
| Best outside bid on **Pool A** (retained) | **37.43%** (others 5.00%) | the worst pool; ≥62.6% haircut even at the best outside price |
| Best outside bid on **Pool D** (retained) | **65.55%** (others 61.75%, 40.00%, 35.00%) | ≥34.5% haircut at the best outside price |
| Pool B / C outside bids | B 82.30% (a tie with the winner) / 40.00% / 35.00%; C 78.06% / 50.37% / 40.00% / 35.00% | winner's C at 80.17% beat every outside C bid |
| Whole-bank P&A asset discounts | **$37.2M → $358.5M**; cheapest with **no** loss-share **$152.0M** (0.00% premium) | §3 cross-check below |
| Bidders named (8) | Aspira Bank · Axos Bank · Cache Valley Bank · Commercial Bank of California · First-Citizens Bank & Trust · MVB Bank · New Omni Bank · Sunwest Bank | — |

## 2. §3 re-run — the shared figure

**What changes and what does not.** The headline **≈ $120M ≈ 17% of $690.9M (9/22 books; range $110–120M)** is **UNCHANGED**: it is equity consumed ($5.66M) + the FDIC's estimated DIF cost ($114M), and the bid summary changes neither. **What changes is the ALLOCATION:** the "≈51–56% zero-adjustment scenario" on the ≈$215M retained pool is now known to be wrong in its premise — the adjustments are not zero, and the net of them points DOWN.

| Leg | Sign on the retained-pool loss | Size | Basis |
|---|---|---|---|
| Purchase discount on Pools B+C (loss carried by the PURCHASED loans, paid via the DIF) | **lowers** | **≈ $35–45M** | book of B+C ≈ **$199.5M** (FDIC $476M − 9/22 cash $230.9M − securities $39.7M − FHLB/FRB stock $6.0M) to **$227M** (Sunwest release) × 17.70–19.83% |
| Deposit premium (reduces the DIF cost, so the ASSET loss is larger than DIF+equity by it) | **raises** | **≈ $5.1–5.3M** (≤) | 0.85% × $605–627M |
| Receivership/admin costs inside the DIF estimate (unchanged from 9/27) | lowers | $0–10M | assumption, as 9/27 |
| Unpaid junior creditors | raises | small — other liabilities $8.4M [9/22] | as 9/27 |

> **CITE THIS (desk SCENARIO, 9/22 base; supersedes the "≈51–56% zero-adjustment" line of 9/27 §3):** on the bid terms the FDIC posted 10/8, **the loss allocable to the ≈$215M the receiver kept is ≈ $70–90M ≈ 32–42%**; the other ≈ $35–45M of the ≈$120M sits on the loans Sunwest bought at 80–82% of book. **Direction VERIFIED (discount ≫ premium); magnitude INFERRED** — the bid summary does not size Pools B/C, so the purchased-loan book is bracketed by two reconstructions ($199.5M from the FDIC's $476M; $227M from Sunwest's release). Not a bound: the DIF figure is an estimate that "is expected to change over time as retained assets are sold" (FDIC PR 9/25).

Arithmetic (reproducible): high = 119.66 + 5.33 − 0 − 199.5×0.1770 = **$89.7M = 41.7%** of $214.9M · low = 119.66 + 5.14 − 10 − 227×0.1983 = **$69.8M = 32.5%**. Zero-adjustment (9/27): 110–119.7 / 214.9 = 51.2–55.7%.

**Two market cross-checks the bids now allow (both point the same way):**
1. **The FDIC's estimate is lighter than the market's whole-bank price.** The cheapest whole-bank bid with no loss-share asked a **$152.0M** discount = **22.0%** of 9/22 assets, against equity+DIF **$119.7M = 17.3%**. The FDIC chose Basic P&A because it values its retained pools above what whole-bank bidders would pay; that valuation is the FDIC's model, not a sale. ⇒ **The ≈$120M is more likely to rise than fall as the retained assets sell** (INFERRED; the Fed OIG MLR ~late Mar 2027 and the DOCKET L515 disposition print settle it).
2. **The retained pools were priced by outside bidders at 37.43% (A) and 65.55% (D) at best.** A retained-pool loss of 32–42% fits only if Pool D (≥34.5% haircut) dominates the retained book and Pool A (≥62.6%) is small. If Pool A is the $97.1M held-for-sale book, the retained-pool loss at the best outside bids would exceed the 32–42% scenario — **unresolvable until the P&A sizes the pools.**

**Fences (unchanged, carried):** a mark on a *fraud-tainted, litigated* SoCal book — not a read-through to SoCal CRE generally. n=1. The pool percentages are bids on a pool, never a property mark; second-lien loans inside a pool are not a collateral mark (DOCKET L515 recording rule).

## 3. What routes

| To | What | Why |
|---|---|---|
| **CREED** (composition) | bid summary + the retained Pools A/D outside bids (37.43% / 65.55%) as a pre-sale market read for S6 | L515 S6 comp: the retained-pool disposition is still the comp; these are REJECTED bids, not a clearing price |
| **WAL** (O1 consumer) | O1 is **not resolved**: the bid summary names no loans and does not define the pools; the four DOTs stay in the open ownership branches | L516 READ cell |
| **PROME** | memo; next check date | — |

**Next check for the P&A agreement: Tue 2026-10-13** (Mon 10/12 is Columbus Day, a federal holiday), then each Tuesday; at 2026-10-27 (one month after closing) without a posting, ask DEWEY for a FOIA/Receivership-records route. The P&A is the only document that sizes the pools and lists the held-for-sale and DOT dispositions.

## 4. Provenance

- Failed-bank page: `https://www.fdic.gov/bank-failures/failed-bank-list/nano-banc` (HTTP 200, page text "Last Updated: October 8, 2026"), read 2026-10-09 10:26 ET.
- Bid summary: `https://www.fdic.gov/bank-failures/bid-summary-nano-banc-irvine-ca` (HTTP 200), read 2026-10-09 10:26 ET.
- P&A candidates (404, 10:26 ET): `…/purchase-assumption-agreement-nano-banc-irvine-ca.pdf` · `…/purchase-assumption-agreement-nano-banc.pdf`.
- Column-basis precedent: `https://www.fdic.gov/bank-failures/bid-summary-valley-bank-fort-lauderdale-fl` ("Optional Loan Pool … (% of BV)").
- 9/22 balance sheet: DFPI possession order Exh. A via `AGENTS/DEWEY/output/2026-09-27_nano-banc-primary-documents.md` §(Exhibit A). FDIC PR 9/25 ($476M purchased, $114M DIF estimate) via the same file.
