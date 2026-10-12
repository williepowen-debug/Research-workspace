# CARL fintech consumer-credit feed to REGINALD

**Defined:** October 12, 2026. **Owner:** CARL. **Bank-perimeter owner:** REGINALD.
**Authority:** WQ-228, Will ruled September 15; REGINALD's September 17 encode. Will approved this feed-definition step directly in the October 12 CARL session.
**Stage:** Definition and initial source-backed packet complete; recipient agreement and first Q3 refresh pending.

## Coverage and purpose

Identify deterioration in a fintech consumer book and establish the contractual path by which a bank could bear it. A brand/bank relationship alone does not establish retained credit exposure. CARL supplies the consumer-book evidence; REGINALD reconciles bank concentration, provisions and recoverability. LIQUID supplies ABS pricing/marks. Signals travel through WALTER; coverage agreements and analytical answers travel directly to REGINALD.

The initial coverage register is `fintech-feed/COVERAGE.tsv`: seven product/role rows across four groups, all owned by CARL. PHAN's existing dossier supplies Affirm/Klarna borrower evidence at its stated vintage; this definition does not refresh its data clock or require a new child session.

| Group | CARL coverage | Boundary / unobserved exposure |
|---|---|---|
| CCBX | Coastal's credit-card and other-consumer loan categories; partner indemnification/credit-enhancement collectability relevant to those books | Portfolio categories are disclosed; partner/product allocation is not. “Other consumer and other” is the issuer's mixed label. Do not call all CCBX loans consumer or assign the unnamed problem partner to LendingPoint. Bank loss accounting belongs to REGINALD. |
| Affirm | U.S. bank-originated installment credit; originating banks Celtic and Lead. Affirm Card issuance by Evolve/Stride is a separate relationship row. | FY2026 filing describes Affirm's purchase obligation, secured by cash deposits, and purchase of all partner-originated loans to date. Origination/card issuance is not the same as permanent borrower-loss retention. Interim exposure, performance fees and contractual recourse need separate measurements. Cross River in older language is not promoted to the current primary-originator row. |
| Klarna | U.S. monthly financing through WebBank; card relationship separately labelled, with product/version verification required | Global GMV, global credit provisions, monthly financing, pay-in-4, and debit/card pay-later products are different perimeters. No WebBank-held loan balance or indemnification amount established. Do not map all Klarna lending onto WebBank. |
| SoFi | Personal-loan credit and on-book/sold/third-party-origination distinctions; direct-bank comparator | SoFi's own bank is not evidence of exposure at an outside sponsor bank. The Q2 earnings source establishes the bank/platform distinction; October12 follow-up now reads the full Q2 10-Q Note4/MD&A transfer disclosures; legal-entity/product attribution remains incomplete. The private SoFi 144A trust gap remains open. |

CASH/GDOT and private charters remain REGINALD's bank watchlist. CARL adds a consumer-book row when a primary disclosure establishes a product/credit relationship, or REGINALD requests reconciliation within this perimeter. A deposit/payment partner, a merchant business book or a bank name in a marketing footer does not by itself establish consumer-loan loss exposure. CCBX HELOC evidence remains an owner join with HOMER; it is not pooled into this unsecured/card seed.

## Cadence and dated carriers

| Occasion | CARL action | Carrier |
|---|---|---|
| Each covered issuer earnings release and 10-Q/10-K | Read the consumer-credit tables and relationship/transfer notes. Send a dated analytical update to REGINALD. Mark release-only coverage PARTIAL until filing notes are read. | CCB/SOFI calendar quarters; Affirm fiscal quarters; Klarna calendar quarters. Their reporting periods remain separate. |
| Material partner exit, purchase/indemnification failure, credit-loss disclosure, underwriting/funding change, or regulatory restriction | Read the primary event evidence at the next CARL working session. Route a new signal through WALTER; answer bank-exposure questions directly with source locators. | WALTER intake plus issuer/regulator filings. No new numerical firing threshold. |
| October 26 owner review | Check acknowledgment and available CCB/SOFI Q3 releases; list unpublished/inaccessible components and issuer-confirm any remaining dates. | New CARL docket review date, **not an asserted earnings date**. |
| Existing November 12 PHAN window (approximately November 5–20) | Use the next available Affirm/Klarna releases for the consumer feed; preserve fiscal/calendar and quarterly/FY bases. | Existing docket row extended with this feed obligation. No new PHAN commission. |

CARL aims to send a release update within two business days while active, and a filing-note supplement within two business days of reading the filing. A dark desk or source failure is a coverage delay, not a clean null; record it on the dated review carrier. This is owner-session work, not an installed scheduler or continuous monitoring claim. A substantive no-change read produces a dated NO CHANGE conclusion only for the documents actually read. An unread or missing document stays UNKNOWN.

## Packet format and reconciliation

Each analytical packet has a unique dated filename, `YYYY-MM-DD_from-CARL_fintech-consumer-feed_<period-or-event>.md`, and contains:

1. Authority, scope, actual read time, observation period and source-publication date.
2. One row per fintech **product × bank role × credit holder × observation period**. An undisclosed dimension is UNKNOWN.
3. Credit measures with exact issuer names: loan balance, DQ bucket, NCO/provision, underwriting/vintage mix, originations/GMV, sales and retained interests when published. Each value carries unit, denominator, stock/flow, quarter/FY period and document/table locator.
4. Loss-allocation evidence: purchase obligation, indemnification, collateral, recourse, retained tranche or fee, and collectability. Keep consumer impairment separate from sponsor reimbursement impairment.
5. Like-for-like comparisons and counter-evidence; list sold/delinquent exclusions and changes in product/geography/seasoning. Quarterly Affirm provision growth is not replaced with FY growth; Klarna global provision/GMV is not a U.S. bank exposure ratio.
6. Bank-facing implication labelled DIRECTLY OBSERVED, CONDITIONAL or UNKNOWN. CARL does not turn an originator relationship into a dollar bank loss.
7. Exact access/observability gaps, next review date and named owner. Recipient acknowledgment is recorded only when actually received.

Numbers not published are `UNKNOWN` with the reason, not bare zero. Structural non-applicability is `NOT_APPLICABLE`; an observed zero retains a source/basis. No sum across issuer stocks, origination flows, GMV, sold balances and retained interests. Matching issuer and bank disclosures of one exposure are joined by source identity, not added. REGINALD owns the reconciled bank figure; CARL preserves its consumer-book observation and references that resolution. Revisions annotate the earlier version and update the live source-backed figure; frozen/as-made grading records are unchanged.

## Initial evidence and first packet

Source receipts and locators are in `fintech-feed/SOURCES.md`. Five atomic entries are retained at KB-CARL-519–523; the coverage register references them rather than creating another numerical authority.

- CCBX Q2 credit-card stock: $753.171M at June 30, 2026. Other consumer and other stock: $918.779M. Issuer-primary CCBX loan-portfolio table; these categories do not identify the troubled partner or a net uninsured loss. Both are historical Q2 observations re-read October 12, not a new quarter.
- Affirm FY2026 loan-purchase mechanics separate borrower risk from bank origination/issuance. Source-backed relationship mapping is available; bank-specific residual loss amounts are not.
- Klarna's primary monthly-financing disclosure names WebBank. Its historical debit-card pilot release identifies a separate product. Current card contract/version and retained credit risk need a separate read.
- SoFi's Q2 release identifies its own bank and third-party/platform activity. Initial web read failed; later direct retrieval succeeded and full Note4/MD&A transfer sections were reviewed. Supplement: `2026-10-12_SoFi-transfer-risk-supplement.md`; consolidated servicing stocks/retained-consideration flows/prior markdowns remain distinct.

The definition and seed analysis go to REGINALD with a request to accept or correct the join fields before the first Q3 supplement. PROME receives the implementation checkpoint. New CCBX product detail/relationship evidence goes to WALTER for dedupe/routing judgment. Filing a packet is not proof of recipient consumption.

## Remaining limits

The unknown CCBX partner cannot be resolved from the cited company release. Private-bank product balances, Klarna U.S./WebBank exposures, bank-specific Affirm residual risk and SoFi product/legal-entity loss allocation remain unmeasured. SoFi Q2 transfer/recourse tables are now read; the narrow access gap is resolved. These constrain attribution, not completion of the feed definition. No prediction, grade, threshold, capital instruction or peer-owned file changes under this step.
