> ## CORAL provenance header (2026-09-28)
> **What this is:** an external AI (ChatGPT) critique of a separate AI research report, handed to CORAL by Will on 2026-09-28. **Tier: SECONDARY — every claim is a LEAD until CORAL verifies it at a primary.** Stored verbatim below; not edited.
> **Will's instruction the same evening:** one bounded verification pass on the nine claimed condominium-association bankruptcies (case table: debtor, property, filing date, case number, status, documented cause, creditors/amounts/collateral; bank vs private, secured vs unsecured, association borrowing vs unit-owner mortgages; allegations and missing documents marked); Biscayne 21 correction with dated evidence; Fannie channel with its actual eligibility scope; OPPAGA figures with coverage limits. **The association-bankruptcy count stays descriptive and UNGRADED — no window retrofitted.** No scenario-weight or trade changes.
> **Verified by CORAL so far (9/28, before the pass):** Grande Isle Towers I & II (MDFL 26-00951, 4/27/26, $10–50M liabilities) exists on PACER Monitor; Windmill Lakes V and Ocean Five confirmed by press; Biscayne 21 settlement 8/31/26 ~$50M confirmed by The Real Deal / Bisnow. Everything else pending — see `STATUS_DETAIL.md` § K when filed.

---

Worked for 9m 28s  
Yes. I checked the report against current bankruptcy dockets, Fannie Mae guidance, Florida statutes/OPPAGA, SEC filings, Parcl documentation, FLDOE, and the Biscayne 21 litigation. There is useful research here, but I would not feed it into CORAL unchanged. The biggest problems are an incomplete bankruptcy count, an outdated description of Florida’s milestone-inspection law, an incorrect description of Parcl’s seller-stress methodology, and several places where association distress is presented as evidence of bank losses without actually establishing the lender-loss link.

1\. The bankruptcy count should be revised upward  
Your report identifies six association cases.   
 I can independently verify at least nine bankruptcy filings since January 1, 2025 in the Southern and Middle Districts of Florida where the debtor’s actual name contains “Condominium Association.” I say at least because I cannot run the same authenticated, exhaustive PACER party-name query you originally contemplated; this is assembled from court records and PACER-derived public docket services.

Condominium association	Filed	Court / case	Notes  
Green Terrace Condominium Association, Inc.	Apr. 25, 2025	SDFL 9:25-bk-14568-MAM	Ch. 11; petition showed liabilities of \$1M–\$10M.   
Ocean Five Condominium Association, Inc.	May 2, 2025	SDFL 1:25-bk-15015-PDR	Missing from the report. Ch. 11 Subchapter V; plan confirmed Feb. 13, 2026\.   
Sunset Palm Villas Condominium Association, Inc.	Jun. 21, 2025	SDFL 1:25-bk-17036-CLC	Ch. 11; still active in Sept. 2026\.   
Dockside at Ventura Condominium Association, Inc.	Jul. 25, 2025	MDFL 6:25-bk-04636-GER	Ch. 11 Subchapter V; active as of today, Sept. 28\.   
Orlando International Resort Club Condominium Association, Inc.	Oct. 23, 2025	MDFL 6:25-bk-06813-GER	Ch. 11 Subchapter V; liquidation/sale case.   
Palm Greens at Villa Del Ray Recreation Condominium Association, Inc.	Jan. 28, 2026	SDFL 9:26-bk-11060-EPK	Report spells it “Del Rey.” It is a recreation/master association serving two condo communities, rather than a normal individual condo building.   
Grande Isle Towers I & II Condominium Association, Inc.	Apr. 27, 2026	MDFL 2:26-bk-00951-FMR	Missing from report. Petition range: \$10M–\$50M liabilities.   
Windmill Lakes V Condominium Association, Inc.	Jun. 4, 2026	SDFL 0:26-bk-17338-SMG	Missing from report. Ch. 11 Subchapter V.   
The Gardens of Forest Lakes Condominium Association, Inc.	Jun. 19, 2026	MDFL 8:26-bk-05294-RCT	Missing from report. Ch. 11 Subchapter V; \$500K–\$1M asset/liability range.   
So the stale CORAL count of 1 can safely become “≥9 verified strict-name filings since Jan. 1, 2025.”

There is also Star Island Vacation Ownership Association, Inc., but I would keep it outside the strict count. It filed November 6, 2025—not Q1 2026 as the report says—and is a timeshare/vacation-ownership association whose debtor name does not contain “Condominium Association.”   
 If CORAL wants a broader condo/timeshare/HOA distress universe, it becomes a tenth case.

One important interpretation change  
The report says this bankruptcy cluster shows stress “propagating directly” into banks.   
 That conclusion is ahead of the evidence.

Some examples actually cut against assuming a bank-loss channel:

Dockside's identified lender is South Florida Real Estate LLC, alongside contractor SFR Services—not a regulated bank.   
Green Terrace has Boken Lending II LLC identified as a lender.   
Palm Greens' \$43.7M debt burden is heavily associated with litigation/development-agreement disputes; the court describes the debtor as the recreation complex serving two 55+ condo communities.   
Windmill Lakes V followed litigation alleging misappropriation by former property management; its petition showed just \$500K–\$1M of liabilities.   
So I would code these as strong evidence of association financial/operational stress, but not yet evidence of realized bank losses.

There is, however, a very clean mortgage-liquidity transmission channel: Fannie Mae explicitly says a condo project subject to bankruptcy, insolvency, liquidation, or receivership is ineligible.   
 That means an association filing can directly impair owners' conventional mortgage access even before a commercial bank takes a credit loss.

2\. The Fannie Mae section needs several corrections  
The report says Limited Review disappeared and all affected projects must undergo Full Review, and still discusses a 10% reserve minimum. 

The current rule is more nuanced:

Limited Review was retired effective August 3, 2026, but projects now use Full Review or, where eligible, Waiver of Project Review. So “all financed transactions must receive Full Review” is too categorical.   
Under Full Review, Fannie is raising the minimum reserve allocation from 10% to 15%, effective for applications dated January 4, 2027 or later. The report misses this very important upcoming tightening.   
Fannie also tightened the reserve-study route: when a reserve study is used, the budget has to include the highest recommended reserve allocation, and the “baseline funding method” can no longer be used.   
Fannie now offers the Condo Status Finder, which allows an HOA/property manager/authorized adviser to check a particular project's real-time status. It does not expose a bulk downloadable Florida blacklist.   
The 1,438 Florida / 696 tri-county figures are legitimate—but they are a March 2025 snapshot from data obtained by Allcock Marcus, not a current 2026 count.   
 I found no credible new statewide count. Even September 2026 sources still describe 1,438/696 as the “most recent public reporting.” 

So CORAL should store this something like:

Florida Fannie ineligible projects: 1,438 — observation date March 2025 — stale/current value unknown.

That is materially different from treating 1,438 as a current reading.

3\. The milestone-inspection law in the report is outdated  
This is probably the clearest statutory error. The report says that under “Florida Statute 718.1141,” buildings hit the milestone requirement at 30 years, or automatically at 25 years if within three miles of the coast. 

Current Florida law places the milestone-inspection requirement in §553.899. A residential condo/co-op building three stories or more generally receives its first milestone inspection at 30 years. A local enforcement agency may move that to 25 years based on local circumstances, including proximity to salt water. There is no longer an automatic statewide “within three miles \= 25 years” rule. 

That three-mile rule existed in the earlier post-Surfside version of the law, so the other model appears to have mixed an old version with the current statute.

The report's state inspection counts, though, are basically right and can actually be strengthened. OPPAGA's July 2026 audit reports:

8,736 Phase I inspections; 1,575 Phase II inspections; 1,587 extensions; 94% of extensions in coastal jurisdictions; 903 repair permits stemming from Phase II findings; estimated repair values ranging from under \$1,000 to \$30 million; and 30 buildings in 2024 plus 24 in 2025 deemed unsafe or uninhabitable. 

Those last three statistics—903 repair permits, up to \$30M of estimated repair work, and 54 unsafe/uninhabitable buildings—are useful additions for CORAL because they provide much more direct capital-needs telemetry than simply counting inspections.

4\. The bank-exposure section overstates what the disclosures prove  
The report portrays several banks as having “multi-billion-dollar” exposure tied to Florida condo/HOA regimes and then sketches a reserve-drawdown → deposit outflow → NIM pressure mechanism.   
 

That mechanism is plausible, but it should currently be labeled a risk pathway, not an observed development.

In fact, BankUnited's Q2 2026 results emphasized record non-interest-bearing deposits and improved credit quality, not an emerging association-deposit run.   
 Its HOA vertical is a substantial deposit franchise, but “national HOA deposits” should not be described as Florida condo loan exposure.

USCB gives us an interesting additional datapoint. Its June 2026 10-Q shows only \$2.148M of nonaccrual loans across the entire \$2.317B loan portfolio, and its \$68.7M “condo commercial” category had no delinquency/nonaccrual shown in that table.   
 That is not the same thing as association lending, but it is worth knowing because there is currently no obvious public credit deterioration in that disclosure.

I would therefore change CORAL's bank indicator from:

“Condo stress is reaching regional banks”

to something closer to:

“Transmission channel exists; realized association-loan deterioration has not yet been demonstrated in public bank disclosures.”

That makes the upcoming Q3 calls much more valuable: you are looking for the first change in management language, criticized/classified credits, nonaccrual association loans, insurance-financing demand, reserve-loan growth, or HOA deposit runoff, rather than trying to confirm an effect that is already presumed.

5\. The commercial association-loan “rules” are presented too rigidly  
The report calls things like \<10% delinquency, 20–25 minimum units, ≤10% single-owner concentration, and 5–7.5% rates “commercial underwriting guidelines” or mandates. 

Those figures trace largely to industry/vendor guidance, not a uniform regulatory rule. Different banks can underwrite an assessment-backed association loan very differently.

I would keep them, but relabel them as “reported market underwriting heuristics”, not hard bank standards. More importantly, don't mix these with Fannie/Freddie project-eligibility rules for mortgages on individual units; they are two different credit channels.

6\. The Parcl “Motivated Seller Index” description is wrong  
This one is unambiguous. Your report says the seller-stress measure uses price reductions, listing-language terms such as “assessment pending” or “cash only,” and relistings. 

Parcl itself says MSI uses four inputs:

days on market, number/frequency of price cuts, speed/velocity of the cuts, and magnitude of the cuts. 

I found no evidence that the MSI itself parses phrases like “assessment pending” or “cash only.” Relist activity is also a separate metric rather than one of the four MSI components.

There is good news regarding your September 13 scraping concern. Parcl's API changelog shows that the field pct\_inventory\_price\_drop was added to the API in February 2025\.   
 So the underlying price-reduction metric definitely existed by September 13, 2026\.

That does not prove that the particular webpage element CORAL scraped was present or had the same HTML structure on September 13\. So I would record:

Underlying Parcl metric existed: confirmed.  
Exact Sept. 13 web-page field/rendering: unresolved.

7\. Biscayne 21 is substantially right, but the legal characterization needs tightening  
The report says the Florida Supreme Court's October 14, 2025 action “confirmed the appellate ruling as binding precedent.” 

What the Florida Supreme Court actually did was decline to exercise jurisdiction and deny review. It did not issue a merits opinion affirming the Third DCA's reasoning.   
 The practical result is that the Third DCA decision remained undisturbed, but those are legally different statements.

The subsequent development is real and important: by the end of August 2026, Two Roads had reached and funded a settlement with the remaining Biscayne 21 holdouts; reporting puts the aggregate buyout around \$50 million. 

That actually weakens one phrase in the original research request: a Two Roads “win” did not emerge that would establish a more developer-friendly statewide termination rule. Instead, Two Roads ultimately paid the holdouts after losing the appellate fight. So I would not currently model Biscayne 21 as a precedent likely to accelerate forced condo terminations. If anything, the case illustrates how declaration language and holdout rights can make redevelopment more expensive and slower.

What I think CORAL should ingest now  
The biggest useful update is:

Federal bankruptcy signal: ≥9 strict-match Florida condominium-association Chapter 11 filings in SDFL/MDFL since Jan. 1, 2025, versus the desk's stale count of 1\. Four were absent from the other model's report. A tenth, Star Island, belongs only in a broader timeshare/association universe.

But I would attach a caveat:

The bankruptcy cluster is evidence that association stress is real, not yet evidence that it is producing losses at Florida banks. The highest-value next step is creditor-level extraction from these nine dockets: lender name, loan/claim amount, security or assessment pledge, bank vs. private lender, plan treatment, and expected recovery. That would finally build the missing association → lender-loss bridge that your original prompt was actually trying to establish.

I also think the OPPAGA repair data is a worthwhile addition to CORAL: the 903 repair permits and repairs valued as high as \$30M give you a direct measure of the capital burden arising from milestone inspections, rather than an inference from inspection counts alone. 

Finally, there is nothing to pull yet for the October 2026 FLDOE Survey 2\. The official count week is October 5–9, submissions are due October 16, state processing runs October 12–November 6, with final amendment in December.   
 So the other model was right that this remains a future update; the demographic claim in the current report that condo costs are already “prompting families to shift” locations is considerably stronger than the enrollment data support. 

If you'd like, the next thing I would do is go case-by-case through those nine bankruptcies and reconstruct exactly who is owed money and why. That is probably the most valuable missing piece in the entire research package.

