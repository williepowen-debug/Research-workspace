# EGBN follow-up: can the Fairfax office maturity outcome be seen publicly? (2026-09-27)

**Scope (one line):** whether and how the outcome of EGBN's four criticized loans over $10M due 8/10–9/30/2026 (the Fairfax office plus three others) can be observed publicly, and the Q3 test card for them. Nothing wider. No score, threshold, tool or trade change.
**Asked by:** PROME task relaying Will 17:57 ET. Builds on the news sweep (`reports/2026-09-27_news_sweep_EGBN_VLY_PFBC.md`, f97e56783): **EDGAR is settled, there has been no 8-K since the 7/22 release**, and I do not repeat that check here.

## Step 1 answer
**Not observable now.** The gate is **identification**: EGBN's deck names the loan only as "Office, CRE, Fairfax" with a balance, maturity, LTV, appraisal and DSCR. There is no address, borrower, property name or tax-map number. Every public record channel (land records, trustee-sale notices, courts) is keyed on property or party, so **none of them can be searched for this loan without first identifying the property.** Identifying it needs a lender-name search of Fairfax land records, which is a **paid, human-account step**. The definitive channel is **EGBN's own Q3 deck (~10/21, estimate)**, which reprints this table.

---

## A. OBSERVED

| # | Fact | Source |
|---|---|---|
| A1 | The loan: **Office · CRE · Fairfax · $22,072K · matures 9/25/2026 · LTV 96% · appraised $23,000K on 4/2/2026 · DSCR 0.74 (as of 3/31/26) · accruing · substandard.** No other identifier. | EGBN Q2-26 deck, "All Special Mention and Substandard Loans Over $10 million", slide 25 (8-K acc 0001050441-26-000088), fetched from EDGAR 9/27 |
| A2 | **The deck marks later outcomes itself.** Footnote 5 reads "Paid-off in full post 06/30/2026 quarter close". In Q2 it flags a $35.4M DC apartment loan. ⇒ **EGBN's Q3 deck will show this loan's outcome in the same table**: gone with a payoff footnote, an extended maturity date, or moved to nonaccrual / OREO. | Same slide |
| A3 | **A second, separate Fairfax office credit is already nonaccrual:** $18,502K, matured **2/28/2026**, LTV 76%, appraised $24.3M (9/5/2025), nonaccrual. It is 16.7% of EGBN's nonaccruals ("Office – Fairfax $18.5M"). ⇒ One Fairfax office loan has already failed at maturity. That is context for this one, **not evidence about it.** | Same deck, slide 25 and NAL-by-loan table |
| A4 | Three other criticized >$10M loans came due in the same window: **storage, Montgomery $56.2M (8/10, SM, DSCR 0.93)** · **apartments, Prince George's $56.0M (8/21, already extended from 4/21, SS, 88% LTV, DSCR 0.63)** · **storage, Anne Arundel $15.0M (9/30, SS, DSCR 0.26, appraisal 6/13/2022)**. None is identified by address. | Same slide |
| A5 | No press or public-notice hit for an EagleBank Fairfax office foreclosure, trustee sale or default (web search 9/27). | WebSearch 9/27 (source list below) |
| A6 | Fairfax land records (deeds of trust, modifications, certificates of satisfaction, substitute-trustee appointments, trustee's deeds) are searchable **by grantor/grantee, address or tax map** only through **CPAN**: a subscription service at **$150 per user per quarter**, on Chrome or Edge. Free alternative: the Land Records Research Room in person at the Fairfax courthouse. | fairfaxcounty.gov Circuit Court / CPAN pages |

## B. CHANNELS

| Channel | Class | Why / when | Needs Will's hands? |
|---|---|---|---|
| **EGBN Q3 earnings deck, same >$10M table** | **OBSERVABLE-LATER: ~10/21 (estimate; not announced)** | Definitive. It shows payoff (footnote 5), extension (new maturity), downgrade, nonaccrual or OREO. | No |
| EGBN Q3 10-Q | OBSERVABLE-LATER, ~early Nov | Office reserve and criticized tables by collateral. Confirms the deck. | No |
| EDGAR 8-K | Settled: nothing through 9/27 | A single $22M loan is below materiality. **An 8-K for this loan alone is unlikely.** | No |
| **Fairfax County land records (CPAN)** | **NOT OBSERVABLE without identification → OBSERVABLE-NOW with a subscription** | A grantee search on "EagleBank" returns its recorded deeds of trust. Filtering to office parcels with a DOT near $22–25M should find the loan. Then any **modification/extension, certificate of satisfaction (payoff), substitute trustee or trustee's deed** shows. ⚠️ Modifications are **not always recorded**, so no modification recorded ≠ not extended. Recording also lags. | **YES: a $150/quarter CPAN subscription (account and payment), or an in-person visit to the Research Room** |
| Virginia trustee-sale notices (non-judicial foreclosure is advertised in a newspaper, e.g. the Washington Times "Foreclosure Sales FFX Cty" classifieds) | **OBSERVABLE-LATER, only if EGBN forecloses** | Notices usually run weeks before a sale, which follows default, which follows maturity. **A sale notice two days after maturity is not expected.** Notices name the property and trustee, often not the lender, so they need identification too. | No (free to read), but only useful once the property is known |
| Fairfax County tax assessment (free) | **Partial**: candidates, not identification | It can list office parcels assessed near ~$23M, but it does not link to a lender. Assessment ≠ appraisal. | No, but low value without land records |
| Courts (a lender suit on a guaranty, a borrower bankruptcy) | OBSERVABLE-LATER, event-dependent | Only if a dispute arises. Searchable by party once the borrower is known. | No (DEWEY's `recap_pull.py` covers federal dockets) |
| Press (Washington Business Journal, Bisnow, CoStar) | Opportunistic | A $22M suburban office loan rarely makes news unless it is a note sale or foreclosure. | Paywalls (WBJ/CoStar) |

## C. ASSUMPTIONS
- EGBN's Q3 deck **keeps the same table format**, with its footnote-5 payoff flag. It has done so in Q1 and Q2, but that is not guaranteed.
- A CPAN "EagleBank" grantee search can isolate the loan. That assumes the DOT was recorded to "EagleBank" (not a participant or trust), and that its face amount is near the balance. A loan that amortized, was refinanced or was upsized would miss a narrow filter.

## D. UNKNOWNS
1. **The property's identity**: address, borrower, whether EGBN holds all of it or participations.
2. **The outcome at 9/25**: payoff, extension (EGBN extended the Prince George's loan once already, 4/21 → 8/21), a forbearance, or default. **None is observable today.**
3. **The same question for the three other loans** in A4. Two of them (8/10, 8/21) are already a month past maturity with no disclosure, so silence is **consistent with extension or modification, not evidence of payoff.**

## E. Next observation, and which way it moves
| Observation | When | Direction |
|---|---|---|
| Q3 deck shows the Fairfax loan **gone with the payoff footnote** | ~10/21 (est.) | **Weakens** EGBN office severity; supports "cleanup mostly done" |
| Q3 deck shows it **extended** (new maturity, still substandard) | ~10/21 | Neutral to adverse: loss deferred, not avoided; the stale-appraisal leg stays live |
| Q3 deck shows it **nonaccrual / charged down / OREO** | ~10/21 | **Strengthens** the office stress leg; a second Fairfax office loan failing at maturity after A3 |
| Any of the 4 moved to nonaccrual together, alongside a new-CEO reserve build (news-sweep addendum) | ~10/21 | Supports the **"kitchen-sink" hypothesis**: severity overstates the quarter's actual deterioration |

**Stop point:** I have not attempted identification, since it needs CPAN or an in-person visit, and I have not widened to other EGBN loans. **Will's call:** buy a CPAN quarter ($150) or have someone visit the Research Room, or wait for the Q3 deck. **My recommendation is to wait.** The Q3 deck is ~3 weeks out, free and definitive. Land records would give a few weeks' lead and might still miss an unrecorded extension.

**Sources:** EGBN Q2-26 deck https://www.sec.gov/Archives/edgar/data/1050441/000105044126000088/final-2q2026egbnearnings.htm · Fairfax CPAN https://www.fairfaxcounty.gov/circuit/online-services/court-public-access-network · Land-records research https://www.fairfaxcounty.gov/circuit/land-records/research · Land records FAQ https://www.fairfaxcounty.gov/circuit/land-records/land-records-faq · Washington Times Fairfax foreclosure classifieds (example) http://classified.washingtontimes.com/category/358/Foreclosure-Sales-FFX-Cty/listings/160284/00104481.html
