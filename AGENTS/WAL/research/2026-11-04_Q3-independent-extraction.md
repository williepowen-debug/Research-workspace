# WAL Q3 Call Report — independent extraction completed

**2026-11-04. Western Alliance Bank, RSSD 3138146; June 30 → September 30 2026.** WAL / OpenAI Codex. This completes the existing approved source/extraction assignment. The earlier same-day UNCHECKED result is superseded for this extraction, not rewritten as a successful earlier request. No completed 10-Q grade, prior prediction resolution, frozen calibration, scenario weight, vector score, target or trade rule is changed.

## Five findings

1. **MI3 fell to 19.81% from 21.20%** on WAL's existing RCON2746 / RCON1766 basis, down 1.397 percentage points. The numerator fell 3.76% while C&I grew 3.02%. The reading remains below the existing 25% bear-fast threshold and within the existing <24 band; the 8/7 kill remains fired, not a new firing or a new scenario re-mark. This measures CRE lending **not secured by real estate**, not the secured-office book or the $99M loan.
2. **NDFI nonaccrual is almost unchanged: $122.456M → $122.497M**, rate 0.77445% → 0.77371%. Exposure grew mainly in unused commitments: $4.884B → $5.900B (+20.80%), including private-equity-fund commitments $544.200M → $1,015.889M (+86.68%). The face amount is contractual capacity, not a funded draw, demonstrated stress or expected loss. Borrower/loss attribution remains absent. No V3 score change.
3. **Modified-loan populations generally improved, with exceptions.** Compliant modifications fell $232.291M → $198.703M; delinquent/nonaccrual modifications fell $101.480M → $51.391M. Other CRE performing modifications rose, while its nonaccrual modifications fell. These changing stocks are not a loan-level cure/migration bridge or an Office-classified proxy. GNMA-adjusted 90+ accruing residual rose $62.520M → $66.202M; the raw $1.385B figure is dominated by $1.319B rebooked GNMA.
4. **Bank mortgage income rebounded despite less sales volume.** RC-P quarterly income $45.723M → $64.982M (+42.12%); sales $16.170B → $15.163B (−6.22%). This is not parent mortgage revenue, recurring EPS, or a gain-on-sale margin. Warranty reserves and servicing foreclosures rose; the report does not bridge valuation, hedging, servicing and entity classifications.
5. **Bank CET1 capital grew, but risk-weighted assets grew faster.** Capital $7,651.672M → $7,731.785M; RWA $66,063.310M → $67,551.574M; reported ratio 11.5823% → 11.4458% (−13.65bp). Bank AOCI −$447.749M → −$785.758M. These are bank figures, not the parent's capital basis or a new capital/ratings trigger. Funding, peers and severity remain REGINALD's.

## Source custody and independent reproduction

CATO supplied full files under `AGENTS/CATO/runs/2026-11-04_ffiec-access/`, with adjacent receipt.json. WAL independently checked endpoint, HTTP status, byte length, SHA-256, row count, every row's bank/period identity, unique MDRMs, and presence of RCON1766. Exact, unmodified byte copies plus CATO's receipt and WAL's provenance are preserved and committed under `sources/ffiec_2026-11-04_verified/`.

| Period | Retrieved by CATO, UTC 11/04 | Rows | Bytes | SHA-256 |
|---|---|---:|---:|---|
| 2026-06-30 | 22:30:27.190295 | 1,812 | 184,829 | `7c40bbb5154eb84e362492f408f95316ef1b44b82ef2dcc9ca82f1b61bccbcdb` |
| 2026-09-30 | 22:30:28.446801 | 1,792 | 182,754 | `2e04cc7bf1a78e525a68059c358215c8ce9e3c24c3639d84ea74ccb8d69c60a4` |

Both came from FFIEC `https://ffieccdr.azure-api.us/public/RetrieveFacsimile`, SDF, RSSD 3138146. The Q3 hash matches WALTER's historical 11/01 receipt exactly; this is a fresh authenticated retrieval of identical complete bytes, not a reconstruction from WALTER's selected rows. June is byte-identical to WAL's accepted October 14 source. CATO's successful retrieval resolves the input/access dependency for this assignment; it does not certify installation of a renewed token on both machines or close every WQ-31 credential task.

Reproduce offline from root: `python3 AGENTS/WAL/scripts/ffiec_wal_extract_20261104.py`. The script independently parses the complete originals with the pre-existing 70-field map, plus total assets required by the existing MI3 ledger. Outputs: `research/2026-11-04_Q3-extraction/{metrics.json,approved-fields.tsv,supporting-schedules.tsv,checks.json}`. **12 validations pass; 2,159 supporting schedule rows across both periods; all 70 Q2 fields reproduce WAL's accepted October 14 extraction.** Q3 has 68 reported approved fields and two expected semiannual omissions; total assets is separately reported. Dollar source values are USD thousands; tables below convert to millions unless marked otherwise. Election flags and percentages retain their own units.

## MI3 and NDFI

| Measure / MDRM | June | September | Basis / implication |
|---|---:|---:|---|
| MI3, RCON2746 | $2,554.610M | $2,458.442M | −$96.168M; −3.76% QoQ |
| C&I item 4, RCON1766 | $12,047.671M | $12,411.862M | +3.02% QoQ |
| MI3 / item 4 | 21.20418% | **19.80720%** | −1.39698pp; existing <24 band, below 25% kill threshold |
| Funded NDFI, RCONJ454 | $15,812.034M | $15,832.394M | +$20.360M; 24.11294% → 24.01231% of total HFI+HFS loans |
| NDFI / HFI, RCONB528 denominator | 25.94276% | 25.72316% | Consistent with rounded parent-table 25.9% → 25.7%; never mix with total-loan basis |
| NDFI nonaccrual, RCONPV25 | $122.456M | $122.497M | +$0.041M; rate 0.77445% → 0.77371% |
| NDFI 30–89 / 90+ accruing, PV23/PV24 | $0 / $0 | $0 / $0 | Reported zero, not missing |
| Unused NDFI, RCONPV11 | $4,884.273M | $5,900.087M | +20.80% |
| Funded + unused contractual face | $20,696.307M | $21,732.481M | +5.01%; not additive expected loss |

| NDFI subtype | June funded | Sept funded | June unused | Sept unused |
|---|---:|---:|---:|---:|
| Mortgage intermediaries | $10,895.412M | $10,767.707M | $1,680.541M | $2,001.874M |
| Business intermediaries | $3,459.295M | $3,599.174M | $2,659.531M | $2,882.324M |
| Private equity funds | $1,457.327M | $1,465.513M | $544.200M | $1,015.889M |
| Consumer / other | $0 / $0 | $0 / $0 | $0 / $0 | $0 / $0 |

Funded subtype ties are exact both periods; September unused ties exactly. June unused subtypes sum $1K below the total, within the **existing** October 14 tolerance; the residual is disclosed, not fixed. The denominator for WAL's frozen MI3 instrument stays item 4; REGINALD owns its separately chosen cross-bank denominator. No cohort rank or new bank comparison is inferred. The prior September 2025 subtype-offset caution remains valid; no new classification story is fitted here.

## Modifications, arrears and realized losses

| Bank measure | June | September |
|---|---:|---:|
| Compliant modifications, HK25 | $232.291M | $198.703M |
| Modified 30–89 / 90+ / nonaccrual, HK26/27/28 | $2.680M / $42.325M / $56.475M | $5.269M / $9.063M / $37.059M |
| Combined reported modified populations | $333.771M | $250.094M |
| Other CRE-NOO compliant / nonaccrual mods, K162/K119 | $72.736M / $51.545M | $88.187M / $21.658M |
| All bank nonaccrual, RCON1403 | $564.365M | $487.951M |
| Raw 90+ accruing / rebooked GNMA, 1407/K043 | $1,285.415M / $1,222.895M | $1,385.227M / $1,319.025M |
| Residual excluding rebooked GNMA only | $62.520M | $66.202M |
| YTD gross charge-offs / recoveries, RIAD4635/4605 | $266.797M / $3.191M | $314.824M / $5.421M |
| HFI / off-balance ACL, RIAD3123/RCONB557 | $487.385M / $52.008M | $512.787M / $61.609M |

Q3 NCO = (314.824 − 5.421) − (266.797 − 3.191) = **$45.797M**, reproducing the already-accepted issuer $45.8M at printed precision; this is a cross-check, not another WAL-02 grading. MI3-specific YTD charge-offs/recoveries are reported $0/$0, but there is no NDFI-only loss attribution or borrower bridge. Bank nonaccrual contains HFS and government-guaranteed/insured populations; source fields keep these separate. The GNMA residual is not wholly unguaranteed NPL. **RCONC410/C411, nonaccrual additions/sales, are absent at Q3 because they are June/December semiannual fields; never zero-fill or infer quarterly cures.**

## Mortgage and contingent exposure

| Bank measure | June | September |
|---|---:|---:|
| Mortgage sales / quarter, FT04 | $16,169.574M | $15,163.102M |
| Retail / wholesale originations and purchases, HT81/82 | $635.166M / $15,709.880M | $379.326M / $14,337.616M |
| RC-P quarterly income, RIADHT85 | $45.723M | $64.982M |
| Repurchase/indemnification principal, HT86 | $23.880M | $22.568M |
| Warranty reserve, M288 | $3.288M | $4.298M |
| Servicing assets carrying / fair value, 3164/A590 | $1,499.649M / $1,499.725M | $1,575.949M / $1,575.949M |
| Serviced without recourse UPB, B805 | $75,682.300M | $74,624.414M |
| Serviced mortgages in foreclosure UPB, F699 | $359.162M | $410.411M |
| Asset sales recourse UPB / maximum exposure, B790/B797 | $963.969M / $963.969M | $1,070.162M / $1,070.162M |

Repurchase principal is not loss. Reserve, servicing and recourse columns have different populations; equal B790/B797 values are not two exposures to add. Quarterly bank income cannot replace the parent's mortgage origination, servicing or fair-value/hedge bridge. Full field locators/definitions and the remaining approved fields are in the extraction TSV.

Bank CET1/RWA reported ratios tie within the pre-existing tolerance; AOCI opt-out is 1 both periods and MSA threshold deductions are reported zero, not zero risk. Other on-balance SSFA exposure/RWA moves **$10,662.094M/$2,123.768M → $10,510.905M/$2,094.035M**; off-balance exposure/RWA **$2,179.545M/$435.909M → $2,571.983M/$544.397M**. These regulatory exposure/RWA rows are not an equity-loss estimate and can overlap NDFI/recourse. Bank assets $98,568.765M → $97,898.530M; not the parent asset figure.

## Record updates, unchanged authority and remaining conditions

MI3_SERIES appends September (13 observations total), advances its real-data date only now, and records the original item-4 band. KB282–287 carry the six evidence families; the prior Q2-only KB230–234 snapshots are retained and marked superseded for current use. THESIS/CHANGELOG receive a dated evidence-only fold: **v2.5, weights 2/12/49/30/7, EV $76.60, PT $52–77, vector scores and composite unchanged**. No retired implication column is executed. STATUS/MEMORY/INDEX and final NEXUS brief are synchronized. Earlier failed-request receipts and the earlier UNCHECKED report remain dated history, with a pointer to this completed result. Funding/peers/severity remain REGINALD's; evidence packet delivered for its own integration. Existing predictions remain resolved; no new Q4 prediction is invented by this extraction.

**Remaining substantive unknowns:** NDFI borrower entries/exits/loss attribution; whether unused capacity is drawn; full modification/cure bridge; parent-versus-bank mortgage/hedge and capital reconciliation; the $99M secured-office appraisal/disposition. The completed Call Report extraction does not resolve those questions. Other carried score/hotel/Q4-prediction work remains separate. Source/access is no longer a blocker to this assignment. Recipient integration/consumption is not established by a saved packet.
