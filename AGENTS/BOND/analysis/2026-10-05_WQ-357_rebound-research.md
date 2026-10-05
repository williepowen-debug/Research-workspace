# BOND — latest market evidence and the WQ-357 rebound question
Written 2026-10-05T10:38:00-04:00; primary/API capture 2026-10-05 10:23 ET. Research requested by Will, authorized under WQ-357 LATER and PROME DOCKET line 608, due 10/5. This is the written deliverable; recipient acknowledgement is separate.

Completed observations do not establish a sustained long-end rebound. The supportive evidence is real: weaker employment, reduced near-term hike pricing, Friday credit relief, falling long-end dealer inventory and an official buyback bid. Against it, the long end gave back Thursday's rally on Friday, real yields remain elevated, and model term premium increased. The evidence supports keeping the two rates channels separate; it cannot establish that bond prices must continue falling.

## Latest figures — observation dates are not retrieval dates

| Measure | Latest | Change / meaning | Observation and source |
|---|---:|---|---|
| Treasury 2Y / 5Y / 10Y / 30Y par | 4.83 / 5.06 / 5.28 / 5.63% | Friday +5 / +5 / +4 / +2bp | 10/2 official Treasury CSV [nominal curve](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_yield_curve) |
| Treasury 10Y / 30Y real | 2.92 / 3.34% | Friday +4 / +3bp | 10/2 [real curve](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_real_yield_curve) |
| 10Y nominal minus real | 2.36% | Unchanged Friday; nominal +4bp was matched by real +4bp | Same-date par-curve difference, not an independently quoted inflation swap |
| 5Y5Y inflation forward | 2.35% | 15bp below the 2.50 red line | FRED T5YIFR 10/2, latest-vintage |
| HY / CCC / IG OAS | 310 / 1202 / 85bp | Friday −14 / −13 / −1bp | FRED 10/2; first-published and latest-vintage agree |
| BBB / BB / B OAS | 104 / 191 / 312bp | Friday −2 / −13 / −17bp | FRED 10/2 latest-vintage |
| CCC−BB | 1011bp | Tail stress persists despite Friday tightening | Same-date subtraction, 1202−191 |
| ACM 10Y term premium | 0.9050 percentage points | +2.0bp / 1 observation, +17.8bp / 5 observations | NY Fed ACM Daily 10/1, latest-vintage model estimate |
| Kim-Wright 10Y term premium | 1.0203 percentage points | Different model/frontier; not averaged with ACM | FRED THREEFYTP10 9/25 |
| FR2004 long-end net inventory | $140.545B | −$3.828B w/w | NY Fed current API partition, as-of 9/23; no newer common-bucket print |
| SOFR minus IORB | −2bp | No positive funding print on this latest shared date | SOFR 3.88−IORB 3.90, both 10/2; LIQUID owns interpretation |
| 30Y fixed mortgage survey | 7.28% | +25bp w/w; mortgage−same-date 10Y = 204bp | [Freddie Mac PMMS](https://www.freddiemac.com/pmms), 10/1 weekly survey; not MBS OAS |
| TLT / TBT | $77.25 (-0.30%) / $42.80 (+0.61%) | Momentary vendor quotes, not closes or execution prices | yfinance captured 2026-10-05T10:23:03.784786-04:00 |

Latest official curves end 10/2; there is no 10/5 official close yet. The H.15/FRED nominal-real frontier still ends 10/1 at this morning's pull. Treasury observations are shown separately, rather than substituted silently into FRED. Full raw records and source hashes: `analysis/2026-10-05_live-refresh/raw/`; reproducible one-off fetch: `analysis/2026-10-05_live-refresh/fetch_snapshot.py`. One archival PDF request timed out after the numeric pulls succeeded; the Paramount pricing release was read through web instead. No full-source archive success is claimed.

## Evidence on both sides

| Supports a rebound | Counters a sustained rebound | What the evidence can establish |
|---|---|---|
| [BLS September employment](https://www.bls.gov/news.release/empsit.nr0.htm): +29,000 payrolls, unemployment 4.2%, July/August revised down 60,000 | 10/2 long-end yields rose despite that release | Weak employment can soften policy expectations; this completed session did not sustain lower long yields |
| Post-October expected EFFR fell from +17.5bp vs current EFFR on 9/28 to +5bp on the 10/2 vendor daily bar | About one cumulative hike remains priced by year-end; the curve still embeds positive tightening | Relief in the front path is different from falling long-duration compensation |
| Treasury can purchase older long-sector bonds, and bought the full $6B cap on 10/1 | It is a capped liquidity operation, without a yield target; newest-vintage share was 0% | An official absorption bid exists; neither its price effect nor yield control follows from size alone |
| Long-end dealer inventory fell for two weekly observations | 3–6Y inventory rose sharply, satisfying the existing paired kill letter | Bucket divergence; aggregate net inventory does not identify auction-specific warehousing |
| HY and lower-quality tiers tightened Friday; Paramount priced a very large financing | CCC still exceeds the escalation line; real yields and mortgage costs remain high | Access for this issuer and one-day credit relief, without proof of broad normalization |

Friday's completed curve: versus 9/30, the 2Y was −5bp, but the 10Y and 30Y only −1bp each. Versus 10/1, nominal 10Y +4bp and real 10Y +4bp imply no 10Y breakeven change. That is consistent with real-rate pressure; it is not, by itself, a term-premium causal decomposition. ACM/KW outputs and fed-funds futures cover different windows and horizons.

The latest [Jefferson speech](https://www.federalreserve.gov/newsevents/speech/jefferson20261001a.htm), 10/1, attributes much of the recent headline inflation pickup to energy, retains data dependence and acknowledges inflation risk. It does **not** explicitly assign the Treasury move to term premium. The earlier STATUS wording did; it is corrected here. No October commitment is inferred from the speech.

## Corporate access and structural demand

[Paramount's 9/30 issuer release](https://ir.paramount.com/node/73371/pdf) priced $41.4B plus €885M of secured notes and $8.5B plus €850M of term loans. Dollar notes comprise $30B first-lien and $11.4B second-lien; second-lien coupons are 8.25%, 8.875% and 9.125%. Expected note closing is 10/5, subject to conditions; pricing is verified, closing is not. The prior ~$12.4B launch estimate is superseded. This is primary-access evidence for one large secured issuer, not a count of all failed/pulled deals, nor an observed aftermarket price.

[NBIM's primary letter](https://www.nbim.no/en/news-and-insights/submissions-to-ministry/2026/the-government-pension-fund-global--analyses-and-assessments-of-the-investment-strategy-for-bonds/), footnote 3, defines its MBS references as agency MBS. The roughly 13% proposed MBS weight therefore belongs to that category; CMBS/ABS are additional, smaller securitized segments. This closes the taxonomy question. Dollar sizing remains an estimate; implementation requires a Ministry decision. No adoption was located in this bounded issuer search.

## The two WALTER checks

**SIG-W-20261003-005:** DTS 10/1 opening $984.046B, closing $893.699B ⇒ −$90.347B, approximately the headline $91B. Deposits $373.651B and withdrawals $463.997B imply −$90.346B; the $1M difference is reporting precision. These are dollar millions in the API's `open_today_bal` field for each labelled account row, including the closing-balance row; `close_today_bal` is null. The 10/1 buyback accepted $6B par and settled **10/2**, so attribution of the 10/1 draw to that operation fails timing as well as scale. The entire cash draw is not bond-buyback spending. Official 9/30→10/1 curve declines were 2Y −10bp, 10Y −5bp, 30Y −3bp; the claim of a uniform 10–12bp Treasury decline also does not match these closing observations. Other causal channels were not adjudicated.

**SIG-W-20261002-032:** own dated vendor-contract reconstruction agrees with the large reduction since 9/28, but cannot certify a strict year-end “less than one hike” headline. Formula with Dec 9 FOMC and change effective Dec 10: post-December expected EFFR = (31×December average −9×November average)/22. On the retrieved 10/2 daily bars November 3.930%, December 4.074997%, EFFR 3.88% ⇒ +25.43bp by year-end, versus WALTER's +24.7bp from a December 4.070% input. On the evolving 10/5 bar the estimate is +25.93bp; post-October +5.50bp corresponds to ~22% only under hold/+25 with stable EFFR basis. This is roughly one hike, sensitive around the 25bp boundary, **not** a verified OIS/CME probability distribution or exchange settlement. CME's embedded tool returned an access error; an authenticated OIS feed is not available. No registered rates item or TBT posture changes solely on that boundary wording. Independently dated FedWatch/OIS comparison remains unavailable.

## Rules, positions and next tests

Composite remains **17/35**, re-summed 5+4+2+3+1+1+1. HY is 40bp below the 350 line; IG 35bp below 120. Credit-equity lead is +47bp from 263, leaving 28–53bp to 338–363; the VIX condition remains VIOLET's observation. CCC escalation remains fired. VX-11's legacy >1200 red field is exceeded by 2bp, but its explicit registered score rule is →4 on >1100; no →5 letter is present, so score 4 is preserved and the spec discrepancy is disclosed rather than invented away.

Real gate remains met; five-close sustain under WQ-246 is satisfied. Treasury's 2026 curve has **17** consecutive real-10Y observations ≥2.50 from 9/10 through 10/2 (the previous 12 count was stale). Its nominal-30Y run ≥5.00 is **63** sessions from 7/7, with 79 of 190 2026 observations ≥5.00. These are Treasury-series counts. The separate whole-series FRED run is 62 through 10/1; do not combine frontiers.

The September 23 5Y paired kill remains **MET**: FR2004 3–6Y $60.079B versus $56.586B bar; +$12.093B from $47.986B PRE. Riders remain: net inventory is not proof of auction warehousing, the funding window is **UNGRADED**, and the operational rule makes no predictive claim. Existing REAFFIRM EXIT recommendation is unchanged. Will's WQ-357 **LATER** preserves TERRY path C to **10/14**, and WQ-280 **NO-ADD** stands. The recorded sleeve is Oct-16 82P ×1 plus TBT 10 shares, per the 10/1 mirror; broker truth was not newly verified. WQ-339 authorized card drafting; WQ-360 fill remains unapproved. No order, capital proposal, gate replacement or new prediction is created.

| Next observation | Date / time ET | Test to read |
|---|---|---|
| 3Y $58B, 91282CRQ6 | 10/6 13:00 | Frozen indirect bar 58.90%; OLD 56.50 / 19.50; cover 2.54 |
| 10Y reopening $39B, 91282CRF0 | 10/7 13:00 | Frozen pooled 65.05%; reopening alternative 66.32; OLD 63.95 / 13.38; cover 2.39 |
| September FOMC minutes | 10/7 14:00 | Policy-path evidence; [Fed October calendar](https://www.federalreserve.gov/newsevents/2026-october.htm) |
| 30Y reopening $22B, 912810UW6 | 10/8 13:00 | Pooled 63.89%; reopening alternative 61.20; OLD 59.95 / 14.74; cover 2.29 |
| FR2004 as-of 9/30; next F2 operation | 10/8 | Published bucket changes and actual CUSIP purchases |
| CPI; WQ-357 held-position clock | 10/14 08:30; card deadline | Same-date real/nominal split, followed by Will/TERRY review |
| October FOMC | 10/28 14:00 | Curve-shape prediction still owed by 10/21 |

The frozen 2dp bars govern, all comparisons strict: equality does not fire. Tomorrow's hand-grade fallback is explicitly selected and disclosed; the unrounded tool tie-band defect remains open. No new numerical trigger is introduced. Monitoring questions for the 10/14 read are whether declines in long real yields/term premium persist across completed observations, whether auction composition improves, and whether policy relief reaches the long end. A single intraday bounce would not settle those questions.

The October issuer auction PDF was inspected by page layout, confirming 20Y-R 10/21, 5Y TIPS 10/22, 2Y 10/26, 5Y 10/27, FRN 10/28, 7Y 10/29. TreasuryDirect's own upcoming-feed coverage remains short; the issuer-PDF verification is a separate method. Paid CDX, MBS OAS and comprehensive pulled-deal coverage remain absent. The HYG/IEF proxy is 0.8651, z20 +0.96 on the evolving 10/5 vendor bar; it is rate-confounded faster-cash evidence, not a synthetic-credit basis. EU/Japan/vol series remain with HANS/SAM/VIOLET; they were not independently refreshed here.
