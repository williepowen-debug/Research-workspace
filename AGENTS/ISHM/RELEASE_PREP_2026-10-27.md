# ISHM — October 27, 2026 release plan

Prepared October 26, before either release. **No October 27 actual or forecast is asserted.** Recheck the issuer schedule and release dateline at the next boot. Current desk evidence: research/2026-10-26_first-session/REPORT.md. Data ledger: workbook/PRINTS.tsv. Mechanism tests: workbook/EXIT_PROTOCOL.md.

## 08:30 ET — September advance durable goods

[Primary Census schedule](https://www.census.gov/manufacturing/m3/release_schedule.html) and [August advance report](https://www.census.gov/manufacturing/m3/adv/pdf/durgd.pdf) both confirm October 27 at 08:30 ET. [Advance PDF endpoint](https://www.census.gov/manufacturing/m3/adv/pdf/durgd.pdf) is mutable: archive the September PDF before later releases overwrite it. Full September M3 successor: November 3 at 10:00 ET.

| Read first | Latest comparable August baseline, full report October 2 | Required comparison |
|---|---:|---|
| Total durable orders | $338.458B; −0.1% m/m | Separate aircraft, defense and ex-transportation before interpreting headline |
| Nondefense capital-goods orders excluding aircraft | $87.640B; +1.6% m/m; July $86.295B | September versus **revised August in the new release**, with prior-vintage revision shown separately |
| Core shipments, same exclusion | $84.960B; +0.5% m/m; July $84.506B | Orders without shipments are a pipeline, not delivered real equipment |
| Computers/electronic-products new orders | $30.868B vs July $30.873B | Broad category; includes items other than AI equipment |
| Electrical equipment/appliances/components new orders | $19.020B vs July $18.822B, +1.1% m/m | Do not label the broad category “grid orders”; WATT owns grid attribution |
| Computers/electronics shipments | $34.233B vs July $34.230B | Domestic factory production/shipments differ from imported servers |
| Electrical/appliances/components shipments | $18.686B vs July $18.538B | Keep shipments and orders separate |

All table values are **nominal, seasonally adjusted USD**, August reference month, revised October 2 except full-report first observations. Source: [full M3](https://www.census.gov/manufacturing/m3/prel/pdf/s-i-o.pdf), Tables 1/2 and Table 5 p10; frozen extracts in research/2026-10-26_first-session/sources/m3_tables.txt. Advance August core shipments **$84.998B, +0.6%** and orders **$87.629B** are historical, not the current baseline. Never compare September first print with an unlabeled old advance baseline.

1. ISHM verifies September reference month and October 27 publication date on the issuer PDF.
2. ISHM saves the release and retrieval clock, with source URL and hash.
3. ISHM records the new release's August revisions beside the October 2 baseline.
4. ISHM records September orders and shipments, ex-transportation, defense/aircraft, computers and electrical categories.
5. ISHM writes ADVANCE rows with successor November 3. ISHM preserves earlier vintages.
6. ISHM updates VX-ISH-03, R1 evidence and the short release synthesis.
7. ISHM delivers the domestic J1 result to VULCAN with the import/BEA limits intact.
8. ISHM routes a material cycle consequence to HENRY/CARL; bank/hiring consequences follow their named owners.

**Interpretation:** a headline driven by aircraft/defense is not broad private-equipment demand. Core strength alongside shipments supports actual equipment buying; nominal growth still requires price/mix caution. A core miss alone does not invalidate imported GPU/server capex. A one-month decline is not the proposed two-month contraction band. No new threshold or prediction is authorized here.

**J1 completion clocks:** October 29 08:30 ET BEA Q3 advance, real equipment and information-processing investment; November 4 08:30 ET FT-900 September computer/accessory imports. August imports were $59.356B versus $61.392B July, SA nominal (Exhibit 8, October 6 release). Quarter-match July–September M3/import aggregates to Q3 BEA; never join a September monthly rate to Q2 annualized GDP as if contemporaneous. Preserve any BEA revisions and price basis. Imported content cannot be read as a domestic M3 share.

**Recovered BEA comparison baseline:** Q2 2026 real equipment +13.4%, information processing +7.6%, computers −6.7% q/q SAAR, September 30 revised vintage. Table 5.3.1 lines 9/10/11 in the saved Section 5 workbook; `data/EQUIPMENT_QUARTERLY.tsv` preserves history. Use the Q2 revision in the October 29 release when comparing Q3. This baseline does not complete the current-quarter test.

## 10:00–10:10 ET — October Richmond manufacturing survey

[Primary Richmond schedule](https://www.richmondfed.org/region_communities/regional_data_analysis/business_surveys/about) confirms the **10-minute release window**. Do not declare a missed release at 10:00. [Current survey page](https://www.richmondfed.org/region_communities/regional_data_analysis/business_surveys/manufacturing); [September primary PDF](https://www.richmondfed.org/-/media/RichmondFedOrg/region_communities/regional_data_analysis/regional_economy/surveys_of_business_conditions/manufacturing/2026/pdf/mfg_09_22_26.pdf).

| September baseline, released September 22; SA diffusion points | Value | October question |
|---|---:|---|
| Composite | −2 | Does activity rejoin the positive regions? |
| New orders | −6 | Does order breadth recover above zero or deteriorate further? |
| Shipments | −5 | Does production/delivery evidence agree with orders? |
| Employment | +7 | Does hiring remain positive despite order weakness? |

1. ISHM verifies October reference month and records any September revision.
2. ISHM separates current orders/shipments from six-month expectations and price-growth measures.
3. ISHM records the composite and all three components in PRINTS notes and the synthesis.
4. ISHM compares October new orders with NY 23.2, Philadelphia 4.3, Kansas City 3 and Dallas 9.3 SA diffusion points. The saved panel is currently 4/5 with its aggregate UNKNOWN. Record Richmond and any revisions in a new dated vintage before reporting full October breadth; do not overwrite the October 26 snapshot. ISHM does not average unlike headline indexes.
5. ISHM re-dates the consumed catalyst to November 24, preserving 10:00–10:10 ET.
6. ISHM routes labor/price consequences to LABOR/CARL and material cycle changes to the remaining consequence owners.

A single Richmond recovery is counterevidence to a universal regional slowdown, not proof of national end-demand. Further negative orders/shipments strengthens caution, but is not an ISM <47 trigger. Proposed regional bands remain unregistered.

## End-of-release closeout

Reconcile both clocks, revisions and source bases. Keep October S&P flash provisional until its November 2 final successor (date currently secondary). Update PRINTS, VX, FLOW only where evidence changes, catalysts and STATUS. Deliver packets through the recipient inboxes with explicit path commits. Fold NEXUS_BRIEF last, pinned to the final STATUS commit. Report any source failure as CANNOT-FIRE for the dependent test; continue independent release work. Do not claim consumption from a delivered file alone.
