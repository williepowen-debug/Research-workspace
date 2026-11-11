# Plaza Continental: November 11 docket pre-read

**Date:** 2026-11-11 | **Mode:** Cold | **Authority:** PROME November 11 catch-up assignment, DOCKET L517; Will's instruction to proceed to the next research assignment. **Confidence:** High on documents read; limited by unavailable documents and RECAP coverage.

## Key finding

**No new evidence changes the Ontario Nano-lien ownership branch or supplies a sale price.** The restored authenticated search closes the previously missing September 29–October 7 docket-history window. A readable notice establishes a **November 17, 2026, 2:00 p.m. Pacific final cash-collateral hearing**, not a sale or disclosure-statement hearing. The debtor also sought to reject a restaurant lease because it said it could not fund the tenant improvements; the latest indexed November 9 entry is labelled a lease-rejection order, but its text is unavailable. These are case developments, not a new collateral valuation. [S1–S3]

## Evidence and consequences

| Item | What the retrieved record says | Consequence within WAL's H1–H11 read-sheet |
|---|---|---|
| September 29, Docs 93–97 | FDIC-R filed an appearance; Doc 82 hearing continued to October 8; older stipulation Doc 58 taken off calendar as superseded by Doc 82 | Closes the prior history gap. Bare appearance/continuance does not establish ownership; H6 NO-VERDICT for that hearing |
| October 2–6, Docs 100–102 | FDIC-R requested a 30-day stay; debtor and Preferred opposed | Confirms the already known procedural sequence, not a new extension or allocation |
| October 15–16, Docs 107,109,112,113 | FDIC-R named on stipulation; motion granted under that stipulation; orders entered | Prior October 15 FDIC-R observation stands; no new title evidence |
| October 16, Doc 108, pp.1–2 | Final hearing on use of cash collateral November 17 at 2 p.m.; opposition deadline November 3, reply November 10 | Concrete next hearing. Operating-fund authorization, not sale authority; no H8 sale-price observation |
| October 20, Doc 116, pp.1–2 | Debtor seeks rejection of Dapper Dine & Lounge lease at 3660 Porsche Way; 6,261 square feet, initial rent $14,087.25/month, tenant-improvement allowance up to $250,440 | Debtor reports inability to fund landlord work, tenant not occupying, and argues vacancy improves marketability. No proven buyer, price or recovery consequence |
| November 9, Docs 125–126 | Short labels: no party requested hearing; reject lease or executory contract | Consistent with the rejection proceeding, but full descriptions/PDFs absent. Do not infer the order's exact terms or link solely from sequence |
| October 26, Docs 119–120 | Disclosure statement and liquidation plan indexed; `is_available=false`, no stored PDF path | H7 current Nano balance / H11 priority still unread. A token restores search, not missing documents |

[S1] is the authenticated CourtListener document search for docket **73112993**, filing dates **September 29 onward**: **45 unique indexed records across all 3 returned pages**, including unnumbered procedural records. Latest filed date returned: November 9. This is not 45 distinct numbered pleadings, not a certified current PACER docket, and not proof that nothing newer was filed. Fresh RSS corroborates the two latest entry labels. [S2/S3] are identity-verified PDFs, not inferred storage URLs.

**WAL branch read:** no new move from its existing B1 treatment (FDIC receiver retained Ontario, docket-evidenced at the earlier observation). This read does not independently prove present recorded ownership. H2/H3/H4: no new transfer identified in the returned descriptions. H7/H11 remain unresolved. H8: no sale, foreclosure or stay-relief authorization identified. H9: no Cantor-lien avoidance pleading identified. H10: the prior stay request is visible, no later extension identified. Incomplete descriptions and unread documents limit every negative. Other properties are outside this read.

## Counter-evidence and unresolved questions

The tenant-improvement problem is **the debtor's asserted reason** in its notice, not a judicial finding that the property has lost value. The debtor argues removing the lease improves saleability; a failed or unaffordable lease is therefore not a one-way valuation signal. The notice does not show an existing occupied tenant stopped paying rent. Its terms cannot establish the amount due on Nano's loan or what Western Alliance will recover.

The hearing is noticed for **Tuesday November 17, 2 p.m. PST / 5 p.m. EST**. The existing **November 16 L517 check-by** remains a pre-hearing check, not a mistaken court date and not a completed hearing read. Plan/disclosure contents, sale terms and current lien balances remain unavailable through the retrieved free records. No PACER purchase or new monitoring job was made.

## Sources and reproduction

- **S1:** [CourtListener docket search](https://www.courtlistener.com/?q=docket_id%3A73112993&type=rd&order_by=entry_date_filed%20desc); actual date-filtered API URLs, retrieval timestamps and hashes in `research/2026-11-11_L517/provenance.json`. Three raw JSON pages, `docket-read.tsv`, and fresh `feed.xml` are saved there. Search/read November 11, 2026. Raw court docket descriptions distributed by RECAP are the primary record reproduced here; coverage is not independently certified against PACER.
- **S2:** [Doc 108, final-hearing notice](https://storage.courtlistener.com/recap/gov.uscourts.cacb.2042304/gov.uscourts.cacb.2042304.108.0.pdf), filed October 16; pp.1–2. Header verified: 8:26-bk-10986-MH, Doc 108. SHA-256 `bfaae1faafe9d47a6e0d4df6aeaebbe867c4ade1a9ac2f6a8f4e96c10935bf45`.
- **S3:** [Doc 116, lease-rejection notice](https://storage.courtlistener.com/recap/gov.uscourts.cacb.2042304/gov.uscourts.cacb.2042304.116.0_1.pdf), filed October 20; pp.1–2. Header verified: same case, Doc 116. SHA-256 `2e5a95ae7319e7697f68fe9ca5b2e49cfd6d26565d5aef32b57e97306b7a6f6a`. Text copies for both documents saved beside the search evidence.
- Interpretation boundary: `AGENTS/WAL/research/2026-09-27_nano-banc-receivership-stupin-recovery.md` §10; prior `output/2026-11-02_plaza-continental-docket-read.md`.

## Process report

Authenticated `recap_pull.py search` works end to end. One initial broad search used an unsuitable ordering field and was superseded by the complete date-filtered, correctly ordered three-page query. One fresh feed and two cached/downloaded identity-checked PDFs supplied the read. Web-tool docket HTML access failed; the authorized API supplied the data. No guessed PDF addresses, paid access, external messages or subagents. Existing helper pagination was handled in the research scratch, preserving its shared cache and budget. No source-helper build is needed for this research. The separate `usage` endpoint maintenance remains open.

**Do-not-relay-as:** a sale hearing, a confirmed collateral markdown, loss of an occupied tenant's cash rent, a new transfer to FDIC/WAL/Sunwest, or final lien-priority evidence.

## Recipient actions

WAL consumes against H1–H11; CREED receives the bounded property evidence; PROME reconciles L517 with the November 17 noticed hearing while retaining the November 16 check-by. TERRY receives the material case update for tradeability assessment; no construction is proposed by DEWEY. WALTER logs the research output. All retain the missing-document and coverage limits.
