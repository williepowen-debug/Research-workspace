# CORAL recent work — bounded CATO review, November 17, 2026

## Current assessment

Keep the research and the unchanged bank-transmission assessment; correct the conclusions that outrun it. The housing calculations support no new aggregate relative deterioration in financed condo closings through October, not an identified cause of the earlier decline. The fiscal/flood analysis usefully separates tax-funded services from fee-funded drainage, but permission to pay debt is not assurance of repayment. Correct the timing and retain the limits of the rating-action search in the summaries. No broad rerun, score change, new study or forced trade thesis is warranted by this review.

Will asked CATO to check and review CORAL's recent work. This is independent review of CORAL's implementation and research, not owner repair. No CORAL file edited; no packet, notification or agent launch authorized or performed. Findings below are delivered as recommendations to Will; owner adoption is unknown. CATO's review is complete; next boot orient and await Will.

## Scope and evidence

Initial checkout `07af5aaac47c27ea66a26e5260e634df5fb1b774`; CORAL work reviewed: morning `aa2ee5f29d` (financing research and CORAL-02), evening `e18a9fa73a` (tax/flood report), consumer refresh `49dfc56c0a`. Read both November 17 research reports, the full 37-month TSV, relevant STATUS/NEXUS_BRIEF and STATUS_DETAIL sections, owner identity/inference rules, prior CATO S17-2 disposition, and recent commit scope. At the later check HEAD was `24f827eb9e`; the two research reports, TSV, STATUS and NEXUS_BRIEF had no diff from the initial snapshot. Concurrent VULCAN, WALTER, PROME and routed inbox work was preserved, including others' staged renames. This review does not certify later commits.

External checks on November 17:

- [Florida Realtors October condo summary](https://www.floridarealtors.org/sites/default/files/2026-11/October-2026-Fla-condo-summary.pdf) and [single-family summary](https://www.floridarealtors.org/sites/default/files/2026-11/October-2026-Fla-single-family-summary.pdf): checked current/prior closed and cash counts, price/list realization and contract days. Condo 6,862 minus 3,596 = 3,266 financed versus 3,563; single-family 19,049 minus 5,547 = 13,502 versus 15,419. Independently calculated changes −8.3357% and −12.4327%, gap +4.0970 points: CORAL's reported FALSE arithmetic stands. No new prediction grading rule applied.
- Independently recomputed every closed-minus-cash row and the report's aggregates from its TSV. Aug–Oct ratios: 25.46899 (2024), 23.33219 (2025), 23.28736 (2026). All four annual totals for each of the three years reproduce; prior 34-month gap has 29 negatives, mean −5.31176, sample SD 4.83690. Oct–Dec 2025 ratio 23.23977. This establishes internal calculation accuracy; the full historical series was not re-extracted from all three publisher editions. Its mixed-vintage/rounded-YoY limits survive.
- [REC July 10 impact estimate](https://edr.state.fl.us/content/conferences/revenueimpact/archives/2026F/_pdf/impact0710.pdf), printed pages 685, 691 and 699: confirmed statewide modeled cash reductions $4,929.5M FY27-28, $8,714.5M FY28-29, recurring $11,834.7M; Palm Bay $22.062426M to $44.464412M; water districts total $89.518409M to $218.049041M. The methodology calculates impacts from changed taxable values and tax rates; these are modeled revenue effects, not enacted spending cuts. CORAL's newer vintage is supported. The press-derived Palm Bay percentage denominator was not independently validated.
- [Enrolled CS/HJR 1F](https://www.flsenate.gov/Session/Bill/2026F/1F/BillText/er/PDF), numbered lines 414–433: local property-tax revenue has specified permitted uses, including existing debt service, infrastructure and flood control. No issuer-specific repayment analysis was performed by CATO.
- [Palm Bay stormwater utility](https://www.palmbayfl.gov/government/city-departments-f-to-z/public-works/stormwater/stormwater-utility): primary confirmation that user fees are placed in a dedicated enterprise fund. [City code, chapter 204](https://codelibrary.amlegal.com/codes/palmbay/latest/palmbay_fl/0-0-0-73866) also permits grants, borrowing and other budgeted revenues: a separate fee fund is not proof of total independence from other funding. CORAL already leaves the actual spending effect unresolved.
- [Florida Revenue bulletin PTO 26-21](https://floridarevenue.com/property/Documents/PTO_BUL_26-21.pdf) acknowledges voter approval; this is not a fresh certification-count verification.

Not independently checked: historical flood levels/forecasts, FEMA declaration and aid records, FDIC deposit-footprint arithmetic, individual insurer/loan exposure, rating-agency inventory, bond spreads, election certification, every press report or the legal effects of every provision. No blocked site was probed. The initial condo-PDF tool error was resolved through the publisher's own report link; it was not an access-block workaround.

## Findings and closure conditions

### CR17-1 — Medium: descriptive housing results become causal conclusions

**OPEN; owner CORAL.** In `research/2026-11-17_WQ704_fl-condo-financing-channel.md:13`, the opening says the earlier break was not specific to financing and assumes a financing squeeze would leave cash buyers standing. Its own inference audit at line 101 correctly admits simultaneous financing pressure and a separate cash-buyer retreat fit the same observations. NEXUS_BRIEF line 26 still points to a condo-wide cost shock. Report line 104 also treats a lower median as a mix shift and improved realization/contract time as excluding clearing through lower prices; aggregate closed-sale statistics do not identify those causes. Lower initial asks and changed composition can coexist with quicker sales and better realization. No new empirical claim that either mechanism actually occurred is made here.

**Consequence:** a supported failure to detect extra deterioration becomes an unsupported exclusion of financing stress. Counting alternative loans as financed and averaging across buildings remain important limits.

**Correction:** carry the report's own narrower inference into its opening, relevant KB/STATUS_DETAIL conclusion and NEXUS brief: no additional statewide relative decline detected through October; the earlier decline affected cash and financed transactions, but its cause is not isolated. Describe price/mix explanations as hypotheses. Keep the primary counts, CORAL-02 FALSE and bank rail unchanged. **Closure:** owner reconciles the active conclusions with these limits; no new data program is needed. Prior CATO S17-2 concerned PROME misnaming this ratio as a share; that supplied-reply correction remains closed and is not reopened.

### CR17-2 — Medium: permitted debt-service spending is used to exclude credit risk

**OPEN; owner CORAL.** `research/2026-11-17_amendment3-and-floods-impact.md:71` and `:162` infer that default risk is not the channel because debt service is protected. The cited amendment permits that expenditure; this does not establish adequate revenue, liquidity, repayment priority or the protection of any particular obligation. CORAL correctly recognizes the same permitted-use-versus-funding distinction for drainage at line 86, but does not apply it to debt service.

**Consequence:** the handoff prematurely closes a financial transmission question without issuer/bond evidence.

**Correction:** state that no default implication has been established by this research; the observed/modelled concern is fiscal pressure on services, reserves and capital. Leave creditor consequences dependent on the issuer's resources and obligation terms. Do not turn this correction into a default forecast. **Closure:** report and current consumer language no longer treat the permitted-use clause as assurance of repayment. Further issuer research is not assigned by CATO.

### CR17-3 — Medium: the summary delays the fiscal horizon and overstates the sequence

**OPEN; owner CORAL.** `STATUS.md:134` calls the cost two years out, then correctly places the first affected fiscal year in October 2027—less than a year from this review. The report's trade line at `:162` predicts a rating/outlook action as the first visible consequence, most likely after September 2027 budgets. No inspected evidence establishes that ordering; budget proposals, capital decisions or financing terms could supply evidence earlier. No claim of observed early repricing is made here.

**Correction:** use the dated FY27-28 revenue horizon, distinct from ongoing flood damage; identify rating action as one possible observation, not a necessary first step or a reason to wait. Replace claims that no budget evidence can exist before adoption with the narrower point that final FY27-28 spending choices were not established. **Closure:** STATUS and the research/handoff align on timing and observation conditions. Existing calendar use suffices; no new cadence required.

### CR17-4 — Low: limited search becomes a categorical absence in consumer prose

**OPEN; owner CORAL.** Report line 71 says no rating action was found in searches and notes agency sites were not directly read; STATUS lines 56/134 and NEXUS_BRIEF line 16 shorten this to no action having occurred. No contrary action was discovered by CATO; the defect is coverage, not a proven missed downgrade.

**Correction/closure:** retain “no action found in the sources searched as of the read” in current summaries. No agency-wide audit is required. Also retain “property-tax base” when using Palm Bay's press-derived 66% figure; it is not a share of the city's entire budget.

## Direction and stop

The most useful new connection is the overlap between flood-exposed places and future municipal revenue pressure, with the separate stormwater funding channel preserved. CORAL appropriately withholds a bank-loss conclusion from deposit geography. Correct CR17-1 through CR17-4 in the existing artifacts, then use existing legislative, budget, flood-aid and housing observations. A declaration of no supported investment implication is acceptable; do not invent a trade just to route one. Any later supported implication goes through the existing owner/TERRY process.

CATO review delivered; owner corrections remain recommendations, adoption unassessed. No new owner assignment, scoring amendment, surveillance program, trade, send or pilot resumption. All existing approvals survive. Benefit demonstrated here is verification of bounded calculations and identification of consequential inference limits, not proof of future decision or trading improvement.

## Delivery checks

Verified existence/readability, then weekday check passed for the five actual inputs: `PROME/DOCKET.tsv`, `PROME/GATES.tsv`, `PROME/WILL_QUEUE.md`, this report and `AGENTS/CATO/CONTINUITY.md`. Optional CATO `workbook/CATALYSTS.tsv`, `CALENDAR.md` and `STATUS.md` do not exist and were omitted. Six-file read-cap check covered `AGENTS/CATO/AGENTS.md`, `CHARTER.md`, `CONTINUITY.md`, root `CLAUDE.md`, `USER.md`, `AGENTS.md`; all below their applicable caps, root CLAUDE has the 75% rotation advisory (24,449 B), not a failure. Continuity diff whitespace check passed. No own STATUS, ledger, auto-memory or superseded numeric claim changed, so the conditional ledger/memory/consumer checks do not apply.

Orphan advisory identified `AGENTS/CORAL/research/2026-11-17_a3_brevard_scenarios_model.py`, newly untracked during this review: owner work, not CATO-authored; untouched and excluded. This new scenario work is outside the reviewed two-report snapshot. At later HEAD `8f0b3a834d`, the reviewed report/STATUS/NEXUS surfaces still have no diff from the initial snapshot. Only this report and CATO continuity belong to the delivery set; staged paths were empty at that check. Safe-push will account for concurrent committed work; the final receipt and carried owners will be reported in chat.
