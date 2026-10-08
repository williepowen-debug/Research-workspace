# VLO held-share management review — October 7, 2026

PROME consumer review requested by Will. Evidence retrieved about 13:07 ET, before today's settlement window. This is not a TERRY owner grade, a new trade proposal, a broker reconciliation, or a month ruling. Existing TERRY card: `AGENTS/TERRY/setups/VLO-SHARE_management-proposal_2026-09-28.md` (WQ-330 BOTH).

**Result:** no sell trigger established by this review. The latest completed-session crack estimate is above both registered lines. Policy searches found no qualifying export restriction, but negative-search coverage is bounded. Current broker holding remains UNKNOWN; the review applies to the one-share holding in the existing mirror.

## Price leg A

VERIFIED vendor identities: HOX26.NYM expiry 2026-10-30 and CLX26.NYM expiry 2026-10-20. Both name November 2026. CME's official ULSD settlements page returned product information without settlement rows; source ① unavailable. No continuous futures series substituted.

Raw capture: `evidence.json`, four CSVs, and reproducible `pull.py` alongside this review. Each source-③ window contains all three 14:28, 14:29, 14:30 ET minute bars with positive total volume on both legs. Calculation follows TERRY's prior typical-price convention: sum(((High+Low+Close)/3)*Volume)/sum(Volume), separately per leg; crack = HO×42−CL. Single-vendor ESTIMATE, not an official CME settlement.

| Session | HO VWAP $/gal | CL VWAP $/bbl | Source ③ crack $/bbl | Source ② daily crack | Consumer interpretation |
|---|---:|---:|---:|---:|---|
| Oct 2 | 4.50189059 | 91.14177579 | 97.93763 | 97.93620 | Above both lines; daily row agrees within $0.002 |
| Oct 5 | 4.54420461 | 89.41062402 | 101.44597 | 101.46839 | Above both lines; daily row agrees within $0.023 |
| Oct 6 | 4.56988799 | 89.42952372 | **102.50577** | 102.47479 | Reject source ②: both volumes duplicate Oct 5. Use source ③ ESTIMATE |

Oct 6 volume: HO 1,613 and CL 12,478 contracts in the windows. Daily duplicated volumes: HO 45,682 and CL 274,982. Close-price VWAP sensitivity gives $102.55079, same side of both lines; it is not a second independent source. Oct 6 estimate is $7.35 above the $95 notice line and $12.35 above the $90.16 exit line, well outside the exit's ±$0.15 UNKNOWN band. Oct 7 has no settlement grade at this touch. Data from later sessions never fills an earlier missing observation.

## Policy legs

| Leg | Evidence and coverage | Result |
|---|---|---|
| B1 signed US export restriction | Read October 5 signed White House diesel order and current Presidential Actions index. Federal Register API since Oct 2: diesel export 0, distillate export 0, petroleum product export 0; control query export control 9, unrelated titles. Query URLs and responses saved in evidence.json. | SEARCH-NOT-FOUND for a qualifying restriction. The October 5 order itself is VERIFIED tax deferral/penalty relief, expressly excluded by the existing card; it does not fire B1. No exhaustive claim covering unindexed or newly issued documents. |
| B2 Valero voluntary curb | Valero IR news page returned an unpopulated dynamic list; targeted Valero/SEC web searches found no qualifying announcement. Direct SEC submissions endpoint was inaccessible through web. | SEARCH-NOT-FOUND; completeness UNKNOWN. Cannot certify absence of a Valero commitment from this coverage. No review-triggering announcement established. |
| B3 weekly exports | EIA index lists Oct 7, but linked table7 PDF returned week ending Sep 25 and an imports table without distillate export detail. | Latest distillate exports UNVERIFIED at this touch; no stale figure labelled current. Context only, never an exit trigger. |

Sources accessed October 7:
- [Signed diesel order](https://www.whitehouse.gov/presidential-actions/2026/10/emergency-tax-relief-on-diesel-fuel/)
- [Presidential Actions](https://www.whitehouse.gov/presidential-actions/)
- [Federal Register API](https://www.federalregister.gov/api/v1/documents.json) — exact parameterized URLs saved locally.
- [Valero IR news](https://investorvalero.com/news/default.aspx)
- [Valero Q3 earnings announcement](https://investorvalero.com/news/news-details/2026/Valero-Energy-Corporation-to-Announce-Third-Quarter-2026-Earnings-Results-on-October-22-2026/default.aspx): October 22, beyond the current price-leg expiry.
- [CME ULSD settlements](https://www.cmegroup.com/markets/energy/refined-products/heating-oil.settlements.html)
- [EIA weekly report](https://www.eia.gov/petroleum/supply/weekly/) / [returned table](https://www.eia.gov/petroleum/supply/weekly/pdf/table7.pdf)

## Overdue month decision — WQ-252 / DOCKET L471

**Still PENDING.** November governs through October 14. Without Will's ruling, A becomes SUSPENDED/UNKNOWN after that date; policy leg B continues. The overdue gate review date is not cleared by this consumer price check. No gate state, threshold, review date or owner grade changed. Both staged additional shares remain stood down under the separate terminal scale gate.

DAEDALUS's options memo WAS delivered October 1, despite DOCKET L472 still saying PENDING: `PROME/inbox/processed/2026-10-01_from-DAEDALUS_WQ-252-crack-contract-month-options-memo.md`. HENRY supplied its response October 2: `PROME/inbox/processed/2026-10-02_from-HENRY_WQ-252-step-measurements-and-calibration-pair.md`. The memo's missing-HENRY caveat is superseded by that response. A TERRY month-consequence delivery was SEARCH-NOT-FOUND in the processed TERRY packets and setup references checked; this is not a fleet-wide absence certification.

| Option from DAEDALUS | Practical consequence |
|---|---|
| A: December fixed from Oct 15 | One switch; later-month margin typically lower, bringing readings closer to the exit without a same-month deterioration. |
| A′: schedule by earlier leg expiry | November through Oct 19; December Oct 20–Nov 19. Extending November beyond Oct 14 needs Will's ruling. |
| B: add a frozen Nov−Dec adjustment to December | Removes the visible switch jump but grades a constructed series; adjustment depends on the chosen date. |
| C: persistence or wider separation | Changes when an exit can fire; persistence does not remove the month step. No new threshold proposed here. |
| D with A/A′: ±2-session roll window | One-month-only crossings are recorded without firing/unfiring during the window; can delay a real exit. |

DAEDALUS design preference: A′+D, not adopted. September single-vendor measurements: Nov−Dec median $4.72, range −$0.03 to $7.24; the two registered thresholds are $4.84 apart. HENRY replicated these figures using the SAME vendor, not independent confirmation. **HENRY withdrew its claim that the original $90.16 calibration was verified as a matched pair: July 23 heating-oil contract identity is UNKNOWN.** That uncertainty is material to transporting the threshold and remains unresolved under every option. These historical step figures are not current prices.

PROME disposition: current evidence supplies no new exit instruction. Keep the existing letter in force through Oct 14; prepare the WQ-252 ruling with TERRY's consequence read and the above calibration caveat before extending or replacing the month basis. No automatic monitoring exists; TERRY owns recommendation/grade and Will owns execution. This review is complete as a bounded consumer check; the owner grade, B2 coverage, broker reconciliation and month ruling remain open.
