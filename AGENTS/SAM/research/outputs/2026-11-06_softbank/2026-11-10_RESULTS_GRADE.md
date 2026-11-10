# SoftBank Q2 FY2026 results: graded against the 11/9 lookup

**Read:** 2026-11-10 10:04–10:11 ET (clock). The scheduled 02:47 ET pass fired at 10:04 ET, most likely because the laptop slept; the results had been out since 01:30 ET. **Owner:** SAM. $0. **Rules:** `2026-11-10_RESULTS_LOOKUP.md`, committed 11/9 before the print, applied as written (not re-tuned).

**Sources read at the primary (SBG IR, downloaded 11/10 ~10:05 ET, SHA-256 prefix):** earnings presentation `earnings-presentation_q2fy2026_01_en.pdf` (1e69c9ec) · investor briefing incl. Finance section `investor-presentation_q2fy2026_01_en.pdf` (a9c2649e) · SVF deck `investor-svf_q2fy2026_01_en.pdf` (19f59e21) · data sheet `earnings-datasheet_q2fy2026_02.pdf` (87990f8b) · financial report `financial-report_q2fy2026_01_en.pdf` (c3fa95f8). No separate finance deck this quarter (the Q1-style `investor-finance_` URL returns 404); the Finance section is inside the investor briefing. **Briefing transcript not yet published; one news search found no coverage of Gotō's remarks.**

## Grade: ✅ ESTIMATE CONFIRMED

| | Value | Basis |
|---|---|---|
| **SoftBank's reported LTV, 9/30** | **15.9%** = net debt **¥11.30T** ÷ equity value of holdings **¥71.14T** | Data sheet p.17; Finance 38/41. FX ¥157.35 |
| SoftBank's basis rolled to the read (Arm **$183.26**, vendor intraday 10:06 ET 11/10; USD/JPY 158.63) | **22.5%** (12.89 / 57.15) | `ltv_lookup.py --nd 11.30 --v 71.14 --arm 183.26 --fx 158.63 --svf2-inside` |
| My A figure at the same Arm price | **21.6%** (C 23.6%) | `ltv_lookup.py --nd 11.10 --v 72.86 --arm 183.26 --fx 158.63` |
| **Difference** | **+0.9 points**, inside ±1.5 | ✅ CONFIRMED |
| Quick-read check (headline only) | 15.9% sits inside the 14.0–16.5% confirm band | agrees; superseded by the calculator row above |
| At the lookup's reference price (Arm $187.71, fx 158.0) | SoftBank basis 22.3% vs my A 21.3%: +1.0 | same grade |
| **Arm price where SoftBank's own basis reaches 25%** | **$145** (35%: $44) | Arm $183.26 is 26% above |

**Not ≥25%: no over-ceiling packet is triggered.** The confirm is on the total, and the parts were both off and partly offsetting (below).

### What the model got wrong inside a confirmed total

| Input | My model (9/30) | Reported | Read |
|---|---|---|---|
| SVF2 $10B loan | Probably **outside** the ratio (KB-SAM-261 Notes) | **INSIDE**: definition item (j) "Inclusion of the outstanding balance of the loan using OpenAI shares held by SVF2 and guaranteed by SBG"; financing slide "Treated as SBG debt in the LTV calculation" | **Wrong.** View C's structure is SoftBank's own. Per the lookup, "A was the kind one" on structure |
| Net debt | 11.10 (A, ex-loan) / 12.69 (C, with loan) | **11.30** with the loan | My non-SVF2 net debt was about ¥1.4T too high |
| Equity value | 72.86 (A) / 74.45 (C) | **71.14** | About ¥3.3T too high on the C basis |
| Headline 9/30 | 15.2% (outside) / **17.0% (inside)** | **15.9%** | The correct-structure model (17.0%) was 1.1 points high |

Both input gaps are consistent with what the model said it could not see ("SVF and Others held at 6/30 except FX; monetizations unknown"): Q2 asset monetization (−2.1 points of LTV per SoftBank's Q2 bridge) and SVF distributions (−0.7) cut debt and value together. That reading is consistent with the bridge, not proven item by item.

## The four lookup figures

| # | Figure | Read |
|---|---|---|
| 1 | 9/30 LTV, net debt, value | **15.9% · ¥11.30T · ¥71.14T** (above). Net debt = consolidated 25.04 − self-financing entities 6.48 − other adjustments 7.25 (asset-backed +6.49, hybrid +0.76). Value: Arm 38.16 (42.06 gross − 3.90 margin loan), SBKK 3.42, T-Mobile 0.00 (collared out), SVF1/SVF2/LatAm 3.45/20.07/0.96, others 5.07 |
| 2 | SVF2 loan inside? | **YES** (above). Financial report: outstanding **¥1,543.7B** at 9/30, guaranteed by SBG; OpenAI shares not pledged; margining provisions reference OpenAI share value; 18 institutions incl. Goldman, JPMorgan, Mizuho, Apollo, SMBC |
| 3 | OpenAI fair value at 9/30 | **Unchanged in the quarter** (SVF deck: "OpenAI valuation unchanged"; "Unchanged Sep-26 Quarter Fair Value Change"). No mark-up, so none of the ~2.6-point no-cash relief. SVF2's OpenAI position as of 10/1, after the final tranche: cost **$65B**, unrealized fair value **$110B**, 1.7× |
| 4 | Pro forma / Gotō | SoftBank printed a **pro forma NAV ¥44.7T ($282B)** and equity value **¥56.0T** at **11/9 closes for Arm ($186.30), SBKK and Intel, FX 158.34, with 9/30 composition**. **It printed no pro forma LTV %**; the implied figure is **11.30 ÷ 56.0 = 20.2% (SAM arithmetic)**. ⚠️ That 20.2% **excludes the $10B October tranche** (¥1.57T at 157.35, funded 10/1, in Q3); adding it gives 22.4% at $186.30, matching my roll. **Gotō's spoken words: not read** (no transcript yet). Deck wording: "Maintain LTV below 25% in normal circumstances (upper threshold of 35% even in extraordinary circumstances)"; "Multiple LTV management measures are available": monetization, asset-backed finance, hybrid finance, adjusting investment pace. No sale of Arm, T-Mobile or SoftBank Corp announced in the deck |

**Roll cross-check:** SoftBank's pro forma equity value (¥56.0T) matches my calculator's Arm-only roll without the October tranche (¥56.03T at $186.30 / 158.34), so SBKK, Intel and FX moves since 9/30 net to about zero. ✅

## §6 read list (`SOFTBANK_FUNDING_STACK.md`)

| # | Read |
|---|---|
| 1 | 15.9% at 9/30; pro forma implied 20.2% ex-October tranche (above) |
| 2 | Inside (above) |
| 3 | SVF2 loan $10.0B raised in Q2 (¥1,573.5B at 157.35; ¥1,543.7B outstanding per the financial report). Referenced OpenAI fair value unchanged in Q2 |
| 4 | OpenAI flat at 9/30 |
| 5 | **Arm margin loan: facility $25B (+$5B, agreement Sep 2026), term 2 years with a one-year extension option, 41 institutions.** Drawn about **$24.8B** at 9/30 (the ¥3.90T asset-backed deduction at 157.35, SAM arithmetic). ⚠️ The "9/2027" maturity I carried from a relay does not match a two-year term from a Sep-2026 agreement (about 9/2028); pledged share count not read |
| 6 | **$11.9B "senior term loan borrowing"** listed under debt financing, not asset-backed, so **inside** net debt; borrower and collateral not stated. Apollo appears as a lender in the OpenAI-shares loan; no separate Apollo loan found in the deck. The 18.8% "if outside" branch is moot |
| 7 | **Cash position ¥5.0T ($32B) vs ¥1.6T of bond redemptions over the next two years** (6/30: ¥2.3T vs ¥1.5T) |
| 8 | ABB robotics: still upcoming, **$5.4B "Q3 onwards"**, about $1.8B of it from LBO finance. ⚠️ Not in my roll: if it closes debt-funded at cost, about +1.2 points on SoftBank's basis (rough SAM arithmetic; the LBO portion may sit outside) |
| 9 | Guarantees: the financial report names the SBG guarantee of the SVF2 OpenAI-shares loan. **No SBG guarantee of SB Energy obligations found** (zero "SB Energy" hits in the financial report). Deck: SBG committed $3.0B to SB Energy ($1.5B funded); the PORTS-Pike credit support is NVIDIA's. **Musk turbine claim (card 20261109-005): no route to SoftBank's leverage found in these documents** |
| 10 | $1.25T round: nothing new found in the deck. VULCAN owns terms |
| 11 | Gotō: transcript not read (above) |

**Other figures (Q2, financial report):** six-month net income attributable to owners **−¥768.0B** (prior year +¥2,924.1B); total assets ¥69.39T; equity ratio 23.6% (29.0% at 3/31). SBG 9984.T closed **¥3,872, +13.88%** on 11/10 (vendor; Tokyo close, read after it).

## Japan consequence

Unchanged. SoftBank's own basis is under its 25% normal-times ceiling at today's Arm (22.5% rolled, Arm $145 for 25%). No rating action or pulled yen retail deal read; the deck cites a **¥1T retail bond issuance record (70th domestic senior "Fukuoka SoftBank Hawks Bonds")**, which is retail demand, not withdrawal. Combo theme KB-SAM-262: no member moves the read.

## Kill-on-sight check

This write-up does not say "SoftBank reported 22%": SoftBank reported **15.9% at 9/30**; 22.5% is **SAM's roll-forward** of SoftBank's figures to Arm $183.26. "Leverage is 13%" appears only as the 6/30 print. No "$40B bridge wall" (repaid 9/15; facility terminated 9/30, deck Finance 8). The 9/30 15.9% is not presented as today's leverage.
