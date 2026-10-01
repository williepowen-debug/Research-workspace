# Florida OIR Affiliated Fee Analysis (RRC) — does the "not fair & reasonable" verdict predict failure?

Built 2026-10-01 for CORAL. Source text is `rrc.txt`, the PDF converted to text with 11,894 lines. The PDF is https://www.propertyinsurancecoveragelaw.com/wp-content/uploads/2026/09/florida-affiliated-fee-analysis.pdf, published by the Sun Sentinel/Orlando Sentinel on 2026-09-25. All `Lnnnn` citations are line numbers in rrc.txt. Every dollar figure covers the 3-year total for 2017–2019 and comes from the report unless marked otherwise.

## 0. Document structure (read this first — it changes the test)

| Part | rrc.txt lines | Memo date | Companies | Threshold for "presumed NOT fair & reasonable" |
|---|---|---|---|---|
| Executive summary | L1–L455 | 2022-03-31 (L16–18) | 57 selected, 4 not reviewed, 53 reviewed (L44–50) | — |
| Phase 1 | L463–L3636 | **2021-03-31** (L474) | 16 | Affiliate net income > greater of $2M/yr or **15%** of insurer net income (L690–694). The F&R band is 10% (L670–674). |
| Phase 2 | L3637–L7149 | 2022-03-31 (L3652) | 18 (2 not reviewed) | Greater of $2M/yr or **115%** (L3870–3874). The F&R band is 110% (L3850–3854). |
| Phase 3 | L7150–L9066 | 2022-03-31 (L7165) | 11 (2 not reviewed) | Same 110%/115% test (L7364–7385) |
| Phase 4 | L9067–end | 2022-03-31 (L9082) | 12 (all national groups) | Same 115% test (L9300–9302) |

- The phase counts add up: 16+18+11+12 = 57. The four not reviewed are Centauri (L5182–5190), Journey (L5549–5555), Capitol Preferred (L7599–7616) and **Southern Fidelity** (L9035–9049).
- **The Phase-1 memo is dated 2021-03-31.** That is before every liquidation in this sample (the first was Gulfstream on 2021-07-28). So the 16 Phase-1 verdicts are a true ex-ante call. Phases 2–4 are dated 2022-03-31, after Gulfstream, St. Johns and Avatar had already failed. The summary's "Three (3)… liquidated in 2021 or 2022" (L50) matches exactly those three: Gulfstream, St. Johns and Avatar.
- The report **never labels individual companies "single-state" or "national"**. The category column below is my inference: Phase 4 plus subsidiaries of national or foreign groups are marked "national". Treat it as unverified.
- The thresholds are inconsistent across phases: 15% in Phase 1 against 115% later. When insurer net income is ≤0, both tests collapse to the same $2M/yr floor, so any affiliate earning more than $6M over three years triggers "NOT".

## 1. TASK 1 — Verdict table (all 53 reviewed + 4 not reviewed)

Verdict key:
- **NOT**: the text says "presumed not to be fair and reasonable".
- **NOT\***: the text says "not presumed to be fair and reasonable" after stating the threshold was exceeded. The wording is ambiguous, but the context puts it in the NOT bucket.
- **F&R**: the text says "presumed to be fair and reasonable".
- **UND**: the text explicitly says it was unable to reach a conclusion.
- **NV**: the text gives no explicit verdict.
- **NR**: not reviewed.

Abbreviations: NI = net income (3-yr total); CC = capital contributions; Fgv = fees forgiven/waived; BP/EM = business-plan review / enhanced monitoring.

**Affiliated fee % of gross written premium (GWP), 2017/18/19:** these figures were parsed from the PDF text, where table columns are sometimes scrambled. Treat them as approximate.

### Phase 1 (memo 2021-03-31)

| § | Company (abbr) | Cat. | Verdict | Operative text (line) | Aff fee % GWP | Insurer NI | Affiliate NI | CC / Fgv | BP/EM rec |
|---|---|---|---|---|---|---|---|---|---|
| III.1 | Avatar P&C Ins Co (APCIC) | single | **NOT** | "fees paid to affiliates are presumed not to be fair and reasonable" (L1101–1109) | 17.7/15.7/16.5 | −$25M (L1083) | >$19M (L1085, L1097) | $10.7M CC+Fgv | No (refile agreements) |
| III.3 (+III.9) | FedNat Ins Co (FIC) + Monarch National (MNIC); also the Louisiana affiliate Maison (MIC) | single | **NOT** (group) | "presumed not to be fair and reasonable…FIC, MNIC and MIC" (L1411–1415) | FIC ~8.5–10.4; MNIC ~7.2–10.7; Maison ~24.9–27.6 (fees distorted by waivers, L1174–1178) | FIC+MIC −$42.0M (L1377–1379); MNIC lost money every year (L1373–1375) | $79.4M (L1403–1405) | ~$90M CC/Fgv/surplus notes (L1361–1365, L1395) | No |
| III.4 | First Protective Ins Co (FPIC, Frontline) | single | **NOT\*** | "are not presumed to be fair and reasonable" (L1605–1607) after threshold exceeded (L1603) | ~29–34 | −$8.0M (L1567–1569) | $10.7M (L1569–1571) | $15M CC 2019 (L1587) | Limited-scope exam suggested (L1615) |
| III.5 (+III.6) | Florida Family Ins Co (FFIC) + Florida Family Home (FFHIC) | single | **NOT** (group) | "presumed not to be fair and reasonable" (L1923) | FFIC ~20–25; FFHIC ~20–25 | −$3.7M (L1807–1809) | FFIS $12.6M (L1809–1811) | None (L1663–1665) | No |
| III.7 (+III.2) | Florida Peninsula Ins Co (FPIC) + Edison Ins Co (EIC) | single | **NOT** (group) | "the fees are presumed not to be fair and reasonable" (L2261–2263) | FPIC ~33.8–35.4; EIC ~30.4–33.1 | −$12.0M (L2222–2224) | FPM+FPCS $93.9M (L2236–2238) | EIC CC $18.2M; also a $10M dividend in a loss year (L2058–2060, L2210) | No |
| III.8 | Gulfstream P&C Ins Co (GPCIC) | single | **NOT** | "accordingly those fees are presumed not to be fair and reasonable" (L2439–2443) | ~26.5–28.6 | −$14.4M (L2411–2413) | GMGA $1.1M after waiving $4.3M of fees; $5.4M before the waiver (L2415–2419) | $11M CC + $4.3M Fgv (L2328, L2421) | No |
| III.10 | Olympus Ins Co (OIC) | single | **F&R (conditional)** | "would be presumed to be fair and reasonable. However, without the 'Claims Administration' adjustment… impaired" (L2631–2645) | ~25.1 | +$3.6M (L2627–2629) | Parent +$5.8M | $56M "Contributions Administration" from the MGA, acting like a fee waiver (L2605–2617) | **Yes**. The Phase-1 table says "Review Business Model" (L836, L850-area) |
| III.11 | Safepoint Ins Co (SIC) | single | **NOT** | "presumed not to be fair and reasonable" (L2829–2833) | ~22.5–28.1 | −$22.1M (L2760–2762) | Holding company SHI +~$0.5M; SMGA equity $5.2M | $23.25M CC+Fgv (L2689) | **Yes**: "detailed review of the overall business model"; possible unsound condition (L2845–2853) |
| III.12 | St. Johns Ins Co (SJIC) | single | **NV** | "Before reaching a conclusion… consider performing a target examination" (L3036–3042) | ~27.2–28.1 | −$37.4M (L3014–3016) | SJMGA $12.9M (L2929–2931); St. James fees >$40M (L3034) | $39M CC/Fgv (L2937) | Target exam |
| III.13 (+III.14, III.15) | Tower Hill Preferred (THPIC), Prime (THPrime), Signature (THSIC) | single | **NOT** (group) | "presumed not to be fair and reasonable" (L3415–3417) | THPIC ~30–32; Prime ~21–28; Sig ~30–33 | Combined +$3.5M. THPIC −$4.7M, Prime ~+$3M, Sig +$5M (L3173–3179) | >$120M (L3181–3183) | $62.2M CC (Prime, Sig) (L3183–3185) | No |
| III.16 | Weston Ins Co (WIC) | single | **NV** | Defers to the RBC Plan under new owner HSCM (L3621–3631) | ~27.1–27.7 | ≈+$0.17M (+$66k / −$1.3M / +$1.4M; L3498–3500) | WIM ~+$3.2M | None. The $9.0M "receivable" from its MGA overstated surplus (L3611–3615) | No (RBC plan) |

### Phase 2 (memo 2022-03-31)

Section numbers: the table of contents (L4044–4188) and the section bodies number these differently. Both are given here as TOC/body.

| § (TOC/body) | Company | Cat. | Verdict | Operative text (line) | Aff fee % GWP | Insurer NI | Affiliate NI | CC / Fgv | BP/EM rec |
|---|---|---|---|---|---|---|---|---|---|
| III.1 (+III.14/III.12) | American Coastal (ACIC) + **United P&C (UPC)**, parent UIHC | single? (UIHC is Florida-based and public) | **NV (conditional)** | "If the affiliates…reported a combined net income…the Office should consider reviewing existing agreements" (L4452–4456) | ACIC 24.2/27.8/36.1; UPC 26.3/26.0/16.4 | ACIC +$21.2M (L4372–4373); UPC **−$51.2M** (L4446) | Not provided | UPC CC $66M (L4309–4310); ACIC paid $99M in dividends (L4298–4300) | The TOC row aligned to "United P&C" reads "Review Business Model, Enhanced Monitoring" (L4164–4166). **This alignment was reconstructed from scrambled PDF columns and is unverified.** The body recommends only reviewing agreements. |
| III.2 | American Integrity Ins Co (AIIC) | single | **NOT** | "This level of fees is presumed not to be fair and reasonable" (L4657–4667) | 28.4/20.8/21.8 | **+$7.2M** (L4635–4637) | $17.4M (L4639) | $38.35M MGA Fgv in 2019; without it, a material 2019 loss (L4543, L4651–4653) | No |
| III.3 (+III.16/III.14) | American Platinum (APPCIC) + **Universal P&C (UPCIC, UVE)** | single | **NOT** (group) | "presumed not to be fair and reasonable…APPCIC and UPCIC" (L4910–4914) | APPCIC 12.8/15.3/9.0; UPCIC 19.8/20.9/16.2 | Combined −$11.1M; UPCIC +$40M in 2017–18 and −$50M in 2019 (L4882–4888) | ERA $166M (L4888) | $30M CC; UPCIC paid a $30M dividend (L4892–4894) | No |
| III.4 | American Traditions (ATIC) | single | **UND** | "the Office is unable to reach a conclusion" (L5159–5163). The company declined to provide MGA financials. | 30.0/20.6/11.5 | −$3.9M (L5131–5133) | Not provided | >$13M commissions forgiven (L5155–5157) | No |
| III.5 | Centauri Specialty | — | **NR** | Not reviewed after the 2021 change of control (L5182–5190) | — | — | — | — | — |
| III.6/III.5 | Granada Ins Co | single | **NOT\*** | "are not presumed to be fair and reasonable" (L5314–5318) | 22.5 flat | **+$6.2M** (L5304) | $14.6M (L5306) | $2.9M CC (L5254) | No |
| III.7/III.6 | Heritage P&C (HPCIC) | single | **NOT** | "presumed not to be fair and reasonable" (L5531–5537) | 40.8/48.1/29.8 | **−$80.9M** (L5519–5521) | $174.3M (L5523) | $41.1M CC (L5521–5523) | No |
| III.8/III.7 | Journey Ins Co | — | **NR** | Began operating in 2019 (L5549–5555) | — | — | — | — | — |
| III.9/III.7 | People's Trust (PTIC) | single | **NV** | No presumption stated. The company itself "determined that the commissions exceeded a fair and reasonable rate" (L5769–5777). | 47.9/62.7/61.5 | +$22.5M (L5750–5752). Without fee waivers it would have lost money every year (L5754–5756). | $6.9M | $53M commission reductions (L5670–5672) | No |
| III.10/III.8 | Safe Harbor Ins Co | single | **NOT** | "presumed not to be fair and reasonable" (L5973–5981), computed jointly with US Coastal | 28.5/28.1/25.5 | −$2.1M (L5895–5897) | CCGIA+Harbor $9.9M (joint with USCPCIC) (L5905–5909) | None | No |
| III.11/III.9 | SafePort Ins Co (IAT) | national? | **NV** | Four info/consistency requests only (L6160–6194) | ~0.6–0.8 | −$2.6M (L6148–6150) | BAIS/Bay Area Claims "positive" | None | The TOC says "Review Current Business Model" (L4152); the body does not |
| III.12/III.10 | Security First (SFIC) | single | **NOT** | "presumed not to be fair and reasonable" (L6343–6347) | 27.2/30.2/32.2 | −$26.8M (L6329–6331) | >$50M (L6333–6335) | $35M CC (L6260–6262) | No |
| III.13/III.11 | Southern Oak (SOIC) | single | **NOT** | "presumed not to be fair and reasonable" (L6522–6526) | 26.6–26.7 | −$13.2M (L6498–6502) | >$25M (L6502) | None (L6429–6431) | No |
| III.15/III.13 | Universal Ins Co of North America (UICNA; Puerto Rico parent UGI) | national? | **NV** | "consider meeting…long-term viability of the current business plan…enhanced monitoring" (L6718–6722) | 23.2/24.0/25.0 | −$6.1M (L6694–6696) | **−$25.8M** (L6698–6700) | $9M CC (L6635–6637) | **Yes** |
| III.17/III.15 | US Coastal P&C (USCPCIC) | single | **NOT** (by cross-reference) | "See Safe Harbor recommendation 3" (L6881). Rec. 3 explicitly includes USCPCIC (L5973–5981). | 12.4/7.8/18.5 (understated by fee adjustments, L6855–6857) | −$3.1M (L6853–6855) | Joint $9.9M | $6.4M CC/surplus notes + $2.2M fee adjustments (L6786–6790) | No |
| III.18/III.16 | Vault Reciprocal Exchange (VRE; Allied World/Fairfax → Hudson) | national? | **NV** | "requesting additional information…to further assess" + BP/EM (L7132–7142) | ~22.7–23.4 | −$6.5M (L7126) | Not provided | None | **Yes** |

### Phase 3 (memo 2022-03-31)

| § | Company | Cat. | Verdict | Operative text (line) | Aff fee % GWP | Insurer NI | Affiliate NI | CC / Fgv | BP/EM rec |
|---|---|---|---|---|---|---|---|---|---|
| III.1 | Capitol Preferred | — | **NR** | (L7599–7616) | — | — | — | — | — |
| III.2 | Cypress P&C | single | **NOT** | "This level of fees is presumed not to be fair and reasonable" (L7826–7828) | ~21.2 (computed)/21.5/17.5 | −$3.9M (L7818–7820) | $32.8M (L7820) | $9M surplus note → capital; $2M CC (L7744–7746) | No |
| III.3 | First Community (Bankers Financial) | single? | **UND** | "we were unable to determine if fees paid to affiliates are fair and reasonable" (L8038–8042) | 6.9/7.4/7.3 | −$9.7M (L8016–8018) | $0.05M | — | No |
| III.4 (+III.5) | FL Farm Bureau Casualty + FL Farm Bureau General | national | **F&R** | "NONE - The fees paid to affiliates are presumed to be fair and reasonable" (L8301) | <1 / ~1.8–5.9 | +$0.13M / +$1.09M (L8285–8291) | Parent +$155M | None | No |
| III.6 | Homeowners Choice P&C (HCI) | single | **NOT** | "This level of fees is presumed not to be fair and reasonable" (L8595–8608) | 29.3/28.5/27.6 | **+$28.7M** (L8577–8579) | MGA $85.0M (L8597) | None; paid $47M in dividends (L8589) | No |
| III.11 (in III.6) | TypTap Ins Co | single | **NV** | "consider meeting…long-term viability…enhanced monitoring" (L8614–8618) | 26.7/25.2/25.0 | −$3.9M; losses continued in 2020–21 (L8581–8585) | — | $5M CC (L8469) | **Yes** |
| III.7 (+III.8) | Main Street America Protection + Old Dominion (American Family) | national | **F&R** | "NONE - The fees paid to affiliates are presumed to be fair and reasonable" (L8826) | 0 | +$1.12M / −$0.52M (L8811–8813) | — | $7M CC to Main St (L8703) | No |
| III.9 | PURE (Tokio Marine) | national | **NOT** | "This level of fees is presumed not to be fair and reasonable" (L9019–9025) | 22.4/21.6/21.6 | −$9.3M (L9019–9021) | Pure Risk $176.1M (L9021–9023) | $149M member contributions (L8939–8941) | No |
| III.10 | Southern Fidelity Ins Co | — | **NR** | (L9035–9049) | — | — | — | $70M CC in 2020 | — |

### Phase 4 (memo 2022-03-31): all national, no NOT verdicts

| § | Company | Verdict | Operative text (line) | Insurer NI |
|---|---|---|---|---|
| III.1 | American Bankers Ins Co of FL (Assurant) | **NV** | "no conclusions could be drawn" (L9890–9896); asked to provide affiliate financials (L9902–9906) | +$493.1M (L9888–9890). This is the outlier at L222. |
| III.2 (+III.3) | American Modern Home Ins Co of FL + American Southern Home (Munich Re) | **NV** ("1. NONE", L10183, with no presumption stated) | — | −$1.6M / +$0.24M (L10165–10170) |
| III.4–III.7, III.11 | American Strategic, ASI Assurance, ASI Home, ASI Preferred, Progressive Property (Progressive/ARX) | **NV** | "no conclusion could be drawn" (L11072–11076) | Combined −$102.3M (L11066–11068) |
| III.8 | Auto Club Ins Co of FL | **NV** | Reporting inconsistencies only (L11343–11351) | +$32.3M; affiliates $562M (L11329–11333) |
| III.9 | FCCI Ins Co | **NV** | "no conclusions could be drawn" (L11496–11500) | +$78.8M (L11494) |
| III.10 | First Floridian Auto & Home (Travelers) | **NV** | Inconsistencies only (L11681–11701) | +$6.9M (L11671) |
| III.12 | State Farm Florida | **NV** | Inconsistencies only (L11870–11888) | −$152.3M (L11860–11862) |

### Verdict count reconciliation — does NOT reconcile; not forced

| Count basis | NOT | F&R (explicit) | UND/NV | NR |
|---|---|---|---|---|
| **Executive summary** (L252–264) | **20** (19 single + 1 national) | 18 implied (11 single + 6 national; derived) | 16 "undetermined" (5 + 11) | 4 |
| **This read, company level** (each legal entity a group verdict covers) | **25**: 23 NOT + 2 NOT\* (First Protective L1605, Granada L5316) | **5**: Olympus (conditional), FFB Cas, FFB Gen, Main St, Old Dominion | **23**: UND 2 (ATIC, First Community) + NV 21 | 4 |
| This read, group level (one per Recommendations block) | 18 | — | — | — |

- The company-level count is **+5 over the summary's 20.** The group-level count is **−2.** Neither basis reproduces 20.
- **Candidate sources of the gap:**
  - The 2 "not presumed" (NOT\*) cases may have been tallied as undetermined.
  - Group subsidiaries (FFHIC, Edison, Monarch, THPrime/THSIC, UPCIC, USCPCIC) may have been counted inconsistently.
  - The phase-1 15% test differs from the phase-2–4 115% test.
- The summary's "18 national, 1 NOT" fits PURE as the single national NOT. It also implies exactly 6 national F&R. The 4 explicit F&R (FFB×2, Main St, Old Dom) plus American Modern and American Southern ("NONE") make 6. That suggests the summary scored a bare "NONE" as F&R. I have scored those two as NV.
- A second internal inconsistency: summary Rec. 9 says "two (2) companies" need business-plan review (L382). The memos recommend it for at least **three**: UICNA (L6718), Vault (L7136), TypTap (L8614). A fourth may be United P&C, depending on the TOC alignment.

## 2. TASK 2 — Florida domestic P&C insurer receiverships, 2021 → 2026-10-01

### Sources

- **DFS Division of Rehabilitation & Liquidation, current receivership list:** https://www.myfloridacfo.com/division/receiver/companies (fetched 2026-10-01). It lists 12 companies in liquidation: American Capital Assurance Corp, Avatar P&C, FedNat, Florida Specialty, Guarantee Ins, Gulfstream P&C, Physicians United Plan, Southern Fidelity, St. Johns, United P&C, Weston P&C, Windhaven.
- **DFS R&L Annual Report FY2024-25:** https://myfloridacfo.com/docs-sf/rehabilitation-and-liquidation-libraries/rehab-static/rl-annual-report.pdf. It states "There were no receiverships opened or closed during the fiscal year" (7/1/2024–6/30/2025) and shows 14 companies in receivership at each fiscal year-end from 2022 to 2025.
- **FIGA insolvency feed:** https://figafacts.com/category/insolvency/feed and https://figafacts.com/category/insolvency/feed?paged=2. The newest entry is Arrowood (not a Florida homeowners writer), liquidated 11/8/2023.

### Receiverships

| Insurer (legal entity) | Liquidation order | Source | In RRC report? |
|---|---|---|---|
| American Capital Assurance Corp | 2021-04-14 | figafacts.com/american-capital-assurance-corporation/ ; DFS list | No |
| Gulfstream P&C Ins Co | 2021-07-28 | figafacts.com/gulfstream-property-casualty-insurance/ ; DFS list | Yes (Ph1, NOT) |
| St. Johns Ins Co | 2022-02-25 | figafacts.com/st-johns-insurance-company/ ; DFS list | Yes (Ph1, NV/target exam) |
| Avatar P&C Ins Co | 2022-03-14 | figafacts.com/avatar-property-casualty-insurance-company/ ; DFS list | Yes (Ph1, NOT) |
| Southern Fidelity Ins Co | 2022-06-15 | figafacts.com/southern-fidelity-insurance-company/ ; DFS order 559_crt_20220615 (myfloridacfo.com/docs-sf/default-source/rehab-and-liquidation_publicdocuments_files/559_crt_20220615_orderappointingthefloridadepartmentoffinancialservicesasreceiverforpurposesofliquidationinjunctionan.pdf) | Selected but **NR** (L9035–9049) |
| Weston P&C Ins Co (NAIC 11853) | 2022-08-08 | figafacts.com/weston-property-casualty-insurance-company/ ; DFS list | **Probable successor** of reviewed Weston Ins Co (Ph1, NV). ⚠ WPCIC was formed by merging Weston Ins Co with Weston Specialty (ex-Anchor Specialty) in early 2022, per press reports (insurancejournal.com 2022/08/04; bermudareinsurancemagazine 2022-01-05). I have not verified which legal entity survived the merger, so the match is flagged. |
| FedNat Ins Co (Maison merged in before the order) | 2022-09-27 | figafacts.com/fednat-insurance-company/ ; DFS detail https://www.myfloridacfo.com/division/receiver/companies/detail/562 | Yes (Ph1, NOT) |
| United P&C Ins Co (UPC) | 2023-02-27 | figafacts.com/united-property-casualty-insurance-company/ ; DFS consent order 563_CRT_20230227 | Yes (Ph2, NV-conditional) |
| Florida Specialty Ins Co | 2019-10-02 | figafacts.com/florida-specialty-insurance-company-2/ | No. **Outside the window** (2019). |
| Lighthouse Property Ins Corp | 2022-04-28 | Louisiana court/LDI (propertycasualty360.com 2022/05/04) | No. **Louisiana-domiciled, not a FL domestic.** Excluded. |

**After 2023-02:** I found no new Florida domestic P&C receivership.
- DFS FY2024-25 opened none.
- The current DFS list (2026-10-01) contains no other name.
- The FIGA feed has no FL homeowners entry after UPC.
- Coverage gap: 2023-07 to 2024-06 is checked only through the FIGA feed and the current list, with no FY2023-24 annual report read.

**Not receivership (visible voluntary or other outcomes):**
- **Monarch National** survived: it assumed about 83k FedNat policies on 6/1/2022 and was sold down to Hale Partnership (theinsurer.com; DFS FedNat notices).
- **Sunshine State** merged into Heritage. It is not in the report.
- **Capitol Preferred** merged into Southern Fidelity in 2020 (L7599–7603).
- **UICNA** is still operating: sold to 5B Alliance on 2025-01-31 and rated B (Fair) under review with negative implications (AM Best via businesswire 2025-08-19). ⚠ The AM Best item names "Universal North America Insurance Co" (UNAIC), which is a different legal entity from UICNA. Unverified.

I did **not** verify merger/exit status for Edison, FFHIC, the Tower Hill entities, APPCIC, ATIC, Granada or Cypress. All are absent from the DFS receivership list, so they are scored "survived" (no receivership).

## 3. TASK 3 — The test

Failure = Florida receivership from 2021 to 2026-10-01. Six reviewed companies failed: Gulfstream, St. Johns, Avatar, Weston (successor match, flagged), FedNat, UPC. Southern Fidelity failed but was not reviewed. Monarch survived.

### A. All 53 reviewed companies

| | Failed | Survived | Total | Failure rate |
|---|---|---|---|---|
| **NOT (incl. NOT\*)** | 3: Avatar, FedNat, Gulfstream | 22 | 25 | **12%** |
| **UND / NV** | 3: St. Johns, Weston‡, UPC | 20 | 23 | **13%** |
| **F&R explicit** | 0 | 5 | 5 | 0% |
| Not flagged NOT (UND+NV+F&R) | 3 | 25 | 28 | 11% |

- Base rate: 6/53 = 11.3%.
- NOT vs not-NOT: Fisher exact two-sided p = 1.0.

### B. Florida-centric subset (n=33)

This drops Phase 4 and the national/foreign-owned subsidiaries: PURE, FFB×2, Main St, Old Dominion, Vault, SafePort, UICNA. This is the subset where the MGA-drain thesis is supposed to live.

| | Failed | Survived | Total | Failure rate |
|---|---|---|---|---|
| NOT | 3 | 21 | 24 | **12.5%** |
| UND/NV/F&R | 3: St. Johns, Weston‡, UPC | 6: ACIC, ATIC, PTIC, First Community, TypTap, Olympus | 9 | **33%** |

Fisher p = 0.31.

### C. Phase 1 only (the true ex-ante test: memo 3/31/2021, before any failure)

| | Failed | Survived | Total | Failure rate |
|---|---|---|---|---|
| NOT (13) | 3 | 10 | 13 | 23% |
| Not NOT (Olympus, St. Johns, Weston) | 2 | 1 | 3 | 67% |

Fisher p = 0.21.

**What actually discriminated was sample selection, not the verdict.** Phase-1 membership failed 5/16 (31%), against phases 2–4 at 1/37 (2.7%); Fisher p = 0.007. OIR evidently put its most worrying companies into the first batch.

**Plain answer: the "NOT fair & reasonable" flag did not discriminate.** Among Florida-centric insurers, flagged companies failed at the base rate or below: 12.5% flagged against 33% unflagged. Five of the six failures that were reviewed came from the cases where OIR could not or did not reach a verdict (St. Johns needed a target exam first; Weston was deferred to its RBC plan), or from the batch it reviewed first. Tiny n: no cell supports inference (all p ≥ 0.2).

### Rival explanation: the flag ≈ "the insurer lost money"

Mechanics: when insurer net income is ≤0, the threshold collapses to the $2M/yr floor. Any affiliate earning more than $6M over three years then trips "NOT" (L690–694, L3870–3874). A loss-making MGA-run insurer is therefore almost guaranteed a NOT whatever its fee rate.

| Among the 25 NOT | Count | Failed |
|---|---|---|
| Insurer 3-yr NI < 0: Avatar, FedNat/Maison, Monarch, First Protective, FFIC/FFHIC†, Fla Peninsula/Edison†, Gulfstream, Safepoint, THPIC, APPCIC, UPCIC, Heritage, Safe Harbor, USCPCIC, SFIC, SOIC, Cypress, PURE | 20 | 3 (15%) |
| Insurer 3-yr NI > 0: THPrime, THSIC, AIIC, Granada, HCI | 5 | 0 |

† Subsidiary figures are not separately stated; each takes the group-level loss.

**80% of flagged companies were loss-makers.** The flag is largely a restatement of "insurer lost money while its affiliate didn't."

Does failure track losses alone? Across all 53:
- 37 loss-makers produced 5 failures (13.5%).
- 16 profit-makers produced 1 failure (6%). That one is Weston at +$0.17M, essentially break-even, and its surplus was overstated by a $9M MGA receivable (L3611–3615).
- Fisher p = 0.66.

So losses explain the flag. Losses alone also do not separate the failures well: survivors include Heritage −$80.9M, State Farm FL −$152M, ASI −$102M, SFIC −$26.8M and Safepoint −$22.1M. What visibly separates them is **deep-pocket parent backing** (State Farm, Progressive, publicly listed Heritage, and capital from Hudson or other investors). That is not something the report measures.

### Caveats (all apply)

1. **Tiny n.** There are 6 failures, and no cell supports a statistical claim.
2. **Timing.** Phases 2–4 (3/31/2022) postdate the Gulfstream, St. Johns and Avatar liquidations, and the report knew of them (L50). Only Phase 1 is ex-ante.
3. **Window mismatch.** The data covers 2017–19. The failures were driven by 2020–22 events: the AOB/litigation peak, the reinsurance hardening of 2021–22, and Hurricanes Ida and Ian. The fee test never saw those years.
4. **Survivorship and selection.** The 57 were chosen by OIR and the selection basis is undocumented. Phase 1 was plainly the high-concern batch. Southern Fidelity, which failed, was excluded as "not reviewed".
5. **Mechanical criterion.** The rival explanation above, "flagged = loss-maker", is supported 20/25.
6. **Entity matching.** The Weston match runs through a 2022 merger and is flagged. The FedNat verdict was rendered at group level, so it covers Monarch, which survived.
7. **Classification.** The single-state vs national split is my inference. The report gives no per-company label.

## 4. TASK 4 — CORAL tracked carriers

| Carrier | In report? | Verdict (line) | Note |
|---|---|---|---|
| Slide Insurance | No | — | **Did not exist in 2017–19** (founded 2021) |
| Manatee Ins Exchange | No | — | **Did not exist in 2017–19** |
| Mangrove Property Ins | No | — | **Did not exist in 2017–19** |
| One Alliance Ins Corp | No | — | **Did not exist in 2017–19** |
| Apex | No | — | Not in report; entity identity unverified |
| American Integrity (AIIC) | Yes, Ph2 III.2 | **NOT** (L4657–4667) | Profitable (+$7.2M), but $38.35M MGA fee forgiveness in 2019 |
| HCI / Homeowners Choice | Yes, Ph3 III.6 | **NOT** (L8606) | Profitable (+$28.7M); MGA earned $85.0M |
| TypTap | Yes, Ph3 III.11 | **NV + business-plan review / enhanced monitoring** (L8614–8618) | −$3.9M |
| Universal P&C (UPCIC, UVE) | Yes, Ph2 III.16/III.14 (reviewed with APPCIC in III.3) | **NOT** (L4910–4914) | ERA (affiliate) earned $166M vs combined −$11.1M. **Not** the failed United P&C. |
| United P&C (UPC, failed 2/27/2023) | Yes, Ph2 III.14/III.12 (in III.1) | **NV-conditional** (L4452–4456) | Separate entity from Universal |
| Heritage P&C | Yes, Ph2 | **NOT** (L5533) | −$80.9M; affiliates $174.3M |
| Security First | Yes, Ph2 | **NOT** (L6343) | −$26.8M; $35M CC |
| Florida Peninsula / Edison | Yes, Ph1 III.7 | **NOT** (L2263) | FPH distributed ~$24–32.5M/yr to members (L2202–2208) |
| Tower Hill (Preferred/Prime/Signature) | Yes, Ph1 III.13 | **NOT** (L3417) | Affiliates >$120M vs +$3.5M |
| Florida Family (FFIC/FFHIC) | Yes, Ph1 III.5 | **NOT** (L1923) | 18% MGA agreement more than 20 years old (L1929–1933) |
| Olympus | Yes, Ph1 III.10 | **F&R-conditional**; table says "Review Business Model" (L2631–2645) | Would have been impaired without the $56M MGA contributions |
| People's Trust | Yes, Ph2 | **NV** (company self-admitted excess; refile; L5769–5777) | Highest fee load in the sample: 48–63% of GWP |
| Safe Harbor | Yes, Ph2 | **NOT** (L5981) | Joint with US Coastal |
| SafePort | Yes, Ph2 | **NV** (L6160–6194) | IAT group; fees <1% of GWP |
| Cypress P&C | Yes, Ph3 III.2 | **NOT** (L7828) | Affiliates $32.8M vs −$3.9M |

**Bottom line for CORAL:** 10 of the tracked Florida domestic groups still operating carry a NOT verdict from 2021 or 2022: AIIC, HCI, Universal, Heritage, Security First, Florida Peninsula, Tower Hill, Florida Family, Safe Harbor and Cypress. None of them has failed in the 4.5 years since. The verdict is not a usable solvency signal on its own. Its value is as evidence of **where profits sit**: in the MGA and holding company, outside the regulated insurer. That matters for a Citizens-assessment or receivership-recovery read, not as a failure predictor.
