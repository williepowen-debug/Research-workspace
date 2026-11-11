# Plaza Continental: broker confirms 31% marketed occupancy; court economics remain unread

**Date:** 2026-11-11 | **Mode:** Cold | **Authority:** Will's instruction to investigate remaining obtainable evidence; DOCKET L517 continuation. **Confidence:** High on what the broker publishes and the retrieved RECAP metadata; UNKNOWN on verified operating occupancy, sale economics and priority.

## Finding

The selling team's own public property page reports **31% occupancy**, approximately **114,505 square feet**, and **“Best Offer”** pricing for Plaza Continental, 3700 Inland Empire Boulevard, Ontario. This upgrades the occupancy figure from a press lead to a directly observed **broker representation**, not an audited rent roll. It supplies no dollar price, current NOI, loan payoff or recovery waterfall. [S1]

The liquidation plan (Doc120), disclosure statement (Doc119), and November9 rejection order (Doc126) still have **no available PDF in fresh individual RECAP metadata**. Their contents remain unread. A public marketing campaign does not establish sale approval, a binding bid, lien ownership or recovery. The previously verified November17 2pm Pacific hearing remains a cash-collateral hearing. [S2; preceding pre-read]

## What the additional search established

| Evidence | Result | Limit |
|---|---|---|
| Broker team's NRP West property page, read Nov11 | 31% occupancy; ±114,505 SF; office/retail and four restaurant pads; price Best Offer | Broker marketing, not independently verified operating results; no effective rent-roll date stated |
| Broker-attributed Showcase sale listing | Main building described as 84,486 SF with 73,110 SF vacant; seven parcels, five improved | Main-building perimeter differs from entire property; cannot use its vacancy as whole-property vacancy |
| Public marketing access | Offering memorandum and financials link leads to registration | No registration, contact submission or external message made; protected materials not read |
| RECAP document records 499226756 / 499226757 / 500834611 | All `is_available=false`; no local or Internet Archive filepath | Confirms absence through this retrieved source, not global unavailability or absence from PACER |
| Fresh docket-document search from Oct20 onward | 13 indexed records, no next page; latest returned filing Nov9 | RECAP indexing is not a certified current court docket |

[S1–S3; evidence saved in `research/2026-11-11_L517-remaining/`.]

## Reconciliation and counter-evidence

Do **not** derive a measured occupancy collapse from the broker's 31% and older city/lease listings. Source dates, building-area totals and leased-versus-occupied definitions are not reconciled. Showcase's broker roster showed 139,841 SF while the specific property page displayed 114,505 SF; the direct NRP property page supports the latter marketed size. These are reasons to prefer the direct page for the current representation, not proof that all physical or leasing measurements agree. [S1/S3]

The property is marketed as a redevelopment/value-add opportunity. Vacancy alone is not a valuation or recovery conclusion. The earlier court notice says the proposed Dapper tenant was not occupying; rejection therefore does not prove loss of an occupied tenant's cash rent. The older Keen-Summit bankruptcy marketing concerns an earlier Sarkis case and must not supply current price/NOI. [S3; preceding pre-read; S4]

## What remains unknown

No verified current rent roll or NOI, accepted bid or sale price, approved sale procedure, current Nano debt balance, final lien priority, or lender recovery was obtained. No source-explained ownership change follows. The plan and disclosure statement may contain relevant economics, but their filing labels do not establish those contents. The free-source pass found additional factual evidence; it did not close the case's economic questions.

**Disposition:** Add the broker's current representation to the property evidence. Keep WAL's existing ownership branch and H7/H8/H11 unresolved questions unchanged. Keep the November16 pre-check and November17 noticed hearing distinct. No new watcher, paid retrieval or trade proposal.

## Sources and reproduction

- **S1 PRIMARY marketing:** [NRP West / CBRE selling-team property page](https://www.nrpwest.com/properties/plazacontinental/). Found through the team's public sitemap; curl GET succeeded when the web reader failed. Full HTML, readable text, timestamp and SHA256 saved as `broker.html`, `broker.txt`, `marketing-provenance.json`. Public offering-materials link: `https://plazacontinental.sharplaunch.com/signup` (not used to register).
- **S2 PRIMARY docket metadata via RECAP:** [CourtListener docket search](https://www.courtlistener.com/?q=docket_id%3A73112993&type=rd&order_by=entry_date_filed%20desc). Exact API query/time/hash in `provenance.json`; raw search and three fresh individual metadata responses saved alongside it. Authenticated authorized reads used the existing shared cache/budget helper. No paid PACER retrieval.
- **S3 BROKER-ATTRIBUTED listing:** [Showcase Plaza Continental sale page](https://www.showcase.com/plaza-continental/42545665/), read Nov11, particularly highlights/overview and area footer; [John Read roster](https://www.showcase.com/p/john-read/2061013/). This republished listing is supporting evidence, not a second independent property measurement.
- **S4 HISTORICAL, excluded from current valuation:** [Keen-Summit earlier marketing](https://www.keen-summit.com/keen-summit-capital-partners-markets-mixed-use-restaurantoffice-complex-in-ontario-ca/).
- Prior identity-checked court notices and hearing/lease evidence: `output/2026-11-11_plaza-continental-preread.md`, S2/S3. No new interpretation of unread Doc126 is asserted here.

## Process report

Targeted public searches, fresh RECAP search and three individual document-metadata reads, then broker-site discovery through its public sitemap. A November4 Registry article supplied the 31% lead; the broker page independently confirmed the published figure. Registry's remainder is paywalled, ElevenFlo documents require access, and a Realmo curl request returned403; none was bypassed or treated as document evidence. No subagents, paid access, broker contact or new tooling. Remaining limitations are disclosed rather than filled by inference.

## Recipient actions

WAL: add the marketing representation within existing H1–H11 work, retaining the unknown economics. CREED: distinguish marketed occupancy from verified rent roll and valuation. TERRY: no new price/recovery or executable trade conclusion. PROME: record the additional evidence; retain L517's existing dates and missing-document condition. WALTER: log the delivered continuation and verify pointers. Consumption remains unverified.
