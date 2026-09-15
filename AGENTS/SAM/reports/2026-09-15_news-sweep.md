# SAM news sweep — September 15, 2026

**Cutoff:** September 15, approximately 09:08 ET / 22:08 JST. New September 14–15 releases checked, plus older material missing from SAM. News and source dates are separate. Market quotes remain at their explicit prior observation clocks; this is a news integration, not a fresh trading snapshot.

## Assessment

Six items merit integration. They strengthen the case for watching the BOJ's treatment of supply shocks and the fiscal burden of higher rates, while leaving long-end demand mixed. **v1.7 remains retired/LOW; no successor, probability change or prediction resolution.** No reviewed item establishes forced overseas-asset sales or a new carry-unwind trigger.

| Item | Publication / observation | Verified fact | SAM disposition |
|---|---|---|---|
| 20Y JGB auction | September 15 | BTC **4.005×**, tail **1.3bp**, cutoff yield **3.869%** | **AMBIGUOUS** on frozen bars; resolved in docket, counter remains 0/2. |
| Industrial production revision | September 14, 13:30 JST; July data | SA production index **104.4**, revised from 104.7; **−0.2% m/m**, +3.9% YoY unadjusted | Softer activity input, with shipments +2.1% m/m; not an economy-wide contraction verdict. |
| BOJ inflation-risk remarks | Summary reported September 14; remarks **May 28** | Koji Nakamura discussed repeated supply shocks and nonlinear import-price/FX pass-through | Reaction-function context for September 18; not new September guidance. |
| FY2027 requests | MOF aggregate September 4; debt-service detail August 28 | **¥143.0656T** requests; **¥36.6386T** debt service, including **¥16.5888T** interest/discount charges | Newly integrated fiscal context; requests are not an enacted budget or issuance plan. |
| Foreign equity/fund flows | MOF September 8; August data; resurfaced in September 15 news | Residents' net purchases **¥1.2983T**; investment-trust managers **¥1.3458T** | Outward-allocation counterflow; not all NISA, a measured FX hedge ratio, or forced carry liquidation. |
| Japan–IEA cooperation | September 14 | Energy-security cooperation and critical-mineral supply-chain resilience reaffirmed | Policy context; no newly quantified delivery or stock-release amount in the reviewed readout. |

## 1. Auction resolved — the tail matters

[MOF's result](https://www.mof.go.jp/english/policy/jgbs/auction/calendar/eresul/eresul20260915.htm) reports issue 197, competitive bids ¥2,131.3B and competitive acceptance ¥532.1B. BTC = 2,131.3 / 532.1 = 4.00545×. Cutoff 3.869% minus average 3.856% = **1.3bp**. Non-price competitive I acceptance ¥167.4B is separate and is not added to the BTC denominator.

The frozen [September 11 ruling](../thesis/AUCTION_GRADING_RULING_2026-09-11.md) applies: SOFT requires BTC <3.5 or tail >2.0bp; FIRM requires BTC ≥4.0 **and** tail ≤1.0bp. Neither branch fires, hence **AMBIGUOUS**. The tail misses FIRM by 0.3bp, beyond the ≤0.1bp precision qualifier. The ingestion script's generic “Orderly” label is a different alert, not the registered grade. This result does not identify a buyer or resolve fiscal-versus-policy attribution. September 29 uniform-price 40Y remains descriptive only; no firm-counter advance.

**Correction to the previous sweep:** the 12:21 JST failed request used `.../eresul/resul20260915.htm`, omitting the initial `e` in the filename. Its 404 cannot establish that the result was unpublished. The correct `eresul20260915.htm` is now verified. Publication timing at the earlier check is unknown. The old report is annotated; its raw failed-attempt record is preserved.

## 2. Growth and the BOJ reaction function

[METI's July revised report, official e-Stat mirror](https://www.e-stat.go.jp/stat-search/file-download?fileKind=2&statInfId=000040504763), page 1, gives production 104.4 (2020=100), down 0.2% m/m; shipments rise 2.1% and inventories 0.5%. The production revision is attributed to pharmaceuticals and canned alcoholic drinks, among other items. The [release record](https://www.e-stat.go.jp/stat-search/files?kikan=00550&layout=dataset&stat_infid=000040504763) confirms September 14, 13:30. Direct METI downloads failed with 403; the government mirror supplied the complete report and page 1 was visually checked. This is a July observation, before September's oil shock.

[BOJ-IMES conference summary](https://www.imes.boj.or.jp/research/papers/english/26-E-12.pdf), printed pp.23–25 / PDF pages 24–26, explains Nakamura's concern that repeated supply shocks may affect underlying inflation and expectations, with nonlinear reactions to import prices and exchange rates. The [conference program](https://www.imes.boj.or.jp/en/conference/2026confsppa.html) places his panel on May 28. [Reuters' September 14 report](https://www.marketscreener.com/news/boj-executive-saw-need-for-vigilance-to-non-linear-inflation-spikes-ce785bdcd88cf121) supplies the new-publication date. **Inference:** watch how the September statement balances activity damage against persistent inflation; the May panel is not a commitment to this week's vote or rate path.

## 3. Fiscal burden — correct units and comparison

[MOF September 4 aggregate](https://www.mof.go.jp/policy/budget/budger_workflow/budget/fy2027/sy20260904.pdf), page 1, totals **1,430,656 × ¥100M = ¥143.0656T**. Page 2 compares with FY2025 supplementary plus FY2026 initial spending of ¥140.6126T: difference **¥2.4530T**. Bringing recurring supplementary spending into initial requests makes comparison with the FY2026 initial budget alone misleading. The general-account strategic investment column is ¥12.1730T and is already included in the total.

[MOF debt-service detail, August 28](https://www.mof.go.jp/about_mof/mof_budget/budget/fy2027/20260828.html) separates ¥20.0025T redemption, ¥16.5888T interest/discount charges and ¥0.0473T administration. Total ¥36.6386T, up ¥5.3628T versus the FY2026 initial budget. **Debt service is not interest alone.** These are requests, with unpriced items and later budget decisions still ahead. They support a fiscal sensitivity watch, not a settled JGB supply forecast or evidence that today's yield move was fiscally caused.

The [Reuters syndicated copy](https://www.investing.com/news/economy-news/japan-budget-requests-swell-to-pandemicera-scale-under-takaichi-agenda-4888765) states ¥143.66T. SAM adopts the visually checked MOF total, **¥143.0656T**, and logs the discrepancy instead of propagating it. Reported interest-rate assumptions and issuance targets are not needed for this finding and are not treated as approved policy.

## 4. Outward allocation and energy policy

[MOF monthly investor-sector equity/investment-fund CSV](https://www.mof.go.jp/policy/international_policy/reference/itn_transactions_in_securities/monthb2.csv), updated September 8, has August total net **12,983 × ¥100M** and investment-trust-manager net **13,458 × ¥100M**. August total is the largest since March (¥2.2210T). [Reuters' September 15 yen story](https://sa.marketscreener.com/news/yen-rally-faces-moment-of-truth-as-boj-risks-disappointing-markets-ce785bddd888f122) resurfaced this older observation. The monthly data do not establish September flows, household-only/NISA participation, or contemporaneous FX transactions. They counter a blanket assumption that domestic rate rises force every investor to repatriate.

[MOFA's September 14 Motegi–Birol readout](https://www.mofa.go.jp/press/release/pressite_000001_02654.html) records POWERR Asia cooperation and critical-mineral resilience. Its reference to an earlier coordinated stock release is not a newly announced quantity. The [same-day Kantei summary](https://japan.kantei.go.jp/105/diplomatic/202609/0914meeting.html) also discusses POWERR GX; that branding already appeared in the [August 26 GX Council account](https://japan.kantei.go.jp/105/actions/202608/26gx.html). Do not call September 14 its launch date. Kantei direct retrieval failed; indexed primary text corroborates context, while the full MOFA page was readable through browsing. No claim here resolves SAM-28's oil route or the physical-volume test.

## Exclusions, remaining evidence and next checks

- Recycled reserve-stock/“Treasury dumping” headlines add no identified transaction. Prior GPIF-capacity and intervention-attribution limits stand. No newly verified named-insurer forced-sale disclosure emerged from this bounded search; that is not proof none exists.
- News pricing and strategist scenarios are not BOJ decisions. Existing dated Totan review remains a historical observation until checked against the latest image; no current Fed probability was authenticated in this news sweep.
- **September 16:** August trade/crude volume, BOJ scheduled 25Y+ operation, FOMC decision/dots. **September 17–18:** institutional flows, CPI, BOJ, CFTC and original SAM-28/31 review at close. No invented route endpoints or VIX fixing convention.
- Fiscal follow-through: final budget and financing/tenor mix. Energy follow-through: funded commitments, actual stock releases, shipments and import volumes. No artificial dated catalyst created for an undated watch.

## Integration and evidence

Auction ledger and frozen-grade assessment updated; completed event removed from both forward calendar feeds. Current STATUS, MEMORY, pillar/channel references, JGB supply/demand assessment, KB and NEXUS brief carry the relevant findings. Raw primary files, calculations, failed-access notes and before-images are in [the evidence folder](../research/outputs/2026-09-15_news-sweep/). Prediction terms, auction registration and money fields remain byte-identical. Validation is recorded there at closeout.
