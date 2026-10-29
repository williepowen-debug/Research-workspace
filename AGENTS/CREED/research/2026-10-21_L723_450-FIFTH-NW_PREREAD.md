# L723 PRE-READ — 450 Fifth St NW ("Judiciary Plaza"), Washington DC: trustee's foreclosure auction Wed 2026-10-28

**Written:** 2026-10-21 (Wed) ~23:00 ET (`date` 22:58 EDT at start), CREED, WQ-472 bounded catch-up (Will, 2026-10-21 22:46 ET). **PROME DOCKET L723.** **Status:** ⛔ the §3 reading below is **FROZEN on commit of this file** — the grading record is appended below §5 after 10/28, never edited above it. **No grade until 10/28.**
**Evidence:** a CREED read-only research helper (Opus), whose findings file is kept verbatim at `research/2026-10-21_L723_helper_findings.md` (every claim tiered). CREED's own spot-check of the auctioneer listing confirmed only that a live Alex Cooper listing exists for 450 5th St NW (the page renders its terms by JavaScript, so CREED's fetch saw placeholders). ⇒ the auction terms below are **PRIMARY-CITED** (read at the auctioneer listing by the helper), not PRIMARY-READ by CREED.

## 1. Identity

| Field | Value | Tier |
|---|---|---|
| Property | 450 5th St NW, Washington DC 20001 (Square 489, Lot 21), "Judiciary Plaza" / "Liberty Square"; the SEC's former headquarters address | primary (auctioneer listing; DC OTR extract 2026-09-18; sec.gov 2001) |
| Class / type | **OFFICE**, 11 stories, built 1981, 2-story 242-space garage; **481,721 ± sf net rentable** (auctioneer). The 539,478 sf in the relay is another measure (SECONDARY). No source read assigns a Class A/B/C grade | primary / secondary |
| Tenancy | Department of Justice was the sole tenant (certificates of occupancy 2008, floors 1–11); agreed in 2022 to move to 555 4th St NW; the 2026 zoning order says the tenant "is vacating". **No dated occupancy %** | primary (CofO, zoning order) / secondary |
| Conversion | Zoning Commission Order 78-17A approved 5-0-0 on 2026-03-23 (applicant Judiciary Plaza, LLC): ~500 units incl. 39 affordable; developer The Georgetown Co. (not on title) | primary (order) / secondary (developer) |
| Owner of record | JUDICIARY PLAZA LLC; sponsor Clark Enterprises per Bisnow 2/2025 | primary / secondary |
| Loan | Deed of trust dated and recorded 2007-11-14 securing **The Prudential Insurance Company of America** (a life-company loan); **assigned 2022-12-21** (Inst. 2022124392) — the assignee is an affiliate of **Criterion Real Estate Capital** per press, legal name not shown | primary as recited in the trustee notice / secondary (Criterion) |
| Position | Senior first-lien **note BUYER** (not originator, not mezz) | INFERRED |
| Amount | **Note $177.5M (2007); $166.6M owed** "according to the notice" | SECONDARY only (WBJ 9/29 via Connect CRE 10/01; the listing states no amount) |
| CMBS / CRE CLO | **None found** (EDGAR full-text swamped by the SEC's own old address; Prudential named directly on the deed of trust fits a balance-sheet loan) | SEARCH-NOT-FOUND / INFERRED |
| Sale | **Substitute Trustee's sale of the FEE** (non-judicial, deed of trust), with FF&E sold under the UCC at the same time. **Wed 2026-10-28 11:00 AM**, Alex Cooper Auctioneers, 4910 Massachusetts Ave NW. Trustee Frederick L. Klein. Deposit $5,000,000 rising to 10%; all cash; settle within 30 days; **the noteholder is exempt from the deposit**; the trustee may postpone. Foreclosure notice recorded 2026-09-28. Listing "active", last updated 2026-10-13 | PRIMARY-CITED |
| Basis marks | 2007-11-14 recorded "Market Sale" $62,047,563 (same day as the deed of trust; may not be a full fee price) · DC assessment: current **$92.9M**; prior-year total $158.39M; proposed new total **$69.71M** (land $67.44M + improvements $2.27M) — **tax-assessor basis, not a market price** | primary fields (OTR extract) / INFERRED meaning |
| After 9/29 | WBJ 9/29 headline: "Housing to proceed near Judiciary Square despite foreclosure filing". No postponement, bankruptcy or payoff found as of 2026-10-21 (PACER not checked — login) | secondary / SEARCH-NOT-FOUND |

**Ledger:** `cases/CASES.tsv` **CASE-CREED-139**.

## 2. What the outcome CAN and CANNOT evidence (stated before the result)

**It cannot evidence, whatever the price:**
- **Anything on `CREED-T-01a` / `T-01b` / `T-02`.** Those read Trepp's CMBS universe; this is a 2007 life-company loan now held by a debt fund, and no securitization was found.
- **Bank transmission (`T-03`).** No bank lender or bank financing is established on this loan.
- **A gate (`T-06b`) or a forced fund sale (`T-06`)** — it is a lender foreclosure on one asset.
- **Prudential's loss.** Prudential sold the note in December 2022 at a price no source read discloses. Any loss on the 2026 sale falls on the Criterion affiliate's purchase basis, which is unknown — so **the auction price measures collateral value against the debt owed, not the holder's realized loss.**
- **"DC office values" in general.** A single-tenant 1981 building whose only tenant is leaving, with a conversion entitlement, is a land-plus-entitlement asset. It is a comp for obsolete-office-to-residential conversions, not for occupied DC office. One case; the ledger's selection-bias rule applies.

**What each outcome would evidence:**

| Outcome on 10/28 | Reads as | Figures (owed $166.6M is SECONDARY; NRA 481,721 sf) |
|---|---|---|
| **A. Noteholder credit bid wins** (most likely: the noteholder needs no deposit) | Title moves to the Criterion affiliate (REO). **No clearing price** — a credit bid is not a cash sale (WALTER SIG-W-20261012-010's rule, adopted). Ledger event only | none |
| **B. Third-party cash bid ≥ $166.6M** | Collateral covers the reported debt: no loss to the noteholder on the reported figure | ≥ $346/sf |
| **C. Cash bid $92.9M – $166.6M** | Shortfall 0–44% of the reported amount owed | $193–346/sf |
| **D. Cash bid $69.71M – $92.9M** | Shortfall 44–58%; priced near the assessor's land-dominated proposed value | $145–193/sf |
| **E. Cash bid < $69.71M** | Shortfall > 58%; below even the assessor's proposed land value | < $145/sf |
| **F. Postponed / bankruptcy filed / pre-sale deal (e.g. a Georgetown Co. takeout)** | No mark. A negotiated price, if later disclosed, is graded as B–E only if it is an arm's-length cash price | — |

**Pre-registered limits on the grade:**
1. Shortfall % uses the **reported** $166.6M, which may include accrued interest and fees; say so beside every percentage. Never compare a sale price to the assessment as if they were one basis — the assessment rows above are reference marks only.
2. ⛔ **Refuse:** "DC office down X%" from one auction · a CMBS-loss comparison without naming that this is not a CMBS loan · reading a credit bid as a price · reading the 2007 $62.0M recorded sale as a purchase price.
3. **Comparators that may be cited beside it, each on its own basis:** CREED's CMBS severity distribution `KB-CREED-041` (CREFC Aug-2026 72.6% monthly; YTD all-types 35%) — a CMBS realized-loss basis, so **context, not a like-for-like comp**.
4. **No CREED band, score, trigger or prediction moves on any outcome.** The result is a case-ledger event (CASE-CREED-139) and, if B–E, a single conversion-asset price datum.

## 3. The pre-registered reading (frozen on commit)

**CREED's expectation, stated as a reading, not a prediction row (no `PRED-` row is opened — scope):** outcome **A (noteholder credit bid) or F (postponement / negotiated conversion deal)** is the most likely result, because the noteholder is exempt from the $5M deposit and the press reports the conversion "will proceed" despite the filing. **If a third-party cash price prints, CREED expects it in bands D–E (below ~$193/sf)**, because the assessor already carries the improvements at $2.27M of a $69.71M proposed total — i.e. the building is valued as a site. A cash price in band B or C would be the surprise and would say the conversion entitlement carries value the assessor does not record.

## 4. Who does what on 10/28

- **PROME** reads the outcome at primary (auctioneer, trustee, press) and puts any CREED launch to Will (DOCKET L723; CREED launches only on Will's word).
- **CREED**, when next launched, appends the grading record below §5 and adds the CASE_EVENTS rows.
- **Routes on the result:** none required. SHADE (insurers holding CRE) is NOT routed — Prudential exited in 2022, so this is not current insurer exposure. REGINALD only if a bank financing of the buyer is disclosed.

## 5. Open unknowns (the grade must say which were resolved)

Exact amount owed per the recorded notice · the Criterion affiliate's legal name and its 2022 purchase price · note rate, maturity, default date · DOJ's actual move-out date and current occupancy · any Georgetown Co. agreement with the lender · a bankruptcy filing (PACER unchecked).

---

## Grading record — append below after 2026-10-28; do not edit above

### Grade 1 — 2026-10-28 (Wed) ~22:56 ET, CREED (Will-launched session)

**Outcome: A — the noteholder took title (provisional, SECONDARY, headline only).** Washington Business Journal, 2026-10-28 14:40 ET: *"Lender buys Judiciary Square office slated for 500-unit conversion at foreclosure auction"* (URL slug `450-5th-criterion-real-estate-capital-dc-office`). The body was paywalled to every fetch shape tried (browser UAs, WebFetch, web.archive.org, archive.ph, RSS); the Alex Cooper listing served a bot wall. Evidence file: `research/2026-10-28_L723_and_trepp_office_helper_findings.md` (read-only Opus helper; every claim tiered).

- **No clearing price.** Whether the lender's bid was a credit bid or cash is UNREAD. Per §2 and the pre-registered limits, a lender bid is **not** a B–E price even if a figure prints; any amount WBJ reports is recorded as the bid amount, not a mark.
- **The §3 reading (A or F most likely) was correct on its first branch.** No postponement: the sale went ahead.
- **§5 unknowns resolved:** none fully. Partly: the buyer is a Criterion entity (headline/slug), legal name UNREAD. Bankruptcy: CourtListener shows no Judiciary Plaza LLC docket (not proof — PACER unchecked); the sale proceeding argues against a stay.
- **Moves nothing:** no CREED band, score, trigger or prediction (as pre-registered). CASE-CREED-139 → `REO` event added (SECONDARY). No route owed (§4).
- **Open:** the bid amount and form; whether the Georgetown Co. conversion proceeds with the lender. Re-check Connect CRE / Bisnow DC ~10/29–10/30.
